import glob

files = glob.glob("Stat-102/*.html") + glob.glob("Sampling/*.html")
for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Make sure CSS paths are absolutely correct
    content = content.replace('href="whiteboard.css?v=1.2"', 'href="../whiteboard/whiteboard.css?v=1.2"')
    content = content.replace('href="whiteboard.css"', 'href="../whiteboard/whiteboard.css"')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {filepath}")
