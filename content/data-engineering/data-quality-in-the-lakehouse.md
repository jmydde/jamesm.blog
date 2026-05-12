---
title: "Data Quality in the Lakehouse: Tools, Patterns, and What Actually Works"
date: 2026-05-14T17:00:00+01:00
draft: true
tags: ["data-engineering", "data-quality", "lakehouse", "great-expectations", "soda", "monte-carlo", "2026"]
description: "A grounded look at how data quality actually works in 2026 lakehouse deployments - the tools (Great Expectations, Soda, Anomalo, Monte Carlo), the patterns that ship to production, the failure modes that the marketing hides, and what teams have learned about doing this for real."
cover:
  image: /assets/images/data-engineering/data-quality-in-the-lakehouse.jpg
  alt: Data Quality in the Lakehouse - Tools, Patterns, and What Actually Works Banner
---

Data quality has been the most-promised and least-delivered area of data engineering for at least a decade. The talks were ambitious, the frameworks were optimistic, the actual production deployments were narrow and partial. By 2026 the picture has improved enough to be worth taking seriously. The lakehouse architecture has stabilised. The tooling has matured. The patterns that work in production are documented. The teams that have shipped real data quality programmes have lessons worth sharing. The honest summary is that the field has moved from "we know we should be doing this" to "we know what actually works," and the gap between the two is what made the last decade frustrating.

## TL;DR

- Data quality in 2026 lakehouse deployments is dominated by four tooling categories: **assertion frameworks** (Great Expectations, Soda, dbt tests), **observability platforms** (Monte Carlo, Anomalo, Bigeye, Acceldata), **catalog-integrated quality** (Unity Catalog data quality, Polaris quality features), and **streaming validation** (in-pipeline checks during ingestion).
- The pattern that works in production is **layered**: cheap explicit assertions at the boundary, statistical anomaly detection on top, and observability tooling to catch the failures the first two layers miss.
- The biggest gap in most data quality programmes is not the tooling but the **incident response process**. Catching the issue is easy. Acting on it - paging the right person, triaging the impact, communicating with downstream consumers - is where most programmes struggle.
- The single most useful piece of data quality work in 2026 is **freshness monitoring**. Most "data quality" incidents that consumers actually notice are freshness incidents, and the freshness checks are the easiest to specify and most actionable to enforce.
- The lakehouse architecture has made data quality both easier and harder. Easier because the centralised catalog and unified table format provide a clean place to attach quality metadata. Harder because the volume of tables in a lakehouse is typically much larger than in a classical warehouse, and the data quality work has to scale accordingly.
- The realistic outcome is **detection of 70-80% of quality issues at the boundary, with the remaining 20-30% caught by observability and downstream consumer feedback**. That is much better than the historical baseline and it is the right thing to optimise for.

## The categories of data quality work

The first thing to understand about data quality in 2026 is that it is several distinct categories of work, and conflating them produces the kind of overambitious programmes that have failed in the past.

**Schema quality.** Does the data have the right columns, types, and structure? This is the easiest category to specify and enforce. The standard tooling (dbt tests, Great Expectations, Soda) handles it well. The failure rate is low and the incidents that do occur are usually obvious.

**Freshness quality.** Is the data up to date? This is the category that consumers actually notice most often. "The dashboard is stale" is a more common complaint than "the dashboard is wrong." Freshness checks are easy to specify (most-recent timestamp within X minutes/hours) and easy to enforce, and they are the single highest-ROI data quality investment for most teams.

**Volume quality.** Did the right amount of data arrive? Volume anomalies catch a class of failures that schema and freshness miss - the data is structurally correct and recent but the row count is wrong. The standard pattern is comparison to historical volumes with bounds.

**Distribution quality.** Are the statistical properties of the data what they should be? Column value distributions, null rates, range checks. This is harder to specify and harder to maintain because legitimate changes in the data can trigger false positives. The successful deployments keep distribution checks narrow and high-signal.

**Referential quality.** Do the relationships between tables hold? Foreign keys, uniqueness, expected cardinality. This is the hardest category to enforce at lakehouse scale because the checks are expensive and the failures cross table boundaries.

**Semantic quality.** Does the data make business sense? Business rules expressed as SQL or DSL assertions. This is the most ambitious category and the one that most often fails to deliver in production. The cost of maintaining semantic checks tends to grow faster than the value.

The pattern that works is to invest heavily in the first three categories, lightly in the next two, and minimally in the last one. The teams that have tried to ship comprehensive semantic validation have generally failed - the maintenance cost is too high, the false positive rate is too high, and the genuine semantic issues that matter are usually caught by downstream consumers anyway.

## The tooling landscape in 2026

The data quality tooling has consolidated around several credible options, each fitting a different deployment pattern.

**[Great Expectations](https://greatexpectations.io/)** is the heaviest of the assertion frameworks, with the largest library of pre-built validations. The framework can express almost any data quality check but the operational overhead is significant. Great Expectations works well for teams with dedicated data engineering capacity and complex validation requirements. It is overkill for teams with simpler needs.

**[Soda Core](https://www.soda.io/)** is the lighter-weight assertion framework, with a YAML-based syntax that is easier to author and maintain than Great Expectations. Soda is the most common choice for teams shipping data contracts in 2026, and the commercial Soda Cloud product adds observability features on top of the open-source core.

**[dbt tests](https://docs.getdbt.com/docs/build/data-tests)** are the most-deployed data quality mechanism by sheer adoption, simply because dbt is the most-deployed transformation framework. The test capability is more limited than Great Expectations or Soda but the integration with the transformation work is unmatched. Most teams shipping data quality in 2026 use dbt tests as the primary mechanism, with one of the dedicated tools added on top for specific use cases.

**[Monte Carlo](https://www.montecarlodata.com/)** is the leading observability platform, focused on catching quality issues through anomaly detection rather than explicit assertions. The advantage is that Monte Carlo catches issues you have not thought to check for. The disadvantage is that the cost is significant (typically tens of thousands per year for serious deployments) and the false positive rate requires ongoing tuning.

**[Anomalo](https://www.anomalo.com/)** is the most aggressive of the ML-driven anomaly detection platforms, applying statistical models to detect distributional shifts in data without explicit rule definition. The framework is particularly useful for teams with too many tables to maintain explicit assertions on each one, but the same false-positive management challenges apply.

**[Bigeye](https://www.bigeye.com/)** and **[Acceldata](https://www.acceldata.io/)** round out the observability category with similar capabilities and different commercial positioning.

**Catalog-integrated quality.** [Unity Catalog](/data-engineering/unity-catalog-in-practice/) and the [other major catalogs](/data-engineering/the-catalog-layer-is-the-new-battleground/) have started shipping data quality features as first-class catalog metadata. The integration is architecturally interesting because it moves quality enforcement closer to the storage layer, but the feature maturity varies and most production deployments still rely on the dedicated tools alongside the catalog features.

**Streaming validation.** For teams running streaming ingestion pipelines, in-pipeline validation (typically with Soda or custom Flink jobs) catches quality issues before bad data enters the lakehouse. The pattern is increasingly common as streaming becomes a default ingestion path.

## The layered pattern that works

The deployment pattern that succeeds in production is layered rather than single-tool. The typical shape:

**Layer 1: Boundary assertions.** Cheap, fast, explicit checks at the points where data enters the lakehouse or moves between layers. The content is schema validation, freshness SLAs, and basic volume checks. The tooling is typically dbt tests or Soda. The enforcement is hard - failures pause the pipeline. This layer catches most of the schema-and-freshness incidents.

**Layer 2: Statistical anomaly detection.** Background monitoring of tables for distributional anomalies that the explicit checks would miss. The tooling is Monte Carlo, Anomalo, or equivalent. The enforcement is soft - failures generate alerts rather than pausing pipelines. This layer catches issues that the explicit checks have not been written for.

**Layer 3: Consumer feedback loops.** Mechanisms for downstream consumers to report quality issues that the upstream checks missed, with a feedback path to add new boundary assertions or anomaly detection rules. The tooling here is usually Slack channels, Linear tickets, or whatever the team's existing communication infrastructure is. This layer catches the long tail of issues that the systematic checks cannot anticipate.

**Layer 4: Catalog-level metadata.** Quality scores, freshness indicators, and incident history surfaced in the catalog so that consumers can make informed decisions about what data to trust. The tooling here is the catalog itself (Unity Catalog data quality features, third-party catalogs like Atlan or Castor). This layer changes the consumer's experience of the data rather than catching issues per se.

The layered pattern works because no single layer catches everything. The boundary assertions are cheap but they only check what they have been told to check. The anomaly detection catches what the assertions miss but it has a false-positive cost. The consumer feedback catches what neither systematic layer catches but it is slow. The catalog metadata makes the failures legible without catching them.

## What incident response actually looks like

The most-missed part of data quality programmes in 2026 is the incident response side. The detection tooling has matured. The response process has not, and the gap is where most programmes deliver less value than they should.

A data quality incident in production typically follows this shape:

1. The detection tooling fires an alert - a schema check failed, an anomaly was detected, a downstream consumer reported a problem.
2. Somebody triages the alert - is this a real incident or a false positive.
3. If real, somebody investigates - what is the root cause, what is the blast radius.
4. Somebody decides on remediation - fix the source, work around the issue, rollback.
5. Somebody communicates - to the downstream consumers, to the source team, to management.
6. Somebody updates the detection - add a new check, tune the anomaly threshold, document the incident.

The teams that have shipped successful data quality programmes have invested in each of these steps explicitly. There is a clear on-call rotation. There is a runbook. There is a Slack channel for incidents. There is a postmortem template. The communication paths are established before the incident happens.

The teams that have failed have invested in detection without investing in response. The alerts fire. Nobody owns them. The Slack channel is full of unactioned messages. The downstream consumers find out about the issues from their own dashboards looking wrong. The detection tooling becomes a source of noise rather than a source of signal.

This is not a tooling problem. It is an organisational problem. The data quality vendors have started shipping incident-management features (Monte Carlo's case-tracking, Soda's collaboration features) but the tooling cannot fix the organisational gap. Teams that are serious about data quality invest in the response process, ideally before the detection programme is deployed.

## The lakehouse-specific challenges

The lakehouse architecture introduces some specific data quality challenges that are worth being explicit about.

**Table proliferation.** A typical lakehouse has thousands of tables - bronze, silver, gold layers, multiple variants per business entity, derived tables for specific use cases. The volume is much larger than in a classical warehouse and the data quality work has to scale accordingly. The pattern that works is to focus on the gold-layer tables that downstream consumers actually use, with lighter checks on the silver layer and minimal checks on bronze.

**Distributed ownership.** In a properly federated lakehouse, different teams own different tables, and the quality work has to span organisational boundaries. The contract-based approaches discussed in the [data contracts](/data-engineering/data-contracts-in-production/) post are the standard solution but they require organisational coordination that is often the binding constraint.

**Schema evolution.** Lakehouse table formats (Iceberg, Delta) support schema evolution natively, which is mostly good but it creates quality challenges. Columns get added, types get changed, partitions get reorganised - and the downstream consumers need to know. The catalog-level metadata is the right place to track this and the integration with the data quality tooling is improving but not yet complete.

**Multi-engine access.** Lakehouse tables are read by many engines - Spark, DuckDB, Snowflake, Trino, BigQuery - and the quality issues can manifest differently in different engines. The quality work has to be engine-aware, and the standard pattern is to run the quality checks in the same engine that the dominant consumers use.

**Storage-level quality.** The new generation of lakehouse formats (DuckLake, the latest Iceberg revisions) are starting to integrate quality features at the table-format level - constraints, default values, automatic null-handling. The features are real but the maturity varies, and most production deployments still rely on the pipeline-layer tooling.

## Where data quality programmes fail

The failure modes for data quality programmes in 2026 are well-documented enough to be worth listing explicitly.

**Over-scoping.** Teams that try to ship data quality across an entire data estate before proving the model on a narrow scope generally fail. The successful pattern is to start with 5-20 high-impact tables, ship quality work on those, prove the model, and expand.

**Tool-first thinking.** Teams that pick a tool before defining what they are trying to detect end up with a tool that does not fit the problem. The pattern that works is to define the failure modes you care about first and then pick the tool that fits.

**Detection without response.** As discussed above, this is the single biggest source of failure. Detection without organised response produces noise rather than value.

**False-positive tolerance.** Anomaly detection systems generate false positives. Teams that do not have a process to triage and tune the alerts find the alerts becoming background noise within a few months. The successful deployments invest in alert tuning as ongoing work.

**Maintenance debt.** Data quality checks have to evolve as the data evolves. Teams that ship checks and then do not maintain them find the checks becoming progressively less reliable over time. The successful deployments treat quality checks as production code with the same maintenance discipline as any other production code.

**Cost surprise.** Anomaly detection platforms (Monte Carlo, Anomalo, etc.) can cost significant amounts at scale, and the cost grows with the number of tables monitored. Teams that adopt these platforms without budgeting for the long-term cost find themselves either narrowing the coverage or absorbing surprise costs.

## The controversial parts

Three claims in the data-quality conversation deserve more pushback than they typically get.

The first is the claim that AI-driven anomaly detection will solve the data quality problem. The empirical evidence is more mixed. ML-driven detection catches some issues that rule-based detection misses, but it also generates more false positives and requires more tuning. The combination of explicit rules and ML-driven anomaly detection works well together; either one alone is a partial solution.

The second is the claim that catalog-level quality integration will eliminate the need for dedicated quality tooling. The catalog integration is genuinely valuable but the dedicated tools still do more sophisticated work, particularly on the statistical and semantic sides. The catalog and the tools are complementary, not competitive.

The third is the claim that data quality is fundamentally a tooling problem. It is not. The technical work is real but the harder problem is organisational - who owns the data, who is accountable when quality breaks, who pays when the response is slow. Teams that approach data quality as a pure technical problem usually fail. Teams that approach it as a technical problem inside an organisational problem usually succeed.

## Where this is heading

The most likely shape of 2027-2028 is that data quality becomes a normal part of the lakehouse operations rather than a separate concern. The catalog-level integration will deepen. The tooling will continue to consolidate around a few dominant vendors in each category. The AI-driven detection will improve and the false-positive rates will come down. The incident response patterns will become more standardised and the on-call practices will look more like SRE.

The other prediction worth making is that quality scores and freshness indicators will become a first-class part of the consumer experience. The pattern of seeing a "verified" or "stale" badge next to a table in a catalog UI, or having a dashboard automatically flag a quality issue affecting its underlying data, is already starting to appear. The trajectory is toward making quality legible to consumers as part of how they interact with the data, rather than as a separate process.

For teams building data quality programmes today, the practical guidance is the boring version of the exciting story. Start with freshness monitoring. Add schema checks. Layer in anomaly detection once the basics are working. Invest in the response process as much as in the detection. Keep the scope narrow until the model is proven. Expect to detect 70-80% of issues at the boundary and accept that the remainder will be caught by observability and consumer feedback. The teams that follow this path generally succeed. The teams that try to ship comprehensive quality everywhere usually do not.

## Related Reading

- [Data Contracts: From Buzzword to Production Practice in 2026](/data-engineering/data-contracts-in-production/) - the contract-driven approach that is one part of the broader quality story.
- [AI-Native Pipelines - What Changes When Your Consumer Is an LLM, Not a Dashboard](/data-engineering/ai-native-pipelines/) - the consumer-side story where quality issues have different consequences.
- [The Modern Lakehouse Stack: What Actually Belongs in Production](/data-engineering/modern-lakehouse-stack/) - the broader stack context.
- [Unity Catalog in Practice: Lessons From the Field](/data-engineering/unity-catalog-in-practice/) - the catalog that increasingly carries quality metadata.
- [dbt vs SQLMesh: The Transformation Layer Showdown in 2026](/data-engineering/dbt-vs-sqlmesh-2026/) - the transformation-layer tools that ship the most-deployed quality enforcement.
