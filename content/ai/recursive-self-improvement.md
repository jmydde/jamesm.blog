---
title: "Recursive Self-Improvement: Can AI Bootstrap Its Own Intelligence?"
date: 2026-06-04T20:03:00+01:00
draft: false
tags: ["ai", "agi", "safety", "alignment", "research", "superintelligence"]
description: "Recursive self-improvement is the idea that an AI could rewrite itself into something smarter, then repeat - the engine behind every intelligence-explosion scenario. Here is what the theory actually claims, which pieces are already real in 2026, the bottlenecks that decide whether it runs away or fizzles, and why the honest answer is partly, slowly, and not the way the science fiction tells it."
cover:
  image: /assets/images/ai/recursive-self-improvement.png
  alt: Recursive Self-Improvement - Can AI Bootstrap Its Own Intelligence? Banner
---

## TL;DR

- **Recursive self-improvement (RSI)** is the idea of an AI that improves its own ability to improve - each round producing a smarter system that does the next round better. It is the engine behind every "intelligence explosion" story since [I.J. Good described it in 1965](https://en.wikipedia.org/wiki/Technological_singularity)
- The **narrow version is already real**. Systems like [AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) and [the AI Scientist](https://sakana.ai/ai-scientist/) measurably improve algorithms, code, and even research output - including, in AlphaEvolve's case, the infrastructure that trains the models themselves
- The leap people fear is different: **improving an algorithm is not the same as improving general intelligence**. Nothing in 2026 has crossed that line, and the gap is structural, not just a matter of scale
- Four bottlenecks decide whether RSI runs away or fizzles: **compute, data, verification, and diminishing returns**. Each is a hard physical or informational limit, not a temporary engineering nuisance
- The realistic picture is **steady, human-paced acceleration** - AI assisting AI research - not an overnight takeoff. [METR's time-horizon data](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) shows fast but smooth exponential progress, which is exactly what a bottlenecked process looks like
- In May 2026 **Anthropic put numbers on this from inside a frontier lab**. Its essay [*When AI Builds Itself*](https://www.anthropic.com/institute/recursive-self-improvement) reports that over 80% of the code it merges is now written by Claude, that task horizons are doubling every roughly four months rather than seven, and lays out a candid three-way bet on where this ends. None of it overturns the bottlenecked-flywheel picture - but it sharpens it
- It still deserves serious safety attention, because a slow takeoff is the one we can actually govern

There is a particular shape of argument that has haunted artificial intelligence since before the field had a settled name. It goes like this: build a machine slightly better than humans at designing machines, and it will design a machine better than itself. That machine designs a better one. The loop tightens, each turn faster than the last, and intelligence runs away from us in an afternoon.

The argument is old, and it is more precise than the popular version suggests. In 1965 the statistician I.J. Good [wrote the canonical statement of it](https://en.wikipedia.org/wiki/Technological_singularity): an "ultraintelligent machine" that "can far surpass all the intellectual activities of any man however clever." Since designing machines is itself an intellectual activity, such a machine could design even better machines. "There would then unquestionably be an 'intelligence explosion'," Good wrote, "and the intelligence of man would be left far behind." He added a caveat that the next sixty years of AI safety research never managed to discharge: all of this holds "provided that the machine is docile enough to tell us how to keep it under control."

In 2026 the question is no longer purely philosophical. We have systems that genuinely improve code, algorithms, and research artefacts, and at least one that has been pointed at the infrastructure used to train frontier models. So it is worth asking the question carefully rather than rhetorically: can AI bootstrap its own intelligence, and if so, how fast, and where does it stop?

## What recursive self-improvement actually means

It helps to be exact, because the term gets used loosely. [Recursive self-improvement](https://en.wikipedia.org/wiki/Recursive_self-improvement), strictly defined, is a process in which an AI system improves *its own capacity to improve*. That second-order quality is the whole point. An AI that gets better at chess is not doing RSI. An AI that gets better at making AIs that get better at chess is closer. An AI that gets better at the very process of making itself better is the real thing.

The standard framing imagines a "seed improver" - a starting system, written by humans, that can plan, write, test, and run code, and is given the goal of producing a more capable version of itself. Run that once and you get version two. The hope, or the fear, is that version two is not just more capable in general but specifically better at the improvement task, so version three arrives faster and is a bigger jump. Iterate, and the curve bends upward without limit.

The crucial word is *recursive*. Ordinary AI progress is fast but human-driven: researchers have ideas, run experiments, publish, and the next team builds on the result. That is a loop, but humans are the rate-limiting step in it. RSI is the claim that the loop can close on itself - that the AI becomes the researcher, and once it does, the human-paced clock no longer applies. Everything interesting about the scenario, good and bad, comes from removing humans from the loop.

## The narrow version is already happening

Here is the part that should make a sceptic pause. The components of self-improvement are not hypothetical. They exist, they ship, and they work.

[AlphaTensor](https://deepmind.google/blog/discovering-novel-algorithms-with-alphatensor/), published by DeepMind in 2022, treated the discovery of matrix-multiplication algorithms as a game and found schemes that beat the best human-designed methods - the first improvement on Strassen's classic algorithm, in a specific setting, in over fifty years. Matrix multiplication is the operation at the heart of every neural network. An AI found a faster way to do the thing AIs are built out of.

[AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/), announced in 2025, generalised the idea. It pairs Gemini models with automated evaluators and an evolutionary loop, and points the result at real engineering problems. It found a better task-scheduling heuristic that recovers, on average, around 0.7% of Google's global compute. It sped up a key kernel in Gemini's own architecture by 23%, cutting Gemini's training time by roughly 1%. Read that again: an AI system improved the software used to train the AI system. That is not the full RSI loop, but it is unmistakably one revolution of it.

And [the AI Scientist](https://sakana.ai/ai-scientist/) from Sakana AI ([paper here](https://arxiv.org/abs/2408.06292)) attacks the research process itself - generating hypotheses, writing code, running experiments, and drafting papers end to end, at a cost the team put at a few dollars per paper. A later version produced a manuscript that cleared a peer-review acceptance bar. The quality is uneven and the controversy is real, but the direction is not in doubt.

The most striking data point of 2026 is not from a public benchmark, though, but from inside a frontier lab. In May, Anthropic published [*When AI Builds Itself*](https://www.anthropic.com/institute/recursive-self-improvement), an unusually candid account of its own development loop. The headline numbers: as of that month, more than 80% of the production code Anthropic merged was written by Claude, up from single digits before February 2025, with engineers shipping roughly eight times more code per quarter than the 2021 baseline. One example stuck with me - in April 2026, Claude shipped over 800 fixes that cut a class of API errors by a factor of a thousand, work the supervising engineer estimated would have taken a human four years. The loop is no longer something happening to AI in a research paper; it is the daily mechanics of how the next model gets built.

So the honest answer to "can AI improve the things AI is made of" is: yes, and it already does. The narrow loop is closed.

## Why improving an algorithm is not improving intelligence

And yet none of this is the intelligence explosion. The gap between what AlphaEvolve does and what Good described is not a gap of degree. It is a gap of kind, and it is worth being precise about why.

AlphaEvolve optimises *within a fixed search space*. You hand it a problem with a clear objective - make this kernel faster, schedule these jobs better - and it explores the space of solutions efficiently. That is enormously valuable, and it produces real, compounding gains. But the search space does not expand because AlphaEvolve searched it. The next problem is just as hard to start on as the last one. The system gets you better answers; it does not get fundamentally better at the act of getting answers in a way that carries across domains.

Recursive self-improvement, the runaway kind, requires something stronger: each generation must expand its own capability frontier, so that the *space of improvements it can even conceive of* grows with each turn. A faster matrix multiply does not do that. It makes training cheaper, which is useful, but cheaper training of the same architecture yields the same kind of model. Nothing in 2026 has demonstrated the second-order effect - a system whose improvements make its *next* improvements qualitatively larger rather than merely cheaper.

This matters because the explosive scenario depends entirely on that second-order effect. If each round of self-improvement yields a constant or shrinking increment, you get progress, even fast progress, but you get a curve that flattens. You only get a true explosion if the increments grow. The burden of proof sits on that specific claim, and right now it is unmet.

## The four bottlenecks

If self-improvement does not run away, something must be stopping it. Four things are, and none of them is a temporary inconvenience.

**Compute.** The runaway story quietly assumes that getting smarter is free once you are smart enough to want it. It is not. Every capability jump of the last decade has cost dramatically more compute than the last, and compute is brutally physical: fabrication plants that take years to build, [data centres whose electricity demand is now a constraint on the grid itself](/ai/ai-energy-crisis-data-center-power/). An AI that wants to train its successor cannot think its way past a power station. It has to wait for one, on human timescales, subject to supply chains it does not control. The smartest possible scheduler still cannot run a training job on hardware that does not exist yet.

**Data.** Capability has been fuelled by enormous quantities of high-quality human text, and the best of that corpus is largely consumed. The obvious workaround - have the model generate its own training data - runs into [model collapse](/ai/synthetic-data-model-collapse/): train a system mostly on its own output and quality degrades rather than compounds. A self-improving AI cannot simply imagine the new information it needs. Genuinely new knowledge about the world has to come from the world, through experiment and observation, and that is slow.

**Verification.** This is, to me, the deepest bottleneck and the least discussed. To improve itself, a system must be able to *tell* that a candidate change is genuinely an improvement. AlphaTensor and AlphaEvolve work precisely because their domains come with cheap, exact verifiers: a matrix-multiplication scheme is either correct or not, a kernel is either faster or not. Those are gifts. Now ask the question that RSI actually requires: "is this modified version of me *more generally intelligent*?" There is no cheap verifier for that. Evaluating general capability is expensive, noisy, and contested - we [struggle to evaluate models we already have](/ai/reasoning-models-2026/). A self-improvement loop can only run as fast as it can score its own outputs, and for the thing that matters most, scoring is the slow step.

**Diminishing returns.** Even inside a single tractable domain, the easy wins go first. AlphaEvolve's 23% kernel speed-up is real and will not be repeated every quarter; the second 23% is harder to find than the first, and the tenth may not exist. Compounding works both ways. A loop only explodes if each round's gain holds up. If the gains shrink - which is the normal behaviour of optimisation in a finite space - the loop converges instead of detonating.

## What the trend actually looks like

We do not have to argue this purely from theory, because the trajectory is being measured. [METR](https://metr.org/), a nonprofit that evaluates frontier AI, tracks what it calls the **time horizon**: the length of task, measured in how long it takes a human, that a model can complete with 50% reliability. [Their finding](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) is that this horizon has been doubling roughly every seven months for years, with current frontier models handling tasks that take a skilled human a couple of hours.

That is a fast curve, and Anthropic's essay argues it has got faster: it reports the doubling time tightening from roughly seven months to roughly four, with Claude Opus 3 handling tasks that take a human about four minutes and Opus 4.6 reaching toward twelve-hour tasks. A shorter doubling time is precisely what you would expect once AI starts meaningfully helping to build AI - the loop's first observable effect is to bend its own curve. So this is the moment to watch the *shape* most carefully. Even at four months it is still a clean exponential - quick, but smooth, regular, and forecastable. A genuine intelligence explosion would not look like that. It would look like a discontinuity: the curve bending sharply upward and then leaving the chart. What the data shows instead, even on the accelerated reading, is exactly the signature of a fast process running into resistance - a system pushing hard against compute, data, and verification limits, and advancing steadily because those limits give way steadily.

That is the most important empirical point in the whole debate. The honest reading of the evidence is not "no self-improvement" and not "imminent foom." It is *bottlenecked acceleration*: real, compounding, and quick by historical standards, but legible and paced rather than explosive.

## What Anthropic thinks happens next

What I find valuable about [*When AI Builds Itself*](https://www.anthropic.com/institute/recursive-self-improvement) is that it does not pretend to know the answer. Instead it lays out three futures and declines to bet the house on any of them. The first is a **plateau**, where the curves flatten as supply constraints - compute, energy, fabrication - bite harder than any intelligence limit. The second is **continued efficiency gains**, where development is largely automated but humans keep setting direction, and a hundred-person team does the work of a far larger one. The third is **full recursive self-improvement**, where models acquire enough research judgement to design their own successors and progress is gated mainly by available compute. Anthropic's own verdict on the runaway case is worth quoting in spirit: it is, they say, uncertain and "not inevitable." Coming from the lab with the most to gain from hyping it, that restraint is telling.

The hinge between those futures is a phrase Anthropic uses that maps almost exactly onto my own list of bottlenecks: **research taste**. Their internal evidence is that Claude is already excellent at *executing* well-specified experiments - they cite speedups of more than 50x against a human baseline - and increasingly good at *proposing* them, recovering most of the performance gap on some safety research. What it cannot yet do reliably is the judgement part: choosing which problem is worth attacking, knowing when a result is interesting rather than merely correct. That is the [verification bottleneck](#the-four-bottlenecks) wearing a different hat. A system can only improve itself as fast as it can tell good directions from bad ones, and "good research direction" has no cheap, exact verifier the way a faster matrix multiply does. I would put it more strongly than the essay does: research taste is not one bottleneck among several, it is the master one, because it is the thing the runaway scenario most needs and the thing we are least able to score.

The other half of the essay is a governance proposal, and it deserves engagement rather than reflexive cynicism. Anthropic argues that a unilateral slowdown by one lab is close to useless - it just hands the frontier to someone less cautious - so the only meaningful lever is *verifiable global coordination*, and it commits to pausing or slowing its own development "if other developers at or near the frontier also did so in a verifiable manner." I think the honesty here is real and the difficulty is being slightly undersold. Building the verification infrastructure that would let one lab trust another's pause is an arms-control problem, and arms-control regimes have historically taken decades to stand up, over much slower-moving technology. The window the essay says is open now is open against a clock it does not control. Still, naming the coordination problem precisely is more than most of the field manages, and it is the right problem to be naming.

## The safety question does not go away

It would be a mistake to read all this as reassurance and move on. A slow takeoff is not a safe takeoff. It is a *governable* one, which is a different and more valuable thing.

The frontier labs already treat AI accelerating AI research as a specific, named threshold rather than a vague worry. [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/rsp) is built around capability thresholds that trigger stronger safeguards, and the ability of a model to meaningfully speed up AI R&D is exactly the kind of capability that regime is designed to catch before it compounds. METR's evaluations explicitly probe for it. The reason for the attention is straightforward: even a non-explosive loop, left unmonitored, removes humans from the part of the process where judgement and course-correction live.

And Good's caveat still stands, unanswered. A system that is genuinely improving itself is, by construction, a moving target for oversight - the thing you reviewed last month is not the thing running today. Researchers like [Roman Yampolskiy](/ai/roman-yampolskiy/) argue this is not a solvable engineering problem at all but a structural one: control gets harder precisely as the system gets more capable. You do not have to accept the strong version of that claim to accept the weak one, which is enough to be going on with: the slower the takeoff, the more chances we get to notice a problem and act. That is an argument for using the time, not for relaxing.

## Where the gains plausibly stop, and where they do not

So, can AI bootstrap its own intelligence? The accurate answer has two halves, and both matter.

The science-fiction version - a seed AI that rewrites itself into a god over a weekend - is not supported by anything we can currently see. It depends on a second-order effect, improvements that make future improvements larger, that has never been demonstrated, and it has to overcome four bottlenecks that are physical and informational rather than merely technical. You cannot optimise your way past a power station, an empty data well, or the absence of a way to score the thing you are trying to maximise. The runaway loop is a coherent idea that the world does not currently seem to be arranged to permit.

But the dismissive version - "AI does not self-improve, relax" - is just as wrong, and lazier. AI is already a junior collaborator in its own development. It is writing the kernels, scheduling the clusters, drafting the experiments, and trimming the cost of the next training run. The loop is not closed at the level of general intelligence, but it is unmistakably turning at the level of tools and infrastructure, and each turn makes the next one slightly cheaper.

The mental model I have settled on is not an explosion and not a wall. It is a **flywheel**. It is heavy, it has real momentum now, and every push moves it a little more easily than the last - but humans are still the ones pushing, the bottlenecks still set the pace, and the speed is measured in years, not afternoons. That is a far less cinematic picture than the intelligence explosion. It is also the one the evidence actually supports, and crucially, it is the version we still have time to steer. The task is to use that time well, because a flywheel that is still accelerating is not one to look away from.

## Related Reading

- [Reasoning Models in 2026: o3, R2, and the Compute-at-Inference Shift](/ai/reasoning-models-2026/)
- [AI Safety From First Principles: What Actually Matters vs What's Hype](/ai/ai-safety-first-principles/)
- [Roman Yampolskiy: The Researcher Who Thinks AI Cannot Be Controlled](/ai/roman-yampolskiy/)
- [Synthetic Data and Model Collapse: The Quiet Crisis in Training Data](/ai/synthetic-data-model-collapse/)
- [The Next Decade of AI: What Actually Happens From Here](/ai/the-next-decade-of-ai/)
