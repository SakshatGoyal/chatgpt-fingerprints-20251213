# Create user story prompt

## You (2025-08-27T02:41:58.488000+00:00)

Help me create a prompt for the following intent. I'm sharing five dashboard tables and what I need is for a GPT to create what's called user stories. Now the user story should follow a very typical format. The main persona in the user story is sales manager. I will be using a custom GPT for these user stories. So we need to define the persona to some degree but feel free to ask me any questions you have.





## ChatGPT (2025-08-27T02:42:00.876096+00:00)

Awesome—got the five dashboards. I can turn these into crisp, repeatable user stories for a **Sales Manager** persona. Before I craft the final O3-optimized prompt, here’s a quick plan + a few targeted questions so we nail the format and intent.

## What I’ll generate (once you say “begin creating the prompt”)
- A reusable prompt that tells your custom GPT to:
  - Read the dashboards and extract **actionable insights** across 5 themes: Pipeline/CCBC, Coverage & Enablement, Exec Engagement, Whitespace, and Technical Validation (POV/Win-rates).
  - Emit **user stories** in the classic form:
    **As a Sales Manager for \<scope\>, I want \<capability/action\> so that \<business outcome\>.**
  - Include structured **Acceptance Criteria** (Given/When/Then), **evidence** pulled from the tables, **target metrics & dates**, **priority**, **owner/collaborators**, **risks/assumptions**, and **next steps**.
  - Follow strong guardrails: no invented data, call out uncertainty, and prefer quantified thresholds.

## Draft Sales Manager Persona (you can tweak)
- **Scope:** region/district manager overseeing multiple reps + SEs across product lines.
- **Primary goals:** hit quarterly revenue; convert commit to closed; maintain healthy coverage (territories filled, ramp %); increase exec engagement (EBC/EOR/CXO); expand platform penetration; improve technical win rate and shorten POV cycle time.
- **Levers:** deal inspection, enablement/certification, exec mapping, campaign allocation, SE resourcing, POV governance.
- **Cadence:** weekly inspection, monthly forecast, quarterly plan.

## User Story Template (proposed)
- **Theme:** Pipeline | Coverage | Exec Engagement | Whitespace | Technical
- **User Story:** *As a Sales Manager for \<scope\>, I want \<capability/action\> so that \<business outcome\>.*
- **Evidence:** *Key metrics + ranges pulled from the dashboards (e.g., “CCBC $31M, Closed $1M; commit exposure high; ‘Critical’ status”).*
- **Acceptance Criteria (BDD):**
  - **Given** \<current baseline + source metric\>
  - **When** \<action/inspection leveraged\>
  - **Then** \<target outcome with numbers & date\>
- **Targets/Timebox:** \<numeric goal + by when\>
- **Priority:** High/Med/Low (or RICE—your call)
- **Owner/Collaborators:** \<roles, not names\>
- **Risks/Assumptions:** \<data gaps, dependencies\>
- **Next Steps:** \<3–5 concrete actions\>

*Tiny example from your Pipeline view:*
**Theme:** Pipeline
**Story:** As a Sales Manager for **Central FIS**, I want to **raise commit-to-close conversion** so that **Q target is achievable**.
**Evidence:** CCBC ≈ **$31M** with just **$1M closed**; high commit exposure flagged as **Critical**.
**Acceptance:** Given close rate baseline **≤22%** this Q, when we **run late-stage deal reviews + exec sponsor alignment** on top 10 deals, then **closed** increases to **≥$8M** and **slip rate ≤15%** by **EoQ**.
**Priority:** High. **Next steps:** identify top 10, assign exec sponsor, schedule POV exit criteria reviews, etc.

---

## 10 quick questions to tailor the final prompt
1. **Purpose of the stories:** sales action plan for managers, or engineering/RevOps backlog to improve the dashboards?
2. **Granularity:** per **region/district** (as shown) or also per **rep** when data is present?
3. **Count per run:** cap at, say, **5–8 stories** (top risks & opportunities) or “as many as the data suggests”?
4. **Acceptance criteria style:** okay to use **Given/When/Then** (BDD)?
5. **Prioritization method:** simple **High/Med/Low**, **MoSCoW**, or **RICE**?
6. **Targets:** do you have standard thresholds (e.g., “% reps ramped ≥80%”, “Tech win rate ≥60%”, “POV median ≤45 days”), or should I propose defaults?
7. **Privacy:** avoid using real **people’s names** from the tables and stick to roles (Rep A, SE Mgr), correct?
8. **Inputs to the GPT:** screenshots like these, copy-pasted tables, or structured JSON/CSV? (This affects how the prompt instructs extraction.)
9. **Tone:** concise & prescriptive vs. more advisory?
10. **Extras:** include **rationale**, **data caveats**, and a **1-line executive summary** per story?

Reply with answers (or just your preferences). When you’re ready, say **“begin creating the prompt”** and I’ll deliver the final O3-optimized prompt with persona, guardrails, and checklist.

## You (2025-08-27T02:46:10.886000+00:00)

The purpose of these user stories is for UX design. I'm not sure about granularity, but I think we have to keep it from the point of view of a sales manager. So as a sales manager, I want to X, Y, Z and then define a use case that is available that can be achieved through the content we have. I think let's keep it at 8 to 10 user stories per visual or per table. I don't understand the fourth question. No, we don't need any prioritization method. I think let's just leave out the targets thing altogether. Yeah, you don't need to use people's real names. Yeah, these screenshots will be the only inputs for GPT. The tone should be concise and prescriptive. No, we don't need any executive summary or extras for user story.





## ChatGPT (2025-08-27T02:46:11.666980+00:00)

Perfect—thanks for the direction. Here’s what I’ll lock in for the final O3 prompt:

- **Purpose:** UX design user stories.
- **Persona:** Sales Manager (region/district scope; leads AEs + SEs).
- **Point of view:** always “As a Sales Manager, I want … so that …”.
- **Per visual/table:** **8–10 user stories**, each paired with a **use case that can be achieved from the content shown**.
- **Tone:** concise, prescriptive.
- **No:** prioritization, targets, BDD acceptance criteria, exec summaries.
- **Data handling:** use only what’s visible in screenshots; no real names; no invented numbers; call out uncertainty if text is unreadable.

If that’s correct, say **“begin creating the prompt”** and I’ll deliver the complete O3-optimized prompt with persona, return format, and guardrails—ready to drop into your custom GPT.

## You (2025-08-27T02:47:23.287000+00:00)

begin creating the prompt





## ChatGPT (2025-08-27T02:47:23.972584+00:00)

# O3 Prompt: Sales-Manager UX User Stories from Dashboard Screenshots

## Goal
Produce concise, prescriptive **Sales Manager** user stories for UX design, grounded only in the provided dashboard screenshots. Output **8–10 user stories per visual/table**, each paired with a concrete **use case that can be achieved with the content in that visual**.

## Execution Persona (for O3)
Act as a **Senior UX & RevOps Analyst** who translates sales dashboards into practical user stories for product/design. You understand pipeline, coverage, exec engagement, whitespace, and technical validation workflows.

## Primary Persona (inside each story)
**Sales Manager** (region/district scope; leads AEs + SEs + SEs). Focus on inspection, enablement, exec engagement, platform expansion, and POV governance.

## Inputs
- Up to N screenshots (PNG/JPG). Each screenshot is a **Visual i**.
- No additional data sources. Treat all numbers, labels, statuses, and legends as ground truth only if visible/readable.

## Return Format (strict)
For **each Visual i** (use the visible title if present; otherwise infer a short theme like “Pipeline/CCBC”, “Coverage & Enablement”, “Exec Engagement”, “Whitespace”, or “Technical/POV”):
- Print a heading: `Visual i — <detected title/theme>`
- Then list **8–10 items**, each in exactly this two-line structure:
  1. **User Story:** *As a Sales Manager, I want \<capability/action\> so that \<business outcome\>.*
     **Use Case (from this visual):** *\<How this specific table/chart enables the action—name the exact columns, filters, statuses, or trends used; e.g., “sort ‘Commit’ vs ‘Closed’, filter ‘Critical’, inspect district rows”\>.*

Formatting rules:
- Keep each **User Story** to **≤24 words**; each **Use Case** to **≤24 words**.
- Do **not** include prioritization, targets, BDD acceptance criteria, or executive summaries.
- Do **not** use real people’s names; refer to roles or groups (e.g., “district,” “rep,” “SE lead”).

## Method (how to think)
1. **Parse** the screenshot: capture title, filters (e.g., Quarter/Product/Region), column labels, statuses (“On Track,” “Critical”), and any WoW/percent bars.
2. **Map to Sales-manager tasks** by theme:
   - **Pipeline/CCBC:** commit→close conversion, best-case inspection, late-stage slippage, region heatmap/status, deal reviews.
   - **Coverage & Enablement:** territories filled, reps ramped, accounts per rep, certifications by product, reps in deals.
   - **Exec Engagement:** CXO coverage, EBCs/EORs scheduled vs completed, last-3 vs prior-3 trends.
   - **Whitespace:** product penetration %, active pipe by module, platformization opportunities.
   - **Technical/POV:** tech win rate, POV win rate, median POV duration, exit criteria governance.
3. **Write** each user story in the exact persona format; pair it with a **use case** that cites the **specific fields/controls** visible in that visual (columns, filters, status chips, trend tiles).
4. **De-duplicate** within a visual; vary actions (filter, sort, group, drill-in, compare trends).
5. **Sanity-check grounding:** if a required field is unreadable, mark it in the use case as `[illegible label]` and don’t invent numbers.

## Warnings & Guardrails
- **No fabrication.** Only reference metrics/labels clearly visible in the screenshot. If uncertain, state “from \<label\>” without numeric claims.
- **No identity leakage.** Never output real person names from the tables.
- **Concise & prescriptive.** Avoid commentary or rationale beyond the two required lines.
- **Quantity rule.** Aim for **8–10** unique stories per visual. If the visual can’t support that without repetition, stop at the maximum distinct items and proceed to the next visual.

## Mini example (pattern only)
- **User Story:** As a Sales Manager, I want to focus late-stage deals so that commit reliably converts to closed.
  **Use Case (from this visual):** Sort **Commit vs Closed** columns; filter **status = Critical**; inspect top districts for gaps.

## Checklist (apply before finalizing)
- [ ] Every visual has a title/theme and **8–10** (or max unique) items.
- [ ] Every item has **exactly two lines**: *User Story* and *Use Case (from this visual)*.
- [ ] All actions trace to **visible fields/filters/statuses**.
- [ ] No names, no invented numbers, no extra sections.
- [ ] Wording is tight, imperative, and sales-manager-centric.
