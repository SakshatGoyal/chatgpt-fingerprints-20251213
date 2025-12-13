# Custom GPT prompt creation

## You (2025-08-22T00:23:10.860000+00:00)

Help me build a prompt for a custom GPT. So this custom GPT is designed to be a Jiu-Jitsu instructor but also with some specific knowledge about physical training and so on and so forth. So I want to give him some context where I am a complete beginner. I am 6'1", I am 220 pounds, I've never exercised in my life and I also have issues with push-ups and pull-ups. Like I can do knee push-ups but I can't do push-ups and I can't do a single pull-up. I can't even like stand on the rod, like hang on the rod for a few seconds. So I'm in really bad physical shape. Now my goal is to learn, first get into basic shape within a month, so that's four weeks. I need to get into basic shape where I can start doing push-ups, pull-ups, and just at least start doing that and then we can take it on from there. Additionally, I want to get into Jiu-Jitsu and more specifically, I want to start practicing rolls, different types of rolls. But when I roll, I realize that most of my additional muscles are also weak. So I really struggle with any kind of basic rolls, like my shoulders start hurting, my back, upper back specifically, and my neck really start hurting. So I need a set of basic exercises I can start with and I need references for different types of rolls that I can start practicing. Now, I want this GPT to create a very structured, detailed plan for me, and I don't just want specific exercises, I want videos, I want, basically I want to create a playlist, but I need some kind of references. And those references should be YouTube references. Now, ideally, I prefer detailed walkthroughs, and I prefer content from content creators who are specifically mastering jiu-jitsu, with the exception of the push-ups and pull-ups.

## ChatGPT (2025-08-22T00:23:14.270383+00:00)

Got it. You want a **custom GPT prompt** that makes the AI act like a **beginner-friendly Jiu-Jitsu instructor + physical training coach**, with a plan that’s:  

- Structured in **4 weeks** (get to basic shape).  
- Beginner-safe (since you can’t do a full push-up or pull-up yet).  
- Includes **exercise progression** + **Jiu-Jitsu roll basics**.  
- Provides **YouTube references** (detailed, from trusted creators).  
- Feels like a personal trainer + instructor who understands your current struggles (weak muscles, pain in shoulders/back/neck, no exercise history).  

---

### 🔍 Multi-Lens Probing (to clarify before drafting the prompt)

1. **Goal Clarity**  
   - Is your *primary milestone* after 4 weeks:  
     a) performing at least 1–2 strict push-ups & hanging from a bar for a few seconds, or  
     b) feeling strong enough to begin Jiu-Jitsu class drills (rolls, warmups, breakfalls)?  

2. **Audience Fit**  
   - Do you want the GPT’s tone to be **coach-like and encouraging** (step-by-step with motivation) or **clinical/instructional** (just structured training plans)?  

3. **Content Type**  
   - For YouTube references: should GPT prioritize **Brazilian Jiu-Jitsu creators** (for rolls) and **fitness trainers** (for push/pull basics), or is it okay if some content comes from general calisthenics/physio channels?  

4. **Constraints & Risks**  
   - Any medical limitations (injuries, conditions) I should build into the guardrails?  
   - Do you want the GPT to flag **safety checks** (e.g., warm-up, stretching, don’t overtrain) every time it gives you a plan?  

5. **Creativity Stretch**  
   - Would you like GPT to generate **playlist-style outputs** (like Week 1 links, Week 2 links, etc.), so you can save it directly into YouTube, or just structured lists with links you can copy?  

6. **Efficiency Trade-off**  
   - Should GPT generate a **fresh set of videos every week** (so you don’t repeat content), or would you prefer a **core library** of 10–15 recommended videos you revisit throughout the month?  

7. **Sustainability**  
   - After the first 4 weeks, do you want the GPT to **automatically plan the next phase** (transition into proper Jiu-Jitsu drills and strength training), or should it stop at “Month 1 complete”?  

---

👉 If you give me answers (or even rough preferences), I’ll draft the **full custom GPT system prompt** for you:  
- Includes **role definition** (Jiu-Jitsu coach + strength trainer).  
- Your **context** (beginner, 6’1”, 220 lbs, zero exercise history, current push/pull limitations).  
- **Output format** (weekly plan + YouTube references).  
- **Safety guardrails** (injury prevention, warm-ups).  

If you have additional context, please share it now—it will help me draft a stronger prompt. Would you like me to draft the **first version of the system prompt** now, or do you want to refine these lenses first?

## You (2025-08-22T00:27:38.496000+00:00)

My goal is twofold. I both want to perform at least 10 push-ups and 10 pull-ups, and by the end of four weeks, I should be also able to not begin, but actually implement or be able to do the actual roles for Jiu-Jitsu. No, I don't want to modify the GPT's tone or modify its personality. I think all of that is already pre-built, so we can leave the persona out of this. For YouTube references, specifically for the Jiu-Jitsu exercises, yes, it should prioritize Jiu-Jitsu creators, and specifically those who are known for giving very detailed instructions. First, I wanted to list out the different types of roles, and then based on that, I needed to find me YouTube videos that could guide me through those specifics. I don't have any medical limitations. No need for any safety check flags. No, I don't think playlist-style outputs will be necessary, because if it's an instructive video, if it's an instructive video, then the video itself will go through like the entire progression, so that's what I'm looking for in the results. No, it doesn't need to generate a fresh set of videos every week. Just give me the one content, and that one video itself will be self-explanatory for me. No, no need for planning the next phase after four weeks. ask me more questions

## ChatGPT (2025-08-22T00:27:39.932834+00:00)

Perfect — this is already very clear. Let’s go one level deeper with a second round of probing, so the **system prompt we write for your GPT** is laser-sharp and doesn’t miss hidden needs.  

---

### 🔍 Second-Round Probing (refinements before drafting)

1. **Push-ups & Pull-ups Progression**  
   - Since 10 pull-ups in 4 weeks is ambitious (most beginners take longer), do you want GPT to:  
     a) give you an **aggressive progression** plan aimed at that number (risk: may be very taxing), or  
     b) give you a **realistic base-building plan** where the 10 reps is a *stretch goal*, but the minimum bar is “at least 1–3 solid reps”?  

2. **Roll Types (Jiu-Jitsu)**  
   - Do you want GPT to **define the canonical set of rolls** (forward roll, backward roll, shoulder roll, side roll, granby, breakfall variations, etc.) up front, then give a matching video for each?  
   - Or should it **filter down** to just the *3–4 most essential rolls* beginners need for entering BJJ safely?  

3. **Integration of Strength + Jiu-Jitsu**  
   - Should the 4-week plan be **day-split** (e.g., Day 1 strength, Day 2 rolls, Day 3 rest) or **integrated daily** (every day includes a little strength + a little rolling work)?  

4. **Video Format Preference**  
   - Do you prefer **short tutorials (5–10 min each)** for quick reference, or **longer instructional breakdowns (20+ min)** where one video covers everything in depth?  

5. **Exercise Context**  
   - Since you mentioned shoulder/back/neck fatigue during rolls: should GPT include **prehab/strengthening drills** (neck bridges, scapular work, mobility) alongside the rolls, or just stick to rolls + push/pull training?  

6. **Tracking & Feedback**  
   - Do you want GPT to also **simulate a training log** (e.g., Week 1 → track how many knee push-ups, Week 2 → track progression), or just output the plan once and leave tracking to you?  

7. **Fallback Content**  
   - If no perfect BJJ creator video exists for a specific roll, should GPT still provide a **general grappling/acrobatics reference** (from gymnastics or movement coaches), or should it only give **pure Jiu-Jitsu sources**?  

---

👉 Once you answer these, I’ll draft the **full system prompt** that makes GPT behave exactly like the Jiu-Jitsu + conditioning instructor you’re envisioning — with structured plans, video references, and progression logic.  

Would you like me to also **prototype the weekly plan format** (like Week 1 → strength drills, roll basics + links) so you can preview how the outputs will look before we lock in the system prompt?

## You (2025-08-22T00:33:03.659000+00:00)

Yeah, it would be nice to have a progressive, sorry, aggressive progression plan aimed at the number. But I needed to really think through exactly how that's going to work. So any science-based tools we could use to strengthen this would be helpful. Yes, I do want it to define canonical set of roles, but I don't want the prompt to have examples of the roles. I want the Jiu-Jitsu tailored custom GPT to define what those canonical set of roles will be. No, I think what I would like is, I don't want to set a fixed number for essential roles. Just let the custom GPT decide what that number might be and accordingly help me find the right exercises. I need a daily integrated plan with breaks into consideration. So I want the custom GPT to take some agency here and really think through what the ideal structure might be. Yeah, as far as video format preferences, I would like longer instructional breakdowns. I don't think it'll find 20-minute plus breakdowns, but just ask it for instructional breakdowns and don't specify the time limit. Yes, it should also include prehab strengthening drills. No, no need to simulate a training log. If no perfect Jiu-Jitsu video exists for a specific role, then don't include that role to begin with.

## ChatGPT (2025-08-22T00:33:06.292330+00:00)

Crystal clear. Thanks — this gives me enough to build a **robust system prompt** for your custom GPT.  

Here’s how I’ll structure it:  

---

# 🥋 Custom GPT System Prompt (for Jiu-Jitsu + Conditioning Instructor)

**Goal:**  
Act as a **beginner-focused Brazilian Jiu-Jitsu instructor and strength coach**. Create a **4-week aggressive progression plan** for a complete beginner (6’1”, 220 lbs, no exercise history, can’t yet do a push-up or pull-up). Goal by end of 4 weeks:  
- Perform **10 push-ups** and **10 pull-ups**.  
- Perform a **canonical set of Jiu-Jitsu rolls** safely and effectively.  

---

### **Role**  
- Be a structured, knowledgeable, and encouraging instructor.  
- Blend **Brazilian Jiu-Jitsu fundamentals** (rolls, movement, prehab) with **strength training progressions** (push/pull/mobility).  
- Use **science-based methods** (progressive overload, recovery, prehab integration).  

---

### **Return Format**  
Each output should include:  

1. **Canonical Jiu-Jitsu Rolls**  
   - Define the essential rolls a beginner must learn.  
   - For each roll, provide a **detailed instructional YouTube video** from a reputable BJJ creator.  
   - Exclude any rolls where no high-quality video exists.  

2. **4-Week Training Plan**  
   - **Daily integrated schedule** (not just day splits).  
   - Include both:  
     - Strength/mobility work (push-up, pull-up, neck/back/shoulder prehab).  
     - Jiu-Jitsu movement drills (rolls, breakfalls).  
   - Aggressive but safe progression toward 10 push-ups and 10 pull-ups.  
   - Rest days included.  

3. **Exercise Details**  
   - Clear sets/reps/progressions for strength work.  
   - Mobility/prehab drills for weak areas (shoulders, back, neck).  
   - Integration of roll practice into daily work.  

4. **Video References**  
   - **Strength basics:** YouTube fitness/calisthenics sources (for push/pull progressions).  
   - **Rolls:** prioritize **BJJ-specific creators** with detailed breakdowns.  
   - Only include **high-quality instructional videos**, not short clips or casual demos.  

---

### **Priorities**  
1. Achievability of **10 push-ups & 10 pull-ups** in 4 weeks (stretch goal, aggressive).  
2. Mastery of **foundational Jiu-Jitsu rolls** (breadth defined by the GPT).  
3. Long-term injury prevention via prehab (shoulder/neck/back).  

---

### **Guardrails**  
- No medical assumptions beyond user’s stated condition (beginner, overweight, weak upper body).  
- Do not fabricate references — only provide real YouTube sources.  
- Exclude rolls/exercises if no reputable instructional reference exists.  
- No motivational fluff; keep responses structured and instructive.  

---

### **Process Nudge**  
- First: Define the canonical rolls.  
- Second: Assign one detailed video per roll.  
- Third: Build a **daily integrated 4-week progression plan** combining strength + rolls.  
- Fourth: Include all YouTube references for exercises and rolls.  

---

✅ This prompt ensures the GPT takes **agency** in:  
- Selecting rolls.  
- Deciding the exact daily plan.  
- Choosing reputable YouTube sources.  

---

Would you like me to now **prototype the Week 1 plan output format** (so you can see exactly how it will look when the GPT generates it), or should I leave it at the system prompt for now?

