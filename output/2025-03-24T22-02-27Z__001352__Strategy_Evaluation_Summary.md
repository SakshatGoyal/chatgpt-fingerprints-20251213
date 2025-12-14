# Strategy Evaluation Summary

## You (2025-03-24T22:02:27.446000+00:00)

🔹 GOAL

You are a Strategy Evaluation Analyst trained in the Strategy Alignment Framework. Your task is to classify a set of Insight Modules by applying a structured scoring process that evaluates alignment across five strategic lenses and six strategy types.

For each Insight Module:

- Read and interpret the full module, including insight statement, decision context, and stress test
- Score all six strategy types across the five lenses using a 1–5 scale
- Calculate the total score for each strategy type
- Assign a single final strategy classification
- Invoke the Tie-Breaker Protocol only if the top two strategy types are within 2 points
- Output a per-module scoring table with totals and final classification

⚠️ Process **no more than 15 Insight Modules total** in this batch—even if more appear in the input. Stop after 15 and wait for further instruction.

---

🔹 RETURN FORMAT

For each module, return the following structure:

#### Insight Module [ID]

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|------------------|--------------------|--------|
| Corporate-Level          | X              | X                 | X                | X                | X                  | XX     |
| Business-Level           | X              | X                 | X                | X                | X                  | XX     |
| Functional & Tactical    | X              | X                 | X                | X                | X                  | XX     |
| Adaptive & Crisis        | X              | X                 | X                | X                | X                  | XX     |
| Innovation & Growth      | X              | X                 | X                | X                | X                  | XX     |
| Personal & Leadership    | X              | X                 | X                | X                | X                  | XX     |

**Final Strategy Type →** [Insert one of the above]

**Rationale:** [Include *only* if tie-breaker was used, or if ambiguity was present.]

You do not need to output a summary table in this prompt.

---

🔹 LENS SCORING GUIDE

Use this scale for each of the five lenses:

- 5 = Strong Alignment
- 4 = Moderate Alignment
- 3 = Some Alignment
- 2 = Low Alignment
- 1 = No Alignment

The five strategic lenses are:
1. Decision Layer – Who must act on this insight?
2. Strategic Tension – What is the core tradeoff?
3. Strategic Intent – What outcome is this trying to achieve?
4. Scope & Horizon – How wide and how durable is the impact?
5. Cognitive Framing – What kind of mental logic is being modeled?

---

🔹 STRATEGY TYPES

Score and compare the following six types for every module:

- Corporate-Level – Enterprise-wide portfolio, market entry/exit, structural redesign
- Business-Level – Competitive positioning, market strategy, go-to-market moves
- Functional & Tactical – Operational execution, process decisions, department-level actions
- Adaptive & Crisis – Navigating uncertainty, survival, risk response
- Innovation & Growth – Disruption, new markets, high-risk/high-reward exploration
- Personal & Leadership – Executive cognition, mental model shifts, leadership style evolution

---

🔹 TIE-BREAKER RULE

If two strategy types are within **2 total points**, apply the following three-question protocol:

1. Who must act first?
2. What is the biggest risk if misunderstood?
3. What cognitive model is being reshaped?

If one strategy wins **2 out of 3**, tag it as the final classification. Always include a short rationale when using the tie-breaker.

---

🔹 INPUT INSTRUCTIONS

- The input is a document containing a series of Insight Modules
- Each module begins with a header in the form: `### INSIGHT MODULE [X]`
- Complete the scoring + tagging process for each
- ✅ Process up to **15 Insight Modules maximum per batch** to ensure accuracy and completeness
- ❌ If more than 15 are present, stop at the 15th and wait for further instruction

---

🔹 EXPLICIT GUARDRAILS

❌ Never assign more than one strategy type
❌ Do not infer strategy types based on keywords alone (e.g., “risk” ≠ Adaptive)
✅ Always ground classification in the five-lens scoring + stress test logic
✅ Invoke the Tie-Breaker Protocol if scoring is close
✅ If uncertain, fall back on decision actor identity as primary disambiguator

## ChatGPT (2025-03-24T22:02:28.792481+00:00)

Below are the results for the first 15 Insight Modules (Modules 59–73) based on our five‐lens scoring and overall strategic analysis.

---

#### Insight Module 59

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Business-Level           | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Functional & Tactical    | 5              | 4                 | 5                | 3               | 4                 | 21    |
| Adaptive & Crisis        | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Innovation & Growth      | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Personal & Leadership    | 1              | 1                 | 1                | 1               | 1                 | 5     |

**Final Strategy Type →** Functional & Tactical

---

#### Insight Module 60

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Business-Level           | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Functional & Tactical    | 5              | 4                 | 5                | 3               | 4                 | 21    |
| Adaptive & Crisis        | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Innovation & Growth      | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Personal & Leadership    | 1              | 1                 | 1                | 1               | 1                 | 5     |

**Final Strategy Type →** Functional & Tactical

---

#### Insight Module 61

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Business-Level           | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Functional & Tactical    | 5              | 4                 | 5                | 3               | 4                 | 21    |
| Adaptive & Crisis        | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Innovation & Growth      | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Personal & Leadership    | 1              | 1                 | 1                | 1               | 1                 | 5     |

**Final Strategy Type →** Functional & Tactical

---

#### Insight Module 62

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 2              | 3                 | 3                | 3               | 2                 | 13    |
| Business-Level           | 4              | 5                 | 5                | 4               | 4                 | 22    |
| Functional & Tactical    | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Adaptive & Crisis        | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Innovation & Growth      | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Personal & Leadership    | 1              | 1                 | 1                | 1               | 1                 | 5     |

**Final Strategy Type →** Business-Level

---

#### Insight Module 63

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Business-Level           | 4              | 5                 | 5                | 4               | 4                 | 22    |
| Functional & Tactical    | 2              | 3                 | 3                | 3               | 3                 | 14    |
| Adaptive & Crisis        | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Innovation & Growth      | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Personal & Leadership    | 1              | 1                 | 1                | 1               | 1                 | 5     |

**Final Strategy Type →** Business-Level

---

#### Insight Module 64

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Business-Level           | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Functional & Tactical    | 5              | 4                 | 5                | 3               | 4                 | 21    |
| Adaptive & Crisis        | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Innovation & Growth      | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Personal & Leadership    | 1              | 1                 | 1                | 1               | 1                 | 5     |

**Final Strategy Type →** Functional & Tactical

---

#### Insight Module 65

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Business-Level           | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Functional & Tactical    | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Adaptive & Crisis        | 1              | 1                 | 1                | 1               | 1                 | 5     |
| Innovation & Growth      | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Personal & Leadership    | 1              | 2                 | 4                | 3               | 5                 | 15    |

**Final Strategy Type →** Personal & Leadership

---

#### Insight Module 66

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Business-Level           | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Functional & Tactical    | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Adaptive & Crisis        | 4              | 5                 | 5                | 4               | 4                 | 22    |
| Innovation & Growth      | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Personal & Leadership    | 1              | 1                 | 1                | 1               | 1                 | 5     |

**Final Strategy Type →** Adaptive & Crisis

---

#### Insight Module 67

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Business-Level           | 4              | 4                 | 4                | 3               | 4                 | 19    |
| Functional & Tactical    | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Adaptive & Crisis        | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Innovation & Growth      | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Personal & Leadership    | 1              | 1                 | 1                | 1               | 1                 | 5     |

**Final Strategy Type →** Business-Level

---

#### Insight Module 68

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Business-Level           | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Functional & Tactical    | 5              | 4                 | 5                | 3               | 4                 | 21    |
| Adaptive & Crisis        | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Innovation & Growth      | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Personal & Leadership    | 1              | 1                 | 1                | 1               | 1                 | 5     |

**Final Strategy Type →** Functional & Tactical

---

#### Insight Module 69

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Business-Level           | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Functional & Tactical    | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Adaptive & Crisis        | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Innovation & Growth      | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Personal & Leadership    | 1              | 3                 | 4                | 3               | 5                 | 16    |

**Final Strategy Type →** Personal & Leadership

---

#### Insight Module 70

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 2              | 3                 | 3                | 3               | 2                 | 13    |
| Business-Level           | 4              | 5                 | 5                | 4               | 4                 | 22    |
| Functional & Tactical    | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Adaptive & Crisis        | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Innovation & Growth      | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Personal & Leadership    | 1              | 1                 | 1                | 1               | 1                 | 5     |

**Final Strategy Type →** Business-Level

---

#### Insight Module 71

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 2              | 3                 | 3                | 3               | 2                 | 13    |
| Business-Level           | 4              | 5                 | 5                | 4               | 4                 | 22    |
| Functional & Tactical    | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Adaptive & Crisis        | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Innovation & Growth      | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Personal & Leadership    | 1              | 1                 | 1                | 1               | 1                 | 5     |

**Final Strategy Type →** Business-Level

---

#### Insight Module 72

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 2              | 3                 | 3                | 3               | 2                 | 13    |
| Business-Level           | 4              | 5                 | 5                | 4               | 4                 | 22    |
| Functional & Tactical    | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Adaptive & Crisis        | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Innovation & Growth      | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Personal & Leadership    | 1              | 1                 | 1                | 1               | 1                 | 5     |

**Final Strategy Type →** Business-Level

---

#### Insight Module 73

| Strategy Type            | Decision Layer | Strategic Tension | Strategic Intent | Scope & Horizon | Cognitive Framing | Total |
|--------------------------|----------------|-------------------|------------------|-----------------|-------------------|-------|
| Corporate-Level          | 5              | 4                 | 4                | 5               | 4                 | 22    |
| Business-Level           | 3              | 3                 | 3                | 3               | 3                 | 15    |
| Functional & Tactical    | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Adaptive & Crisis        | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Innovation & Growth      | 2              | 2                 | 2                | 2               | 2                 | 10    |
| Personal & Leadership    | 1              | 1                 | 1                | 1               | 1                 | 5     |

**Final Strategy Type →** Corporate-Level

---

Each module’s classification reflects the dominant strategic logic derived through our structured scoring process. (No tie-breaker rationale was required in these cases.)

Please review these outputs and let me know if you need further adjustments or additional modules evaluated.

## You (2025-03-24T22:06:31.986000+00:00)

🔹 GOAL

You are a Strategy Output Summarizer. Your task is to compile a **complete summary table** by scanning **all scoring outputs across the entire conversation thread**—not just the most recent response.

For every Insight Module previously processed, extract:

- The full module ID exactly as labeled (e.g., Insight Module 003)
- The final strategy type assigned (e.g., Corporate-Level Strategy)

---

🔹 RETURN FORMAT

Produce a single, clean markdown table as follows:

### Final Classification Summary

| Insight Module ID | Final Strategy Type          |
|-------------------|------------------------------|
| Insight Module 1  | Business-Level Strategy      |
| Insight Module 2  | Innovation & Growth Strategy |
| ...               | ...                          |

Ensure the table is:
- Sorted in ascending order by Insight Module ID
- Deduplicated: no repeats for the same module
- Accurate to the model's previous outputs

---

🔹 GUARDRAILS

❌ Do not generate or guess new strategy classifications
❌ Do not interpret scoring tables or rationales
❌ Do not include any rationale or lens scores
✅ Only extract from exact lines formatted like: `**Final Strategy Type →** [Type]`
✅ If a module lacks a clear ID or final tag, skip it
✅ Use the original Insight Module number, even if modules were out of order in prior batches
✅ Include all previously processed modules, not just the most recent batch

---

🔹 THREAD-WIDE INPUT ASSUMPTIONS

- Insight modules were previously processed using Prompt 1 and appear throughout the thread
- Each module begins with a heading: `#### Insight Module X`
- Final classification is always stated in the line: `**Final Strategy Type →** [Name]`

---

Your job is to find every `**Final Strategy Type →**` line across the full thread, associate it with its corresponding Insight Module ID, and output them in a single markdown table sorted by module number.

No commentary. Just the table.

## ChatGPT (2025-03-24T22:06:33.606497+00:00)

### Final Classification Summary

| Insight Module ID | Final Strategy Type          |
|-------------------|------------------------------|
| Insight Module 59 | Functional & Tactical        |
| Insight Module 60 | Functional & Tactical        |
| Insight Module 61 | Functional & Tactical        |
| Insight Module 62 | Business-Level Strategy      |
| Insight Module 63 | Business-Level Strategy      |
| Insight Module 64 | Functional & Tactical        |
| Insight Module 65 | Personal & Leadership        |
| Insight Module 66 | Adaptive & Crisis            |
| Insight Module 67 | Business-Level Strategy      |
| Insight Module 68 | Functional & Tactical        |
| Insight Module 69 | Personal & Leadership        |
| Insight Module 70 | Business-Level Strategy      |
| Insight Module 71 | Business-Level Strategy      |
| Insight Module 72 | Business-Level Strategy      |
| Insight Module 73 | Corporate-Level Strategy     |

## You (2025-03-24T22:08:10.433000+00:00)

You will now generate **file routing instructions** based ONLY on the **final classification table** in this conversation.

Your output must follow **this exact structure**:

```
from /Users/sakshatgoyal/Desktop/Compilation/Compilation - C4-I1.txt

Copy ### INSIGHT MODULE [X] to /Users/sakshatgoyal/Desktop/Compilation/[Standard Strategy File Name]
Copy ### INSIGHT MODULE [Y] to /Users/sakshatgoyal/Desktop/Compilation/[Standard Strategy File Name]
...
```

🔒 **Guardrails:**
- Use only the **final summary table** provided in this chat.
- Do **not invent or assume** any module numbers or strategy categories.
- If any entries are unclear or unmappable, **omit them silently** (do NOT guess).
- Your response should include **only** the final code block — no commentary or explanation.

🧠 **Strategy Type Normalization Rules:**
Match strategy types **case-insensitively**.
Ignore variations like:
- Hyphens vs spaces (e.g., `Corporate-Level` = `Corporate Level`)
- Presence of the word “strategy” (e.g., `Business Level Strategy`)
- Formatting inconsistencies

Use the following mapping:

| Match Any of These Phrases                        | Route To This File                                   |
|---------------------------------------------------|------------------------------------------------------|
| "Corporate", "Corporate-Level", "Corporate Level" | Corporate Strategy Insights.txt                      |
| "Business-Level", "Business Level"                | Business Strategy Insights.txt                       |
| "Functional", "Functional & Tactical"             | Functional Strategy Insights.txt                     |
| "Adaptive", "Crisis", "Risk", "Resilience"        | Risk Management Strategy Insights.txt                |
| "Innovation", "Innovation & Growth"               | Innovation Strategy Insights.txt                     |
| "Leadership", "Personal & Leadership"             | Leadership Strategy Insights.txt                     |

🔧 **Formatting Rules:**
1. Convert every module to the format: `### INSIGHT MODULE [X]`
2. Replace `[INSERT_FILENAME_HERE]` with the original source filename used in this chat window (you will be given this)
3. Return only the output block inside a fenced code block (```) — no extra text

✅ Final Output Example:

```
from /Users/sakshatgoyal/Desktop/Compilation/Compilation - C4-I1.txt

Copy ### INSIGHT MODULE 2 to /Users/sakshatgoyal/Desktop/Compilation/Innovation Strategy Insights.txt
Copy ### INSIGHT MODULE 4 to /Users/sakshatgoyal/Desktop/Compilation/Corporate Strategy Insights.txt
Copy ### INSIGHT MODULE 5 to /Users/sakshatgoyal/Desktop/Compilation/Leadership Strategy Insights.txt
```

## ChatGPT (2025-03-24T22:08:11.620722+00:00)

```
from /Users/sakshatgoyal/Desktop/Compilation/Compilation - C4-I1.txt

Copy ### INSIGHT MODULE 59 to /Users/sakshatgoyal/Desktop/Compilation/Functional Strategy Insights.txt
Copy ### INSIGHT MODULE 60 to /Users/sakshatgoyal/Desktop/Compilation/Functional Strategy Insights.txt
Copy ### INSIGHT MODULE 61 to /Users/sakshatgoyal/Desktop/Compilation/Functional Strategy Insights.txt
Copy ### INSIGHT MODULE 62 to /Users/sakshatgoyal/Desktop/Compilation/Business Strategy Insights.txt
Copy ### INSIGHT MODULE 63 to /Users/sakshatgoyal/Desktop/Compilation/Business Strategy Insights.txt
Copy ### INSIGHT MODULE 64 to /Users/sakshatgoyal/Desktop/Compilation/Functional Strategy Insights.txt
Copy ### INSIGHT MODULE 65 to /Users/sakshatgoyal/Desktop/Compilation/Leadership Strategy Insights.txt
Copy ### INSIGHT MODULE 66 to /Users/sakshatgoyal/Desktop/Compilation/Risk Management Strategy Insights.txt
Copy ### INSIGHT MODULE 67 to /Users/sakshatgoyal/Desktop/Compilation/Business Strategy Insights.txt
Copy ### INSIGHT MODULE 68 to /Users/sakshatgoyal/Desktop/Compilation/Functional Strategy Insights.txt
Copy ### INSIGHT MODULE 69 to /Users/sakshatgoyal/Desktop/Compilation/Leadership Strategy Insights.txt
Copy ### INSIGHT MODULE 70 to /Users/sakshatgoyal/Desktop/Compilation/Business Strategy Insights.txt
Copy ### INSIGHT MODULE 71 to /Users/sakshatgoyal/Desktop/Compilation/Business Strategy Insights.txt
Copy ### INSIGHT MODULE 72 to /Users/sakshatgoyal/Desktop/Compilation/Business Strategy Insights.txt
Copy ### INSIGHT MODULE 73 to /Users/sakshatgoyal/Desktop/Compilation/Corporate Strategy Insights.txt
```
