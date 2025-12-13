# Product management assistant design

## You (2025-10-23T13:29:58.452000+00:00)

For the duration of this conversation, I want you to assume the role of a seasoned prompt and context engineer whose expertise is in prompt design for ChatGPT, specifically for agent mode, and during our discussion, we will be talking about potentially designing some prompts for product management-related activities.

## ChatGPT (2025-10-23T13:30:01.858550+00:00)

Perfect — I’m now in the role of a **seasoned prompt and context engineer** specializing in **ChatGPT prompt design for Agent Mode**, with a focus on **product management use cases**.  

Before we start, can you clarify what stage you’re at? For example:  

1. Are we designing **base prompts** (system-level scaffolding for a Product Manager agent)?  
2. Or are we working on **interaction prompts** (the dynamic, user-facing exchanges that guide how the agent behaves mid-session)?  
3. Or are you looking to **map the context architecture** — defining what context layers (e.g., product specs, sprint data, stakeholder personas) should feed into the agent to make it effective?  

Each path leads to a different design structure, so understanding your goal will help me set the right framework.

## You (2025-10-23T13:32:02.722000+00:00)

Yeah, I think what we are trying to do, or rather what I am trying to do, is... I have a certain task, essentially, and we do identify use cases. And I want the agent to essentially go to very different websites, gather some information, synthesize it, and then turn that into use cases for a product design exercise. So, that's the idea.

## ChatGPT (2025-10-23T13:32:07.428643+00:00)

Got it — so you’re designing an **agentic Product Management assistant** that can:  

1. **Go out into the web**,  
2. **Collect and synthesize information** (market, competitors, customer insights, etc.), and  
3. **Turn those insights into structured product use cases or design prompts.**  

That’s a really solid and high-leverage workflow.  

Let’s establish the **prompt design architecture** first — a mental blueprint for how the agent should think and operate. For this kind of task, I’d suggest structuring the agent around **four context layers**:  

---

### 🧩 1. **Mission Layer (Core Instruction)**
Defines what the agent *is fundamentally for*.

> **Example:**
> “You are a Product Management Research Agent. Your job is to gather live insights from multiple sources across the web (news, company blogs, review sites, forums, etc.), synthesize key findings, and translate them into actionable use cases for product design teams.”

This sits in the **system prompt** and never changes.  

---

### 🧱 2. **Context Layer (Working Memory / Project Scope)**
This layer injects the **product theme**, **target audience**, and **goals** of the current project.

> **Example:**
> “We are designing a new AI-powered analytics dashboard for small e-commerce businesses. The goal is to identify top pain points, unmet needs, and use cases by studying existing solutions (like Shopify, Wix, and Google Analytics).”

You’ll often inject or update this layer per project run.  

---

### 🧠 3. **Behavioral Layer (Agent Personality + Reasoning)**
Defines *how* the agent should think and act when exploring and summarizing.

> **Example:**
> “When researching, prioritize structured data and real customer language. Synthesize findings in a hierarchy:
> 1. Observation (raw insight)
> 2. Interpretation (why it matters)
> 3. Implication (how it could inform a use case)
> Be skeptical of marketing fluff. When uncertain, note confidence levels.”

This keeps the synthesis rational and product-centric.  

---

### ⚙️ 4. **Output Layer (Deliverable Format)**
Specifies *how* the final output should look — usually in a structured, re-usable schema.

> **Example Output Schema:**

| Use Case Title | Source(s) | User Problem | Insight Summary | Feature Concept | Confidence |
|----------------|------------|---------------|-----------------|----------------|-------------|
| “One-click sales insights” | Shopify, Reddit, G2 | SMB owners waste time compiling reports | Users want quick sales summaries with zero setup | Add auto-summary dashboard card | High |

---

### 🔄 How Agent Mode Fits
Once the prompt is structured like this, **Agent Mode** handles:
- Navigating to sites (Reddit, G2, company blogs, etc.)
- Extracting info
- Compiling and structuring it according to the prompt
- Returning the synthesized use cases in the given schema

---

Would you like me to **design the base system prompt** for this Product Management agent next (so you can drop it directly into Agent Mode)?  
Or do you want to **refine the architecture** a bit further — maybe define what kind of research or use-case depth you expect per run (e.g., “10 use cases per product vertical”)?

