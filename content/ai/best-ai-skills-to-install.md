---
title: "The Best AI Skills to Install (and the Ones I'd Skip)"
date: 2026-11-13T09:00:00+00:00
draft: false
tags: ["ai", "claude", "claude-code", "skill", "agent", "tool"]
description: "A short, opinionated guide to the agent skills actually worth installing: Anthropic's document skills, skill-creator, frontend-design, webapp-testing, the Superpowers workflow, and where to find more without drowning in listicles."
---

## TL;DR

- Start with Anthropic's official skills repo. The four **document skills** (`pdf`, `docx`, `xlsx`, `pptx`) and **skill-creator** are the highest-value installs for most people
- For developers, add **frontend-design**, **webapp-testing**, **mcp-builder** and **claude-api**. They are narrow, so they only cost you context when the task matches
- **Superpowers** is the most ambitious community pick: a whole development workflow (spec, plan, test-first, sub-agent review) packaged as skills
- Install fewer than you think you need. Every skill's description sits in context all the time, so a bloated library makes triggering worse, not better
- Treat any third-party skill like code you are about to run, because it is

I wrote about [what skills are and why the format is portable](/ai/ai-skills-one-folder-any-model/) back in April. This is the practical follow-up people keep asking me for: which ones are actually worth installing.

A caveat up front. "Best" here is my judgement, based on what the skills claim to do in their own files and how well they fit common work. I have not benchmarked them against each other, and the star counts below are a snapshot from 13 November 2026.

## Start With the Official Repo

[anthropics/skills](https://github.com/anthropics/skills) is the obvious first stop. At the time of writing it holds 19 skills, and the repo has well over 100,000 stars on GitHub. The README is upfront that the skills are for demonstration and educational purposes, and that behaviour in Claude may differ from what the examples show, so test before relying on them for anything critical.

In Claude Code, installing is three commands:

```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

You can then ask for a skill by name, for example "use the PDF skill to extract the form fields from this file". On Claude.ai the example skills are available on paid plans, and skills can also be used through the API.

## The Ones I Would Install First

### The document skills: pdf, docx, xlsx, pptx

These are the most practical skills in the repo, because they solve a boring, universal problem: getting a model to reliably read and produce real Office and PDF files. Their descriptions are broad on purpose. The PDF skill covers extracting text and tables, merging and splitting, filling forms, watermarks, encryption and OCR. The spreadsheet skill covers editing and fixing `.xlsx` and `.csv` files, formulas, formatting and charts. The Word and PowerPoint skills cover creating, editing and extracting content from `.docx` and `.pptx` files.

If you only ever install one bundle, make it this one.

### skill-creator

This one is a skill for making skills. By its own description it creates new skills, improves existing ones, runs evals to test them, and tunes a skill's description so it triggers more accurately.

That last part matters more than it sounds. A skill that never fires is worse than no skill, and the description is what decides whether it fires. If you plan to write your own, which I think you should, this is the one to have on hand.

## The Ones I Would Add If You Write Code

### frontend-design

Aimed at the "everything looks like the same template" problem. Its description promises guidance on aesthetic direction and typography, and on making choices that do not read as templated defaults. Useful if you let a model build UI and are tired of the sameness.

### webapp-testing

A toolkit for testing local web apps with Playwright: checking frontend behaviour, debugging UI, capturing screenshots and reading browser logs. It earns its place because it lets the model verify its own work instead of declaring victory.

### mcp-builder

A guide for building good MCP servers, in Python (FastMCP) or Node/TypeScript, so that models interact with external services through well-designed tools. If you are wiring an agent to your own APIs, as in my [home agent setups](/ai/mcp-servers-home-ai-agent/), the real risk is badly designed tools, and this skill targets exactly that.

### claude-api

A reference for the Claude API and SDK: model IDs, parameters, streaming, tool use, caching and migrating between models. It is the antidote to a model confidently quoting an outdated model name or price from memory.

### doc-coauthoring

A structured workflow for writing specs, proposals and decision docs: gather context, refine the structure, then test the draft against a reader. It is a process skill rather than a tool skill, and I like it for that reason.

## The Community Pick: Superpowers

[obra/superpowers](https://github.com/obra/superpowers) is the most popular non-Anthropic skills project I looked at, with a very large GitHub following and an MIT licence. It is less a skill than a methodology delivered as skills.

As the README describes it, the agent does not jump straight into code. It asks what you are really trying to do, draws out a spec and shows it in digestible chunks, then writes an implementation plan. It then runs a sub-agent-driven process that works through each task and reviews the result, with an emphasis on red/green test-driven development and avoiding unnecessary features. The skills trigger automatically, so there is little to remember.

It installs from Anthropic's official plugin marketplace in Claude Code (`/plugin install superpowers@claude-plugins-official`), and the README lists support for many other harnesses, including Cursor, Codex CLI, Gemini CLI and [Hermes Agent](/ai/hermes-agent/).

My take: it is opinionated, and opinionated tools suit some people and grate on others. If you already have a workflow you like, it may fight you. If you do not, it is a strong default.

## Where to Find More

- [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) is an MIT-licensed collection for conversion optimisation, copywriting, SEO, analytics and growth work. Good if marketing is part of your job
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) is a curated list of skills, resources and tools. It is a directory rather than a product, and it has not been updated since September, so expect some drift

## How Many Is Too Many

Skills load progressively: only names and descriptions are present at the start of a session, with the full instructions loaded when a skill is activated. That makes a library cheap, but not free. Every extra description is another thing the model has to choose between, and overlapping descriptions cause the wrong skill to fire.

My rule of thumb is to install a skill only when you can name the last time you needed it. Start with the document skills and skill-creator, add the developer skills when a project calls for them, and write your own for anything you have explained to an assistant more than three times.

## Security: Read Before You Install

A skill is instructions plus, often, scripts your agent will run with your permissions. Before installing anything from outside a source you trust, open the `SKILL.md` and any bundled scripts and read them. Check the licence too. The official repo notes that licences vary by skill folder, so look at each one before reusing it. A star count tells you something about popularity and nothing about safety.

## Related Reading

- [AI Skills: One Folder, Any Model](/ai/ai-skills-one-folder-any-model/)
- [Hermes Agent: Persistent Autonomy That Learns and Grows](/ai/hermes-agent/)
- [An AI Tooling Learning Path: Logical Phases for 2026](/ai/ai-tooling-learning-path/)
- [Claude Code vs Cursor: A 6-Month Comparison](/ai/claude-code-vs-cursor/)

## Sources

- [anthropics/skills (GitHub)](https://github.com/anthropics/skills)
- [obra/superpowers (GitHub)](https://github.com/obra/superpowers)
- [coreyhaines31/marketingskills (GitHub)](https://github.com/coreyhaines31/marketingskills)
- [ComposioHQ/awesome-claude-skills (GitHub)](https://github.com/ComposioHQ/awesome-claude-skills)
