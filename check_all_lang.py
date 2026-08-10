import glob
import re

for f in glob.glob('Sampling/Chapter*.html'):
    with open(f, encoding='utf-8') as file:
        text = file.read()
    
    matches = re.findall(r'<div class="hinglish-content">(.*?)</div>\s*</section>', text, flags=re.DOTALL)
    if len(matches) > 1:
        print(f"--- {f} ---")
        print(matches[1][:150].strip())
