---
title: "The Next Decade of AI: What Actually Happens From Here"
date: 2026-04-19T07:55:00+01:00
draft: false
tags: ['ai']
description: "Most predictions about the future of AI are either utopian or apocalyptic. The real trajectory is stranger and more interesting than both - and it's already visible if you look at what's quietly working right now."
cover:
  image: /assets/images/ai/ai-intelligence.jpg
  alt: AI Intelligence Banner
---

Most predictions about the future of AI fall into two flavours. One camp says we are months away from machines that can do everything a human can do, and we should brace for either paradise or extinction. The other camp says the whole thing is a bubble, the models have plateaued, and in five years we will be talking about something else.

Both are wrong, and both are wrong for the same reason. They are trying to forecast a single headline event - arrival of AGI, collapse of the hype - when the actual future of AI is not an event. It is a slow, uneven transformation of how ordinary work gets done.

The more interesting question is not "when does AI get scary-smart?" It is "what does the world look like in ten years when the stuff that already works today is everywhere, refined, embedded, and cheap?"

That future is already visible if you look closely. Here is what I think actually happens.

## Intelligence Becomes Boring

The first thing that happens is that AI stops being a topic.

Right now, we still talk about "using AI" the way we talked about "using the internet" in 1999. It is a thing you do, a category of activity, a button you click. In ten years it will be a property of almost every piece of software you touch, mostly invisible, like spell-check or autocomplete or search.

When something becomes infrastructure, it disappears. Nobody writes blog posts about electricity. Nobody goes to a conference about "using TCP/IP in the enterprise." The exciting stuff migrates to the application layer, and the underlying capability just hums along in the background.

I wrote about this shift in [We Are Learning to Buy Intelligence](/ai/we-are-learning-to-buy-intelligence). The commodification is not speculative. It is happening in real time, model by model, quarter by quarter. The price per unit of useful reasoning keeps falling. The capability per dollar keeps rising. And once something follows that curve for long enough, it stops being a product and starts being a utility.

The surprising implication is that most of the companies currently branded around "AI" will not exist in ten years - not because they fail, but because the adjective stops making sense. The companies that survive will be the ones that built something useful *with* the AI, the same way the companies that survived the dot-com era were the ones that built something useful with the internet, not the ones with "dot com" in their name.

## The Agent Layer Eats the Interface

The second thing that happens is that the interface to software stops being the interface.

Today, when you want a computer to do something, you open an application and click around. You are the orchestrator. You hold the plan in your head. You know that to process this expense claim you open the portal, upload the receipt, tag the project, submit, and follow up if it bounces.

That model is going to erode. Not disappear - there will always be things you want to touch directly - but erode at the edges. For a growing share of tasks, the interface will be a conversation with an agent that knows what you want, has access to the tools, and does the clicking for you.

This is the direction the serious work is heading. [Cline](/ai/cline/), [Claude Code](/ai/claude-code-review/), [GitHub Copilot](/ai/github-copilot/), and the whole generation of agent frameworks behind them are early versions of this pattern. They are not chatbots. They are something new: software that takes a high-level intent and produces a low-level result, by driving other software on your behalf.

In [The Architect vs The Builder](/ai/architect-vs-builder/) I argued that the human role shifts from execution to direction. The next decade makes that shift general. Not just in coding. In finance, in operations, in research, in customer support, in logistics. Anywhere there is a sequence of deterministic steps connecting an intent to an outcome, an agent will eventually be cheaper, faster, and less error-prone than a human doing the same thing.

The interesting consequence is that the SaaS dashboard - the dominant software metaphor of the last twenty years - starts to look dated. Why build a dashboard with forty buttons when the user is going to ask an agent to do the thing, and the agent is going to press the buttons for them? The pressure on software vendors to expose clean, machine-readable APIs and primitives will become overwhelming, because the real customer is increasingly not a human but an agent acting on a human's behalf.

## The Bottleneck Moves to Judgement

The third thing that happens is the one I find most interesting: the scarce resource changes.

When generating a plausible answer is cheap, the value of generating one drops to near zero. What stays valuable - what actually becomes *more* valuable - is knowing which answer is the right one.

I wrote about this in [Taste Is the New Scarcity](/ai/taste-is-the-new-scarcity). A model can produce a thousand strategies, a thousand designs, a thousand implementations. It cannot tell you which one is worth pursuing. That is a human call, and it is a call that depends on context, judgment, relationships, risk tolerance, and accumulated experience that no amount of training data can substitute for.

[What Does 'Expertise' Mean When AI Can Pass Any Exam?](/ai/expertise-after-ai) pushes on the same point from a different angle. The exam-based definition of competence is dead, because the exam tests knowledge retrieval and the machines are better at knowledge retrieval than we are. What is left when retrieval is free is the thing exams never measured in the first place: the ability to make a call, own the consequences, and do it again tomorrow.

In the next decade, hiring, education, credentialing, and professional identity all get restructured around this shift. It will be messy. Professions that defined themselves by their knowledge monopoly - law, accountancy, parts of medicine - will have to decide what they actually stand for now that the knowledge is free. The ones that adapt will come out stronger, because they will be valuing what their best practitioners were always really paid for. The ones that don't will commoditise themselves.

## The Local/Cloud Split Becomes Permanent

The fourth thing that happens is that AI splits into two distinct species.

On one side, you have the frontier models. These run in enormous data centres, cost billions of dollars to train, and push the boundary of what is possible. They are where the headlines come from. They will continue to grow, and the gap between them and what you can run on your own hardware will, if anything, widen.

On the other side, you have small, local, specialised models. These run on your laptop, your phone, your home server, your car. They are nowhere near as capable as the frontier, but they are shockingly good at the narrow things they are tuned for, and they have three enormous advantages: they are private, they are instant, and they are free at the margin.

I explored this in [Local vs Cloud AI 2026](/ai/local-vs-cloud-ai-2026), [GPU Servers vs API Credits](/ai/gpu-servers-vs-api-credits), and the [Mac Studio Local LLM Guide](/ai/mac-studio-local-llm-guide). The pattern is already clear. For sensitive data, for low-latency interactions, for high-volume automation, and for anything where you do not want to be dependent on a vendor's pricing and uptime, local wins. For anything that needs the absolute state of the art, cloud wins.

The mistake is thinking you have to pick a side. The real architecture, and the one that wins in the next decade, is hybrid. Small models handle most of the traffic locally. Cloud models handle the hard problems. A routing layer decides which is which. Your data stays on your machine unless it has to leave, and even then it leaves in a form that preserves what matters.

This is not speculative. It is what the serious practitioners are already building.

## Costs Do Not Drop the Way People Think

The fifth thing is a correction to a widespread assumption. The cost *per unit of intelligence* is collapsing. The cost *of using AI meaningfully* is not.

I wrote about this in [Token Economics: Why Costs Aren't Going Down](/ai/token-economics-why-costs-arent-going-down). The model per-token price keeps falling. But the amount of tokens we throw at each problem keeps rising even faster. Agentic workflows that used to be a single prompt now involve dozens of steps, tool calls, planning loops, and verification passes. Context windows have grown from a few thousand tokens to millions, and people are filling them.

Net effect: the bill stays roughly the same, or goes up. The intelligence you get for that bill goes up much more. It is a better deal, but it is not a cheaper deal in absolute terms, and the businesses that plan as though AI is about to be free are going to be surprised.

The companies that win here are the ones who treat inference cost as a first-class engineering constraint. Not as a line item to ignore, and not as a terror to flee from, but as a real budget to optimise against - the way we once optimised for memory or disk or bandwidth. Caching, batching, routing to smaller models when possible, and being willing to say "this does not need to be AI-generated" are all going to matter more, not less.

## Reliability Becomes the Unsolved Problem

The sixth thing, and the one the field is least ready for, is that reliability becomes the dominant engineering problem.

Capability gets all the attention. Reliability gets almost none. But as AI agents take over more and more of the actual doing - as they stop being co-pilots and start being operators - the question stops being "can the model do this?" and starts being "can I trust the model to do this a thousand times in a row without a weird failure?"

I wrote about this in [AI Reliability Is Weird](/ai/ai-reliability-is-weird). Our entire engineering discipline for reliability was built around deterministic systems. Unit tests, integration tests, assertions, SLOs. All of these assume the code does the same thing each time. Agentic systems do not. Same prompt, different output. Same plan, different execution path. Mostly fine, occasionally not, and the failure modes are subtle enough that you only notice them in production.

The next decade of serious AI engineering is going to be about inventing the tools and techniques to handle this. Property-based testing for agents. Statistical SLOs instead of binary pass/fail. Evaluation harnesses that measure distributions of behaviour, not single runs. Human-in-the-loop checkpoints at the places where the cost of being wrong is high. This is not glamorous work. It is also where the durable engineering advantage will be, because the companies that figure this out will be able to deploy agents safely into contexts that others cannot.

## The Human Shape of It

Put the six pieces together and the picture looks like this.

Intelligence is ambient. It is in everything, priced like a utility, and most people stop thinking about it consciously. The interface to software is increasingly a conversation with an agent that acts on your behalf. Human work shifts toward judgment, direction, taste, and responsibility - the things the machines cannot do. The infrastructure splits into a powerful, expensive frontier and a fast, cheap, private local layer, joined by hybrid architectures. Costs stay meaningful, forcing real engineering discipline. And reliability - not capability - becomes the hard problem that separates the winners from the also-rans.

None of that sounds like science fiction. It sounds like the logical continuation of what is already working.

There are deeper unknowns sitting beyond this horizon. What happens when agents start talking to other agents at scale, without humans in the loop? What happens when a model is good enough to do genuinely novel research, not just synthesise existing work? What happens to labour markets, to education, to politics, when the cost of producing plausible-looking content drops to zero? These are real questions, and I do not pretend to know the answers. Nobody does.

But you do not need to solve those to act well in the next ten years. You need to act on what is already true: intelligence is becoming infrastructure, agents are becoming operators, judgment is becoming the bottleneck, and the discipline of building reliably with non-deterministic components is becoming the craft.

The future of AI is not a moment. It is a direction. And the direction is already clear enough to start walking.

---

**Related reading:**
- [We Are Learning to Buy Intelligence](/ai/we-are-learning-to-buy-intelligence)  -  On the commodification of intelligence
- [Taste Is the New Scarcity](/ai/taste-is-the-new-scarcity)  -  What becomes valuable when intelligence is cheap
- [What Does 'Expertise' Mean When AI Can Pass Any Exam?](/ai/expertise-after-ai)  -  The expertise problem in an AI world
- [The Architect vs The Builder](/ai/architect-vs-builder/)  -  How the human role is shifting
- [AI Reliability Is Weird](/ai/ai-reliability-is-weird)  -  Why testing non-deterministic systems breaks old assumptions
- [Local vs Cloud AI 2026](/ai/local-vs-cloud-ai-2026)  -  The hybrid architecture that actually works

**External sources:**
- [Anthropic's research on agentic systems](https://www.anthropic.com/research)
- [Stanford HAI AI Index Report](https://hai.stanford.edu/ai-index)
- [The State of AI Report](https://www.stateof.ai/)
