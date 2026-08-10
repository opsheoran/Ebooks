from bs4 import BeautifulSoup
import re

html_in = """
<div class="example">
  <h4>Example Title</h4>
  <p>Some text here.</p>
  <div class="chart-container">
    <canvas id="c1"></canvas>
  </div>
  <script>const x = 1;</script>
</div>
"""

soup = BeautifulSoup(html_in, 'html.parser')

tags_to_translate = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'ul', 'ol', 'blockquote']

# We iterate over these tags and replace each with an english and hinglish version
for tag in soup.find_all(tags_to_translate):
    # Only translate tags that are NOT inside other translating tags (e.g. don't translate <li> if we are translating <ul>)
    # Actually, if we translate the whole <ul>, the <li>s go with it. So we should only grab top-level tags.
    if any(parent.name in tags_to_translate for parent in tag.parents):
        continue
        
    eng_tag = BeautifulSoup(str(tag), 'html.parser').contents[0]
    eng_tag['class'] = eng_tag.get('class', []) + ['english-content']
    
    hin_tag = BeautifulSoup(str(tag).replace('text', 'text_translated').replace('Title', 'Title Translated'), 'html.parser').contents[0]
    hin_tag['class'] = hin_tag.get('class', []) + ['hinglish-content']
    hin_tag['style'] = hin_tag.get('style', '') + '; display: none;'
    
    tag.insert_before(eng_tag)
    tag.insert_before(hin_tag)
    tag.decompose()

print(soup.prettify())
