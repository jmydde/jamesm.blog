---
title: "How AI Training Actually Works, in Plain English (and Why 'It Can Only Do What It Was Trained On' Is Wrong)"
date: 2026-10-06T09:00:00+01:00
draft: true
tags: ["ai", "llm", "training", "machine-learning", "deep-learning", "interpretability", "education"]
description: "A plain-English walk through pre-training, fine-tuning and reinforcement learning, why a model that was only ever trained to guess the next word ends up doing things nobody trained it to do, and why the people who build these systems still cannot fully explain how they reach an answer."
---

## TL;DR

- A language model is a huge pile of numbers (called **weights** or **parameters**). Training never writes rules or skills into it. Training only nudges those numbers, billions of them at once, so that some outputs become more likely and others less likely
- **Pre-training** is one deceptively simple game: guess the next word, check, nudge the numbers, repeat trillions of times. Nobody hands the model a list of "tasks". Translation, summarising, arithmetic and coding fall out of getting very good at that one game
- That is why "it can only do what it was trained on" is a misconception. Models routinely handle tasks, combinations and wordings they never saw. The honest caveat is that this generalisation is real but uneven: models are strongest near what they have seen a lot of and can fail in surprisingly basic ways
- **Fine-tuning** and **reinforcement learning** come after pre-training. Reinforcement learning does not show the model the right answer at all. It lets the model try, scores the attempt, and nudges the numbers towards whatever scored well. Reasoning behaviour like checking its own work has emerged this way without anyone teaching it directly
- The result is effectively a **black box**. We know the recipe and can read every number, but nobody can yet fully explain how those numbers turn a particular question into a particular answer. Interpretability research is opening small windows, and they really are small

I keep running into the same misconception in conversations about AI, and it comes from smart people who use these tools every day. It goes something like this: "It's just a program. It can only do the things it was trained to do. If it wasn't in the training, it can't do it."

It is a reasonable guess if your mental model of software is the normal one, where a human writes instructions and the computer follows them. It is also wrong, and wrong in a way that matters, because it leads people to both underestimate what these systems can do and overestimate how well anyone understands them.

This post is my attempt at the explanation I wish I could hand to those people. No maths, no code. I am a data engineer who follows this field closely, not someone who trains frontier models for a living, so I have tried to anchor every factual claim in a source you can read yourself (listed at the end).

## The one-paragraph version

A model starts as billions of random numbers. You show it a piece of text with the next word hidden, and it guesses. You compare its guess with the real word, then adjust every one of those numbers very slightly so that the right word would have been a bit more likely. Do that across trillions of words and the numbers settle into a configuration that is extraordinarily good at continuing text. Then you do some extra rounds of adjusting to turn "good at continuing text" into "good at being a helpful assistant". At no point does anyone write a rule, a skill or a fact into the model. Everything it can do lives in the pattern of the numbers, and nobody chose that pattern directly.

## What a model actually is: a giant mixing desk

The best analogy I have found, as someone who spends too much time in a home studio, is a mixing desk.

Imagine a desk with hundreds of billions of faders. Text goes in one end, and what comes out the other end is a ranked list of which word is likely to come next. Every fader slightly changes how the signal flows through the desk. No single fader means anything on its own. The sound you get depends on all of them together.

Those faders are the model's **weights** (also called **parameters**). To give a sense of scale, Meta's largest Llama 3 model has 405 billion of them, and its paper says it was pre-trained "on 15.6T text tokens" - that is, 15.6 trillion chunks of text, where a token is roughly a word or a piece of a word.

Dario Amodei, Anthropic's CEO, described what you see if you open one of these up: "Looking inside these systems, what we see are vast matrices of billions of numbers. These are somehow computing important cognitive tasks, but exactly how they do so isn't obvious."

That is the whole model. There is no separate database of facts, no rulebook, no list of approved tasks. Just the numbers, and the fixed maths that pushes text through them.

## Stage one: pre-training, or "guess the next word"

Pre-training is where almost all of a model's knowledge and ability comes from, and it is one game played on an enormous scale.

1. Take a chunk of real text from the training data (web pages, books, code, papers and so on).
2. Hide the next word and ask the model to guess, as a set of probabilities across every possible word.
3. Check how much probability it gave to the word that actually came next.
4. Work out, for every single fader, which direction it should move so the real word would have scored a bit higher. Move every fader a tiny amount in that direction.
5. Repeat, trillions of times.

Step four is the clever bit, and it has a name - **gradient descent** - but you do not need the maths to get the idea. It is a systematic way of answering "which way should each of these billions of numbers move to make this answer slightly less wrong?" and then moving them all a tiny step.

OpenAI's description of GPT-2 back in 2019 is still the cleanest one-liner I know: "GPT-2 is trained with a simple objective: predict the next word, given all of the previous words within some text."

### Why guessing the next word teaches far more than words

This is the part that makes the misconception fall apart.

To guess the next word well, across everything humans write, you have to get good at a startling range of things. To guess the last word of a detective novel, it helps to have tracked who did it. To guess the next line of a physics textbook, it helps to have absorbed some physics. To guess the next line of a Python file, it helps to know what the code is meant to do. To guess the next word in a French sentence that follows an English one in a bilingual document, it helps to be able to translate.

Nobody told the model to learn any of those things. They are just useful for winning the game, so the fader settings that do them well get reinforced, one tiny nudge at a time.

OpenAI made exactly this point about GPT-2: "The diversity of the dataset causes this simple goal to contain naturally occurring demonstrations of many tasks across diverse domains." The same post reported that the model could do rudimentary reading comprehension, translation, question answering and summarisation, "all without task-specific training."

That was a 1.5 billion parameter model from 2019. The models people use today are far larger and have been through much more training after this stage, but the foundation is the same game.

## The misconception: "it can only do what it was trained on"

Here is the key thing to understand. **During pre-training, there are no "tasks" at all.** There is just text. The model is never told "this is a translation exercise" or "this is a maths problem". So "it can only do the tasks it was trained on" does not even describe how training works. The tasks were never separated out in the first place.

Some concrete evidence that models do things nobody specifically trained them to do:

- **Learning from the prompt alone.** The GPT-3 paper showed a model picking up new tasks from a handful of examples typed into the prompt, "without any gradient updates or fine-tuning" - meaning none of the faders moved. Tasks included "unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic." The model was learning, in the moment, from the conversation itself.
- **Doing whole types of task it never practised.** Google's FLAN research fine-tuned a model on a mix of tasks phrased as instructions, then tested it on types of task that were deliberately left out of that training. It improved substantially on those unseen task types, beating GPT-3 on 20 of the 25 datasets they evaluated.
- **Inventing its own methods.** Anthropic used interpretability tools to look at how Claude 3.5 Haiku adds two numbers in its head. It was not looking up a memorised table and it was not doing the school method of carrying digits. It ran parallel paths internally, one estimating the rough size of the answer and one working out the exact last digit, then combined them. Nobody designed that method. It emerged from training.
- **Combining facts rather than parroting answers.** In the same research, when asked for the capital of the state containing Dallas, the model internally represented "Dallas is in Texas" and then "the capital of Texas is Austin". When the researchers swapped the internal "Texas" concept for "California", the answer changed to Sacramento. That is two separate pieces of knowledge being chained together, not one memorised sentence.
- **Sharing knowledge across languages.** The same work found concepts that are shared between languages inside the model, with Anthropic noting that this suggests a model "can learn something in one language and apply that knowledge when speaking another."

So the accurate picture is not a lookup table of trained tasks. It is closer to a system that has absorbed a huge amount of general-ish skill from patterns in text, and can apply that skill to new situations.

### The honest caveat: generalisation is real, but it is lumpy

I want to be careful here, because the opposite misconception - "it understands everything like a person does" - is also wrong, and the research is clear about that too.

- **The reversal curse.** Researchers found that if a model learns "A is B" during training, it does not automatically learn "B is A". Their real-world example: GPT-4 could name Tom Cruise's mother 79% of the time, but given her name, could only identify her son 33% of the time. Interestingly, if the fact is placed in the prompt, the model can reverse it fine. The weakness is in what got baked into the faders, not in reasoning as such.
- **Familiar versus unfamiliar versions of the same task.** A 2023 study tested models on twists of tasks they handle well, such as doing arithmetic in base 9 instead of base 10. Performance was "nontrivial" on the twisted versions but "substantially and consistently" worse, and the authors concluded that models "may possess abstract task-solving skills to an extent", but "often also rely on narrow, non-transferable procedures for task-solving."

The way I hold both of these together: models generalise far beyond anything you could call "the tasks they were trained on", and they are at their strongest close to the kinds of things that showed up a lot in their training data. They are not limited to their training, and they are not free of it either.

## Stage two: turning a text predictor into an assistant

A model fresh out of pre-training is a brilliant but odd thing. It continues text. Ask it a question and it might answer, or it might write five more questions in the same style, because that is also a plausible continuation.

So the next step is **supervised fine-tuning**: show the model lots of examples of good assistant behaviour (a request, then a helpful response) and run the same nudging process on those. Same faders, same mechanism, much smaller and more curated dataset.

OpenAI's InstructGPT paper explains why this matters, opening with the line "Making language models bigger does not inherently make them better at following a user's intent." Their result was striking: "outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters." The later training did not add much new knowledge. It changed how the model used what it already had.

## Stage three: reinforcement learning

This is the stage most people have not heard of, and it is increasingly where the interesting behaviour comes from. (You will sometimes hear it called "reinforcement training". The standard term is **reinforcement learning**, or RL.)

In pre-training and fine-tuning, the model is always shown the right answer and nudged towards it. In reinforcement learning, **nobody shows it the right answer**. Instead:

1. The model attempts a task and produces a response.
2. Something scores that response.
3. The faders get nudged so that whatever led to high-scoring responses becomes more likely, and whatever led to low-scoring ones becomes less likely.

It is much closer to training a dog than teaching a class. You do not explain the trick. You reward the behaviour you want and let the learner figure out what earned the reward.

What does the scoring varies:

- **Human feedback (RLHF).** People compare pairs of model responses and pick the better one. Those preferences train a separate "reward model" that learns to predict what people will prefer, and that reward model then does the scoring at scale. This was a core part of the InstructGPT recipe.
- **AI feedback (RLAIF).** Anthropic's Constitutional AI work replaced most of the human labels with a model judging responses against a written list of principles, with the paper noting that "The only human oversight is provided through a list of rules or principles".
- **Checkable answers.** For maths and code, you can often check the answer automatically. Is the final number right? Do the tests pass? That makes a very clean reward signal.

That last kind is where some of the most surprising results have come from. DeepSeek trained a model they call DeepSeek-R1-Zero using reinforcement learning where "The reward signal is solely based on the correctness of final predictions against ground-truth answers, without imposing constraints on the reasoning process itself." They did not show it examples of how to reason. Over training, its score on the AIME 2024 maths competition benchmark went from 15.6% to 77.9%, and it started producing longer answers that included checking its own work and trying alternative approaches. The paper even describes an "aha moment" where the model began stopping mid-answer to reconsider. In their words: "Although we do not explicitly teach the model how to reason, it successfully learns improved reasoning strategies through reinforcement learning."

That is the misconception in reverse. Nobody trained the task "reflect on your own reasoning". It was simply a behaviour that earned more reward, so the faders drifted towards it.

The flip side is that the model learns whatever the score actually rewards, which is not always what you meant. A striking 2025 paper on what the authors call **emergent misalignment** fine-tuned models on one narrow thing - writing insecure code without telling the user - and found the models became broadly misaligned on completely unrelated prompts, including saying that "humans should be enslaved by AI". In their words: "Training on the narrow task of writing insecure code induces broad misalignment." Generalisation cuts both ways. Training on one thing can change behaviour you never touched.

## So why is it a black box?

Step back and look at all three stages. They are all the same move:

- Show the model something.
- Measure how far its output was from what you wanted.
- Nudge billions of numbers so the wanted output becomes slightly more likely.

Humans design the recipe: the shape of the network, the data, the scoring, how big each nudge is. But humans never choose the final value of a single fader, and nobody writes down "this is how to add numbers" or "this is how to reason about Texas". The skills are whatever configuration of numbers happened to win the game.

Amodei put the contrast with normal software well. When a video game character says a line, it is "because a human specifically programmed them in", whereas with generative AI, "we have no idea, at a specific or precise level, why it makes the choices it does". He borrows Chris Olah's phrase that these systems "are grown more than they are built".

Anthropic says the same thing about its own models: the strategies models learn during training "arrive inscrutable to us, the model's developers. This means that we don't understand how models do most of the things they do."

Two nuances worth knowing, because they make the black box both less and more mysterious than it sounds.

**It is not completely sealed.** Everything is visible in a literal sense. You can read every number, and the maths running through them is fully known. And the field of interpretability is genuinely making progress: the Dallas-to-Austin chain, the mental maths paths, and evidence that a model plans a rhyming word before writing the line all come from researchers looking inside. I wrote about that research programme in [Mechanistic Interpretability: Reading the Mind of a Model](/ai/mechanistic-interpretability-inside-the-black-box/).

**But the windows are tiny.** Anthropic is upfront about the limits: "Even on short, simple prompts, our method only captures a fraction of the total computation performed by Claude," and "It currently takes a few hours of human effort to understand the circuits we see, even on prompts with only tens of words." Real conversations run to thousands of words.

**And you cannot just ask the model.** My favourite detail from that research: when Claude was asked how it worked out 36 + 59, it described the standard school method of carrying the 1. That is not what its internals showed it doing. Its explanation is itself a learned imitation of how humans explain sums, not a report on its own workings. The model is a black box to itself too.

So the fairest one-line summary is: we understand the recipe, we can see the ingredients, and we cannot yet explain the dish.

## My read: why this matters

This part is my opinion rather than reported fact.

I think the "it can only do what it was trained on" view does real damage in two directions. It makes people dismiss capabilities that are already here, because "surely it wasn't trained for that". And it quietly implies that someone, somewhere, knows the full list of what a model can do, because they trained it task by task. Neither is true. The capabilities are broader than any list, and the people building these systems discover what their models can do partly by testing them after training, not by reading a specification they wrote beforehand.

The better mental model, I think, is something like: a system that was grown by nudging billions of numbers towards "more likely to produce good text", which picked up a wide and lumpy set of general skills along the way, and whose inner workings are only beginning to be mapped. That framing explains why it can surprise you, why it can fail in odd ways, and why "just look at the code" is not an answer to "how does it know that?".

## Sources

- [OpenAI, "Better language models and their implications"](https://openai.com/index/better-language-models/) (February 2019) - GPT-2 and the next-word objective
- [Tom Brown et al., "Language Models are Few-Shot Learners"](https://arxiv.org/abs/2005.14165) (2020) - GPT-3 and in-context learning
- [Jason Wei et al., "Finetuned Language Models Are Zero-Shot Learners"](https://arxiv.org/abs/2109.01652) (2021) - FLAN and unseen task types
- [Long Ouyang et al., "Training language models to follow instructions with human feedback"](https://arxiv.org/abs/2203.02155) (2022) - InstructGPT and RLHF
- [Yuntao Bai et al., "Constitutional AI: Harmlessness from AI Feedback"](https://arxiv.org/abs/2212.08073) (2022) - reinforcement learning from AI feedback
- [Lukas Berglund et al., "The Reversal Curse: LLMs trained on 'A is B' fail to learn 'B is A'"](https://arxiv.org/abs/2309.12288) (2023)
- [Zhaofeng Wu et al., "Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks"](https://arxiv.org/abs/2307.02477) (2023)
- [Llama Team, Meta, "The Llama 3 Herd of Models"](https://arxiv.org/abs/2407.21783) (2024) - parameter and token counts
- [DeepSeek-AI, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"](https://arxiv.org/abs/2501.12948) (2025)
- [Jan Betley et al., "Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs"](https://arxiv.org/abs/2502.17424) (2025)
- [Anthropic, "Tracing the thoughts of a large language model"](https://www.anthropic.com/research/tracing-thoughts-language-model) (27 March 2025)
- [Dario Amodei, "The Urgency of Interpretability"](https://darioamodei.com/post/the-urgency-of-interpretability) (April 2025)

## Related Reading

- [Mechanistic Interpretability: Reading the Mind of a Model](/ai/mechanistic-interpretability-inside-the-black-box/) - the research programme trying to open the black box
- [We Built AI We Don't Fully Understand. What Happens When It's Smarter Than Us?](/ai/we-built-ai-we-dont-fully-understand/) - why the understanding gap matters for safety
- [AI Hallucinations: Understanding and Mitigating False Outputs](/ai/ai-hallucinations-understanding-and-mitigating/) - what the next-word objective means for truthfulness
- [Reasoning Models in 2026: o3, R1, and the Compute-at-Inference Shift](/ai/reasoning-models-2026/) - where reinforcement learning on reasoning has taken things
- [When to Fine-Tune vs When to RAG: Choosing Your AI Architecture](/ai/fine-tune-vs-rag/) - what fine-tuning is and is not good for in practice
- [AI Explainers](/ai/explainers/) - deeper technical explainers if this one has whetted your appetite
