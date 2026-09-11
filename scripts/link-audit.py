#!/usr/bin/env python3
"""Report posts with no inbound internal links, and Related Reading links
that point at a section the target post doesn't actually live in.

Run this after `hugo` has built `public/` (see deploy.sh) - it needs the
rendered HTML to see the final link graph, including the automatic "More
on this topic" block (layouts/partials/related_content.html), which is
computed by Hugo at build time and isn't present in the markdown source.

"Inbound internal link" here means a link inside another post's rendered
`.post-content` (the hand-written body, including the curated
`## Related Reading` list) or the automatic related-content block that
follows it. Footer chrome - the tags list, prev/next nav, share buttons -
doesn't count: a post reachable only via chronological prev/next or a tag
page is exactly the invisible-orphan problem this report exists to catch.

The second check reads the markdown source directly: for every post's own
`## Related Reading` section, it resolves each linked slug against the
real content tree and flags links whose URL names a section other than
the one the target post is actually filed under (stale links left behind
when a post moves sections) or that don't resolve to any post at all.

The third check scans every published post's full body (not just Related
Reading) for a link to a post still marked `draft: true` - those render
as a normal-looking href but 404 once clicked, since drafts aren't in the
published output (see EDITORIAL.md's "never link to draft posts" rule).

Deliberately has no dependencies beyond the standard library, so it runs
with the system python3 and never needs its own install step.

Usage:
    hugo && python3 scripts/link-audit.py [--strict]

Reports only by default (exit 0). Pass --strict to exit non-zero when
there are any orphans or Related Reading problems, for wiring into CI
alongside validate-tags.py.
"""
import glob
import os
import re
import sys

REPO_ROOT = __file__.rsplit("/scripts/", 1)[0] if "/scripts/" in __file__ else "."

CONFIG_YAML = f"{REPO_ROOT}/config.yaml"
CONTENT_GLOB = f"{REPO_ROOT}/content/**/*.md"
PUBLIC_DIR = f"{REPO_ROOT}/public"

DRAFT_RE = re.compile(r"^draft:\s*true\s*$", re.MULTILINE)
SLUG_RE = re.compile(r'^slug:\s*[\'"]?([^\'"\n]+?)[\'"]?\s*$', re.MULTILINE)
RELATED_READING_RE = re.compile(
    r"^##\s*Related Reading\s*$(.*?)(?=^##\s|\Z)", re.MULTILINE | re.DOTALL
)
MD_LINK_TARGET_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
REF_SHORTCODE_RE = re.compile(r'\{\{<\s*(?:ref|relref)\s+"([^"]+)"')
HREF_RE = re.compile(r'href="([^"]+)"')


def load_main_sections(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^\s*mainSections:\s*\n((?:^\s*-\s*.+\n)+)", text, re.MULTILINE)
    if not m:
        sys.exit("Could not find params.mainSections in config.yaml")
    return [line.strip().lstrip("-").strip() for line in m.group(1).splitlines()]


def load_posts(main_sections):
    """Return (posts, drafts), each {(section, slug_path): source .md path},
    for every post filed directly under a main section (slug_path may
    itself contain "/" for posts nested in a subdirectory, e.g.
    blockchain/bitcoin).

    Honours a `slug:` frontmatter override - it replaces just the leaf
    filename in the URL, same as Hugo, so a post filed as
    databricks-innovations-2026.md with `slug: "modern-..."` is correctly
    keyed by its real published URL, not its filename."""
    posts, drafts = {}, {}
    prefix_len = len(REPO_ROOT.rstrip("/")) + 1
    for path in sorted(glob.glob(CONTENT_GLOB, recursive=True)):
        rel = path[prefix_len:]
        parts = rel.split("/")
        if len(parts) < 3 or parts[0] != "content":
            continue
        section = parts[1]
        if section not in main_sections:
            continue
        if parts[-1] == "_index.md":
            continue
        slug_parts = "/".join(parts[2:])[: -len(".md")].split("/")
        text = open(path, encoding="utf-8").read()
        fm_end = text.find("\n---", 3)
        frontmatter = text[: fm_end + 4] if text.startswith("---") and fm_end != -1 else ""
        slug_override = SLUG_RE.search(frontmatter)
        if slug_override:
            slug_parts[-1] = slug_override.group(1)
        key = (section, "/".join(slug_parts))
        if DRAFT_RE.search(frontmatter):
            drafts[key] = path
        else:
            posts[key] = path
    return posts, drafts


def resolve_internal_link(href, main_sections):
    """Normalise a raw href/markdown-link target to a (section, slug_path)
    tuple, or None if it isn't a link to one of our own content pages."""
    if href.startswith("https://jamesm.blog"):
        href = href[len("https://jamesm.blog"):]
    elif "://" in href or href.startswith("mailto:"):
        return None
    if not href.startswith("/"):
        return None
    href = href.split("#", 1)[0].split("?", 1)[0]
    path = href.strip("/")
    if not path:
        return None
    parts = path.split("/")
    section = parts[0]
    if section not in main_sections or len(parts) < 2:
        return None
    return section, "/".join(parts[1:])


def find_related_reading_problems(posts, main_sections):
    slug_to_sections = {}
    for section, slug_path in posts:
        slug_to_sections.setdefault(slug_path, set()).add(section)

    mismatches, broken = [], []
    for (section, slug_path), path in posts.items():
        text = open(path, encoding="utf-8").read()
        m = RELATED_READING_RE.search(text)
        if not m:
            continue
        for raw_target in MD_LINK_TARGET_RE.findall(m.group(1)):
            resolved = resolve_internal_link(raw_target, main_sections)
            if resolved is None:
                continue
            link_section, link_slug = resolved
            actual_sections = slug_to_sections.get(link_slug)
            if not actual_sections:
                broken.append(f"{path}: Related Reading links to /{link_section}/{link_slug}/, which doesn't match any post")
            elif link_section not in actual_sections:
                actual = ", ".join(sorted(f"/{s}/{link_slug}/" for s in actual_sections))
                mismatches.append(f"{path}: Related Reading links to /{link_section}/{link_slug}/ but that post is filed at {actual}")
    return mismatches, broken


def find_draft_links(posts, drafts, main_sections):
    """Flag any published post that links to a draft post anywhere in its
    body. Plain markdown links to a draft aren't caught by Hugo at build
    time - they render as a live-looking href that 404s once the reader
    clicks it, since draft pages aren't in the published output."""
    problems = []
    for (section, slug_path), path in posts.items():
        text = open(path, encoding="utf-8").read()
        fm_end = text.find("\n---", 3)
        body = text[fm_end + 4:] if text.startswith("---") and fm_end != -1 else text
        targets = MD_LINK_TARGET_RE.findall(body) + REF_SHORTCODE_RE.findall(body)
        for raw_target in targets:
            resolved = resolve_internal_link(raw_target, main_sections)
            if resolved and resolved in drafts:
                link_section, link_slug = resolved
                problems.append(f"{path}: links to draft post /{link_section}/{link_slug}/ ({drafts[resolved]}) - drafts aren't published and this link 404s")
    return problems


def load_inbound_links(posts, main_sections):
    inbound = {key: set() for key in posts}
    missing_html = []
    for (section, slug_path) in posts:
        html_path = f"{PUBLIC_DIR}/{section}/{slug_path}/index.html"
        try:
            html = open(html_path, encoding="utf-8").read()
        except FileNotFoundError:
            missing_html.append(html_path)
            continue
        start = html.find('<div class="post-content')
        end = html.find('<footer class="post-footer">')
        if start == -1 or end == -1:
            continue
        body = html[start:end]
        for href in HREF_RE.findall(body):
            resolved = resolve_internal_link(href, main_sections)
            if resolved is None or resolved == (section, slug_path):
                continue
            if resolved in inbound:
                inbound[resolved].add((section, slug_path))
    return inbound, missing_html


def main():
    strict = "--strict" in sys.argv

    if not os.path.isdir(PUBLIC_DIR):
        sys.exit(f"{PUBLIC_DIR} not found - run `hugo` first (this report reads the built site).")

    main_sections = load_main_sections(CONFIG_YAML)
    posts, drafts = load_posts(main_sections)

    mismatches, broken = find_related_reading_problems(posts, main_sections)
    draft_links = find_draft_links(posts, drafts, main_sections)
    inbound, missing_html = load_inbound_links(posts, main_sections)
    orphans = sorted(key for key, sources in inbound.items() if not sources)

    problems = bool(orphans or mismatches or broken or draft_links)

    print(f"Link audit: {len(posts)} posts across {len(main_sections)} sections.\n")

    if missing_html:
        print(f"{len(missing_html)} post(s) had no built HTML (build may be stale):")
        for p in missing_html:
            print(f"  - {p}")
        print()

    if orphans:
        by_section = {}
        for section, slug_path in orphans:
            by_section.setdefault(section, []).append(slug_path)
        breakdown = ", ".join(f"{len(v)} in {k}" for k, v in sorted(by_section.items(), key=lambda kv: -len(kv[1])))
        print(f"{len(orphans)} of {len(posts)} posts have zero inbound internal links ({breakdown}):")
        for section, slug_path in orphans:
            print(f"  - /{section}/{slug_path}/  ({posts[(section, slug_path)]})")
        print()
    else:
        print("No orphan posts: every post has at least one inbound internal link.\n")

    if mismatches:
        print(f"{len(mismatches)} Related Reading link(s) point at the wrong section:")
        for m in mismatches:
            print(f"  - {m}")
        print()

    if broken:
        print(f"{len(broken)} Related Reading link(s) don't resolve to any post:")
        for b in broken:
            print(f"  - {b}")
        print()

    if not (mismatches or broken):
        print("Related Reading links all resolve to the right section.\n")

    if draft_links:
        print(f"{len(draft_links)} link(s) to draft posts (these 404 once published):")
        for d in draft_links:
            print(f"  - {d}")
        print()
    else:
        print("No published post links to a draft.")

    if strict and problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
