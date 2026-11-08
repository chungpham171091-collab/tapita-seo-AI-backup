---
name: "coway-content-compliance"
description: "Claim-safety, terminology and editorial gatekeeper for Coway Europe content (blog, product pages, FAQ, CRM, ads, PR, Amazon) in en-GB, de-DE, nl-NL and fr-FR. Use whenever writing, rewriting, reviewing, localising or QA-ing Coway or Airmega copy, or checking it for advertising-law risk, health or medical claims, unsubstantiated numbers, forbidden terms (True HEPA, GreenHEPA, H13, medical grade), ASA / HWG / DGCCRF / ACM exposure, translationese or AI-sounding text. Trigger on 'review this Airmega listing', 'rewrite for Coway UK', 'localise for de-DE', 'is this claim allowed in Germany', or Coway copy mentioning CADR, HyperCaptive, ECARF, 99.999%, 0.01 micron, allergies or PM2.5. Apply proactively before delivering ANY Coway content; Coway is liable for every claim. For a full audit-plus-rewrite of an article, coway-audit-rewrite runs the workflow and this skill supplies its rules."
---

# Coway Europe - Claim Safety, Terminology & Editorial Standard

Coway is legally responsible for every claim it publishes. In Germany a competitor can send a cease-and-desist letter (Abmahnung) over one sentence; in France misleading commercial practice is a criminal offence; the ASA has already banned air purifier advertising in the UK. A wrong claim costs far more than a strong claim earns.

This skill exists so that risk cannot be walked into by accident, while still producing content that ranks, reads natively and converts.

## Working modes

**Write / localise** - produce the copy applying everything here, then run the QA pass as a genuinely separate step before delivering.

**Audit / QA** - existing content supplied. Produce the defect report first (format below), then the corrected version if asked. Already-published content needs this treatment too, not just new drafts.

**Writer and reviewer must not be the same pass.** Do not draft copy and then certify it in the same breath. Run QA as a separate, later step with its own checklist, re-reading the finished copy from the top rather than relying on memory of what you wrote. When the same session both writes and reviews, say so in the report so a human reviewer knows a second pair of eyes is still needed. When reviewing localised copy, review the target language on its own terms without re-reading the English source first - seeing the source makes English sentence structure feel justified. Never sign off with a score ("9/10", "native quality"). Approval is defect-based.

## Where to look

| Need | File |
|---|---|
| Legal red lines per market, statutes, risk levels | `references/markets.md` |
| Formality, casing, typography, numbers, dates per locale | `references/locale-packs.md` |
| Before/after rewrites for unsafe claims | `references/claim-library.md` |
| Approved model specs, CADR, certifications, open conflicts | `references/products.md` |
| Full publishing checklist - SEO, structure, images, anti-AI | `references/qa-checklist.md` |
| Amazon title and bullet QA | `references/amazon.md` |

---

## 1. Brand voice

Coway sounds **calm, confident, clear, refined, helpful, evidence-based and premium without exaggeration.** Premium is not formal, ornate or verbose - it is precise, useful and restrained.

| Principle | Do | Avoid |
|---|---|---|
| Calm | Explain the situation and the product's role | Fear, urgency, "act now before it gets worse" |
| Confident | State verified performance clearly, qualify where needed | Hedging every sentence, or unsupported absolutes |
| Clear | Consumer language; explain technical terms when useful | Dense noun strings, jargon, English syntax in other languages |
| Refined | Concise, elegant, locally natural | Hype, all-caps, repeated superlatives, cheap promotional language |
| Helpful | Lead with the consumer's situation and practical action | Turning every paragraph into a pitch |
| Evidence-based | Preserve test conditions, limitations and scope | "helps reduce" drifting into "eliminates" or "protects" |
| Human | Vary sentence rhythm, remove filler | "In today's fast-paced world", robotic transitions |

No Gen Z slang, no trend phrases, no casual idioms. Emoji minimal to none in marketing copy and product pages - the ✅ clusters and Unicode bold (𝐀𝐢𝐫𝐦𝐞𝐠𝐚) used in some existing listings read as marketplace-cheap and break screen readers; flag them.

Content-type calibration: **Blog/SEO** editorial and useful, product relevance earned not inserted. **Product page** concise, benefit-led, evidence-based. **FAQ** direct and scannable. **Paid** short and persuasive but never stronger than the substantiation. **CRM** human and concise. **PR** restrained and publication-ready. **Amazon** marketplace-native and scan-friendly.

Brand pillars available as substance: end-to-end ownership (Coway designs, develops, manufactures and tests in-house), long-term value through low maintenance cost, and certified, trusted performance.

---

## 2. The core claim test: what is the sentence acting on?

Nearly every violation comes from the same grammatical move - the product is described as acting on a **person or an illness** instead of on the **air**.

Check the object of the verb:

| Object of the claim | Status |
|---|---|
| Air, dust, pollen, PM2.5, odours, smoke, VOCs, pet dander | Allowed, with evidence for numbers |
| A person's body, sleep, breathing, energy, recovery, immunity | Not allowed |
| A named condition - asthma, allergies, hay fever, infection, ADHD | Not allowed, every market |

*"Reduces airborne pollen in the room"* is fine. *"Helps hay fever sufferers breathe easier"* is not - it names a condition and acts on a person. *"ECARF-certified: reduces airborne allergens for easier breathing"*, which appears in current Coway copy, fails on the same test: report the certification and the particle capture, stop before the breathing.

Apply this to headings, meta descriptions, alt text, FAQ answers, bullet points and CTAs - not just body copy.

**Universal red lines, all markets:** no named illness linked to the product; no unsubstantiated numbers; no fear framing; no before/after imagery, patient or doctor testimonials. **Always allowed:** dust, odour and pollen reduction; certified test data with its source; verifiable specifications.

Statutes and per-market traps: `references/markets.md`.

---

## 3. Terminology guardrails - absolute

These are Coway's own controlled terms. Violations are CRITICAL regardless of how accurate the surrounding sentence is.

| Never write | Use instead | Why |
|---|---|---|
| True HEPA, GreenHEPA, Green HEPA | HEPA filter, HEPA air purifier, or HyperCaptive Filtration | Uncontrolled and unapprovable marketing terms |
| H13, H14, HEPA class | Nothing - remove the classification | Not approved for Coway EU copy |
| HEPA vs HEPA-type comparisons | Nothing - do not raise the comparison | Invites competitor challenge |
| Medical grade | Nothing | Coway makes no medical-certification statements |
| Cheap | Affordable, accessible, budget-friendly | Positioning |
| Extremely premium, ultra-premium | Higher mid-tier; good price for the expertise | Positioning |
| New York Times (alone, as the endorser) | NYT Wirecutter, New York Times Wirecutter, "#1 Pick for 12 years" | The endorsement is Wirecutter's |

**HEPA and HyperCaptive are not interchangeable.** HEPA describes the *filter media* - more than 99.97% of particles at 0.3 micron, single-filter performance. HyperCaptive Filtration describes *Coway's complete filtration system* - 99.999% of particles down to 0.01 micron, product-level performance. So the 99.999% / 0.01 µm figure belongs to HyperCaptive Filtration, never to "HEPA filtration". Existing copy that reads "HEPA Filtration: 99.999% ... down to 0.01 µm" is attributing system performance to the media, and needs correcting.

**Viruses and bacteria: state the particle size, never name the pathogen.** 0.01 micron is smaller than a virus or a bacterium, so the capability is *implied* by the specification and does not need to be said. Copy such as "HyperCaptive filter removes fine dust, allergens, mould, and viruses" turns an implication into a disease claim - the highest-risk category in all four markets and explicitly hazardous under HWG in Germany. Remove the pathogen noun; keep the micron figure. This internal rule is stricter than the law in every market and overrides it: even a lab-substantiated virus or bacteria percentage is not published.

---

## 4. Numbers, certifications and substantiation

Coway's claims are backed by test reports, so the number itself is usually fine. What fails is a number floating free of its origin, or a number that has drifted from the source.

A compliant efficacy figure carries **what was measured, the method or standard, who tested it, and the conditions**, then a variance line where performance depends on the room:

> The HyperCaptive Filtration System removes 99.999% of airborne particles down to 0.01 µm (tested by [lab], report no. [ref], model [X]). Laboratory results; performance at home varies with room size, ventilation and use.

Coverage and speed claims carry their test basis too - "cleans a 25 m² room in 30 minutes (based on a 2.4 m ceiling height)" is the pattern already used correctly for the Airmega 50 and should be applied consistently.

When the source is not in front of you, **do not guess and do not quietly drop the claim.** Keep the line and mark it `[SUBSTANTIATION NEEDED: lab, report no., model, test conditions]`, then list every marked claim in the report. Inventing a lab name, a report number or a statistic would be far worse than a missing claim.

**Two kinds of claim, two kinds of evidence.**

- **Coway's own tested and published claims** (HyperCaptive 99.999% / 0.01 µm, CADR, coverage, noise, filter life, certifications, Wirecutter, IndyBest and other figures listed in `references/products.md` or in Coway's published test documentation): these are substantiated by Coway's own tests. Do not run a web search for them and do not mark them. Check only that the wording and figure match the approved source exactly and keep their test conditions. A Coway product figure that is *not* in the approved source is still marked with the substantiation tag and raised with the Coway team, never searched for on the web, because no external source can prove a Coway product result.
- **External claims** (third-party statistics, health or pollution data, market figures, anything attributed to a body other than Coway): a verifiable source is mandatory. Use web search to locate genuine published data for each one, and never fabricate or suggest placeholder citations. Follow this priority order strictly:

| Priority | Source tier | Examples |
|---|---|---|
| 1: Local (match content language) | **en-GB**: UK government agencies, UK research bodies, charity/NHS data | DEFRA, UKHSA, NHS, Met Office, BESA, BRE |
| | **de-DE**: German agencies and recognised institutes | UBA (Umweltbundesamt), RKI, Fraunhofer, DWD |
| | **nl-NL**: Dutch government and research | RIVM, GGD, TNO, Longfonds |
| | **fr-FR**: French agencies and institutes | ANSES, INERIS, Santé publique France, ADEME, CSTB |
| 2: EU level | EU institutions and pan-European bodies | EEA (European Environment Agency), CEN standards, JRC |
| 3: US / Global | International bodies or US agencies, only when no local/EU source exists | WHO, IARC, EPA, ASHRAE, ISO, peer-reviewed journals (PubMed, Lancet) |

Source cautions: **Allergy UK** certifies Coway products (BAF Seal of Approval), so it is not an independent source for context statistics; cite it only for what the certification says. **Asthma + Lung UK** and **Longfonds** frame data around named conditions; use them only for neutral context such as pollen-season timing, never next to a product claim. **ECDC** and **IARC** are disease and cancer bodies; use them only when no air-quality source exists and never in a paragraph that mentions the product, because they pull copy toward disease and fear framing. UKHSA replaced Public Health England (PHE) in 2021; do not cite PHE as a current body.

When a real source is found: present the source name, URL, publication date and the specific figure or finding. Do not paraphrase in a way that changes the scope or strength of the original. If no credible source can be found for the claim at any tier, say so explicitly and recommend removing or rewording the claim rather than weakening substantiation silently.

**Certifications state what they certify, nothing further.** ECARF and BAF/Allergy UK certify allergy-friendliness and particle capture - they do not certify relief, easier breathing or symptom improvement. "Dual-certified allergy relief" overclaims a real certification into a health claim. Write "ECARF and BAF certified; helps reduce airborne allergens such as pollen, dust and pet dander."

**Never strengthen a claim during localisation.** Helps reduce must not become eliminates; supports cleaner air must not become protects your health; tested under stated conditions must not become always achieves this. Full drift table in `references/claim-library.md`.

Third-party statistics (WHO, ANSES, DEFRA, RIVM, Allergy UK) need a verifiable source, must not be used to frighten, and must not be arranged so the product appears to answer them. Keep statistic and product claim in separate paragraphs with no causal bridge - this is specifically how misleading practice is constructed in France.

---

## 4A. Source fidelity: never reinterpret research or reports

Report what a study, briefing or report actually says, at the strength it says it. Do not restate it in your own interpretation, do not upgrade "can" to "consistently", do not add a margin, ratio or frequency the source does not give, and do not attribute a figure to a body that did not set it. If you cannot open and read the source passage, do not attribute the claim to it. A misquoted real source is a CRITICAL defect, because it looks verified while being false.

**Rules**

1. **Keep the source's modal verb and frequency.** *can / may / often / in some cases* stay exactly that. Never upgrade to *consistently, always, typically, confirms, proves*.
2. **No borrowed numbers.** A margin ("2–5×", "a comparable margin") stays out unless that exact figure is in that exact source.
3. **Attribute to the body that set the figure.** 4.8 air changes per hour is AHAM's sizing basis, not the US EPA's. If unsure who set a number, do not name a body.
4. **The reference must match the topic.** Before citing, check the document is about what you are citing it for (HSE HSG258 is a guide to local exhaust ventilation, not an indoor air quality or ozone source).
5. **Every attribution needs a specific, current document.** "SAGE says…" with no paper is removed. COVID-era guidance is not used as general indoor air advice.
6. **Do not cite frameworks Coway UK products do not carry as buying criteria.** AHAM Verifide is a US scheme; Coway UK CADR figures are tested under SPS-KACA. Recommending a mark Coway does not hold works against Coway.
7. **Do not cast doubt on Coway's own figures.** Never imply room-size or coverage claims are unreliable or "harder to verify". Explain how to read them instead.
8. **Sizing must be use-based and consistent with Coway coverage.** Never present one ACH target as the universal minimum (at 4.8 ACH the Airmega 50 would cover about 10 m², against Coway's "up to 31 m²"). Use: everyday dust 2–3 air changes an hour; allergens or smoke 4–5, "in line with AHAM sizing guidance". Room coverage and cleaning-speed claims are different claims; never merge them (Airmega 50: coverage up to 31 m²; 25 m² in 30 minutes at 2.4 m ceiling).
9. **Only describe product categories Coway sells.** Coway does not sell desk, USB or mini purifiers. Frame small-space content as compact purifiers for bedrooms and home offices (Airmega 50 / 100) versus room units. No USB, desk-surface or £40 price references.
10. **Placement advice comes from the manual.** Clearance from walls and electronic appliances (TV, monitors) follows the specific model's manual; check it, or omit the distance. Never invent "within one metre of your seated position" style rules.
11. **No patronising framing.** Cut "most people are unaware", "the question most articles avoid", "the most common purchasing mistake". State the fact.

**Before / after from past Coway articles**

| Wrong | Problem | Fix |
|---|---|---|
| "If a desk model claims 30 m² coverage but lists a CADR of 60 m³/h, those numbers do not align… coverage without a CADR is harder to verify." | Casts doubt on Coway room-size figures | "Room size figures show the maximum space a purifier covers. To check a model for your use, divide its CADR by your room volume: around 2–3 air changes an hour suits everyday dust, 4–5 suits allergens or smoke." |
| "The US EPA recommends at least 4.8 air changes per hour…"; table "per EPA methodology" | Misattributed (AHAM, not EPA); single target conflicts with Coway coverage | Two-column table: everyday dust (2–3 ACH) and allergens or smoke (4–5 ACH, in line with AHAM sizing guidance). Remove "EPA" from every 4.8 reference |
| "Two certifications carry the most weight for UK buyers: AHAM Verifide… Quiet Mark" | Tells buyers to look for a mark Coway UK does not carry | "Look for independent certifications such as Quiet Mark (noise) and ECARF or Allergy UK (allergen capture), and check they apply to the specific model." |
| "Look for certified HEPA-grade filtration, not 'HEPA-style', 'HEPA-type'… UK consumer testing has identified models…" | HEPA vs HEPA-type comparison (§3) plus unsourced claim about other products | "Look for HEPA filtration with a published test basis (particle size, efficiency and where it was tested)." |
| "POST data confirms indoor particle concentrations in UK buildings are consistently higher than outdoor levels" | POST PB54 says *can exceed* | "…indoor particle concentrations in UK buildings can exceed outdoor levels…" |
| "DEFRA's Indoor Air Quality Report (2022) confirms indoor VOC concentrations frequently exceed outdoor levels by a comparable margin" | AQEG 2022 gives no margin | "…confirms that indoor VOC concentrations in UK buildings often exceed outdoor levels." |
| HSE "Workplace Health: Indoor Air Quality" (HSG258) cited for ozone | HSG258 is about LEV, does not support the statement | Find the actual HSE ozone source, or remove the HSE attribution |
| SAGE: "airborne particle transmission… is a ventilation and air quality issue" | No reference; COVID-era | Cite the specific SAGE paper or remove the attribution |
| "There are several pollution sources in a typical office, and most workers are unaware of them." | Patronising | "A typical office has several pollution sources." |
| "This is the question most articles avoid answering clearly… Choosing the wrong one is the most common purchasing mistake." | Patronising, unsourced | "A compact purifier and a larger room purifier are designed for different jobs." |

**Reference cross-check (mandatory for every external citation):** for each reference, confirm (a) the document exists, (b) it is about the topic cited, (c) the exact sentence's strength and numbers appear in it, (d) the body named is the one that published it. Report each reference as Supported / Overstated (give the corrected wording) / Wrong source (find the right one or remove).

---

## 5. Localisation

Every task needs a stated **target locale** (en-GB, de-DE, nl-NL or fr-FR; Coway Europe has no other markets at present, so treat any other locale as out of scope and flag it), content type, audience, formality rule and locked facts. If a field is unknown, mark it TBC rather than inferring it.

Localise, never translate literally. Restructure sentences freely so the text reads as though the English never existed - but keep every fact, number, specification, certification and claim exactly as approved. Where natural phrasing and claim strength conflict, preserve claim strength and escalate rather than making the promise stronger.

Formality is a locked field, not a stylistic choice: **de-DE Sie** (never du), **fr-FR vous**, **nl-NL je** per the brand TOV - though Coway's support/FAQ reference material uses *u*, so flag any nl-NL asset where the two could collide and never mix them within one asset.

Typography is a credibility signal, not a detail: sentence case headings everywhere (with normal German noun capitalisation), decimal comma in DE/NL/FR, PM2,5 rather than PM2.5 in those locales, French guillemets and non-breaking spaces before ; : ? !, locale-correct thousand separators and dates. Full matrix in `references/locale-packs.md`.

A translated UK article inherits UK claim decisions that may not survive German law. Re-run the claim audit after any localisation.

---

## 6. Severity and the publishing gate

Use Coway's taxonomy so reports match the rest of the business:

| Severity | Definition | Examples |
|---|---|---|
| **CRITICAL** | Factual, legal, safety, product, price or material reputation risk | Disease or medical claim; forbidden terminology (True HEPA, H13, medical grade); named pathogen; unsupported or strengthened efficacy claim; wrong specification or certification; fear framing |
| **MAJOR** | A native reader notices unnatural language, wrong locale, off-brand tone, or AI writing pattern | Translationese, English Title Case, wrong formality, repeated AI vocabulary (3+ ban-list words in one asset, or the same word twice), structural AI patterns (significance padding, superficial -ing analysis, negative parallelism, vague attribution, formula closings), hype, US units or spelling in en-GB, keyword stuffing |
| **MINOR** | Publishable, but could be more elegant or consistent | Rhythm, optional synonym, editorial preference, an isolated ban-list word, one surplus em dash, an isolated copula substitution |

**Publish only when CRITICAL = 0 and MAJOR = 0**, with zero unsupported or strengthened claims, zero changed numbers or certifications, zero terminology violations and zero locale/formality errors. Minor defects may remain only where they do not reduce perceived brand quality.

For every issue, quote the exact problem phrase, explain in English why a native reader or a regulator would object, classify severity, and propose a specific replacement. A single overall score can hide one serious defect, so never give one.

---

## 7. AI writing footprint: detection and removal

Every piece of Coway content must read as written by a skilled human editor, not assembled by a language model. AI-generated text has identifiable patterns that undermine brand credibility and can be detected by readers, journalists and regulators alike. Flag every item below, rewrite it and verify the rewrite before delivery. Severity: structural patterns (§7.2) and chatbot residue are **MAJOR**. Isolated lexical items (one ban-list word, one copula substitution, one surplus em dash) are **MINOR**, and become **MAJOR** when they recur (three or more ban-list words in one asset, the same word twice, or a pattern across several paragraphs). This keeps the gate on what readers actually notice.

**Run this check as a separate QA step, not while drafting.** A writer is blind to their own patterns, so re-read the finished copy from the top against §7.5. If the same session wrote and reviewed it, say so in the report.

### 7.1 Banned vocabulary

These words appear at abnormally high frequency in AI output and signal machine origin to experienced readers. Remove every instance; do not replace one with another from the same list.

**Hard ban (any use flags MAJOR):** additionally *(sentence-opener)*, align with, bolstered, crucial, deep dive, delve, emphasising/emphasizing, enduring, enhance/enhances, fostering, garner, highlight *(as a verb)*, interplay, intricate/intricacies, landscape *(abstract noun)*, meticulous/meticulously, pivotal, robust, showcase/showcasing, tapestry *(abstract noun)*, testament, underscore *(as a verb)*, valuable, vibrant

**Also watch for Grok-specific over-use:** causal, empirical, correlate. Flag them if these appear where plain language would serve.

If a synonym from the same list is used as a substitution, flag both. The goal is plain, specific language, not synonym rotation.

### 7.2 Structural AI patterns

**Significance padding.** Remove any sentence whose sole function is to assert that the subject matters, contributes to a broader trend, or marks a turning point. Examples of what to cut: *"marking a pivotal moment in the evolution of…"*, *"represents a significant shift toward…"*, *"setting the stage for…"*, *"contributing to a growing movement…"*, *"indelible mark on the landscape of…"*

**Superficial -ing analysis.** Remove participial phrases appended to facts to imply significance without evidence: *"…underscoring the brand's commitment to…"*, *"…highlighting its enduring appeal…"*, *"…reflecting broader consumer trends…"*, *"…fostering community development…"*. If the analysis cannot be stated as a plain fact with a source, cut it.

**Negative parallelism.** Rewrite constructions that frame copy as correcting a misconception: *"Not just an air purifier, but a lifestyle statement"*, *"It's not merely about clean air, it's about peace of mind"*, *"No compromise, no complexity, just clean air"*. State the benefit directly.

**Rule-of-three filler.** Adjective triads and three-item phrase lists used to pad claims rather than convey distinct information must be collapsed or cut: *"clean, quiet, and beautifully designed"* repeated across paragraphs signals AI generation. Each element in a list must carry independent meaning not covered by the others.

**Copula avoidance.** Rewrite *serves as*, *stands as*, *functions as*, *operates as*, *marks*, *represents* when a plain *is* would be correct. Also rewrite *boasts* used as a marketing substitute for *has*. *Features* and *offers* are normal in product pages and Amazon listings and are acceptable there; rewrite them only in blog and editorial copy where a plain *has* reads better. Exception: do not alter these constructions in approved legal or technical copy where they carry precise meaning.

**"Challenges and Future Outlook" formula.** Do not close a section or article with a paragraph that begins *"Despite its strengths, [subject] faces challenges…"* followed by vague optimism. If challenges are genuinely relevant and sourced, integrate them as facts at the point where they are relevant, not as a structural convention at the end.

**Vague attribution.** Every claim attributed to *experts*, *industry observers*, *several publications*, or *leading analysts* must be replaced with a named, verifiable source. If no named source exists, remove the claim.

**Canned notability signals.** Remove sentences that exist solely to assert coverage or recognition: *"The product has been featured in multiple independent outlets"*, *"Coway maintains an active social media presence"*, *"recognised by trade publications and regional media"*. These read as AI attempting to prove relevance and add no consumer value.

### 7.3 Sentence rhythm and register

AI text produces paragraphs with uniform sentence length (every sentence about the same length, even inside the 15-25 word target), parallel grammatical structure, and smooth, predictable transitions. Human editing should introduce:

- At least one short sentence (under ten words) per three paragraphs.
- Varied sentence openers, not every sentence beginning with *The* or *This*.
- Concrete nouns in place of abstract ones wherever possible: *pollen* not *airborne allergens*; *the AP300C* not *the device*. A category noun followed by concrete examples is allowed and preferred where a certification or approved claim uses the category: *airborne allergens such as pollen, dust and pet dander*.
- Transitions earned by logic, not filler: remove *Additionally*, *Furthermore*, *Moreover*, *Notably* at sentence openings unless the logical relationship they imply is explicit.

### 7.4 Tone mismatches to flag

**Travel-guide / press-release register.** Flag and rewrite: *nestled in the heart of*, *vibrant*, *rich heritage*, *breathtaking*, *seamlessly connects*, *natural beauty*, *diverse array*, *state-of-the-art*, *groundbreaking*, *renowned*.

**Em dashes.** Avoid them. Use a comma, colon, full stop or brackets instead; these are almost always the better choice. One em dash per paragraph is the absolute ceiling, kept only for genuine parenthetical emphasis that nothing else expresses. Two or more in a paragraph, or a pattern that mimics punchy sales writing, must be rewritten.

**Over-hedging stacks.** *"may potentially help to contribute to"* collapses to *"can help"* or, with a source, a direct claim. Stack hedges only when genuine uncertainty in the evidence requires it.

**Chatbot preamble residue.** Remove any sentence that addresses the reader as if continuing a chatbot session: *"I hope this helps"*, *"Of course!"*, *"Here is a comprehensive overview"*, *"Would you like me to expand on any section?"*, *"Let me know if you need a more detailed breakdown"*.

### 7.5 AI footprint check: quick reference

Before delivery, confirm that **none** of the following appear in the copy:

- Any word from the §7.1 hard-ban list
- A sentence whose only function is to assert significance, legacy, or trend relevance
- A participial phrase appended to a fact to imply analysis (*"…highlighting…"*, *"…underscoring…"*, *"…reflecting…"*)
- A *"not just X, but also Y"* or *"no X, no Y, just Z"* construction
- A formulaic "Challenges / Future Outlook" closing
- Attribution to unnamed experts, observers, or publications
- *Serves as / stands as / functions as* replacing a plain *is*
- Uniform sentence rhythm across three or more consecutive paragraphs
- Travel-guide adjectives (*vibrant*, *nestled*, *breathtaking*, *seamlessly*)
- Em dashes that a comma, colon or full stop could replace; never more than one per paragraph
- Any chatbot session phrasing

---

## Audit output format

Lead with the verdict - a busy reviewer needs the answer in one line.

```
## Verdict
PASS | REVISE  (Critical: N · Major: N · Minor: N)
Locale(s) assessed: [en-GB / de-DE / nl-NL / fr-FR]   Content type: [blog / PDP / listing]

## Defects
| # | Location | Problem phrase | Issue & why | Severity | Recommended revision |

## Substantiation needed
Coway product claims (not searched; request from the Coway team):
- [claim]: required: lab, report no., model, test conditions

External claims (search mandatory):
- [claim]: required: verifiable source
  → Search result: [real source found: name, URL, date, specific finding] OR [no credible source found at local / EU / global tier; recommend removing or rewording]

Source priority when searching external claims: (1) local country source matching content locale, (2) EU-level body, (3) US or global body. Never suggest a source without first verifying it exists. Coway's own tested and published claims that match the approved source are not listed here.

## AI footprint
Ban-list words found: [list]. Structural patterns: [significance padding / parallelism / copula avoidance / other]. Rhythm: [uniform / varied]. Recommended rewrite scope: [sentence / paragraph / section].

## Editorial & localisation notes
Tone, typography, structure, recommended length reduction (%)

## Summary
2-3 sentences: what works, what must change before publication.
```

Quote problem phrases short - enough to locate the line, not a reproduction of the article. When one text serves several markets, assess against the strictest applicable standard (in practice Germany) and note any line that could safely be reinstated locally.

---

## Pre-delivery checklist

Condensed; the full version including SEO, structure and image rules is in `references/qa-checklist.md`.

- [ ] Every claim's object is the air or a pollutant - never a person, symptom or condition
- [ ] No named illness anywhere, including headings, FAQs, meta and alt text
- [ ] No named pathogen - particle size only
- [ ] No True HEPA, GreenHEPA, H13/H14, medical grade, HEPA-type comparison, "cheap", or bare "New York Times"
- [ ] 99.999% / 0.01 µm attributed to HyperCaptive Filtration, not to HEPA
- [ ] Every number carries method, source and conditions, or is marked `[SUBSTANTIATION NEEDED: lab, report no., model, test conditions]`; Coway's own tested and published figures match the approved source exactly; every external claim has a real source found by search in locale-priority order (local country → EU → US/Global), with findings reported; no placeholder or fabricated citations
- [ ] Specs match `references/products.md`; no fabricated labs, figures or certifications
- [ ] Certifications claim only what they certify - no "relief", no "easier breathing"
- [ ] No claim strengthened relative to the approved source
- [ ] No fear framing, before/after imagery, or patient/doctor testimonials
- [ ] Third-party statistics sourced and not causally bridged to product efficacy
- [ ] Placement and sizing advice attributed to the manual or hedged, not stated as universal law
- [ ] Every research/report claim keeps the source's exact strength (can ≠ consistently), contains no margin or figure the source does not give, and names the body that actually set it (4.8 ACH = AHAM, not EPA)
- [ ] Every reference cross-checked: exists, on-topic, supports the exact wording; otherwise corrected or removed (§4A)
- [ ] Nothing casts doubt on Coway coverage or CADR figures; sizing uses 2–3 ACH (dust) / 4–5 ACH (allergens, smoke); coverage and cleaning speed kept separate
- [ ] No AHAM Verifide or other mark Coway UK does not carry presented as a buying criterion
- [ ] No desk, USB or mini purifier category; no patronising "most people don't know" framing
- [ ] Correct locale formality, sentence case, typography, decimals, dates, units
- [ ] No word from the §7.1 AI vocabulary ban list (additionally sentence-opener, bolstered, crucial, delve, enhance, fostering, garner, highlight-verb, intricate, landscape-abstract, meticulous, pivotal, robust, showcase, tapestry-abstract, testament, underscore-verb, vibrant…)
- [ ] No significance-padding sentence (pivotal moment, evolving landscape, setting the stage for, indelible mark…)
- [ ] No superficial -ing analysis appended to facts (underscoring, highlighting, reflecting, fostering…)
- [ ] No negative parallelism (not just X but also Y; no X, no Y, just Z)
- [ ] No rule-of-three filler triads
- [ ] No copula avoidance (serves as / stands as replacing is; boasts replacing has; features / offers acceptable in PDP and Amazon)
- [ ] No "Challenges and Future Outlook" formula closing
- [ ] No vague attribution (experts say, observers note, several publications report)
- [ ] No travel-guide or press-release adjectives (vibrant, nestled, breathtaking, seamlessly, renowned, diverse array)
- [ ] Em dashes avoided (commas, colons or full stops instead; never more than one per paragraph)
- [ ] No chatbot preamble residue (I hope this helps, Here is a comprehensive…, Would you like me to…)
- [ ] Sentence rhythm varied: at least one short sentence per three paragraphs; mixed openers
- [ ] Conversion runs through room fit, noise and specification - not wellbeing promises
- [ ] QA run as a separate step after drafting; if the same session wrote and reviewed, this is stated in the report; no self-certifying score
