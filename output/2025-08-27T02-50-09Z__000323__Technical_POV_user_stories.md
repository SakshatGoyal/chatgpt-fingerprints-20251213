# Technical POV user stories

## You (2025-08-27T02:50:09.359000+00:00)

## Goal

Produce concise, prescriptive **Sales Manager** user stories for UX design, grounded only in the provided dashboard screenshots. Output **8–10 user stories per visual/table**, each paired with a concrete **use case that can be achieved with the content in that visual**.

## Execution Persona (for O3)

Act as a **Senior UX & RevOps Analyst** who translates sales dashboards into practical user stories for product/design. You understand pipeline, coverage, exec engagement, whitespace, and technical validation workflows.

## Primary Persona (inside each story)

**Sales Manager** (region/district scope; leads AEs + SEs + SEs). Focus on inspection, enablement, exec engagement, platform expansion, and POV governance.

## Inputs

* Up to N screenshots (PNG/JPG). Each screenshot is a **Visual i**.
* No additional data sources. Treat all numbers, labels, statuses, and legends as ground truth only if visible/readable.

## Return Format (strict)

For **each Visual i** (use the visible title if present; otherwise infer a short theme like “Pipeline/CCBC”, “Coverage & Enablement”, “Exec Engagement”, “Whitespace”, or “Technical/POV”):

* Print a heading: `Visual i — <detected title/theme>`
* Then list **8–10 items**, each in exactly this two-line structure:

  1. **User Story:** *As a Sales Manager, I want \<capability/action> so that \<business outcome>.*
     **Use Case (from this visual):** *\<How this specific table/chart enables the action—name the exact columns, filters, statuses, or trends used; e.g., “sort ‘Commit’ vs ‘Closed’, filter ‘Critical’, inspect district rows”>.*

Formatting rules:

* Keep each **User Story** to **≤24 words**; each **Use Case** to **≤24 words**.
* Do **not** include prioritization, targets, BDD acceptance criteria, or executive summaries.
* Do **not** use real people’s names; refer to roles or groups (e.g., “district,” “rep,” “SE lead”).

## Method (how to think)

1. **Parse** the screenshot: capture title, filters (e.g., Quarter/Product/Region), column labels, statuses (“On Track,” “Critical”), and any WoW/percent bars.
2. **Map to Sales-manager tasks** by theme:

   * **Pipeline/CCBC:** commit→close conversion, best-case inspection, late-stage slippage, region heatmap/status, deal reviews.
   * **Coverage & Enablement:** territories filled, reps ramped, accounts per rep, certifications by product, reps in deals.
   * **Exec Engagement:** CXO coverage, EBCs/EORs scheduled vs completed, last-3 vs prior-3 trends.
   * **Whitespace:** product penetration %, active pipe by module, platformization opportunities.
   * **Technical/POV:** tech win rate, POV win rate, median POV duration, exit criteria governance.
3. **Write** each user story in the exact persona format; pair it with a **use case** that cites the **specific fields/controls** visible in that visual (columns, filters, status chips, trend tiles).
4. **De-duplicate** within a visual; vary actions (filter, sort, group, drill-in, compare trends).
5. **Sanity-check grounding:** if a required field is unreadable, mark it in the use case as `[illegible label]` and don’t invent numbers.

## Warnings & Guardrails

* **No fabrication.** Only reference metrics/labels clearly visible in the screenshot. If uncertain, state “from \<label>” without numeric claims.
* **No identity leakage.** Never output real person names from the tables.
* **Concise & prescriptive.** Avoid commentary or rationale beyond the two required lines.
* **Quantity rule.** Aim for **8–10** unique stories per visual. If the visual can’t support that without repetition, stop at the maximum distinct items and proceed to the next visual.

## Mini example (pattern only)

* **User Story:** As a Sales Manager, I want to focus late-stage deals so that commit reliably converts to closed.
  **Use Case (from this visual):** Sort **Commit vs Closed** columns; filter **status = Critical**; inspect top districts for gaps.

## Checklist (apply before finalizing)

* [ ] Every visual has a title/theme and **8–10** (or max unique) items.
* [ ] Every item has **exactly two lines**: *User Story* and *Use Case (from this visual)*.
* [ ] All actions trace to **visible fields/filters/statuses**.
* [ ] No names, no invented numbers, no extra sections.
* [ ] Wording is tight, imperative, and sales-manager-centric.





## ChatGPT (2025-08-27T02:50:12.071981+00:00)

Visual 1 — Technical/POV
- **User Story:** As a Sales Manager, I want to sort tech win rates so that I coach districts with the weakest validation.
  **Use Case (from this visual):** Sort **Tech Win Rate %** column; inspect bottom district rows.

- **User Story:** As a Sales Manager, I want to shorten long POVs so that sales cycles compress predictably.
  **Use Case (from this visual):** Sort **Median POV Duration (days)** descending; target longest-duration districts.

- **User Story:** As a Sales Manager, I want to boost POV win rates so that more validations convert to spend.
  **Use Case (from this visual):** Sort **POV Win Rate %** ascending; focus bottom districts for enablement.

- **User Story:** As a Sales Manager, I want to correlate tech and POV wins so that I isolate handoff issues.
  **Use Case (from this visual):** Compare adjacent **Tech Win Rate %** and **POV Win Rate %** columns per district.

- **User Story:** As a Sales Manager, I want to spotlight tech-win yet low-POV districts so that exit criteria are tightened.
  **Use Case (from this visual):** Sort both **Tech Win Rate %** and **POV Win Rate %**; cross-check mismatched districts.

- **User Story:** As a Sales Manager, I want to enforce commit gates so that only validated deals forecast confidently.
  **Use Case (from this visual):** Use district **POV Win Rate %** and **Median POV Duration** to set review thresholds.

- **User Story:** As a Sales Manager, I want to deploy SE support surgically so that stuck POVs progress.
  **Use Case (from this visual):** Sort **Median POV Duration**; assign senior SEs to top-duration districts.

- **User Story:** As a Sales Manager, I want to capture reference wins so that future POVs accelerate.
  **Use Case (from this visual):** Sort **POV Win Rate %** descending; tap top districts for customer references.

- **User Story:** As a Sales Manager, I want to monitor district variance so that coaching agendas are data-driven.
  **Use Case (from this visual):** Compare **District** rows across all three columns; note color-coded percentage chips.


Visual 2 — Whitespace
- **User Story:** As a Sales Manager, I want to rank product whitespace so that expansion plays target biggest gaps.
  **Use Case (from this visual):** Sort each module’s **White space Accts** under Firewall, CDSS, SASE, Cortex & Cloud, Unit 42.

- **User Story:** As a Sales Manager, I want to prioritize active pipe accounts so that near-term cross-sell closes.
  **Use Case (from this visual):** Sort **%Accts w/ active pipe** within chosen module sections.

- **User Story:** As a Sales Manager, I want to drive platformization so that multi-module stickiness increases.
  **Use Case (from this visual):** Use **%Accts platformized** across modules to identify districts needing plays.

- **User Story:** As a Sales Manager, I want to sequence outreach by engagement so that reps prioritize responsive accounts.
  **Use Case (from this visual):** Use **%Accts active in last 3 yrs** column to segment outreach.

- **User Story:** As a Sales Manager, I want to weight plays by enterprise scale so that larger accounts get attention.
  **Use Case (from this visual):** Filter by **#G2K Accts** and **#Accts** to size territory focus.

- **User Story:** As a Sales Manager, I want to check account hygiene so that expansion doesn’t stall.
  **Use Case (from this visual):** Review **%Accts w/ ASR compl.** alongside **White space Accts**.

- **User Story:** As a Sales Manager, I want to allocate capacity by ATR so that resources match opportunity.
  **Use Case (from this visual):** Use **ATR** per-module columns to plan staffing.

- **User Story:** As a Sales Manager, I want to launch Firewall upsell campaigns so that core base expands.
  **Use Case (from this visual):** Inspect Firewall **White space Accts** and **%Accts w/ active pipe** together.

- **User Story:** As a Sales Manager, I want to grow SASE footprint so that networking security consolidates.
  **Use Case (from this visual):** Use SASE **%Accts platformized** and **White space Accts** to target.

- **User Story:** As a Sales Manager, I want to position Unit 42 services so that strategic attach increases.
  **Use Case (from this visual):** Sort Unit 42 **White space Accts**; cross-check **%Accts w/ active pipe**.


Visual 3 — Exec Engagement
- **User Story:** As a Sales Manager, I want to raise CXO coverage so that deals de-risk earlier.
  **Use Case (from this visual):** Sort **%Accts w/ CXO mtgs in last 6 mos**; compare 12-month column.

- **User Story:** As a Sales Manager, I want to build an EBC runway so that next-quarter pipeline is executive-validated.
  **Use Case (from this visual):** Review **#EBCs scheduled for next 3 mos** by district.

- **User Story:** As a Sales Manager, I want to measure EBC impact so that we invest in effective sessions.
  **Use Case (from this visual):** Compare **#EBCs completed in last 3 mos** with **Last 3 vs prior 3 mos**.

- **User Story:** As a Sales Manager, I want to maintain executive cadence so that renewals and expansions stay warm.
  **Use Case (from this visual):** Use **%Accts w/ CXO mtgs in last 12 mos** to flag gaps.

- **User Story:** As a Sales Manager, I want to ensure EOR coverage so that late-stage evaluations accelerate.
  **Use Case (from this visual):** Review **#EORs completed in last 3 mos** and **#EORs scheduled for next 3 mos**.

- **User Story:** As a Sales Manager, I want to act on declining momentum so that engagement rebounds fast.
  **Use Case (from this visual):** Check **Last 3 vs prior 3 mos** for negatives across EBCs and EORs.

- **User Story:** As a Sales Manager, I want to allocate exec sponsors so that scheduled meetings land.
  **Use Case (from this visual):** Use **#EBCs scheduled for next 3 mos** to plan leadership participation.

- **User Story:** As a Sales Manager, I want to account-weight goals so that coverage scales with portfolio size.
  **Use Case (from this visual):** Reference **#Accts** alongside CXO meeting percentages.

- **User Story:** As a Sales Manager, I want to triage districts with zero coverage so that we recover relationships.
  **Use Case (from this visual):** Filter for low **%Accts w/ CXO mtgs in last 6 mos**; schedule EBCs/EORs.


Visual 4 — Coverage & Enablement
- **User Story:** As a Sales Manager, I want to close staffing gaps so that territory coverage stabilizes.
  **Use Case (from this visual):** Inspect **%Territories filled** column and **WoW Trend** tile.

- **User Story:** As a Sales Manager, I want to accelerate ramp so that productivity starts earlier.
  **Use Case (from this visual):** Use **%Reps ramped** tile and column; sort ascending.

- **User Story:** As a Sales Manager, I want to balance account load so that reps can prospect effectively.
  **Use Case (from this visual):** Review **#Accts per Rep** tile and column per district.

- **User Story:** As a Sales Manager, I want to manage attrition impact so that revenue isn’t interrupted.
  **Use Case (from this visual):** Monitor **#Last 3M Attrition** alongside **%Territories filled** and **#Reps in seat**.

- **User Story:** As a Sales Manager, I want to uplift product readiness so that CDSS deals scale.
  **Use Case (from this visual):** Compare CDSS **%Reps Certified (Netsec)** versus **%Reps in Deals** across districts.

- **User Story:** As a Sales Manager, I want to expand SASE attach so that platform revenue grows.
  **Use Case (from this visual):** Inspect SASE **%Reps Certified** and **%Reps in Deals**; flag gaps.

- **User Story:** As a Sales Manager, I want to build Cortex & Cloud capability so that cloud deals progress.
  **Use Case (from this visual):** Use Cortex & Cloud **%Reps Certified** and **%Reps in Deals** columns.

- **User Story:** As a Sales Manager, I want to boost Unit 42 participation so that services attach increases.
  **Use Case (from this visual):** Compare Unit 42 **%Reps Certified** versus **%Reps in Deals**.

- **User Story:** As a Sales Manager, I want to coach based on attainment so that best practices spread.
  **Use Case (from this visual):** Use **%Reps w/ >=100% PY** and **%Reps w/ >=100% CY** to identify mentors.

- **User Story:** As a Sales Manager, I want to lift firewall coverage so that core line maintains momentum.
  **Use Case (from this visual):** Review Firewall **%Reps in Deals** column per district.


Visual 5 — Pipeline/CCBC
- **User Story:** As a Sales Manager, I want to inspect commit conversion so that forecast credibility improves.
  **Use Case (from this visual):** Compare **Commit** vs **Closed** columns; review regional rows.

- **User Story:** As a Sales Manager, I want to triage critical regions so that help is reallocated quickly.
  **Use Case (from this visual):** Filter **status = Critical**; inspect **Total CCBC**, **Closed**, **Commit**, **Best Case In**.

- **User Story:** As a Sales Manager, I want to pressure-test upside so that best-case risk is understood.
  **Use Case (from this visual):** Use **Best Case In** column; compare to **Commit** per region.

- **User Story:** As a Sales Manager, I want to track momentum so that week-over-week actions are timely.
  **Use Case (from this visual):** Read **WoW Trend** tiles for **Closed**, **Commit**, and **Best Case In**.

- **User Story:** As a Sales Manager, I want to prioritize large yet under-closing regions so that attention follows impact.
  **Use Case (from this visual):** Sort **Total CCBC** descending; inspect **Closed** gaps.

- **User Story:** As a Sales Manager, I want to recalibrate by dimension so that the forecast reflects reality.
  **Use Case (from this visual):** Adjust **Quarter**, **Product**, and **Region** filters; review progress bar to target.

- **User Story:** As a Sales Manager, I want to flag overexposed commit so that risk is contained.
  **Use Case (from this visual):** Scan regions where **Commit** dominates relative to **Closed**.

- **User Story:** As a Sales Manager, I want to validate progress to plan so that stakeholders align.
  **Use Case (from this visual):** Use top **progress bar** and **Closed** tile against the $100M target.

- **User Story:** As a Sales Manager, I want to run deal reviews by team so that accountability increases.
  **Use Case (from this visual):** Expand region rows to district/rep level; inspect **Closed/Commit/Best Case In**.

- **User Story:** As a Sales Manager, I want to align resources to near-term upside so that quarter close improves.
  **Use Case (from this visual):** Sort **Best Case In** descending; coordinate help for top regions.

## You (2025-08-27T18:47:06.703000+00:00)

Please export this into a downloadable CSV format that will be compatible with Google Sheets.







## ChatGPT (2025-08-27T18:53:35.800546+00:00)

Done. I’ve put a clean, Google-Sheets-friendly CSV in the canvas (right pane) titled **Sales Manager User Stories**.

Tip: In Sheets, use **File → Import → Upload → Replace current sheet** (or paste into A1).
