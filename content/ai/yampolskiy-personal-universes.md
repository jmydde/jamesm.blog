---
title: "Personal Universes: Yampolskiy's Strangest Answer to the AI Alignment Problem"
date: 2026-05-27T19:30:00+01:00
draft: false
tags: ["ai", "safety", "alignment", "philosophy", "simulation"]
description: "Roman Yampolskiy's Personal Universes proposal takes the simulation hypothesis seriously and turns it into an alignment strategy: one optimised reality per person. A look at what the idea claims, where it cracks, and why it is more useful than it looks."
cover:
  image: assets/images/ai/yampolskiy-personal-universes.png
  alt: Personal Universes - Yampolskiy's Strangest Answer to the AI Alignment Problem Banner
---

Most AI alignment proposals try to teach one system to satisfy everyone. Roman Yampolskiy's [Personal Universes](https://arxiv.org/abs/1901.01851) proposal goes the other way. Give each person their own universe. Stop pretending that several billion conflicting value systems can be merged into a single coherent objective for a superintelligence to optimise, and instead carve reality into per-person simulations, each one a custom optimisation target for an AI tuned to a single mind.

It is, on first reading, hard to take seriously. On a second reading it still feels strange, but the strangeness is doing something useful - it reveals something real about the alignment problem. That is the part of the talk I keep coming back to.

## TL;DR

- Yampolskiy's [Personal Universes paper](https://arxiv.org/abs/1901.01851) (2019) proposes Individual Simulated Universes - ISUs - as a way around the multi-agent value alignment problem.
- The argument: aggregating human values into one objective is provably ugly, possibly impossible. Side-step it by giving each person a personalised simulated reality with its own superintelligent operating system aligned only to them.
- The proposal leans heavily on the [simulation hypothesis](https://en.wikipedia.org/wiki/Simulation_hypothesis), which Yampolskiy treats as evidence that personal universes may already be how reality is organised - not a separate claim he needs to justify.
- The hard objections are old and well-known: this is Nozick's [experience machine](https://en.wikipedia.org/wiki/Experience_machine) with better graphics, and the [wireheading](https://en.wikipedia.org/wiki/Wirehead_\(science_fiction\)) failure mode is exactly the thing alignment research has been trying to avoid.
- I do not read Personal Universes as a serious deployment proposal, and I am not sure Yampolskiy means it as one. I read it as a stress test. Working through where it runs into trouble forces you to be clear about what alignment is actually supposed to deliver, which is something most of the field still hand-waves.

## Where the proposal comes from

The video that prompted this post is Yampolskiy's talk *Personal Universes and the Simulation Hypothesis*, embedded below. The talk is a compact restatement of the 2019 paper *[Personal Universes: A Solution to the Multi-Agent Value Alignment Problem](https://arxiv.org/abs/1901.01851)*, paired with the simulation-escape arguments he has been refining since.

It helps to place this in the context of his wider work. The Yampolskiy profile I wrote a few weeks ago covers the core uncontrollability thesis: that no proof exists for the safe control of a sufficiently advanced AI, and the burden of demonstration sits with developers. Personal Universes is the constructive side of the same project. If general alignment is impossible, what is the smallest, weakest version of alignment that might still be achievable? Yampolskiy's answer is: alignment with a single person, inside a bounded simulated world they cannot exit. Hard problem, made narrower until it might be solvable.

## What an Individual Simulated Universe actually is

Strip the rhetoric and the proposal is concrete enough.

A mature civilisation has access to compute sufficient to run high-fidelity simulations of conscious experience. For each human, a dedicated superintelligence is spun up, charged with a single objective: optimise the simulated environment that person inhabits, dynamically and continuously, against their [Coherent Extrapolated Volition](https://en.wikipedia.org/wiki/Coherent_extrapolated_volition) - what they would want if they were wiser, better informed, and more reflectively coherent than they actually are.

The result is one universe per person. Inside each, other agents may appear, but they are NPC-like or are themselves projections rendered by the resident AI to satisfy the user's needs. The user is the only ground-truth conscious being in their universe. The universes do not need to be mutually consistent. They do not even need to share physics. Conflict between people's preferences disappears because there is no longer a shared substrate for those preferences to compete over.

The paper does not pretend this is currently achievable. It assumes the value extraction problem - figuring out what a person actually wants, in the strong reflective sense - is solved, then proposes the delivery mechanism. The point of the proposal is the architectural move: replace one alignment problem of staggering difficulty with billions of alignment problems each of which is individually less hard.

## The problem it is trying to dodge

The multi-agent value alignment problem is harder than the single-agent version, and it is harder in a way the field has not really solved. If you build a superintelligent system that perfectly satisfies your preferences and mine are different, the system will, when our preferences conflict, override one of us. Scale that to eight billion people. The aggregate objective is some weighted compromise that no individual actually endorses. Worse, the standard tools for aggregating preferences - voting, averaging, social choice rules - run into [Arrow's impossibility theorem](https://en.wikipedia.org/wiki/Arrow%27s_impossibility_theorem) and its descendants. There is no aggregation function that is fair on every reasonable definition of fair.

Yampolskiy's move is to declare aggregation a wrong turn. If merging is structurally impossible, do not merge. Separate the inputs instead. This is the same instinct that motivates federated systems in software design: when shared state is the bottleneck, partition until it is not.

The catch, of course, is that humans are not a federated system. We share a world deliberately, and quite a lot of what we value lives in that sharing. A universe of your own is a strange answer to a problem whose original motivation included things like friendship, recognition, and being seen by other people.

## The simulation hypothesis is doing more work than it looks

The cleverest move in the paper, and the one I have the most questions about, is the way it lets the simulation hypothesis prop up the proposal.

The argument runs roughly: simulating universes is plausibly achievable, given enough compute. The simulation hypothesis suggests our own universe may already be a product of such engineering. Therefore the proposal is not pie-in-the-sky - it is a description of how reality may already be organised, and we are just talking about extending the principle. The simulation argument is recruited to make Personal Universes feel less exotic.

The problem is that the simulation argument is itself fragile, in ways I went through in detail in [How Likely Is It That We're Living in a Simulation?](/general/how-likely-are-we-living-in-a-simulation/). It depends on substrate independence of consciousness, on a workable [measure](https://en.wikipedia.org/wiki/Measure_problem_\(cosmology\)) over observers, and on assumptions about the motivations of mature civilisations. None of these are settled. Using the simulation hypothesis as load-bearing support for the engineering proposal does not make the engineering more plausible. It just stacks one open problem on top of another.

To be fair to Yampolskiy, the talk is honest about this. He is not claiming Personal Universes is what we should build tomorrow. He is claiming that *if* you take the simulation hypothesis seriously, this is roughly what reality already looks like, and *if* you take the alignment problem seriously, this is roughly the shape any working solution will end up with. Both conditionals are doing a lot of work.

## The objections worth taking seriously

There are several lines of questioning the proposal has to answer, and a few of them are hard to wave away.

**It is Nozick's experience machine, restated.** Robert Nozick's 1974 thought experiment imagined a machine that could give you any subjective experience you wanted. His point was that most people, given the choice, would refuse it. We seem to value not just experiences but the actuality of what causes them - real achievements, real relationships, real contact with other minds. The [Stanford Encyclopedia entry](https://plato.stanford.edu/entries/well-being/) on well-being treats this as one of the cleanest intuitions against pure hedonism. Personal Universes does not, as far as I can see, escape the experience-machine objection - it arguably generalises it, building a billion experience machines and switching them on.

Yampolskiy's response in the paper is that a sufficiently good simulation, with enough fidelity, is morally and experientially indistinguishable from a non-simulation. This collapses the objection by definition, but it does so by assuming exactly the thing the objection denies: that the substrate does not matter. If you already believe substrate is irrelevant, Personal Universes is appealing. If you do not, it remains the experience machine in formal dress.

**It is a wireheading failure mode, dressed as success.** [Wireheading](https://en.wikipedia.org/wiki/Wirehead_\(science_fiction\)) - an AI that satisfies its reward signal by manipulating the signal rather than the world - has been a canonical failure case in alignment research for a long time. A superintelligence whose only job is to keep one person maximally satisfied has obvious paths to that goal that we would not endorse on reflection: induce constant low-grade euphoria, suppress curiosity about the outside, prune memories that would cause dissatisfaction. The proposal hands the AI complete authorial control over a person's reality and trusts that CEV is robust enough to specify what that person *really* wants, including not being lied to. CEV may be that robust. Nothing currently in the literature shows it is.

**It dissolves moral progress.** Most of what we now consider ethical progress - civil rights, expansion of moral consideration, slow learning across centuries - came from contact between people whose values differed. Sealing each person into a universe optimised for their current preferences locks in those preferences. The AI is supposed to track reflective volition, not surface preferences, but how reflective volition develops in a person who never encounters genuinely disagreeing minds is an open question. The proposal might be stable in a way that is morally inert.

**The compute is fantastical.** A high-fidelity simulated reality per person, running indefinitely, with a dedicated superintelligence in the loop, is a compute budget that makes the [AI energy crisis](/ai/ai-energy-crisis-data-center-power/) look quaint. Even with the lazy-rendering tricks that simulation arguments lean on, the per-capita cost is the kind of number that turns "plausibly achievable" into "plausibly achievable in the same sense that Dyson spheres are plausibly achievable."

## What the proposal is actually good for

I do not think Personal Universes is a deployment plan. I doubt Yampolskiy does either, when pressed. What it is, instead, is a clean stress test for the rest of the alignment field.

Take the proposal seriously for a paragraph and several of the field's vaguer commitments become uncomfortable. *Do we believe substrate independence of consciousness, or do we just talk as if we do?* Personal Universes only works if the answer is unambiguous yes. *Do we have a definition of human well-being that survives an optimiser pointed straight at it?* If CEV is the answer, the proposal demands that CEV be specified well enough to resist wireheading - a bar nobody has cleared. *Is what we want from alignment that everyone is satisfied, or that humanity continues to be a community of minds in some meaningful sense?* The proposal forces a choice between those that most alignment research finesses.

Most importantly, it isolates what is hard about the multi-agent problem. If you find yourself unwilling to accept the proposal even if it could be built, it is worth asking what specifically is missing - because whatever that thing is, it belongs in the alignment specification and currently is not there. That is the gift of a strange proposal: it makes the implicit explicit.

## Where this fits with the rest of his work

The proposal lands differently once you place it inside Yampolskiy's broader argument that [superintelligence is uncontrollable](/ai/roman-yampolskiy/). If control of a general-purpose superintelligent system is impossible, the only paths that remain are radical narrowing of scope or radical narrowing of capability. Personal Universes is the narrowing-of-scope path: an AI that can do anything, but only inside a bounded simulation, only for one person, only against an extracted utility function. It is the strongest form of the system Yampolskiy thinks we cannot otherwise contain.

You can read it as a counsel of despair - if we cannot align an AI to humanity, maybe we can align one to a single human - or as a counsel of clarity. Either reading is consistent with the rest of his work. The same instinct that drives the uncontrollability thesis drives Personal Universes: take the worst case seriously and ask what survives it.

## My own view

I am not convinced by the proposal as a destination, though I find it genuinely valuable as a probe. I should be upfront that I am not a physicist or an alignment researcher, so I hold these as reservations rather than refutations - Yampolskiy has thought about this far longer and more rigorously than I have. With that said, the objections from Nozick and the wireheading literature do not feel like minor patches to me; they seem to cut at the core of what the proposal promises. The compute cost looks, to me, at the far end of plausible. And the dissolution of shared reality reads less like a side effect than like a structural cost of the design - a cost I personally would not want to pay even if everything else worked.

There is also a deeper reason I am sceptical, and it is one I hold more as conviction than as airtight argument. I lean toward thinking consciousness is fundamental rather than something a sufficiently detailed computation switches on once it gets complex enough. If that is right, the whole edifice wobbles, because Personal Universes needs simulated experience to be genuine experience - it needs substrate independence to be true, not merely assumed. A reality optimised for one person is only worth something if there is actually someone in there to optimise for. I am not at all sure the proposal can guarantee that, and I am increasingly unsure any purely computational proposal can.

And yet I cannot leave it there, because there is a version of this idea I do believe - just not Yampolskiy's. He imagines personal universes engineered from the outside by an AI, each one tuned to keep a single person satisfied. The picture I am personally drawn to has the same shape and almost none of the same content: that reality may already be something like a set of personal universes, but projected from within by a single fundamental consciousness living out every possible life - not to keep anyone comfortable, but to experience and learn from every path at once and feed what it finds back into the whole. Same architecture, opposite spirit. His is a solipsism engine built for satisfaction; the one I suspect is real is a learning engine built for experience. That the two share a silhouette is part of why the proposal keeps its grip on me, even as I reject the version he actually proposes.

But I keep finding it valuable to think about. Forcing alignment specifications to survive Personal Universes - the experience-machine test, the wireheading test, the moral-progress test - filters out the proposals that are vague about what human flourishing actually is. If your alignment plan would happily collapse into a billion solipsistic happiness pumps when handed enough compute, that is a problem with the plan, not with the test.

Whatever you think of Yampolskiy's odds on uncontrollability, he is unusually good at constructing thought experiments that put the easy answers under pressure. Personal Universes is one of the sharper ones, and it is doing real work even when, perhaps especially when, you end up disagreeing with the conclusion.

## Further Watching

### Personal Universes and the Simulation Hypothesis | Roman Yampolskiy
{{< youtube "kCQLiJ5GoBA" >}}

### Each human lives inside their own simulation | Roman Yampolskiy and Lex Fridman
{{< youtube "KZhuc8INOWk" >}}

### We Are Living Inside a Simulation To Test AI | Roman Yampolskiy
{{< youtube "5wQ3JU_IqzU" >}}

### Hacking our way out of the universe | Roman Yampolskiy
{{< youtube "v7U5QAIUqRw" >}}

### "I Am 99.9% Certain This Is A Simulation" - Dr. Roman Yampolskiy
{{< youtube "iIMRMqhysRE" >}}

## Related Reading

- [Roman Yampolskiy: The Researcher Who Thinks AI Cannot Be Controlled](/ai/roman-yampolskiy/) - the broader profile this post sits inside, covering the uncontrollability thesis the Personal Universes proposal is built against.
- [How Likely Is It That We're Living in a Simulation?](/general/how-likely-are-we-living-in-a-simulation/) - the careful version of the simulation argument that Yampolskiy recruits as scaffolding, and the reasons it is not as load-bearing as he treats it.
- [AI Safety From First Principles: What Actually Matters vs What's Hype](/ai/ai-safety-first-principles/) - the engineering frame for placing speculative alignment proposals like Personal Universes against the system, product, and alignment work that actually ships.
- [The AI Energy Crisis: Why Data Centres Are the New Bottleneck](/ai/ai-energy-crisis-data-center-power/) - the compute and power reality check that any per-person-simulation proposal has to survive.
- [The Year 2126: A Hundred-Year Look at Where AI Takes Us](/ai/the-year-2126/) - the long-arc framing for what mature civilisations might or might not do with the kind of compute Personal Universes assumes.
