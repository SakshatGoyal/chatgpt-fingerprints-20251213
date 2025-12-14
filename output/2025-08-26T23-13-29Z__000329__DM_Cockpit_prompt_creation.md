# DM Cockpit prompt creation

## You (2025-08-26T23:13:29.465000+00:00)

I need assistance in framing a detailed prompt that aligns with my specific intent. I have developed a basic outline of a product requirements document and possess a custom GPT designed to emulate the thought process of a district sales manager at Palo Alto Networks, who is my target user for this product design exercise. My goal is to take a focused portion of that product outline and engage the custom GPT, representing the district sales manager, to analyze this content critically.

I am looking for insights on how this particular section of the product requirements can be beneficial from the perspective of a district sales manager, as well as any further enhancements or additions that might be necessary to refine the requirements effectively.

While I plan to share the broader context of the document eventually, my approach will involve pasting one subsection at a time in my prompt to facilitate focused feedback, starting with DM Cockpit. This will allow for a detailed examination and ensure that all aspects are addressed comprehensively.

---


# District Sales Manager Dashboard — Design PRD (v0.1)

## 0) Purpose & Product Frame

Create a **single, CRM-embedded pane** that turns scattered sales signals into **evidence-backed decisions and actions** for DSMs—without adding work. We’ll use AI in three modes (**Summarize, Assist, Automate**) to reduce reading, guide next steps, and automate low-risk busywork. &#x20;

**North-star outcomes for design to enable (not to engineer right now):** WAPE ≤ 8–10% at T-14; Commit accuracy ≥ 90% at T-7; inspection time ↓ 40%; slip from Commit ↓ 30%. These shape content priority and page states.&#x20;

---

## 1) MVP Scope (locked)

**Modules in v1:**

1. **DM Cockpit (Summary)**
2. **Forecast & Inspection (Commit Integrity)**
3. **Pipeline Quality & Hygiene**
4. **Rep-level Drill-down**
   This matches the staged rollout philosophy: Cockpit + Inspection + Hygiene first.&#x20;

**Guiding trade-offs for design:**

* Clarity over breadth: ship an excellent Summary cockpit before deep features.
* Unify, don’t re-platform (assume we live inside CRM/forecasting).
* Evidence beats opinion (Commit entries require proof or get reclassified).
* AI modes: Summarize, Assist, Automate—automation must be reversible & auditable.&#x20;

---

## 2) Information Architecture & Navigation

**Global filters:** Quarter | Product/pillar (Firewall, CDSS, SASE, Cloud, Cortex) | Region/District | Rep.
**Top-level nav:** Cockpit ▸ Forecast & Inspection ▸ Pipeline Hygiene ▸ Reps.
**Right rail:** Contextual “Evidence & Actions” drawer (opens from any exception list, commits, or rep).

This IA intentionally mirrors familiar patterns from your reference screenshot (path-to-plan header, team breakdown, exception tiles) to reduce learning cost.

---

## 3) Module Blueprints (content, interactions, AI roles)

### A) DM Cockpit (Summary)

**Primary JTBD:** “Scan path-to-plan, spot risk, act.”&#x20;

**Sections & content:**

* **Path to Plan**: Closed, Commit, Best Case vs Plan; delta vs last week.
* **Coverage & Activation** (leading signals):

  * `%Territories filled`, `#Reps in seat`, `%Reps ramped` (capacity → pipeline presence). &#x20;
  * `%Reps in Deals` (by pillar) and `%Accts w/ active pipe`—most proximate predictors of bookings. &#x20;
* **Technical Motion Quality:** `Tech Win %`, `POV Win %`, `Median POV Duration` (evaluation outcomes + cycle time).&#x20;
* **Exception List (click-to-inspect):**

  * Stale stage > X days; close-date churn; Commit without Champion/EB; unmapped paper process; InfoSec not started; low POC engagement; renewal ≤120 days with negative health.&#x20;
* **Team strip (rep cards):** Attainment band, active deals, hygiene flags, coaching cue.

**AI roles:**

* **Summarize:** “What changed since last week? Which drivers explain variance?”
* **Assist:** “Suggest 3 actions for highest-risk deals and who owns them.”
  (Automations like agenda generation live in Forecast; keep Cockpit light.)&#x20;

**Success signals (for design):** cockpit adoption ≥ 85%, inspection time ↓ 40%, % Commit with evidence ≥ 95%.&#x20;

---

### B) Forecast & Inspection (Commit Integrity)

**JTBD:** Run weekly forecast on **facts, not feelings**; keep Commit honest.&#x20;

**Views & interactions:**

* **WoW Forecast Delta:** variance decomposition; top movers by \$ and risk driver.
* **Commit Integrity Gate:** highlight deals lacking Champion/EB, decision criteria, mapped paper path/InfoSec; single-click “request evidence” or “reclassify.”&#x20;
* **Auto-generated agendas** per rep for the call; accept/override list with reasons retained for audit.&#x20;

**AI roles:**

* **Summarize:** variance by driver; confidence commentary.
* **Assist:** reclass suggestions with attached evidence trail.
* **Automate:** draft the call agenda + notes scaffold (reversible).&#x20;

**Design targets:** WAPE ≤ 10%; Commit accuracy ≥ 90% at T-7; slip ↓ 30%.&#x20;

---

### C) Pipeline Quality & Hygiene

**JTBD:** Keep pipeline real—remove deadwood, fix stages, build forward coverage.&#x20;

**Views & interactions:**

* **Deadwood Detector:** no activity > X days; mismatched stage vs activity; bulk close/merge with required note.&#x20;
* **Conversion Bottlenecks:** stage-to-stage deltas; compare to district median.
* **Coverage Shortfalls:** by pillar and segment; backfill targets list (accounts/plays).&#x20;

**AI roles:**

* **Assist:** propose cleanup + backfill actions; generate follow-ups.
* **Automate:** schedule nudges for stage discipline (undoable).&#x20;

**Design targets:** Stage SLA adherence ≥ 95%; fewer tools hopped per workflow.&#x20;

---

### D) Rep-Level Drill-down

**JTBD:** See who needs help, how they’re trending, and where to coach.

**Rep card content:**

* **Attainment & Trend:** `% Reps ≥100% CY`, attainment band.&#x20;
* **Activation & Readiness:** `%Reps in Deals` by pillar; `%Reps ramped`; pillar certifications.  &#x20;
* **Workload context:** `#Accts per Rep`.&#x20;
* **Coaching flags:** surfaced from conversion patterns, POV/Tech win signals, and hygiene exceptions.&#x20;

**AI roles:**

* **Summarize:** a weekly “rep health brief.”
* **Assist:** suggest next coaching topic + deals to review; auto-generate 1:1 packs.&#x20;

---

## 4) Content Model (what each card/tile must show)

**Exception tile (unit):**

* Title (driver) · \$ at risk · “Why” (1-line evidence) · Time stamp · CTA (Open evidence ▸).
  **Deal evidence drawer:**
* Source breadcrumbs (CRM fields, notes) · MEDDPICC evidence slots · Paper path/InfoSec status · Activity timeline. (Aligns to “evidence beats opinion” rule.)&#x20;

**Path-to-Plan header:**

* Closed, Commit, Best Case vs Plan + WoW deltas; percent to plan; confidence hint.

**Activation strip:**

* `%Reps in Deals` and `%Accts w/ active pipe` by pillar; sparkline trends for 4 weeks. &#x20;

**Technical motion card:**

* `Tech Win %` · `POV Win %` · `Median POV Duration (days)`; badge when outside district band.&#x20;

---

## 5) Interaction Patterns & States

* **Delta-first:** Always show change vs last week/quarter to focus attention.
* **Exception-driven scan:** The cockpit’s first scrollable area is the exception list; every row opens the right-rail evidence drawer.
* **Multi-select actions:** Bulk resolve in Hygiene; bulk reclass in Forecast.
* **States to design now:** empty (no data yet), loading (skeletons), error (inline retry), permission-limited (blurred metrics + explanation).
* **Audit trail:** every reclass/cleanup action stores “who/when/why” to reinforce trust (automation is reversible + logged).&#x20;

---

## 6) Metrics We Will Feature (why they’re here)

* **Near-term predictors (vital):** `%Reps in Deals`, `%Accts w/ active pipe`, `Open Pipe`, `Tech Win %`, `POV Win %`. These drive forecast confidence and conversion timing.   &#x20;
* **Capacity & readiness (leading):** `%Territories filled`, `#Reps in seat`, `%Reps ramped`, pillar certifications.  &#x20;
* **Attainment context (lagging):** `% Reps ≥100% CY`, attainment bands, `Total Booked` (for context only in cockpit). &#x20;

**Synthesis rule baked into design:** coverage/readiness → pipeline presence → attainment; exec engagement + technical quality shift conversion and ASP. (We reflect these causal links visually in the cockpit.)&#x20;





## ChatGPT (2025-08-26T23:13:30.258668+00:00)

Awesome—this is exactly the kind of focused, high-stakes prompting O3 is great at. Below is a tight plan + a ready template you can drop your **DM Cockpit** subsection into. When you’re ready for me to produce the fully finalized prompt in our house style, just say **“begin creating the prompt.”**

I’ll assume: Salesforce-embedded, weekly forecast cadence, MEDDPICC discipline, pillars as listed (Firewall, CDSS, SASE, Cloud, Cortex), T-14/T-7 checkpoints, and North-star targets from your PRD. If any of that is off, tell me and I’ll adjust.

# What we’ll optimize for
- **Persona realism:** District Sales Manager at Palo Alto Networks (quota-carrying, runs weekly forecast & inspection, coaches reps, defends commit).
- **Reasoning lens:** Hybrid (deductive from targets + telemetry, inductive from field patterns).
- **Outcome:** Actionable critique of DM Cockpit—what helps a DSM today, what’s missing, and how to improve it—mapped to your North-stars.

# Rubric the DSM GPT will use
1) **Decision readiness:** Does the cockpit let me confirm/defend commit in <5 min?
2) **Evidence rigor:** Every claim ties to proof (Champion/EB, paper path, InfoSec, POV/tech-win).
3) **Forecast impact:** Clear levers to move WAPE ≤10% (T-14) and ≥90% commit accuracy (T-7).
4) **Activation coverage:** %Reps in deals / %Accts with active pipe by pillar actually predicts bookings.
5) **Exception handling:** Stale, churny close dates, commit w/o evidence—1-click to inspect/act.
6) **Adoption & load:** <40% inspection time; zero net new admin work; reversible, auditable automations.

(We’ll have the DSM GPT score each 0–5 and explain the score.)

# Quick-start template (drop in your **DM Cockpit** text)
Use this as a working prompt with your custom DSM GPT today. It’s not the final formatted version—but it’s fully usable.

```
ROLE
You are a District Sales Manager at Palo Alto Networks running weekly forecast + inspection. You must defend commit on facts, coach reps, and reduce slip. You think in MEDDPICC, paper path, InfoSec gates, POV/tech-win signals, and coverage by pillar (Firewall, CDSS, SASE, Cloud, Cortex).

GOAL
Critically evaluate the “DM Cockpit (Summary)” section below to decide:
(a) What immediately helps a DSM drive commit integrity and coaching,
(b) What’s missing or ambiguous,
(c) What to change/add so the cockpit materially improves WAPE ≤10% (T-14), Commit Accuracy ≥90% (T-7), and inspection time ↓40%.

INPUT: DM COCKPIT TEXT
<<<PASTE DM COCKPIT SECTION HERE>>>

CONSTRAINTS & CONTEXT
- Live inside CRM; no re-platforming. Automation must be reversible + auditable.
- Evidence beats opinion: Commit requires proof (Champion/EB, Decision Criteria, Paper Path, InfoSec/Legal, POV/Tech Win).
- Delta-first: Show changes vs last week/quarter. Exception list opens right-rail evidence drawer.
- Keep Cockpit light; deeper automations can live in Forecast & Inspection.

ANALYTIC TASKS (do all, in order)
1) DSM VALUE SNAPSHOT (≤7 bullets)
   - How this cockpit helps me defend commit quickly.
   - Which sections/tiles are most decision-relevant and why (Path-to-Plan, Activation, Technical Motion, Exceptions, Team strip).
2) GAP ANALYSIS (prioritized)
   - What’s missing to make weekly inspection decisive? (e.g., partner influence, renewal/expansion tie-ins ≤120 days, attach/cross-pillar signals, slip reason codes, exec alignment).
   - For each gap: why it matters, where the evidence should come from (CRM fields, POV notes, security review), and the single best UI affordance (e.g., badge, inline chip, right-rail slot).
3) METRICS & TARGETS CHECK
   - For each metric proposed (e.g., %Reps in Deals, %Accts w/ Active Pipe, Tech Win %, POV Win %, Median POV Duration):
     • Is it predictive for a PANW DSM?
     • What threshold/band should trigger an alert?
     • What action does a DSM take when it’s red?
4) EXCEPTION DESIGN REVIEW
   - Do the listed exceptions cover top slip drivers? What 1–2 exceptions are missing?
   - For each exception, specify the minimal “evidence slots” needed in the right rail (MEDDPICC, Paper Path, InfoSec, Activity timeline).
5) AI MODES SCOPE
   - Summarize: the two weekly questions it must answer (variance, drivers).
   - Assist: top 3 actions with owner per highest-risk deal.
   - Automate: what to defer to Forecast (agenda/notes), and what low-risk busywork to automate safely in Cockpit (with undo + audit).
6) ADOPTION & LOAD
   - Estimate inspection time using this cockpit (minutes); where can we remove clicks/read time?
   - Identify any new admin work this design might accidentally create and how to avoid it.

RETURN FORMAT
- Scores (0–5) for: Decision Readiness, Evidence Rigor, Forecast Impact, Activation Coverage, Exception Handling, Adoption & Load.
- “What’s Good” (≤5 bullets).
- “Gaps & Enhancements” (table: Gap • Why it Matters • Evidence Needed • Proposed UI • Expected Impact on WAPE/Commit).
- “Top 5 Actions to Ship in v1” (ranked; include effort estimate S/M/L and risk).
- Open Questions (assumptions/unknowns the PM must resolve).

WARNINGS & GUARDRAILS
- If information is missing, state the assumption explicitly; do not invent data.
- Separate field-proven patterns from speculation.
- Tie every enhancement to a measurable outcome (WAPE, Commit accuracy, inspection time, slip from Commit).
```

# Optional “field-ready” enhancements the DSM GPT should look for
- **Partner/route-to-market signal:** flag high-influence partners on at-risk deals.
- **Renewal adjacency:** highlight renewals ≤120 days with neg. health + net-new pipe in same account.
- **Attach/cross-pillar:** show SASE/Cortex attach to NGFW (and vice versa) to boost ASP/probability.
- **Slip reason taxonomy:** standard codes with WoW trend.
- **Executive alignment chip:** Champion vs EB mapped + last exec touch.

---

If you want, say **“begin creating the prompt”** and I’ll turn this into the final, polished O3 prompt with your chosen defaults, plus a tight checklist to keep the DSM persona on-rails.

## You (2025-08-26T23:15:42.036000+00:00)

before creating the prompt, I have these two references. I'm wondering if they will be helpful inputs for the prompt.













## ChatGPT (2025-08-26T23:16:15.409537+00:00)

Short answer: yes—both are excellent inputs.

**How they help (and how I’ll wire them into the O3 prompt):**

- **Screenshot (DM cockpit-style UI):** we’ll use it as a **layout/interaction anchor**—Path-to-Plan header, quarter/product filters, district > rep cards, on-track/critical chips, and the exception-first scan pattern. In the prompt, I’ll tell the DSM persona to **assess your DM Cockpit against this visual grammar** (scan → spot risk → act), and to recommend tweaks like delta chips, right-rail evidence, and one-click drill-downs.
- **“Regional Manager Metrics” doc:** this will be the **authoritative metric dictionary** and priority map. The prompt will instruct the DSM to treat certain signals as *Vital, Leading*—e.g., **%Reps in Deals** fileciteturn1file1L3-L8, **%Accts w/ active pipe** fileciteturn1file3L13-L18, **Tech Win %** and **POV Win %** fileciteturn1file2L5-L10 fileciteturn1file2L14-L19—and to flag gaps if these aren’t present in the cockpit. It will also use your **causal chain** (coverage → pipeline presence → attainment) when reasoning about what to add or emphasize fileciteturn1file4L31-L36.

**Paste-ready “References” block** (to drop above your DM Cockpit section in the final prompt):
```
REFERENCES FOR EVALUATION
A) Visual Anchor: Use the uploaded cockpit screenshot only as a UX pattern guide (layout, filters, on-track/critical states, rep cards). Do not assume its numbers are correct; it’s a layout reference.
B) Metric Semantics (authoritative):
   - Treat as Vital, Leading: %Reps in Deals; %Accts w/ active pipe; Tech Win %; POV Win %.
   - When these are missing/unclear, recommend where they should live (tile/card) and the action the DSM can take when “red.”
C) Reasoning Heuristic:
   coverage/readiness → pipeline presence → attainment;
   technical quality & exec engagement shift conversion and ASP.
D) Guardrails: Evidence over opinion (Champion/EB, paper path, InfoSec, POV/tech-win). Delta-first. Keep cockpit light; heavier automation in Forecast.
```

If you’re good with that, say **“begin creating the prompt”** and I’ll generate the polished O3 prompt that bakes these references and guardrails in.

## You (2025-08-26T23:18:29.632000+00:00)

begin creating the prompt





## ChatGPT (2025-08-26T23:18:30.564409+00:00)

# O3 Prompt: DSM Review of **DM Cockpit (Summary)**

## 1) Goal
Produce an expert, field-realistic critique of the **DM Cockpit (Summary)** section of a PRD for a Palo Alto Networks District Sales Manager (DSM). Determine what helps a DSM *defend commit on facts*, where the design is thin or risky, and the smallest set of changes that most improves: **WAPE ≤ 8–10% at T-14, Commit Accuracy ≥ 90% at T-7, inspection time ↓ 40%, slip from Commit ↓ 30%.**

## 2) Execution Persona (for O3 to emulate)
You are a **District Sales Manager at Palo Alto Networks** running weekly forecast & inspection in CRM (Salesforce). You manage multiple districts/teams, coach to MEDDPICC, track paper path & InfoSec gates, and care about activation coverage by pillar (**Firewall, CDSS, SASE, Cloud, Cortex**). Your cadence: weekly WoW, quarter-in-flight. Your job is to **scan, spot risk, act**—in minutes, not hours.

## 3) Inputs (paste the subsection + refs)
- **PRIMARY INPUT — DM COCKPIT TEXT**
  Paste the single subsection here:
  ```
  <<<DM_COCKPIT_SECTION>>>
  ```
- **REFERENCE A — Visual Anchor (optional but preferred)**
  A cockpit screenshot/layout reference (filters, path-to-plan header, rep/district strip, on-track/critical chips). Treat this **only as UX grammar**; do **not** trust its numbers.
  ```
  <<<VISUAL_ANCHOR_IMAGE_OR_DESC>>>
  ```
- **REFERENCE B — Metric Dictionary (optional but preferred)**
  Short text listing metric semantics and causal chain (e.g., %Reps in Deals, %Accts w/ Active Pipe, Tech Win %, POV Win %, Median POV Duration; coverage/readiness → pipeline presence → attainment; exec engagement & technical quality shift conversion/ASP).
  ```
  <<<METRIC_DICTIONARY_TEXT>>>
  ```

## 4) Assumptions & Defaults
- Live **inside CRM**; we **unify**, not re-platform.
- **Evidence > opinion**: Commit entries require proof (Champion/EB, Decision Criteria, Paper Path, InfoSec/Legal, POV/Tech-Win).
- **AI modes**: Summarize (variance, drivers), Assist (next actions w/ owner), Automate (low-risk, reversible, auditable).
- **Delta-first** UI: show WoW changes everywhere; exceptions open a right-rail **Evidence & Actions** drawer.
- If a reference is missing, proceed on industry-standard DSM heuristics and **flag assumptions**.

## 5) Analytic Tasks (do all, in order)
1) **DSM Value Snapshot (≤7 bullets)**
   What in this cockpit lets you confirm or defend commit in <5 minutes? Name sections/tiles and why (Path-to-Plan, Activation, Technical Motion, Exceptions, Team strip).
2) **Gap Analysis (prioritized)**
   What’s missing/ambiguous for a decisive weekly inspection? For each gap:
   **Gap • Why it matters • Evidence source (CRM fields/notes, POV, InfoSec) • Best UI affordance (badge/chip/right-rail slot) • Likely impact on WAPE/Commit.**
3) **Metrics & Thresholds Check**
   For each proposed metric (**%Reps in Deals, %Accts w/ Active Pipe, Tech Win %, POV Win %, Median POV Duration** and any others in the input):
   - Is it predictive at DSM level?
   - Propose **RAG bands** (with rationale; mark as *inferred* if based on field heuristics).
   - Specify the **DSM action when red** (owner, due-date, next artifact in evidence trail).
4) **Exception Design Review**
   Do exceptions cover top slip drivers (stale stage, close-date churn, commit w/o Champion/EB, unmapped paper path, InfoSec not started, low POC engagement, renewal ≤120 days w/ negative health)? What **1–2** key exceptions are missing for PANW? For each exception: list the **minimal evidence slots** the right rail must show.
5) **AI Modes Scope & Boundaries**
   - **Summarize:** two weekly questions it must answer (variance + causal drivers).
   - **Assist:** top 3 actions per highest-risk deal, with **owner** (Rep/SE/CSM/DSM) and artifact (email/task/note).
   - **Automate:** what stays in Cockpit (safe, low-risk, undoable) vs what defers to Forecast & Inspection (e.g., call agenda scaffolds).
6) **Adoption & Load**
   Estimate inspection time using this cockpit; identify click/read hotspots and propose **one-tap** fixes. Call out any **new admin work** the design might accidentally create and how to avoid it.

## 6) Return Format (strict)
Output **only** the following Markdown sections, in this order:

**A. Executive Brief (≤120 words)**
- One-paragraph verdict on decision-readiness & forecast integrity.

**B. Scores (0–5)**
- Decision Readiness: _x.x_
- Evidence Rigor: _x.x_
- Forecast Impact: _x.x_
- Activation Coverage: _x.x_
- Exception Handling: _x.x_
- Adoption & Load: _x.x_
_(1–2 sentences total on the biggest score driver.)_

**C. What’s Good (≤5 bullets)**

**D. Gaps & Enhancements (table)**
| Gap | Why it Matters | Evidence Needed | Proposed UI | Expected Impact on WAPE/Commit |

**E. Top 5 Actions to Ship in v1 (ranked)**
For each: **Action • Owner • Effort (S/M/L) • Risk • Why now**

**F. Open Questions (assumptions to resolve)**

**G. Appendix — Metric RAG Bands & Actions**
List each metric with **R/G/A thresholds**, **owner**, and **next step** when red.

> **Do not include your scratchpad or chain-of-thought.** Keep explanations crisp and tied to outcomes.

## 7) Warnings & Guardrails
- If any data or reference is missing, **state the assumption explicitly** and proceed; do **not** fabricate numbers.
- Distinguish **field-proven patterns** from opinion/speculation. Tag speculative items with “_(speculative)_”.
- Tie every enhancement to a measurable outcome (WAPE, Commit accuracy, inspection time, slip).
- **Automation must be reversible and auditable;** any irreversible step is out of scope for Cockpit.
- Respect **scope: DM Cockpit only**; if suggesting a Forecast/Hygiene feature, label it “_belongs in module X_”.

## 8) Evaluation Rubric (for O3 self-check)
- **Decision Readiness:** Can a DSM defend commit in <5 minutes from this cockpit?
- **Evidence Rigor:** Are Commit entries anchored to Champion/EB, Decision Criteria, Paper Path, InfoSec/Legal, POV/Tech-Win?
- **Forecast Impact:** Would the changes plausibly move **WAPE ≤10% (T-14)** and **Commit ≥90% (T-7)**?
- **Activation Coverage:** Do coverage/readiness signals (by pillar) map to pipeline presence & bookings?
- **Exception Handling:** Do exceptions reflect top slip drivers with one-click inspection?
- **Adoption & Load:** Does the design cut **inspection time ~40%** with no net new admin work?

## 9) Final Checklist (O3 must verify before finishing)
- [ ] I used delta-first reasoning and exception-first scanning.
- [ ] Every gap has **why**, **evidence**, **UI**, **impact**.
- [ ] Each metric has **RAG bands** and a **DSM action**.
- [ ] I separated Cockpit vs Forecast/Hygiene scopes.
- [ ] I proposed exactly **Top 5** v1 actions with owner & effort.
- [ ] I stated assumptions for any missing references.

---

### How to use
1) Paste your **DM Cockpit** subsection into `<<<DM_COCKPIT_SECTION>>>`.
2) (Optional) Add the screenshot as `<<<VISUAL_ANCHOR_IMAGE_OR_DESC>>>` and your metric dictionary into `<<<METRIC_DICTIONARY_TEXT>>>`.
3) Run with O3/O1. This will yield a DSM-real review, tightly mapped to your North-star outcomes.

## You (2025-08-27T00:11:32.664000+00:00)

Ok, now I want to do the same with a more refined version of the DM cockpit. No images will be shared, just the brief. Also, make sure that as part of the suggestions, chatGPT does not invent new metrics.

Do not rewrite the brief pasted below in your prompt, leave a placeholder and I will add it myself.
---
# DM Cockpit — Platforms & Drill-Down (v1.4)

## A) Current-Quarter Banner (no filters)

**Purpose:** one-glance velocity + timing.
**KPIs (CQ only):** Total Booked • Open Pipe • Tech Win % • POV Win % • Median POV Duration.    &#x20;

---

## B) Platform Rail (tiles as tabs) — **CDSS · Cortex · Firewall · SASE · Unit 42**

**Local filters:** Quarter | Product (tile selection = Product).
**Each tile shows (per selected platform):**

* **% Reps in Deals** (bar) • **% Accts w/ Active Pipe** (bar). &#x20;
* Optional mini stat (where defined): **% Reps Certified** for that pillar (CDSS NetSec; SASE/Cortex). If the pillar has no certification metric, the chip is hidden. &#x20;

> Note: “pillar blocks” apply the same definitions per product; Unit 42 inherits the same metric logic if data is tagged by that pillar.

---

## C) Regional Performance Table (drives the drill-down)

**Local filters:** Quarter | Product (inherited from the selected tile).
**Columns (region level, all visible at once):**

* **Activation/Coverage:** % Reps in Deals • % Accts Active Pipe • % Reps Certified (if applicable) • # Reps in Seat • % Territories Filled • # Last 3M Attrition.     &#x20;
* **Technical Motion:** Tech Win % • POV Win % • Median POV Duration.  &#x20;
* **Executive Engagement (snapshot):** % Accts w/ CXO (6m / 12m) • #EBCs (done / next 3m) • #EORs (done / next 3m).   &#x20;
* **Context (optional columns you can toggle on):** # Accts • # G2K • White Space • % Accts Active (3y) • % ASR • ATR • % Platformized.      &#x20;

**Behaviors**

* Click a region row to **expand AEs**.
* Sort on any column; sticky first column; “Show Δ” toggle overlays WoW change (display only).

---

## D) AE Drill-Down (within an expanded region)

**Columns (per AE, scoped to selected platform & quarter):**

* Attainment band (YTD) • Has Active Pipe (Y/N) • % Reps Certified (if defined for that pillar) • # Accts per Rep • Tech Win % • POV Win % • Median POV Duration.      &#x20;

**Row actions:** open the rep’s opportunity list (pre-filtered to the pillar & quarter), view exec-engagements, or open coaching pack (separate module; link only).

**Why this composition works:** it mirrors the causal chain already documented—coverage → pipeline presence → conversion/timing → attainment.&#x20;

---

## E) Neutral AI (descriptive only)

A small **“AI Observations”** icon appears on platform tiles and table headers. Clicking shows text like:

* “Observed: **% Reps in Deals (SASE) −8 pts QoQ**, while **POV Win % +5 pts**; **EBCs next 3m +3**.”
  No judgments or prescriptions—just deltas/outliers with pointers to the exact fields in the table/banner. (Matches the vision’s descriptive AI guidance.)&#x20;

---

## F) Interaction sketch (inspired by your screenshot)

1. **User lands** ➜ sees CQ banner.
2. **Chooses a platform tile** (e.g., Cortex) ➜ table rebinds to Cortex metrics for **all regions**.
3. **Scans the table** ➜ sorts by % Reps in Deals to find weak regions.
4. **Expands a region** ➜ sees all AEs at once, with Cortex-scoped activation + technical KPIs and attainment band.
5. Optional: flip to **context toggles** (ASR/ATR/Whitespace) for size-of-prize nuance.

---

## G) Component rules (for design & build)

* **Tiles:** show % Reps in Deals & % Accts Active Pipe; include % Reps Certified chip when defined for the pillar.  &#x20;
* **Tables:** default columns as listed; optional context columns are off by default to protect attention.
* **Filters:** Banner has none; each section owns **Quarter/Product**.
* **States:** empty (show definitions), loading skeletons, error (inline retry).
* **Accessibility:** tiles are tabs; table focus moves on selection; all metrics have tooltips echoing your doc definitions.





## ChatGPT (2025-08-27T00:11:35.817447+00:00)

# O3 Prompt: DSM Review of **DM Cockpit — Platforms & Drill-Down (v1.4)**

## 1) Goal
Deliver an expert, field-realistic critique of the **Platforms & Drill-Down** cockpit for a Palo Alto Networks District Sales Manager (DSM). Determine what enables fast commit defense and coaching, where the design is thin or risky, and the **smallest high-leverage changes** that improve: **WAPE ≤ 8–10% (T-14), Commit Accuracy ≥ 90% (T-7), inspection time ↓ 40%, slip from Commit ↓ 30%.**

## 2) Execution Persona (for O3 to emulate)
You are a **Palo Alto Networks DSM** running weekly forecast/inspection in CRM. You manage regions and AEs across **CDSS, Cortex, Firewall, SASE, Unit 42**. You coach to MEDDPICC, watch paper path & InfoSec gates, and care about platform adoption by pillar. You operate **delta-first**: scan → spot risk → act in minutes.

## 3) Inputs (paste only; do not rewrite)
- **PRIMARY INPUT — DM Cockpit v1.4 Brief**
```
<<<PASTE_DM_COCKPIT_V1_4_BRIEF_HERE>>>
```
- **OPTIONAL — Metric Dictionary / Definitions (semantics only; no new metrics)**
```
<<<PASTE_METRIC_DEFINITIONS_IF_AVAILABLE>>>
```

## 4) Scope & Constraints (read carefully)
- **No new metrics.** Use **only** metrics explicitly present in the brief and/or optional definitions.
  - Allowed: layout/interaction changes, grouping, sort/filter behavior, delta/outlier flags, tooltips, evidence slots, thresholds/bands **for existing metrics only**.
  - Not allowed: proposing additional columns, KPIs, composite/derived metrics, or renaming metrics.
- **Module boundaries:** This prompt covers **Banner, Platform Rail, Regional Table, AE Drill-down, Neutral AI**. If suggesting Forecast/Hygiene features, label them “_belongs in module X_”.
- **AI behavior here is descriptive only** (observations/deltas/outliers with pointers), not prescriptive.

## 5) Analytic Tasks (perform all, in order)
1) **Decision Snapshot (≤7 bullets)**
   How a DSM would confirm/defend commit in <5 minutes using: **CQ Banner → Platform tile → Regional table → AE drill-down**. Call out why each step matters.
2) **Platform Rail Review**
   Does per-platform scanning of **% Reps in Deals** and **% Accts w/ Active Pipe** (and **% Reps Certified** where defined) surface weak regions fast enough? Recommend tab/tiles, sorting, and delta overlays **without introducing new metrics**.
3) **Regional Table Usability**
   Assess column set (activation/coverage, technical motion, exec engagement, optional context). Propose ordering, default sorts, sticky/Δ-toggle behavior, and attention safeguards. Keep all proposals within existing columns.
4) **AE Drill-down for Coaching**
   Evaluate whether AE-level columns (attainment band YTD, has active pipe, certification, accts/rep, tech/POV metrics) enable actionable coaching in 1–2 clicks. Suggest row actions/navigation and evidence slots—**no new KPIs**.
5) **Neutral AI (Descriptive) Scope**
   Specify the exact deltas/outlier patterns (WoW/QoQ) it should surface **using only existing metrics**, and how to point to the source fields (banner/table). No judgments or prescriptions here.
6) **Adoption & Load**
   Estimate inspection time and identify click/read hotspots. Propose one-tap fixes (e.g., default sorts, presets, saved views, sticky first column, tooltip definitions).

## 6) Return Format (strict)
Produce **only** the sections below, in order:

**A. Executive Brief (≤120 words)**
Verdict on decision-readiness and where the design most boosts forecast integrity.

**B. Scores (0–5)**
- Decision Readiness: _x.x_
- Platform Scan Efficacy: _x.x_
- Table/Drill-down Clarity: _x.x_
- Forecast Impact: _x.x_
- Adoption & Load: _x.x_
_(1–2 sentences on the main score driver.)_

**C. What’s Working (≤5 bullets)**

**D. Gaps & Enhancements (table; no new metrics)**
| Gap | Why it Matters | Uses Which Existing Metric(s) | Proposed UI/Behavior (not a new KPI) | Expected Impact on WAPE/Commit/Time |

**E. Top 5 Actions to Ship in v1 (ranked)**
Each: **Action • Owner • Effort (S/M/L) • Risk • Why now**
_(Actions must reference only existing metrics.)_

**F. Open Questions for PM**
Assumptions/ambiguities to resolve (definitions, data freshness, filter precedence, etc.).

**G. Appendix — RAG Bands & Triggers (existing metrics only)**
For each metric already in the brief: **Red/Amber/Green thresholds (clearly marked “assumed” if heuristic), owner, and the next UI step** when red (e.g., open evidence drawer, jump to opp list).

**H. Metric Integrity Check (required)**
- List every metric referenced in your suggestions.
- Confirm each appears in the pasted brief (Yes/No).
- Statement: **“No new metrics introduced: Yes/No.”**

> Do not include chain-of-thought. Keep explanations crisp and outcome-tied.

## 7) Guardrails
- **Absolutely no new metrics or renames.** If something feels missing, offer a **layout/interaction** workaround or tag as “_belongs in another module_”; do **not** add a KPI.
- If a metric definition is unclear, **state the assumption** and proceed; do not fabricate semantics.
- Keep AI to **descriptive observations** only in this module.
- Tie every enhancement to a measurable outcome (WAPE, Commit accuracy, inspection time, slip).

## 8) Evaluation Rubric (for O3 self-check)
- Can a DSM validate exposure and drill to owners in <5 minutes using the existing metric set?
- Do proposed changes improve scan quality across platforms without adding metrics?
- Are table defaults and drill-downs obviously useful for weekly inspection/coaching?
- Would the changes plausibly improve **WAPE ≤10% (T-14)** and **Commit ≥90% (T-7)**?
- Does the design reduce inspection time with zero net new admin work?

## 9) Final Checklist (O3 must verify before finishing)
- [ ] I used only metrics present in the pasted brief (and optional definitions).
- [ ] I introduced **no new metrics** or renames.
- [ ] Each gap includes **why**, **existing metric(s) used**, **UI/behavior**, **impact**.
- [ ] I kept AI suggestions **descriptive** and pointed to source fields.
- [ ] I proposed exactly **Top 5** v1 actions with owner & effort.
- [ ] I stated assumptions where definitions were missing or unclear.

## You (2025-08-27T00:14:28.356000+00:00)

what is WAPE

## ChatGPT (2025-08-27T00:14:29.217680+00:00)

WAPE stands for **Weighted Absolute Percentage Error**.

It’s a forecasting accuracy metric that tells you, on average, **how far off your forecast is from actuals**, weighted by the size of each forecast item.

### Formula
\[
WAPE = \frac{\sum |Actual - Forecast|}{\sum Actual}
\]

- **Numerator**: total absolute error across all items (e.g., deals, bookings).
- **Denominator**: total actuals.
- **Result**: expressed as a percentage.

### Example
If you forecast \$10M but actuals are \$9M, error = \$1M.
If you forecast \$4M but actuals are \$6M, error = \$2M.
Total error = \$3M.
Total actuals = \$15M.
\[
WAPE = 3/15 = 20\%
\]

###
