---
title: "Polkadot 2.0 One Year On - Did Agile Coretime Deliver?"
date: 2026-05-02T09:00:00+01:00
draft: false
tags: ["polkadot", "blockchain", "web3", "2026"]
description: "A year after Polkadot 2.0 went live, the data is in. Did Agile Coretime, Elastic Scaling, and Asynchronous Backing actually move the needle? An honest scorecard on utilization, builder economics, and what still has not landed."
cover:
  image: /assets/images/blockchain/polkadot-2-one-year-on.jpg
  alt: Polkadot 2.0 One Year On Banner
---

## TL;DR

- One year after [Polkadot 2.0](https://polkadot.com/) shipped its three flagship pieces - **Agile Coretime**, **Elastic Scaling**, and **Asynchronous Backing** - the picture is mixed but mostly positive.
- **What worked:** core prices collapsed, network utilization roughly doubled, and the barrier to entry is now hundreds of dollars instead of millions. New teams are shipping that would never have run a crowdloan.
- **What did not:** the secondary market for cores is thin, bulk sales are dominated by a small set of repeat bidders, and the developer story for "buy a core and ship something" is still rougher than it should be.
- **The honest verdict:** Agile Coretime delivered on the economics. It did not deliver on the user-experience promise. Polkadot 2.0 is a better foundation than Polkadot 1.0 by every measurable metric, but the application layer is still where the network has to prove itself.

## Where We Were A Year Ago

Last September I wrote a [plain-English explainer of Agile Coretime](/blockchain/polkadot-agile-coretime-explainer/). The pitch was simple: stop selling parachain slots like reserved parking spaces and start selling them like a parking meter. Pay for what you use, when you use it. Resell what you do not.

The case for change was strong. Crowdloan auctions had locked up roughly $2-5M of DOT per slot, ran for two years at a time, and left the network operating at maybe 30-40% effective capacity. Smaller teams were locked out. Larger teams were over-provisioned. The economics were a museum piece by 2024.

A year on, the question is no longer "is this a good idea." The question is "did it actually work in production." This post is my attempt to answer that without the marketing gloss.

## The Three Pillars - Status Check

Polkadot 2.0 is really three coordinated upgrades. They have to be evaluated together because they reinforce each other.

### Asynchronous Backing

**Status: shipped, working, and largely invisible.**

Async Backing roughly halved block time and doubled the size of each block. For users this shows up as faster confirmations and a smoother feel, especially on parachains that lean on the relay chain for finality. There is no real controversy here. It is the kind of upgrade that you only notice if you compare clips of the old chain side by side.

### Elastic Scaling

**Status: live, but uneven adoption.**

Parachains can now claim multiple cores during demand spikes. [Moonbeam](https://moonbeam.network/) and [Astar](https://astar.network/) have been the loudest beneficiaries, reporting 3-5x throughput jumps when the feature is engaged. The catch is that most parachains do not actually need this yet. Demand on Polkadot is not the bottleneck for most teams - distribution and product-market fit are. Elastic Scaling is sitting there waiting for traffic that has not fully arrived.

### Agile Coretime

**Status: live, prices below early models, secondary market thin.**

This is the one I want to spend the rest of the post on, because this is the upgrade that was supposed to fix builder economics. Did it?

## The Numbers - Honest Scorecard

I have pulled what is publicly visible from the [Polkadot Coretime dashboards](https://coretime.polkadot.network/) and various ecosystem analytics. The numbers below are directional, not audited.

### Core Prices

When Agile Coretime launched, the assumption was a clearing price somewhere in the low thousands of dollars per core per 28-day period (a "region"). Reality has come in well below that.

- **Bulk sale clearing price (early 2026):** roughly $100-400 per core per region, depending on the cycle.
- **On-demand spot pricing:** typically a small fraction of a cent per block of execution, well below most teams' budgeting threshold.
- **Implied annual cost** to run a single full-time core: a few thousand dollars rather than a few million.

Compared to the old slot model, this is a 100x to 1000x reduction in the cost of access. That part of the thesis worked.

### Utilization

Pre-2.0 estimates put Polkadot's effective core utilization in the 30-40% range. Post-2.0 numbers I have seen quoted by ecosystem analysts put it closer to 55-70% on busy days, with significant variance by core. Not the 95% efficiency of a perfectly packed network, but a clear and durable improvement.

### Number of Active Projects On Cores

This is the metric I find most encouraging. The number of distinct teams paying for coretime in any given month has roughly tripled since the old auction model, even though many of those new entrants are buying small slices rather than full cores. The long tail finally exists.

### Secondary Market Depth

This is where the story gets less flattering. The secondary market - the resale of unused cores between teams - was supposed to be the price-discovery engine that made the system efficient. In practice it is still thin. Most cores are bought directly in the bulk sale and held. Resale volume is a single-digit percentage of primary sales. There is not yet a meaningful liquid market for blockspace on Polkadot.

That is not necessarily fatal. It is exactly what you would expect in year one of any new market. But it is not the picture that was painted.

## What Builders Actually Tell Me

Across the teams I have talked to or read post-mortems from, three observations come up repeatedly.

**The cost is no longer the problem.** Nobody is complaining about coretime pricing. If anything, the bulk sale clearing price is suspiciously low and has fueled some debate about whether the protocol is leaving DOT-denominated revenue on the table.

**The tooling is the problem.** Buying coretime, registering as a parachain, and actually shipping something is still a multi-day exercise involving Substrate, runtime upgrades, and infrastructure decisions that look nothing like deploying a Solidity contract on an EVM rollup. The cost barrier is gone. The cognitive barrier is not.

**The "rent a core for a weekend" use case is theoretical.** The promise of Agile Coretime included light, transient uses - hackathon projects, short-lived experiments, one-off events. In practice almost nobody is doing this, because the operational overhead of standing up and tearing down a chain dwarfs the cost of the core itself.

This is a tooling problem, not an economics problem. But it is the gap between "Agile Coretime works" and "Agile Coretime delivered the experience that was promised."

## What The Critics Got Right

Looking back at the criticism from late 2024 and early 2025, two of the warnings have aged well.

**Variable costs are harder to budget than fixed slots.** Some teams genuinely preferred the old model because it gave them a known two-year runway. Variable pricing means CFO conversations every region. For corporate or grant-funded projects this matters more than the absolute cost.

**A small number of buyers can dominate bulk sales.** The bulk sale mechanism has trended toward a handful of repeat large buyers, which creates concentration risk. The secondary market was supposed to mitigate this, and to date it has not - because the secondary market is thin.

Neither of these is catastrophic. Both are real.

## What The Critics Got Wrong

**"Without crowdloans, DOT loses its sink."** The fear was that ending the auction-driven crowdloan model would kill DOT's primary demand mechanism. In practice, coretime sales, staking, and governance utility have absorbed that role. DOT did not crater on the transition. The market mostly shrugged.

**"Existing parachains will defect."** The expectation in some quarters was that parachains would migrate to other ecosystems once the slot lock-ins expired. The actual pattern has been the opposite - most parachains renewed under the new model and a meaningful minority added cores via Elastic Scaling. Defection has been the exception, not the rule.

**"Without slot scarcity, parachains stop mattering."** The opposite happened. Parachains stopped being the unit of prestige and started being the unit of work. That is healthier.

## The Two Open Questions For Year Two

### 1. Does the secondary market mature?

If coretime is going to behave like a real commodity market, resale liquidity has to grow. That probably needs:

- **Better tooling for listing and pricing** unused cores - the on-chain primitives exist but the UX is not friendly.
- **Standardised core-rental contracts** so a team can cleanly rent excess capacity from another for a region without long negotiations.
- **Aggregators or market makers** willing to take inventory risk and provide quotes.

If those land, the resale market should thicken naturally. If they do not, Agile Coretime ends up looking more like a lower-priced primary auction than a true market.

### 2. Does the application layer finally ship?

Polkadot's biggest 2026 pivot, [as discussed elsewhere on this blog](/blockchain/polkadot/polkadot-2026/), is from infrastructure to applications. The infrastructure case is now made. The application case is still being argued. Coretime is cheap and abundant - the question is whether the things being built on top of it are interesting enough for normal users to care.

That is no longer a Polkadot 2.0 question. That is a Polkadot ecosystem question, and it will be answered by what teams ship over the next 12 months, not by another runtime upgrade.

## So - Did Agile Coretime Deliver?

**On economics: yes, decisively.** Cost of access fell by orders of magnitude. Utilization improved meaningfully. The long tail of small projects exists where it did not before. The thesis is validated.

**On user experience: not yet.** The secondary market is thin. The tooling for casual or transient use is missing. The "rent a core for a weekend" workflow does not exist in practice.

**On strategic positioning: better than expected.** Polkadot did not lose parachains, did not lose DOT demand, and did not lose its identity. It traded an exclusive auction model for a market-based one without breaking what worked.

The way I would summarise it: Polkadot 2.0 fixed the economics it set out to fix. The remaining problems are softer - tooling, application traction, and market depth - and those are the right problems to have. Better to be a chain with cheap blockspace looking for users than a chain with expensive blockspace looking for users.

A year ago I wrote that "the infrastructure is now in place. The question for 2026 and beyond is: will teams and users actually migrate?" The infrastructure has held up. The migration is partial. Year two is where the application thesis gets tested.

## Related Reading

- [Polkadot's Agile Coretime: A Plain-English Explainer](/blockchain/polkadot-agile-coretime-explainer/)
- [Polkadot 2026: From Infrastructure to Applications](/blockchain/polkadot/polkadot-2026/)
- [The State of Blockchain in 2026](/blockchain/state-of-blockchain-2026/)
- [Cardano vs Polkadot](/blockchain/cardono-vs-polkadot/)
- [Quantum Threat to Blockchain](/blockchain/quantum-threat/)
