---
title: "When AI Gets Faster Than Human Review: What ChatJimmy's 17,000 Tokens a Second Hints At"
date: 2026-11-06T15:00:00+00:00
draft: false
tags: ["ai", "agent", "inference", "hardware", "devops", "governance", "future", "2026"]
description: "ChatJimmy, Taalas's demo of a model hardwired into silicon, answers almost instantly. The interesting question is not the chatbot. It is what happens to software engineering when the slowest part of the loop is a human reading a diff."
cover:
  image: /assets/images/ai/when-ai-gets-faster-than-human-review.jpg
  alt: When AI Gets Faster Than Human Review - a person at a desk facing walls of streaming code
---

## TL;DR

- ChatJimmy is a public demo from Toronto startup Taalas. It runs Meta's Llama 3.1 8B on custom silicon and Taalas claims up to 17,000 tokens per second per user
- That is a vendor figure for a small model, not proof that agents are about to run software autonomously
- My argument: as generation gets cheap and fast, the scarce resource in engineering stops being typing speed and becomes **review capacity**
- Two outside sources I read, the OECD and an Australian government report, point the same way: oversight has to be built into the system, not bolted on as a person watching
- Everything after "My read" is opinion, and the scenarios in it are hypothetical

## What ChatJimmy is

[ChatJimmy](https://chatjimmy.ai) is a chatbot demo from Taalas. [OfficeChai's report](https://officechai.com/ai/taalas-chat-jimmy) from 22 February 2026 describes it as running Llama 3.1 8B on Taalas's custom silicon, with an inference API alongside it. The reported claims are:

- 17,000 tokens per second per user, against roughly 1,800 on leading GPU-based systems
- Some test queries answered in 0.044 seconds, at 15,800 tokens per second
- About 20 times cheaper to build and about 10 times less power than comparable GPU infrastructure

[Taalas's own product page](https://taalas.com/products/) lists the HC1 as a "Technology Demonstrator" that "Runs Llama 3.1 8B model" and claims "17k tokens per second per user". The page notes the tests were run in Taalas's own labs, so these are vendor numbers. I covered the chip, the AMD acquisition and the caveats in more detail in [Taalas and AMD: Hardwiring an AI Model Into Silicon](/ai/taalas-amd-hardwired-ai-chips/). The short version of the caveats: the model is small and not state of the art, the chip cannot run anything else, and it uses aggressive quantisation.

So this post is not about whether ChatJimmy is the future. It is about what its speed makes you notice.

## The tell: you stop watching the output

Streaming text, the word-by-word effect we are all used to, exists to hide latency. At ChatJimmy's speed there is nothing to hide. The answer is just there.

That small change in experience is a clue to a bigger one. Much of how we work with AI today is shaped around its slowness. We wait, we read as it types, we interrupt, we go and make tea. If generation becomes close to free in time, the waiting moves somewhere else, and it moves to us.

## My read: review capacity is the new bottleneck

This section is my opinion, not reported fact.

Think about a normal engineering loop: write, review, test, deploy, watch. For decades the first step was the slow one, so we built whole professions around making it faster. Now imagine the first step costing almost nothing. The loop does not get five times faster. It gets stuck on the steps that need a person to understand something.

I think of it as a **review budget**. A team has a fixed number of hours a week in which humans can genuinely read, understand and accept changes. Today, writing code eats most of the time and review gets the remainder. If an agent can produce candidate changes in seconds, the supply of changes can exceed the review budget by orders of magnitude. Then there are only three options:

1. **Let the queue grow.** Changes pile up unreviewed. Nothing ships and the speed is wasted.
2. **Approve without understanding.** Rubber-stamping becomes the default. This is the dangerous one, because it looks like progress.
3. **Move the checking into the system.** Automated verification, limits on what agents may touch, staged rollouts, automatic rollback. Humans review the rules and the exceptions, not every change.

Only the third works at scale, and it is a very different discipline from the one most teams practise today.

## A hypothetical, clearly labelled

To make this concrete, here is an invented scenario. It has not happened to anyone I know of.

A team runs several agents with deploy rights. One fixes a production bug and ships the patch. A second, tuned for performance, rewrites a database query. A third notices the new query pushes load somewhere else and changes an infrastructure setting. A fourth sees odd behaviour and "corrects" it. Each decision is individually reasonable and each passes its tests. Together they leave the system in a state none of the agents, and no human, ever designed.

The point is not that any one agent was wrong. It is that the interaction was nobody's job to review. And at machine speed, that can all happen before anyone has opened a laptop.

## What the outside sources say

I do not want to lean only on my own speculation, so here is what two serious sources I actually read say about this problem space.

**The OECD.** In [Putting agentic AI systems to work](https://oecd.ai/en/wonk/putting-agentic-ai-systems-to-work-what-practitioners-reveal-about-deployment-and-governance) (OECD.AI, 24 September 2026), Sara Rendtorff-Smith and Yuko Harayama report on interviews with 25 organisations. Their finding that stands out for this topic: "none of the participating organisations reported deploying agentic AI with unrestricted autonomy." Deployments cluster where tasks are well defined, results can be checked and mistakes are contained or reversible, with human approval at high-impact or irreversible steps. They also describe layered safeguards, such as sandbox testing, least-privilege access and continuous monitoring, and say monitoring should cover intermediate actions, not only final outcomes. On accountability they note that traceability gets harder in multi-step, multi-agent workflows, which makes it difficult to find where a failure started.

**The Australian Government.** The Department of Industry, Science and Resources published [Risks and controls for multi-agent systems](https://www.industry.gov.au/publications/risks-and-controls-multi-agent-systems), prepared by the Gradient Institute, in August 2026. I could not load the full report during research, so I am relying on the landing page and search summaries rather than the text. As summarised, its core argument is that failures in multi-agent systems cannot be found by examining agents one at a time, so analysis has to cover how they interact, and its controls are grouped by whether they prevent, detect or mitigate failures. Cascading failures, where one agent's error spreads through the links to others, are one of the concerns. Treat that as a pointer to the report, not a substitute for reading it.

Neither source says "agents will run your production systems unattended by next year". Both say, in different words, that autonomy needs to be bounded and observable. That is the mirror image of the review budget problem: if humans cannot review everything, the system must be designed so they do not have to.

## Speed is not the same as autonomy

One caution on my own argument. 17,000 tokens per second does not mean 17,000 decisions or deployments per second. Real agents spend most of their time waiting on tools, builds, test suites and network calls, and a fast model does nothing about those. A faster model also does not make a small 8B model better at judgement.

What it does change is the economics. When fast inference is cheap, running a reviewer agent on every change, or ten agents trying ten approaches, stops being an extravagance. That is the part I find interesting: not one superfast agent, but a lot of cheap ones checking each other.

## What I would want in place first

If I were setting up a team for this world, in rough order:

- **Bounded permissions.** Each agent gets the least access it needs, and nothing that can delete data or change its own limits.
- **Independent verification.** The thing that proposes a change should not be the only thing that decides it is safe. A separate checker, ideally a different model or a deterministic test, gets a veto.
- **Staged rollout with automatic rollback.** Small blast radius first, with pre-agreed conditions that revert without asking.
- **A rate limit on change.** A cap on how many changes can land in a window, so the system stays understandable. Speed should be something you spend on purpose.
- **Traceability.** Every agent action logged in a form a human can follow afterwards, because the OECD's point about hard-to-trace failures applies to your own systems too.
- **Human authority over the irreversible.** Deleting data, moving money, changing access: a person decides.

None of this is glamorous, and most of it is the old reliability engineering playbook applied to a new kind of actor. I wrote about adjacent ideas in [DevOps in the Age of AI Agents](/devops/devops-in-the-age-of-ai-agents/) and [Securing AI Agents](/ai/securing-ai-agents/).

## Where I land

The headline number on ChatJimmy is impressive, but I think the lasting lesson is about us rather than the chip. For most of computing history, machines were the slow part and people were the patient part. Hardware like this hints at the reverse for at least some tasks.

The winners in that world will not be the teams who generate the most changes. They will be the ones who can say, with evidence, why a change is safe without a person reading every line. I suspect the best engineers of the next few years will be recognised less for how fast they write code and more for how well they design the checks around it.

I could be wrong about the timing, and a hardwired 8B model is a long way from a frontier agent. But if tokens get this fast and this cheap, the question of how much oversight we can engineer in advance stops being theoretical.

## Sources

- [OfficeChai: Taalas Builds Custom Chips For AI Models, Releases ChatJimmy App](https://officechai.com/ai/taalas-chat-jimmy) - ChatJimmy description and claims, 22 February 2026
- [Taalas: Products](https://taalas.com/products/) - HC1 specification and the 17k tokens per second claim
- [OECD.AI: Putting agentic AI systems to work](https://oecd.ai/en/wonk/putting-agentic-ai-systems-to-work-what-practitioners-reveal-about-deployment-and-governance) - autonomy, oversight and accountability findings
- [Australian Department of Industry, Science and Resources: Risks and controls for multi-agent systems](https://www.industry.gov.au/publications/risks-and-controls-multi-agent-systems) - summarised from the landing page and search results; full report not read
- [ChatJimmy](https://chatjimmy.ai) - the demo itself

## Related Reading

- [Taalas and AMD: Hardwiring an AI Model Into Silicon for 17,000 Tokens a Second](/ai/taalas-amd-hardwired-ai-chips/) - the chip behind ChatJimmy
- [DevOps in the Age of AI Agents](/devops/devops-in-the-age-of-ai-agents/) - how operations changes when agents act
- [Securing AI Agents](/ai/securing-ai-agents/) - permissions and controls for autonomous agents
