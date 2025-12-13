# Commit Pipeline Table Example

## You (2025-05-27T20:17:08.743000+00:00)

I need to make a detailed table of a commit pipeline table by accounts. Show me what you would like to see in the form of a table with realistic examples

## ChatGPT (2025-05-27T20:17:09.562813+00:00)

Here’s a commit pipeline table format tailored for an AE at Palo Alto Networks. It reflects a standard Salesforce (SFDC)-aligned commit view that balances MEDDPICC rigor, forecast discipline, and cross-functional alignment. This table is typically used in QBRs, forecast calls, or weekly 1:1s with RVPs or SEs. I've populated it with realistic examples across account segments.

---

| **Account Name** | **Segment** | **Close Date** | **ARR ($K)** | **Stage** | **Forecast Category** | **Champion** | **Compelling Event** | **Solution (Product SKU)** | **MEDDPICC Status** | **Next Step** | **Confidence (%)** | **AE Notes** |
|------------------|-------------|----------------|--------------|-----------|------------------------|---------------|------------------------|-----------------------------|----------------------|---------------|--------------------|-----------------------------|
| Acme Healthcare  | Mid-Market  | 06/28/2025     | 235          | Stage 5    | Commit                 | CISO – Dana M. | Compliance audit (HIPAA) | Strata + Cortex XDR + Premium Success | Fully validated   | CISO call + legal redlines | 90%               | Champion pushing legal to close by EOM. SE led successful PoC. |
| RevNet Logistics | SMB         | 06/24/2025     | 65           | Stage 4    | Best Case              | IT Director – Luis F. | Upcoming acquisition | PA-445 + Panorama + PS      | Metrics in progress | Competitive bake-off | 75%               | Competing with Fortinet. We win on integration + services. |
| Genysis Retail   | Enterprise  | 07/15/2025     | 480          | Stage 3    | Pipeline               | TBD           | Ransomware event (Q1) | Prisma SASE + Cortex XSOAR | Paper process weak   | Re-engage CIO via RVP | 50%               | No clear champion. Need exec alignment. Could flip to Q1 if no traction. |
| Orion Bank       | Enterprise  | 06/27/2025     | 310          | Stage 5    | Commit                 | VP of Security – Mike R. | Contract renewal     | Prisma Cloud Enterprise | Fully validated   | Contract routing | 95%               | Renewal and upsell in final stages. Pricing approved. |
| Nimbly AI         | Mid-Market  | 06/30/2025     | 180          | Stage 4    | Best Case              | CTO – Grace Y. | Board mandate to consolidate vendors | Strata + Prisma Access | DDP + Paper not final | CTO sync 5/29 | 80%               | MSFT E5 overlap; SE countering SSE objections. |

---

### Key Notes:
- **Segment**: SMB (<250K), Mid-Market (250K–1M), Enterprise (>1M).
- **Forecast Category**: Align with SFDC (Pipeline, Best Case, Commit, Closed).
- **MEDDPICC Status**: Include shorthand for what's missing – e.g., “DDP” for Decision Process, “Paper” for legal/procurement.
- **Next Step**: Clear action with date owner.
- **Confidence**: AE-calibrated percentage (not SFDC stage %).
- **AE Notes**: Human context—internal blockers, exec touchpoints, SE input.

Let me know if you’d like a version exportable to Excel/Sheets or to add overlays like SE assigned, CPQ status, or vertical/industry alignment.

## You (2025-05-28T05:28:00.985000+00:00)

{'content_type': 'image_asset_pointer', 'asset_pointer': 'file-service://file-ArqdUN6Rkwvyf1uqC9y2Sf', 'size_bytes': 250921, 'width': 2048, 'height': 1456, 'fovea': None, 'metadata': {'dalle': None, 'gizmo': None, 'generation': None, 'container_pixel_height': None, 'container_pixel_width': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'lpe_keep_patch_ijhw': None, 'lpe_delta_encoding_channel': None, 'sanitized': True, 'asset_pointer_link': None, 'watermarked_asset_pointer': None, 'is_no_auth_placeholder': None}}
Imagine you're looking at this table of renewals. Where would you expect this to appear?

- as an individual tab on your page
- as part of(segmented into forecast)
- as part of (segmented into pipeline)

Help me understand your reasoning. What's more efficient?

## ChatGPT (2025-05-28T05:28:02.625460+00:00)

Great question — and this touches on the AE brain’s constant tension between clarity, speed, and actionability. Here's how I'd break it down:

---

### 🧠 **Where Should This View Live?**
#### ✅ Most Efficient: **Individual Tab on the AE Homepage (e.g., "Renewals At Risk")**

**Why?**
- **Mental Model Alignment**: Renewals, especially high-risk ones, behave differently than net new pipeline. They're time-sensitive, have different stakeholders (Customer Success, Support), and follow a different MEDDPICC motion (usually lighter).
- **Speed to Action**: As an AE, I want 1-click visibility into churn risk, downsell risk, and where I need to escalate. I shouldn’t be toggling between pipeline and forecast just to locate my at-risk renewals.
- **Workflow Simplicity**: I’m likely coordinating with CSAMs, TAMs, and AMs on these — not core SEs or BDMs. It needs a dedicated rhythm.

---

### 🧩 Other Options (Less Ideal):

#### 🚫 **Segmented into Forecast**
- *Issue*: Forecast view is built around linear revenue attainment (Commit → Closed), but renewals aren’t always in Commit due to timing, uncertainty, or lack of exec visibility.
- *Net Impact*: Dilutes forecast purity. Makes it harder to run tight forecast calls.

#### 🚫 **Segmented into Pipeline**
- *Issue*: Pipeline is growth-oriented. Renewal risk distracts from upsell/whitespace strategy.
- *Net Impact*: Muddles conversion rates, clutters pipeline health metrics, and can cause confusion in QBRs.

---

### 🔄 What’s Best-in-Class?
A top AE would push for:
- **Dedicated Renewals Tab** with:
  - Filters: “Health,” “Expected Outcome,” “Close Date”
  - Views: “Past Due,” “This Quarter,” “Next 90 Days”
  - Actions: “Request CS Support,” “Launch Save Motion,” “Escalate Risk”

And crucially:
- **Rollup Metrics at the Top** (like your screenshot) are **excellent** for triage. Keep those.

---

### Summary:
**Most efficient setup: standalone tab for At-Risk Renewals.** It's faster, cleaner, and aligns with how a quota-carrying AE thinks: clear lanes for net new, expansion, and retention. That clarity is what drives execution.

Want me to mock up what the tab layout and filters would look like?

