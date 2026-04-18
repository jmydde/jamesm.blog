---
title: "Hitting Claude Code Limits? Here’s the Setup I’m Moving Toward"
date: 2026-03-09T07:09:25+01:00
draft: false
tags: ['ai', 'claude', 'claude code']
---

I keep running into the same problem with Claude Code Pro (\$20/month): I burn through the usage limits faster than I expect. The obvious solution is upgrading to the \$200/month plan, but that feels excessive for how I actually use it.

So I started exploring alternatives.

What I've realised is that the best approach isn't replacing Claude Code entirely - it's building a hybrid AI developer stack where different models handle different types of work.

Think of it like a compute tiering strategy.

------------------------------------------------------------------------

## The Hybrid AI Stack

Instead of relying on a single frontier model, I'm moving towards something like this:

| Task | Model Type | Cost |
|---|---|---|
Quick edits, small scripts | Local model | Free |
General coding tasks | Cheap cloud models | Pennies |
Architecture / complex work | Claude / frontier models | Occasional |

In practice this means most requests never touch the expensive models.

------------------------------------------------------------------------

## Running Models Locally

For basic coding tasks, local models are already surprisingly capable.

Tools to run them:
-   Ollama
-   LM Studio

Then connect them to an IDE agent such as:
-   Continue.dev
-   Cline
-   Aider

Some good coding models:

| Model | Size | Notes |
|---|---|---|
DeepSeek Coder | 6B / 33B | Strong coding performance |
Qwen2.5 Coder | 7B / 32B | Good reasoning + tool use |
Codestral | ~22B | Solid refactoring |
Llama-3.1 | 8B | Fast and lightweight |

Example:

``` bash
brew install ollama
ollama run deepseek-coder:6.7b
```

Local models are great for:
-   writing functions
-   fixing bugs
-   editing files
-   explaining code
-   generating tests

They struggle more with large multi-file reasoning, which is where frontier models still shine.

------------------------------------------------------------------------

## Cheap Cloud Models

Instead of paying subscription pricing, you can also call open models via inference providers.

Some good ones:
-   Groq
-   Together AI
-   DeepInfra
-   Fireworks AI

Typical pricing is tiny:

| Model        | Approx Price                  |
|-------------|-------------------------------|
| Llama-3 70B | ~$0.20 / million tokens       |
| DeepSeek V3 | ~$0.30 / million tokens       |
| Qwen coder  | ~$0.10 / million tokens       |

For normal coding tasks this means pennies per session.

------------------------------------------------------------------------

## Free Coding Assistants

There are also tools offering free or semi-free coding models:

| Tool         | Notes                              |
|-------------|------------------------------------|
| Cursor      | small models + limited premium usage |
| Codeium     | unlimited completions               |
| Tabnine     | free tier available                 |
| JetBrains AI | local + quota models               |

Some allow plugging in your own local models, which removes limits entirely.

------------------------------------------------------------------------

## Using Claude Code Less (But More Strategically)

The key insight for me was this:

Frontier models like Claude are still the best for:
-   architecture decisions
-   large refactors
-   complex reasoning
-   multi-file edits

But they're overkill for everyday coding tasks.

So instead of using Claude for everything, it becomes the top tier tool in the stack.

------------------------------------------------------------------------

## The Setup I'm Experimenting With

Something roughly like this:

    VS Code
     ├─ Continue.dev
     ├─ Ollama (local models)
     │   ├─ qwen2.5-coder
     │   └─ deepseek-coder
     │
     └─ API fallback
         ├─ Groq
         └─ Claude Code

Usage ends up looking like:
-   80% local models
-   15% cheap APIs
-   5% frontier models

Which dramatically reduces usage limits.

------------------------------------------------------------------------

## Hardware Option

If you code constantly, running bigger models locally becomes viable.

Typical developer setups:

| Hardware                   | Cost          |
|----------------------------|---------------|
| Used RTX 3090 workstation  | ~$1.5–2k      |
| RTX 4090 workstation       | ~$3–4k        |

A 24GB GPU can run models in the 30B parameter range, which are good enough for most coding tasks.

------------------------------------------------------------------------

## What's Happening in the AI Coding Space

One thing is clear: coding models are rapidly commoditising.

Frontier models still lead in reasoning and agent reliability, but open models are already competitive for:
-   writing functions
-   generating boilerplate
-   fixing bugs
-   explaining code

The gap is shrinking fast.

------------------------------------------------------------------------

## My Takeaway

Instead of paying for bigger and bigger subscriptions, it makes more sense to build a layered AI workflow:
-   local models for everyday work
-   cheap cloud inference for heavier tasks
-   frontier models only when needed

You keep the power of Claude, but avoid hitting limits constantly.

And realistically, this is probably how most developer AI stacks will look going forward.
