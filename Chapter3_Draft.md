# CHAPTER 3: STRATIFIED RANDOM SAMPLING

> "Sir, In your otherwise beautiful poem ("The Vision of Sin") there is a verse which reads "Every moment dies a man, every moment one is born." Obviously, this cannot be true and I suggest that in the next edition you have it read "Every moment dies a man, every moment 1\frac{1}{16} is born." Even this value is slightly in error but should be sufficiently accurate for poetry." (in a letter to Lord Tennyson) – Charles Babbage

## 3.1 INTRODUCTION

**English Content:**
Welcome class! Today we are discussing Stratified Random Sampling. Of all the methods of sampling, this procedure is the most commonly used in practical surveys. In stratified sampling, our entire population of $N$ units is divided into $k$ sub-groups or sub-populations, which we call **strata**. The $i$-th stratum has $N_i$ units, where $i = 1, 2, ..., k$. 

These strata are non-overlapping and together they comprise the entire population. This means:
$$ N_1 + N_2 + ... + N_k = N $$

From each stratum, a sample is drawn independently. The sample size taken from the $i$-th stratum is $n_i$, such that the total sample size $n$ is:
$$ n_1 + n_2 + ... + n_k = n $$

When the sample is taken randomly from each stratum, the procedure is known as **stratified random sampling**. The main objective of this stratification is to give a better cross-section of the population to gain a higher degree of relative precision. To achieve this, we must carefully consider four points:
1. Formation of strata
2. Number of strata to be made
3. Allocation of sample size within each stratum
4. Analysis of data from a stratified design

---

**Hinglish Content:**
Welcome class! Aaj hum Stratified Random Sampling padhenge. Sampling ke sabhi methods mein, practical surveys mein sabse zyada yahi method use hota hai. Stratified sampling mein, hum apni $N$ units ki puri population ko $k$ sub-groups mein baant dete hain, jinhein hum **strata** kehte hain. $i$-th stratum mein $N_i$ units hote hain.

Ye strata non-overlapping hote hain (yaani ek unit sirf ek hi stratum mein aayegi) aur sab milkar puri population banate hain:
$$ N_1 + N_2 + ... + N_k = N $$

Har ek stratum se hum alag se aur independently ek sample nikalte hain. Agar $i$-th stratum se $n_i$ units ka sample nikala, toh total sample size $n$ banega:
$$ n_1 + n_2 + ... + n_k = n $$

Jab hum har stratum se randomly sample nikalte hain, toh is procedure ko **stratified random sampling** kehte hain. Stratification ka main objective ye hai ki humein population ka ek better cross-section mile, taaki hamare estimates zyada precise (sateek) ho sakein. Ise achieve karne ke liye humein 4 baaton ka dhyan rakhna hota hai:
1. Strata kaise banayein (Formation)
2. Kitne strata banayein (Number)
3. Har stratum se kitna sample lein (Allocation)
4. Stratified data ka analysis kaise karein

## 3.2 PRINCIPLES OF STRATIFICATION

**English Content:**
When stratifying a population, you should follow these principles:
1. The strata should be non-overlapping and should together comprise the whole population.
2. The stratification of the population should be done in such a way that strata are homogeneous within themselves, with respect to the characteristic under study.
3. In many practical situations, when it is difficult to stratify with respect to the characteristic under study, administrative convenience may be considered as the basis for stratification.
4. If the limit of precision for certain sub-populations is given, it will be better to treat each sub-population as a separate stratum.

---

**Hinglish Content:**
Population ko stratify karte waqt aapko in principles ko follow karna chahiye:
1. Strata non-overlapping hone chahiye aur sabhi strata milkar puri population ko cover karne chahiye.
2. Population ka stratification is tarah hona chahiye ki har stratum ke andar ki units aapas mein homogeneous (ek jaisi) ho, specially us characteristic ke regarding jo hum study kar rahe hain.
3. Bahut si practical situations mein study characteristic ke basis par stratify karna mushkil hota hai. Aise mein, administrative convenience (jaise blocks, tehsils ya zones) ko stratification ka basis maan lena chahiye.
4. Agar humein pehle se bataya gaya hai ki kuch sub-populations ke liye ek specific precision limit chahiye, toh behtar hoga ki un sub-populations ko hum alag se ek stratum maan lein.

## 3.3 ADVANTAGES OF STRATIFICATION

**English Content:**
Stratification serves many useful purposes. The principal ones are:
1. **Administrative Convenience:** The survey agency can establish field offices in various administrative zones, leading to better organization and supervision of fieldwork.
2. **Improving Sampling Design:** Stratification by natural characteristics helps. For example, in yield surveys, plains, deserts, and hilly areas have different sampling problems, so they can be separate strata.
3. **Handling Extreme Values:** Extreme values in the population can be segregated into separate strata, reducing variability within other strata. Separate estimates can be combined for a precise overall estimate.
4. **Different Sampling Designs:** You can use different sampling designs in different strata based on what information is available for those units.
5. **Adequate Representation:** It ensures adequate representation to various important groups of the population.
6. **Better Cross-section:** It ensures the selection of a better cross-section of the population than an unstratified approach.
7. **Gain in Precision:** By subdividing a heterogeneous population into homogeneous sub-populations, measurements vary less within each stratum, allowing us to get a more precise estimate with a relatively smaller sample.

---

**Hinglish Content:**
Stratification ke bahut se fayde hain, jinmein se main ye hain:
1. **Administrative Convenience (Prashasnik Suvidha):** Survey agency alag-alag zones mein apne field offices bana sakti hai, jisse field work ka supervision achhe se ho pata hai.
2. **Sampling Design ko Improve karna:** Natural characteristics ke basis par stratification bahut madad karta hai. Jaise kheti ke surveys mein maidaani (plains), registaani (deserts) aur pahaadi (hilly) ilaqon ki alag problems hoti hain, toh unhe alag strata banana chahiye.
3. **Extreme Values ko Handle karna:** Population mein jo extreme values hoti hain, unhe alag stratum mein daal kar baki strata ki variability kam ki ja sakti hai. In sabke alag estimates nikal kar ek precise overall estimate banaya ja sakta hai.
4. **Different Sampling Designs ka Use:** Aap alag-alag strata mein alag-alag sampling methods (designs) use kar sakte hain, depend karta hai ki kahan kaisi information available hai.
5. **Adequate Representation:** Ye ensure karta hai ki population ke sabhi zaruri groups ko proper representation mile.
6. **Better Cross-section:** Bina stratification ke comparison mein, ye humein population ka ek behtar aur balanced cross-section deta hai.
7. **Precision mein Gain:** Ek heterogeneous (alag-alag prakar ki) population ko homogeneous (ek jaisi) sub-populations mein baantne se, har stratum ke andar variance kam ho jata hai. Isse hum chhote sample se bhi zyada sateek (precise) estimate nikal sakte hain.

## 3.4 NOTATIONS

**English Content:**
Let's define our notations carefully. Let $k$ denote the number of strata, $i$ denote a specific stratum, and $j$ denote a sampling unit within that stratum.
For the $i$-th stratum:
- $N_i$: total number of units in the stratum
- $n_i$: number of units in the sample from the stratum
- $W_i = \frac{N_i}{N}$: stratum weight
- $f_i = \frac{n_i}{N_i}$: sampling fraction in the stratum
- $y_{ij}$: value of the $j$-th unit in the $i$-th stratum

Parameters for the $i$-th stratum:
- $\bar{Y}_i = \frac{1}{N_i} \sum_{j=1}^{N_i} y_{ij}$ (Stratum mean)
- $\bar{y}_i = \frac{1}{n_i} \sum_{j=1}^{n_i} y_{ij}$ (Sample mean of the stratum)
- $S_i^2 = \frac{1}{N_i - 1} \sum_{j=1}^{N_i} (y_{ij} - \bar{Y}_i)^2$ (Stratum variance)
- $s_i^2 = \frac{1}{n_i - 1} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2$ (Sample variance of the stratum)

---

**Hinglish Content:**
Chaliye apne notations define karte hain. Maan lijiye $k$ total strata hain, $i$ kisi ek stratum ko darshata hai, aur $j$ us stratum ke andar ki ek sampling unit ko darshata hai.
$i$-th stratum ke liye:
- $N_i$: us stratum mein total units ki sankhya
- $n_i$: us stratum se nikale gaye sample mein units ki sankhya
- $W_i = \frac{N_i}{N}$: stratum ka weight
- $f_i = \frac{n_i}{N_i}$: stratum ka sampling fraction
- $y_{ij}$: $i$-th stratum ki $j$-th unit ki value

$i$-th stratum ke parameters:
- $\bar{Y}_i = \frac{1}{N_i} \sum_{j=1}^{N_i} y_{ij}$ (Stratum ka population mean)
- $\bar{y}_i = \frac{1}{n_i} \sum_{j=1}^{n_i} y_{ij}$ (Stratum ka sample mean)
- $S_i^2 = \frac{1}{N_i - 1} \sum_{j=1}^{N_i} (y_{ij} - \bar{Y}_i)^2$ (Stratum ka population variance)
- $s_i^2 = \frac{1}{n_i - 1} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2$ (Stratum ka sample variance)

## 3.5 ESTIMATION OF THE POPULATION MEAN AND ITS VARIANCE

**English Content:**
Suppose our population of $N$ units is divided into $k$ strata. The overall population mean per unit $\bar{Y}$ can be written as a weighted average of the strata means:
$$ \bar{Y} = \frac{1}{N} \sum_{i=1}^{k} N_i \bar{Y}_i = \sum_{i=1}^{k} W_i \bar{Y}_i $$

To estimate this, we construct an estimator denoted as $\bar{y}_{st}$ (where 'st' stands for stratified). It is defined as:
$$ \bar{y}_{st} = \frac{1}{N} \sum_{i=1}^{k} N_i \bar{y}_i = \sum_{i=1}^{k} W_i \bar{y}_i $$
Note that this is different from the overall simple sample mean $\bar{y} = \frac{1}{n} \sum_{i=1}^k n_i \bar{y}_i$.

**Theorem 3.5.1:** If in every stratum the sample estimator $\bar{y}_i$ is unbiased and samples are drawn independently in different strata, then $\bar{y}_{st}$ is an unbiased estimator of the population mean $\bar{Y}$ and its sampling variance is given by:
$$ V(\bar{y}_{st}) = \sum_{i=1}^{k} W_i^2 V(\bar{y}_i) $$

**Proof:**
Taking the expectation on both sides:
$$ E(\bar{y}_{st}) = E \left( \sum_{i=1}^{k} W_i \bar{y}_i \right) = \sum_{i=1}^{k} W_i E(\bar{y}_i) $$
Since the samples are drawn independently and each strata behaves like a population, $\bar{y}_i$ is an unbiased estimator of $\bar{Y}_i$, so $E(\bar{y}_i) = \bar{Y}_i$.
$$ E(\bar{y}_{st}) = \sum_{i=1}^{k} W_i \bar{Y}_i = \frac{1}{N} \sum_{i=1}^{k} N_i \bar{Y}_i = \bar{Y} $$
This shows that $\bar{y}_{st}$ is an unbiased estimator.

For the variance, since sampling is done independently in each stratum, the covariance terms between different strata are zero:
$$ V(\bar{y}_{st}) = V \left( \sum_{i=1}^{k} W_i \bar{y}_i \right) = \sum_{i=1}^{k} W_i^2 V(\bar{y}_i) $$
Hence, the theorem is proved.

**Theorem 3.5.2:** For stratified random sampling without replacement (WOR), the sample estimator $\bar{y}_{st}$ is unbiased and its sampling variance is given by:
$$ V(\bar{y}_{st}) = \sum_{i=1}^{k} W_i^2 \left( \frac{1}{n_i} - \frac{1}{N_i} \right) S_i^2 = \sum_{i=1}^{k} W_i^2 \frac{N_i - n_i}{N_i n_i} S_i^2 $$

**Proof:**
Since in each stratum, a simple random sample without replacement is taken, $\bar{y}_i$ is an unbiased estimator of $\bar{Y}_i$. By Theorem 3.5.1, $\bar{y}_{st}$ is unbiased for $\bar{Y}$.
Further, applying the known formula for variance of sample mean in SRSWOR to an individual stratum, we have:
$$ V(\bar{y}_i) = \left( \frac{1}{n_i} - \frac{1}{N_i} \right) S_i^2 = \frac{N_i - n_i}{N_i n_i} S_i^2 $$
Substituting this into the result of Theorem 3.5.1, we get:
$$ V(\bar{y}_{st}) = \sum_{i=1}^{k} W_i^2 \left( \frac{1}{n_i} - \frac{1}{N_i} \right) S_i^2 $$

**Corollary 1:** If $\hat{Y}_{st} = N \bar{y}_{st}$ is the estimator of the population total $Y$, then $\hat{Y}_{st}$ is an unbiased estimator and its sampling variance is:
$$ V(\hat{Y}_{st}) = V(N \bar{y}_{st}) = N^2 V(\bar{y}_{st}) = \sum_{i=1}^{k} N_i (N_i - n_i) \frac{S_i^2}{n_i} $$

**Corollary 2:** If in every stratum $\frac{n_i}{N_i}$ is negligible (meaning $N_i$ is very large), the variance reduces to:
$$ V(\bar{y}_{st}) \approx \sum_{i=1}^{k} W_i^2 \frac{S_i^2}{n_i} $$

**Corollary 3:** If in every stratum $\frac{n_i}{N_i}$ is negligible, and the variance in all strata has the same value $S_i^2 = S_w^2$, the result reduces to:
$$ V(\bar{y}_{st}) \approx \frac{S_w^2}{n} \sum_{i=1}^{k} \frac{W_i^2}{n_i} $$

**Corollary 4:** For stratified random sampling with replacement (WR), $\bar{y}_{st}$ is an unbiased estimator and its sampling variance is:
$$ V(\bar{y}_{st}) = \sum_{i=1}^{k} W_i^2 \frac{\sigma_i^2}{n_i} $$
where $\sigma_i^2 = \frac{N_i - 1}{N_i} S_i^2$.

**Theorem 3.5.3:** In stratified random sampling WOR, with sample size $n = \sum n_i$; an unbiased estimator of the population proportion $P$ is given by:
$$ p_{st} = \sum_{i=1}^{k} W_i p_i $$
with its variance:
$$ V(p_{st}) = \sum_{i=1}^{k} W_i^2 \left( \frac{N_i - n_i}{N_i - 1} \right) \frac{P_i Q_i}{n_i} $$
where $p_i$ is the sample estimate of proportion $P_i$ in the $i$-th stratum and $Q_i = 1 - P_i$.

*Corollary 1:* When $N_i / (N_i - 1)$ can be taken as unity, we have:
$$ V(p_{st}) = \sum_{i=1}^{k} W_i^2 \left( 1 - f_i \right) \frac{P_i Q_i}{n_i} $$

*Corollary 2:* If sampling is with replacement:
$$ V(p_{st}) = \sum_{i=1}^{k} W_i^2 \frac{P_i Q_i}{n_i} $$

*Corollary 3:* If $f_i$ is negligible, the sampling variance reduces to:
$$ V(p_{st}) = \sum_{i=1}^{k} W_i^2 \frac{P_i Q_i}{n_i} $$

---

**Hinglish Content:**
Maan lijiye hamari $N$ units ki population $k$ strata mein divided hai. Overall population ka mean $\bar{Y}$ hum strata means ke weighted average ke roop mein likh sakte hain:
$$ \bar{Y} = \sum_{i=1}^{k} W_i \bar{Y}_i $$

Iska estimate nikalne ke liye hum $\bar{y}_{st}$ (stratified mean) banate hain:
$$ \bar{y}_{st} = \sum_{i=1}^{k} W_i \bar{y}_i $$
Dhyan dein ki ye simple sample mean $\bar{y}$ se alag hai, kyunki yahan hum population weights $W_i$ ka use kar rahe hain.

**Theorem 3.5.1:** Agar har stratum mein sample estimator $\bar{y}_i$ unbiased hai, aur samples independently draw kiye gaye hain, toh $\bar{y}_{st}$ bhi $\bar{Y}$ ka unbiased estimator hota hai. Iska variance hota hai:
$$ V(\bar{y}_{st}) = \sum_{i=1}^{k} W_i^2 V(\bar{y}_i) $$
**Proof (Praman):** Expectation lene par, kyuki samples independent hain aur $\bar{y}_i$ unbiased hai, $E(\bar{y}_{st}) = \sum W_i E(\bar{y}_i) = \sum W_i \bar{Y}_i = \bar{Y}$. Aur variance lene par covariance terms zero ho jayengi, isliye $V(\bar{y}_{st}) = \sum W_i^2 V(\bar{y}_i)$.

**Theorem 3.5.2:** Agar hum Without Replacement (WOR) sampling karte hain, toh:
$$ V(\bar{y}_{st}) = \sum_{i=1}^{k} W_i^2 \frac{N_i - n_i}{N_i n_i} S_i^2 $$
**Proof:** Hum jaante hain ki SRSWOR mein ek stratum ka variance $V(\bar{y}_i) = \frac{N_i - n_i}{N_i n_i} S_i^2$ hota hai. Bas isko Theorem 3.5.1 wale formula mein put kar dijiye, aapko result mil jayega. Isme koi mushkil nahi hai.

Iske baad 4 choti Corollaries aati hain. 
- *Corollary 1* mein Total $Y$ ke liye variance nikalte hain bas $N^2$ se multiply karke.
- *Corollary 2* kehti hai ki agar population $N_i$ bahut badi ho (finite population correction yaani fpc chhod dein), toh variance $\sum W_i^2 \frac{S_i^2}{n_i}$ bachega.
- *Corollary 3* kehti hai ki fpc chhodne ke baad agar sab strata ka variance $S_w^2$ same ho, toh ye formula aur simple ho jata hai.
- *Corollary 4* kehti hai ki With Replacement (WR) ke case mein formula mein $S_i^2$ ki jagah $\sigma_i^2$ use hota hai.

**Theorem 3.5.3** same logic ko Proportions $P$ (jaise "kitne log pass hue") ke liye apply karti hai. Iska estimator $p_{st} = \sum W_i p_i$ hota hai aur variance mein $S_i^2$ ki jagah $P_i Q_i$ aa jata hai, jo binomial nature dikhata hai.

## 3.6 ESTIMATE OF VARIANCE

**English Content:**
In practice, the population parameters $S_i^2$ are unknown, so we must estimate $V(\bar{y}_{st})$ from our sample data.
If a simple random sample is taken within each stratum, an unbiased estimator of $S_i^2$ is given by the sample variance $s_i^2$:
$$ s_i^2 = \frac{1}{n_i - 1} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2 $$

**Theorem 3.6:** With stratified random sampling (WOR), an unbiased estimator of the variance of $\bar{y}_{st}$ (denoted as $\widehat{V}(\bar{y}_{st})$ or $v(\bar{y}_{st})$) is given by:
$$ \widehat{V}(\bar{y}_{st}) = v(\bar{y}_{st}) = \sum_{i=1}^{k} W_i^2 \left( \frac{1}{n_i} - \frac{1}{N_i} \right) s_i^2 $$

**Corollary 1:** With stratified random sampling (WOR), an unbiased estimator of $V(\hat{Y}_{st})$ reduces to:
$$ v(\hat{Y}_{st}) = \sum_{i=1}^{k} N_i (N_i - n_i) \frac{s_i^2}{n_i} $$

**Corollary 2:** With stratified random sampling (WOR) for proportions, an unbiased estimator of $V(p_{st})$ is given by:
$$ v(p_{st}) = \sum_{i=1}^{k} W_i^2 \left( \frac{N_i - n_i}{N_i} \right) \frac{p_i q_i}{n_i - 1} $$
where $q_i = 1 - p_i$.

---

**Hinglish Content:**
Asli surveys mein humein population ka variance $S_i^2$ pata nahi hota. Toh hum uski jagah sample se calculate kiya gaya $s_i^2$ use karte hain.

**Theorem 3.6:** Agar hum SRSWOR use kar rahe hain, toh $\bar{y}_{st}$ ke variance ka unbiased estimate nikalne ke liye hum seedha $S_i^2$ ki jagah $s_i^2$ rakh dete hain:
$$ v(\bar{y}_{st}) = \sum_{i=1}^{k} W_i^2 \left( \frac{1}{n_i} - \frac{1}{N_i} \right) s_i^2 $$
Iska proof bahut hi sidha hai kyuki humein pata hai ki $E(s_i^2) = S_i^2$ hota hai. 
**Corollary 1** mein Population Total ke variance ka estimate diya hai jismein wahi $N^2$ ka logic lagta hai. 
**Corollary 2** proportions ke liye batati hai ki variance ko estimate karne ke liye hum $P_i Q_i$ ki jagah $p_i q_i$ use karte hain, bas dhyan rahe denominator mein $n_i - 1$ aayega unbiasedness maintain karne ke liye.

## 3.7 ALLOCATION OF SAMPLE SIZE IN DIFFERENT STRATA

**English Content:**
In stratified sampling, allocating the sample $n$ to different strata depends on three factors:
1. The total number of units in the stratum (stratum size $N_i$).
2. The variability within the stratum ($S_i$).
3. The cost in taking observations per unit in the stratum ($c_i$).

A good allocation provides maximum precision with minimum resources. There are four methods of allocation:
1. Equal allocation
2. Proportional allocation
3. Neyman allocation
4. Optimum allocation

### 3.7.1 Equal Samples From Each Stratum
For administrative convenience, the total sample size $n$ is divided equally among all strata.
$$ n_i = \frac{n}{k} $$

### 3.7.2 Proportional Allocation
Originally proposed by Bowley (1926). When only the sizes $N_i$ are known, the sample is allocated proportional to the stratum size:
$$ n_i \propto N_i \implies n_i = n \frac{N_i}{N} = n W_i $$
This makes the sampling fraction constant ($f_i = \frac{n_i}{N_i} = \frac{n}{N}$), leading to a self-weighting sample.

### 3.7.3 Neyman Allocation
Due to Neyman (1934), this is the minimum variance allocation. Assuming cost per unit is the same across strata, it considers both size and variability:
$$ n_i \propto N_i S_i \implies n_i = n \frac{N_i S_i}{\sum N_i S_i} $$
Minimum variance is achieved here:
$$ V(\bar{y}_{st})_{Neyman} = \frac{1}{n} \left( \sum_{i=1}^{k} W_i S_i \right)^2 - \frac{1}{N} \sum_{i=1}^{k} W_i S_i^2 $$

### 3.7.4 Optimum Allocation
This determines $n_i$ to minimize variance for a specified cost, or minimize cost for a specified variance. 
Cost function: $C = C_0 + \sum_{i=1}^k c_i n_i$ where $C_0$ is overhead cost, $c_i$ is cost per unit.

**Theorem:** Show that in optimum allocation in stratified sampling $n_i \propto \frac{N_i S_i}{\sqrt{c_i}}$.
**Proof (Lagrange Multipliers):**
Let us define Lagrange's multiplier $\lambda$ and formulate the function $\phi$:
$$ \phi = V(\bar{y}_{st}) + \lambda (C - C_0 - \sum c_i n_i) $$
We know that $V(\bar{y}_{st}) = \sum_{i=1}^{k} W_i^2 S_i^2 \left( \frac{1}{n_i} - \frac{1}{N_i} \right)$.
So,
$$ \phi = \sum_{i=1}^{k} \frac{W_i^2 S_i^2}{n_i} - \sum_{i=1}^{k} \frac{W_i^2 S_i^2}{N_i} + \lambda \left( \sum_{i=1}^{k} c_i n_i - (C - C_0) \right) $$
Differentiating with respect to $n_i$ and equating to zero:
$$ \frac{\partial \phi}{\partial n_i} = - \frac{W_i^2 S_i^2}{n_i^2} + \lambda c_i = 0 $$
$$ \implies n_i^2 = \frac{W_i^2 S_i^2}{\lambda c_i} \implies n_i = \frac{W_i S_i}{\sqrt{\lambda c_i}} \implies n_i = \frac{1}{\sqrt{\lambda}} \frac{W_i S_i}{\sqrt{c_i}} $$
Taking the summation over all strata:
$$ \sum_{i=1}^{k} n_i = n = \frac{1}{\sqrt{\lambda}} \sum_{i=1}^{k} \frac{W_i S_i}{\sqrt{c_i}} $$
Therefore,
$$ \sqrt{\lambda} = \frac{\sum (W_i S_i / \sqrt{c_i})}{n} $$
Substituting $\sqrt{\lambda}$ back into the equation for $n_i$:
$$ n_i = \frac{n (W_i S_i / \sqrt{c_i})}{\sum (W_i S_i / \sqrt{c_i})} $$
Since $W_i = N_i / N$, the $N$ cancels out from numerator and denominator, showing that:
$$ n_i \propto \frac{N_i S_i}{\sqrt{c_i}} $$
This relation leads to the conclusion that we should take a larger sample in a stratum if:
1. The stratum size is larger ($N_i$ is large).
2. The stratum has larger variability ($S_i$ is large).
3. The cost per unit is cheaper in that stratum ($c_i$ is small).

**Determination of sample size $n$ under Optimum Allocation:**
**Case I:** When cost $C$ is fixed and we want to minimize variance.
Substituting $n_i$ into the cost function $C = C_0 + \sum c_i n_i$:
$$ C - C_0 = \sum c_i \left( \frac{n \frac{W_i S_i}{\sqrt{c_i}}}{\sum \frac{W_i S_i}{\sqrt{c_i}}} \right) = \frac{n}{\sum \frac{W_i S_i}{\sqrt{c_i}}} \sum (W_i S_i \sqrt{c_i}) $$
$$ \implies n = \frac{(C - C_0) \sum (W_i S_i / \sqrt{c_i})}{\sum (W_i S_i \sqrt{c_i})} $$

**Case II:** When variance $V$ is fixed and we minimize cost.
Using the variance formula $V = \sum \frac{W_i^2 S_i^2}{n_i} - \frac{1}{N} \sum W_i S_i^2$, and substituting $n_i$:
We eventually get:
$$ n = \frac{\left( \sum W_i S_i \sqrt{c_i} \right) \left( \sum W_i S_i / \sqrt{c_i} \right)}{V + \frac{1}{N} \sum W_i S_i^2} $$

---

**Hinglish Content:**
Jab hum stratified sampling karte hain, toh sabse bada sawal ye hota hai ki har stratum se kitna bada sample ($n_i$) liya jaye? Ise **Allocation** kehte hain. Ek achha allocation wo hota hai jismein humein kam se kam kharch mein zyada se zyada accuracy mile. Allocation 4 tarike se hota hai:
1. **Equal Allocation:** Sabhi strata se barabar sample le lo ($n_i = n/k$). Ye tab karte hain jab humein aur koi information nahi hoti aur administration ko simple rakhna hota hai.
2. **Proportional Allocation:** Jiska stratum size ($N_i$) jitna bada, wahan se utna zyada sample lo ($n_i \propto N_i$). Ye sabse zyada use hota hai.
3. **Neyman Allocation:** Isme cost sab jagah same maani jati hai. Hum wahan se zyada sample lete hain jahan population size badi ho aur wahan variance ($S_i$) bhi zyada ho ($n_i \propto N_i S_i$).
4. **Optimum Allocation:** Ye sabse detail method hai. Isme hum cost aur variance dono dekhte hain. Lagrange Multipliers ka use karke hum derive karte hain ki $n_i \propto \frac{N_i S_i}{\sqrt{c_i}}$. Iska matlab, wahan se bada sample lo jahan:
   - Stratum bada ho.
   - Variability (utha-patak) zyada ho.
   - Survey karne ka kharcha ($c_i$) kam ho.

## 3.8 RELATIVE PRECISION OF STRATIFIED RANDOM SAMPLING WITH SIMPLE RANDOM SAMPLING

**English Content:**
In this section, we compare the precision of the usual estimators under simple random sampling (without stratification) and stratified random sampling employing proportional and optimum allocations. The variances are denoted by $V(\bar{y}_n)_{SRS}$, $V(\bar{y}_{st})_{prop}$, and $V(\bar{y}_{st})_{opt}$ respectively.

**Theorem 3.8.1:** If finite population correction (f.p.c.) is ignored, show that:
$$ V(\bar{y}_{st})_{opt} \le V(\bar{y}_{st})_{prop} \le V(\bar{y}_n)_{SRS} $$

**Proof:**
We know the formulas for these variances:
$$ V(\bar{y}_{st})_{prop} = \sum_{i=1}^k \frac{W_i S_i^2}{n} - \sum_{i=1}^k \frac{W_i S_i^2}{N} $$
$$ V(\bar{y}_{st})_{opt} = \frac{(\sum W_i S_i)^2}{n} - \sum_{i=1}^k \frac{W_i S_i^2}{N} $$
$$ V(\bar{y}_n)_{SRS} = \frac{S^2}{n} - \frac{S^2}{N} $$

Ignoring the f.p.c. (the $1/N$ terms), we get:
$$ V_{prop} = \frac{1}{n} \sum W_i S_i^2 $$
$$ V_{opt} = \frac{1}{n} (\sum W_i S_i)^2 $$
$$ V_{SRS} = \frac{1}{n} S^2 $$

Now, let's compare $V_{prop}$ and $V_{opt}$:
$$ V_{prop} - V_{opt} = \frac{1}{n} \left[ \sum W_i S_i^2 - (\sum W_i S_i)^2 \right] $$
Let $\bar{S} = \sum W_i S_i$ (the weighted mean of stratum standard deviations).
$$ V_{prop} - V_{opt} = \frac{1}{n} \sum W_i (S_i - \bar{S})^2 $$
Since a square term is always positive or zero, this is a positive quantity. So, $V_{opt} \le V_{prop}$.

Next, let's compare $V_{SRS}$ and $V_{prop}$. We know the relation between overall variance and stratum variance:
$$ (N-1) S^2 = \sum \sum (y_{ij} - \bar{Y})^2 = \sum_{i=1}^k \sum_{j=1}^{N_i} ((y_{ij} - \bar{Y}_i) + (\bar{Y}_i - \bar{Y}))^2 $$
$$ (N-1) S^2 = \sum_{i=1}^k (N_i - 1) S_i^2 + \sum_{i=1}^k N_i (\bar{Y}_i - \bar{Y})^2 $$
Dividing by $N$ (assuming $N-1 \approx N$ and $N_i-1 \approx N_i$ for large populations):
$$ S^2 \approx \sum W_i S_i^2 + \sum W_i (\bar{Y}_i - \bar{Y})^2 $$
Substituting this into $V_{SRS}$:
$$ V_{SRS} = \frac{1}{n} \left[ \sum W_i S_i^2 + \sum W_i (\bar{Y}_i - \bar{Y})^2 \right] $$
$$ V_{SRS} = V_{prop} + \frac{1}{n} \sum W_i (\bar{Y}_i - \bar{Y})^2 $$
Since the second term is positive, $V_{prop} \le V_{SRS}$.

Combining these two results, we have:
$$ V_{opt} \le V_{prop} \le V_{SRS} $$

**Conclusion:** The larger the difference between the stratum means ($\bar{Y}_i$) and the overall mean ($\bar{Y}$), the greater the gain in precision with proportional allocation over simple random sampling. Furthermore, Neyman's optimum allocation gives better results than proportional allocation.

**Example 3.1:** 
2000 cultivators' holdings in Uttar Pradesh (India) were stratified according to their sizes.
The number of holdings ($N_i$), mean area under wheat per holding ($\bar{Y}_i$) and s.d. of area under wheat per holding ($S_i$) are given for 7 strata.
For a sample of 200 farms, we need to compute the sample size in each stratum under proportional and optimum allocations and compare the sampling variance.

*Calculations Summary:*
$N = 2000$, $n = 200$.
- Proportional Allocation: $n_i = n (N_i/N) = 200 (N_i/2000) = 0.1 N_i$. Sample sizes obtained are 40, 46, 38, 33, 17, 11, and 15 respectively. The variance $V(\bar{y}_{st})_{prop}$ is calculated by ignoring fpc.
- Optimum Allocation: $n_i = n \frac{N_i S_i}{\sum N_i S_i}$. Sample sizes obtained are 19, 36, 34, 39, 24, 17, and 31. The variance $V(\bar{y}_{st})_{opt}$ is calculated by ignoring fpc.
- Simple Random Sampling: $V(\bar{y}_{n})_{SRS}$ is also calculated.
The relative precision shows that Optimum allocation is much more efficient than Proportional, which is in turn more efficient than SRS.

---

**Hinglish Content:**
Is section mein hum dekhte hain ki SRS (jismein koi stratification nahi hota), Proportional Allocation, aur Optimum Allocation mein sabse achha (precise) kaun hai. Hum inke variances $V(\bar{y}_n)_{SRS}$, $V(\bar{y}_{st})_{prop}$, aur $V(\bar{y}_{st})_{opt}$ ko compare karte hain.

**Theorem 3.8.1:** Agar hum finite population correction (f.p.c.) ko ignore karein, toh prove karo ki:
$$ V(\bar{y}_{st})_{opt} \le V(\bar{y}_{st})_{prop} \le V(\bar{y}_n)_{SRS} $$

**Proof:**
Hum teeno ke formulas likhte hain bina f.p.c. ke. 
Pehle $V_{prop}$ aur $V_{opt}$ ko subtract karte hain. Humein $\frac{1}{n} \sum W_i (S_i - \bar{S})^2$ milta hai, jo ki ek square term hone ki wajah se positive hota hai. Iska matlab Optimum allocation hamesha Proportional se behtar ya barabar hoga ($V_{opt} \le V_{prop}$).

Fir hum total variance $S^2$ ka relation strata variance $S_i^2$ aur strata means ke difference $(\bar{Y}_i - \bar{Y})^2$ mein split karte hain (jise Analysis of Variance ya ANOVA jaisa samajh sakte hain). Isse pata chalta hai ki $V_{SRS}$ actually $V_{prop}$ aur strata ke beech ke means ke difference ka sum hai. Isliye $V_{prop} \le V_{SRS}$.
Dono results ko mila kar prove ho jata hai ki: $V_{opt} \le V_{prop} \le V_{SRS}$.

**Nishkarsh (Conclusion):** Jitna zyada alag-alag strata ke means honge, proportional allocation utna hi achha perform karega SRS ke comparison mein. Aur Optimum allocation sabse behtar precision deta hai.
Example 3.1 mein UP ke 2000 kisaano ka data diya gaya hai jisse ye mathematically prove kiya gaya ki Optimum allocation ka variance sabse kam aata hai.

## 3.9 ESTIMATION OF GAIN IN PRECISION DUE TO STRATIFICATION

**English Content:**
In comparing the precision, we assumed the population values ($S_i^2$, $\bar{Y}_i$) were known. But what if we only have a stratified sample and want to estimate the gain in precision due to stratification?
An unbiased estimator of $V(\bar{y}_{st})$ is $v(\bar{y}_{st}) = \sum W_i^2 \left(\frac{1}{n_i} - \frac{1}{N_i}\right) s_i^2$.
To compare, we need an unbiased estimate of $V(\bar{y}_{n})_{SRS}$ based on the stratified sample.
An unbiased estimator of $V_{SRS}$ based on a stratified sample is given by:
$$ \widehat{V}(\bar{y}_{n})_{SRS} = \frac{N-n}{nN} \left[ \sum_{i=1}^k W_i s_i^2 + \sum_{i=1}^k W_i (\bar{y}_i - \bar{y}_{st})^2 - \sum_{i=1}^k W_i (1-W_i) \frac{s_i^2}{n_i} \right] $$

The estimate of the relative gain in precision due to stratification is obtained by:
$$ \text{Relative Gain} = \frac{\widehat{V}(\bar{y}_n)_{SRS} - \widehat{V}(\bar{y}_{st})}{\widehat{V}(\bar{y}_{st})} $$
If the sample allocation is large enough in each stratum ($n_i \ge 50$), the last term in the bracket is small and the relation reduces to a simpler form.

**Example 3.3:** The number of pepper standards for selected villages in three strata of Trivandrum zone was recorded. By calculating $\widehat{V}(\hat{Y}_{st})$ and $\widehat{V}(\hat{Y}_{SRS})$ using the above formula, the percentage gain in precision due to stratification was calculated.

---

**Hinglish Content:**
Abhi tak humne maan liya tha ki population ke $S_i^2$ aur $\bar{Y}_i$ humein pata hain. Lekin survey ke baad agar humein check karna ho ki stratification se kitna fayda (gain) hua, toh kaise karenge?
Stratified variance ka estimate toh humein pata hai $v(\bar{y}_{st})$. Par agar humne strata na banaye hote aur SRS kiya hota, toh uska variance kya aata, uska estimate humein usi stratified sample se nikalna padta hai.
Iska ek complex formula hota hai jo upar diya gaya hai.
Relative gain nikalne ke liye hum dono variance estimates ka difference nikal kar usko stratified variance estimate se divide kar dete hain. 
Example 3.3 mein Trivandrum ke pepper standards ke survey data se calculate karke dikhaya gaya hai ki kaise strata banane se precision percentage mein gain aata hai.

## 3.10 FORMATION OF STRATA

**English Content:**
How do we demarcate the boundaries of strata if the study variable is continuous? The goal is to choose demarcation points $y_1, y_2, ..., y_{k-1}$ to minimize $V(\bar{y}_{st})$. 
Dalenius showed that with proportional allocation, the optimal points are given by:
$$ y_h = \frac{\bar{Y}_h + \bar{Y}_{h+1}}{2} $$
This means the boundary should be the average of the means of the two strata it separates.
However, since applying this is computationally heavy, approximate rules are used:
1. **Equalization of $W_h S_h$:** Dalenius and Gurney (1951) suggested making strata such that $W_h S_h$ is equal for all strata.
2. **Equalization of strata totals:** Mahalanobis (1952) suggested making strata with equal aggregate sizes $N_h \bar{Y}_h$.
3. **Equalization of $N_h \times \text{range}$:** Ekman (1959) suggested forming strata where the product of the number of units and the range of the variate is equal.
4. **Equalization of cumulatives of $\sqrt{f(y)}$:** Dalenius and Hodges (1959) suggested equalizing the cumulative of the square root of the frequency function.

---

**Hinglish Content:**
Agar hamara data continuous hai (jaise income ya age), toh hum strata ki boundaries kahan banayein? Hamara maqsad hai ki $V(\bar{y}_{st})$ minimize ho.
Dalenius ne prove kiya tha ki boundary points $y_h$ un do strata ke means ka average hona chahiye jinko wo separate kar raha hai. 
Lekin practical life mein ise calculate karna bahut mushkil hai. Isliye kuch aasan niyam (rules) banaye gaye:
1. **$W_h S_h$ ko equal rakhna:** Dalenius aur Gurney ka method.
2. **Strata totals barabar karna:** Mahalanobis ka rule jismein hum har stratum ka total size equal rakhte hain.
3. **Ekman Rule:** Jismein $N_h$ aur stratum ki range ke product ko barabar rakha jata hai.
4. **$\sqrt{f(y)}$ ka rule:** Dalenius aur Hodges ka best method, jismein frequency ki square root ko cumulate karke barabar hisso mein baanta jata hai.

## 3.11 DETERMINATION OF NUMBER OF STRATA

**English Content:**
As we increase the number of strata $k$, the variance decreases. Dalenius conjectured that the variance of an estimator with $k$ strata compared to infinite strata is approximately:
$$ \frac{V(\bar{y}_k)}{V(\bar{y}_\infty)} = \frac{k^2}{k^2 - 1} $$
However, increasing the number of strata beyond a certain point is not profitable because the survey cost increases. 
The cost function is $C = C_0 + k C_1 + n C_2$ where $C_1$ is cost per stratum and $C_2$ is cost per unit. The optimum number of strata balances the reduction in variance with the increase in cost. Sethi (1963) suggested that an increase in $k$ beyond 6 would seldom be profitable.

---

**Hinglish Content:**
Kitne strata banane chahiye? Jab hum strata ki sankhya $k$ badhate hain, toh variance kam hota hai. Par iska matlab ye nahi ki hum 100 strata bana dein.
Strata badhane se survey ka kharcha bhi badhta hai. Cost ka formula hai $C = C_0 + k C_1 + n C_2$, jismein $C_1$ naye stratum banane ka kharcha hai.
Optimum strata ki sankhya wo hai jahan variance kam hone ka fayda, kharch badhne ke nuksan ko balance kare. Sethi ki research ke anusaar, 6 se zyada strata banana shayad hi kabhi faydemand hota hai.

## 3.12 METHOD OF COLLAPSED STRATA

**English Content:**
Sometimes the population is so heterogeneous that to achieve better representation, stratification is carried to the point that only $n_i = 1$ (one unit) is selected from each stratum. In such cases, the variance $s_i^2$ cannot be estimated because $n_i - 1 = 0$.
To estimate the variance, strata are grouped in pairs whose means do not differ much. This is called the **technique of collapsed strata**.
By grouping pairs, we get a combined variance estimate. However, this quantity will overestimate the true variance $V(\bar{y}_{st})$. The overestimation is small if the paired strata are similar in size and characteristics.

---

**Hinglish Content:**
Kabhi-kabhi population itni alag-alag (heterogeneous) hoti hai ki humein itne strata banane padte hain ki har stratum se hum sirf 1 hi unit ($n_i = 1$) select kar paate hain. Aise case mein hum variance $s_i^2$ nahi nikal sakte kyuki formula mein $n_i - 1 = 0$ ho jayega.
Variance estimate karne ke liye, hum un strata ke jode (pairs) bana dete hain jo ek dusre se milte-julte hain. Ise **Collapsed Strata** method kehte hain. 
Is jode (pair) se jo variance nikalta hai, wo asli variance se thoda zyada (overestimate) hota hai. Lekin agar humne achhe se pair banaye hain toh ye difference bahut kam hota hai.

## 3.13 POST-STRATIFICATION (STRATIFICATION AFTER SELECTION OF SAMPLE)

**English Content:**
Sometimes, we don't have the frame to stratify before sampling (e.g., we don't have lists of voters by age, but we know their ages after surveying them). We draw a simple random sample, and then classify the selected units into strata. This is called **post-stratification**.
The weighted mean $\bar{y}_{pw} = \sum W_i \bar{y}_i$ is used.
Stephan (1945) showed that for large $n$, the variance is:
$$ V(\bar{y}_{pw}) \approx \frac{1}{n} \sum W_i S_i^2 + \frac{1}{n^2} \sum (1 - W_i) S_i^2 $$
The first term is the variance with proportional allocation, and the second term is a small adjustment due to post-stratification. Hence, for large samples, post-stratification is almost as precise as proportional stratified sampling.

---

**Hinglish Content:**
Kabhi-kabhi survey se pehle hamare paas strata banane ki jankari nahi hoti (jaise, humein nahi pata kaun kis age group ka hai jab tak hum pooch na lein). Aise mein hum ek simple random sample le lete hain, aur fir sample ke andar logo ko unke age-group (strata) mein baant dete hain. Ise **Post-Stratification** kehte hain.
Bade sample size $n$ ke liye, iska variance lagbhag Proportional Allocation wale variance ke barabar hi aata hai, thode se adjustment ke sath. Iska matlab hai ki agar pehle stratification na ho paye, toh baad mein karne se bhi proportional allocation jaisa hi fayda mil jata hai.

## 3.14 DEEP STRATIFICATION

**English Content:**
If there are two alternative criteria of stratification, we can opt for two-way stratification which yields $k_1$ rows and $k_2$ columns, making $k_1 \times k_2$ strata.
If we want to estimate the variance, the minimum sample size must be $2 \times k_1 \times k_2$. A problem arises when the available sample size $n$ is less than the number of strata, yet we want proportional allocation for each criterion.
Bryant, Hartley and Jessen (1960) provided a method called deep stratification or controlled selection. By arranging cells and selecting them such that no two cells belong to the same row or column, original selection probabilities are preserved while maintaining multi-way stratification.

---

**Hinglish Content:**
Agar hamare paas stratification ke 2 criteria hain (jaise Age aur Income dono), toh hum dono ka use karke 2-way stratification kar sakte hain. Isse $k_1 \times k_2$ number of strata banenge.
Variance nikalne ke liye humein kam se kam har cell mein 2 observations chahiye. Par problem tab aati hai jab hamara total sample size $n$, total strata se bhi kam ho.
Iska solution Bryant, Hartley aur Jessen ne diya tha jise **Deep Stratification** ya Controlled Selection kehte hain. Isme hum mathematically cells ko is tarah select karte hain ki dono criteria ka proportional representation bhi ho jaye, aur sample size bhi kam lage.
