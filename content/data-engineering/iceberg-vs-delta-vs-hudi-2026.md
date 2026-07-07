---
title: "Iceberg vs Delta vs Hudi in 2026 - The Format Wars Are Over"
date: 2026-05-03T14:00:00+01:00
draft: false
tags: ["data-engineering", "iceberg", "delta-lake", "hudi", "lakehouse", "data", "2026"]
description: "The open table format wars dominated the lakehouse conversation for five years. In 2026 the picture has settled. A grounded look at where Iceberg, Delta, and Hudi actually stand, who won which battles, and what that means for the people who have to choose."
cover:
  image: /assets/images/data-engineering/iceberg-vs-delta-vs-hudi-2026.jpg
  alt: Iceberg vs Delta vs Hudi 2026 Banner
---

## TL;DR

- The open table format war between [Apache Iceberg](https://iceberg.apache.org/), [Delta Lake](https://delta.io/), and [Apache Hudi](https://hudi.apache.org/) is effectively over in 2026 - and the outcome is not a single winner but a clear settlement.
- **Iceberg** has won the role of the **neutral standard** that engines and platforms expect to read and write. It is the format you choose when you do not want to be coupled to a single vendor.
- **Delta** has won the role of the **incumbent default inside the Databricks ecosystem** and remains a strong choice if Databricks is your primary engine. Delta UniForm has narrowed the gap by letting Delta tables expose Iceberg metadata.
- **Hudi** has not won a category outright. It retains a smaller but loyal user base for streaming-heavy and CDC-heavy workloads, where its design choices still genuinely fit.
- The interesting battle has moved up the stack to the [catalog layer](/data-engineering/the-catalog-layer-is-the-new-battleground/). The format question is mostly settled. The catalog question is the new fight.

## The Format Wars - A Brief History

For most of the early 2020s the lakehouse story was a three-way argument about how to put ACID transactions on top of object storage.

**Hudi** showed up first, in 2017, out of Uber. The motivating problem was upserts and incremental processing on big append-only datasets. Hudi was opinionated about streaming and CDC from the start.

**Delta Lake** came next, in 2019, out of Databricks. The motivating problem was bringing reliable, fast analytics to data lakes. Delta was opinionated about Spark and the Databricks platform from the start, then gradually opened up.

**Iceberg** came roughly in parallel, in 2018, out of Netflix. The motivating problem was correctness at scale - very large tables, very large numbers of partitions, very large numbers of concurrent writers. Iceberg was opinionated about being engine-agnostic from the start.

For five years the three formats fought for share, marketing budget, vendor commitments, and technical credibility. By late 2024 it was clear that the fight was narrowing. By 2026 it has resolved.

## Where Each Format Actually Stands In 2026

### Iceberg

Iceberg is the **default open table format** in 2026. That is not a marketing statement - it is what you can observe in the supported-formats lists of every major engine, vendor, and cloud platform.

- AWS Athena, Glue, EMR, S3 Tables - all native Iceberg.
- Snowflake - native Iceberg with full read and write.
- Google BigQuery - native Iceberg integration.
- Apache Spark, Trino, Flink, Dremio, ClickHouse, DuckDB, StarRocks - all read and write Iceberg.
- Databricks - reads Iceberg, writes Iceberg via UniForm.

The protocol-level commitment from the major engines locked in Iceberg's role as the neutral interchange format. Once your data is in Iceberg, you can pick your engine. That is the property that mattered most to enterprises and they bought it accordingly.

The other thing that helped was Iceberg's **REST catalog spec**. By standardising the catalog API, Iceberg made it possible for many catalog implementations to coexist while presenting the same interface. The format and the catalog protocol grew together.

### Delta

Delta is the **default format inside Databricks**, and Databricks is a serious chunk of the lakehouse market. That alone keeps Delta strategically important.

The decisive 2024-2025 move was [**Delta UniForm**](https://docs.databricks.com/en/delta/uniform.html) - a feature that lets a Delta table expose Iceberg-compatible metadata alongside its native Delta metadata. From the outside, a UniForm-enabled Delta table looks like an Iceberg table. From the inside, it is still Delta.

UniForm was an admission that Iceberg had won the standard-format role and a smart strategic concession. Databricks customers no longer have to choose between Delta's tight integration with their primary platform and Iceberg's broad ecosystem support. They can have both.

The result: Delta did not lose, it just stopped trying to win the neutrality fight. Inside Databricks, Delta is still the right answer. Outside Databricks, Delta is mostly read via its Iceberg-compatible metadata.

### Hudi

Hudi did not win a category in 2026 but it did not lose its identity either. The format retains genuine technical advantages for two specific use cases:

- **Streaming ingest with frequent upserts** - Hudi's MOR (Merge On Read) tables and built-in indexes are still arguably the most thought-through design in the format space for high-frequency upsert workloads.
- **CDC pipelines from operational databases** - Hudi's incremental query model is a natural fit for change-data-capture patterns.

The communities and vendor support around Hudi are smaller than around Iceberg or Delta. The format is alive, the project is healthy, but it is no longer in the running for general-purpose default.

If you have a workload where Hudi's design is a clear technical fit, use it. If you are choosing a format for general analytics, you are probably not choosing Hudi in 2026.

## What Actually Changed In 2025

A few specific 2025 events tipped the balance from "still fighting" to "settled."

**Snowflake's deep Iceberg commitment.** Snowflake fully committed to Iceberg as a first-class citizen, including writing through its own engines. That pulled enterprise customers who valued Snowflake away from a Snowflake-only proprietary format.

**S3 Tables.** AWS shipped a managed Iceberg table service that hides most of the operational pain of running Iceberg yourself. Customers who would have hesitated at the operational complexity now have a managed path.

**Delta UniForm reaching production.** UniForm went from a checkbox to a usable feature that real customers ship in production. That ended the awkward conversation where Databricks customers had to choose between native and interchange formats.

**Iceberg REST catalog gaining traction.** The standardisation of the catalog API meant that the format and the access layer no longer had to come from the same vendor. That is what is now driving the [catalog layer fight](/data-engineering/the-catalog-layer-is-the-new-battleground/).

## How To Choose In 2026

If you are starting fresh, the decision tree is much simpler than it was two years ago.

**Default to Iceberg.** Unless you have a specific reason to pick something else, Iceberg is the safest choice. Maximum engine support, maximum vendor support, no lock-in to a single platform.

**Pick Delta if Databricks is your primary engine and you are committed to it.** Native Delta inside Databricks gets the best performance and feature coverage. Use UniForm to keep the door open to Iceberg readers.

**Pick Hudi if your workload is upsert-heavy streaming or CDC and you have the operational expertise to run it well.** Hudi's design genuinely fits this use case. The smaller ecosystem is a tax you pay deliberately.

**Do not mix formats inside the same table.** This sounds obvious and yet it shows up. Pick one format per table and commit.

**Do not over-index on benchmarks.** Public benchmarks between these formats are noisy, version-dependent, and almost always suspect. The performance differences in 2026 are smaller than the operational and ecosystem differences. Choose for the latter.

## What This Means For Existing Pipelines

If you bet on one of the three formats years ago, the practical answer in 2026 is mostly **stay where you are**.

- **Iceberg shops** - keep going. You picked the format that became the standard.
- **Delta shops on Databricks** - keep going, enable UniForm if you want broader interoperability without migrating.
- **Delta shops not on Databricks** - quietly start planning a migration to Iceberg. The strategic story for non-Databricks Delta is weaker each quarter.
- **Hudi shops with workloads that fit Hudi** - keep going. The format works.
- **Hudi shops with general analytics** - migration to Iceberg is worth a serious look. The community gravity has moved.

Migrations between formats are not free, but they are also not as expensive as they were in 2022. Every major engine now has tooling to read multiple formats, which means migrations can happen incrementally rather than as cutover events.

## What The Format Wars Taught Us

A few lessons that generalise beyond table formats:

**Standards win when neutrality is valued more than features.** Iceberg did not win because it was technically dominant - the three formats are roughly comparable on capability. Iceberg won because being engine-neutral was the property that mattered most to enterprise buyers.

**Vendor moats are weaker than vendor relationships.** Databricks did not lose Delta share by giving up the format fight. Their customers stayed because the platform is sticky for reasons that have nothing to do with the table format.

**Compatibility is a strategy.** UniForm let Databricks have both stories. The lesson is that you do not always have to win a format war - you can sometimes just speak both languages.

**The fight always moves up the stack.** Once the format question settled, the catalog question became the new fight. The next fight after that will be the metadata-and-governance layer. The pattern repeats.

## The Honest Verdict

The format wars are over. Iceberg won the neutral-standard role. Delta won the in-platform-default role inside Databricks. Hudi won a smaller but real niche. Most teams in 2026 should default to Iceberg, and most teams that are already on Delta inside Databricks should stay there.

The interesting work has moved upward. The catalog layer is now where vendors are competing. Governance, lineage, and access control are now where the differentiation lives. The format question, after years of being the loudest debate in data engineering, is now the boring infrastructure question it was always going to become.

Boring infrastructure is a compliment. Boring means stable, interoperable, and out of the way. That is exactly what the lakehouse needed.

## Related Reading

- [Apache Iceberg in 2026](/data-engineering/apache-iceberg-2026/)
- [Snowflake's Apache Iceberg Storage](/data-engineering/snowflake-apache-iceberg-storage/)
- [The Modern Lakehouse Stack](/data-engineering/modern-lakehouse-stack/)
- [Databricks vs Snowflake 2026](/data-engineering/databricks-vs-snowflake-2026/)
- [Unity Catalog in Practice](/data-engineering/unity-catalog-in-practice/)
- [Lakeflow Declarative Pipelines](/data-engineering/lakeflow-declarative-pipelines/)
