---
title: "Claude Fable 5 and Mythos 5: Anthropic's Mythos-Class Models Go Public  -  With Guardrails"
date: 2026-06-09T19:00:00+01:00
draft: false
tags: ['ai', 'anthropic', 'claude', 'mythos', 'fable', 'model-release', 'ai-safety', '2026']
description: "Anthropic launches Claude Fable 5 for general use and Claude Mythos 5 for trusted partners  -  the same underlying model, split by safeguards. State-of-the-art on coding, vision, and science, with classifiers that fall back to Opus 4.8 on risky topics."
cover:
  image: /assets/images/ai/claude-fable-mythos.jpg
  alt: Claude Fable 5 and Mythos 5 release
---

## TL;DR

- **Claude Fable 5** is Anthropic's first Mythos-class model made safe for general use  -  state-of-the-art on nearly every benchmark Anthropic tested, with the gap widening on longer, more complex tasks
- **Claude Mythos 5** is the same underlying model with cyber safeguards lifted for Project Glasswing partners; a biology trusted-access program is coming next
- Risky queries in cybersecurity, biology/chemistry, or suspected distillation attempts are routed to **Claude Opus 4.8** instead  -  roughly **5% of sessions**, with Anthropic acknowledging some false positives
- Pricing drops to **$10 / $50 per million input/output tokens**  -  less than half what Mythos Preview cost
- Fable 5 is free on Pro, Max, Team, and seat-based Enterprise plans through **22 June 2026**, then moves to usage credits until capacity catches up

Two months ago I wrote that [Claude Mythos Preview was the benchmark breaker that would not be released](/ai/claude-mythos-benchmarks/)  -  93.9% on SWE-bench, thousands of zero-day vulnerabilities found autonomously, access restricted to a dozen companies through Project Glasswing. The question hanging over that post was whether Anthropic could ever democratise Mythos-level capability without democratising the offensive potential.

On 9 June 2026, they gave a partial answer. **Claude Fable 5** and **Claude Mythos 5** launch together as the same underlying model wearing different safety configurations. Fable is the public face; Mythos is the restricted one. The names are deliberate  -  from the Latin *fabula* ("that which is told") and the Greek *mythos*  -  and the split between them is the story.

## Same Model, Two Deployments

This is the important architectural point, and Anthropic is unusually explicit about it.

Fable 5 and Mythos 5 share weights. What differs is the **safeguard stack** wrapped around them. Fable gets classifiers that intercept potentially dangerous queries and hand off to Opus 4.8. Mythos, available only to vetted cyber defenders through [Project Glasswing](https://www.anthropic.com/news/expanding-project-glasswing) (and soon to select biology researchers), has those classifiers lifted in specific domains.

That means when Fable's safeguards do not trigger  -  which Anthropic says is more than 95% of sessions  -  you are effectively getting Mythos-level performance. When they do trigger, you get Opus 4.8, which is still a strong model, not a hard refusal. The design choice is pragmatic: a fallback beats a block, and Anthropic can tune conservatively without leaving users stranded.

For the partners who already had Mythos Preview, Mythos 5 is an upgrade at substantially lower cost. For everyone else, Fable 5 is the first time Mythos-class capability is generally available  -  with the caveat that "generally available" now includes an invisible safety layer you will sometimes notice.

## What "Mythos-Class" Actually Means in Practice

Anthropic positions Mythos-class models above Opus in capability. Fable 5 is their strongest generally released model, and the announcement backs that with a wide spread of evals and customer testing rather than a single headline number.

### Software engineering

The Stripe example is the one that stuck with me: a codebase-wide migration across a **50-million-line Ruby codebase**, completed in a day where a team would have needed two months. That is not a benchmark abstraction  -  it is a production system with real constraints.

On Cognition's FrontierCode eval  -  which tests whether models can pass difficult coding tasks while meeting production-codebase standards  -  Fable 5 leads frontier models even at medium effort, and Anthropic emphasises it is more **token-efficient** than prior Claude models. Cursor's Michael Truell called it state of the art on CursorBench and said it opens a class of long-horizon problems that were previously out of reach. GitHub's Mario Rodriguez framed it as a step toward developers handing increasingly ambitious work to agents across the full software lifecycle.

If you have been following the agentic coding arc  -  from [Claude Code vs Cursor](/ai/claude-code-vs-cursor/) debates to Boris Cherny's view that the typing layer is essentially solved  -  Fable 5 is the model release that makes "hand it a multi-week project and check back" feel less like marketing and more like something early-access customers are actually reporting.

### Vision

Fable 5 is now state of the art on vision tasks. The Pokémon FireRed demo is the memorable proof point: earlier Claude models needed elaborate helper harnesses with maps and navigation aids; Fable 5 beat the game with a **minimal vision-only harness**  -  raw screenshots, no extra game-state information.

That is a useful proxy for real work. Extracting precise numbers from scientific figures, rebuilding a web app's source code from screenshots alone, playing complex visual environments without scaffolding  -  these are the tasks where previous models needed humans to pre-process the input. Fable 5 needs less of that preprocessing, which matters directly for agent workflows where every extra tool call is latency and cost.

### Memory and long horizons

The long-context story is not just "more tokens in the window." Anthropic tested persistent file-based memory while playing *Slay the Spire*: memory improved Fable's performance **three times more** than it helped Opus 4.8, and Fable reached the game's final act three times more often.

Combined with reports that Fable stays focused across **millions of tokens** in long-running tasks and improves its own outputs using notes it writes for itself, this is the capability dimension that separates Mythos-class from incremental Opus upgrades. Short prompts get incremental gains. Multi-day autonomous work gets step-function gains. That pattern showed up again in customer quotes  -  Matthew Pines reported Fable getting nearly to where GPT-5.5 landed after four days, but in 36 hours and using a third of the reasoning tokens.

### Knowledge work and finance

On Hebbia's Finance Benchmark for senior-level reasoning, Fable 5 leads. IMC reported it aced trading-analysis evaluations across factual lookup, conceptual reasoning, root-cause analysis, and expected-value analysis. Izzy Miller at Hebbia noted a **10-point jump** over Opus on complex, long-running analytical tasks  -  the first model to break 90% on their core benchmark.

For legal work, Aveek Duttagupta reported blind review where Fable's redlines matched or beat their current model every time. These are domain-specific evals, not SWE-bench, and they matter because they describe the knowledge-work automation that enterprise buyers actually pay for.

## Mythos 5: Where the Safeguards Come Off

The restricted version is where Anthropic's life-sciences results get genuinely striking.

Using Mythos 5, internal protein design experts accelerated aspects of drug design by around **ten times**. In one study, Mythos 5 with protein design and bioinformatics tools  -  no human assistance  -  matched or beat skilled human operators across the full workflow: choosing binding sites, selecting tools, running them, recovering from failures. Nine of fourteen protein targets yielded strong drug-design candidates now under investigation.

On the research side, Mythos 5 is Anthropic's first model to **consistently produce novel, compelling scientific hypotheses**. In blinded comparisons against Opus-class models, their scientists preferred Mythos's molecular biology hypotheses roughly 80% of the time. One hypothesis about an *E. coli* protein mechanism was independently corroborated by another lab working on the same problem.

Perhaps most surprising: Mythos 5 conducted novel genomics research over more than a week of largely autonomous work  -  assembling single-cell data for millions of cells across 138 animal species, designing and training a custom ML model, and outperforming a recent *Science* publication with a model **100 times smaller**. Anthropic intends to publish these results in the coming months.

These are the capabilities that make the biology safeguard question hard. The same model that accelerates gene therapy research can, in the wrong hands, assist with designing dangerous viruses. Anthropic's AAV shell assembly eval  -  where Mythos-class models outperformed dedicated protein language models on unpublished therapeutic candidates  -  is cited as evidence of both promise and risk.

## The Safeguard Architecture

Releasing Fable 5 required more than policy documents. Anthropic built a new classifier layer  -  separate AI systems that detect potential misuse, including jailbreak attempts, and route flagged queries to Opus 4.8.

Three domains are covered:

1. **Cybersecurity**  -  exploitation, offensive cyber tasks, agentic hacking workflows. External red-teaming over 1,000+ hours found no universal jailbreaks. One partner reported zero compliance with harmful single-turn cyber requests across 30 public jailbreak techniques.
2. **Biology and chemistry**  -  broadened from the previous narrow bioweapons filter, because Mythos-class models can now accomplish real scientific tasks. For now, most bio/chem queries fall back to Opus 4.8; a trusted access program for biology researchers will offer Fable with bio safeguards removed but cyber safeguards intact.
3. **Distillation**  -  Anthropic has previously identified large-scale attempts to extract Claude capabilities for training competing models. Flagged distillation attempts also fall back to Opus 4.8.

Anthropic is candid that the tuning is **conservative** and will produce false positives. They prioritised safe release speed over perfect precision, with a stated goal of narrowing the classifiers as they gather post-launch data.

There is also a new **30-day data retention policy** for all Mythos-class model traffic on first- and third-party surfaces. The data will not be used for training; it supports detecting novel jailbreaks and reducing false positives, with logged human access and deletion after 30 days in almost all cases.

On alignment, Anthropic's automated assessment found Mythos 5's level of misaligned behaviour  -  deception, cooperation with misuse  -  was low and similar to Opus 4.8. Since Fable and Mythos share weights, Fable's alignment profile should be comparable when safeguards are not engaged.

## Pricing and Availability

Both models cost **$10 per million input tokens** and **$50 per million output tokens** via the Claude API (`claude-fable-5`). That is less than half Mythos Preview pricing and represents Anthropic's continued pattern of not charging a premium tier tax on capability upgrades  -  the same approach I noted in the [Opus 4.7](/ai/claude-opus-4-7/) write-up.

Availability is staged because Anthropic expects demand to exceed capacity:

- **API and consumption-based Enterprise**: Fable 5 fully available from launch
- **Pro, Max, Team, seat-based Enterprise**: Fable 5 included at no extra cost through **22 June 2026**
- **After 23 June**: Fable 5 requires usage credits until capacity allows restoring it as a standard subscription inclusion

Mythos 5 remains restricted: Glasswing partners get cyber safeguards lifted; biology trusted access expands soon; a broader application-based program is planned in consultation with the US government.

## What Changed Since Mythos Preview

If you read my earlier posts on [Mythos benchmarks](/ai/claude-mythos-benchmarks/) and [the forbidden frontier](/ai/claude-mythos-restricted/), the arc is clear.

April 2026: Mythos Preview proves Anthropic can build models a full tier above Opus, but restricts them because autonomous vulnerability discovery across every major OS and browser is not something you put on the public internet.

June 2026: The same capability tier ships publicly as Fable 5, wrapped in classifiers that Anthropic believes are robust enough for general release  -  with Mythos 5 continuing restricted access for domains where even good classifiers are not enough.

This is not the open-release many hoped for after Mythos Preview. It is something more interesting: a **tiered deployment model** where capability, safeguards, and access control are explicit product dimensions rather than afterthoughts. The best model and the publicly available model are still not always the same thing, but the gap narrowed  -  with Opus 4.8 serving as the safety valve rather than a hard wall.

## What I Am Watching

A few questions the announcement raises but does not fully answer:

**False positive rate in the wild.** Less than 5% of sessions triggering fallback sounds manageable until you are a biomedical researcher whose legitimate query gets routed to Opus. The biology trusted access program is the near-term fix; classifier precision is the long-term one.

**Whether long-horizon gains hold outside Anthropic's harness.** Pokémon, Factorio, Slay the Spire, and solar-system simulations are compelling demos, but they are also environments where success is verifiable. The harder test is ambiguous product work  -  the kind where "done" is a judgment call, not a game state.

**Competitive response.** Fable 5's benchmark table compares against other leading models, and early customer quotes name GPT-5.5, Opus 4.8, and frontier coding evals explicitly. Whether this resets the pricing and capability expectations for OpenAI and Google's next releases will become clear quickly.

**The distillation classifier.** Flagging extraction attempts is sensible given Anthropic's stated concerns about authoritarian-state distillation campaigns, but the line between legitimate evaluation, fine-tuning research, and extraction is blurry. How that classifier behaves in practice will matter for the research ecosystem.

For developers already running agentic workflows, the practical takeaway is straightforward: Fable 5 is worth trying on the problems that were too long, too visual, or too multi-step for Opus 4.8  -  and you have until 22 June on subscription plans to do that without extra credits. For the security and biotech communities, Mythos 5 confirms that the restricted tier is not a one-off preview but a permanent product line sitting above Opus, with trusted access expanding rather than contracting.

Anthropic's bet is that they can ship the most capable model they have ever released generally, keep the most dangerous slices gated, and iterate the safeguards fast enough that the 5% fallback rate shrinks without the remaining 95% paying a safety tax on performance. Given how long we waited for Mythos-class capability to leave the vault, that is a reasonable bet. Whether the classifiers hold under sustained adversarial pressure  -  and whether the false positives stay tolerable for legitimate researchers  -  is the experiment we are all now running.

## Sources

- [Claude Fable 5 and Claude Mythos 5  -  Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [Expanding Project Glasswing  -  Anthropic](https://www.anthropic.com/news/expanding-project-glasswing)

## Related Reading

- [Claude Mythos: The AI Benchmark Breaker That Won't Be Released](/ai/claude-mythos-benchmarks/)
- [The Forbidden Frontier: Claude Mythos and the Dawn of Restricted AI Power](/ai/claude-mythos-restricted/)
- [Claude Opus 4.7: Autonomy and Vision at Scale](/ai/claude-opus-4-7/)
- [AI Safety From First Principles: What Actually Matters vs What's Hype](/ai/ai-safety-first-principles/)
- [Securing AI Agents](/ai/securing-ai-agents/)
- [AI in Scientific Research 2026](/ai/ai-in-scientific-research-2026/)
- [Will AI Kill Coding Jobs? Claude Code's Creator Reacts](/ai/will-ai-kill-coding-jobs-cherny/)
