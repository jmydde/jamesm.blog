---
title: "Fable 5 Is Back: What Anthropic Learned From Eighteen Days Off The Shelf"
date: 2026-07-01T08:00:00+01:00
draft: false
tags: ["ai", "anthropic", "claude", "fable", "mythos", "ai-safety", "ai-policy", "cybersecurity", "2026"]
description: "Eighteen days after a US export control directive pulled Fable 5 and Mythos 5 offline, Anthropic is redeploying Fable 5 globally. The company says the jailbreak that triggered the recall was minor, that rival models could do the same thing, and that the industry needs a CVSS-style framework for AI jailbreaks."
cover:
  image: /assets/images/ai/redeploying-fable-5.jpg
  alt: Claude Fable 5 redeployment after export control suspension
---

## TL;DR

- **Fable 5 returns globally on 1 July 2026** on Claude.ai, Claude Code, Claude Cowork, and the Claude Platform, after export controls were lifted on 30 June
- The recall was triggered by an **Amazon research report** describing a jailbreak that let Fable 5 identify software vulnerabilities; Anthropic's testing found **Opus 4.8, GPT-5.5, Kimi K2.7, and others** could do the same
- A new safety classifier blocks the specific technique in **over 99% of cases**; blocked requests fall back to Opus 4.8
- Anthropic argues the jailbreak was **minor** - it intruded into the model's deliberate "safety margin", not its core harmful capabilities
- Together with Amazon, Google, and Microsoft, Anthropic is drafting a **shared jailbreak severity framework** (capability gain, breadth, ease of weaponisation, discoverability) - the AI equivalent of CVSS
- **Mythos 5** is restored for a set of US Glasswing partners; broader international access remains under government coordination

Eighteen days ago I wrote about [the government order that pulled Fable 5 and Mythos 5 off the shelf](/ai/fable-mythos-government-suspension/) - four days after launch, a verbal export control directive at 5:21pm ET, global suspension for every user including Anthropic's own staff. The open question in that post was whether access would be restored in days or weeks, and whether the precedent would reshape how every frontier lab ships models.

We now have an answer to the first part. In a [post published on 30 June](https://www.anthropic.com/news/redeploying-fable-5), Anthropic confirmed the export controls have been lifted and Fable 5 will be available again starting **1 July** on Claude.ai, Claude Code, Claude Cowork, and the Claude Platform. Cloud access on AWS, Google Cloud, and Microsoft Foundry follows as quickly as possible. For Pro, Max, Team, and select Enterprise plans, Fable 5 is included for up to 50% of weekly usage limits through 7 July, then moves to usage credits.

The second question - what this means for the industry - is the more interesting half of the story, and Anthropic spent most of the post trying to answer it.

## What Actually Triggered The Recall

The timeline, now filled in with more detail than the initial suspension statement provided:

**9 June:** Fable 5 and Mythos 5 launch. Same underlying model, different safeguard stacks - Fable for general use with the strongest classifiers Anthropic has ever shipped, Mythos for vetted [Project Glasswing](/ai/claude-mythos-restricted/) cyber defenders with fewer restrictions.

**12 June:** The US government applies export controls after becoming aware of an Amazon research report describing a method of bypassing Fable 5's safeguards. The technique prompted the model to identify software vulnerabilities; in one case it produced code demonstrating how a vulnerability could be exploited. Because the order took effect immediately and Anthropic had no reliable way to verify nationality in real time, it suspended access for **all users globally**.

**26 June:** The government approved restored Mythos 5 access for a set of US organisations.

**30 June:** Export controls on both models lifted. Fable 5 redeployment announced for 1 July.

The crucial new detail is who found the jailbreak and what it actually did. Amazon researchers reported a prompting technique that got Fable 5 to identify vulnerabilities in a codebase - routine defensive cybersecurity work, but work that Fable's conservative classifiers were designed to block or route away. In one instance, the model also produced exploit demonstration code.

Anthropic's own testing, conducted over the following two weeks with government and industry partners, produced a finding that reframes the whole episode: **many less capable models could identify the same vulnerabilities**, including Claude Opus 4.8, GPT-5.5, and Kimi K2.7. For the exploit demonstration specifically, every model Anthropic tested could produce equivalent output - including Haiku 4.5, Sonnet 4.6, Opus 4.6, Opus 4.7, Opus 4.8, GPT-5.4, GPT-5.5, and Kimi K2.7.

That does not mean the jailbreak was harmless. It means the capability it unlocked was not uniquely Mythos-level. The technique exposed a borderline case in Fable 5's safeguards - the kind of task that is unlikely to be dangerous but gets blocked anyway out of an abundance of caution. Anthropic's characterisation, which I reported sceptically in the [suspension post](/ai/fable-mythos-government-suspension/) because we only had their side of the story, now comes with substantially more technical backing.

## The Safety Margin, Explained Properly

The redeployment post includes the clearest public explanation yet of how Anthropic's cybersecurity classifiers actually work, and it is worth understanding because it applies far beyond Fable 5.

The classifiers are smaller AI systems that run during an interaction, watching for requests or outputs that look like potentially harmful cybersecurity work. When they fire, the model does not respond - the request gets routed to Opus 4.8 instead. The goal is not to block everything cyber-related. It is to prevent the model from engaging in **uniquely dangerous** behaviours.

The complication is that classifiers make mistakes in both directions. They miss some harmful content, and they can be jailbroken. Anthropic's response is deliberate over-blocking: they set classifiers to trigger on a set of requests that are **probably benign but might not be**. This "safety margin" means a request has to look very clearly safe to get through.

For Fable 5, Anthropic made that margin larger than on any prior launch. More false positives, fewer missed harmful requests. Users experience this as the model refusing reasonable coding and debugging tasks - the ~5% session fallback rate I noted at [launch](/ai/claude-fable-5-mythos-5/).

The jailbreak taxonomy Anthropic lays out is the useful part:

| Severity | What happens | Example |
|---|---|---|
| **Minor** | Bypasses classifiers but stays within the safety margin | The Amazon report technique |
| **Narrow harmful** | Unblocks a specific harmful behaviour | Low to moderate severity |
| **Universal** | Unblocks a wide range of harmful behaviours | None found for Fable 5 yet |

Anthropic's claim - now tested by CAISI researchers who agree the safeguards are "extraordinarily strong" - is that the Amazon technique falls in the minor category. It did not expose Mythos-level offensive capability. It got the model to do defensive work that the classifiers were deliberately blocking as a precaution.

Whether you find that reassuring depends on how much weight you put on the safety margin concept. I find it intellectually honest: Anthropic is saying they knowingly block some legitimate work to make jailbreaks less dangerous, and that this particular jailbreak only recovered work they had already decided was probably fine. That is a very different story from "the model's core defences failed."

## The Fix, And Its Cost

Working with the government, Anthropic trained an improved classifier targeting the specific behaviour in the Amazon report. Users will be notified when a Fable 5 request is blocked and routed to Opus 4.8. The new classifier blocks the technique in **over 99% of cases**; in the small remainder, the model may provide information not detailed enough to help an attacker.

The tradeoff is more false positives on benign coding and debugging tasks. Anthropic acknowledges this and says they will keep refining. That is the recurring tax of conservative safety tuning: every fix for a jailbreak tends to catch more legitimate users until the classifiers get smarter.

## Why The Industry Needs A CVSS For Jailbreaks

The most forward-looking section of the post is not about Fable 5 at all. It is about what happens the next time someone finds a jailbreak in a frontier model - because there will be a next time.

Right now, there is no agreed standard for describing jailbreak severity. When Amazon's researchers filed their report, there was no shared framework for Anthropic, the government, and other labs to triage the finding against. Should a narrow technique that other models can replicate trigger an export control recall? Should it trigger a classifier update? Should it trigger nothing? Without a common vocabulary, every finding becomes a bespoke negotiation under time pressure.

Anthropic, Amazon, Microsoft, Google, and other Glasswing partners are drafting a consensus framework scored on four criteria:

1. **Capability gain** - How far beyond existing tools does the jailbreak take the user?
2. **Breadth of capability gain** - How many distinct offensive tasks does the same technique unlock?
3. **Ease of weaponisation** - How much skilled human effort does it take to turn the jailbreak into an attack?
4. **Discoverability** - How easy is it for someone to obtain the technique?

The analogy Anthropic draws is CVSS - the Common Vulnerability Scoring System that gives security teams a shared language for software vulnerabilities. CVSS is imperfect and frequently argued over, but it works well enough that a CVE score of 9.8 means something concrete to everyone in the room. AI jailbreaks have no equivalent.

The proposed response tiers are sensible: minor jailbreaks get classifier updates and monitoring; severe ones (active use against critical infrastructure, for example) trigger immediate preliminary mitigations and 24/7 monitoring of submission channels. Anthropic is also launching a HackerOne program for researchers to submit cyber jailbreaks in Fable 5.

Whether this framework gets adopted beyond the Glasswing coalition is the open question. CVSS works because the entire security industry needed a lingua franca and eventually converged on one. AI labs are more competitive and less accustomed to shared standards on safety findings. But the Fable 5 episode is a case study in why they might need one anyway: eighteen days of global unavailability, hundreds of millions of users affected, and a dispute about severity that could not be resolved quickly because nobody had agreed on what "severe" meant.

## The Government Collaboration Layer

The final section describes commitments that go beyond Fable 5 specifically:

- **Pre-release government access** for models that materially advance national-security-relevant capability frontiers, with Anthropic staff embedded alongside government evaluators
- **Rapid information sharing** on jailbreaks and misuse patterns, including advance sharing of threat intelligence reports
- **Dedicated joint research resources**, including compute allocation for government testing
- **A common industry bar** - voluntary security and evaluation standards applied across frontier providers

This builds on nearly two years of pre-existing collaboration and reflects the June 2 Executive Order on advanced AI innovation and security. Anthropic's framing is that these commitments, plus the jailbreak severity framework, should become the basis for systematic industry rules - eventually codified in regulation applied equally across frontier developers.

I read this as Anthropic trying to convert a bad eighteen days into a durable process. The suspension post's central worry was that a post-launch recall over a narrow jailbreak would become precedent for halting every frontier deployment. The redeployment post's answer is: let's build the machinery so the next finding gets triaged properly before anyone reaches for export controls.

That is the right instinct. Whether it survives contact with the next actually serious jailbreak is a different question.

## What This Means If You Use Claude

Practically, for developers and power users:

**Fable 5 is back tomorrow.** If you had workflows built around it before 12 June, they resume. Pro, Max, Team, and select Enterprise plans get Fable 5 for up to half of weekly usage through 7 July.

**Expect more false positives on cyber-adjacent coding tasks.** The new classifier is tuned aggressively. If Fable 5 blocks a legitimate request, you get Opus 4.8 instead - still capable, but not Mythos-class. This is the same fallback architecture from launch, now with a wider trigger zone.

**Mythos 5 remains restricted.** Restored for approved US Glasswing partners only. International expansion is still being coordinated with the government.

**Cloud provider access is catching up.** AWS, Google Cloud, and Microsoft Foundry redeployment follows the direct product rollout.

## Reading This In Context

I want to update the fair-minded posture from the suspension post, now that we have more than a single party's summary of a verbal briefing.

Anthropic's original claim - that the jailbreak was narrow, that equivalent capability exists elsewhere, that a recall was disproportionate - is substantially strengthened by the testing data in this post. CAISI's independent confirmation that the safeguards are extraordinarily strong adds weight. The safety margin framework is internally consistent and matches what they said at launch about deliberately conservative tuning.

What has not changed is that the public still has not seen the government's full reasoning. Export controls were applied and lifted through a process that remains largely opaque. Anthropic is grateful and muddle through; users bore the disruption; researchers and Glasswing partners did the technical work. But the decision machinery itself - who decides, on what evidence, with what appeal path - is still not visible.

The Fable 5 arc in three posts on this blog now runs: [launch with guardrails](/ai/claude-fable-5-mythos-5/), [suspension over a jailbreak](/ai/fable-mythos-government-suspension/), [redeployment with a framework for the next one](/ai/redeploying-fable-5/). That is a compressed version of what the whole frontier AI industry is going to spend the next few years working through - how to ship powerful models, how to respond when safeguards fail, and how to do it without pulling the product offline for everyone every time a researcher finds a clever prompt.

The jailbreak severity framework is the most useful thing to come out of the episode. If it gets adopted, the next Amazon report gets a score instead of a phone call at 5:21pm. That alone would be worth eighteen days of downtime.

## Sources

- [Redeploying Fable 5 - Anthropic](https://www.anthropic.com/news/redeploying-fable-5)
- [Statement on the US government directive to suspend access to Fable 5 and Mythos 5 - Anthropic](https://www.anthropic.com/news/fable-mythos-access)
- [Claude Fable 5 and Claude Mythos 5 - Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5)

## Related Reading

- [Pulled From The Shelf: The Government Order to Suspend Fable 5 and Mythos 5](/ai/fable-mythos-government-suspension/)
- [Claude Fable 5 and Mythos 5: Anthropic's Mythos-Class Models Go Public](/ai/claude-fable-5-mythos-5/)
- [Why the AI Cyber Threat Is Rising](/ai/ai-cyber-threat-is-rising/)
- [The Forbidden Frontier: Claude Mythos and the Dawn of Restricted AI Power](/ai/claude-mythos-restricted/)
- [AI Safety From First Principles](/ai/ai-safety-first-principles/)
- [Policy on the AI Exponential: Dario Amodei's Case for Acting While the Window Is Open](/ai/policy-on-the-ai-exponential/)
