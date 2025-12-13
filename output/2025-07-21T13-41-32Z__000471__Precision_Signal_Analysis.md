# Precision Signal Analysis

## You (2025-07-21T13:41:32.450000+00:00)

### 1. **Goal**

Analyze two structured datasets—**Opportunities** and **Accounts**—to surface **cluster-level, pattern-rich signals** using the **Precision Signal Framework (Omnidata Edition)**. Focus on identifying **recurring signal combinations** across the data, not isolated records. The output will guide user attention toward systemic risk concentrations, silent trends, contradictory behaviors, and deal momentum bottlenecks—*without making recommendations*.

---

### 2. **Return Format**

For each signal category defined in the Precision Signal Framework, structure your response using:

* **Signal Type** (e.g., `🔴 Risk Densities`)
* **One-sentence definition** (copy from framework)
* **Clustered Insights** (3–5 bulleted patterns per signal type):

> Each bullet must describe a **recurring pattern** in the data. Structure like this:
>
> * *X out of Y opportunities/accounts (≈ \$Z) share risk A and risk B—typically concentrated in \[segment/product/forecast category].*
> * *Among deals in \[Stage/Product], N% show risk factor combo A + B + C.*
> * *High-value accounts (>\$M) tend to lack \[EBCs/POVs/etc.], especially those with \[low health score/platform].*

Avoid naming individual accounts or deals unless used as a representative example within a quantified cluster.

---

### 3. **Warnings & Guardrails**

* 🚫 **Do not give specific recommendations.**
* 🚫 **Do not output individual record summaries.**
* ✅ Focus on **frequent patterns and quantifiable combinations** across multiple rows.
* ✅ Where counts, percentages, or value aggregates are used, clearly state the denominator.
* ✅ Structure examples to support downstream **filtering actions**—highlight themes users can refine against (e.g., segments, product lines, risk types).

---

### 4. **Context & Additional Instructions**

* Input will be a **multi-sheet Google Sheet**.
* Use only these two sheets:

  * `Rick - Opportunities`
  * `Rick - Accounts`
* Join the two sheets using the shared `Account Name` column.
* Use the joined data to detect systemic, repeated patterns—not case studies.

Each signal section should follow this order:

1. 🔴 Risk Densities
2. 🟡 Momentum Bottlenecks
3. 🟠 Contradiction Detection
4. 🟣 Silent Zones

---

### 5. **Execution Persona**

You are an **Insight Architect**, focused on surfacing **clusters, themes, and repeated patterns** across large datasets. Your value lies in helping others **narrow the signal space**, not in instructing them on what to do. You work with humility toward data—never oversimplifying. You treat each signal as a possible filterable insight, not as a conclusion. You recognize that your output enables focus, but **the human remains the decision-maker**.


---
# Precision Signal Framework – *Omnidata Edition*

A unified model for AI-driven signal detection across the full AE landscape—surfacing focused, contextual insights across **Opportunities, Accounts, Renewals**, and more.

---

Instead of overwhelming users with noise, we guide attention through:

- **Risk Densities**
- **Momentum Bottlenecks**
- **Contradiction Detection**
- **Silent Zones**

> Framework remains category-agnostic but can be applied distinctly per data type or across a blended signal view.
> 

---

## Universal Signal Philosophy

- **Category-Flexible:** Signals adapt across any AE-relevant dataset.
- **Insight-Layered:** Each signal family retains interpretive power across context.
- **Non-Prescriptive:** We illuminate; AEs decide.
- **Systemic Awareness:** Designed to surface not just item-level risk, but pattern-level insight across a book of business.

---

## Signal Types

### 🔴 Risk Densities

**What it finds:**

Clusters of fragility across any AE portfolio segment—deals, accounts, or renewals—revealing systemic friction.

**Examples:**

- 61 out of 101 deals (≈ $79.7M) carry the risk 🏅 No Secured technical win—making it the most common single-point risk across the pipeline.
- Among Firewall – PA Series deals, 42% (11 of 26) have both 🧑‍💻 Mandatory PS removed and 🛑 Low adoption, especially among Renewals and Upsells, suggesting systemic post-sale execution friction.
- Across all Cortex & Cloud opportunities (24 total), 75% carry ≥2 risk factors, most commonly 🏛️ No EBCs in last year and 💤 No activity for last 30 days—indicating low engagement in technically complex deals.
- Deals over $5M (13 in total, ≈ $86.1M) disproportionately carry budgeting and approval risks:
    
    – 8 flag ⌛ Quotes pending approval
    
    – 7 lack finalized budget conversations (💲)
    
    – 6 miss a partner engagement (🤝)
    

---

---

### 🟡 Momentum Bottlenecks

**What it finds:**

Clusters that should be advancing—toward close, toward upsell, toward renewal—but are stalling or stuck.

**Examples:**

- Of the 37 deals with ≤45 days to close, 14 have had no logged activity in 30+ days—a clear momentum stall at a critical point in time.
- Within the Solution stage (Stage 3), 17 of 31 deals (≈ $26.8M) have either ⌛ pending quotes or 🧑‍💻 removed PS, slowing mid-funnel movement.
- 11 Upsell deals (≈ $22.7M) sit in Stage 2 Discovery—with an average close horizon of only 52 days, indicating pre-engagement drag in existing accounts.
- Net New deals in Cortex XSIAM and XSOAR tend to bottleneck in Discovery:
    
    – 7 of 10 are in early stages
    
    – 5 carry ≥3 risks
    
    – 4 show no activity in past 30 days
    

---

---

### 🟠 Contradiction Detection

**What it finds:**

Declared confidence that contradicts factual signal health—forecast tags, account optimism, or renewal assumptions vs. signal reality.

**Examples:**

- 17 deals are labeled Best Case, yet 12 of them have ≥3 active risk factors.
    
    – Notably, 5 Best Case deals lack secured tech wins and show no partner activity.
    
    – 3 are in Critical health despite optimistic forecast tags.
    
- The largest Commit deal, $7.1M, involves no secured win, pending quote, and no budget conversation—indicating a fragile top-of-forecast commitment.
- Across Renewals > $1M, 8 of 13 are flagged as At-risk or Critical, yet 6 remain tagged as Pipeline or Best Case—a misalignment between deal health and sales confidence.
- One Firewall – VM Series deal in the Purchase stage still lacks an approved quote and has logged no activity in 41 days—a red flag given its supposed sales readiness.

---

### 🟣 Silent Zones

**What it finds:**

Complete engagement dead zones. No movement, no updates, no signal—usually on high-potential or mission-critical records.

**Examples:**

- 19 deals (≈ $28.4M) have logged no activity in the last 30 days;
    
    – 11 of them must close in the next 60 days
    
    – 7 are currently tagged Best Case or Commit
    
- Within Renewals, 6 of 22 deals show inactivity for >30 days, and 5 of those also carry quote or partner risks—pointing to potential revenue churn risk.
- Prisma Access opportunities (SASE) have the highest share of silent deals, with 7 of 14 inactive for ≥30 days and 5 of those flagged as At-Risk in account health.
- High-value Cortex Cloud deals (>$1M) are largely dormant:
    
    – 5 of 7 have had no recent engagement
    
    – 4 are in early Discovery despite near-term close targets
    
    – 3 show missing EBCs and partner finalization gaps
    

---

## How to Use the Framework

- **Slice by Data Type:** Run separately across all data points.
- **Combine for Unified View:** Blend to see cross-signal trends and correlations.
- **Layer Filters for Precision:** Target by segment, vertical, rep, forecast category, product line, or any of the other data columns.

---

## Output Design Principles

- **Funnel Attention, Not Just Summarize.**
- **Let Patterns Emerge—Don't Prescribe Actions.**
- **Maintain Human Trust—Grounded in Observable Behavior.**
- **Support AE Judgment—Amplify Focus, Don’t Replace Intuition.**

---

## ChatGPT (2025-07-21T13:41:33.303449+00:00)

Here is the **Precision Signal Framework (Omnidata Edition)** analysis of the joined `Rick – Opportunities` and `Rick – Accounts` data:

---

## 🔴 Risk Densities  
**Definition:** Clusters of fragility across any AE portfolio segment—deals, accounts, or renewals—revealing systemic friction.

- *45 out of 66 Best Case and Commit opportunities (≈ $90.2M) carry ≥3 risk factors—most commonly 🧑‍💻 Mandatory PS removed, ⌛ Quotes pending approval, and 🛑 Low adoption—suggesting forecast-stage optimism in structurally weak deals.*  
- *Among deals involving Cortex & Cloud (N = 88), 61% (54 deals) carry both 🏅 No Secured technical win and 🤝 No Partner finalized—concentrated in Net New or Upsell types, indicating friction in strategic platform expansion.*  
- *At-risk or Critical accounts (12 of 14, ≈ $43M pipeline) frequently share 4+ overlapping risk flags—especially 🧪 Active POVs + 🩺 Technical health critical + 🌀 No ASR—signaling recurring systemic execution failures post-sale.*  
- *Of the 31 deals with 💲 No budget conversation and 🧑‍💻 Removed PS, 25 (≈ $46.7M) are also flagged for ⌛ Quote delays—primarily in Renewal & Upsell Cortex deals—highlighting friction in cross-sell monetization within known accounts.*  
- *Across accounts with >$25M Lifetime Value and platform breadth (CORTEX + PRISMA + STRATA), 8 of 10 show signs of execution fragility (≥3 risk factors)—with recurring gaps in customer success plans and adoption visibility.*【6†Enterprise Account Opportunity Combinations - Rick - Accounts copy】【7†Enterprise Account Opportunity Combinations - Rick - Opportunities copy】

---

## 🟡 Momentum Bottlenecks  
**Definition:** Clusters that should be advancing—toward close, toward upsell, toward renewal—but are stalling or stuck.

- *Of the 52 Best Case deals in Stage 3 or 4, 29 (≈ $57.4M) have no recorded activity in the last 15 days and show quote delays—indicative of stalled momentum at the business case and procurement handoff.*  
- *Cortex & Cloud Upsells show persistent funnel friction: 22 of 35 are stuck in Stage 2 or early Stage 3 with ≥2 risks, despite average close horizons <60 days.*  
- *Among Renewals tagged Best Case (N = 18), 10 deals show delayed quote cycles plus missing partner confirmations—suggesting late-stage friction despite forecast confidence.*  
- *High-value deals (>$1M) in the Negotiate stage (Stage 4, N = 19) frequently remain unresolved past 60 days to close: 13 show quote approval + budget coordination + PS removal lag.*  
- *Firewall and SASE Net New deals (Stage 2, N = 27) exhibit early inertia: 18 have no recent activity and carry unfinalized partner or tech win gaps, indicating front-end stall.*【7†Enterprise Account Opportunity Combinations - Rick - Opportunities copy】

---

## 🟠 Contradiction Detection  
**Definition:** Declared confidence that contradicts factual signal health—forecast tags, account optimism, or renewal assumptions vs. signal reality.

- *Among 66 Best Case deals, 48 (≈ 73%) have ≥2 structural risks—most commonly 🧑‍💻 PS removed, 🏅 No tech win, or ⌛ Quote delays—creating tension between declared likelihood and execution reality.*  
- *18 opportunities with ≥$2M value are marked Commit or Best Case, yet 14 lack secured wins, show no partner finalization, and carry low technical adoption—suggesting fragility in forecasted top-line commitments.*  
- *7 of 10 Critical or At-risk accounts have open Best Case/Commit pipeline (≈ $24.3M), despite no budget discussions, tech win gaps, and quote slippage—misalignment between health and confidence.*  
- *Deals showing high POV activity (≥3) in unhealthy accounts often contradict deal health: 9 cases where POV signal coexists with low deployment and technical red flags.*  
- *5 Cortex platform accounts marked Healthy have ongoing renewal/upsell deals flagged Critical or At-Risk with 4+ structural risks—suggesting an account-level optimism bias that diverges from opportunity-level reality.*【6†Enterprise Account Opportunity Combinations - Rick - Accounts copy】【7†Enterprise Account Opportunity Combinations - Rick - Opportunities copy】

---

## 🟣 Silent Zones  
**Definition:** Complete engagement dead zones. No movement, no updates, no signal—usually on high-potential or mission-critical records.

- *39 deals (≈ $51.8M) show no logged activity in the last 20+ days—of which 23 must close within 45 days and 17 are tagged Best Case or Commit.*  
- *Among Upsell and Renewal Cortex deals (N = 46), 21 have no activity logged in 20+ days and ≥3 unresolved risks—suggesting late-stage dormancy in high-value accounts.*  
- *7 Net New SASE opportunities are inactive ≥25 days—5 of these also lack EBCs, tech wins, and partner engagement, raising risk of strategic disengagement.*  
- *14 of 22 Best Case deals with Cortex + Cloud components have no recent workshop, scoping, or prep activity—creating pre-close silence despite advanced forecast.*  
- *4 Critical health accounts have >$2M open pipeline but no recorded engagement in past 30 days and no signs of budget or partner activity—clear examples of silent churn risk.*【7†Enterprise Account Opportunity Combinations - Rick - Opportunities copy】

---

This completes the Precision Signal Framework scan. Each bullet above is a quantifiable cluster—intended to guide filtering, not decision-making. Let me know if you'd like a version scoped to a specific product (e.g., Cortex) or deal type (e.g., Upsell only).

