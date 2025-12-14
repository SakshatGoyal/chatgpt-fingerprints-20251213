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
