# Technical SEO Baseline (OUTSIDE the QRG)

The Search Quality Evaluator Guidelines do not cover technical SEO. This list is general industry practice, included so an audit can be "complete". Always label these findings in the report as "ngoài phạm vi QRG" (outside the QRG) and priority P3 unless they block indexing (then P0).

Only check what you can actually verify with the tools available (fetched HTML, search). Don't invent Core Web Vitals numbers - recommend PageSpeed Insights / Search Console if you can't measure.

## Crawl & index (can block everything → P0 if broken)
- [ ] Page returns 200; no accidental `noindex` meta/header; not blocked by robots.txt
- [ ] Canonical tag points to the right URL (self or intended master)
- [ ] Included in XML sitemap; reachable via internal links (not orphaned)
- [ ] No soft-404s; redirects are single-hop 301s
- [ ] Duplicate/parameter URLs consolidated

## On-page elements
- [ ] One clear `<title>` that summarizes the MC (QRG treats title as MC - accuracy matters)
- [ ] Meta description accurate (affects snippet → Needs Met)
- [ ] Logical H1/H2 structure
- [ ] Descriptive image alt text; original images compressed
- [ ] Internal links with descriptive anchors to related content

## Structured data
- [ ] Schema matches visible content (Product, Offer, Review, Article, Author/Person, Organization, LocalBusiness, FAQ where eligible)
- [ ] No markup for content that isn't on the page (misleading)

## Experience
- [ ] Mobile-friendly, readable without zoom
- [ ] HTTPS everywhere; secure checkout
- [ ] Reasonable speed; no layout shifts pushing MC around (ties to "obstructed MC" in QRG if caused by ads)
- [ ] Interstitials easy to close

## International / local
- [ ] `hreflang` correct for multilingual sites; language matches locale
- [ ] NAP (name, address, phone) consistent for local businesses
