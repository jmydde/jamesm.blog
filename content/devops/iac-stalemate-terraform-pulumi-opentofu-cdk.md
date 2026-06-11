---
title: "The IaC Stalemate: Terraform, Pulumi, OpenTofu, and CDK in 2026"
date: 2026-05-13T08:00:00+01:00
draft: true
tags: ["devops", "iac", "terraform", "pulumi", "opentofu", "cdk"]
description: "Infrastructure as Code in 2026 has settled into a four-way stalemate that nobody predicted. A practical look at Terraform, Pulumi, OpenTofu, and CDK - what each is genuinely good at, where each is fading, and which one you should actually pick today."
cover:
  image: /assets/images/devops/platform-engineering-2026.jpg
  alt: The IaC Stalemate - Terraform Pulumi OpenTofu CDK Banner
---

For most of the cloud-infrastructure era, Infrastructure as Code meant Terraform. Other options existed; almost none of them were a credible default. In 2026 that single-winner picture has fractured. Terraform's licence change in 2023 split the community. Pulumi has consolidated its position in the "real programming language" niche. OpenTofu has emerged as the credible open-source fork. AWS CDK has eaten the AWS-only segment. The result is a four-way stalemate where the answer to "which IaC tool" depends on choices that did not exist three years ago.

## What happened

The 2023 licence change is worth recounting briefly because it shapes everything else. HashiCorp changed Terraform's licence from Mozilla Public License (open source) to Business Source License (source-available, with restrictions on competing with HashiCorp). This was framed as a defensive move against cloud providers running Terraform as a managed service. The community response was significant.

OpenTofu - originally OpenTF - was the response. The Linux Foundation took over the last MPL-licensed Terraform commit and continued development as an open-source fork. By 2024 OpenTofu had achieved feature parity with Terraform on the things that mattered to most users. By 2026 it has diverged enough that the choice between them is a real one.

Meanwhile Pulumi continued its strategy of providing IaC in real programming languages (TypeScript, Python, Go, C#), and AWS CDK consolidated its position as the IaC story for AWS-only deployments.

## The 2026 picture

**Terraform** (now HashiCorp Terraform) remains the most widely-deployed IaC tool. The HashiCorp Cloud Platform offering is mature, the enterprise features (private registries, state management, policy as code with Sentinel) are well-developed, and the existing investment most organisations have in Terraform means switching costs are real.

Terraform fits when:
- You are already heavily invested in Terraform.
- You want the commercial backing and roadmap of HashiCorp.
- You use HCP Terraform or Terraform Cloud as a managed service.
- The licence change does not concern you operationally.

**OpenTofu** is the credible open-source alternative. The Linux Foundation backing has produced a project that is unambiguously open source, with a governance structure that addresses the concerns that led to the fork. OpenTofu has shipped features that Terraform has not (state encryption, removed blocks for resource removal, dynamic functions), and the community has been responsive.

OpenTofu fits when:
- You want pure open-source IaC without commercial restrictions.
- You are starting a new project and want optionality.
- The OpenTofu-specific features (state encryption, others) are valuable to you.
- You are concerned about vendor lock-in to HashiCorp specifically.

**Pulumi** has carved out a specific niche: IaC that is actual code. The pitch is that you write infrastructure in TypeScript or Python or Go or C#, with full IDE support, real testing, real abstraction, real composition. For teams that find HCL frustrating, this is a genuine alternative.

Pulumi fits when:
- Your team strongly prefers real programming languages over DSLs.
- You need significant programmatic infrastructure generation.
- You want to share code between application and infrastructure layers.
- The somewhat different state model (Pulumi has its own) suits your needs.

**AWS CDK** is the answer for AWS-only organisations. Generates CloudFormation underneath, uses real programming languages, integrates deeply with the AWS ecosystem. For teams that are committed to AWS and do not need cross-cloud support, CDK provides better AWS-specific abstractions than the cross-cloud tools.

CDK fits when:
- You are AWS-only and committed to staying that way.
- You want the deepest possible AWS integration.
- The CloudFormation underneath does not bother you.
- You can accept the CDK's slower-than-Terraform pace of feature support.

## Migration patterns

The migration patterns that have emerged in 2026:

**Terraform to OpenTofu** is the cleanest migration. State files are compatible, the syntax is the same, the providers work. Most teams that decide to move have done so without significant friction.

**Terraform to Pulumi** is harder. Different state model, different conceptual approach, different debugging experience. Teams that move usually do so for ideological reasons about wanting real code, and the migration is treated as a multi-month project rather than a tool swap.

**Terraform to CDK** is rare except for AWS-heavy organisations consolidating their stack. Usually motivated by a desire to simplify rather than to gain capabilities.

**No migration** is the most common path. Most organisations using Terraform in 2023 are still using Terraform in 2026, possibly with HCP Terraform managed services. The licence change generated a lot of noise but produced relatively little actual movement.

## What the comparison actually looks like

The honest comparison across the four:

**Ecosystem.** Terraform still has the deepest provider ecosystem. OpenTofu has closed most of the gap. Pulumi covers the major clouds well but has thinner coverage on long-tail providers. CDK is AWS-only.

**Tooling.** Terraform and OpenTofu share the same tooling lineage with broad IDE and CI support. Pulumi gets the benefit of language-native tooling - the IDE experience is meaningfully better. CDK shares Pulumi's language-native advantage.

**State management.** Terraform/OpenTofu use the same state model with file-based or remote state. Pulumi has its own service for state by default but supports self-hosted. CDK uses CloudFormation underneath and has no separate state concept.

**Testing.** Pulumi and CDK win here clearly - real programming languages mean real unit testing. Terraform and OpenTofu have improved their testing story but it remains less ergonomic.

**Performance at scale.** All four have edge cases at very large state files (10,000+ resources). The handling of these has improved across all four but remains an area where bespoke engineering is sometimes needed.

**Commercial backing.** Terraform has HashiCorp, Pulumi has Pulumi the company, CDK has AWS. OpenTofu is foundation-governed which is a different kind of backing.

## What you should actually pick

For a new project in 2026:

- **Multi-cloud or cloud-agnostic, want open source** → OpenTofu
- **Multi-cloud or cloud-agnostic, want commercial support** → Terraform
- **Want real code rather than DSL** → Pulumi
- **AWS-only with no multi-cloud ambition** → CDK
- **Already using Terraform and happy** → Stay on Terraform

For an existing project: the cost of switching is usually larger than the benefit. The right move is usually to stay on what you have and direct effort toward using it well rather than choosing differently.

## The interesting longer-term question

The deeper question this raises is whether the IaC category itself is approaching maturity. The features that distinguish the four tools have narrowed over time. The remaining differences are mostly about philosophy and ecosystem rather than fundamental capability. This is the pattern of a maturing category.

What replaces it? The candidate answer is that the next generation of infrastructure abstraction will be at the application layer - tools like Wing, Eventual, or Encore that generate infrastructure from application code descriptions, rather than tools that describe infrastructure separately. These are still early. Whether they grow into the next dominant pattern remains to be seen.

For now, the IaC choice is real and consequential, but it is not a choice between dramatically different things. All four options can produce working production infrastructure. The differentiation is in the friction of getting there and the ergonomics of operating it over time.

## Related Reading

- [Platform Engineering in 2026](/devops/platform-engineering-2026/)
- [Internal Developer Platforms in 2026](/devops/internal-developer-platforms-2026/)
- [Self-Hosted vs Managed in 2026](/devops/self-hosted-vs-managed-2026/)
- [Database Operations in 2026](/devops/database-operations-2026/)
- [Kubernetes 2026: The Complexity Tax](/devops/kubernetes-2026-complexity-tax/)
