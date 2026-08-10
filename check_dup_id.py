import re
html = open('Stat-101/Unit-II.html', encoding='utf-8').read()
matches = re.finditer(r'<[^>]*?id="properties"[^>]*?>', html)
for m in matches:
    print(m.group(0))
