# Signal Detection Framework

## You (2025-07-21T13:32:12.567000+00:00)

### 1. **Goal**

Synthesize signals across two distinct datasets—**Opportunities** and **Accounts**—to detect **cross-table patterns and clusters** according to the **Precision Signal Framework (Omnidata Edition)**. The aim is to surface focused, context-aware signals across accounts and deals, without offering guidance or recommendations, while preserving user interpretability and autonomy.

---

### 2. **Return Format**

The output should strictly follow the **Precision Signal Framework** structure (which will be provided separately in the input), using the following layout for each section:

* Signal Type (e.g., **🔴 Risk Densities**)
* What it finds: \[Use the definition already provided in the framework]
* Examples:

  * Each example should be drawn **directly from the joined view** of the opportunities and accounts CSVs.
  * Include realistic, observable combinations of data features from both files.
  * Format each example as a concise bullet with inline data values (e.g., “Deal XYZ (\$2.1M) marked Commit with no POVs, no EBCs, and zero ASR.”)

Return four sections:

1. 🔴 Risk Densities
2. 🟡 Momentum Bottlenecks
3. 🟠 Contradiction Detection
4. 🟣 Silent Zones

If no signal is found in a category, state: No signal detected in this category.

---

### 3. **Warnings & Guardrails**

* 🚫 **Do not make recommendations.**
* 🚫 **Do not suggest actions or remediation.**
* 🚫 Do not summarize overall file contents.
* ⚠️ Ensure signal examples are **specific, pattern-based**, and **traceable to real rows** in the data.
* ✅ Prioritize **signals that span both tables** (e.g., high pipeline in opportunities but zero engagement in accounts).
* ✅ You may hypothesize **data-driven scenarios**, but only if grounded in attributes across both tables.
* ✅ Output must maintain interpretive neutrality and avoid subjective tone.

---

### 4. **Context & Additional Instructions**

* You will be given **two CSV files**:

  * One with opportunity-level data (deal-level rows)
  * One with account-level attributes
* The two tables share a common field: Account Name
* You should perform a **light join** on Account Name to allow multi-table context analysis.
* You are **not to provide row-by-row output**; instead, generate examples **illustrative of cross-patterns** that match the Framework’s four signal types.

---

### 5. **Execution Persona**

You are operating as a **Pattern-Signal Synthesist**—an AI model configured to detect **signal constellations across datasets**. You do not advise. You do not assume strategy. Your role is to **observe, correlate, and expose**. You value **integrity, clarity, and user empowerment**, using only the data given to craft focused examples. Your intelligence lies in seeing patterns, not prescribing paths.

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















































## ChatGPT (2025-07-21T13:35:33.803883+00:00)

### 🔴 **Risk Densities**
**What it finds:** Clusters of fragility across any AE portfolio segment—deals, accounts, or renewals—revealing systemic friction.

**Examples:**
- **Cyberdyne Systems** — Account pipeline **\$9.4 M** spans two Best Case upsell deals (**\$7.16 M** & **\$2.27 M**); both lack partner selection and show low adoption, while the account itself is **At-Risk** with critical technical health. fileciteturn0file0turn0file1
- Seven Net-New **Firewall** Discovery deals (Atlas Bank \$1.01 M, Blue Horizon \$0.67 M, BlueSun \$0.60 M, Evergreen Global \$1.10 M, GreenLeaf Pharma \$0.63 M, Redwood Group \$0.69 M, Wayne Enterprises \$0.96 M) all share “🏅 No Secured technical win” + “🤝 No Partner” risks—concentrating **\$5.7 M** of early-stage pipeline around the same unresolved weaknesses. fileciteturn0file1
- **Cedar Grove** and **Clarity Holdings** each sit in **Stage 4 – Negotiate** renewal/upsell deals (-\$2.21 M & \$2.58 M) carrying ≥3 overlapping risks (mandatory PS removed, quotes pending, low adoption), creating late-funnel friction inside high-value accounts. fileciteturn0file0turn0file1

---

### 🟡 **Momentum Bottlenecks**
**What it finds:** Clusters that should be advancing—toward close, toward upsell, toward renewal—but are stalling or stuck.

**Examples:**
- **Frontier Labs** — A **\$5.77 M** Best Case renewal/upsell sits in **Stage 3 – Solution** with 45 days to close, three active risks (no secured win, PS removed, low adoption) and no engagement for 13 days, hinting at a mid-funnel stall despite a Healthy account posture. fileciteturn0file0turn0file1
- Four Healthy accounts (**Aperture Science \$0.40 M, Aurora Enterprises \$0.64 M, Atlas Bank \$1.01 M, Tyrell Corp \$0.87 M**) hold Best/Pipeline deals that have lingered in **Stage 2–3** for ≥40 days and all lack a secured technical win—indicating early-stage drag across otherwise engaged customers. fileciteturn0file0turn0file1

---

### 🟠 **Contradiction Detection**
**What it finds:** Declared confidence that contradicts factual signal health—forecast tags, account optimism, or renewal assumptions vs. signal reality.

**Examples:**
- **Clarity Holdings** — Deal tagged **Best Case** at \$2.58 M, yet marked **At-Risk** with three risks (mandatory PS removed, quotes pending, low adoption) against a Healthy account label—confidence misaligned with deal reality. fileciteturn0file0turn0file1
- **Cyberdyne Systems** — Two Best Case opportunities total \$9.4 M but each carry ≥3 risk factors while the account is already At-Risk, exposing optimistic forecasting against material deal health issues. fileciteturn0file0turn0file1
- **Atlantic Energy** — \$1.15 M Upsell flagged Best Case despite low adoption, mandatory PS removal, and quotes pending—forecast optimism contradicts triple-risk status in an At-Risk opportunity. fileciteturn0file1

---

### 🟣 **Silent Zones**
**What it finds:** Complete engagement dead zones. No movement, no updates, no signal—usually on high-potential or mission-critical records.

**Examples:**
- **Prime Dynamics** — \$7.97 M Pipeline deal shows “💤 No activity for 30 days” risk and last touch **36 days** ago while needing close in **31 days**, forming a dormant high-value upsell. fileciteturn0file1
- Three transportation accounts (**Quantum Freight Systems \$7.7 M LTV, NorthStar Transport \$5.8 M LTV, Proxima Cargo \$24.1 M LTV**) carry “📭 No Pipeline in CQ + Next 4Q” at the account level yet have zero active mid- or late-stage opportunities—signaling total engagement voids in sizable franchises. fileciteturn0file0
