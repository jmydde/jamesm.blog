---
title: "Space Debris Is a Tragedy of the Commons - Here's the Math"
date: 2026-05-03T20:00:00+01:00
draft: false
tags: ['space', 'debris', 'leo', 'kessler', 'satellite', 'sustainability', '2026']
description: "Low Earth orbit is filling up. The economics of space debris look exactly like a textbook tragedy of the commons - private benefits, shared costs, no pricing mechanism. A grounded look at the numbers behind Kessler syndrome and what would actually fix it."
cover:
  image: /assets/images/space/space-debris-tragedy-of-the-commons.jpg
  alt: Space Debris Tragedy of the Commons Banner
---

## TL;DR

- Low Earth orbit (LEO) in 2026 contains roughly **40,000 tracked objects** larger than 10cm and an estimated **1 million pieces** of debris between 1cm and 10cm. Most of it is dead satellites, spent stages, and fragments from past collisions or anti-satellite tests.
- The economics are a textbook **tragedy of the commons**. Each launch operator captures the upside of putting hardware in orbit. The cost of debris is shared across every other operator and every future mission. There is no global price on creating debris.
- The risk is non-linear. **[Kessler syndrome](https://en.wikipedia.org/wiki/Kessler_syndrome)** - a cascade where collisions create more debris that triggers more collisions - is not a hypothetical. We are already in the early stages in some altitude bands.
- The fix is also a textbook commons solution: **price the externality**. End-of-life deorbit requirements, debris remediation funds, transparent collision-avoidance markets, and active debris removal services. Some of this exists. Most of it is undersupplied.
- The realistic 2026 picture: not yet a crisis, on a trajectory that becomes one within a decade if nothing changes, with the most useful policy interventions being the ones that price debris creation directly rather than relying on goodwill.

## The Numbers

Order-of-magnitude figures, drawn from [ESA's space debris office](https://www.esa.int/Space_Safety/Space_Debris) and [LeoLabs](https://leolabs.space/) tracking data, as of 2026:

- **Tracked objects in orbit:** roughly 40,000.
- **Active satellites:** roughly 11,000 - of which around 7,000 are Starlink and similar megaconstellation members.
- **Estimated debris 1-10cm:** roughly 1 million.
- **Estimated debris under 1cm:** in the hundreds of millions.
- **Mass in orbit:** roughly 12,000 tonnes.

Each of these numbers is meaningful in its own way.

The **40,000 tracked objects** is the population that collision-avoidance systems actually know about. Most operational collision risk is calculated against this population.

The **1 million 1-10cm pieces** are mostly invisible to current tracking. They are large enough to destroy a satellite on impact and small enough that we cannot route around them. This is the actual lethal-but-untracked population.

The **hundreds of millions of sub-centimetre pieces** cannot destroy a satellite outright but can erode shielding, puncture solar panels, and degrade optics. They accumulate over time.

The **12,000 tonnes of mass** is the raw material from which future debris is made. Every collision turns active satellites or dormant stages into thousands of new pieces.

## Why It Looks Like A Commons Problem

A commons problem in the economic sense has four features:

1. A shared resource that everyone benefits from.
2. The resource is rivalrous - my use degrades it for you.
3. No mechanism prices the degradation.
4. Individual rational behaviour produces collective irrational outcomes.

Low Earth orbit ticks every box.

**Shared resource.** Orbital slots and altitude bands are accessible to anyone with launch capability.

**Rivalrous.** Every additional object increases collision risk for every other object. The risk is not zero-sum but it is shared.

**No price on debris.** A launch operator who deorbits responsibly pays the cost. A launch operator who leaves stages and dead satellites in orbit pays nothing. The cost is borne by everyone else.

**Individually rational, collectively destructive.** From a single operator's perspective, the cheapest path is "launch, operate, abandon." If everyone does that, LEO becomes unusable.

This is not a metaphor. It is the same structural problem as overfishing, atmospheric pollution, and groundwater depletion. The mathematical solutions are the same too.

## The Kessler Cascade

[Kessler syndrome](https://en.wikipedia.org/wiki/Kessler_syndrome) - named for Donald Kessler's 1978 NASA paper - is the runaway scenario where collisions create enough new debris that further collisions become inevitable, which create more debris, and so on. The end state is an altitude band so densely populated with debris that satellites cannot survive there.

The dynamics are:

- A debris piece hits a satellite or stage.
- The collision produces hundreds to thousands of new debris pieces, depending on the masses and relative velocity.
- Each new piece is itself a potential collider.
- Some of those will hit other objects, producing more pieces.

The threshold for self-sustaining cascade is altitude-dependent. Above about 600km, atmospheric drag is weak enough that debris persists for decades or centuries. Below 500km, drag deorbits debris in a few years. The high-risk band - 700km to 1000km - is exactly where many operational satellites and a lot of historical debris live.

The relevant 2026 estimates from ESA and other tracking organisations suggest that **some altitude bands are already past the threshold** at which the population is self-sustaining even without new launches. The cascade is not catastrophic yet, but the underlying dynamics no longer require new bad behaviour to keep producing debris.

## What Has Actually Happened

A few specific events define the modern debris picture.

**The 2007 Chinese ASAT test** destroyed the [Fengyun-1C satellite](https://en.wikipedia.org/wiki/2007_Chinese_anti-satellite_missile_test) and produced over 3,000 trackable fragments, most of which are still in orbit and will be for decades.

**The 2009 Iridium-Cosmos collision** - an active satellite hitting a defunct one - produced over 2,000 trackable fragments and was the first major accidental collision between two satellites.

**The 2021 Russian ASAT test** destroyed [Cosmos 1408](https://en.wikipedia.org/wiki/2021_Russian_anti-satellite_missile_test) and forced the ISS crew to shelter in their return capsules. Over 1,500 trackable fragments produced.

**The 2024 Long March 5B reentry incidents** raised concerns about uncontrolled large stage deorbits, even though those events removed mass from orbit rather than adding debris.

Each of these is a discrete event that contributed disproportionately to the overall picture. Most years do not have an event of this magnitude. But the long tail of routine launches with unrecoverable upper stages, dead satellites, and occasional minor collisions is also continuously adding to the total.

## What Would Actually Fix It

The economic toolkit for solving commons problems is well understood. Applied to space debris:

### Pricing the externality

The most direct fix is to **charge launch operators a fee proportional to the expected debris contribution of their mission**. Operators who deorbit cleanly pay less. Operators who leave stages in orbit pay more. The fee creates a financial incentive aligned with the social good.

Variants of this exist as proposals. Some form of orbital-use fee has been studied by economists and floated in policy circles. None has been implemented at international scale.

### Mandatory deorbit and end-of-life rules

The [FCC's 5-year rule](https://www.fcc.gov/document/fcc-adopts-new-5-year-rule-deorbiting-satellites) for US-licensed satellites in LEO is a meaningful step. It requires deorbit within five years of mission end rather than the previous 25-year guideline. Other regulators are following.

These rules cover a meaningful share of new launches but not all of them. A coordinated international rule with similar teeth is the natural next step.

### Active debris removal

Active debris removal (ADR) services - vehicles that go to specific debris objects, capture them, and deorbit them - are starting to appear as commercial offerings. [Astroscale](https://astroscale.com/), [ClearSpace](https://clearspace.today/), and a handful of others are developing the technology.

The economics are difficult. Removing a piece of debris costs millions. The benefit is shared across every operator. Without a pricing mechanism that captures the benefit, ADR is a niche service rather than a normal operation.

### Transparent collision-avoidance markets

Most close-approach data is currently held by national militaries. Operators get warnings but the warnings are not always timely or precise. A more transparent, commercial market for tracking data and collision-avoidance services would let operators react more efficiently to actual risk.

[LeoLabs](https://leolabs.space/) and similar commercial trackers are pushing in this direction.

### Insurance and liability

Insurance markets have started to price debris risk into satellite premiums. As the risk grows, premiums grow. This is one of the cleaner indirect pricing mechanisms - operators in higher-debris altitude bands pay more for insurance, which incentivises lower-debris choices.

Liability rules for in-space collisions are still murky. The [1972 Space Liability Convention](https://en.wikipedia.org/wiki/Convention_on_International_Liability_for_Damage_Caused_by_Space_Objects) was written for a different era. Updating it would help.

## What Megaconstellations Mean For The Math

The single biggest variable in the 2026 debris picture is the rapid growth of megaconstellations - Starlink, Project Kuiper, Guowang, OneWeb, and others.

Most of these constellations operate at low altitudes (around 500km) where atmospheric drag deorbits failed satellites in a few years. That is the responsible architectural choice. Combined with active deorbit at end of life, the contribution to long-lived debris is meaningfully smaller than the constellation's headline number suggests.

**However**, three risks scale with megaconstellation deployment:

**Conjunction frequency.** With tens of thousands of active satellites, the number of close approaches per day grows quadratically. Most are handled by automated avoidance. A small fraction are not.

**Individual failure rates matter more.** A 1% failure rate is fine when you have 100 satellites. It is alarming when you have 30,000.

**Atmospheric impact of routine deorbits.** Burning satellites release metals into the upper atmosphere. The long-term atmospheric chemistry effects are an active research area.

The honest picture is that megaconstellations done right are not the main debris problem. They could become the main problem if operators are not disciplined about end-of-life behaviour and if the satellite reliability does not keep pace with the population growth.

## What Would Convince Me Things Were Improving

Specific signals that the trajectory was actually changing:

- **A binding international agreement** with teeth on end-of-life deorbit timelines, not just guidelines.
- **A working orbital-use fee mechanism** in at least one major launching jurisdiction, with revenue going to debris remediation.
- **Routine commercial active debris removal missions** rather than one-off demonstrations.
- **Transparent public sharing** of conjunction data and avoidance manoeuvre counts across major operators.
- **A measured slowdown in tracked-object growth** in the highest-risk altitude bands.

A few of these are happening. Most are not. The overall trajectory is "awareness rising, action lagging."

## The Honest Verdict

Low Earth orbit is not yet ruined. It is being used in ways that, continued unchanged, will ruin it within a decade or two for the most valuable altitude bands.

The fix is not technical. The fix is economic. Treat debris like a pollutant, price it accordingly, and the rational behaviour of operators will follow. Treat it like a free externality and the commons will be exhausted on schedule.

The pattern across every other commons we have managed - fisheries, forests, atmospheric emissions - is that the policy gets serious only when the cost of inaction starts being clearly larger than the cost of action. We are not there yet for orbital debris, which is exactly why the next few years are when the cheap solutions are still possible.

The window is open. It is not infinite. The math says it closes.

## Related Reading

- [Artemis III Lander Architecture - What Could Still Go Wrong](/space/artemis-iii-lander-architecture/)
- [China's Space Programme in 2026 - Tiangong, Chang'e, Lunar Plans](/space/china-space-programme-2026/)
- [SpaceX Starship vs NASA SLS](/space/spacex-starship-vs-nasa-sls/)
- [Why Spacecraft Don't Slow Down Before Reentry](/space/why-spacecraft-dont-slow-down-before-reentry/)
- [Human Spaceflight Rockets 2026](/space/human-spaceflight-rockets-2026/)
