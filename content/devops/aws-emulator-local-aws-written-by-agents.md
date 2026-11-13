---
title: "AWS Emulator: AWS Ships Its Own Local AWS, and Says Its Agents Wrote It"
date: 2026-11-13T12:00:00+00:00
draft: false
tags: ["aws", "cloud", "devops", "agent", "testing", "ai", "claude-code", "software-engineering", "open-source", "2026"]
description: "On 11 November 2026 AWS released AWS Emulator, a free local emulator of AWS APIs. The more interesting claim is how it was built: AWS says autonomous agents wrote it and no human wrote or reviewed the code. Here is what it does, what it doesn't, and how it sits next to LocalStack."
cover:
  image: /assets/images/devops/aws-emulator-local-aws-written-by-agents.jpg
  alt: AWS Emulator - glowing blue agent figures building a cloud architecture on a laptop, beside a fidelity test runner showing 501 Not Implemented results and an "IAM not evaluated" sign
---

## TL;DR

- On 11 November 2026 AWS [announced AWS Emulator](https://aws.amazon.com/blogs/aws/test-your-applications-against-aws-locally-with-aws-emulator/), a local emulator of AWS APIs that your CLI, SDKs and coding agents talk to over a local HTTPS endpoint
- It is written in Rust, has **no additional service fee**, and the code is public on [GitHub](https://github.com/aws/aws-emulator) under CC0 (public domain), apart from a vendored directory under Apache 2.0
- AWS says it is built and maintained by **autonomous agents**. Matthew Goldberg, an AWS senior principal engineer, says his team did not write or review the code
- It does **not** evaluate IAM policies, it is single-account, and state lives in memory. AWS says outright not to use it to test whether your application is secure
- [LocalStack](https://blog.localstack.cloud/aws-emulator-is-here-what-you-need-to-know/) welcomed it and positions itself as the deeper, broader platform. Everything after "My read" is opinion

For years the standard answer to "how do I test against AWS without paying for and waiting on AWS" has been a third-party emulator. Now AWS has shipped its own. I work with data pipelines that lean heavily on S3, queues and event triggers, so this one matters to me more than most launches.

## What AWS shipped

AWS Emulator runs on your machine and speaks the same AWS APIs as the real thing. You point the AWS CLI or an SDK at it with a few environment variables and your application code stays unchanged. Some details from the [AWS announcement](https://aws.amazon.com/blogs/aws/test-your-applications-against-aws-locally-with-aws-emulator/) by Daniel Abib:

- **Local only.** It listens on `127.0.0.1:9297` over HTTPS, so only your own computer can reach it. On startup it generates its own credentials and certificate
- **Same shapes as AWS.** It supports services that have models in AWS's public API models repository. Those same models drive the SDKs, so responses and errors should look like the real ones. Requests must be SigV4 signed
- **Embedded mode.** Rust projects can run it in-process as a dev-dependency, with each instance holding its own state, so parallel tests don't share buckets, tables or queues
- **No account needed.** The [README](https://github.com/aws/aws-emulator) describes it as an emulator for testing without calling AWS or needing an account

Installation is less smooth than "just works" on a Mac. On Linux there are RPM and Debian packages. On macOS and Windows you run it in Docker, and the announcement notes that no ready-made image is published, so you build one from the Dockerfile in the docs. There is also an `aws-emulator` skill for AI agents, installed with AWS CLI 2.35.0 or later, and the post names Kiro and Claude Code as agents that can use the local loop to create resources, check results and iterate without waiting on a deployment.

How many services does it cover? It depends who you ask. The AWS post doesn't give a number. [Unite.AI](https://www.unite.ai/aws-releases-local-emulator-written-entirely-by-autonomous-ai-agents/) reports it is built from "438 AWS API models covering more than 200 services". "Covers" is carrying a lot of weight there, and that brings me to fidelity.

## Fidelity is the whole game

An emulator that accepts your call and returns something plausible is worse than useless if real AWS would have rejected it. AWS's answer is a public fidelity suite. According to the announcement:

- A fidelity test is a short program that uses an AWS SDK to run a workflow and asserts AWS's behaviour, verified against real AWS
- A test passes only if the emulator matches on every call's status code, body, exact error code and message, and on the resources the workflow creates
- Unimplemented operations return HTTP 501, so a gap fails loudly instead of quietly lying to you
- Per-service scores are published with each release, and the tests, including failing ones, are public in the `aws-emulator-evaluation-suite` repository

I like the 501 decision a lot. I haven't gone through the per-service scores on the releases page, and the announcement itself doesn't publish them, so I'm not going to quote a headline fidelity figure. Before you rely on it, check the scores for the exact services you use. That is also what LocalStack tells its own users to do.

## The part that made me stop: agents wrote it

The headline for a developer is "free local AWS". The headline for the industry is how it was built. AWS says the emulator is built and maintained by agents working from the API models, on Amazon Bedrock AgentCore, CodePipeline and CodeCommit:

- **Gap-finding agents** compare the emulator against real AWS and the Smithy models, and file an issue per gap
- **Implementation agents** pick up issues, write tests, implement behaviour and review the change
- **A security agent** independently reviews changes, during development and again in the release pipeline
- **A merge gate** runs the fidelity tests before anything reaches the public repo

According to Unite.AI's write-up of Goldberg's account, his team neither wrote nor reviewed the code, and humans built the specifications, test machinery, merge gates and release pipeline. His own words on the gate: "Without this merge gate, we wouldn't trust what our agents are building."

That sentence is the interesting bit. The agents aren't trusted. The tests are. It is the same lesson I keep seeing in agentic engineering: the quality of the output tracks the quality of the verification, and an emulator is almost the ideal case because real AWS provides an oracle you can check against.

## What it won't do

The limits are stated plainly, which I appreciate:

- **IAM is not evaluated.** A request AWS would deny might succeed locally. The announcement says: "Don't use the emulator to test whether your application is secure."
- **Single account and Region.** Each emulator acts as one account (`000000000000`), with no cross-account or cross-Region behaviour
- **In-memory state.** Per the repo layout and Unite.AI's reading, resources vanish when it stops. It also generates new keys each time it starts
- **Fidelity varies by service and feature.** Not every operation behaves like AWS yet
- **Building from source is heavy.** The README asks for at least 100 GB of disk and a multi-core machine, and the repo doesn't accept pull requests, only issues

Real networking, real permissions and real service-to-service quirks still have to be tested on real AWS. This shortens the loop. It doesn't replace the last mile.

## Where LocalStack fits

LocalStack's response is gracious. It calls AWS Emulator a milestone and says the two products "are built differently". Its pitch is that AWS Emulator "emphasizes breadth, with a very wide range of AWS services", while LocalStack "emphasizes depth on the services most teams build on, including areas like IAM". It also lists persistence and state management among the things it says AWS Emulator doesn't provide, and points to IaC integrations, a web app with resource browsers, and IDE integrations as part of its wider platform. Treat that as a vendor's view of a new competitor, but the IAM and persistence differences line up with what AWS itself says about the emulator.

## My read

Everything from here is my opinion.

1. **For most teams this is a "try it on Monday" tool, not a "migrate on Monday" tool.** If your tests only need S3, SQS, DynamoDB and a few events, a free first-party emulator with a public scoreboard is hard to argue with. If you rely on IAM behaviour, persistence between runs or the surrounding tooling, LocalStack still has the edge on AWS's own admissions
2. **Agents are the real customer.** A free, isolated, disposable AWS per test run is exactly what a coding agent needs. An agent that can break things without touching a shared dev account or a bill is a much safer agent. The IAM gap cuts the other way, though: an agent can happily ship code that passes locally and is denied in production, so permissions need a real-AWS check in CI
3. **The provenance is the story.** AWS is shipping a developer product it says its agents wrote, held to account by public tests. If that holds up, expect more of this: well-specified, oracle-checkable software where the spec and tests are the human work
4. **CC0 is a notable choice.** Public domain means anyone can fork, embed or build on it. That may matter more to the emulator ecosystem than any single feature

The sensible workflow hasn't changed: iterate locally, run integration tests against the emulator, then validate on real AWS before you ship. The loop for the first two steps just got a lot cheaper.

## Related Reading

- [DevOps in the Age of AI Agents](/devops/devops-in-the-age-of-ai-agents/)
- [AWS S3 Files - Bridging File Systems and Object Storage](/devops/aws-s3-files/)
- [Self-Hosted vs Managed in 2026](/devops/self-hosted-vs-managed-2026/)

## Sources

- [AWS News Blog: Test your applications against AWS locally with AWS Emulator](https://aws.amazon.com/blogs/aws/test-your-applications-against-aws-locally-with-aws-emulator/) - announcement by Daniel Abib, 11 November 2026 (updated 12 November)
- [aws/aws-emulator on GitHub](https://github.com/aws/aws-emulator) - README, license, install options, repo layout
- [LocalStack: AWS Emulator is here. Here's what LocalStack users need to know](https://blog.localstack.cloud/aws-emulator-is-here-what-you-need-to-know/) - LocalStack's comparison and positioning
- [Unite.AI: AWS Releases Local Emulator Written Entirely by Autonomous AI Agents](https://www.unite.ai/aws-releases-local-emulator-written-entirely-by-autonomous-ai-agents/) - Matthew Goldberg's engineering account, service-model count, in-memory state
