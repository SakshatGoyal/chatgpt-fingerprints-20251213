# Document content update





## You (2025-12-03T18:41:39.282000+00:00)

add the following content in the document opened in this tab. Use appropriate styling rules.

# Account Health – Scope Confirmation & Next Steps

Thanks — now that we have the latest designs, the meeting transcript, and alignment on the core vision, this document summarizes how we (design) are understanding the scope **and** how we propose to move forward.

This is written to:

* Show that we clearly understand the problem space and future direction.
* Call out where we see complexity or risk (roll‑ups, subjective health, lifecycle status, IA).
* Propose concrete next steps so we can move from concept to executable design work.

It deliberately **does not restate** all of the existing UI or metrics; everyone here already knows the current system well. Instead, it focuses on the *delta* we need to design for.

---

## 1. What we heard and how we’re framing the problem

From the recent conversations, we’re treating “Account Health” as evolving from a **single‑account cockpit** into a **multi‑layered health system** that must support:

1. **Apex accounts** with subsidiaries, where health exists at:

   * Individual account level ("Alphabet as a customer").
   * Apex roll‑up level ("Alphabet as a parent of Google, YouTube, Boston Dynamics, etc.").

2. **Two parallel views of health**:

   * **Objective health** – system‑calculated scores derived from existing KPIs (deployment, technical, adoption, support).
   * **Subjective health** – field / account‑team judgment that layers additional context on top of system data.

3. **Explainability and root cause clarity**, without forcing users to hunt through multiple tabs to understand why a product or account is red.

4. **Clear product lifecycle status** (Active, Inactive, Will‑Churn, Churned) that shapes how health is interpreted and how QBR / renewal conversations happen.

Our goal as design is to make this system **legible, navigable, and trustworthy** for the people who use it in high‑stakes conversations (CSMs, AEs, execs), while keeping the implementation viable for data and engineering.

---

## 2. Where we see complexity / potential issues

Below are the key areas where we see design and system complexity. These are also the areas where further alignment and documentation will reduce risk and rework later.

### 2.1 Roll‑ups (Apex ↔ subsidiary ↔ product)

**What’s straightforward:**

* We can roll up *counts* and *rates* (e.g., case counts, MTTR, adoption %, license volumes) as long as we agree on the aggregation rules.
* We can roll up health states using a simple hierarchy (Critical > At‑Risk > Healthy).

**Where we see potential issues:**

1. **"Two truths" at the Apex level.**

   * Example: Alphabet as a standalone account is Healthy; Alphabet as a roll‑up is Critical because Boston Dynamics is red.
   * We need a clear pattern to show **both** without confusing users.

2. **Not everything can be meaningfully rolled up.**

   * Detailed artifacts like case lists, pit‑stop timelines, PS project tables, and configuration details lose meaning when merged.
   * For these, roll‑up should be: **aggregated signal + drill‑down**, not a single mega‑timeline or mega‑table.

3. **Health semantics across different products.**

   * Health drivers for Prisma Access vs CDSS vs PA‑Series are structurally different.
   * We should ensure the roll‑up doesn’t imply false equivalence (e.g., a single “Critical” that hides whether it’s deployment‑driven or technical‑driven).

4. **IA and mental model at Apex.**

   * Today, all screens assume “one account.”
   * At Apex, users need to understand: *Which subsidiaries are pulling us down? Which products at which subsidiaries? How do I drill into that quickly?*

**Design implications:**

* Apex view must explicitly distinguish:

  * **Apex‑as‑account health** (direct purchases/install base).
  * **Apex roll‑up health** (aggregated subsidiary impact).
* We’ll prefer a **summary + hotspot list** pattern: e.g., “Top 3 subsidiaries dragging health down,” each with direct links into the existing single‑account lenses.
* For metrics that don’t roll up well, we will **not** force aggregation and will instead provide guided paths to the right child views.

---

### 2.2 Subjective health (human judgment on top of system scores)

We haven’t yet established subjective overrides as a full workflow, but the need is clear:

* Field teams want to express, “The system shows Critical, but we’ve mitigated the underlying issue and are confident,” or the opposite.

**Key complexities we see:**

1. **Scope of overrides.**

   * We believe overrides should apply only to **health states**, not raw metrics.
   * Candidate fields:

     * Overall account health
     * Technical health
     * Deployment & adoption health
     * Apex roll‑up health (for leadership‑level judgment)
     * (Optional) per‑product health where necessary

2. **Governance and roles.**

   * Who is allowed to set subjective health? CSM, AE, renewal rep, SE?
   * Does it require approval or is it a free‑form note?

3. **Lifetime and freshness.**

   * An override from six months ago is dangerous if it outlives the underlying data.
   * We’ll need rules like: *expires after X days* or *must be renewed when system health changes state*.

4. **Conflict representation.**

   * System says Critical, field says Healthy.
   * We need a clear, non‑ambiguous visual pattern that shows **both** and invites the user to understand why.

**Design implications:**

* We should treat subjective health as a **layer of annotation** with metadata (who, when, why), not a replacement field.
* The UI will show dual badges, e.g., “System: Critical / Field: At‑Risk,” with a quick way to see the justification.
* In the first iteration, we’d recommend keeping overrides limited to **overall account and Apex roll‑up** to reduce complexity.

---

### 2.3 Product & lifecycle status (Active / Inactive / Will‑Churn / Churned)

Right now, the designs surface a lot of lifecycle signals (support active/inactive, license terms, etc.), but the **state vocabulary isn’t unified**. That creates risk of:

* Misaligned mental models between CS, Renewals, and Product.
* Health scores on products that are effectively “dead” or “not yet started.”

**Where we see issues:**

1. **Fragmented labels.**

   * “Inactive support,” “never had support,” expired licenses, etc., all communicate lifecycle in different ways.

2. **Health on products that shouldn’t be evaluated.**

   * A churned product shouldn’t show “Critical” health in the same way as an active one; that confuses QBR messaging.

3. **Renewal workflows.**

   * The “Will‑Churn” window (contract ended, tenant still active, renewal in play) is key for CS and Renewals, but today it’s not clearly visualized.

**Design implications:**

* We’ll define a **single, shared dictionary** for product status:

  * **Active** – contract in force, usage & health fully relevant.
  * **Inactive** – purchased but not yet started / not activated.
  * **Will‑Churn** – post end‑date grace period; health still relevant to win‑back.
  * **Churned** – contract closed without renewal; health no longer actionable.
* This status will:

  * Appear explicitly in *Health by Products*.
  * Influence styling of the deeper lenses (e.g., greyed‑out charts for Churned).
  * Feed into notification and renewal strategies.

---

### 2.4 Navigation & explainability at Apex

Lastly, combining all of the above introduces **IA and explainability risk**:

* Users must be able to answer, quickly:

  * “Why is my Apex red?”
  * “Which subsidiaries and products are driving that?”
  * “Where do I click to see the evidence?”

Design‑wise, that means:

* Apex pages should behave more like **summary hubs** that point into the existing single‑account views, rather than attempting to show everything in one place.
* We will lean on **lists of hotspots** (subsidiaries/products in trouble) and **guided drill‑downs**.

---

## 3. How we propose to proceed (design next steps)

This section focuses on **what we do next**, not rehashing the past. The goal is to turn the conceptual model into concrete design work with minimal thrash.

### 3.1 Workstream A – Roll‑Up Rules & Apex Overview

**Objective:** Define and visualize how health and key KPIs roll up from subsidiary → Apex, and how we present this in an Apex Health Overview.

**Deliverables:**

1. **Roll‑up rules by metric category** (internal spec):

   * For each KPI we currently surface, document: roll‑up method (sum, weighted average, worst‑state, “no roll‑up – drill‑down only”).
   * Call out metrics that are *explicitly non‑roll‑up* (e.g., case lists, PS tables, pit‑stop timelines).

2. **Apex Account Health Overview wireframe:**

   * Shows Apex‑as‑account vs Apex roll‑up health side‑by‑side.
   * Includes a “Top problem subsidiaries” list with per‑product severity.
   * Provides clear drill‑downs into the existing single‑account lenses.

3. **IA diagram:**

   * Apex → Subsidiary → Product lens (Customer Estate / Deployment / Technical Health).

**Where we’ll need your input:**

* Confirmation of roll‑up behavior for MTTR and other time‑based metrics.
* Desired level of detail at Apex (e.g., is a simple “top 5 bad children” list enough, or do we need more structure?).

---

### 3.2 Workstream B – Subjective Health Model

**Objective:** Introduce a minimal, safe version of subjective health that supports field judgment without compromising trust in system data.

**Deliverables:**

1. **Subjective health spec:**

   * Exact fields where subjective values are allowed (starting with overall account health and Apex roll‑up health).
   * Required metadata (who, when, why, expiry).
   * Conflict resolution and display rules.

2. **UI patterns for dual health display:**

   * Badge layouts and tooltips for “System vs Field” states.
   * Example flows for adding/editing subjective health.

3. **Governance options:**

   * Option A: CSM‑only, no approval, short expiry.
   * Option B: CSM proposes, AE approves.
   * Option C: Pilot on a subset of accounts/products.

**Where we’ll need your input:**

* Which roles can set overrides.
* How long overrides should remain valid by default.
* Whether subjective health should feed into any reporting or is view‑only initially.

---

### 3.3 Workstream C – Product Status Dictionary & UX

**Objective:** Align on a shared lifecycle vocabulary and implement it consistently across the health experience.

**Deliverables:**

1. **Status dictionary v1:**

   * Active / Inactive / Will‑Churn / Churned with precise data conditions (contract start/end, grace window, etc.).

2. **Status → UX mapping:**

   * How each status affects:

     * Health by Products table (badges, greying, tooltips).
     * Deeper lenses (which charts stay active vs get dimmed).
     * Notifications and AI prompts (e.g., “Will‑Churn” drives renewal reminders).

3. **Edge‑case handling:**

   * Multi‑year deals with staggered lines.
   * Products moving from Churned back to Active (win‑back).

**Where we’ll need your input:**

* Confirmation of grace window semantics (e.g., T+30 vs T+60).
* The canonical contract data source and any nuances we should account for.

---

### 3.4 Workstream D – Apex IA & Explainability

**Objective:** Ensure that at Apex, the system tells a coherent story that can be used directly in QBRs and exec reviews.

**Deliverables:**

1. **Apex IA proposal:**

   * Navigation, breadcrumbs, and how users traverse Apex → child → product.

2. **Explainability patterns:**

   * How we answer “Why is this Apex red?” using a combination of:

     * Aggregated metrics
     * Highlighted subsidiaries/products
     * Links into the existing views

3. **QBR‑ready views:**

   * Identify which existing components (trends, timelines, estate views) can be safely reused in QBR decks and what additional summarization might be needed.

---

## 4. Decision checklist for you (what we need from Sumesh)

To keep things moving, here’s a concise list of decisions where your guidance will unlock progress:

1. **Roll‑ups**

   * Confirm approach for time‑based metrics (MTTR, deployment durations).
   * Confirm that detailed artifacts (case lists, PS tables, pit‑stops) remain non‑roll‑up and are handled via drill‑down.

2. **Subjective health**

   * Which fields we should enable in v1 (overall account, Apex roll‑up, others?).
   * Which roles can set or edit subjective health.
   * Default expiry window for overrides.

3. **Product lifecycle status**

   * Agreement on the four statuses (Active / Inactive / Will‑Churn / Churned).
   * Confirmation of grace period rules and contract data source.

4. **Apex IA expectations**

   * How “heavy” or “light” the Apex view should be (high‑level summary vs richer dashboard).
   * Priority personas for Apex (who we optimize for first: CSM, AE, leadership?).

---

## 5. Summary

We’re treating the work ahead as the evolution from a strong single‑account cockpit into a **coherent, multi‑layered health system** that:

* Represents both objective and subjective health,
* Handles the realities of Apex account structures,
* Clarifies product lifecycle status,
* And supports the real conversations teams have in QBRs and renewals.

The four workstreams above (Roll‑ups, Subjective Health, Product Status, Apex IA) are our proposed path to get there. Once we align on the outstanding decisions, we can move quickly into prototypes and validation with field stakeholders.















## ChatGPT (2025-12-03T18:43:18.414783+00:00)

I've added the provided content to your document using appropriate markdown-style headings and bullet lists. The document now reflects the full scope confirmation, complexity analysis, proposed workstreams, decision checklist, and summary sections, all formatted clearly and consistently. You can review the updated document to ensure everything looks good and matches your expectations【122999379062213†screenshot】.
