import glob
import re

for f in glob.glob('Sampling/Chapter*.html'):
    with open(f, encoding='utf-8') as file:
        text = file.read()
    
    matches = re.findall(r'<div class="hinglish-content">(.*?)</div>', text, flags=re.DOTALL)
    if matches:
        print(f"--- {f} ---")
        print(matches[0][:200].strip())
