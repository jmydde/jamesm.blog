---
title: "A Year of Agents, and What is Coming Next"
date: 2026-04-30T08:06:00+01:00
draft: false
tags: ["ai", "agent", "tooling", "workflow", "future", "productivity"]
description: "A look back at how AI tooling and agents shifted between April 2025 and April 2026, what is clearly coming in the next two years, and how the changes will reshape both work and personal workflows."
cover:
  image: assets/images/ai/a-year-of-agents-whats-next.jpg
  alt: A year of AI agents
---

A year ago, in April 2025, "AI in your workflow" mostly meant a chat window in a browser tab and an autocomplete plugin in your editor. You typed, it suggested, you accepted or rejected. The interaction model was small. The blast radius was small. The verb was "ask".

In April 2026, the verb is "delegate".

That is the headline, and it is not subtle once you go looking for it. The tools you use day to day no longer wait for prompts. They run for minutes at a time, open files, edit them, run shells, spin up sub-agents, browse the web, and come back with a result that is either roughly right or visibly wrong. You are no longer in the loop on every keystroke. You are in the loop on the outcome.

This post is a stocktake. What changed in the last twelve months, what is clearly coming in the next twenty-four, and what it does to the shape of a working day - both at work and at home.

------------------------------------------------------------------------

## What Changed in the Last Year

I want to be honest about how much of this snuck up on people. None of it was a single moment. There was no GPT-3-shaped thunderclap. It was a steady drumbeat of capability and ergonomics improvements, and the cumulative effect is that the tools now do qualitatively different work.

A rough taxonomy of what shifted:

**Coding agents went from "assistant" to "operator."** [Claude Code](https://www.claude.com/product/claude-code), [Cursor](https://cursor.com/), [OpenAI Codex](https://developers.openai.com/codex), and a long tail of open-source harnesses ([Cline](https://github.com/cline/cline), [OpenHands](https://openhands.dev/), [Goose](https://goose-docs.ai/), [Aider](https://aider.chat/)) all converged on the same shape: a long-running loop where the model plans, edits, runs, and reviews on its own, and the human judges the diff. The thing you tab between while you make coffee is not the same thing it was a year ago.

**Long-running, multi-step tasks became routine.** A task that takes thirty minutes of agent time was exotic in mid-2025. By the end of 2025 it was normal. Now sub-agents fan out, work in parallel, and report back to a coordinator. I have written about this shift in [Agent-First Architecture](/ai/agent-first-architecture-engineer-as-curator/), and the gist is that you spend less time writing code and more time deciding what should run and reviewing what came back.

**Standards started showing up.** Two are worth singling out. [MCP](https://modelcontextprotocol.io/) (the Model Context Protocol) has become the default way an agent talks to your tools - your filesystem, your database, your calendar, your issue tracker. And [Agent Skills](https://agentskills.io/) - a folder with a `SKILL.md` file - has become the default way you give an agent procedural knowledge that works across tools. Both are open. Both are boring on purpose. Both are the right kind of boring. I wrote up the skills story in [AI Skills: One Folder, Any Model](/ai/ai-skills-one-folder-any-model/).

**Spec-driven development stopped being a meme.** [GitHub's Spec Kit](https://github.com/github/spec-kit) and the broader pattern of writing a spec first, generating an implementation, and reviewing the diff is now how most teams I talk to actually run. The interesting move is that the spec is the artefact. The code is the by-product. That is a different mental model than "AI helps me write code."

**Context windows stopped being scarce.** A million tokens is normal. Several million is not unusual. Prompt caching means that loading a whole repo into context is cheap on the second turn. The economics of "let the model read everything before it answers" are no longer absurd. I wrote about this trajectory in [The LLM Context Window Arms Race](/ai/llm-context-window-arms-race/).

**Local AI stopped being a toy.** A Mac Studio with an M4 Ultra runs a 70B-class model fast enough to be useful. [Ollama](https://ollama.com/) and [LM Studio](https://lmstudio.ai/) made the install painless. The frontier still lives in the cloud, but a serious chunk of "small task, sensitive data" work now happens on a desk.

**Voice and multimodal got real.** Dictation that actually keeps up. Models that read a screenshot and act on it. Computer use that drives a browser well enough to book a flight or extract a number from a PDF. A year ago these felt like demos. Now they feel like features.

If you put all of that together, the change of state is the move from "AI helps me do my job" to "AI does parts of my job, and I supervise."

------------------------------------------------------------------------

## What is Definitely Coming in the Next Two Years

I want to be careful here. The track record of AI predictions is unkind to anyone who picks specific dates. So I am only going to list things where the trajectory is so well-established that the question is "when, exactly?" rather than "if at all?"

**Longer-horizon agents.** Today's agents reliably do tasks that take minutes, sometimes an hour. The frontier of useful is now several hours of unattended work. By 2027 a job-day of agent work, with reasonable check-ins, will be normal. Whether that means "writes a feature end-to-end" or "investigates a bug across three services and proposes a fix" depends on the day, but the direction is the same.

**Multi-agent systems as the default.** Single-agent runs are already starting to feel quaint. The shape that wins is a coordinator and a fleet of specialised sub-agents - one for research, one for code, one for review, one for tests - each running in parallel against the same goal. You will not write the agents. You will configure them.

**Personal AI with persistent memory.** The thing nobody has gotten right yet is an assistant that remembers what you told it last month without you having to remind it. The pieces are now in place: stable embeddings, cheap long context, MCP access to your calendar and email and notes. Within two years this is a product, not a research project. I sketched out where this is going in [Home AI Agent Memory That Lasts](/ai/home-ai-agent-memory-that-lasts/).

**Agents that drive your computer.** "Computer use" - the model controlling a real browser or a real desktop - was clunky in 2025 and credible in 2026. By 2027 the booking, scheduling, form-filling, expense-claim layer of work life is largely something you supervise rather than something you do. Most knowledge workers will spend less time in browsers because their agents will spend more.

**Cheaper inference, more capable small models.** The cost of a frontier-quality token is falling roughly tenfold per year, and there is no reason to think the curve flattens before 2028. Small models keep eating tasks the big ones used to monopolise. The interesting consequence: cost stops being the constraint on agent design. Latency and quality become the only things that matter.

**Robotics moving from demo to deployment.** Humanoid platforms - [Tesla Optimus](/ai/tesla-optimus-robot/), [Boston Dynamics Atlas](https://bostondynamics.com/atlas/), [Unitree G1](https://www.unitree.com/g1) - are the visible bit. The less visible bit is that the same model architectures driving software agents are starting to drive physical ones. Two years out, "an agent did it" stops being purely digital.

**Regulation catches up, unevenly.** The EU AI Act is in force. The US is patchwork. The UK is trying to thread the needle. None of this stops the trajectory, but it changes which products ship in which markets and how fast. Worth watching if your work crosses borders.

There are plenty of things I am genuinely uncertain about - whether we get a true general-purpose agent that holds together across weeks of work, whether AGI-shaped capabilities show up by 2028, whether the labour market reshapes faster than education can - but I would rather list the things I am confident about and stop there.

------------------------------------------------------------------------

## How This Changes the Working Day

The interesting question is not "what can the tools do?" but "what does the day look like?" Here is what I see, both in my own work as a [data engineer](https://en.wikipedia.org/wiki/Data_engineering) and in the teams I talk to.

**Less typing, more reviewing.** The unit of work shifts from "write a function" to "decide whether this diff is right." That is a different cognitive load. It rewards taste, judgement, and the ability to read code fast - skills that were always valuable but were never the bottleneck. They are now. I wrote about this in [Taste is the New Scarcity](/ai/taste-is-the-new-scarcity/).

**Specs become the artefact.** A clear, testable description of what you want is the new commit. The agent generates the code. You review the diff. The spec is what gets versioned, argued about, and revisited. If you are not already writing things down before you build them, you will be.

**Parallelism is real for individuals, not just teams.** A single engineer running three or four agents in parallel against three or four tasks is no longer notable. It is just Tuesday. The constraint is review bandwidth, not implementation bandwidth. People who can keep four threads of work in their head while reviewing the diffs as they land have a real edge.

**The "junior task" middle hollows out.** The work that used to be "give it to a junior to learn the codebase" is the work an agent does best. That has uncomfortable consequences for how careers start, which I have chewed on in [The Junior Developer Pipeline Problem](/ai/junior-developer-pipeline-problem/). It is not solved. It needs to be.

**Standups change shape.** "What I did yesterday" becomes "what my agents did yesterday and what I approved." Demos shift from "look at this code" to "look at these specs and the diffs the agents produced." The metabolism of a team gets faster in a way that is genuinely uncomfortable for the first few months.

------------------------------------------------------------------------

## How This Changes Life Outside Work

This is the bit that gets less coverage and matters more.

**Email, calendar, scheduling.** The amount of mental load you carry around for "who do I owe a reply to, when is that thing, did I confirm the booking" is going to shrink. Personal assistants with MCP access to your inbox, calendar, and a scratchpad of your preferences will do this layer. Not perfectly. Well enough that you stop noticing.

**Research and decisions.** Buying a flat, choosing a school, planning a trip, comparing pension providers. The work is currently slow, lonely, and dependent on whoever has the time to grind through PDFs. A capable assistant collapses the time cost by an order of magnitude. The decision is still yours. The legwork is not.

**Health and admin.** Reading lab results, summarising a consultant's letter, working out which insurance form to fill in, chasing the council about the bins. None of this is glamorous. All of this drains hours from a week. Agents will do almost all of it within two years, with you in the loop only when something matters.

**Learning.** A patient tutor who knows what you already know, has read the textbook, and can run examples on demand is now a real thing. The bottleneck on learning a new field stops being "find a teacher" and becomes "decide what you want to learn." That is a much better problem to have.

**The flip side: attention.** The same systems that save you hours can also fill them. Always-on agents, always-on summaries, always-on suggestions. The skill that compounds is knowing when to switch them off. I do not have a clean answer to this. It is something I am paying attention to.

------------------------------------------------------------------------

## What to Actually Do About It

A short list, because long lists in posts like this rarely survive contact with a Tuesday.

1. **Pick a stack and use it daily.** I have written up mine in [What Actually Belongs in My AI Dev Stack in 2026](/ai/what-actually-belongs-in-my-ai-dev-stack-2026/). The specifics matter less than the habit. You learn this by using it, not by reading about it.
2. **Write specs before code.** Even small ones. Even informal ones. The muscle of "describe what you want clearly" is the muscle that pays off everywhere else.
3. **Get good at reviewing diffs fast.** This is the new core skill. It is not glamorous and it is not taught. You build it by doing it.
4. **Move procedural knowledge into [skills](/ai/ai-skills-one-folder-any-model/).** Anything you do twice should be a skill. Anything in your head that a colleague would also benefit from should be in a folder, not in your head.
5. **Set up one personal agent.** Not for work. For your inbox, your calendar, your reading list. The shape of "AI in my life" makes a lot more sense once you have one running.
6. **Keep a notebook.** When something surprises you - good or bad - write it down. The pace of change is faster than memory. The notebook is how you keep your taste calibrated.

------------------------------------------------------------------------

## A Closing Thought

A year ago I would have called most of this speculative. Now most of it is shipped, in production, and either on my machine or about to be. The thing I keep coming back to is that the change is not really about the models. It is about what happens when capable models are wrapped in good harnesses, given access to the tools you already use, and pointed at problems you care about.

The next two years will be more of the same, faster. The people who do well will be the ones who treat the tools like a craft - learning them carefully, picking the right one for the right job, building habits around review and judgement rather than typing speed.

The verb is "delegate" now. The skill is knowing what to delegate, to whom, and what to do with the result. Everything else follows from that.

## Related Reading

- [AI Agents That Actually Work: Patterns From Real Projects](/ai/ai-agents-that-actually-work/)
- [Agent-First Architecture: The Engineer as System Curator](/ai/agent-first-architecture-engineer-as-curator/)
- [Hermes Agent: Persistent Autonomy That Learns and Grows](/ai/hermes-agent/)
- [The Next Decade of AI: What Actually Happens From Here](/ai/the-next-decade-of-ai/)
- [The Automation Paradox: Why More AI Makes Human Judgment More Valuable](/ai/automation-paradox/)
