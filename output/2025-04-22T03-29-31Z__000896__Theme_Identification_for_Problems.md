# Theme Identification for Problems

## You (2025-04-22T03:29:31.441503+00:00)

help me write a prompt for the following intent.

I have this file called people-problem-statements-v4.md and then I have another file called archetype-things what I need is if you go through the file the people-problem-file, what you'll find is a series of people-problem-statements along with a how do we know this is a problem kind of statement so each of those think of those like proof of a problem so the problem proofs are actually based on some themes that are listed inside the .txt file so if you read the .txt file what you'll also find is each theme has like three content modules and so those content modules essentially represent some extracted information from from a research paper and so that acted as raw data for us and when we were formulating the people-problem-statements and identifying proof of the problem statement we based the proof on the actual modules within each theme now what I want chat-gpt to do is for each individual problem statement I want to understand which theme does it belong to so the best way to find that out would be to read through the problem proof which will be the how do we know this is a problem section read that and read other parts of the .txt file figure out which module it belongs to and return for each individual people-problem-statement I want to know which theme it belongs to just read through the two files and you might get a better sense

## ChatGPT (2025-04-22T03:29:32.328684+00:00)

Awesome—I've gone through both files, and your setup is rich and well-structured. Let's distill your intent clearly before we **begin creating the prompt**. Here's what I’m hearing:

---

### 🧭 **Your Goal**
You want GPT to determine **which theme** (from the `Cluster_Compilation.txt` file) each **people-problem-statement** (from `people-problem-statements-v4.md`) belongs to.

### 📌 **How?**
By:
1. **Reading the “🔍 How do we know this is a problem?” section** of each people-problem.
2. Matching this “proof of problem” section against the **modules within themes** in the .txt file.
3. Identifying which **theme** the “proof” most closely aligns with — since the problem proof was **informed by** specific content modules during your original process.

---

### 🧠 Observations
- Each “proof of problem” contains key contextual signals (e.g., company examples, executive dilemmas, phrases like “Module 18 (Theme 402)”).
- In several cases, the problem already explicitly references a module and theme (e.g., “Module 18 (Theme 402)”), so GPT could treat this as a **strong signal**.
- In others, the theme must be inferred using similarity of concepts, terms, and decision contexts.

---

### 🔧 Output You Expect
For each **People Problem**, you want GPT to return:
- The **matching theme number**
- Optionally, a confidence level or rationale if ambiguity exists
- Possibly the **module number** within that theme, if it's a clear match

---

Before we proceed, quick check:
1. Would you prefer the output **as a table**, a **bullet list**, or **JSON**?
2. Should GPT **strictly assign one theme per problem**, or can it **return multiple themes** with varying confidence?
3. Would you like GPT to **include module numbers**, or is **theme-level identification** sufficient?

Let me know and I’ll queue up the formal creation with those preferences.

## You (2025-04-22T03:30:28.724037+00:00)

I want the output as a table. The GPT can return multiple themes with varying confidence. I can self-correct on that. It doesn't need to include module numbers for now. It's just theme-level identification.

## ChatGPT (2025-04-22T03:30:29.295201+00:00)

Perfect—that gives us everything we need to **begin creating the prompt**. Here's a quick recap of the core insights and preferences before I craft the final O3-optimized prompt.

---

## ✅ Summary of Key Prompt Design Inputs

### **Goal**
Assign each People Problem Statement to one or more **Themes** from a research framework, based on evidence in its “How do we know this is a problem?” section.

### **User Intent Nuance**
- User wants **theme-level mapping only** (no need for module detail).
- GPT should match **based on conceptual, linguistic, and contextual similarity** between the problem proof and research themes.
- Multiple themes can be returned **with varying confidence levels**.
- Output should be in a **clean table format** with each row corresponding to one people-problem and one or more inferred theme(s).

### **Execution Persona**
A **qualitative researcher** or **thematic analyst** trained in inductive and deductive inference from empirical material. The analyst will:
- Perform semantic and thematic coding.
- Prioritize alignment between proof narratives and conceptual frames.
- Acknowledge when thematic mappings are inferential vs. explicit.

### **Reasoning Style**
Hybrid: a mix of **deductive tagging** (when themes are cited explicitly) and **inductive inference** (when mappings must be derived from concept similarity).

---

## ✅ Final Prompt Output

Here is your full O3-compatible prompt:

---

### 🔧 **Prompt Structure for O3**

**Goal:**
For each “People Problem Statement” listed in a markdown file, assign one or more **Themes** from a research framework (contained in a second file) that best align with the rationale in the section titled “How do we know this is a problem?”. Use conceptual similarity and context to guide assignments, not just keyword overlap.

**Return Format:**
Return your results as a **Markdown table** with the following columns:
- **People Problem ID** (e.g., Archetype 1 - Problem 1)
- **Problem Summary** (shortened version of the people problem statement)
- **Assigned Theme(s)** (theme numbers, e.g., “Theme 101, Theme 402”)
- **Confidence & Rationale** (brief explanation; explain if multiple themes are returned)

**Warnings & Guardrails:**
- When a theme is **explicitly mentioned** in the problem proof, treat that as a high-confidence direct match.
- Where multiple themes appear plausible, return all viable candidates and briefly explain.
- Do not return module-level detail.
- Avoid superficial matches—focus on thematic alignment of *problem framing* and *decision-making context*.
- Flag statements where the theme is ambiguous or unclear and explain the ambiguity in the rationale.

**Context & Additional Elements:**
You are a **thematic analyst** trained in qualitative coding of empirical strategy and leadership research. The first file (“People Problem Statements v4.md”) includes problem definitions and supporting rationales (proofs). The second file (“Cluster_Compilation.txt”) outlines themes and associated content modules drawn from empirical research. These modules served as raw material for the problem statements. Your task is to reverse-map which theme(s) each problem proof most likely drew from.

---

Would you like me to test this prompt immediately with a few examples from your files to show what the table might look like?
