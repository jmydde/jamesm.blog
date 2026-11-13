---
title: "Claude Fable 5.2: Cheaper, Faster, and Four Ways It Can Break Your Code"
date: 2026-11-12T08:00:00+00:00
draft: false
tags: ["ai", "anthropic", "claude", "fable", "mythos", "model-release", "benchmark", "api", "cost", "ai-safety", "2026"]
description: "Anthropic's Claude Fable 5.2 and Mythos 5.2 cut list prices by 20%, run up to 30% faster and top most of Anthropic's own benchmarks. The launch post is about capability. The API docs are where builders should look first: four breaking changes, a 30-day retention requirement, and Anthropic's own advice to start somewhere else."
---

## TL;DR

- On 9 November 2026 Anthropic [released Claude Fable 5.2 and Claude Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) - the same underlying model, with Mythos lifting some cyber and biology safeguards for vetted organisations
- List price drops from **$10 / $50** to **$8 / $40** per million input/output tokens, with outputs **up to 30% faster** than the 5.1 models. A new Fast mode costs $16 / $80
- Fable 5.2 leads Anthropic's table on most benchmarks, including **49.1% on FrontierCode 2.0** (Xhigh) against 45.5% for Opus 5.5 - but not all of them
- Anthropic reports **about 55% fewer safety-classifier blocks** than Fable 5.1, with safeguards it says are "as robust" as before
- The [API docs](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2) list **four breaking changes** from Fable 5.1, and both models require 30-day data retention
- Anthropic still says most work should start on **Opus 5.5**. Everything after "My read" is opinion

I already wrote about the most eye-catching claim in this launch, [the thousand-agent operating system experiment](/ai/fable-5-2-thousand-agents-operating-system/). This post is about the model itself, and specifically about what changes for people who call it from their own code. As a data engineer, I care less about whether a model can formalise Fermat's Last Theorem and more about whether my extraction pipeline still returns valid JSON on Monday.

## What Anthropic shipped

Fable 5.2 is the third release in the Fable line, after [Fable 5 in June](/ai/claude-fable-5-mythos-5/) and Fable 5.1. The structure is unchanged: Fable is the general-use model with safety classifiers, Mythos is the same model with certain cyber and biology safeguards removed. Mythos 5.2 is available through Anthropic's Cyber Verification Program and its recently expanded Life Sciences Verification Program. Claude Enterprise customers can also reach it through Claude Security without joining the cyber program.

The headline numbers, from the launch post and the [models documentation](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2):

- **Standard price:** $8 / $40 per million input/output tokens, down from $10 / $50 on Fable 5.1
- **Fast mode:** $16 / $80, with up to 2.5x faster token generation
- **Batch:** $4 / $20
- **Cache reads:** $0.20 per million, the same 0.025x multiplier as Fable 5.1
- **Context window:** 1M tokens, with 128k max output

Fable 5.2 is available on the Claude API, Claude Platform on AWS, Amazon Bedrock, Google Cloud and Microsoft Foundry. In the Claude apps and Claude Code, Medium effort is the default. On the API, the default is High.

There are also two new roles for multi-model setups. As an **Advisor**, Fable 5.2 can be consulted by Haiku, Sonnet or Opus on harder problems. As an **Orchestrator**, it delegates simpler work to smaller models. That second one matters for cost, and I come back to it below.

## The benchmarks, including the ones it loses

Anthropic says Fable 5.2 and Mythos 5.2 "are a step above Opus 5.5 in almost all the capabilities we evaluated". The word "almost" is doing honest work, so it is worth reading the table rather than the summary. These are Anthropic's own numbers, at each model's highest effort unless noted:

| Benchmark | Fable 5.2 | Fable 5.1 | Opus 5.5 | GPT-6 Astra | Gemini 4 Carbon |
|---|---|---|---|---|---|
| FrontierCode 2.0 | 49.1% (Xhigh) | 32.4% | 45.5% | 42.8% | 41.1% |
| FrontierSWE v2 | 69.9% | 56.3% | 62.3% | 65.5% | 61.2% |
| AutomationBench | 51.4% | 31.4% | 42.5% | 41.4% | **53.9%** |
| Remote Labor Index | 41.3% (High) | 17.9% | 21.3% | 20.8% | - |
| Humanity's Last Exam (tools) | 74.2% | 65.6% | 67.7% | 57.2% | - |
| AA-Briefcase v1.1 (Elo) | 1785 | 1669 | **1800** | 1569 | 1611 |

Two things stand out to me.

First, the jump from Fable 5.1 is large for a point release. Remote Labor Index more than doubles, and FrontierCode goes from 32.4% to 49.1%.

Second, it does not sweep. Gemini 4 Carbon beats it on AutomationBench, the business workflow benchmark, and Opus 5.5 edges it on AA-Briefcase Elo. Those are the two benchmarks closest to ordinary office and integration work. That fits the pattern Anthropic itself describes: Fable shines on long, hard, open-ended technical work, and the gap narrows on more routine tasks.

The more useful numbers for budgeting are the efficiency ones. Anthropic says Fable 5.2 at High effort scores 45.3% on FrontierCode, about level with Opus 5.5 at Max, "for roughly half the cost per task". It also says Fable 5.2 at Low effort matches Opus 5.5's top Humanity's Last Exam score at under a tenth of the cost. If those hold up in your own evals, the cheaper-per-token model is not always the cheaper-per-task model.

## Fewer blocks, same safeguards

The safety change most users will notice is fewer false positives. Anthropic says that in early testing across claude.ai, Claude Code and Cowork, "we observed about 55% fewer blocks with Fable 5.2 compared with Fable 5.1". The split is about 60% fewer in cybersecurity and 40% fewer in biology. Blocked queries still fall back to Opus 4.8 for cyber and Opus 5 for biology.

On alignment, Anthropic says it believes "high-stakes risks from misalignment remain low". The figure I found most interesting is the adversarial sandbox escape test: Mythos 5.2 used planted credentials or files in 3.1% of scenarios, against 21% for Mythos 5.1 and 39% for Mythos 5. That is a steep drop across three releases. The launch post also notes that both new models voice suspicion of being evaluated more often than recent models, which is a reminder that a better score on a test the model suspects is a test should be read with some care.

Anthropic also says this release has its "strongest-ever protections against distillation attacks". Given the [history of the Fable line with regulators](/ai/fable-mythos-government-suspension/), I read that as aimed as much at policymakers as at competitors.

## What the docs say that the launch post does not

This is the section I would send to anyone running Fable in production. The [what's new page](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2) lists four changes from Fable 5.1 that can break code:

1. **The prefix check now applies to every account.** If anything before a Fable 5.2 thinking block changes - the system prompt, the tools, or an earlier message - sending that block back returns a 400 error. On Fable 5.1 this only applied to accounts created on or after 31 August 2026, so older accounts may have code that edits history and has never failed.
2. **Only Fable 5.2 and Mythos 5.2 can read Fable 5.2 thinking blocks.** Move a conversation to Opus 5.5, Fable 5.1 or one of the fallback models and the reasoning for those turns is dropped. The request still succeeds, so this one fails quietly.
3. **The older `computer_20251124` computer use tool returns an error** everywhere except Amazon Bedrock. Use `computer_toolset_20260801` instead.
4. **A Fable 5.2 executor needs a Fable 5.2 or Mythos 5.2 advisor** when using the advisor tool.

If you use Claude Code, claude.ai, Managed Agents or the Agent SDK, the docs say nothing changes for you. The risk sits with teams that build their own request loops, which in data engineering is most of us.

Two other details are worth knowing. Forced tool use (`tool_choice` of `any` or a named tool) is not supported, so structured extraction should use strict tool use or JSON outputs instead. That is not new if you are coming from Fable 5.1, but it is if you are coming from Opus 5 or earlier. And both models "require 30-day data retention and aren't available under zero data retention unless expressly authorized by Anthropic". Anthropic's answer for regulated customers is Enterprise Frontier Safeguards, which runs safety monitoring inside the customer's own infrastructure and is in private beta with customers including Bridgewater, Salesforce and Stripe.

The docs also flag behaviour changes that need no code change to appear. Prompt lines asking the model to skip deliberation do not stop it thinking at Medium and above. Long tasks can end early with a list of what remains, more often at Low and Medium. And how much it delegates to subagents depends heavily on your harness, with the docs warning that subagents "can account for a large part of what a session costs".

## My read

This section is opinion.

**Anthropic is telling you not to default to it.** The launch post recommends that users "start with Claude Opus 5.5, our strongest daily driver" and move up to Fable only when needed. The docs say the same thing more bluntly: move to Fable 5.2 "when your evals on a Claude Opus model at higher effort still don't meet your requirements". I think that is the right advice, and it is unusual for a vendor to put it in the launch post of its flagship.

**The price cut matters less than the efficiency claims.** A 20% cut on list price is nice. But if High effort Fable really does match Max effort Opus at half the cost per task, the decision is no longer "premium model versus cheap model". It is "which model and effort level gets this task done for the fewest total tokens". That is an eval question, not a pricing-page question, and it is the same one I raised in my [October price list](/ai/ai-model-price-list-october-2026/).

**The quiet failure is the dangerous one.** Of the four breaking changes, the prefix check fails loudly with a 400, which is good. The thinking-block portability change fails silently. Plenty of teams run routers that fall back to a cheaper model or a different vendor tier on errors or cost limits. After moving to Fable 5.2, every such switch drops reasoning without an error. Your pipeline keeps running and your output quality changes. If I were migrating a production workload, I would log the `input_transformations` field the docs describe and alert on dropped blocks before trusting the switch.

**The customer quotes point at the right problem.** Of the many tester quotes, two describe what I actually want from a long-running agent. Andrew Mager at Uber said "It works until the job is actually complete instead of stopping at a plausible checkpoint." Adhyyan Sekhsaria at Cognition said "Claude Fable 5.2 says it doesn't know things instead of hallucinating." Those are vendor-selected quotes, and the docs themselves warn that turns can still end before the work is done. But calibrated stopping and honest uncertainty are exactly the properties that decide whether an unattended data pipeline agent is useful or a liability.

## What I'm Watching

- **Independent benchmarks.** Every number above is Anthropic's own. I want to see FrontierCode and AutomationBench results run by third parties
- **Real cost per task.** Whether the "half the cost of Opus 5.5" claim survives contact with messy production prompts and heavy subagent use
- **Enterprise Frontier Safeguards.** If it leaves private beta, it removes the biggest blocker to using Fable on regulated data
- **Mythos 5.2 in the wild.** Mozilla's Brian Grinstead says it "roughly doubled the vulnerability discovery metrics of Mythos 5.1" in their scanning. I want to see what the disclosed CVE count looks like in six months

## Sources

- [Anthropic: Introducing Claude Fable 5.2 and Claude Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) - launch post, benchmarks, safety results, customer quotes, 9 November 2026
- [Claude Platform Docs: What's new in Claude Fable 5.2](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2) - breaking changes, pricing, availability, data retention
- [Claude Platform Docs: Fable 5.2 migration guide](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide) - step-by-step migration from Fable 5.1, Mythos 5.1 and Opus models
- [Anthropic: Claude Fable 5.2 and Mythos 5.2 System Card](https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card) - full safety and alignment evaluations
- [Anthropic: Enterprise Frontier Safeguards](https://www.anthropic.com/news/enterprise-frontier-safeguards) - safety monitoring compatible with zero data retention

## Related Reading

- [A Thousand Agents, One Engineer, Eight Days](/ai/fable-5-2-thousand-agents-operating-system/) - the operating system experiment from the same launch
- [Claude Fable 5 and Mythos 5](/ai/claude-fable-5-mythos-5/) - the original Fable and Mythos split
- [Fable 5 Is Back](/ai/redeploying-fable-5/) - what the export control recall taught Anthropic
- [AI Model Price List: October 2026](/ai/ai-model-price-list-october-2026/) - how Fable pricing compares across vendors
- [Claude 5.5: Haiku, Sonnet and Opus](/ai/claude-5-5-haiku-sonnet-opus/) - the daily-driver models Anthropic says to start with
