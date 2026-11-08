# Locale packs

Typography, formality and vocabulary are credibility signals for a premium brand. A German noun in lower case or an English Title Case heading in French tells a native reader immediately that the copy was translated, and that costs more trust than a clumsy sentence does.

Coway Europe currently operates in four markets only: en-GB, de-DE, nl-NL and fr-FR. Any other locale is out of scope; flag it rather than localising.

Every task states its exact locale. "German" is not a locale; de-DE is. nl-NL and nl-BE are separate.

## Contents
- [Baseline matrix](#baseline-matrix)
- [en-GB in detail](#en-gb-in-detail)
- [de-DE](#de-de)
- [nl-NL](#nl-nl)
- [fr-FR](#fr-fr)
- [Open decisions to escalate](#open-decisions-to-escalate)

---

## Baseline matrix

| Locale | Headings | Address | Decimal / grouping | PM notation | Date | Primary native risk |
|---|---|---|---|---|---|---|
| en-GB | Sentence case | you | 2.5 / 1,230.00 | PM2.5 | 10 August 2026 | US spelling & grammar, Title Case, hype, overlong copy |
| de-DE | Sentence case + normal noun capitalisation | **Sie**, never du | 2,5 / 1.230,00 | PM2,5 | 10. August 2026 | Noun capitalisation, compounds, word order, Sie/du mixing |
| nl-NL | Sentence case | **je** per brand TOV (see below) | 2,5 / 1.230,00 | PM2,5 | 10 augustus 2026 | Belgianisms, u/je mixing, English calques, over-formality |
| fr-FR | Sentence case | **vous** | 2,5 / space grouping (1 230,00) | PM2,5 | 10 août 2026 | Translationese, anglicisms, punctuation spacing, English casing |

Currency and price formatting should come from the platform's locale formatter wherever one exists. Do not hard-code English separators into e-commerce copy.

Model names, trademarks (HyperCaptive™, HyperVortex™, MegaJet), test standards and certification names stay unchanged in every locale. The grammar around them inflects naturally.

---

## en-GB in detail

The test: could this have run in a well-edited British consumer title? If it reads as US-origin SEO content that has been spell-checked, it fails, and it fails visibly for a premium brand.

### Spelling and vocabulary

Spelling: odour, colour, favour, behaviour, defence, licence (noun), practise (verb), litre, metre, fibre, optimise, minimise, analyse, travelling, ageing, grey, aluminium, deodorisation, ioniser.

| US | UK |
|---|---|
| nightstand | bedside table |
| apartment | flat |
| HVAC | central heating, ventilation, boiler - name the actual thing |
| closet | wardrobe, cupboard |
| drapes | curtains |
| faucet | tap |
| trash | rubbish, bin |
| fall | autumn |
| gotten | got |
| oftentimes | often |
| dryer | tumble dryer |
| crib | cot |
| yard | garden |
| stroller | pushchair |
| store | shop |
| sidewalk / curb | pavement / kerb |
| zip code | postcode |
| color-coded | colour-coded |

"Air purifier" is correct UK usage. Keep it.

### Units - metric first, imperial only in support

Coway's UK checklist asks for **both imperial and metric where relevant**, while the editorial requirement is that the copy must not read as American. Both are satisfied the same way:

- **Metric is always the primary figure.** Room size: `73 m² (about 785 sq ft)`. Never sq ft alone, never sq ft first.
- Imperial is worth adding only for **room and coverage size**, where UK buyers still shop in both. It adds nothing to airflow, noise, particle size or dimensions.
- **Never use feet or inches for placement, clearance or unit dimensions** - use cm and m. "A 3-foot clearance" is the exact phrasing the reviewer flagged as US-style.
- Airflow m³/h. Noise dB(A). Temperature °C. Particle size µm (write "micron" in body copy where it reads more naturally).
- Dates 10 August 2026 or 10/08/2026. Times 7am, 10.30pm. Currency £1,299.

### Headings and structure

Sentence case throughout - page titles, headings, labels. Capitalise only proper nouns and product names. One H1 per page; clean H1 → H2 → H3 hierarchy. Avoid question headings except in an FAQ block. A heading is a signpost, not a hook.

Sentences 15-25 words. Paragraphs 2-4 sentences. One idea per section - if two sections make the same point in different words, merge them. When revising a US-style SEO draft, a **35-45% cut** is typically what the padding amounts to.

### Voice

Second person, used sparingly. No exclamation marks in body copy. Hedge honestly where the evidence hedges - "can help reduce", "in most rooms", "depending on ventilation"; in this context hedging reads as credibility. Avoid dramatically, drastically, shockingly, alarmingly. Contractions are natural. Never address the reader as a sufferer, a patient, or someone at risk.

### UK context that carries no claim risk

Pollen season timing (tree late March to mid-May, grass mid-May to July, weed to September) - the *season*, never hay fever as a condition to treat. Met Office pollen forecasts and DEFRA air quality index as citable context. Older housing stock: single glazing, damp, condensation, limited mechanical ventilation. Urban roadside PM2.5. Windows shut through winter. Typical UK bedroom sizes in m² when discussing CADR. UK energy costs when discussing running cost. UK 3-pin plug and UK warranty registration are legitimate, checkable purchase factors.

---

## de-DE

Formal **Sie** by default; du requires an explicit documented decision. Keep possessive forms consistent with it.

Sentence case headings, but normal German capitalisation applies - every noun stays capitalised. A lower-case noun looks unprofessional immediately, and it is the single most common defect in AI-localised German.

German quotation marks („…“) per house style, not imported straight quotes. Decimal comma; grouping 1.230,00; PM2,5; dates 10. August 2026.

Prefer natural German compounds and verbs over English noun chains. Check verb placement and sentence length after restructuring from English - a correctly translated German sentence built on English word order still reads as translated. Avoid unnecessary English business vocabulary where an established German term exists.

Germany is also the strictest claim market; read `markets.md` before writing, not after.

---

## nl-NL

**Formality is an open conflict that needs locking.** The Coway brand TOV specifies informal **je** and says not to use *u*; the localisation guideline notes that current FAQ and support reference material commonly uses *u*. Default to **je** for blog, marketing and product copy per the brand TOV, treat *u* as possible only in support content where it is already documented, and never mix the two registers inside one asset. Flag the conflict rather than resolving it silently.

Sentence case; avoid English Title Case. Decimal comma; grouping 1.230,00; PM2,5; dates 10 augustus 2026; € before the number.

Check for Belgian Dutch vocabulary or register - nl-NL and nl-BE are separate locales. Avoid literal English collocations, especially in benefit statements and CTAs. Prefer everyday Netherlands Dutch to stiff administrative phrasing. Dutch readers and the RCC both read superlatives as sales talk, which happens to align with what the law allows.

---

## fr-FR

**Vous.** Sentence case - "Face aux feux de forêt", not "Face aux Feux de Forêt".

French guillemets « … » with protected internal spacing. Non-breaking space before ; : ? ! - use a real non-breaking space so punctuation cannot strand at a line break. Decimal comma; space grouping (1 230,00); PM2,5; dates 10 août 2026.

Write in the register of good French consumer or technology editorial - natural rhythm, no imitation of a named publication. Actively remove anglicisms, calques, pleonasms and English-style noun strings. Avoid *assainir*, and the verb *purifier* when attached to a person or health outcome; the category noun *purificateur d'air* is correct.

France is where a legally clean statistic followed by a legally clean product claim can together constitute a misleading practice. See `markets.md`.

---

## Open decisions to escalate

Flag these rather than inventing an answer:

1. **nl-NL formality** - brand TOV says je, support reference uses u. Needs a locked decision per channel.
2. **Quotation house style** per locale where more than one convention is valid.
3. Any locale-specific typography choice not yet confirmed by a market-native reviewer. Until it is confirmed, it is a candidate, not a rule.
