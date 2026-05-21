---
title: "Data Engineering News - May 2026: The Agentic Control Plane, Iceberg v3, and a $2bn Acquisition"
date: 2026-05-21T22:30:00+01:00
draft: false
tags: ['data-engineering', 'news', 'iceberg', 'databricks', 'snowflake', 'airflow', 'ai']
description: "The biggest data engineering stories of the last month - the platform war over the agentic control plane, Apache Iceberg v3 reaching public preview, Airflow 3.1, the Publicis-LiveRamp deal, and what Meta's ingestion rebuild teaches the rest of us."
cover:
  image: /assets/images/data-engineering/data-engineering-news-may-2026.png
  alt: Data engineering news round-up for May 2026
---

*The views in this post are my own personal reflections on the data industry, written in my own time. They are not about any specific employer, team, or colleague, past or present, and do not draw on any non-public information.*

**TL;DR** - The last month had one dominant theme and several solid supporting acts. The dominant theme: the major platforms have stopped competing on storage and SQL and started competing to be the *control plane for enterprise AI agents*. [Snowflake](https://www.snowflake.com/) pushed Cortex Code into that role, [Databricks](https://www.databricks.com/) shipped Apache Iceberg v3 in public preview, and Google wired agentic troubleshooting into managed [Airflow](https://airflow.apache.org/). On the corporate side, Publicis agreed to buy LiveRamp for $2.167bn. And Meta published a genuinely useful account of rebuilding its ingestion system at petabyte scale. Here is what actually changed.

It has been a busy month for data engineering, and unusually for this beat, the busy-ness has a clear shape to it. Most months you get a scattered handful of releases. This month nearly every major story points the same direction: the platforms want to own the layer where AI agents meet your data. This is a round-up of what mattered from the last four weeks or so, with the marketing filtered out.

## The platform war moved to the "agentic control plane"

For years the [Databricks](https://www.databricks.com/) vs [Snowflake](https://www.snowflake.com/) contest was about compute price, SQL performance, and which notebook experience you preferred. That contest is, for practical purposes, over - the technical gap has narrowed to a sliver. The new battleground is which platform becomes the operating system for enterprise AI: the place where agents are defined, governed, and given access to data.

Snowflake made its move explicit. In late April it [expanded Snowflake Intelligence and Cortex Code](https://www.snowflake.com/en/news/press-releases/snowflake-expands-snowflake-intelligence-and-cortex-code-to-power-the-control-plane-for-the-agentic-enterprise/) and described the result, in its own words, as a "control plane for the agentic enterprise." The detail that matters for working engineers is reach: Cortex Code now connects to external systems including AWS Glue, Databricks, and Postgres, and ships as a VS Code extension and a Claude Code plugin. That is a deliberate repositioning - Snowflake is no longer pitching itself as a place to store data, but as a place to orchestrate agents that act on data wherever it lives.

The financial backdrop explains the urgency. Databricks reported crossing a $5.4bn revenue run-rate earlier this year, growing more than 65% year over year with net retention above 140%. Snowflake guided fiscal 2027 product revenue growth of 27%. Both are large, healthy businesses - which means the only way to justify their valuations is to win the next category, not defend the last one. "Agentic control plane" is that next category, and Microsoft Fabric is pushing into the same space. Expect this framing to dominate every vendor keynote for the rest of the year.

## Apache Iceberg v3 reached public preview

The open table format story had its most consequential month in a while. Databricks announced [Apache Iceberg v3 in public preview](https://www.databricks.com/blog/next-era-open-lakehouse-apache-icebergtm-v3-public-preview-databricks), and the feature list is the substance, not the headline:

- **Row lineage** - permanent row IDs and sequence numbers, so you can identify exactly which rows changed between snapshots. This is the foundation for genuinely cheap incremental processing.
- **Deletion vectors** - logical deletes tracked without rewriting data files, which Databricks measures at up to 10x faster than the merge-on-read alternative.
- **VARIANT** - a native column type for semi-structured data such as logs, API payloads, and IoT events, queryable with standard SQL.

The important part is not any single feature - it is that all three are now in the *open specification*. Row lineage and a proper semi-structured type used to be the kind of thing you got only by accepting a proprietary format. Putting them in the spec means you keep cross-engine portability and stop paying the performance tax for it. The same announcement previewed where v4 is heading: adaptive metadata trees, relative path support, and modernised statistics - all aimed at the scaling pain points teams hit at the very top end.

Iceberg interoperability also got better on the Google side. In a [BigQuery and Iceberg interoperability announcement](https://cloud.google.com/blog/products/data-analytics/improved-interoperability-for-your-apache-iceberg-lakehouse), Google detailed bidirectional read and write between BigQuery and other Iceberg engines - Spark, Trino, Flink - through a Google-managed Iceberg REST Catalog, with BigQuery-managed Iceberg tables moving to general availability. The direction of travel is unmistakable: the [Apache Iceberg](https://iceberg.apache.org/) REST catalog is becoming the neutral meeting point that every vendor now has to support, whether they like the loss of lock-in or not.

## Airflow 3.1 and the rise of agentic orchestration

Orchestration had a quietly significant month. Google's Managed Service for Apache Airflow shipped a wave of features - covered in the [Google Data Cloud round-up](https://cloud.google.com/blog/products/data-analytics/whats-new-with-google-data-cloud) - headlined by the general availability of **Airflow 3.1**, plus AI-powered agentic troubleshooting, a managed **Airflow MCP server** for custom agent integration, and declarative YAML-based pipelines.

The MCP server is the piece worth your attention. Exposing Airflow through the Model Context Protocol means an agent can inspect DAG state, diagnose a failed run, and propose a fix without a human translating between the orchestrator and the LLM. Combined with the agentic troubleshooting feature, this is the "ETL to autonomy" trend becoming concrete rather than aspirational. None of it removes the data engineer - but it does change the job from *writing the runbook* to *reviewing what the agent did with it*.

## Publicis to acquire LiveRamp for $2.167bn

The month's big corporate story: on 17 May, Publicis Groupe [agreed to acquire LiveRamp](https://www.publicisgroupe.com/en/news/press-releases/publicis-to-acquire-liveramp-to-accelerate-data-co-creation-for-smarter-agents) for a $2.167bn enterprise value - $38.50 per share in cash, a 29.8% premium to the prior close - with the deal expected to close before the end of 2026.

LiveRamp is a data collaboration and identity platform - the infrastructure that lets companies unify and activate first-party data across partners. Publicis framed the rationale squarely around AI: building "exclusive and proprietary data" to power "the smartest, most differentiated AI agents." Strip away the agency language and the signal is clear. As models commoditise, *proprietary, well-governed data* becomes the durable competitive moat - and a $2bn cheque for a data collaboration platform is the market pricing that belief. For data engineers, this is a reminder that the data we plumb is increasingly treated as a strategic asset class, not a cost centre.

## Meta on rebuilding ingestion at petabyte scale

My favourite read of the month was not an announcement at all. Meta's engineering team published a detailed account of [migrating its data ingestion system at scale](https://engineering.fb.com/2026/05/12/data-infrastructure/migrating-data-ingestion-systems-at-meta-scale/) - the system that pulls several petabytes of social-graph data from MySQL into the data warehouse.

The interesting part is the migration methodology, because it generalises to any team replacing a critical pipeline. Meta used a three-phase lifecycle:

1. **Shadow** - the new system runs in parallel in pre-production against identical source data, with no production impact.
2. **Reverse shadow** - the new system becomes production while the old one runs as a hot backup, preserving instant rollback.
3. **Cleanup** - only after verification does the legacy system get deprecated.

Throughout, correctness was enforced with row counts and checksums, and the cutover was batched across tens of thousands of jobs to stay within capacity limits. There is no novel technology here - and that is exactly why it is worth reading. It is a clear, honest template for de-risking the kind of migration most data teams dread. Worth bookmarking the next time you need to swap out a pipeline nobody is willing to see break.

## Also worth noting: ICDE 2026

On the research side, the 42nd IEEE [International Conference on Data Engineering](https://icde2026.github.io/) ran 4-8 May in Montréal. The headline panel - "What Can Agentic AI Do for Databases?" - tells you everything about where the academic conversation is. Even the research community has converged on the same question the vendors are racing to monetise.

## The honest take

Strip out the noise and one thing is genuinely new this month: the platforms have openly reframed themselves as control planes for AI agents, and they are building the connective tissue - MCP servers, cross-engine catalogs, IDE plugins - to make that real. That is a bigger shift than any single feature release.

Everything else is significant but incremental. Iceberg v3 is important, but it is the spec catching up to what teams already wanted. Airflow 3.1 is a solid release. The LiveRamp deal is a large cheque for a familiar thesis. And the Meta write-up is valuable precisely because it contains no breakthrough - just disciplined engineering.

If you take one practical thing from the month, make it this: the open table format and the catalog are now the parts of your stack the whole industry agrees on, and the agent layer is the part nobody has finished building. That is where the next year of work - and the next year of vendor noise - is going to land.

## Related Reading

- [Databricks vs Snowflake in 2026: An Honest Comparison](/data-engineering/databricks-vs-snowflake-2026/)
- [The Catalog Layer Is the New Battleground - Unity, Polaris, Gravitino, Nessie](/data-engineering/the-catalog-layer-is-the-new-battleground/)
- [Apache Iceberg in 2026: The Open Table Format That Won](/data-engineering/apache-iceberg-2026/)
- [AI-Native Pipelines - What Changes When Your Consumer Is an LLM, Not a Dashboard](/data-engineering/ai-native-pipelines/)
- [Following the Money: Databricks vs Snowflake vs the Open-Source Alternative](/data-engineering/following-the-money/)
