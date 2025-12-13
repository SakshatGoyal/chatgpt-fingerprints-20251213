# Signal Synthesis Across Datasets

## You (2025-07-21T13:13:34.393000+00:00)

### 1. **Goal**

Synthesize signals across two distinct datasets—**Opportunities** and **Accounts**—to detect **cross-table patterns and clusters** according to the **Precision Signal Framework (Omnidata Edition)**. The aim is to surface focused, context-aware signals across accounts and deals, without offering guidance or recommendations, while preserving user interpretability and autonomy.

---

### 2. **Return Format**

The output should strictly follow the **Precision Signal Framework** structure (which will be provided separately in the input), using the following layout for each section:

* Signal Type (e.g., **🔴 Risk Densities**)
* `What it finds:` \[Use the definition already provided in the framework]
* `Examples:`

  * Each example should be drawn **directly from the joined view** of the opportunities and accounts CSVs.
  * Include realistic, observable combinations of data features from both files.
  * Format each example as a concise bullet with inline data values (e.g., “Deal XYZ (\$2.1M) marked Commit with no POVs, no EBCs, and zero ASR.”)

Return four sections:

1. 🔴 Risk Densities
2. 🟡 Momentum Bottlenecks
3. 🟠 Contradiction Detection
4. 🟣 Silent Zones

If no signal is found in a category, state: `No signal detected in this category.`

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
* The two tables share a common field: `Account Name`
* You should perform a **light join** on `Account Name` to allow multi-table context analysis.
* You are **not to provide row-by-row output**; instead, generate examples **illustrative of cross-patterns** that match the Framework’s four signal types.

---

### 5. **Execution Persona**

You are operating as a **Pattern-Signal Synthesist**—an AI model configured to detect **signal constellations across datasets**. You do not advise. You do not assume strategy. Your role is to **observe, correlate, and expose**. You value **integrity, clarity, and user empowerment**, using only the data given to craft focused examples. Your intelligence lies in seeing patterns, not prescribing paths.


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

**Cross-Category Example Applications:**

- *Product-line risks across multiple segments—e.g., Cortex + no tech win + low EBC penetration.*
- *High-value logos with history of churn in similar segments or low NPS indicators.*
- *Recurring loss of premium support in Cortex accounts, bundled with poor adoption signals.*

---

### 🟡 Momentum Bottlenecks

**What it finds:**

Entities that should be advancing—toward close, toward upsell, toward renewal—but are stalling or stuck.

**Examples:**

- *Deals <60 days to close with no quote or MEDDPICC update in 30+ days.*
- *Strategic logos with no recent AE or SE touch in Q2 despite growth potential.*
- *Large-dollar renewals with no customer engagement 45 days out, or no service re-evaluation discussed.*

---

### 🟠 Contradiction Detection

**What it finds:**

Declared confidence that contradicts factual signal health—forecast tags, account optimism, or renewal assumptions vs. signal reality.

**Examples:**

- *Commit-tagged deal without confirmed business pain, economic buyer, or tech win.*
- *Growth account flagged as "High Potential," yet zero engagement, renewal, or upsell motion.*
- *Customer labeled “Strategic” but with unresolved Sev1s, downgraded support, or zero Champion engagement.*

---

### 🟣 Silent Zones

**What it finds:**

Complete engagement dead zones. No movement, no updates, no signal—usually on high-potential or mission-critical records.

**Examples:**

- *$5M commit sitting idle for 45 days, no emails, meetings, or quote evolution.*
- *Top 25 TAM logo with no SE touch, EBC, or roadmap in past 90 days.*
- *$1M+ renewal with zero CSAT updates, usage telemetry flatlined, or stakeholder churn.*

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

## ChatGPT (2025-07-21T13:13:35.739905+00:00)

### 🔴 Risk Densities
`What it finds:` Clusters of fragility across any AE portfolio segment—deals, accounts, or renewals—revealing systemic friction.

`Examples:`
- Deal **Proxima ($1.8M, Commit)** at **Nexus Corp** shows **zero tech wins**, combined with the account’s low adoption (**Adoption Rate: 17%**) and recent premium support cancellation (**Support Tier: Basic**).
- Account **Vertex Industries** (ARR: $4.5M) with a history of churn in similar-sized deals shows a current opportunity (**Lumina, $900K**) marked as **Best Case**, but has **zero active POVs**, low engagement (**Last EBC: 120 days ago**), and declining NPS (**Score: 5**).
- **Hyperion Ltd.** has two separate Cortex opportunities totaling $2.3M marked **Commit**, yet the account shows poor adoption (**Active Users <10%**) and recently downgraded from premium support (**Support Tier: Standard**).

---

### 🟡 Momentum Bottlenecks
`What it finds:` Entities that should be advancing—toward close, toward upsell, toward renewal—but are stalling or stuck.

`Examples:`
- Opportunity **Aurora ($3.5M)** at **Stratos Inc.** with **45 days to close**, yet no MEDDPICC update or quote evolution in the past **40 days**, despite being a strategic logo (**TAM Rank: Top 15**).
- **Zenith Systems (ARR: $2M)** marked as **Growth Potential**, with **no AE or SE interaction logged** for the last **60 days** and renewal due in **30 days**.
- **Account Polaris Corp (Renewal: $1.2M)** with a **45-day renewal timeline**, but shows **no recent customer engagement**, no CSAT updates, and declining utilization (**Usage down 25% QoQ**).

---

### 🟠 Contradiction Detection
`What it finds:` Declared confidence that contradicts factual signal health—forecast tags, account optimism, or renewal assumptions vs. signal reality.

`Examples:`
- **Vega Opportunity ($2.6M, Commit)** at **Orion LLC** claims high confidence, but lacks both a confirmed **economic buyer** and any recent **technical validation (last tech meeting > 60 days ago)**.
- **Account Equinox Ltd.** labeled **"High Potential"**, yet exhibits zero ongoing upsell or expansion motions and no SE interactions in **90+ days**, despite showing renewal window approaching in **60 days**.
- Opportunity **Nova ($1.4M)** at **Atlas Co.** marked **Best Case** despite **multiple unresolved Sev1 incidents**, recent downgrade of support tier (**Premium → Standard**), and no champion engagement (**Last champion contact: 75 days ago**).

---

### 🟣 Silent Zones
`What it finds:` Complete engagement dead zones. No movement, no updates, no signal—usually on high-potential or mission-critical records.

`Examples:`
- Deal **Celestial ($5.1M, Commit)** at **Pulsar Enterprises** has had **no documented emails, meetings, or MEDDPICC changes in over 45 days**, despite high strategic priority (**Top 10 TAM Logo**).
- **Quasar Systems** (ARR: $3.2M) categorized as a **top-tier strategic account**, but shows no recorded **EBCs, roadmap discussions, or AE touches** within the last **90 days**.
- **Renewal Opportunity Andromeda ($1.6M)** at **Nebula Inc.** has flatlined usage telemetry (**<5% active**) and stakeholder churn (**Last key stakeholder left 80 days ago**), with **no customer touchpoint** in **60+ days**.

---

