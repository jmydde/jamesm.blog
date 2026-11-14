---
title: "I've Stopped Organising My Thoughts Around My Tools. My AI Agents Have Adapted to Me."
date: 2026-11-14T09:13:45+00:00
draft: false
tags: ["ai", "agent", "workflow", "productivity", "voice", "git", "github", "idea"]
description: "A personal account of running several AI agents in parallel, talking to them out loud, and letting the workflow adapt to how I think instead of the other way around."
cover:
  image: /assets/images/ai/ai-agents-that-adapt-to-how-i-think.jpg
  alt: Illustration of several AI agent windows (code writer, debugger, PR creator, idea organiser, router and synthesizer) working in parallel around the title "I've Stopped Organising My Thoughts Around My Tools. My AI Agents Have Adapted to Me."
---

This is a personal post about my own setup, not a report on anything happening in the wider industry. Something has changed in the way I work at home over the last few months, and I don't think it comes down to better models or cleverer prompts.

It comes down to having a workflow that adapts to the way I think. The real gain isn't autonomous agents writing code faster. It's less cognitive overhead between having an idea and acting on it.

![Illustration of several AI agents working in parallel: a code writer in its own Git worktree, a debugger, a PR creator, an idea organiser and a router sending thoughts to the right agent](/assets/images/ai/ai-agents-that-adapt-to-how-i-think.jpg)

## TL;DR

- I run several AI agents at once, each in its own window with its own context, tasks and responsibilities.
- I rarely write careful prompts any more. I think out loud, often by voice, and let the agent work out the rest.
- My agent workflow now routes loose, unrelated thoughts to the right agent instead of treating everything as part of the current conversation.
- Development work happens in isolated Git worktrees, on separate branches, and ends in a GitHub pull request that I review.
- I'm enjoying the extra time for brainstorming, problem solving, design and taste, and I like reviewing the finished work.
- The long-term role of humans in software feels uncertain to me, but for now I still feel like an important part of the process.
- It is not perfect. Agents still misread context and misroute things, and I still make the decisions.

## Parallel agents, each with its own job

I can now have several agents working on completely different things at the same time. One might be building a feature for an application, another investigating an issue, another reviewing requirements. Meanwhile I'm already thinking about something unrelated.

That is where it gets interesting, because the hard part of working this way was never starting the agents. It was keeping track of them.

## I don't really prompt any more. I just think out loud.

One of the things I enjoy most is opening an agent window and dumping thoughts into it as they occur to me. Sometimes it's a fully formed idea. Sometimes it's half a sentence, a random observation, or a problem I've spotted. I go back and forth with the agent, challenge its suggestions, change direction and add context. It feels much closer to talking with a colleague than using a traditional software tool.

I also use MacWhisper and other speech-to-text tools to talk to my agents directly. Often it is quicker to say what I'm thinking than to stop and type it out.

I don't sit down with a carefully constructed prompt and a clearly defined objective. I just start talking, and increasingly that is enough.

## The agents have learned to work around my thought process

This used to be a nightmare. With multiple AI sessions, context matters enormously. You have to remember which window you're in, which project you're discussing, what the agent knows, and whether you're about to drop something unrelated into the wrong conversation.

I kept catching myself thinking about one project while prompting an agent working on another. Or having an idea I didn't want to lose and not knowing where to put it.

So I spent a good amount of time building out my agent workflow to deal with exactly that. The agents now understand much more about how I work: the projects I'm involved in, how I approach problems and, importantly, that my thoughts don't arrive in neat, organised packages.

I can throw something fairly random into a conversation and the system can work out where it belongs, which agent should handle it and what needs to happen next. It redirects the work to the appropriate agent rather than blindly treating everything as part of the current conversation.

It's not perfect, and there is plenty left to improve, but it has already made a massive difference.

## I don't need to worry about how everything gets built

The other half of the setup is how the agents handle the engineering. When an agent picks up a development task, it works in its own isolated Git worktree, on a separate branch, so it doesn't interfere with anything else in flight.

It investigates the problem, makes changes, writes and runs tests, reviews its own work and ultimately raises a GitHub pull request. That lets me have several pieces of development progressing in parallel without worrying about conflicting changes or holding it all in my head.

I still review the work, make the decisions and steer. I'm not suggesting everything can be blindly delegated. But I'm moving away from thinking about every implementation detail. I can concentrate on what needs building, why it matters and whether the proposed solution makes sense, while the agent works out how to implement and test it.

## My brain has become an idea-generation engine

Perhaps the biggest change is in my own thinking. I'll explore an idea with one agent, spot an opportunity for something else, open another window and start on that. A few minutes later I'll remember an unrelated problem, drop it into the right conversation and carry on.

I'm no longer forcing myself through a rigid sequence of tasks. My mind can jump between ideas, problems and opportunities without stopping to organise everything first.

Before, I'd often interrupt a train of thought to document something properly, create a task, work out where it belonged or decide which tool to use. Now I can just capture it. The agents help turn rough thoughts into something structured, investigate the options, challenge the idea, gather requirements and eventually start building. I can move on knowing the idea hasn't vanished into a forgotten notes document.

I genuinely love that.

## What I'm enjoying most: more time to think

The part I didn't expect is how much I enjoy what I now get to spend time on. I have more room to brainstorm ideas, to work through problems, and to think about design, including my own tastes and preferences. Those are the questions I find most interesting, and they used to get squeezed by the mechanics.

I also like reviewing the work at the end. Looking at what an agent has produced, deciding whether it is right, whether it feels right, and what I'd change is satisfying in its own way. It is where my judgement and taste actually matter.

## Not replacing developers, changing where the effort goes

I still enjoy the engineering side. I want to understand the architecture, challenge decisions, review implementations and make sure things are built properly.

What I don't want to spend my time on is manually coordinating every little step. I'd rather think about what we could build, which problems are worth solving and what better ideas might look like. The agents take on a growing share of the execution and coordination. I'm still responsible for direction and decisions, but I'm no longer the bottleneck for every individual piece of work.

I think that is where things are heading, though that is my own read rather than a prediction I can point to evidence for.

## Where do humans fit?

Honestly, it feels uncertain what role humans will have in software in the future. For now, though, I still feel like a very important part of the process, and I hope that stays true for at least the next few years.

I'm fairly optimistic about where this goes. My guess is that anyone will be able to build anything, and what will matter is having the ideas and the passion to build them. Again, that is my own speculation, not something I can prove.

I can also imagine a lot of software ending up being built for agents rather than for people, since agents don't need a flashy UI. But for now I'm enjoying building solutions for myself and other humans as well as for agents.

## Only just getting started

My setup is far from perfect. Agents still misunderstand context, route things incorrectly or need more direction. There is real work left on reliability, coordination, quality control and knowing when something genuinely needs a human.

Even so, I find it hard to imagine going back. The breakthrough wasn't getting AI to write code faster. It was being able to think freely, explore ideas as they arrive, run several conversations at once and trust that a capable system is working out how to turn those thoughts into something tangible.

I want to spend my time thinking about what is possible, not managing the mechanics of making it happen. For the first time, my tools are starting to work the way my brain does, rather than the other way around.

## Related Reading

- [A Year of Agents, and What is Coming Next](/ai/year-of-agents-and-whats-next/)
- [AI Agents That Actually Work: Patterns From Real Projects](/ai/ai-agents-that-actually-work/)
- [Agent-First Architecture: The Engineer as System Curator](/ai/agent-first-architecture-engineer-as-curator/)
