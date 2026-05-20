---
title: "Context Engineering: The Discipline That Replaced Prompt Engineering"
date: 2026-05-20T20:32:00+01:00
draft: false
tags: ["ai", "context-engineering", "llm", "agent", "memory", "agentic-engineering"]
description: "Prompt engineering was about wording a single request well. Context engineering is about curating everything in the model's window - retrieval, memory, tool results, and compaction - across a whole agent run. Here is why the discipline shifted, and the practices that separate reliable production systems from ones that quietly rot."
cover:
  image: /assets/images/ai/context-engineering.png
  alt: Context Engineering - The Discipline That Replaced Prompt Engineering Banner
---

## TL;DR

- **Prompt engineering** optimised the wording of a single human-written request. **Context engineering** optimises the entire set of tokens in the model's window across a whole run - system prompt, tool definitions, retrieved documents, tool results, conversation history, and memory
- The shift happened because of agents. The window is no longer one prompt you wrote - it is an accumulation that grows on every step, and most of it is produced by the system, not by you
- More context is not better context. [Research on "context rot"](https://www.trychroma.com/research/context-rot) and the older [lost-in-the-middle effect](https://arxiv.org/abs/2307.03172) show model accuracy degrades as the window fills, even well below the advertised limit
- The four levers are **retrieval** (what you pull in), **memory** (what persists across runs), **tool results** (what tools dump back), and **compaction** (what you summarise and discard)
- Treat the window as a budget. Measure its token composition, design tools to return terse output, curate rather than accumulate, and keep the static prefix stable so [prompt caching](/ai/prompt-caching/) still works

For a few years, "prompt engineering" was the named skill of working with language models. It meant finding the wording, the framing, the few-shot examples, and the role instructions that coaxed the best answer out of a single request. It produced a small industry of prompt libraries, prompt marketplaces, and job titles. And in 2026 it is mostly gone, absorbed into something larger and harder.

The thing that replaced it is context engineering. The term was popularised through 2025, and [Anthropic's own engineering team now describes it](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) as "the set of strategies for curating and maintaining the optimal set of tokens during LLM inference." That is a deliberately broad definition, and the breadth is the point. Prompt engineering was about one message. Context engineering is about everything the model sees, on every step, for the whole length of a task.

## Why the discipline shifted

Prompt engineering made sense when the interaction was simple: a human writes a prompt, the model writes a response, done. In that world the prompt *was* the context. Optimising the prompt optimised everything.

Agents broke that model. In an agentic run, the model is called in a loop. Each turn it might call a tool, read the result, call another tool, retrieve a document, update its plan, and continue. By the tenth step, the window contains:

- The system prompt and behaviour instructions
- A list of tool definitions, often long and verbose
- Whatever the [retrieval layer](/ai/rag-in-2026-what-won-what-lost/) pulled in
- The full transcript of every tool call and every tool result so far
- The model's own intermediate reasoning and plans
- Any [persistent memory](/ai/home-ai-agent-memory-that-lasts/) loaded from previous sessions
- The user's original request, now buried somewhere near the top

Almost none of that was written by a human. It accumulated. The skill is no longer "write a good prompt" - it is "decide, on every step, what belongs in the window and what does not." That is an engineering problem, not a wording problem, and it does not have a clever-phrasing solution.

## The window is a budget, not a bucket

The most damaging mental model is treating the context window as free space - a bucket you fill until it overflows. The headline numbers encourage this. When a model advertises a 200k or 1M token window, it is tempting to read that as "I can put a million tokens of stuff in and the model will use all of it well."

It will not. Two pieces of evidence matter here.

The first is the [lost-in-the-middle effect](https://arxiv.org/abs/2307.03172), documented back in 2023: models retrieve information reliably when it sits at the start or end of the context, and much less reliably when it sits in the middle. Position inside the window changes whether the model can actually use a fact.

The second is more recent and more uncomfortable. Chroma's [context rot research](https://www.trychroma.com/research/context-rot) evaluated 18 models, including current frontier ones, and found that performance "varies significantly as input length changes, even on simple tasks." Accuracy degrades as the window fills - not at the limit, but well before it. The model does not fail loudly when you overfill it. It just gets quietly worse, and you only notice if you are measuring.

So the window is a budget. Every token you spend on a stale tool result, a document the model does not need, or a verbose tool schema is a token that crowds out something useful and nudges accuracy down. The whole discipline follows from taking that seriously. This is the same instinct behind the [token efficiency mindset](/ai/claude-token-efficiency-mindset/), applied to a system instead of a conversation, and it is why [a bigger context window](/ai/llm-context-window-arms-race/) is far less of a win than it appears.

## The four levers

Context engineering, in practice, is the management of four things. Get these right and the system stays coherent over long runs. Get them wrong and it rots.

### Retrieval: what you pull in

Retrieval decides which external information enters the window. The old reflex was to pull generously - grab the top 20 chunks, paste them all in, let the model sort it out. With a budget mindset, that is backwards. Every irrelevant chunk is a distractor, and Chroma's work shows distractors hurt even when the answer is also present.

The pattern that works is to retrieve less and retrieve later. Pull in a small number of high-precision results, and prefer **just-in-time retrieval** - let the agent fetch a document at the step it needs it, rather than front-loading everything it might conceivably want. A [reranking](/ai/rag-in-2026-what-won-what-lost/) step that trims ten candidates to the three that matter is worth more than a wider net. Precision beats recall when recall costs you accuracy elsewhere.

### Memory: what persists across runs

The window is wiped between runs. Memory is what survives. This is the layer that lets an agent remember your preferences, the decisions made yesterday, and the state of a long project - without dragging the entire history back into context every time.

The mistake is to treat memory as "append the whole transcript to a file and reload it." That just moves the bloat. Good memory is *structured and selective*: durable facts, not raw logs. A short profile, a list of decisions with rationale, the current state of the task - written deliberately, retrieved deliberately. I wrote about [building this for my own home agent](/ai/home-ai-agent-memory-that-lasts/), and the lesson that stuck was that memory is a curation problem too. What you choose not to remember matters as much as what you keep. Anthropic and others now ship dedicated memory tools for exactly this reason, and they are covered in more depth in [what actually works with Claude's memory in 2026](/ai/claude-long-context-and-memory-2026/).

### Tool results: what tools dump back

This is the lever most teams overlook, and it is often the biggest leak. Tools return data, and that data lands in the window verbatim. A database query returns 500 rows. An API call returns a 4,000-token JSON blob with 30 fields when the agent needed two. A file read returns the whole file. A web fetch returns the whole page, navigation and footer included.

By step eight, a large fraction of the window can be stale tool output the model already used and no longer needs. The fixes are unglamorous and effective:

- **Design tools to return what the agent needs, not everything they can.** A tool that returns a [structured, minimal payload](/ai/structured-outputs-schema/) is a context engineering decision disguised as an API design decision.
- **Summarise or truncate large results** before they enter the window, and keep a reference to the full result the agent can re-fetch if it must.
- **Drop stale tool results.** Once a result has been consumed and acted on, it can often be removed or collapsed to a one-line note. The model rarely needs the raw output of step two while doing step nine.

### Compaction: what you summarise and discard

Eventually a long run fills the window anyway. Compaction is the controlled response: when the context approaches its useful limit, summarise the history so far into a compact form, keep the parts that still matter, and discard the rest.

Done well, compaction is the difference between an agent that can run for hours and one that hits a wall. Done badly, it silently drops the one constraint that mattered. The discipline is to compact deliberately - decide what a summary must preserve (open goals, key decisions, unresolved errors, the user's actual request) and what it can shed (resolved sub-tasks, raw tool dumps, superseded plans) - rather than letting a generic "summarise the conversation" call throw away things at random.

## The failure modes have names

When context engineering goes wrong, it goes wrong in recognisable ways. Naming them helps you spot them in a transcript.

- **Context poisoning.** An error, a hallucination, or a wrong assumption enters the window early and is never removed. Every subsequent step treats it as fact. The agent is now confidently building on a bad foundation, and no single later prompt can fix it.
- **Context distraction.** The window is so full of history that the model starts paying more attention to its own past actions than to the current task. Long agent runs drift this way - the agent loops, repeats itself, or forgets the goal.
- **Context confusion.** Irrelevant content - extra tools, unused documents, stale results - is present, and the model uses it because it is there. The presence of an unused tool measurably changes behaviour.
- **Context clash.** Two parts of the window disagree. An early tool result says one thing, a later one contradicts it, and both are still present. The model has no reliable way to know which to trust.

Every one of these is a curation failure. The content that caused it should not have been in the window, or should have been removed once it stopped being useful. If you have ever watched an agent [behave non-deterministically and been unable to explain why](/ai/agent-reliability-debugging-non-deterministic/), a poisoned or cluttered context is one of the first things to check.

## The practices that hold up

A few habits separate teams whose agents stay coherent from teams whose agents quietly degrade.

**They measure the composition of the window.** Not just the total token count - the breakdown. How many tokens are system prompt, how many are tool definitions, how many are tool results, how many are retrieved documents, how many are conversation history. You cannot manage a budget you cannot see, and the breakdown almost always reveals one category quietly eating everything.

**They curate, they do not accumulate.** The default behaviour of an agent loop is to append. Good systems actively remove - dropping consumed tool results, compacting history, pruning retrieved content that did not pan out. Accumulation is the path of least resistance and the path to rot.

**They design tools as context-engineering surface.** Tool descriptions are part of the prompt. Tool outputs are part of the context. A tool that returns terse, structured, relevant data is doing context engineering on the team's behalf. A chatty tool undoes it.

**They keep the static prefix stable.** The system prompt, tool definitions, and other unchanging content should sit at the top of the window and not move, so that [prompt caching](/ai/prompt-caching/) keeps working. Context engineering and cost engineering point the same direction here: a clean, stable, well-ordered prefix is both cheaper and more reliable. The dynamic, fast-changing content belongs at the end.

**They write the system prompt at the right altitude.** Not so vague it gives the model nothing to act on, not so prescriptive it brittle-codes every edge case. The system prompt sets behaviour; the rest of the window supplies the facts. Keeping that separation clean stops the system prompt from bloating into a rulebook.

## What I would tell someone starting today

If you are building anything agentic, stop thinking about "the prompt" as the unit of work. The unit of work is the window, on every step, for the whole run. The prompt is one component of it, and not the one most likely to be your problem.

Start by instrumenting. Log the token composition of the context on each step of a real run and look at where the budget actually goes. The first time most people do this, they find that 60 to 70 percent of the window is stale tool output and documents the agent stopped needing several steps ago. That single measurement reframes the whole problem.

Then work the four levers. Tighten retrieval so it pulls less and later. Give the agent structured memory so it does not reload its whole history. Make tools return what is needed rather than everything available. Compact deliberately when the window fills. None of this is clever wording. It is systems design - deciding what information exists where, and when it enters and leaves the model's attention.

Prompt engineering was a real skill, and the parts of it that mattered - clarity, good examples, precise instructions - still matter. But they are now a small subsection of a larger discipline. The teams shipping reliable AI systems in 2026 are not the ones with the cleverest prompts. They are the ones who treat the context window as the scarce, decaying, carefully managed resource it actually is.

## Related Reading

- [Prompt Caching: The Quiet Performance Win for LLM Applications](/ai/prompt-caching/)
- [The Token Efficiency Mindset - Why Your Claude Conversations Cost More Than They Should](/ai/claude-token-efficiency-mindset/)
- [The LLM Context Window Arms Race: Does It Actually Matter?](/ai/llm-context-window-arms-race/)
- [Claude's Memory and Long Context in 2026: What Actually Works](/ai/claude-long-context-and-memory-2026/)
- [RAG in 2026: What Won, What Lost](/ai/rag-in-2026-what-won-what-lost/)
