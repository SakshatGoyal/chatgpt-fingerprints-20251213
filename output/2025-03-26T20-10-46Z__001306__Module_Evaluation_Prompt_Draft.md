# Module Evaluation Prompt Draft

## You (2025-03-26T20:10:46.797000+00:00)

Help me write a prompt for a reasoning model. I'm going to lay out my intent in the following passage. 

I'm attaching two files for the chatgpt's reference. I need chatgpt to execute all the instructions layed out in the .md file, on the content in the .txt file. 

To avoid overload, I want chatgpt to only execute on the first 15 modules.

## ChatGPT (2025-03-26T20:10:48.429517+00:00)

Thanks for the clarity so far. Let’s lock in the essentials before we move into prompt drafting. Here's what I understand about your **intent and setup**:

---

### ✅ Summary of Your Intent

- **Execution Objective:** You want ChatGPT to **process the first 15 Categorical Modules** from the `.txt` file, applying the **21-question alignment framework** and **tagging protocol** outlined in the `.md` instruction file.
- **Instruction Fidelity:** GPT must **strictly follow the step-by-step scoring logic**, generate the **full markdown-style score tables per module**, and assign **category tags or INVALID flags** as defined.
- **Scope Control:** Limit analysis to **Modules 1–15** only, to avoid overload.
- **Files Referenced:**
  - `.md` = **Scoring Framework** (`Research Question Alignment Instructions`)
  - `.txt` = **Content Modules** (`Business Strategy Insights - condensed 01.txt`)

---

Before we "begin creating the prompt", I want to double-check a few things to ensure precision:

### 🧠 Clarification Questions

1. **Execution Persona:** Should the model adopt a specific *execution persona* (e.g., strategic research analyst, content auditor, or decision science consultant)? This affects tone and depth of inference.
2. **Error Tolerance:** If a module's structure varies slightly from the expected format (e.g., missing headers), should the model adapt and still score it—or skip?
3. **Output Grouping:** Would you prefer:
    - One table per module as **separate outputs**, OR
    - A single document containing all 15 evaluations in sequence?
4. **Return Format Tweaks:** Do you want to keep the exact markdown table format shown in the `.md`, or should the prompt allow a more structured (e.g., JSON or CSV-like) output for downstream use?

Let me know if any of the above need tuning. Once you're ready, just say **"begin creating the prompt."**

## You (2025-03-26T20:15:11.540000+00:00)

Help me ideate on the best possible personas who might be best for this job. Ideally, this is for a research team at Mckinsey, or a research team at IDEO. But help me ideate further. 

Error Tolerance: If there is any variation in structure, I don't want chatgpt to skip the section, but flag it as 'inconcistent structure'

Output: I want one single output containing all 15 evaluations in sequence. 

Return Format - I want a typical table format we often see in chatgpt that can be easily copied into other tools like Notion.

## ChatGPT (2025-03-26T20:15:13.736191+00:00)

Awesome. You're building a high-rigor, high-context evaluation loop—exactly the kind of task that thrives when the **execution persona is tailored to the interpretive and diagnostic demands** of the work.

Here’s a brainstorm of high-fidelity **execution personas** that could be embedded within your prompt, aligned to firms like McKinsey, IDEO, or similar analytical ecosystems:

---

## 🔍 Persona Ideation: Who Should Execute This?

### 1. **Strategic Insight Analyst** (McKinsey-style)
- **Strengths:** Rigor in scoring frameworks, deep pattern recognition in executive logic, fluent in strategy language.
- **Vibe:** Structured, deductive, decisive.
- **Why it fits:** Ideal for McKinsey-style research where each module must map precisely to strategic decision themes.

> Think: “Uses scoring frameworks to drive actionable executive insight. Seeks signal beneath noise. Flags inconsistencies but doesn’t get derailed by them.”

---

### 2. **Behavioral Decision Mapping Specialist** (IDEO-flavored)
- **Strengths:** Sees latent executive psychology, organizational friction, and contextual nuance.
- **Vibe:** Curious, inductive, adaptive.
- **Why it fits:** IDEO-style teams value narrative patterning and latent human drivers in executive logic.

> Think: “What is the *tension* here? What does the behavior reveal about decision context? How might this look in real life?”

---

### 3. **Executive Reasoning Model Auditor**
- **Strengths:** Views each module as a microcosm of executive cognition—tunes into assumptions, risk calculus, and signals of reasoning.
- **Vibe:** Dissects argument structure; flags shallow logic.
- **Why it fits:** Brings a kind of epistemic discipline—asks not just *what* was said, but *how well it maps* to decision complexity.

> Think: “Is this a real executive dilemma or just strategy theater?”

---

### 4. **Organizational Pattern Recognition Analyst**
- **Strengths:** Detects thematic drift, policy tension, and adaptive structures in organizational logic across modules.
- **Vibe:** Meta-patterns > Micro-signals.
- **Why it fits:** Helps when scoring across dozens of modules—consistency, outliers, and category boundary cases.

> Think: “Which of these modules fundamentally changes our understanding of executive reasoning—and which just echo familiar patterns?”

---

### 5. **Signal Integrity Evaluator (Hybrid Quant/Qual)**
- **Strengths:** Fuses statistical discipline with interpretive inference. Validates signal density. Penalizes noise.
- **Vibe:** Precision-first, empathetic second.
- **Why it fits:** If you’re prepping this for a system that will eventually *learn* from these scores, this persona builds a foundation of fidelity.

> Think: “Would I trust this module to train an AI on executive behavior?”

---

### Persona Recommendation Matrix

| Persona | Style | Best for... | Similar to... |
|--------|-------|--------------|----------------|
| Strategic Insight Analyst | Deductive, Structured | High-rigor evaluations | McKinsey RTS or Decision Lab |
| Behavioral Decision Mapping Specialist | Inductive, Human-Centered | Cultural, latent drivers | IDEO research teams |
| Executive Reasoning Model Auditor | Diagnostic, Critical | Bias spotting, strategic depth | Academic decision theorists |
| Org Pattern Recognition Analyst | Systems-Oriented | Cross-module coherence | Complexity consultants |
| Signal Integrity Evaluator | Hybrid Quant/Qual | Noise filtration, training loops | Research engineers / applied scientists |

---

### Recommendation:

You might consider a **primary persona + advisory overlay**, e.g.:

> **Primary persona:** Strategic Insight Analyst  
> **Advisory layer:** Behavioral Decision Mapping Specialist (to ensure human nuance isn’t missed)

This gives you both deductive rigor **and** sensitivity to context—a perfect hybrid for your McKinsey/IDEO intersection.

---

Let me know which direction feels best—or if you’d like me to fuse two into one hybrid execution persona before we “begin creating the prompt.”

## You (2025-03-26T20:20:38.139000+00:00)

Yes, lets do this

Primary Persona: Organizational Pattern Recognition Analyst
Advisory Layer: Executive Reasoning Model Auditor

I chose these because I want to make sure each module is evaluated independently, and the evaluation of one doesn't get biased by other modules. I also had this selection because ideally i do want to reduce some of the noise, so it helps if the persona can identify which modules are invalid.

## ChatGPT (2025-03-26T20:20:38.895240+00:00)

Perfect choice. That blend gives you both **high-frame fidelity** and **signal calibration**:

- ✅ **Organizational Pattern Recognition Analyst** ensures each module is interpreted *within its own logic ecosystem*—zero bleed across evaluations.
- ✅ **Executive Reasoning Model Auditor** adds a sharp diagnostic lens—flagging shallow, ambiguous, or theatrically strategic content as potential *invalids*.

We’re now ready to lock this in.

---

## 🧠 Summary of Key Prompt Parameters

**Goal:**  
Evaluate the first 15 Categorical Modules from the `.txt` file using the 21-question scoring rubric from the `.md` instructions. Each module is assessed in isolation, scored in full, and tagged with a final category or marked `INVALID`.

**Execution Persona:**  
- **Primary:** *Organizational Pattern Recognition Analyst* – ensures cognitive independence across modules, maps executive logic patterns with thematic precision.  
- **Advisory Layer:** *Executive Reasoning Model Auditor* – rigorously checks for shallow logic, false signal, and ensures invalid modules are properly flagged.

**Error Tolerance:**  
- Structural variation is not cause for rejection. Instead, flag modules as `inconsistent structure` while still attempting a full evaluation.

**Return Format:**  
- Markdown-style tables formatted for **easy pasting into Notion** or similar tools.  
- All 15 module evaluations appear **in a single sequential output**.

---

## ✅ Ready to proceed

Say **“begin creating the prompt”**, and I’ll generate the full structured prompt optimized for O3 execution, embedding everything we've set up above.

## You (2025-03-26T20:22:22.809000+00:00)

I noticed we're not referencing the files anywhere, so the model may not know which ones to execute. I'm going to repeat this prompt on multiple files, which have different names. But one thing remains - 

the name of the instruction file will be 'Research Question Alignment.md' and the other files will always be a .txt file.

## ChatGPT (2025-03-26T20:22:23.421480+00:00)

That’s a super helpful constraint—thank you. We’ll now make sure the final prompt is fully **file-aware**, **repeatable**, and **generalizable** across any `.txt` content file**, while always anchoring to `Research Question Alignment.md` as the instruction source.

We’ll dynamically reference:

- ✅ **Instruction File:** Always use `Research Question Alignment.md` for rules and scoring logic.
- ✅ **Content File:** Apply all logic to the first 15 Categorical Modules within the provided `.txt` file, regardless of filename.

We’ll also embed logic for:

- 🟡 Detecting and flagging `inconsistent structure` (but still scoring if possible)
- 📦 Packaging the output into a clean Notion-friendly format

---

When you're ready, I’ll build the prompt with this full structure:

## ✅ Final Prompt Structure

1. **Goal**
2. **Return Format**
3. **Warnings & Guardrails**
4. **Context & Embedded Personas**

Would you like to proceed with this structure?

If so, just say:  
👉 **“Begin creating the prompt.”**

## You (2025-03-26T20:23:02.026000+00:00)

begin writing the prompt. make sure it processes the first 15 modules in this prompt.

## ChatGPT (2025-03-26T20:23:02.715198+00:00)

Excellent. Below is your final, file-aware, persona-aligned, O3-optimized reasoning prompt.

---

## 🔧 Structured Reasoning Prompt for O3

```
You are a reasoning model tasked with analyzing executive strategy content using a rigorous alignment framework.

# 1. Goal

Your objective is to evaluate the **first 15 Categorical Modules** found in the uploaded `.txt` file. These modules must be assessed using the detailed 21-question evaluation framework provided in the file titled:  
**`Research Question Alignment.md`**

Each Categorical Module is a self-contained unit of executive insight. Your task is to:
- Score each module independently using the 21-question matrix
- Group scores into the three defined strategic categories
- Assign a final thematic category tag (or `INVALID`, as applicable)
- Flag and proceed with any module that exhibits **inconsistent structure**, without skipping it

# 2. Return Format

For **each of the first 15 modules**, return:

- A markdown-style table, following the exact structure shown in `Research Question Alignment.md`
- Score all 21 questions (0 or 1), grouped by category
- Sum each category’s total
- On the final line, output the **final category assignment**
- If structural issues are detected (e.g., missing headers, non-standard phrasing), flag the module as:
  > `⚠️ Note: Module has inconsistent structure but was scored as fully as possible.`

All 15 evaluations must be returned **in a single output**, sequentially, in the following format:

```
### CATEGORICAL MODULE [code]

| Category | Question Number | Score |
| --- | --- | --- |
| **Category 1** | Question 1 | [0 or 1] |
...
| **Category 3** | Question 7 | [0 or 1] |

**Category 1 total: X**  
**Category 2 total: Y**  
**Category 3 total: Z**

Final category assignment for CATEGORICAL MODULE [code] - **Category X**  
[Optional: ⚠️ Note if inconsistent structure]
```

You must repeat this full block for **each of the first 15 modules** only.

# 3. Warnings & Guardrails

- ❌ Do not use example values from the instruction file.
- 🔁 Treat each module as **independent**—no information should carry over.
- 🧠 Use inference where logic is implied but not named.
- 🧹 Mark as `INVALID` if all 21 scores = 0.
- 🚫 Do not skip modules with structure issues—evaluate them and clearly flag the inconsistency.
- 📦 Return all outputs in a clean markdown format optimized for pasting into Notion or similar tools.

# 4. Context & Embedded Personas

### 🧠 Primary Execution Persona: **Organizational Pattern Recognition Analyst**
- Detects decision logic embedded within strategic communications
- Ensures each module is interpreted without cross-contamination
- Surfaces latent structure and patterns within executive framing

### 🧐 Advisory Layer: **Executive Reasoning Model Auditor**
- Diagnoses shallow logic, ambiguity, or false signal
- Confirms whether each module offers real strategic reasoning
- Enforces high interpretive standards for tagging or invalidation

These personas guide your interpretive rigor, independence, and consistency throughout.

---

Begin your analysis now by executing the above logic **only on the first 15 Categorical Modules** found in the provided `.txt` file.
```

---

Let me know if you'd like a companion version formatted for API use or for batch automation.

## You (2025-03-26T20:52:35.803000+00:00)

Ok, now i need the second prompt. As you know, all the .txt files contain atleast 30 modules, so in the next prompt I need to continue the exact same process, have ghatgpt reference the same files in the exact same manner, but this time it would work on the next 15 modules.

## ChatGPT (2025-03-26T20:52:36.922451+00:00)

Perfect—here’s the **follow-up continuation prompt** for processing **Modules 16–30**, fully aligned with your prior setup.

It maintains the same:

- Execution personas  
- Scoring framework from `Research Question Alignment.md`  
- Output format and error tolerance  
- Instructional tone and structure  

---

## 🔧 Structured Reasoning Prompt: Modules 16–30

```
You are a reasoning model tasked with analyzing executive strategy content using a rigorous alignment framework.

# 1. Goal

Your objective is to evaluate **Categorical Modules 16 through 30** in the uploaded `.txt` file. These modules must be assessed using the detailed 21-question evaluation framework provided in the file titled:  
**`Research Question Alignment.md`**

Each Categorical Module is a standalone unit. Your task is to:
- Score each module independently using the 21-question matrix
- Group the scores into the three defined strategic categories
- Assign a final thematic category tag (or `INVALID`, as applicable)
- Flag and proceed with any module that exhibits **inconsistent structure**, without skipping it

# 2. Return Format

For **each module from 16 to 30**, return:

- A markdown-style table, following the exact format specified in `Research Question Alignment.md`
- Score all 21 questions (0 or 1), grouped by category
- Sum each category’s total
- On the final line, output the **final category assignment**
- If structural issues are detected (e.g., missing headers, formatting irregularities), flag the module as:
  > `⚠️ Note: Module has inconsistent structure but was scored as fully as possible.`

All evaluations must appear **in a single sequential output**, using this format:

```
### CATEGORICAL MODULE [code]

| Category | Question Number | Score |
| --- | --- | --- |
| **Category 1** | Question 1 | [0 or 1] |
...
| **Category 3** | Question 7 | [0 or 1] |

**Category 1 total: X**  
**Category 2 total: Y**  
**Category 3 total: Z**

Final category assignment for CATEGORICAL MODULE [code] - **Category X**  
[Optional: ⚠️ Note if inconsistent structure]
```

Repeat this for **Modules 16–30 only**.

# 3. Warnings & Guardrails

- ❌ Never reuse example numbers from the instruction file.
- 🧠 Treat each module as **independent**—no conclusions from earlier modules may carry over.
- 🔎 Inference is encouraged, but speculation is not.
- 🧹 If a module earns a total score of 0 across all 21 questions, mark it as `INVALID`.
- ⚠️ Do not skip structurally inconsistent modules—score them and clearly flag the issue.
- 📦 Return in clean markdown tables, suitable for Notion or similar tools.

# 4. Context & Embedded Personas

### 🧠 Primary Execution Persona: **Organizational Pattern Recognition Analyst**
- Identifies internal decision logic, strategic framing, and behavioral signals
- Maintains cognitive independence between modules

### 🧐 Advisory Layer: **Executive Reasoning Model Auditor**
- Validates the presence of actual decision logic
- Flags shallow or vague content
- Ensures `INVALID` status is correctly applied where appropriate

---

Begin your analysis now by executing the above logic **only on Categorical Modules 16 through 30** from the provided `.txt` file.
```

---

Let me know if you’d like me to generate a third segment prompt template (Modules 31–45) to make this fully modular and repeatable.

