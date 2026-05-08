**2. BASIC METHODS OF SIMPLE RANDOM SAMPLING (सरल यादृच्छिक प्रतिचयन की मूल
विधियां)**

*\"To this end was I born for this cause came I into the world, that I
should bear witness unto the truth . .. Pilate saith unto him \'What is
truth?\'\"*

**St. John** (इस उद्देश्य के लिए मेरा जन्म हुआ, इसी कारण मैं दुनिया में आया, कि मैं
सत्य की गवाही दूँ\... पीलातुस ने उससे कहा \'सत्य क्या है?\')

**2.1 SIMPLE RANDOM SAMPLING (सरल यादृच्छिक प्रतिचयन)**

Sampling का सबसे सरल और आम method simple random sampling है जिसमें sample को
unit by unit निकाला जाता है, और प्रत्येक draw में प्रत्येक unit के selection की
probability (प्रायिकता) समान (equal) होती है। इसलिए, simple random
sampling size $N$ की population में से $n$ units को select करने का एक method
है जिसमें सभी units को समान probability दी जाती है, या यह एक ऐसा sampling
procedure है जिसमें $N$ units की population से बनने वाले $n$ units के सभी
possible combinations के selection की probability समान होती है। इसे कभी-कभी
unrestricted random sampling (अप्रतिबंधित यादृच्छिक प्रतिचयन) भी कहा जाता है।
यदि एक unit को select करके नोट किया जाता है और अगला draw निकालने से पहले उसे
वापस population में लौटा दिया जाता है और यह procedure $n$ बार दोहराई जाती
है, तो यह $n$ units का एक simple random sample देता है। इस procedure को
आमतौर पर **simple random sampling with replacement (wr)** (प्रतिस्थापन के
साथ) के रूप में जाना जाता है। यदि इस procedure को तब तक दोहराया जाता है जब तक
कि $n$ distinct (विशिष्ट) units select न हो जाएं और सभी repetitions
(दोहरावों) को ignore कर दिया जाए, तो इसे **simple random sampling without
replacement (wor)** (प्रतिस्थापन के बिना) कहा जाता है।

**Theorem 2.1.1:** यह probability कि population की एक specified unit
किसी भी दिए गए draw में select होती है, उसके पहले draw में select होने की
probability के बराबर होती है।

**Proof:** यह probability कि specified unit $r$-वें draw में select होती है,
स्पष्ट रूप से (a) इस probability कि specified unit पिछले $(r - 1)$ draws में से
किसी में भी select नहीं होती है, और (b) इस probability कि यह $r$-वें draw में इस
शर्त के साथ select होती है कि यह पिछले $(r - 1)$ draws में select नहीं हुई थी,
का गुणनफल (product) है।

\(a\) के अंतर्गत probability इस प्रकार दी जाती है:

$$\frac{N - 1}{N} \cdot \frac{N - 2}{N - 1}\cdots\frac{N - r + 1}{N - r + 2} = \frac{N - r + 1}{N}$$

\(b\) के अंतर्गत probability $1/(N - r + 1)$ दी जाती है। इसलिए आवश्यक
(required) probability $1/N$ है जो term $r$, यानी draw number से
independent (स्वतंत्र) है।

**Theorem 2.1.2:** Sample में एक specified unit के शामिल (included) होने की
probability $n/N$ के बराबर होती है।

**Proof:** मान लीजिए $n$ sample size को दर्शाता है। चूँकि specified unit $n$
draws में से किसी में भी sample में शामिल की जा सकती है, इसलिए एक specified unit
के sample में शामिल होने की probability $n$ mutually exclusive (परस्पर अनन्य)
events की probabilities का sum (योग) है, अर्थात यह पहले draw, दूसरे draw,
\..., $n$-वें draw में sample में शामिल होती है। जैसा कि Theorem 2.1.1 में दिखाया
गया है, प्रत्येक case की probability $1/N$ है। इस प्रकार आवश्यक probability
$n/N$ है।

**Corollary 1:** एक specified sample (क्रम को अनदेखा करते हुए) के $n$ units
की probability $1/\binom{N}{n}$ है।

**Corollary 2:** यदि $N$ units की population में, $m$ units को delete कर
दिया जाता है और $m'$ को add कर दिया जाता है, तो दिखाएं कि एक specified draw
में किसी भी unit के selection की probability $(N - m + m')^{- 1}$ है।

**2.2 PROCEDURES OF SELECTING A RANDOM SAMPLE (यादृच्छिक प्रतिदर्श चुनने की
प्रक्रियाएं)**

चूँकि sampling की theory random sampling की assumption (मान्यता) पर आधारित
है, इसलिए random sampling की technique का बुनियादी महत्व है। Random sample
select करने के लिए उपयोग की जाने वाली कुछ procedures इस प्रकार हैं:

\(i\) Lottery Method (लॉटरी विधि)\
(ii) Use of Random Number Tables (यादृच्छिक संख्या तालिकाओं का उपयोग)

**2.2.1 Lottery Method (लॉटरी विधि)**

व्यवहार में (In practice), population की प्रत्येक unit के साथ एक ticket/chit
जुड़ी हो सकती है। इस प्रकार, प्रत्येक sampling unit का 1 से $N$ तक अपना
identification mark (पहचान चिह्न) होता है। एक individual को select करने की
procedure सरल है। प्रत्येक draw से पहले सभी tickets/chits को एक container,
drum या metallic spherical device में रखा जाता है, जिसमें अच्छी तरह से mixing
या reshuffling (फेरबदल) संभव हो। Tickets/chits के draws तब तक जारी रखे जा
सकते हैं जब तक कि आवश्यक size का sample प्राप्त न हो जाए।

जब population size बड़ा होता है तो tickets/chits पर units को number देने और
reshuffling के बाद एक को select करने की यह procedure बोझिल (cumbersome) हो
जाती है। व्यवहार में पूरी तरह से shuffling प्राप्त करना काफी मुश्किल हो सकता है। इस
method में मानवीय पूर्वाग्रह (human bias) और पक्षपात (prejudice) भी आ सकते हैं।

**2.2.2 Use of Random Number Tables (यादृच्छिक संख्या तालिकाओं का उपयोग)**

Random number table अंकों (digits) 0 से 9 की एक व्यवस्था (arrangement) है, जो
या तो linear या rectangular pattern में होती है, जहाँ प्रत्येक position इन अंकों
में से एक से भरी होती है। Random numbers की एक table इस तरह बनाई जाती है कि
सभी numbers, 0, 1, 2, \..., 9, एक-दूसरे से independent दिखाई देते हैं। सामान्य
उपयोग में आने वाली कुछ random number tables हैं:

\(i\) Tippett\'s random number tables\
(ii) Fisher and Yates tables\
(iii) Kendall and Smith tables\
(iv) A million random digits

यह सुनिश्चित करने के लिए कि random numbers की ये series वास्तव में random हैं,
निम्नलिखित tests लागू किए जा सकते हैं:\
(i) Frequency test\
(ii) Serial test\
(iii) Gap test\
(iv) Poker test

Random sample select करने का एक practical method random numbers की एक
table की मदद से एक-एक करके units को चुनना है। दो अंकों (two-digit) वाली संख्याओं
पर विचार करके, हम 00 से 99 तक की numbers प्राप्त कर सकते हैं, जिनमें सभी की
frequency समान होती है। इसी तरह, इन tables के तीन या अधिक rows या columns
को मिलाकर तीन या अधिक अंकों वाली numbers प्राप्त की जा सकती हैं।

आवश्यक size का sample select करने का सबसे सरल तरीका 1 से $N$ तक एक random
number select करना और फिर उस number वाली unit को लेना है। इस procedure में
कई rejections (अस्वीकृतियां) शामिल होती हैं क्योंकि table में दिखाई देने वाली $N$ से
बड़ी सभी numbers को selection के लिए consider नहीं किया जाता है। इसलिए,
random numbers के उपयोग को modify (संशोधित) किया गया है और इनमें से कुछ
modified procedures हैं:

\(i\) Remainder approach (शेषफल दृष्टिकोण)\
(ii) Quotient approach (भागफल दृष्टिकोण)\
(iii) Independent choice of digits (अंकों का स्वतंत्र चुनाव)

**Remainder Approach (शेषफल दृष्टिकोण)**

मान लीजिए $N$ एक $r$-digit की number है और मान लीजिए इसका $r$-digit का
highest multiple (सबसे बड़ा गुणज) $N'$ है। 1 से $N'$ के बीच एक random number
$k$ चुना जाता है और $k$ को $N$ से divide (विभाजित) करने पर प्राप्त remainder
(शेषफल) के बराबर serial number वाली unit को select किया जाता है। यदि
remainder शून्य (zero) है, तो अंतिम unit को select किया जाता है। एक उदाहरण के
रूप में, मान लीजिए $N = 123$, 123 का सबसे बड़ा three-digit multiple 984 है। एक
unit को select करने के लिए, 001 से 984 तक एक random number select करना
होगा। मान लीजिए कि selected random number 287 है। 287 को 123 से divide करने
पर, remainder 41 आता है। इसलिए, sample में serial number 41 वाली unit को
select किया जाता है।

**Quotient Approach (भागफल दृष्टिकोण)**

मान लीजिए $N$ एक $r$-digit की number है और मान लीजिए इसका $r$-digit का
highest multiple $N'$ इस प्रकार है कि $N'/N = q$ है। 0 से $(N' - 1)$ तक एक
random number $k$ चुना जाता है। $k$ को $q$ से divide करने पर quotient
(भागफल) $r$ प्राप्त होता है और sample में serial number $(r - 1)$ वाली unit
को select किया जाता है। एक उदाहरण के रूप में, मान लीजिए $N = 16$ और इसलिए
$N' = 96$ और $q = 96/16 = 6$ है। मान लीजिए कि चुनी गई two-digit random
number 65 है जो 0 और 95 के बीच है। 65 को 6 से divide करने पर, quotient 10 आता
है और इसलिए sample में number $(10 - 1) = 9$ वाली unit को select किया जाता
है।

**Independent Choice of Digits (अंकों का स्वतंत्र चुनाव)**

Mathai (1954) द्वारा सुझाई गई इस method में दो random numbers का selection
शामिल है जिन्हें मिलाकर एक random number बनाई जाती है। एक random number
population size के पहले digit के अनुसार चुना जाता है और दूसरा शेष digits के
अनुसार। यदि चुना गया number 0 है तो अंतिम unit चुनी जाती है। लेकिन यदि बनी हुई
number $N$ से बड़ी या उसके बराबर है, तो number को reject कर दिया जाता है और
operation को दोहराया जाता है।

**Example 2.1:** एक गाँव में 112 households (घरों) की list से 11 households
का एक random sample चुनें।

(i) Random number table के columns 1 से 3, 4 से 6 और इसी तरह दिए गए 3-digit
    random numbers का उपयोग करके और 112 से बड़ी numbers (और number 000 को
    भी) को reject करके, हमारे पास serial numbers 033, 051, 052, 099, 102,
    081, 092, 013, 017, 076, और 079 वाला sample है।

> \(ii\) उपरोक्त procedure में, बड़ी संख्या में random numbers को reject कर दिया
> जाता है। इसलिए, इतनी बड़ी numbers के rejection से बचने के लिए आमतौर पर
> इस्तेमाल किया जाने वाला device, यानी remainder approach (शेषफल दृष्टिकोण),
> नियोजित किया जाता है। 112 का सबसे बड़ा three-digit multiple 896 है। ऊपर की
> तरह three-digit random numbers का उपयोग करके, sample में serial numbers
> 086, 033, 049, 097, 051, 052, 066, 107, 015, 106 और 020 वाले households
> शामिल होंगे।
>
> \(iii\) यदि quotient approach (भागफल दृष्टिकोण) लागू किया जाता है, तो 112
> का 3-digit multiple 896 है और $896/112 = 8$ है। उन्हीं random numbers का
> उपयोग करते हुए और उन्हें 8 से divide करने पर, हमारे पास replacement method के
> साथ list numbers 025, 004, 020, 026, 006, 006, 092, 041, 085, 027 और
> 086 वाले households का sample है और बिना replacement method के list
> numbers 025, 004, 020, 026, 006, 092, 041, 085, 027, 086 और 042 वाले
> households का sample है।

**Example 2.2:** लखनऊ के पास एक इलाके में दस बागों (orchards) में क्रमशः 125,
793, 970, 830, 1502, 864, 503, 106, 970, 312 फलों के पेड़ थे। Random numbers
का उपयोग करके 10 फलों के पेड़ों का एक random sample निकालें।

मान लीजिए कि पहले बाग में फलों के पेड़ों के serial numbers 1 से 125 तक हैं, दूसरे बाग
में 126 से 918 तक, और इसी तरह। इसलिए, cumulative (संचयी) serial numbers को
125, 918, 1888, 2718, 4220, 5084, 5587, 5693, 6663, 6975 के रूप में लिखा जा
सकता है। समान धारणाओं (notions) के साथ उपरोक्त table के 4-digit random
numbers का उपयोग करके, हमारे पास 1983, 0330, 1614, 2096, 0511, 0524, 3311,
6874, 2183 और 6926 हैं।\
पहले random number 1983 के साथ, हम चौथे (4th) बाग में serial number 95 वाला
फलों का पेड़ select करते हैं। इसी तरह, दूसरे random number 0330 के साथ, हम दूसरे
(2nd) बाग में serial number 205 वाला पेड़ select करते हैं, और इसी तरह। इस
procedure को आगे बढ़ाते हुए, हम पाते हैं कि sample में शामिल बागों के serial
numbers 2, 3, 4, 5 और 10 हैं। इस प्रकार, सभी बागों में फलों के पेड़ों को serial
numbers देना आवश्यक नहीं है, ऊपर दिखाए गए numbers वाले केवल पांच बाग 10 फलों के
पेड़ों का एक random sample select करने के उद्देश्य को पूरा करेंगे।

**2.3 ESTIMATION OF POPULATION PARAMETERS (जनसंख्या मापदंडों का अनुमान)**

मान लीजिए कि population में प्रत्येक unit $u_{i}$ character $y$ के लिए एक
variate value $y_{i}$ से जुड़ी है। Parameters के लिए, मान लें\
Population total (कुल जनसंख्या), $Y = \sum_{i = 1}^{N}\mspace{2mu} y_{i}$\
Population mean (जनसंख्या माध्य),
$\bar{Y} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu} y_{i}$\
Population variance (जनसंख्या प्रसरण),
$\sigma^{2} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu}(y_{i} - \bar{Y})^{2}$

मान लीजिए sample में $n$ units क्रमशः $y_{1},y_{2},\ldots,y_{n}$ variate
values के साथ $u_{1},u_{2},\ldots,u_{n}$ हैं। Population total और mean के
estimators इस प्रकार दिए गए हैं

$$\widehat{Y} = \frac{N}{n}\sum_{i = 1}^{n}\mspace{2mu} y_{i} = N\bar{y}$$

और

$$\bar{y} = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu} y_{i},$$

क्रमशः।

Factor $N/n$ जिससे sample total को गुणा (multiplied) किया जाता है, कभी-कभी
expansion या raising या inflation factor कहलाता है। इसके inverse (उल्टे)
$n/N$ को sampling fraction कहा जाता है और इसे इस text में $f$ अक्षर (letter)
द्वारा दर्शाया गया है।

**Theorem 2.3.1:** Simple random sampling, wor में, sample mean $\bar{y}$,
$\bar{Y}$ का एक unbiased estimator है और इसका sampling variance इस प्रकार
दिया गया है

$$V(\bar{y}) = \left( 1 - \frac{n}{N} \right)\frac{S^{2}}{n} = (1 - f)\frac{S^{2}}{n}\ (2.3.1)$$

जहाँ

$$S^{2} = \frac{N}{N - 1}\sigma^{2}$$

**Proof:** हमारे पास है

$$E(\bar{y}) = E\left( \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu} y_{i} \right) = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu} E(y_{i})$$

Definition के अनुसार,

$$E(y_{i}) = \sum_{i = 1}^{N}\mspace{2mu} P_{i}y_{i} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu} y_{i} = \bar{Y}$$

इसलिए, $E(\bar{y}) = \bar{Y}$\
इस प्रकार sample mean population mean का एक unbiased estimator है।

$\bar{y}$ का variance इस प्रकार दिया गया है

$$V(\bar{y}) = E(\bar{y} - \bar{Y})^{2} = E\left\lbrack \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y}) \right\rbrack^{2} = \frac{1}{n^{2}}E\left\lbrack \sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y})^{2} + 2\sum_{i \neq j}^{}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y})(y_{j} - \bar{Y}) \right\rbrack$$

चूँकि

$$E(y_{i} - \bar{Y})^{2} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu}(y_{i} - \bar{Y})^{2} = \sigma^{2}$$

और

$$E(y_{i} - \bar{Y})(y_{j} - \bar{Y}) = \frac{1}{N(N - 1)}\sum_{i \neq j}^{}\mspace{2mu}(y_{i} - \bar{Y})(y_{j} - \bar{Y}) = \frac{1}{N(N - 1)}\left\lbrack \left( \sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y}) \right)^{2} - \sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y})^{2} \right\rbrack = \frac{- N\sigma^{2}}{N(N - 1)} = - \frac{\sigma^{2}}{N - 1}$$

इस प्रकार,

$$V(\bar{y}) = \frac{1}{n^{2}}\left\{ n\sigma^{2} - n(n - 1)\frac{\sigma^{2}}{N - 1} \right\} = \frac{N - n}{N - 1}\frac{\sigma^{2}}{n} = \left( 1 - \frac{n}{N} \right)\frac{S^{2}}{n}$$

जो theorem को सिद्ध (proves) करता है।

**Corollary 1:** Simple random sampling, wor में, $\bar{y}$ की standard
error इस प्रकार दी जाती है

$$S_{\bar{y}} = S\sqrt{\frac{N - n}{nN}} = S\sqrt{\frac{1 - f}{n}}\ (2.3.2)$$

**Corollary 2:** Simple random sampling, wor में, population total $Y$ के
एक estimator के रूप में $\widehat{Y} = N\bar{y}$ का variance इस प्रकार प्राप्त
किया जाता है

$$V(\widehat{Y}) = E(\widehat{Y} - Y)^{2} = \frac{N^{2}S^{2}(N - n)}{nN} = (1 - f)\frac{N^{2}S^{2}}{n}\ (2.3.3)$$

**Corollary 3:** Simple random sampling, wor में, $\widehat{Y}$ की
standard error इस प्रकार दी जाती है

$$S_{\widehat{Y}} = NS\sqrt{\frac{N - n}{nN}} = NS\sqrt{\frac{1 - f}{n}}\ (2.3.4)$$

यदि sampling replacement (प्रतिस्थापन) के साथ है, तो size $n$ का एक random
sample, sample mean $\bar{y}$ को एक unbiased estimator के रूप में देता है।
उपरोक्त results से, यह आसानी से देखा जा सकता है कि variance के लिए terms
$(N - n)/N$ और standard error के लिए $\sqrt{(N - n)/N}$ population की
finiteness (परिमितता) के कारण पेश किए गए हैं और इन्हें **finite population
corrections (fpc)** कहा जाता है। Random sampling, wr के मामले में, finite
population correction को ignore करके variance और standard error प्राप्त की
जा सकती है।

**Corollary 4:** Random sampling, wr में, $\bar{y}$ की variance और
standard error को इस प्रकार लिखा जा सकता है

$$V(\bar{y}) = \frac{\sigma^{2}}{n},\ \sigma_{\bar{y}} = \frac{\sigma}{\sqrt{n}}\ (2.3.5a)$$

यदि $n$, $N$ की तुलना में छोटा है, तो fpc unity (एक) से बहुत भिन्न नहीं होगा और
mean का sampling variance लगभग एक infinite (अनंत) population से निकाले गए
sample के mean के variance के बराबर होगा।

**Corollary 5:** Random sampling, wr में, $\widehat{Y} = N\bar{y}$ की
variance और standard error को इस प्रकार लिखा जा सकता है

$$V(\widehat{Y}) = \frac{N^{2}\sigma^{2}}{n},\ \sigma_{\widehat{Y}} = \frac{N\sigma}{\sqrt{n}}\ (2.3.5b)$$

**Theorem 2.3.2:** Simple random sampling में,

$$s^{2} = \frac{\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{y})^{2}}{n - 1}\ (2.3.6)$$

$S^{2} = \frac{N}{N - 1}\sigma^{2}$ का एक unbiased estimator है।

**Proof:** हम लिख सकते हैं

$$s^{2} = \frac{\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}\lbrack(y_{i} - \bar{Y}) - (\bar{y} - \bar{Y})\rbrack^{2}}{n - 1} = \frac{\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y})^{2} - n(\bar{y} - \bar{Y})^{2}}{n - 1}$$

इसलिए,

$$E(s^{2}) = \frac{\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu} E(y_{i} - \bar{Y})^{2} - nE(\bar{y} - \bar{Y})^{2}}{n - 1} = \frac{n(N - 1)S^{2}/N - n(N - n)S^{2}/(Nn)}{n - 1} = S^{2}$$

अतः $s^{2}$, $S^{2}$ का एक unbiased estimator है।

**Corollary 1:** Random sampling, wor में $\bar{y}$ के variance का एक
unbiased estimator इस प्रकार दिया जाता है

$$v(\bar{y}) = \frac{(N - n)s^{2}}{Nn} = (1 - f)\frac{s^{2}}{n}\ (2.3.7)$$

Standard error के एक estimate के लिए, हम $s_{\bar{y}} = s\sqrt{(1 - f)/n}$
लेते हैं।

**Corollary 2:** Random sampling, wor में $\widehat{Y} = N\bar{y}$ के
variance का एक unbiased estimator इस प्रकार दिया जाता है

$$v(\widehat{Y}) = \frac{N(N - n)s^{2}}{n} = (1 - f)N^{2}\frac{s^{2}}{n}\ (2.3.8)$$

Standard error के एक estimate के लिए, हम
$s_{\widehat{Y}} = Ns\sqrt{(1 - f)/n}$ लेते हैं।

**Corollary 3:** Random sampling, wr में $\bar{y}$ के variance का एक
unbiased estimator इस प्रकार दिया जाता है

$$v(\bar{y}) = \frac{s^{2}}{n}\ (2.3.9)$$

Standard error के एक estimate के लिए, हम $s_{\bar{y}} = s/\sqrt{n}$ लेते हैं।

**Corollary 4:** Random sampling, wr में $\widehat{Y} = N\bar{y}$ के
variance का एक unbiased estimator इस प्रकार दिया जाता है

$$v(\widehat{Y}) = \frac{N^{2}s^{2}}{n}\ (2.3.10)$$

Standard error के एक estimate के लिए, हम $s_{\widehat{Y}} = Ns/\sqrt{n}$
लेते हैं।

**Example 2.3:** 5 households (घरों) की एक छोटी कॉलोनी (hypothetical
population) से $n = 2$ households का एक random sample लिया गया था, जिनकी
monthly income (रुपये में) इस प्रकार थी:

  ----------------------------------------------
  Household (घर)   1     2     3     4     5
  ---------------- ----- ----- ----- ----- -----
  Income (in       156   149   166   164   155
  rupees)                                  

  ----------------------------------------------

\(i\) Population mean $\bar{Y}$, variance $(\sigma^{2})$ और mean square
error $(S^{2})$ की गणना (calculate) करें।\
(ii) Replacement method द्वारा size 2 के सभी possible samples को Enumerate
करें और दिखाएं कि\
(a) sample mean population mean का एक unbiased estimate देता है और इसका
sampling variance ज्ञात करें;\
(b) sample variance $(s^{2})$ population variance $\sigma^{2}$ का एक
unbiased estimate है; और\
(c) $v(\bar{y}) = (y_{1} - y_{2})^{2}/4$, $V(\bar{y})$ का एक unbiased
estimator है, यानी
$E\lbrack v(\bar{y})\rbrack = V(\bar{y}) = \sigma^{2}/2$।\
(iii) Without replacement method द्वारा size 2 के सभी possible samples को
Enumerate करें और दिखाएं कि\
(a) sample mean population mean का एक unbiased estimate देता है और इसका
sampling variance ज्ञात करें;\
(b) sample variance $(s^{2})$ population variance $S^{2}$ का एक unbiased
estimate है; और\
(c) $v(\bar{y}) = 3(y_{1} - y_{2})^{2}/20$, $V(\bar{y})$ का एक unbiased
estimator है, यानी
$E\lbrack v(\bar{y})\rbrack = V(\bar{y}) = \frac{1 - f}{n}S^{2} = \frac{3}{10}S^{2}$।

\(i\) 5 households का population mean

$$\bar{Y} = (156 + 149 + 166 + 164 + 155)/5 = 158.00$$

Population variance

$$\sigma^{2} = \lbrack(156^{2} + 149^{2} + \cdots + 155^{2}) - 5 \times 158^{2}\rbrack/5 = 38.80$$

इसलिए $S^{2} = N\sigma^{2}/(N - 1) = 5 \times 38.8/4 = 48.50$

\(ii\) यह देखा जा सकता है कि possible samples की कुल संख्या 25 $( = 5^{2})$
है। साथ ही, 25 possible samples में से प्रत्येक के select होने की probability
$(1/25)$ समान है।

**Table 2.3.1:** All samples of 2 units from 5 units in simple random
sampling with replacement

  ---------------------------------------------------------------------------------------------------------------------------------------
  Sample no.    Units in the    Probability   $$y_{1}$$   $$y_{2}$$   $$\bar{y}$$   $$(\bar{y} - \bar{Y})$$   $$(y_{1} - y_{2})^{2}/4$$
                sample                                                                                        
  ------------- --------------- ------------- ----------- ----------- ------------- ------------------------- ---------------------------
  1             1,1             1/25          156         156         156.0         -2.0                      0

  2             1,2             1/25          156         149         152.5         -5.5                      49/4

  3             1,3             1/25          156         166         161.0         3.0                       100/4

  4             1,4             1/25          156         164         160.0         2.0                       64/4

  5             1,5             1/25          156         155         155.5         -2.5                      1/4

  6             2,1             1/25          149         156         152.5         -5.5                      49/4

  7             2,2             1/25          149         149         149.0         -9.0                      0

  8             2,3             1/25          149         166         157.5         -0.5                      289/4

  9             2,4             1/25          149         164         156.5         -1.5                      225/4

  10            2,5             1/25          149         155         152.0         -6.0                      36/4

  11            3,1             1/25          166         156         161.0         3.0                       100/4

  12            3,2             1/25          166         149         157.5         -0.5                      289/4

  13            3,3             1/25          166         166         166.0         8.0                       0

  14            3,4             1/25          166         164         165.0         7.0                       4/4

  15            3,5             1/25          166         155         160.5         2.5                       121/4

  16            4,1             1/25          164         156         160.0         2.0                       64/4

  17            4,2             1/25          164         149         156.5         -1.5                      225/4

  18            4,3             1/25          164         166         165.0         7.0                       4/4

  19            4,4             1/25          164         164         164.0         6.0                       0

  20            4,5             1/25          164         155         159.5         1.5                       81/4

  21            5,1             1/25          155         156         155.5         -2.5                      1/4

  22            5,2             1/25          155         149         152.0         -6.0                      36/4

  23            5,3             1/25          155         166         160.5         2.5                       121/4

  24            5,4             1/25          155         164         159.5         1.5                       81/4

  25            5,5             1/25          155         155         155.0         -3.0                      0

  **Average**                                                         **158.0**                               **19.40**
  ---------------------------------------------------------------------------------------------------------------------------------------

(a) $\bar{y}$ की expected value column (6) की average value द्वारा दी
    जाती है, जो कि population mean 158.0 के रूप में आती है, इस प्रकार यह verify
    होता है कि estimator unbiased है। हम Table 2.3.1 के columns (6) और (7)
    से पाते हैं कि ये estimates आम तौर पर $\bar{Y}( = 158.0)$ से भिन्न होते हैं,
    और यह error आमतौर पर sample से sample में भिन्न होती है। इसके अलावा,
    column (7) से यह ध्यान रखना दिलचस्प है कि column (6) द्वारा दिया गया
    प्रत्येक sample mean $\bar{y}$, population mean $(\bar{Y})$ का एक
    unbiased estimate है क्योंकि column (7) का average शून्य है, जो result को
    साबित करता है। Sampling variance error के squares \[column (7)\] का
    mean है जो 19.40 $( = 38.80/2)$ आता है।

(b) Sample variance $(s^{2})$, $(y_{1} - y_{2})^{2}/2$ द्वारा दिया जाता है
    जो column (8) में दी गई value का दोगुना (twice) है। इसलिए,
    $2 \times (8)$ दिखाता है कि $E(s^{2})$, 38.80 $(\sigma^{2})$ के बराबर
    है, जो दर्शाता है कि simple random sampling, wr में population variance के
    लिए $s^{2}$ एक unbiased estimator है।

(c) $V(\bar{y})$ का एक estimator $v(\bar{y}) = (y_{1} - y_{2})^{2}/4$
    द्वारा दिया जाता है, वे values जो Table 2.3.1 के column (8) में possible
    samples के लिए दी गई हैं। $v(\bar{y})$ की expected value column (8) में
    values का average है, जो दर्शाता है कि
    $E\lbrack v(\bar{y})\rbrack = V(\bar{y}) = \sigma^{2}/2$ है। इस प्रकार
    estimate $v(\bar{y})$ unbiased है।

**Table 2.3.2:** All samples of 2 units from 5 units in simple random
sampling without replacement

  -----------------------------------------------------------------------------------------------------------------------------------
  Sample no.    Units in    Probability   $$y_{1}$$   $$y_{2}$$   $$\bar{y}$$   Error                   $$3(y_{1} - y_{2})^{2}/20$$
                sample                                                          $(\bar{y} - \bar{Y})$   
  ------------- ----------- ------------- ----------- ----------- ------------- ----------------------- -----------------------------
  1             1,2         1/10          156         149         152.5         -5.5                    7.35

  2             1,3         1/10          156         166         161.0         3.0                     15.00

  3             1,4         1/10          156         164         160.0         2.0                     9.60

  4             1,5         1/10          156         155         155.5         -2.5                    0.15

  5             2,3         1/10          149         166         157.5         -0.5                    43.35

  6             2,4         1/10          149         164         156.5         -1.5                    33.75

  7             2,5         1/10          149         155         152.0         -6.0                    5.40

  8             3,4         1/10          166         164         165.0         7.0                     0.60

  9             3,5         1/10          166         155         160.5         2.5                     18.15

  10            4,5         1/10          164         155         159.5         -1.5                    12.15

  **Average**                                                     **158.0**                             **14.55**
  -----------------------------------------------------------------------------------------------------------------------------------

> Iii Random sampling, wor के मामले में, possible samples की संख्या
> $10\left\lbrack = \binom{5}{2} \right\rbrack$ है। यह देखा जा सकता है कि
> 10 possible samples में से प्रत्येक के select होने की probability $(1/10)$
> समान है।

(a) $\bar{y}$ की expected value, जो Table 2.3.2 के column (6) के average
    द्वारा दी गई है, population mean 158.0 आती है, इस प्रकार यह verify होता
    है कि $\bar{y}$, $\bar{Y}$ का एक unbiased estimator है। इसके अलावा,
    sampling variance जो column (7) में दी गई errors के squares का average
    निकालकर प्राप्त किया जाता है, 14.55 आता है, जो verify करता है कि
    $V(\bar{y}) = 3\sigma^{2}/8( = 3S^{2}/10)$।

(b) चूँकि sample variance $(s^{2})$, $(y_{1} - y_{2})^{2}/2$ द्वारा दिया
    गया है, जिसे आसानी से प्राप्त किया जा सकता है, 10 sample mean squares का
    average $E(s^{2})$ देता है।\
    यहाँ, $E(s^{2}) = 485/10 = 48.5$ है। साथ ही, population mean square
    $= 48.5$ है। इस प्रकार, sample mean square population mean square
    $(S^{2})$ का एक unbiased estimator प्रदान करता है, जो verify करता है कि
    $E(s^{2}) = S^{2}$ है।

(c) $V(\bar{y})$ का एक estimator $v(\bar{y}) = 3(y_{1} - y_{2})^{2}/20$
    द्वारा दिया जाता है, वे values जो Table 2.3.2 के column (8) में दी गई हैं और
    यहाँ उपयोग की जा सकती हैं। $v(\bar{y})$ की expected value, जो
    column (8) में values का average है, 14.55 है, जो दर्शाता है कि estimator
    unbiased है, यानी,
    $E\lbrack v(\bar{y})\rbrack = V(\bar{y}) = \frac{3}{10}S^{2}$।

**2.4 ESTIMATION OF POPULATION PROPORTION (जनसंख्या अनुपात का अनुमान)**

कभी-कभी, population में units को दो groups में classify किया जाता है: (i) एक
particular characteristic (विशेषता) वाली और (ii) वह characteristic न रखने
वाली। उदाहरण के लिए, एक फसल का खेत सिंचित (irrigated) हो सकता है या असिंचित।
यदि यह सिंचित है, तो हम कहते हैं कि इसमें \"irrigation\" (सिंचाई) की
characteristic है। यदि यह असिंचित है, तो हम कहते हैं कि इसमें irrigation की
particular characteristic नहीं है। यदि हम सिंचित खेतों के proportion (अनुपात)
का estimate लगाने में रुचि रखते हैं, तो $N$ खेतों की population को variate
$y_{i}$ के साथ परिभाषित किया जा सकता है, जिसका value 1 है यदि खेत सिंचित है,
अन्यथा शून्य। यदि $N$ में से सिंचित खेतों की कुल संख्या $N_{1}$ हो

$$\sum_{i = 1}^{N}\mspace{2mu} y_{i} = N_{1}$$

इस प्रकार,

$$P = \frac{\sum_{}^{}\ y_{i}}{N} = \frac{N_{1}}{N} = \text{proportion of irrigated fields}$$

और

$$\sum_{i = 1}^{N}\mspace{2mu} y_{i}^{2} = N_{1} = NP$$

इस प्रकार, population proportion का estimate लगाने की problem ऊपर की तरह
variate को define करके population mean का estimate लगाने की बन जाती है। यदि
size $n$ के एक random sample में से $n_{1}$ units में वह characteristic है, तो
sample proportion $p = n_{1}/n$ द्वारा दिया जाता है। इस प्रकार

$$\sum_{i = 1}^{n}\mspace{2mu} y_{i} = n_{1} = np$$

इसलिए, $P$ का एक unbiased estimator इस प्रकार दिया जाता है

$$\widehat{P} = (n_{1}/n) = p\ (2.4.1)$$

**Theorem 2.4.1:** Sampling, wor में, $p$ का variance इस प्रकार दिया जाता है

$$V(p) = \frac{N - n}{n(N - 1)}PQ = (1 - f)\frac{N}{N - 1}\frac{PQ}{n}\ (2.4.2)$$

जहाँ $Q = 1 - P$ है। Proof स्पष्ट है।

**Corollary 1:** Sampling, wr में, $p$ का variance इस प्रकार दिया जाता है

$$V(p) = \frac{PQ}{n}\ (2.4.3)$$

**Corollary 2:** किसी desired characteristic वाली units की estimated
total number, $N_{1} = Np$ का variance इस प्रकार दिया जाता है

$$V(N_{1}) = \frac{N^{2}(N - n)PQ}{n(N - 1)}\ (2.4.4)$$

**Theorem 2.4.2:** Sampling, wor में, $V(p)$ का एक unbiased estimator इस
प्रकार दिया जाता है

$$v(p) = (1 - f)\frac{pq}{n - 1}\ (2.4.5)$$

Proof स्पष्ट है।

**Corollary 1:** Sampling, wr में, $V(p)$ का एक unbiased estimator इस
प्रकार दिया जाता है

$$v(p) = \frac{pq}{n - 1}\ (2.4.6)$$

**Corollary 2:** $N_{1} = Np$ के variance का एक unbiased estimate इस
प्रकार दिया जाता है

$$v(N_{1}) = \frac{N(N - n)pq}{n - 1} = (1 - f)\frac{N^{2}pq}{n - 1}\ (2.4.7)$$

**Corollary 3:** $p$ का coefficient of variation (विचरण गुणांक) इस प्रकार
दिया जाता है

$$CV = \frac{\sqrt{PQ/n}}{P} = \sqrt{\frac{Q}{nP}}\ (2.4.8)$$

**Example 2.4:** व्यक्तियों की age (आयु) की accuracy मापने के लिए एक शहर के एक
वार्ड के 3000 मतदाताओं (voters) की list की जाँच की गई। 300 नामों का एक random
sample लिया गया, जिससे पता चला कि 51 नागरिकों को गलत age के साथ दिखाया गया
था। List में age के गलत विवरण वाले मतदाताओं की कुल संख्या का estimate लगाएं और
standard error का estimate लगाएं।\
यहाँ, $N = 3000,n = 300,n_{1} = 51,p = 0.17$\
Age के गलत विवरण वाले मतदाताओं की कुल संख्या का estimate इस प्रकार प्राप्त किया
जाता है

$${\widehat{N}}_{1} = Np = (3000)(0.17) = 510$$

\(i\) यदि sampling, wr पर विचार किया जाता है, तो standard error का
estimate इस प्रकार दिया जाता है

$$S_{{\widehat{N}}_{1}} = N\sqrt{\frac{pq}{n - 1}} = 3000\sqrt{\frac{(0.17)(0.83)}{299}} = 159.3$$

\(ii\) यदि sampling, wor पर विचार किया जाता है, तो estimated standard
error इस प्रकार दी जाती है

$$S_{{\widehat{N}}_{1}} = N\sqrt{(1 - f)\frac{pq}{n - 1}} = 3000\sqrt{(1 - 0.10)\frac{(0.17)(0.83)}{299}} = 151.1$$

**2.5 COMBINATION OF UNBIASED ESTIMATORS (अभिनत आकलकों का संयोजन)**

ऐसी स्थितियां होती हैं जहां एक combined estimate प्राप्त करने के लिए कई samples
पर आधारित estimates को pool (मिलाना) करना पड़ता है। यदि
$t_{i}(i = 1,2,\ldots,m)$ एक parameter $\theta$ के unbiased estimators हैं,
जो mutually independent (परस्पर स्वतंत्र) हैं, तो pooled estimator

$$T = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu} t_{i}}{m}\ (2.5.1)$$

भी $\theta$ का एक unbiased estimator है। $T$ का variance इस प्रकार दिया
जाता है

$$V(T) = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu} V(t_{i})}{m^{2}}\ (2.5.2)$$

और variance का estimate

$$v(T) = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu}(t_{i} - T)^{2}}{m(m - 1)}\ (2.5.3)$$

हम निम्नलिखित मामलों (cases) के लिए समस्या पर विचार करेंगे:\
(i) Variables के लिए simple random sampling\
(ii) Attributes के लिए simple random sampling

**2.5.1 Simple Random Sampling for Variables**

मान लीजिए कि ${\bar{y}}_{1},{\bar{y}}_{2},\ldots,{\bar{y}}_{m}$ sample
means हैं, जिनमें से प्रत्येक को $n_{1},n_{2},\ldots,n_{m}$ sizes के साथ
independently निकाला गया है। सभी samples का एक pooled estimator निम्न लेकर
दिया जाता है\
(i) $m$ estimates का arithmetic mean

$${\bar{y}}' = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu}{\bar{y}}_{i}}{m}\ (2.5.4)$$

\(ii\) $m$ estimates का weighted mean

$${\bar{y}}'' = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu} n_{i}{\bar{y}}_{i}}{n}\ (2.5.5)$$

जहाँ $n = \sum_{i = 1}^{m}\mspace{2mu} n_{i}$ है।

**When Sampling is With Replacement Method (जब प्रतिचयन प्रतिस्थापन के साथ
है)**\
${\bar{y}}'$ और ${\bar{y}}''$ के sampling variances इस प्रकार दिए गए हैं

$$V({\bar{y}}') = \frac{1}{m^{2}}\sum_{i = 1}^{m}\mspace{2mu}\frac{\sigma^{2}}{n_{i}}\ (2.5.6)$$

और

$$V({\bar{y}}'') = \frac{\sigma^{2}}{n}\ (2.5.7)$$

$V({\bar{y}}')$ और $V({\bar{y}}'')$ के unbiased estimators इस प्रकार प्रदान
किए जाते हैं

$$v({\bar{y}}') = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu}({\bar{y}}_{i} - {\bar{y}}')^{2}}{m(m - 1)}\ (2.5.8)$$

और

$$v({\bar{y}}'') = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu} n_{i}({\bar{y}}_{i} - {\bar{y}}'')^{2}}{n(n - 1)}\ (2.5.9)$$

यह ध्यान दिया जाना चाहिए कि relation (2.5.5) में दिया गया estimate (2.5.4)
में दिए गए estimate की तुलना में अधिक efficient (कुशल) है और दोनों मामलों में
variances की तुलना करके इसे verify किया जा सकता है।

**When Sampling is Without Replacement Method (जब प्रतिचयन प्रतिस्थापन के
बिना है)**\
${\bar{y}}'$ और ${\bar{y}}''$ के sampling variances इस प्रकार दिए गए हैं

$$V({\bar{y}}') = \frac{1}{m^{2}}\sum_{i = 1}^{m}\mspace{2mu}(1 - f_{i})\frac{S_{i}^{2}}{n_{i}}\ (2.5.10)$$

और

$$V({\bar{y}}'') \approx \frac{S^{2}}{n}(1 - f)\ (2.5.11)$$

$V({\bar{y}}')$ और $V({\bar{y}}'')$ के unbiased estimators इस प्रकार प्रदान
किए जाते हैं

$$v({\bar{y}}') = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu}(1 - f_{i})s_{i}^{2}}{m^{2}n_{i}}\ (2.5.12)$$

और

$$v({\bar{y}}'') = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu} n_{i}(1 - f_{i})s_{i}^{2}}{n^{2}}\ (2.5.13)$$

Estimators ${\bar{y}}'$ और ${\bar{y}}''$ identical (समान) हो जाते हैं यदि
sample sizes $n_{1},n_{2},\ldots,n_{m}$ समान हों।

**2.5.2 Simple Random Sampling for Attributes**

पिछले section में प्राप्त results को attributes के लिए simple random sampling
पर भी लागू किया जा सकता है। यदि $p_{1},p_{2},\ldots,p_{m}$,
$n_{1},n_{2},\ldots,n_{m}$ size के $m$ samples पर आधारित sample
proportions हैं, जिनमें से प्रत्येक को independently निकाला गया है। सभी sample का
एक pooled estimator निम्न लेकर दिया जाता है

\(i\) $m$ estimates का arithmetic mean

$$p' = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu} p_{i}}{m}\ (2.5.14)$$

\(ii\) $m$ estimates का weighted mean

$$p'' = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu} n_{i}p_{i}}{n}\ (2.5.15)$$

जहाँ $n = \sum_{i = 1}^{m}\mspace{2mu} n_{i}$ है।

**2.6 CONFIDENCE LIMITS (विश्वास सीमाएं)**

Population parameter के बारे में conclusions (निष्कर्ष) निकालने के लिए, sample
estimate के चारों ओर confidence limits का निर्माण किया जाता है। यदि sample
size बड़ा है, तो sample mean $\bar{Y}$ mean और $V(\bar{y})$ variance के साथ
normally distributed होता है। इसलिए, population mean के लिए
$100(1 - \alpha)\%$ confidence limits इस प्रकार दी जाती हैं

$$\bar{y} \pm t(\alpha)S_{\bar{y}}$$

जहाँ $t(\alpha)$ confidence के दिए गए level के अनुरूप normal variate का value
है।

**Example 2.5:** एक फसल की total yield (कुल उपज) का estimate लगाने के लिए
500 plots की population से 50 plots का एक simple random sample select
किया गया था। Sample mean yield प्रति plot 550 kg थी जिसका sample variance
$s^{2} = 111.25$ था। फसल की total yield का estimate लगाएं और 95%
confidence limits स्थापित करें।

यहाँ, $N = 500,n = 50,\bar{y} = 550,s^{2} = 111.25$\
Estimated total yield है

$$\widehat{Y} = N\bar{y} = 500 \times 550 = 275,000\text{~kg}$$

$\widehat{Y}$ की standard error है

$$S_{\widehat{Y}} = N\sqrt{(1 - f)\frac{s^{2}}{n}} = 500\sqrt{\left( 1 - \frac{50}{500} \right)\frac{111.25}{50}} = 500\sqrt{0.9 \times 2.225} = 500 \times 1.418 = 709$$

95% confidence के लिए, $t(\alpha) = 1.96$ है। Confidence limits हैं

$$275,000 \pm 1.96 \times 709 \Rightarrow (273,610,276,390)$$

**2.7 ESTIMATION OF SAMPLE SIZE (प्रतिदर्श आकार का अनुमान)**

Population parameters का estimate लगाने के लिए एक sample survey की
planning करते समय, महत्वपूर्ण सवाल यह है कि निकाले जाने वाले sample का size कैसे
निर्धारित किया जाए। यह permissible loss (अनुमेय हानि) और confidence के level
के संदर्भ में risk (या precision) की degree को specify करके किया जा सकता है।
इससे पहले कि हम विभिन्न sampling methods के लिए समस्या पर चर्चा करें, आइए sample
size के estimation की समस्या के generalized solution पर पहुंचें।

मान लीजिए $z$ estimate लेने पर error की मात्रा (amount) है और मान लीजिए
$l(z)$ इसे लेने से होने वाला loss है। एक दिए गए sampling method के लिए, theory
हमें density function प्रदान करेगी। इस प्रकार, एक दिए गए sample size के लिए
loss की expected value इस प्रकार प्राप्त की जाती है

$$L(n) = E\lbrack l(z)\rbrack\ (2.7.1)$$

आइए size $n$ के sample के लिए cost function पर भी विचार करें, जिसे इस प्रकार
दर्शाया गया है

$$C(n) = a + cn\ (2.7.2)$$

जहाँ $a$ over-head cost है, और $c$ sampling method में cost per unit है।

Relations (2.7.1) और (2.7.2) को मिलाकर, हमें total loss मिलता है जो इस
प्रकार दिया गया है

$$\Phi(n) = L(n) + \lambda C(n)\ (2.7.3)$$

जहाँ $\lambda$ कोई constant (स्थिर) मात्रा है।

चूँकि sample लेने का उद्देश्य total loss को minimize करना है, इसलिए $n$ को इस
तरह चुना जाना चाहिए कि relation (2.7.3) minimize हो जाए। $\Phi(n)$ को $n$
के संबंध में differentiate करके और $d\Phi/dn = 0$ के बराबर रखकर, $n$ का optimum
value निर्धारित किया जा सकता है।

**Example 2.6:** यदि $\bar{y}$ में error के कारण loss function
$|\bar{y} - \bar{Y}|$ के proportional (समानुपाती) है और यदि survey की total
cost $C = a + cn$ है, तो दिखाएं कि simple random sampling के साथ, fpc को
ignore करते हुए, $n$ का optimum value $(k\sigma/c\sqrt{2\pi})^{2/3}$ है,
जहाँ $k$ एक constant है।\
यहाँ $l(z) = |\bar{y} - \bar{Y}|$\
या $l(z) = k|\bar{y} - \bar{Y}|$\
जहाँ $k$ कोई constant है।\
इस प्रकार, यह अनुसरण करता है कि

$$L(n) = kE|\bar{y} - \bar{Y}| = k\sqrt{\frac{2}{\pi}}\frac{\sigma}{\sqrt{n}}$$

\[यह माना जाता है कि $\bar{y}$, $N(\bar{Y},\sigma/\sqrt{n})$ वितरित
(distributed) है\]\
इसलिए

$$\Phi(n) = a + cn + k\sqrt{\frac{2}{\pi}}\frac{\sigma}{\sqrt{n}}$$

Differentiation (अवकलन) करने और $d\Phi/dn = 0$ के बराबर रखने पर, हमारे पास है

$$n = \left( \frac{k\sigma}{c\sqrt{2\pi}} \right)^{2/3}$$

इसी तरह का treatment और analysis किसी भी sampling method पर लागू किया जा
सकता है जिसमें loss function $n$ के inversely proportional हो और cost
function भी $n$ का एक function हो। एक generalized discussion Yates
(1960), और Raiffa और Schlaifer (1961) द्वारा दी गई है। Chaudhary (1977) और
Chaudhary और Singh (1979) ने sequential methods के लिए एक लाइन पर चर्चा की
है। Classified discussion के लिए, methods का एक अच्छा विवरण Nordin (1944),
Blythe (1945), Deming (1950) और Tippett (1950) द्वारा दिया गया है।

अब आइए उस characteristic के लिए simple random sampling के results को विस्तृत
करें जिसे quantitatively (मात्रात्मक रूप से) मापा जा सकता है। मान लीजिए कि
estimate में permissible marginal error $e$ है, और $(1 - \alpha)$
confidence का level है। Sample mean को mean $\bar{Y}$ और variance

$$V(\bar{y}) = \frac{N - n}{Nn}S^{2}$$

के साथ normally distributed माना जाता है।\
इसलिए,

$$e = t(\alpha)\sqrt{\frac{(N - n)S^{2}}{Nn}}\ (2.7.4)$$

जहाँ $t(\alpha)$ दिए गए $(1 - \alpha)$ के अनुरूप normal variate का value है,
जो देता है

$$n = \frac{t^{2}S^{2}/e^{2}}{1 + t^{2}S^{2}/(Ne^{2})}\ (2.7.5)$$

\(i\) यदि fpc को ignore किया जाता है, तो हमारे पास है

$$n_{0} = \frac{t^{2}S^{2}}{e^{2}}\ (2.7.6)$$

\(ii\) यदि fpc को ignore नहीं किया जाता है, तो हम Eqn. (2.7.5) में $n_{0}$
की value रखकर $n$ की value प्राप्त कर सकते हैं और हमारे पास है,

$$n = \frac{n_{0}}{1 + n_{0}/N}\ (2.7.7)$$

**Example 2.7:** 500 sampling units वाली एक population में sampling
methods का एक अध्ययन (study) किया गया था। Total count से यह प्राप्त हुआ कि
$\bar{Y} = 49$ और $S^{2} = 44.6$ है। एक simple random sampling में, 10
प्रतिशत के permissible marginal error और 95 प्रतिशत confidence coefficient
के साथ $\bar{Y}$ का estimate लगाने के लिए कितनी sampling units चुनी जानी
चाहिए, जब sampling (i) replacement method के साथ (ii) without replacement
method के साथ की जाती है?\
(i) Sampling with replacement - इस मामले में, हम fpc को ignore कर सकते हैं और
हमारे पास है

$$n_{0} = \frac{t^{2}S^{2}}{e^{2}} = \frac{(1.96)^{2} \times 44.6}{(4.9)^{2}} = 7.136 \approx 8$$

\(ii\) Sampling without replacement - इस मामले में, fpc को ignore नहीं किया
जा सकता है और हम लेते हैं

$$n = \frac{n_{0}}{1 + n_{0}/N} = \frac{7.136}{1 + 7.136/500} = 7.035 \approx 8$$

इसी तरह, हम इन results पर तब भी चर्चा कर सकते हैं जब sampling units को किसी
characteristic की उपस्थिति (presence) या अनुपस्थिति (absence) द्वारा
classify किया जाता है। समान धारणाओं (notions) के साथ, sample proportion $p$
को $P$ और variance $(N - n)P(1 - P)/n(N - 1)$ के साथ normally distributed
माना जा सकता है। इसलिए, precision के pre-assigned level के साथ $n$ की value
का estimate इसके द्वारा लगाया जा सकता है

$$e = t(\alpha)\sqrt{\frac{(N - n)P(1 - P)}{n(N - 1)}}\ (2.7.8)$$

जहाँ $t(\alpha)$ का वही अर्थ है जो relation (2.7.4) में दिया गया है, जो देता है

$$n = \frac{Nt^{2}P(1 - P)/e^{2}}{N - 1 + t^{2}P(1 - P)/e^{2}}\ (2.7.9)$$

\(i\) यदि fpc को ignore किया जाता है, तो हमारे पास है

$$n_{0} = \frac{t^{2}P(1 - P)}{e^{2}}\ (2.7.10)$$

\(ii\) यदि fpc को ignore नहीं किया जाता है, तो हमें मिलता है

$$n = \frac{n_{0}}{1 + (n_{0} - 1)/N}\ (2.7.11)$$

**Example 2.8:** 4000 लोगों की एक population में जिन्हें अपना वोट डालने के लिए
बुलाया गया था, 50 प्रतिशत मतदान के लिए लौटे। इस proportion का estimate लगाने
के लिए sample size का estimate लगाएं ताकि marginal error 95 प्रतिशत
confidence coefficient के साथ 5 प्रतिशत हो, जब sampling (i) with
replacement और (ii) without replacement methods के साथ की जाती है।\
(i) Sampling with replacement - इस मामले में, हम fpc को ignore कर सकते हैं और
हमारे पास है,

$$n_{0} = \frac{t^{2}P(1 - P)}{e^{2}} = \frac{(1.96)^{2}(0.5)(0.5)}{0.0025} \approx 385$$

\(ii\) Sampling without replacement - इस मामले में, fpc को ignore नहीं किया
जा सकता है और हमारे पास है,

$$n = \frac{n_{0}}{1 + (n_{0} - 1)/N} = \frac{385}{1 + 384/4000} = 352$$

**SET OF PROBLEMS (समस्याओं का समूह)**

**2.1** मान लीजिए, serially numbered $N$ फैक्ट्रियों की एक list में, $m$
फैक्ट्रियां अस्तित्व से बाहर हो गई हैं (out of existence) और list में $n$ नई
फैक्ट्रियां जोड़ी गई हैं जिससे फैक्ट्रियों की कुल संख्या $(N - m + n)$ हो गई है। मूल
(original) $N$ फैक्ट्रियों को फिर से numbering करने से बचते हुए, $(N - m + n)$
फैक्ट्रियों से समान probability (equal probability) के साथ एक फैक्ट्री select करने
के लिए एक सरल procedure बताएं और दिखाएं कि आपकी procedure नई फैक्ट्रियों के लिए
समान probability प्राप्त करती है।

**2.2** Random numbers की मदद से, निम्नलिखित में से प्रत्येक से size 5 के random
samples निकालें:\
(i) Cauchy\'s population:

$$f(x) = \frac{1}{\pi}\frac{\lambda}{\lambda^{2} + (x - \mu)^{2}}$$

जहाँ $- \infty < x < \infty$ और $\lambda = 3.8$ cm और $\mu = - 2.1$ cm
है।\
(ii) Normal population:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}exp\left\{ - \frac{(x - \mu)^{2}}{2\sigma^{2}} \right\}\  - \infty < x < \infty$$

$\mu = 8$ और $\sigma = 2$\
(iii) Bivariate normal population जिसमें दो variates, $x$ और $y$ के means
क्रमशः 68 cm और 170 kg हैं; $x$ और $y$ के s.d क्रमशः 3 cm और 7 kg हैं; और
correlation coefficient $\rho$ है (i) $+ 1$ (ii) 0 और (iii) $- 1$।

**2.3** धान (paddy) पर crop-cutting experiments के लिए खेतों (fields) का
sample select करने के लिए निम्नलिखित procedure का उपयोग किया गया है:\
प्रत्येक selected गाँव के नाम के सामने highest survey number से छोटी तीन random
numbers दिखाई गई हैं। ये random numbers crop-cutting experiments के लिए तीन
धान के खेतों के अनुरूप (correspond) हैं। यदि selected survey number में धान नहीं
उगता है, तो उसके स्थान पर अगला धान उगाने वाला survey number select करें।\
यह जांचें कि क्या उपरोक्त method गाँव में सभी धान उगाने वाले survey numbers को
sample में शामिल होने का समान अवसर (equal chance) प्रदान करेगा, यह देखते हुए:\
(i) गाँव का नाम: पयागपुर (Payagpur)\
(ii) Survey numbers की कुल संख्या: 299\
(iii) Random numbers: 28, 189, 269\
(iv) धान उगाने वाले survey numbers: 39 से 88 और 189 से 299\
दिखाएं कि survey number 39 के sample में शामिल होने का chance $39/299$ है,
survey number 189 का chance $101/299$ है, जबकि शेष (remaining) survey
numbers में से प्रत्येक का chance केवल $1/299$ है। (I.C.A.R., 1951)

**2.4** एक population में $N$ units हैं, एक unit का variate value $y_{0}$
ज्ञात है। शेष $(N - 1)$ units से एक random sample, wor निकाला जाता है। दिखाएं
कि estimator $\bar{y} + (N - 1)y_{0}$ का variance संपूर्ण population से
निकाले गए size $n$ के random sample, wor पर आधारित $N\bar{y}$ की तुलना में
छोटा है।

**2.5** (i) Simple random sampling को Define करें। क्या sample mean,
population mean का एक consistent और unbiased estimator है? Sample mean का
variance दें और इस variance का unbiased estimate भी दें। एक दी गई standard
error के साथ population mean का estimate लगाने के लिए कितने sample size की
आवश्यकता है?\
(ii) साथ ही, यदि sample में $n_{1}$ units type A की हैं, तो population में
type A की units के proportion का एक unbiased estimate दें और इसका sampling
variance और estimate प्राप्त करें। यदि sample size पर्याप्त रूप से बड़ा है, तो
population में type A की units के unknown proportion के लिए 95% confidence
limits लिखें।

**2.6** मान लीजिए $N$ units की population से replacement के साथ equal
probability के साथ चुने गए $n$ units के sample में $\nu$ distinct units आती हैं।
दिखाएं कि estimator
$\frac{N}{n}\sum_{i = 1}^{\nu}\mspace{2mu}\frac{y_{i}}{\pi_{i}}$
population mean के लिए unbiased है। इस estimator के variance का एक unbiased
estimator प्राप्त करें।

**2.7** $n$ units के एक random sample से, $m$ units का एक random
sub-sample बिना replacement के निकाला जाता है और original sample में जोड़ा
जाता है। दिखाएं कि $(n + m)$ units पर आधारित mean, population mean का एक
unbiased estimator है, और इसके variance का original $n$ units के mean के
variance से अनुपात (ratio) लगभग $(1 + 3m/n)/(1 + m/n)^{2}$ है, यह मानते हुए
कि population size बड़ा है।

**2.8** एक finite population से बिना replacement के निकाले गए एक simple
random sample के variance के लिए expression (व्यंजक) प्राप्त करें। $Mp$ लाल और
$Mq$ सफेद गेंदों (balls) की आपूर्ति से random तौर पर निकाली गई $N$ गेंदों को एक
lot container में रखा जाता है। फिर lot container से random तौर पर $n$ गेंदों का
एक sample निकाला जाता है और एक sample container में रखा जाता है। यह पाया गया
है कि, इन $n$ गेंदों में से, $r$ लाल हैं। $V(r)$ ज्ञात करें जब $N$ गेंदों को lot
container में (i) with replacement और (ii) without replacement के साथ रखा
जाता है।

**2.9** Simple random sampling में, sample mean का variance
$V(\bar{y}) = N^{2}(1/n - 1/N)\frac{\sum_{}^{}\ y_{i}^{2} - N{\bar{y}}^{2}}{N - 1}$
द्वारा दिया जाता है। $V(\bar{y})$ के एक unbiased estimator को $v$ द्वारा
दर्शाते हुए और यह ध्यान देते हुए कि
$E\left\lbrack \frac{N}{n}\sum_{}^{}\ y_{i}^{2} \right\rbrack = \sum_{}^{}\ y_{i}^{2}$,
दिखाएं कि

$$E(v) = \frac{1}{N - 1}E\left\lbrack \frac{N - n}{n}\left( \frac{N}{n}\sum_{}^{}\ y_{i}^{2} - N({\bar{y}}^{2} - v) \right) \right\rbrack$$

**2.10** एक निश्चित तहसील (tehsil) के 100 गाँवों की गेहूं की फसल (wheat crop) के
लिए उपज (yield) क्विंटल में नीचे दी गई है। (कोष्ठक (brackets) के भीतर के आंकड़े गाँव
के numbers को दर्शाते हैं)।\
(i) Size 20 और 25 units के simple random samples चुनें और selected units के
आधार पर उनकी standard errors के साथ प्रति plot average yield का estimate
लगाएं।\
(ii) 95 प्रतिशत confidence interval स्थापित करें और टिप्पणी (comment) करें।\
(iii) 5 प्रतिशत standard error के साथ mean yield का estimate लगाने के लिए
आवश्यक sample का size प्राप्त करें।

  ---------------------------------------------
  \(1\) 20 \(2\) 21 \(3\) 32 \(4\) 41 \(5\) 55
  -------- -------- -------- -------- ---------
  \(6\) 22 \(7\) 64 \(8\) 42 \(9\) 28 \(10\) 35

  \(11\)   \(12\)   \(13\)   \(14\)   \(15\) 75
  25       25       24       32       

  \(16\)   \(17\)   \(18\)   \(19\)   \(20\) 19
  28       29       38       19       

  \(21\)   \(22\)   \(23\)   \(24\)   \(25\) 29
  16       28       30       29       

  \(26\)   \(27\)   \(28\)   \(29\)   \(30\) 35
  19       37       34       31       

  \(31\)   \(32\)   \(33\)   \(34\)   \(35\) 39
  29       19       27       42       

  \(36\)   \(37\)   \(38\)   \(39\)   \(40\) 61
  11       26       21       45       

  \(41\)   \(42\)   \(43\)   \(44\)   \(45\) 63
  16       29       32       40       

  \(46\)   \(47\)   \(48\)   \(49\)   \(50\) 18
  30       21       35       28       

  \(51\)   \(52\)   \(53\)   \(54\) 8 \(55\) 35
  24       32       23                

  \(56\)   \(57\)   \(58\)   \(59\)   \(60\) 29
  27       35       25       29       

  \(61\)   \(62\)   \(63\)   \(64\)   \(65\) 43
  25       31       38       31       

  \(66\)   \(67\)   \(68\)   \(69\)   \(70\) 47
  21       36       30       37       

  \(71\)   \(72\)   \(73\)   \(74\)   \(75\) 50
  15       19       32       19       

  \(76\)   \(77\)   \(78\)   \(79\)   \(80\) 43
  10       27       36       28       

  \(81\)   \(82\)   \(83\)   \(84\) 6 \(85\) 4
  28       25       31                

  \(86\)   \(87\)   \(88\)   \(89\)   \(90\) 44
  22       24       39       71       

  \(91\)   \(92\)   \(93\)   \(94\)   \(95\) 10
  24       34       18       28       

  \(96\)   \(97\)   \(98\)   \(99\)   \(100\)
  70       20       32       42       47
  ---------------------------------------------

**2.11** भारत में ग्रो-मोर-फूड (Grow-More-Food) अभियान के हिस्से के रूप में एक जिले
में वर्ष 1964 के दौरान 5000 कुओं (wells) के निर्माण के लिए सामग्री (Material) जारी
की गई थी। उन किसानों (cultivators) की list जिन्हें यह जारी किया गया था, साथ
ही प्रत्येक कुएं का proposed location उपलब्ध है। वास्तव में निर्मित (constructed)
और सिंचाई (irrigation) उद्देश्य के लिए उपयोग किए गए कुओं के proportion $p$ का
estimate लगाने का प्रस्ताव है। Sample को simple random sampling द्वारा select
करने का प्रस्ताव है। $P$ के 0.5 से 0.9 तक की values के लिए sample का size
निर्धारित करें, यदि error का permissible margin 10 प्रतिशत है और assurance
(आश्वासन) की desired degree 95 प्रतिशत है।

**2.12** नीचे दिया गया डेटा एक संगठित डेरी फार्म (organised dairy farm) में 250
गायों के दूध की उपज (10 kg में) के एक पूर्ण स्तनपान (complete lactation) से संबंधित
है।

\(i\) Size 25 का एक simple random sample चुनें।\
(ii) इसकी standard error के साथ mean का estimate लगाएं।\
(iii) Population mean के लिए 95 प्रतिशत confidence limit का निर्माण करें।

\| 230 \| 293 \| 163 \| 290 \| 200 \| 173 \| 194 \| 322 \| 169 \| 230
\|\
\| 297 \| 151 \| 248 \| 271 \| 259 \| 214 \| 167 \| 207 \| 240 \| 286
\|\
\| 184 \| 248 \| 327 \| 338 \| 165 \| 177 \| 270 \| 177 \| 202 \| 155
\|\
\| 155 \| 293 \| 190 \| 172 \| 150 \| 319 \| 151 \| 118 \| 213 \| 114
\|\
\| 186 \| 167 \| 129 \| 185 \| 231 \| 199 \| 265 \| 306 \| 173 \| 276
\|\
\| 291 \| 231 \| 205 \| 220 \| 246 \| 239 \| 186 \| 299 \| 233 \| 208
\|\
\| 265 \| 204 \| 300 \| 195 \| 239 \| 173 \| 237 \| 282 \| 221 \| 218
\|\
\| 197 \| 215 \| 213 \| 290 \| 146 \| 232 \| 305 \| 184 \| 149 \| 267
\|\
\| 188 \| 219 \| 171 \| 99 \| 329 \| 199 \| 180 \| 225 \| 257 \| 202 \|\
\| 189 \| 207 \| 792 \| 327 \| 201 \| 300 \| 206 \| 199 \| 299 \| 153
\|\
\| 175 \| 287 \| 277 \| 230 \| 258 \| 137 \| 174 \| 301 \| 260 \| 282
\|\
\| 211 \| 212 \| 284 \| 214 \| 283 \| 139 \| 223 \| 212 \| 207 \| 224
\|\
\| 207 \| 111 \| 272 \| 192 \| 127 \| 303 \| 221 \| 187 \| 309 \| 263
\|\
\| 203 \| 176 \| 233 \| 239 \| 176 \| 218 \| 193 \| 243 \| 236 \| 275
\|\
\| 288 \| 198 \| 241 \| 219 \| 167 \| 193 \| 234 \| 179 \| 126 \| 173
\|\
\| 279 \| 178 \| 275 \| 260 \| 191 \| 174 \| 235 \| 338 \| 242 \| 238
\|\
\| 211 \| 187 \| 184 \| 189 \| 305 \| 221 \| 253 \| 225 \| 327 \| 203
\|\
\| 195 \| 158 \| 156 \| 185 \| 170 \| 271 \| 160 \| 188 \| 165 \| 218
\|\
\| 312 \| 143 \| 267 \| 298 \| 196 \| 139 \| 205 \| 298 \| 238 \| 217
\|\
\| 145 \| 201 \| 313 \| 230 \| 185 \| 166 \| 147 \| 223 \| 271 \| 133
\|\
\| 155 \| 230 \| 287 \| 329 \| 265 \| 150 \| 286 \| 271 \| 268 \| 198
\|\
\| 214 \| 231 \| 163 \| 335 \| 198 \| 270 \| 187 \| 174 \| 163 \| 201
\|\
\| 192 \| 247 \| 247 \| 297 \| 178 \| 240 \| 290 \| 234 \| 170 \| 227
\|\
\| 230 \| 353 \| 170 \| 159 \| 236 \| 181 \| 230 \| 240 \| 212 \| 242
\|\
\| 151 \| 158 \| 253 \| 179 \| 263 \| 158 \| 250 \| 226 \| 246 \| 301 \|

**2.13** एक देश में 232 शहरों का frequency distribution, population size
(000) के अनुसार नीचे दिया गया है:

  -----------------------------------------------------------------------
  Population     No. of   Population     No. of   Population     No. of
  size class     cities   size class     cities   size class     cities
  -------------- -------- -------------- -------- -------------- --------
  50-75          81       500-550        2        1800-1850      1

  75-100         45       550-600        3        1850-1950      0

  100-150        42       600-650        1        1950-2000      1

  150-200        14       650-700        1        2000-2050      0

  200-250        9        700-750        0        2050-2100      1

  250-300        5        750-800        1        2100-3600      0

  300-350        6        800-850        2        3600-3650      1

  350-400        5        850-900        1        3650-7850      0

  400-450        5        900-950        2        7850-7900      1

  450-500        2        950-1800       0                       
  -----------------------------------------------------------------------

**REFERENCES (संदर्भ)**

Cochran, W.G., *Sampling Techniques*, John Wiley & Sons, New York,
(1977).\
Deming, W.E., *Some Theory of Sampling*, John Wiley & Sons, New York,
(1950).\
Fisher, R.A., *The Design of Experiments*, Oliver & Boyd, London
(1935).\
\"The Sub-Commission on Statistical Sampling of the United Nations,\"
*Bull. Int. Statist. Inst.* 32, 207-209, (1950).\
Hansen, M.H., Hurwitz, W.N. and Jabine, T.B., \"The use of imperfect
lists for probability sampling at the U.S. Bureau of the Census,\"
*Bull. Int. Statist. Inst.*, 40, 497-517, (1963).\
Lahiri, D.B., \"Some thoughts on multi-subject sample survey system,\"
*Contributions to Statistics*, 175-220 (Presented to Professor P.C.
Mahalanobis on his 70th Birthday). Statistical Publishing Society,
Calcutta, (1963).\
Mahalanobis, P.C., \"On large-scale sample surveys\", *Phil. Trans. R.
Soc.*, 231, 329-451, (1944). \"Cost and accuracy of results in sampling
and complete enumeration\", *Bull. Int. Statist. Inst.*, 32, 210-213,
(1950).\
Seal, K.C., \"Use of outdated frames in large sample surveys\" *Bull.
Cal. Statist. Assoc.*, 11, 68-84, (1962).\
Singh, D., *Taking Agricultural Censuses*, FAO, Rome (1978).\
United Nations, \"Recommendations concerning the preparation of reports
on sampling surveys.\" *Statistical Paper Series, C, 1*, New York,
revised in 1964, *Statistical Paper Series, C, 1, rev. 2*, (1949).\
Yates, F., *Sampling Methods for Censuses and Surveys*, Charles Griffin
& Co., London, (1960).\
Zarkovich, S.S., *Sampling Methods and Censuses*. Food and Agricultural
Organization of the United Nations, Rome, (1961).
