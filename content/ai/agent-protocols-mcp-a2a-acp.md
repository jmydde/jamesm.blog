---
title: "The Quiet Standardisation of Agent Protocols - MCP, A2A, ACP Compared"
date: 2026-05-03T12:00:00+01:00
draft: false
tags: ['ai', 'agent', 'mcp', 'protocol', 'tools', 'interoperability', '2026']
description: "While the headlines were about model launches, the agent ecosystem quietly converged on three protocols that matter - MCP, A2A, and ACP. A grounded comparison of what each one actually does, where they overlap, and which to bet on if you are building agents in 2026."
cover:
  image: /assets/images/ai/agent-protocols-mcp-a2a-acp.jpg
  alt: Agent Protocols MCP A2A ACP Banner
---

## TL;DR

- The 2026 agent ecosystem has, while nobody was paying close attention, converged on three protocols that solve different problems and partly overlap: **MCP** (Model Context Protocol), **A2A** (Agent-to-Agent), and **ACP** (Agent Communication Protocol).
- **MCP** is the model-to-tool protocol. It standardises how an agent talks to its tools, data sources, and local context. This is the one that has clearly won its layer.
- **A2A** is the agent-to-agent protocol. It standardises how separately deployed agents discover each other, exchange tasks, and pass results. Adoption is growing but the picture is less settled.
- **ACP** is the orchestration-and-runtime protocol. It standardises how an agent runtime exposes its lifecycle, state, and operations to the systems around it. Newer, more enterprise-focused, and not yet a clear winner.
- The mental model: **MCP for tools, A2A for peers, ACP for the platform.** Build with all three in mind even if you only need one today.

## Why Protocols, Why Now

A year ago "agents" was still a debate about whether the things existed. By mid-2026 the debate has shifted. Agents exist. They do useful work. The interesting question is no longer "will this work" but "how do we connect them to everything else."

That second question is exactly the kind of question that gets answered with protocols. When the same problem - how does my agent reach my tools, your tools, our data, their data - keeps showing up across vendors, somebody writes a spec. Then somebody else writes an implementation. Then a few of those implementations get widely adopted and the rest fall away.

That is the phase the agent ecosystem is in right now. It looks chaotic if you are reading announcements. It looks orderly if you are reading the protocol specs.

Three of those specs matter.

## MCP - Model Context Protocol

[MCP](https://modelcontextprotocol.io/) was introduced by Anthropic in late 2024 and rapidly adopted across the ecosystem. It solves one specific problem: how a language model talks to external tools, data sources, and local context.

### What it does

MCP defines a JSON-RPC based protocol where an agent (the *client*) connects to one or more *servers*, each of which exposes:

- **Tools** - functions the model can call.
- **Resources** - data the model can read.
- **Prompts** - reusable templates the model can invoke.

A single agent can talk to many MCP servers simultaneously. A single MCP server can be connected to many agents. The protocol does not care which language model you are running. It does not care whether the server is local or remote. It just standardises the wire format.

### Why it won

MCP succeeded for three reasons.

**Right scope.** It solved one problem cleanly rather than trying to solve everything. The protocol is small enough that you can read the spec in an afternoon and implement a server in a day.

**Right backers.** Anthropic shipped it with first-party support across Claude Desktop and Claude Code. Within months, third-party support arrived from OpenAI tooling, JetBrains, VS Code, and a long tail of editors and IDEs. Once your tools support MCP, you cannot afford not to.

**Right ecosystem moment.** Every serious AI tooling company in 2025 was building bespoke integrations against bespoke surfaces. MCP gave them a place to consolidate. The "build it once, work everywhere" pitch was exactly what tool authors needed.

### Where MCP fits

If your agent needs to read your filesystem, talk to your database, hit your internal API, control your local machine, or reach into a SaaS tool - that is MCP territory. As of 2026 there are thousands of MCP servers in the wild, ranging from official integrations for major SaaS platforms to one-off personal servers for home automation.

This is the protocol that already has the answer. Build for it.

## A2A - Agent-to-Agent

[A2A](https://a2a-protocol.org/) (sometimes written as A2A Protocol) was introduced by Google in 2025 and has gained traction in environments where multiple agents from multiple vendors have to cooperate.

### What it does

A2A defines how independent agents - potentially built by different teams, hosted on different platforms, running different models - **discover each other, advertise capabilities, exchange tasks, and report results**.

The protocol introduces a few core abstractions:

- **Agent cards** - structured descriptions of what an agent can do, published at well-known endpoints.
- **Tasks** - units of work that one agent sends to another with structured inputs.
- **Messages** - the conversation history between agents during a task.
- **Artifacts** - structured outputs produced as the task progresses.

The pitch: when your travel-booking agent needs to talk to your hotel-booking agent and they were built by different companies, A2A is the lingua franca.

### Where A2A is in 2026

A2A's adoption story is more uneven than MCP's. Google has been the loudest backer. A handful of enterprise platforms support it. The independent developer community has been less enthusiastic, partly because most agents in the wild today are still single-agent rather than multi-agent.

The honest read: A2A solves a problem that exists, but it solves a problem most teams do not yet have. If you are building one agent today, A2A is theoretical. If you are building an enterprise platform that has to interoperate with other companies' agents, A2A is increasingly the expected answer.

### Where A2A fits

Multi-agent workflows across organisational or vendor boundaries. Agent marketplaces. Composed agent systems where each piece is built and operated separately. If your architecture diagram has multiple boxes labelled "agent" with arrows between them and those arrows cross trust boundaries, that is A2A territory.

## ACP - Agent Communication Protocol

[ACP](https://agentcommunicationprotocol.dev/) was introduced by IBM and the Linux Foundation in 2025 and lives in a different layer from the other two. Where MCP is model-to-tool and A2A is agent-to-agent, ACP is closer to **agent-to-runtime** or **agent-to-platform**.

### What it does

ACP standardises how an agent runtime exposes itself to the systems around it. That includes:

- **Lifecycle operations** - start, stop, suspend, resume.
- **State exposure** - what the agent is doing, what tools it has called, what context it is operating with.
- **Observability hooks** - structured events that monitoring and audit systems can consume.
- **Streaming I/O** - bidirectional message and event streaming with backpressure semantics.

ACP is more of an enterprise concern. The problem it solves is "I need to deploy this agent into a regulated, observed, governed environment and the platform needs a standard way to talk to it."

### Where ACP is in 2026

ACP is the youngest of the three. Adoption is concentrated in enterprise platforms and is still building. The Linux Foundation home gives it credibility but credibility alone does not move adoption. What is going to determine ACP's trajectory over the next 12-18 months is whether the major commercial agent platforms standardise on it or roll their own equivalents.

I would call ACP **the most important protocol you can still afford to wait on**, with the caveat that if you are building enterprise agent infrastructure, you cannot wait on it.

### Where ACP fits

Enterprise agent platforms. Regulated environments where audit, observability, and lifecycle management are not optional. Internal developer platforms that need to host third-party agents the way Kubernetes hosts third-party workloads.

## How They Compose

The three protocols are not competitors. They live at different layers and the cleanest mental model treats them as a stack.

```
┌──────────────────────────────────────────────┐
│   ACP - agent runtime ⟷ platform/observers   │
├──────────────────────────────────────────────┤
│   A2A - agent ⟷ peer agents                  │
├──────────────────────────────────────────────┤
│   MCP - model ⟷ tools/data/context           │
└──────────────────────────────────────────────┘
```

A complete agent system in 2026 might:

- Use **MCP** to reach its tools and data sources.
- Use **A2A** to delegate sub-tasks to other agents inside or outside the organisation.
- Be deployed inside an **ACP**-aware runtime that exposes its lifecycle and state to the surrounding platform.

You can use any one of these without the others. Most production agent systems today use MCP and nothing else, and that is fine. The point of the stack is that as your needs grow upward, the protocol you reach for is already standardised.

## What To Bet On In 2026

If you are starting an agent project today and have to make protocol decisions:

**Adopt MCP unconditionally.** Build all your tool and context integrations against MCP. The ecosystem of servers is already vast. The cost of using MCP is low, the cost of not using it is rebuilding integrations later.

**Design your agent so that A2A is plausible later.** You probably do not need to implement A2A today. But the moment your agent is going to talk to another agent across a trust boundary, you will want to. Keep your task definitions structured and your interfaces clean enough that adding A2A is an afternoon, not a rewrite.

**Ignore ACP unless you are an enterprise platform builder.** For application teams, ACP is overhead. For platform teams hosting third-party or multi-tenant agents, it is rapidly becoming table stakes.

## What This Means For The Agent Hype Cycle

Standardisation is one of the cleanest signals that a category has matured. When you can read three protocols in a weekend and have a working mental model of how the agent ecosystem fits together, the technology is no longer in its experimental phase.

That does not mean every agent in 2026 works well. Most still do not. But the substrate is now coherent. Tool integrations are not a per-vendor problem. Cross-vendor agent communication is not a per-deal problem. Enterprise deployment is not a per-platform problem.

The boring infrastructure has shown up. That is exactly what was missing in 2024 and 2025 and exactly what was needed for agents to move from demos to production. The exciting part of the story has stopped being the model launches and started being the protocols nobody is writing headlines about.

Pay attention to the boring parts. They are where the next year of agent value actually lives.

## Related Reading

- [AI Agents That Actually Work](/ai/ai-agents-that-actually-work/)
- [Agent-First Architecture - Engineer as Curator](/ai/agent-first-architecture-engineer-as-curator/)
- [MCP Servers for Home AI Agent](/ai/mcp-servers-home-ai-agent/)
- [Year of Agents and What's Next](/ai/year-of-agents-and-whats-next/)
- [AI Skills - One Folder, Any Model](/ai/ai-skills-one-folder-any-model/)
