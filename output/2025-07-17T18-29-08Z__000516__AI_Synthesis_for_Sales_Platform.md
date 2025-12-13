# AI Synthesis for Sales Platform

## You (2025-07-17T18:29:08.016000+00:00)

{'content_type': 'image_asset_pointer', 'asset_pointer': 'file-service://file-8ouSA3wp1rX9TZN4tt94Uy', 'size_bytes': 580526, 'width': 2048, 'height': 1946, 'fovea': None, 'metadata': {'dalle': None, 'gizmo': None, 'generation': None, 'container_pixel_height': None, 'container_pixel_width': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'lpe_keep_patch_ijhw': None, 'lpe_delta_encoding_channel': None, 'sanitized': True, 'asset_pointer_link': None, 'watermarked_asset_pointer': None, 'is_no_auth_placeholder': None}}
[media pointer="file-service://file-MfXrF9dnN6xEGEHs4NZt5i"]
For a few minutes, I'd like you to think like a human-centered designer. Help me ideate.  

The context here is we are designing an internal sales platform for account executives at Palo Alto Networks. In the screen I've shared with you, we are highlighting certain opportunities, which is the Salesforce opportunities that they have. And right now, we're just giving a very curated look. As you can see, they have a number of filters like time period, product, run, which indicates renewal, upsell, and net new, forecast category, sales stage, deal size, and risk category. The risk category correlates with the risk factors, and there can be multiple risk factors associated with an account, like mandatory professional services was removed, or no partner selected, or finalized, or low customer adoption, or customer health. So those kinds of risk factors for any individual deal.

One of the challenges we've encountered is the fact that because a user may have 120 or even 200 opportunities, an AI-generated summary would be too inactionable and almost remove the whole purpose of any AI-generated summary. So I'm trying to ideate on ways in which we can create some kind of AI synthesis, not a summary, that can actually be valuable. So one option was the fact that those summaries get generated as a user selects certain filters. For example, if they select a certain deal value size, then we get a synthesis only for those particular deal sizes. Additionally, if someone selects something like renewals under opportunity type, then it would basically synthesize all the deals that are renewal-centric.

One of the things we don't want to do is be too prescriptive because we want to respect the autonomy of an individual user. We understand that these are professionals and they know what's best. However, what we do want to figure out is what we can share. So, for example, we know we can't share things like next steps or things like recommendations or some kind of takeaway that would require a certain amount of creativity. Rather, we just want to report facts, report any underlying dichotomies, and we want to understand if there's a way to almost minimize the summary. And when I say minimize, I mean we don't want a synthesis that is one page long. We just need a few sentences that can tell any executive exactly where to look or point them in the right direction. So one of the approaches could be like exploring dichotomies, exploring some unobvious points of view or risks that are truly critical and need immediate attention.

For your context, I'm attaching some data guidelines for you. 
🔹 Opportunity Metadata
account_name: a realistic company name
activeQuote_id: [Q-00XXX]
Opportunity_name: [how a typical opportunity might look like in salesforce for PaloAlto Networks
opportunity_amount: [can be any amount for an enterprise customer at PANW]
opportunity_type: [Net New, or Upsell, or Renewal, or Renewal and Upsell]
days_to_close: 38 (numeric)


🔹 Sales Stage & Pipeline Info
pipeline_status: [Pipeline, or Best Case, or Commit]
sales_stage: [Stage 4 – Negotiate
Stage 3 – Solution
Stage 5 – Purchase
Stage 2 – Discovery]

🔹 Product Components
product_components: a combination of [Firewall
CDSS
SASE
Cortex & Cloud
Unit 42}

can be any combination. it can be 1 or 5 or anything in between. 

🔹 Health & Risk
account_health: [Healthy, or Critical, or At-risk]
risk_factor_count: [I want the numeric, and a combination of the following:

📭 No Pipeline in CQ + Next 4Q
🏛️ No EBCs in last year
🏅 No Secured technical win
🤝 No Partner selected or finalized 
🩺 Customer technical health is critical.
🛑 Customer adoption/deployment rate is low
🧑‍💻 Mandatory PS was removed
⌛ Quotes pending approval
💲 Budget conversation not scheduled or complete
🔁 Term length less than 3 years or without financing/billing plans being proposed 
💤 No activity for last 30 days ]

---

## ChatGPT (2025-07-17T18:29:09.661287+00:00)

Here are several ideas to explore, anchored in a human-centered design approach, that could make AI-generated synthesis actionable and succinct without being prescriptive:

### 1. **Highlight Outlier Patterns**
   - Rather than summarizing all data, identify clear outliers or exceptions (e.g., "All your large renewal deals over $1M are healthy except SprintRay, which is at-risk due to pending technical POV."). This immediately directs attention toward anomalies worth deeper inspection.

### 2. **Context-Aware Dichotomies**
   - Provide concise contrasts between similar deals with differing risk profiles:
     - "Of your renewal opportunities closing in 60 days, 5 are Healthy, but 3 critical deals (e.g., Capstone Logistics) require immediate attention due to incomplete budget conversations."

### 3. **Time Sensitivity Indicators**
   - Synthesize time-based urgency clearly:
     - "Within opportunities closing in the next 30 days, 2 deals remain in negotiation, and both have critical health due to delayed approvals and inactivity exceeding 30 days."

### 4. **Dynamic Focus Statements**
   - Dynamically alter the synthesis based on selected filters. For instance, when filtering by risk category, synthesis explicitly calls out priority areas:
     - "You've filtered for high-risk renewals: 4 deals require immediate budget or partner resolution."

### 5. **Minimalist Risk Spotlight**
   - Limit the synthesis to a single, highly impactful insight per applied filter:
     - "Largest renewal deal (Capstone Logistics, $2.4M) is flagged Critical: Budget conversation urgently needed."

### 6. **Action-oriented Framing Without Prescriptiveness**
   - Present factual urgency without explicit recommendation:
     - "3 of your upcoming commitments have no partner finalized, risking potential delays."

### 7. **Visual/Metaphorical Cues**
   - Combine short textual synthesis with simple visual metaphors or traffic-light indicators, succinctly communicating urgency without excessive explanation:
     - "Your renewals pipeline is mostly green (healthy), but 2 large deals are flashing red for missing budget conversations."

### 8. **Trend-Based Insights**
   - Quickly surface shifts or trends without detail overload:
     - "Compared to last month, risk factors increased by 25% in renewal opportunities due to partner selection delays."

### 9. **Critical Path Highlight**
   - Identify the "most impactful" or "critical path" issue that executives should prioritize without explicitly instructing action:
     - "Mandatory professional services removal is affecting 3 imminent commitments."

### 10. **Interactive Drill-down Statements**
   - Use synthesis as entry-points rather than summaries, encouraging deeper exploration:
     - "Renewal opportunities over $1M show notable inactivity—review Capstone and Newage for critical next steps."

### Example synthesis (implementing these ideas):
- **Filtered by Renewal + Critical risk**:
  > "Your renewals have 3 critical risks. Largest concern: Capstone Logistics ($2.4M) lacks budget clarity with closure in 38 days."

- **Filtered by Deal Size > $1M + At-Risk**:
  > "SprintRay ($1.1M, Upsell) is uniquely at-risk—technical POV unresolved."

- **Filtered by Inactivity**:
  > "Two commitments (Dade Paper, Capstone) flagged for inactivity over 30 days. Urgent review recommended."

---

These minimalist yet targeted synthesis approaches empower users by surfacing critical signals clearly and succinctly, inviting informed exploration rather than overwhelming them with information.

