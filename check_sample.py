import re
html = open('Stat-101/Unit-II - smple.html', encoding='utf-8').read()
m = re.search(r'<div class="example">.*?</canvas>', html, re.DOTALL)
if m:
    print(m.group(0))
else:
    print("Not found")
