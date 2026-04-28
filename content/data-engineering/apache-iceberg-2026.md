---
title: "Apache Iceberg in 2026: The Open Table Format That Won"
date: 2026-04-22T07:53:00+01:00
draft: false
tags: ['iceberg', 'lakehouse', 'open-source', 'data-engineering', 'table-format', 'catalog']
description: "A technical deep dive into Apache Iceberg in 2026 - how the metadata layer works, catalog choices (Polaris, Nessie, Unity), migration patterns, and why both Snowflake and Databricks now treat it as first-class."
slug: "apache-iceberg-2026"
cover:
  image: /assets/images/data-engineering/apache-iceberg-2026.jpg
  alt: Apache Iceberg in 2026
---

In 2023, the question was "which open table format will survive - Iceberg, Delta, or Hudi?" In 2026, that debate is over. Apache Iceberg won, and it won for reasons that have almost nothing to do with its raw performance.

It won because it is the only format that **both Snowflake and Databricks now treat as a first-class citizen**, because the vendors picked sides on catalogs rather than table formats, and because enterprise buyers decided that multi-engine portability was worth more than a small performance edge.

If your existing understanding of Iceberg stops at "it's like Parquet but better," this post is the technical grounding you need. For where it sits in the wider 2026 platform picture, see [The modern lakehouse stack](/data-engineering/modern-lakehouse-stack/).

## What Apache Iceberg Actually Is

Iceberg is **not a storage format**. It is a **table format** - a metadata specification that sits on top of open file formats like Parquet, ORC, or Avro.

The distinction matters. A Parquet file describes a single immutable chunk of columnar data. A table is usually thousands of those files, and the table format is the rulebook for answering questions like:

- Which files belong to this table right now?
- Which files belonged to this table ten minutes ago?
- What schema applied when these files were written?
- How do I commit a write atomically without another reader seeing a half-written state?

Iceberg answers these via a layered metadata tree stored alongside your data files in object storage.

### The Three Metadata Layers

```
s3://my-bucket/warehouse/db/table/
 - data/
    - 00000-0-abc.parquet
    - 00001-0-def.parquet
 - metadata/
    - v1.metadata.json        (table metadata)
    - snap-123.avro           (manifest list)
    - manifest-abc.avro       (manifest file)
```

1. **Table metadata** (`vN.metadata.json`) - the current schema, partition spec, snapshot history, and a pointer to the latest snapshot.
2. **Manifest list** (one per snapshot) - an inventory of manifest files that make up that snapshot, with partition-level summary statistics.
3. **Manifest files** - the actual list of data files in a partition, with per-file column stats (min/max, null counts, row counts).

A read plan walks this tree top-down and uses the stats at each level to prune files before reading any Parquet. That is how Iceberg delivers fast queries on tables with billions of rows across hundreds of thousands of files.

## Why Iceberg Beat Delta Lake and Hudi

All three formats solved roughly the same problems: ACID transactions on object storage, schema evolution, time travel, and efficient reads. Technically, they are closer than their marketing suggests. So why did Iceberg take the lead?

### 1. Governance, Not Databricks

Delta Lake was donated to the Linux Foundation in 2019, but it always had a Databricks center of gravity. New features landed in Databricks first, then trickled into open-source Delta months later. Iceberg was built inside Netflix and Apple, donated to the [Apache Software Foundation](https://iceberg.apache.org/) in 2018, and has never had a single dominant vendor. That neutrality is what convinced Snowflake, AWS, Google, and eventually Databricks to back it.

### 2. True Engine Portability

An Iceberg table written by Spark can be read by Trino, StarRocks, DuckDB, Flink, Snowflake, and Dremio **without conversion**. Delta had similar ambitions with its UniForm feature, but the semantics are a superset-of-Delta flavor of Iceberg, not pure Iceberg. If you want any engine to write to your tables (not just read), Iceberg is the only format where that works cleanly today.

### 3. Hidden Partitioning

Hive-style partitioning requires the query writer to know the physical layout. If a table is partitioned by `event_date`, a query filtering on `event_ts > '2026-01-01'` will scan the whole table unless the user manually derives the partition column.

Iceberg introduced **hidden partitioning** via partition transforms:

```sql
CREATE TABLE events (
  event_id BIGINT,
  event_ts TIMESTAMP,
  user_id STRING
)
USING iceberg
PARTITIONED BY (days(event_ts));
```

The query writer filters on `event_ts` and Iceberg figures out which day-partitions to read. You can also **evolve the partition spec** - switch from daily to hourly partitioning - without rewriting historical data. Old snapshots keep their old spec, new ones use the new spec, and reads work across the boundary.

This single feature made long-lived Iceberg tables much cheaper to operate than Hive-style Delta or Parquet tables.

### 4. The Vendors Moved the Fight to Catalogs

The most interesting strategic shift in 2024-2025 was that the major vendors **stopped fighting over the table format and started fighting over the catalog**. Once Snowflake announced Polaris and Databricks opened Unity Catalog, the question wasn't "Delta or Iceberg?" anymore. It was "whose catalog will you use to govern your Iceberg tables?" Iceberg became the assumed substrate.

## The Catalog Question

An Iceberg table on its own is just files in a bucket. Something has to own the mapping of `catalog.schema.table` to the current metadata pointer. That something is a **catalog**, and it is where the interesting design decisions live in 2026.

### Polaris Catalog (Snowflake)

[Polaris](https://www.snowflake.com/en/data-cloud/polaris/) is Snowflake's open-source Iceberg catalog, donated to the Apache Software Foundation in mid-2024. It implements the Iceberg REST catalog spec and supports cross-engine read and write. Snowflake uses it as the substrate for its own Iceberg tables and positions it as vendor-neutral.

**Strength:** true REST-catalog standardization; no Snowflake lock-in on the catalog layer itself.

**Watch for:** operational maturity compared to Unity Catalog.

### Unity Catalog (Databricks)

Databricks open-sourced [Unity Catalog](https://www.unitycatalog.io/) in June 2024. The open-source version supports Iceberg tables via the REST catalog spec; the managed Databricks version adds lineage, governance, and AI asset support on top. In 2026 it is the richest governance catalog, but the open-source feature gap is still meaningful.

**Strength:** governance, lineage, and ML model support in one place.

**Watch for:** differences between OSS Unity and the Databricks-managed version.

### Project Nessie

[Nessie](https://projectnessie.org/) takes a different approach: Git-like branching and merging for data. You can create a `dev` branch off `main`, run a test pipeline, validate the results, and merge the snapshot back - with full rollback. For teams that want to version data the way they version code, Nessie is the most interesting catalog on the market.

**Strength:** branching, tagging, and transactional multi-table commits.

**Watch for:** smaller ecosystem and fewer managed-service options.

### AWS Glue and REST Catalogs

AWS Glue Data Catalog has supported Iceberg tables since 2022 and is the default for Iceberg workloads on AWS. In 2026, most modern engines speak the [Iceberg REST catalog spec](https://iceberg.apache.org/spec/#appendix-a-format-version), which means you can point the same engine at Polaris, Unity, Nessie, or Glue with a config change.

### Which to Choose

- You live on Snowflake, and want Iceberg portability - **Polaris**.
- You live on Databricks - **Unity Catalog** (managed).
- You want Git-style data versioning - **Nessie**.
- You want a minimal, AWS-native option - **Glue** with Iceberg tables.
- You are multi-engine and vendor-neutral is the top priority - **Polaris OSS** or **Unity OSS**, with the REST spec as your contract.

## Reading and Writing Iceberg in 2026

### From Spark

```python
spark.sql("""
  CREATE TABLE local.db.events (
    event_id BIGINT,
    user_id STRING,
    event_ts TIMESTAMP,
    properties MAP<STRING, STRING>
  )
  USING iceberg
  PARTITIONED BY (days(event_ts))
""")

spark.sql("""
  INSERT INTO local.db.events VALUES
    (1, 'user-1', TIMESTAMP '2026-04-22 10:00:00', MAP('source', 'web'))
""")
```

### From Trino

```sql
SELECT user_id, COUNT(*) AS event_count
FROM iceberg.db.events
WHERE event_ts > TIMESTAMP '2026-04-01 00:00:00'
GROUP BY user_id;
```

### From Snowflake

```sql
CREATE ICEBERG TABLE events
  CATALOG = 'my_polaris_catalog'
  BASE_LOCATION = 'events';

SELECT user_id, COUNT(*) FROM events
WHERE event_ts > '2026-04-01'
GROUP BY user_id;
```

### From DuckDB

```sql
INSTALL iceberg;
LOAD iceberg;

SELECT * FROM iceberg_scan('s3://my-bucket/warehouse/db/events');
```

Same table, same metadata, four engines. That is the portability story that Delta Lake cannot match today.

## Schema Evolution Without Rewrites

Schema evolution is one of Iceberg's most underrated features. Because every column has a stable internal ID (separate from its name), you can safely:

- **Rename columns** without rewriting data
- **Drop columns** without breaking old snapshots
- **Reorder columns** without corrupting reads
- **Promote types** (int to long, float to double) without rewriting
- **Add columns** with no data movement at all

```sql
ALTER TABLE events ADD COLUMN session_id STRING;
ALTER TABLE events RENAME COLUMN properties TO event_properties;
ALTER TABLE events ALTER COLUMN event_id TYPE BIGINT;
```

Each of these is a metadata-only operation. A one-billion-row table evolves its schema in milliseconds.

Delta Lake supports most of these too, but Iceberg's column-ID approach is architecturally cleaner and avoids a class of edge cases around rename-then-add-with-same-name.

## Time Travel and Rollback

Every write creates a new snapshot. Every snapshot is queryable.

```sql
-- Snapshot by ID
SELECT * FROM events VERSION AS OF 7821394123987;

-- Snapshot by timestamp
SELECT * FROM events TIMESTAMP AS OF '2026-04-20 09:00:00';

-- Diff between two snapshots
SELECT * FROM events.changes
WHERE snapshot_id BETWEEN 7821394123987 AND 7821394123988;

-- Rollback a bad write
CALL system.rollback_to_snapshot('db.events', 7821394123987);
```

This is useful for debugging bad pipeline runs, reproducing model-training inputs, and satisfying regulatory "what did this table look like on date X" questions.

**Gotcha:** snapshots pin data files. If you want to reclaim storage, you have to **expire old snapshots** explicitly:

```sql
CALL system.expire_snapshots('db.events', TIMESTAMP '2026-01-01 00:00:00');
```

Most managed catalogs now do this automatically, but self-hosted Iceberg deployments frequently blow up their storage bill by forgetting.

## Migration Patterns: Hive or Delta to Iceberg

### From Hive-Style Parquet

Iceberg supports in-place migration for tables that already follow Hive partition conventions:

```sql
CALL system.migrate('hive_catalog.db.events');
```

The files stay where they are; Iceberg writes metadata on top. This is a metadata-only operation, which means it is fast even for petabyte-scale tables. The risk is that any external writer still writing Hive-style into those paths will produce files Iceberg's metadata doesn't know about.

### From Delta Lake

Two options:

1. **Full rewrite** with `CREATE TABLE ... AS SELECT * FROM delta_table` - safest, slowest.
2. **Delta UniForm** - write Iceberg metadata alongside Delta metadata so both formats see the same table. Good for staged migrations but doubles your metadata write cost.

In practice, most teams doing a serious Delta-to-Iceberg move rewrite once during a maintenance window. The CAS-based approach is simpler to reason about than maintaining dual metadata.

### Operational Reality

- Expect **two weeks** to migrate a single mid-sized warehouse (100 TB), most of which is validation and ETL job cutover rather than the actual data move.
- **Permissions do not migrate.** Re-grant explicitly in your new catalog.
- **Dashboards and BI tools** need their connections repointed. This is usually the slowest step.

## The Compaction Problem

Iceberg inherits object-storage's biggest operational challenge: small files.

A streaming pipeline committing every minute produces ~1,440 tiny files per day per partition. Reads get slower, metadata gets bloated, and query planning dominates runtime. The fix is compaction:

```sql
CALL system.rewrite_data_files(
  table => 'db.events',
  options => map('target-file-size-bytes', '536870912')
);
```

This rewrites small files into 512 MB chunks. In 2026, most managed services (Databricks predictive optimization, Snowflake's managed Iceberg, Tabular, Estuary) run compaction automatically. If you are self-hosting, schedule it explicitly or your tables will degrade within weeks.

## Row-Level Deletes: Copy-on-Write vs Merge-on-Read

Iceberg v2 introduced two strategies for deletes and updates:

**Copy-on-write (CoW):** rewrite the affected files on every update. Fast reads, expensive writes. Good for mostly-append tables.

**Merge-on-read (MoR):** write a separate delete file pointing to which rows are dead. Fast writes, slower reads (the engine reconciles at query time). Good for CDC and high-update workloads.

```sql
ALTER TABLE events SET TBLPROPERTIES (
  'write.delete.mode' = 'merge-on-read',
  'write.update.mode' = 'merge-on-read'
);
```

Iceberg v3 (finalized in 2025) introduced **variant encoding** for deletes and **row lineage** tracking, which cut MoR read overhead substantially. If you are on v2, the v3 upgrade is worth prioritizing for update-heavy tables.

## When Not to Use Iceberg

Iceberg is the right default for analytical tables on object storage. It is the wrong choice for:

- **OLTP workloads.** Iceberg is not a transactional database. If you need single-row lookups by primary key at sub-millisecond latency, use Postgres or a key-value store.
- **Tiny tables.** The metadata overhead isn't worth it for tables under ~1 GB. Use a plain Parquet file or a managed warehouse table.
- **Extremely low-latency streaming sinks.** Iceberg commit latency is seconds, not milliseconds. For sub-second freshness requirements, write to Kafka or a streaming-native sink and compact into Iceberg downstream.
- **Single-engine environments where you already pay for a warehouse.** If everything lives inside Snowflake and will stay there, native Snowflake tables are simpler.

## The 2026 Reference Stack

If I were designing an open lakehouse today:

```
Storage       - S3 / ADLS / GCS (Parquet)
Table format  - Apache Iceberg v3
Catalog       - Polaris (if Snowflake) | Unity OSS (if Databricks) | Nessie (if Git-style)
Compute (SQL) - Trino or StarRocks for interactive; Spark for heavy ETL
Streaming     - Kafka to Iceberg via Flink or Estuary
Orchestration - Dagster or Airflow 3
Transformation- dbt or SQLMesh, targeting the Iceberg catalog directly
BI            - Any tool with an Iceberg or Trino connector
```

The point of this stack is that **every layer is replaceable**. Change the compute engine, keep the data. Change the catalog, keep the files. Change the storage provider, keep the metadata. That is the property that made Iceberg the default choice for enterprise architects who lived through one too many vendor lock-in cycles.

## Final Thought

Iceberg winning was not inevitable. Delta Lake had a two-year head start and the backing of the dominant lakehouse vendor. Hudi had better streaming semantics for years. Iceberg won because its governance model, its metadata design, and its catalog ecosystem all pointed in the same direction: **the table format should be the boring part of your stack**.

In 2026, that is exactly what it is. You will spend your design time arguing about catalogs, compute engines, and transformation frameworks - not about whether your files are readable in five years. That is the quiet success of an open standard.

## Useful Resources

- [Apache Iceberg official documentation](https://iceberg.apache.org/)
- [Iceberg table spec](https://iceberg.apache.org/spec/)
- [Iceberg REST catalog spec](https://iceberg.apache.org/spec/#appendix-a-format-version)
- [Polaris Catalog on GitHub](https://github.com/apache/polaris)
- [Unity Catalog OSS](https://www.unitycatalog.io/)
- [Project Nessie](https://projectnessie.org/)
- [Dremio's Iceberg guide](https://www.dremio.com/resources/guides/apache-iceberg/)
- [Tabular's Iceberg internals series](https://tabular.io/blog/)

---

**Related Posts:**
- [Databricks vs Snowflake in 2026: An Honest Comparison](/data-engineering/databricks-vs-snowflake-2026/)
- [Following the Money: Databricks vs Snowflake vs the Open-Source Alternative](/data-engineering/following-the-money/)
- [Snowflake Storage for Apache Iceberg](/data-engineering/snowflake-apache-iceberg-storage/)
- [Unity Catalog in Practice: Lessons From the Field](/data-engineering/unity-catalog-in-practice-2026/)

*Last Updated: April 22, 2026*
