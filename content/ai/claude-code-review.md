---
title: "Claude Code Just Got a Serious Code Review Feature"
date: 2026-03-09T07:14:25+01:00
draft: false
tags: ['ai', 'claude', 'code reviews']
---

I genuinely think a lot of people still underestimate how fast the AI developer tooling ecosystem is evolving.

A good example of that is the new **Code Review** feature in Claude Code, which Anthropic just released in research preview.

Docs: https://code.claude.com/docs/en/code-review

At first glance it sounds like another "AI reviews your code" feature. We've had plenty of those.

But when you look closer, this one is actually quite different.

Most automated code review tools are basically static analysis with a large language model wrapped around them. They skim the diff, leave a few comments, maybe point out a style issue or a possible bug.

Claude Code’s new system takes a very different approach.

Instead of running a single model pass over your pull request, it dispatches a team of AI agents to review the PR in parallel. Each agent hunts for issues from a different perspective, verifies potential bugs, and then the system ranks the findings by severity before posting a structured review.

The result is a single high-signal review comment plus inline comments directly on the relevant lines of code.

In other words, it's trying to replicate what a really good human code review actually looks like.

## The real problem this is solving

The interesting part here is not the technology. It's the problem.

AI is massively increasing the amount of code being written.

Anthropic reported that code output per engineer internally has increased by about **200% over the last year**, which created an unexpected bottleneck: code review.

If developers are shipping more code, the review process becomes the limiting factor.

Humans skim.

We all do it.

You open a PR with 600 lines changed, scroll through the diff, and give it a quick approval because everything looks fine.

That works right up until the one-line change that silently breaks authentication in production.

Apparently that exact scenario already happened internally. A one-line diff that looked trivial was flagged by Claude Code Review as a critical issue that would have broken authentication for a service.

That’s the type of bug humans miss all the time.

## Multi-agent review is the interesting part

The architecture is what makes this feature interesting.

Instead of one model doing a shallow scan, Claude Code:

- launches multiple review agents
- runs bug detection in parallel
- cross-checks findings to filter false positives
- ranks issues by severity before posting feedback

The agents analyse changes from different angles and only high-confidence issues are surfaced, which dramatically reduces noise in the review.

Anyone who has used traditional static analysis tools knows how big a deal that is. False positives are what make people ignore automated reviews.

If the signal is clean, developers actually pay attention.

## It scales with the size of the PR

Another clever detail is that the review depth scales with the change.

Small PRs get a lightweight pass.  
Large or complex PRs get a deeper analysis with more agents.

Reviews typically take around **20 minutes to run** and cost roughly **$15-$25 per review**, since the system is token-based and designed for depth rather than speed.

That might sound expensive at first.

But compared to the cost of shipping a subtle production bug, it’s trivial.

## It doesn’t replace human review

One thing I like about the design is that it doesn't approve pull requests.

Humans still do that.

The AI’s job is simply to surface issues that reviewers might otherwise miss.

Think of it less like replacing the reviewer and more like giving every PR a **superhuman pre-review** before a human even opens the diff.

That’s a much healthier model than trying to automate approvals.

## Where this is going

What’s really happening here is something bigger.

AI is increasing code generation by an order of magnitude.

That means the rest of the software development lifecycle needs to evolve too:

- review
- testing
- debugging
- CI
- maintenance

Claude Code’s new review system feels like one of the first serious attempts to adapt **code review to the AI-generated code era**.

Instead of one developer reviewing another developer’s work, you now have AI reviewing AI-generated code before humans ever see it.

That’s a pretty wild shift in how software gets built.

And honestly, I suspect this is just the beginning.
