---
title: "Threat Modeling for Engineers: Finding the Flaws Before Attackers Do"
date: 2026-05-20T10:30:00+01:00
draft: false
tags: ["security", "architecture"]
description: "Most security work is reactive - a scanner flags an issue, someone patches it. Threat modeling is the opposite: a structured way to find design flaws before you write the code. Here is how it works, a worked example, and why it is the one security skill every engineer should have."
cover:
  image: /assets/images/security/threat-modeling-for-engineers.png
  alt: Threat Modeling for Engineers - Finding the Flaws Before Attackers Do Banner
---

## TL;DR

- A scanner finds bugs in code that already exists. **Threat modeling** finds flaws in a design before the code exists - which is the cheapest possible time to find them
- It is a structured conversation built around four questions: what are we building, what can go wrong, what are we going to do about it, and did we do a good job
- **STRIDE** gives you a vocabulary for "what can go wrong": Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, and Elevation of privilege
- You do not need a tool or a certificate. You need a diagram, the people who understand the system, and an hour
- The highest-value moment to threat model is when the design is still cheap to change - and the most common mistake is treating it as a one-off audit instead of a habit

Most security work, as people experience it day to day, is reactive. A scanner flags a vulnerable dependency. A penetration test produces a report. An alert fires. Someone patches the thing, closes the ticket, and moves on. This is necessary work, but it has a structural weakness: it can only find problems in systems that already exist. By the time a scanner can see a flaw, you have already built it, shipped it, and possibly run it in production for months.

**Threat modeling** is the discipline that runs in the other direction. It is a structured way to ask "how could this be attacked?" while the system is still a diagram on a whiteboard - when changing the answer costs an afternoon instead of a quarter. It is, in my view, the single highest-leverage security skill a general engineer can learn, and it does not require being a security specialist. This post is the introduction, and the anchor for this section.

## Why checklists are not enough

The instinct, when a team decides to "do security", is to reach for a checklist. Use HTTPS. Hash passwords. Patch dependencies. Validate input. These lists are not wrong, and you should do all of them. But a checklist has a built-in blind spot: it can only contain things someone thought of in advance, and it knows nothing about *your* system.

A checklist will tell you to hash passwords. It will not tell you that your password reset flow emails a token that never expires, or that your new internal admin tool trusts a header set by a load balancer that an attacker can also reach, or that your AI agent has a tool that can read arbitrary files and a prompt that an outsider can influence. Those are design flaws. They live in the relationships between components, not inside any single component, and no generic checklist will surface them.

Threat modeling finds exactly that class of problem, because it starts from your actual design rather than from a generic list.

## What threat modeling actually is

Stripped of jargon, threat modeling is a **structured conversation about how a system could be attacked**. The [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/) - written by a group of well-known practitioners - frames it around four questions, and they are worth memorising because they are the whole method:

1. **What are we working on?** Draw the system. Components, data stores, the boundaries data crosses, and who talks to whom.
2. **What can go wrong?** Walk the diagram and enumerate threats. This is where a vocabulary like STRIDE helps.
3. **What are we going to do about it?** For each threat that matters, decide: mitigate it, accept it, or design it away.
4. **Did we do a good job?** Review the model. Was the diagram accurate? Did you miss a trust boundary?

That is it. There is no required tool, no certificate, no heavyweight process. [OWASP's threat modeling guidance](https://owasp.org/www-community/Threat_Modeling) describes the same loop. The value is almost entirely in doing it at all, with the right people in the room, before the design is set in concrete.

## STRIDE: a vocabulary for "what can go wrong"

The hardest of the four questions is the second one. Staring at a diagram and asking "what can go wrong" is too open-ended. You need prompts. The most durable set of prompts is **STRIDE**, a model that originated at Microsoft and is now standard vocabulary. Each letter is a category of threat:

- **Spoofing** - pretending to be someone or something you are not. Defended by authentication.
- **Tampering** - modifying data or code without authorisation. Defended by integrity controls, signing, and validation.
- **Repudiation** - denying you did something, when the system cannot prove otherwise. Defended by logging and audit trails.
- **Information disclosure** - exposing data to someone who should not see it. Defended by encryption and access control.
- **Denial of service** - making the system unavailable. Defended by rate limiting, quotas, and capacity planning.
- **Elevation of privilege** - gaining capabilities you should not have. Defended by authorisation and least privilege.

The technique is mechanical and that is the point: take each element of your diagram - each process, each data store, each flow across a trust boundary - and ask all six STRIDE questions of it. Most will not apply. The ones that do are your threat list. You can read the longer form on [the STRIDE page](https://en.wikipedia.org/wiki/STRIDE_model), but the six words above are enough to start.

## A worked example: a small web service

Abstract descriptions of threat modeling are unconvincing, so here is a concrete one. Imagine a modest service: a single-page web app, talking to an API, which reads and writes a database, and which calls one third-party payment provider.

**Question one - what are we building?** The diagram has four boxes: the browser, the API, the database, the payment provider. The important features are the **trust boundaries** - the lines data crosses where the level of trust changes. There are three: the public internet between browser and API, the network between API and database, and the call out to the payment provider.

**Question two - what can go wrong?** Walking the boundaries with STRIDE:

- *Browser to API.* **Spoofing**: can a request pretend to be a logged-in user? That points straight at how session tokens are issued and validated. **Tampering**: the client controls every byte it sends, so any field the server trusts without re-checking - a price, a user ID, a quantity - is a flaw. **Denial of service**: is there rate limiting, or can one client exhaust the API?
- *API to database.* **Information disclosure**: if the API is compromised, what can it read? Does it connect with a broad account or a scoped one? **Tampering**: is input parameterised, or is SQL injection on the table?
- *API to payment provider.* **Spoofing**: when the provider calls your webhook to confirm a payment, how do you know the call is genuinely from them and not an attacker forging a "payment succeeded" message?

**Question three - what do we do?** Maybe you already issue short-lived signed tokens, so spoofing is handled. Maybe you discover the price is taken from the client request - that is a real flaw, and the fix is to look the price up server-side. Maybe the payment webhook has no signature verification - another real flaw, with a clear fix.

Notice what happened. In one hour, with a diagram and six prompt words, the team found two genuine design flaws that no dependency scanner would ever have reported, because the code is not wrong in isolation - the *design* trusts something it should not. That is the entire return on investment of threat modeling, in miniature.

## When to do it

The most valuable moment to threat model is **when the design is still cheap to change**: at the start of a new service, a significant feature, or a re-architecture. That is when the answer to "what are we building" is still a proposal rather than a deployed reality.

It is also worth doing when a system takes on a new kind of risk. Adding a new trust boundary - a new external integration, a new class of user, a new automated component - is a natural trigger. AI agents are a sharp current example: the moment a system can take actions through tools *and* its instructions can be influenced by untrusted input, you have created a powerful new elevation-of-privilege path that did not exist before, and it deserves a fresh model.

What you should not do is treat threat modeling as a single gate before launch. The design will drift. A model from twelve months ago describes a system that no longer exists.

## Common mistakes

A few failure modes show up again and again:

- **Modelling the diagram instead of the system.** If the diagram is aspirational and the real system differs, you have threat modeled a fiction. Draw what is actually built.
- **Trying to be exhaustive.** You will not enumerate every threat, and chasing completeness produces a huge list nobody acts on. Find the threats that matter and address those.
- **No follow-through.** A threat model that does not produce tracked, owned actions was a pleasant conversation, not a security control.
- **Making it a specialist-only ritual.** The engineers who built the system understand it best. A security expert is a great facilitator, but the model belongs to the team.
- **Doing it once.** Threat modeling is a habit, not an audit. The teams that get value from it model little and often.

## Where this section goes next

Threat modeling gives you the map. The rest of this section fills in the territory: the software supply chain and what the [xz backdoor](https://en.wikipedia.org/wiki/XZ_Utils_backdoor) taught the industry, secrets management, zero trust and identity as the new perimeter, cryptography you can actually use, OAuth and OIDC without the confusion, securing AI agents, the anatomy of a real data breach, and the move toward passkeys. Frameworks like [MITRE ATT&CK](https://attack.mitre.org/) - a catalogue of how real attackers behave - will turn up repeatedly, because the best threat models are informed by how systems are actually attacked, not how we imagine they might be.

If you build software, you are already making security decisions. Threat modeling just makes them deliberate.

## Related Reading

- [Understanding Types of Cyber Attacks: A DevOps Guide](/devops/cyber-attack-types/)
- [The Quiet Standardisation of Agent Protocols - MCP, A2A, ACP Compared](/ai/agent-protocols-mcp-a2a-acp/)
- [AI Agents That Actually Work: Patterns From Real Projects](/ai/ai-agents-that-actually-work/)
- [The eBPF Revolution - What Every Platform Engineer Should Know](/devops/ebpf-revolution/)
