import os

def generate_mcqs():
    q_data = [
        ("The word 'Statistics' is derived from the Latin word:", ["(a) Statista", "(b) Status", "(c) Statistik", "(d) Stat"], 1),
        ("Statistics deals with:", ["(a) Isolated individuals", "(b) Qualitative data only", "(c) Aggregates of facts", "(d) Mathematical certainty"], 2),
        ("Data collected originally by the investigator is called:", ["(a) Secondary Data", "(b) Grouped Data", "(c) Primary Data", "(d) Published Data"], 2),
        ("Number of students in a class is an example of:", ["(a) Continuous data", "(b) Qualitative data", "(c) Discrete data", "(d) Nominal data"], 2),
        ("Yield of wheat per acre is an example of:", ["(a) Discrete data", "(b) Continuous data", "(c) Ordinal data", "(d) Secondary data"], 1),
        ("Eye color of a person is an example of:", ["(a) Quantitative data", "(b) Continuous data", "(c) Qualitative data", "(d) Discrete data"], 2),
        ("Census of India reports are a source of:", ["(a) Primary Data", "(b) Secondary Data", "(c) Experimental Data", "(d) Unpublished Data"], 1),
        ("Data collected over different points in time is known as:", ["(a) Cross-sectional data", "(b) Time series data", "(c) Geographical data", "(d) Nominal data"], 1),
        ("Classification of data based on geographical location is:", ["(a) Chronological", "(b) Geographical", "(c) Qualitative", "(d) Quantitative"], 1),
        ("Which of the following is NOT a limitation of statistics?", ["(a) It deals with aggregates only", "(b) It is exact like mathematical laws", "(c) It can be misused", "(d) It deals only with quantitative characteristics"], 1),
        ("Data which have already been collected by someone are called:", ["(a) Primary data", "(b) Secondary data", "(c) Raw data", "(d) Fictitious data"], 1),
        ("Arranging data in rows and columns is called:", ["(a) Classification", "(b) Tabulation", "(c) Scrutiny", "(d) Editing"], 1),
        ("Checking data for internal consistency is called:", ["(a) Collection", "(b) Scrutiny", "(c) Tabulation", "(d) Presentation"], 1),
        ("The grades A, B, C, D awarded to students represent:", ["(a) Nominal data", "(b) Ordinal data", "(c) Interval data", "(d) Ratio data"], 1),
        ("Blood groups of individuals represent:", ["(a) Ordinal data", "(b) Nominal data", "(c) Discrete data", "(d) Continuous data"], 1),
        ("Which of the following is true about statistical laws?", ["(a) They are exact", "(b) They are true on average", "(c) They are always completely false", "(d) None of the above"], 1),
        ("Data collected from various countries in the year 2025 is:", ["(a) Time series data", "(b) Cross-sectional data", "(c) Ordinal data", "(d) Primary data"], 1),
        ("Which of these is a method of collecting primary data?", ["(a) Direct personal interview", "(b) RBI Bulletins", "(c) WHO reports", "(d) Statistical abstracts"], 0),
        ("A variable that can take any value between two given points is called a:", ["(a) Discrete variable", "(b) Continuous variable", "(c) Qualitative variable", "(d) Attribute"], 1),
        ("The process of grouping data according to common characteristics is:", ["(a) Tabulation", "(b) Classification", "(c) Scrutiny", "(d) Editing"], 1),
        ("In agriculture, statistics is primarily used to:", ["(a) Determine the exact number of pests", "(b) Evaluate treatment effects through designed experiments", "(c) Predict weather with 100% accuracy", "(d) Avoid the use of fertilizers"], 1),
        ("Which of the following is quantitative data?", ["(a) Religion", "(b) Gender", "(c) Height", "(d) Nationality"], 2),
        ("Which data type cannot be subjected to meaningful arithmetic operations?", ["(a) Continuous", "(b) Discrete", "(c) Nominal", "(d) Time series"], 2),
        ("Temperature recorded every hour constitutes:", ["(a) Cross-sectional data", "(b) Time series data", "(c) Nominal data", "(d) Ordinal data"], 1),
        ("A statistical table should ideally have:", ["(a) A title", "(b) Headings and subheadings", "(c) Source note", "(d) All of the above"], 3),
        ("Errors committed during data collection are called:", ["(a) Sampling errors", "(b) Non-sampling errors", "(c) Standard errors", "(d) Systematic errors"], 1),
        ("Unpublished data can be found in:", ["(a) Research journals", "(b) Government publications", "(c) Internal office records", "(d) Newspapers"], 2),
        ("Checking if the 'age of son > age of father' is a part of:", ["(a) Scrutiny for internal consistency", "(b) Tabulation", "(c) Data collection", "(d) Sampling"], 0),
        ("Number of petals on a flower is:", ["(a) Continuous", "(b) Discrete", "(c) Qualitative", "(d) Nominal"], 1),
        ("Statistics refers to both statistical data and:", ["(a) Statistical methods", "(b) Statistical errors", "(c) Statistical limitations", "(d) Statistical formulas"], 0)
    ]
    html = '''
        <div id="mcq" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">❓</span> Multiple Choice Questions — 30 Questions</h2>
                    <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
                        Click <em>Show Answer</em> to reveal the correct option and explanation.
                    </p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">❓</span> Multiple Choice Questions (बहुविकल्पीय प्रश्न) — 30 Questions</h2>
                    <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
                        सही विकल्प और स्पष्टीकरण देखने के लिए <em>Show Answer</em> पर क्लिक करें।
                    </p>
                </div>
    '''
    for i, (q, opts, ans_idx) in enumerate(q_data, 1):
        opt_html = " &nbsp;&nbsp; ".join(opts)
        ans_text = opts[ans_idx]
        html += f'''
        <div class="question">
            <strong>Q{i}.</strong> {q}
            <div class="mcq-options">
                <p>{opt_html}</p>
            </div>
        </div>
        <button class="toggle-btn" onclick="toggleAnswer('mcq{i}')">Show Answer ▼</button>
        <div class="answer" id="mcq{i}">
            <strong>Answer:</strong> {ans_text}
        </div>
        '''
    html += '</section></div>'
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
    html = '''
        <div id="fib" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">✏️</span> Fill in the Blanks — 30 Questions</h2>
                    <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
                        Click <em>Show Answer</em> to reveal the correct word.
                    </p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">✏️</span> Fill in the Blanks (रिक्त स्थान भरें) — 30 Questions</h2>
                    <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
                        सही शब्द देखने के लिए <em>Show Answer</em> पर क्लिक करें।
                    </p>
                </div>
    '''
    for i, (q, ans) in enumerate(q_data, 1):
        html += f'''
        <div class="question">
            <strong>Q{i}.</strong> {q}
        </div>
        <button class="toggle-btn" onclick="toggleAnswer('fib{i}')">Show Answer ▼</button>
        <div class="answer" id="fib{i}">
            <strong>Answer:</strong> {ans}
        </div>
        '''
    html += '</section></div>'
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
    html = '''
        <div id="tf" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">✅</span> True / False — 30 Questions</h2>
                    <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
                        Click <em>Show Answer</em> to reveal the correct statement.
                    </p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">✅</span> True / False (सही/गलत) — 30 Questions</h2>
                    <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
                        सही कथन देखने के लिए <em>Show Answer</em> पर क्लिक करें।
                    </p>
                </div>
    '''
    for i, (q, ans) in enumerate(q_data, 1):
        html += f'''
        <div class="question">
            <strong>Q{i}.</strong> {q}
        </div>
        <button class="toggle-btn" onclick="toggleAnswer('tf{i}')">Show Answer ▼</button>
        <div class="answer" id="tf{i}">
            <strong>Answer:</strong> {"True" if ans else "False"}
        </div>
        '''
    html += '</section></div>'
    return html

def generate_subj():
    q_data = [
        ("Define Statistics and discuss its scope in Agriculture.", "Statistics is the science of collecting, organizing, presenting, analyzing, and interpreting numerical data to make decisions under uncertainty. In Agriculture, it is used to evaluate the impact of different fertilizers, seed varieties, or farming practices through properly designed experiments."),
        ("Differentiate between Qualitative and Quantitative data with examples.", "Qualitative data refers to attributes that cannot be measured numerically (e.g., eye color, gender, religion). Quantitative data refers to measurable quantities that can be expressed numerically (e.g., height, weight, crop yield)."),
        ("What is the difference between Discrete and Continuous variables? Give two examples of each.", "A discrete variable can only take specific, whole values (e.g., number of students, number of cars). A continuous variable can take any value within a range, including decimals (e.g., temperature, weight of a person)."),
        ("Explain the difference between Primary and Secondary data. State two sources of Secondary data.", "Primary data is fresh data collected for the first time by a researcher. Secondary data is data already collected by someone else. Sources of secondary data include government census reports and hospital records."),
        ("Discuss the limitations of Statistics.", "Limitations include: 1) It only deals with numbers. 2) It studies groups, not single individuals. 3) Its rules are true only on average. 4) It can be misused by people who do not understand it well."),
        ("What do you mean by scrutiny of data? Why is it necessary?", "Scrutiny of data means checking raw data carefully for mistakes and missing details. It is necessary to fix errors early so that the final analysis is correct and reliable."),
        ("Explain Nominal and Ordinal data with examples.", "Nominal data has no logical order (e.g., blood groups: A, B, O). Ordinal data has a clear order or rank (e.g., grades: A, B, C, or satisfaction: Low, Medium, High)."),
        ("Define Time Series Data and Cross-Sectional Data.", "Time Series data is collected over different time periods (e.g., monthly rainfall in 2023). Cross-Sectional data is collected at a single point in time from different groups (e.g., height of all students in class today)."),
        ("Describe the process of Tabulation. What are its main components?", "Tabulation is arranging data neatly into rows and columns. A good table has a table number, a title, column headings, row headings, the main body of numbers, and a source note."),
        ("How is statistics useful in State Administration?", "Governments use statistics to make good plans. They look at data on population, jobs, and income to build roads, schools, and hospitals where they are needed most."),
        ("A researcher wants to study the impact of a new teaching method. Should they use primary or secondary data? Justify your answer.", "They should use primary data. Since the teaching method is new, there is no old data available. The researcher must collect fresh data directly from the students to see if it works."),
        ("Identify the type of data for the following: a) Temperature b) Marital status c) Ranking of players d) Number of cars produced.", "a) Continuous Quantitative b) Qualitative (Nominal) c) Qualitative (Ordinal) d) Discrete Quantitative."),
        ("Why is it said that 'Statistics deals with aggregates of facts'?", "Because a single number tells us very little. We cannot compare one person's height. But if we have the heights of all students in a class, we can find the average and compare them. This group of numbers is an aggregate."),
        ("What are internal consistencies during data scrutiny? Give an example.", "Internal consistency checks if two related answers make sense together. For example, if a form says a person is 10 years old and has been married for 5 years, it is a clear mistake. They do not match."),
        ("Can qualitative attributes be subjected to statistical analysis? If so, how?", "Yes. We can count how many people fit into each category. For example, we can count how many people have brown eyes or blue eyes. We can also assign numbers, like 1 for Yes and 0 for No."),
        ("A government publication provides the agricultural yield data of a state for the last 10 years. What type of data is this for a researcher analyzing it?", "For the researcher, this is Secondary data because the government already collected it. It is also Time Series data because it covers 10 years."),
        ("What is meant by the 'misuse of statistics'?", "Misuse happens when people change numbers or show only half the truth to prove their point. For example, a company might show a graph that makes a tiny increase in sales look like a huge jump."),
        ("List three methods of collecting primary data.", "1) Direct personal interviews. 2) Telephone surveys. 3) Questionnaires filled out by the public."),
        ("Distinguish between Classification and Tabulation.", "Classification is sorting data into groups based on their similarities (like sorting boys and girls). Tabulation is putting those sorted groups neatly into a table with rows and columns."),
        ("Why is the concept of 'uncertainty' central to the definition of statistics?", "In real life, we cannot check everyone or everything. We only check a sample. Because we do not check everything, we are never 100% sure. Statistics gives us tools to guess the correct answer and know how much error might be there.")
    ]
    html = '''
        <div id="subj" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">📝</span> Subjective Questions — 20 Questions</h2>
                    <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
                        Answer the following questions in detail. Think about the concepts and real-life examples before clicking <em>Show Answer</em>.
                    </p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">📝</span> Subjective Questions (विषयपरक प्रश्न) — 20 Questions</h2>
                    <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
                        निम्नलिखित प्रश्नों के उत्तर विस्तार से दें। <em>Show Answer</em> पर क्लिक करने से पहले Concepts और वास्तविक जीवन के उदाहरणों के बारे में सोचें।
                    </p>
                </div>
    '''
    for i, (q, ans) in enumerate(q_data, 1):
        html += f'''
        <div class="question">
            <strong>Q{i}.</strong> {q}
        </div>
        <button class="toggle-btn" onclick="toggleAnswer('subj{i}')">Show Answer ▼</button>
        <div class="answer" id="subj{i}">
            <p>{ans}</p>
        </div>
        '''
    html += '</section></div>'
    return html

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unit I – Introduction & Data Collection | STAT-M-101</title>
    
    <!-- MathJax -->
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700&family=Source+Serif+4:ital,wght@0,400;0,600&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
    
    <link rel="stylesheet" href="../common_style.css">
    <link rel="stylesheet" href="../whiteboard/whiteboard.css">

    <style>
        .chapter-header { position: relative; }
        .header-lang-toggle {
            position: absolute; top: 20px; right: 30px;
            background: rgba(255, 255, 255, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.4);
            color: #fff; padding: 6px 14px; border-radius: 20px;
            font-family: 'DM Sans', sans-serif; font-size: 0.85rem; font-weight: 600;
            cursor: pointer; transition: all 0.3s;
            display: inline-flex; align-items: center; gap: 6px;
        }
        .header-lang-toggle:hover { background: rgba(255, 255, 255, 0.3); transform: translateY(-2px); }

        /* ── EXERCISE SPECIFIC CSS FROM STAT-102 ─────────────────────── */
        .question {
            background: #fff;
            border: 1px solid var(--border);
            border-left: 4px solid var(--navy-light);
            padding: 16px 20px;
            margin: 14px 0 6px;
            border-radius: 0 8px 8px 0;
            font-size: 1rem;
            color: var(--text-dark);
            line-height: 1.7;
        }

        .question strong { color: var(--navy); }
        .mcq-options p { margin: 8px 0 0; color: var(--text-mid); font-size: .95rem; }

        .toggle-btn {
            background: var(--navy);
            color: #fff;
            border: none;
            padding: 7px 18px;
            border-radius: 20px;
            cursor: pointer;
            font-family: 'DM Sans', sans-serif;
            font-size: .82rem;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: all .25s;
            margin: 4px 0 8px;
            letter-spacing: .3px;
        }

        .toggle-btn:hover {
            background: var(--navy-light);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(27,42,74,.3);
        }

        .answer {
            display: none;
            background: #F0FBF5;
            border-left: 4px solid var(--sage);
            padding: 16px 20px;
            margin: 2px 0 12px;
            border-radius: 0 8px 8px 0;
            animation: fadeSlideIn .3s ease;
            color: var(--text-dark) !important;
            font-size: .97rem;
            line-height: 1.75;
        }
        
        .answer.show { display: block; }

        .section-card h3, .section-card h4 {
            font-family: 'Playfair Display', serif;
            color: var(--navy-light);
            margin: 28px 0 12px;
        }
        .section-card h3 { font-size: 1.35rem; font-weight: 700; }
        .section-card h4 { font-size: 1.15rem; font-weight: 600; }
    </style>
</head>
<body>
    <header class="book-header">
        <button class="menu-toggle" onclick="toggleSidebar()" aria-label="Toggle menu">
            <i class="fas fa-bars"></i>
        </button>
        <div class="header-icon">📈</div>
        <div class="header-text">
            <h1>Statistical Methods-I</h1>
            <div class="subtitle">UNIT I · INTRODUCTION & DATA COLLECTION</div>
        </div>
        
        <div class="header-badge">Prof. O.P. Sheoran</div>
        <button class="draw-mode-toggle" id="draw-mode-btn">
            <i class="fas fa-chalkboard"></i> Open Whiteboard
        </button>
    </header>

    <nav class="sidebar" id="sidebar">
        <div class="sidebar-brand">
            <h2>Unit I</h2>
            <p>Introduction & Data<br>CCS Haryana Agricultural University</p>
        </div>
        <div class="sidebar-author">
            <img src="../Stat-102/opsheoran.png" alt="Prof. O.P. Sheoran" class="sidebar-photo">
            <div class="sidebar-author-info">
                <h3>Prof. O.P. Sheoran</h3>
                <p>Author & Instructor</p>
            </div>
        </div>

        <div class="nav-group-label">Navigation</div>
        <ul class="nav-list">
            <li class="nav-item"><a class="nav-link" href="index.html" style="background: rgba(200,146,42,0.1); color: var(--gold-light); font-weight: 600;"><span class="nav-num">🏠</span> Course Home</a></li>
            <li class="nav-item"><a class="nav-link" href="../index.html" style="background: rgba(27,42,74,0.3); color: white; font-weight: 600; margin-top: 5px;"><span class="nav-num">📚</span> Back to Library</a></li>
        </ul>

        <div class="nav-group-label">Main Concepts</div>
        <ul class="nav-list">
            <li class="nav-item"><a class="nav-link active" href="#" onclick="showTopic('sec1-1');return false;"><span class="nav-num">1.1</span> Introduction</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('sec1-2');return false;"><span class="nav-num">1.2</span> What is Statistics?</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('sec1-3');return false;"><span class="nav-num">1.3</span> Scope of Statistics</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('sec1-4');return false;"><span class="nav-num">1.4</span> Advantages of Statistics</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('sec1-5');return false;"><span class="nav-num">1.5</span> Limitations of Statistics</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('sec1-6');return false;"><span class="nav-num">1.6</span> Areas of Application</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('sec1-7');return false;"><span class="nav-num">1.7</span> Conclusion</a></li>
        </ul>
        
        <div class="nav-group-label">Exercises</div>
        <ul class="nav-list">
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('mcq');return false;"><span class="nav-num">❓</span> Multiple Choice</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('fib');return false;"><span class="nav-num">✏️</span> Fill in Blanks</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('tf');return false;"><span class="nav-num">✅</span> True / False</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('subj');return false;"><span class="nav-num">📝</span> Subjective Qs</a></li>
        </ul>
    </nav>

    <main class="main-content">
        <div class="chapter-header">
            <button id="lang-toggle-btn" class="header-lang-toggle" onclick="toggleLanguage()">
                <i class="fas fa-language"></i> <span id="lang-toggle-text">Read in Hinglish</span>
            </button>
            <h1>Unit I: Introduction & Data Collection</h1>
            <div class="author">By Prof. O.P. Sheoran</div>
            <div class="syllabus-tag">
                <strong>Syllabus:</strong> Origin, development, definition, scope, uses, limitations. Types of Data. Collection and Scrutiny of Data.
            </div>
        </div>

        <!-- SECTION 1.1: INTRODUCTION -->
        <div id="sec1-1" class="topic-section active">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">1.1</span> Introduction</h2>
                    <p>Hello students! Welcome to the BSc First Year <strong>Statistics</strong> course. Statistics is very important today. Every day, computers and phones create huge amounts of data. Because of this, we need people who know statistics to understand the data.</p>
                    <p>In this course, you will learn what statistics is. You will learn its uses, benefits, and limits. We will use simple examples from daily life and from Haryana to make it easy.</p>

                    <h3>Historical Development</h3>
                    <p>Statistics started a very long time ago. Old governments collected data about their people, taxes, and armies. This helped them run their empires well. In India, a famous book called Kautilya's Arthashastra shows that kings kept records of farming and trade around 300 BCE.</p>
                    <p>In Europe, people started studying birth and death records in the 17th century. Later, scientists created "Probability Theory". This made statistics a real science. Today, with fast computers, statistics is used everywhere.</p>

                    <h3>Development of Statistics in India</h3>
                    <p>India has a rich history in statistics. After independence, this field grew very fast. Professor P.C. Mahalanobis is called the father of Indian statistics. In 1931, he started the famous Indian Statistical Institute (ISI) in Kolkata. He also helped make India's Second Five-Year Plan.</p>
                    <p>In 1950, the government started the National Sample Survey Office (NSSO). In Haryana, the State Statistics Department collects data on farming, health, and schools to make good plans for the people.</p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">1.1</span> Introduction (परिचय)</h2>
                    <p>Hello students! BSc First Year <strong>Statistics</strong> course में आपका स्वागत है। आज के समय में Statistics बहुत महत्वपूर्ण है। हर दिन, फ़ोन और कंप्यूटर बहुत सारा <strong>data</strong> बनाते हैं। इसलिए, हमें ऐसे लोगों की आवश्यकता है जो data को समझने के लिए statistics जानते हों।</p>
                    <p>इस course में, आप सीखेंगे कि statistics क्या है। आप इसके उपयोग, लाभ और सीमाएं (limits) सीखेंगे। हम इसे आसान बनाने के लिए daily life और हरियाणा के simple examples का उपयोग करेंगे।</p>

                    <h3>Historical Development (ऐतिहासिक विकास)</h3>
                    <p>Statistics की शुरुआत बहुत पहले हुई थी। पुरानी सरकारें अपने लोगों, taxes और सेना के बारे में data एकत्र करती थीं। इससे उन्हें अपने राज्यों को अच्छी तरह से चलाने में मदद मिलती थी। भारत में, कौटिल्य के अर्थशास्त्र (लगभग 300 BCE) से पता चलता है कि राजा खेती और व्यापार का record रखते थे।</p>
                    <p>यूरोप में, लोगों ने 17वीं शताब्दी में जन्म और मृत्यु के रिकॉर्ड का अध्ययन करना शुरू किया। बाद में, वैज्ञानिकों ने "Probability Theory" बनाई। इससे statistics एक वास्तविक विज्ञान बन गया। आज तेज़ कंप्यूटरों के साथ, statistics का उपयोग हर जगह किया जाता है।</p>

                    <h3>Development of Statistics in India (भारत में सांख्यिकी का विकास)</h3>
                    <p>भारत में statistics का एक समृद्ध इतिहास है। आजादी के बाद, यह क्षेत्र बहुत तेज़ी से बढ़ा। Professor P.C. Mahalanobis को भारतीय सांख्यिकी का जनक (father of Indian statistics) कहा जाता है। 1931 में, उन्होंने कोलकाता में प्रसिद्ध Indian Statistical Institute (ISI) की स्थापना की। उन्होंने भारत की द्वितीय पंचवर्षीय योजना बनाने में भी मदद की।</p>
                    <p>1950 में, सरकार ने National Sample Survey Office (NSSO) शुरू किया। हरियाणा में, State Statistics Department खेती, स्वास्थ्य और स्कूलों पर data एकत्र करता है ताकि लोगों के लिए अच्छी योजनाएं बनाई जा सकें।</p>
                </div>
            </section>
        </div>

        <!-- SECTION 1.2: WHAT IS STATISTICS -->
        <div id="sec1-2" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">1.2</span> What is Statistics?</h2>
                    <p>Statistics is the science of collecting, organizing, analyzing, and presenting data. It helps us make good decisions even when we are not completely sure about the future.</p>
                    <p>We look at statistics in two ways:</p>
                    <ul>
                        <li><strong>Numerical facts:</strong> A collection of numbers. For example, student marks or cricket scores.</li>
                        <li><strong>Analytical method:</strong> The maths and tools we use to study those numbers.</li>
                    </ul>

                    <h3>Types of Statistics</h3>
                    <p>We divide statistics into two main parts:</p>
                    <ul>
                        <li><strong>Descriptive Statistics:</strong> This helps us summarize data to get a quick picture. We use the Mean, Median, and Mode to find the center. We use Bar Charts and Pie Charts to show data in pictures.</li>
                        <li><strong>Inferential Statistics:</strong> This helps us make guesses about a large group based on a small sample. We use it to test claims and make predictions. For example, checking 500 farms to guess the total wheat production of Haryana.</li>
                    </ul>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">1.2</span> What is Statistics? (सांख्यिकी क्या है?)</h2>
                    <p>Statistics data को collect, organize, analyze, और present करने का विज्ञान है। यह हमें सही निर्णय लेने में मदद करता है, तब भी जब हम भविष्य के बारे में पूरी तरह सुनिश्चित (completely sure) नहीं होते हैं।</p>
                    <p>हम statistics को दो तरीकों से देखते हैं:</p>
                    <ul>
                        <li><strong>Numerical facts (संख्यात्मक तथ्य):</strong> संख्याओं का एक collection। उदाहरण के लिए, छात्रों के अंक या क्रिकेट के स्कोर।</li>
                        <li><strong>Analytical method (विश्लेषणात्मक विधि):</strong> उन संख्याओं का अध्ययन करने के लिए हम जिन maths और tools का उपयोग करते हैं।</li>
                    </ul>

                    <h3>Types of Statistics (सांख्यिकी के प्रकार)</h3>
                    <p>हम statistics को दो मुख्य भागों में बाँटते हैं:</p>
                    <ul>
                        <li><strong>Descriptive Statistics (वर्णनात्मक सांख्यिकी):</strong> यह data को summarize करने में मदद करता है ताकि एक त्वरित तस्वीर (quick picture) मिल सके। हम केंद्र खोजने के लिए Mean, Median, और Mode का उपयोग करते हैं। हम data को चित्रों में दिखाने के लिए Bar Charts और Pie Charts का उपयोग करते हैं।</li>
                        <li><strong>Inferential Statistics (अनुमानात्मक सांख्यिकी):</strong> यह हमें एक छोटे sample के आधार पर एक बड़े समूह (large group) के बारे में अनुमान लगाने में मदद करता है। हम इसका उपयोग दावों का परीक्षण करने और भविष्यवाणी करने के लिए करते हैं। उदाहरण के लिए, हरियाणा के कुल गेहूं उत्पादन का अनुमान लगाने के लिए 500 खेतों की जांच करना।</li>
                    </ul>
                </div>
            </section>
        </div>

        <!-- SECTION 1.3: SCOPE OF STATISTICS -->
        <div id="sec1-3" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">1.3</span> Scope of Statistics</h2>
                    <p>Statistics is used in almost every area of life. The main steps of statistical work are:</p>

                    <h3>Data Collection</h3>
                    <p>The first step is to get the data. We use sampling methods so we don't have to check everyone. For example, "Random Sampling" is like picking names from a hat. We collect data by using written questionnaires or talking to people in interviews.</p>

                    <h3>Data Organization</h3>
                    <p>Raw data is messy. We have to sort it and arrange it in tables so we can read it easily. We can sort data by qualities (like gender), by numbers (like age), or by time (like months). We also draw graphs to make the numbers look clear.</p>

                    <h3>Data Analysis</h3>
                    <p>After sorting, we analyze the numbers. We find the average to see the center. We also look at how much the numbers vary. This helps us understand the true meaning of the data.</p>

                    <h3>Inference and Decision Making</h3>
                    <p>The final step is to make a decision. Even if our data is only a small sample, statistics helps us guess the truth with high confidence. This helps leaders and businesses make smart choices.</p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">1.3</span> Scope of Statistics (सांख्यिकी का कार्यक्षेत्र)</h2>
                    <p>Statistics का उपयोग जीवन के लगभग हर क्षेत्र में किया जाता है। Statistical कार्य के मुख्य steps हैं:</p>

                    <h3>Data Collection (डेटा संग्रह)</h3>
                    <p>पहला कदम data प्राप्त करना है। हम sampling methods का उपयोग करते हैं ताकि हमें हर किसी की जांच न करनी पड़े। उदाहरण के लिए, "Random Sampling" एक टोपी से नाम चुनने जैसा है। हम लिखित प्रश्नावली (questionnaires) का उपयोग करके या साक्षात्कार (interviews) में लोगों से बात करके data एकत्र करते हैं।</p>

                    <h3>Data Organization (डेटा संगठन)</h3>
                    <p>Raw data बहुत बिखरा हुआ (messy) होता है। हमें इसे छांटना (sort) होगा और tables में व्यवस्थित करना होगा ताकि हम इसे आसानी से पढ़ सकें। हम data को गुणों (जैसे लिंग), संख्याओं (जैसे आयु), या समय (जैसे महीनों) के आधार पर छांट सकते हैं। संख्याओं को स्पष्ट दिखाने के लिए हम ग्राफ़ भी बनाते हैं।</p>

                    <h3>Data Analysis (डेटा विश्लेषण)</h3>
                    <p>Sorting के बाद, हम संख्याओं का विश्लेषण (analyze) करते हैं। हम केंद्र देखने के लिए औसत (average) निकालते हैं। हम यह भी देखते हैं कि संख्याएं कितनी बदलती हैं (vary)। इससे हमें data का सही अर्थ समझने में मदद मिलती है।</p>

                    <h3>Inference and Decision Making (अनुमान और निर्णय लेना)</h3>
                    <p>अंतिम कदम निर्णय लेना है। भले ही हमारा data केवल एक छोटा sample है, statistics हमें उच्च विश्वास (high confidence) के साथ सच्चाई का अनुमान लगाने में मदद करता है। इससे नेताओं और व्यवसायों को smart विकल्प (smart choices) चुनने में मदद मिलती है।</p>
                </div>
            </section>
        </div>

        <!-- SECTION 1.4: ADVANTAGES OF STATISTICS -->
        <div id="sec1-4" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">1.4</span> Advantages of Statistics</h2>
                    <p>Why do we learn statistics? Here are the simple benefits:</p>
                    <ul>
                        <li><strong>Turns words into numbers:</strong> It turns vague ideas into solid numbers, like "85% of people are happy".</li>
                        <li><strong>Helps in clear thinking:</strong> We don't have to guess. We can make logical decisions based on facts.</li>
                        <li><strong>Finds hidden patterns:</strong> It draws graphs to show if sales are going up or down.</li>
                        <li><strong>Predicts the future:</strong> By looking at past data, it helps us predict what might happen next year.</li>
                    </ul>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">1.4</span> Advantages of Statistics (सांख्यिकी के लाभ)</h2>
                    <p>हम statistics क्यों सीखते हैं? यहाँ कुछ सरल लाभ (benefits) दिए गए हैं:</p>
                    <ul>
                        <li><strong>शब्दों को संख्याओं में बदलता है:</strong> यह अस्पष्ट विचारों (vague ideas) को ठोस संख्याओं में बदलता है, जैसे "85% लोग खुश हैं"।</li>
                        <li><strong>स्पष्ट सोच में मदद करता है:</strong> हमें अनुमान नहीं लगाना पड़ता है। हम तथ्यों (facts) के आधार पर तार्किक निर्णय (logical decisions) ले सकते हैं।</li>
                        <li><strong>छिपे हुए patterns ढूंढता है:</strong> यह दिखाने के लिए ग्राफ़ बनाता है कि बिक्री (sales) ऊपर जा रही है या नीचे।</li>
                        <li><strong>भविष्य की भविष्यवाणी करता है:</strong> पिछले data को देखकर, यह हमें भविष्यवाणी करने में मदद करता है कि अगले साल क्या हो सकता है।</li>
                    </ul>
                </div>
            </section>
        </div>

        <!-- SECTION 1.5: LIMITATIONS OF STATISTICS -->
        <div id="sec1-5" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">1.5</span> Limitations of Statistics</h2>
                    <p>Statistics is very useful, but it has some weak points:</p>
                    <ul>
                        <li><strong>It only likes numbers:</strong> It cannot directly study honesty or beauty. We have to give them numbers first.</li>
                        <li><strong>It ignores the individual:</strong> It only cares about the group average. It doesn't tell us about one specific person.</li>
                        <li><strong>It is not exactly perfect:</strong> Statistical rules are only true on average. There is always a small chance of error.</li>
                        <li><strong>It can be misused:</strong> People can hide facts or use wrong data to trick others.</li>
                    </ul>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">1.5</span> Limitations of Statistics (सांख्यिकी की सीमाएं)</h2>
                    <p>Statistics बहुत उपयोगी है, लेकिन इसके कुछ कमजोर बिंदु (weak points) हैं:</p>
                    <ul>
                        <li><strong>यह केवल संख्याओं को पसंद करता है:</strong> यह सीधे ईमानदारी (honesty) या सुंदरता का अध्ययन नहीं कर सकता। हमें पहले उन्हें नंबर देने होंगे।</li>
                        <li><strong>यह व्यक्ति (individual) को ignore करता है:</strong> यह केवल समूह के औसत (group average) की परवाह करता है। यह हमें किसी एक विशिष्ट व्यक्ति के बारे में नहीं बताता।</li>
                        <li><strong>यह पूरी तरह से perfect नहीं है:</strong> Statistical नियम केवल औसतन सत्य होते हैं। इसमें हमेशा error की थोड़ी गुंजाइश होती है।</li>
                        <li><strong>इसका दुरुपयोग (misuse) किया जा सकता है:</strong> लोग दूसरों को मूर्ख बनाने के लिए तथ्यों को छिपा सकते हैं या गलत data का उपयोग कर सकते हैं।</li>
                    </ul>
                </div>
            </section>
        </div>

        <!-- SECTION 1.6: AREAS OF APPLICATION -->
        <div id="sec1-6" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">1.6</span> Areas of Application</h2>
                    <p>Today, statistics is used everywhere. It helps people in almost every job make better choices. Here are some clear examples:</p>
                    
                    <h3>Science and Research</h3>
                    <p>Scientists use statistics to test their ideas and check experiment results.<br>
                    <em>Example:</em> A researcher wants to know which fertilizer is better. They use Fertilizer A on one field and Fertilizer B on another. They collect crop yield data and use a statistical test to prove which one is truly better.</p>

                    <h3>Social Sciences</h3>
                    <p>Social scientists use statistics to study human behavior and population trends.<br>
                    <em>Example:</em> The government conducts the National Family Health Survey. They use statistical sampling to gather data on nutrition and family planning. This helps them understand society's needs.</p>

                    <h3>Business and Finance</h3>
                    <p>Companies use data to understand what customers want to buy and to manage risks.<br>
                    <em>Example:</em> A mobile phone company looks at the sales data of the last 5 years. Using time series analysis, they predict they will sell more phones during Diwali. So, they produce enough phones before the festival starts.</p>

                    <h3>Government and Policy</h3>
                    <p>The government needs statistics to build the country and help the people.<br>
                    <em>Example:</em> The government counts the population (Census). If the data shows a district has many young children, the government uses this data to build more schools and parks there.</p>

                    <h3>Technology and Computing</h3>
                    <p>Tech companies use statistics to build Artificial Intelligence (AI) and Machine Learning models.<br>
                    <em>Example:</em> AI systems use probability to recognize your face on a phone. Video apps use statistics of your past choices to suggest the next video you should watch.</p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">1.6</span> Areas of Application (अनुप्रयोग के क्षेत्र)</h2>
                    <p>आज, statistics का हर जगह उपयोग किया जाता है। यह लगभग हर काम में लोगों को बेहतर विकल्प (better choices) चुनने में मदद करता है। यहाँ कुछ स्पष्ट उदाहरण (clear examples) दिए गए हैं:</p>
                    
                    <h3>Science and Research (विज्ञान और अनुसंधान)</h3>
                    <p>वैज्ञानिक अपने विचारों (ideas) का परीक्षण करने और प्रयोग के परिणामों (experiment results) की जांच करने के लिए statistics का उपयोग करते हैं。<br>
                    <em>उदाहरण:</em> एक शोधकर्ता (researcher) जानना चाहता है कि कौन सा उर्वरक (fertilizer) बेहतर है। वे एक खेत में Fertilizer A और दूसरे में Fertilizer B का उपयोग करते हैं। वे फसल की उपज का data एकत्र करते हैं और यह साबित करने के लिए एक statistical test का उपयोग करते हैं कि वास्तव में कौन सा बेहतर है।</p>

                    <h3>Social Sciences (सामाजिक विज्ञान)</h3>
                    <p>सामाजिक वैज्ञानिक (Social scientists) मानव व्यवहार (human behavior) और जनसंख्या के trends का अध्ययन करने के लिए statistics का उपयोग करते हैं。<br>
                    <em>उदाहरण:</em> सरकार राष्ट्रीय परिवार स्वास्थ्य सर्वेक्षण (National Family Health Survey) आयोजित करती है। वे पोषण (nutrition) और परिवार नियोजन पर data एकत्र करने के लिए statistical sampling का उपयोग करते हैं। इससे उन्हें समाज की जरूरतों को समझने में मदद मिलती है।</p>

                    <h3>Business and Finance (व्यापार और वित्त)</h3>
                    <p>कंपनियां यह समझने के लिए data का उपयोग करती हैं कि ग्राहक क्या खरीदना चाहते हैं और risks का प्रबंधन (manage) कैसे करें。<br>
                    <em>उदाहरण:</em> एक मोबाइल फोन कंपनी पिछले 5 वर्षों के बिक्री data को देखती है। time series analysis का उपयोग करके, वे भविष्यवाणी (predict) करते हैं कि वे दिवाली के दौरान अधिक फोन बेचेंगे। इसलिए, वे त्योहार शुरू होने से पहले पर्याप्त फोन का उत्पादन (produce) करते हैं।</p>

                    <h3>Government and Policy (सरकार और नीति)</h3>
                    <p>देश के निर्माण और लोगों की मदद के लिए सरकार को statistics की आवश्यकता होती है。<br>
                    <em>उदाहरण:</em> सरकार जनसंख्या की गिनती (Census) करती है। यदि data से पता चलता है कि किसी जिले में छोटे बच्चों की संख्या अधिक है, तो सरकार वहां अधिक स्कूल और पार्क बनाने के लिए इस data का उपयोग करती है।</p>

                    <h3>Technology and Computing (प्रौद्योगिकी और कंप्यूटिंग)</h3>
                    <p>Tech कंपनियां आर्टिफिशियल इंटेलिजेंस (AI) और मशीन लर्निंग मॉडल बनाने के लिए statistics का उपयोग करती हैं。<br>
                    <em>उदाहरण:</em> AI सिस्टम फ़ोन पर आपका चेहरा पहचानने के लिए probability का उपयोग करते हैं। Video ऐप्स आपके पिछले विकल्पों (past choices) के statistics का उपयोग करके आपको यह सुझाव देते हैं कि आपको अगला कौन सा वीडियो देखना चाहिए।</p>
                </div>
            </section>
        </div>

        <!-- SECTION 1.7: CONCLUSION -->
        <div id="sec1-7" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">1.7</span> Conclusion</h2>
                    <p>In this chapter, we learned that statistics is a broad subject. It deals with collecting, organizing, analyzing, and presenting data. We learned about descriptive statistics (which summarizes data) and inferential statistics (which helps us draw conclusions from a sample).</p>
                    <p>Statistics has many advantages, like helping us make evidence-based decisions. It also has limits, as it ignores individual facts. Still, statistics gives us the power to tell stories through numbers. It is truly a guiding lighthouse in the sea of uncertainty.</p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">1.7</span> Conclusion (निष्कर्ष)</h2>
                    <p>इस अध्याय में, हमने सीखा कि statistics एक व्यापक (broad) विषय है। यह data को collect, organize, analyze और present करने से संबंधित है। हमने descriptive statistics (जो data को summarize करती है) और inferential statistics (जो हमें sample से निष्कर्ष निकालने में मदद करती है) के बारे में सीखा।</p>
                    <p>Statistics के कई फायदे हैं, जैसे साक्ष्य-आधारित (evidence-based) निर्णय लेने में हमारी मदद करना। इसकी सीमाएँ (limits) भी हैं, क्योंकि यह individual facts को अनदेखा करता है। फिर भी, statistics हमें संख्याओं के माध्यम से कहानियाँ बताने की शक्ति देता है। यह अनिश्चितता के समुद्र में वास्तव में एक मार्गदर्शक प्रकाशस्तंभ (guiding lighthouse) है।</p>
                </div>
            </section>
        </div>

        <!-- EXERCISES INJECTED HERE -->
        {EXERCISES_PLACEHOLDER}

    </main>

    <script>
        let isHinglish = false;
        function toggleLanguage() {
            isHinglish = !isHinglish;
            const btnText = document.getElementById('lang-toggle-text');
            const engContents = document.querySelectorAll('.english-content');
            const hinContents = document.querySelectorAll('.hinglish-content');

            if (isHinglish) {
                btnText.textContent = 'Read in English';
                engContents.forEach(el => el.style.display = 'none');
                hinContents.forEach(el => el.style.display = 'block');
            } else {
                btnText.textContent = 'Read in Hinglish';
                hinContents.forEach(el => el.style.display = 'none');
                engContents.forEach(el => el.style.display = 'block');
            }
        }

        function showTopic(id) {
            document.querySelectorAll('.topic-section').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-link').forEach(el => el.classList.remove('active'));
            
            const targetSection = document.getElementById(id);
            if (targetSection) {
                targetSection.classList.add('active');
            }
            
            const activeLink = document.querySelector(`a[onclick*="'${id}'"]`);
            if (activeLink) {
                activeLink.classList.add('active');
            }
            
            window.scrollTo(0,0);
            
            if (window.innerWidth <= 768) {
                document.getElementById('sidebar').classList.remove('open');
            }
        }

        function toggleSidebar() {
            document.getElementById('sidebar').classList.toggle('open');
        }

        /* ── TOGGLE ANSWER LOGIC FROM STAT-102 ───────────────────────── */
        function toggleAnswer(id) {
            const answer = document.getElementById(id);
            const btn = event.target;
            if (answer.classList.contains('show')) {
                answer.classList.remove('show');
                btn.innerHTML = 'Show Answer ▼';
            } else {
                answer.classList.add('show');
                btn.innerHTML = 'Hide Answer ▲';
            }
        }
    </script>
    <script src="../whiteboard/whiteboard.js?v=2.0"></script>
</body>
</html>
"""

exercises_html = generate_mcqs() + generate_fib() + generate_tf() + generate_subj()
final_html = html_template.replace('{EXERCISES_PLACEHOLDER}', exercises_html)

with open('Stat-101/Unit-I.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Stat-101/Unit-I.html generated successfully with verbatim headings.")
