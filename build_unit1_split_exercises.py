import os

# --- EXERCISE GENERATORS ---
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
    html = '''
        <div id="mcq" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">❓</span> Multiple Choice Questions (MCQs)</h2>
                    <p>Select the correct answer from the given options.</p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">❓</span> Multiple Choice Questions (बहुविकल्पीय प्रश्न)</h2>
                    <p>दिए गए विकल्पों में से सही उत्तर चुनें।</p>
                </div>
                <ul class="question-list">
    '''
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
    html += '</ul></section></div>'
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
                    <h2><span class="section-num">✏️</span> Fill in the Blanks</h2>
                    <p>Complete the following sentences with the correct word.</p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">✏️</span> Fill in the Blanks (रिक्त स्थान भरें)</h2>
                    <p>निम्नलिखित वाक्यों को सही शब्द से पूरा करें।</p>
                </div>
                <ul class="question-list">
    '''
    for i, (q, ans) in enumerate(q_data, 1):
        html += f'''
        <li>
            <div class="question"><strong>Q{i}.</strong> {q}</div>
            <button class="get-solution-btn" data-question-id="fib-{i}">Get Solution</button>
            <div class="solution" id="solution-fib-{i}"><strong>Answer:</strong> {ans}</div>
        </li>'''
    html += '</ul></section></div>'
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
                    <h2><span class="section-num">✅</span> True / False</h2>
                    <p>Determine whether the following statements are True or False.</p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">✅</span> True / False (सही/गलत)</h2>
                    <p>निर्धारित करें कि निम्नलिखित कथन सही हैं या गलत।</p>
                </div>
                <ul class="question-list">
    '''
    for i, (q, ans) in enumerate(q_data, 1):
        html += f'''
        <li>
            <div class="question"><strong>Q{i}.</strong> {q}</div>
            <button class="get-solution-btn" data-question-id="tf-{i}">Get Solution</button>
            <div class="solution" id="solution-tf-{i}"><strong>Answer:</strong> {"True" if ans else "False"}</div>
        </li>'''
    html += '</ul></section></div>'
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
                    <h2><span class="section-num">📝</span> Subjective Questions</h2>
                    <p>Answer the following questions in detail. Think about the concepts and real-life examples.</p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">📝</span> Subjective Questions (विषयपरक प्रश्न)</h2>
                    <p>निम्नलिखित प्रश्नों के उत्तर विस्तार से दें। Concepts और वास्तविक जीवन (real-life) के उदाहरणों के बारे में सोचें।</p>
                </div>
                <ul class="question-list">
    '''
    for i, (q, ans) in enumerate(q_data, 1):
        html += f'''
        <li>
            <div class="question"><strong>Q{i}.</strong> {q}</div>
            <button class="get-solution-btn" data-question-id="subj-{i}">Get Solution</button>
            <div class="solution" id="solution-subj-{i}"><p>{ans}</p></div>
        </li>'''
    html += '</ul></section></div>'
    return html

# --- MAIN HTML TEMPLATE ---
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
                    <p>Hello students! Welcome to the BSc First Year <strong>Statistics</strong> course. Statistics is very important in today's world. Every day, phones, computers, and sensors create huge amounts of <strong>data</strong>. Because we have so much data, we need people who know statistics to make sense of it.</p>
                    <p>In this course, you will learn what statistics is. You will learn its uses, its benefits, and its limits. We will use simple examples from daily life and from Haryana to make it easy. This will show you how statistics helps build our nation.</p>

                    <h3>1.1.1 Historical Development</h3>
                    <p>Statistics started a very long time ago. Old governments collected data about their people, taxes, and army. This helped them run their empires well. In India, a book called Kautilya's Arthashastra (around 300 BCE) shows that kings kept records of farming and trade.</p>
                    <p>In the 17th and 18th centuries, people in Europe started studying birth and death records. By the 19th century, scientists developed the 'Probability Theory'. This made statistics a true science. In the 20th century, great scientists like R.A. Fisher and Karl Pearson created modern statistical tools. Today, with fast computers, statistics is used everywhere.</p>

                    <h4>1.1.1.1 Development of Statistics in India</h4>
                    <p>India has a rich history in statistics. After India got independence, the field of statistics grew very fast. Professor P.C. Mahalanobis (1893-1972) is called the father of Indian statistics. In 1931, he founded the famous Indian Statistical Institute (ISI) in Kolkata. He helped make India's Second Five-Year Plan.</p>
                    <p>In 1950, the government started the National Sample Survey Office (NSSO). The NSSO collects important data for the whole country. In Haryana, the State Statistics Department collects data on farming, health, and schools. The government uses this data to make good plans for the people.</p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">1.1</span> Introduction (परिचय)</h2>
                    <p>Hello students! BSc First Year <strong>Statistics</strong> course में आपका स्वागत है। आज के समय में Statistics बहुत महत्वपूर्ण है। हर दिन, फ़ोन और कंप्यूटर बहुत सारा <strong>data</strong> बनाते हैं। चूँकि हमारे पास बहुत सारा data है, हमें ऐसे लोगों की आवश्यकता है जो statistics को समझते हों।</p>
                    <p>इस course में, आप सीखेंगे कि statistics क्या है। आप इसके उपयोग, लाभ और सीमाएं (limits) सीखेंगे। हम इसे आसान बनाने के लिए daily life और हरियाणा के simple examples का उपयोग करेंगे। इससे पता चलेगा कि statistics हमारे देश को बनाने में कैसे मदद करता है।</p>

                    <h3>1.1.1 Historical Development (ऐतिहासिक विकास)</h3>
                    <p>Statistics की शुरुआत बहुत पहले हुई थी। पुरानी सरकारें (Old governments) अपने लोगों, taxes और सेना के बारे में data एकत्र करती थीं। इससे उन्हें अपने राज्यों को अच्छी तरह से चलाने में मदद मिलती थी। भारत में, कौटिल्य के अर्थशास्त्र (लगभग 300 BCE) से पता चलता है कि राजा खेती और व्यापार का record रखते थे।</p>
                    <p>17वीं और 18वीं शताब्दी में, यूरोप में लोगों ने जन्म और मृत्यु के रिकॉर्ड का अध्ययन करना शुरू किया। 19वीं शताब्दी तक, वैज्ञानिकों ने 'Probability Theory' विकसित की। इससे statistics एक वास्तविक विज्ञान बन गया। 20वीं सदी में, R.A. Fisher और Karl Pearson जैसे महान वैज्ञानिकों ने modern statistical tools बनाए। आज तेज़ कंप्यूटरों के साथ, statistics का उपयोग हर जगह किया जाता है।</p>

                    <h4>1.1.1.1 Development of Statistics in India (भारत में सांख्यिकी का विकास)</h4>
                    <p>भारत में statistics का एक समृद्ध इतिहास है। भारत को स्वतंत्रता मिलने के बाद, statistics का क्षेत्र बहुत तेज़ी से बढ़ा। Professor P.C. Mahalanobis (1893-1972) को भारतीय सांख्यिकी का जनक (father of Indian statistics) कहा जाता है। 1931 में, उन्होंने कोलकाता में प्रसिद्ध Indian Statistical Institute (ISI) की स्थापना की। उन्होंने भारत की द्वितीय पंचवर्षीय योजना (Second Five-Year Plan) बनाने में मदद की।</p>
                    <p>1950 में, सरकार ने National Sample Survey Office (NSSO) शुरू किया। NSSO पूरे देश के लिए महत्वपूर्ण data एकत्र करता है। हरियाणा में, State Statistics Department खेती, स्वास्थ्य और स्कूलों पर data एकत्र करता है। सरकार इस data का उपयोग लोगों के लिए अच्छी योजनाएं बनाने के लिए करती है।</p>
                </div>
            </section>
        </div>

        <!-- SECTION 1.2: WHAT IS STATISTICS -->
        <div id="sec1-2" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">1.2</span> What is Statistics?</h2>
                    <p>Statistics is a science. It deals with collecting, sorting, looking at, and showing data. The word "Statistics" comes from the Latin word "status" which means "related to the state."</p>
                    <div class="definition">
                        <h4>Simple Definition of Statistics</h4>
                        <p>Statistics is the science of collecting, organizing, analyzing, and presenting data. It helps us make good decisions even when we are not 100% sure about the future.</p>
                    </div>
                    <p>Today, we look at statistics in two simple ways:</p>
                    <ul>
                        <li><strong>Numerical facts:</strong> This just means a collection of numbers. For example, the marks of all students in a class or the runs scored by a cricketer.</li>
                        <li><strong>Analytical method:</strong> This means the tools and maths we use to study those numbers and find meaning in them.</li>
                    </ul>

                    <h3>1.2.1 Types of Statistics</h3>
                    <p>We can divide statistics into two main parts:</p>
                    
                    <h4>A. Descriptive Statistics:</h4>
                    <p>This part helps us summarize the data. It gives us a quick picture of what the data looks like. It includes:</p>
                    <ul>
                        <li><strong>Central Tendency:</strong> Finding the middle point (Mean, Median, Mode).</li>
                        <li><strong>Dispersion:</strong> Finding how spread out the numbers are (Range, Variance).</li>
                        <li><strong>Graphs:</strong> Showing data in pictures like Bar Charts and Pie Charts.</li>
                    </ul>

                    <h4>B. Inferential Statistics:</h4>
                    <p>This part helps us make guesses about a large group based on a small sample. It helps us make decisions. It includes:</p>
                    <ul>
                        <li><strong>Hypothesis Testing:</strong> Testing if a claim is true (like a t-test).</li>
                        <li><strong>Estimation:</strong> Guessing the real average from sample data.</li>
                    </ul>

                    <div class="example">
                        <h4>Example: Crop Production in Haryana</h4>
                        <p>The Haryana Agriculture Department wants to know the total wheat production. They cannot visit every single farm. So, they visit only 500 farms (a sample).</p>
                        <p><strong>Descriptive:</strong> They find the average yield of these 500 farms is 5.2 tons per hectare.</p>
                        <p><strong>Inferential:</strong> Using maths, they make a smart guess. They say the whole state of Haryana will have an average yield between 5.1 and 5.3 tons per hectare.</p>
                    </div>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">1.2</span> What is Statistics? (सांख्यिकी क्या है?)</h2>
                    <p>Statistics एक विज्ञान है। यह data को एकत्र करने, छांटने (sorting), देखने और दिखाने से संबंधित है। "Statistics" शब्द लैटिन शब्द "status" से आया है जिसका अर्थ है "राज्य से संबंधित"।</p>
                    <div class="definition">
                        <h4>Simple Definition of Statistics (सरल परिभाषा)</h4>
                        <p>Statistics data को collect, organize, analyze, और present करने का विज्ञान है। यह हमें सही निर्णय लेने में मदद करता है, तब भी जब हम भविष्य के बारे में 100% सुनिश्चित (sure) नहीं होते हैं।</p>
                    </div>
                    <p>आज, हम statistics को दो सरल तरीकों से देखते हैं:</p>
                    <ul>
                        <li><strong>Numerical facts (संख्यात्मक तथ्य):</strong> इसका मतलब सिर्फ संख्याओं का एक collection है। उदाहरण के लिए, कक्षा में सभी छात्रों के अंक या क्रिकेटर द्वारा बनाए गए रन।</li>
                        <li><strong>Analytical method (विश्लेषणात्मक विधि):</strong> इसका मतलब उन tools और maths से है जिनका उपयोग हम उन संख्याओं का अध्ययन करने और उनमें अर्थ खोजने के लिए करते हैं।</li>
                    </ul>

                    <h3>1.2.1 Types of Statistics (सांख्यिकी के प्रकार)</h3>
                    <p>हम statistics को दो मुख्य भागों में बाँट सकते हैं:</p>
                    
                    <h4>A. Descriptive Statistics (वर्णनात्मक सांख्यिकी):</h4>
                    <p>यह हिस्सा हमें data को summarize (संक्षेप) करने में मदद करता है। यह हमें एक त्वरित तस्वीर (quick picture) देता है कि data कैसा दिखता है। इसमें शामिल हैं:</p>
                    <ul>
                        <li><strong>Central Tendency:</strong> मध्य बिंदु खोजना (Mean, Median, Mode)।</li>
                        <li><strong>Dispersion:</strong> यह खोजना कि संख्याएं कितनी फैली हुई हैं (Range, Variance)।</li>
                        <li><strong>Graphs:</strong> Bar Charts और Pie Charts जैसे चित्रों में data दिखाना।</li>
                    </ul>

                    <h4>B. Inferential Statistics (अनुमानात्मक सांख्यिकी):</h4>
                    <p>यह हिस्सा एक छोटे sample के आधार पर एक बड़े समूह (population) के बारे में अनुमान लगाने में हमारी मदद करता है। यह हमें निर्णय लेने में मदद करता है। इसमें शामिल हैं:</p>
                    <ul>
                        <li><strong>Hypothesis Testing:</strong> यह test करना कि कोई दावा सच है या नहीं।</li>
                        <li><strong>Estimation:</strong> Sample data से वास्तविक औसत (real average) का अनुमान लगाना।</li>
                    </ul>

                    <div class="example">
                        <h4>Example: Crop Production in Haryana (हरियाणा में फसल उत्पादन)</h4>
                        <p>हरियाणा कृषि विभाग कुल गेहूं उत्पादन जानना चाहता है। वे हर एक खेत का दौरा नहीं कर सकते। इसलिए, वे केवल 500 खेतों (एक sample) का दौरा करते हैं।</p>
                        <p><strong>Descriptive:</strong> वे पाते हैं कि इन 500 खेतों की औसत उपज 5.2 टन प्रति हेक्टेयर है।</p>
                        <p><strong>Inferential:</strong> Maths का उपयोग करके, वे एक smart guess लगाते हैं। वे कहते हैं कि पूरे हरियाणा राज्य में औसत उपज 5.1 और 5.3 टन प्रति हेक्टेयर के बीच होगी।</p>
                    </div>
                </div>
            </section>
        </div>

        <!-- SECTION 1.3: SCOPE OF STATISTICS -->
        <div id="sec1-3" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">1.3</span> Scope of Statistics</h2>
                    <p>Statistics is used in almost every area of life. It is used in science, business, hospitals, and government. The main steps of statistical work are:</p>

                    <h3>1.3.1 Data Collection</h3>
                    <p>The first step is to get the data. We use sampling methods so we don't have to check everyone.</p>
                    <ul>
                        <li><strong>Random Sampling:</strong> Picking people by pure chance (like a lottery).</li>
                        <li><strong>Stratified Sampling:</strong> Dividing people into groups first (like boys and girls), and then picking randomly from each group.</li>
                    </ul>
                    <p>We can collect data by asking people questions on a paper (Questionnaires) or talking to them directly (Interviews).</p>

                    <h3>1.3.2 Data Organization</h3>
                    <p>Raw data is messy. We have to sort it and arrange it in tables so we can read it easily.</p>
                    <ul>
                        <li><strong>Qualitative Classification:</strong> Sorting by qualities like gender or religion.</li>
                        <li><strong>Quantitative Classification:</strong> Sorting by numbers like age or income.</li>
                        <li><strong>Temporal Classification:</strong> Sorting by time (like months or years).</li>
                    </ul>
                    <p>We also draw pictures like Pie Charts and Bar Charts to make the numbers look clear.</p>

                    <h3>1.3.3 Data Analysis</h3>
                    <p>After sorting, we analyze the numbers. We find the average (Mean) to see the center. We find the standard deviation to see how much the numbers vary.</p>

                    <h3>1.3.4 Inference and Decision Making</h3>
                    <p>The final step is to make a decision. Even if our data is only a sample, statistics helps us guess the truth with high confidence.</p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">1.3</span> Scope of Statistics (सांख्यिकी का कार्यक्षेत्र)</h2>
                    <p>Statistics का उपयोग जीवन के लगभग हर क्षेत्र में किया जाता है। इसका उपयोग विज्ञान, व्यवसाय, अस्पतालों और सरकार में किया जाता है। Statistical कार्य के मुख्य steps हैं:</p>

                    <h3>1.3.1 Data Collection (डेटा संग्रह)</h3>
                    <p>पहला कदम data प्राप्त करना है। हम sampling methods का उपयोग करते हैं ताकि हमें हर किसी की जांच न करनी पड़े।</p>
                    <ul>
                        <li><strong>Random Sampling (यादृच्छिक प्रतिचयन):</strong> लोगों को पूरी तरह से संयोग (chance) से चुनना (जैसे लॉटरी)।</li>
                        <li><strong>Stratified Sampling:</strong> पहले लोगों को समूहों में विभाजित करना (जैसे लड़के और लड़कियां), और फिर प्रत्येक समूह से randomly चुनना।</li>
                    </ul>
                    <p>हम लोगों से एक paper (Questionnaires) पर प्रश्न पूछकर या उनसे सीधे बात करके (Interviews) data collect कर सकते हैं।</p>

                    <h3>1.3.2 Data Organization (डेटा संगठन)</h3>
                    <p>Raw data बहुत बिखरा हुआ (messy) होता है। हमें इसे छांटना (sort) होगा और tables में व्यवस्थित करना होगा ताकि हम इसे आसानी से पढ़ सकें।</p>
                    <ul>
                        <li><strong>Qualitative Classification:</strong> लिंग (gender) या धर्म जैसे गुणों के आधार पर छांटना।</li>
                        <li><strong>Quantitative Classification:</strong> उम्र या आय जैसे नंबरों के आधार पर छांटना।</li>
                        <li><strong>Temporal Classification:</strong> समय (जैसे महीनों या वर्षों) के अनुसार छांटना।</li>
                    </ul>
                    <p>हम संख्याओं को स्पष्ट (clear) दिखाने के लिए Pie Charts और Bar Charts जैसे चित्र भी बनाते हैं।</p>

                    <h3>1.3.3 Data Analysis (डेटा विश्लेषण)</h3>
                    <p>Sorting के बाद, हम संख्याओं का analysis करते हैं। हम केंद्र देखने के लिए औसत (Mean) निकालते हैं। हम देखते हैं कि संख्याएं कितनी बदलती हैं (standard deviation)।</p>

                    <h3>1.3.4 Inference and Decision Making (अनुमान और निर्णय लेना)</h3>
                    <p>अंतिम कदम निर्णय लेना है। भले ही हमारा data केवल एक sample है, statistics हमें उच्च विश्वास (high confidence) के साथ सच्चाई का अनुमान लगाने में मदद करता है।</p>
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
                        <li><strong>Turns words into numbers:</strong> It helps us turn vague ideas like "many people are happy" into solid numbers like "85% of people are happy".</li>
                        <li><strong>Helps in clear thinking:</strong> We don't have to guess. We can look at the data and make a logical decision based on facts.</li>
                        <li><strong>Finds hidden patterns:</strong> When we have a lot of numbers, we can't see the trend. Statistics draws a graph and shows us if sales are going up or down.</li>
                        <li><strong>Predicts the future:</strong> By looking at past data (like rain over the last 10 years), statistics helps us predict what might happen next year.</li>
                    </ul>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">1.4</span> Advantages of Statistics (सांख्यिकी के लाभ)</h2>
                    <p>हम statistics क्यों सीखते हैं? यहाँ कुछ सरल लाभ (benefits) दिए गए हैं:</p>
                    <ul>
                        <li><strong>शब्दों को संख्याओं में बदलता है:</strong> यह हमें "कई लोग खुश हैं" जैसे अस्पष्ट विचारों (vague ideas) को "85% लोग खुश हैं" जैसे ठोस संख्याओं में बदलने में मदद करता है।</li>
                        <li><strong>स्पष्ट सोच में मदद करता है:</strong> हमें अनुमान नहीं लगाना पड़ता है। हम data को देख सकते हैं और तथ्यों (facts) के आधार पर logical decision ले सकते हैं।</li>
                        <li><strong>छिपे हुए patterns ढूंढता है:</strong> जब हमारे पास बहुत सारे number होते हैं, तो हम trend नहीं देख सकते। Statistics एक ग्राफ बनाता है और हमें दिखाता है कि sales ऊपर जा रही है या नीचे।</li>
                        <li><strong>भविष्य की भविष्यवाणी करता है:</strong> पिछले data (जैसे पिछले 10 वर्षों में बारिश) को देखकर, statistics हमें यह अनुमान लगाने में मदद करता है कि अगले साल क्या हो सकता है।</li>
                    </ul>
                </div>
            </section>
        </div>

        <!-- SECTION 1.5: LIMITATIONS OF STATISTICS -->
        <div id="sec1-5" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">1.5</span> Limitations of Statistics</h2>
                    <p>Statistics is very useful, but it has some weak points you should remember:</p>
                    <ol>
                        <li><strong>It only likes numbers:</strong> It cannot directly study honesty, beauty, or kindness. We have to give them numbers first (like giving a score out of 10).</li>
                        <li><strong>It ignores the individual:</strong> Statistics only cares about the group. If the average score of a class is 80%, it doesn't tell us about the one student who failed.</li>
                        <li><strong>It is not exactly perfect:</strong> In math, 2 + 2 is always 4. But statistical rules are only true on average. There is always a small chance of error.</li>
                        <li><strong>It can be misused:</strong> If someone uses wrong data or hides half the data, they can trick people using statistics.</li>
                    </ol>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">1.5</span> Limitations of Statistics (सांख्यिकी की सीमाएं)</h2>
                    <p>Statistics बहुत उपयोगी है, लेकिन इसके कुछ कमजोर बिंदु (weak points) हैं जिन्हें आपको याद रखना चाहिए:</p>
                    <ol>
                        <li><strong>यह केवल संख्याओं को पसंद करता है:</strong> यह सीधे ईमानदारी (honesty), सुंदरता या दयालुता का अध्ययन नहीं कर सकता। हमें पहले उन्हें नंबर देने होंगे (जैसे 10 में से स्कोर देना)।</li>
                        <li><strong>यह व्यक्ति (individual) को ignore करता है:</strong> Statistics केवल समूह की परवाह करता है। यदि किसी कक्षा का औसत (average) स्कोर 80% है, तो यह हमें उस एक छात्र के बारे में नहीं बताता जो fail हो गया।</li>
                        <li><strong>यह पूरी तरह से perfect नहीं है:</strong> गणित में, 2 + 2 हमेशा 4 होता है। लेकिन statistical नियम केवल औसतन सत्य होते हैं। इसमें हमेशा error की थोड़ी गुंजाइश होती है।</li>
                        <li><strong>इसका दुरुपयोग (misuse) किया जा सकता है:</strong> यदि कोई गलत data का उपयोग करता है या आधा data छुपाता है, तो वे statistics का उपयोग करके लोगों को मूर्ख (trick) बना सकते हैं।</li>
                    </ol>
                </div>
            </section>
        </div>

        <!-- SECTION 1.6: AREAS OF APPLICATION -->
        <div id="sec1-6" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">1.6</span> Areas of Application</h2>
                    <p>Today, statistics is used everywhere. It helps people in almost every job make better choices. Here are some clear examples of how statistics is applied in real life:</p>
                    
                    <div class="highlight-box">
                        <p><strong>1.6.1 In Science and Research (Agriculture)</strong></p>
                        <p>Farmers and scientists use statistics to grow better crops. <br>
                        <em>Example:</em> A researcher wants to know which fertilizer is better. They use Fertilizer A on one field and Fertilizer B on another field. They collect the crop yield data and use a statistical test (like a t-test) to see which fertilizer really gave a better yield, not just by random chance.</p>
                    </div>

                    <div class="highlight-box">
                        <p><strong>1.6.2 In Healthcare and Medicine (Social Sciences)</strong></p>
                        <p>Doctors rely on statistics to know if a medicine is safe and works well. <br>
                        <em>Example:</em> Before launching a new vaccine for a virus, doctors give it to 10,000 volunteers and a dummy medicine (placebo) to another 10,000. They compare the number of people who got sick in both groups. Statistics proves if the vaccine is effective.</p>
                    </div>

                    <div class="highlight-box">
                        <p><strong>1.6.3 In Business and Finance</strong></p>
                        <p>Companies use data to understand what customers want to buy. <br>
                        <em>Example:</em> A mobile phone company looks at the sales data of the last 5 years. By using "time series analysis," they can predict that they will sell more phones during the Diwali festival. So, they make sure to produce enough phones before Diwali starts.</p>
                    </div>

                    <div class="highlight-box">
                        <p><strong>1.6.4 In Government and Policy</strong></p>
                        <p>The government needs statistics to build the country and help the poor. <br>
                        <em>Example:</em> The government conducts a Census (counting people). If the data shows that a specific district has a very high number of young children, the government will use this statistical data to build more schools and parks in that district.</p>
                    </div>

                    <div class="highlight-box">
                        <p><strong>1.6.5 In Technology and Computing</strong></p>
                        <p>Tech companies use statistics to build Artificial Intelligence and Machine Learning models. <br>
                        <em>Example:</em> AI systems use probability to recognize your face on a phone or to suggest which video you should watch next on YouTube based on your past choices.</p>
                    </div>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">1.6</span> Areas of Application (अनुप्रयोग के क्षेत्र)</h2>
                    <p>आज, statistics का हर जगह उपयोग किया जाता है। यह लगभग हर काम में लोगों को बेहतर विकल्प (better choices) चुनने में मदद करता है। वास्तविक जीवन में statistics कैसे लागू होता है, इसके कुछ स्पष्ट उदाहरण (clear examples) यहां दिए गए हैं:</p>
                    
                    <div class="highlight-box">
                        <p><strong>1.6.1 In Science and Research (विज्ञान और कृषि में)</strong></p>
                        <p>किसान और वैज्ञानिक बेहतर फसल उगाने के लिए statistics का उपयोग करते हैं। <br>
                        <em>उदाहरण:</em> एक शोधकर्ता जानना चाहता है कि कौन सा उर्वरक (fertilizer) बेहतर है। वे एक खेत में Fertilizer A और दूसरे खेत में Fertilizer B का उपयोग करते हैं। वे फसल की उपज का data collect करते हैं और यह देखने के लिए एक statistical test (जैसे t-test) का उपयोग करते हैं कि वास्तव में किस उर्वरक ने बेहतर उपज दी है।</p>
                    </div>

                    <div class="highlight-box">
                        <p><strong>1.6.2 In Healthcare and Medicine (स्वास्थ्य सेवा और चिकित्सा में)</strong></p>
                        <p>डॉक्टर यह जानने के लिए statistics पर निर्भर करते हैं कि कोई दवा सुरक्षित है या नहीं। <br>
                        <em>उदाहरण:</em> किसी वायरस के लिए नया टीका (vaccine) launch करने से पहले, डॉक्टर इसे 10,000 स्वयंसेवकों (volunteers) को देते हैं और अन्य 10,000 को एक डमी दवा देते हैं। वे तुलना करते हैं कि दोनों समूहों में कितने लोग बीमार पड़े। Statistics साबित करता है कि टीका प्रभावी (effective) है या नहीं।</p>
                    </div>

                    <div class="highlight-box">
                        <p><strong>1.6.3 In Business and Finance (व्यापार और वित्त में)</strong></p>
                        <p>कंपनियां यह समझने के लिए data का उपयोग करती हैं कि ग्राहक क्या खरीदना चाहते हैं। <br>
                        <em>उदाहरण:</em> एक मोबाइल फोन कंपनी पिछले 5 वर्षों के बिक्री (sales) data को देखती है। "time series analysis" का उपयोग करके, वे भविष्यवाणी (predict) कर सकते हैं कि वे दिवाली के त्योहार के दौरान अधिक फोन बेचेंगे। इसलिए, वे दिवाली शुरू होने से पहले पर्याप्त फोन का production करना सुनिश्चित करते हैं।</p>
                    </div>

                    <div class="highlight-box">
                        <p><strong>1.6.4 In Government and Policy (सरकारी योजना में)</strong></p>
                        <p>देश के निर्माण और गरीबों की मदद के लिए सरकार को statistics की आवश्यकता होती है। <br>
                        <em>उदाहरण:</em> सरकार जनगणना (Census) करती है। यदि data से पता चलता है कि एक विशिष्ट जिले में छोटे बच्चों की संख्या बहुत अधिक है, तो सरकार उस जिले में अधिक स्कूल और पार्क बनाने के लिए इस statistical data का उपयोग करेगी।</p>
                    </div>

                    <div class="highlight-box">
                        <p><strong>1.6.5 In Technology and Computing (प्रौद्योगिकी और कंप्यूटिंग)</strong></p>
                        <p>Tech कंपनियां आर्टिफिशियल इंटेलिजेंस (AI) और मशीन लर्निंग मॉडल बनाने के लिए statistics का उपयोग करती हैं। <br>
                        <em>उदाहरण:</em> AI सिस्टम probability का उपयोग करके फोन पर आपका चेहरा पहचानते हैं या आपकी पिछली पसंद के आधार पर सुझाव देते हैं कि आपको YouTube पर कौन सा वीडियो देखना चाहिए।</p>
                    </div>
                </div>
            </section>
        </div>

        <!-- SECTION 1.7: CONCLUSION -->
        <div id="sec1-7" class="topic-section">
            <section class="section-card">
                <div class="english-content">
                    <h2><span class="section-num">1.7</span> Conclusion</h2>
                    <p>In this chapter, we have studied various aspects of statistics. We have seen that statistics is a broad subject that deals with the collection, organization, analysis, interpretation, and presentation of data.</p>
                    <p>We learned about the two main types of statistics: descriptive statistics (which summarizes data) and inferential statistics (which helps us draw conclusions about the population from a small sample).</p>
                    <p>Statistics has many advantages, such as turning vague information into clear numbers, and helping us make evidence-based decisions. However, it also has limitations, as it only deals with numbers and ignores individual facts. Still, statistics gives us the power to tell stories through numbers and to understand complex realities. It is truly a guiding lighthouse in the sea of uncertainty.</p>
                </div>
                <div class="hinglish-content" style="display:none;">
                    <h2><span class="section-num">1.7</span> Conclusion (निष्कर्ष)</h2>
                    <p>इस अध्याय में, हमने statistics के विभिन्न पहलुओं (aspects) का अध्ययन किया है। हमने देखा है कि statistics एक व्यापक विषय है जो data के collection, organization, analysis, interpretation और presentation से संबंधित है।</p>
                    <p>हमने statistics के दो मुख्य प्रकारों के बारे में सीखा: descriptive statistics (जो data को summarize करती है) और inferential statistics (जो हमें एक छोटे sample से जनसंख्या के बारे में निष्कर्ष निकालने में मदद करती है)।</p>
                    <p>Statistics के कई फायदे हैं, जैसे अस्पष्ट जानकारी (vague info) को स्पष्ट संख्याओं में बदलना, और साक्ष्य-आधारित (evidence-based) निर्णय लेने में हमारी मदद करना। हालाँकि, इसकी सीमाएँ भी हैं, क्योंकि यह केवल संख्याओं से संबंधित है और individual facts को अनदेखा करता है। फिर भी, statistics हमें संख्याओं के माध्यम से कहानियाँ बताने और जटिल वास्तविकताओं (complex realities) को समझने की शक्ति देता है। यह अनिश्चितता के समुद्र में वास्तव में एक मार्गदर्शक प्रकाशस्तंभ (guiding lighthouse) है।</p>
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
    </script>
    <script src="../whiteboard/whiteboard.js?v=2.0"></script>
</body>
</html>
"""

exercises_html = generate_mcqs() + generate_fib() + generate_tf() + generate_subj()
final_html = html_template.replace('{EXERCISES_PLACEHOLDER}', exercises_html)

with open('Stat-101/Unit-I.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Stat-101/Unit-I.html generated successfully with split exercises.")
