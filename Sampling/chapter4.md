**4. SYSTEMATIC RANDOM SAMPLING**

**4.1 INTRODUCTION**

In the previous chapters we have discussed those sampling techniques
where sampling units were selected randomly. Now we shall discuss a
sampling technique which has a nice feature of selecting the whole
sample with just one random start. A sampling technique in which only
the first unit is selected with the help of random numbers and the rest
get selected automatically according to some pre-designed pattern is
known as **systematic random sampling**. Systematic random sampling is
also referred to briefly as **systematic sampling**.

Suppose $N$ units of the population are numbered from 1 to $N$ in some
order. Let $N = nk$, where $n$ is the sample size and $k$ is an integer,
and a random number less than or equal to $k$ be selected and every
$k$th unit thereafter. The resultant sample is called **every** $k$**th
systematic sample** and such a procedure termed **linear systematic
sampling**. If $N \neq nk$, and every $k$th unit be included in a
circular manner till the whole list is exhausted, it will be called
**circular systematic sampling**.

Systematic sampling is simple and foolproof. Apart from its simplicity,
this procedure, in many situations, provides estimates more efficient
than simple random sampling and is widely used in various types of
surveys. Systematic sampling has been discussed at length by Madow and
Madow (1944), Madow (1949, 1953) and others. Its applications in
different fields has been demonstrated by Finney (1948) and Sukhatme et
al. (1958). Singh et al. (1968) have suggested a modified systematic
sampling procedure and its suitability has been illustrated by its
application to a survey for estimating milk yield.

**4.2 SAMPLE SELECTION PROCEDURES**

Systematic sampling is a commonly used technique if a complete and
up-to-date sampling frame is made available. We shall first discuss
these sample selection procedures before we evaluate their advantages
and disadvantages.

**4.2.1 Linear Systematic Sampling**

As mentioned above, a common procedure is the linear systematic sampling
scheme. We suppose that the population is linearly ordered in some way
such that units can be referred to by number, without ambiguity.
Further, let $N$ be expressible in the form $N = nk$ and let the
selected random number be $i$ ($\leq k$), $k$ being called the
**sampling interval**. In this procedure, the sample comprises the
units, $i,i + k,i + 2k,\ldots,i + (n - 1)k$. The technique will generate
$k$ systematic samples with equal probability which may be shown in the
schematic diagram given below:

**Table 4.2.1** Schematic diagram showing $k$ systematic samples in the
population

  --------------------------------------------------------------------------------------------------------------------------------
  Sample Number 1                      2                      $$\ldots$$   $$i$$                  $$\ldots$$   $$k$$
  ------------- ---------------------- ---------------------- ------------ ---------------------- ------------ -------------------
                $$y_{1}$$              $$y_{2}$$              $$\ldots$$   $$y_{i}$$              $$\ldots$$   $$y_{k}$$

                $$y_{1 + k}$$          $$y_{2 + k}$$          $$\ldots$$   $$y_{i + k}$$          $$\ldots$$   $$y_{2k}$$

                $$y_{1 + 2k}$$         $$y_{2 + 2k}$$         $$\ldots$$   $$y_{i + 2k}$$         $$\ldots$$   $$y_{3k}$$

                $$\vdots$$             $$\vdots$$             $$\ldots$$   $$\vdots$$             $$\ldots$$   $$\vdots$$

                $$y_{1 + (j - 1)k}$$   $$y_{2 + (j - 1)k}$$   $$\ldots$$   $$y_{i + (j - 1)k}$$   $$\ldots$$   $$y_{jk}$$

                $$\vdots$$             $$\vdots$$             $$\ldots$$   $$\vdots$$             $$\ldots$$   $$\vdots$$

                $$y_{1 + (n - 1)k}$$   $$y_{2 + (n - 1)k}$$   $$\ldots$$   $$y_{i + (n - 1)k}$$   $$\ldots$$   $$y_{nk}$$

  **Mean**      $${\bar{y}}_{1}$$      $${\bar{y}}_{2}$$      $$\ldots$$   $${\bar{y}}_{i}$$      $$\ldots$$   $${\bar{y}}_{k}$$
  --------------------------------------------------------------------------------------------------------------------------------

Another practical situation is that $N$ is not expressible in the form
$N = nk$. In this case, the present sampling scheme will give rise to
samples of unequal size, $k$ is taken as an integer nearest to $N/n$.
Then a random number is chosen from 1 to $k$ and every $k$th unit is
drawn in the sample. Under this condition, the sample size is not
necessarily $n$ and in some cases it may be $(n - 1)$. For example, if
$N = 11$, $n = 4$, then the value of $k$ is 3 and possible samples are
$(1,4,7,10)$; $(2,5,8,11)$ and $(3,6,9)$, which are not of the same
size. We shall discuss an improvement over it in the next section.

**4.2.2 Circular Systematic Sampling**

To overcome the difficulty of varying sample size under the situation
$N \neq nk$, the procedure is modified slightly by which a sample of
constant size is always obtained. The procedure consists in selecting a
unit, by a random start, from 1 to $N$ and then thereafter selecting
every $k$th unit, $k$ being an integer nearest to $N/n$, in a circular
manner, until a sample of $n$ units is obtained. This technique is
generally known as **circular systematic sampling**. Suppose that a unit
with random number $i$ is selected. The sample will then consist of the
units corresponding to the serial numbers

$$\begin{matrix}
i + jk & \ \text{if~}i + jk \leq N \\
i + jk - N & \ \text{if~}i + jk > N
\end{matrix}$$

for $j = 0,1,\ldots,(n - 1)$.

It can be easily verified that every unit has got an equal probability
of selection $(1/N)$ in this method.

As an illustration, let $N = 11$, and $n = 4$. Then $k = 3$.

The possible samples are, therefore,

$(1,4,7,10)$; $(2,5,8,11)$; $(3,6,9,1)$; $(4,7,10,2)$; $(5,8,11,3)$;
$(6,9,1,4)$; $(7,10,2,5)$; $(8,11,3,6)$; $(9,1,4,7)$; $(10,2,5,8)$; and
$(11,3,6,9)$.

Further, it will be seen that systematic sampling has the drawback of
not yielding an unbiased estimate of sampling variance with single
sample. To overcome this difficulty, a new systematic sampling procedure
has been suggested by Singh and Singh (1977), which we shall explain in
Section 4.9 of this chapter.

**4.3 ADVANTAGES AND DISADVANTAGES**

The main advantage of systematic sampling is its simplicity of
selection, operational convenience and even spread of the sample over
the population. It has, therefore, been found very useful in forest
surveys for estimating the volume of timber, in fisheries for estimating
the total catch of fish, in milk yield surveys for estimation of the
lactation yield, etc. Another advantage is that, except for populations
with periodicities, systematic sampling provides an efficient estimate
as compared to alternative designs. Sometimes systematic sampling
variances are much smaller than the variances for random selection of
units within strata.

In case of periodicity in the population, systematic sampling has to be
used with considerable care. If, for periodic population, sampling
interval is an odd multiple of half the period of the cycle, systematic
sampling provides zero variance. When the sampling interval is a simple
multiple of the period of the cycle, systematic sampling is no better
than selecting one unit at random. A serious disadvantage of systematic
sampling lies in its use with populations having unforeseen periodicity
which may substantially contribute bias to the estimate of the
population mean value. Another disadvantage concerns the drawback of
estimating the sampling variance of estimators with single sample.

**4.4 ESTIMATION OF MEAN AND ITS SAMPLING VARIANCE**

Let $y_{ij}$ denote the $j$th member of the $i$th systematic sample,
($j = 1,2,\ldots n$; $i = 1,2,\ldots,k$). The mean of the $i$th sample
may be denoted by ${\bar{y}}_{i}$. We have to consider the problem of
estimating the population mean under two different situations: (i) when
$N = nk$ and (ii) when $N \neq nk$. First we shall discuss the situation
when $N = nk$.

**Theorem 4.4.1:** In systematic sampling with interval $k$, sample mean
${\bar{y}}_{sy}$ is an unbiased estimator of the population mean
$\bar{Y}$. Its sampling variance is given by

$$V({\bar{y}}_{sy}) = \frac{(k - 1)S_{c}^{2}}{k}\ (4.4.1)$$

where $S_{c}^{2}$ denotes the mean square between the column means in
the population ($c$ stands for column).

**Proof:** Since the probability of selection of the $i$th systematic
sample is $1/k$, we have

$$E({\bar{y}}_{sy}) = \sum_{i = 1}^{k}\mspace{2mu}\frac{{\bar{y}}_{i}}{k} = \frac{\sum_{i}^{}\mspace{2mu}\mspace{2mu}\sum_{j}^{}\mspace{2mu}\mspace{2mu} y_{ij}}{nk} = \bar{Y}$$

Hence, ${\bar{y}}_{sy}$ is an unbiased estimator.

If the $i$th sample is considered the $i$th column, the total sum of
squares due to column means is given by

$$\sum_{i = 1}^{k}\mspace{2mu}({\bar{y}}_{i} - \bar{Y})^{2} = (k - 1)S_{c}^{2}$$

Hence, the variance of the sample means ${\bar{y}}_{sy}$ is given by

$$V({\bar{y}}_{sy}) = \frac{E({\bar{y}}_{i} - \bar{Y})^{2}}{k} = \frac{(k - 1)S_{c}^{2}}{k}$$

It should not be inferred from the above formula that the variance of
systematic sample mean will decrease if the sample size is increased.
This makes the point clear that systematic sampling is a delicate device
and should be used carefully.

**Theorem 4.4.2:** The sampling variance of sample mean ${\bar{y}}_{sy}$
is given by

$$V({\bar{y}}_{sy}) = \frac{(N - 1)S^{2}}{N} - \frac{(n - 1)S_{w}^{2}}{n} = \sigma^{2} - \sigma_{w}^{2}\ (4.4.2)$$

where

$$S_{w}^{2} = \frac{\sum_{i}^{}\mspace{2mu}\mspace{2mu}\sum_{j}^{}\mspace{2mu}\mspace{2mu}(y_{ij} - {\bar{y}}_{i})^{2}}{k(n - 1)}$$

with $(n - 1)S_{w}^{2} = n\sigma_{w}^{2}$, and $\sigma^{2}$ has its
usual meaning.

**Proof:** We know that the total sum of squares is given by

$$TSS = (N - 1)S^{2} = \sum_{i}^{}\mspace{2mu}\sum_{j}^{}\mspace{2mu}(y_{ij} - {\bar{y}}_{i})^{2} + n\sum_{i}^{}\mspace{2mu}({\bar{y}}_{i} - \bar{Y})^{2}$$

Also, we know that the variance of ${\bar{y}}_{sy}$ is

$$V({\bar{y}}_{sy}) = \frac{\sum_{i}^{}\mspace{2mu}\mspace{2mu}({\bar{y}}_{i} - \bar{Y})^{2}}{k}$$

and

$$(N - 1)S^{2} = k(n - 1)S_{w}^{2} + nkV({\bar{y}}_{sy})$$

Hence,

$$V({\bar{y}}_{sy}) = \frac{(N - 1)S^{2}}{N} - \frac{(n - 1)S_{w}^{2}}{n} = \sigma^{2} - \sigma_{w}^{2}$$

Since $\sigma^{2}$ is fixed for a given population, it is obvious from
this result that in order to reduce $V({\bar{y}}_{sy})$ it is necessary
to increase the within-sample variation.

**4.5 COMPARISON OF SYSTEMATIC WITH RANDOM SAMPLING**

The relative efficiency of systematic sampling in comparison with simple
random sampling can be studied by considering the intra-class
correlation coefficient. It can be shown that

$$V({\bar{y}}_{sy}) = \frac{(nk - 1)S^{2} + \rho(nk - 1)(n - 1)S^{2}}{nk} = \frac{(nk - 1)S^{2}\lbrack 1 + (n - 1)\rho\rbrack}{nk}\ (4.5.1)$$

where $\rho$ is the intra-class correlation between the units of the
same systematic sample and is defined by

$$\rho = \frac{E(y_{ij} - \bar{Y})(y_{ij'} - \bar{Y})}{E(y_{ij} - \bar{Y})^{2}} = \frac{\sum_{i}^{}\mspace{2mu}\mspace{2mu}\sum_{j \neq j'}^{}\mspace{2mu}\mspace{2mu}(y_{ij} - \bar{Y})(y_{ij'} - \bar{Y})}{nk(n - 1)(nk - 1)S^{2}/nk}\ (4.5.2)$$

From relation (4.5.1) it can be seen that a positive correlation between
units in the same sample inflates the sampling variance of the estimate.
The increase is quite significant even for small positive correlation
because of the term $(n - 1)$. Since $S^{2}$ is fixed for a given
population, it is clear from the above relation that an arrangement with
the largest possible negative value of $\rho$ should be preferred. This
again leads to the same conclusion that the units within the same
systematic sample should be as heterogeneous as possible with respect to
the characteristic under study. Since $V_{sy}$ is never less than zero,
$\rho$ cannot be less than $- 1/(n - 1)$. Thus the minimum value of
$\rho$ is $- 1/(n - 1)$ and in this case $V_{sy} = 0$.

The relative precision of systematic sample mean with simple random mean
is given by

$$\frac{V_{sr}}{V_{sy}} = \frac{N - 1}{N - n}\lbrack 1 + \rho(n - 1)\rbrack\ (4.5.3)$$

It can be seen that the relative precision depends on the value of
$\rho$. For $\rho = - 1/(N - 1)$, the two methods give estimates of
equal precision; for $\rho < - 1/(N - 1)$, the estimate based on
systematic sample is more precise; while if $\rho > - 1/(N - 1)$, it
reverses. The maximum value which $\rho$ can attain is 1, when the
relative precision of systematic sampling is given by $(k - 1)/(N - 1)$.

**4.6 COMPARISON OF SYSTEMATIC WITH STRATIFIED RANDOM SAMPLING**

Let us suppose that the population of $N = nk$ units is divided into $n$
strata corresponding to $n$ rows of the schematic diagram in Table 4.1
and that one unit is drawn randomly from each stratum, thus giving a
stratified sample of size $n$. Then the mean of the $j$th stratum is

$${\bar{y}}_{\cdot j} = \frac{1}{k}\sum_{i = 1}^{k}\mspace{2mu} y_{ij},\ (j = 1,2,\ldots,n)\ (4.6.1)$$

and the population mean is

$$\bar{Y} = \frac{\sum_{i}^{}\mspace{2mu}\mspace{2mu}\sum_{j}^{}\mspace{2mu}\mspace{2mu} y_{ij}}{nk} = \frac{\sum_{j}^{}\mspace{2mu}\mspace{2mu}\sum_{i}^{}\mspace{2mu}\mspace{2mu} y_{ij}}{nk} = \frac{1}{n}\sum_{j}^{}\mspace{2mu}{\bar{y}}_{\cdot j}$$

Similarly, the stratum mean square of the units within the $j$th stratum
(row) is defined by

$$S_{\cdot j}^{2} = \frac{\sum_{i = 1}^{k}\mspace{2mu}\mspace{2mu}(y_{ij} - {\bar{y}}_{\cdot j})^{2}}{k - 1},\ (j = 1,2,\ldots,n)\ (4.6.2)$$

Hence, the pooled mean square between units within stratum is defined by

$$S_{wst}^{2} = \frac{\sum_{j}^{}\mspace{2mu}\mspace{2mu}\sum_{i}^{}\mspace{2mu}\mspace{2mu}(y_{ij} - {\bar{y}}_{\cdot j})^{2}}{n(k - 1)} = \frac{1}{n}\sum_{j}^{}\mspace{2mu} S_{\cdot j}^{2}\ (4.6.3)$$

Clearly, the variance of the mean of this stratified sample will be

$$V_{st}(\bar{y}) = \frac{(k - 1)S_{wst}^{2}}{nk} = (1 - f)\frac{S_{wst}^{2}}{n}\ (4.6.4)$$

Now we shall express the variance of the systematic sample in a suitable
form for a comparative study. Equation (4.4.1) can be written as

$$V({\bar{y}}_{sy}) = \frac{1}{n^{2}k}\sum_{i}^{}\mspace{2mu}\left\lbrack \sum_{j}^{}\mspace{2mu}\mspace{2mu} y_{ij} - \sum_{j}^{}\mspace{2mu}\mspace{2mu}{\bar{y}}_{\cdot j} \right\rbrack^{2} = \frac{1}{n^{2}k}\left\lbrack \sum_{i}^{}\mspace{2mu}\mspace{2mu}\sum_{j}^{}\mspace{2mu}\mspace{2mu}(y_{ij} - {\bar{y}}_{\cdot j})^{2} + \sum_{i}^{}\mspace{2mu}\mspace{2mu}\sum_{j \neq j'}^{}\mspace{2mu}\mspace{2mu}(y_{ij} - {\bar{y}}_{\cdot j})(y_{ij'} - {\bar{y}}_{\cdot j'}) \right\rbrack$$

$$= \frac{1}{n^{2}k}\left\lbrack n(k - 1)S_{wst}^{2} + n(n - 1)(k - 1)\rho_{wst}S_{wst}^{2} \right\rbrack$$

$$= \frac{(k - 1)S_{wst}^{2}\lbrack 1 + (n - 1)\rho_{wst}\rbrack}{nk}\ (4.6.5)$$

where $\rho_{wst}$ is a non-circular serial correlation coefficient
defined by

$$\rho_{wst} = \frac{E({\bar{y}}_{\cdot j} - \bar{Y})({\bar{y}}_{\cdot j'} - \bar{Y})}{E({\bar{y}}_{\cdot j} - \bar{Y})^{2}} = \frac{\sum_{j}^{}\mspace{2mu}\mspace{2mu}\sum_{j' \neq j}^{}\mspace{2mu}\mspace{2mu}\lbrack({\bar{y}}_{\cdot j} - \bar{Y})({\bar{y}}_{\cdot j'} - \bar{Y})\rbrack}{(n - 1)n(k - 1)S_{wst}^{2}}\ (4.6.6)$$

Comparing relations (4.6.4) and (4.6.5), we get

$$R.P. = \frac{V_{st}}{V_{sy}} = \lbrack 1 + (n - 1)\rho_{wst}\rbrack^{- 1}\ (4.6.7)$$

Thus we see that the relative precision of systematic sampling over
stratified random sampling depends upon the values of $\rho_{wst}$. If
$\rho_{wst}$ is positive then stratified random sampling will provide a
better estimate of $\bar{Y}$. However, if $\rho_{wst} = 0$, it may be
concluded that both systematic sampling and stratified random sampling
are equally good.

**Example 4.1:** Given below are the daily milk yield (in litres)
records of the first lactation of a specified cow belonging to the
Tharparkar herd maintained at the Government Cattle Farm, Patna. The
milk yields of the first five days were not recorded, being the
colostrum period.

**Table: Daily milk yield records (203 days)**

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

Find the efficiency of systematic sampling with 7 and 14 days\' interval
of recording, with respect to corresponding simple random sampling, in
estimating the lactation yield of the cow.

Hence
$\bar{Y} = \frac{1}{7}\sum_{i}^{}\mspace{2mu}{\bar{y}}_{i} = 3370$.

Taking random start $i = 5$, we get the 5th sample.

In this case, the unbiased estimate of the total milk yield is given by

$${\widehat{Y}}_{sy} = 7 \times 486 = 3402$$

The variance of systematic sampling for the population total estimate is
given by

$$V({\widehat{Y}}_{sy}) = \frac{N^{2}}{k}\sum_{i = 1}^{k}\mspace{2mu}({\bar{y}}_{i} - \bar{Y})^{2} = \frac{203^{2}}{7}\lbrack{16.45}^{2} + {17.07}^{2} + \ldots + {16.03}^{2}\rbrack - \frac{3370^{2}}{7} = 5192$$

The variance of simple random sample estimate of total milk yield is
given by

$$V({\widehat{Y}}_{sr}) = N^{2}(1 - f)\frac{S^{2}}{n}$$

where
$S^{2} = \frac{1}{N - 1}\sum_{i = 1}^{N}\mspace{2mu}(y_{i} - \bar{Y})^{2}$

$$V({\widehat{Y}}_{sr}) = (203)^{2}\left( 1 - \frac{7}{203} \right) \times \frac{3865.7228}{28} = 23194.33$$

Thus, the relative precision of systematic sampling over simple random
sampling will be

$$\frac{23194.33}{5192} \times 100 = 446.73\%$$

\(ii\) For $N = 203$ and $k = 14$, we have $n = 15$ or $14$.

Taking a random start $i = 10$, we get the 10th sample. In this case,
the unbiased estimate of total milk yield is given by

$${\widehat{Y}}_{sy} = 14 \times 246 = 3444$$

Its variance is given by

$$V({\widehat{Y}}_{sy}) = \frac{N^{2}}{k}\sum_{i = 1}^{k}\mspace{2mu}{\bar{y}}_{i}^{2} - {\bar{Y}}^{2} = 14 \times \frac{812028}{14} - (2270)^{2} = 11492$$

The variance of a simple random sample estimate of total milk yield will
be

$$V({\widehat{Y}}_{sr}) = N^{2}\left( \frac{1}{k} - \frac{1}{N} \right)S^{2} = (203)^{2}\left( \frac{1}{14} - \frac{1}{203} \right) \times \frac{3865.7228}{202} = 52187.2578$$

Therefore, the relative precision of systematic estimate over simple
random sample estimate is

$$\frac{52187.2578 \times 100}{11492} = 454.12\%$$

**4.7 ESTIMATION OF VARIANCE**

An unbiased estimate of the variance is not available for a systematic
sample with one random start because a systematic sample is regarded as
a random sample of one unit (cluster). However, some biased estimators
are possible on the basis of a systematic sample. If two or more
systematic samples are available, an unbiased estimate of the variance
of the estimated mean can be made.

Suppose $m$ independent systematic samples are available, each of size
$n$. Then, an unbiased estimate of the variance is given by

$$v({\bar{y}}_{sy}) = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu}({\bar{y}}_{i} - {\bar{y}}_{sy})^{2}}{m(m - 1)}\ (4.7.1)$$

where
${\bar{y}}_{sy} = \frac{1}{m}\sum_{i = 1}^{m}\mspace{2mu}{\bar{y}}_{i}$.

An approximate and biased estimate of the variance of a systematic
sample mean is given by

$$v({\bar{y}}_{sy}) = \frac{(1 - f)}{n} \times S_{wc}^{2}\ (4.7.2)$$

where
$S_{wc}^{2} = \frac{\sum_{i = 1}^{n - 1}\mspace{2mu}\mspace{2mu}(y_{i} - y_{i + 1})^{2}}{2(n - 1)}$.

Another approximate and biased estimate of variance of a systematic
sample mean is given by

$$v({\bar{y}}_{sy}) = \frac{(1 - f)}{N} \times \frac{\sum_{i = 1}^{n - 1}\mspace{2mu}\mspace{2mu}(y_{i} - y_{i + 1})^{2}}{2(n - 1)}\ (4.7.3)$$

These estimators, given by relations (4.7.2) and (4.7.3), are biased and
should be used with caution otherwise they may provide misleading
results in practice. It is, therefore, desirable to get an idea of the
bias in a specific case by comparing it with the sampling variance
obtained by using the entire data. These estimators are based on the
results given by Cochran (1946) and Yates (1948).

**Example 4.2:** In an experimental agricultural census carried out by
I.A.S.R.I., New Delhi, in the Loni block of Meerut District in U.P.
(India) during 1967-68, two villages of the block were selected
randomly. Out of 225 holdings in two villages, namely Panch-lok and
Agrola, 45 holdings were selected by systematic sampling (with 5 as the
sampling interval). The total arable land (in kacha bigha)\* for the 45
selected holdings are given below:

**Table 4.7.1: Total arable land for selected holdings**

  ------------------------------------------------------
  S.N.            1    2    3     4     5     6     7
  --------------- ---- ---- ----- ----- ----- ----- ----
  **Total arable  60   50   14    10    1     0     0
  land**                                            

  S.N.            8    9    10    11    12    13    14

  **Total arable  0    0    0     150   150   100   20
  land**                                            

  S.N.            15   16   17    18    19    20    21

  **Total arable  0    25   192   25    0     13    0
  land**                                            

  S.N.            22   23   24    25    26    27    28

  **Total arable  0    50   0     10    0     0     0
  land**                                            

  S.N.            29   30   31    32    33    34    35

  **Total arable  85   30   30    70    30    35    0
  land**                                            

  S.N.            36   37   38    39    40    41    42

  **Total arable  30   0    0     10    0     20    70
  land**                                            

  S.N.            43   44   45                      

  **Total arable  16   15   35                      
  land**                                            
  ------------------------------------------------------

\*(5 kacha bigha = 1 acre)

Estimate the total arable land in the two villages and also the
approximate standard error of the estimate.

An estimate of the total arable land is given by

$$\widehat{Y} = \frac{N}{n}\sum_{i = 1}^{n}\mspace{2mu} y_{i} = 225 \times \frac{1348}{45} = 6740$$

An estimate of the variance of $\widehat{Y}$ is given by

$$v(\widehat{Y}) = \frac{N^{2}(1 - f)}{n} \times \frac{\sum_{i = 1}^{n - 1}\mspace{2mu}\mspace{2mu}(y_{i} - y_{i + 1})^{2}}{2(n - 1)}$$

$$= \frac{225^{2} \times (5 - 1)}{45} \times \frac{116845}{2 \times (45 - 1)}$$

$$= 11,950,031.25$$

$\therefore$ Estimated standard error of
$\widehat{Y} = \sqrt{11,950,031.25} = 3456.88$.

**4.8 INTERPENETRATING SYSTEMATIC SAMPLING**

If it is essential to have a rigorous estimate of the sampling variance,
it can be done by taking systematic sub-samples with independent random
starts, each containing $n/m$ units to keep the total sample size the
same. Let ${\bar{y}}_{1},{\bar{y}}_{2},\ldots,{\bar{y}}_{m}$ be
estimates based on $m$ independent systematic sub-samples. An unbiased
estimator of the population mean is the pooled mean given by

$$\bar{y} = \frac{1}{m}\sum_{i = 1}^{m}\mspace{2mu}{\bar{y}}_{i}\ (4.8.1)$$

Then, an unbiased estimate of the variance of $\bar{y}$ is

$$v(\bar{y}) = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu}({\bar{y}}_{i} - \bar{y})^{2}}{m(m - 1)}\ (4.8.2)$$

In case of $m$ systematic sub-samples of $n/m( = n')$ units, each with
random starts from 1 to $mk( = k')$, the variance and estimated variance
of the pooled mean $\bar{y}$ are

$$V(\bar{y}) = \frac{(k' - m)}{k'm(k' - 1)}\sum_{i = 1}^{k'}\mspace{2mu}({\bar{y}}_{i} - \bar{Y})^{2}\ (4.8.3)$$

where ${\bar{y}}_{i}$ is the $i$th sample mean ($i = 1,\ldots,k'$) and

$$v(\bar{y}) = \frac{(k' - m)}{k'm(m - 1)}\sum_{i = 1}^{m}\mspace{2mu}({\bar{y}}_{i} - \bar{y})^{2}\ (4.8.4)$$

Though these variance estimators are unbiased, they are less precise if
$m$ is small. Similarly if $m$ is increased by decreasing the sub-sample
size, the combined estimator of the population mean is likely to be less
efficient. Hence, one has to arrive at a decision between the desire of
getting a good estimate of variance or a good estimate of the population
mean.

**4.9 NEW SYSTEMATIC SAMPLING\***

As pointed out in the previous section, systematic sampling suffers from
the drawback of not being able to provide an unbiased estimator of
sampling variance on the basis of a single sample. One possible way of
getting an unbiased variance estimator is to use interpenetrating
systematic sampling, but this results in loss in precision and
simplicity. Singh and Singh (1977) have suggested a new systematic
sampling procedure which provides an unbiased variance estimator. In
this section, we shall discuss briefly the outlines of the main results.

Suppose a population consists of $N$ distinct units and a sample of size
$n$ is to be drawn from it. Let $u$ ($\leq n$) and $d$ be two
predetermined integers which are chosen in such a way that (i) every
sample contains distinct units, and (ii) the inclusion probability for
each pair of units is non-zero. Starting with a random number
$r( \leq N)$, we select $u$ units continuously, and thereafter the
remaining $n - u( = v)$ units with interval $d$ such that $d \leq u$ and
$u + vd \leq N$. With these restrictions, a sample of desired sample
size $n$ can be drawn in two or more phases by this sampling scheme.
Here the term \'phase\' is used in the sense that the ultimate sample of
the given size is selected in stages. The number of phases $p$ required
for selecting a sample of $n$ units from a population of size $N$ is
given by

$$p \geq \frac{loglog(N/2) - loglog(n/2)}{log2}\ (4.9.1)$$

The sample space corresponding to the selection procedure contains $N$
possible samples, and the sample point corresponding to the random
number $r$ is given by $s_{r} = \{ s',s''\}$ where $s'$ consists of the
unit indices $r + m$ ($m = 0,1,\ldots,u - 1$) and $s''$ consists of the
unit indices $r + u - 1 + m'd$ ($m' = 1,2,\ldots,v$).

The probability of selecting each sample is $1/N$, and thus, the
probability measure associated with the selection procedure is given by

$$P = \{ P(s_{r}):P(s_{r}) = 1/N,r = 1,2,\ldots,N\}\ (4.9.2)$$

Thus, the inclusion probabilities for individual units and pairwise
units are given by $\pi_{i}$ and $\pi_{ij}$, which are known under the
new systematic sampling procedure. Hence, the Horvitz-Thompson estimator
of the population mean simplifies to

$${\bar{y}}_{nsy} = \frac{1}{n}\sum_{i \in s}^{}\mspace{2mu} y_{i} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu} y_{i}\ (4.9.3)$$

The sampling variance of the estimator ${\bar{y}}_{nsy}$ in Yates-Grundy
form reduces to

$$V({\bar{y}}_{nsy}) = \frac{1}{2}\sum_{i}^{}\mspace{2mu}\sum_{j}^{}\mspace{2mu}\frac{(\pi_{i}\pi_{j} - \pi_{ij})}{\pi_{ij}}\left( \frac{y_{i}}{\pi_{i}} - \frac{y_{j}}{\pi_{j}} \right)^{2}\ (4.9.4)$$

which can be written as

$$V({\bar{y}}_{nsy}) = \frac{N - n}{N}S^{2} - \frac{n - 1}{n}S_{wnsy}^{2}\ (4.9.5)$$

where
$S_{wnsy}^{2} = \frac{\sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{y})^{2}}{N(n - 1)}$.

An unbiased estimator of $V({\bar{y}}_{nsy})$ can be obtained by

$$v({\bar{y}}_{nsy}) = \frac{1}{2}\sum_{i \in s}^{}\mspace{2mu}\sum_{j \in s,j > i}^{}\mspace{2mu}\left( \frac{1}{\pi_{ij}} - \frac{1}{n^{2}} \right)(y_{i} - y_{j})^{2}\ (4.9.6)$$

In a comparative study, the efficiency of the new systematic sampling
over the usual systematic sampling and simple random sampling has been
examined by considering different types of populations. It was
concluded, in this study, that for many natural populations, new
systematic sampling provides better results than the usual systematic
sampling.

*\*May be omitted at the first reading.*

**4.10 COMPARISON OF SYSTEMATIC WITH SIMPLE AND STRATIFIED RANDOM
SAMPLES FOR SOME SPECIFIED POPULATIONS**

The performance of systematic sampling in relation to stratified or
simple random sampling depends very much on the nature of the population
in which the characteristic under study has some simple trend in terms
of units alone. Some main trends are discussed here as under.

**4.10.1 Populations with Linear Trend**

Suppose the values of the population units increase in accordance with a
linear model such that

$$y_{i} = a + bi$$

where $a$ and $b$ are constants and $i$ goes from 1 to $N$.

Hence

$$\bar{Y} = \frac{\sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}(a + bi)}{N} = a + \frac{b(N + 1)}{2}$$

and

$$S^{2} = \frac{\sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y})^{2}}{N - 1} = \frac{b^{2}\sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}\lbrack i - (N + 1)/2\rbrack^{2}}{N - 1} = \frac{b^{2}N(N + 1)}{12}$$

Therefore

$$V_{sr} = \frac{N - n}{Nn}S^{2} = \frac{(nk - 1)b^{2}}{12} \times \frac{k - 1}{nk} = \frac{(k - 1)(nk + 1)b^{2}}{12}\ (4.10.1)$$

Similarly, to find variance within strata, we have to put $k$ for $N$,
and we get

$$V_{st} = \frac{N - n}{Nn}S_{w}^{2} = \frac{nk - 1}{nk} \times \frac{(k - 1)k(k + 1)b^{2}}{12n} = \frac{(k - 1)(k + 1)b^{2}}{12n}\ (4.10.2)$$

For systematic sampling, the values can be put in Eqn. (4.3.2)

$$V_{sy} = \frac{1}{k}\sum_{i = 1}^{k}\mspace{2mu}({\bar{y}}_{i} - \bar{Y})^{2} = \frac{b^{2}}{k}\sum_{i = 1}^{k}\mspace{2mu}\left\lbrack i - \frac{k + 1}{2} \right\rbrack^{2} = \frac{b^{2}k(k + 1)(k - 1)}{12k} = \frac{(k - 1)(k + 1)b^{2}}{12}\ (4.10.3)$$

which proves

$$V_{st}:V_{sy}:V_{sr} = \left\lbrack \frac{k + 1}{n}:k + 1:nk + 1 \right\rbrack = \frac{1}{n}:1:n = 1:n:n^{2}\ (4.10.4)$$

It is seen that the variance of a stratified sample is only $1/n$th of
the variance of a systematic sample in a population with linear trend.
Similarly, the variance of a systematic sample is approximately $1/n$th
of the variance of a random sample. Hence, stratified sampling is the
most efficient of all the methods for eliminating the effect of linear
trend. The performance of systematic sampling in the presence of a
linear trend can be improved by applying the end corrections given by
Yates (1948) or the modified method of Singh et al (1968), which chooses
pairs of units equidistant from the ends of the population.

**4.10.2 Populations with Periodic Variations**

Suppose the population consists of a periodic trend which is represented
by

$$y_{i} = sin\left( \frac{\pi i}{n} \right) + \theta_{i}$$

where $i$ varies from 0 to an integral multiple of $2\pi$. Assuming
$2\pi = 20$, successive sampling units will repeat themselves after
every 20th value.

A five per cent systematic sample from such a population will consist of
sampling units drawn from the same position of each cycle. An estimate
from such a sample will be as good as a single value. On the other hand,
a five per cent random sample will contain units from different parts of
the population and estimates from such samples will be more precise for
the effect of a periodic trend. If we select 10 per cent systematic
sample, then the estimate will be as good as the population value, thus
making systematic sampling the most precise of all sampling methods.
Thus, the precision of systematic sampling from populations having a
periodic trend depends upon the periodicity. The most favourable case
occurs when $k$ is an odd multiple of the half period.

**4.10.3 Natural Populations**

Systematic sampling is both operationally convenient and efficient in
sampling some natural populations like forest areas for estimating the
volume of timber, hardwood seedlings, areas under different types of
covers, etc. Osborne (1942), Yates (1948) and Finney (1948, 1950) have
examined the relative efficiency of systematic sampling in certain
natural populations and observed that performance of systematic sampling
had been comparatively better.

**4.10.4 Auto-correlated Populations**

It has already been observed that the efficiency of systematic sampling
in comparison with simple random sampling or stratified sampling depends
upon the nature of the population. In various natural populations, units
close to each other are more alike than units far apart. For the study
of such populations, called auto-correlated populations, we assume that
the observations $y_{i}$ and $y_{j}$ ($i,j = 1,2,\ldots,N$) are
positively correlated and the serial correlation coefficient $\rho_{d}$
is a function of the distance in between, i.e. $d = |i - j|$. Suppose
the units $y_{i}$ are drawn from an infinite population (called super
population) with mean $\mu$ and variance $\sigma^{2}$, then

$$E(y_{i}) = \mu,\ E(y_{i} - \mu)^{2} = \sigma^{2}\ (4.10.5)$$

and

$$E(y_{i} - \mu)(y_{j} - \mu) = \rho_{d}\sigma^{2}$$

for $i = 1,2,\ldots,N$ and $d = 1,2,\ldots,(N - 1)$\
where

$$\rho_{d} \geq \rho_{d'} \geq 0\ \text{whenever~}d < d'$$

The graph of $\rho_{d}$ as a function of $d$ is called a correlogram. It
has been observed that $\rho_{d}$ increases as $d$ decreases. Madow and
Madow (1944) have shown that if the units in the population are ordered,
then it is enough to adopt systematic sampling instead of simple random
sampling. Cochran (1946) has shown that if, besides the assumptions
taken in Eqn. (4.10.5), it is assumed that

$$\delta_{d} = \rho_{d} + \rho_{d + 2} - 2\rho_{d + 1} \geq 0\ (4.10.6)$$

for all $d = 2,3,\ldots,(nk - 2)$,\
then

$$E(V_{sy}) \leq E(V_{st})\ (4.10.7)$$

The condition, $\delta_{d} \geq 0$, about the second difference of
serial correlation coefficients, implies that the correlogram is concave
upwards, and for such populations systematic sampling is more efficient
than stratified sampling.

Singh et al (1968) have discussed different cases, viz.

\(i\) population with linear trend plus random element,\
(ii) population with linear trend and periodic variation, and\
(iii) population with parabolic trend,\
and they have shown that the performance of modified systematic sampling
over stratified or simple random sampling is quite satisfactory.

**4.11 TWO-DIMENSIONAL SYSTEMATIC SAMPLING**

So far we have discussed one-dimensional systematic sampling in which
the population units are supposed to be serially ordered on a line.
There are many situations where the population units are naturally
arranged on an area or a plane instead of a line. A systematic sampling
procedure for such a situation is known as plane systematic or
two-dimensional systematic sampling. The simplest extension of a linear
systematic sample to the two-dimensional plane is popularly known as a
squared grid or aligned sample. Quenouille (1949) and Das (1950) have
discussed the problem of two-dimensional systematic sampling at length.
In this section, we describe briefly a procedure for selecting a
two-dimensional systematic sample.

Let us assume that the population consists of $N$ square (or
rectangular) grid areas of equal size and a sample of $n$ grid areas is
to be taken. Also assume that the grids are arranged in $l \times m$
($= nk = N$) form of cells and each cell is arranged in the form of $r$
rows and $s$ columns. The simplest way is to select a pair of random
numbers $(i,j)$ such that $i \leq r$, $j \leq s$. Thus, the random
location of a grid in the cell is determined uniquely. A systematic
sample selected by this procedure is an aligned or square-grid sample
and the selected grids are shown by the dots in Fig. 4.3 (a).

Another procedure is as follows: the grids are arranged in the form of
$r \cdot l$ rows and $m \cdot s$ columns and it is required to select a
systematic sample of size $n = rs$ grids.

Select $r$ independent random numbers $i_{1},i_{2},\ldots,i_{r}$, each
less than or equal to $l$; and $s$ independent random numbers
$j_{1},j_{2},\ldots,j_{s}$, each less than or equal to $m$. The grids
included in the sample are, $(i_{x} + xl,j_{y} + ym)$ for
$x = 0,1,\ldots,(r - 1)$ and $y = 0,1,\ldots,(s - 1)$.

A sample selected by this procedure is known as an unaligned sample and
the selected grid points are shown by the dots in Fig. 4.3(b).

Investigations given by Quenouille (1949) and Das (1950) indicated that
an unaligned pattern will be superior both to a square grid and a
stratified random sample. Milne (1959) has proposed a central square
grid technique in which the sample point lies at the centre of the
square. A two- and three-dimensional lattice sampling technique has been
discussed by Yates (1960).

**SET OF PROBLEMS**

**4.1** What is systematic sampling? Give the circumstances under which
it is to be preferred to simple random sampling. Explain how you will
estimate the variance of a systematic sample with a random start.

**4.2** Describe \'linear\' and \'circular\' systematic sampling
procedures and discuss briefly their advantages and disadvantages. In a
finite population of size $N$, show that systematic sampling will be
more efficient than random sampling with equal probability, wor, if the
intra-class correlation coefficient

$$\rho < - \frac{1}{N - 1}.$$

**4.3** Discuss the situations under which systematic samples are
preferred to other types of samples in censuses and surveys. Show that a
systematic sample mean is a more efficient estimator of the population
mean than a simple random mean, but less efficient than a stratified
random sample mean in a population with linear trend.

**4.4** Describe precisely the procedure of drawing a systematic sample
of $n$ units from a population of $N$ units, where $N$ is not
necessarily a multiple of $n$. (i) How would you estimate the mean of a
characteristic in the population and examine its unbiasedness? (ii) How
would you combine the estimates from three systematic samples of size
$n$ into a single pooled estimate which is unbiased and estimate its
standard error?

**4.5** In a two-dimensional population with $N^{2} = n^{2}k^{2}$ units,
the linear trend is given by $y_{ij} = i + j$ ($i,j = 1,2,\ldots,nk$),
where $y_{ij}$ is the item value in the $i$th row and $j$th column.

A systematic square grid sample of $n^{2}$ units is taken by taking two
independent random starts $(i,j)$ each between 0 and $k$ and
$(i_{x} + xk,j_{y} + yk)$ for $x,y = 0,1,\ldots,(n - 1)$. Show that the
mean of this sample has the same precision as the sample mean of size
$n^{2}$ (Cochran, 1977).

**REFERENCES**

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
