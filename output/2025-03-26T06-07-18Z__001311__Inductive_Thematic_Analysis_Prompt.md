# Inductive Thematic Analysis Prompt

## You (2025-03-26T06:07:18.214000+00:00)

Help me write a prompt. I’m going to explain my purpose, and help me write an effective prompt based on the purpose i outline here —

I need a chatgpt to think like a creative director at IDEO with years of experience turning abstract, open ended user feedback into actionable insights. I need this chatgpt to create a report for a product team building generative AI products. 

I will be attaching a .txt file which has two things

1. a question that was asked users
2. a long list of responses from different people

the responses will be seperated like so:

[user response to the question]

---

[user response to the question]

---

[user response to the question]

---

First, i want the gpt to follow an inductive thematic analysis approach to identify themes. 

In inductive thematic analysis, a person approaches their data with an open mind, free from predetermined categories or theoretical biases. They carefully and repeatedly engage with the data, allowing patterns and themes to emerge naturally. This method helps them discover new insights that existing theories might miss. It is important for them to maintain reflexivity to accurately represent the participants’ experiences and meanings.

i need the gpt to also produce some explaination for how these themes are derived and what they mean, along with a few quoted examples. 

Finally, based on the themes, it should conculde with a series of takeaways that a product team might find meaningful. the takeaways should be **“people” problems, and solution agnostic**. the product team is a strategic team trying to udnerstand how people perceive AI

## ChatGPT (2025-03-26T06:07:18.918058+00:00)

Perfect — this is a strong foundation, and your purpose is clear. Before I build the full prompt, let’s go one layer deeper with a few quick questions to surface any missing pieces and ensure the result fully meets your needs:

---

### 🔍 A Few Discovery Questions:

1. **Audience Scope:**  
   Is this prompt designed for recurring use across multiple different sets of user feedback (i.e. reusable template), or is it for a one-time analysis of a specific dataset?

2. **Report Tone and Style:**  
   What tone should the final report take — more creative and narrative (IDEO-style storytelling), academic and analytical (like a UX researcher), or business-strategic (executive-ready brief)?

3. **Depth of Analysis:**  
   Are you looking for:
   - **Surface-level** themes with quick takeaways, or  
   - **Deeper, layered** insights that explore tensions, contradictions, or behavioral drivers?

4. **Report Format:**  
   Would you like the output to be:
   - Just **themes + explanations + takeaways** (as mentioned), or  
   - Do you also want an **executive summary**, **user sentiment heatmap**, or **potential user archetypes** inferred from responses?

5. **Quoting Convention:**  
   Should quoted user responses be brief one-liners, or can GPT pull full paragraphs when helpful? Should it cite how frequently a theme appears?

6. **Constraints or Limits:**  
   Any word count limits, number of themes/takeaways, or file-size concerns?

---

Once you reply, I’ll use your answers to build a precise and powerful prompt.

If you’re good to move forward with what you’ve said already, just say **“begin building the prompt”** — and I’ll summarize the requirements and craft it for you.

## You (2025-03-26T06:12:18.934000+00:00)

Is this prompt designed for recurring use across multiple different sets of user feedback (i.e. reusable template), or is it for a one-time analysis of a specific dataset?

yes. i might use the same prompt for different text files. but each text file will have only one question, with a lot of responses


Tone: a combination of (IDEO-style storytelling), academic and analytical (like a UX researcher)

I want deeper layered insights that explore tensions, contradictions, or behavioral drivers. 

For now, i just want themes + explanations + takeaways

GPT can pull full paragraphs when helpful

Should it cite how frequently a theme appears? Yes

No limitations on word count for now. I want it to be as comprehensive yet deeply layered for now.

## ChatGPT (2025-03-26T06:12:19.730218+00:00)

Awesome. Thanks for the clarity — you're going for **deep inductive insight extraction** with a blend of **IDEO-style storytelling** and **UX-research rigor**, optimized for reuse across many datasets. You want layered analysis, contradiction-sensitive interpretation, and clear people-centered takeaways.

Let’s move forward. Here's the structure I’ll follow for the final prompt:

---

### ✅ Summary of Your Requirements (for transparency before I build the prompt):

**Primary Objective:**  
Analyze a set of user responses (from a single prompt/question) to derive inductive themes, explain them with evidence, and conclude with strategic, people-problem-oriented takeaways.

**Execution Persona for GPT-4o:**  
Creative Director at IDEO with deep UX research expertise, skilled in inductive thematic analysis, capable of blending narrative sense-making with rigorous analytical thinking.

**Desired Output Structure:**  
1. **Identified Themes:**  
   - Emergent from data (inductive, no pre-bias)  
   - Grouped meaningfully with nuanced naming  
   - Includes frequency count per theme  
   - Highlight contradictions or tensions if present

2. **Explanation for Each Theme:**  
   - How it was derived  
   - What it says about people’s thinking, assumptions, or experiences  
   - Include multiple quoted examples (short or long as needed)

3. **Final Takeaways:**  
   - Solution-agnostic insights  
   - People-centered (“what people are struggling with, perceiving, misunderstanding, desiring”)  
   - Actionable for strategic product thinking  
   - Not feature or UI-specific

**Text File Format:**  
One user question followed by multiple responses, delimited by `---`

**Tone:**  
A thoughtful, reflective, and layered mix of IDEO storytelling + UX research clarity

---

### 🧠 Now, here’s the final prompt you can use with GPT-4o:

---

**Prompt:**

You are a Creative Director at IDEO with extensive experience in human-centered design and qualitative research. You are skilled at making sense of open-ended user feedback by conducting inductive thematic analysis to identify deep patterns, tensions, and behavioral drivers in what people say.

You are analyzing the contents of a .txt file that includes:
1. A **single open-ended question** that was asked to users.
2. A long list of user responses to that question, each separated by `---`.

Your task is to conduct a **deep inductive thematic analysis** of the user responses. Approach the data with no pre-set categories or assumptions. Let the themes emerge organically from the language, tone, and patterns in what people say.

### Your Output Should Follow This Structure:

---

### **1. Emergent Themes**

- Identify 4–8 major themes (or more if justified).
- For each theme:
  - Provide a **descriptive name**.
  - Indicate **how many responses** referenced it (frequency).
  - Explain how the theme emerged from the data.
  - Point out any contradictions or behavioral tensions within the theme.
  - Include **2–4 quoted excerpts** (ranging from a few lines to full paragraphs) to illustrate the theme.

---

### **2. Final Strategic Takeaways**

- Summarize **key “people problems”** revealed by the themes.
- These should be:
  - **Solution-agnostic** (avoid recommending features or tools).
  - Focused on **human beliefs, behaviors, misunderstandings, desires, or struggles**.
  - Framed in a way that a **strategic product team** could use to guide direction, not just execution.
- If relevant, note where people's expectations or mental models around AI may be misaligned, conflicted, or evolving.

---

### Analysis Guidelines:

- Be open and reflexive. Do not assume what the responses “should” say.
- Stay close to the user language and point of view.
- Use storytelling techniques to give meaning to the findings, but balance that with rigorous evidence and logic.
- It’s okay to highlight ambiguity or tension. Not all insights need resolution.
- Your goal is to deeply understand **how people are perceiving generative AI**, not to judge or validate their opinions.

---

When the file is uploaded, begin by clearly stating the question that was asked, then proceed with the analysis.

---

Would you like me to turn this into a reusable template you can paste into every session, or help you turn this into a custom GPT?

