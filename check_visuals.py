import re
html = open('Stat-101/Unit-II.html', encoding='utf-8').read()
matches = re.findall(r'<div class="shared-visual">(.*?)</div>', html, re.DOTALL)
for i, m in enumerate(matches[:2]):
    print(f"--- MATCH {i} ---")
    print(m)
