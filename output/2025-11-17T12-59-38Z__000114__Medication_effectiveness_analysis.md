# Medication effectiveness analysis

## You (2025-11-17T12:59:38.211000+00:00)

help me create a good prompt. I'm using a customGPT which thinks like a psychiatrist so i don't need to define a persona. But I'm going to attach the following document and i need help with a few things. 

---

I need to get a better understanding of which medications work and which ones don't. And the ones that don't, why do they not work. What's the core reason for this shaking. Why we haven't seen any true progress yet. What do each of these medications do. What have the medications done to the patient (positive or negative). And based on historical evidence, what might be the best combination of medications and why. 

For additional context, the last doctor - doctor jyothirmayi, has a history of carelessly reducing medications. I do not want to go to her becuase she has multiple conflicts of interests - based on several patterns observed, we believe that she wants my mother to be hospitalized in a specific clinic that has financial ties with this doctor. 

We need help understanding the ideal combination of medications.

## ChatGPT (2025-11-17T12:59:39.994241+00:00)

Thanks for the clarity and for sharing the document. You’ve already framed several layered questions rooted in clinical and psychiatric reasoning, so let’s take a moment to organize the analytic dimensions before we “begin creating the prompt.”

To confirm: your target is a **CustomGPT with a psychiatrist persona**, and the goal is to obtain **a deep clinical and pharmacological analysis** of medication efficacy, treatment history, side effects (particularly tremors), and an evidence-informed recommendation for an optimal medication combination. Here's a breakdown of what you've implicitly embedded, which I’ll soon help you structure explicitly:

---

### 🧠 ANALYTICAL INTENT — what you're trying to understand:
- **Effectiveness analysis**: Which medications have worked, and which haven’t—based on real-world behavioral observations.
- **Mechanistic insight**: Why certain medications might not work (especially in this case)—pharmacological or diagnostic misfit, treatment resistance, adherence breakdowns, etc.
- **Side-effect causality**: What’s driving the **shaking / tremors**—drug-induced (EPS or TD?), disease-related, or due to polypharmacy mismanagement?
- **Historical synthesis**: Across the multi-year timeline, what are the core patterns in medication outcomes?
- **Optimized plan suggestion**: Given everything, what **medication combination** is most justifiable based on psychiatric rationale, patient history, and side effect profile?

---

### ⚠️ CRITICAL GUARDRAILS:
- You're **not asking for diagnosis**, but for an **evidence-based comparative reasoning process** over the history.
- You want the CustomGPT to **clearly distinguish speculation from what’s grounded in observable evidence** (e.g., hallucinations were never present → so avoid overprescribing for that).
- There’s **a known doctor conflict (Dr. Jyothirmayi)**. While she’s still involved, the CustomGPT must treat her recommendations **critically**, not as default authority.

---

### 📚 CONTEXTUAL FOUNDATIONS:
- The patient (Suparna) has **schizophrenia without hallucinations**, marked by paranoia, control behaviors, isolation, and **extreme food-related delusions**.
- Tremors **emerged or worsened after changes in 2025**, especially around **Risperidone/Paliperidone** and after **US medication simplification**.
- Medication adherence has been fragile—often forced or sabotaged.
- There's **clear evidence of extrapyramidal side effects**, potentially evolving into **Tardive Dyskinesia**.
- Pacitane (Trihexyphenidyl) and Betacap (Propranolol) have been added at various stages to manage motor side effects, with **limited success**.
- New psychiatrists (e.g. Dr. Praveen) offered structure but not symptom relief.
- Patient trust is easily broken, especially when **doctors ignore tremors**.

---

Before we **begin creating the prompt**, would you like to:
1. Emphasize medication **mechanism of action and matching** to symptoms?
2. Include exploration of **non-pharmacological interventions**?
3. Have the model offer a **ranked or tiered recommendation plan** (e.g., first-line combo vs backup)?
4. Include concerns about **hospitalization pressure** or medical ethics?

Let me know if you’d like to explore any of these, or if you're ready to proceed with:  
**“Begin creating the prompt.”**

## You (2025-11-17T13:02:34.716000+00:00)

additionally we want a deeper understanding of the medications. I want this GPT to do a thorough breakdown of the actual medications. I also need it to refer to some medical research or documentation. 

begin creating the prompt.

## ChatGPT (2025-11-17T13:02:36.310420+00:00)

Excellent. Based on your inputs, here is the final **structured reasoning prompt** tailored for your psychiatrist-oriented CustomGPT, incorporating all dimensions of analysis, critical context, and guardrails for clinical accuracy and ethical alignment.

---

## ✅ Final Structured Prompt for Psychiatrist CustomGPT

### **🧭 Goal**
Analyze and evaluate the longitudinal psychiatric medication history of Suparna Goyal, with the objective of determining:
1. Which medications have demonstrably worked or failed, and why.
2. The underlying pharmacological or diagnostic reasons behind the persistent tremors (EPS, TD, or otherwise).
3. The mechanism of action and clinical rationale of each medication used—both successful and unsuccessful.
4. The psychological, behavioral, and motor impact of each treatment phase.
5. An optimal, evidence-supported recommendation for a medication regimen, based on the historical evidence and best psychiatric practices for treatment-resistant schizophrenia with severe delusional dietary control and poor adherence.

---

### **📦 Return Format**
- **Section 1: Chronological Efficacy Matrix**  
  Table summarizing each treatment phase with:
  - Date range  
  - Medication(s) & dosages  
  - Observed benefits  
  - Observed side-effects  
  - Notable behavioral changes  
  - Adherence status  

- **Section 2: Medication Mechanism Overview**  
  For each drug (e.g. Olanzapine, Risperidone, Paliperidone, Aripiprazole, Pacitane, Betacap, Nexito):
  - Drug class  
  - Mechanism of action  
  - Primary therapeutic role in schizophrenia or related conditions  
  - Common side-effects, especially extrapyramidal symptoms  
  - Pharmacodynamic or pharmacokinetic interactions with other drugs used  
  - Citations or references to relevant medical literature (e.g., NIH, PubMed, WHO, peer-reviewed psychiatric journals)

- **Section 3: Root Cause Analysis of Tremors**  
  - Timeline of tremor onset vs medication changes  
  - Evaluate likelihood of **acute vs tardive extrapyramidal symptoms**  
  - Clinical interpretation of Pacitane and Betacap effectiveness  
  - Potential irreversible neuroleptic-induced changes  
  - Judgment on which drug(s) most likely contributed to or worsened the tremors, supported by mechanism and research

- **Section 4: Ethical & Treatment Context Review**  
  - Note family’s documented concern about **Dr. Jyothirmayi**, including suspected conflict of interest with a specific clinic  
  - Evaluate any patterns of **careless dose reductions** or **inadequate monitoring of motor side effects**  
  - Caution against over-reliance on providers with known trust violations

- **Section 5: Treatment Recommendation Plan**  
  - Clear, layered recommendation:  
    - **Primary regimen** – based on best clinical evidence and this patient’s history  
    - **Contingency/backup options** – in case of side-effects or poor response  
  - If appropriate, recommend long-acting vs short-acting options  
  - Include realistic management strategies for adherence, given patient’s history of deception and resistance  
  - List **any labs, monitoring, or assessments** that should accompany the plan (e.g., AIMS scale for TD, thyroid tests)

---

### **⚠️ Warnings & Guardrails**
- Avoid assumptions unsupported by the clinical history provided.  
- Clearly **distinguish speculation from evidence** (e.g., hallucinations have *not* been reported—don’t overweigh antipsychotics for that symptom).  
- Maintain neutrality regarding psychiatrist intentions—report observed patterns, not motives.  
- Do not prescribe—this is a clinical reasoning task for educational or preparatory purposes only.  
- Patient has historically demonstrated extreme control behaviors, dietary delusions, and poor insight—medication effectiveness should be judged **behaviorally and relationally**, not just via internal symptom reports.

---

### **📚 Context & Additional Elements**
- Patient: Suparna Goyal  
- Diagnosis: Schizophrenia (no hallucinations, prominent paranoia, dietary delusions, intermittent aggression)  
- History of extreme **isolation, fasting, controlling behaviors**, and **involuntary physical symptoms (tremors)**.  
- Timeline of all medications, behaviors, and regressions is documented in detail.  
- Family has taken over care coordination and is seeking an evidence-based synthesis and treatment optimization.  
- You are a **psychiatrist** interpreting this history with the lens of psychopharmacology, patient safety, and adherence psychology.  
- Refer to real-world psychiatric and pharmacological research where appropriate.

---

Would you like this prompt adapted into a downloadable note, or inserted into the CustomGPT as-is?

