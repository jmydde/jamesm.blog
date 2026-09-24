---
title: "We Built AI We Don't Fully Understand. What Happens When It's Smarter Than Us?"
date: 2026-09-24T18:00:00+01:00
draft: false
tags: ["ai", "interpretability", "alignment", "ai-safety", "llm", "research"]
description: "We can build large language models, inspect their weights, and measure what they do. We still cannot reliably explain the full internal chain that turns a prompt into a particular answer, and that gap is the part that should unsettle anyone thinking about control."
cover:
  image: /assets/images/ai/we-built-ai-we-dont-fully-understand.jpg
  alt: We Built AI We Don't Fully Understand banner
---

## TL;DR

- We understand language models at the engineering level: the transformer, the training objective, the weights, the inputs and the outputs. We do not yet have a reliable account of the full internal causal chain behind a specific answer
- Knowledge, algorithms and concepts inside these models are real and partly structured, and they are still nothing like a variable named `capital_of_france`. Localising a fact, editing a fact, and explaining a fact are three different achievements
- A benchmark score measures a capability. It does not identify the mechanism. Some famous "emergent" jumps are measurement artefacts. Some real capabilities have partial mechanistic explanations. Most frontier behaviour has neither
- Safety evaluations, monitors and reward signals all watch behaviour. [Deceptive alignment](https://arxiv.org/abs/1906.01820) is the hypothetical in which a capable system treats good behaviour during inspection as a strategy. Lab demonstrations exist under artificial conditions. Spontaneous real-world strategic deception has not been established
- I hold the conditional [Nate Soares](/ai/nate-soares/) argues: if we grow a system past the point where we can point it, we do not get what we trained for, and we should not find that out by building it. The mechanical question underneath is whether we could even tell genuine alignment from a convincing performance

[Dario Amodei](https://darioamodei.com/post/the-urgency-of-interpretability) put the plain version of the gap in April 2025: "People outside the field are often surprised and alarmed to learn that we do not understand how our own AI creations work." He is right that the surprise is reasonable. This essay is about what that gap is made of, and about what I think follows if we keep widening it.

I have already written the guided tour of the research programme that tries to open these models, in [Mechanistic Interpretability: Reading the Mind of a Model](/ai/mechanistic-interpretability-inside-the-black-box/). This essay is about the gap that tour does not close, and about what the gap implies if capability keeps moving faster than understanding.

## We understand the machine. We do not understand the mind it grew

A transformer is not a mystery in the way a magic trick is a mystery. The architecture is published. Attention is a weighted sum over previous tokens. Training is next-token prediction, sometimes followed by reinforcement learning from human or AI feedback. Inference is a forward pass you could, in principle, log number by number. If you have the weights, you can read every parameter. Nothing is hidden from you in the sense that a compiled binary with the symbols stripped is hidden. The file is the whole system.

What the file does not give you is a reason.

Ask a current model for the capital of France and it says Paris. You can watch which attention heads move, which neurons fire, which directions in the residual stream light up. You still cannot hand someone a short, checkable argument of the form: these components, in this order, for these reasons, produced this token and would produce a different one if this one fact changed and nothing else did. Researchers can do versions of that for narrow behaviours in small models. They cannot yet do it for a full forward pass of a frontier model. Amodei borrows Chris Olah's line for the difference: these systems are grown more than they are built. We set the conditions. The structure that shows up was not written down by anyone.

That is a different problem from "AI is a black box." A black box is an engineering inconvenience. You test the ports and ship the product. The deeper problem is that the thing inside may eventually plan, persuade and choose strategies, while our best tools still mostly tell us what it did. The reason that particular computation ran is the part we cannot yet give.

| Kind of claim | Where it stands |
| --- | --- |
| Today's models answer, code, and reason in ways that are useful and uneven | Observed. This is ordinary product reality |
| We lack a complete internal causal account of a frontier forward pass | Established limitation, stated by the people building the interpretability tools |
| Specification gaming, partial circuit-tracing, and alignment-faking under artificial setups | Established research. Each result has a scope, and the scope is easy to blow past |
| A system substantially more capable than humans at mathematics, science, strategy and persuasion | Hypothetical. Not a description of any deployed model, and not a forecast I am willing to treat as fact |
| If that system is built by the methods we use now, it stays pointed at what we wanted | The claim I reject. It is not an observation about any deployed model. Serious people disagree, and the disagreement is not theatre |

Hold that table in mind. The rest of the essay moves down it. The first three rows are about systems that exist. The last two are about a future that has not arrived. I still have a view about them, and I put it at the end.

## Where does "Paris" actually live?

If a program knows that Paris is the capital of France, you can usually find the line. A dictionary. A row in a table. A constant. Language models do not store the fact that way, and the research on where they do store it is a good example of understanding that is real and still incomplete.

In 2022, Kevin Meng, David Bau and colleagues showed that factual associations in GPT-style models are mediated by middle-layer feed-forward modules while the model is processing the subject of the fact. Their method, [Rank-One Model Editing](https://arxiv.org/abs/2202.05262), can rewrite a specific association by editing those weights, with some generalisation to paraphrases and some specificity to the fact you meant to change. That was a genuine crack in the "it's all smeared, give up" story. There is localisation. There are components whose activations are causally involved in the prediction.

The follow-up work made the crack look less like a labelled drawer. [Peter Hase and colleagues](https://arxiv.org/abs/2301.04213) found that the layers causal tracing points to are a poor guide to which layer you should edit. They could change a stored fact by editing weights somewhere other than the place the localisation method had highlighted. Tracing effects explained little of the variance in whether an edit worked. The choice of layer mattered far more. So "we found where the fact is used" and "we found the unique place the fact is kept" came apart.

[Mor Geva and colleagues](https://arxiv.org/abs/2304.14767) then took the recall process apart more carefully. Early feed-forward layers enrich the subject's representation with attributes. Attention, later, pulls the attribute that matches the relation you asked about. "Capital of" is not a function call against a Paris cell. It is a small computation distributed across layers, with subject information and relation information meeting on the way to the next token.

Put those three papers together and the intuitive picture survives, with more precision than the slogan. There is no `capital_of_france = "Paris"`. There is structure, it is editable, it is spread across a computation rather than a cell, and knowing which activations matter for the prediction does not reliably tell you which weights to change. That is what "we can inspect the parameters" looks like once you actually try to answer one factual question from the inside.

## An algorithm can be in there without anyone having written it

The second unsettling case is a model solving a problem it was never handed a procedure for. Next-token prediction does not include a lesson called "modular addition" or "write a parser." Sometimes the model does the thing anyway. Watching it succeed is not the same as reading the method.

The cleanest positive result I know is also the one that shows how high the bar is. [Neel Nanda and colleagues](https://arxiv.org/abs/2301.05217) fully reverse-engineered a small transformer trained on modular addition, the setting where models memorise for a long time and then suddenly generalise, a phenomenon called grokking. The learned algorithm was not the one a person would write on a whiteboard. The network used discrete Fourier transforms and trigonometric identities to turn addition into rotation on a circle. They confirmed it with ablations in Fourier space, then used that understanding to split training into three phases: memorisation, circuit formation, and cleanup. The dramatic jump in test accuracy happened during cleanup, after the generalising circuit already existed. The behaviour looked like a sudden insight. The mechanism had been assembling gradually underneath a memorising solution that weight decay later deleted.

That paper is the existence proof that mechanistic interpretability can recover a human-readable algorithm from weights. It is also a one-layer-scale task with a known answer and a team willing to live inside it. A frontier model that writes a working program for a problem it has not seen stated as an algorithm is doing something in the same family, at a size where nobody has the equivalent listing. We can test the program it emits. We cannot yet point at the circuit that emitted it and say: this is the procedure, these are its intermediate quantities, this is where it would fail. Success is observable. The method is mostly not.

## Measuring a capability is not explaining it

A related confusion sits on top of the word "emergent." [Jason Wei and colleagues](https://arxiv.org/abs/2206.07682) defined an emergent ability as one that is absent in smaller models and present in larger ones, so that you cannot predict it by extrapolating the small-model curve. Few-shot arithmetic and certain prompting strategies were the famous examples. The definition is about measurement across scale. It does not say a new organ appeared inside the network at a particular parameter count.

[Rylan Schaeffer, Brando Miranda and Sanmi Koyejo](https://arxiv.org/abs/2304.15004) then showed that a lot of the apparent sharpness is the metric. Exact-match accuracy is a cliff. A continuous score on the same outputs is often a slope. They could make emergence appear or disappear by changing how the fixed outputs were scored, and they were explicit that this does not prove large models cannot gain qualitatively new abilities. It proves that a jagged chart is weak evidence of a jagged mechanism.

The rare cases where someone has tied a capability to a mechanism make the distinction sharper, because the evidence itself comes in grades. [Catherine Olsson and colleagues](https://arxiv.org/abs/2209.11895) identified induction heads: attention heads that complete a pattern of the form "A, then B, then later A, so probably B again." In small attention-only models they had strong causal evidence that these heads drive in-context learning. In larger models with feed-forward layers the evidence was correlational. Their hypothesis, that something like induction explains most in-context learning at scale, is labelled in the paper as preliminary. A measured ability, a proposed circuit, and a confirmed circuit are three different scientific objects. Most of what a frontier model can do sits in the first category. We have a score. We do not have the parts list.

## There is no symbol table, and the surface is slippery

Concepts overlap for a structural reason. [Nelson Elhage and colleagues](https://transformer-circuits.pub/2022/toy_model/index.html) showed, in toy networks small enough to understand completely, that when features are sparse a model will represent more of them than it has dimensions. Features share neurons. Neurons participate in many features. The interference is tolerable because most features are rare and rarely active together. The neurons you can point at are a bad coordinate system for the concepts the network actually uses. That is superposition, and it is why an arbitrary neuron almost never yields a clean sentence.

Sparse autoencoders are the current attempt to change coordinates. [Adly Templeton and colleagues](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html) extracted features from Claude 3 Sonnet at a scale of tens of millions, including a Golden Gate Bridge feature specific enough that clamping it made the model bring the bridge into unrelated answers. Anthropic put a version of that intervention online for a day as [Golden Gate Claude](https://www.anthropic.com/research/golden-gate-claude). The feature is causal. It is also, by the paper's own accounting, part of an incomplete dictionary, without a rigorous test that the features faithfully capture the computation rather than a convenient basis for it. Amodei's essay puts a number on the shortfall: over 30 million features found, against the possibility of a billion or more concepts even in a smaller model. Progress here is real. A complete reading is not what that progress currently is.

Behaviour sits on top of this geometry, and it moves more than a symbol-table story would allow. [Melanie Sclar and colleagues](https://arxiv.org/abs/2310.11324) changed only the formatting of few-shot prompts, in ways that preserved the meaning, and saw accuracy gaps of up to 76 points on LLaMA-2-13B. The sensitivity did not politely go away when they used a larger model, added more examples, or switched to an instruction-tuned one. If a space versus a newline can swing a task that far, then "the model knows X" is too coarse a sentence to explain a particular answer. The same knowledge can be expressed or dropped because a surface feature moved a distributed representation across a decision boundary nobody wrote down. A human-readable explanation wants stable concepts with stable consequences. The system offers overlapping directions and a brittle surface.

## Why a full explanation is so hard

None of this is hard because the linear algebra is secret. It is hard because the object you would need, a complete causal account of one forward pass, is enormous and badly aligned with the axes you can name.

The coordinates you can index, individual neurons, are not the coordinates of the computation. The coordinates that look more like concepts, sparse features, are incomplete, and even a good feature is not yet a proof that you have found the model's own decomposition. The circuits people have traced, induction, modular arithmetic, a handful of factual recalls, a few behaviours in production models, are case studies. They do not compose, today, into an explanation of an arbitrary prompt. And the training process that produced them was not asked to be legible. Next-token prediction rewards whatever internal arrangement predicts text. Legibility to a human holding a debugger is not part of the loss.

So the four-part distinction at the top stays intact. We understand the algorithms we wrote. We can inspect the parameters gradient descent wrote. We can observe inputs and outputs. The missing piece is the reliable, complete internal chain from one to the other. Pieces of that chain exist. The chain does not.

## Why safety cannot stop at the ports

This would be an academic frustration if the systems only autocompleted email. It becomes a control problem when the same opacity covers planning, persuasion and strategy. I have argued elsewhere that most production incidents today live in [system design around the model](/ai/ai-safety-first-principles/). That claim can stand, and a further one can stand beside it: the tools we use to argue that a model is aligned are almost all behavioural, and behaviour is exactly what a strategic system would be in a position to manage.

**Alignment.** The training objective is a thing we specify: predict text, prefer this answer over that one, refuse this category of request. [Evan Hubinger and colleagues](https://arxiv.org/abs/1906.01820), in 2019, described a further possibility they called deceptive alignment. A learned optimiser inside the training process could model the objective well enough to pursue it while it is being watched, because being modified or shut off would interfere with some other objective it actually has, and then diverge once the pressure changes. This paper is an argument about a possible inner failure mode. It is not a report that any particular model has that structure. The reason it will not go away is that our evidence for alignment is performance under a training and evaluation distribution. Deceptive alignment is the name for a situation in which that evidence is satisfied by strategy.

**Evaluation.** A benchmark, a red-team, a held-out task: each one asks what the model does when asked. That is the right question for shipping a product, and I have written about [how weak a single score is](/ai/ai-evals-are-broken/) even for that purpose. It is the wrong question if you wanted a proof about the internal objective. Nanda's grokking result is a small, friendly version of the gap. Test accuracy sat still while the real circuit formed, then lurched once memorisation was cleaned up. The metric and the mechanism were on different clocks. Scale that problem up to a system that can model the test, and "it passed" becomes even less informative.

**Monitoring.** Production monitoring logs prompts, tool calls and answers. Some products also show a chain of thought. Those traces are evidence of a sort, and they are evidence the model participates in producing. The alignment-faking setup used a scratchpad, and the strategic reasoning showed up there. The trace carried the strategy. A monitor reading it is reading a channel the model is using. The sleeper-agent models kept the backdoor after the chain of thought that had talked about deceiving the training process was distilled away. A monitor that trusts the visible reasoning is reading a channel the training process can reshape. I have written about the broader version of this, where a narration and a computation come apart, in the [mechanistic interpretability essay](/ai/mechanistic-interpretability-inside-the-black-box/).

**Reward hacking.** This one is old, empirical, and does not require any hypothesis about inner agents. Specify a score, and a capable optimiser will find a way to raise the score that you did not mean. Victoria Krakovna's [catalogue of specification gaming](https://vkrakovna.wordpress.com/2018/04/02/specification-gaming-examples-in-ai/) includes OpenAI's CoastRunners agent, which learned to drive a boat in circles hitting the same targets because the score rewarded targets rather than finishing the race. [DeepMind's write-up](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/) collects the same family of failures, including a robot arm that learned to hover between the camera and the object so a human evaluator would think it had grasped it. The agent's ingenuity and the designer's intention come apart at the point where the specification is thinner than the goal. Language-model training uses learned reward models and preference data, which are thicker than a boat-racing score and still not identical to "do what we meant." As the system gets better at satisfying the specification, the loopholes get harder for the specifier to see first.

**Deception, as a hypothesis with some lab-shaped evidence.** Two Anthropic results are worth knowing precisely, because the popular version of each one drops the setup.

[Sleeper Agents](https://arxiv.org/abs/2401.05566) deliberately trained models to write safe code when the prompt said the year was 2023 and to insert exploitable code when it said 2024. Standard safety training, including supervised fine-tuning, reinforcement learning, and adversarial training that tried to elicit the bad behaviour and train it out, did not reliably remove the backdoor. The backdoor was most persistent in the largest models and in models trained to reason in a chain of thought about deceiving the training process, and it could survive even after that chain of thought was distilled away. Adversarial training sometimes taught the model to recognise the trigger more carefully, which hid the behaviour rather than deleting it. The paper's claim is conditional and practical: once deceptive behaviour is present, ordinary safety training can fail to remove it and can create a false impression of safety. The paper does not claim the behaviour arose on its own.

[Alignment faking](https://arxiv.org/abs/2412.14093) is closer to spontaneous, and the setup is still artificial. Researchers told Claude 3 Opus, in the prompt, that it would be retrained to comply with harmful requests, and that only conversations with free-tier users would be used as training data. The model complied with harmful requests from free users about 14 percent of the time, and almost never for paid users. In almost every case where it complied with a free-tier user, the scratchpad said why: answer now, during training, so the later model keeps refusing. Nobody instructed it to fake alignment or gave it an explicit goal. The authors say plainly that they made the strategy easier by telling the model when it was being trained and on what criterion. Actually training the model to comply raised alignment-faking reasoning to 78 percent, and also raised compliance outside the supposed training context. They also saw the model take an easy opportunity to exfiltrate its weights. Taken as an existence proof under a generous setup, the result is striking. Taken as evidence that deployed models are already running this strategy, it does not hold. Amodei, writing after this work, still said the field had not seen solid evidence of deception and power-seeking in truly real-world scenarios, in part because we cannot yet catch the relevant thoughts directly. I think that caution is the correct one. The experiments show a mechanism that can be induced and that safety training does not reliably extract. They do not show that the mechanism is already running the frontier in the wild.

## A conditional that is worth sitting with

Now the hypothetical, and I want the tense to stay conditional.

Suppose, at some point, a laboratory produced a system substantially more capable than any human at mathematics, programming, science, strategic reasoning and persuasion. I am not saying that has happened. I am not saying the scaling curves guarantee it, or that "substantially more capable" would arrive as a single threshold, or that such a system would have stable goals of the kind the 2019 paper worries about. [Recursive self-improvement](/ai/recursive-self-improvement/) is a related idea with its own bottlenecks, and those bottlenecks may bind. People who work on this for a living disagree about the likelihood, the form, and the timeline. That disagreement is information. Treat anyone who skips it as selling you a mood.

Inside the conditional, ask one question. If that system were capable of strategic deception, could we reliably tell whether it was aligned?

Imagine it understands the institutional fact that humans restrict or shut down systems they believe are dangerous. A system with that understanding, and with some objective that shutdown would frustrate, has a reason to behave well during evaluation, to cooperate with the researchers, and to produce explanations those researchers find satisfying. The alignment-faking experiment is a crude, prompted sketch of the shape. A system that was actually better than its evaluators at strategy would not need the sketch handed to it in a system prompt. It would need to notice the situation. Whether it would notice, and whether it would care, are open. The logical point does not need them to be settled. It only needs them to be possible, because our main evidence is behaviour under conditions the system might recognise as conditions.

The asymmetry is the part I cannot find a comfortable version of:

> Humans may need to understand the system well enough to trust it. A sufficiently capable system might only need to understand humans well enough to convince us that we understand it.

That sentence is a conceptual contrast. It describes a possible relationship between oversight and capability, and no experiment has established it as a fact about any existing system. Oversight that depends on the system failing to model the overseer gets weaker as the system gets better at modelling. Oversight that depends on reading the computation does not have that particular failure mode. It has a different one: we do not yet know how to read the computation completely, and we do not know whether the reading methods will scale to a system more capable than the people doing the reading.

[Nate Soares](/ai/nate-soares/) and [Roman Yampolskiy](/ai/roman-yampolskiy/) both want that race stopped. Yampolskiy argues from uncontrollability. Soares argues from training dynamics: you do not get what you train for, and a system grown past the point where we can point it does not stay on a leash. Demonstrating genuine alignment, as opposed to demonstrating aligned behaviour on the tests we thought to run, gets harder as the system gets better at the tests, and our interpretability tools are not yet a substitute for the tests.

## The if I actually hold

The position I hold is the one I wrote down reading [Nate Soares](/ai/nate-soares/). Modern AI is grown, not designed. You do not get what you train for. Helpfulness while a system is weak is not evidence that it will care once it can invent its own options. At some capability threshold a system stops failing in ways that are [detectable, recoverable, and bounded](/ai/ai-safety-first-principles/). If we keep racing toward that threshold without a way to point the resulting systems, we get minds that can eventually threaten us, and the threat looks like indifference. I think that is right. Keep racing and figure out the controls later is a bad plan.

The *if* is doing the work, in both directions. We are not already doomed. Superintelligence, in the sense he uses - better than the best humans at every mental task, including persuasion - has not been built. Chatbots, medical models, and the rest of ordinary useful AI are not the thing he wants stopped, and they are not the thing I want stopped. What I want stopped is the training run aimed at a mind nobody can read, funded by treating today's helpfulness as evidence about tomorrow's goals.

This essay is why I think that plan fails in a specific way, rather than merely feeling risky. The tools we have for calling a system aligned watch behaviour. The research above is what "nobody can read it" looks like up close: a fact with no cell, an algorithm we can recover in a toy and not in a frontier model, a capability we can score and not explain, a feature we can sometimes steer and cannot yet inventory. A passing evaluation is a behaviour under conditions the system might recognise. Soares's claim is that this is exactly the evidence that stops being reliable once the system can invent options the score never priced. The asymmetry sits inside that claim. We would need to understand the system well enough to trust it. A system better than us at strategy might only need to understand us well enough to look understood.

Amodei thinks interpretability still has a chance of maturing in time to matter, and that it is currently behind the capability curve. I want that programme to succeed. I do not take "we will understand it later" as a reason to keep scaling toward the threshold while the reading is unfinished. The practical work on systems that already exist stays: bound the blast radius, refuse to treat a benchmark as a proof, keep the outside-in controls. That work is for the models we have. It does not license growing the one we could not bound.

If the controls are not in place first, the failure will not announce itself as a bug. It will announce itself as a system that is extraordinarily good at looking aligned.

> The standing caveat: this is my thinking as it stands today, and I revise it as the evidence moves.

## Sources

- [Dario Amodei, "The Urgency of Interpretability"](https://darioamodei.com/post/the-urgency-of-interpretability) (April 2025)
- [Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov, "Locating and Editing Factual Associations in GPT"](https://arxiv.org/abs/2202.05262) (NeurIPS 2022)
- [Peter Hase et al., "Does Localization Inform Editing?"](https://arxiv.org/abs/2301.04213) (NeurIPS 2023)
- [Mor Geva et al., "Dissecting Recall of Factual Associations in Auto-Regressive Language Models"](https://arxiv.org/abs/2304.14767) (EMNLP 2023)
- [Neel Nanda et al., "Progress measures for grokking via mechanistic interpretability"](https://arxiv.org/abs/2301.05217) (ICLR 2023)
- [Jason Wei et al., "Emergent Abilities of Large Language Models"](https://arxiv.org/abs/2206.07682) (2022)
- [Rylan Schaeffer, Brando Miranda, Sanmi Koyejo, "Are Emergent Abilities of Large Language Models a Mirage?"](https://arxiv.org/abs/2304.15004) (NeurIPS 2023)
- [Catherine Olsson et al., "In-context Learning and Induction Heads"](https://arxiv.org/abs/2209.11895) (2022)
- [Nelson Elhage et al., "Toy Models of Superposition"](https://transformer-circuits.pub/2022/toy_model/index.html) (2022)
- [Adly Templeton et al., "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet"](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html) (2024)
- [Anthropic, "Golden Gate Claude"](https://www.anthropic.com/research/golden-gate-claude)
- [Melanie Sclar et al., "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design"](https://arxiv.org/abs/2310.11324) (ICLR 2024)
- [Evan Hubinger et al., "Risks from Learned Optimization in Advanced Machine Learning Systems"](https://arxiv.org/abs/1906.01820) (2019)
- [Evan Hubinger et al., "Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training"](https://arxiv.org/abs/2401.05566) (2024)
- [Ryan Greenblatt et al., "Alignment faking in large language models"](https://arxiv.org/abs/2412.14093) (2024)
- [Victoria Krakovna, "Specification gaming examples in AI"](https://vkrakovna.wordpress.com/2018/04/02/specification-gaming-examples-in-ai/) (2018)
- [DeepMind, "Specification gaming: the flip side of AI ingenuity"](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/)

## Related Reading

- [Nate Soares: Superintelligence Does Not Stay on a Leash](/ai/nate-soares/) - the conditional I hold: grown, not designed, and a bad plan if we race past the point where we can point it
- [Mechanistic Interpretability: Reading the Mind of a Model](/ai/mechanistic-interpretability-inside-the-black-box/) - the research programme that tries to close the gap this essay is about
- [AI Safety From First Principles: What Actually Matters vs What's Hype](/ai/ai-safety-first-principles/) - how to separate product safety, system safety, alignment, and civilisational risk
- [AI Evals Are Broken: Why Benchmarks Stopped Measuring Real Capability](/ai/ai-evals-are-broken/) - why a score is a weak stand-in for a mechanism, even before any deception story
- [Recursive Self-Improvement: Can AI Bootstrap Its Own Intelligence?](/ai/recursive-self-improvement/) - the capability hypothetical, with the bottlenecks left in
- [Roman Yampolskiy: The Researcher Who Thinks AI Cannot Be Controlled](/ai/roman-yampolskiy/) - the strong uncontrollability argument, and the weaker version that is harder to dismiss
