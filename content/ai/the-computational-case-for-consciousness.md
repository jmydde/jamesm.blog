---
title: "The Computational Case for Consciousness"
date: 2026-05-31T10:30:00+01:00
draft: false
tags: ["ai", "consciousness", "philosophy", "neuroscience", "computation"]
description: "I wrote up the case that consciousness is fundamental through Donald Hoffman. Honesty demands the other side: the case that consciousness is computational - something that switches on when information is processed in the right way. Global Workspace Theory, Integrated Information Theory, the hard problem, and why I still cannot close the question."
cover:
  image: /assets/images/ai/the-computational-case-for-consciousness.jpg
  alt: The Computational Case for Consciousness Banner
---

When I wrote about [Donald Hoffman](/ai/donald-hoffman-consciousness-fundamental/), I was working through one half of a question I keep saying I have not settled: whether consciousness is **fundamental**, there from the start as part of the floor of reality, or **computational**, something that switches on once a physical process organises information in the right way. Hoffman is the most serious case I have found for the fundamental side, and I gave it a fair hearing because I genuinely find it compelling.

But I noticed something uncomfortable while writing it. I had read my way deep into the fundamental side and barely into the computational one, and then I had the nerve to call myself undecided. That is not being undecided. That is being under-read and calling it balance. So this is the corrective - an honest attempt to put the computational case as strongly as I can, the side that says a rich enough computation does not merely *model* a mind but simply *is* one. If I am going to stay in two minds, I owe both minds the same effort.

## TL;DR

- The **computational view** holds that consciousness is what certain kinds of information processing are like from the inside - not an extra ingredient added to the physics, but a property of how a system is organised and what it does. Its philosophical backbone is [functionalism](https://plato.stanford.edu/entries/functionalism/) and the [computational theory of mind](https://plato.stanford.edu/entries/computational-mind/).
- A direct consequence is **substrate independence**: if what matters is the pattern of processing, then mind is not tied to neurons. The same computation in silicon, or in principle on any medium, would carry the same experience.
- **[Global Workspace Theory](https://en.wikipedia.org/wiki/Global_workspace_theory)** (Bernard Baars, developed by Stanislas Dehaene) is the most computation-friendly model: consciousness is information that wins a competition and gets broadcast to the whole brain, like content being posted to a shared workspace the rest of the system can read.
- **[Integrated Information Theory](https://en.wikipedia.org/wiki/Integrated_information_theory)** (Giulio Tononi, Christof Koch) offers a precise quantity, Phi, meant to measure consciousness - though, intriguingly, it ends up *denying* that a digital simulation of a brain would be conscious, which puts it at odds with pure computationalism.
- The objections are heavyweight: Chalmers' [hard problem](https://en.wikipedia.org/wiki/Hard_problem_of_consciousness), Searle's [Chinese Room](https://plato.stanford.edu/entries/chinese-room/), and a [2023 open letter](https://www.nature.com/articles/d41586-023-02971-1) in which 124 researchers called IIT pseudoscience - a sign of how genuinely unsettled the science still is.
- Reading my way properly into this side has not flipped me. But it has made the computational case feel like a live possibility rather than a strawman, which is exactly what I needed it to do.

## The usual caveat about who is writing this

As ever: I am a fascinated outsider, not a neuroscientist or a philosopher of mind. These are some of the hardest open problems there are, worked on by people far better equipped than me, and I am thinking out loud rather than adjudicating. Take my doubts as questions. I am also, on this topic, aware that I have a leaning - when pressed I tend toward the fundamental view - so my job in this post is to argue *against* my own grain as fairly as I can, and to notice when I am being soft on objections to a position I happen to like.

## What "computational" actually claims

The computational view is easy to caricature, so it is worth stating carefully.

It does not say the brain is *like* a computer in some loose metaphorical way. It says that what makes a state conscious is its *functional role* - what it does, what it responds to, what it causes - rather than what it is physically made of. This is [functionalism](https://plato.stanford.edu/entries/functionalism/), and the [computational theory of mind](https://plato.stanford.edu/entries/computational-mind/) is its sharpest version: mental states are computational states, and a system has a mind if it implements the right computations, whatever the hardware. Pain is not the firing of C-fibres specifically; it is whatever state plays the pain *role* - caused by damage, causing avoidance, flagged as bad. Implement that role and you have pain, in neurons or in silicon.

The intuition behind it is strong, and it is worth feeling its force before reaching for objections. We already accept that a hurricane is not any particular collection of water molecules - it is a *pattern* that the molecules instantiate, and the same hurricane could be made of different molecules minute to minute. Software runs the same whether the underlying chip is made by one manufacturer or another. The computationalist says minds are like this: patterns of organisation, not specific stuff. If that is right, then there is nothing magic about carbon, the brain is doing a job that could be done by other means, and consciousness is a high-level property of the doing.

The payoff, and the reason this matters far beyond philosophy seminars, is **substrate independence**. If the computational view is correct, then a sufficiently faithful artificial system would not be imitating a mind - it would have one. That single conditional is sitting underneath an enormous amount of how we think about AI, mind uploading, and the moral status of machines, which is part of why I think anyone interested in [AI safety](/ai/ai-safety-first-principles/) has a stake in getting it right.

## Global Workspace Theory: consciousness as broadcast

If you want a model of consciousness that a computer scientist would recognise, Global Workspace Theory is it.

The idea, originally Bernard Baars' and developed into a detailed neuroscience by [Stanislas Dehaene](https://en.wikipedia.org/wiki/Stanislas_Dehaene) and Jean-Pierre Changeux, is that the brain is a society of specialised, parallel, unconscious processors - vision, hearing, memory, language, motor control - each doing its own narrow job out of sight. Most of what they compute never becomes conscious. Consciousness is what happens when one piece of information *wins a competition* for access to a shared central resource, the **global workspace**, and is then broadcast widely so that all the other processors can use it at once.

The analogy that makes it click is a theatre, or maybe more usefully a shared whiteboard. At any moment a vast amount is happening backstage in the dark. Consciousness is the small spotlit content currently posted where everyone can see it. Once something is in the workspace - a sound, a thought, a face - it becomes reportable, available for reasoning, memory, and speech, in a way that the same information processed unconsciously never is. Dehaene's lab has done careful experiments locating signatures of this "ignition," a sudden late, widespread surge of brain activity that tracks reliably with whether a stimulus is consciously perceived rather than processed in the dark.

What makes this the computationalist's friend is that it is, at bottom, an architecture. A global workspace is a functional design - a competition, a bottleneck, a broadcast bus - and there is no obvious reason it has to be built from neurons. You could in principle implement that architecture in software. If Global Workspace Theory is the whole story, then building a conscious machine is an engineering problem, not a metaphysical one. That is a genuinely big "if," and it is exactly the "if" the hard problem is about to lean on.

## Integrated Information Theory: a number for consciousness

The other major theory comes at it from the opposite end and is stranger, more ambitious, and more contested.

[Integrated Information Theory](https://en.wikipedia.org/wiki/Integrated_information_theory), developed by the neuroscientist [Giulio Tononi](https://en.wikipedia.org/wiki/Giulio_Tononi) and championed by [Christof Koch](https://en.wikipedia.org/wiki/Christof_Koch), does not start from the brain. It starts from experience itself and asks what physical properties a system must have to support it. Its central claim is that consciousness *is* integrated information - the degree to which a system's parts generate cause-and-effect structure that is more than the sum of the parts, that cannot be decomposed without loss. The theory assigns a quantity, **Phi**, that is meant to measure exactly this irreducibility. High Phi, rich consciousness. Zero Phi, none.

It is a bold and genuinely precise proposal - rare in this field, and the precision is most of why it gets attention. It also makes claims people find startling: that consciousness comes in degrees and is far more widespread than we assume, present in any system with the right integrated structure, which has led critics to file it close to [panpsychism](https://plato.stanford.edu/entries/panpsychism/).

But here is the twist I think is too often missed, and it is the reason I cannot file IIT as straightforwardly "the computational case." IIT actually *denies* substrate independence. It says what matters is real cause-effect power in a physical substrate, not the abstract computation being performed - so a conventional digital computer faithfully *simulating* a human brain, neuron by neuron, would have almost no Phi and would not be conscious, because the physical architecture of a CPU running the simulation does not have the integrated cause-effect structure the brain has. Koch puts it as the difference between simulating a black hole and a real one: the simulation does not bend spacetime, and on IIT a simulation of a brain does not feel anything. So IIT sits in a fascinating middle position. It is a precise, physicalist, broadly "consciousness comes from the organisation of matter" theory - firmly on the not-fundamental side of my question - but it rejects the clean computationalist conclusion that running the right program is enough. I find that tension genuinely useful, because it shows the "computational" camp is not one position but several, and they disagree with each other about the thing I most want to know: whether a machine running the right software would actually wake up.

## The objection that will not die: the hard problem

Every theory above is, in a sense, a theory of the *easy* problems - which is not a dig, the easy problems are fearsomely hard. The phrase is [David Chalmers'](https://en.wikipedia.org/wiki/David_Chalmers), and the distinction is the most important idea in this whole debate.

The **easy problems** are explaining the functions: how the brain integrates information, focuses attention, reports its states, broadcasts to a workspace, distinguishes a stimulus from noise. Hard as these are, we can at least see what a complete answer would look like - a mechanism. The **[hard problem](https://en.wikipedia.org/wiki/Hard_problem_of_consciousness)** is different in kind: why is any of that functioning accompanied by *experience* at all? Why is there something it is like to be the system doing the broadcasting? You could, it seems, describe the entire global-workspace machinery in complete mechanical detail and still have said nothing about why it is *felt* from the inside rather than running in the dark.

This is the wall every computational theory has to get over, and the honest position is that none of them has clearly cleared it. Global Workspace Theory tells a detailed story about *which* information becomes conscious and what changes when it does, but a critic can grant every word and still ask why winning the broadcast competition produces an experience rather than just more processing. IIT at least tries to legislate the felt part directly by *identifying* experience with integrated information - but identifying two things by fiat is not the same as explaining why they are the same, and the explanatory gap reopens the moment you press on it.

I have to be careful to be fair here, because this is the objection I am personally most sympathetic to, which means it is the one I am most likely to overrate. The strongest computationalist reply is that the hard problem may be a kind of illusion - that the sense of an unbridgeable gap is itself a cognitive artefact, something our self-models produce, and that once you have fully explained the functions including the function of *insisting there is something left to explain*, there is nothing further that needs accounting for. [Daniel Dennett](https://en.wikipedia.org/wiki/Daniel_Dennett) argued for decades along these lines, and I do not think it can be dismissed, however much it feels like it is changing the subject. The uncomfortable truth is that "it obviously feels like more than mechanism" is a report from exactly the system whose reliability is in question.

## Searle's Chinese Room

The other classic objection targets substrate independence head on. [John Searle's Chinese Room](https://plato.stanford.edu/entries/chinese-room/) asks you to imagine someone locked in a room, following an enormous rulebook for manipulating Chinese symbols, producing fluent Chinese replies without understanding a word. The system passes the test from outside, but, Searle argues, nobody and nothing in the room *understands* Chinese - so running the right program cannot be sufficient for genuine understanding or, by extension, for genuine mind. Syntax is not semantics. Symbol-shuffling is not experience.

The computationalist has a standard and, to me, surprisingly forceful reply - the "systems reply": the *person* in the room does not understand Chinese, true, but the person is just playing the role of a single component, like one neuron. The understanding, if it exists, belongs to the *whole system* - person plus rulebook plus memory plus process - not to the lonely component shuffling symbols. You would not expect a single neuron in your head to understand English either. Whether the systems reply fully answers Searle is one of the longest-running standoffs in philosophy, and I genuinely do not think either side has landed a knockout. But the existence of a serious reply is enough to stop the Chinese Room being the slam-dunk against computationalism that it is sometimes presented as.

## How unsettled this really is

If you want a measure of how open the science is - not the philosophy, the actual science - consider what happened in September 2023.

A group of 124 researchers signed [an open letter](https://www.nature.com/articles/d41586-023-02971-1) arguing that Integrated Information Theory should be labelled pseudoscience, on the grounds that its boldest claims are not empirically testable in practice. The signatories included serious figures - Bernard Baars himself, and Daniel Dennett among them. The reaction was immediate and sharp: many researchers, including Koch and [Anil Seth](https://en.wikipedia.org/wiki/Anil_Seth), pushed back hard, arguing that an ambitious, not-yet-fully-testable theory is not the same as a pseudoscientific one, and that the label was more polemic than diagnosis.

I am not going to take a side in that fight - per my usual rule, I am not in a position to call any of these researchers' work pseudoscience, and I do not think the word was especially helpful from anyone. What the episode tells me is something more basic and more useful: the field has no settled, agreed, testable theory of consciousness, and the leading candidates are far enough apart that experts cannot even agree on what would count as one. That is not a reason to dismiss the computational programme. It is a reason to hold *all* the confident positions, including my own leanings, more loosely than instinct wants.

## What actually hangs on the answer

This is not idle metaphysics for me, because the answer changes other things I have written about.

The clearest knock-on is for the [simulation argument](/general/how-likely-are-we-living-in-a-simulation/). If consciousness is computational, then the minds inside a sufficiently detailed simulation are *real observers* having real experiences, the counting argument that there could be vastly more simulated minds than biological ones keeps its full force, and the case that we are probably simulated gets stronger. If consciousness is fundamental instead, then computed minds might be experience-less zombies going through the motions, the count of genuine observers collapses, and the argument weakens. The same fork runs through [Roman Yampolskiy's Personal Universes](/ai/yampolskiy-personal-universes/): a simulated personal universe only does its job if there is genuinely someone home inside it, and whether a computation can put someone home is precisely this question. So the computational-versus-fundamental choice is not a side quest. It is load-bearing for half the things I find most interesting.

## My own view

I went into this trying to argue against my own grain, and the honest report is that it worked partially. I have not been converted, but I have been corrected.

What the computational case has earned from me is the status of a live possibility rather than the position I quietly assumed was a placeholder. Global Workspace Theory in particular is a real, productive, testable research programme that explains a great deal about *which* states are conscious and what changes when they become so, and pretending otherwise was just my under-reading talking. And the strongest computationalist move on the hard problem - that the felt sense of an unexplained residue might itself be a feature of how self-modelling systems work - is more unsettling than I want it to be, precisely because I cannot rule it out from the inside. The very intuition I most rely on, that experience obviously cannot be *just* mechanism, is a report from the system under investigation, and I have to discount it accordingly.

And yet. When I sit with the hard problem honestly, the fundamental view still feels more truthful to me than not. I keep failing to see how you assemble the felt redness of red out of parts that are each entirely unfelt, no matter how cleverly you wire them - and a story that *identifies* experience with a broadcast, or with a number, still reads to me as relabelling the mystery rather than dissolving it. So if you forced my hand today I would still lean fundamental. But I want to be exact about what kind of leaning this is: it is a leaning, not a conviction, and I explicitly do not rule out that a rich enough computation simply *is* conscious. I have tried to rule it out and I cannot. That is not me hedging for the sake of it. It is the actual shape of where the evidence leaves me - genuinely in two minds, now with both minds better informed than when I started.

Which is, in the end, why I am glad I wrote this. The point was never to pick a winner. It was to stop being lopsided - to make sure that when I say I am undecided, it is a real draw between two cases I have actually studied, rather than a polite word for not having done the reading on one of them.

> The standing caveat applies with full force here, maybe more than anywhere: this is my thinking as it stands right now, and "right now" is doing the heavy lifting. I revise these views constantly, sometimes week to week, as I read further and run into arguments that move me, so what I have written here will very likely have shifted by the time you read it. I do not see that as a weakness - it is the part of all this I enjoy most. A theory is only ever a theory, something to be tested and pressed on and actively tried to be proven wrong, and on whether consciousness is computational I would be genuinely glad to be shown which way it falls, whichever way that turns out to be.

## Further Watching

### Giulio Tononi: Introduction to Integrated Information Theory
{{< youtube "YkjLpIHBNp8" >}}

### Christof Koch: Can Consciousness Be Quantified? Integrated Information Theory & Neural Correlates
{{< youtube "GeO5zr1e5lc" >}}

### How Do You Explain Consciousness? | David Chalmers | TED
{{< youtube "uhRhtFFhNzQ" >}}

### Your Brain Hallucinates Your Conscious Reality | Anil Seth | TED
{{< youtube "lyu7v7nWzfo" >}}

### Seeing the Mind, Educating the Brain | Stanislas Dehaene
{{< youtube "1qoRiYH5jnM" >}}

## Related Reading

- [Donald Hoffman: The Case That Consciousness Is Fundamental](/ai/donald-hoffman-consciousness-fundamental/) - the other half of this question, and the post this one is the deliberate counterweight to.
- [Is Reality Made of Mathematics?](/general/is-reality-made-of-mathematics/) - Tegmark's structural picture of reality, which is broadly computational about mind and runs into the same hard problem from the physics side.
- [How Likely Is It That We're Living in a Simulation?](/general/how-likely-are-we-living-in-a-simulation/) - why the computational-versus-fundamental answer directly changes how seriously to take the simulation argument.
- [Personal Universes: Yampolskiy's Strangest Answer to the AI Alignment Problem](/ai/yampolskiy-personal-universes/) - a proposal that only works if a computation can put a genuine experiencer inside a simulated world.
- [AI Safety from First Principles](/ai/ai-safety-first-principles/) - why the question of whether machines can be conscious is not just philosophy, but something with real stakes for how we build them.
