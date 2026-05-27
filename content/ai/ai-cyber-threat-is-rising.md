---
title: "Why the AI Cyber Threat Is Rising"
date: 2026-05-26T07:30:00+01:00
draft: false
tags: ["ai", "cybersecurity", "anthropic", "security", "agent"]
description: "Sky News technology correspondent Rowland Manthorpe lays out the evidence that AI models are getting dramatically better at offensive cyber tasks. A look at what the AISI and CAISI numbers actually say, why open-weight releases change the threat curve, and what defenders should do about it."
cover:
  image: /assets/images/ai/ai-cyber-threat-is-rising.png
  alt: Why the AI Cyber Threat Is Rising Banner
---

For most of the last few years, the "AI and cybersecurity" conversation has been a vibes argument. One side said the models would soon write novel exploits at scale. The other side said the models were still tripping over basic shell commands and could not be trusted to hack anything more dangerous than a CTF box. The honest answer was that nobody had hard numbers, so the debate stayed stuck on intuition.

That has changed. Over the last several months the UK [AI Security Institute](https://www.aisi.gov.uk/) and the US [Center for AI Standards and Innovation](https://www.nist.gov/aisi) have published evaluation results that move this from anecdote to measurement. Sky News technology correspondent Rowland Manthorpe walks through the picture in a short segment that is worth watching end to end.

## Video

### Why the AI cyber threat is rising

{{< youtube rlRlhEQDvVA >}}

*Rowland Manthorpe summarises the AISI and CAISI evaluation data on frontier model offensive cyber capability, and explains why the open-weight side of the market matters more than people think.*

## TL;DR

- Frontier model performance on offensive cyber benchmarks has moved sharply upward in the last twelve months, and the slope is not flattening
- Government-run evaluations from AISI and CAISI are now the most credible source of data on this, displacing the vendor self-reports that used to dominate
- The shift from "AI as advisor" to "AI as operator" is the substantive change - agentic models can chain steps, not just describe them
- Open-weight releases, many of them from Chinese labs, are the asymmetric risk: capability that lands in a closed lab can be safety-tuned, capability that lands as weights cannot
- The defender's homework is unglamorous - patch faster, reduce the vulnerable surface, and assume the next CVE will be weaponised in hours rather than weeks

## What actually changed

The substantive change is not that models got smarter in some abstract sense. It is that they got noticeably better at the specific shape of work that an offensive operator does. That work is mostly not "write a zero-day from scratch". It is reading source, recognising vulnerable patterns, chaining several brittle tools together, recovering when a step fails, and grinding through reconnaissance without losing the thread.

Twelve months ago, frontier models were intermittently useful for this. They could explain a vulnerability class and sketch an exploit, but a human had to drive every step. In the last twelve months, the agentic loop got tight enough that a model can sustain an operation across many tool calls without falling apart. That is the change. It is less impressive than "AI invented a new attack" and more dangerous, because it scales.

Anthropic's own [post on disrupting an AI-orchestrated espionage campaign](https://www.anthropic.com/news/disrupting-AI-espionage) is the clearest concrete example. Their assessment was that the threat actor used the model to perform 80-90% of the campaign, with human intervention required only sporadically. The interesting number is not 80%. It is the ratio of operator hours to compromised targets. That ratio dropped by an order of magnitude.

## Why government evaluations matter now

For a while the only public benchmark numbers on offensive capability came from the labs themselves. That was always going to be a problem - the same organisation cannot both ship the product and be the trusted referee on whether it is dangerous. The UK AISI and the US CAISI exist specifically to fill that gap, and over the last year they have built up the methodology and the testing infrastructure to do it credibly.

What you get from their evaluations is not a single headline number but a curve. Capability on cyber range exercises, on capture-the-flag style problems, on vulnerability discovery in real codebases - all measured against fixed eval sets, run against successive model releases. The curve is what tells you whether the next twelve months looks like the last twelve.

The curve is currently steep. Nothing in the public results suggests it is about to bend back down.

## The open-weight asymmetry

This is the part of Manthorpe's segment that does not get enough airtime. If the only frontier offensive-capable models lived behind APIs run by labs that do refusal training and monitor abuse, the threat surface would still grow, but the labs would retain control of the failure mode. They can revoke keys, throttle suspicious workloads, and patch the model.

Open-weight releases collapse that control surface entirely. Once weights are public, every safety property of the released artefact is fixed at release time. The community will strip refusals. The community will fine-tune for whatever task the base model resists. That is not a hypothesis - it is what has happened to every previous open-weight release once it crossed a capability threshold worth the effort.

The interesting question is not whether this will happen with future open-weight cyber-capable models. It is who ships first. Chinese labs have been the most aggressive open-weight publishers for the last two years, and the gap between their releases and the closed frontier has narrowed faster than most analysts expected. The implication is that the offensive-capable open-weight model arrives sooner than the policy machinery is ready for.

## What defenders should actually do

Most of the policy commentary on this lands on "regulate the frontier labs". That is a reasonable thing to argue about, but it is not the work defenders can do this quarter. The work this quarter is:

**Shrink the patch window.** The threat model has shifted from "skilled human operator with weeks of dwell time" to "agentic model with hours of dwell time once a CVE drops". Patch-Tuesday-and-hope is no longer adequate for internet-facing surface.

**Reduce the vulnerable surface.** Every internet-exposed service is now a potential first hop in an automated campaign. The question to ask of every box is not "is this hardened" but "does this need to be reachable at all".

**Invest in detection that catches agents.** Agentic operations produce a recognisable shape of traffic - methodical, fast, willing to abandon a thread and try another. That shape is detectable if you are looking for it. Few SOCs are currently tuned to look for it.

**Use the same tools.** This is the point Anthropic and others have been making consistently, and it is correct. The same agentic capabilities that scale attacks also scale defence: triage, log review, vulnerability scanning at the codebase level. Defenders who do not adopt the toolchain are choosing to fight asymmetrically.

## The honest summary

The threat curve is going up because the capability curve is going up, and the two are now tightly coupled in a way they were not eighteen months ago. The evaluation infrastructure to measure this exists and is improving. The open-weight side of the market is the wildcard that determines whether the next twelve months looks merely difficult or genuinely chaotic.

None of this is reason to panic. Some of it is reason to bring forward work that was already on the roadmap.

## Related Reading

- [The Forbidden Frontier: Claude Mythos and the Dawn of Restricted AI Power](/ai/claude-mythos-restricted/)
- [AI Safety: First Principles](/ai/ai-safety-first-principles/)
- [The State of Open-Weight Models in 2026](/ai/state-of-open-weight-models-2026/)
- [Threat Modeling for Engineers](/security/threat-modeling-for-engineers/)
- [AI Agents That Actually Work: Patterns From Real Projects](/ai/ai-agents-that-actually-work/)
