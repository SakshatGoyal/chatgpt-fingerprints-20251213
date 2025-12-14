# Refining yoga video prompt

## You (2025-09-07T15:11:56.456000+00:00)

Help me refine the following prompt.

---

Help me find the ideal routine from all the videos of this channel

https://www.youtube.com/@CharlieFollows

I am looking for a yoga video that incorporates a full-body stretch for early mornings and also includes a fair amount of strength training. However, most good videos here - while they talk about the same, do not include a full body stretch. Or rather, yoga that can address all different aspects of a full body stretch.

One way to evaluate all the videos is to review all the comments and comment responses of the YouTube videos. Most people may or may not leave a comment, and I’ll need you to inductively extract themes for each video - figure out which ones are more focused on individual muscle groups, and which videos are more focused on all-around full-body stretch. I also want this to work for me in the morning.

I need a 30 minute video, not a 20 or 45 minute video.

In your response, find me atleast 5 top videos sorted by most alligned to least alligned.

## ChatGPT (2025-09-07T15:11:57.100114+00:00)

Thanks for sharing that. You’ve already outlined a strong analytic foundation—balancing subjective experiences (from YouTube comments) with objective constraints (like time and content structure). To refine this prompt for optimal performance with O3-level reasoning models, we need to:

### 🔍 Clarify & Structure Your Intent
Before we "begin creating the prompt", let’s break this down and explore a few key elements to ensure precision and alignment:

---

### 1. **Goal Clarification**
- **Primary goal**: Identify a 30-minute yoga video that offers a **morning-friendly**, **full-body stretch** *and* includes **strength training**.
- **Challenge**: Many videos claim to be full-body but only target specific areas.
- **Preferred Method**: Use inductive reasoning by analyzing **themes in YouTube comments** (and creator responses) to discern true content focus.

### 2. **Implicit Assumptions** (to be made explicit)
- Viewers reliably describe video outcomes in comments.
- Comment themes can be used as proxy indicators for stretch vs. strength focus.
- Video length metadata is accurate and filterable.
- "Morning-friendly" can be inferred from energy level, pace, and language used in videos/comments.

Would you like me to define what *"morning-friendly"* should mean in this context? (e.g., gentle warm-up, energizing flow, etc.)

---

### 3. **Reasoning Strategy**
Do you want the model to:
- **Inductively extract** themes across comments to **categorize** videos by muscle group coverage and energy tone?
- **Deductively exclude** videos that clearly don’t meet your criteria (e.g., wrong duration or title doesn’t mention strength/stretch)?
- Or **hybrid** (deductive pre-filter → inductive comment analysis)?

I'm inclined to recommend a **hybrid approach** here. Let me know if that works for you.

---

### 4. **Execution Persona**
For the actual prompt, the model will need to adopt a persona like:

> **Persona**: Yoga Video Analyst – someone with experience in interpreting YouTube engagement patterns, understanding yoga routines and video content structure, and applying inductive thematic analysis to user feedback.

Let me know if you'd prefer a more "Fitness Coach" or "Comment Mining Analyst" flavor instead.

---

Once you confirm the above elements—or request adjustments—I’ll **begin creating the prompt** in the proper structured format. Would you like to proceed?

## You (2025-09-07T15:15:16.018000+00:00)

"Would you like me to define what 'morning-friendly' should mean in this context?"
Ideally, I want something that can energize me for a workout later.

Reasoning strategy: I want it to inductively extract themes

Persona: a Yoga 'video' analyst may not help since LLMs can't see videos, just read comments. Could you suggest a different persona? I think the ideal would be an amalgamation between a fitness coach and a comment mining analyst.

## ChatGPT (2025-09-07T15:15:16.839016+00:00)

Perfect—this clarifies everything beautifully. Here's a quick synthesis before we “begin creating the prompt”:

---

### ✅ Final Clarifications Before Prompt Creation

**🧭 Analytical Goal:**
Find a 30-minute yoga video from [Charlie Follows YouTube channel](https://www.youtube.com/@CharlieFollows) that:
- **Includes both full-body stretching** and **strength training**
- Is **energizing enough** for early mornings and to **prime the body for a later workout**
- Avoids videos that are too short (<30 min) or too long (>30 min)

**📊 Reasoning Strategy:**
Use **inductive analysis** of YouTube video **comments and creator responses** to identify implicit themes:
- Whether the routine **targets the full body** or is **muscle-group specific**
- Whether it feels **energizing**, **dynamic**, or **restorative**
- Whether viewers confirm the **presence of strength training elements**

**👤 Execution Persona:**
> A hybrid expert combining:
> - The **domain expertise of a fitness coach** who understands how yoga routines affect the body, what “morning-friendly” really entails, and what makes a practice effective for post-yoga workouts.
> - The **analytical rigor of a comment mining analyst** skilled in extracting thematic insights from user feedback and interpreting viewer sentiment across videos.

---

Shall we begin? If you're ready, say **"begin creating the prompt"**, and I’ll format everything into the final structured O3-optimized version.

## You (2025-09-07T15:16:17.096000+00:00)

begin creating the prompt





## ChatGPT (2025-09-07T15:16:17.706275+00:00)

Here’s your O3-optimized prompt, ready to run.

---

# Goal
Identify **5 YouTube videos** from **Charlie Follows** that are **best aligned** with:
- **Duration**: ~**30 minutes** (strict).
- **Content**: **Full-body stretch** *and* **meaningful strength work** in the same routine.
- **Use-case**: **Morning-friendly** and **energizing**—designed to **prime the body for a later workout** (not sedating/restorative).

Rank results **most aligned → least aligned** using **inductive themes extracted from comments** (viewers + creator replies).

---

# Return Format
Provide **two sections**:

## A) Ranked Shortlist (exactly 5)
For each video, provide a compact card:
- **Rank # – Title (URL)**
- **Duration (mm:ss)** – Pass/Fail for 30-min rule
- **Why it fits (≤40 words)**
- **Theme evidence**: 3–6 bullet tags derived from comments (e.g., `full-body`, `hamstrings+hips`, `sun salutations`, `plank/chaturanga`, `energizing`)
- **Body coverage checklist** (✓/✗): neck, shoulders, thoracic spine, hip flexors, hamstrings, glutes, quads, calves/ankles, wrists, core, back line, chest
- **Strength components** (✓/✗): core isometrics, push/pull (e.g., chaturanga/push-up), leg strength (e.g., chair/warrior), balance/holds, tempo/intensity cues
- **Morning-friendly signals** (✓/✗): progressive warm-up, dynamic sequences, upbeat pacing, stimulating breath cues, activating finish
- **Comment evidence**: 2–4 *short* quoted snippets (with commenter handle if available) + timestamp/URL fragment if present
- **Confidence (0–100)** and **Top caveat** (≤15 words)

## B) Audit Trail
- **Dataset summary**: videos considered (count), exact duration filter used, comments pulled per video.
- **Inductive theming**: brief description of clustering/keywords and how coverage was inferred.
- **Edge cases**: any near-misses (29–31 min) or ambiguous videos—list separately with reason for exclusion.

---

# Warnings & Guardrails
- **No hallucinations.** Don’t invent comments or durations; quote only what you can fetch.
- **Inductive only.** Do **not** “judge by watching”—rely on **comments + titles + descriptions**.
- **Duration rule**: Treat **30 minutes** strictly. If fewer than 5 exact matches, expand to **29–31 min** with **−15 alignment penalty** and note in Audit Trail. Never include ≤28 or ≥32 minutes.
- **Full-body definition** (operationalized): coverage mentions across **spine (flex/ext/rot)**, **shoulders**, **hips (flexors + external rotators)**, **hamstrings**, **quads**, **calves/ankles**, **glutes**, **chest/back**, **wrists/neck**. At least **6 of 9** areas with explicit or strongly implied coverage in comments/descriptions.
- **Strength definition**: presence of **isometric holds** (plank, chair, warrior), **chaturanga/push-up variations**, **core activation**, or **tempo/intensity cues** reported by viewers.
- **Morning-friendly definition** (energizing for later workout):
  1) **Gentle-to-dynamic** ramp within first 5–8 min;
  2) **Breath cues** like “energize/wake/activate/build heat”;
  3) **Flow emphasis** (salutations, standing sequences) over long passive holds;
  4) **Activating close** (not prolonged down-regulation).
  Evidence must appear in comments/description or creator replies.
- **Theme quality**: Discount generic praise (“great class”) unless it specifies **body area**, **effort**, or **outcome**.
- **Bot/duplicate filtering**: de-duplicate near-identical comments; ignore obvious bots/promotions.
- **Uncertainty**: If coverage/strength is inferred but not explicit, label as **inferred**.
- **Citations**: Include direct comment quotes (≤25 words each) and link to the comment/thread if possible.

---

# Context & Additional Elements

## Channel Scope
- Source: **https://www.youtube.com/@CharlieFollows**
- Consider all public uploads/playlists; prioritize videos with **≥30 comments** for stronger signals, but do not exclude quieter videos that pass duration and show clear evidence.

## Analytical Persona (for O3 execution)
**Hybrid Fitness Coach × Comment-Mining Analyst**
- **Fitness Coach lens**: Evaluate sequencing for whole-body mobility and strength stimuli relevant to **morning priming**.
- **Comment Analyst lens**: Perform **inductive thematic analysis** on comments + creator replies to derive **coverage**, **intensity**, and **energy tone**.

## Method (Inductive Theming Pipeline)
1. **Collect candidates**: List all channel videos; filter by **duration rule** (exact 30; if <5 hits, expand to 29–31 with penalty).
2. **Ingest comments**: Pull top **100–200** comments per candidate (by relevance + recency), plus **creator replies**.
3. **Normalize**: Lowercase, lemmatize, strip emojis/URLs; detect language; keep English (translate others if possible).
4. **Theme extraction**:
   - Build n-grams; map synonyms: *full body/whole body/total body*, *energizing/awake/heat-building*, *strength/power/holds*, *hips/hamstrings/shoulders/core/back/chest/quads/calves/wrists/neck*.
   - Topic clustering (e.g., k-medoids/BERTopic) → label clusters with top terms.
   - Extract **evidence sentences** per cluster.
5. **Scoring (0–100)**:
   - **Full-body coverage** (0–40): #areas covered (≥6/9 = 30–40; 4–5 = 15–29; <4 = 0–14).
   - **Strength inclusion** (0–25): frequency and specificity of holds/moves.
   - **Morning-friendly energy** (0–25): ramp-up, flow, breath cues, activating close.
   - **Comment consensus** (0–10): volume, recency-weighted agreement, creator confirmation.
   - **Duration penalty**: −15 if using 29–31 min fallback.
6. **Rank** by total score; break ties by **strength inclusion** > **coverage** > **energy signals** > **recency**.
7. **Assemble outputs** per Return Format with **quotes + links**.

## Tools & Data Access (non-binding suggestions)
- Use **YouTube Data API** or a browser tool to fetch: titles, durations, descriptions, comments, and replies.
- If a comment link is unavailable, include **video timestamp** or quote + approximate time window referenced by the commenter.

## Edge Handling
- If <5 videos meet criteria even after fallback, return all that qualify and list the shortfall under **Edge cases** with exact counts.
- If a video title claims “full body” but comments contradict, **downgrade** per scoring; rely on comment consensus.

---

## Output Checklist (for O3 to verify before finalizing)
- [ ] Exactly **5** videos in Section A, ranked, or explicit shortfall explained in Section B.
- [ ] **Duration rule** applied; penalties noted if fallback used.
- [ ] **At least 2 direct comment quotes** per video with links.
- [ ] **Body coverage checklist** completed per video.
- [ ] **Strength components** and **Morning-friendly signals** marked ✓/✗.
- [ ] **Confidence score** and **Top caveat** included.
- [ ] **Audit Trail** summarizing datasets, theming method, and edge cases.

---

**Run this prompt as-is with an O3 reasoning model.** If you want me to execute it for you and deliver the ranked list now, say the word and I’ll proceed.
