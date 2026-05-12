---
title: "Apache Flink in 2026: Streaming SQL Comes of Age"
date: 2026-05-14T11:00:00+01:00
draft: true
tags: ["data-engineering", "flink", "streaming", "confluent", "real-time", "2026"]
description: "A grounded look at where Apache Flink sits in 2026 after the 2.0 release - disaggregated state, materialised tables, Flink SQL coming of age on Confluent Cloud, and what it means for streaming finally being a normal part of the data engineering stack rather than a specialist niche."
cover:
  image: /assets/images/data-engineering/apache-flink-2026-streaming-sql.jpg
  alt: Apache Flink in 2026 - Streaming SQL Comes of Age Banner
---

For most of the last decade, "real-time" was a thing that was always supposed to be coming and was never quite ready to be the default. The streaming systems were powerful but operationally heavy, the SQL surface was limited, and the failure modes were exotic enough that most teams settled for batch and accepted the latency. By 2026 that has stopped being a defensible position. Apache Flink shipped its 2.0 release with disaggregated state and materialised tables. Confluent Cloud has made managed Flink genuinely operationally simple. The Flink SQL surface is now mature enough to be the default for most streaming workloads. The interesting question is no longer whether streaming is ready for production. It is which workloads should have been streaming all along.

## TL;DR

- **[Apache Flink 2.0](https://flink.apache.org/2025/03/24/apache-flink-2.0.0-a-new-era-of-real-time-data-processing/)** shipped in March 2025, with 2.0.1 in November and **[2.2.0 in December 2025](https://flink.apache.org/2025/12/04/apache-flink-2.2.0-advancing-real-time-data--ai-and-empowering-stream-processing-for-the-ai-era/)**. The release line is the largest set of changes Flink has shipped in years.
- The key architectural changes are **disaggregated state management** (using distributed file systems as the primary state storage rather than local disk), **materialised tables** (a declarative unification of stream and batch), and **asynchronous execution** with the new ForSt state backend.
- **Flink SQL** is the deployment surface that has changed most for real users. It is now ANSI-compliant enough that most analytical SQL works without modification, and the managed-service experience on **[Confluent Cloud for Apache Flink](https://docs.confluent.io/cloud/current/flink/overview.html)** has effectively eliminated the operational complexity that kept teams away from streaming.
- The **[dbt-confluent adapter](https://www.kai-waehner.de/blog/2026/03/26/dbt-meets-apache-flink-one-workflow-for-data-engineers-on-snowflake-bigquery-databricks-and-confluent/)** shipped in early 2026, which means you can now define streaming pipelines as dbt models. This is the integration that has done more for streaming adoption than any technical change in the underlying engine.
- The **Flink Agents** project (currently 0.2.0) is the new AI-era extension: a streaming SQL agent surface that unifies data streams, vector search, embeddings, and LLM calls in one pipeline. It is early but it is the credible answer to the question of how streaming and AI fit together.
- The strategic picture: streaming has moved from a specialist niche into the default for any workload where latency matters and the SQL-on-stream surface is mature enough to be a normal part of the data engineering toolkit.

## What changed with Flink 2.0

Flink 2.0 was the largest release the project has shipped in years - 165 contributors, 25 FLIPs (Flink Improvement Proposals), 369 issues - and the changes are substantive enough to be worth understanding in detail.

**Disaggregated state.** This is the single most important change. The classical Flink architecture kept state local to each task manager - on local disk, with periodic checkpointing to remote durable storage. The model worked but it imposed real constraints. State was bounded by local disk. Scaling a stateful job up or down was expensive because the state had to be redistributed. Recovery from failure required re-reading large amounts of state from checkpoints. The disaggregated state model in 2.0 uses distributed file systems (typically S3 or equivalent) as the primary state storage, with local memory and disk acting as cache. The implication is that state size is no longer bounded by local disk, that scaling is much faster, and that the cloud-native deployment story is genuinely operationally simpler.

**Materialised tables.** The 2.0 release introduced materialised tables as a first-class concept, where the same SQL definition can be served as either a streaming or a batch result depending on what the consumer needs. The unification of stream and batch under a single declarative surface has been a long-standing Flink ambition and 2.0 is the first version where the implementation matches the framing in production.

**Asynchronous execution and ForSt.** The new asynchronous execution model and the ForSt state backend together reduce the latency overhead of stateful operations. The combination is particularly relevant for workloads with large state or frequent checkpointing.

**Flink Agents.** The [Flink Agents](https://flink.apache.org/2026/02/06/apache-flink-agents-0.2.0-release-announcement/) project (currently 0.2.0) is the AI-era extension - a streaming SQL agent surface that integrates LLM calls, vector search, and embedding generation directly into Flink pipelines. The project is early but it is the most credible answer to the question of how streaming systems fit into the new AI-driven workflows.

The 2.2.0 release in December 2025 added further AI-era capabilities, particularly around real-time vector operations and LLM-aware operators. The trajectory is that Flink is positioning itself as the streaming substrate for AI-era workloads, not just for the classical analytics and event-processing use cases.

## Why Flink SQL is the deployment surface

The single biggest practical change for most teams between 2024 and 2026 is that Flink SQL has become operationally simple enough to be the default deployment surface. The historical Flink experience involved writing Java or Scala against the DataStream API, with significant ceremony around state management, watermarks, and checkpointing. The Flink SQL experience in 2026 is dramatically simpler.

The Flink SQL surface is now ANSI-compliant enough that most analytical SQL works without modification. The streaming-specific features - windowing, temporal joins, pattern matching - have clean SQL syntax that maps to the underlying execution model. The Table API in Java and Python provides the same capabilities for teams that prefer a programmatic surface. The operational surface area for a SQL-based deployment is much smaller than for a DataStream-based one, and the result is that teams without dedicated streaming engineers can now run production streaming workloads.

The **dbt-confluent adapter** shipped in early 2026 is the integration that has mattered most for adoption. Data engineers who already know dbt can define streaming pipelines as dbt models, deploy them to Flink compute pools using the standard `dbt run` command, and integrate streaming work into the same CI/CD pipelines that handle batch transformations. The cognitive overhead of "streaming is a different thing" largely goes away when the deployment surface is the same dbt project that handles the batch work.

## Confluent Cloud and the operational simplicity story

The other big shift between 2024 and 2026 is that **Confluent Cloud for Apache Flink** has made managed Flink operationally simple enough to be a default option. The historical experience of running Flink involved managing clusters, configuring state backends, tuning checkpointing intervals, and debugging exotic state issues. Confluent's managed offering hides all of this. You deploy a Flink SQL statement to a compute pool and the platform handles the rest.

The managed-service maturity has changed the calculation for teams considering streaming. The operational cost of streaming used to be a significant fraction of the total cost - sometimes the dominant fraction. The managed offering reduces it to roughly the same as the operational cost of a managed batch warehouse, which means the decision becomes about whether streaming is the right architecture for the workload rather than about whether the team has the bandwidth to run a streaming system.

The other thing the managed service has done is to lower the floor of viable streaming use cases. Workloads that were too small to justify dedicated streaming infrastructure - small dashboards that need to be a few seconds fresh rather than a few minutes, internal analytics that benefit from low-latency updates, fraud-detection systems that need to react quickly but do not have huge data volumes - now have a cost-effective deployment path. The volume of net-new streaming workloads in 2026 is dominated by these smaller cases, not by the large enterprise deployments that have always justified the investment.

## What real teams are actually doing with Flink

The deployment patterns that are winning in 2026 cluster around a few specific shapes.

**Change Data Capture pipelines.** The single largest production use case for Flink in 2026 is CDC - capturing changes from operational databases (typically Postgres or MySQL) and applying them to analytical systems (typically a lakehouse or data warehouse). Flink SQL with the [Debezium](https://debezium.io/) connectors is the standard pattern, and the result is a continuously-updated mirror of the operational data in the analytical system with sub-second latency.

**Streaming feature pipelines.** For teams running production machine learning systems, Flink is increasingly the default for the feature pipelines that compute the features used at inference time. The pattern is to compute features once in the streaming pipeline, write them to a feature store, and read them at inference. The latency requirements for many ML features make streaming the only credible architecture and Flink is the dominant engine for this work.

**Real-time analytics on lakehouse data.** With Iceberg, Delta, and increasingly DuckLake as the underlying storage format, Flink can read and write lakehouse tables directly. The pattern of using Flink to maintain low-latency views over lakehouse data is increasingly common, and the integration with the table formats has matured to the point where it is production-quality.

**Event-driven application logic.** Flink continues to be a credible engine for the event-driven application logic that has been its historical use case - fraud detection, alerting, complex event processing, business rules over event streams. The Flink SQL surface has made these workloads much more accessible to teams without dedicated streaming engineers.

**AI-era streaming workloads.** The Flink Agents project and the broader AI integration in 2.2.0 are pulling Flink into a new category of workloads - LLM-driven event processing, real-time vector search, streaming RAG (Retrieval-Augmented Generation) pipelines. The deployments are early but the trajectory is clearly toward Flink being a serious option for the streaming side of AI applications.

## Where Flink is not the right answer

The honest case against Flink in 2026 is also worth being clear about.

**Pure batch workloads.** For workloads that are genuinely batch - daily, weekly, monthly aggregations with no latency requirement - the batch warehouses (Snowflake, BigQuery, Databricks) are still operationally simpler and competitively priced. Flink can do batch work but the framework is optimised for streaming, and the choice is mostly about whether you also have streaming workloads that share the infrastructure.

**Very simple streaming workloads.** For trivial transformations on event streams - filter, route, simple enrichment - a stream processor like [Materialize](https://materialize.com/) or a simpler tool like [Bytewax](https://bytewax.io/) or [Quix Streams](https://quix.io/) may be the right choice. Flink's full power is overkill for these workloads and the simpler tools have lower operational overhead.

**Workloads requiring exotic latency.** Flink is fast enough for most "real-time" workloads where "real-time" means seconds or sub-seconds. For workloads requiring sub-millisecond latency - high-frequency trading, certain ad-tech use cases, some IoT applications - more specialised systems remain the right choice.

**Teams without streaming experience.** Even with the managed-service improvements, Flink has a steeper learning curve than the equivalent batch systems. The streaming concepts - watermarks, event time vs processing time, exactly-once semantics, state management - are real and they have to be understood even when the platform hides the operational details. Teams without any streaming experience should expect a real ramp-up period.

## The competitive landscape

Flink is the dominant streaming engine in 2026 but it is not unchallenged. The competitive picture is worth understanding.

**[Apache Spark Structured Streaming](https://spark.apache.org/streaming/)** remains a credible alternative, particularly for teams already deeply invested in Spark for batch work. The micro-batch model gives up some latency for simplicity, and for many workloads the trade-off is acceptable. The Databricks-managed Spark experience is competitive with Confluent's managed Flink for teams that prefer the Databricks ecosystem.

**[Materialize](https://materialize.com/)** is the SQL-first streaming database that has built significant adoption around its incremental view maintenance model. Materialize is operationally simpler than Flink for the workloads it handles, but the workload coverage is narrower. The two are complementary more than competitive in most deployments.

**[RisingWave](https://www.risingwave.com/)** is a streaming database built around the same incremental view maintenance approach as Materialize, with a focus on cloud-native deployment and a Postgres-compatible interface. The trajectory is similar to Materialize - smaller surface area than Flink, but operationally simpler for the workloads it handles.

**The lakehouse-native streaming options.** Both Databricks (with Spark Streaming) and Snowflake (with Snowpipe Streaming and Dynamic Tables) have invested heavily in streaming capabilities native to their platforms. For teams already using one of these platforms, the native streaming option may be operationally simpler than introducing Flink as a separate system.

The honest framing is that Flink wins on capability breadth and on the complex stateful workloads that the other options cannot handle as cleanly. The other options win on operational simplicity for the workloads they cover. For most teams in 2026, the decision is between Flink (for the full-spectrum streaming use case) and one of the simpler options (for narrower but more contained workloads).

## The controversial parts

Three claims in the Flink-and-streaming conversation deserve more pushback than they typically get.

The first is the claim that streaming is now the default and batch is the exception. The empirical evidence is that streaming has grown a lot but batch is still much larger by a wide margin. The reasonable framing is that streaming is now a normal part of the data engineering toolkit rather than a specialist niche, not that it has replaced batch.

The second is the claim that managed Flink has eliminated all of the operational complexity. The framing is mostly right at the platform level but the application-level concerns - thinking about watermarks, handling late-arriving data, reasoning about exactly-once semantics, debugging state issues - have not gone away. Teams adopting streaming need to take the application-level concepts seriously even when the platform handles the rest.

The third is the claim that Flink Agents is going to be the dominant pattern for AI-era streaming workloads. The project is early, the deployment patterns are still being worked out, and the competitive landscape for AI-integrated streaming is wide open. The empirical record by end of 2026 will be more informative than the current trajectory.

## Where this is heading

The most likely shape of 2027-2028 is that streaming becomes a normal part of the data engineering stack for most teams, with Flink as the dominant engine for the complex workloads and the simpler streaming options handling the workloads where they fit. The managed-service improvements will continue and the deployment patterns will continue to converge with the patterns used for batch work.

The other prediction worth making is that the AI integration is going to drive the next wave of streaming adoption. The real-time RAG patterns, the streaming feature pipelines for ML, the LLM-driven event processing - these are all workloads where streaming is the natural architecture, and the AI side of the industry is going to pull more teams into streaming than the classical analytics use cases ever did.

For people building with data engineering tools today, the practical guidance is to treat streaming as a default tool in the kit rather than a specialist niche. The cost of trying Flink for a workload is much lower than it used to be. The integration with the rest of the stack (dbt, lakehouse tables, the broader data platform) has matured. The talent pool has grown. The patterns are documented. The streaming question in 2026 is not "can we" but "should we for this workload," and for a growing fraction of workloads the answer is yes.

## Further Watching

### A deep dive into Flink SQL - Jark Wu, Kurt Young
{{< youtube "KDD8e4GE12w" >}}

### What is Apache Flink? (Confluent)
{{< youtube "PVoc5tRr6to" >}}

### scale.bythebay.io: Stephan Ewen, Apache Flink and the Next Wave of Stream Processing Applications
{{< youtube "GB-icNc9QtE" >}}

### The State of Flink and how to adopt Stream Processing - Stephan Ewen
{{< youtube "EMle4ChUcEk" >}}

### DuckDB Co-Creator Hannes Mühleisen on Why Single-Node Beats Distributed
{{< youtube "o53onmgnQDU" >}}

## Related Reading

- [Real-Time Data Processing: Stream Processing vs Batch Processing](/data-engineering/stream-vs-batch-processing/) - the broader streaming vs batch comparison Flink sits inside.
- [AI-Native Pipelines - What Changes When Your Consumer Is an LLM, Not a Dashboard](/data-engineering/ai-native-pipelines/) - the AI-era streaming use cases Flink Agents targets.
- [dbt vs SQLMesh: The Transformation Layer Showdown in 2026](/data-engineering/dbt-vs-sqlmesh-2026/) - the transformation-layer story that now integrates with Flink via the dbt-confluent adapter.
- [Apache Iceberg in 2026: The Open Table Format That Won](/data-engineering/apache-iceberg-2026/) - the storage layer Flink increasingly reads and writes against.
- [The Modern Lakehouse Stack: What Actually Belongs in Production](/data-engineering/modern-lakehouse-stack/) - the broader stack context.
