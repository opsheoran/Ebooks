from bs4 import BeautifulSoup
import re

with open('Stat-101/Chapter2.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

section = soup.find(id='simple-bar-chart')
if section:
    print(section.prettify()[:2000])
else:
    print("Section not found")
