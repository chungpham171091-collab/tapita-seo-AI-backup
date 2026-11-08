---
name: shopify-collection-seo
description: "End-to-end SEO content workflow for Shopify collection pages (category pages). Use this skill whenever the user asks to write, optimise, or…"
---

# Shopify Collection Page SEO Content Skill

End-to-end workflow for writing SEO-optimised content for Shopify collection pages. Covers strategy research, outline, on-page meta, sub-collection and product linking, related-blog recommendations, and full content writing.

This skill is for **commercial category pages**, not blog posts. Tone, structure, length, and CTAs differ.

## How the deliverable is shaped

Get this part right; it drives everything else.

- **The article is written as one continuous, clean, copy-ready piece.** The user pastes it straight into the Shopify collection description, so it carries content only: no "Block 1 / Block 2" dividers, no "H1:" / "H2:" / "H3:" label prefixes on headings. Headings are plain heading text (markdown `##` / `###`).
- **No H1 in the body.** The Shopify theme already renders the collection title as the page H1, so writing another H1 would create a duplicate. The article opens with the intro paragraph. (Do still check that the collection title itself contains the primary keyword, and flag it to the user if it doesn't.)
- **Links live inline in the body.** Sub-collection links, named-product links, contextual links, and blog links all appear as natural inline markdown links inside the article. The consolidated list of them (anchor + URL + placement) is NOT in the article - it goes in your task summary in the chat.
- **The article ends with two fixed bottom blocks, in this order:** the `Related Blogs` section (the last reader-facing content), then the `META` block (Meta Title + Meta Description) as the technical footer.

So at delivery there are two things: (1) the clean article, ending with Related Blogs then the META footer; (2) a task summary in chat that lists every link used and notes any keyword substitutions.

---

## Workflow Overview

Every request follows this sequence. Do NOT skip steps. Confirm with the user at each gate.

```
Step 1: Collect required inputs (URL + keyword + brand + internal link list + product URLs + blog URLs)
Step 2: Pull top 10 SERP results (web_search - REQUIRED)
Step 3: Fetch collection page + pick links (sub-collections, products, contextual) + 3-5 related blogs
Step 4: Produce strategy report + outline -> WAIT for user confirmation
Step 5: Write the content (one continuous, clean, copy-ready article)
Step 6: Run keyword + dash + meta length check
Step 7: Deliver (clean article ending with Related Blogs + META; link list + keyword notes in the task summary)
```

---

## Step 1: Collect Required Inputs

Before doing anything, confirm all of the following are present. If any are missing, STOP and ask the user.

**Required from user:**
- **Collection URL** (the actual live Shopify collection URL, e.g. `https://store.com/collections/xyz`)
- **Primary keyword** (single phrase the page should rank for)
- **Secondary keywords / variants / semantic terms** (optional but recommended - if not provided, ask)
- **Brand name** (needed for the mandatory "Why Buy ... at [Brand]" section. Usually inferable from the store domain; confirm with the user if ambiguous.)
- **Internal link list** (full website URL list - sub-collections / child collections, sibling collections, **product URLs**, and blog URLs. Required for internal linking, including linking each named product to its product page. Ask for this upfront.)
- **Blog URL list** (the site's blog/article URLs - for the Related Blogs section in Step 3c. If already inside the internal link list, just confirm blog posts are included.)
- **Top sellers / featured products** (optional - if not provided, will try to fetch the collection page in Step 3; if grid is empty or unfetchable, ask. These are the only products that get named, and each should link to its product URL.)

**Do not proceed without collection URL, primary keyword, brand name, internal link list, and blog URLs.** Ask in a single message:

> Mình cần các thông tin sau trước khi bắt đầu:
> 1. URL collection page (live URL)
> 2. Từ khoá chính + từ khoá phụ / variants (nếu có)
> 3. Tên thương hiệu (để dùng cho mục "Why buy ... at [Brand]")
> 4. Danh sách URL toàn site để chọn internal link (sub-collection + product URL + blog URLs)
> 5. Danh sách URL blog/bài viết (để chọn 3-5 bài cho mục Related Blogs)
>
> Optional: nếu Max đã có list top sellers / featured products (kèm product URL) thì gửi luôn, không thì mình sẽ tự fetch.

---

## Step 2: SERP Research (web_search REQUIRED)

**Hard rule:** Use `web_search` to pull the top 10 results on Google for the target market. Do not infer from training data.

**If `web_search` is not available or fails:** STOP and report to the user. Present two options and wait for the user's choice - do NOT proceed automatically.

```
web_search không khả dụng / fail. Max chọn 1 trong 2 hướng:

Option 1 - Cung cấp data thủ công:
Paste top 10 kết quả Google.co.uk cho từ khoá "[KEYWORD]"
(URL + page title; bonus nếu có headings hoặc word count)

Option 2 - Tự chạy tiếp không có SERP:
Mình sẽ skip phần SERP insight và làm strategy report dựa trên
intent + persona + best practice cho ngành. Sẽ flag rõ phần này
trong report để Max biết SERP gap chưa được kiểm chứng.
```

Do not silently skip or fabricate SERP data. Wait for user response before continuing.

Search formatting:
- Query = primary keyword exactly as given
- Add market modifier if needed: `[keyword] UK`, `[keyword] site:.co.uk`, etc.
- For UK market: use `google.co.uk` results context
- Run 2-3 queries if needed: primary keyword, primary keyword + market, primary keyword + "best" or "buy"

For each top result, record:
- URL
- Page type (collection / category / product / blog / marketplace)
- H1 / page title
- Visible heading structure (use `web_fetch` on the top 3-5 most relevant for deeper analysis)
- Approximate word count of text content
- Trust signals (reviews, materials, shipping info)

**Output of this step:** a table of 10 results with the columns above, plus 2-3 insight sentences on what Google is rewarding for this keyword.

---

## Step 3: Fetch Collection Page + Pick Links + Related Blogs

### 3a. Fetch the target collection page

Use `web_fetch` on the collection URL provided. Extract:
- Current collection title (this is the H1) and meta
- Number of products in the collection
- Top 4-6 product names + their product URLs (for the listing - the only place products get named and linked)
- Any existing description text (so the rewrite doesn't lose context)

**If `web_fetch` fails, returns empty, or the product grid can't be parsed:**
- Do NOT block. Use the internal link list provided in Step 1 - the sub-collection / sibling URLs and slugs give enough context to infer the category, variants, and likely featured products.
- In the strategy report (Step 4), note: "Collection page fetch failed - product count + top sellers inferred from internal link list. Please confirm or correct."
- Default to **standard length** unless the user indicates otherwise.

### 3b. Select links from the user's list

From the URL list provided in Step 1, select the links that will appear inline in the article:

**Sub-collection links (priority for hub / large category pages):** if this collection is a parent with relevant child collections, link to them. These power the "Shop by category / Browse our range" section. Always link a sub-collection if a relevant one exists in the list.

**Product links:** every product you name in the listing (Step 4 outline) must link to its product page, using the product URL from the user's list. If a named product has no URL in the list, name it without a link and flag it in the task summary so the user can add the link.

**Contextual links:** the closest sibling collection (same category, different variant), a related material/occasion collection, or a relevant parent.

Rules:
- Each link appears exactly once in the final content.
- Anchor text must be natural in context (not exact-match stuffed, never "click here").
- Never link to operational / out-of-stock / promo-event collections.
- Never invent URLs - only use URLs from the list the user provided.
- Never link to the collection page being optimised (self-link).

### 3c. Select 3-5 related blogs (for the "Related Blogs" section)

From the **blog URL list**, pick **3-5 blog posts** that feature the products or cover a closely related topic (styling, care, buying guides, gift guides, trend pieces). They power the Related Blogs section at the bottom of the article.

Selection priority:
1. Posts that directly use / feature the collection's products
2. How-to, care, or styling guides relevant to the product type
3. Buying guides, gift guides, or trend round-ups in the same niche

Rules:
- Pick 3-5 (not fewer than 3, not more than 5). If fewer than 3 relevant posts exist, use what's relevant and note the shortfall.
- Each blog gets a natural 1-2 sentence blurb, not a bare link.
- Only use URLs from the user's provided blog list. Never invent blog URLs.
- These count as internal links and go in the link list in the task summary (Step 7).

---

## Step 4: Strategy Report + Outline

Produce sections A through G below. Keep prose tight. This is the deliverable the user reviews before writing begins.

### A. Search Intent Analysis

- Primary intent: Transactional / Commercial Investigation / Informational
- Purchase readiness: Low / Medium / High (collection pages usually Medium-High)
- What the user wants to do immediately after the search
- Emotional drivers (status, gift-giving, self-expression, problem-solving, etc.)

### B. User Persona

- Demographic: age, gender, role
- Core pain point or job-to-be-done
- Top 3-5 criteria they evaluate before buying
- Common questions they need answered before adding to cart

### C. Top 10 SERP Insight Summary

- Dominant page type ranking
- Recurring heading patterns across top results
- Content gaps - what the top 10 are NOT doing well
- **Information-gain shortlist:** from those gaps, pick 2-3 expert differentiator points the article will cover that the top 10 do not (specialist knowledge a seller has but competitors don't write down: e.g. wax type vs burn time for candles, fabric GSM for apparel, chemical pH vs surface type for cleaning). Prefer points that turn a seemingly cosmetic attribute into a functional buying criterion. These carry into the outline and MUST appear in the final article.
- One paragraph: what Google is rewarding for this keyword

### D. Strategy Decision

| Item | Value |
|---|---|
| Primary intent to serve | ... |
| Content goal | ... |
| Conversion mechanism | ... |
| Tone | ... |
| Word count target | ... (use the cheat sheet, but expand freely for hub pages) |

### E. Outline

The article is one continuous piece. In the outline you may label heading levels for planning - those labels get stripped in the final article (Step 5). There is no H1 in the body; the Shopify collection title is the H1.

**Opening**
- **Intro paragraph** (50-70 words, no bullets, opens with primary keyword in the first sentence where natural). No H1 above it.

**Body** - choose the optional H2 sections that fit; the two marked ALWAYS are mandatory. Order the mandatory bottom blocks exactly as shown.

- **Shop by category / Browse our range** - introduce the relevant **sub-collections** (each linked) and/or the **best-seller / featured products** (each linked to its product page). This is the ONLY section where specific product names appear. For a parent/hub page this is usually the backbone and can use H3 sub-headings per sub-collection.
- **Method / how-to-choose guide** (buying guide - useful with multiple variants or methods)
- **Applications / use cases by role or scenario** - use when the collection serves several distinct situations, user types, or occasions (e.g. jewellery by occasion: wedding / gifting / everyday; cleaning chemicals by surface type; gym gear by training goal). One short paragraph per scenario, each ending with a concrete spec or variant recommendation, general terms only (no product names). Strong for long-tail coverage; skip if the collection has one obvious use.
- **Benefits / standout features** of this product group
- **Styling / usage / care guide** (especially valuable for sparse collections)
- **Why Buy [Product Group] at [Brand]** - ALWAYS include. Brand-name heading (e.g. "Why Buy Your Carpet Chemicals at TMF Store"). Short, 60-100 words, real differentiators (sourcing, expertise, value, shipping), not fluff.
- **FAQ** - 5-7 short Q&As.
- **Related Blogs** - ALWAYS include, at the BOTTOM. Heading is literally "Related Blogs". Introduces the 3-5 blogs from Step 3c, each with a 1-2 sentence blurb and a link. This is the last reader-facing section.
- **META block** - the technical footer, appended below Related Blogs: Meta Title + Meta Description.

### F. On-page SEO

- **Collection title (the H1):** confirm it contains the primary keyword. Set in Shopify, NOT written in the body. Flag to the user if the keyword is missing.
- **Meta Title** (under 60 chars, primary keyword at start)
- **Meta Description** (under 155 chars, primary keyword once, includes a soft CTA)

### G. Links + Related Blogs

List, with proposed anchor text and placement: sub-collection links, named-product links, other contextual links, and the 3-5 related blog links. This is what you'll report in the task summary at delivery (it does not go inside the article).

**END OF STEP 4 - ask the user to confirm before writing.** Do not proceed to Step 5 without explicit approval.

---

## Step 5: Writing Rules

Apply ALL of these rules to every piece of collection content.

### Structure

- One continuous article, top to bottom. No "Block 1 / Block 2" split.
- **No H1 in the body.** Open with the intro paragraph.
- **Intro:** 50-70 words, opens with primary keyword in the first sentence where natural.
- Every H2 opens with a paragraph before any sub-elements (H3s, lists).
- Every table is followed by a 1-2 sentence summary.
- **Bottom order is fixed:** the "Why Buy ... at [Brand]" section and FAQ sit above, then **Related Blogs** is the last reader-facing section, then the **META** footer closes the article.
- Stick strictly to the approved outline. Do NOT add or remove H2s without asking.

### Product naming + linking - only in the Shop by category / listing section

Name specific products / SKUs ONLY inside the "Shop by category / Browse our range" (top sellers / featured) section. Everywhere else - how-to-choose, benefits, why-buy, FAQ, Related Blogs - keep it about the category, method, materials, and benefits in general terms. This keeps the page evergreen (products change; the guide content shouldn't break) and concentrates the buying signal where it converts.

Each named product links to its product page (`[Product Name](product-url)`) using the URL from the user's list. No URL available -> name it without a link and flag it in the summary.

### Bullets

Bullets are fine and expected for genuine listings: the product "top picks" under each sub-collection, included items, product types. For explanatory content (intro, how-to-choose, benefits, why-buy), prefer flowing prose. So: list-type content -> bullets OK; explanation -> prose.

### Information gain - mandatory

Every article must include the 2-3 expert differentiator points shortlisted in Step 4C (knowledge the top 10 SERP results do not cover). Weave them into the how-to-choose, applications, or benefits sections, and echo at least one of them in an FAQ answer so the claim gets restated naturally. If SERP research was skipped (Step 2 Option 2), still include 2-3 specialist points based on category knowledge and flag in the task summary that they are unverified against the SERP.

### Comparison + spec ladder pattern

When the collection spans multiple materials, types, or tiers, use this repeatable pattern:

- **Comparison block:** one short bullet per option (material A vs B vs C, or type/range comparison), each stating its strength AND its limitation.
- **Spec ladder:** a short tiered list mapping a measurable spec to use level (e.g. price bands, sizes, thickness, wattage: "entry tier - light use / mid tier - regular use / top tier - heavy or professional use").
- **Closing line:** every comparison block and spec ladder ends with one plain-prose "In short, ..." sentence that tells the reader which option fits which buyer. Never leave a comparison or ladder without this decision sentence.

### Commercial signals - placement and limits

Commercial signals are the store's offers: free-shipping threshold, case/bulk pricing, quote requests, warranty, trade accounts, etc.

- **Only use offers the user provided or that are visible on the site when fetched in Step 3.** Never invent or assume an offer (no guessing shipping thresholds or discounts).
- Placement: once in the intro OR early body, once in the "Why Buy ... at [Brand]" section, and at most once in an FAQ answer.
- Hard cap: the same offer appears **no more than 3 times** in the whole article. Repeating "free shipping over $X" in every section reads as filler and dilutes the copy.

### Claims verification - certifications, standards, legal and health claims

Any claim about certifications, standards, regulations, or health/safety effect (e.g. FDA-compliant, CE marked, NFPA/ASTM/ISO certified, "required by law in most states", "clinically proven", "hypoallergenic", organic/eco certifications) may ONLY be used if it appears on the fetched collection/product page or was explicitly provided by the user.

- If a claim cannot be verified from those sources: leave it out, or soften to a non-claim ("check the product page for current certification details") and flag it in the task summary.
- Extra caution for YMYL-adjacent categories (supplements, medical/PPE, baby products, food, finance-related goods): in these niches, unverifiable claims must be dropped, not softened.
- Never copy a certification from one product onto the whole collection ("all gloves here are NFPA certified" when only one SKU is).

### Dashes - hyphen only

Use only the standard hyphen `-`. Never use an em dash (`—`), an en dash (`–`), or a double hyphen (`--`) anywhere. If a sentence wants a long dash for a pause or aside, rewrite it: use a comma, a colon, parentheses, or split into two sentences. Applies to body, headings, bullets, FAQ, and META - everywhere.

### Tone

- Commercial, not editorial. This is a category page, not a blog.
- Confident, product-aware language. Avoid information-page phrasings like "in this article we'll explore...".
- Match the brand voice (UK English for UK brands, US English for US brands, etc.)
- Avoid AI-tells: "delve into", "navigate the world of", "look no further", "elevate your style" used repeatedly, etc.

### Keyword Rules

Natural grammar and context come first. Hitting a keyword count never justifies an awkward sentence.

- **Primary keyword:** at least **2 times per 1,000 words** of body text (a floor, not a target to pad toward).
- **Primary keyword required in:** Meta Title, Meta Description, the collection title (the Shopify H1 - check and flag, not written in the body), at least one H2, and the first sentence of the intro (or the second sentence if first-sentence flow demands it).
- **Secondary keywords:** each appears **at least once** in the body.
- **Dual primary keyword (exception, not default):** a collection page should target ONE primary keyword. Only run two primaries when the user confirms the page intentionally serves two buyer groups on one page (e.g. "tattoo gloves" + "beauty salon gloves"). In that case: both keywords appear in the intro's first two sentences, each gets at least one H2, each meets the 2-per-1000-words floor, and the Meta Title carries both (or the closest combined form that fits 60 chars). If the two keywords have genuinely different intents, recommend splitting into two collections instead of forcing one page - flag this in the strategy report and let the user decide.
- **When the exact keyword does not fit grammar or the paragraph's context:** use a close variant of that keyword (singular/plural, reordered words, a natural synonym) or split the phrase across the sentence instead of forcing the exact string. Do this for primary or secondary keywords as needed. **Whenever you substitute or split a keyword, record it in the task summary** so the user knows which exact-match target was adapted and why.
- Never stuff. If the text feels keyword-heavy when read aloud, it is too much.

### FAQ

- Placed near the end, just above Related Blogs.
- 5-7 questions.
- Each answer: **short, 20-40 words**, direct, no filler. Keep to this even on technical topics - split into a second FAQ if one answer needs more.
- Questions a buyer would actually ask before purchase (sizing, materials, compatibility, care, shipping, gifting, durability).

### Output Format - clean and copy-ready

The user pastes the whole article into Shopify, so it carries content only.

- **Headings are plain heading text.** Use markdown `##` / `###`, but never prefix a heading with a label.

  Write this:
  ```
  ## How to Choose Carpet Cleaning Chemicals That Match the Job
  ```
  Not this:
  ```
  H2: How to Choose Carpet Cleaning Chemicals That Match the Job
  ```

- **No zone dividers** ("BLOCK 1 / TOP OF PAGE" etc.) inside the article. It is one continuous piece.
- **Links are inline markdown links** (`[anchor](https://...)`). The consolidated list of them lives in the task summary, not the article.
- **The article ends with these two blocks, in order:**
  ```
  ## Related Blogs
  [blog 1 blurb + link]
  [blog 2 blurb + link]
  [blog 3 blurb + link]

  ## META
  Meta Title: ...
  Meta Description: ...
  ```

---

## Step 6: Keyword + Dash + Meta Check

After writing, before delivering, run a quick check. Use bash with python or node.

```bash
python3 -c "
import re
text = '''PASTE FULL CONTENT HERE'''
meta_title = 'PASTE META TITLE HERE'
meta_desc = 'PASTE META DESCRIPTION HERE'
text_lower = text.lower()
total = len([w for w in re.findall(r'\b\w+\b', text)])
primary = 'PRIMARY KEYWORD'.lower()
primary_count = len(re.findall(re.escape(primary), text_lower))
print(f'Total words: {total}')
print(f'Primary keyword \"{primary}\": {primary_count} times')
print(f'Floor: at least 2 per 1000 words = {max(2, round(total/1000*2))}')
for k in ['SECONDARY 1', 'SECONDARY 2']:
    c = len(re.findall(re.escape(k.lower()), text_lower))
    print(f'  {k}: {c} (need >= 1)')
for bad in ['\u2014', '\u2013', '--']:
    if bad in text:
        print(f'WARNING: found banned dash: {repr(bad)}')
print(f'Meta Title: {len(meta_title)} chars (max 60)' + (' - TOO LONG' if len(meta_title) > 60 else ' - OK'))
print(f'Meta Description: {len(meta_desc)} chars (max 155)' + (' - TOO LONG' if len(meta_desc) > 155 else ' - OK'))
if primary not in meta_title.lower():
    print('WARNING: primary keyword missing from Meta Title')
if primary not in meta_desc.lower():
    print('WARNING: primary keyword missing from Meta Description')
"
```

**Fix rules:**
- Primary keyword below the floor -> add naturally in section openers, FAQ answers, table summaries. If it won't fit cleanly, use a variant / split the phrase and note it in the summary.
- Any secondary keyword at 0 -> add once in the most natural spot; if it won't fit, use a variant and note it.
- Any em dash, en dash, or double hyphen found -> rewrite the sentence.
- Meta Title over 60 chars or Meta Description over 155 chars -> shorten before delivery. Cut modifiers, not the primary keyword.

Do not deliver content that fails the checks. Fix inline first.

---

## Step 7: Delivery

Deliver in this order:

**1. The article** - one continuous, clean, copy-ready block. Headings as plain markdown headings, no labels, no zone dividers. Links inline. It ends with the FAQ, then `Related Blogs`, then the `META` footer.

**2. Task summary (in chat, not pasted into the article)** - a short wrap-up that MUST include:

Full link list - every link in the article, with anchor, full URL, and placement:
```
Links used:
- Sub-collections:
  1. [anchor] -> [URL]  (placed in: Shop by category)
- Products (in listing):
  1. [Product] -> [product URL]
- Other contextual links:
  1. [anchor] -> [URL]  (placed in: section)
- Related Blogs:
  1. [anchor] -> [URL]
  (3-5 total)
```

Keyword notes - any place the exact primary/secondary keyword was substituted with a variant or split for grammar/context, and where:
```
Keyword adaptations:
- "[exact keyword]" -> used variant "[variant]" in [section], because [reason]
- (or: none - all exact-match targets hit naturally)
```

Plus a one-line keyword + dash + meta length check result, and any flags (missing product URLs, keyword not in collection title, fewer than 3 relevant blogs, unverified certification/compliance claims removed or softened, information-gain points unverified against SERP).

Default delivery is markdown in the chat. Only export to `.docx` if the user explicitly asks.

---

## Quick Reference - Common Mistakes to Avoid

| Mistake | Fix |
|---|---|
| Writing like a blog ("in this guide we'll...") | Commercial tone, product-aware |
| Adding an H1 to the body | No body H1; the Shopify collection title is the H1. Open with the intro |
| Naming products outside the listing section | Specific SKUs only in Shop by category / Featured; other sections stay general |
| Named product without a link | Link each named product to its product page; flag if no URL is available |
| Skipping the sub-collection links | Link relevant sub-collections so the hub passes equity down |
| Missing the "Why Buy ... at [Brand]" section | Always include it, with the brand name in the heading |
| Related Blogs not at the bottom | Related Blogs is the last content section, just above the META footer |
| FAQ or blogs in the middle | Order is: ... Why Buy ... -> FAQ -> Related Blogs -> META |
| "H2:" / "Block 1" labels inside the article | Headings are plain markdown headings only |
| Link list inside the article | Links inline in the body; the list goes in the chat task summary |
| Forcing an awkward exact-match keyword | Use a variant or split the phrase, and note it in the summary |
| Product names inside FAQ answers | FAQ stays general (category, materials, specs); product names live only in the listing section |
| "Why Buy ... at [Brand]" running long | Keep it 60-100 words, one tight paragraph of real differentiators |
| FAQ with more than 7 questions | 5-7 max; cut the weakest questions, fold overlaps together |
| Unverified certification / legal / health claims | Only claims found on the fetched page or given by the user; otherwise drop and flag |
| One product's certification applied to the whole collection | Attribute certifications to the specific SKU only |
| Same offer ("free shipping over $X") repeated everywhere | Max 3 mentions: intro/early body, Why Buy, at most one FAQ |
| Comparison or spec ladder with no takeaway | End every comparison block with an "In short, ..." decision sentence |
| Skipping the information-gain points from Step 4C | The 2-3 expert differentiators are mandatory in the final article |
| Meta Title over 60 chars / Meta Description over 155 chars | Shorten before delivery; cut modifiers, keep the primary keyword |
| Two primary keywords by default | One primary per page; dual primaries only with user confirmation of a dual-intent page |
| Forgetting the keyword-adaptation notes | Always report any substitutions in the task summary |
| Em dash / en dash / double hyphen | Hyphen `-` only; rewrite the sentence |
| Inventing internal, product, or blog URLs | Only use URLs from the user's provided lists |
| Writing without user confirmation of outline | Always wait for explicit approval after Step 4 |

---

## Collection Size Cheat Sheet

Word counts are starting points, not caps. Expand freely for hub pages or when SERP leaders are longer.

| Products / structure | Strategy |
|---|---|
| Parent / hub (has sub-collections) | Longest. Lead with Shop by category linking each sub-collection (H3 per sub-collection), plus how-to-choose, Why Buy at [Brand], FAQ, Related Blogs. Often 900+ words. |
| 1-7 products | Long (~600-900 words). Heavy on benefits, styling/care, brand trust. Listing names + links the few products. Why Buy + FAQ + Related Blogs required. |
| 8-20 products | Standard (~350-500 words, expand if useful). Grid is the hero. Intro + a couple of H2s + listing + Why Buy + FAQ + Related Blogs. |
| 20+ products | Lean intro (~50-70 words). Longer body (4-5 H2s) for SEO depth. Use how-to-choose / shop-by-category. Why Buy + FAQ + Related Blogs required. |
