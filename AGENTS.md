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
- Tags in post frontmatter must come from the canonical list in
  `data/tags.yaml` - `python3 scripts/validate-tags.py` checks this and is
  run by `deploy.sh`.
- After adding or editing a post, run `hugo && python3 scripts/link-audit.py`
  to check for orphan posts, broken `## Related Reading` links, and links to
  drafts.
- `deploy.sh` builds with Hugo and rsyncs `public/` straight to the live
  server - it does not go through git, so a post can go live without ever
  being committed. Commit content changes promptly so the repo and the live
  site don't drift apart.
