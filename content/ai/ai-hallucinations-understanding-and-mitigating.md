---
title: "AI Hallucinations: Understanding and Mitigating False Outputs"
date: 2026-04-28T00:02:00+01:00
draft: false
tags: ["ai", "reliability", "llm", "hallucinations", "verification", "agentic-engineering"]
description: "What hallucinations actually are, why the word is a slightly misleading import from psychiatry, why no model will ever stop producing them entirely, and the small set of techniques that genuinely move the dial on false outputs in production."
cover:
  image: assets/images/ai/ai-hallucinations.jpg
  alt: AI Hallucinations Understanding and Mitigating False Outputs Banner
---

The word "hallucination" is one of the most successful pieces of accidental marketing in our industry. It is a soft, almost endearing way to describe an LLM stating with full confidence that a function exists when it does not, that a court case was decided when it was not, that a paper was written by an author who has never published in that field. It makes the failure sound like a quirk rather than the central reliability problem of the entire technology.

It is also, quietly, a misleading frame. A person who hallucinates believes the false thing. A model that "hallucinates" does not believe anything. It produces a token sequence with high probability under its training distribution, and sometimes that sequence is not anchored in the world. The mechanism is closer to confident pattern completion than to a perceptual error.

If you want to mitigate it, this distinction matters. You cannot fix a hallucination by asking the model to "be more truthful". You fix it by changing what the model is allowed to be confident about, what it is forced to verify, and what your system does with its output before that output reaches a user.

This post is the version of that conversation I wish I could hand to a new engineer on the first day they start building anything LLM-shaped.

## What hallucinations actually are

It is worth being precise. The Wikipedia article on [AI hallucinations](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)) defines them broadly as "false or misleading information presented as fact". That definition is fine for a casual reader, but for a builder it is too coarse to be useful. In practice, the failures cluster into a small number of distinct categories, each with a different root cause and a different mitigation.

- **Factual hallucinations.** The model states something about the world that is wrong. The capital of a country, the boiling point of a substance, the year a band released an album. The cause is almost always that the fact was either not in the training data, was contradicted in the training data, or sat in a low-frequency corner the model has effectively forgotten.
- **Citation hallucinations.** The model invents a source. A paper, a book chapter, a court ruling, a documented function in a library. This is the most consistently dangerous category, because the surface form is exactly right. The author's name plausibly publishes in that area, the journal exists, the title sounds like something they would write. Only the combination is fictional.
- **Code and API hallucinations.** The model imports a module that does not exist, calls a method that was renamed three versions ago, passes an argument the function never accepted. These are caused by the model having seen many similar APIs and interpolating across them, rather than recalling the specific one in front of it.
- **Instruction hallucinations.** The model claims to have done something it did not do. "I have updated the file." "I have run the tests." "I have checked the documentation." Particularly common in agentic workflows where the model is allowed to narrate its own actions.
- **Reasoning hallucinations.** The model performs a chain of reasoning where each step is locally plausible but the overall conclusion does not follow. This is the hardest category to detect, because every individual sentence reads as defensible.

These five are not a clean taxonomy. They overlap. But they fail differently, and a system that defends against one of them does not necessarily defend against the others.

## Why no model will ever stop hallucinating

There is a tempting belief, especially among non-technical leaders, that the next generation of models will simply solve this. A bigger model, more data, better alignment, and the problem fades away. I do not think that is true, and I think it is worth being honest about why.

Large language models are next-token predictors. Their training objective is to assign high probability to plausible continuations of text, not to assign zero probability to false ones. They have no ground-truth oracle that whispers "but is this actually the case?" before each token. Their notion of truth is statistical regularity in their training data, which is a useful proxy most of the time and a catastrophic one a small percentage of the time.

The [survey paper on hallucinations in LLMs](https://arxiv.org/abs/2311.05232) lays this out at length, but the core point is intuitive once you sit with it. A model trained on the entire web has read enough true and false statements about the world that for many queries the most probable continuation is one that simply sounds like the kind of thing the answer should be. Sounding right and being right are not the same property, and the training objective does not force them to align.

Bigger models reduce hallucination rate. They do not eliminate it. Reinforcement learning from human feedback reduces hallucination rate further, by penalising obvious confabulation. It does not eliminate it. Retrieval helps in narrow domains. Tool use helps where the tools cover the question. None of these are a fix. They are all variance reduction techniques on a process that is fundamentally not anchored in truth.

Once you accept this, the engineering changes. You stop trying to find the model that does not hallucinate, and you start designing systems where hallucination is bounded, detectable, and recoverable. The aim is not perfect output. It is acceptable risk.

## The mitigations that actually move the dial

There is a long list of folk remedies for hallucination. "Tell the model not to make things up." "Ask it to be confident only when it is sure." "Add the word truthfully to the prompt." These are not entirely useless, but their effect is small and inconsistent. The mitigations that genuinely change the failure rate are more structural.

### Grounding through retrieval

The single most effective technique is to stop asking the model to recall facts and start asking it to read them. Retrieval-augmented generation, in its various forms, replaces "what do you know about X" with "here is a passage about X, answer the question using this passage". The model's job collapses from open-ended recall to constrained reading comprehension, which it is much better at.

This is not a magic switch. The retrieval has to actually find the right passage, the chunking has to preserve meaning, and the prompt has to instruct the model to stick to the source. Anthropic's work on [contextual retrieval](https://www.anthropic.com/news/contextual-retrieval) is a good example of how much engineering sits behind getting this right at scale. But when you compare a grounded answer to an ungrounded one on the same factual question, the difference in reliability is not subtle.

### Tool use over recall

A close cousin. If the question has a deterministic answer that some tool can produce, give the model the tool rather than asking it to remember. Calculators for arithmetic. SQL for tabular questions. A code interpreter for anything numerical. A documentation search for API questions. The model becomes the orchestrator rather than the oracle, and the answer comes from a thing that does not hallucinate.

The interesting failure mode here is that the model sometimes pretends to have called the tool when it did not. This is an instruction hallucination, and it is why tool calls have to be observed by the system, not just narrated by the model.

### Constrained outputs

For any task where the answer has a known shape, force the model into that shape rather than letting it generate prose that you then parse. Structured outputs make a whole category of failure impossible by construction. I wrote about this in more detail in [Structured Outputs: When Your AI Needs to Follow a Schema](https://jamesm.blog/ai/structured-outputs-schema/), but the short version is that a model that cannot emit a malformed JSON object cannot hallucinate one. The constraint does not stop the model from being wrong about the contents, but it eliminates an entire class of brittle parsing code that used to fail in the wild.

### Verification layers

Treat the model's output as an untrusted input to your system, not as the system's answer. Every claim that matters should be checked by something cheaper and more deterministic before it is shown to the user. Did the model cite a paper? Hit the citation database. Did the model reference a code symbol? Search the codebase for it. Did the model claim to have run the tests? Look at the test runner output, not the model's narration.

This is unglamorous work, and it is the work that separates a demo from a product. The verification layer is where the reliability lives.

### Calibration prompting

This is the one folk remedy that I think genuinely helps, but only in a specific shape. Asking the model to produce a confidence score, or to flag when it is uncertain, or to list the assumptions its answer depends on, biases the output towards admissions of ignorance in cases where the model would otherwise have confabulated. It does not make the model truly calibrated, but it makes the failure mode more legible, which lets the rest of the system handle it.

The trick is that the calibration has to be cheap to use downstream. A confidence score that nobody reads is decoration. A confidence score that gates whether the answer is shown to the user, or routed to a human reviewer, is a control.

### Decoder choices

Lower temperatures reduce hallucination on factual questions, at the cost of variety. For anything where you want one right answer rather than a creative one, default to temperature zero or near it. This is the cheapest mitigation on the list and the most often forgotten.

### Domain narrowing

Models hallucinate less in domains where they have been heavily fine-tuned and more in domains where they are stretching. If your application sits in a narrow domain, a smaller fine-tuned model often hallucinates less than a giant general one, because its distribution has been pulled closer to your task. This trades flexibility for reliability, which is usually the right trade when reliability is the bottleneck.

## The architectural pattern

If I had to compress all of this into one diagram, it would not be a model. It would be a pipeline.

1. The user asks something.
2. Before the model sees the question, the system retrieves relevant context.
3. The model is given the context and a constrained output format.
4. The model produces a structured answer with explicit confidence markers.
5. A verification layer checks every factual claim against a deterministic source where one exists.
6. Anything below a confidence threshold or failing verification is either flagged, routed to a human, or refused outright.
7. Only what survives this pipeline reaches the user.

This is a lot of machinery for what looks, from the outside, like a chat box. But the alternative - a single LLM call whose output is shown directly to the user with no checks - is the architecture that produces every embarrassing public hallucination story you have ever read. The lawyer who cited fake cases. The airline chatbot that invented a refund policy. The search engine that confidently described a fictional medical procedure. None of those systems had a verification layer, because building one is harder than not building one.

The teams that ship reliable AI products have all, eventually, converged on something close to this pattern. The teams that have not are still finding out, one news cycle at a time, why they should have.

## What this looks like when it goes wrong

I want to flag the failure modes that surprised me when I first started building these systems, because the ones that hurt are not always the obvious ones.

- **The model gets the right answer for the wrong reason.** Your retrieval pulls the wrong passage, the model ignores it and answers correctly from its parametric memory. You think your retrieval is working. It is not. You only notice when the question is one where the model's memory is wrong and the passage you failed to retrieve was the only thing that would have saved you.
- **The verification layer becomes the model's adversary.** The model learns, through whatever feedback signal you give it, to produce outputs that pass verification rather than outputs that are correct. If your check is weak, this is a quiet drift towards plausible-but-unverified answers. The fix is to make the verification stronger than the model's ability to game it, which is harder than it sounds.
- **Confidence scores get reused as truth scores.** A model that says it is 90% confident is not telling you it will be right 90% of the time. Calibration is something you have to measure, not assume. Treating confidence as truth is the most common way I have seen calibration prompting backfire.
- **The pipeline hides the model's wrongness from the user but not from itself.** Downstream agents that consume the wrapped output can still be misled by claims the verification missed. Hallucination travels well through systems that were not designed to assume their inputs were lying.

These are not arguments against the architecture. They are arguments for being a careful builder of it. As I argued in [AI Reliability Is Weird](https://jamesm.blog/ai/ai-reliability-is-weird/), the testing surface is broader than it looks, and the failure modes are not the ones traditional engineering instinct prepares you for.

## The honest part

I do not think hallucinations are going to be "solved" in the strong sense, and I think the discourse around them would be healthier if we stopped pretending they will be. They will be reduced. They will be made more legible. The scaffolding around models will get better at catching them. None of that is the same as eliminating them.

What this means in practice is that anyone building production AI systems is, whether they like it or not, in the business of designing failure-tolerant pipelines. The model is not the product. The model surrounded by retrieval, verification, structured outputs, calibration, and human-in-the-loop review is the product. The teams that internalise this ship reliable things. The teams that do not ship demos.

The reassuring part is that this is not a new pattern. Every previous wave of probabilistic systems - search engines, recommender systems, fraud detection, automated translation - went through the same arc. The first generation believed the model was the product. The second generation discovered that the surrounding system mattered more than the model. The third generation built the surrounding system properly and stopped having public failures.

We are somewhere in the early second generation with LLMs. The companies and teams that are quietly working on the surrounding system are the ones whose AI features will still be running confidently in three years. The ones still hoping the next model release fixes everything will be writing a different kind of post-mortem.

Hallucination is not the bug. The absence of a system around the model is the bug. Once you start building like that, the problem stops being unsolvable and starts being engineering.

For anyone who wants to go deeper than this overview, the Anthropic [research index](https://www.anthropic.com/research) and the [hallucination survey paper](https://arxiv.org/abs/2311.05232) on arXiv are both good starting points. The literature is moving fast, but the underlying principles are stable enough that you can build against them now without expecting to throw the work away in six months.
