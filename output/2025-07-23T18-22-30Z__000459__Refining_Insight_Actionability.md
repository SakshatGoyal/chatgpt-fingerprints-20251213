# Refining Insight Actionability

## You (2025-07-23T18:22:30.690000+00:00)

I need help refining the following prompt. Currently, the prompt only prompts ChatGPT to focus on surface-level insights from the transcript and considers very high-level feedback. I need to spend a significant amount of time carefully analyzing the entire conversation shared in the transcript to understand the intent and meaning behind Prasanna's feedback. Based on this understanding, I want to frame the insights more effectively. Right now, the output is making only minor changes by adding or replacing a few words, but the essence of the conversation goes much deeper than these surface-level modifications. Below is the prompt I currently have.

Begin creating the new prompt.

---
Your objective is to review the conversation between Sakshat Goyal and Prasanna Rathinasami and modify the language for each insight accordingly. 

Review the transcript of this meeting and carefully consider the feedback from Prasanna Rathinasami regarding the insights shared in these scenarios. The feedback focuses on two aspects:

- Making insights actionable while not giving recommended next actions. 
- Making the insights contextual to a specific quarter. 

While phrasing the new insights, ensure to think like an Account Executive, not just a manager of an Account Executive. 

Most of the feedback on this is limited to the 0-minute to 27-minute range in the recording transcript. 

Maintain the same output structure as before and do not change the interaction scenarios, only the phrasing of the insights to match Prasanna's feedback.

## ChatGPT (2025-07-23T18:22:31.696656+00:00)

Excellent. Let's refine this prompt to ensure it elicits **deep, intent-driven analysis** of Prasanna's feedback, encourages **interpretive synthesis** over shallow rewording, and adopts the **execution mindset** of an Account Executive. Here's a refined version of the prompt based on your goals.

---

### ✅ Final Refined Prompt

**1. Goal**  
Deeply analyze the conversation between Sakshat Goyal and Prasanna Rathinasami, with the purpose of reframing each insight from the meeting transcript in a way that reflects the *underlying intent* behind Prasanna’s feedback. Go beyond surface-level language tweaks—capture and embed the strategic reasoning, tone, and framing that Prasanna implicitly or explicitly encourages. Your goal is to re-articulate each insight so it is more actionable (but not directive) and grounded in quarter-specific context, as if written by an Account Executive for internal consumption or strategic reflection.

**2. Return Format**  
Produce an updated set of insights that:
- Preserve the original interaction scenarios unchanged.
- Modify only the language of the insights.
- Reflect the strategic guidance emphasized in the transcript between the 0–27 minute mark.
- Are phrased from the voice, mindset, and strategic lens of an Account Executive.
- Are sharply contextualized to a specific quarter (as per cues in the transcript).
- Avoid giving explicit recommendations or next steps, but naturally set up the reader to infer those steps.

Return the insights in the same structural format as the original output (e.g., if they were in a list under each scenario, maintain that format). Annotate or comment within each change only where necessary to briefly clarify how the rewording aligns with the deeper feedback.

**3. Warnings & Guardrails**  
- **Do not** perform superficial edits or focus solely on diction-level feedback (e.g., word swaps or minor phrasing changes).
- **Do not** generalize the insights—make them sharper by anchoring them to actual context from the quarter referenced.
- **Avoid recommendations**—instead, embed implications subtly within each insight’s phrasing.
- Where Prasanna’s feedback implies a mental model, framing shift, or strategic posture, **incorporate that shift**.
- If the original insight lacks context, infer reasonable context based on the conversation—but flag that assumption explicitly.

**4. Context & Additional Elements**  
- **Transcript Source**: Feedback and interpretive cues should be drawn primarily from minutes 0 to 27 of the Sakshat–Prasanna conversation.
- **Embedded Persona**: Think, reason, and write as an Account Executive (not their manager), showing awareness of sales cycle timing, account posture, and revenue planning realities.
- **Analytical Lens**: Adopt a *hybrid reasoning* approach—interpret inductively from the transcript while also applying deductive structure to reframe the insights.
- **Tone**: Strategic, grounded, and calibrated for internal clarity—avoiding ambiguity, fluff, or overgeneralization.

---

Would you like me to walk through a before/after example of an insight reframing to demonstrate how this refined prompt would guide the model differently?

## You (2025-07-23T18:30:13.427000+00:00)

Help me refine this follow-up prompt. begin creating the prompt:
---
Maintaining the same language and approach to phrasing insights, create 3 scenarios where the insights for ALL opportunities remain the same. In the different scenarios, a user is simply selecting filters based on what they might want to consider based on 4 insights. the 4 insights should be as follows:

### 1. Find Risk Densities

**Goal:** Surface important patterns of revenue risk without prescribing solutions.

**Use-cases:**

- When a user filters for deals in the "Critical" or "At-risk" account health category, AI highlights common, high-impact risk factors:
    
    > "8 deals (\$4.2M) marked Critical share common risks: mandatory professional services removed (6 deals), low adoption rate (4 deals)."
    > 
- When filtering opportunities by high-value renewals (> \$1M), identify clusters of risk:
    
    > "3 out of 5 high-value renewals totaling \$7.2M are at-risk due to no partner finalized and pending budget approval."
    > 
- When viewing specific products (e.g., Cortex & Cloud), highlight recurring risks specific to the product:
    
    > "60% of Cortex deals in Pipeline status have risk factors of low customer adoption and no recent EBC activity."
    > 

---

### 2. Finding the Bottleneck in Momentum

**Goal:** Highlight deals stalled in the sales process, facilitating user-initiated interventions.

**Use-cases:**

- When users filter for deals closing soon (<45 days), AI detects stalled progress:
    
    > "4 'Commit' stage deals totaling \$3.1M have had no activity for over 30 days; predominantly in SASE."
    > 
- When filtering for upsell opportunities, pinpoint potential slowdown points:
    
    > "Two large upsell opportunities (\$1.9M) have been stuck in 'Solution' stage beyond average timelines, both lack a secured technical win."
    > 
- When viewing high-value renewals, surface pipeline inactivity:
    
    > "25% of renewals above \$500K show no activity for 30+ days, primarily due to pending quote approvals and lack of partner selection."
    > 

---

### 3. **Outlier and Contradiction Detection**

**Goal:** Alert users to mismatches between forecast optimism and underlying risks.

**Use-cases:**

- When filtering for "Commit" forecast deals, highlight contradictions in the data:
    
    > "1 Commit deal valued at \$1.2M (Capstone Logistics) has Critical account health and multiple unresolved risk factors."
    > 
- Upon filtering for large deals, show counterintuitive flags (e.g., high-value "Best Case" deals with extensive risk):
    
    > "2 of your top 5 ‘Best Case’ deals (\$2.3M) exhibit unexpected risk factors: budget conversations incomplete, no technical win secured."
    > 
- When examining net-new opportunities, highlight critical risks that could derail optimistic forecasts:
    
    > "3 of 6 high-value net-new deals forecasted positively (\$2.1M total) currently have critical technical health and zero partner activity."
    > 

---

### 4. **Detecting Silent Zones**

**Goal:** Surface areas of prolonged inactivity or neglect within a user's opportunity pipeline.

**Use-cases:**

- When viewing deals closing in the next 90 days, flag prolonged inactivity:
    
    > "5 high-value (\$2.8M total) opportunities have had zero activity in the past month; most show no EBC engagement."
    > 
- Filtering opportunities by renewal status identifies inactive renewal opportunities:
    
    > "3 of your renewal opportunities totaling \$1.1M have no logged activity for over 45 days, and have mandatory PS removed."
    > 
- Upon examining large enterprise accounts, highlight dormant, high-risk opportunities:
    
    > "2 enterprise accounts (>\$1M each) currently show zero pipeline activities in the last 30 days and risk losing momentum."
    >

---

This framework should be followed in every step of each scenario.

## ChatGPT (2025-07-23T18:30:14.414114+00:00)

Great—your goal is clear: you want to maintain a consistent language and insight structure while varying only the **filtering context** to simulate different user interactions. The purpose is to **demonstrate how the same 4 insights** (Risk Densities, Bottlenecks, Outliers, Silent Zones) dynamically adapt to different filters without changing their phrasing strategy.

Here is a fully refined and directive prompt:

---

### ✅ Refined Prompt

**1. Goal**  
Generate **3 user-filtered scenarios** that apply the *same 4 insight frameworks*—Risk Densities, Bottlenecks in Momentum, Outlier Detection, and Silent Zones—but vary only in the **filter combinations** used to surface those insights. The insights themselves should retain their structure, phrasing style, and voice as defined, with each adapting naturally to the filter context selected by the hypothetical user. 

Each scenario reflects a different combination of filters the user might apply, leading to surfaced insight variations **anchored in the same conceptual models**. Think of these scenarios as simulations of how an intelligent sales assistant might respond in different usage contexts, always guided by the same underlying insight types.

**2. Return Format**  
Produce three fully fleshed-out scenarios. For each scenario:
- Label the scenario (e.g., *Scenario 1: Upsell Focus in Q4*).
- Clearly state the **user filters applied** (e.g., `"Forecast: Commit", "Segment: Enterprise", "Product: Cloud"`).
- Include all **4 insight types**, using the same structure and level of specificity shown in the original examples.
- Use realistic numbers, product names, and brief explanations grounded in the filter context.
- Keep insights concise, numerically grounded, and implicitly actionable without prescribing next steps.

**3. Warnings & Guardrails**  
- Do **not** change the phrasing approach or analytical goals of the 4 insight types.
- Do **not** remove or substitute insight types—each of the 3 scenarios must include **all four**: Risk Densities, Bottlenecks, Outliers, and Silent Zones.
- Do **not** suggest next steps or actions; insights should only **surface patterns, contradictions, or inactivity.**
- Ensure that the insights remain **business-credible**: sales stage, dollar amounts, and timing should align plausibly with the filter context.
- Avoid generic, vague, or repetitive patterns—each scenario should feel distinct yet grounded in the same conceptual framework.

**4. Context & Additional Elements**  
- This prompt assumes prior alignment on phrasing tone, persona (Account Executive), and clarity of each insight category.
- Feel free to creatively vary filters across dimensions such as:
  - Forecast category (e.g., Best Case, Commit)
  - Deal type (e.g., Renewal, Expansion, Net-new)
  - Account health (e.g., At-Risk, Strong)
  - Product family (e.g., Cloud, Cortex, SASE)
  - Timeframe (e.g., Closing in 30/60/90 days)
  - Segment (e.g., Mid-Market, Enterprise)
- Prioritize **realistic combinations** that would reflect how users explore data in live tools.

---

Would you like me to generate a sample *Scenario 1* to demonstrate how this works in practice?

## You (2025-07-23T18:32:36.184000+00:00)

In the output of this prompt, I see the insights, but I don't see the steps. Right now, it has basically ignored the previous formatting, which is the three scenarios and the four steps within each scenario. Now it's using its own formatting. So I also needed to maintain the same format as previously used.

## ChatGPT (2025-07-23T18:32:36.828431+00:00)

Got it—that’s a key detail. You want the **formatting structure of the output** to exactly follow the original:  

- ✅ **3 distinct scenarios**  
- ✅ Each scenario should contain **all 4 insights**,  
- ✅ Each insight must be broken down into:
  - **Insight Title**
  - **Goal**
  - **Use-cases** with examples (bulleted or blockquote format as shown)

Here’s the **corrected and fully formatted version of the prompt**, ensuring strict adherence to your formatting rules.

---

### ✅ Refined Prompt (with Output Format Preservation)

**1. Goal**  
Generate 3 different scenarios where users apply distinct filters when reviewing their pipeline data. For each scenario, surface insights using the **same 4 insight categories**—**Find Risk Densities**, **Finding the Bottleneck in Momentum**, **Outlier and Contradiction Detection**, and **Detecting Silent Zones**—**without changing their phrasing structure or style**.

The insights themselves should retain the tone, format, and execution mindset of an Account Executive and remain analytically grounded and contextually rich. Only the **filter combinations** and corresponding surfaced examples should change between scenarios. Do not reframe the insight categories.

**2. Output Format**  
For each of the 3 scenarios, follow this exact format:

---

**Scenario [X]: [Descriptive Scenario Name]**

> **Applied Filters**:  
> [Filter 1], [Filter 2], [Filter 3]...

---

### 1. Find Risk Densities  
**Goal:** Surface important patterns of revenue risk without prescribing solutions.

**Use-cases:**

- [Insight example 1, written in same format as original prompt]  
- [Insight example 2]  
- [Insight example 3]  

---

### 2. Finding the Bottleneck in Momentum  
**Goal:** Highlight deals stalled in the sales process, facilitating user-initiated interventions.

**Use-cases:**

- [Insight example 1]  
- [Insight example 2]  
- [Insight example 3]  

---

### 3. Outlier and Contradiction Detection  
**Goal:** Alert users to mismatches between forecast optimism and underlying risks.

**Use-cases:**

- [Insight example 1]  
- [Insight example 2]  
- [Insight example 3]  

---

### 4. Detecting Silent Zones  
**Goal:** Surface areas of prolonged inactivity or neglect within a user's opportunity pipeline.

**Use-cases:**

- [Insight example 1]  
- [Insight example 2]  
- [Insight example 3]  

---

**3. Warnings & Guardrails**  
- Maintain the **exact formatting** and insight phrasing structure from the original example.
- Do **not** change the four insight types or their associated Goals or section headers.
- Do **not** alter the tone, style, or execution voice (Account Executive focused).
- Do **not** prescribe next actions—focus only on surfacing meaningful patterns or flags.
- Do **not** generalize across filters—each insight must align tightly with the scenario’s specific filters.
- Ensure all examples are realistic, numerically credible, and context-aware.

**4. Context & Persona Notes**  
- Assume the user is a field-facing Account Executive using a data assistant interface.
- Each scenario should reflect a plausible use-case where they apply filters to understand pipeline health, risk, and momentum.
- Filters may include combinations like:  
  - Segment (e.g., Mid-Market, Enterprise)  
  - Forecast (e.g., Commit, Best Case)  
  - Deal type (Renewal, Expansion, Net-new)  
  - Product (e.g., Cortex, Cloud)  
  - Account health (e.g., Critical, At-Risk)  
  - Timeframe (e.g., Close in 30/60/90 days)  

---

Would you like me to generate **Scenario 1** using this structure so you can test the format?

