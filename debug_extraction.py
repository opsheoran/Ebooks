from bs4 import BeautifulSoup
import re

with open('Stat-101/Chapter2.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

visual_blocks = []
section = soup.find(id='simple-bar-chart')

for visual in section.find_all(['canvas', 'div'], class_=lambda c: c in ['chart-container', 'chart-item', 'cg-mb-6'] if c else False):
    if visual.name == 'canvas':
        if visual.parent and visual.parent.get('class') and any(c in visual.parent.get('class') for c in ['chart-container', 'chart-item']):
            continue
    placeholder_id = f"VISUAL_BLOCK_{len(visual_blocks)}"
    placeholder = BeautifulSoup(f'<div id="{placeholder_id}" class="visual-placeholder"></div>', 'html.parser').div
    
    visual_html = str(visual)
    visual_blocks.append((placeholder_id, visual_html))
    visual.replace_with(placeholder)

eng_html_raw = "".join([str(child) for child in section.children])
print("--- RAW HTML ---")
print(eng_html_raw)

eng_parts = re.split(r'(<div class="visual-placeholder" id="VISUAL_BLOCK_\d+"></div>)', eng_html_raw)
print(f"Split count: {len(eng_parts)}")
