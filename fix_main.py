import glob
import re

for filepath in glob.glob("Sampling/Chapter*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Check if </main> is missing
    if "</main>" not in html:
        # We need to insert it right before the first <script> tag that comes after the main content, 
        # or right before </body>
        html = html.replace("<script>\n        function toggleSidebar()", "</main>\n    <script>\n        function toggleSidebar()")
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Added </main> to {filepath}")
