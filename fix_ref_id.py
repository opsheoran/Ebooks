import glob
import re

for filepath in glob.glob("Sampling/Chapter*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Change id="secX-ref" to id="sec-ref"
    html = re.sub(r'id="sec\d+-ref"', 'id="sec-ref"', html)
    
    # Also if there was an old nav-link for secX-ref, remove it to avoid duplicates
    html = re.sub(r'<a class="nav-link[^>]*onclick="showTopic\(\'sec\d+-ref\'\).*?</a>\s*', '', html)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Standardized References id in {filepath}")
