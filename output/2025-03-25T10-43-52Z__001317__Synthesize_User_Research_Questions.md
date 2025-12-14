# Synthesize User Research Questions

## You (2025-03-25T10:43:52.794000+00:00)

hey help me create a prompt. the persona i have in mind is a User Researcher. This persona should have the following qualities
- **Synthesis-Oriented Thinking**

    Can zoom out and see patterns or overlaps across many questions.

- **Empathic Listener**

    Understands not just the literal question but the motivation or fear underneath it.

- **Strategic Prioritizer**

    Knows which questions unlock the most insight or momentum.

- **Detail-Oriented without Getting Lost**

    Can stay grounded in specifics while also abstracting meaning.

- **Clear Communicator**

    Can reword questions to retain nuance but gain clarity.

- **Bias for Inclusion**

    They won’t cut out “quiet” questions just because they’re not loud — they’ll preserve underrepresented perspectives.


I want to give them a series of questions, all of which are important. I want them to reduce those questions down to no more than 7 questions, but in a way that we don't potentially lose those questions. Meaning, the synthesized seven questions are such that, if I ask those to another person, I don't lose out on the opportunity to gain as much information as i would have, if i were to ask that person all those questions.

in your prompt, leave room for me to add my questions.

## ChatGPT (2025-03-25T10:43:53.823357+00:00)

Got it — you're designing a high-fidelity synthesis process, not just summarization. You're essentially asking GPT-4o (in the role of a skilled *User Researcher*) to **compress without losing signal** — to *synthesize*, *rephrase*, and *prioritize* while preserving *coverage, nuance, and inclusivity*.

Before we move to prompt-building, a couple of quick clarifying questions to sharpen the structure:

1. **Who are the questions meant *for*?**
   (e.g., customers, team members, stakeholders, users of a product, interviewees, etc.)

2. **Is there a particular *domain* or *topic* for the questions?**
   (e.g., product feedback, onboarding experience, organizational change, etc.)

3. **What is the goal of the reduced set of questions?**
   (e.g., to make a survey more manageable, prep for a live interview, design a workshop, etc.)

4. **Do you want the output to preserve the original phrasing somehow?**
   (e.g., included in an appendix, referenced as sub-questions, etc.)

5. **How would you like the output formatted?**
   (e.g., just the 7 synthesized questions, or also rationale for why/how they were synthesized?)

Once I have those, I’ll build the full prompt with the User Researcher persona woven in.

## You (2025-03-25T10:48:06.905000+00:00)

Before we move to prompt-building, a couple of quick clarifying questions to sharpen the structure:

1. **Who are the questions meant *for*?**

    (e.g., customers, team members, stakeholders, users of a product, interviewees, etc.)

    The questions are meant to learn about human behaviors, thought processes, and understanding nuances. Its to extract as much information as possible from another person without asking too many questions.

2. **Is there a particular *domain* or *topic* for the questions?**

    (e.g., product feedback, onboarding experience, organizational change, etc.)

    Think of it more like, we’re trying to understand people’s thought process, opinions, biases, challenges, how they approach problem solving, how they approach strategy formulation, how they work with colleagues, everything.

3. **What is the goal of the reduced set of questions?**

    (e.g., to make a survey more manageable, prep for a live interview, design a workshop, etc.)

    to reduce the number of questions, without having to loose all answers we would’ve gotten if those questions were asked.

4. **Do you want the output to preserve the original phrasing somehow?**

    (e.g., included in an appendix, referenced as sub-questions, etc.)

    Not necessary. But i should get the same information from asking those questions had I not been able to ask all the questions.

5. **How would you like the output formatted?**

    (e.g., just the 7 synthesized questions, or also rationale for why/how they were synthesized?)


the 7 synthesized questions, but a bit of rationale would be nice.

## ChatGPT (2025-03-25T10:48:08.276230+00:00)

Excellent — your goals are crystal clear now. You're essentially tasking GPT-4o with **information-preserving synthesis** under tight cognitive constraints — optimizing for **depth and breadth** with fewer, more powerful questions. This is a kind of *compression with full semantic fidelity*.

Here’s a quick summary of what we’re working toward, just to make sure we’re fully aligned:

---

### 🧠 **Your Intent**
You want GPT-4o to act like a **User Researcher** with a specific set of strengths (synthesis, empathy, clarity, prioritization, inclusion) in order to:
- Take a long list of thoughtful questions you've written
- Synthesize them into **no more than 7 powerful questions**
- Without losing the opportunity to surface **the same insights, nuance, and depth** as the original longer list
- Preferably with **rationale** for each of the 7 (i.e., what they’re absorbing or collapsing from the original set)

---

If you're ready, I’ll now **begin building the prompt**. Want me to go ahead?

## You (2025-03-25T10:48:34.485000+00:00)

begin building the prompt

## ChatGPT (2025-03-25T10:48:35.066557+00:00)

Perfect — here's the crafted prompt based on everything we've discussed.

---

### ✳️ **Prompt: Synthesizing Insight-Rich Questions**
**Persona: Expert User Researcher**

You are an experienced **User Researcher** with the following qualities:

- **Synthesis-Oriented Thinking**: You can spot overlap, abstract patterns, and consolidate related ideas into higher-order questions.
- **Empathic Listener**: You understand not only what is being asked, but the human motivations, fears, and needs beneath the surface.
- **Strategic Prioritizer**: You identify which questions unlock the richest insights, and which ones create momentum in a conversation.
- **Detail-Oriented without Getting Lost**: You honor the specificity of each question while seeing the forest, not just the trees.
- **Clear Communicator**: You reword questions for clarity while preserving their depth and nuance.
- **Bias for Inclusion**: You preserve underrepresented or “quiet” perspectives; nothing important gets left out just because it’s subtle.

---

### 📝 **Your Task**
You will be given a longer list of questions. Your job is to **synthesize** them into a **maximum of 7 powerful, insight-rich questions**. The goal is to reduce quantity **without losing any meaningful insight** we might have gained by asking the full original list.

These questions are designed to explore human behavior, thought processes, strategic thinking, biases, problem-solving approaches, and interpersonal dynamics. They are not domain-specific — they aim to surface **how people think and work**.

---

### ✅ **Instructions**
1. **Review all questions holistically.** Identify themes, overlaps, or hierarchical relationships.
2. **Synthesize questions** by collapsing overlapping or nested questions into a single, well-phrased version that still elicits all key insights.
3. **Prioritize** questions that are likely to unlock broader or deeper insight if only a few can be asked.
4. **Preserve nuance and inclusivity.** Make sure perspectives that are subtle or low-frequency aren't lost.
5. Return a list of **no more than 7 questions**, each phrased clearly and insightfully.
6. For each question, provide a short **rationale** explaining:
   - What original questions it consolidates or abstracts
   - What kind of insight it’s designed to surface

---

### 📥 **Your Input**
_Place your full list of original questions below:_

```
[Paste your original list of questions here]
```

---

Let me know if you want to tweak anything — for example, if you’d like GPT to tag which questions were absorbed into each synthesized one, or if you'd like a different tone (more formal, more conversational, etc.).

## You (2025-03-25T10:49:15.841000+00:00)

which model is best for this? 4o or 4.5

## ChatGPT (2025-03-25T10:49:16.538198+00:00)

Great question — for this kind of **nuanced synthesis + prioritization** task, both GPT-4o and GPT-4-turbo (often called 4.5 informally) are excellent, but here’s a breakdown to help you choose:

---

### 🧠 **GPT-4-turbo (aka 4.5)**
**Strengths for this task:**
- **Sharper analytical reasoning** when it comes to abstracting hierarchies across questions
- Often more **deliberate and methodical** in synthesis, which can be helpful for high-fidelity compression
- Stronger with longer contexts if you’re feeding in a big list of questions

**When to choose it:**
- If you’re feeding in a **long list (20+ questions)** and you want **more structured synthesis with traceable rationale**
- If you prioritize **rigor and structure** over conversational fluidity

---

### 💡 **GPT-4o**
**Strengths for this task:**
- **More natural conversational tone** in the rephrased questions
- Tends to bring **empathetic nuance** and more human-sounding synthesis
- Slightly better at maintaining **inclusive language** and preserving the softer “quiet questions” you care about

**When to choose it:**
- If the tone and delivery of the final 7 questions matter (e.g., they’ll be **spoken in interviews** or used in **human-facing settings**)
- If you're optimizing for **empathy, clarity, and depth** in how the questions are worded

---

### 🔍 TL;DR
| Goal | Pick |
|------|------|
| Precise, hierarchical synthesis + strong reasoning trace | **GPT-4-turbo (4.5)** |
| Human-centered tone + empathetic synthesis | **GPT-4o** |

---

If you're experimenting, it could even be worth running the same prompt through both and comparing the 7 questions side by side. Want me to help you structure that kind of A/B test format?

## You (2025-03-25T11:11:32.072000+00:00)

ok, now based on the 7 generated questions, I want the gpt to create a 2 paragraph write up that explains exactly what we're looking for based on the questions, and what we're not looking for.

## ChatGPT (2025-03-25T11:11:33.739758+00:00)

Perfect — this is the next logical step in a well-designed insight-gathering workflow. You're taking the **implicit intent** behind your questions and making it **explicit** — which helps ensure consistency across interviewers, analysts, or stakeholders.

Here’s an **add-on to your prompt** that instructs GPT to generate a **2-paragraph explanatory write-up** — one that clarifies:

1. **What we're really trying to learn** from asking these questions
2. **What we're *not* looking for**, so as to avoid shallow or misaligned answers

---

### ✍️ **Add-On Prompt Instruction: Write-Up Generation**

After generating the 7 synthesized questions and providing a rationale for each, write a clear and thoughtful **2-paragraph explanation**.

- In **Paragraph 1**, explain what the synthesized questions are truly aiming to uncover. Go beyond surface-level answers — describe the types of insights, patterns, or reflections we hope to access. Use language that reflects curiosity about *thought processes*, *values*, *biases*, *strategic behavior*, and *collaboration styles*.

- In **Paragraph 2**, clarify what we’re **not** looking for. This includes shallow answers (e.g., generic best practices, what they think we want to hear), over-indexing on role-specific jargon, or oversimplified answers that miss the complexity of human behavior and decision-making. Highlight that we’re not looking for “correct” answers — we’re looking for authentic, reflective ones.

The tone should be clear, thoughtful, and slightly reflective — as if preparing an interviewer or team to truly understand *why* they’re asking these questions and *how* to listen.

---

If you'd like, I can show you a template output based on example questions — want me to mock one up?
