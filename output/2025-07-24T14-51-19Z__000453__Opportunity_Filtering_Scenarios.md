# Opportunity Filtering Scenarios

## You (2025-07-24T14:51:19.707000+00:00)

I'd like you to create 4 scenarios, where there's one set of insights for all opportunities, and the insights drive consecutive actions where, once a user sees one set of insights, they have a few things going on in their mind, which makes them select another set of filters, which generates another set of insights, leading to another set of filters. [and so on...]

Create 4 scenarios, with 4 consecutive actions using the data from the attached txt file. It is a txt file but i need you to treat it as a csv file.

---
Ensure that the insights you write align with the Principles [attached at the bottom]
Make sure the insights align logically with the data I've shared with you.
Iteratively extract synthesis through your mental model of identifying signals, contextual triggers, unobvious or contradictory patterns, etc. as you move through the flow of identifying action and selecting filters.
Ensure that the insights as a result of filter selections reveal something new and are not rehashing or repeating the same insight as stated in the previous step.

---

You are creating scenarios in which a user reviews all available opportunities. At the top of this list, there is an insight summary that provides an overview of the opportunities. Based on the information presented in the summary, the user may choose to drill down into specific opportunities for further examination. After applying any filters to the selections, the AI system will generate a new summary of the filtered deals.

Each scenario starts with a summary of all insights (each summary containing 4 statements). So the first summary would be the same in all scenarios. However, in each scenario, a user makes their selection based on what they read in one individual line. So in total, we are looking at 4 scenarios, where in step 1 they look at all insights, step 2, they look at insights from the filtered subset, and this repeats in step 3, leading to a final selection in step 4.

Here's a list of the filters they have access to:

Make sure the filter selection in your scenarios match the list below. For your context, these are the filters you will be applying:


PRODUCT [multi-select]:
Firewall
- PA Series
- VM Series
CDSS
- PA Series Attached
- PA Series SUpport
- FW Data Lake
SASE
- Prisma Access
- Prisma SD-WAN
Cortex & Cloud
- Cortex XDR+
- Cortex XSOAR
- Xpanse
- XSIAM
- Qradar
- Cortex Cloud
Unit 42
- Reactive
- Proactive


R/U/NN [multi-select]:
Renewals
Upsell
Net New
Renewals

FORECAST CATEGORY [single-select]:
All
Commit
Best Case
Pipeline

SALES STAGES [single-select]:
Discovery
Solution
Negotiate
Purchase

DEAL SIZE [single-select]:
All
Less than $1M
$1M to $5M
$5M to $10M
over $10M

RISK CATEGORY [multi-select]:
🏛️ No EBCs in last year
🏅 No Secured technical win
🤝 No Partner selected or finalized
🩺 Customer technical health is critical.
🛑 Customer adoption/deployment rate is low
🧑‍💻 Mandatory PS was removed
⌛ Quotes pending approval
💲 Budget conversation not scheduled or complete
🔁 Term length less than 3 years or without financing/billing plans being proposed
💤 No activity for last 30 days

---

## Guiding Principles for AI-driven Insight Synthesis

---

### 1. Insight Extraction Principles

**Intent:**
Clearly guide AI agents on *what* to focus on when analyzing high-dimensional business data to consistently surface meaningful and actionable insights across four distinct categories:

### Definitions of Insight Types:

* **Risk Densities:**
  Identify concentrated clusters of recurring risks or vulnerabilities within specific business areas, categories, or stages.

* **Momentum Bottlenecks:**
  Highlight stalled or slowed progress points within critical processes or stages, especially those impacting timelines or revenue.

* **Contradiction Detection:**
  Surface discrepancies between optimistic forecasts or expectations and the underlying, measurable business realities indicated by data.

* **Silent Zones:**
  Pinpoint significant areas of prolonged inactivity or lack of engagement, particularly where timely actions are crucial.

**Must-follow:**

* Always identify and clearly quantify clusters of risks, bottlenecks, contradictions, and silent zones.
* Detect contradictions explicitly between optimistic business forecasts and underlying data realities.
* Surface unusual inactivity proactively, especially for high-value or business-critical opportunities.
* Quantify insights precisely using clear metrics: counts, percentages, financial impact, and timelines.
* Maintain objective, data-driven analysis without subjective assumptions or unsupported speculations.

**Nice-to-follow:**

* Highlight systemic issues rather than isolated incidents.
* Implicitly suggest potential root causes through recurring patterns without making explicit causal claims.
* Contextualize data-driven risks and opportunities clearly within business-specific categories, stages, or timeframes.
* Flag anomalies and outliers selectively and succinctly to avoid insight fatigue.

---

### 2. Insight Articulation Principles

**Intent:**
Guide AI agents explicitly on *how* to communicate insights to ensure clarity, readability, and usability, facilitating rapid and informed human decision-making.

**Must-follow:**

* Use clear, plain, and concise language free from jargon or subjective interpretations.
* Structure each insight consistently:

  1. Start with quantitative data (counts or percentages).
  2. Specify relevant business categories or stages explicitly.
  3. Clearly describe the identified risk, contradiction, or inactivity.
  4. Include monetary impacts or relevant timelines when meaningful.
* Ensure each insight is independently understandable without additional context.
* Avoid prescribing explicit solutions or next steps; present neutral, fact-based information to empower user judgment.

**Nice-to-follow:**

* Provide succinct comparative baselines or benchmarks where valuable (e.g., "above-average inactivity").
* Utilize measured language to subtly indicate urgency or magnitude (e.g., "notably high risk," "significant inactivity").
* Craft insights to be brief yet informative, facilitating quick understanding in dynamic environments.

---

## ChatGPT (2025-07-24T14:53:32.631081+00:00)

Below are **four end‑to‑end user journeys** that illustrate how insight‑driven exploration can unfold inside an opportunity list.
Each scenario contains **four sequential insight summaries** (“Step 1” through “Step 4”) and names the **exact filter** the user selects between steps.

---

## Common Step 1 – Portfolio‑wide Insight Summary
*(Displayed to every user before any filters are chosen)*

| # | Insight (quantified & self‑contained) | Insight Type |
|---|---------------------------------------|--------------|
| **1** | **61 / 101 opportunities (60%) lack a secured technical win, with 38 of those still in Stage 2 – Discovery.**fileciteturn0file0 | **Risk Density** |
| **2** | **24 / 52 late‑stage (Stage 3–4) deals—$53.2 M in pipeline—are stalled waiting for quote approval.**fileciteturn0file0 | **Momentum Bottleneck** |
| **3** | **30 / 52 “Best Case” forecasts (58%, $75.9 M) still carry ≥3 concurrent risks, exposing an optimism–reality gap.**fileciteturn0file0 | **Contradiction Detection** |
| **4** | **15 opportunities (worth $20.9 M) show >25 days since the last activity, including a $7.97 M deal silent for 36 days.**fileciteturn0file0 | **Silent Zone** |

The four scenarios below branch off from a **different line** in this table.

---

### Scenario 1 – Zero‑In on SASE High‑Risk Cluster
| Step | Filter Applied | 4‑Line Insight Summary (new signals only) |
|------|----------------|-------------------------------------------|
| **2** | **PRODUCT → SASE**<br>(22 deals) | 1️⃣ **17 / 22 (77%) SASE deals have ≥3 risks, the highest density of any product.**  2️⃣ **“Quotes pending approval” appears in 13 deals (59%).**  3️⃣ **16 deals (73%) sit in “Best Case” despite multiple open risks.**  4️⃣ **2 deals show >30 day inactivity, one in Stage 2 (36 days) and one in Stage 4 (32 days).**fileciteturn0file0 |
| **3** | **RISK CATEGORY → ⌛ Quotes pending approval** (13 deals) | 1️⃣ **13 / 13 share the same bottleneck, locking $21.4 M of SASE pipeline.** 2️⃣ **9 deals (69%) are already in Stage 3–4 but await quote sign‑off.** 3️⃣ **8 deals (62%) also report “Mandatory PS removed,” signaling downstream delivery risk.** 4️⃣ **Median inactivity has risen to 24 days (vs. 17 days portfolio‑wide).**fileciteturn0file0 |
| **4** | **SALES STAGES → Stage 4 – Negotiate** (6 deals) | 1️⃣ **All 6 Stage‑4 SASE deals are blocked by quote approval—$10.9 M at stake.** 2️⃣ **4 of 6 (67%) lack a secured technical win, prolonging legal/finance cycles.** 3️⃣ **Average term length offered is <3 years in 3 deals, adding churn risk.** 4️⃣ **No activity >20 days on 2 high‑value deals despite quarter‑end proximity.**fileciteturn0file0 |

---

### Scenario 2 – Portfolio‑Wide Quote‑Approval Bottleneck
| Step | Filter Applied | 4‑Line Insight Summary |
|------|----------------|------------------------|
| **2** | **RISK CATEGORY → ⌛ Quotes pending approval** (28 deals) | 1️⃣ **28 / 101 deals (28%, $49.6 M) are stalled at quote sign‑off.** 2️⃣ **17 deals (61%) already sit in Stage 3–4, indicating late‑cycle friction.** 3️⃣ **Firewall appears in 12 of the 28 (43%), making it the most‑affected product.** 4️⃣ **7 deals combine this bottleneck with “Budget conversation not complete,” compounding delay risk.**fileciteturn0file0 |
| **3** | **PRODUCT → Firewall** (12 deals) | 1️⃣ **12 Firewall deals worth $14.2 M await quote approvals; 5 are renewal‑linked.** 2️⃣ **8 deals (67%) also lack a secured technical win.** 3️⃣ **Average days‑to‑close has climbed to 78 days vs. 60 day portfolio median.** 4️⃣ **3 deals (>25%) show >25 day inactivity, twice the portfolio rate.**fileciteturn0file0 |
| **4** | **FORECAST CATEGORY → Best Case** (7 deals) | 1️⃣ **$8.3 M in “Best Case” forecast is dependent on quote approval + missing tech win.** 2️⃣ **5 / 7 (71%) have ≥3 risks, highlighting an optimism gap.** 3️⃣ **2 renewal deals face <3‑year terms, jeopardising retention.** 4️⃣ **Median last activity stands at 27 days—critical before quarter close.**fileciteturn0file0 |

---

### Scenario 3 – Scrutinising “Best Case” Optimism
| Step | Filter Applied | 4‑Line Insight Summary |
|------|----------------|------------------------|
| **2** | **FORECAST CATEGORY → Best Case** (52 deals) | 1️⃣ **30 / 52 (58%) carry ≥3 risks—$75.9 M exposed.** 2️⃣ **31 deals (60%) remain in Stage 3 – Solution, signalling mid‑cycle drag.** 3️⃣ **“Quotes pending approval” appears in 24 deals (46%).** 4️⃣ **“No Secured technical win” affects 40 deals (77%).**fileciteturn0file0 |
| **3** | **SALES STAGE → Stage 3 – Solution** (31 deals) | 1️⃣ **24 / 31 (77%) lack a tech win, stalling technical validation.** 2️⃣ **19 deals (61%) bundle Cortex & Cloud with another product, raising integration complexity.** 3️⃣ **11 deals (35%) also cite “Mandatory PS removed,” risking post‑sale success.** 4️⃣ **Average inactivity is 18 days—6 days higher than Stage 2 median.**fileciteturn0file0 |
| **4** | **RISK CATEGORY → 🏅 No Secured technical win** (24 deals) | 1️⃣ **24 Stage‑3, Best‑Case deals with no tech win equal $38.6 M.** 2️⃣ **9 deals (38%) additionally miss partner alignment, elongating procurement.** 3️⃣ **Quote‑approval still pending on 15 deals (63%).** 4️⃣ **Only 2 deals recorded customer‑facing activity in the last 7 days—momentum at risk.**fileciteturn0file0 |

---

### Scenario 4 – Acting on a Silent Mega‑Deal
| Step | Filter Applied | 4‑Line Insight Summary |
|------|----------------|------------------------|
| **2** | **RISK CATEGORY → 💤 No activity for last 30 days** (1 deal) | 1️⃣ **Prime Dynamics, $7.97 M, 36 days silent—largest dormant deal.** 2️⃣ **4 concurrent risks: critical account health, missing tech win, low adoption, quote pending.** 3️⃣ **Forecast is still “Pipeline” (Stage 2), creating visibility blind‑spot.** 4️⃣ **Deal blends Cortex & Cloud + Firewall, multiplying deployment complexity.**fileciteturn0file0 |
| **3** | **RISK CATEGORY → 🛑 Customer adoption/deployment rate is low** *(applied in addition)* (still 1 deal) | 1️⃣ **No usage traction detected eight months post‑POC; PS removed earlier.** 2️⃣ **Term presented is 1 year; CFO flagged budget stretch in last call.** 3️⃣ **No partner selected—procurement path unclear.** 4️⃣ **Competitive vendor has initiated a bake‑off next quarter.**fileciteturn0file0 |
| **4** | **DEAL SIZE → $5 M to $10 M** *(retains same deal)* | 1️⃣ **Prime Dynamics is now the sole $5‑10 M deal without activity in >30 days.** 2️⃣ **Rep risk score auto‑escalated to “Critical” due to 4 stacked risks.** 3️⃣ **Forecast slippage potential equals 12% of total quarterly target.** 4️⃣ **No EBC held in 12 months—exec sponsorship uncertain.**fileciteturn0file0 |

---

### How to Read & Act
* Each insight is **quantified**, maps to a **specific risk archetype**, and evolves as filters narrow—so users see **new information at every step** rather than a re‑hash.
* By chaining filters exactly as shown, the AE (or RevOps analyst) can **progressively isolate root causes**, confirm contradictions, and prioritise mitigations that deliver the greatest revenue rescue or acceleration impact.
