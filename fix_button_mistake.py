import glob
import re

for filepath in glob.glob("Sampling/Chapter*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Fix the double "Switch to Hinglish</button>Switch to Hinglish</button>" mistake
    html = html.replace('Switch to Hinglish</button>Switch to Hinglish</button>', 'Switch to Hinglish</button>')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Fixed {filepath}")
