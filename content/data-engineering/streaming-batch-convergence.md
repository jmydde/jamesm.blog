---
title: "Streaming Meets Batch: The Convergence That Took a Decade"
date: 2026-05-10T08:30:00+01:00
draft: true
tags: ["data", "streaming", "batch", "flink", "kafka", "iceberg"]
description: "For a decade the data engineering field has been promising that streaming and batch processing would converge into a single paradigm. In 2026 that convergence is genuinely happening, just not in the way the original proponents expected. A practical look at what actually changed."
cover:
  image: /assets/images/data-engineering/streaming-batch-convergence.jpg
  alt: Streaming Meets Batch Convergence Banner
---

For a decade the streaming-batch convergence has been the perennial promise of data engineering. Apache Spark would unify them. Apache Beam would unify them. Apache Flink would unify them. Each new framework arrived with the pitch that the artificial distinction between stream processing and batch processing would finally collapse. None of these unifications produced the predicted reality. In 2026 the convergence is genuinely happening, but it looks different from what the original proponents expected.

## The original promise and why it did not happen

The 2016-2020 framing of streaming-batch convergence was that a single processing framework would handle both modes. You would write your job once and execute it as either streaming or batch depending on the deployment configuration. The same code, the same semantics, just running at different cadences.

This did not happen because the assumption was wrong. The interesting problems in batch processing - large joins, complex aggregations, optimised query plans - are different from the interesting problems in streaming - event-time handling, windowing, exactly-once semantics, out-of-order events. A framework that treats them as the same case ends up doing both badly.

The actual practitioners knew this. Companies that needed both streaming and batch ran separate frameworks for each (Kafka Streams or Flink for streaming, Spark or Snowflake for batch) and built infrastructure to make the two ecosystems work together. The "unified" frameworks remained niche choices.

## What is actually converging

The 2026 convergence is happening at a different layer. The frameworks are still distinct - Spark for batch, [Flink](/data-engineering/apache-flink-2026-streaming-sql/) for streaming - but the storage layer, the catalog layer, and the query interface above them have unified.

The shared substrate is open table formats. [Apache Iceberg](/data-engineering/apache-iceberg-2026/), Delta Lake, and Hudi all support both streaming writes and batch reads on the same physical tables. A Flink job can write rows to an Iceberg table in real time; a Spark batch job can read the same table for historical analysis; a Trino query can answer interactive questions over the same data. The underlying tables are the same; the processing modes are different.

This is a more practical convergence than the framework-level one. The engines stay specialised; the data stays unified. You write your streaming logic in Flink because Flink is good at streaming. You write your batch logic in Spark or dbt because they are good at batch. You write your interactive queries in Trino or DuckDB because they are good at interactive. Everything points at the same Iceberg tables.

## The patterns that work

The architectures that work for combined streaming and batch in 2026 share a recognisable shape:

**One source of truth.** A set of Iceberg or Delta tables that hold the canonical data. Streaming jobs write to them; batch jobs read from them; everything stays consistent through the table format's ACID semantics.

**Streaming for derived state.** Flink jobs that compute aggregations, joins, or derivations as data arrives, writing the results back to Iceberg tables. The streaming layer produces state that batch processes can consume.

**Batch for historical and offline work.** Long-running aggregations, ML training, regulatory reports, complex joins - all done as batch over the same tables that the streaming jobs are writing.

**Catalog as coordination.** [Unity Catalog](/data-engineering/unity-catalog-in-practice/), Polaris, or Nessie managing the namespace, access control, and metadata for both streaming and batch consumers.

**Interactive query for exploration.** Trino, DuckDB, or whatever is convenient pointed at the same tables for ad-hoc analysis.

This is meaningfully different from the lambda architecture that dominated the previous generation. There is no separate batch and speed layer. There is one storage layer, with multiple processing engines pointed at it for different purposes.

## What this means for data engineers

The implications for working data engineers:

**The framework choice has narrowed.** Most production work in 2026 uses some combination of Flink for streaming, Spark or dbt for batch, and an interactive engine for exploration. The proliferation of frameworks from the 2016-2020 era has consolidated.

**The storage choice matters more.** Picking between Iceberg, Delta, and Hudi has implications across all your processing engines. The storage decision is now an architectural decision rather than a tactical one.

**Lambda architecture is dying.** Maintaining separate batch and speed layers, with reconciliation logic between them, is increasingly recognised as more cost than benefit. The single-storage-multiple-engines pattern is replacing it.

**Streaming-only and batch-only specialisations are blurring.** The data engineer who can work in both streaming and batch contexts is more valuable than one who specialises in either alone. Cross-modal fluency is the new baseline.

## The 2026 picture by use case

A practical breakdown of which approach for which problem in 2026:

**Real-time analytics on event streams** → Flink reading from Kafka, writing to Iceberg. Trino or similar reading from Iceberg for interactive analytics. The Kafka layer is for transport; the Iceberg layer is for state.

**Periodic batch analytics** → Spark or dbt reading from Iceberg, writing back to Iceberg. The same tables the streaming jobs are writing.

**ML feature pipelines** → Flink for online features, Spark for offline features, both writing to a shared feature store that is itself often Iceberg-backed.

**Operational dashboards** → Streaming aggregations in Flink, materialised as Iceberg tables, read by a BI tool. The dashboards are batch reads of streaming state.

**Audit and historical analysis** → Pure batch reads of Iceberg tables, often using DuckDB or BigQuery for the actual query work.

Note that "Kafka" appears mostly as a transport rather than as a destination. The 2026 pattern is to use Kafka for what Kafka is good at (durable streaming transport, decoupling producers from consumers) and put the actual state in Iceberg. This is a meaningful change from architectures that used Kafka as the storage layer itself.

## What the convergence does not do

Worth being honest about the limits:

**It does not eliminate the cognitive split between streaming and batch.** Engineers writing streaming code still need to think about event time, watermarks, windowing, and out-of-order events. Engineers writing batch code do not. The mental models remain different even if the storage is shared.

**It does not make every framework interchangeable.** Flink is still better than Spark at streaming. Spark is still better than Flink at large-scale batch. The choice between them still matters.

**It does not solve the operational complexity of running streaming systems.** Streaming is still operationally harder than batch. State management, exactly-once semantics, backpressure handling - all of these remain real challenges.

**It does not collapse the latency-throughput trade-off.** Streaming systems still have higher per-record overhead than batch systems. The cost of low-latency processing is real.

## The honest summary

The streaming-batch convergence is happening in 2026 in the way that mature ecosystems usually converge - at the integration points rather than at the implementation level. Different engines for different jobs, pointed at the same storage layer, coordinated through the catalog. This is less elegant than the single-framework vision of the previous decade but considerably more practical.

The teams that have absorbed this architecture have simpler data platforms than the previous generation. The lambda-architecture complexity is gone; the multi-system coordination is significantly easier. The trade-off is committing to the lakehouse architecture seriously, which means picking your table format, your catalog, and your engines deliberately rather than running each component independently.

For most teams in 2026, that trade-off is worth it. The convergence at the storage layer turned out to be the convergence that actually mattered, and it took most of a decade to figure out.

## Related Reading

- [Apache Flink 2026: Streaming SQL](/data-engineering/apache-flink-2026-streaming-sql/)
- [The Quiet Death of the Classic Data Warehouse Pattern](/data-engineering/death-of-classic-data-warehouse-pattern/)
- [Apache Iceberg in 2026](/data-engineering/apache-iceberg-2026/)
- [Iceberg V3 - What the New Spec Changes](/data-engineering/iceberg-v3-what-changes/)
- [Unity Catalog in Practice](/data-engineering/unity-catalog-in-practice/)
