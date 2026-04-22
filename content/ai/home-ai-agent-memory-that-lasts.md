---
title: "Giving Your Home AI Agent Memory That Lasts"
date: 2026-04-22T19:30:00+01:00
draft: false
tags: ["ai", "memory", "mac-studio", "agent", "local-llm", "rag", "claude"]
description: "An agent with tools but no memory forgets you every morning. A walkthrough of how I bolted durable, structured memory onto my home AI agent running on a Mac Studio - what I store, where it lives, how retrieval works, and the mistakes I stopped making after the third rewrite."
cover:
  image: /assets/images/ai/home-ai-agent-memory.jpg
  alt: Home AI Agent Memory That Lasts Banner
---

## TL;DR

- **Problem:** a home agent with tools but no memory is a very well-read goldfish. Every morning it re-meets you.
- **Answer:** split memory into three layers - working, episodic, and semantic - and give each layer its own store and its own rules for what gets written.
- **Where it lives:** SQLite for episodic and facts, a local vector store for semantic search, and a tiny policy file that decides what is worth remembering in the first place.
- **How it plugs in:** a [memory MCP server](/ai/mcp-servers-home-ai-agent/) that exposes `recall`, `remember`, and `forget` - nothing else.
- **Result:** the agent can say "last Tuesday we tried restarting the Postgres container and it worked" and mean it. It also knows what *not* to store.

## The Goldfish Problem

The [home agent](/ai/phone-your-home-ai-agent/) I built over the last few weeks can do real things now. It can read my mail, move files around my workspace, turn lights off, and check my calendar. What it could not do, until this week, was remember any of it.

Every conversation started cold. "Remind me what we decided about the deploy script" got back "I do not have context for that". Every time I phoned the agent I had to re-explain who I was talking about, which project I meant, which Postgres container. The tool calls worked. The continuity did not.

This is the bit that quietly makes or breaks a home agent. Tools are the product. Memory is what stops the product being exhausting to use.

## Three Layers, Not One

The first thing I got wrong was treating memory as one big bucket. I pointed the agent at a vector store, dumped every message into it, and called it done. Within a week the store was 40,000 chunks of "ok" and "thanks" and the retrieval was useless - every search hit a pile of conversational filler before the actual fact.

The model that works for me now splits memory into three clearly different things:

1. **Working memory** - the current conversation. Lives in the context window. Dies when the session ends. This is what the model already does.
2. **Episodic memory** - "what happened". Timestamped events, tool calls, decisions. Lives in SQLite. Queried by time and topic.
3. **Semantic memory** - "what is true". Facts, preferences, relationships, project conventions. Lives in a small vector store plus a structured table. Queried by similarity and by key.

Those three have completely different write rules and completely different retrieval patterns. Collapsing them is why the single-bucket version rotted so fast.

## What Actually Gets Stored

The second thing I got wrong was letting the agent decide what was worth remembering. It is not good at that yet. Left alone it remembers the most recent thing, not the most important thing, and it remembers things in the model's own phrasing rather than mine.

I now have a tiny policy file that says what each layer is allowed to capture. It is not clever, and that is the point.

```yaml
episodic:
  capture:
    - tool_calls: all
    - decisions: when the user says "let's", "we decided", "going with"
    - incidents: when a tool returns an error the user reacts to
  retention: 180 days

semantic:
  capture:
    - preferences: when the user says "I prefer", "always", "never"
    - facts: when the user states something about a person, project, or thing
    - corrections: when the user corrects the agent's previous statement
  retention: until contradicted

forbidden:
  - ephemeral_state: "I am tired", "let's pick this up tomorrow"
  - ui_noise: "ok", "thanks", "nice"
  - model_self_narration: "I will now search for..."
```

The rules are enforced in the memory server, not in the prompt. Prompts drift. A 60-line Python function does not.

## Where It All Lives

Everything runs on the same [Mac Studio](/ai/mac-studio-local-llm-guide/) as the rest of the agent. No cloud, no third-party vector DB, no managed service.

```
~/agent-memory/
├── episodic.sqlite       (events, tool calls, decisions, with FTS5)
├── semantic.sqlite       (structured facts: key, value, source, updated_at)
├── vectors/              (local vector store for semantic search)
│   └── index.bin
└── policy.yaml           (the capture rules above)
```

A few specific choices worth calling out:

- **SQLite with FTS5 for episodic.** Full-text search is more useful than embeddings for "did we ever talk about X". It is also trivial to grep at 11pm when something weird happens.
- **A local vector store, not Pinecone.** I use a single-file index that lives next to the SQLite databases. The whole thing is ~40 MB after two months of daily use. It backs up with `cp`.
- **Structured facts next to the vectors.** Vectors are good for "find me something like this". A plain `(key, value)` table is better for "what is the user's preferred deploy command". Both, not either.
- **Embeddings run locally.** A small embedding model on the same machine - no external API call on the write path. This matters because the agent writes memory more often than it reads it.

## The MCP Server, Deliberately Boring

The [memory MCP server](/ai/mcp-servers-home-ai-agent/) exposes three tools to the agent. That is all.

```
recall(query, layer?, since?, limit?)   -> list of hits
remember(content, layer, tags?)         -> id
forget(id | query)                      -> count
```

`recall` is the workhorse. It searches the right store based on the `layer` hint, or all three if unhinted. Episodic hits come back with timestamps. Semantic hits come back with the source message so the agent can cite itself. Every call is logged to the same SQLite audit trail as every other tool.

`remember` is called by the server itself far more often than by the agent. The policy engine watches the conversation and writes memories proactively. The agent can also call `remember` directly when the user explicitly asks ("remember that Alex is on the infra team"), but that path is the minority.

`forget` is the one the agent is not allowed to call on its own initiative. If the user says "forget that", the server confirms what it is about to delete and waits for a yes. I learned this one the hard way after the agent helpfully "cleaned up" three weeks of project notes it decided were no longer relevant.

## Retrieval: The Bit That Decides Whether It Feels Alive

Writing memory is easy. Retrieval is the part that decides whether the agent feels like it knows you or like it is guessing.

The pattern that works:

1. **Pre-retrieve on session start.** When a session begins, the server runs a cheap query for "recent decisions, last 7 days" and "pinned facts" and injects a short summary into the system prompt. This is the equivalent of the agent flicking through yesterday's notes before the meeting starts.
2. **On-demand recall during the session.** When the agent is about to answer something that smells like it needs history, it calls `recall` with a specific query. The key word is *specific* - "Postgres container restart" not "database stuff".
3. **Cite back to the user.** If the agent uses a memory, it says so: "last Tuesday we restarted it and it came back in about 40 seconds". The user can correct it. Corrections feed back into semantic memory as higher-weighted facts.

The third one is where trust is built or lost. A memory system that silently shapes answers is unsettling. A memory system that says "I remember this from last Tuesday, is that still right?" feels like an assistant.

## What I Got Wrong First

In rough order:

- **One bucket for everything.** Already covered. The three-layer split was the single biggest improvement.
- **Embedding every message.** Most messages are not worth embedding. Filtering by the policy rules before embedding cut the vector store from 40,000 entries to about 1,200, and retrieval quality went up, not down.
- **Letting the agent pick what to remember.** It reliably picked the wrong things. Moving the decision into the server, with explicit rules, fixed it.
- **Summarising at write time.** I used to summarise long conversations into a single "gist" and store that. You lose the texture. Now I store the raw events in episodic and let the retrieval step summarise if it needs to.
- **No expiry.** The first version never forgot anything. Six months in, the agent was confidently quoting a project convention that had been reversed in January. Retention windows fix this - facts live until contradicted, episodes live 180 days, incidents live forever.
- **No user-visible view.** For a month I had no way to see what the agent "knew" about me. I now have a small local web page that lists the contents of the semantic store, grouped by topic. Being able to read your own agent's memory is non-negotiable.

## Contradictions, Which Are the Hard Part

Facts change. "I use Postgres 15" becomes "I use Postgres 16". A good memory system has to detect and resolve contradictions, not just accumulate.

My current approach is pragmatic rather than clever:

- Every semantic fact has a key, a value, a source message, and an `updated_at`.
- When the server sees a new fact with the same key, it checks whether the values agree. If not, it writes the new value and keeps the old one with a `superseded_at` timestamp.
- The retrieval layer only returns non-superseded facts unless the agent explicitly asks for history.
- The user can ask "what did I used to use" and get the superseded chain back.

This is not a full truth-maintenance system. It does not need to be. Most contradictions in a personal assistant are "I changed my mind" or "this project moved on", and a timestamped supersede chain handles both.

## Privacy, Because Someone Will Ask

Everything is local. The stores sit in an encrypted APFS volume. The MCP server only listens on `localhost` and is reachable over [Tailscale](https://tailscale.com/) from my phone for the [call-in agent](/ai/phone-your-home-ai-agent/). Nothing touches a third-party service on the write or read path.

The one exception is the fallback to the Claude API when a local model is not strong enough for a task. In that case, the memory retrieval still happens locally - the agent pulls the relevant snippets, then sends only those snippets to the API along with the current turn. The full store never leaves the box. This is the minimum bar I was willing to accept.

## Where This Goes Next

Two things on the list.

First, **per-project scoping.** Right now memory is global to me. It should be scoped so that "our deploy convention" resolves differently depending on which repo I am working in. This is the bridge to my [personal AI dev stack](/ai/personal-ai-dev-stack/) post - project-level context that the agent picks up from cwd without being told.

Second, **a memory-of-memory layer.** The agent should notice when it has been asked the same thing three times and promote that into a pinned fact. Right now I do the promotion manually. Automating it carefully is a small research project in its own right.

If you are building a home agent and you have the tools layer working, memory is the next unlock. It is not a vector database. It is three stores, a policy, and a habit of citing what you recall. Get those right and the agent stops being a clever stranger every morning.

## Further Reading

- [Model Context Protocol specification](https://modelcontextprotocol.io/specification)
- [SQLite FTS5 documentation](https://www.sqlite.org/fts5.html)
- [Anthropic on agent memory patterns](https://www.anthropic.com/research)
- [Tailscale for private service mesh](https://tailscale.com/kb/)
- [My earlier post on MCP servers for a home agent](/ai/mcp-servers-home-ai-agent/)
