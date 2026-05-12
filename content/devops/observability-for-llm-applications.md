---
title: "Observability for LLM Applications: What Actually Works in 2026"
date: 2026-05-12T22:00:00+01:00
draft: true
tags: ["devops", "observability", "llm", "tracing", "monitoring"]
description: "Watching an LLM-powered application in production is harder than watching a classic service - the failure modes are different and the signals are noisier. A practical look at the observability patterns that have stabilised in 2026 and which tools are doing the work."
cover:
  image: /assets/images/devops/observability-for-llm-applications.jpg
  alt: Observability for LLM Applications Banner
---

Watching a classic web service is a well-understood problem. Requests per second, error rates, p99 latency, resource utilisation - the signal-to-noise ratio is high, and the failure modes are mostly familiar. Watching an LLM-powered application is harder. The service can be "up" by every traditional measure and still be producing wrong answers. The latency can spike for reasons unrelated to load. The cost can grow without the traffic growing. The same input can produce different outputs from one minute to the next.

The observability discipline has had to catch up with these new failure modes, and the patterns that work in 2026 are different enough from classic application observability to be worth talking about.

## What is different about LLM apps

A few specific things that conventional observability tooling does not handle well:

**Non-determinism by default.** The same input produces different outputs. Classic comparison-based testing does not apply. The signal "this output looks wrong" requires evaluation, not just comparison.

**Quality is a real metric.** A service that returns 200 OK with a bad answer is failing in a way that traditional uptime monitoring cannot see. Quality has to be measured directly, often expensively.

**Cost is a first-class concern.** Per-request cost varies by an order of magnitude based on input. Total cost can spike without total traffic spiking. This needs its own observability discipline.

**Failure is silent more often than loud.** A model that starts producing slightly worse outputs - because of a prompt change, a context change, a model version update - does not throw exceptions. The degradation is invisible until someone notices the downstream effect.

**The dependency surface is unusual.** The application depends on third-party model APIs whose behaviour can shift without notice. Provider-side rate limits, latency variations, model deprecations, and quality changes are all sources of variability outside the team's control.

## The observability layers that emerged

The teams running LLM applications in production in 2026 are using a layered observability approach that has settled into a recognisable shape:

**Traces of the full LLM call.** Every call captures the full prompt, the full response, the model version, the latency, the token counts, the cost, and the parent task context. This is more data per call than a traditional service captures, and the storage cost is real - but the diagnostic value when something goes wrong is impossible to replicate without it.

**Structured task tracking above individual calls.** A user task often spans many model calls. The trace structure needs to reflect this - a parent task with child spans for each model call, tool call, retrieval, and tool result. OpenTelemetry-style distributed tracing extended for LLM-specific span types has become the standard.

**Evaluation as observability.** Continuous evaluation of model outputs against quality benchmarks, ideally on a sample of live production traffic. This catches quality regressions that no traditional monitoring would notice.

**Drift detection on prompt and output distributions.** Detecting when the inputs to the model are changing in distribution, or when the outputs are. Either can indicate a problem.

**Cost observability per call site and per user.** Knowing where the spend is going at fine granularity. The [FinOps angle](/devops/finops-for-ai-era/) overlaps significantly with observability here.

## The tools that actually work

The 2026 toolchain for LLM observability has consolidated around a few categories:

**LLM-specific observability platforms** - Langfuse, Helicone, Arize Phoenix, Braintrust, Weights & Biases Weave. These focus on prompt-level tracing, evaluation, and prompt versioning. The leaders share similar feature sets; the differentiation is integration depth and pricing.

**Extensions to general observability platforms.** Datadog, Honeycomb, Grafana, and the other generalists have all shipped LLM-specific features. The advantage is integration with the rest of the observability stack; the disadvantage is depth.

**The model providers themselves.** Anthropic, OpenAI, and others all provide their own dashboards. These are useful but limited - they see only their own traffic, not the application context around it.

The realistic 2026 deployment is hybrid: a specialist LLM observability tool for the LLM-specific work, integrated with the existing observability stack for everything else. Trying to do LLM observability through the classic tools alone is workable but limits visibility into the LLM-specific failure modes.

## What to actually measure

The metrics that distinguish good LLM application observability from theatrical LLM application observability:

**Quality regression rate.** Per-feature, per-model-version. Catches the silent degradation that uptime monitoring misses.

**Cache hit rate.** Both prompt-level and application-level. Critical for cost control.

**Time-to-first-token and time-to-final-token.** Two separate latency metrics that matter to users in different ways.

**Token cost per task.** Not per call - per user-visible task. Agent tasks that take many calls to complete are visible only at this level.

**Failure modes by category.** Refusals, hallucinations, format violations, tool-call failures, timeout failures. The distribution of failure modes tells you what to fix.

**Drift in input distribution.** Are users asking different questions than they were last week? Are the prompts the application is generating to the model changing?

**Tool call success rate.** For agentic systems, the tool layer is often the silent failure point. Tracking tool call success and the reasons for failure is critical.

## What is harder than expected

A few specific things that are harder than the marketing for LLM observability tools suggests:

**Evaluation cost.** Continuously evaluating model output quality is expensive - often itself requiring LLM calls. The cost of observability can rival the cost of the application it observes if not managed carefully.

**Defining "quality" for open-ended outputs.** What does it mean for a chatbot's response to be "good"? The evaluation criteria are not obvious, and getting them wrong produces metrics that look meaningful but are not.

**Privacy in trace storage.** Full-prompt logging is the most useful diagnostic data and the most sensitive privacy data. The trade-offs are real and not fully resolved.

**Cross-model comparability.** A trace from a Claude call and a trace from a GPT-4 call have different structures, different cost models, different latency profiles. Comparing across providers is not as easy as comparing across regions of a single cloud.

The 2026 picture is that LLM observability is real, the tooling is improving, and the practice is meaningfully ahead of where it was a year ago. It is not a solved problem - it has the kind of trade-offs and rough edges that any new operational discipline has. The teams that have invested in it are catching real production issues that the teams that have not are missing.

## Related Reading

- [The SRE Skillset in 2026](/devops/sre-skillset-2026/)
- [FinOps for the AI Era](/devops/finops-for-ai-era/)
- [DevOps in the Age of AI Agents](/devops/devops-in-the-age-of-ai-agents/)
- [eBPF Revolution](/devops/ebpf-revolution/)
- [AI Reliability Is Weird](/ai/ai-reliability-is-weird/)
