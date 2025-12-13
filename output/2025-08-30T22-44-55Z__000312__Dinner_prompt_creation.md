# Dinner prompt creation

## You (2025-08-30T22:44:55.033083+00:00)

Help me create a prompt.

I wanna take my family out for dinner. We're an Indian vegetarian family. One of us is on a keto diet, and while he can adjust, it would be better to find some options that don't require complete abandonment of the keto diet [ only minimal carbs allowed]

It's a special occasion so it's ok to find some place expensive. But price does not always equate to quality. 

I'm in Mountainview and we ideally want something in the south bay area where Mountainview is.

Ask me a few questions to refine the objective.

## ChatGPT (2025-08-30T22:44:56.220536+00:00)

Got it — thanks for laying that out clearly. Let’s refine step by step so I can help you build a strong prompt that an O3 reasoning model can execute effectively. Right now, I see a few moving parts:  

- **Constraints:** Indian vegetarian baseline, keto-friendly options needed for one person, South Bay geography, quality over price.  
- **Context:** Family dinner, special occasion → ambience and experience matter too, not just food.  

To narrow things down, I’ll ask a few clarifying questions. Answer whichever feel most relevant:  

1. **Ambience:** Do you want something formal and celebratory (white-tablecloth fine dining), or more relaxed but still high-quality (upscale casual, modern fusion, etc.)?  
2. **Cuisine Flexibility:** Does it need to be Indian cuisine only, or are vegetarian-friendly restaurants of other cuisines acceptable (Mediterranean, Californian, etc.)?  
3. **Keto Accommodation:** Should the prompt focus on restaurants that explicitly advertise keto/low-carb options, or is it enough if the menu has adaptable dishes (paneer, salads, avocado-based dishes, etc.)?  
4. **Family Size:** How many people are we talking about, and do you want the prompt to factor in whether the restaurant is good for groups (e.g., private dining room, big tables, shareable menu)?  
5. **Occasion Style:** Is this more of a *fun celebration* (lively, vibrant) or a *serious/meaningful occasion* (calmer, elegant)?  

Do you want me to structure the eventual prompt so the O3 model **recommends specific restaurants** with reasoning, or more like **a framework/checklist for choosing one yourself**?

## You (2025-08-30T22:51:06.027167+00:00)

Yes, formal and celebratory vibe 

Indian cuisine, but we can go for Thai too. Indian is the preference 

No I don't think good restaurants will explicitly show keto friendly options. Chatgpt will need to look through the menu and make an analytical assessment if the restaurant can cater to some degree to someone on a keto diet. BTW, not a strict keto but keto adjacent if that makes sense.

We have 5 people

The occasion is just a get together.

I'll need chatgpt to do some thorough research on this, give me atleast 20 options in the area and make sure to do it's research based on both - Google reviews as well as editorials like eater or other editorial food sites.

## ChatGPT (2025-08-30T22:51:09.298816+00:00)

{"content_type": "thoughts", "thoughts": [{"summary": "Continuing discovery process", "content": "Alright, the user wants to refine a prompt, but the task guidelines say to trigger creation only after they say, “begin creating the prompt.” Since they've already shared answers, we'll keep exploring and maybe ask a few follow-ups to confirm anything that might need clarifying before starting the actual prompt creation.", "chunks": [], "finished": true}, {"summary": "Confirming details for prompt creation", "content": "Alright, before creating the prompt, I need to confirm some key details: date/time constraints, dietary preferences, budget, seating, accessibility, and such. Also, the user wants thorough research done with specific parameters, so I’ll need to get more clarity on areas like locations, reviewer sources, and any special requests related to restaurant preferences—especially with that balance of Indian vs Thai!", "chunks": [], "finished": true}, {"summary": "Final clarifications before starting", "content": "Before creating the prompt, I’ll clarify key details like contact info, keto-friendly suggestions, hours, and other preferences. Given our goal, I’ll also propose evaluation criteria and the output format to confirm. This is part of the discovery process—without diving into any actual research, as that's for later!", "chunks": [], "finished": true}, {"summary": "Clarifying preferences and details", "content": "I need to ask about the travel radius and specific cities to focus on, especially whether to avoid SF city for the South Bay. I’ll double-check dietary preferences, spice levels, vegan, and gluten-free restrictions, and clarify keto specifics. I’ll also confirm the balance of Indian vs Thai and some restaurant vibe preferences!", "chunks": [], "finished": true}], "source_analysis_msg_id": "0293a6ee-7d27-4c75-836e-7666a0df2372"}

## ChatGPT (2025-08-30T22:51:26.487610+00:00)

{"content_type": "reasoning_recap", "content": "Thought for 17s"}

## ChatGPT (2025-08-30T22:51:08.728872+00:00)

Awesome — this is super clear. A few quick, targeted questions to lock the scope and output so O3 can execute cleanly:

1) Geography & radius  
- Which cities should count as “South Bay” for you? (e.g., Mountain View/Los Altos/Palo Alto/Sunnyvale/Santa Clara/Cupertino/San Jose/Saratoga/Los Gatos/Milpitas).  
- Max driving time from Mountain View at ~7 pm? (e.g., ≤25 min / ≤35 min).

2) Indian vs Thai split  
- OK to target ~15 Indian + ~5 Thai options, all upscale/formal-friendly?

3) Vegetarian specifics  
- Any strict constraints like **no onion/garlic (Jain)**, **no eggs**, or **vegan needed for anyone**?  
- Are non-veg kitchens acceptable if they have strong veg menus, or do you prefer **veg-only** restaurants?

4) Keto-adjacent guardrails  
- Any quantitative limit you want to enforce when assessing dishes (e.g., “prefer mains likely ≤10–15 g net carbs”)?  
- Are paneer/tofu/coconut-based curries, sautéed veg, salads-without-croutons, and tandoori/grilled items acceptable; avoid sugars, starch thickeners, rice, breads, and sweet chutneys?

5) Experience details  
- Noise tolerance (quiet/elevated vs lively)?  
- Alcohol program important (cocktails/wine), or neutral?  
- Parking/valet a factor?

6) Evidence & output style  
- I’ll instruct O3 to use **Google reviews + editorial sources (Eater, Michelin, SF Chronicle, Infatuation, local blogs)** and include **dates** for recency. Do you want a **ranked Top 10 + 10 more**, or a flat **ranked Top 20**?  
- Preferred format: a **table** with fields like *Name | Cuisine | City | Vibe | Price | Veg Depth | Keto-Adjacent Orders (2–3) | Evidence Snapshot (Google rating + editorial cites with dates) | Distance/ETA from MV at 7 pm | Reservations link | Notes* — plus a short narrative summary. Sound good?

Reply with your choices. When you’re ready, say **“begin creating the prompt”** and I’ll generate the final, O3-optimized research prompt with persona, guardrails, and structured return format.

## You (2025-08-30T22:54:46.997586+00:00)

Yeah, I think the cities you've listed out can count as within the South Bay area. I think a 20-minute drive from Mountain View should be good enough. I think I need 15 Indian options and 5 Thai options. As far as vegetarian, there's no strict guidelines. We're not Jains, so we're open to that.

Abt keto, I think paneer, tofu, coconut are acceptable.

Begin crafting the prompt. Make sure the prompt is in such a way that chatgpt really thinks for a long time.

## ChatGPT (2025-08-30T22:54:48.867464+00:00)

{"content_type": "thoughts", "thoughts": [{"summary": "Evaluating prompt structure", "content": "The user seems to want me to start crafting the prompt but the instructions specify it only begins with the phrase \"begin creating the prompt.\" Even though it's not an exact match, the user's intent is clear. I’ll follow the strict instructions but still capture the user's goals. Time to craft the structure!", "chunks": [], "finished": true}, {"summary": "Refining prompt content", "content": "I need to incorporate trusted sources like Google reviews or editorial outlets such as Eater, Michelin, and SF Chronicle for dish suggestions. I’ll provide keto-friendly options using ingredients like paneer, tofu, and coconut and propose a ranking system. I'll also clarify how to estimate drive times at 7 p.m. without live browsing.", "chunks": [], "finished": true}, {"summary": "Structuring reasoning process", "content": "I need to instruct ChatGPT to use multi-step reasoning but keep everything internal, not revealing the process itself. The model should reason step-by-step, ensuring recency and checking menu details. I'll include a table format for clarity and provide a confidence score based on food quality, keto fit, and other criteria.", "chunks": [], "finished": true}, {"summary": "Finalizing prompt structure", "content": "The prompt needs to cover all the requested details like off-menu requests, reservation info, noise levels, and parking. It should also address child-friendliness, even if not explicitly requested, for family gatherings. I'll ensure the format follows their structure with goal, format, guardrails, and context. I'll also include persona details.", "chunks": [], "finished": true}], "source_analysis_msg_id": "ce96cd4d-5c66-460e-b2e4-3a0122ae4167"}

## ChatGPT (2025-08-30T22:55:17.598664+00:00)

{"content_type": "reasoning_recap", "content": "Thought for 28s"}

## ChatGPT (2025-08-30T22:54:48.354796+00:00)

Here’s your O3-optimized research prompt. It’s structured to force deep, multi-phase reasoning and careful evidence gathering.

---

# Goal
Identify **20 upscale, formal-celebratory restaurants in the South Bay** (within ~**20 minutes driving from Mountain View at ~7:00 pm PT**) suitable for a **5-person Indian vegetarian family**. Deliver **15 Indian** and **5 Thai** options that (a) excel on food quality and ambience, (b) are reliably vegetarian-friendly (veg-forward menus are preferred; veg-only not required), and (c) offer **keto-adjacent** paths for one diner (paneer/tofu/coconut OK; minimize breads, rice, sugar, flour/cornstarch thickeners; favor grilled/tandoor/sautéed/low-starch dishes). Base conclusions on **Google user reviews** and **editorial sources** (e.g., Eater, Michelin, SF Chronicle, Infatuation, respected local food publications) plus current **official menus**.

# Return Format
Provide two parts:

**A) Ranked Table (Top 20 overall, interleaving Indian and Thai as scored):**  
Columns (one row per restaurant):
1. **Rank** (1–20)  
2. **Name**  
3. **Cuisine** (Indian/Thai; style if relevant: regional, modern, fine dining)  
4. **City** (South Bay only: Mountain View, Los Altos, Palo Alto, Sunnyvale, Santa Clara, Cupertino, San Jose, Saratoga, Los Gatos, Milpitas)  
5. **Vibe** (formal celebratory notes: white tablecloth, elegant, quiet-to-moderate noise, private room availability if any)  
6. **Price** ($$–$$$$, and estimated spend per person before tax/tip)  
7. **Vegetarian Depth** (brief: % of veg mains or count; standout veg dishes)  
8. **Keto-Adjacent Orders (2–3)** (concrete dish names + customization notes to minimize carbs; note likely starch/sugar sources to request omitted)  
9. **Evidence Snapshot**  
   - **Google:** rating, review count, last 12-month sentiment (e.g., “4.5★, 2.3k reviews; trend stable/up since 2024”).  
   - **Editorial cites:** outlet + date (e.g., “Eater 2023 feature; Michelin 2024 Bib; SF Chronicle 2022 review”).  
10. **Menu Check** (link to current menu + date accessed; confirm veg/keto feasibility)  
11. **Drive Time @7 pm** (minutes + miles; method/assumption)  
12. **Reservations** (OpenTable/Resy/direct; lead time tips for party of 5)  
13. **Watch-outs** (e.g., sweet sauces, cashew paste, hidden starch, service pace, noise)  
14. **Weighted Score (0–100)** (see rubric)

**B) Narrative Synthesis (≤600 words):**  
- **Why the Top 5 rank where they do** (1–2 lines each).  
- **Indian vs Thai tradeoffs** (where Thai wins for keto-adjacent, where Indian shines for veg depth/celebration).  
- **Clear playbook for the keto-adjacent diner** (what to request/avoid, common substitutions that staff understood during reviews/menus).  
- **Booking & timing tips** for a 5-top on a special-occasion evening in South Bay.

# Warnings & Guardrails
- **Deliberation:** Use a **multi-phase plan** (Plan → Search → Gather → Filter → Verify → Score → Compile → QA). Keep scratch work internal; **do not** reveal chain-of-thought. Present only conclusions and citations.  
- **Evidence standard:** For **every listing**, include **(i)** a Google review snapshot and **(ii)** at least **one editorial source** (or two if Google rating <4.3 or review count <300). Prefer items with **recent editorial mentions (2021–2025)**; if older, justify with current reviews/menu stability.  
- **Recency & menu validity:** Verify **current menus** (official sites/menus or recent PDFs); if only archived or social posts exist, state limitation and reduce confidence.  
- **Distance/time constraint:** Use authoritative mapping estimates (or distance-based proxy). If **>20 minutes @7 pm** in typical conditions, exclude unless exceptional; then flag as **borderline** with rationale.  
- **Vegetarian baseline:** Family is Indian vegetarian; non-veg kitchens acceptable. **Penalize** venues with weak vegetarian mains (e.g., one token veg curry).  
- **Keto-adjacent rubric:**  
  - **Good:** ≥3 plausible low-carb veg mains or sides; sauces manageable without sugar/thickener; clear substitutions (extra veg for rice/bread).  
  - **OK:** 1–2 mains workable with modifications; some sauces likely sweet/starchy—must specify “no sugar/cornstarch/flour; add veg; sauce on side.”  
  - **Weak:** Mostly carb-heavy (biryani, breads, sweet curries) with limited mod paths → deprioritize or exclude.  
- **Ambience requirement:** Prioritize **formal celebratory** rooms (tablecloths, composed plating, service polish). Busy but upscale is OK; loud casual or canteen style → exclude.  
- **Quality ≠ price:** Do **not** equate $$$$ with superiority. Use a **weighted score** driven by evidence.  
- **Uncertainty handling:** If evidence conflicts (e.g., great editorial, sliding Google trend), note it in **Watch-outs** and reflect in the score.  
- **No hallucinations:** Every factual claim (awards, Bib/Michelin status, private room, corkage, valet) must have a source. If unknown, say “not found.”

# Context & Additional Elements
- **User profile:** 5 people; special-occasion get-together; **Indian cuisine preferred**, **Thai acceptable**; keto-adjacent diner can eat paneer/tofu/coconut; minimal carbs desired.  
- **Geography/time:** Base location **Mountain View, CA**; **South Bay** cities listed above; evaluate **7:00 pm PT** travel time.  
- **Execution Persona (embed in your approach):**  
  - **Primary:** *South Bay Dining Researcher & Menu Analyst* — expert in Bay Area dining press, reservation dynamics, and menu composition.  
  - **Secondary:** *Vegetarian Keto-Adjacent Nutrition Analyst* — identifies hidden carbs (sugar, jaggery, honey, cornflour, besan/potato binders, sweet chutneys), proposes practical substitutions.  
- **Research Requirements:**  
  1. **Google**: pull rating, review count, and summarize last-12-month sentiment (look at review recency keywords).  
  2. **Editorial**: prioritize Eater SF, SF Chronicle, Michelin Guide, Infatuation, respected local blogs; include **publication dates**.  
  3. **Menus**: confirm veg options and feasibility of keto-adjacent customizations; link and **date accessed**.  
  4. **Reservations**: note OpenTable/Resy/direct path and earliest typical availability for a 5-top (estimate if necessary; mark as estimate).  
  5. **Mapping**: estimate **drive time & miles** from a central Mountain View point (state the point used).  
- **Scoring Rubric (0–100):**  
  - Food quality & consistency (30)  
  - Vegetarian depth & clarity (15)  
  - Keto-adjacent feasibility (25)  
  - Ambience & service polish for celebrations (15)  
  - Review/editorial acclaim & recency (10)  
  - Group suitability/reservations (5)  
  *Show sub-scores and total.*  
- **Exclusions:** No San Francisco/Peninsula beyond Palo Alto; no East Bay; no purely casual/cafeteria formats; exclude if **Google <4.1★** with ≥500 reviews **unless** strong editorial acclaim in 2023–2025 and clear menu improvements (justify).  
- **Deliverable QA:** Before finalizing, re-check that each row has **both** Google + editorial citations, a **current menu link**, concrete **keto-adjacent dish guidance**, and a **drive time** entry.

---

## Checklist for the Assistant (must confirm each item before submitting)
- [ ] Exactly **20** restaurants: **15 Indian**, **5 Thai**.  
- [ ] All within **~20 minutes** of Mountain View at **7 pm** (borderlines flagged).  
- [ ] Each row includes **keto-adjacent dish suggestions** with **customization notes** (e.g., “Palak Paneer, ask no cornflour, no sugar; double sautéed spinach; skip naan/rice”).  
- [ ] **Google rating + review count + trend** (recent months) present.  
- [ ] **At least one editorial citation** per venue with **date**; two if Google <4.3 or reviews <300.  
- [ ] **Menu link** + **date accessed** present.  
- [ ] **Weighted score** with sub-scores per rubric.  
- [ ] **Reservations path** included.  
- [ ] **Watch-outs** clearly stated (hidden sugars/starches, noise, service pace).  
- [ ] **Narrative synthesis** (≤600 words) explains Top 5 and tradeoffs.

**Instruction to the model:** Think in stages, allocate adequate reasoning time, search widely (beyond the first page), cross-validate menus and reviews, and keep your internal deliberations private. Output only the formatted table and synthesized narrative with clear, dated citations and links.

