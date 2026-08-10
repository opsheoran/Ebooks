import re
html = open('Stat-101/Unit-II.html', encoding='utf-8').read()
matches = re.findall(r'<div class="shared-visual">(.*?)</div>\s*(?:<div class="english-content">|</section>)', html, re.DOTALL)
if matches:
    print(matches[0])
