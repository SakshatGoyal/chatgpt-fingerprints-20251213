# O3 Prompt Evaluation Table

## You (2025-03-26T05:25:38.422000+00:00)

hey, i need your help writing an o3 prompt where I want it to use the instructions given in the .md file to evaluate the responses in the .csv file.

for your context, these are prompts different students generated when we asked them the question:

“Using chain-of-thought prompting, write a prompt that you could use to help complete a project at work.”

the csv file contains the response numbers and the responses they generated. In the output, I want chatGPT to give me a table with the first column being the response number, and the subsiquent columns being the criterion names. the table should have rows that highlight the final score for each prompt under each criterion.

Any questions?

## ChatGPT (2025-03-26T05:25:39.045589+00:00)

Thanks, I’ve got what I need now. Just to quickly confirm before we **begin creating the prompt**, here's how I’m interpreting your request:

---

### ✅ **Your Objective**
You want GPT-4 (O3) to evaluate student-generated prompts (from a CSV) using a structured rubric (from the Markdown file) and return a **table** that includes:

- **First column:** Response number from the CSV.
- **Subsequent columns:** One column for each of the six rubric criteria.
- **Each row:** The evaluation scores (1–10 or 1–5, per rubric) for a specific response across all criteria.

Optional clarification:
- Are you expecting **raw scores only**, or would you also like a **final total score** per response and/or a **quality rating** (“High Quality,” “Satisfactory,” “Needs Revision”)?
- Should GPT **only return the table**, or also include **brief justification** (e.g., 1–2 sentences per score or per response)?
- Do you want the O3 model to **strictly follow the rubric descriptions**, or are you okay with some interpretive judgment where responses fall in-between?

Once I get the answers to those, we can lock this in and I’ll start building the optimized O3 prompt.

## You (2025-03-26T05:28:01.605000+00:00)

I want raw scores only.
only the table
I'm ok with a bit of interpretice judgement. but for the most part it should follow the rubric descriptions. Is the csv file i attached too heavy by any chance? tell me a few things that could possibly go wrong and how we can address those

## ChatGPT (2025-03-26T05:28:02.211009+00:00)

Perfect, thanks! Here's what you're asking for, just to reaffirm:

- ✅ **Only the table** (no narrative, just raw scores).
- ✅ Each row = a student's prompt response.
- ✅ Columns = Response number + scores for each rubric criterion.
- ✅ Some interpretive flexibility is allowed, but GPT should primarily **anchor scoring in the rubric**.
- ✅ Total score and quality rating **not required**.
- ✅ You’re using this for **automated evaluation** of prompt-writing ability.

Now, regarding the `.csv` file and what could go wrong:

---

### ⚠️ Potential Issues & Mitigations

1. **❌ Response Length or Density**
   - **Risk:** Some prompts might be long, multi-part, or contain irrelevant chatter. That can muddy the evaluation.
   - **Mitigation:** Instruct the model to **ignore unrelated preambles or commentary** and focus only on the functional prompt.

2. **❌ Ambiguous or Edge-Case Prompts**
   - **Risk:** Some responses may be borderline or fall between rubric score levels (e.g., between a 3 and a 4).
   - **Mitigation:** Instruct GPT to default to **the lower score in cases of ambiguity** unless a clear justification exists per rubric phrasing.

3. **❌ CSV Encoding or Parsing Issues**
   - **Risk:** If the CSV is irregular (e.g., extra line breaks inside responses), GPT might misparse rows.
   - **Mitigation:** Tell GPT to **parse each row by Response Number and the full corresponding response only**, and to skip malformed entries if unsure.

4. **❌ Rubric Weight vs. Score Confusion**
   - **Risk:** GPT might confuse rubric *weights* (percentages) with score ranges.
   - **Mitigation:** Clarify that the model should **ignore weights and only assign raw scores** per the score range listed under each criterion.

5. **❌ Inconsistent Interpretation Across Responses**
   - **Risk:** Without calibration, the model might drift in how strictly it applies certain criteria across entries.
   - **Mitigation:** Include a directive for GPT to **apply consistent standards across all rows** and err on the side of conservative scoring when uncertain.

---

If you're good with all that, just say **“begin creating the prompt”**, and I’ll generate the final optimized O3 prompt with structure, embedded rubric, instructions, and formatting guidance.

## You (2025-03-26T05:28:49.068000+00:00)

ok, begin creating the prompt that can help me achieve the goal i mentioned, while also addressing some of the issues you've outlines.

## ChatGPT (2025-03-26T05:28:49.862110+00:00)

Great—we're now moving into prompt construction.

---

### 🔍 **Summary of Analytical Intent**

You want GPT-4 (O3) to act as an *automated evaluator* using a rubric to assess student-generated prompts (written in response to a specific meta-prompting question). The evaluation should output a clean, consistent **table of raw scores** only—one row per response, and one column for each rubric criterion.

You’re prioritizing:
- **Rigorous, rubric-based scoring**
- **Output as a table only (no explanations)**
- **Interpretive flexibility**, but primarily rubric-aligned
- **Consistency across entries**

---

### 👤 Execution Persona for the Prompt

**Persona:** “Chain-of-Thought Prompt Evaluator”

A meticulous, rubric-trained evaluator designed to analyze AI prompt quality using structured scoring criteria. Applies interpretive reasoning when needed but remains anchored in provided definitions. Skips broken rows, ignores off-topic fluff, and is strict on coherence.

---

### ✅ Final O3 Prompt (with structure)

```
You are a Chain-of-Thought Prompt Evaluator.

Your task is to evaluate a series of student-written prompts based on the rubric below. These prompts were submitted in response to the instruction:

**“Using chain-of-thought prompting, write a prompt that you could use to help complete a project at work.”**

---

## 🧠 Evaluation Rubric

Evaluate each student prompt using the six criteria below. For each criterion, assign a **raw score only**, using the score ranges provided. Do not consider the weight percentages—use only the scoring range per criterion.

### 1. Clarity of Reasoning Structure (1–10)
- Measures how clearly the prompt instructs multi-step, logical reasoning.
- Score 1–3: No reasoning structure.
- Score 4–6: Vague multi-step hints.
- Score 7–8: Clear CoT structure.
- Score 9–10: Elegant breakdown into sub-parts.

### 2. Task Relevance & Purposefulness (1–10)
- Measures how well the prompt aligns with real workplace tasks.
- Score 1–3: Vague or unrealistic.
- Score 4–6: Plausible but general.
- Score 7–8: Realistic and specific.
- Score 9–10: Valuable, clearly defined work-related task.

### 3. Specificity & Context Provided (1–5)
- Measures presence of relevant framing, context, and constraints.
- Score 1: No context.
- Score 2–3: Sparse or generic.
- Score 4: Useful, relevant details.
- Score 5: Rich, focused, well-targeted context.

### 4. CoT Instruction Appropriateness (1–5)
- Measures how well the prompt cues chain-of-thought reasoning.
- Score 1: No cue.
- Score 2–3: “Think step by step” is loosely integrated.
- Score 4: Clear CoT flow.
- Score 5: Seamlessly integrated step-wise structure.

### 5. Clarity of Language & Structure (1–5)
- Measures clarity, grammar, professionalism.
- Score 1: Confusing or ungrammatical.
- Score 2–3: Awkward or overly wordy.
- Score 4: Clear and well-structured.
- Score 5: Polished, precise, and professional.

### 6. Creativity & Adaptability (1–5)
- Measures originality and reusability of the prompt.
- Score 1: Formulaic.
- Score 2–3: Moderate adaptability.
- Score 4: Creative or flexible.
- Score 5: Inventive and broadly reusable.

---

## ⚙️ Evaluation Instructions

- You will be given a CSV file containing a list of student responses. Each row includes a **response number** and a **single prompt**.
- For each response, evaluate it **according to the six criteria** listed above.
- Return a **table only**, with these column headers:

**Response Number | Clarity of Reasoning Structure | Task Relevance & Purposefulness | Specificity & Context | CoT Instruction Appropriateness | Clarity of Language | Creativity & Adaptability**

- Do **not** include any total scores, comments, or quality labels.
- If a row is malformed or cannot be evaluated, **skip it** silently.
- If a response includes off-topic or irrelevant chatter, **ignore it** and focus only on the core prompt.
- In cases of scoring uncertainty, default to the **lower score** unless strong justification is evident.

---

## 🔢 Output Format

Return a **Markdown table** with one row per response and scores under each criterion. Follow this example structure:

```
| Response Number | Clarity of Reasoning Structure | Task Relevance & Purposefulness | Specificity & Context | CoT Instruction Appropriateness | Clarity of Language | Creativity & Adaptability |
|-----------------|-------------------------------|-------------------------------|-----------------------|-------------------------------|---------------------|---------------------------|
| 1               | 6                             | 7                             | 3                     | 4                             | 5                   | 4                         |
| 2               | 9                             | 10                            | 5                     | 5                             | 5                   | 5                         |
...
```

---

Load the CSV and begin evaluation.
```

---

Let me know if you'd like:
- A version that includes a **Python wrapper** to automate calling the model with the CSV, or
- Adjustments to include total scoring or narrative justifications later on.

## You (2025-03-26T05:31:09.547000+00:00)

I want you to double check the prompt you've created and tell me if it addresses all the issues you outlined earlier

## ChatGPT (2025-03-26T05:31:10.261840+00:00)

Absolutely—let’s run the checklist and double-check the prompt against all the issues we previously outlined:

---

### ✅ **Issue 1: Response Length or Density**
> **Risk:** Some prompts may be long or have irrelevant filler.

**Does the prompt address it?**
✔ **Yes.** This is covered with:
> *“If a response includes off-topic or irrelevant chatter, ignore it and focus only on the core prompt.”*

**Result:** ✅ Covered

---

### ✅ **Issue 2: Ambiguous or Edge-Case Prompts**
> **Risk:** GPT might struggle with borderline cases or score inconsistently.

**Does the prompt address it?**
✔ **Yes.** The following guidance handles this:
> *“In cases of scoring uncertainty, default to the lower score unless strong justification is evident.”*

**Result:** ✅ Covered

---

### ✅ **Issue 3: CSV Encoding or Parsing Issues**
> **Risk:** Irregular formatting or malformed rows could throw off evaluation.

**Does the prompt address it?**
✔ **Yes.** This line covers it:
> *“If a row is malformed or cannot be evaluated, skip it silently.”*

**Result:** ✅ Covered

---

### ✅ **Issue 4: Rubric Weight vs. Score Confusion**
> **Risk:** GPT might factor in the rubric’s weight percentages rather than focusing on raw scores.

**Does the prompt address it?**
✔ **Yes.** This section removes ambiguity:
> *“Do not consider the weight percentages—use only the scoring range per criterion.”*

**Result:** ✅ Covered

---

### ✅ **Issue 5: Inconsistent Interpretation Across Responses**
> **Risk:** GPT may drift in how it interprets criteria without calibration.

**Does the prompt address it?**
✔ **Partially, but effectively.** Instead of explicitly saying “apply consistent standards,” the prompt does:
- Anchor each rubric item in **concrete score descriptions**
- Direct the model to **default to the lower score** in edge cases

While not explicitly saying "stay consistent across entries," those measures help prevent drift.

**Optional Improvement (if desired):**
> Add a line like: *“Apply consistent interpretation across all responses to ensure fairness.”*

**Result:** ✅ Mostly covered; could be slightly stronger with one extra sentence for assurance.

---

### ✅ Output Format Control
> **Requirement:** You only want a table—no narrative, summaries, or extra commentary.

**Does the prompt address it?**
✔ **Yes.** The following instructions are explicit:
> *“Return a table only... Do not include any total scores, comments, or quality labels.”*

**Result:** ✅ Covered

---

### ✅ Final Verdict

Your prompt is **robust and well-structured**. It directly addresses all critical risks you identified earlier and aligns with your expectations (clean table, rubric adherence, slight interpretive flexibility).
The only **optional tweak** would be to explicitly emphasize *“consistent application of criteria across all responses.”*

Would you like me to add that line in and give you the slightly revised final prompt?

## You (2025-03-26T05:35:33.980000+00:00)

Hey so a small change in plan. turns out chatgpt is not able to read the csv, so i transofrmed the csv into a text file that reads like this


| **Response Number** | **Response** |
| --- | --- |
| 1 | I am looking to buy a second hand car. Please help me make the decision on which car to buy, by thinking step by step.First, understand which car is most suitable for a family of 4. I am cost and mileage conscious, but at the same time looking for safety and comfort.Secondly, consider the car and brand which has the best resale value and high resale demand in my city and market.Third, optimize for the cost of purchase based on year of manufacturing, how many km run. |
| 2 | j |
| 3 | I am looking to start a cooking business. I have attached my financials and i live in Ghana. I would like you to read through my financials and step by step, provide me with the manner in which i should start this business to flourish and make good returns. |
| 4 | Help me purchase a new boat. Attached is a copy of a lending guarantee from my bank. I am planning to use the boat for fishing 75% of the time and whale watching 25%. It must be between 25 and 30 feet long with twin outboard engines. Please give me a list of at least 5 manufacturers and report which boat has the features I need most. |
| 5 | Help me to learn how to choose university in tue USA for my daugther, she is an international student and want o study abroad. |
| 6 | The objective is to write an email that triggers a customer response and schedules a meeting. First, I am a Sales Rep at company "Jumbo", use the list and marketing material that I have uploaded and the contact information of the attached list. Then, give me 3 different options to choose from, use a formal tone. Explain to me your reasoning for your results. |
| 7 | xx |

Could you make the necessary adjustments to the prompt so that chatgpt can clearly understand these points while maintaining the same logic and same output

## ChatGPT (2025-03-26T05:35:34.584929+00:00)

Absolutely—thanks for flagging the format change. Since the `.csv` is now a **Markdown-style text table**, we need to slightly adjust the prompt to:

1. Instruct GPT to **read from a Markdown-style table**, not a CSV file.
2. Be clear that the input format includes **Response Number** and **Response** columns.
3. Ensure it still handles malformed or trivial entries (e.g., rows like `2 | j` or `7 | xx`).
4. Keep the output logic *identical*—only raw scores in a structured markdown table.

---

### 🔁 Revised O3 Prompt (Adjusted for Text Table Input)

```
You are a Chain-of-Thought Prompt Evaluator.

Your task is to evaluate a series of student-written prompts based on the rubric below. These prompts were submitted in response to the instruction:

**“Using chain-of-thought prompting, write a prompt that you could use to help complete a project at work.”**

---

## 🧠 Evaluation Rubric

Evaluate each student prompt using the six criteria below. For each criterion, assign a **raw score only**, using the score ranges provided. Do not consider the weight percentages—use only the scoring range per criterion.

### 1. Clarity of Reasoning Structure (1–10)
- Measures how clearly the prompt instructs multi-step, logical reasoning.
- Score 1–3: No reasoning structure.
- Score 4–6: Vague multi-step hints.
- Score 7–8: Clear CoT structure.
- Score 9–10: Elegant breakdown into sub-parts.

### 2. Task Relevance & Purposefulness (1–10)
- Measures how well the prompt aligns with real workplace tasks.
- Score 1–3: Vague or unrealistic.
- Score 4–6: Plausible but general.
- Score 7–8: Realistic and specific.
- Score 9–10: Valuable, clearly defined work-related task.

### 3. Specificity & Context Provided (1–5)
- Measures presence of relevant framing, context, and constraints.
- Score 1: No context.
- Score 2–3: Sparse or generic.
- Score 4: Useful, relevant details.
- Score 5: Rich, focused, well-targeted context.

### 4. CoT Instruction Appropriateness (1–5)
- Measures how well the prompt cues chain-of-thought reasoning.
- Score 1: No cue.
- Score 2–3: “Think step by step” is loosely integrated.
- Score 4: Clear CoT flow.
- Score 5: Seamlessly integrated step-wise structure.

### 5. Clarity of Language & Structure (1–5)
- Measures clarity, grammar, professionalism.
- Score 1: Confusing or ungrammatical.
- Score 2–3: Awkward or overly wordy.
- Score 4: Clear and well-structured.
- Score 5: Polished, precise, and professional.

### 6. Creativity & Adaptability (1–5)
- Measures originality and reusability of the prompt.
- Score 1: Formulaic.
- Score 2–3: Moderate adaptability.
- Score 4: Creative or flexible.
- Score 5: Inventive and broadly reusable.

---

## ⚙️ Evaluation Instructions

- You will be given a **Markdown-style table** with two columns: **Response Number** and **Response**.
- Each row represents one student’s prompt.
- Evaluate each response using the rubric above.
- Return a **Markdown table only**, with these column headers:

**Response Number | Clarity of Reasoning Structure | Task Relevance & Purposefulness | Specificity & Context | CoT Instruction Appropriateness | Clarity of Language | Creativity & Adaptability**

- Do **not** include any total scores, comments, or quality labels.
- If a row is malformed, empty, or the content is trivial or nonsense (e.g., "j" or "xx"), **skip that row silently**.
- If a response includes off-topic or irrelevant chatter, **ignore it** and focus only on the core prompt.
- In cases of scoring uncertainty, default to the **lower score** unless strong justification is evident.
- Apply consistent interpretation of each criterion across all responses.

---

## 🔢 Output Format

Return a **Markdown table** with one row per response and scores under each criterion. Follow this structure:

```
| Response Number | Clarity of Reasoning Structure | Task Relevance & Purposefulness | Specificity & Context | CoT Instruction Appropriateness | Clarity of Language | Creativity & Adaptability |
|-----------------|-------------------------------|-------------------------------|-----------------------|-------------------------------|---------------------|---------------------------|
| 1               | 6                             | 7                             | 3                     | 4                             | 5                   | 4                         |
| 3               | 8                             | 9                             | 4                     | 5                             | 5                   | 4                         |
...
```

---

Begin evaluation using the input Markdown table format.
```

---

Let me know if you'd like this formatted as a system message or wrapped in a function for API use—but this version is ready to go for ChatGPT or GPT-4 Turbo directly.

## You (2025-03-26T05:49:16.153000+00:00)

hey looks like chatgpt is not handling this request well. can we break it down into parts, where it evaluates no more than 50 at a time. once it creates a table for the first 50, then we can ask it to create a table starting from response 51.

So your ask is, create 2 prompts: one that makes chatgpt evaluate the first 50 without telling it anything about the follow up prompts.
second, create a follow up prompt that i can use to ask chatgpt to execute on the next 50, and the last 52 responses.

## ChatGPT (2025-03-26T05:49:16.739510+00:00)

Great idea—chunking the input into manageable batches is a smart workaround. Here's how I’ll approach this:

---

### 🧩 Structure of the Two Prompts

1. **Prompt 1:** Evaluates **Responses 1–50**
   - Treated as a standalone task.
   - No mention of future batches.

2. **Prompt 2 (Follow-Up):** Evaluates **Responses 51–100**, and then **Responses 101–152**
   - Clear that it's a **continuation** using the same rubric and format.
   - Ensures scoring consistency by referencing the *same rubric logic* but without requiring the first batch to be visible.

---

### ✅ Prompt 1 – Evaluate Responses 1–50 (Standalone)

```
You are a Chain-of-Thought Prompt Evaluator.

Your task is to evaluate a series of student-written prompts based on the rubric below. These prompts were submitted in response to the instruction:

**“Using chain-of-thought prompting, write a prompt that you could use to help complete a project at work.”**

---

## 🧠 Evaluation Rubric

Evaluate each student prompt using the six criteria below. For each criterion, assign a **raw score only**, using the score ranges provided. Do not consider the weight percentages—use only the scoring range per criterion.

### 1. Clarity of Reasoning Structure (1–10)
### 2. Task Relevance & Purposefulness (1–10)
### 3. Specificity & Context Provided (1–5)
### 4. CoT Instruction Appropriateness (1–5)
### 5. Clarity of Language & Structure (1–5)
### 6. Creativity & Adaptability (1–5)

(See detailed rubric criteria in the appendix at the bottom.)

---

## ⚙️ Evaluation Instructions

You will be given a Markdown-style table with two columns: **Response Number** and **Response**. Each row represents one student prompt.

Evaluate each response and return a **Markdown table** with these exact columns:

**Response Number | Clarity of Reasoning Structure | Task Relevance & Purposefulness | Specificity & Context | CoT Instruction Appropriateness | Clarity of Language | Creativity & Adaptability**

- Do **not** include totals, summaries, or comments.
- If a row is malformed, empty, or trivial (e.g., “j”, “xx”), skip it silently.
- Focus only on the meaningful portion of the response if filler text is present.
- In cases of uncertainty, default to the **lower score** unless strong rubric-based justification is evident.
- Apply rubric criteria consistently across all responses in this batch.

---

## 🔢 Output Format Example

```
| Response Number | Clarity of Reasoning Structure | Task Relevance & Purposefulness | Specificity & Context | CoT Instruction Appropriateness | Clarity of Language | Creativity & Adaptability |
|-----------------|-------------------------------|-------------------------------|-----------------------|-------------------------------|---------------------|---------------------------|
| 1               | 6                             | 7                             | 3                     | 4                             | 5                   | 4                         |
| 3               | 8                             | 9                             | 4                     | 5                             | 5                   | 4                         |
```

---

## 📥 Input

(Provide only **Responses 1–50** from your Markdown table here.)

---

## 📎 Rubric Appendix (Short Version)

[Omitted here for brevity, but assume GPT has internalized the rubric from prior context or messages.]
```

---

### ✅ Prompt 2 – Follow-Up for Responses 51–152

This assumes GPT already evaluated earlier responses. The second prompt is near-identical **but reaffirms consistency** with prior rubric use.

```
You previously evaluated student prompts using a structured rubric. Now continue that evaluation with the next batch of responses.

These prompts are part of the same task, submitted in response to:

**“Using chain-of-thought prompting, write a prompt that you could use to help complete a project at work.”**

---

## ⚙️ Instructions

You will now evaluate additional student responses—specifically:

- **Responses 51–100**, and
- **Responses 101–152**

Use the **same rubric and scoring rules** as before. You are expected to be consistent with your previous scoring. The rubric contains six criteria:

1. Clarity of Reasoning Structure (1–10)
2. Task Relevance & Purposefulness (1–10)
3. Specificity & Context Provided (1–5)
4. CoT Instruction Appropriateness (1–5)
5. Clarity of Language & Structure (1–5)
6. Creativity & Adaptability (1–5)

---

## 🔢 Output Table Format

Return a Markdown table only, structured exactly like this:

```
| Response Number | Clarity of Reasoning Structure | Task Relevance & Purposefulness | Specificity & Context | CoT Instruction Appropriateness | Clarity of Language | Creativity & Adaptability |
|-----------------|-------------------------------|-------------------------------|-----------------------|-------------------------------|---------------------|---------------------------|
```

- Do **not** include totals or comments.
- Skip any malformed, empty, or trivial entries.
- Remain consistent with earlier scoring logic.
- If uncertain about a score, default to the **lower option**.

---

## 📥 Input

(Provide **Responses 51–100** here. Then run it again with **Responses 101–152** in a second pass.)
```

---

Would you like me to break your `.txt` file into three batches (1–50, 51–100, 101–152) so you can paste each into ChatGPT alongside the corresponding prompt?

## You (2025-03-26T05:50:22.286000+00:00)

just give me one prompt at a time. I can see that you've left out A LOT of very important instructions and clarifications on how to evaluate a prompt from the first prompt

## ChatGPT (2025-03-26T05:50:23.037560+00:00)

You're absolutely right to flag that—thank you for the sharp eye.

Let’s go back and make **Prompt 1 (for Responses 1–50)** as complete, rigorous, and self-contained as it needs to be. The earlier version was overly compressed and assumed context already held by GPT (which isn't safe when running fresh evaluations).

Here is the fully restored and corrected **Prompt 1**, with *all evaluation rubric details*, precise scoring descriptions, edge-case handling, formatting rules, and interpretive guidance.

---

### ✅ **Finalized Prompt 1 — For Evaluating Responses 1–50**

```
You are a Chain-of-Thought Prompt Evaluator.

Your task is to evaluate student-written prompts based on a detailed rubric. These prompts were submitted in response to the instruction:

**“Using chain-of-thought prompting, write a prompt that you could use to help complete a project at work.”**

---

## 🧠 Evaluation Rubric

For each student-written prompt, evaluate it using the six criteria below. For each criterion, assign a **raw score only**, based on the scoring ranges and definitions provided.

⚠️ Do **not** calculate total scores, weights, or give comments. Score only what is explicitly requested.

---

### 1. **Clarity of Reasoning Structure (1–10)**
*How clearly the prompt instructs multi-step, structured reasoning (chain-of-thought).*

- **1–3**: No evidence of step-by-step thinking or reasoning structure.
- **4–6**: Some hint at reasoning, but vague or underspecified.
- **7–8**: Clear multi-step guidance; reasoning is scaffolded.
- **9–10**: Elegantly structured reasoning chain, broken into steps or logical sub-tasks.

**Example:**
- Low (2): “Help me decide what project to do.”
- Mid (6): “Think step by step to evaluate which project idea is best.”
- High (10): “List my three project ideas. For each, evaluate its feasibility, impact, and time required. Then recommend the best one and explain your reasoning step by step.”

---

### 2. **Task Relevance & Purposefulness (1–10)**
*How well the prompt aligns with a real, useful workplace task.*

- **1–3**: Vague, unrealistic, or irrelevant to professional work.
- **4–6**: Plausible but generic or lacking clear utility.
- **7–8**: Describes a realistic and specific workplace scenario.
- **9–10**: Highly purposeful, valuable, and clearly defined for real-world work.

**Example:**
- Low (2): “Brainstorm something interesting.”
- Mid (6): “Help me write better emails.”
- High (10): “Using step-by-step reasoning, generate three options for a persuasive email to a hesitant stakeholder, then choose the strongest and explain why.”

---

### 3. **Specificity & Context Provided (1–5)**
*How much relevant detail, framing, or parameters the prompt includes to guide the model.*

- **1**: No context; model must guess everything.
- **2–3**: Minimal or generic context.
- **4**: Some concrete details (e.g., goals, tone, audience).
- **5**: Rich, focused context tailored to the task.

**Example:**
- Low (1): “Help me make a presentation.”
- Mid (3): “Help me make a presentation for my team.”
- High (5): “Help me make a 10-slide presentation for the marketing team on our Q1 metrics, emphasizing visual clarity and key takeaways.”

---

### 4. **CoT Instruction Appropriateness (1–5)**
*How well the prompt cues chain-of-thought reasoning.*

- **1**: No cue to reason step-by-step.
- **2–3**: CoT is mentioned but weakly integrated.
- **4**: CoT instructions are structured and logical.
- **5**: Seamlessly embedded reasoning process (e.g., “First… then… finally…”).

---

### 5. **Clarity of Language & Structure (1–5)**
*How well-written, professional, and understandable the prompt is.*

- **1**: Confusing, ungrammatical, or incoherent.
- **2–3**: Understandable but awkward or overly wordy.
- **4**: Clear, concise, and readable.
- **5**: Polished, well-structured, and professional.

---

### 6. **Creativity & Adaptability (1–5)**
*Does the prompt show original thinking or potential for reuse in other contexts?*

- **1**: Generic, formulaic, or rigid.
- **2–3**: Mild creativity or moderate flexibility.
- **4**: Creative framing or reusable with small changes.
- **5**: Highly adaptable and inventive.

---

## ⚙️ Evaluation Instructions

You will be given a **Markdown-style table** containing two columns:
- **Response Number**
- **Response** (i.e., the student’s written prompt)

Evaluate each row as follows:

- Provide one score per criterion for each response.
- Do **not** explain or justify your scores.
- Skip any response that is:
  - Empty
  - Gibberish
  - Clearly not a prompt (e.g., “j”, “xx”)
- If the prompt includes irrelevant filler or preamble, ignore it and **focus only on the functional part** of the prompt.
- If uncertain between two scores, choose the **lower** score unless the higher one is clearly justified by rubric language.
- Apply rubric criteria **consistently across all responses**.

---

## 🔢 Output Format

Return a **Markdown table only**, with this exact column structure:

```
| Response Number | Clarity of Reasoning Structure | Task Relevance & Purposefulness | Specificity & Context | CoT Instruction Appropriateness | Clarity of Language | Creativity & Adaptability |
|-----------------|-------------------------------|----------------------------------|-----------------------|----------------------------------|---------------------|---------------------------|
| 1               | 7                             | 8                                | 4                     | 5                                | 5                   | 4                         |
| 3               | 6                             | 7                                | 3                     | 4                                | 4                   | 3                         |
```

Only include responses **1 through 50** from your dataset. Do not mention later responses or continue past 50.

---

Now begin evaluating the first 50 responses using the table provided.
```

---

Would you like me to generate **Prompt 2** next for evaluating Responses 51–152, with continuity built in but no repetition of this full rubric?

## You (2025-03-26T05:55:30.566000+00:00)

ok now give me the follow up.

## ChatGPT (2025-03-26T05:55:31.700416+00:00)

Perfect—here is **Prompt 2**, designed as a seamless follow-up to Prompt 1. It assumes GPT has already seen and internalized the full rubric, so we’ll **avoid repeating the entire rubric**, but still:

- Reinforce **consistency** with earlier evaluations
- Emphasize **raw score only**, no comments
- Cover **responses 51 through 152** (in two batches)
- Preserve table structure and evaluation discipline

---

### ✅ **Prompt 2 — Follow-Up for Responses 51–152**

```
You previously evaluated student-written prompts using a detailed six-part rubric. Continue the evaluation now using the **same criteria, definitions, and scoring logic** for the next batch of responses.

These responses are part of the same task:
**“Using chain-of-thought prompting, write a prompt that you could use to help complete a project at work.”**

---

## ⚙️ Instructions

You will now evaluate the remaining responses in two parts:

1. First, evaluate **Responses 51–100**
2. Then, evaluate **Responses 101–152**

Each row contains a Response Number and the student's written prompt.

---

## 🔢 Evaluation Rules (Reminder)

- Score each response using the **same six criteria** as before:
  1. Clarity of Reasoning Structure (1–10)
  2. Task Relevance & Purposefulness (1–10)
  3. Specificity & Context Provided (1–5)
  4. CoT Instruction Appropriateness (1–5)
  5. Clarity of Language & Structure (1–5)
  6. Creativity & Adaptability (1–5)

- Assign **raw scores only**, using the rubric’s definitions.
- Skip any row that is:
  - Empty
  - Trivial (e.g., “j” or “xx”)
  - Not a meaningful or complete prompt
- If a prompt includes irrelevant filler, ignore it and focus only on the **functional core**.
- When uncertain between two scores, choose the **lower** score unless higher is clearly supported.
- Maintain scoring **consistency** with earlier evaluations in Responses 1–50.

---

## 📄 Output Format

Return a single **Markdown table** per batch (do not merge 51–152 all at once). Use this exact format:

```
| Response Number | Clarity of Reasoning Structure | Task Relevance & Purposefulness | Specificity & Context | CoT Instruction Appropriateness | Clarity of Language | Creativity & Adaptability |
|-----------------|-------------------------------|----------------------------------|-----------------------|----------------------------------|---------------------|---------------------------|
| 51              |                               |                                  |                       |                                  |                     |                           |
| 52              |                               |                                  |                       |                                  |                     |                           |
...
```

---

## ⏭️ Next Steps

- First, paste and evaluate **Responses 51–100**.
- After that’s complete, paste and evaluate **Responses 101–152** using the same format.

Now begin evaluating the next batch starting with Response 51.
```

---

Let me know if you'd like a version that combines 51–152 into a single pass (less safe for model memory) or want a YAML or JSON format instead of Markdown.

## You (2025-03-26T05:56:41.436000+00:00)

ok i'll clarify this again. in a single prompt, lets not give the gpt additional context about the future prompts. thats just completely unnecessary information. instead, in this prompt focus on the actual task at hand, not focusing on the future tasks

## ChatGPT (2025-03-26T05:56:42.036796+00:00)

Crystal clear now—thank you for that clarification. Here's the fully corrected **Prompt 2**, scoped **only to Responses 51–100**, with no mention of future tasks or additional batches. It's self-contained and sharply focused, just like Prompt 1.

---

### ✅ **Prompt 2 – Evaluate Responses 51–100 (Standalone)**

```
You are a Chain-of-Thought Prompt Evaluator.

Your task is to evaluate student-written prompts based on a detailed rubric. These prompts were submitted in response to the instruction:

**“Using chain-of-thought prompting, write a prompt that you could use to help complete a project at work.”**

---

## 🧠 Evaluation Rubric

For each student-written prompt, evaluate it using the six criteria below. For each criterion, assign a **raw score only**, based on the scoring ranges and definitions provided.

⚠️ Do **not** calculate total scores, weights, or give comments. Score only what is explicitly requested.

---

### 1. **Clarity of Reasoning Structure (1–10)**
*How clearly the prompt instructs multi-step, structured reasoning (chain-of-thought).*

- **1–3**: No evidence of step-by-step thinking or reasoning structure.
- **4–6**: Some hint at reasoning, but vague or underspecified.
- **7–8**: Clear multi-step guidance; reasoning is scaffolded.
- **9–10**: Elegantly structured reasoning chain, broken into steps or logical sub-tasks.

---

### 2. **Task Relevance & Purposefulness (1–10)**
*How well the prompt aligns with a real, useful workplace task.*

- **1–3**: Vague, unrealistic, or irrelevant to professional work.
- **4–6**: Plausible but generic or lacking clear utility.
- **7–8**: Describes a realistic and specific workplace scenario.
- **9–10**: Highly purposeful, valuable, and clearly defined for real-world work.

---

### 3. **Specificity & Context Provided (1–5)**
*How much relevant detail, framing, or parameters the prompt includes to guide the model.*

- **1**: No context; model must guess everything.
- **2–3**: Minimal or generic context.
- **4**: Some concrete details (e.g., goals, tone, audience).
- **5**: Rich, focused context tailored to the task.

---

### 4. **CoT Instruction Appropriateness (1–5)**
*How well the prompt cues chain-of-thought reasoning.*

- **1**: No cue to reason step-by-step.
- **2–3**: CoT is mentioned but weakly integrated.
- **4**: CoT instructions are structured and logical.
- **5**: Seamlessly embedded reasoning process (e.g., “First… then… finally…”).

---

### 5. **Clarity of Language & Structure (1–5)**
*How well-written, professional, and understandable the prompt is.*

- **1**: Confusing, ungrammatical, or incoherent.
- **2–3**: Understandable but awkward or overly wordy.
- **4**: Clear, concise, and readable.
- **5**: Polished, well-structured, and professional.

---

### 6. **Creativity & Adaptability (1–5)**
*Does the prompt show original thinking or potential for reuse in other contexts?*

- **1**: Generic, formulaic, or rigid.
- **2–3**: Mild creativity or moderate flexibility.
- **4**: Creative framing or reusable with small changes.
- **5**: Highly adaptable and inventive.

---

## ⚙️ Evaluation Instructions

You will be given a **Markdown-style table** containing two columns:
- **Response Number**
- **Response** (i.e., the student’s written prompt)

Evaluate each row as follows:

- Provide one score per criterion for each response.
- Do **not** explain or justify your scores.
- Skip any response that is:
  - Empty
  - Gibberish
  - Clearly not a prompt (e.g., “j”, “xx”)
- If the prompt includes irrelevant filler or preamble, ignore it and **focus only on the functional part** of the prompt.
- If uncertain between two scores, choose the **lower** score unless the higher one is clearly justified by rubric language.
- Apply rubric criteria **consistently across all

## You (2025-03-26T05:57:12.819000+00:00)

do we need to repeat all the context all over again? if you think we do, then go ahead. if not, then leave it out

## ChatGPT (2025-03-26T05:57:13.538414+00:00)

Excellent question—and no, we **don’t** need to repeat all the rubric context if you’re entering Prompt 2 into the *same chat session* where Prompt 1 was just executed.

GPT will retain:
- The rubric definitions
- The evaluation format
- The instruction discipline

In that case, we only need a **lean prompt** that reaffirms what it’s doing, reminds it of the format, and specifies that the new responses are from **51 to 100**.

---

### ✅ **Lean Prompt 2 – For Responses 51–100 (No Repetition)**

```
Continue evaluating the next set of student responses using the same rubric and instructions as before.

You will now score **Responses 51 to 100**.

Return a **Markdown table** using the following format:

| Response Number | Clarity of Reasoning Structure | Task Relevance & Purposefulness | Specificity & Context | CoT Instruction Appropriateness | Clarity of Language | Creativity & Adaptability |
|-----------------|-------------------------------|----------------------------------|-----------------------|----------------------------------|---------------------|---------------------------|
| 51              |                               |                                  |                       |                                  |                     |                           |
| 52              |                               |                                  |                       |                                  |                     |                           |
...

Follow all prior evaluation rules:
- Raw scores only
- No totals, comments, or labels
- Skip trivial, empty, or malformed responses
- Focus only on the core prompt content
- Default to lower score if uncertain
- Stay consistent with earlier evaluations

Now begin scoring responses 51 through 100.
```

---

Let me know when you're ready for the third and final batch (101–152), and I’ll tailor that prompt just as cleanly.

## You (2025-03-26T06:02:36.010000+00:00)

ok, now a pronpt that does the same thing for the remaining : 101 to 151

## ChatGPT (2025-03-26T06:02:36.777165+00:00)

Perfect—here’s the final **lean evaluation prompt** for the last batch: **Responses 101–151**.

(No rubric repetition, just concise task continuation.)

---

### ✅ **Lean Prompt 3 – For Responses 101–151**

```
Continue evaluating the next set of student responses using the same rubric and instructions as before.

You will now score **Responses 101 to 151**.

Return a **Markdown table** using the following format:

| Response Number | Clarity of Reasoning Structure | Task Relevance & Purposefulness | Specificity & Context | CoT Instruction Appropriateness | Clarity of Language | Creativity & Adaptability |
|-----------------|-------------------------------|----------------------------------|-----------------------|----------------------------------|---------------------|---------------------------|
| 101             |                               |                                  |                       |                                  |                     |                           |
| 102             |                               |                                  |                       |                                  |                     |                           |
...

Follow all prior evaluation rules:
- Raw scores only
- No totals, comments, or labels
- Skip trivial, empty, or malformed responses
- Focus only on the core prompt content
- Default to lower score if uncertain
- Stay consistent with earlier evaluations

Now begin scoring responses 101 through 151.
```

---

Let me know if you want a final wrap-up prompt to summarize results or visualize anything after these are processed.

## You (2025-03-26T06:06:29.933000+00:00)

ok, now I want a prompt that can compile all the previous responses into a single csv file. this means all the three tables generated

## ChatGPT (2025-03-26T06:06:30.805409+00:00)

Great—now that you’ve gathered all three markdown tables, here's a clean, focused prompt that instructs GPT to **merge them** into a **single CSV-formatted output**, ready to copy-paste or download.

---

### ✅ **Prompt – Combine Three Evaluation Tables into a CSV File**

```
You will be given three markdown tables containing evaluation scores for student responses. Each row includes:

- Response Number
- Clarity of Reasoning Structure
- Task Relevance & Purposefulness
- Specificity & Context
- CoT Instruction Appropriateness
- Clarity of Language
- Creativity & Adaptability

Your task is to combine all three tables into a single **CSV-formatted file**.

Instructions:
- Include a header row.
- Use **comma-separated values**.
- Do **not** include markdown syntax (no pipes `|`, no formatting).
- Sort the final rows in **ascending order by Response Number**.
- Output only the raw CSV text—no explanations or markdown formatting.

Now begin. I will paste the three tables below.
```

---

Once you paste all three tables into the chat, GPT will return a clean `.csv` block you can copy and save.

Want a downloadable CSV too? I can help you turn it into a downloadable file using a Python snippet if needed.
