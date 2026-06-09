---
title: "Reasoning Models in 2026: o3, R2, and the Compute-at-Inference Shift"
date: 2026-05-08T19:00:00+01:00
draft: false
type: essay
tags: ["ai", "reasoning", "openai", "deepseek", "anthropic", "gemini", "inference", "2026"]
description: "A grounded look at the reasoning-model wave - what makes o3, DeepSeek R1/R2, Gemini Deep Think, and Claude Extended Thinking different from the generation that came before, when to actually reach for one, and what the cost and capability trade-offs look like in production."
cover:
  image: /assets/images/ai/reasoning-models-2026.png
  alt: Reasoning Models in 2026 - o3, R2, and the Compute-at-Inference Shift Banner
---

Two years ago the way to make a model better was to train a bigger one. By the start of 2026 that recipe has stopped being the most interesting answer. The frontier has moved to a different lever - letting the model think for longer at inference time, generating intermediate reasoning, and only then producing the final answer. The category has a name now (reasoning models) and a family of products built around it. The interesting questions are no longer whether the trick works, because it clearly does, but when to reach for one, where it lands in production, and what the costs actually look like once the demo glow wears off.

## TL;DR

- The reasoning-model wave began in late 2024 with OpenAI's o1 and went mainstream in 2025-2026 with **OpenAI o3**, **DeepSeek R1** and the R2 successor, **Gemini Deep Think**, and **Claude Extended Thinking**.
- The core mechanism is **test-time compute**: the model generates a long chain of intermediate reasoning before the final answer. The chain may consume tens or hundreds of thousands of tokens for a single hard problem.
- **Reasoning models trade time and tokens for accuracy.** They are slower, more expensive per task, and substantially better on problems that genuinely require multi-step reasoning. Use them for hard problems where being right matters more than being fast - mathematical derivations, complex coding refactors, scientific reasoning, structured argument analysis.
- **Use non-reasoning models for everything else.** Conversational interactions, simple lookups, content generation, anything where a competent first-pass answer is enough.
- The benchmark gains are real and large. [o3 scores 87.7% on GPQA Diamond](https://aiweekly.co/learning-ai/deep-learning/what-test-time-compute-how-ai-models-think-they-answer) (graduate-level science) and broke the ARC-AGI benchmark with 96.7% in its high-compute setting. DeepSeek R1 hit 79.8% on AIME 2024 at roughly 5% of o1's API price.
- The cost structure has flipped. In the high-compute regime, [o3 averages around 57 million tokens per question and roughly 14 minutes of runtime](https://aiweekly.co/learning-ai/deep-learning/what-test-time-compute-how-ai-models-think-they-answer) for the hardest problems. The economics of inference now look more like the economics of training.
- The category is splitting into **two product modes**: synchronous reasoning (the model thinks for seconds-to-minutes and returns an answer) and **agentic reasoning** (the model thinks across many tool calls and external interactions over hours).
- The deployment pattern that works is **hybrid routing** - send easy queries to fast models and hard queries to reasoning models, deciding at runtime which is which.

## What actually changed

The classical transformer model produces tokens left-to-right, one at a time, with the same fixed amount of compute per token. The only way to make the model better at a given task was to make the model itself larger or to train it on more data. That scaling regime delivered most of the gains of the 2020-2024 era.

The reasoning-model wave came from a different direction. Instead of making the model bigger, you let the model think for longer. The model is trained to generate a long internal chain of intermediate reasoning - exploring solution strategies, checking partial answers, backing up when something looks wrong - and only after this chain is done does it produce the final response. The internal chain is often not shown - the model thinks privately, then writes the response. The technical name for the lever is *test-time compute*, or sometimes *inference-time scaling*, and the empirical result is that you can trade compute at inference for capability on hard problems in a way that the older scaling regime did not allow.

The training is the part that matters. Reasoning models are post-trained, typically with reinforcement learning, to produce internal reasoning chains that are factually accurate, well-structured, and lead to correct conclusions. The chain itself is not a magic incantation - it is the result of significant training effort directed at making the model's own reasoning reliable.

The reason this is a big deal is that the curves are favourable. On a wide range of hard reasoning tasks - mathematics olympiad problems, graduate-level science, competitive programming, novel logic puzzles - adding inference compute keeps improving the score for far longer than was expected. The [o3 high-compute results](https://aiweekly.co/learning-ai/deep-learning/what-test-time-compute-how-ai-models-think-they-answer) on ARC-AGI are the most striking public demonstration of this - a benchmark that was specifically designed to be hard for current models was effectively saturated by spending substantial compute on each problem.

The other reason it is a big deal is that it works on much smaller base models than the brute-force scaling approach. DeepSeek R1, released in early 2025, demonstrated that you can get reasoning performance comparable to OpenAI's o1 with a model whose API pricing was roughly [3-5% of o1's](https://magazine.sebastianraschka.com/p/state-of-llms-2025). The R2 successor that followed in late 2025 narrowed the gap with the frontier further. The implication is that the reasoning capability is not locked behind frontier-scale training and that the open-weight ecosystem can compete on this dimension in a way it could not when the only lever was raw model size.

## The state of the frontier

The reasoning-model category in 2026 has four serious entrants and a longer tail of credible open-weight alternatives.

**OpenAI o3 and o4** are the current performance leaders on most public benchmarks. The o-series is what most teams reach for when they need state-of-the-art reasoning and are willing to pay for it. The high-compute setting is genuinely strong but very expensive - tens of millions of tokens per hard problem and runtimes measured in minutes. The low-compute setting is much cheaper and is what most production deployments actually use. OpenAI has also shipped **o3-mini** and **o4-mini** as smaller, faster variants for use cases that need reasoning without the full o3 cost structure.

**Anthropic's Claude Extended Thinking** is built into the Claude family rather than being a separate product. The extended-thinking mode gives [Claude](/ai/claude-opus-4-7/) deliberate internal reasoning steps; the same model can be invoked in fast mode for routine work. The Anthropic implementation is unusual in that it exposes the reasoning trace to the user by default, which has implications for both interpretability and how the product is used. The strength is integration with the rest of the Claude ecosystem - tool use, agentic loops, long context all work the same way regardless of thinking mode. The [Claude Opus 4.7](/ai/claude-opus-4-7/) release in early 2026 made significant gains on the agentic-reasoning end of the spectrum.

**Google Gemini Deep Think** is Google DeepMind's entry in the category, integrated into the Gemini Ultra tier. It has carved out the niche of strong reasoning at competitive pricing, with particular strength on multimodal reasoning problems - Gemini's reasoning over images, video, and audio is meaningfully ahead of the text-only reasoning competition. The 2.0 generation, shipped in late 2025, introduced significantly stronger long-horizon reasoning and tool use.

**DeepSeek R1 and R2** are the open-weight benchmark. R1 was released in January 2025 and demonstrated that reasoning performance comparable to o1 was possible at a fraction of the cost. R2 followed later in 2025 with significant improvements on coding and on longer-horizon reasoning. The models are available under permissive licences and have been adopted widely across the open-source ecosystem. The trade-off is that you have to run the inference yourself. Their existence is the single biggest reason the price floor for reasoning models has compressed so quickly.

Beyond these four, the open-weight ecosystem has shipped credible reasoning models from Qwen, Mistral, and several smaller research labs. The category is increasingly crowded and the gap between the frontier and the open alternatives is narrower on reasoning than it is on raw capability.

## The cost story is the story

The most underappreciated fact about reasoning models is how dramatically they change the cost structure of inference. The classical pricing model for an LLM API was a fixed cost per input and output token, and most production workloads consumed a small enough number of tokens per request that the cost was approximately constant.

Reasoning models break this. In the high-compute regime, a single hard problem can consume tens of millions of tokens of internal reasoning before producing a final answer. The runtime can stretch to minutes or longer. The cost per problem can rise into the dollars rather than the cents. The economics of inference, for hard problems, start to look more like the economics of small training runs than like the economics of classical API calls.

The practical implication is that reasoning models are not a drop-in replacement for the classical models on every workload. For an enormous fraction of production use cases - text generation, summarisation, classification, routine code generation, routine question answering - the marginal value of the reasoning capability is small and the marginal cost is large. The reasoning models are the wrong tool for these workloads and the smart deployment pattern is to keep the classical models in place for the bulk of traffic and route only the hard problems to the reasoning models.

## Where reasoning models actually win

The category wins on a specific shape of problem and is mediocre or wasteful on everything else.

**Hard reasoning problems with verifiable answers.** Mathematics, formal logic, competitive programming with test cases, scientific questions with structured answers. Word problems, derivations, statistical analysis, financial calculations - the kind of work where a small error early in the chain compounds into a wrong final answer. The reasoning chain has something to verify against and the model can self-correct when it goes wrong. The benchmark gains in this category are the largest and the most defensible.

**Long-horizon coding tasks.** Multi-file refactors, debugging subtle bugs, designing data structures - anything that requires holding multiple files, multiple constraints, and multiple steps in working memory while reasoning about the changes. The frontier reasoning models have transformed what you can ship in a single coding turn, and the [Claude Code](/ai/claude-code-vs-cursor/) and related agentic-coding products are built around this capability.

**Complex tool use and agentic workflows.** Tasks where the model has to plan a sequence of actions, execute them, observe the results, and revise the plan. The reasoning capability is what makes this work end-to-end without constant human intervention. The agentic deployments that work in 2026 are almost all built on top of reasoning models.

**Structured analytical work.** Financial analysis, legal reasoning, scientific literature synthesis. Reading a legal document and identifying the obligations, examining a contract for ambiguities, evaluating a logical argument. Tasks where the answer requires holding many constraints and structured arguments together. The reasoning models are markedly better at this than the classical predecessors and the gap is large enough to be commercially meaningful.

**High-stakes decisions where being right matters.** Cases where the cost of a wrong answer is high enough to justify the extra inference cost.

## Where they do not

The places where reasoning models add friction without value:

- **Conversational interactions.** The latency makes them feel slow and unnatural in chat.
- **Content generation.** Writing an email, drafting a blog post, creating marketing copy - a fast model produces work that is hard to distinguish from a slow one.
- **Simple lookups.** "What is the capital of Bolivia" does not benefit from extended thought.
- **Tool-heavy agentic loops where the bottleneck is orchestration.** When most of the work is calling tools and parsing results, the reasoning model's strength is wasted on the overhead.
- **Subjective tasks and creative writing** where the bottleneck is style rather than logic.

The hype around reasoning models has sometimes obscured how narrow the actual capability advantage is, and the production deployment patterns have started to reflect this. Using a reasoning model for everything is expensive and slow; using one for nothing leaves accuracy on the table for the cases that benefit.

## The hybrid pattern that works

The deployment pattern that most teams running serious production workloads have converged on is hybrid routing. A cheap, fast classifier model looks at the incoming request and decides whether it is a "hard" question that warrants reasoning-model treatment or a "routine" question that goes to a fast model. The decision is made in milliseconds; the routing is invisible to the user.

This is harder to operate than picking one model and using it for everything, but the economics are dramatically better. Reserving reasoning-model spend for the queries that actually need it - typically a small fraction of total traffic for most applications - keeps the cost manageable while preserving the accuracy benefit where it matters.

Teams running this pattern report 80-90% of queries handled by fast models and 10-20% routed to reasoning models. The split varies by domain. A coding assistant routes more to reasoning. A customer support bot routes less.

Several of the frontier providers now offer hybrid endpoints that automatically decide whether a given query needs the reasoning path or can be handled by the classical model. The accuracy of this routing layer is one of the more consequential factors in real-world cost-to-serve, and the labs are competing on it in ways that are not yet visible in the public benchmarks.

## The controversial parts

Four claims about reasoning models deserve more pushback than they typically get.

The first is the claim that reasoning models are a step toward AGI. The framing is appealing but the empirical case is weaker than it sounds. The benchmarks where reasoning models do best are benchmarks specifically designed to test the kinds of reasoning the models are now good at. The benchmarks where they do less well - long-horizon planning, novel-context generalisation, dealing with genuine ambiguity - are still hard for them. The progress is real but it is progress along a specific axis, not progress along all axes.

The second is the claim that the reasoning capability is fundamentally different from what came before. There is a credible technical argument that the long chain-of-thought is just a way of unlocking capability that was already latent in the base model, rather than a new capability per se. The training procedure that turns a base model into a reasoning model - large-scale reinforcement learning on reasoning traces with verifiable outcomes - is genuinely new, but the resulting model is on a continuum with the predecessors rather than a phase change away from them.

The third is the claim that test-time compute scales indefinitely. The [test-time compute paradox](https://www.arturmarkus.com/the-test-time-compute-paradox-why-reasoning-models-like-o1-and-deepseek-r1-are-proving-that-more-inference-compute-can-destroy-accuracy/) is real - in some regimes, adding more inference compute starts to hurt accuracy rather than help it. The model gets lost in its own reasoning, talks itself out of correct answers, or wastes compute on dead ends. The current frontier reasoning models have made significant progress on this but it has not been eliminated and the optimal amount of compute per problem is itself a hard tuning question.

The fourth is the claim that DeepSeek R1 and R2 prove that the open-weight ecosystem has caught up with the frontier. The benchmark numbers are real but the production reliability gap is larger than the benchmarks suggest. The frontier models from OpenAI, Anthropic, and Google have advantages in long-tail reliability, in tool integration, and in the surrounding infrastructure that do not show up in the public scores. The gap is closing but it has not yet closed, particularly on the hardest agentic workloads.

## Where this is heading

The reasoning-model era has split the LLM market into two related but distinct product categories. Fast models for the high-volume, latency-sensitive, accuracy-tolerant work. Reasoning models for the lower-volume, accuracy-critical work. The pricing reflects this, the architectures are diverging, and the labs are increasingly developing them as separate product lines. The 2026 application developer is no longer choosing "which model" - they are choosing which mix of models, with which routing logic, for which workloads.

The most likely shape of 2027 is that reasoning models become a normal part of the API surface rather than a distinct category, with the routing between reasoning and non-reasoning paths happening transparently at the provider level. The price differential between the modes will compress as the providers compete on cost-to-serve, and the deployment patterns will stabilise around the workload shapes that actually benefit from the capability.

The other prediction worth making is that the open-weight reasoning ecosystem will continue to compress the price floor faster than the frontier labs can keep up with on commercial pricing. The DeepSeek R2 release is the template - a reasoning model that is open-weight, available under permissive licences, and price-competitive with the frontier on most production workloads. The strategic implication for the closed labs is that the moat on reasoning capability is narrower than the moat on raw capability has been, and the differentiation has to come from somewhere other than the model itself.

The third prediction is that agentic deployments are going to drive most of the real-world reasoning-model demand by 2027. The early 2026 picture is that synchronous reasoning - the user asks a question and waits for the answer - is the dominant use case. The 2027 picture is more likely to be agentic reasoning - the model is doing extended work on the user's behalf, taking actions, observing results, and reasoning across long horizons. The compute demand from this shift is one of the things that is going to keep the [AI energy crisis](/ai/ai-energy-crisis-data-center-power/) at the centre of the conversation.

For people building with reasoning models today, the practical guidance is the boring version of the exciting story. Use them for the workloads where they win. Keep classical models for the workloads where they do not. Build the routing layer carefully because that is where the cost-to-serve actually lives. Expect the price-per-token in the high-compute regime to come down significantly over the next 18 months, and expect new capability gains to keep arriving from the open-weight side faster than the closed-lab marketing implies.

## Related Reading

- [The Rise of Small Language Models: Why Size Isn't Everything](/ai/small-language-models/) - the model-size counterpart to the test-time-compute story.
- [DeepSeek](/ai/deepseek/) - the lab whose R1/R2 releases reset the price floor for reasoning models.
- [Claude Opus 4.7: Autonomy and Vision at Scale](/ai/claude-opus-4-7/) - the agentic-reasoning story from the Anthropic side.
- [The LLM Context Window Arms Race: Does It Actually Matter?](/ai/llm-context-window-arms-race/) - the adjacent capability lever that reasoning models complicate.
- [Cerebras, Groq, SambaNova: The Inference Hardware Insurgents](/ai/inference-hardware-insurgents/) - the hardware story that reasoning models have made commercially significant.
