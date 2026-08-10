import glob
import re

for filepath in glob.glob("Sampling/Chapter*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Remove inline style from the lang-toggle-btn so that the common_style.css absolute positioning works
    html = re.sub(r'<button class="lang-toggle-btn" onclick="toggleLanguage\(\)"[^>]*>', 
                  '<button class="lang-toggle-btn" onclick="toggleLanguage()">Switch to Hinglish</button>', html)

    # 2. Convert MathJax \quad (X.Y.Z) to \tag{X.Y.Z}
    # For example: \[ V(\bar{y}) = \dots \quad (2.3.1) \] -> \[ V(\bar{y}) = \dots \tag{2.3.1} \]
    html = re.sub(r'\\quad\s*\(([^)]+)\)\s*\\\]', r'\\tag{\1} \]', html)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Fixed {filepath}")
