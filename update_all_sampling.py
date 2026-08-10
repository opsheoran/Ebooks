import re
import glob

def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Extract chapter title info
    # E.g. <title>Chapter 2 – Simple Random Sampling | Theory of Sampling</title>
    title_match = re.search(r'<title>Chapter (\d+)\s*[-–]\s*(.*?)\s*\|.*?</title>', html)
    if title_match:
        ch_num = title_match.group(1)
        ch_name = title_match.group(2).strip()
    else:
        # fallback
        h1_match = re.search(r'<h1>Chapter (\d+):\s*(.*?)</h1>', html)
        if h1_match:
            ch_num = h1_match.group(1)
            ch_name = h1_match.group(2).replace(" | Theory of Sampling", "").strip()
        else:
            ch_num = "X"
            ch_name = "Topic"

    # E.g. Chapter 2 – Simple Random Sampling -> CHAPTER 2 · SIMPLE RANDOM SAMPLING
    subtitle_upper = f"CHAPTER {ch_num} · {ch_name.upper()}"

    # 1. Update Header
    new_header = f"""<header class="book-header">
    <button class="menu-toggle" onclick="toggleSidebar()" aria-label="Toggle menu"><i class="fas fa-bars"></i></button>
    <div class="header-icon">🎲</div>
    <div class="header-text">
        <h1>Theory of Sampling</h1>
        <div class="subtitle">{subtitle_upper}</div>
    </div>
    <div class="header-badge">Prof. O.P. Sheoran</div>
    <button class="draw-mode-toggle" id="draw-mode-btn">
        <i class="fas fa-chalkboard"></i> Open Whiteboard
    </button>
</header>"""
    html = re.sub(r'<header class="book-header">.*?</header>', new_header, html, flags=re.DOTALL)

    # 2. Sidebar rewrite
    sidebar_match = re.search(r'<aside class="sidebar">(.*?)</aside>', html, re.DOTALL)
    if sidebar_match:
        sidebar_content = sidebar_match.group(1)
        
        # Extract links
        links = re.findall(r'<a class="nav-link[^>]*onclick="showTopic\(\'([^\']+)\'\)".*?>(.*?)</a>', sidebar_content)
        
        new_sidebar = f"""<nav class="sidebar" id="sidebar">
    <div class="sidebar-brand">
        <h2>Chapter {ch_num}</h2>
        <p>{ch_name}<br>CCS Haryana Agricultural University</p>
    </div>
    <div class="sidebar-author">
        <img src="opsheoran.png" alt="Prof. O.P. Sheoran" class="sidebar-photo">
        <div class="sidebar-author-info">
            <h3>Prof. O.P. Sheoran</h3>
            <p>Author & Instructor</p>
        </div>
    </div>
    <div class="nav-group-label">Navigation</div>
    <ul class="nav-list">
        <li class="nav-item">
            <a class="nav-link" href="index.html#home" style="background: rgba(200,146,42,0.1); color: var(--gold-light); font-weight: 600;">
                <span class="nav-num">🏠</span> Home
            </a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="../index.html" style="background: rgba(27,42,74,0.3); color: white; font-weight: 600; margin-top: 5px;">
                <span class="nav-num">📚</span> Back to E-Books Library
            </a>
        </li>
    </ul>
    <div class="nav-group-label">Main Concepts</div>
    <ul class="nav-list">\n"""
        
        for i, (topic_id, text) in enumerate(links):
            if 'quiz' in topic_id.lower() or 'Exercise' in text or 'Set of Problems' in text:
                continue
            
            text = text.strip()
            num_match = re.match(r'^([\d\.]+)\s+(.*)', text)
            if num_match:
                num = num_match.group(1)
                title = num_match.group(2)
            else:
                num = "📌" if i == 0 else "🔹"
                title = text
                
            active_class = " active" if i == 0 else ""
            new_sidebar += f'        <li class="nav-item"><a class="nav-link{active_class}" href="#" onclick="showTopic(\'{topic_id}\');return false;"><span class="nav-num">{num}</span> {title}</a></li>\n'
        
        new_sidebar += """    </ul>
    <div class="nav-group-label">Practice Exercises</div>
    <ul class="nav-list">\n"""
        
        for topic_id, text in links:
            if 'quiz' in topic_id.lower() or 'Exercise' in text or 'Set of Problems' in text:
                text = text.strip()
                num = ""
                if "Multiple" in text: num = "❓"
                elif "Blanks" in text: num = "✏️"
                elif "True" in text: num = "✅"
                elif "Exercise" in text or "Problems" in text: num = "📝"
                else: num = "🔹"
                
                clean_text = text.replace('❓', '').replace('✏️', '').replace('✅', '').replace('📝', '').strip()
                clean_text = re.sub(r'^[^\w]+', '', clean_text).strip()
                
                new_sidebar += f'        <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic(\'{topic_id}\');return false;"><span class="nav-num">{num}</span> {clean_text}</a></li>\n'
                
        new_sidebar += "    </ul>\n</nav>"
        html = html.replace(sidebar_match.group(0), new_sidebar)

    # 3. Main content Chapter header
    chapter_header = f"""<div class="chapter-header">
    <h1>Chapter {ch_num}: {ch_name}</h1>
    <div class="author">By Prof. O.P. Sheoran · Department of Mathematics & Statistics</div>
</div>\n\n"""

    if "lang-toggle-btn" in html and '<div class="chapter-header">' not in html:
        html = html.replace('<main class="main-content">\n        <button class="lang-toggle-btn" onclick="toggleLanguage()">Switch to Hinglish</button>', 
                            f'<main class="main-content">\n        <button class="lang-toggle-btn" onclick="toggleLanguage()" style="margin-bottom: 20px; z-index: 100; position: relative;">Switch to Hinglish</button>\n        {chapter_header}')
    elif '<div class="chapter-header">' not in html:
        # Fallback if no lang toggle button (e.g. Chapter 5?)
        html = html.replace('<main class="main-content">', f'<main class="main-content">\n        {chapter_header}')

    # 4. Wrap sections in .topic-section and style headers
    sections = re.findall(r'(<section id="([^"]+)" class="section-card([^"]*)">.*?</section>)', html, re.DOTALL)
    for full_section, topic_id, active_classes in sections:
        is_active = "active" in active_classes
        active_str = " active" if is_active else ""
        
        new_section = f'<div id="{topic_id}" class="topic-section{active_str}">\n<div class="section-card">\n'
        
        # Strip the <section> tag itself, preserving inner content
        inner_html = re.sub(r'^<section[^>]+>', '', full_section).strip()
        inner_html = re.sub(r'</section>$', '', inner_html).strip()
        
        def h2_repl(m):
            content = m.group(1)
            num_m = re.match(r'^([\d\.]+)\s+(.*)', content)
            if num_m:
                return f'<h2><span class="section-num">{num_m.group(1)}</span> {num_m.group(2)}</h2>'
            return f'<h2>{content}</h2>'
            
        inner_html = re.sub(r'<h2>(.*?)</h2>', h2_repl, inner_html)
        
        new_section += inner_html + '\n</div>\n</div>'
        html = html.replace(full_section, new_section)

    # 5. Fix Javascript showTopic
    js_old = """document.querySelectorAll('.section-card').forEach(card => card.classList.remove('active'));"""
    js_new = """document.querySelectorAll('.topic-section').forEach(card => card.classList.remove('active'));"""
    html = html.replace(js_old, js_new)

    # Fix JS Sidebar Toggle
    if "function toggleSidebar()" not in html:
        html = html.replace('</script>', """
        function toggleSidebar() {
            var sidebar = document.getElementById('sidebar');
            if (sidebar) {
                sidebar.classList.toggle('open');
            }
        }
    </script>""")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Finished {filepath}")

for i in range(1, 10):
    filepath = f"Sampling/Chapter{i}.html"
    try:
        process_file(filepath)
    except FileNotFoundError:
        print(f"File {filepath} not found, skipping.")
