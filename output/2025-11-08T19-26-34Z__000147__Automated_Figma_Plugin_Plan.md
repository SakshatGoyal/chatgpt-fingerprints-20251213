# Automated Figma Plugin Plan

## You (2025-11-08T19:26:34.352000+00:00)

You are a senior product manager with strong technical fluency but no direct access to a team. Your objective is to create a Figma plugin that replicates the core functionality of the A11y Contrast Checker plugin. Your constraints: you must delegate all work—research, coding, DevOps, and Figma integration—to AI agents, specifically using **Atlas** (browser-based agent) and **Codex** (code-generation agent), along with GitHub and Figma as platforms. You must design a **complete, automated execution plan** that minimizes or eliminates manual intervention. Your audience is a technically fluent PM or stakeholder with little to no design or plugin experience.

---

**📦 Return Format**
Produce a **Notion-compatible document** (Markdown format preferred) organized as follows:

1. **Overview Section**

   * Project summary
   * Goals and constraints
   * Tools used (Atlas, Codex, GitHub, Figma)
   * Assumed skillset of executor

2. **Execution Plan (Phased Breakdown)**

   * Use a clear hierarchical structure:

     * **Phase** → **Milestones** → **Tasks**
     * Include dependencies and tool delegation (e.g., “Codex generates X”, “Atlas triggers Y”)
   * Each task should:

     * Specify input/output formats
     * Identify automation strategy
     * Flag any unavoidable manual steps (if any)

3. **Folder & Repo Architecture**

   * GitHub repo structure
   * Naming conventions
   * Suggested automation (e.g., CI/CD GitHub Actions for plugin bundling)

4. **Deployment & DevOps Automation**

   * How builds are triggered, tested, and published
   * Environment setup (e.g., Node, Plugin manifest)
   * Release management and versioning

5. **Risks & Limitations**

   * Where AI delegation may need fallback logic or validation
   * Legal or policy constraints with publishing to Figma community

6. **Appendix**

   * Links to similar plugins for reference
   * Glossary of Figma Plugin terms for non-designers
   * Example code snippets or commands (delegated to Codex)

---

**🚧 Warnings & Guardrails**

* Be transparent where full automation may not be possible (e.g., Figma plugin publishing may require human review).
* Explicitly distinguish **what Atlas does vs what Codex does**—do not conflate them.
* If assumptions are made (e.g., which API to use, project structure), list them clearly.
* Ensure that the plan is **executable by a solo PM**, not a developer.

---

**📚 Context & Additional Elements**

* Assume the plugin will replicate **core A11y contrast ratio detection**, including scanning text elements, comparing against WCAG thresholds, and reporting failures in a UI.
* Codex is capable of full-stack generation but must be guided step-by-step with context.
* Atlas is capable of browsing, submitting forms, scraping, and file operations within a controlled browser environment.
* The user is comfortable triggering actions but prefers a “one-command” DevOps flow where possible.







## ChatGPT (2025-11-08T19:26:50.275675+00:00)

# A11y Contrast Checker — Fully Automated Build Plan (Atlas × Codex)

---

## 1) Overview

**Project summary**
Deliver a Figma plugin that scans selected frames/layers, computes text–background contrast, evaluates against WCAG (AA/AAA), and reports failures with fix suggestions—replicating the core behavior of “A11y Contrast Checker.”

**Goals & constraints**
- 100% of research, coding, testing, and packaging delegated to AI:
  - **Atlas** (browser agent) for web tasks, forms, repo ops via the web UI, and Figma Community submission steps that must occur in-app.
  - **Codex** (code agent) for all code generation, edits, tests, and CI config.
- Minimize manual steps; prefer “one-command” flows to kick off everything.
- Ship a working MVP; optional niceties are deferred.

**Tools**
- **Atlas**: browse docs, scaffold repos via GitHub UI, manage PRs/releases, fill store forms, run Figma desktop steps that need UI (with your assistance to click where required).
- **Codex**: generate plugin code (TypeScript), UI (HTML/React), tests, build scripts, GitHub Actions.
- **GitHub**: remote repo, issues/PRs, Actions for CI/CD.
- **Figma**: Plugin API, desktop app for local dev & publishing (submission requires desktop flow).

**Assumed executor skillset**
Technically fluent PM comfortable triggering agents, approving PRs, and clicking through one-time Figma submission dialogs. No prior plugin or design experience required.

---

## 2) Execution Plan (Phased)

### Phase 0 — Project Bootstrap
**Milestones**
- M0.1 Decision record + assumptions
- M0.2 Repo + CI skeleton live

**Tasks**
1) **Draft assumptions (Atlas)**
   - **Input**: This brief + appendix links
   - **Output**: `/docs/assumptions.md` with: WCAG refs, plugin scope, supported nodes (TEXT + fills), thresholds (AA/AAA), and limits.
   - **Automation**: Atlas searches official Figma Plugin docs and publishing rules; stores excerpts in the doc.

2) **Create GitHub repo (Atlas)**
   - **Input**: Org/name you choose
   - **Output**: Repo with default branch `main`, branch protection on.
   - **Automation**: Atlas uses GitHub UI to create repo, labels, and issue templates.

3) **Scaffold CI (Codex)**
   - **Input**: Repo URL
   - **Output**: `.github/workflows/build.yml` and `.nvmrc`, `package.json` with scripts.
   - **Automation**: Codex commits a workflow that installs Node, builds plugin bundle, runs tests, and uploads artifacts.

---

### Phase 1 — Plugin Foundations
**Milestones**
- M1.1 Valid `manifest.json`
- M1.2 Dev server + hot-reload

**Tasks**
1) **Initialize plugin skeleton (Codex)**
   - **Input**: Requirement “Figma plugin with custom UI”
   - **Output**: `/src/code.ts`, `/src/ui/*`, `manifest.json` (with `ui.html`, menu, permissions), `esbuild.config.js` (or `create-figma-plugin` config).
   - **Automation**: Codex generates manifest per latest Figma spec.

2) **Local run instructions (Codex)**
   - **Input**: macOS target
   - **Output**: npm scripts: `dev`, `build`, `package`.
   - **Automation**: Codex includes notes to load the built folder via Figma’s **Plugins → Development → Import from manifest**.

3) **CI build artifact (Codex)**
   - **Input**: build script
   - **Output**: zipped `/dist` artifact on every PR and `main` push.

---

### Phase 2 — Core Contrast Engine
**Milestones**
- M2.1 Node scanning
- M2.2 WCAG evaluation
- M2.3 Report model

**Tasks**
1) **Node traversal (Codex)**
   - **Input**: spec of supported nodes (TEXT layers; also vector/rect with fills as backgrounds)
   - **Output**: `scanNodes()` extracting computed foreground/background color pairs per text node (resolving styles, fills, opacity, effects).
   - **Automation**: Codex writes pure TypeScript using Figma Plugin API.

2) **Color extraction & flattening (Codex)**
   - **Input**: fills/effects; blending
   - **Output**: `resolveColor(node)` that returns sRGB for fg/bg.

3) **WCAG computation (Codex)**
   - **Input**: sRGB colors + text size/weight
   - **Output**: `getContrastRatio(fg, bg)`, thresholds for AA/AAA (normal/large).
   - **Automation**: Codex includes unit tests for ratio math and threshold logic.

4) **Result model & UI channel (Codex)**
   - **Input**: scan results
   - **Output**: JSON payload to UI `{nodeId, contrast, status, requiredLevel, suggestions[]}`; typed with Zod/TS types.

---

### Phase 3 — UI & Fix Suggestions
**Milestones**
- M3.1 Results UI (filter/sort)
- M3.2 One-click color suggestions
- M3.3 Annotate failures

**Tasks**
1) **UI list + filters (Codex)**
   - **Input**: result JSON
   - **Output**: `ui.html` + `ui.tsx` with table; filters by status (Fail/Pass AA/AAA), search, “jump to layer.”

2) **Suggestion engine (Codex)**
   - **Input**: failed pairs + target level
   - **Output**: `suggestAccessibleColor(fg, bg, target)` returning nearest AA/AAA pair; “Apply” sends message to update fills.

3) **Annotations (Codex)**
   - **Input**: failures
   - **Output**: group of “issue markers” near offending nodes, with relaunch buttons in right-click menu to recheck.

---

### Phase 4 — QA, Telemetry (opt-in), and Docs
**Milestones**
- M4.1 Unit tests (math & parsing)
- M4.2 Manual test script
- M4.3 README + screenshots

**Tasks**
1) **Test suite (Codex)**
   - **Input**: edge cases (transparent overlays, mixed fills)
   - **Output**: Jest/Vitest tests; snapshot of UI render.

2) **Atlas test pass**
   - **Input**: sample Figma file
   - **Output**: Atlas executes a written test script: scan a page, verify counts, exercise “Apply fix,” export a summary.

3) **Docs (Codex + Atlas)**
   - **Input**: feature list
   - **Output**: `README.md` with install/run, GIFs, and troubleshooting; Atlas sources links to official docs and similar plugins.

---

### Phase 5 — Packaging, Releases, and Community Submission
**Milestones**
- M5.1 Versioned release
- M5.2 Community submission queued

**Tasks**
1) **Release pipeline (Codex)**
   - **Input**: semver tag
   - **Output**: GitHub Action: on `v*` tag, run build, attach zip, generate changelog, create GitHub Release.

2) **Community submission (Atlas + You)**
   - **Input**: built zip, icon, cover assets, description
   - **Output**: Submitted plugin (pending Figma review).
   - **Automation**: Atlas guides the Figma desktop flow; **Figma requires desktop app submission** and review against guidelines. Some manual clicks are unavoidable.

---

### Phase 6 — Post-Launch Ops
**Milestones**
- M6.1 Feedback loop
- M6.2 Patch flow
- M6.3 Roadmap next

**Tasks**
1) **Issue templates (Atlas)**
   - **Output**: Bug/feature templates in `.github/ISSUE_TEMPLATE/*`.

2) **Hotfix protocol (Codex)**
   - **Output**: “/docs/release.md” with version bump rules; patch via `fix/*` branches and Actions.

3) **Backlog (Atlas)**
   - **Output**: Notion board items—bulk scan performance, style inheritance edge cases, per-brand contrast presets, and widget variant (optional).
   - **Note**: Widgets have a different manifest if you expand later.

---

## 3) Folder & Repo Architecture

```
figma-a11y-contrast/
├─ .github/
│  └─ workflows/
│     └─ build.yml
├─ docs/
│  ├─ assumptions.md
│  └─ release.md
├─ src/
│  ├─ code.ts              # main plugin logic (Figma Plugin API)
│  ├─ engine/
│  │  ├─ scan.ts           # traverse nodes, collect pairs
│  │  ├─ color.ts          # sRGB conversions, flatten fills
│  │  └─ wcag.ts           # contrast math + thresholds
│  ├─ ui/
│  │  ├─ ui.html
│  │  ├─ ui.tsx
│  │  └─ styles.css
│  └─ types.ts
├─ manifest.json           # per Figma spec
├─ esbuild.config.js       # or create-figma-plugin config
├─ package.json
├─ tsconfig.json
└─ README.md
```

**Naming**
- Package: `@yourorg/figma-a11y-contrast`
- Branches: `main`, `feat/*`, `fix/*`, `docs/*`
- Tags: `vMAJOR.MINOR.PATCH`

**Automation**
- GitHub Actions: build/test on PR; release on tag; attach zip artifact.
- Optional: use `create-figma-plugin` for scaffolding and packaging.

---

## 4) Deployment & DevOps Automation

**Environment**
- Node LTS in CI (`.nvmrc`)
- `manifest.json` maintained by Codex per Figma spec.

**Build & Test**
- `npm run build` → bundles `/dist`
- `npm test` → unit/snapshot tests
- CI caches `~/.npm`, produces artifacts on every PR

**Release**
- Tag `vX.Y.Z` → Action runs build + changelog → GitHub Release with zip attached

**Publish to Figma Community**
- Use **Figma desktop**: Plugins → Manage → **Publish**; fill details, upload media, submit for review (can’t be fully automated). Reviewed against Figma’s guidelines.

---

## 5) Risks & Limitations

- **Submission friction**: Figma requires desktop app submission & human review—cannot be fully automated.
- **API edge cases**: Complex fills, blend modes, nested instances may yield ambiguous background colors—add “best-effort” resolution + fallback warning.
- **Legal/policy**: Must meet Community review rules; avoid misleading claims; include correct licensing and permissions.
- **Overlap with native features**: Figma provides built-in contrast checks; differentiate via batch scan/reporting and fix suggestions.
- **Color suggestion safety**: Ensure automatic fixes respect brand palettes (optional constraint list); provide undo.

---

## 6) Appendix

### A) Reference plugins & resources
- **Figma built-in Color Contrast Checker** (baseline behavior)
- **Stark** — accessibility suite (contrast, vision sim, more)
- **Able** — quick layer-to-layer contrast checks
- **Contrast (WillowTree)** — popular free plugin overview
- **A11y Contrast Checker (how-to video)** — scanning & pass/fail flow
- **Figma Plugin Quickstart & API** — official docs
- **Plugin Manifest spec** — required fields & options
- **Community publishing** — process & permissions; review guidelines
- **create-figma-plugin (quick start)** — bundling/scaffolding tool

### B) Glossary (for non-designers)
- **Figma Plugin**: A small app that runs inside Figma’s editor to read/modify file contents via the Plugin API.
- **manifest.json**: Metadata file declaring plugin name, entry points, UI, permissions.
- **WCAG**: Web Content Accessibility Guidelines—contrast thresholds (AA/AAA) for legibility.
- **AA/AAA**: Conformance levels (AAA is stricter).
- **Node / Layer**: Objects in the Figma document (e.g., frames, text, rectangles).
- **Release**: Versioned build attached to a GitHub tag.

### C) Example artifacts (Codex-generated)

**package.json (scripts)**
```json
{
  "scripts": {
    "dev": "esbuild src/code.ts --bundle --outfile=dist/code.js --watch & esbuild src/ui/ui.tsx --bundle --outfile=dist/ui.js --watch && http-server dist",
    "build": "node scripts/build.js",
    "test": "vitest run",
    "package": "node scripts/package.js"
  }
}
```

**GitHub Action**
```yaml
name: build
on:
  push: { branches: [ main ] }
  pull_request:
jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 'lts/*', cache: 'npm' }
      - run: npm ci
      - run: npm test
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with: { name: figma-a11y-contrast-dist, path: dist/ }
```

**manifest.json (minimal)**
```json
{
  "name": "A11y Contrast Checker (MVP)",
  "id": "com.yourorg.a11y-contrast",
  "api": "1.0.0",
  "main": "dist/code.js",
  "ui": "dist/ui.html",
  "editorType": ["figma", "figjam"],
  "permissions": [],
  "relaunchButtons": [{ "command": "recheck", "name": "Re-check contrast" }]
}
```

---

## 🔌 What Atlas does vs. what Codex does

- **Atlas**
  - Finds docs, examples, and comparable plugins; collects requirements into `/docs/assumptions.md`.
  - Creates GitHub repo, labels, issue/PR templates; opens PRs; manages releases via web UI.
  - Walks you through Figma **desktop** submission steps that require UI (cannot be fully automated).

- **Codex**
  - Generates all code: manifest, engine, UI, tests, build scripts.
  - Writes GitHub Actions for build/test/release; produces zipped artifacts.
  - Iterates on bugs via PR diffs until CI is green.

---

## 🚧 Guardrails & Assumptions

- **Unavoidable manual touchpoints**: Final **Publish** flow happens in the Figma desktop app and undergoes human review. Expect to click through forms and upload assets.
- **Assumptions**:
  - We target Figma Design editor first (FigJam supported where feasible).
  - We use sRGB contrast math consistent with WCAG; no external network calls.
  - We differentiate from native contrast checks via **batch scan**, **sortable report**, and **one-click fix**.

---

## One-Command Flow (you trigger; agents do the rest)

1) “**Atlas, create repo and open a PR scaffolding CI for a Figma plugin**.”
2) “**Codex, generate the plugin (TypeScript + React UI) that scans text layers, computes WCAG ratios, and suggests fixes. Push to the open PR.**”
3) “**Codex, add tests for color math and thresholds; ensure CI passes.**”
4) “**Atlas, create a versioned release; attach build artifact.**”
5) “**Atlas, guide me through Figma desktop to Import from manifest, test, and Publish to Community.**”

---

If you want, I can turn this into a live GitHub issue board with pre-filled tasks next.





## You (2025-11-08T19:29:33.222000+00:00)

Thinking like a product manager, and responsibly document all this in notion. Think through the folder and file structure, figure out the different pages you need to build out and document everything.









































## ChatGPT (2025-11-08T19:31:21.379319+00:00)

Here’s a well‑structured Notion‑ready document capturing the entire plan with clear page hierarchy and full content for each section. You can import it into your Notion workspace or copy the page hierarchy and content manually.

{{file:file-VyjFy6bZpQ2ZF38HT5h9GB}}

## You (2025-11-08T19:35:49.561000+00:00)

Can you take over this window and document your plan by creating the necessary notion pages





































## ChatGPT (2025-11-08T19:36:46.949801+00:00)

I navigated to Notion in the browser to create the requested pages, but the site was unreachable due to a network issue (ERR_TUNNEL_CONNECTION_FAILED)【15329204262356†screenshot】. Without access to Notion through the browser and with only read‑only Notion API endpoints available, I’m unable to create the pages directly.

I’ve prepared a comprehensive Notion‑compatible document with all the planned sections and hierarchy. You can import this document into your Notion workspace to create the pages manually. Here’s the file again for your convenience:


Once you have access to Notion, create a top‑level page titled “A11y Contrast Checker Plugin Project” and add each of the sub‑pages (Overview, Execution Plan, Repository Architecture, Deployment & DevOps, Risks & Limitations, Appendix) as outlined in the document. This will give you a well‑organized knowledge base for managing the project.



## You (2025-11-08T19:37:28.605000+00:00)

Take over the current window i have opened. and complete the steps









## ChatGPT (2025-11-08T19:37:52.224584+00:00)

It looks like Notion is prompting for login. Please log in to your Notion account in the open window, and let me know once you’re logged in so I can proceed with creating the pages.



## You (2025-11-08T20:12:24.347000+00:00)

I took control of the virtual browser. If you're unsure what changed, ask for more context. If the task is complete, just acknowledge and wrap it up. Otherwise, please proceed.

## You (2025-11-08T20:13:52.383000+00:00)

execute phase 0 using the tools available at your disposal
