import glob
import re

css_link = '<link rel="stylesheet" href="../common_style.css">'

for file_path in glob.glob('Sampling/Chapter*.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already linked
    if css_link in content:
        print(f"Skipping {file_path}, already linked.")
        continue
        
    # Replace <style>...</style> with the link
    # We will find the closing </head> and put the link right before it, 
    # and remove the <style>...</style> block completely.
    new_content = re.sub(r'<style>.*?</style>', css_link, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated CSS in {file_path}")
