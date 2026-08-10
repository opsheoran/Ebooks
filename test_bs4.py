import re
from bs4 import BeautifulSoup

html = '<div id="VISUAL_BLOCK_0" class="visual-placeholder"></div>'
soup = BeautifulSoup(html, 'html.parser')
print(str(soup.div))
