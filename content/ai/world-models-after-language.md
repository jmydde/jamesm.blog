---
title: "World Models: What Comes After the Language-Only Era"
date: 2026-06-13T10:00:00+01:00
draft: false
series: ["Trust"]
type: essay
tags: ["ai", "world-model", "robotics", "agent", "multimodal", "agentic-engineering"]
description: "Language-only models have a statistical shadow of physical reality, not a reliable simulator of it. A grounded look at world models - what they are, where the 2026 frontier sits, and why they matter for agents that need to act rather than answer."
cover:
  image: /assets/images/ai/humanoid-robotics-2026.jpg
  alt: World Models - What Comes After the Language-Only Era Banner
slug: "world-models-after-language"
---

## TL;DR

- **Language-only models do not contain a reliable simulator of physical reality** - they contain a statistical shadow of one, good enough for many tasks and dangerously wrong for others.
- **A world model** is a system that learns to predict how an environment evolves and can plan inside that prediction - not just describe it in text.
- **The gap matters for agents** that must act in physical space, manipulate objects, or reason about counterfactuals where the answer is not in the training corpus.
- **The 2026 frontier** includes generative world simulators, vision-language-action models for robotics, and sim-to-real pipelines - not one breakthrough but a stack assembling in parallel.
- **For builders today:** language agents with MCP tools are the right architecture for knowledge work. World models are the path to agents that can competently act in the physical world.

Almost everything I have written about AI agents assumes a model whose understanding of the world arrives through text. That assumption has carried the field a long way. [Context engineering](/ai/context-engineering/), [tool use via MCP](/ai/mcp-servers-home-ai-agent/), [memory across sessions](/ai/home-ai-agent-memory-that-lasts/) - all of it sits on top of language models that read, reason, and call APIs.

I do not think that assumption carries us all the way. The next research frontier I am watching is **world models** - systems that learn predictive simulators of environments and can plan inside them. This post is a first pass at why that matters, what the term actually means, and where the honest line between hype and engineering sits in 2026.

------------------------------------------------------------------------

## The language-only ceiling

Language models are extraordinary at tasks where the world can be adequately represented as text. Code, law, medicine at the reference-knowledge level, customer support, document synthesis, most of what we call "knowledge work" - the representation works because the domain was already textual.

The ceiling shows up in tasks that require **causal and physical reasoning** the model cannot verify against reality:

**Counterfactual physics.** Ask a language model whether a stack of three objects will fall if you remove the bottom one. It will usually answer correctly - because that scenario appears thousands of times in training text. Ask about a novel arrangement of irregular objects on a soft surface and the answer becomes unreliable in ways that are hard to detect without running the experiment.

**Long-horizon physical plans.** "Move the cup to the shelf without spilling" decomposes into grasp selection, force control, collision avoidance, and recovery from slips. A language model can narrate a plausible plan. It cannot simulate whether the plan survives contact with a wet ceramic rim.

**Closed-loop control.** Text generation is open-loop: the model produces tokens and never observes the consequence of its output on the environment. Physical action is closed-loop: every movement changes what you see next. Language models trained on static text never experience that loop during training.

These are not edge cases for a narrow slice of robotics. They are the **default condition** for any agent that must act in physical space rather than call an API.

The model has read descriptions of physics. It has not lived inside a physics engine. The difference is the gap world models are trying to close.

------------------------------------------------------------------------

## What a world model actually is

The term comes from David Ha and Jürgen Schmidhuber's [2018 paper "World Models"](https://arxiv.org/abs/1803.10122), which is still the clearest framing. The architecture has three parts:

1. **A perception module** that compresses high-dimensional observations (images, sensor readings) into a compact state representation.
2. **A dynamics model** that predicts the next state given the current state and an action.
3. **A controller** that plans by searching or learning inside the dynamics model - trying actions in simulation before executing them in reality.

The key property is **predictive simulation**. The system can ask "what happens if I do X?" and get an answer from an internal model of the environment, not from retrieving a similar paragraph from training data.

```
Observations (images, sensors)
        │
        ▼
┌───────────────────┐
│ Perception module │  compress to compact state
└─────────┬─────────┘
          │ state_t
          ▼
┌───────────────────┐     action
│  Dynamics model   │◄────────────┐
│  (world model)    │             │
└─────────┬─────────┘             │
          │ predicted state_{t+1} │
          ▼                       │
┌───────────────────┐             │
│    Controller     │─────────────┘
│  (plan in sim)    │
└─────────┬─────────┘
          ▼
    Execute in reality
```

This is distinct from several things it is often confused with:

| Not a world model | Why |
|---|---|
| Bigger context window | More text history does not give you a physics engine |
| RAG over a document corpus | Retrieval finds descriptions; it does not simulate consequences |
| Chain-of-thought reasoning | Language about a plan is not execution of a plan |
| Video generation | Pretty pixels without actionable state are not controllable simulation |

A world model is useful to the degree that its predictions are **actionable** - good enough to plan with, not just good enough to watch.

------------------------------------------------------------------------

## Where the 2026 landscape actually sits

The field in 2026 is not one breakthrough but several stacks maturing in parallel.

**Generative world simulators.** Models in the lineage of Google DeepMind's Genie and similar work learn to simulate game-like environments from video. You can give an action - move left, jump, interact - and the model generates the next frame. The simulation quality is still rough for arbitrary real-world scenes, but the capability is real and improving fast. These are research platforms today and game-engine replacements tomorrow.

**Vision-language-action (VLA) models for robotics.** The [humanoid robotics wave in 2026](/ai/humanoid-robotics-2026/) is powered partly by models that map camera input and language instructions directly to motor commands - Figure's Helix, Google DeepMind's Gemini Robotics lineage, 1X's Redwood. These are not classical world models in the Ha and Schmidhuber sense, but they embed learned dynamics implicitly in the policy network. The robot does not narrate a plan; it executes one conditioned on what it sees.

**Sim-to-real pipelines.** The practical path for industrial robots remains: train in simulation with a known physics engine, transfer to reality with domain randomisation and teleoperation fine-tuning. NVIDIA Isaac, Meta's Habitat, and a growing list of open simulators are the training grounds. World models may eventually replace hand-built simulators. Today they augment them.

**Multimodal foundation models.** Models that see, hear, and read are necessary but not sufficient. [Multimodal AI beyond vision](/ai/multimodal-ai-beyond-vision/) adds perception channels. World models add the predictive layer on top - the "what happens next if I act" that perception alone does not provide.

The honest summary: **no one has a general-purpose world model good enough to drop into an arbitrary physical deployment.** The pieces exist. The integration does not. That is why this is a research frontier and not a product category yet.

------------------------------------------------------------------------

## Implications for agents

If you are building agents today, the practical split looks like this:

**Language agents with tools** - the MCP stack, the home agent, the coding agent - are the right architecture for tasks where the environment is already API-shaped. Filesystem, database, calendar, CI pipeline. The world is legible as text and HTTP. [Securing those agents](/ai/securing-ai-agents/) is the urgent engineering problem.

**World-model-backed agents** become necessary when:

- The task requires **closed-loop physical action** - manipulation, navigation, assembly.
- The cost of a failed action in reality is high and **cannot be reduced by a confirmation gate** - a dropped glass, a collision, a mis-grasped component.
- Planning requires **counterfactual simulation** - "if I reach around the obstacle, can I still grasp the handle?" - that text reasoning cannot verify.

The bridge between these two worlds in 2026 is mostly human: a language agent plans at the task level, a human or a specialised robot policy executes at the physical level. The integration point - a language agent that can invoke a world model to validate a plan before actuation - is where the interesting engineering is starting but has not yet standardised.

**Evaluation changes too.** [Endpoint evals are broken](/ai/ai-evals-are-broken/) for language tasks. They are worse for physical ones, where the metric is not "did it produce the right text" but "did the predicted state match reality after action." Synthetic rollouts inside a world model are one path to pre-deployment testing - run the plan in simulation, measure divergence from expected state, reject trajectories that fail before they touch hardware. That connects world models directly to the trajectory-evaluation problem on my research map.

------------------------------------------------------------------------

## What I am watching, not building

A few areas I find compelling but have deliberately left off my active work list:

**General-purpose physical world models.** The Genie-class simulators are impressive demos. I do not yet have a workload where I can test them against reality on my own hardware. Watching, not building.

**Quantum or neuromorphic accelerators for world-model inference.** Real research directions, not close enough to my stack to earn depth time.

**Claims that language models "already are" world models.** Sometimes true in narrow domains where the environment is text-shaped. Misleading as a general statement about physical reality. I prefer the honest gap to the comforting conflation.

The line between watching and researching is the line between "I can run an experiment this month" and "I can read papers and feel informed." World models are moving toward the first category for robotics teams. For a home-agent builder on a Mac Studio, they are still mostly the second.

------------------------------------------------------------------------

## The through-line

Language got us agents that can **answer and orchestrate**. World models are the path to agents that can **predict and act** in environments where the consequence of an action is not already written down.

That is not a small increment. It is the difference between an assistant that describes how to stack boxes and one that stacks them - and notices when the stack is unstable before letting go.

The language-only era is not ending tomorrow. Most of the agents shipping in 2026 are language agents with tools, and that is the right call for most workloads. But the research direction is clear: the models that will matter for robotics, autonomous systems, and any agent that touches physical reality will need an internal simulator, not just a vast memory of descriptions.

Understanding that distinction early is cheaper than discovering it after you have bet an architecture on text alone.

## Related Reading

- [What I'm Researching in AI Right Now](/ai/what-im-researching-in-ai-right-now/) - where world models sit on my research map.
- [Humanoid Robotics in 2026: From Prototypes to Production](/ai/humanoid-robotics-2026/) - the deployment context world models must eventually serve.
- [Securing AI Agents](/ai/securing-ai-agents/) - the trust problem for language agents with tool access today.
- [AI Evals Are Broken](/ai/ai-evals-are-broken/) - why endpoint scoring fails, and why it fails harder for physical action.
- [AI in Scientific Research: From AlphaFold to the Long Tail](/ai/ai-in-scientific-research-2026/) - where simulation and prediction already beat pure language.
- [Recursive Self-Improvement: Can AI Bootstrap Its Own Intelligence?](/ai/recursive-self-improvement/) - the long-horizon capability question world models connect to.
- [Reading the Signals: The Four Futures Framework](/ai/reading-the-signals-four-futures/) - long-horizon framing for where embodied AI fits.
