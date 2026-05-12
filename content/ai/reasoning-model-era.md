---
title: "The Reasoning Model Era: When to Use o3, R1, Gemini Thinking, and Claude Extended"
date: 2026-05-12T20:30:00+01:00
draft: true
tags: ["ai", "reasoning", "model", "openai", "anthropic", "deepseek", "gemini"]
description: "Reasoning models became a distinct product category in 2025-2026. A practical breakdown of when to reach for one, when the cheaper non-reasoning model is the right call, and how each of the major reasoning models actually differs in production use."
cover:
  image: /assets/images/ai/reasoning-model-era.jpg
  alt: The Reasoning Model Era Banner
---

In 2023 every LLM was a "reasoning model" in the loose sense that you could ask it to think and it would produce something that resembled thought. In 2024 OpenAI shipped o1 and the industry quietly invented a new product category: models that visibly spend more compute thinking through a problem before answering, and that perform meaningfully better on hard problems as a result. By 2026 every frontier lab has shipped its own reasoning model, the patterns for when to use them have stabilised, and the price differences are big enough that the choice actually matters.

## TL;DR

- **Reasoning models trade time and tokens for accuracy.** They are slower, more expensive per task, and substantially better on problems that genuinely require multi-step reasoning.
- **Use them for hard problems where being right matters more than being fast.** Mathematical derivations, complex coding refactors, scientific reasoning, careful analysis of structured arguments.
- **Use non-reasoning models for everything else.** Conversational interactions, simple lookups, content generation, anything where a competent first-pass answer is enough.
- **The major options in 2026** are OpenAI's o3 and o4 series, Anthropic's Claude Extended Thinking, Google's Gemini Reasoning, and DeepSeek's R1 successors - each with distinct strengths.
- **The interesting design pattern** is hybrid: route easy queries to fast models and hard queries to reasoning models, deciding at runtime which is which.

## What reasoning models actually do

The product label hides a fairly specific technical thing. A reasoning model is a frontier LLM that has been trained to spend a meaningful amount of inference compute generating an internal chain of thought before producing the user-visible answer. The internal chain is often not shown - the model thinks privately, then writes the response.

The training is the part that matters. Reasoning models are post-trained, typically with reinforcement learning, to produce internal reasoning chains that are factually accurate, well-structured, and lead to correct conclusions. The chain itself is not a magic incantation - it is the result of significant training effort directed at making the model's own reasoning reliable.

The empirical result is that on hard problems - the kind where a non-reasoning model would confidently produce a plausible-sounding wrong answer - reasoning models often produce the correct answer with high reliability. The trade-off is wall-clock time (often seconds per response) and per-call cost (often an order of magnitude higher than a non-reasoning equivalent).

## Where they pay off

The cases where reaching for a reasoning model is the right call cluster around a few categories:

**Mathematical and quantitative reasoning.** Word problems, derivations, statistical analysis, financial calculations. The kind of work where a small error early in the chain compounds into a wrong final answer.

**Complex coding tasks.** Multi-file refactors, debugging subtle bugs, designing data structures. Reasoning models think through the implications of a change before suggesting it.

**Scientific and technical analysis.** Reasoning about experimental design, interpreting results, evaluating claims in technical papers. Anything where the model needs to be careful rather than fluent.

**Structured argument analysis.** Reading a legal document and identifying the obligations, examining a contract for ambiguities, evaluating a logical argument. The kind of task that rewards methodical step-by-step thought.

**High-stakes decisions where being right matters.** Cases where the cost of a wrong answer is high enough to justify the extra inference cost.

## Where they do not

The places where reasoning models add friction without value:

- **Conversational interactions.** The latency makes them feel slow and unnatural in chat.
- **Content generation.** Writing an email, drafting a blog post, creating marketing copy - a fast model produces work that is hard to distinguish from a slow one.
- **Simple lookups.** "What is the capital of Bolivia" does not benefit from extended thought.
- **Tool-heavy agentic loops.** When most of the work is calling tools and parsing results, the reasoning model's strength is wasted on the orchestration overhead.

The honest assessment is that reasoning models are a specialised tool, not a default. Using one for everything is expensive and slow; using one for nothing leaves accuracy on the table for the cases that benefit.

## How the major options compare

**OpenAI o3 and o4** remain the headline products. The strongest pure-reasoning performance on benchmark math and coding tasks, the highest cost per token, and the most aggressive "spend more compute, get better answers" knob. The o-series is what most teams reach for when they need state-of-the-art reasoning and are willing to pay for it.

**Anthropic's Claude Extended Thinking** is built into the Claude family rather than being a separate product. The extended-thinking mode gives [Claude](/ai/claude-opus-4-7/) deliberate internal reasoning steps; the same model can be invoked in fast mode for routine work. The strength is integration with the rest of the Claude ecosystem - tool use, agentic loops, long context all work the same way regardless of thinking mode.

**Google Gemini Reasoning** has carved out the niche of strong reasoning at competitive pricing, with particular strength on multimodal reasoning problems. Gemini's reasoning over images, video, and audio is meaningfully ahead of the text-only reasoning competition.

**DeepSeek R1** and its successors remain the open-weight reasoning option that opened the category to non-frontier-lab users. The performance is competitive with the closed alternatives for many tasks; the cost-per-token is much lower; the trade-off is that you have to run the inference yourself.

## The hybrid pattern that works

The deployment pattern that most teams running serious production workloads have converged on is hybrid routing. A cheap, fast classifier model looks at the incoming request and decides whether it is a "hard" question that warrants reasoning model treatment or a "routine" question that goes to a fast model. The decision is made in milliseconds; the routing is invisible to the user.

This is harder to operate than picking one model and using it for everything, but the economics are dramatically better. Reserving reasoning-model spend for the queries that actually need it - typically a small fraction of total traffic for most applications - keeps the cost manageable while preserving the accuracy benefit where it matters.

The teams running this pattern report 80-90% of queries handled by fast models and 10-20% routed to reasoning models. The split varies by domain. A coding assistant routes more to reasoning. A customer support bot routes less.

## The interesting consequence

The interesting longer-term consequence of the reasoning-model era is that it has split the LLM market into two related but distinct product categories. Fast models for the high-volume, latency-sensitive, accuracy-tolerant work. Reasoning models for the lower-volume, accuracy-critical work. The pricing reflects this, the architectures are diverging, and the labs are increasingly developing them as separate product lines.

The 2026 application developer is no longer choosing "which model" - they are choosing which mix of models, with which routing logic, for which workloads. That is a more sophisticated design problem than the 2023 version of the same question, and it produces more sophisticated applications.

## Related Reading

- [Claude Opus 4.7: Autonomy and Vision at Scale](/ai/claude-opus-4-7/)
- [Claude's Memory and Long Context in 2026](/ai/claude-long-context-and-memory-2026/)
- [The Open Weight Models Renaissance](/ai/open-weight-models-renaissance/)
- [DeepSeek](/ai/deepseek/)
- [GPT-5.5 Is Here](/ai/gpt-5-5-release/)
