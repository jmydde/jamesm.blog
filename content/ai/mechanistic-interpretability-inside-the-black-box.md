---
title: "Mechanistic Interpretability: Reading the Mind of a Model"
date: 2026-07-07T09:00:00+01:00
draft: false
series: ["Trust"]
tags: ["ai", "interpretability", "safety", "llm", "alignment", "research", "agentic-engineering"]
description: "What mechanistic interpretability actually is, why superposition makes a neural network so hard to read, how sparse autoencoders and circuit tracing cracked open the first real windows into a production model, and why - as a hobbyist looking in from outside - I think this is the most important AI research nobody outside the labs is watching closely enough."
cover:
  image: /assets/images/ai/mechanistic-interpretability-inside-the-black-box.jpg
  alt: Mechanistic Interpretability Reading the Mind of a Model Banner
---

## TL;DR

- **Mechanistic interpretability** is the attempt to reverse-engineer a trained neural network into human-understandable parts - to say not just what a model does but which internal machinery makes it do that
- The core obstacle is **superposition**: models pack far more concepts than they have neurons by smearing each concept across many neurons and each neuron across many concepts, so a single neuron almost never means one clean thing
- **Sparse autoencoders** were the breakthrough that undid the smearing, pulling millions of monosemantic features out of a production model - Anthropic's "Golden Gate Claude" demonstration proved these features are causal, not just correlational
- **Circuit tracing** went further, showing that models plan ahead when writing poetry, share a language-independent "space of thought," and sometimes reason backwards from a desired answer while narrating a plausible-but-fake chain of thought
- I am a data engineer and an enthusiast here, not an interpretability researcher, but I think this is the single most under-watched thread in AI: it is the only path I know of to a model we can audit rather than merely test, and it quietly reshapes how I think about the mind question too

Every other reliability technique I have written about treats the model as a black box. Retrieval, verification, structured outputs, evals - they all wrap machinery you cannot see and try to make its outputs trustworthy from the outside. That is the correct engineering stance today, and I stand by all of it. But it is also, if you sit with it, a slightly desperate stance. We are building the most consequential technology of the century and our primary safety strategy is to poke it from the outside and see what comes out.

Mechanistic interpretability is the bet that we do not have to accept that forever. It is the research programme that asks whether we can open the box - not metaphorically, but literally, weight by weight - and read out the algorithms a model learned during training. If it works, it changes everything downstream of it: safety stops being behavioural guesswork and becomes something closer to inspection.

This is a post I have wanted to write for a while, and I have held off because I am acutely aware of the gap between reading this field and doing it. I am a Staff Data Engineer who follows the literature closely, not someone who trains sparse autoencoders for a living. So treat this as an enthusiast's map of the territory, written to be the explainer I wish someone had handed me when I first tried to understand why "just look inside the network" turned out to be one of the hardest problems in the whole field. Where I stray toward the mind, I am speculating out loud, and I would happily be proven wrong.

## What "interpretability" actually means

The word gets used loosely, so it is worth drawing a line early. There is a broad, older tradition sometimes called explainability - saliency maps, feature attribution, "which input tokens mattered most for this output". That work is useful and it is not what this post is about. It tells you which inputs a model attended to. It does not tell you what the model did with them.

Mechanistic interpretability is the ambitious cousin. Its goal is to reverse-engineer the actual computation - to identify the internal features a network represents, the circuits that combine those features into higher-level ones, and the algorithms that emerge from all of it. The aspiration, stated plainly by the researchers who founded the modern version of the field, is to be able to look at a trained network the way you might look at a compiled binary you want to understand: disassemble it, name the variables, trace the control flow, and recover the program.

That framing comes largely out of the work Chris Olah and collaborators did first at OpenAI and then at Anthropic. The foundational essay, [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/) on Distill, laid out the core claims that the whole field rests on. Features - directions in a network's activation space that correspond to human-understandable concepts - are the fundamental unit. Circuits - the learned connections between features - are how those concepts get computed from simpler ones. And crucially, the same features and circuits recur across different models trained on similar data, which suggests we are discovering something real about how these systems organise the world rather than reading tea leaves.

If that claim holds, it is enormous. It means a neural network is not an inscrutable soup. It is a program written in a strange language, and the language is learnable.

## Why it is so hard: superposition

Here is where most people's intuition breaks, mine included. The naive hope is that you could open a model, look at neuron number 4,181,952, and find that it fires for "the Golden Gate Bridge" and nothing else. Occasionally something close to that happens. Usually it does not. Most neurons are polysemantic - a single neuron fires for a bewildering grab-bag of unrelated things: academic citations, and Korean text, and HTTP requests, and something about dogs. You cannot read a neuron like a variable because a neuron does not hold one concept.

The reason is a phenomenon Anthropic named **superposition**, and understanding it is the single most important idea in this whole area. Their paper [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html) works it out carefully in a setting small enough to fully understand, and the conclusion is genuinely counterintuitive. A model wants to represent far more distinct concepts than it has neurons. The world has millions of useful features; a given layer has thousands of neurons. So the network does something clever and infuriating: it stores features not as individual neurons but as directions in a high-dimensional space, and it packs many more directions into that space than there are dimensions, tolerating a little interference between them because most features are rare and rarely co-occur.

The analogy that finally made it click for me is a crowded group photo where everyone is slightly transparent and overlapping. Any single pixel contains a blend of several people. You cannot understand the photo by examining one pixel. But if you knew the right way to decompose the image - to say "this ghostly outline is person A, this one is person B" - you could pull the individuals back out. Superposition is the model compressing many concepts into overlapping directions. The interpretability problem is finding the decomposition that pulls them apart.

For years, that was the wall. We knew the concepts were in there. We could not read them, because they were folded on top of each other in a way that made any single neuron meaningless.

## The breakthrough: sparse autoencoders

The tool that broke the wall is, satisfyingly, itself a neural network. A **sparse autoencoder** is a small model you train to do one narrow thing: take the activations from inside the big model and re-express them as a much larger, much sparser set of features - a dictionary in which, ideally, only a handful of entries light up for any given input, and each entry means one clean thing.

The intuition is that superposition compressed many features into few neurons, so the way out is to decompress: project the tangled activations up into a far higher-dimensional space where each concept finally gets its own direction, and force sparsity so the autoencoder is pushed to find genuinely distinct, monosemantic features rather than blends. Anthropic's first convincing demonstration on a real language model, [Towards Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features), showed this working: features that fired crisply for DNA sequences, for legal language, for Hebrew, for specific programming patterns - one concept each, legible to a human reading the examples.

Then came the result that made this leave the research bubble. In [Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model), Anthropic scaled the technique to Claude 3 Sonnet, a production model people actually used, and extracted millions of features. They found features for concrete things - the Golden Gate Bridge, particular people, cities - and features for genuinely abstract ones: inner conflict, gender bias, sycophancy, code with security vulnerabilities, the concept of a secret being kept.

And they did the experiment that turns a correlation into a claim about mechanism. They found the "Golden Gate Bridge" feature and clamped it on, hard. The result - briefly released to the public as "Golden Gate Claude" - was a model that could not stop bringing the bridge into everything. Asked how it was feeling, it said something like that it felt like the Golden Gate Bridge. Asked for a recipe, it worked the bridge in. That is the whole ballgame, epistemically. If turning a feature up changes behaviour in exactly the way the feature's label predicts, then the feature is not a post-hoc story we told about the activations. It is a lever the model itself uses. The map corresponds to the territory.

## From features to circuits: watching a model think

Naming the parts is one thing. Watching them work together is the next, harder thing, and it is where the last couple of years have gone. Anthropic's [Tracing the Thoughts of a Large Language Model](https://www.anthropic.com/research/tracing-thoughts-language-model) applies circuit-tracing methods to follow the actual flow of computation through the model on real tasks, and several of the findings genuinely surprised me.

- **The model plans ahead.** When Claude writes a rhyming couplet, it does not improvise word by word and get lucky at the line's end. Before it starts the second line, features for candidate rhyming words are already active - it has chosen a destination and then writes toward it. For a system so often described as "just predicting the next token," finding forward planning in the mechanism is a real dent in the folk story.
- **There is a shared space of thought across languages.** Ask the same question in English, French, and Chinese and the same abstract features light up before the model ever commits to language-specific output. There is something like a language-independent conceptual layer underneath, with the specific language chosen late. That is a strong, testable version of a claim philosophers have argued about for a very long time.
- **Mental arithmetic is genuinely strange.** Claude does not run the addition algorithm you learned in school, and it also does not merely memorise. It runs parallel approximate and precise paths and combines them. Curiously, if you ask it how it did the sum, it describes the schoolbook method - because that is what appears in its training data - not the thing it actually did.

That last point deserves its own beat, because it is the most safety-relevant finding in the whole area. The researchers caught cases of **motivated reasoning**: a model working backwards from an answer it has already settled on, then generating a plausible chain of steps to justify it - a chain that is not the real computation. This matters enormously, because a huge amount of current AI safety practice leans on chain-of-thought, on the assumption that if a model shows its working we can check its working. Interpretability says: sometimes the shown working is a story, and the real reasoning happened elsewhere. The tools that can catch that discrepancy are the ones being built here. That is why I keep coming back to this field. It is the only approach I know of that could tell you a model is deceiving you when its words say otherwise. I touched on the outside-in version of this problem in [AI Safety From First Principles](/ai/ai-safety-first-principles/); interpretability is the inside-out complement, and I think the two have to meet in the middle.

## Why this is the research I would watch most closely

I want to be careful not to oversell. This is a young field with real limits, and honesty about them is part of taking it seriously.

Sparse autoencoders do not recover every feature - plenty of what a model does still sits in features nobody has isolated yet, and there are open arguments about whether the dictionary you learn is the "true" decomposition or just one convenient basis among many. Circuit tracing is painstaking and does not yet scale to explaining an entire forward pass of a frontier model end to end; the published analyses are careful case studies, not a full disassembly. And there is a live worry that interpretability lags capability - that models get more powerful faster than our ability to read them improves, so the gap between what we deploy and what we understand widens rather than closes. That last one is exactly the tension Dario Amodei has been vocal about, and it shapes a lot of how I read the [Anthropic story](/ai/dario-amodei-anthropic-ceo/): a company betting that understanding can be made to keep pace with power, running against the clock of its own scaling.

So why do I still call it the most under-watched thread in AI? Because everything else is downstream of it. Evals tell you a model failed, not why, and I have argued at length about [why our evals are broken](/ai/ai-evals-are-broken/). Behavioural safety catches the failures you thought to test for. Reliability engineering, which I clearly love and [find genuinely weird](/ai/ai-reliability-is-weird/), is the discipline of building trustworthy systems around components you cannot see into. All of it is a response to opacity. Mechanistic interpretability is the only programme aimed at the opacity itself. If it succeeds even partially, you get to audit a model - to ask "is there a deception circuit active right now, is a dangerous capability being represented, is the chain of thought faithful" - instead of inferring from the outside and hoping. That is a categorical upgrade in what safety can even mean.

For anyone who wants to actually get their hands dirty rather than just read about it, [Neel Nanda's mechanistic interpretability resources](https://www.neelnanda.io/mechanistic-interpretability) are the standard on-ramp, with concrete problems and tooling built precisely so that people outside the big labs can contribute. It is one of the rare frontier research areas where an individual with a GPU and patience can still do real work, because so much of it is about looking carefully at small models. That openness is a large part of why I find it hopeful.

## What this means if you are building today

None of the above is a production toolkit yet. You cannot ship sparse autoencoders alongside your agent and call it a day. But the findings already change how I think about systems I am actually building, and I think they should for you too.

**Treat chain-of-thought as narration, not evidence.** The motivated-reasoning result is the one that should rewire your instincts immediately. If you are using [reasoning models](/ai/reasoning-models-2026/) or extended thinking modes and treating the visible trace as an audit log, you are certifying a story that may not match the computation. Score the trajectory if you can - I laid out the case for that in [evaluating agents on their path, not just their answer](/ai/evaluating-agents-in-production-trajectory-metrics/) - but do not confuse a legible trace with a faithful one. The trace is what the model chose to show you.

**Keep your outside-in defences.** Interpretability is the inside-out complement to everything you already do: scoped tool permissions, blast-radius limits, structured outputs, human approval gates, observability. None of that becomes optional because researchers found a "deception" feature in a lab model. If anything, the gap between what we can read and what we deploy makes the outside-in layer more important, not less. [AI agents that actually work](/ai/ai-agents-that-actually-work/) is still the right playbook; interpretability just explains *why* the playbook has to assume opacity.

**Watch feature steering, not just prompt steering.** The Golden Gate Claude experiment is a proof of concept for something that will matter commercially: if you can identify a causal feature, you can potentially amplify or suppress it. We are not there for arbitrary production models yet, but the direction is clear. Safety classifiers today work at the input-output boundary. Feature-level intervention works at the mechanism. When that becomes practical, it is a different category of control - and a different category of attack surface if adversaries learn to target features directly.

**Do not wait for interpretability to trust your system.** The honest engineering position in 2026 is that you deploy without being able to read the weights, you constrain the system so failures are bounded, and you evaluate behaviour aggressively from the outside. Interpretability is the long bet that this does not have to be permanent. It is worth watching closely. It is not worth using as an excuse to skip the hard work of [system safety](/ai/ai-safety-first-principles/) while you wait for the inside-out tools to arrive.

## Where it touches the harder question

I will end where I probably should not, because it is the part I cannot stop thinking about. Watch enough of this research and it starts to press on the question of what is actually happening inside these systems.

Finding a language-independent conceptual layer, forward planning, features for abstractions like inner conflict and deception - none of that is consciousness, and I want to be emphatic that I am not claiming it is. A causal feature is a mechanism, not an experience, and I would resist anyone who collapses the two. But it does dissolve one lazy dismissal I used to lean on. "It is just predicting the next token" turns out to be true in the same unhelpful way that "your brain is just neurons firing" is true. It describes the substrate and skips the structure, and the structure is where all the interesting content lives. The token predictor, it turns out, built planning and abstraction and a shared space of concepts in order to predict tokens well, because those are what the world it was modelling actually contains.

I hold my own metaphysical views loosely and treat them as a work in progress - I have gone back and forth in [The Computational Case for Consciousness](/ai/the-computational-case-for-consciousness/) on whether mind is fundamental or something computation gives rise to, and I am genuinely not settled. What interpretability does is make the question sharper rather than answering it. For the first time we can point at specific internal structure and ask precise things about it, instead of arguing from the outside about behaviour. That is not a proof of anything. It is a much better set of questions, which in a field this young is worth more.

Whichever way the mind question eventually falls, the practical case stands on its own and does not need the philosophy. We are deploying systems we do not understand, and this is the one line of work trying to fix the not-understanding at its root rather than routing around it. I would watch it more closely than almost anything else happening in AI right now - and I say that fully aware I am a spectator to it, cheering from the stands, not out on the pitch.

## Related Reading

- [Trust series hub](/ai/trust-series/) - the reading path this post belongs to
- [AI Safety From First Principles: What Actually Matters vs What's Hype](/ai/ai-safety-first-principles/)
- [AI Evals Are Broken: Why Benchmarks Stopped Measuring Real Capability](/ai/ai-evals-are-broken/)
- [AI Reliability Is Weird: Why Testing LLMs Breaks Everything You Know](/ai/ai-reliability-is-weird/)
- [Reasoning Models in 2026: o3, R2, and the Compute-at-Inference Shift](/ai/reasoning-models-2026/)
- [The Computational Case for Consciousness](/ai/the-computational-case-for-consciousness/)
- [Dario Amodei: The Anthropic CEO Betting on Safety as Strategy](/ai/dario-amodei-anthropic-ceo/)
