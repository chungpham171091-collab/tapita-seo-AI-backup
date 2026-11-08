---
name: harry-reference-check
description: "Harry's reference quality assurance workflow for content before publication. Audits every citation, URL, DOI, statistic, and external claim in an…"
---

# Harry Reference Check

This skill audits every external reference in a piece of content before publication. Nine specific failure modes account for almost all reference errors in AI-assisted content. Each requires a different fix.

Run this check before publishing any article, product page, or blog post that contains external citations, statistics, or URLs.

---

## The Nine Failure Modes

### 1. Inherited errors from source material
The original document being rewritten already contained wrong data. AI carries these forward unchecked.
- Wrong issue numbers (e.g. journal vol. 54(3) vs actual 54(5))
- Outdated URLs that now 404
- DOIs that were never verified in the original
- Statistics misattributed to the wrong organization

**Rule:** Treat every reference in a source document as a draft. Verify independently.

### 2. Constructed URLs and DOIs
AI knows URL patterns (e.g. `ncbi.nlm.nih.gov/pmc/articles/PMC[number]`) and constructs plausible-looking links that may not resolve, or may resolve to a different paper.

**Rule:** A DOI or URL is only valid if it was returned verbatim by a web search result, successfully fetched and the content matches the cited claim, or present verbatim in the original source document AND verified via fetch. Never construct a DOI from a pattern. Never build a URL from an ID number without fetching it.

### 3. Attribution scope mismatch
The statistic is real but attributed to an organization that does not measure that thing.
- EEA cited for indoor air pollution (EEA measures ambient/outdoor only)
- NHS cited for global statistics (NHS covers England/UK only)
- A charity cited for government policy data

**Rule:** Before attributing a number to an organization, confirm that organization's scope matches what is being claimed. Read `references/scope-reference.md` for a lookup table.

### 4. Organization name and URL changes
Charities merge, rebrand, or restructure. Old URLs go dead.
- British Lung Foundation → Asthma + Lung UK (2020)
- Public Health England → UKHSA (2021)

**Rule:** For any UK charity, public body, or government department, verify the current name before citing.

### 5. Claim strength drift
The most common and hardest-to-detect failure mode. AI paraphrases study findings using stronger language than the study actually uses.

| Study says | Article must NOT say |
|---|---|
| "association found between X and Y" | "X causes Y" / "X proves Y" |
| "may reduce" / "can help reduce" | "reduces" (as a definitive fact) |
| "22.6-92% reduction range" | "up to 92% reduction" (dropping the lower bound) |
| "in hospital ward conditions" | applying directly to home environments |
| "self-reported sleep quality improved" | "sleep quality improves" |
| "statistically significant association" | "proves" / "demonstrates" |

**Rule:** The article's claim must not be stronger than what the cited study states. When in doubt, add a qualifier ("may", "can", "in study conditions"). Read `references/claim-verification.md` for patterns and fixes.

### 6. Second-order citation
Article A cites Study B for a finding. But Study B's finding was itself cited from Study C. The article is attributing Study C's finding to Study B.

**How it happens:** AI reads a review paper or systematic meta-analysis and attributes the underlying primary studies' findings to the review, or reads an article that summarizes another study and cites the article rather than the original study.

**How to detect:** Fetch Study B. If the specific claim in the article does not appear as Study B's own finding (only as something Study B is citing from elsewhere), the citation is wrong.

**Rule:** Trace every specific data point to its primary source. If Study B says "According to Study C, PM2.5 was reduced by X%", the correct citation is Study C, not Study B.

### 7. Population and context mismatch
A study conducted on a specific population or in a specific setting is applied to a different context without caveat.

Common patterns in health and air quality content:
- Study conducted in hospital → applied to UK homes
- Study on patients with a specific condition → generalized to all adults
- Study conducted in China or US → applied to UK context without noting the difference
- Study using a specific device brand → attributed as general proof for all HEPA purifiers

**Rule:** Every citation must carry the study's population and setting as a caveat when it differs from the context being written about. Read `references/claim-verification.md` for the required caveat language.

### 8. Reference list integrity
The in-text citations and the reference list drift out of sync during editing.
- A reference cited in text has no corresponding entry in the reference list
- A reference in the list is never cited in the text (orphan reference)
- Numbered references appear in the wrong order or with wrong numbers after editing
- The same study appears twice in the reference list under slightly different citation formats

**Rule:** After any edit to either the article body or the reference list, re-verify that every in-text citation has a matching reference entry and every reference entry is cited at least once in the text.

### 9. Temporal drift
Statistics appear current but refer to old data; or recent publications are cited for data that has since been superseded.

- A 2024 paper may report data collected in 2019 or 2022 - cite the data year, not just the publication year
- Organisational statistics (disease prevalence, mortality figures) are updated periodically; verify which year's data the cited figure represents
- "Current" or "recent" language in the article is only valid if the cited figure is from the last 2-3 years

**Rule:** When citing a statistic, confirm both the publication year and the data reference year. Flag any "current" claim backed by data more than three years old.

---

## Audit Workflow

Run these steps in order. Do not skip steps for references that "look fine."

### Step 1 - Extract all references

Pull every external claim from the article into a structured list:

```
| # | Claim in article | Cited source | URL/DOI | Type | Risk |
```

Types: `URL` / `DOI` / `PMC` / `PMID` / `stat-no-url` / `conference` / `preprint`

### Step 2 - Classify each reference by risk

| Risk | Criteria |
|---|---|
| HIGH | DOI present but unverified; URL older than 2 years; UK charity or public body cited; statistic involves indoor vs outdoor or UK vs EU vs global scope; study population differs from article context |
| MEDIUM | URL present but not recently fetched; journal citation without URL; statistic with no year specified |
| LOW | Official `.gov.uk` or `.europa.eu` URL fetched this session; primary source with confirmed DOI |

Verify HIGH first, then MEDIUM. LOW can be spot-checked.

### Step 3 - Verify URLs

For every URL in the article:
1. Fetch the URL
2. Confirm the page resolves (not 404, not redirect to homepage)
3. Confirm the specific claim from the article appears on that page
4. If 404: search for the current correct URL. Only use a URL returned by search or confirmed by fetch.

Special cases: fetch `doi.org/` links, PubMed links, and PMC links - do not assume they resolve.

### Step 4 - Verify DOIs

For every DOI in the article:
1. Search: `[author] [year] [journal] [title keywords] DOI`
2. Accept only if returned by PubMed, CrossRef, or the publisher's own page
3. If unconfirmable, remove the DOI - cite the paper without it
4. Cross-check volume and issue number against what the search returns

Read `references/journal-verification.md` for search strategies and identifier types.

### Step 5 - Verify attribution scope

For each statistic, confirm:
```
□ Does this organization actually publish this type of data?
□ Does the geographic scope match? (UK / EU / global)
□ Does the domain match? (indoor vs outdoor; ambient vs occupational)
□ Does the year in the claim match the actual data year in the publication?
```

Read `references/scope-reference.md` for a lookup table of common organizations.

### Step 6 - Verify organization names

For any UK charity or public body, confirm current name:
1. Search `[name] current status [year]`
2. Update in-text citation and reference entry if name has changed
3. Verify current domain and fetch to confirm it resolves

Known changes: British Lung Foundation → Asthma + Lung UK (`asthmaandlung.org.uk`); Public Health England → UKHSA (`ukhsa.gov.uk`).

### Step 7 - Verify claim strength

For every finding cited from a study, read `references/claim-verification.md` and check:
```
□ Does the article's claim use stronger language than the study uses?
□ Is the study's setting (hospital, lab, home) preserved in the article?
□ Is the study population (asthma patients, coronary disease patients) noted
  when it differs from the article's audience?
□ Are the study's own caveats (self-reported, laboratory conditions,
  small sample) carried into the article?
□ Is this finding from the cited study itself, or from a source the
  study cited? (second-order citation check)
```

### Step 8 - Check reference list integrity

Run through the article and the reference list in parallel:
```
□ Every in-text citation [number] has a matching entry in the reference list
□ Every entry in the reference list is cited at least once in the text
□ No entry appears twice under different numbers
□ Reference numbering is sequential and consistent after any edits
□ No claim in the text is unattributed when it should carry a citation
```

### Step 9 - Check preprint and retraction status

For any academic paper cited:
```
□ Is it published in a peer-reviewed journal? (not bioRxiv / medRxiv / SSRN)
□ If citing a conference presentation, is it labelled as preliminary/unpublished?
□ Search "[author] [title] retracted" to check for retraction notices
```

Conference presentations should be labelled: "Preliminary findings reported at [conference], [year]; peer-reviewed publication pending."

### Step 10 - Check temporal integrity

For every statistic in the article:
```
□ What year does the cited publication say the data is from?
  (A 2024 paper may report 2022 or 2019 data)
□ Is the data year cited in the article, not just the publication year?
□ Does the article use "current" or "latest" language?
  If so, is the data from the last 2-3 years?
□ Is a more recent publication available for this statistic?
```

### Step 11 - Compile audit report

```
## Reference QA Audit Report

Total references audited: [N]
Pass: [N] | Fail: [N] | Warning: [N]

| # | Source | URL | DOI | Scope | Claim | Temporal | Status | Fix |
|---|---|---|---|---|---|---|---|---|
| 1 | UKHSA Cheek 2021 | ✅ | n/a | ✅ | ✅ | ✅ | PASS | - |
| 2 | BLF 2024 | ❌ 404 | n/a | ✅ | ✅ | ✅ | FAIL | New org name + URL |
| 3 | EEA 2024 | ❌ 404 | n/a | ❌ indoor | ✅ | ✅ | FAIL | New URL; remove indoor claim |
| 4 | Kadalayil DOI | ✅ | ⚠️ unverified | ✅ | ⚠️ population | ✅ | WARN | Remove DOI; add caveat |

### Corrected References Section
[Full corrected reference list]

### Notes for editor
[Claims that could not be fully verified; items needing manual checking]
```

---

## Hard Rules (non-negotiable)

1. **Never use a DOI not returned by a trusted bibliographic source.** If unverifiable, cite without DOI.

2. **Never construct a URL from an ID number.** Fetch it before using it.

3. **Never carry a statistic forward without checking its scope.** The org, geography, and domain must all match.

4. **If a URL returns 404, do not guess.** Search for the current URL and fetch to confirm.

5. **If an organization has changed its name, update both the in-text citation and the reference entry.**

6. **Never strengthen a study's claim in paraphrase.** Match or weaken; never amplify.

7. **If a study was conducted in a different setting than the article's context, say so.** A hospital study is not proof for home use without that caveat.

8. **Trace every specific data point to its primary source.** Do not attribute Study C's finding to Study B that cited it.

9. **State the data year, not just the publication year, for time-sensitive statistics.**

---

## Reference Files

Read `references/scope-reference.md` when:
- Article covers health, environment, or regulatory topics
- Statistic involves indoor vs outdoor air, UK vs EU vs global
- Unsure whether an organization covers the claimed domain

Read `references/journal-verification.md` when:
- Journal citations with volume/issue/page numbers are present
- DOIs are present in the article
- Source document is more than 12 months old

Read `references/claim-verification.md` when:
- Article paraphrases findings from academic studies
- Study setting or population differs from article context
- Article uses language like "proves", "shows", "reduces" attributing to a single study
