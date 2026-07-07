---
title: "AI Skills: One Folder, Any Model"
date: 2026-04-30T06:32:00+01:00
draft: false
tags: ["ai", "claude", "skill", "agent", "tool", "llm"]
description: "What Claude Code skills actually are under the hood, why the SKILL.md format is model-agnostic, and how the same folder can drive Claude, Gemini, Codex, and a dozen other agents without changes."
cover:
  image: /assets/images/ai/ai-skills.jpg
  alt: AI Skills banner
---

## TL;DR

- A **Claude Code skill** is just a folder with a `SKILL.md` file - YAML frontmatter plus natural-language instructions - and the same folder works across Cursor, Gemini CLI, Codex, and a dozen other tools
- The format is model-agnostic because it contains no provider-specific syntax; any instruction-following model can read it, and any harness that loads markdown can execute it
- **Progressive disclosure** keeps large skill libraries cheap: only names and descriptions load at session start, with full instructions loading only when a skill is activated
- The portability is practically valuable - version-controlled runbooks that survive tool switches, model upgrades, and team growth without being rewritten
- Core skills are genuinely portable; advanced frontmatter extensions (like `allowed-tools` or `context: fork`) are tool-specific and may need tuning across harnesses

Most of the tooling I have written about over the last year has been provider-specific. A particular model, a particular harness, a particular set of features. The thing I find interesting about [agent skills](https://agentskills.io) is that they are not.

A skill is a folder. Inside the folder is a `SKILL.md` file with some YAML frontmatter and some markdown instructions. That is the whole format. [Anthropic](https://www.anthropic.com/) shipped them in [Claude Code](https://code.claude.com/docs/en/skills), open-sourced the spec, and at this point you can drop the same folder into [Cursor](https://cursor.com/), the [Gemini CLI](https://geminicli.com/), [OpenAI Codex](https://developers.openai.com/codex), [OpenHands](https://openhands.dev/), [Goose](https://block.github.io/goose/), [VS Code](https://code.visualstudio.com/), [GitHub Copilot](https://github.com/), and a couple of dozen other tools, and they all do roughly the same thing with it.

That portability is the part I want to think about, because I do not think most teams have noticed yet how unusual it is.

## What a Skill Actually Is

Strip a skill back to its essentials and you get something almost embarrassingly simple. It is a directory with one required file, `SKILL.md`, that looks like this:

```yaml
---
name: commit
description: Stage and commit the current changes following our conventions
---

When committing changes:

1. Run `git status` to see what is staged
2. Group related changes into a single commit
3. Write a short subject line and a body that explains the why
4. Never commit secrets or credentials
```

That is the whole thing. The frontmatter has a name and a description. The body has natural-language instructions. The agent reads this when it decides the skill is relevant, or when you invoke it directly with `/commit`.

You can add more if you want. Supporting files for templates and reference docs. Scripts the agent can run. A frontmatter field that pre-approves certain tool calls. A flag that makes the skill run in an isolated sub-agent. A glob pattern that scopes it to certain file paths. But none of that is required, and the cheapest version of a skill is genuinely just a markdown file.

## Why the Format Is Model-Agnostic

Here is the thing that took me a while to internalise.

A skill does not contain anything model-specific. There is no Anthropic-flavoured syntax. No special tokens. No tool schemas you have to hand-write. The instructions are plain English. The file format is the same markdown frontmatter you see in [Hugo](https://gohugo.io/), [Jekyll](https://jekyllrb.com/), [Astro](https://astro.build/), and half of the static site generators on the planet.

That means the only things required to make a skill work are:

- A model that can follow instructions in natural language.
- A harness that knows how to load the file, decide when it is relevant, and inject it into the model's context.

The model is the easy part. Every frontier instruction-following model can read English and execute against it. The harness is the part that varies, and that is exactly where the tools differ. Cursor's loader is not Claude Code's loader. Gemini CLI's is different again. But because the input format is shared, the same skill works in all of them.

If you are used to thinking about this stack like an API contract, the analogy is useful. The model is the runtime. The harness is the OS. The skill is the program. The program does not need to know which OS or runtime it is targeting, as long as both speak the same format.

## Progressive Disclosure Is the Trick

The reason this works at scale, rather than collapsing under its own weight once you have fifty skills installed, is a pattern the spec calls progressive disclosure.

It works in three stages:

1. **Discovery.** At session start, the harness loads only the skill name and a short description. Cheap. Fits hundreds of skills in a few thousand tokens.
2. **Activation.** When the user's request matches a skill's description, either via the model's judgement or a direct `/skill-name` invocation, the harness loads the full `SKILL.md` body into context.
3. **Execution.** The model follows the instructions. If `SKILL.md` references supporting files - a template, a reference doc, a script - the model only loads them when actually needed.

This is the same idea behind lazy imports in a programming language, or content-on-demand in a CDN. You pay the cost when you use the thing, not when it sits on disk.

It is also why a `CLAUDE.md` full of long procedural playbooks is usually the wrong tool. `CLAUDE.md` content is loaded into every session, whether you need it or not. A skill loads when relevant. If a section of `CLAUDE.md` has grown into a procedure rather than a fact, it probably wants to be a skill. I have written before about the [token efficiency mindset](/ai/claude-token-efficiency-mindset/) this kind of trade-off forces, and skills are one of the cleanest expressions of it.

## What Portability Actually Buys You

Let me try to make this concrete with the kind of skill I would actually write.

Suppose I have a deployment playbook. Six steps, some sanity checks, a rollback path, a rule about never deploying on a Friday. Today this lives as institutional knowledge in three engineers' heads and one wiki page nobody updates.

If I write it as a skill:

- It is version-controlled in the repo at `.claude/skills/deploy/SKILL.md`.
- New engineers get it for free the moment they clone.
- Anyone using Claude Code, Cursor, or Codex on this codebase gets the same procedure, executed the same way.
- I can add `disable-model-invocation: true` so the agent never auto-deploys without me asking.
- If the procedure changes, I edit one file and everyone's tooling picks it up.

The portability piece is not theoretical. I do not have to pick a tool and commit to it forever. I do not have to rewrite the playbook when I switch models. I do not have to maintain three different versions for three different agents.

The same goes the other way. If a vendor ships a new model that is meaningfully better at something, I can swap to it without losing my skills library. The skills are decoupled from the runtime.

This is the kind of decoupling that, when it works, you barely notice. Like the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) for editors, or [Model Context Protocol](https://modelcontextprotocol.io/) for tool integrations. Boring, ubiquitous, and quietly load-bearing.

## Where the Generic Story Breaks Down

I do not want to over-sell this. There are real limits.

**Model capability varies.** A skill is just instructions. If the underlying model is bad at following multi-step instructions, the skill will be bad. A skill that works beautifully on a frontier model may produce mush on a smaller open-weights model running locally. The format is portable; the *quality* is not.

**Tool surfaces differ.** A skill that says "run `gh pr diff` and summarise it" assumes the harness has a Bash tool with `gh` available. Different harnesses expose different tools, with different permission models. The body of `SKILL.md` is portable in the abstract, but if your skill leans on tool calls, it leans on the harness's tool set.

**Frontmatter extensions diverge.** Claude Code supports fields like `context: fork`, `allowed-tools`, and `paths`. Other tools may ignore those, or implement them differently. The core spec is shared; the extensions are where each tool puts its own spin.

**Subagent and context semantics are not standardised.** "Run this in a fork" means subtly different things in different harnesses. So does "load these supporting files only when needed".

So the honest version of the pitch is: the *core* of a skill is genuinely portable. The *advanced* features are tool-specific and you should expect to tune them when moving between products. That is still a much better starting point than where we were a year ago, when every tool wanted you to author its own custom format from scratch.

## A Mental Model

If I had to compress this into a single picture, it would be:

- **A skill is a runbook.** Written for a smart, literate operator who has not seen this codebase before.
- **The model is the operator.** It reads the runbook and executes against it.
- **The harness is the building.** It decides which runbook to hand the operator, when to hand it over, and what tools the operator is allowed to use.

The only thing that has to be portable is the runbook. Different operators can be more or less skilled. Different buildings can have different toolboxes. But if the runbook is written clearly enough, the procedure survives the swap.

## Where I Would Start

If you have not written a skill yet, I would not start with anything ambitious. Pick something you have explained to your AI assistant more than three times. A commit convention. A test scaffold. A way you like to write migration scripts. The format your team uses for incident write-ups.

Make it a folder. Drop a `SKILL.md` in it. Three lines of frontmatter, twenty lines of instructions, save.

Notice that the next time you do that task, you do not have to re-explain anything. Notice that the same file works whether you opened the project in Claude Code or Cursor today. That is the part that is genuinely new. The rest is implementation detail.

I have written before about [how I think about Claude Code vs Cursor](/ai/claude-code-vs-cursor/) and the broader [AI tooling learning path](/ai/ai-tooling-learning-path/). Skills are the piece I would now slot in between the two. They are the artefact that survives the choice of tool, which is the closest thing this ecosystem currently has to a standard.

If the long arc of agentic tooling is heading toward something like the [agent-first architecture I sketched out previously](/ai/agent-first-architecture-engineer-as-curator/), then the parts of your stack that are model-agnostic are the parts most worth investing in. Skills happen to be one of them.

A folder of markdown is not a glamorous answer. But "boring, portable, and version-controlled" is a much stronger starting position than most of what came before it.

## Related Reading

- [The Token Efficiency Mindset - Why Your Claude Conversations Cost More Than They Should](/ai/claude-token-efficiency-mindset/)
- [Claude Code vs Cursor: A 6-Month Comparison](/ai/claude-code-vs-cursor/)
- [Claude Opus 4.7: Autonomy and Vision at Scale](/ai/claude-opus-4-7/)
- [An AI Tooling Learning Path: Logical Phases for 2026](/ai/ai-tooling-learning-path/)
