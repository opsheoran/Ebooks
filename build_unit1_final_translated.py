import os
import urllib.request, urllib.parse, json, re, time
from bs4 import BeautifulSoup

def translate_text(text):
    if not text.strip() or not re.search('[a-zA-Z]', text):
        return text
    try:
        q = urllib.parse.quote(text.strip())
        url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=hi&dt=t&q={q}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        translated = "".join([chunk[0] for chunk in data[0] if chunk[0]])
        
        # Restore leading/trailing spaces
        prefix = ' ' if text.startswith(' ') or text.startswith('\n') else ''
        suffix = ' ' if text.endswith(' ') or text.endswith('\n') else ''
        return prefix + translated + suffix
    except Exception as e:
        return text

def t(text):
    return translate_text(text)

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
    
    eng_content = '''
        <h2><span class="section-num">❓</span> Multiple Choice Questions — 30 Questions</h2>
        <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
            Click <em>Show Answer</em> to reveal the correct option and explanation.
        </p>
    '''
    hin_content = '''
        <h2><span class="section-num">❓</span> Multiple Choice Questions (बहुविकल्पीय प्रश्न) — 30 Questions</h2>
        <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
            सही विकल्प देखने के लिए <em>Show Answer</em> पर क्लिक करें।
        </p>
    '''
    
    for i, (q, opts, ans_idx) in enumerate(q_data, 1):
        # English
        opt_html = " &nbsp;&nbsp; ".join(opts)
        ans_text = opts[ans_idx]
        eng_content += f'''
        <div class="question">
            <strong>Q{i}.</strong> {q}
            <div class="mcq-options">
                <p>{opt_html}</p>
            </div>
        </div>
        <button class="toggle-btn" onclick="toggleAnswer('mcq-eng-{i}')">Show Answer ▼</button>
        <div class="answer" id="mcq-eng-{i}">
            <strong>Answer:</strong> {ans_text}
        </div>
        '''
        # Hindi
        q_hi = t(q)
        opts_hi = [t(opt) for opt in opts]
        ans_text_hi = opts_hi[ans_idx]
        opt_html_hi = " &nbsp;&nbsp; ".join(opts_hi)
        hin_content += f'''
        <div class="question">
            <strong>Q{i}.</strong> {q_hi}
            <div class="mcq-options">
                <p>{opt_html_hi}</p>
            </div>
        </div>
        <button class="toggle-btn" onclick="toggleAnswer('mcq-hin-{i}')">Show Answer ▼</button>
        <div class="answer" id="mcq-hin-{i}">
            <strong>Answer:</strong> {ans_text_hi}
        </div>
        '''
        
    return f'''
        <div id="mcq" class="topic-section">
            <section class="section-card">
                <div class="english-content">{eng_content}</div>
                <div class="hinglish-content" style="display:none;">{hin_content}</div>
            </section>
        </div>
    '''

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
    eng_content = '''
        <h2><span class="section-num">✏️</span> Fill in the Blanks — 30 Questions</h2>
        <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
            Click <em>Show Answer</em> to reveal the correct word.
        </p>
    '''
    hin_content = '''
        <h2><span class="section-num">✏️</span> Fill in the Blanks (रिक्त स्थान भरें) — 30 Questions</h2>
        <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
            सही शब्द देखने के लिए <em>Show Answer</em> पर क्लिक करें।
        </p>
    '''
    for i, (q, ans) in enumerate(q_data, 1):
        eng_content += f'''
        <div class="question"><strong>Q{i}.</strong> {q}</div>
        <button class="toggle-btn" onclick="toggleAnswer('fib-eng-{i}')">Show Answer ▼</button>
        <div class="answer" id="fib-eng-{i}"><strong>Answer:</strong> {ans}</div>
        '''
        hin_content += f'''
        <div class="question"><strong>Q{i}.</strong> {t(q)}</div>
        <button class="toggle-btn" onclick="toggleAnswer('fib-hin-{i}')">Show Answer ▼</button>
        <div class="answer" id="fib-hin-{i}"><strong>Answer:</strong> {t(ans)}</div>
        '''
    return f'''
        <div id="fib" class="topic-section">
            <section class="section-card">
                <div class="english-content">{eng_content}</div>
                <div class="hinglish-content" style="display:none;">{hin_content}</div>
            </section>
        </div>
    '''

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
    eng_content = '''
        <h2><span class="section-num">✅</span> True / False — 30 Questions</h2>
        <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
            Click <em>Show Answer</em> to reveal the correct statement.
        </p>
    '''
    hin_content = '''
        <h2><span class="section-num">✅</span> True / False (सही/गलत) — 30 Questions</h2>
        <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
            सही कथन देखने के लिए <em>Show Answer</em> पर क्लिक करें।
        </p>
    '''
    for i, (q, ans) in enumerate(q_data, 1):
        ans_txt = "True" if ans else "False"
        eng_content += f'''
        <div class="question"><strong>Q{i}.</strong> {q}</div>
        <button class="toggle-btn" onclick="toggleAnswer('tf-eng-{i}')">Show Answer ▼</button>
        <div class="answer" id="tf-eng-{i}"><strong>Answer:</strong> {ans_txt}</div>
        '''
        ans_txt_hi = "सही (True)" if ans else "गलत (False)"
        hin_content += f'''
        <div class="question"><strong>Q{i}.</strong> {t(q)}</div>
        <button class="toggle-btn" onclick="toggleAnswer('tf-hin-{i}')">Show Answer ▼</button>
        <div class="answer" id="tf-hin-{i}"><strong>Answer:</strong> {ans_txt_hi}</div>
        '''
    return f'''
        <div id="tf" class="topic-section">
            <section class="section-card">
                <div class="english-content">{eng_content}</div>
                <div class="hinglish-content" style="display:none;">{hin_content}</div>
            </section>
        </div>
    '''

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
    eng_content = '''
        <h2><span class="section-num">📝</span> Subjective Questions — 20 Questions</h2>
        <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
            Answer the following questions in detail. Think about the concepts and real-life examples before clicking <em>Show Answer</em>.
        </p>
    '''
    hin_content = '''
        <h2><span class="section-num">📝</span> Subjective Questions (विषयपरक प्रश्न) — 20 Questions</h2>
        <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
            निम्नलिखित प्रश्नों के उत्तर विस्तार से दें। <em>Show Answer</em> पर क्लिक करने से पहले Concepts और वास्तविक जीवन के उदाहरणों के बारे में सोचें।
        </p>
    '''
    for i, (q, ans) in enumerate(q_data, 1):
        eng_content += f'''
        <div class="question"><strong>Q{i}.</strong> {q}</div>
        <button class="toggle-btn" onclick="toggleAnswer('subj-eng-{i}')">Show Answer ▼</button>
        <div class="answer" id="subj-eng-{i}"><p>{ans}</p></div>
        '''
        hin_content += f'''
        <div class="question"><strong>Q{i}.</strong> {t(q)}</div>
        <button class="toggle-btn" onclick="toggleAnswer('subj-hin-{i}')">Show Answer ▼</button>
        <div class="answer" id="subj-hin-{i}"><p>{t(ans)}</p></div>
        '''
    return f'''
        <div id="subj" class="topic-section">
            <section class="section-card">
                <div class="english-content">{eng_content}</div>
                <div class="hinglish-content" style="display:none;">{hin_content}</div>
            </section>
        </div>
    '''


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

        .section-card h2 {
            font-family: 'Playfair Display', serif;
            font-size: 1.85rem;
            font-weight: 700;
            color: var(--navy);
            margin: 40px 0 20px;
            padding-bottom: 14px;
            border-bottom: 2px solid var(--border);
        }

        .section-card h3, .section-card h4 {
            font-family: 'Playfair Display', serif;
            color: var(--navy-light);
            margin: 28px 0 12px;
        }
        .section-card h3 { font-size: 1.35rem; font-weight: 700; }
        .section-card h4 { font-size: 1.15rem; font-weight: 600; }
        
        .section-card p, .section-card ul, .section-card ol {
            font-size: 1.05rem;
            line-height: 1.8;
            color: var(--text-mid);
            margin-bottom: 16px;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        table th, table td {
            border: 1px solid var(--border);
            padding: 10px;
            text-align: left;
        }
        table th { background: var(--navy-light); color: white; }
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

        <div class="nav-group-label">Theory Sections</div>
        <ul class="nav-list">
            <li class="nav-item"><a class="nav-link active" href="#" onclick="showTopic('introduction');return false;"><span class="nav-num">1.1</span> Introduction</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('historical-development');return false;"><span class="nav-num">1.2</span> Historical Development</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('what-is-statistics');return false;"><span class="nav-num">1.3</span> What is Statistics?</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('scope-of-statistics');return false;"><span class="nav-num">1.4</span> Scope of Statistics</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('advantages-of-statistics');return false;"><span class="nav-num">1.5</span> Advantages of Statistics</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('limitations-of-statistics');return false;"><span class="nav-num">1.6</span> Limitations of Statistics</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('areas-of-application');return false;"><span class="nav-num">1.7</span> Areas of Application</a></li>
            <li class="nav-item"><a class="nav-link" href="#" onclick="showTopic('conclusion');return false;"><span class="nav-num">1.8</span> Conclusion</a></li>
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
                <i class="fas fa-language"></i> <span id="lang-toggle-text">Switch Language (Hinglish)</span>
            </button>
            <h1>Unit I: Introduction & Data Collection</h1>
            <div class="author">By Prof. O.P. Sheoran</div>
            <div class="syllabus-tag">
                <strong>Syllabus:</strong> Origin, development, definition, scope, uses, limitations. Types of Data. Collection and Scrutiny of Data.
            </div>
        </div>

        <!-- VERBATIM THEORY SECTIONS INJECTED HERE -->
        {VERBATIM_PLACEHOLDER}

        <!-- EXERCISES INJECTED HERE -->
        {EXERCISES_PLACEHOLDER}

    </main>

    <script>
        // Ensure only the first topic section is active on load
        document.addEventListener('DOMContentLoaded', () => {
            const sections = document.querySelectorAll('.topic-section');
            sections.forEach((sec, index) => {
                if (index === 0) {
                    sec.classList.add('active');
                } else {
                    sec.classList.remove('active');
                }
            });
        });

        let isHinglish = false;
        function toggleLanguage() {
            isHinglish = !isHinglish;
            const btnText = document.getElementById('lang-toggle-text');
            const engContents = document.querySelectorAll('.english-content');
            const hinContents = document.querySelectorAll('.hinglish-content');

            if (isHinglish) {
                btnText.textContent = 'Switch Language (English)';
                engContents.forEach(el => el.style.display = 'none');
                hinContents.forEach(el => el.style.display = 'block');
            } else {
                btnText.textContent = 'Switch Language (Hinglish)';
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

print("Reading translated theory...")
with open('extracted_theory_translated.html', 'r', encoding='utf-8') as f:
    theory_html = f.read()

print("Generating translated exercises...")
exercises_html = generate_mcqs() + generate_fib() + generate_tf() + generate_subj()

print("Replacing placeholders...")
final_html = html_template.replace('{VERBATIM_PLACEHOLDER}', theory_html).replace('{EXERCISES_PLACEHOLDER}', exercises_html)

print("Writing final file...")
with open('Stat-101/Unit-I.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Stat-101/Unit-I.html fully updated with translated exercises and translated verbatim theory!")
