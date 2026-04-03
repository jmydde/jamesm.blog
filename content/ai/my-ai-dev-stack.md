---
title: "Personal AI Development Stack"
date: 2026-04-03T23:09:25+01:00
draft: false
tags: ['ai']
---

This guide documents a highly productive, AI-driven development stack using a combination of cloud-based LLMs, terminal tools, IDEs, and mobile access. It is designed for developers who want persistent workflows, AI-powered coding assistance, and flexible access from multiple devices.

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
                        │ MacBook Air │
                        │ (tmux /     │
                        │ zellij +    │
                        │ caffeinate) │
                        └─────────────┘
                              │
        ┌─────────────────────┼──────────────────┐
        │                     │                  │
        ▼                     ▼                  ▼
  ┌────────────┐       ┌────────────┐    ┌───────────────┐
  │ VS Code    │       │ Terminus   │    │  Cursor AI    │
  │ + Cline    │       │ (SSH)      │    │ (Primary IDE) │
  │ + Continue │       └────────────┘    └───────────────┘
  └────────────┘                                 │
        │                                        ▼
        ▼                        ┌──────────────────────────────┐
┌────────────────┐               │   AI Coding Agents & Tools   │
│ Test / Scripts │               │------------------------------│
│ (AI-driven)    │               │ • Cline                      │
└────────────────┘               │ • Continue.dev               │
                                 │ • Claude Code                │
                                 │ • Ollama (local models)      │
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

---

## Component Descriptions

### iPhone
- **Purpose:** Mobile access to coding sessions, remote terminals, and LLM interfaces.
- **Tools:** Termius (SSH), web browsers for cloud LLMs.
- **Connection:** Via **Tailscale VPN** for secure, private access to your MacBook.

### Tailscale VPN
- **Purpose:** Secure, on-demand VPN that allows devices to communicate without exposing ports publicly.
- **Use case:** Connect iPhone or other devices to your MacBook seamlessly.

### MacBook
- **Purpose:** Primary development machine.
- **Enhancements:**
  - **tmux / zellij:** Terminal multiplexers for persistent, multi-pane sessions.
  - **caffeinate / Amphetamine:** Prevent sleep to maintain long-running processes or server tasks.

### IDEs and Terminals
- **VS Code + Cline + Continue.dev**
  - Modern IDE with AI-powered code suggestions and integrations.
- **Terminus**
  - SSH client for remote server access and workflow continuity.
- **Cursor AI**
  - AI-focused primary IDE for code generation and testing.

### AI Coding Agents & Tools
- **Purpose:** Automate coding, testing, and documentation.
- **Key Tools:**
  - **Cline:** Terminal-based AI coding assistant.
  - **Continue.dev:** AI automation for workflows.
  - **Claude Code:** Heavy-duty coding in CLI.
  - **Aider / Windsurf / Gemini CLI / GitHub Copilot:** Multi-purpose AI agents integrated with IDEs.

### LLM Routing & Orchestration
- **Purpose:** Optimize which AI model handles which task.
- **Features:**
  - Multi-model routing based on task type (research, coding, testing, image generation).
  - Speed and cost optimization for different models.
  - Seamless IDE integration for on-the-fly AI assistance.

### Cloud / Web LLM Interfaces
- **Purpose:** External interfaces for research, code generation, and real-time AI support.
- **Examples:**
  - **ChatGPT Web / Codex:** General-purpose research and code generation.
  - **Perplexity Web:** Citation-focused research.
  - **Claude Web + Desktop / Claude Code:** Heavy coding workflows.
  - **Grok / SuperGrok:** Image processing, real-time AI applications.

---

## Workflow Example

1. **Start your MacBook environment:**
   ```bash
   tmux new -s dev
   caffeinate -dims &
   ```
2. **Connect iPhone via Tailscale VPN**
   - Open Termius to SSH into the MacBook.
   - Access web LLM interfaces via browser.

3. **Code & Test:**
   - Open VS Code or Cursor AI.
   - Use AI agents for code suggestions (`Claude Code`, `Aider`).
   - Run tests and scripts locally or via AI automation.

4. **Route AI Tasks via LLM Orchestration:**
   - Route heavy coding to Claude Code CLI.
   - Use Perplexity Web for research and citations.
   - Use ChatGPT for general guidance.

5. **Deploy / Integrate:**
   - Final code merges via VS Code.
   - Push code to GitHub or deploy with scripts automated by Continue.dev.

---

## Tips & Best Practices
- Keep **tmux/zellij sessions persistent** to avoid losing long-running AI tasks.
- Use **Tailscale** for mobile-first remote access; no port forwarding required.
- Use **LLM orchestration** to reduce latency and cost by assigning tasks to the most efficient model.
- Combine terminal-based and web-based AI tools for optimal workflow flexibility.
- Regularly update your AI agents and IDE plugins for maximum compatibility.

---

This stack allows seamless integration of **mobile access, persistent development environments, AI coding assistants, and multi-model orchestration**, ideal for solo developers or small teams who heavily rely on AI-driven productivity.
