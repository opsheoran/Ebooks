**4. SYSTEMATIC RANDOM SAMPLING (व्यवस्थित यादृच्छिक प्रतिचयन)**

**4.1 INTRODUCTION (परिचय)**

पिछले अध्यायों (chapters) में हमने उन sampling techniques पर चर्चा की है जहाँ
sampling units को randomly (यादृच्छिक रूप से) चुना गया था। अब हम एक ऐसी
sampling technique पर चर्चा करेंगे जिसमें सिर्फ एक random start के साथ पूरे sample
को select करने की एक अच्छी विशेषता (nice feature) है। एक sampling technique
जिसमें केवल पहली unit को random numbers की मदद से select किया जाता है और बाकी
units किसी पूर्व-निर्धारित पैटर्न (pre-designed pattern) के अनुसार अपने आप
(automatically) select हो जाती हैं, **systematic random sampling**
(व्यवस्थित यादृच्छिक प्रतिचयन) कहलाती है। Systematic random sampling को संक्षेप
(briefly) में **systematic sampling** भी कहा जाता है।

मान लीजिए कि population की $N$ units को किसी क्रम में 1 से $N$ तक number
दिया गया है। मान लीजिए $N = nk$, जहाँ $n$ sample size है और $k$ एक पूर्णांक
(integer) है, और $k$ से कम या उसके बराबर एक random number select किया जाता
है और उसके बाद हर $k$-वीं unit को select किया जाता है। परिणामी sample
(resultant sample) को **every** $k$**th systematic sample** कहा जाता है
और ऐसी procedure को **linear systematic sampling** (रैखिक व्यवस्थित
प्रतिचयन) कहा जाता है। यदि $N \neq nk$ है, और हर $k$-वीं unit को एक गोलाकार
तरीके (circular manner) से तब तक शामिल किया जाता है जब तक कि पूरी list समाप्त
(exhaust) न हो जाए, तो इसे **circular systematic sampling** (वृत्ताकार
व्यवस्थित प्रतिचयन) कहा जाएगा।

Systematic sampling सरल और अचूक (foolproof) है। इसकी सरलता के अलावा, यह
procedure कई स्थितियों में, simple random sampling की तुलना में अधिक efficient
(कुशल) estimates प्रदान करती है और विभिन्न प्रकार के surveys में व्यापक रूप से
उपयोग की जाती है। Systematic sampling पर Madow और Madow (1944), Madow
(1949, 1953) और अन्य लोगों द्वारा विस्तार से चर्चा की गई है। विभिन्न क्षेत्रों में इसके
applications को Finney (1948) और Sukhatme et al. (1958) द्वारा प्रदर्शित
(demonstrated) किया गया है। Singh et al. (1968) ने एक modified systematic
sampling procedure का सुझाव दिया है और दूध की उपज (milk yield) का estimate
लगाने के लिए एक survey में इसके application द्वारा इसकी उपयुक्तता (suitability)
को दर्शाया गया है।

**4.2 SAMPLE SELECTION PROCEDURES (प्रतिदर्श चयन की प्रक्रियाएं)**

Systematic sampling एक आमतौर पर इस्तेमाल की जाने वाली technique है यदि एक
पूरा और up-to-date sampling frame उपलब्ध कराया जाता है। हम पहले इन sample
selection procedures पर चर्चा करेंगे इससे पहले कि हम उनके फायदों (advantages) और
नुकसानों (disadvantages) का मूल्यांकन (evaluate) करें।

**4.2.1 Linear Systematic Sampling (रैखिक व्यवस्थित प्रतिचयन)**

जैसा कि ऊपर उल्लेख किया गया है, एक सामान्य procedure linear systematic
sampling scheme है। हम मानते हैं कि population किसी तरह से रैखिक रूप से क्रमित
(linearly ordered) है ताकि units को बिना किसी अस्पष्टता (ambiguity) के
number द्वारा संदर्भित (referred) किया जा सके। इसके अलावा, मान लीजिए $N$ को
$N = nk$ के रूप में व्यक्त (expressible) किया जा सकता है और मान लीजिए कि
selected random number $i$ ($\leq k$) है, जहाँ $k$ को **sampling
interval** (प्रतिचयन अंतराल) कहा जाता है। इस procedure में, sample में units
$i,i + k,i + 2k,\ldots,i + (n - 1)k$ शामिल होती हैं। यह technique समान
probability के साथ $k$ systematic samples उत्पन्न करेगी जिन्हें नीचे दिए गए
schematic diagram में दिखाया जा सकता है:

**Table 4.2.1** Schematic diagram showing $k$ systematic samples in the
population (जनसंख्या में $k$ व्यवस्थित प्रतिदर्शों को दर्शाने वाला योजनाबद्ध आरेख)

  ---------------------------------------------------------------------------------------------------------------------------------
  Sample Number  1                      2                      $$\ldots$$   $$i$$                  $$\ldots$$   $$k$$
  -------------- ---------------------- ---------------------- ------------ ---------------------- ------------ -------------------
                 $$y_{1}$$              $$y_{2}$$              $$\ldots$$   $$y_{i}$$              $$\ldots$$   $$y_{k}$$

                 $$y_{1 + k}$$          $$y_{2 + k}$$          $$\ldots$$   $$y_{i + k}$$          $$\ldots$$   $$y_{2k}$$

                 $$y_{1 + 2k}$$         $$y_{2 + 2k}$$         $$\ldots$$   $$y_{i + 2k}$$         $$\ldots$$   $$y_{3k}$$

                 $$\vdots$$             $$\vdots$$             $$\ldots$$   $$\vdots$$             $$\ldots$$   $$\vdots$$

                 $$y_{1 + (j - 1)k}$$   $$y_{2 + (j - 1)k}$$   $$\ldots$$   $$y_{i + (j - 1)k}$$   $$\ldots$$   $$y_{jk}$$

                 $$\vdots$$             $$\vdots$$             $$\ldots$$   $$\vdots$$             $$\ldots$$   $$\vdots$$

                 $$y_{1 + (n - 1)k}$$   $$y_{2 + (n - 1)k}$$   $$\ldots$$   $$y_{i + (n - 1)k}$$   $$\ldots$$   $$y_{nk}$$

  **Mean**       $${\bar{y}}_{1}$$      $${\bar{y}}_{2}$$      $$\ldots$$   $${\bar{y}}_{i}$$      $$\ldots$$   $${\bar{y}}_{k}$$
  ---------------------------------------------------------------------------------------------------------------------------------

एक और व्यावहारिक स्थिति (practical situation) यह है कि $N$, $N = nk$ के रूप में
expressible नहीं है। इस मामले में, वर्तमान sampling scheme असमान आकार (unequal
size) के samples को जन्म देगी, $k$ को $N/n$ के निकटतम पूर्णांक (nearest
integer) के रूप में लिया जाता है। फिर 1 से $k$ तक एक random number चुना जाता है
और sample में हर $k$-वीं unit को निकाला जाता है। इस शर्त (condition) के तहत,
sample size जरूरी नहीं कि $n$ हो और कुछ मामलों में यह $(n - 1)$ हो सकता है।
उदाहरण के लिए, यदि $N = 11$, $n = 4$ है, तो $k$ का value 3 है और possible
samples $(1,4,7,10)$; $(2,5,8,11)$ और $(3,6,9)$ हैं, जो समान आकार के नहीं हैं।
हम अगले section में इसके सुधार (improvement) पर चर्चा करेंगे।

**4.2.2 Circular Systematic Sampling (वृत्ताकार व्यवस्थित प्रतिचयन)**

स्थिति $N \neq nk$ के तहत अलग-अलग sample size की कठिनाई को दूर करने के लिए,
procedure को थोड़ा modify किया जाता है जिसके द्वारा हमेशा एक constant (स्थिर)
size का sample प्राप्त होता है। इस procedure में एक random start द्वारा 1 से
$N$ तक एक unit को select करना और उसके बाद हर $k$-वीं unit को select करना
शामिल है, जहाँ $k$, $N/n$ के निकटतम पूर्णांक है, एक गोलाकार तरीके (circular
manner) में, जब तक कि $n$ units का sample प्राप्त न हो जाए। इस technique को
आमतौर पर **circular systematic sampling** के रूप में जाना जाता है। मान लीजिए
कि random number $i$ वाली एक unit select की गई है। तब sample में serial
numbers के अनुरूप units शामिल होंगी

$$\begin{matrix}
i + jk & \ \text{if~}i + jk \leq N \\
i + jk - N & \ \text{if~}i + jk > N
\end{matrix}$$

$j = 0,1,\ldots,(n - 1)$ के लिए।

यह आसानी से verify किया जा सकता है कि इस method में प्रत्येक unit के selection
की probability $(1/N)$ समान (equal) है।

एक उदाहरण के रूप में, मान लीजिए $N = 11$, और $n = 4$ है। तो $k = 3$ है।

इसलिए possible samples हैं,

$(1,4,7,10)$; $(2,5,8,11)$; $(3,6,9,1)$; $(4,7,10,2)$; $(5,8,11,3)$;
$(6,9,1,4)$; $(7,10,2,5)$; $(8,11,3,6)$; $(9,1,4,7)$; $(10,2,5,8)$; और
$(11,3,6,9)$।

इसके अलावा, यह देखा जाएगा कि systematic sampling में single sample के साथ
sampling variance का एक unbiased estimate न देने की कमी (drawback) है। इस
कठिनाई को दूर करने के लिए, Singh और Singh (1977) द्वारा एक नई systematic
sampling procedure का सुझाव दिया गया है, जिसे हम इस अध्याय के Section 4.9 में
समझाएंगे।

**4.3 ADVANTAGES AND DISADVANTAGES (लाभ और हानियां)**

Systematic sampling का मुख्य लाभ इसके selection की सरलता, operational
convenience (परिचालन सुविधा) और population पर sample का समान फैलाव (even
spread) है। इसलिए, लकड़ी (timber) की मात्रा का estimate लगाने के लिए वन
सर्वेक्षणों (forest surveys) में, मछली की कुल पकड़ का estimate लगाने के लिए मत्स्य
पालन (fisheries) में, स्तनपान उपज (lactation yield) का estimate लगाने के लिए
दूध की उपज के सर्वेक्षणों (milk yield surveys) में, इसे बहुत उपयोगी पाया गया है। एक
और फायदा यह है कि, periodicities (आवधिकता) वाली populations को छोड़कर,
systematic sampling alternative designs की तुलना में अधिक efficient
estimate प्रदान करती है। कभी-कभी systematic sampling variances, strata के
भीतर units के random selection के लिए variances से बहुत छोटे होते हैं।

Population में periodicity (आवधिकता) के मामले में, systematic sampling का
उपयोग बहुत सावधानी के साथ किया जाना चाहिए। यदि, periodic population के लिए,
sampling interval चक्र की आधी अवधि (half the period of the cycle) का एक
विषम गुणज (odd multiple) है, तो systematic sampling शून्य variance (zero
variance) प्रदान करती है। जब sampling interval चक्र की अवधि का एक सरल गुणज
(simple multiple) होता है, तो systematic sampling random तौर पर एक unit
select करने से बेहतर नहीं होती है। Systematic sampling का एक गंभीर नुकसान
(serious disadvantage) अप्रत्याशित (unforeseen) periodicity वाले
populations के साथ इसके उपयोग में निहित है जो population mean value के
estimate में काफी bias (पूर्वाग्रह) का योगदान दे सकता है। एक और नुकसान single
sample के साथ estimators के sampling variance का estimate लगाने की कमी से
संबंधित है।

**4.4 ESTIMATION OF MEAN AND ITS SAMPLING VARIANCE (माध्य और उसके प्रतिचयन
प्रसरण का अनुमान)**

मान लीजिए $y_{ij}$, $i$-वें systematic sample के $j$-वें सदस्य (member) को
दर्शाता है, ($j = 1,2,\ldots n$; $i = 1,2,\ldots,k$)। $i$-वें sample के mean
को ${\bar{y}}_{i}$ द्वारा दर्शाया जा सकता है। हमें दो अलग-अलग स्थितियों के तहत
population mean का estimate लगाने की समस्या पर विचार करना होगा: (i) जब
$N = nk$ और (ii) जब $N \neq nk$। पहले हम उस स्थिति पर चर्चा करेंगे जब $N = nk$
हो।

**Theorem 4.4.1:** Interval $k$ के साथ systematic sampling में, sample mean
${\bar{y}}_{sy}$ population mean $\bar{Y}$ का एक unbiased estimator
(अभिनत आकलक) है। इसका sampling variance इस प्रकार दिया गया है

$$V({\bar{y}}_{sy}) = \frac{(k - 1)S_{c}^{2}}{k}\ (4.4.1)$$

जहाँ $S_{c}^{2}$ population में column means के बीच mean square को दर्शाता है
($c$, column के लिए है)।

**Proof (प्रमाण):** चूँकि $i$-वें systematic sample के selection की
probability $1/k$ है, हमारे पास है

$$E({\bar{y}}_{sy}) = \sum_{i = 1}^{k}\mspace{2mu}\frac{{\bar{y}}_{i}}{k} = \frac{\sum_{i}^{}\mspace{2mu}\mspace{2mu}\sum_{j}^{}\mspace{2mu}\mspace{2mu} y_{ij}}{nk} = \bar{Y}$$

अतः, ${\bar{y}}_{sy}$ एक unbiased estimator है।

यदि $i$-वें sample को $i$-वां column माना जाता है, तो column means के कारण
squares का total sum इस प्रकार दिया जाता है

$$\sum_{i = 1}^{k}\mspace{2mu}({\bar{y}}_{i} - \bar{Y})^{2} = (k - 1)S_{c}^{2}$$

अतः, sample means ${\bar{y}}_{sy}$ का variance इस प्रकार दिया जाता है

$$V({\bar{y}}_{sy}) = \frac{E({\bar{y}}_{i} - \bar{Y})^{2}}{k} = \frac{(k - 1)S_{c}^{2}}{k}$$

उपरोक्त सूत्र (formula) से यह निष्कर्ष (inferred) नहीं निकाला जाना चाहिए कि यदि
sample size बढ़ाया जाता है तो systematic sample mean का variance कम हो
जाएगा। यह इस बात को स्पष्ट करता है कि systematic sampling एक नाजुक उपकरण
(delicate device) है और इसका उपयोग सावधानी से किया जाना चाहिए।

**Theorem 4.4.2:** Sample mean ${\bar{y}}_{sy}$ का sampling variance इस
प्रकार दिया गया है

$$V({\bar{y}}_{sy}) = \frac{(N - 1)S^{2}}{N} - \frac{(n - 1)S_{w}^{2}}{n} = \sigma^{2} - \sigma_{w}^{2}\ (4.4.2)$$

जहाँ

$$S_{w}^{2} = \frac{\sum_{i}^{}\mspace{2mu}\mspace{2mu}\sum_{j}^{}\mspace{2mu}\mspace{2mu}(y_{ij} - {\bar{y}}_{i})^{2}}{k(n - 1)}$$

$(n - 1)S_{w}^{2} = n\sigma_{w}^{2}$ के साथ, और $\sigma^{2}$ का अपना
सामान्य अर्थ (usual meaning) है।

**Proof (प्रमाण):** हम जानते हैं कि total sum of squares इस प्रकार दिया गया है

$$TSS = (N - 1)S^{2} = \sum_{i}^{}\mspace{2mu}\sum_{j}^{}\mspace{2mu}(y_{ij} - {\bar{y}}_{i})^{2} + n\sum_{i}^{}\mspace{2mu}({\bar{y}}_{i} - \bar{Y})^{2}$$

साथ ही, हम जानते हैं कि ${\bar{y}}_{sy}$ का variance है

$$V({\bar{y}}_{sy}) = \frac{\sum_{i}^{}\mspace{2mu}\mspace{2mu}({\bar{y}}_{i} - \bar{Y})^{2}}{k}$$

और

$$(N - 1)S^{2} = k(n - 1)S_{w}^{2} + nkV({\bar{y}}_{sy})$$

अतः,

$$V({\bar{y}}_{sy}) = \frac{(N - 1)S^{2}}{N} - \frac{(n - 1)S_{w}^{2}}{n} = \sigma^{2} - \sigma_{w}^{2}$$

चूँकि दी गई population के लिए $\sigma^{2}$ fixed (निश्चित) है, यह इस result से
स्पष्ट है कि $V({\bar{y}}_{sy})$ को कम करने के लिए within-sample variation
(नमूने के भीतर भिन्नता) को बढ़ाना आवश्यक है।

**4.5 COMPARISON OF SYSTEMATIC WITH RANDOM SAMPLING (यादृच्छिक प्रतिचयन के
साथ व्यवस्थित प्रतिचयन की तुलना)**

Simple random sampling की तुलना में systematic sampling की relative
efficiency (सापेक्ष दक्षता) का अध्ययन intra-class correlation coefficient
(अंतर-वर्ग सहसंबंध गुणांक) पर विचार करके किया जा सकता है। यह दिखाया जा सकता है कि

$$V({\bar{y}}_{sy}) = \frac{(nk - 1)S^{2} + \rho(nk - 1)(n - 1)S^{2}}{nk} = \frac{(nk - 1)S^{2}\lbrack 1 + (n - 1)\rho\rbrack}{nk}\ (4.5.1)$$

जहाँ $\rho$ एक ही systematic sample की units के बीच intra-class
correlation है और इसे इस प्रकार परिभाषित (defined) किया गया है

$$\rho = \frac{E(y_{ij} - \bar{Y})(y_{ij'} - \bar{Y})}{E(y_{ij} - \bar{Y})^{2}} = \frac{\sum_{i}^{}\mspace{2mu}\mspace{2mu}\sum_{j \neq j'}^{}\mspace{2mu}\mspace{2mu}(y_{ij} - \bar{Y})(y_{ij'} - \bar{Y})}{nk(n - 1)(nk - 1)S^{2}/nk}\ (4.5.2)$$

Relation (4.5.1) से यह देखा जा सकता है कि एक ही sample में units के बीच एक
positive correlation estimate के sampling variance को बढ़ा (inflates) देता
है। Term $(n - 1)$ के कारण छोटे positive correlation के लिए भी यह वृद्धि काफी
significant (महत्वपूर्ण) है। चूँकि $S^{2}$ एक दी गई population के लिए fixed है,
उपरोक्त relation से यह स्पष्ट है कि $\rho$ की अधिकतम संभव negative (नकारात्मक)
value वाली व्यवस्था (arrangement) को प्राथमिकता (preferred) दी जानी चाहिए।
यह फिर से इसी निष्कर्ष पर ले जाता है कि एक ही systematic sample के भीतर units
अध्ययन किए जा रहे characteristic के संबंध में यथासंभव heterogeneous (विषम) होनी
चाहिए। चूँकि $V_{sy}$ कभी शून्य से कम नहीं होता है, $\rho$, $- 1/(n - 1)$ से कम
नहीं हो सकता है। इस प्रकार $\rho$ का न्यूनतम मान (minimum value)
$- 1/(n - 1)$ है और इस मामले में $V_{sy} = 0$ है।

Simple random mean के साथ systematic sample mean की relative precision इस
प्रकार दी गई है

$$\frac{V_{sr}}{V_{sy}} = \frac{N - 1}{N - n}\lbrack 1 + \rho(n - 1)\rbrack\ (4.5.3)$$

यह देखा जा सकता है कि relative precision $\rho$ के value पर निर्भर करती है।
$\rho = - 1/(N - 1)$ के लिए, दोनों methods समान precision के estimates देते
हैं; $\rho < - 1/(N - 1)$ के लिए, systematic sample पर आधारित estimate अधिक
precise है; जबकि यदि $\rho > - 1/(N - 1)$ है, तो यह उल्टा (reverses) हो
जाता है। $\rho$ जो अधिकतम value प्राप्त कर सकता है वह 1 है, जब systematic
sampling की relative precision $(k - 1)/(N - 1)$ द्वारा दी जाती है।

**4.6 COMPARISON OF SYSTEMATIC WITH STRATIFIED RANDOM SAMPLING (स्तरीकृत
यादृच्छिक प्रतिचयन के साथ व्यवस्थित की तुलना)**

मान लीजिए कि $N = nk$ units की population को Table 4.1 में schematic
diagram की $n$ rows के अनुरूप $n$ strata में विभाजित किया गया है और प्रत्येक
stratum से एक unit randomly निकाली जाती है, इस प्रकार size $n$ का एक
stratified sample प्राप्त होता है। तब $j$-वें stratum का mean है

$${\bar{y}}_{\cdot j} = \frac{1}{k}\sum_{i = 1}^{k}\mspace{2mu} y_{ij},\ (j = 1,2,\ldots,n)\ (4.6.1)$$

और population mean है

$$\bar{Y} = \frac{\sum_{i}^{}\mspace{2mu}\mspace{2mu}\sum_{j}^{}\mspace{2mu}\mspace{2mu} y_{ij}}{nk} = \frac{\sum_{j}^{}\mspace{2mu}\mspace{2mu}\sum_{i}^{}\mspace{2mu}\mspace{2mu} y_{ij}}{nk} = \frac{1}{n}\sum_{j}^{}\mspace{2mu}{\bar{y}}_{\cdot j}$$

इसी तरह, $j$-वें stratum (row) के भीतर units का stratum mean square इस
प्रकार परिभाषित किया गया है

$$S_{\cdot j}^{2} = \frac{\sum_{i = 1}^{k}\mspace{2mu}\mspace{2mu}(y_{ij} - {\bar{y}}_{\cdot j})^{2}}{k - 1},\ (j = 1,2,\ldots,n)\ (4.6.2)$$

अतः, stratum के भीतर units के बीच pooled mean square इस प्रकार परिभाषित
किया गया है

$$S_{wst}^{2} = \frac{\sum_{j}^{}\mspace{2mu}\mspace{2mu}\sum_{i}^{}\mspace{2mu}\mspace{2mu}(y_{ij} - {\bar{y}}_{\cdot j})^{2}}{n(k - 1)} = \frac{1}{n}\sum_{j}^{}\mspace{2mu} S_{\cdot j}^{2}\ (4.6.3)$$

स्पष्ट रूप से, इस stratified sample के mean का variance होगा

$$V_{st}(\bar{y}) = \frac{(k - 1)S_{wst}^{2}}{nk} = (1 - f)\frac{S_{wst}^{2}}{n}\ (4.6.4)$$

अब हम एक comparative study (तुलनात्मक अध्ययन) के लिए एक उपयुक्त रूप (suitable
form) में systematic sample के variance को व्यक्त करेंगे। Equation (4.4.1) को इस
प्रकार लिखा जा सकता है

$$V({\bar{y}}_{sy}) = \frac{1}{n^{2}k}\sum_{i}^{}\mspace{2mu}\left\lbrack \sum_{j}^{}\mspace{2mu}\mspace{2mu} y_{ij} - \sum_{j}^{}\mspace{2mu}\mspace{2mu}{\bar{y}}_{\cdot j} \right\rbrack^{2} = \frac{1}{n^{2}k}\left\lbrack \sum_{i}^{}\mspace{2mu}\mspace{2mu}\sum_{j}^{}\mspace{2mu}\mspace{2mu}(y_{ij} - {\bar{y}}_{\cdot j})^{2} + \sum_{i}^{}\mspace{2mu}\mspace{2mu}\sum_{j \neq j'}^{}\mspace{2mu}\mspace{2mu}(y_{ij} - {\bar{y}}_{\cdot j})(y_{ij'} - {\bar{y}}_{\cdot j'}) \right\rbrack$$

$$= \frac{1}{n^{2}k}\left\lbrack n(k - 1)S_{wst}^{2} + n(n - 1)(k - 1)\rho_{wst}S_{wst}^{2} \right\rbrack$$

$$= \frac{(k - 1)S_{wst}^{2}\lbrack 1 + (n - 1)\rho_{wst}\rbrack}{nk}\ (4.6.5)$$

जहाँ $\rho_{wst}$ एक non-circular serial correlation coefficient है जिसे इस
प्रकार परिभाषित किया गया है

$$\rho_{wst} = \frac{E({\bar{y}}_{\cdot j} - \bar{Y})({\bar{y}}_{\cdot j'} - \bar{Y})}{E({\bar{y}}_{\cdot j} - \bar{Y})^{2}} = \frac{\sum_{j}^{}\mspace{2mu}\mspace{2mu}\sum_{j' \neq j}^{}\mspace{2mu}\mspace{2mu}\lbrack({\bar{y}}_{\cdot j} - \bar{Y})({\bar{y}}_{\cdot j'} - \bar{Y})\rbrack}{(n - 1)n(k - 1)S_{wst}^{2}}\ (4.6.6)$$

Relations (4.6.4) और (4.6.5) की तुलना करने पर, हमें मिलता है

$$R.P. = \frac{V_{st}}{V_{sy}} = \lbrack 1 + (n - 1)\rho_{wst}\rbrack^{- 1}\ (4.6.7)$$

इस प्रकार हम देखते हैं कि stratified random sampling की तुलना में systematic
sampling की relative precision $\rho_{wst}$ के values पर निर्भर करती है।
यदि $\rho_{wst}$ positive है तो stratified random sampling $\bar{Y}$ का
एक बेहतर estimate प्रदान करेगी। हालाँकि, यदि $\rho_{wst} = 0$ है, तो यह
निष्कर्ष निकाला जा सकता है कि systematic sampling और stratified random
sampling दोनों समान रूप से अच्छे हैं।

**Example 4.1:** पटना के सरकारी मवेशी फार्म (Government Cattle Farm) में रखे
गए थारपारकर झुंड (Tharparkar herd) से संबंधित एक specific गाय के पहले स्तनपान
(first lactation) के दैनिक दूध की उपज (daily milk yield) (लीटर में) के रिकॉर्ड
नीचे दिए गए हैं। पहले पांच दिनों की दूध की उपज दर्ज (recorded) नहीं की गई थी,
क्योंकि यह कोलोस्ट्रम अवधि (colostrum period) थी।

**Table: Daily milk yield records (203 days) (दैनिक दूध उपज रिकॉर्ड (203
दिन))**

+-----------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| Day                         | 1-10                              | 11-20                             | 21-30                             | 31-40                         | 41-50                         | 51-60                         | 61-70                         | 71-80                         | 81-90                         |
+:==========+:================+:================+:================+:================+:================+:================+:================+:==============================+:==============================+:==============================+:==============================+:==============================+:==============================+
| **Yield**                   | 10,11,14,10,14,9,10,8,11,10       | 6,9,8,7,9,10,11,11,13,12          | 12,10,11,11,14,15,12,17,18,16     | 13,14,14,15,16,16,16,13,16,17 | 14,16,15,14,14,15,17,15,16,17 | 25,22,23,19,18,16,22,21,21,23 | 21,19,19,19,19,19,19,19,19,19 | 18,19,21,20,17,16,18,18,18,22 | 22,22,20,20,20,18,20,21,21,20 |
+-----------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| Day                         | 91-100                            | 101-110                           | 111-120                           | 121-130                       | 131-140                       | 141-150                       | 151-160                       | 161-170                       | 171-180                       |
+-----------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| \-\--                       | \-\--                             | \-\--                             | \-\--                             | \-\--                         | \-\--                         | \-\--                         | \-\--                         | \-\--                         | \-\--                         |
+-----------------------------+-----------------------------------+-----------------------------------+-----------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| **Yield**                   | 18,21,22,22,20,21,21,21,21,21     | 19,20,21,20,21,20,21,20,21,20     | 19,21,18,21,20,22,21,21,21,16     | 19,15,15,16,19,12,16,14,15,17 | 16,20,15,19,16,16,20,20,18,21 | 22,22,21,22,21,21,21,18,20,17 | 20,20,21,21,21,20,20,16,16,15 | 18,19,18,20,19,18,16,14,14,13 | 16,16,16,18,16,15,16,18,18,15 |
+-----------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| Day       | 181-190                           | 191-200                           | 201-203                           |                 |                               |                               |                               |                               |                               |                               |
+-----------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| \-\--     | \-\--                             | \-\--                             | \-\--                             |                 |                               |                               |                               |                               |                               |                               |
+-----------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| **Yield** | 18,16,17,18,17,16,13,14,13,12     | 16,10,13,8,8,6,8,9,4,5            | 6,6,4                             |                 |                               |                               |                               |                               |                               |                               |
+-----------+-----------------------------------+-----------------------------------+-----------------------------------+-----------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+

गाय की स्तनपान उपज (lactation yield) का estimate लगाने में, corresponding
simple random sampling के संबंध में, रिकॉर्डिंग के 7 और 14 दिनों के interval के साथ
systematic sampling की efficiency ज्ञात कीजिए।

इसलिए
$\bar{Y} = \frac{1}{7}\sum_{i}^{}\mspace{2mu}{\bar{y}}_{i} = 3370$।

Random start $i = 5$ लेते हुए, हमें 5-वां sample मिलता है।

इस मामले में, total milk yield का unbiased estimate इस प्रकार दिया गया है

$${\widehat{Y}}_{sy} = 7 \times 486 = 3402$$

Population total estimate के लिए systematic sampling का variance इस प्रकार
दिया गया है

$$V({\widehat{Y}}_{sy}) = \frac{N^{2}}{k}\sum_{i = 1}^{k}\mspace{2mu}({\bar{y}}_{i} - \bar{Y})^{2} = \frac{203^{2}}{7}\lbrack{16.45}^{2} + {17.07}^{2} + \ldots + {16.03}^{2}\rbrack - \frac{3370^{2}}{7} = 5192$$

Total milk yield के simple random sample estimate का variance इस प्रकार
दिया गया है

$$V({\widehat{Y}}_{sr}) = N^{2}(1 - f)\frac{S^{2}}{n}$$

जहाँ
$S^{2} = \frac{1}{N - 1}\sum_{i = 1}^{N}\mspace{2mu}(y_{i} - \bar{Y})^{2}$

$$V({\widehat{Y}}_{sr}) = (203)^{2}\left( 1 - \frac{7}{203} \right) \times \frac{3865.7228}{28} = 23194.33$$

इस प्रकार, simple random sampling की तुलना में systematic sampling की
relative precision होगी

$$\frac{23194.33}{5192} \times 100 = 446.73\%$$

\(ii\) $N = 203$ और $k = 14$ के लिए, हमारे पास $n = 15$ या $14$ है।\
एक random start $i = 10$ लेते हुए, हमें 10-वां sample मिलता है। इस मामले में,
total milk yield का unbiased estimate इस प्रकार दिया गया है

$${\widehat{Y}}_{sy} = 14 \times 246 = 3444$$

इसका variance इस प्रकार दिया गया है

$$V({\widehat{Y}}_{sy}) = \frac{N^{2}}{k}\sum_{i = 1}^{k}\mspace{2mu}{\bar{y}}_{i}^{2} - {\bar{Y}}^{2} = 14 \times \frac{812028}{14} - (2270)^{2} = 11492$$

Total milk yield के एक simple random sample estimate का variance होगा

$$V({\widehat{Y}}_{sr}) = N^{2}\left( \frac{1}{k} - \frac{1}{N} \right)S^{2} = (203)^{2}\left( \frac{1}{14} - \frac{1}{203} \right) \times \frac{3865.7228}{202} = 52187.2578$$

इसलिए, simple random sample estimate पर systematic estimate की relative
precision है

$$\frac{52187.2578 \times 100}{11492} = 454.12\%$$

**4.7 ESTIMATION OF VARIANCE (प्रसरण का अनुमान)**

एक random start वाले systematic sample के लिए variance का एक unbiased
estimate उपलब्ध नहीं है क्योंकि एक systematic sample को एक unit (cluster) का
random sample माना जाता है। हालाँकि, एक systematic sample के आधार पर कुछ
biased estimators संभव हैं। यदि दो या दो से अधिक systematic samples उपलब्ध हैं,
तो estimated mean के variance का एक unbiased estimate बनाया जा सकता है।

मान लीजिए $m$ independent systematic samples उपलब्ध हैं, जिनमें से प्रत्येक का
size $n$ है। तब, variance का एक unbiased estimate इस प्रकार दिया जाता है

$$v({\bar{y}}_{sy}) = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu}({\bar{y}}_{i} - {\bar{y}}_{sy})^{2}}{m(m - 1)}\ (4.7.1)$$

जहाँ
${\bar{y}}_{sy} = \frac{1}{m}\sum_{i = 1}^{m}\mspace{2mu}{\bar{y}}_{i}$
है।

एक systematic sample mean के variance का एक अनुमानित (approximate) और
biased estimate इस प्रकार दिया जाता है

$$v({\bar{y}}_{sy}) = \frac{(1 - f)}{n} \times S_{wc}^{2}\ (4.7.2)$$

जहाँ
$S_{wc}^{2} = \frac{\sum_{i = 1}^{n - 1}\mspace{2mu}\mspace{2mu}(y_{i} - y_{i + 1})^{2}}{2(n - 1)}$
है।

एक systematic sample mean के variance का एक और approximate और biased
estimate इस प्रकार दिया जाता है

$$v({\bar{y}}_{sy}) = \frac{(1 - f)}{N} \times \frac{\sum_{i = 1}^{n - 1}\mspace{2mu}\mspace{2mu}(y_{i} - y_{i + 1})^{2}}{2(n - 1)}\ (4.7.3)$$

Relations (4.7.2) और (4.7.3) द्वारा दिए गए ये estimators biased हैं और इनका
उपयोग सावधानी के साथ किया जाना चाहिए अन्यथा वे व्यवहार (practice) में भ्रामक
(misleading) परिणाम प्रदान कर सकते हैं। इसलिए, संपूर्ण data का उपयोग करके प्राप्त
sampling variance के साथ इसकी तुलना करके एक विशिष्ट मामले (specific case) में
bias का विचार (idea) प्राप्त करना वांछनीय (desirable) है। ये estimators
Cochran (1946) और Yates (1948) द्वारा दिए गए परिणामों पर आधारित हैं।

**Example 4.2:** 1967-68 के दौरान यूपी (भारत) के मेरठ जिले के लोनी ब्लॉक में
I.A.S.R.I., नई दिल्ली द्वारा की गई एक प्रायोगिक कृषि जनगणना (experimental
agricultural census) में, ब्लॉक के दो गाँवों को randomly select किया गया था।
दो गाँवों, अर्थात् पंच-लोक और अग्रोला में 225 जोतों (holdings) में से, 45 जोतों को
systematic sampling (sampling interval के रूप में 5 के साथ) द्वारा select किया
गया था। 45 selected जोतों के लिए कुल कृषि योग्य भूमि (total arable land) (कच्चा
बीघा में)\* नीचे दी गई है:

**Table 4.7.1: Total arable land for selected holdings (चयनित जोतों के लिए
कुल कृषि योग्य भूमि)**

  -------------------------------------------------------
  S.N.             1    2    3     4     5     6     7
  ---------------- ---- ---- ----- ----- ----- ----- ----
  **Total arable   60   50   14    10    1     0     0
  land**                                             

  S.N.             8    9    10    11    12    13    14

  **Total arable   0    0    0     150   150   100   20
  land**                                             

  S.N.             15   16   17    18    19    20    21

  **Total arable   0    25   192   25    0     13    0
  land**                                             

  S.N.             22   23   24    25    26    27    28

  **Total arable   0    50   0     10    0     0     0
  land**                                             

  S.N.             29   30   31    32    33    34    35

  **Total arable   85   30   30    70    30    35    0
  land**                                             

  S.N.             36   37   38    39    40    41    42

  **Total arable   30   0    0     10    0     20    70
  land**                                             

  S.N.             43   44   45                      

  **Total arable   16   15   35                      
  land**                                             
  -------------------------------------------------------

\*(5 कचा बीघा = 1 एकड़)

दो गाँवों में कुल कृषि योग्य भूमि (total arable land) का estimate लगाएँ और
estimate की approximate standard error का भी।

Total arable land का एक estimate इस प्रकार दिया गया है

$$\widehat{Y} = \frac{N}{n}\sum_{i = 1}^{n}\mspace{2mu} y_{i} = 225 \times \frac{1348}{45} = 6740$$

$\widehat{Y}$ के variance का एक estimate इस प्रकार दिया गया है

$$v(\widehat{Y}) = \frac{N^{2}(1 - f)}{n} \times \frac{\sum_{i = 1}^{n - 1}\mspace{2mu}\mspace{2mu}(y_{i} - y_{i + 1})^{2}}{2(n - 1)}$$

$$= \frac{225^{2} \times (5 - 1)}{45} \times \frac{116845}{2 \times (45 - 1)}$$

$$= 11,950,031.25$$

$\therefore$ $\widehat{Y}$ की Estimated standard error
$= \sqrt{11,950,031.25} = 3456.88$.

**4.8 INTERPENETRATING SYSTEMATIC SAMPLING (अंतर-प्रवेशी व्यवस्थित प्रतिचयन)**

यदि sampling variance का एक कठोर (rigorous) estimate होना आवश्यक है, तो इसे
independent random starts के साथ systematic sub-samples लेकर किया जा सकता
है, जिसमें प्रत्येक में कुल sample size को समान रखने के लिए $n/m$ units शामिल हों।
मान लीजिए कि ${\bar{y}}_{1},{\bar{y}}_{2},\ldots,{\bar{y}}_{m}$, $m$
independent systematic sub-samples पर आधारित estimates हैं। Population
mean का एक unbiased estimator pooled mean है जो इस प्रकार दिया गया है

$$\bar{y} = \frac{1}{m}\sum_{i = 1}^{m}\mspace{2mu}{\bar{y}}_{i}\ (4.8.1)$$

तब, $\bar{y}$ के variance का एक unbiased estimate है

$$v(\bar{y}) = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu}({\bar{y}}_{i} - \bar{y})^{2}}{m(m - 1)}\ (4.8.2)$$

$n/m( = n')$ units के $m$ systematic sub-samples के मामले में, प्रत्येक 1 से
$mk( = k')$ तक random starts के साथ, pooled mean $\bar{y}$ का variance और
estimated variance हैं

$$V(\bar{y}) = \frac{(k' - m)}{k'm(k' - 1)}\sum_{i = 1}^{k'}\mspace{2mu}({\bar{y}}_{i} - \bar{Y})^{2}\ (4.8.3)$$

जहाँ ${\bar{y}}_{i}$, $i$-वां sample mean है ($i = 1,\ldots,k'$) और

$$v(\bar{y}) = \frac{(k' - m)}{k'm(m - 1)}\sum_{i = 1}^{m}\mspace{2mu}({\bar{y}}_{i} - \bar{y})^{2}\ (4.8.4)$$

यद्यपि ये variance estimators unbiased हैं, यदि $m$ छोटा है तो वे कम precise
(सटीक) होते हैं। इसी तरह यदि sub-sample size कम करके $m$ बढ़ाया जाता है, तो
population mean का combined estimator कम efficient होने की संभावना है।
इसलिए, किसी को variance का अच्छा estimate प्राप्त करने की इच्छा या population
mean का अच्छा estimate प्राप्त करने के बीच एक निर्णय (decision) पर पहुंचना होता
है।

**4.9 NEW SYSTEMATIC SAMPLING\* (नया व्यवस्थित प्रतिचयन\*)**

जैसा कि पिछले section में बताया गया है, systematic sampling में single sample के
आधार पर sampling variance का एक unbiased estimator प्रदान करने में सक्षम न
होने की कमी है। Unbiased variance estimator प्राप्त करने का एक संभव तरीका
interpenetrating systematic sampling का उपयोग करना है, लेकिन इसके
परिणामस्वरूप precision और simplicity में कमी आती है। Singh और Singh (1977) ने
एक नई systematic sampling procedure का सुझाव दिया है जो एक unbiased
variance estimator प्रदान करती है। इस section में, हम मुख्य परिणामों (main
results) की रूपरेखा (outlines) पर संक्षेप में चर्चा करेंगे।

मान लीजिए कि एक population में $N$ distinct units हैं और उसमें से size $n$ का
एक sample निकाला जाना है। मान लीजिए $u$ ($\leq n$) और $d$ दो
predetermined (पूर्वनिर्धारित) पूर्णांक (integers) हैं जिन्हें इस तरह चुना जाता है कि
(i) प्रत्येक sample में distinct units हों, और (ii) units के प्रत्येक pair के लिए
inclusion probability गैर-शून्य (non-zero) हो। एक random number
$r( \leq N)$ से शुरू करके, हम लगातार $u$ units select करते हैं, और उसके बाद शेष
$n - u( = v)$ units को interval $d$ के साथ select करते हैं ताकि $d \leq u$
और $u + vd \leq N$ हो। इन प्रतिबंधों (restrictions) के साथ, इस sampling
scheme द्वारा दो या अधिक चरणों (phases) में वांछित (desired) sample size $n$
का एक sample निकाला जा सकता है। यहाँ \'phase\' शब्द का उपयोग इस अर्थ में किया
गया है कि दिए गए size का अंतिम sample चरणों (stages) में select किया जाता है।
$N$ size की population से $n$ units का sample select करने के लिए आवश्यक
phases $p$ की संख्या इस प्रकार दी गई है

$$p \geq \frac{loglog(N/2) - loglog(n/2)}{log2}\ (4.9.1)$$

Selection procedure के अनुरूप sample space में $N$ possible samples होते हैं, और
random number $r$ के अनुरूप sample point $s_{r} = \{ s',s''\}$ द्वारा दिया
जाता है जहाँ $s'$ में unit indices $r + m$ ($m = 0,1,\ldots,u - 1$) शामिल हैं
और $s''$ में unit indices $r + u - 1 + m'd$ ($m' = 1,2,\ldots,v$) शामिल हैं।

प्रत्येक sample को select करने की probability $1/N$ है, और इस प्रकार,
selection procedure से जुड़ी probability measure इस प्रकार दी गई है

$$P = \{ P(s_{r}):P(s_{r}) = 1/N,r = 1,2,\ldots,N\}\ (4.9.2)$$

इस प्रकार, individual units और pairwise units के लिए inclusion
probabilities $\pi_{i}$ और $\pi_{ij}$ द्वारा दी जाती हैं, जो नई systematic
sampling procedure के तहत ज्ञात हैं। इसलिए, population mean का
Horvitz-Thompson estimator सरल होकर यह हो जाता है

$${\bar{y}}_{nsy} = \frac{1}{n}\sum_{i \in s}^{}\mspace{2mu} y_{i} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu} y_{i}\ (4.9.3)$$

Yates-Grundy रूप में estimator ${\bar{y}}_{nsy}$ का sampling variance कम
होकर यह हो जाता है

$$V({\bar{y}}_{nsy}) = \frac{1}{2}\sum_{i}^{}\mspace{2mu}\sum_{j}^{}\mspace{2mu}\frac{(\pi_{i}\pi_{j} - \pi_{ij})}{\pi_{ij}}\left( \frac{y_{i}}{\pi_{i}} - \frac{y_{j}}{\pi_{j}} \right)^{2}\ (4.9.4)$$

जिसे इस प्रकार लिखा जा सकता है

$$V({\bar{y}}_{nsy}) = \frac{N - n}{N}S^{2} - \frac{n - 1}{n}S_{wnsy}^{2}\ (4.9.5)$$

जहाँ
$S_{wnsy}^{2} = \frac{\sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{y})^{2}}{N(n - 1)}$
है।

$V({\bar{y}}_{nsy})$ का एक unbiased estimator इसके द्वारा प्राप्त किया जा
सकता है

$$v({\bar{y}}_{nsy}) = \frac{1}{2}\sum_{i \in s}^{}\mspace{2mu}\sum_{j \in s,j > i}^{}\mspace{2mu}\left( \frac{1}{\pi_{ij}} - \frac{1}{n^{2}} \right)(y_{i} - y_{j})^{2}\ (4.9.6)$$

एक comparative study में, विभिन्न प्रकार की populations पर विचार करके सामान्य
systematic sampling और simple random sampling पर नई systematic sampling
की efficiency की जांच की गई है। इस अध्ययन में यह निष्कर्ष निकाला गया कि कई
प्राकृतिक (natural) populations के लिए, नई systematic sampling सामान्य
systematic sampling की तुलना में बेहतर परिणाम प्रदान करती है।

*\*पहले पठन पर छोड़ा जा सकता है (May be omitted at the first reading)।*

**4.10 COMPARISON OF SYSTEMATIC WITH SIMPLE AND STRATIFIED RANDOM
SAMPLES FOR SOME SPECIFIED POPULATIONS (कुछ निर्दिष्ट जनसंख्याओं के लिए सरल और
स्तरीकृत यादृच्छिक प्रतिदर्शों के साथ व्यवस्थित की तुलना)**

Stratified या simple random sampling के संबंध में systematic sampling का
प्रदर्शन (performance) बहुत हद तक population की प्रकृति पर निर्भर करता है जिसमें
अध्ययन किए जा रहे characteristic का केवल units के संदर्भ में कुछ सरल रुझान (simple
trend) होता है। कुछ मुख्य रुझानों (trends) पर नीचे चर्चा की गई है।

**4.10.1 Populations with Linear Trend (रैखिक प्रवृत्ति वाली जनसंख्याएं)**

मान लीजिए population units के values एक linear model के अनुसार बढ़ते हैं जैसे कि

$$y_{i} = a + bi$$

जहाँ $a$ और $b$ constants हैं और $i$, 1 से $N$ तक जाता है।

अतः

$$\bar{Y} = \frac{\sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}(a + bi)}{N} = a + \frac{b(N + 1)}{2}$$

और

$$S^{2} = \frac{\sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y})^{2}}{N - 1} = \frac{b^{2}\sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}\lbrack i - (N + 1)/2\rbrack^{2}}{N - 1} = \frac{b^{2}N(N + 1)}{12}$$

इसलिए

$$V_{sr} = \frac{N - n}{Nn}S^{2} = \frac{(nk - 1)b^{2}}{12} \times \frac{k - 1}{nk} = \frac{(k - 1)(nk + 1)b^{2}}{12}\ (4.10.1)$$

इसी तरह, strata के भीतर variance खोजने के लिए, हमें $N$ के लिए $k$ रखना होगा,
और हमें मिलता है

$$V_{st} = \frac{N - n}{Nn}S_{w}^{2} = \frac{nk - 1}{nk} \times \frac{(k - 1)k(k + 1)b^{2}}{12n} = \frac{(k - 1)(k + 1)b^{2}}{12n}\ (4.10.2)$$

Systematic sampling के लिए, values को Eqn. (4.3.2) में रखा जा सकता है

$$V_{sy} = \frac{1}{k}\sum_{i = 1}^{k}\mspace{2mu}({\bar{y}}_{i} - \bar{Y})^{2} = \frac{b^{2}}{k}\sum_{i = 1}^{k}\mspace{2mu}\left\lbrack i - \frac{k + 1}{2} \right\rbrack^{2} = \frac{b^{2}k(k + 1)(k - 1)}{12k} = \frac{(k - 1)(k + 1)b^{2}}{12}\ (4.10.3)$$

जो यह साबित (proves) करता है

$$V_{st}:V_{sy}:V_{sr} = \left\lbrack \frac{k + 1}{n}:k + 1:nk + 1 \right\rbrack = \frac{1}{n}:1:n = 1:n:n^{2}\ (4.10.4)$$

यह देखा गया है कि एक stratified sample का variance linear trend वाली
population में systematic sample के variance का केवल $1/n$-वां हिस्सा है। इसी
तरह, एक systematic sample का variance एक random sample के variance का
लगभग $1/n$-वां हिस्सा है। इसलिए, linear trend के प्रभाव को खत्म करने के लिए
stratified sampling सभी methods में सबसे efficient है। Linear trend की
उपस्थिति में systematic sampling के प्रदर्शन (performance) को Yates (1948)
द्वारा दिए गए end corrections या Singh et al (1968) के modified method को
लागू करके सुधारा जा सकता है, जो population के सिरों (ends) से समान दूरी
(equidistant) पर units के जोड़े (pairs) चुनता है।

**4.10.2 Populations with Periodic Variations (आवधिक भिन्नता वाली
जनसंख्याएं)**

मान लीजिए population में एक periodic trend (आवधिक प्रवृत्ति) शामिल है जिसे इसके
द्वारा दर्शाया गया है

$$y_{i} = sin\left( \frac{\pi i}{n} \right) + \theta_{i}$$

जहाँ $i$, 0 से $2\pi$ के एक पूर्णांक गुणज (integral multiple) तक बदलता है।
$2\pi = 20$ मान लें, तो क्रमिक (successive) sampling units हर 20-वें value के
बाद खुद को दोहराएंगी।

ऐसी population से पांच प्रतिशत systematic sample में प्रत्येक चक्र (cycle) के समान
स्थान से निकाली गई sampling units शामिल होंगी। ऐसे sample से एक estimate एक
single value जितना ही अच्छा होगा। दूसरी ओर, एक पांच प्रतिशत random sample में
population के विभिन्न भागों से units शामिल होंगी और ऐसे samples से estimates एक
periodic trend के प्रभाव के लिए अधिक precise होंगे। यदि हम 10 प्रतिशत
systematic sample select करते हैं, तो estimate population value के समान अच्छा
होगा, इस प्रकार systematic sampling सभी sampling methods में सबसे precise बन
जाती है। इस प्रकार, periodic trend वाले populations से systematic sampling
की precision, periodicity पर निर्भर करती है। सबसे अनुकूल मामला (most
favourable case) तब होता है जब $k$ आधी अवधि (half period) का एक विषम गुणज
(odd multiple) होता है।

**4.10.3 Natural Populations (प्राकृतिक जनसंख्याएं)**

लकड़ी (timber) की मात्रा, दृढ़ लकड़ी (hardwood) के पौधे (seedlings), विभिन्न
प्रकार के आवरणों (covers) के तहत क्षेत्रों आदि का estimate लगाने के लिए वन क्षेत्रों
(forest areas) जैसी कुछ प्राकृतिक (natural) populations का sample लेने में
systematic sampling परिचालन रूप से सुविधाजनक (operationally convenient) और
कुशल (efficient) दोनों है। Osborne (1942), Yates (1948) और Finney (1948,
1950) ने कुछ प्राकृतिक populations में systematic sampling की relative
efficiency की जांच की है और देखा है कि systematic sampling का प्रदर्शन
(performance) तुलनात्मक रूप से (comparatively) बेहतर रहा था।

**4.10.4 Auto-correlated Populations (स्व-सहसंबंधित जनसंख्याएं)**

यह पहले ही देखा जा चुका है कि simple random sampling या stratified sampling
की तुलना में systematic sampling की efficiency population की प्रकृति (nature)
पर निर्भर करती है। विभिन्न प्राकृतिक populations में, एक दूसरे के करीब की units
बहुत दूर की units की तुलना में अधिक समान होती हैं। ऐसी populations, जिन्हें
auto-correlated populations कहा जाता है, के अध्ययन के लिए, हम मानते हैं कि
observations $y_{i}$ और $y_{j}$ ($i,j = 1,2,\ldots,N$) positively
correlated हैं और serial correlation coefficient $\rho_{d}$ बीच की दूरी
(distance) का एक function है, यानी $d = |i - j|$। मान लीजिए कि units
$y_{i}$ को mean $\mu$ और variance $\sigma^{2}$ के साथ एक अनंत (infinite)
population (जिसे super population कहा जाता है) से निकाला गया है, तो

$$E(y_{i}) = \mu,\ E(y_{i} - \mu)^{2} = \sigma^{2}\ (4.10.5)$$

और

$$E(y_{i} - \mu)(y_{j} - \mu) = \rho_{d}\sigma^{2}$$

$i = 1,2,\ldots,N$ और $d = 1,2,\ldots,(N - 1)$ के लिए जहाँ

$$\rho_{d} \geq \rho_{d'} \geq 0\ \text{जब कभी~}d < d'\text{~हो}$$

$d$ के एक function के रूप में $\rho_{d}$ का ग्राफ correlogram (सहसंबंध आरेख)
कहलाता है। यह देखा गया है कि $d$ के घटने पर $\rho_{d}$ बढ़ता है। Madow और Madow
(1944) ने दिखाया है कि यदि population में units क्रमित (ordered) हैं, तो simple
random sampling के बजाय systematic sampling को अपनाना पर्याप्त है। Cochran
(1946) ने दिखाया है कि यदि, Eqn. (4.10.5) में ली गई मान्यताओं के अलावा, यह माना
जाता है कि

$$\delta_{d} = \rho_{d} + \rho_{d + 2} - 2\rho_{d + 1} \geq 0\ (4.10.6)$$

सभी $d = 2,3,\ldots,(nk - 2)$ के लिए,

तब

$$E(V_{sy}) \leq E(V_{st})\ (4.10.7)$$

Serial correlation coefficients के दूसरे अंतर (second difference) के बारे में
शर्त, $\delta_{d} \geq 0$, का तात्पर्य है कि correlogram ऊपर की ओर अवतल
(concave upwards) है, और ऐसे populations के लिए systematic sampling
stratified sampling की तुलना में अधिक efficient है।

Singh et al (1968) ने विभिन्न मामलों पर चर्चा की है, अर्थात

\(i\) linear trend और random element वाली population,

\(ii\) linear trend और periodic variation वाली population, और

\(iii\) parabolic trend वाली population,

और उन्होंने दिखाया है कि stratified या simple random sampling पर modified
systematic sampling का प्रदर्शन काफी संतोषजनक (satisfactory) है।

**4.11 TWO-DIMENSIONAL SYSTEMATIC SAMPLING (द्वि-आयामी व्यवस्थित प्रतिचयन)**

अब तक हमने one-dimensional (एक-आयामी) systematic sampling पर चर्चा की है
जिसमें population units को एक रेखा (line) पर क्रमिक रूप से व्यवस्थित (serially
ordered) माना जाता है। कई ऐसी स्थितियाँ होती हैं जहाँ population units
स्वाभाविक रूप से एक रेखा के बजाय एक क्षेत्र (area) या समतल (plane) पर व्यवस्थित
होती हैं। ऐसी स्थिति के लिए एक systematic sampling procedure को plane
systematic या two-dimensional systematic sampling के रूप में जाना जाता है।
Two-dimensional plane में एक linear systematic sample का सबसे सरल विस्तार
(simplest extension) लोकप्रिय रूप से squared grid या aligned sample के रूप में
जाना जाता है। Quenouille (1949) और Das (1950) ने two-dimensional
systematic sampling की समस्या पर विस्तार से चर्चा की है। इस section में, हम
संक्षेप में एक two-dimensional systematic sample select करने की एक procedure
का वर्णन करते हैं।

मान लीजिए कि population में समान आकार के $N$ वर्गाकार (square) (या आयताकार -
rectangular) ग्रिड क्षेत्र (grid areas) शामिल हैं और $n$ ग्रिड क्षेत्रों का एक
sample लिया जाना है। यह भी मान लें कि ग्रिड्स को कोशिकाओं (cells) के
$l \times m$ ($= nk = N$) रूप में व्यवस्थित किया गया है और प्रत्येक सेल को $r$
rows और $s$ columns के रूप में व्यवस्थित किया गया है। सबसे सरल तरीका random
numbers $(i,j)$ की एक जोड़ी (pair) का चयन करना है जैसे कि $i \leq r$,
$j \leq s$। इस प्रकार, सेल में एक ग्रिड का random location विशिष्ट रूप से
(uniquely) निर्धारित किया जाता है। इस procedure द्वारा selected एक
systematic sample एक aligned या square-grid sample है और selected ग्रिड्स
को Fig. 4.3 (a) में बिंदुओं (dots) द्वारा दिखाया गया है।

एक अन्य procedure इस प्रकार है: ग्रिड्स को $r \cdot l$ rows और $m \cdot s$
columns के रूप में व्यवस्थित किया गया है और $n = rs$ ग्रिड्स के size का एक
systematic sample select करना आवश्यक है।\
$r$ स्वतंत्र random numbers $i_{1},i_{2},\ldots,i_{r}$ चुनें, जिनमें से प्रत्येक $l$
से कम या उसके बराबर हो; और $s$ स्वतंत्र random numbers
$j_{1},j_{2},\ldots,j_{s}$ चुनें, जिनमें से प्रत्येक $m$ से कम या उसके बराबर हो।
Sample में शामिल ग्रिड्स $(i_{x} + xl,j_{y} + ym)$ हैं
$x = 0,1,\ldots,(r - 1)$ और $y = 0,1,\ldots,(s - 1)$ के लिए।\
इस procedure द्वारा select किए गए sample को unaligned sample के रूप में जाना
जाता है और selected ग्रिड बिंदुओं को Fig. 4.3(b) में बिंदुओं द्वारा दिखाया गया है।

Quenouille (1949) और Das (1950) द्वारा दी गई जांच (investigations) से संकेत
मिलता है कि एक unaligned pattern एक square grid और एक stratified random
sample दोनों से बेहतर होगा। Milne (1959) ने एक central square grid technique
प्रस्तावित (proposed) की है जिसमें sample बिंदु वर्ग (square) के केंद्र में स्थित होता
है। Yates (1960) द्वारा एक two- और three-dimensional lattice sampling
technique पर चर्चा की गई है।

**SET OF PROBLEMS (समस्याओं का समूह)**

**4.1** Systematic sampling क्या है? उन परिस्थितियों (circumstances) को बताएं
जिनके तहत इसे simple random sampling पर प्राथमिकता (preferred) दी जानी
चाहिए। समझाएं कि आप एक random start के साथ systematic sample के variance का
estimate कैसे लगाएंगे।

**4.2** \'Linear\' और \'circular\' systematic sampling procedures का
वर्णन करें और संक्षेप में उनके फायदों (advantages) और नुकसानों (disadvantages) पर
चर्चा करें। Size $N$ की एक finite population में, दिखाएं कि समान probability के
साथ random sampling, wor की तुलना में systematic sampling अधिक efficient
होगी, यदि intra-class correlation coefficient

$$\rho < - \frac{1}{N - 1}.$$

**4.3** उन स्थितियों (situations) पर चर्चा करें जिनके तहत censuses और surveys
में अन्य प्रकार के samples पर systematic samples को प्राथमिकता दी जाती है।
दिखाएं कि एक systematic sample mean, population mean का एक simple random
mean की तुलना में अधिक efficient estimator है, लेकिन एक linear trend वाली
population में stratified random sample mean की तुलना में कम efficient है।

**4.4** $N$ units की population से $n$ units का systematic sample निकालने
की procedure का ठीक-ठीक वर्णन करें, जहाँ $N$ का $n$ का गुणज (multiple) होना
आवश्यक नहीं है। (i) आप population में किसी characteristic के mean का estimate
कैसे लगाएंगे और इसकी unbiasedness (अभिनतता) की जांच कैसे करेंगे? (ii) आप $n$ size
के तीन systematic samples के estimates को एक एकल pooled estimate (एकल
संयोजित अनुमान) में कैसे संयोजित (combine) करेंगे जो unbiased है और इसकी standard
error का estimate कैसे लगाएंगे?

**4.5** $N^{2} = n^{2}k^{2}$ units वाली एक two-dimensional population में,
linear trend $y_{ij} = i + j$ ($i,j = 1,2,\ldots,nk$) द्वारा दिया गया है,
जहाँ $y_{ij}$, $i$-वीं row और $j$-वें column में item value है।\
$n^{2}$ units का एक systematic square grid sample 0 और $k$ के बीच दो
स्वतंत्र random starts $(i,j)$ लेकर और $x,y = 0,1,\ldots,(n - 1)$ के लिए
$(i_{x} + xk,j_{y} + yk)$ लेकर लिया जाता है। दिखाएं कि इस sample के mean में
$n^{2}$ size के sample mean के समान precision है (Cochran, 1977)।

**REFERENCES (संदर्भ)**

Cochran, W.G., \"Comparison of methods for determining stratum
boundaries\", *Bull. Int. Statist. Inst.*, 38, 345-358, (1961).\
Das, M.N., \"On the relative efficiency of systematic sampling\", *Ann.
Math. Statist.*, 21, 456-460, (1950).\
Finney, D.J., \"On the efficiency of systematic sampling\", *J. Agric.
Sci.*, 38, 190-196, (1948). \"The efficiency of systematic sampling in
practice\", *J. Agric. Sci.*, 40, 207-216, (1950).\
Madow, W.G., \"On the theory of systematic sampling\", *Ann. Math.
Statist.*, 14, 333-354, (1943). \"On the theory of systematic sampling
II\", *Ann. Math. Statist.*, 20, 1-18, (1949). \"On the theory of
systematic sampling III\", *Ann. Math. Statist.*, 24, 101-106, (1953).\
Madow, W.G. and L.H. Madow, \"On the theory of systematic sampling\",
*Ann. Math. Statist.*, 15, 1-24, (1944).\
Milne, A., \"The centric systematic area-sample treated as a random
sample\", *Ann. Math. Statist.*, 30, 207-216, (1959).\
Osborne, J.G., \"Efficiency of systematic sampling in a forest survey\",
*J. Forestry*, 40, 865-869, (1942).\
Quenouille, M.H., \"On the comparison of systematic and random
sampling\", *Ann. Math. Statist.*, 20, 456-460, (1949).\
Singh, D., F.S. Chaudhary and R.K. Singh, \"A modified systematic
sampling procedure\", *Biometrics*, 24, 699-704, (1968).\
Singh, R. and S. Singh, \"A new systematic sampling procedure\",
*Biometrical Journal*, 19, 351-356, (1977).\
Sukhatme, P.V., B.V. Sukhatme and S. Sukhatme, *Sampling Theory of
Surveys with Applications*, Iowa State University Press, Ames, Iowa,
(1984).\
Yates, F., \"Systematic sampling\", *Phil. Trans. Roy. Soc. London,
Series A*, 241, 345-377, (1948). *Sampling Methods for Censuses and
Surveys*, Charles Griffin & Co., London, (1960).
