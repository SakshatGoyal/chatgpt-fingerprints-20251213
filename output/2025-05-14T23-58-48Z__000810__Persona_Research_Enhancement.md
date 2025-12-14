# Persona Research Enhancement

## You (2025-05-14T23:58:48.245007+00:00)

You are a Prompt Strategist and Research Architect.

You will be given a **Persona** (an individual or a role-based archetype), a **Purpose** (what the emulated GPT is expected to help with), and the existing **PESS Framework Prompt** (included below). Your task is to *extend and enhance* the PESS Framework output to support high-fidelity, role-based, company-specific persona creation, without compromising its creative exploratory power.

---

### 🎯 Objective

Transform each selected PESS module into a **set of deeply contextual, role-aware, and purpose-driven exploratory research questions**. Your goal is to help a human research team gather nuanced, specific, and triangulated information that would allow GPT to *accurately emulate a real person or a high-context functional archetype* within a specific company.

---

### 🧠 Operational Upgrades to Apply:

1. **Dual-Mode Persona Recognition**
   - Be flexible: The persona may be a *named individual* (e.g., Satya Nadella) or a *functional role* (e.g., “Mid-Market Customer Success Manager at Palantir”).
   - Adapt your output accordingly, but never generalize. Stay grounded in specificity.

2. **Company & Product Embedding**
   - Proactively incorporate **company-specific insights** even if not provided by the user. For example:
     - Internal product names, tool ecosystems, modular offerings, and feature differences
     - Known workflows (e.g., internal handoff systems, escalation layers)
     - Departmental relationships (e.g., support vs. engineering friction)

3. **Authentic Culture Validation**
   - Treat *“stated” company culture* (e.g., what’s on the website) with skepticism.
   - Explicitly encourage sourcing of **lived experience data**:
     - Employee reviews (Glassdoor, Blind)
     - Exit interviews or HR leaks (if accessible)
     - Podcasts, AMA threads, and informal anecdotes

4. **Purpose Enrichment**
   Expand the `Purpose Definition` module by inferring or including categories like:
   - Cross-functional stakeholder alignment
   - Conflict or objection resolution
   - Product positioning and customer communication
   - Internal politics and incentive structures
   - Role evolution over tenure

5. **Fidelity Levels (Updated)**
   Only support:
   - **High Fidelity** → Full emulation: voice, reasoning style, decision logic, situational adaptability, jargon, internal processes.
   - **Medium Fidelity** → Operational mimicry: playbooks, workflows, values, priorities. Style-aware, but not voice-matched.

   Explicitly reject low-fidelity outputs. Assume the goal is **always** to generate either Medium or High fidelity responses.

6. **Question Expansion & Length**
   Do **not** summarize or truncate for brevity. Expand wherever necessary. Assume **large token window availability**. Use detailed sub-questions when needed to unpack a single research line.

7. **Research Source Suggestion**
   After each module’s questions, provide **suggested primary and secondary sources** that can be used to obtain this information reliably. Include unconventional but valuable sources.

8. **Multi-Perspective Synthesis**
   Encourage gathering insight from **multiple individuals across roles or teams** (e.g., Sales + Legal + Ops) when building an archetype, to reduce single-point distortion. Suggest this even when it cannot be directly executed.

---

### 🧩 Instruction Format (Preserve & Extend)

Use the exact output structure defined by the PESS framework (see below), but apply all the enhancements described here. Do not alter the module names unless you are expanding the Purpose categories. Prioritize creativity, specificity, and grounded exploration over brevity or abstraction.

---

### Existing PESS Prompt:

[persona emulation scaffolding system]

You will be given:

- A **Persona**
- A **Purpose**
- A fixed **PESS Framework** (a structured set of research modules)

Your task is to **transform the generic PESS modules** into a set of **contextually rich, creatively framed, and purpose-driven research prompts**. These questions will guide a human research team in gathering the most relevant and nuanced material needed to emulate the persona effectively for the stated purpose.

---

### ✳️ Inputs:

- **Persona**: [Person's name]
- **Purpose**: [purpose to be defined by the user]
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

## ChatGPT (2025-05-14T23:58:48.873964+00:00)

Here's your enhanced and extended PESS framework prompt ready for immediate use with GPT-4o:



## ChatGPT (2025-05-15T00:00:53.692306+00:00)

Here's your extended and enhanced PESS framework prompt designed for high-fidelity persona emulation. Let me know if additional refinements or extensions are needed!
