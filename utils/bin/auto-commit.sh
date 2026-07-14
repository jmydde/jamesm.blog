#!/usr/bin/env bash
# Stage all changes, generate a Conventional Commits message from the diff
# via the claude CLI, show it for approval, then commit and push.
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

git add -A

if git diff --staged --quiet; then
    echo "No changes to commit."
    exit 0
fi

DIFF="$(git diff --staged)"

PROMPT="Write a git commit message for the diff below.

Follow Conventional Commits:
- Format: <type>(<optional scope>): <subject>
- type is one of: feat, fix, refactor, perf, docs, test, build, ci, chore
- subject: imperative mood, <=50 chars, no trailing period
- blank line, then a body wrapped at 72 chars explaining the motivation
  and contrast with previous behavior (omit the body for trivial changes)
- do not invent a reason that isn't evident from the diff

Output ONLY the raw commit message text. No code fences, no preamble,
no explanation.

Diff:
$DIFF"

MESSAGE="$(claude -p "$PROMPT")"

echo "----- Proposed commit message -----"
echo "$MESSAGE"
echo "------------------------------------"

read -r -p "Commit with this message? [y/N] " CONFIRM
if [[ "$CONFIRM" =~ ^[Yy]$ ]]; then
    git commit -m "$MESSAGE"
    echo "Committed."
    git push
    echo "Pushed."
else
    echo "Aborted. Changes remain staged."
fi
