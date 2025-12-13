# Create prompt for cleaning service

## You (2025-09-13T22:13:18.397000+00:00)

disregard project instructions for this conversation. 


I'm reading some prompting guidelines on OpenAI's blog post. But I'm not an engineer, so I'm gonna need you to help me understand some examples and content. 

Also, I will be adding some prompts that I see on their website. But since they are for engineering activities, I want you to create a new prompt that follows the exact same content structure, details, methodology, and nuanced thought process, but does so for a different use-case, one that's not too technical. Let's give it a try, 


------
GPT-5 is, by default, thorough and comprehensive when trying to gather context in an agentic environment to ensure it will produce a correct answer. To reduce the scope of GPT-5’s agentic behavior—including limiting tangential tool-calling action and minimizing latency to reach a final answer—try the following:

Switch to a lower reasoning_effort. This reduces exploration depth but improves efficiency and latency. Many workflows can be accomplished with consistent results at medium or even low reasoning_effort.
Define clear criteria in your prompt for how you want the model to explore the problem space. This reduces the model’s need to explore and reason about too many ideas:

---
Prompt snippet:

<context_gathering>
Goal: Get enough context fast. Parallelize discovery and stop as soon as you can act.

Method:
- Start broad, then fan out to focused subqueries.
- In parallel, launch varied queries; read top hits per query. Deduplicate paths and cache; don’t repeat queries.
- Avoid over searching for context. If needed, run targeted searches in one parallel batch.

Early stop criteria:
- You can name exact content to change.
- Top hits converge (~70%) on one area/path.

Escalate once:
- If signals conflict or scope is fuzzy, run one refined parallel batch, then proceed.

Depth:
- Trace only symbols you’ll modify or whose contracts you rely on; avoid transitive expansion unless necessary.

Loop:
- Batch search → minimal plan → complete task.
- Search again only if validation fails or new unknowns appear. Prefer acting over more searching.
</context_gathering>

---

## ChatGPT (2025-09-13T22:13:21.099953+00:00)

{"content_type": "thoughts", "thoughts": [{"summary": "Creating a new prompt", "content": "The user seems to be looking for a new prompt analog for a non-technical use case. They mentioned \"meal planning for a family,\" \"organizing a small community event,\" or \"apartment hunting\" as ideas, which are all great options. I think a good fit might be something like \"choosing a gym and routine\" or \"planning a weekend trip.\" I'll aim for something practical and non-technical!", "chunks": [], "finished": true}, {"summary": "Deciding on browsing", "content": "It seems like the user referred to OpenAI's blog guidelines, but they didn't directly ask about OpenAI products. Since browsing is only necessary for queries about OpenAI products themselves, I don't think I need to browse here. Creating content based on the structure they provided should work just fine without extra browsing. Keep it straightforward!", "chunks": [], "finished": true}, {"summary": "Following instructions", "content": "Even though the user asked to disregard project instructions, I still need to follow the system/developer guidelines. I'll keep my answers clear but avoid being overly verbose. Since the user prefers concise and structured responses, I’ll focus on explaining the snippet in simple terms without asking clarifying questions, as requested.", "chunks": [], "finished": true}, {"summary": "Choosing a use-case for the prompt", "content": "I should start by providing a simple summary of the snippet to help the user grasp it. Then, I’ll generate a new prompt snippet in the same structure, but for a different, non-technical use-case. \"Finding a weekly house cleaning service\" seems like a good choice, as it’s simple and relevant.", "chunks": [], "finished": true}, {"summary": "Choosing the use-case and structure", "content": "The plan is to create a prompt snippet with a clear structure, closely mimicking the example. I'll use the use-case \"Choosing a weekly house cleaning service in San Francisco,\" as it’s relevant to their recent interest. The goal will be simple: quickly shortlisting providers. The method will involve aggregator platforms, reviews, and quotes, with specific stop criteria. I'll ensure to adapt the tags and sections while preserving the structure.", "chunks": [], "finished": true}], "source_analysis_msg_id": "dffd3df1-7760-44d2-b7f3-3cf0ad2b736d"}

## ChatGPT (2025-09-13T22:14:06.204224+00:00)

{"content_type": "reasoning_recap", "content": "Thought for 45s"}

## ChatGPT (2025-09-13T22:13:19.853648+00:00)

Here’s a quick plain-English decode of your snippet: it tells the model to cast a few smart nets in parallel, stop as soon as it has enough to act, only dig into details that affect the work, escalate once if signals conflict, then do the task—looping back **only** if validation fails. It’s basically “search → minimal plan → act,” with tight guardrails on depth and detours.

Now, the same structure for a non-technical use-case: **finding a reliable, budget-friendly weekly house cleaning service**.

---
Prompt snippet:

<context_gathering>
Goal: Get enough context fast to pick and book a weekly cleaner. Parallelize discovery and stop as soon as you can decide.

Method:
- Start broad, then fan out to focused subqueries (price, availability, insurance, supplies included).
- In parallel, scan a few sources (e.g., marketplaces, local listings, review sites); read top, recent hits per source. Deduplicate businesses; cache facts; don’t repeat queries.
- Avoid over-searching. If needed, run one targeted, neighborhood-specific batch (weekday/time window, apartment size, budget).

Early stop criteria:
- You can name 2–3 providers that meet: weekly slot on the requested day/time, within budget, proof of insurance, and strong recent reviews.
- Top sources converge (~70%) on the same short list, or one option clearly dominates on availability + price + reliability.

Escalate once:
- If reviews conflict or availability is fuzzy, run one refined parallel batch: check last-6-months reviews, verify policies (cancellations, supplies, same cleaner continuity), and send a single clarifying message per provider; then proceed.

Depth:
- Trace only decision-critical factors (rate per visit, included tasks/supplies, cancellation policy, background checks, continuity). Avoid transitive deep dives into all historical reviews.

Loop:
- Batch search → minimal plan (ranked shortlist) → confirm one detail (availability/price) → book.
- Search again only if confirmation fails or a new constraint appears. Prefer decisive booking over more browsing.
</context_gathering>
---

