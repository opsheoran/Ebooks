import re
import os

with open("Chapter5.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Sidebar
sidebar_old = r"""<div style="padding: 10px 20px; color: var(--gold); font-size: 0.8rem; font-weight: bold; text-transform: uppercase;">Quizzes</div>
        <a class="nav-link" onclick="showTopic('quiz-mcq')">❓ Multiple Choice</a>
        <a class="nav-link" onclick="showTopic('quiz-fib')">✏️ Fill in Blanks</a>
        <a class="nav-link" onclick="showTopic('quiz-tf')">✅ True / False</a>
        <hr style="border: 0.5px solid rgba(255,255,255,0.1); margin: 15px 20px;">
        <a class="nav-link" href="index.html"><i class="fas fa-home"></i> Back to Index</a>"""

sidebar_new = r"""<hr style="border: 0.5px solid rgba(255,255,255,0.1); margin: 15px 20px;">
        <div style="padding: 10px 20px; color: var(--gold); font-size: 0.8rem; font-weight: bold; text-transform: uppercase;">Quizzes / Exercises</div>
        <a class="nav-link" onclick="showTopic('quiz-mcq')">❓ Multiple Choice</a>
        <a class="nav-link" onclick="showTopic('quiz-fib')">✏️ Fill in Blanks</a>
        <a class="nav-link" onclick="showTopic('quiz-tf')">✅ True / False</a>
        <a class="nav-link" onclick="showTopic('sec5-13')">📝 Exercise (Subjective)</a>
        <hr style="border: 0.5px solid rgba(255,255,255,0.1); margin: 15px 20px;">
        <a class="nav-link" href="index.html"><i class="fas fa-home"></i> Back to Index</a>"""

html = html.replace(sidebar_old, sidebar_new)
html = html.replace("""<a class="nav-link" onclick="showTopic('sec5-13')">Set of Problems</a>\n        <hr style="border: 0.5px solid rgba(255,255,255,0.1); margin: 15px 20px;">""", "")

# 2. Add References & Update Set of Problems to Exercise (Subjective)
problems_old = r"""<section id="sec5-13" class="section-card">
            <div class="english-content">
                <h2>Set of Problems</h2>"""

problems_new = r"""<section id="sec5-ref" class="section-card">
            <div class="english-content">
                <h2>References</h2>
                <ul>
                    <li>Cochran, W. G. (1977). <em>Sampling Techniques</em> (3rd ed.). John Wiley & Sons.</li>
                    <li>Singh, D., & Chaudhary, F. S. (1986). <em>Theory and Analysis of Sample Survey Designs</em>. New Age International.</li>
                    <li>Lahiri, D. B. (1951). A method of sample selection providing unbiased ratio estimates. <em>Bull. Int. Statist. Inst.</em>, 33, 133-140.</li>
                    <li>Horvitz, D. G., & Thompson, D. J. (1952). A generalization of sampling without replacement from a finite universe. <em>J. Amer. Statist. Assoc.</em>, 47, 663-685.</li>
                    <li>Des Raj (1956). Some estimators in sampling with varying probabilities without replacement. <em>J. Amer. Statist. Assoc.</em>, 51, 269-284.</li>
                    <li>Murthy, M. N. (1957). Ordered and unordered estimators in sampling without replacement. <em>Sankhya</em>, 18, 379-390.</li>
                    <li>Midzuno, H. (1952). On the sampling system with probability proportionate to sum of sizes. <em>Ann. Inst. Statist. Math.</em>, 3, 99-107.</li>
                    <li>Rao, J. N. K., Hartley, H. O., & Cochran, W. G. (1962). On a simple procedure of unequal probability sampling without replacement. <em>J.R. Statist. Soc.</em>, 24B, 482-491.</li>
                </ul>
            </div>
            <div class="hinglish-content">
                <h2>References (संदर्भ)</h2>
                <ul>
                    <li>Cochran, W. G. (1977). <em>Sampling Techniques</em> (3rd ed.). John Wiley & Sons.</li>
                    <li>Singh, D., & Chaudhary, F. S. (1986). <em>Theory and Analysis of Sample Survey Designs</em>. New Age International.</li>
                    <li>Lahiri, D. B. (1951). A method of sample selection providing unbiased ratio estimates. <em>Bull. Int. Statist. Inst.</em>, 33, 133-140.</li>
                    <li>Horvitz, D. G., & Thompson, D. J. (1952). A generalization of sampling without replacement from a finite universe. <em>J. Amer. Statist. Assoc.</em>, 47, 663-685.</li>
                    <li>Des Raj (1956). Some estimators in sampling with varying probabilities without replacement. <em>J. Amer. Statist. Assoc.</em>, 51, 269-284.</li>
                    <li>Murthy, M. N. (1957). Ordered and unordered estimators in sampling without replacement. <em>Sankhya</em>, 18, 379-390.</li>
                    <li>Midzuno, H. (1952). On the sampling system with probability proportionate to sum of sizes. <em>Ann. Inst. Statist. Math.</em>, 3, 99-107.</li>
                    <li>Rao, J. N. K., Hartley, H. O., & Cochran, W. G. (1962). On a simple procedure of unequal probability sampling without replacement. <em>J.R. Statist. Soc.</em>, 24B, 482-491.</li>
                </ul>
            </div>
        </section>

        <section id="sec5-13" class="section-card">
            <div class="english-content">
                <h2>Exercise (Subjective)</h2>"""

html = html.replace(problems_old, problems_new)
html = html.replace("<h2>Set of Problems (समस्याओं का समूह)</h2>", "<h2>Exercise (Subjective) (अभ्यास - व्यक्तिपरक)</h2>")

# 3. Replace Quizzes
quizzes_start = html.find('<!-- QUIZZES SECTION -->')
if quizzes_start != -1:
    html = html[:quizzes_start]

quizzes_content = r"""<!-- QUIZZES SECTION -->
        <section id="quiz-mcq" class="section-card">
            <h2>❓ Multiple Choice Questions (बहुविकल्पीय प्रश्न)</h2>
            
            <div class="question-box">
                <div class="question">1. In PPS sampling, the probability of selecting a unit is proportional to: <br> (PPS सैंपलिंग में, किसी इकाई को चुनने की प्रायिकता किसके समानुपाती होती है?)</div>
                <ul class="mcq-options">
                    <li>a) Sample size (\(n\))</li>
                    <li>b) Size of the unit (\(X_i\))</li>
                    <li>c) Population size (\(N\))</li>
                    <li>d) Variance of the population (\(S^2\))</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq1')">Show/Hide Answer</button>
                <div id="mcq1" class="answer"><strong>Correct Answer:</strong> b) Size of the unit (\(X_i\)) <br> <em>Explanation:</em> The core principle of Probability Proportional to Size (PPS) sampling is that larger units have a higher probability of selection, explicitly \( p_i = X_i/X \).</div>
            </div>
            
            <div class="question-box">
                <div class="question">2. Which method uses cumulative totals to select a PPS sample? <br> (PPS प्रतिदर्श चुनने के लिए कौन सी विधि संचयी योग का उपयोग करती है?)</div>
                <ul class="mcq-options">
                    <li>a) Lahiri's Method</li>
                    <li>b) Des Raj Method</li>
                    <li>c) Cumulative Total Method</li>
                    <li>d) Midzuno Method</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq2')">Show/Hide Answer</button>
                <div id="mcq2" class="answer"><strong>Correct Answer:</strong> c) Cumulative Total Method <br> <em>Explanation:</em> This method calculates the cumulative sum of sizes and selects a unit based on a random number falling within its cumulative range.</div>
            </div>

            <div class="question-box">
                <div class="question">3. What is the major mathematical drawback of the Cumulative Total Method? <br> (संचयी योग विधि का प्रमुख गणितीय दोष क्या है?)</div>
                <ul class="mcq-options">
                    <li>a) It is biased</li>
                    <li>b) It fails for large samples</li>
                    <li>c) It requires calculating massive successive cumulative totals</li>
                    <li>d) It cannot be used with replacement</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq3')">Show/Hide Answer</button>
                <div id="mcq3" class="answer"><strong>Correct Answer:</strong> c) It requires calculating massive successive cumulative totals <br> <em>Explanation:</em> The absolute compulsion to compute massive successive cumulative totals rapidly becomes time-consuming and computationally costly when the population size \( N \) is astronomically large.</div>
            </div>

            <div class="question-box">
                <div class="question">4. Lahiri's method was developed specifically to avoid: <br> (लाहिड़ी की विधि विशेष रूप से किस चीज़ से बचने के लिए विकसित की गई थी?)</div>
                <ul class="mcq-options">
                    <li>a) Calculating variances</li>
                    <li>b) Calculating cumulative totals</li>
                    <li>c) Ordered estimators</li>
                    <li>d) Negative probabilities</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq4')">Show/Hide Answer</button>
                <div id="mcq4" class="answer"><strong>Correct Answer:</strong> b) Calculating cumulative totals <br> <em>Explanation:</em> Lahiri (1951) elegantly suggested an alternative procedure in which tedious mathematical cumulations are completely avoided.</div>
            </div>

            <div class="question-box">
                <div class="question">5. In Lahiri's method, what does \( M \) denote? <br> (लाहिड़ी की विधि में, \( M \) क्या दर्शाता है?)</div>
                <ul class="mcq-options">
                    <li>a) Sample size</li>
                    <li>b) Number of strata</li>
                    <li>c) The absolute maximum size among all \( N \) units</li>
                    <li>d) Total population size</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq5')">Show/Hide Answer</button>
                <div id="mcq5" class="answer"><strong>Correct Answer:</strong> c) The absolute maximum size among all \( N \) units <br> <em>Explanation:</em> A random number is cleanly chosen between 1 and \( M \), where \( M \) is mathematically the absolute maximum size among all the \( N \) units of the population.</div>
            </div>

            <div class="question-box">
                <div class="question">6. In PPS sampling with replacement, the estimator \( \widehat{Y}_{pps} = \frac{1}{n} \sum_{i=1}^n \frac{y_i}{p_i} \) is: <br> (प्रतिस्थापन के साथ PPS प्रतिचयन में, अनुमानक \( \widehat{Y}_{pps} \) है:)</div>
                <ul class="mcq-options">
                    <li>a) Always biased</li>
                    <li>b) Unbiased for the population total</li>
                    <li>c) Unbiased for the population mean</li>
                    <li>d) Both b and c</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq6')">Show/Hide Answer</button>
                <div id="mcq6" class="answer"><strong>Correct Answer:</strong> b) Unbiased for the population total <br> <em>Explanation:</em> Theorem 5.3.1 strictly proves that \( E(\widehat{Y}_{pps}) = Y \), making it an unbiased estimator of the population total.</div>
            </div>

            <div class="question-box">
                <div class="question">7. Simple random sampling can be considered a special case of PPS sampling where: <br> (सरल यादृच्छिक प्रतिचयन को PPS प्रतिचयन का एक विशेष मामला माना जा सकता है जहाँ:)</div>
                <ul class="mcq-options">
                    <li>a) \( p_i = 1/N \)</li>
                    <li>b) \( p_i = 1/n \)</li>
                    <li>c) \( p_i = n/N \)</li>
                    <li>d) \( p_i = X_i/N \)</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq7')">Show/Hide Answer</button>
                <div id="mcq7" class="answer"><strong>Correct Answer:</strong> a) \( p_i = 1/N \) <br> <em>Explanation:</em> If the probability of selection for all units is equal (\( 1/N \)), PPS flawlessly reduces to a simple random sample.</div>
            </div>

            <div class="question-box">
                <div class="question">8. In PPS sampling without replacement, as the sample size increases, calculating exact inclusion probabilities \( \pi_i \) and \( \pi_{ij} \) becomes: <br> (प्रतिस्थापन के बिना PPS प्रतिचयन में, जैसे-जैसे नमूने का आकार बढ़ता है, \( \pi_i \) और \( \pi_{ij} \) की गणना करना हो जाता है:)</div>
                <ul class="mcq-options">
                    <li>a) Linearly simpler</li>
                    <li>b) Intensely complex and tedious</li>
                    <li>c) Constant</li>
                    <li>d) Unnecessary</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq8')">Show/Hide Answer</button>
                <div id="mcq8" class="answer"><strong>Correct Answer:</strong> b) Intensely complex and tedious <br> <em>Explanation:</em> The exact mathematical computations unavoidably become intensely tedious safely for exact \( n \) explicitly greater definitively than 2.</div>
            </div>

            <div class="question-box">
                <div class="question">9. Which estimator takes the exact true order of selected units into account? <br> (कौन सा अनुमानक चयनित इकाइयों के सटीक वास्तविक क्रम को ध्यान में रखता है?)</div>
                <ul class="mcq-options">
                    <li>a) Horvitz-Thompson Estimator</li>
                    <li>b) Murthy's Estimator</li>
                    <li>c) Des Raj's Estimator</li>
                    <li>d) Midzuno's Estimator</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq9')">Show/Hide Answer</button>
                <div id="mcq9" class="answer"><strong>Correct Answer:</strong> c) Des Raj's Estimator <br> <em>Explanation:</em> Des Raj (1956) strictly proposed an ordered estimator that makes flawless use exclusively of sequential conditional specific probabilities based firmly on the specific true order securely of exact units safely selected.</div>
            </div>

            <div class="question-box">
                <div class="question">10. The Horvitz-Thompson estimator is an example of an: <br> (हॉर्विट्ज़-थॉम्पसन अनुमानक किसका एक उदाहरण है:)</div>
                <ul class="mcq-options">
                    <li>a) Ordered estimator</li>
                    <li>b) Unordered estimator</li>
                    <li>c) Biased estimator</li>
                    <li>d) Inconsistent estimator</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq10')">Show/Hide Answer</button>
                <div id="mcq10" class="answer"><strong>Correct Answer:</strong> b) Unordered estimator <br> <em>Explanation:</em> Horvitz and Thompson (1952) suggested strictly exactly an explicit estimator which does strictly not safely depend cleanly on the true exact order explicitly in which the true specific units definitively are cleanly carefully drawn.</div>
            </div>

            <div class="question-box">
                <div class="question">11. In general, mathematically, which class of estimators is more highly efficient? <br> (सामान्य तौर पर, गणितीय रूप से, अनुमानकों का कौन सा वर्ग अधिक कुशल है?)</div>
                <ul class="mcq-options">
                    <li>a) Ordered estimators</li>
                    <li>b) Unordered estimators</li>
                    <li>c) Both are exactly equal</li>
                    <li>d) Simple Random Estimators</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq11')">Show/Hide Answer</button>
                <div id="mcq11" class="answer"><strong>Correct Answer:</strong> b) Unordered estimators <br> <em>Explanation:</em> Murthy (1957) and Basu (1958) have elegantly mathematically shown safely that cleanly these specific explicit unordered estimators explicitly securely are rigorously more highly efficient heavily exactly than ordered proper estimators.</div>
            </div>

            <div class="question-box">
                <div class="question">12. Under Narain's Scheme of Sample Selection, the exact inclusion probabilities \( \pi_i \) are proportional exclusively to: <br> (नारायण की प्रतिदर्श चयन योजना के तहत, सटीक समावेशन प्रायिकताएँ \( \pi_i \) विशेष रूप से किसके समानुपाती होती हैं?)</div>
                <ul class="mcq-options">
                    <li>a) \( S^2 \)</li>
                    <li>b) Sample size \( n \)</li>
                    <li>c) Original probabilities of explicit selection \( p_i \)</li>
                    <li>d) \( \pi_{ij} \)</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq12')">Show/Hide Answer</button>
                <div id="mcq12" class="answer"><strong>Correct Answer:</strong> c) Original probabilities of explicit selection \( p_i \) <br> <em>Explanation:</em> The scheme involves constructing completely revised distinct probabilities of specific selection \( p_i' \) such that the exact inclusion probabilities \( \pi_i \) are strictly proportional exclusively to the original probabilities of explicit selection \( p_i \).</div>
            </div>

            <div class="question-box">
                <div class="question">13. In the Random Group Method (Rao, Hartley, Cochran), the population of \( N \) units is divided at random into how many groups? <br> (रैंडम ग्रुप मेथड में, \( N \) इकाइयों की आबादी को यादृच्छिक रूप से कितने समूहों में विभाजित किया जाता है?)</div>
                <ul class="mcq-options">
                    <li>a) \( N \) groups</li>
                    <li>b) \( M \) groups</li>
                    <li>c) \( n \) groups</li>
                    <li>d) 2 groups</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq13')">Show/Hide Answer</button>
                <div id="mcq13" class="answer"><strong>Correct Answer:</strong> c) \( n \) groups <br> <em>Explanation:</em> The method consists of dividing the units of the population into \( n \) groups at random and then selecting one unit with pps from each of the \( n \) random groups.</div>
            </div>

            <div class="question-box">
                <div class="question">14. What is the variance of the Horvitz-Thompson estimator? <br> (हॉर्विट्ज़-थॉम्पसन अनुमानक का प्रसरण क्या है?)</div>
                <ul class="mcq-options">
                    <li>a) \( \sum_i \frac{1 - \pi_i}{\pi_i} y_i^2 + \sum_i \sum_{j \neq i} \frac{\pi_{ij} - \pi_i \pi_j}{\pi_i \pi_j} y_i y_j \)</li>
                    <li>b) \( \sum_i \frac{\pi_i - 1}{\pi_i} y_i^2 \)</li>
                    <li>c) \( \frac{\pi_{ij}}{\pi_i \pi_j} y_i y_j \)</li>
                    <li>d) \( \frac{(N-1)S^2}{n} \)</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq14')">Show/Hide Answer</button>
                <div id="mcq14" class="answer"><strong>Correct Answer:</strong> a) \( \sum_i \frac{1 - \pi_i}{\pi_i} y_i^2 + \sum_i \sum_{j \neq i} \frac{\pi_{ij} - \pi_i \pi_j}{\pi_i \pi_j} y_i y_j \) <br> <em>Explanation:</em> Theorem 5.9.1 rigorously dictates this specific formulation using both individual and joint inclusion probabilities.</div>
            </div>

            <div class="question-box">
                <div class="question">15. The Sen-Midzuno method consists of selecting the very first unit with: <br> (सेन-मिदज़ुनो विधि में पहली इकाई का चयन किसके साथ किया जाता है?)</div>
                <ul class="mcq-options">
                    <li>a) Simple Random Sampling (SRS)</li>
                    <li>b) Probability Proportional to Size (PPS)</li>
                    <li>c) Lahiri's Method</li>
                    <li>d) Cumulative Totals</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq15')">Show/Hide Answer</button>
                <div id="mcq15" class="answer"><strong>Correct Answer:</strong> b) Probability Proportional to Size (PPS) <br> <em>Explanation:</em> The method consists definitively in safely selecting the very first unit explicitly with pps and the remaining \( (n - 1) \) units by precise simple random sampling.</div>
            </div>

            <div class="question-box">
                <div class="question">16. The inclusion probability of the \( i \)-th unit in the Sen-Midzuno method is: <br> (सेन-मिदज़ुनो विधि में \( i \)-वीं इकाई की समावेशन प्रायिकता है:)</div>
                <ul class="mcq-options">
                    <li>a) \( \pi_i = p_i + (1 - p_i) \frac{n - 1}{N - 1} \)</li>
                    <li>b) \( \pi_i = p_i \frac{n}{N} \)</li>
                    <li>c) \( \pi_i = n p_i \)</li>
                    <li>d) \( \pi_i = \frac{1}{N} \)</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq16')">Show/Hide Answer</button>
                <div id="mcq16" class="answer"><strong>Correct Answer:</strong> a) \( \pi_i = p_i + (1 - p_i) \frac{n - 1}{N - 1} \) <br> <em>Explanation:</em> The unit can be selected at the first draw with probability \( p_i \), or if not selected (\( 1-p_i \)), it can be selected in the subsequent \( n-1 \) simple random draws.</div>
            </div>

            <div class="question-box">
                <div class="question">17. The Random Group Method estimator \( \widehat{Y}_{RHC} \) variance reaches its minimum when: <br> (रैंडम ग्रुप मेथड अनुमानक \( \widehat{Y}_{RHC} \) का प्रसरण अपने न्यूनतम स्तर पर तब पहुँचता है जब:)</div>
                <ul class="mcq-options">
                    <li>a) \( N_1 \neq N_2 \neq N_n \)</li>
                    <li>b) \( N_1 = N_2 = \cdots = N_n = N/n \)</li>
                    <li>c) \( N_1 = N \)</li>
                    <li>d) \( N_n = 1 \)</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq17')">Show/Hide Answer</button>
                <div id="mcq17" class="answer"><strong>Correct Answer:</strong> b) \( N_1 = N_2 = \cdots = N_n = N/n \) <br> <em>Explanation:</em> Corollary 1 dictates that if the choice is that all random groups are of exactly equal size \( N/n \), the variance minimizes.</div>
            </div>

            <div class="question-box">
                <div class="question">18. In PPS systematic sampling, the units are first: <br> (PPS व्यवस्थित प्रतिचयन में, इकाइयों को सबसे पहले:)</div>
                <ul class="mcq-options">
                    <li>a) Stratified</li>
                    <li>b) Arranged at random</li>
                    <li>c) Sorted by size</li>
                    <li>d) Removed from the population</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq18')">Show/Hide Answer</button>
                <div id="mcq18" class="answer"><strong>Correct Answer:</strong> b) Arranged at random <br> <em>Explanation:</em> Madow's generalization requires the method to arrange the units at random and form cumulative totals before selecting a random start.</div>
            </div>

            <div class="question-box">
                <div class="question">19. In Des Raj's estimator, the variable \( z_2 \) safely incorporates: <br> (देस राज के अनुमानक में, चर \( z_2 \) सुरक्षित रूप से शामिल करता है:)</div>
                <ul class="mcq-options">
                    <li>a) The unconditional probability of the first draw</li>
                    <li>b) The exact specific conditional unbiased contribution definitively of strictly the exact second draw</li>
                    <li>c) The standard variance of the population</li>
                    <li>d) The median of the sample</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq19')">Show/Hide Answer</button>
                <div id="mcq19" class="answer"><strong>Correct Answer:</strong> b) The exact specific conditional unbiased contribution definitively of strictly the exact second draw <br> <em>Explanation:</em> \( z_2 \) incorporates the conditional probability \( p_j / (1-p_1) \) ensuring the second draw maintains unbiasedness in ordered extraction.</div>
            </div>

            <div class="question-box">
                <div class="question">20. The primary motivation for using PPS sampling without replacement over with replacement is: <br> (प्रतिस्थापन के साथ पीपीएस प्रतिचयन के बजाय प्रतिस्थापन के बिना उपयोग करने की प्राथमिक प्रेरणा क्या है?)</div>
                <ul class="mcq-options">
                    <li>a) It is computationally simpler</li>
                    <li>b) It generates a smaller effective sample size</li>
                    <li>c) It robustly provides a more efficient estimator due to a larger effective sample size</li>
                    <li>d) It allows for negative inclusion probabilities</li>
                </ul>
                <button class="toggle-btn" onclick="toggleAnswer('mcq20')">Show/Hide Answer</button>
                <div id="mcq20" class="answer"><strong>Correct Answer:</strong> c) It robustly provides a more efficient estimator due to a larger effective sample size <br> <em>Explanation:</em> Since the effective sample size strictly in the case of without replacement sampling is inherently mathematically larger, it robustly provides a more efficient estimator.</div>
            </div>

        </section>

        <section id="quiz-fib" class="section-card">
            <h2>✏️ Fill in the Blanks (रिक्त स्थान भरें)</h2>

            <div class="question-box">
                <div class="question">1. In pps sampling, the probability of selecting a unit is proportional to its ____________. <br> (pps प्रतिचयन में, किसी इकाई को चुनने की प्रायिकता उसके ____________ के समानुपाती होती है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib1')">Show/Hide Answer</button>
                <div id="fib1" class="answer"><strong>Answer:</strong> size (\( X_i \)) (आकार) <br> <em>Explanation:</em> The core defining feature is that probability is proportional to size, yielding \( p_i = X_i / X \).</div>
            </div>

            <div class="question-box">
                <div class="question">2. Lahiri's method strictly avoids the absolute compulsion to compute massive successive ____________. <br> (लाहिड़ी की विधि विशाल क्रमिक ____________ की गणना करने की पूर्ण मजबूरी से सख्ती से बचाती है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib2')">Show/Hide Answer</button>
                <div id="fib2" class="answer"><strong>Answer:</strong> cumulative totals (संचयी योग) <br> <em>Explanation:</em> Lahiri (1951) elegantly suggested an alternative procedure in which tedious mathematical cumulations are completely avoided.</div>
            </div>

            <div class="question-box">
                <div class="question">3. Estimators that rely strictly on the sequence in which units were selected are called ____________ estimators. <br> (अनुमानक जो सख्ती से उस क्रम पर निर्भर करते हैं जिसमें इकाइयों को चुना गया था, ____________ अनुमानक कहलाते हैं।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib3')">Show/Hide Answer</button>
                <div id="fib3" class="answer"><strong>Answer:</strong> ordered (क्रमबद्ध) <br> <em>Explanation:</em> These are mathematically based firmly on the specific true order securely of exact units safely selected (e.g., Des Raj's estimator).</div>
            </div>

            <div class="question-box">
                <div class="question">4. The Horvitz-Thompson estimator is a classic example of an ____________ estimator. <br> (हॉर्विट्ज़-थॉम्पसन अनुमानक एक ____________ अनुमानक का उत्कृष्ट उदाहरण है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib4')">Show/Hide Answer</button>
                <div id="fib4" class="answer"><strong>Answer:</strong> unordered (अक्रमबद्ध) <br> <em>Explanation:</em> It structurally does not depend cleanly on the true exact order explicitly in which the units were drawn.</div>
            </div>

            <div class="question-box">
                <div class="question">5. According to Murthy (1957), unordered estimators are rigorously more highly ____________ than ordered estimators. <br> (मूर्ति (1957) के अनुसार, अक्रमबद्ध अनुमानक क्रमबद्ध अनुमानकों की तुलना में अधिक ____________ हैं।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib5')">Show/Hide Answer</button>
                <div id="fib5" class="answer"><strong>Answer:</strong> efficient (कुशल) <br> <em>Explanation:</em> Murthy mathematically showed safely that these explicit estimators are rigorously more highly efficient.</div>
            </div>

            <div class="question-box">
                <div class="question">6. In simple random sampling, the mathematical probability of drawing any specified unit at any given draw is rigorously exactly the ____________. <br> (सरल यादृच्छिक प्रतिचयन में, किसी दिए गए ड्रा पर किसी भी निर्दिष्ट इकाई को निकालने की गणितीय प्रायिकता कठोरता से बिल्कुल ____________ होती है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib6')">Show/Hide Answer</button>
                <div id="fib6" class="answer"><strong>Answer:</strong> same (\( 1/N \)) (समान) <br> <em>Explanation:</em> Unlike PPS, simple random sampling does not vary probabilities from draw to draw.</div>
            </div>

            <div class="question-box">
                <div class="question">7. The joint probability of inclusion for units \( i \) and \( j \) in the Horvitz-Thompson estimator is denoted by ____________. <br> (हॉर्विट्ज़-थॉम्पसन अनुमानक में इकाइयों \( i \) और \( j \) के लिए समावेशन की संयुक्त प्रायिकता को ____________ द्वारा दर्शाया गया है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib7')">Show/Hide Answer</button>
                <div id="fib7" class="answer"><strong>Answer:</strong> \( \pi_{ij} \) <br> <em>Explanation:</em> \( \pi_{ij} \) represents the probability exactly safely successfully seamlessly completely correctly of safely carefully correctly cleanly inclusion of both the \( i \)-th and \( j \)-th units.</div>
            </div>

            <div class="question-box">
                <div class="question">8. In the Cumulative Total Method, the unit selected is the one whose associated range contains the drawn ____________ number. <br> (संचयी योग विधि में, चयनित इकाई वह होती है जिसकी संबंधित सीमा में खींचा गया ____________ नंबर होता है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib8')">Show/Hide Answer</button>
                <div id="fib8" class="answer"><strong>Answer:</strong> random (यादृच्छिक) <br> <em>Explanation:</em> A random number \( k \) is cleanly chosen from the range 1 to \( X \), and the unit associated with it is selected.</div>
            </div>

            <div class="question-box">
                <div class="question">9. Durbin's \( \pi \)ps sampling procedure is generally designed specifically for a sample size of exactly ____________. <br> (डर्बिन की \( \pi \)ps प्रतिचयन प्रक्रिया आम तौर पर विशेष रूप से बिल्कुल ____________ के नमूने के आकार के लिए डिज़ाइन की गई है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib9')">Show/Hide Answer</button>
                <div id="fib9" class="answer"><strong>Answer:</strong> 2 (दो) <br> <em>Explanation:</em> Most \( \pi \)ps sampling procedures in literature are strictly for sample size 2 alone.</div>
            </div>

            <div class="question-box">
                <div class="question">10. Under the Sen-Midzuno method, the subsequent \( (n-1) \) actual units are firmly selected using ____________ sampling. <br> (सेन-मिदज़ुनो विधि के तहत, बाद की \( (n-1) \) वास्तविक इकाइयों का दृढ़ता से ____________ प्रतिचयन का उपयोग करके चयन किया जाता है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib10')">Show/Hide Answer</button>
                <div id="fib10" class="answer"><strong>Answer:</strong> simple random (सरल यादृच्छिक) <br> <em>Explanation:</em> The first unit is selected PPS, and the rest are selected by precise simple random sampling, strictly wor.</div>
            </div>

            <div class="question-box">
                <div class="question">11. In Lahiri's Method, if the second random number \( j \) is strictly greater than \( X_i \), the selection is ____________. <br> (लाहिड़ी की विधि में, यदि दूसरा यादृच्छिक नंबर \( j \) सख्ती से \( X_i \) से अधिक है, तो चयन ____________ है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib11')">Show/Hide Answer</button>
                <div id="fib11" class="answer"><strong>Answer:</strong> rejected (अस्वीकार) <br> <em>Explanation:</em> If it exceeds the unit's size, the entire procedure is rejected and rigorously repeated.</div>
            </div>

            <div class="question-box">
                <div class="question">12. The mathematical variance of \( \widehat{Y}_{pps} \) is strictly ____________ proportional to the sample size \( n \). <br> (\( \widehat{Y}_{pps} \) का गणितीय प्रसरण सख्ती से नमूने के आकार \( n \) के ____________ अनुपाती है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib12')">Show/Hide Answer</button>
                <div id="fib12" class="answer"><strong>Answer:</strong> inversely (व्युत्क्रमानुपाती) <br> <em>Explanation:</em> The \( 1/n \) multiplier shows that variance strictly decreases as sample size indiscriminately increases.</div>
            </div>

            <div class="question-box">
                <div class="question">13. In Des Raj's estimator for \( n=2 \), the mathematical expectation \( E(z_2 | y_1) \) flawlessly equals ____________. <br> (\( n=2 \) के लिए देस राज के अनुमानक में, गणितीय अपेक्षा \( E(z_2 | y_1) \) निर्दोष रूप से ____________ के बराबर होती है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib13')">Show/Hide Answer</button>
                <div id="fib13" class="answer"><strong>Answer:</strong> \( Y \) <br> <em>Explanation:</em> The expected conditional value mathematically cancels correctly to equal the total population \( Y \).</div>
            </div>

            <div class="question-box">
                <div class="question">14. The Random Group Method is mathematically due to Rao, Hartley, and ____________. <br> (यादृच्छिक समूह विधि गणितीय रूप से राव, हार्टले और ____________ के कारण है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib14')">Show/Hide Answer</button>
                <div id="fib14" class="answer"><strong>Answer:</strong> Cochran (कोचरन) <br> <em>Explanation:</em> Rao, Hartley and Cochran (1962) suggested the procedure of varying probabilities by dividing into random groups.</div>
            </div>

            <div class="question-box">
                <div class="question">15. In PPS systematic sampling, the units must be arranged at ____________ before selection. <br> (PPS व्यवस्थित प्रतिचयन में, चयन से पहले इकाइयों को ____________ रूप से व्यवस्थित किया जाना चाहिए।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib15')">Show/Hide Answer</button>
                <div id="fib15" class="answer"><strong>Answer:</strong> random (यादृच्छिक) <br> <em>Explanation:</em> Madow's method consists of arranging the units at random and forming cumulative totals to avoid periodicity biases.</div>
            </div>

            <div class="question-box">
                <div class="question">16. The total sum of probabilities \( \sum_{i=1}^N p_i \) in PPS sampling is mathematically universally ____________. <br> (PPS प्रतिचयन में प्रायिकताओं का कुल योग \( \sum_{i=1}^N p_i \) गणितीय रूप से सार्वभौमिक रूप से ____________ होता है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib16')">Show/Hide Answer</button>
                <div id="fib16" class="answer"><strong>Answer:</strong> 1 (एक) <br> <em>Explanation:</em> This ensures the probabilities represent a complete valid distribution over the entire population space.</div>
            </div>

            <div class="question-box">
                <div class="question">17. In the random group method, to minimize variance, the group sizes \( N_i \) should be ideally ____________. <br> (यादृच्छिक समूह विधि में, प्रसरण को कम करने के लिए, समूह का आकार \( N_i \) आदर्श रूप से ____________ होना चाहिए।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib17')">Show/Hide Answer</button>
                <div id="fib17" class="answer"><strong>Answer:</strong> equal (समान) <br> <em>Explanation:</em> Variance minimizes when \( N_1 = N_2 = \cdots = N_n = N/n \).</div>
            </div>

            <div class="question-box">
                <div class="question">18. To calculate the gain due to PPS sampling over SRS directly, one estimates the percentage ____________. <br> (SRS पर PPS प्रतिचयन के कारण लाभ की सीधे गणना करने के लिए, कोई प्रतिशत ____________ का अनुमान लगाता है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib18')">Show/Hide Answer</button>
                <div id="fib18" class="answer"><strong>Answer:</strong> gain / efficiency (लाभ / दक्षता) <br> <em>Explanation:</em> Gain = \( [\widehat{v}_{pps}(\bar{y}_{SR}) - \widehat{v}(\bar{y}_{pps})] / \widehat{v}(\bar{y}_{pps}) \times 100 \).</div>
            </div>

            <div class="question-box">
                <div class="question">19. Murthy's Unordered Estimator is formed by ____________ all possible ordered estimators with their respective probabilities. <br> (मूर्ति का अक्रमबद्ध अनुमानक सभी संभावित क्रमबद्ध अनुमानकों को उनकी संबंधित प्रायिकताओं के साथ ____________ करके बनाया जाता है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib19')">Show/Hide Answer</button>
                <div id="fib19" class="answer"><strong>Answer:</strong> weighting (वजन देकर) <br> <em>Explanation:</em> It averages or weights all ordered sequences \( P(s_i|s) \) that could result in the exact same sample.</div>
            </div>

            <div class="question-box">
                <div class="question">20. Under Hanurav's scheme, if the two units selected are not distinct, the sample is firmly ____________. <br> (हनुराव की योजना के तहत, यदि चुनी गई दो इकाइयाँ विशिष्ट नहीं हैं, तो प्रतिदर्श दृढ़ता से ____________ है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('fib20')">Show/Hide Answer</button>
                <div id="fib20" class="answer"><strong>Answer:</strong> rejected (अस्वीकार) <br> <em>Explanation:</em> The procedure rejects duplicates and resamples to enforce without-replacement properties while maintaining \( \pi \)ps.</div>
            </div>

        </section>

        <section id="quiz-tf" class="section-card">
            <h2>✅ True or False (सही या गलत)</h2>

            <div class="question-box">
                <div class="question">1. Simple random sampling inherently operates as a special case of PPS sampling. <br> (सरल यादृच्छिक प्रतिचयन स्वाभाविक रूप से PPS प्रतिचयन के एक विशेष मामले के रूप में कार्य करता है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf1')">Show/Hide Answer</button>
                <div id="tf1" class="answer"><strong>Answer:</strong> True (सही) <br> <em>Explanation:</em> When \( p_i = 1/N \) for all units, PPS sampling mathematically devolves entirely into simple random sampling.</div>
            </div>

            <div class="question-box">
                <div class="question">2. The Cumulative Total Method is highly efficient and recommended for astronomically large populations. <br> (संचयी योग विधि अत्यधिक कुशल है और खगोलीय रूप से बड़ी आबादी के लिए अनुशंसित है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf2')">Show/Hide Answer</button>
                <div id="tf2" class="answer"><strong>Answer:</strong> False (गलत) <br> <em>Explanation:</em> The absolute compulsion to compute massive successive cumulative totals makes it computationally costly and difficult for very large populations.</div>
            </div>

            <div class="question-box">
                <div class="question">3. Lahiri's Method requires knowledge of the absolute maximum size \( M \) among all units in the population. <br> (लाहिड़ी की विधि के लिए जनसंख्या की सभी इकाइयों के बीच पूर्ण अधिकतम आकार \( M \) का ज्ञान आवश्यक है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf3')">Show/Hide Answer</button>
                <div id="tf3" class="answer"><strong>Answer:</strong> True (सही) <br> <em>Explanation:</em> A random number \( j \) is chosen between 1 and \( M \) to test whether to retain or reject the provisionally selected unit.</div>
            </div>

            <div class="question-box">
                <div class="question">4. In PPS sampling with replacement, the sample mean \( \bar{y}_{pps} \) is a biased estimator of the population mean \( \bar{Y} \). <br> (प्रतिस्थापन के साथ PPS प्रतिचयन में, प्रतिदर्श माध्य \( \bar{y}_{pps} \), जनसंख्या माध्य \( \bar{Y} \) का एक पक्षपाती अनुमानक है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf4')">Show/Hide Answer</button>
                <div id="tf4" class="answer"><strong>Answer:</strong> False (गलत) <br> <em>Explanation:</em> As shown in the Corollary to Theorem 5.3.1, \( \bar{y}_{pps} \) is mathematically an unbiased estimator.</div>
            </div>

            <div class="question-box">
                <div class="question">5. The Horvitz-Thompson estimator is an ordered estimator. <br> (हॉर्विट्ज़-थॉम्पसन अनुमानक एक क्रमबद्ध अनुमानक है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf5')">Show/Hide Answer</button>
                <div id="tf5" class="answer"><strong>Answer:</strong> False (गलत) <br> <em>Explanation:</em> It is an unordered estimator, relying only on inclusion probabilities \( \pi_i \) rather than the strict order of draws.</div>
            </div>

            <div class="question-box">
                <div class="question">6. Unordered estimators have been proven to be mathematically more highly efficient than ordered estimators. <br> (अक्रमबद्ध अनुमानकों को गणितीय रूप से क्रमबद्ध अनुमानकों की तुलना में अधिक कुशल सिद्ध किया गया है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf6')">Show/Hide Answer</button>
                <div id="tf6" class="answer"><strong>Answer:</strong> True (सही) <br> <em>Explanation:</em> Murthy (1957) and Basu (1958) demonstrated safely that ignoring the draw order reduces variance, making unordered estimators more precise.</div>
            </div>

            <div class="question-box">
                <div class="question">7. The variance of the sample means \( \bar{y}_{sy} \) in systematic sampling will always decrease if the sample size is indiscriminately increased. <br> (व्यवस्थित प्रतिचयन में प्रतिदर्श माध्य \( \bar{y}_{sy} \) का प्रसरण हमेशा कम हो जाएगा यदि प्रतिदर्श आकार को अंधाधुंध बढ़ाया जाता है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf7')">Show/Hide Answer</button>
                <div id="tf7" class="answer"><strong>Answer:</strong> False (गलत) <br> <em>Explanation:</em> It should absolutely not be inferred that variance continuously decreases, as systematic sampling is a delicate device heavily dependent on periodicity.</div>
            </div>

            <div class="question-box">
                <div class="question">8. In the Sen-Midzuno method, the second and subsequent units are selected with equal probability without replacement. <br> (सेन-मिदज़ुनो विधि में, दूसरी और बाद की इकाइयों को प्रतिस्थापन के बिना समान प्रायिकता के साथ चुना जाता है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf8')">Show/Hide Answer</button>
                <div id="tf8" class="answer"><strong>Answer:</strong> True (सही) <br> <em>Explanation:</em> Only the very first unit is selected with PPS; the remaining \( (n-1) \) units are selected strictly by simple random sampling (SRS) WOR.</div>
            </div>

            <div class="question-box">
                <div class="question">9. The Random Group Method eliminates the need for any PPS sampling. <br> (यादृच्छिक समूह विधि किसी भी PPS प्रतिचयन की आवश्यकता को समाप्त कर देती है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf9')">Show/Hide Answer</button>
                <div id="tf9" class="answer"><strong>Answer:</strong> False (गलत) <br> <em>Explanation:</em> It divides units into groups at random, but then explicitly requires selecting exactly one unit with PPS from each group.</div>
            </div>

            <div class="question-box">
                <div class="question">10. Durbin's \( \pi \)ps sampling procedure is mathematically practical mostly for a sample size of exactly 2. <br> (डर्बिन की \( \pi \)ps प्रतिचयन प्रक्रिया मुख्य रूप से बिल्कुल 2 के प्रतिदर्श आकार के लिए गणितीय रूप से व्यावहारिक है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf10')">Show/Hide Answer</button>
                <div id="tf10" class="answer"><strong>Answer:</strong> True (सही) <br> <em>Explanation:</em> For sample sizes greater than 2, the exact inclusion probability expressions involved become prohibitively complicated.</div>
            </div>

            <div class="question-box">
                <div class="question">11. A serious disadvantage of systematic sampling is its vulnerability to unforeseen periodicities. <br> (व्यवस्थित प्रतिचयन का एक गंभीर नुकसान अप्रत्याशित आवधिकताओं के प्रति इसकी भेद्यता है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf11')">Show/Hide Answer</button>
                <div id="tf11" class="answer"><strong>Answer:</strong> True (सही) <br> <em>Explanation:</em> If the sampling interval coincides with a periodic cycle, it can contribute a devastating bias to the estimate.</div>
            </div>

            <div class="question-box">
                <div class="question">12. Des Raj's estimator requires the calculation of exact joint inclusion probabilities \( \pi_{ij} \). <br> (देस राज के अनुमानक के लिए सटीक संयुक्त समावेशन प्रायिकताओं \( \pi_{ij} \) की गणना की आवश्यकता होती है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf12')">Show/Hide Answer</button>
                <div id="tf12" class="answer"><strong>Answer:</strong> False (गलत) <br> <em>Explanation:</em> It makes flawless use of sequential conditional specific probabilities, explicitly bypassing the need to calculate complex \( \pi_{ij} \).</div>
            </div>

            <div class="question-box">
                <div class="question">13. In Narain's Scheme, \( \pi_i \) is forced to be strictly equal to \( n \times p_i \). <br> (नारायण की योजना में, \( \pi_i \) को कड़ाई से \( n \times p_i \) के बराबर होने के लिए बाध्य किया जाता है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf13')">Show/Hide Answer</button>
                <div id="tf13" class="answer"><strong>Answer:</strong> True (सही) <br> <em>Explanation:</em> The scheme explicitly constructs revised distinct probabilities \( p_i' \) to ensure \( \pi_i = n p_i \).</div>
            </div>

            <div class="question-box">
                <div class="question">14. If the variable under study is highly correlated with the size of the unit, equal probability sampling is the best method. <br> (यदि अध्ययन के तहत चर इकाई के आकार के साथ अत्यधिक सहसंबद्ध है, तो समान प्रायिकता प्रतिचयन सबसे अच्छी विधि है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf14')">Show/Hide Answer</button>
                <div id="tf14" class="answer"><strong>Answer:</strong> False (गलत) <br> <em>Explanation:</em> In such cases, probability proportional to size (PPS) sampling is overwhelmingly preferred to increase efficiency.</div>
            </div>

            <div class="question-box">
                <div class="question">15. In Lahiri's method, the number of random number pairs drawn will exactly equal the desired sample size \( n \). <br> (लाहिड़ी की विधि में, खींचे गए यादृच्छिक संख्या युग्मों की संख्या बिल्कुल वांछित प्रतिदर्श आकार \( n \) के बराबर होगी।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf15')">Show/Hide Answer</button>
                <div id="tf15" class="answer"><strong>Answer:</strong> False (गलत) <br> <em>Explanation:</em> Because some pairs may be rejected if \( j > X_i \), the total number of draws usually exceeds \( n \) until exactly \( n \) units are secured.</div>
            </div>

            <div class="question-box">
                <div class="question">16. The variance of the PPS estimator decreases as within-sample variation \( \sigma_w^2 \) increases. <br> (PPS अनुमानक का प्रसरण घटता है क्योंकि प्रतिदर्श के भीतर भिन्नता \( \sigma_w^2 \) बढ़ती है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf16')">Show/Hide Answer</button>
                <div id="tf16" class="answer"><strong>Answer:</strong> True (सही) <br> <em>Explanation:</em> As shown in the derivation \( \sigma^2 - \sigma_w^2 \), since \( \sigma^2 \) is fixed, mathematically increasing \( \sigma_w^2 \) directly reduces the overall variance.</div>
            </div>

            <div class="question-box">
                <div class="question">17. PPS sampling with replacement ensures that no unit can be selected more than once. <br> (प्रतिस्थापन के साथ PPS प्रतिचयन यह सुनिश्चित करता है कि किसी भी इकाई को एक से अधिक बार नहीं चुना जा सकता है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf17')">Show/Hide Answer</button>
                <div id="tf17" class="answer"><strong>Answer:</strong> False (गलत) <br> <em>Explanation:</em> Sampling *with replacement* (wr) inherently allows units to be selected multiple times.</div>
            </div>

            <div class="question-box">
                <div class="question">18. The relative precision of systematic sampling over simple random sampling depends heavily on the intra-class correlation coefficient. <br> (सरल यादृच्छिक प्रतिचयन पर व्यवस्थित प्रतिचयन की सापेक्ष सटीकता काफी हद तक अंतर-वर्ग सहसंबंध गुणांक पर निर्भर करती है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf18')">Show/Hide Answer</button>
                <div id="tf18" class="answer"><strong>Answer:</strong> True (सही) <br> <em>Explanation:</em> As mathematically derived in relation (4.5.3), relative precision depends directly on the true value of \( \rho_w \).</div>
            </div>

            <div class="question-box">
                <div class="question">19. In Des Raj's estimator, \( E(\widehat{Y}_D) \) mathematically evaluates to zero. <br> (देस राज के अनुमानक में, \( E(\widehat{Y}_D) \) का गणितीय मूल्यांकन शून्य होता है।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf19')">Show/Hide Answer</button>
                <div id="tf19" class="answer"><strong>Answer:</strong> False (गलत) <br> <em>Explanation:</em> It evaluates precisely to \( Y \), proving it is a completely unbiased estimator.</div>
            </div>

            <div class="question-box">
                <div class="question">20. Horvitz-Thompson estimators are only applicable to ordered sampling structures. <br> (हॉर्विट्ज़-थॉम्पसन अनुमानक केवल क्रमबद्ध प्रतिचयन संरचनाओं पर लागू होते हैं।)</div>
                <button class="toggle-btn" onclick="toggleAnswer('tf20')">Show/Hide Answer</button>
                <div id="tf20" class="answer"><strong>Answer:</strong> False (गलत) <br> <em>Explanation:</em> They are explicitly the primary example of an unordered estimator, depending solely on the set of elements in the sample, not their draw order.</div>
            </div>

        </section>
        
        <script>"""
html = html + quizzes_content

with open("Chapter5.html", "w", encoding="utf-8") as f:
    f.write(html)
