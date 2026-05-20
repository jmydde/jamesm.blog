---
title: "What I'm Researching in AI Right Now - And Where I'm Going Next"
date: 2026-05-21T07:30:00+01:00
draft: false
tags: ["ai", "agent", "research", "context-engineering", "reliability", "world-model"]
description: "I treat my own learning like a research agenda - a small set of questions I am actively chasing rather than a reading list. Here are the AI areas I have been deep in, the ones I have decided to move into next, and the ones I am deliberately leaving on the watch list."
cover:
  image: /assets/images/ai/what-im-researching-in-ai.png
  alt: What I'm Researching in AI Right Now Banner
---

## TL;DR

- I treat my own learning like a **research agenda** - a small set of questions I am actively chasing, not a reading list I feel guilty about
- The work I have been deep in clusters into four areas: **agent reliability and non-determinism**, **context engineering and memory**, **the economics of intelligence**, and **the open-weight and small-model frontier**
- The areas I have decided to move into next are the ones where I keep hitting questions I cannot answer well: **securing agents that hold real tool access**, **evaluating agents on their trajectory rather than their final answer**, **world models beyond the language-only era**, and the **machine-to-machine agent economy**
- I treat **AGI timelines** less as a forecast to win and more as a planning input - what changes for an engineer if capable autonomous systems arrive in three years rather than fifteen
- I am deliberately not chasing every frontier. Quantum machine learning and neuromorphic hardware sit on my watch list, not my work list, and being honest about that line is the whole point

Most people consume AI news. I used to do the same - a feed of model releases, benchmark claims, and launch threads that left me feeling informed and changed nothing about what I could actually build.

At some point I stopped treating it as news and started treating it as a research agenda.

The difference is small but it changes everything. News is something that happens to you. A research agenda is a short list of questions you have decided are worth your own time, that you return to deliberately, and that you expect to make progress on. It has a shape. It has gaps you can name. It has things you have consciously chosen to ignore.

This post is that agenda, written down. Part of it is a map of where I have already been spending my time. Part of it is where I have decided to go next. And part of it is the frontier I am deliberately leaving alone for now, because pretending to research everything is the same as researching nothing.

------------------------------------------------------------------------

## How I think about a research map

A research map is not a backlog. A backlog is everything you might do. A map is the small number of questions you have committed to, organised so you can see how they connect.

Mine has three rules.

**It stays small.** If I am chasing more than four or five live questions at once, none of them get real depth. Breadth is what the feed gives you for free. Depth is the thing you have to choose.

**Every item is a question, not a topic.** "Agents" is a topic. "Why does an agent that passed every test in staging behave differently on the same input in production" is a question. Topics let you read forever and conclude nothing. Questions tell you when you are done.

**It has an explicit not-doing list.** The areas I have decided to leave alone are part of the map, not an omission from it. Writing them down stops me feeling I am falling behind every time one of them trends.

With that framing, here is the actual map.

------------------------------------------------------------------------

## Where I have been deep

These are the four clusters I have spent the most time on, and the ones most of my recent writing has come out of. They are not finished - research questions rarely close cleanly - but they are mature enough that I can say what I have actually learned.

### 1. Agent reliability and the non-determinism problem

This is the question that pulled me in and has not let go: why is an AI agent that works in the demo so unreliable in production, and what do you actually do about it.

The classic reliability toolkit - unit tests, deterministic replay, traditional monitoring - was built for systems that behave the same way each time given the same input. Agents do not. That mismatch is not a minor operational annoyance, it is the central engineering challenge of the category, and I have written about [debugging non-deterministic agent systems](/ai/agent-reliability-debugging-non-deterministic/) and [what it takes to build agents that actually work](/ai/ai-agents-that-actually-work/) trying to pin it down.

What I have concluded so far: reliability here is less about making the model deterministic and more about constraining the system around it - narrow tools, explicit checkpoints, bounded autonomy, and the assumption that any single step can fail. The agent is the unreliable component. The architecture is where reliability gets engineered back in.

### 2. Context engineering and memory

The second cluster grew directly out of the first. If agents fail in long runs, a lot of the failure traces back to what is in the context window.

I have spent real time on this one. [Context engineering](/ai/context-engineering/) - treating the whole window as a curated, decaying budget rather than a bucket you fill - is, I think, the production skill that quietly replaced prompt engineering. Anthropic's engineering team frames it well in their write-up on [effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): the job is curating what enters the model's limited attention at each step, not wording one request perfectly.

The adjacent questions have kept me busy too: [memory that survives across runs](/ai/home-ai-agent-memory-that-lasts/), [what actually works with long context](/ai/claude-long-context-and-memory-2026/), [prompt caching](/ai/prompt-caching/) as a cost lever, and the [token efficiency mindset](/ai/claude-token-efficiency-mindset/) that ties them together. The through-line: more context is almost never the answer, and the teams shipping reliable systems are the ones who curate aggressively.

### 3. The economics of intelligence

The third cluster is the one I underrated at first and now think about constantly: what does intelligence actually cost, and who pays.

It is easy to assume inference costs only ever fall. They do not, cleanly - and I dug into [why costs are not going down](/ai/token-economics-why-costs-arent-going-down/) the way the headline price-per-token numbers suggest. Around that sit the questions of [running models locally versus in the cloud](/ai/local-vs-cloud-ai-2026/), the [hardware war](/ai/ai-hardware-wars-blackwell-mi300x-tpuv6/) deciding who can serve intelligence cheaply, and the [data-centre power crunch](/ai/ai-energy-crisis-data-center-power/) that turns out to be a hard physical ceiling on the whole thing.

What I have taken from it: cost is a design constraint, not an afterthought. The architecture decisions that look like pure engineering - which model tier, local or hosted, how much context - are economic decisions wearing engineering clothes.

### 4. The open-weight and small-model frontier

The fourth cluster is the counterweight to the frontier-model story. While the headlines track the largest models, the more interesting question for a practitioner is how small and how open you can go before quality actually breaks.

I have looked at the [state of open-weight models](/ai/state-of-open-weight-models-2026/), the case for [small language models](/ai/small-language-models/) doing real work, the [fine-tuning landscape](/ai/fine-tuning-landscape-2026/), and [what RAG won and lost](/ai/rag-in-2026-what-won-what-lost/) as a way of getting capability without scale. The pattern is consistent: a surprising amount of production work does not need a frontier model, and the skill is knowing which work does.

------------------------------------------------------------------------

## Where I am going next

The four clusters above are where I have answers. The next four are where I keep running into questions I cannot answer well yet - which is exactly why they are moving onto the active part of the map. I have decided these are the areas worth my next stretch of real time.

### 1. Securing agents that hold real tool access

This is the one I am most certain about. The more I work on agent reliability, the more obvious it becomes that I have been studying the failure modes where nobody is trying to break the system. The moment an agent holds genuine tool access - reading files, calling APIs, moving money, touching production - reliability and security stop being separate problems.

The specific questions I am taking on: how the confused-deputy problem shows up when an agent acts with its own privileges on behalf of an untrusted instruction, how to harden [the protocols agents talk through](/ai/agent-protocols-mcp-a2a-acp/) such as the [Model Context Protocol](https://modelcontextprotocol.io/), and how prompt injection stops being a curiosity and becomes the primary attack surface. The [OWASP Top 10 for LLM applications](https://genai.owasp.org/llm-top-10/) - prompt injection, excessive agency, improper output handling - reads like a list of things my own designs do not yet defend against properly. That is the gap I am closing.

### 2. Evaluating agents on the trajectory, not the answer

The second move follows from how unsatisfied I am with current evaluation. I have argued that [AI evals are broken](/ai/ai-evals-are-broken/), and the deeper I get into agents the more I think the break is specifically this: we score the final answer when the thing that determines reliability is the path taken to get there.

An agent can reach a correct answer through a reckless trajectory - calling the wrong tool, getting lucky, ignoring a constraint that did not happen to bite this time. Score only the endpoint and you certify that behaviour. So the question I am taking on is trajectory evaluation: step-level scoring, replay harnesses that catch regressions in *how* an agent works, and metrics that treat a multi-step run as the unit of quality. I do not have a clean method for this yet. That is the point of putting it on the map.

### 3. World models and the end of the language-only era

The third move is the most speculative, and the one I think is most underrated. Almost everything I have researched so far assumes a model whose understanding of the world arrives through text. That assumption has carried us a long way. I do not think it carries us all the way.

A model trained only on language has no reliable internal simulator of physical and causal reality - it has a statistical shadow of one. World models, in the sense David Ha and Jürgen Schmidhuber set out in their [2018 "World Models" paper](https://arxiv.org/abs/1803.10122) and the line of work that followed, are systems that learn a predictive model of an environment and can reason and plan inside it. That capability is what stands between today's agents and ones that can act competently in physical space, which is also why it connects directly to [humanoid robotics](/ai/humanoid-robotics-2026/) and [multimodal AI that goes beyond vision](/ai/multimodal-ai-beyond-vision/). I want to understand what comes after the language-only era before it arrives, not after.

### 4. The agent economy

The fourth move is what happens when the first three mature. Once agents are reliable enough to trust, secured enough to give real access, and evaluated well enough to deploy, the next question is what they do with each other.

I have started on this with a look at [agents that buy and sell](/ai/agent-economy-buy-sell/) and the broader idea of [the engineer as a curator of agent-first systems](/ai/agent-first-architecture-engineer-as-curator/). The open questions are concrete: what does identity, payment, and reputation look like when the transacting parties are software; what contracts are enforceable; and what infrastructure has to exist before machine-to-machine commerce is anything other than a demo. This is further out than the other three, but it is the logical destination, so it belongs on the map.

### A planning input, not a forecast: AGI timelines

One more thing sits across all of this. I do not treat AGI timelines as a prediction to get right - that game is mostly ego. I treat them as a planning input.

The useful exercise is conditional. If broadly capable autonomous systems are three years away, the rational thing to research now is security, evaluation, and orchestration - the scaffolding for systems you cannot fully supervise. If they are fifteen years away, fundamentals compound and the scaffolding can wait. I have written around the edges of this in [the next decade of AI](/ai/the-next-decade-of-ai/), [recursive self-improvement](/ai/recursive-self-improvement/), and [AI safety from first principles](/ai/ai-safety-first-principles/). The honest position is that I do not know the timeline - but knowing how my priorities *should* shift under each one is itself the research.

------------------------------------------------------------------------

## What I am deliberately not chasing

A research map is only honest if it names what is off it.

There are areas I find genuinely interesting that I have decided not to make active research, because they are too far from anything I can build with or test against right now. **Quantum machine learning** is the clearest example - I want to know when qubits genuinely accelerate learning rather than just appearing in a press release, but that is a watch-list item, not a work-list item. **Neuromorphic and event-driven hardware** is the same: real, promising, and not yet close enough to my work to earn deep time. **Machine consciousness** is a question I think matters, but it is a philosophical one, and I would rather hold it lightly than pretend I am researching it.

The point of writing these down is not modesty. It is that "watching" and "researching" are different activities, and blurring them is how you end up shallow on everything. I check in on these. I do not pretend to be deep on them.

------------------------------------------------------------------------

## How I actually do this

The method behind the map is unglamorous and it is most of why it works.

I write to find the gaps. Drafting a post is the fastest way I know to discover which parts of an idea I only thought I understood - the paragraph I cannot write cleanly is the question that is not actually answered yet.

I build small things against each question. A research item with no artefact attached tends to stay vague. A tiny harness, a throwaway agent, a measured comparison - something concrete - is what turns reading into knowing.

And I let the questions feed each other. Reliability led to context engineering. Context engineering led to economics. Reliability is now leading to security. A good map is not a list of separate subjects; it is a chain, and each answered question tends to hand you the next one.

------------------------------------------------------------------------

## The through-line

Looking at the whole map, there is one thread running through all of it: I am not really researching AI in the abstract. I am researching the conditions under which it can be trusted to do real work.

Reliability is trust in the system. Context engineering is trust in what the model is reasoning over. Economics is trust that it is sustainable. Security is trust under an adversary. Evaluation is trust that you measured the right thing. World models are trust extended into physical reality. The agent economy is trust between machines.

That is the actual subject. Everything on the map is a different angle on the same question: what has to be true before you can hand a non-deterministic system a real job and walk away.

I do not have that fully answered. But I know which questions get me closer, I know which ones I have parked, and I know what I am working on next. For a field that produces this much noise, having a map you actually chose feels like the only sane way to work.

## Related Reading

- [Context Engineering: The Discipline That Replaced Prompt Engineering](/ai/context-engineering/)
- [The Agent Reliability Problem: Debugging Non-Deterministic Systems](/ai/agent-reliability-debugging-non-deterministic/)
- [AI Evals Are Broken: Why Benchmarks Stopped Measuring Real Capability](/ai/ai-evals-are-broken/)
- [Recursive Self-Improvement: Can AI Bootstrap Its Own Intelligence?](/ai/recursive-self-improvement/)
- [The Next Decade of AI: What Actually Happens From Here](/ai/the-next-decade-of-ai/)
