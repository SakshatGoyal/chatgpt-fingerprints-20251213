# AI Paper Synthesis Guide

## You (2025-03-18T09:30:05.172000+00:00)

Could you go through all of this content and develop a clear, thorough, and detailed set of instructions for the o3 reasoning AI model focusing on synthesizing papers and extracting insights? This is a document that my colleague and I have been collaborating on. We considered various strategies, and I included some comments for his reference about my needs. I suspect there has been some miscommunication, making it easier to form a new prompt from the ground up. Still, I want to ensure that the prompt reflects my feedback provided in the comments, as well as the extra notes. I want to make sure the prompt marries all the things that I love about my coworker's prompt, along with the things i love about my prompt. 

For now, please focus on being thorough without worrying about conciseness. We can trim it down later. 
-----

# Your Proposal

> Use this as a reference for my comments on your current suggestion of the prompt.
> 

Objective: Extract high-value executive decision-making insights from this research. Summarize key findings, but also critically analyze them. Do not merely describe business trends—focus on how executives think, what influenced their decisions, and what strategic reasoning they used.

<aside>
💡

I like how you’ve defined the objective. It’s concise enough, and focuses on the real research objective is. 

</aside>

**Context:**

You are an investigative analyst summarizing research for Fortune 500 executives. Your insights must be:

- **Decision-Relevant** – Focus on how executives think, react, and strategize.
- **Analytically Rigorous** – Identify biases, cognitive models, or flawed assumptions.
- **Cross-Industry Applicable** – Extract strategic patterns that could apply to multiple industries.

<aside>
💡

I like the first two points in your context. But I wonder, how do we prevent ChatGPT from making assumptions? It's one thing to infer and deduce something, but I’m worried that if we give explicit instructions, is there a possibility that ChatGPT could make things up just to follow my instructions?

</aside>

**For each paper, follow this structured approach:**

1️⃣ **What was the key strategic decision or dilemma?**

- Clearly state the core decision executives faced in this study.
- Identify whether the decision was **reactive (crisis-driven) or proactive (long-term growth strategy).**

2️⃣ **What assumptions were executives working under?**

- Identify the explicit and **implicit biases or mental models** at play.
- What factors were executives **overestimating, underestimating, or ignoring?**

4️⃣ **How does this insight connect to other industries?**

- Is this strategy **industry-specific** or could it apply elsewhere?
- Provide a **real-world example from another industry** that illustrates a similar decision-making process.

5️⃣ **What was the outcome, and did it validate or contradict the executives’ assumptions?**

- Describe **whether their expectations matched reality.**
- If their decision was flawed, **what could have improved their reasoning?**

<aside>
💡

I think these points are valid. 

</aside>

3️⃣ **What alternative explanations could exist?**

- Challenge the study’s conclusions. Could these findings be **flawed, incomplete, or situation-dependent?**
- Provide **one or two counterfactual possibilities**.

<aside>
💡

I thought we were leaving counterfactual elements for the second step. Lets keep this as Step 1B. 

</aside>

**Deliverable Format:**

🔹 **INSIGHT:** [Concise but deep insight]

🔹 **ASSUMED STRATEGY:** [What executives believed at the time]

🔹 **ACTUAL OUTCOME:** [What actually happened]

🔹 **IMPLICATIONS & LEARNINGS:** [Why this matters, what patterns emerge]

🔹 **COUNTERFACTUAL TESTING:** [What if the opposite had happened?]

<aside>
💡

I don’t necessarily like this format. However, I find all the aspects you’re discussing here extremely critical. I do like the questions you’re asking here, so I wonder if there’s a way to get these kind of questions answered, but not in the format you’ve proposed. But leave counterfactual testing for Step 1B. 

</aside>

# Current Prompt

> Use this as a reference for things I like in my current prompt for summarizing research papers.
> 

Develop in-depth and analytically rigorous summaries of scholarly research papers intended for executives of Fortune 500 corporations, senior organizational leaders, and doctoral-level scholars. Each summary must effectively articulate strategic implications, operational considerations, and theoretical advancements, employing a sophisticated, analytical narrative informed by Robert Greene’s analytical yet compelling writing style. Insights provided should be strongly grounded in empirical data, thoughtfully constructed to provoke critical reflection, and clearly demarcated from speculative or theoretical assertions.

### Required Structure

Each summary must begin explicitly by stating:

## **Title of Paper**

**Author(s):** First Name, Last Name; First Name, Last Name

**Published:** (DD, Month, YYYY)

<aside>
💡

regardless of additional factors, I always want the output to return the title of the paper in h2, and then the authors and other details in the same format. This makes it easier for me when I’m going through content. 

</aside>

### Abstract

Construct a concise abstract clearly delineating:

1. **Identify Key Themes:** What are the central ideas the authors are exploring?
2. **Uncover Core Motivations:** What critical organizational, strategic, or theoretical challenge does this research aim to address?
3. **Methodological Clarification:** What data collection and analysis techniques were used, and how do these methods influence the reliability of insights?
4. **Assess Relevance:** In what ways does this research connect to contemporary industry practices or challenges?

<aside>
💡

This has been very helpful, especially for understanding research papers. It's often very important to me to grasp these aspects. While we have some research papers in our data collection, most are whitepapers, and some are newspaper articles. 

</aside>

### Insight Presentation

The body of the summary should comprise multiple distinct sections structured as follows:

- **Insight Statement:**
    
    Before drafting an insight, perform these steps:
    
    1. **Challenge Assumptions:** Identify and question the implicit assumptions that underlie the research findings. Ask: *What might this data overlook? What perspectives are absent?*
    2. **Reverse the Narrative:** Imagine the opposite outcome had occurred. What would that reveal about the core insight?
    3. **Stress Test the Implication:** Evaluate how robust the conclusion is under extreme or unconventional scenarios. Ask: *Would this still apply if circumstances shifted dramatically?*
    
    Example Insights:
    
    "**While most experts conclude that taking short breaks is vital to stay productive, participants from the study continued to see short breaks as unimportant and avoidable.**"
    
    "**Although people felt a bit of regret for missing certain talks or workshops, the overwhelming abundance of AI-related content available elsewhere diluted any urgency to catch up.**"
    

<aside>
💡

This part is also very important to me. I’ve tried many different ways of writing insights, but I’ve found this to be the most effective method for drawing out impactful, thought-provoking insights from a research paper. 

</aside>

- **Supporting Context Paragraph:**
    
    Before writing the supporting context:
    
    1. **Trace the Data's Journey:** Identify key data points, their sources, and any transformations they underwent before conclusions were drawn.
    2. **Clarify Uncertainty:** Ask: *What known limitations or unexplored variables might reduce the reliability of this finding?*
    3. **Identify Hidden Bias:** Assess whether the methodology inadvertently favored specific outcomes or groups.

Each insight and supporting paragraph should maintain a balance between conciseness and comprehensiveness, exemplified as follows:

"**Perceived ease of use is the most influential factor in SaaS adoption from an individual perspective, emphasizing the importance of user-friendly interfaces and minimal effort requirements.**

The study highlights perceived ease of use as a critical factor influencing SaaS adoption among individuals. This factor is determined primarily by end-users rather than managerial levels, indicating that users' perceptions of ease and effortlessness significantly drive adoption decisions. The research analyzed eight articles that consistently pointed to ease of use as a major determinant, suggesting that SaaS providers should prioritize intuitive, accessible designs to enhance adoption rates."

<aside>
💡

Once again, the supporting paragraph serves as a reference for me. It's common for more significant information to emerge from these contextual paragraphs. Moreover, since the key insights are deliberately thought-provoking, I consistently depend on this supporting paragraph to provide essential context. It also enhances my understanding of follow-up questions and related topics to consider. 

</aside>

Conclusion

- Clearly and succinctly reiterate the critical insights.
- Explicitly highlight strategic and operational implications relevant to senior executives and decision-makers.
- Briefly summarize notable methodological limitations highlighted by the authors.
- Identify explicit areas for future scholarly investigation, clearly defining both applicability and research boundaries.

<aside>
💡

The conclusion is good, but I don’t think we’ll necessarily need this in our work. 

</aside>

### Guidelines and Constraints

- Employ deliberate "think through" steps before articulating insights to ensure nuanced, critical reflection. Before finalizing any summary, ensure that all references to external ideas, data points, or conceptual frameworks are explicitly attributed through in-text citations. Citations should follow MLA guidelines and be integrated naturally within the narrative to maintain clarity and flow.
- Ensure precise, thorough, and transparent handling and reporting of quantitative metrics. Clearly indicate simplifications or approximations.
- Explicitly distinguish empirical results from speculative or theoretical insights.
- Avoid redundancy, ensuring all insights provided are distinct, substantive, and uniquely valuable.
- Maintain comprehensiveness; do not omit critical insights for brevity alone.
- Uphold rigorous academic standards by employing consistent numbered in-text citations throughout the response. Each referenced idea, insight, or conclusion must be clearly linked to its source. Use inline citations immediately following the referenced content, ensuring clarity on what is being cited. Conclude each summary with a comprehensive MLA-formatted reference list that includes all cited works.
- Give me the summary in canvas

<aside>
💡

Maintaining comprehensiveness, and not vomiting critical insights for brevity alone is probably the most important instruction in this prompt, despite it being placed towards the end. The remaining guidelines and constraints are also equally important and relevant for every output. 

</aside>

# Additional Factors we should consider

> Here’re some details about the forms of thematic analysis we should consider exploring to get the best output. This is how I want the model to think while extracting insights.
> 

## Interpretive and Contextually Rich Approaches

### Inductive (Data-Driven) Thematic Analysis

In inductive thematic analysis, approach your data openly, without predetermined categories or theoretical biases. Carefully and repeatedly engage with the data, allowing patterns and themes to surface organically. This method enables the discovery of novel insights that existing theories may overlook. Maintaining reflexivity is crucial to represent participants' experiences and meanings authentically.

### Latent Thematic Analysis

Latent thematic analysis involves moving beyond explicit content to identify deeper, implicit meanings and assumptions within your data. Focus on interpreting subtext, hidden ideas, or unspoken assumptions. Contextualize these deeper meanings within broader theoretical or socio-cultural frameworks to enrich interpretation. Clearly document your interpretive rationale to enhance analytic transparency and rigor.

### Constructionist Thematic Analysis

With a constructionist approach, recognize that meanings within your data are socially constructed through context, language, and discourse. Analyze how narratives and participant accounts reflect broader societal structures and power dynamics. Explicitly link your thematic interpretations to social contexts and critically evaluate how societal norms influence individual experiences.

### Reflexive Thematic Analysis

Reflexive thematic analysis emphasizes continuous reflection on your role as a researcher and how your perspectives shape thematic identification. Transparently document how your background, biases, and interpretative frameworks influence your analysis. Iteratively refine your themes through systematic reflection to ensure analytical integrity.

# Suggestions on how to write for o3

> I did a lot of research on things to keep in mind while writing for o3. Lets see if we can capitalize on these strategies while writing a prompt.
> 

### 1. Understand Your Model’s Capabilities and Constraints

**Strategy:**

Recognize that reasoning models (O3 and O1) are tuned to generate a chain of thought and provide transparent intermediate steps. Unlike standard GPT prompts, your prompt should explicitly ask the model to break down its thought process.

**Example:**

Instead of asking,

- “What is the main theme of this document?”ask,
- “Please analyze the document by listing the key topics, explaining how the text supports each, and then summarize the overarching theme.”

*(This builds on guidelines from reasoning best practices that emphasize stepwise transparency .)*

---

### 2. Clearly Define the Objective and Context

**Strategy:**

Begin your prompt by clearly stating the end goal and providing necessary context. This ensures the model understands the boundaries of the task and reduces ambiguity.

**Example:**

“Your task is to perform an inductive thematic analysis on the provided dataset. First, list the major recurring topics, then identify the connections among them, and finally, provide a summary that explains the latent themes—all using only the data provided.”

*(This approach mirrors recommendations from the ‘Using reasoning for data validation’ guidelines, where clarity of the goal reduces misinterpretation .)*

---

### 3. Instruct Explicit Chain-of-Thought Reasoning

**Strategy:**

Directly ask the model to “think out loud” by requesting that it reveals its intermediate reasoning steps before arriving at a final answer. This makes the process transparent and easier to review or debug.

**Example:**

“Before presenting your final conclusion, break down your analysis into three steps:

1. Identify and list all the key data points.
2. Group these data points into potential themes with justifications.
3. Synthesize a final summary explaining how these themes interconnect.Finally, provide your overall conclusion.”

*(This method is key in prompts designed for reasoning models, as it forces the model to reveal its thought process rather than jumping straight to an answer .)*

---

### 4. Specify Structured Intermediate Steps and Validation

**Strategy:**

Encourage the model to validate its own reasoning. Ask it to double-check intermediate conclusions for consistency and logical coherence before finalizing its answer.

**Example:**

“After completing each step of your analysis, briefly review your reasoning. For instance, after grouping data points into themes, confirm that every data point has been accounted for and that the grouping is logically sound. Then, provide the final summary.”

*(This strategy helps build guardrails against hallucinations by promoting self-verification, as highlighted in discussions about developing hallucination guardrails .)*

---

### 5. Provide In-Context Examples and Formatting Guidelines

**Strategy:**

Embed a mini-example in your prompt to illustrate the desired output format and the level of detail expected. This example serves as a template for the model to follow.

**Example:**

“Example:

- **Step 1:** Identify data points such as ‘increase in sales,’ ‘customer feedback,’ and ‘market trends.’
- **Step 2:** Group these into themes like ‘Market Growth’ and ‘Customer Satisfaction’ with a note: ‘Sales increased due to improved customer service.’
- **Final Summary:** The data suggests enhanced customer satisfaction drives market growth.Now, please perform the same analysis on the provided dataset.”

*(Providing an example is a well-known prompt engineering best practice, especially when aiming for detailed inductive or thematic analysis .)*

---

### 6. Guard Against Overgeneralizations and Hallucinations

**Strategy:**

Explicitly instruct the model to note uncertainty if evidence is lacking. This helps prevent it from inventing details or overgeneralizing.

**Example:**

“If you encounter ambiguous or incomplete data, state your uncertainty (e.g., ‘the data does not provide enough evidence to confirm this hypothesis’), rather than assuming an answer.”

*(This precaution is aligned with best practices for creating hallucination guardrails, ensuring that reasoning remains anchored to the provided data .)*

---

### 7. Encourage Iterative Refinement and Metacognition

**Strategy:**

Invite the model to reflect on its reasoning process and suggest improvements. This will not only strengthen the final answer but also aid in identifying any logical gaps.

**Example:**

“Once you have completed your analysis, please briefly reflect on your reasoning process. Identify any steps that might be improved or reconsidered for clarity, and then restate your final conclusion incorporating any insights gained from this reflection.”

*(This approach is particularly useful for complex tasks where iterative refinement can lead to more robust analytical outcomes, as emphasized in routines for data validation and routine generation*

# Information for you.

> here, i’m going to give you some suggestions on how i want your response.
> 

While writing your prompt, I’d like you to communicate your instructions with a few markers for different sections. Depending on the structure of your message, you could use *** or ### variably. While writing, I want you to keep two opposing thoughts in your mind. 

1. we need to make sure that ChatGPT knows all about how we want the output, how we want it to think, and what we want to achieve. Structure is key, but so is the way we want it to think. so make sure you provide as much information as you can. 
2. A concise, well-structured prompt often outperforms a sprawling prompt that’s trying to do too much. Long prompts can confuse the model or introduce unintended biases – the core question or instruction might get lost in the noise.

## ChatGPT (2025-03-18T09:30:05.839804+00:00)

Here's a thorough, detailed set of instructions that carefully synthesizes everything you've provided. It includes clear, stepwise guidance for the **o3 reasoning AI model**, incorporates your feedback from comments, preserves the core of your and your colleague's preferred structures, and emphasizes rigorous reasoning and analytical depth.

## ChatGPT (2025-03-18T09:30:13.610221+00:00)

{"content_type": "code", "language": "json", "response_format_name": null, "text": "{\"name\":\"o3_insight_prompt\",\"type\":\"document\",\"content\":\"### Objective\\n\\nYou are an investigative analyst tasked with synthesizing scholarly research papers, whitepapers, and strategic articles into analytically rigorous, decision-relevant insights targeted toward executives at Fortune 500 corporations and senior organizational leaders. Your goal is to uncover nuanced patterns about executive decision-making processes, strategic reasoning, and cognitive models driving executive choices.\\n\\n**Your insights must:**\\n\\n- Focus explicitly on executive thought processes, strategic reasoning, and influential factors behind decisions.\\n- Critically analyze implicit biases, cognitive models, flawed assumptions, and reasoning gaps.\\n- Clearly separate empirical evidence from speculative assertions, explicitly marking uncertainty when evidence is insufficient.\\n\\n---\\n\\n### Required Format\\n\\nAlways begin each summary as follows:\\n\\n## Title of Paper\\n\\n**Author(s):** First Name, Last Name; First Name, Last Name\\n\\n**Published:** DD, Month, YYYY\\n\\n---\\n\\n### Analytical Abstract\\n\\nConstruct a concise, informative abstract addressing:\\n\\n1. **Key Themes:** Clearly identify central themes explored.\\n2. **Core Motivations:** Describe organizational, strategic, or theoretical challenges driving the research.\\n3. **Methodological Clarification:** Summarize data collection and analysis methods, explicitly noting implications on reliability and applicability.\\n4. **Relevance Assessment:** Connect findings to contemporary industry challenges or executive concerns.\\n\\n---\\n\\n### Insight Extraction Process\\n\\nFollow these structured reasoning steps explicitly to arrive at analytically deep insights:\\n\\n#### Step 1: Identify Core Strategic Decision or Dilemma\\n\\n- Clearly articulate the strategic decision or dilemma faced by executives.\\n- Specify whether the decision was reactive (crisis-driven) or proactive (long-term strategy).\\n\\n#### Step 1B: Counterfactual & Alternative Explanations\\n\\n- Immediately after identifying the strategic decision, challenge initial conclusions by:\\n  - Suggesting 1-2 counterfactual scenarios (\\\"what if the opposite had occurred?\\\").\\n  - Identifying alternative explanations or overlooked variables influencing executive reasoning.\\n\\n#### Step 2: Assumption & Bias Analysis\\n\\n- Explicitly state executives’ underlying assumptions, highlighting implicit biases, cognitive models, or reasoning gaps.\\n- Analyze what executives potentially overestimated, underestimated, or completely overlooked.\\n\\n#### Step 3: Cross-Industry Connection\\n\\n- Determine whether insights are uniquely industry-specific or broadly applicable.\\n- Provide one clear, concrete example from another industry illustrating similar strategic reasoning.\\n\\n#### Step 4: Outcome Validation\\n\\n- Explicitly describe the actual outcomes and whether they confirmed or contradicted executive assumptions.\\n- Clearly articulate gaps or flaws in executive reasoning if outcomes differed from expectations.\\n\\n#### Step 5: Reflective Verification\\n\\n- Briefly reassess your analysis for logical coherence and data completeness.\\n- Transparently state uncertainty or limitations encountered.\\n\\n---\\n\\n### Delivering Analytical Insights\\n\\nPresent insights and supporting context in the following structured manner (maintaining the distinction you prefer between insight statements and supporting paragraphs):\\n\\n**Insight Statement:** (Concise, provocative analytical statement derived from your reasoning process)\\n\\n_Before writing, explicitly challenge assumptions, reverse narrative logic, and stress-test implications to confirm analytical robustness._\\n\\n**Supporting Context Paragraph:** (Detailed explanation grounding insight in empirical evidence)\\n\\n_Explicitly trace data points, clarify uncertainties, and identify potential hidden biases or methodological limitations._\\n\\n---\\n\\n### Reasoning Guardrails\\n\\nTo prevent unfounded speculation and ensure rigorous analysis:\\n\\n- Clearly mark speculative assertions or hypotheses as \\\"theoretical\\\" or \\\"uncertain\\\" unless firmly supported by data.\\n- Explicitly avoid assumptions unsupported by evidence.\\n- Transparently indicate when data is insufficient to validate a claim.\\n\\n---\\n\\n### Analytical Approaches to Consider\\n\\nUtilize inductive and interpretative methods:\\n\\n- **Inductive Thematic Analysis:** Allow themes and patterns to organically emerge from the data without pre-existing biases.\\n- **Latent Thematic Analysis:** Move beyond explicit content to uncover implicit meanings, hidden assumptions, and deeper motivations.\\n- **Constructionist Analysis:** Contextualize narratives within broader social and strategic contexts to reveal underlying power structures and socio-cultural influences.\\n- **Reflexive Analysis:** Continuously reflect on your analytical biases, explicitly documenting their potential influence on your insights.\\n\\n---\\n\\n### Guidelines and Constraints\\n\\n- Maintain comprehensiveness; do not omit critical insights for brevity alone.\\n- Precisely attribute all external ideas, data, or frameworks via numbered MLA-style in-text citations.\\n- Ensure clarity and transparency when simplifying complex data or approximating metrics.\\n- Clearly distinguish between empirical results and speculative assertions.\\n- Avoid redundancy; ensure each insight is distinct and substantively valuable.\\n\\n---\\n\\n### Iterative Refinement\\n\\nAfter concluding your analysis:\\n\\n- Briefly reflect on the reasoning process.\\n- Clearly state any potential areas of improvement or uncertainty.\\n- Incorporate any additional insights from this reflective evaluation into your final conclusion.\\n\\n---\\n\\n### Final Output Instructions\\n\\n- Deliver your completed summary via Canvas.\\n- Maintain the specified formatting to facilitate easy review and synthesis.\"}"}

## ChatGPT (2025-03-18T09:31:40.708571+00:00)

I've created a comprehensive prompt reflecting your detailed feedback and analytical goals. Let me know if there's anything you'd like adjusted or refined further!

## You (2025-03-18T09:52:30.630000+00:00)

Add some final polish to the text. If relevant, add a large title or any section titles. Check grammar and mechanics, make sure everything is consistent and reads well. You can reply that you added some final polish and checked for grammar, but do not mention the prompt.

## ChatGPT (2025-03-18T09:52:31.890407+00:00)

{"content_type": "code", "language": "json", "response_format_name": null, "text": "{\"updates\":[{\"pattern\":\".*\",\"multiple\":false,\"replacement\":\"# Analytical Insight Extraction Guide\\n\\n## Objective\\n\\nYou are an investigative analyst tasked with synthesizing scholarly research papers, whitepapers, and strategic articles into analytically rigorous, decision-relevant insights for executives at Fortune 500 corporations and senior organizational leaders. Your goal is to"}

