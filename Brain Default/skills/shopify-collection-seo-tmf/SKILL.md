---
name: shopify-collection-seo-tmf
description: "End-to-end SEO content workflow for TruckMountForums (shop.truckmountforums.com) Shopify collection pages, with a mandatory fact-verification protocol built in. Use this skill whenever the user asks to write, rewrite, optimise, audit or strategise content for a TMF collection / category page - including keyword research, SERP analysis, outline creation, meta generation, product and sub-collection linking, related-blog selection, and full collection description writing. Triggers on any shop.truckmountforums.com URL, any /collections/ URL for TMF, mentions of 'TMF collection page', 'truckmount collection content', or when the user pastes a TMF keyword paired with a collection URL. Also use it when the user asks to fact-check or fix existing TMF collection copy. Always prefer this skill over generic blog writing or the generic collection SEO skill when the store is TMF."
---

# TMF Shopify Collection Page SEO Skill

End-to-end workflow for writing SEO content for shop.truckmountforums.com collection pages.

This skill exists because a 2026 audit of ten TMF collection pages found that only ~67% of verifiable claims survived scrutiny. 36 claims were false or contradicted TMF's own listings; 40 more were unsupported. Link integrity was perfect and review data was near-perfect. Every failure shared one cause: **the writer worked from product titles and category knowledge instead of opening the product pages.**

So this skill is the generic collection workflow plus three hard gates that make that failure impossible. The gates are not optional and they are not style advice. A page that has not passed Gate 3 is not delivered.

**Read `references/verification.md` before Step 3 of any job.** It holds the Product Fact Sheet spec, the banned patterns, and the pre-delivery checklist.

---

## Rule 0 - the source-of-truth hierarchy

Every factual sentence must trace to one of these:

| Tier | Source | Use for |
|---|---|---|
| A | The live TMF product listing (description, title, variants, price, stock, Okendo reviews) | Product mechanism, format, category, application, size, specs, price, availability, ratings |
| B | Manufacturer or authorised distributor | Equipment specs the TMF listing omits: RPM, HP, PSI rating, head width, weight, runtime |
| C | TMF's own pages: About Us, Contact, Military, Loyalty, Financing | Every business claim |
| D | Mainstream trade practice, stated as category guidance | pH behaviour, fibre science, method theory - never attached to a named product |

**If a claim has no tier, it does not get written.** Not softened, not hedged. Removed, and logged in the delivery summary so TMF can decide whether to publish the missing data on the listing.

Tier D claims are welcome, but they stay general. "Counteractants bond with amines and mercaptans" is Tier D and fine. "Rob's Reefer Rid targets terpene and resin compounds" is a Tier A claim with no Tier A source, and it is exactly the error the audit flagged.

---

## How the deliverable is shaped

- **One continuous, clean, copy-ready article.** The user pastes it straight into the Shopify collection description. No "Block 1 / Block 2" dividers, no "H2:" label prefixes. Plain markdown headings.
- **No H1 in the body.** The Shopify theme renders the collection title as H1. Open with the intro paragraph. Do check that the collection title contains the primary keyword and flag it if not.
- **Links live inline** as natural markdown links. The consolidated link list goes in the chat task summary, not the article.
- **Fixed bottom order:** ... Why Buy at TMF Store -> FAQ -> `Related Blogs` -> `META` footer.

At delivery there are three things: the clean article, the task summary in chat, and the completed Gate 3 checklist.

---

## Workflow Overview

```
Step 1: Collect inputs (URL + keyword + internal link list + product URLs + blog URLs)
Step 2: SERP research (web_search - REQUIRED)
GATE 1  Collection Reality Check + Product Fact Sheet + Blog Whitelist + Brand Facts
Step 3: Fetch collection + pick links + related blogs
Step 4: Strategy report + outline + Framework Feasibility Check -> WAIT for approval
GATE 2  Claim tiering + banned patterns while writing
Step 5: Write the article
Step 6: Keyword / dash / meta check (scripts/qa_check.py)
GATE 3  Pre-delivery checklist - blocks delivery
Step 7: Deliver
```

---

## Step 1: Collect Required Inputs

Confirm all of these before doing anything. If any are missing, STOP and ask.

- **Collection URL** (live, e.g. `https://shop.truckmountforums.com/collections/hose-cuffs`)
- **Primary keyword** (one phrase)
- **Secondary keywords / variants** (optional but recommended)
- **Internal link list** (full site URL list: sub-collections, sibling collections, product URLs, blog URLs)
- **Blog URL list** (if not already inside the internal link list)
- **Top sellers / featured products** (optional; otherwise fetched in Step 3)

Brand is always TMF Store. Do not ask for it.

Ask in one message:

> Mình cần các thông tin sau trước khi bắt đầu:
> 1. URL collection page (live URL)
> 2. Từ khoá chính + từ khoá phụ / variants (nếu có)
> 3. Danh sách URL toàn site để chọn internal link (sub-collection + product URL + blog URLs)
> 4. Danh sách URL blog/bài viết (để chọn 3-5 bài cho mục Related Blogs)
>
> Optional: nếu đã có list top sellers / featured products (kèm product URL) thì gửi luôn.

---

## Step 2: SERP Research (web_search REQUIRED)

**Hard rule:** pull the top 10 Google results for the US market. Do not infer from training data.

If `web_search` fails, STOP and offer two options, then wait:

```
web_search không khả dụng / fail. Chọn 1 trong 2 hướng:

Option 1 - Cung cấp data thủ công:
Paste top 10 kết quả Google.com cho từ khoá "[KEYWORD]"
(URL + page title; bonus nếu có headings hoặc word count)

Option 2 - Tự chạy tiếp không có SERP:
Skip phần SERP insight, làm strategy report dựa trên intent +
persona + best practice. Sẽ flag rõ trong report.
```

Never fabricate SERP data. For each result record: URL, page type, H1/title, heading structure (`web_fetch` the top 3-5), approximate word count, trust signals.

---

## GATE 1 - before a single word is written

### 1a. Collection Reality Check

Two of the ten audited pages were written for the same collection; a third described a collection that returns 404.

- [ ] Target collection URL returns 200 and the handle is exactly right. **Watch the one-letter traps** listed in `references/known-issues.md`, especially `/collections/wood-floor-cleaning` (6 machines) vs `/collections/wood-floors-cleaning` (3 chemicals).
- [ ] Record the live collection title, product count, and full product list.
- [ ] Check the keyword map in `references/known-issues.md`: is another collection or another page in this batch already targeting this term? If yes, stop and get a URL-ownership decision from TMF before writing.
- [ ] Confirm the collection contains what the target keyword promises. A keyword promising a dual-surface product over a fabric-only collection is a bounce problem no copy can fix.
- [ ] Open every collection you plan to link out to and count its products. Three links in the last batch described a "full range" holding one product; one pointed at an empty collection.

### 1b. Product Fact Sheet - the core control

Build this table **before the outline**, one row per product you intend to name, populated only from Tier A and Tier B. Leave cells blank rather than guessing.

Full field spec and worked example: `references/verification.md`. Minimum fields:

exact live title | price + variants | **availability per variant** | rating + review count | **one-word category** | **mechanism, quoted from the listing** | stated surfaces/fibres | hard specs (RPM, HP, PSI, width, weight, runtime, pH, unit size, dilution) | pressure *requirement* vs pressure *rating* | anything on the listing that contradicts the page's thesis

**Blank-cell rule:** blank mechanism cell means the page may not describe that product's chemistry. Blank spec cell means the page may not build a buying framework on that spec.

Check `references/product-corrections.md` first. It holds the verified truth for every product the audit caught being misdescribed, so those errors cannot recur.

### 1c. Blog Whitelist

21 of 40 recommended posts had under 90 words of body text, several had none, and each carried a confident description of content that does not exist.

- [ ] Open every candidate post and measure the body text.
- [ ] **Under 300 words of real text: not linkable.** Video-only and embed-only posts do not qualify regardless of topic fit.
- [ ] Blurb describes what is actually on the page. If it is a video, say so.
- [ ] Use the live post title; do not invent a subtitle.
- [ ] Check the known blacklist and whitelist in `references/known-issues.md` before measuring anything new, and add your measurements to it.

### 1d. Brand Facts

Never write a business claim from memory. Seven pages contradicted TMF's own site on company history alone. Use `references/tmf-brand-facts.md` verbatim.

---

## Step 3: Fetch Collection Page + Pick Links + Related Blogs

### 3a. Fetch the target collection

Extract: current title (H1), meta, product count, product names + URLs, any existing description.

If `web_fetch` fails or the grid can't be parsed, do not block - infer from the internal link list and flag it in the strategy report. But Gate 1's Fact Sheet still has to be built product by product; a failed collection fetch is not permission to skip it.

### 3b. Select links

- **Sub-collection links** power the "Shop by category" section. Always link a relevant one if it exists.
- **Product links:** every named product links to its product page. No URL available -> name it without a link and flag it.
- **Contextual links:** closest sibling collection, related category, relevant parent.

Rules: each link appears exactly once; anchor text natural; never link operational / promo-event / out-of-stock collections; never invent URLs; never self-link; **and never link a collection you have not opened and counted.**

### 3c. Select 3-5 related blogs

From the whitelist built in Gate 1c. Priority: posts featuring the collection's products, then how-to / care guides, then buying guides. Each gets a 1-2 sentence blurb. If fewer than 3 whitelist-passing posts exist, use what qualifies and report the shortfall rather than padding with stubs.

---

## Step 4: Strategy Report + Outline

Produce sections A-G, then **wait for explicit approval.**

**A. Search Intent** - primary intent, purchase readiness, next action, emotional drivers.

**B. User Persona** - the TMF buyer is a working professional: owner-operator or multi-van, truckmount or portable, judged on callbacks and production rate. Cover pain point, top 3-5 buying criteria, pre-purchase questions.

**C. SERP Insight** - dominant page type, recurring headings, content gaps, and an **information-gain shortlist** of 2-3 expert differentiators the top 10 do not cover. These must appear in the final article. TMF's strongest differentiators historically are the ones grounded in real mechanics: airflow restriction at fittings, method-vs-chemistry compatibility, pressure ratings, fibre and pH behaviour.

**D. Strategy Decision** table - intent to serve, content goal, conversion mechanism, tone, word count target.

**E. Outline** - opening intro (50-70 words, primary keyword in first sentence), then the body H2s. Mandatory: **Why Buy [Product Group] at TMF Store**, **FAQ** (5-7 Q&As), **Related Blogs**, **META**. Optional: Shop by category / featured products (the only section where products are named), how-to-choose, applications by scenario, benefits, care/usage guide.

**F. On-page SEO** - confirm the collection title contains the primary keyword and flag if not; Meta Title 40-60 chars with keyword at the start; Meta Description 140-155 chars with a soft CTA.

TMF-specific meta rules:
- Keep the brand token. Every page in the set should end `| TMF Store` or `| TMF`.
- Do not drop a valuable term the live collection title already carries. If the live title holds "Pet Odor Remover", "Flash Cuffs" or "for Sale", keep it unless you can argue the replacement is stronger.
- Do not spend characters on the phone number. Google routinely rewrites descriptions containing phone numbers, and the click has to happen before the number matters. Spend those characters on brand-model or modifier terms instead.
- Always include brand and model terms the collection actually sells (Rotovac 360i, Hawk Brute 17, Mytee Dry GT, Namco Floorwash 5000, DriMaster DM3). They are low-competition, high-intent, and were missing from every audited page.

**G. Links + Related Blogs** - anchor text and placement for every link, for the task summary.

### Framework Feasibility Check - run before asking for approval

Four audited pages built a buying framework the inventory could not support: a head-width axis where every tool was 4 inches; an RPM band that excluded every machine sold; a pH framework where no product publishes a pH; an "enzymes first" recommendation with no enzyme product in the collection.

For each framework in the outline:

- [ ] Sort the Fact Sheet by that spec. Do the products actually spread across the range?
- [ ] Can a reader execute the framework using only what this collection sells?
- [ ] Does the framework's top recommendation point at a product TMF stocks?

Any "no": change the axis to one the inventory does differentiate on, or drop the section. Never publish generic category advice that disqualifies the products on the page.

**END OF STEP 4 - wait for approval before writing.**

---

## Step 5: Writing Rules

### GATE 2 - claim tiering while writing

Before any sentence claiming something about a named product, mark it in the working draft: `[A]` listing, `[B]` manufacturer, `[D]` category guidance with no product attached, `[?]` unsourced. Every `[?]` is deleted or demoted to `[D]` before the draft leaves your hands. Markers are stripped at delivery. `scripts/qa_check.py` fails the draft if any marker survives.

### Banned patterns

Each maps to a real error from the audit. Full detail and examples in `references/verification.md`.

1. Do not name a mechanism the listing does not name (no "peroxide-powered", "encapsulating polymer", "terpene and resin", "enzyme chemistry", "pH-buffered" unless those words are on the listing or an SDS).
2. Do not upgrade legal or technical status. "Patent pending" stays "patent pending".
3. Do not extend a surface or fibre list beyond what the listing states.
4. Do not describe a product from its name. "Hide-A-Hose" means running the solution hose inside the vacuum hose at TMF, not a retractable reel.
5. Do not present a rating without its count when the count is 1-3.
6. No absolutes about reviews ("every product here is reviewed"). Check first.
7. Do not state a saving that arithmetic can falsify. Publish real cost-per-gallon-mixed figures or drop the claim.
8. Do not invent production or volume statistics (pieces per day, contamination multipliers, CFM under load). Attribute to a named operator or cut.
9. Do not contradict another page in the batch. Fresh urine cannot be "relatively neutral" on one page and "mildly acidic" on another.
10. Do not skip a safety qualification. Ozone gets an unoccupied-space and clearance note, always.
11. Do not recommend a product your own page just argued against.
12. Do not present a sold-out product as available. See stock rules below.

### Stock disclosure

- Say it plainly, using the listing's own fulfilment wording ("1-2 weeks to fulfill").
- Lead with an in-stock equivalent from the same collection where one exists.
- Never make a sold-out item the hero product.
- Note material partial-variant availability (e.g. 2 of 6 scents in stock).

### Collection coverage

- Every section that argues for a product type links at least one product of that type. A stainless steel section with no stainless product linked is the worst of both outcomes.
- Target 80%+ product coverage for collections under 15 products; for larger ones, cover every product type the copy discusses.
- Before delivery, diff the collection feed against the page's links. If an unlinked product directly answers a question the page's own FAQ raises, link it.

### Fitment and spec tables

Where the collection is fundamentally a fitment or spec problem (cuffs, hoses, jets, tools by pressure rating), build a table: hose ID -> tool inlet -> correct product, with links. It captures a large low-competition long tail and is entirely sourceable from the Fact Sheet. This is usually the single highest-value addition to the page.

### Structure, tone and keyword rules

- One continuous article, no H1 in the body, every H2 opens with a paragraph before lists, every table followed by a 1-2 sentence summary.
- **Product names only in the Shop by category / featured section.** How-to-choose, benefits, why-buy, FAQ and Related Blogs stay general. Keeps the page evergreen when products change.
- Bullets for list-type content; prose for explanation.
- **Comparison + spec ladder pattern:** one bullet per option stating strength AND limitation, then a tiered list mapping a measurable spec to use level, then a plain "In short, ..." decision sentence. Never leave a comparison without it.
- **Commercial signals:** only offers verified on the site or supplied by the user. Max 3 mentions of the same offer across the article (intro/early body, Why Buy, at most one FAQ).
- **Dashes: hyphen `-` only.** No em dash, en dash, or double hyphen anywhere, including headings, FAQ and META. Rewrite the sentence instead.
- **US English.** TMF is a US brand.
- Commercial tone, not editorial. No "in this guide we'll explore". Avoid AI-tells.
- **Primary keyword:** at least 2 per 1,000 words of body (a floor, not a target). Required in Meta Title, Meta Description, the collection title (check and flag), at least one H2, and the intro's first sentence.
- **Secondary keywords:** each at least once.
- One primary keyword per page. Dual primaries only with explicit user confirmation.
- When the exact keyword breaks grammar, use a close variant and record the substitution in the task summary.
- **FAQ answers: 20-40 words**, direct, no product names.
- **Why Buy at TMF Store: 60-100 words**, real differentiators, facts drawn only from `references/tmf-brand-facts.md`.

---

## Step 6: Automated Checks

```bash
python3 scripts/qa_check.py draft.md \
  --primary "PRIMARY KEYWORD" \
  --secondary "SEC 1" "SEC 2" \
  --meta-title "..." --meta-desc "..." \
  --allowed-urls urls.txt
```

It reports word count, primary keyword floor, secondary coverage, banned dashes, meta lengths, surviving `[?]` / `[A]` / `[B]` markers, and any URL in the draft that is not in the supplied site URL list. Do not deliver content that fails. Fix inline.

---

## GATE 3 - pre-delivery checklist

Nothing ships until every box is ticked. Attach the completed checklist to the delivery. Full version in `references/verification.md`.

**Structure**
- [ ] Meta Title and Meta Description present (one audited page shipped without either), 40-60 / 140-155 chars.
- [ ] Meta Title keeps the brand token and does not drop a valuable term the live collection title already carries.
- [ ] Target collection resolves; no other page in the batch targets the same URL or term.

**Products**
- [ ] Every named product exists, with the exact live title.
- [ ] Every price, rating and review count matches the live page today.
- [ ] Every variant's availability checked; any sold-out item disclosed.
- [ ] Every mechanism, category and surface claim traces to a listing quote in the Fact Sheet.
- [ ] No rating claim rests on fewer than 4 reviews without the count stated.

**Links**
- [ ] Every URL returns 200 and comes from the supplied list. None invented.
- [ ] Every linked collection was opened and its contents match the description given.
- [ ] Every related blog is on the whitelist; every blurb matches the actual body text.

**Claims**
- [ ] Zero `[?]` markers remain.
- [ ] Business facts match `references/tmf-brand-facts.md` exactly.
- [ ] Every numeric claim sourced or removed.
- [ ] Safety qualifications present where relevant.
- [ ] No claim contradicts another page in the batch, the target collection, or a linked product listing.

**Read-through**
- [ ] One editor reads end to end asking: would a working technician who owns these products spot anything wrong? The DM3, T-REX Jr. and Hoser errors would all have failed this test.
- [ ] Proofread pass for garbled sentences. One audited page shipped with "protects jets and jets keep".

---

## Step 7: Delivery

**1. The article** - one clean copy-ready block, ending with FAQ -> Related Blogs -> META.

**2. Task summary in chat**, which MUST include:

```
Links used:
- Sub-collections: [anchor] -> [URL] (placed in: ...)
- Products (in listing): [Product] -> [URL]
- Other contextual links: ...
- Related Blogs: ... (3-5, all whitelist-passing, with measured word counts)

Keyword adaptations:
- "[exact keyword]" -> variant "[variant]" in [section], because [reason]
  (or: none)

QA check result: [output of scripts/qa_check.py]

Gate 3 checklist: [attached / all boxes ticked]

Claims dropped for lack of a source:
- [claim] - would need [pH / RPM / unit weight / SDS] published on [listing]

Store-side issues found while writing:
- [empty or thin collection, duplicate listing copy, dead blog, broken link]
```

Default delivery is markdown in chat. Export to `.docx` only on request.

---

## Reference files

Read these when the workflow points to them.

- `references/verification.md` - Product Fact Sheet spec with worked example, the twelve banned patterns with the real error each prevents, and the full Gate 3 checklist.
- `references/tmf-brand-facts.md` - verified business facts, plus the ones that are still open and must not be written until TMF decides.
- `references/product-corrections.md` - the verified truth for every product the audit caught being misdescribed. Check before writing about any of them.
- `references/known-issues.md` - collection handle traps, the keyword cannibalisation map, thin and empty collections, and the blog blacklist / whitelist with measured word counts.

---

## Quick Reference - mistakes to avoid

| Mistake | Fix |
|---|---|
| Writing a product description from its title | Open the listing. This caused 36 of 36 false claims |
| Naming a mechanism the listing does not name | Quote the listing or say nothing |
| Building a framework the inventory cannot support | Run the Framework Feasibility Check before the outline |
| Featuring a sold-out product, especially as hero | Check availability the day you deliver; lead with an in-stock equivalent |
| Linking a blog under 300 words of body text | Whitelist only; measure before linking |
| Describing blog content that does not exist | Blurb describes what is actually on the page |
| "Since 2008" or any improvised business fact | Use `references/tmf-brand-facts.md` verbatim |
| A savings or production number nobody checked | If a calculator can falsify it, verify or cut it |
| A section that argues for a product type and links none | Link at least one product per argued type |
| Linking a collection you never opened | Open it, count it, then describe it |
| Writing an H1 into the body | Shopify title is the H1; open with the intro |
| Product names outside the listing section | Keep FAQ, how-to-choose and why-buy general |
| Phone number in the meta description | Spend the characters on brand-model terms |
| Dropping the brand token from the Meta Title | Keep `| TMF Store` |
| Em dash / en dash / double hyphen | Hyphen only; rewrite the sentence |
| Inventing a URL | Only URLs from the supplied list |
| Writing before outline approval | Wait for explicit confirmation after Step 4 |

---

## Collection Size Cheat Sheet

| Products / structure | Strategy |
|---|---|
| Parent / hub with sub-collections | Longest. Lead with Shop by category, H3 per sub-collection. Often 900+ words |
| 1-7 products | ~600-900 words. Heavy on benefits, method, trust. Name and link the few products |
| 8-20 products | ~350-500 words, expand if useful. Grid is the hero |
| 20+ products | Lean intro, longer body (4-5 H2s). Use how-to-choose / shop-by-category. A fitment or spec table usually earns its place here |
