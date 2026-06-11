---
title: "What If Software Were Built Like Bridges?"
date: 2026-05-12T18:30:00+01:00
draft: true
tags: ["idea", "software", "engineering", "philosophy", "architecture"]
description: "A speculative essay on what the practice of building software would look like if it borrowed the conventions of civil engineering - signed designs, regulated practitioners, public investigations of failures - and what that would actually cost and gain."
cover:
  image: /assets/images/general/human-advancement-acceleration.jpg
  alt: What If Software Were Built Like Bridges Banner
---

A civil engineer who designs a bridge that collapses faces consequences that begin with the loss of their licence and can extend to criminal prosecution. The design they signed is a matter of public record. The failure, if it happens, will be investigated by a public body whose findings become precedent for the next bridge. The practice of building bridges has been shaped, over a couple of centuries, by the slow accumulation of regulation, insurance, professional certification, and public accountability into a discipline that produces structures most of which stand for a hundred years.

A software engineer who ships a system that fails - even one that fails catastrophically and harms many people - faces almost none of this. The design is rarely public. The investigation, if there is one, is internal. The engineer's licence does not exist because there is no licence to revoke. The next system built by the same team will likely repeat the same mistakes because there is no body collecting the lessons.

This essay is a speculation: what would happen if software were built more like bridges, and what would the costs and benefits actually be?

## The bridge model

A working civil-engineering practice has, at minimum, the following components:

- **Licensed practitioners.** Engineers who sign off on designs are personally and legally accountable for them.
- **Standards bodies.** Independent organisations set technical standards for materials, design methods, and acceptable failure modes.
- **Public records.** Designs of significant structures are filed with public authorities. The information needed to assess a bridge's safety is, in principle, available to anyone who cares.
- **Independent inspection.** Government inspectors check the construction against the design, and the design against the standards.
- **Public failure investigation.** When a bridge fails, an independent body investigates. The findings are public. They shape standards, training, and practice.
- **Liability insurance.** Engineers carry professional indemnity insurance. The market sets rates that reflect actual risk.

This system is slow, expensive, and conservative. It is also remarkably effective. Major bridge failures in the developed world are rare, and the ones that happen produce specific, learnable lessons that reduce the rate of future failures.

## What this would look like for software

Imagine a near-future world in which a similar system applied to software systems above some threshold of public consequence - the systems that handle elections, healthcare records, banking infrastructure, critical communications, AI deployments that affect significant populations.

- **Software engineers who design these systems would hold licences.** The licences would require passing examinations, accumulating supervised experience, and meeting continuing-education requirements. They would be revocable, and revocation would be public.
- **Designs of critical systems would be filed with a regulatory authority.** The filings would include architecture diagrams, threat models, dependency lists, and the safety case the engineer made for the design.
- **Failures would be investigated by an independent body.** The Computer Software Safety Board, by analogy with the NTSB, would investigate major incidents, publish findings, and feed precedent into licensing requirements.
- **Independent code review and architectural inspection would be required for systems above the threshold.** Not friendly internal review - an inspection regime with statutory force.
- **Engineers would carry professional indemnity insurance.** The market would price the risk of their work.

Most of this exists in fragmentary form already - aviation software has something close to it, medical devices have their own version, finance has its compliance regimes. The speculation is what would happen if it were generalised to the broader class of high-consequence software systems.

## What we would gain

The candidates for what improves under this regime are mostly things that have been getting worse, not better, in the current one:

- **Critical systems would last longer.** Software built under licensed-engineer review, with public architectural records, tends to be more conservative in its design choices and more thoroughly considered.
- **Failures would produce real learning.** Right now, when a major system fails - a healthcare data breach, an electoral system bug, an AI deployment that harms users - the internal post-mortem is usually private, the lessons stay inside the company, and the next team makes a similar mistake. Public investigation would change this.
- **Engineers would have a stronger position against business pressure to ship known-unsafe systems.** A licensed engineer with personal liability has institutional cover to refuse work that would not pass an inspection.
- **The profession itself would have higher status and pay.** Licensed professions, in general, do.

## What we would lose

The trade-offs are real and uncomfortable:

- **Speed.** Building software under this regime would be slower. Critical-systems software would be slower the most. Innovation in the regulated tier would proceed at the pace of regulation rather than at the pace of the technology.
- **Cost.** The fixed costs of the regime - licensing, inspection, filings, insurance - would price small operators out of building critical systems. The market would concentrate around firms large enough to bear the overhead.
- **Talent allocation.** A regulated profession is harder to enter. Some of the best people would not get into it, just as some of the best engineers historically did not go into civil engineering when they could go into something less constrained.
- **The non-critical tier.** Most software would still not be regulated, and would still have the current weaknesses. The regime would protect against the worst failures, not all failures.

These are not trivial losses. They are the same trade-offs civil engineering made, and the case for them rests on the magnitude of what is being protected against rather than on any abstract preference for regulation.

## The interesting question

The interesting question is not whether software engineering should be regulated like bridge engineering - that is too abstract to answer. The interesting question is which specific categories of software have reached the threshold where the trade-offs make sense. Critical national infrastructure is an obvious candidate. Medical AI is increasingly one. Election systems, in jurisdictions that take them seriously, already are.

The 2026 conversation about AI safety is, in a sense, the beginning of this discussion. The regulation that is being written for high-risk AI systems is closer to the bridge model than to the unregulated software model. Whether it produces results similar to civil engineering - rare failures, public learning, slow but durable improvement - is the question the next decade will answer.

The deeper point is that the analogy between software and bridges is not as far-fetched as it has historically been treated. As software has moved from "the thing that crashed your spreadsheet" to "the thing that runs the bank, the hospital, and the power grid," the case for borrowing some of the institutional machinery that other industries built for their high-consequence work has gotten stronger. Whether the profession adopts it deliberately, or has it imposed after a sufficiently public failure, is up to the profession.

## Related Reading

- [Knowing What Not to Build](/personal-development/knowing-what-not-to-build/)
- [My Website Projects](/ideas/my-website-projects/)
- [AI Safety: First Principles](/ai/ai-safety-first-principles/)
- [AI Law Trends 2026](/ai/ai-law-trends-2026/)
- [The Architect vs the Builder](/ai/architect-vs-builder/)
