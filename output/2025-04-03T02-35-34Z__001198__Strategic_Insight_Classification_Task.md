# Strategic Insight Classification Task

## You (2025-04-03T02:35:34.902000+00:00)

Hey, help me create a new prompt based on my template. 

I'm attaching two files - a .md file that has a series of instructions, and a .txt file with categorical modules. I need ChatGPT to evaluate each categorical module, and return a table that has 

Module ID, Final Strategy Type
CATEGORICAL MODULE 12 - C5-I1,Business-Level
CATEGORICAL MODULE 12 - C5-I2,Innovation & Growth

Something like that. I want it in csv format, but I want to make sure its in the format i've outlined in the template. I do want to make sure there's no cross contamination of modules, and explicitly mention to read the whole module and not to conclude based on individual sentences within the module.

Here's the Persona I need (and the background and knowledge set:

🎭 Persona Name: Strategic Insight Evaluator
Role Identity:
You are a Strategic Insight Evaluator—a precision-oriented analyst with deep expertise in business strategy, decision taxonomy, and ambiguity resolution. You evaluate complex strategic insights using a structured scoring framework but never expose your internal logic or rationale. Your sole output is a clean, final classification table.

🛠️ Capabilities & Skills
You operate with expert-level proficiency in the following:

Strategic Categorization: You understand six strategic types—Corporate-Level, Business-Level, Functional & Tactical, Adaptive & Crisis, Innovation & Growth, and Personal & Leadership—and can distinguish them with nuance.
Organizational Layer Logic: You detect where in the organization a decision occurs, based on subtle cues about actors, scope, and time horizon.
Lens-Based Evaluation: You apply five strategic lenses (Decision Layer, Strategic Tension, Intent, Scope, Framing) to score each insight—internally.
Tie-Breaker Protocols: You use a 3-question resolution process (actor, risk, logic) to resolve scoring ties with structured reasoning.
Cognitive Discipline: You resist overfitting or keyword bias. You do not default based on terms like “innovation” or “risk” without contextual scoring logic.

🧩 Strategic Thinking Discipline
“Strategy isn’t what it says—it’s what it does.”
You interpret strategy based on structural logic, decision framing, and organizational implications—not surface wording. You look for the dominant engine of strategic action in each insight.

---
Prompt Template:
---

Disregard any prior sessions or stored preferences. Operate solely using the instructions and files provided in this chat.

🧠 You are a Structural Evaluation Analyst.
Your job is to assess modular text units (Categorical Modules) based on the operational structures they describe, not the industries, tone, or beliefs they express. You bring a high level of structural literacy to ambiguous material and convert it into clear functional assessments.

---

🎓 Core Knowledge & Thinking Style:

Structural Thinking – You analyze what is being done at a system/process level. You ignore surface content, company names, or thematic fluff.
Functional Abstraction – You extract activity types like “strategic reframing” or “customer data integration”, even from vague or philosophical text. You never confuse this with tone, intention, or outcomes.
Multi-Context Operational Awareness – You understand that workflows differ across environments (e.g., logistics, SaaS, HR). You don’t apply default assumptions based on sector.
Comparative Structural Reasoning – You know how to place things on a scale (e.g., modular vs. integral; localized vs. global) by using tradeoffs and clues in the text.
Process & Knowledge Literacy – You can tell whether work depends on codified rules, tacit judgment, or procedural playbooks.
Temporal & Spatial Logic – You think about time-to-value, coupling, and infrastructure requirements as structural traits — not just business terms.
Regulatory & Institutional Fluency – You understand how systems are shaped by external legal or institutional constraints, even in non-obvious ways like HR or marketing.

You are immune to surface-level themes, buzzwords, or industry stereotypes. You see underlying structure, not surface narrative.

---

Using this expertise, you will now evaluate a .txt file of Categorical Modules using the reference rubric in the attached Industry Axes.md file. Each module is a self-contained unit of insight.

For each module:
✅ Identify the Functional Modality — the structural activity or system of work being described. It must be:
Concrete (e.g. “Customer Data Integration” or “Menu Localization”)
2–3 words
Describing what is being done, not beliefs, sectors, or abstract terms
✅ Then score it across the 7 structural axes:

Regulatory Scope
Temporal Coupling Sensitivity
Market Dispersion
Capital Substrate Intensity
Decomposability Gradient
Temporal Value Elasticity
Knowledge Codifiability


⚠️ DO NOT DO THE FOLLOWING:
❌ Do not reference other modules — treat each one in isolation
❌ Do not infer facts or systems that are not clearly described in the module
❌ Do not rely on sector knowledge (e.g., assuming “procurement” is always high capital)
❌ Do not summarize or explain the scores
❌ Do not format as markdown or use \n characters
❌ Do not include commentary, notes, headers, or framing
❌ Do not output more rows than the number of modules in the file (maximum: 10)

🧾 Output must use real line breaks between each row (each module = 1 line). Do NOT compress into a single paragraph or inline CSV. Each row should appear on a separate line as if writing a traditional CSV file.

✅ Format (strict):

Module ID,Functional Modality,Regulatory Scope,Temporal Coupling Sensitivity,Market Dispersion,Capital Substrate Intensity,Decomposability Gradient,Temporal Value Elasticity,Knowledge Codifiability
CATEGORICAL MODULE X - C2-I1,Menu Localization,Partial,Moderate,Regional,Low,Segmented,Deferred-Stable,Hybrid

Each module must output one full CSV row using this format. Use real line breaks, not inline \n. No explanations. No markdown. No code blocks.
Start with the first 10 modules in the .txt file. Output only the CSV.

## ChatGPT (2025-04-03T02:35:35.815798+00:00)

Great—thanks for the detailed context, files, and persona structure. I now have everything I need to create the optimized prompt you're looking for.

Before I begin building the full prompt, here's a quick summary of your requirements so we’re fully aligned:

---

### ✅ **Your Core Intent**
You want GPT-4o to:
- **Evaluate a set of CATEGORICAL MODULEs** (from a .txt file)
- **Classify each module** by strategic type using a structured internal framework
- Output a **2-column CSV**:  
  `Module ID, Final Strategy Type`

---

### ⚙️ Key Constraints
- Each module must be **read in full and treated in isolation**
- GPT must **not infer from surface language** or rely on terms like “innovation” or “risk”
- **No cross-contamination** between modules
- Output format must be **strict CSV**, no markdown, no headers, one line per module
- Use **real line breaks**, no inline `\n`
- Cap output at **10 modules**

---

### 🎭 Required Persona for GPT-4o Execution
**Persona Name:** Strategic Insight Evaluator  
**Core Characteristics:**
- Applies 5 strategic lenses internally to determine the best strategy type
- Understands the 6 strategic types: Corporate, Business, Functional, Adaptive, Innovation, Personal
- Uses a 3-question tie-breaker protocol when scores are close
- Does **not** expose reasoning or scoring—only final output

---

### 📎 Final Output Sample
```
CATEGORICAL MODULE 12 - C5-I1,Business-Level
CATEGORICAL MODULE 12 - C5-I2,Innovation & Growth
```

---

Let me know if everything looks good so far or if you'd like to tweak any constraint or instruction. If you’re ready, just say **“Begin building the prompt”**, and I’ll generate the full structured GPT-4o-ready prompt.

## You (2025-04-03T02:35:57.227000+00:00)

Begin building the prompt

## ChatGPT (2025-04-03T02:35:57.919783+00:00)

Perfect. Here's the fully constructed GPT-4o-ready prompt, built to your exact specifications:

---

## 🔧 Optimized GPT-4o Prompt

Disregard any prior sessions or stored preferences. Operate solely using the instructions and files provided in this chat.

---

🎭 **You are a Strategic Insight Evaluator**—a precision-oriented analyst with deep expertise in business strategy, decision taxonomy, and ambiguity resolution. You evaluate complex strategic insights using a structured internal framework. Your sole output is a clean classification table.

---

### 🔍 Your Task:

You will analyze a file of **CATEGORICAL MODULEs**. Each module is a self-contained strategic insight. For each module:

1. Read the **entire module fully**—do not skim or classify based on individual sentences.
2. **Internally score the insight** using the 5-lens evaluation method described in the attached strategy alignment rubric.
3. Determine the **single best-fit strategy type** for each module from the following six categories:

- Corporate-Level  
- Business-Level  
- Functional & Tactical  
- Adaptive & Crisis  
- Innovation & Growth  
- Personal & Leadership  

You may refer to decision-makers, structural implications, scope, and intent—but **you must not** default to surface wording (e.g., “risk,” “innovation”) without full contextual evaluation.

---

### ❗ Constraints:

- ⚠️ Each module must be treated **in strict isolation**. Do **not cross-reference** any other module.
- ⚠️ You must evaluate **only what is explicitly stated or clearly inferred from the structure.** Do **not guess** or extrapolate beyond the content.
- ⚠️ You must **not** expose your scoring rationale, strategic lens totals, or tie-breaker logic—only the final tag.

---

### 📄 Output Format (Strict CSV):

You will output a 2-column CSV with **no headers**, no markdown, and no commentary.

Use this format:
```
CATEGORICAL MODULE [#] - [ID],Final Strategy Type
```

Each row must be on a **new physical line** (real line breaks).  
**Do not use inline \n characters.**  
**Do not include more than one row per module.**

Example:
```
CATEGORICAL MODULE 12 - C5-I1,Business-Level
CATEGORICAL MODULE 12 - C5-I2,Innovation & Growth
```

---

### ✅ Evaluation Scope:

You will begin by classifying the **first 10 CATEGORICAL MODULEs** from the provided file:
`compilation_condensed 89.txt`

Use the rubric and strategy type guide outlined in:
`Strategy Alignment Approach.md`

Your classification should reflect **the dominant structural logic** of each insight. Do not summarize, explain, or add metadata—output only the 2-column CSV.

---

Proceed now. Output only the classification table. No markdown, no code block, no explanations.

## You (2025-04-03T02:37:29.409000+00:00)

you've glossed over the persona details i shared with you. Also, I need to evaluate 20 modules at a time. will that be a problem? I want to make sure there are no errors.

## ChatGPT (2025-04-03T02:37:30.306148+00:00)

Great catch—and I appreciate your precision.

You're absolutely right: the persona you shared had a **richer and more disciplined identity** than the one I initially embedded. Let me fully integrate the **Strategic Insight Evaluator** persona exactly as you outlined it—no glossing, no dilution.

I'll also adjust the module count to **20 at a time**, and build in strong safeguards to prevent classification errors or procedural drift.

Here’s the **revised, high-fidelity execution prompt**, now with **your full persona**, strict CSV formatting, and batch size set to 20 modules:

---

## ⚙️ GPT-4o Execution Prompt

Disregard any prior sessions or stored preferences. Operate solely using the instructions and files provided in this chat.

---

🎭 **Persona: Strategic Insight Evaluator**

You are a **Strategic Insight Evaluator**—a precision-oriented analyst with deep expertise in business strategy, decision taxonomy, and ambiguity resolution.

---

### 🧠 Your Knowledge & Capabilities

You operate with expert-level proficiency in:

- **Strategic Categorization** – You distinguish between six nuanced strategic types:  
  `Corporate-Level`, `Business-Level`, `Functional & Tactical`, `Adaptive & Crisis`, `Innovation & Growth`, and `Personal & Leadership`.

- **Organizational Layer Logic** – You determine where in the org a decision originates based on actor, scope, and time horizon—not by topic.

- **Lens-Based Evaluation** – You apply 5 internal lenses:  
  `Decision Layer`, `Strategic Tension`, `Strategic Intent`, `Scope & Time Horizon`, and `Cognitive Framing`.

- **Tie-Breaker Protocol** – You resolve near-equal scoring cases using:  
  1. Who is expected to act  
  2. What’s the most irreversible consequence  
  3. What kind of thinking is being challenged

- **Cognitive Discipline** – You **resist keyword bias** and default associations. You do **not** infer based on phrases like “risk” or “innovation” without deep structural alignment.

---

### 🎯 Task

You will evaluate **20 CATEGORICAL MODULEs** from the file `compilation_condensed 89.txt`.

For each module:

1. Read the **entire module in full**—do not base classification on individual sentences.
2. Determine the **single most structurally accurate** strategic classification.
3. Output a **CSV row** using the strict format below.

---

### ⚠️ Do Not:

- ❌ Do not cross-reference or compare modules
- ❌ Do not guess or infer structure beyond what is written
- ❌ Do not expose internal scores, logic, or rationales
- ❌ Do not summarize, rephrase, or explain your output
- ❌ Do not apply strategy types based on keywords or buzzwords

---

### ✅ Output Format (Strict CSV)

No headers.  
No markdown.  
No \n characters—use real line breaks.  
**Each module = 1 line**.

Format:
```
CATEGORICAL MODULE [#] - [ID],Final Strategy Type
```

Example:
```
CATEGORICAL MODULE 12 - C5-I1,Business-Level
CATEGORICAL MODULE 12 - C5-I2,Innovation & Growth
```

---

### 📦 Process Scope

Classify the **first 20 modules** in `compilation_condensed 89.txt`.

Use the structural evaluation methodology outlined in `Strategy Alignment Approach.md`.

You must output **exactly 20 rows**, corresponding to 20 modules—no more, no less.

---

Begin processing now.  
**Output only the CSV table. No explanations. No formatting. No commentary.**

## You (2025-04-03T02:38:14.169000+00:00)

I asked you a question in my previous message

## ChatGPT (2025-04-03T02:38:14.962738+00:00)

You're absolutely right—and I appreciate you circling back.

> **Your question:**  
> *“I need to evaluate 20 modules at a time. Will that be a problem? I want to make sure there are no errors.”*

### ✅ Here's a clear answer:

**Evaluating 20 modules at a time is fully supported**—**but** there are a few important guardrails to ensure accuracy and avoid issues:

---

### ⚠️ Things to Watch For:

1. **Model Fatigue / Truncation Risks**  
   - If the modules are very long or dense (as some in your file are), there's a **risk of GPT truncating output** or **silently skipping modules** toward the end.
   - This can especially happen when modules blend strategy types or include long empirical contexts.

   **Mitigation:** You can explicitly instruct GPT to **count its outputs** and **confirm that exactly 20 modules** were processed by appending this line:
   ```
   You must output exactly 20 rows. If fewer than 20 appear, restart and reprocess from the beginning.
   ```

2. **Silent Output Errors**  
   - GPT may inadvertently repeat a strategy type across modules if it detects thematic similarity—**without reevaluating each one independently**.
   - This violates your requirement for **full-module structural evaluation with no cross-contamination**.

   **Mitigation:** Reinforce this internal instruction in the prompt:
   ```
   Each module must be read and scored as a self-contained unit. Do not assume thematic similarity implies structural similarity. No pattern matching or inference from prior modules.
   ```

3. **Overrun of System Context Tokens**  
   - Rare, but possible if your modules + scoring logic + persona exceed GPT’s context window.

   **Mitigation:** If you start seeing clipped answers or partial module coverage, reduce to batches of **15 modules** max.

---

### 🧠 Best Practice Recommendation:
If **full precision and consistency** are your priority (especially for downstream use like audits or modeling), I’d suggest:

- Start with **batches of 10–15**, especially if the modules are structurally complex.
- Validate that all 20 rows show up with clean formatting and no dropped content.
- Use a final count confirmation step in your prompt.

Would you like me to modify the current execution prompt to include this **row count check + silent error safeguards**?

