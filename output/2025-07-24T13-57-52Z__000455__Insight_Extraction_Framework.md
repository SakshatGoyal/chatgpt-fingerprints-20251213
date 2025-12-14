# Insight Extraction Framework

## You (2025-07-24T13:57:52.896000+00:00)

Help me create a prompt with the following intent.

I'm attaching two sets of principles here. One of them is the core foundational set of principles, and the other is more of an ancillary set of insights and information. Now, both of them are critical, but the first one deals with exactly how insights should be looked for in the sense that how an AI system or a person should extract insights from a large dataset. And the second one is more about how they should be phrased, but it has some elements of how the insights should also be looked for. It's going to be tricky, and we want to find the right balance. We don't want to omit anything necessarily, but we want some way to basically integrate both into one system for extracting insights. And for this prompt, I'm going to need the skill set of someone who knows how to conduct design research, knows how to define design principles, ideally someone from IDO or frog design, someone who has a lot of experience leading not just design teams, but product teams, so that's engineering, design, everything, but still has a strong research foundation, so they know how to exactly communicate the process of writing insights.

I'm attaching the two sets below for your context. But don't include too many specifics or the principles themselves in the prompt.

---
AI SYNTHESIS GUIDELINES


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

| Name | **Risk Densities** | **Momentum Bottlenecks** | **Contradiction Detection** | **Silent Zones** |
| --- | --- | --- | --- | --- |
| Description | Clusters of risk factors among certain deal types, products, or health statuses. | Deals approaching close that show no recent activity or stage progression. | Mismatches between forecast confidence and underlying deal health. | High-value or critical opportunities that have gone quiet for long periods. |
| Example of Insight 1 | 61 out of 101 deals (≈ $79.7M) carry the risk 🏅 No Secured technical win—making it the most common single-point risk across the pipeline. | Of the 37 deals with ≤45 days to close, 14 have had no logged activity in 30+ days—a clear momentum stall at a critical point in time. | 17 deals are labeled Best Case, yet 12 of them have ≥3 active risk factors.– Notably, 5 Best Case deals lack secured tech wins and show no partner activity.– 3 are in Critical health despite optimistic forecast tags. | 19 deals (≈ $28.4M) have logged no activity in the last 30 days;– 11 of them must close in the next 60 days– 7 are currently tagged Best Case or Commit |
| Example of Insight 2 | Among Firewall – PA Series deals, 42% (11 of 26) have both 🧑‍💻 Mandatory PS removed and 🛑 Low adoption, especially among Renewals and Upsells, suggesting systemic post-sale execution friction. | Within the Solution stage (Stage 3), 17 of 31 deals (≈ $26.8M) have either ⌛ pending quotes or 🧑‍💻 removed PS, slowing mid-funnel movement. | The largest Commit deal, $7.1M, involves no secured win, pending quote, and no budget conversation—indicating a fragile top-of-forecast commitment. | Within Renewals, 6 of 22 deals show inactivity for >30 days, and 5 of those also carry quote or partner risks—pointing to potential revenue churn risk. |
| Example of Insight 3 | Across all Cortex & Cloud opportunities (24 total), 75% carry ≥2 risk factors, most commonly 🏛️ No EBCs in last year and 💤 No activity for last 30 days—indicating low engagement in technically complex deals. | 11 Upsell deals (≈ $22.7M) sit in Stage 2 Discovery—with an average close horizon of only 52 days, indicating pre-engagement drag in existing accounts. | Across Renewals > $1M, 8 of 13 are flagged as At-risk or Critical, yet 6 remain tagged as Pipeline or Best Case—a misalignment between deal health and sales confidence. | Prisma Access opportunities (SASE) have the highest share of silent deals, with 7 of 14 inactive for ≥30 days and 5 of those flagged as At-Risk in account health. |
| Example of Insight 4 | Deals over $5M (13 in total, ≈ $86.1M) disproportionately carry budgeting and approval risks:– 8 flag ⌛ Quotes pending approval– 7 lack finalized budget conversations (💲)– 6 miss a partner engagement (🤝) | Net New deals in Cortex XSIAM and XSOAR tend to bottleneck in Discovery:– 7 of 10 are in early stages– 5 carry ≥3 risks– 4 show no activity in past 30 days | One Firewall – VM Series deal in Purchase stage still lacks an approved quote and has logged no activity in 41 days—a red flag given its supposed sales readiness. | High-value Cortex Cloud deals (>$1M) are largely dormant:– 5 of 7 have had no recent engagement– 4 are in early Discovery despite near-term close targets– 3 show missing EBCs and partner finalization gaps |

---

### Deal Insights Writing Guide ( *Opportunities* )

| Section | Guidance | Rationale |
| --- | --- | --- |
| **Language & Tone** | Use **plain, quantitative statements** → “*30 of 61 deals also lack exec engagement*”. Avoid jargon like “flagging lacking”.
Make the insight actionable without necessarily writing opinions or next steps.  | Clear counts are easier to scan and discuss in forecast calls |
| **Audience Split** | *Sellers* → highlight **forgotten updates / overdue tasks**. | Each role needs different granularity; managers care about scale, reps care about next action |
| **Insight Anatomy** | 1. **Count + Stage** (Pipeline / Commit / Best Case).

2. **Risk type**.

3. **Dollar impact (optional)**. | Keeps copy concise while guiding immediate remediation |

---

## ChatGPT (2025-07-24T13:57:53.613735+00:00)

This is a great foundation. Let's dive into **discovery mode** first so I can construct a truly effective prompt that meets the nuance of your intent. You're clearly balancing **two systems of logic**: one about *how to find insights*, the other about *how to express them*, with some overlap. So let’s explore a few critical dimensions before I start constructing the prompt:

---

### 🔍 1. Clarifying the Intent
You mentioned wanting a **unified system** that synthesizes both sets of principles. Could you clarify the **final output or system behavior** you're hoping the prompt will create?
Examples:
- A model that **generates insights** from structured data using these combined principles?
- A framework or function that **evaluates whether a given insight follows** both sets of principles?
- Or a **meta-level generator** that outputs insight templates for future use?

---

### 🧠 2. Scope of Data & Context
To generate the insights effectively:
- Is the input assumed to be structured tabular data (like CRM/sales pipelines)?
- Will the AI have access to full records (e.g., deal metadata, activity logs, account health, etc.)?

Also, how **broadly applicable** do you want the logic to be—specific to the examples given, or more abstract so it can work across different verticals?

---

### 🛠️ 3. Constraints & Integration Balance
You mentioned not wanting to *omit anything* but still finding the *right balance*. Let’s explore:
- Would you prefer the **core AI synthesis guidelines** to take precedence, with the **writing guide** acting as a filter/lens?
- Or should it be a **merge**, where each principle from either set gets a functional role (e.g., some for detection, others for phrasing)?

Also: Should the prompt **prioritize clarity or exhaustiveness** when insights appear ambiguous?

---

### 🗣️ 4. Execution Persona and Tone
You’ve nailed the desired expertise—someone with a blend of:
- **Design research sensibility** (as seen in IDO/Frog),
- **Insight synthesis discipline**,
- **Cross-functional leadership mindset** (product, design, engineering).

Just to confirm:
- Would you like the model to **emulate that persona** in tone and reasoning while synthesizing insights?
- Or should the model just follow their approach but output insights in a neutral voice (like for internal use in a product)?

---

### 🧾 5. Format of Output
Should the insights:
- Always follow the `Insight Anatomy` structure (e.g., Count + Stage → Risk → Optional Dollar impact)?
- Be generated in bulk (e.g., top 5 insights for a filter set)?
- Or be single-shot, per user filter or query?

Would you want a **consistent format/template** (Markdown? JSON?) for downstream use?

---

### ⚠️ 6. Edge Cases
Some edge cases I’m already anticipating:
- Overlapping signals (e.g., a deal qualifies for both “momentum stall” and “silent zone”).
- Missing or noisy data—should the AI flag that or stay silent?
- Conflicts between a risk and the forecast—how strongly should those be emphasized?

---

Once you respond to these questions (even partially), I’ll be ready to **begin building the prompt**. You’re close—we just want to lock in the exact expectations.

## You (2025-07-24T13:59:44.690000+00:00)

I'm hoping the prompt doesn't create insights but rather creates a set of guiding principles that can be strictly followed repetitively. It's very important for these principles to be crisp, precise, leaves little room for ambiguity, but at the same time I want to make sure that we're not being too prescriptive so as to inhibit anyone following those principles to draw insights that would otherwise be valuable.

---

I think this is the key difference, now ask me your questions

## ChatGPT (2025-07-24T13:59:47.742320+00:00)

Perfect—this clarification fundamentally shifts the task from **insight generation** to **principle system construction**, where the prompt will instruct GPT-4o to **synthesize a compact, operational, repeatable framework** for others (AI or human) to follow while extracting insights.

Let’s now zoom in on the **sharpest questions** that will help me construct that balanced, clear, and *non-limiting* prompt you're aiming for:

---

### 1. 🧱 **Principle Format Expectations**
How would you like the final principles to be **structured or formatted**?
- Should they be in a **bulleted list**?
- Organized by **"What to look for"** vs **"How to express it"?**
- Should we separate **mandatory rules** from **flexible heuristics**?

---

### 2. 🎯 **Clarity vs Interpretive Room**
You want to avoid both ambiguity *and* over-prescriptiveness. Here's a trade-off zone:
- Would you prefer **binary filters** (e.g., “Always use quantifiable units”) or **probabilistic heuristics** (e.g., “Prefer numeric summaries when possible”)?
- Should there be **example DOs and DON’Ts** for clarity, or is that too limiting for your audience?

---

### 3. 🧠 **Principle Audience and Use**
Who will be following these principles?
- Is it for **an AI agent** (like a retrieval-augmented generation system)?
- Or for **human analysts**?
- Or both?

This affects how strict or instructional the language needs to be.

---

### 4. ⚙️ **Integration Strategy Between the Two Sets**
You noted overlap and subtle tension between the two sets (foundational + phrasing). Given that:
- Would you like the prompt to **merge them into one unified set** of principles?
- Or produce **two clearly distinguished sections**—like “Insight Extraction” and “Insight Articulation”—but built to work as a system?

---

### 5. 🧬 **Reusability & Generalizability**
Should these principles be:
- **Strictly scoped to revenue/sales pipelines** like the examples?
- Or should the prompt build principles that are **abstracted enough** to apply to other high-dimensional business data contexts?

This will affect how domain-specific the language in the prompt should be.

---

### 6. 🚦 **Should Principles Be Ranked or Prioritized?**
Would it help the eventual users if:
- Principles are **ranked by importance**?
- Or grouped into **“must-follow” vs “nice-to-follow”** buckets?

---

Once I have your preferences for these dimensions, I’ll be ready to **begin building the prompt**—with precision and balance at the core.

## You (2025-07-24T14:04:37.165000+00:00)

1. 🧱 Principle Format Expectations:
- not bulleted, but in a way that communicates the intent clearly.
- yes
- yes

2. 🎯 Clarity vs Interpretive Room
- a blend of both
- Yes

3. 🧠 Principle Audience and Use
- yes, its for an AI agent.

4. ⚙️ Integration Strategy Between the Two Sets
produce two clearly distinguished sections—like “Insight Extraction” and “Insight Articulation”—but built to work as a system

5. 🧬 Reusability & Generalizability
abstracted enough to apply to other high-dimensional business data contexts

6. 🚦 Should Principles Be Ranked or Prioritized?
“must-follow” vs “nice-to-follow” buckets

begin building the prompt

## ChatGPT (2025-07-24T14:04:37.730491+00:00)

Here's the thoughtfully structured and concise prompt optimized for your intent:



## ChatGPT (2025-07-24T14:05:46.757156+00:00)

The prompt is structured and ready. If you have any refinements or additional requests, feel free to share!
