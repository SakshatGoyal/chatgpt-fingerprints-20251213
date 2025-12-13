# Insight Evaluation Strategy

## You (2025-03-25T05:38:15.922000+00:00)

Hey Michael, I'm giving you some context for now and going to take a pause and let you digest it. Once you've done that, then we'll move to the next steps where i'll need your help. 


## ✅ **Primary Goal**

To **evaluate and reduce a large set of structured insight modules** (a.k.a. categorical modules) in order to:

- Eliminate redundant, shallow, or low-utility insights
- Retain only the most **strategically sharp, cognitively rich, and product-relevant** modules
- Prepare a curated, high-quality corpus for synthesis, theme extraction, and future product use

We currently have about 225 insights, and we need some way to quickly prune some of those so we can focus on what's important.
---

## 🎯 **Use Case Context**

- We are building an **AI assistant** for strategic thinking in the future. For now we’re trying to lay the foundation for trying to find a product market fit.
- This assistant will help users explore strategic decisions (without access to internal company data).
- Our insight corpus comes from research papers focused on **organizational behavior**, **executive decision-making**, and **strategy**.
- Each insight module includes a full narrative: strategic insight, decision context, bias exploration, stress test, limitations, and critique.

---

## 👥 **Team & Process Constraints**

- We have a team of **5 designers**, each reviewing **~45 modules**.
- Designers read the **entire module holistically** (not just isolated statements).
- Each reviewer is expected to **eliminate 10–15 insights** based on a shared evaluation model.
- Reviewers work independently—so consistency and clarity are key.

---

Format of each Insight

### 📘 Each CATEGORICAL MODULE (treated as one insight) Has Two Parts:

---

### **1. Insight Construction** *(Primary content)*

This is where the strategic idea is introduced, contextualized, and supported.

- **Insight Statement**
    
    Concise, critical framing of a core idea. Often challenges prevailing logic or introduces a surprising pattern.
    
    > What assumption or mental model is being questioned?
    > 
- **Executive Decision-Making Context**
    
    Includes:
    
    - Strategic dilemma (what’s at stake?)
    - Underlying beliefs and biases (what assumptions are being surfaced?)
    - Expected vs. actual outcomes (what went differently than planned?)
    - Broader implications (what could change systemically?)
    
    > Who’s making the decision? What kind of decision is it? What organizational layer does it affect?
    > 
- **Supporting Context**
    
    Empirical grounding or theoretical basis for the insight. Includes references to data, frameworks, case studies, or precedent.
    
    > Does this insight come from market dynamics, internal operations, innovation logic, or individual reflection?
    > 

---

### 2. Stress Test

This section pushes the insight into boundary conditions. It helps clarify **what the insight is not**, **where it breaks down**, and **what assumptions it hides**.

| Component | What It Tells You | Why It Matters Strategically |
| --- | --- | --- |
| **Counterfactual Scenario** | A fictional case where the insight fails | Reveals *contextual boundaries*. Helps disqualify strategy types it might superficially resemble |
| **Assumptions & Biases** | Hidden cognitive shortcuts | Indicates *mental framing*—especially useful for spotting **Leadership**, **Business**, or **Innovation** logic |
| **Context Limitations** | Known edge cases where the insight breaks down | Helps narrow the scope of the insight (e.g., it may not apply org-wide, so not Corporate) |
| **Final Critique** | Conceptual tensions or contradictions | Great signal for identifying trade-offs—often highlights **Adaptive** or **Strategic Tension** dimensions clearly |


Example of an Categorical Module:

**CATEGORICAL MODULE 1**

Reconceptualizing Processes as Coordinated Competencies
Insight Statement:
The paper challenges conventional views by framing business processes not as static sequences of activities but as dynamic assemblies of coordinated competencies, where both human and machine cognitive abilities interweave to solve problems. [Empirical]

Executive Decision-Making Context:

Strategic Dilemma: Executives must choose between adhering to traditional, step-based process models or embracing a dynamic, competency-based approach that leverages distributed cognitive strengths.
Underlying Beliefs & Biases: There is a prevalent bias toward linear, predictable models, even when such approaches falter in complex, knowledge-intensive environments.
Expected vs. Actual Outcomes: Traditional methods promise efficiency through standardization; however, the framework suggests that a focus on integrated competencies can lead to more adaptable and resilient operations.
Broader Implications: Shifting to a competency-based model may necessitate rethinking investments in IT, training, and organizational design to foster effective knowledge coordination. [Inferred]
Supporting Context:
The authors build their argument on the knowledge-based theory of the firm, arguing that the true challenge lies in integrating specialist knowledge via distributed cognition. They articulate that process design should focus on orchestrating task competencies rather than merely structuring sequential activities. [Empirical]

🔹 COUNTERFACTUAL SCENARIO:

A large-scale manufacturing organization operates within a heavily regulated, safety-critical industry such as nuclear energy or aerospace. Regulatory compliance mandates explicit and rigid sequential procedures, leaving minimal scope for dynamic coordination. In this scenario, treating processes as dynamic cognitive assemblies leads to unpredictability, compliance failures, increased inspection costs, and potential safety hazards.

🔹 ASSUMPTIONS & BIASES:

Overconfidence in adaptability over standardized efficiency.
Assumption that dynamic cognition always outweighs procedural stability.
Ignoring regulatory and safety requirements as binding constraints.
🔹 CONTEXT LIMITATIONS:

This insight falters in environments requiring strict compliance, predictable repetition, or minimal variance. Industries such as pharmaceuticals, aviation, nuclear power, and financial auditing may reject dynamic interpretations due to regulatory and quality control demands.

🔹 FINAL CRITIQUE:

This insight introduces a conceptual tension: it implicitly undervalues scenarios where rigidity and predictability are strategically advantageous or legally necessary, potentially creating internal contradictions between innovation and compliance.

## 🧰 **Evaluation Approach**

We're using a **scoring matrix** based on clearly defined criteria. Each module is evaluated against several **dimensions**, each reflecting a different aspect of value.

Reviewers **don’t need to compare modules** against one another—they evaluate each one on its own merit.

---

## 📐 **Scoring Methodology**

You're using a **two-tiered weighted scoring model**:

| Step | Description |
| --- | --- |
| **1. Define Evaluation Criteria** | Each criterion reflects a different aspect of strategic or product value |
| **2. Assign Weights to Each Criterion** | From **1 to 5**, based on importance to your overall goal |
| **3. Score Each Module on Each Criterion** | From **1 to 10**, based on performance or strength |
| **4. Multiply Weight × Score** | This gives a weighted score per criterion |
| **5. Sum All Scores** | Total score helps you **rank, retain, or eliminate** modules |

## Questions our scoring mechanism should answer (all are important)
This is our criteria and we're trying to figure out how we can further refine this to make it actionable


### **Human-Centered & Conceptual Depth Criteria**

(Does the insight help us understand or improve the way people *think*, *feel*, or *decide*?)

| Criterion | What It Evaluates |
| --- | --- |
| **Identifies a Clear Problem** | Does the insight diagnose a real, specific tension or strategic pain point? |
| **Challenges Common Assumptions** | Does it surface a contradiction, bias, or outdated mental model? |
| **Highlights a Strategic Dichotomy** | Does it reveal a trade-off, conflict, or opposing forces (e.g., speed vs. accuracy, innovation vs. compliance)? |
| **Reframes the Problem Space** | Does it offer a new lens or mental model for an old challenge? |

### **Context-Specific & Relevance Criteria**

(Derived from the Strategy Classification Handbook + system design perspective)

| Criterion | What It Evaluates |
| --- | --- |
| **Cross-Level Noise** | Is this insight muddy or ambiguous in terms of its strategic classification? (if so, lower score unless clarified elsewhere) |

### **Product-Centric Criteria**

(Focused on product-market fit + assistant interaction model)

| Criterion | What It Evaluates |
| --- | --- |
| **Avoids Organizational Integration Dependency** | Would this insight still be useful if the AI assistant doesn’t have access to internal company data? |
| **Highlights Use of Reasoning Over Data** | Does the insight center around *thinking patterns*, not just analytics infrastructure? |

### **D. Technical Filtering Criteria (For Use in Elimination/Quality Control)**

| Criterion | What It Evaluates |
| --- | --- |
| **Strategic Novelty** | Is the insight just a rephrasing of a known truism (e.g., "data matters")? |

### **Insight Construction**

| Criteria | Description | Why It Matters |
| --- | --- | --- |
| **Clarity of Strategic Tension** | Is there a real **dilemma, conflict, or contradiction** in the Executive Context? | We’re building an assistant that thrives on illuminating tension |
| **Bias Visibility** | Are **underlying beliefs or heuristics** clearly identified, not just outcomes? | Differentiates this from generic strategy writing |
| **Over-Generality Penalty** | Is this just a safe, obvious, or too-general observation? | Weakens potential use—ideally scored as a *negative weight* |

### **Insight Stress Test**

| Criteria | Description | Why It Matters |
| --- | --- | --- |
| **Diversity of Contextual Breakdown** | Do the **Context Limitations** reflect a variety of edge conditions (e.g., political, regulatory, economic)? | Captures scope boundaries clearly—helps define relevance later |
| **Clarity of Bias Attribution** | Are the **Assumptions & Biases** specific, insightful, and relevant to executive cognition or strategy logic? | Biases should reflect framing, not just behavior |
| **Sharpness of Final Critique** | Does the **Final Critique** meaningfully challenge the validity or reliability of the insight? | Avoids the trap of “counterfactual lite” sections that are polite but uncritical |
| **Balance Between Optimism and Skepticism** | Does the stress test avoid being overly dismissive or unreasonably optimistic? | Real strategic environments require *tension*, not certainty |

### **Systemic/Meta-Level Criteria**

| Criteria | Description | Why It Matters |
| --- | --- | --- |
| **Interaction Potential** | Could this insight spark a question, counterpoint, or reflection in dialogue with a human user? | Tied directly to your assistant’s design language |
| **Thematic Rarity** | Does this insight reflect a rare pattern, blind spot, or underrepresented theme? | Helps avoid cutting insights that may seem “niche” but are valuable for diversity of coverage |

## ChatGPT (2025-03-25T05:38:16.901543+00:00)

Thanks for providing such detailed context. I'll pause here to thoroughly digest and internalize this information. Once I'm ready, we can proceed with the next steps. Feel free to let me know when you'd like me to move forward or if you have any additional context or clarifications to share!

