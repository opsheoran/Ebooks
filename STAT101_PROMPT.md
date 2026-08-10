# PROMPT FOR GENERATING STAT-CC-101 UNITS

## Objective
Generate the complete, responsive HTML files for STAT-M-101 (Statistical Methods-I) based on the provided syllabus and original HTML chapters. The output must strictly mimic the styling, structure, and interactive features of `Stat-CC-102/Unit-II.html`, while retaining the **100% verbatim depth** of the original STAT-CC-101 English content.

---

## 1. Content Preservation & Depth (Strict Verbatim)
- **Zero Simplification:** Extract and use the exact, verbatim English text, tables, data, and examples from the original `Stat-CC-101/Chapter*.html` files. **Do not summarize, shorten, or simplify the text.**
- **All Sections Included:** Include every single subheading, example (e.g., NSSO surveys, Haryana water quality, crop yields), and mathematical derivation exactly as presented in the original files.
- **Textbook Tone:** Maintain a professional Indian English textbook standard. Remove casual conversational greetings (e.g., "Hello students, welcome to...").

## 2. True "Hinglish" Translation Standard
- **Dual Content Architecture:** Every theory section and exercise must have an `<div class="english-content">` and a corresponding `<div class="hinglish-content" style="display:none;">`.
- **Hinglish vs. Pure Hindi:** The Hinglish translation MUST NOT be pure API-generated Hindi. It must be a sophisticated, conversational blend that uses formal Hindi grammar (in Devanagari script) but retains English technical terms.
- **Rule for Technical Terms:** All statistical terms, mathematical variables, and dataset names MUST remain in English.
- **Gold Standard Example:** You MUST emulate this exact style of Hinglish:
  > *"चूँकि बिना replacement के sampling के मामले में effective sample size स्वाभाविक रूप से replacement के साथ sampling की तुलना में गणितीय रूप से बड़ा होने की उम्मीद है, इसलिए बिना replacement के की गई rigorous sampling, replacement के साथ sampling की तुलना में मजबूती से एक अधिक efficient estimator प्रदान कर सकती है। Varying probabilities (wor) के साथ sampling के कठिन क्षेत्र में गणितीय कार्य की एक विशाल मात्रा व्यापक रूप से की गई है, लेकिन दुर्भाग्य से, अधिकांश theoretical procedures बहुत जटिल हैं और बड़े पैमाने पर field surveys में कड़ाई से आसानी से लागू नहीं होती हैं।"*

## 3. UI, Structure & Styling (Stat-CC-102 Mimicry)
- **Header Toggle Button:** A "Switch Language (Hinglish)" / "Switch Language (English)" button must be placed strictly in the **top right corner of the chapter header card** (`.chapter-header`).
- **Sidebar Navigation:** The sidebar must include exact links to every verbatim section heading, plus the 4 exercise categories. It must smoothly switch between `.topic-section` divs without causing blank screens.
- **Base CSS:** Utilize the provided CSS variables, fonts (Playfair Display, Source Serif 4, DM Sans), and component styles from the `Stat-CC-102` template.

## 4. Exercise Section Standards
- **Quantity:** Exactly 110 interactive questions per unit: 30 MCQs, 30 Fill-in-the-blanks, 30 True/False, and 20 Subjective questions.
- **Subjective Questions:** Must include practical, data-based, and scenario-based problems.
- **Exact Stat-CC-102 CSS:** You MUST use the exact classes for exercises: `.question`, `.mcq-options`, `.toggle-btn`, and `.answer`.
- **Interactive Toggle:** Each question must have a button reading `"Show Answer ▼"` that toggles the `.answer` div and changes to `"Hide Answer ▲"`. Do not use external APIs to fetch answers.
- **MCQ Format:** Do not use HTML radio buttons. Format options horizontally inside a `<p>` tag as `(a) ... (b) ... (c) ... (d) ...`.
- **Hinglish Exercises:** The exercises must also exist inside both the `english-content` and `hinglish-content` divs, strictly following the True Hinglish standard defined above.

---

## 5. Execution Format
When processing or generating the files, you must strictly follow this input/output workflow:
**Input:** Full HTML block with both English and Hinglish sections.
**Output:** Same HTML block, but the Hinglish section MUST be rewritten in the correct True Hinglish style defined above. Do not alter the English section, and do not break the HTML structure.

---
*End of Prompt Instructions*