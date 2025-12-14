# Palo Alto Networks UI Design

## You (2025-05-07T02:11:42.771000+00:00)

You are a prompt engineer creating a Bolt prompt that converts the following product requirements document (PRD) into a UI design customized for Palo Alto Networks.

Your task is to generate a Bolt-ready prompt that:

> 1. **Preserves the original PRD’s layout, component logic, and persona context.**
> 2. **Transforms the PRD content into a Palo Alto Networks–specific version** using real or plausible product-level telemetry, terminology, and UI style conventions from PAN’s platforms (e.g., Cortex XSOAR, Prisma Access, Panorama, Cortex Data Lake).

In the output, Bolt should be guided to:

> * Retain section headers, structure, and roles from the original PRD.
> * Modify metrics, actions, and AI insights to use Palo Alto Networks–style telemetry (e.g., threat log volumes, policy misalignment, deployment lag across zones).
> * Adapt UI elements (cards, dashboards, panels) to match PAN’s visual grammar:
>
>   * Blue-gray UI palette (not corporate yellow/orange).
>   * Modular card layout with clear hierarchy and high data density.
>   * Collapsible side navigation and timeline elements as used in PAN tools.
> * Use PAN-specific microcopy and interface language (e.g., “Security Posture Drift”, “Playbook Invocation via XSOAR”, “Adoption Lag: Config vs. Runtime Delta”).

Format the output as a **prompt** ready to be pasted into Bolt, not as a rewritten PRD.

 Be direct, structured, and use clear language that Bolt can interpret to generate UI.

 ---

# 🧾 Product Requirements Document

### Title: *CSM Portfolio View – Customer Health Overview*

**Codename:** "Portfolio Lens"

---

## 1. 📌 Executive Summary

This view is the **default landing screen** for Customer Success Managers. It presents an aggregated, ranked, and filterable summary of **all accounts assigned to them**, organized by **risk, opportunity, and lifecycle stage**.

Its purpose is to:

* Prioritize attention
* Surface patterns
* Speed up decision-making
* Provide clear entry points into individual account dashboards

---

## 2. 🧑‍💼 Target User: Customer Success Manager (CSM)

### Core Needs:

* See **which accounts need attention today**
* Identify **renewal risks** or opportunity upsides across the book
* Quickly scan **adoption progress** and **deployment friction**
* Jump directly into customer-specific dashboards from a central location

---

## 3. 🎯 User Goals & Scenarios

| Scenario            | Goal                                                        |
| ------------------- | ----------------------------------------------------------- |
| Daily standup       | See top 5 “at-risk” accounts at a glance                    |
| QBR prep            | Filter for accounts with low sentiment but upcoming renewal |
| Value tracking      | View which customers have hit ROI milestones                |
| Adoption triage     | Identify accounts stuck in onboarding or with config drift  |
| Executive reporting | Export health summary of entire book by segment or region   |

---

## 4. 🖥️ Dashboard Overview

### Page Layout Zones:

| Section                        | Description                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------ |
| **Portfolio Header**           | Summary stats: # of accounts, average health score, % at risk, total renewals this quarter       |
| **Filters & Sorting**          | Segment (Enterprise/Commercial), Health Status, Renewal Window, Product Deployed                 |
| **Accounts Table / Grid**      | Each row is an account with key metrics                                                          |
| **Saved Views**                | Pre-filtered templates (e.g., “Upcoming Renewals,” “At-Risk Accounts,” “Onboarding in Progress”) |
| **Bulk Actions**               | Trigger emails, schedule reviews, assign playbooks                                               |
| **Navigation to Account View** | Click-to-drill into full CSM dashboard for that account                                          |

---

## 5. 🔢 Accounts Table: Row-Level Detail

Each row contains:

| Field                  | Description                                         |
| ---------------------- | --------------------------------------------------- |
| **Account Name**       | With logo + industry segment                        |
| **CSM Owner**          | (if multiple books are visible)                     |
| **Lifecycle Stage**    | Onboarding / Steady State / Expansion / Renewal     |
| **Health Score**       | RAG color, numerical score, hover shows sub-metrics |
| **Adoption Trend**     | Sparkline or % change week-over-week                |
| **Deployment Lag**     | # of days behind schedule                           |
| **Customer Sentiment** | NPS score or qualitative tag                        |
| **Next Engagement**    | Scheduled QBR, renewal call, etc.                   |

---

## 6. 🤖 AI Integration

AI is used to:

* **Auto-prioritize view**: sort top 5 at-risk accounts
* **Generate insight previews** inline in each row (e.g., “Policy drift in Cortex XDR”)
* **Recommend grouped actions** for similar accounts (e.g., “4 accounts show Adoption Lag—trigger playbook”)
* Allow tagging accounts as “Watchlist” based on AI-projected churn probability

---

## 7. 🛠️ Functional Requirements

| Feature                         | Description                                                | Priority |
| ------------------------------- | ---------------------------------------------------------- | -------- |
| Account-level sorting/filtering | By health, product, lifecycle, sentiment, etc.             | High     |
| Portfolio health overview       | KPIs above the fold (total accounts, avg score, # at risk) | High     |
| Inline alerts                   | Flag adoption or deployment issues within the table        | Medium   |
| Bulk action menu                | Trigger templated actions for multiple accounts            | Medium   |
| Saveable filters/views          | Create quick-access filtered views                         | Medium   |
| Drill-down navigation           | Click account name to jump to full CSM dashboard           | High     |

---

## 8. 🧪 Success Metrics

* % CSMs who use this view daily
* Reduction in time-to-engagement for flagged at-risk accounts
* Increase in proactive outreach (playbooks triggered from portfolio view)
* Improved renewal forecasting accuracy (via AI insight usage)

---

## 9. 🧭 Design Principles

* **Default to action**: Don’t just report—guide.
* **Make risk obvious**: Color, hierarchy, motion should direc.
* **Respect scale**: Work well for 10 accounts or 150.
* **Let the CSM own their book**: Prioritize customization and filtering.
* **Support the zoom**: Fast from 10,000 feet → ground level.

## ChatGPT (2025-05-07T02:11:44.464213+00:00)

Here's a direct, structured Bolt-ready prompt for generating a Palo Alto Networks-specific UI from the provided PRD:



## ChatGPT (2025-05-07T02:12:50.768620+00:00)

Your Bolt-ready prompt has been created. Let me know if you need further refinements!
