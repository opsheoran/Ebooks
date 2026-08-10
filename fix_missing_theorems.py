import re
import glob

def fix_theorems():
    for filepath in glob.glob("Sampling/Chapter*.html"):
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()

        # Fix <h3><strong>Theorem X.Y.Z</strong></h3>
        # Followed by potentially some text or just a math formula
        # Let's just find <h3><strong>Theorem(.*?)</strong></h3>\s*<p>(.*?)</p>
        # And <p><strong>Theorem(.*?)</strong></p> (without colon)
        
        # 1. <h3><strong>Theorem X</strong></h3>\n<p>text</p>
        html = re.sub(r'<h3><strong>Theorem([^<]+)</strong></h3>\s*<p>(.*?)</p>', r'<div class="theorem"><h4>Theorem\1</h4><p>\2</p></div>', html, flags=re.DOTALL)
        
        # 2. <p><strong>Theorem X:</strong> text</p> was handled, what about <p><strong>Theorem:</strong> text</p>
        html = re.sub(r'<p><strong>Theorem:</strong>(.*?)</p>', r'<div class="theorem"><h4>Theorem</h4><p>\1</p></div>', html, flags=re.DOTALL)
        
        # 3. <p><strong>Theorem([^<]+)</strong>(.*?)</p>
        # Sometimes there's no colon
        html = re.sub(r'<p><strong>Theorem\s+([0-9\.]+)\s*</strong>(.*?)</p>', r'<div class="theorem"><h4>Theorem \1</h4><p>\2</p></div>', html, flags=re.DOTALL)
        
        # 4. Same for Examples, Corollaries, Definitions if they missed the colon
        html = re.sub(r'<h3><strong>Example([^<]+)</strong></h3>\s*<p>(.*?)</p>', r'<div class="example"><h4>Example\1</h4><p>\2</p></div>', html, flags=re.DOTALL)
        html = re.sub(r'<p><strong>Example\s+([0-9\.]+)\s*</strong>(.*?)</p>', r'<div class="example"><h4>Example \1</h4><p>\2</p></div>', html, flags=re.DOTALL)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Fixed remaining theorems in {filepath}")

fix_theorems()
