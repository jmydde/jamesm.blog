---
title: "How to Phone Your Home AI Agent Running on a Mac Studio"
date: 2026-04-21T21:48:00+01:00
draft: false
tags: ["ai", "mac-studio", "agent", "voice", "local-llm", "livekit", "twilio", "whisper"]
description: "A practical walkthrough of the stack I use to literally phone my Mac Studio, speak to a local AI agent, and get it to run or check work while I'm away from the desk."
cover:
  image: /assets/images/ai/phone-agent.jpg
  alt: Phone Your Home AI Agent Banner
---

## TL;DR

- **Goal:** Call a real phone number and have a proper back-and-forth with my Mac Studio agent while walking the dog.
- **Hardware:** Mac Studio (M2 Ultra, 128 GB) running a local model via Ollama or MLX.
- **Voice pipeline:** Twilio SIP in, [LiveKit Agents](https://docs.livekit.io/agents/) orchestrating STT / LLM / TTS, Whisper for transcription, Piper or ElevenLabs for speech.
- **Brain:** A local 30B-class model for chat plus tool calls, with Claude API as a fallback for the harder reasoning.
- **Reach:** [Tailscale](https://tailscale.com) between the Mac and a tiny VPS so I never punch a hole in my home router.
- **Outcome:** I can ring a UK landline number, ask "what's failing on the CI pipeline?" and get a spoken answer in ~2 seconds.

## Why bother phoning your own agent?

Typing is great at a desk. Outside the desk, it's hopeless. I wanted the simplest possible interface to the box sat under my desk at home - dial a number, talk, hang up. No app, no login, no VPN dance on my phone.

This isn't a gimmick. A voice line to a home agent unlocks three things you can't really get from ChatGPT on your phone:

1. **It knows your actual work** - it's pointed at your repos, your notes, your local services.
2. **It can do real things** - trigger a build, re-run a flaky test, stage a commit, check a dashboard.
3. **It's private by default** - the recording never leaves your kit unless you ask it to.

The rest of this post is the exact stack I landed on after a weekend of messing about. I've tried to be honest about the bits that are fiddly.

## The shape of the system

Before we go deep, here's the flow of a single call:

1. I dial a Twilio number from my mobile.
2. Twilio routes the call over SIP to a small cloud worker.
3. The worker hands the audio to [LiveKit Agents](https://docs.livekit.io/agents/) running as the voice orchestrator.
4. LiveKit streams the audio over Tailscale to the Mac Studio.
5. On the Mac - Whisper transcribes, the local LLM reasons and calls tools, Piper speaks the reply.
6. Audio streams back out the same way. Total round trip - roughly 1.5 to 2.5 seconds per turn.

Most of the cleverness is already in LiveKit's agent framework. You are not writing a real-time audio pipeline from scratch, which is the whole reason this is doable in a weekend.

## The Mac Studio side

I'm running the setup on an M2 Ultra 128 GB - more than most people need, but I already had it from the [local LLM experiments I wrote up previously](/ai/mac-studio-local-llm-guide/). An M2 Max 64 GB would be completely fine if you stay on a 13B class model.

The key services on the Mac are all run under `launchd` so they come back after reboots:

- **[Ollama](https://ollama.ai)** serving a 30B-class model on `localhost:11434`. I'm using a Qwen MoE for most calls and falling back to Claude Sonnet via the [Anthropic API](https://docs.anthropic.com) for anything that needs proper reasoning.
- **[whisper.cpp](https://github.com/ggerganov/whisper.cpp)** with the Metal backend, running a streaming server that takes audio chunks and returns partial transcripts. `large-v3-turbo` is my default - fast enough on Apple Silicon and very forgiving with UK accents.
- **[Piper TTS](https://github.com/rhasspy/piper)** for voice out. The `en_GB-alan-medium` voice is the best local option I've tried. If I'm feeling flush I swap in [ElevenLabs](https://elevenlabs.io) streaming TTS for a much nicer voice - but then the audio does leave the house.
- **A thin Python worker** that holds the tool-call plumbing - GitHub status, a read-only SSH into my dev box, a couple of bash shortcuts for "check the build" and "what's Claude saying about PR 42".

The Python worker is the only code I actually had to write. Everything else is off-the-shelf.

## The voice orchestrator

I spent an evening comparing [LiveKit Agents](https://docs.livekit.io/agents/), [pipecat](https://github.com/pipecat-ai/pipecat) and the [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime). For a local-first setup, LiveKit wins easily:

- Pluggable STT, LLM and TTS, each of which can point at a local endpoint. I plug Whisper in for STT, Ollama in for LLM, and Piper in for TTS - no cloud dependency required.
- Proper voice-activity detection and turn-taking out of the box. This is the part that makes it feel like a phone call rather than a radio handset.
- SIP ingress via [LiveKit SIP](https://docs.livekit.io/sip/) so a real phone call lands cleanly inside your agent session.

Pipecat is lovely but its SIP story is thinner. The OpenAI Realtime API is superb but it's a cloud model - which defeats the point for me.

## The phone number

For the actual PSTN side you need a SIP trunk. I'm using [Twilio Programmable Voice](https://www.twilio.com/docs/voice) because the SIP configuration is easy and I already have an account. A UK local number is about £1 a month plus pennies per minute.

The TwiML config is literally a single verb that dials the SIP URI exposed by LiveKit. Twilio handles the PSTN to SIP bridge. LiveKit handles the SIP to WebRTC bridge. Your agent just sees an audio track.

If you already use [Telnyx](https://telnyx.com) or [Vonage](https://www.vonage.com/communications-apis/voice/) the same pattern works - anything that can terminate a SIP URI is fine. I wouldn't use a consumer VoIP provider; the jitter is noticeably worse.

## Connecting the Mac to the world without opening ports

This is where most home setups go wrong. You do not want a public IP on your Mac Studio, and you do not want to mess with port forwarding on your home router.

I use [Tailscale](https://tailscale.com) with two nodes:

- The Mac Studio at home.
- A tiny £4/month VPS (hosted at [Hetzner](https://www.hetzner.com/cloud/)) that runs the LiveKit server and the SIP worker.

The VPS has a public address and handles the call from Twilio. LiveKit then reaches the Mac agent process over the Tailscale interface, not the open internet. Latency between the VPS and the Mac is about 15 ms on my connection - which is fine for conversational voice.

If you'd rather not run a VPS at all, LiveKit Cloud works the same way and the free tier covers my usage. I just prefer owning the box that holds the SIP credentials.

## The agent's tools

This is the bit that separates a chat toy from something actually useful. The agent has a small, boring toolbox:

- `github_status(repo)` - hits the GitHub API and summarises open PRs, failing checks, new issues.
- `check_ci(pipeline)` - reads the latest run from GitHub Actions and returns the current step.
- `run_shortcut(name)` - runs a macOS Shortcut on the Mac (brilliant for "start the dev server" or "open my daily note").
- `search_notes(query)` - greps my Obsidian vault.
- `ask_claude(prompt)` - escalates a hard reasoning task to Claude Sonnet via the API, with the local context stuffed in.

That last tool is the quiet star of the show. A local 30B model is great at conversation and orchestration - not always great at nuanced code reasoning. Letting it delegate to a smarter model when it needs to is the difference between "neat demo" and "thing I actually use".

All the tools are defined with [function calling](https://docs.anthropic.com/en/docs/tool-use) and exposed to the local model via Ollama's tool calling support.

## Making it feel like a phone call, not a radio

Getting the plumbing working is maybe 60% of the job. Making it feel conversational is the other 40%.

Things that matter:

- **Barge-in.** The user should be able to interrupt the agent mid-sentence. LiveKit's VAD handles this; make sure you enable it.
- **Short responses by default.** I prompt the model to reply in under three sentences unless I ask for detail. Nothing kills a voice interface faster than a six-paragraph monologue.
- **Confirmations for actions.** Anything destructive - pushing code, merging a PR, deleting anything - has to prompt back "are you sure?" and wait for a clear yes.
- **Filler audio.** When a tool call takes more than about 800 ms, the agent says something like "one sec, checking" to bridge the silence. Without this, people hang up thinking the line has dropped.

These are prompt-engineering problems, not infrastructure problems. The LiveKit agent's system prompt is where the personality lives.

## Costs

Rounded monthly numbers for my setup:

- Twilio number plus talk: ~£3-5
- VPS: ~£4
- Electricity for the Mac Studio: negligible on top of what it was already using (it idles most of the day)
- Local models: free
- ElevenLabs (when I use it): ~£4 for the starter tier

So about £10 a month, all in. Cheaper than another subscription, and it's mine.

## What I'd skip if I were starting again

- **Don't start with Piper.** Piper is genuinely good, but ElevenLabs is so much better that you'll lose a weekend chasing local TTS before you give up and pay. Prototype with ElevenLabs, then decide if local is worth it.
- **Don't build your own SIP bridge.** Just use Twilio plus LiveKit SIP. The RTP and codec nightmares are not a good use of your time.
- **Don't expose the agent to the raw internet.** Tailscale or WireGuard is a half-hour job and saves you a very bad afternoon.
- **Don't let the agent do destructive things without confirmation.** You're going to misspeak eventually.

## Is this the future?

It probably is, but in the specific sense that everyone's home will have a small agent they can talk to - not in the sense that they'll build this stack themselves.

The crazy thing is I now literally feel like I'm speaking to a real person - a real developer. Every day the agent is learning about my needs, my passions, who I am and what I'm trying to achieve. It's become a very personal assistant. It knows my repos better than I do some days. It understands the shortcuts and patterns I take. It's stopped feeling like I'm talking to a chatbot and started feeling like I'm talking to a colleague who happens to live in my Mac.

The interesting part of this project isn't the phone line. It's the realisation that a competent local model plus five or six tool calls is already enough to replace most of the reasons I open a laptop on the weekend.

If you want the bigger picture view on where local agents fit, I've written separately about [the local vs cloud AI trade-off in 2026](/ai/local-vs-cloud-ai-2026/) and [what actually belongs in my AI dev stack](/ai/what-actually-belongs-in-my-ai-dev-stack-2026/). This phone setup slots neatly into both.

## References

- [LiveKit Agents framework](https://docs.livekit.io/agents/) - the backbone of the voice pipeline
- [LiveKit SIP integration](https://docs.livekit.io/sip/) - how the phone audio gets in
- [Twilio Programmable Voice](https://www.twilio.com/docs/voice) - for the actual phone number
- [whisper.cpp](https://github.com/ggerganov/whisper.cpp) - local STT
- [Piper TTS](https://github.com/rhasspy/piper) - local TTS
- [Ollama](https://ollama.ai) - local LLM serving
- [Tailscale](https://tailscale.com) - the only sane way to reach a home box
- [Anthropic API docs](https://docs.anthropic.com) - for the Claude fallback tool
