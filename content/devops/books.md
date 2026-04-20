---
title: "DevOps Books"
date: 2023-04-21T23:07:18+01:00
draft: false
tags: ['devops', 'book', 'python', 'docker', 'kubernetes', 'terraform', 'iac', 'linux', 'programming', 'bash', 'sql', 'golang', 'sre']
description: "Recommended reading list of DevOps and infrastructure engineering books covering culture, cloud, containers, infrastructure as code, SRE, and programming languages."
---

A working DevOps engineer draws from several disciplines at once - distributed systems, operating systems, network engineering, software development, and the organisational side that keeps it all moving. The books below are the ones I have either read cover-to-cover or regularly pull off the shelf to reference. I have added a one-line note on why each one is on the list.

## Culture and Practice

The hardest problems in DevOps are usually not technical.

- [The Phoenix Project](https://www.oreilly.com/library/view/the-phoenix-project/9781457191350/) - Gene Kim's novel that dramatises the Three Ways of DevOps; a fast read that has changed how many organisations talk about delivery
- [The DevOps Handbook](https://www.oreilly.com/library/view/the-devops-handbook/9781457191381/) - the practitioner companion to The Phoenix Project, covering the concrete practices behind high-performing teams
- [Accelerate](https://itrevolution.com/product/accelerate/) - Nicole Forsgren, Jez Humble, and Gene Kim's research-backed book on what separates elite from low performers (the source of the four key DORA metrics)

## Site Reliability Engineering

- [Site Reliability Engineering (Google SRE Book)](https://sre.google/sre-book/table-of-contents/) - the founding text, free online, still the clearest definition of the discipline
- [The Site Reliability Workbook](https://sre.google/workbook/table-of-contents/) - the practical follow-up, strong on SLOs and alerting
- [Seeking SRE](https://www.oreilly.com/library/view/seeking-sre/9781491978856/) - David Blank-Edelman's collection of perspectives on how SRE plays out in different organisations

## Containers

### Docker

- [Docker Deep Dive](https://nigelpoulton.com/books/) - Nigel Poulton's annually updated guide, the fastest path from zero to productive Docker use

### Kubernetes

- [Kubernetes: Up and Running](https://www.oreilly.com/library/view/kubernetes-up-and/9781491935668/) - a comprehensive introduction from Kelsey Hightower, Brendan Burns, and Joe Beda
- [The Kubernetes Book](https://nigelpoulton.com/books/) - Nigel Poulton's pairing with his Docker book, similarly practical and regularly refreshed
- [Kubernetes Patterns](https://www.oreilly.com/library/view/kubernetes-patterns-2nd/9781098131678/) - pattern catalogue for building robust applications on Kubernetes

## Infrastructure as Code

### Terraform

- [Terraform: Up and Running](https://www.oreilly.com/library/view/terraform-up-and/9781098116736/) - Yevgeniy Brikman's book is still the best single source on production-grade Terraform, including the module patterns that keep large codebases sane

## Observability

- [Observability Engineering](https://www.oreilly.com/library/view/observability-engineering/9781492076438/) - Charity Majors, Liz Fong-Jones, and George Miranda on what modern observability actually means beyond the three-pillars cliché

## Linux

- [Linux in a Nutshell](https://www.oreilly.com/library/view/linux-in-a/9780596806088/) - the definitive single-volume reference for Linux commands and utilities
- [How Linux Works](https://nostarch.com/howlinuxworks3) - Brian Ward's walk through what is actually happening beneath the commands you type every day

## Programming Languages

### Bash

- [Learning the bash Shell](https://www.oreilly.com/library/view/learning-the-bash/0596009658/) - a careful introduction to shell programming from O'Reilly

### C and C++

- [The C Programming Language (K&R)](https://en.wikipedia.org/wiki/The_C_Programming_Language) - still the canonical text for learning C, forty years on

### Golang

- [Introducing Go](https://www.oreilly.com/library/view/introducing-go/9781491941997/) - a short, approachable introduction
- [Learning Go](https://www.oreilly.com/library/view/learning-go/9781492077206/) - Jon Bodner's longer book, strong on idiomatic Go

### Perl

- [Learning Perl](https://www.oreilly.com/library/view/learning-perl-6th/9781449311063/) - the starting point, co-authored by the language's creator
- [Programming Perl](https://www.oreilly.com/library/view/programming-perl-4th/9781449321451/) - the comprehensive reference (the "Camel Book")
- [Mastering Perl](https://www.oreilly.com/library/view/mastering-perl/9780596527242/) - for when you need to move beyond the basics

### Python

- [Dive Into Python 3](https://diveintopython3.net/) - Mark Pilgrim's free online book, an effective path into modern Python
- [Fluent Python](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) - Luciano Ramalho's deep dive into Python's idioms, a must-read once you have the basics

### SQL

- [Learning SQL](https://www.oreilly.com/library/view/learning-sql-3rd/9781492057604/) - Alan Beaulieu's well-paced introduction to relational querying

## Related Pages

- [DevOps Blogs]({{< ref "/devops/blogs" >}})
- [DevOps Courses]({{< ref "/devops/devops-courses" >}})
- [Development Courses]({{< ref "/devops/dev-courses" >}})
