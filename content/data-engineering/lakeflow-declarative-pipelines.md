---
title: "Lakeflow Declarative Pipelines: From DLT to Production"
date: 2026-04-06T18:00:00+00:00
draft: false
tags: ["databricks", "lakeflow", "dlt", "pipeline", "data-engineering", "etl"]
lastmod: 2026-09-26T09:00:00+01:00
description: "From Delta Live Tables to Lakeflow Declarative Pipelines: how declarative ETL patterns have evolved and how to design production pipelines in 2026."
slug: "lakeflow-declarative-pipelines-2026"
cover:
  image: /assets/images/data-engineering/data.jpg
  alt: Lakeflow Declarative Pipelines
---

## TL;DR

- Lakeflow Declarative Pipelines is Delta Live Tables renamed (June 2025), and the same engine was contributed to Apache Spark as Spark Declarative Pipelines, so the pattern is no longer Databricks-only
- The three core building blocks are streaming tables (incremental, append-only sources), materialized views (refreshed incrementally where the query allows, fully recomputed otherwise), and AUTO CDC for slowly-changing dimensions without hand-rolled merge logic
- Physical optimisation is increasingly automatic in 2026 - liquid clustering is the recommended layout, predictive optimization handles maintenance, and Z-order is legacy
- Keep hand-rolled Spark jobs for imperative control flow, heavy external API enrichment, and ML workloads; Lakeflow is for dataset-shaped data movement
- Lakeflow and dbt are complementary rather than competitors - some teams use Lakeflow for ingestion to silver and dbt for silver-to-gold

If you've been writing Delta Live Tables (DLT) pipelines, you've been building with Lakeflow without knowing the new name. Databricks renamed DLT at Data + AI Summit in June 2025, and at the same time [contributed the engine to Apache Spark as Spark Declarative Pipelines](https://www.infoq.com/news/2025/07/databricks-declarative-pipelines), which ships as a native capability in [Apache Spark 4.1](https://www.databricks.com/discover/how-to-get-started-with-spark-declarative-pipelines).

The syntax you know still works. What changed is the packaging, the tooling around it, and a few newer building blocks worth knowing. Let me show you what changed and why it matters. For where Lakeflow fits relative to other orchestration choices and the broader paradigm question, see [The modern lakehouse stack](/data-engineering/modern-lakehouse-stack/) and [Stream vs batch processing](/data-engineering/stream-vs-batch-processing/).

## What Lakeflow Actually Is

Lakeflow Declarative Pipelines is the modern Databricks way to say: "I describe what data I want, and Databricks manages how to get it."

You define:
- **Datasets** (streaming tables, materialized views, and temporary or private views)
- **Dependencies** (what feeds what)
- **Update semantics** (incremental, CDC, append-only, etc.)

Databricks handles:
- Orchestration (running transformations in dependency order)
- Incremental execution (only processing new or changed data)
- Performance optimization (caching, clustering, partitioning)
- Error handling and recovery
- Scaling (serverless or classic pipeline compute)

This is declarative programming applied to data pipelines. You say *what*, not *how*.

## Why This Matters: The Evolution from DLT

### The Old DLT Syntax (2022–2024)

```sql
CREATE OR REFRESH STREAMING LIVE TABLE bronze_events AS
  SELECT * FROM cloud_files('s3://raw-bucket/events/', 'json');

CREATE OR REFRESH LIVE TABLE silver_events AS
  SELECT event_id, event_type, event_ts, user_id
  FROM LIVE.bronze_events
  WHERE event_id IS NOT NULL;
```

This still works, but it had rough edges:

- **Naming was confusing.** "Delta Live Tables" doesn't communicate the pattern as clearly as "declarative pipelines", and the `LIVE` keyword leaked into every query.
- **It was Databricks-only.** The pattern couldn't be run or tested outside the platform.
- **CDC was verbose.** `APPLY CHANGES INTO` worked, but read like a bolt-on.
- **Outputs were tables only.** Writing to Kafka or an external Delta location meant leaving the pipeline.

### What Actually Changed (2025–2026)

```sql
CREATE OR REFRESH STREAMING TABLE bronze_events AS
  SELECT * FROM STREAM read_files('s3://raw-bucket/events/', format => 'json');

CREATE OR REFRESH MATERIALIZED VIEW silver_events AS
  SELECT event_id, event_type, event_ts, user_id
  FROM bronze_events
  WHERE event_id IS NOT NULL;
```

The practical changes:

- **`STREAMING TABLE` and `MATERIALIZED VIEW` are the vocabulary.** The `LIVE` keyword is no longer needed.
- **An open-source core.** Spark Declarative Pipelines means the same SQL and Python definitions can run on open-source Spark 4.1, with Databricks adding the managed runtime, serverless compute, and UI.
- **A new Python module.** Python pipelines use `pyspark.pipelines` (conventionally `from pyspark import pipelines as dp`) rather than the old `dlt` module.
- **`AUTO CDC`** replaces `APPLY CHANGES INTO` as the recommended CDC API.
- **Sinks** let a flow write to Kafka, Event Hubs, or external Delta tables, so fan-out no longer means leaving the pipeline.
- **A dedicated pipeline editor** with a dependency graph, per-dataset previews, and runs of a single table.

## Key Concepts in Lakeflow 2026

### 1. Streaming Tables (Append-Only)

Use when: New data is appended; you never update or delete old records.

```sql
CREATE OR REFRESH STREAMING TABLE raw_events AS
  SELECT * FROM STREAM read_files('s3://bucket/events/', format => 'json');
```

- Each record from the source is processed exactly once
- Checkpointed for recovery
- Ideal for event data, logs, telemetry

**When to use:** Events, clicks, API calls, anything that's append-only and time-ordered.

### 2. Materialized Views (Always Correct, Incremental Where Possible)

Use when: The result must always reflect the current source data, including updates and deletes, and you want the platform to decide how to refresh it.

```sql
CREATE OR REFRESH MATERIALIZED VIEW user_daily_summary AS
  SELECT 
    user_id,
    DATE(event_ts) AS event_date,
    COUNT(*) AS event_count
  FROM raw_events
  GROUP BY user_id, DATE(event_ts);
```

- On serverless, refreshes are **incremental when the query allows it** (aggregations, joins, filters over Delta sources) and fall back to a full recompute otherwise
- Non-deterministic functions such as `current_date()` force a full recompute, which is worth knowing before you put a rolling window in an MV
- Correct under source updates and deletes, which streaming tables are not
- Great for aggregations, joins, and gold-layer tables

**When to use:** Dashboards, aggregations, joins, and derived metrics refreshed on a schedule or when upstream data changes.

### 3. AUTO CDC (Change Data Capture)

Use when: Source data is being updated/deleted and you need to track those changes in your lakehouse.

```sql
CREATE OR REFRESH STREAMING TABLE users_scd2;

CREATE FLOW user_cdc AS
  AUTO CDC INTO users_scd2
  FROM stream(bronze_users_cdf)
  KEYS (user_id)
  SEQUENCE BY update_timestamp
  STORED AS SCD TYPE 2;
```

- Tracks inserts, updates, deletes from source system
- Produces SCD Type 2 slowly-changing dimensions
- Maintains `__START_AT` and `__END_AT` columns automatically
- Easier than hand-rolling merge logic

**When to use:** Syncing databases, data warehouses, CRM data - anything that mutates at the source.

### 4. Private Datasets

For intermediate transformations that shouldn't be published to the catalog:

```sql
CREATE PRIVATE MATERIALIZED VIEW users_deduped AS
  SELECT * FROM bronze_users
  QUALIFY ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY updated_at DESC) = 1;

CREATE TEMPORARY VIEW active_users AS
  SELECT * FROM users_deduped WHERE status = 'active';
```

Private datasets exist only for the pipeline's use (older docs call them temporary tables), and temporary views aren't materialised at all. Both help organise complex pipelines without cluttering the catalog.

## Pattern: Building a Production Lakeflow Pipeline

Here's how a modern 2026 pipeline looks:

```sql
-- BRONZE: Raw ingestion
CREATE OR REFRESH STREAMING TABLE bronze_events AS
  SELECT * FROM STREAM read_files(
    's3://raw-bucket/events/',
    format => 'json',
    schema => 'event_id STRING, user_id STRING, event_ts TIMESTAMP, properties STRING'
  );

-- SILVER: Cleaned, typed, deduplicated
CREATE OR REFRESH MATERIALIZED VIEW silver_events AS
  SELECT 
    event_id,
    user_id,
    event_ts,
    from_json(properties, 'key STRING, value STRING') AS properties
  FROM bronze_events
  WHERE event_id IS NOT NULL AND user_id IS NOT NULL
  QUALIFY ROW_NUMBER() OVER (PARTITION BY event_id ORDER BY event_ts) = 1;

-- GOLD: Business logic (daily aggregation)
CREATE OR REFRESH MATERIALIZED VIEW gold_daily_events AS
  SELECT 
    DATE(event_ts) AS event_date,
    user_id,
    COUNT(*) AS event_count,
    COUNT(DISTINCT event_id) AS unique_event_count
  FROM silver_events
  GROUP BY DATE(event_ts), user_id;

-- CDC Example: Syncing a mutable source
CREATE OR REFRESH STREAMING TABLE bronze_users_changes AS
  SELECT * FROM STREAM read_files('s3://raw-bucket/users-cdc/', format => 'json');
  -- each record carries an operation column (INSERT/UPDATE/DELETE) and a change timestamp

CREATE OR REFRESH STREAMING TABLE silver_users;

CREATE FLOW silver_users_cdc AS
  AUTO CDC INTO silver_users
  FROM STREAM(bronze_users_changes)
  KEYS (user_id)
  APPLY AS DELETE WHEN operation = 'DELETE'
  SEQUENCE BY change_ts
  COLUMNS * EXCEPT (operation, change_ts)
  STORED AS SCD TYPE 1;
```

**Pattern principles:**

1. **Bronze = Raw** (minimal transformation, just schema validation)
2. **Silver = Clean** (deduplication, type casting, filtering nulls)
3. **Gold = Ready** (business aggregations, denormalization for BI)
4. **Use streaming for immutable appends; materialized views for computed aggregations**
5. **Let AUTO CDC handle ordering and deletes** (sequence by a reliable change timestamp, never by ingestion time)

## Lakeflow vs Hand-Rolled Spark Jobs

When would you *not* use Lakeflow?

### Use Spark Jobs (Not Lakeflow) When:

- **Complex imperative control flow** (loops, branching on runtime results, orchestration logic)
- **Heavy external enrichment** (per-record API calls with rate limits and retries are easier to own in a job you control)
- **Non-dataset side effects** (sending notifications, calling operational APIs)
- **GPU/ML training workloads** (Lakeflow is for data movement; training lives elsewhere)

Multiple outputs are no longer a reason to leave: a pipeline can have several flows writing to one target, and sinks can write to Kafka or external Delta tables.

```python
# A Spark job for API enrichment: batch per partition, reuse one HTTP session
import pandas as pd
import requests
from requests.adapters import HTTPAdapter, Retry

def enrich(batches):
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=Retry(total=5, backoff_factor=0.5)))
    for pdf in batches:
        ids = pdf["user_id"].unique().tolist()
        resp = session.post("https://api.company.com/users/batch", json={"ids": ids}, timeout=30)
        resp.raise_for_status()
        profiles = pd.DataFrame(resp.json())  # user_id, segment
        yield pdf.merge(profiles, on="user_id", how="left")

events = spark.read.table("main.silver.events")
enriched = events.mapInPandas(enrich, schema=events.schema.add("segment", "string"))
enriched.write.mode("overwrite").saveAsTable("main.silver.enriched_events")
```

`mapInPandas` works on standard and serverless compute (RDD APIs don't), and batching per partition keeps you inside the API's rate limits.

**Rule of thumb:** If your transformation can be expressed as datasets and their dependencies, use Lakeflow. If it needs control flow, side effects, or tight control over external calls, use a Spark job orchestrated alongside it in Lakeflow Jobs.

## Performance and Cost Considerations

### Streaming Tables vs Materialized Views: Cost Tradeoffs

| Aspect | Streaming Tables | Materialized Views |
|:---|:---|:---|
| **Processing** | Incremental (each new record once) | Incremental where possible, full recompute otherwise |
| **Handles source updates/deletes** | No (append-only semantics) | Yes |
| **Latency** | Lower (continuous or frequent) | Depends on refresh schedule or trigger |
| **Best for** | Ingestion, event data, logs | Aggregations, joins, gold tables, BI |
| **Example** | Raw events ingestion | Daily user summary |

### Optimization in Lakeflow (2026)

Lakeflow now handles much of this automatically:

- **Liquid clustering** is the recommended layout for new tables (automatic clustering can pick keys for you)
- **Predictive optimization** runs maintenance automatically
- **Skipping files** based on statistics (Z-order is legacy)

```sql
CREATE OR REFRESH STREAMING TABLE events
CLUSTER BY (user_id, event_date);  -- Liquid clustering, not partitions
```

You still need to understand the tradeoff (streaming incremental vs materialized full-recompute), but the physical optimization is handled.

### Monitoring and Cost Tracking

In 2026, Lakeflow pipelines expose cost metrics:

- **Compute cost** per pipeline run
- **Storage cost** for each table and intermediate result
- **Data scan volume** to understand shuffle and network costs

This makes it clear which transformations are expensive:

- Is your materialized view falling back to a full recompute? (Check the refresh details in the event log; non-deterministic functions are a common cause)
- Is your streaming table checkpointing massive state? (Check the intermediate storage)
- Are you recalculating data that could be cached? (Use materialized views + clustering)

## Testing Lakeflow Pipelines

Declarative pipelines are easier to test than Spark jobs because they're mostly SQL. But testing still matters.

### Data Quality Checks With Expectations

Expectations are the built-in way to assert data quality, and they're recorded in the pipeline event log:

```sql
CREATE OR REFRESH MATERIALIZED VIEW silver_events (
  CONSTRAINT valid_ids EXPECT (event_id IS NOT NULL AND user_id IS NOT NULL) ON VIOLATION DROP ROW,
  CONSTRAINT sane_timestamps EXPECT (event_ts > '2020-01-01') ON VIOLATION FAIL UPDATE
) AS
  SELECT * FROM bronze_events;
```

### Assertion Queries

After a refresh, simple queries catch logic errors (each should return zero rows):

```sql
-- Duplicates survived deduplication
SELECT event_id, COUNT(*) FROM silver_events GROUP BY event_id HAVING COUNT(*) > 1;

-- Nulls survived filtering
SELECT * FROM silver_events WHERE event_id IS NULL OR user_id IS NULL;
```

### Integration Test Pattern

Pipeline-managed tables can't be truncated or written to from outside the pipeline, so test by running the same pipeline definition against fixture data:

1. Parameterise the source path and target schema in your bundle configuration
2. Deploy a `test` target that points the source at a small fixture folder in a volume
3. Run it with `databricks bundle run` and then execute the assertion queries above against the test schema

## The Operational Picture: From Lakeflow to Production

### Development → Staging → Production

Environments are separate deployments of the same pipeline definition, not separate tables inside one pipeline. Databricks Asset Bundles handle this with targets:

```yaml
# databricks.yml (excerpt)
targets:
  dev:
    variables:
      catalog: dev
      source_path: /Volumes/dev/landing/events_sample/
  prod:
    variables:
      catalog: prod
      source_path: s3://raw-events/
```

Pipeline infrastructure supports:
- **Multi-workspace deployment** (dev workspace, prod workspace)
- **Git integration** (Git folders and bundles in CI/CD)
- **Notifications** (email or webhook alerts on pipeline failure)
- **Triggered or continuous runs** (on schedule, on file arrival, or always on)

## Lakeflow vs dbt

In 2026, you might ask: "Should I use Lakeflow or dbt?"

**They're complementary, not competitors:**

| Aspect | Lakeflow | dbt |
|:---|:---|:---|
| **Native to** | Databricks | Any data warehouse |
| **Orchestration** | Built-in (Lakeflow service) | dbt Cloud, Airflow/Dagster, or a dbt task in Lakeflow Jobs |
| **Incremental logic** | Managed by the engine (streaming, CDC, incremental MVs) | Native incremental models, but you write the merge/filter logic |
| **Testing** | SQL assertions and expectations | dbt tests, great dbt ecosystem |
| **Best for** | Databricks-native workflows | Multi-warehouse, BI-heavy stacks |

**Use Lakeflow if:** You're all-in on Databricks and want the simplest path to production.

**Use dbt if:** You have multiple data warehouses, need stronger testing, or want portable SQL transformations.

**Use both if:** Lakeflow for ingestion to silver, dbt for silver-to-gold transformations (some teams do this).

## The Future of Lakeflow (2026 and Beyond)

What's coming:

- **AI-assisted pipeline generation** (describe your data, Databricks generates the SQL)
- **Finer cost tracking** (optimize specific transformations)
- **Broader federation** (more Lakehouse Federation sources usable inside pipelines)
- **Better testing frameworks** (built-in data quality tools)
- **Streaming SQL improvements** (more flexible windowing and stateful operations)

The direction is clear: make declarative pipelines the default path, and push complexity (ML, external APIs, GPU workloads) to specialized tools.

## Putting It Together: A Real Example

Building a recommendation engine's featurization pipeline:

```sql
-- BRONZE: Raw events
CREATE OR REFRESH STREAMING TABLE bronze_events AS
  SELECT * FROM STREAM read_files('s3://events/', format => 'parquet');

-- SILVER: Validated events
CREATE OR REFRESH STREAMING TABLE silver_events AS
  SELECT 
    event_id,
    user_id,
    product_id,
    event_type,
    event_ts,
    CURRENT_TIMESTAMP() AS processed_ts
  FROM stream(bronze_events)
  WHERE user_id IS NOT NULL 
    AND product_id IS NOT NULL
    AND event_ts > CURRENT_TIMESTAMP() - INTERVAL 1 YEAR;

-- GOLD: 30-day user features
CREATE OR REFRESH MATERIALIZED VIEW gold_user_features AS
  SELECT 
    user_id,
    COUNT(*) AS events_30d,
    COUNT(DISTINCT product_id) AS products_viewed_30d,
    COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) AS purchases_30d,
    COUNT(CASE WHEN event_type = 'view' THEN 1 END) AS views_30d,
    MAX(event_ts) AS last_event_ts
  FROM silver_events
  WHERE event_ts >= DATE_SUB(CURRENT_DATE(), 30)  -- current_date() means this MV fully recomputes
  GROUP BY user_id;

-- GOLD: Product popularity (hourly)
CREATE OR REFRESH MATERIALIZED VIEW gold_product_popularity AS
  SELECT 
    product_id,
    DATE_TRUNC('hour', event_ts) AS hour,
    COUNT(*) AS event_count,
    COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) AS purchases
  FROM silver_events
  WHERE event_ts >= DATE_SUB(CURRENT_DATE(), 7)
  GROUP BY product_id, DATE_TRUNC('hour', event_ts);
```

**This entire pipeline is:**
- Automatically orchestrated (dependencies detected)
- Incrementally processed where possible (streaming tables always; the MVs here recompute because of the rolling window)
- Monitored (metrics, lineage, cost tracked)
- Scalable (from notebook to production cluster)

And you wrote pure SQL. No Spark tuning, no cluster management, no orchestration code.

That's the promise of Lakeflow.

---

*Last Updated: September 26, 2026*

## Related Reading

- [Data Engineering & Data Science Courses](/data-engineering/data-engineering-science-courses/)
- [Modern Data Engineering on Databricks (2026 Guide)](/data-engineering/modern-data-engineering-databricks-2026/)
- [Databricks Training & Certification](/data-engineering/databricks-training-certification/)
- [ETL Tools & Data Integration Platforms](/data-engineering/etl-tools/)
