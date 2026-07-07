---
title: "Policy on the AI Exponential: Dario Amodei's Case for Acting While the Window Is Open"
date: 2026-06-11T06:23:00+01:00
draft: false
tags: ["ai", "policy", "anthropic", "safety", "regulation", "economics", "2026"]
description: "Dario Amodei's new essay argues that slow-moving institutions are now the binding constraint on a fast-moving technology, and lays out a five-part policy agenda for the exponential. A summary of the argument, what lands, and where I still have questions."
cover:
  image: /assets/images/ai/policy-on-the-ai-exponential.jpg
  alt: Policy on the AI Exponential Banner
---

Dario Amodei has published a new essay, [*Policy on the AI Exponential*](https://darioamodei.com/post/policy-on-the-ai-exponential), and it reads like the third act of a trilogy. [*Machines of Loving Grace*](https://www.darioamodei.com/essay/machines-of-loving-grace) made the case for what powerful AI could give us. [*The Adolescence of Technology*](https://www.darioamodei.com/essay/the-adolescence-of-technology) catalogued what could go wrong. This one is about the machinery in between - the laws, agencies, and international arrangements that will decide which of those two essays turns out to be the better prediction.

## TL;DR

- Amodei's framing device is Treebeard from *The Lord of the Rings*: institutions that deliberate at the pace of decades are now facing a technology that compounds at the pace of months, and that mismatch is itself the central policy problem
- He proposes action across five domains: frontier model regulation, labour market disruption, scientific acceleration, civil liberties, and geopolitical strategy
- The regulatory centrepiece is mandatory third-party testing for models above a compute threshold, covering cybersecurity, biological weapons, loss of control, and automated AI R&D - with government backstop power to block genuinely unsafe deployments
- On jobs, he accepts that enduring displacement is plausible despite mitigation, and proposes wage insurance, retention incentives, better measurement, and potentially universal basic income as a fallback
- On geopolitics, he argues AI will be the dominant source of national power and backs tightened, allied-coordinated export controls on chips and semiconductor equipment
- The essay's most quotable stance is its rejection of the "PR problem" framing: public concern about AI, he argues, is democratic accountability working as it should

## The Treebeard problem

The essay opens with an analogy that does a lot of work. Treebeard, the ancient tree-shepherd of Middle-earth, takes hours to say anything because anything worth saying takes a long time to say. Our policy institutions are Treebeards by design - deliberate, consensus-seeking, slow to anger and slow to act - and for most of history that has been a feature. Amodei's claim is that the design assumption no longer holds. When a technology doubles in capability on a timescale of months, an institution that responds on a timescale of years is not being prudent. It is being absent.

What makes this more than rhetoric is that Amodei has spent years arguing the opposite side of a related point. His position through the early 2020s was that heavy-handed regulation was premature because nobody could yet say with confidence what the risks were. The essay explicitly marks the shift: the uncertainty that justified caution has, in his view, largely resolved. The risks he and others sketched hypothetically - models meaningfully assisting with biological weapons design, [AI systems writing most of the code that builds the next AI systems](/ai/recursive-self-improvement/), automated cyber operations - now show up in evaluations and deployment data rather than thought experiments. Whether you agree with every item on that list, the structure of the argument is honest: he is saying the evidence changed, so the policy position should change with it.

## Five domains, one agenda

The essay's body works through five areas, and the breadth is the point - Amodei is arguing that AI policy is not one problem but a portfolio.

**Frontier regulation.** Models above a compute threshold would face mandatory third-party testing in four risk areas: cybersecurity, biological weapons, loss of control, and automated R&D. He floats an FAA-style model, including the possibility of "regulatory markets" where government-authorised private bodies do the testing. Crucially, the government would hold the power to block deployment of a model that fails - paired, he says, with safeguards against that power being used politically.

**Labour and macroeconomics.** This is the section where the essay is most candid. Amodei has previously said AI could displace a large share of entry-level white-collar work, and here he accepts that some displacement may be enduring rather than transitional. The proposals are correspondingly unglamorous: build government statistics that can actually measure displacement as it happens, fund wage insurance and retraining, create retention tax incentives, and keep universal basic income on the table - funded by taxes on the companies capturing the gains. The phrase that stuck with me is that these measures are about "buying time" for society to adapt, not about pretending adaptation is automatic.

**Scientific acceleration.** The flip side of regulation is making sure the upside arrives. He wants regulatory agencies to develop standards for AI-driven drug development *before* the applications flood in, so approval pipelines do not become the bottleneck on the century's biggest health gains. This is the part of the agenda most directly descended from *Machines of Loving Grace*, and the part least likely to make headlines.

**Civil liberties.** Amodei repeats his warning that AI could become the "ultimate tool of autocracy" and proposes concrete guardrails: accountability rules for autonomous weapons, a ban on domestic deployment of them, closing loopholes that let governments buy in bulk the data they could not legally collect, and a right for citizens to use AI in legal disputes with the state. This section deserves more attention than it will get - it is the rare case of an AI lab CEO proposing limits on state power rather than just corporate behaviour.

**Geopolitics.** The essay frames AI as more consequential for national power than nuclear weapons, credits export controls on chips and semiconductor manufacturing equipment as a major contributor to the current American lead, and argues for a coalition of democracies that shares compute internally while denying it to adversaries - a coalition that grows by being attractive to join rather than by coercion.

## What lands

The strongest thing about the essay is that it treats the benefits and the risks as one policy problem rather than two competing camps. Most public AI argument sorts people into accelerationists and doomers, and both camps produce policy proposals that assume the other side's concerns are fake. Amodei's portfolio approach - regulate the frontier *and* pre-clear the drug pipeline, control the chips *and* protect civil liberties - is what it looks like when you take both columns of the ledger seriously. I made a related argument from the engineering side in [AI safety from first principles](/ai/ai-safety-first-principles/): the conversation only becomes actionable when you stop treating "AI safety" as one undifferentiated thing.

The civil liberties section also deserves credit for cutting against interest. A frontier lab CEO calling for limits on government bulk data collection and domestic autonomous weapons is not saying what the procurement environment wants to hear.

And the closing move is genuinely well judged. Rejecting the idea that public concern about AI is a "PR problem" to be managed - insisting instead that it is democratic accountability functioning correctly - is the right posture for an industry that will spend the next decade asking for public trust.

## Where I still have questions

I should say upfront that I am a data engineer reading policy essays as an interested outsider, not a policy person, so take these as questions rather than verdicts.

The FAA analogy is the part I keep turning over. Aviation regulation works partly because aircraft change slowly and failure modes are well characterised - the regulator's knowledge can keep up with the regulated object. A frontier-model regulator faces an object that changes substantially every few months, which is the very Treebeard problem the essay opens with. The "regulatory markets" idea is presumably the answer - private testers can move faster than agencies - but it imports its own incentive problems, since testing bodies paid within the industry they test have a long history in other sectors of drifting toward their customers. I would have liked more on how that drift gets prevented.

The coalition strategy has a similar tension. Export controls have clearly helped maintain the compute gap, and the essay is right that they only work if allies move together. But a strategy whose endgame is permanent denial assumes the gap stays decisive, and the [history of compute efficiency](/ai/token-economics-why-costs-arent-going-down/) suggests capability has a way of needing less hardware than the last generation did. If the moat narrows, the coalition needs a plan B that is not just a taller fence - and the essay gestures at attraction and benefit-sharing, but the hard version of that question is left for another day.

None of this undermines the central claim. The mismatch between institutional speed and technological speed is real, the window for acting deliberately rather than reactively is finite, and the essay's proposals are concrete enough to argue with - which is more than can be said for most writing in this genre. On the labour question in particular, where Anthropic has [published numbers from inside its own development loop](https://www.anthropic.com/institute/recursive-self-improvement) showing how fast the change is arriving, the case for building the measurement and cushioning infrastructure now seems hard to dispute.

## The window

The essay ends on an unusual note for the genre: optimism about politics. Amodei reports that policymakers across the spectrum are more open to forward-looking AI policy than at any point he can remember, and argues that this openness is a window that will not stay open - either because a crisis forces reactive lawmaking or because positions harden into partisan trenches. Whichever of those you find more likely, the conclusion is the same: the cheapest time to build the machinery is before it is needed.

Treebeard, for what it is worth, did eventually act - and when the Ents finally marched, they were decisive. The essay's quiet hope is that our institutions have the same second gear. I hope he is right.

## Related Reading

- [Dario Amodei: The Anthropic CEO Betting on Safety as Strategy](/ai/dario-amodei-anthropic-ceo/) - a profile of the essay's author and how the safety message became Anthropic's commercial position
- [Recursive Self-Improvement: The Loop Closes](/ai/recursive-self-improvement/) - the automated R&D risk the essay wants tested, and the data Anthropic has published about its own loop
- [AI Safety From First Principles](/ai/ai-safety-first-principles/) - my attempt to separate the four layers of "AI safety", from product safety up to the civilisational layer this essay operates at
- [AI Law Trends 2026](/ai/ai-law-trends-2026/) - where the actual legislation stands across jurisdictions
- [Four Futures for the Machine-Speed Economy](/ai/four-futures-machine-speed-economy/) - the longer-arc scenarios behind the labour-market section
