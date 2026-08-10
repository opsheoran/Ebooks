import os

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
    html = '<div class="exercise-section"><div class="exercise-header"><h3>Multiple Choice Questions (MCQs)</h3></div><ul class="question-list">'
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
    html += '</ul></div>'
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
    html = '<div class="exercise-section"><div class="exercise-header"><h3>Fill in the Blanks</h3></div><ul class="question-list">'
    for i, (q, ans) in enumerate(q_data, 1):
        html += f'''
        <li>
            <div class="question"><strong>Q{i}.</strong> {q}</div>
            <button class="get-solution-btn" data-question-id="fib-{i}">Get Solution</button>
            <div class="solution" id="solution-fib-{i}"><strong>Answer:</strong> {ans}</div>
        </li>'''
    html += '</ul></div>'
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
    html = '<div class="exercise-section"><div class="exercise-header"><h3>True or False</h3></div><ul class="question-list">'
    for i, (q, ans) in enumerate(q_data, 1):
        html += f'''
        <li>
            <div class="question"><strong>Q{i}.</strong> {q}</div>
            <button class="get-solution-btn" data-question-id="tf-{i}">Get Solution</button>
            <div class="solution" id="solution-tf-{i}"><strong>Answer:</strong> {"True" if ans else "False"}</div>
        </li>'''
    html += '</ul></div>'
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
    html = '<div class="exercise-section"><div class="exercise-header"><h3>Subjective Questions</h3></div><ul class="question-list">'
    for i, (q, ans) in enumerate(q_data, 1):
        html += f'''
        <li>
            <div class="question"><strong>Q{i}.</strong> {q}</div>
            <button class="get-solution-btn" data-question-id="subj-{i}">Get Solution</button>
            <div class="solution" id="solution-subj-{i}"><p>{ans}</p></div>
        </li>'''
    html += '</ul></div>'
    return html

# Read parts
with open('Stat-101/unit1_part1.html', 'r', encoding='utf-8') as f: p1 = f.read()
with open('Stat-101/unit1_part2.html', 'r', encoding='utf-8') as f: p2 = f.read()
with open('Stat-101/unit1_part3.html', 'r', encoding='utf-8') as f: p3 = f.read()
with open('Stat-101/unit1_part4.html', 'r', encoding='utf-8') as f: p4 = f.read()

# Generate exercises
exercises_html = generate_mcqs() + generate_fib() + generate_tf() + generate_subj()

# Replace placeholder in part 4
p4 = p4.replace('{EXERCISES_PLACEHOLDER}', exercises_html)

# Combine all parts
final_html = p1 + p2 + p3 + p4

# Write final output
with open('Stat-101/Unit-I.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Stat-101/Unit-I.html generated successfully.")

# Clean up parts
os.remove('Stat-101/unit1_part1.html')
os.remove('Stat-101/unit1_part2.html')
os.remove('Stat-101/unit1_part3.html')
os.remove('Stat-101/unit1_part4.html')
