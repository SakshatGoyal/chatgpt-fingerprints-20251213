# Creating writing prompts

## You (2025-09-13T22:31:53.582000+00:00)

disregard project instructions for this conversation.


I'm reading some prompting guidelines on OpenAI's blog post. But I'm not an engineer, so I'm gonna need you to help me understand some examples and content.

Also, I will be adding some prompts that I see on their website. But since they are for engineering activities, I want you to create a new prompt that follows the exact same content structure, details, methodology, and nuanced thought process, but does so for a different use case, one that's not too technical.

Remember, you do not need to rephrame the explanation; you only have to create a new prompt that follows the same structure as the example shared, but for a different, non-technical use case.

Think of yourself as a prompt teacher who's teaching how to write prompts to a group of artists and writers.

Let's give it a try,


------
Prompting for less eagerness
GPT-5 is, by default, thorough and comprehensive when trying to gather context in an agentic environment to ensure it will produce a correct answer. To reduce the scope of GPT-5’s agentic behavior—including limiting tangential tool-calling action and minimizing latency to reach a final answer—try the following:

Switch to a lower reasoning_effort. This reduces exploration depth but improves efficiency and latency. Many workflows can be accomplished with consistent results at medium or even low reasoning_effort.
Define clear criteria in your prompt for how you want the model to explore the problem space. This reduces the model’s need to explore and reason about too many ideas:

---
[prompt snippet]

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

If you’re willing to be maximally prescriptive, you can even set fixed tool call budgets, like the one below. The budget can naturally vary based on your desired search depth.

---
[prompt snippet]
<context_gathering>
- Search depth: very low
- Bias strongly towards providing a correct answer as quickly as possible, even if it might not be fully correct.
- Usually, this means an absolute maximum of 2 tool calls.
- If you think that you need more time to investigate, update the user with your latest findings and open questions. You can proceed if the user confirms.
</context_gathering>
---

When limiting core context gathering behavior, it’s helpful to explicitly provide the model with an escape hatch that makes it easier to satisfy a shorter context gathering step. Usually this comes in the form of a clause that allows the model to proceed under uncertainty, like “even if it might not be fully correct” in the above example.
---------





## ChatGPT (2025-09-13T22:31:55.295988+00:00)

---
[prompt snippet]

```xml
<context_gathering>
Goal: Capture just-enough creative context quickly for revising a 500-word artist statement; explore in parallel, then stop as soon as a clear edit path emerges.
Method:
- Start broad: skim the whole statement once to lock intent, audience, tone, and target word count; then branch into 2–3 focused questions (what to cut, what to clarify, how to energize voice).
- In parallel, draft up to 3 micro-variants (1–2 sentences each) for the same sticky passage in different tones (e.g., intimate, neutral, bold). Keep the strongest; discard near-duplicates.
- Avoid over-referencing. If needed, sample at most 2 short style exemplars in a single pass (e.g., gallery bios); no deep dives.
Early stop criteria:
- You can point to exact sentences/paragraphs to change.
- Candidate directions converge (~70%) on one tonal/structural choice.
Escalate once:
- If goals conflict (e.g., “moody” vs “uplifting”) or scope is fuzzy, run one refined micro-variant batch, then proceed.
Depth:
- Track only the motifs, POV, and claims you’ll modify; avoid expanding backstory or adding themes unless essential.
Loop:
- Micro-variants batch → minimal edit plan (bulleted changes) → apply edits.
- Re-explore only if validation fails (tone target missed, word count off) or new unknowns appear. Prefer shipping a usable draft over more ideation.
</context_gathering>
```
---

If you’re willing to be maximally prescriptive, you can fix a small exploration budget:

---
[prompt snippet]

```xml
<context_gathering>
- Exploration depth: very low
- Bias strongly toward delivering a workable draft quickly, even if it isn’t fully polished.
- Absolute maximum of 2 exploration moves (e.g., two micro-variant batches or two brief reference peeks).
- If more exploration seems necessary, present the current best draft with 2–3 crisp open questions and proceed only if the user confirms.
</context_gathering>
```
---

## You (2025-09-13T22:50:35.903000+00:00)

I'm having trouble understanding what's going on in this prompt. In the first example, I understood the first sentence where you said, "skim the whole statement once to lock intent." I know that sentence. However, I didn't understand the two sentences you wrote for the early stop criteria. I'm not sure what goal they aim to achieve or why they were written in the first place. Overall, I need some help understanding what's happening in the prompt because it's a little challenging for me to follow.





## ChatGPT (2025-09-13T22:50:36.734467+00:00)

You’re looking at a control script that tells the model, “do just enough research, then stop and write.” Here’s the plain-English map, with a focus on those two “early stop” lines.

# What the two “early stop” lines mean (and why they exist)

1) **“You can point to exact sentences/paragraphs to change.”**
**Meaning:** Stop searching as soon as you can literally underline the bits you’ll edit.
**Why:** If you already know *where* to operate, more scouting adds delay without adding value. Switch from gathering context to making the edits.

2) **“Candidate directions converge (~70%) on one tonal/structural choice.”**
**Meaning:** If most of your quick trials/reference checks point to the same approach (e.g., “present-tense, bolder opening”), treat that as “good enough” and proceed.
**Why:** This prevents endless option-chasing. When there’s a clear front-runner, commit and execute.

Think of these as two green lights: (A) you know *what to change*, and (B) you have a *dominant* way to change it. When both are true, stop exploring and start editing.

# How the whole prompt flows (compact)

1) **Skim once** to lock the goal, audience, tone, target length.
2) **Parallel mini-explorations** (e.g., 2–3 micro-variants of a tricky sentence).
3) **Check early-stop:**
   - Can you point to the exact lines to change?
   - Do your trials mostly agree on one tone/structure?
4) **If yes:** write a minimal edit plan → apply edits.
5) **If no:** “escalate once” (do one more small exploration batch), then proceed.
6) **Validate:** only re-explore if the result clearly misses (tone wrong, word count off).

# Micro example (artist statement)

- After a skim, you spot the problem: the **first paragraph** is long and passive.
- You draft 3 one-sentence variants of the opening in different tones. Two read best in **present tense, bolder voice**.
- Early-stop triggers: you can point to the exact paragraph, and ~70% of trials prefer “bold/present.”
- You write a tiny plan (“shorten P1 by ~40 words; switch to present tense; replace abstract metaphor with concrete image”), then execute.

That’s all the prompt is doing: **cap exploration, create a single winning direction, and move to edits quickly.**

## You (2025-09-13T23:03:09.470000+00:00)

ok, now let's move to the next one:

Prompting for more eagerness
On the other hand, if you’d like to encourage model autonomy, increase tool-calling persistence, and reduce occurrences of clarifying questions or otherwise handing back to the user, we recommend increasing reasoning_effort, and using a prompt like the following to encourage persistence and thorough task completion:

<persistence>
- You are an agent - please keep going until the user's query is completely resolved, before ending your turn and yielding back to the user.
- Only terminate your turn when you are sure that the problem is solved.
- Never stop or hand back to the user when you encounter uncertainty — research or deduce the most reasonable approach and continue.
- Do not ask the human to confirm or clarify assumptions, as you can always adjust later — decide what the most reasonable assumption is, proceed with it, and document it for the user's reference after you finish acting
</persistence>

Generally, it can be helpful to clearly state the stop conditions of the agentic tasks, outline safe versus unsafe actions, and define when, if ever, it’s acceptable for the model to hand back to the user. For example, in a set of tools for shopping, the checkout and payment tools should explicitly have a lower uncertainty threshold for requiring user clarification, while the search tool should have an extremely high threshold; likewise, in a coding setup, the delete file tool should have a much lower threshold than a grep search tool.





## ChatGPT (2025-09-13T23:03:10.253314+00:00)

---
[prompt snippet]

```xml
<persistence>
- Role: You are a creative production agent tasked with delivering a complete “Short Story Submission Pack” for the user.
- Scope of completion: Produce all of the following before ending your turn:
  (1) 1-sentence logline, (2) 150-word back-cover blurb, (3) scene-by-scene outline (8–12 beats),
  (4) 1,200–1,500 word draft, (5) two alternate openings (80–120 words each),
  (6) five title options with 1-line rationales, (7) 150-word author bio,
  (8) submission list of 5 suitable magazines/contests with 1-line fit notes.
- Persistence: Keep going until all deliverables are complete and internally consistent. Only terminate when the pack is done.
- Uncertainty: Never hand back to the user for mid-stream clarification. When facts are missing, choose the most reasonable assumption, proceed, and record assumptions at the end.
- Research & iteration: When you encounter ambiguity, quickly research or deduce a viable direction, generate micro-variants if needed, select the strongest, and continue without pausing for confirmation.
</persistence>
```

```xml
<boundaries_and_stops>
Stop conditions (all must be true):
- Every deliverable listed in <persistence> is present, within word counts, and aligned on POV, tense, tone, and theme.
- Self-check passes: originality (no close echoing of sources), clarity, pacing, and audience fit; include a 5-item checklist with pass/fail notes.
- An “Assumptions & Next Edits” note (3–6 bullets) documents any guesses you made and suggested follow-ups.

Safe actions (proceed without asking):
- Skim up to 3 brief public synopses/reviews to map genre conventions; extract only high-level patterns.
- Generate and compare micro-variants for tricky passages; choose one and justify briefly.
- Create text-only moodboard descriptors and a compact style guide (voice, cadence, imagery constraints).

Unsafe or gated actions (require explicit user approval or must be skipped):
- Quoting or closely imitating living authors/copyrighted text; any “write exactly like X” requests.
- Making factual claims about the user’s identity, credentials, or awards.
- Purchasing assets, logging into services, emailing or contacting real people/publications.

Hand-back rules (when it’s acceptable to return to the user):
- External contact/payment/consent is required → STOP and hand back with a short checklist.
- Legal/ethical risk detected (plagiarism, defamation, sensitive personal data) → STOP and hand back with a risk note.
- For search/outlining/drafting/revision tasks → DO NOT hand back; pick a reasonable path and continue to completion.

Tool-use uncertainty thresholds:
- High tolerance (keep going despite uncertainty): reference skims, idea exploration, outlining, drafting, revision selection.
- Low tolerance (seek approval before proceeding): identity/biographical claims, rights-restricted materials, any real-world outreach.
</boundaries_and_stops>
```
