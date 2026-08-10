import re

file_path = 'Sampling/Chapter7.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We want to ensure that multiple inline equations \( ... \) inside a derivation-block are separated by <br>.
# Or even better, just wrap each \( ... \) inside a derivation block with a <div>...</div> to make them block level.
# Actually, the user says "be uniform in css use \(...\)". 
# Let's just find all derivation-blocks and add <br> before every \( except the first one on a line.
# A simpler way: inside a derivation-block, if a line has \( ... \) and there is another line with \( ... \), we should put <br>
# Let's replace each \( ... \) with <div class="math-line">\( ... \)</div>

def process_block(match):
    block_content = match.group(1)
    # Wrap every \( ... \) in <div class="math-line">
    new_block_content = re.sub(r'(\\\(.*?\\\))', r'<div style="padding: 5px 0;">\1</div>', block_content, flags=re.DOTALL)
    return f'<div class="derivation-block">{new_block_content}</div>'

new_content = re.sub(r'<div class="derivation-block">(.*?)</div>', process_block, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Applied math-line wrappers inside derivation blocks.")
