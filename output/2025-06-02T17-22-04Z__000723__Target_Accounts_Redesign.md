# Target Accounts Redesign

## You (2025-06-02T17:22:04.253000+00:00)

earlier we had a dashboard view that looked something like this...

[attached image]

Based on the following feedback, help me essentially rethink/restructure/redesign the content around the account rows and section.

---

Feedback:

Account Views: What’s Needed
1. Target Accounts Section
A. Explicit Feedback Tie-Back
Prasanna:

“Empower sales representatives managing 100+ accounts to efficiently identify, prioritize, act upon, and track critical opportunities and risks.”

“Surface a manageable number (e.g., top 5–10) of the most critical accounts and their single most urgent action from the representative’s entire book of business.”

“Clearly define, and make transparent... the logic and criteria (e.g., urgency, potential revenue, risk score, days to close) that determine which accounts/actions are flagged as ‘most critical.’”

Lavina:

“Showcase some areas which can be clicked.”

“Ability to look at Sales play/renewals that tab on the top.”

B. Specific, Unambiguous Requirements
i. Target Accounts Identification

The view must show a prioritized list of “Target Accounts,” not just all accounts.

Target Accounts = accounts that meet at least one “critical” criteria (at risk, high value, upcoming renewal, upsell/cross-sell opportunity).

How to visually mark: Use a clear badge, highlight, or pin at the top of the section—do not bury Target Accounts among others.

ii. Ranking Logic (make transparent)

Display to user why each account is a target (e.g., “At risk renewal,” “Large deal,” “High cross-sell potential,” etc.)

Action: Each account tile must have a “reason for priority” label, always visible.
(“Critical: Renewal at risk”, “Critical: Large Q-end deal”, etc.)

iii. One-click Filtering by Tab

Sales Plays and Renewals tabs must instantly filter the Target Accounts to only those where those plays or renewals are relevant.

Action: Clicking “Renewals” only shows accounts with active/at-risk renewals.

iv. Actionability (Clickability)

Every Target Account must have at least one clickable action:

Critical Action pill/card

Sales Play available

Account Insight details

Consumption/Usage badge or trend

On click: Show supporting data (modal, side panel, or detail screen), ideally pulling (or mock-showing) underlying Salesforce fields, next steps, or insights (as Lavina requested).

v. Consumption Data

Each Target Account must surface consumption/engagement trend (not just a static number)—badge (Low/Med/High) or arrow, always visible.

Clicking badge opens usage trend chart or detail.

2. Account Insights Section
A. Explicit Feedback Tie-Back
Prasanna:

“Design UI elements that clearly demonstrate how product adoption metrics (or lack thereof) are factored into account health scores and renewal risk assessments.”

“Integrate adoption data to proactively suggest specific upsell/cross-sell opportunities or relevant Sales Plays.”

“Provide direct links to underlying data (e.g., declining account health scores, low engagement metrics).”

Lavina:

“Showcase some areas which can be clicked.”

“Showcase Consumption data more prominently for the accounts with a view on trending low, medium, high.”

B. Specific, Unambiguous Requirements
i. Insights Breakdown & Visualization

Show at least these four metrics for each account:

Retention Score (with visual badge/trend)

Expansion Potential (with badge/trend)

Engagement Score (with badge/trend)

Account Health (flag: “Critical,” “At Risk,” etc.)

Action: Each metric is not just a number—it must have a badge, color, or icon (e.g., green/yellow/red, up/down arrow) indicating trend/urgency.

ii. Clickable Insights

Each metric/badge is clickable:

On click: Reveal supporting data (trend over time, what’s driving the score, recommended action, pulled or mock-pulled from Salesforce or product analytics).

Example: Clicking “Engagement: 6.3 ↓” opens a mini-trend graph and notes (e.g., “Logins down 22% MoM. Suggest: Customer check-in.”)

iii. Account-Level Critical Actions

Each Account Insight section must surface a “most urgent action” (pulled from Salesforce/CRM logic).

“Initiate Exec check-in,” “Review renewal risk,” “Run Upsell Play”—always shown, always clickable.

On click, bring up SFDC-aligned details and an “Action” modal for workflow.

iv. Sales Play Integration

If a Sales Play is recommended for this account, surface as a badge or pill.

Click = opens Sales Play details (key messages, playbook, attach to opportunity).

v. Consumption Data

Consumption or adoption trend must be prominent (NOT just a number).

Use a bar, trend arrow, or badge for “Low/Medium/High.”

Clicking gives a consumption detail pane or graph.

-----

Imagine I'm a UX designer and you're giving me feedback based on your knowledge as an account executive. Give me realistic data while thinking through your work.

## ChatGPT (2025-06-02T17:22:05.293672+00:00)

Great — thanks for pulling this together and sharing the feedback. Here’s how I’d rethink and restructure the **“Account Rows”** and broader **Account Insights section** from the lens of a field AE who needs to triage 100+ accounts at speed. I'll split my feedback into **structure**, **function**, and **data realism**, reflecting what would truly make the experience action-driven and quota-impacting.

---

### 🔁 **Proposed Structural Redesign of the “Account Rows” Section**

#### 1. **Rename Section: “Target Accounts” → “Top Priority Accounts”**
This better aligns with the sales mindset: urgency and importance. The logic should be:

> **“These are the 5–10 accounts where action today moves your Q target forward.”**

---

### 🧱 **Account Row Redesign Structure (What the AE Sees)**

Each account row becomes a **summary tile** with the following sections:

---

#### ✅ **A. Account Header:**
- **[Logo] [Account Name] [Segment + Industry]**
- **Badges for priority trigger(s)**:
  - 🔴 `Critical: Renewal at Risk`
  - 🟡 `Upcoming Renewal: 29 Days`
  - 🟣 `High Expansion Potential`
  - 🟢 `Sales Play: Prisma SASE`

---

#### 📊 **B. Insight Summary Bar (Left to Right)**:
- **Retention Score:** `78 ↑` (trend icon)
- **Expansion Potential:** `6.5 →`
- **Engagement Score:** `6.3 ↓`
- **Consumption Trend:** `Medium ↓` (click to open 30-day graph)
- **Account Health:** `⚠️ At Risk` or `✅ Healthy`

> **Color-coded, arrow-trended**, and **all metrics are clickable.**

---

#### 🧠 **C. Critical Action (Right-Aligned)**:
A **single pill** with the most urgent action:
- 🟩 `Review Renewal Risk`
- 🟦 `Run Cross-Sell Play`
- 🟥 `Initiate Exec Check-In`

> **Clickable: Opens modal with supporting data + suggested next step.**

---

#### 🔗 **D. Quick Access Buttons (Optional, Compact Icons)**:
- Salesforce icon = open Opp
- Playbook icon = open Sales Play
- Graph icon = open consumption trend
- Email icon = trigger outreach template

---

### 🧠 **Functionality / Filters (Above the Row List)**

Make this area surgical. Filters should be:

- `🔁 Renewals`
- `📈 Upsell/Cross-Sell`
- `⚠️ At Risk`
- `💼 Sales Plays`
- `⬆️ Consumption Dip`

Toggles should **dynamically filter** the account row list — like a heatmap filter for pipeline gaps.

---

### 📐 **Design Feedback: Strategic Tie-Backs to User Feedback**

#### ✅ Prasanna’s Point: “Transparency of Logic”
We **badge** the “why” for priority right up front — no need to dig.

#### ✅ Lavina’s Point: “Clickability”
Every metric and action is **clickable** — revealing a focused modal with underlying data.

---

### 📊 **Supporting Data (What the AE Would Want to See)**

#### Example Account Tile: “InnoWave Technologies”
- **ARR:** $212,345 — Renewal in 29 days
- **Retention Score:** 44.4 (🔻 over 90 days)
- **Engagement:** 6.3 (🔻 -22% logins MoM)
- **Expansion Potential:** 5.5 (→)
- **Consumption:** Low (↓ 15% usage on Prisma Cloud)
- **Sales Play Active:** Cortex XDR Consolidation
- **Critical Action:** 🔴 “Schedule Exec QBR (Last: 180 days ago)”

> AE clicks “Retention Score” → Sees trendline, usage breakdown, last support ticket, AE notes.

> AE clicks “Critical Action” → Sees QBR date, prior notes, scheduler button.

---

### 🎯 Sales Behavior Enablement

This design delivers the **“attention economy”** we live in. It lets us:

- Prioritize what moves pipeline *now*
- Take action in 1–2 clicks
- Justify outreach with real, transparent data
- Use product usage signals to drive upsell plays

---

### 📎 Summary

The redesigned **account tile** becomes a live command center — not just a list. It answers:
> *“What’s happening, why should I care, what should I do next?”*

Let me know if you'd like a quick wireframe-style sketch or Figma-ready content structure breakdown — happy to mock that up too.

## You (2025-06-02T17:24:05.283000+00:00)

segregate this data into info that

'brings your attention to the account' and 'lets you understand in more detail'. right now the tiles are too big and we need some form of expanded and collapsed view

## ChatGPT (2025-06-02T17:24:05.932271+00:00)

Absolutely — that makes a ton of sense. As an AE, **collapsing the noise to surface just what's urgent**, then giving me the **option to expand** into detail **when I choose**, is the ideal UX. Here’s how we can restructure the content of each account tile into two layers:

---

## 🔔 Collapsed View (Brings Your Attention to the Account)

Think of this as the **headline layer** — just enough to say *“Hey, pay attention to this account right now.”*

### ✅ What’s Shown in Collapsed State:
#### 🔹 Account Identification
- **[Logo] Account Name**
- **ARR / Segment / Industry (small font)**

#### 🔹 Priority Trigger(s)
- 🔴 `Critical: Renewal at Risk`
- 🟣 `High Expansion Potential`
- 🟡 `Renewal in 29 Days`
- 🟢 `Sales Play Available`

> Limit to **max 2 visible badges**, rest collapse into a "+2 more" dropdown.

#### 🔹 Most Urgent Action
- `⚠️ Schedule Exec Check-in`
- `🔁 Review Upcoming Renewal`
- `📈 Run Cross-Sell Play`

> One-line, color-coded pill. **Clickable**.

#### 🔹 Key Metric Snapshot (Mini-Badges)
- Retention: `78 ↑`
- Engagement: `6.3 ↓`
- Consumption: `Medium ↓`

> Display as compact **icon-badges**, not full score blocks. All are **clickable**, tooltipped, and drive into detail.

---

## 🔍 Expanded View (Lets You Understand in More Detail)

Only shown **when the user clicks to expand** or **hovers on mobile**. Think of this as **“I need to know *why* this is flagged.”**

### 🧩 What’s Revealed in Expanded State:
#### 📊 Full Metric Breakdown
- Retention Score: `78 ↑`
  > Trend: +6pts QoQ
  > Driver: Support CSAT 92%

- Engagement: `6.3 ↓`
  > Trend: -22% MoM logins
  > Driver: No XDR console activity

- Expansion Potential: `6.5 →`
  > Signals: Interest in Prisma SASE logged in Salesforce

- Account Health: `⚠️ At Risk`
  > Composite of declining engagement + renewal proximity

#### 📉 Consumption Detail
- **Current Adoption:** Medium
- **30-day Trend:** ↓ 15% usage
  > Click opens mini trend chart modal

#### 🧠 Action Center
- Most Urgent Action (Same as collapsed)
- ✅ Secondary suggestions:
  - Review stalled opportunity
  - Re-engage SE

#### 📚 Sales Play (if applicable)
- Badge: `💼 Prisma SASE`
- Click opens: key messages, pitch assets, attach play

---

### 🧰 Suggested UX Behaviors

| State | Interaction | Result |
|------|-------------|--------|
| Collapsed | Click on metric or badge | Expands detail drawer |
| Expanded | Click “Most Urgent Action” | Opens Action Modal |
| Hover (desktop) | Show detail tooltip or quick chart | Enhances scan-ability |
| Mobile tap | Tap to toggle expanded view | Keeps it touch-friendly |

---

### 🧠 AE Mental Model

As a rep, my scan path is:

1. **Who needs my attention?** → [Collapsed view]
2. **Why is this critical?** → [Expand]
3. **What should I do about it?** → [Click actionable pill or metric]

This layered design matches how we mentally triage pipeline risk.

---

Want me to sketch this tile layout visually? Or annotate the existing screenshot with collapsed vs. expanded cut lines?

## You (2025-06-02T17:25:31.391000+00:00)

do you have retention score as a valid metric at PANW? how would you define it and how would you calculate it?

## ChatGPT (2025-06-02T17:25:32.056524+00:00)

Excellent call-out. The term **"Retention Score"** isn’t an official, codified metric at Palo Alto Networks (like NRR or CSAT might be), but the concept **does map to how top AEs and CS teams intuitively assess customer stickiness and renewal likelihood.** So let’s unpack how you’d define and operationalize it *in the context of PANW* — especially in an internal dashboard.

---

## 🔁 **What Would “Retention Score” Mean at PANW?**

It would be a **composite, forward-looking signal of renewal likelihood** — driven by product engagement, support satisfaction, account behavior, and known risk flags.

Think of it as a **risk-weighted score between 0–100**, where:

- **90–100** = Very Likely to Renew
- **70–89** = Likely
- **50–69** = At Risk
- **<50** = Critical

---

## 🧮 **How Could PANW Calculate a Retention Score?**

Here’s a plausible scoring model based on internal behavior and available signals across Strata, Prisma, and Cortex customers:

### 🧠 **1. Product Adoption Score (35%)**
- Prisma/NGFW/XDR usage trends (30-day/90-day)
- % of licensed features in use
- Telemetry adoption (e.g., ADEM for Prisma Access)

🟢 High = Daily/weekly usage, feature breadth
🔴 Low = Little to no telemetry, stale deployment

---

### 📞 **2. Support Experience (20%)**
- # of critical tickets in last 90 days
- Time to resolution
- CSAT score if collected

🟢 High = No Sev 1s, CSAT >90%
🔴 Low = Active Sev 1, CSAT <70%

---

### 👥 **3. Engagement Score (15%)**
- Exec sponsor participation
- QBR attendance
- Open renewal conversation in SFDC

🟢 High = Engaged CISO, regular cadence
🔴 Low = Ghosted, no AE/SE touches in 90+ days

---

### 🧾 **4. Commercial Risk Signals (15%)**
- Contract <60 days to renew
- Procurement delays
- Discounts > standard

🟢 Low = No redlines, renewal doc in flight
🔴 High = Legal stall, finance pushback

---

### 📊 **5. Historical Behavior / Trendline (15%)**
- Prior renewal behaviors
- Deal slippage pattern
- Seat shrink in past

🟢 Positive = Multi-year renewals in past
🔴 Risk = Shrinking ARR YoY

---

## 🧪 Example Formula (Simplified):

```text
Retention Score =
(Adoption * 0.35) +
(Support * 0.20) +
(Engagement * 0.15) +
(Commercial * 0.15) +
(Trendline * 0.15)
```

Where each component is normalized to a 0–100 scale.

---

## 🧭 Why This Metric is Useful (if surfaced)

As an AE:
- I **know what’s driving the risk** — not just that risk exists.
- I can **correlate usage drops to churn signals.**
- I can **proactively triage** customers who *look fine on the surface (healthy ARR)* but are actually slipping.

As a CS or Renewal Specialist:
- I can stack rank accounts for **pre-renewal interventions**.

---

### ✅ Final Thoughts

We don’t formally call it a “Retention Score” in internal systems, but we *absolutely think this way.* If you name it transparently and tie it to known inputs (support, usage, engagement, etc.), you’ve got a credible and useful health proxy that AEs and CS teams will actually trust — and use.

Want help mapping this into a Figma annotation or user-facing tooltip text to explain what the score means?

## You (2025-06-02T17:27:03.422000+00:00)

leave out the retention score for now, rethink the expanded and collapsed view and while designing it, tie it back to the feedback from prasanna and lavina

## ChatGPT (2025-06-02T17:27:04.225078+00:00)

Perfect — let’s re-approach the **collapsed vs. expanded view** design without using a "Retention Score," while still fully respecting the intent behind Prasanna and Lavina’s feedback.

---

## 🔁 Rethinking the **Account Tile** With a Collapsed / Expanded Design

> 🎯 **Goal:** Give AEs a fast, prioritized scan of which accounts matter most (collapsed), with easy access to rich, contextual insights and actions (expanded) — without overwhelming them.

---

## 🔹 Collapsed View = “Scan and Triage Mode”

This is your **default**, **dense**, and **high-signal** view. Designed for:
- Surfacing urgency
- Scannable prioritization
- One-click action

### 🔒 Collapsed View: Content Layout

**1. Top Bar (Left to Right)**
- **Account Name** | Segment | ARR
- **Badges (priority logic)**
  - 🔴 `At Risk Renewal`
  - 🟡 `Upsell Signal`
  - 🟣 `Sales Play Available`

**2. Consumption + Engagement Strip**
- **Adoption Trend Badge**: 🔽 Low / Medium / High (with arrow)
- **Engagement Badge**: 🔽 (based on activity/usage or SE notes)

**3. Most Urgent Action Pill**
- E.g. `📞 Schedule Exec Check-In`, `📁 Finalize Renewal`, `💡 Run Upsell Play`
- **Clickable** — opens contextual modal or next-step panel.

**4. Expand Icon**
- ➕ expands to reveal detailed insights.

> 📌 Tie to **Prasanna’s** feedback: This view **prioritizes**, **surfaces urgency clearly**, and **makes logic visible** via badges like `Critical: Renewal`, `High Value`, etc.

> 📌 Tie to **Lavina’s** feedback: Each element is **clickable** (badges, action pills, expand icon).

---

## 🔓 Expanded View = “Understand and Act Mode”

Activated only when needed — on click, hover, or tap — to **diagnose and execute**.

### 🔓 Expanded View: Content Layout

**1. Top Section**
- Full **Account Header**
- **Action Icons** (tiny SFDC icon, email, playbook link)

**2. Insights Grid** (visually chunked)
| Metric | Value | Trend | Click for... |
|--------|-------|--------|--------------|
| **Engagement** | 6.3 | 🔻 22% MoM | Mini trend + recent activity |
| **Expansion Potential** | Medium | → | Feature usage / SE notes |
| **Health Status** | `At Risk` | — | Breakdown of risk drivers |
| **Consumption** | Medium | 🔽 | 30-day usage graph |

> 🔗 All metrics are **clickable**. Tooltip or modal shows:
> - What’s driving the trend?
> - What’s the recommended action?
> - Link to underlying system (Salesforce, telemetry, etc.)

**3. Sales Play Section**
- `💼 Prisma SASE Available`
- Click to view playbook assets, customer references, attach to opp.

**4. Supporting Context**
- Last QBR held: `180 days ago`
- Open opps: `1 (Q3 Close Target)`
- CSAT (if known): `89% last 30d`

> 📌 Tie to **Prasanna’s** feedback:
> - “Logic transparency” → all metrics show **what’s driving them**
> - “Actionability” → every tile includes **next step** AND links to **underlying data**

> 📌 Tie to **Lavina’s** feedback:
> - All metrics and insights are **clickable**
> - Usage and health trends are **visual and prominent** (badges, trend arrows, mini charts)

---

## 🔧 Implementation Notes (UX Suggestions)

| Behavior | Interaction | Outcome |
|----------|-------------|---------|
| Click badge | Opens tooltip/modal | Shows score drivers |
| Click Action Pill | Opens workflow modal | Triggers task, outreach, Salesforce note |
| Expand toggle | Slide-down drawer | Rich insights appear |
| Collapsed state | Default on page load | Fast triage for AEs managing 100+ accounts |

---

## 🧠 Final AE Value

This design allows me to:
- **Prioritize instantly** (“Who needs me now?”)
- **Act efficiently** (“What should I do next?”)
- **Drill in smartly** (“Why is this flagged?”)
- **Trust the logic** (badges reflect transparent criteria)

Let me know if you'd like this visually mocked up as a wireframe, or if you'd like to test this interaction pattern live in Figma — we could tag certain accounts with test data and simulate click-through behavior.

## You (2025-06-02T17:47:05.818000+00:00)

ok, this is the structure for the collapsed view. Could you create 5 rows like this with the same informaiton structure but with some realistic data

## ChatGPT (2025-06-02T17:47:07.366671+00:00)

Absolutely — here are 5 realistic collapsed view rows based on Palo Alto Networks AE context, incorporating meaningful Signals, Performance indicators, ARR ranges, and next-best Actions:

---

### **1.** **TechNova Solutions** | Professional Services | Mid-Market
**ARR:** **$212,378**
**Signals:**
🔴 *At Risk Renewal* 🟡 *Upsell Signal* 🟦 *Sales Play Available*
**Performance:**
🔼 *High Adoption* 🔽 *Low Engagement*
**Actions:**
✨💡 *Run Upsell Play* [+2 more]

---

### **2.** **InnoWave Technologies** | Manufacturing | Enterprise
**ARR:** **$587,000**
**Signals:**
🔴 *Renewal in 29 Days* 🟣 *Cross-Sell Potential* 🟦 *Sales Play Available*
**Performance:**
🔽 *Low Adoption* 🔽 *Low Engagement*
**Actions:**
📞💡 *Schedule Exec Check-in* [+2 more]

---

### **3.** **Quantum Dynamics Inc.** | Software Development | Enterprise
**ARR:** **$1,034,212**
**Signals:**
🟡 *High Expansion Value* 🟣 *Sales Play Available*
**Performance:**
🔼 *Medium Adoption* 🔼 *Medium Engagement*
**Actions:**
📁💼 *Review Open Opps* [+2 more]

---

### **4.** **Medix Global** | Healthcare | Strategic
**ARR:** **$3,245,980**
**Signals:**
🔴 *Churn Risk* 🟣 *Upsell Signal* 🟦 *Sales Play Available*
**Performance:**
🔽 *Low Adoption* 🔽 *Low Engagement*
**Actions:**
🚨💡 *Escalate to CS/Exec Sponsor* [+2 more]

---

### **5.** **ByteLink Systems** | Technology | Commercial
**ARR:** **$143,980**
**Signals:**
🟡 *New Use Case Detected* 🟣 *Sales Play Available*
**Performance:**
🔼 *High Adoption* 🔼 *High Engagement*
**Actions:**
🎯💡 *Attach New Logo Use Case Play* [+2 more]

---

Would you like me to turn these into a visual mock (replicating the style in your screenshot) or annotate what the +2 actions could be for each row?

## You (2025-06-02T18:01:29.945000+00:00)

Actually, I'd like you to internally recap all the feedback form prasanna and lavina, and give me an expanded view for the following accounts from your list that addresses the feedback they both had for this iteration.

Medix Global
Technova Solutions
ByteLink Systems

## ChatGPT (2025-06-02T18:01:30.638877+00:00)

Here’s how I’ve structured the **expanded views** for the three accounts — Medix Global, TechNova Solutions, and ByteLink Systems — based directly on **Prasanna and Lavina’s feedback**.

---

## ✅ Feedback Summary (Internalized)

### 📌 **Prasanna’s Feedback (Strategic + Action-Oriented):**
- Prioritize a small number of **most critical accounts**
- Make the **logic for prioritization transparent**
- Highlight the **single most urgent action**
- Show **consumption and adoption trends**, not just point-in-time numbers
- Show **recommended sales plays** where applicable

### 📌 **Lavina’s Feedback (UX + Clarity):**
- Everything must be **clickable** (badges, actions, metrics)
- Use **trend visuals** (↑↓ arrows, badges, bars)
- Show **consumption levels prominently**
- Make **sales plays discoverable and accessible**
- **Action pills must lead somewhere** (workflow, SFDC pane, etc.)

---

## 🔍 Expanded Views

---

### 🧠 **1. Medix Global**
*Healthcare | Strategic | ARR: $3,245,980*

#### 🚩 Priority Logic
- 🔴 *Churn Risk Detected*
- 🟡 *Upsell Signal from Cortex Usage*
- 🟦 *Sales Play Available (Cortex XSIAM Consolidation)*

#### 📉 Performance Breakdown
| Metric | Value | Trend | Click Result |
|--------|-------|-------|---------------|
| **Adoption** | Low | 🔻 -28% usage over 30d | Opens trend graph by product area (e.g., Cortex, Strata) |
| **Engagement** | Low | 🔻 2 QBRs missed, no SE touch in 90d | Shows Salesforce engagement log |
| **Health** | At Risk | Composite score below renewal threshold | Opens breakdown by telemetry + CS alerts |

#### 🔢 Consumption Signal
- **Current Level:** Low
- **Driver:** XSIAM agent deployment stalled at 60%
- **Trend:** ↓ –25% in login activity MoM

#### 🎯 Action Center
- **Primary Action:** 🚨 *Escalate to CS/Exec Sponsor*
- **Secondary:** 📅 Schedule QBR, 📈 Present Cortex Consolidation ROI

#### 🧰 Sales Play Integration
- `💼 Cortex XSIAM Consolidation`
- **Click to view**: Playbook PDF, TCO calculator, win stories

---

### 🧠 **2. TechNova Solutions**
*Professional Services | Mid-Market | ARR: $212,378*

#### 🚩 Priority Logic
- 🔴 *At Risk Renewal (<30d)*
- 🟡 *Upsell Signal from Prisma Access traffic growth*
- 🟦 *Sales Play Available (Prisma SASE Upgrade)*

#### 📉 Performance Breakdown
| Metric | Value | Trend | Click Result |
|--------|-------|-------|---------------|
| **Adoption** | High | 🔼 +35% usage QoQ | Opens product usage by SKU chart |
| **Engagement** | Low | 🔻 No execs in last QBR, SE flagged low responsiveness | Opens engagement timeline |
| **Health** | At Risk | Renewal flagged w/ discount ask & slow replies | Opens renewal opp notes in SFDC

#### 🔢 Consumption Signal
- **Current Level:** Medium–High
- **Driver:** Steady increase in Prisma throughput + new mobile users
- **Trend:** ↑ Consistent 10% MoM

#### 🎯 Action Center
- **Primary Action:** 📞 *Run Upsell Play (Prisma SASE)*
- **Secondary:** 📨 Email renewal proposal, 🛠️ Attach ADEM for visibility boost

#### 🧰 Sales Play Integration
- `💼 Prisma SASE Cloud Migration`
- **Click to view**: Key messages, customer reference deck, attach-to-opp button

---

### 🧠 **3. ByteLink Systems**
*Technology | Commercial | ARR: $143,980*

#### 🚩 Priority Logic
- 🟡 *New Use Case Detected (ZTA interest from SE notes)*
- 🟦 *Sales Play Available (ZTA + Prisma Access)*

#### 📉 Performance Breakdown
| Metric | Value | Trend | Click Result |
|--------|-------|-------|---------------|
| **Adoption** | High | 🔼 +42% Prisma Access increase | Opens feature-level adoption chart |
| **Engagement** | High | 🔼 Active POC, regular SE connects | Opens notes from SE weekly syncs |
| **Health** | Healthy | Trending positive | No open risks logged

#### 🔢 Consumption Signal
- **Current Level:** High
- **Driver:** Secure hybrid work enablement
- **Trend:** ↑ Volume spike as remote access use cases expand

#### 🎯 Action Center
- **Primary Action:** 🎯 *Attach New Logo Use Case Play*
- **Secondary:** 📊 Pitch Zero Trust Outcomes, 📝 Prep case study opportunity

#### 🧰 Sales Play Integration
- `💼 Prisma Access for ZTA`
- **Click to view**: Use case deck, implementation roadmap, success plan doc

---

Let me know if you'd like to mock these up visually, or want the +2 actions per account mapped to SFDC workflows or GTM assets.

## You (2025-06-02T18:02:40.456000+00:00)

in one of your earlier responses, you also mentioned some of the additional links like salesforce button, etc... that need to be added. Could you just recap that for me?

## ChatGPT (2025-06-02T18:02:41.169381+00:00)

Absolutely — here’s a focused recap of the **quick-access buttons and supporting link-outs** I recommended earlier for the **expanded view** (and possibly as hover-accessible in collapsed view). These are based on how top AEs at PANW work day-to-day — jumping between Salesforce, GTM content, and customer context.

---

## 🔗 **Quick-Access Actions / Buttons (Expanded View)**

These buttons are meant to make the tile *execution-ready* — not just informative.

| Icon | Function | Use Case |
|------|----------|----------|
| 🗂️ **Salesforce Icon** | Opens the related Opportunity, Renewal record, or Account in Salesforce | Needed to check stage, notes, close date, quote status |
| 📎 **Playbook Icon** | Opens relevant **Sales Play content** (PDF, battlecard, pitch deck) | AE clicks to prep for call, attach to opp |
| 📈 **Graph/Trend Icon** | Opens **consumption dashboard** or mini trend chart | For investigating usage anomalies or growth |
| ✉️ **Email Icon** | Launches template for **Exec QBR outreach, renewal notice**, etc. | Sends templated messaging via Gmail/Outreach |
| 🧭 **Next Step / Workflow Icon** | Opens a **task modal** (e.g., “Schedule QBR,” “Submit Quote Request”) | Links to internal workflow or CRM task |

---

## 💡 **Behavioral Notes**
- Buttons should **appear in expanded view** but also be accessible via hover tooltip or drawer in collapsed mode.
- Every **Primary Action Pill** (e.g., `📞 Schedule Exec Check-in`) should **open a workflow modal or Salesforce pane** when clicked — **no dead ends**.

---

## 🧠 AE Rationale

These link-outs directly support:
- 🔍 Diagnosing (Salesforce, consumption, SE notes)
- 🎯 Acting (email, attach play, launch task)
- 🔄 Context-switching without tab chaos

Want a row mockup with these icons visibly embedded and labeled? Happy to help sketch or annotate.
