---
title: "Data Processing Patterns: A Field Guide to Batch, Streaming, ETL, ELT and What Else You Need to Know"
date: 2026-10-09T08:20:00+01:00
draft: false
tags: ["data-engineering", "architecture", "batch", "streaming", "etl", "pipeline", "tool", "comparison", "kafka", "flink", "spark", "dbt", "airflow", "lakehouse"]
description: "A practical map of the ten data processing patterns every data engineer should know - batch, streaming, ETL, ELT, incremental, lambda and kappa, CDC, medallion, reverse ETL, federation and orchestration - each with a diagram and the best open source, SaaS and enterprise tools for the job."
---

## TL;DR

- **Batch vs streaming** and **ETL vs ELT** are the two questions everyone asks, but they are only two of ten patterns you will actually combine in a real platform
- The other patterns worth knowing: **incremental (micro-batch)**, **lambda and kappa**, **change data capture (CDC)**, **medallion layering**, **reverse ETL**, **federation**, and **orchestration** as the control plane around all of them
- Batch and ELT are the sensible defaults in 2026. Add streaming, CDC and reverse ETL where a specific latency or activation need justifies the extra moving parts
- For tools, I group the options three ways - **open source**, **SaaS** and **enterprise** - and say which I would reach for first. Those picks are my opinion, not a benchmark
- Vendor ownership has shifted a lot recently: IBM now owns Confluent, Fivetran has merged with dbt Labs, and Salesforce owns Informatica. Worth knowing before you sign anything

---

Most data engineering arguments start with a false choice. Batch or streaming. ETL or ELT. Warehouse or lakehouse. In practice a healthy platform uses several patterns at once, and the skill is knowing which one fits which problem.

This post is the map I would draw on a whiteboard for someone joining a data team. Each pattern gets a diagram, a plain description, the trade-offs, and the tools in three tiers: **open source** (you run it or pay a managed host), **SaaS** (someone else runs it and bills you), and **enterprise** (vendor suites, usually with licences, support contracts and governance features to match).

Two of these patterns already have deeper posts here, on [stream vs batch processing](/data-engineering/stream-vs-batch-processing/) and the convergence of the two. I keep those sections short and focus on the wider picture.

## How the patterns fit together

Think of the patterns as answering different questions:

| Question | Patterns |
|---|---|
| **When** does processing happen? | Batch, streaming, incremental |
| **Where** does the transformation happen? | ETL, ELT |
| **How** do I get data out of source systems? | Batch extract, CDC |
| **How** do I organise the result? | Medallion, lambda, kappa |
| **Where does the data go next?** | Reverse ETL, federation |
| **What keeps it all running?** | Orchestration |

You pick one answer per question, per pipeline. A single platform might ingest orders with CDC, process them incrementally into a medallion lakehouse, serve a few fraud signals through streaming, and push audiences to the CRM with reverse ETL - all scheduled by one orchestrator.

## 1. Batch processing

![Batch processing diagram](/assets/images/data-engineering/data-processing-patterns/01-batch.png)

Batch processes a **bounded** set of data in one go, on a schedule. Data accumulates, a job wakes up, reads everything it needs, transforms it and publishes the result.

**Use it when** latency of hours is fine, which covers most reporting, finance close, ML training sets and regulatory extracts. It is the cheapest per row, the easiest to debug (re-run the same input and compare) and the easiest to backfill.

**Watch out for** the latency floor set by your schedule, and for jobs that quietly grow until the nightly window is no longer big enough.

| Tier | Tools |
|---|---|
| Open source | [Apache Spark](https://spark.apache.org/), [DuckDB](https://duckdb.org/) for single-node work, [Trino](https://trino.io/) for SQL over lakes, [Apache Beam](https://beam.apache.org/) |
| SaaS | [Databricks](https://www.databricks.com/), [Snowflake](https://www.snowflake.com/), [Google BigQuery](https://cloud.google.com/bigquery), [AWS Glue](https://aws.amazon.com/glue/) |
| Enterprise | [Ab Initio](https://www.abinitio.com/), [IBM DataStage](https://www.ibm.com/products/datastage), [SAP Data Services](https://www.sap.com/products/technology-platform/data-services.html) |

**My first pick:** Spark if the data is large, DuckDB if it fits on one machine. The single-node renaissance is real, and most teams overestimate how big their data is.

## 2. Stream processing

![Stream processing diagram](/assets/images/data-engineering/data-processing-patterns/02-streaming.png)

Streaming processes an **unbounded** flow of events continuously. A broker holds the events in a partitioned, replayable log; a stream processor reads them, keeps state, and emits results within seconds or less.

**Use it when** the value of an event decays quickly: fraud checks, operational alerts, live inventory, personalisation, anything where "tomorrow morning" is too late.

**Watch out for** the costs that do not show on the whiteboard: always-on compute, state management, event time versus processing time, late data, and harder backfills. The [stream vs batch post](/data-engineering/stream-vs-batch-processing/) goes through these in detail.

| Tier | Tools |
|---|---|
| Open source | [Apache Kafka](https://kafka.apache.org/) (the log), [Apache Flink](https://flink.apache.org/) and [Kafka Streams](https://kafka.apache.org/documentation/streams/) (processing), Spark Structured Streaming, [RisingWave](https://risingwave.com/) for streaming SQL |
| SaaS | [Confluent Cloud](https://www.confluent.io/), [Amazon Kinesis](https://aws.amazon.com/kinesis/), Google Dataflow, [Redpanda](https://www.redpanda.com/) Cloud |
| Enterprise | Confluent Platform (now part of IBM), [Striim](https://www.striim.com/), Azure Event Hubs with Stream Analytics |

**My first pick:** Kafka for the log, Flink for anything stateful. Kafka 4.0, released in March 2025, removed ZooKeeper entirely and made KRaft the only metadata mode, which removes a whole class of operational pain. For Flink's SQL story see Apache Flink in 2026.

## 3. ETL vs ELT

![ETL vs ELT diagram](/assets/images/data-engineering/data-processing-patterns/03-etl-vs-elt.png)

The difference is **where the transform runs**.

- **ETL** extracts, transforms on a separate engine, then loads only the curated result. It made sense when warehouse compute was scarce and expensive
- **ELT** loads raw data first, then transforms it inside the warehouse or lakehouse using SQL. It became dominant because cloud compute is elastic and storage is cheap, and because keeping raw data means you can re-derive anything later

**Use ETL when** data must be masked, filtered or validated *before* it lands (privacy, sovereignty, regulated PII), or when the target cannot do the transform. **Use ELT** for nearly everything else. There is also a hybrid, sometimes called **EtLT**: a small lightweight transform before load (drop PII columns, fix types, flatten JSON), then heavy modelling after.

| Role | Open source | SaaS | Enterprise |
|---|---|---|---|
| Extract + load | [Airbyte](https://airbyte.com/), [dlt](https://dlthub.com/), [Meltano](https://meltano.com/) | [Fivetran](https://www.fivetran.com/), Airbyte Cloud | [Informatica](https://www.informatica.com/), [Qlik Talend](https://www.talend.com/), IBM DataStage |
| Transform (ELT) | [dbt Core](https://www.getdbt.com/), [SQLMesh](https://sqlmesh.com/), Spark SQL | dbt platform, Snowflake dynamic tables, Databricks Lakeflow | Informatica, Ab Initio |

**My first pick:** dlt or Airbyte for loading, dbt or SQLMesh for modelling. I compare the last two in dbt vs SQLMesh, and the wider tool landscape is in the [ETL tools guide](/data-engineering/etl-tools/).

A note on ownership, because it matters for procurement: Fivetran announced completion of its merger with dbt Labs on 1 June 2026, so the most popular loader and the most popular transformation framework now sit under one roof. My own read, not reported fact: it is worth watching how dbt Core's open source side evolves under the combined company.

## 4. Incremental (micro-batch) processing

![Incremental micro-batch diagram](/assets/images/data-engineering/data-processing-patterns/04-micro-batch.png)

This is the pattern most teams should try before real streaming. A short-lived job wakes on a trigger (every few minutes, hourly, or when a file arrives), processes only what is new since its last checkpoint, writes the result and **exits**. Nothing runs between triggers.

You get the bookkeeping of streaming - each record handled once, progress checkpointed, no hand-rolled "since last run" logic - with the economics of batch. Run it every five minutes and you have near-real-time without an always-on cluster. Moving to continuous processing later is a configuration change, not a rewrite.

| Tier | Tools |
|---|---|
| Open source | Spark Structured Streaming with an available-now style trigger, dbt incremental models, Flink in batch mode, Delta and Iceberg incremental reads |
| SaaS | [Databricks Lakeflow Declarative Pipelines](/data-engineering/lakeflow-declarative-pipelines/), Snowflake dynamic tables and Snowpipe, BigQuery materialized views |
| Enterprise | Informatica and DataStage incremental loads |

**My first pick:** whatever incremental feature your warehouse or lakehouse already has. It is almost always the lowest-effort route to "fresh enough".

## 5. Lambda and Kappa architectures

![Lambda vs Kappa diagram](/assets/images/data-engineering/data-processing-patterns/05-lambda-kappa.png)

These two are patterns for **organising** batch and streaming together.

- **Lambda** runs two paths: a streaming "speed layer" for fast, approximate results, and a batch layer that recomputes the authoritative answer. A serving layer merges them. It is robust, but you maintain the same logic twice
- **Kappa** runs one streaming code path over a long-retention log. If the logic changes or has a bug, you replay history through the new version into a fresh view and swap it in. One codebase, but replay at scale has to actually work

In 2026 the two have blurred. Open table formats such as [Apache Iceberg](/data-engineering/apache-iceberg-2026/) give you cheap, replayable storage, and engines like Flink and Spark can run the same SQL in batch or streaming mode. That makes a Kappa-style design far more practical than it was, and it is the heart of the streaming and batch convergence story.

**Tools:** the same engines as batch and streaming. Pick one that can run identical logic in both modes (Flink, Spark, or a streaming database) and keep raw events in object storage so replay is always possible.

## 6. Change data capture (CDC)

![Change data capture diagram](/assets/images/data-engineering/data-processing-patterns/06-cdc.png)

CDC reads a database's own **transaction log** (the WAL, binlog or redo log) and turns every insert, update and delete into an event. Compared with repeatedly querying tables, you get:

- Deletes, which snapshot-based extraction misses entirely
- Far lower load on the source database
- Low latency, and a faithful history of changes in order

It is the cleanest way to get operational data into an analytical platform, and the usual bridge between the transactional world and everything else in this post. Land the change stream, then `MERGE` it into a current-state table and optionally keep the history as an audit feed or slowly changing dimension.

**Watch out for** schema changes at the source, large initial snapshots, and log retention: if your connector is down longer than the database keeps its log, you must re-snapshot.

| Tier | Tools |
|---|---|
| Open source | [Debezium](https://debezium.io/) (Kafka Connect based), Flink CDC, Airbyte CDC connectors |
| SaaS | Fivetran database connectors, Confluent Cloud managed connectors, [Estuary](https://estuary.dev/), cloud-native options such as AWS DMS |
| Enterprise | [Oracle GoldenGate](https://www.oracle.com/integration/goldengate/), [Qlik Replicate](https://www.qlik.com/us/products/qlik-replicate), IBM data replication, Striim |

**My first pick:** Debezium if you already run Kafka, a managed connector if you do not want to. For regulated Oracle estates, GoldenGate is still the safe answer.

## 7. Medallion (multi-hop) architecture

![Medallion architecture diagram](/assets/images/data-engineering/data-processing-patterns/07-medallion.png)

Medallion organises data into layers of increasing quality:

- **Bronze:** raw, append-only, exactly as received. Your insurance policy
- **Silver:** cleaned, deduplicated, typed and conformed. The reusable foundation
- **Gold:** business-level models, metrics and features, shaped for consumers

Put quality checks and data contracts at each hop, so bad data is stopped at the cheapest layer to fix. The pattern pairs naturally with ELT and incremental processing, since each layer is just another transformation reading the one before it. Variations exist (raw/staging/marts in dbt vocabulary, for example), but the idea is the same: never transform in place, and keep a replayable raw layer.

**Tools:** it is an organising principle, not a product. Delta Lake or Iceberg tables, plus dbt, SQLMesh or Lakeflow for the transformations, plus a catalog for governance. See the [modern lakehouse stack](/data-engineering/modern-lakehouse-stack/) and data quality in the lakehouse.

## 8. Reverse ETL

![Reverse ETL diagram](/assets/images/data-engineering/data-processing-patterns/08-reverse-etl.png)

Reverse ETL moves modelled data **out of** the warehouse and into the operational tools where people act on it: CRM, ad platforms, support desks, email and marketing automation. A SQL model defines the audience or record set, and a sync engine handles diffing, field mapping, rate limits and retries.

It exists because the warehouse became the best single view of the customer, yet salespeople and marketers do not live in SQL. The honest caveat: it adds another system that writes to production tools, so treat it with the same change control as any other integration, and watch for the argument that some of it is better done as a proper application feature.

| Tier | Tools |
|---|---|
| Open source | Few mature options; teams often script syncs with dlt or Airbyte destinations, or use [RudderStack](https://www.rudderstack.com/) |
| SaaS | [Hightouch](https://hightouch.com/), [Census](https://www.getcensus.com/), Fivetran activations, Segment |
| Enterprise | Salesforce Data 360 and similar CDP suites, Adobe Real-Time CDP |

**My first pick:** a dedicated SaaS tool. This is one of the few places where buying beats building, because the long tail of destination APIs is miserable to maintain yourself.

## 9. Federation and virtualisation

![Federation and virtualisation diagram](/assets/images/data-engineering/data-processing-patterns/09-federation.png)

Sometimes the best pipeline is no pipeline. A federated query engine reads data **where it lives** - a Postgres database, an Iceberg table, a SaaS API - and joins across them in one SQL statement, pushing filters down to each source.

**Use it for** exploration, prototyping, one-off cross-system questions, and as a bridge while a migration is in flight. **Avoid it** for heavy, repeated workloads: you inherit every source's performance and availability problems, and a slow source slows the whole query. Copy the data once it becomes a dependency.

| Tier | Tools |
|---|---|
| Open source | Trino, DuckDB (with its extension ecosystem), [Apache Drill](https://drill.apache.org/) |
| SaaS | [Starburst](https://www.starburst.io/), [Dremio](https://www.dremio.com/), Snowflake and BigQuery external tables, Databricks Lakehouse Federation |
| Enterprise | [Denodo](https://www.denodo.com/), [TIBCO Data Virtualization](https://www.tibco.com/), IBM data virtualization |

A close relative is the **zero-ETL** integration some cloud vendors offer between their own operational and analytical services. It is convenient inside one vendor's walls and, in effect, managed CDC. A catalog layer keeps the governance coherent, which is why the [catalog layer is the new battleground](/data-engineering/the-catalog-layer-is-the-new-battleground/).

## 10. Orchestration: the control plane

![Orchestration diagram](/assets/images/data-engineering/data-processing-patterns/10-orchestration.png)

Orchestration is not a processing pattern so much as the thing that makes every other pattern operable. The orchestrator schedules work, resolves dependencies, gates publishing on validation, retries failures, alerts people and supports backfills from the point of failure.

Two ideas to take with you. First, design tasks to be **idempotent**: re-running a task for the same input must give the same result and never double-count. Without this, retries and backfills are dangerous. Second, prefer **asset-based** thinking (what data should exist and how fresh is it?) over pure task-based thinking (did the script run?), which is how modern orchestrators model the world.

| Tier | Tools |
|---|---|
| Open source | [Apache Airflow](https://airflow.apache.org/), [Dagster](https://dagster.io/), [Prefect](https://www.prefect.io/), Kestra |
| SaaS | Astronomer, Dagster+, Prefect Cloud, Databricks Jobs, Google Cloud Composer, Amazon MWAA |
| Enterprise | [Control-M](https://www.bmc.com/it-solutions/control-m.html), Azure Data Factory, Informatica workflows, Ab Initio Control Center |

**My first pick:** Airflow if your team already knows it, Dagster for greenfield work built around data assets.

## Patterns worth adding to your vocabulary

Beyond these ten, a few practices belong in the same conversation, even though they are properties of pipelines rather than architectures:

- **Idempotency and replay:** every pipeline should be safely re-runnable
- **Data contracts:** an agreed schema and quality promise between producer and consumer, enforced in CI
- **Slowly changing dimensions (SCD):** how you keep history when attributes change
- **Event sourcing and outbox:** designing the *source* application so it emits reliable events, rather than reverse-engineering them later
- **Observability and lineage:** knowing what broke, what it affects, and who to tell

## How to choose

A short decision path I use:

1. **Is hours-level latency acceptable?** Yes: batch or incremental, ELT, medallion. Stop here for most workloads
2. **Do you need minutes?** Use incremental processing on a short trigger before reaching for streaming
3. **Do you need seconds, and does the value decay fast?** Streaming, probably with Kafka and Flink, with raw events also landing in object storage
4. **Is the data in an operational database?** Use CDC rather than polling
5. **Do operators need the results in their own tools?** Add reverse ETL
6. **Is it a one-off or exploratory question?** Federate, then copy if it sticks
7. **Always:** wrap it in an orchestrator, add contracts and tests at layer boundaries, make every task idempotent

## Summary

Patterns are not competing religions. Batch and streaming differ in *when*, ETL and ELT in *where*, CDC in *how data leaves the source*, medallion in *how it is organised*, reverse ETL and federation in *where it goes*, and orchestration in *how it all stays running*. Default to the cheap, replayable options, add complexity only where a real requirement pays for it, and keep a raw copy so you can always change your mind.

## Related Reading

- [Real-Time Data Processing: Stream Processing vs Batch Processing](/data-engineering/stream-vs-batch-processing/)
- [ETL Tools & Data Integration Platforms](/data-engineering/etl-tools/)
- [The Modern Lakehouse Stack](/data-engineering/modern-lakehouse-stack/)
- [Diagrams as Code](/data-engineering/diagrams-as-code/)

## Sources

- [IBM completes $11bn Confluent acquisition](https://www.channelweb.co.uk/news-network/2026/ibm-completes-11bn-confluent-acquisition) (IBM completed the purchase on 17 March 2026)
- [Fivetran and dbt Labs complete merger](https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents)
- [Salesforce completes acquisition of Informatica](https://www.salesforce.com/news/?p=91078) (completed 18 November 2025)
- [Kafka 4 KRaft architecture, InfoQ](https://www.infoq.com/news/2025/04/kafka-4-kraft-architecture)
