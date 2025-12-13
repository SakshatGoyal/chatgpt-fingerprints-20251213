# AI Synthesis for Sales AEs

## You (2025-07-17T17:15:24.539000+00:00)

{'content_type': 'image_asset_pointer', 'asset_pointer': 'file-service://file-MfXrF9dnN6xEGEHs4NZt5i', 'size_bytes': 533761, 'width': 2048, 'height': 1908, 'fovea': None, 'metadata': {'dalle': None, 'gizmo': None, 'generation': None, 'container_pixel_height': None, 'container_pixel_width': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'lpe_keep_patch_ijhw': None, 'lpe_delta_encoding_channel': None, 'sanitized': True, 'asset_pointer_link': None, 'watermarked_asset_pointer': None, 'is_no_auth_placeholder': None}}
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

## ChatGPT (2025-07-17T17:15:26.882225+00:00)

Fantastic prompt—thank you for the depth. Let’s ideate from a *human-centered design* perspective, with respect for the cognitive load, autonomy, and expertise of sales executives. Here’s a structured approach to synthesize information **without overstepping into recommendations**, while still being surgically useful and highly contextual.

---

### 🧠 FRAME: What kind of AI synthesis is actually useful here?

Think of synthesis not as summarization, but as **“signal surfacing”**. The AI’s role isn’t to tell the AE what to do—it’s to **help them notice what they might otherwise miss**. Imagine it like a radar ping—not a script.

So the synthesis should feel more like:
> “Across your Q3 renewals, 40% of deals over $1M have risk factors involving no partner selected or low deployment. These represent $6.4M in pipeline and are concentrated in Cortex.”

Rather than:
> “You should engage these customers or escalate to SE leadership.”

---

### 🔁 MODULAR SYNTHESIS FRAMES
Here are **five synthesis “lenses”** that could each be auto-triggered by a user applying filters. Think of them as **synthesis templates**, optimized for brevity and usefulness.

---

#### 1. **Risk Density Mapping**
> **What’s hot and at risk?**
```text
Within [filtered view], [$X] in pipeline is tied to accounts flagged “Critical,” representing [Y]% of deal volume. 
Common risk signals: [Top 2 risk types], concentrated in [Product/Stage].
```

*Purpose:* Surfaces where revenue is at high risk. The AE decides how to act.

---

#### 2. **Momentum Bottlenecks**
> **Where is velocity stalled or unexpected?**
```text
[$X] in [opportunity type] deals have remained in [same sales stage] for over 30 days, despite expected close within [N] days. 
Most are tied to [Product] with [shared risk signals].
```

*Purpose:* Flags deals “frozen in time,” helping AEs prioritize velocity recoveries.

---

#### 3. **Outlier Signals**
> **What doesn’t fit the pattern?**
```text
1 of your top 5 deals has 3+ risk factors despite a “Commit” forecast. 
This deal is in [account name], with [account health status] and includes [Product].
```

*Purpose:* Nudges attention to misaligned or contradictory signals—forecast optimism vs underlying red flags.

---

#### 4. **Upside Anomalies**
> **Where is unexpected opportunity?**
```text
[$X] in [“Best Case” or “Pipeline”] deals show “Healthy” account status with zero flagged risk factors. 
These are all in [Product] and may be candidates for reforecasting.
```

*Purpose:* Not prescriptive, but suggests “quiet strong” deals that may be under-forecasted.

---

#### 5. **Silent Zones**
> **Where’s the ghost town?**
```text
[Z]% of your [opportunity type] deals over [$X] show no activity in the last 30 days. 
Many are flagged with [“No EBCs” or “No Partner Selected”], most commonly in [Product].
```

*Purpose:* Helps catch neglected or passive deals that might otherwise fall off the radar.

---

### 🎛️ USER-TRIGGERED MICRO-SYNTHESIS
Rather than dumping a synthesis when a user hits the page, **make synthesis conditional on filters**. For example:

- On filter change (e.g., selecting "Renewals > $1M"), show a small module:  
  > “AI Synthesis Available for These Filters → View Summary”  
- On click, reveal a **single sentence + expand option.**
  
This lets the AE opt-in, protecting autonomy.

---

### 🔭 FUTURE VISION: Interactive Trendlines
Over time, let the system learn user behavior: e.g., which deals they engage with after a synthesis, and dynamically adjust the lens surfaced next. You’re not prescribing—you're curating awareness.

---

Would you like me to prototype a few of these summaries using the actual data in the image you shared? I can map a couple of them to give you a feel.

## You (2025-07-17T17:19:56.312000+00:00)

ok, this is a good start. I'd like you to translate these suggestions into a series of guidelines for a product designer defining AI usecases and interactions. Eventually they would use these guidelines to build system prompt, but for now, design centrc guidelines are good enough. 

You can think of these guidelines also as use-cases. (which is similar to the way you've laid out your ideas). Make sure to include atleast 3 examples for each guideline or scenario.

