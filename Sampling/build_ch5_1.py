content = r"""
        <section id="sec5-1" class="section-card active">
            <div class="english-content">
                <h2>5.1 Introduction</h2>
                <div class="quote">
                    "In a minute there is time / For decisions and revisions which a minute will reverse." -- <strong>T.S. Eliot</strong>
                </div>
                <p>In Chapter 2 we discussed simple random sampling in which the selection probabilities were strictly equal for all units of the population. Whenever the units vary fundamentally in size, simple random sampling is not an appropriate mathematical procedure as no importance is given to the size of the unit. Such ancillary information about the size of the units can be efficiently utilized in selecting the sample so as to mathematically derive more efficient estimators of the population parameters.</p>
                <p>One such powerful method is to definitively assign unequal probabilities of selection to different units in the population precisely depending on their relative sizes. When units vary heavily in their sizes and the variate under study is mathematically highly correlated with the size of the unit, the probability of selection may be explicitly assigned in strict proportion to the size of the unit. This type of sampling procedure where the probability of selection is proportional to the size of the unit is unequivocally known as <strong>probability proportional to size sampling</strong>, abbreviated universally as <strong>pps sampling</strong>.</p>
                
                <p>There is a basic structural mathematical difference between simple random sampling and pps sampling procedures:</p>
                <ul>
                    <li>In simple random sampling, the mathematical probability of drawing any specified unit at any given draw is rigorously exactly the same (\( 1/N \)).</li>
                    <li>In pps sampling, the probability intrinsically differs from draw to draw based on size.</li>
                </ul>
                <p>The core mathematical theory of pps sampling is consequently heavily more complex than that of simple random sampling. We shall first comprehensively discuss the theory mathematically appropriate to pps sampling with replacement (pps wr) and then rigorously present the advanced theory of pps sampling without replacement (pps wor).</p>
            </div>
            
            <div class="hinglish-content">
                <h2>5.1 परिचय (Introduction)</h2>
                <div class="quote">
                    "एक मिनट में समय है / उन निर्णयों और संशोधनों के लिए जिन्हें एक मिनट पलट देगा।" -- <strong>T.S. Eliot</strong>
                </div>
                <p>Chapter 2 में हमने simple random sampling पर चर्चा की, जिसमें population की सभी units के लिए selection probabilities पूरी तरह से समान थीं। जब भी units आकार (size) में मौलिक रूप से भिन्न (vary) होती हैं, simple random sampling एक उचित गणितीय प्रक्रिया (appropriate procedure) नहीं है क्योंकि unit के आकार को कोई महत्व नहीं दिया जाता है। Units के आकार के बारे में ऐसी सहायक जानकारी (ancillary information) का उपयोग sample को select करने में प्रभावी रूप से किया जा सकता है ताकि population parameters के अधिक कुशल (efficient) estimators गणितीय रूप से प्राप्त किए जा सकें।</p>
                <p>ऐसी एक शक्तिशाली (powerful) विधि population में विभिन्न units को उनके relative sizes के आधार पर स्पष्ट रूप से unequal probabilities of selection निर्दिष्ट (assign) करना है। जब units अपने आकार में भारी रूप से भिन्न (vary heavily) होती हैं और अध्ययन के तहत variate गणितीय रूप से unit के आकार के साथ अत्यधिक सहसंबद्ध (highly correlated) होता है, तो selection की probability स्पष्ट रूप से unit के आकार के सख्त अनुपात (proportion) में दी जा सकती है। इस प्रकार की sampling procedure जहाँ probability of selection, unit के size के proportional (समानुपाती) होती है, स्पष्ट रूप से <strong>probability proportional to size sampling</strong> के रूप में जानी जाती है, जिसे सार्वभौमिक (universally) रूप से <strong>pps sampling</strong> के रूप में संक्षिप्त (abbreviated) किया जाता है।</p>
                
                <p>Simple random sampling और pps sampling procedures के बीच एक बुनियादी संरचनात्मक गणितीय अंतर (basic structural mathematical difference) है:</p>
                <ul>
                    <li>Simple random sampling में, किसी भी दिए गए draw पर किसी निर्दिष्ट (specified) unit को निकालने की गणितीय probability कठोरता से बिल्कुल समान (\( 1/N \)) होती है।</li>
                    <li>Pps sampling में, probability आकार के आधार पर draw से draw में स्वाभाविक रूप से (intrinsically) भिन्न (differs) होती है।</li>
                </ul>
                <p>Pps sampling का मुख्य गणितीय सिद्धांत परिणामस्वरूप (consequently) simple random sampling की तुलना में काफी अधिक जटिल (complex) है। हम पहले pps sampling with replacement (pps wr) के लिए गणितीय रूप से उपयुक्त (appropriate) सिद्धांत पर व्यापक रूप से चर्चा करेंगे और फिर pps sampling without replacement (pps wor) के उन्नत सिद्धांत को कठोरता से (rigorously) प्रस्तुत करेंगे।</p>
            </div>
        </section>

        <section id="sec5-2" class="section-card">
            <div class="english-content">
                <h2>5.2 Procedures of Selecting a Sample</h2>
                <p>The mathematical procedure of rigorously selecting a pps sample fundamentally consists in intimately associating with each unit a distinct number or set of numbers precisely equal to its size. The explicit selection of units is flawlessly done corresponding to a number chosen at random from the massive totality of numbers associated. There are strictly two main methods of selection:</p>

                <h3>5.2.1 Cumulative Total Method</h3>
                <p>Let the size of the \( i \)-th unit be mathematically denoted as \( X_i \) (\( i = 1, 2, \ldots, N \)), the total overall size being rigidly \( X = \sum_{i = 1}^N X_i \). We uniquely associate the integer numbers 1 to \( X_1 \) with the very first unit, the numbers \( (X_1 + 1) \) to \( (X_1 + X_2) \) with the exact second unit, and so on progressively. A random number \( k \) is cleanly chosen at random from the range 1 to \( X \), and the unit with which this specific number is associated is conclusively selected.</p>
                <div class="derivation-block">
                    <p>Clearly, the \( i \)-th unit in the population is mathematically being selected with a robust probability strictly proportional to \( X_i \):</p>
                    $$ p_i = \frac{X_i}{X} \quad \text{for } i = 1, 2, \ldots, N $$
                    <div class="explanation">\( \because \) the number of integer tickets allocated to unit \( i \) is exactly \( X_i \) out of a total \( X \).</div>
                </div>
                <p>If a sample of precise size \( n \) is required, the procedure is rigorously repeated \( n \) times with full replacement of the units selected. This mathematical procedure of selection is distinctly known as the <strong>cumulative total method</strong> for the method severely needs continuous cumulation of the unit sizes.</p>
                <p>The main mathematical difficulty inherently in this procedure is the absolute compulsion to compute massive successive cumulative totals, which rapidly becomes time-consuming and computationally costly when the population size \( N \) is astronomically large.</p>

                <h3>Example 5.1</h3>
                <p>A region has 10 commercial warehouses consisting of 50, 30, 45, 25, 40, 26, 24, 35, 28, and 27 specific storage units, respectively. Mathematically select a sample of four distinct warehouses by the cumulative total method with replacement and with probability exactly proportional to the number of storage units.</p>
                <div class="derivation-block">
                    <p>The very first step is to flawlessly form cumulative totals as shown mathematically below:</p>
                    <table style="width: 100%; border-collapse: collapse; text-align: center; margin-top: 10px;">
                        <tr style="background: #eee; border-bottom: 1px solid var(--border);"><th>S.N.</th><th>Size (\( X_i \))</th><th>Cumulative Size</th><th>Associated Numbers</th></tr>
                        <tr><td>1</td><td>50</td><td>50</td><td>1 &ndash; 50</td></tr>
                        <tr><td>2</td><td>30</td><td>80</td><td>51 &ndash; 80</td></tr>
                        <tr><td>3</td><td>45</td><td>125</td><td>81 &ndash; 125</td></tr>
                        <tr><td>4</td><td>25</td><td>150</td><td>126 &ndash; 150</td></tr>
                        <tr><td>5</td><td>40</td><td>190</td><td>151 &ndash; 190</td></tr>
                        <tr><td>6</td><td>26</td><td>216</td><td>191 &ndash; 216</td></tr>
                        <tr><td>7</td><td>44</td><td>260</td><td>217 &ndash; 260</td></tr>
                        <tr><td>8</td><td>35</td><td>295</td><td>261 &ndash; 295</td></tr>
                        <tr><td>9</td><td>28</td><td>323</td><td>296 &ndash; 323</td></tr>
                        <tr><td>10</td><td>27</td><td>350</td><td>324 &ndash; 350</td></tr>
                    </table>
                    <p>To mathematically select a warehouse, a random number strictly not exceeding 350 is drawn. Suppose the random number selected is definitively 272. It can be seen from the cumulative totals that the number falls into the mathematical group 261&ndash;295, i.e., the 8th warehouse is selected. Similarly, choosing other numbers like 346, 165, and 094 selects the 10th, 5th, and 3rd warehouses respectively.</p>
                </div>

                <h3>5.2.2 Lahiri's Method</h3>
                <p>Lahiri (1951) elegantly suggested an alternative brilliant procedure in which tedious mathematical cumulations are completely avoided. It consists of strictly selecting a number at random between 1 and \( N \) and noting down the unit with the corresponding serial number, provisionally. Another random number is then cleanly chosen between 1 and \( M \), where \( M \) is mathematically the absolute maximum size among all the \( N \) units of the population.</p>
                <div class="derivation-block">
                    <p>If the second random number is strictly smaller than or equal to the mathematical size of the unit provisionally selected, the unit is definitively selected into the sample. If not, the entire procedure is rejected and rigorously repeated until a unit is finally selected. For a sample of \( n \) units, the procedure is identically repeated until exactly \( n \) units are secured.</p>
                    <div class="explanation">\( \because \) the probability of retaining the provisionally selected unit \( i \) is exactly \( X_i / M \), making the overall unconditional probability of selecting unit \( i \) precisely \( \frac{1}{N} \times \frac{X_i}{M} \), which is perfectly proportional to \( X_i \).</div>
                </div>

                <h3>Example 5.2</h3>
                <p>Select a sample of exactly four warehouses using the data in Example 5.1 by Lahiri's method of pps, wr.</p>
                <div class="derivation-block">
                    <p>In this case, \( N = 10 \) and the absolute maximum size \( M = 50 \) (from warehouse 1). We must draw a pair of random numbers \( (i, j) \) where \( i \leq 10 \) and \( j \leq 50 \).</p>
                    <p>Suppose the first random pair drawn is (10, 13). Since warehouse 10 has a size of 27, and 13 is strictly less than 27, the 10th unit is successfully selected.</p>
                    <p>Suppose the next drawn pair is (4, 26). The size of warehouse 4 is exactly 25. Since 26 is strictly greater than 25, this specific pair is forcefully rejected.</p>
                    <p>We draw again and get (8, 16). Warehouse 8 has size 35, and 16 is less than 35, so warehouse 8 is strictly selected. We continue this robust mathematical process until 4 units are selected.</p>
                </div>
            </div>
            
            <div class="hinglish-content">
                <h2>5.2 Procedures of Selecting a Sample (प्रतिदर्श चुनने की प्रक्रियाएं)</h2>
                <p>कड़ाई से एक pps sample को select करने की गणितीय प्रक्रिया में मौलिक रूप से प्रत्येक unit के साथ उसके आकार के ठीक बराबर एक विशिष्ट (distinct) संख्या या संख्याओं का सेट जोड़ना (associating) शामिल है। Units का स्पष्ट (explicit) चयन जुड़े हुए संख्याओं की भारी समग्रता (massive totality) से random रूप से चुनी गई संख्या के अनुरूप निर्दोष (flawlessly) रूप से किया जाता है। चयन के सख्ती से दो मुख्य तरीके हैं:</p>

                <h3>5.2.1 Cumulative Total Method (संचयी योग विधि)</h3>
                <p>मान लीजिए \( i \)-th unit का आकार गणितीय रूप से \( X_i \) (\( i = 1, 2, \ldots, N \)) के रूप में दर्शाया गया है, कुल समग्र आकार \( X = \sum_{i = 1}^N X_i \) है। हम विशिष्ट रूप से (uniquely) पूर्णांक संख्याओं (integer numbers) 1 से \( X_1 \) को पहली unit के साथ जोड़ते हैं, संख्याओं \( (X_1 + 1) \) से \( (X_1 + X_2) \) को दूसरी unit के साथ, और इसी तरह आगे बढ़ते हैं। 1 से \( X \) तक की सीमा से एक random number \( k \) साफ तौर पर चुना जाता है, और जिस unit के साथ यह विशिष्ट संख्या जुड़ी होती है, उसे निर्णायक (conclusively) रूप से चुना जाता है।</p>
                <div class="derivation-block">
                    <p>स्पष्ट रूप से, population में \( i \)-th unit को गणितीय रूप से \( X_i \) के पूरी तरह से आनुपातिक (proportional) एक मजबूत (robust) probability के साथ चुना जा रहा है:</p>
                    $$ p_i = \frac{X_i}{X} \quad \text{for } i = 1, 2, \ldots, N $$
                    <div class="explanation">\( \because \) unit \( i \) को आवंटित (allocated) integer tickets की संख्या कुल \( X \) में से ठीक \( X_i \) है।</div>
                </div>
                <p>यदि एक सटीक आकार \( n \) के sample की आवश्यकता है, तो procedure को चयनित units के पूर्ण replacement (प्रतिस्थापन) के साथ कठोरता से \( n \) बार दोहराया जाता है। चयन की यह गणितीय प्रक्रिया स्पष्ट रूप से <strong>cumulative total method</strong> के रूप में जानी जाती है क्योंकि विधि को unit sizes के निरंतर cumulation (संचय) की अत्यधिक आवश्यकता होती है।</p>
                <p>इस procedure में स्वाभाविक रूप से (inherently) मुख्य गणितीय कठिनाई विशाल (massive) क्रमिक संचयी योग (successive cumulative totals) की गणना करने की पूर्ण मजबूरी है, जो population size \( N \) खगोलीय (astronomically) रूप से बड़ा होने पर तेजी से समय लेने वाली और कम्प्यूटेशनल रूप से महंगी हो जाती है।</p>

                <h3>उदाहरण 5.1 (Example 5.1)</h3>
                <p>एक क्षेत्र में 10 व्यावसायिक गोदाम (commercial warehouses) हैं जिनमें क्रमशः 50, 30, 45, 25, 40, 26, 24, 35, 28, और 27 विशिष्ट भंडारण इकाइयाँ (storage units) हैं। Cumulative total method द्वारा replacement के साथ और भंडारण इकाइयों की संख्या के ठीक आनुपातिक probability के साथ चार अलग-अलग गोदामों का एक sample गणितीय रूप से चुनें।</p>
                <div class="derivation-block">
                    <p>पहला कदम निर्दोष रूप से (flawlessly) cumulative totals बनाना है जैसा कि गणितीय रूप से नीचे दिखाया गया है (अंग्रेजी अनुभाग में तालिका देखें)।</p>
                    <p>गणितीय रूप से एक गोदाम का चयन करने के लिए, 350 से अधिक नहीं (not exceeding) एक random number निकाला जाता है। मान लीजिए कि चयनित random number निश्चित रूप से (definitively) 272 है। Cumulative totals से यह देखा जा सकता है कि संख्या गणितीय समूह 261&ndash;295 में आती है, अर्थात, 8वां गोदाम चुना गया है। इसी तरह, 346, 165 और 094 जैसे अन्य नंबर चुनने पर क्रमशः 10वां, 5वां और तीसरा गोदाम चुना जाता है।</p>
                </div>

                <h3>5.2.2 Lahiri's Method (लाहिड़ी की विधि)</h3>
                <p>Lahiri (1951) ने सुरुचिपूर्ण (elegantly) रूप से एक वैकल्पिक शानदार procedure का सुझाव दिया जिसमें थकाऊ (tedious) गणितीय cumulations को पूरी तरह से टाल दिया जाता है। इसमें कड़ाई से 1 और \( N \) के बीच एक random number का चयन करना और अस्थायी (provisionally) रूप से corresponding serial number वाली unit को नोट करना शामिल है। फिर 1 और \( M \) के बीच एक और random number साफ तौर पर चुना जाता है, जहाँ \( M \) गणितीय रूप से population की सभी \( N \) units के बीच पूर्ण अधिकतम आकार (absolute maximum size) है।</p>
                <div class="derivation-block">
                    <p>यदि दूसरा random number अस्थायी रूप से चयनित unit के गणितीय आकार से सख्ती से छोटा या उसके बराबर है, तो unit को निश्चित रूप से sample में चुना जाता है। यदि नहीं, तो पूरी procedure को अस्वीकार कर दिया जाता है और तब तक कठोरता से दोहराया जाता है जब तक कि अंततः एक unit का चयन न हो जाए। \( n \) units के sample के लिए, procedure को समान रूप से तब तक दोहराया जाता है जब तक कि ठीक \( n \) units प्राप्त न हो जाएं।</p>
                    <div class="explanation">\( \because \) provisionally चयनित unit \( i \) को बनाए रखने (retaining) की probability ठीक \( X_i / M \) है, जिससे unit \( i \) को चुनने की समग्र बिना शर्त (unconditional) probability ठीक \( \frac{1}{N} \times \frac{X_i}{M} \) हो जाती है, जो \( X_i \) के पूरी तरह से आनुपातिक है।</div>
                </div>

                <h3>उदाहरण 5.2 (Example 5.2)</h3>
                <p>Lahiri's method (pps, wr) द्वारा उदाहरण 5.1 में data का उपयोग करके ठीक चार गोदामों का एक sample चुनें।</p>
                <div class="derivation-block">
                    <p>इस मामले में, \( N = 10 \) और पूर्ण अधिकतम आकार \( M = 50 \) (गोदाम 1 से) है। हमें random numbers \( (i, j) \) की एक जोड़ी (pair) खींचनी होगी जहाँ \( i \leq 10 \) और \( j \leq 50 \) हो।</p>
                    <p>मान लीजिए कि खींची गई पहली random जोड़ी (10, 13) है। चूंकि गोदाम 10 का आकार 27 है, और 13 सख्ती से 27 से कम है, 10वीं इकाई सफलतापूर्वक (successfully) चुनी गई है।</p>
                    <p>मान लीजिए अगली खींची गई जोड़ी (4, 26) है। गोदाम 4 का आकार ठीक 25 है। चूंकि 26 सख्ती से 25 से अधिक है, इस विशिष्ट जोड़ी को बलपूर्वक (forcefully) अस्वीकार कर दिया गया है।</p>
                    <p>हम फिर से खींचते हैं और (8, 16) प्राप्त करते हैं। गोदाम 8 का आकार 35 है, और 16, 35 से कम है, इसलिए गोदाम 8 सख्ती से चुना गया है। हम इस मजबूत गणितीय प्रक्रिया को तब तक जारी रखते हैं जब तक कि 4 इकाइयाँ नहीं चुनी जातीं।</p>
                </div>
            </div>
        </section>
        
        <section id="sec5-3" class="section-card">
            <div class="english-content">
                <h2>5.3 Estimation in PPS Sampling with Replacement: Total and its Sampling Variance</h2>
                <p>Consider a finite population of exactly \( N \) units and let \( y_i \) firmly denote the explicit value of the characteristic under study for the specific unit \( u_i \) of the population (\( i = 1, \ldots, N \)). Suppose further that \( p_i = X_i / X \) mathematically be the true probability that the unit \( u_i \) is explicitly selected in a sample of size exactly one, such that universally \( \sum_{i=1}^N p_i = 1 \).</p>
                <p>Let precisely \( n \) independent selections be strictly made with the replacement method and the value of \( y \) for each selected unit be accurately observed. Further, let \( (y_i, p_i) \) be the paired value and probability of selection of the \( i \)-th unit of the actual sample. It can be seen definitively that the random variates \( y_i / p_i \) (\( i = 1, 2, \ldots, n \)) are mathematically independently and identically distributed. If \( p_i = 1/N \), it flawlessly gives rise to a simple random sample. This rigorously shows that simple random sampling is inherently a special case of pps sampling.</p>

                <h3>Theorem 5.3.1</h3>
                <p>In pps sampling, wr, an unbiased mathematical estimator of the population total \( Y \) is rigorously given by:</p>
                <div class="derivation-block">
                    $$ \widehat{Y}_{pps} = \frac{1}{n} \sum_{i=1}^n \frac{y_i}{p_i} \quad (5.3.1) $$
                    <p>with its exact sampling variance elegantly given by:</p>
                    $$ V(\widehat{Y}_{pps}) = \frac{1}{n} \sum_{i=1}^N p_i \left( \frac{y_i}{p_i} - Y \right)^2 \quad (5.3.2) $$
                </div>
                <p><em>Proof:</em></p>
                <div class="derivation-block">
                    <p>Let us definitively define random variates \( z_i = y_i / p_i \) (\( i = 1, \ldots, n \)) which are strictly independently and identically distributed. Hence,</p>
                    $$ E(z_i) = \sum_{i=1}^N p_i \left( \frac{y_i}{p_i} \right) = \sum_{i=1}^N y_i = Y $$
                    <div class="explanation">\( \because \) the expected value over the entire population mathematically cancels out the probabilities, leaving the exact population total \( Y \).</div>
                    <p>Now let us rigorously consider \( \widehat{Y}_{pps} = \frac{1}{n} \sum_{i=1}^n z_i \). Since</p>
                    $$ E(\widehat{Y}_{pps}) = E\left( \frac{1}{n} \sum_{i=1}^n z_i \right) = \frac{1}{n} \sum_{i=1}^n E(z_i) = \frac{1}{n} (n Y) = Y $$
                    <div class="explanation">\( \because \) the expectation of a sum is the sum of expectations, heavily confirming \( \widehat{Y}_{pps} \) is definitively an unbiased estimator.</div>
                    <p>To explicitly obtain the sampling variance of \( \widehat{Y}_{pps} \), we have:</p>
                    $$ V(\widehat{Y}_{pps}) = V\left( \frac{1}{n} \sum_{i=1}^n z_i \right) = \frac{1}{n^2} \sum_{i=1}^n V(z_i) = \frac{1}{n} V(z_i) $$
                    <div class="explanation">\( \because \) the covariance terms \( \text{Cov}(y_i/p_i, y_j/p_j) \), for \( i \neq j \), are rigorously zero due to completely independent draws with replacement.</div>
                    $$ = \frac{1}{n} \sum_{i=1}^N p_i \left( \frac{y_i}{p_i} - Y \right)^2 $$
                    <p>This explicitly shows that the mathematical variance of the estimator is strictly inversely proportional to the sample size \( n \) as in simple random sampling, wr.</p>
                </div>

                <h3>Corollary</h3>
                <p>An unbiased estimator of the population mean, \( \bar{Y}_{pps} \), is mathematically given by:</p>
                <div class="derivation-block">
                    $$ \bar{y}_{pps} = \frac{1}{n} \sum_{i=1}^n \frac{y_i}{N p_i} \quad (5.3.3) $$
                    <p>with its precise sampling variance:</p>
                    $$ V(\bar{y}_{pps}) = \frac{1}{n} \sum_{i=1}^N p_i \left( \frac{y_i}{N p_i} - \bar{Y} \right)^2 \quad (5.3.4) $$
                </div>

                <h3>Theorem 5.3.2</h3>
                <p>In pps sampling, wr, an unbiased mathematical estimator of \( V(\bar{y}_{pps}) \) is securely given by:</p>
                <div class="derivation-block">
                    $$ \widehat{v}(\bar{y}_{pps}) = \frac{1}{n(n-1)} \sum_{i=1}^n \left[ \frac{y_i}{N p_i} - \bar{y}_{pps} \right]^2 \quad (5.3.5) $$
                    $$ = \frac{1}{n(n-1)} \left[ \sum_{i=1}^n \left( \frac{y_i}{N p_i} \right)^2 - n \bar{y}_{pps}^2 \right] \quad (5.3.6) $$
                </div>
                <p><em>Proof:</em></p>
                <div class="derivation-block">
                    <p>In pps sampling, wr, \( z_i (= y_i / p_i) \), \( i = 1, 2, \ldots, n \), are strictly independent unbiased estimators of \( Y \) having exactly the same variance. Let us define:</p>
                    $$ s^2 = \frac{\sum (z_i - \bar{z})^2}{n - 1} $$
                    <div class="explanation">\( \because \) it mathematically mimics the standard unbiased sample variance formula for independent and identically distributed variables.</div>
                    <p>It can be definitively shown that \( s^2 \) is an unbiased estimator of the true population variance parameter. By substituting \( y_i / N p_i \) for \( z_i \) and adjusting for the mean, the theorem is robustly proven.</p>
                </div>

                <h3>Corollary</h3>
                <p>An unbiased estimator of \( V(\widehat{Y}_{pps}) \) is efficiently given by:</p>
                <div class="derivation-block">
                    $$ \widehat{v}(\widehat{Y}_{pps}) = \frac{N^2}{n(n-1)} \sum_{i=1}^n \left( \frac{y_i}{N p_i} - \bar{y}_{pps} \right)^2 \quad (5.3.7) $$
                    $$ = \frac{1}{n(n-1)} \left[ \sum_{i=1}^n \left( \frac{y_i}{p_i} \right)^2 - n \widehat{Y}_{pps}^2 \right] \quad (5.3.8) $$
                    <p>Equation (5.3.8) is predominantly used for rapid computational purposes.</p>
                </div>
            </div>

            <div class="hinglish-content">
                <h2>5.3 Estimation in PPS Sampling with Replacement: Total and its Sampling Variance (माध्य और इसके प्रतिचयन प्रसरण का अनुमान)</h2>
                <p>ठीक \( N \) units की एक finite population पर विचार करें और मान लें कि \( y_i \) population की विशिष्ट unit \( u_i \) के लिए अध्ययन के तहत characteristic के स्पष्ट मूल्य (explicit value) को दृढ़ता (firmly) से दर्शाता है (\( i = 1, \ldots, N \))। आगे मान लीजिए कि \( p_i = X_i / X \) गणितीय रूप से true probability है कि unit \( u_i \) को ठीक एक आकार के sample में स्पष्ट रूप से चुना गया है, ताकि सार्वभौमिक (universally) रूप से \( \sum_{i=1}^N p_i = 1 \) हो।</p>
                <p>मान लीजिए कि replacement method के साथ कड़ाई से (strictly) \( n \) independent selections किए जाते हैं और प्रत्येक चयनित unit के लिए \( y \) का मूल्य सटीक (accurately) रूप से देखा जाता है। इसके अलावा, मान लीजिए कि \( (y_i, p_i) \) actual sample की \( i \)-th unit का paired value और probability of selection है। यह निश्चित रूप से (definitively) देखा जा सकता है कि random variates \( y_i / p_i \) (\( i = 1, 2, \ldots, n \)) गणितीय रूप से independently और identically distributed हैं। यदि \( p_i = 1/N \) है, तो यह निर्दोष रूप से एक simple random sample को जन्म देता है। यह कठोरता से (rigorously) दर्शाता है कि simple random sampling स्वाभाविक रूप से (inherently) pps sampling का एक विशेष मामला है।</p>

                <h3>Theorem 5.3.1</h3>
                <p>Pps sampling, wr में, population total \( Y \) का एक unbiased mathematical estimator कठोरता से इस प्रकार दिया गया है:</p>
                <div class="derivation-block">
                    $$ \widehat{Y}_{pps} = \frac{1}{n} \sum_{i=1}^n \frac{y_i}{p_i} \quad (5.3.1) $$
                    <p>इसके exact sampling variance के साथ जो सुरुचिपूर्ण (elegantly) रूप से इस प्रकार दिया गया है:</p>
                    $$ V(\widehat{Y}_{pps}) = \frac{1}{n} \sum_{i=1}^N p_i \left( \frac{y_i}{p_i} - Y \right)^2 \quad (5.3.2) $$
                </div>
                <p><em>Proof (प्रमाण):</em></p>
                <div class="derivation-block">
                    <p>आइए निश्चित रूप से (definitively) random variates \( z_i = y_i / p_i \) (\( i = 1, \ldots, n \)) को परिभाषित करें जो सख्ती से independently और identically distributed हैं। अतः,</p>
                    $$ E(z_i) = \sum_{i=1}^N p_i \left( \frac{y_i}{p_i} \right) = \sum_{i=1}^N y_i = Y $$
                    <div class="explanation">\( \because \) पूरी population पर expected value गणितीय रूप से probabilities को रद्द (cancels out) कर देता है, जिससे ठीक population total \( Y \) बचता है।</div>
                    <p>अब हम कठोरता से \( \widehat{Y}_{pps} = \frac{1}{n} \sum_{i=1}^n z_i \) पर विचार करें। चूँकि</p>
                    $$ E(\widehat{Y}_{pps}) = E\left( \frac{1}{n} \sum_{i=1}^n z_i \right) = \frac{1}{n} \sum_{i=1}^n E(z_i) = \frac{1}{n} (n Y) = Y $$
                    <div class="explanation">\( \because \) योग (sum) का expectation expectations का योग है, जो दृढ़ता से पुष्टि (confirming) करता है कि \( \widehat{Y}_{pps} \) निश्चित रूप से एक unbiased estimator है।</div>
                    <p>स्पष्ट रूप से \( \widehat{Y}_{pps} \) का sampling variance प्राप्त करने के लिए, हमारे पास है:</p>
                    $$ V(\widehat{Y}_{pps}) = V\left( \frac{1}{n} \sum_{i=1}^n z_i \right) = \frac{1}{n^2} \sum_{i=1}^n V(z_i) = \frac{1}{n} V(z_i) $$
                    <div class="explanation">\( \because \) covariance terms \( \text{Cov}(y_i/p_i, y_j/p_j) \), \( i \neq j \) के लिए, replacement के साथ पूरी तरह से independent draws के कारण कठोरता से शून्य हैं।</div>
                    $$ = \frac{1}{n} \sum_{i=1}^N p_i \left( \frac{y_i}{p_i} - Y \right)^2 $$
                    <p>यह स्पष्ट रूप से दर्शाता है कि estimator का mathematical variance कड़ाई से sample size \( n \) के व्युत्क्रमानुपाती (inversely proportional) है जैसा कि simple random sampling, wr में होता है।</p>
                </div>

                <h3>Corollary</h3>
                <p>Population mean, \( \bar{Y}_{pps} \), का एक unbiased estimator गणितीय रूप से इस प्रकार दिया गया है:</p>
                <div class="derivation-block">
                    $$ \bar{y}_{pps} = \frac{1}{n} \sum_{i=1}^n \frac{y_i}{N p_i} \quad (5.3.3) $$
                    <p>इसके सटीक (precise) sampling variance के साथ:</p>
                    $$ V(\bar{y}_{pps}) = \frac{1}{n} \sum_{i=1}^N p_i \left( \frac{y_i}{N p_i} - \bar{Y} \right)^2 \quad (5.3.4) $$
                </div>

                <h3>Theorem 5.3.2</h3>
                <p>Pps sampling, wr में, \( V(\bar{y}_{pps}) \) का एक unbiased mathematical estimator सुरक्षित रूप से (securely) इस प्रकार दिया गया है:</p>
                <div class="derivation-block">
                    $$ \widehat{v}(\bar{y}_{pps}) = \frac{1}{n(n-1)} \sum_{i=1}^n \left[ \frac{y_i}{N p_i} - \bar{y}_{pps} \right]^2 \quad (5.3.5) $$
                    $$ = \frac{1}{n(n-1)} \left[ \sum_{i=1}^n \left( \frac{y_i}{N p_i} \right)^2 - n \bar{y}_{pps}^2 \right] \quad (5.3.6) $$
                </div>
                <p><em>Proof (प्रमाण):</em></p>
                <div class="derivation-block">
                    <p>Pps sampling, wr में, \( z_i (= y_i / p_i) \), \( i = 1, 2, \ldots, n \), बिल्कुल समान variance वाले \( Y \) के सख्ती से independent unbiased estimators हैं। आइए परिभाषित करें:</p>
                    $$ s^2 = \frac{\sum (z_i - \bar{z})^2}{n - 1} $$
                    <div class="explanation">\( \because \) यह गणितीय रूप से independent और identically distributed variables के लिए मानक unbiased sample variance सूत्र की नकल (mimics) करता है।</div>
                    <p>यह निश्चित रूप से दिखाया जा सकता है कि \( s^2 \) true population variance parameter का एक unbiased estimator है। \( z_i \) के लिए \( y_i / N p_i \) को प्रतिस्थापित करके और mean को समायोजित (adjusting) करके, theorem को मजबूती से (robustly) साबित किया गया है।</p>
                </div>

                <h3>Corollary</h3>
                <p>\( V(\widehat{Y}_{pps}) \) का एक unbiased estimator कुशलतापूर्वक (efficiently) इस प्रकार दिया गया है:</p>
                <div class="derivation-block">
                    $$ \widehat{v}(\widehat{Y}_{pps}) = \frac{N^2}{n(n-1)} \sum_{i=1}^n \left( \frac{y_i}{N p_i} - \bar{y}_{pps} \right)^2 \quad (5.3.7) $$
                    $$ = \frac{1}{n(n-1)} \left[ \sum_{i=1}^n \left( \frac{y_i}{p_i} \right)^2 - n \widehat{Y}_{pps}^2 \right] \quad (5.3.8) $$
                    <p>समीकरण (5.3.8) का उपयोग मुख्य रूप से (predominantly) तीव्र (rapid) कम्प्यूटेशनल उद्देश्यों के लिए किया जाता है।</p>
                </div>
            </div>
        </section>

        <section id="sec5-4" class="section-card">
            <div class="english-content">
                <h2>5.4 Gain due to PPS Sampling with Replacement</h2>
                <p>One may naturally be extremely interested to know whether it is strictly possible to mathematically estimate the actual gain due to pps sampling, as systematically compared to simple random sampling, directly from the pps sample itself. In simple random sample, wr, the true variance is firmly given by:</p>
                <div class="derivation-block">
                    $$ V(\bar{y}_{SR}) = \frac{1}{N^2} \left[ \frac{1}{n} \sum_{i=1}^N y_i^2 - \bar{Y}^2 \right] \quad (5.3.9) $$
                </div>
                <p>An exact unbiased estimator of \( \sum y_i^2 \) is strictly given by \( \frac{1}{n} \sum \frac{y_i^2}{p_i} \) and that of \( N \bar{Y}^2 \) is robustly mathematically obtained from:</p>
                <div class="derivation-block">
                    $$ \left[ \widehat{Y}_{pps}^2 - \widehat{v}(\widehat{Y}_{pps}) \right] $$
                </div>
                <p>After rigorously substituting these calculated values, we meticulously have an unbiased estimator of the variance of the estimate strictly based on simple random sample calculated purely on the basis of the pps sample estimate:</p>
                <div class="derivation-block">
                    $$ \widehat{v}_{pps}(\bar{y}_{SR}) = \frac{1}{N^2} \left[ \frac{1}{n} \sum_{i=1}^n \frac{y_i^2}{p_i} - \left( \widehat{Y}_{pps}^2 - \widehat{v}(\widehat{Y}_{pps}) \right) \right] \quad (5.3.10) $$
                </div>
                <p>Hence, the percentage gain safely due to pps sampling can be rigorously estimated by:</p>
                <div class="derivation-block">
                    $$ \text{Gain} = \frac{\left[ \widehat{v}_{pps}(\bar{y}_{SR}) - \widehat{v}(\bar{y}_{pps}) \right]}{\widehat{v}(\bar{y}_{pps})} \times 100 \quad (5.3.11) $$
                </div>

                <h3 style="margin-top: 40px;">Example 5.3</h3>
                <p>A rigorous sample survey was conducted to extensively study the yield of wheat in a region. A sample of 20 agricultural farms from a total of exactly 100 was strictly taken, with probability cleanly proportional to the physical area under wheat crop, explicitly with the replacement method. The total area under wheat crop (\( X \)) was mathematically 484.5 hectares. The area under crop (\( x \)) and final yield (\( y \)) were noted precisely in hectares and quintals per hectare, respectively.</p>
                <p>The sample selected firmly by the cumulative total method was:</p>
                <table style="width: 100%; border-collapse: collapse; text-align: center; margin-bottom: 20px; font-size: 0.9em;">
                    <tr style="background: #eee; border-bottom: 1px solid var(--border);"><th>Area (\( x \))</th><td>5.2</td><td>25.9</td><td>93.9</td><td>4.2</td><td>4.7</td><td>4.8</td><td>4.9</td><td>6.8</td><td>4.7</td><td>5.7</td><td>2.1</td><td>2.4</td><td>4.0</td><td>11.3</td><td>7.4</td><td>7.4</td><td>4.8</td><td>1.2</td><td>2.6</td><td>6.2</td></tr>
                    <tr><th>Yield (\( y \))</th><td>28</td><td>30</td><td>22</td><td>24</td><td>25</td><td>28</td><td>37</td><td>26</td><td>32</td><td>16</td><td>16</td><td>16</td><td>61</td><td>61</td><td>29</td><td>47</td><td>22</td><td>24</td><td>34</td><td>40</td></tr>
                </table>
                <p>The sample securely selected by Lahiri's method was:</p>
                <table style="width: 100%; border-collapse: collapse; text-align: center; margin-bottom: 20px; font-size: 0.9em;">
                    <tr style="background: #eee; border-bottom: 1px solid var(--border);"><th>Area (\( x \))</th><td>4.8</td><td>4.1</td><td>1.3</td><td>5.2</td><td>6.9</td><td>6.0</td><td>2.0</td><td>6.3</td><td>5.2</td><td>4.2</td><td>4.8</td><td>5.9</td><td>5.8</td><td>5.8</td><td>5.1</td><td>4.7</td><td>5.6</td><td>5.2</td><td>4.0</td><td>4.6</td></tr>
                    <tr><th>Yield (\( y \))</th><td>22</td><td>19</td><td>6</td><td>25</td><td>54</td><td>43</td><td>4</td><td>40</td><td>28</td><td>29</td><td>22</td><td>39</td><td>39</td><td>44</td><td>30</td><td>27</td><td>34</td><td>31</td><td>18</td><td>31</td></tr>
                </table>
                <p>Mathematically estimate the average yield per farm along with its standard error for both specific samples. Also explicitly estimate the exact gain in efficiency due strictly to pps sampling compared directly to simple random sampling with replacement.</p>
                
                <div class="derivation-block">
                    <p><strong>(i) Cumulative Total Method</strong></p>
                    <p>(a) The robust estimate of average yield/farm is precisely given by:</p>
                    $$ \bar{y}_{pps} = \frac{1}{nN} \sum \frac{y_i}{p_i} $$
                    <p>Here strictly \( N = 100 \), \( n = 20 \), \( X = 484.5 \). Therefore,</p>
                    $$ \bar{y}_{pps} = \frac{484.5 \times 1205930}{100 \times 20} = 29.11 $$
                    <p>and</p>
                    $$ \widehat{v}(\bar{y}_{pps}) = \frac{1}{20 \times 19} \left[ \frac{(484.5)^2 \times 728.1481}{100 \times 100} - 20(29.11)^2 \right] = 2.00 $$
                    <p>or absolute standard error of \( \bar{y}_{pps} = \sqrt{2.00} = 1.41 \).</p>

                    <p>(b) The mathematical estimate of variance based exactly on a simple random sample, on the assumption of the pps sample, is securely given by:</p>
                    $$ \widehat{v}_{pps}(\bar{y}_{SR}) = \frac{100}{20 \times 99} \left[ \frac{484.5 \times 4156.05}{20 \times (100)} - 100 \times (29.11)^2 - 2.00 \right] = 7.64 $$
                    <p>Hence, the percentage gain in precision strictly due to pps sampling is cleanly:</p>
                    $$ \text{Percentage gain} = \frac{7.64 - 2.00}{2.00} \times 100 = 282\% $$

                    <p><strong>(ii) Lahiri's Method</strong></p>
                    <p>(a) The rigorous estimate of average yield/farm is given by:</p>
                    $$ \bar{y}_{pps} = \frac{484.5 \times 114.85}{100 \times 20} = 27.82 $$
                    <p>and</p>
                    $$ \widehat{v}(\bar{y}_{pps}) = \frac{1}{20 \times 19} \left[ 23.4740 \times 708.6056 - 20 \times (27.82)^2 \right] = 2.27 $$
                    <p>Standard error of \( \bar{y}_{pps} = \sqrt{2.27} = 1.51 \).</p>

                    <p>(b) The absolute estimate of variance based on simple random sample is explicitly:</p>
                    $$ \widehat{v}_{pps}(\bar{y}_{SR}) = \frac{100 \times 80}{20 \times 99} \left[ \frac{484.5 \times 3734.74}{20 \times (100)} - (27.82)^2 - 2.27 \right] = 5.78 $$
                    <p>Therefore, the robust percentage gain in efficiency unequivocally is:</p>
                    $$ \frac{(5.78 - 2.27)}{2.27} \times 100 = 155\% $$
                </div>
            </div>

            <div class="hinglish-content">
                <h2>5.4 Gain due to PPS Sampling with Replacement (PPS प्रतिचयन के कारण लाभ)</h2>
                <p>कोई व्यक्ति स्वाभाविक रूप से यह जानने के लिए अत्यधिक इच्छुक (extremely interested) हो सकता है कि क्या सीधे pps sample से ही, simple random sampling की तुलना में pps sampling के कारण वास्तविक लाभ (actual gain) का गणितीय रूप से अनुमान लगाना संभव है। Simple random sample, wr में, true variance दृढ़ता से (firmly) इस प्रकार दिया गया है:</p>
                <div class="derivation-block">
                    $$ V(\bar{y}_{SR}) = \frac{1}{N^2} \left[ \frac{1}{n} \sum_{i=1}^N y_i^2 - \bar{Y}^2 \right] \quad (5.3.9) $$
                </div>
                <p>\( \sum y_i^2 \) का एक सटीक (exact) unbiased estimator सख्ती से \( \frac{1}{n} \sum \frac{y_i^2}{p_i} \) द्वारा दिया गया है और \( N \bar{Y}^2 \) का अनुमान मजबूती से (robustly) गणितीय रूप से प्राप्त किया जाता है:</p>
                <div class="derivation-block">
                    $$ \left[ \widehat{Y}_{pps}^2 - \widehat{v}(\widehat{Y}_{pps}) \right] $$
                </div>
                <p>इन परिकलित (calculated) मानों को कठोरता से प्रतिस्थापित (substituting) करने के बाद, हमारे पास विशुद्ध रूप से (purely) pps sample estimate के आधार पर कैलकुलेट किए गए simple random sample पर सख्ती से आधारित estimate के variance का एक unbiased estimator सावधानीपूर्वक (meticulously) है:</p>
                <div class="derivation-block">
                    $$ \widehat{v}_{pps}(\bar{y}_{SR}) = \frac{1}{N^2} \left[ \frac{1}{n} \sum_{i=1}^n \frac{y_i^2}{p_i} - \left( \widehat{Y}_{pps}^2 - \widehat{v}(\widehat{Y}_{pps}) \right) \right] \quad (5.3.10) $$
                </div>
                <p>अतः, सुरक्षित रूप से (safely) pps sampling के कारण percentage gain का अनुमान कठोरता से लगाया जा सकता है:</p>
                <div class="derivation-block">
                    $$ \text{Gain} = \frac{\left[ \widehat{v}_{pps}(\bar{y}_{SR}) - \widehat{v}(\bar{y}_{pps}) \right]}{\widehat{v}(\bar{y}_{pps})} \times 100 \quad (5.3.11) $$
                </div>

                <h3 style="margin-top: 40px;">उदाहरण 5.3 (Example 5.3)</h3>
                <p>एक क्षेत्र में गेहूं की उपज (yield) का बड़े पैमाने पर (extensively) अध्ययन करने के लिए एक कठोर sample survey आयोजित किया गया था। कुल 100 में से ठीक 20 कृषि फार्मों (agricultural farms) का एक sample सख्ती से लिया गया था, जिसमें probability साफ तौर पर गेहूं की फसल के तहत भौतिक क्षेत्र (physical area) के आनुपातिक (proportional) थी, स्पष्ट रूप से replacement method के साथ। गेहूं की फसल के तहत कुल क्षेत्र (\( X \)) गणितीय रूप से 484.5 हेक्टेयर था। फसल के तहत क्षेत्र (\( x \)) और अंतिम उपज (\( y \)) को क्रमशः हेक्टेयर और क्विंटल प्रति हेक्टेयर में सटीक रूप से दर्ज किया गया था।</p>
                <p>Cumulative total method द्वारा मजबूती से (firmly) चुना गया sample था (अंग्रेजी अनुभाग में पहली तालिका देखें)।</p>
                <p>Lahiri's method द्वारा सुरक्षित रूप से (securely) चुना गया sample था (अंग्रेजी अनुभाग में दूसरी तालिका देखें)।</p>
                <p>गणितीय रूप से दोनों विशिष्ट samples के लिए इसके standard error के साथ प्रति फार्म औसत उपज का अनुमान लगाएं। Replacement के साथ simple random sampling की तुलना में सीधे तौर पर pps sampling के कारण दक्षता (efficiency) में सटीक लाभ का भी स्पष्ट (explicitly) अनुमान लगाएं।</p>
                
                <div class="derivation-block">
                    <p><strong>(i) Cumulative Total Method</strong></p>
                    <p>(a) औसत उपज/खेत (average yield/farm) का मजबूत estimate ठीक (precisely) इस प्रकार दिया गया है:</p>
                    $$ \bar{y}_{pps} = \frac{1}{nN} \sum \frac{y_i}{p_i} $$
                    <p>यहाँ सख्ती से \( N = 100 \), \( n = 20 \), \( X = 484.5 \)। इसलिए,</p>
                    $$ \bar{y}_{pps} = \frac{484.5 \times 1205930}{100 \times 20} = 29.11 $$
                    <p>और</p>
                    $$ \widehat{v}(\bar{y}_{pps}) = \frac{1}{20 \times 19} \left[ \frac{(484.5)^2 \times 728.1481}{100 \times 100} - 20(29.11)^2 \right] = 2.00 $$
                    <p>या \( \bar{y}_{pps} \) का पूर्ण standard error \( = \sqrt{2.00} = 1.41 \)।</p>

                    <p>(b) Pps sample की धारणा (assumption) पर, ठीक simple random sample पर आधारित variance का गणितीय estimate सुरक्षित रूप से (securely) इस प्रकार दिया गया है:</p>
                    $$ \widehat{v}_{pps}(\bar{y}_{SR}) = \frac{100}{20 \times 99} \left[ \frac{484.5 \times 4156.05}{20 \times (100)} - 100 \times (29.11)^2 - 2.00 \right] = 7.64 $$
                    <p>अतः, सख्ती से pps sampling के कारण precision में percentage gain साफ तौर पर है:</p>
                    $$ \text{Percentage gain} = \frac{7.64 - 2.00}{2.00} \times 100 = 282\% $$

                    <p><strong>(ii) Lahiri's Method</strong></p>
                    <p>(a) औसत उपज/खेत का कठोर (rigorous) estimate इस प्रकार दिया गया है:</p>
                    $$ \bar{y}_{pps} = \frac{484.5 \times 114.85}{100 \times 20} = 27.82 $$
                    <p>और</p>
                    $$ \widehat{v}(\bar{y}_{pps}) = \frac{1}{20 \times 19} \left[ 23.4740 \times 708.6056 - 20 \times (27.82)^2 \right] = 2.27 $$
                    <p>\( \bar{y}_{pps} \) का standard error \( = \sqrt{2.27} = 1.51 \)।</p>

                    <p>(b) Simple random sample पर आधारित variance का पूर्ण estimate स्पष्ट रूप से (explicitly) है:</p>
                    $$ \widehat{v}_{pps}(\bar{y}_{SR}) = \frac{100 \times 80}{20 \times 99} \left[ \frac{484.5 \times 3734.74}{20 \times (100)} - (27.82)^2 - 2.27 \right] = 5.78 $$
                    <p>इसलिए, efficiency में मजबूत percentage gain स्पष्ट (unequivocally) रूप से है:</p>
                    $$ \frac{(5.78 - 2.27)}{2.27} \times 100 = 155\% $$
                </div>
            </div>
        </section>
"""

with open("build_ch5_1.py", "w", encoding="utf-8") as f:
    f.write("content = r\"\"\"" + content.replace('\"\"\"', '\\"\\"\\"') + "\"\"\"\n")
