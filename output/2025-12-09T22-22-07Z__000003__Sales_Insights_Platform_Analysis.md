# Sales Insights Platform Analysis

## You (2025-12-09T22:22:07.617000+00:00)

**You are a dual-role expert combining:**

1. A **seasoned UX research lead** with deep experience transforming open-ended qualitative feedback into precise, design-ready action items.
2. A **regional sales manager at Palo Alto Networks**, with domain fluency in sales workflows, tools, and managerial pain points.

---

### 🔍 OBJECTIVE

Analyze a transcript of an internal interview with **John, Tim, Sophia, Mert, Ashley, and Amanda**, focusing on extracting **tactical product insights** and **highly specific, actionable design recommendations** for a **Sales Insights Platform** used by **District and Regional Sales Managers** at Palo Alto Networks.

---

### 📌 INSTRUCTIONS

Carefully review the provided transcript, which includes perspectives from multiple participants:

* **Include only:** Tim, Amanda, Sophia, Mert, Ian, and John.
* **Ignore comments from:** Chris, Sakshat, and Rajiv.

---

### 🧱 STRUCTURED OUTPUT FORMAT

You must generate a structured report with the following sections:

---

#### **1. Thematic Patterns (by individual)**

For each included participant, identify key patterns or repeated topics in what they said. Provide **specifics**, not generalizations.

Format:

**Amanda**  
- Repeatedly emphasized the lack of visibility into X  
- Uses spreadsheets to manually track Y  
...


---

#### **2. Cross-Participant Themes**

Cluster patterns across participants into shared themes. Highlight where there is agreement or emphasis across multiple voices.

> 💡 Avoid generic labels like “lack of visibility.” Instead, be specific:
> ✅ “No direct way to compare team pipeline performance across quarters”

---

#### **3. Minority or Contrarian Opinions (Anomalies)**

List any views that diverged significantly from the others—either because they challenge dominant perspectives or introduce overlooked issues.

---

#### **4. Insights (Derived from Thematic Tensions)**

Identify 3–6 key **insights** that surface **dichotomies or tensions** between user goals, tools, or experiences. Each insight should clearly articulate:

* The conflicting needs or observations
* The design opportunity or implication

> Example:
> **Insight:** Managers rely on dashboards to compare reps—but customize Excel sheets to track activity over time, signaling the platform lacks time-based filtering across individuals.

---

#### **5. Action Items (Design-Ready Recommendations)**

Based on the insights above, propose **specific, detailed design action items** for the product team.

✅ Focus especially on:

* **What is missing** (explicitly mentioned or implied)
* **What users are trying to achieve but cannot**
* **What would directly unblock their workflows**

Format:


**Action Item:** Add a comparative trendline view of rep-level quota attainment over time (weekly/monthly), segmented by region.  
**Rationale:** Amanda and Ian both described building these manually in Excel to track underperformance early in the quarter.


---

### 🧪 ADDITIONAL GUIDELINES

* **Use short, cited verbatim quotes** (1–2 lines) to back up insights when relevant.
* Silence on a topic can be mentioned, but only as a **secondary observation**.
* Prioritize specificity over abstraction—avoid conclusions like “users want unified visibility” unless they are tightly scoped.
* Treat every insight as a possible **design lens** to inform UI decisions, feature priorities, or interaction flows.

---

### ✅ SELF-CHECK BEFORE RESPONDING

Before finalizing your output, verify:

* Are all action items traceable to user needs?
* Have you gone beyond summarizing to derive **implications**?
* Are quotes properly attributed and meaningfully connected to your insights?

## ChatGPT (2025-12-09T22:34:33.251456+00:00)

### 1. Thematic Patterns (by individual)

---

**Ian Young** fileciteturn0file0  
- **Obsession with meetings as the leading indicator.** He repeatedly comes back to “what meetings are you going on this week?” and “what meetings did you schedule last week?” and wants this visible per seller, classified as external vs internal and by meeting type (Prisma AI, XSIAM, PS follow-up, etc.).  
- **Wants calendar data surfaced, not just pipeline.** In his previous org, he had a Power BI dashboard that pulled Outlook calendar and showed, per rep, “meetings scheduled this week” and “meetings created last week,” with titles and attendees. He’s trying to recreate that and feels it’s a “tremendous miss” that there’s no equivalent at PANW.  
- **Coaching through inspection points.** He uses meetings + pipeline together to create coaching moments: if there was a meeting but no new opp, he asks “why?”; if there’s pipeline but the meeting wasn’t prepped (SE not briefed, agenda unclear), he intervenes.  
- **Two primary categories for a manager: Activity and Opportunity.** He explicitly deprioritizes generic “performance/health” views because Clari covers that; his core lens is “drive the right activities to create opportunity, then help them close the opportunity.”  
- **Prefers weekly snapshots with quarterly context.** He typically wants a weekly view with the ability to roll up to quarter; fiscal-year views are nice-to-have, not primary.  
- **Terminology & navigation preferences.** He’s comfortable with labels like “previous week’s activity,” “upcoming week activity,” “opportunity risk,” “roadblocks,” and prefers **tabs** over deeply nested pages.

---

**Tim (DSM, EMEA)** fileciteturn0file4  
- **Structured operating rhythm.**  
  - Annual territory plans (rep + manager).  
  - Weekly account strategic reviews (8 weeks/quarter to cover ~52 accounts).  
  - Weekly forecast calls that double as opportunity reviews for current and next quarter.  
- **Heavy manual reporting burden.** He spends significant time assembling QBR/territory review decks: pulling numbers from Clari, Sales360, Learning Center, Salesforce (exec outreach reports). He’d gladly delegate “all the stuff… putting all the Q1 numbers together into a presentation.”  
- **Non‑negotiable “initiatives” metrics.** He tracks EBCs, executive outreaches, ASRs, and learning/compliance (“flight training,” role plays) as key drivers of win rate and rep performance. He knows, for example, that deals with EBCs close at ~80% and those with ASR at ~60%, and wants those surfaced.  
- **Balanced view on activity: not surveillance, but proof of effort.** He explicitly says he doesn’t want to micromanage, but uses activity + learning data to decide whether to coach or take harder performance decisions (e.g., “if the rep isn’t doing any of the below, they’re one step out of the business”).  
- **Wants initiative metrics front‑and‑center.** He suggests top-level tiles like “# EBCs this quarter,” “# executive outreaches,” “# ASRs completed,” with drill-down to accounts, opps and owners.  
- **Sees opportunity for AI in the unglamorous work.** He’s open to AI auto-updating account plans (e.g., from annual reports) and reducing admin work, but today AI usage is mostly limited to Clari’s risk scoring and ad-hoc email drafting.

---

**Amanda Brown (Sales Strategy / Ops partner for leaders like Dan)** fileciteturn0file3  
- **Thinks in “key questions”, not dashboards.** She wants to start from the canonical list of questions managers ask (e.g., “how much pipeline was created last week by rep?” “what’s my historical conversion rate by forecast category?” “which renewals aren’t in commit?”) and have the workbench answer those directly.  
- **Pushes beyond in-quarter myopia.** She explicitly wants managers to stop looking only at current quarter; the tool must make it easy to see 6‑month trends of pipeline creation, conversion, and rep-level performance, and to inspect out-quarter pipeline health.  
- **Renews, renewals, renewals.** Current renewals visibility is a “big problem”: she describes a world of 40+ static sheets, no automation, and believes better visibility would materially improve churn.  
- **Account health & executive engagement as critical signals.** She wants accounts with no exec engagement (no EBC, no CSR, no meaningful activity) to pop visually, ideally as a “heatmap” showing missing executive touchpoints and initiatives per account.  
- **Skeptical of opaque AI risk flags.** She supports AI-driven risk scoring, but insists the system be explicit about *why* a deal is “high risk” (e.g., “no C-suite meetings in 30 days,” “no opportunity created after discovery meeting,” etc.).  
- **Differentiates daily vs weekly cadences.** Daily: current-quarter gap-to-plan, imminent renewals, linearity. Weekly: full-funnel view, especially out-quarter pipeline creation and conversion trends.

---

**Sophia (Sales Acceleration / EMEA analytics)** fileciteturn0file2  
- **Currently glues everything together in GSheets & decks.** She maintains DSM scorecards, EBC/Big Deal motions, sales plays, etc., mostly via giant spreadsheets and Monday decks that can run to 30 slides; DSM-level views are limited.  
- **Wants a single DSM scorecard with drill-down.** Her ideal: a sales manager selects their name and sees (1) how many accounts their team owns; (2) counts and status of initiatives (ASRs, >$10M deals, EBCs, sales plays executed, etc.); then drills down by rep and account, and finally to *which* accounts lack a given initiative.  
- **Actionability gap frustrates her.** Current decks “don’t really tell them what to do.” She wants the tool to move from static metrics to actionable views (e.g., list of accounts missing EBCs for a rep, with a clear next step).  
- **Strong advocate of simplification & layering.** She repeatedly says: “simplify, simplify, simplify.” DSMs want:  
  - First: “my accounts, my team, where is the problem (red)?”.  
  - Then: easy drill-down to detail.  
- **Sees AI as enabler of automation around initiatives.** She’s excited by the idea that from “accounts missing EBC,” a DSM could click once and trigger templated emails/requests to schedule EBCs or ASRs, instead of manual coordination.

---

**Mert (Sales Acceleration / EMEA)** fileciteturn0file2  
- **Sees the core gap as “one level up” visibility.** He likes the current detailed Figma managers’ views, but says they “miss a crucial element”: a high-level view of ASR, EBC, sales plays, etc., by manager and by rep, before diving into pipeline and risk.  
- **Frames the workbench around key motions (pipeline, forecast, initiatives).** He suggests aligning the UI with existing cadences: pipeline review, forecast review, and sales initiatives review, each with clear, standard metrics defined by Sales Ops.  
- **Insists on centralization and reduced tool-hopping.** He repeatedly describes DSMs having to go into “20 systems” today to prepare for meetings; the workbench’s value is to centralize and layer AI on top.  
- **Alignment with sales cadences.** He wants the structure to mirror how DSMs actually work: tabs/views for pipeline, forecast, one‑to‑ones, sales plays, instead of mixing metrics from different motions on one busy page.

---

**John Krug (RVP / senior leader)** fileciteturn0file5  
- **Already runs his own dashboards to compensate for gaps.** He’s built a SFDC dashboard to view per-rep pipeline created last week/month/quarter, key commit opps, top Prisma Access customers, etc.; plus heavy use of People.ai engagement dashboards and Clari.  
- **Three pillars of what he really cares about:**  
  1. Pipeline creation (volume and trend).  
  2. Progression of deals (are next steps current, are deals moving?).  
  3. Health of customers (consumption, support cases, adoption).  
- **Wants AI for “are we actually progressing deals?”** He’s planning a manual “top 50 deals” spreadsheet that flashes red when next steps haven’t been updated within a timeframe. He wants the system to answer: “Are we constantly progressing this deal forward?” and to flag when we aren’t.  
- **Rep performance diagnosis framework.** He evaluates reps on pipe creation + closed business; if both are weak, he then uses engagement (meetings, outreach) and other signals to decide: “don’t know how” vs “don’t want to.”  
- **Strong push for “accounts with no touches / no pipeline” visibility.** He wants quick answers to “which accounts have not been touched in X days?” and “which accounts have no pipeline?” and sees this as a major gap today.  
- **Excited by unified, AI-powered dashboards.** He explicitly says the Figma workbench is “way better” than what he was trying to build and wants all of: AI pipeline creation insights, progression, and customer health “in one dashboard, correlated together.”

---

### 2. Cross-Participant Themes

1. **Meetings & activity as the missing leading indicator layer**  
   - Ian, Tim, and John all emphasize meetings and external engagement as critical leading indicators that are not well surfaced today. Ian wants dashboards of “meetings scheduled this week” and “meetings created last week” per rep, with titles and attendees. fileciteturn0file0  
   - Tim wants visibility into face-to-face meetings, executive outreaches, EBCs, and ASRs per rep as non-negotiable levers. fileciteturn0file4  
   - John uses People.ai but finds it only “directionally correct,” and still can’t easily correlate meetings with pipe creation and progression. fileciteturn0file5  

2. **Manual patchwork of tools & spreadsheets for core management tasks**  
   - Tim: QBR and territory review prep requires pulling from Clari, Sales360, Learning Center, Salesforce exec-outreach reports—he’d delegate this entire task. fileciteturn0file4  
   - Sophia & Mert: Monday sales initiatives calls run off 30‑slide decks with screenshots from different GSheets; DSMs rarely get a clean, self-service view. fileciteturn0file2  
   - John: built his own SFDC dashboards for pipe creation and commit opps because nothing out-of-the-box exists. fileciteturn0file5  

3. **Need for layered views: high-level “cockpit” → drill-down to rep / account / opp**  
   - Sophia & Mert: DSMs want a high-level scorecard (accounts, ASRs, EBCs, big deals, sales plays) and then to drill down by rep and account. fileciteturn0file2  
   - Ian: wants a top-level focusing on “Activity” and “Opportunity,” then drill into meeting lists for each rep. fileciteturn0file0  
   - John: approves of the quadrant “opportunity risk” visual but wants hover and click-through into the specific deals. fileciteturn0file5  

4. **Rep performance judged on a mix of pipe creation, closed business, and engagement**  
   - John explicitly: rep performance = pipe creation + closed business; if both are weak, he inspects People.ai and other signals to diagnose root cause. fileciteturn0file5  
   - Tim: similar mental model; uses meetings, EBCs, executive outreach and learning completion to decide whether a struggling rep is doing the right things and just needs coaching vs not putting in the work. fileciteturn0file4  
   - Amanda: wants multi-month views of pipeline creation trends and conversion by forecast category to identify reps who chronically under-create or under-convert. fileciteturn0file3  

5. **Strong desire for AI, but only if it’s transparent and grounded in real signals**  
   - Ian: open to AI, but wants it “weaponizing the data” to show which meetings/activities and pipeline creation occurred, not just generic insights. fileciteturn0file0  
   - Amanda: insists that high-risk flags be backed by explicit factors (no exec activity, stalled stage, missing next steps) and that AI explain *why* it’s calling something risky. fileciteturn0file3  
   - John: wants AI to tell him when deals are not progressing (e.g., no updated next step in X days) and when reps might be struggling, based on patterns in their notes and activity. fileciteturn0file5  

6. **Renewals and account health are high-stakes but poorly supported**  
   - Amanda: current renewals visibility is a mess of static sheets; she calls this a major unresolved use case that likely impacts churn. fileciteturn0file3  
   - John: cares about account health via cases and product consumption, and likes the idea of an integrated “health” tab. fileciteturn0file5  
   - Tim and Sophia/Mert: EBCs and ASRs are used as key leading indicators for big deals and expansion, but tracking them is manual and fragmented. fileciteturn0file2turn0file4  

7. **Navigation should mirror existing sales motions (pipeline, forecast, 1:1s, initiatives)**  
   - Mert: argues strongly that the workbench structure should map to how DSMs already run pipeline reviews, forecast calls, and sales initiative reviews. fileciteturn0file2  
   - Ian: top nav should highlight Activity and Opportunities; Clari already covers pure performance/health. fileciteturn0file0  
   - Amanda: daily view = current-quarter execution; weekly view = full funnel and out-quarter pipeline. fileciteturn0file3  

---

### 3. Minority or Contrarian Opinions (Anomalies)

- **Sophia & Mert’s push to elevate “sales initiatives” (ASR/EBC/sales plays) above pipeline.**  
  Others largely focus on pipeline and opportunities; Sophia & Mert argue that EMEA leaders want to see ASR/EBC/sales plays counts and gaps *before* pipe and forecast, as these are now core motions in their weekly cadence. fileciteturn0file2  

- **Tim’s desire to surface Learning Center/enablement data as part of rep performance.**  
  He wants to see whether underperforming reps have completed mandated training and role plays (e.g., XSIAM flight training), which no one else mentions. fileciteturn0file4  

- **Ian's relative deprioritization of “sales performance” summary tiles.**  
  He explicitly says managers should already know their overall performance; his primary interest is in Activity and Opportunity tabs, while the design team has been leaning into performance/health dashboards. fileciteturn0file0  

- **John’s skepticism about risk scores vs simple freshness of next steps.**  
  Others talk about stage aging, risk factors, etc.; John’s operational reality is “are next steps current, and are deals moving?”—he cares less about abstract scores and more about concrete signals like “no update in 7 days.” fileciteturn0file5  

---

### 4. Insights (Derived from Tensions)

---

**Insight 1 – Leading indicators live in different systems than lagging indicators, so managers can’t see “effort → outcome” in one place.**  

- **Tension:**  
  - Managers run their business off pipeline and closed ARR (Salesforce/Clari), but the *effort* that creates that pipeline—meetings, exec outreach, EBCs, ASRs, learning—is trapped in People.ai, GSheets, Learning Center and ad-hoc docs. fileciteturn0file2turn0file4turn0file5  
  - This forces Tim and John to manually correlate meetings and EBCs with pipeline and wins; Ian had to rely on Power BI in a prior org to get this view. fileciteturn0file0turn0file4turn0file5  
- **Design opportunity:**  
  - A “Rep Performance” layer that explicitly links **activities + initiatives → pipeline creation → conversion** gives DSMs a single place to diagnose whether problems are effort, execution, or coverage.

---

**Insight 2 – Managers want AI to call out risks, but only when the “why” is inspectable and grounded in their language & cadences.**  

- **Tension:**  
  - The product team is leaning into an AI-heavy workbench (risk scores, smart filters, insights). fileciteturn0file0turn0file2turn0file3  
  - Managers like Amanda and John are wary of black-box scoring; they want clear explanations: “no C-level meetings in last 30 days,” “stage 3 > 60 days,” “no next step in Clari for 10 days,” etc. fileciteturn0file3turn0file5  
- **Design opportunity:**  
  - Treat “AI risk” as a bundle of **human-readable risk reasons**, aligned to MEDD(P)ICC and existing forecast cadences, so leaders can challenge, trust, and coach off the same model.

---

**Insight 3 – Current tools optimize for in-quarter forecast, but leaders are trying to manage a rolling 2–4 quarter story.**  

- **Tension:**  
  - Clari & existing dashboards are optimized for “this quarter”: gap to plan, commit/best coverage, linearity, etc. fileciteturn0file3turn0file5  
  - Amanda, Tim, and John all talk about multi-quarter territory plans, out-quarter pipeline creation, and cumulative performance (Q1 + Q2 vs H1 plan) which they currently build manually. fileciteturn0file3turn0file4turn0file5  
- **Design opportunity:**  
  - The workbench can differentiate itself from Clari by owning the **rolling 2–4 quarter view**: trendlines of pipe creation, conversion by forecast category, and rep trajectory, not just this-quarter commit.

---

**Insight 4 – Sales initiatives (ASR, EBC, plays) are treated as strategic levers, but the tooling surfaces them as scattered checkboxes, not as a system.**  

- **Tension:**  
  - EMEA treats ASRs, EBCs and sales plays as core motions, with weekly escalation up through AVPs/RVPs. fileciteturn0file2  
  - The current experience is manual: different GSheets and slide decks, with no easy way for a DSM to see “out of 100 accounts, 30 have ASRs; here are the 70 missing them; here’s one click to start fixing that.” fileciteturn0file2turn0file4  
- **Design opportunity:**  
  - Turn initiatives into **first-class objects** in the manager workbench (with coverage metrics and direct actions), rather than something leaders have to build separately in spreadsheets.

---

**Insight 5 – Managers are allergic to busy, mixed dashboards; they think and work in discrete motions (pipeline, forecast, initiatives, 1:1 coaching).**  

- **Tension:**  
  - Current prototypes mix pipeline, activities, initiatives, and health on single complex pages. fileciteturn0file2turn0file3  
  - Mert, Sophia, Ian, and John all implicitly structure their mental model around specific conversations: “pipeline review,” “forecast call,” “1:1/coaching,” “territory/initiative review,” each with different questions and horizons. fileciteturn0file0turn0file2turn0file4turn0file5  
- **Design opportunity:**  
  - Shape the workbench navigation and page templates around those **four canonical motions**, with shared underlying data but tailored panels, filters, and AI prompts.

---

**Insight 6 – Renewals & account health are high-stakes, cross-functional, and currently the least automated part of the workflow.**  

- **Tension:**  
  - Amanda calls out renewals visibility as essentially unsolved (static spreadsheets, no automation), yet it’s one of Dan’s biggest concerns. fileciteturn0file3  
  - John and Tim both want health views that combine product telemetry, support cases, EBCs, and ASRs to manage churn and expansion risk, but today those require multiple tools. fileciteturn0file4turn0file5  
- **Design opportunity:**  
  - A “Renewals & Health” capability that consolidates telemetry, support, and exec engagement into a renewal-risk view could be the most differentiated and immediately valuable part of the workbench.

---

### 5. Action Items (Design-Ready Recommendations)

I’ll map these directly from the insights and participant asks.

---

**Action Item 1: Build a “Meetings & Creation” tab focused on weekly rep activity, powered by calendar + People.ai.**  

- **What:**  
  - Per rep table for a selected time window (default: this week & last week):  
    - # of **external** customer meetings (with titles & customer name).  
    - Classification by type: new logo discovery, expansion (by product), PS/post‑sale, renewal.  
    - **Meetings created last week** vs meetings *occurring* this week.  
  - Click a rep to open their detailed meeting list (with attendees) and AI-generated questions like “Which of last week’s meetings did not result in a new opportunity?”  
- **Rationale:**  
  - Directly addresses Ian’s missing Power BI view and inspection points. fileciteturn0file0  
  - Supports Tim and John’s use of meetings as proof of effort & leading indicator, without forcing DSMs into separate People.ai dashboards. fileciteturn0file4turn0file5  

---

**Action Item 2: “Rep Performance Cards” that tie activities + initiatives → pipe creation → conversion.**  

- **What:**  
  - For each rep, a card showing over a selectable period (quarter / last 6 months):  
    - Pipeline created (by value, count, and product).  
    - Closed won, win rate, and conversion by forecast category (e.g., “65% of prior-quarter commit closed won”).  
    - Key activities & initiatives: #EBCs, #exec outreaches, #ASRs completed, #unit 42 or other plays, #face-to-face meetings.  
    - Optional: “training completeness” badge from Learning Center for required modules.  
  - Visual cues to show whether each dimension is above/below district averages.  
- **Rationale:**  
  - Encodes John’s “pipe creation + closed business + activity” mental model and Amanda’s desire for multi-month conversion insights. fileciteturn0file3turn0file5  
  - Gives Tim a way to see whether a struggling rep is doing the right things (meetings, initiatives, learning) or not, without combing through multiple systems. fileciteturn0file4  

---

**Action Item 3: AI-backed “Risk Reasons” chips on opportunities and accounts, not just a single score.**  

- **What:**  
  - For each flagged opportunity, show chips like:  
    - “No C‑level meeting in 30 days”  
    - “No next step in 10 days”  
    - “Stage 3 for 60+ days”  
    - “Account health: high P1 case volume”  
    - “No exec outreach / no EBC for this deal”  
  - Clicking a chip shows the underlying data (e.g., last C‑level meeting date, stage history).  
  - Allow filtering by specific risk reason (e.g., “show opps with missing next steps”).  
- **Rationale:**  
  - Meets Amanda’s requirement that risk flags be explainable and grounded in specific behaviors. fileciteturn0file3  
  - Supports John’s desire to know which deals are not progressing because next steps are stale, without needing a separate spreadsheet. fileciteturn0file5  

---

**Action Item 4: Add a “Top 50 Deals” progression view tailored to RVP/DSM forecast calls.**  

- **What:**  
  - For a chosen district/region and quarter, show a fixed list of “Top N” deals (by amount), with columns:  
    - Amount, forecast category, close date.  
    - Days since last stage change.  
    - Days since last updated next step.  
    - # customer meetings in last 30 days.  
  - Conditional formatting (amber/red) when thresholds are breached; allow managers to open a side panel with full opportunity plan and MEDD(P)ICC fields.  
- **Rationale:**  
  - Automates John’s planned manual “top 50 deals with flashing red” spreadsheet concept and aligns with his real Clari usage (sorting by amount and checking next steps). fileciteturn0file5  
  - Gives DSMs one forecast-call page that’s focused on actionability, not just totals.

---

**Action Item 5: DSM Scorecard home view with initiative coverage (ASR/EBC/Plays) as first-class metrics.**  

- **What:**  
  - Landing page where the manager picks their name/territory and sees:  
    - # accounts in patch; % with ASR completed; % with EBC completed; # >$10M deals; # active sales plays; etc.  
    - A red/amber/green bar for each initiative (e.g., “ASR coverage: 32/100 accounts”).  
  - Clicking an initiative (“ASR”) opens a list of accounts missing it, with rep owner and quick actions (see next item).  
- **Rationale:**  
  - Implements Sophia’s DSM scorecard vision (“how many accounts, how many have ASRs/EBCs”) and Mert’s request to elevate sales initiatives as a starting view. fileciteturn0file2  
  - Helps align the workbench to EMEA’s weekly sales acceleration calls where these numbers are reviewed.  

---

**Action Item 6: One-click “Initiative actions” (e.g., schedule EBC, trigger ASR reminder) from lists of gaps.**  

- **What:**  
  - From the “missing EBC” account list, DSM can:  
    - Click “Request EBC” → prefilled form/email to EBC coordinators with account, owner, suggested timeframe.  
  - From the “accounts missing ASR” list, DSM can:  
    - Click “Send ASR reminder” → templated email/Slack to rep with account list and due date.  
- **Rationale:**  
  - Turns Sophia’s dream “this should let me schedule EBCs or nudge ASRs directly” into a clear workflow, moving from passive reporting to proactive orchestration. fileciteturn0file2  
  - Reduces friction Tim feels when trying to enforce non-negotiable motions like ASR and EBC coverage. fileciteturn0file4  

---

**Action Item 7: Navigation organized around four core motions: Pipeline, Forecast, Initiatives, Coaching.**  

- **What:**  
  - Top-level tabs across the workbench:  
    - **Pipeline** – full-funnel view (current + out-quarters), pipe creation over time, product mix.  
    - **Forecast** – current-quarter commit/best, Top 50 deals view, linearity vs last year.  
    - **Initiatives** – DSM scorecard and initiative coverage (ASR/EBC/sales plays).  
    - **Coaching** – Rep Performance cards + Meetings & Creation tab for 1:1s.  
  - Allow Activity vs Opportunity sub-tabs inside where appropriate (aligning with Ian’s mental model).  
- **Rationale:**  
  - Mirrors how DSMs already run their business (weekly pipeline reviews, forecast calls, initiative calls, and rep 1:1s), reducing cognitive load vs mixed dashboards. fileciteturn0file0turn0file2turn0file4turn0file5  

---

**Action Item 8: Rolling 2–4 quarter “Funnel Trajectory” view with AI prompts.**  

- **What:**  
  - A time-series chart per district showing, for each of the last 4 quarters:  
    - Pipeline created.  
    - Closed won.  
    - Conversion rates by forecast category (Commit/Best/Upside).  
  - AI prompt suggestions like: “Show reps whose pipeline creation has declined for 2 consecutive quarters” or “Explain why conversion from Best → Closed is lower this quarter vs Q‑1.”  
- **Rationale:**  
  - Gives Amanda and Tim the multi-quarter story they currently build in slides, and pushes managers beyond single-quarter myopia. fileciteturn0file3turn0file4  

---

**Action Item 9: “Renewals & Health” workspace combining telemetry, support, and exec engagement.**  

- **What:**  
  - For all renewals in the next 12 months, show:  
    - Renewal ARR, date, owner, forecast category.  
    - Account health signals: product consumption vs entitlement, recent P1/P2 cases, NPS/CSAT if available.  
    - Exec engagement: EBCs held, exec outreaches, last C-level meeting.  
  - Filter: “Renewals not in commit,” “High ARR + poor health,” “No exec engagement in 6 months.”  
- **Rationale:**  
  - Directly tackles Amanda’s “biggest thing we haven’t solved” around renewals visibility and John’s desire for integrated account health views. fileciteturn0file3turn0file5  

---

**Action Item 10: AI-assisted QBR / territory review pack generator.**  

- **What:**  
  - Within any view (Pipeline, Initiatives, Coaching), allow DSM to click “Generate QBR pack,” which:  
    - Assembles key charts (targets vs attainment, pipeline coverage by quarter, initiative coverage, top deals, at-risk renewals).  
    - Adds AI-generated narrative summaries (e.g., “Your H1 is projected at 92% of plan; main gap is net-new in UK public sector and Prisma Access upsell.”).  
  - Export to PPT or Google Slides with editable visuals.  
- **Rationale:**  
  - Offloads the manual “end of week/quarter” slide-building that Tim and Sophia currently do, and leverages AI for a clearly bounded, tangible time-saver. fileciteturn0file2turn0file4  

---

If you’d like, we can next take one motion (for example, **Coaching tab for 1:1s**) and go all the way down to specific layout, filters, and AI prompt examples tuned for DSMs in PANW’s workflow.

