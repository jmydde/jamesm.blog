# Editorial Guide

Standards for writing and publishing on [jamesm.blog](https://jamesm.blog). Use this alongside [README.md](README.md) for setup and [ROADMAP.md](ROADMAP.md) for planned posts.

## Post archetypes

Not every page is an essay. Pick one shape before you start writing.

### A. Analysis essay (default for long-form)

**Target:** 1,200-2,500 words. The default format for new posts.

**Required frontmatter:**

```yaml
---
title: "Post Title"
date: 2026-06-30T08:00:00+01:00
draft: false
tags: ["tag1", "tag2"]
description: "One sentence for SEO and social previews"
cover:
  image: /assets/images/<category>/slug.jpg
  alt: Descriptive alt text
---
```

**Required sections:**

- `## TL;DR` - 4-7 bullets with dates, numbers, and 1-2 inline source links
- Opening paragraph - thesis; one disclaimer if making claims outside your expertise
- 3-5 `##` sections with a single argumentative arc
- `## Related Reading` - 3-5 links from the same topic cluster

**Recommended for timely or claims-heavy posts:**

- `## What I'm Watching` - forward-looking hooks
- `## Sources` - primary links grouped at the bottom
- Closing disclaimer for finance, medical, or legal-adjacent claims

**Gold standard:** [content/ai/openai-ipo-chatgpt-market-share.md](content/ai/openai-ipo-chatgpt-market-share.md)

**Scaffold:** `hugo new ai/my-post.md --kind essay`

### B. Reference / hub page

**Target:** curated reading path, not an essay.

**Required frontmatter:**

```yaml
---
title: "Series Name: Short Description"
date: 2026-06-30T08:00:00+01:00
draft: false
type: reference
series: ["Series Name"]
tags: ["ai", "topic"]
description: "What this reading path covers and who it is for"
cover:
  image: /assets/images/<category>/slug.jpg
  alt: Series banner
slug: "series-slug"
---
```

**Required sections:**

- `## TL;DR` - what the series answers and read order
- Ordered reading list (`## Start here`)
- Optional `## Supporting reading` and `## Related paths`
- Link to `/series/<slug>/` index

**Examples:** [content/ai/trust-series.md](content/ai/trust-series.md), [content/ai/four-futures-series.md](content/ai/four-futures-series.md)

**Scaffold:** `hugo new ai/my-series.md --kind reference`

### C. Resource list

**Target:** books, links, courses, gear lists, news roundups.

**Required:** `description`, `cover` (may reuse an image from a related essay).

**Optional:** short intro paragraph. No TL;DR required.

**Examples:** [content/personal-development/books.md](content/personal-development/books.md), category `blogs.md` files.

**Scaffold:** `hugo new <category>/my-list.md` (default archetype)

---

## Section conventions

### TL;DR

- Lead with the event or claim, not background
- Include at least one hard number and one date when the post is timely
- Put the strongest source link on the most controversial bullet
- Do not duplicate the opening disclaimer (pick TL;DR or intro, not both)

### Related Reading

Every link must share **at least two tags** with the post, or sit in the **same declared series**.

Prefer posts that extend the argument, not loosely adjacent topics.

### Sources

Add `## Sources` when the post includes:

- Analyst forecasts
- Market share or revenue figures
- Legal or regulatory filings
- Pre-release rumours reported by press

Prefer primary sources (SEC filings, company newswire, investor presentations) over aggregators.

### Inline internal links

Target 2-4 contextual internal links inside the body, not only in Related Reading.

### Punctuation

Do not use em dashes (`—`). Use a spaced hyphen instead: ` - `

See [.cursor/rules/blog-punctuation.mdc](.cursor/rules/blog-punctuation.mdc).

---

## Voice and structure

### Opening hooks

Open with tension or a surprising fact. Avoid restating the title in prose.

### Section titles

H2s should carry argument ("The $2.22 Problem", "Why a Decade?") not label ("Overview", "Conclusion").

### Visual anchors

For posts comparing three or more figures, add one ASCII table or timeline. See [content/general/human-advancement-acceleration.md](content/general/human-advancement-acceleration.md).

### Disclaimers

One disclaimer in the intro **or** a footnote at the end. Not both TL;DR and intro and closing.

### Media blocks

YouTube embeds and trailers go after the argument, under a clearly labeled appendix section.

---

## Metadata

| Field | Rule |
|-------|------|
| `date` | ISO 8601 with timezone, e.g. `2026-04-28T14:30:00+01:00` |
| `tags` | Singular nouns (`ai`, `gaming`, `economics`). Avoid category name as tag. |
| `description` | One sentence; used for SEO and social previews |
| `cover.image` | `/assets/images/<category>/<slug>.jpg` under `static/` |
| `series` | Use for multi-post reading paths; pair with a hub page |

### Images

Place cover images at:

```
static/assets/images/<category>/<slug>.jpg
```

Reference in frontmatter as `/assets/images/<category>/<slug>.jpg`.

---

## Publish checklist

Before setting `draft: false`:

1. Frontmatter complete (`title`, `date`, `tags`, `description`, `cover`)
2. `## TL;DR` present (analysis essays only)
3. External links verified
4. No em dashes (`—`)
5. Related Reading passes topical rubric (shared tags or same series)
6. `## Sources` added if 3+ external factual claims
7. Cover image exists at referenced path
8. Preview with `hugo server -D` or `./hugo.server.dev.sh`

### Monthly news drafts

Posts from [scripts/generate-monthly-news.sh](scripts/generate-monthly-news.sh) ship as drafts. Before publishing:

1. Review and edit content
2. Add cover image
3. Audit sources and Related Reading
4. Set `draft: false`

---

## Backfill priorities

Do not retrofit all posts. Prioritize in waves:

1. **Wave 1** - Cornerstone published essays missing TL;DR or Related Reading
2. **Wave 2** - Claim-heavy posts missing Sources
3. **Wave 3** - Hub pages for series clusters
4. **Wave 4** - Draft backlog (see [DRAFTS.md](DRAFTS.md))

**Leave alone:** resource lists, tweet embeds, short link collections.

---

## Series index

| Series | Hub page | Index URL |
|--------|----------|-----------|
| Trust | [trust-series.md](content/ai/trust-series.md) | `/series/trust/` |
| Four Futures | [four-futures-series.md](content/ai/four-futures-series.md) | `/series/four-futures/` |
| AI Economics | [ai-economics-hardware.md](content/ai/ai-economics-hardware.md) | - |
| Gaming | [gaming-hub.md](content/gaming/gaming-hub.md) | `/gaming/` |
