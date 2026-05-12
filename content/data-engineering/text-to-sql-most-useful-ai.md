---
title: "Text-to-SQL Has Quietly Become the Most Useful AI in Data Engineering"
date: 2026-05-14T19:00:00+01:00
draft: true
tags: ["data-engineering", "ai", "sql", "text-to-sql", "llm", "2026"]
description: "A grounded look at how text-to-SQL has gone from research demo to genuinely useful AI in production data teams - what the current tools (Vanna, Snowflake Cortex Analyst, Databricks AI/BI Genie, custom solutions) actually do, where they work, and where the demos still oversell what's possible."
cover:
  image: /assets/images/data-engineering/text-to-sql-most-useful-ai.jpg
  alt: Text-to-SQL Has Quietly Become the Most Useful AI in Data Engineering Banner
---

Most of the AI marketing in data engineering in 2026 is about agents that build pipelines, copilots that write transformations, and platforms that "democratise data through natural language." Most of it overpromises. The one thing that has actually shipped, that actually works for actually-real users on actually-real data, that produces actual production value, is text-to-SQL. The unglamorous case of "ask a question, get a SQL query back, see the result" has quietly become the most useful piece of AI in the data engineering toolkit, and the gap between what works in production and what the rest of the AI-for-data category claims is wide enough to be worth being explicit about.

## TL;DR

- **Text-to-SQL** - the task of converting a natural-language question into a SQL query that runs against a database - has matured dramatically in 2025-2026 and is now genuinely useful for production analytical workloads.
- The current tools split into three categories: **embedded in BI/warehouse platforms** ([Snowflake Cortex Analyst](https://www.snowflake.com/en/data-cloud/cortex/), [Databricks AI/BI Genie](https://www.databricks.com/), Google BigQuery's natural language interfaces, ThoughtSpot Sage), **standalone frameworks** ([Vanna](https://vanna.ai/), [WrenAI](https://getwren.ai/), [DefogAI](https://defog.ai/)), and **custom internal builds** on top of frontier LLMs.
- The honest accuracy numbers are: **roughly 80-90% on well-modelled questions against well-documented schemas**, falling sharply on poorly-documented schemas, ambiguous questions, or queries requiring complex joins and aggregations.
- The pattern that works in production is **scoped to a curated semantic layer**, with the LLM translating between natural language and the semantic-layer concepts rather than directly to raw SQL. The semantic layer carries the business definitions, the join paths, and the metric definitions that the LLM cannot reliably infer from schema alone.
- The biggest commercial impact is on **the long tail of analyst work**: ad-hoc questions, exploratory analysis, and the simple-but-frequent queries that consumed a meaningful fraction of analyst time. Text-to-SQL has not replaced senior analytical engineers but it has materially reduced the workload of the rest of the analytics team.
- The most underrated point: text-to-SQL is the AI application that **actually produces a verifiable artefact**. The SQL query is something a human can read, modify, and trust. The artefact-producing nature is what makes the technology genuinely safe to deploy.

## Why text-to-SQL is the AI application that worked

The reason text-to-SQL has worked where other AI-for-data applications have struggled is worth being explicit about, because it tells us something about which AI applications are durable and which are not.

**The output is verifiable.** A text-to-SQL system produces a SQL query as its primary output. The query is something a human can read, understand, and assess. If the query is wrong, the human can see why it is wrong and decide whether to use the result. Compare this to AI systems that produce final answers directly - the user has no way to assess whether the answer is correct without doing the analysis themselves, which defeats the purpose.

**The task is well-defined.** "Convert this question into SQL" is a clear task with a clear success criterion. The query either runs and produces the right answer or it does not. The well-defined nature is the kind of thing AI is actually good at, and the contrast with the more open-ended applications (agents that "help with analysis," AI that "explores the data") is stark.

**The substrate is mature.** SQL is a 50-year-old language with enormous training data on the public internet, a stable specification, and a clear ground truth for correctness. The frontier LLMs have absorbed essentially all public SQL and have a strong baseline capability that did not have to be built from scratch.

**The deployment is incremental.** Text-to-SQL can be deployed as an assistant tool that an analyst reviews, not as an autonomous system that ships answers directly to users. The human-in-the-loop pattern is the safe deployment model and it is the one that has driven the actual adoption.

The combination - verifiable output, well-defined task, mature substrate, incremental deployment - is rare in the broader AI-for-data landscape, and it is the reason text-to-SQL has shipped while flashier applications have not.

## What the current tools actually do

The 2026 text-to-SQL landscape has three distinct product categories. Each fits a different deployment pattern.

### Embedded in BI/warehouse platforms

**[Snowflake Cortex Analyst](https://www.snowflake.com/en/data-cloud/cortex/)** is the most mature of the warehouse-embedded options. The system uses a semantic model that the customer defines (a YAML specification of tables, columns, joins, and business definitions) and translates natural-language questions into SQL queries that run against the semantic model rather than against raw tables. The accuracy on well-modelled questions is reported in the 90%+ range and the production deployments at scale are real.

**[Databricks AI/BI Genie](https://www.databricks.com/)** is the Databricks equivalent, similarly built on a semantic-model substrate (Unity Catalog metric definitions) and similarly producing high-quality SQL on well-modelled domains. The integration with the broader Databricks platform is the differentiator.

**Google BigQuery natural language interfaces** - the Gemini-driven SQL generation inside the BigQuery console, plus the Looker integration - cover the equivalent ground for Google Cloud customers. The quality is competitive with the other two, with the integration angles being the primary differentiator.

**ThoughtSpot Sage** is the most established of the BI-side products, with a longer track record of using natural language interfaces in business analytics. The product has been around longer than the LLM-driven competitors but the LLM integration has significantly improved its capability since 2023.

### Standalone frameworks

**[Vanna](https://vanna.ai/)** is the most popular open-source text-to-SQL framework. The system uses a combination of schema understanding, example queries, and documentation to produce SQL for arbitrary natural-language questions. Vanna can be deployed against any database with a JDBC connector and the open-source core is free. The commercial offering adds collaboration and management features.

**[WrenAI](https://getwren.ai/)** is the more recently emerged open-source option, with a semantic-model approach similar to the warehouse-embedded products. The framework defines an MDL (Model Definition Language) for business concepts and translates questions to MDL operations rather than directly to SQL.

**[DefogAI](https://defog.ai/)** is the framework with the most specific focus on fine-tuning. Defog ships fine-tuned models that have been trained on SQL generation specifically, which performs well on certain workloads but requires more investment in model deployment than the others.

### Custom internal builds

For teams with specific requirements that the off-the-shelf products do not meet, building on top of frontier LLMs (Claude, GPT, Gemini) is increasingly viable. The pattern involves prompting the model with the relevant schema, a sample of example queries, the business context, and the user's question, and getting back a SQL query.

The custom-build approach has real costs - prompt engineering, evaluation infrastructure, ongoing maintenance - but it allows tight integration with internal systems, control over the data flow, and customisation that the off-the-shelf products do not allow. The teams that have built custom solutions are typically large enterprises with significant data infrastructure investment.

## What "working" actually means

The published accuracy numbers for text-to-SQL systems should be read with significant caution. The benchmarks (Spider, BIRD, the various proprietary internal benchmarks) measure performance on specific test sets that may or may not reflect your workload.

The honest version of "does this work for production" has three components:

**Schema and documentation quality.** Text-to-SQL accuracy is dominated by schema and documentation quality, not by model quality. A well-documented schema with clear table names, descriptive column names, foreign-key relationships defined, and business-level descriptions in place produces high-quality SQL from essentially any modern text-to-SQL system. A poorly-documented schema with cryptic column names, no relationship metadata, and no business context produces unreliable SQL from any system. The single most useful investment for improving text-to-SQL performance is improving the documentation, not improving the model.

**Question complexity.** Simple questions ("how many users signed up last week") work reliably across essentially all current systems. Complex questions involving multiple joins, nested aggregations, window functions, or specific business definitions work much less reliably. The published benchmarks tend to over-represent simple questions and under-represent the hard cases that actually matter in production.

**Semantic ambiguity.** Real business questions are often ambiguous in ways the systems struggle with. "Revenue" could mean GAAP revenue, net revenue, gross revenue, billings, or any of several other definitions. "Active users" has at least five common definitions in most B2B businesses. The systems that handle ambiguity well force the user to pick from a curated list of business concepts; the systems that try to infer from natural language alone fail in unpredictable ways.

The realistic accuracy range for text-to-SQL in production in 2026 is roughly **80-90% on well-modelled questions against well-documented schemas**. The number falls sharply outside those conditions. The gap between the marketing numbers and the production reality is real but it is narrower than it was a year ago, and the trajectory is favourable.

## The semantic-layer pattern that wins

The single most important architectural decision in deploying text-to-SQL is whether to operate against raw tables or against a curated semantic layer. The pattern that wins in 2026 production is the semantic layer.

A **semantic layer** is a layer of business-level definitions on top of the raw data warehouse. It defines what a "customer" is, what "revenue" means, which tables join to which on which keys, and which metrics are sanctioned for use. The semantic layer carries the institutional knowledge that the raw schema does not.

Text-to-SQL systems that translate natural language to semantic-layer concepts (rather than directly to raw SQL) have much higher accuracy because they are translating between two well-defined surfaces - the natural-language question and the curated semantic concept space - rather than from natural language to the much larger and noisier space of valid SQL against the raw schema.

The semantic-layer approach is what Snowflake Cortex Analyst, Databricks AI/BI Genie, WrenAI, and most of the production-grade frameworks use. The deployment pattern requires up-front investment in defining the semantic layer (this is the work that most teams skip and then wonder why their text-to-SQL deployment underperforms) but it pays back in accuracy and in long-term maintainability.

The other thing the semantic layer does is to make text-to-SQL output verifiable. If the LLM produces a query against the semantic layer, the query is using concepts that have been pre-vetted by the data team. The risk surface is much smaller than if the LLM is producing arbitrary SQL against raw tables.

## What teams are actually doing

The deployment patterns that are winning in 2026 cluster around a few specific shapes.

**The analyst's assistant.** The most common deployment is text-to-SQL as a tool that analysts use to draft initial queries, with the analyst reviewing and adjusting before running. The pattern preserves analyst judgement, reduces analyst workload, and produces verifiable results. The 80-90% accuracy threshold is acceptable because the analyst is reviewing the output.

**Self-service for business users.** A meaningful number of teams are deploying text-to-SQL as a direct self-service tool for business users (product managers, marketers, executives), with the queries scoped to a curated semantic layer. The pattern works when the semantic layer is well-defined and the user questions are within the curated scope. It fails badly when either condition is not met.

**Embedded in BI dashboards.** Several BI tools now embed text-to-SQL as a way to extend pre-built dashboards. The user asks a question, the tool generates a SQL query, the result is rendered as a chart, and the user can save the new view. The pattern is particularly valuable for the long tail of "I wish this dashboard had X" requests that previously required engineering work.

**Engineering productivity.** Data engineers are using text-to-SQL tools themselves for tasks like exploratory schema analysis, drafting initial transformations, and understanding unfamiliar databases. The use case is not customer-facing but it is a meaningful productivity gain for the engineering team itself.

**Migration and refactoring.** A specific use case worth highlighting is the use of text-to-SQL (and the related text-to-anything frameworks) for cross-dialect SQL translation. Teams migrating between warehouses (Snowflake to Databricks, on-prem to cloud, etc.) increasingly use AI to translate the existing SQL, with the dialect translation being a particularly well-defined task that AI handles well.

## Where text-to-SQL fails

The honest case for the limits of text-to-SQL is also worth being clear about.

**Poorly-documented schemas.** The system cannot infer what tables and columns are without good metadata. Teams that try to deploy text-to-SQL on schemas with cryptic names and minimal documentation get bad results. The fix is documentation, not better models.

**Complex multi-join queries.** Queries that require navigating multiple joins, particularly across non-obvious foreign-key relationships, are where the systems most often fail. The semantic-layer approach helps because the join paths are pre-defined, but complex queries remain hard.

**Time-series and window-function queries.** SQL window functions are a class of operation the systems handle inconsistently. Queries involving moving averages, period-over-period comparisons, or rank-within-partition operations often produce queries that look right but are subtly wrong.

**Business-definition ambiguity.** As discussed above, real business questions often have multiple valid interpretations. The systems that try to silently pick one interpretation often pick the wrong one. The systems that force the user to disambiguate are slower but more correct.

**Performance-sensitive queries.** Text-to-SQL systems optimise for query correctness, not for query performance. A correct but slow query is a real outcome, and on large tables it can be expensive. Production deployments typically need a performance review layer on top of the generated SQL.

## The controversial parts

Three claims in the text-to-SQL conversation deserve more pushback than they typically get.

The first is the claim that text-to-SQL will eliminate the need for data analysts. The empirical evidence is that text-to-SQL increases analyst productivity rather than replacing analysts. The hard parts of analytical work - asking the right question, interpreting the results, communicating the implications - are not the parts that text-to-SQL helps with. The boring parts - writing the routine queries - are. The net effect is to shift analyst time from typing to thinking, which is good but not revolutionary.

The second is the claim that text-to-SQL benchmarks reliably predict production performance. They do not. The benchmark queries are dominated by simple questions, the schemas are usually well-documented, and the workloads do not include the long tail of edge cases that production deployments hit. Real-world performance has to be measured on real-world workloads.

The third is the claim that direct-to-raw-SQL approaches are catching up with semantic-layer approaches. They are improving but the gap remains real. The semantic-layer approach is structurally easier for the LLM and produces more reliable output. The trajectory may eventually close the gap but as of 2026 the architectural choice still matters.

## Where this is heading

The most likely shape of 2027-2028 is that text-to-SQL becomes a normal part of the BI and analytics surface, with most major platforms shipping it as a standard feature. The accuracy will continue to improve and the deployment patterns will continue to mature. The semantic-layer approach will continue to win the production deployments. The standalone frameworks will continue to thrive in the long tail of use cases the major platforms do not cover.

The other prediction worth making is that text-to-SQL is the AI-for-data application that will most clearly demonstrate the broader pattern of "AI that produces verifiable artefacts." The success of text-to-SQL is going to inspire similar applications - text-to-dbt-model, text-to-pipeline-config, text-to-dashboard - that operate on the same principle of producing something a human can verify rather than producing final answers directly. The category is going to expand and the lessons from text-to-SQL will shape what comes next.

For teams considering text-to-SQL deployments today, the practical guidance is the boring version of the exciting story. Invest in your schema and documentation before you invest in tools. Define a semantic layer. Start with analyst-assistant deployments before moving to self-service. Measure accuracy on your own workload, not on published benchmarks. Accept that the technology is genuinely useful but not magical, and the limits are real. The teams that approach text-to-SQL with realistic expectations and the right architectural foundations are generally getting real value. The teams that expect autonomous data-analyst replacement are generally disappointed.

## Related Reading

- [AI-Native Pipelines - What Changes When Your Consumer Is an LLM, Not a Dashboard](/data-engineering/ai-native-pipelines/) - the broader AI-in-data context.
- [dbt vs SQLMesh: The Transformation Layer Showdown in 2026](/data-engineering/dbt-vs-sqlmesh-2026/) - the transformation layer that text-to-SQL increasingly integrates with.
- [The Catalog Layer Is the New Battleground - Unity, Polaris, Gravitino, Nessie](/data-engineering/the-catalog-layer-is-the-new-battleground/) - the metadata substrate that text-to-SQL accuracy depends on.
- [Data Contracts: From Buzzword to Production Practice in 2026](/data-engineering/data-contracts-in-production/) - the contracts that document the semantics text-to-SQL needs.
- [Databricks vs Snowflake in 2026: An Honest Comparison](/data-engineering/databricks-vs-snowflake-2026/) - the platform context for the warehouse-embedded text-to-SQL products.
