---
title: "Agent-First Architecture: The Engineer as System Curator"
date: 2026-04-23T21:01:00+01:00
draft: false
tags: ["ai", "agent", "architecture", "platform-engineering", "data-engineering", "product-management", "leadership"]
description: "Some thoughts on where agent-first architecture might take us, and what engineering could look like if the job shifts from building systems line by line to curating, governing, and evolving fleets of agents."
cover:
  image: assets/images/ai/agent-first-architecture.jpg
  alt: Agent-First Architecture Banner
---

This is a "thinking out loud" post, not a report from the front lines. I have no evidence any of this is happening at scale, and it is not how my current day job looks. These are just ideas I keep turning over, and I wanted to write them down to see if they hold together.

The question I keep coming back to is simple. If AI agents continue to improve at the rate they seem to be, what does engineering work look like five or ten years from now? Not tomorrow. Not next quarter. Further out, where the shape of the job might actually be different.

Here is where my thinking currently lands.

## The Idea: Agent-First Architecture

Most systems today have AI features bolted on. A chat box here, a copilot there, a model called from a handler. That feels like an intermediate step to me, not an end state. The patterns that separate agents that actually survive contact with production from the ones that don't are something I have written about more concretely in ["AI agents that actually work"](/ai/ai-agents-that-actually-work/).

The thing I find myself imagining is something different. A system where the primary unit of work is an agent with intent, tools, memory, and a feedback loop, and where the human's role is to define, constrain, observe, and evolve it. I have started calling this agent-first architecture in my head, though I am sure smarter people have better names for it.

I do not know if this is where we are actually heading. It might be a dead end. It might be partially true. But if I squint at the trajectory of tools like [Claude](https://www.anthropic.com/claude), [Cursor](https://cursor.com/), and the broader agent ecosystem, this is the direction it feels like it could go.

## What It Might Look Like

Imagine a data pipeline, far enough out that today's tools look quaint. Instead of a human-authored DAG and an on-call engineer, you might have an objective ("keep this dataset fresh, correct, and documented"), a set of tools the agent can use ([dbt](https://www.getdbt.com/), a warehouse, a lineage graph, a ticketing system), guardrails (budgets, SLAs, rules about sensitive columns), and a supervisor that reviews its decisions. Sometimes that supervisor is a human. Sometimes it is another agent.

The DAG would probably still exist. The agent would just maintain it instead of a person doing it by hand.

I could see a similar pattern in infrastructure. Platform teams might eventually treat [Kubernetes](https://kubernetes.io/), [Terraform](https://www.terraform.io/), and their internal developer platforms as environments that agents operate within, rather than tools humans drive directly. The engineer would write the policy. An agent would propose the change. Another agent would review it. A human would approve the ones that matter.

I want to be clear: this is a guess about where things might go. It is not a description of how anything works today, certainly not anywhere I have worked.

## A Possible Shift: Builder to Curator

If something like the above does come to pass, I think the interesting question is what the human role looks like. My best guess is that it moves further away from "building and maintaining" and further toward "curating, governing, and evolving".

Curation is a real discipline. Museums curate. Editors curate. Good product managers curate. It is not passive. It means deciding what belongs, what does not, what the through-line is, and what the thing is trying to say.

If that framing is right, an engineer as system curator might end up responsible for:

- **Logic** - what the system is supposed to do, and under what assumptions.
- **Reliability** - how it behaves when those assumptions break.
- **Ethics** - who it affects, how, and what it must never do.
- **Outcomes** - whether it actually moves the business or the user somewhere better.

I am not claiming this is how engineers work today. I am wondering whether this is how the job ends up being defined once the execution layer is mostly automated. It might not. The craft of writing code might remain central for reasons we are currently underestimating. But this is the version of the future I find myself sketching when I daydream about it.

## What I Think Might Get Automated, and What Might Not

This is the part I am most uncertain about, so take it as a guess rather than a forecast.

Things I could imagine being automated well, eventually:

- Glue code between APIs, services, and schemas.
- Routine pipeline maintenance - schema drift, column renames, documentation, test scaffolding.
- First-pass incident triage - log gathering, correlation, likely-cause hypotheses.
- Migration work - framework upgrades, dependency bumps, boilerplate refactors.
- Meeting notes, status updates, ticket hygiene, reporting.
- Draft PRs for well-specified changes.

Things I suspect will resist automation for a long time, possibly forever:

- Deciding what the system should be for.
- Negotiating trade-offs between teams with different incentives.
- Holding a consistent architectural intent across months of change.
- Knowing which constraint is load-bearing and which is historical accident.
- Taking responsibility when an agent fleet does something wrong.

I could be completely wrong about both lists. Some of the things in the second list might be automatable with better models and better context. Some of the things in the first list might turn out to be much harder than they look. These are hunches, not predictions.

## Roles That Might Converge

My background is in data engineering and infrastructure/platform engineering, so I am looking at this from that angle. But when I try to project agent-first thinking across the full software development lifecycle - build, test, ship, run, support - I find myself wondering whether the space between a lot of adjacent roles ends up narrowing.

If I try to sketch it forward, here is how I imagine it *might* play out. I want to stress the word "might". None of this is a description of how things work today.

**Software / application engineering** might move away from writing feature code line by line and toward specifying intent, defining contracts, and reviewing agent-generated implementations. Code literacy would still matter enormously - possibly more than ever, because reviewing wrong-looking-right code is harder than writing it fresh.

**Infrastructure / platform engineering** has always been about scaling things and keeping them up. It might become more about designing substrates that agents can operate on safely - tight blast radius, clear rollback paths, dependable observability, enforced resource budgets. The deliverable could end up being less "a system" and more "a governed environment".

**Data engineering** might move further away from moving and shaping data by hand, and further toward declaring what the data should mean, what quality bar it must meet, and what lineage and [observability](https://www.montecarlodata.com/) an agent fleet needs to maintain. Pipelines would still exist. They would just be written and maintained differently.

**DevOps / release engineering** might fold further into platform engineering as agents handle routine pipeline work, deploys, and environment management. The interesting human work probably shifts to release strategy, progressive delivery, and the policy layer around it.

**QA / test engineering** might shift from authoring tests to designing evaluation frameworks - how do you actually know an agent-written change is correct, safe, and non-regressive? "How do we test the things the agents build" feels like a growing problem, not a shrinking one.

**Site Reliability Engineering / operations** might see agents absorb first-pass triage, runbook execution, and routine remediation. I suspect humans end up owning the hard incidents, the post-mortems, and the slow work of making the system less fragile over time. The on-call shape probably changes more than the on-call need.

**Security / AppSec** might actually *grow* rather than shrink. Agent fleets with tool access are a different threat model, and someone has to think hard about blast radius, policy, secrets, and adversarial misuse. This feels like one of the roles most underweighted in current conversations about automation.

**Technical project management** might become less about coordinating humans and more about coordinating a mix of humans and agents against a shared plan, watching for drift, and deciding when an agent's confident-looking output actually needs a person in the loop. I suspect the classic PM skills - clarity, sequencing, risk framing - would matter more, not less, because agents amplify whatever plan you give them, including a bad one.

**Product management** might shift further from "deciding what to build" to "deciding what the system should optimise for, for whom, over what horizon, at what acceptable cost". If delivery genuinely gets cheap, the bottleneck probably stops being delivery and starts being judgment about which features deserve to exist.

**Support / customer engineering** might see the biggest visible shift, because tier 1 and tier 2 work is already an obvious fit for agents. The human role probably moves toward escalations, edge cases, and being the feedback channel that tells product and engineering what the fleet is actually getting wrong in the wild.

Whether any of these roles actually converge into a single "multi-disciplinary systems thinker" is an open question, and probably not a desirable outcome even if it were possible - the specialisms exist for good reasons. But the shape of the work in each of them feels like it could push in a similar direction: less manual execution, more intent, policy, evaluation, and accountability.

## Managing a Fleet of Agents

The mental model I find myself reaching for, when I try to picture this, is fleet management.

You do not write the logic for every truck in a logistics company. You design the routes, set the policies, audit the drivers, watch the dashboards, and investigate anomalies. The trucks do the driving.

If engineering ends up in a similar place, the job might look something like:

- **Define intent.** What is this agent for? What problem does it own? What does "done" look like?
- **Set constraints.** Budget, latency, data access, tools it may call, actions that always require human approval, things it must never touch.
- **Design feedback loops.** How does the agent learn it is wrong? What metrics matter? Where does a human get pulled in, and under what thresholds?
- **Curate the fleet.** Which agents exist, which should be retired, which should be merged, which should be split. Editorial work.
- **Own the outcomes.** When the fleet causes an incident, the fleet did not make that call. A human did, somewhere upstream.

I find the accountability question especially interesting, because it does not go away. If anything, I suspect it concentrates. One person supervising ten agents might end up owning more than a team of ten engineers does today. Whether that is healthy or sustainable is another question I do not have an answer to.

## What "Higher-Order Work" Might Actually Mean

"Agents free you up for higher-order work" is the kind of sentence that shows up on vendor slides and makes me roll my eyes. But if I try to steelman it, the work I imagine it could mean is something like:

- Designing an architecture that can absorb a 10x traffic change, a new regulatory regime, and a product pivot without a rewrite.
- Writing the contracts, SLOs, and guardrails that would let an agent fleet run without constant human babysitting.
- Choosing what *not* to automate, because the feedback loop is too slow, the stakes are too high, or the judgement is genuinely human.
- Translating a fuzzy business outcome into a precise objective that an agent could optimise against, and noticing when that objective stops matching reality.
- Sitting with a stakeholder for an hour to understand what they actually need, which I suspect will remain one of the most leveraged activities in software.

None of this is a description of my current day. It is a description of what I would *hope* the job becomes, if the optimistic version of this trajectory plays out.

## Skills, Mindset, and Habits That Might Matter

I am wary of writing a "skills of the future" list, because those age badly. But if I had to guess, here is what I would bet on. Take these as working hypotheses, not advice.

**Skills:**

- Systems thinking across infrastructure, data, delivery, and product - not deep expertise in all four, but enough fluency to reason across them.
- Specification as a craft. If agents really do become the execution layer, the ability to write unambiguous intent probably becomes more valuable.
- Observability and evaluation. Knowing whether a fleet is doing the right thing might matter more than knowing how much code it wrote.
- Security and policy literacy. Autonomous systems with tool access feel like a different threat model, and I suspect we are still early in understanding it.

**Mindset:**

- Outcome orientation over task orientation.
- Comfort with leverage - being willing to spend hours on a decision that saves weeks later.
- Humility about agents. They are fast, confident, and often wrong in ways that look right.
- Accountability without ego. Fix the system, not the blame.

**Habits:**

- Write the intent down.
- Review agent work the way a senior engineer reviews a junior's - carefully, with an eye for subtle wrongness.
- Keep a running log of what worked, what broke, and what you learned.
- Talk to the humans. I suspect this becomes more important, not less.

I am aware this list could look silly in five years. That is part of why I am writing the post: to pin my thinking down so I can come back and see how much of it was wrong.

## A Note on Fear

I have deliberately not written about whether jobs are going away. I do not find that framing useful, and I do not have any special insight into it.

What I *hope* happens - and it is a hope, not a prediction - is that the repetitive, low-leverage work people never really enjoyed gets absorbed, and the more interesting work around design, intent, judgement, ethics, and outcomes becomes more of the job. That would be the optimistic version of this story.

It might not play out that way. The cynical version is just as plausible. But the optimistic version is the one I want to think towards, because it is the one worth building for.

If any of this resonates, I have been circling similar ideas from different angles in recent posts: the [architect vs builder split](/ai/architect-vs-builder/), the [automation paradox](/ai/automation-paradox/), and [platform engineering in 2026](/devops/platform-engineering-2026/). None of them are predictions. They are all me trying to think out loud about where this might be going.

I would rather be usefully wrong in public than quietly uncertain.
