---
title: "Iceberg V3: What the New Spec Actually Changes"
date: 2026-05-12T23:00:00+01:00
draft: true
tags: ["data", "iceberg", "lakehouse", "format", "table"]
description: "Apache Iceberg V3 is the most significant change to the format since it became the de facto lakehouse standard. A practical look at what V3 actually adds, which use cases benefit, and what migration looks like."
cover:
  image: /assets/images/data-engineering/iceberg-v3-what-changes.jpg
  alt: Iceberg V3 - What the New Spec Changes Banner
---

Apache Iceberg has become the table-format default for the lakehouse era, at a level of adoption that would have been hard to predict three years ago. Every major data platform - Snowflake, Databricks, BigQuery, AWS, Starburst - supports it as a first-class format. That makes the V3 spec, which has been in development through 2024 and 2025 and is reaching production maturity in 2026, the most consequential format change in the analytical data space in years.

This post is a working summary of what V3 actually changes, what stays the same, and what the migration path looks like.

## The headline changes

V3 introduces a few features that meaningfully expand what Iceberg can do:

**Row lineage tracking.** V3 supports tracking individual row-level changes - the equivalent of change-data-capture, baked into the table format. This is significant for any workload that needs to know not just the current state but the history of changes, with row-level granularity.

**Deletion vectors.** V3 introduces deletion vectors as a first-class concept, replacing the equality-and-position-delete file structure from V2. The implementation is more efficient, the read path is faster, and the storage overhead for tables with frequent deletes is much lower.

**Variant data type.** Native support for a `VARIANT` type that can hold semi-structured data (JSON-like) with efficient storage and query semantics. This bridges the gap between strict schema enforcement and the flexibility of JSON-typed columns.

**Default values and column-level defaults.** Tables can now specify default values for columns, simplifying schema evolution. Adding a new column with a default no longer requires re-writing every row.

**Better support for nested types.** Improved handling of complex nested structures, including better support for evolving nested schemas without full rewrites.

**Improved partition evolution.** Partition specs can now evolve more flexibly without rewriting existing data, which makes operational changes to partition strategy substantially less painful.

## What stays the same

V3 is explicitly designed for backward compatibility. The core promises of Iceberg - ACID semantics, schema evolution, time travel, hidden partitioning - all carry over unchanged. Existing V2 tables can be read by V3-aware tooling without conversion. V3 features are opt-in at the table level, so a single catalog can hold V2 and V3 tables side by side.

The catalog story is also unchanged - V3 works with the same catalog implementations (Glue, Nessie, [Unity](/data-engineering/unity-catalog-in-practice/), Polaris, REST) that V2 worked with, with the catalog protocol extended for the new features.

## Why row lineage matters

The row-lineage feature is the most novel of the V3 additions and is worth a closer look. It allows the table to maintain a history of which rows have been added, modified, or deleted, with row-level identity tracking that survives partition changes and compaction.

The use cases this enables include:

- **Cheap change-data-capture without a separate pipeline.** Downstream systems can subscribe to row-level changes from an Iceberg table directly, without needing Debezium or similar.
- **Audit trails.** Compliance use cases that require tracking who changed what when, at row granularity.
- **Incremental processing.** Downstream ETL that needs to process "what changed since last run" can do so against Iceberg's own metadata, without separate change-tracking infrastructure.
- **AI workloads with provenance.** Knowing which rows fed a model training run, for reproducibility and lineage tracking.

This feature alone is enough to justify V3 adoption for workloads that previously depended on separate CDC infrastructure.

## The variant type and its trade-offs

The new `VARIANT` type is conceptually similar to Snowflake's variant or Postgres's JSONB - it lets you store semi-structured data without requiring a strict schema. The implementation is efficient, with sub-document extraction supported at query time without parsing the entire document.

This is useful but not free. Variant columns lose some of the schema-enforcement benefits that have always been part of Iceberg's value proposition. The right pattern is to use variant for genuinely variable data and stick to strict types for everything else - the same advice as with similar features in other systems.

## What migration looks like

For most users, V3 adoption is straightforward:

1. **Upgrade to a V3-capable engine.** Most major engines have shipped V3 support over the course of 2025, with full production readiness through early 2026.
2. **Create new tables as V3.** The default format for new tables can be set at the catalog or namespace level.
3. **Leave existing V2 tables alone.** No migration needed unless you specifically want to use V3 features on those tables.
4. **Migrate V2 tables incrementally.** When you do want a specific V2 table at V3, the conversion is a single table-level operation that rewrites metadata without touching the data files.

The realistic migration timeline for most enterprise data platforms is staged - new tables at V3 first, conversion of existing tables based on which V3 features each table would benefit from. There is no rush, and the spec was explicitly designed to avoid forcing a big-bang migration.

## What does not change

The interesting things V3 does *not* address are worth noting because they are sometimes wrongly attributed to the new spec:

- **V3 does not change the underlying Parquet file format.** Iceberg sits on top of Parquet; the file format work happens separately.
- **V3 does not address the catalog protocol fundamentally.** Improvements to catalog operations are happening in parallel through the REST catalog spec evolution.
- **V3 does not solve the cross-format interoperability problem.** Iceberg, Delta, and Hudi remain separate formats. Conversion tools exist but the formats are not converging.
- **V3 does not improve query performance directly.** Performance gains from V3 come from feature-specific improvements (deletion vectors, variant query semantics) rather than a general performance uplift.

## The bigger picture

V3 represents Iceberg maturing from "a credible alternative to proprietary table formats" to "a comprehensive analytical table format that handles cases proprietary formats handle." The features that V3 adds are the ones that operators of mature data platforms have been asking for - row lineage, better delete semantics, default values, variant types, partition evolution.

The result is that Iceberg V3 is harder to dismiss as "Delta but open" in 2026 than V2 was in 2024. It is a complete, mature table format with feature parity for most production use cases and clear ownership outside any single vendor. That position - widely adopted, vendor-neutral, technically complete - is the position that drives long-term industry standardisation. V3 makes Iceberg's claim on it stronger.

## Related Reading

- [Apache Iceberg in 2026](/data-engineering/apache-iceberg-2026/)
- [Iceberg vs Delta vs Hudi 2026](/data-engineering/iceberg-vs-delta-vs-hudi-2026/)
- [The Catalog Layer Is the New Battleground](/data-engineering/the-catalog-layer-is-the-new-battleground/)
- [Unity Catalog in Practice](/data-engineering/unity-catalog-in-practice/)
- [Snowflake and Apache Iceberg Storage](/data-engineering/snowflake-apache-iceberg-storage/)
