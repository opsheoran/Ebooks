import os
import glob

# 1. Update Sampling Chapters
sampling_files = glob.glob("Sampling/Chapter*.html")

for filepath in sampling_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Add whiteboard.css
    if "whiteboard.css" not in content:
        content = content.replace("</head>", '    <link rel="stylesheet" href="whiteboard.css">\n</head>')

    # Add whiteboard.js
    if "whiteboard.js" not in content:
        content = content.replace("</body>", '    <script src="whiteboard.js?v=1.3"></script>\n</body>')

    # Add whiteboard button
    if "draw-mode-btn" not in content:
        button_html = '\n        <button class="draw-mode-toggle" id="draw-mode-btn" style="position: absolute; right: 20px; top: 50%; transform: translateY(-50%);"><i class="fas fa-chalkboard"></i> Open Whiteboard</button>\n    </header>'
        content = content.replace("</header>", button_html)

    # Add Author Photo to Sidebar
    if "opsheoran.png" not in content:
        photo_html = """<aside class="sidebar">
        <div style="text-align: center; margin-bottom: 20px; margin-top: 10px;">
            <img src="opsheoran.png" alt="Prof. O.P. Sheoran" style="width: 100px; height: 100px; border-radius: 50%; border: 3px solid var(--gold); margin-bottom: 10px; object-fit: cover;">
            <h3 style="color: white; font-family: \\'Playfair Display\\', serif; font-size: 1.1rem; margin: 0;">Prof. O.P. Sheoran</h3>
        </div>"""
        content = content.replace('<aside class="sidebar">', photo_html)

    # Update Sidebar Links
    old_links = '<a class="nav-link" href="index.html"><i class="fas fa-home"></i> Back to Index</a>'
    new_links = """<a class="nav-link" href="index.html#home"><i class="fas fa-home"></i> Home</a>
        <a class="nav-link" href="index.html#preface"><i class="fas fa-scroll"></i> Preface</a>
        <a class="nav-link" href="index.html#syllabus"><i class="fas fa-list-alt"></i> Syllabus</a>
        <a class="nav-link" href="index.html#author"><i class="fas fa-user-tie"></i> About Author</a>
        <a class="nav-link" href="../index.html" style="background: rgba(255,255,255,0.1); margin-top: 10px;"><i class="fas fa-book-open"></i> Back to E-Books Library</a>"""
    content = content.replace(old_links, new_links)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {filepath}")


# 2. Update Stat-102 Units
stat_units = glob.glob("Stat-102/Unit-*.html")

for filepath in stat_units:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "../index.html" not in content:
        target = '</a>\n            </li>\n        </ul>\n\n        <div class="nav-group-label">Main Concepts</div>'
        replacement = '</a>\n            </li>\n            <li class="nav-item">\n                <a class="nav-link" href="../index.html" style="background: rgba(27,42,74,0.3); color: white; font-weight: 600; margin-top: 5px;">\n                    <span class="nav-num">📚</span> Back to E-Books Library\n                </a>\n            </li>\n        </ul>\n\n        <div class="nav-group-label">Main Concepts</div>'
        if target in content:
            content = content.replace(target, replacement)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {filepath}")
        else:
            print(f"Target not found in {filepath}")

# 3. Update stat102.html
stat102_path = "Stat-102/stat102.html"
if os.path.exists(stat102_path):
    with open(stat102_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "../index.html" not in content:
        target = '<span class="nav-icon"><i class="fas fa-book-open"></i></span> Suggested Readings\n                </a>\n            </li>\n        </ul>\n    </nav>'
        replacement = '<span class="nav-icon"><i class="fas fa-book-open"></i></span> Suggested Readings\n                </a>\n            </li>\n        </ul>\n        <div class="nav-group-label" style="margin-top: 20px;">Library</div>\n        <ul class="nav-list">\n            <li class="nav-item">\n                <a class="nav-link" href="../index.html" style="background: rgba(200,146,42,0.1); color: var(--gold-light); font-weight: 600;">\n                    <span class="nav-icon"><i class="fas fa-book-open"></i></span> Back to E-Books Library\n                </a>\n            </li>\n        </ul>\n    </nav>'
        
        if target in content:
            content = content.replace(target, replacement)
            with open(stat102_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {stat102_path}")
        else:
            print(f"Target not found in {stat102_path}")
