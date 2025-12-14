# User frustration with partial AI

## You (2025-10-02T18:26:49.593000+00:00)

Let's say I'm designing an AI system that mostly learns from a company's internal data. I have deployed this AI system to potential users. The challenge now is that the AI is not yet fully developed, and therefore, the AI system can only access parts of the data that the company needs to make sense of it. I want you to think from the standpoint of a human user. How would people feel when a system is unable to access all the data, or more specifically, is only able to answer some of their simple, and perhaps deep, questions?

## ChatGPT (2025-10-02T18:27:06.233099+00:00)

From the standpoint of a human user—especially one inside a company expecting an AI system to be helpful—partial comprehension feels like a betrayal of promise.

At first, people might be intrigued or even excited. You’ve unveiled something that hints at capability, that gestures toward intelligence. But that early curiosity very quickly collides with **expectation mismatches**. When users realize the system can only *sometimes* answer simple questions—and is blind to other critical, obvious context—they experience a blend of emotions:

---

### 1. **Frustration (It’s not doing what I need)**
> *“Why can’t it find this file? It’s on SharePoint.”*
> *“It gave me the org chart but can’t tell me who owns this project?”*

Users often assume that because a system can *understand language*, it must also *understand their world*. When it fails on basic questions (especially those that feel obvious), it feels less like an early beta and more like incompetence. The human brain is unforgiving about inconsistencies in perceived intelligence.

---

### 2. **Distrust (How can I rely on this?)**
Partial knowledge is dangerous. If the AI *sometimes* knows the answer and *sometimes* doesn’t, users begin to doubt when they can trust it. Worse, if it confidently *hallucinates* in the absence of data, it crosses a red line: it becomes untrustworthy.

People don’t want a *sometimes useful oracle*. They want either:
- A **clearly limited tool** they can control.
- Or a **competent assistant** they can rely on.

Waffling in between is the worst of both worlds.

---

### 3. **Confusion (Where’s the line?)**
> *“Wait—can it access Confluence or not?”*
> *“I thought it had access to Jira tickets?”*

If the system doesn’t transparently communicate **what it knows** and **what it doesn’t**, users struggle to form a working model of it. They ask the wrong things, get bad results, and blame the system.

This is especially pronounced when the system uses natural language—it *sounds* like it should know more than it does.

---

### 4. **Decreased Use (Quiet Abandonment)**
The most dangerous outcome is silence. People stop using it. Not out of protest—but because it quietly slips below the usefulness threshold. The internal momentum dies. Now the AI becomes just another tool nobody opens. It wasn’t *bad*, it just wasn’t *worth integrating* into daily behavior.

---

### So what to do?

To rebuild trust and improve usability in this in-between phase, you need to:
- **Expose the map**: Let users *see what data the AI has access to* and *what it doesn’t*. Make that boundary explicit.
- **Signal growth**: Use metaphors like “we’re building its knowledge muscle” or “you’re seeing the AI grow in real time.” Invite users to *train* or *contribute*. This creates emotional investment.
- **Handle “unknowns” gracefully**: When the AI can’t answer, it should say *why*—and ideally, *what would unlock the answer*. ("I don’t yet have access to the finance team’s Notion workspace. Request access?")
- **Design for feedback loops**: Every failure is an opportunity. Let users flag “I expected this to work”—that becomes training data for prioritizing data integrations.

---

### Visionary Framing (Paul's Perspective)

In the grand arc of AI system evolution, this phase you’re in—the *cognitive scaffolding* stage—is the equivalent of building a telescope and only having part of the lens. People look through it, see blurry fragments of the cosmos, and wonder if it’s broken. But what they don’t yet see is that you’re calibrating the instrument that will one day let them navigate the stars of their organization with precision.

So you have two jobs:
1. **Engineer visibility into the system’s current limits.**
2. **Tell the story of the system’s trajectory, not just its current state.**

That’s how you turn users from passive skeptics into active co-pilots.

---

Would you like help framing this system's messaging or scaffolding the user onboarding experience to align with this narrative?

## You (2025-10-02T18:50:58.355000+00:00)

Yes, show me these two jobs, engineering visibility into the system's current limit and tell the story of the system's trajectory. Show me these two jobs through specific scenarios and examples.

## ChatGPT (2025-10-02T18:51:00.625566+00:00)

Excellent. These two jobs—**engineering visibility into the system’s current limits** and **telling the story of the system’s trajectory**—aren’t just about UX or product framing. They are *psychological contracts* you’re forming with your users. The clearer and more emotionally resonant they are, the more resilient your system becomes during its early imperfections.

Let’s break each one down with **concrete scenarios**, examples, and design patterns.

---

## ⚙️ **Job 1: Engineer Visibility Into the System’s Current Limits**

**Goal:** Help users *predict* what the AI can and cannot do, *before* they’re disappointed. This creates *trust* and *predictability*, which are more valuable in the early phase than flashy capabilities.

### **Scenario A: AI Assistant in a Knowledge-Rich Enterprise (e.g., Consulting Firm)**

**User Question:** “Who owns the XYZ client relationship?”

**Current Reality:** The AI has access to Salesforce data but not internal Slack or client team docs.

### 🧠 How to Engineer Visibility:

#### 1. **Proactive Boundary Acknowledgement (Inline UI Clarity)**
> _"Right now, I can search Salesforce contacts and recent client meetings, but I don’t yet have access to Slack or your team’s Confluence notes. Would you like to request that integration?"_

✅ This:
- Acknowledges what’s possible
- Explains the limitation
- Offers agency to the user

#### 2. **Knowledge Coverage Map (Dashboards / Status Panel)**
Provide a “Data Access” map inside the UI:
- ✅ Salesforce: Connected
- ❌ Slack: Not Connected
- ❌ Shared Drives: Partial Access
- ✅ HRIS: Connected

🔍 Let users explore the map or even type: “What do you know about XYZ project?” → and the system answers from sources *it can access*, while tagging the source.

---

### **Scenario B: AI System for Finance Operations (e.g., Procurement Automation)**

**User Input:** “What’s our total spend with Vendor A last year?”

**Problem:** The AI has some invoice data from SAP, but nothing from expense reports in Workday.

### 🧠 Design Pattern:

#### 3. **Explain Missing Context in the Response**
> _“I found $245,000 in spend via SAP invoices. To get a complete picture, I need access to Workday expense reports. You can enable that here.”_

### Bonus: **‘Unknowns Summary’ Feature**
At the end of each interaction:
> _“I answered this using 2 of 4 relevant systems. Want to improve this answer?”_

---

## 🚀 **Job 2: Tell the Story of the System’s Trajectory**

**Goal:** Position the AI system not as a static product but as a *living, learning organism*—one that *grows with the company*. This transforms users into **stakeholders in the AI’s evolution**, not just consumers of it.

### **Scenario A: AI Rolled Out to 100 Early Employees**

You’re in week 3 of deployment. People are asking basic things. The AI sometimes gives good answers, other times misses entirely.

### 🧠 How to Tell the Story:

#### 1. **The Growth Metaphor**
Use storytelling in the onboarding UI:
> _“You’re one of the first 100 people helping this AI learn your company’s brain. Right now, it’s like a smart intern—eager, learning fast, but still missing pieces. Every question you ask helps it grow stronger.”_

This frames imperfection as progress.

---

#### 2. **Roadmap as Narrative, Not Feature List**
Don’t just say “We’ll add Slack and Notion access in Q4.”

Instead:
> _“This month, we’re teaching the AI to listen to internal Slack conversations. Next month, it will learn to reason over project timelines. Eventually, it will be able to spot duplicate work across departments before you even ask.”_

You’re inviting users to believe in a *trajectory*.

---

#### 3. **Use a ‘Learning Log’ or Changelog with Emotion**
Imagine a weekly update:
> _“This week your AI learned 15 new concepts from Confluence and added 3,000 structured documents to its index. It's now 27% better at answering product lifecycle questions.”_

Give it *metrics*, but also *character*. People like watching growth.

---

### **Scenario B: Executives Ask “Why Can’t It Just Answer Everything Yet?”**

Rather than apologizing or over-promising, give them a frame:

> _“We’re modeling this AI like a company-wide neural network. Right now, it sees isolated neurons—Salesforce, Confluence, SAP. The breakthrough happens when we light up the connections between them. We're not building a dashboard. We’re building organizational cognition.”_

Tell the story of the *second brain* you’re building—one node at a time.

---

## 🧬 A Closing Metaphor: **You’re Building the Mind of the Company**

If the company is a body, its data systems are its organs. Your AI is learning to become its **central nervous system**.

But just like a child learning language, comprehension comes in stages:
1. **Listening** (connecting data)
2. **Speaking** (responding)
3. **Understanding nuance** (reasoning)
4. **Anticipating needs** (proactive)

Every user interaction is part of this developmental process. When they see the AI not just as a tool, but as a *growing intelligence* they’re helping shape, their tolerance increases, and their participation deepens.

---

Would you like to workshop a sample onboarding flow or narrative copy for a launch email? Or even a live "learning log" concept?

## You (2025-10-02T18:56:40.422000+00:00)

Could you provide some constructive criticism on the above responses from our AI system? Remember, our goal is two fold:

1. Maintain credibility.
We know a system may not have all the answers. And the users will know soon. How do we maintain our messaging through these limitations without making our users feel we can't deliver. Paul suggested a few things which i find promising:
--Engineer visibility into the system’s current limits.
--Tell the story of the system’s trajectory, not just its current state.


2. Not bore our users.
While the two sub-principles are critical, and may help; we also don't want to create a situation of overexplaining. We want some way to allow users to continue their conversation with us. So we need to continue providing value. All this needs to be done while maintaining credibility.

## ChatGPT (2025-10-02T18:56:44.122903+00:00)

Your goals are astutely defined: **credibility** and **continued engagement**. But the difficulty lies in balancing the **humility required to acknowledge current limitations** with the **confidence necessary to retain user faith**, *without falling into pedantic or defensive tones*.

Below, I’ll critique the previous AI responses with those twin aims in mind, highlighting where they succeed, where they threaten to undercut credibility or bore the user, and how they can be sharpened.

---

## 🔍 **Constructive Criticism of Previous Responses**

---

### ⚠️ **1. Risk of *Overqualifying* and *Apologizing for the Limitations***

**Issue:**
Phrases like:
- “Right now, I can search Salesforce contacts and recent meetings, but I don’t yet have access to Slack or your team’s Confluence notes…”
- “I only found X; I’d need Y to be more accurate…”

These signal conscientiousness, but if repeated too often, they begin to sound like **disclaimers**, not *capabilities*. It risks creating an impression that the system is always *on the verge* of being useful—like an assistant who's perpetually “in training.”

> ⚔️ *Machiavellian Principle:* When your weakness is visible, do not dwell on it. Shift the user’s attention to what **you can control**, and always leave them with something **useful**.

**Fix:**
Replace apologetic transparency with **strategic redirection**:
> _“I’ve pulled everything I found in Salesforce—no signal yet from Slack. Want me to flag this topic for deeper coverage when more data is unlocked?”_

This does *three things*:
- Shows activity, not deficiency.
- Projects progress (“when more data is unlocked”).
- Offers the user a role (“want me to flag this?”) → *turns a lack into a micro-engagement*.

---

### ⚠️ **2. Messaging That Puts the Burden on the User**

Some lines ask:
> “Would you like to request that integration?”
> “You can enable that here.”

**Problem:**
These requests shift the responsibility back to the user **too early**, before trust or excitement is established. Early adopters will tolerate friction if they feel *momentum*, but not if they feel they're being asked to do the work of the system.

**Fix:**
Offer *assistance*, not options:
> _“I’ll mark that integration as high-priority and notify your admin—unless you'd prefer I don’t.”_

That flips the psychology: the AI is *moving things forward* unless stopped. It sounds competent, not hesitant. It still informs, but subtly reinforces its own autonomy.

---

### ⚠️ **3. Over-Explaining the Trajectory**

**Example:**
> “This month, we’re teaching the AI to listen to Slack. Next month, it will learn to reason over project timelines…”

**Issue:**
While informative, this is dangerously close to “product roadmap theater.” It sounds like an internal update, not something a user **wants** to read mid-conversation. You risk boring the user and breaking flow.

**Fix:**
Compress narrative into punchy, confidence-laden statements:
> _“Right now I’m learning Slack; next time you ask, you’ll likely get a richer answer.”_
Or even:
> _“Slack’s on my radar. Give me a few weeks.”_

Keep the trajectory **implied**, not **documented**. You’re seducing the user with signs of growth—not burdening them with status reports.

---

## ✅ **What Worked Well and Should Be Retained**

### ✅ Framing the AI as a "Growing Organism"
This metaphor—"smart intern," “second brain,” “neural network”—is *powerful*. It buys goodwill. It gives users a stake in the system’s maturation. *But don’t overuse it.* It should surface in **onboarding**, **milestone notifications**, and **periodic summaries**, *not in routine conversation*.

### ✅ Giving Partial Answers with Confidence
The phrasing:
> _“I found $245,000 via SAP invoices…”_

This is good. It avoids the sin of silence. Always **give what you can**. People prefer **partial insight** to **a blank stare**—provided it’s framed confidently.

---

## 🧠 Strategic Suggestions Going Forward

---

### 🎯 **Guiding Principle #1: Limitations Must Never Be the Last Word**

Every message—especially one involving a limitation—must end with **a pivot**:

| If AI can’t answer | Don’t just say… | Say this instead |
|--------------------|----------------|------------------|
| “I don’t know.” | “I don’t have access.” | “I’ll mark this as a blind spot—expect sharper answers soon.” |
| “That data isn’t connected.” | “You can connect X here.” | “I’ll notify your admin. You’ll hear from me when it's live.” |
| “I can’t give you a full picture.” | “Here’s what I found.” | “This gives you 80% of the story. I’ll fill in the rest once Workday is live.” |

---

### 🧲 **Guiding Principle #2: Create Micro-Engagement Loops**

Boredom arises from *passivity*. Give users small, satisfying levers to pull.

- After a failed query:
  > “Want me to watch for updates on this?”
- After a partial answer:
  > “Should I alert you when I learn more?”
- After an insight:
  > “Want to dive deeper?”

These are not just UX features. They’re **psychological tethers**, keeping the user in *conversation*, not judgment.

---

### 📈 **Guiding Principle #3: Make Progress Tangible**

Don’t tell users the system is growing. **Show** it.

- “Last week I learned 5,200 new contracts.”
- “I’m now 35% better at answering budget questions.”
- “I used to answer this in 3.2s—now it's 1.1s.”

Make growth **numerical**, **visible**, and **linked to their actions** (e.g., “Thanks to your questions, I learned X.”)

---

## 🧩 Summary: How to Thread the Needle

| Objective | Bad Pattern | Good Pattern |
|----------|-------------|--------------|
| Maintain credibility | Over-apologizing for gaps | Acknowledge + redirect with agency |
| Avoid boredom | Long-winded roadmaps | Short, sharp growth metaphors |
| Keep conversation alive | Dead-end messages | Micro-engagement hooks |
| Project intelligence | Passive status | Autonomy and initiative |
| Inspire belief | Defend today’s limits | Seduce with tomorrow’s power |

---

Would you like help rewriting a few real examples from your system with these principles in mind? Or do you want a tone/style guide you can hand off to your AI team's writers?

## You (2025-10-02T19:18:25.887000+00:00)

These principles are promising. Now I want you to do two things:

1. Create a universal set of principles that integrates your principles with the ones that Paul shared earlier, and with the ones that you have shared based on the concerns I've had. Remember that you are not simply adding on 2+3; you are creating a set of universal principles that integrate the two essential mindsets. Ensure that you consider edge cases when creating these principles.

2. Elaborate and articulate in detail what you want a person to interpret and act on the principles derived. The principles, while solid, lack a certain versatility in their interpretation. Once you have clearly articulated these principles, a team will be able to apply them to broader conversations and use cases.

## ChatGPT (2025-10-02T19:18:27.764882+00:00)

Excellent. You're asking for **a unified doctrine**—a flexible yet rigorous framework that merges *Paul’s strategic mindsets* (engineering visibility + telling the system’s story) with your concern for *user trust, narrative restraint, and ongoing utility*. This requires not just aggregation, but **synthesis**: something smaller than a manifesto, larger than a checklist. It must serve as both compass and scalpel—guiding high-level thinking while informing on-the-ground product choices.

Let us begin.

---

# 🔷 Part 1: The Unified Principles – *The Credibility Loop*

## ✦ **The Credibility Loop**:
A **strategic design framework** for AI systems learning from partial data, aimed at sustaining user trust and driving engagement—even when the system is incomplete.

The loop consists of **5 interconnected principles**, unified by a single core aim:

> To **maintain belief in the system’s value** even when it cannot yet fulfill the user's needs—and to **convert limitations into invitations** for deeper interaction.

---

## 🜂 1. **Show the Edges of Knowledge**
> *“An intelligence that hides its blindness invites disbelief.”*

**Design your system to reveal what it knows, what it doesn’t, and what it’s learning next.** Users don’t need perfection, but they need **transparency**. Knowing the edges of capability helps them **model the system in their mind**—which is essential for long-term use.

### Implementation Guidelines:
- Always *disclose the scope* of data being searched.
- Provide **confidence bands** or **knowledge coverage maps** when possible.
- Embed “What I know about this topic” summaries.
- Default to showing sources—even for partial answers.

**Edge Case:**
Avoid drowning users in technical limits. Never offer a list of missing APIs unless the user asks for it. The point is to map the *function*, not the *plumbing*.

---

## 🜁 2. **Always Leave With Value**
> *“A half-truth is forgivable. A dead-end is fatal.”*

Even when the system lacks full information, **never return empty-handed**. Users forgive imperfection, not uselessness. Give a partial answer, a directional insight, or a plan of action. What matters is momentum.

### Implementation Guidelines:
- Return partial answers with clear framing.
- Offer fallback content (“related knowledge,” “common workflows,” “linked experts”).
- If blocked, suggest the next best thing (“I can’t get you that—but here’s what I do know”).

**Edge Case:**
Avoid speculative or hallucinated answers masked as “value.” Don’t guess if you can’t frame the answer clearly as a **partial**, not a **whole**.

---

## 🜃 3. **Narrate the Arc, Not the Apology**
> *“Speak not of what you lack. Speak of what you are becoming.”*

Users are investing not just in a tool, but in a **trajectory**. Frame limitations not as *shortfalls*, but as *milestones on the system’s evolution*. This sustains belief and builds emotional equity.

### Implementation Guidelines:
- Use metaphors: “apprentice,” “growing brain,” “second nervous system.”
- Surface clear, *succinct* growth updates ("Last week I learned X").
- Bake trajectory into UI moments: onboarding, milestone triggers, periodic summaries.
- When relevant, show what the AI *will* be able to do soon—but only sparingly.

**Edge Case:**
Do not dump roadmaps on users mid-task. Reserve aspirational messaging for *moments of opt-in attention*, not operational flow.

---

## 🜄 4. **Pull the User Into the Loop**
> *“Invite participation. Seduce contribution. Make growth a shared victory.”*

Let users feel that their input **trains, shapes, or expands** the system. This transforms them from consumers into *co-creators* of the intelligence. Emotional ownership increases tolerance and engagement.

### Implementation Guidelines:
- Ask users to flag “blind spots” or suggest integrations.
- Let them “subscribe” to improvements on topics they care about.
- Acknowledge their contribution: “Thanks to your query, I’ve added new context.”

**Edge Case:**
Avoid making the user your mechanical Turk. Don’t offload friction or hide under “training” excuses. Contribution must feel like **collaboration**, not **compensation for system failure**.

---

## 🜛 5. **Sustain Flow, Not Just Trust**
> *“Trust sustains belief. Flow sustains attention.”*

Explanations must never clog the conversation. Ensure the system **keeps the user in motion**, whether by returning information, prompting next steps, or subtly framing follow-ups. Brevity is not just elegance—it’s survival.

### Implementation Guidelines:
- Default to action over explanation.
- End every reply with a “hook”:
   - “Want to dig deeper?”
   - “Should I flag this for follow-up?”
   - “Would you like me to track this area?”

**Edge Case:**
When dealing with high-stakes topics (e.g. finance, legal, exec queries), clarity trumps flow. Pause the narrative if the user’s trust is on the line—but return to motion *immediately after*.

---

# 🔷 Part 2: Applying the Principles – Interpretive Guide for Teams

Now that we have our five principles, the question becomes: **how should a product, design, or conversational UX team *use* them?**

The key is to treat them not as rigid rules, but as **navigational instruments**. They tell you **where to move** when facing product ambiguity, user frustration, or narrative fatigue.

Here’s how to interpret and apply each principle:

---

## 🜂 1. **Show the Edges of Knowledge** → *Design for Predictability, Not Perfection*

### What this means for you:
- Let the user form a mental model of what the system *knows today*.
- Use UI affordances (maps, source tags, filters) to make scope *visible*.
- Don’t oversell—frame each answer as rooted in its *knowledge perimeter*.

### Example Application:
> A user asks: “How are Q2 budgets looking for Team B?”
> Your system replies:
> _“I have visibility into finalized budgets in Workday, but not into real-time expense reports. Based on what I see, Team B is at 72% utilization. Want me to flag this when the rest comes in?”_

---

## 🜁 2. **Always Leave With Value** → *Never Abandon the User Empty-Handed*

### What this means for you:
- Don’t say “I don’t know.” Say, “Here’s what I *do* know.”
- Relevance > completeness. Give a foothold into the topic.
- Suggest adjacent queries or related actions.

### Example Application:
> A user asks: “What’s the outcome of the last vendor negotiation?”
> Your system replies:
> _“I don’t have the meeting transcript, but I found the updated contract and timeline. Would you like a summary of the key terms that changed?”_

---

## 🜃 3. **Narrate the Arc, Not the Apology** → *Make Incompleteness a Chapter, Not a Crisis*

### What this means for you:
- Avoid defensive language. Show growth.
- Use narrative voice where appropriate—this humanizes limits.
- Keep forward-looking language **brief**, **confident**, and **intentional**.

### Example Application:
> “Slack conversations aren’t included yet, but that’s one of the next data sources I’m learning. For now, here’s what I can infer from Jira + Salesforce.”

---

## 🜄 4. **Pull the User Into the Loop** → *Invite Collaboration, Not Just Consumption*

### What this means for you:
- Let users shape the system’s evolution without burdening them.
- Give them visible credit (“Thanks to your input…”).
- Make feedback loops part of the **core UX**, not just forms at the bottom.

### Example Application:
> After a failed question:
> _“I couldn’t answer this today. Want me to prioritize learning this area? I’ll notify you when I can.”_

---

## 🜛 5. **Sustain Flow, Not Just Trust** → *Keep the Conversation in Motion*

### What this means for you:
- Minimize exposition unless requested.
- Add "soft next steps" to every output.
- Avoid heavy transitions. Keep users talking to the system.

### Example Application:
> _“Here’s the project timeline based on current data. Want to see dependencies next?”_

---

# 🧭 Final Thought: Strategy Over Sympathy

The trap many AI teams fall into is **empathy without assertiveness**: they apologize, explain, and soften until their system sounds like an underconfident intern.

But credibility is not built on apologies—it’s built on **predictability**, **narrative coherence**, and **useful motion**.

This framework—**The Credibility Loop**—lets you do both:
- **Show humility without losing power**,
- **Show incompleteness without losing trust**,
- **Show forward motion without boring detours.**

Would you like me to translate these principles into UX copy guidelines, design prompts, or product review checklists next?
