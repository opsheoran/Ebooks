import glob
import re

for filepath in glob.glob("Sampling/Chapter*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Find the wrongly placed toggleSidebar() inside MathJax
    wrong_script = """    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
        function toggleSidebar() {
            var sidebar = document.getElementById('sidebar');
            if (sidebar) {
                sidebar.classList.toggle('open');
            }
        }
    </script>"""

    correct_mathjax = """    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>"""
    
    sidebar_script = """
    <script>
        function toggleSidebar() {
            var sidebar = document.getElementById('sidebar');
            if (sidebar) {
                sidebar.classList.toggle('open');
            }
        }
    </script>
</body>"""

    if "function toggleSidebar()" in wrong_script and wrong_script in html:
        html = html.replace(wrong_script, correct_mathjax)
        html = html.replace("</body>", sidebar_script)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Fixed script in {filepath}")
    else:
        # It's possible the script wasn't inside MathJax, let's verify where it is.
        # Remove any stray toggleSidebar and re-add at bottom cleanly
        if "function toggleSidebar()" in html:
            html = re.sub(r'\s*function toggleSidebar\(\) \{\s*var sidebar = document\.getElementById\(\'sidebar\'\);\s*if \(sidebar\) \{\s*sidebar\.classList\.toggle\(\'open\'\);\s*\}\s*\}\s*', '', html)
            
            # If it left empty script tag
            html = re.sub(r'<script>\s*</script>', '', html)
            # Remove it from MathJax tag
            html = re.sub(r'<script id="MathJax-script"[^>]*>\s*</script>', correct_mathjax, html)
            
            html = html.replace("</body>", sidebar_script)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Refixed script in {filepath}")

