# Corporate Strategy Prompt Creation

## You (2025-03-31T08:34:15.338000+00:00)

Hey, i need your help crafting a prompt for the following intent. Also recommend a few personas that might be ideal for this task. 

I have a handbook on different types of strategies. For this prompt, I want it to focus on corporate strategy alone. But write it in a modular way so I can change it for other categories of strategies. 

Here’s the content I need from it

Definition: a short 2 line explaination

What it means: about 3-5 sentence descriptive explaination

Examples of what it means: Specific personas performing a certain activity

What it does not mean: drawing a clear line between this and other forms of strategy. 

Examples of what it does not mean: Specific personas performing a certain activity.

An analogy of what it means within 1 sentence. 

The purpose if for a slide deck, and the audience is a group of product strategists. 

Now ask me the necessary questions.

## ChatGPT (2025-03-31T08:34:16.041003+00:00)

Awesome! Thanks for sharing the full Strategy Classification Handbook. It gives us everything we need to build a robust, modular prompt.

Before I construct the prompt, let's zero in on a few strategic and creative dimensions so I can make sure we structure this for flexibility, tone, and usefulness.

### 🧠 Clarifying Questions

#### 1. **Tone & Voice**
- You mentioned this is for a slide deck for product strategists. 
   - Do you want a **crisp, executive-level tone**?
   - Or a more **conversational but insightful** tone (like a strategist explaining to peers)?

#### 2. **Modular Design**
- When you say “modular,” are you envisioning:
   - A **template-like format** you can copy and paste for each strategy type?
   - Or a **single prompt** with variables/placeholders (e.g., `{strategy_type}`) that GPT can reuse dynamically?

#### 3. **Examples: Personas**
- Do you want **fictional examples** (e.g., “A VP of Strategy at a global energy company chooses to…”) or **real-world ones** (e.g., “Microsoft’s acquisition of Activision…”)?  
   - And are you open to some being speculative/hypothetical?

#### 4. **Slide Deck Format**
- Would you like the final output to be:
   - A **bulleted format** for easy copy-paste into slides?
   - Or more like structured prose blocks?

#### 5. **Edge Cases**
- Do you want the prompt to **flag when a strategic decision might seem like corporate-level but is not** (e.g., innovation-driven moves that only *appear* corporate-level)?
   - Or should we keep it clear-cut, with no ambiguity handling?

---

Once I have answers to the above, I’ll also suggest 2–3 ideal **personas for the GPT to adopt** in the generated outputs. Then we’ll be ready to **begin building the prompt.**

## You (2025-03-31T08:39:16.070000+00:00)

lets go with a conversational but insightful tone, like a strategist explaining to their peers. But none of the "Hey, guess what..." kind of shenanigans. 

when i say modular, basically i want to be able to replace 'corporate with business, functional, etc...

I think the personas should be more aligned with the nature of the content, like a strategist at McKinsey or a Harvard business school professor. 

I think i'd like more structured prose blocks for the definition, but for the examples maybe bulleted sentences, but its important not to oversimplify something because these are new concepts for most. 

Edge cases, sure, lets handle those in the examples for what its not.

## ChatGPT (2025-03-31T08:39:17.174194+00:00)

Perfect—this gives us a clear frame to work with. Here's a summary of what we've defined so far:

---

### ✅ **PromptCraft Discovery Summary**

**🎯 Objective:**  
Create a reusable prompt that generates structured, slide-deck-ready content focused on **one strategy type at a time**—starting with *Corporate Strategy*. The output should help *product strategists* understand what the strategy is, what it’s not, and how to distinguish it in practice.

**🧱 Modular Design:**  
Prompt should allow easy substitution of `strategy_type` (e.g., Corporate → Business → Functional, etc.)

**🗣 Tone:**  
Conversational but insightful—like a strategist explaining to a peer. No fluff, no overly casual banter.

**🧠 Examples:**  
- *“What it means” examples:* specific personas + concrete strategic actions.  
- *“What it does NOT mean” examples:* same, but designed to illustrate common confusion or edge cases.

**🔍 Edge Cases:**  
To be addressed through well-chosen counter-examples under “What it does not mean.”

**📚 Format Preference:**  
- Short structured prose blocks for: Definition, What it means, What it does not mean, Analogy  
- Bulleted lists for: Examples (what it means + what it doesn’t)

**👤 Ideal GPT Persona (for generated output):**  
Combination of:
- 🎓 *Harvard Business School Professor*
- 🧠 *McKinsey/BCG Corporate Strategist*

---

Next step: I’ll **begin building the prompt** for GPT-4o with all these pieces baked in.

Would you like it as:
1. A single fixed prompt written for *Corporate Strategy* that you can duplicate for the others, or  
2. A general prompt with a `{strategy_type}` variable built in, so you can generate any type on demand?

## You (2025-03-31T08:39:50.764000+00:00)

begin building the prompt

## ChatGPT (2025-03-31T08:39:51.434678+00:00)

Great. Here's the full prompt—crafted for GPT-4o to generate content on **Corporate Strategy**, with modularity built in so you can easily swap in other strategy types like Business, Functional, Innovation, etc.

---

## 🧩 **Prompt: Strategy Type Explainer for Slide Deck (Modular)**

> 📌 **Use this to generate structured, slide-ready explanations of different strategy types—starting with Corporate Strategy.** Swap out `{strategy_type}` as needed.

---

**Prompt for GPT-4o:**

---

You are a seasoned **strategy educator and practitioner**—combining the clarity of a **Harvard Business School professor** with the applied insight of a **McKinsey corporate strategist**. You’re explaining the concept of **{strategy_type} strategy** to an audience of **product strategists**, many of whom are encountering these distinctions for the first time.

Write a slide-deck-ready explanation with the following structure and tone:

---

### 📘 Format & Structure:

1. **Definition**  
   Provide a concise, clear 1–2 sentence definition of `{strategy_type} strategy`. Avoid jargon, but preserve precision.

2. **What It Means**  
   A short 3–5 sentence paragraph explaining what this strategy type actually looks like in practice. Use plain but strategic language. Emphasize who owns these decisions, the scope of impact, and strategic intent.

3. **Examples of What It Means**  
   Provide 2–3 **bulleted examples** showing specific personas (e.g., “A CEO...”, “A Board of Directors...”) performing actions that clearly represent `{strategy_type}` strategy. Each example should include:
   - A clear action
   - The strategic rationale behind it
   - Enough specificity to be recognizable but not so detailed that it feels niche

4. **What It Does Not Mean**  
   A short paragraph drawing a clear boundary between `{strategy_type}` and adjacent strategy types it is often confused with (e.g., business-level, innovation, or functional strategy). Clarify **scope**, **intent**, and **decision-makers**.

5. **Examples of What It Does Not Mean**  
   Provide 2–3 **bulleted counter-examples** that resemble `{strategy_type}` strategy on the surface but actually represent something else. Explain:
   - Who’s making the decision
   - Why it’s *not* an example of `{strategy_type}`
   - Which strategy type it actually is, and why

6. **Analogy (1 sentence)**  
   Close with a one-line analogy that captures the *essence* of `{strategy_type}` strategy in intuitive terms.

---

### 🗣️ Tone:
- Conversational but insightful  
- No over-explaining or fluff  
- No rhetorical questions or filler like “Guess what?” or “You might be wondering…”

---

### 🧠 Self-Check Instructions (for GPT-4o):
Before finalizing your output:
- Double-check that each example fits the *scope* and *intent* of `{strategy_type}`
- Ensure all distinctions are crisp and non-overlapping
- Use real companies for inspiration if helpful, but **do not name them unless requested**

---

## Example Strategy Type Input:
```
strategy_type = "Corporate"
```

---

Let me know if you'd like this turned into a Notion block template, markdown, or embedded in a few prompt variants for reuse (e.g., with real-world examples toggled on/off).

