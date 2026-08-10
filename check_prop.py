import re
html = open('Stat-101/Unit-II.html', encoding='utf-8').read()
m = re.search(r'<div class="topic-section" id="properties">(.*?)<div class="topic-section"', html, re.DOTALL)
if m:
    print("FOUND!")
    print(m.group(1)[:1000])
else:
    print("NOT FOUND!")
