---
title: "CI/CD Tools"
date: 2022-08-21T11:51:18+01:00
draft: false
tags: ['ci-cd', 'devops', 'continuous-delivery', 'automation', 'kubernetes', 'pipeline']
description: "Overview of popular CI/CD and continuous delivery tools - managed services, self-hosted platforms, and GitOps systems - for automating software builds, testing, and deployments."
---

CI/CD is the plumbing that turns a commit into running software. The tools below cover the full spectrum - from fully managed SaaS that you never have to operate, to self-hosted automation servers you tune yourself, to GitOps controllers that treat your Kubernetes cluster as the deployment target.

## How to choose

A few questions that tend to cut through the vendor noise:

- Is your code in GitHub, GitLab, or Bitbucket? Staying in-ecosystem reduces integration effort dramatically
- Do you deploy to Kubernetes? GitOps tools like Argo CD and Flux are often a better fit than traditional pipelines
- Do you want to operate the control plane yourself? Jenkins gives you maximum flexibility and maximum operational burden
- How many parallel runners will you need at peak, and who pays for them?

## Hosted CI/CD platforms

Low operational overhead, tight integration with their source-control parents, and usage-based pricing.

- [GitHub Actions](https://github.com/features/actions) - the default for anything hosted on GitHub, with a huge marketplace of community actions
- [GitLab CI/CD](https://about.gitlab.com/) - built into GitLab, covering plan-to-production in a single product
- [CircleCI](https://circleci.com/) - long-standing hosted CI with strong caching and parallelism features
- [Buildkite](https://buildkite.com/) - hybrid model where the control plane is hosted but your runners execute the work
- [Travis CI](https://www.travis-ci.com/) - one of the earlier hosted CI services, still widely used in open source

## Cloud-provider pipelines

Tightly integrated with the rest of the provider's services, which matters more as your deployment targets grow.

- [AWS CodePipeline](https://aws.amazon.com/codepipeline/) - continuous-delivery orchestration across CodeBuild, CodeDeploy, and CodeArtifact
- [Azure DevOps](https://azure.microsoft.com/en-gb/products/devops) - version control, boards, pipelines, artefacts, and test plans in one suite
- [Google Cloud Build](https://cloud.google.com/build) - container-native builds that integrate cleanly with Cloud Run and GKE

## Self-hosted automation servers

Full control, rich plugin ecosystems, and the operational burden that comes with both.

- [Jenkins](https://www.jenkins.io/) - the original open-source automation server, with hundreds of plugins and a loyal operator community
- [TeamCity](https://www.jetbrains.com/teamcity/) - JetBrains' build server, free for small teams and strong at .NET and JVM ecosystems
- [Drone](https://www.drone.io/) - container-native CI that runs every step as a Docker container

## GitOps and Kubernetes-native delivery

Declarative continuous deployment where the cluster state is reconciled from Git.

- [Argo CD](https://argo-cd.readthedocs.io/en/stable/) - declarative, GitOps continuous delivery for Kubernetes, with a clear UI for drift detection
- [Flux](https://fluxcd.io/) - the other major GitOps controller, now part of the CNCF
- [Spinnaker](https://spinnaker.io/) - multi-cloud continuous delivery originally built at Netflix, strong at complex deployment strategies

## Release strategy helpers

Pipelines handle build and deploy, but progressive delivery - canaries, blue/green, feature flags - usually needs dedicated tooling.

- [Argo Rollouts](https://argoproj.github.io/rollouts/) - advanced deployment strategies for Kubernetes workloads
- [LaunchDarkly](https://launchdarkly.com/) - feature-flag platform that decouples deploy from release
- [Flagger](https://flagger.app/) - progressive delivery operator for Kubernetes

## Further reading

- [Continuous Delivery (Humble & Farley)](https://continuousdelivery.com/) - the book that still defines the terminology
- [DORA State of DevOps reports](https://dora.dev/research/) - annual research on what distinguishes high-performing delivery teams

## Related Pages

- [DevOps Best Practices]({{< ref "/devops/best-practices" >}})
- [Monitoring]({{< ref "/devops/monitoring" >}})
