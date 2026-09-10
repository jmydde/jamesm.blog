#!/usr/bin/env python3
"""Fail the build if any post uses a tag outside the canonical list.

Reads the allowlist from data/tags.yaml and every `tags:` field under
content/**/*.md (skipping section index pages and other untagged utility
pages), and reports any tag not on the list plus any post with no tags at
all. Exits non-zero on a violation so it can gate a build (see deploy.sh).

Deliberately has no dependencies beyond the standard library, so it runs
with the system python3 and never needs its own install step.
"""
import glob
import re
import sys

REPO_ROOT = __file__.rsplit("/scripts/", 1)[0] if "/scripts/" in __file__ else "."

TAGS_YAML = f"{REPO_ROOT}/data/tags.yaml"
CONTENT_GLOB = f"{REPO_ROOT}/content/**/*.md"

# Pages that intentionally carry no tags (section indexes, utility pages).
UNTAGGED_OK = re.compile(r"(^|/)_index\.md$|(^|/)(search|archives)\.md$")

INLINE_RE = re.compile(r"^tags:\s*\[(.*)\]\s*$", re.MULTILINE)
MULTI_RE = re.compile(r"^tags:\s*$\n((?:^\s*-\s*.+$\n?)+)", re.MULTILINE)
MULTI_ITEM_RE = re.compile(r"^\s*-\s*(.+?)\s*$", re.MULTILINE)


def strip_quotes(tok):
    tok = tok.strip()
    if len(tok) >= 2 and tok[0] == tok[-1] and tok[0] in ("'", '"'):
        return tok[1:-1]
    return tok


def load_canonical(path):
    tags = set()
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^\s*-\s*(.+?)\s*$", line)
        if m:
            tags.add(strip_quotes(m.group(1)))
    return tags


def extract_tags(frontmatter):
    m = INLINE_RE.search(frontmatter)
    if m:
        return [strip_quotes(t) for t in m.group(1).split(",") if t.strip()]
    m = MULTI_RE.search(frontmatter)
    if m:
        return [strip_quotes(t) for t in MULTI_ITEM_RE.findall(m.group(1))]
    return None


def main():
    canonical = load_canonical(TAGS_YAML)
    problems = []

    for path in sorted(glob.glob(CONTENT_GLOB, recursive=True)):
        text = open(path, encoding="utf-8").read()
        fm_end = text.find("\n---", 3)
        if not text.startswith("---") or fm_end == -1:
            continue
        frontmatter = text[: fm_end + 4]

        tags = extract_tags(frontmatter)
        if tags is None:
            if not UNTAGGED_OK.search(path):
                problems.append(f"{path}: no `tags:` field")
            continue

        unknown = [t for t in tags if t not in canonical]
        if unknown:
            problems.append(f"{path}: tag(s) not in data/tags.yaml: {unknown}")
        if not tags:
            problems.append(f"{path}: `tags:` field is empty")

    if problems:
        print("Tag validation failed:\n", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        print(
            f"\n{len(problems)} problem(s). To add a new tag deliberately, "
            "add it to data/tags.yaml. To fix a typo or one-off tag, reuse "
            "an existing canonical tag instead.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Tag validation passed: all tags in {len(canonical)}-tag canonical list.")


if __name__ == "__main__":
    main()
