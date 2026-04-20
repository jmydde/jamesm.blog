---
title: "AWS re:Invent Slides (2022)"
date: 2022-12-03T11:04:16+01:00
draft: false
tags: ['aws', 'devops', 'conference', 're-invent', 'kubernetes', 'eks', 'ci-cd', 'pipeline', 'security', 'compliance', 'devsecops']
description: "Curated collection of presentation slide decks from AWS re:Invent 2022, covering DevOps, Kubernetes on EKS, CI/CD, and DevSecOps topics with short practitioner summaries."
---

This is the set of re:Invent 2022 slide decks I found most useful when they were published, grouped by topic. Each entry links to the official AWS-hosted PDF and carries a short, plain-language note about what the session is useful for in practice - so you can decide which decks are worth reading before committing the time.

For the full session video recordings, see the [AWS Events channel on YouTube](https://www.youtube.com/@AWSEventsChannel).

## DevOps

### [Amazon's approach to high-availability deployment](https://d1.awsstatic.com/events/reinvent/2019/REPEAT_1_Amazon's_approach_to_high-availability_deployment_DOP404-R1.pdf.pdf)

The practices Amazon's own delivery teams use to reach near-zero deployment failure rates. Most of the value is in the guardrail patterns - pre-production gates, automated rollback triggers, and how to design a release process that protects itself from human error.

### [Automating cross-account CI/CD pipelines](https://d1.awsstatic.com/events/reinvent/2021/Automating_crossaccount_CICD_pipelines_REPEAT_DOP402-R1.pdf)

A worked example of multi-account deployment using CDK, CodePipeline, and CloudFormation. Useful if you are moving from a single-account delivery setup to the recommended multi-account model and want a reference architecture to adapt.

### [Continuous improvement of code quality with Amazon CodeGuru](https://d1.awsstatic.com/events/reinvent/2020/Continuous_improvement_of_code_quality_with_Amazon_CodeGuru_DOP403.pdf)

Onboarding, architecture, and pipeline integration patterns for CodeGuru. Worth reading if you are evaluating ML-assisted code review tooling, though the market has shifted significantly since 2022 and newer AI-native options now compete directly.

### [Continuous security and compliance for your CI/CD pipeline](https://d1.awsstatic.com/events/reinvent/2021/Continuous_security_and_compliance_for_your_CICD_pipeline_REPEAT_DOP401-R2.pdf)

Shift-left security patterns using CodeGuru Reviewer, CloudFormation Guard, and AWS Config. A useful menu of checkpoints to consider adding to an existing pipeline, rather than a prescriptive blueprint.

### [Deep dive into AWS Cloud Development Kit](https://d1.awsstatic.com/events/reinvent/2019/REPEAT_1_Deep_dive_into_AWS_Cloud_Development_Kit_DOP402-R1.pdf)

Introduction to building AWS infrastructure with the CDK - constructs, stacks, applications - in your language of choice. The right starting point if you are considering CDK over raw CloudFormation or Terraform.

### [Implementing DevSecOps pipelines with compliance in mind](https://d1.awsstatic.com/events/Summits/reinvent2022/DOP402-R_Implementing-DevSecOps-pipelines-with-compliance-in-mind.pdf)

Pattern for a pipeline that includes software composition analysis, SAST, and DAST, with vulnerability findings aggregated into a single view. Practical if you are building out a pipeline from scratch and want to understand where each scanning stage fits.

### [Multi-account and multi-Region deployments at scale](https://d1.awsstatic.com/events/Summits/reinvent2022/DOP403-R_Multi-account-and-multi-Region-deployments-at-scale.pdf)

Options for deploying into many accounts and regions, including GovCloud, and how to align deployment targets with AWS Control Tower organisational units. Useful if you are about to hit the wall where a single account is no longer sufficient.

## Kubernetes (EKS)

### [Amazon EKS SaaS: Building a working multi-tenant environment](https://d1.awsstatic.com/events/Summits/reinvent2022/SAS401-R_Amazon-EKS-SaaS-Building-a-working-multi-tenant-environment.pdf)

End-to-end walk through building a multi-tenant SaaS on EKS, including onboarding, tenant isolation, tiering, cost attribution, and data partitioning. Strong reference if you are architecting a SaaS product on Kubernetes rather than starting from scratch.

### [Best practices for using Amazon EKS add-ons](https://d1.awsstatic.com/events/Summits/reinvent2022/CON201_Best-practices-for-using-Amazon-EKS-add-ons.pdf)

How to manage the operational software layer on EKS clusters - networking, observability, autoscaling - as a consistent, versioned set of add-ons rather than ad-hoc installs.

### [Best practices platform teams can use to streamline Kubernetes operations](https://d1.awsstatic.com/events/Summits/reinvent2022/PRT002_Best-practices-platform-teams-can-use-to-streamline-Kubernetes-operations-sponsored-by-Rafay-Systems.pdf)

Partner-sponsored session on scaling platform engineering practices across many EKS clusters and application teams. Some vendor-specific framing, but the organisational patterns are widely applicable.

### [Bootstrapping "batteries-included" Amazon EKS clusters](https://d1.awsstatic.com/events/Summits/reinvent2022/CON403-R_Bootstrapping-batteries-included-Amazon-EKS-clusters--.pdf)

Using EKS Blueprints (Terraform) to stand up opinionated, security-compliant clusters with managed node groups, Fargate profiles, and a curated set of open-source add-ons (Karpenter, Argo CD, Load Balancer Controller, and so on). A useful fast path if you are tired of reinventing cluster bootstrap.

### [Build Kubernetes at scale using AWS file services](https://d1.awsstatic.com/events/Summits/reinvent2022/STG326_Build-Kubernetes-at-scale-using-AWS-file-services-.pdf)

Using Amazon FSx as persistent storage for containerised workloads on EKS, covering performance, high availability, and cross-region replication.

### [Data analysis with Amazon EKS and AWS Batch](https://d1.awsstatic.com/events/Summits/reinvent2022/CMP335-R_Data-analysis-with-Amazon-EKS-and-AWS-Batch.pdf)

Using AWS Batch to manage large-scale data-analysis workloads on EKS, including a worked example of training a simple ML model. Interesting if you run analytics jobs on Kubernetes and want to replace hand-rolled job orchestration.

### [Disaster recovery, high availability, and resiliency on Amazon EKS](https://d1.awsstatic.com/events/Summits/reinvent2022/CON404_Disaster-recovery-high-availability-and-resiliency-on-Amazon-EKS.pdf)

Patterns for building resilient Kubernetes clusters, including chaos-engineering techniques to simulate failures and validate recovery procedures against RTO and RPO targets.

### [Getting started with Amazon EKS](https://d1.awsstatic.com/events/Summits/reinvent2022/CON204-R_Getting-started-with-Amazon-Elastic-Kubernetes-Service-Amazon-EKS.pdf)

Introductory workshop deploying microservices on EKS with load balancing, centralised logging, and autoscaling. Useful as a refresher or as onboarding material for someone new to Kubernetes on AWS.

### [How to monitor and reduce your compute costs](https://d1.awsstatic.com/events/Summits/reinvent2022/CON405_How-to-monitor-and-reduce-your-compute-costs.pdf)

Practical cost-reduction walkthrough using OpenCost, Kubecost, Karpenter, and Graviton, with a case study from Adobe. Worth reading before you negotiate your next EKS budget.

### [Running efficient Kubernetes clusters on Amazon EC2 with Karpenter](https://d1.awsstatic.com/events/Summits/reinvent2022/CMP405-R_Running-efficient-Kubernetes-clusters-on-Amazon-EC2-with-Karpenter.pdf)

Deep dive on Karpenter as a node-lifecycle manager, including how its intent-based instance selection differs from the cluster autoscaler.

### [Simplifying Kubernetes application management with cdk8s](https://d1.awsstatic.com/events/reinvent/2020/Simplifying_Kubernetes_application_management_with_cdk8s_DOP401.pdf)

Using cdk8s to define Kubernetes applications in familiar programming languages instead of raw YAML. Worth a look if your team is drowning in YAML and considering a programmatic abstraction.

### [Spot Invaders: A fault-tolerant chaos engineering game](https://d1.awsstatic.com/events/Summits/reinvent2022/CMP001_Spot-invaders-A-fault-tolerant-chaos-engineering-game.pdf)

A genuinely playful session using an arcade-style game to teach Spot instance best practices and chaos engineering with AWS Fault Injection Simulator. Lighter content but a clever way to introduce the concepts.

## Related Pages

- [AWS Summit London 2023 - Agenda Announcement]({{< ref "/devops/aws-summit-2023" >}})
- [AWS Summit London 2023 - Full Agenda]({{< ref "/devops/aws-summit-2023-agenda" >}})
- [DevOps Conferences]({{< ref "/devops/devops-conferences" >}})
