# Balanced Insight Flow

## You (2025-07-21T13:47:49.682000+00:00)

Thank you for the detailed context and previous structure. Here is the **revised O3 prompt** tailored precisely to your new requirement:

---

## ✅ O3 Prompt: Multi-Step Insight Flows from Opportunities and Accounts (Balanced Split)

### 1. **Goal**

Generate **three user-driven scenarios**, where each scenario consists of a **progressive sequence of 4 insight steps**, simulating how users interact with AI-generated insights to iteratively apply filters and refine focus across a blend of **Opportunities** and **Accounts**.

This time, insights must reflect a **balanced 50/50 split** between the **Opportunity-level** and **Account-level** datasets—ensuring that both types of records are equally represented across the insight steps.

The AI should surface insights in the order they emerge from typical user workflows:

* Initial insight reveals a meaningful signal in the full dataset.
* The user is led to apply a small set of filters.
* A refined subset is surfaced, revealing deeper, **non-redundant** insights.
* Repeat this loop for **4 total steps** per scenario.

Each insight should act as a **contextual trigger** for the next filter selection—supporting focused navigation without prescribing decisions.

---

### 2. **Return Format**

For each of the 3 scenarios:

* Use a numbered structure:
  **Scenario 1**

  * **Step 1 Insight:**
    *\[Signal based on entire dataset]*
    → *Suggested filters applied by the user*
  * **Step 2 Insight:**
    *\[Signal derived from filtered subset]*
    → *Next filters applied*
  * **Step 3 Insight:**
    *...*
    → *Next filters*
  * **Step 4 Insight:**
    *\[Final focused insight from narrowed slice]*

Each **insight** must:

* Reflect real patterns using the joined `Rick - Opportunities` and `Rick - Accounts` sheets.
* Follow the design voice and **AI Synthesis Guidelines**.
* Be precise, filter-guiding, and non-repetitive across steps.

Each **filter application** must:

* Pull directly from the **valid filter values list** (provided).
* Be plausible and well-motivated by the preceding insight.

**Balance requirement:**
Each scenario must have **2 Opportunity-based insights** and **2 Account-based insights**, distributed across the 4 steps.

---

### 3. **Warnings & Guardrails**

* 🚫 Do not offer recommendations.
* 🚫 Do not invent filters—use only provided ones.
* 🚫 Avoid repeating insights across steps.
* ✅ Each insight should unlock **new information**.
* ✅ Ensure filters are plausible in context and can co-exist (especially for multi-select).
* ✅ Avoid edge-case contradictions (e.g., a filter that narrows by one risk while implicitly excluding others that could still appear).

---

### 4. **Context & Source Data**

You will be given a **multi-sheet Google Sheet file**, but only these two sheets are relevant:

* `Rick - Opportunities`
* `Rick - Accounts`

Each sheet contains structured data representing either deals or customer-level context. Both share a common column `Account Name`.

Your synthesis will emulate what a well-informed AE might encounter when using AI to progressively slice their book of business using focused filters. Insights must reflect **cluster-level signal synthesis**, not individual examples.

---

### 5. **Execution Persona**

You are operating as a **Context-Aware Signal Synthesizer**, embedded into an intelligent sales interface. Your purpose is to surface signals that help users funnel their attention—**not to tell them what to do**. You believe that good synthesis accelerates intuition, and that insights are only as useful as the filters they unlock.

You balance **narrative fluency** with **analytical rigor**, always respecting AE autonomy and preserving trust through observable logic.

---
Filters for your context:

Filter Values for opportunities:

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

Filters for Accounts:

PRODUCT: (same as opportunities)
R/U/NN: (same as opportunities)
Risk Categories: 
📭 No Pipeline in CQ + Next 4Q
🏛️ No EBCs in last year
🔌  Not Platformized
🧪 Active POVs
🩺 Customer technical health is critical.
🛑 Customer adoption/deployment rate is low
🌀 No ASR / Stale ASR
🚧 No customer success plan

## ChatGPT (2025-07-21T13:49:09.597350+00:00)

**Scenario 1**

* **Step 1 Insight (Opportunity):**  
  *78 % of Discovery‑stage deals—especially in Firewall and Cortex & Cloud—still carry 🏅 No Secured technical win, signalling early momentum without validation.* fileciteturn0file1  
  → **Suggested filters applied by the user:** `SALES STAGE: Discovery` + `RISK CATEGORY: 🏅 No Secured technical win` + `PRODUCT: Firewall, Cortex & Cloud`

* **Step 2 Insight (Account):**  
  *Among the accounts behind those deals, 9 out of 10 are marked Healthy yet all show 🧪 Active POVs—evidence of active trials that still need closure.* fileciteturn0file0  
  → **Next filters applied:** `Risk Categories: 🧪 Active POVs`

* **Step 3 Insight (Opportunity):**  
  *Inside this subset, Best Case opportunities already in Stage 4 – Negotiate average > 3 risk flags, and 60 % are waiting on ⌛ Quotes pending approval.* fileciteturn0file1  
  → **Next filters applied:** `FORECAST CATEGORY: Best Case` + `SALES STAGE: Negotiate` + `RISK CATEGORY: ⌛ Quotes pending approval`

* **Step 4 Insight (Account):**  
  *The remaining accounts consistently pair 🚧 No customer success plan with 🛑 Low adoption—highlighting a post‑sale execution gap despite healthy surface scores.* fileciteturn0file0  


---

**Scenario 2**

* **Step 1 Insight (Account):**  
  *Every At‑Risk account lists 🛑 Customer adoption/deployment rate is low, yet together they represent nearly one‑quarter of total lifetime value.* fileciteturn0file0  
  → **Suggested filters applied:** `Risk Categories: 🛑 Customer adoption/deployment rate is low`

* **Step 2 Insight (Opportunity):**  
  *Opportunities from these accounts that bundle Cortex & Cloud with Firewall average 3.5 risk flags—about 50 % higher than the portfolio mean.* fileciteturn0file1  
  → **Next filters applied:** `PRODUCT: Cortex & Cloud, Firewall`

* **Step 3 Insight (Account):**  
  *Within this group, accounts lacking 🏛️ EBCs in the last year post roughly 30 % smaller Q4 pipeline than peers, hinting at stalled executive alignment.* fileciteturn0file0  
  → **Next filters applied:** `Risk Categories: 🏛️ No EBCs in last year`

* **Step 4 Insight (Opportunity):**  
  *Net New deals under $1 M that have reached Stage 4 – Negotiate almost universally still lack a secured technical win, keeping close dates uncertain.* fileciteturn0file1  
  → **Next filters applied:** `R/U/NN: Net New` + `SALES STAGE: Negotiate` + `DEAL SIZE: Less than $1M` + `RISK CATEGORY: 🏅 No Secured technical win`


---

**Scenario 3**

* **Step 1 Insight (Opportunity):**  
  *SASE‑only deals make up 22 % of open pipeline; two‑thirds sit in Best Case, yet one‑third still flag 🏅 No Secured technical win.* fileciteturn0file1  
  → **Suggested filters applied:** `PRODUCT: SASE` + `FORECAST CATEGORY: Best Case`

* **Step 2 Insight (Account):**  
  *Accounts tied to these SASE plays frequently lack current ASRs—over half show 🌀 No ASR / Stale ASR—suggesting outdated success reviews.* fileciteturn0file0  
  → **Next filters applied:** `Risk Categories: 🌀 No ASR / Stale ASR`

* **Step 3 Insight (Opportunity):**  
  *Within those accounts, Stage 3 – Solution opportunities that blend SASE with CDSS carry double the average risk count and high rates of ⌛ Quotes pending approval.* fileciteturn0file1  
  → **Next filters applied:** `SALES STAGE: Solution` + `PRODUCT: SASE, CDSS` + `RISK CATEGORY: ⌛ Quotes pending approval`

* **Step 4 Insight (Account):**  
  *Most of the accounts still emerge as Healthy and continue to run 🧪 Active POVs—showing momentum if technical gaps can be bridged.* fileciteturn0file0

