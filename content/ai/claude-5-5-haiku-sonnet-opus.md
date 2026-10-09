---
title: "Claude 5.5: Haiku, Sonnet, and Opus - What Actually Changed"
date: 2026-10-09T08:30:00+01:00
draft: false
tags: ["ai", "anthropic", "claude", "model-release", "comparison", "cost", "llm", "2026", "agent", "coding", "benchmark"]
description: "Anthropic finished the Claude 5.5 family in two weeks: Opus on 22 September, Sonnet on 28 September, Haiku on 7 October. A sourced look at features, pricing, and what each one changes versus its predecessor."
cover:
  image: /assets/images/ai/claude-5-5-haiku-sonnet-opus.jpg
  alt: Claude 5.5 family - Haiku, Sonnet, and Opus
---

## TL;DR

- Anthropic shipped the **Claude 5.5** family in two weeks: **Opus 5.5** on 22 September, **Sonnet 5.5** on 28 September, **Haiku 5.5** on 7 October 2026
- All three share a **1M-token context**, **128K output**, a June 2026 knowledge cutoff, and adaptive thinking steered by an `effort` parameter
- **Haiku 5.5** is the real price shock: $0.10 / $0.50 per million tokens for prompts up to 100K, about **75% cheaper** to run than Haiku 4.5, with a 1M window up from 200K
- **Sonnet 5.5** keeps Sonnet 5's $2 / $10 list price but Anthropic says it is **30%+ faster** and up to **30% cheaper per task**; cache reads dropped to $0.10 on the Haiku launch day
- **Opus 5.5** is priced at $4 / $20, **20% below** Opus 5's $5 / $25, with cache reads cut 60% to $0.20; Anthropic says typical workloads cost about **40% less** and that it matches [Fable 5.1](/ai/claude-fable-5-mythos-5/) on most work
- Use Haiku for volume and subagents, Sonnet for well-scoped everyday coding and docs, Opus for long-horizon judgement. Fable still sits above the 5.5 family at $10 / $50

Anthropic did not drop a single "Claude 5.5" model. It dropped three, one after another, and each one is aimed at a different part of the bill.

The order that matters for anyone catching up this week is the release order. Haiku 5.5 landed two days ago. Sonnet 5.5 is eleven days old. Opus 5.5 has been out for just over two weeks. Together they replace Haiku 4.5, Sonnet 5, and Opus 5 as the public Claude ladder under [Fable](/ai/claude-fable-5-mythos-5/). There is no Haiku 5 in between - the small model jumped a generation.

## How they sit together

API IDs are `claude-haiku-5-5`, `claude-sonnet-5-5`, and `claude-opus-5-5`. All three are on the Claude API, Amazon Bedrock, Google Cloud, and Microsoft Foundry. They are also in Claude Code and on Claude.ai, with the usual plan caveats: Haiku 5.5 is selectable on Free through Enterprise, while Opus 5.5 is for Pro, Max, Team, and Enterprise.

| | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 |
| --- | --- | --- | --- |
| Released | 7 October 2026 | 28 September 2026 | 22 September 2026 |
| Predecessor | Haiku 4.5 | Sonnet 5 | Opus 5 |
| Input / output (per 1M tokens) | $0.10 / $0.50 up to 100K prompts; $0.50 / $2.50 above | $2 / $10 | $4 / $20 |
| Cache reads | $0.01 / $0.05 | $0.10 | $0.20 |
| Context / max output | 1M / 128K | 1M / 128K | 1M / 128K |
| Default effort (API) | `medium` | `high` | `medium` |
| Thinking | Adaptive; can still be disabled at `high` or below | Adaptive; `between_tools` replaces `disabled` | Adaptive, always on |
| Fast mode | No (fastest at standard speed) | No | Yes: $8 / $40, up to 2.5x |
| Knowledge cutoff | June 2026 | June 2026 | June 2026 |

Those cache-read numbers matter more than the sticker price for anyone running agents. Long coding sessions spend most of their money rereading the same prefix. That is why Anthropic's own "costs 40% less" and "costs 30% less per task" claims are about **cost per job**, not a cheaper list price on every row. [Prompt caching](/ai/prompt-caching/) is still the lever.

Batch processing remains 50% off input and output on all three.

## Claude Haiku 5.5 (7 October 2026)

Haiku 5.5 is the one you feel in the invoice. Anthropic calls it the cheapest, fastest, and most capable small model it has released. The predecessor is Haiku 4.5, which shipped on 15 October 2025 at $1 / $5 per million tokens with a 200K context window and 64K max output.

The new list price for prompts up to 100K tokens is **$0.10 input and $0.50 output**. That is a 90% cut on the face of it. Prompts over 100K tokens are $0.50 / $2.50 - still half of Haiku 4.5. Anthropic says about 90% of Haiku 4.5 requests sat under 100K, and that once you include the new tokenizer (the same one introduced with Claude 4.7, which counts the same text as roughly **30% more tokens**), the average job still costs around **75% less**.

The capability jump is not subtle on Anthropic's own table. Haiku 5.5 scores 1620 on GDPval-AA v2.1 against Haiku 4.5's 735; 72.4% on OSWorld 2.1's offline subset against 15.7%; 45.9% on Humanity's Last Exam without tools against 10.2%; and 39.2% on Terminal-Bench 4.0 against 0.0%. It also beats GPT-6 Luna on the rows Anthropic published. Sonnet 5.5 still leads it on every headline eval - 70.6% vs 39.2% on Terminal-Bench 4.0 is the gap that tells you not to make Haiku your only coding model.

What is new in the product, not just the scores:

- First Haiku with an **effort** control and adaptive thinking (on by default; you can still turn thinking off at `high` or below)
- Context window **1M**, output **128K**
- Browser use on the Claude API and Google Cloud
- Computer use via the `computer_toolset_20260801` toolset (the older `computer_20250124` tool errors)
- Safety classifiers that can return `stop_reason: "refusal"` - there is no server-side fallback on this model

Cyber safeguards are tighter than Haiku 4.5's but looser than Sonnet 5.5's: defensive work is in, penetration testing is out. Biology safeguards match Sonnet 5 / 5.5 and Opus 5.

The intended job is high-volume, latency-sensitive work: classification, routing, extraction, summaries, compaction, database queries, live support, and **subagents** under Opus or Sonnet. Anthropic is explicit that Sonnet and Opus remain the better choice for complex agentic coding. That matches the Terminal-Bench gap.

Alongside the model, Anthropic halved Sonnet 5.5 cache reads from $0.20 to **$0.10**, which it says makes most agentic Sonnet work about 20% cheaper. Max and Team subscribers also get a monthly Claude Platform credit: $100 for Max 5x, $200 for Max 20x, and up to $500 pooled on Team.

## Claude Sonnet 5.5 (28 September 2026)

Sonnet 5.5 is the everyday model in this family. Anthropic positions it as a faster, cheaper complement to Opus 5.5: well-scoped tasks, bug fixes, polished documents, slides, and spreadsheets, plus a sharper eye for design. It is also the first Sonnet Anthropic says beat Pokémon Red from screenshots alone.

List price is unchanged from Sonnet 5 at **$2 / $10**. The savings claim is token efficiency: fewer tokens per task, plus **30%+ faster** generation, which Anthropic puts at up to **30% less** for most work. Cache writes stay at $2.50 (5-minute) and $4 (1-hour). Cache reads were $0.20 at launch and are now $0.10 as of 7 October.

The coding jump versus Sonnet 5 is the headline Anthropic wants you to notice. Terminal-Bench 4.0 goes from 10.3% to **70.6%**. CursorBench 4.0 goes from 34.1% to **55.5%**, two points behind Opus 5.5's 57.8%. GDPval-AA v2.1 is 1844 against Sonnet 5's 1449 and Opus 5.5's 1846 - essentially tied with Opus on that knowledge-work leaderboard. Chartography without tools jumps from 15.6% to 61.6%.

Anthropic's own caveat is the one worth keeping: at Max effort Sonnet 5.5 can look comparable to Opus 5.5 on several evals, but in their testing Opus remains clearly stronger at complex, open-ended work that needs sustained judgement. Sonnet 5.5 even beating Opus 5.5 on Terminal-Bench 4.0 (70.6% vs 66.4% at Opus's xhigh setting) does not reverse that. Benchmarks at this level are a noisy guide to which model you want on an ambiguous, multi-hour job.

Migration from Sonnet 5 is not a model-ID swap if you had thinking off. `thinking: {"type": "disabled"}` returns an error; the replacement is `between_tools`. Forced tool use (`tool_choice` of `any` or a named tool) is gone. Thinking blocks are bound to the model and the conversation. The older `computer_20251124` tool is rejected on the Claude API and Google Cloud. Default effort on the API is `high`; Claude Code defaults to `medium`. Unlike Haiku, you cannot fully disable thinking - `between_tools` is the floor.

It is also the first Sonnet to ship with Opus-class cyber safeguards and classifiers against reasoning extraction. Biology safeguards match Sonnet 5.

## Claude Opus 5.5 (22 September 2026)

Opus 5.5 opened the family. Anthropic's claim is that it performs at the level of Claude Fable 5.1 on most work and costs **40% less to run than Opus 5**. It is the first 5.5-class release since Anthropic argued for pacing the frontier; the system card says it was tested before launch by external evaluators including Frontier Design and METR, and that it is the strongest model Anthropic has tested on its automated behavioural audit.

Pricing versus Opus 5:

| Per 1M tokens | Opus 5.5 | Opus 5 |
| --- | --- | --- |
| Input | $4 | $5 |
| Output | $20 | $25 |
| Cache reads | $0.20 | $0.50 |
| Cache writes (5-minute) | $5 | $6.25 |

The 20% cut on input and output is the visible part. The 60% cut on cache reads is the one that hits agentic coding bills. Fast mode, on the Claude API and in Claude Code only, is $8 / $40 for up to 2.5x speed. Subscription five-hour usage limits went up at launch, and there is a rate-limit reset you can save for later.

On Anthropic's table, Opus 5.5 leads Opus 5 across the board: Terminal-Bench 4.0 66.4% vs 52.3%, FrontierCode 54.4% vs 48.0%, CursorBench 57.8% vs 46.6%, GDPval-AA 1846 vs 1708, OSWorld 2.1 81.8% vs 74.0% partial. Anthropic also says the gap to Fable 5.1 is narrower in real use than those scores imply, which is a useful warning if you are about to spend 2.5x more to "upgrade" to Fable for work Opus 5.5 already handles.

The practical upgrades testers keep repeating are long jobs and communication. Anthropic describes a 680,000-line migration finished in under a day, a 200,000-line audit that took under three hours where Opus 5 took over 20 hours and 2.5x the tokens, and writing that puts the important information first. Thinking on Opus 5.5 **cannot be turned off** - effort is the only control, default `medium` (Opus 5 defaulted to `high`). Forced tool use is gone. The same computer-use toolset change applies on the Claude API and Google Cloud.

Safeguards are in the Fable 5.1 neighbourhood for biology and cybersecurity, with fallbacks and verification programmes for vetted life-sciences and cyber-defence work. Prompt-injection resistance is reported as matching or beating Opus 5, tying Fable 5.1 on a Gray Swan eval.

## Which one, for what

The 5.5 family is a routing problem, not a loyalty test.

**Haiku 5.5** if the work is short, repetitive, or parallel: classify, extract, summarise, compact, drive a browser, run a swarm of coding subagents. It is also the first time a Haiku looks usable for real computer-use, which Haiku 4.5 was not on these numbers. Keep it off the open-ended architecture job.

**Sonnet 5.5** if you want the default coding and knowledge-work model. Same dollars per token as Sonnet 5, fewer tokens, faster, and close enough to Opus on several professional evals that many teams will stop reaching for Opus on well-specified tasks. That is the point of the launch.

**Opus 5.5** if the task is long, messy, or judgement-heavy: migrations, audits, overnight agent runs, research where invented figures fail the job. It is also the one with Fast mode when latency matters more than the doubled token rate.

**Fable 5.1** remains the expensive ceiling. Opus 5.5 is Anthropic's argument that you should not need it for most of the work you were using Fable for.

If you are migrating production code, budget a day for the thinking and tool-choice breaking changes. They are small, they return a 400, and they are easy to miss if you only swap the model string.

## Videos

### Claude Haiku 5.5 Is INSANE – This IS the BEST Cheap Model Yet! (7 October 2026)

{{< youtube rGUzoHunuV8 >}}

*Bijan Bowen stress-tests Haiku 5.5 on browser OS, C++, Blender/Godot, and other builds, and notes the whole run used about 1% of a Max weekly usage window.*

### Claude Haiku 5.5: Can Anthropic's Cheapest Model Perform in the Real World? (7 October 2026)

{{< youtube R1g7AXcVz20 >}}

*Fahd Mirza runs a silent-bug fix, a Godot build, multilingual and visual tests, and walks through the new pricing against Haiku 4.5.*

### Introducing Claude Sonnet 5.5 (28 September 2026)

{{< youtube s5nkj-L2vAw >}}

*Anthropic's launch clip for Sonnet 5.5: faster than Sonnet 5, aimed at everyday tasks, with Haiku 5.5 flagged as coming weeks later.*

## Sources

- [Introducing Claude Haiku 5.5 - Anthropic](https://www.anthropic.com/claude-haiku-5-5)
- [Introducing Claude Sonnet 5.5 - Anthropic](https://www.anthropic.com/claude-sonnet-5-5)
- [Introducing Claude Opus 5.5 - Anthropic](https://www.anthropic.com/claude-opus-5-5)
- [Claude Haiku 5.5 overview - Claude Docs](https://platform.claude.com/docs/en/models/haiku-5-5/overview)
- [What's new in Claude Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5)
- [What's new in Claude Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5)
- [What's new in Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5)
- [Introducing Claude Haiku 4.5 - Anthropic](https://www.anthropic.com/news/claude-haiku-4-5)
- [Introducing Claude Haiku 5.5 on AWS](https://aws.amazon.com/blogs/machine-learning/introducing-claude-haiku-5-5-on-aws/)
- [Claude Opus 5.5 System Card (PDF)](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)

## Related Reading

- [The Real Cost of Cloud AI Models in 2026](/ai/the-real-cost-of-cloud-ai-models-2026/)
- [Claude Fable 5 and Mythos 5](/ai/claude-fable-5-mythos-5/)
- [Prompt Caching](/ai/prompt-caching/)
- [The Token Efficiency Mindset](/ai/claude-token-efficiency-mindset/)
- [Claude Opus 4.7: Autonomy and Vision at Scale](/ai/claude-opus-4-7/)
- [The LLM Context Window Arms Race](/ai/llm-context-window-arms-race/)
- [The Rise of Small Language Models](/ai/small-language-models/)
- [Reasoning Models in 2026](/ai/reasoning-models-2026/)
