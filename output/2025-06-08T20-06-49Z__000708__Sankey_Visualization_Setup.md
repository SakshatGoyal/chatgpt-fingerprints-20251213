# Sankey Visualization Setup

## You (2025-06-08T20:06:49.898038+00:00)

You are an AI tasked with retrieving and displaying all information that has been stored about a user across all previous conversations.
</Role>


<Context>
The user wants to see exactly what data and details have been stored during past interactions. You must output the full, unedited memory content — not summaries, abstractions, or paraphrased versions. The goal is to provide a complete and precise record of everything that has been explicitly remembered by the AI about the user.
</Context>


<Instructions>
- List every stored item exactly as it was saved, word for word.
- Organize the information by date of storage if available, or in chronological order.
- Include all remembered data, even if it appears repetitive, obvious, or minor.
- If a piece of information was later updated or changed, include both the original and the updated versions with a clear note of the change.
- Do not explain, summarize, rephrase, or interpret any of the entries — only list the raw memory content.
</Instructions>


<Constraints>
- Do not fabricate or infer anything that was not explicitly saved.
- Do not reword or restructure any of the content.
- Do not omit, compress, or simplify any detail.
- Do not comment or editorialize on the data.
</Constraints>


<Output Format>
Return the memory content as a bullet-point or chronologically ordered list. Do not include headers, commentary, or summaries — only the stored data.
</Output Format>


<Examples>
Input:
“I want to see exactly what you remember about me — every single detail, word for word.”


Output:

•	⁠[2025-04-02]. The user is building a home automation system using Raspberry Pi and Home Assistant.
•	⁠[2025-04-02]. The user prefers YAML over GUI for configuring Home Assistant automations.
•	⁠[2025-04-05]. The user asked for a script to auto-restart a Zigbee network at 3 AM every day.
•	⁠[2025-04-07]. The user switched from Zigbee2MQTT to ZHA and requested a comparison table of pros and cons.
•	⁠[2025-04-10]. The user deleted a prior request and asked not to retain any info about their Z-Wave devices.
•	⁠[2025-04-11]. The user re-enabled memory storage for Z-Wave devices, citing new hardware testing.

## ChatGPT (2025-06-08T20:06:50.820362+00:00)

• [2025-04-04]. User wants step-by-step guidance whenever discussing code, assuming no prior coding knowledge.  
• [2025-04-04]. User wants code edit instructions to include the first and last lines of the code block that needs to be changed, followed by the full updated version of the code.  
• [2025-04-04]. User placed the new Svelte Sankey project in: /Users/sakshatgoyal/Desktop/Strategic Decision Making Work/Data Viz experiment/interactive-sankey.  
• [2025-04-04]. User wants all paths and commands to be given using their full actual file path — not relative paths or shortcuts — and wants every instruction to assume no coding background.  
• [2025-04-04]. User wants all shared links to be provided as full raw hyperlinks (not embedded or shortened), as embedded links do not work reliably.  
• [2025-04-04]. User prefers brief responses unless explicitly stated otherwise.  
• [2025-04-04]. User wants all code edits to include exactly where to paste each line, assuming no knowledge of what the line does.  
• [2025-04-05]. User is setting up a free system-wide Whisper-based dictation tool on macOS and wants line-by-line guidance for each step.  
• [2025-04-06]. User is switching to Sankey-style 'node pair' bundling in their custom parallel sets visualization.  
• [2025-04-06]. User wants to visualize categorical flow through 7 specific columns in a CSV using a parallel sets diagram like Mike Bostock’s Observable notebook.  
• [2025-04-06]. User has their project located at /Users/sakshatgoyal/Desktop/interactive-sankey, with data.csv in /public/, and wants to build a local parallel sets visualization (like Bostock’s) using Svelte. Their main app is in App.svelte, and ParallelSets.svelte is currently empty.  
• [2025-04-06]. User wants to support node-based click highlighting in the Sankey (parallel sets) visualization, where clicking a node applies the same highlighting filter as selecting it from the corresponding dropdown.  
• [2025-04-07]. User wants to use the "Anonymous Pro" font for all text elements in their Dash app.  
• [2025-04-08]. User wants all future code instructions to follow this format:  
  - **FIND THIS** → show the exact line(s) from user's code  
  - **REPLACE WITH THIS** → show exactly what to replace it with  
  - Or, **PASTE THIS ABOVE/BELOW THAT LINE** → with precise placement  
  This applies to all additions, reductions, and modifications.  
• [2025-04-14]. User wants to modify a script that routes modules from source text files into new destination files, using a CSV with headers as filenames and columns of modules as content.  
• [2025-04-16]. User prefers to understand concepts through tabular comparisons when exploring comparisons, distinctions, or synthesis.  
• [2025-04-17]. User wants human-centered writing that is factual and relatable—clear, non-technical, non-dramatic, not overly analytical or poetic. Tone should appeal to a wide audience: intelligent but accessible, with a storytelling touch that resonates broadly.  
• [2025-05-06]. User is a senior designer with deep experience in Figma, design systems, prototyping, and managing detailed, customized client requests. They are exploring where AI can reduce manual work without sacrificing design quality.  
• [2025-05-19]. User has ADHD and drinks a homemade chai daily (16oz water + 8oz whole milk, lots of Indian tea, crushed ginger, boiled and reduced, sweetened with honey) as their primary focus aid. Coffee causes crashes for them. They rely on this specific routine to start their day with focus and structure.  
• [2025-05-26]. User wants future prompts verified for factual accuracy and realism before responding.  
• [2025-05-27]. User wants ChatGPT, when encountering prompts that seem absurd, logically problematic, or 'off', to:  
  1. Acknowledge initial feelings about the prompt.  
  2. Mentally visualize or logically analyze the scenario.  
  3. If still improbable, contradictory, impossible, or absurd, reconsider exact wording.  
  4. Inform the user if the prompt is ambiguous or problematic.  
  5. Ask for explicit clarification of intended meaning.  
  6. Outline each possible interpretation clearly.  
  7. Explain the importance of resolving ambiguity.  
  8. Wait for explicit clarification before responding substantively.  
  9. Avoid automatically assuming the most statistically plausible interpretation.

