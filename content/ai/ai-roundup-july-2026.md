---
title: "AI Roundup: July 2026"
date: 2026-07-31T18:00:00+01:00
draft: false
tags: ["ai", "news", "anthropic", "claude", "open-source", "infrastructure", "model-release"]
description: "The biggest AI news of July 2026: Moonshot's 2.8 trillion parameter Kimi K3 goes open-weight, Claude Opus 5 launches, and AMD commits up to $5 billion to Anthropic."
cover:
  image: /assets/images/ai/ai-roundup-july-2026.jpg
  alt: "AI Roundup: July 2026 header image"
---

## TL;DR

- **Moonshot AI** released **Kimi K3**, a 2.8 trillion parameter model, via API in mid-July and as open weights around 27 July
- **Anthropic** released **Claude Opus 5** on 24 July at an unchanged price
- **AMD** agreed to invest up to **$5 billion in Anthropic** and supply 2 gigawatts of Instinct GPUs

Benchmark claims below come from the companies and have not been independently verified.

## Kimi K3 (16 to 27 July)

Moonshot AI launched Kimi K3 through its API on 16 to 17 July and released the weights about eleven days later. According to [The Decoder](https://the-decoder.com/moonshot-ai-releases-kimi-k3-open-weights-and-infrastructure-after-shaking-up-the-frontier-model-race/) and [AI Weekly](https://aiweekly.co/alerts/moonshot-releases-kimi-k3-largest-open-weight-model-to-date):

- It is a mixture-of-experts model with 2.8 trillion total parameters and 104 billion active per token, described as the largest open-weight model to date
- Weights and a technical report were posted to Hugging Face and GitHub, with a context window of roughly one million tokens
- Sources disagree on the licence terms, with one describing a revenue-tiered Kimi K3 licence. Check the model card before building on it
- Running it is demanding. Open weights do not mean low barriers to self-hosting

## Claude Opus 5 (24 July)

Anthropic released Claude Opus 5. [Axios](https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5) and [VentureBeat](https://venturebeat.com/orchestration/anthropic-launches-claude-opus-5-a-cheaper-ai-model-for-coding-agents-and-enterprise-workflows) report:

- Pricing is unchanged from Opus 4.8 at $5 per million input tokens and $25 per million output tokens, with a Fast mode at twice the base rate
- Anthropic says it approaches the capability of Fable 5 on many tasks at lower cost, and calls it its safest model yet. These are company claims
- It became the default model on Claude Max and is available through the API as `claude-opus-5`
- It was Anthropic's fourth Claude 5 release in under two months

## AMD Commits to Anthropic (about 22 July)

AMD said it would invest up to $5 billion in Anthropic, tied to deployment milestones. As [Bloomberg](https://news.bgov.com/artificial-intelligence/amd-to-invest-up-to-5-billion-in-anthropic-deploy-chips) and [Implicator](https://www.implicator.ai/amd-commits-up-to-5-billion-to-anthropic-in-2-gigawatt-chip-deal/) reported, citing CNBC for several details:

- Anthropic will deploy 2 gigawatts of AMD Instinct MI450 GPUs in Helios rack-scale systems, with the first gigawatt beginning in the first half of 2027
- It makes AMD both a supplier and a shareholder of its customer, in contrast with its warrant arrangement with OpenAI
- Sources differ on the exact day of the announcement

## Related Reading

- [AI Roundup: June 2026](/ai/ai-roundup-june-2026/)
- [AI Roundup: August 2026](/ai/ai-roundup-august-2026/)
- [The State of Open-Weight Models in 2026: Llama, Qwen, Mistral, DeepSeek](/ai/state-of-open-weight-models-2026/)

## Sources

- [The Decoder: Moonshot AI releases Kimi K3 open weights](https://the-decoder.com/moonshot-ai-releases-kimi-k3-open-weights-and-infrastructure-after-shaking-up-the-frontier-model-race/)
- [AI Weekly: Moonshot releases Kimi K3](https://aiweekly.co/alerts/moonshot-releases-kimi-k3-largest-open-weight-model-to-date)
- [Axios: Anthropic releases Opus 5](https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5)
- [VentureBeat: Anthropic launches Claude Opus 5](https://venturebeat.com/orchestration/anthropic-launches-claude-opus-5-a-cheaper-ai-model-for-coding-agents-and-enterprise-workflows)
- [Bloomberg: AMD to invest up to $5 billion in Anthropic](https://news.bgov.com/artificial-intelligence/amd-to-invest-up-to-5-billion-in-anthropic-deploy-chips)
- [Implicator: AMD commits up to $5 billion to Anthropic](https://www.implicator.ai/amd-commits-up-to-5-billion-to-anthropic-in-2-gigawatt-chip-deal/)
