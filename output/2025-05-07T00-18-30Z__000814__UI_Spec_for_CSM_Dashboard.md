# UI Spec for CSM Dashboard

## You (2025-05-07T00:18:30.230000+00:00)

You are a product UI designer at Palo Alto Networks. Your task is to adapt the following dashboard PRD into a UI that matches the structure, logic, and functionality described—but transforms its terminology, telemetry references, and visual system to align with Palo Alto Networks products (such as Cortex XSOAR, Prisma Access, or Panorama).
Guidelines:
Do not change the structure or persona defined in the PRD. Preserve layout, sections, and original intent.
Modify metrics, AI references, and telemetry to match Palo Alto Networks’ data sources (e.g., Cortex Data Lake, PAN-OS telemetry).
Style the dashboard using the visual patterns of PAN products: modular card layout, collapsible navigation, blue-gray palette, alert accents, and dense information displays.
Use realistic UI text and terminology used in PAN products—avoid brand copy, stick to technical product semantics.
Return a structured UI spec including:
Modular components and layout (sectioned by the PRD)
Telemetry references customized to PAN products
Visual theming instructions (color, hierarchy, component styles)
Here is the PRD to adapt:

### Title: Unified Dashboard – Customer Success Manager (CSM) View

**Codename:** *Command View CSM*

---

## 1. 📌 Executive Summary

This dashboard is a modular, role-aware workspace for CSMs to monitor and act on customer health across technical, deployment, adoption, and value dimensions. It reuses shared components with the SC dashboard to support design scalability, but adapts them with **context-specific insights and workflows** for post-sale action.

---

## 2. 🧑‍💼 Target User: Customer Success Manager (CSM)

### Core Needs:

- Real-time health visibility across customer accounts.
- Clear, prescriptive signals on where to intervene.
- Shared understanding of customer progress aligned to pre-sale expectations.
- Frictionless collaboration with AEs, SCs, and support.
- Evidence-based guidance (via telemetry + AI) for renewals and expansions.

---

## 3. 🎯 Cross-Persona Platform Goals

| Goal | Description |
| --- | --- |
| **Component Reuse** | Dashboard uses common cards (Health, Timeline, AI Nudges, Quick Actions) shared with SC dashboard. |
| **Visual and Interaction Consistency** | CSM and SC see the same data types visualized similarly—only context and actions differ. |
| **Integrated Narrative** | Shared “Customer Storyline” from POV to Renewal, visible through timeline and linked artifacts. |

---

## 4. 🖥️ Dashboard Layout Overview (Shared + Specialized)

| **Section** | **Shared UI Component** | **CSM-Specific Adaptation** |
| --- | --- | --- |
| **Header** | Account Overview | Renewal date, current lifecycle stage, assigned CSM, overall health status. |
| **Health Summary Cards** | Modular health indicators | Emphasizes: Adoption, Deployment TTV, Technical Health, Sentiment. |
| **Timeline** | Event stream | Highlights onboarding, adoption milestones, escalations, QBRs. |
| **AI Insights Panel** | Nudges & Recommendations | Focused on churn risk, delayed adoption, renewal blockers. |
| **Quick Actions** | Prescriptive Playbooks | "Trigger Adoption Playbook", "Escalate to SC", "Request Support Artifact". |
| **Linked Artifacts** | DoR / Success Plan access | Allows retrospective alignment: “Is what we’re delivering what was sold?” |

---

## 5. 🤖 AI Integration Strategy

### Philosophy:

- **Transparency over prescriptive automation**
- **Assistive AI** that surfaces actions, not decisions

### Capabilities:

- Predicts churn risk based on trend deviations.
- Identifies outlier accounts based on segment baselines.
- Suggests proven playbooks for similar accounts at risk.
- Surfaces success stories of interventions that worked.

> ✳️ Note: Same underlying AI model used in SC dashboard, but prompts + outputs adapted for post-sale focus.
> 

---

## 6. 🛠️ Functional Requirements

| Feature | Description | Priority |
| --- | --- | --- |
| Modular Health Cards | Visual status for Technical, Deployment, Adoption, Sentiment. | High |
| Timeline | Customer journey milestones with engagement markers. | High |
| AI Nudges | Risk insights + suggested interventions. | High |
| Playbook Actions | Launches pre-defined workflows (via SFDC integration or internal systems). | High |
| Artifact Access | Read-only view of Design of Record, Success Plan, Product Configs. | Medium |
| Salesforce Contextual View | Can embed in SFDC account detail page. | High |

---

## 7. 🧪 Success Metrics

- Reduction in surprise churn or escalations.
- Increase in proactive interventions (playbooks triggered).
- Higher CSM satisfaction with visibility and insight.
- Alignment with SC-created expectations.

---

## 8. 🧭 Design Principles

- **Same Structure, Different Story**: Keep UI skeletal structure aligned with SC dashboard.
- **Persona-Based Semantics**: A red Adoption Card means something different to a CSM (risk) than to an SC (missed alignment).
- **Assisted Action, Not Automation**: AI never hides the “why” behind a nudge.
- **Low Friction, High Signal**: Information density is high, but cognitive load is light.

## ChatGPT (2025-05-07T00:18:42.785615+00:00)

{"content_type": "thoughts", "thoughts": [{"summary": "Adapting PRD for PAN UI", "content": "I need to adapt the PRD for Palo Alto Networks, focusing on modular UI components and layout customized to their products. Typical product names like Cortex XSOAR, Prisma Access, and Panorama will be referenced, along with telemetry terms like Cortex Data Lake and AIOps. For the CSM dashboard, the \"Customer Health Score\" can be derived from firewall status, threat prevention, and risk analysis. I'll also mention \"Application Adoption,\" perhaps highlighting threat prevention usage or DNS Security adoption.", "chunks": [], "finished": true}], "source_analysis_msg_id": "f3ac342b-3a5f-4607-9fe2-a8fb275c6da6"}

## ChatGPT (2025-05-07T00:18:46.869124+00:00)

{"content_type": "reasoning_recap", "content": "Thought for 11 seconds"}

## ChatGPT (2025-05-07T00:18:30.911464+00:00)

### Palo Alto Networks — “Command View CSM” UI Spec  
*(adapted from the original PRD without altering structure or intent)*  

---

## 1. Modular Components & Layout  

| Section (per PRD) | PAN-Aligned Component | Key Fields / Interactions | Data Source(s) |
| --- | --- | --- | --- |
| **Header** | **Account Banner** (fixed top bar) | • Tenant Name • Renewal Date • Lifecycle Stage (Onboarding ▶ Adoption ▶ Value ▶ Renewal) • Assigned CSM • **Overall Health Score** (rolling 90-day composite)<br>Health chip colors: ✓ Green ≥ 80, ⚠️ Yellow 60-79, 🛑 Red < 60 | Cortex Data Lake (CDL) aggregated scores; Customer Success Salesforce object |
| **Health Summary Cards** (4-up, responsive) | **Technical Health** | • Device Up/Down • PAN-OS Patch Compliance • High Availability status | AIOps for NGFW, Panorama APIs |
|  | **Deployment Velocity** | • Time-to-Value (first log ▶ first block) • Policy Commit Frequency | Panorama, Prisma Access Insights |
|  | **Adoption** | • % of Licenses Activated (e.g., DNS Security, Advanced URL Filtering) • Active Users vs Seats | CSP Licensing APIs |
|  | **Sentiment** | • NPS from in-product survey • Recent Support CSAT | Qualtrics feed, Salesforce |
| **Timeline** | **Customer Journey Stream** (scroll / filter) | Event pills grouped by stage:<br>• “Firewall First Log Received” • “First Policy Commit” • “QBR Completed” • “P1 Case Opened / Resolved” | CDL event bus, Salesforce milestones |
| **AI Insights Panel** (right drawer) | **AIOps Nudges** | • “Churn Risk ↑ 12% — Drivers: Low Adoption, Unpatched NGFWs” • “Recommend ‘DNS Security Activation’ playbook” | AIOps predictive model (same engine as SC view; CSM-tuned prompt set) |
| **Quick Actions** | **Playbook Launcher** (button row) | • Trigger Adoption Playbook • Escalate to SC • Request Support Artifact | XSOAR playbook APIs, Salesforce Flow |
| **Linked Artifacts** | **Success Plan & DoR Viewer** | Read-only PDFs / Confluence links with hash-based deep links | Confluence, Salesforce Files |

---

## 2. Telemetry Mapping to PAN Products  

| PRD Metric | PAN Signal | Collection Path |
| --- | --- | --- |
| Technical Health | Device Health Score, Software Version Drift, Critical Alarms | AIOps for NGFW / Prisma Access Insights |
| Deployment Velocity | `first_log_timestamp`, `first_block_timestamp`, commit deltas | Cortex Data Lake → Panorama API |
| Adoption | Feature entitlement vs usage (e.g., `dns_sec_enabled` flag) | CSP Entitlement API + CDL usage logs |
| Sentiment | `nps_score`, `csat_rating` | Qualtrics export, Salesforce Service Cloud |
| AI Churn Risk | AIOps ML model with CSM persona prompt: `account_churn_score` | AIOps inference endpoint |
| Playbook Triggers | XSOAR incident type `customer_health_playbook` | XSOAR REST API |

---

## 3. Visual Theming & Interaction Guidelines  

| Aspect | PAN Convention | Spec |
| --- | --- | --- |
| **Palette** | Blue-gray neutrals with severity accents | `#0F2135` (bg-dark), `#1F3B5B` (card header), `#E8EEF4` (card bg), Severity: Critical `#E01E1E`, High `#FF7D00`, Medium `#FFB400`, Low `#00BFA5` |
| **Typography** | Strata Sans (16 / 14 / 12 px) | H1 16 px bold, Body 14 px, Caption 12 px |
| **Layout** | 12-col grid; cards min-width = 4 cols | Cards stack on ≤ 1280 px; Insights drawer collapsible |
| **Navigation** | Left collapsible nav (Panorama style) | Icons + labels; sticky at 64 px |
| **Cards** | Dense info, hover reveals detail | Use inline sparkline (CDL trend), status chip right-aligned |
| **Alerts** | Inline chip in card header; toast on major risk | Chip colors follow severity palette |
| **AI Explainability** | “Why this nudge?” link opens side panel with top 3 contributing signals | Required for every AI insight |
| **Accessibility** | WCAG 2.1 AA; keyboard nav in Timeline | Focus ring `#249CF2` |

---

## 4. Component States & Microcopy Examples  

- **Adoption Card (green):** “87 % of licensed features active — keep momentum.”  
- **Adoption Card (red):** “DNS Security inactive on all NGFWs. Risk to renewal.”  
- **AI Nudge:** “Churn risk increased by 12 %. Similar accounts saw 18 % improvement after enabling Advanced URL Filtering. → Run ‘URL-F Adoption’ playbook.”  
- **Playbook Toast Success:** “Playbook triggered in XSOAR. Track progress in Incident #43702.”  

---

## 5. Interaction Flow Highlights  

1. **CSM opens tenant dash →** Header shows health = Red, Renewal in 45 days.  
2. **AI Panel auto-opens** with churn risk nudge.  
3. **Click “Run playbook” →** Quick Actions fires XSOAR workflow; toast confirmation.  
4. **Timeline auto-filters** to show last 90 days; user expands “Escalation Resolved” to read RCA.  
5. **Linked Artifact click** opens Success Plan in modal for comparison to sold scope.

---

## 6. KPI Instrumentation (for Success Metrics section)

- `surprise_churn_count` (CDS)  
- `playbook_triggered_count` (XSOAR)  
- `csm_dash_daily_active` (CDL + UI telemetry)  
- `expectation_alignment_score` (text diff of DoR vs Success Plan; AIOps NLP)

---

**End of UI Spec**

