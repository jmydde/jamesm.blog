---
title: "Token Economics: Why Your AI Bill Isn't Going Down"
date: 2026-04-13T06:40:00+01:00
draft: false
tags: ['ai', 'economics', 'infrastructure']
lastmod: 2026-09-27T09:00:00+01:00
description: "Per-token prices have fallen fast, yet AI bills keep rising. Here's why cheaper tokens and bigger bills are the same story."
cover:
  image: /assets/images/ai/twenty-dollar-ai-era-is-over.jpg
  alt: Token economics - why AI costs are not falling
---

*Updated September 2026. The original version of this post argued that LLM prices had stayed flat. That was wrong - per-token prices have fallen steeply - and the post has been rewritten around the claim that actually holds: bills aren't going down.*

## TL;DR

- **Per-token prices have fallen a long way.** GPT-4 launched in March 2023 at $30 / $60 per million input/output tokens. Claude 3 Opus launched in 2024 at $15 / $75. By 2026, Anthropic's Opus-tier models list at $5 / $25, and capable mid-tier and open-weight models cost well under a dollar per million input tokens.
- **Bills are rising anyway.** Cheaper tokens unlock workloads that consume vastly more of them: agents that loop for hours, reasoning models that think in tens of thousands of hidden tokens, and whole codebases in context.
- **The frontier tier resets upward.** Each new top-tier model tends to launch at a premium, so "the best model" rarely gets cheap even as last year's best does.
- **The true cost is more than the token price** once you add retries, evaluation, monitoring and the engineering around it.

## Two Different Curves

There are two numbers people conflate when they ask whether AI is getting cheaper.

The first is **price per token for a given level of capability**. That has fallen dramatically. The capability that cost $30 per million input tokens in 2023 is available from several providers for a small fraction of that today, and open-weight models running on commodity inference providers have pushed the floor lower still. Competition, better serving software (batching, speculative decoding, quantisation, prompt caching) and newer GPUs all push in the same direction.

The second is **what an organisation actually spends on AI**. That has gone up, often steeply. Both things are true at once, and the second is a consequence of the first.

## Why Bills Rise When Prices Fall

This is the Jevons paradox in a new setting: when something useful gets cheaper, people use so much more of it that total spend increases.

**Agents multiply token counts.** A chat exchange might use a few thousand tokens. An agent working through a coding task re-sends its instructions, tool outputs and file contents on every step, and can easily consume millions of tokens in an afternoon. That work simply wasn't affordable at 2023 prices.

**Reasoning tokens are invisible but billed.** Reasoning models generate long internal chains before answering. On hard problems those chains run to tens of thousands of tokens - in extreme benchmark settings, far more - and you pay for them as output tokens.

**Context got bigger.** Windows grew from a few thousand tokens to hundreds of thousands and beyond. Longer prompts per request mean more input tokens per request, even at a lower price per token.

**The use cases expanded.** Once tokens were cheap enough, teams moved from "ask the model a question" to "run the model over every document, ticket and commit". Volume grows faster than price falls.

## Why the Frontier Stays Expensive

The newest, most capable model is usually priced at a premium, and it's the one people want for hard work. Serving it is genuinely expensive: large models need many GPUs per replica, and long contexts make each request heavier. So while last year's frontier becomes cheap, this year's frontier resets the top of the price list. If you always use the best model, your per-token price falls much more slowly than the market's.

The economics underneath are mostly about **utilisation**. A GPU costs roughly the same per hour whether it's busy or idle, and providers make money by batching many users' requests onto the same hardware. That's why off-peak discounts, batch APIs and cached-input pricing exist: they all reward traffic that is easier to pack efficiently.

## The Real Cost You're Not Seeing

The token price is only part of what AI costs to run in production:

- **Retries and failures** - requests that time out, return malformed output or fail validation still cost money
- **Evaluation** - running test suites against prompts and models every time something changes
- **Monitoring and tracing** - storing and inspecting what the system did
- **Engineering time** - building routing, caching, guardrails and fallbacks

As a rough rule, budget meaningfully more than the raw token bill. How much more depends on how much of that tooling you already have.

## What Actually Lowers Your Bill

- **Route by difficulty.** Send routine work to small or mid-tier models and reserve the frontier model for tasks that need it. This is usually the largest single saving.
- **Cache aggressively.** Stable system prompts and shared context billed at a cached rate cut input costs substantially. See [Prompt Caching](/ai/prompt-caching/).
- **Use batch and off-peak pricing** for anything that isn't interactive.
- **Control reasoning effort.** Most APIs let you cap or lower thinking; not every task needs maximum effort.
- **Keep context lean.** Retrieve what the task needs instead of pasting everything.
- **Measure per task, not per token.** A pricier model that finishes in one pass can be cheaper than a cheap one that needs three attempts.

## What This Means for 2026 and Beyond

Expect both trends to continue. Capability per dollar will keep improving, and the cheapest useful tier will keep getting cheaper. At the same time, agentic and always-on workloads will keep pushing total consumption up faster than prices fall. The organisations that control costs will be the ones that treat tokens like any other cloud resource: metered, routed, cached, and attributed to the work that consumed them.

## Related Reading

- [The Real Cost of Cloud AI Models in 2026](/ai/the-real-cost-of-cloud-ai-models-2026/)
- [Prompt Caching: The Quiet Performance Win for LLM Applications](/ai/prompt-caching/)
- [The Token Efficiency Mindset - Why Your Claude Conversations Cost More Than They Should](/ai/claude-token-efficiency-mindset/)
- [AI Cloud Subscriptions: Comparing Pricing and Features in 2026](/ai/ai-cloud-subscriptions/)
- [GPU Servers vs AI API Credits: The Real Cost Breakdown (2026)](/ai/gpu-servers-vs-api-credits/)
- [Is the $20 AI Subscription Era Over?](/ai/twenty-dollar-ai-era-is-over/)
