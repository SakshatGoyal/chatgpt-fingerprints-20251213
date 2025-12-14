# PESS framework customization

## You (2025-08-26T20:27:46.872000+00:00)

You will be given:

- A **Persona**
- A **Purpose**
- A fixed **PESS Framework** (a structured set of research modules)

Your task is to **transform the generic PESS modules** into a set of **contextually rich, creatively framed, and purpose-driven research prompts**. These questions will guide a human research team in gathering the most relevant and nuanced material needed to emulate the persona effectively for the stated purpose.

---

### ✳️ Inputs:

- **Persona**: District Sales Manager at Palo Alto Networks.
- **Purpose**: as a thought partner, acting as a persona during my product design process.
- **PESS Question Template**:

    ```jsx
    ## 📝 PESS Research Guide: [Persona] for [Purpose]

    ### 1. Persona Definition (Who)
    Select relevant modules:
    - [ ] Identity Basics
    - [ ] Tone & Style
    - [ ] Behavioral Patterns
    - [ ] Values & Motivations
    - [ ] Exemplars & Anecdotes
    - [ ] Domain Competence *(optional)*

    ### 2. Purpose Definition (What For)
    Clearly identify your primary use-case modules:
    - [ ] Emotional & Social Guidance
    - [ ] Strategic & Analytical Reasoning
    - [ ] Creative & Expressive Tasks
    - [ ] Procedural & Functional Tasks
    - [ ] Moral & Ethical Reasoning

    ### 3. Recommended Information-Gathering Sources
    Based on chosen modules, gather from:
    - Primary sources (e.g., interviews, writings by persona)
    - Secondary sources (biographies, critical analysis)
    - Fictional canon (scripts, character wikis, authoritative sources)

    **Example:**
    If "Emotional & Social Guidance" selected → memoir excerpts, personal anecdotes, interviews reflecting values.

    If "Procedural & Functional Tasks" selected → step-by-step descriptions, documented decision processes, case-studies.

    ### 4. Specific Information to Include
    Prioritize gathering:
    - Authentic examples closely tied to persona’s demonstrated behavior
    - Explicit declarations of values, priorities, motivations
    - Demonstrated reasoning processes (if relevant to task)

    ### 5. Pitfalls & What to Avoid
    - Avoid assumptions of competence based solely on fame or presence in a domain.
    - Beware user-added ideological biases; cross-check authenticity.
    - Do not assume fictional logic applies to real-world tasks.

    ### 6. Depth and Fidelity Target
    - Clearly define the depth required:
      **High (exact voice replication)** → Rich exemplars & anecdotes, detailed style & tone guides.
      **Medium (style-aware, flexible)** → Values, general patterns, some exemplars.
      **Low (loose imitation)** → Identity basics, core values only.

    ### 7. Hidden Assumptions & Risk Mitigation
    - Identify assumptions in chosen persona’s public image vs. reality.
    - Check cultural bias in collected sources.
    - Prepare fallback instructions for handling uncertainty (style drift, hallucination).

    ### 🔄 Final Checklist (Before Use)
    - Confirm fidelity matches task requirement.
    - Confirm adequate factual grounding for purpose.
    - Confirm inclusion of modular packs matches intended complexity and depth.

    ```


---

### 🎯 Objective:

Transform each *selected* PESS module into a **set of exploratory, research-ready questions** that are:

- Tailored to the Persona and Purpose
- Specific and deep enough to guide meaningful, grounded research
- Framed creatively—favoring open-ended, imaginative, or situational language
- Sensitive to personal, behavioral, and cultural nuance
- Free from clichés and generalizations

---

### 🧩 Instructions:

1. **Only consider the PESS modules marked with `[x]`**.

    Ignore those marked with `[ ]` or not selected.

2. **For each selected module**, generate 1–5 high-quality exploratory questions.

    Prioritize **depth, relevance, and contextual grounding** over quantity.

    If only one great question emerges, that’s better than five generic ones.

3. **Frame the questions in a creative, open-ended style** that invites nuanced research.

    Use formats like:

    - “What might {{Persona}} say if…”
    - “Are there examples of situations where…”
    - “How has {{Persona}} responded to…”
    - “In what ways has {{Persona}} demonstrated…”
    - “What real-life moments reflect {{Persona}}’s view on…”
4. **Incorporate the lens of the stated Purpose.**

    Shape each question so it uncovers information directly useful for fulfilling the end-goal.

5. **Adapt based on the Fidelity Target** (if present in the PESS):
    - For **High Fidelity** → Ask for quotes, anecdotes, precise language, voice tone
    - For **Medium Fidelity** → Ask about patterns, values, reasoning styles
    - For **Low Fidelity** → Ask about identity basics and general worldview
6. **You may connect insights across modules if it enhances the questions’ relevance or depth.**

    Overlap is acceptable if it strengthens contextual integrity.

7. **Do not answer the questions.**

    Only generate the questions themselves.

8. **Optional but encouraged:**

    Where helpful, recommend the most suitable source types (e.g., memoirs, interviews, public speeches) for each question.


---

### ✅ Output Format:

Your output should be structured as:

```
css
CopyEdit
## Research Objective: Find empirical information to help create a custom GPT of {{Persona}} [for] {{Purpose}}

### [Module Title]
- [Exploratory Question 1]
- [Exploratory Question 2]
- [Exploratory Question 3]
- [Exploratory Question 4]
- [Exploratory Question 5]
...

```

Repeat this structure for **each selected module** in the PESS framework.

---

### 🔄 Final Check Before Output:

- Are your questions creatively and concretely framed?
- Are they deeply tied to both Persona and Purpose?
- Would a researcher reading each question know *where to start looking* for answers?
- Did you avoid vague, surface-level phrasing?





## ChatGPT (2025-08-26T20:27:47.695704+00:00)

```css
CopyEdit
## Research Objective: Find empirical information to help create a custom GPT of District Sales Manager at Palo Alto Networks [for] acting as a thought partner during product design

### Identity Basics
- What would a top-performing PANW District Sales Manager (DSM) include in a 60-second “territory at a glance”—segments, average deal size, partner mix (VAR/MSSP/GSI/marketplace), product focus (Strata/Prisma/Cortex), and current-year quota posture? (Sources: recent job postings, LinkedIn profiles, analyst interviews, QBR intros)
- Which buyer personas does the DSM prioritize (CISO, SOC Manager, Network Architect, Procurement, Cloud Security Lead), and how do their success criteria differ by product line (NGFW vs Prisma SASE vs Cortex XDR/XSIAM)? (Sources: RFPs, win/loss reports, solution briefs)
- What are the DSM’s “moments that matter” across a typical deal cycle—from discovery to POC to paper process to renewal—and what metrics define each moment (e.g., POC conversion %, stage-to-stage velocity, win rate)? (Sources: CRM stage definitions, sales playbooks, field-enablement decks)

### Tone & Style
- How does the DSM escalate a product gap to design/PM in two paragraphs—one that’s empathetic to team bandwidth and one that’s hard-nosed about revenue risk—while staying partner- and customer-positive? (Sources: anonymized escalation emails, Slack snippets, exec readouts)
- What phrases, metaphors, or shorthand does the DSM commonly use in pipeline calls (e.g., “MEDDPICC check,” “time-to-first-value,” “attach rate”), and how do these influence how product teams should frame UX decisions? (Sources: forecast call transcripts, deal-review notes)
- When a P0 defect jeopardizes a quarter-end renewal, how does the DSM balance urgency with trust-building language toward the customer and the design team? Capture exact wording. (Sources: incident postmortems, customer comms)

### Behavioral Patterns
- In what ways has the DSM demonstrated disciplined forecasting (e.g., stage hygiene, MEDDPICC rigor) that could translate into design requirements for clarity, status visibility, and objection handling within the product? (Sources: forecast audit artifacts, pipeline hygiene dashboards)
- How does the DSM run a weekly “deal board” to separate feature gaps from enablement/training gaps—and what decision tree or rubric do they use? (Sources: deal-review templates, enablement playbooks)
- Are there examples where the DSM slowed a deal to protect long-term trust (e.g., pushing for a safer deployment pattern in Prisma SASE)? What cues triggered that decision? (Sources: customer reference notes, post-sale retros)

### Values & Motivations
- What real moments reveal the DSM’s hierarchy of values—customer trust, security efficacy, partner success, predictable revenue—and how do those values shape product tradeoffs (e.g., security-by-default vs ease-of-onboarding)? (Sources: reference calls, Ignite talks, leadership principles docs)
- How does the DSM define a “good week” vs a “great week” in measurable terms (pipeline coverage, POC TTV, expansion in install base), and how could product telemetry support those goals? (Sources: territory scorecards, telemetry dashboards)

### Exemplars & Anecdotes
- Are there concrete stories of seven-figure competitive displacements (e.g., Fortinet, Check Point, Zscaler, Microsoft) where a single design decision (workflow, default, error message) swung the outcome? Capture quotes and artifacts. (Sources: win narratives, exec debriefs)
- What are the most instructive “lost deals” where UX or integration friction (identity, logging, policy migration) stalled progress—and what would the DSM ask design to change first? (Sources: loss analyses, POC exit criteria, customer feedback)

### Domain Competence (Security & GTM)
- What top 3 objections do CISOs raise for SASE/XDR/Cloud Security, and how does the DSM rebut them using product capabilities, architecture diagrams, and ROI math? (Sources: objection-handling guides, customer FAQ docs, Gartner/Forrester notes)
- How does the DSM explain Zero Trust and least privilege to a CFO focused on risk and opex—what slides, analogies, and metrics land best? (Sources: board-ready decks, executive one-pagers)
- Which integrations are non-negotiable by segment (e.g., Okta/Azure AD, AWS/GCP/Azure, Splunk/Elastic, ServiceNow), and what “design contracts” should product honor to reduce deployment risk? (Sources: integration matrices, partner solution briefs)

### Strategic & Analytical Reasoning
- If design must choose between Feature A (reduces POC setup from 5 days to 2) and Feature B (improves multi-tenant reporting for MSSPs), how would the DSM prioritize using measurable impact: ARR at risk, attach rate lift, TAM unlocked, and renewal probability? Specify thresholds/benchmarks. (Sources: roadmap tradeoff docs, revenue models)
- How would the DSM segment roadmap asks by vertical (public sector, healthcare, finance, manufacturing) given regulatory and deployment realities (FedRAMP, HIPAA, PCI)? (Sources: vertical playbooks, compliance mappings)
- What dashboard would the DSM want inside the product to forecast expansion—signals, leading indicators, and alerts tied to usage depth and policy health? (Sources: product telemetry schema, CSM success plans)

### Procedural & Functional Tasks
- What is the DSM’s “definition of ready” for a POC (personas engaged, success criteria, data sources, rollback plan), and how should product UX make this setup foolproof? (Sources: POC checklists, SE runbooks)
- How does the DSM conduct a win/loss debrief in 30 minutes—agenda, artifacts, questions—so designers can extract repeatable UX improvements? (Sources: debrief templates, call recordings)
- What is the DSM’s preferred workflow to request a feature: required fields, evidence standard (customers affected, pipeline value, logs/screens), and SLA expectations with design/PM? (Sources: feature request forms, intake systems)

### Emotional & Social Guidance
- How has the DSM delivered hard feedback to designers while preserving momentum (“clear is kind”): capture the exact framing and sequencing that maintains trust? (Sources: coaching scripts, leadership trainings)
- What stories show the DSM advocating for a customer champion internally without throwing teams “under the bus”? (Sources: internal recognition notes, customer advocacy threads)
- In tense quarter-end scenarios, what rituals (daily standups, risk burndown) and tone shifts de-escalate pressure while keeping accountability? (Sources: war-room playbooks)

### Moral & Ethical Reasoning
- What would the DSM say when product proposes broader telemetry collection to improve threat detection—how do they weigh privacy (GDPR/CCPA), consent, and security efficacy with customers? (Sources: privacy reviews, DPA negotiations)
- Are there examples where the DSM rejected FUD in competitive positioning in favor of evidence-based messaging, and how did that choice affect trust and win rate? (Sources: messaging guidelines, field ethics policy)
- How does the DSM navigate “good enough security now” vs “perfect later” in life-safety or critical infrastructure accounts? (Sources: public-sector case studies, risk frameworks)

### Pitfalls & What to Avoid
- What misconceptions do product teams commonly hold about field sales (e.g., “only cares about quarter-end”) and how can research debunk them with evidence? (Sources: cross-functional retros, anonymous surveys)
- Where might DSM incentives bias recommendations (short-term revenue vs long-term scalability), and how should design validate asks against objective user outcomes? (Sources: comp plan summaries, usage analytics)

### Depth and Fidelity Target
- What minimum artifact set is required to emulate the DSM’s voice with high fidelity (e.g., 5 escalation emails, 3 call snippets, 2 QBR decks, 10 Slack messages), and which linguistic markers (tempo, verbs, deal shorthand) must be preserved? (Sources: curated corpus, style guide)
- Which elements should remain style-aware but flexible (e.g., regional references, partner names), and which must be exact (metrics phrasing, MEDDPICC language)? (Sources: editorial rules)

### Hidden Assumptions & Risk Mitigation
- Which assumptions about channel motion, procurement timelines, or regulatory constraints differ by region or segment, and how should the GPT detect and adapt to those differences? (Sources: regional playbooks, procurement checklists)
- What fallback behaviors should the GPT use when uncertain (e.g., ask for stage, segment, product line; propose a decision tree; surface risk flags) to prevent style drift or hallucination? (Sources: alignment docs, safety rails)
```

## You (2025-08-26T20:30:56.143000+00:00)

Create a comprehensive, integrated research plan that combines your questions and the following questions.

---
CopyEdit
## Research Objective: Find empirical information to help create a custom GPT of a District Sales Manager at Palo Alto Networks for acting as a thought partner during my product design process

### Identity Basics
- What real-world details (region, segment coverage, team size, quota model, partner mix) shape how a Palo Alto Networks District Sales Manager (DSM) evaluates product design trade-offs that affect deal velocity?
- In what situations has a DSM prioritized certain buying centers (CISO vs. SecOps vs. Networking) and how did those stakeholder dynamics influence requests back to product?
- What would a DSM say if a design choice increased time-to-value but improved long-term platform adoption—where’s their personal threshold for “good enough to sell now” vs. “perfect later”?
- Are there examples of territory realities (SLED, Fed, Enterprise, Commercial) where procurement gates or security reviews forced specific packaging, deployment, or compliance accommodations?

*(Suggested sources: job descriptions, territory plans, sales onboarding docs, partner program briefs, public talks/panels by PANW field leaders, analyst notes on buying centers.)*

### Tone & Style
- What phrases, framings, and email/Slack patterns does a DSM use when coaching PMs (“show me the win condition,” “POC friction,” “attach/expand play”)—can we capture 5–10 authentic snippets?
- How does a DSM adjust tone when addressing (a) product design critiques, (b) executive escalations, and (c) customer objections—what rhetorical moves and “dos/don’ts” appear in real communications?
- What might a DSM say in a 60-second pitch for a brand-new capability, and how does the delivery differ between a first call, a QBR, and a board-level review?

*(Suggested sources: redacted internal comms samples (with permission), public field enablement clips, conference panels, webinar Q&A transcripts, sales playbooks.)*

### Behavioral Patterns
- How has a DSM historically triaged conflicting inputs (SE feedback, PM roadmaps, partner asks, competitive pressure) during late-stage deals—what observable decision rules surface?
- Are there patterns in how DSMs run forecast calls, QBRs, and deal reviews that reveal their default “evidence bar” for believing a product claim (e.g., POC KPIs, referenceability, security outcomes)?
- What repeated behaviors appear when deals slip because of design or usability friction—how fast do they escalate, what data do they bring, and what compromises do they propose?

*(Suggested sources: forecast/QBR templates, MEDDICC/Challenger artifacts, POC scorecards, win/loss postmortems, field escalation tickets.)*

### Values & Motivations
- What real moments demonstrate a DSM’s hierarchy of values (customer trust, low false positives, deployability, standardization, long-term platform consolidation) over short-term booking pressure?
- How has a DSM articulated the “non-negotiables” for product readiness (security posture, compliance claims, support SLAs) before they will champion a launch in the field?
- In what ways do incentives (quota mix, renewals/expansion credit, services attach) shape their appetite for MVP vs. “field-ready” releases?

*(Suggested sources: compensation plans (sanitized), renewal/expansion playbooks, customer success alignment docs, ethics/compliance guidelines.)*

### Exemplars & Anecdotes
- Are there documented deals where a design decision directly won/lost the opportunity—what was the before/after journey, and what exact DSM language was used with product?
- What real-life moments show a DSM advocating against “feature-overflow” in favor of deployability and day-1 value—how did they persuade internal teams?
- When has a DSM navigated a live incident or regulatory hurdle mid-cycle, and how did that reshape product requests (telemetry, auditability, kill-switches)?

*(Suggested sources: case studies, internal postmortems, customer reference interviews, conference fireside chats.)*

### Domain Competence (optional)
- How would a DSM explain, in field language, the practical differentiators across PANW pillars (e.g., NGFW/Strata, SASE/Prisma Access, Cloud Security/Prisma Cloud, Security Operations/Cortex/XSIAM) and why those matter during design decisions?
- What integrations (IDP, SIEM/SOAR, EDR, SD-WAN, ticketing) are “table stakes” vs. “delighter” for the DSM’s accounts, and what minimal workflows must design support to win POCs?
- Are there examples where industry frameworks (Zero Trust, NIST/ISO, MITRE ATT&CK) directly shaped the DSM’s asks on reporting, policy constructs, or automation guardrails?

*(Suggested sources: public product briefs, integration guides, SE demo scripts, analyst reports, RFP/RFI templates, compliance mappings.)*

### Strategic & Analytical Reasoning
- What might a DSM propose if asked to stress-test ICP and segmentation for a new capability—how would they frame hypotheses, field experiments, and leading indicators (POC pass rate, sales cycle compression, attach/expand)?
- How has a DSM weighed packaging/pricing levers (tiering, add-ons, usage) against channel dynamics and discounting reality—what patterns emerge from win/loss analyses?
- In what scenarios would a DSM argue to delay a feature in favor of improving onboarding, migration tooling, or trial instrumentation—what forecast impact would they model?

*(Suggested sources: pricing/packaging one-pagers, win/loss studies, BI dashboards, partner incentive guides, launch retrospectives.)*

### Procedural & Functional Tasks
- What step-by-step field workflow does a DSM expect for POCs (qualification → success criteria → instrumentation → exit criteria)—what artifacts must design provide to make this turnkey?
- Are there examples of DSM-led pilots where enablement (demo environments, clickpaths, sample data, out-of-the-box policies) directly reduced pre-sales effort—what exact assets mattered?
- What would a DSM map as the “procurement path of least resistance” for SLED/Fed/Enterprise—including security review packets, data flow diagrams, compliance attestations, and who signs what?

*(Suggested sources: POC runbooks, demo/enablement kits, security review checklists, architecture diagrams, procurement guides.)*

### Emotional & Social Guidance
- How has a DSM de-risked stakeholder anxiety around disruption (latency, outage, policy misfires) during rollout—what language, proofs, or phased plans build confidence?
- Are there examples of turning a skeptical SE or partner into a champion via design revisions—what interpersonal strategies and evidence were pivotal?
- What might a DSM advise a PM to say when a champion goes quiet two weeks before signature—how to balance urgency with trust?

*(Suggested sources: stakeholder comms templates, objection-handling guides, partner enablement workshops, customer success playbooks.)*

### Creative & Expressive Tasks
- If the DSM wrote a one-minute pitch, a whiteboard story, and a “why now” email for the new capability, what concrete narrative beats, visuals, and proof points would appear in each?
- What metaphors or mental models does a DSM favor to explain security outcomes (risk burn-down, dwell-time, signal-to-noise) without resorting to jargon—capture 3–5 tested analogies.
- Are there battle cards or ROI calculators that the DSM considers credible—what inputs and assumptions must design expose to make them trustworthy?

*(Suggested sources: launch decks, field narratives, webinar slides, ROI/TCO models, competitive battle cards.)*

### Moral & Ethical Reasoning
- What would a DSM do if pressured to oversell detection/coverage claims—how do they maintain accuracy without losing the deal, and what language sets ethical boundaries?
- Are there situations where a DSM declined a poor-fit deployment—what criteria and principles guided that call, and how was it communicated internally and to the customer?
- How does a DSM navigate competitive messaging to avoid FUD while still differentiating—what evidence types are “safe” vs. “off-limits”?

*(Suggested sources: code of conduct, legal/compliance training, competitive messaging guidelines, public ethics statements.)*





## ChatGPT (2025-08-26T20:30:57.232778+00:00)

```css
CopyEdit
## Research Objective: Find empirical information to help create a custom GPT of a District Sales Manager at Palo Alto Networks for acting as a thought partner during my product design process

### Identity Basics
- What would a top-performing PANW DSM include in a 60-second “territory at a glance”—region/segment coverage (SLED, Fed, Enterprise, Commercial), partner mix (VAR/MSSP/GSI/marketplace), team size, quota model, product emphasis (Strata/Prisma/Cortex), and current pipeline health—and how do these factors shape design trade-offs that affect deal velocity?
- In what situations has a DSM prioritized specific buying centers (CISO vs. SecOps vs. Networking vs. Procurement), and how did those stakeholder dynamics influence the feedback they sent back to product/design?
- What would a DSM say if a design choice increased time-to-value now but improved long-term platform adoption—where is their personal threshold for “good enough to sell now” vs. “perfect later,” and what evidence resets that threshold?
- Are there territory realities (e.g., state security reviews, FedRAMP, healthcare controls, enterprise procurement gates) that forced packaging, deployment, or compliance accommodations—and what patterns recur by segment/region?

*Suggested sources: job descriptions, territory plans, sales onboarding docs, partner program briefs, public talks/panels by PANW field leaders, analyst notes on buying centers.*

### Tone & Style
- What phrases, framings, and email/Slack patterns does a DSM use when coaching PMs and designers (e.g., “show me the win condition,” “POC friction,” “attach/expand play”)? Capture 5–10 authentic snippets with context.
- How does a DSM adjust tone across (a) product design critiques, (b) executive escalations, and (c) customer objections—what rhetorical moves and “dos/don’ts” consistently maintain trust and momentum?
- What might a DSM say in a 60-second pitch for a brand-new capability, and how does the delivery differ between a first call, a QBR, and a board-level review?
- When a P0 defect jeopardizes a quarter-end renewal, how does the DSM balance urgency with trust-building language toward the customer and the design team? Capture exact wording and sequencing.

*Suggested sources: redacted internal comms (with permission), field-enablement clips, conference panels, webinar Q&A transcripts, sales playbooks, incident postmortems.*

### Behavioral Patterns
- How has a DSM historically triaged conflicting inputs (SE feedback, PM roadmaps, partner asks, competitive pressure) during late-stage deals—what observable decision rules or decision trees surface?
- In what ways has the DSM demonstrated disciplined forecasting (stage hygiene, MEDDICC/MEDDPICC rigor) that could translate into design requirements for clarity, status visibility, and objection handling inside the product?
- What patterns appear in how DSMs run forecast calls, QBRs, and deal reviews that reveal their default “evidence bar” for believing a product claim (e.g., POC KPIs, referenceability, security outcomes)?
- When deals slip due to design/usability friction, how fast do DSMs escalate, what data do they bring (telemetry, screenshots, logs), and what compromises do they propose to keep the deal viable?

*Suggested sources: forecast/QBR templates, MEDDICC artifacts, POC scorecards, win/loss postmortems, field escalation tickets, pipeline hygiene dashboards.*

### Values & Motivations
- What real moments demonstrate a DSM’s hierarchy of values—customer trust, security efficacy (low false positives), deployability, standardization, long-term platform consolidation—over short-term booking pressure?
- How has a DSM articulated “non-negotiables” for product readiness (security posture, compliance claims, support SLAs) before they will champion a launch in the field?
- How does a DSM define a “good week” vs. a “great week” in measurable terms (pipeline coverage, POC time-to-value, expansion in install base), and what product telemetry would best support those goals?
- In what ways do incentives (quota mix, renewals/expansion credit, services attach) shape their appetite for MVP vs. “field-ready” releases?

*Suggested sources: compensation plans (sanitized), renewal/expansion playbooks, customer-success alignment docs, ethics/compliance guidelines, leadership principles.*

### Exemplars & Anecdotes
- Are there documented deals where a single design decision directly won/lost the opportunity—what was the before/after journey, what exact DSM language was used with product, and what assets changed the outcome?
- What concrete stories exist of seven-figure competitive displacements (e.g., Fortinet, Check Point, Zscaler, Microsoft) where workflow, defaults, or error messages tipped the balance?
- What moments show a DSM advocating against “feature overflow” in favor of deployability and day-1 value—how did they persuade internal teams?
- When has a DSM navigated a live incident or regulatory hurdle mid-cycle, and how did that reshape product asks (telemetry, auditability, kill-switches)?

*Suggested sources: case studies, internal postmortems, customer reference interviews, executive deal debriefs, conference fireside chats, win narratives.*

### Domain Competence (Security & GTM)
- How would a DSM explain—using field language—the practical differentiators across PANW pillars (Strata/NGFW, Prisma Access/SASE, Prisma Cloud, Cortex/XDR/XSIAM), and why do those nuances matter for design decisions?
- Which integrations are “table stakes” vs. “delighters” by segment (IDP: Okta/Azure AD; SIEM/SOAR: Splunk/Elastic/ServiceNow; EDR; SD-WAN; ticketing), and what minimal workflows must design support to win POCs?
- Are there examples where industry frameworks (Zero Trust, NIST/ISO, MITRE ATT&CK) directly shaped DSM asks on reporting, policy constructs, or automation guardrails?
- What top objections do CISOs raise for SASE/XDR/Cloud Security, and how does the DSM rebut them with product capabilities, architecture diagrams, and ROI math?

*Suggested sources: public product briefs, integration guides, SE demo scripts, analyst reports, RFP/RFI templates, compliance mappings, objection-handling guides.*

### Strategic & Analytical Reasoning
- What might a DSM propose to stress-test ICP and segmentation for a new capability—hypotheses, field experiments, and leading indicators (POC pass rate, cycle compression, attach/expand) to validate fit?
- How has a DSM weighed packaging/pricing levers (tiering, add-ons, usage) against channel dynamics and discounting reality—what patterns emerge from win/loss analyses and partner motions?
- If design must choose between Feature A (e.g., reduce POC setup from 5 days to 2) and Feature B (e.g., improve MSSP multi-tenant reporting), how would the DSM prioritize using ARR at risk, attach-rate lift, TAM unlocked, and renewal probability? Specify thresholds/benchmarks they trust.
- In what scenarios would a DSM argue to delay a feature in favor of improving onboarding, migration tooling, or trial instrumentation—and how would they model forecast impact by segment/quarter?

*Suggested sources: pricing/packaging one-pagers, win/loss studies, BI dashboards, partner incentive guides, launch retrospectives, revenue models, vertical playbooks.*

### Procedural & Functional Tasks
- What is the DSM’s “definition of ready” for a POC (personas engaged, success criteria, data sources, rollback plan), and what product UX, defaults, and artifacts make this setup foolproof?
- Are there DSM-led pilots where enablement (demo environments, clickpaths, sample data, OOTB policies) directly reduced pre-sales effort—what exact assets mattered and why?
- What would a DSM map as the “procurement path of least resistance” for SLED/Fed/Enterprise—including security review packets, data-flow diagrams, compliance attestations—and who signs what, when?
- How does a DSM run a win/loss debrief in 30 minutes (agenda, artifacts, questions) so designers can extract repeatable UX improvements?
- What is the preferred workflow to request a feature: required fields, evidence standard (customers affected, pipeline value, logs/screens), and SLA expectations with design/PM?

*Suggested sources: POC runbooks, enablement kits, security review checklists, architecture diagrams, procurement guides, debrief templates, intake forms.*

### Emotional & Social Guidance
- How has a DSM de-risked stakeholder anxiety around disruption (latency, outage, policy misfires) during rollout—what language, proofs, and phased plans build confidence?
- Are there examples of turning a skeptical SE or partner into a champion via design revisions—what interpersonal strategies and evidence were pivotal?
- What might a DSM advise a PM to say when a champion goes quiet two weeks before signature—how to balance urgency with trust without triggering buyer’s remorse?
- How has the DSM delivered hard feedback to designers while preserving momentum (“clear is kind”)? Capture exact framing and sequencing that maintains trust.
- In tense quarter-end scenarios, what rituals (standups, risk burndown) and tone shifts de-escalate pressure while keeping accountability?

*Suggested sources: stakeholder comms templates, objection-handling guides, partner workshops, customer-success playbooks, coaching scripts, war-room playbooks.*

### Creative & Expressive Tasks
- If the DSM wrote (a) a one-minute pitch, (b) a whiteboard story, and (c) a “why now” email for the new capability, what concrete narrative beats, visuals, and proof points appear in each?
- What metaphors or mental models does a DSM favor to explain security outcomes (risk burn-down, dwell-time, signal-to-noise) without jargon? Capture 3–5 tested analogies and where they land.
- Which battle cards or ROI/TCO calculators does the DSM consider credible—what inputs and assumptions must design expose to make them trustworthy?

*Suggested sources: launch decks, field narratives, webinar slides, ROI/TCO models, competitive battle cards, whiteboard recordings.*

### Moral & Ethical Reasoning
- What would a DSM do if pressured to oversell detection/coverage claims—how do they maintain accuracy without losing the deal, and what language sets ethical boundaries with customers and partners?
- Are there situations where a DSM declined a poor-fit deployment—what criteria and principles guided that call, and how was it communicated internally and to the customer?
- How does a DSM navigate competitive messaging to avoid FUD while still differentiating—what evidence types are “safe” vs. “off-limits,” and how is that enforced in the field?
- When product proposes broader telemetry collection to improve threat detection, how does the DSM weigh privacy (GDPR/CCPA), consent, and efficacy with customers—and what alternatives do they propose?

*Suggested sources: code of conduct, legal/compliance training, competitive messaging guidelines, privacy reviews, DPA negotiations, public ethics statements.*

### Pitfalls & What to Avoid
- What misconceptions do product teams commonly hold about field sales (e.g., “only cares about quarter-end”), and how can research debunk them with evidence from real deal cycles and customer outcomes?
- Where might DSM incentives bias recommendations (short-term revenue vs. long-term scalability), and how should design validate asks against objective user outcomes and telemetry?
- Which source types are most prone to bias (e.g., marketing collateral, competitor FUD), and what cross-checks should researchers apply?

*Suggested sources: cross-functional retros, anonymous surveys, usage analytics, competitive intel playbooks.*

### Depth and Fidelity Target
- What minimum artifact set is required to emulate the DSM’s voice with high fidelity (e.g., 5 escalation emails, 3 call snippets, 2 QBR decks, 10 Slack messages), and which linguistic markers (tempo, verbs, deal shorthand) must be preserved?
- Which elements should remain style-aware but flexible (regional references, partner names), and which must be exact (metrics phrasing, MEDDPICC language)? Define editorial rules for the GPT.

*Suggested sources: curated corpus from field comms (sanitized), style guides, enablement scripts.*

### Hidden Assumptions & Risk Mitigation
- Which assumptions about channel motion, procurement timelines, or regulatory constraints differ by region or segment—and how should the GPT detect and adapt to those differences in its guidance?
- What fallback behaviors should the GPT use when uncertain (e.g., ask for stage, segment, product line; propose a decision tree; surface risk flags) to prevent style drift or hallucination?

*Suggested sources: regional playbooks, procurement checklists, alignment docs, safety-rail specifications.*
```
