---
title: "Apache Arrow and the Composable Data Stack"
date: 2026-05-14T09:00:00+01:00
draft: true
tags: ["data-engineering", "apache-arrow", "datafusion", "composable", "open-source", "2026"]
description: "A grounded look at the Apache Arrow ecosystem and the composable data stack thesis - how a memory format from 2016 became the universal substrate for DuckDB, Polars, DataFusion, Velox, and most of the next generation of data infrastructure, and what that means for builders in 2026."
cover:
  image: /assets/images/data-engineering/apache-arrow-composable-stack.jpg
  alt: Apache Arrow and the Composable Data Stack Banner
---

The most consequential piece of data infrastructure built in the last decade is not a database, a warehouse, or a transformation framework. It is a memory format. Apache Arrow defines how columnar data is laid out in memory, and that definition has become the substrate the next generation of analytical engines is being built on. DuckDB uses it. Polars uses it. DataFusion uses it. Velox uses it. Spark uses it for its inter-process boundaries. The cumulative effect is that the data stack has stopped being a stack of vertically-integrated systems and started looking like a stack of swappable components that all speak the same language. This is what the people who work on it call the composable data stack, and 2026 is the year the thesis has visibly worked.

## TL;DR

- **[Apache Arrow](https://arrow.apache.org/)** is a language-independent columnar memory format and a set of libraries built around it. The format was started by [Wes McKinney](https://wesmckinney.com/) (the creator of pandas) and a coalition of contributors in 2016 and is now the de-facto standard for in-memory columnar data.
- **The composable data stack** is the thesis that data infrastructure should be built from interoperable components - storage formats, memory formats, query engines, execution layers - that can be mixed and matched, rather than from monolithic vertically-integrated systems. Arrow is the connective tissue that makes the thesis work.
- The key components of the 2026 composable stack are: **Arrow** (memory format and libraries), **Parquet** (file format), **Iceberg/Delta/DuckLake** (table formats), **DuckDB / DataFusion / Velox / Polars** (compute engines), and **the SQL parser layer** (SQLGlot and equivalents).
- The reason the composable stack matters is that it changes the cost of building new data infrastructure. A team that wants to ship a new analytical engine in 2026 does not have to build the memory format, the file readers, the parser, the optimiser, or the execution engine from scratch - they pick the components that fit their use case and integrate.
- The commercial implications are large. The vertically-integrated platforms (Snowflake, Databricks, the major cloud warehouses) increasingly compete with stacks assembled from open components, and the cost differential is significant. The strategic response from the platform vendors has been to absorb the composable components into their offerings.
- **[Apache DataFusion](https://github.com/apache/datafusion)** is the part of the composable stack that has changed the picture most in 2025-2026. It is a Rust-based query engine that uses Arrow as its memory format and has become the foundation for a growing number of production systems - including parts of Apache Spark, Polars, and several commercial offerings.

## What Arrow actually is

The simplest way to understand Apache Arrow is that it specifies how columnar data should be laid out in memory. Not on disk - on disk you use [Parquet](https://parquet.apache.org/), or ORC, or Avro, depending on the use case. In memory, after you have read the file and decoded it, the resulting data structure needs to be in a format that the compute layer can work with. Arrow says: it should be in this specific columnar layout, with these specific buffer conventions, these specific null-handling rules, and these specific metadata structures.

That specification turns out to do an enormous amount of work. Once everyone agrees on the in-memory format, you can pass data between systems without serialisation. You can hand a chunk of Arrow data from a file reader to a query engine, from a query engine to a Python pandas DataFrame, from pandas to a machine learning library, from the machine learning library back to a database client - without ever serialising and deserialising the data. The serialisation cost was historically one of the dominant overheads in real-world data pipelines, and Arrow effectively eliminates it whenever both sides of a boundary are Arrow-aware.

The other thing the specification does is enable the libraries built on top of it to share work. The Arrow C++ library implements file readers (Parquet, CSV, JSON, ORC), compute kernels (filtering, aggregation, joins), and inter-process communication (Arrow Flight, Arrow IPC). The Rust library implements the same things in Rust. The Python library wraps the C++ library. The Java library, the Go library, the JavaScript library, the R library - all of them implement substantially the same functionality on top of the same memory format. A new analytical engine that wants to read a Parquet file does not have to write a Parquet reader; it imports the one the Arrow project ships and gets reliable, well-tested file reading for free.

## What the composable stack looks like in 2026

The composable data stack thesis - that data infrastructure should be built from interchangeable components - was articulated by Wes McKinney and others in the Arrow community several years ago. By 2026 it is no longer a thesis. It is the visible architecture of an increasing fraction of the actual data infrastructure being shipped.

The components that make up the 2026 stack:

**Storage and table formats.** [Parquet](https://parquet.apache.org/) is the dominant columnar file format, with Arrow defining the memory representation of decoded Parquet data. [Iceberg](/data-engineering/apache-iceberg-2026/), Delta Lake, and Hudi are the dominant table formats on top of Parquet, with [DuckLake](/data-engineering/duckdb-in-process-analytics-eating-the-stack/) emerging as a credible alternative. The catalog layer ([Unity, Polaris, Gravitino, Nessie](/data-engineering/the-catalog-layer-is-the-new-battleground/)) sits above the table formats and manages the metadata.

**Compute engines.** [DuckDB](https://duckdb.org/) is the single-node default for analytical SQL. [Polars](https://pola.rs/) is the DataFrame-first alternative, particularly popular in Python and machine learning workflows. [Apache DataFusion](https://github.com/apache/datafusion) is the embeddable Rust query engine used as a foundation for other systems. [Velox](https://velox-lib.io/) is the C++ unified execution engine from Meta, used as the execution layer in [Presto](https://prestodb.io/) and a growing list of other systems. [GPU-accelerated engines](https://www.rapids.ai/) (cuDF, RAPIDS) handle the workloads where the GPU matters.

**SQL parsing.** [SQLGlot](https://github.com/tobymao/sqlglot) has emerged as the universal SQL parser, used by SQLMesh and a growing list of other systems. The parser layer separates the lexical analysis of SQL from the execution, which makes it possible to write SQL once and target multiple engines.

**Inter-process communication.** Arrow Flight is the standard wire format for shipping Arrow data between processes. The protocol is built on gRPC and is used by an increasing number of database drivers, including the Databricks SQL connector, the BigQuery client, and many of the open-source data tools.

The architecture means that a single workload can flow through multiple components without overhead. A query might be parsed by SQLGlot, optimised by DataFusion, executed against Iceberg tables read by Arrow-aware Parquet readers, with intermediate results streamed via Arrow Flight to a downstream consumer that uses Polars for the post-processing. The pieces are different and they are built by different teams, but they speak the same memory format and the same wire protocol, so the composition is essentially free.

## Why DataFusion is the story

Of all the components of the composable stack, DataFusion has changed the picture most in 2025-2026, and it is worth dwelling on why.

DataFusion is a Rust-based query engine that uses Arrow as its memory format. The project started in 2017 as a Rust port of Spark's Catalyst optimiser and has grown into a full SQL query engine with planner, optimiser, and execution engine. The technical contributions are real - the engine is fast, the codebase is well-engineered, the API is clean - but the strategic significance is bigger than the technical merit alone.

DataFusion is **embeddable**. Other systems can use it as a library rather than as a separate service. The cost of adding SQL execution to an application is much smaller than it was a few years ago, because DataFusion is a dependency you can add to your build rather than a service you have to operate.

DataFusion is **modular**. The parser, the optimiser, the execution engine, the catalog, the storage layer - all of these are pluggable. You can take DataFusion's optimiser and combine it with your own storage layer, or use its execution engine with your own parser. The modularity is the property that has made it the foundation for a growing number of production systems rather than a competing product to other engines.

DataFusion is **Apache-licensed and community-governed**. The project is hosted at the Apache Software Foundation, the contributors come from many organisations, and the governance model is permissive enough that commercial vendors can build on it without worrying about licence or governance risk.

The combination has made DataFusion the embedded query engine of choice for a growing list of systems. Polars uses it for its lazy query optimisation. Several commercial offerings - InfluxDB 3.0, Greptime, Comet (the Spark accelerator), GreptimeDB - use it as their execution layer. Parts of Apache Spark are being rewritten on top of DataFusion. The trajectory is that DataFusion is becoming to query execution what Arrow is to memory format - the substrate that everyone else builds on.

## What the composable stack actually enables

The reason to care about the composable stack is not the architectural elegance. It is what the architecture makes possible at the application level.

**New analytical engines can be built much faster.** A team that wants to ship an analytical database in 2026 does not need to build a SQL parser (use SQLGlot), an optimiser (use DataFusion's), an execution engine (use DataFusion's or build one on Arrow), a Parquet reader (use Arrow's), a memory format (Arrow), or an inter-process protocol (Arrow Flight). The team can focus on the parts of the system that are actually differentiated - the workload model, the deployment story, the user experience - rather than on rebuilding the substrate.

**Interoperability between systems is essentially free.** A pipeline that uses Parquet on object storage, Arrow in memory, DataFusion for SQL execution, and Polars for the Python post-processing has zero serialisation overhead at the boundaries between components. Compare this to a pipeline that uses different in-memory formats at each stage, where the cost of converting between formats can dominate the total compute cost.

**The platform vendors compete on different axes than before.** The historical moat for Snowflake or Databricks was that they did everything end-to-end. The composable stack means a customer can assemble a credible alternative from open-source components, and the platform vendors increasingly compete on managed-service quality, on developer experience, and on the integrated workflow rather than on raw capability. The strategic response from the vendors has been to absorb the composable components - Databricks open-sourcing Unity Catalog, Snowflake's Iceberg adoption, both vendors supporting Arrow at their boundaries - which is itself an admission that the composable thesis has won.

**The cost of running data infrastructure has gone down.** A team running analytical workloads in 2026 on a stack of open components - Parquet on S3, DuckDB or DataFusion for compute, Iceberg or DuckLake for the catalog, dbt or SQLMesh for transformations - typically pays a fraction of what an equivalent workload on a managed warehouse would cost. The trade-off is operational - someone has to assemble and maintain the stack - but for teams that have the engineering capacity, the cost savings are real and significant.

## Where the composable stack is not the right answer

The honest case against the composable stack is also worth being clear about.

**Operational complexity.** Assembling a stack from components requires more engineering capacity than buying a managed warehouse. The components mostly work well together but they are not zero-touch, and the teams that have tried to run composable stacks without sufficient engineering investment have generally regretted it. The managed platforms exist because operational simplicity is genuinely valuable.

**Maturity in specific areas.** The composable stack is mature for batch analytical workloads. It is less mature for streaming, for OLTP, for the very high-concurrency analytical workloads that the established warehouses handle well, and for the complex workload-management features that large enterprises rely on. The vendors continue to lead on these dimensions.

**Support and accountability.** When something breaks in a composable stack, the accountability is distributed across multiple open-source projects. When something breaks in a managed warehouse, there is a vendor on the other end of a support contract. For teams that need vendor support, the composable stack is the wrong choice regardless of the cost arithmetic.

**Talent.** The composable stack requires engineers who can reason about all of the components and how they fit together. The talent pool that can do this is smaller than the talent pool that can use a managed platform, and the salaries are higher. The total-cost-of-ownership calculation has to include the people, not just the compute.

## The controversial parts

Three claims in the composable-stack conversation deserve more pushback than they typically get.

The first is the claim that the composable stack will displace the managed platforms. The empirical evidence is that the two are converging rather than replacing each other. Snowflake and Databricks are absorbing the composable components into their offerings. The composable stack vendors (Tobiko, MotherDuck, the various DataFusion-backed startups) are building managed offerings on top of the open components. The likely end state is a mix where the underlying components are open and the deployment story can be either managed or self-assembled depending on the customer's needs.

The second is the claim that the composable stack is cheaper than the managed platforms. It is cheaper on compute. It is often more expensive on engineering. The total-cost-of-ownership comparison depends on the specific workload, the size of the team, and the value of the operational simplicity, and the composable stack is not uniformly cheaper.

The third is the claim that the standardisation around Arrow is permanent. The format is well-designed and broadly adopted, but the history of data infrastructure suggests that no format is permanent. The next generation of hardware (particularly accelerators with non-standard memory models) is going to put pressure on the Arrow specification, and the long-run question is whether the format evolves to accommodate or whether something else replaces it. The current trajectory is favourable to Arrow but the future is not guaranteed.

## Where this is heading

The most likely shape of 2027-2028 is that the composable stack continues to win share in the long tail of data infrastructure work, that the managed platforms continue to dominate the high-end enterprise market, and that the two ecosystems continue to converge on the underlying technology even as they remain commercially distinct. Arrow will continue to be the connective tissue, DataFusion will continue to be the embedded query engine of choice, and the components will continue to mature in directions that make them easier to assemble.

The other prediction worth making is that the composable thesis is going to extend further into the platform vendors than it has already. The unbundling has happened at the storage and catalog layers. The compute layer is next, and the vendor offerings that emerge over the next two years are likely to be increasingly modular in their internals even when the customer-facing surface remains integrated.

For people building with data engineering tools today, the practical guidance is to understand the composable stack even if you do not adopt it wholesale. The components are showing up inside the managed platforms whether you notice them or not, the open ecosystem is growing fast enough to be a real competitor for any new workload, and the architectural patterns are increasingly the default in the field. The teams that understand Arrow, DataFusion, and the broader composable landscape are better positioned for the next several years of data infrastructure decisions than the teams that do not.

## Further Watching

### Future of DataFrames and Data Systems with Wes McKinney
{{< youtube "vY3QfLCK7ms" >}}

### DC_THURS: Apache Arrow w/ Wes McKinney
{{< youtube "G2ljqxRxqW0" >}}

### Apache Arrow: High-Performance Columnar Data Framework
{{< youtube "YhF8YR0OEFk" >}}

### "Apache Arrow and the Future of Data Frames" with Wes McKinney
{{< youtube "fyj4FyH3XdU" >}}

### Wes McKinney - Apache Arrow: Present & Future
{{< youtube "SBy1WtA3b6o" >}}

## Related Reading

- [DuckDB: The In-Process Analytics Engine Eating the Stack](/data-engineering/duckdb-in-process-analytics-eating-the-stack/) - one of the most important consumers of the Arrow memory format.
- [The Modern Lakehouse Stack: What Actually Belongs in Production](/data-engineering/modern-lakehouse-stack/) - the production architecture that increasingly maps to the composable thesis.
- [dbt vs SQLMesh: The Transformation Layer Showdown in 2026](/data-engineering/dbt-vs-sqlmesh-2026/) - the transformation-layer side of the composable story, with SQLGlot as the parser layer.
- [Apache Iceberg in 2026: The Open Table Format That Won](/data-engineering/apache-iceberg-2026/) - the table-format layer of the composable stack.
- [The Catalog Layer Is the New Battleground - Unity, Polaris, Gravitino, Nessie](/data-engineering/the-catalog-layer-is-the-new-battleground/) - the catalog layer that the composable stack sits on top of.
