# Journal Citation Verification Guide

Use this file when verifying journal citations, DOIs, and PMIDs in articles. Read alongside the main SKILL.md Step 4 workflow.

---

## Where to Verify Citations (in order of preference)

### 1. PubMed (pubmed.ncbi.nlm.nih.gov)
Best for: biomedical and clinical research
- Search by author + year + title keywords
- Returns: PMID, PMCID (if open access), journal, volume, issue, pages, DOI
- The PMID in the URL (e.g. pubmed.ncbi.nlm.nih.gov/39247934) is confirmed by fetch
- The DOI returned on the PubMed page is confirmed and usable

### 2. CrossRef (search.crossref.org)
Best for: confirming DOIs across all academic publishers
- Search by title or author
- Returns the canonical DOI as registered by the publisher
- Use when PubMed does not index the journal

### 3. Publisher websites directly
Best for: journals not indexed in PubMed (some environmental, engineering journals)
- e.g. Wiley Online Library (onlinelibrary.wiley.com) for CEA, Indoor Air, Allergy
- e.g. ScienceDirect (sciencedirect.com) for Elsevier journals (STE, Environment International)
- The DOI on the publisher's abstract page is confirmed

### 4. Google Scholar
Useful as a last resort but treat with caution - Scholar sometimes shows incorrect metadata. Prefer publisher page or PubMed over Scholar.

---

## How to Search for a Citation

**Search query format:**
```
[First author surname] [year] "[title keywords 3-5 words]" [journal name]
```

**Example:**
```
Kadalayil 2024 "air purifiers rhinitis sleep" Clinical Experimental Allergy
```

**What to check in results:**
1. Author surname matches
2. Year matches
3. Journal name matches
4. Volume and issue number - note what the search returns; compare to what is in the article
5. DOI - copy exactly from the search result or publisher page; do not retype

---

## DOI Rules

| Situation | Action |
|---|---|
| DOI returned by PubMed fetch | ✅ Use as-is |
| DOI returned verbatim in search result snippet | ✅ Use, but fetch to double-check |
| DOI present in source document | ⚠️ Verify independently before using |
| DOI follows a pattern you recognize (e.g. 10.1111/xxx.nnnnn) | ❌ Do not use without verification |
| No DOI found after searching PubMed + CrossRef + publisher | ✅ Cite without DOI; include author, year, journal, vol, issue, page |

**A paper without a verified DOI is still a valid citation.** The citation is: Author(s). (Year). Title. Journal, Volume(Issue), Page(s).

---

## PMC Numbers vs PMIDs vs DOIs

These are three different identifiers and are NOT interchangeable:

| Identifier | Example | What it is | Can construct URL? |
|---|---|---|---|
| PMID | 39247934 | PubMed database record ID | Yes - pubmed.ncbi.nlm.nih.gov/[PMID] is reliable |
| PMCID | PMC9022093 | PubMed Central full-text ID | Caution - ncbi.nlm.nih.gov/pmc/articles/[PMCID]/ usually works but fetch to confirm |
| DOI | 10.1016/j.scitotenv.2020.142585 | Publisher-assigned permanent identifier | Never construct; only use from verified source |

**When the source document gives a PMC number** (e.g. "Topp et al., PMC9022093"):
- This is a valid citation identifier on its own
- The URL ncbi.nlm.nih.gov/pmc/articles/PMC9022093/ is a standard pattern that usually works
- Still recommended to fetch before publishing to confirm the paper matches

---

## Common Citation Errors Caught in QA

| Error type | Example | How to catch |
|---|---|---|
| Wrong issue number | 54(3) when actual is 54(5) | Search the paper; check what issue number search returns |
| Constructed DOI | doi.org/10.1111/cea.14451 not verified | Search PubMed for the paper; DOI not found = remove |
| PMID as DOI | Using PMID in place of DOI field | These are different things; use PubMed to find the actual DOI |
| Author order wrong | "Smith et al." when first author is "Jones" | Fetch PubMed entry to confirm first author |
| Year off by one | Paper published 2023 cited as 2024 | Check PubMed entry for exact publication date |
| Wrong journal name | Similar-sounding journal names confused | Fetch the DOI or PubMed entry |

---

## Pre-Publication Citation Checklist

Before signing off on any reference list:

```
For each citation:
□ Author(s) correct?
□ Year correct?
□ Journal name correct (not a similar-sounding journal)?
□ Volume and issue correct (cross-checked, not assumed)?
□ DOI: returned by PubMed/CrossRef/publisher, not constructed?
□ URL: fetched successfully, content matches the claim?
□ Claim in article matches what the paper actually found?
  (Not a finding from a paper the cited paper itself cited?)
```
