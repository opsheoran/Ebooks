import re

with open('common_style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add import
import_stmt = "@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+Devanagari:wght@400;500;600;700&display=swap');\n"
if "Noto+Serif+Devanagari" not in css:
    css = import_stmt + css

# Update .hinglish-content
old_hinglish = ".hinglish-content { display: none; }"
new_hinglish = """.hinglish-content { display: none; font-family: 'Noto Serif Devanagari', 'Source Serif 4', serif; font-size: 1.05rem; }
.hinglish-content h2, .hinglish-content h3, .hinglish-content h4 { font-family: 'Noto Serif Devanagari', 'Playfair Display', serif; }"""

css = css.replace(old_hinglish, new_hinglish)

with open('common_style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Added Noto Serif Devanagari to common_style.css")
