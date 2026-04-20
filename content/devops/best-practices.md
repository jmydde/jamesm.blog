---
title: "DevOps Best Practices"
date: 2023-12-16T09:33:18+01:00
draft: false
tags: ['devops', 'best-practice', 'microservice', 'system-design', 'architecture', 'ci-cd']
description: "Practical DevOps and system design best practices covering microservices architecture, CI/CD pipelines, observability, and scalable system design."
---

"Best practice" is a phrase that should be treated with suspicion. What works for a fintech running 500 engineers rarely works for a five-person startup. The notes below are patterns I have seen hold up across multiple organisations - but always weighed against context, team size, and what the system is actually trying to do.

## Microservices

Microservices solve organisational problems as much as technical ones. A service boundary is a team boundary in disguise.

### When to reach for microservices

- When your monolith has become a merge-conflict factory and deploys are blocking each other
- When distinct parts of the system genuinely have different scaling, reliability, or data requirements
- When multiple teams need to ship independently without coordinating every release

### Patterns worth adopting early

- **Well-defined contracts** - OpenAPI or gRPC schemas published and versioned, not a Slack message
- **Independent deployability** - a service that cannot be released without its neighbour is not really a microservice
- **Observability by default** - distributed tracing from day one, not bolted on during the first outage
- **Circuit breakers and bulkheads** - assume downstream services will fail and contain the blast radius
- **Idempotent APIs** - retries become safe, which is the whole point when the network is unreliable

### Typical tech stack

Most production microservice stacks converge on a similar shape: Kubernetes or a managed container platform for runtime, Kafka or a managed equivalent for asynchronous messaging, a service mesh such as Istio or Linkerd for mTLS and traffic policy, and OpenTelemetry feeding Prometheus, Grafana, and a tracing backend.

{{< x user="bytebytego" id="1718500151311093823" >}}

{{< x user="alexxubyte" id="1718875007798104135" >}}

## System Design

The interesting system design decisions happen before you write any code. Once you have committed to a database, a messaging pattern, or an identity model, changing direction is expensive.

### Questions worth answering up front

- What are the acceptable latency and availability targets, and who decides?
- Where is the source of truth for each piece of data, and who owns writes?
- What happens when each dependency is slow, down, or lying?
- How will you know the system is behaving correctly in production?

{{< x user="javinpaul" id="1718571820436361222" >}}

## CI/CD

A healthy pipeline is short, fast, and trusted. A pipeline that takes 40 minutes and fails flakily is worse than no pipeline - people learn to ignore it.

- **Keep main always releasable** - treat a red main branch as an all-hands incident
- **Deploy small changes often** - smaller diffs are easier to review and easier to roll back
- **Automate the rollback** - if rollback is a manual runbook, it will be too slow in the moment
- **Parallelise tests aggressively** - engineer time is more expensive than CI minutes

## Observability

The three pillars - metrics, logs, and traces - are the starting point, not the destination. What actually matters is whether you can answer "is this behaving correctly for real users?" without guessing.

- Define SLOs before you build dashboards
- Alert on symptoms (user-visible impact) not causes (CPU, memory)
- Log with structure, not prose - future-you will need to query it

## Reference reading

- [The Twelve-Factor App](https://12factor.net/) - still the clearest statement of how modern services should be built
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/) - the source text for SLOs, error budgets, and toil management
- [Microservices.io patterns](https://microservices.io/patterns/) - Chris Richardson's pattern catalogue

## Related Pages

- [CI/CD Tools]({{< ref "/devops/cicd-tools" >}})
- [Monitoring]({{< ref "/devops/monitoring" >}})
- [DevOps Books]({{< ref "/devops/books" >}})
