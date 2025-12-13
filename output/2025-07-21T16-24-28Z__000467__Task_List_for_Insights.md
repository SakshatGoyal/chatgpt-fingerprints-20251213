# Task List for Insights

## You (2025-07-21T16:24:28.340000+00:00)

Help me refine this prompt for an o3 model. Begin creating the prompt. 

---
I need you to create a list of tasks, similar to the one you provided in the previous response. However, this time, I need you to create more targeted tasks that can be tied back to the insights I share with you. 

As an input, I’m sharing two files - 

Rick - Opportunities

Rick - Accounts

these are txt files but i need you to treat them as csv files. 

For each of these files, we’ve extracted insights. 

### Opportunity Insights

- **Technical Win Gaps:** 61 out of 101 deals (≈ $79.7M) carry the risk 🏅 No Secured technical win—making it the most common single-point risk across the pipeline.
- **Activity Stalls:** Of the 37 deals with ≤45 days to close, 14 have had no logged activity in 30+ days—a clear momentum stall at a critical point in time.
- **Forecast Inconsistencies:** 17 deals are labeled Best Case, yet 12 of them have ≥3 active risk factors.
    - Notably, 5 Best Case deals lack secured tech wins and show no partner activity.
    - 3 are in Critical health despite optimistic forecast tags.
- **Dormant Opportunities:** 19 deals (≈ $28.4M) have logged no activity in the last 30 days;
    - 11 of them must close in the next 60 days
    - 7 are currently tagged Best Case or Commit

### Account Insights

- **25 of 50** accounts (≈ $33.7 M in Q4 pipeline) carry **🛑 Low adoption** → most common single risk.
    - **7** also flag **🌀 No ASR**, forming the highest‑risk micro‑cluster (≈ $13.6 M).
    - **9** Low‑adoption accounts are already **At‑Risk/Critical**, yet still total ≈ $15.1 M pipeline—momentum under threat.
    - **16** remain **Healthy** despite ≥1 major risk—health label vs. signal mismatch.
- **19 / 50** accounts (≈ $37 M pipeline) show **🌀 No ASR** —second‑largest risk cluster.
    - **12** of those also carry
    - **🛑 Low adoption**, signalling post‑sale fragility.
    - **11** belong to the **Firewall** family (STRATA platform) → product‑specific density.
    - **6 / 19** are At‑Risk/Critical yet still labelled Healthy in forecasts—contradiction detected.
- **3** accounts show **📭 No pipeline in CQ + next 4 Q**—rare but severe silent zone.
    - Two of the three are already **At‑Risk** (one is Critical) yet still lack forecast coverage—contradiction.
    - All three carry ≥4 risks, making them the densest individual risk records.
    - Combined lifetime value ≈ $51 M—legacy revenue under threat.
    

For your context, we are developing an AI-driven insight system that analyzes multiple opportunities and accounts to surface key actionable insights in the form of clusters. These insights are not recommendations, but rather they are just surfacing anomalies or aspects about their accounts that an account executive needs to know as they are completing tasks. 

Your task is to provide a list of tasks that can align with the insights. For example, if an insight reads

“61 out of 101 deals (≈ $79.7M) carry the risk 🏅 No Secured technical win—making it the most common single-point risk across the pipeline.”
then are there specific tasks around those deals that an account executive might need to look at in order to start taking action on those deals?

However, the tasks do need to be realistic. So maybe an indeal approach might be to first internally create a list of tasks based on the account details, and then see if any of those tasks can align best with the insights shared. Do not provide a task for an account or deal that is unrelated to the key message or takeaway of the insight. For example, 

if an insight reads “61 out of 101 deals (≈ $79.7M) carry the risk 🏅 No Secured technical win—making it the most common single-point risk across the pipeline.”, then ‘Hold/Push: Budget Freeze – Check Back in Q1’ may not be ideal to show since it may not help an AE with the message in the takeaway. 

Also, make sure that there’s some logical coherence with the data and the tasks. For example, if an insight reads 

“3 deals currently in Best-Case”, then ‘schedule discovery call’ would make no sense since the deal is already in best case. 

Make sure to first review all the data, and internally make sense of the scenario before creating a list of tasks for yourself.

## ChatGPT (2025-07-21T16:24:40.986799+00:00)

{"content_type": "thoughts", "thoughts": [{"summary": "Crafting the prompt", "content": "The user wants me to start creating the prompt. I need to follow the structure: Goal, Return Format, Warnings & Guardrails, and Context & Additional Elements. Based on their instructions, I'll summarize key insights from our conversation and choose the right analytical persona, like \"Revenue Operations Analyst\" or \"Sales Strategy Analyst\". Since this is an internal task, there's no need for external data or clarifications. I'll proceed directly with generating a well-structured prompt that meets their requirements and reflects the content provided.", "chunks": [], "finished": true}], "source_analysis_msg_id": "aa3bbd45-6643-4464-a40d-ae0e2b18d65a"}

## ChatGPT (2025-07-21T16:24:45.083281+00:00)

{"content_type": "reasoning_recap", "content": "Thought for 12 seconds"}

## ChatGPT (2025-07-21T16:24:29.116611+00:00)

**Prompt for O3 Model**

---

### 1. Goal  
Produce a **concise, prioritized task list** for an Account Executive (AE) that directly addresses the highest-impact pipeline and customer-health risks surfaced in two CSV-formatted files:  

- `Rick - Opportunities.csv` (opportunity-level data)  
- `Rick - Accounts.csv` (account-level data)  

The tasks **must tie back explicitly to the numbered insights** supplied below, preserving logical coherence with stage, health, forecast label, and time horizon details.

---

### 2. Return Format  
Return a JSON array of task objects, ordered by decreasing dollar impact, where each object has:

| Key | Type | Description |
|-----|------|-------------|
| `task_id` | string | Unique, human-readable ID, e.g., `"T-OPP-TW-001"` |
| `insight_ref` | string | ID of the insight that triggered the task (e.g., `"Opp-01"` or `"Acct-02"`) |
| `impact_$` | number | Pipeline or ARR at risk that the task addresses |
| `task_title` | string | Action verb + target (≤ 80 chars) |
| `description` | string | One-sentence “why this matters,” referencing concrete deal/account attributes |
| `due_in_days` | integer | Reasonable time-box (e.g., 3, 7, 14) based on urgency signalled by the insight |
| `required_roles` | string[] | Stakeholders to involve, e.g., `["SE"]`, `["CSM","Partner Manager"]` |

Example element:
```json
{
  "task_id": "T-OPP-TW-001",
  "insight_ref": "Opp-01",
  "impact_$": 79700000,
  "task_title": "Secure technical win for high-value stalled deals",
  "description": "61 deals lack confirmed technical validation; obtain SE sign-off to unblock closure.",
  "due_in_days": 7,
  "required_roles": ["SE"]
}
```

---

### 3. Warnings & Guardrails  

1. **Stay Insight-Bound** – generate **no tasks** that cannot be clearly justified by the supplied insights.  
2. **No Speculation** – use only fields present in the two CSVs (assume typical CRM headers such as `Stage`, `ForecastCategory`, `LastActivityDate`, `HealthScore`, etc.).  
3. **Realistic Actions** – task verbs must reflect standard AE motions (e.g., secure technical win, schedule executive alignment, involve CSM).  
4. **Consistent Logic** – avoid tasks that contradict deal stage (e.g., no “discovery call” for `Stage = Negotiation`).  
5. **Dollar Impact Precision** – compute `impact_$` by summing the `Amount` (Opportunities) or `ARR`/`Pipeline` (Accounts) referenced by each insight.  
6. **No Recommendations** – tasks merely surface what to do next; they **do not** prescribe strategic shifts or probability adjustments.  

---

### 4. Context & Additional Elements  

#### 4.1 Execution Persona  
Embed the reasoning of a **“Revenue Operations Analyst”**—skilled at interrogating CRM data, quantifying risk clusters, and translating them into next-step tasks that sales teams actually perform.

#### 4.2 Supplied Insights  

| ID | Category | Insight (abridged) | Dollar Impact |
|----|----------|--------------------|---------------|
| **Opp-01** | Opportunity | 61 / 101 deals lack secured technical win | ≈ $79.7 M |
| **Opp-02** | Opportunity | 14 / 37 imminent-close deals show ≥30 days inactivity | *see file* |
| **Opp-03** | Opportunity | 12 Best-Case deals carry ≥3 risks; 5 lack tech win & partner activity; 3 in Critical health | *see file* |
| **Opp-04** | Opportunity | 19 dormant deals; 11 close ≤ 60 days; 7 tagged Best Case/Commit | ≈ $28.4 M |
| **Acct-01** | Account | 25 / 50 accounts Low Adoption (7 also No ASR) | ≈ $33.7 M |
| **Acct-02** | Account | 19 / 50 accounts No ASR (12 also Low Adoption) | ≈ $37 M |
| **Acct-03** | Account | 3 accounts: no pipeline next 5 Qs, ≥4 risks, high LTV | ≈ $51 M |

Use these IDs in `insight_ref`.

#### 4.3 Analytical Steps (implicit)  
1. Load both CSVs.  
2. Filter opportunities/accounts linked to each insight criteria.  
3. Quantify `impact_$`.  
4. Draft candidate tasks; discard any lacking direct linkage.  
5. Output JSON array per **Return Format**.

---

**Checklist (before returning):**  
- [ ] Every task references exactly one `insight_ref`.  
- [ ] `impact_$` sums match source rows.  
- [ ] No speculative fields or recommendations.  
- [ ] Actions, roles, and due dates are realistic.

