---
title: "Personal AI Development Stack"
date: 2026-04-03T23:09:25+01:00
draft: false
tags: ['ai']
description: "A practical, AI-driven development stack combining cloud and local LLMs, terminal tools, IDEs, and mobile access for persistent, productive workflows."
---

This guide documents a highly productive, AI-driven development stack using cloud-based LLMs, terminal tools, IDEs, and mobile access. It is designed for developers who want persistent workflows, AI-powered coding assistance, and flexible access from multiple devices.

---

## TL;DR

- **Primary IDE:** [Cursor AI](https://www.cursor.com/) for daily work, [Claude Code](https://code.claude.com/) CLI for multi-file refactors.
- **Local completions:** [Ollama](https://ollama.ai/) with Qwen 2.5 Coder or Llama 3.3 to keep latency low and costs at zero.
- **Routing:** [OpenRouter](https://openrouter.ai/) as a single API gateway; [LiteLLM](https://litellm.ai/) if you want fallback chains.
- **Persistence:** [tmux](https://github.com/tmux/tmux) sessions survive disconnects; [Tailscale](https://tailscale.com/) makes your MacBook reachable from an iPhone without port forwarding.
- **Total baseline:** around $20/month (Cursor only) scaling to $40-50/month plus API usage for the full stack.

---

## Architecture Overview

### Hardware & Connectivity

An iPhone connects over Tailscale VPN to a MacBook Air. The MacBook runs tmux or zellij for session persistence, alongside Lungo or Patterned as keep-awake utilities.

### IDE & Editor Layer

- **Primary:** Cursor AI  -  fastest iteration with a native AI engine
- **Secondary:** VS Code (with Cline and Continue.dev)  -  battle-tested
- **Terminal:** Claude Code CLI  -  heavy multi-file work
- **SSH:** Termius  -  mobile remote access

[Cursor](https://www.cursor.com/) | [VS Code](https://code.visualstudio.com/) | [Cline](https://github.com/cline/cline) | [Continue.dev](https://continue.dev/) | [Claude Code](https://code.claude.com/) | [Termius](https://www.termius.com/)

### AI Tools & LLM Backends

- **Agents:** Cline, Claude Code, Aider, Windsurf
- **Local:** Ollama  -  free, instant completions
- **Routers:** OpenRouter, LiteLLM  -  cost and speed optimization
- **Web:** ChatGPT, Perplexity, Claude Web, Grok

[Aider](https://aider.chat/) | [Windsurf](https://codeium.com/windsurf) | [Ollama](https://ollama.ai/) | [OpenRouter](https://openrouter.ai/) | [LiteLLM](https://litellm.ai/) | [ChatGPT](https://chatgpt.com/) | [Perplexity](https://www.perplexity.ai/) | [Grok](https://x.com/i/grok)

---

## Tool Selection Decision Tree

**Use this to pick the right tool for the task:**

| Task | Best Tool | Why | Speed | Cost |
|------|-----------|-----|-------|------|
| Quick code completion | Cursor AI (inline) | Instant, local context | <100ms | $20/mo |
| Multi-file refactor | Claude Code CLI | Best at cross-file reasoning | 30-60s | $20/mo |
| Testing & test generation | Aider (CLI) | Specialized for tests, iterative | 10-30s | Free |
| Research + citations | Perplexity Web | Built-in fact-checking | 5-10s | Free |
| Image generation | Grok / Gemini | Purpose-built for images | 5-20s | Variable |
| Local completions (offline) | Ollama (Qwen 2.5 Coder 7B) | Zero cost, instant | <100ms | Free |
| Complex problem-solving | Claude Code + ChatGPT | Two perspectives, no blind spots | 1-2m | Combined |
| Code review + refactoring | Continue.dev (VS Code) | Good at style suggestions | 10-30s | Free |

---

## Component Descriptions

### iPhone
- **Purpose:** Mobile access to coding sessions, remote terminals, and LLM interfaces.
- **Tools:** Termius (SSH), web browsers for cloud LLMs.
- **Connection:** Via **Tailscale VPN** for secure, private access to your MacBook (no port forwarding).

### Tailscale VPN
- **Purpose:** Secure, on-demand [WireGuard-based](https://www.wireguard.com/) VPN that allows devices to communicate without exposing ports publicly.
- **Setup:** `brew install tailscale && tailscale up`
- **Use case:** Connect iPhone/iPad to your MacBook seamlessly, share files, run remote commands.
- **Learn more:** [Tailscale](https://tailscale.com/)

### MacBook
- **Purpose:** Primary development machine.
- **Enhancements:**
  - **[tmux](https://github.com/tmux/tmux) / [zellij](https://zellij.dev/):** Terminal multiplexers for persistent, multi-pane sessions.
  - **Lungo** or **Patterned:** Keep display awake without dimming during long coding sessions.
  - **caffeinate:** Built-in macOS utility to prevent sleep during long-running tasks: `caffeinate -dims &`

### IDEs and Terminals

#### Cursor AI (Primary)
- **Purpose:** AI-native IDE with advanced code reasoning and multi-file understanding.
- **When to use:** Daily coding, quick iterations, in-file suggestions, refactoring.
- **Strengths:** Fast, context-aware, great refactoring support.
- **Cost:** $20/month after free tier.
- **Keyboard shortcut:** Cmd+K for inline edits, Cmd+Shift+K for codebase search.

#### VS Code + Cline + Continue.dev (Secondary)
- **Purpose:** Battle-tested with AI extensions for automation.
- **When to use:** Complex projects requiring fine-grained control, or when you prefer open-source tooling.
- **Strengths:** Extensive plugin ecosystem, highly customizable.
- **Cost:** Free (extensions optional).

#### Claude Code CLI (Heavy Lifting)
- **Purpose:** Terminal-based AI assistant for multi-file projects.
- **When to use:** Major refactors, implementing large features, batch testing.
- **Strengths:** Best at understanding entire codebases, can modify multiple files at once.
- **Cost:** Claude API usage (typically $0.50-$2 per complex task).
- **Usage:** `claude code --file=src/ "refactor authentication module"`

#### Termius (Mobile SSH)
- **Purpose:** SSH client for remote server access from iPhone.
- **Setup:** Configure Tailscale + store SSH keys in Termius.
- **Use case:** Emergency fixes, monitoring from anywhere.

---

## LLM Routing & Orchestration

**Goal:** Assign each task to the model that solves it fastest and cheapest.

### Model Selection by Task

| Task Type | Recommended Model | Reason | Cost |
|-----------|-------------------|--------|------|
| Code generation | [Claude Sonnet 4.6](https://www.anthropic.com/claude) | Best for logic, edge cases | $0.003-0.015/task |
| Quick completions | Ollama (Llama 3.3 or Qwen 2.5 Coder) | Instant, local, free | Free |
| Research + facts | [Perplexity](https://www.perplexity.ai/) | Built-in web search, citations | Free / Pro |
| Image generation | [Grok](https://x.com/i/grok) or [Gemini](https://gemini.google.com/) | Fast visual reasoning | Variable |
| Debugging | [Claude Opus 4.7](https://www.anthropic.com/claude) | Strongest at error analysis | $0.015-0.06/task |
| Long-context tasks | Claude Sonnet 4.6 | 200K+ token window | $0.003-0.015/task |
| Cheap batch tasks | [Claude Haiku 4.5](https://www.anthropic.com/claude) | Fastest Claude model, low cost | $0.001-0.005/task |

### Setup: OpenRouter or LiteLLM

1. **OpenRouter** (recommended for simplicity):
   - Sign up at openrouter.ai
   - Get API key and add to env: `export OPENROUTER_API_KEY=sk-...`
   - Configure IDEs to use OpenRouter endpoint

2. **LiteLLM** (for advanced routing):
   - Install: `pip install litellm`
   - Create config file specifying fallback chains
   - Use in scripts: `from litellm import completion; response = completion(...)`

### Example Routing Logic

For fast tasks (under a 30-second deadline), set your primary model to Ollama (local and instant) with a cheap hosted backup via OpenRouter, such as [GPT-4o mini](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/) or Claude Haiku 4.5.

For complex tasks without a time limit, set your primary to Claude Opus 4.7 for best reasoning, and use a second frontier model (such as GPT-5 or Gemini 2.5 Pro) as a fallback for a second opinion.

---

## Setup Checklist

### Phase 1: Hardware & Connectivity (30 mins)
- [ ] Install Tailscale: `brew install tailscale && tailscale up`
- [ ] Install terminal multiplexer: `brew install tmux` or `brew install zellij`
- [ ] Install keep-awake utility: `brew install lungo` or search App Store for "Lungo"
- [ ] Verify SSH key on MacBook: `ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519`
- [ ] Install Termius on iPhone, add MacBook via Tailscale

### Phase 2: IDEs & Editors (1 hour)
- [ ] Download Cursor AI from [cursor.com](https://www.cursor.com/)
- [ ] Install VS Code: `brew install visual-studio-code`
- [ ] VS Code extensions: 
  - [ ] Cline (saoudrizwan.cline)
  - [ ] Continue (Continue.dev)
  - [ ] GitLens
- [ ] Cursor AI setup: Link GitHub account, configure models and API keys

### Phase 3: LLM Routing (30 mins)
- [ ] Create OpenRouter account at openrouter.ai
- [ ] Generate API key, add to `~/.zshrc`: `export OPENROUTER_API_KEY=sk-...`
- [ ] Install LiteLLM: `pip install litellm`
- [ ] Create `~/.config/litellm.yaml` with model preferences
- [ ] Test with: `python -c "from litellm import completion; print(completion(...))"`

### Phase 4: Claude Code CLI (15 mins)
- [ ] Install Claude Code: `brew install anthropic-ai/claude-code/claude-code`
- [ ] Authenticate: `claude code auth`
- [ ] Test: `claude code --help`
- [ ] Add to PATH if needed: `echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc`

### Phase 5: Terminal Setup (20 mins)
- [ ] Create tmux config: `vim ~/.tmux.conf`
- [ ] Copy example config from https://github.com/tmux-plugins/tpm
- [ ] Start persistent session: `tmux new -s dev -d`
- [ ] Alias for quick access: `echo "alias devs='tmux attach -t dev'" >> ~/.zshrc`
- [ ] Start keep-awake: `caffeinate -dims &` or open Lungo app

---

## Costs & Tradeoffs

### Subscription Summary
| Tool | Cost | Value | Notes |
|------|------|-------|-------|
| Cursor AI | $20/mo | High | Offset by faster coding speed |
| OpenAI (ChatGPT Pro) | $20/mo | Medium | Use for research, not coding |
| Perplexity Pro | $20/mo | Medium | Optional, good for cited research |
| Claude API (OpenRouter) | Pay-as-you-go | High | Usually $1-5/day if used heavily |
| GitHub Copilot | $10/mo | Low (if Cursor replaces it) | Redundant with Cursor |
| Ollama + Local Models | Free | High | Best value for completions |
| **TOTAL** | **~$40-50/mo + API** | | Can be reduced to $20/mo (Cursor only) |

### Cost Optimization Strategies
1. **Use Ollama for quick completions**  -  saves ~$200/month vs. API-only
2. **Route expensive tasks to cheaper models**  -  use Haiku 4.5 or GPT-4o mini instead of Opus/GPT-5 for simple edits
3. **Batch AI requests**  -  run multiple tasks in one session to amortize API calls
4. **Leverage free tiers**  -  Perplexity, Grok free tier for research
5. **Track usage**  -  Monitor OpenRouter dashboard to catch runaway costs

---

## Troubleshooting

### Common Issues & Solutions

**Problem: Claude Code timeout (>60s)**
- **Cause:** Large codebase or complex reasoning
- **Solution:** Break task into smaller chunks, or use ChatGPT for a "second opinion" first
- **Prevention:** Use Cursor AI for quick edits, reserve Claude Code for 5+ file changes

**Problem: Cursor AI not connecting to Tailscale**
- **Cause:** VPN not active or Tailscale daemon stopped
- **Solution:** `tailscale up`, then restart Cursor
- **Check:** `tailscale status` should show your devices

**Problem: Ollama is slow / consuming all CPU**
- **Cause:** Model too large for available RAM, or system under load
- **Solution:** Switch to a smaller model (e.g., Qwen 2.5 Coder 3B) or use cloud LLMs for critical tasks
- **Check:** `ollama ps` to see running models

**Problem: IDE/CLI tools conflicting over API keys**
- **Cause:** Multiple tools trying to authenticate simultaneously
- **Solution:** Use OpenRouter as single auth point, disable individual API keys
- **Setup:** Set `OPENROUTER_API_KEY` globally, remove `OPENAI_API_KEY` from individual tools

**Problem: Tailscale VPN drops on iPhone**
- **Cause:** WiFi/cellular switching, or Tailscale daemon restarted on Mac
- **Solution:** Toggle VPN off/on in Termius, restart MacBook daemon with `tailscale up`
- **Prevention:** Enable "always on" in Tailscale iPhone settings

**Problem: tmux session lost after MacBook sleep**
- **Cause:** caffeinate/Lungo didn't prevent sleep
- **Solution:** Use `caffeinate -dims &` in your tmux session, or ensure Lungo is running
- **Check:** `ps aux | grep caffeinate` to verify process is alive

---

## Performance Baselines

Use these to estimate task completion time and pick the right tool:

| Task | Tool | Time | Notes |
|------|------|------|-------|
| Add a function | Cursor AI | 15-30s | Inline, with context |
| Refactor 3-5 files | Claude Code CLI | 45-90s | Full codebase reasoning |
| Write unit test | Aider | 20-40s | Iterative, high accuracy |
| Debug error message | ChatGPT Web | 1-2m | Manual back-and-forth |
| Research question | Perplexity Web | 10-20s | Instant with citations |
| Image generation (3 iterations) | Grok | 30-45s | Via web UI |
| Local code completion (offline) | Ollama | <100ms | No latency |

---

## Keyboard Shortcuts for Speed

Add these aliases and keybindings to your `~/.zshrc`:

**Quick AI access:** alias `claude` to `claude code`, alias `aider` to `aider`, and alias `perp` to open the Perplexity web app in your browser.

**Terminal multiplexing:** alias `devs` to attach to the `dev` tmux session (or create one if it doesn't exist), and alias `devkill` to kill it.

**Tailscale shortcuts:** alias `tailon` to `tailscale up`, `tailoff` to `tailscale down`, and `tailstatus` to `tailscale status`.

### IDE Keybindings

**Cursor AI:**
- `Cmd+K`  -  inline edit
- `Cmd+Shift+K`  -  codebase search
- `Cmd+/`  -  AI chat

**VS Code (with Cline):**
- `Ctrl+Shift+`   -  open Cline
- `Ctrl+I`  -  inline edit (Continue.dev)

---

## Essential vs. Optional

### Core Stack (Must-Have)
- ✅ **Cursor AI** OR **VS Code + Cline** (pick one)
- ✅ **Claude Code CLI** (for heavy work)
- ✅ **Ollama** (free local completions)
- ✅ **Tailscale** (mobile access)

### Nice-to-Have (Recommended)
- 📌 **Perplexity** (research speed)
- 📌 **OpenRouter** (cost optimization)
- 📌 **Aider** (test generation)

### Optional (Niche Use Cases)
- 🔲 **Continue.dev** (if VS Code is your primary)
- 🔲 **Windsurf** (alternative to Cursor)
- 🔲 **GitHub Copilot** (redundant with Cursor)

---

## Workflow Example

### Morning Setup (2 mins)

Start a detached tmux session named `dev`, run `caffeinate -dims &` to prevent sleep, and bring Tailscale up. Your dev environment is now ready to attach to from any device on your tailnet.

### During Coding (all day)
1. **Quick edit** → Cursor AI inline (Cmd+K)
2. **Need research** → Jump to Perplexity in browser
3. **Stuck on bug** → Ask ChatGPT, get second opinion from Claude Code
4. **Write tests** → Use Aider: `aider --test src/myfeature.ts`
5. **Big refactor** → Claude Code CLI: `claude code --file=src/ "refactor..."`
6. **On mobile** → SSH via Termius → attach to dev tmux session

### Evening Cleanup

Kill the `dev` tmux session and bring Tailscale down to close out for the day.

---

## Tips & Best Practices

- **Keep tmux/zellij sessions persistent**  -  don't kill sessions, reattach and resume.
- **Use Tailscale for mobile-first**  -  no port forwarding, no security holes.
- **Route expensive tasks to cheaper models**  -  use Haiku 4.5 before Opus, Ollama before paid APIs.
- **Batch API requests**  -  group 5 small tasks into one session to save on round-trip overhead.
- **Monitor API costs**  -  set OpenRouter budget limits ($5/day) to avoid surprises.
- **Test locally first**  -  use Ollama for quick validation before hitting paid APIs.
- **Combine multiple tools**  -  use Claude for reasoning, ChatGPT for alternative viewpoints, Perplexity for facts.
- **Version your configs**  -  backup `~/.tmux.conf`, `~/.zshrc`, `~/.config/litellm.yaml` to git.

---

This stack provides **seamless mobile access, persistent development environments, AI coding assistants, and cost-optimized LLM routing**  -  ideal for solo developers or small teams who rely heavily on AI-driven productivity.

---

## Related Reading

- [AI Cloud Subscriptions: Comparing Pricing and Features in 2026](/ai/ai-cloud-subscriptions/)
- [Which Mac Studio Should You Buy for Running LLMs Locally?](/ai/mac-studio-local-llm-guide/)
- [Claude Code vs Cursor](/ai/claude-code-vs-cursor/)
- [Local vs Cloud AI in 2026](/ai/local-vs-cloud-ai-2026/)
- [Tailscale docs](https://tailscale.com/kb/) for VPN setup and advanced ACLs
- [Ollama model library](https://ollama.com/library) for picking local coding models
