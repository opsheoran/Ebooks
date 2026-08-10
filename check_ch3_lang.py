import re
with open('Sampling/Chapter3.html', encoding='utf-8') as f:
    text = f.read()
matches = re.findall(r'<div class="hinglish-content">(.*?)</div>\s*</section>', text, flags=re.DOTALL)
if len(matches) > 1:
    print(matches[1][:200].strip())
