from bs4 import BeautifulSoup
import re

html_in = '<div id="VISUAL_BLOCK_0" class="visual-placeholder"></div>'
soup = BeautifulSoup(html_in, 'html.parser')
html_out = str(soup.div)
print("IN:", html_in)
print("OUT:", html_out)

regex = r'(<div class="visual-placeholder" id="VISUAL_BLOCK_\d+"></div>)'
print("Regex match on OUT?", bool(re.search(regex, html_out)))
