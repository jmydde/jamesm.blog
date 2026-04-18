---
title: "Running Qwen3.6-35B-A3B on Mac Studio: What Actually Works"
date: 2026-04-18T14:00:00+01:00
draft: false
tags: ["ai", "apple-silicon", "llm", "qwen", "mac-studio", "inference", "local-llm"]
description: "A practical breakdown of which Mac Studio configuration actually runs Qwen3.6-35B-A3B well, realistic performance expectations, and whether it's worth the investment versus alternatives."
---

You want to run Qwen3.6-35B-A3B locally on a Mac Studio. Good idea—unified memory is genuinely useful for LLMs. But the specs matter more than you might think, and there are some hard truths about what "works" versus what feels responsive.

## What the model actually needs

The trap most people fall into: Qwen3.6-35B-A3B is a mixture-of-experts model with roughly 3B active parameters. That sounds small. It isn't.

Even though only ~3B parameters activate per token, the full 35B weight matrix lives in memory. Always.

Here's what memory you need depending on quantisation:

- **Q4 quantisation**: ~19–22 GB
- **Q5 quantisation**: ~24–28 GB
- **Q8 quantisation**: ~36 GB
- **FP16 (full precision)**: ~70 GB

Then add overhead: KV cache (the stored context attention weights) adds another 0.5–4 GB depending on your context window length.

Realistic minimum for decent quality: **24–28 GB usable memory** with Q4 quantisation and 4K–8K context.

## The Apple Silicon advantage and its limits

Mac Studio sits in an interesting middle ground.

**What's good:**
- Unified memory architecture (GPU and CPU share the same pool)
- No VRAM bottleneck
- Memory bandwidth is genuinely strong (800+ GB/s on Ultra variants)

**What's limiting:**
- Not CUDA—you're stuck with Metal backend or custom implementations
- Raw compute is lower than high-end GPUs
- Generation speed is memory-bound, and that bandwidth matters more than raw TFLOPs

This means Mac Studio doesn't compete with a gaming GPU rig on tokens/second, but it punches above its weight on simplicity and price per GB of usable memory.

## The configs that actually work

Let me cut through the marketing and give you the real picture.

### M2 Max (32–64 GB)

**Can it run Qwen 35B?**
Technically yes. In practice, not well.

- Q2–Q3 quantisation only
- ~8–15 tokens/second
- Frequent memory pressure
- Feels laggy

**Verdict:** Skip for this model. Great for 7B–13B, frustrating for 35B.

### M2 Ultra (64–128 GB)

**This is the sweet spot.**

- M2 Ultra specs: 20 cores CPU, 16 cores GPU, ~800 GB/s bandwidth
- With 64 GB RAM: Q4 Qwen 35B runs at ~15–22 tok/s
- With 128 GB RAM: ~18–25 tok/s, much smoother under pressure

This is where you actually hit your target of "feels responsive for interactive use."

Cost: £3,000–£5,500 new; ~£2,400–£3,200 refurbished.

**When you'd buy this:** You want to run the model reasonably well without overspending. Good refurbished market for this generation.

### M3 Ultra (96–256 GB)

**The no-compromises choice.**

- Newer GPU architecture
- Same bandwidth as M2 Ultra, but better utilisation
- 20–30 tok/s on Qwen 35B (Q4)
- Huge RAM ceiling (up to 256 GB)

Cost: £4,200–£7,500+.

**When you'd buy this:** You're serious about local AI as a workstation. You want to run multiple models, or handle longer contexts (32K+), or don't want to think about memory constraints.

### M4 Max (36–128 GB)

**The confusion card.**

M4 Max is newer, yes. But it has a critical weakness: memory bandwidth of only 410–546 GB/s versus 800+ on the Ultra variants.

For Qwen 35B:
- 36 GB / 64 GB configs: ~10–18 tok/s (barely viable, inconsistent)
- 128 GB config: ~15–22 tok/s (only version worth considering)

**Verdict:** Only works if you max out to 128 GB, at which point you're paying nearly as much as an M2 Ultra. Not recommended for this workload.

## Realistic performance expectations

If you actually buy one of these, what will generation feel like?

**Token speed thresholds:**
- 8–12 tok/s: noticeably laggy, typing pauses
- 15–18 tok/s: acceptable, feels responsive enough
- 20–25 tok/s: very good, near-ChatGPT-like
- 30+ tok/s: excellent, zero perceptible lag

**Context window penalty:**
Your context length matters a lot. Longer contexts = larger KV cache = slower generation.

- 4K context: baseline
- 16K context: -10–25% speed
- 32K context: -25–40% speed
- 100K+: can halve throughput

So "20 tok/s at 4K context" becomes "maybe 12 tok/s at 32K context" on the same hardware.

## Which Mac should you actually buy?

**If you want the best value:**
**M2 Ultra with 64 GB minimum**

- ~£3,000 new or £2,400 refurbished
- Hits ~18–22 tok/s on Qwen 35B (Q4)
- Solid headroom with 64 GB
- Large refurbished market (these machines age gracefully)

**If you don't want to think about limits:**
**M2 Ultra or M3 Ultra with 128 GB**

- M2 Ultra: ~£4,000–£5,000
- M3 Ultra: ~£5,000–£6,500
- Both provide comfortable performance and room to breathe
- Can experiment with larger context windows

**If you want the latest:**
**M3 Ultra with 128 GB**

- £5,000–£6,500
- Best sustained performance (20–30 tok/s)
- Newest GPU architecture means better efficiency over time
- Better for concurrent sessions

## The honest comparison

For £3,000–£4,000, you're in a decision point:

| Setup | Cost | Qwen 35B tok/s | Headroom | Vibes |
|-------|------|----------------|----------|-------|
| M4 Max 128 GB | £3.5k | 15–22 | tight | on-edge |
| M2 Ultra 64 GB | £3.0k | 18–25 | good | solid |
| M2 Ultra 128 GB | £4.5k | 18–25 | excellent | comfortable |
| M3 Ultra 128 GB | £5.5k | 20–30 | massive | production-grade |

**My recommendation:** M2 Ultra with 64 GB. You're not paying for the latest and greatest, but you get genuine performance, strong refurbished availability, and it's the point where the experience stops feeling compromised.

## The context window trap

One thing people overlook: Qwen supports 262K context, but that doesn't mean you should use it locally.

On a Mac:
- 4K context: 20 tok/s baseline ✓
- 32K context: 12–15 tok/s (still good)
- 100K context: 8–10 tok/s (barely acceptable)
- 262K context: approach this only on M3 Ultra with 256 GB

Most practical use (code assistance, research chat): 4K–16K is your happy place. You get speed without sacrificing useful context.

## Alternative: GPU rigs aren't cheaper

Since you're spending £3k–£5k anyway, you should know: a comparable GPU setup isn't obviously better.

A single RTX 4090:
- £1,800–£2,200
- 24 GB VRAM
- 40–70 tok/s on Qwen 35B
- But: CUDA setup overhead, electricity cost, cooling

**RTX 4090 vs M2 Ultra 64 GB:**
- RTX is 2–3× faster
- Mac is simpler, cheaper running costs, unified memory
- You're paying for convenience more than performance

Both are legitimate choices. Mac Studio is the right call if you value simplicity.

## Bottom line

Run the numbers for your actual use case:

- **Interactive solo use** (chat, code): M2 Ultra 64 GB is enough
- **Serious local workstation** (experiments, fine-tuning, concurrency): M2 Ultra 128 GB or M3 Ultra 128 GB
- **Production inference** (serving others): consider a GPU rig instead

And if you haven't committed to Mac yet: price out a RTX 4090 build anyway. Sometimes the GPU path makes more sense.

---

**See also:**
- [Ollama](https://ollama.ai) - Easy local LLM runner for Mac
- [MLX](https://github.com/ml-explore/mlx) - Apple's ML framework (very fast on Apple Silicon)
- [vLLM](https://vllm.ai) - Production inference engine (good batching)
- [llama.cpp](https://github.com/ggerganov/llama.cpp) - Portable quantised inference
- [Mac Studio specs](https://www.apple.com/mac-studio/specs/) - Official configurations
