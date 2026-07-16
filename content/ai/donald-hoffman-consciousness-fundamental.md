---
title: "Donald Hoffman: The Case That Consciousness Is Fundamental"
date: 2026-05-29T10:30:00+01:00
draft: false
tags: ["ai", "consciousness", "philosophy", "physics", "multimodal"]
description: "Donald Hoffman argues that consciousness is fundamental and the physical world is an evolved interface - and he tries to prove it with evolutionary game theory and a formal mathematics of conscious agents. A walk through the argument, the maths, the objections, and why I keep coming back to it."
cover:
  image: /assets/images/ai/donald-hoffman-consciousness-fundamental.jpg
  alt: Donald Hoffman - The Case That Consciousness Is Fundamental Banner
---

When I wrote about [Yampolskiy's Personal Universes](/ai/yampolskiy-personal-universes/) recently, I left a thread hanging. The question underneath that whole post - the one I said I genuinely had not settled - was whether consciousness is fundamental, there first with the universe as something it experiences, or whether it is computational, something that switches on once a process gets complex enough. I said I had only recently started reading my way into the fundamental side, mostly through Donald Hoffman. This is me pulling on that thread properly.

Hoffman is a cognitive scientist at UC Irvine, and what makes him unusual is not the conclusion - philosophical idealism, the idea that consciousness rather than matter is the bedrock of reality, is old. What is unusual is the route. He does not arrive at it through pure metaphysics. He arrives at it through evolutionary game theory and a formal mathematics of what he calls conscious agents. Whether or not the maths does what he says it does, the attempt to *formalise* idealism rather than simply assert it is what holds my attention.

## TL;DR

- Hoffman's argument builds in stages, each one trying to earn the next. It starts in evolution and ends in a mathematics of consciousness.
- The **[Fitness-Beats-Truth theorem](https://link.springer.com/article/10.1007/s10441-020-09400-0)** is the entry point: in evolutionary simulations, organisms tuned to fitness reliably outcompete organisms tuned to seeing reality accurately. Perception evolved to guide useful behaviour, not to report truth.
- From there comes the **Interface Theory of Perception**: what we see is a species-specific desktop of icons, not a window onto reality. This is explicitly *not* simulation theory - there is no external programmer.
- Hoffman then leans on theoretical physics - the [amplituhedron](https://en.wikipedia.org/wiki/Amplituhedron) and the work of [Nima Arkani-Hamed](https://en.wikipedia.org/wiki/Nima_Arkani-Hamed) - to argue that **spacetime is not fundamental**, which clears the ground for the radical step.
- That step is **Conscious Realism**: consciousness is the only primitive, and the physical world is a network of interacting conscious agents. Brains do not produce consciousness; consciousness gives rise to brains.
- He formalises a conscious agent as a **six-tuple** of [Markov kernels](https://en.wikipedia.org/wiki/Markov_kernel) and a counter, and claims this framework solves the [combination problem](https://plato.stanford.edu/entries/panpsychism/) and is Turing-complete.
- The maths is contested. Showing a *correspondence* between his structures and known physics is not the same as *deriving* physics from consciousness, and even Hoffman calls his framework "a precise hypothesis that, of course, might be precisely wrong." That honesty is part of why I take it seriously.

## Why I find this worth the effort

I should be upfront, as I always am with this stuff: I am not a physicist or a cognitive scientist. I hold what follows as a fascinated outsider working through someone else's ideas, not as anyone qualified to adjudicate the maths. Hoffman has spent decades on this and I have spent weeks. Treat my reservations as questions, not refutations.

What pulled me in is that Hoffman is doing the thing I keep wishing more people in these debates would do. Idealism usually arrives as assertion - *consciousness is primary, matter is derivative, here is why that feels right.* Hoffman tries to make it cash out in equations and predictions. He may fail. But a falsifiable attempt at idealism is rarer and more useful than another confident sentence about the primacy of mind, and I would rather engage with something that can be wrong than something that cannot.

## Step 1: Fitness beats truth

The argument starts with a claim about evolution that is more unsettling the longer you sit with it.

Hoffman and his collaborators ran evolutionary game simulations pitting organisms that perceived the world accurately against organisms that perceived only what mattered for survival. The accurate perceivers lost, and they lost reliably. The formal result, the **[Fitness-Beats-Truth theorem](https://link.springer.com/article/10.1007/s10441-020-09400-0)**, is that a strategy tuned to maximise expected fitness, making no attempt to estimate the true state of the world, generically dominates a strategy tuned to truth - and the dominance grows as the perceptual world gets richer.

The intuition behind it is almost mundane. Truth takes energy. Tracking the full structure of reality is expensive, and evolution punishes waste. If a stripped-down, functional shortcut keeps you alive and reproducing just as well, the shortcut wins. So perception is shaped to guide adaptive behaviour, not to estimate a pre-existing physical truth.

The implication is the radical part. The tomato on your plate - its redness, its roundness, its thereness - is not a reading of objective reality. It is an evolved shortcut. Colour, shape, distance: adaptive icons, not measurements. You do not see the world as it is. You see a functional, stripped-down interface that hides whatever is actually going on underneath.

## Step 2: The Interface Theory of Perception

That last word is the bridge to the next step. Hoffman calls our perceptual world an **interface**, and the analogy he reaches for is the computer desktop.

The blue rectangular icon for a file you are editing is not blue, not rectangular, and not the file. The file is voltages and magnetic states scattered across hardware you will never see. The icon is a deliberate, useful lie - it lets you act without knowing any of that. Hoffman's claim is that our entire sensory world works this way. Space, time, objects, colours: icons on a species-specific desktop, evolved to let us act, actively hiding the underlying reality precisely so we do not have to deal with it.

It is worth being clear about what this is *not*, because the obvious comparison is misleading. This is not [simulation theory](/theories/how-likely-are-we-living-in-a-simulation/). A simulation needs a programmer, a substrate, a layer of base reality running the code. Hoffman's interface has no external programmer. The interface is not generated by some computer in a deeper physical world - on his view consciousness itself is the architect, and there is no deeper physical world for the computer to sit in. This distinction matters a lot later, and it is the cleanest line between Hoffman and someone like Yampolskiy, whose [Personal Universes](/ai/yampolskiy-personal-universes/) proposal assumes exactly the engineered, substrate-based picture Hoffman rejects.

## Step 3: Spacetime is not fundamental

If the interface hides reality, what is reality? Hoffman's first move is to argue that it is not spacetime, and here he borrows from theoretical physics rather than cognitive science.

He points to work by physicists like [Nima Arkani-Hamed](https://en.wikipedia.org/wiki/Nima_Arkani-Hamed) on structures such as the [amplituhedron](https://en.wikipedia.org/wiki/Amplituhedron) and the cosmological polytope. These are geometric objects that let physicists compute particle scattering amplitudes far more efficiently than the standard spacetime-based machinery, and crucially they do it *without reference to space or time at all*. The physics that comes out is the same; the spacetime scaffolding turns out to be optional. Hoffman reads this as a hint from physics itself that spacetime is not bedrock - that it may be, in his language, an evolved perceptual interface rather than the foundation of the universe.

I want to flag the seam here, because it is the one critics press on hardest, and rightly. That physicists can compute amplitudes without spacetime is a real and striking result. That this *implies* spacetime is a perceptual construct generated by consciousness is a much larger inference, and the physicists doing the amplituhedron work do not generally draw it. Hoffman is borrowing the suggestiveness of the physics without the physicists necessarily signing on to the metaphysics. That is allowed - but it is worth seeing the join.

## Step 4: Conscious Realism

With spacetime demoted, Hoffman makes the ontological move the whole structure has been building toward. He calls it **Conscious Realism**: consciousness is fundamental, and what we call the physical world is a network of interacting conscious agents.

This is a clean inversion of the standard scientific picture. The default assumption - so default we rarely notice it is an assumption - is that matter and spacetime are the foundation, and consciousness somehow *emerges* from physical processes in the brain once they get complicated enough. That emergence is the famous [hard problem](https://en.wikipedia.org/wiki/Hard_problem_of_consciousness): nobody has a remotely satisfying account of how electrochemistry becomes the felt redness of red. Hoffman's response is to refuse the problem at the root. Brains do not produce consciousness. Consciousness produces brains, and tables, and electrons, and spacetime itself - these are how conscious agents appear to one another through the interface.

It is a big swallow. But notice that it dissolves the hard problem rather than solving it. If consciousness is fundamental, there is no mystery about how it arises from matter, because it does not arise from matter - matter arises from it. You trade one hard problem for the burden of explaining everything physics already explains, in new terms. Which is exactly what the maths is for.

## Step 5: The mathematics - conscious agents as six-tuples

This is where Hoffman stops gesturing and starts defining, and it is the part I find most interesting even where I cannot fully follow it.

He defines a **conscious agent** not as a brain or an organism but as an abstract mathematical object - a **six-tuple** characterised entirely by what it does: perceive, decide, act. In the formalism from [*Objects of Consciousness*](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00577/full) (Hoffman and Prakash, 2014), an agent is built from:

- An **experience space (X)** - the set of possible conscious experiences or qualia available to the agent.
- An **action space (G)** - the set of actions it can take.
- A **perception map (P)** - a [Markov kernel](https://en.wikipedia.org/wiki/Markov_kernel) from the world W to experiences X.
- A **decision map (D)** - a Markov kernel from experiences X to actions G.
- An **action map (A)** - a Markov kernel from actions G back to the world W.
- A **counter (N)** - an integer tracking the sequence of experiences, which is where Hoffman tries to get time *out* of the dynamics rather than assuming it.

The use of Markov kernels - probability distributions governing transitions between states - is the deliberate bit. Each interaction between an agent and its world is modelled as a message passed over a channel: world to perception, perception to decision, decision to action, action back to world, round and round. Consciousness, on this account, is fundamentally about structured information flow, and the agent is whatever sits at the nodes doing the perceiving and acting. No physical substrate is mentioned anywhere in the definition, which is the whole point.

## Step 6: The combination problem and fusing agents

Any theory that makes consciousness fundamental runs straight into the **[combination problem](https://plato.stanford.edu/entries/panpsychism/)**: if the basic stuff of reality is little conscious things, how do they combine into the rich, unified consciousness you are having right now? This is the objection that has dogged panpsychism for a century, and Hoffman claims his maths answers it directly.

Given two agents C₁ and C₂, he defines a **fusion operation** that produces a new agent C₃ whose kernels are specified combinations of the kernels of the originals. The fused agent has access to both perception channels and both action repertoires - a genuine enlargement of capacity rather than two agents merely running side by side. Qualia fuse to make new qualia. Agents combine into richer agents and, going the other way, can decompose into simpler ones.

The dynamics of *n* agents, in his framework, form a high-dimensional **Markov polytope**, and Hoffman argues the whole construction is Turing-complete - that conscious-agent dynamics can compute anything computable, in the same sense the [Church-Turing thesis](https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis) makes the Turing machine universal. And the recursion runs all the way up: agents combining into agents, retaining their identities, climbing toward agents of unbounded richness. As he puts it, "that's where we start to get theological, because we now have infinite consciousnesses."

I will admit that line is where my own attention sharpens rather than wanders, for reasons I will come back to.

## Step 7: Mathematics as part of the bones of consciousness

There is a further claim Hoffman makes that I find quietly radical, separate from the agent formalism. He argues that mathematics is not merely a *tool* for describing consciousness from the outside - it is intrinsic to consciousness, part of its structure. Seeing a circle, he says, is already a structured experience involving the ratio of circumference to radius. "In every experience there is mathematics throughout." Maths is part of the bones of consciousness, not a language we invented to point at it.

I notice I have to be careful here, because this one lands close to something I already believe, and "it agrees with me" is not evidence. I have written before that I lean toward maths being fundamental rather than invented, and Hoffman's framing fits that like a glove. So I am deliberately discounting how persuasive it feels. Still, set against the older Platonic intuition that mathematical truths exist independently of any mind, Hoffman's version - maths as the structure of mind itself - is a genuinely different and interesting move, and I would like to understand it better than I currently do.

## Step 8: Trying to recover physics from agents

The most technically ambitious part of the project - and the most contested - is the attempt to recover physics *from* conscious-agent dynamics rather than the other way around. Hoffman proposes a correspondence between the Markov polytopes describing agent dynamics and the on-shell diagrams that physicists use to generate scattering amplitudes, mapping his Markov chains onto the decorated permutations and combinatorial structures that show up in the amplituhedron programme.

The payoff he is reaching for is that quantities like position, momentum and energy stop being fundamental facts about a physical universe and become *properties of interacting conscious agents* - readouts of the interface rather than features of the bedrock. If it worked all the way, it would be physics derived from consciousness, which would be an extraordinary result.

Here is the honest summary of where it stands, and it is the crux of the whole critical case against him. A *correspondence* between two mathematical structures is not a *derivation* of one from the other. That Hoffman can map agent dynamics onto the same combinatorics that appear in scattering amplitudes is suggestive, but showing two formalisms share a skeleton does not show that one generates the other, nor that consciousness is doing the generating. The maths might be pointing at something deep, or it might be a coincidence of structure dressed up as an explanation. To his real credit, Hoffman says this himself - his framework is, in his words, "a precise hypothesis that, of course, might be precisely wrong." I find that more convincing than certainty would be.

## The whole argument at a glance

| Layer | Claim | Mechanism |
|---|---|---|
| Evolutionary | Perception tracks fitness, not truth | Fitness-Beats-Truth theorem |
| Perceptual | Our reality is a species-specific interface | Interface Theory of Perception |
| Physical | Spacetime is not fundamental | Amplituhedron, cosmological polytope |
| Ontological | Consciousness is the only primitive | Conscious Realism |
| Mathematical | Agents are Markov six-tuples | Kernel composition, Markov polytopes |
| Combination | Rich consciousness from agent fusion | Kernel products, Turing-completeness |

Each row is meant to earn the next. The honest reading is that the top rows are stronger than the bottom ones: the evolutionary and perceptual claims are arguments many people find compelling even if they reject the conclusion, while the recovery of physics from agents is, for now, a promissory note.

## My own view

I land in a familiar place: genuinely unsettled, and content to be. The question I flagged in the Yampolskiy post - fundamental consciousness or computational consciousness - is exactly the one Hoffman forces, and reading him has not resolved it for me so much as sharpened what each answer would cost.

What I find strongest is the front of the argument. Fitness-beats-truth is a real result with a clear intuition behind it, and the interface idea follows naturally enough that I cannot dismiss it. The claim that our perceptions are useful constructions rather than transparent reports of reality seems to me more likely true than not, and you do not have to be an idealist to accept it - plenty of straightforwardly physicalist cognitive scientists accept some version of it. So the first two steps I am fairly persuaded by.

What I cannot yet judge is the back of the argument, where the load-bearing weight sits. The leap from "physicists can do without spacetime in some calculations" to "spacetime is a perceptual construct of consciousness" is large, and I notice the physicists themselves mostly do not take it. And the recovery of physics from agent dynamics, the part that would actually distinguish Hoffman's idealism from a poetic restatement of it, is the part still owed. A correspondence is not a derivation. Until that gap closes I have to file the strong conclusion as fascinating and unproven, however much I enjoy it.

I also want to be honest about a pull I feel and am trying not to be moved by. Hoffman's picture rhymes with things I already lean toward - maths as fundamental, and that line of his about the recursion running up to infinite consciousnesses, where it "starts to get theological." That sits unnervingly close to my own intuition about a single underlying consciousness, and it connects to the shape I reached at the end of the Personal Universes piece: reality as something like a set of personal universes projected from within by one fundamental consciousness living out every possible life. Hoffman's agents-fusing-into-ever-richer-agents is a different mechanism, but it points up the same ladder. The trouble is that "this agrees with what I already wanted to believe" is precisely when I should trust myself least, so I am holding the resonance at arm's length rather than treating it as support.

If I try to say something definite: I think Hoffman has the most serious attempt I have seen to make idealism do real work, and I think the verdict on whether it does that work is genuinely open. That is not a fence-sit for its own sake. It is where the evidence actually leaves me, and the part I enjoy is that working through his maths has made me clearer about *what would have to be true* for each answer to win, even though it has not told me which one does.

> The usual caveat, which matters more on this topic than most: this is my current thinking, and "current" is the operative word. I revise this stuff constantly as I read more, and the version I hold today will probably have shifted by next month. A theory is only ever a theory - something to be tested and actively tried to be proven wrong - and on the question of whether consciousness is fundamental I would be genuinely glad to be shown which way it falls, whichever way that is.

## Further Watching

### What's Outside The Simulation? w/ Donald Hoffman | Impact Theory
{{< youtube "EykaPqzzdQg" >}}

### The Greatest Discovery About Reality & the Consciousness Behind It | Donald Hoffman
{{< youtube "xaeafKPfs1M" >}}

### Fusions of Consciousness | Donald Hoffman Technical Interview
{{< youtube "cSk5l1BOvts" >}}

### Donald Hoffman: Consciousness May Be Fundamental to Physics
{{< youtube "12PZQrDbjlg" >}}

### Donald Hoffman - What is Consciousness?
{{< youtube "ynTqCFBhRmw" >}}

### Do we see reality as it is? | Donald Hoffman | TED
{{< youtube "oYp5XuGYqqY" >}}

## Related Reading

- [Personal Universes: Yampolskiy's Strangest Answer to the AI Alignment Problem](/ai/yampolskiy-personal-universes/) - the companion piece to this one, where I first set out the fundamental-versus-computational question that Hoffman's work is my attempt to think through.
- [How Likely Is It That We're Living in a Simulation?](/theories/how-likely-are-we-living-in-a-simulation/) - the simulation argument, which looks superficially like Hoffman's interface theory but rests on the opposite assumption: a base-reality substrate and a programmer that Conscious Realism denies.
- [Roman Yampolskiy: The Researcher Who Thinks AI Cannot Be Controlled](/ai/roman-yampolskiy/) - the broader profile of the thinker whose engineered, substrate-based picture of reality is the cleanest foil for Hoffman's idealism.
- [Interstellar: The Physics and Philosophy](/space/interstellar-physics-and-philosophy/) - more on spacetime, perception and where the bedrock of reality might actually sit, from a different angle.
- [The Year 2126: A Hundred-Year Look at Where AI Takes Us](/ai/the-year-2126/) - the long-arc framing for what it would mean if questions like this one ever moved from philosophy into something we could build on.
