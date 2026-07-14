---
title: "Which Mac Studio Should You Buy for Running LLMs Locally?"
date: 2026-07-13T21:22:00+01:00
draft: false
type: guide
tags: ["ai", "apple", "llm", "mac-studio", "inference", "local-llm", "qwen", "llama"]
description: "A practical guide to Mac Studio configs for running popular free models locally (Qwen, LLaMA, Mixtral), realistic performance expectations, and which hardware actually makes sense."
cover:
  image: /assets/images/ai/which-mac-studio-llms.jpg
  alt: Mac Studio LLMs Icon
---

## TL;DR

- **Best entry point:** M2 Max 32-64 GB (~£1.4k-£2k) for 7B-13B models at 25-40 tok/s
- **Best sweet spot:** M2 Ultra 64-128 GB (~£3k-£4.5k) handles 30B+ models comfortably
- **Best for 70B models:** M3 Ultra 128 GB+ (~£5.5k+) with 800+ GB/s bandwidth
- **Newer alternative:** M4 Max (£2k-£4k) - lower bandwidth (410-546 GB/s) than Ultra chips, but still solid for 7B-13B models
- **Key rule:** Memory bandwidth matters more than raw compute for token generation
- **Reality check:** A RTX 5090 rig is 2-3× faster for similar money - buy Mac for simplicity and unified memory
- **July 2026 update:** Apple's memory crunch has killed new 256GB/512GB Ultra configs for now - big-memory Macs are refurb-only until the M5 Ultra (tested up to 768GB) lands late 2026
- **On the horizon:** the M7 Ultra, rumoured for around 2029, is reportedly designed to support up to 1.5TB of unified memory - see [the road ahead](#the-road-ahead-m5-ultra-this-year-then-a-15tb-m7-ultra) below

You want to run large language models locally on a Mac Studio. Good idea - unified memory is genuinely useful for LLMs. But the specs matter, and there are some hard truths about what "works" versus what feels responsive. More importantly: the right Mac depends entirely on which model you want to run.

If you're also weighing up NVIDIA's dedicated AI box, see my companion piece: [DGX Spark vs Mac Studio: Which Personal AI Supercomputer Should You Buy?](/ai/dgx-spark-vs-mac-studio/) - it goes deeper on the CUDA vs Apple Silicon trade-off.

## Memory requirements: which model fits your Mac?

Different models have wildly different memory demands. Here's what you actually need for the top free models:

### Small models (great for any Mac)
- [**LLaMA 3 7B**](https://huggingface.co/meta-llama/Meta-Llama-3-8B): ~4–5 GB (Q4), ~8 GB (Q5)
- [**Mistral 7B**](https://huggingface.co/mistralai/Mistral-7B-v0.1): ~4–5 GB (Q4), ~8 GB (Q5)
- [**Phi 2**](https://huggingface.co/microsoft/phi-2): ~2.5 GB (Q4)

**Reality:** Runs on M2 Max easily. 15–40 tok/s depending on chip.

### Medium models (the practical sweetspot)
- **LLaMA 3 13B**: ~8–10 GB (Q4), ~13 GB (Q5)
- **Deepseek Chat 7B / 13B**: ~4–10 GB
- **Gemma 7B / 13B**: ~4–10 GB

**Reality:** Comfortable on M2 Max, excellent on M2 Ultra. 20–40 tok/s is standard.

### Large dense models (needs real hardware)
- [**LLaMA 3 70B**](https://huggingface.co/meta-llama/Meta-Llama-3-70B): ~38–42 GB (Q4), ~65 GB (Q5)
- [**Mixtral 8x7B MoE**](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1): ~14–16 GB (Q4), ~24 GB (Q5)

**Reality:** Mixtral works well on M2 Ultra. 70B needs M3 Ultra or a GPU rig.

### Mixture-of-experts (tricky)
- [**Qwen 35B MoE**](https://huggingface.co/Qwen) (3B active): ~19–22 GB (Q4), ~36 GB (Q8)
- [**Mixtral 8x22B**](https://huggingface.co/mistralai/Mixtral-8x22B-v0.1): ~24–28 GB (Q4), ~40 GB (Q5)

**Reality:** You must load all weights even though only part activates. Needs M2 Ultra minimum.

The key gotcha: active parameters ≠ memory footprint. Qwen 35B with 3B active still needs 35B worth of weights in memory.

Add overhead for KV cache (0.5–4 GB depending on context window), and you need realistic headroom: at least 24–28 GB total for any 30B+ model.

## The Apple Silicon advantage and its limits

Mac Studio sits in an interesting middle ground.

**What's good:**
- Unified memory architecture (GPU and CPU share the same pool)
- No VRAM bottleneck
- Memory bandwidth is genuinely strong (800+ GB/s on Ultra variants)

**What's limiting:**
- Not CUDA - you're stuck with Metal backend or custom implementations
- Raw compute is lower than high-end GPUs
- Generation speed is memory-bound, and that bandwidth matters more than raw TFLOPs

This means Mac Studio doesn't compete with a gaming GPU rig on tokens/second, but it punches above its weight on simplicity and price per GB of usable memory.

## Mac Studio configs and real-world performance

Here's what actually runs well on each Mac, with realistic token speeds.

### M2 Max (32–64 GB) - Budget entry point

**What runs well:**
- LLaMA 3 7B–13B: ✅ excellent (25–40 tok/s)
- Mistral 7B: ✅ excellent (25–40 tok/s)
- Mixtral 8x7B: ⚠️ tight but viable (12–18 tok/s at 32GB)
- Qwen 35B / 70B: ❌ frustrating (8–15 tok/s, memory pressure)

**Cost:** £1,400–£2,500 new

**Verdict:** Perfect for small–medium models. Skip if you want 30B+ class models.

### M2 Ultra (64–128 GB) - The sweet spot

**What runs well:**
- LLaMA 3 7B–13B: ✅ excellent (30–45 tok/s)
- Mixtral 8x7B: ✅ very good (18–28 tok/s)
- Qwen 35B / Mixtral 8x22B: ✅ responsive (15–25 tok/s at 64GB, 18–28 tok/s at 128GB)
- LLaMA 70B: ⚠️ barely viable (8–12 tok/s at 128GB only)

**Specs:** 20 cores CPU, 16 cores GPU, ~800 GB/s bandwidth

**Cost:** £3,000–£5,500 new; ~£2,400–£3,200 refurbished

**When to buy:** You want proper performance on 30B+ models without overspending. Excellent refurbished market (these age well).

### M3 Ultra (96–512 GB) - No compromises

> **Availability note (July 2026):** Apple discontinued the 256GB and 512GB M3 Ultra options in March 2026 amid memory chip supply issues, and new units now cap at 96GB - at a higher price than before. Anything bigger means the refurbished or second-hand market until the M5 Ultra refresh arrives. Full details in [MacRumors' report](https://www.macrumors.com/2026/06/25/m5-ultra-mac-studio-2026/).

**What runs well:**
- All medium models: 🚀 excellent (35–50+ tok/s)
- Qwen 35B / Mixtral variants: 🚀 very smooth (20–30 tok/s)
- LLaMA 70B: ✅ smooth (22–30 tok/s at 128GB, faster at 192GB+)
- Multiple concurrent models: ✅ comfortable headroom

**Cost:** £4,200–£7,500+

**When to buy:** You're serious about local AI. You want to run large models, experiment with different ones, or handle long contexts (32K+).

### M4 Max (36–128 GB) - The newer alternative

**Bandwidth trade-off:** 410–546 GB/s vs 800+ on Ultra chips. Still faster than NVIDIA's DGX Spark (273 GB/s), just lower than Ultra-tier Macs.

**What runs well:**
- LLaMA 3 7B–13B: ✅ great (25–35 tok/s)
- Mixtral 8x7B: ✅ workable (15–22 tok/s)
- Qwen 35B: ⚠️ only if maxed to 128GB, then ~15–22 tok/s (M2 Ultra does similar for less)

**Cost:** ~£2,000–£4,000

**Verdict:** Newer chip with better efficiency, genuinely good for 7B-13B models at the base config. If you want 30B+ headroom, M2/M3 Ultra is the better-bandwidth pick.

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

## Picking your Mac based on your model choice

**You want to run 7B–13B models (LLaMA 3, Mistral, etc.)**

→ **M2 Max with 32–64 GB** (~£1.5k–£2.5k)

- 25–40 tok/s is standard
- Great value, these are excellent utility models
- Plenty of power

**You want to run 30B–35B models (Qwen, Mixtral, etc.)**

→ **M2 Ultra with 64 GB minimum** (~£3k, or £2.4k refurbished)

- 15–25 tok/s depending on model
- Comfortable performance for interactive use
- Good refurbished availability

→ **M2 Ultra with 128 GB** (~£4.5k) if you want headroom

- Smoother under load, room for larger context windows
- Best price/performance for serious local AI work

**You want to run 70B models or experiment with multiple large models**

→ **M3 Ultra with 128 GB** (~£5.5k)

- 22–30 tok/s on 70B models
- Newest architecture, better efficiency
- Actually comfortable for production-style use

**You want maximum flexibility (mix of models, large contexts, concurrency)**

→ **M3 Ultra with 192 GB or 256 GB** (~£7k+)

- Handles everything without compromise
- Can run multiple models simultaneously
- Proper AI workstation feel

## The honest comparison table

| Mac Config | Price | LLaMA 13B | Mixtral 8x7B | Qwen 35B | 70B Models | Vibes |
|-------|-------|-----------|------|----------|---------|-------|
| M2 Max 32GB | £1.4k | 30–40 ✅ | not viable ❌ | not viable ❌ | no ❌ | Budget entry |
| M2 Max 64GB | £2k | 30–40 ✅ | 12–18 ⚠️ | struggles ❌ | no ❌ | Good for small |
| M2 Ultra 64GB | £3k | 35–45 ✅ | 18–28 ✅ | 15–22 ✅ | 8–12 ⚠️ | Sweet spot |
| M2 Ultra 128GB | £4.5k | 35–45 ✅ | 20–30 ✅ | 18–25 ✅ | 10–15 ⚠️ | Comfortable |
| M3 Ultra 128GB | £5.5k | 40–50 🚀 | 22–32 🚀 | 20–28 🚀 | 22–30 ✅ | Excellent |
| M3 Ultra 256GB | £8k+ | 40–50 🚀 | 22–32 🚀 | 20–28 🚀 | 25–32 ✅ | Workstation |
| M4 Max 36GB | £2k | 25–35 ✅ | not viable ❌ | not viable ❌ | no ❌ | Newer, efficient |
| M4 Max 64GB | £3k | 25–35 ✅ | 15–22 ✅ | struggles ❌ | no ❌ | Decent mid-tier |
| M4 Max 128GB | £4k | 25–35 ✅ | 15–22 ✅ | 15–22 ⚠️ | no ❌ | Good but Ultra wins |

**My recommendation:** If you're spending £3k–£4k anyway, M2 Ultra with 64–128 GB is the inflection point where the experience stops feeling constrained. You get real performance without paying for the latest chip.

## Context window penalty (often overlooked)

Larger context windows mean larger KV cache, which means slower generation. This hits harder on Mac than GPU rigs.

**Typical slowdown:**
- 4K context: baseline speed
- 16K context: -10–25% slower
- 32K context: -25–40% slower
- 100K+ context: can halve throughput

**Real example:** If your model does 25 tok/s at 4K context, expect ~12–15 tok/s at 32K context on the same Mac.

**Practical implication:** For local use, aim for 4K–16K context windows. You keep speed without losing useful context for code, research, or chat. Only go beyond 32K on M3 Ultra with 128 GB+ if you truly need it.

## Alternative: GPU rigs aren't cheaper

Since you're spending £3k–£5k anyway, you should know: a comparable GPU setup isn't obviously better.

A single RTX 5090:
- £2,500–£3,500 (depending on availability)
- 32 GB VRAM
- 40–70 tok/s on Qwen 35B
- But: CUDA setup overhead, electricity cost (~600W), cooling

**RTX 5090 vs M2 Ultra 64 GB:**
- RTX is 2–3× faster on models that fit in VRAM
- Mac is simpler, cheaper running costs, unified memory (no 32GB VRAM ceiling)
- You're paying for convenience more than raw performance

Both are legitimate choices. Mac Studio is the right call if you value simplicity. For a detailed side-by-side with NVIDIA's purpose-built AI box, see [DGX Spark vs Mac Studio](/ai/dgx-spark-vs-mac-studio/) - prefill speed, CUDA fine-tuning, and the hybrid setup that beats either alone.

## Popular models ranked by memory + performance

Since you're choosing both a Mac and a model, here's what actually matters:

| Model | Size | Memory (Q4) | tok/s (M2 Ultra) | tok/s (M3 Ultra) | Best for |
|-------|------|------------|--------|--------|----------|
| LLaMA 3 7B | 7B | 4–5 GB | 30–40 | 40–50 | Fast, responsive, coding |
| Mistral 7B | 7B | 4–5 GB | 30–40 | 40–50 | Similar to LLaMA, French origin |
| Mixtral 8x7B | MoE 56B | 14–16 GB | 18–28 | 22–32 | Better quality than 7B, still fast |
| Deepseek Coder | 6.7B–33B | 4–18 GB | 25–35 | 35–45 | Code generation specialty |
| LLaMA 3 13B | 13B | 8–10 GB | 25–35 | 35–45 | Better reasoning than 7B |
| Gemma 13B | 13B | 8–10 GB | 25–35 | 35–45 | Smaller, efficient alternative |
| Qwen 35B MoE | MoE 35B | 19–22 GB | 15–22 | 20–28 | Strong reasoning, sparse |
| Mixtral 8x22B | MoE 141B | 24–28 GB | 12–18 | 16–24 | Highest quality dense-equivalent |
| LLaMA 3 70B | 70B | 38–42 GB | 8–12 | 22–30 | Expert-level, needs headroom |

**Patterns:**
- 7B models: fit anywhere, 30–40+ tok/s even on M2 Max
- 13B models: good sweet spot, 25–35 tok/s on M2 Ultra
- MoE models: efficient for their capability, 15–28 tok/s depending on size
- 70B+: only practical on M3 Ultra or GPU

## Real-world advice

**If you just want something that works:** Grab LLaMA 3 7B or Mistral 7B. They run everywhere, generate good output, and hit 30+ tok/s. You don't need to spend £3k.

**If you want better quality without overspending:** LLaMA 3 13B or Mixtral 8x7B on an M2 Ultra 64GB (£3k). This is where quality meets responsive performance.

**If you're serious about local AI:** M2 Ultra 128 GB or M3 Ultra 128 GB. You can keep multiple models loaded, experiment freely, and handle longer contexts without compromise.

**If GPU is an option:** Price out a RTX 5090 rig anyway. For £3k–£4k, a 5090 will give you 2–3× the speed on models that fit in 32GB VRAM. Mac Studio is the right choice only if you value simplicity + unified memory + larger model support + lower power consumption.

## The road ahead: M5 Ultra this year, then a 1.5TB M7 Ultra

*Updated July 2026.* Everything above is about what you can buy today. But Apple's chip roadmap has leaked in enough detail that it's worth factoring into any purchase decision - because the ceiling on local AI is about to move a long way.

### M5 Ultra Mac Studio (expected late 2026)

The next Mac Studio refresh was originally pencilled in for mid-2026 but has slipped to an expected October window, delayed by memory chip supply issues and price rises. According to [MacRumors' reporting](https://www.macrumors.com/2026/06/25/m5-ultra-mac-studio-2026/), the M5 Ultra is expected to bring:

- ~36 CPU cores and ~80 GPU cores
- Tested support for up to **768GB of unified memory** - triple the M3 Ultra's original 256GB mid-tier and half again over its 512GB ceiling
- The caveat: supply constraints could keep the biggest memory option off the launch configurator, and a 768GB variant would likely cost well north of $10,000

If you're eyeing a big-memory Mac and can wait a few months, the M5 Ultra is the obvious thing to wait for. If you can't, the refurbished M2/M3 Ultra market remains the value play.

### The M7 Ultra rumour: 1.5TB of unified memory by ~2029

This is the one that made me sit up. According to Bloomberg's Mark Gurman, whose reporting was picked up by [9to5Mac](https://9to5mac.com/2026/07/12/m7-ultra-mac-studio-to-support-up-to-1-5-tb-unified-memory/) and [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai), Apple plans to skip high-end M6 desktop variants entirely and jump to an M7 generation, with an **M7 Ultra designed to support up to 1.5TB of unified memory** - roughly double the M5 Ultra's ceiling, finally matching the 2019 Intel Mac Pro's RAM limit, and aimed at Blackwell-class AI performance. A server variant of the chip is reportedly also in the works. Expected arrival: around 2029.

The usual rumour disclaimers apply, and [Macworld makes a fair point](https://www.macworld.com/article/3189940/apple-is-working-on-an-ultra-chip-with-1-5tb-of-ram-but-we-may-never-see-it.html) that the state of the RAM market will decide whether the 1.5TB configuration ever actually ships. Apple has confirmed none of this.

### What 1.5TB on a desk would actually mean

The rumour went properly viral when [Alex Finn put it bluntly on X](https://x.com/AlexFinn/status/2076800124072955959): "You are going to be able to run Fable 5 locally on your desk... With just 300GB of memory you can run Opus 4.8 level intelligence. Think of what you can do with 5x that."

I'd gently correct the letter of that while agreeing with the spirit. Frontier labs don't publish their weights, so nobody will be downloading Fable 5 or Opus 4.8 onto a Mac Studio. What you *will* be able to do is run **open-weight models at the trillion-parameter scale** - and the open-weight frontier has been tracking a couple of years behind the closed frontier. Around 300GB already fits today's largest open-weight models at sensible quantisation (see my [state of open-weight models](/ai/state-of-open-weight-models-2026/) post). So "2029-era open weights on 1.5TB of memory" plausibly does mean something like today's frontier-level intelligence, running on your desk, with no subscription and no data leaving the room. That's a genuinely different world for privacy, tinkering, and home agents.

Two engineering caveats before anyone gets carried away:

- **Capacity isn't speed.** Token generation is bandwidth-bound, and 1.5TB of weights doesn't help if the bandwidth-per-byte doesn't scale with it. A dense trillion-parameter model would still generate slowly; in practice mixture-of-experts architectures (where only a fraction of weights activate per token) are what make this class of machine useful, exactly as with the MoE models covered above.
- **This is a 2029 rumour about an unannounced chip**, filtered through a supply-constrained RAM market. Plan with it, don't bank on it.

### How to prepare now

Here's the part of Finn's thread I fully agree with: the people who learn local AI now will be miles ahead when this hardware lands. The skills transfer completely - a 7B model on an M2 Max teaches you the same stack you'd use on a 1.5TB M7 Ultra:

- Get comfortable with [Ollama](/ai/ollama/) and quantised models - even on a MacBook
- Put a proper interface on it with [Open WebUI](/ai/open-webui-self-hosted-llm-interface/)
- Understand the [local vs cloud trade-offs](/ai/local-vs-cloud-ai-2026/) so you know what belongs where
- Start wiring up a [home agent stack](/ai/home-agent-stack/) - agents are where big local memory pays off most, since you can keep several specialised models resident at once

None of that requires new hardware. All of it compounds.

---

## Tools to actually run these models

- [Ollama](https://ollama.ai) - Easiest entry point for Mac, supports most popular models
- [MLX](https://github.com/ml-explore/mlx) - Apple's own ML framework, fastest on Apple Silicon
- [llama.cpp](https://github.com/ggerganov/llama.cpp) - Portable, works everywhere, widely used
- [LM Studio](https://lmstudio.ai) - Desktop UI, good for beginners
- [Open Web UI](https://openwebui.com) - Modern web interface for local models, great with Ollama
- [GPT4All](https://gpt4all.io) - Easy desktop app with built-in models, minimal setup
- [Text Generation WebUI](https://github.com/oobabooga/text-generation-webui) - Feature-rich web interface with chat, notebook, and API modes
- [LocalAI](https://localai.io) - OpenAI-compatible API for local inference, easy integration
- [vLLM](https://vllm.ai) - Production inference engine if you need batching/concurrency
- [Hugging Face Transformers](https://huggingface.co/docs/transformers) - The foundational library for running any model programmatically

## Model sources

- [Hugging Face](https://huggingface.co/models) - Largest model repository
- [Ollama library](https://ollama.ai/library) - Pre-configured models for easy download
- [TheBloke quantisations](https://huggingface.co/TheBloke) - High-quality Q4/Q5 versions of popular models

## Reference

- [Mac Studio specs](https://www.apple.com/mac-studio/specs/) - Official Apple configurations
- [Apple MLX documentation](https://ml-explore.github.io/mlx/) - Framework optimised for Apple Silicon
- [llama.cpp Metal backend](https://github.com/ggerganov/llama.cpp/blob/master/docs/build.md#metal-build) - How Metal acceleration works on Mac
- [MacRumors: M5 Ultra Mac Studio](https://www.macrumors.com/2026/06/25/m5-ultra-mac-studio-2026/) - Late-2026 refresh, up to 768GB tested
- [9to5Mac: M7 Ultra and 1.5TB unified memory](https://9to5mac.com/2026/07/12/m7-ultra-mac-studio-to-support-up-to-1-5-tb-unified-memory/) - The ~2029 roadmap rumour

## Related Reading

- [DGX Spark vs Mac Studio: Which Personal AI Supercomputer Should You Buy?](/ai/dgx-spark-vs-mac-studio/) - full comparison with NVIDIA's Blackwell-powered AI appliance
- [Running AI Models Locally with Ollama](/ai/ollama/) - practical walkthrough of the easiest local-inference stack
- [Local vs Cloud AI in 2026](/ai/local-vs-cloud-ai-2026/) - when to run locally versus pay per token
- [Giving Your Home AI Agent Real Tools: MCP Servers on a Mac Studio](/ai/mcp-servers-home-ai-agent/) - wiring the tool layer once the hardware is sorted
- [AI Economics and Hardware: A Reading Path](/ai/ai-economics-hardware/) - full reading path on token costs, GPU choices, and energy constraints
