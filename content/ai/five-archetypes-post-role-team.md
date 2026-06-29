---
title: "Five Archetypes for a Post-Role Team"
date: 2026-06-29T20:30:00+01:00
draft: false
tags: ["ai", "role", "career", "team", "engineering"]
description: "Boris Cherny, who created Claude Code, sketched five archetypes he sees on his team as engineering, product, design, and data science melt into one role. Here is what that framing gets right, and where I think it still leaves us guessing."
cover:
  image: /assets/images/ai/five-archetypes-post-role-team.jpg
  alt: Five archetypes for a post-role team
---

## TL;DR

- [Boris Cherny](https://x.com/bcherny/status/2071379474277613732), who built [Claude Code](https://code.claude.com/docs/en/overview) at Anthropic, posted a short framing: as engineering, product, design, and data science melt into one role, he sees five archetypes on his team
- The five are **Prototyper**, **Builder**, **Sweeper**, **Grower**, and **Maintainer** - and crucially, none of them map cleanly to a job title
- The interesting claim is not the list, it is the decoupling: the archetype is a description of what energy you bring to a system, not what your contract says you do
- I think the framing is genuinely useful as a self-diagnostic, and quietly radical for how teams get staffed and rewarded
- Where it leaves me unsure: it describes a steady-state team that already exists, and says less about how you grow people into these shapes, or what happens to the people who do not fit any of them

A short post on X has been rattling around my head for a few days. [Boris Cherny](https://x.com/bcherny/status/2071379474277613732), who built Claude Code at [Anthropic](https://www.anthropic.com/), was reflecting on what happens to roles when the old functional boundaries stop meaning much. His observation: when he looks at the Claude Code team, he does not really see engineers, designers, PMs, and data scientists. He sees five archetypes that cut across all of them.

I want to take the idea seriously, because I think it is pointing at something real, and then push on the parts I am less sure about. As always, this is one hobbyist's reading of someone else's framework, not a pronouncement - I am thinking out loud, and happy to be talked out of any of it.

## The Five Archetypes

Here is the list, in my own words rather than as a transcript.

1. **The Prototyper.** Generates a high volume of fresh ideas, knowing most will be thrown away. Their real output is optionality, not product. You measure them on the quality of the bets they surface, not the hit rate.

2. **The Builder.** Takes a half-formed sketch and hardens it into something that can actually run in production - app or infrastructure. They are the bridge between "this could work" and "this works".

3. **The Sweeper.** The cleanup specialist. Trims the interface, untangles the code, retires features that have stopped paying their way, and wins back performance. The person whose job is partly to *unship*.

4. **The Grower.** Inherits a working product and pushes it, iteration by iteration, toward a better fit with its market. Lives in the loop of measure, adjust, measure again.

5. **The Maintainer.** Stewards a system that has already matured, holding the line on security, reliability, speed, and efficiency as load climbs. The least glamorous and most load-bearing of the five.

The detail that makes this more than a personality quiz is Cherny's footnote: these roles are not tied to job function. Across the org, some designers are Prototypers and some are Sweepers. Some engineers are Growers. Plenty of people span two of them, occasionally three. The archetype describes the shape of the contribution, not the line on the org chart.

## Why the Decoupling Is the Real Idea

The list itself is not new. You could map it onto older language without much effort - the Sweeper is a cousin of the refactoring-minded senior engineer, the Grower is a growth PM in disguise, the Maintainer is the SRE who never sleeps. If that were all there was, this would be a repackaging exercise.

The part I find genuinely interesting is the claim that the function is dissolving and the archetype is what survives.

For most of the history of software teams, the function *was* the archetype. If you were hired as a designer, you did design; the title carried a fixed bundle of responsibilities, tools, and rituals. What [AI-assisted development](/ai/ai-augmented-design-workflow/) has done is unbundle that. When a single person armed with a capable agent can prototype an interface, wire up the backend, write the migration, and ship it behind a flag, the question "are you an engineer or a designer?" stops doing useful work. The more useful question becomes "what do you do to a system when you arrive at it?"

That is the shift. The new variable is not your discipline. It is your *relationship to the lifecycle of a thing*. Do you bring it into existence, harden it, prune it, grow it, or keep it alive? I have written before about [the architect versus the builder](/ai/architect-vs-builder/) as a two-way split; Cherny's five is the higher-resolution version of the same instinct, and I think the higher resolution earns its keep.

## What I Think It Gets Right

A few things ring true from teams I have watched up close, where the functional lines were always blurrier than the org chart admitted.

**It explains friction that titles cannot.** I have watched a brilliant Prototyper get quietly miserable being asked to maintain the thing they invented, and an excellent Maintainer get visibly stressed being asked to brainstorm in a blank-page meeting. Neither was bad at their job. They were being asked to operate in the wrong archetype. The framing gives you language for a mismatch that "they are a senior engineer, they should be able to do this" actively hides.

**It legitimises the Sweeper.** Most reward systems are catastrophically bad at valuing the person who deletes things. Shipping a feature is legible; *unshipping* one, simplifying a data model, or killing a pipeline nobody uses is not, even though it is often higher-leverage. Naming the Sweeper as a first-class archetype is a small act of organisational honesty. The best [data engineering](/data-engineering/) I have seen has been subtractive at least as often as additive.

**It is a good self-diagnostic.** Read the five and you will usually feel a tug toward one or two. That tug is worth paying attention to, because the [most durable kind of expertise after AI](/ai/expertise-after-ai/) is increasingly about knowing what energy you bring to a system rather than which tool you have memorised.

## Where I Get Less Sure

I do not want to over-claim on someone else's behalf, so here are the seams I keep catching on.

**It describes a steady state, not a path.** The five archetypes read like a snapshot of a team that already works - a strong one, staffed by senior people at a frontier lab. It says much less about how you *grow* someone into a Builder, or how a junior person finds out which archetype they are before they have enough scar tissue to know. A model of a finished team is not yet a model of how teams are made.

**Some archetypes have a gravity problem.** Prototyping is intoxicating; maintenance is not. If the culture quietly rewards the Prototyper and the Builder over the Sweeper and the Maintainer - and most cultures do, whatever they say - then the archetypes are not really equal, and people will optimise toward the glamorous end. The framing is descriptively even-handed. Real incentive systems usually are not.

**It is unclear what happens to the people who do not fit.** Five clean buckets is a tidy story. Plenty of strong contributors are connectors, coordinators, mentors, or domain specialists whose value is hard to express as a lifecycle stage. I would not want "which of the five are you?" to become a new way of making good people feel illegible, the same way the old titles did.

**The melt is not finished, and the destination is unknown.** "Engineering, product, design, and data science melt into a new kind of role" is the premise, not a proven outcome. It is happening fastest at places like Anthropic, where everyone is unusually strong and the tooling is unusually good. Whether it generalises to a 200-person enterprise data org with compliance constraints and legacy systems is a genuinely open question. I lean toward thinking the *direction* is right and the *speed* is wildly uneven - but that is a hunch, and the kind of thing I expect to revise.

## What This Could Mean for Specific Roles

The frontier-lab version of the melt is the dramatic one. But most of us work in orgs where the titles are not going to vanish next quarter - data engineering, data science, product, and delivery are still real lines on a budget. So the more useful exercise, for me, is to ask what each of those roles *bends toward* if Cherny is even half right. Not "which title gets deleted", but "which archetypes does this role start to live in once the hand-cranked parts are automated away?"

These are guesses, and deliberately so. I am a hobbyist mapping someone else's framework onto roles I have worked alongside, not predicting anyone's org chart.

**Data engineering.** This is the role I think shifts hardest toward **Sweeper** and **Maintainer**. When an agent can scaffold a pipeline, write the transformation, and draft the tests, the scarce skill stops being "can you build the DAG" and becomes "should this pipeline exist, and what do we delete to keep the platform coherent?" The job gets more subtractive - pruning redundant models, killing tables nobody queries, defending data contracts and lineage as the agents generate more surface area faster than humans used to. The best data engineers become curators of a system that is now partly written by machines, which is the shift toward [the engineer as system curator](/ai/agent-first-architecture-engineer-as-curator/) I keep coming back to. There is still a **Builder** core - someone has to own the hard infrastructure decisions - but the centre of gravity moves toward keeping a fast-growing system simple, governed, and trustworthy.

**Infrastructure engineering.** This one bends toward **Maintainer** and **Builder**, and the split between them sharpens. Once an agent can write the Terraform, wire up the networking, and draft the provisioning scripts, "can you stand up the cluster" stops being the question and "what should this system look like, and what failure modes are we signing up for?" takes its place. The Builder core survives and arguably grows - someone still has to own the genuinely hard, irreversible architecture decisions, the ones where a wrong call costs you months. But the day-to-day centre of gravity shifts toward keeping a sprawling, fast-growing estate coherent and reliable as the agents generate infrastructure faster than humans used to review it. The best infrastructure engineers become the people who decide what *not* to build - the same curator instinct, applied to the substrate everything else runs on.

**Site reliability engineering.** The **Maintainer** archetype was practically named after the SRE - owning a mature system and keeping it secure, reliable, fast, and efficient as it scales is the job description almost word for word. What I think changes is that the role leans harder into **Sweeper** than people expect. A lot of reliability work is subtractive: deleting noisy alerts, removing toil, simplifying a runbook, killing the bespoke automation that has quietly become its own source of incidents. As agents take over more of the rote execution - triaging the page, running the runbook, drafting the postmortem - the human work concentrates in judgement about reliability tradeoffs: where to spend the error budget, what is worth the on-call cost, what complexity to refuse. The SRE who just executes runbooks is the most exposed; the one who curates *which* reliability work is actually worth doing is the one the agents make more valuable, not less.

**Platform engineering.** I find this the most interesting of the three, because a platform team is really an internal product team, so it lives in **Builder** and **Grower** at once. The Builder half ships the paved road - the golden paths, the self-service tooling, the guardrails that let everyone else move fast. The Grower half is the part most platform teams under-invest in: a paved road nobody adopts is just shelfware, so the measure-adjust-measure loop of finding out what developers actually use and iterating toward real internal product-market fit is the difference between a platform and a pile of abandoned tools. And there is a heavy **Sweeper** obligation hiding underneath, because a platform that only ever accretes features becomes a swamp - the discipline to deprecate, consolidate, and delete is what keeps the paved road paved. With agents lowering the cost of building tooling, the scarce skill moves decisively toward [taste about what is worth building and keeping](/ai/taste-is-the-new-scarcity/), because the volume of buildable platform features has exploded and most of them are traps.

**Data science.** I think this one splits cleanly into two archetypes that used to live in one uncomfortable role. The exploratory half - hypotheses, feature ideas, "what if we modelled it this way" - is pure **Prototyper**, and agents make it dramatically cheaper to churn through bad ideas to find good ones. The other half, taking a model that works and grinding it toward real impact, is the **Grower**: the measure-adjust-measure loop, the work of moving a metric rather than producing a notebook. The classic failure mode of data science - brilliant analysis that never changes a decision - is really a team that staffed Prototypers and forgot it needed Growers. Naming the two archetypes makes that gap visible. The piece that gets automated fastest is the plumbing in the middle, which pushes the role toward judgement at both ends.

**Product owner.** If anyone is already living the melt, it is a good product owner, who has always been part Prototyper (framing the bet) and part Grower (iterating toward fit). What changes is that the gap between "idea" and "something you can put in front of a user" collapses - a PO with a capable agent can prototype the thing rather than write a ticket asking someone else to. That is a real expansion of the role toward **Builder**, and it raises the bar uncomfortably: when the cost of building the wrong thing has dropped and the volume of buildable things has exploded, judgement about what deserves to exist becomes the whole game. The PO who just curates a backlog is the most exposed; the one who can prototype and grow is suddenly far more powerful.

**Technical project manager.** This is the role I find hardest to place, and I think that is informative. Cherny's five are all archetypes of *making and tending a system* - none of them is "coordinate the humans". A lot of classic TPM work is coordination overhead that exists precisely because functions were siloed and someone had to be the connective tissue between them. As the functions melt and small agent-augmented teams own more of the lifecycle end to end, some of that coordination simply evaporates. The part that survives, I think, bends toward **Maintainer** and **Sweeper** at the level of *process* rather than code: keeping the delivery system reliable, removing ceremony that is not earning its keep, owning the operational health of how the team ships. The TPM who reinvents themselves as a steward of the team's systems and guardrails has a clear seat. The one whose value was purely status-chasing across silos has the least obvious one - which is uncomfortable to write, and I would genuinely like to be wrong about it.

The thread running through all of them: the archetypes that gain are the ones requiring *judgement about a system* - what to build, what to keep, what to kill, what to grow. The parts that shrink are the hand-cranked production steps in the middle that agents now do well. None of these roles disappears, but each one hollows out in the centre and thickens at the edges of taste and stewardship.

## How I Would Actually Use It

Despite the caveats, I think this is one of the more useful things I have read on team shape this year, precisely because it is small and unpretentious. Here is where I would put it to work.

- **As a self-check.** Which one or two pull at you? Are you currently being paid to operate in that mode, or fighting against it? A lot of career unhappiness is an archetype mismatch wearing a title-shaped mask.
- **As a staffing lens.** Before assigning a project, ask what *stage* it is in. A zero-to-one bet wants a Prototyper and a Builder. A creaking, widely-used system wants a Maintainer and a Sweeper. Putting the wrong archetype on the wrong stage is a common, invisible way to waste good people.
- **As a reward audit.** Look at who got promoted and recognised last cycle. If every name is a Prototyper or a Builder, your system is blind to half the value being created. That is fixable, but only once you can see it.

This connects to a bigger theme I keep circling back to: as the [engineer's job shifts toward curating and governing systems](/ai/agent-first-architecture-engineer-as-curator/) rather than hand-writing every line, the thing that distinguishes people is less their function and more their disposition toward the systems they touch. Cherny's five archetypes are a clean, early attempt to name those dispositions. I do not think it is the final taxonomy. But "what energy do you bring to a system?" is a much better question than "what is your job title?", and the gap between those two questions is roughly the gap between how teams used to work and how they are starting to.

## Related Reading

- [The Architect vs The Builder: Redefining Engineering Roles in 2026](/ai/architect-vs-builder/)
- [Agent-First Architecture: The Engineer as System Curator](/ai/agent-first-architecture-engineer-as-curator/)
- [What Does 'Expertise' Mean When AI Can Pass Any Exam?](/ai/expertise-after-ai/)
- [Taste Is the New Scarcity](/ai/taste-is-the-new-scarcity/)
- [The Meaning of Work in an Age of Abundance](/ai/meaning-of-work-age-of-abundance/)
