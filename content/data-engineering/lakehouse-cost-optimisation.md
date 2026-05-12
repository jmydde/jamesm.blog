---
title: "Cost Optimisation in the Lakehouse Era: Where the Money Actually Goes"
date: 2026-05-15T09:00:00+01:00
draft: true
tags: ["data-engineering", "cost", "finops", "lakehouse", "databricks", "snowflake", "2026"]
description: "A grounded look at where the money actually goes in a 2026 lakehouse deployment - the cost categories that matter, the over-spending patterns that show up everywhere, and the optimisation moves that actually work."
cover:
  image: /assets/images/data-engineering/lakehouse-cost-optimisation.jpg
  alt: Cost Optimisation in the Lakehouse Era - Where the Money Actually Goes Banner
---

The single most useful diagnostic you can run on a data team in 2026 is a careful audit of where the money actually goes. The answers are reliably surprising. The compute that dominates the bill is usually different from what people think. The storage that looks cheap on paper is usually not. The "optimisation" work that teams pour effort into is often working on the wrong category. The compounding effect across most data organisations is a meaningful fraction of the data budget being spent on the wrong things, and the optimisation moves that actually shift the numbers are not the ones most teams start with.

## TL;DR

- The dominant cost categories in a 2026 lakehouse deployment are, in approximate order of magnitude: **compute** (warehouse queries and pipeline runs), **storage** (object storage with the per-API-call costs being more consequential than the per-GB costs), **data transfer** (cross-region and cross-cloud movement), **catalog and metadata operations**, and **vendor licence costs**.
- The single biggest source of waste in most deployments is **idle and over-provisioned compute**. Warehouses sized for peak load run at peak cost. Auto-scaling that does not actually scale down. CI/CD pipelines that spin up large clusters for trivial work.
- The second biggest is **redundant transformation work**. Tables that are recomputed when they have not changed. Joins that re-read entire tables when only a small change occurred. Daily full refreshes for data that has been incremental for years.
- **The single most effective optimisation move in 2026** is to identify the top 10 most expensive queries or pipelines in your deployment and rewrite them. The cost distribution is heavily skewed - 10% of the workloads typically account for 60-80% of the cost, and concentrated optimisation on the top of the distribution returns the largest gains.
- The architectural moves that matter: **right-sizing the compute layer** (sometimes smaller, sometimes single-node, sometimes the wrong vendor entirely), **incremental-by-default transformations** (which the move from dbt to [SQLMesh](/data-engineering/dbt-vs-sqlmesh-2026/) frequently enables), **file-format optimisation** (compaction, partitioning, sorting), and **query review** (the Snowflake/Databricks query insights, plus actual human attention to the top of the cost distribution).
- The realistic cost reduction available to most teams from a serious optimisation programme is **30-50% in the first year**, with the bulk of the savings coming from a small number of concentrated changes rather than from broad-based efficiency improvements.

## Where the money actually goes

The first step in any cost optimisation programme is to understand where the spending actually goes. The answer is reliably different from what people assume.

The typical breakdown of a moderately-sized lakehouse deployment ($500k-$5M annual data spend) looks roughly like this:

**Compute: 50-70% of total spend.** This is the dominant category in essentially every deployment. The split within compute varies but the rough shape is: scheduled production pipelines (40-60% of compute), ad-hoc and analyst queries (20-30%), CI/CD and development environments (10-20%), and ML training and inference (the remainder).

**Storage: 10-25% of total spend.** The per-GB cost of object storage is genuinely cheap. The surprise in this category is usually the **per-API-call cost** - S3, GCS, and Azure Blob charge for LIST and GET and PUT operations, and a poorly-tuned lakehouse with many small files can rack up significant API costs even with modest storage.

**Data transfer: 5-15% of total spend.** Cross-region replication, cross-cloud movement, and egress for downstream consumers. This category is heavily affected by architectural choices about where data lives and how it moves. Cross-cloud egress in particular is a hidden cost that has bitten many teams that adopted multi-cloud architectures.

**Catalog and metadata operations: 1-5% of total spend.** Usually small in absolute terms but growing fast as the catalog layer becomes more central to the architecture. Unity Catalog, Polaris, and the equivalent commercial offerings charge for metadata operations and the costs can scale unexpectedly in heavily-fragmented deployments.

**Vendor licence costs: variable, depending on architecture.** Snowflake credits, Databricks commit, the Salesforce/Tableau/Looker license, the Monte Carlo or Anomalo subscription, the various third-party connectors. The licence-driven costs can be 20-40% of total spend for teams that have not actively managed vendor relationships.

The reason the breakdown matters is that the optimisation moves are different in each category. Compute optimisation is mostly about right-sizing and incremental processing. Storage optimisation is mostly about file compaction and partitioning. Transfer optimisation is mostly about architecture - keeping data co-located with the compute that processes it. Each category needs its own approach.

## The cost distribution is skewed

The single most useful empirical fact about lakehouse spending is that the cost distribution is heavily skewed. The Pareto pattern is universal:

- 10% of the workloads typically account for 60-80% of the compute cost
- The top 10 most expensive queries or pipelines often account for 30-50% of compute
- A handful of poorly-tuned tables typically dominate the storage and metadata-operation costs

The implication is that concentrated optimisation on the top of the distribution returns the largest gains. The "broad-based efficiency improvements" approach - tuning everything by a small amount - returns much less than the focused approach of identifying the largest cost contributors and fixing them.

The practical pattern that works: use the platform's query insights (Snowflake Query History, Databricks Query Profile, BigQuery INFORMATION_SCHEMA) to identify the top 10-20 most expensive queries or pipelines. Audit each one. Most of them will have an obvious fix - missing partition pruning, full-refresh instead of incremental, over-provisioned warehouse size, redundant joins. Fixing the top 10 typically returns 20-40% of total compute cost.

## The over-provisioning trap

The single most common source of waste in 2026 lakehouse deployments is over-provisioned compute. The pattern shows up in several forms.

**Warehouses sized for peak load.** A warehouse that runs at peak utilisation for two hours per day and at 10% utilisation for the other 22 spends most of its credits doing very little. The fix is auto-scaling or, more commonly, a different sizing strategy that uses small warehouses for the routine work and large warehouses only for the peak workloads.

**Auto-scaling that does not scale down.** Most auto-scaling implementations are good at scaling up and bad at scaling down. The cluster grows during a peak, the peak ends, the cluster sits at the elevated size until a timeout, the timeout is long, the cluster sits idle for hours. The fix is more aggressive scale-down timeouts and explicit teardown of clusters that are not being used.

**CI/CD pipelines on production-sized compute.** CI pipelines that spin up large Spark clusters or warehouses for tests that could run on much smaller infrastructure. The cost can be significant given the frequency of CI runs, and the fix is usually trivial - smaller CI infrastructure, or running tests locally on developer machines instead of in cloud-based CI.

**Development environments that mirror production scale.** Dev and staging environments running at production sizes "just in case." The fix is to right-size the non-production environments based on the actual work being done in them, with explicit ramp-up paths if production-scale testing is needed for specific changes.

**Idle interactive warehouses.** Snowflake warehouses that have been left running after the analyst finished the query, Databricks all-purpose clusters that nobody is using, BigQuery slots that are reserved but underutilised. The fix is aggressive auto-suspend policies and explicit cluster lifecycle management.

The cumulative effect of over-provisioning is large. Teams that audit their compute utilisation carefully typically find 20-40% of compute spend is on idle or over-sized resources, and the fixes are usually straightforward.

## The redundant work trap

The second-most-common source of waste is redundant transformation work. The pattern shows up in several forms.

**Daily full refreshes.** Tables that are completely rebuilt every day even though only a small fraction of the data changes. The fix is incremental processing, which the move from dbt to SQLMesh frequently enables - the [virtual development environments and incremental-by-default models](/data-engineering/dbt-vs-sqlmesh-2026/) in SQLMesh specifically address this pattern.

**Cascading recomputation.** When a single upstream table changes, every downstream table recomputes even though most of the downstream data has not changed. The fix is finer-grained lineage tracking and partial-recomputation patterns that update only the affected rows.

**Joins that re-read large tables.** A pipeline that joins a small change against a large reference table by re-reading the entire reference table. The fix is either to keep the small change in memory, to use broadcast joins, or to restructure the pipeline to filter the reference table earlier.

**Multiple consumers re-computing the same intermediate result.** Several pipelines that each independently compute the same intermediate aggregation or join. The fix is to materialise the intermediate result once and have all consumers read from it.

**Snapshot-style time-travel queries on large tables.** Iceberg, Delta, and similar table formats support time-travel queries, which is useful but can be expensive when the queries are running over many snapshots of large tables. The fix is usually to use the table format's compaction features and to optimise the query patterns.

## File format and partitioning

A significant fraction of cost-optimisation work in 2026 is at the file-format level rather than at the query or pipeline level. The patterns that matter:

**Compaction.** Lakehouse tables tend to accumulate many small files - one per write transaction, with frequent transactions producing many small files. Reading many small files is expensive both in I/O and in metadata operations. The fix is regular compaction (Iceberg's `optimize`, Delta's `OPTIMIZE`, equivalent operations on other formats), which combines small files into larger ones and significantly improves both query performance and metadata efficiency.

**Partitioning.** Choosing the right partition keys is one of the highest-leverage decisions in lakehouse design. Wrong partitioning produces full-table scans on what should be partition-pruned queries. The right partitioning depends on the query patterns - the columns most frequently filtered on, the cardinality of those columns, the time dimension - and getting it right typically requires iteration.

**Z-ordering and clustering.** Within partitions, the physical ordering of data affects query performance. Z-ordering (Delta) or sort-based clustering (Iceberg) groups related rows together, which improves both query performance and compression. The trade-off is the cost of running the clustering operations, which is significant for large tables.

**Column statistics.** Modern lakehouse formats maintain per-file column statistics (min/max values, null counts, etc.) that enable file skipping during query execution. Keeping the statistics up to date is essential for good query performance, and the cost of maintaining them is typically much smaller than the cost of not having them.

The file-format optimisation work is unglamorous but it produces real cost savings. A well-organised lakehouse with appropriate compaction, partitioning, and clustering can be 2-5x cheaper to query than a poorly-organised one, and the optimisation work pays back quickly on any reasonably-sized deployment.

## The architectural moves

Beyond the tactical optimisations, several architectural moves produce larger cost reductions for teams willing to make them.

**Right-sizing the compute layer.** Sometimes this means smaller warehouses. Sometimes it means moving to a different vendor. Sometimes it means moving to [single-node engines](/data-engineering/single-node-renaissance/) for the workloads that fit. The most consequential question is whether the current compute architecture is appropriate for the actual workload, and the answer is often no.

**Incremental-by-default transformations.** The move from full-refresh to incremental transformations has been a stated goal for years. The actual implementations have lagged because the tooling made it hard. The current generation of tools (SQLMesh in particular) makes incremental processing the default rather than the exception, and adopting them is one of the higher-impact optimisation moves available.

**Workload-appropriate engines.** Different workloads have different cost profiles on different engines. Analytical SQL on small data runs cheaper on DuckDB than on Snowflake. ML feature pipelines run cheaper on Polars than on Spark for many workloads. Log analytics run cheaper on ClickHouse than on the general-purpose warehouses. Matching the engine to the workload can return 5-10x cost reductions on specific workloads, and the aggregate impact across the full set of workloads is substantial.

**Storage tiering.** Object storage providers offer multiple storage classes - hot, cool, archive - at different price points. Most lakehouse deployments use only the hot tier even though much of the data is rarely accessed. The fix is to tier old or rarely-accessed data to cheaper storage classes, with the access patterns determining where each table lives.

**Vendor relationship management.** A significant fraction of total data spend goes to vendor licences and committed-spend agreements. Most teams negotiate these once and forget about them. The teams that actively manage the relationships - renegotiating commits annually, evaluating alternatives, threatening to switch - typically extract 10-20% better pricing than the teams that do not.

## The FinOps practice

The teams that have shipped sustainable cost optimisation typically have a FinOps practice - an ongoing process for cost monitoring, attribution, and accountability - rather than a one-off optimisation project.

The components of a working FinOps practice:

**Cost attribution.** Knowing which team, project, or use case is responsible for which costs. This is usually enabled by tagging at the resource level and by query-level cost attribution in the platform (Snowflake's query attribution, Databricks' tagged compute, BigQuery's labels).

**Cost monitoring.** Dashboards that show cost trends over time, alerts on anomalous spikes, weekly or monthly reviews with the responsible teams. The cadence varies but the principle is the same - cost should be visible and the visibility should drive accountability.

**Cost budgets.** Per-team or per-project budgets that constrain spending, with explicit processes for requesting increases. Hard limits are usually impractical (the cost of a blocked production workload is higher than the cost of going over budget) but soft limits with escalation requirements work well.

**Optimisation cadence.** Regular reviews of the top of the cost distribution, with specific optimisation work scheduled and tracked. The practice prevents the slow drift toward over-spending that happens when nobody is looking.

**Vendor relationship management.** Annual reviews of vendor commitments, comparison shopping at renewal, and explicit alternatives evaluation. This is usually the responsibility of a finance or procurement function rather than the data team itself but the data team has to be informed enough to weigh in on the technical implications.

The teams that institutionalise these practices tend to maintain optimisation gains over time. The teams that do not tend to slide back to over-spending within 12-18 months of any one-off optimisation effort.

## The controversial parts

Three claims in the cost-optimisation conversation deserve more pushback than they typically get.

The first is the claim that the managed platforms (Snowflake, Databricks, BigQuery) are inherently expensive. The reality is that the managed platforms are competitively priced for the workloads they handle well and over-priced for workloads they handle badly. The cost problem is usually a workload-matching problem rather than a vendor problem, and the fix is usually to match workloads to engines rather than to switch vendors wholesale.

The second is the claim that switching to open-source alternatives is the path to lower costs. It can be, but it has costs of its own - engineering capacity, operational overhead, support contracts. The total-cost-of-ownership calculation depends on the specific workloads and on the team's actual ability to operate open-source infrastructure. The teams that have switched to open-source for the cost savings without budgeting for the operational cost have often ended up paying more, not less.

The third is the claim that cost optimisation is a one-time project. It is not. The drift toward over-spending is constant, and the optimisation work has to be ongoing. The teams that treat cost optimisation as a project that completes typically see the savings erode over 12-18 months as new workloads are added without optimisation discipline.

## Where this is heading

The most likely shape of 2027-2028 is that cost optimisation becomes a normal part of data engineering practice rather than a specialist concern. The platforms will continue to ship better cost-attribution and optimisation tooling. The third-party FinOps platforms (CloudZero, Vantage, etc.) will continue to mature. The architectural patterns that produce sustainable cost efficiency will continue to spread.

The other prediction worth making is that AI-assisted cost optimisation is going to become a real feature of the data platforms. Automatic query optimisation, automatic warehouse right-sizing, automatic file compaction tuning - these are tasks that AI is well-suited for and that the platforms have significant data to train on. The "let the platform optimise this automatically" path will become a default feature rather than a separate product.

For teams thinking about cost in 2026, the practical guidance is the boring version of the exciting story. Audit where the money actually goes. Focus on the top of the distribution. Right-size compute. Adopt incremental processing where it makes sense. Optimise file formats. Build a FinOps practice. Renegotiate vendor agreements. The teams that do this consistently outperform the teams that do not by significant margins, and the savings compound year over year in ways that materially affect the team's broader investment capacity.

## Related Reading

- [Databricks vs Snowflake in 2026: An Honest Comparison](/data-engineering/databricks-vs-snowflake-2026/) - the platform context for most lakehouse cost discussions.
- [Following the Money: Databricks vs Snowflake vs the Open-Source Alternative](/data-engineering/following-the-money/) - the broader vendor economics.
- [The Single-Node Renaissance: When Your Data Fits on a Laptop](/data-engineering/single-node-renaissance/) - the most consequential architectural move for cost reduction on the workloads where it applies.
- [dbt vs SQLMesh: The Transformation Layer Showdown in 2026](/data-engineering/dbt-vs-sqlmesh-2026/) - the transformation-layer cost dynamics, with SQLMesh's incremental-by-default model being a major lever.
- [The Modern Lakehouse Stack: What Actually Belongs in Production](/data-engineering/modern-lakehouse-stack/) - the architectural context for the optimisation discussion.
