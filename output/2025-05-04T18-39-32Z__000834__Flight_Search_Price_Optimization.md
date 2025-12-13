# Flight Search Price Optimization

## You (2025-05-04T18:39:32.220559+00:00)

Help me make an o3 prompt for the following intent:

Help me find a flight from San Francisco to Hyderabad on either Emirates or Cathay Pacific for any date between May 23rd and May 30th. 

Make sure you explore every possible option available on every different site, my goal is to find the lowest fair prices. 

I don't want flights where I have to swtich airlines. I don't want the overall journey including lay over to be more than 28 hours. 
---

Basically, I want chatgpt to explore every possible option. I want to make sure I am getting the cheapest possible flight. Oh, and I want the amount in INR. My dad is booking from india so I need to make sure that the sites I'm exploring are in india.

## ChatGPT (2025-05-04T18:39:33.954507+00:00)

Excellent—thanks for the detailed intent. Let me walk you through a few clarification points to ensure the prompt we create will push O3 to reason deeply and comprehensively, across multiple sites and constraints:

---

### 🔍 Clarification Pass: Intent & Constraints

1. **Goal Clarity**:
   - ✅ You want to **find the lowest fare** for a flight from **San Francisco (SFO) to Hyderabad (HYD)**.
   - ✅ Only **Cathay Pacific or Emirates** are acceptable.
   - ✅ The flight must **depart between May 23–30**.
   - ✅ No **airline switching** during the trip.
   - ✅ Total **journey duration must not exceed 28 hours**.
   - ✅ **Display fare in INR**.
   - ✅ Search **Indian-facing travel sites** to ensure pricing reflects what your dad in India would see.

2. **Depth of Exploration**:
   - You want **exhaustive coverage**, including **site-by-site comparisons** across **aggregators** (e.g., MakeMyTrip, Yatra, Cleartrip) and **direct airline portals** (e.g., emirates.com/in, cathaypacific.com/in).
   - Price should reflect **economy class**, unless you want to explore other classes as well?

3. **Assumptions to Confirm**:
   - Would you like **both one-stop and direct flights**?
   - Are **overnight layovers** acceptable within the 28-hour limit?
   - Do you want the model to **sort by price only**, or **weigh other factors** (e.g., layover quality, airport comfort)?
   - Do you want to **exclude red-eye flights** or flights arriving at odd hours?

---

Once you confirm (or revise) those assumptions, I’ll move into the **prompt creation phase**. Just say **"begin creating the prompt"** once you're ready.

Would you like to include both one-stop and direct flights, or direct only?

## You (2025-05-04T18:42:34.681363+00:00)

i want both - one stop and direct flights. However one stop has a higher likelihood of being cheaper so lets stick with one stop. But not two stop. 

Yes, but just to be sure, the overall 'journey', not the layover should be 28 hours. Meaning, I Do not want the layover to be 28 hours, the complete trip including flying hours should not exceed 28 hours. 

No sort by price only for now. 

No don't exclude flights arriving at odd hours. 

The only facotrs include price, travel time, and the airlines (has to either be emirates or cathay pacific)

## ChatGPT (2025-05-04T18:42:36.196630+00:00)

Perfect—that’s the level of clarity we need for a sharp O3 prompt. Here’s a quick recap of the refined constraints and intent before I generate the full structured prompt.

---

### ✅ Finalized Analytical Intent Summary

- **Route:** San Francisco (SFO) → Hyderabad (HYD)  
- **Airlines:** Emirates or Cathay Pacific only  
- **Date Range:** May 23–30 (any departure date in this range)  
- **Stops:** Direct or **one-stop only**; **no two-stop** itineraries  
- **Total Journey Time:** Must be **28 hours or less**, including all layovers  
- **Currency:** Prices shown in **INR**, as booking will be done from India  
- **Sources to Explore:** All major **India-facing portals** (e.g., MakeMyTrip, Yatra, Cleartrip, airline websites with /in regional pages)  
- **Class:** Economy (assumed)  
- **Priorities:** **Price first**, then airline constraint and total travel time  
- **No exclusions** based on time-of-day or layover length (as long as within 28 hrs total)

Let’s move into prompt generation.

---

Please confirm with: **"begin creating the prompt"**  
And I’ll generate the full structured O3 reasoning model prompt, complete with guardrails and execution persona.

## You (2025-05-04T18:42:47.499868+00:00)

begin crafting prompt

## ChatGPT (2025-05-04T18:42:48.352508+00:00)

Excellent. Based on everything you've shared, here's the fully structured O3-optimized reasoning prompt tailored to your goal.

---

### ✳️ O3 Reasoning Prompt for Cheapest Flight Search (SFO → HYD)

#### 1. **Goal**  
Identify the **lowest fare** economy-class flight from **San Francisco (SFO) to Hyderabad (HYD)** between **May 23 and May 30**, operated **exclusively by Emirates or Cathay Pacific**, with **no more than one stop**, and a **total journey duration (including layovers) not exceeding 28 hours**. The objective is to optimize for **minimum total fare in INR** as seen from **India-facing travel platforms**.

#### 2. **Return Format**
Provide:
- ✅ A **ranked list** of matching flights (sorted by **lowest INR price first**)
- ✅ For each flight, include:
  - Airline name
  - Date of departure
  - Total price in INR
  - Total journey duration (in hours and minutes)
  - Layover city and duration
  - Departure and arrival local times
  - Booking link (Indian version of the site, if available)
  - Source site (e.g., Emirates India site, MakeMyTrip India, etc.)

#### 3. **Warnings & Guardrails**
- ⚠️ **Do not include** any flights with **two or more stops**, **airline switches**, or **codeshare hops** outside Emirates or Cathay Pacific.
- ⚠️ Only return flights with a **total journey time ≤ 28 hours**.
- ⚠️ Ensure the INR pricing reflects what would be shown to an Indian user—**use India-based travel portals or the `/in` region of the airline's website**.
- ⚠️ Do not infer availability—**only use verifiable listings**.
- ⚠️ If no qualifying flights exist for a particular date, say so explicitly.

#### 4. **Context & Additional Elements**
- Assume the request is being made by someone booking on behalf of a family member in India, where **INR-based pricing and local booking portals** are essential.
- Prioritize **one-stop flights** over direct flights due to likelihood of lower fares, but **include both** if they meet all other constraints.
- Execution persona: **Travel Analyst with access to Indian travel portals**, skilled at comparative fare analysis and route optimization, fluent in interpreting layover durations and fare structures across booking sites.

---

Would you like me to convert this into a reusable tool prompt format (e.g., for recurring use or API)?

