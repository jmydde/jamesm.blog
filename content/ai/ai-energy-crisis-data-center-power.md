---
title: "The AI Energy Crisis: Why Data Center Power Will Define the Next Decade"
date: 2026-05-12T17:00:00+01:00
draft: true
tags: ["ai", "energy", "infrastructure", "data-center", "policy", "2026"]
description: "A grounded look at the energy constraint becoming the binding limit on AI deployment in 2026 - the power demand, the transformer backlogs, the grid interconnect queues, the rising consumer electricity prices, and what it means for the shape of the next decade of compute."
cover:
  image: /assets/images/ai/ai-energy-crisis-data-center-power.jpg
  alt: AI Energy Crisis - Why Data Center Power Will Define the Next Decade Banner
---

For most of the AI conversation in 2024 and 2025, the binding constraints on the build-out were chips and capital. By 2026 the conversation has shifted, and the constraint that gets discussed most seriously inside the hyperscalers is electricity. Not the cost of electricity. The actual physical availability of electrons - at gigawatt scale, in the places where the data centres need to be, on the schedule the model labs need them to be. The story does not have a single villain or a single number, but it has a shape, and the shape is becoming the story of the second half of the decade.

## TL;DR

- The [International Energy Agency](https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions) projects global data centre electricity consumption to reach roughly 1,100 TWh in 2026 - approximately equivalent to Japan's entire national electricity consumption.
- US data centre demand is forecast to roughly double from around 80 GW in 2025 to 150 GW by 2028, with [Morgan Stanley estimating](https://www.morganstanley.com/insights/articles/powering-ai-energy-market-outlook-2026) a power shortfall of approximately 49 GW against planned demand by the end of the decade.
- The binding constraints are not generation capacity in the abstract but the specific bottlenecks underneath it: **high-voltage transformer lead times** (now 36-48 months in some markets), **grid interconnection queues**, **water for cooling**, and the **regulated rate-making process** in the markets where the data centres want to sit.
- Between 12 and 16 GW of announced US data centre capacity will not come online on schedule, against only roughly 5 GW currently under active construction. The gap is not capital - it is permission, transformers, and grid access.
- Retail US electricity prices are up 42% since 2019, and Goldman Sachs forecasts AI-driven data centre demand will add roughly 0.1% to core inflation in 2026 and 2027. The political economy of the energy build-out is now a real story, not a hypothetical.
- The strategic implication is that the location of compute is no longer a choice - it is a function of where the power is. The next wave of AI infrastructure investment is moving to where the grid will actually deliver, including locations that would not have been on anyone's data centre map five years ago.

## The numbers people stopped wanting to update

The single most striking fact about the 2025-2026 AI energy story is how fast the forecasts have moved. The number that was the upper bound in 2024 became the lower bound in 2025 and the baseline by 2026.

The [IEA's December 2024 forecast](https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions) for data centre electricity consumption was revised upward by approximately 18% in early 2026 to a projected 1,100 TWh for the year. To put that in context, that is roughly the entire annual electricity consumption of Japan, or roughly 4% of global electricity demand attributable to a single workload category. The growth rate is what matters more than the level. Data centre consumption is growing at roughly 15-20% per year in the major markets, against an overall electricity demand growth rate that has historically been close to flat in the developed economies.

In the US specifically, the [Bloom Energy January 2026 report](https://www.morganstanley.com/insights/articles/powering-ai-energy-market-outlook-2026) projects total data centre demand approximately doubling from 80 GW in 2025 to 150 GW by 2028, driven almost entirely by AI training and inference. Morgan Stanley's own forecast is somewhat lower - roughly 74 GW of new US demand by 2028 - but it is the gap between forecast demand and forecast available supply that matters, and that gap is approximately 49 GW. That is more than the total electricity consumption of most European countries, and it is the supply that does not exist on the timetable the AI build-out is assuming.

The reason the forecasts keep moving is that the underlying assumptions about model efficiency, deployment density, and agent workloads have all moved faster than the forecasters expected. A single agentic workload in 2026 consumes orders of magnitude more compute than the equivalent chat workload did in 2023, not because the models are bigger but because they think for longer per task and run many parallel branches. The IEA's [March 2026 update](https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions) is explicit that the inference cost dynamics, not the training cost dynamics, are what drove the upward revision.

## The bottlenecks under the bottleneck

The headline framing - "AI needs more electricity" - obscures the more important point. The constraint is not generation in the abstract but the specific physical and institutional bottlenecks that determine whether new generation can be delivered to a specific data centre on a specific timetable.

**Transformers.** High-voltage transformers are the substations that step grid power down to the levels useful inside a data centre. Lead times for new transformers have stretched from a typical 12-18 months to 36-48 months in some markets. The manufacturers - a small number of mostly European and Asian firms - are running at full capacity and the order backlog has lengthened faster than the production capacity has been able to scale. A data centre that has the land, the power purchase agreement, and the construction crew can still be delayed by 18 months waiting for the transformer.

**Grid interconnection queues.** Large new loads do not simply plug into the existing grid. They go through an interconnection study, often a series of studies, and they wait in a queue with every other new generation and load project. The queues have lengthened to the point where projects announced in 2024 are routinely now expected to energise in 2027 or later. The queue is itself a function of how slowly the interconnection studies are being done relative to the number of new projects, and it is one of the few constraints in the AI build-out that is institutional rather than physical.

**Water.** Most large data centres use significant water for cooling, particularly in hot climates. The water requirements have become a binding constraint in several markets including parts of Arizona, Texas, and the Midwest, and the permitting process for new water rights has slowed significantly. The newer designs use less water through closed-loop cooling or air-cooled approaches, but the retrofit cost on existing announcements is meaningful.

**Regulated rates.** Most US electricity is sold at rates set by state public utility commissions. Large new loads change the cost structure of the local grid in ways that affect existing residential and commercial customers, and the rate-making process for accommodating them is contentious and slow. Several states have passed or proposed legislation requiring data centres to pay differential rates that reflect the cost of the infrastructure they require, which changes the unit economics significantly relative to the assumptions baked into many existing data centre business cases.

These constraints compound. A data centre can be capital-blessed, model-lab-backed, and shovel-ready and still be unable to energise on schedule because any one of these four constraints is binding. The reason between 12 and 16 GW of announced capacity will not energise on schedule is not that the capital walked away - it is that the slowest of these constraints determined the actual delivery date.

## Where the build-out is actually going

The interesting consequence of the constraint shifting from capital to power is that the geography of AI infrastructure is changing. The decisions about where to build in 2026 look different from the decisions that were being made in 2022.

The historical default for hyperscale data centres - Northern Virginia, Phoenix, parts of the Pacific Northwest - is increasingly saturated. The interconnection queues in those markets are long, the transformer wait times are at the upper end of the range, and the regulated-rate fights are most advanced. The new wave of investment is moving to places that have either large existing generation surplus, regulatory environments friendly to new load, or both. That includes parts of the upper Midwest near major hydroelectric and nuclear sources, parts of Texas with abundant wind and gas generation, and a small but growing number of international destinations including parts of the Nordic countries, parts of Canada near large existing hydro capacity, and parts of the Middle East where the combination of cheap energy and ambitious sovereign-fund backing has created new build-out programmes.

The other shift is toward co-located generation. The model labs and hyperscalers are no longer treating the grid as the default power source. Several of the largest announced deployments in 2025-2026 are explicitly tied to specific generation assets - new nuclear (small modular reactors and large light-water units), large gas-fired plants, and dedicated renewable build-outs with battery storage. The implication is that the data centre and the power plant are increasingly designed and financed together as a single project, which is a significant change from the historical model where the data centre just bought power from the grid like everyone else.

## The price story nobody wanted

The most politically consequential part of the AI energy story is the part affecting consumer electricity prices.

US retail electricity prices have risen approximately 42% since 2019, against a CPI increase of approximately 29% over the same period. The rate of increase has accelerated in 2025-2026 as the demand growth from data centres has started showing up in the rate base. Goldman Sachs projects that AI-driven data centre demand will add approximately 0.1% to core inflation in 2026 and 2027 - small in the aggregate but concentrated in the household electricity bills of consumers who are not benefiting in any direct way from the AI build-out.

The political response is starting. Several states have proposed legislation requiring data centres to pay rates that reflect the full marginal cost of the infrastructure they require, rather than the average cost rolled into the existing rate base. The Federal Energy Regulatory Commission has signalled it will scrutinise new large-load interconnections more carefully. The Inflation Reduction Act's incentives for new generation are starting to be conditioned on demonstrated load-balancing commitments. The trajectory is toward a regulatory environment that is friendlier to new generation paired with new load but less friendly to data centres that expect the grid to absorb their demand at average cost.

The implication for the model labs is that the cost of compute, in real terms, is going to include a significant new component - the cost of the power infrastructure dedicated to that compute. The numbers people use today, which often quote raw electricity rates, understate the true cost of new compute by something between 20% and 50%, depending on how the regulatory landscape settles over the next two years.

## What this means for the shape of the next decade

The reason the energy story is the story of the decade is that it changes what is possible at the frontier, not just what is expensive.

If the binding constraint is power and the timeline for new power is multi-year, the frontier-model build-out has to slow regardless of how much capital is willing to fund it. The labs that have already secured power for the build-out they are doing today have a window of advantage that is hard to close. The labs that have not have a structural problem that capital alone cannot solve. The current scramble for power purchase agreements, for sites with existing interconnection, and for partnerships with electricity producers is the visible consequence of this.

The other implication is that the cost of compute has stopped falling on the trajectory that the last decade established. The historical assumption - that the cost of inference would keep falling by roughly half every 12-18 months indefinitely - is now in tension with the energy cost component. Some of the cost is still falling (chips, model efficiency, software) but some of it is now rising (power, real estate, transformers), and the net trajectory depends on how the regulatory environment settles. The pricing pressure on the consumer-facing AI products is downstream of this and it is one of the reasons the [$20 subscription era](/ai/twenty-dollar-ai-era-is-over/) is ending.

The third implication is geopolitical. The countries that can deliver gigawatts of new compute capacity on shorter timelines have a real economic advantage over those that cannot, and the policy choices being made in 2025-2027 about nuclear permitting, grid investment, and regulatory streamlining are going to determine who gets to host the next wave of AI infrastructure. The current picture is favourable to the US, to a handful of Middle Eastern states, and to parts of Asia that have invested seriously in grid capacity. Most of Europe is significantly behind on this dimension, with the UK particularly badly positioned, and the consequence for the European AI industry is becoming a real conversation in EU policy circles.

## The controversial parts

Four claims in the AI-energy conversation deserve more pushback than they typically get.

The first is the claim that AI energy demand will continue to grow indefinitely at current rates. There is no historical precedent for any single workload category growing at 15-20% per year for a decade without either hitting a physical constraint or being supplanted by something else. The most plausible scenario is that the growth rate slows substantially before 2030, either because efficiency improvements in models and hardware reduce demand per unit of useful work, or because the energy and infrastructure constraints bind harder than the labs currently expect.

The second is the claim that AI demand will be offset by AI-enabled efficiency gains in the rest of the economy. This is the talking point most often used by AI executives when challenged on the energy footprint. The empirical case for this is real - AI is contributing to efficiency improvements in industrial processes, building management, and grid optimisation - but the magnitude is much smaller than the demand increase, and the time horizon on the efficiency gains is longer than the time horizon on the demand growth. The two will eventually offset each other on some timescale, but not on the timescale that determines whether the grid can supply the build-out.

The third is the claim that small modular reactors and large-scale renewable build-outs will solve the problem within the relevant time horizon. SMRs are real, the announced deployments are credible, but the lead times are 5-10 years from now to first power. Large-scale renewables can be built faster but the interconnection queue and the firming capacity for intermittent generation are real constraints. The honest answer is that the energy supply that will meet the 2026-2028 AI demand is mostly already-built generation being repurposed or marginally expanded, and the new build-outs are part of the answer for 2028-2032 rather than for the near term.

The fourth is the claim that the energy crisis is fundamentally a regulatory problem and that streamlining permitting would solve it. The regulatory environment is real and matters, but the physical bottlenecks - transformers, transmission infrastructure, generation lead times - would not disappear even with a perfect regulatory environment. The pace of physical infrastructure construction is the real constraint and it is not something policy can fully eliminate even with significant political will.

## Where this is heading

The most likely shape of 2028-2030 is that the AI energy build-out becomes one of the largest single infrastructure programmes any major economy has run since the post-war period, and that the costs of it are distributed unevenly across consumers, taxpayers, and the AI customers themselves. The political economy of that distribution is going to be a major topic in US, EU, and UK politics for the rest of the decade, and the outcome will materially affect what AI deployment actually looks like.

For people building with AI today, the practical implication is mostly indirect. Cost-of-compute trajectories will be less favourable than the last decade conditioned us to expect. Capacity constraints will affect the availability of frontier models more often than the price card on the API page suggests. The geographic distribution of where compute happens will become more diverse as the model labs respond to where the power is. And the policy environment around AI will be increasingly entangled with the policy environment around energy, in ways that are going to surprise the AI industry's lobbyists for the next several years.

The energy story is the story of the next decade because it is the constraint capital cannot relieve. It is also the story that does not feature in the marketing pitch for any frontier-model product, which is itself a useful signal of how the conversation is being managed.

## Related Reading

- [Token Economics: Why the Cost of AI Isn't Going Down](/ai/token-economics-why-costs-arent-going-down/) - the cost-of-compute story the energy constraint sits inside.
- [Cerebras, Groq, SambaNova: The Inference Hardware Insurgents](/ai/inference-hardware-insurgents/) - the chip-side response to the same efficiency pressure the energy story creates.
- [Stargate](/ai/microsoft-openai-stargate/) - the most visible large-scale AI infrastructure programme tied directly to the dynamics this post describes.
- [Is the $20 AI Subscription Era Over?](/ai/twenty-dollar-ai-era-is-over/) - the consumer-pricing consequence of the cost-of-compute trajectory.
- [Four Futures for the Machine-Speed Economy](/ai/four-futures-machine-speed-economy/) - the broader scenarios the energy story is one of the binding constraints inside.
