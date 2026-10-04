---
title: "Taalas and AMD: Hardwiring an AI Model Into Silicon for 17,000 Tokens a Second"
date: 2026-10-04T10:00:00+01:00
draft: false
tags: ["ai", "hardware", "inference", "gpu", "acquisition", "2026"]
description: "AMD has agreed to buy Taalas, the Toronto startup that etches an AI model's weights directly into a chip. Its first chip claims around 17,000 tokens per second per user. Here is how it works, what is verified, what is not, and where it could lead."
cover:
  image: /assets/images/ai/taalas-amd-hardwired-ai-chips.jpg
  alt: Taalas and AMD - Hardwiring an AI Model Into Silicon for 17,000 Tokens a Second banner
---

## TL;DR

- On 6 August 2026 AMD announced a definitive agreement to acquire Taalas, a Toronto startup founded in 2023. No price was disclosed and the deal is subject to regulatory approval
- Taalas builds chips with a single AI model hardwired into the silicon. Its first, the HC1, runs Meta's Llama 3.1 8B
- Taalas claims up to 17,000 tokens per second per user at roughly a tenth of the power of a GPU. An outside test measured 14,357
- The catch is flexibility: the chip cannot run any other model. Taalas says it can turn a new model into silicon in about two months
- AMD says it will fold the technology into its accelerator roadmap alongside Instinct GPUs

## The idea

A normal AI chip is a general-purpose machine. The model's weights sit in memory, and for every token generated the chip has to fetch billions of them across to the compute units. Most of the time and energy goes on that movement, not the arithmetic. That is the "memory wall" people talk about in inference.

Taalas takes the opposite approach. Instead of loading a model onto a chip, it makes the model part of the chip. Co-founder Ljubisa Bajic [described the problem](https://www.unite.ai/amd-buys-taalas-to-put-hard-wired-ai-models-in-its-accelerator-roadmap/) this way: "general-purpose inference hardware carries an artificial divide: memory on one side, compute on the other." Taalas's answer is to remove the divide.

## What the HC1 is

From [Taalas's own product page](https://taalas.com/products/) and [heise's report](https://www.heise.de/en/news/AI-inference-cast-in-silicon-Taalas-announces-HC1-chip-11185112.html):

- Made by TSMC on a 6nm process, an 815 mm² die with 53 billion transistors
- Runs Llama 3.1 8B and nothing else
- Taalas lists "17k tokens per second per user"
- No HBM memory, no water cooling and no advanced packaging, according to heise
- The context window size is configurable and LoRA fine-tuning is supported, so it is not completely frozen

According to [Sovereign Magazine's write-up](https://www.sovereignmagazine.com/article/taalas-hc1-ai-chip), only the top two metal layers of the roughly 100 on the chip are customised for a given model. That is what makes the fast turnaround possible: about two months to put a new model into silicon, against roughly six for a full custom chip.

## How fast is 17,000 tokens a second?

For scale, a person reads at perhaps 5 to 8 tokens a second. At 17,000 the answer to a long question is effectively there before you finish pressing enter. Taalas puts this at 73 times an Nvidia H200.

The same Sovereign Magazine piece reports that Karl Freund of Cambrian AI, writing in Forbes, "measured 14,357 tokens a second in his own test and reports HC1 racks drawing 12 to 15kW where GPU racks draw 120 to 600kW." I have not read the Forbes piece itself, so treat that as reported second-hand. It does suggest the headline number is broadly real rather than a lab best case.

## What is not yet proven

[Futurum's coverage](https://futurumgroup.com/insights/amd-acquires-taalas-to-advance-ai-workload-optimization/) and the others are clear about the limits:

- The figures are mostly vendor-supplied and need independent validation
- The first chip uses very aggressive quantisation. Heise reports a proprietary 3-bit format with 6-bit parameters, and Unite.ai notes this degrades output quality compared with GPU benchmarks
- Llama 3.1 8B is a small, now fairly old model. Nobody has shown a frontier-scale model on this approach yet
- A chip frozen to one model risks becoming obsolete as soon as a better model appears

## What AMD says it will do

AMD's Vamsi Boppana said: "AMD is building a full-stack AI platform that gives customers flexibility to deploy the right compute solutions for every AI workload." AMD intends to integrate the Taalas technology into its accelerator roadmap and build systems that pair it with Instinct GPUs, its Helios rack-scale platform, EPYC CPUs and the ROCm software stack.

Futurum analyst Brendan Burke argues the real prize may be the process more than the chip: AMD is acquiring "a team fluent in its own instruction sets and a working demonstration of a compressed silicon design cycle", at a time when AI-driven chip design tools are emerging.

## My read

This section is my opinion, not reported fact.

**Speed changes what you can build.** Most of today's AI applications are shaped around slow generation. At thousands of tokens a second you can do things that are impractical now: an agent that tries fifty approaches and picks the best before you notice, reasoning models that think at length without a wait, voice that never pauses. Tokens per second per user is a different bottleneck from total throughput, and it is the one people feel.

**Expect a split, not a replacement.** GPUs stay for training and for the fast-moving frontier where models change monthly. Hardwired chips make sense for a model that is good enough and stable, and where it will be called billions of times: a default assistant, a speech model, a code completion model. AMD pairing these with Instinct GPUs fits that picture, though AMD has not said how.

**The two-month cycle is the real bet.** If a model can reach silicon in two months and that falls further with automated chip design, the obsolescence problem shrinks. If it does not, hardwiring only suits models that are already settled.

**Efficiency matters as much as speed.** The rack power numbers, if they hold, speak directly to the data-centre power crunch. Cheaper tokens also mean more usage, which could cancel out some of the saving.

What I would watch for next: a hardwired chip running a model that is genuinely competitive today, independent quality benchmarks against the full-precision version, and whether AMD ships it as a product or keeps it as a design method.

## Videos

I could not find an interview with anyone at Taalas itself. What follows are explainers and analysis, plus an older interview with Taalas's CEO from his previous company. Most recent first.

### Coding Horizon: Local AI: This Hardware Runs Qwen At 17,000 Tok/S (28 September 2026)
{{< youtube M1A5rnfSO9U >}}

About twelve minutes. The description says it looks at Taalas's reported 17,000 tokens per second from a hardwired model alongside dedicated chips that bring Qwen to a local workstation, and asks what that means in practice.

### TechTechPotato: Why did AMD just buy this REALLY WEIRD chip company? (6 August 2026)
{{< youtube 3MKRjt59hh4 >}}

About sixteen minutes, uploaded the day the deal was announced. The description explains that Taalas has built a chip with a single AI model wired directly into its metal layers, with no programmability at all, so one part runs one model and nothing else.

### Turing Post TV: This chip runs a "baked" Llama so fast it looks like a glitch (Taalas HC1) (24 February 2026)
{{< youtube ibbB5CsDwxQ >}}

About thirteen minutes, from just after the HC1 was unveiled. The description says it covers how the chip outruns human perception at 17,000 tokens per second by baking the 8B Llama model into the silicon.

### Tenstorrent: Software and Silicon in Serbia w/ Ljubisa Bajic and Jim Keller (17 March 2022)
{{< youtube 5bn54FSe_0A >}}

Not about Taalas, which was founded in 2023. This is an hour-long conversation from Bajic's earlier company, Tenstorrent, where he was a founder, and it gives a sense of how he thinks about the limits of general-purpose computing for AI.

## Sources

- [Unite.ai: AMD Buys Taalas to Put Hard-Wired AI Models in Its Accelerator Roadmap](https://www.unite.ai/amd-buys-taalas-to-put-hard-wired-ai-models-in-its-accelerator-roadmap/) - deal terms, quotes from Boppana and Bajic, quantisation caveat
- [Futurum Group: AMD Acquires Taalas to Advance AI Workload Optimization](https://futurumgroup.com/insights/amd-acquires-taalas-to-advance-ai-workload-optimization/) - AMD's plans, analyst view and risks
- [heise: AI inference cast in silicon, Taalas announces HC1 chip](https://www.heise.de/en/news/AI-inference-cast-in-silicon-Taalas-announces-HC1-chip-11185112.html) - chip specifications
- [Taalas: Products](https://taalas.com/products/) - the HC1 and its 17k tokens per second claim
- [Sovereign Magazine: Taalas Builds AI Models Directly Into Its Silicon](https://www.sovereignmagazine.com/article/taalas-hc1-ai-chip) - the Cambrian AI measurement and the two-metal-layer detail
- [CNBC: AMD buys Taalas](https://www.cnbc.com/2026/08/06/amd-buys-taalas-startup-that-hardwires-ai-models-into-its-silicon.html) - original report, found via search and via Slashdot's summary (I could not open the page directly)

## Related Reading

- [AI Economics and Hardware](/ai/ai-economics-hardware/) - why the cost of inference matters
- [AI Energy Crisis and Data Centre Power](/ai/ai-energy-crisis-data-center-power/) - the power problem hardwired chips could ease
