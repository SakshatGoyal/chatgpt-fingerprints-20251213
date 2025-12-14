# FigJam synthesis template

## You (2025-11-19T22:44:25.658000+00:00)

This is a conversation between me and Tim, with a few additional participants. I'm giving this to a designer to try and breakdown the conversation into actionable information. I need you to think like a research/design manager and try to create a template that would be applicable to break down all the information into figjam. Like what scenarios were discussed, challenges, potential opportunities discussed, any information we need from them further, etc... Use your own approach. I'm attaching a brief about the project below for your reference.

---

## What this platform is

A DSM cockpit built to drive **forecast discipline and pipeline hygiene**. It brings together performance, deal risk, and renewal posture, then layers **AI-curated callouts** on top so the manager knows **where to intervene next**.

---

## Information architecture (how the product is organized)

* **Top-level tabs:** **Summary**, **Sales Performance**, **Opportunities**, **Health**.
* **Each working tab follows one pattern:**

  1. a **raw data** view (complete list with filters),
  2. an **Analysis** view (opinionated visual insight),
  3. **Curations** (AI-generated shortlists based on anomalies or notable patterns).

A persistent **“What would you like to ask?”** bar with suggested questions appears in context, plus a right‑rail assistant with prompts (e.g., *“Give me a RUNN explanation for our deal.”*).

---

## Core metrics & vocabulary used throughout

* **Plan** – the quarterly target.
* **Closed** – booked revenue YTD in-quarter.
* **Commit** – pipeline the team has explicitly committed to close this quarter.
* **Best Case‑In** – additional in‑quarter pipeline beyond Commit (deals that could land).
* **Total‑In / CCBC** – shorthand for **Closed + Commit + Best Case‑In** (the in‑quarter “coverage” numerator).
* **Coverage ratio** – Total‑In (CCBC) relative to target; <1.0x signals a shortfall.
* **Target / Target Gap** – the goal and the remaining delta to target.
* **Risk Factor Count** – number of risk flags for an opportunity (e.g., inactivity >30 days, configuration/fit issues, etc.).
* **Account Health** – renewal risk proxy; rolls up **Technical Health** and **Deployment & Adoption** signals over time.
* **Days Remaining** – days left to quarter close or renewal.

---

## SUMMARY (the daily snapshot)

**Purpose:** Fast, evidence‑based orientation for the quarter—where the district stands, what threatens the number, and where renewals may wobble.

1. **Plan overview**
   A tile strip shows **Plan, Closed, Commit, Best Case‑In, Total‑In, Best Case‑Out, Total Pipeline, Total Forecast** with progress vs. target—your at‑a‑glance forecast posture.

2. **Critical Territories**
   Side‑by‑side bars per district/territory (by AE) show **Closed / Commit / Best Case‑In** against **Target**, along with **Target Gap** and **coverage**. It spotlights where the **commit ratio** is out of balance or a **coverage gap** puts target at risk.

3. **Opportunities at Risk**
   A prioritized list of live deals with **Forecast category, Stage, Risk factors, Days remaining, Value**. It concentrates the manager on **near‑term, high‑impact** risk.

4. **Renewals at Risk due to Account Health**
   Renewal motions whose underlying **Account Health** is weak or deteriorating—so you can mobilize CS/SE/Partner support before renewal friction shows up at signature time.

---

## SALES PERFORMANCE

### Territories (raw data)

A structured, sortable roster of districts → territories (by **AE**) with **Total CCBC, Closed, Commit, Best Case‑In, Coverage**. Trend mini‑charts (e.g., WoW) help see whether **Closed/Commit/BC‑In** are moving up or down. Coverage chips highlight **<1x** (under‑covered) vs **>2x** (strong coverage).

**Controls:** quarter selector, deal‑type filters (e.g., R/U/NN), and simple zoom/sort to focus by district or individual AE.

### Analysis (opinionated lens)

* **Coverage gauge across four quarters** (current + next three). Each quarter is labeled **Healthy / Medium / Low** based on coverage; the manager can **set the coverage threshold**.
* **AE Performance Quadrant:** plots each AE by **Median Closed** (execution) vs **Median CCBC‑In** (pipeline sufficiency).

  * **High Close / High CCBC** → high confidence.
  * **High Close / Low CCBC** → **needs pipeline**.
  * **Low Close / High CCBC** → **conversion/coaching** needed (pipeline exists).
  * **Low Close / Low CCBC** → **critical** (both pipeline and execution lacking).
* **Velocity table (rate of change by week):** for each AE, week‑over‑week **change in closed pipeline**, with heat‑coloring (red = stalled weeks). This exposes **momentum** (or lack thereof), not just static totals.

### Curations (AI callouts)

AI surfaces **small, focused subsets** that need a point of view—e.g., *“2 territories have had a consistent ratio of Closed, Commit, Best Case for 3+ weeks”* (stagnation). Each curation expands to show the affected district/AE rows with the same **CCBC breakdown and coverage** so the DSM can coach or reallocate attention immediately.

---

## OPPORTUNITIES

### Opportunities (raw data)

A comprehensive **deal inventory** with multi‑facet filters (Product, Forecast, Stage, Deal Size, Other Risks, Account Health). Each row shows:

* **Account & Opportunity**, **value**, and **close timing** (e.g., “closing in 31 days”),
* **Forecast category** (Pipeline, Base Case, Commit),
* **Sales stage**,
* **Products in scope**,
* **Account Health** (Critical / At‑Risk / Healthy),
* **Other Risk count** and **last activity** with age (“Architecture Review – 31 days ago”).

A header insight frames the list (e.g., *“Renewal‑heavy pipeline with weak account health.”*) so the DSM immediately understands **composition risk**.

### Analysis (risk–value map)

* **Quadrant scatterplot** of **Opportunity Value** (x) vs **Risk Factor Count** (y), split at medians to form:

  * **High Value / High Risk** (forecast swing zone),
  * **High Value / Low Risk** (confidence zone),
  * **Low Value / High Risk** (low return on attention),
  * **Low Value / Low Risk** (background wins).
* A quarter‑by‑quarter bar view quantifies **how much value sits in each risk category** for current and forward quarters.
* Tabs below the chart list the **actual opportunities** in each quadrant with the same rich row detail for quick triage.

### Curations (AI callouts)

Targeted shortlists generated by pattern detection—e.g., *“4 Commit opportunities ($12.4M) with no activity in 30+ days.”* Other examples in the sidebar include install‑base fit issues or deals with **no risks** (sanity check). The goal is to protect **forecast credibility** by surfacing hygiene failures (stale Commit, missing movement) and structural risks.

---

## HEALTH

### Renewals (raw data)

A renewal‑centric list that ties **customer telemetry** to revenue risk. For each renewal opportunity:

* **Account & linked opportunity**, **renewal value**, **days to renewal**,
* **Account Health** with trend mini‑series, decomposed into:

  * **Technical Health** (stability/quality signals),
  * **Deployment & Adoption** (usage depth, adoption momentum).
    Filters (e.g., **Account Health**, **Deal size**, **Product**, **time window** like “Last 3 months”) let a DSM isolate accounts with **declining health** and little time left—so CS/SE/Partner resources can be engaged early.

*(The Health tab in your set has no separate Analysis screenshot; its raw view already emphasizes trend‑over‑time.)*

---

## Common interaction patterns & aids

* **Contextual Q&A bar** with suggested prompts (e.g., *“How does the current quarter compare to the last 3 quarters?”*, *“Are close rates tracking to historic norms?”*).
* **Consistent filters** (Quarter, deal type, Forecast, Stage, Deal Size, Account Health, Other Risks) and **Reset** actions.
* **Pagination & items‑per‑page** controls for long lists.
* **Badges & chips** (Commit/Base Case/Pipeline, coverage chips, risk counts) to compress critical state into scannable UI.

---

## What insights the platform is trying to provide (in plain terms)

* **Are we covered to hit the number?**
  Coverage gauges and CCBC vs Target show sufficiency **now** and **next quarters**.
* **Where are the gaps by territory/AE?**
  Territory coverage, **Target Gap**, and AE quadrants distinguish **pipeline problems** from **conversion problems**.
* **Which deals will swing the forecast?**
  **High value / high risk** opportunities are singled out, with time left and last activity.
* **Is Commit credible?**
  Curations flag **stale Commit** and other hygiene failures that erode forecast trust.
* **What renewals are at risk and why?**
  Account Health trendlines (with **Technical** and **Adoption** components) tie product reality to renewal probability and timing.

---

## The DSM experience in practice

1. **Start at Summary** to see quarter posture, territory exceptions, at‑risk deals, and renewal hot spots.
2. **Drill into Sales Performance** to separate **coverage issues** from **execution issues** (AE quadrant + weekly momentum).
3. **Open Opportunities** to triage **high‑value, high‑risk** deals and clean up **stale Commit** via Curations.
4. **Check Health** to line up CS/SE/Partner interventions on renewals with deteriorating **Technical** or **Adoption** trends.

The net effect: a **guided, evidence‑first workflow** that keeps the forecast tight, focuses coaching where it matters, and reduces surprise at quarter end.





## ChatGPT (2025-11-19T22:45:11.752567+00:00)

Here’s a FigJam-ready synthesis template you can give your designer so they can turn this (and future) DSM interviews into structured, actionable insights for the cockpit.

I’ll first outline the **board structure**, then detail each frame (with example prompts), and sprinkle in a few concrete examples from this Tim session so it’s clear how to use it. fileciteturn0file0

---

## 0. Overall FigJam Layout

Ask the designer to lay out frames **left → right** like a story:

1. **Session Overview**
2. **Person & Context**
3. **Scenarios & Workflows**
4. **Pain Points & Frictions**
5. **Needs & Opportunities (mapped to product IA)**
6. **AI-Specific Opportunities**
7. **Open Questions & “Need More Info”**
8. **Top Bets & Design Directions**

Suggested sticky/color key:

- 🟨 Yellow = **Verbatim quote / observation**
- 🟦 Blue = **Insight / interpretation**
- 🟧 Orange = **Pain point / challenge**
- 🟩 Green = **Opportunity / idea**
- 🟪 Purple = **Open question / follow-up**

---

## 1. Session Overview (Frame 1)

**Purpose:** Make it easy for anyone to understand *who*, *when*, and *what* in 30 seconds.

**Columns / fields (use a simple grid):**

- **Participant(s):**
  - Role, level (e.g., DSM – Major Accounts, UK), tenure in role.
- **Date & source:**
  - Date of interview, link to recording / transcript.
- **Org context:**
  - Region, segment (e.g., Private Sector UK), team size, quota type.
- **Session goals:**
  - What you wanted to learn in this interview.
- **High-level summary (3 bullets):**
  - 1–2 sentences each: “How they run the quarter”, “Where they struggle”, “How they think about AI/productivity”.

*Example from Tim (for designer to fill):*
- “DSM, started Aug 1; new to role but 12 yrs as AE; manages mix of renewals, upsell, net new.” fileciteturn0file0

---

## 2. Person & Context (Frame 2)

**Purpose:** Anchor everything in this specific DSM’s world.

Create a 2x2-ish layout:

### A. Responsibilities & Success

- **Sticky prompts:**
  - How is this person measured? (Plan, mix of Net New / Upsell / Renewal, etc.)
  - What “good quarter” means to them.
  - How many reps / territories they oversee.
  - Key cadences they’re accountable for (QBRs, territory reviews, forecast calls, etc.).

### B. Current Tooling Stack

Cluster stickies under **“Systems they touch”**:

- Salesforce
- Clari
- Sales 360
- People.AI
- Learning Center / enablement tools
- Spreadsheets / Slides
- Others

For each, capture:

- **What do they use it for?**
- **Pain points / limits?**

*Example notes from Tim:*
- “Uses Clari for forecast reporting upstream to his boss.”
- “Has to jump between Clari, Learning Center, Sales 360, Salesforce for exec outreach reports to prep one QBR deck.” fileciteturn0file0

### C. Mental Model of “Productivity”

- How *they* define productivity (e.g., “time with customers vs admin”).
- Their attitude towards micromanaging activity (they may resist it).
- Any explicit non-negotiables (e.g., face-to-face meetings, EBCs, exec outreach). fileciteturn0file0

---

## 3. Scenarios & Workflows (Frame 3)

**Purpose:** Turn the conversation into discrete **scenarios** the product can serve.

Create a **scenario swimlane**. Each row = scenario. Each column:

1. **Trigger**
2. **Goal**
3. **Steps & Tools**
4. **Metrics they look at**
5. **Pain points**
6. **Opportunities / product hooks**

Suggested core scenarios (based on this convo and your brief):

1. **Quarter / Territory Planning**
2. **Weekly account strategic reviews (Monday)**
3. **Weekly forecast & opportunity reviews (Thursday)**
4. **Preparing exec / territory reviews for leadership**
5. **Rep coaching & performance / development check-ins**
6. **Pipeline hygiene & commit sanity checking**
7. **Monitoring rep activity & engagement (EBCs, exec outreach, etc.)**
8. **Using AI tools (today) for sales workflows**

For each scenario, designer fills stickies under the columns.

*Example row – “Preparing exec / territory reviews”:* fileciteturn0file0

- **Trigger:**
  - Asked to present H1 + FY26 update; quarterly territory review; leadership wants view on net new vs upsell vs renewals.
- **Goal:**
  - Show performance vs plan, growth vs last year, and spotlight problem areas.
- **Steps & Tools:**
  - Pull numbers from Clari, Sales 360, Learning Center, Salesforce (exec outreach reports).
  - Build manual deck summarizing everything.
- **Metrics looked at:**
  - Growth rates YoY, mix of net new vs renewals, activity metrics (EBC count, exec outreach, etc.).
- **Pain points:**
  - Very manual, duplicative work; data scattered across 4–5 systems.
- **Opportunities / hooks:**
  - Dashboard that automatically compiles these views and exports into a QBR-ready narrative.

The designer repeats this structure for every scenario mentioned.

---

## 4. Pain Points & Frictions (Frame 4)

**Purpose:** Central “problem wall” across all scenarios.

Use a **big frame** titled: **“What makes this hard?”**

Inside, create clusters:

1. **Data Fragmentation & Duplication**
   - “Going into 4–5 systems to prepare one presentation.” fileciteturn0file0
   - Duplicative meetings/updates (Thursday prep for Friday exec review).

2. **Pipeline & Forecast Hygiene**
   - Stale opportunity plans (not updated for months).
   - Surprise downgrades (“Rep tells me 3 deals aren’t in this FY anymore → ⅓ of pipe disappears.”). fileciteturn0file0

3. **Rep Development & Coaching Visibility**
   - Hard to see, in one view, how reps are doing on learning / mandatory courses vs performance.
   - No clear linkage between performance issues → coaching plan.

4. **Activity & Engagement Insight**
   - Wants to track EBCs, exec outreach, C-level meetings, but currently separate reports.
   - Wants to avoid micromanagement yet still see if non-negotiable activities are happening.

5. **AI & Automation Gaps**
   - Existing AI (e.g., in Clari) highlights risk/errors but doesn’t suggest next actions.
   - AI not auto-updating account plans from external signals (e.g., annual reports).

Each orange sticky = *one* pain point, written as a problem statement:

> “I have to pull from 4–5 systems to prepare a single QBR, which eats time I’d rather spend with reps/customers.”

---

## 5. Needs & Opportunities Mapped to Product IA (Frame 5)

**Purpose:** Translate problems into opportunities, aligned with **Summary / Sales Performance / Opportunities / Health**.

Create a 2D grid:

**Columns = Product Areas**

- Summary
- Sales Performance
- Opportunities
- Health
- Cross-cutting (e.g., Q&A bar, AI curations, Activity & Coaching layer)

**Rows = Need Types**

- Orientation (What’s going on?)
- Decision / Prioritization (Where should I focus?)
- Coaching & Enablement (How do I help reps?)
- Reporting / Communication (How do I tell this story upward?)

For each cell, designers place **green “opportunity” stickies**:

### A. Summary tab – opportunities

- Orientation:
  - “Single place to see: Plan, Closed, Commit, Best Case-In, Total-In + mix (net new vs upsell vs renewal).”
- Prioritization:
  - “Highlight territories with low commit ratio *and* weak activity (few EBCs / exec meetings).”
- Reporting:
  - “Export a simple summary that can drop into a QBR deck.”

### B. Sales Performance – opportunities

- Orientation:
  - “Per-AE view of CCBC, coverage, WoW momentum (velocity) across quarters.”
- Coaching:
  - “Overlay rep activity (EBCs, exec outreach, Learning completion) on performance quadrant to guide 1:1s.” fileciteturn0file0

### C. Opportunities – opportunities

- Pipeline hygiene:
  - “Curations that flag: high-value opportunities with stale or missing opportunity plans; Meddic gaps; no movement in X days.”
- Decision:
  - “High value / high risk map that highlights which deals could swing the quarter.”

### D. Health – opportunities

- Renewals:
  - “Prioritize accounts with declining Account Health & limited days to renewal; show whether CS/SE/Partner is already engaged.”
- Coaching:
  - “Show which reps consistently manage account health well vs who is reactive.”

### E. Cross-cutting

- Q&A bar:
  - Questions like, “Which territories are weak on net new vs renewal?” or “Which reps have low coverage and low EBCs this quarter?”
- AI curations:
  - “Show me opportunities in the next 3 quarters whose plans haven’t been updated in 90+ days.”
  - “List reps behind on mandatory learning who are also behind on plan.”

The designer’s job: turn each pain point from Frame 4 into at least one **green opportunity sticky** in this grid.

---

## 6. AI-Specific Opportunities (Frame 6)

**Purpose:** Separate out AI ideas from generic dashboarding.

Create three columns:

1. **Automate**
   - Auto-populate account plans with info from annual/quarterly reports. fileciteturn0file0
   - Auto-tag risk factors (stale plan, no exec engaged, no partner steps, etc.).

2. **Augment Decisions**
   - “Based on your standards, here are 5 opportunities where forecast category vs plan completeness is inconsistent.”
   - “Compared to similar districts, your net new is lagging; here’s where the shortfall concentrates.”

3. **Assist Communication**
   - Draft QBR/territory review narrative sections from current metrics.
   - Draft follow-up emails to reps: e.g., “Here’s your key risk deals and suggested actions before Thursday’s call.”

Each sticky is phrased as **“AI could…”** or **“Assistant can…”** to avoid jumping straight into solution UI.

---

## 7. Open Questions & “Need More Info” (Frame 7)

**Purpose:** Capture what’s unclear and what you’d ask next time.

Columns:

- **About their process**
  - “How standardized is the weekly account review template across managers?”
- **About metrics**
  - “What are the official global definitions for pipeline vs forecast KPIs (e.g., linearity, CCBC, etc.) at this org?”
- **About systems / data**
  - “Which of these activity metrics (EBCs, exec outreach, Learning completion) are reliably tracked and accessible?”
- **About AI appetite & constraints**
  - “What level of AI suggestion feels trustworthy vs intrusive for DSMs?”

These become your **research backlog** for future sessions.

---

## 8. Top Bets & Design Directions (Frame 8)

**Purpose:** End the board with a **clear, prioritized set of design “bets”**.

Create a simple **2x2 priority matrix**:

- X-axis: **Impact on DSM’s effectiveness**
- Y-axis: **Feasibility (data + design effort)**

Place **larger green stickies** for:

- “Single cockpit that replaces the need to consult 4–5 systems for QBR prep.”
- “Curations that surface stale or low-credibility Commit and missing opportunity plans.”
- “Performance quadrant + activity & enablement overlay for coaching.”
- “AI narrative that explains quarter posture and suggests where to intervene next (deals, reps, territories).”

Below the matrix, add a small list:

- **Now (MVP pilot)**
- **Next**
- **Later**

and sort key opportunities accordingly.

---

## How to Use This Template Across Interviews

Give your designer this simple workflow:

1. **Paste transcript link & session info** → fill Frames 1–2.
2. **Re-listen skim once** → highlight every time the DSM:
   - Describes a *scenario* (“On Mondays we…”)
   - Expresses *friction* (“It takes a long time to…”)
   - Expresses *desire / wish* (“It would be great if…”)
3. **Map those quotes into the Scenario swimlane** (Frame 3) and Pain wall (Frame 4).
4. **Translate pain → opportunity** in the IA grid (Frame 5).
5. **Extract AI-specific ideas** into Frame 6.
6. **Note gaps / confusions** in Frame 7.
7. **End with 3–5 top bets** in Frame 8.

If you’d like, I can next:
- Take this exact Tim interview and **partially fill the template** (e.g., first 3 scenarios + opportunity grid) so your designer sees a concrete example.

## You (2025-11-19T22:47:18.967000+00:00)

could you make this much simpler? keep in mind the task should be finished in less than 4 hours by a junior designer.

## ChatGPT (2025-11-19T22:47:20.750814+00:00)

Absolutely — here is a **much simpler, lightweight template** a junior designer can execute in under 4 hours. It’s designed to be *fast, structured, repeatable,* and easy to translate into FigJam.

---

# **🎨 Simple FigJam Template for Breaking Down a DSM Conversation**
_Total time to complete: 2–4 hours_

Use **five frames** only. Each frame has a clear purpose and a few sticky categories. That’s it.

---

# **FRAME 1 — Session Snapshot (5–10 min)**
Purpose: Quickly anchor who/what/why.

**Stickies (one row):**
- **Person** (Role, region, team size)
- **Top Responsibilities** (1–3 bullets)
- **Goals of Conversation** (why we talked to them)
- **Key Takeaways** (3 bullets max)

---

# **FRAME 2 — What We Heard (45–60 min)**
Purpose: Capture everything said, but *lightly sorted.*

Create **four columns**. Drop stickies directly from transcript summary.

### **1. Tasks / Workflows**
(Things they do weekly or quarterly)
Examples: weekly forecast review, QBR prep, deal reviews, renewal triage.

### **2. Challenges / Pain Points**
(Any friction, admin burden, confusion, surprises)

### **3. Behaviors / Habits**
(How they make decisions, what they check, rituals, cadences)

### **4. Quotes**
(1–2 verbatims that feel important)

This frame is messy **on purpose** — it’s your raw material.

---

# **FRAME 3 — What They’re Trying to Solve (30–45 min)**
Purpose: Convert the raw notes into **clear problem buckets.**

Create **three clusters**:

### **A. Forecast Discipline Problems**
(e.g., stale commits, missing opportunity plans, late surprises)

### **B. Pipeline Health Problems**
(e.g., low coverage, poor AE hygiene, unclear next steps)

### **C. Renewal / Account Health Problems**
(e.g., weak adoption signals, at-risk accounts not surfaced early)

In each cluster, place 3–5 stickies summarizing the actual problems you heard.

*Tip:* Use short “problem statements” like:
- *“Takes hours to pull data from 4–5 systems before exec reviews.”*
- *“Doesn’t trust commit because reps don’t update plans.”*

---

# **FRAME 4 — Opportunities (45–60 min)**
Purpose: Turn problems into product opportunities.
Create **four columns** that map directly to the cockpit’s IA:

1. **Summary tab**
2. **Sales Performance**
3. **Opportunities**
4. **Health**

Under each, create 3–5 green stickies starting with phrases like:

- **“Surface when…”**
- **“Help them see…”**
- **“Make it easier to…”**
- **“Automatically flag…”**
- **“Provide a simple view of…”**

Examples:
- Summary → *“Surface territories with low coverage + weak activity.”*
- Opportunities → *“Flag high-value deals with no activity for 30+ days.”*
- Health → *“Show renewals with declining technical health and <90 days left.”*

---

# **FRAME 5 — Open Questions (10–20 min)**
Purpose: Capture what we still don’t know.

3 columns only:

- **About their workflow** (e.g., “What’s the standard for opportunity plans?”)
- **About metrics/data**
- **About AI usefulness / limits**

These become follow-up items.

---

# **That’s the whole template. Simple, fast, repeatable.**

If you want, I can now:
👉 **Auto-fill this template with content from the Tim conversation** (using your transcript) so your designer sees exactly how to use it.
