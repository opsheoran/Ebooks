import re
import glob

def process_ch1():
    filepath = "Sampling/Chapter1.html"
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Convert $$ ... $$ to <div class="formula-box">\[ ... \]</div>
    html = re.sub(r'\$\$(.*?)\$\$', r'<div class="formula-box">\[ \1 \]</div>', html, flags=re.DOTALL)
    
    # In Chapter 1, we also need to fix <strong>Theorem etc. Wait, I ran fix_styles.py before which fixed <p><strong>Theorem 1.1... but let's make sure.
    # In chapter 1, let's see if there are any Theorem blocks left.
    html = re.sub(r'<p><strong>Theorem(.*?):</strong>(.*?)</p>', r'<div class="theorem"><h4>Theorem\1</h4><p>\2</p></div>', html)
    html = re.sub(r'<p><strong>Example(.*?):?</strong>(.*?)</p>', r'<div class="example"><h4>Example\1</h4><p>\2</p></div>', html)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print("Fixed Chapter 1 math blocks and styles.")

process_ch1()
