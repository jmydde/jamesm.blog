---
title: "Own the Agent, Rent the Intelligence: Building My Always-On AI Agent Server"
date: 2026-09-03T07:00:00+01:00
draft: false
type: guide
tags: ["ai", "agent", "hermes", "deepseek", "claude", "mac-mini", "hardware", "local-llm"]
description: "Why I ended up choosing a Mac mini M6 (24GB) over a Mac Studio for an always-on AI agent server - and why the deciding factor wasn't local inference power at all, but cheap cloud routing through Hermes, DeepSeek, and Claude."
cover:
  image: /assets/images/ai/mac-mini-m6-hermes-agent-infographic.png
  alt: Infographic showing the Mac mini M6 hardware and software setup on the left and the Hermes model-routing decision flow with DeepSeek and Claude pricing on the right
---

## TL;DR

- **Goal:** a small, silent, always-on machine that runs [Hermes Agent](https://hermes-agent.nousresearch.com/) ([GitHub](https://github.com/nousresearch/hermes-agent), [my review](/ai/hermes-agent/)), MCP servers, and automations independently of my laptop.
- **What I didn't need it to be:** a local inference workstation. I looked seriously at a Mac Studio and other machines capable of running 70B-class models, and talked myself out of it.
- **What I bought instead:** a **Mac mini M6, 24GB unified memory, 512GB SSD** (~£1,299) - enough headroom for containers, browsers, and small local models, not enough (or intended) to run frontier-class weights locally.
- **The routing policy:** small local model → [DeepSeek V4 Flash](https://api-docs.deepseek.com/quick_start/pricing) → DeepSeek V4 Pro → Claude Sonnet, cheapest capable model first.
- **The number that changed my mind:** DeepSeek's off-peak output pricing is cents per million tokens. A realistic monthly routing mix comes out under $10, which is a lot cheaper than the electricity and depreciation on a GPU rig.
- **The line I keep coming back to:** own the agent, rent the intelligence.

I've been experimenting with AI agents, coding assistants, and different models for a while now, but one problem kept coming up: my workflows were still tied to my laptop. Close the lid, and every agent, every scheduled job, every long-running task dies with it.

I wanted a small, silent computer that sits at home, runs 24/7, and acts as a permanent AI agent server - something that coordinates agents, executes tools, and intelligently routes hard work to the best cloud models, rather than trying to *be* the intelligence itself.

I'd been circling the idea of a proper local inference box for a while - the kind of machine that could run a genuinely large model at home. After actually pricing that route out, I landed somewhere much simpler:

> **Mac mini M6 (24GB) + Hermes Agent + DeepSeek V4 Flash/Pro + Claude Sonnet**

The interesting part isn't the shopping list. It's why I talked myself out of the bigger machine.

---

## What I Actually Needed

My main requirement wasn't local AI inference. It was **AI orchestration**.

I wanted a dedicated machine capable of continuously running:

- [Hermes Agent](/ai/hermes-agent/)
- Docker containers
- [MCP servers](https://modelcontextprotocol.io/)
- Python and Node.js
- Git repositories
- Playwright / browser automation
- PostgreSQL and Redis
- A vector database such as [Qdrant](https://qdrant.tech/)
- Scheduled jobs
- Tailscale and SSH for remote access
- Small local models where useful
- Multiple cloud AI providers

That machine becomes the **body** of the AI system. The cloud models provide most of the **intelligence**. That distinction changes the hardware requirements completely - and it's the thing I got wrong on my first pass at this.

---

## The Hardware

**Apple Mac mini M6**

- M6, 12-core CPU, 12-core GPU, 16-core Neural Engine
- **24GB unified memory**
- **512GB SSD**
- 2.5Gb Ethernet, Wi-Fi 7, Bluetooth 6
- macOS
- ~£1,299

The obvious question: why spend that much when an older, cheaper Mac mini would run Hermes just as well if all the inference happens in the cloud? That's a fair challenge, and an M1 or M2 mini with 16GB would genuinely be capable of it.

But this machine is meant to become permanent infrastructure, not another general-purpose computer I outgrow in a year. The extra memory buys headroom for containers, browser sessions, a vector database, and concurrent agent sessions - and unlike an external drive, it isn't upgradeable later. I'd rather have 24GB and not need it than hit a wall in two years and have to replace the whole box.

---

## Why I Didn't Build a Local Inference Machine

This was the actual conclusion of the research, and it's the opposite of where I started.

Running powerful models locally sounds attractive on paper: no API bills, complete privacy, no dependency on a provider. I looked hard at this - Mac Studio configurations, Ryzen AI Max mini PCs with huge unified memory pools, even GPU rigs capable of running 70B models at speed. I go into the local-inference sizing question properly in [Which Mac Studio Should You Buy for Running LLMs Locally?](/ai/mac-studio-local-llm-guide/) and [DGX Spark vs Mac Studio](/ai/dgx-spark-vs-mac-studio/) if you want the hardware-comparison version of this.

Small models are easy - an 8B model runs comfortably on almost anything modern. Once you go past 30B, though, memory bandwidth becomes the constraint, and getting to something like 100 tokens/second on a 30B-class model generally means serious GPU hardware: more cost, more electricity, more heat, more noise, more depreciation. And even after spending thousands, the result can still be meaningfully behind a frontier model available over an API.

That made me question the entire objective. I wasn't trying to build an AI agent server - I was trying to reproduce a slice of a datacentre in my house, for a worse result than just calling one.

### Specifically, why not a 64GB, 128GB or 256GB Mac Studio?

I went back and forth on this one longest, because a Mac Studio was the obvious "just buy enough memory and stop worrying about it" answer. The honest reason I didn't is cost, plainly: an M2/M3 Ultra with 64-128GB is somewhere around £3,000-£4,500, and a 256GB config (where you can still get one) pushes well past that. That's real money to spend on hardware whose main job would be sitting mostly idle, running inference I can currently get from DeepSeek for a few dollars a month.

I'm not against local frontier-class inference on principle - I just can't justify that outlay *right now* against what I'm actually getting for it. £3k+ buys a lot of DeepSeek and Claude API calls, and I'm genuinely fine with the privacy and latency trade-offs of calling cloud models for the hard reasoning, given the security and confirmation-gate layer I already run in front of anything an agent can do (see [Securing AI Agents](/ai/securing-ai-agents/)). If the economics were different - if I were running enough volume that the API bill rivalled the hardware cost, or if a 128GB machine were meaningfully cheaper - the answer might flip.

### The bet I'm making instead

I wrote about this properly in [The Day I Stop Chasing Better AI: When Frontier Models Come Home](/ai/frontier-models-come-home/): my guess is that somewhere around 2029-2031, the capability of *today's* frontier cloud models becomes cheap enough to run permanently on desktop-class hardware. When that happens, a local machine won't need to chase whatever the frontier is at that point - it just needs to match what Claude Sonnet or DeepSeek V4 Pro can already do today, which will look increasingly modest as hardware and smaller/smarter models both improve.

So the Mac mini isn't a rejection of local inference, it's a deferral. Right now, cheap cloud models make a big local-inference machine hard to justify. In a few years, I expect that trade to flip - at which point the sensible move is to buy the local hardware once it can match today's cloud frontier for a fraction of the cost, rather than buying it now while it's still catching up.

---

## Cloud AI Changes the Economics

The deciding factor was [DeepSeek's](https://www.deepseek.com/) API pricing. It makes genuinely capable inference remarkably cheap - cheap enough that I stopped thinking of "AI compute" as something I need to own outright, and started treating it more like a utility. Hermes can just pick the appropriate model for each task:

```text
Small local model
       ↓
DeepSeek V4 Flash
       ↓
DeepSeek V4 Pro
       ↓
Claude Sonnet
```

Each tier is progressively more capable and is only used when the tier below it isn't enough.

### Tier 1: local

Small models like Qwen 8B or Qwen 14B still run fine on the Mac mini - not to compete with Claude or DeepSeek Pro, but for classification, extraction, simple SQL, routing decisions, local RAG, and anything that should stay private or work offline. Cost per token here is £0, electricity aside.

### Tier 2: DeepSeek V4 Flash

This is the default cloud workhorse - where most everyday coding, reasoning, and agent work should land. Current pricing (per [DeepSeek's API pricing page](https://api-docs.deepseek.com/quick_start/pricing)):

| V4 Flash | Off-Peak | Peak |
|---|---:|---:|
| Cached input / 1M tokens | $0.007 | $0.014 |
| Uncached input / 1M tokens | $0.22 | $0.44 |
| Output / 1M tokens | **$0.66** | **$1.32** |

DeepSeek's peak window is 01:00-04:00 and 06:00-10:00 UTC, Monday to Friday; everything else is off-peak.

### Tier 3: DeepSeek V4 Pro

For harder reasoning and agentic work, roughly triple the Flash price:

| V4 Pro | Off-Peak | Peak |
|---|---:|---:|
| Cached input / 1M tokens | $0.022 | $0.044 |
| Uncached input / 1M tokens | $0.66 | $1.32 |
| Output / 1M tokens | **$1.98** | **$3.96** |

Three times a very small number is still a small number - a million output tokens off-peak on Pro is under $2.

### Tier 4: Claude Sonnet

I already pay for [Claude Pro](https://www.anthropic.com/pricing) at $20/month, so Sonnet becomes the final escalation - for when DeepSeek repeatedly struggles, a coding problem is genuinely hard, or I want a second opinion from a different model family. It doesn't need to process everything; it's another specialist Hermes can reach for.

---

## The Routing Policy

Rather than deciding manually which model handles a given request, Hermes makes that call:

```text
                    Incoming task
                          │
                          ▼
             Simple, repetitive, private,
                 or offline task?
                    │           │
                   YES          NO
                    │           │
                    ▼           ▼
             Local model   DeepSeek V4 Flash
                    │           │
                    └─────┬─────┘
                          ▼
                   Was it successful?
                    │           │
                   YES          NO
                    │           │
                    ▼           ▼
                  Finish   DeepSeek V4 Pro
                                │
                                ▼
                         Was it successful?
                          │           │
                         YES          NO
                          │           │
                          ▼           ▼
                        Finish   Claude Sonnet
```

The objective isn't to minimise cost for its own sake - it's to use the cheapest model that can reliably finish the task.

---

## What This Actually Costs

Say Hermes generates 10 million output tokens in a month, split roughly:

```text
80% DeepSeek Flash → 8M × $0.66  = $5.28
15% DeepSeek Pro   → 1.5M × $1.98 = $2.97
5% Local           → 0.5M         = $0.00
                                   --------
                          Total ≈ $8.25/month (output only)
```

Input costs are additional, and cached input is dramatically cheaper again. Even a pessimistic estimate leaves this well under the cost of a single additional SaaS subscription, let alone a GPU workstation. Electricity for the Mac mini itself is negligible next to running a GPU rig continuously - it's also silent, tiny, and low-heat, which matters more than benchmark numbers for a box that has to live under a desk permanently.

---

## Why Not Just Use My Laptop?

Because I want the agents to exist independently of it. My laptop should be a client, not the infrastructure. I want to be able to close it, leave the house, reboot it, or switch machines entirely without killing every scheduled job and running agent.

With [Tailscale](https://tailscale.com/) and SSH, I can reach the Mac mini remotely while it stays safely on my home network - the same pattern I've used before for [phoning a home agent](/ai/phone-your-home-ai-agent/) without opening a port on my router. Hermes keeps executing scheduled tasks and workflows regardless of what I'm doing with my laptop.

---

## The Final Architecture

```text
                        Internet
                           │
           ┌───────────────┼────────────────┐
           ▼               ▼                ▼
     DeepSeek Flash   DeepSeek Pro    Claude Sonnet
           ▲               ▲                ▲
           └───────────────┼────────────────┘
                           │
                    Hermes router
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          Local LLM     MCP servers    Agents
              │            │            │
              └────────────┼────────────┘
                           │
                     Mac mini M6
                     24GB / 512GB
                           │
        ┌──────────┬───────┼───────┬──────────┐
        ▼          ▼       ▼       ▼          ▼
      Docker    Browser   Git    Python     Databases
                 tools           Node
```

The Mac provides the persistent execution environment. Hermes provides the orchestration. DeepSeek and Claude provide the intelligence. Local models provide privacy, speed, and offline capability.

Here's the setup laid out as one infographic - hardware and software on the left, the Hermes routing decision flow and DeepSeek pricing on the right:

![Infographic showing the Mac mini M6 hardware and software setup on the left, and the Hermes model-routing decision flow with DeepSeek/Claude pricing tables on the right](/assets/images/ai/mac-mini-m6-hermes-agent-infographic.png)

This is a work in progress and subject to change as the build evolves - worth checking back on this post for updates rather than treating it as final.

---

## Why the M6 24GB Mac Mini, in the End

I looked at cheaper Mac minis, high-end Mac minis, Mac Studios, Intel and AMD Ryzen AI mini PCs with huge unified memory pools, and GPU rigs built to run 70B models at speed. I kept optimising the wrong variable.

I don't need to own the AI compute. I need to own the orchestration layer. Cloud AI is improving fast enough that spending several thousand pounds today to replicate it locally risks buying hardware that's outclassed before it's paid for itself. The Mac mini gives me plenty of headroom for the part I actually want to own - agents, tools, memory, databases, automation, browsers, code, MCP, workflows - while the inference layer stays swappable. Today that's DeepSeek V4 Flash → Pro → Claude Sonnet. If something better or cheaper shows up, I change a routing config, not the hardware.

**Own the agent, rent the intelligence.** My files, tools, databases, automation, and agent state stay under my control on hardware I own. When an agent needs serious reasoning power, it borrows infrastructure far bigger than anything I'd reasonably install at home, for a few dollars a month.

---

## Final Setup

- **Hardware:** Mac mini M6, 24GB unified memory, 512GB SSD, ~£1,299 one-off
- **Agent platform:** [Hermes Agent](https://hermes-agent.nousresearch.com/) by [Nous Research](https://www.nousresearch.com/), [open source on GitHub](https://github.com/nousresearch/hermes-agent)
- **Local AI:** Qwen 8B/14B and similar small models, where appropriate
- **Default cloud AI:** DeepSeek V4 Flash
- **Advanced reasoning:** DeepSeek V4 Pro
- **Frontier escalation:** Claude Sonnet (Claude Pro, $20/month, already paid for)
- **Additional DeepSeek spend:** realistically a few dollars a month under normal use

---

## Conclusion

I started this research expecting to end up buying a powerful local inference workstation. I ended up deciding almost the opposite: for an always-on agent server, the orchestrator doesn't need to be the intelligence. It needs to be reliable, quiet, efficient, and good at coordinating everything else - which is exactly what a small Mac mini is for.

Small jobs stay local. Most serious work goes to DeepSeek Flash. Hard problems escalate to DeepSeek Pro. Claude stays available when I want a different frontier model in the loop. Rather than spending thousands trying to bring a datacentre into my house, I've built a small, efficient gateway into whichever models happen to be best at the time - which feels like a considerably more future-proof way to run an always-on personal AI system.

This build is still evolving, so I'll keep this post updated as the setup changes.

## Related Reading

- [Hermes Agent: Persistent Autonomy That Learns and Grows](/ai/hermes-agent/)
- [Which Mac Studio Should You Buy for Running LLMs Locally?](/ai/mac-studio-local-llm-guide/)
- [DGX Spark vs Mac Studio: Which Personal AI Supercomputer Should You Buy?](/ai/dgx-spark-vs-mac-studio/)
- [Local AI vs Cloud AI in 2026](/ai/local-vs-cloud-ai-2026/)
- [The Day I Stop Chasing Better AI: When Frontier Models Come Home](/ai/frontier-models-come-home/)
