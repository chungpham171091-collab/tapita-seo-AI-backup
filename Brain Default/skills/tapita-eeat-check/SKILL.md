---
name: "tapita-eeat-check"
description: Full SEO quality audit of a webpage, website or draft content based on Google's Search Quality Evaluator Guidelines (QRG, Sept 2025) - Page Quality (Lowest to Highest), E-E-A-T, YMYL, spam policies (scaled content abuse, site reputation abuse, expired domain abuse, copied/paraphrased/AI content), deceptive design, title quality, filler, ads/SC, reputation, and Needs Met / search intent fit for a target keyword. Use this skill whenever the user asks to audit, review, check, score or diagnose a page or content for SEO, E-E-A-T, helpful content, content quality, YMYL compliance, ranking drops after a core update, or "why is this page not ranking" - even if they don't mention Google guidelines. Triggers include a URL plus "audit", "kiểm tra SEO", "đánh giá chất lượng trang", "audit E-E-A-T", "kiểm tra nội dung chuẩn Google", "check helpful content", "tại sao trang bị tụt hạng", "chấm điểm page quality", "kiểm tra spam/AI content", or pasted article/product copy the user wants reviewed before publishing.
---

# SEO Quality Audit (based on Google Search Quality Evaluator Guidelines)

This skill turns the 182-page Search Quality Evaluator Guidelines (QRG, version 11 Sept 2025) into a repeatable audit. It answers two questions Google's raters answer:

1. **Page Quality (PQ)** - how well does the page achieve its purpose, and is it trustworthy? (independent of any query)
2. **Needs Met (NM)** - how well does the page satisfy the user searching a specific query? (only if a target keyword is given)

Keep in mind (and tell the user once, briefly): rater scores don't directly change rankings. The QRG describes what Google's ranking systems are *trying* to reward, so it is the best public map of "quality" - but it does not cover crawling, indexing, speed or other technical SEO. Those live in `references/technical-baseline.md` and are clearly labelled as outside the QRG.

## Step 0 - Collect inputs

Work out what you have before starting. Ask at most one question, and only if something essential is missing.

- **The page**: URL (fetch it with web_fetch), or pasted content/draft. For a draft, you can't check live layout, ads, or site info - say so and audit what's there.
- **Target query + locale** (optional): needed for Needs Met. If the user names a keyword, use it. Default locale to the user's market (e.g. Vietnamese - VN).
- **Site context**: homepage, About, Contact, author page, policies. Fetch them if you have a URL - a PQ rating needs the website, not just the page.
- **Scope**: single page, a template (e.g. all product pages), or a site sample. For site-level issues (scaled content, systemic broken pages), look at several pages.

## Step 1 - Understand the page

Record, in a few lines:

- **Purpose** of the page (inform, sell, review, entertain, tool, forum...). Every page type can be Highest or Lowest - type never decides quality.
- **Page type** - pick the matching checklist in `references/page-type-checklists.md`.
- **MC / SC / Ads**: what is Main Content (including title, tabs, reviews, tools), Supplementary Content (navigation, related links), and Ads/monetization (ads, affiliate links - all monetized links count as Ads).
- **Who is responsible** for the site and **who created the MC** (company, named author, UGC users).
- **YMYL level**: clear YMYL / maybe / not YMYL, and which type (Health & Safety, Financial Security, Government/Civics/Society, Other). Use the two-question test and examples in `references/eeat-ymyl-reputation.md`. YMYL raises the bar for everything below.

## Step 2 - Lowest screening (always do this first)

Google's raters screen for harm and deception *before* judging quality. Any single hit = **Lowest**, no matter how expert or polished the page is. Check every item in `references/lowest-spam-trust.md`:

- Harmful purpose / harmful to self, others, or specified groups
- Harmfully misleading information (clearly false, contradicts expert consensus, unsubstantiated theories) - especially on YMYL
- Untrustworthy: deceptive purpose, fake/AI-generated author profiles, invented credentials, fake testing claims, impersonation, fake physical store
- Deceptive design: ads disguised as content or navigation, trick buttons, title unrelated to content
- Deliberately obstructed MC (sticky ads impossible to close, coercive interstitials, MC pushed far down by ads)
- Spam: no/gibberish MC, hacked or spammed comments, **expired domain abuse**, **site reputation abuse**, **scaled content abuse**, MC almost entirely copied/paraphrased/AI-generated/embedded with no added value
- YMYL or transactional pages with no information at all about who runs the site
- Extremely negative reputation (fraud, scams)
- Extremely misleading/shocking title

If anything here hits, lead the report with it - it outweighs every other fix.

## Step 3 - Low checks

Any one of these = **Low** (details and examples in `references/page-quality-levels.md`):

- MC lacks the effort, originality, talent/skill needed for its purpose; mild inaccuracies
- Much of the MC is repackaged (paraphrased lists, "best X" built from others' reviews, reposts) with little added value
- **Filler**: lots of low-value text, or prominent filler that pushes the useful answer down (e.g. recipe/how-to buried under generic intro)
- Title slightly misleading, exaggerated or clickbait
- Ads/SC significantly distract from or interrupt the MC
- Not enough info about the site/author for the page's purpose (stores and payment pages need full customer-service info: contact, returns, payment, shipping)
- Mildly negative reputation
- Inadequate E-E-A-T for the topic (e.g. review without using the product, YMYL advice without expertise)
- Exaggerated or mildly misleading claims about the site/author's expertise

## Step 4 - High / Highest signals

Medium = achieves its purpose, nothing wrong, nothing special ("typical" pages on a topic are Medium, not High). To go higher the page must show at least one of these (with no Low/Lowest problems):

- **High**: high effort/originality/skill MC (original photos, first-hand testing, unique data, well-organized and edited), positive reputation for the topic, high E-E-A-T
- **Highest**: some of the best content on the topic online; very positive reputation (experts, professional bodies, awards for YMYL); uniquely authoritative or go-to source

Compare against the current top results for the topic when possible - High is judged relative to what's available.

## Step 5 - Needs Met (only if a target query is given)

Use `references/needs-met-intent.md`:

1. Interpret the query: dominant / common / minor interpretations; intent type (Know, Know Simple, Do, Website, Visit-in-person); locale and explicit location; freshness needs.
2. Rate the page: Fully Meets (only for one specific target), Highly, Moderately, Slightly, Fails to Meet.
3. Remember: an untrustworthy or outdated page can't be Highly Meets; a useless page is Fails to Meet even with good PQ; a page matching keywords but ignoring important query words (e.g. "non emergency", "healthy") misses the intent.
4. Check the SERP snippet: does the title + meta description accurately represent the MC?

## Step 6 - Rate and prioritize

- Give a PQ rating on the scale Lowest, Lowest+, Low, Low+, Medium, Medium+, High, High+, Highest. If torn between two, use the lower; between three, the middle.
- Every finding needs **evidence** (quote the line, name the element, link the source) and the **QRG section** it comes from. No evidence → mark as "cần kiểm tra thêm" (needs verification), not as a fact.
- Do reputation research with web_search when you have a URL: `[brand -site:domain]`, `["domain.com" reviews -site:domain]`, `[brand site:wikipedia.org]`, news, expert mentions. Independent sources beat what the site says about itself. No reputation info for a small site is neutral, not negative.
- Prioritize fixes: **P0** = Lowest triggers (fix before anything else), **P1** = Low triggers, **P2** = steps from Medium to High/Highest, **P3** = technical baseline / nice-to-have.

## Report format

Write the report in the user's language (Vietnamese if they wrote in Vietnamese; keep English terms like E-E-A-T, YMYL, MC in parentheses the first time). Use this structure:

```
# Báo cáo SEO Quality Audit: [page/title]
**URL / nội dung:** ...  |  **Truy vấn mục tiêu:** ... (locale)  |  **Ngày audit:** ...

## 1. Tóm tắt
- Page Quality: [rating] - 1-2 câu lý do chính
- Needs Met: [rating] cho [query] (nếu có)
- YMYL: [mức] - [loại]
- 3 việc cần làm ngay

## 2. Hiểu trang
Mục đích | Loại trang | MC / SC / Ads | Ai chịu trách nhiệm & ai tạo nội dung

## 3. Kiểm tra Lowest (P0)
Bảng: Tiêu chí | Đạt / Không đạt / Cần kiểm tra | Bằng chứng | Mục QRG

## 4. Kiểm tra Low (P1)
(cùng bảng)

## 5. E-E-A-T & danh tiếng
Experience | Expertise | Authoritativeness | Trust - mỗi mục: đánh giá + bằng chứng
Kết quả nghiên cứu danh tiếng (nguồn độc lập)

## 6. Needs Met & ý định tìm kiếm (nếu có truy vấn)

## 7. Lộ trình lên High/Highest (P2)

## 8. Kỹ thuật cơ bản - ngoài phạm vi QRG (P3, nếu kiểm tra)

## 9. Danh sách việc cần làm
Bảng: Ưu tiên | Vấn đề | Cách sửa cụ thể | Mục QRG
```

For a quick check (user asks "nhanh", or pastes a short draft), shorten to sections 1, 3-4 combined, and 9.

Fixes must be concrete: not "improve E-E-A-T" but "add an author box linking to [name]'s profile with their 8 years as a licensed pharmacist; cite the Ministry of Health guideline for the dosage claim in paragraph 3".

## Judgment rules from the guidelines

- Trust is the center of E-E-A-T. An untrustworthy page has low E-E-A-T however expert it looks.
- Harm assessment overrides experience/expertise.
- Ads alone never lower quality; obstruction and deception do. Paywalls/logins are fine.
- AI use alone doesn't decide quality - effort, originality and added value do. But fake AI author personas are deceptive (Lowest).
- Licensed/syndicated content isn't "copied".
- YMYL facts and advice need expertise; YMYL personal experience is valuable if safe and consistent with expert consensus.
- Aliases are fine on forums/UGC; stores and YMYL pages need real identity and contact info.
- Don't rate on looks ("is it pretty?") - rate on purpose, MC, trust.
- Don't penalize a page because it's in another country/locale for PQ; locale matters for Needs Met.

## Reference files

Read the ones you need - each is self-contained:

- `references/lowest-spam-trust.md` - full Lowest criteria, spam policies, deception types, how to detect copied/paraphrased/AI content (read for every audit)
- `references/page-quality-levels.md` - Low / Medium / High / Highest criteria with examples
- `references/eeat-ymyl-reputation.md` - E-E-A-T definitions, YMYL test and examples, reputation research method, experience vs expertise for YMYL
- `references/needs-met-intent.md` - query interpretation, intent types, Needs Met scale, freshness, product and local queries, PQ vs NM
- `references/page-type-checklists.md` - checklists for product, category/collection, blog/how-to, review/affiliate, YMYL health/finance, local business, news, forum/UGC, homepage/About, 404/error pages, AI-assisted content programs
- `references/technical-baseline.md` - technical SEO items outside the QRG (crawl, index, speed, schema)
