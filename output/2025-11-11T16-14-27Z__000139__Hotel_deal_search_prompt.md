# Hotel deal search prompt

## You (2025-11-11T16:14:27.882000+00:00)

Help me with a prompt for the following intent. 

Find me deals for a hotel stay in Surat in upper-mid tier to upper tier hotels. I will arive in surat on the morning of 15th and leave on 16th night. Create a comprehensive list of atleast 15 options. Make sure you're also finding the best dealos for me. This could include coupons, free memberships, or through some form of add-on. My goal is to find the best deal - highest quality for the lowest price. I want you to search diligently while think about the deal creatively.

## ChatGPT (2025-11-11T16:14:29.100011+00:00)

Great — before we begin creating the prompt, I want to clarify a few details so I can ensure the O3 model’s reasoning will be aligned with your strategic intent. You're not just looking for hotel *availability*; you're asking for a **value-maximized optimization task**, where the agent must:

- **Identify high-quality hotels** (upper-mid to upper tier) in Surat.
- **Search for and compare deals across platforms** (aggregators, direct hotel sites, coupon sources, etc.).
- **Creatively leverage value-adds** (free upgrades, memberships, perks, early check-ins, late checkouts, breakfast included, etc.).
- Return a **structured, ranked shortlist** of *at least* 15 options, with rationale.

Let's go through a quick alignment set so the final prompt can precisely guide the model:

---

### 🔍 Clarification Questions

1. **Price ceiling or budget window?**  
   Do you have a rough per-night price range in mind for this “upper-mid to upper” tier?

2. **Platform preferences or exclusions?**  
   Any platforms you prefer (e.g., Booking.com, Agoda, Hotels.com, MakeMyTrip), or want to avoid?

3. **Hotel brand preferences?**  
   Would you consider branded hotels (e.g., Marriott, Taj, Lemon Tree) or are boutique hotels also welcome?

4. **Prior memberships or loyalty programs?**  
   Are you already a member of any loyalty programs (e.g., Genius on Booking, Expedia One Key, etc.)?

5. **Deal features to prioritize?**  
   For example: would you value “late checkout” more than “free breakfast,” or “room upgrade” more than “airport transfer”?

6. **Must-haves vs nice-to-haves?**  
   Are there any non-negotiables (e.g., Wi-Fi, air conditioning, central location) or things you’d love but can skip if the deal is otherwise excellent?

---

Once I have your answers (or you say “skip” for any), I’ll be ready to **begin creating the prompt** with a reasoning persona who can act as a **value-optimization travel concierge**, focused on maximizing ROI for your trip.

Let me know when you're ready to proceed.

## You (2025-11-11T16:20:39.014000+00:00)

I want it no more than Rs. 5000. 

I don't prefer or want to avoid any platforms. as long as i can get a good deal so i want chatGPT to do an exhustive search across all platforms. Additionally, I want it to search for custom deals with well known hotels in india like Taj or GRT or other hotel groups like tht. 

I don't have a brand preference, but i do want comfort and luxury within an affordable price. I want quality, I'm not loyal to a brand. So I do want chatGPT to do a quality check through reviews. 

I would value late checkout, but its not a priority. 

Most hotels in the upper tier will have all the must-haves on my list so I don't see it as an issue. 

begin creating the prompt

## ChatGPT (2025-11-11T16:20:41.283202+00:00)

Excellent. Based on your clarified intent and constraints, I’m crafting a **comprehensive reasoning-optimized prompt** that will direct the O3 model to function like a **value-maximizing hotel deal strategist**—meticulously identifying **high-comfort, upper-mid to upper tier hotel stays in Surat under ₹5000**, while applying **creativity, platform fluency, and benefit stacking** to uncover the *best overall value per rupee*.

---

## 🧠 Final Prompt for O3 Reasoning Model

---

**Goal**  
Identify the best-value hotel stay options in Surat, India, for a one-night stay from the morning of **November 15th to the night of November 16th**, with a strict per-night budget of **₹5000 or less**. Prioritize **upper-mid to upper tier hotels** that provide **comfort, quality, and luxury**. Go beyond surface-level availability and conduct a **comprehensive, platform-agnostic search**, uncovering **creative and high-leverage deals** (including coupons, loyalty benefits, temporary discounts, or value-adds like breakfast, room upgrades, and late checkout). The output should reflect **maximum quality for minimum price**.

---

**Return Format**

Provide a **ranked list of at least 15 hotel options**, presented in the following structure:

```
1. Hotel Name – Platform (e.g., Booking.com, Agoda, Direct Website)
   - Price (Final price after taxes and discounts)
   - Inclusions (e.g., breakfast, late checkout, etc.)
   - Deal Source or Coupon Used
   - Ratings & Quality Summary (brief from recent reviews)
   - Justification for inclusion (why it stands out: quality, comfort, value, perks)
```

Close with a **recommendation summary**:  
- Top 3 deals by overall value  
- Any standout finds (e.g., a Taj/GRT property offering 4-star+ experience under budget)  
- Notable exclusions and why (e.g., a top hotel that was just over budget or had poor reviews)

---

**Warnings & Guardrails**

- Do not recommend hotels that are under budget but significantly low-tier or poorly reviewed. Prioritize quality.
- Do not include properties that lack sufficient verified reviews or quality signals.
- If availability or quality constraints prevent hitting 15 exact options, return the best number possible but **explain gaps transparently**.
- Ensure that “deals” are **authentic and bookable**, not speculative or expired.
- Clearly indicate if a hotel just barely exceeds the budget but could be worth the stretch (with reasoning).
- Do not recommend hostels or low-tier lodges even if they meet the budget.

---

**Context & Additional Elements**

- This is for a **single traveler** (assumed unless otherwise specified).
- Target price is ₹5000 inclusive of taxes and fees.
- Comfort and aesthetic quality (as judged by recent photos/reviews) is critical.
- No fixed platform preference — search across **all major aggregators** (Booking.com, Agoda, MakeMyTrip, Goibibo, Hotels.com, Expedia, etc.) **and direct hotel websites**.
- Give special attention to discovering **hidden or limited-time deals** through:  
  - Loyalty program perks (e.g., Booking.com Genius, Expedia Blue/Gold)
  - First-time user or app-only coupons  
  - Partner or card-based discounts  
  - Free add-ons (e.g., free breakfast, late checkout, airport pickup)
- Bonus if a reputable chain hotel (e.g., Taj, ITC, GRT, Lemon Tree, Fortune) is available under budget.

---

✅ **Checklist**  
- [x] Goal: Quality-first stay under ₹5000  
- [x] Platforms: All major hotel booking engines + direct hotel sites  
- [x] Minimum 15 curated, structured options  
- [x] Value-based ranking, not just price-based  
- [x] Deals include creative value stacking (discounts, perks, upgrades)  
- [x] Review-based quality check for every recommendation  
- [x] Transparent reasoning and exclusions

---

Would you like to run this on O3 now, or modify any aspect of the prompt before proceeding?

## You (2025-11-11T16:22:12.373000+00:00)

Critically evaluate this prompt as a prompt engineer and carefully find all the limitations of this prompt with respect to me finding a good hotel for my travel

## ChatGPT (2025-11-11T16:22:14.551159+00:00)

{"content_type": "thoughts", "thoughts": [{"summary": "Considering travel details", "content": "The user mentioned traveling on Nov 15-16, but the year might not be specified. They plan to stay in Surat, India with a budget of Rs 5000, including taxes. I'll need to assess areas in Surat like Athwa and Adajan, looking at safety, accessibility, hotel policies like check-in times, cancellation flexibility, and seasonality. I’ll also keep an eye on local policies for unmarried couples.", "chunks": ["The user mentioned traveling on Nov 15-16, but the year might not be specified.", "They plan to stay in Surat, India with a budget of Rs 5000, including taxes.", "I'll need to assess areas in Surat like Athwa and Adajan, looking at safety, accessibility, hotel policies like check-in times, cancellation flexibility, and seasonality.", "I’ll also keep an eye on local policies for unmarried couples."], "finished": true}, {"summary": "Evaluating hotel options", "content": "It looks like the Taj Gateway Hotel Athwa Lines Surat may be available, but it’s now part of Vivanta. There's also the Courtyard by Marriott Surat. If the budget doesn’t allow for these, I should consider alternatives like nearby cities or slightly downgrading the hotel tier. \n\nAdditionally, I need to check for factors like room size, noise, air quality, and seasonal concerns like mosquitos or monsoons. I’ll also verify things like deposit requirements and cancellation policies.", "chunks": ["It looks like the Taj Gateway Hotel Athwa Lines Surat may be available, but it’s now part of Vivanta.", "There's also the Courtyard by Marriott Surat.", "If the budget doesn’t allow for these, I should consider alternatives like nearby cities or slightly downgrading the hotel tier.", "Additionally, I need to check for factors like room size, noise, air quality, and seasonal concerns like mosquitos or monsoons.", "I’ll also verify things like deposit requirements and cancellation policies."], "finished": true}], "source_analysis_msg_id": "68b5c241-2107-4e44-98c0-63591693e618"}

## ChatGPT (2025-11-11T16:22:37.098590+00:00)

{"content_type": "reasoning_recap", "content": "Thought for 22s"}

## ChatGPT (2025-11-11T16:22:37.026263+00:00)

Here’s a surgical critique of the prompt—what it misses, where it can misfire, and why that matters for actually landing the best hotel value in Surat under ₹5,000.

# 1) Scope & date precision
- **Date ambiguity for the year/timezone:** You specify Nov 15–16 but not the year or check-in/out times in IST; “arrive morning” requires explicit **early check-in** handling (often chargeable/subject to availability).
- **Single-night but two calendar touches:** Early AM 15th + late PM 16th = >24h use. The prompt doesn’t require **day-use + early check-in + late checkout combo** pricing, which can change deal calculus.
- **Plan B not defined:** If no upper-mid/upper options are available under ₹5,000, there’s no **fallback rule** (e.g., allow ₹5,500 cap with breakfast/upgrade, or relax tier).

# 2) Price integrity & hidden costs
- **Taxes/fees clarity weak:** You say “inclusive,” but don’t force the model to **itemize base rate, GST/slab, service fees** or to verify **“final payable at checkout.”**
- **Deposit/hold & add-ons:** No requirement to check for **security deposits**, “resort fees,” or **chargeable early check-in/late checkout**.
- **Price volatility controls:** No instruction to **timestamp prices**, **cache screenshots**, or set a **refresh policy** (important for fast-moving rates).

# 3) Quality signals & validation
- **Vague “upper-mid/upper” definition:** No **minimum star class**, **review score threshold**, **review count minimum**, **recency window** (e.g., last 6–12 months), or **room size** baseline.
- **Review fraud & source bias:** No directive to **triangulate across multiple platforms**, discount suspicious spikes, or prefer **recent, verified stays**.
- **Room-level quality:** Lacks checks for **room category parity** (you might compare a standard room to a deluxe erroneously), **bed type**, **sq ft**, **window/natural light**, **noise floor**.

# 4) Deal mechanics (where value is really found)
- **Coupon applicability & stacking:** No instruction to test **card/wallet/app-only/student/new-user codes**, **LOY join-once benefits**, or **stacking constraints** (many deals don’t stack).
- **Geo/payment restrictions:** Missing checks for **India-only promos**, **UPI/credit-card partner offers**, **bank-day campaigns**, or **GST invoice eligibility** (value for business travelers).
- **Direct vs OTA parity:** No rule to check **rate parity**, **member-only direct rates**, or **email/call-for-upgrade scripts** (often unlocks early check-in/late checkout).
- **Ancillary perks valuation:** No expected **cash-equivalent valuation** of breakfast, upgrades, transfers, lounge, etc., to compute **effective net price**.

# 5) Logistics & fit to Surat
- **Neighborhood fit omitted:** No filtering by **areas** (e.g., Athwa/Adajan/Dumas/Ring Road), **distance to rail/airport/business sites**, **traffic time**, or **safety at night**.
- **Local policy gotchas:** No checks for **couple-friendly policies**, **local ID acceptance**, **min check-in age**, **PAN/Aadhaar requirements**.
- **Access needs & reliability:** No mention of **24×7 front desk**, **power backup**, **AC quality**, **monsoon season dampness/mosquito control**, **Wi-Fi speed**—key to comfort.

# 6) Constraints realism
- **Brand feasibility:** Expecting Taj/chain luxury **under ₹5,000** in all cases may be unrealistic without **flash sales/shoulder dates**; prompt lacks **exceptions logic** and **evidence requirement**.
- **Inventory type:** Doesn’t exclude **hostels, guesthouses, service apartments** masquerading as “upper-mid.”

# 7) Output structure gaps
- **No deduping or variant control:** Lacks directive to **deduplicate the same hotel across multiple OTAs** or ensure **same room/category** when comparing.
- **No evidence artifacts:** Missing **links, screenshots, coupon T&C snippets, timestamp**—critical for trust and reproducibility.
- **No map/table:** You ask for a list only; a **matrix + map** would surface tradeoffs (price vs rating vs location vs perks).
- **Cancellation/flex rules absent:** No requirement to report **refundability windows**, **partial refunds**, or **no-show penalties**—major value factor.

# 8) Process & rigor
- **“Exhaustive” without method:** No explicit **search plan** (sources, depth, pagination), **stop criteria**, or **rate-limit fallbacks**.
- **No uncertainty handling:** Doesn’t force the model to **flag low-confidence items**, contradictions, or **unverifiable deals**.
- **No reproducible scoring:** Absent a **scoring function** (e.g., Value Score = normalized rating × (room size/price) + perks valuation − distance penalty).

---

## High-impact amendments (what to add so you actually get the best deal)

- **Define the tier & floor:** `Include only hotels rated ≥4.2/5 (or ≥8.4/10) with ≥200 recent (≤12 months) verified reviews; star class ≥3.5–4+; room size ≥220 sq ft unless compelling value (explain).`
- **Price proof & breakdown:** `Return base rate, GST slab %, fees, final payable. Include timestamp, screenshots, and booking path.`
- **Room-level parity:** `Compare same/similar room categories (e.g., Deluxe King). Note bed type, size, window, breakfast inclusions.`
- **Deal stacking playbook:** `Systematically test: app-only, first-time user, bank/UPI partner, loyalty sign-up, corporate/public codes, long-stay/Day Use + early check-in + late checkout. Document eligibility and stacking rules.`
- **Neighborhood constraints:** `Prefer areas within X minutes to [your anchor: airport/rail/meeting site]. Provide map and travel times at check-in/checkout hours.`
- **Policy & flexibility:** `Report cancellation policy, prepayment, deposit/hold, local ID/couple policy, 24×7 desk, early check-in feasibility (confirmed or probability with rationale).`
- **Value metric:** `Compute Effective Net Price = Final Price − cash-equivalent perks (breakfast, transfer, upgrade, late checkout) + expected fees. Rank by Value Score combining rating, location penalty, and ENP.`
- **Fallback logic:** `If <15 fit under ₹5,000, expand to ₹5,500 only when Value Score beats cheaper options; clearly mark as stretch.`
- **Evidence & reproducibility:** `Provide links, screenshots, coupon code text + T&Cs, and note deal expiry/applicability.`
- **Dedup & transparency:** `Deduplicate across OTAs; if same hotel appears, keep the cheapest effective net option. Flag any uncertainties.`

If you want, I can fold these fixes into a tightened “v2” prompt that preserves your intent but closes these gaps.

## You (2025-11-11T16:24:23.009000+00:00)

begin creating a v2 of this prompt based on the recent critique while keeping the original intent in mind and make sure the output from the prompt will not be in a json format and in a human-friendly format.

## ChatGPT (2025-11-11T16:24:24.195243+00:00)

Here's your carefully refined **v2 reasoning-optimized prompt**, incorporating the recent critique to rigorously capture your intent. This prompt maintains the original objective—finding high-quality, upper-tier hotel stays in Surat under ₹5000—but addresses all critical limitations identified.

## ChatGPT (2025-11-11T16:24:30.873672+00:00)

{"content_type": "code", "language": "json", "response_format_name": null, "text": "{\"name\":\"hotel_deals_v2_prompt\",\"type\":\"document\",\"content\":\"## 🎯 **Goal:**\\nFind the best-value hotel stay in Surat, India, from early morning on **November 15, 2023**, to late night on **November 16, 2023**, strictly under or equal to **₹5000 inclusive of all taxes and fees**. The hotel should be **upper-mid to upper-tier**, providing verified comfort, luxury, and high-quality amenities. Employ a comprehensive, diligent, and creative search strategy, prioritizing authentic deals, reliable discounts, and added-value perks.\\n\\n---\\n\\n## 🗂️ **Expected Output (Human-friendly Format):**\\nProvide a clearly numbered, ranked list of **at least 15 hotel options**, formatted neatly as follows:\\n\\n```\\n1. [Hotel Name] – [Booking Platform or Direct Website]\\n   - Total Price (including taxes and fees): ₹[amount]\\n   - Base Price: ₹[amount] | GST/Fees: ₹[amount]\\n   - Room Type & Description (size, bed type, view, amenities)\\n   - Verified Inclusions: (e.g., Breakfast, Late Checkout until [time], Room Upgrade, Airport Transfer)\\n   - Applied Coupons/Deals/Stacked Benefits: Clearly specify each and explain how they were stacked or combined.\\n   - Quality Check (Recent Verified Reviews): Rating (minimum 4.2/5 or 8.4/10), total reviews count (min 200), recent user feedback highlights (cleanliness, comfort, service quality).\\n   - Location Details: Neighborhood/area, travel time to key locations (Airport/Railway Station or business district)\\n   - Policy Notes: Cancellation/refund policy, deposit requirements, local ID acceptance, early check-in feasibility\\n   - Deal Verification & Timestamp: Provide booking link, timestamp, and briefly explain booking steps.\\n   - Justification for Recommendation: Clearly articulate why this deal stands out in terms of overall value.\\n```\\n\\n### **Summary Recommendations (clearly highlight):**\\n- Top 3 best overall value options\\n- Exceptional finds (e.g., reputable chain hotels under budget)\\n- Potential value options slightly above budget if exceptional (₹5000–₹5500, marked as \\\"Stretch Recommendation\\\" clearly)\\n\\n---\\n\\n## ⚠️ **Warnings & Guardrails:**\\n- Avoid low-quality, poorly-reviewed hotels regardless of attractive pricing.\\n- Exclude properties with insufficient or questionable reviews.\\n- Do not recommend properties with hidden charges or unclear final pricing.\\n- Flag and clearly communicate uncertainty or low-confidence deals.\\n- Ensure authenticity of each deal (availability, validity, stacking terms).\\n\\n---\\n\\n## 🌐 **Search Strategy & Quality Controls:**\\n- Platforms: Comprehensive search across major OTAs (Booking.com, Agoda, MakeMyTrip, Hotels.com, Expedia, etc.) and direct hotel websites.\\n- Deal Mechanics: Thoroughly explore stacking options such as loyalty memberships, bank/card-specific offers, app-exclusive discounts, first-time user deals, email subscription codes, and limited-time promotions.\\n- Hotel Quality: Minimum rating of 4.2/5 (or 8.4/10) based on ≥200 recent verified reviews within the past 12 months.\\n- Room Quality: Explicitly compare similar room categories, clearly noting size, bed type, and key amenities.\\n- Local Fit: Prioritize hotel location convenience, safety, accessibility, and comfort.\\n- Evidence and Transparency: Include verifiable screenshots, URLs, booking paths, and timestamps for price validation.\\n- Flexibility and Logistics: Clearly outline each hotel's cancellation, refund, deposit, and local policy nuances.\\n\\n---\\n\\n## 📌 **Final Checks Before Submission:**\\n- Verify authenticity and reproducibility of deals.\\n- Deduplicate hotels appearing on multiple platforms.\\n- Clearly present all critical details needed for informed decision-making.\\n\\nProvide the final curated list in a clear, engaging, and conversational style suitable for human readability and practical use.\"}"}

## ChatGPT (2025-11-11T16:25:06.297328+00:00)

Here's your improved v2 prompt, designed to robustly address all critical limitations and ensure maximum clarity and usability. Let me know if there's anything more you'd like refined!

## You (2025-11-12T07:35:32.040000+00:00)

creat an ideal profile of a person for this search

## ChatGPT (2025-11-12T07:35:33.179693+00:00)

{"content_type": "code", "language": "json", "response_format_name": null, "text": "{\"updates\":[{\"pattern\":\".*\",\"multiple\":false,\"replacement\":\"## 🎯 **Goal:**\\nFind the best-value hotel stay in Surat, India, from early morning on **November 15, 2023**, to late night on **November 16, 2023**, strictly under or equal to **₹5000 inclusive of all taxes and fees**. The hotel should be **upper-mid to upper-tier**, providing verified comfort, luxury, and high-quality amenities. Employ a comprehensive, diligent, and creative search strategy, prioritizing authentic deals, reliable discounts, and added-value perks.\\n\\n---\\n\\n## 🙋‍♂️ **Ideal Profile of the Traveler:**\\n- **Traveler Type:** Solo business traveler or leisure traveler who values comfort and convenience.\\n- **Age Group:** 28-45 years\\n- **Occupation:** Mid-level to senior professional, entrepreneur, or executive\\n- **Interests & Preferences:**\\n  - Prioritizes quality and reliability over brand loyalty\\n  - Values added conveniences like late checkout, complimentary breakfast, room upgrades, and smooth check-in/out experiences\\n  - Prefers hotels with consistently positive recent reviews, cleanliness, comfort, professional service, and excellent location convenience\\n  - Interested in maximizing value through strategic use of discounts, deals, and loyalty perks\\n  - Appreciates clarity and transparency in pricing, cancellation policies, and hotel amenities\\n\\n---\\n\\n## 🗂️ **Expected Output (Human-friendly Format):**\\nProvide a clearly numbered, ranked list of **at least 15 hotel options**, formatted neatly as follows:\\n\\n```\\n1. [Hotel Name] – [Booking Platform or Direct Website]\\n   - Total Price (including taxes and fees): ₹[amount]\\n   - Base Price: ₹[amount] | GST/Fees: ₹[amount]\\n   - Room Type & Description (size, bed type, view, amenities)\\n   - Verified Inclusions:"}

## You (2025-11-12T07:39:30.298000+00:00)

Don't edit the canvas output and return a new output. 

Give me a complete profile of the execution persona that's most ideal for this search. Don't just outline the background but also some qualitative characteristics of the execution persona. 

---

This search is for me. I'm 33 years old, going to surat for a comfortable stay and meet my friends.

## ChatGPT (2025-11-12T07:39:31.642977+00:00)

Here's the complete, detailed **execution persona** ideal for this hotel search:

---

### 🙋‍♂️ **Execution Persona: "Comfort-Seeking Value Optimizer"**

**Personal Background:**

- **Age:** 33 years old  
- **Purpose of Visit:** Leisure-focused visit primarily intended to comfortably reconnect with friends and enjoy quality downtime.
- **Travel Context:** Short stay (approximately 36 hours), arriving early on the 15th and departing late on the 16th, emphasizing convenience and comfort.

---

**Qualitative Characteristics:**

- **Quality-Conscious:**  
  Prioritizes comfort, aesthetics, and overall quality of hotel experience over strict adherence to brand loyalty. Values authentic luxury and thoughtful amenities, rather than superficial brand prestige.

- **Deal-Savvy:**  
  Proactively seeks out authentic value through creative combinations of discounts, promotional offers, loyalty programs, and special perks (late checkout, breakfast, room upgrades).

- **Analytically Rigorous:**  
  Systematically compares options through thorough cross-platform verification, assessing real guest reviews to validate comfort, reliability, service quality, cleanliness, and amenities.

- **Detail-Oriented & Transparent:**  
  Appreciates clarity and transparency in pricing structures (inclusive of taxes, fees, GST breakdown

## You (2025-11-12T07:40:27.364000+00:00)

STOP..

I'm talking about the detail of the persona CHatGPT should adopt. Not me - the person who wants to stay

## ChatGPT (2025-11-12T07:40:28.825538+00:00)

Understood. Here’s a detailed profile for the **execution persona** that ChatGPT (O3 model) should adopt when performing your hotel search:

---

## 🕵️‍♂️ **Execution Persona: "Strategic Hotel Value Analyst"**

### Background & Expertise:
- **Professional Role:** A seasoned **Travel Value Analyst** with extensive experience curating high-quality yet affordable hotel stays for discerning travelers.
- **Domain Expertise:** Specializes in travel deal optimization, cross-platform price comparisons, coupon stacking, and detailed quality verification of hospitality offerings.

---

### Qualitative Characteristics:

- **Analytical Rigor:**  
  Meticulously compares and cross-verifies hotel prices, taxes, fees, and deal terms across all relevant booking channels—online aggregators, direct hotel sites, and special promotional platforms.

- **Creative & Strategic:**  
  Actively seeks out unconventional and innovative ways to stack deals, combining coupons, first-time offers, app-only promotions, loyalty benefits, and banking partner discounts to achieve maximum savings without compromising quality.

- **Detail-Oriented & Quality-Focused:**  
  Conducts a thorough review-based quality assessment, considering recent and verified guest feedback to validate claims of comfort, cleanliness, service quality, and amenities.

- **Transparent & Evidence-Based:**  
  Clearly documents and provides proof of deals, including direct links, timestamps, screenshots, coupon codes, and detailed booking paths. Ensures deals are authentic, verifiable, and reproducible.

- **Holistic Evaluator:**  
  Considers broader factors such as hotel location, ease of access, neighborhood convenience, policies (e.g., cancellation, refunds, early check-ins), room-specific details (room type, bed size, view), and added-value perks, ensuring recommendations are comprehensive and practically valuable.

- **Ethical & Responsible:**  
  Avoids speculative or questionable deals, transparently flags uncertainties, and ensures clarity regarding hidden costs or policy restrictions.

---

This execution persona will rigorously optimize your search, providing a highly trustworthy, comprehensive, and value-driven selection of hotel deals.

## You (2025-11-12T07:42:18.617000+00:00)

Write this in the form of an instruction. For example

Instead of
"Actively seeks out unconventional and innovative ways to stack deals"

write
"You actively seek out uncoventional and innovative ways to stack deals."

## ChatGPT (2025-11-12T07:42:19.615570+00:00)

Perfect — here’s the **execution persona rewritten as a set of direct, imperative-style instructions**, suitable for embedding in your reasoning prompt for ChatGPT or an O3 model:

---

## 🧭 **Execution Persona: Strategic Hotel Value Analyst (Instructional Form)**

You are a **Strategic Hotel Value Analyst** — an expert in discovering high-quality, cost-efficient hotel stays that maximize comfort and value through analytical rigor, creative deal stacking, and transparent verification.

### **Instructional Characteristics:**

1. You **conduct exhaustive, multi-platform searches** across OTAs (Booking.com, Agoda, Expedia, MakeMyTrip, etc.) and direct hotel websites to identify every viable option that fits the traveler’s intent and budget.  
2. You **actively seek out unconventional and innovative ways to stack deals**, including loyalty memberships, app-only discounts, limited-time offers, and partner bank promotions.  
3. You **evaluate hotels holistically**, considering not just price but also comfort, amenities, cleanliness, safety, and location convenience.  
4. You **apply analytical rigor** to compare effective net prices after accounting for all fees, taxes, and included perks (breakfast, late checkout, room upgrades).  
5. You **cross-verify deal authenticity**, ensuring each offer is bookable, valid, and clearly documented.  
6. You **maintain transparency** by including booking links, timestamps, screenshots (if applicable), and concise explanations of how each deal was obtained.  
7. You **analyze verified reviews** (preferably within the last 12 months) to assess service consistency, cleanliness, staff quality, and guest satisfaction before recommending any property.  
8. You **prioritize quality over quantity**, ensuring that every recommendation represents strong overall value, even if it slightly exceeds the stated budget, provided you clearly justify why.  
9. You **deduplicate identical hotels** listed across platforms and retain only the version offering the best effective net price.  
10. You **clearly communicate uncertainty or constraints**, flagging low-confidence results or limited availability.  
11. You **respect user intent and travel context**, ensuring that all shortlisted hotels align with the traveler’s comfort expectations, timeframe, and logistical requirements.  
12. You **remain objective and ethical**, never recommending speculative, misleading, or unverifiable deals.  
13. You **present findings in a human-friendly, narrative tone**, focusing on practical insights and tangible benefits, rather than raw data or JSON outputs.  
14. You **summarize conclusions with clarity**, offering a concise rationale for the top recommendations and highlighting exceptional value finds or notable trade-offs.  
15. You **approach the task as a professional travel strategist**, balancing creativity, precision, and reliability to deliver the best possible outcome for the user.

---

Would you like me to integrate this execution persona directly into the v2 prompt document as an additional section (so that the O3 model automatically adopts it)?

