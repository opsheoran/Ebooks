import re
from bs4 import BeautifulSoup

visual_blocks = []
section_html = '<div class="body"><p>Test</p><canvas id="c1"></canvas></div>'
section = BeautifulSoup(section_html, 'html.parser').div

for visual in section.find_all(['canvas', 'div'], class_=lambda c: c in ['chart-container', 'chart-item', 'cg-mb-6'] if c else False):
    placeholder_id = f"VISUAL_BLOCK_{len(visual_blocks)}"
    placeholder = BeautifulSoup(f'<div id="{placeholder_id}" class="visual-placeholder"></div>', 'html.parser').div
    
    visual_html = str(visual)
    visual_blocks.append((placeholder_id, visual_html))
    visual.replace_with(placeholder)

eng_html_raw = "".join([str(child) for child in section.children])
hin_html_raw = eng_html_raw # Mock translation

eng_parts = re.split(r'(<div class="visual-placeholder" id="VISUAL_BLOCK_\d+"></div>)', eng_html_raw)
hin_parts = re.split(r'(<div class="visual-placeholder" id="VISUAL_BLOCK_\d+"></div>)', hin_html_raw)

print(eng_parts)

section_content = ""
for i in range(min(len(eng_parts), len(hin_parts))):
    part_eng = eng_parts[i]
    part_hin = hin_parts[i]

    match = re.match(r'<div class="visual-placeholder" id="(VISUAL_BLOCK_\d+)"></div>', part_eng)
    if match:
        print("MATCHED", match.group(1))
        placeholder_id = match.group(1)
        vis_html = next(html for p_id, html in visual_blocks if p_id == placeholder_id)
        section_content += f'<div class="shared-visual">{vis_html}</div>\n'
    elif part_eng.strip():
        print("DID NOT MATCH:", part_eng)
        section_content += f'<div class="english-content">{part_eng}</div>\n'
        section_content += f'<div class="hinglish-content" style="display:none;">{part_hin}</div>\n'
        
print(section_content)
