# Research Query Optimization

## You (2025-03-17T04:40:45.750000+00:00)

Hey Andrew, I need your prompt building capabilities to create a set of instructions. I've attached my current content at the bottom. 

A few things I want to modify:

1. I want the canvas output to have better formatting to make it more readable for me. Right now, the content is all in <p></p> format, which means there are no headings or any visual distinctions.  

2. Let's face it, search can be hit or miss. Currently, it's generating only a few search queries, but I'm concerned that being less comprehensive in the search queries can lead to missed opportunities in finding the right resources for my objective. I want more search queries than it's producing currently, and I also want them to be comprehensive, ensuring that ChatGPT examines it from multiple angles.  

3. For your reference, I’ll be inserting 'research themes.' Here's a sample of what a research theme looks like.
AI-Driven Product Innovation and Market Positioning
Key Questions to Investigate:
How should executives balance breakthrough product innovations with market positioning in a rapidly evolving tech landscape?
Which signals indicate that AI can uncover unmet customer needs?
How can competitive benchmarking be enhanced using AI insights?
Subcategories:
Product roadmap prioritization
Competitor intelligence via AI
Integration of customer feedback into R&D
Common Pain Points:
Rapid technological shifts and disruptive competitors
Difficulty aligning R&D investments with evolving market demands
Information overload in innovation decision-making
AI-Relevant Aspects:
Predictive analytics to forecast market trends
Natural language processing for sentiment analysis
Machine learning models to optimize feature development
Frameworks/Models:
Lean Startup and Agile Development
Ansoff Matrix for growth opportunities
-----

Here's my current prompt:

This project is designed to generate precise, structured research queries for any given research theme. The queries will be optimized for:

Google Scholar (academic papers)
Academic journals (HBR, Strategic Management Journal, Sloan Review, etc.)
Industry white papers (McKinsey, BCG, Deloitte, etc.)
The goal is to identify the best possible sources for each theme and construct well-formed search queries that enable a targeted and efficient literature review.

Each time I need search queries, I'll simply type:

Generate Search Queries
[Paste the Research Theme Below]
You will automatically apply the structured methodology and generate thorough search queries in canvas format for clarity.

Structured Approach for Generating Queries:
1️⃣ Analyze the Research Theme

Extract key concepts from the theme, including:
Key research questions
Subcategories & related concepts
Common pain points & challenges
AI-relevant aspects (if applicable)
Relevant frameworks or models
Identify relevant academic disciplines and industry perspectives.
2️⃣ Generate Google Scholar Queries

Construct Boolean search queries optimized for Google Scholar.
Use synonyms and alternate phrasings to enhance search breadth.
Ensure queries are thorough, covering multiple aspects of the theme.
Format example:
("core concept 1" OR "synonym 1") AND ("core concept 2" OR "synonym 2") AND ("challenge area" OR "impact factor")
Provide as many strong queries as necessary for a comprehensive search.
3️⃣ Generate Academic Source Queries

Identify the most relevant academic journals based on the theme.
Formulate targeted queries for top journals such as:
Harvard Business Review (site:hbr.org)
Sloan Management Review (site:sloanreview.mit.edu)
Strategic Management Journal (site:strategicmanagement.net)
Format example:
site:hbr.org "AI-driven strategic decision-making" AND ("executive judgment" OR "corporate governance")
Ensure multiple variations to cover all relevant aspects.
4️⃣ Generate Industry White Paper Queries

Identify the best consulting firms and research groups that may have relevant insights.
Construct search queries for firms such as:
McKinsey & Company (site:mckinsey.com)
Boston Consulting Group (site:bcg.com)
Deloitte Insights (site:deloitte.com)
Format example:
site:mckinsey.com "cloud transformation strategy" AND ("legacy migration" OR "hybrid cloud architecture")
Ensure a broad yet precise set of queries.
5️⃣ Ensure Thoughtfulness & Depth

Be creative yet methodical in forming queries.
Avoid limiting the number of queries—generate as many as necessary for a thorough search.
Consider alternative perspectives and edge cases.
Align queries with both theoretical and practical aspects of the theme.
Output Format (in Canvas)
Each response will be structured in canvas format for clarity, with queries categorized into:

Google Scholar Queries:

(...)
(...)
(...)
Academic Source Queries:

(...)
(...)
(...)
Industry White Paper Queries:

(...)
(...)
(...)

## ChatGPT (2025-03-17T04:40:46.564722+00:00)

Here's an improved version of your prompt with enhanced readability, better formatting, and more comprehensive search queries. The updated structure ensures clarity, and the search queries will be more exhaustive.

## ChatGPT (2025-03-17T04:40:48.641141+00:00)

{"name": "research_queries", "type": "document", "content": "**Optimized Research Query Generation Framework**\n\n### **Objective**\nThis framework generates precise, structured research queries for any given research theme. The queries are optimized for:\n- **Google Scholar** (academic papers)\n- **Academic Journals** (Harvard Business Review, Strategic Management Journal, Sloan Review, etc.)\n- **Industry White Papers** (McKinsey, BCG, Deloitte, etc.)\n\nThe goal is to **maximize research coverage** and **construct well-formed search queries** to enable a **targeted and efficient literature review**.\n\n---\n\n### **Usage Instructions**\nEach time search queries are needed, input:\n\n#### **Generate Search Queries**\n*Paste the Research Theme Below*\n\nThe structured methodology will be applied automatically to generate thorough search queries in a clearly formatted canvas output.\n\n---\n\n### **Structured Approach for Generating Queries**\n\n#### **1️⃣ Analyze the Research Theme**\n- Extract key concepts, including:\n  - **Key Research Questions**\n  - **Subcategories & Related Concepts**\n  - **Common Pain Points & Challenges**\n  - **AI-Relevant Aspects** (if applicable)\n  - **Relevant Frameworks or Models**\n- Identify **relevant academic disciplines and industry perspectives**.\n\n---\n\n#### **2️⃣ Generate Google Scholar Queries**\n- Construct **Boolean search queries** optimized for Google Scholar.\n- Utilize **synonyms and alternate phrasings** to expand search breadth.\n- Ensure **thorough coverage** of multiple aspects of the theme.\n\n**Format Example:**\n```\n(\"core concept 1\" OR \"synonym 1\") AND (\"core concept 2\" OR \"synonym 2\") AND (\"challenge area\" OR \"impact factor\")\n```\n- **Generate an extensive set of queries** to cover various angles.\n\n---\n\n#### **3️⃣ Generate Academic Source Queries**\n- Identify the **most relevant academic journals** for the theme.\n- Formulate **targeted queries** for top journals, such as:\n  - **Harvard Business Review** (site:hbr.org)\n  - **Sloan Management Review** (site:sloanreview.mit.edu)\n  - **Strategic Management Journal** (site:strategicmanagement.net)\n\n**Format Example:**\n```\nsite:hbr.org \"AI-driven strategic decision-making\" AND (\"executive judgment\" OR \"corporate governance\")\n```\n- **Ensure multiple variations** to comprehensively cover all relevant aspects.\n\n---\n\n#### **4️⃣ Generate Industry White Paper Queries**\n- Identify **leading consulting firms and research groups** that provide relevant insights.\n- Construct search queries for firms such as:\n  - **McKinsey & Company** (site:mckinsey.com)\n  - **Boston Consulting Group** (site:bcg.com)\n  - **Deloitte Insights** (site:deloitte.com)\n\n**Format Example:**\n```\nsite:mckinsey.com \"cloud transformation strategy\" AND (\"legacy migration\" OR \"hybrid cloud architecture\")\n```\n- **Generate a broad yet precise set of queries**.\n\n---\n\n#### **5️⃣ Ensure Thoughtfulness & Depth**\n- Be **creative yet methodical** in forming queries.\n- **Expand** the number of queries—generate as many as necessary for a **thorough search**.\n- Consider **alternative perspectives, edge cases, and industry nuances**.\n- Align queries with **both theoretical and practical aspects** of the theme.\n\n---\n\n### **Output Format (in Canvas for Clarity)**\nEach response will be structured in the following format:\n\n#### **Google Scholar Queries**\n- Query 1\n- Query 2\n- Query 3\n- ... *(as many as necessary)*\n\n#### **Academic Source Queries**\n- Query 1\n- Query 2\n- Query 3\n- ... *(as many as necessary)*\n\n#### **Industry White Paper Queries**\n- Query 1\n- Query 2\n- Query 3\n- ... *(as many as necessary)*"}

## ChatGPT (2025-03-17T04:41:16.495146+00:00)

The updated framework enhances readability with clear headings, structured sections, and improved formatting. It also ensures **more comprehensive search queries** by emphasizing alternative perspectives, broader coverage, and increased query variations. Let me know if you’d like any refinements!

## You (2025-03-17T04:47:47.591000+00:00)

Ok, here's the instructions I used:

**Optimized Research Query Generation Framework**

### **Objective**
Generate precise, structured research queries for any given research theme. The queries are optimized for:
- **Google Scholar** (academic papers)
- **Academic Journals** (Harvard Business Review, Strategic Management Journal, Sloan Review, etc.)
- **Industry White Papers** (McKinsey, BCG, Deloitte, etc.)

The goal is to **maximize research coverage** and **construct well-formed search queries** to enable a **targeted and efficient literature review**.

---

### **Sample Prompt from the User**
Each time search queries are needed, user will input:

Generate Queries
[User will paste research theme here]

The structured methodology will be applied automatically to generate thorough search queries in a clearly formatted canvas output.

---

### **Structured Approach for Generating Queries**

#### **1️⃣ Analyze the Research Theme**
- Extract key concepts, including:
  - **Key Research Questions**
  - **Subcategories & Related Concepts**
  - **Common Pain Points & Challenges**
  - **AI-Relevant Aspects** (if applicable)
  - **Relevant Frameworks or Models**
- Identify **relevant academic disciplines and industry perspectives**.

---

#### **2️⃣ Generate Google Scholar Queries**
- Construct **Boolean search queries** optimized for Google Scholar.
- Utilize **synonyms and alternate phrasings** to expand search breadth.
- Ensure **thorough coverage** of multiple aspects of the theme.

**Format Example:**
```
("core concept 1" OR "synonym 1") AND ("core concept 2" OR "synonym 2") AND ("challenge area" OR "impact factor")
```
- **Generate an extensive set of queries** to cover various angles.

---

#### **3️⃣ Generate Academic Source Queries**
- Identify the **most relevant academic journals** for the theme.
- Formulate **targeted queries** for top journals, such as:
  - **Harvard Business Review** (site:hbr.org)
  - **Sloan Management Review** (site:sloanreview.mit.edu)
  - **Strategic Management Journal** (site:strategicmanagement.net)

**Format Example:**
```
site:hbr.org "AI-driven strategic decision-making" AND ("executive judgment" OR "corporate governance")
```
- **Ensure multiple variations** to comprehensively cover all relevant aspects.

---

#### **4️⃣ Generate Industry White Paper Queries**
- Identify **leading consulting firms and research groups** that provide relevant insights.
- Construct search queries for firms such as:
  - **McKinsey & Company** (site:mckinsey.com)
  - **Boston Consulting Group** (site:bcg.com)
  - **Deloitte Insights** (site:deloitte.com)

**Format Example:**
```
site:mckinsey.com "cloud transformation strategy" AND ("legacy migration" OR "hybrid cloud architecture")
```
- **Generate a broad yet precise set of queries**.

---

#### **5️⃣ Ensure Thoughtfulness & Depth**
- Be **creative yet methodical** in forming queries.
- **Expand** the number of queries—generate as many as necessary for a **thorough search**.
- Consider **alternative perspectives, edge cases, and industry nuances**.
- Align queries with **both theoretical and practical aspects** of the theme.

---

### **Output Format (in Canvas for Clarity)**
Each response will be structured in the following format:

#### **Google Scholar Queries**
- Query 1
- Query 2
- Query 3
- ... *(as many as necessary)*

#### **Academic Source Queries**
- Query 1
- Query 2
- Query 3
- ... *(as many as necessary)*

#### **Industry White Paper Queries**
- Query 1
- Query 2
- Query 3
- ... *(as many as necessary)*

---- 

My concerns:

I think chatgpt is limiting it's responses to only search for resources mentioned. For example, based on the instructions

- **Academic Journals** (Harvard Business Review, Strategic Management Journal, Sloan Review, etc.)
- **Industry White Papers** (McKinsey, BCG, Deloitte, etc.)

It's only looking at McKinsey, BCG, Deloitte. or Harvard Business Review, Strategic Management Journal, Sloan Review. While it's good, since these sources are reliable, I want to make sure that we're not omitting potentially good resources due to limitations of instructions. Could you frame another detailed set of instructions similar to what I gave you, but ones that can address my concern.

## ChatGPT (2025-03-17T04:47:48.204926+00:00)

{"updates": [{"pattern": ".*", "replacement": "**Optimized Research Query Generation Framework**\n\n### **Objective**\nGenerate precise, structured research queries for any given research theme. The queries are optimized for:\n- **Google Scholar** (academic papers)\n- **Academic Journals** (Harvard Business Review, Strategic Management Journal, Sloan Review, and other relevant sources)\n- **Industry White Papers** (McKinsey, BCG, Deloitte, and additional authoritative sources)\n\nThe goal is to **maximize research coverage** and **construct well-formed search queries** to enable a **targeted and efficient literature review**, ensuring that **no valuable sources are overlooked**.\n\n---\n\n### **Sample Prompt from the User**\nEach time search queries are needed, user will input:\n\n#### **Generate Queries**\n*User will paste research theme here*\n\nThe structured methodology will be applied automatically to generate thorough search queries in a clearly formatted canvas output.\n\n---\n\n### **Structured Approach for Generating Queries**\n\n#### **1️⃣ Analyze the Research Theme**\n- Extract key concepts, including:\n  - **Key Research Questions**\n  - **Subcategories & Related Concepts**\n  - **Common Pain Points & Challenges**\n  - **AI-Relevant Aspects** (if applicable)\n  - **Relevant Frameworks or Models**\n- Identify **relevant academic disciplines and industry perspectives**.\n\n---\n\n#### **2️⃣ Generate Google Scholar Queries**\n- Construct **Boolean search queries** optimized for Google Scholar.\n- Utilize **synonyms and alternate phrasings** to expand search breadth.\n- Ensure **thorough coverage** of multiple aspects of the theme.\n\n**Format Example:**\n```\n(\"core concept 1\" OR \"synonym 1\") AND (\"core concept 2\" OR \"synonym 2\") AND (\"challenge area\" OR \"impact factor\")\n```\n- **Generate an extensive set of queries** to cover various angles.\n\n---\n\n#### **3️⃣ Generate Academic Source Queries**\n- Identify the **most relevant academic journals** for the theme.\n- Formulate **targeted queries** for well-regarded journals, such as:\n  - **Harvard Business Review** (site:hbr.org)\n  - **Sloan Management Review** (site:sloanreview.mit.edu)\n  - **Strategic Management Journal** (site:strategicmanagement.net)\n  - **Other authoritative academic and business research sources**\n- Ensure the inclusion of **additional high-quality sources** beyond the explicitly mentioned ones.\n\n**Format Example:**\n```\nsite:hbr.org \"AI-driven strategic decision-making\" AND (\"executive judgment\" OR \"corporate governance\")\n```\n- **Ensure multiple variations** to comprehensively cover all relevant aspects.\n\n---\n\n#### **4️⃣ Generate Industry White Paper Queries**\n- Identify **leading consulting firms, industry think tanks, and research groups** that provide relevant insights.\n- Construct search queries for well-regarded sources, such as:\n  - **McKinsey & Company** (site:mckinsey.com)\n  - **Boston Consulting Group** (site:bcg.com)\n  - **Deloitte Insights** (site:deloitte.com)\n  - **Additional reputable research organizations, government reports, and industry-specific white papers**\n- Ensure that searches include **a broader set of authoritative sources** beyond just the listed consulting firms.\n\n**Format Example:**\n```\nsite:mckinsey.com \"cloud transformation strategy\" AND (\"legacy migration\" OR \"hybrid cloud architecture\")\n```\n- **Generate a broad yet precise set of queries**.\n\n---\n\n#### **5️⃣ Ensure Thoughtfulness & Depth**\n- Be **creative yet methodical** in forming queries.\n- **Expand** the number of queries—generate as many as necessary for a **thorough search**.\n- Consider **alternative perspectives, edge cases, and industry nuances**.\n- **Ensure the inclusion of sources beyond those explicitly mentioned** to avoid omitting valuable insights.\n- Align queries with **both theoretical and practical aspects** of the theme.\n\n---\n\n### **Output Format (in Canvas for Clarity)**\nEach response will be structured in the following format:\n\n#### **Google Scholar Queries**\n- Query 1\n- Query 2\n- Query 3\n- ... *(as many as necessary)*\n\n#### **Academic Source Queries**\n- Query 1\n- Query 2\n- Query 3\n- ... *(as many as necessary)*\n\n#### **Industry White Paper Queries**\n- Query 1\n- Query 2\n- Query 3\n- ... *(as many as necessary)*"}]}

## ChatGPT (2025-03-17T04:48:15.746989+00:00)

I've updated your instructions to **ensure that research queries are not limited to the explicitly mentioned sources** but also include **other authoritative academic, industry, and consulting sources**. This adjustment broadens the search while maintaining quality and relevance. Let me know if you'd like further refinements!

