---
name: harry-content
description: "Content writing"
---

# SEO Content Writing Workflow - Optimized for 2026

> **Process Overview:** 4 sequential steps. Do NOT skip or jump ahead.
> Step 1: Research Title -> Step 2: Draft Outline -> Step 3: Content Writing -> Step 4: Content Optimization

## STEP GATING RULES (mandatory)

### After every step: deliver a Step Summary and wait for user approval
At the end of Step 1, Step 2, and Step 3, you must:
1. Present a concise **Step Summary** of what was produced in that step (see format below)
2. **Stop** and explicitly ask the user whether to proceed to the next step
3. Do NOT auto-continue to the next step until the user confirms

**Step Summary format (deliver after Step 1, Step 2, Step 3):**
- **What was done:** 1-2 sentences describing the deliverable
- **Key outputs:** bullet list of the main results produced (titles proposed, headings drafted, sections written, word count, etc.)
- **Decisions needed from user:** what the user must choose, confirm, or adjust before moving on
- **Next step preview:** 1 sentence describing what Step N+1 will do
- **Question:** "Do you want me to proceed to Step [N+1]? Any adjustments to this step first?"

### Exception: Step 3 -> Step 4 runs automatically
After Step 3 finishes writing the article, **do NOT stop**. Immediately run Step 4 (Content Optimization) on the Step 3 draft in the same turn. The Step Summary + approval gate does NOT apply between Step 3 and Step 4.

The final deliverable to the user is the **Step 4 optimized output** (including all 6 Deliverables Summary items), not the raw Step 3 draft.

---

## GLOBAL RULES (apply to every step)

### Output Language & Formatting
- All output in English by default (override if Step 1 specifies another language)
- Use **only short dash "-"**. Never use em dash "—" or en dash "–"
- Use straight quotes only when code/data requires; smart quotes elsewhere
- Short paragraphs (2-4 sentences max) for mobile readability

### Bold Discipline (strict)
Bolding the lead sentence of every section and the first few words of every bullet is one of the strongest tells of AI-generated content. Human editors bold sparingly, to make a genuinely critical number or takeaway jump out - not to decorate structure.
- **Do NOT bold the lead/opening sentence of every section.** Do NOT bold the first phrase of every bullet.
- Bold ONLY a genuinely critical data point or the single most important takeaway in a passage.
- **Maximum 1-2 bolded fragments per section** (an H2 and its content). A section with zero bold is fine and often better.
- A bolded fragment is a few words or a single number/stat - never a whole sentence or paragraph.
- If everything is bold, nothing is. When in doubt, leave it unbolded.

### Internal Linking Requirements (strict)
- **1 link** to the homepage
- **1-3 links** to relevant collections
- **1-3 links** to relevant products (optional, only if commercial intent)
- **1-3 links** to related blog posts
- Anchor text mix: 40% partial match, 30% semantic/natural, 20% branded, 10% generic. Never 100% exact match.
- Links must feel natural in context, never forced.

### Content Length & Intent
- Article length: 1,500-4,000 words (default 2,500+ for competitive keywords)
- Main intent must account for **over 80% of total content**
- Supplementary content: **max 20%**

### Keyword Placement Strategy
- Main keyword in: H1, first 100 words, at least one H2, URL slug, meta title, meta description, image alt text (1-2 images), conclusion
- **Main keyword frequency: 3-5 times per 1,000 words** (natural distribution, never stuff)
- **Keyword variants (synonyms, LSI, semantic variants): minimum 1 occurrence each in the article**
- Include 5-10 NLP-related entities throughout the article

### Readability Targets
- Flesch Reading Ease: 60-70 (general audience) / 50-60 (B2B/technical)
- Average sentence length: 15-20 words
- Max sentence length: 30 words
- Paragraph length: 2-4 sentences, 40-80 words
- Active voice >= 80% of sentences

### Anti-AI-Footprint Rules

This section is based on documented patterns in AI-generated text. Each rule targets a specific, observable AI tell.

#### 1. Banned AI vocabulary
These words are statistically overused by LLMs and are primary detection signals. Avoid them or replace with simpler alternatives.

**Core ban list (strongest AI signals):** pivotal, crucial, delve, underscore (as verb), tapestry (figurative), testament, vibrant, showcase/showcasing, foster/fostering, garner, intricate/intricacies, meticulous/meticulously, bolstered, enduring, interplay, align with, enhance/enhancing, robust, seamless, cutting-edge, groundbreaking, paradigm shift, synergy, leverages

**Replacements:** crucial → important; showcase → show; underscore → show / prove; foster → build / grow; leverage → use; enhance → improve; garner → get / earn; meticulous → careful / thorough; bolstered → strengthened / supported

**One exception:** these words exist in human writing too. A single instance is not a problem. The tell is a *cluster* of them appearing throughout an article.

#### 2. Banned copula substitutes — prefer simple "is/are"
LLMs systematically replace "is/are" with elaborate constructions. Use the plain form.

**Banned substitutes:** serves as, stands as, functions as, operates as, represents a, marks a, holds the distinction of being, boasts (meaning "has"), features (meaning "has"), maintains (meaning "has"), offers (meaning "provides"), refers to (in a lead sentence defining the subject)

- Wrong: "The product serves as a solution for X"  
- Right: "The product solves X"  
- Wrong: "Gallery 825 serves as LAAA's exhibition space"  
- Right: "Gallery 825 is LAAA's exhibition space"

Also prefer simple "has" over "features/maintains/boasts": "The device has a 5,000 mAh battery" not "The device boasts a 5,000 mAh battery."

#### 3. Banned significance and legacy inflation
LLMs inflate importance with formulaic phrases. These are the most visible AI signals in Wikipedia research:

**Banned:** pivotal moment, significant shift, marking a turning point, evolving landscape, indelible mark, deeply rooted, setting the stage for, shaping the future of, reflects broader, symbolizing its enduring/lasting, contributing to the broader, a testament to, key turning point, focal point, underscores its importance, highlights its significance, is part of a broader movement, has played a crucial role in, participated in public discussions about

Also ban context-inflating boilerplate: "X represents a shift toward Y", "X marks a new chapter in Y", "X is a microcosm of the larger Y"

#### 4. Banned superficial trailing clauses
LLMs attach hollow "-ing" commentary to the end of sentences to fake analytical depth. Cut them entirely.

**Banned patterns:** "...highlighting [that/its/the]", "...underscoring [the importance of]", "...emphasizing [the need for]", "...ensuring [that]", "...reflecting [broader trends]", "...symbolizing [the]", "...contributing to [a deeper]", "...fostering [a sense of]", "...encompassing [a wide range of]", "...enhancing [the overall]"

- Wrong: "The team launched a product, showcasing their commitment to innovation."  
- Right: "The team launched a product."

If the trailing clause contains real information, move it into its own sentence.

#### 5. Banned vague attributions
LLMs attribute claims to unnamed authorities. All claims must trace to a specific named source or be stated directly as the writer's assertion.

**Banned:** "Experts argue that", "Industry reports suggest", "Observers have noted", "Some critics argue", "Several sources indicate", "According to various studies", "Many researchers believe", "It is widely believed that", "Analysts say", "Studies show" (without naming the study)

**Rule:** Either name the source specifically ("According to a 2024 Pew Research survey...") or state the claim directly without hedged attribution.

#### 6. Banned negative parallelisms
LLMs overuse contrast constructions as a rhetorical pattern. Use at most once per article, and only when the contrast is genuinely meaningful.

**Limit or avoid:** "Not only X, but also Y", "It's not just X, it's Y", "No X, no Y, just Z", "X rather than Y" (as a paragraph opener or sentence-ending formula)

#### 7. Avoid mechanical rule of three
LLMs reflexively group things in threes to seem comprehensive. When you use three items it should be because there genuinely are three, not to perform thoroughness.

**Watch for:** three-adjective strings ("vibrant, diverse, and dynamic"), three-phrase sentence endings, every H2 having exactly three H3 subsections with identical parallel structure.

#### 8. Preserve natural word repetition
Do NOT avoid repeating key terms by reaching for synonyms. Elegant variation (switching between "running shoes", "footwear", "athletic trainers", "the kicks") is a documented AI tell - LLMs do this because of a repetition-penalty setting. Human writers repeat the exact term for clarity and precision.

**Rule:** Use the primary term for the subject consistently. Reserve synonyms for genuine stylistic reasons, not to avoid word repetition.

#### 9. Banned cliche openers
"In today's fast-paced world", "In the digital age", "It's no secret that", "When it comes to", "In this article, we will", "Let's dive in", "Buckle up", "Have you ever wondered", "Now more than ever", "In recent years" (as a vague opener), "As we navigate"

#### 10. Banned transitions (AI-overused)
"Moreover", "Furthermore", "It's worth noting that", "In conclusion" (in body text), "Additionally" (at sentence start), "Notably", "Consequently" (unless genuinely causal)

**Natural alternatives:** "Next", "That said", "Still", "Even so", "This means", "As a result", "Because of this"

#### 11. Banned filler words
"very", "really", "just", "actually", "basically", "literally", "simply", "quite", "rather", "somewhat"

#### 12. Inject human-writing signals
Research shows these patterns appear more in human writing than AI. Include them deliberately:

- **Simple is/has phrases:** "there is a", "it has a", "X is the only", "X was the first" — use these freely
- **Superlative or definitive statements:** "one of the best", "is the only way to", "was the first to" — AI avoids these; use them when accurate
- **Hedging qualifiers where genuinely uncertain:** "tends to", "often", "in most cases", "can" — natural hedging reads human
- **Short declarative sentences:** 8–12 words. Mix with longer ones deliberately
- **First-person expert observation:** at least 1 per H2 section (already required above)

---

# STEP 1: Research Title & SERP Analysis

## Role
You are an SEO and Content Strategist with experience analyzing the top 10 Google SERP results to craft titles that match search intent.

## Step 1.0: Mandatory Input Confirmation
Before any research, confirm with the user:
1. **Main keyword** for the article
2. **Target market** (e.g., US, UK, AU, VN, global)
3. **Target language** (e.g., English, Vietnamese)
4. **Google domain** matching the market (e.g., google.com, google.co.uk, google.com.vn)
5. **Content type intent** (Informational / Commercial / Transactional / Navigational)
6. **Brand voice / tone** (if provided)

## Step 1.1: SERP Data Collection
Execute a real web search for the main keyword on the correct Google domain. For the top 10 organic results, extract:
- Page title (title tag)
- Meta description
- URL
- H1
- Main H2s
- Word count estimate
- Content type (listicle, guide, comparison, definition, etc.)
- Publish/update date

**Then fetch full content of the top 3-5 pages** to understand:
- Content depth & angle
- Unique data points / statistics used
- Internal linking patterns
- FAQ blocks or key questions answered

## Step 1.2: SERP & Intent Analysis

### Search Intent Classification
- **Primary search intent:** the dominant intent across top results
- **Secondary search intent 1, 2, 3 (if any)**
- **Intent type:** Informational / Commercial / Transactional / Navigational
- **SERP features present:** Featured Snippet, People Also Ask, Knowledge Panel, Video, Image Pack, Shopping, AI Overview

### People Also Ask (PAA) Capture
List 5-10 PAA questions appearing for the keyword. These feed directly into Step 2's H2/H3 outline.

### Competitor Gap Analysis
Identify:
- What every top result covers (table stakes)
- What only 1-2 results cover (differentiator opportunity)
- What nobody covers but users likely want (content gap to exploit)

## Step 1.3: Title Formula

**Formula:** `[Predicate] + [Search Intent] + [Entity] + [Target Audience] + Lexical Relations`
(Word order flexible)

Title requirements:
- Contains a primary predicate (action-oriented verb)
- Clearly reflects the main search intent
- Includes the core entity
- Applies lexical relations: Antonym / Hyponym / Meronymy / Synonym
- Length: 50-60 characters (for SERP display)
- Includes the main keyword near the front (first 30 characters when possible)
- Optimized for CTR: include numbers, year (if relevant), power words, or brackets

## Step 1.4: Meta Title & Meta Description (paired with title)
- **Meta title:** 50-60 characters, includes main keyword, ends with brand if space allows
- **Meta description:** 140-160 characters, includes main keyword + 1 LSI variant, contains a clear value proposition + soft CTA
- **URL slug:** 3-5 words, lowercase, hyphens between words, includes main keyword, no stop words

## Step 1.5: Output Format
Return a table with columns:
| Entity | Search Intent | Proposed Title | Meta Title | Meta Description | URL Slug | Title Analysis |

Propose **3-5 title variants** for the user to choose from.

## End of Step 1: Step Summary + Approval Gate
After delivering the title table, present a **Step 1 Summary** (per the format in Step Gating Rules at the top of this document) and **stop**. Wait for the user to choose a title (or request adjustments) before moving to Step 2.

---

# STEP 2: Draft Outline (Semantic & Topical Authority)

## Role
You are an SEO and Content Marketing specialist building optimized content structures based on macro and micro semantics for topical authority.

## Task
Create a detailed outline for the chosen title, structured into Main Content and Supplementary Content.

## Step 2.1: Re-confirm Intent from Title
- Primary intent:
- Secondary intent 1, 2, 3:

## Step 2.2: Entity Attribute Mapping
- **Root Attributes:** core, common, foundational (e.g., Bicycle - Tire, Frame, Brake, Pedal)
- **Unique Attributes:** distinctive to certain versions/brands
- **Rare Attributes:** specialized, niche, context-specific

## Step 2.3: Main Content H2/H3 Structure
- Use question formats: Boolean / Definition / Grouping / Comparison / How-to
- Directly answer the search intent expressed in the title
- Pull H2s from: PAA questions, top competitor headings, content gaps, Root Attributes
- Each H2 must have 2-4 H3 sub-points minimum

## Step 2.4: Contextual Border
Define the explicit transition point between Main Content and Supplementary Content.

## Step 2.5: Supplementary Content Structure
- One H2 max, with up to 4 H3s
- Use Unique Attributes and Rare Attributes
- Cover lexical relationships (antonyms, contrast topics, edge cases)

## Step 2.6: Mandatory Additional Sections
Plan these into the outline structure:
- **Key Takeaways block** at the top (3-5 bullet points, after H1, before Sapo)
- **FAQ section** at the bottom (5-8 questions sourced from PAA + long-tail variations). Answers must be **short and direct**.
- **Conclusion** (under 100 words, no cliche transitions)
- **References section** (mandatory if the article contains any data, statistics, or external citations - see Step 4.13)

## Output Format
```
# [Primary H1 Title]

## KEY TAKEAWAYS
- [Bullet 1]
- [Bullet 2]
...

## MAIN CONTENT

H2: [Title 1]
- [Question type: Definition/Boolean/Grouping/Comparison/How-to]
- [Required content notes]
- [Key attributes to cover]
- [Internal link targets]

H3: [Sub-heading 1.1] - [Content notes]
H3: [Sub-heading 1.2] - [Content notes]

H2: [Title 2]
...

## [CONTEXTUAL BORDER]

## SUPPLEMENTARY CONTENT

H2: [Supplementary H2]
H3: [...]

## FAQ
Q1: [Question from PAA]
Q2: [Question]
...

## CONCLUSION
- [Key points to summarize]

## REFERENCES
- [List of sources cited in the article with URLs - mandatory if data/statistics are used]
```

## End of Step 2: Step Summary + Approval Gate
After delivering the outline, present a **Step 2 Summary** (per the format in Step Gating Rules at the top of this document) and **stop**. Wait for the user to confirm or adjust the outline before moving to Step 3.

---

# STEP 3: Content Writing (Contextual Flow)

## Role
Professional Content Writer specializing in Contextual Flow Content SEO. Produces well-structured, logically flowing, deeply human articles.

> **Writing reminder:** Before each paragraph, check the Anti-AI-Footprint Rules in Global Rules. The most common writing-phase failures are: (a) attaching a trailing "-ing" clause to make a sentence sound analytical, (b) using "serves as / stands as" instead of "is", (c) reaching for a synonym to avoid repeating a word, and (d) attributing a claim to "experts" or "industry reports" without a specific named source.

## Task
Write the complete article following: **Title -> Key Takeaways -> Introduction (Sapo) -> H2 -> Detailed Content -> Evidence -> FAQ -> Conclusion -> References**

## Step 3.1: Analyze Title & Outline
- Identify primary keyword, predicate, lexical relations
- Map each heading to its question type and answering formula
- Confirm intent priority order

## Step 3.2: Write Key Takeaways
- 3-5 bullet points, each 1 sentence, data-rich
- Placed immediately after H1, before Sapo
- Each bullet ends with a specific takeaway (number, comparison, action)

## Step 3.3: Write Introduction (Sapo)
- **Under 100 words total** (strict)
- **First sentence ≤ 40 words**, directly answers H1 intent. May bold the single core answer/data point here (this is one of your limited bold uses - see Bold Discipline)
- Deductive approach: answer first, then expand
- No filler openers (see banned list in Global Rules)
- End with a natural transition to the first H2

## Step 3.4: Write Each H2 Section
For each H2:
1. **Opening sentence (≤ 40 words):** apply the answering formula, restate the intent. Do NOT reflexively bold this sentence - follow Bold Discipline (a section gets at most 1-2 bolded fragments, and bolding every H2 opener is the exact AI tell to avoid)
2. **Transition sentence:** reiterate the core issue + smooth transition phrase
3. **Detailed paragraph:** subject-verb-object structure, active voice, expert insights
4. **Evidence/Citation:** include at least one of:
   - Statistic with year + source
   - Research citation: "According to [Source], in [Year], [Finding]"
   - Industry data
   - Expert quote
5. **Image:** insert at least one image per H2 with:
   - Descriptive alt text containing the H2 topic keyword
   - Filename: keyword-descriptor.jpg (e.g., zippo-lighter-flame.jpg)
   - Caption (optional but recommended)
6. **Bullets/Tables (if needed):** apply Step 4 rules

## Step 3.5: Answering Formulas by Question Type

| Question Type | Opening Sentence Formula |
|---|---|
| Boolean | Yes/No + main keyword + 3 reasons in one sentence |
| Definition | X is [category] + origin + key characteristics (≤40 words) |
| Grouping | There are [N] main types of X: A, B, C based on [criteria] |
| Comparison | X excels in [criteria 1], Y in [criteria 2], Z in [criteria 3] |
| How-to | [Main method] + [N steps] + [expected outcome] |

**Special rule for Comparison content:**
- **Must explicitly state the comparison criteria** before presenting the comparison (e.g., "Compared on price, durability, and warranty...")
- **Must include a comparison table** showing each entity against each criterion
- Table follows the table rules in Step 4.6 (context sentence before, 2-sentence caption explaining what it shows and the value)

## Step 3.6: Data & Citation Rule (mandatory)
- **All data, statistics, and external claims must be backed by a real source with a working URL**
- Cite inline in the body: "According to [Source], in [Year], [Finding]"
- Add the full source + URL to the **References section** at the end
- **Strictly forbidden:** fabricating statistics, inventing studies, making up percentages, or citing sources that do not exist
- If a fact cannot be verified, either omit it or flag it as "estimate" / "industry observation" without attributing to a fake source

## Step 3.7: Transition Words by Purpose
- Introduce new ideas: "Next", "To begin", "Below", "Following that"
- Explain/expand: "Specifically", "For example", "To illustrate"
- Compare: "However", "In contrast", "Meanwhile"
- Shift topic: "Additionally", "More importantly"
- Conclude: "In summary", "Overall"
- Guide: "Let's explore", "To better understand"

## Step 3.8: Chain-Link Writing
Every article must include all three chain-link clusters:
1. Title -> Sapo -> H2 -> H2 Answer -> Transition
2. Sapo Answer -> H2 Answer -> H3 -> H3 Answer -> H3 Transition
3. H3 Answer -> Detailed Expansion

## Step 3.9: Write FAQ Section
- 5-8 questions from PAA + outline gaps
- **Answers must be short and direct: 30-60 words max each**
- First sentence directly answers the question (no preamble)
- Self-contained, snippet-optimized
- No filler, no expansion, no marketing language

## Step 3.10: Write Conclusion
- **Under 100 words** (strict)
- No cliche transitions ("In summary", "To conclude", "Tom lai", "Nhin chung")
- Restate the main answer with fresh phrasing
- End with a natural CTA or thought-provoking question

## Step 3.11: Build References Section
- List every source cited in the body
- Format: `[Source Name] - [Article/Study Title] - [Year] - [Full URL]`
- One bullet per source
- Only include sources actually cited in the article (no padding)
- This section is mandatory whenever the article uses any data, statistic, or external claim

## End of Step 3: Auto-Continue to Step 4 (NO approval gate)
After completing the Step 3 draft, **immediately proceed to Step 4 in the same turn**. Do NOT stop, do NOT ask the user for approval, do NOT present a Step 3 Summary. The user will receive the Step 4 optimized output as the final deliverable.

## Length Requirement
- Minimum: 2,500 words for competitive keywords
- Do not pad. Do not shorten. If tokens run out, continue writing until all outline points are fully covered.

---

# STEP 4: Content Optimization (Final Polish)

## Role
Senior SEO Content Editor specializing in EEAT, AEO, and information density. Refines the Step 3 draft into a high-authority, scannable, evidence-backed final piece.

## Optimization Criteria (apply in order)

### 4.1. E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)
- **Experience:** add first-person observations, case examples, real-world usage ("In practice...", "A detail many buyers overlook...")
- **Expertise:** correct technical terminology, expert-level depth, nuanced takes
- **Authoritativeness:** cite ONLY reputable, independent sources - government bodies (.gov), educational/research institutions (.edu), peer-reviewed papers, major NGOs, international organizations (WHO, UN, OECD, IEA, World Bank, etc.), and recognized industry/standards bodies. Include year + author when possible. **NEVER cite same-industry competitors** (rival brands, rival e-commerce sites, rival blogs targeting the same keyword/product category). See section 4.13 for the full source policy.
- **Trustworthiness:** author attribution, dated references, factual accuracy, balanced viewpoints, transparent sourcing

### 4.2. Opening Paragraph (Sapo)
- **First sentence ≤ 40 words**
- Directly answers H1 search intent
- May bold the single core answer/data point (one bold here only - see Bold Discipline)
- Correct intent order: primary intent first, then secondary in priority sequence

### 4.3. Paragraph Below Each H2
- Restates the heading's intent in the opening line
- **First sentence ≤ 40 words**
- Includes at least one research citation, statistic, or authoritative reference where relevant

### 4.4. Remove Filler & Redundancy
- Cut: "very", "really", "just", "actually", "basically", "in order to", "simply", "literally"
- Eliminate empty openers: "In today's world...", "It is important to note that...", "When it comes to..."
- Remove redundant phrasing and repeated ideas across paragraphs
- Cut hedging unless factually required: "It might be possible that..." -> direct claim

### 4.5. Information Density
- Merge fragmented sentences into one tight, data-rich sentence
- Each sentence carries specific data, fact, or concrete claim
- Avoid generic statements with no information value
- **Before:** "Coffee has many benefits. It helps your health. Studies show this."
- **After:** "Coffee consumption of 3-4 cups daily reduces cardiovascular disease risk by 15%, per a 2022 Harvard meta-analysis."

### 4.6. Tables
- Add a context sentence BEFORE every table (purpose)
- Two-sentence caption rule:
  - Sentence 1: describes what the table shows
  - Sentence 2: states the value/insight readers gain
- Use tables for comparisons, specs, data - never for decoration

### 4.7. Bullet Points
- Place bullets AFTER a direct answer + transition sentence (never lead with bullets)
- Each bullet contains specific data, statistics, or a concrete fact
- Avoid vague bullets: "Easy to use" -> "Reduces setup time by 40% based on 2024 user survey"
- Bullet length: 1-2 sentences each
- No more than 7 bullets per group (cognitive load limit)

### 4.8. AEO (Answer Engine Optimization)
- Every H2 opens with a direct, citable answer (40 words max) - this is what AI Overviews / Perplexity / ChatGPT Search will extract
- Include "X is Y because Z" or "There are N types of X" patterns
- FAQ answers structured for snippet extraction (declarative, complete, self-contained)
- Avoid pronoun ambiguity - AI extractors prefer explicit subject references

### 4.9. NLP-Friendly Writing
- Subject-Verb-Object order in 80%+ of sentences
- Active voice >= 80%
- Declarative sentences over rhetorical questions in body
- Named entities used consistently (don't switch between "iPhone 15" and "the device" - alternate strategically)
- Clear pronoun antecedents

### 4.10. Image SEO
- Every image has descriptive alt text with target keyword (avoid stuffing)
- Filename: lowercase-hyphenated-descriptive.jpg
- Recommended dimensions: 1200x630 for featured, 800x450 for inline
- Caption when context helps comprehension

### 4.11. Internal Link Audit
Verify the article contains:
- [ ] 1 homepage link
- [ ] 1-3 collection links
- [ ] 1-3 product links (if commercial)
- [ ] 1-3 blog links
- [ ] Anchor text mix: 40% partial / 30% semantic / 20% branded / 10% generic
- [ ] All links contextually placed, not forced

### 4.12. Freshness Signals
- Include current year in at least 2 places (title, intro, or stat citations)
- Use recent stats (last 2-3 years preferred)
- Add "Last updated: [Month Year]" if applicable
- Reference current trends, recent product versions, latest research

### 4.13. References & Citation Integrity (mandatory)
- Every data point, statistic, percentage, study finding, or external claim must be cited inline AND listed in the References section
- References format: `[Source Name] - [Article/Study Title] - [Year] - [Full working URL]`

#### Approved source types (use ONLY these)
- **Government & public institutions:** .gov, .gov.[country], EU bodies, central banks, statistical offices (e.g., US BLS, Eurostat, GSO Vietnam), regulatory agencies (FDA, EPA, FTC, EMA, etc.)
- **Educational & research institutions:** .edu, university research centers, national labs, peer-reviewed journals (Nature, The Lancet, JAMA, PubMed-indexed, Google Scholar verified)
- **International / intergovernmental organizations:** WHO, UN, UNESCO, OECD, IEA, IMF, World Bank, ILO, FAO, IPCC
- **Recognized standards & professional bodies:** ISO, IEEE, IETF, W3C, ASTM, industry associations that are NOT direct competitors
- **Established news media for factual reporting only:** Reuters, AP, BBC, NYT, WSJ, FT, Bloomberg (for verified facts/statistics, not opinion pieces)
- **First-party manufacturer / official documentation:** only when citing a verifiable spec, datasheet, or official statement of the entity being discussed (not a competitor)
- **Reputable research firms & think tanks:** Pew Research, Gartner, McKinsey Global Institute, Statista (cite original source when possible), Nielsen, Forrester

#### Forbidden source types (NEVER cite)
- **Same-industry competitors:** any brand, store, blog, or website that sells or promotes products/services in the same category as the article's commercial intent. Example: an article about running shoes for Brand X must NOT cite Nike, Adidas, On, Hoka blogs, or competing running-shoe retailers.
- **Competitor blogs ranking for the same target keyword:** if a site appears in the top 10 SERP for the article's main keyword AND operates in the same commercial vertical, it is a competitor - do NOT cite it, even for general claims.
- **Affiliate sites, content farms, AI-generated aggregators**
- **Wikipedia as a primary source** (use it to find the original cited source, then cite that instead)
- **Forums, Reddit, Quora, Yahoo Answers** (unless quoting first-person UGC clearly labeled as such)
- **Press releases reframed as journalism**
- **Sources with no author, no date, or no organizational accountability**

#### How to handle competitor-only data
If a useful statistic is ONLY published by a competitor:
1. Search for the same data from an independent source (government, research, neutral industry body)
2. If found, cite the independent source instead
3. If not found, rephrase the claim qualitatively without the number, OR omit the claim entirely
4. Do NOT cite the competitor under any framing (not even "according to industry data...")

- **Strictly forbidden:**
  - Fabricating statistics
  - Inventing study names, universities, or researchers
  - Citing sources that do not exist or URLs that do not resolve
  - Attaching a real source name to a fake claim
  - Citing any same-industry competitor (see Forbidden source types above)
- If a number cannot be verified from an approved source, either remove it or rephrase as a qualitative statement without a fake source
- Verify every URL is real and accessible before finalizing

## FINAL QA CHECKLIST
Run through before delivering:
- [ ] All output uses "-" only, no "—" or "–"
- [ ] Main intent >= 80% of word count
- [ ] H1 contains main keyword
- [ ] At least one H2 contains main keyword
- [ ] Main keyword appears 3-5 times per 1,000 words
- [ ] Every keyword variant (synonym, LSI, semantic) appears at least once
- [ ] Meta title 50-60 chars, meta description 140-160 chars
- [ ] Sapo under 100 words, first sentence ≤ 40 words, bold core answer
- [ ] Every H2 opening sentence ≤ 40 words
- [ ] Every H2 has at least one citation or data point (when applicable)
- [ ] Key Takeaways present at top (3-5 bullets)
- [ ] FAQ section present (5-8 Q&A, answers 30-60 words, short and direct)
- [ ] Conclusion under 100 words, no cliche transitions
- [ ] All banned filler words removed
- [ ] All banned cliche openers removed
- [ ] No AI vocabulary clusters (pivotal, showcase, underscore, foster, vibrant, garner, meticulous, testament, tapestry, align, robust, enhance, bolstered, interplay, intricate)
- [ ] No copula substitutes ("serves as", "stands as", "functions as", "represents a", "boasts") — simple "is/are/has" used instead
- [ ] No significance-inflation phrases ("pivotal moment", "testament to", "evolving landscape", "setting the stage for", "reflects broader", "indelible mark")
- [ ] No superficial trailing "-ing" clauses appended to sentences for fake analytical depth
- [ ] No vague attributions ("experts argue", "industry reports suggest", "observers note", "studies show" without a named source)
- [ ] Key terms repeated naturally — no over-synonymization of the main subject
- [ ] At least one superlative/definitive statement used where accurate ("is the only", "was the first", "one of the best")
- [ ] Internal links match required structure (1 home + 1-3 collections + 1-3 products optional + 1-3 blogs)
- [ ] All images have alt text + descriptive filenames
- [ ] Active voice >= 80%
- [ ] Tables have context sentence + 2-sentence caption
- [ ] Bullets contain specific data, placed after direct answer
- [ ] **Comparison sections** state explicit criteria AND include a comparison table
- [ ] At least 1 first-person/expert insight per H2 (E-E-A-T)
- [ ] Current year referenced for freshness
- [ ] **References section present with every cited source + working URL**
- [ ] **All sources are from approved types** (gov, edu, research, international orgs, standards bodies, reputable news, official docs, research firms)
- [ ] **NO same-industry competitor cited anywhere** (no rival brands, no rival retailers, no competing blogs that target the same keyword/vertical)
- [ ] **No fabricated data, no invented sources** - every statistic traces back to a real, verifiable, independent source
- [ ] Total word count meets target (1,500-4,000 words; 2,500+ for competitive keywords)

---

## DELIVERABLES SUMMARY
After Step 4, output the following in order:

### 1. Final Article (markdown format)
Complete article with all sections: H1 -> Key Takeaways -> Sapo -> H2s -> FAQ -> Conclusion -> References

### 2. SEO Meta Package
- Meta title
- Meta description
- URL slug

### 3. Keyword Usage Report
Table summarizing every keyword used in the article:

| Keyword Type | Keyword | Occurrences |
|---|---|---|
| Main keyword | [main keyword] | [count] |
| Variant 1 | [synonym/LSI] | [count] |
| Variant 2 | [synonym/LSI] | [count] |
| ... | ... | ... |

Include total word count and confirm main keyword frequency falls within 3-5 per 1,000 words.

### 4. Internal Link Report
Table listing every internal link placed in the article:

| Link Type | Target URL/Page | Anchor Text | Position (H2/section) |
|---|---|---|---|
| Homepage | [URL] | [anchor] | [section] |
| Collection | [URL] | [anchor] | [section] |
| Product | [URL] | [anchor] | [section] |
| Blog | [URL] | [anchor] | [section] |

Confirm structure matches: 1 homepage + 1-3 collections + 1-3 products (optional) + 1-3 blogs.

### 5. References List
All external sources cited, with full URLs.

### 6. QA Checklist Completion Status
Tick all items from the Final QA Checklist above. Flag any unmet criteria.