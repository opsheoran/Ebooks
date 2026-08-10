import glob
import re

def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Move <button class="lang-toggle-btn"...> from before <div class="chapter-header"> to inside it.
    
    # First, let's find the button
    btn_pattern = r'<button class="lang-toggle-btn"[^>]*>Switch to Hinglish</button>'
    btn_match = re.search(btn_pattern, html)
    
    if btn_match:
        btn_html = btn_match.group(0).strip()
        # Remove it from wherever it is currently
        html = re.sub(btn_pattern + r'\s*', '', html)
        
        # Insert it right after <div class="chapter-header">
        ch_header_pattern = r'(<div class="chapter-header">)'
        if re.search(ch_header_pattern, html):
            html = re.sub(ch_header_pattern, r'\1\n    ' + btn_html, html, count=1)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Moved lang-toggle-btn into chapter-header for {filepath}")
        else:
            print(f"Could not find chapter header in {filepath}")
    else:
        print(f"Could not find button in {filepath}")

for filepath in glob.glob("Sampling/Chapter*.html"):
    process_file(filepath)
