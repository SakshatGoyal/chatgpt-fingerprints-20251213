# Active Concepts in Luminoso

## You (2025-01-20T07:09:13.523456+00:00)

in luminoso, what's the significance of 'active concepts'. I'm selecting active concepts but I'm not sure what happens next

## ChatGPT (2025-01-20T07:09:30.503879+00:00)

In Luminoso, **active concepts** play a central role in determining the focus of analysis and the insights generated. Here's a breakdown of their significance and what happens when you select them:

### **What Are Active Concepts?**
Active concepts are the specific ideas, themes, or topics that you identify as relevant or significant to your analysis. These concepts are typically chosen from the concepts detected in your dataset or added manually if they are important but not automatically detected.

### **What Happens When You Select Active Concepts?**
1. **Refining Focus**:
   By selecting active concepts, you're telling Luminoso to prioritize these concepts in its analysis. The system will emphasize these topics when:
   - Calculating relationships between concepts.
   - Building insights such as sentiment trends, importance, or unique associations.
   - Summarizing the dataset.

2. **Concept Relationships**:
   Luminoso evaluates how the active concepts relate to one another and to other concepts in the dataset. This includes:
   - Measuring **similarity** between concepts.
   - Identifying **hidden connections** or **clusters** that help you understand broader themes.

3. **Impact on Dashboards and Visualizations**:
   - The selection influences **concept maps**, **sentiment analysis**, and **impact scores**.
   - Key metrics like **salience** and **sentiment distribution** are highlighted for these concepts.

4. **Insight Prioritization**:
   Active concepts are more likely to feature in the **insights engine**, which surfaces trends, anomalies, and actionable insights.

5. **Filtering and Reporting**:
   Selecting active concepts allows you to filter reports or dashboards by these topics, making it easier to generate targeted outputs or presentations.

### **What Should You Do Next?**
After selecting active concepts, you can:
- **Explore Relationships**: Use the concept map or clustering tools to see how active concepts connect to others.
- **Review Sentiment and Trends**: Check if active concepts show significant sentiment shifts or trends over time.
- **Generate Insights**: Use the insights tab to discover what Luminoso reveals about your active concepts.
- **Export Reports**: Create targeted visualizations or summaries focusing on these concepts.

If you're unsure about your selection, you can experiment with different active concepts and observe how they change the analysis, then refine your choices as needed!

## You (2025-01-20T07:35:03.231371+00:00)

I'm trying to do a usability audit on Luminoso, the platform. Could you give me a series of use cases or 'keypaths' after the login step for me to evaluate the platform?

For your context, imagine I am a data analyst and I am using luminous so I have a copy of the Portland grocery store reviews and this is a combination of different data sets roughly 7000 data sets different data sets as far as the description of this goes this is a review of whole food, Trader Joe's, Safeway, new seasons, Fred Meyer, and a few more grocery outlets it says under description it says compare unique to different brands like Fred Meyer to Trader Joe's to see what the Portland market likes and dislikes about grocery stores so imagine a and less trying to make sense of this data through luminous so could you give me a few keypads or use cases that I can conduct my analysis on

## ChatGPT (2025-01-20T07:36:00.029567+00:00)

To conduct a **usability audit of Luminoso**, we can outline a series of **keypaths or use cases** that mimic the typical workflows a data analyst might follow to analyze a dataset like the Portland grocery store reviews. These keypaths will focus on critical user journeys, usability checkpoints, and feature interactions that you can evaluate step-by-step.

---

### **Keypaths and Use Cases for Usability Audit**

#### **1. Dataset Overview and Initial Exploration**
**Goal**: Understand the data and ensure it has been uploaded correctly.
1. **Log in and Load Project**: Open the Portland grocery store review dataset.
   - Evaluate the ease of navigating to existing projects.
   - Check if the dataset metadata (description, size, upload time) is displayed clearly.
2. **Dataset Summary**:
   - Verify that Luminoso summarizes key details (number of reviews, concepts extracted, etc.).
   - Evaluate whether important stats like sentiment distribution or concept counts are intuitive to access.
3. **Explore Dataset**:
   - Check if reviewing individual entries or sample data is straightforward.
   - Look for quick ways to validate data integrity or spot anomalies.

---

#### **2. Concept Identification and Active Concept Selection**
**Goal**: Identify key themes and focus the analysis.
1. **Explore Auto-Extracted Concepts**:
   - Evaluate if concepts are logically grouped and easy to understand.
   - Test if irrelevant or redundant concepts can be easily dismissed.
2. **Manually Add/Edit Concepts**:
   - Add custom concepts like specific store names (e.g., "Fred Meyer") or themes (e.g., "price").
   - Check if adding, renaming, or merging concepts is user-friendly.
3. **Select Active Concepts**:
   - Choose a mix of brand names (e.g., "Trader Joe's") and sentiment-driven themes (e.g., "quality of produce").
   - Test the platform’s feedback or guidance for selecting meaningful active concepts.

---

#### **3. Sentiment Analysis**
**Goal**: Understand customer sentiment for specific grocery stores and themes.
1. **View Sentiment Dashboard**:
   - Check if sentiment data is broken down by stores, themes, or time periods.
   - Evaluate how clear sentiment visualization is (e.g., bar charts, time-series graphs).
2. **Drill Down into Specific Themes**:
   - Analyze how sentiment for "price" compares between Trader Joe's and Safeway.
   - Test filtering options to refine data by store, product, or sentiment level.
3. **Export Insights**:
   - Export sentiment-related charts or raw sentiment data.
   - Evaluate the ease of creating shareable reports.

---

#### **4. Concept Relationships and Maps**
**Goal**: Identify connections between themes, brands, and topics.
1. **Concept Map**:
   - Evaluate how easy it is to interpret the concept map.
   - Test zoom, filtering, and customization options to isolate key clusters (e.g., connections between "customer service" and "Trader Joe’s").
2. **Similarity Analysis**:
   - Compare how similar Trader Joe’s reviews are to Whole Foods reviews.
   - Check if explanations for similarity scores are clear and actionable.
3. **Hidden Relationships**:
   - Investigate any unexpected connections (e.g., "organic produce" linked with "price complaints").
   - Test whether these connections can be highlighted and explored easily.

---

#### **5. Trends and Time-Based Analysis**
**Goal**: Analyze temporal patterns in reviews or sentiment.
1. **Sentiment Over Time**:
   - Evaluate if sentiment trends are displayed intuitively (e.g., line graphs showing changes for Trader Joe's vs. Fred Meyer).
2. **Thematic Changes**:
   - Check how mentions of themes like "quality" or "price" change across seasons.
   - Test filtering by specific time ranges (e.g., “last 6 months”).
3. **Export Trend Data**:
   - Export visualizations or data tables showing these trends.
   - Assess if exporting is smooth and supports common formats.

---

#### **6. Comparison and Benchmarking**
**Goal**: Compare performance across grocery store brands.
1. **Compare Concepts**:
   - Evaluate how themes like "price" or "quality" differ for Fred Meyer and Whole Foods.
   - Test if the platform provides clear metrics for comparison (e.g., sentiment scores, frequency of mentions).
2. **Identify Unique Attributes**:
   - Use Luminoso to identify what is unique to Trader Joe’s reviews versus Safeway’s.
   - Assess how actionable and interpretable the results are.
3. **Export Comparisons**:
   - Generate and export reports showing these comparisons.

---

#### **7. Insight Generation and Actionable Reports**
**Goal**: Surface key insights and prepare outputs for stakeholders.
1. **Explore Automatic Insights**:
   - Test how relevant and actionable the insights are (e.g., “Fred Meyer’s customer service has declining sentiment”).
   - Evaluate the clarity and usefulness of insight explanations.
2. **Customize Insight Generation**:
   - Adjust settings to generate more focused insights (e.g., restrict to "organic produce").
   - Test if customization options are intuitive and effective.
3. **Export and Share Insights**:
   - Create a report summarizing the findings (e.g., brand comparison, sentiment trends).
   - Evaluate if the exported report is polished and stakeholder-ready.

---

### **Evaluation Criteria for Usability**
- **Navigation**: Is it easy to move between steps in the workflow?
- **Clarity**: Are visualizations and metrics easy to interpret without prior expertise?
- **Interactivity**: Are filtering, sorting, and customization options intuitive and responsive?
- **Efficiency**: Can tasks be completed quickly with minimal friction?
- **Error Handling**: How does the platform handle errors, such as invalid concept selections or data uploads?
- **Guidance**: Does the platform offer help or tips for new users at each step?

---

These keypaths should give you a structured way to evaluate Luminoso’s usability and provide actionable feedback on how well it supports a data analyst's workflow.
