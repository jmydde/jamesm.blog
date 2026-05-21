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
