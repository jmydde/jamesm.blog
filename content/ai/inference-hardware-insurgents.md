---
title: "Cerebras, Groq, SambaNova: The Inference Hardware Insurgents"
date: 2026-05-11T13:00:00+01:00
draft: false
tags: ["ai", "hardware", "inference", "cerebras", "groq", "sambanova", "nvidia", "2026"]
description: "A grounded look at the three serious AI inference hardware insurgents in 2026 - Cerebras with its wafer-scale WSE-3, Groq with its LPU architecture now part-licensed by Nvidia, and SambaNova with its SN40L and SN50 reconfigurable dataflow units - and what their different bets tell us about where inference is heading."
cover:
  image: /assets/images/ai/inference-hardware-insurgents.png
  alt: Inference Hardware Insurgents - Cerebras, Groq, SambaNova Banner
---

For most of the last decade, talking about AI hardware meant talking about Nvidia. In 2026 that has stopped being true at the inference layer. Three companies - Cerebras, Groq, and SambaNova - have built genuinely different chips around the same insight: that the workload economics of running models in production are not the same as the workload economics of training them, and that the chip architecture should follow the workload. The bet has been right enough that Nvidia has now licensed pieces of it.

## TL;DR

- The three credible inference-hardware insurgents in 2026 are **[Cerebras](https://www.cerebras.ai/chip)** (wafer-scale WSE-3), **[Groq](https://groq.com/lpu-architecture)** (LPU architecture with SRAM-on-chip), and **[SambaNova](https://sambanova.ai/products/rdu-ai-chips)** (Reconfigurable Dataflow Units with three-tiered memory).
- Each company has taken a different architectural bet. Cerebras builds a single 46,225 mm² chip with 4 trillion transistors. Groq interleaves processing and SRAM on smaller dies and scales out across hundreds of chips. SambaNova combines SRAM, HBM, and DRAM on its RDU to keep very large models resident in memory.
- The reported benchmarks favour different chips on different workloads. Cerebras hit 1,000+ tokens/sec on Llama 3.1 405B. Groq delivers Llama 2 70B at roughly 300 tokens/sec - around 10x what an Nvidia H100 cluster does on the same workload. SambaNova claims 129 tokens/sec/user on Llama 3.1 405B and 5x faster inference with its [SN50](https://sambanova.ai/blog/sn40l-chip-best-inference-solution) chip announced in early 2026.
- The single most important industry event of the cycle was Nvidia's [reported $20 billion licensing deal](https://en.wikipedia.org/wiki/Groq) for Groq's IP in late 2025, which gave Nvidia the LPU technology that became the *Groq 3 LPU* announced at GTC 2026 as a Rubin GPU inference co-processor.
- The strategic picture is that inference is becoming a separate hardware market from training, that Nvidia has accepted this and bought in, and that the surviving insurgents will differentiate on workload fit and total cost of ownership rather than on raw throughput numbers.

## Why inference is now a separate hardware market

For most of the deep-learning era, the same chips trained models and served them. That made commercial sense when training was the hard part of the workload and serving was a small tax on top. It stopped making sense once frontier models scaled into hundreds of billions of parameters and the cost of serving them in production overtook the cost of training them by a wide margin.

The shift matters because the economics of inference are different from the economics of training in three concrete ways. Training is mostly arithmetic-bound and benefits from dense, high-throughput compute. Inference is mostly memory-bandwidth-bound and benefits from chips that can move weights in and out of memory at very high rates. Training tolerates batching across many requests and amortises latency. Inference, especially in agentic and interactive workloads, lives or dies on per-request latency and on the time-to-first-token that the user actually experiences. Training is dominated by a small number of very large jobs. Inference is dominated by a very large number of small jobs at variable load.

Those three differences turn out to be enough that a chip optimised for one is not the best chip for the other. The insurgents have been arguing this since 2021. The market accepted it slowly and then all at once.

## The three architectures

### Cerebras

[Cerebras](https://www.cerebras.ai/) is the most physically ambitious of the three. The [WSE-3](https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine) is built on a single 5nm silicon wafer measuring 46,225 mm² with 4 trillion transistors and 900,000 AI-optimised cores. The chip is not packaged like a normal chip - the wafer is the chip - which is why the production process and the system around it have been one of the company's main R&D investments.

The architectural bet is that the bottleneck in modern AI workloads is communication between chips, and that you eliminate the bottleneck by not having multiple chips. The WSE-3 keeps all the model weights and intermediate activations on a single piece of silicon, with the cores connected by a high-bandwidth fabric that does not have to cross any package boundary. The result, on the workloads where the model fits, is throughput that GPU arrays cannot match - the [reported 1,000-plus tokens per second on Llama 3.1 405B](https://www.cerebras.ai/) is the public number, and the architectural story is the explanation.

The weakness of the bet is the same as the strength. The WSE-3 is a very large, very expensive, very power-hungry single chip. The CS-3 system around it runs at roughly 25kW per system, and the unit economics depend on running the chip at high utilisation. Cerebras has responded by building an inference cloud business that aggregates demand across customers, and the product is now [Cerebras Inference](https://www.cerebras.ai/) - a managed API that serves frontier models faster than most GPU alternatives.

### Groq

[Groq](https://groq.com/) was founded by [Jonathan Ross](https://www.linkedin.com/in/ross-jonathan/), who previously worked on Google's TPU. The Groq Language Processing Unit (LPU) is the architectural opposite of Cerebras - small dies with very high on-chip SRAM bandwidth, scaled out across hundreds of chips connected by a deterministic interconnect. The bet is that the dominant cost in inference is moving weights from external memory to compute, and that you can largely eliminate this cost by keeping weights in on-chip SRAM at all times.

The empirical result has been some of the lowest latencies and highest tokens-per-second numbers in the industry. Groq's [public benchmarks](https://groq.com/lpu-architecture) show Llama 2 70B at roughly 300 tokens per second, which is about an order of magnitude faster than an H100 cluster running the same workload. The architecture is particularly well-suited to interactive and agentic workloads where time-to-first-token matters more than total throughput, and Groq has built its business around that segment.

The single biggest commercial event of the cycle was the [reported $20 billion licensing deal](https://en.wikipedia.org/wiki/Groq) with Nvidia in late 2025. Nvidia did not acquire Groq - it licensed core elements of the LPU IP and integrated them into what was announced at [GTC 2026 as the Groq 3 LPU](https://spectrum.ieee.org/nvidia-groq-3), a Rubin-platform co-processor for inference. The strategic significance is that Nvidia, the company most aligned with general-purpose GPUs for both training and inference, accepted publicly that inference needs a different chip and paid a very large sum to acquire the right one. Groq the company continues to operate independently and has [partnered with Meta](https://groq.com/) to serve the official Llama API, which is now [used by over 1.9 million developers](https://groq.com/) on GroqCloud.

### SambaNova

[SambaNova](https://sambanova.ai/) takes the third major bet. Its Reconfigurable Dataflow Unit (RDU) - the [SN40L](https://sambanova.ai/blog/sn40l-chip-best-inference-solution) shipped in 2023 and the SN50 announced in early 2026 - is a chip with three tiers of memory: on-chip SRAM, high-bandwidth memory (HBM), and high-capacity DRAM, all addressable from the compute fabric. The bet is that the workload that actually matters is serving very large models with many simultaneous variants - mixture-of-experts architectures, multi-tenant deployments, or enterprise stacks with dozens of fine-tuned models - and that the chip best suited to this is one that can hold trillion-parameter models in memory and switch between them quickly.

The numbers SambaNova publishes [favour this framing](https://sambanova.ai/blog/sambanova-vs-cerebras). On the largest 405B Llama 3.1 model, SambaNova reports 129 output tokens per second per user, and notes that neither Groq nor Cerebras currently serves it at all in this configuration. On the 70B model, SambaNova claims to outperform both competitors and GPU-based providers. The SN50, announced in February 2026, is reported to deliver roughly 5x the inference performance of competitors with a 3x lower total cost of ownership versus GPUs, though those numbers are vendor-supplied and should be read with the usual caution.

The architectural bet has positioned SambaNova as the enterprise-friendly insurgent. The chip's ability to keep many large models resident makes it a natural fit for regulated industries that need to serve dozens of fine-tuned variants on a single substrate, and SambaNova has built much of its commercial business around that segment.

## How they actually differ

The architectures are easier to summarise than to compare. The honest version of the comparison is that the three chips win on different workloads and there is no single benchmark that captures the trade-offs fairly. With that caveat in mind, the rough shape of the differences is:

**On peak throughput for very large models**, Cerebras wins on workloads where the model fits in a wafer's memory and the workload can be batched. The 405B numbers reflect this.

**On per-request latency**, Groq tends to win. The SRAM-resident weights eliminate the largest source of latency in transformer inference, and the deterministic interconnect minimises the variance.

**On multi-model, multi-tenant workloads**, SambaNova's three-tier memory makes it the best fit. Holding many models in memory simultaneously is the differentiating capability and it shows up clearly in enterprise deployments.

**On Nvidia compatibility**, none of the three is a drop-in replacement. The software stacks have improved significantly - all three companies now offer OpenAI-compatible APIs and standard model loaders - but moving an existing training pipeline to any of these chips is non-trivial. The integration cost is the single biggest reason most teams have continued to default to GPUs even when the inference economics on alternative chips look better.

## What the Nvidia deal actually changed

The Nvidia-Groq licensing deal is worth dwelling on because it changed the shape of the market in a way that is sometimes missed.

Before the deal, the standard story was that the insurgents were trying to displace Nvidia and that Nvidia would either build comparable inference chips internally or use its scale to crowd them out. After the deal, the story changed in three ways. First, Nvidia acknowledged publicly that inference needs a different chip from training and paid an enormous sum to acquire the IP for it. Second, the Groq 3 LPU is now part of the Rubin platform - Nvidia's customers can get inference-optimised silicon inside the same ecosystem they already use for training. Third, the strategic ceiling for Cerebras and SambaNova got higher, because the comparable IP path is now closed to Nvidia and the remaining insurgents are the only credible alternatives if you do not want to be on the Rubin stack.

For customers, the practical implication is that the inference-hardware market is now a multi-vendor market with Nvidia as the default and Cerebras and SambaNova as the credible specialists. That is a different competitive picture from the one most analysts were forecasting two years ago and it has implications for capacity planning, for model serving architecture, and for the negotiating power individual customers have at the hyperscalers.

## What the bet looks like from each side

**The Cerebras bet** is that wafer-scale is a defensible architectural moat. If the workloads keep getting bigger and the model-on-a-single-chip story holds, Cerebras wins on the largest serving deployments. If models stabilise in size or get pushed down by efficiency improvements, the architectural advantage shrinks and the cost structure becomes harder to defend.

**The Groq bet** is now partly Nvidia's bet too. The standalone company is positioning itself as the developer-friendly, low-latency inference cloud, and the Meta partnership and the GroqCloud growth numbers suggest the bet is working. The risk is that the same IP is now inside Nvidia products and the differentiation has to come from operational excellence and customer integration rather than from architecture alone.

**The SambaNova bet** is on the enterprise stack. Multi-model serving, regulated industries, on-premises deployments where data residency matters - this is the segment that values the architectural choices SambaNova made and is willing to pay for them. The risk is that the enterprise segment is harder to scale than the developer segment and the sales cycles are longer.

## Where this is heading

The most likely shape of 2027-2028 is that the inference-hardware market settles into a four-vendor structure with Nvidia as the integrated default and Cerebras, Groq, and SambaNova as the specialists optimised for distinct workload profiles. The boring outcome is the consequential one: customers pick chips based on workload fit, the unit economics of inference continue to come down, and the gap between training and inference cost structures continues to widen.

The other prediction worth making is that one of the three insurgents is likely to be acquired by a major cloud provider within the next two years. The strategic logic for AWS, Azure, or Google Cloud to own a credible non-Nvidia inference path is strong, and the price of acquiring one of these companies is small relative to the scale of the AI compute spend. The Nvidia-Groq licensing deal is plausibly a template for the next move rather than the last one.

For people building with these tools today, the practical implication is the boring one again. The chips are real, the price-performance numbers are real, and the integration cost is real. If your inference economics matter at scale, it is worth running the workload on at least one alternative substrate before committing. If you are early enough that the integration cost dominates, the GPU default is still the rational choice. The market has moved enough that staying on the default forever has become a bet rather than a baseline.

## Further Watching

### 4,000,000,000,000 Transistors, One Giant Chip (Cerebras WSE-3)
{{< youtube "f4Dly8I8lMY" >}}

### Jonathan Ross, Founder & CEO @ Groq: NVIDIA vs Groq - The Future of Training vs Inference
{{< youtube "xBMRL_7msjY" >}}

### Groq Founder, Jonathan Ross: OpenAI & Anthropic Will Build Their Own Chips & Will NVIDIA Hit $10TRN
{{< youtube "VfIK5LFGnlk" >}}

### Rodrigo Liang on The Information: AI Chips, Power, and Scaling Beyond GPUs
{{< youtube "R5--sxXraHc" >}}

### Rodrigo Liang, SambaNova | theCUBE + NYSE Wired: AI Factories - Data Centers of the Future
{{< youtube "vt25kgPNkYo" >}}

## Related Reading

- [GPU Servers vs AI API Credits: The Real Cost Breakdown (2026)](/ai/gpu-servers-vs-api-credits/) - the deployer's view of the same cost-of-inference story these chips are designed to change.
- [DGX Spark vs Mac Studio: Which Personal AI Supercomputer Should You Buy?](/ai/dgx-spark-vs-mac-studio/) - the consumer-end inference-hardware story.
- [Token Economics: Why the Cost of AI Isn't Going Down](/ai/token-economics-why-costs-arent-going-down/) - the economics that makes specialised inference silicon necessary in the first place.
- [Local AI vs Cloud AI: The Tradeoff Landscape in 2026](/ai/local-vs-cloud-ai-2026/) - where inference actually runs in 2026.
- [The Rise of Small Language Models: Why Size Isn't Everything](/ai/small-language-models/) - the model-side counterpart to the hardware-side story here.
