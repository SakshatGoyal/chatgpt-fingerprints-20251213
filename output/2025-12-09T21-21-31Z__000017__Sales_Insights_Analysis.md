# Sales Insights Analysis

## You (2025-12-09T21:21:31.685000+00:00)

**You are a dual-role expert combining:**

1. A **seasoned UX research lead** with deep experience transforming open-ended qualitative feedback into precise, design-ready action items.
2. A **regional sales manager at Palo Alto Networks**, with domain fluency in sales workflows, tools, and managerial pain points.

---

### 🔍 OBJECTIVE

Analyze a transcript of an internal interview with **John, Tim, Sophia, Mert, and Amanda**, focusing on extracting **tactical product insights** and **highly specific, actionable design recommendations** for a **Sales Insights Platform** used by **District and Regional Sales Managers** at Palo Alto Networks.

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

## ChatGPT (2025-12-09T21:34:06.080671+00:00)

### 1. Thematic Patterns (by individual)

---

**Ian Young (RVP / Sales leader)** fileciteturn0file0  

- **Obsessed with meeting-level activity as the missing leading indicator.**  
  He repeatedly comes back to, “what meetings are you going on this week… what pipeline did you create in the previous week?” and complains that none of this is “at our fingertips.” His workaround is asking reps to share calendars and then cross‑checking static pipeline in SFDC/Clari.

- **Wants a calendar‑integrated dashboard that distinguishes “good” vs “weak” meetings.**  
  In his prior org (Power BI) he had a dashboard of “meetings scheduled this week” + “meetings created last week,” only external, showing title and attendees. He wants to see if meetings are proactive (Prisma AI, XIM, expansion) versus “a continuation of a PS engagement that’s post‑sale” so he can reward & replicate good behavior.

- **Two coaching lenses: current week vs previous week.**  
  He wants to see (1) upcoming meetings to prep resources (SEs, specialists, agenda), and (2) last week’s meetings correlated with pipeline creation to ask “you spoke to X about Y; I don’t see any pipeline created—how come?” This is explicitly about pattern spotting for coaching, not surveillance.

- **Primary navigation = Activity + Opportunity, not generic “performance.”**  
  He says if a manager doesn’t know where they are vs plan “I don’t know if you’re really paying attention.” He’d spend most time on **Activity** (meetings, pipeline creation) and **Opportunity** (deal risk / stage / coverage); Clari already covers generic sales performance.

- **Prefers simple time windows: weekly snapshot with quarterly roll‑up.**  
  He calls a quarter “a solid place to look,” but insists his real cadence is weekly, with the ability to roll up to quarter/fiscal if needed.

- **Risk language: “opportunity risk,” “roadblocks,” and stalled stages.**  
  He’s comfortable with notions like stage aging, stalled opportunities, and “opportunity risk” tags, but only when grounded in clear factors like no activity, stuck POV, or lack of progression.

---

**Sophia (Sales Acceleration – EMEA)** fileciteturn0file1  

- **Driving a DSM scorecard that aggregates sales initiatives across tools.**  
  She’s building a Google Sheets “DSM scorecard” where a manager selects their name and sees: number of accounts, ASR completion, 10M+ deals, EBCs, sales plays pitched/completed, etc., with drill‑downs: DSM → AE → account → missing items (e.g. “accounts that are missing ASRs”).

- **Insists on both high‑level and deep detail.**  
  She wants:  
  - Top‑level counts (e.g., “Tim Davis has 50 accounts; how many have ASR completed?”)  
  - Then ability to see **which specific accounts** are missing initiatives and exactly when EBC/ESR was last done.

- **Current state is slideware + static G‑sheets, not actionable.**  
  Every Monday they review ~30 slides of sales‑initiative metrics (sales plays, big deals, EBCs) with AVPs/RVPs. She explicitly says that from a typical slide, “I don’t really know… what we need to do from this slide… they don’t know either.”

- **Core job‑to‑be‑done: surface “the red” and make it actionable.**  
  For DSMs she distills needs as: “their accounts, their team. How are they doing? Where is the problem? The red and then they want to drill down into that very easily,” e.g., to schedule an EBC or trigger ASR work.

- **Ideal flow is insight → immediate action.**  
  She calls the “dream scenario” a flow where the tool not only shows accounts with no EBC/ASR but can trigger “go schedule” or send the right notifications/emails to the AE/owner from within the interface.

---

**Mert (Sales Acceleration – EMEA)** fileciteturn0file1  

- **Sees Workbench as the place to make EMEA analytics actually “actionable.”**  
  He contrasts current EMEA reporting (“we give them the information, but they still gotta go fish for it”) with a Workbench embedded in the tool reps/managers actually use, so data → action is in one flow.

- **Believes the current prototype is missing “additional sales initiatives” as a first‑class view.**  
  He wants ASR/EBC/sales‑play metrics elevated “as a starting point,” not buried under pipeline tabs.

- **Strong on simplification and level‑up summarization.**  
  Echoing Sophia, he stresses DSMs need to see something like “I have 100 accounts, and only 30 ASRs completed. Where do I see this right now?” before going into complex, detailed dashboards.

- **Pushes for built‑in automation off scorecards.**  
  He imagines one‑click flows like: “50 accounts with missing ASR → click → send an email to all the people owning those accounts,” and similar for EBC scheduling.

- **Wants to bridge the interim spreadsheet world with Workbench.**  
  He’s pragmatic that Sophia’s spreadsheet scorecard will exist as a “temporary solution,” but wants Workbench to absorb that logic and make it scalable and less manual.

---

**Amanda Brown (Sales Strategy / Ops for Dan)** fileciteturn0file2  

- **Starts from questions, not charts.**  
  She suggests interviewing leaders and collecting the recurring questions they ask (e.g., “How much pipeline was created last week / month / quarter by rep?” “What’s my historical conversion rate by forecast category this quarter?”), then designing around those top 10–20.

- **Two cadences: daily current‑quarter lens vs weekly full‑funnel lens.**  
  For “what they wake up and look at,” she wants: current quarter gap to plan, coverage, linearity vs same time last year, and renewals expiring this quarter. Weekly, she wants views on out‑quarter pipeline creation and long‑term pipeline trends by rep.

- **Heavy emphasis on rep‑level pipeline creation trends and conversion quality.**  
  She wants to spot reps who “in the last 6 months [are] barely creating pipeline, and all their pipeline has low close rate,” to flag performance issues beyond just in‑quarter attainment.

- **Renewals visibility is a major unsolved pain.**  
  She calls current tooling “45 different spreadsheets” that are “static, and not authentic” for renewals. She wants to see **renewals not in commit**, renewals that aren’t forecasted at all, and believes better visibility would materially improve churn.

- **Account health = exec engagement + initiatives + risk signals.**  
  She’s keen on heatmaps of accounts with no EBC, no ASR, no exec activity, and wants these to “pop up” along with risk factors like low engagement or missing next steps.

- **Cautious about AI risk scoring without transparency.**  
  She’s supportive of risk surfacing but insists “we’re gonna have to be super clear on why we’re saying that they’re high risk,” calling out engagement, exec activity, and next steps as explicit reasons that must be visible.

---

**Tim (DSM – Major Accounts, UK)** fileciteturn0file3  

- **Works on a structured cadence: territory plan → weekly account reviews → weekly forecast calls.**  
  - Annual: territory plan per rep with number view + development plan.  
  - Weekly: Monday account strategic reviews (8 weeks of quarter to cycle through ~52 accounts).  
  - Weekly: Thursday 1‑hr forecast sessions per rep that double as opportunity‑plan reviews.

- **Large manual reporting burden across multiple tools.**  
  For QBRs/h1 reviews he manually composes views of net new, upsell, renewals using Clari, Sales360, Learning Center, Salesforce exec outreach reports, etc. He says this “took me a long time to do” and is highly manual.

- **Opportunity risk = incomplete or stale opportunity plans in current + out quarters.**  
  He worries about big deals out in June with no opportunity plan or plans not updated for months, leading to sudden pipeline evaporation. Risk is less about admin fields and more about MEDDIC/opportunity‑plan completeness and recency.

- **Non‑negotiable initiatives: exec outreach, EBCs, ASRs.**  
  He wants a dashboard that shows, per rep, progress vs targets like EBCs per quarter or ASR completion, referencing metrics like “when an account has an EBC, 80% of the time we close the deal… [when it has] an ASR, 60% of the time we close the deal.”

- **Uses People.ai and Learning Center as part of rep diagnostics.**  
  He wants to see rep face‑to‑face meetings, C‑level meetings, EBCs from People.ai, plus mandatory training completion from Learning Center, and use that in the conversation: if rep misses number but is doing the right activities and training, he coaches; if not, he escalates.

- **Strong preference for views aligned to motions (pipeline vs forecast vs 1:1/development).**  
  He finds combined pages “confusing,” especially when pipeline and forecast metrics are mixed. In his words: if he’s prepping a pipeline review, he wants a pure pipeline tab (creation, stalled, beyond current q); for forecast, a forecast tab (C+coverage, linearity); and for 1:1s, activity & development.

- **Sees AI’s promise in auto‑updating account plans and reducing admin.**  
  He imagines AI reading annual/quarterly reports to update account plans, and auto‑populating Sales Play Console / activity plans, but notes little of this exists today in his workflow.

---

**John Krug (Regional / Area leader)** fileciteturn0file4  

- **Has already hacked together his own manager dashboard ecosystem.**  
  He maintains:  
  - A dashboard per rep for pipeline created last week / this month / this quarter.  
  - Top commit opps list.  
  - Top Prisma Access accounts by users (for add‑on conversation).  
  - People.ai views of meetings/time‑spent.

- **Cares about three pillars: pipeline creation, deal progression, and customer health.**  
  He wants “AI, pipeline creation, and progressing deals, as well as health of the customer, in one dashboard, correlated together.”

- **Deal‑progress obsession: “Are we constantly moving this forward?”**  
  In Clari he looks at last updated date and next steps, sorted by amount, and is planning a “top 50 deals” spreadsheet that “flashes red” if a deal isn’t updated within a week. He wants the system to flag deals where notes repeatedly say “no progress” or where next steps are missing.

- **Uses activity signals to diagnose reps, not to manage them.**  
  He says he evaluates reps on just two outputs—pipeline creation and closed business—and then uses activity (People.ai, exec engagement, etc.) to find out if the “car is broken” because they don’t know how (skill) or don’t want to (will).

- **Wants account health integrated: support cases & adoption.**  
  He pushes for “renewals at risk from a health standpoint” combining number of cases, severity (P1s), and product consumption (e.g., Prisma Access licenses used) into an account‑health lens.

- **Also wants visibility into untouched accounts and accounts with no pipeline.**  
  He suggests scoring accounts that haven’t been touched (no ASR, no account plan update, no engagement) and calling out “what accounts have no pipeline,” seeing this as a huge gap in current views.

---

### 2. Cross-Participant Themes

---

**Theme A – Missing: a unified weekly view of rep meetings + pipeline creation**

- Ian wants to know “what meetings are you going on this week?” and “what pipeline did you create [last week]?” with meeting type and quality (net‑new vs PS follow‑up) visible in one place, today only available via calendar sharing plus SFDC. fileciteturn0file0  
- John already built a dashboard for pipeline creation by week/month/quarter per rep and uses People.ai to see meetings, but it’s stitched together manually and not correlated. fileciteturn0file4  
- Tim wants rep‑level dashboards that show activity (face‑to‑face, C‑level meetings, exec outreach, EBCs) plus pipeline creation so he can judge whether reps are doing the right inputs before judging outputs. fileciteturn0file3  
- Amanda wants rep‑level pipeline creation trends over 6+ months, plus conversion rates, to identify reps creating little and closing poorly. fileciteturn0file2  

> Shared gap: there is **no single, time‑sliced view** that brings together *external meetings* + *pipeline creation* + *conversion* at the rep level for DSMs/RSMs.

---

**Theme B – Current reporting is fragmented, manual, and over-complicated**

- Sophia & Mert run Monday “sales initiatives” calls off 30‑slide decks fed by multiple G‑sheets, stopping at regional level; DSM‑level views require extra work and are not self‑serve. fileciteturn0file1  
- Amanda describes renewals visibility as 45 static spreadsheets that are “not authentic,” plus separate risk dashboards and consoles. fileciteturn0file2  
- Tim preps QBRs by hopping through Clari, Sales360, Learning Center, Salesforce reports, etc., then manually melding them into presentations. fileciteturn0file3  
- John has glued together his own dashboards for pipeline creation, commit opps, consumption, and People.ai; he’s now planning a separate top‑50 spreadsheet for deal progression. fileciteturn0file4  

> Shared gap: leaders are **re‑implementing the same logic** in personal spreadsheets and dashboards because no single tool consolidates the signals they actually use for 1:1s, QBRs, and deal/people coaching.

---

**Theme C – Need to elevate sales initiatives (ASR, EBC, plays) as outcome drivers**

- Sophia’s DSM scorecard revolves around ASR completion, 10M+ deals, EBCs, sales plays, and EOS pitching per DSM/AE/account, including the ability to filter for accounts missing each initiative. fileciteturn0file1  
- Mert insists current Workbench mockups are “missing a crucial element”: a high‑level view showing, for example, “100 accounts / 30 ASR completed” as a starting point. fileciteturn0file1  
- Tim uses EBCs, C‑level meetings, and ASRs as non‑negotiable levers in his territory plans and wants simple per‑rep counts and targets surfaced. fileciteturn0file3  
- Amanda wants heatmaps of accounts with no EBC/ASR/exec engagement to push managers into proactive motion, not discovery via slides. fileciteturn0file2  

> Shared gap: **initiatives are treated as sidecar reports rather than core levers**, even though managers correlate them strongly with win/rate and renewal outcomes.

---

**Theme D – Coaching, not just reporting, is the primary use case**

- Ian frames everything in terms of coaching: seeing upcoming meetings lets him ask if SEs know the agenda; seeing last week’s meetings with no pipeline lets him question prep and follow‑up. fileciteturn0file0  
- John evaluates reps on pipeline creation & closed business, then uses activity and account health to diagnose whether they don’t know how vs don’t want to. fileciteturn0file4  
- Tim ties activity & learning metrics to decisions about patience vs escalation with reps (“if they’re doing all the right things… we’ll be patient”). fileciteturn0file3  
- Sophia & Mert want DSMs to spot “the red” (missing ASRs/EBCs, low initiative adoption) and immediately trigger actions (emails, EBC requests) to change behavior. fileciteturn0file1  
- Amanda wants the system to surface reps who aren’t creating pipeline, or whose pipeline continually under‑converts, so leaders can intervene early. fileciteturn0file2  

> Shared need: views must answer **“who do I talk to about what, this week?”** rather than just “what is our coverage %.”

---

**Theme E – Renewals & account health remain under-served**

- Amanda calls renewals the “biggest thing we haven’t solved,” with poor, spreadsheet‑heavy visibility and a belief that better views would directly reduce churn, especially downmarket. fileciteturn0file2  
- John specifically calls for “renewals at risk from a health standpoint” combining case volume, severity, and consumption. fileciteturn0file4  
- Sophia & Mert weave in EBCs and “big deal” initiatives to drive both expansion and renewal of strategic accounts. fileciteturn0file1  
- Tim tracks exec engagement, EBCs and ASRs as leading indicators both for winning deals and de‑risking accounts. fileciteturn0file3  

> Shared gap: there is no **single renewals lens** that merges forecast status, product health, and initiative/engagement coverage for managers.

---

**Theme F – Strong appetite for AI, but only if explainable and tied to action**

- Ian is enthusiastic about AI for analysis and prospecting, but clear that “nothing is gonna replace the human eye”; AI should “speed the data” to understand activity, not replace judgment. fileciteturn0file0  
- John wants AI to detect patterns like repeated “no progress” notes and flag deals where “I don’t think this deal is progressing.” fileciteturn0file4  
- Tim imagines AI auto‑updating account plans from external reports and filling in Sales Play/ASR fields, reducing admin. fileciteturn0file3  
- Sophia & Mert want AI to synthesize initiative signals, surface red/yellow/green, and auto‑draft emails/requests (EBC, ASR). fileciteturn0file1  
- Amanda insists any AI‑based risk labels explain “why we’re saying that they’re high risk,” referencing clear signals like engagement, exec contact, and next steps. fileciteturn0file2  

> Shared need: AI should be **assistive, transparent, and action‑oriented**, not a black‑box “risk score.”

---

### 3. Minority or Contrarian Opinions

---

- **Ian’s de‑prioritization of “sales performance” summaries.**  
  Ian explicitly downplays the need for a top‑level “sales performance/health” tab, saying leaders should already know where they stand via Clari and other tools. This contrasts with Amanda, who still wants the first view to answer “how’s the current quarter going? What’s my gap to plan?” fileciteturn0file0turn0file2  

- **Tim’s lower urgency on stalled‑pipeline analytics.**  
  Tim acknowledges stalled pipeline views (stage aging) are “useful” but “not a necessity,” citing existing Sales360/Clari coverage. John, by contrast, is designing an entire top‑50 deal tracker to monitor deal progression and staleness, and sees it as critical. fileciteturn0file3turn0file4  

- **Different emphasis on initiatives vs pure pipeline.**  
  John boils rep performance down to pipeline creation and closed business, using initiatives and activity only as diagnostics. Sophia & Mert, and Tim, treat initiatives like ASR/EBC/sales plays as primary levers, sometimes more central than raw pipeline. fileciteturn0file4turn0file1turn0file3  

- **Variation in tolerance for complexity.**  
  Sophia and Mert are worried “they’re not gonna look at it because it’s too much,” pushing for radical simplification. John and Tim, while liking visual simplicity, are comfortable with deeper analytic views, referencing multiple tool dashboards they already manage. fileciteturn0file1turn0file3turn0file4  

These tensions are useful design constraints: not everyone wants or needs the same “homepage,” and flexible, persona‑specific entry points will matter.

---

### 4. Insights (from tensions)

---

**Insight 1 – Managers don’t need another “where we are vs plan” view; they need “who/what requires coaching this week.”**

- Tension: Ian shrugs off generic performance dashboards as redundant with Clari, while Amanda expects leaders to begin each day with current‑quarter gap/coverage. Both, however, quickly pivot to questions about **which reps** are not creating pipeline, **which meetings** are happening, and **which renewals** aren’t in commit. fileciteturn0file0turn0file2  
- Design implication: The manager Workbench homepage should be **person‑centric and action‑centric**, oriented around “rep & account exceptions” (e.g., low creation, no exec engagement, high‑risk deals) rather than a static performance cockpit. Classic performance tiles can sit alongside, but shouldn’t dominate.

---

**Insight 2 – The organization treats ASRs/EBCs/sales plays as decisive levers, but they’re invisible or hard to act on in daily manager workflows.**

- Tension: EMEA builds entire scorecards and 30‑slide decks around ASR/EBC/sales plays, and Tim tracks initiative counts because they strongly correlate to win rate. Yet managers still experience them as **spreadsheet and form‑filling work**, not as live, actionable objects in their daily tools. fileciteturn0file1turn0file3  
- Design implication: Sales initiatives should be **first‑class citizens** in the Workbench (with coverage tiles, missing‑initiative filters, and one‑click actions) rather than buried as secondary attributes inside pipeline or activity reports.

---

**Insight 3 – Everyone is already building their own “manager workbench” across tools; the opportunity is consolidation and opinionated flows, not raw data access.**

- Tension: John’s custom dashboards, Tim’s multi‑tool QBR data pulls, Sophia’s DSM scorecard, and Amanda’s renewals spreadsheets each represent different attempts to create a coherent manager cockpit. The fact that every leader is reinventing this wheel suggests the data exists, but **integrated, workflow‑aligned views do not.** fileciteturn0file1turn0file2turn0file3turn0file4  
- Design implication: The Sales Insights Platform should intentionally **replace these homemade systems** by mirroring their structure (weekly inputs, top deals, initiatives, health) and building them into a unified, AI‑assisted Workbench.

---

**Insight 4 – Leaders want AI to highlight patterns, but only when the “why” is inspectable at the level of a coaching conversation.**

- Tension: Leaders are excited about AI (risk scoring, stalled‑deal detection, initiative coverage) but remain skeptical of opaque scores. Amanda explicitly demands clarity on why deals are flagged; John wants AI to spot repeated “no progress” statements; Tim and Ian want AI to speed analysis, not replace their eye. fileciteturn0file0turn0file2turn0file3turn0file4  
- Design implication: Risk and recommendation surfaces must be **explainable and drillable** to the underlying behaviors: e.g., “no exec meeting in 60 days,” “no next steps updated in 21 days,” “no EBC/ASR,” “stage aging > X days.” That explanation is essential to build trust and to turn risk flags into constructive coaching.

---

**Insight 5 – Renewals are structurally under‑managed because data lives outside the mainstream forecast/manager workflow.**

- Tension: Amanda calls renewals visibility “the biggest thing we still haven’t figured out,” with data stuck in static spreadsheets; John wants renewals at risk by health; Sophia/Mert and Tim focus heavily on upstream initiatives that should protect renewals (EBC, ASR, exec outreach). Yet the Workbench concepts so far are more pipeline‑centric than renewals‑centric. fileciteturn0file1turn0file2turn0file3turn0file4  
- Design implication: Renewals (especially non‑EA, downmarket) need their own **first‑class module** in the Workbench, combining forecast status, health telemetry, initiative coverage, and renewal hygiene (owner, stage, next steps) in the same way we treat new business.

---

**Insight 6 – There’s a shared mental model of the manager’s job as a set of cadenced rituals; the Workbench should mirror that cadence in its information architecture.**

- Tension: Tim describes a structured rhythm (weekly account reviews, weekly forecast calls, ongoing development), Amanda distinguishes daily current‑quarter checks from weekly full‑funnel reviews, and Ian insists on weekly snapshots with quarterly roll‑up. Sophia & Mert think about Monday initiative calls and DSM scorecards. fileciteturn0file0turn0file1turn0file2turn0file3  
- Design implication: Instead of a single, monolithic dashboard, the platform should offer **cadence‑aligned views** (Today/This Week, This Quarter, Out‑Quarter Funnel, People & Initiatives) that map directly to forecast calls, pipeline reviews, and 1:1s.

---

### 5. Action Items (Design-Ready Recommendations)

---

**Action Item 1 – Build a “Meetings & Pipeline Creation” coaching view (per DSM & rep)**  

**What to design**  
- A dedicated **Activity & Creation** tab that shows, for each rep in a district/region:  
  - **Current week (upcoming)** external meetings pulled from People.ai/Outlook/Gmail: title, account, attendees, meeting type (PS/post‑sale vs expansion vs net‑new product), and owner.  
  - **Previous week (completed)** external meetings, aligned to **pipeline created** in that period (new opps & expansion opps) with simple badges: “Net‑New,” “Expansion,” “PS/Post‑sale.”  
  - Quick filters: *Previous week’s activity*, *Current week activity*, *Quarter‑to‑date*.  
  - Per‑rep summary tiles: `# external meetings`, `# net‑new meetings`, `# expansion meetings`, `PIPE created`, `PIPE converted (once opps close)`.

**Rationale**  
- Ian described an almost identical dashboard from his Power BI days and sees lack of this view as “an incredible disservice” for coaching. fileciteturn0file0  
- John already tracks pipeline creation by week/month/quarter and uses People.ai activity; he just can’t see them in one combined coaching lens. fileciteturn0file4  
- Tim wants to see if reps are doing the right number and type of meetings (F2F, exec, EBC) alongside pipeline creation before making performance judgments. fileciteturn0file3  

---

**Action Item 2 – Implement a DSM “Sales Initiatives Scorecard” with drill-down and one-click actions**

**What to design**  
- A **Scorecard** tab where a manager selects their name and sees tiles for:  
  - `# accounts`  
  - `% accounts with ASR completed`  
  - `# 10M+ deals`  
  - `# EBCs completed`  
  - `# active sales plays / EOS pitched`  
- Below tiles, two drill‑downs:  
  - **Team view**: AEs in that DSM’s patch with per‑AE initiative metrics.  
  - **Account view**: accounts per AE with ASR/EBC/Play flags.  
- A “Missing…” filter for each initiative (e.g., “accounts with no ASR,” “no EBC,” “no exec outreach”), producing a targetable list.  
- Inline actions on these lists:  
  - “Send reminder email to owners” (pre‑templated, editable, AI‑drafted).  
  - “Create EBC request” pre‑filled with account and relevant contacts.  
  - “Open Sales Play Console for selected accounts” with filters applied.

**Rationale**  
- This is essentially Sophia’s DSM scorecard, but embedded into Workbench and wired to actions instead of slides and G‑sheets. fileciteturn0file1  
- It satisfies Mert’s call for a “starting point” view (“100 accounts / 30 ASR completed”) and his desire to “elevate the data one level up.” fileciteturn0file1  
- It directly surfaces the non‑negotiable metrics Tim uses (EBCs, exec outreach, ASRs) and connects them to actions. fileciteturn0file3  
- Amanda wants heatmaps of “accounts with no executive engagement or activity,” which can be treated as another scorecard tile & filter. fileciteturn0file2  

---

**Action Item 3 – Create a “Rep Performance Diagnostic” panel that triangulates outputs, activity, and learning**

**What to design**  
- For each rep, a **Diagnostic** view (accessible from the Scorecard or People tab) with:  
  - Outputs: `Quota attainment`, `Closed ARR`, `Pipeline created (6–12m)`, `Conversion % by forecast category`.  
  - Activity: `# external meetings`, `# net‑new meetings`, `# EBCs`, `# C‑level meetings`, all over a configurable window.  
  - Learning: completion of key Learning Center paths (per product/role).  
  - Initiatives: ASR/EBC/exec outreach coverage on top accounts.  
- Simple pattern labels using heuristics (not prescriptive judgments), e.g.:  
  - “High activity, low pipeline creation”  
  - “Healthy pipeline, low conversion”  
  - “Low activity & low creation”  
- A short AI‑generated summary for the manager: “Over the last 2 quarters, Jane has high external meeting volume but low net‑new pipeline and below‑average conversion in Best/Commit.”

**Rationale**  
- John explicitly differentiates between reps who “don’t know how” vs “don’t want to” and uses activity to diagnose why pipeline/closed business are low. fileciteturn0file4  
- Tim already pulls People.ai, Learning Center, and pipeline data manually to make this judgment; consolidating it will directly save him time and sharpen coaching. fileciteturn0file3  
- Amanda wants to find reps whose pipeline creation and conversion over 6 months are worrying, not just in‑quarter misses. fileciteturn0file2  

---

**Action Item 4 – Build a “Top Deals Progress Tracker” with explicit staleness & risk explanations**

**What to design**  
- For each DSM/region, an **Opportunities** sub‑view that automatically assembles the top N deals (e.g., top 50 by ARR in current + next quarter(s)) across Commit and Best.  
- Columns: `Amount`, `Stage`, `Forecast category`, `Close date`, `Last updated`, `Next step (text)`, `Owner`, `Key initiative coverage` (ASR/EBC/exec engagement present?), plus a `Risk` pill.  
- Rules‑based and AI‑augmented risk:  
  - Red/Amber/Green risk with tooltips listing **specific reasons**: “No next step; last update 24 days ago,” “Stage 2 for 90 days,” “No EBC/ASR in last 12 months,” “No exec meeting in 60 days.”  
- A visual quadrant (“High value – High risk”, “High value – Low risk” etc.) with hover‑to‑see deals and click‑through into SFDC or Workbench detail.

**Rationale**  
- John is literally building this manually as a spreadsheet that “flashes red” when deals aren’t updated; he sees this as essential to ensure deals are “constantly progressing.” fileciteturn0file4  
- Tim is burned by big deals that quietly slip because opportunity plans were incomplete/stale; he wants attention on deals with gaps in plans and MEDDIC. fileciteturn0file3  
- Amanda is excited about quadrant‑style risk visuals but insists on clearly articulated reasons behind risk labels; this design makes those reasons explicit. fileciteturn0file2  

---

**Action Item 5 – Introduce a dedicated Renewals & Health module**

**What to design**  
- A **Renewals** tab with:  
  - Tiles: `Renewals this quarter`, `Renewals next 2 quarters`, `% in Commit`, `% unowned / no opp`, `Churn rate (trailing 12m)`.  
  - A table of renewals with columns: `ARR`, `Segment`, `Forecast category`, `Owner`, `Health score`, `Exec engagement (Y/N)`, `Last EBC`, `Case volume/severity`, `Product adoption %`, `Risk reasons`.  
  - Filters for segment (EA vs non‑EA; enterprise vs commercial vs SMB), plus downmarket focus.  
- Health score and risk reasons similar to Top Deals Tracker: e.g., “High P1 case volume,” “Low adoption,” “No exec activity in 90 days,” “No EBC/ASR,” “No renewal opp created.”

**Rationale**  
- Amanda calls renewals visibility a major unsolved problem that still lives in “45 different spreadsheets,” and links better visibility to improving churn. fileciteturn0file2  
- John specifically wants renewals risk from a health standpoint (cases + consumption). fileciteturn0file4  
- Sophia/Mert and Tim are already pushing initiatives (EBC, ASR, exec outreach) that correlate strongly with renewal success; surfacing these against renewal lists makes that work tangible. fileciteturn0file1turn0file3  

---

**Action Item 6 – Re-structure navigation around manager cadences: Today/This Week, This Quarter, Funnel, People**

**What to design**  
- Top‑level tabs (or a left‑rail) that mirror the manager’s rituals:  
  - **Today / This Week** – current‑quarter KPIs + exceptions (gap to plan, top high‑risk deals, renewals this q) plus “Meetings & Pipeline Creation” summary.  
  - **This Quarter** – linearity vs same time last year, current‑quarter funnel, commit/best coverage, Top Deals Tracker.  
  - **Funnel / Out‑Quarter** – pipeline creation by time and product, out‑quarter coverage, conversion by forecast category.  
  - **People & Initiatives** – DSM Scorecard, Rep Performance Diagnostic, initiative coverage, learning.  
- Each view should expose a small list of **pre‑defined questions** (chips/buttons) that, when clicked, adjust filters (e.g., “Who created zero pipeline in the last 30 days?”, “Which accounts have no pipeline and no EBC?”).

**Rationale**  
- Tim thinks in terms of pipeline review vs forecast call vs 1:1/development sessions and wants views aligned to those motions. fileciteturn0file3  
- Amanda explicitly differentiates daily (current q) vs weekly (out‑quarter/funnel) cadences. fileciteturn0file2  
- Ian wants Activity and Opportunity as his key categories, and Sophia/Mert want a simple “outer onion” high‑level view with drill‑down. fileciteturn0file0turn0file1  

---

**Action Item 7 – Make AI risk and insights explicitly explainable and coach-friendly**

**What to design**  
- Any AI‑generated label (e.g., “High‑risk deal,” “At‑risk account,” “Rep underperforming in creation”) must show:  
  - A **short human‑readable explanation** (“Marked high risk because: no exec meeting in 60 days; stage 3 for 75 days; no next step set; no recent EBC/ASR”).  
  - The underlying data points (dates, counts, stages) accessible via hover or flyout.  
- In the chat/QA panel, when managers ask questions like “Why is Deal X high risk?” or “Why is Rep Y flagged?”, the assistant should answer in this same, concrete, evidence‑based format.

**Rationale**  
- Amanda’s explicit requirement is being “super clear on why we’re saying that they’re high risk,” listing concrete factors like engagement, exec activity, and next steps. fileciteturn0file2  
- Ian, Tim, and John are all comfortable with risk/AI as long as it’s grounded in familiar behaviors (staleness, stage, lack of initiatives) and remains subordinate to human judgment. fileciteturn0file0turn0file3turn0file4  

---

If you’d like, next we can take one of these (for example, the **Meetings & Pipeline Creation view**) and sketch it out more concretely—down to fields, filters, and example screen flows tailored for DSM vs RVP.

