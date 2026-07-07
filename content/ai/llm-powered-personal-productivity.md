---
title: "LLM-Powered Personal Productivity: Building a Private Automation Stack"
date: 2026-05-03T08:00:00+01:00
draft: false
tags: ["ai", "local-llm", "ollama", "obsidian", "automation", "memory", "privacy", "productivity"]
description: "Local LLMs have quietly become good enough to run a real personal automation stack - inbox triage, second-brain notes, home routines, voice capture - without sending anything to the cloud. A walkthrough of what I run, why each piece is there, and where the seams are."
cover:
  image: /assets/images/ai/llm-powered-personal-productivity.jpg
  alt: LLM-Powered Personal Productivity Banner
---

## TL;DR

- The interesting question in 2026 is not "can a local model do this", it is "which jobs should you give it".
- My stack: [Ollama](https://ollama.ai/) for inference, [Letta](https://www.letta.com/) for persistent agent memory, [Obsidian](https://obsidian.md/) as the second brain, [Home Assistant](https://www.home-assistant.io/) for the physical world, and a small router that decides where each thought goes.
- Three jobs are the sweet spot for local: inbox triage, note enrichment, and routine automation. Each one is repetitive, private, and tolerant of a bit of latency.
- Two jobs are still worth handing to a frontier cloud model: anything novel-and-hard, and anything where you want the best draft on the first attempt.
- The bit nobody talks about is the **router**. The model is not the product. The thing that decides which model gets which job is the product.

## Why Local Got Interesting

For years the answer to "should I run an LLM locally" was "no, just use the API". The API was cheaper, faster, smarter, and you did not have to think about VRAM. The only reason to go local was privacy, and most people did not actually care about privacy enough to give up the quality gap.

Two things changed that.

First, the open-weight models caught up to where the cloud models were 18 months ago. An 8B model on a laptop can now do the kinds of triage, summarisation, and tagging tasks that used to need a frontier model. It is not as good at novel reasoning, but most personal-productivity work is not novel reasoning. It is repetitive shape-matching.

Second, hardware got embarrassingly capable. Apple Silicon's [unified memory](/ai/mac-studio-local-llm-guide/) means a Mac Mini can hold a 30B model in RAM with room to spare for the rest of your laptop's life. A second-hand RTX 3090 is now the cheapest way to run a useful local agent, and it sits quietly in a closet.

The combination means you can put a model in front of every email, every note, and every sensor in your house, and the marginal cost of a query is the electricity. That changes what you build.

## The Stack

Here is what is actually running on the machine in my study.

```
                   ┌──────────────┐
   voice / text ──▶│   router     │── classify intent
                   │  (small LLM) │
                   └──────┬───────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   ┌─────────┐     ┌─────────────┐    ┌──────────────┐
   │ inbox   │     │  Obsidian   │    │   Home       │
   │ triage  │     │  enrichment │    │   Assistant  │
   └────┬────┘     └──────┬──────┘    └──────┬───────┘
        │                 │                  │
        └─────────────────┼──────────────────┘
                          ▼
                   ┌──────────────┐
                   │    Letta     │  long-term memory
                   │  (persistent)│  shared across jobs
                   └──────────────┘
```

Each box is small on its own. The glue is the router and the shared memory. Without those you end up with three separate agents that all forget you in slightly different ways.

## Inbox Triage

The first job I gave the local stack was email. Not draft replies - **triage**. Drafting is the part where you actually want to be involved. Triage is the part where you waste 20 minutes a day deciding what is worth opening.

The flow is small:

1. A cron job pulls new messages every five minutes via IMAP.
2. Each message goes to a local 8B model with a fixed prompt: "classify into {urgent, reply-needed, FYI, newsletter, automated, junk}, and extract any dates or asks".
3. The result becomes labels and a one-line summary in a sidebar I read once a day.

The interesting part is what I did **not** do. I did not let the model write replies, even drafts. Drafts feel helpful but they anchor you to the model's framing, and once you read the draft you cannot un-read it. Triage gives you the same time saving without the framing cost.

The other interesting part is the failure mode. About one in fifty messages gets miscategorised, and the same kinds get miscategorised every time - short personal messages from people the model has never seen before look like newsletters. The fix was not a smarter model. It was adding a "people I know" file to the prompt. A 40-line text file fixed more than three months of model upgrades would have.

## Obsidian as the Second Brain

[Obsidian](https://obsidian.md/) is a markdown file in a folder, with a UI on top. That is the whole pitch and it is why a local LLM fits it well - the model can just read the folder.

What I run on top of the vault:

- **Daily summary.** At 9pm a job reads the day's new notes and produces a one-paragraph "what changed today". This goes into a `daily/` folder. It is the only AI-generated content in the vault.
- **Backlink suggestions.** When I save a note, a job reads it, finds the five most similar existing notes by embedding, and adds a suggested-links block at the bottom. I accept or ignore. The model never edits the body of a note.
- **Tag normalisation.** Once a week, a job looks for tags I used inconsistently (`#ml`, `#machine-learning`, `#machinelearning`) and proposes merges. I review and apply.

The rule I keep coming back to: **the model proposes, I dispose**. The vault is mine. The AI's job is to reduce the cost of finding things, not to author the things.

## Home Assistant: The Physical Loop

[Home Assistant](https://www.home-assistant.io/) is the boring but productive bit. Local sensors, local triggers, local actions. The LLM gets pulled in for two narrow jobs:

- **Anomaly explanation.** When a routine fails ("hallway light did not turn off at midnight") the agent reads the recent state history and writes a one-line plain-English explanation. It does not fix anything. It just shortens the time between "something is off" and "I know what is off".
- **Natural-language automations.** I describe a routine in English ("if the back door is open after 10pm and nobody is home, ping me"), the model generates the YAML, I review and commit. The commit is the contract, not the prompt.

The rule, again: the model writes the proposal, the file is the source of truth. I do not let the model push to Home Assistant directly. Once you let an LLM hold the steering wheel of your house, you are debugging at 3am in a cold kitchen.

## Persistent Memory with Letta

The thing that makes the stack feel like one assistant rather than three scripts is the shared memory layer. I use [Letta](https://www.letta.com/) for this. Letta gives an agent a structured memory store - facts, preferences, relationships - that persists across sessions and processes.

What gets stored:

- **People.** Names, who they relate to, recent context. So "draft a note for Sarah's birthday" pulls in the right Sarah.
- **Preferences.** "I prefer evening reminders" gets written once and respected by the inbox job, the Obsidian summary, and the home routines.
- **Project state.** What I am currently working on, so a "summarise today" actually knows what *today* was about.

What does not get stored:

- Conversational filler.
- Anything the agent inferred without me confirming.
- Anything from the inbox or vault that the model just happened to read - those have their own stores.

I covered the structure of this in more depth in [Giving Your Home AI Agent Memory That Lasts](/ai/home-ai-agent-memory-that-lasts/). The Letta layer is the "semantic" tier in that model.

## The Capture Layer

The last piece is the bit nobody writes about because it sounds trivial. **How do you get a thought into the system?**

If capturing a thought takes more than three seconds you will not bother, and the whole stack is academic. The thing that worked for me:

- A back-tap shortcut on the phone opens a single voice prompt.
- Whisper transcribes locally.
- A tiny router model classifies the intent into one of about eight buckets (note, task, calendar, shopping, message, reminder, journal, ask).
- The transcript and intent get pushed to the right destination - vault note, task list, calendar, etc.
- One confirmation toast. No app to open.

The whole loop is under two seconds end-to-end. That is the difference between "I will use this" and "this is a project I will revisit at the weekend". It is also the answer to why local matters here - even a few hundred milliseconds of network latency at this layer makes the whole thing feel sluggish.

## What I Would Not Do Locally

To balance the picture, here is what I still send to a frontier model in the cloud:

- **Long-form drafting.** Anything I am going to publish. The quality gap on first-draft prose is still real.
- **Hard reasoning.** Debugging code I do not understand, working through a tricky decision, anything where the answer is not pattern-matched from existing examples.
- **Multi-step research.** When the agent needs to plan, browse, and compose, the frontier models are still meaningfully better at the planning bit.

The split is not "local for cheap stuff, cloud for important stuff". It is "local for shape-matching, cloud for novelty". Most personal productivity is shape-matching. That is why the local stack pays off. There is more on this split in [Local AI vs Cloud AI: The Tradeoff Landscape in 2026](/ai/local-vs-cloud-ai-2026/).

## Costs and Constraints

A few things I wish I had known before starting.

- **VRAM is the budget, not the model size.** Plan around how much memory you have, then pick the largest quantised model that fits with headroom for context. Running a 13B model at 90% memory pressure is worse than running an 8B model with room to breathe.
- **Latency budgets matter more than benchmark scores.** A model that scores two points lower on MMLU but responds in 400ms instead of 1.5s will be used ten times as often.
- **Persistent memory is the moat.** Three months in, the value of the stack is not the prompts or the models. It is the accumulated knowledge of *me* that the agent has. Back it up.
- **One router beats five clever agents.** I tried building specialised agents for each job. The thing that worked was a small classifier that decided which prompt to run, with one shared memory. Less code, fewer failure modes, easier to reason about.

## Closing

The story of local AI in 2026 is not "frontier models are obsolete". It is that there is now a clean split between **the things you want a giant cloud model for** (novelty, top-quality drafts, hard reasoning) and **the things you want a small, fast, private model for** (everything else in your daily life). Building the second half yourself, on hardware you own, with files you control, is the part that quietly changes how you work.

The fun bit is not the model. It never was. It is the seams between the model and the rest of your life - the inbox, the notes, the lights, the voice memo at the bus stop. Local LLMs let you stitch those seams without renting them from someone else.

## Related Reading

- [Running AI Models Locally with Ollama: From Setup to OpenClaw](/ai/ollama/)
- [Local AI vs Cloud AI: The Tradeoff Landscape in 2026](/ai/local-vs-cloud-ai-2026/)
- [Giving Your Home AI Agent Memory That Lasts](/ai/home-ai-agent-memory-that-lasts/)
- [Mac Studio Local LLM Guide](/ai/mac-studio-local-llm-guide/)
- [The Automation Paradox](/ai/automation-paradox/)
