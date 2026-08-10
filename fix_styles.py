import re
import glob

def process_file(filepath):
    print(f"Processing styles in {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. derivation-block to derivation
    html = html.replace('class="derivation-block"', 'class="derivation"')

    # 2. explanation to proof-step
    html = html.replace('class="explanation"', 'class="proof-step"')

    # 3. formula boxes
    # <div style="padding: 5px 0;">\( ... \)</div> -> <div class="formula-box">\[ ... \]</div>
    html = re.sub(r'<div style="padding:\s*5px\s*0;?">\s*\\\(\s*(.*?)\s*\\\)\s*</div>', r'<div class="formula-box">\[ \1 \]</div>', html, flags=re.DOTALL)
    
    # <div style="padding: 5px 0;">$$ ... $$</div> -> <div class="formula-box">\[ ... \]</div>
    html = re.sub(r'<div style="padding:\s*5px\s*0;?">\s*\$\$\s*(.*?)\s*\$\$\s*</div>', r'<div class="formula-box">\[ \1 \]</div>', html, flags=re.DOTALL)

    # 4. Theorems
    # Type 1: <p><strong>Theorem 1.1:</strong> text</p>
    html = re.sub(r'<p><strong>Theorem\s+([^:]+):</strong>(.*?)</p>', r'<div class="theorem"><h4>Theorem \1</h4><p>\2</p></div>', html)
    # Type 2: <h3><strong>Theorem 1.1:</strong></h3>\s*<p>text</p>
    html = re.sub(r'<h3><strong>Theorem\s+([^:]+):</strong></h3>\s*<p>(.*?)</p>', r'<div class="theorem"><h4>Theorem \1</h4><p>\2</p></div>', html, flags=re.DOTALL)

    # 5. Examples
    # Type 1: <p><strong>Example 1.1:</strong> text</p>
    html = re.sub(r'<p><strong>Example\s+([^:]+):?</strong>(.*?)</p>', r'<div class="example"><h4>Example \1</h4><p>\2</p></div>', html)
    # Type 2: <h3><strong>Example 1.1:</strong></h3>\s*<p>text</p>
    html = re.sub(r'<h3><strong>Example\s+([^:]+):?</strong></h3>\s*<p>(.*?)</p>', r'<div class="example"><h4>Example \1</h4><p>\2</p></div>', html, flags=re.DOTALL)

    # 6. Corollaries
    html = re.sub(r'<p><strong>Corollary\s+([^:]+):</strong>(.*?)</p>', r'<div class="note"><h4>Corollary \1</h4><p>\2</p></div>', html)

    # 7. Definitions
    html = re.sub(r'<p><strong>Definition\s+([^:]+):</strong>(.*?)</p>', r'<div class="definition"><h4>Definition \1</h4><p>\2</p></div>', html)
    html = re.sub(r'<h3><strong>Definition\s+([^:]+):</strong></h3>\s*<p>(.*?)</p>', r'<div class="definition"><h4>Definition \1</h4><p>\2</p></div>', html, flags=re.DOTALL)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Saved {filepath}")

for filepath in glob.glob("Sampling/Chapter*.html"):
    process_file(filepath)
