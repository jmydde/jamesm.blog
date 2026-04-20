---
title: "DevOps Explainers"
date: 2023-12-16T09:36:18+01:00
draft: false
tags: ['devops', 'education', 'explainer', 'api', 'database', 'dns', 'git', 'linux', 'programming']
description: "Short explainer posts on DevOps fundamentals - APIs, databases, DNS, Git, Linux, and programming languages - paired with the best explanatory content I have found."
---

Most engineering concepts are easier than they look once someone explains them clearly. This page collects short explainer notes on the fundamentals I find myself re-explaining most often, each paired with the best external visual or video I have found on the topic.

## APIs

An API is a contract: this is what I will accept, this is what I promise to return, this is how I will behave when something goes wrong. Everything else - REST, GraphQL, gRPC, WebSockets - is just a different way of expressing that contract over the wire.

### Types of API testing

There are nine commonly-cited categories of API test: functional, load, security, reliability, runtime error, validation, UI, penetration, and fuzz. In practice most teams do contract tests and load tests well, security tests occasionally, and the rest intermittently.

{{< x user="alexxubyte" id="1717566324208230449" >}}

### API vs SDK

An API is the contract; an SDK is a wrapper library that makes calling the API in a specific language less painful. You can always call the API directly - you almost never should, because the SDK handles retries, pagination, auth, and rate limits for you.

{{< x user="alexxubyte" id="1717924971195097136" >}}

## Databases

### Six database types worth knowing

Relational, document, key-value, column-family, graph, and time-series. Most production systems use more than one, picked per workload rather than chosen as a single organisational standard. "Polyglot persistence" is the term, and the hard part is not picking the database - it is keeping them in sync.

{{< x user="AmigosCode" id="1717498576702435477" >}}

### Why is Redis fast

The short answer: everything lives in memory, the data structures are purpose-built, and the single-threaded event loop avoids lock contention. The longer answer involves the specifics of epoll, the Redis protocol, and pipelining.

{{< x user="sahnlam" id="1718864218597019747" >}}

## DNS

DNS is the phone book of the internet, and like a phone book it is eventually consistent, aggressively cached, and occasionally wrong. Most production outages I have seen that looked like "the internet is broken" were actually DNS - either a stale record, a propagation delay, or a resolver misconfigured somewhere.

{{< x user="hackinarticles" id="1718732714394759429" >}}

## Git

Git's popularity comes down to three things: it is distributed (every clone is a full copy), branching is cheap enough to be a casual operation, and the content-addressable object model is surprisingly simple once you understand it. The confusion most people hit comes from the command-line interface, which is famously inconsistent, rather than from the model underneath.

{{< x user="sahnlam" id="1718104645665693906" >}}

## Linux

### How the Linux boot process works

BIOS or UEFI hands control to the bootloader (usually GRUB), which loads the kernel and an initial RAM disk. The kernel mounts the root filesystem and launches PID 1 (systemd on most modern distributions), which then starts every other service according to its dependency graph.

{{< youtube XpFsMB6FoOs >}}

## Programming Languages

### How C++, Java, and Python differ under the hood

C++ compiles directly to machine code and has no runtime garbage collector - you manage memory yourself. Java compiles to bytecode which runs on the JVM, with a garbage collector and a JIT compiler that optimises hot paths. Python is interpreted (CPython reads bytecode at runtime), dynamically typed, and significantly slower than either for CPU-bound work - which is why the scientific ecosystem pushes heavy computation into C extensions via NumPy and friends.

{{< x user="alexxubyte" id="1716478069945532810" >}}

## Further reading

- [High Performance Browser Networking](https://hpbn.co/) - Ilya Grigorik's free book covering TCP, TLS, HTTP, and WebRTC in illustrated depth
- [Julia Evans' zines](https://wizardzines.com/) - illustrated explainers on Linux, networking, Git, and debugging

## Related Pages

- [DevOps Cheatsheets]({{< ref "/devops/cheatsheets" >}}) - reference material to pair with these concepts
- [DevOps Best Practices]({{< ref "/devops/best-practices" >}})
