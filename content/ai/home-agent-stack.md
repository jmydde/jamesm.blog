---
title: "Home Agent Stack: From Mac Mini to Secured MCP Tools"
date: 2026-05-15T08:00:00+01:00
draft: false
type: reference
tags: ["ai", "agent", "mcp", "mac-mini", "agentic-engineering"]
description: "A reading path for building a home AI agent on Apple Silicon - hardware sizing, cloud model routing, MCP servers, persistent memory, remote access, and security hardening in order."
cover:
  image: /assets/images/ai/mcp-servers-home-agent.jpg
  alt: Home agent stack reading path
slug: "home-agent-stack"
---

## TL;DR

- This path walks through the full stack I run on a Mac mini M6: **hardware and routing decision → MCP tools → memory → remote access → security**
- Almost no other blogs document the build *and* the hardening layer together
- Finish with [Securing AI Agents](/ai/securing-ai-agents/) before giving the agent real filesystem or mail access
- Part of the broader [Trust series](/ai/trust-series/)
- **Update:** this path originally started from a Mac Studio local-inference build. I've since moved to a smaller Mac mini M6 that routes most reasoning to DeepSeek and Claude instead - see the first entry below for why.

------------------------------------------------------------------------

## Read in order

1. [Own the Agent, Rent the Intelligence: Building My Always-On AI Agent Server](/ai/mac-mini-m6-always-on-ai-agent-server/) - the hardware and cloud-routing decision
2. [Giving Your Home AI Agent Real Tools: MCP Servers on a Mac mini M6](/ai/mcp-servers-home-ai-agent/) - wiring the tool layer
3. [Giving Your Home AI Agent Memory That Lasts](/ai/home-ai-agent-memory-that-lasts/) - persistence across sessions
4. [How to Phone Your Home AI Agent](/ai/phone-your-home-ai-agent/) - remote access when you are away
5. [Securing AI Agents](/ai/securing-ai-agents/) - least privilege, confirmation gates, audit logs

------------------------------------------------------------------------

## Adjacent guides

- [Running AI Models Locally with Ollama](/ai/ollama/) - lighter-weight local inference option
- [Agent Protocols in 2026: MCP, A2A, and ACP](/ai/agent-protocols-mcp-a2a-acp/) - the protocol layer
- [Local AI vs Cloud AI](/ai/local-vs-cloud-ai-2026/) - when to host vs call APIs
- [DGX Spark vs Mac Studio](/ai/dgx-spark-vs-mac-studio/) - if you are sizing a dedicated inference box

------------------------------------------------------------------------

## Related Reading

- [AI Economics and Hardware: A Reading Path](/ai/ai-economics-hardware/) - token costs, GPU sizing, and energy constraints behind every hardware decision
- [AI Dev Tooling: A Reading Path for 2026](/ai/ai-dev-tooling/) - the coding and development layer that sits above the agent infrastructure
- [Open WebUI: A Self-Hosted LLM Interface](/ai/open-webui-self-hosted-llm-interface/) - web interface layer to pair with local inference
- [Agent Protocols in 2026: MCP, A2A, and ACP](/ai/agent-protocols-mcp-a2a-acp/) - the protocol layer connecting agents to tools
