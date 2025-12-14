# AI-Driven Opportunity Synthesis

## You (2025-07-21T15:28:37.089000+00:00)

For a few minutes, I'd like you to think like a human-centered designer. Help me ideate.

The context here is we are designing an internal sales platform for account executives at Palo Alto Networks. In the screen I've shared with you, we are highlighting certain opportunities, which is the Salesforce opportunities that they have. And right now, we're just giving a very curated look. As you can see, they have a number of filters like time period, product, run, which indicates renewal, upsell, and net new, forecast category, sales stage, deal size, and risk category. The risk category correlates with the risk factors, and there can be multiple risk factors associated with an account, like mandatory professional services was removed, or no partner selected, or finalized, or low customer adoption, or customer health. So those kinds of risk factors for any individual deal.

One of the challenges we've encountered is the fact that because a user may have 120 or even 200 opportunities, an AI-generated summary would be too inactionable and almost remove the whole purpose of any AI-generated summary. So I'm trying to ideate on ways in which we can create some kind of AI synthesis, not a summary, that can actually be valuable. So one option was the fact that those summaries get generated as a user selects certain filters. For example, if they select a certain deal value size, then we get a synthesis only for those particular deal sizes. Additionally, if someone selects something like renewals under opportunity type, then it would basically synthesize all the deals that are renewal-centric.

One of the things we don't want to do is be too prescriptive because we want to respect the autonomy of an individual user. We understand that these are professionals and they know what's best. However, what we do want to figure out is what we can share. So, for example, we know we can't share things like next steps or things like recommendations or some kind of takeaway that would require a certain amount of creativity. Rather, we just want to report facts, report any underlying dichotomies, and we want to understand if there's a way to almost minimize the summary. And when I say minimize, I mean we don't want a synthesis that is one page long. We just need a few sentences that can tell any executive exactly where to look or point them in the right direction. So one of the approaches could be like exploring dichotomies, exploring some unobvious points of view or risks that are truly critical and need immediate attention.

For your context, I'm attaching some data guidelines for you.

1. **Account Name**


2. **Lifetime Value** (Total cumulative historical spend of the account)

3. **Value of the Last 3 Years** (Cumulative revenue from the last 3 years)

4. **Pipeline in Q4 FY25**

5. **Account Health** (Possible values: Healthy, At-Risk, Critical)

6. **Active POVs**

7. **EBCs in the Last Year**

8. **Risk Factors** (Multiple binary risk factors; assign logically, values listed below)

   * 📭 No Pipeline in CQ + Next 4Q (true/false)
   * 🏛️ No EBCs in last year (true/false, logically consistent with EBC count)
   * 🔌 Not Platformized (true/false; likely always false)
   * 🧪 Active POVs (true/false, logically consistent with POV count)
   * 🩺 Customer technical health is critical (true/false; logically consistent with account health)
   * 🛑 Customer adoption/deployment rate is low (true/false)
   * 🌀 No ASR / Stale ASR (true/false)
   * 🚧 No customer success plan (true/false)

9. **Platformizations** (Assigned logically based on opportunities; possible values: PRISMA, SASE, STRATA, CORTEX)

## ChatGPT (2025-07-21T15:28:38.215755+00:00)

Let's approach this with a human-centered design perspective focused on synthesis, not summary. Here are ideas for how AI-generated synthesis could provide high-value insights without overwhelming or being overly prescriptive:

### **1. Synthesis through Contrasts (Highlighting Dichotomies)**
Provide succinct insights by surfacing unexpected contrasts or outliers:

- **Examples:**
  - "High-value accounts ($1M+) have fewer EBC engagements compared to lower-value accounts."
  - "Accounts marked 'Critical' consistently lack ASR updates, whereas 'At-Risk' accounts primarily struggle with low adoption."

_Why it works:_
This quickly directs attention to unobvious but meaningful insights.

---

### **2. Filter-Driven Micro-Synthesis (Contextual)**
Generate concise insights only when users apply filters, reducing cognitive load and improving actionability:

- **Examples based on user filters:**
  - **Renewals Selected:** "75% of Renewal accounts are At-Risk, primarily due to low adoption rates."
  - **High-Value Selected:** "High-value deals in the pipeline frequently lack customer success plans."

_Why it works:_
Contextual synthesis respects autonomy, offering specific yet non-prescriptive insights linked explicitly to user interest.

---

### **3. Risk Clusters (Pattern Identification)**
Identify clusters of risk factors, enabling quick recognition of systematic issues:

- **Examples:**
  - "12 Accounts simultaneously experiencing 'low adoption' and 'critical technical health,' representing $5.5M in pipeline."
  - "High pipeline value is disproportionately concentrated in accounts without recent EBC engagement."

_Why it works:_
Clearly shows users where systematic interventions might be impactful without prescribing specific actions.

---

### **4. Anomaly Spotting (Unusual Activity Alerting)**
Automatically surface statistically unusual combinations or anomalies:

- **Examples:**
  - "Unusually high pipeline ($1.2M) paired with zero Active POVs in Vertex Transport Solutions."
  - "Critical-risk Orion Shipping shows high EBC engagement (12), yet retains multiple unresolved risk factors."

_Why it works:_
Pointing directly to anomalies helps executives intuitively know where deeper investigation is required.

---

### **5. Simple Comparative Benchmarks**
Provide synthesis through short comparative benchmarking between filtered accounts and historical averages or norms:

- **Examples:**
  - "Selected pipeline accounts average 3 risk factors, above the normal threshold (avg: 1.7)."
  - "Pipeline size for critical accounts significantly higher than historical norms, indicating concentration of risk."

_Why it works:_
Executives immediately grasp relative urgency or unusual shifts without needing comprehensive context.

---

### **6. Critical Priority Nudges** (Factual but not Prescriptive)
Surface factual statements that subtly guide attention without dictating next steps:

- **Examples:**
  - "Top three largest pipeline opportunities are all in Critical or At-Risk accounts."
  - "Nebula Logistics is the only large account with zero EBC activity."

_Why it works:_
Guides executives without explicit instructions, preserving autonomy while emphasizing priorities.

---

### **7. Dynamic Risk Spotlighting**
Highlight single critical risk factors that consistently appear across valuable segments:

- **Examples:**
  - "No customer success plan consistently emerges as the leading risk factor in high-value renewal opportunities."

_Why it works:_
Pinpoints exactly where systemic challenges appear, focusing attention on impactful risks.

---

### **Summary of Recommended Approach**
Combine these elements into a minimalist yet impactful design that only activates insights as relevant filters are applied. For instance:

- **On load:** No synthesis provided.
- **On filter selection:** Dynamic synthesis surfaces briefly at the top, only sharing unobvious insights, dichotomies, anomalies, or critical clusters.

By focusing synthesis on contrasts, anomalies, clusters, and context-driven insights, you'll respect executive autonomy, ensure actionability, and create genuine value without overwhelming users.
