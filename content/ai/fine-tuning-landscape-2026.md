---
title: "The Fine-Tuning Landscape in 2026: LoRA, Full FT, and Distillation"
date: 2026-05-14T05:00:00+01:00
draft: true
tags: ["ai", "fine-tuning", "model", "training"]
description: "Fine-tuning has matured into a discipline with real choices: LoRA for adaptation, full fine-tuning for capability, distillation for cost. A practical look at which method to pick for which job, and what has actually changed in 2026."
cover:
  image: /assets/images/ai/fine-tuning-landscape-2026.jpg
  alt: The Fine-Tuning Landscape in 2026 Banner
---

Two years ago, "fine-tuning" was essentially one thing: take a base model, train it on your data, and end up with a model that knows your domain. The decision was mostly about whether to do it at all. In 2026, the choice is more interesting. There are now four distinct techniques - LoRA, full fine-tuning, distillation, and continued pre-training - with meaningfully different costs, trade-offs, and appropriate use cases. Picking the wrong one is an expensive mistake. Knowing which to reach for has become a real engineering decision, not an afterthought.

## TL;DR

- **LoRA** is the default for adapting a model's behaviour at low cost and low complexity.
- **Full fine-tuning** is the right call when you need real capability changes, not just style.
- **Distillation** is the right call when you have a big model that works and want a smaller, cheaper one with similar behaviour.
- **Continued pre-training** is the right call when you have a substantial domain-specific corpus the base model has not seen.
- **In 2026** all four are routine production techniques, not exotic research methods.

## LoRA and its variants

[LoRA - low-rank adaptation](https://arxiv.org/abs/2106.09685) - trains a small set of additional parameters that adjust the base model's behaviour without modifying the base weights. The original paper froze the pre-trained weights and injected trainable rank-decomposition matrices into each transformer layer, cutting trainable parameters by roughly four orders of magnitude. The fine-tuned model is the base model plus a small "adapter" that can be loaded or removed at runtime.

The case for LoRA is strong for most adaptation scenarios. Training cost is a tiny fraction of full fine-tuning. The resulting adapters are small (megabytes rather than gigabytes). Multiple LoRAs can be combined or hot-swapped at inference time. The base model is unchanged, so security and licensing implications are straightforward.

The cases where LoRA falls short are real but specific: when the desired behaviour requires the model to know things it does not currently know, when the training data is large enough to justify the higher cost of full fine-tuning, when the behavioural change is large enough that the low-rank approximation cannot capture it.

In 2026 LoRA and its variants (DoRA, VeRA, QLoRA for memory efficiency) are the default fine-tuning method for most production use cases. The training is cheap, the deployment is flexible, and the results are usually good enough.

## Full fine-tuning

Full fine-tuning - training the entire base model on your data - is more expensive, more complex, and more powerful. The case for it has narrowed since LoRA became viable, but the remaining cases are real.

Full fine-tuning makes sense when:

- The desired capability change is genuinely large - not just "respond in this style" but "understand this completely new domain."
- The training corpus is large enough (millions of examples or more) to justify the higher cost.
- You need full control over the resulting model weights for licensing, deployment, or modification reasons.
- The base model needs to be modified, not just adapted - say, to remove a behaviour rather than redirect it.

The economics of full fine-tuning have improved significantly. Open-weight models like [Llama, Mistral, and Qwen](/ai/state-of-open-weight-models-2026/) are full-fine-tuneable for costs that a year or two ago would have required a research-lab budget.

## Distillation

[Distillation](https://arxiv.org/abs/1503.02531) takes a large model that works well and trains a smaller model to replicate its behaviour. The idea goes back to Hinton, Vinyals, and Dean's 2015 work on transferring the knowledge of a large ensemble into a single deployable model; in 2026 it is one of the most-used compression techniques in production. The smaller model is cheaper to run, faster to respond, and can be deployed in places the larger model cannot.

The 2026 distillation landscape is the most active research area of the three. Several specific techniques are in production use:

- **Output distillation** - train the student to match the teacher's output distribution on a representative dataset.
- **Reasoning distillation** - train the student on the teacher's chain of thought, including from [reasoning models](/ai/reasoning-models-2026/).
- **Task-specific distillation** - train a small model just for one specific task, using a larger model to generate training data.

Distillation is the right approach when you have an expensive model that works and you need a cheaper one that approximates it. The cost trade-off is usually favourable - a few hundred dollars of distillation cost saves orders of magnitude more in inference cost over the deployed lifetime.

## Continued pre-training

The fourth technique, often overlooked, is continued pre-training - taking a base model and continuing the original pre-training process on a domain-specific corpus before any task-specific fine-tuning.

This is appropriate when you have a large unlabelled corpus in a domain the base model has not seen well. Medical literature, legal documents in a specific jurisdiction, code in a specific language, scientific papers in a niche field. Continued pre-training builds in domain knowledge that subsequent fine-tuning then adapts to specific tasks.

The cost is higher than LoRA but lower than full fine-tuning from scratch. The benefit is real when the domain genuinely matters and the base model is genuinely weak on it.

## Picking between them

A practical decision tree for 2026:

- **Need behavioural style adaptation** (tone, format, persona) → LoRA
- **Need task-specific capability** with reasonable training data → LoRA, possibly multi-task LoRA
- **Need significant capability change** → full fine-tuning
- **Need a smaller model that behaves like a large one** → distillation
- **Need a model that understands a substantial new domain** → continued pre-training, then LoRA on top

The boring summary: each technique has its place, and in 2026 it is a real engineering decision to pick the right one. A year ago many teams defaulted to whichever technique was easiest to set up; now the right answer depends on what is actually being asked of the model.

## What has changed

Three specific things changed the fine-tuning landscape in 2026:

**Open-weight models with permissive licensing.** The Llama, Mistral, and Qwen families all allow commercial fine-tuning under reasonable terms. The legal friction that limited fine-tuning two years ago is largely resolved.

**Better tooling.** Libraries like Axolotl, [Unsloth](https://github.com/unslothai/unsloth), and the various Hugging Face tools have made fine-tuning routine rather than research-grade work. Unsloth alone claims training speed-ups of around 2x with up to 70% less VRAM across hundreds of models. A small team can produce production-quality fine-tunes without a dedicated ML engineering function.

**Cheaper compute.** The combination of [improved hardware](/ai/ai-hardware-wars-blackwell-mi300x-tpuv6/) and cloud GPU availability has made fine-tuning costs an order of magnitude lower than they were two years ago.

The combined effect is that fine-tuning is no longer a specialised activity reserved for big labs. It is a normal tool in the production AI toolkit, with the same caveat as any normal tool - knowing when to use it matters more than knowing how to do it.

## Related Reading

- [The State of Open-Weight Models in 2026](/ai/state-of-open-weight-models-2026/)
- [Fine-Tune vs RAG](/ai/fine-tune-vs-rag/)
- [Reasoning Models in 2026](/ai/reasoning-models-2026/)
- [AI Hardware Wars 2026](/ai/ai-hardware-wars-blackwell-mi300x-tpuv6/)
- [Claude's Memory and Long Context in 2026](/ai/claude-long-context-and-memory-2026/)
