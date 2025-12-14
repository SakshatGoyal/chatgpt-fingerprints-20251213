# Handover notes and next steps

## You (2025-11-08T15:39:38.058901+00:00)

I'm documenting my activities so far for your context.

---

Here’s a clean hand-off you can paste into a team doc. It’s written in first-person so the next crew can pick up exactly where we stopped.

Figma MCP Server × ChatGPT — Handover Notes

1) My goal

My goal was to let ChatGPT safely “see and act on” my Figma content by running a small local app (an MCP server) on my Mac. This server exposes a few tools (like “who am I?”, “get file summary”, etc.) that ChatGPT—or a tester UI called MCP Inspector—can call. Later, I planned to add write-actions (comments/tokens now; canvas edits via a plugin later).

⸻

2) What I actually built
	•	A TypeScript MCP server called figma-mcp that:
	•	Runs over STDIO (for MCP Inspector) and HTTP /mcp (for ChatGPT Connectors).
	•	Implements tools:
	•	ping → health check
	•	env_check → confirms the Figma token is loaded (masked)
	•	figma_whoami → verifies token by calling GET /v1/me (US→EU fallback, timeouts, error clarity)
	•	figma_get_file → fetches Figma file data with modes:
	•	summary (default): name + page list with IDs and counts (small)
	•	page: one page via /nodes?ids=…
	•	nodes: specific nodes via /nodes?ids=…
	•	full: whole file; optionally saveToFile:true writes to /tmp/figma-<key>-<ts>.json to avoid huge responses
	•	Handles US/EU data-residency fallback, timeouts, and clean errors.
	•	Never prints to STDOUT (only STDERR). This is critical for STDIO MCP.

⸻

3) The environment on my Mac
	•	MacBook Pro (M3 Pro), macOS Sequoia 15.7.1
	•	Node + npm, TypeScript, tsx
	•	Project deps (key ones): @modelcontextprotocol/sdk, express, undici, zod, @types/express
	•	Folder: ~/figma-mcp

⸻

4) Tokens & secrets (how I handled them)
	•	.env lives at ~/figma-mcp/.env and contains exactly:

FIGMA_TOKEN=figd_...   # Personal Access Token from Figma Settings → Security


	•	I removed dotenv.config() because it printed a banner to STDOUT (breaks STDIO).
Instead, index.ts manually reads .env (silent), sets process.env.FIGMA_TOKEN, and all tools read it via a helper (getToken()).
	•	Do not put your token in Inspector UI; let the server read .env.
	•	Ensure .gitignore includes .env.

⸻

5) How it works (mental model)
	•	MCP server = a local mini-API with named “tools”.
	•	Inspector = a browser UI to test tools over STDIO (no ChatGPT needed).
	•	HTTP /mcp = the same server exposed as an HTTP endpoint so ChatGPT Connectors can call it.
	•	For internet access, I use ngrok to map http://localhost:3000/mcp → https://*.ngrok.app/mcp.

⸻

6) What I did on the machine (chronology, compressed)
	1.	Created ~/figma-mcp, initialized npm, installed SDK + libs, added TypeScript & tsx.
	2.	Implemented index.ts with:
	•	MCP server setup
	•	Tools: ping, env_check, figma_whoami, figma_get_file (modes)
	•	Silent .env loader (no STDOUT noise)
	•	STDIO bootstrap for Inspector
	•	Express server + StreamableHTTPServerTransport at POST /mcp for ChatGPT
	3.	Fixed common gotchas:
	•	.env not loaded (Inspector CWD) → Load file relative to index.ts.
	•	dotenv banner → removed dotenv.config(), manual file read only.
	•	Token invalid → regenerate PAT; avoid Inspector env override.
	•	EU region → try api.figma.com then api.eu.figma.com.
	•	Huge files → use summary or saveToFile:true to avoid UI/proxy limits.
	4.	Verified:
	•	env_check says token present
	•	figma_whoami returns my Figma user JSON
	•	figma_get_file works on a simple file; for heavy files, summary/page/nodes or full + saveToFile:true.

⸻

7) Value proposition (what this system can do now)
	•	Read/analyze Figma files at scale and return structured info for ChatGPT to reason about.
	•	Post-MVP “actions” without plugins:
	•	Comments (via Figma REST)—easy to add as a new tool.
	•	Variables (design tokens) create/update/delete—also addable via REST.
	•	What it cannot do via REST: live canvas edits. That needs a Figma Plugin. The intended path is: MCP analyzes → produces a “patch JSON” → small plugin applies edits inside Figma.

⸻

8) How to run it again (single-screen cheat sheet)

Start the server (STDIO + HTTP)

cd ~/figma-mcp
npm install
npm i -D @types/express
# Ensure .env has:
# FIGMA_TOKEN=figd_...

npm run dev
# Expect on STDERR:
# [figma-mcp] Starting MCP server on stdio…
# [figma-mcp] env: FIGMA_TOKEN present
# [figma-mcp] HTTP MCP ready at http://localhost:3000/mcp

Open Inspector (tests without ChatGPT)

# In a new Terminal tab
cd ~/figma-mcp
npx @modelcontextprotocol/inspector stdio -- node ./node_modules/.bin/tsx src/index.ts
# In the browser: Connect → Tools:
# 1) env_check     → should say “present”
# 2) figma_whoami  → should show Figma user JSON
# 3) figma_get_file (input):
#    { "fileKey": "XXXXX", "mode": "summary" }

Expose HTTP for ChatGPT (ngrok)

brew install ngrok/ngrok/ngrok        # one-time
ngrok config add-authtoken <YOUR_TOKEN>  # one-time
ngrok http 3000
# Copy: https://<random>.ngrok.app/mcp

In ChatGPT: Settings → Connectors → Create → name it (e.g., “Figma MCP”) → URL = https://<random>.ngrok.app/mcp.
In a chat, pick the connector and ask it to run one of the tools.

⸻

9) Troubleshooting I already hit (and fixes)
	•	Inspector shows “Connection Error” / JSON parse errors
Cause: something printed to STDOUT (e.g., dotenv banner).
Fix: all logs to STDERR only; manual .env read; no dotenv.config().
	•	“Invalid token” from Figma
Causes: revoked/expired token; copied with trailing space; wrong Figma account.
Fix: regenerate PAT, paste cleanly in .env. Use env_check then figma_whoami.
Optional: curl -H "X-Figma-Token: $FIGMA_TOKEN" https://api.figma.com/v1/me.
	•	404 Not Found on files
Cause: wrong key or wrong region.
Fix: copy exact key from URL; try again; our code already tries US→EU.
	•	Big files time out / UI chokes
Fix: use { "mode": "summary" } or { "mode": "full", "saveToFile": true }, or fetch page/nodes.
	•	Port 3000 busy
Fix: kill $(lsof -ti :3000) 2>/dev/null || true

⸻

10) Security notes
	•	.env must be local only, never committed. Add .env to .gitignore.
	•	Never paste tokens in chat or screenshots. Use env_check to verify presence without revealing.

⸻


⸻

12) Quick command reference (copy/paste)

# Project folder
cd ~/figma-mcp

# Install deps safely (repeatable)
npm install
npm i -D @types/express

# Start server (STDIO + HTTP :3000)
npm run dev

# Inspector (prefilled)
npx @modelcontextprotocol/inspector stdio -- node ./node_modules/.bin/tsx src/index.ts

# Tunnel to the internet (for ChatGPT)
ngrok http 3000

# Token sanity (shell)
export $(grep FIGMA_TOKEN .env)
curl -s -H "X-Figma-Token: $FIGMA_TOKEN" https://api.figma.com/v1/me | python -m json.tool


⸻

13) Appendix — What lives where
	•	~/figma-mcp/.env → FIGMA_TOKEN=figd_…
	•	~/figma-mcp/src/index.ts → server entry:
	•	Tool registrations
	•	Silent .env loader
	•	STDIO transport
	•	Express HTTP /mcp transport

⸻

14) Final state summary (so the next team knows)
	•	Local server runs; Inspector connects; tools respond.
	•	HTTP /mcp endpoint is live on port 3000 for Connectors.
	•	Token handling is robust (file-relative, silent, override-proof).
	•	Heavy file handling has modes and saveToFile to prevent timeouts.
	•	Clear path to actions (comments/variables) and true edits via plugin.

If anything’s unclear, the fastest end-to-end verification is:
npm run dev → npx @modelcontextprotocol/inspector … → run env_check, figma_whoami, and figma_get_file with mode:"summary".

## ChatGPT (2025-11-08T15:39:39.983559+00:00)

Perfectly written hand-off — clear, complete, and production-ready.

Here’s what you could add at the very end (Section 15) to make it fully “handover-proof” for the next engineer or researcher picking it up later:

---

**15) Suggested Next Steps (for whoever continues)**
1. **Add write-tools** — start with:
   • `figma_post_comment` → POST `/v1/files/{file_key}/comments`
   • `figma_manage_variables` → CRUD via `/v1/variables` endpoints.
2. **Add schema validation** — use `zod` to strictly type each tool’s input/output.
3. **Automate region fallback** — abstract API base URL selection into a helper.
4. **Integrate plugin bridge** — small Figma Plugin that listens for `patch.json` from MCP and applies edits.
5. **Package for npm** — rename to `@yourorg/figma-mcp`, include a README + type declarations.
6. **Connector test plan** — document exact ChatGPT Connector payloads + sample responses.
7. **Security review** — check token handling, logging, and output redaction.
8. **Version bump & changelog** — mark this build as `v0.1.0` (MVP, read-only).

---

Would you like me to turn this whole hand-off (with the new Section 15) into a clean markdown README.md so it can live in your repo’s root folder?
