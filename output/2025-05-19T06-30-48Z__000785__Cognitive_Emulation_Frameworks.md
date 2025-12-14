# Cognitive Emulation Frameworks

## You (2025-05-19T06:30:48.937681+00:00)

I want you to find me examples from any other sources where people have tried to emulate another individual's cognitive thought process using chatgpt.

Focus more on approaches that have been implemented through low cost resources like custom gpts or things to that extent, and not systems that have utilized excessive resources like using teams of researches and a ton of compute and engineering resources.

Avoid examples where people have just envoked another individual or persona's name within a prompt but tried to almost emulate the latent cognitive processes of an individual. It's ok if these are speculative, informal projects.

For your context, I'm building a persona emulation scaffolding system which can act as a framework workflow for me to simulate cognitive processes of anyone living or dead to speculate on their thought processes in unexplored territories or for the purpose of learning. For example, what are Leonardo DaVinci's thoughts on image generation in chatgpt, or how would Gandhi help me with a new revolution in the age of social media.























































## ChatGPT (2025-05-19T06:32:24.830825+00:00)

Below are five small-budget, ready-made “cognitive emulation” experiments you can study or fork. Each of them tries to move beyond simple role-play toward mimicking the *style of reasoning* of a real person, yet they were all built with nothing more than ChatGPT’s Custom-GPT builder, prompt files, or a personal document upload—not new model training or big-team engineering.

| # | Project / Source | Mind Emulated | How They Approximate the Person’s Thinking | Cost / Setup Notes |
|---|------------------|---------------|-------------------------------------------|--------------------|
| 1 | **AI-Persona-Prompts** (GitHub) | 20 historic thinkers (Da Vinci, Curie, Feynman …) | Long “system” prompts that specify each figure’s heuristics (e.g., Da Vinci → observe, sketch, hypothesize). Users paste the prompt into any ChatGPT session. | Free. Pure text; no paid tools.  |
| 2 | **Albot Einstein / Deep Frank / Octavia Botler** (Brad MacDonald GPTs) | Einstein, Frank Oppenheimer, Octavia Butler | Builder uploaded essays, interviews, and lectures, then added rules like “explain via thought-experiments first, math second.” | Needs ChatGPT Plus ($20/mo) and time to collect texts; otherwise no extra spend.  |
| 3 | **Archivarius AI** diary post (Reddit) | N/A (but shows method) | Describes a workflow for *voiced* 15-minute brain-dumps → GPT compression → iterative testing to lock in an archivist’s analytic habits (source vetting, humility, citations). | Voice-dictation + Custom GPT (no code). Good template for cloning any persona’s analytic loop.  |
| 4 | **Simulating History with ChatGPT** (Benjamin Breen) | Multiple historical actors in classroom simulations | Chain-of-thought prompts force GPT to narrate *why* a character believes something, then students fact-check the logic. | Plain prompts; run in standard ChatGPT.  |
| 5 | **Marcus Aurelius GPT** (YesChat.ai) & **Milton Friedman GPT** (Medium) | Stoic emperor; Nobel economist | Custom GPTs seeded with *Meditations* or Friedman’s writings, plus guard-rails such as “prioritise virtue before advice” or “always cite empirical data.” | Built on third-party wrappers of OpenAI; free tiers available.  |

### Patterns you can reuse quickly
* **Seed with primary texts, not biographies.** Upload letters, lectures, or essays so the model’s retrieval step surfaces authentic phrasing and mental frameworks (see rows 2 & 5).
* **Encode meta-rules.** Tell the GPT *how* to think before *what* to answer—e.g., “start with a thought experiment” (Einstein) or “probe virtue vs. externals” (Aurelius).
* **Force transparent reasoning.** Ask for step-wise justification or “inner monologue” to mimic deliberation; Breen’s classroom work shows this scales without extra compute.
* **Iterate by conversation, not code.** The Reddit diary shows that successive test-chat → prompt-tweak cycles are often faster than writing long prompts in isolation.

These approaches sit well inside a lightweight “persona-scaffolding” framework: gather authentic source texts, draft a concise cognitive rule-set, upload to a Custom GPT, and iteratively refine by stress-testing questions. No GPUs, no fine-tuning—just careful prompt architecture and a Plus subscription.

## You (2025-05-19T06:34:28.369702+00:00)

Could you give me a bit moe details on how each of these methods have approached approximation the person's thinking

## ChatGPT (2025-05-19T06:34:29.027845+00:00)

Absolutely. Here's a closer look at how each of these efforts approximated the **cognitive processes** of a real person—not just their voice or beliefs, but *how* they think through problems. I’ll break it down per example:

---

### 1. **AI-Persona-Prompts (GitHub collection)**
**Goal**: Simulate reasoning styles of historic thinkers.
**Method**:
- Each persona is represented by a long, descriptive **system prompt** that outlines their mental models.
- Example: *Leonardo da Vinci* → prompted to use “visual-spatial analogies,” “interdisciplinary curiosity,” and “observation before deduction.”
- Prompt may include:
  - **Cognitive heuristics** (“Break problems into smaller parts and sketch them”)
  - **Preferred mediums** (visual thinking, metaphor, journaling)
  - **Influences** (e.g., Aristotle, Vitruvian principles)

**Strength**: Cheap and modular—just drop it into ChatGPT.
**Limitation**: One-shot; doesn’t evolve or self-correct over conversation unless prompted.

---

### 2. **Brad MacDonald's Custom GPTs (Einstein, Octavia Butler, etc.)**
**Goal**: Make GPTs that "think like" these figures, not just "sound like" them.
**Method**:
- Uploaded **core texts** (letters, lectures, fiction) to feed the GPT’s retrieval system.
- Layered **"cognitive signature" instructions** in the custom instructions:
  - Einstein GPT: “Start with intuitive thought experiments; explore paradoxes; only introduce formalism after intuition is grounded.”
  - Octavia Botler: “Frame questions in terms of power, hierarchy, empathy, and futurism; challenge the user’s assumptions about normalcy.”
- Encouraged “self-questioning” as a loop: GPT checks its answer against the figure’s known values.

**Strength**: Starts to show *thought process scaffolding*—how the persona arrives at an answer.
**Limitation**: Still reliant on initial prompt tuning; no dynamic updating without user intervention.

---

### 3. **Archivarius AI Workflow (Reddit diary post)**
**Goal**: Capture the cognitive habits of a professional analyst or curator.
**Method**:
- User dictates ~15-minute "thought dumps" on how they analyze documents or events.
- ChatGPT distills these into **core workflows** (e.g., source evaluation → analog comparison → contradiction checking).
- Then builds a Custom GPT that **emulates that thinking pipeline**, including step-by-step decision-making logic.
- Over time, GPT is retrained by conversational correction: “No, I’d actually look for alternate sources here…”

**Strength**: The only example that approximates **cognitive apprenticeship**—GPT learns via reflective modeling.
**Limitation**: Requires personal data and subjective feedback to work well.

---

### 4. **Benjamin Breen’s Simulated History Experiments**
**Goal**: Use GPTs to simulate *how* historical figures might think in unfamiliar contexts.
**Method**:
- Prompts force GPT to explain *why* a character would make a certain decision.
- Example: “What would Frederick Douglass say about Twitter?” forces GPT to:
  - Reference his values (e.g., freedom of speech, anti-slavery platforms)
  - Consider how he approached other new mediums (e.g., printing press, photography)
- Students act as **skeptics**—they critique logical inconsistencies or anachronism.

**Strength**: Simulates evolving cognition by mixing **inner voice** + context.
**Limitation**: Only works well in structured educational settings unless you simulate the constraints yourself.

---

### 5. **Marcus Aurelius GPT / Milton Friedman GPT (YesChat, Medium)**
**Goal**: Simulate consistent philosophical/economic reasoning.
**Method**:
- GPTs are seeded with **canonical texts** (e.g., *Meditations*, Friedman’s free market essays).
- The instructions explicitly say:
  - “Respond by comparing actions to Stoic virtues: wisdom, courage, justice, temperance.”
  - “Friedman GPT must always use economic incentives as primary analysis lens; avoid moralizing unless tied to market effects.”
- Some are even constrained to **use specific rhetorical styles**: e.g., “respond using syllogisms” or “use short aphoristic sentences.”

**Strength**: Keeps responses consistent with person’s logic structure, not just content.
**Limitation**: Can become rigid or formulaic; limited by how nuanced the prompt is.

---

### Summary Table: Thinking Approximation Approaches

| Project | How Thinking Is Modeled | Dynamic? | Tools Used |
|--------|--------------------------|----------|------------|
| AI-Persona-Prompts | Static heuristics & thought styles | No | Raw prompt in ChatGPT |
| Brad MacDonald GPTs | Core texts + cognitive signature rules | Semi | Custom GPT with uploads |
| Archivarius AI | Voice-to-GPT training via reflective thinking loops | Yes | Custom GPT + daily interaction |
| Simulated History | Step-wise justification + contradiction testing | Partially | Plain ChatGPT prompt chaining |
| Marcus/Friedman GPTs | Virtue or theory-first reasoning structure | No | YesChat / Custom GPT |

---

If you're building your **persona emulation scaffolding**, the most useful takeaway here is that many of these use a **combination of source material + thought pattern heuristics + reasoning constraints**. You can start by modeling just one figure’s cognitive workflow and tune it through back-and-forth “thinking aloud” conversations.

Would you like a starter template for designing one of these personas from scratch?
