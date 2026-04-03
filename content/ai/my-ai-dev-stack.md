---
title: "My AI Development Stack"
date: 2026-04-03T23:09:25+01:00
draft: false
tags: ['ai']
---
```
                        ┌──────────┐
                        │  iPhone  │
                        └──────────┘
                              │
                  Tailscale VPN (on-demand)
                              │
                              ▼
                        ┌─────────────┐
                        │ MacBook     │
                        │ (tmux /     │
                        │ zellij +    │
                        │ caffeinate) │
                        └─────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
  ┌────────────┐       ┌────────────┐    ┌───────────────┐
  │ VS Code    │       │ Terminus   │    │  Cursor AI    │
  │ + Cline    │       │ (SSH)      │    │ (Primary IDE) │
  │ + Continue │       └────────────┘    └───────────────┘
  └────────────┘                                 │
        │                                        ▼
        ▼                            ┌──────────────────────────────┐
┌────────────────────┐               │   AI Coding Agents & Tools   │
│ Test / Scripts     │               │------------------------------│
│ (AI-driven)        │               │ • Cline                      │
└────────────────────┘               │ • Continue.dev               │
                                     │ • Claude Code                │
                                     │ • Aider                      │
                                     │ • Windsurf (Cascade)         │
                                     │ • Gemini CLI                 │
                                     │ • GitHub Copilot             │
                                     └──────────────────────────────┘
                                                     │
                                                     ▼
                               ┌────────────────────────────────────┐
                               │ LLM Routing & Orchestration        │
                               │------------------------------------│
                               │ • OpenRouter / LiteLLM             │
                               │ • Multi-model routing              │
                               │ • Cost / speed optimisation        │
                               │ • IDE integrations                 │
                               └────────────────────────────────────┘
                                                     │
                                                     ▼
                     ┌────────────────────────────────────────────────────┐
                     │        Cloud / Web LLM Interfaces                  │
                     │----------------------------------------------------│
                     │ ChatGPT Web / Codex        → Research / general    │
                     │ Perplexity Web             → Cited research        │
                     │ Claude Code (terminal)     → Heavy coding          │
                     │ Claude Web + Desktop       → General usage         │
                     │ Grok / SuperGrok           → Images + real-time    │
                     └────────────────────────────────────────────────────┘
```
