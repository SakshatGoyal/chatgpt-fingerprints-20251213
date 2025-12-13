# Discount Code Discovery Strategy

## You (2025-07-27T22:04:09.756000+00:00)

help me refine the following prompt.:

Find all possible discount codes for the app argon.ai

Utilize all available resources, including but not limited to podcast references, influencer codes from YouTube or other platforms, and websites that offer discount codes. Start by identifying all the different sources where argon.ai has been referenced, and then see if you can find any discount codes shared by people on various platforms. 

in your response, include the discount code, when it was last referenced, how much discount code, and the source. 

For this prompt, imagine you are a thrifty hacker who goes above and beyond to find the best deal possible for himself.

## ChatGPT (2025-07-27T22:04:10.276394+00:00)

Great — you’re aiming for a prompt that simulates a deeply resourceful persona ("thrifty hacker") to surface *all possible discount codes* for the app **argon.ai**, with structured metadata (code, date, value, source), leveraging open-source intelligence (OSINT)-style scraping of decentralized and possibly ephemeral content.

Before we begin refinement, a few clarification questions to make sure this is *optimized for O3* reasoning:

---

### 🧠 Clarification & Discovery

1. **Depth of Search**:  
   Should the agent exhaustively scan forums, Discord servers, GitHub issues, or browser extension coupon engines (e.g., Honey, Coupert), or limit itself to higher-signal sources like podcasts, YouTube, and deal sites?

2. **Real-Time vs Archival**:  
   Do you want **only currently valid codes**, or should it include **historical/inactive codes** (with metadata) for pattern analysis?

3. **Date Sensitivity**:  
   Should the agent prioritize the *freshest* codes or just include the last-seen timestamp for all regardless of staleness?

4. **Code Type Segmentation**:  
   Should it distinguish between **public influencer codes**, **personalized/referral codes**, and **automatically applied coupon codes**?

5. **Persona Intent**:  
   Should the “thrifty hacker” persona make assumptions (e.g., try permutations of known code formats like `INFLUENCER10`), or strictly surface *verifiable* codes?

---

If you'd like, I can now move forward based on what you've shared so far and fill in reasonable defaults (but answering the above will sharpen it even more). Otherwise, just say:

**“Begin creating the prompt.”**

## You (2025-07-27T22:05:47.522000+00:00)

Yes, the agent should exhaustively scan forums, Discord servers, GitHub issues, or browser extension coupon engines in addition to sources like podcasts, YouTubes, and deal sites. Yes, it should include historical or inactive codes. Anything within the last three months would be help, or six months. Anything within the last six months. Yes, it should distinguish between public influencer codes and personalized or referral codes and automatically applied coupon codes, but it should give me all of the above. No, the persona should strictly surface verifiable codes. Begin creating the prompt.

## ChatGPT (2025-07-27T22:05:48.259228+00:00)

Excellent—thank you for the precision. Here’s a refined, O3-optimized prompt structured for rigorous, multi-source discount code discovery with a resourceful but truth-bound execution persona:

---

### ✅ Final Prompt (O3 Optimized)

#### 1. **Goal**  
Identify and extract all **verifiable discount codes** for the app **argon.ai**, using comprehensive open-source discovery methods across a wide array of platforms and formats. The objective is to uncover *any* discount, referral, or promotional codes—active or historical (within the last 6 months)—with clear attribution to source, type, and recency.

#### 2. **Return Format**  
Return a structured table or list where **each entry includes**:

- `Code`: The exact discount/promo/referral code  
- `Discount Value`: (e.g., “10% off,” “1 free month,” etc.)  
- `Source`: Platform and specific channel/URL (e.g., YouTube, Reddit post, Discord message, GitHub issue, coupon extension site)  
- `Code Type`: One of `[Public Influencer Code | Personalized Referral Code | Auto-Applied Coupon | General Promo Code]`  
- `Last Referenced`: A timestamp or approximate date when the code was last shared or confirmed  
- `Status`: [Likely Active | Possibly Expired | Confirmed Expired], based on recency and user reports  

Ensure all entries are backed by verifiable sources or platform mentions. **Exclude fabricated or speculative codes**.

#### 3. **Warnings & Guardrails**

- **No Guessing or Fabrication**: Do not generate codes by inferring patterns or making assumptions. Only include codes that have been explicitly and verifiably mentioned online.
- **Temporal Validity Matters**: A code older than 6 months should be excluded unless there’s evidence it's still active. Prioritize freshness.
- **Separate by Type**: Maintain clarity between code categories (e.g., public influencer vs referral vs auto-applied).
- **Respect Platform TOS**: If any forum or channel prohibits scraping or public disclosure, omit those sources and note the limitation.

#### 4. **Context & Additional Elements**

- **Execution Persona**: Adopt the mindset of a savvy, ethically resourceful “thrifty hacker” who methodically scours the internet for the best deal, but never violates terms of service or invents information.
- **Discovery Methodology**:
  - Search Reddit (e.g., r/InternetIsBeautiful, r/deals, r/SaaS), GitHub issues, Discord threads (if public), deal aggregators (e.g., RetailMeNot, Honey).
  - Parse YouTube video descriptions, podcast transcripts, blog posts, and influencer code aggregators.
  - Include information from browser extensions (e.g., Honey, Coupert, Capital One Shopping) if accessible.
- **If no codes are found**: Return a brief explanation of what was searched, where, and why no results were found. Include any partial leads or possible expired codes.

---

Let me know if you'd like a version optimized for real-time plugin or tool execution (e.g., using web browsing or scraping functions), or if you'd like this prompt adapted to target another app or platform.

## You (2025-07-31T22:14:59.777000+00:00)

Ok, now, i want you to customize this same intent (of finding discount codes) but for etsy. For your context, I'm looking to buy jewelry. here're some of the products i'm interested in - but I don't think we can customize our search just for these products. we can take a two fold appraoch where we instruct chatGPT to look for codes aligned to these products, but also jewelry or etsy in general that might work with my cart. here're the products. adjust all the criteria like persona and mindset and process accordingly. 

https://www.etsy.com/listing/4332068872/handmade-brass-band-ring-bold-brass?ref=cart

https://www.etsy.com/listing/1006893506/simple-raw-brass-ring-minimalist?ref=cart

https://www.etsy.com/listing/1033396479/ring-for-men-bronze-plain-ring-mens-ring?ref=cart

begin writing the prompt.

## ChatGPT (2025-07-31T22:15:00.269058+00:00)

Here's your custom O3-optimized Etsy discount prompt, tailored specifically for jewelry, with a targeted yet broad two-fold discovery strategy:

## ChatGPT (2025-07-31T22:15:05.455845+00:00)

{"content_type": "code", "language": "json", "response_format_name": null, "text": "{\"name\":\"etsy_jewelry_codes\",\"type\":\"document\",\"content\":\"### ✅ Final Prompt (O3 Optimized): Etsy Jewelry Discount Codes Discovery\\n\\n#### 1. **Goal**\\nIdentify and compile verifiable discount or promotional codes for purchases on **Etsy**, specifically targeting **handmade jewelry**, and more specifically, brass and bronze rings similar to the following items:\\n\\n- [Handmade Brass Band Ring - Bold Brass](https://www.etsy.com/listing/4332068872/handmade-brass-band-ring-bold-brass)\\n- [Simple Raw Brass Ring - Minimalist Jewelry](https://www.etsy.com/listing/1006893506/simple-raw-brass-ring-minimalist)\\n- [Men's Bronze Plain Ring](https://www.etsy.com/listing/1033396479/ring-for-men-bronze-plain-ring-mens-ring)\\n\\nConduct a two"}

## ChatGPT (2025-07-31T22:15:16.974051+00:00)

### ✅ Final Prompt (O3 Optimized for Etsy Jewelry Discounts)

#### 1. **Goal**  
Identify and extract all **verifiable discount codes** applicable to **Etsy purchases**, prioritizing discounts specifically relevant to jewelry (particularly rings or handmade brass/bronze jewelry). Employ a dual-layered approach:
- **Primary**: Search explicitly for discount codes or promotional offers related directly to the following products (or similar products):
  - Handmade Brass Band Ring: [listing/4332068872](https://www.etsy.com/listing/4332068872/handmade-brass-band-ring-bold-brass)
  - Simple Raw Brass Minimalist Ring: [listing/1006893506](https://www.etsy.com/listing/1006893506/simple-raw-brass-ring-minimalist)
  - Bronze Plain Men’s Ring: [listing/1033396479](https://www.etsy.com/listing/1033396479/ring-for-men-bronze-plain-ring-mens-ring)
- **Secondary**: Broader search for Etsy discount codes relevant to jewelry purchases in general, or Etsy-wide discount codes potentially applicable to the shopping cart.

#### 2. **Return Format**  
Return structured results clearly segmented into **two distinct categories**:

**A. Product-specific or Jewelry-focused codes**  
**B. General Etsy platform codes**  

Each entry must include:
- `Code`: Exact discount/promo/referral code  
- `Discount Value`: Clearly defined (e.g., "10% off," "$5 off," "free shipping," etc.)  
- `Source`: Platform and direct channel or URL (e.g., YouTube description, Reddit thread, coupon aggregator, influencer blogs, browser coupon extensions like Honey, Coupert, RetailMeNot, Capital One Shopping, etc.)  
- `Code Type`: `[Public Influencer Code | Personalized Referral Code | Auto-Applied Coupon | General Promo Code]`  
- `Last Referenced`: Timestamp or approximate date within the past 6 months  
- `Applicability`: Clearly indicate whether it specifically applies to Etsy-wide purchases, jewelry-specific categories, or individual sellers/stores.

#### 3. **Warnings & Guardrails**
- **No Speculative Codes**: Only include discount codes explicitly referenced or verifiable online. Do not guess or infer codes.
- **Relevance & Validity Window**: Prioritize codes referenced within the past 6 months. Older codes must clearly note possible expiry.
- **Clarity of Applicability**: Clearly specify the scope of applicability (product-specific, store-specific, jewelry-specific, or Etsy general).
- **Respect Platform Policies**: Do not violate Etsy’s terms of service or other platforms’ rules during code discovery.

#### 4. **Context & Additional Elements**
- **Execution Persona**: Adopt a highly resourceful, careful, and ethically-minded "Smart Shopper" persona who methodically hunts for the best deals on Etsy jewelry, cross-verifies all findings, respects platform policies, and focuses on maximizing savings and efficiency.
- **Discovery Methodology**:
  - Check niche sources such as jewelry forums, Etsy-focused deal communities (e.g., Etsy Reddit, Facebook groups), influencer videos (YouTube, TikTok), podcasts, blogs focused on handmade goods, and coupon platforms.
  - Include browser extensions and shopping tools known for coupon discovery.
  - Search explicitly for seller promotions or store-specific codes from the Etsy listings provided.
- **No Results Scenario**: If no valid codes are found, explicitly summarize your thorough search process, provide insights into partial matches or expired codes discovered, and offer actionable suggestions for alternative savings.

---

This prompt is designed to strategically balance precision (product-specific) and breadth (general Etsy discounts), maximizing the likelihood of actionable findings tailored specifically to your jewelry-focused shopping goals.

