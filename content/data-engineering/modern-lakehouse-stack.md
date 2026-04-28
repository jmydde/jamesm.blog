---
title: "The Modern Lakehouse Stack: What Actually Belongs in Production"
date: 2026-05-08T08:00:00+01:00
draft: false
tags: ["lakehouse", "data-engineering", "architecture", "iceberg", "databricks", "platform"]
description: "A working data engineer's view of what genuinely belongs in a 2026 lakehouse stack, the layers that have shaken out, and the parts of the marketing landscape that deserve to be ignored."
cover:
  image: assets/images/data-engineering/modern-lakehouse-stack.jpg
  alt: The Modern Lakehouse Stack Banner
---

The word "lakehouse" has been doing a lot of work for the last five years. It has been used to describe everything from a thin SQL layer over object storage to a fully integrated platform with governance, lineage, ML training, and BI built on top. Like most umbrella terms, this elasticity has been useful for marketers and confusing for engineers.

This post is the version of the conversation I would have with a senior engineer who has been asked to "build out our lakehouse" and wants to know which pieces are load-bearing and which are noise. It draws on what I have actually seen ship and survive in production data platforms in 2026, and it tries to be specific about why each layer is in the stack rather than just describing the picture as a fait accompli.

## What the lakehouse actually solved

It is worth being clear about why this architecture exists at all, because the reasoning explains the shape of the stack.

For most of the 2000s and 2010s, you had two roughly disjoint worlds. Data warehouses, which were closed, expensive, fast for analytics, and structurally hostile to unstructured or semi-structured data. And data lakes, which were open, cheap, flexible, and unable to give you the transactional guarantees and query performance of a warehouse. You picked one or you ran both, and most large organisations ran both, with painful and brittle pipelines moving data between them.

The [lakehouse architecture](https://en.wikipedia.org/wiki/Data_lakehouse), as articulated by [Databricks](https://www.databricks.com/blog/2020/01/30/what-is-a-data-lakehouse.html) and others around 2020, was the thesis that you could get warehouse-like guarantees on lake-shaped data by adding a thin metadata layer. Open table formats sit on top of object storage, the metadata gives you ACID transactions and schema enforcement, and you keep the openness, the cost profile, and the multi-engine flexibility of the lake.

Six years later, that thesis has held up. The lakehouse is now the default architectural assumption for new data platforms, and the question has shifted from "is this a real architecture?" to "which specific pieces should I actually use?"

## The layered model

A lakehouse stack in 2026 has roughly seven layers, from bottom to top. Each layer has a few real choices and a long tail of options that are mostly noise. I will go through them in order.

### Layer 1: Object storage

This is the foundation, and the choice is almost trivial. You are using [S3](https://aws.amazon.com/s3/), [Azure Data Lake Storage](https://azure.microsoft.com/en-us/products/storage/data-lake-storage/), [Google Cloud Storage](https://cloud.google.com/storage), or one of the open-source equivalents like [MinIO](https://min.io/) for on-prem. The differences between the three major cloud options are less significant than the cost of being on the wrong cloud for the rest of your stack. Pick the one that matches your organisation's cloud commitment.

The thing that matters at this layer is not the storage product itself. It is the bucket layout, the partitioning scheme, and the lifecycle rules. These are the boring decisions that determine whether your platform stays cost-controllable in three years.

### Layer 2: Open table format

This is where the real architectural choice is. The three contenders are [Apache Iceberg](https://iceberg.apache.org/), [Delta Lake](https://delta.io/), and [Apache Hudi](https://hudi.apache.org/), and the situation in 2026 is clearer than it has ever been.

Iceberg has won the open standard battle. It is the format that both Snowflake and Databricks now treat as a first-class citizen, it is supported across the broadest range of engines, and the catalog ecosystem around it has matured into something usable. If you are starting fresh in 2026, Iceberg is the default choice and it should be a positive case to use anything else.

Delta Lake remains the natural choice if you are already deep in the Databricks ecosystem and you do not need cross-engine portability. It is the format Databricks's own tooling is most tightly integrated with, and the performance characteristics on Databricks-native workloads are excellent.

Hudi is the format I increasingly do not see in new builds. It has its strengths, particularly around upsert-heavy workloads, but the gravitational pull of the other two has left it as a niche choice rather than a contender.

I wrote about this in more detail in [the Iceberg-in-2026 deep dive](/data-engineering/apache-iceberg-2026/), but the short version is: choose Iceberg unless you have a specific reason not to.

### Layer 3: Catalog

This is the layer where most lakehouse platforms in 2026 are actively shifting, and where the marketing is the loudest.

A catalog is the metadata service that knows where your tables are, who can read them, what their schemas look like, and how to find them across multiple engines. In an Iceberg world, the catalog choice is increasingly the most important architectural decision in the platform, because it determines who can use your data and how.

The serious options in 2026 are [Unity Catalog](https://www.databricks.com/product/unity-catalog) (now open-sourced), [Polaris Catalog](https://www.snowflake.com/en/blog/introducing-polaris-catalog/) from Snowflake, and [Apache Nessie](https://projectnessie.org/) for teams that want a fully open-source git-like catalog with branching semantics. The choice between Unity and Polaris tends to follow your engine choice, since each is a first-class catalog for its own platform and a second-class one for the other. The choice of Nessie is appropriate for teams that genuinely value git-style data versioning enough to manage the additional operational overhead. I wrote about the operational realities of running Unity at scale in [Unity Catalog in practice](/data-engineering/unity-catalog-in-practice-2026/).

For most teams in 2026, the catalog choice is downstream of which compute engine they have already committed to. Picking your catalog before your engine is usually putting the cart before the horse.

### Layer 4: Compute engine

This is where the actual processing happens. The serious options for a lakehouse in 2026 are [Databricks](https://www.databricks.com/), [Snowflake](https://www.snowflake.com/), [Trino](https://trino.io/) or its commercial cousin [Starburst](https://www.starburst.io/), and increasingly [DuckDB](https://duckdb.org/) for smaller workloads.

Databricks remains the strongest choice if you have meaningful Spark workloads and machine learning training that lives near your data. Snowflake is the strongest choice if your workloads are mostly SQL analytics and you value operational simplicity over raw flexibility. Trino is the strongest choice if you need a federated query layer across multiple data sources, and if you have the engineering talent to operate it at scale. DuckDB is the strongest choice for workloads that do not need a cluster and for in-process analytics where the data fits on one machine. The Databricks-vs-Snowflake choice in particular has its own dedicated [head-to-head comparison](/data-engineering/databricks-vs-snowflake-2026/), and Snowflake's recent move to host Iceberg natively is covered in [Snowflake storage for Apache Iceberg](/data-engineering/snowflake-apache-iceberg-storage/).

The mistake I see organisations make is committing to a single engine because it feels architecturally cleaner. In practice, the lakehouse architecture is most powerful when you can run different engines against the same tables without copying data. That is the whole point of open formats. Pick a primary engine, but build the platform such that other engines can be added when the use case demands it.

### Layer 5: Orchestration

Above the compute layer sits orchestration: the system that defines what jobs run, when they run, what their dependencies are, and what to do when they fail.

The choice is essentially between [Apache Airflow](https://airflow.apache.org/), [Dagster](https://dagster.io/), [Prefect](https://www.prefect.io/), or the platform-native option from your engine vendor (Databricks Workflows, Snowflake Tasks, etc.). On Databricks specifically, the declarative pipeline story is now [Lakeflow](/data-engineering/lakeflow-declarative-pipelines-2026/), which I have written about separately.

Airflow remains the dominant choice for orchestration that needs to span multiple systems, especially if your platform involves data movement between non-lakehouse systems. Dagster has a meaningfully better developer experience and asset-centric model that fits the lakehouse paradigm well. Prefect is a credible third option with strong cloud-native ergonomics.

For most teams, the orchestration layer is the part of the platform that engineers spend the most day-to-day time in, so the choice should weight developer experience and observability more than raw feature count. Pick the one your team will be happy operating in five years.

### Layer 6: Transformation

This is where raw data becomes the data products that downstream users actually consume. In 2026, this layer has consolidated heavily around [dbt](https://www.getdbt.com/) and [SQLMesh](https://sqlmesh.com/), with dbt being dominant and SQLMesh being the credible alternative for teams that need stronger data warehouse semantics around environments and column-level lineage.

The thing to recognise about this layer is that the transformation tool is not really the value. The value is the discipline the tool enforces: code-defined transformations, version-controlled SQL, dependency-aware scheduling, declarative tests. Almost any tool that enforces these properties will be a major step up from hand-rolled scripts. The choice between dbt and SQLMesh is one of degree, not kind.

### Layer 7: Governance and observability

This is the layer that gets neglected and is the most expensive to retrofit. It includes data quality monitoring (tools like [Great Expectations](https://greatexpectations.io/) or [Soda](https://www.soda.io/)), data lineage (typically delivered through your catalog or a dedicated tool like [OpenLineage](https://openlineage.io/)), data observability (tools like [Monte Carlo](https://www.montecarlodata.com/) or open-source [Marquez](https://marquezproject.ai/)), and access control (delivered through your catalog).

Skipping this layer is the single most common mistake I see in newly-built lakehouse platforms. Teams build the first six layers, ship some pipelines, and then discover six months later that they have no idea whether the data is correct, who is using it, or what would break if a source schema changed. Retrofitting governance onto a running platform is several times the cost of building it in from the start.

## What I would tell a team starting today

If you are building a new lakehouse in 2026, the default stack is something like:

- Object storage on your existing cloud
- Iceberg as the table format
- Unity or Polaris as the catalog, depending on your primary engine
- Databricks or Snowflake as the primary engine
- Dagster or Airflow for orchestration
- dbt for transformation
- A dedicated data quality and observability tool from day one

This is not the stack for every team. It is the stack you should deviate from with intent, not by default. The shape of a 2026 lakehouse has stabilised enough that the cost of accidentally building something exotic is meaningful, and the benefit of staying close to the well-trodden path is real: better tooling, better hiring, better support, and better integrations across the rest of your data ecosystem.

The thing not to do is to spend six months evaluating options before shipping anything. The lakehouse architecture rewards iteration. Build a first version that runs end-to-end on a small slice of your data, prove that the bones work, and then expand. The platforms that succeed are the ones that get to a working state quickly and improve from there. The platforms that fail are the ones that try to architect their way to perfection before any data has flowed.
