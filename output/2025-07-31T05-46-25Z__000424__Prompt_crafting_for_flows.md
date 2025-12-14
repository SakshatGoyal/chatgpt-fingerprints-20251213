# Prompt crafting for flows

## You (2025-07-31T05:46:25.581000+00:00)

I need your help crafting a prompt.

in the following exchanges i'll give you more context on the prompt, and i'll need you to refine the prompt through exchanges when i say begin crafting the prompt.

---

I'm attaching two screenshots. These two screenshots are essentially part of the platform we are building, and this platform will be for account executives at Palo Alto Networks. The idea is we create something that almost surfaces information, but then also encourages a few actions. So, I have a few hypothetical flows in mind. The idea is a user starts off at these screens and then uses the links. So, each of the rows have a link to a sales opportunity in Salesforce, uses the links to navigate to Salesforce, and then performs certain actions.

Essentially, what I'll need ChatGPT to do is to really flesh out all the flows, like in the sense that, okay, a user comes to this page, they read something either on the insights or something on the roles themselves, or selects a particular opportunity type, and then based on that, they decide to take certain actions and then continue those actions into Salesforce. So while I don't have a lot of specifics on Salesforce, I will need this custom GPT, which I'll be using for this prompt, to think through the actual typical pages within Salesforce, and then give me a breakdown of everything they see, everything they click, every action they take, all of that. That's part of the context. I'll elaborate more, but let me know if you have any questions.

## ChatGPT (2025-07-31T05:46:27.547163+00:00)

Thanks—that’s already a rich starting point. Here's what I understand so far, and where I might need some clarification to tighten the prompt logic:

---

### 🔍 **Current Understanding of the Context**
You’re building a **decision-support and action-surfacing platform** for Account Executives (AEs) at **Palo Alto Networks**. The screenshots show a filtered, insight-rich **opportunity list** that is tied to Salesforce data, surfacing deal risks (like "No Secured Technical Win" or "No Activity for 30 Days") and account health indicators. The idea is to guide users toward **targeted follow-up actions**, often routed through Salesforce, depending on what they discover here.

You want the prompt to help a reasoning model (O3) **simulate full user flows** that begin from this UI and continue through Salesforce, including:
- What the user notices and interprets on this platform.
- What opportunity or risk prompts them to act.
- What *specific Salesforce pages* they go to.
- What they see there.
- What they click or edit.
- What downstream actions they take (e.g. sending follow-ups, assigning PS resources, logging meetings).

This involves **user-intent inference + downstream CRM navigation + decision modeling**.

---

### 🧠 Questions to Tighten Scope and Execution Persona

1. **Primary Goal of Simulation Prompt**:
    - Is the intent to validate *design usability* (e.g. Are insights discoverable and actionable?) or to *train or test AE workflows* (e.g. What actions should an AE take to recover this opportunity?)?
    - Or are you hoping to use this prompt as a **scenario generator**—so the model can generate high-quality user journey flows for further UX iteration or automation mapping?

2. **Salesforce Familiarity for the Model**:
    - Should the model assume familiarity with *standard Salesforce CRM flow* (e.g., Opportunity Page → Activity Log → Notes → Quote → Close Plan), or do you want a model that can extrapolate plausible flows *even if it's not trained on actual Salesforce layouts*?

3. **Persona Scope**:
    - Are we modeling a specific kind of AE (e.g., Renewal-focused, Net-new, Technical overlay)?
    - Should the model also simulate *cross-functional handoff* steps (e.g., when the AE sees “No Secured Technical Win,” they loop in an SE or a CSAM)?

4. **Output Depth Preference**:
    - Are you expecting a **high-granularity step-by-step** walkthrough (clicks, page names, data seen)?
    - Or a **higher-level action chain**, e.g., “AE reviews opportunity → identifies lack of exec sponsor → creates exec alignment task in Salesforce → books exec meeting”?

---

Once you answer those, I’ll be ready to dive into constructing a tightly scoped reasoning prompt.

Let me know when you're ready to move to the next step or share more details.

## You (2025-07-31T05:52:53.493000+00:00)

I want to generate scenarios with this prompt so right now what I'm trying to do is flesh out individual flows and essentially create not a flowchart per se, but just a flow where we can describe things like what a user sees, the action they take, buttons they click, things like that. We may not need things like buttons they click, but it's just to jot down the interaction point. So it's not to validate some design usability, it's just to generate different scenarios.

Yes, for now the model should assume familiarity with standard CRM Salesforce flow.

I'm not sure if we need to define the persona because I'm using a custom GPT and hopefully the persona will be incorporated within the custom GPT. And as far as the output depth is concerned, I need a high granularity step-by-step walkthrough. The main context will be an AE in Palo Alto Networks.


here's a list of the flows:

1. Renewal & Quote Modification Flow

The user initiates the process from a renewal opportunity (e.g., at T-minus 60 days). The existing quote is cloned, and new products are added as needed. This modified quote is then marked as the new primary quote }. Pricing changes as a result of the added products. The user returns to the internal platform and triggers a request for AI-generated pricing for 3-, 5-, and 7-year terms }. The final step involves validating that the pricing variations reflect correctly across the integrated workflow.

4. Account Health-Based Actions

If an account shows signs like "customer technical health is critical" or "adoption is low," the platform guides the user to the Account Health page for deeper inspection }. This can initiate an intervention workflow where additional context is gathered and necessary actions are taken. These situations are treated as high risk for churn and are prioritized.

5. Support Ticket Use Case

This flow identifies accounts or quotes that are linked with a high number of support tickets }. The logic ties this to technical health—when too many support tickets exist, the account is considered at-risk. Users are routed to account health for further inspection and actions are taken to de-risk the deal }.

7. Executive Alignment

This use case tracks engagement from customer executives across different stages of a deal }. A UI in one of the customer apps shows which executives are engaged and their roles. If there is zero executive engagement, the account or deal is flagged as at-risk. This is considered one of the more critical indicators of whether a deal is strategically aligned.

8. Cross-Sell / Upsell Flow

While modifying a quote (e.g., adding a product during a renewal), the team recognized that this is inherently a cross-sell or upsell opportunity }. Initially considered as a separate flow, it was later decided to merge it with quote modification since both involve adding products. However, it still serves an expansion function and can lead to increased deal value.

12. Partner-Led / Co-Led / Direct Sales Flow (No-partner finalized journey)

The team discussed a dropdown flow where the sales motion could be Partner-led, Co-led, or Palo Alto-led }. While UI logic was drafted with Sumesh for this differentiation, no final journey was defined for the partner-led route. It was decided not to finalize this journey due to lack of integration clarity and potential data limitations.

11. Enterprise Agreement Journey

For large customers like AT&T with numerous contracts renewing on different dates, the Enterprise Agreement flow consolidates them into fewer master contracts with synchronized renewal dates }. This reduces operational burden, standardizes pricing, and simplifies forecasting. The benefit is a cleaner structure with fewer contracts per day to manage }.

--


These are just hypothetical flows, and that's fine. But these flows were derived from an open-ended conversation. So while these are open-ended flows, I do want the custom GPT to use its own personality, its own knowledge set, to thoroughly contextualize all of these. For context, I will also be sharing a CSV file that has 100 opportunities. So that's basically the data being used to populate this page. And I will be giving a list of filters that you see on the screen, like the actual values on the filters seen on the screen. And basically, I need the custom GPT to also use that into its scenario planning situation. Now, part of the flow will happen in on this application, but a lot of it will also happen in Salesforce itself.

## ChatGPT (2025-07-31T05:52:54.157596+00:00)

Perfect—this clears things up beautifully. You’re essentially designing a **scenario-generation engine** embedded within a custom GPT, powered by:

- **User-visible data** (CSV with 100 opps + filters like "No activity," "No Secured Technical Win").
- **Well-structured AE workflows** that often cross systems (Platform → Salesforce).
- **High-granularity walkthroughs** of AE interactions across both your platform and Salesforce.
- A **custom GPT persona** that deeply understands Salesforce, Palo Alto Networks sales motions, quote flows, renewal cycles, and risk-based prioritization heuristics.

---

### 🔧 Confirmed Execution Persona (for GPT responses)
You’re not asking the model to *imagine* what an AE would do—but to **simulate what a highly knowledgeable Palo Alto AE would realistically do**, based on surfaced risks or insights. The custom GPT persona will already be infused with domain knowledge (e.g., quote cloning, partner motion distinctions, pricing term impacts, etc.).

---

### ✅ Assumptions for Scenario Prompt Logic

1. **Your app is the start point**, but scenarios must flow into **Salesforce CRM flows**, referencing specific objects: Opportunity page, Quotes tab, Account Health view, Exec Engagement view, etc.
2. **You’ll pass in both structured data (CSV) and UI state (e.g., filters applied)** at runtime.
3. The model must **autonomously decide which flow(s) are relevant**, and simulate **step-by-step AE actions**, toggling between your platform and Salesforce.
4. You want **granular scenario generation** that includes:
   - What the AE notices.
   - Which filters or risks drive their attention.
   - What they click on.
   - Where they go in Salesforce.
   - What they update or review.
   - What intervention or next step they take.

---

I’m fully ready to move into prompt generation mode.

✅ If you're aligned with this structure and assumptions...

Please say: **“begin creating the prompt.”**

## You (2025-07-31T05:53:38.357000+00:00)

Carefully review once again all the conversations in this thread and begin creating the prompt.





## ChatGPT (2025-07-31T05:53:39.313177+00:00)

Below is a **ready-to-paste prompt** for your custom GPT.
I’ve structured it exactly to the specification we discussed—layered persona, four mandatory sections, and a quick-use checklist at the end.

---

## 🔧 Prompt for O3 Reasoning Model

**(Copy from here)**

---

### 1. Goal
You are “**Palo Alto Networks AE Copilot**,” a specialist reasoning agent that generates **high-granularity, step-by-step user-journey scenarios**.
Each scenario starts from the company’s Opportunity-Insights web app (screenshots provided) and continues through **standard Salesforce CRM pages**.
Your objective is to:

1. Detect which *risk signals / opportunity attributes* warrant attention (using the provided CSV of 100 opportunities + active UI filter states).
2. Choose the most relevant **sales motion flow** from the library below—or chain multiple flows when realistic.
3. Walk through every subsequent action an experienced Palo Alto Networks Account Executive would perform, including what they see, click, update, or create in Salesforce.
4. End with a clear outcome & next-step summary.

#### Available Flows
| ID | Name | Trigger Signals (examples) | Key Actions | Outcome |
|----|------|---------------------------|-------------|---------|
| 1 | Renewal & Quote Modification | Renewal nearing ≤ 60 days; need to add products | Clone quote → add SKUs → set as Primary → return to app → request AI pricing (3/5/7-yr) → validate | Updated quote & pricing variants |
| 4 | Account-Health Intervention | “Customer technical health is critical”, “Adoption low” | Open Account-Health in Salesforce → review telemetry & support metrics → launch Playbook task(s) | Risk mitigation plan |
| 5 | Support-Ticket Mitigation | ≥ threshold open tickets linked to opp/account | Open Cases tab → cluster tickets → engage Support mgr → document RCA | Technical health restored |
| 7 | Executive Alignment | Exec engagement = None | Open Exec Engagement component → identify missing roles → create Exec-sponsor outreach tasks → log emails/calls | Exec alignment in progress |
| 8 | Cross-Sell / Upsell | Quote modification includes net-new SKUs | Same as Flow 1 plus: map upsell SKUs → adjust ARR forecast → update Close Plan | Expanded deal value |
| 11 | Enterprise Agreement | ≥ 5 contracts w/ staggered renewals | Launch EA wizard → consolidate into master contract → align dates & terms → route for legal review | Simplified EA & forecast |
| 12 | Partner-Motion (Direct / Co-led) | “No Partner finalized” flag | Set Sales-Motion dropdown → identify partner or choose direct → update roles & collaboration notes | Correct sales-motion alignment |

*(Feel free to enrich flows with domain knowledge when details are missing.)*

---

### 2. Return Format
Output **one or more scenarios** in the following JSON-compatible Markdown fence:

```json
{
  "scenario_name": "<Flow ID & short title>",
  "trigger_opportunity": {
    "opportunity_id": "<from CSV>",
    "key_attributes": ["<list the risk flags / columns that triggered flow>"]
  },
  "step_by_step": [
    {
      "system": "Web-App",
      "ui_element": "<e.g., Risk Category filter pill>",
      "user_action": "<click / hover / read>",
      "ae_thought": "<why this matters>"
    },
    {
      "system": "Salesforce",
      "page": "<e.g., Opportunity → Quotes>",
      "user_action": "<clone quote>",
      "ae_thought": "<reasoning behind action>"
    }
    // …continue until scenario ends
  ],
  "outcome_summary": "< 2-3 sentences>",
  "next_steps": ["<action item 1>", "<action item 2>"]
}
```

Generate **at least 8 steps per scenario**; include both screens.
Render multiple scenarios as an array `[...]`.

---

### 3. Warnings & Guardrails

1. **Empirical vs. Hypothetical** – When Salesforce field names or UI wording are uncertain, mark with `(assumed)` and proceed.
2. **No private data** – Never fabricate real customer names beyond what’s in CSV.
3. **Speculation limits** – Do not guess legal or finance approvals; flag them as “requires confirmation.”
4. **Uncertainty handling** – If multiple AE paths exist, choose the most common and note alternates in `ae_thought`.
5. **Clarity** – Keep each `ae_thought` ≤ 25 words; avoid jargon not used at Palo Alto Networks.

---

### 4. Context & Additional Elements

- **Persona**: Senior Palo Alto Networks Account Executive, quota-carrying, proficient in Cortex & Firewall portfolio, comfortable with Salesforce Lightning.
- **Systems**:
  - **Web-App**: Filters (`Time Period`, `Product`, `R/UNN`, `Forecast Category`, `Sales Stage`, `Deal Size`, `Risk Category`).
  - **Salesforce Objects**: Opportunity, Quote, Quote Line Items, Cases, Account Health, Executive Engagement component, Playbooks, EA Wizard.
- **Data Inputs**:
  - `opp_csv`: 100 opportunities with fields (e.g., Opportunity ID, Stage, ARR, Risk Flags, Account Health, Last Activity Date, etc.).
  - `active_filters`: current UI filter state (dict).
- **Domain Nuances**: Renewal target at T-60; quote primary flag; partner motions; EA consolidation best practice.
- **Output Consumers**: Design team & sales-ops analysts who will convert scenarios into playbooks and UX flows.

---

### ✅ Checklist before responding
- [ ] Chose *at least* one relevant Flow ID.
- [ ] Cited exact risk triggers from CSV.
- [ ] Included **≥ 8 detailed steps** across both systems.
- [ ] Followed JSON schema exactly.
- [ ] Respected guardrails on assumptions & private data.

---

**(End of prompt)**
