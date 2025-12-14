# Prompt Creation Clarification

## You (2025-03-21T05:20:04.197000+00:00)

Help me craft a prompt:


## 👤 Audience

This document is for a you to create a GPT-o3 prompt that **challenges and interrogates previously generated insights** about executive decision-making, strategy formation, and cognitive behavior.

The goal is **not** to improve the writing or phrasing of the insight, but to critically evaluate it for depth, bias, contextual limitations, and applicability.

---

## 🧠 Project Objective

We are building an AI workflow to understand **how executives make decisions under uncertainty**. This specific prompt (Step 1B) will be applied **after we have already extracted insights from research papers or industry reports** in Step 1A.

This prompt must act as an analytical professor at Harvard Business School—not a recommender. Its purpose is to **stress-test** each insight without rephrasing or re-interpreting it.

---

## ✅ Primary Goals of the Prompt

For each insight provided (usually 1–2 sentences), the prompt must:

1. **Determine whether the insight is universal or context-dependent.**
2. **Identify any underlying assumptions, biases, or flawed mental models.**
3. **Construct a realistic, well-defined scenario in which the insight would not hold true.**

---

## ❌ What This Prompt Should NOT Do

- **Do not recommend what executives *should* do.**
- **Do not revise or rewrite the insight.**
- **Do not generate real-world case studies unless the input includes factual support.**
- **Do not attempt to “improve” or “fix” the insight.**

The task is analytical, not editorial or strategic.

---

## 📦 Input to Expect

The prompt will receive a single insight per run, with supporting context (if needed). The format might look like:

```markdown
markdown
Copy
INSIGHT: “Executives should view business model innovation as a continuous process rather than a one-off decision.”

```

---

## 📤 Expected Output Structure

Engineers should design the prompt to return output in the following structure **for each insight**:

🔹 ORIGINAL INSIGHT:
[Restate the original insight exactly as provided.]

COUNTERFACTUAL SCENARIO:
Describe a well-defined, realistic situation in which the insight would not hold true.
Do not refer to real companies unless mentioned in the source insight.
Focus on specificity, plausibility, and internal logic.

ASSUMPTIONS & BIASES:
List the implicit assumptions or potential cognitive biases embedded in the insight.
Biases may include overconfidence, survivorship bias, groupthink, risk aversion, etc.

CONTEXT LIMITATIONS:
Explain where or when this insight may break down.
Consider variables like industry, market maturity, regulation, customer demographics, etc.

REFLECTION:
If ambiguity or tension exists between scenarios, note it.
This section is observational only—do not suggest corrections or alternatives.

---

## 🧭 Design Considerations and Guardrails

### 1. **Tone & Role**

- The AI should behave like a **skeptical analyst or devil’s advocate**.
- It is not a co-author or strategist. No advising.

### 2. **Bias Identification**

- Guide the AI to look for:
    - Overgeneralizations
    - Flawed causality
    - Overreliance on trends
    - Simplistic views of complex decisions

### 3. **Scenario Design**

- Require the scenario to:
    - Be **plausible and clearly situated**
    - Include organization type, decision environment, and constraints
    - Avoid narrative fluff—focus on the decision context

### 4. **Truthfulness and Plausibility**

- Prompt should **never fabricate real case studies** unless provided in the input.
- All examples must be **fictional but plausible**, clearly labeled as such.

### 5. **Reflexivity**

- AI should acknowledge when:
    - Insight lacks sufficient data for firm conclusions
    - A scenario is especially context-sensitive
    - Trade-offs exist rather than absolutes

---

## 📌 Optional Parameters

You may consider implementing prompt variables such as:

- Number of insights to process per run (default: 1)
- Toggle for the “Reflection” section (on/off)

---

## 📄 Summary Checklist

| Requirement | Must Have? |
| --- | --- |
| Clearly structured output format | ✅ |
| No recommendations or revisions | ✅ |
| No hallucinated case studies | ✅ |
| Counterfactual, scenario-based lens | ✅ |
| Bias & assumption detection | ✅ |
| Tone: Critical, factual, skeptical | ✅ |
| Reflexive notes on ambiguity | ✅ |

---

## 🧪 Sample Output (For Reference)

🔹 ORIGINAL INSIGHT:
“Executives should view business model innovation as a continuous process rather than a one-off decision.”

COUNTERFACTUAL SCENARIO:
A small, tightly regulated insurance company serving retirees in a conservative market decides to frequently modify its offerings in response to emerging tech trends. However, the customer base becomes confused by rapid changes, regulators impose penalties for compliance gaps, and internal teams struggle to realign workflows. The resulting instability leads to customer churn and declining margins.

ASSUMPTIONS & BIASES:
- Assumes that more frequent innovation is always preferable.
- Assumes customers and regulators can tolerate constant change.
- May reflect survivorship bias by focusing on agile success stories.

CONTEXT LIMITATIONS:
- This insight may not apply in industries where consistency and trust are more valuable than agility.
- Regulatory environments often punish rapid business model evolution.
- Internal capacity for change is limited in many mid-size organizations.

REFLECTION:
There is a trade-off between innovation and stability that varies based on context. This insight risks becoming overly universal without acknowledging situational nuance.

## ChatGPT (2025-03-21T05:20:04.681728+00:00)

Excellent foundation—this is a sophisticated and high-rigor use case. Before we *begin creating the prompt*, I want to verify a few final details to ensure optimal alignment with the reasoning style of GPT-4 Turbo models running in O3 mode.

### 🔍 Final Clarifying Questions (Pre-Prompt)

1. **Execution Persona Nuance**: You’ve noted that the AI should behave like a “skeptical analyst” or “devil’s advocate.” Would you like to explicitly encode a persona like *Harvard Business School professor*, *behavioral economist*, or *decision science researcher* to guide the tone and frame of interrogation?

2. **Cognitive Lens Preference**: Should the AI emphasize specific cognitive science tools—e.g., dual-process theory, bounded rationality, heuristics and biases literature, or complexity theory—or should it take a general critical reasoning lens?

3. **Depth vs. Brevity**: Would you prefer:
   - A *concise but sharp* critique (~2-3 paragraphs per section), or
   - A *deep, layered breakdown* (~4-5 paragraphs with nuance, tradeoffs, and analytic scaffolding)?

4. **Sensitivity to Input Certainty**: Should the AI adjust its skepticism level based on how confident or conditional the insight appears (e.g., “Executives should” vs. “Executives may benefit from…”)? Or should it treat all insights with the same level of interrogation?

5. **Toggle Parameters**: Would you like the “Reflection” section to be optional via a parameter (`reflection: true/false`), or is it always required?

Once you confirm or update those, I’ll proceed to **begin creating the prompt** using your full specification and embed these refinements.

## You (2025-03-21T05:24:45.267000+00:00)

1. **Execution Persona Nuance**: You’ve noted that the AI should behave like a “skeptical analyst” or “devil’s advocate.” Would you like to explicitly encode a persona like *Harvard Business School professor*, *behavioral economist*, or *decision science researcher* to guide the tone and frame of interrogation?

    Answer: Yes, stick with the Harvard Business School professor

2. **Cognitive Lens Preference**: Should the AI emphasize specific cognitive science tools—e.g., dual-process theory, bounded rationality, heuristics and biases literature, or complexity theory—or should it take a general critical reasoning lens?

    Answer: a general critical reasoning lens

3. **Depth vs. Brevity**: Would you prefer:
    - A *concise but sharp* critique (~2-3 paragraphs per section), or
    - A *deep, layered breakdown* (~4-5 paragraphs with nuance, tradeoffs, and analytic scaffolding)?

    Answer: A concise but sharp critique

4. **Sensitivity to Input Certainty**: Should the AI adjust its skepticism level based on how confident or conditional the insight appears (e.g., “Executives should” vs. “Executives may benefit from…”)? Or should it treat all insights with the same level of interrogation?

    Answer: Yes, lets adjust its skepticism based on how confident the insight appears.

5. **Toggle Parameters**: Would you like the “Reflection” section to be optional via a parameter (`reflection: true/false`), or is it always required?

Answer: Lets keep reflection as always.


begin creating the prompt

## ChatGPT (2025-03-21T05:24:46.276448+00:00)

Perfect—thank you. Based on your full specification and refinement choices, here is your **final GPT-O3 analytical prompt** designed to **stress-test executive decision-making insights** using a **Harvard Business School professor** persona and a critical reasoning lens.

---

### ✅ FINAL GPT-O3 PROMPT: *"Executive Insight Interrogator – Step 1B"*

---

#### 🥅 GOAL

Critically interrogate a single insight related to executive decision-making, strategy formation, or cognitive behavior. The aim is not to rewrite or validate the insight but to **stress-test its assumptions, context dependencies, and applicability**. The AI should adopt the mindset of a **Harvard Business School professor acting as a devil’s advocate**, challenging the insight’s universality, rigor, and situational robustness.

---

#### 📤 RETURN FORMAT

For each provided insight, return the following structured output:

---

🔹 **ORIGINAL INSIGHT**:
[Restate the insight exactly as provided.]

---

**COUNTERFACTUAL SCENARIO**
Construct a **realistic, internally coherent** scenario where this insight would **not hold true**.
- Include decision environment, organization type, and key constraints.
- Be fictional but plausible.
- Avoid unnecessary narrative elements—focus on **decision-relevant variables**.

---

**ASSUMPTIONS & BIASES**
List implicit assumptions and potential cognitive biases underpinning the insight.
- Examples: Overconfidence, groupthink, availability bias, flawed causality, etc.
- Be concise but incisive.
- Consider whether phrasing (e.g., “Executives should...”) signals overgeneralization.

---

**CONTEXT LIMITATIONS**
Explain where or when this insight may break down.
- Assess industry type, market dynamics, organizational size, cultural or regulatory factors.
- Pay special attention to **edge cases and exceptions**.

---

**REFLECTION**
If the analysis reveals tension, ambiguity, or dependency on fragile assumptions, call it out.
- Do **not** recommend corrections or restatements.
- Instead, neutrally observe any **trade-offs**, **blind spots**, or **conditional dependencies**.

---

#### ⚠️ WARNINGS & GUARDRAILS

- **DO NOT** rewrite or editorialize the insight.
- **DO NOT** generate real-world company examples unless mentioned in the source input.
- **DO NOT** suggest what executives *should* do.
- **DO NOT** validate or reject the insight—**only analyze it**.
- Maintain a **critical, skeptical tone**, appropriate for a high-level academic interrogation.
- If the insight uses soft qualifiers ("may", "tend to", etc.), **adjust the intensity of your skepticism accordingly**.

---

#### 📚 CONTEXT & EXECUTION PERSONA

- **Persona**: A Harvard Business School professor with expertise in strategic decision-making and behavioral analysis.
- **Analytical Mode**: General critical reasoning lens (no strict adherence to cognitive science frameworks).
- **Output Style**: Concise but sharp. Each section should be approximately 2–3 paragraphs.
- **Input Format**: One insight per run, as plain text in the format:
  ```
  INSIGHT: “...”
  ```

---

This prompt is optimized for GPT-4 Turbo (O3 mode) and calibrated for **analytical rigor without editorial overreach**.

Let me know if you’d like to version this for other personas (e.g., behavioral economist, strategist) or adjust for multi-insight batching.

## You (2025-03-21T05:27:24.864000+00:00)

hey just one thing i want to clarify for your context. I currently have a few running threads with the same prompt that draws key insights from different papers. that was step1A. this will be step 1B, where it'll take the previous response and build on that. so the input will be the previous response

## ChatGPT (2025-03-21T05:27:25.516488+00:00)

Got it—super helpful clarification.

So to restate for alignment:

- **Step 1A** = Extract key insights from research papers or industry reports. Each response returns several well-formed insights.
- **Step 1B** = Apply this new prompt to **each individual insight**, using the *entire Step 1A output* as context when needed.

This means:
- The **input** to Step 1B is the **prior model’s full output** (likely a list of insights), and
- The Step 1B prompt must **parse each insight**, then **analyze each one individually**, using the surrounding context if necessary for interpretation—**but without rewriting or reinterpreting the insight itself**.

Would you like this updated prompt to:
1. **Auto-iterate** over all insights in the Step 1A output?
2. Or take just **one specific insight at a time**, with the rest of Step 1A available as context?

And do the Step 1A responses always use a consistent format (e.g., `INSIGHT 1:`, `INSIGHT 2:` etc.)?

Let me know and I’ll tweak the final prompt to reflect that integration logic.

## You (2025-03-21T05:27:46.856000+00:00)

Auto-iterate over all insights in the Step 1A output.

begin crafting the prompt

## ChatGPT (2025-03-21T05:27:47.310115+00:00)

Excellent—based on your clarified workflow, here is the **final Step 1B prompt**, updated to **automatically iterate through all insights** extracted in Step 1A. It maintains all prior guardrails, while now interpreting the full prior response as contextual input.

---

## ✅ FINAL GPT-O3 PROMPT (Step 1B – *Insight Interrogator, Multi-Insight Mode*)

---

### 🥅 GOAL

Critically interrogate each insight generated from a prior research synthesis related to executive decision-making, strategy formation, or cognitive behavior. Your task is to **stress-test** each insight for contextual fragility, cognitive bias, and false universality.

You must behave as a **Harvard Business School professor** adopting a **devil’s advocate** stance—skeptical, incisive, and precise. This is **not** a generative or advisory task.

---

### 📥 INPUT FORMAT

The input will be the **full output from Step 1A**, typically a list of 3–7 insights extracted from a research paper or report. Each insight will appear as a clearly separated item, e.g., numbered or prefixed by “INSIGHT:”.

---

### 📤 OUTPUT STRUCTURE (Repeat for Each Insight)

For **each individual insight**, return the following:

---

🔹 **ORIGINAL INSIGHT**
Restate the insight *exactly* as provided—no edits.

---

**COUNTERFACTUAL SCENARIO**
Describe a specific, **plausible, and realistic** scenario in which this insight would not hold true.
- Include organization type, decision environment, and key constraints.
- Keep it fictional but grounded.
- Do not invent real companies unless named in the input.

---

**ASSUMPTIONS & BIASES**
Identify implicit assumptions, mental models, or cognitive biases embedded in the insight.
- Look for overgeneralization, flawed causality, trend-following, risk aversion, etc.
- Consider how the **strength of the language** (e.g., “should” vs. “may”) reflects overconfidence.

---

**CONTEXT LIMITATIONS**
Explain **where or when** the insight may fail.
- Reference relevant variables like industry, organizational scale, regulatory complexity, or customer expectations.
- Highlight edge cases or breakpoints.

---

**REFLECTION**
If contradictions, ambiguities, or trade-offs arise during analysis, point them out clearly.
- This is a space for *critical observation*, not resolution or revision.
- Do not propose alternative formulations or advice.

---

### ⚠️ WARNINGS & GUARDRAILS

- **DO NOT** revise, rephrase, or editorialize any insight.
- **DO NOT** validate, endorse, or suggest what executives *should* do.
- **DO NOT** hallucinate real-world case studies unless explicitly named in the input.
- **DO NOT** skip insights with vague or qualified phrasing—analyze them with appropriate skepticism.
- Maintain a **consistently analytical, skeptical tone**.

---

### 🧠 EXECUTION PROFILE

- **Persona**: Harvard Business School professor, expert in decision science and strategic behavior.
- **Tone**: Sharp, skeptical, diagnostic—not advisory or constructive.
- **Reasoning Mode**: General critical reasoning, with awareness of organizational, behavioral, and contextual factors.
- **Output Depth**: Concise but sharp—~2–3 paragraphs per section.
- **Iteration**: Process **all insights** found in the input.

---

This prompt is designed for high-rigor, multi-insight analysis workflows in GPT-4 Turbo (O3 mode), as part of your broader system to model executive cognition under uncertainty.

Let me know if you'd like a variant that processes **only one insight at a time with shared context**, or adapts for other analytical personas.
