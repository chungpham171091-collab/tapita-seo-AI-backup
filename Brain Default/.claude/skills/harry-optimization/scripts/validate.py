#!/usr/bin/env python3
"""
Harry Optimization — deterministic output validator.

Checks the mechanical rules that a language model is unreliable at counting by
eye: keyword word-counts, per-length band counts, meta title/description
character lengths, and main-keyword presence.

USAGE
    python scripts/validate.py <path-to-input.json>
    cat input.json | python scripts/validate.py -

INPUT JSON SCHEMA
    {
      "products": [
        {
          "url": "https://example.com/p/1",        # optional, for labeling
          "target_language": "en",                    # optional, informational
          "word_separated": true,                     # optional, default true.
                                                       #   set false for CJK etc.
          "main_keyword": "Conical Burr Coffee Grinder",
          "keywords": ["Coffee Grinder", "Baratza Grinder", ...],
          "meta_title": "Baratza Encore ESP Conical Burr Coffee Grinder",
          "meta_description": "Baratza Encore ESP is a conical burr ..."
        }
      ]
    }

EXIT CODE
    0  -> no hard errors (warnings may still be printed)
    1  -> at least one hard error (rule violation)
    2  -> bad input / usage error

RULES ENFORCED (hard errors unless noted)
    - every keyword is 2-4 words; 1-word and 5+-word keywords are errors
    - 2-word keywords: 2-3 of them
    - 3-word keywords: 10-15 of them
    - 4-word keywords: 10-15 of them
    - main_keyword must appear in the keywords list (case-insensitive)
    - meta_title length 40-60 characters
    - meta_description length 120-150 characters
    - main_keyword is 3-4 words                              (WARNING)
    - main_keyword appears in meta_title / meta_description   (WARNING)
    - duplicate keywords                                      (WARNING)

For word_separated=false (e.g. Japanese/Chinese), word-count and band checks
are skipped with a warning, since whitespace token counting is not meaningful.
"""

import json
import sys

BAND_RULES = {2: (2, 3), 3: (10, 15), 4: (10, 15)}
TITLE_MIN, TITLE_MAX = 40, 60
DESC_MIN, DESC_MAX = 120, 150


def word_count(phrase):
    return len(phrase.split())


def validate_product(p, idx):
    """Return (errors, warnings) lists of strings for one product."""
    errors, warnings = [], []
    label = p.get("url") or f"product #{idx + 1}"

    keywords = p.get("keywords")
    if not isinstance(keywords, list) or not keywords:
        errors.append(f"[{label}] 'keywords' must be a non-empty list")
        keywords = []

    main_kw = (p.get("main_keyword") or "").strip()
    if not main_kw:
        errors.append(f"[{label}] 'main_keyword' is missing or empty")

    word_separated = p.get("word_separated", True)

    # ---- keyword word-count + band checks -------------------------------
    if word_separated:
        band_counts = {2: 0, 3: 0, 4: 0}
        for kw in keywords:
            kw = str(kw).strip()
            if not kw:
                errors.append(f"[{label}] empty keyword in list")
                continue
            wc = word_count(kw)
            if wc <= 1:
                errors.append(f"[{label}] keyword '{kw}' is 1 word (min 2)")
            elif wc >= 5:
                errors.append(f"[{label}] keyword '{kw}' is {wc} words (5+ not allowed)")
            else:
                band_counts[wc] += 1

        for length, (lo, hi) in BAND_RULES.items():
            n = band_counts[length]
            if n < lo or n > hi:
                errors.append(
                    f"[{label}] {length}-word keywords: {n} found "
                    f"(required {lo}-{hi})"
                )
    else:
        warnings.append(
            f"[{label}] word_separated=false -> word-count and band checks "
            f"skipped (verify 2-3 / 10-15 / 10-15 manually for this language)"
        )

    # ---- main keyword presence + length ---------------------------------
    if main_kw and keywords:
        lowered = [str(k).strip().lower() for k in keywords]
        if main_kw.lower() not in lowered:
            errors.append(
                f"[{label}] main_keyword '{main_kw}' is not present in the keywords list"
            )
    if main_kw and word_separated:
        mwc = word_count(main_kw)
        if mwc < 3 or mwc > 4:
            warnings.append(
                f"[{label}] main_keyword '{main_kw}' is {mwc} words "
                f"(preferably 3-4)"
            )

    # ---- duplicate keywords ---------------------------------------------
    seen, dupes = set(), set()
    for kw in keywords:
        key = str(kw).strip().lower()
        if key in seen:
            dupes.add(key)
        seen.add(key)
    for d in sorted(dupes):
        warnings.append(f"[{label}] duplicate keyword: '{d}'")

    # ---- meta title -----------------------------------------------------
    title = (p.get("meta_title") or "").strip()
    if not title:
        errors.append(f"[{label}] meta_title is missing or empty")
    else:
        n = len(title)
        if n < TITLE_MIN or n > TITLE_MAX:
            errors.append(
                f"[{label}] meta_title is {n} chars (required {TITLE_MIN}-{TITLE_MAX}): \"{title}\""
            )
        if main_kw and main_kw.lower() not in title.lower():
            warnings.append(
                f"[{label}] main_keyword not found verbatim in meta_title"
            )

    # ---- meta description -----------------------------------------------
    desc = (p.get("meta_description") or "").strip()
    if not desc:
        errors.append(f"[{label}] meta_description is missing or empty")
    else:
        n = len(desc)
        if n < DESC_MIN or n > DESC_MAX:
            errors.append(
                f"[{label}] meta_description is {n} chars (required {DESC_MIN}-{DESC_MAX})"
            )
        if main_kw and main_kw.lower() not in desc.lower():
            warnings.append(
                f"[{label}] main_keyword not found verbatim in meta_description"
            )

    return errors, warnings


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2

    src = argv[1]
    try:
        raw = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
        data = json.loads(raw)
    except FileNotFoundError:
        print(f"ERROR: file not found: {src}")
        return 2
    except json.JSONDecodeError as e:
        print(f"ERROR: invalid JSON: {e}")
        return 2

    products = data.get("products") if isinstance(data, dict) else None
    if products is None and isinstance(data, list):
        products = data          # allow a bare list of products
    if not isinstance(products, list) or not products:
        print("ERROR: input must contain a non-empty 'products' list")
        return 2

    all_errors, all_warnings = [], []
    for i, p in enumerate(products):
        e, w = validate_product(p, i)
        all_errors.extend(e)
        all_warnings.extend(w)

    print(f"Validated {len(products)} product(s).\n")

    if all_warnings:
        print(f"⚠️  {len(all_warnings)} warning(s):")
        for w in all_warnings:
            print(f"   - {w}")
        print()

    if all_errors:
        print(f"❌ {len(all_errors)} error(s):")
        for e in all_errors:
            print(f"   - {e}")
        print("\nRESULT: FAIL — fix the errors above and re-validate.")
        return 1

    print("✅ RESULT: PASS — all hard rules satisfied.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
