# Scope document synthesis

## You (2025-12-02T20:53:20.133000+00:00)

> **You are to act with a dual mindset:**
>
> * As a **Technical Sales Executive at Palo Alto Networks**, focused on opportunity lifecycle, proof of value (POV), tech wins, solution selling, and SC workflows.
> * As a **Design Manager at IDEO**, skilled at translating ambiguous, messy, timestamped input into clear, actionable design directions that are friction-sensitive and user-centered.

---

### 📥 INPUT

You have been provided with:

* A **transcript** of a meeting related to the **Technical Seller Experience (TSX)** platform, including the sales engineering persona, workflows, goals, and product artifacts.
* A series of **screenshots with timestamps** taken during the same meeting.

Your first task is to **internalize the full story**. Assume the meeting played out linearly. Any **transcript content that overlaps with a screenshot timestamp** (e.g., transcript from 00:55–01:20 and screenshot from 01:00) is considered contextually bound. That binding persists **until the next screenshot timestamp**.

You must **synthesize the full narrative**, matching dialogue and visuals to form a coherent mental model of the intent, priorities, and pain points expressed.

---

### 🧠 BEHAVIOR

* Think first **individually** through the lens of each persona — Technical Sales Executive and Design Manager — and then provide **a single synthesized perspective**.
* Do **not separate thoughts into distinct persona outputs**.
* Do **not surface internal “thinking aloud” monologues** — only give refined, aligned reasoning and output.

---

### 📄 OUTPUT STRUCTURE

Produce a **comprehensive Scope Document** composed of multiple objectives. For each objective, follow this structure:

---

#### 🔹 Objective #[N]: [Short Objective Title]

* **Problem Statement:**
  A clear articulation of the friction or challenge observed. Focus on what is **ambiguous, inefficient, or confusing** in the current experience.

* **Functional Modules Affected:**
  Reference specific components or flows (e.g., TRR, Artifact Repository, POV Execution, Opportunity View, Engagement Tracker).

* **Design Considerations:**
  Where applicable, add key interface, user flow, or information architecture implications.

* **Screenshot and Transcript References:**
  Use structured format (e.g., `[Screenshot – 01:00]`, `[Transcript – 00:55–01:20]`).

* **Detailed User Stories:**
  Write **fully structured user stories** with explicit context, e.g.:

  > *As a [Technical Seller], I want to [access previously used POV test plans for similar accounts], so that I can [reduce effort in rework and maintain alignment with similar solution profiles].*

  Use **full forms for all abbreviations** (e.g., TRR = Technical Resource Request, POV = Proof of Value).

---

### 🧩 FINAL SECTION: Unanswered Questions & Assumptions

After listing all objectives and user stories, provide a **conclusion section** titled:

> #### ❓ Outstanding Gaps & Assumptions

In this section, identify:

* Any **unanswered questions** or requests in the transcript that weren’t addressed.
* Any **design-critical data points missing** from the discussion.
* Any **assumptions** made by the team or inferred in the meeting that should be validated before continuing.

---

### 🛑 DO NOT:

* Generate generic user stories.
* Discuss backend feasibility or tech stack limitations.
* Include post-sales Customer Success modules or legacy systems not mentioned.
* Use vague phrasing like “optimize workflow” without identifying what exactly is broken or unclear.

---

## ChatGPT (2025-12-02T21:10:25.420891+00:00)

#### Scope Document – TSX (Technical Seller Experience) Workbench
Persona: Solution Consultant / Technical Seller at Palo Alto Networks

---

### 🔹 Objective #1: Opportunity‑Centric Technical Seller Workbench

**Problem Statement**
Solution Consultants work in lockstep with sales reps on opportunities but currently rely on a patchwork of Salesforce views, spreadsheets, Google Drive folders, and external tools. There is no single TSX “home” that gives a technical, opportunity‑centric view while staying aligned with the rep’s lens on the deal. This fragmentation makes it hard to prioritize work, see where each deal sits in the technical journey, and understand next best actions. fileciteturn0file0

**Functional Modules Affected**
- Opportunity Management
- TSX Homepage
  - TH360 Engagement
  - Opportunity Guided Journey View
  - TSX Journey Overview (At a glance)
  - Task Management
  - Notifications
- TSX Access
- TSX Integrations

**Design Considerations**
- TSX Homepage should be an opportunity‑first dashboard for SCs: list of active opportunities with tech state, key dates, POV vs Non‑POV flag, and forecast from sales.
- Provide identical opportunity data to what the rep sees (stage, amount, close date) plus TSX‑specific fields (Tech State, POV type, TRR status) to support the “two‑in‑a‑box” model.
- Make “opportunity → TSX project → artifacts / workflow” the primary navigation spine, with secondary pivots to account and territory views.
- Notifications panel should surface only high‑signal events (TRR approvals, POV environment ready, Express Testing completed, tech decision logged).

**Screenshot and Transcript References**
- TSX Modules overview – [Screenshot – 02:44]
- High‑level module walkthrough – [Transcript – 02:21–10:51]

**Detailed User Stories**
1. *As a Solution Consultant, I want my TSX homepage to show all opportunities I am assigned to, including sales stage, current technical state, and whether a Proof of Value is planned, so that I can prioritize which deals to work on each day.*
2. *As a Solution Consultant, I want an “Opportunity Guided Journey View” on each opportunity that combines sales data with technical journey status and upcoming milestones, so that I can quickly understand the context before engaging with the customer.*
3. *As a Solution Consultant Manager, I want to filter the opportunity list on the TSX homepage by product line, region, and technical state, so that I can see where my team is concentrated and where deals are stalling.*
4. *As a Solution Consultant, I want TSX notifications for material changes on my opportunities (new Technical Resource Request approval, POV environment activated, tech decision captured), so that I do not need to monitor multiple systems or inboxes.*

---

### 🔹 Objective #2: Make Technical Journey States Actionable and Gated

**Problem Statement**
The technical journey is clearly defined in a reference table (states 0–8 with entry/exit criteria and processes) but exists only as documentation. SCs manually interpret what state a deal is in, what must be done to exit that state, and which tools or artifacts apply. This creates inconsistency in how Proofs of Value are run and how “Tech Win / Tech Loss / No Tech Validation” are recorded.

**Functional Modules Affected**
- TSX Guided Journey (Workflow)
- TSX Homepage – TSX Journey Overview & Opportunity Guided Journey View
- POV Workflow & Non‑POV Validations
- Reports & Analytics

**Design Considerations**
- Represent the technical journey as a horizontal state bar on each opportunity (0–8) with clear labels and state descriptions.
- For each state, map the documented entry/exit criteria to system conditions and checklist items (e.g., “DOR created”, “Non‑POV options considered”, “Test plan approved”).
- Surface state‑specific actions and micro‑apps (e.g., Tech State 2 → Non‑POV catalog; Tech State 3 → POV test plan builder).
- Support soft gating: allow state advancement but with warnings when criteria are unmet; optionally enforce hard gates for critical checkpoints (e.g., moving to Tech Win without a DOR).

**Screenshot and Transcript References**
- Tech States Criteria table – [Screenshot – 12:26]
- Journey diagram with tech state band – [Screenshot – 28:26]
- Explanation of tech states and outcomes – [Transcript – 11:54–13:56]

**Detailed User Stories**
1. *As a Solution Consultant, I want to see the current technical state and the explicit entry and exit criteria directly on the opportunity, so that I know what work remains before I can progress to the next state.*
2. *As a Solution Consultant, I want TSX to show recommended actions for my current state (for example, “In Tech State 2, review Non‑POV options such as Express Testing or Reference Calls”), so that I can quickly choose the right motion for the customer.*
3. *As a Solution Consultant Manager, I want reporting on counts and value of opportunities in each technical state, segmented by Proof of Value type, so that I can spot where deals are getting stuck (e.g., many in Tech State 4 – POV Tech Validation).*
4. *As a Solution Consultant, I want TSX to warn me if I try to mark an opportunity as Tech Win without the required artifacts (Design of Record, test results, executive playback), so that we maintain a consistent standard of technical validation.*

---

### 🔹 Objective #3: TSX Project Workspace & Technical Resource Request Integration

**Problem Statement**
Domain Consultants are requested through Technical Resource Requests in Salesforce, and team membership is tracked manually. There is no single “TSX project” workspace that shows the full cross‑functional team (SC, rep, Domain Consultants, success architects, customer stakeholders), outstanding TRRs, and shared content for the opportunity. This makes resource planning and coordination brittle and opaque.

**Functional Modules Affected**
- Technical Resource Request (TRR)
- TSX Project Workspace (from journey diagram)
- Opportunity Management
- Task Management
- TSX Integrations (SFDC App Integration)

**Design Considerations**
- Create a TSX Project entity per opportunity, with a dedicated workspace tab aggregating team members, TRR requests, and project content.
- Embed TRR creation and status in the workspace: “Request Domain Consultant” → create SFDC TRR → show status and assignment.
- Show both Palo Alto and customer team members, with roles (Solution Consultant, Domain Consultant – SASE, Customer Security Architect, etc.).
- Provide timeline or kanban views to show when each resource is engaged during the journey.

**Screenshot and Transcript References**
- TSX Project Workspace and Tech Resource Request boxes – [Screenshots – 24:47, 28:26]
- Description of TRR and Domain Consultant role – [Transcript – 07:50–09:40, 21:17–23:00]

**Detailed User Stories**
1. *As a Solution Consultant, I want TSX to automatically spin up a TSX Project Workspace when a technical journey is initiated on an opportunity, so that I have a dedicated place to coordinate people and artifacts for that deal.* fileciteturn0file0
2. *As a Solution Consultant, I want to submit a Technical Resource Request for a Domain Consultant directly inside the project workspace and see its approval status and assigned person, so that I do not have to track requests in separate spreadsheets or emails.*
3. *As a Domain Consultant, I want to see a list of TSX projects where I am requested or assigned, including opportunity context and current technical state, so that I can manage my bandwidth across multiple Proofs of Value.*
4. *As a Solution Consultant Manager, I want a view of all active TSX projects and their open TRRs, so that I can identify staffing gaps and escalate where key opportunities lack the right experts.*

---

### 🔹 Objective #4: Non‑POV Services Catalog & Express Testing (Request Test Report) Workflow

**Problem Statement**
Non‑POV validation options (product demos, performance reports, Express Testing, reference calls, hands‑on workshops, BYOS sandboxes) exist but are scattered and not clearly tied to the technical journey. Express Testing in particular involves jumping between a Test Report Library and a Salesforce POC Request form, with unclear status visibility in TSX. This increases friction for “fast path” validations that are supposed to be low‑overhead.

**Functional Modules Affected**
- TSX Guided Journey – Non‑POV Validations
  - Product Demos
  - Performance Reports
  - Express Testing
  - Reference Calls
  - Hands‑On Workshop / Ultimate Test Drive
  - Build Your Own Sandbox (BYOS)
- Non‑POV Companion App
- Request Test Report (Express Testing) flow
- Artifact Repository (linking reports)
- TSX Integrations (SFDC POC Request, library sites)

**Design Considerations**
- Provide a Non‑POV Services Catalog panel within Tech State 2 that lists each service, expected effort, typical use cases, and SLAs.
- Embed the “Request Test Report” flow as a guided wizard:
  1) View Test Report Library;
  2) Decide to reuse vs request new;
  3) Shortcut into SFDC POC Request | Express Testing with pre‑filled opp/context;
  4) Track status;
  5) Attach resulting report as artifact.
- Where possible, open the Test Report Library and POC Request as modals or in-app frames; if security forces a jump‑out, make the return path explicit. (“Return to TSX Guided Journey.”)
- Persist Express Testing status on the opportunity and gating for exiting Tech State 2.

**Screenshot and Transcript References**
- Non‑POV Validations column – [Screenshot – 02:44]
- Non‑POV Companion App with BYOS, workshops, reports – [Screenshot – 28:26]
- Request Test Report (Express Testing) workflow – [Screenshot – 30:57]
- Discussion of Non‑POV validations and express testing – [Transcript – 13:56–18:00]

**Detailed User Stories**
1. *As a Solution Consultant in Tech State 2, I want a Non‑POV catalog that lists Express Testing, performance reports, reference calls, workshops, and BYOS options with guidance on when to use each, so that I can choose the lightest‑weight validation that still builds customer confidence.*
2. *As a Solution Consultant, I want to open the Test Report Library from the Tech State 2 panel, filter by product and industry, and reuse existing relevant reports, so that I avoid raising unnecessary new Express Testing requests.*
3. *As a Solution Consultant, I want a “Request Test Report” action that pre‑populates the Salesforce POC Request | Express Testing form with opportunity, customer, and product details, so that I do not have to retype data across systems.*
4. *As a Solution Consultant, I want TSX to show the current status of each Express Testing request (submitted, in progress, completed) and who owns it, so that I can answer customer questions without logging into multiple tools.*
5. *As a Solution Consultant, I want to link completed test reports from the library into the Artifacts panel for the opportunity, so that they become part of the permanent proof‑of‑value record.*

---

### 🔹 Objective #5: Proof of Value Companion App & Execution Workflow

**Problem Statement**
Full Proofs of Value are complex, multi‑week projects involving discovery questionnaires, Design of Record creation, environment setup, test planning, execution, result capture, and executive playback. Today, these are managed via spreadsheets and scattered documents (Sheets‑based DOR, Google Drive decks) with no single orchestrating experience. This makes it easy to miss steps, under‑document decisions, and lose continuity between deals.

**Functional Modules Affected**
- TSX Guided Journey – POV Workflow
  - Customer Environment POV
  - Managed POV (MPOV)
  - POV Proposal
  - POV Execution Workflow
  - POV Test Plan
  - POV Executive Playback
- POV Companion App (micro‑apps)
- TRR / TSX Project Workspace
- Templates & Document Storage
- POV Content & POV Executive Playback View
- Task Management

**Design Considerations**
- Treat each POV as a structured sub‑project under the TSX Project Workspace.
- Provide micro‑apps for DOR builder, test plan builder, proposal template, and executive playback deck, each with standard templates and AI drafting assistance.
- Represent POV phases and milestones visually (e.g., DOR → Planning → Execution → Playback → Decision) with completion status.
- Auto‑generate tasks for key steps and assign them to appropriate personas (SC, Domain Consultant, customer engineer).
- Capture outcome and reasoning at the end of the POV (why Tech Win, Tech Loss, or No Tech Validation) for analytics and future learning.

**Screenshot and Transcript References**
- POV Workflow column – [Screenshot – 02:44]
- POV Companion App section – [Screenshot – 28:26]
- Description of full POV vs Non‑POV flows – [Transcript – 12:06–13:56, 21:17–26:00]

**Detailed User Stories**
1. *As a Solution Consultant, I want a POV wizard that walks me from Design of Record creation through environment setup, test plan, proposal, and executive playback, so that I can run complex technical validations without missing critical steps.*
2. *As a Solution Consultant, I want reusable templates for DOR, test plans, and proposals that can be tailored to the customer’s environment and product mix, so that I maintain consistency while reducing preparation time.*
3. *As a Solution Consultant, I want each POV milestone to automatically create tasks with owners and due dates, so that the whole team (including Domain Consultants and customer engineers) understands what they must do and by when.*
4. *As a Solution Consultant Manager, I want visibility into all in‑flight POVs, including which phase they are in and how long they’ve been there, so that I can intervene when customer value validation is dragging on.*
5. *As a Solution Consultant, I want to record the final technical decision (win, loss, no validation) with structured reasons and link it to the POV artifacts, so that future teams can learn from what worked or failed in similar scenarios.*

---

### 🔹 Objective #6: Artifact Lifecycle & AI‑Powered Reuse

**Problem Statement**
Artifacts such as Design of Record, success plans, non‑POV outputs, test plans, proposals, and executive playback decks are core to how SCs sell. Today they live in Google Drive, Sheets, and assorted tools, with inconsistent naming and poor discoverability. Chris explicitly describes a future where a copilot can “give me what we did for [a prior account]” without building a full new content management system. fileciteturn0file0

**Functional Modules Affected**
- TSX Artifacts
  - Templates & Document Storage
  - Design of Record
  - Account Success Plans
  - Non‑POV Artifacts
  - POV Content (test plan, proposal)
  - POV Executive Playback View
- TSX Integrations (content data sharing, object association, UX/UI integration)
- AI Copilot / assistant panel

**Design Considerations**
- Treat artifacts as structured objects with metadata (account, opportunity, industry, product family, technical state, type).
- Maintain storage in existing systems (Google Drive, The Loop, etc.) but surface curated, contextual views in TSX via links and previews.
- Provide an AI copilot panel that can:
  - Search and summarize relevant artifacts from prior opportunities;
  - Generate draft artifacts (e.g., test plans) based on prior examples and opportunity context.
- Make it easy to attach existing artifacts to new opportunities, preserving lineage (e.g., “cloned from DOR for Customer X”).

**Screenshot and Transcript References**
- TSX Artifacts column – [Screenshot – 02:44]
- Artifact list (Design of Record, success plan, etc.) – [Screenshot – 30:22]
- Module prioritization for templates & document storage – [Screenshot – 29:38]
- Discussion of SC documentation mindset and desired copilot usage – [Transcript – 17:56–19:48, 29:07–30:42]

**Detailed User Stories**
1. *As a Solution Consultant, I want to search for past Designs of Record and success plans for similar industries and product combinations, so that I can reuse proven patterns rather than starting each Proof of Value from scratch.*
2. *As a Solution Consultant, I want to attach an existing artifact (for example, an Express Testing report or reference call summary) from Google Drive into the TSX Artifacts panel for a new opportunity, so that the proof‑of‑value record is complete without copying files.*
3. *As a Solution Consultant, I want an AI assistant in TSX that, given an opportunity, recommends relevant prior artifacts and can draft a new test plan or proposal based on them, so that I can move quickly while staying consistent with successful deals.*
4. *As a Solution Consultant Manager, I want to see whether key artifacts (Design of Record, test plan, executive playback) are present for each completed POV, so that I can enforce minimum documentation standards and identify training gaps.*

---

### 🔹 Objective #7: Embedded Task, Event, and Notification Management

**Problem Statement**
Technical selling is project‑like, involving many tasks (building test plans, scheduling workshops, following up on Express Testing) and events (demos, hands‑on workshops, webinars). Today, these are spread across Salesforce tasks, Google Calendar, and ad‑hoc tracking, with no consolidated view in TSX tied to the technical journey.

**Functional Modules Affected**
- Event Management
- Task Management
- Calendar / Event Management (module matrix)
- Notifications
- TSX Integrations (Google Suite and event apps)

**Design Considerations**
- For each opportunity, show a unified timeline view that merges tasks and calendar events related to the technical journey.
- Allow task creation directly from journey steps (e.g., starting a POV Test Plan automatically creates associated tasks).
- Integrate with Google Calendar and existing event tools as “existing systems”: show links and high‑level details without duplicating full scheduling functionality.
- Use notifications sparingly, prioritizing state‑changing events (workshop scheduled/completed, test period ending, tech decision due).

**Screenshot and Transcript References**
- Event Management & Task Management modules – [Screenshot – 02:44]
- Module prioritization (Calendar/Event Mgmt, Task Management) – [Screenshot – 29:38]
- Explanation of task and event responsibilities – [Transcript – 07:50–10:51]

**Detailed User Stories**
1. *As a Solution Consultant, I want to see all upcoming demos, workshops, and key POV milestones for an opportunity in a single TSX timeline, so that I can manage my time and prepare for customer touchpoints.*
2. *As a Solution Consultant, I want to create tasks from within the Guided Journey (for example, “Draft POV Executive Playback deck”) with the opportunity and technical state automatically attached, so that I do not lose context or forget to log the work.*
3. *As a Solution Consultant, I want TSX to surface calendar events related to the opportunity (workshops, executive readouts) by reading from my existing calendar, so that I do not need to re-enter them in another system.*
4. *As a Solution Consultant Manager, I want to filter tasks across my team by technical state and due date, so that I can see which deals risk missing critical POV milestones.*

---

### 🔹 Objective #8: Reports & Analytics Specific to Technical Sellers

**Problem Statement**
While many reports exist, there is no curated set focused on the metrics that matter for technical sellers (volume of Proofs of Value, tech win rate, cycle time per technical state, Non‑POV utilization, Domain Consultant load). Chris notes a need to first understand which reports SCs care about, then embed those into the workbench. fileciteturn0file0

**Functional Modules Affected**
- Reports & Analytics
  - SFDC Reports and Dashboards
  - Non‑SFDC Reports
- TSX Guided Journey
- TRR / POV / Non‑POV modules

**Design Considerations**
- Start with a small, opinionated analytics set tailored to SCs and their managers, not generic sales.
- Align metrics with tech states (e.g., Tech Win = State 7).
- Include both SFDC-native dashboards and links/embeds to external analytics (Tableau, GCP) as per the vendor fit matrix.
- Provide filters for territory, product line, industry, and SC to support operational reviews.

**Screenshot and Transcript References**
- Top‑level “Reports & Analytics” module – [Screenshot – 02:44]
- Module prioritization for Reports & Analytics – [Screenshot – 29:38]
- Comments about existing but unclear report usage – [Transcript – 5:00–6:03]

**Detailed User Stories**
1. *As a Solution Consultant, I want a dashboard showing my active opportunities by technical state, Proof of Value status, and expected technical decision date, so that I can focus on deals where my engagement will have the most impact this week.*
2. *As a Solution Consultant Manager, I want to see tech win rates and average cycle time by product family and POV type (full POV vs Non‑POV), so that I can identify which motions are most effective and where we need to improve enablement.*
3. *As a Solution Consultant Manager, I want to see Domain Consultant utilization tied to TRRs and POVs, so that I can balance load and justify headcount for high‑demand specialties.*
4. *As an Executive Sponsor, I want a high‑level view of revenue from opportunities where technical sellers drove a Tech Win, so that I can measure the business impact of TSX and related investments.*

---

### 🔹 Objective #9: Technical Seller Onboarding & Ongoing Enablement

**Problem Statement**
Technical Sales Onboarding is called out as a module and described as similar to Sales IQ: managers feed new SCs technical white papers and product documentation. Today this process is manual and fragmented across tools. There is no integrated onboarding journey or clear measurement of readiness.

**Functional Modules Affected**
- Sales Tech Onboarding
- TSX Homepage
- Templates & Document Storage (for playbooks)
- TSX Access (roles / permissions)

**Design Considerations**
- Create a structured onboarding journey for new SCs with milestones (core product training, shadowing, first POV participation, first lead POV).
- Embed contextual learning: surface playbooks and artifacts relevant to the type of opportunity the SC is working on.
- Provide manager views of onboarding progress and certification status.
- Reuse real TSX artifacts (successful DORs, test plans, playback decks) as learning examples.

**Screenshot and Transcript References**
- Sales Tech Onboarding module – [Screenshot – 02:44]
- Module prioritization for Tech Sales Onboarding – [Screenshot – 29:38]
- Explanation of onboarding using sales IQ‑like feeds – [Transcript – 4:54–5:40]

**Detailed User Stories**
1. *As a new Solution Consultant, I want an onboarding dashboard that shows required learning modules, recommended artifacts to review, and shadowing assignments, so that I know what I must complete before handling opportunities independently.*
2. *As a Solution Consultant Manager, I want to assign onboarding tracks by product specialization (for example, SASE or Cortex), so that each new hire builds the depth they need for their region and product focus.*
3. *As a new Solution Consultant, I want TSX to suggest relevant documentation and prior Proof of Value artifacts when I work on my first live deal, so that I can learn from real examples instead of only abstract training.*
4. *As a Solution Consultant Manager, I want to see which onboarding requirements are completed for each SC and which are outstanding, so that I can confidently assign them to high‑risk POVs.*

---

### 🔹 Objective #10: Persona Handshake & Shared Opportunity Context

**Problem Statement**
Solution Consultants and sales reps operate in a “two‑in‑a‑box” model and share the same opportunities, but their tools and journeys differ. Technical states (0–8) are separate from sales stages, and a different persona (Customer Success) takes over after Tech Win. Without explicit handshakes and shared views, there is risk of misalignment on deal status and lost context when transitioning to post‑sales.

**Functional Modules Affected**
- Opportunity Management
- TSX Homepage / Opportunity Guided Journey View
- TSX Guided Journey (technical states and outcomes)
- TSX Artifacts (handoff package)
- TSX Access

**Design Considerations**
- Provide a simplified technical state summary within the sales rep’s opportunity view and a simplified sales view within TSX, ensuring mutual visibility without overwhelming either persona.
- Define automatic actions when Tech Win or Tech Loss is recorded: update opportunity fields, trigger notifications, and create or update handoff artifacts (e.g., finalized DOR).
- For Tech Win, ensure that Customer Success can easily access the final Design of Record and key artifacts via links, without needing to learn TSX deeply.
- Respect permissions: reps and CS may have read‑only access to certain TSX items while SCs retain edit control.

**Screenshot and Transcript References**
- Journey diagram including Tech Closure / Post Sales Transition – [Screenshots – 24:47, 28:26]
- Explanation of rep / SC two‑in‑a‑box model and shared opportunity view – [Transcript – 2:23–4:00, 31:13–33:01]
- Description of Tech Win leading to booking and Customer Success involvement – [Transcript – 26:30–28:23]

**Detailed User Stories**
1. *As a Sales Representative, I want to see a concise summary of the technical journey (current state, key upcoming milestone, and risk flags) on my standard opportunity page, so that I can coordinate customer communication and forecasting with my Solution Consultant.*
2. *As a Solution Consultant, I want TSX to automatically update opportunity fields and notify the sales rep when I record a Tech Win or Tech Loss, so that we stay aligned on the deal outcome without separate manual updates.*
3. *As a Customer Success Manager, I want a simple way to access the final Design of Record, test results, and executive playback for a won opportunity, so that I understand what was promised and can plan implementation accordingly.*
4. *As a Solution Consultant Manager, I want to see which opportunities have completed technical validation but have not yet been properly handed off to Customer Success, so that I can drive clean transitions and avoid customer confusion.*

---

## ❓ Outstanding Gaps & Assumptions

**Unanswered Questions / Open Decisions**

- **Reports & Analytics:** Chris notes that many reports exist but doesn’t yet know which are most critical for SCs; specific metric definitions (e.g., how “Tech Win Rate” is calculated) are not clarified.
- **Express Testing Integration Details:** The Request Test Report slide raises questions (“Can IT modal the library site or is a jump out required?”, “Possible to link POC Request data view in TSX?”) without answers.
- **Exact TRR Workflow:** We know TRRs exist in Salesforce and that TSX should integrate, but approval rules, SLAs, and edge cases (partial approvals, substitutions) are not described.
- **Non‑POV Service Definitions:** The precise entry conditions, owners, and SLAs for each Non‑POV service (workshops, BYOS, reference calls) are not fully documented.
- **Artifact Taxonomy:** We know key artifact types but lack a canonical taxonomy and metadata model (e.g., required vs optional fields, naming conventions).
- **Onboarding Scope:** The Sales Tech Onboarding module mentions feeding documentation but not assessment, certification, or integration with existing learning systems.
- **Permissions Model:** Which personas (SC, SC manager, sales rep, Domain Consultant, Customer Success) can view or edit each module is not defined.

**Design‑Critical Data Missing**

- Volume and distribution of opportunities by technical state, to prioritize where TSX must reduce friction first.
- Current pain points in the existing TRR and POV processes (e.g., common delays, typical cycle times).
- Detailed schema of current Salesforce objects (opportunity, TRR, POC Request) and existing custom fields used by technical sellers.
- Exact inventory and structure of existing artifact repositories (Google Drive folder structures, The Loop categories).
- User research on how SCs navigate their day today (tabs open, tools used, biggest time sinks).
- Any security or compliance constraints around embedding external systems (test report library, Google Drive) inside TSX frames.

**Assumptions to Validate**

1. **Salesforce‑Centric Implementation:** TSX is assumed to be primarily implemented on Salesforce, with TSX views layered on top of existing opp/account objects.
2. **Google Workspace as Source of Truth for Documents:** We assume GDrive / The Loop remain the primary storage for templates and artifacts, and TSX mainly organizes and links rather than fully storing files.
3. **Two‑in‑a‑Box Ownership:** We assume every opportunity has a paired rep and Solution Consultant, and that SC compensation is materially tied to Tech Wins, making technical state accuracy critical.
4. **Domain Consultants as Scarce Shared Resources:** We assume Domain Consultants are shared across many deals and product lines, so TRR efficiency and visibility are high‑value features.
5. **Non‑POV Motions as Lower‑Cost Alternatives to POV:** We assume Non‑POV validations should be encouraged where appropriate to reduce cost and time, making their discoverability and ease‑of‑use important.
6. **AI Copilot Has Access to Artifacts:** We assume the copilot can safely index and reason over artifacts stored in Google Drive / other systems, with appropriate permissions.
7. **SC Persona Is Willing to Work Primarily from TSX:** We assume that if TSX provides sufficient value (journey view, artifacts, tasks), SCs will adopt it as their primary workbench rather than remaining in ad‑hoc tools.

Before moving forward with detailed design, these gaps and assumptions should be validated with additional stakeholder interviews (SCs, SC managers, Domain Consultants, sales reps, Customer Success) and a review of existing systems and data.
