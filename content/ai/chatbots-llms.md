---
title: "Chatbots & Large Language Models (LLMs)"
date: 2024-05-17T17:06:25+01:00
draft: false
tags: ["ai",-"llm",-"chatbot",-"gpt",-"claude",-"gemini",-"llama"]
description: "A practical explainer on the difference between chatbots and large language models, how modern model families fit together, and how to choose the right AI tool for a task."
---

Most people still talk about chatbots and large language models as if they are the same thing.

They are related, but they are not identical.

A chatbot is the product experience. A large language model is the reasoning engine underneath. Once you separate those two layers, the AI landscape becomes much easier to understand.

## Quick Answer

If you only want the short version:

- an **LLM** is the underlying model
- a **chatbot** is the product wrapped around that model
- the best choice depends on the task, the interface, and the context you need

## Chatbot vs LLM At A Glance

| Question | LLM | Chatbot |
|:---|:---|:---|
| What is it? | The model itself | The user-facing product |
| Main job | Generate and transform language and other modalities | Make the model usable in a workflow |
| Typical interface | API, SDK, model endpoint | Chat UI, app, assistant product |
| Common extras | None by default | memory, files, search, tools, voice |
| Best for | automation, integration, custom systems | everyday use, exploration, fast collaboration |

## The Simple Distinction

A **large language model (LLM)** is a model trained to predict and generate language. In practice, modern LLMs can also handle code, structured data, reasoning tasks, and increasingly multimodal inputs such as images, audio, and video.

A **chatbot** is the interface built on top of that model:

- a chat window
- memory or conversation history
- file uploads
- tool use
- web search
- voice mode
- product-specific workflows

The model is the engine.
The chatbot is the vehicle.

That distinction matters because two chatbots can feel very different while using similarly capable models, and one model can appear in multiple products with different strengths.

## What LLMs Actually Do

Modern LLMs are useful because they compress a huge amount of language and pattern knowledge into something you can query interactively.

They are especially good at:

- summarizing information
- rewriting text
- explaining unfamiliar concepts
- generating first drafts
- translating between formats
- writing and refactoring code
- helping think through tradeoffs

They are much less reliable when you treat them like perfectly grounded systems with guaranteed facts. They can sound certain while being wrong, outdated, or overly smooth.

That is why the best way to use an LLM is not as an oracle, but as a fast collaborator whose output still needs judgment and verification.

## The Main Model Families

The market changes fast, but the categories are more stable than the individual releases.

### Frontier general-purpose models

These are the models most people think of first:

- [OpenAI GPT](https://openai.com/) models
- [Anthropic Claude](https://www.anthropic.com/) models
- [Google Gemini](https://gemini.google.com/) models

They tend to be strongest at broad reasoning, writing, coding help, and multimodal tasks. They are usually the best choice when quality matters more than absolute cost.

### Open-weight and self-hostable models

This category includes model families such as [Llama](https://www.meta.com/llama/) and other open or partially open ecosystems.

These matter because they give developers more control over:

- cost
- privacy
- deployment
- customization
- local or self-hosted workflows

They are often a better fit for experimentation, internal tooling, high-volume workloads, or teams that want more control over where inference happens.

### Product-specific assistants

Some tools matter less because of the underlying model and more because of how they are packaged:

- [ChatGPT](https://chatgpt.com/)
- [Claude](https://claude.ai/)
- [Gemini](https://gemini.google.com/)
- [Perplexity](https://www.perplexity.ai/)
- [Notion AI](https://www.notion.so/product/ai)
- [GitHub Copilot](https://github.com/features/copilot)
- [Cursor](https://www.cursor.com/)

These are not just models. They are workflows.

Their value often comes from the surrounding product decisions:

- how they search
- how they use files
- how well they fit into coding or writing
- how they present sources
- how much friction they remove

## How I Think About Choosing the Right Tool

A useful rule of thumb is to choose based on the job, not the brand.

### A simple decision rule

- if you want **conversation and convenience**, start with a chatbot
- if you want **control and automation**, start with an API or model endpoint
- if you want **repo-aware coding help**, start with a coding-native AI tool

### Use a chatbot when you want:

- quick exploration
- brainstorming
- summarization
- lightweight Q&A
- an accessible interface for everyday work

### Use an API or model endpoint when you want:

- automation
- repeatable workflows
- product integration
- routing between models
- control over prompting and infrastructure

### Use a coding-native AI tool when you want:

- repo context
- multi-file edits
- code review support
- terminal or editor integration

The mistake people make is trying to force one interface to solve every problem.

## What Actually Matters in Practice

When comparing LLMs or chatbot products, I think these questions matter more than leaderboard obsession:

- Is it fast enough to stay in my workflow?
- Does it have access to the right context?
- Can I trust it to show uncertainty when it should?
- Is it affordable for the kind of usage I actually have?
- Does it fit the job: writing, coding, research, or planning?

The best model on paper is not always the best tool in practice.

Sometimes a cheaper, faster model with the right interface beats a more powerful model wrapped in a clumsy workflow.

## The Bigger Shift

The reason this category matters so much is that chatbots are turning LLMs into consumer products, while APIs are turning them into infrastructure.

That means we are living through two changes at once:

- AI as a product experience
- AI as a programmable utility

If you understand both layers, the market stops looking chaotic.

You can see the pattern more clearly:

- chatbots make intelligence easy to access
- models make intelligence cheap to produce
- workflows determine whether that intelligence is actually useful

## My Take

The important question is no longer "which chatbot is best?"

The better question is:

**Which combination of model, interface, and workflow is best for this specific task?**

That is a much more useful way to think about AI than treating the whole space like a horse race.

---

**Related reading:**
- [What Actually Belongs in My AI Dev Stack in 2026](/ai/what-actually-belongs-in-my-ai-dev-stack-2026)  -  How I think about combining different AI tools into one workflow
- [We Are Learning to Buy Intelligence](/ai/we-are-learning-to-buy-intelligence)  -  Why intelligence itself is starting to behave like infrastructure
- [AI Explainers](/ai/explainers)  -  Foundational resources for understanding how the underlying systems work
