# Product detail document

## You (2025-12-03T17:37:52.340000+00:00)

Review these design mockups and create a complete product detail document that captures the following.

1. Each page name
2. the content that each page contains; all the differrent metrics, tables, charts, views, etc...
3. what each page is trying to communicate

----
for your context, this is an internal platform for a customer success team at Palo Alto Networks.  This evaluates a single customer's account health from different lenses.



## ChatGPT (2025-12-03T17:38:30.204041+00:00)

from PIL import Image, ImageOps, ImageFilter, ImageEnhance, ImageStat, ImageChops, ImageFont
import matplotlib.pyplot as plt

paths = [
"/mnt/data/7777c453-a54f-47eb-8d5a-25151da7befd.png",
"/mnt/data/b9328cad-9df5-4d92-9660-d9086bbbeeef.png",
"/mnt/data/678bfb1e-e8d0-4e71-9573-8a66180f95de.png",
"/mnt/data/89c0c89b-dd76-42c7-ad9a-31eda84ec060.png",
"/mnt/data/57f2b4d5-16cb-45f3-b886-009aebc9c3b9.png",
"/mnt/data/5e85ac12-404a-41b6-95bc-08b86bb4a6c1.png",
"/mnt/data/ea934a8e-e10a-4ceb-a3b7-312fe5179dac.png"
]
len(paths)

## ChatGPT (2025-12-03T17:38:52.530764+00:00)

fig, axes = plt.subplots(len(paths), 1, figsize=(6, 30))
for ax, p in zip(axes, paths):
    img = Image.open(p)
    ax.imshow(img)
    ax.axis('off')
    ax.set_title(p.split('/')[-1])
plt.tight_layout()



## ChatGPT (2025-12-03T17:39:17.400432+00:00)

img = Image.open(paths[0])
plt.figure(figsize=(8,6))
plt.imshow(img.crop((0,200,1800,1500)))  # crop central area
plt.axis('off')



## ChatGPT (2025-12-03T17:39:59.233514+00:00)

plt.figure(figsize=(8,6))
plt.imshow(Image.open(paths[0]).crop((0,900,1800,2100)))
plt.axis('off')



## ChatGPT (2025-12-03T17:40:43.908058+00:00)

plt.figure(figsize=(8,7))
plt.imshow(Image.open(paths[1]).crop((0,850,1800,2100)))
plt.axis('off')



## ChatGPT (2025-12-03T17:41:03.725195+00:00)

plt.figure(figsize=(8,7))
plt.imshow(Image.open(paths[1]).crop((0,900,1500,2100)))
plt.axis('off')



## ChatGPT (2025-12-03T17:41:44.609451+00:00)

plt.figure(figsize=(8,7))
plt.imshow(Image.open(paths[2]).crop((0,850,1800,2100)))
plt.axis('off')



## ChatGPT (2025-12-03T17:42:15.843549+00:00)

plt.figure(figsize=(8,7))
plt.imshow(Image.open(paths[3]).crop((0,860,1800,2100)))
plt.axis('off')



## ChatGPT (2025-12-03T17:42:49.139214+00:00)

plt.figure(figsize=(8,7))
plt.imshow(Image.open(paths[4]).crop((0,880,1800,2100)))
plt.axis('off')

## ChatGPT (2025-12-03T17:43:15.585078+00:00)

img4 = Image.open(paths[4])
img4.size

## ChatGPT (2025-12-03T17:43:26.722832+00:00)

plt.figure(figsize=(6,10))
plt.imshow(img4)
plt.axis('off')

## ChatGPT (2025-12-03T17:43:51.114949+00:00)

img5 = Image.open(paths[5])
img5.size

## ChatGPT (2025-12-03T17:44:03.604111+00:00)

plt.figure(figsize=(6,10))
plt.imshow(img5)
plt.axis('off')

## ChatGPT (2025-12-03T17:44:32.560744+00:00)

img6 = Image.open(paths[6])
img6.size



## ChatGPT (2025-12-03T17:44:45.198263+00:00)

plt.figure(figsize=(6,10))
plt.imshow(img6)
plt.axis('off')





## ChatGPT (2025-12-03T17:46:40.837986+00:00)

Here’s a structured product-detail doc based on the mockups, written as if this were a spec you’d hand to PM/Eng.

---

## 0. Common layout & global context (all pages)

All screenshots are different “detail lenses” inside one parent view:

**Top-level frame**

- **Page title / context**
  - Breadcrumb: *Home > Newage Industries*
  - Account name: **Newage Industry**
  - Global metrics:
    - *Open Pipeline (next 12 months)* – dollar amount
    - *TCV* – total contract value
  - Link: **View Account & Service Team**

- **Primary tab set (top of page)**
  - **Account Health Overview** (selected in all mocks)
  - **Account Health Notifications** (not shown in detail here)

- **Global “Account Health” summary card (top left)**
  - Overall **Account Health status**: Critical / At-Risk / Healthy
  - Sub-types:
    - **Technical Health** – status + 12-month trend sparkline
    - **Deployment and Adoption** – status + 12-month trend sparkline

- **Health Insights panel (left sidebar under Account Health)**
  - Narrative bullets, e.g.:
    - Upcoming $10M renewal at risk due to outstanding account health issues.
    - Delayed deployments, configuration issues, MTTR patterns, etc.
  - This gives the CSM a human-readable explanation and recommended focus areas.

- **“Health by Products” table (center)**
  - Columns:
    - Platform (e.g., *PRISMA SASE*, *STRATA*, *CORTEX*)
    - Products (e.g., *Prisma Access, PA Series, CDSS…*)
    - Technical Health status
    - Deployment & Adoption status
    - Open Pipeline (per product)
    - TCV (per product)
    - Next Renewal Date
  - Each row is color-coded by status (Critical, At-Risk, Healthy).

- **“Products by Health” chip row (below table)**
  - Product filter chips:
    - Prisma Access, PA Series, CDSS, VM Series, Cortex XSIAM, Cortex XSOAR
  - Each page below is effectively “this lower panel, scoped to the selected chip + sub-tab.”

- **Right-hand AI assistant panel**
  - Greeting: “Hey, Jason. How can I help you today?”
  - Prompt box with send button.
  - Suggested prompts:
    - Summarize recent changes in this account’s health.
    - What are the key reasons this account is in a ‘Critical’ health, per product?
    - What additional sales context should I be aware of?
    - Create all customer-facing documents for my upcoming meeting.
    - Show me the current success plans and call-to-actions for an account.

These elements frame all the more detailed “pages” below.

---

## Page 1 – Customer Estate: Prisma Access infrastructure & commercial footprint

### Working name
**Customer Estate – Prisma Access Infrastructure & Licensing**

### Content & structures

**Filter / context**

- Product chip: **Prisma Access** selected.
- Sub-tab: **Customer Estate** (within the Prisma Access detail area).

**Panels**

1. **Prisma Access Infrastructure (card)**
   - *Data Plane* – value like `PA-VM-SaaS-10.2.4`
   - *Cloud Services Plugin* – version (e.g., `4.0`)
   - *Panorama* – PAN-OS version (e.g., `PAN-OS-10.2.8`)

2. **Prisma Access Current State Assessment (card)**
   - *Prisma Access License Purchased*:
     - MU (Mobile Users) count
     - RN (Remote Networks) count
   - *Service Connections* – e.g., “All 6 Deployed”
   - *License Expiration* – date

3. **CASB/DLP Current State Assessment (card)**
   - *Prisma Access DLP Add-On Expiration* – date
   - *Data Security for SaaS (CASB) Application* – expiration date or state

4. **Purchase Data Information (table)**
   - Columns:
     - Product Code (e.g., `PAN-PRISMA-ACCESS-MU-LCL-ENTERPRISE`)
     - Product Name
     - Purchase Date
     - Quantity
     - Term Start Date
     - Term End Date
     - Term (months)
   - Rows enumerate all Prisma Access SKUs purchased.

### What this page is trying to communicate

- **What has this customer actually bought and deployed for Prisma Access?**
  - Concrete inventory of infrastructure (versions, components).
  - Commercial commitments (SKUs, quantities, terms).
  - License coverage and expiration risk.
- It gives the CSM a **quick, factual snapshot of estate and entitlements** before talking about adoption or health issues.

---

## Page 2 – Deployment & Adoption: Prisma Access project progress & usage

### Working name
**Deployment & Adoption – Prisma Access (Project “Pit Stops” & Adoption)**

### Content & structures

**Filter / context**

- Product chip: **Prisma Access**.
- Sub-tab: **Deployment and Adoption**.

**Left rail**

1. **Deployment & Adop. Health (card)**
   - Status: Critical / At-Risk / Healthy.
   - 12-month trend sparkline.

2. **Deployment & Adop. Insights (card)**
   - Narrative bullets explaining:
     - Why deployment is at risk (e.g., early activation issues, configuration delays).
     - Evidence (e.g., elevated MTTR, customers pausing deployment).
   - **Recommended Next Steps**:
     - Engage Account Exec and stakeholders.
     - Engage Product team to understand specific roadblocks, etc.

**Main content**

1. **Top deployment summary strip**
   - *Deployment & Adoption Health*: status (Critical).
   - *Professional Services*: overall status (e.g., Active).
   - *Customer Since* (or adoption %): value like **22%**.

2. **Deployment “Pit Stop” timeline**
   - Tabs: *Mobile Users*, *RN*, *RN – Sites*, *PAB* (selected), *Add-Ons*.
   - Pit stops across a time axis:
     - Pit Stop 1: Customer kickoff complete.
     - Pit Stop 2: Technical Planning complete.
     - Pit Stop 3: Environment established.
     - Pit Stop 4: 1st users activated / 50 licenses deployed.
     - Pit Stop 5+: 25%/50%/90% of licenses deployed, etc.
   - For each pit stop:
     - Expected days vs Actual days (e.g., 30 days vs 45 days).
     - Visual markers showing schedule slippage.
   - Status text under the timeline: e.g., “Deployment is on track” or “Deployment is on pause.”

3. **Adoption chart**
   - Metrics summary above chart:
     - *Units Purchased* – e.g., 20,000.
     - *Total Adoption* – e.g., 22%.
   - Line chart with:
     - X-axis: time (months, last 12 months).
     - Y-axis: “Deployment Adoption (%)” or similar.
     - Vertical marker for “5,000 Licenses Purchased.”
     - Primary line: actual adoption trajectory.

4. **Professional Services Engagement table**
   - Columns:
     - Project Type (e.g., Consulting)
     - Project Manager
     - Consultant
     - Partner (e.g., Deloitte)
     - Track Status (e.g., *On Hold*, *In Progress*)
     - Project End Date
   - Collapsible section: **Current Adoption** (likely breakdown by region / segment).

### What this page is trying to communicate

- **Is the Prisma Access deployment actually getting implemented and used, and where is it stuck?**
  - Timeline shows **implementation progress vs expected schedule.**
  - Adoption chart shows **license consumption vs purchased capacity.**
  - Insights + PS table show **who is responsible** and **what actions are underway**.
- For a CSM, this page answers:
  - “Are we behind or on track?”
  - “What are the specific deployment bottlenecks?”
  - “How much of what they bought are they really using?”

---

## Page 3 – Technical Health: Prisma Access incidents & case list

### Working name
**Technical Health – Prisma Access (Case Reports View)**

### Content & structures

**Filter / context**

- Product chip: **Prisma Access**.
- Sub-tab: **Technical Health**.
- Sub-toggle: **Reports** (vs Trends).

**Left rail**

1. **Technical Health (card)**
   - Status: e.g., **Critical**.
   - 12-month trend sparkline.

2. **Technical Health Insights (card)**
   - Narrative bullets describing the *most common configuration problems* in Prisma Access, e.g.:
     - Panorama commit / validation issues.
     - GlobalProtect Gateway configuration problems.
     - Certificate changes causing errors.
     - Template configuration issues in Prisma Access.
   - Recommended action: e.g., work with PS to resolve config issues.

**Main metrics row**

- KPI tiles, each with numeric value + status chip:
  - **Incidents** – e.g., 3 (At-Risk).
  - **Critical Case Count (P1)** – e.g., 4 (Critical).
  - **Critical Case MTTR (P1)** – e.g., 7 days (Critical).
  - **High Case MTTR (P2)** – e.g., 4 days (Critical/Healthy).
  - **Open Case Backlog** – e.g., 2 (At-Risk).
  - **Jira % of Cases** – e.g., 3% (Critical).

- Toggle buttons: **Reports** (selected), **Trends**.

**Tables**

1. **Case List (full support ticket list)**
   - Columns:
     - Case Number
     - Created (timestamp)
     - Case Owner
     - Priority (High/Medium/Low)
     - Status (Open/Closed/Researching, etc.)
     - Subject (short description)
   - Row count label (e.g., “Case List (419)”).
   - “View More” link to expand.

2. **Incident List (subset of cases flagged as incidents)**
   - Columns:
     - Incident No.
     - Created
     - Case Owner
     - Priority
     - Status
     - Summary
   - Smaller labeled count, e.g., “Incident List (2)”.

### What this page is trying to communicate

- **How healthy is the product operationally, as seen through support cases?**
  - Are there many critical issues?
  - Are cases resolving quickly or lingering?
  - What patterns exist in the configuration / incident types?
- It’s the **operational “X-ray”** of Prisma Access:
  - For a CSM preparing for a meeting, this explains “why the health is Critical” in concrete ticket terms.
  - It also surfaces which owners and which incidents require follow-up.

---

## Page 4 – Technical Health: Prisma Access trends & KPIs over time

### Working name
**Technical Health – Prisma Access (Trends View)**

### Content & structures

**Filter / context**

- Product chip: **Prisma Access**.
- Sub-tab: **Technical Health**.
- Sub-toggle: **Trends** selected.

**Left rail**

- Same two cards as Page 3:
  - Technical Health status card (with trend).
  - Technical Health Insights narrative.

**Main metrics row**

- Same KPI tiles as in Page 3 for:
  - Incidents
  - Critical Case Count (P1)
  - Critical Case MTTR (P1)
  - High Case MTTR (P2)
  - Open Case Backlog
  - Jira % of Cases

**Trend charts grid**

A set of mini dashboards (each with a status chip):

1. **Total Case Count**
   - Bar chart by month.
   - Label: total cases in last 12 months (e.g., “600 cases”).
   - Status: At-Risk.

2. **Incidents**
   - Bar chart by month.
   - Label: total incident count (e.g., “3 incidents”).
   - Status: Critical.

3. **Critical Case Count (P1)**
   - Bar chart by month.
   - Label: e.g., “4 cases”.
   - Status: Critical.

4. **Critical Case MTTR (P1)**
   - Bar chart for average days to close P1 cases.
   - Label: e.g., “7 days”.
   - Status: Critical.

5. **High Case MTTR (P2)**
   - Bar chart for average P2 MTTR.
   - Label: e.g., “4 days”.
   - Status: Healthy.

6. **Open Case Backlog > 30 days**
   - Bar chart showing count of long-running open cases.
   - Label: e.g., “2 cases”.
   - Status: At-Risk.

7. **Support Cases with Jira Attached (%)**
   - Line chart over time.
   - Label: percentage value (e.g., 3%).
   - Status: Critical.

### What this page is trying to communicate

- **How is technical health trending over time, not just what it looks like today?**
  - Whether case volume is improving or worsening.
  - Whether MTTR and backlog are under control.
  - The maturity of support processes (e.g., Jira linkage).
- This lets the CSM (and TAM/SE) answer:
  - “Are we stabilizing this account or sliding into more risk?”
  - “Which metrics are causing the ‘Critical’ label?”

---

## Page 5 – Customer Estate: Hardware estate & lifecycle + CDSS context

### Working name
**Customer Estate – Hardware Estate & CDSS Context (PA Series-centric)**

*(This page shows a more hardware-oriented view of the estate and overlays CDSS data.)*

### Content & structures

**Filter / context**

- “Products by Health” chip row present; likely **PA Series** selected.
- Sub-tab: **Customer Estate**.

**Top metrics**

1. **Total Devices**
   - Count: e.g., 10,000.

2. **Support status breakdown**
   - Active Support – count.
   - Inactive Support – count.
   - Not Registered – count.

**Devices Lifespan and Support Status (table)**
- Columns:
  - Remaining Days bucket (e.g., `<7 days`, `8–30 days`, `31–90 days`, `91–180 days`, `>180 days`, `Not Available`).
  - For each bucket: counts of:
    - Active
    - Inactive
    - Not Registered
    - Total
- Purpose: highlight devices close to end of support or not covered.

**Secondary tab row under this section**
- Tabs such as:
  - **Support Status by Remaining Days** (selected)
  - Device Generations
  - Model Numbers
  - PAN-OS Version
  - Registered / Not Registered breakdown
- Each tab would swap out the underlying breakdown table / chart.

**CDSS Context (bottom section)**

1. **Device Breakdown table**
   - Rows: segments (Total, ELA, Bundle, A-la-Carte).
   - Columns:
     - Total devices
     - Registered
     - Active Support
     - Inactive Support
     - Checked in to CU server
     - Decryption Enabled
     - Sending PA telemetry

2. **License Utilization Breakdown table**
   - Overall row: “Total”.
   - Columns:
     - License Purchased
     - License Enabled
     - Checked-in to CU Server
     - Basic features in use
     - Eligible for Advanced
     - Advanced features in use
     - Upsell Opportunity
   - Each column further broken out by CDSS module (TP, ATP, URL, AURL, WF, AWF, etc.) with raw counts and percentage in parentheses.

### What this page is trying to communicate

- **What is the customer’s physical / hardware security estate and how healthy is its lifecycle and coverage?**
  - Where are there renewal risks (devices near end of support / EOS/EOL)?
  - Are devices registered and sending telemetry?
  - How are CDSS features licensed vs actually enabled?
- For a CSM, this surfaces:
  - **Lifecycle risk**: devices out of support or near EoL.
  - **Adoption / upsell potential**: advanced features purchased vs enabled vs in use.

---

## Page 6 – Customer Estate: CDSS device & license utilization (product-focused)

### Working name
**Customer Estate – CDSS Estate & License Utilization**

### Content & structures

**Filter / context**

- Product chip: **CDSS** selected.
- Sub-tab: **Customer Estate**.

**Device Breakdown**

- Similar table structure as the “CDSS Context” portion from Page 5, now scoped specifically to the CDSS product:
  - Device counts by:
    - Total
    - Registered
    - Active Support
    - Inactive Support
    - Checked in to CU Server
    - Decryption Enabled
    - Sending PA Telemetry

**License Utilization Breakdown**

- Rich table showing, for CDSS:
  - *License Purchased* per module (TP, ATP, URL, AURL, WF, AWF).
  - *License Enabled* per module.
  - *Checked-in to CU Server* per module.
  - *Basic Features in Use*.
  - *Adv Features in Use*.
  - *Upsell Opportunity* (% and counts).
- Percentages show penetration for each feature set.

*(Visually this page looks very similar to the bottom half of Page 5, but focused as the main content for the CDSS chip.)*

### What this page is trying to communicate

- **For CDSS specifically, are licenses being used as intended, and where is there headroom?**
  - Are purchased licenses actually enabled and checked in?
  - Are basic features turned on, and are advanced features adopted?
  - Where does upsell opportunity exist (unused advanced entitlements)?
- It’s essentially the **“license utilization & opportunity” lens** for the CDSS product.

---

## Page 7 – Deployment & Adoption: CDSS consumption vs HW cap

### Working name
**Deployment & Adoption – CDSS Consumption vs Hardware Cap**

### Content & structures

**Filter / context**

- Product chip: **CDSS** selected.
- Sub-tab: **Deployment and Adoption**.
- Dropdown filter: **Last 12 Months**.

**Left rail**

- **Deployment & Adop. Insights (card)** similar to Prisma Access:
  - Explanation of why deployment is at risk or on track.
  - Recommended next steps.

**Main content**

1. **Deployment and Adoption summary**
   - Headline metrics:
     - **HW Estate Consuming ELA** – number + % of cap (e.g., 28,000 (140%)).
     - **HW Cap Level** – number (e.g., 20,000).
   - This effectively shows **over / under consumption** vs the entitlements.

2. **Deployment & Adoption line chart**
   - X-axis: time (last 12 months).
   - Y-axis: “Deployment & Adoption” or % of HW estate consuming ELA.
   - Two lines:
     - HW Estate Consuming ELA.
     - HW Cap Level (flat reference line).
   - Visual highlight of where consumption crosses cap.

3. **Professional Services Engagement table**
   - Same shape as on Prisma Access deployment page:
     - Project Type
     - Project Manager
     - Consultant
     - Partner
     - Track Status
     - Project End Date

4. **Expandable section: Current Adoption**
   - Likely details how adoption is distributed (regions, models, or modules).

### What this page is trying to communicate

- **Is CDSS deployment aligned with the customer’s hardware capacity and entitlements?**
  - Are they under-consuming (adoption risk) or over-consuming (capacity / renewal opportunity)?
  - How is consumption trending over time?
  - Is Professional Services engaged to remediate risks or accelerate adoption?
- For the CSM, this page answers:
  - “Are they actually using what they bought in CDSS?”
  - “Are we approaching capacity or oversubscribed?”
  - “Who is helping the customer move forward?”

---

## How these pages fit together conceptually

- **Account Health Overview (top band)** gives the cross-product status and narrative.
- **Customer Estate pages** (1, 5, 6) show **what exists and what’s licensed**.
- **Deployment & Adoption pages** (2, 7) show **how much of that estate is live and being used**.
- **Technical Health pages** (3, 4) show **how well the live deployment is behaving** from a support/incident perspective.

Together, these give the Customer Success team a **multi-lens view of one customer’s health**: commercial, lifecycle, adoption, and operational.
