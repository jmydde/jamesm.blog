---
title: "Own the Agent, Rent the Intelligence: Building My Always-On AI Agent Server"
date: 2026-09-19T06:20:00+01:00
draft: false
tags: ["ai", "agent", "hermes", "deepseek", "claude", "claude-code", "mac-mini", "hardware", "local-llm", "docker", "ollama", "mcp", "postgres", "observability"]
description: "Why I ended up choosing a Mac mini M6 (24GB) over a Mac Studio for an always-on AI agent server - and why the deciding factor wasn't local inference power at all, but cheap cloud routing through Hermes, DeepSeek V4.1 Flash, and Claude Sonnet 5."
cover:
  image: /assets/images/ai/mac-mini-m6-hermes-agent-infographic.jpg
  alt: Infographic of the always-on Hermes AI agent server - Mac mini M6 hardware and software on the left, Hermes routing policy with DeepSeek V4.1 Flash and Claude Sonnet 5 on the right
---

## TL;DR

- **Goal:** a small, silent, always-on machine that runs [Hermes Agent](https://hermes-agent.nousresearch.com/) ([GitHub](https://github.com/nousresearch/hermes-agent), [my review](/ai/hermes-agent/)) as a coordinator, with [Claude Code](https://claude.com/claude-code), [Codex](https://github.com/openai/codex), MCP servers, and automations independently of my laptop.
- **What I didn't need it to be:** a local inference workstation. I looked seriously at a Mac Studio and other machines capable of running 70B-class models, and talked myself out of it.
- **What I bought instead:** a **Mac mini M6, 24GB unified memory, 512GB SSD** (~£1,299) - enough headroom for containers, browsers, and small local models, not enough (or intended) to run frontier-class weights locally.
- **The routing policy:** small local model → [DeepSeek V4.1 Flash](https://api-docs.deepseek.com/quick_start/pricing) → [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5), cheapest capable model first.
- **The software layer:** Homebrew, GitHub CLI, Docker, Tailscale, tmux, and the usual Unix primitives on day one; Ollama, Playwright, Postgres, Qdrant, and Paperless next; observability and encrypted backups once agents are actually running unattended.
- **The number that changed my mind:** DeepSeek V4.1 Flash off-peak output is $0.60 per million tokens. Claude Pro is already $20/month (~£20). Electricity is £2-£4. A realistic month is a few dollars of DeepSeek on top of a subscription I already pay for.
- **The line I keep coming back to:** own the agent, rent the intelligence.

I've been experimenting with AI agents, coding assistants, and different models for a while now, but one problem kept coming up: my workflows were still tied to my laptop. Close the lid, and every agent, every scheduled job, every long-running task dies with it.

I wanted a small, silent computer that sits at home, runs 24/7, and acts as a permanent AI agent server - something that coordinates agents, executes tools, and intelligently routes hard work to the best cloud models, rather than trying to *be* the intelligence itself.

I'd been circling the idea of a proper local inference box for a while - the kind of machine that could run a genuinely large model at home. After actually pricing that route out, I landed somewhere much simpler:

> **Mac mini M6 (24GB) + Hermes Agent + Codex / Claude Code + DeepSeek V4.1 Flash + Claude Sonnet 5**

The interesting part isn't the shopping list. It's why I talked myself out of the bigger machine.

---

## What I Actually Needed

My main requirement wasn't local AI inference. It was **AI orchestration**.

I wanted a dedicated machine capable of continuously running:

- [Hermes Agent](/ai/hermes-agent/) as the coordinator, with [Claude Code](https://claude.com/claude-code) and [Codex](https://github.com/openai/codex) doing the actual coding work
- Docker containers
- [MCP servers](https://modelcontextprotocol.io/)
- Python (via [uv](https://docs.astral.sh/uv/)) and Node.js
- Git repositories plus the [GitHub CLI](https://cli.github.com/)
- Playwright / browser automation
- PostgreSQL and Redis
- A vector database such as [Qdrant](https://qdrant.tech/)
- Scheduled jobs
- Tailscale and SSH for remote access
- Small local models where useful, served by [Ollama](https://ollama.com/)
- Multiple cloud AI providers
- Encrypted backups and a health-check layer once agents are running unattended

That machine becomes the **body** of the AI system. The cloud models provide most of the **intelligence**. That distinction changes the hardware requirements completely - and it's the thing I got wrong on my first pass at this.

---

## The Hardware

**Apple Mac mini M6**

- M6, 12-core CPU (2 super / 4 performance / 6 efficiency), 12-core GPU, Dual 16-core Neural Engine
- **24GB unified memory**, up to 170GB/s memory bandwidth
- **512GB SSD**
- 2.5Gb Ethernet, Wi-Fi 7, Bluetooth 6
- macOS
- ~£1,299

The obvious question: why spend that much when an older, cheaper Mac mini would run Hermes just as well if all the inference happens in the cloud? That's a fair challenge, and an M1 or M2 mini with 16GB would genuinely be capable of it.

But this machine is meant to become permanent infrastructure, not another general-purpose computer I outgrow in a year. The extra memory buys headroom for containers, browser sessions, a vector database, and concurrent agent sessions - and unlike an external drive, it isn't upgradeable later. I'd rather have 24GB and not need it than hit a wall in two years and have to replace the whole box.

I also looked at the same chip with less storage - **Mac mini M6, 24GB/256GB, £1,099** - and ruled it out for a more mundane reason: not enough SSD headroom once you account for container images, logs, a local vector database, and caching, on a box that's meant to keep running for years without a storage upgrade path. £200 for another 256GB was an easy call.

---

## The Full Shortlist: Every Machine I Priced Out

The Mac mini wasn't the only box on the list, and it wasn't even the first purpose-built option I looked at. Roughly cheapest to most expensive, here's everything else I priced out - Mac and non-Mac - and why each one is or isn't what's sitting on my desk now.

| Option | Spec | Price | Verdict |
|---|---|---:|---|
| [Umbrel Home](https://umbrel.com/umbrel-home) | Intel N150 quad-core, 16GB (soldered), 2TB NVMe | £699 (£599-£949 across capacities) | Ruled out - not upgradeable, not general-purpose enough |
| [Start9 Server One](https://store.start9.com/products/server-one-2026) | AMD Ryzen 5/7, up to 32GB LPDDR5, up to 4TB NVMe | $899-$1,399 | Ruled out - no official Hermes app, no Docker Compose |
| Mac mini M6 | 24GB unified memory, 256GB SSD | £1,099 | Ruled out - too little SSD headroom |
| **Mac mini M6** | **24GB unified memory, 512GB SSD** | **£1,299** | **Bought** |
| Used RTX 3090/4090 (GPU only, not a full machine) | 24GB VRAM | ~£600-700 second-hand | Ruled out - solves a problem I don't have |
| [Ryzen AI Max+ 395 mini PC](https://www.layer3labs.io/gear/ryzen-ai-mini-pcs) | up to 128GB unified LPDDR5X | roughly £1,500-£2,500+ depending on OEM | Ruled out - same reason as the 3090 |
| [NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) | 128GB unified LPDDR5X (only option), 4TB NVMe | $4,699 (~£3,700) | Ruled out - fixed 128GB, same reason as the Mac Studio |
| Mac mini M5 Pro | 64GB unified memory | £3,199 | Ruled out - overkill for an API router |
| Mac Studio (M5 Max / M5 Ultra) | up to 128GB / up to 512GB | £3,000-£4,500+ | Ruled out - enterprise-grade |

### Umbrel Home - the purpose-built appliance, and why 16GB soldered was the dealbreaker

[Umbrel Home](https://umbrel.com/umbrel-home) is genuinely well-matched to this job on paper: an Intel N150 quad-core box with 16GB of DDR5 and a choice of 1TB/2TB/4TB NVMe storage, running £599-£949 depending on capacity (I was pricing the 2TB config, £699). It runs a containerized, Docker-native OS with Tailscale and Tor built in, draws about 10W, and - the part that made it a serious contender - [Hermes Agent is an official one-click install from the Umbrel App Store](https://apps.umbrel.com/app/hermes-agent), published directly by Nous Research. There's also [Umbrel Pro](https://umbrel.com/umbrel-pro) for more storage, same 16GB memory ceiling.

I even priced out running two Umbrel units instead of one Mac mini - one for Hermes, one as a secondary node - and talked myself out of it. Two boxes with 16GB of soldered, non-upgradeable memory each don't add up to more usable headroom than one machine with 24GB and room to run Docker, Postgres, Redis, Qdrant, and a browser session at the same time, and I'd rather administer one box than keep two in sync. The 16GB ceiling on a single unit was the real problem: fine for Hermes alone, tight the moment you add a vector database and a few concurrent browser-automation sessions on a machine that's meant to be permanent infrastructure with no upgrade path. If all I wanted was Hermes running somewhere, Umbrel Home would be the cheaper, more purpose-built answer.

### Start9 Server One - a similar shape of box, ruled out on packaging

[Start9](https://store.start9.com/products/server-one-2026) makes a comparable home-server appliance: AMD Ryzen 5 or 7, configurable up to 32GB of RAM and 4TB of NVMe, running $899-$1,399 depending on spec, on their own OS with its own curated app marketplace. It's a step up from Umbrel Home on RAM ceiling alone. Two things ruled it out quickly, though: there's no official Hermes Agent app in their marketplace, and StartOS doesn't support Docker Compose - it only runs one Dockerfile per service, so anything outside the marketplace has to be hand-packaged into their own format and sideloaded rather than just `docker compose up`. More friction than Umbrel for the one app I actually needed, so it didn't get further than the shortlist.

### A used RTX 3090/4090 - the right answer to a question I wasn't asking

Part of my earlier local-inference research was sizing GPUs rather than complete machines. The rough ladder, for reference:

- **8-16GB VRAM**: 7B-14B models
- **24GB VRAM** (a used RTX 3090 or 4090, roughly £600-700 second-hand): 32B models at Q4 quantization - the local sweet spot for price against capability
- **48GB+ VRAM**: 70B-class models, at which point you're stacking cards or buying workstation-grade hardware

A used 3090/4090 is the correct answer if the goal is "run the biggest model I can locally for the least money." It stopped being relevant here because that was never the actual goal - Hermes calls hosted models over an API, so there's no local inference workload for a 24GB card to accelerate. Buying one would mean building (and powering, and cooling) a second machine to sit next to the Mac mini and mostly idle, which is exactly the trap I was trying to avoid by not buying a Mac Studio.

Worth noting for anyone doing the same comparison: Apple Silicon trades roughly 40-70% of an NVIDIA card's raw inference throughput for full unified-memory access to the weights, with no separate VRAM ceiling to size around - one reason the Mac Studio conversation below is about memory capacity rather than GPU throughput. And [Ollama](https://ollama.com/) is the sensible default runtime either way - an OpenAI-compatible API with tens of millions of monthly downloads, and it slots straight into Cline, Continue.dev, and Claude Code if I ever do want a local model in the loop.

### Ryzen AI Max+ 395 mini PCs - huge memory, same problem as the 3090

This is the non-Mac mini PC people usually bring up in this conversation, and for good reason: AMD's Ryzen AI Max+ 395 pairs 16 Zen 5 cores with up to 128GB of unified LPDDR5X memory, up to 96GB of which can be handed to the integrated GPU - enough to load genuinely large models without a discrete card at all. [GMKtec's EVO-X2 is usually the cheapest way into a full 128GB configuration](https://www.layer3labs.io/gear/ryzen-ai-mini-pcs), with Beelink, Framework Desktop, Bosgame, and HP all shipping their own versions at various price points, generally landing somewhere between a Mac mini and a Mac Studio.

It's a legitimately good machine for local inference - arguably better value than a Mac Studio on a pure £-per-GB-of-memory basis. But it's still solving the problem I decided I didn't have: a 128GB local box only pays for itself if you're running large models locally often enough that the hardware cost beats the API bill. Mine doesn't, so it joined the 3090 and the Mac Studio in the "genuinely good hardware, wrong problem for this build" pile.

### NVIDIA DGX Spark - one fixed memory size, and no cheaper way in

[NVIDIA's DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) is the purpose-built compute appliance in this comparison rather than a general-purpose mini PC: a GB10 Grace Blackwell Superchip pairing a Blackwell-generation GPU with a 20-core Arm CPU, **128GB of unified LPDDR5X memory at 273 GB/s bandwidth**, a 4TB NVMe SSD, up to 1 petaFLOP of FP4 compute, in a 5.9" x 5.9" x 2" box drawing roughly 240W under load. It launched at $3,999 and NVIDIA raised that to **$4,699** (~£3,700) in February 2026, citing memory supply constraints - pricing that's held through to when I was shopping for this build.

Two things ruled it out quickly. First, unlike the Mac mini or Mac Studio, there's no smaller or cheaper configuration to step down into - DGX Spark ships in exactly one memory size, 128GB, full stop. The $4,699 entry price is the only price. Second, and more fundamentally, it's the same "wrong problem" as the Mac Studio and the Ryzen AI Max+ box below: Hermes calls hosted models over an API, so 128GB of unified memory and a petaFLOP of Blackwell compute would sit there mostly idle behind an agent orchestrator that doesn't do local inference. DGX Spark genuinely wins for prefill-heavy workloads and CUDA fine-tuning - I go through the benchmarks properly in [DGX Spark vs Mac Studio](/ai/dgx-spark-vs-mac-studio/) - but neither is what an always-on agent server needs.

---

## Why I Didn't Build a Local Inference Machine

This was the actual conclusion of the research, and it's the opposite of where I started.

Running powerful models locally sounds attractive on paper: no API bills, complete privacy, no dependency on a provider. I looked hard at this - Mac Studio configurations, Ryzen AI Max mini PCs with huge unified memory pools, even GPU rigs capable of running 70B models at speed. I go into the local-inference sizing question properly in [Which Mac Studio Should You Buy for Running LLMs Locally?](/ai/mac-studio-local-llm-guide/) and [DGX Spark vs Mac Studio](/ai/dgx-spark-vs-mac-studio/) if you want the hardware-comparison version of this.

Small models are easy - an 8B model runs comfortably on almost anything modern. Once you go past 30B, though, memory bandwidth becomes the constraint, and getting to something like 100 tokens/second on a 30B-class model generally means serious GPU hardware: more cost, more electricity, more heat, more noise, more depreciation. And even after spending thousands, the result can still be meaningfully behind a frontier model available over an API.

That made me question the entire objective. I wasn't trying to build an AI agent server - I was trying to reproduce a slice of a datacentre in my house, for a worse result than just calling one.

### Specifically, why not the Mac mini M5 Pro, or a 64GB, 128GB or 256GB Mac Studio?

I went back and forth on this one longest, because a Mac Studio - or the step just below it - was the obvious "just buy enough memory and stop worrying about it" answer. I priced a **Mac mini M5 Pro with 64GB for £3,199**: same chassis as the machine I bought, same idea as the Mac Studio conversation, just in a smaller box. The extra £1,900 over my final spec buys local-inference headroom for 30B-70B class models, which I ruled out for the identical reason as the Mac Studio below - Hermes calls hosted models over an API rather than running local inference, so that headroom would sit unused.

The honest reason I didn't go further up to a Mac Studio is cost, plainly: an M2/M3 Ultra with 64-128GB is somewhere around £3,000-£4,500, and a 256GB config (where you can still get one) pushes well past that. That's real money to spend on hardware whose main job would be sitting mostly idle, running inference I can currently get from DeepSeek for a few dollars a month.

I'm not against local frontier-class inference on principle - I just can't justify that outlay *right now* against what I'm actually getting for it. £3k+ buys a lot of DeepSeek and Claude API calls, and I'm genuinely fine with the privacy and latency trade-offs of calling cloud models for the hard reasoning, given the security and confirmation-gate layer I already run in front of anything an agent can do (see [Securing AI Agents](/ai/securing-ai-agents/)). If the economics were different - if I were running enough volume that the API bill rivalled the hardware cost, or if a 128GB machine were meaningfully cheaper - the answer might flip.

### The bet I'm making instead

I wrote about this properly in [The Day I Stop Chasing Better AI: When Frontier Models Come Home](/ai/frontier-models-come-home/): my guess is that somewhere around 2029-2031, the capability of *today's* frontier cloud models becomes cheap enough to run permanently on desktop-class hardware. When that happens, a local machine won't need to chase whatever the frontier is at that point - it just needs to match what Claude Sonnet 5 or DeepSeek V4.1 Flash can already do today, which will look increasingly modest as hardware and smaller/smarter models both improve.

So the Mac mini isn't a rejection of local inference, it's a deferral. Right now, cheap cloud models make a big local-inference machine hard to justify. In a few years, I expect that trade to flip - at which point the sensible move is to buy the local hardware once it can match today's cloud frontier for a fraction of the cost, rather than buying it now while it's still catching up.

---

## Cloud AI Changes the Economics

The deciding factor was [DeepSeek's](https://www.deepseek.com/) API pricing. [V4.1 Flash](https://api-docs.deepseek.com/news/news260910) shipped in September 2026 as `deepseek-flash` - native vision, 1M context, tool calling, and cheaper than the V4 Flash it replaced. It makes genuinely capable inference cheap enough that I stopped thinking of "AI compute" as something I need to own outright, and started treating it more like a utility. Hermes picks the appropriate model for each task:

```text
Small local model
       ↓
DeepSeek V4.1 Flash
       ↓
Claude Sonnet 5
```

Each tier is only used when the tier below it isn't enough. DeepSeek still lists V4 Pro on the API, but it isn't in this routing path - V4.1 Flash is the default workhorse, and Sonnet 5 is the independent frontier opinion.

### Local models (on the Mac mini)

Small models like Qwen 8B, Qwen 14B, or Granite 8B still run fine on the Mac mini - not to compete with Claude or DeepSeek, but for classification, extraction, simple SQL, routing decisions, local RAG, and anything that should stay private or work offline. Roughly 40-70 tok/s on an 8B and 25-40 tok/s on a 14B, depending on quantisation. Cost per token here is £0, electricity aside.

**Best for:** simple, repetitive, private, or offline tasks.

### DeepSeek V4.1 Flash (default workhorse)

This is where most everyday coding, reasoning, and agent work should land. 1M context, tool calling, vision, max output 384K. API throughput is roughly 100-300 tok/s depending on load. Current pricing (per [DeepSeek's API pricing page](https://api-docs.deepseek.com/quick_start/pricing)):

| V4.1 Flash (per 1M tokens) | Off-Peak | Peak |
|---|---:|---:|
| Input (cache hit) | $0.003 | $0.006 |
| Input (cache miss) | $0.15 | $0.30 |
| Output | **$0.60** | **$1.20** |

DeepSeek's peak window is 01:00-04:00 and 06:00-10:00 UTC, Monday to Friday, excluding Chinese public holidays. Weekends, those holidays, and every other weekday hour are off-peak at half the peak rate.

**Best for:** most everyday coding, reasoning, and agent tasks.

### Claude Sonnet 5 (escalation / second opinion)

I already pay for [Claude Pro](https://www.anthropic.com/pricing) at $20/month (~£20), so [Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) becomes the final escalation - for when DeepSeek struggles, a coding problem is genuinely hard, the task is high-risk, or I want a second opinion from a different model family. API list price is $2 / $10 per million input/output tokens; Pro covers the Sonnet 5 usage on this box unless I blow past the subscription limits. Context is up to 1M tokens with a 128K max output.

**Best for:** complex tasks, high risk, independent reasoning.

---

## The Routing Policy

Rather than deciding manually which model handles a given request, Hermes makes that call:

```text
                    Incoming task
                 (user / agent / schedule)
                          │
                          ▼
             Simple, repetitive, private,
                 or offline task?
                    │           │
                   YES          NO
                    │           │
                    ▼           ▼
             Local model   DeepSeek V4.1 Flash
             Qwen 8B/14B   (default workhorse)
             Granite 8B
                    │           │
                    └─────┬─────┘
                          ▼
              Failed, very difficult,
                 or high risk?
                    │           │
                   NO          YES
                    │           │
                    ▼           ▼
                  Finish   Claude Sonnet 5
                                │
                                ▼
                       Still struggling, or
                    want a second opinion?
                          │           │
                         YES          NO
                          │           │
                          ▼           ▼
                 Second opinion     Finish
```

The objective isn't to minimise cost for its own sake - it's to use the cheapest model that can reliably finish the task.

---

## What This Actually Costs

Output-only, off-peak, per [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing) and [Anthropic](https://www.anthropic.com/pricing):

| Model | 1M tokens | 10M tokens | 100M tokens |
|---|---:|---:|---:|
| Local (Qwen 8B/14B, Granite 8B) | £0 | £0 | £0 |
| DeepSeek V4.1 Flash | $0.60 | $6.00 | $60.00 |
| Claude Sonnet 5 (API) | $10.00 | $100.00 | $1,000.00 |

I don't pay Sonnet 5 per token for this machine. Claude Pro at $20/month already includes it. A realistic mix is mostly Flash, with Sonnet 5 as escalation on that subscription:

```text
80% DeepSeek V4.1 Flash → 8M × $0.60  = $4.80
20% local / Claude Pro  → 2M           = $0.00 extra
Claude Pro (already paid)              = $20.00
Electricity (~10-15W, ~£2-£4)          ≈ $3.00
                                   --------
                    Total ≈ $28/month  (~£21)
```

A lighter month - a few million Flash tokens rather than 10M - lands closer to $22, which is essentially Claude Pro plus a couple of dollars of DeepSeek. Input costs are additional, and cached input on Flash is $0.003 per million off-peak. Either way this is well under the cost of a GPU workstation. Electricity for the Mac mini itself is negligible next to running a GPU rig continuously - it's also silent, tiny, and low-heat, which matters more than benchmark numbers for a box that has to live under a desk permanently.

---

## Why Not Just Use My Laptop?

Because I want the agents to exist independently of it. My laptop should be a client, not the infrastructure. I want to be able to close it, leave the house, reboot it, or switch machines entirely without killing every scheduled job and running agent.

With [Tailscale](https://tailscale.com/) and SSH, I can reach the Mac mini remotely while it stays safely on my home network - the same pattern I've used before for [phoning a home agent](/ai/phone-your-home-ai-agent/) without opening a port on my router. Hermes keeps executing scheduled tasks and workflows regardless of what I'm doing with my laptop.

---

## Software and Tools

The hardware is settled. Hermes plus Paperless is not enough of a software layer: "Docker, MCP, Python/Node" is the orchestration *idea*, not the actual stack an always-on agent server needs.

Hermes should be the **coordinator**, not the thing doing every piece of work itself. Coding goes to Claude Code and Codex. Services, databases, and Paperless run in Docker. Small local models go through Ollama. Secrets stay out of `.env` files. And once agents are running unattended, I want to know they are still up without discovering three days later that a launchd job died.

I'm not installing all of this on day one. The table is the target stack; the phases further down are the order.

| Tool | Priority | What it's for |
|---|---|---|
| [Homebrew](https://brew.sh/) | Essential | Package management for everything that isn't a container |
| Git + [GitHub CLI (`gh`)](https://cli.github.com/) | Essential | Repos, PRs, issues, Actions, auth - the biggest omission if this is going to be an autonomous development machine |
| [Docker Desktop](https://www.docker.com/products/docker-desktop/) | Essential | Run services, MCP helpers, and databases without cluttering macOS |
| [Tailscale](https://tailscale.com/) | Essential | Secure remote access without opening router ports |
| [tmux](https://github.com/tmux/tmux) | Essential | Persistent terminal and admin sessions even if Hermes itself runs as a service |
| [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`) | Essential | Fast repo search - the primitive agents actually use |
| [jq](https://jqlang.github.io/jq/) + [yq](https://github.com/mikefarah/yq) | Essential | JSON/YAML manipulation for scripts and tool output |
| [uv](https://docs.astral.sh/uv/) | Essential | Fast Python environments, so agents don't turn a global install into a dependency graveyard |
| Node.js via [fnm](https://github.com/Schniz/fnm) | Essential | MCP servers, Playwright, JS tooling |
| [Hermes Agent](https://hermes-agent.nousresearch.com/) ([GitHub](https://github.com/nousresearch/hermes-agent), [my review](/ai/hermes-agent/)) | Essential | Persistent coordinator: memory, routing, scheduled work |
| [Claude Code](https://claude.com/claude-code) | Recommended | Coding agent Hermes can hand work to, rather than implementing every edit itself |
| [Codex](https://github.com/openai/codex) | Recommended | Same idea from the OpenAI side; Hermes can optionally run Codex as a runtime underneath it |
| [Ollama](https://ollama.com/) ([my write-up](/ai/ollama/)) | Recommended | Local Qwen and Granite models for private, cheap, or offline tasks |
| [Playwright](https://playwright.dev/) | Recommended | Browser automation: logins, deploys, forms, screenshots, regression checks |
| [Qdrant](https://qdrant.tech/) | Recommended | Vector / RAG memory, in Docker |
| [PostgreSQL](https://www.postgresql.org/) | Recommended | Durable structured agent state and an audit trail, in Docker |
| [Paperless-ngx](https://docs.paperless-ngx.com/) ([GitHub](https://github.com/paperless-ngx/paperless-ngx), [my write-up](/ai/paperless-ngx-self-hosted-document-management/)) | Recommended | Self-hosted document archive with OCR, in Docker |
| [Restic](https://restic.net/) | Recommended | Encrypted backups. Time Machine is not enough for this box. |
| [1Password CLI](https://developer.1password.com/docs/cli/) | Recommended | Agent-accessible secrets without plaintext `.env` files |
| [Redis](https://redis.io/) | Later | Queues, locks, transient state, in Docker |
| [Loki](https://grafana.com/oss/loki/) + [Grafana](https://grafana.com/) | Later | Agent and service logs once several things are running unattended |
| [Uptime Kuma](https://uptime.kuma.pet/) | Later | Simple health checks with a phone alert when Hermes has been down for four minutes |
| [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) | Optional | Expose a selected service without port forwarding. Tailscale covers me for almost everything. |

If I sit down at the machine today, the first additional installs are `gh`, `uv`, `tmux`, `ripgrep`, `jq`, `yq`, `fzf`, Docker, Tailscale, Ollama, and Playwright. Postgres, Qdrant, Redis, and Paperless stay behind Docker rather than living on macOS itself.

### Hermes as coordinator

The machine is structured around Hermes handing work out, not swallowing it:

```text
Hermes
   │
   ├── Git
   ├── GitHub CLI
   ├── Claude Code
   ├── Codex
   ├── DeepSeek
   ├── MCP
   ├── Playwright
   └── Docker
```

That is closer to a personal AI operating system than "a Mac running Hermes." It also matches how Hermes is actually evolving: it can optionally hand `openai/*` and `openai-codex/*` turns to the [Codex CLI app-server](https://hermes-agent.nousresearch.com/docs/user-guide/features/codex-app-server-runtime) instead of running its own tool loop. Native Codex plugins such as GitHub, Linear, Gmail, and Calendar then show up inside the Hermes session. Default Hermes behaviour is unchanged unless you opt in.

[GitHub CLI](https://cli.github.com/) is the biggest day-one gap. With `gh auth login` in place, Hermes, Claude Code, and Codex can work with issues, pull requests, branches, releases, Actions, and code review instead of treating GitHub as a remote you only `git push` to.

### Python, terminals, and boring Unix tools

Python is [uv](https://docs.astral.sh/uv/), not a global Homebrew Python that every agent pollutes:

```bash
brew install uv
uv python install 3.13
```

Each project gets its own environment. Agents do not inherit last month's dependency soup.

[tmux](https://github.com/tmux/tmux) is the emergency/admin layer even if Hermes normally runs as a service:

```text
tmux
├── hermes
├── coding
├── monitoring
├── paperless
└── maintenance
```

And the unglamorous CLI tools are extremely useful once an agent is exploring a repo or parsing tool output. On every agent machine I want `rg`, `fd`, `jq`, `yq`, and `fzf`; `bat` and `tree` come along for free:

```bash
brew install ripgrep jq yq fzf fd bat tree gh uv tmux
```

### Local models without becoming a local-inference workstation

[Ollama](https://ollama.com/) goes on even though this is deliberately *not* a local-inference box. The 24GB is for small Qwen or Granite models doing classification, extraction, routing, simple SQL, and anything that should stay private or work offline - not for keeping an enormous model resident.

```text
Hermes
   │
   ├── Qwen 8B / Granite 8B  ← cheap / private / simple
   │
   ├── DeepSeek V4.1 Flash   ← normal work
   │
   └── Claude Sonnet 5       ← hardest / second opinion
```

That is a much better use of this machine than trying to run a 70B-class model continuously. I wrote about the Ollama setup itself in [Running AI Models Locally with Ollama](/ai/ollama/).

### Browser automation as a first-class component

[Playwright](https://playwright.dev/) is not a nice-to-have for a box that is meant to keep working while I am not looking. Login checks, deployment verification, form submission, screenshots, regression tests - those are jobs, not prompts. A nightly loop looks more like:

```text
Nightly
   ↓
Hermes
   ↓
Open a production site
   ↓
Check critical pages / login / forms
   ↓
Check errors
   ↓
Report anomalies
```

That is more useful than an LLM sitting idle waiting for the next chat.

### Memory: four stores, not one vector database

Qdrant stays in Docker. Postgres does too. I am not making a vector database the entire memory system.

```text
PostgreSQL
    ↓
facts / jobs / state / audit records

Qdrant
    ↓
semantic memory / documents / previous investigations

Git
    ↓
code / configuration / agent instructions

Markdown
    ↓
human-readable knowledge
```

Postgres rather than SQLite for the core persistent services. For an autonomous agent the audit trail matters more than squeezing another few percent out of the model: what did you do, why, which model decided it, which tools ran, what changed. Tables along the lines of `agent_runs`, `agent_tasks`, `agent_events`, `agent_errors`, `approvals`, `scheduled_jobs`, `model_usage`, `model_cost`, and `security_events`.

Paperless is the document half of that picture - OCR'd paperwork the agent can search, not rewrite. I go through the product itself in [Paperless-ngx](/ai/paperless-ngx-self-hosted-document-management/).

### Secrets, backups, and (later) observability

Once Hermes has real permissions, plaintext `.env` files full of API keys are the wrong shape. The goal is:

```text
Agent → approved secret → tool
```

not "read the entire `.env` and here are 27 credentials." [1Password CLI](https://developer.1password.com/docs/cli/) fits the confirmation-gate approach I already use in [Securing AI Agents](/ai/securing-ai-agents/).

Backups are [Restic](https://restic.net/), encrypted, and not Time Machine alone. Local working data, an external copy, and an encrypted off-machine copy. At minimum: Hermes config and memory, agent instructions, project repos, Postgres dumps, Qdrant snapshots, and Paperless documents.

Observability is the piece that can wait until several agents are actually running, and then becomes critical. Loki and Grafana for logs; Uptime Kuma watching Hermes, Postgres, Qdrant, Paperless, MCP endpoints, and anything customer-facing. The point is a phone alert that Hermes has been down for four minutes, not a forensic reconstruction three days later. I covered the Grafana/Loki side of this more generally in [Monitoring and Observability](/devops/monitoring/).

```text
                 ┌───────────────┐
                 │    Hermes     │
                 └───────┬───────┘
                         │
                ┌────────▼────────┐
                │ Agent event log │
                └────────┬────────┘
                         │
          ┌──────────────┼─────────────┐
          ↓              ↓             ↓
      PostgreSQL        Loki        metrics
          │              │             │
          └──────────────┼─────────────┘
                         ↓
                      Grafana
```

### Don't install everything at once

**Phase 1 - foundation**

```text
Homebrew, Git, GitHub CLI, Tailscale, SSH, tmux,
ripgrep, jq, yq, uv, Node.js, Docker
```

**Phase 2 - AI**

```text
Hermes, Claude Code, Codex, Ollama, Qwen, MCP servers
```

**Phase 3 - agent capabilities**

```text
Playwright, PostgreSQL, Qdrant, Redis, Paperless-ngx
```

**Phase 4 - autonomous infrastructure**

```text
launchd, Uptime Kuma, Grafana, Loki, Restic,
automated backups, health checks, cost monitoring
```

---

## The Final Architecture

```text
                         ┌──────────────┐
                         │    HUMAN     │
                         └──────┬───────┘
                                │
                         approval / goals
                                │
                         ┌──────▼───────┐
                         │    HERMES    │
                         │  coordinator │
                         └──────┬───────┘
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
     ┌────▼────┐          ┌─────▼──────┐        ┌─────▼─────┐
     │  Local  │          │  DeepSeek  │        │  Claude   │
     │ Qwen /  │          │ V4.1 Flash │        │ Sonnet 5  │
     │ Granite │          └────────────┘        └───────────┘
     └─────────┘
                                │
                    ┌───────────┼───────────┐
                    │           │           │
                 Codex     Claude Code   Playwright
                    │           │           │
                    └───────────┼───────────┘
                                │
                     ┌──────────▼──────────┐
                     │     Tool layer      │
                     │ MCP / Git / GitHub  │
                     │ Docker / APIs / SSH │
                     └──────────┬──────────┘
                                │
             ┌──────────────────┼──────────────────┐
             ↓                  ↓                  ↓
          Postgres            Qdrant          Paperless
```

The Mac provides the persistent execution environment. Hermes coordinates. Codex and Claude Code do the coding. DeepSeek V4.1 Flash and Claude Sonnet 5 provide the intelligence. Local models provide privacy, speed, and offline capability. Postgres, Qdrant, and Paperless are the memory and document layer, all in Docker.

Here's the hardware and routing view as one infographic - Mac mini and local services on the left, the Hermes decision flow with DeepSeek V4.1 Flash and Claude Sonnet 5 on the right:

![Infographic of the always-on Hermes AI agent server - Mac mini M6 hardware and software on the left, Hermes routing policy with DeepSeek V4.1 Flash and Claude Sonnet 5 pricing on the right](/assets/images/ai/mac-mini-m6-hermes-agent-infographic.jpg)

Why this setup works:

- Best-in-class cloud models for the money (DeepSeek V4.1 Flash / Claude Sonnet 5)
- Local models for privacy, speed, and offline use
- Smart routing keeps cost down without giving up quality
- Mac mini M6 is silent, efficient, and built for 24/7
- Predictable monthly running cost

This is a work in progress and subject to change as the build evolves - worth checking back on this post for updates rather than treating it as final.

---

## Why the M6 24GB Mac Mini, in the End

I looked at cheaper Mac minis, high-end Mac minis, Mac Studios, a purpose-built Umbrel Home appliance, Ryzen AI Max mini PCs with huge unified memory pools, and a used RTX 3090/4090 built into its own GPU rig. I kept optimising the wrong variable.

I don't need to own the AI compute. I need to own the orchestration layer. Cloud AI is improving fast enough that spending several thousand pounds today to replicate it locally risks buying hardware that's outclassed before it's paid for itself. The Mac mini gives me plenty of headroom for the part I actually want to own - agents, tools, memory, databases, automation, browsers, code, MCP, workflows - while the inference layer stays swappable. Today that's DeepSeek V4.1 Flash → Claude Sonnet 5, with Claude Code and Codex as the coding workers underneath Hermes. If something better or cheaper shows up, I change a routing config, not the hardware.

**Own the agent, rent the intelligence.** My files, tools, databases, automation, and agent state stay under my control on hardware I own. When an agent needs serious reasoning power, it borrows infrastructure far bigger than anything I'd reasonably install at home, for a few dollars a month.

---

## Final Setup

- **Hardware:** Mac mini M6, 24GB unified memory, 512GB SSD, ~£1,299 one-off
- **Coordinator:** [Hermes Agent](https://hermes-agent.nousresearch.com/) by [Nous Research](https://www.nousresearch.com/), [open source on GitHub](https://github.com/nousresearch/hermes-agent)
- **Coding agents:** [Claude Code](https://claude.com/claude-code) and [Codex](https://github.com/openai/codex), with Hermes optionally using Codex's [app-server runtime](https://hermes-agent.nousresearch.com/docs/user-guide/features/codex-app-server-runtime)
- **Local AI:** Qwen 8B/14B and Granite 8B via [Ollama](https://ollama.com/), where appropriate
- **Default cloud AI:** DeepSeek V4.1 Flash (`deepseek-flash`)
- **Frontier escalation:** Claude Sonnet 5 (Claude Pro, $20/month / ~£20, already paid for)
- **Access:** [Tailscale](https://tailscale.com/) and SSH - no router ports opened
- **Data:** PostgreSQL, Qdrant, and [Paperless-ngx](https://docs.paperless-ngx.com/) in Docker
- **Secrets / backups:** [1Password CLI](https://developer.1password.com/docs/cli/) and [Restic](https://restic.net/)
- **Running cost:** Claude Pro $20 + a few dollars of DeepSeek + £2-£4 electricity

---

## Conclusion

I started this research expecting to end up buying a powerful local inference workstation. I ended up deciding almost the opposite: for an always-on agent server, the orchestrator doesn't need to be the intelligence. It needs to be reliable, quiet, efficient, and good at coordinating everything else - which is exactly what a small Mac mini is for.

Small jobs stay local. Most serious work goes to DeepSeek V4.1 Flash. Hard or high-risk problems escalate to Claude Sonnet 5. Coding work goes to Claude Code and Codex rather than making Hermes implement every edit. Rather than spending thousands trying to bring a datacentre into my house, I've built a small, efficient gateway into whichever models happen to be best at the time - which feels like a considerably more future-proof way to run an always-on personal AI system.

This build is still evolving, so I'll keep this post updated as the setup changes.

## Related Reading

- [Hermes Agent: Persistent Autonomy That Learns and Grows](/ai/hermes-agent/)
- [Securing AI Agents: Tool-Calling Risks, MCP Hardening, and the Confused Deputy Problem](/ai/securing-ai-agents/)
- [Giving Your Home AI Agent Real Tools: MCP Servers on a Mac mini M6](/ai/mcp-servers-home-ai-agent/)
- [Paperless-ngx: Self-Hosted Document Management Without the Vendor Lock-in](/ai/paperless-ngx-self-hosted-document-management/)
- [Running AI Models Locally with Ollama: From Setup to OpenClaw](/ai/ollama/)
- [Which Mac Studio Should You Buy for Running LLMs Locally?](/ai/mac-studio-local-llm-guide/)
- [DGX Spark vs Mac Studio: Which Personal AI Supercomputer Should You Buy?](/ai/dgx-spark-vs-mac-studio/)
- [Local AI vs Cloud AI in 2026](/ai/local-vs-cloud-ai-2026/)
- [The Day I Stop Chasing Better AI: When Frontier Models Come Home](/ai/frontier-models-come-home/)
- [Monitoring and Observability](/devops/monitoring/)
