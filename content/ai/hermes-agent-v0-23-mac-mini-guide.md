---
title: "Hermes Agent v0.23 on a Mac mini: Slack, Telegram, WhatsApp and a Kanban Board in Your Pocket"
date: 2026-11-13T12:00:00+00:00
draft: false
tags: ["ai", "agent", "hermes", "open-source", "mac-mini", "self-hosted", "automation", "ios"]
description: "What the latest Hermes Agent release (v0.23 'The Hearth') can do, how to run the gateway on a Mac mini under launchd, how to talk to it over Slack, Telegram and WhatsApp, and how to reach its Kanban board from an iPhone."
---

## TL;DR

- **Hermes Agent v0.23.0 "The Hearth"** shipped on 5 November 2026. The headline changes are a **Webapp** (your Desktop workspace in a browser tab, served by your own gateway), **one gateway that owns every conversation**, `/rewind`, **Group Chats** with automatic routing, and **spend limits** for paid MCP tools. A v0.23.1 patch followed on 9 November
- On a **Mac mini**, the gateway installs as a **launchd agent** with `hermes gateway install`, so it starts on login and keeps running
- You can talk to the same agent over **Slack, Telegram and WhatsApp** (plus Discord, Signal, Teams, Email and more) through that one gateway. Slack uses Socket Mode, so no public URL is needed
- Hermes has a built-in **Kanban board**, and there are **iPhone apps** that show it. They are **third-party apps, not official Nous Research apps**: Hermex is the one I looked at most closely
- The security defaults are sensible but the stakes are real. This is an agent with terminal access, so allowlists, approvals and isolation matter

I wrote about [what Hermes is and how it compares to its rivals](/ai/hermes-agent/) in April, and about [why I built a Mac mini M6 around it](/ai/mac-mini-m6-always-on-ai-agent-server/) in September. This is the practical update: what the current release can do, and how to make it useful from your phone.

## What Is New in v0.23 "The Hearth"

These come from the [official v0.23.0 release notes](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.0). The release rolls up roughly 1,950 merged PRs since v0.22.0.

**One gateway owns every conversation.** Previously the CLI, TUI, Desktop, editors, messaging bots and cron could each run their own copy of the agent against the same chat, which could write messages twice or lose them between surfaces. Now one gateway per machine owns each session and every surface attaches to it as a client. A chat you open anywhere is the same chat, with one queue and one history. For a Mac mini that you reach from a laptop, a phone and a chat app, this is the change that matters most.

**The Webapp.** The gateway can now serve the full Desktop workspace to a browser tab: the same chats, Group Chats, plugins and settings, from any browser on your network or behind a public URL with sign-in. It is **off by default**. Turn it on with `webapp.enabled` or Web Access in Settings.

**Rewind.** Press Esc twice or type `/rewind` in the TUI or classic CLI, pick an earlier message, then edit and resend it or fork a new session from that point. The original session stays as it was.

**Group Chats that run themselves.** In Bot Mode rooms, a lead bot or automatic router can choose who answers a message that names nobody. Scheduled jobs can post into a room, and loop guards stop bots pinging each other endlessly.

**Price tags and spend limits.** Paid MCP tools can declare what a call costs. The approval prompt shows each call's price and the chat's running total, and Hermes asks before a chat exceeds its limit, even in YOLO mode.

**Plugins.** The catalog grew from about 600 to over 1,050 entries, with a Verified tier for plugins built by the vendor, and `hermes plugins update` updates everything at once.

**Breaking changes to know about.** The old `browser_*` tools are replaced by `browser_exec`, Desktop now needs macOS 13+ (or 64-bit Windows), and `hermes mcp serve` is now the plugin command `hermes mcp-serve`.

The [v0.23.1 patch](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.1) fixed a plugin catalog size limit that had caused installs to silently fall back to an older catalog. The notes say full curated notes for the window since v0.23.0 will ship with v0.24.0, so expect more detail soon.

## Running It on a Mac mini

The Mac mini is a good fit: small, silent, low power, and always on. Hermes installs with the official one-liner on macOS, Linux and WSL2:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Then run it as a background service. Per the [messaging docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/):

```bash
hermes gateway install   # install as a launchd agent
hermes gateway start
hermes gateway status
tail -f ~/.hermes/logs/gateway.log
```

The launchd plist lives at `~/Library/LaunchAgents/ai.hermes.gateway.plist`. One gotcha from the docs: if you install new tools later, such as Node.js or ffmpeg, run `hermes gateway install` again so the plist picks up the updated `PATH`.

The gateway is a single background process that connects to every messaging platform you configure, handles sessions and runs cron jobs. Closing Desktop does not stop it, so routines and in-flight turns keep running. Stop it with `hermes gateway stop`.

To keep it current, `hermes update` updates the CLI, and the Docker image is `nousresearch/hermes-agent:stable` if you would rather run it in a container.

## Talking to It: Slack, Telegram and WhatsApp

One gateway, many front doors. Each platform needs an allowlist: by default the gateway **denies** anyone who is not on one or has not paired.

### Slack

Slack uses **Socket Mode**, which means it connects out over a WebSocket and needs **no public URL**, ideal for a box behind a home router.

1. Generate an app manifest with `hermes slack manifest --agent-view --write` and paste it at api.slack.com/apps (or create the app manually)
2. Enable Socket Mode and create an app-level token (`xapp-`, scope `connections:write`)
3. Install the app and copy the bot token (`xoxb-`)
4. Put `SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN` and `SLACK_ALLOWED_USERS` (your Slack member ID) in `~/.hermes/.env`
5. Run `hermes gateway`, then `/invite @Hermes Agent` in any channel you want it in

In DMs it answers every message. In channels it answers when mentioned and replies in a thread. Slack blocks slash commands inside threads, so use the `!` prefix there instead, such as `!stop`. `SLACK_HOME_CHANNEL` sets where cron output and proactive messages land.

### Telegram

The quickest route is the dashboard or desktop app: Messaging, then Telegram, then **Create with QR**. Hermes creates the bot, detects your user ID and writes `TELEGRAM_BOT_TOKEN` and `TELEGRAM_ALLOWED_USERS` for you. Manually, create a bot with @BotFather and set those two variables. Voice notes are transcribed by your chosen speech-to-text provider (local faster-whisper needs no key), and photos and files work too.

### WhatsApp

WhatsApp is the one to be careful with. There are two routes:

- **The built-in bridge** (`hermes whatsapp`) emulates a WhatsApp Web session: scan a QR code, set `WHATSAPP_ENABLED=true` and `WHATSAPP_MODE`, and start the gateway. It needs Node.js 20+
- **The WhatsApp Business Cloud API**, the official route, which the docs recommend for a stable business bot

The docs are blunt about the bridge: WhatsApp "does **not** officially support third-party bots outside the Business API", and using a bridge "carries a small risk of account restrictions." Their advice is to use a **separate number** for the bot rather than your personal one, and to keep the saved session directory private, because it grants full access to the account. Set `WHATSAPP_ALLOWED_USERS` too.

## The Kanban Board

Hermes has a built-in Kanban board, a durable task board shared across all your Hermes profiles. According to the [Kanban docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban):

- Tasks have a title, an assignee (a profile name) and a status: `triage`, `todo`, `ready`, `running`, `blocked`, `review`, `done` or `archived`
- Tasks can depend on each other: a child moves to `ready` when its parents are `done`
- A **dispatcher** runs inside the gateway, spawns a worker for each assigned profile and reclaims stale tasks
- Workers can use a scratch directory, a git **worktree** for coding tasks, or an existing directory
- You drive it with `hermes kanban`, the `/kanban` command in chat (including Slack and Telegram), or the dashboard

A minimal run looks like this:

```bash
hermes kanban init
hermes gateway start
hermes kanban create "research AI funding landscape" --assignee researcher
hermes kanban watch
```

Assignee names must match real profiles, so create the profiles first. For the web view, run `hermes dashboard` and a Kanban tab appears with status columns and drag and drop.

## Kanban on an iPhone

There is no official Nous Research iPhone app that I could find. What exists are **independent apps** from third-party developers that connect to a Hermes server you run yourself:

- **[Hermex](https://hermexapp.com/)** is a free, MIT-licensed native SwiftUI app. Its [GitHub page](https://github.com/uzairansaruzi/hermex) lists chat, sessions, files and Git, tasks, skills, memory, push notifications, Live Activities and **Kanban boards with live updates**. It needs iOS 18 and Hermes Agent 0.21.3 or later, and says it is not affiliated with Nous Research
- Others include [Hermes Conduit](https://hermesconduit.app/), [Herald](https://heraldapp.dev/) and [ScarfGo](https://github.com/awizemann/scarf), each of which also lists Hermes Kanban support. I have only looked at their listings, so check each before installing

All of them need your Hermes server to be **reachable from your phone**. Hermex connects to the dashboard (`hermes dashboard`, which listens on `127.0.0.1:9119` by default), signs in with a username and password, and recommends **Tailscale Serve** to expose it privately. That fits a Mac mini that is already on a tailnet. Its README warns that plain same-Wi-Fi access with `--host 0.0.0.0` sends the password unencrypted.

Agent execution still happens on the Mac mini. The phone is only a window onto it.

## What I Would Use It For

These are suggestions, not benchmarks:

- **A morning briefing** delivered to Slack or Telegram by a cron routine, using Hermes's natural-language scheduling
- **A research queue** on the Kanban board: drop tasks in from your phone, let a `researcher` profile work through them, and review the results when you are back at the desk
- **Voice notes to action.** Send a Telegram voice note, have it transcribed, and let the agent act on it
- **A small team of bots.** With Bot Mode, give each profile a role, model and memory, and let a router decide who answers in a group chat
- **Coding handoffs.** Kanban worktree workspaces suit tasks that hand work to a coding agent, as in [my Mac mini setup](/ai/mac-mini-m6-always-on-ai-agent-server/)

## Keep It Safe

This is the part not to skip. Hermes can run terminal commands on your machine, and you are putting a chat interface in front of it. The [security docs](https://hermes-agent.nousresearch.com/docs/user-guide/security) recommend, for an always-on gateway:

1. Set explicit allowlists, and leave `GATEWAY_ALLOW_ALL_USERS` unset
2. Use `terminal.backend: docker` (or `ssh` to a separate host) so commands run isolated from the gateway
3. Set container CPU, memory and disk limits
4. Keep `~/.hermes/.env` private with `chmod 600`
5. Run the gateway as a non-root user and run `hermes update` regularly

Approvals default to `smart` mode, where an auxiliary model auto-approves low-risk commands and denies dangerous ones, and headless contexts such as cron default to **deny**. YOLO mode bypasses prompts but not the hardline blocklist or the MCP spend limits. Also note the docs' own caveat: the file-write denylist is "defense-in-depth, not a hard boundary", so the container backends are the real isolation.

And the Webapp is off by default for a reason. If you turn it on, put it behind Tailscale or proper sign-in rather than the open internet.

## Where It Stands

Hermes is moving fast: the v0.23.0 notes alone cover roughly 1,950 merged PRs. That is exciting and a little tiring, because docs and third-party apps can lag the releases, and the breaking changes above are a reminder to read release notes before updating a box you rely on.

For a Mac mini owner, the appeal is clear. One always-on agent, reachable from Slack, Telegram or WhatsApp, with a Kanban board you can check from your phone, all running on hardware you own.

## Related Reading

- [Hermes Agent: Persistent Autonomy That Learns and Grows](/ai/hermes-agent/)
- [Own the Agent, Rent the Intelligence: Building My Always-On AI Agent Server](/ai/mac-mini-m6-always-on-ai-agent-server/)
- [How to Phone Your Home AI Agent Running on a Mac mini M6](/ai/phone-your-home-ai-agent/)
- [Giving Your Home AI Agent Real Tools: MCP Servers on a Mac mini M6](/ai/mcp-servers-home-ai-agent/)
- [Giving Your Home AI Agent Memory That Lasts](/ai/home-ai-agent-memory-that-lasts/)

## Sources

- [Hermes Agent v0.23.0 release notes (GitHub)](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.0)
- [Hermes Agent v0.23.1 release notes (GitHub)](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.1)
- [NousResearch/hermes-agent (GitHub)](https://github.com/NousResearch/hermes-agent)
- [Hermes docs: messaging gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
- [Hermes docs: Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)
- [Hermes docs: security](https://hermes-agent.nousresearch.com/docs/user-guide/security)
- [Hermex (GitHub)](https://github.com/uzairansaruzi/hermex)
- [Hermex (App Store)](https://apps.apple.com/us/app/hermes-agent-mobile/id6767006319)
