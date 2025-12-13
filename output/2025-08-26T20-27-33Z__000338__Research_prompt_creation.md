# Research prompt creation

## You (2025-08-26T20:27:33.014000+00:00)

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

## ChatGPT (2025-08-26T20:27:38.722599+00:00)

{"content_type": "thoughts", "thoughts": [], "source_analysis_msg_id": "99cb95f5-5a9a-4607-85a3-55e444eef624"}

## ChatGPT (2025-08-26T20:28:35.594945+00:00)

{"content_type": "reasoning_recap", "content": "Thought for 56s"}

## ChatGPT (2025-08-26T20:27:36.140660+00:00)

```css
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
```

