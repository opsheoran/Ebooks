import os
import re

root_dir = r"E:\Theory of Sampling Singh and Chaudhary"
favicon_name = "favicon.svg"

count = 0
for subdir, dirs, files in os.walk(root_dir):
    if '.git' in subdir or '__pycache__' in subdir:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(subdir, file)
            
            rel_dir = os.path.relpath(root_dir, subdir)
            if rel_dir == '.':
                rel_favicon = f"./{favicon_name}"
            else:
                rel_favicon = f"{rel_dir}/{favicon_name}".replace('\\', '/')
                
            favicon_tag = f'\n    <link rel="icon" type="image/svg+xml" href="{rel_favicon}">'
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                if 'rel="icon"' not in content:
                    new_content = re.sub(r'(<head[^>]*>)', r'\1' + favicon_tag, content, count=1, flags=re.IGNORECASE)
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        count += 1
            except Exception as e:
                print(f"Failed to process {filepath}: {e}")

print(f"Added favicon to {count} files.")