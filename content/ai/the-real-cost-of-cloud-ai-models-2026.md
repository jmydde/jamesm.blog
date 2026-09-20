---
title: "The Real Cost of Cloud AI Models in 2026"
date: 2026-09-20T08:20:00+01:00
draft: false
tags: ["ai", "openai", "anthropic", "deepseek", "xai", "cursor", "cost", "economics", "llm", "2026", "agent"]
description: "A September 2026 snapshot of OpenAI, Anthropic, DeepSeek, SpaceXAI and Cursor pricing. Frontier output still costs $50 per million tokens. Grok 4.6 is $6. Composer 2.5 is $2.50. Off-peak DeepSeek Flash is $0.60. The real metric is cost per successful task."
cover:
  image: /assets/images/ai/ai-cloud-subscriptions.jpg
  alt: Cloud AI model pricing comparison for 2026
---

## TL;DR

- Published API prices now run from **$0.15 per million input tokens** (DeepSeek V4.1 Flash, off-peak) to **$50 per million output tokens** (GPT-6 Astra, Claude Fable 5.1, and several other frontier models)
- SpaceXAI prices [Grok 4.6](https://x.ai/news/grok-4-6) at **$2/$6**, and claims it matches GPT-5.6 Sol on the Artificial Analysis Intelligence Index. Cursor's in-house [Composer 2.5](https://cursor.com/blog/composer-2-5) is **$0.50/$2.50**
- A hypothetical coding agent using 10M input tokens and 20M output tokens costs about **$1,100** on Astra or Fable 5.1, **$140** on Grok 4.6, **$55** on Composer 2.5, and about **$13.50** on off-peak DeepSeek Flash
- For many developers the bill is not an API invoice. It is a [Cursor](https://cursor.com/docs/models-and-pricing) plan plus usage pools, with daily agent users typically landing at **$60 - $100 a month** and power users at **$200+**
- Raw token price is the wrong metric. The useful one is **cost per successful task**, after retries, caching, batch discounts, peak/off-peak scheduling, and whether you left Fast mode on
- Cached input can be **40x to 50x** cheaper than fresh input. Anthropic's Batch API halves input and output. DeepSeek charges half-price outside two weekday UTC windows
- The winning architecture is not "one smartest model." It is expensive intelligence where it matters, cheap intelligence where it does not, and routing between them

Imagine two coding agents doing the same amount of work: 10 million input tokens in, 20 million output tokens out.

On [GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra) or [Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview), that bill is about **$1,100**.

On [Grok 4.6](https://docs.x.ai/developers/pricing) it is about **$140**. On [Composer 2.5](https://cursor.com/docs/models-and-pricing) it is about **$55**.

On [DeepSeek V4.1 Flash](https://api-docs.deepseek.com/quick_start/pricing) during off-peak hours, it is about **$13.50**.

Same token counts. More than an 80-fold difference at the extremes, and a wide middle that did not exist when frontier output all clustered near $50.

That is the shape of cloud AI pricing in September 2026. The gap between models is no longer a few cents per million tokens. It is the difference between a serious production budget and pocket change - and it is large enough that model choice has become an optimisation problem rather than a brand preference.

The question is no longer "which model is smartest?" It is:

> **What level of intelligence does this task require, and what is the lowest total cost at which it can be completed reliably?**

This is a snapshot of published rates from OpenAI, Anthropic, DeepSeek, SpaceXAI and Cursor as of 20 September 2026. Prices move. Treat the tables as a map of the current market, not a quote that will still be true in December.

I wrote in April that [token prices were not falling in a way that mattered](/ai/token-economics-why-costs-arent-going-down/). That was true at the frontier then, and it is still true at the $50 output tier now - Astra and Fable still charge that. What has changed is everything underneath. The cheap models have got much cheaper, SpaceXAI is selling a claimed Sol-class model at $6 output, Cursor has an in-house coding model at $2.50, caching has become a first-order cost lever, and DeepSeek has started pricing inference like electricity: more expensive when the grid is busy.

---

## Five Very Different Approaches

**OpenAI** sells a broad range from Luna at $0.20/$1.20 through to GPT-6 Astra at $10/$50, with a lot of emphasis on agentic workloads and cost efficiency. The GPT-5.6 family is three durable capability tiers - Sol, Terra, Luna - sitting under Astra at the top.

**Anthropic** has a more obvious capability ladder: Haiku, Sonnet, Opus, then the much more expensive Fable tier, with Mythos as a restricted twin of Fable.

**DeepSeek** is aggressively optimising price-performance. V4.1 Flash currently offers particularly low token prices, and the company prices peak and off-peak hours separately.

**SpaceXAI** (xAI) prices Grok 4.6 as a frontier coding and agent model at $2/$6 - Sonnet-class money for a model it says matches Sol on a composite intelligence index. Long prompts at 200k tokens double the rate. A separate coding model, Grok Build 0.1, sits at $1/$2.

**Cursor** is not a lab. It is the editor through which a large share of these tokens are actually burned. It sells $20 / $60 / $200 plans with two usage pools, an in-house Composer 2.5 model at $0.50/$2.50, and jointly trained Grok 4.6 at the same list price as the SpaceXAI API. On-demand usage after the included pool is billed at those token rates.

These are not directly equivalent models. A $0.15/M input model is not competing with a $10/M input model on exactly the same workload. The important question is what each model can reliably accomplish.

---

## OpenAI Model Pricing

OpenAI's current text API lineup is centred on four GPT-5.6 and GPT-6 tiers. These are the standard-processing rates for contexts below 272K input tokens. Requests above that threshold are billed at 2x input and cache rates and 1.5x output for the full request. Batch and Flex processing are half the standard rates. Fast mode is twice. ([OpenAI API pricing](https://developers.openai.com/api/docs/pricing))

| Model             | Input / 1M | Cached input / 1M | Output / 1M | Positioning        |
| ----------------- | ---------: | ----------------: | ----------: | ------------------ |
| **GPT-6 Astra**   |     $10.00 |             $1.00 |      $50.00 | Frontier           |
| **GPT-5.6 Sol**   |      $4.00 |             $0.40 |      $20.00 | Frontier reasoning |
| **GPT-5.6 Terra** |      $2.00 |             $0.20 |      $12.00 | High capability    |
| **GPT-5.6 Luna**  |      $0.20 |             $0.02 |       $1.20 | High-volume        |

Sol's $4/$20 rate is promotional. OpenAI says that pricing remains available at least through 21 November 2026. Do not treat it as a permanent budget assumption.

OpenAI describes the GPT-5.6 family as three durable capability tiers: **Sol** as flagship intelligence, **Terra** as the balanced option, and **Luna** as the fastest and most cost-efficient. Astra sits above them as the frontier model. All four currently have a 1.05M-token context window and support up to 128K output tokens. ([GPT-5.6 announcement](https://openai.com/index/gpt-5-6/), [Astra model page](https://developers.openai.com/api/docs/models/gpt-6-astra))

The company has also been cutting the efficient end. On 30 July 2026 it reduced Luna's price by 80% and Terra's by 20%. ([OpenAI](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/))

### GPT-6 Astra

**$10/M input, $50/M output**

Astra is the sort of model where token cost becomes secondary to capability when the task itself is difficult: architecture that will be expensive to get wrong, complex research, sophisticated autonomous agents, large-scale codebase analysis, cybersecurity, scientific work. OpenAI describes it as its most capable model, built for the hardest end-to-end work.

### GPT-5.6 Sol

**$4/M input, $20/M output** (promotional)

Sol is the flagship GPT-5.6 model. OpenAI reports state-of-the-art results across coding, knowledge work, cybersecurity and science evaluations, and positions it as substantially cheaper than Astra while still occupying the frontier tier. Typical work: complex coding, architecture, difficult debugging, advanced research, high-value agent tasks.

### GPT-5.6 Terra

**$2/M input, $12/M output**

Terra is the balanced option - everyday software development, code review, technical writing, research, business analysis, moderately complex agents, document processing. For many production applications this is the model that makes more economic sense than sending every request to the frontier.

### GPT-5.6 Luna

**$0.20/M input, $1.20/M output**

This is where OpenAI's pricing becomes particularly interesting. At $1.20 per million output tokens, Luna costs a fraction of Sol or Astra. OpenAI calls it its fastest and most affordable model and says it is designed for cost-sensitive, high-volume workloads. Typical work: routine coding, test generation, documentation, classification, extraction, background agents, repository maintenance.

For an agent generating tens or hundreds of millions of tokens, that difference is the budget.

---

## Anthropic Model Pricing

Anthropic currently has a broader capability ladder. These are the standard API rates. Batch processing halves input and output. ([Claude Platform pricing](https://platform.claude.com/docs/en/about-claude/pricing))

| Model                 | Input / 1M | Cache hit / 1M | Output / 1M | Positioning               |
| --------------------- | ---------: | -------------: | ----------: | ------------------------- |
| **Claude Fable 5.1**  |     $10.00 |          $0.25 |      $50.00 | Frontier / long-horizon   |
| **Claude Mythos 5.1** |     $10.00 |          $0.25 |      $50.00 | Specialised frontier      |
| **Claude Fable 5**    |     $10.00 |          $1.00 |      $50.00 | Frontier                  |
| **Claude Mythos 5**   |     $10.00 |          $1.00 |      $50.00 | Specialised frontier      |
| **Claude Opus 5**     |      $5.00 |          $0.50 |      $25.00 | Very high capability      |
| **Claude Opus 4.8**   |      $5.00 |          $0.50 |      $25.00 | High capability           |
| **Claude Sonnet 5**   |      $2.00 |          $0.20 |      $10.00 | High capability / agentic |
| **Claude Haiku 4.5**  |      $1.00 |          $0.10 |       $5.00 | Fast / efficient          |

### Claude Fable 5.1

**$10/M input, $50/M output, $0.25/M cached input**

Fable 5.1 is Anthropic's most demanding generally available model for long-horizon agentic work. It has a 1M-token context, 128K maximum output, adaptive reasoning that is always on, a high default effort, and slower latency. Anthropic positions it for demanding reasoning, long-running agents, complex coding, research and large knowledge-work tasks. For most workloads it still tells you to start with Opus 5 and move up when evals fall short. ([Fable 5.1 overview](https://platform.claude.com/docs/en/models/fable-5-1/overview))

The interesting part is not just the $10/$50 headline. Cache reads are **$0.25/M** - 40 times cheaper than uncached input, and a quarter of what Fable 5 charged. Anthropic says that cheaper cache reads reduce typical workload costs by around 25%, and highly agentic workloads by up to about 45%. ([Anthropic](https://www.anthropic.com/claude/fable))

I covered the original [Fable 5 / Mythos 5 split](/ai/claude-fable-5-mythos-5/) when it launched. 5.1 keeps the same headline price and changes the economics of actually using it.

### Claude Mythos 5.1

Same underlying model and pricing as Fable 5.1, available through specialised trusted-access programmes rather than general availability. Anthropic describes it as intended for vetted cyberdefenders and life scientists. For normal software development, Fable is the relevant model. ([Anthropic](https://www.anthropic.com/claude/mythos))

### Claude Opus 5 and Opus 4.8

**$5/M input, $25/M output**

Opus sits below Fable and remains a high-end model for complex coding, research, reasoning and agentic workflows. Anthropic's current docs still position Opus 5 as the model to start with for many demanding workloads.

Opus 4.8 remains available alongside it at the same standard price. Fast mode doubles those rates to **$10/M input and $50/M output** in exchange for substantially lower latency. Anthropic says Fast mode for Opus 4.8 can run at 2.5x the speed. ([Opus 4.8 announcement](https://www.anthropic.com/news/claude-opus-4-8))

That is another pricing dimension worth taking seriously:

> **Sometimes you are not paying for more intelligence. You are paying for less waiting.**

### Claude Sonnet 5

**$2/M input, $10/M output**

Sonnet 5 is arguably one of the most important models in Anthropic's portfolio from an economics perspective. Anthropic describes it as its most agentic Sonnet yet, with strong coding, reasoning, tool use and professional-work capabilities. The $2/$10 rate, originally announced as introductory pricing through 31 August 2026, is now permanent. The scheduled rise to $3/$15 did not happen. ([Anthropic](https://www.anthropic.com/news/claude-sonnet-5))

Typical work: software development, coding agents, debugging, code review, research, document analysis, business automation, tool-using agents. This is the middle ground between expensive frontier models and cheap bulk-processing models.

### Claude Haiku 4.5

**$1/M input, $5/M output**

Haiku 4.5 is designed for speed and cost efficiency. Anthropic describes it as a small model that can deliver near-frontier performance on some workloads while being considerably faster and cheaper than larger models. Typical work: chat, customer-service agents, pair programming, rapid coding, classification, extraction, sub-agents, high-volume processing.

Its economics are particularly interesting for architectures where a larger model plans a task and many smaller agents execute subtasks. ([Haiku 4.5 announcement](https://www.anthropic.com/news/claude-haiku-4-5))

---

## DeepSeek Pricing

DeepSeek takes a noticeably different approach. Its current API exposes two major models. The lower figure in each range is the off-peak price; the higher figure is peak. ([DeepSeek API docs](https://api-docs.deepseek.com/quick_start/pricing))

| Model                   |  Input / 1M | Cached input / 1M | Output / 1M | Positioning           |
| ----------------------- | ----------: | ----------------: | ----------: | --------------------- |
| **DeepSeek V4.1 Flash** | $0.15-$0.30 |     $0.003-$0.006 | $0.60-$1.20 | High-volume / agentic |
| **DeepSeek V4 Pro**     | $0.66-$1.32 |     $0.022-$0.044 | $1.98-$3.96 | High capability       |

Both models support a 1M-token context window, tool calls and thinking mode. V4.1 Flash also supports vision. Maximum output is 384K tokens.

### DeepSeek V4.1 Flash

**Off-peak:** $0.15/M input, $0.003/M cached input, $0.60/M output

**Peak:** $0.30/M input, $0.006/M cached input, $1.20/M output

Peak hours are Monday-Friday, **01:00-04:00 UTC** and **06:00-10:00 UTC**, excluding Chinese public holidays. All other hours are off-peak, including weekends and Chinese public holidays in full.

That is 7 peak hours per weekday and 17 off-peak hours, plus the entire weekend. DeepSeek is effectively saying: if you do not need the computation during the busiest periods, it will charge you less. That is conceptually similar to how traditional cloud infrastructure distinguishes scarce capacity from abundant capacity.

### DeepSeek V4 Pro

**Off-peak:** $0.66/M input, $0.022/M cached input, $1.98/M output

**Peak:** $1.32/M input, $0.044/M cached input, $3.96/M output

When V4.1 Flash launched on 10 September, DeepSeek said it would start routing `deepseek-v4-pro` requests to Flash from 14 September. The same day's changelog then said it would keep serving V4 Pro after user demand, with billing unchanged. As of 20 September it is still listed on the pricing page, so it remains relevant for workloads where its capability profile is preferable to Flash. ([DeepSeek changelog](https://api-docs.deepseek.com/updates))

---

## SpaceXAI Grok Pricing

SpaceXAI's text API is a shorter ladder than OpenAI or Anthropic, with a 200k-token long-context surcharge that doubles rates for the whole request. These are the standard (below 200k) rates. ([SpaceXAI API pricing](https://docs.x.ai/developers/pricing))

| Model              | Input / 1M | Cached input / 1M | Output / 1M | Positioning                 |
| ------------------ | ---------: | ----------------: | ----------: | --------------------------- |
| **Grok 4.6**       |      $2.00 |             $0.50 |       $6.00 | Frontier coding / agents    |
| **Grok 4.5**       |      $2.00 |             $0.30 |       $6.00 | Previous frontier           |
| **Grok 4.3**       |      $1.25 |             $0.20 |       $2.50 | Fast / long context         |
| **Grok Build 0.1** |      $1.00 |             $0.20 |       $2.00 | Fast coding (public beta)   |

Prompts at or above 200k tokens are billed at twice those rates for all tokens in the request, including cache and output. Grok 4.6 and 4.5 have a 500k context window. Grok 4.3 has 1M. Build 0.1 has 256k. Dated `grok-4.20-0309` snapshots are still listed at the same prices as Grok 4.3.

SpaceXAI also sells Priority Processing at **2x** standard rates, a US regional endpoint for Grok 4.6 at a **10%** premium, and a Batch API that is **20%** off - but only for Grok 4.3 and the 4.20 family. Grok 4.6, 4.5 and Build currently have no batch discount. ([SpaceXAI pricing](https://docs.x.ai/developers/pricing))

### Grok 4.6

**$2/M input, $6/M output, $0.50/M cached input**

Grok 4.6 is SpaceXAI's current flagship, with a 500k context, no text output limit, and reasoning effort from low through to `xhigh`. The company describes it as a frontier model for coding, agentic tasks and knowledge work, with a particular focus on long-running agents. A fast variant is twice the price. ([Grok 4.6 docs](https://docs.x.ai/developers/grok-4-6), [announcement](https://x.ai/news/grok-4-6))

The price is the story. SpaceXAI says Grok 4.6 matches [GPT-5.6 Sol](https://openai.com/index/gpt-5-6/) on the Artificial Analysis Intelligence Index, a composite of nine benchmarks. Sol is **$4/$20**. Grok 4.6 is **$2/$6**. Same claimed intelligence-index score, a third of the output price. Treat that as SpaceXAI's published comparison, not an independent audit - but even if you only believe half of it, the list price still sits with Sonnet and Terra, not with Astra and Fable.

Cached input is only **4x** cheaper than fresh input. That is a much weaker cache discount than Fable 5.1's 40x. SpaceXAI is competing on output price, not on making repeated context almost free.

### Grok 4.5

**$2/M input, $6/M output, $0.30/M cached input**

Same headline rates as 4.6, cheaper cache. Still listed and still relevant if you already have prompts tuned to it, or if the extra cache discount matters more than 4.6's capability delta. Cursor bills Grok 4.5 cache reads at $0.50/M rather than $0.30/M, so the API and the IDE are not identical invoices.

### Grok 4.3

**$1.25/M input, $2.50/M output**

Grok 4.3 is the 1M-context model, with configurable reasoning including a `none` setting for maximum speed. SpaceXAI's docs call it fast and reliable, with strong tool calling and instruction following. It is also one of the few Grok models that gets the 20% batch discount. At $2.50 output it sits next to Composer 2.5 and well below Haiku.

### Grok Build 0.1

**$1/M input, $2/M output**

Build 0.1 is SpaceXAI's fast coding model, in public beta on the API, and the same model that powers the Grok Build agent. The company says it is trained for agentic coding - web development, debugging, MCP - served at 100+ tokens per second. It also positions it as a cheap general-purpose tool-calling option outside coding. Context is 256k, so it is not the long-repo model. ([Grok Build 0.1](https://x.ai/news/grok-build-0-1))

---

## Cursor Pricing

Most of the prices above are what you pay if you call a lab's API yourself. A large share of coding-agent tokens never take that path. They run inside [Cursor](https://cursor.com/docs/models-and-pricing), which sits on top of those APIs and adds its own models.

Cursor splits usage into two pools that reset with the billing cycle:

- **Cursor Models:** Grok 4.6, Grok 4.5, and Composer 2.5. Significantly more included usage.
- **Other Models:** third-party models, charged at that model's public API price. Pro, Pro Plus and Ultra include this pool. The India-only Start plan does not.

On-demand usage after the included amount is billed at the same token rates. Requests are not silently downgraded. ([Cursor models and pricing](https://cursor.com/docs/models-and-pricing))

| Plan        | Price              | Cursor Models | Other Models |
| ----------- | -----------------: | ------------- | ------------ |
| **Start**   | ₹649/mo (India)    | Included      | Not included |
| **Pro**     |            $20/mo  | Included      | Included     |
| **Pro Plus**|            $60/mo  | Included      | Included     |
| **Ultra**   |           $200/mo  | Included      | Included     |
| **Teams**   | $40 or $120/user   | Included      | Included     |

Cursor's own usage guide says daily Tab users and limited Agent users often stay inside the included pool; **daily Agent users typically land at $60 - $100 a month** all-in; power users running multiple agents or automation often hit **$200+**. That is the number that should sit next to the $20 headline, not instead of the token tables - the token tables explain why the $20 plan runs out.

On Teams and Enterprise, third-party model requests also pick up a **Cursor Token Rate of $0.25 per million tokens**, on top of the underlying API price, including BYOK. First-party Cursor models - Grok and Composer - are exempt.

### Composer 2.5

**Standard:** $0.50/M input, $0.20/M cached input, $2.50/M output

**Fast:** $3.00/M input, $0.50/M cached input, $15.00/M output

Composer 2.5 is Cursor's in-house agentic coding model. Fast is the default in the product. I covered the [2.5 release](/ai/cursor-composer-2-5/) in May; the list price has not moved. Cursor says Fast is cheaper than the fast tiers of other frontier models at similar speeds. That may be true against Opus Fast or Astra Fast. It is not cheap compared with leaving Fast off: the default is **6x** the standard input and output rate.

That is another version of paying for less waiting. Leave Fast on for interactive sessions. Turn it off for overnight agents, evals, and anything that can wait.

### Cursor Grok 4.6 and 4.5

Cursor lists Grok 4.6 at the same **$2/$0.50/$6** as the SpaceXAI API, and Grok 4.6 Fast at **$4/$1/$12**. Both rows are marked as jointly trained by Cursor and SpaceXAI. Grok 4.6 received supplemental training on anonymised Cursor workflow data, and Cursor bills it from the Cursor Models pool rather than as a third-party Other Model. ([Cursor pricing](https://cursor.com/docs/models-and-pricing), [Grok 4.6 model card](https://media.x.ai/v1/website/card-4p6-4cd2dc57.pdf))

The practical effect: if you live in Cursor, routing daily agent work to Composer or Grok burns the cheaper, larger pool. Routing it to Fable or Astra burns the Other Models pool at $10/$50. That is a first-order cost decision, not a preference about chat personality.

---

## Putting the Prices Side by Side

The difference becomes much clearer when you compare output pricing.

| Model                          | Output / 1M |
| ------------------------------ | ----------: |
| Claude Fable 5.1               |  **$50.00** |
| Claude Mythos 5.1              |  **$50.00** |
| GPT-6 Astra                    |  **$50.00** |
| Claude Fable 5                 |  **$50.00** |
| Claude Opus 5                  |  **$25.00** |
| Claude Opus 4.8                |  **$25.00** |
| GPT-5.6 Sol                    |  **$20.00** |
| Composer 2.5 Fast              |  **$15.00** |
| GPT-5.6 Terra                  |  **$12.00** |
| Grok 4.6 - long context        |  **$12.00** |
| Claude Sonnet 5                |  **$10.00** |
| Grok 4.6                       |   **$6.00** |
| Claude Haiku 4.5               |   **$5.00** |
| DeepSeek V4 Pro - peak         |   **$3.96** |
| Composer 2.5                   |   **$2.50** |
| Grok 4.3                       |   **$2.50** |
| Grok Build 0.1                 |   **$2.00** |
| DeepSeek V4 Pro - off-peak     |   **$1.98** |
| GPT-5.6 Luna                   |   **$1.20** |
| DeepSeek V4.1 Flash - peak     |   **$1.20** |
| DeepSeek V4.1 Flash - off-peak |   **$0.60** |

The spread is extraordinary. The difference between **$50/M** and **$0.60/M** is more than **80x**.

That does not mean the $0.60 model is 80 times less capable. It means the economics of inference are increasingly disconnected from simple model-size comparisons.

---

## Why Is DeepSeek So Cheap?

There is not a single reason. The price reflects architecture, inference efficiency, hardware utilisation, batching, serving strategy, caching, competition, and demand management.

DeepSeek is unusually explicit about the architecture behind the price. It describes V4.1 Flash as a 552-billion-parameter mixture-of-experts model with a causal encoder-decoder that activates 8 billion parameters for input and 16 billion for output, plus a much smaller KV cache - a quarter of the previous generation's HBM requirement, and an eighth of the SSD storage. Cache-hit charges, it notes, often account for a large share of agent costs. ([DeepSeek](https://api-docs.deepseek.com/news/news260910))

The important lesson is:

> **Model capability and inference cost are not the same thing.**

A more expensive model can be more capable, but the cost difference may be much larger than the capability difference for a particular workload.

---

## Cached Input Changes Everything

One of the easiest mistakes when comparing model prices is to look only at the standard input rate.

Agentic systems frequently reuse enormous amounts of context. Every request might contain system instructions, tool definitions, project documentation, repository context, previous decisions, coding standards, files, and conversation history. If all of that is sent as fresh input every time, the bill becomes significant. If the provider supports [prompt caching](/ai/prompt-caching/), repeated context becomes dramatically cheaper.

Fable 5.1: normal input **$10/M**, cached input **$0.25/M**. That is a **40x** difference.

DeepSeek V4.1 Flash: normal off-peak input **$0.15/M**, cached off-peak input **$0.003/M**. That is **50x** cheaper.

Grok 4.6: normal input **$2/M**, cached input **$0.50/M**. That is only **4x** cheaper. Composer 2.5 is **2.5x** ($0.50 down to $0.20). Cheap output does not automatically mean cheap cache.

Caching is not a minor optimisation for agents. It can fundamentally change the economics of an application. I have written about the [token-efficiency mindset](/ai/claude-token-efficiency-mindset/) before; the 2026 price tables make that argument sharper, not weaker.

---

## Batch Processing Is Another Major Discount

Anthropic offers a 50% discount on input and output tokens through its Batch API. Fable 5.1 becomes approximately **$5/M input and $25/M output**. OpenAI does the same thing with Batch and Flex processing. SpaceXAI's Batch API is only **20%** off, and only for Grok 4.3 and the dated 4.20 snapshots - Grok 4.6 does not get it.

This matters for work that does not need an immediate response: overnight analysis, document processing, evaluation runs, dataset classification, bulk summarisation, large-scale code analysis.

The lesson is similar to DeepSeek's off-peak pricing:

> **Latency has a price.**

If you do not need an answer immediately, do not pay for infrastructure optimised for immediate answers.

---

## Peak Versus Off-Peak AI

Traditional cloud computing has long differentiated between on-demand, reserved, spot, batch and autoscaling. AI inference is starting to develop similar economics.

For DeepSeek V4.1 Flash:

| Period       | Time                                      |
| ------------ | ----------------------------------------- |
| **Peak**     | Mon-Fri 01:00-04:00 UTC                   |
| **Peak**     | Mon-Fri 06:00-10:00 UTC                   |
| **Off-peak** | All other times, including Chinese holidays |

An automated system can deliberately schedule non-urgent work outside those windows.

**Peak:** interactive coding, human-in-the-loop requests, urgent agent tasks.

**Off-peak:** repository analysis, test generation, documentation, bulk classification, data processing, background maintenance.

That is capacity-aware AI orchestration. It is the same instinct as [running bulk work on GPUs and reserving APIs for the hard cases](/ai/gpu-servers-vs-api-credits/), just applied to someone else's fleet.

---

## The Cost of an AI Coding Agent

Token pricing becomes much more important when an agent starts doing real work.

Take a hypothetical agent that consumes **10M input tokens** and generates **20M output tokens**. Approximate standard-processing cost, with no caching and no batch discount:

| Model                          | 10M input + 20M output |
| ------------------------------ | ---------------------: |
| GPT-6 Astra                    |             **$1,100** |
| Claude Fable 5.1               |             **$1,100** |
| Claude Opus 5                  |               **$550** |
| GPT-5.6 Sol                    |               **$440** |
| Composer 2.5 Fast              |               **$330** |
| GPT-5.6 Terra                  |               **$260** |
| Claude Sonnet 5                |               **$220** |
| Grok 4.6                       |               **$140** |
| Claude Haiku 4.5               |               **$110** |
| DeepSeek V4 Pro - peak         |             **$92.40** |
| Grok 4.3                       |              **$62.50** |
| Composer 2.5                   |                **$55** |
| Grok Build 0.1                 |                **$50** |
| DeepSeek V4 Pro - off-peak     |             **$46.20** |
| GPT-5.6 Luna                   |                **$26** |
| DeepSeek V4.1 Flash - peak     |                **$27** |
| DeepSeek V4.1 Flash - off-peak |             **$13.50** |

These are illustrative calculations using published token rates, not measurements of actual agent workloads. Real agents will cache a large share of that input, retry failures, and burn extra tokens on tool calls.

Even so, the headline is startling. Astra/Fable versus off-peak Flash is roughly **$1,100 vs $13.50**. Grok 4.6 lands at **$140**. Composer 2.5 lands at **$55** - or **$330** if you leave Fast on.

---

## The Cheapest Model Is Not Automatically the Cheapest Solution

This is the most important qualification.

Suppose a cheap model completes a task successfully 70% of the time, and a more expensive model succeeds 90% of the time. If failed tasks require retries, additional model calls, validation, debugging, or human intervention, the cheap model's apparent advantage can disappear.

The real metric is not cost per million tokens. It is **cost per successful task**. And ultimately, **cost per useful outcome**.

A simple classification task does not need frontier reasoning:

```text
Is this support ticket:
A) billing
B) technical
C) account
D) other
```

There is little reason to use a $50/M output model. A cheap, fast model is appropriate.

Now consider:

```text
Analyse this 800,000-line
distributed data platform.

Identify architectural weaknesses,
security risks, scalability problems,
and propose a migration strategy.
```

That is a completely different workload. The cost of the model is probably insignificant compared with the engineering time involved. This is why model selection needs to be task-aware.

---

## A Practical Capability Matrix

| Workload               | Model class                    | Examples                             |
| ---------------------- | ------------------------------ | ------------------------------------ |
| Frontier reasoning     | Fable / Astra / Sol / Grok 4.6 | Complex architecture, research       |
| Advanced coding        | Opus / Sol / Fable / Grok 4.6  | Large refactors, difficult debugging |
| Agent planning         | Fable / Opus / Sol / Grok 4.6  | Multi-step autonomous tasks          |
| General coding         | Sonnet / Terra / V4 Pro / Composer | Implementation, code review      |
| Routine coding         | Haiku / Luna / Flash / Build   | Tests, boilerplate, documentation    |
| Bulk processing        | Luna / Flash / Haiku           | Classification, extraction           |
| High-volume agents     | Luna / Flash / Composer        | Background automation                |
| Long-context analysis  | Astra / Fable / Sonnet / Grok 4.3 | Large documents and repositories  |
| Interactive assistants | Sonnet / Haiku / Luna / Composer Fast | Chat and productivity           |
| Batch workloads        | Any appropriate tier           | Large-scale offline processing       |

The key word is **appropriate**.

---

## Think Expensive. Execute Cheaply.

The most economically interesting architecture is not choosing one model. It is choosing different models for different stages of the same task.

```text
                    TASK
                      │
                      ▼
             ┌─────────────────┐
             │ Frontier model  │
             │ Analyse, plan,  │
             │ architecture    │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Mid-tier model  │
             │ Implement,      │
             │ refactor, debug │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Cheap model     │
             │ Tests, docs,    │
             │ classification  │
             └────────┬────────┘
                      │
                      ▼
                 VALIDATION
```

**Think.** Use a frontier model for architecture, difficult reasoning, research, planning, and complex debugging.

**Build.** Use a strong mid-tier model for implementation, refactoring, code review, and normal debugging.

**Repeat.** Use inexpensive models for tests, documentation, extraction, classification, and repetitive transformations.

**Validate.** Use another model or deterministic tooling for tests, linting, type checking, security scanning, and infrastructure validation.

This is much more efficient than blindly routing every request to the most capable model available. It is the same hybrid instinct as [local versus cloud](/ai/local-vs-cloud-ai-2026/), applied inside a single cloud workflow.

---

## The Economics of Agentic Software

Traditional AI applications look like: user, prompt, model, answer.

Agents look more like: task, model, tool call, result, model, tool call, result, model, code, tests, failure, model, fix, tests, success.

One user request can produce dozens or hundreds of model interactions. That makes token economics much more important. A difference of a few dollars per million tokens becomes thousands of dollars when multiplied across an autonomous system operating continuously.

And token prices are only one component of the total cost. A production AI system can also incur tool calls, search, computer use, vector databases, storage, network traffic, observability, orchestration, retries, evaluation, and human review. The model may actually be the cheapest part of some systems. Measure **cost per completed workflow**, not just API prices.

This is also why [subscription pricing built for chat](/ai/twenty-dollar-ai-era-is-over/) keeps colliding with agent usage. The $20 plan was never designed for a loop that burns 20 million output tokens. Cursor's published usage bands make that concrete: a daily agent user is already a $60 - $100 month, and the power-user band starts at $200. The subscription is the entry ticket. The token tables are the bill.

---

## The Price-Performance Frontier Is Moving Quickly

The most significant trend is not simply that models are getting smarter. They are getting cheaper at the same time - at least below the frontier.

OpenAI has repeatedly reduced prices for its efficient GPT models. Anthropic has made Sonnet 5's $2/$10 pricing permanent and dramatically reduced Fable 5.1 cache-read costs. DeepSeek has introduced extremely low token prices and variable peak/off-peak rates. SpaceXAI is selling Grok 4.6 at $2/$6 against Sol's $4/$20. Cursor is selling Composer 2.5 at $0.50/$2.50, with Fast as the default for people who would rather pay than wait.

Yesterday's expensive frontier model can become tomorrow's mid-tier model. Yesterday's mid-tier model can become tomorrow's background automation engine. Intelligence is still something [you buy by the token](/ai/we-are-learning-to-buy-intelligence/). The catalogue just has a much wider set of prices.

---

## What This Means for Developers

When inference costs were high, it made sense to carefully ration model usage. As capable models become cheaper, it becomes economically viable to have agents continuously review pull requests, generate tests, analyse logs, check Terraform, review SQL, monitor infrastructure, update documentation, scan dependencies, analyse incidents, and maintain repositories.

The limiting factor increasingly becomes **what useful work we can give the agents**, rather than **whether we can afford to run the model**.

I would reduce the whole subject to three rules.

**1. Start with the cheapest model that can reliably do the job.** Do not start with the most expensive model. Start with the workload. Determine the minimum capability required. Then test upward if necessary.

**2. Measure successful outcomes, not tokens.** A model costing $1 per task is not cheaper if it requires three retries and 20 minutes of human intervention. Measure cost per successful task.

**3. Exploit caching and batch/off-peak processing.** If your workload repeatedly sends the same context, use caching. If it does not need an immediate answer, use batch processing where available. If your provider has peak/off-peak pricing, schedule background work accordingly. These optimisations can produce larger savings than switching between otherwise similar models.

---

## The Future Is Not One Model

The AI industry is beginning to look increasingly like the cloud infrastructure industry. We now have different dimensions of compute: capability, latency, throughput, caching, context size, availability, batch processing, geography, and price.

The idea that everyone will eventually use one universally superior AI model is becoming less convincing. The emerging architecture looks more like a distributed computing stack.

A frontier model might reason about a problem. A mid-tier model might implement the solution. A cheap model might generate tests. Another model might review the result. Deterministic tools might validate it. An orchestrator might decide which model to use at every stage.

The winning architecture is not necessarily the one with the smartest model. It may be the one that uses **the right amount of intelligence at each step**.

---

## Conclusion

Cloud AI has entered an interesting phase.

At the top end, models such as GPT-6 Astra and Claude Fable 5.1 cost around **$50 per million output tokens**.

In the middle, Grok 4.6 costs **$6**, and Composer 2.5 costs **$2.50**.

At the other end, DeepSeek V4.1 Flash can produce a million output tokens for **$0.60 off-peak**, while GPT-5.6 Luna costs **$1.20**.

That is an enormous economic range. But price alone is not the answer.

The real optimisation is capability, reliability, latency, token consumption, caching, and orchestration, multiplied together.

The best AI architecture is therefore not "use the smartest model everywhere."

It is: **use expensive intelligence where it matters, cheap intelligence where it does not, and automate the routing between them.**

For developers building AI agents in 2026, understanding that economics may be almost as important as understanding the models themselves.

## Sources

- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [GPT-6 Astra model page](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [GPT-5.6 announcement](https://openai.com/index/gpt-5-6/)
- [Advancing the price-performance frontier with GPT-5.6](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/)
- [Claude Platform pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Claude Fable 5.1 overview](https://platform.claude.com/docs/en/models/fable-5-1/overview)
- [Claude Fable product page](https://www.anthropic.com/claude/fable)
- [Claude Mythos product page](https://www.anthropic.com/claude/mythos)
- [Introducing Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)
- [Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)
- [Introducing Claude Haiku 4.5](https://www.anthropic.com/news/claude-haiku-4-5)
- [DeepSeek models and pricing](https://api-docs.deepseek.com/quick_start/pricing)
- [DeepSeek V4.1 Flash announcement](https://api-docs.deepseek.com/news/news260910)
- [DeepSeek API changelog](https://api-docs.deepseek.com/updates)
- [SpaceXAI API pricing](https://docs.x.ai/developers/pricing)
- [Grok 4.6 docs](https://docs.x.ai/developers/grok-4-6)
- [Introducing Grok 4.6](https://x.ai/news/grok-4-6)
- [Grok 4.6 model card](https://media.x.ai/v1/website/card-4p6-4cd2dc57.pdf)
- [Grok 4.3 docs](https://docs.x.ai/developers/models/grok-4.3)
- [Grok Build 0.1 on API](https://x.ai/news/grok-build-0-1)
- [Cursor models and pricing](https://cursor.com/docs/models-and-pricing)
- [Composer 2.5 docs](https://cursor.com/docs/models/cursor-composer-2-5)
- [Introducing Composer 2.5](https://cursor.com/blog/composer-2-5)

## Related Reading

- [Token Economics: Why the Cost of AI Isn't Going Down](/ai/token-economics-why-costs-arent-going-down/)
- [Prompt Caching: The Quiet Performance Win for LLM Applications](/ai/prompt-caching/)
- [The Token Efficiency Mindset](/ai/claude-token-efficiency-mindset/)
- [Is the $20 AI Subscription Era Over?](/ai/twenty-dollar-ai-era-is-over/)
- [We Are Learning to Buy Intelligence](/ai/we-are-learning-to-buy-intelligence/)
- [GPU Servers vs AI API Credits](/ai/gpu-servers-vs-api-credits/)
- [Local AI vs Cloud AI in 2026](/ai/local-vs-cloud-ai-2026/)
- [Claude Fable 5 and Mythos 5](/ai/claude-fable-5-mythos-5/)
- [DeepSeek](/ai/deepseek/)
- [Composer 2.5: Cursor's In-House Model Grows Up](/ai/cursor-composer-2-5/)
- [Cursor AI](/ai/cursor-ai/)
- [SpaceX's $60 Billion Cursor Acquisition](/ai/spacex-cursor-acquisition/)
