import re
html = open('Stat-101/Unit-II.html', encoding='utf-8').read()
links = re.findall(r'<a class="nav-link" href="#(.*?)"', html)
print(links)
