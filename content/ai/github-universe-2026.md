---
title: "GitHub Universe 2026: Agenda, Themes and What You Can Learn"
date: 2026-09-29T08:30:00+01:00
draft: false
tags: ["ai", "github", "agent", "agentic-engineering", "conference", "mcp", "open-source", "2026"]
description: "GitHub Universe 2026 runs 28-29 October at Fort Mason in San Francisco, and in person or virtual. Here is the published agenda, the 'agentic era' theme, the three session tracks, and what you can realistically learn from it."
---

## TL;DR

- **GitHub Universe 2026** runs **28-29 October** at Fort Mason Center in San Francisco, in person and virtual (the virtual pass is free)
- The theme is **"All together now, in the agentic era"**, and the site's tagline is that this is where "builders become orchestrators"
- Sessions sit under three tracks: **Find Your Flow**, **Find Your People** and **Build What's Next**
- The programme is heavy on Copilot, agents, MCP and open source, with a panel that includes people from Anthropic and OpenAI
- The full schedule is published, and a few sessions were still going through a community vote when GitHub announced it

## The basics

Per the [official Universe site](https://githubuniverse.com/), the event is on 28-29 October in San Francisco, with in-person and virtual attendance. The programme, as listed there:

- **27 October:** invitation-only programming
- **28 October:** opening keynote at 9 AM, breakout sessions from 10 AM to 5:30 PM, evening events
- **29 October:** sessions from 9 AM to 2 PM, closing keynote at 2 PM
- **30 October:** a learning day at GitHub HQ

Ticket prices and availability move, so check the site rather than trusting a blog post. When I looked, the site listed an in-person pass, a free virtual pass, a team package, paid workshops, and certification vouchers.

## The themes

### The headline: the agentic era

The framing on the site is that Universe unites "humans, agents, and the world's code". GitHub's own [schedule announcement](https://github.blog/news-insights/company-news/your-guide-to-github-universe-2026-is-here-the-schedule-just-launched/) was published on 13 August. The [coverage I found](https://www.startuphub.ai/ai-news/technology/2026/github-universe-enters-the-agentic-era) reads the theme as a shift from AI as autocomplete to AI as an autonomous collaborator. That is a secondary reading of the branding, not a GitHub quote, but the session titles below back it up.

### The three pillars

The site also splits the event into three pillars, written as code:

- `dev.experience()` - product launches and workflows
- `dev.learn()` - skills, through workshops
- `dev.connect()` - community and networking

### The three tracks

The published sessions are grouped into three tracks:

- **Find Your Flow** - working better day to day
- **Find Your People** - community, adoption and open source
- **Build What's Next** - where AI-assisted development is heading

The track descriptions are my paraphrase from the session titles. GitHub's post lists the sessions, not a definition of each track.

## The agenda: sessions GitHub has named

These are the sessions GitHub highlighted in its schedule announcement. It is a sample, not the full schedule.

### Find Your Flow

- **Stop prompting, start delegating: Configure Copilot to own the work** - Ken Muse and Mickey Gousset (GitHub)
- **Inside GitHub Copilot's coding harness: Optimizing across every model** - Julia Kasper (Microsoft)
- **Stop waiting on your own pull requests: GitHub stacked pull requests in practice** - Sameen Karim (GitHub)

### Find Your People

- **Building AI fluency at UPS** - Jared Hatfield (UPS)
- **Code is the easy part: Building Home Assistant in the open** - Franck Nijhof (Open Home Foundation)
- **I made my Octolamp think with GitHub Copilot CLI hooks** - Beatris Mendez Gandica (Nuevo Foundation)

### Build What's Next

- **The view from the labs: What's next for AI-assisted development** - a panel with Cara Phillips (Anthropic), Rohan Varma (OpenAI) and Kate Catlin (GitHub)
- **Open pull requests, don't merge them: Fine-grained authorization for hosted MCP servers** - Nick Taylor (Pomerium)
- **From writing code to managing agents: Scaling 50+ services at GitHub** - Anjuan Simmons (GitHub)

### Community-voted sessions

Three breakouts were competing for a main stage slot, with voting open until 21 August:

- **Why sketching in code matters more in the age of AI** - Qianqian Ye and John Maeda
- **Still open: How AI reshaped open source** - Angie Jones, David A. Wheeler and Priya Pahwa
- **The human side of AI: How building community drove 94% Copilot adoption** - Brittany Istenes

I have not checked which of these won. The vote closed weeks ago, so look at the live schedule before planning around them.

### Formats

GitHub's [schedule announcement](https://github.blog/news-insights/company-news/your-guide-to-github-universe-2026-is-here-the-schedule-just-launched/) also lists interactive workshops and hands-on technical sessions, **Ship & Tell** sessions showcasing projects people have built, partner booths and demos, and one-on-one conversations with GitHub team members.

## What you can learn

Reading the titles rather than the marketing, the practical takeaways cluster into four areas:

1. **Delegating to agents properly.** "Stop prompting, start delegating" and "From writing code to managing agents" are about configuring Copilot and running many services with agents, not typing better prompts. If you use Copilot, this is the most directly useful thread. I covered the basics in [my GitHub Copilot post](/ai/github-copilot/) and the spec-driven side in [GitHub Spec Kit](/ai/github-spec-kit/).
2. **Fixing the review bottleneck.** Stacked pull requests are aimed at the part of the workflow that agents make worse: more code, same number of reviewers.
3. **Securing agent access.** The MCP authorization session is about fine-grained permissions for hosted MCP servers. That matters as soon as an agent can touch anything real.
4. **Adoption and community.** The UPS and 94% Copilot adoption sessions are about how organisations get people to use these tools, which is usually a people problem rather than a tooling one. The Home Assistant and open source sessions cover how open projects cope with AI-assisted contribution.

## My read

This is my own opinion, not reporting. The interesting part of the agenda is what is *not* a launch. Several of the highlighted talks are about coping with agents: review queues, authorization, adoption, keeping open source healthy. The product announcements will land in the keynotes, and I would not guess at them before 28 October. If you can only watch a little, the free virtual pass plus the lab panel and the MCP authorization talk look like the best value.

## Sources

- [GitHub Universe 2026 - official site](https://githubuniverse.com/)
- [Your guide to GitHub Universe 2026 is here: The schedule just launched! - The GitHub Blog](https://github.blog/news-insights/company-news/your-guide-to-github-universe-2026-is-here-the-schedule-just-launched/)
- [GitHub Universe Enters the Agentic Era - StartupHub.ai](https://www.startuphub.ai/ai-news/technology/2026/github-universe-enters-the-agentic-era)

## Related Reading

- [GitHub Copilot](/ai/github-copilot/)
- [GitHub Spec Kit](/ai/github-spec-kit/)
