from bs4 import BeautifulSoup
import re

html_in = '<div class="visual-placeholder" id="VISUAL_BLOCK_0"></div>'
soup = BeautifulSoup(html_in, 'html.parser')
html_out = str(soup)
print("IN:", html_in)
print("OUT:", html_out)

print("Split IN:", len(re.split(r'(<div class="visual-placeholder" id="VISUAL_BLOCK_\d+"></div>)', html_in)))
print("Split OUT:", len(re.split(r'(<div class="visual-placeholder" id="VISUAL_BLOCK_\d+"></div>)', html_out)))
