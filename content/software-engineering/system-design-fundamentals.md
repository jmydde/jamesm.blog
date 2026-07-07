---
title: "System Design Fundamentals: Making Trade-offs You Won't Regret"
date: 2026-05-19T12:00:00+01:00
draft: false
tags: ["software-engineering", "architecture"]
description: "System design is not about knowing the right answer. It is about understanding the trade-offs well enough to choose deliberately. Here are the core axes every design decision moves along, a worked example, and why designing for scale you do not have is the most common self-inflicted wound in software."
cover:
  image: /assets/images/software-engineering/system-design-fundamentals.png
  alt: System Design Fundamentals - Making Trade-offs You Won't Regret Banner
---

## TL;DR

- System design has no right answers, only **trade-offs chosen deliberately or chosen by accident**. The skill is making the choice consciously
- Most decisions move along a few core axes: consistency against availability, latency against throughput, simplicity against flexibility, and build against buy
- A good design states its assumptions - expected load, acceptable latency, failure tolerance - because a design is only "good" relative to assumptions
- The most common self-inflicted wound is **designing for scale you do not have**. Complexity added for an imagined future is paid for every day until that future arrives, if it ever does
- Write designs down. A short document that names the options, the choice, and the reason is worth more than any diagram

There is a particular kind of interview question, and a particular kind of blog post, that treats system design as a body of correct answers - as if there were a known-good way to "design a URL shortener" or "design a news feed" and the job is to recall it. This framing is actively harmful, because it teaches people that system design is about memorising solutions.

It is not. System design is about **trade-offs**. Every meaningful decision gives you something and costs you something else, and there is no option that is purely better. A senior engineer is not someone who knows the right architecture. They are someone who can see the trade-offs clearly, has a feel for which ones matter for the problem in front of them, and chooses on purpose rather than by habit. This post lays out the fundamentals, and it anchors a section about the craft of building software.

## System design is trade-off management

Here is the reframe that makes everything else easier: **a design decision you did not know you were making is still a decision**. If you reach for a microservices architecture because that is what the last team used, you have chosen operational complexity over simplicity - you just did not choose it deliberately. If you put everything in one database because it was fastest to build, you have chosen simplicity now over flexibility later - again, possibly without noticing.

The goal is not to avoid trade-offs. That is impossible. The goal is to make them **visible and intentional**. When you can name what you are giving up, three good things happen: you can check whether the trade is right for this problem, you can write it down so future maintainers understand it, and you can revisit it honestly when the assumptions change. A design is not good or bad in the abstract. It is good or bad relative to a set of assumptions, and the worst designs are the ones whose assumptions were never stated.

## The core axes

Most system design decisions, underneath the specifics, move along a small number of axes. Knowing them gives you a checklist for "what am I actually trading here".

**Consistency against availability.** When data is replicated across machines and the network between them fails - and networks always eventually fail - you must choose. Do you refuse to answer rather than risk returning stale data, or do you stay available and accept that two replicas might disagree for a while? This is the heart of the [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem). A bank balance and a "like" count want opposite answers. There is no universally correct choice, only a choice that fits the data.

**Latency against throughput.** Latency is how long one request takes. Throughput is how many requests you handle per unit time. They pull against each other constantly. Batching work improves throughput and worsens latency. Adding a queue smooths load and absorbs spikes, at the cost of end-to-end delay. A caching layer cuts latency and adds a consistency problem. You cannot maximise both; you decide which one the product actually needs.

**Simplicity against flexibility.** A flexible system - one with plugin points, configuration, abstraction layers, generality - can absorb future change without rework. It also costs more to build, more to understand, and more to debug, every single day, including all the days the anticipated change never arrives. Simplicity is not a lack of sophistication. It is a deliberate refusal to pay for flexibility you do not yet need.

**Build against buy.** Almost nothing you need is genuinely novel. Authentication, queues, search, observability, feature flags - mature solutions exist. Building your own gives you control and a perfect fit, and hands you the maintenance, the security patching, and the operational burden forever. Buying or adopting gives you a fast start and someone else's roadmap, constraints, and pricing. The right answer depends entirely on whether the thing is core to your product or merely necessary for it.

## A worked example

Consider a feature: a notification system that tells users when something relevant happens. Watch how the axes drive the design.

Start with **build against buy**. Notifications are necessary but rarely a product differentiator, so a managed delivery service is likely the right call. That decision alone removes a large amount of work and a large amount of future maintenance.

Now **latency against throughput**. Do notifications need to arrive instantly, or is a few seconds fine? For almost every product, a few seconds is fine - which means you can put a queue between the event and the delivery. That queue buys you throughput, smooths spikes, and gives you a natural retry point. You traded a little latency, which the product did not need, for resilience, which it did.

Now **consistency against availability**. If the notification service is briefly down, what should happen - block the user action that triggered the notification, or let the action succeed and deliver the notification late? Almost always the action should succeed. The notification is not worth coupling the availability of a core flow to a secondary system.

And **simplicity against flexibility**. It is tempting to build a general notification platform - every channel, every preference, a rules engine. If today's requirement is "email when an order ships", build that. The general platform is flexibility you would pay for now and might never use.

None of these choices is clever. Each is just an axis, named, and a decision made on purpose. That is the method.

## Designing for the scale you have

If there is one failure mode worth burning into memory, it is this: **designing for scale you do not have**. It is the most common self-inflicted wound in software, and it is committed almost entirely by capable, well-meaning engineers who are trying to be responsible.

The reasoning feels prudent. "We should design for scale so we do not have to rewrite later." But complexity added for an imagined future is not free until that future arrives. You pay for it every day in between - in onboarding time, in debugging difficulty, in slower changes, in more things that can break. A system sharded across many services and databases to handle millions of users, while it actually has thousands, is not prepared. It is just expensive and slow to change, which makes it *harder* to reach those millions of users.

The honest approach is to design for roughly the next order of magnitude, keep the design simple enough to change, and trust that you will learn far more about your real bottlenecks by running the simple version than by speculating. The systems that scale well are usually not the ones that were designed for scale up front. They are the ones that stayed simple enough to be reshaped when the real load showed up. Premature scaling and premature optimisation are the same mistake wearing different clothes, and [Martin Fowler's writing](https://martinfowler.com/) has been making this argument patiently for two decades.

## Write the design down

A design that lives only in someone's head, or only in a diagram, is not really a design - it is a memory. The single highest-leverage habit in system design is writing a short document before significant work begins.

It does not need to be long. It needs to state the **assumptions** (expected load, acceptable latency, failure tolerance, team size), the **options considered**, the **decision**, and crucially the **reason** - which trade-offs were accepted and why. That last part is what makes the document valuable a year later, when someone asks "why is it built like this?" and the honest answer is either a recorded, deliberate trade-off or an embarrassing shrug.

For the diagram that usually accompanies it, the [C4 model](https://c4model.com/) is a sensible, low-ceremony way to draw software at a few levels of zoom without inventing your own notation. But the prose matters more than the picture. The picture shows what was built. The prose explains why - and why is the part that decays from memory first.

## What this section covers

This post is the foundation. The rest of the Software Engineering section goes deeper into the craft: API design and the contract mindset, when a language like [Rust](https://www.rust-lang.org/) earns its complexity and why [Go](https://go.dev/) keeps winning backend work, testing strategy, debugging as a discipline, code review that improves code rather than just catching bugs, the design patterns still worth knowing, concurrency models compared, and how to name and pay down technical debt.

The connecting thread is the one in this post: software engineering is not the accumulation of correct answers. It is the practised judgement to see the trade-offs and choose well.

## Related Reading

- [Kubernetes in 2026 - Is It Still Worth the Complexity Tax?](/devops/kubernetes-2026-complexity-tax/)
- [Platform Engineering in 2026: What It Is and Why DevOps Teams Are Adopting It](/devops/platform-engineering-2026/)
- [Context Engineering: The Discipline That Replaced Prompt Engineering](/ai/context-engineering/)
- [Apache Iceberg in 2026: The Open Table Format That Won](/data-engineering/apache-iceberg-2026/)
