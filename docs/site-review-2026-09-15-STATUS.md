# Site review — status

**Full write-up:** https://claude.ai/artifact/9tU2XY6bW82WjcTSZ497GS
**Source file (same content, kept in sync):** [site-review-2026-09-15.html](site-review-2026-09-15.html)

Neither file is built into the site — `docs/` isn't a Hugo content or static
mount, so this never ships to production.

## Where things stand

- **38 findings** total, from a full audit of the live site, a clean local
  build, and the repo.
- **10 fixed** so far — all 9 that were rated Critical, plus the alias-redirect
  bug that started this (originally its own fix, done first).
- **28 open** — none critical. Breakdown by section is in the artifact
  itself (each finding is tagged Fixed / Critical / High / Medium / Low).
- **Committed, merged, and deployed.** [PR #4](https://github.com/jmydde/jamesm.blog/pull/4)
  merged to `main` on 15 Sep 2026, then `./deploy.sh` was run - live on
  jamesm.blog. Spot-checked after deploy: alias redirects gone, favicons
  and 404 page serving, pagination and search index sizes match the build,
  the reassigned cover image and the gaming related-content fix both
  confirmed on the live site.

## What was fixed

1. `/blog/`, `/posts/`, `/articles/`, `/showcase/`, `/docs/` no longer
   redirect to `/space/` (12 section `_index.md` files)
2. Pagination config (`config.yaml`) - was silently ignored, now 15/page
3. `gaming` added to `mainSections` (`config.yaml`)
4. 4 missing favicon files generated (`static/`)
5. Custom 404 page wired up (`static/.htaccess`)
6. Homepage/site-wide cover images resized and recompressed in place
   (`static/assets/images/` - 46 MB → 24 MB)
7. Search index trimmed (`layouts/_default/index.json` - new override)
8. Nav "Topics" dropdown built (`layouts/partials/header.html` - new
   override, plus `config.yaml` menu weights)
9. About page added (`content/about.md`), linked from nav
10. 17 cover images that had another post's title rendered into them -
    47 posts reassigned to safe generic covers

Full detail, evidence, and verification notes for each are in the artifact.

## To resume in a new session

1. Open the artifact link above (or ask Claude to read it) to see current
   fixed/open status - the 9 critical findings are done and live; 28
   lower-severity ones remain, none critical.
2. `git log` / `git status` to confirm nothing's changed since (the fixes
   landed via PR #4, already deployed as of this note).
3. Tell Claude what to do next - e.g. "fix the next highest-priority open
   finding," or point it at a specific section of the artifact.
