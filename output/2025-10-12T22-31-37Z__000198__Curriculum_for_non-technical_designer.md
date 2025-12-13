# Curriculum for non-technical designer

## You (2025-10-12T22:31:37.763000+00:00)

### 🔹 **Goal**

Provide a curriculum-style, tiered learning path for a non-technical designer seeking to use Model-CoPilot Platforms (MCPs) like Codeium CLI, Gemini, or GitHub Copilot to generate functional front-end code from Figma prototypes. The user has zero prior experience with programming or developer tools. The goal is to identify the essential minimum skills, concepts, and tooling knowledge required at each tier (Beginner → Intermediate → Advanced) to:

* Set up and use MCPs with Figma
* Diagnose and troubleshoot common issues
* Understand how AI-generated code works
* Prompt MCPs effectively for usable front-end prototypes

### 🔹 **Return Format**

Return a structured curriculum in three tiers:

1. **Beginner Tier**

   * Learning objectives
   * Key concepts (plain-language explanations)
   * Required tools and setup steps
   * Practical exercises (including prompts to try with MCPs)
   * Common pitfalls and how to address them

2. **Intermediate Tier**

   * Deeper understanding of file structures, front-end architecture (HTML/CSS/JS basics)
   * Enhanced MCP prompting strategies
   * Diagnostic techniques for AI-generated code (e.g., reading error messages)
   * Real-world scenarios (e.g., modifying generated code, handling responsiveness)

3. **Advanced Tier**

   * Strategies for improving AI output quality
   * Basic git usage (pull, commit, push)
   * Integrating Figma plugins or design tokens into code workflows
   * Diagnosing deeper problems (e.g., why the UI isn’t rendering as expected)

Each tier should be learner-friendly, progressive, and aligned with real-world workflows between Figma and AI-assisted code generation.

### 🔹 **Warnings & Guardrails**

* Avoid assuming any prior programming knowledge; introduce technical terms in plain language.
* Do not assume access to paid tools unless explicitly free or noted.
* Clearly distinguish between **must-know skills** vs. **nice-to-have/advanced** ones at each tier.
* Flag ambiguous areas where AI code may fail or need user intervention, and offer diagnostic tips.
* Be transparent about limitations of MCPs (e.g., hallucinated code, poor error messages, missing context from Figma).

### 🔹 **Context & Additional Elements**

Persona: A non-technical UX/UI designer with strong visual and interaction design skills but zero coding or toolchain exposure.
Tools: Figma (with plugins), MCPs (like Codeium CLI, Gemini, or Copilot), AI assistants
Execution Style: Clear, accessible language. Encourage hands-on experimentation with guided AI prompts and sandbox projects.

## ChatGPT (2025-10-12T22:40:59.236122+00:00)

Below is a practical, three‑tier curriculum designed **for a non‑technical designer** who wants to turn Figma prototypes into working front‑end code with the help of Model/AI co‑pilots (e.g., Codeium/Windsurf, Gemini CLI/Code Assist, GitHub Copilot). It focuses on the **minimum** skills and tools you need at each step, with hands‑on prompts, guardrails, and diagnostics.

> **Note on “MCP”:** In this guide, “co‑pilots” refers to coding assistants like **Codeium/Windsurf**, **Gemini (CLI / Code Assist)**, and **GitHub Copilot**. Separately, Figma now offers an **MCP server** that lets AI agents pull design context directly (advanced + requires paid Figma seats). Where relevant, this is flagged and kept optional. citeturn3view0

---

## Overview — What you’ll be able to do

- **Beginner:** Open a project, preview a page, ask an AI to generate simple, usable HTML/CSS, and fix common breakages.
- **Intermediate:** Read folder/file structure, understand HTML/CSS/JS basics, prompt for responsiveness, and debug with DevTools.
- **Advanced:** Improve AI output quality with design tokens and constraints, use Git to version/deploy, and (optionally) connect Figma’s MCP server so co‑pilots can pull design context directly from your file.

---

## Tier 1 — **Beginner**

### 1) Learning objectives
- Install the essential tools (editor, browser preview, an AI co‑pilot).
- Open a folder, create `index.html` and `style.css`, and run a local preview.
- Prompt an AI to generate a simple, working section from a Figma frame.
- Export assets from Figma and reference them in your page.
- Diagnose the **top 10 beginner errors** (e.g., CSS didn’t load, wrong file path).

### 2) Key concepts (plain language)
- **File vs. folder:** A *file* is a single document like `index.html`; a *folder* holds files.
- **HTML / CSS:** HTML = structure (the boxes on the page). CSS = appearance (colors, spacing, fonts).
- **Linking CSS:** Your HTML must “link” to your CSS file so styles apply.
- **Live preview:** A simple web server that refreshes the page when you save.
- **Prompting:** Telling the AI what to build and how (constraints), not just “make a site.”

### 3) Required tools & setup (free‑first)
- **Visual Studio Code** (or VSCodium).  
- **Live preview**: VS Code “**Live Server**” extension (one‑click local preview). citeturn1search1  
- **An AI co‑pilot** (choose one):
  - **GitHub Copilot (Free plan available with monthly limits)** in VS Code. citeturn0search1turn0search11  
  - **Windsurf / Codeium VS Code extension (free for individuals)**. citeturn5search2  
  - **Gemini Code Assist (VS Code extension) or Gemini CLI** (free/individual options available; quotas apply). citeturn7search13turn7search1
- **Figma → Dev Mode (viewer/inspector)** to see sizes, fonts, colors, and export assets. citeturn0search3

> Optional installs now (you’ll certainly need later): **Node.js LTS** and **Git**. If you install Node now, prefer the LTS release. citeturn1search2turn1search4

**Setup checklist**
- Install VS Code → add **Live Server**. citeturn1search1  
- Install one AI co‑pilot (Copilot / Codeium / Gemini extension). citeturn0search1turn5search2turn7search13  
- In Figma, open your file → **Dev Mode** → identify a single frame to replicate (typography, spacing, colors, images). citeturn0search3  
- Export any needed images/SVGs from that frame.

### 4) Practical exercises (with prompts)

**Exercise A — Your first hero section (static)**
1) Create a folder `landing/` → add `index.html` and `style.css`.  
2) Start **Live Server** to preview. citeturn1search1  
3) In Figma Dev Mode, note: font family, sizes, color hex codes, spacing, and images for the hero. citeturn0search3  
4) **Prompt (Copilot/Codeium/Gemini in VS Code):**  
   > *“Generate a minimal, accessible **hero section** for `index.html`. Put **all styles in `style.css`**, no frameworks. Use these tokens from Figma: Heading font: Inter 48/56, Body: Inter 16/24, Primary color: #4F46E5, Gray text: #6B7280, Spacing scale: 8px steps. Include a call‑to‑action button and a placeholder image at `assets/hero.png`. Make it readable on mobile and desktop. Explain how to link `style.css` and where to place the image.”*
5) Paste generated HTML/CSS, ensure `<link rel="stylesheet" href="style.css">` is present, save, and refresh.

**Exercise B — Two‑column feature list**
- Same flow, new frame. Prompt for a two‑column layout with **CSS Grid** and a mobile single column.

**Exercise C — Swap colors & spacing**
- Prompt:  
  > *“Refactor `style.css` to switch the primary color to `#0EA5E9` and increase section padding by 8px, keeping everything else unchanged.”*

### 5) Common pitfalls & quick fixes
- **Blank white page?** Start/refresh Live Server; ensure you opened the **folder**, not just files. citeturn1search1  
- **Styles not applying?** Check the `<link>` tag and file name/path; save both files.  
- **Images not showing (404):** Put assets in `assets/` and reference with a *relative* path like `src="assets/hero.png"`.  
- **Fonts wrong:** The web needs a web‑safe font or a web font import; ask the AI to add a Google Fonts import for your family.  
- **Layout broken on mobile:** Ask the AI to add a **mobile‑first** media query and test by narrowing the browser.

---

## Tier 2 — **Intermediate**

### 1) Learning objectives
- Understand basic **front‑end architecture**: what goes in HTML, CSS, and small amounts of JS.
- Read a **project structure** and keep code organized.
- Prompt for **responsive** layouts and semantic HTML.
- Use **browser DevTools** and **console** to diagnose issues.
- Make small, safe edits to AI‑generated code.

### 2) Key concepts (plain language)
- **Project structure:**  
  ```
  /project
    index.html
    /assets (images, icons)
    /css (style.css or more files later)
    /js  (optional enhancements)
  ```
- **Semantic HTML:** Use tags that convey meaning: `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`.
- **CSS layout:** **Flexbox** (1‑D rows/columns), **Grid** (2‑D layout), **media queries** (sizes).
- **Progressive enhancement:** Page should work without JS; JS adds interactivity (e.g., mobile menu).
- **Debugging loop:** Reproduce → Inspect → Hypothesize → Change → Verify.

### 3) Enhanced prompting strategies
- **Constrain scope:** “**Only** HTML + CSS. No frameworks. Put styles in `/css/style.css`.”
- **Be explicit about responsiveness:** “Mobile‑first, breakpoint at 768px; stack to single column below that.”
- **Ask for comments:** “Comment the CSS sections and explain the layout decisions in plain language.”
- **Provide inputs:** Paste exact **colors/spacing** from Figma Dev Mode and link to any exported SVGs. citeturn0search3

**Prompt examples**
- *“Given `index.html` and `/css/style.css`, turn this hero into a **3‑breakpoint responsive** layout (≤480px, 481–1024px, ≥1025px). Keep typography consistent with: H1 48/56, body 16/24, color #111827 / #6B7280. Explain your media queries.”*
- *“Create an accessible mobile nav: hamburger button, focus states, `aria-expanded`. Vanilla JS in `/js/nav.js`. Keep HTML/CSS unchanged except for minimal hooks.”*

### 4) Diagnostic techniques for AI‑generated code
- **Read the console (F12 → Console):** Look for red error lines; they often point to the file and line number.
- **Inspect elements:** Right‑click → *Inspect*. Hover CSS rules to see what’s applying; look for crossed‑out rules (overridden by specificity).
- **Layout debugging:** Temporarily add `outline: 1px solid` to key containers; ask the AI to add a `.debug * { outline: 1px solid }` helper then remove later.
- **File paths:** Keep asset paths **relative** and case‑correct (`assets/Icon.svg` ≠ `assets/icon.svg`).

### 5) Real‑world scenarios & exercises

**Exercise D — Make it responsive**
- Take your Tier‑1 section and request **two breakpoints** with Grid for desktop and single column for mobile. Validate in DevTools’ responsive mode.

**Exercise E — Add a mobile menu (JS)**
- Prompt for minimal JS that toggles a class on a nav; require **ARIA** attributes and focus styles.

**Exercise F — Modify generated code**
- Ask the co‑pilot to *refactor* CSS to variables at the top of `style.css` (e.g., `--color-primary: #4F46E5;`) and reuse them consistently.

**Exercise G — Read and resolve an error**
- Deliberately mis‑name an image; reload; read the 404 in console; fix the path; confirm resolution.

### 6) Common pitfalls (and fixes)
- **CSS “fights” itself:** If rules don’t apply, reduce specificity; prefer class selectors over ID/deep nesting.
- **Jumping layout:** Missing fixed dimensions for images or inconsistent padding; use consistent spacing scale.
- **Accessibility gaps:** Ensure color contrast; keyboard focus is visible; add `aria-label` to icon‑only buttons.

---

## Tier 3 — **Advanced**

### 1) Learning objectives
- **Improve AI output quality** by supplying **design tokens**, component constraints, and code style rules.
- Use **Git** to save versions, branch safely, and publish a static prototype.
- **(Optional)** Connect **Figma’s MCP server** to your co‑pilot so it can pull design context (components, variables) rather than guessing from screenshots.
- Diagnose deeper rendering problems (stacking context, overflow, z‑index, pathing, MIME issues).

### 2) Strategies to improve AI output quality
- **Feed tokens early:** Provide a small `tokens.json` (colors, spacing, radii, typography) and ask the co‑pilot to emit CSS variables from it (or Tailwind config if you later choose Tailwind).
- **Lock a stack:** Specify “vanilla HTML/CSS” or “React + Vite” (only when you’re ready); otherwise assistants may add frameworks you don’t want.
- **Ask for **diff‑based** changes:** “Only modify the button component; show the diff and explain.”
- **Reference components:** Describe Figma component names and expected props/states so generated code maps cleanly.
- **Linter/formatter:** Ask the co‑pilot to add **Prettier** config and keep to it for consistent output.

### 3) Integrating Figma plugins, variables, and design tokens
- **Tokens in Figma:** Use **Tokens Studio** (plugin) to manage design tokens in Figma; it can mirror tokens as JSON you can map to CSS variables. citeturn0search4turn0search14
- **Dev Mode to code:** Use Figma Dev Mode to inspect variables, spacing, and component properties for precise specs. citeturn0search3
- **(Optional / paid plans)** **Figma MCP server**: lets an AI client (e.g., Gemini CLI, VS Code clients) pull design context (variables, components, node selection) directly. Requires a **Dev or Full seat on a paid plan**; available via local or remote server and can be connected to supported clients (VS Code, Cursor, etc.). citeturn3view0
  - Example: **Gemini CLI + Figma** — install the **Figma Gemini CLI extension** then authenticate; the co‑pilot can reference Figma frames via links. citeturn6view0

### 4) Basic Git (pull, commit, push) + deploy (free)
- **Why Git?** Safe checkpoints and easy rollbacks.
- **Must‑know commands:** `git add`, `git commit -m "msg"`, `git push origin main`. citeturn4search6turn4search4
- **Publish a static prototype** with **GitHub Pages** (free): enable Pages on your repo and serve from the root or `/docs`. citeturn4search2turn4search1

**Exercise H — Add tokens to your CSS**
- Export or write minimal design tokens (colors, spacing scale, font sizes).  
- Prompt:  
  > *“Create a `:root` block of CSS variables from this tokens JSON and refactor `style.css` to use them. Add comments and keep the visual appearance unchanged.”*

**Exercise I — (Optional) Figma MCP server → Gemini CLI**
- Install **Gemini CLI** and then the **Figma Gemini CLI extension**; authenticate; paste a Figma frame link; ask:  
  > *“Generate semantic HTML/CSS for this selected Figma frame. Use my CSS variables; explain any mismatches. Return exactly two files: `index.html` and `css/style.css`.”* citeturn7search2turn7search0turn6view0

**Exercise J — Git & deploy**
- Initialize a repo, commit your files, push to GitHub, enable GitHub Pages, and share a public URL. citeturn4search2

### 5) Deep‑dive diagnostics (why the UI isn’t rendering)
- **Blank page with JS present:** A JavaScript error halted rendering—open Console; fix the first red error.
- **Z‑index doesn’t work:** Parent has `overflow: hidden` or a new stacking context (`position` + `z-index` interplay). Remove/adjust the offending property.
- **Fonts not loading:** Check network panel for 404 or CORS; ensure the CSS `@import` or `<link>` uses HTTPS and correct paths.
- **SVG not visible:** May inherit `fill="none"` or be masked by CSS; try `svg { width/height }` and set explicit `fill`.
- **Images fuzzy:** Export 2× from Figma for high‑DPI screens; include `width`/`height` attributes in HTML to avoid layout shifts.

---

## Must‑know vs. Nice‑to‑have (at each tier)

**Beginner — Must‑know**
- Run a local preview; create/edit `index.html` + `style.css`.
- Export assets from Figma Dev Mode and reference with correct paths. citeturn0search3
- Prompt an AI to produce a small, focused section and iterate.

**Beginner — Nice‑to‑have**
- Node.js LTS installed for future tooling. citeturn1search2

**Intermediate — Must‑know**
- Semantic HTML, Flexbox/Grid basics, media queries.
- Read console errors; inspect and modify CSS rules live.

**Intermediate — Nice‑to‑have**
- Simple vanilla JS for interactivity; CSS variables.

**Advanced — Must‑know**
- Git add/commit/push; publish via GitHub Pages. citeturn4search6turn4search2
- Use tokens or a style guide to steer AI output.

**Advanced — Nice‑to‑have**
- **Figma MCP server** with supported AI clients (orgs on paid plans). citeturn3view0
- Gemini CLI extensions workflow (e.g., Figma extension) to pull design context. citeturn6view0

---

## Limitations & guardrails (be aware)

- **AI can hallucinate**: Class names, assets, or files that don’t exist. Always check file paths and the **actual folder** contents.
- **Missing context from Figma**: Without MCP integration, AIs don’t “see” your file; you must paste measurements/tokens or share images/specs manually. citeturn0search3
- **Paid requirements**: Figma **MCP server** and **Figma for VS Code** require specific paid seats/plans—treat as optional extras for org teams. citeturn3view0turn1search0
- **Security** (advanced): Be cautious with any co‑pilot that can execute commands via CLI; keep tools updated and avoid running untrusted instructions. (Gemini CLI is actively evolving—keep to patched versions and review commands.) citeturn7news20

---

## Your first 2–3 weeks (suggested path)

1) **Week 1 (Beginner)**  
   - Tools + Hello World hero section + fix 3 common pitfalls.
2) **Week 2 (Intermediate)**  
   - Add responsiveness, mobile nav JS, and refactor to CSS variables.
3) **Week 3 (Advanced)**  
   - Introduce tokens from Figma/Tokens Studio; version with Git; publish on GitHub Pages; (optional) try Gemini CLI + Figma MCP server if your plan allows. citeturn0search4turn4search2turn3view0

---

## Copy‑paste prompt kit (you can adapt)

- **Structure & constraints**
  - “Create a **single** `index.html` and `css/style.css`. **No frameworks**. Mobile‑first, 768px breakpoint. Explain your CSS sections.”
- **Match Figma**
  - “Use these exact values from Figma: Primary `#4F46E5`, Neutral `#6B7280`, Spacing 8/16/24/32px, H1 48/56 Inter, Body 16/24 Inter.”
- **Accessibility**
  - “Ensure accessible color contrast, keyboard focus outlines, and `aria-label` for icon buttons.”
- **Refactor**
  - “Refactor to **CSS variables** at the top of `style.css`. Keep visuals identical. Show only changed lines.”
- **Debug help**
  - “Why is my hero image not visible? Inspect `index.html` + `css/style.css` and propose the smallest fix. Explain the root cause.”

---

### References (for when you want the official docs)
- **Figma Dev Mode** (inspect & handoff). citeturn0search3  
- **Figma MCP server** (open beta; paid seats; local/remote setup; supported clients). citeturn3view0  
- **Figma ↔ VS Code** extension (availability/seat requirements). citeturn1search0  
- **Gemini CLI / extensions** (open‑source CLI; extension install commands). citeturn7search2turn7search0  
- **Gemini Code Assist (VS Code)** setup. citeturn7search13  
- **Git essentials** (add/commit/push). citeturn4search6  
- **GitHub Pages** quickstart (free static hosting). citeturn4search2turn4search1  
- **Live Server** (VS Code preview). citeturn1search1  
- **Tokens Studio** (design tokens in Figma). citeturn0search4  
- **GitHub Copilot in VS Code** (includes info on a free plan with limits). citeturn0search1

---

### Final advice
Start **small and specific** (one section, one breakpoint). Give the AI **clear constraints**, paste the exact values from Figma, and keep a **tight feedback loop**: preview → inspect → refine. As you gain confidence, graduate to tokens, Git, and (if your team has the seats) Figma’s MCP server for richer context.

