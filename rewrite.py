import re

with open('Stat-101/Unit-IV.html', 'r', encoding='utf-8') as f:
    content = f.read()

english_content = """    <div class="english-content">
      <h2><span class="section-num">📝</span> Subjective Questions (Data Based)</h2>
      
      <div class="question"><strong>Q1.</strong> Prove that \\(\\beta_2 \\ge \\beta_1 + 1\\) for any frequency distribution.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-1')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-1">
        <p><strong>Solution:</strong> This is a standard property of moments. It can be proved using the variance of a quadratic function or the Cauchy-Schwarz inequality. The variance of \\( (X - \\bar{x})^2 + c(X - \\bar{x}) \\) is always non-negative, which ultimately reduces to:</p>
        \\[ \\begin{aligned} \\mu_4 \\mu_2 - \\mu_3^2 - \\mu_2^3 &\\ge 0 \\\\ \\frac{\\mu_4 \\mu_2}{\\mu_2^3} - \\frac{\\mu_3^2}{\\mu_2^3} - \\frac{\\mu_2^3}{\\mu_2^3} &\\ge 0 \\\\ \\beta_2 - \\beta_1 - 1 &\\ge 0 \\\\ \\beta_2 &\\ge \\beta_1 + 1 \\end{aligned} \\]
        <p>∎</p>
      </div>

      <div class="question"><strong>Q2.</strong> Prove the relationship between Yule's Coefficient of Association (Q) and Coefficient of Colligation (Y): \\(Q = \\frac{2Y}{1+Y^2}\\).</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-2')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-2">
        <p><strong>Solution:</strong> Let \\(p = \\sqrt{(AB)(\\alpha\\beta)}\\) and \\(q = \\sqrt{(A\\beta)(\\alpha B)}\\). Then \\(Y = \\frac{p-q}{p+q}\\) and \\(Q = \\frac{p^2-q^2}{p^2+q^2}\\). Expanding \\(\\frac{2Y}{1+Y^2}\\) by substituting Y:</p>
        \\[ \\begin{aligned} \\frac{2Y}{1+Y^2} &= \\frac{2\\left(\\frac{p-q}{p+q}\\right)}{1+\\left(\\frac{p-q}{p+q}\\right)^2} \\\\ &= \\frac{\\frac{2(p-q)}{p+q}}{\\frac{(p+q)^2+(p-q)^2}{(p+q)^2}} \\\\ &= \\frac{2(p-q)(p+q)}{(p+q)^2+(p-q)^2} \\\\ &= \\frac{2(p^2-q^2)}{2(p^2+q^2)} \\\\ &= Q \\end{aligned} \\]
        <p>∎</p>
      </div>

      <div class="question"><strong>Q3.</strong> For a distribution, the Mean is 50, Median is 48, and Standard Deviation is 10. Calculate Karl Pearson's coefficient of skewness.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-3')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-3">
        <p><strong>Solution:</strong></p>
        \\[ \\begin{aligned} S_k &= \\frac{3(\\text{Mean} - \\text{Median})}{\\sigma} \\\\ &= \\frac{3(50 - 48)}{10} \\\\ &= \\frac{6}{10} \\\\ &= +0.6 \\end{aligned} \\]
        <p>The distribution is positively skewed.</p>
      </div>

      <div class="question"><strong>Q4.</strong> The quartiles of a dataset are Q₁=30, Q₂=45, and Q₃=70. Calculate Bowley's coefficient of skewness.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-4')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-4">
        <p><strong>Solution:</strong></p>
        \\[ \\begin{aligned} S_Q &= \\frac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1} \\\\ &= \\frac{70 + 30 - 2(45)}{70 - 30} \\\\ &= \\frac{100 - 90}{40} \\\\ &= +0.25 \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q5.</strong> Given the first four central moments: μ₁=0, μ₂=16, μ₃=−64, μ₄=162. Calculate β₁ and β₂ and comment on the shape of the distribution.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-5')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-5">
        <p><strong>Solution:</strong></p>
        \\[ \\begin{aligned} \\beta_1 &= \\frac{\\mu_3^2}{\\mu_2^3} = \\frac{(-64)^2}{16^3} = \\frac{4096}{4096} = 1 \\end{aligned} \\]
        <p>Since \\(\\mu_3\\) is negative, the curve is negatively skewed.</p>
        \\[ \\begin{aligned} \\beta_2 &= \\frac{\\mu_4}{\\mu_2^2} = \\frac{162}{16^2} = \\frac{162}{256} \\approx 0.633 \\end{aligned} \\]
        <p>Since \\(\\beta_2 < 3\\), it is Platykurtic.</p>
      </div>

      <div class="question"><strong>Q6.</strong> In a population of N=500, we have (A)=300, (B)=250, and (AB)=150. Find the remaining ultimate class frequencies.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-6')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-6">
        <p><strong>Solution:</strong></p>
        \\[ \\begin{aligned} (A\\beta) &= (A) - (AB) = 300 - 150 = 150 \\\\ (\\alpha B) &= (B) - (AB) = 250 - 150 = 100 \\\\ (\\alpha\\beta) &= N - (A) - (B) + (AB) = 500 - 300 - 250 + 150 = 100 \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q7.</strong> Check the consistency of the following data: N=1000, (A)=600, (B)=500, (AB)=50.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-7')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-7">
        <p><strong>Solution:</strong> Check the ultimate class \\((\\alpha\\beta)\\):</p>
        \\[ \\begin{aligned} (\\alpha\\beta) &= N - (A) - (B) + (AB) \\\\ &= 1000 - 600 - 500 + 50 \\\\ &= -50 \\end{aligned} \\]
        <p>Since a frequency cannot be negative, the data is inconsistent.</p>
      </div>

      <div class="question"><strong>Q8.</strong> For N=400, (A)=250, (B)=150, (AB)=100. Calculate Yule's coefficient of association (Q).</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-8')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-8">
        <p><strong>Solution:</strong> First find the ultimate frequencies:</p>
        \\[ \\begin{aligned} (A\\beta) &= 250 - 100 = 150 \\\\ (\\alpha B) &= 150 - 100 = 50 \\\\ (\\alpha\\beta) &= 400 - 250 - 150 + 100 = 100 \\end{aligned} \\]
        \\[ \\begin{aligned} Q &= \\frac{(AB)(\\alpha\\beta) - (A\\beta)(\\alpha B)}{(AB)(\\alpha\\beta) + (A\\beta)(\\alpha B)} \\\\ &= \\frac{100(100) - 150(50)}{100(100) + 150(50)} \\\\ &= \\frac{10000 - 7500}{10000 + 7500} \\\\ &= +0.143 \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q9.</strong> Find Yule's Y for the data in Q8 and verify the relation \\(Q = \\frac{2Y}{1+Y^2}\\).</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-9')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-9">
        <p><strong>Solution:</strong> Let \\(p = \\sqrt{(AB)(\\alpha\\beta)}\\) and \\(q = \\sqrt{(A\\beta)(\\alpha B)}\\):</p>
        \\[ \\begin{aligned} p &= \\sqrt{10000} = 100 \\\\ q &= \\sqrt{7500} \\approx 86.60 \\\\ Y &= \\frac{p-q}{p+q} = \\frac{100 - 86.60}{100 + 86.60} \\approx 0.0718 \\end{aligned} \\]
        <p>Verification:</p>
        \\[ \\begin{aligned} \\frac{2Y}{1 + Y^2} &= \\frac{2(0.0718)}{1 + (0.0718)^2} \\\\ &\\approx \\frac{0.1436}{1.00515} \\\\ &\\approx 0.143 \\\\ &= Q \\quad \\text{✓} \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q10.</strong> In a survey of 200 farms, 120 use fertiliser (A) and 100 have high yield (B). If 80 farms use fertiliser and have high yield, test the association.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-10')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-10">
        <p><strong>Solution:</strong></p>
        \\[ \\begin{aligned} E(AB) &= \\frac{(A) \\times (B)}{N} \\\\ &= \\frac{120 \\times 100}{200} \\\\ &= 60 \\end{aligned} \\]
        <p>Observed (AB) = 80. Since Observed > Expected, there is a positive association.</p>
      </div>

      <div class="question"><strong>Q11.</strong> Calculate Karl Pearson's coefficient of skewness for the following frequency distribution:
        <div class="freq-table-wrap">
          <table class="freq-table">
            <thead><tr><th>X</th><th>10–20</th><th>20–30</th><th>30–40</th><th>40–50</th><th>50–60</th></tr></thead>
            <tbody><tr><td>f</td><td>5</td><td>12</td><td>20</td><td>10</td><td>3</td></tr></tbody>
          </table>
        </div>
      </div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-11')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-11">
        <p><strong>Solution:</strong> By preparing a calculation table, we get Mean = 33.8, Mode = 34.44, and Standard Deviation (\\(\\sigma\\)) ≈ 10.4.</p>
        \\[ \\begin{aligned} S_k &= \\frac{\\text{Mean} - \\text{Mode}}{\\sigma} \\\\ &= \\frac{33.8 - 34.44}{10.4} \\\\ &= -0.061 \\end{aligned} \\]
        <p>The distribution is slightly negatively skewed.</p>
      </div>

      <div class="question"><strong>Q12.</strong> Calculate Bowley's coefficient of skewness for the data:
        <div class="freq-table-wrap">
          <table class="freq-table">
            <thead><tr><th>Income (₹000)</th><th>Below 10</th><th>10–20</th><th>20–30</th><th>30–40</th><th>40–50</th><th>Above 50</th></tr></thead>
            <tbody><tr><td>No. of families</td><td>5</td><td>15</td><td>25</td><td>30</td><td>15</td><td>10</td></tr></tbody>
          </table>
        </div>
      </div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-12')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-12">
        <p><strong>Solution:</strong> \\(N = 100\\).</p>
        \\[ \\begin{aligned} Q_1 \\text{ (item 25)} &\\in 10\\text{--}20 \\rightarrow Q_1 = 10 + \\frac{25-5}{15} \\times 10 = 23.33 \\\\ Q_2 \\text{ (item 50)} &\\in 20\\text{--}30 \\rightarrow Q_2 = 20 + \\frac{50-20}{25} \\times 10 = 32 \\\\ Q_3 \\text{ (item 75)} &\\in 30\\text{--}40 \\rightarrow Q_3 = 30 + \\frac{75-45}{30} \\times 10 = 40 \\\\ S_Q &= \\frac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1} \\\\ &= \\frac{40 + 23.33 - 2(32)}{40 - 23.33} \\\\ &= \\frac{-0.67}{16.67} \\\\ &\\approx -0.04 \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q13.</strong> Find the first four central moments and coefficient of kurtosis (\\(\\beta_2\\)) for the values: 2, 4, 6, 8, 10.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-13')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-13">
        <p><strong>Solution:</strong> Mean = 6. Deviations \\((x - \\bar{x})\\): -4, -2, 0, 2, 4.</p>
        \\[ \\begin{aligned} \\mu_1 &= 0 \\\\ \\mu_2 &= \\frac{16+4+0+4+16}{5} = 8 \\\\ \\mu_3 &= 0 \\\\ \\mu_4 &= \\frac{256+16+0+16+256}{5} = 108.8 \\\\ \\beta_2 &= \\frac{\\mu_4}{\\mu_2^2} = \\frac{108.8}{64} = 1.7 \\end{aligned} \\]
        <p>Since \\(\\beta_2 < 3\\), it is platykurtic.</p>
      </div>

      <div class="question"><strong>Q14.</strong> From the following contingency table, calculate Yule's coefficient of association (Q) between Eye color of fathers and sons:
        <div class="freq-table-wrap">
          <table class="cont-table">
            <thead><tr><th>Fathers \\ Sons</th><th>Light Eyes</th><th>Dark Eyes</th></tr></thead>
            <tbody>
              <tr><td><strong>Light Eyes</strong></td><td>400</td><td>50</td></tr>
              <tr><td><strong>Dark Eyes</strong></td><td>80</td><td>470</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-14')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-14">
        <p><strong>Solution:</strong> Let \\((AB) = 400\\), \\((A\\beta) = 50\\), \\((\\alpha B) = 80\\), \\((\\alpha\\beta) = 470\\).</p>
        \\[ \\begin{aligned} Q &= \\frac{(AB)(\\alpha\\beta) - (A\\beta)(\\alpha B)}{(AB)(\\alpha\\beta) + (A\\beta)(\\alpha B)} \\\\ &= \\frac{400 \\times 470 - 50 \\times 80}{400 \\times 470 + 50 \\times 80} \\\\ &= \\frac{188000 - 4000}{188000 + 4000} \\\\ &= \\frac{184000}{192000} \\\\ &\\approx +0.958 \\end{aligned} \\]
        <p>High positive association.</p>
      </div>

      <div class="question"><strong>Q15.</strong> Calculate Yule's Coefficient of Colligation (Y) for the following treatment data:
        <div class="freq-table-wrap">
          <table class="cont-table">
            <thead><tr><th></th><th>Recovered</th><th>Not Recovered</th></tr></thead>
            <tbody>
              <tr><td><strong>Treated</strong></td><td>200</td><td>50</td></tr>
              <tr><td><strong>Not Treated</strong></td><td>100</td><td>150</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-15')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-15">
        <p><strong>Solution:</strong> \\((AB)=200\\), \\((A\\beta)=50\\), \\((\\alpha B)=100\\), \\((\\alpha\\beta)=150\\).</p>
        \\[ \\begin{aligned} p &= \\sqrt{200 \\times 150} = \\sqrt{30000} \\approx 173.2 \\\\ q &= \\sqrt{50 \\times 100} = \\sqrt{5000} \\approx 70.7 \\\\ Y &= \\frac{p - q}{p + q} \\\\ &= \\frac{173.2 - 70.7}{173.2 + 70.7} \\\\ &= \\frac{102.5}{243.9} \\\\ &\\approx +0.42 \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q16.</strong> Examine the consistency of the data: N = 1000, (A) = 500, (B) = 400, (A\\(\\beta\\)) = 200.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-16')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-16">
        <p><strong>Solution:</strong> We need to check if any ultimate class frequency is negative.</p>
        \\[ \\begin{aligned} (AB) &= (A) - (A\\beta) = 500 - 200 = 300 \\\\ (\\alpha B) &= (B) - (AB) = 400 - 300 = 100 \\\\ (\\alpha\\beta) &= N - (A) - (\\alpha B) = 1000 - 500 - 100 = 400 \\end{aligned} \\]
        <p>All ultimate frequencies (300, 200, 100, 400) are \\(\\ge 0\\). The data is consistent.</p>
      </div>

      <div class="question"><strong>Q17.</strong> Given the first two raw moments about the origin are 5 and 35. Find the variance and standard deviation.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-17')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-17">
        <p><strong>Solution:</strong> \\(\\mu'_1 = 5\\), \\(\\mu'_2 = 35\\).</p>
        \\[ \\begin{aligned} \\text{Variance } (\\mu_2) &= \\mu'_2 - (\\mu'_1)^2 \\\\ &= 35 - 5^2 \\\\ &= 35 - 25 \\\\ &= 10 \\\\ \\text{Standard Deviation} &= \\sqrt{10} \\approx 3.16 \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q18.</strong> A frequency distribution gives \\(P_{10} = 15\\), \\(P_{50} = 35\\), \\(P_{90} = 65\\). Find Kelly's Coefficient of Skewness.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-18')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-18">
        <p><strong>Solution:</strong></p>
        \\[ \\begin{aligned} S_P &= \\frac{P_{90} + P_{10} - 2P_{50}}{P_{90} - P_{10}} \\\\ &= \\frac{65 + 15 - 2(35)}{65 - 15} \\\\ &= \\frac{80 - 70}{50} \\\\ &= +0.20 \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q19.</strong> Calculate expected frequency of (AB) and determine the type of association if: N = 200, (A) = 100, (B) = 50, and Observed (AB) = 20.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-19')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-19">
        <p><strong>Solution:</strong></p>
        \\[ \\begin{aligned} E(AB) &= \\frac{(A)(B)}{N} \\\\ &= \\frac{100 \\times 50}{200} \\\\ &= 25 \\end{aligned} \\]
        <p>Since Observed (AB) = 20 is less than Expected (25), there is a negative association between A and B.</p>
      </div>

      <div class="question"><strong>Q20.</strong> If \\((A) = (\\alpha) = (B) = (\\beta) = \\frac{N}{2}\\), prove that the maximum value of \\((AB)\\) is \\(\\frac{N}{2}\\) and minimum is 0 for consistency.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-eng-20')">Show Answer ▼</button>
      <div class="answer" id="subj-eng-20">
        <p><strong>Solution:</strong> Consistency requires \\(\\max(0, (A)+(B)-N) \\le (AB) \\le \\min((A), (B))\\).</p>
        <p>Substituting \\(A = N/2\\) and \\(B = N/2\\):</p>
        \\[ \\begin{aligned} \\max\\left(0, \\frac{N}{2}+\\frac{N}{2}-N\\right) &\\le (AB) \\le \\min\\left(\\frac{N}{2}, \\frac{N}{2}\\right) \\\\ \\max(0, 0) &\\le (AB) \\le \\frac{N}{2} \\\\ 0 &\\le (AB) \\le \\frac{N}{2} \\end{aligned} \\]
        <p>∎</p>
      </div>
    </div>"""

hinglish_content = """    <div class="hinglish-content" style="display:none;">
      <h2><span class="section-num">📝</span> Subjective Questions (Data Based)</h2>
      
      <div class="question"><strong>Q1.</strong> Prove करें कि किसी भी frequency distribution के लिए \\(\\beta_2 \\ge \\beta_1 + 1\\) होता है।</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-1')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-1">
        <p><strong>Solution:</strong> यह moments की एक standard property है जिसे Cauchy-Schwarz inequality या quadratic function के variance द्वारा prove किया जा सकता है। \\( (X - \\bar{x})^2 + c(X - \\bar{x}) \\) का variance हमेशा non-negative होता है, जो ultimately इस प्रकार है:</p>
        \\[ \\begin{aligned} \\mu_4 \\mu_2 - \\mu_3^2 - \\mu_2^3 &\\ge 0 \\\\ \\frac{\\mu_4 \\mu_2}{\\mu_2^3} - \\frac{\\mu_3^2}{\\mu_2^3} - \\frac{\\mu_2^3}{\\mu_2^3} &\\ge 0 \\\\ \\beta_2 - \\beta_1 - 1 &\\ge 0 \\\\ \\beta_2 &\\ge \\beta_1 + 1 \\end{aligned} \\]
        <p>∎</p>
      </div>

      <div class="question"><strong>Q2.</strong> Yule's Q और Y के बीच relationship prove करें: \\(Q = \\frac{2Y}{1+Y^2}\\)।</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-2')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-2">
        <p><strong>Solution:</strong> मान लें \\(p = \\sqrt{(AB)(\\alpha\\beta)}\\) और \\(q = \\sqrt{(A\\beta)(\\alpha B)}\\)। तब \\(Y = \\frac{p-q}{p+q}\\) और \\(Q = \\frac{p^2-q^2}{p^2+q^2}\\)। \\(\\frac{2Y}{1+Y^2}\\) को Y substitute करके expand करें:</p>
        \\[ \\begin{aligned} \\frac{2Y}{1+Y^2} &= \\frac{2\\left(\\frac{p-q}{p+q}\\right)}{1+\\left(\\frac{p-q}{p+q}\\right)^2} \\\\ &= \\frac{\\frac{2(p-q)}{p+q}}{\\frac{(p+q)^2+(p-q)^2}{(p+q)^2}} \\\\ &= \\frac{2(p-q)(p+q)}{(p+q)^2+(p-q)^2} \\\\ &= \\frac{2(p^2-q^2)}{2(p^2+q^2)} \\\\ &= Q \\end{aligned} \\]
        <p>∎</p>
      </div>

      <div class="question"><strong>Q3.</strong> Mean = 50, Median = 48, σ = 10. Karl Pearson's coefficient of skewness निकालें।</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-3')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-3">
        <p><strong>Solution:</strong></p>
        \\[ \\begin{aligned} S_k &= \\frac{3(\\text{Mean} - \\text{Median})}{\\sigma} \\\\ &= \\frac{3(50 - 48)}{10} \\\\ &= \\frac{6}{10} \\\\ &= +0.6 \\end{aligned} \\]
        <p>Distribution positively skewed है।</p>
      </div>

      <div class="question"><strong>Q4.</strong> Quartiles Q₁=30, Q₂=45, Q₃=70 दिए गए हैं। Bowley's coefficient निकालें।</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-4')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-4">
        <p><strong>Solution:</strong></p>
        \\[ \\begin{aligned} S_Q &= \\frac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1} \\\\ &= \\frac{70 + 30 - 2(45)}{70 - 30} \\\\ &= \\frac{100 - 90}{40} \\\\ &= +0.25 \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q5.</strong> μ₁=0, μ₂=16, μ₃=−64, μ₄=162. β₁ और β₂ निकालें और shape बताएं।</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-5')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-5">
        <p><strong>Solution:</strong></p>
        \\[ \\begin{aligned} \\beta_1 &= \\frac{\\mu_3^2}{\\mu_2^3} = \\frac{(-64)^2}{16^3} = \\frac{4096}{4096} = 1 \\end{aligned} \\]
        <p>चूँकि \\(\\mu_3\\) negative है, curve negatively skewed है।</p>
        \\[ \\begin{aligned} \\beta_2 &= \\frac{\\mu_4}{\\mu_2^2} = \\frac{162}{16^2} = \\frac{162}{256} \\approx 0.633 \\end{aligned} \\]
        <p>चूँकि \\(\\beta_2 < 3\\), यह Platykurtic है।</p>
      </div>

      <div class="question"><strong>Q6.</strong> N=500, (A)=300, (B)=250, (AB)=150. बची हुई frequencies निकालें।</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-6')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-6">
        <p><strong>Solution:</strong></p>
        \\[ \\begin{aligned} (A\\beta) &= (A) - (AB) = 300 - 150 = 150 \\\\ (\\alpha B) &= (B) - (AB) = 250 - 150 = 100 \\\\ (\\alpha\\beta) &= N - (A) - (B) + (AB) = 500 - 300 - 250 + 150 = 100 \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q7.</strong> Consistency check करें: N=1000, (A)=600, (B)=500, (AB)=50.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-7')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-7">
        <p><strong>Solution:</strong> Ultimate class \\((\\alpha\\beta)\\) check करें:</p>
        \\[ \\begin{aligned} (\\alpha\\beta) &= N - (A) - (B) + (AB) \\\\ &= 1000 - 600 - 500 + 50 \\\\ &= -50 \\end{aligned} \\]
        <p>Negative frequency impossible है, इसलिए data inconsistent है।</p>
      </div>

      <div class="question"><strong>Q8.</strong> N=400, (A)=250, (B)=150, (AB)=100. Yule's Q निकालें।</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-8')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-8">
        <p><strong>Solution:</strong> पहले ultimate frequencies निकालें:</p>
        \\[ \\begin{aligned} (A\\beta) &= 250 - 100 = 150 \\\\ (\\alpha B) &= 150 - 100 = 50 \\\\ (\\alpha\\beta) &= 400 - 250 - 150 + 100 = 100 \\end{aligned} \\]
        \\[ \\begin{aligned} Q &= \\frac{(AB)(\\alpha\\beta) - (A\\beta)(\\alpha B)}{(AB)(\\alpha\\beta) + (A\\beta)(\\alpha B)} \\\\ &= \\frac{100(100) - 150(50)}{100(100) + 150(50)} \\\\ &= \\frac{10000 - 7500}{10000 + 7500} \\\\ &= +0.143 \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q9.</strong> Q8 के data से Y निकालें और verify करें।</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-9')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-9">
        <p><strong>Solution:</strong> मान लें \\(p = \\sqrt{(AB)(\\alpha\\beta)}\\) और \\(q = \\sqrt{(A\\beta)(\\alpha B)}\\):</p>
        \\[ \\begin{aligned} p &= \\sqrt{10000} = 100 \\\\ q &= \\sqrt{7500} \\approx 86.60 \\\\ Y &= \\frac{p-q}{p+q} = \\frac{100 - 86.60}{100 + 86.60} \\approx 0.0718 \\end{aligned} \\]
        <p>Verification:</p>
        \\[ \\begin{aligned} \\frac{2Y}{1 + Y^2} &= \\frac{2(0.0718)}{1 + (0.0718)^2} \\\\ &\\approx \\frac{0.1436}{1.00515} \\\\ &\\approx 0.143 \\\\ &= Q \\quad \\text{✓} \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q10.</strong> 200 farms के survey में, 120 fertiliser (A) use करते हैं, 100 की high yield (B) है। (AB)=80 है तो association test करें।</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-10')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-10">
        <p><strong>Solution:</strong></p>
        \\[ \\begin{aligned} E(AB) &= \\frac{(A) \\times (B)}{N} \\\\ &= \\frac{120 \\times 100}{200} \\\\ &= 60 \\end{aligned} \\]
        <p>Observed 80 > Expected 60, इसलिए Positive association है।</p>
      </div>

      <div class="question"><strong>Q11.</strong> निम्नलिखित frequency distribution के लिए Karl Pearson's coefficient of skewness निकालें:
        <div class="freq-table-wrap">
          <table class="freq-table">
            <thead><tr><th>X</th><th>10–20</th><th>20–30</th><th>30–40</th><th>40–50</th><th>50–60</th></tr></thead>
            <tbody><tr><td>f</td><td>5</td><td>12</td><td>20</td><td>10</td><td>3</td></tr></tbody>
          </table>
        </div>
      </div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-11')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-11">
        <p><strong>Solution:</strong> Calculation table से: Mean = 33.8, Mode = 34.44, Standard Deviation (\\(\\sigma\\)) ≈ 10.4.</p>
        \\[ \\begin{aligned} S_k &= \\frac{\\text{Mean} - \\text{Mode}}{\\sigma} \\\\ &= \\frac{33.8 - 34.44}{10.4} \\\\ &= -0.061 \\end{aligned} \\]
        <p>Distribution slightly negatively skewed है।</p>
      </div>

      <div class="question"><strong>Q12.</strong> दिए गए data के लिए Bowley's coefficient of skewness निकालें:
        <div class="freq-table-wrap">
          <table class="freq-table">
            <thead><tr><th>Income (₹000)</th><th>Below 10</th><th>10–20</th><th>20–30</th><th>30–40</th><th>40–50</th><th>Above 50</th></tr></thead>
            <tbody><tr><td>No. of families</td><td>5</td><td>15</td><td>25</td><td>30</td><td>15</td><td>10</td></tr></tbody>
          </table>
        </div>
      </div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-12')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-12">
        <p><strong>Solution:</strong> \\(N = 100\\).</p>
        \\[ \\begin{aligned} Q_1 \\text{ (item 25)} &\\in 10\\text{--}20 \\rightarrow Q_1 = 10 + \\frac{25-5}{15} \\times 10 = 23.33 \\\\ Q_2 \\text{ (item 50)} &\\in 20\\text{--}30 \\rightarrow Q_2 = 20 + \\frac{50-20}{25} \\times 10 = 32 \\\\ Q_3 \\text{ (item 75)} &\\in 30\\text{--}40 \\rightarrow Q_3 = 30 + \\frac{75-45}{30} \\times 10 = 40 \\\\ S_Q &= \\frac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1} \\\\ &= \\frac{40 + 23.33 - 2(32)}{40 - 23.33} \\\\ &= \\frac{-0.67}{16.67} \\\\ &\\approx -0.04 \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q13.</strong> Values: 2, 4, 6, 8, 10 के लिए पहले चार central moments और kurtosis coefficient (\\(\\beta_2\\)) निकालें।</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-13')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-13">
        <p><strong>Solution:</strong> Mean = 6. Deviations \\((x - \\bar{x})\\): -4, -2, 0, 2, 4.</p>
        \\[ \\begin{aligned} \\mu_1 &= 0 \\\\ \\mu_2 &= \\frac{16+4+0+4+16}{5} = 8 \\\\ \\mu_3 &= 0 \\\\ \\mu_4 &= \\frac{256+16+0+16+256}{5} = 108.8 \\\\ \\beta_2 &= \\frac{\\mu_4}{\\mu_2^2} = \\frac{108.8}{64} = 1.7 \\end{aligned} \\]
        <p>चूँकि \\(\\beta_2 < 3\\), यह platykurtic है।</p>
      </div>

      <div class="question"><strong>Q14.</strong> इस contingency table से fathers और sons के Eye color के बीच Yule's coefficient of association (Q) निकालें:
        <div class="freq-table-wrap">
          <table class="cont-table">
            <thead><tr><th>Fathers \\ Sons</th><th>Light Eyes</th><th>Dark Eyes</th></tr></thead>
            <tbody>
              <tr><td><strong>Light Eyes</strong></td><td>400</td><td>50</td></tr>
              <tr><td><strong>Dark Eyes</strong></td><td>80</td><td>470</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-14')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-14">
        <p><strong>Solution:</strong> मान लें \\((AB) = 400\\), \\((A\\beta) = 50\\), \\((\\alpha B) = 80\\), \\((\\alpha\\beta) = 470\\)।</p>
        \\[ \\begin{aligned} Q &= \\frac{(AB)(\\alpha\\beta) - (A\\beta)(\\alpha B)}{(AB)(\\alpha\\beta) + (A\\beta)(\\alpha B)} \\\\ &= \\frac{400 \\times 470 - 50 \\times 80}{400 \\times 470 + 50 \\times 80} \\\\ &= \\frac{188000 - 4000}{188000 + 4000} \\\\ &= \\frac{184000}{192000} \\\\ &\\approx +0.958 \\end{aligned} \\]
        <p>High positive association है।</p>
      </div>

      <div class="question"><strong>Q15.</strong> Treatment data के लिए Yule's Coefficient of Colligation (Y) निकालें:
        <div class="freq-table-wrap">
          <table class="cont-table">
            <thead><tr><th></th><th>Recovered</th><th>Not Recovered</th></tr></thead>
            <tbody>
              <tr><td><strong>Treated</strong></td><td>200</td><td>50</td></tr>
              <tr><td><strong>Not Treated</strong></td><td>100</td><td>150</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-15')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-15">
        <p><strong>Solution:</strong> \\((AB)=200\\), \\((A\\beta)=50\\), \\((\\alpha B)=100\\), \\((\\alpha\\beta)=150\\)।</p>
        \\[ \\begin{aligned} p &= \\sqrt{200 \\times 150} = \\sqrt{30000} \\approx 173.2 \\\\ q &= \\sqrt{50 \\times 100} = \\sqrt{5000} \\approx 70.7 \\\\ Y &= \\frac{p - q}{p + q} \\\\ &= \\frac{173.2 - 70.7}{173.2 + 70.7} \\\\ &= \\frac{102.5}{243.9} \\\\ &\\approx +0.42 \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q16.</strong> Data की consistency जांचें: N = 1000, (A) = 500, (B) = 400, (A\\(\\beta\\)) = 200.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-16')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-16">
        <p><strong>Solution:</strong> Ultimate class frequencies \\(\\ge 0\\) होनी चाहिए।</p>
        \\[ \\begin{aligned} (AB) &= (A) - (A\\beta) = 500 - 200 = 300 \\\\ (\\alpha B) &= (B) - (AB) = 400 - 300 = 100 \\\\ (\\alpha\\beta) &= N - (A) - (\\alpha B) = 1000 - 500 - 100 = 400 \\end{aligned} \\]
        <p>सभी frequencies (300, 200, 100, 400) \\(\\ge 0\\) हैं, इसलिए data consistent है।</p>
      </div>

      <div class="question"><strong>Q17.</strong> Origin के about पहले दो raw moments 5 और 35 हैं। Variance और standard deviation निकालें।</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-17')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-17">
        <p><strong>Solution:</strong> \\(\\mu'_1 = 5\\), \\(\\mu'_2 = 35\\)।</p>
        \\[ \\begin{aligned} \\text{Variance } (\\mu_2) &= \\mu'_2 - (\\mu'_1)^2 \\\\ &= 35 - 5^2 \\\\ &= 35 - 25 \\\\ &= 10 \\\\ \\text{Standard Deviation} &= \\sqrt{10} \\approx 3.16 \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q18.</strong> एक frequency distribution में \\(P_{10} = 15\\), \\(P_{50} = 35\\), \\(P_{90} = 65\\) है। Kelly's Coefficient of Skewness निकालें।</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-18')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-18">
        <p><strong>Solution:</strong></p>
        \\[ \\begin{aligned} S_P &= \\frac{P_{90} + P_{10} - 2P_{50}}{P_{90} - P_{10}} \\\\ &= \\frac{65 + 15 - 2(35)}{65 - 15} \\\\ &= \\frac{80 - 70}{50} \\\\ &= +0.20 \\end{aligned} \\]
      </div>

      <div class="question"><strong>Q19.</strong> (AB) की expected frequency निकालें और association का type बताएं: N = 200, (A) = 100, (B) = 50, और Observed (AB) = 20.</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-19')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-19">
        <p><strong>Solution:</strong></p>
        \\[ \\begin{aligned} E(AB) &= \\frac{(A)(B)}{N} \\\\ &= \\frac{100 \\times 50}{200} \\\\ &= 25 \\end{aligned} \\]
        <p>Observed (20) &lt; Expected (25), इसलिए negative association है।</p>
      </div>

      <div class="question"><strong>Q20.</strong> यदि \\((A) = (\\alpha) = (B) = (\\beta) = \\frac{N}{2}\\), prove करें कि consistency के लिए (AB) की maximum value \\(\\frac{N}{2}\\) और minimum 0 है।</div>
      <button class="toggle-btn" onclick="toggleAnswer('subj-hin-20')">Show Answer ▼</button>
      <div class="answer" id="subj-hin-20">
        <p><strong>Solution:</strong> Consistency condition: \\(\\max(0, A+B-N) \\le (AB) \\le \\min(A, B)\\)।</p>
        <p>\\(A = N/2\\), \\(B = N/2\\) रखने पर:</p>
        \\[ \\begin{aligned} \\max\\left(0, \\frac{N}{2}+\\frac{N}{2}-N\\right) &\\le (AB) \\le \\min\\left(\\frac{N}{2}, \\frac{N}{2}\\right) \\\\ \\max(0, 0) &\\le (AB) \\le \\frac{N}{2} \\\\ 0 &\\le (AB) \\le \\frac{N}{2} \\end{aligned} \\]
        <p>∎</p>
      </div>
    </div>"""

match_eng = re.search(r'<div class="english-content">\s*<h2><span class="section-num">📝</span> Subjective Questions.*?</div>\s*<div class="hinglish-content"', content, flags=re.DOTALL)
match_hin = re.search(r'<div class="hinglish-content".*?<h2><span class="section-num">📝</span> Subjective Questions.*?</div>\s*</section>', content, flags=re.DOTALL)

if match_eng and match_hin:
    new_content = content[:match_eng.start()] + english_content + '\n' + hinglish_content + '\n  </section>'
    with open('Stat-101/Unit-IV.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success")
else:
    print("Could not match the sections")
