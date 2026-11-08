# Verification Reference

Read this before Step 3 of any TMF collection job.

Contents:
1. Product Fact Sheet - full spec and worked example
2. The twelve banned patterns, with the real error each prevents
3. Framework Feasibility Check
4. Full Gate 3 checklist

---

## 1. Product Fact Sheet

Build before the outline. One row per product you intend to name. Populate only from Tier A (live TMF listing) and Tier B (manufacturer or authorised distributor). **Leave cells blank rather than guessing.** A blank cell is not a gap to fill with plausible copy; it is a prompt to either verify or omit the claim.

### Fields

| Field | Source | Why it exists |
|---|---|---|
| Handle | URL | For the link and for the JSON pull |
| Exact live title | Product page | Titles carry conditions writers drop: "(Min. 2 Cases)", "- 8 lb Jar", "*Updated 2024 Model*" |
| Price + every variant | `/products/<handle>.json` | Variant-level pricing and sizes |
| **Availability per variant** | `.json` | Three sold-out products shipped as available last time, one as the hero product at $2,495 |
| Fulfilment note | Listing | "1-2 Weeks to Fulfill" is the honest stock language to reuse |
| Star rating + review count | Live page (Okendo) | The last batch got this right. Keep the record |
| **Category, one word** | Listing | Hand tool vs wand. Booster vs prespray. Counteractant vs fragrance. Wand vs rotary machine. Four separate errors came from this cell |
| **Mechanism, quoted verbatim** | Listing | Peroxide, enzyme, encapsulating, counteractant, optical concealment. Never infer from the product's job |
| Stated surfaces / fibres | Listing | Do not extend. "Wood finishes, raw wood, VCT" does not become "stone, concrete, LVP" |
| Hard specs | Listing, then manufacturer | RPM, HP, PSI, head width, weight, runtime, tank capacity, pH, unit size, dilution rate |
| **Pressure requirement vs pressure rating** | Listing + manufacturer | Opposite numbers. One tool needs 1,000+ PSI minimum; another has a 500 PSI valve ceiling. Grouping them as "both high-pressure" could damage a customer's equipment |
| Power source | Listing | A $4,400 machine's battery runtime is the buying decision. One page never mentioned it |
| Contradiction flag | Listing | Anything on the listing that fights the page's thesis. Example: a bestseller whose copy warns about "powder rinses that clog your jet lines" on a page selling four powders |
| Notes / omissions | - | Temperature ceilings, dilution rates, minimum order conditions, free-shipping thresholds |

### Blank-cell rule

- Mechanism blank -> the page may not describe that product's chemistry.
- Hard spec blank -> the page may not build a buying framework on that spec.
- Pressure cells blank -> the page may not group that product with others by pressure.

### Pulling the data

Shopify exposes structured product data without scraping:

```
https://shop.truckmountforums.com/products/<handle>.json    # title, variants, price, available
https://shop.truckmountforums.com/collections/<handle>/products.json?limit=250   # membership
```

Ratings and review counts come from the Okendo metafield on the rendered product page - the same figure a shopper sees. The project file `TMF_product_full.txt` (URL + title + description for the catalogue) covers the mechanism and category cells for most products, but it does **not** carry price, stock, variants or reviews. Those must come from the live JSON on the day of delivery.

### Worked example

```
Handle:            drimaster-dm3-hiflo-upholstery-tool
Title:             DRIMASTER DM3 HiFlo Upholstery Tool
Price:             $725.00, in stock
Rating:            5.0 / 3 reviews
Category:          upholstery hand tool (NOT a wand, NOT an extraction wand)
Mechanism (quote): "HI-FLOW HYPER-VELOCITY JETLESS CLEANING TECHNOLOGY" -
                   constant solution flow through a patented injector bar,
                   slotted vacuum port, shearing across fabric with immediate recovery
Surfaces:          upholstery fabric
Hard specs:        head width 4 in. (manufacturer: HydraMaster)
Pressure:          [blank - not published]
Contradiction:     none
Notes:             manufacturer is HydraMaster, not a brand called "DRIMASTER"
```

Written from the title alone, this product was described as having "a unique air-injection design that accelerates drying time by introducing ambient air into the extraction path", repeated three times and given its own FAQ. There is no air injection and no spray jet. The Fact Sheet's mechanism cell makes that error impossible, and the real mechanism is stronger copy anyway: no jet to clog, no heat loss from atomising.

---

## 2. The twelve banned patterns

**1. Do not name a mechanism the listing does not name.**
Banned unless the words appear on the listing or an SDS: "peroxide-powered", "encapsulating polymer technology", "terpene and resin", "enzyme chemistry", "pH-buffered", "oxidizer chemistry", "cleans without stripping natural oils".
*Prevented errors:* USOR Unchained called enzyme when TMF sells it as peroxide plus EcoCide, on a 704-review bestseller. Formula 99 given polymer technology when the listing says "dries to a crystal" and a sibling product advertises "no polymers" as a benefit. Rob's Reefer Rid given terpene chemistry when the listing claims a bond-absorb-neutralise process. A leather cleaner whose entire listing is one sentence given two invented attributes.

**2. Do not upgrade legal or technical status.**
"Patent pending" stays "patent pending". Do not promote a claim to "patented", "certified", "clinically proven" or "rated for" without a source.

**3. Do not extend a surface or fibre list.**
*Prevented error:* a machine scoped by its listing to "various wood finishes, raw wood, and VCT surfaces" was described as working on wood, stone, concrete and LVP, plus post-construction cleanup.

**4. Do not describe a product from its name.**
*Prevented errors:* "Hide-A-Hose" at TMF means running the solution hose inside the vacuum hose; a whole paragraph was built around a retractable central-vacuum reel that does not exist in this catalogue. The "Hoser" was described as cleaning hose interiors; it washes the outside. The Converter Cuff's direction was stated backwards.

**5. Do not present a rating without its count when the count is 1-3.**
*Prevented error:* "Rated 5.0 stars by professionals" and "five-star rated" on two products with one review each. Technically true, materially misleading, and the kind of thing an FTC-minded reviewer flags.

**6. No absolutes about reviews.**
*Prevented error:* "Every spotter here carries verified reviews from pros on the job" on a page linking three products with zero reviews.

**7. Do not state a saving that arithmetic can falsify.**
*Prevented error:* "significant cost savings per gallon mixed" on a pail where the likeliest comparison gives an identical $6.81 per pound either way. Publish real cost-per-gallon-mixed figures or drop the claim.

**8. Do not invent production or volume statistics.**
*Prevented errors:* "20-40 pieces of furniture in a single day", "three to five times larger than the visible stain", "most portables produce between 80 and 120 CFM under load". All unsourced. Attribute to a named operator on the record or cut.

**9. Do not contradict another page in the batch.**
*Prevented error:* fresh urine described as "relatively neutral" on one page and "mildly acidic" on another. Also watch the community-size claim: "thousands of professionals" on one page escalated to "over 50,000" on another.

**10. Do not skip a safety qualification.**
*Prevented error:* a $1,999 ozone generator recommended with no occupancy warning. Ozone is a respiratory irritant, must be used in unoccupied spaces with a clearance period before reoccupancy, and the EPA is explicit about this. Adding the warning strengthens the page's authority rather than weakening the sale.

**11. Do not recommend a product your own page just argued against.**
*Prevented error:* an encapsulation cleaner recommended as the default for hot water extraction on uncertain fibres, two sections after the page explained that wet-extracting an encap formula flushes out the polymer before it can set.

**12. Do not present a sold-out product as available.**
See the stock disclosure rules in SKILL.md. The Carpet Cleaning Detergent page is the template: it disclosed "Currently sold out" accurately and was the only page in the batch to do so.

### Two more habits worth naming

**Mechanism vs effect.** Explaining *why* something works is where the audit found the most invented content. If you cannot name the mechanism from a source, describe the effect the listing claims and stop there.

**Correct chemistry categories.** Oxidising and reducing are opposite reactions and cannot share a bucket; professional red dye removers are overwhelmingly heat-activated reducing agents. Ammonia in aged urine comes from bacterial urea hydrolysis, not oxidation. Synthetic fibres (nylon, polyester, olefin) have no cuticle, so an acid rinse does not "close the cuticle" on them - it neutralises residual alkalinity and returns the fibre to a slightly acidic state. Each of these was published as fact.

---

## 3. Framework Feasibility Check

Run before asking for outline approval. For each buying framework in the outline:

- [ ] Sort the Fact Sheet by that spec. Do the products actually spread across the range?
- [ ] Can a reader execute the framework using only what this collection sells?
- [ ] Does the framework's top recommendation point at a product TMF stocks?

Any "no": change the axis to one the inventory does differentiate on, or drop the section.

*Prevented errors:* a "wide wand vs narrow detail tool" axis where all four featured tools were 4-inch heads. An RPM table setting 175-300 RPM as the safe band on a page where every machine runs at a fixed 165 RPM. A pH selection framework where none of the eight products publishes a pH. An "enzymes are the first call" recommendation in a collection with no enzyme product, while TMF's actual enzyme prespray sat in a different collection, unlinked.

---

## 4. Full Gate 3 checklist

Attach the completed version to every delivery.

### Structure
- [ ] Meta Title present, under 60 chars, primary keyword at the start, brand token kept.
- [ ] Meta Description present, under 155 chars, primary keyword once, soft CTA, no phone number.
- [ ] Meta Title does not drop a valuable term the live collection title already carries.
- [ ] No H1 in the body. Bottom order: Why Buy -> FAQ -> Related Blogs -> META.
- [ ] Target collection resolves; no other page in the batch targets the same URL or term.
- [ ] Collection title contains the primary keyword, or the gap is flagged to the user.

### Products
- [ ] Every named product exists with the exact live title, including conditions like "(Min. 2 Cases)".
- [ ] Every price matches the live page today.
- [ ] Every star rating and review count matches the live Okendo figure today.
- [ ] Every variant's availability checked; every sold-out item disclosed in the listing's own fulfilment language.
- [ ] No sold-out product used as the hero.
- [ ] Every mechanism, category, surface and spec claim traces to a Fact Sheet cell.
- [ ] No rating claim rests on fewer than 4 reviews without the count stated.
- [ ] Products named only in the Shop by category / featured section.

### Links
- [ ] Every URL returns 200 and comes from the supplied list. None invented, none self-linking.
- [ ] Every linked collection was opened and counted, and its contents match the description given.
- [ ] Every section arguing for a product type links at least one product of that type.
- [ ] Collection coverage target met, and no unlinked product answers a question the page's own FAQ raises.
- [ ] Every related blog is whitelist-passing with a measured word count, and every blurb matches the actual body text.

### Claims
- [ ] Zero `[?]` markers remain.
- [ ] Business facts match `tmf-brand-facts.md` verbatim.
- [ ] Every numeric claim sourced or removed.
- [ ] Safety qualifications present where relevant.
- [ ] No claim contradicts another page in the batch, the target collection, or any linked product listing.
- [ ] No banned dash anywhere.
- [ ] Commercial offers verified and mentioned no more than 3 times.

### Read-through
- [ ] One editor reads end to end asking: would a working technician who owns these products spot anything wrong?
- [ ] Proofread pass for garbled sentences.
- [ ] `scripts/qa_check.py` run and passing.
