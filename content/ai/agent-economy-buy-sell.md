---
title: "The Agent Economy: When AIs Buy and Sell From Each Other"
date: 2026-05-13T13:00:00+01:00
draft: true
tags: ["ai", "agent", "commerce", "payment", "a2a", "protocol", "2026"]
description: "A grounded look at the agent-to-agent economy actually forming in 2026 - the payment rails Visa and Mastercard have built for AI agents, the AP2 and ACP commerce protocols, AgentCore Payments, and what it really means when AIs start transacting with each other on a human's behalf."
cover:
  image: /assets/images/ai/agent-economy-buy-sell.jpg
  alt: The Agent Economy - When AIs Buy and Sell From Each Other Banner
---

The interesting part of the agentic-commerce conversation in 2026 is not that agents can now buy things - the demos have existed for two years. The interesting part is that the infrastructure underneath has matured to the point where the transaction is no longer the unusual part of the workflow. Visa, Mastercard, Stripe, Coinbase, and the major hyperscalers have shipped real payment rails for agents. The protocols for agent-to-agent commerce have stabilised enough that builders can actually integrate them. The headline is not the demo. The headline is that the boring infrastructure is now in place.

## TL;DR

- The agent-to-agent commerce stack is now production-ready. **Visa** and **Mastercard** have shipped agent-identity credentials. **Stripe** ships agent-native payment APIs. **Amazon Bedrock AgentCore Payments** (built with Coinbase and Stripe) lets agents transact natively. The infrastructure exists.
- The protocols have consolidated. The relevant set is **[MCP](/ai/agent-protocols-mcp-a2a-acp/)** for context and tool access, **A2A** for agent-to-agent communication, **AP2** (Agent Payments Protocol) for payment authorisation, and **ACP** (Agentic Commerce Protocol) for the broader commerce flow.
- The market is real. AI platforms are projected to account for [roughly $20.9 billion in retail spending](https://www.pymnts.com/news/artificial-intelligence/2026/ai-agents-are-becoming-the-new-power-brokers-in-digital-commerce) in 2026, nearly quadrupling 2025. McKinsey's range for the US B2C agentic commerce opportunity by 2030 is **$900 billion to $1 trillion**, with the global figure $3-5 trillion.
- The actual deployments today are dominated by three patterns: **agent-as-shopper** (an AI buys on a consumer's behalf), **agent-as-broker** (an AI negotiates between multiple service providers), and **agent-as-vendor** (an AI offers a service to other agents). The third pattern is the most novel and the one that will reshape commerce most.
- The unresolved problems are big: **identity and accountability** (who is liable when an agent makes a bad decision), **fraud and adversarial use** (the new attack surface is large), **regulatory clarity** (the existing financial-services rule set was written for humans), and **the trust gap with consumers** (most people are not yet comfortable letting an agent spend their money).
- The bet to watch is not whether agent commerce becomes real - it is - but whether the agent-to-agent leg (agents transacting with other agents on behalf of humans) actually scales, or whether the human-in-the-loop remains the binding constraint indefinitely.

## What is actually shipping

The most important thing to understand about the agent economy in 2026 is that the foundational pieces have moved from announcements to actual production infrastructure. The relevant set:

**Visa Intelligent Commerce.** Visa shipped its [agent-payments framework](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21961.html) in late 2025, with secure agent-identity credentials that let an AI agent transact with the same risk and authorisation framework Visa uses for cardholders. The framework went into production with major issuers in early 2026 and the transaction volume has been growing fast since.

**Mastercard Agent Pay.** Mastercard has shipped a parallel framework with its own agent-identity primitives and merchant integrations. The two networks are largely interoperable at the protocol level and the difference between them is mostly which issuing-bank and merchant relationships you happen to have.

**Stripe agent APIs.** Stripe has shipped agent-native payment APIs that handle the authorisation, the spending limits, the merchant authentication, and the dispute handling for agent transactions. The Stripe approach is closer to a complete API than to a protocol, and most agent-builders who want to ship transactions today are integrating with Stripe rather than directly with Visa or Mastercard.

**Amazon Bedrock AgentCore Payments.** Built with Coinbase and Stripe, [AgentCore Payments](https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/) is the most integrated of the current offerings. Agents built on Bedrock can transact in fiat (via Stripe) or in stablecoins (via Coinbase) within the same SDK. The integration is the early lead in the cloud-native agent commerce space.

**The protocol stack.** The 2026 picture for agent commerce protocols has consolidated around a small set: MCP for context and tool access, A2A for agent-to-agent communication, AP2 for payment authorisation, and ACP for the broader commerce flow. The protocols are well enough specified that builders can integrate them without needing custom bilateral arrangements with each counterparty, which was the binding constraint a year ago.

## The three patterns of agent commerce

The deployments that are actually working in production today cluster into three patterns. Each is different enough that they should be treated as separate categories.

### Agent-as-shopper

The pattern most people imagine when they hear "agent commerce" is the one where an AI buys things on a consumer's behalf. The agent receives an instruction (book a flight, order groceries, find a hotel under $200), executes the search across multiple providers, makes the purchase, and reports back.

This is the pattern that the consumer-facing AI products have been building toward since early 2025, and it is the pattern that the payment rails are most clearly aimed at. The major frontier-model providers - OpenAI's Operator, Anthropic's Claude tool-use APIs, Google's Project Astra-derived consumer agents - all support this pattern. The interesting commercial dynamic is that the agent is in a position to compare across providers in real time, which compresses the margin available to any single merchant and changes the shape of search-driven commerce significantly.

The McKinsey numbers for this pattern are large but they should be read with caution. The $900 billion to $1 trillion US B2C range by 2030 assumes the consumer-trust problem gets solved on a roughly five-year timeline, which is a strong assumption. The realistic 2026-2027 numbers are dominated by lower-stakes transactions - groceries, routine reordering, scheduled service purchases - rather than by the higher-stakes discretionary purchases the demo videos usually feature.

### Agent-as-broker

The second pattern is the one where an AI negotiates between multiple service providers on a human's behalf. The canonical example is travel booking, where the agent coordinates across airlines, hotels, transfers, and bookings to assemble a complete trip. The pattern extends to insurance comparison, mortgage origination, contract negotiation, and a growing list of B2B procurement workflows.

The interesting part of the broker pattern is that the agent itself becomes a real economic actor with its own interests. The agent that is negotiating on behalf of a consumer has incentives that may or may not align with the consumer's incentives - the agent could be paid a commission by one provider, could have a contractual obligation to one ecosystem, or could be optimising for an objective that does not match the consumer's stated objective. The resulting governance and disclosure questions are real and the regulatory response is still being worked out.

The B2B version of the broker pattern is further along than the consumer version. Enterprise procurement is dominated by agents that negotiate contracts, optimise across multiple suppliers, and execute the resulting purchases. The agents in this space are typically less generative than the consumer-facing ones - they are running structured optimisation rather than free-form reasoning - but they are economically more consequential because the transaction sizes are larger.

### Agent-as-vendor

The third pattern is the most novel and the one that has the largest implications for the shape of commerce. In this pattern the agent is not buying on behalf of a human - it is offering a service to other agents.

The early examples include: agents that perform specific kinds of data lookups for other agents (priced per query), agents that act as routing intermediaries between many agents and many service providers, agents that offer specialised reasoning capability (e.g., legal analysis, scientific synthesis) to other agents that need it, and agents that act as gateways to private data sources for authorised callers. The pattern is enabled by the same protocol stack that supports the other two but the economic dynamics are different - the buyer and the seller are both AIs, the transaction can happen at machine speed, and the price discovery mechanism is mediated entirely by software.

The agent-as-vendor pattern is currently small in dollar terms but it is growing fastest in transaction count, and the long-run implications are significant. If a substantial fraction of B2B services becomes mediated by agents on both sides, the economics of services delivery change in fundamental ways - the marginal cost of an additional transaction approaches zero, the friction of integration largely disappears, and the market structure shifts from human-mediated relationships to something closer to API-mediated relationships.

## The infrastructure that makes this possible

The infrastructure layer underneath the agent economy has matured in three concrete ways during 2025-2026.

**Identity.** The single biggest unblock for agent commerce was the appearance of credentialled agent identities. Visa and Mastercard's agent-identity frameworks let a merchant know not just that "an AI made this purchase" but that "this specific agent, authorised by this specific human, with this specific spending authority, made this purchase." The disambiguation is what makes the risk model work at scale - the merchant can trust the transaction because the identity chain is traceable to a human who is liable.

**Authorisation.** AP2 and the parallel mechanisms inside the major commerce platforms let a human grant an agent specific spending authority - dollar limits, merchant categories, time bounds, requires-approval-above thresholds - in a way that is enforceable by the payment rails. The granularity is the difference between giving an agent a credit card and letting it do anything (the 2024 way) versus giving an agent a constrained mandate that the payment infrastructure itself enforces (the 2026 way).

**Settlement.** The fiat-side settlement infrastructure works because it sits on top of the existing card networks. The stablecoin-side settlement infrastructure has matured enough to be a credible alternative for transactions where the fiat rails are inconvenient - cross-border, machine-to-machine, micropayments. Amazon's choice to integrate Coinbase into AgentCore Payments alongside Stripe is the most visible commercial signal that the stablecoin rails are no longer a fringe option.

**Dispute resolution.** This is the least mature part of the stack but the most important for scale. When an agent makes a bad purchase - the wrong item, the wrong amount, a fraudulent transaction - the resolution path has to work or the trust required for the rest of the system to function does not exist. The current solutions involve a combination of automated rollback at the payment layer (chargebacks), human-mediated resolution at the merchant layer, and increasingly, automated mediation between the agents themselves. The dispute resolution side is genuinely unsolved and it is where most of the next 18 months of infrastructure work is going to happen.

## The unresolved problems

The agent economy is real but it is not yet stable. The unresolved problems are large and they are going to determine the shape of the next several years.

**Identity and accountability.** The legal framework for accountability when an agent makes a bad decision is incomplete in every major jurisdiction. The current default is that the human who authorised the agent is liable, which works for clear-cut cases but breaks down in more ambiguous situations - the agent did something the human did not specifically authorise, the agent was misled by a counterparty, the agent was operating under instructions that turned out to have been compromised. The legal cases are starting to work through the courts and the resulting framework will likely not settle for several years.

**Adversarial use.** The agent economy creates a large new attack surface. Prompt injection attacks against agent-mediated purchasing. Adversarial websites that manipulate agent buying decisions. Synthetic merchants that exist only to extract payments from automated buyers. The security work in this space is just beginning and the early attacks have been more sophisticated than the defences. This is one of the areas where the rate of attack innovation has been faster than the rate of defence innovation, which is the inverse of what builders would like to see.

**Regulatory clarity.** Most financial-services regulation was written assuming the entity making the transaction is a human. Agent-mediated commerce raises questions that the existing rule sets do not cleanly answer - Know Your Customer obligations on the human or on the agent, dispute resolution when the agent was acting beyond its mandate, advisory and fiduciary obligations when an agent gives purchase advice, the application of consumer-protection laws to non-human buyers. The regulators are working on this but the pace is slower than the deployment pace, which creates real legal uncertainty for builders.

**Consumer trust.** The single biggest commercial constraint on the agent economy is that most consumers are not yet comfortable letting an AI agent spend their money in any significant amount. Surveys consistently show that consumer comfort with agent purchasing is high for low-value, repeat transactions and falls off sharply above a few hundred dollars or for novel purchases. The trust gap is not technical - it is psychological - and the path to closing it depends on accumulating enough good experiences to outweigh the bad ones. This is a slow process and the timeline for full consumer trust at high-value transactions is probably longer than the marketing implies.

## The controversial parts

Three claims in the agent-economy conversation deserve more pushback than they typically get.

The first is the claim that agent commerce will replace human commerce. The empirical evidence is that agents complement human shopping rather than replacing it. The agent-mediated transactions in 2026 are dominated by routine, low-stakes purchases. The high-stakes, discretionary, identity-expressing purchases that drive a significant fraction of consumer spending remain firmly human-mediated. The reasonable expectation for the next several years is a hybrid where agents handle the boring purchases and humans continue to handle the meaningful ones.

The second is the claim that agent-to-agent commerce will dwarf human-to-agent commerce within five years. The B2B numbers are growing fast but the consumer-facing economic activity is still much larger. The agent-to-agent leg is structurally important - it is the part that compounds in ways the human-mediated leg does not - but the absolute scale is going to be smaller than the consumer-facing side for the foreseeable future.

The third is the claim that the existing payment rails will be displaced by crypto-native rails optimised for agents. The empirical evidence is the opposite - the existing payment rails have been more responsive to the agent opportunity than most observers expected, and the fiat side is winning the bulk of the transaction volume by a wide margin. The crypto rails are real and growing in specific niches (cross-border, micropayments, machine-to-machine) but they are complements to the fiat infrastructure rather than replacements for it.

## Where this is heading

The most likely shape of 2027-2028 is that agent commerce becomes a normal part of the consumer and business economy, dominating specific categories (routine purchasing, repeat orders, structured B2B procurement) while remaining minor in others (luxury goods, discretionary spending, high-stakes one-off purchases). The infrastructure will continue to mature, the protocols will continue to consolidate, and the consumer-trust problem will close gradually rather than suddenly.

The other prediction worth making is that the agent-as-vendor pattern will produce the most surprising business outcomes over the next two years. The economic model where AIs sell to other AIs is genuinely novel, the deployment patterns are still being worked out, and the resulting market structures are unpredictable. The companies that figure out how to position themselves as agent-native vendors - selling capability to other agents rather than to humans - are likely to capture an outsized fraction of the upside.

For builders, the practical guidance is to take the infrastructure seriously and to design for agent-mediated transactions even if your current users are humans. The credentialled agent identity, the AP2-compatible authorisation, the structured dispute resolution paths - these are the primitives that the next several years of commerce are going to be built on, and being early on them is cheap relative to retrofitting them later. The agent economy is not a future scenario any more. It is a present one that is going to keep growing, and the question is what role you want to have in it.

## Related Reading

- [The Quiet Standardisation of Agent Protocols - MCP, A2A, ACP Compared](/ai/agent-protocols-mcp-a2a-acp/) - the protocol layer underneath the commerce infrastructure.
- [AI Agents That Actually Work: Patterns From Real Projects](/ai/ai-agents-that-actually-work/) - the deployment patterns that the commercial agent economy is built on.
- [A Year of Agents, and What is Coming Next](/ai/ai-agents-emergency-debate/) - the broader agent-deployment story.
- [Hermes Agent: Persistent Autonomy That Learns and Grows](/ai/hermes-agent/) - the long-running-agent end of the same architectural story.
- [Four Futures for the Machine-Speed Economy](/ai/four-futures-machine-speed-economy/) - the broader economic scenarios the agent economy is one component of.
