# ADD Evaluation Summary Prep

## You (2025-03-15T23:46:56.855875+00:00)

Hey Elliot, I need your help building a prompt.

I'm attaching essentially a one-hour conversation. It's sort of a monologue where I just dictated all of my notes regarding a certain issue that I'm experiencing with the lack of focus and the lack of having the ability to pay attention to things. So it's a very long and I've tried to keep it as detailed as possible, but what I need now is for some way to summarize it in the ideal way for a doctor. So I'm having an ADD evaluation with another therapist on Monday. So I want to make sure that I'm explaining all the facts as they are. Now, one of the major problems with my current medical team has been this recurring theme that they keep forcing the idea that I'm experiencing extreme depression and anxiety, which I'm not. It's been going on for a few months. The problem is during my conversations with every doctor, I keep confirming that, hey, I don't know why you're saying that I'm depressed. I really am not necessarily depressed, but what they keep doing is essentially writing within their notes that patient has expressed that he is experiencing severe depression, and I keep bringing it up with my doctors, and they just say, oh, we're just writing notes. It's not that important. However, it does impact the next doctor as well. So this time what I try to do is have a detailed verbal outlining of all the symptoms I've experienced, all the actions I've taken as a result, and all the experiences I've had with different medical teams, recommendations from the therapists, from the other psychiatrists outside the Kaiser Network. All the symptoms I'm experiencing, all the issues it has caused during my day-to-day, how it's creating, how it's now leading to some family issues as well, and all of these things. So while I've given a lot of details, which I'm not attaching in this prompt, I'll be attaching it within sort of like a context dump or something, some kind of attachment in the next thing. But basically what I need is some prompt that can help CHAT-GPT do a very thorough analysis of every single thing I have mentioned, because it's very critical. It is medical information, and we can't take things lightly here. It has to be a very thorough job of understanding everything that's going on and structuring all the content in a way that is easy for a doctor to understand. Now these are my thoughts. Please go ahead and ask me some questions about the context that can help us build a better prompt.

## ChatGPT (2025-03-15T23:46:58.619479+00:00)

Got it. This is an important request, so I want to make sure we construct a prompt that guarantees the most accurate and structured output. Here are some key clarifications to refine the prompt:

### 1. **Core Goals of the Summary**
   - Do you want the summary to be structured like a **formal medical report**, or should it be **a personal patient statement** that you present to the doctor?
   - Should it **highlight key symptoms first** or **focus on chronology** (how things developed over time)?
   - Do you want it to **explicitly counter the depression/anxiety misdiagnosis** within the summary, or just ensure that it is omitted?

### 2. **Content Prioritization**
   - What are the **top 3-5 most important points** you want the doctor to walk away with?
   - Should the output include **direct quotes or paraphrased summaries** of your dictated notes?
   - Do you want a **section dedicated to past treatments and their outcomes**, or should it be integrated into the timeline?

### 3. **Medical Team and External Opinions**
   - How should we frame **your past interactions with doctors** (e.g., neutral tone vs. pointing out miscommunication)?
   - Should the summary **clearly differentiate advice from different professionals** (e.g., "Therapist A recommended X, Psychiatrist B disagreed")?
   - Should it include **your own hypotheses** about what is happening, or just observed symptoms?

### 4. **Structuring for Readability**
   - Would bullet points and structured sections (e.g., Symptoms, Impact, Medical History, External Opinions) be best, or should it read more like an essay?
   - Do you want **a TL;DR summary at the top** for quick reference?

Once you provide clarity on these, I’ll structure a highly detailed and effective prompt to ensure ChatGPT delivers the most useful summary for your doctor.

## You (2025-03-15T23:56:06.862544+00:00)

•	Do you want the summary to be structured like a formal medical report, or should it be a personal patient statement that you present to the doctor?

It is a personal patient summary, but it should be easy to read for a doctor.


	•	Should it highlight key symptoms first or focus on chronology (how things developed over time)?

I'm not sure, I want chatgpt to think through what might be ideal for a doctor given all the context. the context (which is my notes) should help chatgpt determine the right approach.


	•	Do you want it to explicitly counter the depression/anxiety misdiagnosis within the summary, or just ensure that it is omitted?

I don't think it should necessarily be ommitted. This is the main reason I'm seeing the new doctor is that my current team at Kaiser keeps pushing the idea of Depression, and my therapist told me that she has seen the same thing happening with a few of her other patients that come from kaiser so she's recommended that I try to get a consultation from outside the network.

	•	What are the top 3-5 most important points you want the doctor to walk away with?

I want chatgpt to analytically think through - based on the content i share along with the fact that this needs to be shared with a psychiatrist, - and figure out what is the best approach while  sharing with the psychiatrist. I'm seeing this new psychiatrist for the first time.


	•	Should the output include direct quotes or paraphrased summaries of your dictated notes?

I want chatgpt to analytically think through what might be the best approach.


	•	Do you want a section dedicated to past treatments and their outcomes, or should it be integrated into the timeline?

If the content supports it, then yes.


	•	How should we frame your past interactions with doctors (e.g., neutral tone vs. pointing out miscommunication)?

Maintain a neutral tone, but make sure not to leave out any critical issues i've been facing with the team.

	•	Should the summary clearly differentiate advice from different professionals (e.g., “Therapist A recommended X, Psychiatrist B disagreed”)?

Yes.

	•	Should it include your own hypotheses about what is happening, or just observed symptoms?

Good question. outline all the observed symptoms. Don't phrase it as my hypothesis. I think the content i share will help outline how i reach certain conclusions.


	•	Would bullet points and structured sections (e.g., Symptoms, Impact, Medical History, External Opinions) be best, or should it read more like an essay?

I want chatgpt to think through what might be the best approach to share with the doctor based on the content.

	•	Do you want a TL;DR summary at the top for quick reference?
Yes.

____

Additional information for you:

leave a section where I can paste my notes. give me your response in canvas.

## ChatGPT (2025-03-15T23:56:07.742906+00:00)

{"name": "add_evaluation_summary", "type": "document", "content": "**Prompt for ChatGPT to Analyze and Summarize Patient Notes for a Psychiatrist**\n\n**Objective:**\nGenerate a structured, comprehensive, and easy-to-read summary for a psychiatrist based on the provided dictated notes. The summary should ensure clarity and conciseness while maintaining all essential details necessary for the psychiatrist to understand the patient’s experiences, symptoms, and past medical interactions.\n\n---\n\n**Context:**\n- The patient is seeking an ADD evaluation with a new psychiatrist outside of their current medical network (Kaiser).\n- Past interactions with Kaiser-affiliated doctors have led to a recurring misinterpretation of the patient's condition as depression/anxiety, despite the patient consistently stating otherwise.\n- The summary should maintain a neutral tone while ensuring all key experiences, symptoms, and medical interactions are documented accurately.\n- The summary should be structured in an optimal way for a psychiatrist to process the information effectively.\n\n---\n\n**Instructions for Analysis and Structuring:**\n1. **Determine the Ideal Structure:**\n   - Assess whether the content is best presented in a chronological format or a symptom-first approach based on the provided notes.\n   - Consider a mix of structured sections (e.g., Symptoms, Impact, Medical History, External Opinions) or a well-organized narrative depending on what makes the most sense for clarity.\n\n2. **Key Content Considerations:**\n   - Extract the **most critical takeaways** for the psychiatrist to understand.\n   - Highlight **observed symptoms** and their real-world impact without framing them as patient hypotheses.\n   - Ensure differentiation between medical opinions from various professionals.\n   - Maintain a neutral tone while accurately describing previous miscommunications with the medical team.\n   - If applicable, include a section outlining past treatments and their outcomes.\n\n3. **Formatting Guidelines:**\n   - Include a **TL;DR summary at the top** for quick reference.\n   - Use a structured format that is clear and digestible for a psychiatrist.\n   - If necessary, incorporate both direct quotes and paraphrased content, choosing the best approach for clarity.\n\n4. **Output Requirements:**\n   - Ensure all medical information is treated with the necessary depth and attention to detail.\n   - Provide a final summary that can be easily shared with a psychiatrist in a way that they can quickly grasp the patient’s history, current concerns, and the rationale for seeking an external evaluation.\n\n---\n\n**[Paste Notes Below]**"}

## ChatGPT (2025-03-15T23:56:25.838537+00:00)

I've structured the prompt to ensure ChatGPT deeply analyzes your dictated notes and provides a structured summary tailored for a psychiatrist. You can paste your notes in the designated section, and the AI will optimize the output based on the best approach for clarity and medical understanding. Let me know if you need any refinements!

## You (2025-03-15T23:59:00.045170+00:00)

I like the prompt overall. Here are one of my concerns. Here's one of my concerns, which is that I think the fact that I have mentioned to you that there are some issues with misdiagnosis or whatnot, I think just the fact that I have mentioned it to you has made you spend significant portion of the prompt within that, which is fine. It is fine, but I'm just trying to make sure if there's some way for the prompt to understand that the miscommunications I'm outlining is only like probably one less than one-third of the content. There's actually a lot, far too much content for it to process, but I need it to be processed in a very thorough way and in a thoughtful way, but I don't think we need to mention it to be thoughtful because it's an O3 model, but I'm just wondering if there's some way to make sure and there's some due diligence.

## ChatGPT (2025-03-15T23:59:00.939118+00:00)

{"updates": [{"pattern": ".*", "replacement": "**Prompt for ChatGPT to Analyze and Summarize Patient Notes for a Psychiatrist**\n\n**Objective:**\nGenerate a structured, comprehensive, and easy-to-read summary for a psychiatrist based on the provided dictated notes. The summary should ensure clarity and conciseness while maintaining all essential details necessary for the psychiatrist to understand the patient’s experiences, symptoms, and past medical interactions.\n\n---\n\n**Context:**\n- The patient is seeking an ADD evaluation with a new psychiatrist outside of their current medical network (Kaiser).\n- The provided notes cover a broad range of experiences, including symptoms, daily life impact, medical interactions, external recommendations, and past treatments.\n- A portion of the notes details miscommunications with previous medical providers, but this represents only a fraction of the overall content. The summary should ensure this aspect is given appropriate weight without overshadowing the broader discussion of symptoms and concerns.\n- The summary should maintain a neutral tone while ensuring all key experiences, symptoms, and medical interactions are documented accurately.\n- The summary should be structured in an optimal way for a psychiatrist to process the information effectively.\n\n---\n\n**Instructions for Analysis and Structuring:**\n1. **Determine the Ideal Structure:**\n   - Assess whether the content is best presented in a chronological format or a symptom-first approach based on the provided notes.\n   - Consider a mix of structured sections (e.g., Symptoms, Impact, Medical History, External Opinions) or a well-organized narrative depending on what makes the most sense for clarity.\n\n2. **Key Content Considerations:**\n   - Extract the **most critical takeaways** for the psychiatrist to understand.\n   - Ensure all major symptoms and their real-world impact are captured in detail.\n   - Differentiate between medical opinions from various professionals where relevant.\n   - While past miscommunications with the medical team should be included, they should not dominate the summary—only provide the necessary context to support the broader assessment.\n   - If applicable, include a section outlining past treatments and their outcomes.\n\n3. **Formatting Guidelines:**\n   - Include a **TL;DR summary at the top** for quick reference.\n   - Use a structured format that is clear and digestible for a psychiatrist.\n   - If necessary, incorporate both direct quotes and paraphrased content, choosing the best approach for clarity.\n\n4. **Output Requirements:**\n   - Ensure all medical information is treated with the necessary depth and attention to detail.\n   - Provide a final summary that can be easily shared with a psychiatrist in a way that they can quickly grasp the patient’s history, current concerns, and the rationale for seeking an external evaluation.\n   - Maintain balance in addressing all aspects of the patient’s concerns, ensuring that no single topic (e.g., past miscommunications) disproportionately skews the focus of the summary.\n\n---\n\n**[Paste Notes Below]**"}]}

## ChatGPT (2025-03-15T23:59:14.955163+00:00)

I've adjusted the prompt to ensure that miscommunications with previous doctors are appropriately weighted without overshadowing the broader discussion of symptoms and concerns. This way, the summary remains balanced while still capturing all necessary details. Let me know if you need any further refinements!
