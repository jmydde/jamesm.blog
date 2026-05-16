---
title: "The SRE Skillset in 2026: What Actually Matters Now"
date: 2026-05-10T13:30:00+01:00
draft: true
tags: ["devops", "sre", "reliability", "observability", "agent"]
description: "Site Reliability Engineering has not disappeared in the AI era - it has changed shape. A look at which classic SRE skills still pay off in 2026, which have faded, and the new ones that have moved to the centre of the job."
cover:
  image: /assets/images/devops/sre-skillset-2026.jpg
  alt: The SRE Skillset in 2026 Banner
---

Site Reliability Engineering as a discipline turned fifteen in 2026. The role looks meaningfully different from what Google's original SRE team set out to define. Some of the original skills have aged into universal table stakes; others have faded as the underlying systems changed; new ones have moved to the centre of the work.

Here is what actually matters for an SRE in 2026, based on what the role looks like in production now rather than what it looked like in the 2017 book.

## What still matters - more than ever

**Reading systems under pressure.** The job has not stopped being about understanding why a complex system is doing the wrong thing at 3am. If anything, the systems are more complex - more managed services, more third-party dependencies, more distributed failure modes - so the ability to look at a flood of signals and find the actual cause is more valuable, not less.

**Capacity planning that does not assume linear traffic.** AI-driven workloads have bursty, unpredictable shapes. Knowing how to reason about p99 latency under traffic spikes and how to instrument for it is now critical for any service that touches an AI feature.

**Postmortems as a real discipline.** The Google SRE habit of blameless postmortems with measurable action items has become standard practice across the industry. SREs who can run them well - structured, honest, producing real change - are still differentiated.

## What has faded

**Hand-rolled monitoring stacks.** Building your own Prometheus-plus-Grafana stack from scratch is something fewer SREs spend time on now. The hosted observability vendors (Datadog, Honeycomb, Grafana Cloud, New Relic) have absorbed most of that work. The SRE skill is now in configuring and querying them well, not in operating the underlying time-series databases.

**Manual oncall toil.** The expectation that an SRE spends a meaningful share of their week fighting recurring fires has faded. If an incident type recurs, the expectation is that it gets automated away, not staffed against. Teams that still tolerate high oncall toil look outdated rather than busy.

**Bespoke deployment tooling.** Most SRE-built deployment systems have been retired in favour of standardised platforms. The platform-engineering wave displaced the "I will write our deploy tool" instinct.

## What has moved to the centre

**Observability as a design discipline, not a monitoring concern.** The 2026 SRE thinks about instrumentation while the service is being designed, not bolted on afterwards. Distributed tracing, structured logging with shared correlation IDs, and SLO-driven dashboards are now part of the design phase. [eBPF](/devops/ebpf-revolution/) has made low-overhead deep instrumentation feasible in ways it was not five years ago.

**Reasoning about AI-system reliability.** A growing share of production traffic flows through AI services - either ones the team operates or third-party APIs the system depends on. The reliability characteristics are different: latency that varies by an order of magnitude based on input, accuracy that degrades on edge cases, failure modes that are silent rather than loud. SREs who can build observability around these systems are increasingly the bottleneck.

**Cost as a first-class reliability concern.** Cloud and AI-API costs have become a real operational concern at most companies. Cost-driven incidents - a runaway batch job, a misconfigured retry loop hammering a paid API - are now common enough that cost observability sits next to latency and error-rate observability in the SRE dashboard. [The data centre power story](/ai/ai-energy-crisis-data-center-power/) feeds into this directly.

**Platform-as-product thinking.** SRE teams that own internal platforms increasingly treat the platform like a product, with users (other engineering teams), an interface, and a feedback loop. This is closer to product management than to classic SRE, and the teams that have made the shift produce noticeably better internal tools.

## The skill that surprised people

The skill that has appreciated most quickly in 2026 is something most original SRE job descriptions would not have mentioned: writing for agents. SREs increasingly produce runbooks, incident-response procedures, and operational documentation that an AI agent can execute against - not just a human at 3am. The structure, specificity, and verifiability of those documents matters in a way it did not when only humans read them.

The teams furthest along on this have started treating "the runbook" as a first-class engineering artefact, version-controlled, tested, and continuously refined based on the outcomes of incidents an agent helped resolve.

## What the role looks like in practice

The 2026 SRE spends less time on tooling, more time on systems thinking. Less time on operational toil, more time on cost and capacity. Less time on log-grepping, more time on instrumentation design. Less time on "the deploy is broken," more time on "the third-party AI API our system depends on is degraded - how do we keep working."

The discipline has not been displaced by AI. It has absorbed AI as a new category of dependency to be reasoned about, and it has shifted toward the higher-leverage work as the lower-leverage work has been automated. The SREs who have kept up are doing more interesting work than they were three years ago. The ones who have not are watching the toil that defined the job disappear and wondering what comes next.

## Related Reading

- [Platform Engineering in 2026](/devops/platform-engineering-2026/)
- [eBPF Revolution](/devops/ebpf-revolution/)
- [Kubernetes 2026: The Complexity Tax](/devops/kubernetes-2026-complexity-tax/)
- [Monitoring](/devops/monitoring/)
- [DevOps in the Age of AI Agents](/devops/devops-in-the-age-of-ai-agents/)
