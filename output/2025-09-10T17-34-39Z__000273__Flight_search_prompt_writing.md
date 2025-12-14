# Flight search prompt writing

## You (2025-09-10T17:34:39.184000+00:00)

help me write a prompt for the following intent:

I need to travel from SFO to HYD sometime between the 2nd and 3rd week of october. I need chatGPT to find the cheapest available flight.

I'll travel economy class. I also want the same flight for the 2 or 3 leg flight. Preference will be for weekend travel.

## ChatGPT (2025-09-10T17:34:40.065142+00:00)

Excellent — thanks for the clear intent. Let’s walk through and clarify a few dimensions so that the final prompt for GPT (O3) is structured, analytically rigorous, and optimized for a real-time flight search scenario.

---

### 🧭 DISCOVERY QUESTIONS

Please answer or confirm the following to ensure the final prompt reflects your full intent:

1. **Travel Flexibility**:
   - Is your date range flexible within **Oct 7–20** (which covers the 2nd and 3rd week of October)?
   - Do you want **ChatGPT to prioritize weekends** but **still return weekday options if they’re significantly cheaper**?

2. **Flight Preferences**:
   - You mentioned a **2- or 3-leg flight** — would you prefer **nonstop if available**, or are **layovers acceptable** if cost is lower?
   - Do you want **all legs on the same airline**, or is a mix of airlines okay if it reduces cost?

3. **Airports**:
   - Will you fly **only from San Francisco (SFO)** or are nearby airports (OAK, SJC) also acceptable for departure?
   - Similarly, is **Hyderabad (HYD)** the only acceptable destination airport?

4. **Return Ticket**:
   - Is this a **one-way** or **round-trip** search?

5. **Tools**:
   - Should ChatGPT use **live plugin data** (e.g., Expedia, Kayak, Skyscanner plugins), or should the prompt assume **manual research** via browsing mode?

Once you confirm or clarify the above, just say **"begin creating the prompt"**, and I’ll distill all the information into a high-precision O3-ready prompt with structure, constraints, and reasoning strategies.

## You (2025-09-10T17:36:35.167000+00:00)

Let's change the dates from Oct 10 to Oct 18. Non-stop flights may not be available for cheap. A mix of airlines is not ok. I also want ChatGPT to give me the exact flight link, cuz usually it gives me a fake link or one that redirects me to the homepage of the booking site. I want it to look through all sources, like kayak, booking.com, google flights, etc... ALL options.

## ChatGPT (2025-09-10T17:36:36.153419+00:00)

Perfect. Thanks for the detailed clarification — this sharpens the requirements significantly. Here's a quick structured summary of your clarified intent, which I’ll use to generate the prompt once you say “begin creating the prompt.”

---

### ✅ CLARIFIED INTENT SUMMARY

#### 🎯 **Goal**:
Find the **cheapest available economy-class flight** from **San Francisco (SFO)** to **Hyderabad (HYD)** between **October 10–18, 2025**, preferably on a **weekend**. Flights must be **same-airline**, with **2 or 3 legs acceptable**, and **nonstop is optional but unlikely**.

#### ✈️ **Flight Preferences**:
- **Class**: Economy only.
- **Airline**: **All legs must be on the same airline.** No codeshares or airline mixes.
- **Flight Legs**: 2–3 layovers acceptable.
- **Weekend Preference**: Prioritize departures on **Oct 11–12** (Sat–Sun) and **Oct 17–18** (Fri–Sat), but include cheaper weekday options if significant savings exist.
- **Airports**: Only **SFO → HYD**.
- **Search Scope**: Explore **all major booking engines** (e.g., **Google Flights, Kayak, Booking.com, Expedia, Skyscanner**, etc.).

#### 🔗 **Special Constraint**:
Return **exact, real booking URLs** to the **actual flight page** (not just airline homepages or placeholder links).

#### 🔁 **Trip Type**:
**One-way** (SFO to HYD).

---

Just say **"begin creating the prompt"**, and I’ll generate a structured O3-optimized prompt using this.

## You (2025-09-10T17:37:01.268000+00:00)

begin creating the prompt





## ChatGPT (2025-09-10T17:37:02.009171+00:00)

Below is your O3-ready prompt. You can paste it directly into ChatGPT (with browsing enabled).

---

# Goal
Find the **cheapest available economy-class one-way flight** from **San Francisco (SFO)** to **Hyderabad (HYD)** **departing between Oct 10–18, 2025**, with a **preference for weekend departures**. Itineraries must be **all on the same airline across all segments** (no mixed carriers; avoid codeshares where the operating carrier differs). **2- or 3-leg** connections are acceptable. Deliver **real, working deep links** to book the exact itinerary (not homepages).

# Return Format
1) **Top pick summary (≤120 words)** explaining why it’s optimal (price vs. weekend preference, total duration, layover quality).
2) **Results table (markdown)** with columns:
   - Rank • Date (local dep) • Depart/Arrive (local + TZ) • Airline • Flight #s • Segments • Total duration • Longest layover + airport • Fare brand (Basic/Standard) • Baggage policy • Total price (USD, all-in) • Link label (“Direct airline”, “Google Flights”, “Kayak”, etc.)
3) **Machine-readable JSON** for all returned options (up to 12):
   ```json
   {
     "searched_dates": ["2025-10-10", "...", "2025-10-18"],
     "cheapest_overall": "<rank_id>",
     "cheapest_weekend": "<rank_id>",
     "options": [
       {
         "id": "opt1",
         "date": "2025-10-12",
         "segments": [
           {"from":"SFO","to":"DXB","carrier_marketing":"EK","carrier_operating":"EK","flight_no":"225","dep_local":"2025-10-12 15:45 PDT","arr_local":"2025-10-13 18:55 GST"},
           {"from":"DXB","to":"HYD","carrier_marketing":"EK","carrier_operating":"EK","flight_no":"528","dep_local":"2025-10-13 21:50 GST","arr_local":"2025-10-14 02:30 IST"}
         ],
         "same_airline_all_segments": true,
         "total_duration":"XXh YYm",
         "longest_layover":{"airport":"DXB","duration":"ZZh"},
         "fare_brand":"Economy Saver",
         "baggage":{"carry_on":"7kg","checked":"1x23kg"},
         "price_usd_total": 0,
         "price_source":"Direct airline | Google Flights | Kayak | Skyscanner | Expedia | Booking.com",
         "deep_links":{
           "direct_airline":"<exact itinerary URL>",
           "google_flights":"<exact itinerary URL>",
           "kayak":"<exact itinerary URL>"
         },
         "ref_checks":{"screenshot_ids":["..."],"timestamp_utc":"..."}
       }
     ]
   }
   ```
4) **Reproducibility**: for every link, add a 1–3 step “Open → Filters applied → How to land on the exact itinerary” recipe.
5) **Notes & risks**: flag layovers **>6h**, **overnights**, potential **transit-visa** airports (just a warning, not advice), fare-brand gotchas (no changes, no seat selection), and any **price anomalies**.
6) **Sources list** with working links (no homepages).

# Warnings & Guardrails
- **No mixed carriers**: All segments must share the **same marketing and operating carrier**. If any segment shows “operated by” a different carrier, **exclude** it.
- **Link quality**: Provide **live, deep links** that open the exact itinerary. If a site generates session URLs, prefer a **direct airline deep link** (with prefilled origin, destination, date, cabin, and flight numbers). If still unstable, include a **stable search URL + exact filter path** and mark it as “semi-deep.”
- **De-duplication**: If multiple sources display the same itinerary, report the **lowest total price** and list alternates under the same row.
- **Transparency**: Cite every price with its source and **timestamp (UTC)**. If a link appears to redirect to a homepage or fails on retest, **replace it or mark it broken** and provide a reproducible path.
- **Uncertainty**: Do **not** expose chain-of-thought; provide a concise reasoning summary.
- **If no valid same-airline options** on a given date: return **N/A for that date** and continue; still output the cheapest valid option across all dates.

# Context & Additional Elements
- **Traveler**: 1 adult, economy. (If different, ask once, then proceed.)
- **Date set**: Search **every day from 2025-10-10 to 2025-10-18** inclusive.
- **Weekend preference**: Prioritize **Fri 10/10–Sat 10/11**, **Sun 10/12**, **Fri 10/17–Sat 10/18**; still include cheapest weekday if it’s significantly lower. Report **both** “cheapest overall” and “cheapest weekend.”
- **Airports**: Depart **SFO only**; arrive **HYD only**.
- **Baggage/fare**: Report fare brand and included baggage from the **source of truth (airline site)** when available.
- **Time zones**: Show **local times with TZ codes** (PDT/IST/etc.).
- **Quality filters** (do not exclude, just **flag**): total duration >30h, layovers >6h, overnight transfers, risky connections (<90 min on intl-to-intl).
- **Search scope (use all)**: Google Flights, Kayak, Skyscanner, Expedia, Booking.com/Flights, direct **airline websites** for any discovered single-carrier itinerary.
- **Method (hybrid)**:
  1. Generate the **candidate date list**; weekend subset as tie-breaker.
  2. For each date, query all sources; **filter to same marketing+operating carrier across segments**; allow 2

## You (2025-09-10T17:40:13.631000+00:00)

Stop giving me json format for the output. I just want the response to be in simple text. Assume that I don't want json in the output format unless i expecitly ask for it.
