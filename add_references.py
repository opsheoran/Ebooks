import glob
import re

ref_block_eng = """        <div id="sec-ref" class="topic-section">
<div class="section-card">
<div class="english-content">
                <h2>References</h2>
                <ul>
                    <li>Cochran, W. G. (1977). <em>Sampling Techniques</em> (3rd ed.). John Wiley & Sons.</li>
                    <li>Singh, D., & Chaudhary, F. S. (1986). <em>Theory and Analysis of Sample Survey Designs</em>. New Age International.</li>
                    <li>Sukhatme, P. V. (1954). <em>Sampling Theory of Surveys with Applications</em>. Iowa State College Press.</li>
                    <li>Yates, F. (1960). <em>Sampling Methods for Censuses and Surveys</em>. Charles Griffin & Co.</li>
                    <li>Des Raj (1968). <em>Sampling Theory</em>. McGraw-Hill.</li>
                </ul>
            </div>
            <div class="hinglish-content">
                <h2>References (संदर्भ)</h2>
                <ul>
                    <li>Cochran, W. G. (1977). <em>Sampling Techniques</em> (3rd ed.). John Wiley & Sons.</li>
                    <li>Singh, D., & Chaudhary, F. S. (1986). <em>Theory and Analysis of Sample Survey Designs</em>. New Age International.</li>
                    <li>Sukhatme, P. V. (1954). <em>Sampling Theory of Surveys with Applications</em>. Iowa State College Press.</li>
                    <li>Yates, F. (1960). <em>Sampling Methods for Censuses and Surveys</em>. Charles Griffin & Co.</li>
                    <li>Des Raj (1968). <em>Sampling Theory</em>. McGraw-Hill.</li>
                </ul>
            </div>
</div>
</div>
"""

missing_singh = """<li>Singh, D., & Chaudhary, F. S. (1986). <em>Theory and Analysis of Sample Survey Designs</em>. New Age International.</li>"""

for filepath in glob.glob("Sampling/Chapter*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Check if there is already a References section
    if "<h2>References" not in html:
        # Find the last topic-section closing div before </main>
        # Just insert it before </main>
        if "</main>" in html:
            html = html.replace("</main>", ref_block_eng + "\n    </main>")
            # Also add to sidebar
            sb_link = """        <a class="nav-link" onclick="showTopic('sec-ref')">📚 References</a>\n        <hr style="border: 0.5px solid rgba(255,255,255,0.1); margin: 15px 20px;">"""
            html = html.replace("""<a class="nav-link" href="index.html#home">""", sb_link + """\n        <a class="nav-link" href="index.html#home">""")
            print(f"Added References to {filepath}")
    else:
        # Ensure Singh & Chaudhary is in the list
        if "Singh, D., & Chaudhary, F. S." not in html:
            # Add to the <ul> inside the References section
            # We can find <h2>References</h2>\s*<ul> and insert it there.
            html = re.sub(r'(<h2>References.*?</h2>\s*<ul>)', r'\1\n                    ' + missing_singh, html, flags=re.DOTALL)
            print(f"Added Singh & Chaudhary to {filepath}")
            
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
