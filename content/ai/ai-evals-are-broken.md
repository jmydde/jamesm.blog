---
title: "AI Evals Are Broken: Why Benchmarks Stopped Measuring Real Capability"
date: 2026-06-12T19:00:00+01:00
draft: false
series: ["Trust"]
tags: ["ai", "eval", "benchmark", "agentic-engineering"]
description: "A grounded look at why the public benchmark numbers you see on AI model launches in 2026 are increasingly disconnected from real-world capability - saturation, contamination, gaming, and what's replacing them as the basis for actual decisions."
cover:
  image: /assets/images/ai/ai-evals-are-broken.jpg
  alt: AI Evals Are Broken - Why Benchmarks Stopped Measuring Real Capability Banner
---

When a frontier lab releases a new model in 2026, the press release leads with a row of benchmark scores. The numbers are bigger than they were a year ago, the model is the new state-of-the-art on whichever evaluation the lab chose to highlight, and the headline writes itself. The honest summary is that most of these numbers have stopped measuring what they were designed to measure, and the gap between benchmark performance and real-world capability is now wide enough that the benchmark-led narrative is actively misleading.

## TL;DR

- The most-cited benchmarks - [**MMLU**](https://arxiv.org/abs/2009.03300), **GSM8K**, **HumanEval**, and most of the early reasoning benchmarks - are **functionally saturated** at the frontier. Top models cluster within a few points of each other and within a few points of the ceiling.
- **Contamination is rampant.** Independent reproduction studies estimate [MMLU scores are inflated by 8-15 points](https://digiterialabs.com/ai/insights/model-benchmarks-reality-check) on frontier models due to training data overlap. MMLU questions have been found verbatim in Common Crawl, the primary pre-training corpus.
- The replacement benchmarks - **MMLU-Pro**, **GPQA Diamond**, **SWE-Bench Verified**, **Humanity's Last Exam** - have helped but the same dynamics are appearing. MMLU-Pro is approaching saturation. SWE-Bench Verified scores are converging at the frontier. Each new harder benchmark survives roughly 18-24 months before the same problems recur.
- **Public benchmarks no longer differentiate the frontier models on most production-relevant dimensions.** Real-world capability differences between Claude Opus 4.7, GPT-5.5, and Gemini 3 Ultra are measurable in production deployments but not legible in the headline numbers.
- The labs that take evaluation seriously have moved to **internal eval suites**, **agentic benchmarks**, **head-to-head deployment trials**, and **continuous online evaluation** of production traffic. The public benchmark game is mostly marketing now.
- For builders, the practical implication is to **stop selecting models by leaderboard** and start running workload-specific evaluations against your own data. The cost of running a proper eval has fallen dramatically and the value of doing so has risen at the same rate.

## How we got here

The benchmark culture in AI is downstream of how the field developed. The early ML community was small, the problems were well-defined, the datasets were curated, and competing on a shared benchmark was a useful coordination mechanism for measuring progress. ImageNet, MNIST, the various GLUE benchmarks, the early QA datasets - all of these worked because the community was small enough to be self-policing about contamination, the tasks were narrow enough to be unambiguous, and the gap between the state-of-the-art and the ceiling was wide enough that any improvement was meaningful.

That world has stopped existing. The current AI ecosystem has commercial pressures that did not exist when the benchmark culture was formed. The training datasets are large enough and unfiltered enough that contamination is unavoidable unless you actively prevent it. The labs have an incentive to highlight whichever benchmark they happen to lead on this quarter. The benchmarks that were designed to distinguish good models from great ones now have ceilings that the great models routinely hit.

The trajectory has been visible for several years. [MMLU saturated in 2024](https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough). GSM8K saturated shortly after. HumanEval became uninformative once the labs started training on code corpora that contained the test set. The community has responded by building harder benchmarks - MMLU-Pro, GPQA, SWE-Bench, ARC-AGI, Humanity's Last Exam - and each one has either saturated or shown signs of contamination within 18 to 24 months of release.

## The contamination problem

The single most under-discussed problem in the current eval landscape is data contamination. The framing is straightforward: if a model has seen the test questions during training, the model's score on those questions is not a measure of capability but a measure of memorisation. The empirical question is how much contamination there actually is.

The recent studies on this are stark. The [Digiteria Labs reproduction study](https://digiterialabs.com/ai/insights/model-benchmarks-reality-check) found that MMLU scores are inflated by 8 to 15 points on average across frontier models released in the last six months. Every model tested showed statistically significant training data overlap with at least three of the five most-cited benchmarks. The estimated contamination rate on MMLU exceeds 12% of test questions for some models. MMLU questions have been found verbatim in Common Crawl, which is the primary web-crawl dataset used in pre-training corpora.

The labs are not unaware of this. Several have responded by holding out test sets, by paraphrasing test questions, by adversarial filtering of training data, and by maintaining private evaluation suites. The practical reality is that these mitigations are partial, that the public benchmarks reflect them inconsistently across labs, and that the resulting numbers are comparable to each other only with significant caveats that almost never appear in the marketing materials.

The deeper problem is structural. Benchmarks live on the public internet. Models are trained on the public internet. The only ways to break the loop are either to keep the benchmark private (which destroys its value as a community coordination mechanism) or to publish the benchmark after the training cutoff (which only works once). Neither approach has been adopted consistently, and the current eval landscape reflects the resulting compromise.

## The saturation problem

The other structural problem is saturation. Once a benchmark's frontier scores are within a few percentage points of the ceiling, score differences at the top stop carrying information about capability differences between models.

| Benchmark | Frontier range (early 2026) | Still informative? | Main failure mode |
|---|---|---|---|
| MMLU | 90–93% | No | Saturation; heavy contamination |
| GSM8K | 95%+ | No | Saturation; training overlap |
| HumanEval | 90%+ | No | Test-set leakage in code corpora |
| MMLU-Pro | ~88–90% | Fading | Approaching saturation |
| GPQA Diamond | 87–90% | Partially | Frontier convergence |
| SWE-Bench Verified | 75–82% | Partially | Agentic but gaming risk rising |
| Humanity's Last Exam | ~37% best model | Yes | Young; contamination risk ahead |
| WebArena / OSWorld | Wide spread | Yes | Hard to contaminate; action-space evals |

The headline benchmarks have stopped being useful for distinguishing the top three or four models, which are the models anyone making a real production decision is actually choosing between.

The harder benchmarks designed to delay saturation have helped, but only briefly. **Humanity's Last Exam** - 2,500 questions designed by domain experts at the edge of academic knowledge - drops the best model to roughly 37.5% as of early 2026. That is currently informative. It will probably stay informative for 18 to 24 months. The empirical pattern is that any benchmark good enough to be useful gets saturated within two years of release, and the community has not yet developed a sustainable answer to this dynamic.

The reason this matters in practice is that vendor marketing continues to cite saturated benchmarks as if the numbers still meant something. A model launch claiming "state of the art on MMLU" in 2026 is making a claim that has no decision-relevant content. The job of the reader is to know which benchmarks are still informative and which have effectively retired, and the labs have not been generous about disclosing this.

## What real evaluation looks like now

The labs that take evaluation seriously have moved away from public benchmarks as the primary basis for model decisions. The current state of the art in serious evaluation has several components.

**Workload-specific eval suites.** The most important shift in serious evaluation is that you write evaluations for your specific workload, on your specific data, in the conditions that will obtain in production. The eval is not a number that says "this model is good" - it is a number that says "this model is good for this thing I am building." The cost of running these evals has fallen dramatically in 2025-2026 as the tooling has improved (LangSmith, Braintrust, Weights & Biases, Anthropic's evals tooling, OpenAI's evals product), and the value of doing so has risen as the public benchmarks have become less informative.

**Agentic benchmarks.** The category of tasks that requires multi-step reasoning, tool use, and long-horizon planning has become the most important new benchmark frontier. SWE-Bench Verified is the canonical example, but the broader family includes WebArena, OSWorld, GAIA, and a growing list of others. These are harder to contaminate (the action space is large and the test environments evolve), harder to game (the scoring depends on actual task completion rather than text generation), and harder to saturate (the ceiling is genuinely high). Agentic benchmarks are the most active area of evaluation research and the area where the next two years of progress is most likely to be measurable.

**Head-to-head deployment trials.** Most serious enterprise deployments now do head-to-head trials between candidate models on real production traffic, with human raters or with rubric-based automatic scoring of the actual outputs. The trials are expensive but they are the only way to get a defensible answer to the question of which model is best for a specific workload. The labs have started shipping tooling to make this easier - the inference-time A/B testing tools, the structured-output scoring frameworks, and the per-request telemetry that lets you compare models across the same input distribution.

**Continuous online evaluation.** The serious production deployments run continuous evaluation of their inference traffic against quality rubrics, with alerting on regressions and automated routing to the model that is currently performing best for a given workload type. This is the deployment pattern that most clearly reflects the post-leaderboard era - the question of which model is best is answered in production, on real data, on a continuous basis, rather than at the point of model selection.

## What the labs actually use internally

The interesting question for anyone trying to understand which model to pick is: what evaluations do the frontier labs themselves use to decide which model to ship? The answer is partially public and mostly not.

The public part of the answer is that all of the frontier labs maintain large internal eval suites - typically hundreds to thousands of evaluations across capability categories - that are used to gate model releases. These suites include the public benchmarks but are dominated by private evals built around specific capabilities the labs care about. The release decision is gated on aggregate movement across the private suite rather than on movement on any single public number.

The non-public part is what is in those suites and how the evals are weighted. The labs do not publish this, partly for competitive reasons and partly because the evals themselves would become contamination targets if they were public. The result is that the most decision-relevant evaluation work in the AI industry happens behind closed doors and the public benchmark numbers are the part of the iceberg above the waterline.

The implication for outsiders trying to understand model capability is that the public benchmarks are now best read as marketing artefacts rather than as evidence. The serious evaluation work exists but it is not what is in the press release.

## What this means for builders

The practical guidance has three parts.

**Stop selecting models by leaderboard.** If you are picking between Claude Opus 4.7, GPT-5.5, Gemini 3 Ultra, and one of the open-weight frontier models, the public benchmark scores will tell you those four models are approximately equivalent. The real differences will show up when you run them against your specific workload. Build a small workload-specific eval - a few hundred examples is enough for most use cases - and run all four against it. The result will be more informative than any number you can read on a leaderboard.

**Treat agentic benchmarks more seriously than capability benchmarks.** The most important capability differences between frontier models in 2026 are on long-horizon, multi-step tasks. The single-shot capability benchmarks (MMLU, GPQA, even most SWE-Bench variants) do not capture the differences that matter for production agentic workloads. SWE-Bench Verified, WebArena, GAIA, and the various proprietary agentic benchmarks the labs themselves use are better signals.

**Invest in continuous online evaluation.** The deployment pattern that wins in the post-leaderboard era is the one where you keep evaluating your traffic continuously, route between models based on observed performance, and remain ready to switch when something better appears. The cost of building this is now reasonable, the tooling has improved significantly, and the value compounds over the life of the deployment.

## The controversial parts

Three claims in the eval conversation deserve more pushback than they typically get.

The first is the claim that public benchmarks are useless. They are not. They are useful as a coarse filter and as a way to verify that a model is in the right capability class. The problem is not that they have zero information but that they have less information than the marketing implies, and that the information they have is concentrated in the lower-tier capability distinctions rather than the frontier distinctions that matter for production model selection.

The second is the claim that the contamination problem is a solved engineering issue. It is not. The mitigations the labs use are partial, the disclosure about which mitigations are applied is inconsistent, and the empirical evidence from independent reproduction studies suggests the actual contamination remains significant. The framing that says "the labs have figured out contamination" is wrong and it leads to overconfidence in the public scores.

The third is the claim that the right response is to build harder benchmarks. The track record suggests this is a treadmill rather than a solution. Every harder benchmark gets saturated within two years. The structural answer is not a harder static benchmark but a different paradigm for evaluation - private evals, continuous evaluation, workload-specific assessment, and reduced reliance on shared static evaluations as the basis for decisions.

## Where this is heading

The most likely shape of 2027 is that the public benchmark landscape becomes increasingly performative - a marketing surface where the labs continue to claim state-of-the-art on whichever evaluation they happen to lead on this quarter - while the actual model-selection decisions move further into private, workload-specific evaluation. The infrastructure for serious evaluation will continue to improve and the gap between the leaderboard view of capability and the production view of capability will continue to widen.

The other prediction worth making is that agentic and tool-use benchmarks will become the most important public evaluations of the next year. The reason is that these are the dimensions where the frontier models actually differ in production-relevant ways, and the existing benchmarks in this category are sufficiently young that they have not yet been saturated or contaminated to the same degree as the older capability evaluations.

For people building with AI today, the practical guidance is the boring version of the exciting story. Build your own evals. Run candidate models against your own data. Trust your eval set more than the leaderboard. Update your evals when the model landscape changes. Treat the public benchmarks as one signal among many and not as the basis for the decision. The labs are doing this internally. The serious enterprises are doing this externally. The leaderboard-driven decision-making is the part of the AI industry that has aged worst between 2023 and 2026, and the move away from it is the most important methodological shift in serious AI deployment.

## What to do instead: a minimal workload-eval checklist

If you are starting from zero, this is enough to stop picking models by leaderboard:

1. **Collect 50-200 real examples** from production logs, support tickets, or actual user sessions - not synthetic prompts you wrote in a hurry.
2. **Write a rubric per example** - what a good answer must include, what it must not do, and which tools it should or should not call.
3. **Run every candidate model 10+ times per example** - agents are non-deterministic; a single pass tells you almost nothing.
4. **Score agentic tasks on the trajectory**, not just the final answer - which tools were called, in what order, with what arguments. A correct endpoint reached through a reckless path is a failure you will see in production.
5. **Track regressions statistically** - a 5-point drop across 100 trials is real; one failed demo is noise.
6. **Re-run when anything material changes** - model version, prompt, tool surface, or retrieval corpus.
7. **Keep a held-out set you never tune against** - otherwise you are just overfitting your eval to your current stack.

That is the whole playbook. The tooling (LangSmith, Braintrust, Weights & Biases, Anthropic Evals, OpenAI Evals) makes steps 3-5 easier than they were a year ago, but the structure is the same regardless of vendor.

For multi-step agents specifically, endpoint scoring is not enough. Step-level scoring and replay harnesses are the next layer - see [Evaluating Agents in Production: Trajectory Metrics](/ai/evaluating-agents-in-production-trajectory-metrics/).

## Related Reading

- [What I'm Researching in AI Right Now](/ai/what-im-researching-in-ai-right-now/) - where trajectory evaluation sits on my research map.
- [Securing AI Agents: Tool-Calling Risks, MCP Hardening, and the Confused Deputy Problem](/ai/securing-ai-agents/) - the trust problem from the adversary side.
- [AI Reliability Is Weird: Why Testing LLMs Breaks Everything You Know](/ai/ai-reliability-is-weird/) - the closely-related testing-and-quality story for production LLM systems.
- [The State of Open-Weight Models in 2026: Llama, Qwen, Mistral, DeepSeek](/ai/state-of-open-weight-models-2026/) - the model landscape these evals are supposed to be measuring.
- [Reasoning Models in 2026: o3, R2, and the Compute-at-Inference Shift](/ai/reasoning-models-2026/) - the capability category that has driven much of the recent benchmark saturation.
- [AI Hallucinations: Understanding and Mitigating False Outputs](/ai/ai-hallucinations-understanding-and-mitigating/) - the failure mode that benchmarks particularly badly capture.
- [Claude Mythos: The AI Benchmark Breaker That Won't Be Released](/ai/claude-mythos-benchmarks/) - the broader story of how benchmark-leading models do not necessarily become production models.
