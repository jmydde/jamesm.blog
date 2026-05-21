#!/usr/bin/env bash
#
# generate-monthly-news.sh
# -----------------------------------------------------------------------------
# Generates a "top 5 news stories" blog post for each configured category by
# calling Claude Code in headless mode. Built to run unattended once a month.
#
# Usage:
#   ./scripts/generate-monthly-news.sh                 # all configured categories
#   ./scripts/generate-monthly-news.sh devops ai       # only the named categories
#
# A post is skipped if one already exists for the current month, so the script
# is safe to re-run.
# -----------------------------------------------------------------------------
set -euo pipefail

# Make sure cron/launchd can find claude, node, git, etc.
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

# =============================================================================
# Configuration - edit these
# =============================================================================
REPO_DIR="/Users/jamesmyddelton/Documents/projects/jamesm.blog"

# Categories to generate news posts for. Each must match a content/<name>/ folder.
CATEGORIES=(
  ai
  blockchain
  data-engineering
  data-science
  devops
  music-production
  security
  software-engineering
  space
)

# Save posts as drafts ("true") so you review before publishing, or "false".
DRAFT="true"

# Number of top stories per post.
STORY_COUNT=5

# Claude model: leave empty to use your default, or set e.g. "opus" / "sonnet".
MODEL=""

# Per-category spend cap in USD. Leave empty to disable.
MAX_BUDGET_USD="5"

# =============================================================================
# Derived values - no need to edit below this line
# =============================================================================
CLAUDE_BIN="$(command -v claude || echo "$HOME/.local/bin/claude")"
MONTH_NAME="$(date +%B)"                                    # e.g. May
MONTH_SLUG="$(date +%B | tr '[:upper:]' '[:lower:]')"       # e.g. may
YEAR="$(date +%Y)"                                          # e.g. 2026
TODAY="$(date +%Y-%m-%d)"
SINCE_DATE="$(date -v-1m +%Y-%m-%d 2>/dev/null || date -d '1 month ago' +%Y-%m-%d)"
LOG_DIR="$REPO_DIR/scripts/logs"
RUN_LOG="$LOG_DIR/news-$YEAR-$MONTH_SLUG.log"

# Allow running a subset by passing category names as arguments.
if [ "$#" -gt 0 ]; then
  CATEGORIES=("$@")
fi

mkdir -p "$LOG_DIR"
cd "$REPO_DIR"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$RUN_LOG"; }

if [ ! -x "$CLAUDE_BIN" ]; then
  log "ERROR: claude CLI not found. Install it or fix PATH, then re-run."
  exit 1
fi

log "=== Monthly news generation started: $MONTH_NAME $YEAR ==="
log "Categories: ${CATEGORIES[*]}"

# Headless flags. allowedTools is one comma-separated string so it does not
# swallow the prompt argument that follows it.
CLAUDE_FLAGS=(
  --print
  --permission-mode acceptEdits
  --allowedTools "WebSearch,WebFetch,Read,Write,Edit,Glob,Grep,TodoWrite"
)
[ -n "$MODEL" ] && CLAUDE_FLAGS+=(--model "$MODEL")
[ -n "$MAX_BUDGET_USD" ] && CLAUDE_FLAGS+=(--max-budget-usd "$MAX_BUDGET_USD")

created=0
skipped=0
failed=0
created_files=()

for category in "${CATEGORIES[@]}"; do
  content_dir="content/$category"
  post_path="$content_dir/$category-news-$MONTH_SLUG-$YEAR.md"
  display_name="${category//-/ }"

  if [ ! -d "$content_dir" ]; then
    log "SKIP  $category - no $content_dir folder"
    skipped=$((skipped + 1))
    continue
  fi

  if [ -f "$post_path" ]; then
    log "SKIP  $category - post already exists ($post_path)"
    skipped=$((skipped + 1))
    continue
  fi

  log "GEN   $category - researching and writing $post_path"

  prompt="Today is $TODAY. Research the top $STORY_COUNT news stories in \"$display_name\" from roughly the last month (between $SINCE_DATE and $TODAY) and write ONE blog post about them for this Hugo blog.

Requirements:
- Use the WebSearch and WebFetch tools to find real, current, specific stories. Never invent stories or facts.
- Verify EVERY external link actually loads (HTTP 200 - no 404 or 403) with WebFetch before including it. Drop any link that fails verification.
- Follow the conventions in CLAUDE.md and the project auto-memory exactly. In particular:
  - YAML frontmatter with: title, date (ISO 8601 with timezone, e.g. ${TODAY}T09:00:00+01:00), draft: $DRAFT, tags (singular form, e.g. 'ai' not 'ai-tools'), description, and a cover block.
  - The cover block must be: cover:\n      image: /assets/images/$category/$category-news-$MONTH_SLUG-$YEAR.jpg\n      alt: <short alt text>
  - Use space-dash-space ( - ) instead of em dashes.
  - All wording must be original and copyright-free. Never use a full personal name as author - use 'James M' if a name is needed.
  - Include links to authoritative sources and organisations.
- Structure: open with a short TL;DR, cover the $STORY_COUNT stories with brief honest analysis, and end with a '## Related Reading' section linking 3-5 existing posts found in the $content_dir folder (use their real file slugs).
- If you cannot find $STORY_COUNT solid stories, write the post with what you genuinely found and say so.
- Save the finished post to exactly this path: $post_path
- Do not modify any other files and do not run git commands."

  if "$CLAUDE_BIN" "${CLAUDE_FLAGS[@]}" "$prompt" >>"$RUN_LOG" 2>&1; then
    if [ -f "$post_path" ]; then
      log "OK    $category - created $post_path"
      created=$((created + 1))
      created_files+=("$post_path")
    else
      log "FAIL  $category - Claude finished but $post_path was not created"
      failed=$((failed + 1))
    fi
  else
    log "FAIL  $category - claude exited non-zero (see log above)"
    failed=$((failed + 1))
  fi
done

log "=== Done: $created created, $skipped skipped, $failed failed ==="
if [ "$created" -gt 0 ]; then
  log "New posts to review:"
  for f in "${created_files[@]}"; do
    log "  - $f"
  done
  log "Next: review each draft, add the cover image referenced in its frontmatter, then set draft: false to publish."
fi
log "Full log: $RUN_LOG"

exit 0
