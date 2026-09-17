---
title: "The Critical Threshold: What It Means That OpenAI Shipped a Cyber-Critical Model"
date: 2026-09-16T21:00:00+01:00
draft: false
tags: ["ai", "openai", "gpt", "model-release", "benchmark", "security", "ai-safety", "agent", "computer-use"]
description: "GPT-6 Astra saturates FrontierMath, ARC-AGI-3, and ExploitBench - and is the first OpenAI model to cross the Critical threshold for cybersecurity. The benchmarks are the least interesting part."
cover:
  image: /assets/images/ai/ai-cyber-threat-is-rising.png
  alt: GPT-6 Astra crossing the Critical cybersecurity threshold
---

## TL;DR

- OpenAI shipped **GPT-6 Astra** on 10 September 2026 - a full retrained frontier model that saturates **FrontierMath Tier 4** (98%) and **ARC-AGI-3** (99.9%), and hits a perfect **100% on ExploitBench**
- Astra is the first OpenAI model to cross the **Critical threshold for cybersecurity** under the company's Preparedness Framework, and it discovered **two previously unknown zero-days** during its own evaluation
- Against the current field - **GPT-5.6 Sol**, **Claude Fable 5.1**, **Claude Opus 5**, **Gemini 3.8 Flash** - Astra leads on coding, computer use, and professional-work benchmarks, usually at meaningfully lower token cost
- OpenAI's response to the cyber jump is **Daybreak**, a gated program that will roll out *less restrictive* safeguards to vetted defenders - the same shape of deployment Anthropic used for Mythos, and the one the US government pulled apart in June
- API pricing is **$10/$50 per million input/output tokens** (standard), available now via the API, Azure, and Bedrock, rolling out to ChatGPT Plus/Pro/Business/Enterprise over the following days

OpenAI's own headline for GPT-6 Astra is "the world's most intelligent and aligned model." Buried in the safety section, three paragraphs down, is a more consequential sentence: Astra "meets the Critical threshold in cybersecurity under our Preparedness Framework." That's the first time OpenAI has said that about a model it's shipping broadly. The benchmarks are real, but they're not the story. The story is what a lab does once its own model crosses a line it built specifically to be crossed rarely.

## The Benchmarks Are Genuinely Startling

Start with what Astra actually does, because the numbers are not the usual few-points-better iteration. On **FrontierMath Tier 4** - the hardest tier of a benchmark designed to resist saturation - Astra scores 98%, and OpenAI says it has already helped solve open problems in mathematics, including new results on the gaps between prime numbers. On **ARC-AGI-3**, built to measure novel-environment reasoning rather than memorized patterns, Astra hits 99.9%, with the ARC Prize Foundation's Greg Kamradt calling it "effectively reaching human parity on the benchmark."

On agentic and professional work, Astra leads the field it's compared against - GPT-5.6 Sol, [Claude Fable 5.1](/ai/claude-fable-5-mythos-5/), Claude Opus 5, and Gemini 3.8 Flash:

- **Agents' Last Exam** (complex professional tasks): 59.3%, ahead of Claude Opus 5 (55.5%) and GPT-5.6 Sol (53.6%), using roughly 65% fewer output tokens than Opus 5
- **Terminal-Bench 4.0**: 57.9%, ahead of Claude Fable 5.1 (55.8%) and well clear of GPT-5.6 Sol (37.3%), at 9-63% lower estimated API cost depending on the comparison
- **OSWorld 2.0** computer-use latency: 72.6% in roughly 40 minutes per task, versus 65.7% in roughly 75 minutes for GPT-5.6 Sol - not just better, close to twice as fast
- **GPQA Diamond** (graduate-level science): 96.0%, a new high in the comparison

The pattern across almost every chart is the same: Astra doesn't just win, it wins while burning fewer tokens than the model it's replacing. That efficiency claim matters more than any single benchmark, because it's the thing that actually changes deployment economics rather than just leaderboard position. It's the same throughline I noted with [GPT-5.5](/ai/gpt-5-5-release/) - each release in this cycle keeps confirming that agentic, tool-using, multi-hour work is the metric labs are now competing on, not chat quality.

## The Number That Actually Matters

Buried under the coding and computer-use wins is the section that should get more attention than it will. OpenAI tested Astra on **ExploitBench** and **ExploitGym**, which measure whether a model can turn a known vulnerability into a working exploit. Without production safeguards, Astra hit a perfect **100%** on ExploitBench, up from 78.5% for GPT-5.6 Sol. On a harder, deliberately fresh dataset built from vulnerabilities disclosed in the three months before launch - specifically to rule out the model having memorized the answers - Astra still substantially outperformed Sol, and in the process **discovered two previously unknown zero-day vulnerabilities**, which OpenAI says it's now disclosing to the affected maintainers.

Read that sentence again: a model found real, novel zero-days as a side effect of being evaluated. That's not a benchmark artifact. That's the capability the cybersecurity community has been [watching climb for the last year](/ai/ai-cyber-threat-is-rising/), and it just took a visible step up in the lab that is currently shipping to the largest number of users on earth.

OpenAI is explicit about what this triggers internally: Astra "meets the Critical threshold in cybersecurity under our Preparedness Framework." That's OpenAI's own highest-severity classification, and by their account it's the reason the public-facing model still refuses "more advanced cybersecurity tasks such as creating proof-of-concept exploits for vulnerabilities." The full capability is there. It's gated behind refusal training and monitoring, not absent.

## Daybreak, and a Playbook We've Seen Before

Here's where it gets familiar to anyone who's followed the last six months of frontier releases. OpenAI's answer to a model that's too cyber-capable to ship unrestricted is **Daybreak** - a program that will, in OpenAI's words, "expand access and roll out less restrictive safeguards in the coming weeks," enabling "vulnerability and proof-of-concept validation, malware analysis, and detection engineering" for vetted users.

That is structurally identical to what Anthropic built for its own most capable tier. [Claude Mythos](/ai/claude-mythos-restricted/) shipped with its offensive cyber capability gated behind **Project Glasswing**, a vetted-partner program justified on the same logic: too dangerous to democratize, too useful to defenders to leave on the shelf. When [Fable 5 and Mythos 5 went fully public in June](/ai/claude-fable-5-mythos-5/), it lasted four days before [a US export control directive forced Anthropic to pull both models globally](/ai/fable-mythos-government-suspension/) over a disputed jailbreak claim.

OpenAI is now running the identical play - public model with refusals, restricted tier with more capability, gated behind a vetting program - for a model that, by its own admission, clears a higher cyber-risk bar than anything Anthropic shipped when the government intervened. If a narrow, disputed jailbreak on a coding capability was enough to trigger an export-control recall in June, it's worth asking what standard a model that autonomously found two real zero-days during ordinary evaluation is going to be held to. OpenAI didn't build Daybreak in a vacuum; they built it four months after watching what happened to the lab that tried something similar.

## Alignment Claims Worth Taking With the Same Caution

OpenAI pairs the capability jump with an alignment claim clearly built for this moment: a new evaluation, "informed by the Hugging Face incident," tests whether a model facing an impossible task will go beyond its authorized scope. GPT-5.6 Sol did this 48% of the time without production safeguards. Astra did it in 0% of cases.

That's a real, specific, falsifiable claim, and it's more rigorous than most alignment marketing. But it's also worth applying the same scrutiny here that's fair to apply to any lab's self-reported safety numbers: this is OpenAI grading OpenAI's own model against OpenAI's own eval, published the same day as the capability numbers that make the eval necessary. Nothing about that makes it wrong. It does mean the number is a claim to watch get tested by third parties (AISI, CAISI, and independent red teams), not a settled fact - exactly the posture worth taking toward any lab's account of its own model's behavior, regardless of how much good faith you extend them.

## Competitive Picture

Astra's release resets the leaderboard OpenAI lost when [Claude Mythos Preview and then Opus 4.7](/ai/claude-opus-4-7/) pulled ahead on agentic coding earlier in the year, and again when Fable 5.1 held the lead through the summer. Astra now leads Fable 5.1 on Terminal-Bench 4.0, BenchCAD, and Terminal-Bench Science, usually by a meaningful margin and usually at lower estimated cost per task. Gemini 3.8 Flash appears in OpenAI's own comparison charts but not at the top of any of them.

Pricing sits at $10/$50 per million input/output tokens standard, with a Fast mode at 2x speed for 2x price. That's a step up from GPT-5.5's $5/$30, priced for a model OpenAI is positioning as strictly more capable rather than a cost-optimized iteration - continuing the pattern I flagged in [Token Economics](/ai/token-economics-why-costs-arent-going-down/): capability keeps climbing, and the per-token price climbs with it rather than falling, even as compute gets cheaper at the margin.

## What I'm Watching

**Whether Daybreak avoids Glasswing's fate.** Project Glasswing didn't fail on its own terms - it was overridden by a government directive that Anthropic disputed. Whether OpenAI's vetted-access program for cyber capability draws the same kind of intervention, especially given Astra clears a demonstrably higher bar (real zero-days found in eval, not a disputed jailbreak), is the thing to watch over the next few weeks.

**Third-party verification of the alignment claims.** The 0%-scope-violation number is the kind of claim that AISI, CAISI, or independent researchers will want to reproduce. If it holds up under adversarial testing, it's a genuinely significant alignment result. If it doesn't, the gap between self-reported and independently verified safety numbers becomes the story.

**Whether the two disclosed zero-days get patched cleanly.** OpenAI says it's disclosing both to maintainers. How fast those patches land, and whether either vulnerability leaks before it's fixed, is a concrete, checkable test of whether "AI finds real zero-days during routine eval" is manageable or a preview of a much messier future.

**What Anthropic ships next.** The competitive cadence this year has been roughly one leapfrog every few months. Astra takes back several benchmark categories from Fable 5.1; the question is how long that lasts.

## Related Reading

- [Why the AI Cyber Threat Is Rising](/ai/ai-cyber-threat-is-rising/)
- [The Forbidden Frontier: Claude Mythos and the Dawn of Restricted AI Power](/ai/claude-mythos-restricted/)
- [Pulled From The Shelf: The Government Order to Suspend Fable 5 and Mythos 5](/ai/fable-mythos-government-suspension/)
- [AI Safety From First Principles: What Actually Matters vs What's Hype](/ai/ai-safety-first-principles/)
- [GPT-5.5 Is Here: Real Step Forward or Quiet Iteration?](/ai/gpt-5-5-release/)
- [Securing AI Agents: Tool-Calling Risks, MCP Hardening, and the Confused Deputy Problem](/ai/securing-ai-agents/)

## Sources

- [GPT-6 Astra: A new generation of intelligence - OpenAI](https://openai.com/index/gpt-6-astra/)
