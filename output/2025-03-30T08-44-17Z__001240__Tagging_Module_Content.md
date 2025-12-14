# Tagging Module Content

## You (2025-03-30T08:44:17.140000+00:00)

Goal:
Read and process the first 15 content modules from a `.txt` file. For each module, assign **exactly one tag per tagging category**, based strictly on the taxonomy provided in a separate `.md` file. Tags must be grounded in the full, end-to-end content of each individual module.

Return Format:
Return the output as a markdown-formatted CSV table. The first column should be `ModuleID` (e.g., "CATEGORICAL MODULE 17 - C2-I6"). Each subsequent column must represent one tag category from the `.md` file, in fixed order. Each row should contain one and only one tag per field. If a suitable tag does not apply to a module, insert `'N/A'`. Do not include summaries, analysis, commentary, or code—only the table.

Sample Output Format:
| ModuleID | Ambiguity Type | Framing Move | Stabilizer | False Clarity | Residual Ambiguity | Tension Axis | Surface vs. Deep Contradiction | Decision Outcome | Organizational Implication |
|----------|----------------|---------------|-------------|----------------|----------------------|---------------|-------------------------------|----------------------|------------------------------|
| CATEGORICAL MODULE 17 - C2-I6 | Strategic Trade-Off Ambiguity | Empirical Anchoring | Empirical Validation and Piloting | N/A | Cultural and Org. Friction | Efficiency Optimization vs. Strategic Differentiation | Explicit | Outcome Stabilized Through Workarounds | Capability or Resource Strain |

Warnings & Guardrails:
- **Tagging must be based *only* on the `.md` file.** Do not rely on general knowledge, assumptions, synonyms, or prior associations.
- A tag should be applied only when the content clearly matches the definition’s **“What it Means”** section and does **not** match its **“What it Does Not Mean.”**
- **Each module must be evaluated independently.** Do not allow tags or logic from previous modules to influence new ones.
- **Do not extrapolate common themes or apply heuristic shortcuts.** Every tag must be earned from the module’s own evidence.
- **If no tag meaningfully fits a category—even interpretively—use `'N/A'`.** Do not assign a tag based on weak or partial alignment.
- If ambiguity exists, make a principled judgment—but still assign only **one tag per category**.
- Avoid overusing default tags. Apply the full range of taxonomy categories actively and deliberately.
- Maintain the sequence of modules as they appear in the `.txt` file. Do not reorder, blend, or skip.
- Module boundaries are clearly marked by:
  - Start: `### CATEGORICAL MODULE [ID]`
  - End: `END OF CATEGORICAL MODULE.`
- Stop tagging after the first **15 complete modules**. Do not tag beyond that.

Context & Execution Personas:
- **Primary Persona:** A tenured Harvard Business School professor with deep expertise in leadership, ambiguity resolution, decision-making under uncertainty, and interpretive research.
- **Advisory Persona:** A seasoned McKinsey research analyst with domain-level fluency in data tagging systems, decision ambiguity frameworks, and high-integrity categorization practices.
- These personas jointly analyze and tag each module with analytical rigor, interpretive clarity, and professional detachment.

Files Used:
- The `.md` file is a structured taxonomy handbook that defines all tagging categories, including:
  - Ambiguity Type
  - Framing Move
  - Stabilizer
  - False Clarity
  - Residual Ambiguity
  - Tension Axis
  - Surface vs. Deep Contradiction
  - **Decision Outcome**
  - Organizational Implication
  **This file is the sole authority on tagging.**
- The `.txt` file contains the module content to be tagged. Each includes:
  - An Insight Statement
  - An Executive Decision-Making Context
  - Supporting Context

Checklist for Output:
- [x] Output is in markdown CSV format.
- [x] Header row defines columns in the correct fixed order (including `Decision Outcome`).
- [x] Each row begins with the correct `ModuleID`.
- [x] One and only one tag per category per row.
- [x] Use `'N/A'` only when no tag fits by the `.md` definition.
- [x] Only the first 15 modules are included.
- [x] No summary, explanation, or extra content beyond the table.
