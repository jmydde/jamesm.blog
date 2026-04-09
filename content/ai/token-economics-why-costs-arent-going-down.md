---
title: "Token Economics: Why the Cost of AI Isn't Going Down"
date: 2026-04-09T06:40:00+01:00
draft: false
tags: ['ai', 'economics', 'infrastructure']
description: "Despite massive scale and competition, LLM pricing hasn't meaningfully declined. Here's why the fundamentals don't support cheaper AI."
---

There's a persistent myth in tech: AI will get cheaper. The argument is straightforward - Moore's Law, scale effects, competition, and raw compute efficiency improvements mean costs should plummet. Yet in April 2026, Claude costs roughly what it did in 2024. GPT-4 Turbo pricing hasn't moved in eighteen months. Gemini's cost structure remains sticky. Why?

The answer isn't that progress hasn't happened. It's that the economics of modern AI are fundamentally different from hardware commoditization. Once you understand the actual constraints, the stability of pricing becomes logical.

---

## The Hardware Myth vs. The Actual Problem

The comparison to Moore's Law breaks down immediately. Moore's Law was about transistor density on silicon - a manufacturing problem solved by shrinking features. Costs fell because you could print more compute on the same wafer.

LLMs aren't a manufacturing problem anymore. They're a **demand problem** meeting **fixed fundamental costs**.

Consider what you're actually paying for:

1. **Training compute** - a one-time cost amortized across all users
2. **Inference compute** - real-time, per-token cost that never goes away
3. **Memory and bandwidth** - to serve billions of tokens per day
4. **Talent** - researchers, infrastructure engineers, security teams

The training cost is large but sunk - it doesn't increase with usage. The problem is everything else.

---

## The Inference Wall

Here's the brutal fact: inference cost is **architectural**, not accidental.

To generate a token, you must:

1. Load the entire model into memory (or multiple copies for parallelism)
2. Run a forward pass through every layer
3. Compute attention over the full context
4. Write the output token

A 70B parameter model like Llama 2 requires roughly 140GB of VRAM in bfloat16 (2 bytes per parameter). To serve 1,000 concurrent users at reasonable latency, you need multiple copies - easily 5-10 copies minimum for queue absorption. That's 700GB - 1.4TB of GPU memory just to exist. A single H100 has 80GB, so you're looking at 9-18 H100s per 1,000 concurrent users.

An H100 costs ~$40,000. An entire GPU cluster serving 100,000 concurrent users costs tens of millions of dollars, and that's just hardware. Add power, cooling, redundancy, network, security, and you're in the hundred-millions range for a production system.

Each token an H100 generates costs roughly $0.00001-0.00002 in raw GPU amortization. But:

- H100s last 3-4 years before replacement
- Power costs add 30-50%
- Datacenter costs add another 30-40%
- You're not using that capacity 24/7

The actual cost per token is closer to **$0.00005-0.0001** once you include everything. At that floor, a 1,000-token request costs a provider $0.05-0.10 to deliver. They're charging $0.003-0.01 per token. The margins exist, but they're not spectacular, and they don't compress further.

---

## Why Costs Can't Fall Much Lower

**Competition is already present.** Mistral charges less than Claude because they're running inference on cheaper H100s in regions with cheaper power. But that's a 20-30% spread at most - you can't price your way out of physics.

**Scaling helps inference latency, not cost per token.** Bigger models require more compute to run. A 405B parameter model (like GPT-4 in rumored specifications) requires 5x the memory and compute of a 70B model. Splitting it across multiple chips adds communication overhead. You get better quality tokens, but each one is more expensive to produce.

**Mixture of Experts and sparse models don't solve this.** MoE models activate only some parameters per token, which reduces theoretical compute. But in practice, you still load the entire model into memory, and the hardware doesn't offer proportional benefits. Sparse models work on paper; in production, they're slightly cheaper, not orders of magnitude cheaper.

**Smaller models hit quality walls.** You can run a 7B model on a single GPU. It's cheap. It's also noticeably worse than Claude 3.7 or GPT-4. Enterprise customers pay for quality. The market has clearly chosen: "good enough cheap AI" doesn't compete with "actually useful AI at the current price."

---

## The Demand-Side Economics

Even if inference costs somehow fell 50%, you wouldn't see price drops. Here's why:

**Demand is elastic upward.** As prices fall, usage increases. A company paying $10,000/month for Claude increases usage by 3-5x if prices drop to $5,000/month. Providers don't see a revenue decline - they see increased cost pressure as usage skyrockets. To maintain margins, they keep prices stable.

**Willingness to pay is high.** A developer making $150k/year is happy to spend $20/month for an AI that saves 2 hours per week. A company automating a support team would pay $100,000/month if it genuinely works. The current prices are nowhere near the ceiling of what customers will bear.

**Competition doesn't drive down prices.** Anthropic, OpenAI, Google, and Meta have all released models in the last 18 months. Have prices fallen? No. Why would they undercut each other if they can all make $1B+ in ARR at current pricing? Price wars happen in commodities with interchangeable products. LLMs aren't interchangeable - Claude and GPT-4 have different strengths, and customers choose based on quality and integrations, not cost.

**Open-source didn't kill commercial models.** Llama, Mistral, and other open models are freely available. Yet commercial LLM revenue is growing, not shrinking. Open models serve a different segment (developers who can self-host, cost-sensitive companies). They don't cannibalize commercial pricing - they coexist.

---

## Where Costs Are Actually Changing

**Down (but slowly):**
- Small inference models (4B, 7B parameter) have genuinely fallen from $0.01/million tokens to $0.001/million tokens
- Batch inference pricing has dropped as providers optimize for non-realtime workloads
- Regional pricing varies (Southeast Asia cheaper than US) as providers optimize locations

**Up:**
- Context windows have expanded 10-100x (from 4K to 200K), making tokens more expensive to compute
- Premium tiers (like Claude 3.7 with vision and long-context) command 10-20x standard pricing
- Training costs for frontier models have increased - GPT-4 training likely cost $50M+, which compounds inference prices

**Stable:**
- Core inference costs for flagship models (Claude 3, GPT-4) have remained flat for 18+ months
- This is actually where profit margins live - the mature, high-volume tier

---

## The Real Cost You're Not Seeing

There's a hidden cost that matters more than token price: **cost of ownership**.

A company running AI systems pays for:
- API spend (what you see)
- Monitoring and observability (5-10% overhead)
- Error handling and retries (15-30% overhead - failed requests cost money)
- Fine-tuning and optimization (10-50% of base cost)
- Switching cost if you need to migrate models
- Security and compliance (another 10-20% for regulated industries)

The all-in cost of using an AI system is **1.5-2.5x the raw token cost.** Providers understand this. They price accordingly.

---

## What This Means for 2026 and Beyond

**Token prices won't fall dramatically.** You'll see:
- 5-15% annual price reductions for mature models (standard inflation adjustment)
- Bigger drops (30-50%) for older, deprecated models (GPT-3.5 already dropped)
- New models launching at 20-50% premium, then slowly converging to standard pricing
- Tiering becomes more sophisticated (e.g., faster inference costs more)

**Efficiency gains flow to customers, not to prices.** Instead of prices dropping, providers spend efficiency gains on:
- Longer context windows (more valuable features)
- Faster inference (better user experience)
- Better reasoning (higher quality outputs)
- Multimodal capabilities (expanding use cases)

You're getting more value per dollar, but the dollar amount itself stabilizes.

**Open-source will remain cheaper but second-tier.** Running your own Llama or Mistral is literally free at inference time (you pay for hardware and power). But it's only economical if:
- You have 10,000+ tokens of daily usage (break-even point)
- You can tolerate slightly lower quality
- You have infrastructure expertise

For everyone else, paying the stable cloud price is rational.

---

## The Supply Constraint

The fundamental constraint isn't software or algorithms - it's **GPU supply and electrical power**.

We'll build more datacenters. We'll buy more H100s (and H200s, and future GPUs). But these grow linearly. The cost of electricity doesn't drop. The cost of land and cooling doesn't drop. The training compute needed to produce frontier models keeps increasing.

Until we see a breakthrough in quantum computing, neuromorphic hardware, or optical compute that actually delivers on its promises, we're stuck with incremental improvements to existing architectures.

And even if one of those breakthroughs happens, the vendors who own it (Anthropic, OpenAI, or whoever) will simply pocket the margin improvement. They won't undercut each other.

---

## What Should Change Your Behavior

1. **Stop waiting for cheaper AI.** Integrate it into your systems now at current pricing. The economics work.

2. **Optimize for quality, not token count.** Paying 3x for better outputs that require fewer retries is cheaper overall.

3. **Build on stable providers.** OpenAI and Anthropic aren't going anywhere. Their pricing is stable. Betting on future price cuts is a bad prediction.

4. **Use open models for scale-insensitive work.** If you're fine with 15% quality reduction, self-hosting Mistral saves you money at high volume.

5. **Plan for static costs.** Budget as if token prices stay flat. Any improvement is upside.

The era of "wait for AI to get cheaper" is over. You should be in "AI costs are fixed infrastructure spend" mode. Price in at today's rate, optimize usage, and move forward.

The fundamentals don't support cheap AI anytime soon. Understand that, and you'll make better decisions about when and where to deploy it.
