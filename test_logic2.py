import re
from bs4 import BeautifulSoup

visual_blocks = []
section_html = '<div class="body"><p>Test</p><div class="chart-container"><canvas id="c1"></canvas></div></div>'
section = BeautifulSoup(section_html, 'html.parser').div

for visual in section.find_all(['canvas', 'div'], class_=lambda c: c in ['chart-container', 'chart-item', 'cg-mb-6'] if c else False):
    placeholder_id = f"VISUAL_BLOCK_{len(visual_blocks)}"
    placeholder = BeautifulSoup(f'<div id="{placeholder_id}" class="visual-placeholder"></div>', 'html.parser').div
    
    visual_html = str(visual)
    visual_blocks.append((placeholder_id, visual_html))
    visual.replace_with(placeholder)

eng_html_raw = "".join([str(child) for child in section.children])
hin_html_raw = eng_html_raw # Mock translation

print("eng_html_raw:", eng_html_raw)

eng_parts = re.split(r'(<div class="visual-placeholder" id="VISUAL_BLOCK_\d+"></div>)', eng_html_raw)
hin_parts = re.split(r'(<div class="visual-placeholder" id="VISUAL_BLOCK_\d+"></div>)', hin_html_raw)

print(eng_parts)
