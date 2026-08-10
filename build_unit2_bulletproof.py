import os
import urllib.request, urllib.parse, json, re, time
from bs4 import BeautifulSoup, NavigableString

hinglish_dict = {
    'सांख्यिकीय': 'statistical',
    'सांख्यिकी': 'Statistics',
    'डेटा': 'data',
    'आंकड़ों': 'data',
    'आंकड़े': 'data',
    'प्रतिदर्श': 'sample',
    'नमूने': 'samples',
    'नमूना': 'sample',
    'जनसंख्या': 'population',
    'आबादी': 'population',
    'चरों': 'variables',
    'चर': 'variable',
    'गुणात्मक': 'qualitative',
    'मात्रात्मक': 'quantitative',
    'औसत': 'average',
    'माध्यिका': 'median',
    'माध्य': 'mean',
    'बहुलक': 'mode',
    'मानक विचलन': 'standard deviation',
    'प्रसरण': 'variance',
    'प्रायिकता': 'probability',
    'वितरण': 'distribution',
    'परिकल्पना परीक्षण': 'hypothesis testing',
    'परिकल्पना': 'hypothesis',
    'परीक्षण': 'testing',
    'प्रतिगमन': 'regression',
    'सहसंबंध': 'correlation',
    'वर्गीकरण': 'classification',
    'सारणीकरण': 'tabulation',
    'अवलोकन': 'observation',
    'प्रश्नावली': 'questionnaire',
    'साक्षात्कार': 'interview',
    'प्राथमिक': 'primary',
    'द्वितीयक': 'secondary',
    'विश्लेषणात्मक': 'analytical',
    'विश्लेषण': 'analysis',
    'वर्णनात्मक': 'descriptive',
    'अनुमानात्मक': 'inferential',
    'अनुमान': 'estimation',
    'प्रतिचयन': 'sampling',
    'स्तरीकृत': 'stratified',
    'यादृच्छिक': 'random',
    'गुच्छ': 'cluster',
    'व्यवस्थित': 'systematic',
    'सर्वेक्षणों': 'surveys',
    'सर्वेक्षण': 'survey',
    'ग्राफ': 'graph',
    'चार्ट': 'chart',
    'पाई चार्ट': 'pie chart',
    'बार चार्ट': 'bar chart',
    'हिस्टोग्राम': 'histogram',
    'स्कैटर प्लॉट': 'scatter plot',
    'केंद्रीय प्रवृत्ति': 'central tendency',
    'प्रकीर्णन': 'dispersion',
    'विषमता': 'skewness',
    'कुकुदता': 'kurtosis',
    'संकेतन': 'notation',
    'द्विभाजन': 'dichotomy',
    'आवृत्तियां': 'frequencies',
    'आवृत्ति': 'frequency',
    'विशेषताओं': 'attributes',
    'गुण': 'attribute',
    'स्वतंत्रता': 'independence',
    'संगति': 'consistency',
    'गुणांक': 'coefficient',
    'संबंध': 'association',
    'संभाव्यता': 'probability',
    'विज्ञान': 'science',
    'गणितीय': 'mathematical',
    'गणित': 'mathematics',
    'प्रक्रियाओं': 'procedures',
    'प्रक्रिया': 'process',
    'शोधकर्ता': 'researcher',
    'शोध': 'research',
    'त्रुटियों': 'errors',
    'त्रुटि': 'error',
    'सटीकता': 'accuracy',
    'परिणामों': 'results',
    'परिणाम': 'result',
    'निर्णय': 'decision',
    'निष्कर्ष': 'conclusion',
    'तकनीकों': 'techniques',
    'तकनीक': 'technique',
    'विधियां': 'methods',
    'विधि': 'method',
    'सॉफ्टवेयर': 'software',
    'इंटरैक्टिव': 'interactive',
    'डिज़ाइन': 'design',
    'मॉडल': 'model',
    'मापन': 'measurement',
    'मूल्यांकन': 'evaluation',
    'समीक्षा': 'review',
    'अध्याय': 'chapter',
    'तथ्यों': 'facts',
    'तथ्य': 'facts',
    'जानकारी': 'information',
    'समस्याओं': 'problems',
    'समस्या': 'problem',
    'समाधान': 'solution',
    'उदाहरण': 'example',
    'अनुप्रयोग': 'application',
    'मूल्यों': 'values',
    'मूल्य': 'value',
    'स्तर': 'level',
    'उपज': 'yield',
    'क्षेत्र': 'field',
    'प्रभावी': 'effective',
    'प्रतिस्थापन': 'replacement',
    'आकार': 'size',
    'जटिल': 'complex',
    'सैद्धांतिक': 'theoretical',
    'सिद्धांत': 'theory',
    'प्रदान': 'provide'
}

def to_hinglish(text):
    if not text.strip() or not re.search('[a-zA-Z]', text):
        return text
    try:
        q = urllib.parse.quote(text.strip())
        url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=hi&dt=t&q={q}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        translated = "".join([chunk[0] for chunk in data[0] if chunk[0]])
        
        sorted_keys = sorted(hinglish_dict.keys(), key=len, reverse=True)
        for hindi_term in sorted_keys:
            eng_term = hinglish_dict[hindi_term]
            translated = translated.replace(hindi_term, eng_term)
            
        translated = re.sub(r'([a-zA-Z])([।,.?!])', r'\1 \2', translated)
        
        prefix = ' ' if text.startswith(' ') or text.startswith('\n') else ''
        suffix = ' ' if text.endswith(' ') or text.endswith('\n') else ''
        return prefix + translated + suffix
    except Exception as e:
        time.sleep(0.5)
        return text

def translate_html_block(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    for node in soup.find_all(string=True):
        if isinstance(node, NavigableString):
            text = str(node)
            if node.parent.name in ['script', 'style']:
                continue
            if '\\(' in text or '\\[' in text:
                continue
            trans = to_hinglish(text)
            node.replace_with(trans)
    return str(soup)

def t(text):
    return to_hinglish(text)

def generate_unit2_exercises():
    mcq_data = [
        ("The process of arranging data in rows and columns is called:", ["(a) Classification", "(b) Tabulation", "(c) Frequency Distribution", "(d) Graphical Representation"], 1),
        ("Which of the following is a one-dimensional diagram?", ["(a) Bar chart", "(b) Pie chart", "(c) Histogram", "(d) Cylinder"], 0),
        ("A histogram is used to present:", ["(a) Ungrouped data", "(b) Grouped frequency distribution", "(c) Time series data", "(d) Qualitative data"], 1),
        ("The most common measure of central tendency is:", ["(a) Median", "(b) Mode", "(c) Arithmetic Mean", "(d) Geometric Mean"], 2),
        ("Which measure of central tendency is most affected by extreme values?", ["(a) Median", "(b) Mode", "(c) Arithmetic Mean", "(d) Geometric Mean"], 2),
        ("The middle value of an ordered array of numbers is the:", ["(a) Mean", "(b) Median", "(c) Mode", "(d) Harmonic Mean"], 1),
        ("The value that occurs most frequently in a dataset is the:", ["(a) Mean", "(b) Median", "(c) Mode", "(d) Average"], 2),
        ("Geometric Mean is particularly useful for:", ["(a) Finding average speed", "(b) Finding average growth rate", "(c) Finding extreme values", "(d) Categorical data"], 1),
        ("Harmonic Mean is best used for averaging:", ["(a) Heights", "(b) Weights", "(c) Rates and ratios like speed", "(d) Income"], 2),
        ("Which partition value divides the dataset into four equal parts?", ["(a) Median", "(b) Quartiles", "(c) Deciles", "(d) Percentiles"], 1),
        ("The second quartile (Q2) is identical to the:", ["(a) Mean", "(b) Median", "(c) Mode", "(d) First Decile"], 1),
        ("Deciles divide the data into how many equal parts?", ["(a) 4", "(b) 10", "(c) 100", "(d) 2"], 1),
        ("A frequency polygon is constructed by plotting frequencies against:", ["(a) Class boundaries", "(b) Class limits", "(c) Class marks (midpoints)", "(d) Cumulative frequencies"], 2),
        ("An ogive is used to determine the:", ["(a) Mean", "(b) Median", "(c) Mode", "(d) Geometric Mean"], 1),
        ("In a positively skewed distribution, the relationship is:", ["(a) Mean > Median > Mode", "(b) Mean < Median < Mode", "(c) Mean = Median = Mode", "(d) Mode > Mean"], 0),
        ("In a perfectly symmetrical distribution, Mean, Median, and Mode are:", ["(a) Ascending", "(b) Descending", "(c) Equal", "(d) Unrelated"], 2),
        ("The sum of deviations of individual observations from the arithmetic mean is:", ["(a) 1", "(b) Minimum", "(c) Zero", "(d) Maximum"], 2),
        ("For a dataset with values 2, 4, 8, the Geometric Mean is:", ["(a) 4", "(b) 6", "(c) 8", "(d) 14"], 0),
        ("Which average cannot be calculated if any value is zero?", ["(a) Arithmetic Mean", "(b) Median", "(c) Mode", "(d) Geometric Mean"], 3),
        ("Stem-and-leaf display is an alternative to:", ["(a) Bar chart", "(b) Pie chart", "(c) Frequency distribution", "(d) Scatter plot"], 2),
        ("A pie chart is used to represent:", ["(a) Trend over time", "(b) Components of a total", "(c) Frequency distribution", "(d) Cumulative frequencies"], 1),
        ("The empirical relationship between Mean, Median, and Mode is:", ["(a) Mode = 3 Median - 2 Mean", "(b) Mean = 3 Median - 2 Mode", "(c) Median = 3 Mode - 2 Mean", "(d) Mode = 2 Median - 3 Mean"], 0),
        ("Which measure of location is most suitable for qualitative data (e.g., shoe size)?", ["(a) Mean", "(b) Median", "(c) Mode", "(d) Geometric Mean"], 2),
        ("Partition values include:", ["(a) Mean, Median, Mode", "(b) Quartiles, Deciles, Percentiles", "(c) Range, Variance", "(d) Skewness, Kurtosis"], 1),
        ("The 50th percentile (P50) is equal to:", ["(a) First Quartile", "(b) Median", "(c) Third Quartile", "(d) Mode"], 1),
        ("Which chart is drawn using cumulative frequencies?", ["(a) Histogram", "(b) Frequency Polygon", "(c) Ogive", "(d) Bar Chart"], 2),
        ("The lower and upper limits of a class are 10 and 20. The class mark is:", ["(a) 10", "(b) 15", "(c) 20", "(d) 30"], 1),
        ("Data presented in the form of a table is called:", ["(a) Tabulation", "(b) Classification", "(c) Observation", "(d) Interpretation"], 0),
        ("The arithmetic mean of first 5 natural numbers is:", ["(a) 2", "(b) 3", "(c) 4", "(d) 5"], 1),
        ("Which measure provides a robust estimate of central tendency in the presence of outliers?", ["(a) Arithmetic Mean", "(b) Median", "(c) Geometric Mean", "(d) Harmonic Mean"], 1)
    ]
    
    fib_data = [
        ("Arranging data into homogeneous groups based on common characteristics is called ____.", "Classification"),
        ("A systematic presentation of numerical data in rows and columns is called ____.", "Tabulation"),
        ("The difference between the upper and lower class boundaries is known as class ____.", "Width (or Interval)"),
        ("The midpoint of a class is known as the class ____.", "Mark"),
        ("A ____ chart represents data using rectangles of equal width but varying heights.", "Bar"),
        ("A ____ diagram uses sectors of a circle to represent the components of a total.", "Pie"),
        ("The graphical representation of a grouped frequency distribution using contiguous rectangles is a ____.", "Histogram"),
        ("An Ogive is plotted using ____ frequencies.", "Cumulative"),
        ("The measure of central tendency defined as the sum of all observations divided by the number of observations is the ____.", "Arithmetic Mean"),
        ("The middlemost value in an ordered dataset is the ____.", "Median"),
        ("The value that occurs most frequently in a dataset is called the ____.", "Mode"),
        ("The nth root of the product of n observations is called the ____ Mean.", "Geometric"),
        ("The reciprocal of the arithmetic mean of the reciprocals of observations is the ____ Mean.", "Harmonic"),
        ("For averaging rates and speeds, the appropriate measure is the ____ Mean.", "Harmonic"),
        ("The sum of deviations of individual items from their arithmetic mean is always ____.", "Zero"),
        ("Values that divide a dataset into four equal parts are called ____.", "Quartiles"),
        ("Values that divide a dataset into ten equal parts are called ____.", "Deciles"),
        ("The Second Quartile (Q2) is equal to the ____.", "Median"),
        ("The ____ decile is equal to the median.", "5th (Fifth)"),
        ("The ____ percentile is equal to the Third Quartile (Q3).", "75th"),
        ("In a positively skewed distribution, the Mean is ____ than the Median.", "Greater"),
        ("The empirical formula connecting mean, median, and mode is Mode = 3 ____ - 2 Mean.", "Median"),
        ("A frequency polygon is obtained by joining the midpoints of the tops of the rectangles in a ____.", "Histogram"),
        ("Stem-and-leaf display retains the original ____ while grouping them.", "Values (or Data)"),
        ("For averaging growth rates or percentages, the ____ Mean is best.", "Geometric"),
        ("Extreme values strongly affect the ____.", "Arithmetic Mean"),
        ("If a dataset has two values with the highest identical frequency, it is called ____.", "Bimodal"),
        ("The number of observations falling in a particular class is called the class ____.", "Frequency"),
        ("A table has rows and ____.", "Columns"),
        ("The intersection of an Ogive 'less than' and Ogive 'more than' gives the ____.", "Median")
    ]
    
    tf_data = [
        ("Classification is the first step in data presentation before tabulation.", True),
        ("A bar chart can only be drawn vertically.", False),
        ("A pie chart shows the proportion of different components.", True),
        ("A histogram is used for categorical data.", False),
        ("An ogive is a cumulative frequency polygon.", True),
        ("The arithmetic mean is not affected by extreme values.", False),
        ("The median is the exact middle value of an ordered dataset.", True),
        ("The mode can be determined graphically using a histogram.", True),
        ("The median can be determined graphically using an ogive.", True),
        ("The geometric mean is always greater than or equal to the arithmetic mean.", False),
        ("Harmonic mean is useful for calculating average speed.", True),
        ("The sum of the deviations from the mean is always zero.", True),
        ("Quartiles divide the data into ten equal parts.", False),
        ("The 50th percentile is the same as the median.", True),
        ("The mode is always a unique value in any dataset.", False),
        ("Geometric mean cannot be calculated if any observation is zero.", True),
        ("A frequency polygon must touch the x-axis at both ends.", True),
        ("In a symmetric distribution, Mean = Median = Mode.", True),
        ("The 3rd quartile (Q3) leaves 25% of the observations below it.", False),
        ("Tabulation helps in easy comparison of data.", True),
        ("A multiple bar chart can show two or more related variables side-by-side.", True),
        ("The class mark is the sum of the lower and upper limits.", False),
        ("Stem-and-leaf plots lose individual data values.", False),
        ("Deciles divide the distribution into 100 equal parts.", False),
        ("The geometric mean of 2 and 8 is 4.", True),
        ("Weighted arithmetic mean gives equal importance to all items.", False),
        ("Arithmetic mean is based on all observations in the dataset.", True),
        ("The median is affected by the replacement of the extreme values.", False),
        ("A unimodal distribution has exactly one mode.", True),
        ("Relative frequency is the class frequency divided by the total frequency.", True)
    ]
    
    subj_data = [
        ("What are the main parts of a statistical table?", "A statistical table must have a Table Number, a Title, Headnotes (if necessary), Captions (column headings), Stubs (row headings), the Body (the actual data), and Footnotes/Source notes at the bottom."),
        ("Differentiate between Classification and Tabulation.", "Classification is the process of grouping data into homogeneous categories based on common characteristics. Tabulation is the systematic presentation of this classified data in rows and columns to facilitate comparison and analysis."),
        ("Explain the difference between a Bar Chart and a Histogram.", "A Bar Chart represents categorical or discrete data using separate bars with equal spacing between them. A Histogram represents grouped continuous frequency distributions using contiguous rectangles with no spaces between them."),
        ("What is an Ogive? How is it useful?", "An Ogive is a cumulative frequency curve. It is plotted using class boundaries on the x-axis and cumulative frequencies on the y-axis. It is highly useful for graphically determining partition values like the Median, Quartiles, and Deciles."),
        ("What are the characteristics of a good measure of central tendency?", "A good measure should be: 1) Rigidly defined, 2) Easy to calculate and understand, 3) Based on all observations, 4) Capable of further algebraic treatment, 5) Unaffected by extreme values (outliers), and 6) Stable across samples."),
        ("Why is the Arithmetic Mean the most widely used average?", "It is rigidly defined, based on all observations, easy to understand, and highly amenable to algebraic manipulations. It forms the basis for advanced statistical analysis like variance and regression."),
        ("Discuss the situations where the Median is preferred over the Mean.", "The Median is preferred when the dataset contains extreme values (outliers) that would distort the Mean, and when dealing with open-ended class intervals where the Mean cannot be computed accurately."),
        ("Explain the concept of the Geometric Mean and state its main application.", "The Geometric Mean is the nth root of the product of n observations. It is best applied when dealing with ratios, percentages, or rates of change, such as calculating average population growth or compound interest."),
        ("What is the Harmonic Mean? Give an example of its use.", "The Harmonic Mean is the reciprocal of the arithmetic mean of the reciprocals of the data values. It is exceptionally useful for averaging rates and ratios, such as finding the average speed of a vehicle traveling equal distances at different speeds."),
        ("Explain the Empirical Relationship between Mean, Median, and Mode.", "For moderately skewed distributions, the difference between the mean and mode is approximately three times the difference between the mean and median. The formula is: Mode = 3(Median) - 2(Mean)."),
        ("Define Partition Values and name the three main types.", "Partition values are points that divide an ordered dataset into equal parts. The three main types are Quartiles (divide into 4 parts), Deciles (10 parts), and Percentiles (100 parts)."),
        ("What is the difference between Class Limits and Class Boundaries?", "Class Limits are the smallest and largest values included in a class. Class Boundaries are the true limits used to ensure continuity in grouped data, removing the gap between the upper limit of one class and the lower limit of the next."),
        ("How do you graphically locate the Median of a frequency distribution?", "The median can be located by drawing an Ogive (cumulative frequency curve). Locate N/2 on the y-axis, draw a horizontal line to the curve, and then drop a perpendicular to the x-axis. The point on the x-axis is the Median."),
        ("How do you graphically locate the Mode of a frequency distribution?", "Draw a Histogram. Identify the tallest rectangle (modal class). Draw diagonal lines from the top corners of this rectangle to the top corners of the adjacent rectangles. The intersection point dropped to the x-axis gives the Mode."),
        ("Describe a Pie Chart and its construction.", "A Pie Chart is a circular diagram divided into sectors, where the angle of each sector is proportional to the magnitude of the component it represents. Angle = (Component Value / Total Value) * 360°."),
        ("What is a Stem-and-Leaf display? Why is it better than a frequency distribution?", "It is a technique that organizes numerical data by splitting each value into a 'stem' (leading digit) and a 'leaf' (trailing digit). Unlike a frequency distribution, it retains the exact original data values while showing the distribution shape."),
        ("Define Relative Frequency and Cumulative Frequency.", "Relative Frequency is the frequency of a class divided by the total frequency. Cumulative Frequency is the running total of frequencies, showing the number of observations falling below (or above) a certain boundary."),
        ("Explain the concept of Weighted Arithmetic Mean.", "When observations in a dataset are not of equal importance, weights are assigned to them. The Weighted Mean is calculated by multiplying each observation by its weight, summing these products, and dividing by the sum of the weights."),
        ("What are Quartiles? Explain Q1, Q2, and Q3.", "Quartiles divide data into 4 equal parts. Q1 (Lower Quartile) has 25% of data below it. Q2 is the Median (50% below). Q3 (Upper Quartile) has 75% of data below it."),
        ("A farmer wants to compare the area under three crops and their respective yields over 5 years. Which graphical tool should he use?", "A Multiple Bar Chart is ideal here, as it allows side-by-side comparison of multiple variables (area and yield) across different categories (years) simultaneously.")
    ]
    
    eng_html = '''
        <h2><span class="section-num">❓</span> Multiple Choice Questions — 30 Questions</h2>
        <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
            Click <em>Show Answer</em> to reveal the correct option and explanation.
        </p>
    '''
    hin_html = '''
        <h2><span class="section-num">❓</span> Multiple Choice Questions (बहुविकल्पीय प्रश्न) — 30 Questions</h2>
        <p style="color:var(--text-soft);font-family:'DM Sans',sans-serif;font-size:.9rem;margin-bottom:20px;">
            सही विकल्प देखने के लिए <em>Show Answer</em> पर क्लिक करें।
        </p>
    '''
    for i, (q, opts, ans_idx) in enumerate(mcq_data, 1):
        opt_str = " &nbsp;&nbsp; ".join(opts)
        ans_text = opts[ans_idx]
        eng_html += f'''
        <div class="question"><strong>Q{i}.</strong> {q}<div class="mcq-options"><p>{opt_str}</p></div></div>
        <button class="toggle-btn" onclick="toggleAnswer('mcq-eng-{i}')">Show Answer ▼</button>
        <div class="answer" id="mcq-eng-{i}"><strong>Answer:</strong> {ans_text}</div>
        '''
        hin_html += f'''
        <div class="question"><strong>Q{i}.</strong> {t(q)}<div class="mcq-options"><p>{" &nbsp;&nbsp; ".join([t(o) for o in opts])}</p></div></div>
        <button class="toggle-btn" onclick="toggleAnswer('mcq-hin-{i}')">Show Answer ▼</button>
        <div class="answer" id="mcq-hin-{i}"><strong>Answer:</strong> {t(ans_text)}</div>
        '''
    mcq_block = f'<div id="mcq" class="topic-section"><section class="section-card"><div class="english-content">{eng_html}</div><div class="hinglish-content" style="display:none;">{hin_html}</div></section></div>'

    eng_html = '<h2><span class="section-num">✏️</span> Fill in the Blanks — 30 Questions</h2>'
    hin_html = '<h2><span class="section-num">✏️</span> Fill in the Blanks (रिक्त स्थान भरें) — 30 Questions</h2>'
    for i, (q, ans) in enumerate(fib_data, 1):
        eng_html += f'<div class="question"><strong>Q{i}.</strong> {q}</div><button class="toggle-btn" onclick="toggleAnswer(\'fib-eng-{i}\')">Show Answer ▼</button><div class="answer" id="fib-eng-{i}"><strong>Answer:</strong> {ans}</div>'
        hin_html += f'<div class="question"><strong>Q{i}.</strong> {t(q)}</div><button class="toggle-btn" onclick="toggleAnswer(\'fib-hin-{i}\')">Show Answer ▼</button><div class="answer" id="fib-hin-{i}"><strong>Answer:</strong> {t(ans)}</div>'
    fib_block = f'<div id="fib" class="topic-section"><section class="section-card"><div class="english-content">{eng_html}</div><div class="hinglish-content" style="display:none;">{hin_html}</div></section></div>'

    eng_html = '<h2><span class="section-num">✅</span> True / False — 30 Questions</h2>'
    hin_html = '<h2><span class="section-num">✅</span> True / False (सही/गलत) — 30 Questions</h2>'
    for i, (q, ans) in enumerate(tf_data, 1):
        eng_html += f'<div class="question"><strong>Q{i}.</strong> {q}</div><button class="toggle-btn" onclick="toggleAnswer(\'tf-eng-{i}\')">Show Answer ▼</button><div class="answer" id="tf-eng-{i}"><strong>Answer:</strong> {"True" if ans else "False"}</div>'
        hin_html += f'<div class="question"><strong>Q{i}.</strong> {t(q)}</div><button class="toggle-btn" onclick="toggleAnswer(\'tf-hin-{i}\')">Show Answer ▼</button><div class="answer" id="tf-hin-{i}"><strong>Answer:</strong> {"सही (True)" if ans else "गलत (False)"}</div>'
    tf_block = f'<div id="tf" class="topic-section"><section class="section-card"><div class="english-content">{eng_html}</div><div class="hinglish-content" style="display:none;">{hin_html}</div></section></div>'

    eng_html = '<h2><span class="section-num">📝</span> Subjective Questions — 20 Questions</h2>'
    hin_html = '<h2><span class="section-num">📝</span> Subjective Questions (विषयपरक प्रश्न) — 20 Questions</h2>'
    for i, (q, ans) in enumerate(subj_data, 1):
        eng_html += f'<div class="question"><strong>Q{i}.</strong> {q}</div><button class="toggle-btn" onclick="toggleAnswer(\'subj-eng-{i}\')">Show Answer ▼</button><div class="answer" id="subj-eng-{i}"><p>{ans}</p></div>'
        hin_html += f'<div class="question"><strong>Q{i}.</strong> {t(q)}</div><button class="toggle-btn" onclick="toggleAnswer(\'subj-hin-{i}\')">Show Answer ▼</button><div class="answer" id="subj-hin-{i}"><p>{t(ans)}</p></div>'
    subj_block = f'<div id="subj" class="topic-section"><section class="section-card"><div class="english-content">{eng_html}</div><div class="hinglish-content" style="display:none;">{hin_html}</div></section></div>'

    return mcq_block + fib_block + tf_block + subj_block

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unit II – Presentation of Data & Central Tendency | STAT-M-101</title>
    
    <!-- MathJax -->
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700&family=Source+Serif+4:ital,wght@0,400;0,600&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
    
    <link rel="stylesheet" href="../common_style.css">
    <link rel="stylesheet" href="stat101_style.css">
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

        /* Ensure shared visuals stay centered */
        .shared-visual { margin: 24px 0; padding: 16px; background: #fff; border-radius: 8px; box-shadow: var(--shadow-sm); }
        
        /* OVERRIDE for Chart.js compatibility in hidden tabs */
        .topic-section {
            display: block !important;
            height: 0;
            overflow: hidden;
            visibility: hidden;
            opacity: 0;
            position: absolute;
            animation: none;
            width: 100%;
        }
        .topic-section.active {
            height: auto;
            overflow: visible;
            visibility: visible;
            opacity: 1;
            position: relative;
            animation: fadeSlideIn .45s ease;
        }
    </style>
</head>
<body>
    <header class="book-header">
        <button class="menu-toggle" onclick="toggleSidebar()" aria-label="Toggle menu"><i class="fas fa-bars"></i></button>
        <div class="header-icon">📈</div>
        <div class="header-text">
            <h1>Statistical Methods-I</h1>
            <div class="subtitle">UNIT II · PRESENTATION OF DATA & CENTRAL TENDENCY</div>
        </div>
        <div class="header-badge">Prof. O.P. Sheoran</div>
        <button class="draw-mode-toggle" id="draw-mode-btn"><i class="fas fa-chalkboard"></i> Open Whiteboard</button>
    </header>

    <nav class="sidebar" id="sidebar">
        <div class="sidebar-brand">
            <h2>Unit II</h2>
            <p>Presentation & Averages<br>CCS Haryana Agricultural University</p>
        </div>
        <div class="sidebar-author">
            <img src="../Stat-102/opsheoran.png" alt="Prof. O.P. Sheoran" class="sidebar-photo">
            <div class="sidebar-author-info">
                <h3>Prof. O.P. Sheoran</h3><p>Author & Instructor</p>
            </div>
        </div>

        <div class="nav-group-label">Navigation</div>
        <ul class="nav-list">
            <li class="nav-item"><a class="nav-link" href="index.html" style="background: rgba(200,146,42,0.1); color: var(--gold-light); font-weight: 600;"><span class="nav-num">🏠</span> Course Home</a></li>
            <li class="nav-item"><a class="nav-link" href="../index.html" style="background: rgba(27,42,74,0.3); color: white; font-weight: 600; margin-top: 5px;"><span class="nav-num">📚</span> Back to Library</a></li>
        </ul>

        <div class="nav-group-label">Theory Topics</div>
        <ul class="nav-list">
        {NAV_LINKS_PLACEHOLDER}
        </ul>
        
        <div class="nav-group-label">Practice Exercises</div>
        <ul class="nav-list">
            <li class="nav-item"><a class="nav-link" href="#mcq" onclick="showTopic('mcq');return false;"><span class="nav-num">❓</span> Multiple Choice</a></li>
            <li class="nav-item"><a class="nav-link" href="#fib" onclick="showTopic('fib');return false;"><span class="nav-num">✏️</span> Fill in Blanks</a></li>
            <li class="nav-item"><a class="nav-link" href="#tf" onclick="showTopic('tf');return false;"><span class="nav-num">✅</span> True / False</a></li>
            <li class="nav-item"><a class="nav-link" href="#subj" onclick="showTopic('subj');return false;"><span class="nav-num">📝</span> Subjective Qs</a></li>
        </ul>
    </nav>

    <main class="main-content">
        <div class="chapter-header">
            <button id="lang-toggle-btn" class="header-lang-toggle" onclick="toggleLanguage()">
                <i class="fas fa-language"></i> <span id="lang-toggle-text">Switch Language (Hinglish)</span>
            </button>
            <h1>Unit II: Presentation of Data & Central Tendency</h1>
            <div class="author">By Prof. O.P. Sheoran</div>
            <div class="syllabus-tag">
                <strong>Syllabus:</strong> Presentation of Data. Measures of Central Tendency and Location. Partition Values.
            </div>
        </div>

        {VERBATIM_PLACEHOLDER}
        {EXERCISES_PLACEHOLDER}

    </main>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const hash = window.location.hash.substring(1);
            if (hash && document.getElementById(hash)) {
                showTopic(hash);
            } else {
                const firstSec = document.querySelector('.topic-section');
                if(firstSec) showTopic(firstSec.id);
            }
        });

        let isHinglish = false;
        function toggleLanguage() {
            isHinglish = !isHinglish;
            const btnText = document.getElementById('lang-toggle-text');
            const engContents = document.querySelectorAll('.english-content');
            const hinContents = document.querySelectorAll('.hinglish-content');

            if (isHinglish) {
                btnText.innerHTML = '<i class="fas fa-language"></i> Switch Language (English)';
                engContents.forEach(el => el.style.display = 'none');
                hinContents.forEach(el => el.style.display = 'block');
            } else {
                btnText.innerHTML = '<i class="fas fa-language"></i> Switch Language (Hinglish)';
                hinContents.forEach(el => el.style.display = 'none');
                engContents.forEach(el => el.style.display = 'block');
            }
        }

        function showTopic(id) {
            document.querySelectorAll('.topic-section').forEach(el => {
                el.classList.remove('active');
            });
            document.querySelectorAll('.nav-link').forEach(el => {
                el.classList.remove('active');
            });
            
            const targetSection = document.getElementById(id);
            if (targetSection) {
                targetSection.classList.add('active');
            }
            
            const activeLink = document.querySelector(`.nav-link[href="#${id}"]`);
            if (activeLink) {
                activeLink.classList.add('active');
            }
            
            window.scrollTo(0,0);
            
            if (window.innerWidth <= 768) {
                document.getElementById('sidebar').classList.remove('open');
            }
            
            history.replaceState(null, null, '#' + id);
        }

        function toggleSidebar() { document.getElementById('sidebar').classList.toggle('open'); }

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
    
    {SHARED_SCRIPTS_PLACEHOLDER}
    <script src="../whiteboard/whiteboard.js?v=2.0"></script>
</body>
</html>
"""

def extract_and_combine(file2, file3):
    print("Reading files...")
    with open(file2, 'r', encoding='utf-8') as f:
        soup2 = BeautifulSoup(f.read(), 'html.parser')
    with open(file3, 'r', encoding='utf-8') as f:
        soup3 = BeautifulSoup(f.read(), 'html.parser')

    all_sections = []
    shared_scripts = ""
    
    # 1. Extract all global scripts exactly ONCE from the source
    for s in soup2.find_all('script'):
        if not s.get('src') and not 'MathJax' in s.text:
            shared_scripts += str(s) + '\n'
            s.decompose() 

    for s in soup3.find_all('script'):
        if not s.get('src') and not 'MathJax' in s.text:
            shared_scripts += str(s) + '\n'
            s.decompose()

    # 2. Flatten sections
    for s in soup2.find_all(['div', 'section'], class_='section'):
        if not s.get('id') or 'exercises' in s.get('id').lower(): continue
        s.extract() 
        all_sections.append(s)
        
    for s in soup3.find_all(['div', 'section'], class_='section'):
        if not s.get('id') or 'exercises' in s.get('id').lower(): continue
        s.extract()
        all_sections.append(s)

    nav_links = ""
    sections_html = ""
    current_h2 = 0
    current_h3 = 0
    
    for idx, section in enumerate(all_sections):
        sec_id = section.get('id')
        
        # Prevent nested IDs routing breakage
        for nested in section.find_all(['div', 'section'], class_='section'):
            if nested.get('id') and nested != section:
                del nested['id']
        
        head_div = section.find('div', class_='head')
        nav_title = "Section"
        nav_num = ""
        nav_level = "h2"
        
        if head_div:
            num_div = head_div.find('div', class_='num')
            title_div = head_div.find('h2', class_='title') or head_div.find('h3', class_='title') or head_div.find('div', class_='title')
            
            if title_div:
                nav_title = title_div.get_text(strip=True)
                orig_num = num_div.get_text(strip=True) if num_div else ""
                
                if orig_num == "3.1" and nav_title.upper() == "INTRODUCTION":
                    nav_title = "Measures of Central Tendency"
                
                dots = orig_num.count('.')
                if dots == 1:
                    current_h2 += 1
                    current_h3 = 0
                    nav_num = f"2.{current_h2}"
                    nav_level = 'h2'
                elif dots == 2:
                    current_h3 += 1
                    nav_num = f"2.{current_h2}.{current_h3}"
                    nav_level = 'h3'
                else:
                    nav_num = orig_num
                    nav_level = 'h4'

                new_h = BeautifulSoup(f"<{nav_level}>{nav_num} {nav_title}</{nav_level}>", 'html.parser')
                head_div.replace_with(new_h)
        
        if nav_level == 'h2':
            nav_links += f'<li class="nav-item"><a class="nav-link" href="#{sec_id}" onclick="showTopic(\'{sec_id}\');return false;"><span class="nav-num">{nav_num}</span> {nav_title}</a></li>\n'
        elif nav_level == 'h3':
            nav_links += f'<li class="nav-item nav-sub"><a class="nav-link" href="#{sec_id}" onclick="showTopic(\'{sec_id}\');return false;"><span class="nav-num">{nav_num}</span> {nav_title}</a></li>\n'

        # Extract visual blocks so they aren't hidden by language toggles
        # Using extract() directly so we can append them at the end of the section instead of trying to interleave with string splits, which caused the DOM breakage.
        visual_blocks = []
        for visual in section.find_all(['canvas', 'div'], class_=lambda c: c in ['chart-container', 'chart-item', 'cg-mb-6'] if c else False):
            if visual.name == 'canvas':
                if visual.parent and visual.parent.get('class') and any(c in visual.parent.get('class') for c in ['chart-container', 'chart-item']):
                    continue
            
            visual_html = str(visual)
            visual_blocks.append(visual_html)
            visual.extract()

        # Decompose any stray scripts again just in case
        for script in section.find_all('script'):
            script.decompose()

        eng_html_raw = "".join([str(child) for child in section.children])

        # Mathematical equations
        eng_html_raw = re.sub(r'<p>\s*(\\\[.*?\\\])\s*</p>', r'<div class="formula-box">\1</div>', eng_html_raw, flags=re.DOTALL)
        eng_html_raw = re.sub(r'(?<!<div class="formula-box">)\s*(\\\[.*?\\\])\s*(?!</div>)', r'<div class="formula-box">\1</div>', eng_html_raw, flags=re.DOTALL)
        eng_html_raw = re.sub(r'<p>\s*(\\\(.*?\\\))\s*</p>', r'<p class="derivation">\1</p>', eng_html_raw, flags=re.DOTALL)

        print(f"Translating section: {sec_id}")
        hin_html_raw = translate_html_block(eng_html_raw)

        # Build final section content securely by appending visuals at the END of the section
        # This completely guarantees the DOM is never broken by regex splits
        shared_visuals_html = ""
        for vis_html in visual_blocks:
            shared_visuals_html += f'<div class="shared-visual">{vis_html}</div>\n'

        sections_html += f'''
            <div class="topic-section" id="{sec_id}">
                <section class="section-card">
                    <div class="english-content">{eng_html_raw}</div>
                    <div class="hinglish-content" style="display:none;">{hin_html_raw}</div>
                    {shared_visuals_html}
                </section>
            </div>
        '''
        
    return nav_links, sections_html, shared_scripts

print("Processing Unit II...")
nav_links_html, sections_html, shared_scripts = extract_and_combine('Stat-101/Chapter2.html', 'Stat-101/Chapter3.html')

print("Generating True Hinglish exercises...")
exercises_html = generate_unit2_exercises()

print("Replacing placeholders...")
final_html = html_template.replace('{NAV_LINKS_PLACEHOLDER}', f'<div class="nav-group-label">Theory Topics</div><ul class="nav-list">{nav_links_html}</ul>')\
                          .replace('{VERBATIM_PLACEHOLDER}', sections_html)\
                          .replace('{EXERCISES_PLACEHOLDER}', exercises_html)\
                          .replace('{SHARED_SCRIPTS_PLACEHOLDER}', shared_scripts)

print("Writing final file...")
with open('Stat-101/Unit-II.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Stat-101/Unit-II.html fully generated without JS duplicate errors and with full graphs!")
