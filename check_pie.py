import re
with open('Stat-101/Unit-II.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<div class="topic-section" id="pie-diagrams">(.*?)</div>\s*<div class="topic-section"', html, re.DOTALL)
if m:
    print(m.group(0))
else:
    print("Section pie-diagrams not found")
