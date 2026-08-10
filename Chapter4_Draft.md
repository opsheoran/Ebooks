# 4. SYSTEMATIC RANDOM SAMPLING

## 4.1 INTRODUCTION
**English Content:**
In the previous chapters, we discussed sampling techniques where sampling units were selected randomly at every step. Now, we shall discuss a technique that has the wonderful feature of selecting the entire sample with just one single random start. This procedure, where only the first unit is selected with the help of random numbers and the remaining units get selected automatically following a pre-designed pattern, is called **systematic random sampling** (or simply systematic sampling).

Suppose the $N$ units of the population are numbered from $1$ to $N$ in a specific order. Let us assume $N = nk$, where $n$ is the desired sample size and $k$ is an integer. If we select a random number less than or equal to $k$ and then select every $k$-th unit thereafter, the resulting sample is called an "every $k$-th systematic sample." This procedure is termed **linear systematic sampling**. However, if $N$ is not equal to $nk$, we can include every $k$-th unit in a circular manner until the whole list is exhausted, which is called **circular systematic sampling**.

Systematic sampling is simple and foolproof. Besides its simplicity, it often provides estimates that are more efficient than simple random sampling and is widely used in various types of surveys. It has been thoroughly discussed by researchers like Madow and Madow (1944) and its practical applications have been demonstrated by Finney (1948) and Sukhatme et al. (1958). Additionally, Singh et al. (1968) suggested a modified procedure and illustrated its suitability by applying it to a survey for estimating milk yield.

**Hinglish Content:**
Pichle chapters mein humne un sampling techniques ko discuss kiya jahan sampling units har step par randomly select hoti thi. Ab hum ek aisi technique padhenge jisme ek bahut achha feature hai: pura sample sirf ek random start se select ho jata hai. Ek aisi sampling technique jisme sirf pehli unit random numbers ki madad se select ki jati hai, aur baaki ki units automatically ek pre-designed pattern ke according select ho jati hain, use **systematic random sampling** (ya short mein systematic sampling) kehte hain.

Maan lijiye population ki $N$ units ko $1$ se $N$ tak kisi order mein number kiya gaya hai. Maan lijiye $N = nk$, jahan $n$ sample size hai aur $k$ ek integer hai. Agar hum $k$ ya usse chhota ek random number select karein, aur uske baad har $k$-th unit ko select karte jayein, toh is resultant sample ko "every $k$-th systematic sample" kehte hain. Is procedure ko **linear systematic sampling** kaha jata hai. Agar $N \neq nk$ ho, aur har $k$-th unit ko circular manner mein list khatam hone tak include kiya jaye, toh isko **circular systematic sampling** kehte hain.

Systematic sampling simple aur foolproof hai. Apni simplicity ke alawa, yeh kai situations mein simple random sampling se zyada efficient estimates provide karti hai aur various surveys mein widely use hoti hai.

## 4.2 SAMPLE SELECTION PROCEDURES
**English Content:**
Systematic sampling is a commonly used technique whenever a complete and up-to-date sampling frame is available. Before we evaluate its advantages and disadvantages, we shall first discuss these sample selection procedures.

**Hinglish Content:**
Systematic sampling ek commonly use hone wali technique hai agar hamare paas ek complete aur up-to-date sampling frame available ho. Iske faayde aur nuksan (advantages aur disadvantages) evaluate karne se pehle, aaiye hum in sample selection procedures ko detail mein discuss karte hain.

### 4.2.1 Linear Systematic Sampling
**English Content:**
As mentioned earlier, a common procedure is the linear systematic sampling scheme. We suppose the population is linearly ordered in some way such that units can be numbered without ambiguity. Further, let $N$ be expressible in the form $N = nk$. Let the initially selected random number be $i$ (where $1 \le i \le k$). Here, $k$ is called the sampling interval. 

The selected sample comprises the units:
$$ i, i+k, i+2k, \dots, i+(n-1)k $$

This technique will generate $k$ systematic samples with equal probability. Below is the schematic diagram showing $k$ systematic samples in the population:

| Sample Number | 1 | 2 | ... | $i$ | ... | $k$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Units** | 1 | 2 | ... | $i$ | ... | $k$ |
| | $1+k$ | $2+k$ | ... | $i+k$ | ... | $2k$ |
| | $1+2k$ | $2+2k$ | ... | $i+2k$ | ... | $3k$ |
| | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
| | $1+(n-1)k$ | $2+(n-1)k$ | ... | $i+(n-1)k$ | ... | $nk$ |
| **Means** | $\bar{y}_{.1}$ | $\bar{y}_{.2}$ | ... | $\bar{y}_{.i}$ | ... | $\bar{y}_{.k}$ |

Another practical situation arises when $N$ is not expressible in the form $nk$. In this case, the present sampling scheme will give rise to samples of unequal size. $k$ is taken as the integer nearest to $N/n$. A random number is chosen from $1$ to $k$ and every $k$-th unit is drawn in the sample. Under this condition, the sample size is not necessarily $n$; in some cases, it may be $n-1$. For example, if $N=11, n=4$, then $k = 3$. The possible samples are: $\{1, 4, 7, 10\}$ (size 4), $\{2, 5, 8, 11\}$ (size 4), and $\{3, 6, 9\}$ (size 3), which are of unequal sizes. 

**Hinglish Content:**
Jaisa ki pehle bataya gaya, linear systematic sampling ek aam procedure hai. Hum yeh maante hain ki population ek linear order mein arrange hai taaki units ko bina kisi ambiguity ke number kiya ja sake. Maan lijiye $N$ ko $N = nk$ ke form mein express kiya ja sakta hai. Ek random number $i$ ($1 \le i \le k$) select kiya jata hai, jahan $k$ ko sampling interval kehte hain.

Sample mein yeh units aati hain:
$$ i, i+k, i+2k, \dots, i+(n-1)k $$

Yeh technique equal probability ke sath $k$ possible systematic samples generate karti hai, jise upar table mein dikhaya gaya hai.

Ek aur practical situation aati hai jab $N$, $nk$ ke form mein expressible nahi hota. Is case mein, $k$ ko $N/n$ ke nearest integer ke roop mein liya jata hai. $1$ se $k$ tak ek random number choose hota hai aur har $k$-th unit ko sample mein draw kiya jata hai. Is condition mein, sample size hamesha strictly $n$ nahi hota, kabhi kabhi yeh $n-1$ bhi ho sakta hai (jaise example mein size 4 aur 3 ke samples mile). Is unequal size ki problem ko overcome karne ke liye hum agla section discuss karenge.

### 4.2.2 Circular Systematic Sampling
**English Content:**
In linear systematic sampling, the main drawback is that the observed sample size can differ from the required sample size when $N \neq nk$. Hence, the sample mean is not unbiased for the population mean. To overcome the difficulty of varying sample sizes, D.B. Lahiri (1952) suggested **Circular Systematic Sampling**, which ensures a sample of constant size $n$ is always obtained.

**Steps for Circular Systematic Sampling:**
1. Let $k$ be an integer nearest to $N/n$.
2. Select a random start $i$ from $1$ to $N$ (instead of $1$ to $k$).
3. Select every $k$-th unit in a circular manner until a sample of size $n$ is obtained.

The selected sample units will correspond to the serial numbers:
- $i + j k$, if $i + j k \le N$
- $i + j k - N$, if $i + j k > N$
for $j = 0, 1, \dots, n-1$.

Every unit has got an equal probability of selection, which is $n/N$. 
**Example:** Let $N = 18$ and $n = 5$. Then $k \approx 18/5 = 3.6 \implies k = 4$.
The possible samples from different starts $i$ would be:
- If $i=1$: units are $\{1, 5, 9, 13, 17\}$
- If $i=2$: units are $\{2, 6, 10, 14, 18\}$
- If $i=3$: units are $\{3, 7, 11, 15, 1\}$
- If $i=4$: units are $\{4, 8, 12, 16, 2\}$
... and so on up to $i=18$.

**Theorem: In circular systematic sampling, the sample mean is an unbiased estimator of the Population mean.**
*Proof:*
Let the sample mean be $\bar{y}_{sys}$. 
$$ E(\bar{y}_{sys}) = \sum_{i=1}^{N} P_i \bar{y}_i $$
Since there are $N$ possible samples, each selected with probability $P_i = \frac{1}{N}$:
$$ E(\bar{y}_{sys}) = \frac{1}{N} \sum_{i=1}^{N} \left( \frac{1}{n} \sum_{j \in S_i} y_j \right) = \frac{1}{Nn} \sum_{i=1}^{N} \sum_{j \in S_i} y_j $$
Because each population unit exactly occurs $n$ times across all $N$ possible samples, the sum over all samples covers every population unit $n$ times:
$$ E(\bar{y}_{sys}) = \frac{1}{Nn} \left( n \sum_{j=1}^{N} y_j \right) = \frac{1}{N} \sum_{j=1}^{N} y_j = \bar{Y} $$
Hence, in circular systematic sampling, even if $N \neq nk$, we achieve a constant observed sample size $n$, and the sample mean remains an unbiased estimator of the population mean.

**Hinglish Content:**
Linear systematic sampling mein ek main drawback yeh tha ki jab $N \neq nk$ hota hai, toh observe kiya gaya sample size require kiye gaye size se alag ho sakta hai. Is problem ko overcome karne ke liye, D.B. Lahiri (1952) ne **Circular Systematic Sampling** propose ki jisse hamesha constant size $n$ ka sample milta hai.

**Steps:**
1. $k$ ko $N/n$ ke nearest integer pe round off karein.
2. $1$ se $N$ ke beech ek random start $i$ select karein (na ki $1$ se $k$ tak).
3. Har $k$-th unit ko circular order mein tab tak select karein jab tak $n$ units ka sample poora na ho jaye.

Units is tarah aayengi:
- Agar $i + j k \le N$ hai, toh $i + j k$
- Agar $i + j k > N$ hai, toh $i + j k - N$
(jahan $j = 0, 1, \dots, n-1$).

Har unit ke select hone ki probability equal hoti hai, jo ki $n/N$ hoti hai. Humne upar $N=18, n=5, k=4$ ka example dekha ki kaise circular manner mein values aati hain (jaise 15 ke baad $15+4=19$, par total 18 hi hain, toh wapas ghoom kar 1 par aa gaye). Is method mein har unit exactly $n$ samples mein aati hai, jiske wajah se mathematical proof ke according sample mean population mean ka bilkul unbiased estimator ban jata hai.

## 4.3 ADVANTAGES AND DISADVANTAGES
**English Content:**
The main advantage of systematic sampling is its simplicity of selection, operational convenience, and even spread of the sample over the entire population. Therefore, it has been found very useful in forest surveys for estimating the volume of timber, in fisheries for estimating the total catch of fish, in milk yield surveys for estimation of the lactation yield, etc. 
Another advantage is that, except for populations with periodicities, systematic sampling provides an efficient estimate compared to alternative designs. Sometimes systematic sampling variances are much smaller than the variances for random selection of units within strata.

In the case of periodicity in the population, systematic sampling has to be used with considerable care. If, for a periodic population, the sampling interval is an odd multiple of half the period of the cycle, systematic sampling provides zero variance. When the sampling interval is a simple multiple of the period of the cycle, systematic sampling is no better than selecting one unit at random. A serious disadvantage of systematic sampling lies in its use with populations having unforeseen periodicity which may substantially contribute bias to the estimate. Another disadvantage concerns the drawback of estimating the sampling variance of estimators with a single sample.

**Hinglish Content:**
Systematic sampling ka sabse bada faayda iska simple selection process, operational convenience, aur pure population par sample ka evenly spread hona hai. Isliye yeh forest surveys (timber volume nikalna), fisheries, aur milk yield surveys mein bahut useful mani jati hai. Periodic populations ko chhod kar, systematic sampling zyada efficient estimates deti hai. Kayi baar iska variance stratified random sampling se bhi chhota hota hai.

Lekin, agar population mein periodicity (ek regular wave jaisa pattern) ho, toh isko bahut dhyan se use karna padta hai. Agar sampling interval cycle ke period ka simple multiple ban jaye, toh systematic sampling kisi single random unit jitni hi bekaar ho jati hai. Sabse bada disadvantage ye hai ki unforeseen periodicity estimator mein bahut zyada bias la sakti hai. Ek aur nuksan yeh hai ki single sample ki madad se variance ka unbiased estimate nahi nikala ja sakta.

## 4.4 ESTIMATION OF MEAN AND ITS SAMPLING VARIANCE
**English Content:**
Let $y_{ij}$ denote the $j$-th member of the $i$-th systematic sample, where $i = 1, 2, \dots, k$ and $j = 1, 2, \dots, n$. The mean of the $i$-th sample is denoted by $\bar{y}_{.i}$. 
We consider the problem of estimating the population mean under the situation when $N = nk$.

**Theorem 4.4.1:** In systematic sampling with interval $k$, the sample mean $\bar{y}_{sys}$ is an unbiased estimator of the population mean $\bar{Y}$. Its sampling variance is given by:
$$ V(\bar{y}_{sys}) = \frac{k-1}{k} S_b^2 $$
where $S_b^2$ denotes the mean square between the column means in the population (where $i$ stands for column).

**Full Derivation:**
Since the probability of selection of the $i$-th systematic sample from the $k$ possible samples is $1/k$, we have:
$$ E(\bar{y}_{sys}) = \sum_{i=1}^{k} P_i \bar{y}_{.i} $$
Substitute $P_i = \frac{1}{k}$:
$$ E(\bar{y}_{sys}) = \frac{1}{k} \sum_{i=1}^{k} \bar{y}_{.i} = \frac{1}{k} \sum_{i=1}^{k} \left( \frac{1}{n} \sum_{j=1}^{n} y_{ij} \right) = \frac{1}{nk} \sum_{i=1}^{k} \sum_{j=1}^{n} y_{ij} $$
$$ E(\bar{y}_{sys}) = \frac{1}{N} \sum_{i=1}^{k} \sum_{j=1}^{n} y_{ij} = \bar{Y} $$
Hence, $\bar{y}_{sys}$ is an unbiased estimator.

If the $i$-th sample is considered the $i$-th column, the total sum of squares due to column means (between-sample variation) is defined as:
$$ (k-1) S_b^2 = \sum_{i=1}^{k} (\bar{y}_{.i} - \bar{Y})^2 $$
By definition, the variance of the sample mean $\bar{y}_{sys}$ is:
$$ V(\bar{y}_{sys}) = E(\bar{y}_{sys} - \bar{Y})^2 = \frac{1}{k} \sum_{i=1}^{k} (\bar{y}_{.i} - \bar{Y})^2 $$
Substituting the sum of squares:
$$ V(\bar{y}_{sys}) = \frac{1}{k} [ (k-1) S_b^2 ] = \frac{k-1}{k} S_b^2 $$
It should not be inferred from the above formula that the variance of the systematic sample mean will simply decrease if the sample size is increased. This makes it clear that systematic sampling is a delicate device and should be used carefully.

**Theorem 4.4.2:** The sampling variance of the sample mean $\bar{y}_{sys}$ is given by:
$$ V(\bar{y}_{sys}) = \frac{N-1}{N} S^2 - \frac{k(n-1)}{N} S_w^2 $$
where
$$ S_w^2 = \frac{1}{k(n-1)} \sum_{i=1}^{k} \sum_{j=1}^{n} (y_{ij} - \bar{y}_{.i})^2 $$
is the within-sample variance, and $S^2$ is the total population variance.

**Full Derivation:**
We know that the total sum of squares for the entire population is given by:
$$ (N-1)S^2 = \sum_{i=1}^{k} \sum_{j=1}^{n} (y_{ij} - \bar{Y})^2 $$
We can split this into within-sample and between-sample sum of squares:
$$ \sum_{i=1}^{k} \sum_{j=1}^{n} (y_{ij} - \bar{Y})^2 = \sum_{i=1}^{k} \sum_{j=1}^{n} [(y_{ij} - \bar{y}_{.i}) + (\bar{y}_{.i} - \bar{Y})]^2 $$
$$ (N-1)S^2 = \sum_{i=1}^{k} \sum_{j=1}^{n} (y_{ij} - \bar{y}_{.i})^2 + \sum_{i=1}^{k} \sum_{j=1}^{n} (\bar{y}_{.i} - \bar{Y})^2 + 2 \sum_{i=1}^{k} (\bar{y}_{.i} - \bar{Y}) \sum_{j=1}^{n} (y_{ij} - \bar{y}_{.i}) $$
The cross-product term is zero because the algebraic sum of deviations from the mean is zero ($\sum_{j=1}^{n} (y_{ij} - \bar{y}_{.i}) = 0$).
Hence,
$$ (N-1)S^2 = \sum_{i=1}^{k} \sum_{j=1}^{n} (y_{ij} - \bar{y}_{.i})^2 + n \sum_{i=1}^{k} (\bar{y}_{.i} - \bar{Y})^2 $$
By definition of $S_w^2$ and $V(\bar{y}_{sys})$:
$$ \sum_{i=1}^{k} \sum_{j=1}^{n} (y_{ij} - \bar{y}_{.i})^2 = k(n-1)S_w^2 $$
$$ n \sum_{i=1}^{k} (\bar{y}_{.i} - \bar{Y})^2 = n [ k \cdot V(\bar{y}_{sys}) ] = N \cdot V(\bar{y}_{sys}) $$
Substituting these, we get:
$$ (N-1)S^2 = k(n-1)S_w^2 + N V(\bar{y}_{sys}) $$
$$ N V(\bar{y}_{sys}) = (N-1)S^2 - k(n-1)S_w^2 $$
$$ V(\bar{y}_{sys}) = \frac{N-1}{N} S^2 - \frac{k(n-1)}{N} S_w^2 $$
Since $S^2$ is fixed for a given population, it is obvious from this result that in order to reduce $V(\bar{y}_{sys})$ (between-sample variance), it is necessary to increase $S_w^2$ (within-sample variation).

**Hinglish Content:**
Maan lijiye $i$-th systematic sample ki $j$-th value $y_{ij}$ hai.
**Theorem 4.4.1** mein mathematical proof ke sath yeh dikhaya gaya hai ki systematic sample mean $\bar{y}_{sys}$ population mean $\bar{Y}$ ka unbiased estimator hota hai. Kyunki har sample ki aane ki probability $1/k$ hoti hai, unka expected value seedha population mean ke barabar hota hai. Iska variance $V(\bar{y}_{sys}) = \frac{k-1}{k} S_b^2$ hota hai, jahan $S_b^2$ column means ke beech ka variance hai.

**Theorem 4.4.2** ek bahut important relationship derive karke batata hai. Total population variance ko hum within-sample (sample ke andar ka) aur between-sample (samples ke aapas ka) variance mein break kar sakte hain. Derivation se pata chalta hai ki $V(\bar{y}_{sys}) = \frac{N-1}{N} S^2 - \frac{k(n-1)}{N} S_w^2$. Is formula se clear hai ki agar hume estimator ka variance kam karna hai (taaki precision badhe), toh $S_w^2$ (within-sample variance) ko zyada hona chahiye. Iska matlab systematic sample ke andar ki units jitni zyada heterogeneous (alag-alag) hongi, hamara estimate utna hi achha hoga.

## 4.5 COMPARISON OF SYSTEMATIC WITH RANDOM SAMPLING
**English Content:**
The relative efficiency of systematic sampling in comparison with simple random sampling can be studied by considering the intra-class correlation coefficient, denoted by $\rho$, between the units of the same systematic sample.

**Theorem: In systematic sampling, show that $V(\bar{y}_{sys}) = \frac{N-1}{Nn} S^2 [1 + (n-1)\rho]$**
**Full Derivation:**
By definition, the variance of $\bar{y}_{sys}$ is:
$$ V(\bar{y}_{sys}) = E(\bar{y}_{sys} - \bar{Y})^2 = \frac{1}{k} \sum_{i=1}^{k} (\bar{y}_{.i} - \bar{Y})^2 $$
$$ V(\bar{y}_{sys}) = \frac{1}{k} \sum_{i=1}^{k} \left( \frac{1}{n} \sum_{j=1}^{n} y_{ij} - \bar{Y} \right)^2 $$
$$ V(\bar{y}_{sys}) = \frac{1}{k n^2} \sum_{i=1}^{k} \left( \sum_{j=1}^{n} (y_{ij} - \bar{Y}) \right)^2 $$
Expanding the square:
$$ V(\bar{y}_{sys}) = \frac{1}{k n^2} \left[ \sum_{i=1}^{k} \sum_{j=1}^{n} (y_{ij} - \bar{Y})^2 + \sum_{i=1}^{k} \sum_{j \neq j'}^{n} (y_{ij} - \bar{Y})(y_{ij'} - \bar{Y}) \right]  \quad --- (1) $$

We know the first part is the total population sum of squares: 
$$ \sum_{i=1}^{k} \sum_{j=1}^{n} (y_{ij} - \bar{Y})^2 = (N-1)S^2 = n k \left( \frac{N-1}{N} \right) S^2 $$
The intra-class correlation coefficient $\rho$ within $k$ samples of size $n$ is defined by the sum of cross products divided by the total variance terms:
$$ \rho = \frac{\sum_{i=1}^{k} \sum_{j \neq j'}^{n} (y_{ij} - \bar{Y})(y_{ij'} - \bar{Y})}{k n (n-1) \left( \frac{N-1}{N} \right) S^2} $$
From this, the sum of cross products is:
$$ \sum_{i=1}^{k} \sum_{j \neq j'}^{n} (y_{ij} - \bar{Y})(y_{ij'} - \bar{Y}) = \rho k n (n-1) \left( \frac{N-1}{N} \right) S^2 $$
Substituting these back into equation (1):
$$ V(\bar{y}_{sys}) = \frac{1}{k n^2} \left[ k n \left( \frac{N-1}{N} \right) S^2 + \rho k n (n-1) \left( \frac{N-1}{N} \right) S^2 \right] $$
$$ V(\bar{y}_{sys}) = \frac{k n}{k n^2} \left( \frac{N-1}{N} \right) S^2 [1 + (n-1)\rho] $$
$$ V(\bar{y}_{sys}) = \frac{N-1}{Nn} S^2 [1 + (n-1)\rho] $$

**Comparison with SRSWR:**
$$ V(\bar{y}_{srswr}) = \frac{\sigma^2}{n} = \frac{N-1}{Nn} S^2 $$
Relative efficiency with SRSWR:
$$ \frac{V(\bar{y}_{srswr})}{V(\bar{y}_{sys})} = \frac{1}{1 + (n-1)\rho} $$
Systematic sampling is more efficient than SRSWR if its relative efficiency $> 1$:
$$ \frac{1}{1 + (n-1)\rho} > 1 \implies 1 + (n-1)\rho < 1 \implies \rho < 0 $$

**Comparison with SRSWOR:**
$$ V(\bar{y}_{srswor}) = \frac{N-n}{Nn} S^2 $$
Systematic sampling would be more efficient than SRSWOR if $V(\bar{y}_{sys}) < V(\bar{y}_{srswor})$:
$$ \frac{N-1}{Nn} S^2 [1 + (n-1)\rho] < \frac{N-n}{Nn} S^2 $$
$$ (N-1) + (N-1)(n-1)\rho < N-n $$
$$ (N-1)(n-1)\rho < N - n - N + 1 \implies (N-1)(n-1)\rho < -(n-1) $$
$$ \rho < -\frac{1}{N-1} $$

**Range of $\rho$ in systematic sampling:**
Since variance cannot be negative, $V(\bar{y}_{sys}) \ge 0$:
$$ 1 + (n-1)\rho \ge 0 \implies \rho \ge -\frac{1}{n-1} $$
Since $\rho$ is a correlation coefficient, $\rho \le 1$.
Therefore, the range is $-\frac{1}{n-1} \le \rho \le 1$. The maximum value $\rho$ can attain is 1, and the minimum is $-\frac{1}{n-1}$ (in which case $V(\bar{y}_{sys}) = 0$).

**Hinglish Content:**
Systematic sampling ko Simple Random Sampling (SRS) ke sath compare karne ke liye hum **intra-class correlation coefficient** $\rho$ (rho) ka use karte hain. $\rho$ ek systematic sample ke andar ki units ke beech ka correlation hota hai.

Humne mathematical derivation se prove kiya ki $V(\bar{y}_{sys}) = \frac{N-1}{Nn} S^2 [1 + (n-1)\rho]$. 
Is relation se pata chalta hai ki agar $\rho$ positive hota hai, toh variance badh jata hai. Iska seedha matlab hai ki ek sample mein aane wali units apas mein alag (heterogeneous) honi chahiye, taaki unke beech correlation negative ho sake. 
Jab hum SRSWR (with replacement) se compare karte hain, toh systematic sampling tab better hoti hai jab $\rho < 0$ ho. 
Aur jab SRSWOR (without replacement) se compare karte hain, toh systematic sampling tab better hoti hai jab $\rho < -\frac{1}{N-1}$ ho.

Kyunki variance kabhi negative nahi ho sakta, isliye $\rho$ ki value hamesha $-\frac{1}{n-1}$ se lekar $1$ tak hi hoti hai. Jab $\rho$ minimum (yaani $-\frac{1}{n-1}$) hoti hai, tab variance bilkul $0$ ho jata hai aur humein highest possible precision milti hai.

## 4.6 COMPARISON OF SYSTEMATIC WITH STRATIFIED RANDOM SAMPLING
**English Content:**
Let us suppose that the population of $N$ units is divided into $n$ strata corresponding to $n$ rows of the schematic diagram in Table 4.2.1 and that one unit is drawn randomly from each stratum, thus giving a stratified sample of size $n$. 
The pooled mean square between units within a stratum is defined by:
$$ S_w^2 = \frac{1}{n(k-1)} \sum_{j=1}^{n} \sum_{i=1}^{k} (y_{ij} - \bar{y}_{j.})^2 $$
Clearly, the variance of the mean of this stratified sample will be:
$$ V(\bar{y}_{st}) = \frac{k-1}{nk} S_w^2 $$
Now we shall express the variance of the systematic sample in a suitable form for comparative study. Equation (4.4.1) can be written as:
$$ V(\bar{y}_{sys}) = \frac{k-1}{nk} S_w^2 [1 + (n-1)\rho_{wst}] $$
where $\rho_{wst}$ is a non-circular serial correlation coefficient.
Comparing the two, we get:
$$ V(\bar{y}_{sys}) = V(\bar{y}_{st}) [1 + (n-1)\rho_{wst}] $$
Thus, we see that the relative precision of systematic sampling over stratified random sampling depends upon the value of $\rho_{wst}$. If $\rho_{wst}$ is positive, then stratified random sampling will provide a better estimate. If $\rho_{wst} = 0$, both are equally good. If $\rho_{wst}$ is negative, systematic sampling is better.

### Example 4.1
**English Content:**
Given below are the daily milk yield (in litres) records of the first lactation of a specified cow belonging to the Tharparkar herd maintained at the Government Cattle Farm, Patna. The milk yields of the first five days were not recorded, leaving a 203 days record.
(Data table of 203 days is given in the source).
Total sum of values $\sum y = 1435.5$. Hence $\bar{Y} = 1435.5 / 203 = 7.071$.
$S^2 = 3.655$.

**Case (i): Systematic sampling with 7 days' interval ($k=7$).**
$n = 203/7 = 29$. Taking random start $i=5$, we get the 5th sample.
The unbiased estimate of the total milk yield is:
$$ \hat{Y}_{sys} = N \times \bar{y}_{sys} = 203 \times \left( \frac{200.7}{29} \right) = 1404.9 \text{ litres} $$
The variance of systematic sampling for the population total estimate is given as $809.11$.
The variance of simple random sample estimate (for $n=29$) is:
$$ V(\hat{Y}_{srs}) = \frac{N^2}{n} \left(1 - \frac{n}{N}\right) S^2 = 4426.68 $$
Thus, the relative precision of systematic sampling over simple random sampling will be:
$$ \frac{4426.68}{809.11} \times 100 = 547.1\% $$

**Case (ii): Systematic sampling with 14 days' interval ($k=14$).**
For $k=14$, $n$ is nearest integer to $203/14 \approx 14.5 \implies n=14$.
Taking a random start $i=10$, we get the 10th sample. The unbiased estimate of total milk yield is:
$$ \hat{Y}_{sys} = \frac{203}{14} \times 98.6 = 15 \times 98.6 = 1479.0 \text{ litres} $$
Its variance is $3991.60$.
The variance of a simple random sample estimate of size 14 will be $10014.70$.
Relative precision:
$$ \frac{10014.70}{3991.60} \times 100 = 250.9\% $$

**Hinglish Content:**
Maan lijiye ki population ko $n$ strata (rows) mein baant diya gaya aur har stratum se 1 unit randomly nikali gayi. Isse stratified sampling ka variance milta hai: $V(\bar{y}_{st}) = \frac{k-1}{nk} S_w^2$. 
Agar hum systematic variance ko ek serial correlation coefficient $\rho_{wst}$ ki form mein likhein, toh wo aata hai: $V(\bar{y}_{sys}) = V(\bar{y}_{st}) [1 + (n-1)\rho_{wst}]$.
Yahan par relative precision puri tarah $\rho_{wst}$ par depend karti hai. Agar $\rho_{wst} > 0$ hoga, toh stratified sampling behter hogi. Agar $\rho_{wst} < 0$ hoga, toh systematic sampling baazi maar legi.

**Example 4.1** mein ek gaaye ke $203$ din ke doodh (milk yield) ka data diya gaya hai. Jab hum $k=7$ (7 din ka interval) lete hain, toh systematic sampling ki precision simple random sampling ke mukable $547.1\%$ aati hai, matlab yeh 5 guna zyada efficient hai! Wahin jab hum $k=14$ lete hain, tab bhi yeh $250.9\%$ precise hai. Yeh example clearly proof karta hai ki practical cases mein systematic sampling kafi powerful hoti hai.

## 4.7 ESTIMATION OF VARIANCE
**English Content:**
An unbiased estimate of the variance is not available for a systematic sample with one random start because a systematic sample is regarded as a random sample of one unit (cluster).
Recall that:
$$ (N-1)S^2 = k(n-1)S_w^2 + N V(\bar{y}_{sys}) $$
Substituting this in the variance formula, we get:
$$ V(\bar{y}_{sys}) = \frac{N-1}{N} S^2 - \frac{k(n-1)}{N} S_w^2 $$
We can estimate $S^2$ and $S_w^2$ unbiasedly if we have multiple samples. However, from a single systematic sample, we cannot find an unbiased estimator of the variance because no two consecutive units can occur in the same sample.

If $m$ independent systematic samples are available, each of size $n$, an unbiased estimate of the variance of the estimated mean is given by:
$$ \hat{V}(\bar{y}_{sys}) = \frac{N-nm}{nm(m-1)N} \sum_{i=1}^{m} (\bar{y}_{.i} - \bar{y}_{.})^2 $$
where $\bar{y}_{.}$ is the overall mean.

For a single systematic sample, some biased approximate estimators based on the differences between successive observations are:
$$ v_1 = \frac{N-n}{Nn} \frac{\sum_{i=1}^{n-1} (y_{i+1} - y_i)^2}{2(n-1)} $$
$$ v_2 = \frac{N-n}{Nn} \frac{\sum_{i=1}^{n-2} (y_{i+2} - 2y_{i+1} + y_i)^2}{6(n-2)} $$
These estimators are biased and should be used with caution, otherwise they may provide misleading results in practice.

### Example 4.2
**English Content:**
In an experimental agricultural census out of 225 holdings in two villages, 45 holdings were selected by systematic sampling (with $k=5$). The total arable land for the 45 holdings is $\sum y = 1968$.
An estimate of the total arable land is given by:
$$ \hat{Y} = k \sum_{i=1}^{n} y_i = 5 \times 1968 = 9840 \text{ kacha bigha} $$
An approximate estimate of the variance of $\hat{Y}$ is given by using the successive differences:
$$ \hat{V}(\hat{Y}) = \frac{N^2 (N-n)}{Nn} \frac{\sum (y_{i+1} - y_i)^2}{2(n-1)} = 45500 $$
Estimated standard error of $\hat{Y} = \sqrt{45500} = 213.3$ kacha bigha.

**Hinglish Content:**
Systematic sampling ki ek sabse badi problem yeh hai ki agar sirf ek hi sample liya gaya hai, toh hum uske variance ka unbiased estimate nahi nikal sakte. Formula ke derivation se pata chalta hai ki humein total variance $S^2$ aur within-sample variance $S_w^2$ dono chahiye hote hain. Par kyunki ek systematic sample mein lagatar 2 units ek sath aati hi nahi hain, isliye variance accurately estimate nahi kiya ja sakta.

Agar hum $m$ independent systematic samples le lein, tabhi ek exact unbiased variance nikal sakta hai. Lekin agar ek hi sample ho, toh Cochran aur Yates ne successive observations (ek ke baad ek aane wali) ke differences use karke kuch approximate (par biased) estimators ($v_1$ aur $v_2$) diye hain. Inhe sambhal kar use karna chahiye.

**Example 4.2** mein 225 holdings mein se $k=5$ ke interval par 45 holdings ka data liya gaya, total 1968 bigha zameen nikli. Poori population ki zameen ka estimate $1968 \times 5 = 9840$ bigha aaya. Uska error successive differences wala formula laga ke approximate kiya gaya jo $213.3$ bigha ka Standard Error aaya.

## 4.8 INTERPENETRATING SYSTEMATIC SAMPLING
**English Content:**
If it is essential to have a rigorous estimate of the sampling variance, it can be done by taking $m$ systematic sub-samples with independent random starts, each containing $n/m$ units to keep the total sample size the same. Let $\bar{y}_i$ be estimates based on $m$ independent systematic sub-samples. An unbiased estimator of the population mean is the pooled mean:
$$ \bar{y}_{.} = \frac{1}{m} \sum_{i=1}^{m} \bar{y}_i $$
Then, an unbiased estimate of the variance of $\bar{y}_{.}$ is:
$$ \hat{V}(\bar{y}_{.}) = \frac{1}{m(m-1)} \sum_{i=1}^{m} (\bar{y}_i - \bar{y}_{.})^2 $$
Though these variance estimators are unbiased, they are less precise if $m$ is small. Similarly, if $m$ is increased by decreasing the sub-sample size, the combined estimator of the population mean is likely to be less efficient. Hence, one has to arrive at a decision between getting a good estimate of variance or a good estimate of the population mean.

**Hinglish Content:**
Agar variance ka bilkul sahi aur rigorous unbiased estimate chahiye hi chahiye, toh hum "Interpenetrating systematic sampling" use karte hain. Isme ek bada lamba sample lene ki jagah, chote-chote $m$ independent systematic samples alag-alag random start se liye jate hain. 
Un sabka average nikal ke pooled mean banta hai, aur un $m$ samples ke apne means ka variance nikal kar overall variance ka unbiased estimate asani se mil jata hai. Par isme ek dikkat hai, agar $m$ ko zyada bada kiya jaye, toh har sub-sample ka size chhota ho jata hai, jisse population mean ka estimate thoda kam efficient (less precise) ho sakta hai. Isliye mean aur variance dono ki precision ke beech ek balance rakhna padta hai.

## 4.9 NEW SYSTEMATIC SAMPLING
**English Content:**
As pointed out in previous sections, regular systematic sampling suffers from the drawback of not being able to provide an unbiased estimator of sampling variance on the basis of a single sample. One way was interpenetrating systematic sampling, but it results in loss in precision. Singh and Singh (1977) suggested a "New Systematic Sampling" procedure which provides an unbiased variance estimator from a single sample.

Suppose a population consists of $N$ units and a sample of size $n$ is to be drawn. Let $a$ and $k$ be two predetermined integers chosen such that every sample contains $n$ distinct units, and the inclusion probability for each pair of units is non-zero. Starting with a random number, we select $a$ units continuously, and thereafter the remaining $n-a$ units with an interval $k$.
The number of phases $N'$ required for selecting a sample is:
$$ N' = N - (n-a)k - a + 1 $$
The inclusion probabilities for individual units $\pi_i$ and pairwise units $\pi_{ij}$ are all known under this scheme. Hence, the Horvitz-Thompson estimator of the population mean simplifies to:
$$ \hat{\bar{Y}}_{HT} = \frac{1}{N} \sum_{i \in s} \frac{y_i}{\pi_i} $$
The sampling variance of this estimator in Yates-Grundy form reduces to:
$$ V(\hat{\bar{Y}}_{HT}) = \frac{1}{2N^2} \sum_{i \neq j}^{N} (\pi_i \pi_j - \pi_{ij}) \left( \frac{y_i}{\pi_i} - \frac{y_j}{\pi_j} \right)^2 $$
An unbiased estimator of this variance can be directly obtained from the single sample by:
$$ \hat{V}(\hat{\bar{Y}}_{HT}) = \frac{1}{2N^2} \sum_{i \neq j \in s} \frac{\pi_i \pi_j - \pi_{ij}}{\pi_{ij}} \left( \frac{y_i}{\pi_i} - \frac{y_j}{\pi_j} \right)^2 $$
In comparative studies, it was concluded that for many natural populations, new systematic sampling provides better results than the usual systematic sampling.

**Hinglish Content:**
Jaisa ki pehle bataya gaya, normal systematic sampling ka sabse bada drawback ye hai ki single sample se variance ka unbiased estimate nahi milta. Singh aur Singh (1977) ne ek "New Systematic Sampling" technique banayi taaki ek single sample se hi variance ka unbiased estimate nikala ja sake, wo bhi bina precision lose kiye. 
Is method mein, ek naye pattern mein sample select hota hai. Hum pehli kuch $a$ units continuously chunte hain aur baaki units $k$ ke interval par. Is tarike se har unit ke select hone ki probability ($\pi_i$) aur kisi bhi do units ke ek sath sample mein aane ki probability ($\pi_{ij}$) non-zero ho jati hain. Phir Horvitz-Thompson estimator ki madad se mean aur variance dono smoothly aur unbiased tareeke se estimate ho jate hain, aur iska result natural populations ke liye kafi better hota hai.

## 4.10 COMPARISON OF SYSTEMATIC WITH SIMPLE AND STRATIFIED RANDOM SAMPLES FOR SOME SPECIFIED POPULATIONS
**English Content:**
The performance of systematic sampling in relation to stratified or simple random sampling depends very much on the nature of the population in which the characteristic under study has some simple trend. 

### 4.10.1 Populations with Linear Trend
**English Content:**
Suppose the values of the population units increase in accordance with a linear model such that:
$$ y_i = a + i \cdot c $$
where $a$ and $c$ are constants and $i$ goes from 1 to $N$.
The Population Mean is:
$$ \bar{Y} = a + \frac{N+1}{2} c $$
The Population variance is:
$$ S^2 = \frac{1}{N-1} \sum_{i=1}^{N} (y_i - \bar{Y})^2 = c^2 \frac{N(N+1)}{12} $$

**Case I: When units are selected by SRSWOR:**
$$ V(\bar{y}_{srswor}) = \frac{N-n}{Nn} S^2 = \frac{N-n}{Nn} c^2 \frac{N(N+1)}{12} = \frac{c^2 (N-n)(N+1)}{12n} $$

**Case II: Systematic Sampling:**
The $j$-th unit of the $i$-th systematic sample is $y_{ij} = a + \{i + (j-1)k\}c$.
The mean of the $i$-th systematic sample is:
$$ \bar{y}_{.i} = a + i c + \frac{k(n-1)}{2} c $$
Subtracting the population mean $\bar{Y}$:
$$ \bar{y}_{.i} - \bar{Y} = c \left[ i - \frac{k+1}{2} \right] $$
The variance of the systematic sample is:
$$ V(\bar{y}_{sys}) = \frac{1}{k} \sum_{i=1}^{k} (\bar{y}_{.i} - \bar{Y})^2 = \frac{c^2}{k} \sum_{i=1}^{k} \left( i - \frac{k+1}{2} \right)^2 = c^2 \frac{k^2 - 1}{12} $$

**Case III: Stratified Sampling:**
Similarly, the variance within strata is found by replacing $N$ with $k$ and $n$ with 1:
$$ V(\bar{y}_{st}) = \frac{1}{n} \left( \frac{k^2 - 1}{12} c^2 \right) = \frac{c^2 (k^2 - 1)}{12n} $$

**Comparison:**
Comparing the variances:
$$ V(\bar{y}_{st}) = \frac{c^2(k^2-1)}{12n} \quad , \quad V(\bar{y}_{sys}) = \frac{c^2(k^2-1)}{12} \quad , \quad V(\bar{y}_{srswor}) = \frac{c^2(n-1)(nk+1)}{12n} $$
Therefore, $V(\bar{y}_{st}) = \frac{1}{n} V(\bar{y}_{sys})$.
For large $n$, they are in the ratio:
$$ V(\bar{y}_{st}) : V(\bar{y}_{sys}) : V(\bar{y}_{srswor}) \approx 1 : n : n^2 $$
It is seen that the variance of a stratified sample is only $1/n$-th of the variance of a systematic sample. Hence, stratified sampling is the most efficient of all methods for eliminating the effect of linear trend. 

**Hinglish Content:**
Agar population mein data ek seedhi line (linear trend) ki tarah badh raha ho (jaise $y_i = a + ic$), toh systematic aur baaki methods kaisa perform karenge?
Humne mathematical derivation se total variance $S^2$ nikala, phir teeno methods ke variance nikale.
Jab inko compare karte hain toh pata chalta hai ki $V(\bar{y}_{st}) = \frac{1}{n} V(\bar{y}_{sys})$. Yani ratio lagbhag $1 : n : n^2$ (Stratified : Systematic : SRSWOR) aati hai. 
Iska matlab linear trend wali population mein Stratified sampling sabse best (most efficient) hoti hai, Systematic sampling beech mein hoti hai (SRS se $n$ times better, par Stratified se $n$ times kharab). Is trend ke asar ko sudharne ke liye hum 'end corrections' ya modified systematic sampling use kar sakte hain jisme dono ends se equidistant pairs chune jate hain.

### 4.10.2 Populations with Periodic Variations
**English Content:**
Suppose the population consists of a periodic trend which is represented by a sine wave that repeats after every cycle.
**Case I:** When the sampling interval $k$ is equal to or a simple multiple of the period of cyclic variation. All the units in the sample will be drawn from the same position of each cycle, making them perfectly homogeneous. Hence, $S_w^2$ is very small, and the variance $V(\bar{y}_{sys})$ will be extremely large, making the estimate as bad as a single unit. Low precision.
**Case II:** When the sampling interval is not equal to, or is an odd multiple of half the period of cycles. Then the sample units will span the peaks and troughs of the wave, becoming highly heterogeneous. Thus, $S_w^2$ is large and $V(\bar{y}_{sys})$ is very small. In a very favorable case, precision could be maximized (even yielding zero variance). 

**Hinglish Content:**
Agar population mein ek periodic variation (jaise wave ka regular upar-neeche jana, machines ke cycles aadi) hai, toh systematic sampling ki efficiency is baat par nirbhar karegi ki interval $k$ kya hai.
Agar $k$ poore cycle ki length ke barabar hai, toh har sample mein ek hi jaise values ayenge (sabse chote ya sabse bade), matlab sample andar se bilkul homogeneous ho jayega, aur isse hamara estimate sabse kharab (low precision) aayega. 
Par agar $k$ half-cycle ka odd multiple (jaise cycle 20 ki hai, aur $k=10$ liya) hai, toh sample mein sabse choti aur sabse badi values dono ek sath ayengi. Sample bahut heterogeneous ho jayega, aur tab systematic sampling sabse highest precision degi.

### 4.10.3 Natural Populations
**English Content:**
Systematic sampling is both operationally convenient and efficient in sampling natural populations like forest areas for estimating the volume of timber, hardwood seedlings, etc. Osborne (1942), Yates (1948) and Finney (1948) have examined its relative efficiency in natural populations and observed its performance is comparatively much better.

**Hinglish Content:**
Natural populations jaise jungalon mein pedon (timber) ki volume ya plants ko estimate karne mein yeh method bahut aasan aur convenient hota hai. Purani studies ne saabit kiya hai ki aise naturally phaili hui populations mein systematic sampling SRS se kahin zyada better perform karti hai.

### 4.10.4 Auto-correlated Populations
**English Content:**
In various natural populations, units close to each other are more alike than units far apart. For the study of such populations, called auto-correlated populations, we assume that observations $y_i$ and $y_{i+u}$ are positively correlated, and their serial correlation coefficient $\rho_u$ depends on the distance $u$ between them, decreasing as $u$ increases. 
The graph of $\rho_u$ as a function of $u$ is called a correlogram. 
Madow and Madow (1944) have shown that if units are simply ordered, it is better to adopt systematic sampling instead of simple random sampling. Cochran (1946) has shown that if the second difference of the serial correlation coefficients is positive:
$$ \Delta^2 \rho_u = \rho_{u-1} - 2\rho_u + \rho_{u+1} \ge 0 $$
which implies the correlogram is concave upwards, then for such populations systematic sampling is even more efficient than stratified sampling:
$$ V(\bar{y}_{sys}) \le V(\bar{y}_{st}) \le V(\bar{y}_{srs}) $$

**Hinglish Content:**
Kayi natural situations mein, paas-paas ki units apas mein zyada milti julti hain. Inhe **auto-correlated populations** kehte hain. Yahan paas ki units mein correlation zyada hota hai, aur distance $u$ badhne par serial correlation $\rho_u$ kam hota jata hai. Iske graph ko correlogram kehte hain. 
Cochran ne mathematical terms mein prove kiya ki agar yeh correlation lagatar is tarah kam ho ki uski shape upward concave ho ($\Delta^2 \rho_u \ge 0$), toh systematic sampling sirf SRS se hi nahi, balki stratified sampling se bhi zyada achi (efficient) hoti hai!

## 4.11 TWO-DIMENSIONAL SYSTEMATIC SAMPLING
**English Content:**
So far we have discussed one-dimensional systematic sampling in which the population units are serially ordered on a line. There are many situations (like agriculture or forestry) where units are naturally arranged on an area or a plane. A systematic sampling procedure for such a situation is known as plane systematic or **two-dimensional systematic sampling**.
Let us assume the population area consists of $N = n \times k$ grid areas, arranged in an $n \times n$ form of cells, where each cell is $k \times k$ grids.
1. **Square Grid (Aligned sample):** The simplest way is to select a pair of random numbers $(i, j)$ such that $1 \le i \le k, 1 \le j \le k$. The random location is determined uniquely for all cells. The selected grids form an aligned or square-grid pattern.
2. **Unaligned sample:** Select $n$ independent random numbers $i_r \le k$ and $n$ independent random numbers $j_c \le k$. The grids included are $(r k + i_r, c k + j_c)$. This creates an unaligned pattern.
Investigations by Quenouille (1949) indicated that an unaligned pattern will be superior both to an aligned square grid and a stratified random sample. 

**Hinglish Content:**
Ab tak humne linear systematic sampling padhi jahan units ek line mein ordered the. Lekin kheti (agriculture) ya jungle (forestry) mein zameen ek area (2D plane) par hoti hai. Aisi jagah **two-dimensional systematic sampling** (plane systematic sampling) use hoti hai.
Agar area ko grid cells mein baanta jaye, toh do main tarike hain:
1. **Aligned Sample (Square grid):** Bas ek set random coordinates $(i, j)$ choose karo, aur pure area mein har cell ke usi jagah wale grids ko sample mein le lo. Yeh ek perfect aligned grid pattern banata hai.
2. **Unaligned Sample:** Har row aur har column ke liye alag random numbers choose karo, isse grid pattern unaligned ho jata hai.
Quenouille ki research ne dikhaya ki yeh unaligned pattern simple grid ya stratified sampling dono se zyada behtar aur accurate result deta hai.
