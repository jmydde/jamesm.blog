---
title: "The Catalog Layer Is the New Battleground - Unity, Polaris, Gravitino, Nessie"
date: 2026-05-02T15:00:00+01:00
draft: false
tags: ['data-engineering', 'catalog', 'iceberg', 'unity-catalog', 'lakehouse', 'governance', '2026']
description: "The open table format wars are over. The fight has moved up to the catalog layer where Unity, Polaris, Gravitino, and Nessie are now competing. A grounded look at what each one is, what they share, and where the battle lines actually run."
cover:
  image: /assets/images/data-engineering/catalog-layer-battleground.jpg
  alt: Catalog Layer Battleground Banner
---

## TL;DR

- With the [open table format wars largely settled](/data-engineering/iceberg-vs-delta-vs-hudi-2026/), the strategic fight in 2026 has moved up to the **catalog layer** - the system that manages tables, namespaces, governance, and access.
- Four credible open or open-ish catalogs are now in serious play: **[Unity Catalog](https://www.unitycatalog.io/)** (Databricks), **[Polaris](https://polaris.apache.org/)** (Snowflake), **[Apache Gravitino](https://gravitino.apache.org/)** (Datastrato/community), and **[Project Nessie](https://projectnessie.org/)** (Dremio/community).
- All four implement the **Iceberg REST catalog spec** to varying degrees, which means clients can talk to them through a common protocol. The differentiation has moved to **governance, multi-tenancy, lineage, federation, and developer experience**.
- **Unity** is the most production-mature and the most coupled to Databricks. **Polaris** is the cleanest open implementation of the REST spec. **Gravitino** is the most ambitious in scope - aiming to catalog non-table assets too. **Nessie** is the most opinionated about Git-style branching for data.
- The winning catalog will probably not be a single project. It will be **the protocol** (Iceberg REST) plus **multiple compliant implementations** plus **federation between them**. That is the picture 2026 ends with.

## Why The Catalog Layer Matters Now

A table format defines how data is laid out on disk. A catalog defines:

- **What tables exist.** Names, schemas, partitions, snapshots.
- **Where they live.** Storage locations, region, account.
- **Who can see them.** Authentication, authorisation, masking, row-level security.
- **What is happening to them.** Audit logs, lineage, access history.
- **How they relate to each other.** Namespaces, hierarchies, dependencies.

In 2022 most of this lived inside whichever vendor owned your warehouse. The data and the catalog came as a bundle. Once Iceberg made the data layer truly portable, the catalog was suddenly the binding that held the bundle together. Move the data, and you have to take the catalog with you - or risk losing every governance and access decision you ever made.

That is why the catalog layer is now the strategic battleground. Whoever owns the catalog owns the governance plane, the access controls, the lineage, and - in practice - the customer relationship.

## The Four Catalogs

### Unity Catalog

[Unity Catalog](https://www.unitycatalog.io/) is the most mature of the four. Databricks open-sourced it in 2024 and continues to ship aggressively. Unity Catalog is the catalog you adopt if you want production-ready governance today.

**Strengths:**

- **Maturity.** Unity has been in heavy production at thousands of Databricks customers for years. The hard cases - cross-region replication, fine-grained access control, audit logging at scale - have been worked out.
- **Scope.** Unity catalogs tables, volumes, models, functions, and now [AI assets](/data-engineering/unity-catalog-in-practice-2026/). The scope expansion since the open-source release has been significant.
- **Federation.** Unity can federate to external catalogs (Hive Metastore, AWS Glue, others) which makes adoption incremental rather than cutover.
- **Native Iceberg REST support.** External engines can read Unity-managed tables through the Iceberg REST API.

**Weaknesses:**

- **Databricks gravity.** The full feature set is best on Databricks. The open-source version is real and useful but trails the managed version.
- **Operational complexity.** Running Unity yourself is non-trivial. Most Unity adoption is via Databricks, and that is the path Databricks would prefer.

### Polaris

[Polaris](https://polaris.apache.org/) was open-sourced by Snowflake in 2024 and donated to the Apache Software Foundation. Polaris is the cleanest open implementation of the Iceberg REST catalog spec.

**Strengths:**

- **Open by design.** Polaris was built to be a reference REST catalog implementation rather than to plug into a specific vendor's ecosystem first.
- **Engine neutrality.** Polaris works equally well with Snowflake, Trino, Spark, Flink, and any other Iceberg-aware engine.
- **Apache governance.** The donation to ASF was a genuine signal that Snowflake wants Polaris to be a community-owned project rather than a strategic asset of one vendor.

**Weaknesses:**

- **Less mature governance scope.** Compared to Unity, Polaris's governance, lineage, and audit story is thinner. It is a strong table catalog. It is a smaller governance plane.
- **Still establishing momentum.** The community is forming. The vendor support outside Snowflake is real but earlier in its trajectory than Unity's.

### Gravitino

[Apache Gravitino](https://gravitino.apache.org/) was started by Datastrato and entered the Apache Incubator in 2024. Gravitino is the most ambitious of the four in scope - it positions itself as a **metadata lake** rather than just a table catalog.

**Strengths:**

- **Cross-asset cataloging.** Gravitino aims to catalog tables, files, ML models, message queues, and more, with a unified metadata layer above all of them.
- **Federation-first design.** Gravitino is built to federate across multiple underlying systems rather than be the sole source of truth.
- **Multi-cloud, multi-engine.** No deep coupling to any single vendor's platform.

**Weaknesses:**

- **Younger project.** Less production traffic than Unity. Less industry alignment than Polaris.
- **Scope ambition is also a risk.** Trying to catalog everything is harder than trying to catalog tables well. The execution has to follow the vision.

### Project Nessie

[Project Nessie](https://projectnessie.org/) is the oddest and arguably most interesting of the four. Nessie treats data the way Git treats code - branches, commits, tags, merges. It is backed by Dremio and has a small but committed community.

**Strengths:**

- **Branching.** Real, working data branching. You can spin up an isolated branch, do your work, and merge it back. This is genuinely useful for testing pipelines, ML experimentation, and disaster recovery.
- **Multi-table transactions.** Nessie can commit changes across multiple tables atomically, which most catalogs cannot.
- **Strong opinions, well executed.** Nessie does not try to be everything. It does branching very well.

**Weaknesses:**

- **Smaller ecosystem.** Engine support is real but narrower than Unity or Polaris.
- **Not a governance plane.** Nessie focuses on versioning and branching. Audit, lineage, and access control are weaker.

## Where The Battle Lines Actually Run

Once you stop asking "which catalog is best" and start asking "which catalog wins which job," the picture clarifies.

**For Databricks-centric organisations:** Unity is the obvious answer. The integration is deepest, the operational story is most mature, and the cost of fighting it is high.

**For Snowflake-centric organisations:** Polaris is the natural fit. Snowflake's commitment is real and Polaris is engineered to be a credible open catalog beneath Snowflake's commercial offering.

**For multi-engine, multi-cloud organisations that do not want to bet on a vendor:** Polaris or Gravitino. Polaris if you mostly care about tables. Gravitino if you have meaningful non-table assets to catalog as well.

**For data engineering teams that need branching and isolation:** Nessie, possibly alongside one of the others as the primary governance plane.

**For organisations evaluating from scratch:** the protocol matters more than the implementation. Pick a catalog that implements the **Iceberg REST spec** correctly and completely. That keeps the door open to switching later.

## What Is Actually Standardising

The most underappreciated story of 2025-2026 is that all four catalogs are converging on the **Iceberg REST catalog protocol** as their wire format. That is the equivalent of the format wars settling on Iceberg one layer down.

What this means in practice:

- An engine that knows how to talk to one Iceberg REST catalog can talk to any of them.
- Customers can switch catalogs without rewriting their query layer.
- Catalog vendors compete on governance, performance, scale, and developer experience rather than on protocol differences.

This is healthy. It is also strategically uncomfortable for vendors who would prefer a deeper moat. Expect the protocol to keep being extended in directions that favour each implementation - more permissive in some places, more strict in others - while the core stays interoperable.

## What Catalogs Need To Solve Next

Three problems are still genuinely unsolved across all four projects.

**Cross-catalog federation.** Most organisations have multiple catalogs in production - Glue here, Unity there, Hive Metastore in a corner that nobody wants to touch. A meta-catalog that unifies them is what every large data platform team is building manually right now. Whichever catalog ships this cleanly first will pull share quickly.

**Governance for AI and ML assets.** Tables are the easy case. Models, prompts, embeddings, agent state - these are now real production assets and most catalogs are not handling them gracefully. Unity is furthest along here. The others need to catch up.

**Audit and lineage at scale.** Every catalog claims lineage. Few catalogs deliver it cleanly across pipelines that span multiple engines. This is hard, the customers want it, and nobody has nailed it yet.

## The Honest Verdict

The catalog layer fight in 2026 is more interesting than the format fight ever was, because the catalog layer touches more of the things that actually matter to enterprises - governance, access, audit, lineage, and the integration of data with AI workflows.

The realistic 2026-2027 outcome looks like this: **multiple catalog implementations, all speaking the Iceberg REST protocol, with federation between them, and most organisations running more than one**. Unity will dominate Databricks shops. Polaris will dominate Snowflake shops. Gravitino and Nessie will carve out specific roles. Federation will be table stakes.

If you are choosing today, the safest move is to optimise for **protocol compliance and federation** rather than for picking a single winner. You probably will not pick a single winner. You will pick a primary catalog and learn to live with two or three.

The format wars taught us that standards win when neutrality is valued. The catalog wars are going to teach us the same lesson, just at a higher layer of the stack.

## Related Reading

- [Iceberg vs Delta vs Hudi in 2026 - The Format Wars Are Over](/data-engineering/iceberg-vs-delta-vs-hudi-2026/)
- [Unity Catalog in Practice](/data-engineering/unity-catalog-in-practice-2026/)
- [Apache Iceberg in 2026](/data-engineering/apache-iceberg-2026/)
- [The Modern Lakehouse Stack](/data-engineering/modern-lakehouse-stack/)
- [Databricks vs Snowflake 2026](/data-engineering/databricks-vs-snowflake-2026/)
