# Known Issues on shop.truckmountforums.com

Site-level traps that caused errors in the 2026 audit batch. Check this before Gate 1a and Gate 1c. Update it as you verify new things.

State as of 27 August 2026. Product counts and blog lengths change - re-verify anything you depend on.

---

## 1. Collection handle traps

| Handle | Live title | Contents |
|---|---|---|
| `/collections/wood-floor-cleaning` | "Professional Commercial Floor Cleaning Machine" | **6 floor machines, zero chemicals** |
| `/collections/wood-floors-cleaning` | "Professional Hardwood Floor Cleaner" | **3 wood chemicals** |

One letter apart, and the titles swap their apparent subjects. One audited page told readers the machine collection "has tools and chemicals matched to these surfaces specifically" - there are no chemicals in it.

Other near-duplicate handles in the site URL list that need the same care: `/collections/sprayers` vs `/collections/sprayerss` vs `/collections/sprayers-1`; `/collections/encapsulation-vlm` vs `/collections/encapsulation-vlm-1`; `/collections/sprayer-parts` vs `/collections/sprayer-parts-1`; `/collections/wood-floor-cleaning` vs `/collections/wood-floors-cleaning` vs `/collections/wood-floors-cleaning`; `/collections/new` vs `/collections/new-products` vs `/collections/new-arrivals` vs `/collections/newest-products`.

**Rule:** never type a collection handle from memory or infer it from a page title. Copy it from the supplied URL list and confirm it returns 200 with the expected products.

### Collections that do not exist

Every plausible hard-floor handle returns 404: `/collections/hard-floor-cleaner-machines`, `/collections/hard-surface-machines`, `/collections/hard-floor-machines`, `/collections/hard-surface-cleaning-equipment`. One audited page opened with "Four purpose-built tools make up this collection" for a collection that does not exist; its four products actually live in `/collections/tile-grout` and `/collections/wood-floor-cleaning`.

---

## 2. Keyword cannibalisation map

Resolve URL ownership with TMF **before** writing any page in these clusters.

| Contested term | Pages competing | Recommendation |
|---|---|---|
| Hard floor machines | "Hard floor cleaner machines" + "Wood floor cleaning" + `/collections/floor-machines` (21 products) + `/collections/wood-floors-cleaning` | **Severe.** Two agency pages share two products and one targets a collection that does not exist. Consolidate to one machine page and one wood-chemistry page |
| Pet odour | "Pet stain and odor removal" + "Carpet cleaner deodorizer" | **Real.** Both target pet urine odour, both discuss UV mapping, both feature TMF Fresh Blocks, both link Odor Control, and the deodoriser collection's live title already contains "Pet Odor Remover". Split: deodoriser owns odour chemistry and scent; pet page owns urine stain removal and protocol |
| Carpet cleaner (generic) | "Carpet and upholstery cleaner" + `/collections/carpet-cleaning-chemicals` (115) + `/collections/carpet-prespray` (18) | **Real and self-inflicted.** The term promises a dual-surface product; the collection holds eight upholstery-only chemicals. Retarget to "upholstery cleaning chemicals" or build a genuine dual-surface page |
| Stain removal | "Carpet spotting chemicals" + "Pet stain and odor removal" | **Moderate.** Keep spotting on non-biological spills and dye chemistry; push urine, faeces and odour language to the pet page |
| Upholstery | "Upholstery cleaning tools" + "Carpet and upholstery cleaner" | **Mild.** Tools page owns hardware intent; chemicals page owns formula and method intent. Neither should drift into fabric-type advice the other covers |

---

## 3. Thin, empty or misleading collections

Do not describe these as a range, and think twice before linking them at all.

| Collection | Reality | The claim that was wrong |
|---|---|---|
| `/collections/samples` | **Zero products**, and it sits in the main site navigation | A page told customers to order samples from it before committing to a pail |
| `/collections/truckmount-parts` | **One product** - a stainless five-gallon jug holder | Described as holding "filters and replacement components" |
| `/collections/concrete-cleaning-equipment` | **One product** | Called "a full range of equipment" |
| `/collections/rotary-machines` | Rotovac carpet extraction equipment, **no pads** | A page sent readers there for diamond and stripping pads. Pads are in `/collections/bonnets-pads` |
| `/collections/odor-control` | Ozone generators and a fogger, **not air scrubbers** | Described as the destination for air scrubbers. Those are in `/collections/air-scrubbers-negative-air` |
| `/collections/encapsulation-vlm-1` | 4 products | Thin for a section telling readers to build out a low-moisture service |

**Rule:** open and count every collection before you describe it.

---

## 4. Blog blacklist - do not link

Measured body text, 27 August 2026. All are under the 300-word floor; most are video or Instagram embeds. Each of these was linked with a confident description of content that does not exist on the page.

| URL | Body text |
|---|---|
| `/blogs/news/avoid-re-do-jobs` | 6 words - title only |
| `/blogs/news/tmf-upholstery` | 0 - product grid, no editorial copy |
| `/blogs/training/proper-psi-carpets-upholstery-tile-grout-inline-sprayers` | 28 - Instagram embed |
| `/blogs/news/how-to-clean-a-leather-chair-cleaning-tips-and-hacks` | 33 - video |
| `/blogs/tmf-clips/microfiber-or-leather-furniture` | 34 - video |
| `/blogs/tmf-clips/floor-protection-tips-cleaning-tile-grout-upholstery-stairs` | 46 - video |
| `/blogs/tmf-clips/how-to-identify-hard-surface-floors` | 70 - video |
| `/blogs/tmf-clips/redos-how-to-fix-carpet-cleaning-redos` | 89 - video |
| `/blogs/cleaning-videos/best-vlm-method-and-how-to-encap-carpets-properly` | 39 - video |
| `/blogs/tmf-clips/tips-on-wand-cuffs-to-maximize-vacuum` | 36-71 - video |
| `/blogs/tmf-clips/which-flash-cuffs-is-right-for-you` | 36-71 - video |
| `/blogs/tmf-clips/video-should-you-use-a-leader-hose` | 36-71 - video |
| `/blogs/truckmount-tips/how-to-increase-your-truckmount-vacuum-power` | 36-71 - video |
| `/blogs/news/become-tmf-certified-in-pet-urine-odor-removal` | promotional offer, described as certification coursework |
| `/blogs/news/top-50-urine-odor-removers-for-cat-dog-human` | contains a single link pointing back at itself; recommended from two pages as a comprehensive roundup |

**The PSI post is the highest-value fix available.** Three of the ten audited pages leaned on it as their authority for pressure recommendations, and it contains 28 words. Ask TMF to commission 600-900 words for it.

---

## 5. Blog whitelist - verified substantial

| URL | Body text |
|---|---|
| `/blogs/news/how-to-clean-hardwood-floors` | ~4,400 words |
| `/blogs/cleaning-videos/how-to-clean-a-linen-sofa` | ~4,000 |
| `/blogs/news/best-solution-for-high-traffic-tile-floor` | ~2,700 |
| `/blogs/news/how-to-get-red-stains-out-of-carpet` | ~2,450 |
| `/blogs/news/carpet-walk-behind-extractor-vs-portable-vs-truck-mount` | ~1,110 |
| `/blogs/news/remove-pet-odor-from-carpets` | ~1,100 |
| `/blogs/news/rotovac-system-vs-truck-mount-carpet-cleaning` | ~1,060 |
| `/blogs/truckmount-tips/5-commercial-carpet-cleaning-techniques-employees` | ~1,000 |
| `/blogs/news/truckmount-forum-best-professional-carpet-spotting-kit` | ~870 |
| `/blogs/news/the-ultimate-guide-lvp-clean-and-recoat-for-sheen-finish` | ~600 |
| `/blogs/news/rob-allen-clean-carpets-filled-with-stinky-cat-pee-odors` | ~590 |
| `/blogs/training/tips-to-remove-the-top-5-worst-carpet-stains` | ~540 |

Note the live title when linking: the spotting kit post is "Truckmount Forum Best Professional Carpet Spotting Kit", and the high-traffic tile post is singular ("Tile Floor"), not plural.

Everything not on either list is **unmeasured**. Measure it before linking, then add it here.

---

## 6. Store-side fixes to raise with TMF

Not content problems, but several are why claims could not be verified, and all cost money or trust independently of the copy.

**Blocking**
1. Decide the company history answer and apply it once across all pages and About Us. Three different answers currently exist.
2. Resolve the hard-floor / wood-floor collection collision. Four URLs compete for overlapping intent.
3. Populate `/collections/samples` or remove it from the main navigation.

**High value**
4. Publish pH, unit size and dilution on every chemical listing; RPM, HP, weight, runtime and pressure rating on every equipment listing. This retires a whole class of unverifiable claim and would make these pages better than any competitor's.
5. Fix the RSF Alkaline and RSF Acid listings, which carry near-identical copy both saying the product "will drop the pH", and publish the actual pH of each. This is why the alkaline-vs-acid argument could not be sourced.
6. Commission real copy for the PSI post.
7. Settle the Spot-N-Boost filtration-soil contradiction: the collection page says general spotters cannot touch filtration soil, while the Spot-N-Boost listing calls it one of the best filtration-line removers on the planet.
8. Sweep the catalogue for leaked import metadata. The Stainless Steel Hose Connector 2 inch description ends with spreadsheet row and sheet IDs.
9. Fix the self-referential link in the Top 50 Urine Odor Removers post.
10. Confirm the Flash Cuff locking mechanism with the supplier so it can be described accurately.
