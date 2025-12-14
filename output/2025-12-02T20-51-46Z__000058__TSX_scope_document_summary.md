# TSX scope document summary

## You (2025-12-02T20:51:46.185000+00:00)

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



## ChatGPT (2025-12-02T20:52:21.441903+00:00)

from PIL import Image, ImageOps, ImageFilter, ImageEnhance, ImageStat, ImageChops, ImageFont
import matplotlib.pyplot as plt

paths = [
    "/mnt/data/Screenshot 2025-12-02 at 12.25.16 PM.png",
    "/mnt/data/Screenshot 2025-12-02 at 12.25.44 PM.png",
    "/mnt/data/Screenshot 2025-12-02 at 12.26.42 PM.png",
    "/mnt/data/Screenshot 2025-12-02 at 12.27.16 PM.png",
    "/mnt/data/Screenshot 2025-12-02 at 12.27.30 PM.png",
    "/mnt/data/Screenshot 2025-12-02 at 12.27.42 PM.png",
]
imgs = [Image.open(p) for p in paths]



## ChatGPT (2025-12-02T20:52:36.603249+00:00)

plt.imshow(imgs[0]); plt.axis('off')



## ChatGPT (2025-12-02T20:52:49.803645+00:00)

plt.figure(figsize=(8,5))
plt.imshow(imgs[0].crop((0,200,2500,1400))); plt.axis('off')



## ChatGPT (2025-12-02T20:53:04.325196+00:00)

plt.figure(figsize=(5,6))
plt.imshow(imgs[0].crop((150,250,900,1400))); plt.axis('off')



## ChatGPT (2025-12-02T20:53:26.384813+00:00)

plt.figure(figsize=(5,6))
plt.imshow(imgs[0].crop((900,250,1700,1400))); plt.axis('off')



## ChatGPT (2025-12-02T20:53:47.859454+00:00)

plt.figure(figsize=(5,6))
plt.imshow(imgs[0].crop((1650,250,2470,1400))); plt.axis('off')



## ChatGPT (2025-12-02T20:54:17.721312+00:00)

plt.imshow(imgs[1]); plt.axis('off')

## ChatGPT (2025-12-02T20:54:44.249612+00:00)

plt.figure(figsize=(8,6))
plt.imshow(imgs[1].crop((0,150,2500,1350))); plt.axis('off')



## ChatGPT (2025-12-02T20:55:04.045563+00:00)

plt.imshow(imgs[2]); plt.axis('off')

## ChatGPT (2025-12-02T20:55:21.045025+00:00)

plt.figure(figsize=(8,5))
plt.imshow(imgs[2].crop((0,150,2500,1350))); plt.axis('off')



## ChatGPT (2025-12-02T20:55:45.329875+00:00)

plt.imshow(imgs[3]); plt.axis('off')

## ChatGPT (2025-12-02T20:56:03.731173+00:00)

plt.figure(figsize=(8,5))
plt.imshow(imgs[3].crop((450,150,2450,1350))); plt.axis('off')



## ChatGPT (2025-12-02T20:56:26.046933+00:00)

plt.imshow(imgs[4]); plt.axis('off')

## ChatGPT (2025-12-02T20:56:42.137662+00:00)

plt.figure(figsize=(8,5))
plt.imshow(imgs[4].crop((0,150,2500,1350))); plt.axis('off')



## ChatGPT (2025-12-02T20:57:10.788275+00:00)

plt.imshow(imgs[5]); plt.axis('off')

## ChatGPT (2025-12-02T20:57:28.569698+00:00)

plt.figure(figsize=(8,6))
plt.imshow(imgs[5].crop((0,120,2500,1350))); plt.axis('off')





## ChatGPT (2025-12-02T21:00:13.818258+00:00)

### TSX Scope Document — Technical Seller Experience (Solution Consultant Workbench)

Persona in focus: **Solution Consultant / Technical Seller (SC)** working side-by-side with an account executive on opportunities, responsible for **technical validation, proof of value (POV), and technical win**. fileciteturn0file0

---

## 🔹 Objective #1: Make the Technical Journey Visible and Actionable on Every Opportunity

**Problem Statement**
The current **technical journey (states 0–8)** exists as a process chart and spreadsheet-style definition, but not as a **living, at-a-glance experience**. SCs must mentally map where an opportunity is (Tech Discovery, POV Planning, Non-POV Tech Validation, etc.), what the **entry/exit criteria** are, and which activities or artifacts are still missing. This creates ambiguity about **“where we are, what’s done, and what unlocks the next state”** for each deal.

**Functional Modules Affected**

- TSX Homepage
- Opportunity Management
- TSX Guided Journey (Workflow)
- TSX Journey Overview (At a glance)
- Task Management
- Notifications
- Reports & Analytics (SFDC Reports and Dashboards, Non-SFDC Reports)

**Design Considerations**

- Represent the **Technical Journey states (0–8)** as a **horizontal journey bar** on each opportunity, with clear labels (e.g., “1 – Tech Discovery”, “3 – POV Planning”, “5 – Tech Decision Pending”).
- For each state, surface:
  - **Entry criteria** and **exit criteria** as concise checklists.
  - **Required key processes** (e.g., “Build Design of Record”, “Execute POV Test Plan”).
  - **Required / recommended artifacts** (e.g., Design of Record, Test Plan, Executive Playback deck).
- Show **state readiness** (e.g., “3 of 5 criteria met”) and **blocking items**.
- TSX Journey Overview should provide:
  - A **portfolio view** of all opportunities by technical state.
  - Filters by region, product, SC, and time horizon.
- Integrate with **Tasks** and **Notifications** so that missing criteria automatically generate tasks or prompts.
- Maintain a **single shared view with the sales rep** for the opportunity state and forecast, while keeping the **technical journey lens** specific to the SC.

**Screenshot & Transcript References**

- [Screenshot – 02:44] “TSX Modules” showing **TSX Guided Journey**, TSX Homepage, TSX Journey Overview, Task Management, Notifications.
- [Screenshot – 12:26] “Technical Journey | Tech States Criteria, Processes, and Outputs” table (states 0–8, entry/exit criteria, key processes, tools & artifacts, outputs).
- [Transcript – 11:54–13:56] Explanation of technical journey states and how deals progress to Tech Win/Loss, and Non-POV vs POV paths. fileciteturn0file0

**Detailed User Stories**

1. *As a Solution Consultant, I want to see the current **technical state** of each opportunity (for example, “3 – POV Planning”) directly on the TSX opportunity view, so that I can quickly understand how far the deal has progressed in the technical journey.*

2. *As a Solution Consultant, I want each **technical state** to show its **entry and exit criteria** as a checklist, so that I know exactly which activities and artifacts must be completed before advancing the opportunity.*

3. *As a Solution Consultant, I want TSX to **automatically suggest the next state** once all exit criteria are met, so that I can move the opportunity forward with confidence and avoid premature state changes.*

4. *As a Solution Consultant, I want to see a **portfolio view of all my opportunities grouped by technical state** in TSX Journey Overview, so that I can prioritize my time on deals that are stuck or nearing a decision.*

5. *As a Sales Representative, I want to see a **read-only view of the technical journey state and key milestones** on the same opportunity page I use for forecasting, so that I can align my forecast with the technical reality of the deal.*

6. *As a Technical Seller Manager, I want **reports and dashboards** that show conversion rates between states (for example, from Tech Discovery to POV Planning), so that I can identify where deals typically stall and coach my team on those stages.*

---

## 🔹 Objective #2: Create a Canonical TSX Project Workspace and Team Composition Hub

**Problem Statement**
Today, assembling the **project team** and managing the **TSX project workspace** is fragmented. SCs manually add Domain Consultants (DCs) through separate **Technical Resource Requests (TRR)** in Salesforce.com (SFDC), track participants in spreadsheets, and scatter documents across “one-off drives and docs”. This creates confusion about **who is on the technical project team, who owns which tasks, and where to find shared content**.

**Functional Modules Affected**

- TSX Project Workspace (from Lucidchart flow)
- Technical Resource Request (TRR)
- Opportunity Management
- Event Management (for workshops, demos)
- Task Management
- TSX Access (roles, permissions)

**Design Considerations**

- Introduce a **TSX Project Workspace** object tied to an Opportunity:
  - Shows **internal team members** (SC, Domain Consultant, Success Architect, etc.) and **customer technical contacts**.
  - Lists **open tasks** and **upcoming events** (workshops, reference calls, demos).
- Integrate **Technical Resource Request (TRR)** into the workspace:
  - Ability to request a **Domain Consultant (DC)** from the appropriate domain (for example, Secure Access Service Edge, Cortex, Cloud) and see request status.
- Provide **role tagging** (SC, DC, customer architect, security lead) and default notification behaviors based on roles.
- Auto-create a **TSX content folder structure** in the existing document system (for example, Google Drive / TheLoop) when a new TSX Project is created.
- Support **“Today / Future Enhancements”** view per box for transparency about what is automated now vs planned.

**Screenshot & Transcript References**

- [Screenshot – 24:47] TSX Project Workspace boxes: “Add Team Members”, “Create TSX Content Folder”, “Request DC and Add to Project Team”, with “Today” and “Future Enhancements” notes.
- [Screenshot – 28:26] Extended flow showing “Add Resources to TSX Team” and integrations.
- [Transcript – 7:52–9:55] Description of task management, project-like nature of each deal, and need to coordinate multiple personas including Domain Consultants. fileciteturn0file0

**Detailed User Stories**

1. *As a Solution Consultant, I want TSX to **create a TSX Project Workspace automatically** when a technical validation is needed for an opportunity, so that I have a single place to manage the technical aspects of the deal.*

2. *As a Solution Consultant, I want to **add team members (internal and customer) with clear roles** to the TSX Project Workspace, so that everyone knows who is involved and what they are responsible for.*

3. *As a Solution Consultant, I want to **submit a Technical Resource Request (TRR) from within the TSX Project Workspace** to add a Domain Consultant, so that I do not have to switch to a separate Salesforce.com page.*

4. *As a Solution Consultant, I want to see the **status of each Technical Resource Request** (for example, “requested”, “assigned”, “declined”) in the same workspace, so that I can plan workshops and test activities with confidence.*

5. *As a Domain Consultant, I want to receive a **clear invitation with opportunity context and expected contribution** when I am added via TSX, so that I can prepare appropriately for my part in the proof of value.*

6. *As a Technical Seller Manager, I want to see a **summary of active TSX projects per SC and per Domain Consultant**, so that I can balance workload and avoid overcommitting specialist resources.*

---

## 🔹 Objective #3: Unify Non-POV Services and Express Testing into a Seamless Request & Tracking Flow

**Problem Statement**
Non-POV validations (such as **Product Demos, Performance Reports, Express Testing, Reference Calls, Hands-On Workshops, Building Your Own Sandbox**) live across **separate companion apps** and **Salesforce.com Proof of Concept (POC) Request** flows. SCs must jump between TSX, SFDC POC Request, and test-report libraries, making it hard to **request, track, and attach results** back to the TSX guided journey.

**Functional Modules Affected**

- Non-POV Validations (Product Demos, Performance Reports, Express Testing, Reference Calls, Hands-On Workshop / Ultimate Test Drive, Building Your Own Sandbox)
- Non-POV Companion App
- Request Test Report / Express Testing workflow
- SFDC POC Request | Express Testing
- TSX Guided Journey (Tech State 2 and beyond)
- TSX Artifacts (for adding test reports)

**Design Considerations**

- Provide a **Non-POV Service Catalog** inside TSX where SCs can:
  - See available services, **eligibility**, and typical timelines.
  - Trigger requests in a **consistent way**, regardless of whether fulfillment happens in SFDC or another app.
- For **Express Testing / Request Test Report**:
  - Allow SCs in **Tech State 2** to:
    - Browse **Test Report Library** from within TSX (modal over TSX if possible; avoid full context switch).
    - Request new test reports via a **unified request form** that writes into SFDC POC Request where needed.
  - Show **status and owner** of each request in TSX (using SFDC status as the system of record).
- Ensure that **completed test reports** can be linked as **TSX artifacts** and appear in the relevant technical state checklist.
- Support **auditability**: who requested which report, when, and for which customer use case.

**Screenshot & Transcript References**

- [Screenshot – 02:44] Non-POV Validations section in TSX Modules: “Product Demos”, “Performance Reports”, “Express Testing”, “Reference Calls”, “Hands on Workshop / Ultimate Test Drive”, “Building Your Own Sandbox (BYOS)”.
- [Screenshot – 30:57] “Workflow | Request Test Report (aka Express Testing) (Non-POV)” steps outlining navigation via Tech State 2, Test Report Library, SFDC POC Request, and artifact linking.
- [Screenshot – 24:47 / 28:26] Non-POV Companion App box listing BYOS Sandboxes, Performance Reports, Hands-On Workshops, Reference Calls, Industry Reports.
- [Transcript – 13:56–18:40] Explanation of Non-POV vs POV paths, express testing, performance reports, reference calls, hands-on workshops, and BYOS sandboxes. fileciteturn0file0

**Detailed User Stories**

1. *As a Solution Consultant, I want a **Non-POV Service Catalog view in TSX** that lists all available validation options (for example, Express Testing, Performance Reports, Reference Calls), so that I can quickly choose the right low-cost validation path for each customer.*

2. *As a Solution Consultant, I want to **open the Test Report Library in a modal within TSX** while staying in Tech State 2, so that I can review existing reports without losing my place in the guided journey.*

3. *As a Solution Consultant, I want to **request a new test report from Tech State 2** and have TSX automatically create or update the corresponding Salesforce.com POC Request, so that I do not have to manage duplicate entries.*

4. *As a Solution Consultant, I want TSX to **display the status of each test report request** (for example, “in progress”, “completed”) using Salesforce.com data, so that I can update customers without manually checking multiple systems.*

5. *As a Solution Consultant, I want to **add completed test reports as artifacts** in the TSX Guided Journey and have them count toward the exit criteria of the relevant technical state, so that documentation and process stay aligned.*

6. *As a Technical Seller Manager, I want to see **analytics on Non-POV service usage** (for example, how often Express Testing vs demos vs reference calls are used and their impact on tech wins), so that I can refine our recommended validation patterns.*

---

## 🔹 Objective #4: Systematize POV Workflow and Artifact Creation Across the Journey

**Problem Statement**
The **POV workflow**—covering POV proposal, test plan, execution workflow, and executive playback—is well described in decks and spreadsheets but is currently executed through **manual documents in Google Drive and other tools**. SCs are “into documentation” and create rich artifacts (Design of Record, Success Plan, Test Plan, Proposal, Executive Playback), but there is **no structured, guided workspace** in TSX to orchestrate these artifacts as part of the journey.

**Functional Modules Affected**

- POV Workflow (Customer Environment POV, Managed POV)
- POV Proposal
- POV Test Plan
- POV Execution Workflow
- POV Executive Playback
- TSX Artifacts (Design of Record, Account Success Plans, Non-POV Artifacts, POV Content, POV Executive Playback View)
- Templates & Document Storage
- POV Companion App (POV Huddle, POV Test Plan App, POV Proposal App, POV Request, POV Playback App)

**Design Considerations**

- Treat **POV as a structured project**:
  - POV Setup → POV Design (Design of Record + Success Plan) → Execution → Executive Playback → Outcome (Tech Decision Pending → Tech Win / Tech Loss).
- Provide **guided POV workspaces**:
  - Pre-configured **templates** for Design of Record, Test Plan, Proposal deck, and Executive Playback.
  - **Checklists** linked to each artifact:
    - For example, Test Plan requires specific scenarios, metrics, and success criteria.
- Integrate with existing **document systems**:
  - Templates stored in **Templates & Document Storage** (Google Drive / TheLoop).
  - TSX links to documents, not necessarily storing them.
- POV Companion Apps (Huddle, Test Plan, Proposal, Playback) can be conceptualized as **micro-apps or panels** within TSX, sharing a common opportunity and technical state context.
- Explicitly align **POV state transitions** with artifacts:
  - Cannot move from “4 – POV Tech Validation” to “5 – Tech Decision Pending” until **execution test results** and a summary are attached.
- Allow **reuse of prior POV assets** (see Objective #5).

**Screenshot & Transcript References**

- [Screenshot – 02:44] TSX Modules showing **POV Workflow** stages and TSX Artifacts.
- [Screenshot – 28:26] POV Companion App column listing POV Huddle, POV Test Plan App, POV Proposal App, POV Request, POV Playback App, and future AI/POV Bot Recommendations.
- [Transcript – 12:06–20:22] Explanation of proof of value, POV planning, tech win vs tech loss, and definition of artifacts such as Design of Record, Success Plan, Test Plan, Proposal, Executive Playback. fileciteturn0file0

**Detailed User Stories**

1. *As a Solution Consultant, I want TSX to **offer a POV workspace linked to the opportunity** that shows all POV-related steps and artifacts in one place, so that I can manage the proof of value as a structured project.*

2. *As a Solution Consultant, I want **standardized templates for Design of Record, Test Plan, Proposal, and Executive Playback** accessible from TSX, so that I can produce consistent, high-quality artifacts without recreating structure each time.*

3. *As a Solution Consultant, I want TSX to **track completion status of each POV artifact** (for example, Design of Record “draft”, Test Plan “approved”, Executive Playback “delivered”), so that I know what is remaining before a tech decision.*

4. *As a Solution Consultant, I want **POV Huddle notes and decisions** to be captured in TSX and linked to the Test Plan and Proposal, so that the team’s internal alignment is preserved as part of the POV record.*

5. *As a Technical Seller Manager, I want to **review a concise POV summary** (including artifacts and test outcomes) directly from TSX, so that I can support escalations and validate whether a technical win is justified.*

6. *As a Sales Representative, I want a **high-level POV status indicator** (for example, “in design”, “in testing”, “executive playback scheduled”), so that I can manage stakeholder expectations and forecast timing accurately.*

---

## 🔹 Objective #5: Enable Intelligent Artifact Discovery and Reuse via TSX and AI Assistant

**Problem Statement**
Artifacts (Design of Record, Success Plan, Test Plan, Proposals, Executive Playback decks, non-POV outputs) are currently stored in various **Google Drive folders and TheLoop**, with limited structure. SCs must remember **which past accounts** had similar solutions and **manually hunt** for relevant artifacts. This makes it hard to reuse good work, maintain consistency, and quickly tailor content to new opportunities.

**Functional Modules Affected**

- TSX Artifacts (Templates & Document Storage, Design of Record, Account Success Plans, Non-POV Artifacts, POV Content, POV Executive Playback View)
- TSX Access (permissions)
- Knowledge Management (Build)
- AI / Copilot panel on the right-hand side (proposed)

**Design Considerations**

- Provide an **Artifact Library panel** within each opportunity where:
  - TSX lists **all artifacts linked to this opportunity**.
  - The AI assistant can **suggest additional relevant artifacts** from **similar opportunities** (same segment, product mix, technical state).
- Index artifacts stored in existing systems (Google Drive, TheLoop) via metadata:
  - Opportunity ID, technical state, product family, customer segment, region, SC owner.
- Allow SCs to issue **natural-language queries** to the AI assistant:
  - “Show me Design of Record and Success Plan for similar Secure Access Service Edge deals in the last 12 months.”
- When SCs create new artifacts, TSX should:
  - Encourage them to **add key metadata** (products, use cases, industry, complexity).
  - Offer **“start from prior example”** suggestions.
- Respect permissions:
  - Only suggest artifacts the user is allowed to view.
- Avoid duplicating files; always **link back to the system of record**.

**Screenshot & Transcript References**

- [Screenshot – 02:44] TSX Artifacts section and “Templates & Document Storage”.
- [Transcript – 17:36–20:22] Discussion about artifacts as knowledge base, repository, and AI assistant usage (“give me what we did for so-and-so account… tell me what relevant documents I can leverage for this account”). fileciteturn0file0

**Detailed User Stories**

1. *As a Solution Consultant, I want TSX to **show all artifacts related to the current opportunity** (Design of Record, Success Plan, Test Plan, Proposal, Executive Playback) in a single panel, so that I do not need to search multiple drives and folders.*

2. *As a Solution Consultant, I want an AI assistant in TSX where I can ask, **“Show me all prior Design of Record and Success Plan documents for similar accounts”**, so that I can reuse proven patterns instead of starting from scratch.*

3. *As a Solution Consultant, I want TSX to **suggest prior POV test plans and proposals** when I start a new POV for a similar product and segment, so that I can accelerate document creation while maintaining consistency.*

4. *As a Solution Consultant, I want to **tag artifacts with products, use cases, and industry** when I upload or link them, so that future searches and AI recommendations can be more accurate.*

5. *As a Technical Seller Manager, I want to see **usage metrics for artifacts** (for example, which templates and prior POVs are reused most often), so that I can invest in improving the highest-impact collateral.*

---

## 🔹 Objective #6: Clarify the SC–Sales Rep Handshake Around Opportunity and Tech Win

**Problem Statement**
SCs and Sales Reps are “two in a box” on each deal, sharing the same opportunity but using different lenses. The **hand-off from sales to technical seller** (“you go do the POV”) and the **return from tech win to commercial close** are conceptually clear but **not explicitly modeled in TSX UI**. This can lead to misalignment between **technical win status, forecast, and compensation**.

**Functional Modules Affected**

- Opportunity Management
- TSX Access (shared visibility)
- Reports & Analytics (forecast, tech win metrics)
- TSX Guided Journey (Tech Win / Tech Loss states)

**Design Considerations**

- Make the **hand-off points explicit**:
  - When an opportunity moves from sales stage to requiring technical validation, TSX should **prompt the rep and SC** to create a TSX Project and pick Non-POV vs POV path.
- Show **Tech Win / Tech Loss / No Tech Validation** clearly:
  - At the end of the journey, TSX should record the **technical outcome** separately from commercial close.
- Integrate with **forecasting**:
  - When a technical win is recorded, surface this in **Salesforce.com forecast views** so reps and managers can adjust probabilities.
- Ensure **symmetry of views**:
  - SC and Sales Rep see the same high-level status but with **role-appropriate detail** (SC gets deeper technical state data; Rep sees aggregated indicators).
- Maintain a clear link between **technical decision pending (state 5)** and **customer decision & verbal confirmation** captured by sales.

**Screenshot & Transcript References**

- [Screenshot – 12:26] Technical Journey table, especially states 5–8 (“Tech Decision Pending”, “Tech Loss – Closed”, “Tech Win – Closed”, “No Tech Validation – Closed”).
- [Transcript – 20:55–33:01] Discussion of overlap between SC workbench and sales workbench, shared access to opportunities and forecast, and compensation based on tech wins. fileciteturn0file0

**Detailed User Stories**

1. *As a Sales Representative, I want TSX to **prompt me to involve a Solution Consultant** when an opportunity meets technical validation criteria, so that I do not forget to bring in technical expertise.*

2. *As a Solution Consultant, I want to **accept or acknowledge ownership of the technical journey** for a given opportunity, so that it is clear who is responsible for driving the technical validation.*

3. *As a Solution Consultant, I want the **technical outcome (Tech Win, Tech Loss, No Tech Validation)** to be recorded in TSX and synced back to the opportunity, so that my performance and compensation reflect actual technical results.*

4. *As a Sales Representative, I want to see **whether the technical decision is pending, positive, or negative** directly from my Salesforce.com opportunity view, so that my forecast accurately reflects the technical reality.*

5. *As a Sales Manager, I want dashboards that **correlate technical wins with closed-won deals**, so that I can understand how TSX and technical sellers influence revenue.*

---

## 🔹 Objective #7: Embed Technical Seller Onboarding and Continuous Enablement into TSX

**Problem Statement**
Technical onboarding for SCs is currently **high effort**, drawing on SalesIQ-style feeds of white papers and documentation. There is not yet a **TSX-specific path** that ties onboarding content to **real TSX modules and workflows**, nor an easy way for technical seller managers to track **readiness**.

**Functional Modules Affected**

- Sales Tech Onboarding
- TH360 Engagement
- Knowledge Management
- Reports & Analytics (for readiness metrics)

**Design Considerations**

- Provide a **Sales Tech Onboarding module** inside TSX that:
  - Maps learning content directly to **TSX modules and journey states** (for example, “Learn POV workflow”, “Practice Non-POV Service Catalog usage”).
  - Includes **hands-on exercises** linked to demo opportunities or sandboxes.
- Allow managers to track **onboarding progress**:
  - Which modules completed, quiz scores, simulated POV projects.
- Integrate with **TH360 Engagement**:
  - Use **TH360 Engagement cards** to guide SCs to relevant content and practice tasks.
- Over time, use **“knowledge gaps”** seen in real opportunities (for example, recurring errors in POV artifacts) to refine onboarding tasks.

**Screenshot & Transcript References**

- [Screenshot – 02:44] TSX Modules row showing **Sales Tech Onboarding** and **TH360 Engagement**.
- [Screenshot – 29:38] Prioritization table where **Tech Sales Onboarding** appears with Business Priority 2 and recommendation “Build” due to high effort on onboarding processes.
- [Transcript – 4:54–6:10] Description of Sales Tech Onboarding and technical enablement similar to SalesIQ. fileciteturn0file0

**Detailed User Stories**

1. *As a new Solution Consultant, I want a **guided onboarding path in TSX** that walks me through core workflows (technical journey, Non-POV catalog, POV artifacts, TSX Project Workspace), so that I can become productive quickly.*

2. *As a Technical Seller Manager, I want to **see onboarding completion and readiness metrics** for new SCs, so that I know when they are ready to own opportunities independently.*

3. *As a Solution Consultant, I want to **practice building a mock Design of Record and Test Plan** in a safe sandbox with feedback, so that I can learn expectations before working on live customer deals.*

4. *As a Solution Consultant, I want TSX to **surface targeted learning content** (for example, “short video on Express Testing”) when I first use a module, so that I can learn in context instead of reading long generic documentation.*

---

## ❓ Outstanding Gaps & Assumptions

This section lists **questions, missing data, and inferred assumptions** that should be validated before finalizing design.

### Unanswered Questions

1. **Key Reports & Analytics for SCs**
   - Which specific **Salesforce.com and non-Salesforce.com reports** do SCs rely on most (for example, pipeline by technical state, POV duration, Non-POV service utilization)?
   - Are there **canonical dashboards** today that we must mirror or improve inside TSX?

2. **Non-Salesforce Tools in Use**
   - Which **external tools** (beyond Google Drive and TheLoop) are most critical to the technical seller workflow (for example, Lucidchart, Confluence, internal test systems)?
   - What are the **integration constraints** (security, APIs) for each?

3. **Technical Resource Request Process**
   - What is the **current Service-Level Agreement (SLA)** for Domain Consultant assignment?
   - Who **approves** Technical Resource Requests, and what criteria do they use (deal size, product complexity, region)?

4. **Artifact Governance**
   - Is there an existing **taxonomy or naming convention** for artifacts (Design of Record, Success Plan, Test Plan, etc.) that TSX must enforce?
   - Who is responsible for **curating templates** and ensuring they stay up-to-date?

5. **POV vs Non-POV Decision Rules**
   - Are there explicit **rules of thumb** (deal size, segment, product) that determine when to run a full **proof of value** versus **Non-POV validations** like Express Testing and demos?
   - Should TSX **recommend a path** (Non-POV vs POV) based on these rules, or simply document the choice?

6. **Permissions and Data Sharing**
   - How should access rights differ between **Solution Consultants, Sales Representatives, Domain Consultants, and Customer Success** for TSX modules and artifacts?
   - Are there **regulatory or data-classification constraints** around storing customer network diagrams, logs, or security reports in shared repositories?

7. **AI / Copilot Scope**
   - What is the intended **scope of the AI assistant**: only **content retrieval**, or also **drafting artifacts** (for example, first-pass Design of Record, Test Plan, Proposal) using existing data?
   - What **guardrails** are required to avoid exposing sensitive customer data via AI suggestions?

### Design-Critical Assumptions to Validate

1. **TSX will not replace Salesforce.com as system of record** for opportunities; it will **orchestrate** the technical journey on top of Salesforce.com data.
2. **Google Drive and TheLoop remain primary storage systems** for documents; TSX will link to files rather than store them natively.
3. **Customer Success and post-sales workflows** are **out of scope** for this phase, except for the hand-off artifact (for example, sharing Design of Record with Customer Success).
4. **Technical Journey states 0–8** are accepted and will not significantly change; TSX design will therefore treat them as a stable backbone.
5. **SC and Sales Rep always operate as a pair** (“two in a box”) on opportunities; TSX can assume this relationship when modeling access and workflow.

Validating these questions and assumptions with stakeholders (Solution Consultants, Domain Consultants, Sales Leadership, Product Owners, and IT / Integration teams) will be essential before moving from **scope definition** into **detailed interaction design and build planning**.





## You (2025-12-02T21:18:13.559000+00:00)

Find a way to document everything except the Outstanding Gaps and Asusmptions into a single large spreadsheet that captures

- Objective
- Functional Modules Affected
- Design Considerations
- Detailed User Stories

Into one single sheet. Specifically for the user stories, break the sentences into columns labeled 'As a Technical Seller, I want to...' and 'so that I...'. Change all 'Solution Consultant' to 'Technical Seller'

Use the google sheet tab labeled 'User Stories for TSX' for your documentation









































































## ChatGPT (2025-12-02T21:23:41.727479+00:00)

All the objectives, modules, design considerations, and user stories have been documented in the Google Sheet under the tab **“User Stories for TSX”**.  Each user story has been split into two separate columns as requested, with **“As a Technical Seller, I want to…”** holding the first part of the user story (actor and intent) and **“so that I…”** holding the purpose.  I also replaced “Solution Consultant” with “Technical Seller” throughout. The sheet now comprehensively captures the scope document’s content in a structured format【160500081801842†screenshot】.

## You (2025-12-02T21:28:45.394000+00:00)

Now do the same on the new sheet labeled User Stores V2.

Find a way to document everything except the Outstanding Gaps and Asusmptions into a single large spreadsheet that captures - Objective - Functional Modules Affected - Design Considerations - Detailed User Stories Into one single sheet. Specifically for the user stories, break the sentences into columns labeled 'As a Technical Seller, I want to...' and 'so that I...'.

But this time use the following content:

---------------

🔹 Objective #1: Make “The Technical Journey” Concrete and Navigable

Problem Statement
The technical journey is well-defined conceptually (states 0–8 with entry/exit criteria) but not yet visibly embodied in TSX. Terms like engagement, journey, project are used interchangeably, and it is unclear how a Technical Seller sees “where I am” and “what is next” in a given opportunity.

Functional Modules Affected
	•	TSX Homepage (TSX Journey Overview, Opportunity Guided Journey View)
	•	TSX Guided Journey (Workflow – POV and Non-POV)
	•	Tech States framework (0–8)
	•	Opportunity Management

Design Considerations
	•	The journey must behave like a state machine with memory, not just a checklist.
	•	Naming and IA should reconcile “TSX Project,” “Engagement,” and “Journey” into a coherent mental model.
	•	Each state should clearly surface:
	•	Current state, next eligible states
	•	Required activities/artifacts to progress
	•	Risks if the state is stalled
	•	Must align with the shared Opportunity object so that rep and Technical Seller see consistent status.

Screenshot & Transcript References
	•	[Screenshot – 12:26] (Tech States Criteria, Processes, and Outputs)
	•	[Transcript – ~11:54–13:56] – explanation of states 0–8, POV vs Non-POV
	•	[Screenshot – 02:44] – TSX Modules, Journey Overview and Guided Journey

Detailed User Stories
	•	As a Technical Seller, I want to see the current technical state for each opportunity and what actions are required to move forward, so that I can systematically progress opportunities toward a technical win.
	•	As a Technical Seller, I want TSX to show me when an opportunity has been stuck in the same technical state for too long, so that I can proactively re-engage stakeholders or adjust the validation plan.
	•	As a Technical Seller, I want a single “technical journey” view that clearly explains the relationship between the TSX Project, the Engagement, and the Opportunity, so that I am not guessing which object drives my workflow.

⸻

🔹 Objective #2: Clarify and Operationalize POV vs Non-POV Decisioning

Problem Statement
The distinction between Proof of Value (POV) and Non-POV Tech Validation is conceptually described but operationally fuzzy. The system does not yet help Technical Sellers decide whether a POV is warranted, which Non-POV options to use, or how to justify the cost and effort.

Functional Modules Affected
	•	TSX Guided Journey (POV Workflow and Non-POV Validations)
	•	Non-POV Companion App (BYOS, performance reports, workshops, reference calls, express testing)
	•	POV Companion App (POV Huddle, Test Plan, Proposal, Playback)
	•	Tech States 2–5 (Non-POV Tech Validation, POV Planning, POV Tech Validation, Tech Decision Pending)

Design Considerations
	•	The decision between Non-POV and POV should be explicit:
	•	Triggers/criteria (deal size, complexity, risk, competitive pressure).
	•	Impact on effort, time, and resource consumption.
	•	TSX should offer guided recommendations but maintain seller control.
	•	Each path must expose expected outputs (e.g., test plan, playback, reports) so sellers can set expectations with customers.

Screenshot & Transcript References
	•	[Screenshot – 12:26] – Tech states and associated processes
	•	[Screenshot – 28:26] – Full journey including Non-POV and POV branches
	•	[Transcript – ~13:30–18:00] – discussion of POV cost and Non-POV options

Detailed User Stories
	•	As a Technical Seller, I want TSX to highlight whether a given opportunity appears to require a full Proof of Value or can be handled with Non-Proof of Value options, so that I can choose the lightest effective validation path.
	•	As a Technical Seller, I want to see recommended Non-Proof of Value options (for example, performance reports, reference calls, workshops) based on the opportunity profile, so that I can confidently propose a lean validation plan when a full Proof of Value is not justified.
	•	As a Technical Seller, I want TSX to summarize the expected effort, duration, and resources for a proposed Proof of Value, so that I can align customer and internal stakeholders before committing.

⸻

🔹 Objective #3: Orchestrate Projects and Resources Without Manual Workarounds

Problem Statement
Technical Sellers are effectively project managers for each opportunity, but today rely on manual tracking, one-off folders, and separate systems for resource requests and team management. TSX needs to provide a cohesive project workspace anchored to the opportunity.

Functional Modules Affected
	•	TSX Project Workspace (New TSX Project, Add Team Members, Create TSX Content Folder)
	•	Tech Resource Request (Domain Consultant / SME onboarding)
	•	Opportunity Management
	•	Task Management and Notifications

Design Considerations
	•	“TSX Project” should feel like an organizing container for all people, tasks, and artifacts related to an opportunity’s technical work.
	•	Resource requests (for Domain Consultants and specialists) should be:
	•	Discoverable from the journey.
	•	Traceable (who was requested, status, assignments).
	•	Project-level views should show:
	•	Who is on the team (internal and customer).
	•	What is happening this week (tasks, workshops, test cycles).
	•	Key milestones tied to journey states.

Screenshot & Transcript References
	•	[Screenshot – 24:47] – left/mid section of TSX Project flow (Add Team Members, Create TSX Content Folder, Request DC)
	•	[Screenshot – 28:26] – full journey including Non-POV and POV paths
	•	[Transcript – ~21:17–28:26] – explanation of project-oriented nature of Technical Sellers and resource requests

Detailed User Stories
	•	As a Technical Seller, I want to create a TSX Project directly from an opportunity and automatically invite core team members, so that I do not have to build separate ad-hoc tracking artifacts for each deal.
	•	As a Technical Seller, I want to submit and track Technical Resource Requests for Domain Consultants within the same TSX Project workspace, so that I always know who has been requested, who is assigned, and what is pending.
	•	As a Technical Seller, I want TSX to show a consolidated view of all project tasks, workshops, and testing milestones linked to the technical journey state, so that I can coordinate both internal and customer teams effectively.

⸻

🔹 Objective #4: Govern the Artifact Lifecycle and Enable Fast Reuse

Problem Statement
Artifacts such as Design of Record (DOR), Account Success Plans, Non-POV artifacts, POV test plans and proposals, and executive playbacks are central to technical selling. Today they are scattered across drives and tools, making it hard to find, reuse, and keep them aligned with the technical journey and account history.

Functional Modules Affected
	•	TSX Artifacts (Templates & Document Storage, Design of Record, Account Success Plans, Non-POV Artifacts, POV Content, Executive Playback View)
	•	TSX Guided Journey (where artifacts are produced and consumed)
	•	AI/Copilot surface (future; right-hand artifact intelligence)

Design Considerations
	•	Each artifact type needs:
	•	A clear purpose (when it is required, who consumes it).
	•	A template or schema (fields and structure).
	•	A relationship to journey states and opportunities/accounts.
	•	Artifact retrieval should be contextual:
	•	“Show me everything we have for this opportunity.”
	•	“Show me comparable Design of Record documents for similar accounts.”
	•	Future AI behavior depends on consistent metadata and structure; scope must define minimum tagging and linkage.

Screenshot & Transcript References
	•	[Screenshot – 02:44] – TSX Modules with TSX Artifacts panel
	•	[Screenshot – 30:57] – Request Test Report workflow, adding artifacts to TSX Guided Journey
	•	[Transcript – ~28:23–30:57] – discussion of artifacts and documentation culture

Detailed User Stories
	•	As a Technical Seller, I want TSX to automatically organize Design of Record documents, test plans, proposals, and playback decks by opportunity and account, so that I can quickly find the latest approved version during customer conversations.
	•	As a Technical Seller, I want to search TSX for past artifacts from similar opportunities (for example, same product family or industry), so that I can reuse proven structures and avoid rebuilding every Design of Record or test plan from scratch.
	•	As a Technical Seller, I want TSX to indicate which artifacts are required before closing a technical state (for example, a completed Design of Record before Tech Win), so that I do not accidentally skip critical documentation.

⸻

🔹 Objective #5: Integrate Non-POV “Express Testing” into the Core Journey

Problem Statement
The Request Test Report (Express Testing) workflow is outlined in detail but is not yet smoothly integrated into TSX. There are open questions about navigation (modal vs jump-out) and data linkage to Salesforce requests, creating risk of context switching and status ambiguity.

Functional Modules Affected
	•	Non-POV Companion App – Express Testing
	•	TSX Guided Journey – Tech State 2 panel
	•	SFDC POC Request / Express Testing object and status
	•	TSX Artifacts (Test Reports)

Design Considerations
	•	From the Technical Seller’s perspective, Express Testing should feel like one continuous flow:
	•	Browse library → request report → track status → attach to journey artifacts.
	•	UX should minimize jumping between systems; if jumps are required, TSX must maintain breadcrumbs and context.
	•	Status of the underlying SFDC request (engineer, status, completion) must be visible within TSX to avoid double-checking elsewhere.

Screenshot & Transcript References
	•	[Screenshot – 30:57] – Workflow | Request Test Report (aka Express Testing)
	•	[Transcript – ~30:12–end] – stepwise description and inline questions about modals and data linking

Detailed User Stories
	•	As a Technical Seller, I want to open the Test Report Library from my Tech State 2 panel without losing my place in the TSX Guided Journey, so that I can evaluate available reports in context of the current opportunity.
	•	As a Technical Seller, I want to submit a new Express Testing request from within TSX and automatically link it to the underlying Salesforce Proof of Concept request, so that I do not have to duplicate data entry.
	•	As a Technical Seller, I want TSX to show the status of each Express Testing request (assigned engineer, in progress, completed) and notify me when a report is ready, so that I can promptly review and add it to my technical validation artifacts.

⸻

🔹 Objective #6: Clarify Reports & Analytics Around Technical Outcomes

Problem Statement
Reports & Analytics is recognized as a top module, but stakeholders do not yet know which views matter most to Technical Sellers. There is a risk of either recreating generic CRM reports or missing the specific technical KPIs that guide behavior (for example, tech win rates by product, POV cycle times, state-level leakage).

Functional Modules Affected
	•	Reports & Analytics (SFDC Reports and Dashboards, Non-SFDC Reports)
	•	Opportunity Management (forecast alignment with reps)
	•	TSX Guided Journey (state data feeding analytics)

Design Considerations
	•	Reporting should focus on technical outcomes, not just commercial ones:
	•	Tech win / loss rates.
	•	Distribution and duration of tech states.
	•	Volume and impact of POV vs Non-POV paths.
	•	TSX should support both:
	•	Individual seller views (“my pipeline, my POV workload, my tech risk”).
	•	Manager views (patterns across teams, products, regions).
	•	Design work must avoid over-building until there is clarity on core questions Technical Sellers and managers actually ask.

Screenshot & Transcript References
	•	[Screenshot – 02:44] – TSX Modules, Reports & Analytics area
	•	[Screenshot – 29:38] – module priority table showing Reports & Analytics as Build with rationale
	•	[Transcript – ~02:23–11:12, 28:23–29:38] – comments about needing to understand which reports matter

Detailed User Stories
	•	As a Technical Seller, I want a dashboard that shows my opportunities by technical state, including how long each has been in that state, so that I can focus my attention on deals at risk of stalling.
	•	As a Technical Sales Manager, I want to see tech win and tech loss patterns by product family and Non-Proof of Value versus Proof of Value path, so that I can coach my team on where to invest technical effort.
	•	As a Technical Seller, I want to view a workload summary of open Proof of Value engagements and Non-Proof of Value activities, so that I can manage my time and avoid overcommitting to too many concurrent Proof of Value projects.

⸻

🔹 Objective #7: Reduce Tool Sprawl and Context Switching

Problem Statement
Technical Sellers currently rely on a mix of external tools, drives, and Salesforce components. TSX risks becoming just another layer unless it deliberately anchors key workflows and clarifies when and how to move between systems.

Functional Modules Affected
	•	TSX Access and Integrations
	•	Templates & Document Storage (existing tools like Google Suite, theLoop)
	•	Non-SFDC reports and external services
	•	All companion apps (Non-POV and POV)

Design Considerations
	•	TSX should not attempt to replace every tool, but must clearly:
	•	Define which actions are “done in TSX” versus “opened from TSX”.
	•	Provide consistent patterns for jump-outs vs embedded views (for example, Express Testing library).
	•	Surface integration depth icons/labels (as hinted by the A/B/C/D legend in the TSX Modules slide) so users know what to expect when clicking.

Screenshot & Transcript References
	•	[Screenshot – 02:44] – TSX Modules and integration legend (A/B/C/D)
	•	[Screenshot – 30:57] – open questions about modals vs jump-outs
	•	[Transcript – ~02:23–11:12, 30:12–end] – remarks on external tools and integration questions

Detailed User Stories
	•	As a Technical Seller, I want TSX to indicate whether a linked tool opens as an integrated view or an external application, so that I am not surprised by disruptive context switches.
	•	As a Technical Seller, I want frequently used external tools (for example, document repositories or testing portals) accessible from a consistent TSX sidebar or panel, so that I do not have to maintain separate bookmark systems.
	•	As a Technical Seller, I want TSX to remember where I was in the technical journey when I return from an external tool, so that I can resume my workflow without re-navigating.

⸻







































## ChatGPT (2025-12-02T21:33:16.055396+00:00)

I’ve successfully populated the **User Stores V2** sheet with all objectives, affected modules, design considerations, and the detailed user stories broken into the two requested columns. Each objective spans multiple rows—one per user story—so you can easily filter or pivot the data by objective or persona action. The sheet is now fully documented as instructed【318086014959856†screenshot】.
