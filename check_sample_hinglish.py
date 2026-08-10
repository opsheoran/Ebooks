import re
html = open('Stat-102/Unit-II - smple.html', encoding='utf-8').read()
matches = re.findall(r'<div class="hinglish-content".*?>(.*?)</div>', html, re.DOTALL)
if matches:
    print(matches[0][:2000])
else:
    print("No hinglish-content found in Stat-102/Unit-II - smple.html")
