---
title: "AI Roundup: October 2026"
date: 2026-10-31T18:00:00+00:00
draft: false
tags: ["ai", "news", "anthropic", "openai", "google", "gemini", "mistral", "model-release"]
description: "The biggest AI news of October 2026: Claude Haiku 5.5, Gemini 4 Argon rolling out, OpenAI's parallel agents and its Google Cloud deal, Mistral's one-trillion-parameter open-weights model, and Anthropic's IPO preparations."
cover:
  image: /assets/images/ai/ai-roundup-october-2026.jpg
  alt: "AI Roundup: October 2026 header image"
---

## TL;DR

- **Anthropic** released **Claude Haiku 5.5** on 7 October, its cheapest and fastest small model yet, and went into IPO preparation
- **Google** rolled **Gemini 4 Argon** out beyond its initial group of cyber defenders after announcing it on 30 September
- **OpenAI** added **parallel agents** to GPT-6 Pro in ChatGPT on 16 October, and on 21 October announced its models and Codex are coming to **Google Cloud**
- **Mistral** released the weights for **Mistral Large 4 ("Le Chonk")**, a roughly one-trillion-parameter open-weights model, at the end of the month

This roundup covers what major outlets and the companies themselves reported. Where sources disagree on a date or figure, I say so. Benchmark and pricing claims come from the companies unless noted.

## Claude Haiku 5.5 (7 October)

Anthropic released Claude Haiku 5.5 on 7 October, nine days after Claude Sonnet 5.5. According to [Decrypt](https://decrypt.co/380351/anthropic-launches-haiku-5-5-cheapest-fastest-claude-model) and [Anthropic's product page](https://anthropic.com/claude-haiku-5-5), the company calls it its cheapest, fastest and most capable small model.

- **Pricing:** $0.10 per million input tokens and $0.50 per million output tokens for prompts up to 100,000 tokens, against $1.00 and $5.00 for Haiku 4.5. One comparison lists higher rates above 100K tokens, which I could not confirm against Anthropic's own pricing page
- **A caveat on the saving:** Anthropic says the new tokenizer produces roughly 30% more tokens for the same text than Haiku 4.5, so the real-world saving is smaller than the headline per-token cut
- **Availability:** the Claude API, Amazon Bedrock, Google Cloud and Microsoft Foundry, among others

## Gemini 4 Argon Rolls Out

Google announced Gemini 4 Argon on 30 September. As [TheNextWeb reports](https://thenextweb.com/news/google-gemini-4-argon-cyber-defenders-fairwind), it went first to a group of trusted cyber defenders through Google's Fairwind program, with paid API customers and Google AI Ultra subscribers to follow. Google describes it as built for long-running work in software engineering, finance, legal and cybersecurity, and raised the output limit from 64 thousand to 1 million tokens.

Wider availability followed during October. Sources differ on exact dates and on introductory pricing, so check Google's own pages for current terms. The benchmark comparisons circulating online come from Google's announcement and have not been independently verified.

## OpenAI: Parallel Agents and Google Cloud

Two OpenAI announcements stood out.

**Parallel agents in GPT-6 Pro (16 October).** According to coverage such as [Mixed](https://mixed-news.com/en/chatgpt-gpt-6-pro-parallel-agents-faster-responses/), OpenAI announced that GPT-6 Pro in ChatGPT can split a task across several agents working at once. Users can follow progress in the conversation and open each completed task to inspect the agent's work. It is limited to eligible paid plans and is rolling out gradually. OpenAI has not said how many agents run together or how the split is decided.

**Models and Codex on Google Cloud (21 October).** OpenAI and Google Cloud announced that OpenAI's frontier models and its Codex agent workflows will be offered through Google Cloud's Model Garden and purchasable through Google Cloud Marketplace, with existing Google Cloud spending commitments applicable. [OpenAI's announcement](https://openai.com/id-ID/index/openai-models-google-cloud/) did not name specific models or give a general availability date, and reports differ on whether the first access is a private preview.

## Mistral Large 4 "Le Chonk" Goes Open-Weights

Mistral released the weights for Mistral Large 4, nicknamed "Le Chonk", on Hugging Face at the end of October, after a preview on its API. According to [AI Weekly](https://aiweekly.co/alerts/mistral-previews-1t-param-open-weight-large-4-le-chonk) and other coverage:

- It is a mixture-of-experts model of roughly one trillion parameters, with about 49 billion active per token
- It is released under the Mistral Ecosystem Open-Weight licence, a modified MIT licence that restricts some model-as-a-service uses
- Mistral emphasises coding and cybersecurity and says it matches the leading open-weight model on one index using 47% fewer tokens per task
- Independent testing was mixed: one outlet reports Artificial Analysis put it well behind OpenAI and Anthropic's flagship models, while ahead of the most capable US open-weights model

Reports differ on the exact release date and parameter count. Check Mistral's model card for the details.

## Anthropic Prepares to List

Anthropic told investors on 14 October that third-quarter revenue was $16.8 billion, according to Reuters as cited by secondary coverage, and moved its IPO preparations forward. The numbers were formalised in an amended filing on 2 November, which I cover in the [November roundup](/ai/ai-roundup-november-2026/). For what the filing means for people building on Claude, see [Anthropic's IPO: What the S-1 Says That Matters If You Build on Claude](/ai/anthropic-ipo-s-1-what-builders-should-read/).

## Related Reading

- [AI Roundup: September 2026](/ai/ai-roundup-september-2026/)
- [Anthropic's IPO: What the S-1 Says That Matters If You Build on Claude](/ai/anthropic-ipo-s-1-what-builders-should-read/)
- [The AI Model Price List, October 2026](/ai/ai-model-price-list-october-2026/)
- [The State of Open-Weight Models in 2026: Llama, Qwen, Mistral, DeepSeek](/ai/state-of-open-weight-models-2026/)

## Sources

- [Decrypt: Anthropic launches Haiku 5.5](https://decrypt.co/380351/anthropic-launches-haiku-5-5-cheapest-fastest-claude-model)
- [Anthropic: Claude Haiku 5.5](https://anthropic.com/claude-haiku-5-5)
- [TheNextWeb: Google unveils Gemini 4 Argon](https://thenextweb.com/news/google-gemini-4-argon-cyber-defenders-fairwind)
- [Mixed: GPT-6 Pro parallel agents in ChatGPT](https://mixed-news.com/en/chatgpt-gpt-6-pro-parallel-agents-faster-responses/)
- [OpenAI: OpenAI models on Google Cloud](https://openai.com/id-ID/index/openai-models-google-cloud/)
- [AI Weekly: Mistral previews 1T-parameter open-weight Large 4](https://aiweekly.co/alerts/mistral-previews-1t-param-open-weight-large-4-le-chonk)
