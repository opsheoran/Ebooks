import re
html = open('Stat-101/Unit-II.html', encoding='utf-8').read()
matches = re.findall(r'<span class="nav-num">(2\.1[23]\.\d+)</span>', html)
print("Subheadings under 2.12 or 2.13:", matches)
