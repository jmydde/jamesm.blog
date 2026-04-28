---
title: "Prompt Caching: The Quiet Performance Win for LLM Applications"
date: 2026-05-12T08:00:00+01:00
draft: false
tags: ["ai", "prompt-cache", "performance", "llm", "cost", "agentic-engineering"]
description: "What prompt caching actually is, why it is the highest-leverage performance and cost optimisation available to most LLM applications, and the patterns that determine whether you get a 90 percent cost reduction or no benefit at all."
cover:
  image: assets/images/ai/prompt-caching.jpg
  alt: Prompt Caching Banner
---

If you build LLM applications for any length of time, you eventually notice that you are paying to have the model read the same instructions over and over again. The system prompt, the tool definitions, the few-shot examples, the [structured output schema](/ai/structured-outputs-schema/) - all of it goes back into the model on every single request, and you pay for the input tokens every single time. For a chatbot doing one or two thousand requests a day this is annoying. For an [agent doing tens of thousands of requests with long contexts](/ai/ai-agents-that-actually-work/), it is the dominant cost line.

Prompt caching is the technique that fixes this, and in 2026 it is one of the highest-leverage optimisations available to anyone running production LLM workloads. It also has surprisingly subtle failure modes when you get the layout of your prompts wrong, which is why posts like this one exist.

## What prompt caching actually is

When a language model processes a prompt, it builds an internal representation of every token in the input. That representation is expensive to compute, because it involves running the full attention mechanism over every preceding token. For a long prompt, the cost of building this representation dominates the time and cost of the request.

[Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching), as offered by major model providers including [Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) and [OpenAI](https://platform.openai.com/docs/guides/prompt-caching), is the practice of saving that internal representation between requests, so that subsequent requests with the same prompt prefix can reuse the cached representation rather than recomputing it. The model still has to process the new tokens at the end of the prompt, but the long static prefix becomes essentially free.

The savings are dramatic. On most providers, cached prompt tokens cost roughly ten percent of the price of uncached tokens, and the latency improvement is similar. A request that was previously 3000 input tokens at full price becomes a request with 2900 cached tokens at ten percent and 100 new tokens at full price. The math at scale is significant.

## Why this is bigger than it sounds

The reason prompt caching is high-leverage is that LLM applications tend to have a specific shape. The prompt is mostly static. The system prompt, tool definitions, examples, and instructions can easily be 1500 to 5000 tokens, and they are identical across requests. The dynamic part - the user's question, the conversation history, the current state of the agent's task - is comparatively small.

Without caching, you are paying full price to remind the model of the same instructions on every request. With caching, you pay full price once and then near-zero price for the rest of the day. For an application that has any meaningful traffic, the cost reduction is often eighty to ninety percent of the input token bill. This is one of the few levers that genuinely moves the needle in the broader [token economics picture](/ai/token-economics-why-costs-arent-going-down/), and it is what informs much of the [token efficiency mindset](/ai/claude-token-efficiency-mindset/) I write about elsewhere.

Latency benefits stack on top of this. The cached tokens are not just cheaper, they are also faster, because the model is not actually computing them again. For interactive applications where time-to-first-token matters, prompt caching can move you from feeling laggy to feeling responsive without any other changes.

## The shape of a cacheable prompt

The thing that determines whether you get the benefit is whether your prompt has a long, identical prefix across requests. If it does, caching works. If it does not, caching is silently doing nothing.

The discipline that makes caching work is to structure your prompts in three layers, in this order:

1. **Static instructions.** System prompt, tool definitions, output schemas, behaviour guidelines, few-shot examples. Anything that is identical across requests goes here, at the top.
2. **Slow-changing context.** Documents that change infrequently, the user's profile or persona, project-level information that is stable across a session. This layer is cacheable across many requests but invalidated when the underlying context changes.
3. **Dynamic input.** The user's current message, the latest conversation turn, this request's specific input. This is the only part that should change request-to-request.

If you structure your prompt this way, the cache key naturally lines up with the longest stable prefix, and the dynamic part becomes the small tail you pay full price for. If you interleave dynamic input into the middle of your prompt - inserting the user's name into the system prompt, putting the current timestamp before the static instructions, sprinkling fresh information through the prompt rather than appending it at the end - you defeat caching, and you do so silently.

## The single most common mistake

The single most common mistake I see is variables interpolated into the system prompt. Something like:

```
You are an assistant for {customer_name}'s account, currently in {timezone},
with these current preferences: {preferences}.

[long static instructions]

User: {user_message}
```

This looks fine on its face, and produces correct outputs. The problem is that every customer's prompt is different in the first sentence, and so the entire static section beneath it is uncacheable. You are paying full price for the static instructions on every request, despite them being literally identical.

The fix is mechanical. Move the variables to the end:

```
[long static instructions]

Account context: {customer_name}, timezone {timezone}, preferences {preferences}.

User: {user_message}
```

Now the static instructions are at the top and form a long stable prefix that caches across all customers. The dynamic context is at the end where it belongs.

This sounds obvious in retrospect. It is not obvious in the moment, because the natural way to write a prompt is in narrative order, with the personalisation up front. Writing prompts in cache-aware order is a learned discipline, and it is one of the highest-leverage things you can teach your team.

## Cache lifetimes and invalidation

Cached prompts do not live forever. Each provider has its own caching lifetime - typically minutes to a small number of hours - and the cache is invalidated when the prefix changes in any way, including changes you might not expect. Whitespace changes, newline normalisation, even small differences in formatting can produce a different cache key.

The practical implications are:

- **Use the same prompt construction code on every request.** Do not regenerate the system prompt with slightly different formatting, even if the formatting differences are semantically irrelevant.
- **Be deliberate about when you bust the cache.** Adding a new tool, updating the system prompt, changing the output schema - these are cache-busting events. Plan them so they happen at low-traffic moments rather than during peak.
- **Watch your cache hit rate.** Most providers expose metrics for cache hits versus misses. If your hit rate is dropping, something in your prompt construction is changing that you did not expect, and the cost of finding it is small compared to the cost of paying full price.
- **Use cache breakpoints intentionally.** Anthropic's API exposes explicit cache control points that let you mark specific positions in the prompt as cacheable. This gives you fine-grained control and lets you cache portions of the prompt selectively.

## Where caching does not help

There are workloads where prompt caching does not provide significant benefit, and it is worth being clear about them.

**Single-shot one-off requests.** If your application generates a unique prompt for each user, with no shared structure, caching has nothing to cache. This is rare in practice but it does happen.

**Workloads with very long dynamic context.** If 80 percent of your prompt is the user's just-uploaded document and 20 percent is your system prompt, you only get caching on the 20 percent. The economics still favour caching, but the savings are modest. This is one of the reasons the [context window arms race](/ai/llm-context-window-arms-race/) matters less than it appears - more headroom does not help if you cannot cache it.

**Workloads with very low traffic.** Cache lifetimes are bounded. If your traffic is so low that the cache expires between requests, you pay the full miss penalty on every request and get the same cost as no caching. This affects very small applications and rarely-used internal tools.

**Workloads where the prompt is fundamentally per-request.** Some agent workloads have a long memory of the agent's history that grows with each step. The prompt is partially shared with previous steps but is fundamentally different each time. Caching helps but the gains are smaller than for static-prefix workloads.

In all of these cases, caching is not harmful - it just does not help much. The discipline of structuring prompts cache-friendly is still worth keeping, because the moment your usage pattern changes, the caching benefit will appear automatically.

## The operational pattern that works

The teams I see getting the most out of prompt caching share a few practices.

**They measure cache hit rate explicitly.** Every dashboard for the LLM workload shows the cache hit rate alongside the request volume and the cost. This makes regressions visible immediately rather than showing up as a gradually rising bill.

**They version their prompts explicitly.** Prompt changes are deliberate, reviewed, and rolled out at known times. This makes it easy to understand why the cache hit rate dropped on a given day, because you can see the deployment that caused it.

**They centralise prompt construction.** The code that builds the prompt is in one place, behaves deterministically, and is the only path that produces a request to the model. Decentralised prompt construction with similar-but-not-identical templates is one of the most reliable ways to invisibly destroy cache performance.

**They treat the cache as a first-class resource.** When estimating the cost of a feature, they distinguish between requests that will hit the cache and requests that will miss it. When estimating latency, the same. Cache behaviour is part of the system design, not an afterthought.

## What I would tell someone starting today

If you are building any LLM application that has more than a handful of requests, structure your prompts cache-friendly from day one. The discipline is small. The savings compound.

If you have an existing application, the highest-leverage optimisation you can do this week is to audit your prompt construction, find the variables that are interleaved with static content, move them to the end, and watch your cache hit rate climb. The cost of doing this is hours. The savings can be tens of thousands of dollars a month at production scale.

If you are evaluating model providers, ask explicitly how their caching works. The mechanics differ. The pricing differs. The cache lifetime differs. These differences can be the deciding factor in which provider is cheapest for your workload, and the headline per-token price is misleading without them.

The reason prompt caching is the quiet performance win is that it does not require model changes, prompt-engineering wizardry, or fancy infrastructure. It requires writing prompts in a slightly different order. The leverage-to-effort ratio is the highest of any optimisation in the LLM toolkit, and it remains underused. If you are paying full price for tokens you have already computed, you are leaving money on the table.
