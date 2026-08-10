import re
with open('Sampling/Chapter3.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'<div class="hinglish-content">(.*?)</div>\s*</section>', text, flags=re.DOTALL)
for i, m in enumerate(matches):
    content = m.group(1).strip()
    print(f"Hinglish Section {i+1}: {content[:100]} ...")
