# Blog automation scripts

## generate-monthly-news.sh

Generates a "top 5 news stories" blog post for each configured category by
calling Claude Code in headless mode. Designed to run unattended once a month.

### What it does

For each category in the `CATEGORIES` list it asks Claude Code to:

1. Research the top 5 news stories from the last month using web search.
2. Verify every external link loads before including it.
3. Write a post following the blog conventions (frontmatter, singular tags,
   space-dash-space, original wording, `## Related Reading`).
4. Save it to `content/<category>/<category>-news-<month>-<year>.md` as a draft.

A category is skipped if a post for the current month already exists, so the
script is safe to re-run.

### Usage

```bash
# All configured categories
./scripts/generate-monthly-news.sh

# Only specific categories (handy for testing)
./scripts/generate-monthly-news.sh devops ai
```

### Configuration

Edit the variables at the top of `generate-monthly-news.sh`:

- `CATEGORIES` - which `content/<name>/` folders to generate posts for.
- `DRAFT` - `"true"` saves posts as drafts (default), `"false"` publishes them.
- `STORY_COUNT` - stories per post (default 5).
- `MODEL` - empty uses your default Claude model, or set `"opus"` / `"sonnet"`.
- `MAX_BUDGET_USD` - per-category spend cap.

### After a run

Posts are created as **drafts**. For each one:

1. Review and edit the content.
2. Add the cover image referenced in the frontmatter
   (`assets/images/<category>/<category>-news-<month>-<year>.jpg`) - the script
   cannot generate images.
3. Set `draft: false` and commit.

Run logs are written to `scripts/logs/` (git-ignored).

### Monthly schedule

A `launchd` agent runs the script automatically at 09:00 on the 1st of every
month:

- Agent file: `~/Library/LaunchAgents/blog.jamesm.monthly-news.plist`
- Check status: `launchctl list | grep jamesm`
- Disable:  `launchctl unload ~/Library/LaunchAgents/blog.jamesm.monthly-news.plist`
- Re-enable: `launchctl load -w ~/Library/LaunchAgents/blog.jamesm.monthly-news.plist`

The Mac must be powered on for it to run; if it is asleep at 09:00 on the 1st,
the job runs when the Mac next wakes. `launchd` is used instead of `cron`
because it runs inside your login session and can reach the credentials Claude
Code needs.

## validate-tags.py

Fails the build if a post's frontmatter uses a tag that isn't in the
canonical allowlist at `data/tags.yaml`. Run automatically by `deploy.sh`
before `hugo` builds the site; you can also run it standalone:

```bash
python3 scripts/validate-tags.py
```

No dependencies beyond the standard library.

### Adding a new tag

The list exists to stop tags piling up one-off per post (that's how the site
got to 457 distinct tags, a third of them used exactly once). Before adding a
new tag, check whether an existing one in `data/tags.yaml` already covers the
topic - reuse it instead. Add a genuinely new tag only when you expect more
than one post to eventually carry it: use it in the post's frontmatter (as a
singular noun, see the tag-format convention), then add the same string to
`data/tags.yaml` in alphabetical order. The next `deploy.sh` run will fail
until both are done.

## link-audit.py

Reports internal-linking problems that are otherwise invisible - a post
nothing else links to is only reachable via search, a tag page, or deep
pagination. Run automatically by `deploy.sh` after `hugo` builds the site
(it needs the rendered `public/` output, not just the markdown source);
run it standalone any time with:

```bash
hugo && python3 scripts/link-audit.py
```

It checks three things:

1. **Orphan posts** - any post with zero inbound links from another post's
   body or its automatic "More on this topic" block (see
   `layouts/partials/related_content.html`). Tag pages, prev/next nav, and
   the tags footer don't count as real discoverability.
2. **Related Reading section mismatches** - a curated `## Related Reading`
   link whose URL names a section the target post doesn't actually live
   in (left behind when a post moves between sections), or that doesn't
   resolve to any post at all.
3. **Links to drafts** - any published post linking to a post still marked
   `draft: true`. Plain markdown links to a draft aren't caught by Hugo at
   build time; they render as a normal-looking link that 404s once the
   reader clicks it.

Reports only by default (exit 0), so it won't block a deploy - treat it as
the weekly ten-minute chore of skimming the output and fixing what it
finds. Pass `--strict` to exit non-zero on any finding instead, for wiring
into CI once the backlog it finds is clear. No dependencies beyond the
standard library.
