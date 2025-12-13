# Forecast vs pipeline confusion

## You (2025-11-25T21:23:44.154000+00:00)

{'content_type': 'image_asset_pointer', 'asset_pointer': 'sediment://file_00000000081072099522dcdaf8a7d5ce', 'size_bytes': 203515, 'width': 1680, 'height': 1264, 'fovea': None, 'metadata': {'dalle': None, 'gizmo': None, 'generation': None, 'container_pixel_height': None, 'container_pixel_width': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'lpe_keep_patch_ijhw': None, 'lpe_delta_encoding_channel': None, 'sanitized': True, 'asset_pointer_link': None, 'watermarked_asset_pointer': None, 'is_no_auth_placeholder': None}}
I want your quick thoughts on something, when i showed this to sales managers they said we're micxing forecast and pipeline. Could you help me understadn where the problem is

## ChatGPT (2025-11-25T21:23:46.478646+00:00)

Here’s the clean DSM read — **yes, the managers are reacting to a real issue**, and their instinct is right. The view is *blending forecast concepts (Commit/Best/Closed)* with *pipeline concepts (coverage, target gap, CCBC)* into one screen without a clear separation of purpose.

### **Where the confusion comes from (the core issue)**  
You're showing, **in the same frame**:

1. **Forecast constructs**  
   - Closed  
   - Commit  
   - Best Case  

2. **Pipeline constructs**  
   - Target Gap  
   - CCBC (coverage)  
   - Total Target  

3. **Territory performance analytics**  
   - “Territories with lowest commit ratio”  
   - “Highest critical accounts”

Those are three *different jobs-to-be-done*, each with its own mental model for a sales leader. When they’re mixed, managers don’t know whether this screen is supposed to be:

- a **Forecast roll-up**  
- a **Pipeline health report**  
- a **Territory diagnostic dashboard**

Because the data elements imply conflicting intent.

---

## **Why this matters (DSM lens)**  
Forecast = **facts that close this quarter**  
Pipeline = **coverage and future build**  

When put together, managers naturally ask:  
“Is this telling me what will close **now**, or what we have to work **later**?”

Your view currently answers both — therefore answers neither crisply. This is the “mixing” they’re reacting to.

---

## **Specific mixing points**
### 1. **Target Gap + CCBC** → Pipeline view  
Those belong in a pipeline health dashboard.  
They imply next-quarter risk and coverage, not forecast accuracy.

### 2. **Closed / Commit / Best** → Forecast view  
These belong to the in-quarter forecast roll-up. They’re “evidence gates” not coverage gates.

### 3. **District/Rep-level targets**  
Annual or quarterly targets pull people back into a **performance** view, which is neither forecast nor pipeline.

### 4. **Filters: “Territories with lowest commit ratio”**  
Commit ratio is a forecast metric, but “Territories with highest critical accounts” is a pipeline risk metric.

---

## **How to fix it (high-level product POV)**
**Split this into two modes** that match real sales motions:

### **1. Forecast Mode (in-quarter, evidence-based)**
- Closed  
- Commit  
- Best/Upside  
- Evidence gates (Champion, InfoSec, Paper process)  
- Expected slip-risk  

**Exclude:** target gaps, CCBC, coverage ratios.

---

### **2. Pipeline Mode (forward-looking build + risk)**
- Target Gap  
- CCBC  
- Stage mix  
- Inflow quality  
- Aging deals  
- Critical accounts  

**Exclude:** commit/best bars.

---

## **DSM recommendation (if we were coaching PM)**
“Forecast and pipeline answer different questions. Keep them separate so managers stay in the right mental model. Forecast = current-quarter evidence. Pipeline = future-quarter coverage. Combine only in an executive summary with clear labeling.”

---

If you want, I can mock up **what each mode should look like**, with the correct fields for each and the “manager job-to-be-done” tied to each view.

## You (2025-11-25T21:26:10.361000+00:00)

Could you synthesize the core issue and your explanation in 4-5 sentences for a design leader so they could figure out how to handle this in their strategy.

## ChatGPT (2025-11-25T21:26:11.759152+00:00)

The core issue is that the view blends **forecast constructs** (Closed/Commit/Best) with **pipeline constructs** (coverage, target gaps, CCBC) in the same frame, which forces managers into two different mental models at once. Forecast answers *“What will close this quarter?”* while pipeline answers *“Do we have enough and the right mix for future quarters?”* — and mixing them makes neither story clear or actionable. The presence of territory performance metrics further muddies the job-to-be-done. The result is cognitive overload and unclear intent: managers don’t know whether to interpret this as a forecast roll-up, a pipeline health dashboard, or a territory diagnostic. A clean strategy is to separate these modes so each view supports a single, unambiguous decision workflow.

## You (2025-11-25T22:04:53.557000+00:00)

ok, and what is EBC?

## ChatGPT (2025-11-25T22:04:56.015259+00:00)

In the context of your screenshot, **EBC = “Expected Best Case”**.

Some teams abbreviate “Best Case In” or “Expected Best Case” as **EBC** to differentiate it from pure Best Case pipeline. It usually means: *the amount a manager believes can realistically land this quarter **if** the identified risks are cleared*, i.e., the upside that still has a credible path to close. It’s not pipeline, and it’s not commit — it’s the forecastable upside bucket tied to evidence, not hope.

If your org uses a slightly different

## You (2025-11-25T22:35:31.004000+00:00)

no in the context of executive alignemnt and not my screenshot

## ChatGPT (2025-11-25T22:35:32.032629+00:00)

Got it — in **executive alignment**, **EBC = Executive Business Case**.

This typically refers to the **formalized business case** created with, and validated by, the customer’s executive stakeholders. It captures the *why now* — the quantifiable outcomes, cost justification, risk reduction, and strategic priorities that anchor the deal to the customer’s top-level objectives. An EBC is one of the strongest forms of **Decision Criteria + Champion/Economic Buyer alignment** because it proves that the exec sponsor agrees on the problem, the economics, and the success measures.

In short: **EBC = the jointly authored “business value proof” with the customer’s execs**, and it's a major evidence point in MEDDPICC.

