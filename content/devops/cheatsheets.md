---
title: "DevOps Cheatsheets"
date: 2023-12-16T09:28:18+01:00
draft: false
tags: ['devops', 'cheatsheet', 'cloud', 'reference', 'linux', 'kubernetes', 'aws']
description: "Quick reference guides and cheatsheets for DevOps tools, cloud computing concepts, Linux commands, and Kubernetes operations."
---

Cheatsheets are one of the most under-rated learning tools in the DevOps toolbox. When you are three hours into debugging a broken pipeline, you don't want a 400-page book - you want the one page that reminds you which flag does what. This page collects quick references I keep within arm's reach.

## Cloud Computing

A concise summary of the core cloud service models (IaaS, PaaS, SaaS), deployment patterns, and the shared responsibility model is a good starting point for anyone new to cloud infrastructure.

{{< x user="alexxubyte" id="1735700099261780259" >}}

### Official provider references

- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/) - the canonical command reference for the AWS command line
- [Google Cloud CLI cheatsheet](https://cloud.google.com/sdk/docs/cheatsheet) - the most common `gcloud` commands on a single page
- [Azure CLI quick reference](https://learn.microsoft.com/en-us/cli/azure/reference-index) - searchable index of every `az` command

## Linux and Shell

When you move between machines and distributions all day, keeping Linux fundamentals handy saves real time.

- [tldr pages](https://tldr.sh/) - a community-driven collection of simplified, example-heavy man pages
- [explainshell](https://explainshell.com/) - paste any shell command and get a plain-English breakdown of every flag
- [Bash scripting cheatsheet](https://devhints.io/bash) - a dense overview of arrays, conditionals, and expansion syntax

## Kubernetes

Kubernetes has a large surface area, and most day-to-day work is covered by a small set of `kubectl` commands.

- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/quick-reference/) - the official quick reference from the Kubernetes project
- [Kubernetes API Reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.29/) - the full object specification
- [k9s shortcuts](https://k9scli.io/topics/commands/) - navigation keys for the terminal UI

## Git

- [Git Cheat Sheet (GitHub)](https://education.github.com/git-cheat-sheet-education.pdf) - GitHub's one-page PDF covering branching, merging, and remotes
- [Oh Shit, Git!?!](https://ohshitgit.com/) - recovery recipes for the moments when a push goes wrong

## Related Pages

- [DevOps Explainers]({{< ref "/devops/explainers" >}}) - conceptual deep-dives to pair with these references
- [DevOps Best Practices]({{< ref "/devops/best-practices" >}})
