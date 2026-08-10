from bs4 import BeautifulSoup
import re

html_in = """
<div class="example">
  <p>The bar chart for this is drawn below:</p>
  <div class="chart-container">
    <canvas id="simpleBarChart"></canvas>
  </div>
  <script>
    const ctx_simpleBar = document.getElementById('simpleBarChart').getContext('2d');
  </script>
</div>
"""
soup = BeautifulSoup(html_in, 'html.parser')

visual_blocks = []
for container in soup.find_all(['div', 'canvas'], class_=lambda c: c in ['chart-container', 'chart-item', 'cg-mb-6'] if c else False):
    if container.name == 'canvas' and container.parent and container.parent.get('class') and any(c in container.parent.get('class') for c in ['chart-container', 'chart-item']):
        continue
    
    associated_script = container.find_next_sibling('script')
    
    placeholder_id = f"VISUAL_BLOCK_{len(visual_blocks)}"
    placeholder = BeautifulSoup(f'<div id="{placeholder_id}" class="visual-placeholder"></div>', 'html.parser').div
    
    visual_html = str(container)
    if associated_script:
        visual_html += "\n" + str(associated_script)
        associated_script.extract()
    
    visual_blocks.append((placeholder_id, visual_html))
    container.replace_with(placeholder)

print("--- Modified Soup ---")
print(str(soup))
print("--- Visual Blocks ---")
for pid, vhtml in visual_blocks:
    print(pid)
    print(vhtml)
