from bs4 import BeautifulSoup
html_str = 'Some text <div class="visual-placeholder" id="VISUAL_BLOCK_0"></div> more text'
soup = BeautifulSoup(html_str, 'html.parser')
print(str(soup))
