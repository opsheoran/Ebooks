# Project Guidelines & Memory

## True Hinglish Translation Standard
When generating Hinglish content, strictly adhere to the following style:
- **Hindi Grammar + English Technical Terms:** Use formal Hindi grammar (in Devanagari script) but rigorously maintain ALL statistical, mathematical, and technical terms in English.
- **No Pure Hindi Translation:** Do NOT use automated translation APIs that convert everything to pure Hindi (e.g., never translate "Statistics" to "सांख्यिकी" or "Sampling" to "प्रतिचयन").
- **Gold Standard Example:**
  > "चूँकि बिना replacement के sampling के मामले में effective sample size स्वाभाविक रूप से replacement के साथ sampling की तुलना में गणितीय रूप से बड़ा होने की उम्मीद है, इसलिए बिना replacement के की गई rigorous sampling, replacement के साथ sampling की तुलना में मजबूती से एक अधिक efficient estimator प्रदान कर सकती है। Varying probabilities (wor) के साथ sampling के कठिन क्षेत्र में गणितीय कार्य की एक विशाल मात्रा व्यापक रूप से की गई है, लेकिन दुर्भाग्य से, अधिकांश theoretical procedures बहुत जटिल हैं और बड़े पैमाने पर field surveys में कड़ाई से आसानी से लागू नहीं होती हैं।"

## Stat-CC-101 / Stat-CC-102 Formatting Rules
- **Verbatim Content:** Use the exact text from the original source files. Do not summarize or simplify the depth of the explanations or examples.
- **Textbook Tone:** Do not use conversational greetings (e.g., "Hello students").
- **Exercise Structure:** Exercises must exactly mimic the `Stat-CC-102` template using `.question`, `.mcq-options`, `.toggle-btn`, and `.answer` classes, with a "Show Answer ▼" toggle button.
- **Hinglish Toggle:** Place a "Switch Language (Hinglish)" / "Switch Language (English)" toggle button in the top right corner of the chapter header card.