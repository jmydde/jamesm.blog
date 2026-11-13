# jamesm.blog

This is a real, currently-published Hugo blog. Posts under `content/` cover
genuinely happening events - AI model releases, corporate actions, government
and policy actions, lawsuits, incidents - alongside opinion essays, how-tos,
and personal/hobbyist writing (physics, music production, retro computing,
etc.) that are clearly framed as such in their own text.

## Verify before publishing

The single most important rule for anything under `content/`: **this is not
speculative fiction**, even when a post references a company, product, or
model name you don't recognise. The blog moves faster than any fixed
knowledge cutoff - search first, never assume something is fictional just
because it's unfamiliar.

Before setting `draft: false` on any post that describes a specific
real-world event, quote, statistic, or action attributed to a real,
identifiable company, person, or government body:

1. **Web search to confirm the event actually happened.** Never invent a
   plausible-sounding continuation of a story and publish it as fact.
2. **Never invent quotes.** Every quoted sentence attributed to a real
   person or organisation must come from a source you actually read.
3. **Never invent citation URLs.** Every link in a `## Sources` section
   must be a URL you fetched or found via search - not one constructed to
   look plausible (e.g. guessing a company's blog URL pattern).
4. **If a claim can't be verified, don't publish it as fact.** Leave the
   post as `draft: true`, cut the unverifiable claim, or explicitly frame
   it as your own speculation in the body text.
5. **Vague, unattributed trend claims count too.** "People are saying...",
   "it's going viral because..." need the same scrutiny as a direct quote -
   point to a real, checkable source, or frame it explicitly as your own
   read rather than reported fact.
6. **Check the post's `date` field isn't in the future** relative to now.
   Hugo silently excludes future-dated posts from the build, which can mask
   a publishing mistake instead of surfacing it.

If proper sourcing takes real research, that's fine: draft with
`draft: true`, research it properly, then flip to `false` once every
factual claim traces to something actually verified.

## Other conventions

- No em dashes (`—`) in blog article bodies - use ` - ` instead.
- The title that introduces a YouTube embed must end with that video's upload date in brackets, day then full month then year, for example `### Extended interview: Dario Amodei (13 September 2026)`. Do not invent the date.
- A list of YouTube videos goes most recent first. Keep each video's blurb with that video. Do not reorder a video that illustrates a specific essay section.
- Tags in post frontmatter must come from the canonical list in
  `data/tags.yaml` - `python3 scripts/validate-tags.py` checks this and is
  run by `deploy.sh`.
- After creating a new blog post, always finish by suggesting a ready-to-paste
  X post for it, with hashtags (e.g. `#AI #AISafety`). Keep it under 280
  characters (a link counts as 23), mention the subject's X handle where there
  is one, and use the clean live URL `https://jamesm.blog/<section>/<slug>/`
  with no query string. No em dashes. Don't suggest posting it until the post
  is deployed.
- After adding or editing a post, run `hugo && python3 scripts/link-audit.py`
  to check for orphan posts, broken `## Related Reading` links, and links to
  drafts.
- **Monthly AI roundup.** James wants one "biggest AI news" post at the end of
  every month, at `content/ai/ai-roundup-<month>-<year>.md` titled
  `AI Roundup: <Month> <Year>` (e.g. `ai-roundup-october-2026.md`). **Reminder
  rule:** at the start of any session, if today is the 25th of the month or
  later (or the 1st-3rd, and last month's roundup is missing), check whether
  that month's roundup exists. If not, remind James it is due and offer to
  write it. Follow the verify-before-publishing rules above: research each
  item by web search, prefer primary or major-outlet sources, say where
  sources disagree, attribute company claims, and never include an item you
  could not corroborate. Keep it as `draft: true` until James has reviewed it.
  Link the previous month's roundup in `## Related Reading`. Every roundup
  needs a header image: run `python3 scripts/make-roundup-cover.py <year>
  <month>` (writes `static/assets/images/ai/ai-roundup-<month>-<year>.jpg`
  with the title baked in) and set `cover.image` to it in the frontmatter.
  A roundup's `date` is the last day of its month, but Hugo hides future-dated
  posts, so the current month's roundup keeps today's date while it is being
  updated, and is set to the month's last day when finalised on that day.
  Start the next month's roundup on the 1st.
- News posts on controversial or sensitive topics (scandals, lawsuits, personal
  conduct) state confirmed facts only: no "My take", no personal opinion, and
  no unconfirmed allegations about named people.
- `deploy.sh` builds with Hugo and rsyncs `public/` straight to the live
  server - it does not go through git, so a post can go live without ever
  being committed. Commit content changes promptly so the repo and the live
  site don't drift apart.
