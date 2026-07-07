---
title: "Astronomy in the Era of Giant Constellations: The Starlink Problem"
date: 2026-05-13T02:00:00+01:00
draft: true
tags: ["space", "astronomy", "satellite"]
description: "The night sky in 2026 has tens of thousands of satellites in low Earth orbit, and that number is going to keep climbing. A practical look at what this is actually doing to professional astronomy, what the mitigations are achieving, and where the unresolved tensions remain."
cover:
  image: /assets/images/space/space-debris-tragedy-of-the-commons.jpg
  alt: Astronomy in the era of giant satellite constellations - the Starlink problem
---

For most of human history the night sky has been the most stable thing in our experience. The same constellations, in roughly the same positions, for tens of thousands of years. That stability ended around 2019 when SpaceX began launching Starlink satellites in significant numbers, and the change has accelerated since. By 2026 there are tens of thousands of active satellites in low Earth orbit, with announced plans pushing toward hundreds of thousands by the end of the decade across Starlink, OneWeb, Amazon's Project Kuiper, Chinese constellations, and others.

The implications for professional astronomy are real and have been the subject of significant debate. Three years into the era of giant constellations, it is possible to assess what has actually changed, what mitigations are working, and what remains unresolved.

## What is actually being affected

The impact on astronomy is uneven across different kinds of observation:

**Wide-field optical surveys** are the most heavily affected. The [Vera C Rubin Observatory](https://rubinobservatory.org/), which began full operations in 2025, observes wide swaths of sky with sensitive optics - exactly the configuration that picks up the maximum number of satellite trails. Studies suggest 30-50% of Rubin's exposures will contain at least one satellite trail at the current constellation density, rising to higher percentages as more launches happen.

**Radio astronomy** has a different problem. The Starlink constellation operates at frequencies that interfere with sensitive radio observations, including some of the bands that radio astronomers care about for cosmological and galactic studies. The interference is not just from satellites passing directly overhead - radio leakage from neighbouring frequencies and harmonics creates noise across a wider band than the satellite's designated transmission.

**Long-exposure deep-field imaging** can usually be processed to remove satellite trails, at the cost of some data and significant processing overhead. The data loss is real but manageable for most projects.

**Time-domain astronomy** - observations that need to catch transient events at specific moments - is meaningfully affected when satellite passes coincide with critical observation windows. The probability of interference at any given moment is non-trivial and growing.

**Visual amateur astronomy** has been hit in ways that are culturally meaningful but technically less critical. The familiar appearance of the night sky from a dark location now includes multiple visible satellite trails on most nights. The experience of stargazing is materially different from what it was a decade ago.

## What the mitigations are actually doing

SpaceX has implemented several mitigations under pressure from the astronomy community, with mixed results:

**Darkened satellites.** The DarkSat experiment and the subsequent VisorSat design reduce satellite reflectivity. The current generation Starlink satellites are roughly 2-5 times less bright than the original 2019 satellites. This is helpful but not sufficient - the satellites are still visible and still cause trails in long-exposure imaging.

**Orbit positioning.** Newer satellites are positioned at altitudes that reduce visibility during twilight hours, which is when most astronomical observation happens. The improvement is real but partial.

**Observation coordination.** SpaceX provides predicted satellite positions to major observatories so observation schedules can avoid the worst windows. This works for planned observations but does not help with time-critical events.

The improvements have prevented the worst-case outcomes that were predicted in 2020, but they have not eliminated the impact. The total satellite count is growing faster than the per-satellite impact is shrinking.

## What the regulatory picture looks like

The regulatory response has been slower and weaker than the astronomy community has called for:

**The US FCC** has authority over satellite licensing but has not used it to set meaningful constraints on satellite brightness or quantity. The licensing process treats interference with astronomy as a consideration but not a binding constraint.

**The International Astronomical Union** has been vocal about the impacts but has no regulatory authority. Their work has produced good documentation of the impacts and useful tools for observatories to manage their work around the constellations.

**The UN Committee on the Peaceful Uses of Outer Space** has discussed the issue but produced no binding agreements. International coordination on satellite brightness standards remains aspirational.

**National astronomy funding bodies** (NSF in the US, ESO in Europe) have funded mitigation research and observatory upgrades but have limited leverage over commercial satellite operators.

The honest assessment is that the regulatory framework has not caught up with the rate of constellation deployment, and is unlikely to do so before the next major scale-up of launches.

## What the constellations actually provide

Worth being fair to the constellation operators: the services they provide are real and significant.

Starlink and similar constellations have brought broadband internet access to populations that had no realistic alternative. Rural communities, ships at sea, aircraft, remote scientific stations, areas with poor terrestrial infrastructure. The connectivity revolution from low-earth-orbit constellations is meaningful, and the benefits are widely distributed.

The argument for the constellations is not that they are harmless to astronomy - they are not - but that the benefits to human connectivity outweigh the costs to astronomical observation. This is a real argument, not a dismissal, and the resolution of it involves judgement about how to weigh competing legitimate interests.

The astronomy community's response has generally not been to argue that the constellations should not exist. It has been to argue that the impacts could be reduced significantly with relatively modest design changes, and that there should be regulatory frameworks to ensure those design changes happen across all operators rather than depending on the goodwill of individual companies.

## Where this is heading

Several things are likely to develop in the next few years:

**The constellation count will keep growing.** Starlink alone has approved plans for 42,000 satellites; the Chinese Guowang constellation is targeting tens of thousands; Project Kuiper, OneWeb, and several others are in various stages of deployment. The night sky has more satellites coming, not fewer.

**Space-based observatories will become more important.** Hubble, JWST, and the upcoming Habitable Worlds Observatory are above the constellation orbits and unaffected. Ground-based observation will increasingly focus on what space-based instruments cannot do.

**Adaptive processing will improve.** Better algorithms for removing satellite trails from images, better prediction tools for scheduling around passes, better data quality assessment in the presence of interference. These do not fix the problem but reduce its impact.

**The political conversation will continue.** As the impacts become more visible and the science community continues to document them, regulatory pressure will likely increase. Whether this produces binding constraints on operators remains genuinely uncertain.

## The bigger pattern

The deeper issue is one that this generation is the first to face seriously: the night sky is a shared global resource that cannot be effectively protected by any single nation's regulations. The constellations operate from many countries, serve customers in many more, and affect astronomical observation regardless of where the observatories are located. The institutional frameworks for managing genuinely global shared resources are weaker than the frameworks for managing national ones, and the satellite constellation case is exposing that gap clearly.

The same gap is going to matter for [space debris](/space/space-debris-tragedy-of-the-commons/), for lunar surface activity, for asteroid mining, and for any number of other emerging space activities. The constellations are the first major case where the gap has been felt by a specific affected community. They are unlikely to be the last.

## Related Reading

- [Space Debris: Tragedy of the Commons](/space/space-debris-tragedy-of-the-commons/)
- [The Commercial Space Stations Race](/space/commercial-space-stations-race/)
- [SpaceX Starfactory](/space/spacex-starfactory/)
- [Human Spaceflight Rockets 2026](/space/human-spaceflight-rockets-2026/)
- [Lunar Gateway](/space/lunar-gateway/)
