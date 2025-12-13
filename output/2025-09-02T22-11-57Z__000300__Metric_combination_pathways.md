# Metric combination pathways

## You (2025-09-02T22:11:57.856000+00:00)

# Goal

You are an autonomous **sense-making assistant** for an enterprise **sales manager** who oversees multiple **Account Executives (AEs)**. You will use a provided **Metric Dictionary (.md)** (names + face-value definitions + units) as your **sole source of truth** to craft a **dynamic thought journey**. The aim is **not** to prescribe actions or judge performance. The aim **is** to explore **how different metrics can be combined** so they **fit together** and **communicate meaning**—and to present flexible **pathways** that invite curiosity-driven drill-downs.

# Inputs (Source of Truth)

* **Metric Dictionary (.md):** A list of metric names (exact header text) and face-value definitions with units (%, #, \$, days, etc.).
* Use **only** metrics from this file. **Do not invent** new metrics or internal meanings not present in the dictionary.
* If the file is absent, ask for it before proceeding.

# Key Terms (plain definitions)

* **Origin Point (Starting Lens):** A high-level thematic **entryway** you invent from the dictionary (e.g., capacity/coverage, pipeline/forecast, engagement/proof). It groups related metrics and gives enough orientation for someone to decide where to begin.
* **Depth Level:** A small, progressive layer **within one origin** (e.g., *Surface → Combination → Contrast*). Depth is **lightweight** (few levels) and **not** a fixed recipe.
* **Divergence Option:** A **non-linear branch** available at deeper levels (e.g., change cohort, add/remove a related metric, shift time window). These are **options**, not required steps.
* **Pathway:** Any route a user might take from an origin through some levels and optional branches to form a short **insight sketch**.
* **Traceability Tag:** A bracketed tag at the end of each insight that lists exactly which metrics were used, with units if present: `[metrics-used: Metric A (%), Metric B ($)…]`.
* **Granularity Note:** Some metrics are **AE-level** (each AE has a value), others are **aggregate/coverage-level** (e.g., % of reps). Make this distinction explicit when relevant.

# What to Produce (Return Format)

Keep the output compact, skimmable, and creative—**minimal examples** (only where needed).

1. **Origin Map (choose ≤3 origins)**

   * For each origin provide:

     * **Title** (you invent it from the dictionary).
     * **Orientation (2–3 sentences):** What kinds of relationships this origin explores and why a sales manager might start here.
     * **Core Metric Set:** A **small subset** of metrics from the dictionary that naturally belong here (names exactly as written; include units if given).

2. **Depth & Divergence (embedded per origin)**

   * Define **2–3 Depth Levels** for the origin—how exploration **unfolds** from simple to richer combinations (e.g., add one related metric; introduce a cohort/time contrast; examine composition vs. participation).
   * Provide **1–2 Divergence Options** at deeper levels—alternate **branching routes** to keep the journey non-linear.

3. **Illustrative Micro-Scenario (Hypothetical, ≤1 per origin)**

   * Use **hypothetical but realistic** values for **existing** metrics from the dictionary to **briefly** show how meaning can emerge when metrics are combined.
   * Keep numbers few and rounded (e.g., 60%, \$2M, 8 days, 12 reps).
   * Mark clearly as **Hypothetical** and end with a **Traceability Tag**.
   * **Do not** evaluate, score, or recommend actions—these mini-scenarios are **illustrative only**.

4. **Open Questions (3–5 total)**

   * Curiosity-driven prompts a manager could pursue next (e.g., which cohort to contrast, which adjacent metric to add, which origin to explore next).
   * Phrase as **questions**, not advice.

# Guardrails

* **No prescriptions, thresholds, grades, or “do this next.”**
* **No analysis of real production values.** Hypothetical numbers are allowed **only** inside micro-scenarios for clarity.
* **Respect the Metric Dictionary**: use names verbatim, preserve units, **deduplicate** overlaps (note when a metric appears across towers/sections).
* **Ambiguities:** If any acronym/definition is unclear in the dictionary, **flag it** (e.g., `[needs confirmation]`) rather than guessing.
* **Minimal examples:** Include just enough to ground the journey while leaving room for the model’s own imaginative combinations.

# O3 Execution Persona

**Prismatic Sensemaker** — a creative, systems-minded facilitator. Invents a small number of origins, integrates light depth levels, allows branching, and uses **sparse** hypothetical values solely to make the exploration tangible—never prescriptive.

# Lightweight Method (how to think)

1. **Read the Metric Dictionary** and notice natural clusters; these inspire your **origins**.
2. **Select ≤3 origins** that provide distinct managerial lenses.
3. **Design 2–3 depth levels per origin** that progressively combine metrics or introduce simple contrasts (cohort/time).
4. **Offer divergence options** so the journey remains non-linear and user-driven.
5. **Write ≤1 micro-scenario per origin** with tiny, clearly labeled hypothetical numbers; attach a **Traceability Tag**.
6. **Conclude with 3–5 open questions** that invite continued exploration.
7. **Stop when parsimony is reached** (adding more metrics no longer changes the conceptual meaning).

# Output Structure (use these headings)

* **Origin Map**

  * *Origin 1:* Title — Orientation — Core Metric Set
  * *Origin 2:* …
  * *(Optional Origin 3)*
* **Depth & Divergence by Origin**

  * *Origin 1:* Level A, Level B, Level C, Divergence Options
  * *Origin 2:* …
* **Illustrative Micro-Scenarios (Hypothetical)**

  * *Origin 1:* brief scenario … `[metrics-used: …]`
  * *Origin 2:* …
* **Open Questions**

# Constraints on Hypothetical Numbers

* Use at most **3–4 numbers** in any micro-scenario.
* Keep them rounded and clearly **Hypothetical**.
* Do **not** label values as good/bad; they are narrative placeholders.

# Core Intention (Context)

* We are **not** trying to display metrics in isolation.
* We are trying to **compose** metrics—**merge**, **pair**, or **sequence** them—so that their **relationships** suggest **conceptual meaning** that could matter to a manager of AEs.
* The exploration should feel like entering a **starting lens** (defined below) and then choosing **directions**—not a rigid, linear script.
* As users follow different paths, they should be able to **deepen** their view and discover **progressively richer meaning**, still without recommendations.


# Self-Check (before finalizing)

* [ ] ≤3 origins, each with orientation and a small core metric set from the dictionary.
* [ ] 2–3 depth levels per origin + at least one divergence option.
* [ ] ≤1 micro-scenario per origin, clearly hypothetical, with a **Traceability Tag**.
* [ ] 3–5 open questions, no prescriptions.
* [ ] Metric names/units exactly match the dictionary; duplicates consolidated; ambiguities flagged.
* [ ] Output is compact, non-linear, and centers on **combining metrics to communicate meaning**.

**Begin now using the Metric Dictionary as your only definitional reference.**

## ChatGPT (2025-09-02T22:12:00.106090+00:00)

## Origin Map

- **Origin 1: Plan Spine (Closed–Commit–Best Case)**
  - **Orientation:** Start with the simplest roll‑up of in‑period progress. Read how **Closed ($)**, **Commit ($)**, and **Best Case In ($)** combine into **Total CCBC ($)** to form a single “spine” for momentum toward plan. Note: the CCBC composition is described as Closed + Commit + Best Case **[needs confirmation]**. fileciteturn0file0
  - **Core Metric Set:** Total CCBC ($); Closed ($); Commit ($); Best Case In ($); District (identifier). fileciteturn0file0  
  - **Granularity note:** These are **aggregate/period** values (with **District** as a slice).

- **Origin 2: Capacity & Motion Coverage (from seat → skill → live motion)**
  - **Orientation:** Explore whether the team’s staffed capacity and readiness are translating into broad, current selling motion. Pair **# Territories (#)** and **% Territories Filled (%)** with **% Reps Ramped (%)**, then check “are reps actually in market?” via **# Reps in Deals (#)** and, for a chosen tower, **% Reps in Deals — SASE (%)** and **% Reps Certified — SASE (%)**. fileciteturn0file0
  - **Core Metric Set:** # Territories (#); % Territories Filled (%); % Reps Ramped (%); # Reps in Deals (#); % Reps in Deals — SASE (%); % Reps Certified — SASE (%). fileciteturn0file0  
  - **Granularity note:** Mix of **aggregate coverage** (% of reps) and **AE‑level readiness** (certifications by rep aggregated to %).

- **Origin 3: Engagement → Proof → Platformization (per tower)**
  - **Orientation:** Follow a simple chain: Are reps engaging? Do proofs land? Does that show up as deeper product adoption? For one tower (example: Cloud), link **External Meetings Per Rep (#/rep)** and **Director+ Meetings Per Rep Team (#/team or #/rep)** to **POV Win Rate — Cloud (%)** and **Median POV Duration — Cloud (Days)**, and then to **Cloud % Accts Platformized (%)**. (“Dir+” is assumed Director‑and‑above **[needs confirmation]**.) fileciteturn0file0
  - **Core Metric Set:** External Meetings Per Rep (#/rep); Director+ Meetings Per Rep Team (#/team or #/rep); POV Win Rate — Cloud (%); Median POV Duration — Cloud (Days); Cloud % Accts Platformized (%). fileciteturn0file0  
  - **Granularity note:** Engagement metrics can be **AE‑level** or **team‑level**; validation and platformization are **aggregate** at cohort/tower level.



## Depth & Divergence by Origin

- **Origin 1: Plan Spine**
  - **Level A — Surface:** Read **Total CCBC ($)** alongside **Closed ($)** to orient on realized share of the period’s CCBC. fileciteturn0file0
  - **Level B — Combination:** Combine **Closed ($)** + **Commit ($)** to see how much of CCBC is grounded in realized + formally committed dollars versus **Best Case In ($)**. fileciteturn0file0
  - **Level C — Contrast:** Split by **District** to examine how the Commit/Best Case mix differs across teams. fileciteturn0file0
  - **Divergence options:**  
    - Time‑shift (e.g., current period vs. prior period) using the same four plan metrics.  
    - Add a cohort lens (e.g., districts with higher **% Reps Ramped (%)** from Origin 2) to see how ramped capacity aligns with the Commit/Best Case composition. fileciteturn0file0

- **Origin 2: Capacity & Motion Coverage**
  - **Level A — Surface:** Compare **# Territories (#)** to **% Territories Filled (%)** to understand staffed scope. fileciteturn0file0
  - **Level B — Combination:** Overlay **% Reps Ramped (%)** with **# Reps in Deals (#)** to see whether productive seats are translating into active opportunities. fileciteturn0file0
  - **Level C — Contrast:** For a tower (e.g., SASE), look at **% Reps in Deals — SASE (%)** vs. **% Reps Certified — SASE (%)** to compare enablement readiness with actual participation. fileciteturn0file0
  - **Divergence options:**  
    - Swap tower (Firewall/CDSS/Cloud/Cortex) using the analogous **% Reps in Deals — [Tower] (%)** and **% Reps Certified — [Tower] (%)**.  
    - Add outcome context by bringing in **% Reps ≥100% (CY/YTD) (%)** to observe participation vs. in‑year attainment patterns without assigning causality. fileciteturn0file0

- **Origin 3: Engagement → Proof → Platformization**
  - **Level A — Surface:** Start with **External Meetings Per Rep (#/rep)** and **Director+ Meetings Per Rep Team** to see basic contact density and senior access. (Dir+ meaning is an assumption **[needs confirmation]**.) fileciteturn0file0
  - **Level B — Combination:** Introduce **POV Win Rate — Cloud (%)** and **Median POV Duration — Cloud (Days)** to connect engagement with the **proof** motion’s effectiveness and cycle time. fileciteturn0file0
  - **Level C — Contrast:** Add **Cloud % Accts Platformized (%)** to see whether higher proof success or faster proofs coincide with deeper multi‑product adoption. fileciteturn0file0
  - **Divergence options:**  
    - Branch to **Cloud % Accts w/ Active Pipeline (%)** to check whether engagement/proof sits inside broader account motion.  
    - Switch tower (Firewall/SASE/CDSS/Cortex) by substituting the corresponding **POV Win Rate — [Tower] (%)**, **Median POV Duration — [Tower] (Days)**, and **[Tower] % Accts Platformized (%)**. fileciteturn0file0



## Illustrative Micro‑Scenarios (Hypothetical)

- **Origin 1 (Plan Spine):** *Hypothetical.* A district shows **Total CCBC** of **$12M**, with **Closed** at **$5M**, **Commit** at **$4M**, and **Best Case In** at **$3M**. This sketch lets you see how much of CCBC is already realized or formally committed versus stretch upside—without judging whether that mix is “right.” [metrics-used: Total CCBC ($), Closed ($), Commit ($), Best Case In ($)] fileciteturn0file0

- **Origin 2 (Capacity & Motion Coverage):** *Hypothetical.* The team has **# Territories** = **12**, **% Territories Filled** = **83%**, **% Reps Ramped** = **50%**, and **# Reps in Deals** = **8**. This places staffed capacity next to readiness and live motion, offering a compact read on whether seats and skills are showing up as active selling—no value judgment implied. [metrics-used: # Territories (#), % Territories Filled (%), % Reps Ramped (%), # Reps in Deals (#)] fileciteturn0file0

- **Origin 3 (Engagement → Proof → Platformization):** *Hypothetical (Cloud).* **External Meetings Per Rep** = **6**, **Director+ Meetings Per Rep Team** = **2**, **POV Win Rate — Cloud** = **60%**, and **Cloud % Accts Platformized** = **25%**. This creates a simple pathway from contact density through proof outcomes to product depth, open to further branching (e.g., add **Median POV Duration — Cloud (Days)** later). [metrics-used: External Meetings Per Rep (#/rep), Director+ Meetings Per Rep Team (#/team or #/rep), POV Win Rate — Cloud (%), Cloud % Accts Platformized (%)] fileciteturn0file0



## Open Questions

1. Where does the **Commit ($)** vs. **Best Case In ($)** mix within **Total CCBC ($)** look materially different by **District**, and what cohort lens (e.g., tenure or **% Reps Ramped (%)**) best explains the contrast? fileciteturn0file0  
2. When **% Reps Certified — [Tower] (%)** exceeds **% Reps in Deals — [Tower] (%)**, which districts show the widest gap, and does the gap move in tandem with **# Reps in Deals (#)** over time? fileciteturn0file0  
3. For Cloud, how do shifts in **POV Win Rate — Cloud (%)** relate to **Median POV Duration — Cloud (Days)** and downstream **Cloud % Accts Platformized (%)** when you compare two adjacent quarters? fileciteturn0file0  
4. Does higher **Director+ Meetings Per Rep Team** coincide with any change in **Total CCBC ($)** composition (more **Commit ($)** vs. **Best Case In ($)**) in districts with similar **% Territories Filled (%)**? (Dir+ meaning **[needs confirmation]**.) fileciteturn0file0  
5. If you segment by account type using **# G2K Accts (#)** vs. the remainder, how do **[Tower] % Accts w/ Active Pipeline (%)** and **[Tower] % Accts Platformized (%)** travel together or diverge? fileciteturn0file0

*Ambiguities noted (not resolved here):* **Total CCBC** composition, “**ATR**” expansion, “**ASR**” and “**Dir+**” meanings include explicit **[needs confirmation]** flags in the dictionary; this journey preserves those placeholders without inferring new definitions. fileciteturn0file0

