---
title: "The AI Model Price List, October 2026"
date: 2026-10-17T08:00:00+01:00
draft: false
tags: ["ai", "llm", "cost", "economics", "openai", "anthropic", "deepseek", "google", "xai", "cursor", "qwen", "comparison", "model", "2026"]
description: "All 35 major model prices as of 17 October 2026, from Meta's $0.10/$0.20 Contributor tier to GPT-6 Astra Fast at $20/$100, with what each model is actually for."
cover:
  image: /assets/images/ai/ai-cloud-subscriptions.jpg
  alt: AI model API pricing comparison for October 2026
---

## TL;DR

- Every figure below was checked against the provider's own pricing page on **17 October 2026**. Prices are USD per million tokens, standard tier unless labelled
- The input floor is now **$0.10 per million tokens**, set by Meta's Muse Spark Contributor tier, Claude Haiku 5.5, and GPT-6 Luna. The output floor is **$0.20**, set by Muse Spark Contributor
- The ceiling is **$20 input / $100 output** for GPT-6 Astra in Fast mode at short context. Standard Astra, Claude Fable 5.1 and Claude Mythos 5.1 sit at **$10 / $50**
- The same model can cost **2x to 21x** more depending on context length, speed mode, time of day, and whether you accept training-data terms. Grok 4.7 doubles above 200K prompt tokens. DeepSeek doubles at peak. Gemini 3.8 Flash and Gemini 4 Argon both have scheduled price increases
- Claude Opus 5.5 is cheaper than the model it replaced: **$4/$20** against Opus 5's **$5/$25**. Claude Haiku 5.5, released 7 October, undercuts almost every "cheap" model at **$0.10/$0.50** for prompts up to 100K tokens
- The useful question is not which model is cheapest. It is which tasks need the expensive tier, and which can be routed down without anyone noticing

I pulled these numbers directly from [OpenAI](https://developers.openai.com/api/docs/pricing), [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing), [Google](https://ai.google.dev/gemini-api/docs/pricing), [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing), [xAI](https://docs.x.ai/developers/pricing), [Meta](https://dev.meta.ai/docs/pricing-rate-limits), [Z.AI](https://docs.z.ai/guides/overview/pricing), [MiniMax](https://platform.minimax.io/docs/guides/pricing), [Moonshot](https://platform.moonshot.ai/docs/pricing), [QwenCloud](https://www.qwencloud.com/), [LongCat](https://longcat.chat/platform/docs/pricing/longcat-2.0), [Sakana](https://sakana.ai/fugu/), [Together](https://www.together.ai/pricing) and [Cursor](https://cursor.com/docs/models-and-pricing).

Two caveats. Xiaomi's console is a client-rendered app that served no readable price table to an unauthenticated fetch, so the MiMo figures come from [OpenRouter's public model API](https://openrouter.ai/api/v1/models). LongCat's docs now list only a limited-time rate of $0.30/$1.20. The $0.75/$2.95 standard rate that appeared in older comparison tables is no longer shown, so I have left it out rather than repeat a number I could not verify.

This is a snapshot, not a quote. Treat it as a map of the market on one day.

---

## The Full Price List

Sorted by output price, then input price. "1M + 1M" is one million input tokens plus one million output tokens. It is a ranking device, not a realistic workload, because most production traffic is far more input-heavy than output-heavy.

| Model | Input / 1M | Output / 1M | 1M + 1M | Best for |
| --- | ---: | ---: | ---: | --- |
| **Meta Muse Spark 1.2 / 1.3 Contributor** | $0.10 | $0.20 | $0.30 | Prototyping and bulk agent runs where Meta may train on your data |
| **Xiaomi MiMo-V2.6-Flash** | $0.14 | $0.28 | $0.42 | High-volume agentic and multimodal work; open weights |
| **OpenAI GPT-6 Luna** | $0.10 | $0.50 | $0.60 | Classification, extraction, routing, high-volume tasks |
| **Anthropic Claude Haiku 5.5 (prompts up to 100K)** | $0.10 | $0.50 | $0.60 | Classification, routing, extraction, subagents |
| **DeepSeek V4.1 Flash, off-peak** | $0.15 | $0.60 | $0.75 | Overnight and batch agent work; vision support |
| **Xiaomi MiMo-V2.6-Pro** | $0.435 | $0.87 | $1.305 | Flagship coding and long-horizon agentic work |
| **MiniMax M3 (up to 512K input)** | $0.30 | $1.20 | $1.50 | Long-horizon agents and coding with 1M context |
| **LongCat 2.0, limited-time promo** | $0.30 | $1.20 | $1.50 | Repository-level coding and agentic work |
| **DeepSeek V4.1 Flash, peak** | $0.30 | $1.20 | $1.50 | The same model when you cannot schedule around UTC peak |
| **DeepSeek V4 Pro, off-peak** | $0.66 | $1.98 | $2.64 | Harder reasoning and coding, scheduled off-peak |
| **Google Gemini 3.8 Flash (through 31 December 2026)** | $0.75 | $3.75 | $4.50 | Long-horizon software engineering and enterprise agents |
| **DeepSeek V4 Pro, peak** | $1.32 | $3.96 | $5.28 | The same model at peak hours |
| **Meta Muse Spark 1.1 / 1.2 / 1.3** | $1.25 | $4.25 | $5.50 | Long-running agentic, multi-agent and coding work |
| **Meta Muse Spark Open, Together serverless** | $1.25 | $4.25 | $5.50 | Serverless access to the open-weight coding model |
| **Z.AI GLM-5.3** | $1.40 | $4.40 | $5.80 | Coding agents and tool use |
| **xAI Grok 4.7 (prompt below 200K)** | $2.00 | $6.00 | $8.00 | Agentic tool calling and coding; 500K context |
| **QwenCloud Qwen3.8-Max** | $2.00 | $6.00 | $8.00 | 2.4T-parameter MoE flagship; coding, office work, native vision |
| **Google Gemini 3.8 Flash (from 1 January 2027)** | $1.50 | $7.50 | $9.00 | The same model after the scheduled increase |
| **OpenAI GPT-6.1 Sol** | $2.00 | $10.00 | $12.00 | Near-Astra coding, computer use and professional work |
| **Anthropic Claude Sonnet 5.5** | $2.00 | $10.00 | $12.00 | Best speed-intelligence balance for coding agents |
| **Google Gemini 4 Argon (intro, through 30 November 2026)** | $2.00 | $10.00 | $12.00 | Flagship reasoning, software engineering, maths and science |
| **xAI Grok 4.7 (prompt 200K and above)** | $4.00 | $12.00 | $16.00 | The same model with a long prompt |
| **Cursor Grok 4.7 Fast (up to 256K)** | $4.00 | $12.00 | $16.00 | Lower-latency coding inside Cursor |
| **OpenAI GPT-5.4** | $2.50 | $15.00 | $17.50 | Older flagship for coding and professional work |
| **Moonshot Kimi K3** | $3.00 | $15.00 | $18.00 | 2.8T-parameter open-weight model for coding and knowledge work |
| **Anthropic Claude Opus 5.5** | $4.00 | $20.00 | $24.00 | Long-running agentic coding and knowledge work |
| **Cursor Grok 4.7 Fast (256K to 500K)** | $6.00 | $18.00 | $24.00 | Fast mode with larger context inside Cursor |
| **Google Gemini 4 Argon (from 1 December 2026)** | $4.00 | $20.00 | $24.00 | The same model after introductory pricing ends |
| **Meta Muse Wonder 1.0** | $4.00 | $20.00 | $24.00 | Frontier multimodal reasoning for complex agents |
| **Sakana Fugu Ultra (up to 272K)** | $5.00 | $30.00 | $35.00 | Multi-agent orchestration for hard, high-stakes problems |
| **Anthropic Claude Opus 5.5 Fast** | $8.00 | $40.00 | $48.00 | Lower latency at 2x the standard price |
| **Anthropic Claude Fable 5 / Mythos 5** | $10.00 | $50.00 | $60.00 | Long-horizon frontier work; Mythos is restricted access |
| **Anthropic Claude Fable 5.1 / Mythos 5.1** | $10.00 | $50.00 | $60.00 | Current frontier; long-running agents |
| **OpenAI GPT-6 Astra** | $10.00 | $50.00 | $60.00 | The most demanding reasoning, coding, computer use and research |
| **OpenAI GPT-6 Astra Fast** | $20.00 | $100.00 | $120.00 | The same model at 2x the standard rate |

A few context tiers are hidden inside single rows. Claude Haiku 5.5 rises to **$0.50/$2.50** above 100K prompt tokens. MiniMax M3 rises to **$1.20/$4.80** above 512K input tokens. Sakana Fugu Ultra rises to **$10/$45** above 272K. Grok 4.7 and Cursor's Fast variant are split into separate rows because the jump is large enough to change routing decisions.

---

## What Changed Since September

My September post on cloud AI costs told a simple story: frontier output cost $50, and everything underneath was getting cheaper. That is still true, but the shape has changed in four ways.

**The floor moved down again.** Meta's Contributor mode prices Muse Spark at **$0.10/$0.20** in exchange for permission to train on your prompts and outputs. Claude Haiku 5.5, released on 7 October, is **$0.10/$0.50** for prompts up to 100K tokens. GPT-6 Luna is **$0.10/$0.50**. The cheapest output tier in this table is now **$0.20 per million tokens**, and four models charge $0.50 or less.

**The middle got crowded.** Between $1.20 and $6 output there are now more than a dozen credible models: MiMo-V2.6-Pro, MiniMax M3, LongCat 2.0, DeepSeek V4 Pro off-peak, Gemini 3.8 Flash, Muse Spark, GLM-5.3, Grok 4.7 and Qwen3.8-Max. This is where most production coding agents should probably live.

**Anthropic cut the price of its own flagship.** Claude Opus 5.5 launched on 22 September at **$4/$20**, below Opus 5 at **$5/$25**. Sonnet 5.5 launched on 28 September at **$2/$10**, the same price as Sonnet 5. Haiku 5.5 then arrived at the bottom. For once, the newer model is not the more expensive one.

**Two promotional prices have hard end dates.** Gemini 3.8 Flash is **$0.75/$3.75** through 31 December 2026, then **$1.50/$7.50** from 1 January 2027. Gemini 4 Argon is **$2/$10** through 30 November 2026, then **$4/$20** from 1 December 2026. Those are not forecasts. They are published prices with dates attached, and they double the cost of two models that look cheap in every comparison table today.

There is also a softer change: discounts are increasingly conditional. MiniMax advertises M3 at **$0.30/$1.20** with a "permanent 50% off" label against a list price of **$0.60/$2.40**. "Permanent" is a marketing promise, not a contract term. LongCat's **$0.30/$1.20** is explicitly a limited-time promo. Meta's cheapest tier is cheap because you are paying with your data. The headline number is real, but the conditions around it matter as much as the number.

---

## The Four Levers That Move the Bill

Published rates are only the first line of the invoice. Four multipliers do most of the damage.

### 1. Context length

Long prompts are no longer billed at the same rate as short ones. Grok 4.7 goes from **$2/$6** to **$4/$12** once the prompt crosses 200K tokens. Cursor's Grok 4.7 Fast goes from **$4/$12** to **$6/$18** above 256K. Claude Haiku 5.5 multiplies by five above 100K. MiniMax M3 doubles above 512K. Fugu Ultra doubles its input price and adds 50% to output above 272K. GPT-6 Astra charges **2x input and 1.5x output** for the whole request above 272K tokens.

This is not a rounding error. A retrieval-heavy agent that stuffs 300K tokens of repository context into every call can pay twice the advertised rate on every call. The fix is architectural: retrieve less, cache more, compact aggressively.

### 2. Speed mode

Fast modes are a latency tax. GPT-6 Astra Fast doubles the standard rate to **$20/$100**. Claude Opus 5.5 Fast doubles to **$8/$40**. Cursor's Grok 4.7 Fast doubles input and output. OpenAI also sells an Ultrafast tier for Astra at **$60/$300**, six times standard.

The question to ask is not "is fast worth it?" It is "which calls are on the critical path?" A planning call that blocks a user-facing response might justify Fast. A background summarisation job almost never does.

### 3. Time of day

DeepSeek is the clearest example of inference priced like electricity. Peak hours are **01:00 to 04:00 and 06:00 to 10:00 UTC, Monday to Friday**, excluding Chinese public holidays. Everything else is off-peak at half price. V4.1 Flash is **$0.15/$0.60** off-peak and **$0.30/$1.20** at peak. V4 Pro is **$0.66/$1.98** off-peak and **$1.32/$3.96** at peak.

If your workload is batch, you can halve the bill by moving it. If it is interactive and global, you cannot, and you should budget the peak rate.

### 4. Data terms

Meta's Contributor mode is **12.5x cheaper on input and 21.25x cheaper on output** than Standard mode for Muse Spark. That is the largest single discount in this table, and it is not a volume discount. It is payment in training data. For a hobby project or a throwaway prototype, that can be a good trade. For customer data, regulated data, or anything under NDA, it is not a discount at all.

Caching and batch processing sit alongside these. Anthropic and OpenAI both halve batch prices. Cache reads are typically 10% of input, and on Fable 5.1 and Mythos 5.1 they are **2.5%**. A well-cached agent can beat a nominally cheaper model that has no cache.

---

## What Each Tier Is Actually For

**Under $1 output: plumbing.** Haiku 5.5, GPT-6 Luna, MiMo-V2.6-Flash, DeepSeek V4.1 Flash off-peak and Muse Spark Contributor. These are not models you ask to design a system. They classify, extract, route, tag, summarise, and act as subagents. Anthropic explicitly positions Haiku 5.5 for classification, routing, extraction and subagent tasks. OpenAI positions Luna for "focused, high-volume tasks." Using either for open-ended reasoning is a false economy, because you will spend the savings on retries.

**$1 to $6 output: the workhorse tier.** MiMo-V2.6-Pro, MiniMax M3, LongCat 2.0, DeepSeek V4 Pro off-peak, Gemini 3.8 Flash, Muse Spark, GLM-5.3. This is where coding agents, repository assistants, document pipelines and long-horizon tool users should start. The models are good enough for multi-step work, and the price is low enough that a failed attempt does not hurt. Gemini 3.8 Flash is the standout here on capability per dollar, but only until 31 December.

**$6 to $18 output: frontier-adjacent.** Grok 4.7, Qwen3.8-Max, GPT-6.1 Sol, Claude Sonnet 5.5, Gemini 4 Argon at introductory pricing, GPT-5.4 and Kimi K3. These are the models you escalate to when the workhorse fails. Sonnet 5.5 and Sol are the obvious defaults for serious coding agents. Kimi K3 is open-weight, which changes your leverage over price and deployment. Qwen3.8-Max matters because it is a 2.4T-parameter flagship at **$2/$6**.

**$20 to $60 output: frontier and orchestration.** Claude Opus 5.5, Muse Wonder, Sakana Fugu Ultra, Fable 5/5.1, Mythos 5/5.1 and GPT-6 Astra. Opus 5.5 is the value pick of this group at **$4/$20**, and Anthropic itself says most workloads should start there and move up to Fable only when evals justify it. Fugu Ultra is a different product category: a learned multi-agent orchestrator that routes across a pool of models and bills a single blended rate. It is for hard, high-stakes problems where answer quality matters more than token price.

**Fast modes: latency.** GPT-6 Astra Fast at **$20/$100** and Opus 5.5 Fast at **$8/$40**. You are not buying more intelligence. You are buying the same intelligence sooner.

---

## A Worked Example: 10M Input, 2M Output

Assume a coding agent that reads 10 million tokens and writes 2 million in a month. That is a 5:1 input-to-output ratio, which is closer to real agent traffic than the 1:1 ranking column above.

| Model | Monthly cost |
| --- | ---: |
| GPT-6 Astra or Claude Fable 5.1 | $200.00 |
| Claude Opus 5.5 | $80.00 |
| GPT-6.1 Sol or Claude Sonnet 5.5 | $40.00 |
| Gemini 3.8 Flash (2026 price) | $15.00 |
| DeepSeek V4.1 Flash, off-peak | $2.70 |
| Claude Haiku 5.5 or GPT-6 Luna | $2.00 |
| Xiaomi MiMo-V2.6-Flash | $1.96 |
| Meta Muse Spark Contributor | $1.40 |

The same token count ranges from **$1.40 to $200**, a 143x spread. No single model wins on both quality and cost. The point is that the choice is now large enough to be worth engineering: route the easy 80% down, escalate the hard 20%, and measure the difference in success rate rather than in tokens.

That is the same argument I made in [The Real Cost of Cloud AI Models in 2026](/ai/the-real-cost-of-cloud-ai-models-2026/), and the spread has widened since September. The cheapest models got cheaper. The expensive ones did not.

---

## What I'm Watching

- **1 December 2026:** Gemini 4 Argon doubles from $2/$10 to $4/$20. Any product built on introductory Argon pricing needs a new unit economics model before then
- **1 January 2027:** Gemini 3.8 Flash doubles from $0.75/$3.75 to $1.50/$7.50. It is the best value in the table today and will be merely competitive next year
- **Whether "permanent" discounts survive.** MiniMax's 50% off and LongCat's promo are both conditional. If either ends, the workhorse tier shifts
- **Whether Contributor-style pricing spreads.** Meta has made data consent a first-class price tier. If other labs follow, the cheapest model may be the one that trains on you
- **Whether Haiku 5.5 pulls the floor down elsewhere.** A $0.10/$0.50 model with a 1M context and adaptive thinking puts pressure on every mid-priced "small" model

The direction of travel is clear. Intelligence at the top is holding its price. Intelligence in the middle is collapsing. The engineering problem is no longer access to a good model. It is knowing which call deserves one.

---

## Sources

- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [GPT-6 Astra model page](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [GPT-6.1 Sol model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
- [GPT-6 Luna model page](https://developers.openai.com/api/docs/models/gpt-6-luna)
- [GPT-5.4 model page](https://developers.openai.com/api/docs/models/gpt-5.4)
- [Claude Platform pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Claude Haiku 5.5 overview](https://platform.claude.com/docs/en/models/haiku-5-5/overview)
- [Claude Sonnet 5.5 overview](https://platform.claude.com/docs/en/models/sonnet-5-5/overview)
- [Claude Opus 5.5 overview](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- [Claude Fable 5.1 overview](https://platform.claude.com/docs/en/models/fable-5-1/overview)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [DeepSeek models and pricing](https://api-docs.deepseek.com/quick_start/pricing)
- [xAI API pricing](https://docs.x.ai/developers/pricing)
- [xAI models and context windows](https://docs.x.ai/docs/models)
- [Meta Model API pricing and rate limits](https://dev.meta.ai/docs/pricing-rate-limits)
- [Z.AI pricing](https://docs.z.ai/guides/overview/pricing)
- [MiniMax pricing](https://platform.minimax.io/docs/guides/pricing)
- [MiniMax text generation docs](https://platform.minimax.io/docs/guides/text-generation)
- [Moonshot Kimi pricing](https://platform.moonshot.ai/docs/pricing)
- [Kimi K3 quickstart](https://platform.moonshot.ai/docs/guide/kimi-k3-quickstart)
- [QwenCloud](https://www.qwencloud.com/)
- [LongCat 2.0 pricing](https://longcat.chat/platform/docs/pricing/longcat-2.0)
- [Sakana Fugu pricing](https://sakana.ai/fugu/)
- [Together AI pricing](https://www.together.ai/pricing)
- [Cursor models and pricing](https://cursor.com/docs/models-and-pricing)
- [OpenRouter model API](https://openrouter.ai/api/v1/models)
- [Xiaomi MiMo platform](https://platform.xiaomimimo.com/)

## Related Reading

- [The Real Cost of Cloud AI Models in 2026](/ai/the-real-cost-of-cloud-ai-models-2026/)
- [Token Economics: Why Your AI Bill Isn't Going Down](/ai/token-economics-why-costs-arent-going-down/)
- [Claude 5.5: Haiku, Sonnet, and Opus](/ai/claude-5-5-haiku-sonnet-opus/)
- [Is the $20 AI Subscription Era Over?](/ai/twenty-dollar-ai-era-is-over/)
- [We Are Learning to Buy Intelligence](/ai/we-are-learning-to-buy-intelligence/)
