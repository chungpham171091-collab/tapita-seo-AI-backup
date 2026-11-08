#!/usr/bin/env python3
"""
Pre-delivery QA check for TMF collection pages.

Checks:
  - word count and primary keyword floor (2 per 1,000 words)
  - secondary keyword coverage (each at least once)
  - primary keyword present in Meta Title and Meta Description
  - Meta Title <= 60 chars, Meta Description <= 155 chars
  - banned dashes: em dash, en dash, double hyphen
  - surviving claim-tier markers ([?], [A], [B], [D])
  - every URL in the draft appears in the supplied site URL list
  - phone number in the Meta Description (TMF rule: keep it out)
  - brand token in the Meta Title

Usage:
  python3 qa_check.py draft.md \
      --primary "hose cuffs" \
      --secondary "flash cuffs" "swivel cuff" \
      --meta-title "..." --meta-desc "..." \
      --allowed-urls urls.txt

Meta Title and Meta Description are parsed from the draft's META block if the
flags are omitted.

Exit code 0 = pass, 1 = one or more failures.
"""

import argparse
import re
import sys

BANNED_DASHES = {"\u2014": "em dash", "\u2013": "en dash", "--": "double hyphen"}
MARKER_RE = re.compile(r"\[\?\]|\[A\]|\[B\]|\[D\]")
URL_RE = re.compile(r"https?://[^\s\)\]\>\"']+")
PHONE_RE = re.compile(r"\b1[-\s]?800[-\s]?\d{3}[-\s]?\d{4}\b")

FAILS = []
WARNS = []


def fail(msg):
    FAILS.append(msg)
    print(f"FAIL  {msg}")


def warn(msg):
    WARNS.append(msg)
    print(f"WARN  {msg}")


def ok(msg):
    print(f"ok    {msg}")


def strip_meta_block(text):
    """Return (body_without_meta, meta_title, meta_desc)."""
    title = desc = ""
    m = re.search(r"^\s*#{0,6}\s*\**META\**\s*:?\s*$", text, re.M)
    body = text[: m.start()] if m else text
    tail = text[m.start():] if m else ""
    t = re.search(r"Meta Title:\s*(.+)", tail)
    d = re.search(r"Meta Description:\s*(.+)", tail)
    if t:
        title = t.group(1).strip().strip("*").strip()
    if d:
        desc = d.group(1).strip().strip("*").strip()
    return body, title, desc


def main():
    p = argparse.ArgumentParser()
    p.add_argument("draft")
    p.add_argument("--primary", required=True)
    p.add_argument("--secondary", nargs="*", default=[])
    p.add_argument("--meta-title", default=None)
    p.add_argument("--meta-desc", default=None)
    p.add_argument("--allowed-urls", default=None,
                   help="File containing every URL the client supplied, one per line")
    p.add_argument("--brand-token", default="TMF")
    args = p.parse_args()

    text = open(args.draft, encoding="utf-8").read()
    body, meta_title, meta_desc = strip_meta_block(text)
    meta_title = args.meta_title or meta_title
    meta_desc = args.meta_desc or meta_desc

    low = body.lower()
    words = re.findall(r"\b[\w']+\b", body)
    total = len(words)
    print(f"\n--- TMF collection QA: {args.draft} ---")
    print(f"Body word count: {total}\n")

    # keywords
    primary = args.primary.lower()
    pc = len(re.findall(re.escape(primary), low))
    floor = max(2, round(total / 1000 * 2))
    if pc < floor:
        fail(f'primary keyword "{args.primary}": {pc} occurrences, floor is {floor}')
    else:
        ok(f'primary keyword "{args.primary}": {pc} (floor {floor})')

    for s in args.secondary:
        c = len(re.findall(re.escape(s.lower()), low))
        if c == 0:
            fail(f'secondary keyword "{s}": 0 occurrences, needs at least 1')
        else:
            ok(f'secondary keyword "{s}": {c}')

    # headings + intro
    h2s = re.findall(r"^##\s+(.+)$", body, re.M)
    if not any(primary in h.lower() for h in h2s):
        warn("primary keyword not found in any H2")
    else:
        ok("primary keyword present in an H2")

    if re.search(r"^#\s+\S", body, re.M):
        fail("body contains an H1; the Shopify collection title is the H1")
    else:
        ok("no H1 in body")

    intro = body.strip().split("\n\n")[0].lower()
    if primary not in intro:
        warn("primary keyword not in the opening paragraph")
    else:
        ok("primary keyword in the opening paragraph")

    # dashes
    dash_hit = False
    for ch, name in BANNED_DASHES.items():
        n = text.count(ch)
        if n:
            fail(f"banned {name} found {n} time(s)")
            dash_hit = True
    if not dash_hit:
        ok("no banned dashes")

    # claim markers
    markers = MARKER_RE.findall(text)
    if markers:
        fail(f"claim-tier markers still in draft: {len(markers)} "
             f"({', '.join(sorted(set(markers)))}) - strip before delivery")
    else:
        ok("no claim-tier markers left in draft")

    # meta
    if not meta_title:
        fail("Meta Title missing")
    else:
        n = len(meta_title)
        (ok if n <= 60 else fail)(f"Meta Title {n} chars (max 60)")
        if primary not in meta_title.lower():
            fail("primary keyword missing from Meta Title")
        if args.brand_token.lower() not in meta_title.lower():
            fail(f'brand token "{args.brand_token}" missing from Meta Title')

    if not meta_desc:
        fail("Meta Description missing")
    else:
        n = len(meta_desc)
        (ok if n <= 155 else fail)(f"Meta Description {n} chars (max 155)")
        if primary not in meta_desc.lower():
            fail("primary keyword missing from Meta Description")
        if PHONE_RE.search(meta_desc):
            fail("phone number in Meta Description - spend those characters on "
                 "brand-model or modifier terms instead")

    # urls
    urls = [u.rstrip(".,;") for u in URL_RE.findall(body)]
    seen = {}
    for u in urls:
        seen[u] = seen.get(u, 0) + 1
    dupes = [u for u, c in seen.items() if c > 1]
    if dupes:
        warn(f"{len(dupes)} URL(s) linked more than once: " + ", ".join(dupes[:5]))
    print(f"      {len(urls)} links, {len(seen)} unique")

    if args.allowed_urls:
        allowed = set()
        for line in open(args.allowed_urls, encoding="utf-8"):
            line = line.strip()
            if line:
                allowed.add(line.rstrip("/"))
        unknown = sorted({u for u in seen if u.rstrip("/") not in allowed})
        if unknown:
            fail(f"{len(unknown)} URL(s) not in the supplied site URL list "
                 "(possible invented link):")
            for u in unknown:
                print(f"        - {u}")
        else:
            ok("every link is in the supplied site URL list")
    else:
        warn("no --allowed-urls supplied; invented-link check skipped")

    # blog stub heuristic
    if "/blogs/tmf-clips/" in body or "/blogs/cleaning-videos/" in body:
        warn("draft links a /tmf-clips/ or /cleaning-videos/ post - these are "
             "usually video stubs. Confirm 300+ words of body text "
             "(see references/known-issues.md)")

    # summary
    print()
    if FAILS:
        print(f"RESULT: {len(FAILS)} failure(s), {len(WARNS)} warning(s). "
              "Do not deliver until failures are fixed.")
        return 1
    print(f"RESULT: passed with {len(WARNS)} warning(s). "
          "Automated checks only - Gate 3 still needs the manual checklist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
