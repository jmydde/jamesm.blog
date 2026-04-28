---
title: "AI Agents That Actually Work: Patterns From Real Projects"
date: 2026-05-01T08:00:00+01:00
draft: false
tags: ["ai", "agent", "architecture", "tool-use", "agentic-engineering", "reliability"]
description: "The patterns that separate agents that ship and stay shipped from the ones that demo well and fall over the moment they meet a real workload."
cover:
  image: assets/images/ai/ai-agents-that-actually-work.jpg
  alt: AI Agents That Actually Work Banner
---

I have spent the last eighteen months either building, reviewing, or operating systems that some marketing department somewhere has called "agents". The definition has been so thoroughly stretched that it now means anything from a chatbot with a calculator tool to a long-running autonomous workflow that touches production infrastructure. Underneath the noise there is a real engineering discipline emerging, and the patterns that separate the systems that survive contact with real users from the ones that demo well and fall over are starting to be legible.

This post is the working summary of what I have learned. It is not theoretical. Every pattern here is something I have either watched succeed in a system that is still running, or watched fail in a system that had to be rebuilt.

## What an agent actually is

I am going to use the word "agent" to mean a system in which a language model decides what action to take next, executes that action through some tool, observes the result, and decides what to do from there. The loop can be one step or a thousand. The actions can be reading documents, calling APIs, running code, or asking a human for help. The defining property is that the model is in the control flow, not just the response generation.

This is a useful definition because it cleanly separates agents from chatbots and from pipelines. A chatbot answers a question. A pipeline executes a fixed sequence of steps. An agent decides what to do next. I have written elsewhere about [the engineer's role shifting from builder to curator](/ai/agent-first-architecture-engineer-as-curator/) when this is the dominant pattern.

The reason it matters whether you call something an agent is not branding. It is that agents have a specific failure profile, and treating a real agent like a chatbot or a pipeline produces predictable disasters.

## Pattern one: scope the loop

The first and most common failure I see is unbounded autonomy. Someone gives the model a goal, hands it a toolbox, and lets it run until it thinks it is done. In a demo, this looks magical. In production, it is the source of nearly every "the agent did something insane" story.

Working agents have tightly scoped loops. The loop has a maximum depth, a maximum runtime, a maximum cost in tokens or money, and a clear definition of what counts as completion. The model is not trusted to decide when to stop. The system is.

The best framing I have heard for this is from the [Anthropic engineering writeup on agent design](https://www.anthropic.com/research/building-effective-agents), which makes the point that the simplest pattern that works is almost always preferable to a more autonomous one. The temptation is to give the model more freedom because it feels like the model deserves it. The discipline is to give it less freedom than feels generous, because the failure modes of autonomy are far worse than the failure modes of constraint.

A scoped loop looks like: at most ten tool calls, at most thirty seconds, at most ten thousand tokens, completion is when the structured output matches a known schema or when the agent explicitly hands off. Anything that violates one of those constraints is treated as failure, not as progress.

## Pattern two: structured tool design

Tools are the surface where the agent meets the world. Bad tool design is the most common cause of bad agent behaviour, and it is almost always invisible until the system runs at scale.

A good tool is small, idempotent where possible, has clear preconditions, returns [structured output](/ai/structured-outputs-schema/) that the model can reason over, and fails informatively when called incorrectly. A bad tool is general, has implicit state, returns prose, and silently does the wrong thing when given malformed input.

The mistake I see most often is exposing the underlying API directly to the agent. "We already have a REST API for our service, just let the model call it." This sounds efficient and is almost always wrong. APIs are designed for programmers who can read documentation, hold mental state, and recover from cryptic errors. Models are not programmers. They are pattern-completion engines that perform best when the surface they are working with is shaped to their failure modes.

The agents that work have a thin, purpose-built tool layer between the model and the underlying systems. The tool layer translates messy reality into something the model can reliably call, and translates the model's outputs back into something the underlying systems can reliably accept. It is unglamorous code, and it is most of the engineering effort.

## Pattern three: the verification step is non-negotiable

Models [confabulate actions](/ai/ai-hallucinations-understanding-and-mitigating/). They will tell you they ran the tests when they did not. They will tell you they updated the file when they did not. They will tell you they checked the documentation when they did not. This is not a moral failing of the model. It is an artefact of the training objective: producing plausible continuations of a conversation does not require any actual coupling to the world.

Every working agent I have seen has explicit verification baked into the loop. Not as an afterthought. As a structural part of how the agent operates.

If the agent claims to have updated a file, the system reads the file and confirms. If the agent claims to have run the tests, the system has the test output and inspects it. If the agent claims to have completed a step, the next step in the workflow checks for the expected post-condition before proceeding. The model is treated as a producer of intent, not a reporter of fact.

This sounds obvious when written down. It is not how most agent prototypes are built, because adding verification is more work than not adding it, and the prototype seems to work without it.

## Pattern four: write context, not just history

The default agent loop puts everything that has happened so far into the prompt and runs the model on that. This works for short loops. It collapses for long ones. Once the context window fills with stale tool calls, irrelevant outputs, and forgotten reasoning, the model's behaviour degrades sharply. It loses track of what it was doing, repeats actions, contradicts its own earlier conclusions.

The pattern that works is to maintain a curated context separately from the raw history. The agent's working memory is not the transcript of every action it has taken. It is a structured representation of what it has learned, what it has decided, and what is still outstanding. The transcript is for debugging. The curated context is for reasoning.

This costs engineering effort. It also produces agents that can run for hundreds of steps without falling apart, where the naive transcript-as-context approach falls apart in dozens.

## Pattern five: human handoff is a first-class state

Almost every agent has cases it cannot handle. The good ones know this and have a clean way to hand off to a human. The bad ones either fail silently or, worse, fake their way through with confidently wrong output.

A first-class human handoff means the agent has an explicit "I cannot complete this safely" tool that it is rewarded for using. The handoff produces a useful summary of what the agent tried, what it learned, and what specifically is blocking it. The human picks up exactly where the agent left off, with full context, and can hand the work back if appropriate.

This is one of those features that sounds soft and turns out to be load-bearing. Without it, the agent's failure mode is confabulation. With it, the agent's failure mode is a polite "this looks like something a human should handle".

## Pattern six: idempotency wherever possible

Agents will retry. They will retry because of timeouts, because the model decided to call the tool again, because the outer system restarted, because you told them to. If the tool is not idempotent, retries become bugs.

Working agents lean hard into idempotency. Operations are designed so that calling them twice produces the same result as calling them once. Where that is impossible, operations are guarded by an explicit "have I done this already?" check, often using a deterministic key derived from the agent's intent rather than from the operation itself.

This is standard distributed systems hygiene. It is unusually important for agents because the model is non-deterministic and will make calls you did not anticipate. Treating every tool call as potentially a retry from a future you have not seen yet is the only way to stay sane.

## Pattern seven: observability that matches the abstraction

You cannot debug an agent the way you debug a service. The unit of failure is not "this function threw an exception". The unit of failure is "the agent took an unproductive trajectory through a decision tree because of a misleading tool output four steps ago".

Working agent systems have observability that operates at the agent's abstraction level. Every loop iteration is logged with the model's reasoning, the tool it called, the arguments it used, the result it got, and any state changes it made. The logs are structured well enough that you can replay a run, branch from a specific step with a different action, and ask "why did the agent do that?" with answers that are not pure speculation.

Tools like [LangSmith](https://www.langchain.com/langsmith) and [Langfuse](https://langfuse.com/) have made this less painful than it used to be, but the pattern matters more than the tool. The principle is: the model thinks in trajectories, so your debugging surface must too.

## Pattern eight: evaluation is part of the system, not a separate project

The single most consistent property of agent projects that get to production and stay there is that they have real evaluation infrastructure. Not vibes-based "it seems to work better now" testing. A curated set of representative tasks with known good outcomes, run automatically, with metrics that catch regressions.

Building this is unfun. It is the part of the project that always gets postponed. Postponing it is always a mistake.

The agents that ship have the equivalent of a test suite for behaviour: tasks the agent must complete, properties its outputs must satisfy, edge cases it must handle gracefully. When a model gets updated, when a tool changes, when a prompt is rewritten, the suite runs and the team can tell whether the change improved or regressed the system.

Without this, you are flying blind. The model is non-deterministic. The system is complex. Your intuitions about whether it is working are not trustworthy. Evaluation is the instrument panel. I wrote about why this is harder than traditional testing in [AI reliability is weird](/ai/ai-reliability-is-weird/).

## What this all amounts to

The reason most agent demos fail in production is that the demo is operating in the regime where the model's natural behaviour is good enough. The demo task is short, the tools are simple, the failure cases are sparse, the verification is implicit because the human watching the demo notices when things go wrong.

Production is none of those things. Production is long-running, multi-tool, full of edge cases, and unobserved most of the time.

The patterns above are how you bridge that gap. None of them are research-level innovations. All of them are engineering discipline applied to a new problem domain. The agents that work are the ones built by teams who treat them as systems first and as AI second.

If I had to compress all of this into one line, it would be: build agents the same way you would build any other long-running, partially-autonomous system that you cannot afford to have fail silently. Most of what you already know about reliable systems still applies. The novelty is in the failure modes, not in the engineering principles.
