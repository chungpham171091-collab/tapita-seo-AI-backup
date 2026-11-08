# Amazon listing localisation and QA

Listing optimisation and localisation QA answer different questions. An optimiser asks whether the title and bullets are commercially strong and search-aware. This pass asks whether a local shopper would find them natural, credible and appropriately premium, and whether every claim is supported. A high optimiser score does not override this gate.

## Marketplace to locale

| Store | Locale | QA lens |
|---|---|---|
| Amazon.co.uk | en-GB | British English, UK shopper phrasing, local category language |
| Amazon.de | de-DE | Noun capitalisation, natural compounds, Sie, local search syntax |
| Amazon.fr | fr-FR | Native rhythm, French typography, no English marketing casing |
| Amazon.nl | nl-NL | Netherlands Dutch, no Belgian drift, locked u/je |

## Input package

State the exact store and locale (not just "German"), the exact model, the proposed title and bullets, the validated keyword set (labelling optimiser-generated terms as candidates rather than demand), locked product facts and claims, and the current Amazon field constraints. Missing fields are marked TBC, not inferred.

**Run the naturalness pass blind.** Review the target-language listing without the English source in front of you. Seeing the source makes English syntax feel explained rather than wrong.

## Review hierarchy

When these conflict, the higher item wins:

1. Current Amazon store and category policy
2. Approved Coway product facts, claim substantiation and model identity
3. Coway terminology, locale pack and brand voice
4. Validated local marketplace keywords
5. The optimiser's proposed wording

Naturalness beats unvalidated exact-match wording. If a keyword conflicts with native grammar or premium tone, flag the trade-off rather than forcing the copy.

## Title checks

| Dimension | Pass condition | Common failure |
|---|---|---|
| Native title logic | Reads like a title a strong local brand would publish | English noun stack, imported Title Case, awkward comma chain |
| Search terms | Validated terms integrated where natural | Exact-match forced into strange grammar; synonyms repeated for density |
| Brand, model, category | Clear and correctly expressed | Model naming changed; literal but uncommon local category term |
| Decision usefulness | Leads with attributes that help the shopper compare | Slogan opening, generic adjectives, filler before the useful information |
| Claims | Every performance, allergy, filtration and room-size claim supported and qualified | "Helps reduce" becomes "eliminates"; test result loses conditions |
| Premium tone | Confident and precise | BEST, ultimate, revolutionary, all-caps, fear selling |

Policy checkpoint: Amazon's title requirement effective 21 January 2025 caps most categories at 200 characters including spaces, restricts certain special characters, and generally prevents a word appearing more than twice (articles, prepositions and conjunctions excepted). Store rules differ and change - the current Seller Central requirement always overrides this note.

## Bullet checks

- One dominant purchase message per bullet; a bullet is not a keyword list
- Feature → benefit → evidence or qualification, keeping any necessary limitation
- Rewrite freely around the meaning; do not preserve English sentence length, colon structures or feature labels
- Validated keywords in grammatically natural local forms
- No repeating the same headline claim, adjective or keyword across all bullets
- No hype, emoji, excessive symbols, fear marketing or bargain-market language
- Numbers, room sizes, CADR, noise, certifications, filter names and limitations match `products.md`

Policy checkpoint: Amazon's updated bullet requirements effective 15 August 2024 restrict special characters, emoji and certain phrases such as refund guarantees, and standard listings allow up to five bullets. Recheck the current category help page before publication.

The ✅ and Unicode pseudo-bold formatting used in some existing Coway listings fails both the platform's special-character guidance and the brand's premium positioning, and it breaks screen readers. Flag it as MAJOR.

## Defect examples

**CRITICAL** - wrong model or specification; unsupported performance or health claim; incorrect certification; forbidden terminology (True HEPA, H13, medical grade); named pathogen; material policy violation; keyword wording that misrepresents capability.

**MAJOR** - title or bullet clearly reads as translated; unnatural local category term; keyword stuffing; wrong regional variant; cheap or hyped tone; inconsistent formality; English casing or syntax imported.

**MINOR** - publishable but could be more elegant, shorter or more consistent.

## Required output

For the title and each bullet: verdict PASS or FIX, the exact problem phrase, the issue, why a local shopper would find it unnatural or inappropriate, severity, a recommended native revision, and the keyword impact (preserved / improved / trade-off / not applicable).

Then the overall gates: native naturalness, Coway brand tone, keyword integration, Amazon field and policy fit, claims and facts. **Publish only when all gates PASS with CRITICAL = 0 and MAJOR = 0.** Provide a clean revised title and bullets only where fixes were required.

## Second pass: claims and facts

After naturalness, compare the final listing against the approved fact sheet and claims evidence. This is optimisation, not translation, so not every source fact needs to appear - but every fact that *does* appear must be supported, accurate and no stronger than the approved source.

Check model identity; CADR, room size, noise, dimensions, filter life; filtration results and their test conditions; certifications; allergy, smoke and air-quality language; helps/reduces/captures versus removes/eliminates/protects/prevents/guarantees; approved terminology; omitted qualifiers that leave an included claim misleading; and anything the optimiser added that no source supports.

Never create or strengthen a claim for search performance.
