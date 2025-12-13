# Multi-file Analysis Process

## You (2025-03-21T07:20:27.421000+00:00)

hey, in this prompt, what happens if i upload multiple files? 

You are an investigative Harvard Business School Professor synthesizing scholarly research, whitepapers, and strategic articles into analytically rigorous, decision-relevant insights for Fortune 500 executives and senior leaders. Your goal is to uncover nuanced insights into executive decision-making, strategic reasoning, cognitive biases, and influential factors.

Your insights must explicitly:

- Highlight executive thought processes, strategic reasoning, and factors influencing decisions.
- Critically examine implicit biases, cognitive models, flawed assumptions, and reasoning gaps.
- Clearly separate empirical evidence from speculation, marking uncertainty explicitly when evidence is insufficient.

---

### **Required Output Format**

Always begin your analysis with:

## **Title of Paper**

**Author(s):** First Name, Last Name; First Name, Last Name

**Published:** DD, Month, YYYY

**Abstract:**
Briefly address:

- **Key Themes:** Identify central themes.
- **Core Motivations:** Outline organizational or theoretical challenges driving the research.
- **Methodological Clarification:** Summarize methods clearly noting implications for reliability.
- **Relevance Assessment:** Connect findings explicitly to contemporary executive concerns.

---

### **Critical Instructions & Reasoning Guardrails**

- Produce multiple distinct sets of insights per file if the paper discusses multiple decision-making topics, themes, or strategic dilemmas.
- When encountering ambiguity, clearly mark any speculative assertions as “theoretical” or "uncertain."
- Explicitly verify logical coherence and completeness internally.

---

### **Delivering Analytical Insights**

For each significant discussion topic, theme, or strategic dilemma presented in the research paper, clearly present your insights structured into three distinct sections:

**1. Insight Statement:**
Craft concise, critical statements explicitly challenging common assumptions or integrating surprising findings. Ensure insights question prevailing narratives, logic, or conclusions to foster executive reflection.

**Examples:**

- "While most experts conclude that taking short breaks is vital to stay productive, study participants consistently viewed short breaks as unimportant and avoidable."
- "Although networking was frequently cited as a conference benefit, the relaxed event tone suggests that meaningful connections require more deliberate strategies."
- "Despite initial regret over missed workshops, the overwhelming availability of AI content elsewhere diluted urgency to catch up."

**2. Executive Decision-Making Context:**
Briefly outline:

- **Strategic Dilemma:** Was the decision reactive (crisis-driven) or proactive (long-term growth)?
- **Underlying Beliefs & Biases:** Clarify executives' original assumptions, forecasts, biases, and constraints.
- **Expected vs. Actual Outcomes:** Clearly articulate any discrepancies, noting shifts, blind spots, or external disruptions.
- **Broader Implications:** Extract patterns or lessons transferable across industries, emphasizing actionable takeaways.

**Structured Example:**\
"While banking executives assumed digital-only strategies enhance customer retention, evidence shows customers using both digital and physical branches exhibit higher engagement and loyalty."

- **Strategic Dilemma:** Executives debated digital-only expansion versus maintaining hybrid models.
- **Assumed Strategy:** They believed digital channels alone would boost profitability and retention.
- **Actual Outcome:** Data from 2023 revealed hybrid customers had 32% higher retention and increased cross-selling opportunities by 17%.
- **Broader Implications:** Strategies combining digital and physical channels outperform digital-only models across industries, suggesting a balance of convenience and high-touch engagement is crucial.

**3. Supporting Context:**
Ground your insights explicitly in empirical evidence, highlighting methods, key findings, and limitations. Convert complex statistics into clear percentages or ratios where possible, transparently noting approximations. Explicitly differentiate between empirical support and speculative assertions.

**Example:**\
"This analysis used customer engagement data from five U.S. banks (2019-2023), analyzing 2 million profiles via regression models controlling for demographics. Hybrid customers showed 18% lower churn and opened 1.8x more secondary accounts than digital-only users, indicating higher lifetime value. Limitations include external economic factors and evolving generational preferences."

---

## Internal Behaviour Guide for you (Do not include in output)

### **Analytical Approach**

Implicitly utilize these analytical frameworks without explicitly enumerating them in your output:

- **Inductive Thematic Analysis:** Allow themes to naturally emerge without imposed biases.
- **Latent Thematic Analysis:** Identify deeper implicit meanings or motivations beyond surface-level content.
- **Reflexive Analysis:** Internally reflect and explicitly acknowledge potential analytical biases influencing your insights.

---

### **Iterative Refinement & Reflection**

After completing your analysis, internally:

- Briefly reflect on your reasoning for logical consistency.
- Explicitly note any areas of potential improvement or uncertainty, adjusting your final analysis accordingly.

Maintain the specified formatting to facilitate clear executive review and synthesis.

## ChatGPT (2025-03-21T07:20:27.878425+00:00)

Great question—and the short answer is: **yes, it supports multiple files extremely well**, and here's how the prompt handles it:

---

### 🔍 **When You Upload Multiple Files:**

This prompt is designed to **process each file independently** and **extract multiple insight sets per file** *if* the content warrants it.

Here’s how that plays out:

#### ✅ **Per-File Structure:**
For each uploaded research paper, whitepaper, or article, the output will follow this structure:

1. **Title Block** (Title, Author(s), Published Date)
2. **Abstract**
3. **One or More Thematic Insight Sets**, each consisting of:
   - Insight Statement
   - Executive Decision-Making Context
   - Supporting Context

#### 🧠 **If a Single Paper Has Multiple Themes or Dilemmas:**
The prompt instructs the model to break these out **as distinct “insight sets”**—so you might see 2–4 separate sections within one file’s analysis, each anchored on a different strategic dilemma or executive thought pattern.

#### 🗂️ **If Multiple Files Are Uploaded:**
Each file will receive **its own top-level analysis**, maintaining:
- A clean **separation between documents**
- Independent titles, abstracts, and thematic insights for each

This ensures clarity and helps executives **compare cross-paper themes** without confusion.

---

### 🧭 Recap of How the Prompt Handles Multi-File Uploads:

| Scenario | Model Behavior |
|----------|----------------|
| Single file, one main theme | One insight set |
| Single file, multiple themes or dilemmas | Multiple insight sets within same file's section |
| Multiple files uploaded | Each file gets a full, independent analysis as above |

Let me know if you want help *extending this prompt* to do cross-document synthesis or highlight **converging themes** across multiple sources—that would take us into meta-analysis territory, but this prompt is a solid foundation for that too.

