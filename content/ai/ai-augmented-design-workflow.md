---
title: "My AI-Augmented Design Workflow: A 10-Minute Loop From Discussion to Documented Decision"
date: 2026-04-29T08:30:00+01:00
draft: false
tags: ['ai', 'workflow', 'cursor', 'claude-code', 'codex', 'documentation', 'spec-driven', 'design']
description: "How a combination of Cursor in the IDE, Claude Code and Codex in the terminal, and ChatGPT for general questions, collapsed my discuss-design-document loop to under ten minutes - backed by transcribed meetings checked into GitHub and a daily cross-check between code and design."
cover:
  image: assets/images/ai/ai-augmented-design-workflow.jpg
  alt: AI-Augmented Design Workflow Banner
---

Since making a combination of [Cursor](https://www.cursor.com/) in the IDE and [Claude Code](https://github.com/anthropics/claude-code) and [Codex](https://github.com/openai/codex) in the terminal the centre of my working day - with [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT) for general questions and [GitHub Spec Kit](https://github.com/github/spec-kit) holding the design contract - the way I move from a question on Slack to a documented design decision has changed beyond recognition.

What used to be a multi-day shuffle of meetings, follow-ups, written summaries, and "I will circle back on that" is now a tight loop that closes in five to ten minutes. The result is not just faster - it feels qualitatively different. There is no context switching, no postponed thinking, no half-finished docs. The decision is made, captured, validated against the rest of the design, and rendered into diagrams before the next meeting starts.

This post is partly a writeup of what that workflow looks like in practice, and partly a set of notes on the things I am still trying to get right. AI is now suggesting improvements faster than I can implement them, which is a strange new bottleneck to reason about.

## The tools, and what each one is actually for

It is worth being precise about which tool does what, because I use a combination of them and the division of labour matters.

- **Cursor is my main IDE, with its own models.** It is where the code, the design corpus, the meeting transcripts, and the Mermaid diagrams all live, and it is where the cross-checking happens.
- **Sometimes I use Visual Studio Code (VSC) instead**, with extensions for [Claude Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code), [Codex](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt), [Cline](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev), and [Google Gemini](https://marketplace.visualstudio.com/items?itemName=Google.geminicodeassist) - same loop, different surface.
- **Claude Code is an agent in the terminal.** It is the tool I reach for when I want something planned, refactored, or audited across the repo from the command line.
- **Codex is another agent in the terminal.** I run it alongside Claude Code, picking whichever model feels right for the task in front of me.
- **ChatGPT is for general questions.** Anything outside the repo - a half-remembered concept, a quick explainer, a sanity check on a non-code topic - goes there. It is no longer in the inner loop.
- **GitHub Spec Kit holds the contract.** The spec is the artefact every other tool reconciles against.

## Picking the right model for the job

Within Claude Code I move between models depending on what the task actually needs. Anthropic offers a spread - [Haiku](https://www.anthropic.com/claude/haiku) for fast and cheap, [Sonnet](https://www.anthropic.com/claude/sonnet) for the balanced middle, and [Opus](https://www.anthropic.com/claude/opus) for slow, expensive, deep work - and it pays to be deliberate about which one I reach for.

- **Cheaper, faster models (Haiku, smaller Sonnet variants) for small jobs.** Basic refactoring on a single file, a one-line tweak, drafting a simple idea, or quickly prototyping something that may not go anywhere. There is no point spending Opus tokens on a throwaway sketch.
- **The most expensive models (Opus) for the heavy lifting.** Large refactors that span the repo, deep thinking and analysis, anything where the cost of a wrong answer is high. When I have decided on a firm path, I bring Opus in to check all of my work and ideas end to end.
- **A two-pass pattern in between.** I will often let a cheaper model produce a first draft - a refactor, a stub, an exploratory design - and then ask the more expensive model to verify, rewrite, or enhance it. The cheaper pass surfaces the shape of the answer; the expensive pass makes sure it is actually correct.

The mental model is the same one I apply to people: do not use senior time for things a junior can do well, but do not let a junior ship something load-bearing without a senior reading it.

## The loop

The core flow has six steps and lives between three surfaces: [Slack](https://slack.com), Cursor in the IDE, and an agent in the terminal (Claude Code or Codex, depending on the task).

1. **Discuss and ideate.** Everything starts on Slack. Someone raises a question, an issue, or a design challenge. The thread is the rawest possible artefact - opinions, half-formed ideas, links, gut reactions.
2. **AI brainstorming.** I pull the thread into Cursor or one of the terminal agents to unpack it, surface trade-offs, and shape it into a structured proposal. The model is not deciding anything; it is putting structure under the conversation that humans had.
3. **Collaborative refinement.** The structured proposal goes back into Slack. The team responds. I loop between human input and model iterations until the shape of the decision is stable.
4. **Automated documentation.** The agent extracts the final decision and emits a Markdown summary in the format the design corpus uses - title, context, decision, consequences, open questions.
5. **Seamless integration.** The summary lands directly in Cursor, in the right place in the design tree, with the right cross-links.
6. **AI validation and maintenance.** Cursor cross-checks the new decision against the rest of the design, flags conflicts with earlier choices, updates [Mermaid](https://mermaid.js.org/) diagrams, and revises sample data and data models so they stay coherent.

The whole loop, discussion to documented decision, takes five to ten minutes. The first time it closed inside a single coffee, I genuinely sat back and stared at the screen.

## The end-to-end picture

The six-step loop is the inner cycle, but it sits inside a broader pipeline that runs from the first Slack message all the way through to production support. Everything in the diagram below converges on a single GitHub repository - code, design, transcripts, specs, and tests all live together so the agents can reason across the lot.

```text
                  ┌─────────────────────┐     ┌──────────────────────┐
                  │  Slack discussions  │     │  Meetings            │
                  │  questions · issues │     │  auto-transcribed    │
                  └──────────┬──────────┘     └──────────┬───────────┘
                             │                           │
                             ▼                           │
   ┌─────────────────────────────────────────┐           │
   │  DESIGN                                 │           │
   │  ┌───────────────────────────────────┐  │           │
   │  │ Cursor + Claude Code + Codex      │  │           │
   │  │ structure the proposal            │  │           │
   │  └────────────────┬──────────────────┘  │           │
   │                   ▼                     │           │
   │  ┌───────────────────────────────────┐  │           │
   │  │ Slack feedback loop               │  │           │
   │  └────────────────┬──────────────────┘  │           │
   │                   ▼                     │           │
   │  ┌───────────────────────────────────┐  │           │
   │  │ Markdown decision                 │  │           │
   │  │ context · decision · consequences │  │           │
   │  └────────────────┬──────────────────┘  │           │
   │                   ▼                     │           │
   │  ┌───────────────────────────────────┐  │           │
   │  │ GitHub Spec Kit  (living contract)│  │           │
   │  └────────────────┬──────────────────┘  │           │
   └───────────────────┼─────────────────────┘           │
                       │                                 │
                       ▼                                 ▼
              ╔══════════════════════════════════════════════════╗
              ║              GitHub repository                   ║
              ║   code · design · transcripts · specs · tests    ║◀─── reads ───┐
              ╚════════════════════┬═════════════════════════════╝              │
                                   │                                            │
                                   ▼                                            │
   ┌─────────────────────────────────────────┐                                  │
   │  DEVELOPMENT                            │                                  │
   │  Agent plans the change vs the spec     │                                  │
   │            ▼                            │                                  │
   │  Cursor (IDE) + Claude Code + Codex     │                                  │
   │            ▼                            │                                  │
   │  Pull request, linked to the decision   │                                  │
   └────────────────┬────────────────────────┘                                  │
                    ▼                                                           │
   ┌─────────────────────────────────────────┐                                  │
   │  TESTING                                │                                  │
   │  Unit & integration tests               │                                  │
   │            ▼                            │                                  │
   │  Agent-callable regression suite        │                                  │
   │            ▼                            │                                  │
   │  AI-assisted code review                │                                  │
   └────────────────┬────────────────────────┘                                  │
                    ▼                                                           │
   ┌─────────────────────────────────────────┐                                  │
   │  DEPLOYMENT                             │                                  │
   │  CI pipeline  ──▶  Release to prod      │                                  │
   └────────────────┬────────────────────────┘                                  │
                    ▼                                                           │
   ┌─────────────────────────────────────────┐                                  │
   │  SUPPORT                                │                                  │
   │  Monitoring & alerts                    │                                  │
   │            ▼                            │                                  │
   │  Agent triage vs design + transcripts ──┼──── reads history ───────────────┘
   │            ▼                            │
   │  Issues feed back to Slack ─────────────┼──── (loop closes) ──▶ back to top
   └─────────────────────────────────────────┘

                ┌──────────────────────────────────────────────┐
                │  Nightly design CI  (idea, not live yet)     │
                │  would cross-check code ↔ design ↔ spec,     │
                │  and flag drift into Slack each morning      │
                └──────────────────────────────────────────────┘
```

A few things in this picture are worth pulling out. The GitHub repo is the gravitational centre - every other surface either feeds it or reads from it. Meeting transcripts land in it directly, so the agents that triage a production incident can read what was said in the design review nine months ago. The nightly design CI in the diagram is an idea, not something I have running yet - today the same job is done by hand, with me asking Cursor in the IDE chat to update the docs and code when something drifts. And the support loop closes back into Slack, so a real-world issue becomes a new Slack thread, which becomes a new design decision, which becomes a new spec, which becomes new code. The whole thing is one cycle, not a line.

## All the design work, centralised

Everything now lives in a single Cursor workspace, backed by GitHub - meeting notes, design discussions, data models, business rules, sample data, and Mermaid process and data flow diagrams. The [docs-as-code](https://www.writethedocs.org/guide/docs-as-code/) philosophy was right ten years ago and is more right now, because the tools that read the docs are also the tools that maintain them.

Crucially, **every meeting is transcribed and the transcript is checked into GitHub** alongside the design corpus. That means the agents have access to the full historical record - not just the curated decisions, but the conversations that led to them. When Claude Code is asked *why* a particular choice was made, it does not have to guess. It can read the room from six months ago. This single change has done more for the quality of AI-suggested designs than any prompt-engineering trick I have tried, because the model is no longer reasoning from a sanitised summary; it is reasoning from the actual debate.

On top of that, **everything is cross-checked regularly** - though for now that cross-checking is a manual habit, not an automated job. I lean on Cursor's IDE chat to walk the repo with me and ask one question over and over: does the code still match the design, and does the design still match itself? Drift gets flagged the day I look, not the quarter it appears. The plan is to hand this off to a scheduled agent so it happens overnight without me, but that is the next step, not the current state. Either way, it is the difference between documentation as an artefact and documentation as a system.

Cursor does not just store. It thinks. It restructures documents, surfaces related concepts, and finds connections I would not have noticed. During design reviews it has become a running joke - I will suggest adding something, and someone will reply, "No James, it is already there." And it is, perfectly phrased and in exactly the right place.

For the design-heavy phase I am in, this setup is saving weeks. It maintains a living, self-updating documentation set, flags inconsistencies, highlights conflicting decisions, and reminds us about unfinished actions. I also wrote a small script that merges every Markdown file in the corpus into a single concatenated `.md`, which I upload to a custom GPT for deeper synthesis when I want a second opinion on the entire design at once.

## AI-assisted meeting notes review

Even meeting notes go through a review pass. I have a model check every note for tone, professionalism, and objectivity before it is shared. The output is a simple two-list report - what the notes correctly include (technical summaries, task assignments, design and architecture decisions, professional references to teammates) and what they are clean of (biased language, personal remarks, controversial opinions).

The notes are stakeholder-ready by the time they leave my machine, with a neutral, business-like tone that reflects how I want my team's work to land in the rest of the organisation. This single pass has eliminated a class of after-the-fact edits that used to chew up an hour a week.

## The real breakthrough is cognitive flow

The transformation I did not predict is in mental flow. There is no context switching. The iteration loop is so fast that I can make complex design decisions in real time, while the problem is still fresh in my head.

Before, I would constantly postpone things - "I will come back to that later." Now those delays are mostly gone. It is not that AI made me cleverer. It removed the friction between thinking and recording, so the thinking does not get lost waiting for the recording to catch up. It feels like working in a state of continuous clarity, which is the part I would miss most if you took it away.

This connects to a point I have been trying to articulate in a [previous post on judgment and execution](/ai/automation-paradox/) - when execution becomes cheap, the only thing worth optimising for is the quality of the next decision. Cognitive flow is what lets you actually deliver on that.

## AI is racing ahead, and I am the bottleneck

For the first time, I genuinely feel how quickly AI is pulling ahead. It suggests best practices and design improvements that are correct - but I often cannot implement them immediately because I am still finishing previously committed work. The AI is moving faster than my human brain can deliver, and the queue of "we should also do this" is growing.

This has made me think seriously about automating the next stage. Three things are on the experiment list:

- **A code refactoring automation system** that takes a model's structured suggestion and applies it as a draft pull request, ready for human review.
- **A regression suite the AI can call autonomously**, so the model can verify its own refactor against behavioural expectations before asking for a human eye.
- **Overnight tasks** - letting agents refactor designs, regenerate diagrams, or verify logic while I sleep, so I wake up to a fresh, reconciled system and a morning report in Slack.

The constraint here is not capability. The constraint is verbosity. AI produces so much documentation that I now spend a non-trivial slice of the week compacting, deduplicating, and structuring it across multiple docs. The fix I am converging on is to invert the role - rather than asking the model to *generate* docs, I ask it to *compact* them, reducing each document to its load-bearing claims and pushing the detail into appendices the human reader can ignore. Generation is the easy half of the job. Compaction is the half that takes taste.

## Managing multiple design states

I am currently maintaining three parallel views of the design.

1. **Current** - the implemented, production-aligned version.
2. **Next or immediate future** - improvements currently in flight.
3. **Long-term or ideal end state** - the architecture vision we are pulling towards.

Each has its own lifecycle, dependencies, and assumptions. The interesting question is how to store them.

My initial instinct was feature branches. The more I sit with it, the more I think subfolders are the right answer - `current/`, `next/`, `north-star/` - with a small README in each that names the lifecycle and the dependencies. Branches obscure the parallel views, because you cannot see them side by side. Subfolders let the AI read all three at once and reason about the deltas. The reconciliation between them becomes a first-class workflow rather than a merge conflict.

The nightly "design CI" I mentioned earlier is the same idea applied to these three folders, and it is still an idea rather than a running pipeline. Today I do the equivalent by hand inside Cursor's IDE chat - asking it to walk all three folders, regenerate Mermaid diagrams, flag drift between the spec and the code, and reconcile deltas between the layers. The aspiration is to hand that off to a scheduled agent that posts a morning report into Slack while I sleep. This is the [spec-driven](/ai/spec-driven-development/) idea taken one step further: the spec is not just a target, it is a living artefact that an agent audits against meeting transcripts, code, and design docs that all live in the same repo.

## The result

This AI-augmented workflow has reshaped not just how the team works, but how I think about working. The headline outcomes are the obvious ones - instant iteration loops, automated documentation and visualisation, proactive surfacing of design insights, and AI-driven suggestions that go beyond human bandwidth. The deeper change is harder to summarise.

The role of the senior engineer is starting to look less like "the person who writes the design" and more like "the person who curates the design the AI maintains." The taste, the constraints, the willingness to say *no, not that* - those still belong to the humans. Everything downstream of those judgments is increasingly machine work.

It is efficient, creative, and constantly evolving. And even though it is already miles ahead of me, I am doing my best to keep up.

## Related Reading

- [Spec-Driven Development: When the Brief Becomes the Product](/ai/spec-driven-development/)
- [Claude Design: Closing the Design-to-Code Gap](/ai/claude-design/)
- [GitHub Spec Kit in 2026: SDD Goes Mainstream 🚀](/ai/github-spec-kit-2026-update/)
- [Cursor AI, Spec-Driven Magic, and Why My Entire Development Workflow Just Leveled Up 🤯](/ai/cursor-ai/)
- [Claude Code vs Cursor: A 6-Month Comparison](/ai/claude-code-vs-cursor/)
