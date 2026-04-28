---
title: "Where Should Documentation Actually Live? Thinking Out Loud in the AI Era"
date: 2026-04-24T14:30:00+01:00
draft: true
tags: ['devops', 'documentation', 'knowledge-management', 'ai', 'workflow', 'confluence']
description: "A brainstorm - not a proposal - on where different types of documents and artefacts should live, what the source of truth should be, and how AI tooling is reshaping that question."
cover:
  image: assets/images/devops/where-should-documentation-live.jpg
  alt: Where Should Documentation Live Banner
---

This post is me thinking out loud. It is not a proposal, not a recommended pattern, and possibly not even a useful framing. I am writing it because I am actively stuck on the question, and writing in public tends to be the fastest way I find out what I have got wrong. Feel free to disagree with any of it.

The question is simple to state and hard to answer: where should different kinds of documents actually live, and how should that change now that AI tooling can read, write, and reason across all of them?

## The sprawl I am currently living with

Just within my own working week, documents and artefacts are scattered across:

- [Confluence](https://www.atlassian.com/software/confluence) for team-level knowledge bases, architecture decisions, and long-form writeups
- Jira for tickets, epics, and anything with a workflow attached
- SharePoint for policy and board-adjacent documents
- Google Docs for collaborative drafts, meeting notes, and anything that needs to be edited live
- PowerPoint and Google Slides for anything that needs to be presented
- Markdown files in [GitHub](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files) for READMEs, runbooks, and a growing pile of architecture notes
- Miro and Figma for diagrams and early-stage design thinking
- Email and chat for the things that probably should have been documents but never made it that far

Every one of these tools is good at what it does. That is part of the problem. There is no single bad choice to point at and remove. The sprawl is the natural result of each team picking the tool that fits its own job best.

The cost is not in any single tool. It is in the joints between them. A decision written up in Confluence, linked to a Jira epic, referenced in a GitHub pull request, and summarised in a slide deck for the board - that is four copies of the same thing, drifting out of sync from the moment the first one is written.

## The core tension

There are three forces pulling in different directions, and I cannot see a clean way to resolve them:

1. **Source of truth.** Every fact should have one canonical home. Anything else is a render of that home.
2. **Discoverability.** A developer, an operator, a technical PM, a product manager, a director, a VP - all of them need to find the thing that is relevant to them, in a surface they already use, without having to learn a new tool.
3. **Governance.** Not everyone should see everything. Budgets, security posture, legal drafts, and people-related documents need real access control, not just "well, it is a private page."

Optimise purely for source of truth and you end up with markdown in Git that half the business cannot read. Optimise purely for discoverability and you end up with the current sprawl, with nine copies of the same architecture diagram. Optimise purely for governance and you end up with so many locked doors that people give up and email each other attachments.

Any workflow that ignores one of these three will fail. That is the only thing I feel confident saying.

## A first attempt at principles

If I try to write down what I think I believe, the list looks something like this. I expect at least half of these to be wrong.

**1. Separate the master from the render.** Every document has a canonical location. Anything that appears elsewhere is a generated view, not an editable copy. If someone wants to change the content, they change the master and let the render update.

**2. Pick the master based on the primary author, not the primary audience.** Code documentation should live where engineers write it, because that is where it stays accurate. Board-level summaries should live where directors write them, for the same reason. The audience can be served by a render, but the master needs to live where the people who maintain it actually work.

**3. Treat engineering artefacts as docs-as-code.** Architecture decisions, runbooks, service catalogues, onboarding guides, API references - these belong in Git, as markdown, next to the code they describe. The [docs-as-code philosophy](https://www.writethedocs.org/guide/docs-as-code/) has been the right answer for a decade, and AI tooling makes it more right, not less.

**4. Treat business artefacts as docs-as-docs.** Meeting notes, OKRs, policies, board packs, customer-facing narratives - these belong in whatever collaborative doc tool the business has already standardised on. Forcing the CFO to write in markdown is not a strategy. It is a way to lose the CFO.

**5. Publish, do not duplicate.** If a piece of engineering content needs to reach a non-engineering audience, publish a rendered version into Confluence, a shared drive, or a portal, with a visible note that it is generated and a link back to the master. Do not let anyone edit the render.

**6. Build the seams, not another store.** The problem is not that we lack another place to put documents. The problem is that the seams between the places we already have are manual. Spend the effort on search, linking, and render pipelines, not on a new wiki.

## A workflow I am mentally sketching

If I force myself to draw a picture of what this might look like, it comes out something like this. I am not claiming it works. I am claiming it is the least bad thing I can currently imagine.

```
                  ┌──────────────────────────────────────────┐
                  │            DISCOVERY LAYER               │
                  │   unified search + AI agent across all   │
                  │       respects access boundaries         │
                  └────────────────────┬─────────────────────┘
                                       │
                  ┌────────────────────┴─────────────────────┐
                  │              RENDER LAYER                │
                  │  generated views, read-only, link back   │
                  │     to master ("do not edit here")       │
                  └─────────┬────────────────────┬───────────┘
                            │                    │
            ┌───────────────┴────────┐  ┌────────┴───────────────┐
            │   ENGINEERING LAYER    │  │    BUSINESS LAYER      │
            │  (master: Git + MD)    │  │  (master: Confluence,  │
            │                        │  │   Google Docs, Drive)  │
            │  ADRs, runbooks,       │  │                        │
            │  service catalogue,    │  │  meeting notes, OKRs,  │
            │  API specs, golden     │  │  policies, board packs,│
            │  paths                 │  │  strategy drafts       │
            └────────────┬───────────┘  └──────────┬─────────────┘
                         │                         │
                  ┌──────┴─────────────────────────┴─────────┐
                  │            GOVERNANCE LAYER              │
                  │   access control enforced at the store   │
                  │    renders strip or redact at boundary   │
                  └──────────────────────────────────────────┘
```

### The engineering layer

- A monorepo or a small number of repos hold the master copy of every technical document: architecture decisions (ADRs), runbooks, service definitions, platform golden paths, API specs.
- Content is written in markdown, reviewed in pull requests, and rendered through something like [MkDocs](https://www.mkdocs.org/), [Backstage TechDocs](https://backstage.io/docs/features/techdocs/), or an equivalent static site generator.
- The rendered site is the developer portal. It is searchable, linkable, and versioned with the code.
- AI agents operate directly on the markdown. They can read it, edit it, open pull requests against it, and reason about it using the same tooling they already use to reason about code.

### The business layer

- Confluence (or equivalent) remains the home of team and business knowledge that is not part of a code repository. Meeting notes, team rituals, OKRs, strategy drafts, onboarding for non-engineering roles.
- SharePoint or Google Drive remains the home of formal business documents: policies, legal drafts, and board packs.
- Neither of these tries to be the master for anything that belongs in the engineering layer.

### The render layer

- Key technical documents are rendered into Confluence automatically, with a clear "generated from Git, do not edit here" banner and a link to the source.
- Key business decisions that affect engineering are mirrored the other way, ideally as a link with a short summary rather than a full copy.
- Slide decks are generated from the underlying master documents where possible, not hand-authored from scratch every quarter.

### The governance layer

- Access is enforced by the store the content lives in, not by obscurity.
- Sensitive categories - budgets, security posture, salary bands, incident forensics, legal - live in explicitly access-controlled spaces, not in the general developer portal.
- Renders into general-access locations strip or redact anything that should not cross the boundary. If a render cannot be made safe, it does not get rendered.

### The discovery layer

- One search surface that indexes across Confluence, Git-rendered docs, Jira, and the shared drive, respecting the access controls of each.
- One ontology for ownership: every document has a known team or person responsible for it, so that staleness has an owner.
- An AI agent sitting on top of the search surface, able to answer "where is the latest architecture for X?" and hand back the master location, not a five-year-old slide deck.

## How AI tooling changes the question

Before AI tooling, the argument for docs-as-code ran into a wall at the business boundary. Non-engineering stakeholders were not going to learn markdown, Git, or pull requests. So the compromise was always to keep two worlds and hope they stayed in sync.

AI tooling weakens that wall in two directions.

**Going out:** a business user asking "what is our current authentication strategy" can get an answer generated from the engineering master without ever seeing the markdown. The model reads the source, respects the access boundary, and produces a summary in the user's preferred surface - a chat reply, a Confluence page, a slide.

**Coming in:** an engineer drafting an architecture decision can pull in the business context from Confluence, the relevant tickets from Jira, the policy constraints from SharePoint, and produce a coherent ADR, without manually reconciling four windows.

If that actually works in practice, the case for a single physical store gets weaker, not stronger. The important thing becomes the access-and-index layer, not the storage layer. Documents can live in the tool best suited to their author, as long as an AI-enabled discovery layer can traverse them for everyone else.

That is a big "if." Current AI search over enterprise content is not there yet. It hallucinates, it misses access boundaries, and it treats stale documents as equally authoritative as fresh ones. I am not willing to bet a governance model on today's tooling. I am willing to design towards where the tooling is clearly heading.

## Where I still do not have an answer

A genuine list of things I have not resolved:

- **Versioning across the boundary.** If a markdown ADR is rendered into Confluence and then the ADR changes, how do I guarantee the Confluence version either updates or gets loudly marked as stale? I have seen every "sync" solution eventually drift.
- **Editing the render.** People will try to edit the rendered version. I do not yet have a good answer for what happens to those edits - lose them, surface them as suggestions on the master, or something else.
- **Ownership of the render pipeline.** Is this a platform team responsibility, a knowledge-management team responsibility, or something new? Every org I have seen under-invests in this and the pipeline rots.
- **Tickets as documents.** Jira is both a workflow tool and a de facto document store. Epics turn into narratives. I do not know if that should be formalised or fought against.
- **The [Diátaxis](https://diataxis.fr/) question.** Even within engineering, documentation splits into tutorials, how-to guides, reference, and explanation. Do all four live in the same place, or does "reference" belong next to code and "explanation" belong somewhere more discursive? I lean towards all-in-one, but I am not sure.
- **Security documentation.** Runbooks for incidents contain details that must not leak, but they are also the thing oncall most needs to find at 3am. The access control needs to be strict without being so strict it blocks the people it is meant to serve.

## The honest summary

I do not have a good answer. I have a shape of an answer - docs-as-code for technical content, collaborative tools for business content, a render layer between them, an AI-assisted discovery layer across all of it, and explicit governance at the boundaries. But every one of those pieces has open questions I have not resolved, and the whole thing might collapse in contact with a real organisation.

What I do believe is that the question is worth taking seriously, right now, because the assumption underneath every existing documentation strategy - that humans are the only ones reading and writing these documents - is no longer true. AI agents are becoming first-class consumers and producers of organisational knowledge, and the workflow has not caught up.

If you have solved this at your organisation, or if you have tried something similar and watched it fail, I would genuinely like to hear about it. This post is an open question, not a conclusion.
