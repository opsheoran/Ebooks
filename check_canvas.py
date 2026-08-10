import re
html = open('Stat-101/Unit-II.html', encoding='utf-8').read()
# Let's see the content around 'simpleBarChart'
idx = html.find('simpleBarChart')
if idx != -1:
    print(html[max(0, idx-500) : min(len(html), idx+500)])
else:
    print("simpleBarChart NOT FOUND")
