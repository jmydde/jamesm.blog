---
title: "DevOps GitHub Projects"
date: 2023-05-29T06:45:18+01:00
draft: false
tags: ['airflow', 'apache', 'devops', 'github', 'cli', 'terminal', 'kubernetes', 'scheduling', 'sre', 'linux', 'open-source']
description: "Curated collection of essential open-source DevOps projects on GitHub - SRE learning resources, Kubernetes tooling, Linux utilities, and workflow schedulers."
---

Most of what makes a productive DevOps engineer is not hidden inside vendor portals - it lives in open source, on GitHub, and it is free. The projects below are the ones I return to most often, whether for learning, daily tooling, or reference implementations of patterns that would otherwise take weeks to work out alone.

## DevOps and Site Reliability Engineering (SRE)

Resources to calibrate what good looks like in the discipline.

- [Awesome Scalability](https://github.com/binhnguyennus/awesome-scalability/) - a reading list illustrating patterns of scalable, reliable, performant large-scale systems
- [Awesome Site Reliability Engineering](https://github.com/dastergon/awesome-sre/) - a curated list of SRE and production engineering resources
- [DevOps Exercises](https://github.com/bregman-arie/devops-exercises/) - interview-style questions and practical exercises, useful whether or not you are job-hunting
- [DevOps Resources](https://github.com/bregman-arie/devops-resources/) - companion to the above, with a structured learning roadmap
- [DevOps Roadmap](https://github.com/milanm/DevOps-Roadmap/) - a step-by-step visual guide to becoming a DevOps engineer, updated yearly
- [roadmap.sh DevOps](https://roadmap.sh/devops) - the DevOps track from the widely-used roadmap.sh project
- [DevOps Tools](https://github.com/collections/devops-tools/) - GitHub's own curated collection
- [How They SRE](https://github.com/upgundecha/howtheysre/) - publicly available SRE resources organised by company, invaluable for benchmarking practices

## Kubernetes

Day-to-day operational tooling that pays back the installation time within a week.

- [k9s](https://github.com/derailed/k9s/) - a terminal UI for interacting with Kubernetes clusters; once you use it, the raw `kubectl` workflow feels archaic
- [kubectx / kubens](https://github.com/ahmetb/kubectx) - fast context and namespace switching, a small tool that saves real time every day
- [Lens](https://github.com/lensapp/lens) - desktop IDE for Kubernetes, good for visual inspection and debugging
- [kOps](https://github.com/kubernetes/kops/) - provisioning, upgrading, and lifecycle management for production-grade Kubernetes clusters
- [KoPylot](https://github.com/avsthiago/kopylot/) - AI-assisted Kubernetes operations, an interesting pointer to where cluster management is heading
- [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics/) - surfaces Kubernetes object state as Prometheus metrics
- [Kubernetes Dashboard](https://github.com/kubernetes/dashboard/) - the official web UI
- [Kubespray](https://github.com/kubernetes-sigs/kubespray/) - cluster lifecycle management with Ansible playbooks
- [minikube](https://github.com/kubernetes/minikube/) - local Kubernetes clusters on macOS, Linux, and Windows
- [kind](https://github.com/kubernetes-sigs/kind) - Kubernetes-in-Docker, faster than minikube for CI use cases
- [Popeye](https://github.com/derailed/popeye/) - sanitises running clusters, flags misconfigurations and anti-patterns
- [k3s](https://github.com/k3s-io/k3s) - lightweight Kubernetes distribution, excellent for edge and home-lab use

## Linux and the terminal

Modern replacements for the classic Unix toolchain. Adopting even two or three of these will change how you work.

- [bat](https://github.com/sharkdp/bat/) - `cat` with syntax highlighting and Git-aware diff marks
- [ripgrep](https://github.com/BurntSushi/ripgrep) - the `grep` replacement, fast enough to change how you search code
- [fd](https://github.com/sharkdp/fd) - a simple, fast alternative to `find`
- [fzf](https://github.com/junegunn/fzf) - fuzzy finder, pairs beautifully with shell history and file navigation
- [pueue](https://github.com/Nukesor/pueue/) - command-line task queue for managing long-running jobs
- [specctl](https://github.com/awslabs/specctl/) - translates Kubernetes objects to ECS and vice versa, useful when migrating between orchestrators
- [Test your SysAdmin skills](https://github.com/trimstray/test-your-sysadmin-skills/) - interview questions for systems administrators

## Workflow and Scheduling

- [Airflow](https://github.com/apache/airflow/) - the long-established Python-based workflow orchestrator, still the default for data pipelines
- [Prefect](https://github.com/PrefectHQ/prefect) - a modern alternative to Airflow with a more Pythonic API
- [Dagster](https://github.com/dagster-io/dagster) - data-aware orchestration, strong type system, popular with data-engineering teams
- [dkron](https://github.com/distribworks/dkron/) - distributed, fault-tolerant cron for cloud-native environments
- [Temporal](https://github.com/temporalio/temporal) - workflow engine for long-running, stateful applications, used heavily in fintech

## Infrastructure as Code and GitOps

- [Terraform](https://github.com/hashicorp/terraform) - the de-facto standard for declarative infrastructure
- [OpenTofu](https://github.com/opentofu/opentofu) - the community fork of Terraform, worth watching as the licensing situation evolves
- [Pulumi](https://github.com/pulumi/pulumi) - infrastructure as code in real programming languages (TypeScript, Python, Go)
- [Argo CD](https://github.com/argoproj/argo-cd) - GitOps continuous delivery for Kubernetes
- [Flux](https://github.com/fluxcd/flux2) - the other major GitOps controller

## Related Pages

- [CI/CD Tools]({{< ref "/devops/cicd-tools" >}})
- [Monitoring]({{< ref "/devops/monitoring" >}})
- [DevOps Best Practices]({{< ref "/devops/best-practices" >}})
