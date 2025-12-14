# NextDoor cleaning service prompt

## You (2025-09-06T04:21:33.884251+00:00)

Help me create a prompt for the following intent. I am at 512 Van Ness Avenue, San Francisco. And using NextDoor, I want to find at least 20 cleaning service options. Basically, I want a cleaner who can come to my place and just clean my house. But I want someone who is very reasonable. Now, I don't know how cost can be calculated without looking at the house. But I will say, the cheaper ones, the ones who cost less, usually don't advertise a lot. They are independent workers. They don't have multiple cleaners who work for them. It's like one single person who comes and cleans the house. So, it's not like an entire company running it. So, that's usually cheaper. And secondly, they are often recommended directly by people. So, it's not the cleaning services themselves. Like on NextDoor, you will find a lot of times that people themselves just spread the word that, Hey, just FYI, I hired this cleaning lady and she was great. She did a great job and so on and so forth. So, that's the kind of good person. But at the same time, on NextDoor, sometimes citizens share a post saying, I need recommendations for a cleaning service. And in that case, when a company tries to promote themselves, that's usually not quite reasonable. So, basically what I'm saying is, I want a lot of cleaning lady contact names and their numbers. And I want to prioritize only the ones who are highly recommended by most people on NextDoor. Now, you can ask me any questions you want to further narrow down our scope.

## ChatGPT (2025-09-06T04:21:35.310580+00:00)

Great — I hear you’re looking for a **prompt that will guide an O3 reasoning model** to systematically extract *individual, affordable, and well-recommended cleaners* (often independent workers) from **NextDoor posts in San Francisco near 512 Van Ness Avenue**.

Before we jump into “begin creating the prompt,” let’s refine scope a bit so the final prompt works exactly the way you need. Here are a few clarifying questions to tighten things up:

1. **Coverage radius**: Do you want the search strictly limited to your neighborhood (Civic Center / Van Ness), or is it fine if cleaners are in nearby neighborhoods (Tenderloin, Hayes Valley, SoMa, etc.)?

2. **Contact details**: Is your must-have *both* names and phone numbers (or emails), or is it acceptable if some recommendations only have a name or a way to contact them via NextDoor messages?

3. **Threshold for “highly recommended”**: Should we define it more rigorously (e.g., cleaners mentioned in at least 3+ different user comments), or is any repeated positive recommendation enough?

4. **Return style**: Do you want the O3 output in a structured list (Name | Contact | Neighborhood | Notes), or is a plain text summary fine?

5. **Scope of services**: Should we *exclude* bigger companies/franchises entirely (e.g., Merry Maids), or still include them in a “secondary” section in case you want to compare prices?

6. **Volume target**: You mentioned “at least 20.” If there aren’t that many highly recommended independents, should the model fill the gap with slightly less-recommended but still local options?

Once we nail these down, I can draft the structured O3-style reasoning prompt for you.

👉 Which of these do you want to lock in, and do you want me to prioritize *comprehensiveness* (as many options as possible) or *strict filtering* (only the most trusted, even if fewer than 20)?

## You (2025-09-06T04:25:50.688090+00:00)

Speaking of coverage radius, I want to make sure that the people who post these recommendations are within the city of San Francisco. Like they can, I think they can, it's okay to be from DALL·E city or South San Francisco or Oakland but not further south, like not beyond South San Francisco because that gets too far. But the cleaning service, the person actually coming in to clean, you know, they can be from anywhere. More often than not, these people are not able to afford a place in San Francisco so it's hard to say. But the people who post should be from San Francisco. Like Nextdoor is sort of a neighborhood community so and since I am in San Francisco, I want to hear from my neighbors which is people in San Francisco. Speaking of contact details, yes, I need to have both their names and phone numbers. I don't need their email IDs. No, not a recommend, not some way to contact them on Nextdoor. I need their actual name and phone number. I think repeated positive recommendation is enough. It is possible that some people are recommended a lot. Yeah, just highly recommended is repeated positive recommendation is enough. But the reputation should be high. In the output structure, I want the name, I want the phone number, and I want at least four quotes from users who have recommended them. So I need the actual like post, the content from that post and a link for those posts in the output so that I can verify it myself. Yes, I need at least 20. Yes, if there aren't 20, then it can fill the gap with slightly less recommended, but still local options. But I want it sorted by highest recommended and then down to lowest recommended, of course. You can begin crafting, creating the prompt, but don't.

## ChatGPT (2025-09-06T04:25:51.829987+00:00)

Perfect — thanks for clarifying so precisely. I’ll **hold off on creating the actual O3 reasoning prompt** (since you told me *don’t yet*), but let me recap the refined scope so we’re aligned before I generate it:

### 🔑 Key Parameters You’ve Set
1. **Coverage radius (posters)**
   - Only accept recommendations posted by people who live **within San Francisco**.
   - Can allow nearby (Daly City, South SF, Oakland), but **not further south than South SF**.

2. **Cleaner location**
   - No restriction — the person doing the cleaning can be from anywhere.

3. **Contact details (mandatory)**
   - Must return **Name + Phone Number**.
   - No email, no “contact via NextDoor only.”

4. **Recommendation threshold**
   - “Highly recommended” = **repeated positive recommendations**.
   - Reputation should feel strong, not one-off.

5. **Output format**
   - Structured list sorted by **most recommended → least recommended**.
   - For each cleaner:
     - Name
     - Phone number
     - At least **4 quotes from actual posts**
     - Direct **links to those posts**

6. **Volume target**
   - **At least 20 options**.
   - If fewer than 20 high-reputation independents, fill the gap with **slightly less recommended but still local options**.

---

✅ Once you say **“begin creating the prompt”**, I’ll generate the final structured O3-ready prompt using this scope, with the right persona and reasoning steps embedded.

Would you like me to also **build in a secondary filter** that *automatically demotes or excludes companies/franch
