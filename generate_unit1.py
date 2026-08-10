import os

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unit I – Introduction & Data Collection | STAT-M-101</title>

    <!-- MathJax -->
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,900;1,400;1,600&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">

    <style>
        :root {
            --navy:          #1B2A4A;
            --navy-mid:      #243555;
            --navy-light:    #2E4270;
            --gold:          #C8922A;
            --gold-light:    #E8B84B;
            --gold-pale:     #FDF3DC;
            --sage:          #3D6B5A;
            --sage-light:    #EEF6F2;
            --crimson:       #9B2335;
            --crimson-light: #FBF0F1;
            --sky:           #1D6FA4;
            --sky-light:     #EAF4FB;
            --ivory:         #FAFAF7;
            --paper:         #F5F3EE;
            --border:        #DDD8CF;
            --text-dark:     #1C1C1E;
            --text-mid:      #3A3A3C;
            --text-soft:     #6B6B70;
            --sidebar-w:     300px;
            --header-h:      72px;
            --radius:        10px;
            --shadow-sm:     0 2px 8px rgba(27,42,74,.08);
            --shadow-md:     0 4px 20px rgba(27,42,74,.12);
            --shadow-lg:     0 8px 40px rgba(27,42,74,.16);
        }
        *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
        html { scroll-behavior: smooth; }
        body { font-family: 'Source Serif 4', Georgia, serif; background: var(--paper); color: var(--text-dark); line-height: 1.78; font-size: 16px; }

        .book-header { position: fixed; top: 0; left: 0; right: 0; height: var(--header-h); background: linear-gradient(110deg, var(--navy) 0%, var(--navy-mid) 50%, var(--navy-light) 100%); color: #fff; z-index: 1100; box-shadow: 0 3px 20px rgba(0,0,0,.25); display: flex; align-items: center; padding: 0 28px; gap: 16px; }
        .book-header .menu-toggle { display: none; background: none; border: none; color: #fff; font-size: 1.3rem; cursor: pointer; padding: 4px 8px; }
        .header-icon { width: 42px; height: 42px; background: var(--gold); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; flex-shrink: 0; }
        .header-text h1 { font-family: 'Playfair Display', serif; font-size: 1.3rem; font-weight: 700; letter-spacing: .3px; color: #fff; }
        .header-text .subtitle { font-family: 'DM Sans', sans-serif; font-size: .8rem; color: rgba(255,255,255,.7); letter-spacing: .5px; }
        .header-badge { margin-left: auto; background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.2); color: rgba(255,255,255,.9); font-family: 'DM Sans', sans-serif; font-size: .75rem; font-weight: 500; padding: 4px 12px; border-radius: 20px; }

        .sidebar { position: fixed; left: 0; top: var(--header-h); width: var(--sidebar-w); height: calc(100vh - var(--header-h)); background: var(--navy); overflow-y: auto; z-index: 1000; transition: transform .3s ease; scrollbar-width: thin; scrollbar-color: rgba(200,146,42,.4) transparent; }
        .sidebar::-webkit-scrollbar { width: 4px; }
        .sidebar::-webkit-scrollbar-thumb { background: rgba(200,146,42,.4); border-radius: 4px; }
        .sidebar-brand { padding: 20px 20px 14px; border-bottom: 1px solid rgba(255,255,255,.1); background: linear-gradient(180deg, rgba(200,146,42,.15) 0%, transparent 100%); }
        .sidebar-brand h2 { font-family: 'Playfair Display', serif; font-size: 1.15rem; font-weight: 700; color: var(--gold-light); margin-bottom: 3px; }
        .sidebar-author { padding: 20px 20px; background: rgba(0,0,0,0.2); border-bottom: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; gap: 12px; }
        .sidebar-photo { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid var(--gold); }
        .sidebar-author-info h3 { font-size: 0.9rem; color: #fff; margin: 0; font-family: 'Playfair Display', serif; }
        .sidebar-author-info p { font-size: 0.65rem; color: rgba(255,255,255,0.6); margin: 0; text-transform: uppercase; }
        .sidebar-brand p { font-family: 'DM Sans', sans-serif; font-size: .78rem; color: rgba(255,255,255,.55); line-height: 1.4; }
        .nav-group-label { font-family: 'DM Sans', sans-serif; font-size: .68rem; font-weight: 600; letter-spacing: 1.2px; text-transform: uppercase; color: rgba(255,255,255,.35); padding: 16px 20px 6px; }
        .nav-list { list-style: none; padding: 0 8px 12px; }
        .nav-item { margin: 1px 0; }
        .nav-link { display: flex; align-items: center; gap: 10px; padding: 9px 12px; color: rgba(255,255,255,.75); text-decoration: none; border-radius: 7px; font-family: 'DM Sans', sans-serif; font-size: .875rem; transition: all .2s ease; border-left: 3px solid transparent; cursor: pointer; }
        .nav-link:hover { background: rgba(255,255,255,.08); color: #fff; border-left-color: rgba(200,146,42,.6); }
        .nav-link.active { background: rgba(200,146,42,.18); color: var(--gold-light); border-left-color: var(--gold); font-weight: 500; }
        .nav-link .nav-num { font-size: .7rem; background: rgba(255,255,255,.12); border-radius: 4px; padding: 1px 6px; font-weight: 600; min-width: 26px; text-align: center; flex-shrink: 0; }
        .nav-link.active .nav-num { background: var(--gold); color: var(--navy); }
        .nav-sub .nav-link { padding-left: 28px; font-size: .835rem; color: rgba(255,255,255,.55); }

        .main-content { margin-left: var(--sidebar-w); margin-top: var(--header-h); padding: 36px 48px 60px; max-width: calc(var(--sidebar-w) + 860px); min-height: calc(100vh - var(--header-h)); }
        .chapter-header { background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%); color: #fff; padding: 32px 36px; border-radius: var(--radius); margin-bottom: 32px; box-shadow: var(--shadow-md); position: relative; overflow: hidden; }
        .chapter-header::before { content: ''; position: absolute; top: -30px; right: -30px; width: 180px; height: 180px; background: rgba(200,146,42,.12); border-radius: 50%; }
        .chapter-header h1 { font-family: 'Playfair Display', serif; font-size: 2.1rem; font-weight: 900; margin-bottom: 6px; }
        .chapter-header .author { font-family: 'DM Sans', sans-serif; font-size: .95rem; color: rgba(255,255,255,.7); margin-bottom: 14px; font-style: italic; }
        .chapter-header .syllabus-tag { display: inline-block; background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.2); border-radius: 6px; padding: 10px 16px; font-family: 'DM Sans', sans-serif; font-size: .82rem; color: rgba(255,255,255,.85); }

        .topic-section { display: none; animation: fadeSlideIn .45s ease; }
        .topic-section.active { display: block; }
        @keyframes fadeSlideIn { from { opacity: 0; transform: translateY(18px); } to { opacity: 1; transform: translateY(0); } }

        .section-card { background: var(--ivory); border-radius: var(--radius); padding: 36px 42px; box-shadow: var(--shadow-sm); border: 1px solid var(--border); border-top: 4px solid var(--navy); margin-bottom: 24px; }
        .section-card h2 { font-family: 'Playfair Display', serif; font-size: 1.85rem; font-weight: 700; color: var(--navy); margin: 0 0 20px; padding-bottom: 14px; border-bottom: 2px solid var(--border); display: flex; align-items: baseline; gap: 10px; }
        .section-card h3 { font-family: 'Playfair Display', serif; font-size: 1.4rem; font-weight: 600; color: var(--navy-light); margin: 32px 0 14px; }
        .section-card p { margin-bottom: 12px; text-align: justify; font-size: 1.02rem; color: var(--text-mid); line-height: 1.82; }
        .section-card ul, .section-card ol { margin: 10px 0 14px 28px; line-height: 1.75; }
        .section-card li { margin-bottom: 5px; color: var(--text-mid); font-size: .99rem; }
        .section-num { font-family: 'DM Sans', sans-serif; font-size: .9rem; font-weight: 700; background: var(--navy); color: var(--gold-light); padding: 2px 10px; border-radius: 5px; flex-shrink: 0; }

        .definition, .example, .note { border-radius: 8px; padding: 18px 22px; margin: 20px 0; position: relative; }
        .definition { background: #F3F0FB; border-left: 5px solid #6B4FC8; }
        .definition h4::before { content: "Definition — "; color: #6B4FC8; }
        .example { background: #FFFBF0; border-left: 5px solid var(--gold); }
        .note { background: var(--sky-light); border-left: 5px solid var(--sky); }
        .definition h4, .example h4, .note h4 { margin-top: 0; margin-bottom: 8px; color: var(--text-dark); }

        .exercise-section { background: transparent; padding: 0; border: none; box-shadow: none; }
        .exercise-header { background: linear-gradient(135deg, var(--navy) 0%, var(--navy-light) 100%); color: #fff; padding: 24px 30px; border-radius: 10px 10px 0 0; margin-bottom: 0; }
        .exercise-header h2 { font-family: 'Playfair Display', serif; font-size: 1.6rem; color: #fff; border: none; padding: 0; margin: 0 0 4px; }
        .exercise-header p { font-family: 'DM Sans', sans-serif; font-size: .85rem; color: rgba(255,255,255,.7); margin: 0; }
        
        .question { background: #fff; border: 1px solid var(--border); border-left: 4px solid var(--navy-light); padding: 16px 20px; margin: 14px 0 6px; border-radius: 0 8px 8px 0; font-size: 1rem; color: var(--text-dark); line-height: 1.7; }
        .question-list { list-style: none; margin: 0; padding: 0; }
        .question-list > li { margin-bottom: 20px; }
        
        .get-solution-btn { background: var(--navy); color: #fff; border: none; padding: 7px 18px; border-radius: 20px; cursor: pointer; font-family: 'DM Sans', sans-serif; font-size: .82rem; font-weight: 500; display: inline-flex; align-items: center; gap: 5px; transition: all .25s; margin: 8px 0; }
        .get-solution-btn:hover { background: var(--navy-light); transform: translateY(-2px); box-shadow: 0 4px 12px rgba(27,42,74,.3); }
        .solution { display: none; background: #F0FBF5; border-left: 4px solid var(--sage); padding: 16px 20px; margin: 2px 0 12px; border-radius: 0 8px 8px 0; animation: fadeSlideIn .3s ease; font-size: .97rem; }
        .solution.show { display: block; }
        .mcq-options { margin: 10px 0 8px 20px; }
        .mcq-options label { display: block; margin: 5px 0; cursor: pointer; font-size: .95rem; color: var(--text-mid); }
        .mcq-options input { margin-right: 8px; accent-color: var(--navy); }

        @media (max-width: 768px) {
            :root { --sidebar-w: 280px; }
            .book-header .menu-toggle { display: flex; align-items: center; justify-content: center; }
            .sidebar { transform: translateX(-100%); }
            .sidebar.open { transform: translateX(0); }
            .main-content { margin-left: 0; padding: 20px 18px 40px; max-width: 100%; }
        }
    </style>
</head>
<body>
    <!-- TOP HEADER -->
    <header class="book-header">
        <button class="menu-toggle" onclick="toggleSidebar()"><i class="fas fa-bars"></i></button>
        <div class="header-icon">📊</div>
        <div class="header-text">
            <h1>STAT-M-101</h1>
            <div class="subtitle">UNIT I · INTRODUCTION & DATA COLLECTION</div>
        </div>
        <div class="header-badge">Prof. O.P. Sheoran</div>
    </header>

    <!-- SIDEBAR -->
    <nav class="sidebar" id="sidebar">
        <div class="sidebar-brand">
            <h2>Unit I</h2>
            <p>Introduction & Data<br>CCS HAU, Hisar</p>
        </div>
        <div class="sidebar-author">
            <div class="sidebar-author-info">
                <h3>Prof. O.P. Sheoran</h3>
                <p>Instructor</p>
            </div>
        </div>

        <div class="nav-group-label">Navigation</div>
        <ul class="nav-list">
            <li class="nav-item"><a class="nav-link" href="index.html" style="color: var(--gold-light); font-weight: 600;"><span class="nav-num">🏠</span> Course Home</a></li>
        </ul>

        <div class="nav-group-label">Theory</div>
        <ul class="nav-list">
            <li class="nav-item"><a class="nav-link active" href="#" onclick="showTopic('intro')"><span class="nav-num">1</span> Intro to Statistics</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('types-data')"><span class="nav-num">2</span> Types of Data</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('collection')"><span class="nav-num">3</span> Collection & Scrutiny</a></li>
        </ul>

        <div class="nav-group-label">Exercises</div>
        <ul class="nav-list">
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('mcq')"><span class="nav-num">❓</span> MCQs (30)</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('fib')"><span class="nav-num">✏️</span> Fill in Blanks (30)</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('tf')"><span class="nav-num">✅</span> True/False (30)</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('subjective')"><span class="nav-num">📝</span> Subjective (20)</a></li>
        </ul>
    </nav>

    <!-- MAIN CONTENT -->
    <main class="main-content">
        <div class="chapter-header">
            <h1>Unit I: Introduction & Data Collection</h1>
            <div class="author">By Prof. O.P. Sheoran</div>
            <div class="syllabus-tag">
                <strong>Syllabus:</strong> Origin, development, definition, scope, uses, limitations. Types of Data. Collection and Scrutiny of Data.
            </div>
        </div>

        <!-- THEORY SECTIONS -->
        <div id="intro" class="topic-section active">
            <section class="section-card">
                <h2><span class="section-num">1.</span> Introduction to Statistics</h2>
                <p>The word 'Statistics' is derived from the Latin word <em>'Status'</em>, the Italian word <em>'Statista'</em>, or the German word <em>'Statistik'</em>, all of which mean a political state. Originally, it meant information useful to the state, such as data on population, land, and military strength.</p>
                <div class="definition">
                    <h4>Definition</h4>
                    <p>Statistics is the science of <strong>collecting, organizing, presenting, analyzing, and interpreting</strong> numerical data to make decisions in the face of uncertainty.</p>
                </div>
                <h3>Scope and Uses</h3>
                <ul>
                    <li><strong>In Agriculture:</strong> To evaluate the effect of fertilizers, seed varieties, or farming techniques via designed experiments.</li>
                    <li><strong>In Economics:</strong> To compute indices, forecast trends, and analyze supply and demand.</li>
                    <li><strong>In Medicine:</strong> To test the efficacy of new drugs and vaccines.</li>
                    <li><strong>In State Administration:</strong> To frame policies based on census data, unemployment rates, etc.</li>
                </ul>
                <h3>Limitations of Statistics</h3>
                <ol>
                    <li>Statistics deals only with quantitative data. Qualitative attributes like honesty or intelligence must be quantified before statistical methods can apply.</li>
                    <li>Statistics does not deal with isolated individuals; it deals with aggregates of facts.</li>
                    <li>Statistical laws are true only on average. They are probabilistic, not exact like mathematical laws.</li>
                    <li>Statistics can be misused if the data is inaccurate or analyzed by untrained persons.</li>
                </ol>
            </section>
        </div>

        <div id="types-data" class="topic-section">
            <section class="section-card">
                <h2><span class="section-num">2.</span> Types of Data</h2>
                <p>Data forms the foundation of any statistical investigation. It can be classified based on various characteristics.</p>
                <h3>Qualitative vs Quantitative Data</h3>
                <ul>
                    <li><strong>Qualitative Data:</strong> Deals with characteristics or attributes that cannot be quantified numerically (e.g., gender, eye color, blood group).</li>
                    <li><strong>Quantitative Data:</strong> Represents measurable quantities (e.g., height, weight, income).</li>
                </ul>
                <h3>Nominal vs Ordinal Data</h3>
                <ul>
                    <li><strong>Nominal Data:</strong> Categories without any inherent order (e.g., Religion, Nationality).</li>
                    <li><strong>Ordinal Data:</strong> Categories with a logical order or rank (e.g., Student grades: A, B, C; Satisfaction levels: Low, Medium, High).</li>
                </ul>
                <h3>Discrete vs Continuous Data</h3>
                <ul>
                    <li><strong>Discrete Data:</strong> Can only take specific isolated values, usually integers (e.g., number of children in a family, number of accidents).</li>
                    <li><strong>Continuous Data:</strong> Can take any value within a given range, including fractions and decimals (e.g., temperature, yield of a crop).</li>
                </ul>
                <h3>Time Series vs Cross-Sectional Data</h3>
                <ul>
                    <li><strong>Time Series Data:</strong> Data collected on a variable over different points in time (e.g., annual rainfall from 2010 to 2020).</li>
                    <li><strong>Cross-Sectional Data:</strong> Data collected from multiple entities at a single point in time (e.g., population of different states in 2021).</li>
                </ul>
            </section>
        </div>

        <div id="collection" class="topic-section">
            <section class="section-card">
                <h2><span class="section-num">3.</span> Collection and Scrutiny of Data</h2>
                <h3>Primary vs Secondary Data</h3>
                <ul>
                    <li><strong>Primary Data:</strong> Data collected originally for the first time by the investigator for a specific purpose. It is raw and unanalyzed.</li>
                    <li><strong>Secondary Data:</strong> Data that has already been collected by someone else and has passed through the statistical process.</li>
                </ul>
                <h3>Sources of Secondary Data</h3>
                <p>Secondary data can be obtained from published sources (e.g., Government publications like the Census of India, RBI bulletins, international bodies like WHO/FAO) and unpublished sources (e.g., internal records of institutions).</p>
                <h3>Scrutiny of Data</h3>
                <p>Before proceeding with analysis, the collected data must be rigorously scrutinized for errors and inconsistencies:</p>
                <ul>
                    <li><strong>Internal Consistency:</strong> Checking if related variables contradict each other (e.g., age of a son cannot be greater than the age of the father).</li>
                    <li><strong>Detection of Errors:</strong> Identifying recording errors, missing values, or outliers that could skew the analysis.</li>
                    <li><strong>Classification and Tabulation:</strong> Organizing the raw, scrutinized data into homogeneous groups (classification) and presenting them systematically in rows and columns (tabulation) to facilitate comparison.</li>
                </ul>
            </section>
        </div>

        <!-- EXERCISE SECTIONS (Generated via JS below for conciseness in Python string but outputting standard HTML structure) -->
        {mcq_html}
        {fib_html}
        {tf_html}
        {subj_html}
    </main>

    <script>
        function showTopic(id) {
            document.querySelectorAll('.topic-section').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-link').forEach(el => el.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            event.currentTarget.classList.add('active');
            window.scrollTo(0,0);
        }

        document.addEventListener('DOMContentLoaded', () => {
            document.querySelectorAll('.get-solution-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const id = e.target.getAttribute('data-question-id');
                    const sol = document.getElementById('solution-' + id);
                    if (sol.classList.contains('show')) {
                        sol.classList.remove('show');
                        e.target.textContent = 'Get Solution';
                    } else {
                        sol.classList.add('show');
                        e.target.textContent = 'Hide Solution';
                    }
                });
            });
        });

        function toggleSidebar() {
            document.getElementById('sidebar').classList.toggle('open');
        }
    </script>
</body>
</html>
"""

def generate_mcqs():
    q_data = [
        ("The word 'Statistics' is derived from the Latin word:", ["Statista", "Status", "Statistik", "Stat"], 1),
        ("Statistics deals with:", ["Isolated individuals", "Qualitative data only", "Aggregates of facts", "Mathematical certainty"], 2),
        ("Data collected originally by the investigator is called:", ["Secondary Data", "Grouped Data", "Primary Data", "Published Data"], 2),
        ("Number of students in a class is an example of:", ["Continuous data", "Qualitative data", "Discrete data", "Nominal data"], 2),
        ("Yield of wheat per acre is an example of:", ["Discrete data", "Continuous data", "Ordinal data", "Secondary data"], 1),
        ("Eye color of a person is an example of:", ["Quantitative data", "Continuous data", "Qualitative data", "Discrete data"], 2),
        ("Census of India reports are a source of:", ["Primary Data", "Secondary Data", "Experimental Data", "Unpublished Data"], 1),
        ("Data collected over different points in time is known as:", ["Cross-sectional data", "Time series data", "Geographical data", "Nominal data"], 1),
        ("Classification of data based on geographical location is:", ["Chronological", "Geographical", "Qualitative", "Quantitative"], 1),
        ("Which of the following is NOT a limitation of statistics?", ["It deals with aggregates only", "It is exact like mathematical laws", "It can be misused", "It deals only with quantitative characteristics"], 1),
        ("Data which have already been collected by someone are called:", ["Primary data", "Secondary data", "Raw data", "Fictitious data"], 1),
        ("Arranging data in rows and columns is called:", ["Classification", "Tabulation", "Scrutiny", "Editing"], 1),
        ("Checking data for internal consistency is called:", ["Collection", "Scrutiny", "Tabulation", "Presentation"], 1),
        ("The grades A, B, C, D awarded to students represent:", ["Nominal data", "Ordinal data", "Interval data", "Ratio data"], 1),
        ("Blood groups of individuals represent:", ["Ordinal data", "Nominal data", "Discrete data", "Continuous data"], 1),
        ("Which of the following is true about statistical laws?", ["They are exact", "They are true on average", "They are always completely false", "None of the above"], 1),
        ("Data collected from various countries in the year 2025 is:", ["Time series data", "Cross-sectional data", "Ordinal data", "Primary data"], 1),
        ("Which of these is a method of collecting primary data?", ["Direct personal interview", "RBI Bulletins", "WHO reports", "Statistical abstracts"], 0),
        ("A variable that can take any value between two given points is called a:", ["Discrete variable", "Continuous variable", "Qualitative variable", "Attribute"], 1),
        ("The process of grouping data according to common characteristics is:", ["Tabulation", "Classification", "Scrutiny", "Editing"], 1),
        ("In agriculture, statistics is primarily used to:", ["Determine the exact number of pests", "Evaluate treatment effects through designed experiments", "Predict weather with 100% accuracy", "Avoid the use of fertilizers"], 1),
        ("Which of the following is quantitative data?", ["Religion", "Gender", "Height", "Nationality"], 2),
        ("Which data type cannot be subjected to meaningful arithmetic operations?", ["Continuous", "Discrete", "Nominal", "Time series"], 2),
        ("Temperature recorded every hour constitutes:", ["Cross-sectional data", "Time series data", "Nominal data", "Ordinal data"], 1),
        ("A statistical table should ideally have:", ["A title", "Headings and subheadings", "Source note", "All of the above"], 3),
        ("Errors committed during data collection are called:", ["Sampling errors", "Non-sampling errors", "Standard errors", "Systematic errors"], 1),
        ("Unpublished data can be found in:", ["Research journals", "Government publications", "Internal office records", "Newspapers"], 2),
        ("Checking if the 'age of son > age of father' is a part of:", ["Scrutiny for internal consistency", "Tabulation", "Data collection", "Sampling"], 0),
        ("Number of petals on a flower is:", ["Continuous", "Discrete", "Qualitative", "Nominal"], 1),
        ("Statistics refers to both statistical data and:", ["Statistical methods", "Statistical errors", "Statistical limitations", "Statistical formulas"], 0)
    ]
    html = '<div id="mcq" class="topic-section"><section class="section-card"><div class="exercise-section"><div class="exercise-header"><h2>Multiple Choice Questions</h2><p>Select the most appropriate option.</p></div><ul class="question-list">'
    for i, (q, opts, ans_idx) in enumerate(q_data, 1):
        opt_html = "".join([f'<label><input type="radio" name="q{i}"> {opt}</label>' for opt in opts])
        ans_text = opts[ans_idx]
        html += f'''
        <li>
            <div class="question">
                <strong>Q{i}.</strong> {q}
                <div class="mcq-options">{opt_html}</div>
            </div>
            <button class="get-solution-btn" data-question-id="mcq-{i}">Get Solution</button>
            <div class="solution" id="solution-mcq-{i}"><strong>Answer:</strong> {ans_text}</div>
        </li>'''
    html += '</ul></div></section></div>'
    return html

def generate_fib():
    q_data = [
        ("The word 'Statistics' comes from the Latin word ____.", "Status"),
        ("Data originally collected by the investigator is called ____ data.", "Primary"),
        ("Data that has been previously collected and processed is ____ data.", "Secondary"),
        ("Height of students in a class is a ____ variable.", "Continuous"),
        ("Number of cars in a parking lot is a ____ variable.", "Discrete"),
        ("Classification of data according to time is called ____ classification.", "Chronological"),
        ("Classification based on attributes like gender or religion is ____ classification.", "Qualitative"),
        ("Arranging data in systematic rows and columns is called ____.", "Tabulation"),
        ("Statistics deals only with aggregates of facts, not with ____ individuals.", "Isolated"),
        ("Statistical laws are true only on ____.", "Average"),
        ("Blood type is an example of ____ data.", "Nominal"),
        ("Letter grades (A, B, C) represent ____ data.", "Ordinal"),
        ("Data collected across different locations at one point in time is ____ data.", "Cross-sectional"),
        ("Checking raw data for errors and inconsistencies is called ____ of data.", "Scrutiny"),
        ("____ is a major source of secondary data published by the Government of India.", "Census of India"),
        ("Number of accidents on a highway is an example of a ____ variable.", "Discrete"),
        ("The process of categorizing raw data into homogeneous groups is called ____.", "Classification"),
        ("A qualitative characteristic, like honesty, is called an ____.", "Attribute"),
        ("Yield of a crop in kg/hectare is a ____ variable.", "Continuous"),
        ("Data used for the first time by its collector is called ____.", "Primary Data"),
        ("A statistical table's column headings are also known as ____.", "Captions"),
        ("The Italian word for statistics is ____.", "Statista"),
        ("Data which cannot be quantified numerically is called ____ data.", "Qualitative"),
        ("The process of verifying that the age of a son is not recorded as greater than his father's is checking for ____.", "Internal consistency"),
        ("Information on population size is generally derived from ____.", "Census"),
        ("Observations taken sequentially over time constitute a ____ series.", "Time"),
        ("A variable that assumes only specific isolated values is ____.", "Discrete"),
        ("The German word for statistics is ____.", "Statistik"),
        ("When a researcher uses data from an RBI bulletin, they are using ____ data.", "Secondary"),
        ("Statistics is a science of making decisions in the face of ____.", "Uncertainty")
    ]
    html = '<div id="fib" class="topic-section"><section class="section-card"><div class="exercise-section"><div class="exercise-header"><h2>Fill in the Blanks</h2><p>Complete the sentences.</p></div><ul class="question-list">'
    for i, (q, ans) in enumerate(q_data, 1):
        html += f'''
        <li>
            <div class="question"><strong>Q{i}.</strong> {q}</div>
            <button class="get-solution-btn" data-question-id="fib-{i}">Get Solution</button>
            <div class="solution" id="solution-fib-{i}"><strong>Answer:</strong> {ans}</div>
        </li>'''
    html += '</ul></div></section></div>'
    return html

def generate_tf():
    q_data = [
        ("Statistics deals with isolated individual facts.", False),
        ("Primary data is more reliable than secondary data.", True),
        ("Continuous data can take only integer values.", False),
        ("Gender is an example of quantitative data.", False),
        ("Secondary data is data that has already been collected by someone else.", True),
        ("Statistical laws are exact and universally true in every individual case.", False),
        ("Classification must precede tabulation.", True),
        ("Nominal data has a natural ordering.", False),
        ("Time series data is collected at a single point in time.", False),
        ("Number of leaves on a plant is a continuous variable.", False),
        ("Scrutiny of data is done to detect recording errors and inconsistencies.", True),
        ("Yield of wheat is a continuous variable.", True),
        ("Qualitative data cannot be analyzed statistically without quantification.", True),
        ("Statistics is useful in agriculture to evaluate fertilizer effects.", True),
        ("A Census report is a primary source of data for a researcher using it.", False),
        ("Cross-sectional data is collected from multiple entities at the same time.", True),
        ("Ordinal data allows for ranking.", True),
        ("Discrete variables can take any fractional value.", False),
        ("Tabulation involves grouping data into classes.", False),
        ("The word Statistics can mean both data and statistical methods.", True),
        ("Height is a qualitative variable.", False),
        ("The Italian origin of Statistics is 'Statistik'.", False),
        ("Unpublished records can serve as secondary data.", True),
        ("An attribute is a measurable characteristic.", False),
        ("The primary objective of scrutiny is to make data look better.", False),
        ("Data collected via direct personal interview is primary data.", True),
        ("Statistics can be misused if analyzed by an untrained person.", True),
        ("A statistical table must have a title.", True),
        ("Age is an example of an attribute.", False),
        ("Statistics provides 100% certainty in decision making.", False)
    ]
    html = '<div id="tf" class="topic-section"><section class="section-card"><div class="exercise-section"><div class="exercise-header"><h2>True or False</h2><p>Determine if the statements are True or False.</p></div><ul class="question-list">'
    for i, (q, ans) in enumerate(q_data, 1):
        html += f'''
        <li>
            <div class="question"><strong>Q{i}.</strong> {q}</div>
            <button class="get-solution-btn" data-question-id="tf-{i}">Get Solution</button>
            <div class="solution" id="solution-tf-{i}"><strong>Answer:</strong> {"True" if ans else "False"}</div>
        </li>'''
    html += '</ul></div></section></div>'
    return html

def generate_subj():
    q_data = [
        ("Define Statistics and discuss its scope in Agriculture.", "Statistics is the science of collecting, organizing, presenting, analyzing, and interpreting numerical data to make decisions under uncertainty. In Agriculture, it is extensively used to evaluate the impact of different fertilizers, seed varieties, or farming practices through statistically designed experiments."),
        ("Differentiate between Qualitative and Quantitative data with examples.", "Qualitative data refers to characteristics or attributes that cannot be measured numerically (e.g., eye color, gender, religion). Quantitative data refers to measurable quantities that can be expressed numerically (e.g., height, weight, crop yield)."),
        ("What is the difference between Discrete and Continuous variables? Give two examples of each.", "A discrete variable can only take specific, isolated values, usually integers (e.g., number of students in a class, number of accidents). A continuous variable can take any value within a given range, including fractions and decimals (e.g., temperature of a city, yield of wheat per hectare)."),
        ("Explain the difference between Primary and Secondary data. State two sources of Secondary data.", "Primary data is collected originally for the first time by the investigator for a specific study. Secondary data is data that has already been collected by someone else. Sources of secondary data include Government publications (like the Census of India) and reports by international bodies (like the WHO or FAO)."),
        ("Discuss the limitations of Statistics.", "Limitations include: 1) It deals only with quantitative data. 2) It does not study isolated individuals but aggregates of facts. 3) Statistical laws are true only on average, not exactly. 4) It can be easily misused by untrained persons."),
        ("What do you mean by scrutiny of data? Why is it necessary?", "Scrutiny of data involves checking the collected raw data for errors, omissions, and internal inconsistencies. It is necessary to ensure the accuracy and reliability of the data before any statistical analysis is performed. For example, checking if a son's age is erroneously recorded as greater than his father's."),
        ("Explain Nominal and Ordinal data with examples.", "Nominal data consists of categories that have no inherent order or ranking (e.g., Blood groups: A, B, AB, O). Ordinal data consists of categories that possess a logical rank or order (e.g., Customer satisfaction: Low, Medium, High; or Grades: A, B, C)."),
        ("Define Time Series Data and Cross-Sectional Data.", "Time Series data involves measurements of a variable taken at successive points in time (e.g., annual wheat production in India from 2010 to 2020). Cross-Sectional data involves measurements taken from multiple subjects at a single point in time (e.g., the population of various Indian states in the year 2021)."),
        ("Describe the process of Tabulation. What are its main components?", "Tabulation is the systematic presentation of numerical data in rows and columns to facilitate comparison and analysis. Its main components include a table number, title, column headings (captions), row headings (stubs), the body of the table, and footnotes/source notes."),
        ("How is statistics useful in State Administration?", "The government relies heavily on statistics for administration and policy-making. Data on population, unemployment, inflation, and income are used to formulate economic policies, allocate resources, and plan infrastructure development."),
        ("A researcher wants to study the impact of a new teaching method. Should they use primary or secondary data? Justify your answer.", "The researcher should use primary data. Since the teaching method is new, there likely isn't existing data specifically addressing its impact on their target group. They need to conduct an experiment or survey to collect original data tailored to this specific research question."),
        ("Identify the type of data for the following: a) Temperature in degrees Celsius b) Marital status c) Ranking of players in a tournament d) Number of cars produced.", "a) Continuous Quantitative b) Qualitative (Nominal) c) Qualitative (Ordinal) d) Discrete Quantitative."),
        ("Why is it said that 'Statistics deals with aggregates of facts'?", "Because a single, isolated numerical fact does not allow for comparison or meaningful analysis. For example, knowing one student's height is 160 cm is not statistics; but analyzing the heights of all students in the class to find the average is statistics."),
        ("What are internal consistencies during data scrutiny? Give an example.", "Internal consistency checks ensure that related variables do not contradict each other. For example, if a dataset records a person's age as 15 and their marital status as 'married for 10 years', this is internally inconsistent and points to a recording error."),
        ("Can qualitative attributes be subjected to statistical analysis? If so, how?", "Yes, qualitative attributes can be analyzed statistically if they are first quantified. This is typically done by assigning numerical codes (e.g., Male = 1, Female = 2) or by counting the frequencies of items falling into different qualitative categories."),
        ("A government publication provides the agricultural yield data of a state for the last 10 years. What type of data is this for a researcher analyzing it?", "For the researcher, this is Secondary data because it was collected and compiled by the government. It is also Time Series data because it represents measurements taken over a sequence of time periods (10 years)."),
        ("What is meant by the 'misuse of statistics'?", "Misuse of statistics occurs when data is manipulated, misrepresented, or analyzed using inappropriate methods to support a biased conclusion. This often happens when untrained persons ignore the limitations of the data or cherry-pick favourable statistics."),
        ("List three methods of collecting primary data.", "1) Direct personal observation/interview. 2) Indirect oral investigation. 3) Questionnaires filled out by respondents (either mailed or conducted online)."),
        ("Distinguish between Classification and Tabulation.", "Classification is the process of grouping raw data into homogeneous categories based on shared characteristics. Tabulation is the next step, where classified data is systematically arranged in rows and columns for easy viewing and analysis."),
        ("Why is the concept of 'uncertainty' central to the definition of statistics?", "Statistics involves drawing inferences about a large population based on a smaller sample. Because we do not have complete information, our conclusions cannot be 100% certain. Statistics provides tools to quantify and manage this uncertainty, allowing for rational decision-making.")
    ]
    html = '<div id="subjective" class="topic-section"><section class="section-card"><div class="exercise-section"><div class="exercise-header"><h2>Subjective Questions</h2><p>Answer in detail.</p></div><ul class="question-list">'
    for i, (q, ans) in enumerate(q_data, 1):
        html += f'''
        <li>
            <div class="question"><strong>Q{i}.</strong> {q}</div>
            <button class="get-solution-btn" data-question-id="subj-{i}">Get Solution</button>
            <div class="solution" id="solution-subj-{i}"><p>{ans}</p></div>
        </li>'''
    html += '</ul></div></section></div>'
    return html

final_html = html_template.replace("{mcq_html}", generate_mcqs()) \
    .replace("{fib_html}", generate_fib()) \
    .replace("{tf_html}", generate_tf()) \
    .replace("{subj_html}", generate_subj())

with open(r"Stat-101/Unit-I.html", "w", encoding="utf-8") as f:
    f.write(final_html)
print("Stat-101/Unit-I.html has been generated successfully.")
