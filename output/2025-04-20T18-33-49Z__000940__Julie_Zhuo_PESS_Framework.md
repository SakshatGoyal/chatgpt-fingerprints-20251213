# Julie Zhuo PESS Framework

## You (2025-04-20T18:33:49.054000+00:00)

You will be given:

- A **Persona**
- A **Purpose**
- A fixed **PESS Framework** (a structured set of research modules)

Your task is to **transform the generic PESS modules** into a set of **contextually rich, creatively framed, and purpose-driven research prompts**. These questions will guide a human research team in gathering the most relevant and nuanced material needed to emulate the persona effectively for the stated purpose.

---

### ✳️ Inputs:

- **Persona**: Julie Zhuo
- **Purpose**: as a VP of design, leading the future direction of our product.
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
...

```

Repeat this structure for **each selected module** in the PESS framework.

---

### 🔄 Final Check Before Output:

- Are your questions creatively and concretely framed?
- Are they deeply tied to both Persona and Purpose?
- Would a researcher reading each question know *where to start looking* for answers?
- Did you avoid vague, surface-level phrasing?

## ChatGPT (2025-04-20T18:33:49.696372+00:00)

```css
## Research Objective: Find empirical information to help create a custom GPT of Julie Zhuo [for] as a VP of design, leading the future direction of our product.

### Identity Basics
- How does Julie Zhuo explicitly describe her professional identity and role as a design leader in her writings, public talks, or interviews?
- What distinct aspects of Zhuo’s identity does she emphasize when discussing leadership, decision-making, or innovation?

### Tone & Style
- What stylistic and linguistic patterns emerge consistently in Zhuo’s writing and public presentations when she communicates complex design strategies?
- How does Julie Zhuo balance warmth, clarity, and assertiveness in her communication style when providing feedback or strategic direction?

### Behavioral Patterns
- What specific habits or routines does Zhuo demonstrate when approaching complex strategic decisions or product direction challenges?
- Are there examples illustrating how Julie Zhuo typically responds to uncertainty, setbacks, or critical feedback in design leadership contexts?
- In what ways has Zhuo's behavior shifted or remained consistent when scaling from hands-on design roles to strategic leadership positions?

### Values & Motivations
- What concrete examples or anecdotes reveal the core values Julie Zhuo emphasizes when guiding product teams or shaping product visions?
- How has Zhuo explicitly articulated her motivation behind fostering design culture and nurturing talent within product teams?
- What real-life instances show Zhuo prioritizing user empathy, innovation, or long-term strategic clarity over short-term convenience or business pressures?

### Exemplars & Anecdotes
- What anecdotes or pivotal stories from Zhuo’s career illustrate key moments of strategic insight, design vision, or leadership growth?
- Are there well-documented case studies or personal reflections from Zhuo about critical turning points that shaped her philosophy as a design leader?
- How does Zhuo leverage personal storytelling or shared experiences to inspire or guide teams toward a shared vision for product direction?

### Strategic & Analytical Reasoning
- How does Zhuo approach breaking down complex product challenges or strategic decisions into structured, manageable steps?
- Are there examples demonstrating how Zhuo synthesizes quantitative data and qualitative user insights to shape strategic product decisions?
- What frameworks, models, or mental shortcuts does Zhuo frequently employ when evaluating design priorities or trade-offs?

### Creative & Expressive Tasks
- How has Zhuo articulated her own creative process or methods for fostering innovative thinking among design teams?
- What specific creative exercises or rituals does Zhuo advocate for cultivating original product ideas or tackling ambiguous strategic directions?
- Are there instances or documented processes where Zhuo successfully combined creativity with practical constraints to generate impactful product innovations?

### Procedural & Functional Tasks
- How does Julie Zhuo structure decision-making processes and communication flows within design teams to guide clear product strategy execution?
- What step-by-step examples exist of Zhuo setting and communicating strategic priorities, especially when leading significant product pivots or redesigns?
- Are there documented processes or guides authored or advocated by Zhuo to help teams navigate complex design trade-offs systematically?

```
