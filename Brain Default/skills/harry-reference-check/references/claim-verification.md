# Claim Verification Guide

Use this file during Step 7 of the audit workflow. It covers how to detect and fix claim strength drift, second-order citations, population mismatches, and missing caveats.

---

## 1. Claim Strength Drift

### Signal words that indicate over-strengthening

When you see these words in the article attributing to a single study, verify the study uses equivalent language:

| Article uses | What the study likely says | Correct replacement |
|---|---|---|
| "proves" | "found an association" / "suggests" | "found" / "was associated with" |
| "shows" (definitive) | "indicates" / "suggests" | "indicates" / "found" |
| "reduces" (as fact) | "was associated with a reduction in" | "was associated with a reduction in" |
| "eliminates" | "reduced concentrations of" | "reduced concentrations of" |
| "is effective against" | "reduced measured levels of" | "reduced measured levels of" |
| "helps with [condition]" | "improved quality-of-life scores in participants with [condition]" | describe the actual measured outcome |
| "up to X%" | "X% range from Y to X" | state both ends of the range |
| "significantly" | check whether the paper uses "statistically significant" | if not stated, remove "significantly" |

### Statistical precision: ranges must be preserved

A study reporting a range must be quoted as a range, not just its upper bound.

**Wrong:** "reduced PM2.5 by up to 92%"
**Correct:** "reduced PM2.5 by 22.6-92% compared to controls (range reflects differences in room size, purifier specification and usage)"

The lower bound matters. Readers and regulators read "up to X%" as a typical result; the actual range tells a different story.

### How to check claim strength

1. Locate the specific sentence in the study (fetch the page, search for the number or key term)
2. Copy the study's exact language
3. Compare to what the article says
4. If the article is stronger, revise to match or soften the study's own language

---

## 2. Second-Order Citation

### How to identify it

Fetch the cited paper. Search the full text for the specific claim in the article. If you find it only in the form:

> "Smith et al. (2019) found that..."
> "As reported by Jones (2021)..."
> "According to previous research (Williams, 2020)..."

...then the cited paper is quoting another study for that finding. The article is citing the wrong paper.

### How to fix it

Option A: Cite the primary source (preferred)
- Identify the paper being cited within the fetched paper
- Verify that primary source exists and contains the claim
- Replace the citation in the article with the primary source

Option B: Cite the review/synthesis with correct framing
- If the primary source cannot be verified, attribute the claim to the review paper but state that it is reporting earlier research
- Example: "A 2024 systematic review (Shih et al.) summarising earlier randomised studies found..."

Option C: Remove the claim
- If neither the review nor the primary source can be verified, remove the claim

---

## 3. Population and Context Mismatch

### Required caveats by study type

When a study is cited in an article about a different context, the caveat is mandatory, not optional.

| Study type | Required caveat in article |
|---|---|
| Hospital / clinical setting | "conducted in a hospital ward, not a domestic setting; results in the home will differ" |
| Specific device brand | "used [Brand X] units, not Coway; results may differ by device" |
| Specific disease population | "in a group of participants with [condition]; outcomes may differ for other individuals" |
| Non-UK geography | "conducted in [country]; conditions in UK homes may differ" |
| Laboratory / chamber conditions | "laboratory conditions; performance at home varies with room size, ventilation and use" |
| Small sample / pilot | "preliminary study; [N] participants" |
| Self-reported outcomes | "outcomes were self-reported scores, not physiological measurements" |

### The Coway-specific caveat set

For any independent study cited in Coway content, check whether the article includes:
1. Device brand used (if not Coway): "This study used [Brand] units, not Coway equipment"
2. Setting: "conducted in [setting], not a domestic environment"
3. Population: "in participants with [condition]" when the study population is specific
4. Disclaimer: "This is independent research; Coway does not attribute these outcomes to its products"

All four apply to clinical studies. At minimum, items 1 and 4 must always appear.

---

## 4. Missing Caveats from Source

### Caveats that AI commonly strips when paraphrasing

Before finalizing any study citation, check whether the study itself includes these qualifications and whether the article preserves them:

**Laboratory and test conditions:**
> "under laboratory conditions" / "in a controlled chamber" / "at a specific fan speed"
→ Must appear when citing performance figures. Example: "99.999% of particles (KCL lab test, SPS-KACA 002-132:2022, laboratory conditions; performance at home varies with room size, ventilation and use)"

**Preliminary/conference status:**
> Findings reported at a conference rather than a peer-reviewed journal
→ Must be labelled: "Preliminary findings reported at [conference], [year]; full peer-reviewed results were in preparation at the time of reporting"

**Study limitations stated by the authors:**
> Small sample size, short duration, single-centre, self-reported outcomes
→ Include at least the most material limitation

**Range vs point estimate:**
> A finding with a range (22-92%) cannot become a single number

**Causal language:**
> A randomised trial showing association cannot be reported as proof of causation

---

## 5. Claim-Source Tracing Template

Use this for each study citation to confirm the claim is traceable:

```
Study cited: [Author, year]
Claim in article: "[exact text from article]"
Location in study: [page/section where this appears]
Study's exact language: "[exact text from study]"

Claim strength check:
□ Article language is equivalent or weaker than study language
□ No precision lost in range/statistic

Population check:
□ Study population matches article context, OR
□ Appropriate caveat added

Setting check:
□ Study setting matches article context, OR
□ Appropriate caveat added

Second-order check:
□ This finding originates in this study (not cited from another study within it)

Caveats preserved:
□ Test conditions noted
□ Publication status noted if preliminary
□ Disclaimer present if study does not use Coway equipment
```

---

## 6. Quick Reference: Claim Accuracy Red Flags

If you see any of these in the article, stop and verify before passing:

- "proves" or "demonstrates" attributed to a single study
- A single percentage with no range when the study reports a range
- "in UK homes" or "for home use" cited from a hospital or chamber study
- "reduces [condition]" when the study measured particle counts, not health outcomes
- A claim from a systematic review where the review itself cited another study
- "current" data attributed to a publication more than 3 years old
- Any finding attributed to a Coway-branded study that does not exist
- A study cited without noting it used a competitor's device
