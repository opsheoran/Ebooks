import glob
import re

sb_link = '        <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic(\'sec-ref\');return false;"><span class="nav-num">📚</span> References</a></li>\n'

for filepath in glob.glob("Sampling/Chapter*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    if "showTopic('sec-ref')" not in html and "showTopic('sec2-ref')" not in html:
        # It's missing from the sidebar.
        # Find the last </ul>\n</nav> and insert it before the </ul>
        # Wait, the sidebar has "Practice Exercises" and then </ul>\n</nav>
        # Let's insert it inside the last </ul>
        html = html.replace('    </ul>\n</nav>', sb_link + '    </ul>\n</nav>')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Added sidebar link to {filepath}")
    else:
        # ensure it's not named 'sec2-ref' because I've used 'sec-ref' in chapter 1, 5, 7.
        pass

