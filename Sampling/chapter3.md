**3. STRATIFIED RANDOM SAMPLING**

*\"Sir, In your otherwise beautiful poem (\"The Vision of Sin\") there
is a verse which reads \"Every moment dies a man, every moment one is
born.\" Obviously, this cannot be true and I suggest that in the next
edition you have it read \"Every moment dies a man, every moment*
$1\frac{1}{16}$ *is born.\" Even this value is slightly in error but
should be sufficiently accurate for poetry.\"* (in a letter to Lord
Tennyson) -- **Charles Babbage**

**3.1 INTRODUCTION**

Of all the methods of sampling, the procedure most commonly used in
surveys is stratified sampling. In stratified sampling, the population
of $N$ units is sub-divided into $k$ sub-populations called strata, the
$i$th sub-population having $N_{i}$ units ($i = 1,2,\ldots,k$). These
sub-populations are non-overlapping so that they comprise the whole
population such that

$$N_{1} + N_{2} + \cdots + N_{k} = N\ (3.1.1)$$

A sample is drawn from each stratum independently, the sample size
within the $i$th stratum being $n_{i}$ ($i = 1,2,\ldots,k$) such that

$$n_{1} + n_{2} + \cdots + n_{k} = n\ (3.1.2)$$

The procedure of taking samples in this way is known as stratified
sampling. If the sample is taken randomly from each stratum, the
procedure is known as stratified random sampling.

The main objective of stratification is to give a better cross-section
of the population so as to gain a higher degree of relative precision.
To achieve this, the following points are to be examined carefully:\
(i) Formation of strata\
(ii) Number of strata to be made\
(iii) Allocation of sample size within each stratum\
(iv) Analysis of data from a stratified design

We shall discuss the first two points after examining the last two
points relating to the theory of stratified sampling.

**3.2 PRINCIPLES OF STRATIFICATION**

The principles to be followed in stratifying a population are summarised
below:\
(i) The strata should be non-overlapping and should together comprise
the whole population.\
(ii) The stratification of population should be done in such a way that
strata are homogeneous within themselves, with respect to the
characteristic under study.\
(iii) In many practical situations when it is difficult to stratify with
respect to the characteristic under study, administrative convenience
may be considered as the basis for stratification.\
(iv) If the limit of precision for certain sub-populations is given, it
will be better to treat each sub-population as a stratum.

**3.3 ADVANTAGES OF STRATIFICATION**

Stratification serves many useful purposes. The principal ones are the
following:\
(i) Stratification may be desired for administrative convenience. The
agency conducting the survey work can establish its field offices in
various administrative zones with well-defined jurisdiction, thereby
leading to better organisation and supervision of field work.\
(ii) Stratification by natural characteristics helps in improving the
sampling design. For example, in area and yield surveys, there may be
different types of sampling problems in plains, deserts and hilly areas
which may need different approaches. Hence, it would be advantageous to
constitute a separate stratum for each of such areas.\
(iii) Stratification is particularly more effective when there are
extreme values in the population which can be segregated into separate
strata, thereby reducing the variability within strata. Separate
estimates obtained for individual stratum can be combined into a precise
estimate for the whole population.\
(iv) Stratification makes it possible to use different sampling designs
in different strata. In many practical situations, the information for
stratification is not uniformly available for all units in the
population. In these cases, the whole population is sub-divided into
strata according to the nature of the information available and some
suitable sampling scheme of selection of units within these strata is
adopted.\
(v) Stratification ensures adequate representation to various groups of
the population, which may be of some interest or importance.\
(vi) Stratification also ensures selection of a better cross-section of
the population than that under unstratified population.\
(vii) Stratification brings a gain in the precision in estimation of a
characteristic of a population. To achieve it, a heterogeneous
population is sub-divided into sub-populations, each of which is
homogeneous within itself. If each stratum is homogeneous such that
measurement, within it vary little from one unit to another, a more
precise estimate can be obtained by taking a relatively smaller sample.

**3.4 NOTATIONS**

Let $i$ denote for the stratum and $j$ for the sampling unit within the
stratum. The following symbols refer to stratum $i$:\
$N_{i} =$ total number of units\
$n_{i} =$ number of units in sample\
$W_{i} = N_{i}/N$ stratum weight\
$f_{i} = n_{i}/N_{i}$ sampling fraction in the stratum

Let $y_{ij}$ be the value of the $j$th unit in the stratum.\
${\bar{Y}}_{i} = \sum_{}^{}\ y_{ij}/N_{i}$ stratum mean\
${\bar{y}}_{i} = \sum_{}^{}\ y_{ij}/n_{i}$ sample mean\
$S_{i}^{2} = \sum_{}^{}\ (y_{ij} - {\bar{Y}}_{i})^{2}/(N_{i} - 1)$
stratum variance

**3.5 ESTIMATION OF THE POPULATION MEAN AND ITS VARIANCE**

Suppose that a population of $N$ units is divided into $k$ strata. The
population mean per unit can be written as

$$\bar{Y} = \frac{\sum_{}^{}\ \sum_{}^{}\ y_{ij}}{N} = \sum_{}^{}\ \frac{N_{i}{\bar{Y}}_{i}}{N} = \sum_{}^{}\ W_{i}{\bar{Y}}_{i}$$

An estimator ${\bar{y}}_{st}$ (st for stratified) for the population
mean $\bar{Y}$ can be written as

$${\bar{y}}_{st} = \sum_{}^{}\ \frac{N_{i}{\bar{y}}_{i}}{N}\ (3.5.1)$$

which is different from the overall sample mean

$$\bar{y} = \frac{\sum_{}^{}\ n_{i}{\bar{y}}_{i}}{n}\ (3.5.2)$$

**Theorem 3.5.1:** If in every stratum the sample estimator
${\bar{y}}_{i}$ is unbiased and samples are drawn independently in
different strata, then ${\bar{y}}_{st}$ is an unbiased estimator of the
population mean and its sampling variance is given by

$$V({\bar{y}}_{st}) = \sum_{}^{}\ \frac{N_{i}^{2}V({\bar{y}}_{i})}{N^{2}} = \sum_{}^{}\ W_{i}^{2}V({\bar{y}}_{i})\ (3.5.3)$$

**Proof:** We have that

$$E({\bar{y}}_{st}) = E\left( \sum_{}^{}\ \frac{N_{i}{\bar{y}}_{i}}{N} \right) = \sum_{}^{}\ \frac{N_{i}E({\bar{y}}_{i})}{N} = \sum_{}^{}\ \frac{N_{i}{\bar{Y}}_{i}}{N} = \bar{Y}\ (3.5.4)$$

This shows that ${\bar{y}}_{st}$ is an unbiased estimator.

To obtain the sampling variance, we note that sampling is done
independently in each stratum and, therefore,

$$V({\bar{y}}_{st}) = V\left( \sum_{}^{}\ \frac{N_{i}{\bar{y}}_{i}}{N} \right) = \sum_{}^{}\ \frac{N_{i}^{2}V({\bar{y}}_{i})}{N^{2}} = \sum_{}^{}\ W_{i}^{2}V({\bar{y}}_{i})\ (3.5.5)$$

**Theorem 3.5.2:** For stratified random sampling, wor, the sample
estimator ${\bar{y}}_{st}$ is unbiased and its sampling variance is
given by

$$V({\bar{y}}_{st}) = \sum_{}^{}\ \frac{N_{i}(N_{i} - n_{i})S_{i}^{2}}{N^{2}n_{i}} = \sum_{}^{}\ (1 - f_{i})\frac{W_{i}^{2}S_{i}^{2}}{n_{i}}\ (3.5.6)$$

**Proof:** Since, in each stratum, a simple random sample is taken,
${\bar{y}}_{i}$ is an unbiased estimator of ${\bar{Y}}_{i}$ and hence,
by Theorem 3.5.1, it can be shown that ${\bar{y}}_{st}$ is an unbiased
estimator of $\bar{Y}$.

Further, by Theorem 2.3.1 applied to an individual stratum, we have

$$V({\bar{y}}_{i}) = \frac{(N_{i} - n_{i})S_{i}^{2}}{N_{i}n_{i}}$$

Substituting the value in the result of Theorem 3.5.1, we get

$$V({\bar{y}}_{st}) = \sum_{}^{}\ \frac{N_{i}^{2}V({\bar{y}}_{i})}{N^{2}} = \sum_{}^{}\ \frac{N_{i}(N_{i} - n_{i})S_{i}^{2}}{N^{2}n_{i}} = \sum_{}^{}\ (1 - f_{i})\frac{W_{i}^{2}S_{i}^{2}}{n_{i}}$$

**Corollary 1:** If $Y_{st} = N{\bar{y}}_{st}$ is the estimator of the
population total $Y$, then $Y_{st}$ is an unbiased estimator and its
sampling variance is given by

$$V(Y_{st}) = \sum_{}^{}\ \frac{N_{i}(N_{i} - n_{i})S_{i}^{2}}{n_{i}} = \sum_{}^{}\ N_{i}^{2}(1 - f_{i})\frac{S_{i}^{2}}{n_{i}}\ (3.5.7)$$

**Corollary 2:** If in every stratum $(n_{i}/n) = (N_{i}/N)$, the
variance of ${\bar{y}}_{st}$ reduces to

$$V({\bar{y}}_{st}) = \frac{(N - n)}{nN^{2}}\sum_{}^{}\ N_{i}S_{i}^{2} = (1 - f)\frac{\sum_{}^{}\ W_{i}S_{i}^{2}}{n}\ (3.5.8)$$

**Corollary 3:** If in every stratum $n_{i}/n = N_{i}/N$, and the
variance in all strata has the same value $S_{w}^{2}$, the result
reduces to

$$V({\bar{y}}_{st}) = \frac{(N - n)S_{w}^{2}}{nN} = (1 - f)\frac{S_{w}^{2}}{n}\ (3.5.9)$$

**Corollary 4:** For stratified random sampling, wr, ${\bar{y}}_{st}$ is
an unbiased estimator and its sampling variance is given by

$$V({\bar{y}}_{st}) = \sum_{}^{}\ \frac{N_{i}^{2}S_{i}^{2}}{N^{2}n_{i}} = \sum_{}^{}\ \frac{W_{i}^{2}S_{i}^{2}}{n_{i}}\ (3.5.10)$$

**Theorem 3.5.3:** In stratified random sampling, wor, with sample size
$n_{i} = 1,2,\ldots,k$; $\sum_{}^{}\ n_{i} = n$ an unbiased estimator of
the population proportion $P$ is given by

$$P_{st} = \sum_{}^{}\ \frac{N_{i}p_{i}}{N} = \sum_{}^{}\ W_{i}p_{i}\ (3.5.11)$$

with its variance

$$V(P_{st}) = \sum_{}^{}\ (1 - f_{i})\frac{W_{i}^{2}N_{i}P_{i}(1 - P_{i})}{(N_{i} - 1)n_{i}}\ (3.5.12)$$

where $p_{i}$ is the sample estimate of proportion $P_{i}$ in the $i$th
stratum. The proof is obvious.

**Corollary 1:** $N_{i}/(N_{i} - 1)$ can be taken as unity, we have

$$V(P_{st}) = \sum_{}^{}\ (1 - f_{i})\frac{W_{i}^{2}P_{i}(1 - P_{i})}{n_{i}}\ (3.5.13)$$

**Corollary 2:** If stratified random sampling is with replacement, the
sampling variance is given by

$$V(P_{st}) = \sum_{}^{}\ \frac{W_{i}^{2}P_{i}(1 - P_{i})}{n_{i}}\ (3.5.14)$$

**Corollary 3:** If in every stratum $n_{i}/n = N_{i}/N$, the sampling
variance reduces to

$$V(P_{st}) = \frac{(1 - f)}{n}\sum_{}^{}\ \frac{N_{i}W_{i}^{2}P_{i}(1 - P_{i})}{N_{i} - 1}\ (3.5.15)$$

$$\approx (1 - f)\frac{\sum_{}^{}\ W_{i}P_{i}(1 - P_{i})}{n}\ (3.5.16)$$

The variance of $P$ depends on the product of $P_{i}$ and $(1 - P_{i})$
within strata. The product is small if $P_{i}$ is near zero or unity.
Thus, the efficiency can be increased if the strata are formed such that
units belonging to a given class are allocated in the same stratum.

**3.6 ESTIMATE OF VARIANCE**

If a simple random sample is taken within each stratum, an unbiased
estimator of $S_{i}^{2}$ is given by

$$s_{i}^{2} = \frac{\sum_{}^{}\ (y_{ij} - {\bar{y}}_{i})^{2}}{(n_{i} - 1)}\ (3.6.1)$$

Then, an unbiased estimator of sampling variance of ${\bar{y}}_{st}$ can
be obtained as follows:

**Theorem 3.6:** With stratified random sampling, wor, an unbiased
estimator of the variance of ${\bar{y}}_{st}$ is given by

$$v({\bar{y}}_{st}) = \sum_{}^{}\ \frac{N_{i}(N_{i} - n_{i})s_{i}^{2}}{N^{2}n_{i}} = \sum_{}^{}\ \frac{W_{i}^{2}s_{i}^{2}}{n_{i}} - \sum_{}^{}\ \frac{W_{i}s_{i}^{2}}{N}\ (3.6.2)$$

The proof is obvious.

**Corollary 1:** With stratified random sampling, wor, an unbiased
estimator of $V({\bar{y}}_{st})$ reduces to

$$v({\bar{y}}_{st}) = \sum_{}^{}\ \frac{W_{i}^{2}s_{i}^{2}}{n_{i}}\ (3.6.3)$$

**Corollary 2:** With stratified random sampling, wor, an unbiased
estimator of $V(P_{st})$ is given by

$$v(P_{st}) = \sum_{}^{}\ \frac{(1 - f_{i})W_{i}^{2}p_{i}(1 - p_{i})}{(n_{i} - 1)}\ (3.6.4)$$

**3.7 ALLOCATION OF SAMPLE SIZE IN DIFFERENT STRATA**

In stratified sampling, the allocation of the sample to different strata
is done by the consideration of three factors, viz.,\
(i) the total number of units in the stratum, i.e. stratum size\
(ii) the variability within the stratum, and\
(iii) the cost in taking observations per sampling unit in the stratum.

A good allocation is one where maximum precision is obtained with
minimum resources, or in other words, the criterion for allocation is to
minimize the budget for a given variance or minimize the variance for a
fixed budget, thus making the most effective use of the available
resources.

There are four methods of allocation of sample sizes to different strata
in a stratified sampling procedure. These are:\
(i) Equal allocation\
(ii) Proportional allocation\
(iii) Neyman allocation\
(iv) Optimum allocation

**3.7.1 Equal Samples From Each Stratum**

This is a situation of considerable practical interest for reasons of
administrative or field work convenience. In this method, the total
sample size $n$ is divided equally among all the strata, i.e. for the
$i$th stratum

$$n_{i} = n/k\ (3.7.1)$$

**3.7.2 Proportional Allocation**

This allocation, generally known as proportional allocation, was
originally proposed by Bowley (1926). This procedure of allocation is
very common in practice because of its simplicity. When no other
information except $N_{i}$, the total number of units in the $i$th
stratum, is available, the allocation of a given sample of size $n$ to
different strata is done in proportion to their sizes, i.e. in the $i$th
stratum,

$$n_{i} = nN_{i}/N\ (\text{or~}f_{i} = f)\ (3.7.2)$$

This means that the sampling fraction is the same in all strata. It
gives a self-weighting sample by which numerous estimates can be made
with greater speed and a higher degree of precision.

**3.7.3 Neyman Allocation**

This allocation of the total sample size to strata is called minimum
variance allocation and is due to Neyman (1934). This result appears to
have been first discovered by Tschuprow (1923) but remained unknown
until it was rediscovered independently by Neyman. The allocation of
samples among different strata is based on a joint consideration of the
stratum size and the stratum variation. In this allocation, it is
assumed that the sampling cost per unit among different strata is the
same and the size of the sample is fixed. Sample sizes are allocated by

$$n_{i} = n\frac{W_{i}S_{i}}{\sum_{}^{}\ W_{i}S_{i}} = n\frac{N_{i}S_{i}}{\sum_{}^{}\ N_{i}S_{i}}\ (3.7.3)$$

A formula for the minimum variance with fixed $n$ is obtained by
substituting the value of $n_{i}$ in Eqn. (3.5.6) when we get

$$V_{m}({\bar{y}}_{st}) = \frac{(\sum_{}^{}\ W_{i}S_{i})^{2}}{n} - \frac{\sum_{}^{}\ W_{i}S_{i}^{2}}{N}\ (3.7.4)$$

There may be difficulty in using this method as the value of $S_{i}$
will usually be unknown. However, the stratum variances may be obtained
from previous surveys or from a specially planned pilot survey. The
other alternative is to conduct the main survey in a phased manner and
utilize the data collected in the first phase for ensuring better
allocation in the second phase.

**3.7.4 Optimum Allocation**

In this method of allocation the sample sizes $n_{i}$ in the respective
strata are determined with a view to minimize $V({\bar{y}}_{st})$ for a
specified cost of conducting the sample survey or to minimize the cost
for a specified value of $V({\bar{y}}_{st})$. The simplest cost function
in stratified sampling that can be taken is

$$C = a + \sum_{}^{}\ n_{i}c_{i}\ (3.7.5)$$

where the overhead cost $a$ is constant and $c_{i}$ is the average cost
of surveying one unit in the $i$th stratum, which may depend upon the
nature and size of the units in the stratum.

To determine the optimum value of $n_{i}$, we consider the function

$$\Phi = V({\bar{y}}_{st}) + \lambda C\ (3.7.6)$$

where $\lambda$ is some unknown constant.

Using the calculus method of Lagrange multipliers, we select $n_{i}$ and
the constant $\lambda$ to minimize $\Phi$.

Differentiating with respect to $n_{i}$, we have

$$- \frac{W_{i}^{2}S_{i}^{2}}{n_{i}^{2}} + \lambda c_{i} = 0\ (i = 1,2,\ldots,k)$$

or

$$n_{i} = \frac{W_{i}S_{i}}{\sqrt{\lambda c_{i}}}\ (3.7.7)$$

Summing over all strata, we get

$$n = \sum_{}^{}\ \left( \frac{W_{i}S_{i}}{\sqrt{\lambda c_{i}}} \right)\ (3.7.8)$$

From relations (3.7.7) and (3.7.8) we can obtain

$$n_{i} = n\frac{W_{i}S_{i}/\sqrt{c_{i}}}{\sum_{}^{}\ (W_{i}S_{i}/\sqrt{c_{i}})} = n\frac{N_{i}S_{i}/\sqrt{c_{i}}}{\sum_{}^{}\ (N_{i}S_{i}/\sqrt{c_{i}})}\ (3.7.9)$$

Thus the relation (3.7.9) leads to the following important conclusions
that, in a given stratum, we have to take a larger sample if\
(i) the stratum size is larger;\
(ii) the stratum has larger variability; and\
(iii) the cost per unit is cheaper in the stratum.

If $c_{i}$\'s are the same from stratum to stratum, relation (3.7.9)
will lead to the Neyman allocation. Similarly, if $c_{i}$\'s and
$S_{i}$\'s do not vary from stratum to stratum, relation (3.7.9) will
lead to proportional allocation.

The total sample size $n$ required for estimating the population with a
specified cost $C$ is given by

$$n = \frac{(C - a)\sum_{}^{}\ (W_{i}S_{i}/\sqrt{c_{i}})}{\sum_{}^{}\ W_{i}S_{i}c_{i}}\ (3.7.10)$$

If $V$ is fixed, we find

$$n = \frac{\left( \sum_{}^{}\ W_{i}S_{i}/\sqrt{c_{i}} \right)\left( \sum_{}^{}\ W_{i}S_{i}c_{i} \right)}{V + \sum_{}^{}\ W_{i}S_{i}^{2}}\ (3.7.11)$$

The values of the stratum variances can be obtained from earlier surveys
or from a knowledge of the measurements within each stratum.

An alternative proof of the allocation results due to Stuart (1954) may
be summarized as follows:

Let $V'$ and $C'$ be the parts of $V$ and $C$ that depend on $n_{i}$ or
in a simple form, $V' = \sum_{}^{}\ A_{i}/n_{i}$ and
$C' = \sum_{}^{}\ c_{i}n_{i}$.

Minimizing $V$ for fixed $C$ or vice versa are both equivalent to
minimizing the product

$$V'C' = \left( \sum_{}^{}\ \frac{A_{i}}{n_{i}} \right)\left( \sum_{}^{}\ c_{i}n_{i} \right)\ (3.7.12)$$

Now, by Cauchy-Schwarz\'s inequality,

$$\left( \sum_{}^{}\ x_{i}^{2} \right)\left( \sum_{}^{}\ y_{i}^{2} \right) \geq \left( \sum_{}^{}\ x_{i}y_{i} \right)^{2}$$

we have

$$\left( \sum_{}^{}\ \frac{A_{i}}{n_{i}} \right)\left( \sum_{}^{}\ c_{i}n_{i} \right) \geq \left( \sum_{}^{}\ \sqrt{A_{i}c_{i}} \right)^{2}$$

The equality being if and only if $y_{i}$ is proportional to $x_{i}$,
i.e.

$$c_{i}n_{i} \propto \frac{\sqrt{A_{i}}}{n_{i}}$$

which yields

$$n_{i} \propto \sqrt{A_{i}/c_{i}}\ (3.7.13)$$

\(i\) In case $A_{i} = W_{i}^{2}S_{i}^{2}$, we get from relation
(3.7.13) the optimum sample sizes within strata as given in relation
(3.7.9).\
(ii) In case $c_{i} = c$ and $A_{i} = W_{i}^{2}S_{i}^{2}$, the optimum
sample sizes for Neyman allocation are given by the above relation.\
(iii) In case $A_{i} = W_{i}$ and $c_{i} = c$, proportional allocation
is also obtained by the above relation.

**3.8 RELATIVE PRECISION OF STRATIFIED RANDOM SAMPLING WITH SIMPLE
RANDOM SAMPLING**

In this section, we shall make a comparative study of the usual
estimators under simple random sampling, without stratification and
stratified random sampling employing various schemes of allocation, i.e.
proportional and optimum allocations. The variances of these estimators
of mean are denoted by $V_{SR}$, $V_{prop}$ and $V_{opt}$ respectively.

**Theorem 3.8.1:** If fpc is ignored, show that

$$V_{opt} \leq V_{prop} \leq V_{SR}\ (3.8.1)$$

**Proof:** When fpc is ignored, we have

$$V_{SR} = S^{2}/n$$

$$V_{prop} = \sum_{}^{}\ \frac{N_{i}S_{i}^{2}}{Nn} = \sum_{}^{}\ \frac{W_{i}S_{i}^{2}}{n}$$

$$V_{opt} = \frac{(\sum_{}^{}\ N_{i}S_{i})^{2}}{N^{2}n} - \frac{\sum_{}^{}\ N_{i}S_{i}^{2}}{N^{2}n}$$

Since terms $1/N_{i}$ and $1/N$ are negligible, we can have

$$NS^{2} = \sum_{}^{}\ N_{i}S_{i}^{2} + \sum_{}^{}\ N_{i}({\bar{Y}}_{i} - \bar{Y})^{2}$$

Hence, we have

$$V_{SR} = \frac{S^{2}}{n} = \frac{1}{nN}\left\lbrack \sum_{}^{}\ N_{i}S_{i}^{2} + \sum_{}^{}\ N_{i}({\bar{Y}}_{i} - \bar{Y})^{2} \right\rbrack$$

$$= V_{prop} + \frac{\sum_{}^{}\ N_{i}({\bar{Y}}_{i} - \bar{Y})^{2}}{nN}\ (3.8.2)$$

or $V_{SR} - V_{prop} =$ a positive quantity.

Thus, it proves that $V_{prop} \leq V_{SR}$.

Hence, it may be concluded that the larger the difference in the stratum
means, the greater is the gain in precision with proportional allocation
over simple random sampling.

Similarly

$$V_{prop} - V_{opt} = \frac{\sum_{}^{}\ N_{i}S_{i}^{2}}{Nn} - \frac{(\sum_{}^{}\ N_{i}S_{i})^{2}}{N^{2}n}$$

$$= \frac{1}{nN^{2}}\sum_{}^{}\ N_{i}(S_{i} - \bar{S})^{2}\ (3.8.3)$$

where $\bar{S} = \sum_{}^{}\ N_{i}S_{i}/N$.

Also

$$V_{SR} = V_{opt} + \frac{\sum_{}^{}\ N_{i}(S_{i} - \bar{S})^{2}}{nN} + \frac{\sum_{}^{}\ N_{i}({\bar{Y}}_{i} - \bar{Y})^{2}}{nN}\ (3.8.4)$$

which proves that $V_{opt} \leq V_{prop}$. Hence,
$V_{opt} \leq V_{prop} \leq V_{SR}$.

It concludes that Neyman\'s optimum allocation gives better results than
proportional allocation. We observe from Eqn. (3.8.4) that as we change
from simple random sampling to stratified random sampling with Neyman\'s
allocation, the gain in precision of the estimates results from two
factors, viz.\
(i) the differences between stratum means and\
(ii) the difference between the stratum standard deviations.

**Corollary:** If fpc cannot be neglected, show that
$V_{opt} \leq V_{prop} \leq V_{SR}$.

**Example 3.1:** 2000 cultivators\' holdings in Uttar Pradesh (India)
were stratified according to their sizes. The number of holdings
($N_{i}$), mean area under wheat per holding (${\bar{Y}}_{i}$) and s.d.
of area under wheat per holding ($S_{i}$) are given below for each
stratum:

  -------------------------------------------------------------------------
  Stratum     Number of       Mean area under wheat  s.d. of area under
  number      holdings        per-holding            wheat per-holding
              ($N_{i}$)       (${\bar{Y}}_{i}$)      ($S_{i}$)
  ----------- --------------- ---------------------- ----------------------
  1           394             5.4                    8.3

  2           461             16.3                   13.3

  3           381             24.3                   15.1

  4           334             34.5                   19.8

  5           169             42.1                   24.5

  6           113             50.1                   26.0

  7           148             63.8                   35.2
  -------------------------------------------------------------------------

For a sample of 200 farms, compute the sample size in each stratum under
proportional and optimum allocations. Calculate the sampling variance of
the estimated area under wheat from the sample (i) if the farms are
selected under proportional allocation by with and without replacement
methods, (ii) if the farms are selected under Neyman\'s allocation by
with and without replacement methods. Also compute the gain in
efficiency from these procedures as compared to simple random sampling.

The relevant calculations have been shown below in Table 3.1:

**Table 3.8.1:** Calculations of allocations, means and sampling
variances

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Stratum     $$N_{i}$$   $${\bar{Y}}_{i}$$   $$S_{i}$$   $$W_{i}$$    $$nW_{i}$$   $$W_{i}S_{i}$$   $n_{i}$   $$W_{i}{\bar{Y}}_{i}$$   $$W_{i}{\bar{Y}}_{i}^{2}$$   $$W_{i}S_{i}^{2}$$
                                                                                                     (Opt)                                                           
  ----------- ----------- ------------------- ----------- ------------ ------------ ---------------- --------- ------------------------ ---------------------------- --------------------
  1           394         5.4                 8.3         0.1970       40           1.64             19        1.06                     5.72                         13.612

  2           461         16.3                13.3        0.2305       46           3.07             36        3.76                     61.29                        40.831

  3           381         24.3                15.1        0.1905       38           2.88             34        4.63                     112.51                       43.488

  4           334         34.5                19.8        0.1670       33           3.31             39        5.76                     198.72                       65.538

  5           169         42.1                24.5        0.0845       17           2.07             24        3.56                     149.88                       50.715

  6           113         50.1                26.0        0.0565       11           1.47             17        2.83                     141.78                       38.220

  7           148         63.8                35.2        0.0740       15           2.61             31        4.72                     301.14                       91.872

  **Total**   **2000**                                    **1.0000**   **200**      **17.05**        **200**   **26.32**                **971.04**                   **344.276**
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Proportional Allocation:** $n_{i} = nN_{i}/N$ or $n_{i} = nW_{i}$\
The numbers of holdings to be selected from strata are given in column
(6) of the table and are 40, 46, 38, 33, 17, 11 and 15, respectively.

$$V({\bar{y}}_{prop})_{wor} = \frac{(N - n)}{nN}\sum_{}^{}\ W_{i}S_{i}^{2} = 1.5492$$

If fpc is ignored, we have

$$V({\bar{y}}_{prop})_{wr} = \frac{1}{n}\sum_{}^{}\ W_{i}S_{i}^{2} = 1.7214$$

**Optimum Allocation:** $n_{i} \propto N_{i}S_{i}$ or
$n_{i} = n\frac{W_{i}S_{i}}{\sum_{}^{}\ W_{i}S_{i}}$\
The numbers of holdings to be selected from strata are given in column
(8) of the table and are 19, 36, 34, 39, 24, 17 and 31, respectively.

$$V({\bar{y}}_{opt})_{wor} = \frac{(\sum_{}^{}\ W_{i}S_{i})^{2}}{n} - \frac{\sum_{}^{}\ W_{i}S_{i}^{2}}{N} = 1.2813$$

If fpc is ignored, we get

$$V({\bar{y}}_{opt})_{wr} = \frac{(\sum_{}^{}\ W_{i}S_{i})^{2}}{n} = 1.4535$$

**Simple Random Sampling:** The variance of the estimate of mean is
given by

$$V({\bar{y}}_{SR})_{wor} = \frac{(N - n)}{n(N - 1)}\left\lbrack \frac{1}{N}\sum_{}^{}\ N_{i}S_{i}^{2} + \sum_{}^{}\ \frac{N_{i}}{N}({\bar{Y}}_{i} - \bar{Y})^{2} \right\rbrack = 3.0420$$

If fpc is ignored, we get

$$V({\bar{y}}_{SR})_{wr} = V_{prop} + \frac{\sum_{}^{}\ W_{i}({\bar{Y}}_{i} - \bar{Y})^{2}}{n} = 3.1129$$

\(i\) The relative precision of proportional allocation is given by\
(a) without replacement method $V_{SR}/V_{prop} = 1.9636$\
(b) with replacement method $V_{SR}/V_{prop} = 1.8084$

\(ii\) The relative precision of optimum allocation is given by\
(a) without replacement method $V_{SR}/V_{opt} = 2.3742$\
(b) with replacement method $V_{SR}/V_{opt} = 2.1416$

**3.9 ESTIMATION OF GAIN IN PRECISION DUE TO STRATIFICATION**

In comparing the precision of stratified with unstratified random
sampling, it was assumed that the population values of stratum means and
variances were known.

It is sometimes of interest to examine, from a survey, how useful the
mode of stratification has been. What is available is only a stratified
sample and the problem is to estimate the gain in precision due to
stratification. An estimate of the variance of the estimate, in case of
unstratified sampling, is obtained from a stratified sample and a
comparison can be made with a situation in which no stratification is
done.

Let $n_{1},n_{2},\ldots,n_{k}$ represent the stratified sample. Also,
stratum means and variances are estimated from the sample. Let us denote
the estimated stratum means by
${\bar{y}}_{1},{\bar{y}}_{2},\ldots,{\bar{y}}_{k}$ and the estimated
variances by $s_{1}^{2},s_{2}^{2},\ldots,s_{k}^{2}$. The problem is,
therefore, to get an unbiased estimate of $V({\bar{y}}_{SR})$ based on
the given stratified sample. Here, it can be shown that an estimate
$s^{2} = \sum_{}^{}\ \sum_{}^{}\ (y - \bar{y})^{2}/(n - 1)$ will not be
an unbiased estimate of $S^{2}$.

An unbiased estimator of $V({\bar{y}}_{SR})$ based on stratified sample
is given by

$$v({\bar{y}}_{SR}) = \frac{(N - n)}{n(N - 1)}\left\lbrack \sum_{}^{}\ W_{i}s_{i}^{2} + \sum_{}^{}\ W_{i}({\bar{y}}_{i} - {\bar{y}}_{st})^{2} - \frac{1}{N}\sum_{}^{}\ W_{i}(1 - W_{i})s_{i}^{2}/n_{i} \right\rbrack\ (3.9.1)$$

The estimate of the relative gain in precision due to stratification is
thus obtained by

$$\frac{v({\bar{y}}_{SR}) - v({\bar{y}}_{st})}{v({\bar{y}}_{st})}\ (3.9.2)$$

If the sample allocation is large enough in each stratum, i.e.,
$n_{i} > 50$, the relation (3.9.1) reduces to

$$V({\bar{y}}_{SR}) = \frac{N - n}{nN}\left\lbrack \sum_{}^{}\ W_{i}s_{i}^{2} + \sum_{}^{}\ W_{i}{\bar{y}}_{i}^{2} - (\sum_{}^{}\ W_{i}{\bar{y}}_{i})^{2} \right\rbrack\ (3.9.3)$$

In actual practice, it is found that sampling variance is not much
sensitive to small or even moderate deviations in the allocations. If
allocation is proportional, i.e. $n_{i} = nW_{i}$, we can write $s^{2}$,
by applying the technique of analysis of variance, as

$$s^{2} = \sum_{}^{}\ W_{i}s_{i}^{2} + \sum_{}^{}\ W_{i}({\bar{y}}_{i} - \bar{y})^{2}$$

giving that $s^{2}$ is an unbiased estimator in proportional allocation.

**Example 3.3:** The number of pepper standards for selected villages in
each of the three strata of Trivandrum zone is as follows:

  --------------------------------------------------------------------------
  Stratum   Total number of   Number of villages   Number of pepper
            villages in the   selected from the    standards in each of the
            stratum           stratum              selected villages
  --------- ----------------- -------------------- -------------------------
  1         441               11                   41, 116, 19, 15, 144,
                                                   159, 212, 57, 28, 119, 76

  2         405               12                   39, 70, 38, 37, 161, 38,
                                                   27, 119, 36, 128, 30, 208

  3         103               7                    252, 385, 192, 296, 115,
                                                   159, 120
  --------------------------------------------------------------------------

Estimate the total number of pepper standards along with its standard
error in Trivandrum zone. Also, estimate the gain in precision due to
stratification.

The relevant calculations have been done in Table 3.2. *(Note: Table 3.2
data reconstructed from OCR artifacts for clarity)*

An estimate of the total number of pepper standards is given by

$${\widehat{Y}}_{st} = \sum_{}^{}\ N_{i}{\bar{y}}_{i} = 87,376.54$$

An estimate of variance of ${\widehat{Y}}_{st}$ is

$$v({\widehat{Y}}_{st}) = \sum_{}^{}\ N_{i}^{2}\left( 1 - \frac{n_{i}}{N_{i}} \right)\frac{s_{i}^{2}}{n_{i}} = 116,432,940.29$$

or standard error of
${\widehat{Y}}_{st} = \sqrt{116,432,940.29} = 10,790.41$

Estimate of the variance of the total number of pepper standards, when
simple random sampling is assumed, is given by

$$v({\widehat{Y}}_{SR}) = \frac{N(N - n)}{n(N - 1)}\left\lbrack \sum_{}^{}\ N_{i}s_{i}^{2} + \sum_{}^{}\ N_{i}({\bar{y}}_{i} - {\bar{y}}_{st})^{2} + \sum_{}^{}\ \frac{N_{i}(N_{i} - n_{i})}{n_{i}}s_{i}^{2} \right\rbrack = 167,269,559.37$$

Thus, the percentage gain in precision due to stratification

$$= \frac{v({\widehat{Y}}_{SR}) - v({\widehat{Y}}_{st})}{v({\widehat{Y}}_{st})} \times 100$$

$$= \frac{167,269,559.37 - 116,432,940.29}{116,432,940.29} \times 100 = 43.66\%$$

**3.10 FORMATION OF STRATA**

The problem of formation of strata has been discussed by Hagood and
Bernert (1945), Dalenius (1950, 1952), Dalenius and Gurney (1951),
Mahalanobis (1952) and Dalenius and Hodges (1959). Ekman suggested
approximations to the theoretical solutions. Cochran (1961) has examined
the application of these approximations through empirical studies. Sethi
(1963) derived the solutions for optimum points of stratification in
case of certain populations and Hess, Sethi and Balakrishnan (1966) have
applied these solutions to some empirical studies. In this section, we
shall discuss in brief the outlines for the construction of strata on
these lines, although the results derived are necessarily approximate
and of limited importance from the point of view of application.

In order to form $k$ strata, the range of main variates under study is
to be subdivided at the points $y_{1},y_{2},\ldots,y_{k - 1}$ such that
$a \leq y_{1} < y_{2} < \cdots < y_{k - 1} < b$. It has been seen
earlier in Eqn. (3.5.10) that the variance of ${\bar{y}}_{st}$ (with
proportional allocation) is given by

$$V({\bar{y}}_{st}) = \frac{1}{n}\sum_{}^{}\ W_{i}S_{i}^{2} - \frac{1}{N}\sum_{}^{}\ W_{i}S_{i}^{2}\ (3.10.1)$$

As mentioned in the beginning, the main purpose of stratification is to
increase precision, therefore $V({\bar{y}}_{st})$ is to be minimized.
Since the term $\sum_{}^{}\ W_{i}S_{i}^{2}/N$ in relation (3.10.1) is a
constant and independent of stratification, the problem is to obtain a
value of $y_{i}$ which maximizes $\sum_{}^{}\ W_{i}{\bar{Y}}_{i}^{2}$.
Assuming that all points except $y_{i}$ are fixed, it can be proved that
the value of $y_{i}$ which maximizes the term is given by iterative
procedures as

$$y_{i} = \frac{{\bar{Y}}_{i} + {\bar{Y}}_{i + 1}}{2}\ (3.10.2)$$

This shows that the best $y_{i}$ is the average of the two strata means,
which it separates. Hence, all the points, $y_{i}$
($i = 1,\ldots,k - 1$) can be obtained and the desired strata formed.

The problem of strata construction in equal and optimum allocations can
also be treated similarly. The sampling variances in equal allocation
and optimum allocation are

$$\sum_{}^{}\ \frac{W_{i}S_{i}^{2}}{n}\ \text{and}\ \frac{(\sum_{}^{}\ W_{i}S_{i})^{2}}{n},\text{respectively.}$$

Proceeding as before, the best points of stratification in the two cases
are given by

$$W_{i}\lbrack S_{i}^{2} + ({\bar{y}}_{i} - y_{i})^{2}\rbrack = W_{i + 1}\lbrack S_{i + 1}^{2} + ({\bar{y}}_{i + 1} - y_{i})^{2}\rbrack\ (3.10.3)$$

and

$$\frac{S_{i}^{2} + ({\bar{y}}_{i} - y_{i})^{2}}{S_{i}} = \frac{S_{i + 1}^{2} + ({\bar{y}}_{i + 1} - y_{i})^{2}}{S_{i + 1}}\ (3.10.4)$$

for $i = 1,\ldots,k - 1$, respectively.

Since it is difficult to apply them in practical situations, due to the
heavy computational work, some approximate solutions and simpler methods
are summarized below:\
(i) **Equalization of** $W_{i}S_{i}$**:** Dalenius and Gurney (1951)
suggested that the construction of strata on the basis of equalization
of $W_{i}S_{i}$ and giving equal allocation to the strata, would lead to
optimum stratification. This method is not convenient in practice since
it involves the calculation of $S_{i}$ for different stratification
points.\
(ii) **Equalization of strata totals:** Another rule widely used was
proposed by Mahalanobis (1952). He suggested making strata which have
the same aggregate size $W_{i}{\bar{Y}}_{i}$, with equal allocation.
This would lead to efficient stratification if the strata coefficients
of variation are the same. This procedure was found to give poorer
results when applied to normal, gamma and beta distributions (Sethi,
1963).\
(iii) **Equalization of** $W_{i}R_{i}$**:** Among the other approximate
rules suggested is the one by Ayoma (1954), in which he suggested the
formation of strata on the basis of equalization of strata ranges and
with equal allocation. Ekman (1959) suggested also the equalization of
$W_{i}R_{i}$ for forming strata with equal allocation, where $R_{i}$ is
the range of the variate in the $i$th stratum. This method is quite
simple and can be useful in practice. A good performance of Ekman\'s
method has also been reported in all these cases.\
(iv) **Equalization of cumulatives of** $\sqrt{f(y)}$**:** Dalenius and
Hodges (1959) suggested construction of strata by equalization of the
cumulative of $\sqrt{f(y)}$, where $f(y)$ is the frequency function. The
assumptions of the rule are that the distribution is bounded and that
the number of strata is large. Sethi (1963) has shown that this rule
provides optimum stratification even when the number of strata is as
small as 2 or 3.\
(v) **Equalization of** $\lbrack\sqrt{f(y)} + l(y)\rbrack/2$**:** Durbin
(1959) suggested the equalization of the cumulative frequencies of a
distribution, $\phi(y)$, which is in between the original distribution
$f(y)$ and rectangular distribution $l(y)$ over the given range of $y$.
$l(y)$ is given by $F(y)/R$, where $F(y)$ is the distribution function
of $y$ and $R$ is the range of the study variate. Thus, the best points
of stratification are obtained by equalization of the cumulatives of the
function

$$\phi(y) = \frac{\sqrt{f(y)} + l(y)}{2}$$

Rules for obtaining optimum points of stratification with different
types of estimators are given by Singh (1967), in which optimum
properties have also been studied.

**3.11 DETERMINATION OF NUMBER OF STRATA**

In context with the decision about the number of strata, the points to
be discussed are\
(i) how $V({\bar{y}}_{st})$ decreases as $k$ increases?\
(ii) how the cost of survey is affected by a change in $k$?

Dalenius and Gurney (1951), Dalenius (1953), Cochran (1961), Sethi
(1963), and Hess, Sethi and Balakrishnan (1966) have discussed the first
question and some models have been proposed for the determination of the
number of strata. For the second aspect regarding the cost with a change
in $k$, Sethi (1963) suggested that an increase in $k$ beyond 6 would
seldom be profitable. Some results which have practical significance in
surveys have been discussed in this section in the light of the above
mentioned works.

It can be shown easily that stratification increases efficiency if the
number of strata is increased by further sub-division of the strata. The
ultimate limit of stratification is the sample size so as to arrive at
the point of selecting only one unit from each stratum. But it can also
be shown that multiplication of strata beyond a reasonable number is not
profitable. In large-scale surveys, there may not be much advantage by
increasing the number of strata up to the maximum possible extent
because it may adversely affect the cost of the survey. It has been
conjectured by Dalenius (1953) that the ratio of the variance of an
estimator of the population mean based on $k$ optimum strata to that
based on $(k - 1)$ optimum strata is $(k - 1)^{2}/k^{2}$ approximately,
i.e.

$$V_{k}({\bar{y}}_{st})/V_{k - 1}({\bar{y}}_{st}) = (k - 1)^{2}/k^{2}\ (3.11.1)$$

This relationship has been verified by Cochran (1961) for $k = 2,3$ and
4, for eight distributions relating to different characteristics and
found to hold good in all cases.

For determination of the optimum number of strata, the cost function may
be defined as

$$C = a + kc_{1} + nc_{2}\ (3.11.2)$$

where $a$ is the overhead cost and $c_{1}$ and $c_{2}$ are the costs per
stratum and per unit, respectively.

Sethi (1963) has shown that for optimum stratification with proportional
and equal allocations, in case of gamma distribution, the relationship
between sampling variance and number of strata is of the form

$$V_{k}({\bar{y}}_{st}) = \frac{S^{2}}{n}(bk^{2} + ck + d)^{- 1}\ (3.11.3)$$

where $b,c,d$ are constants to be determined by considering the values
of the variance ratio for $k = 1,2$ and 3.

The optimum value of $k$ for a given cost can be determined with the
value which minimises Eqn. (3.11.3) along with restrictions given by
Eqn. (3.11.2). It can be shown easily that the optimum values of $k$ and
$n$ are given by

$$k = \sqrt{\frac{2(C - a)}{3c_{1}}},\ n = \frac{C - a}{3c_{2}}\ (3.11.4)$$

For ensuring a specified efficiency with minimum cost, a similar
procedure can be followed. Generally, this is being done by graphing the
variance or cost against the number of strata for different values of
$n$. The optimum number of strata is then to be located in them
carefully.

**3.12 METHOD OF COLLAPSED STRATA**

Sometimes the population is so heterogeneous that, to achieve a better
representation of the population, stratification is carried to the point
that only one unit is selected from each stratum. In such cases, it will
not be possible to estimate the variance of the estimated mean.

An approximate estimate of the variance of the estimated mean may be
obtained by grouping the strata in pairs. The method of grouping
together pairs of strata whose means do not differ much is called the
technique of collapsed strata.

Let the units drawn in a typical pair be $y_{1j}$ and $y_{2j}$ where $j$
takes value from 1 to $k/2$, $k$ being an even number. Then, averaging
over all samples from this pair,

$$E(y_{1j} - y_{2j})^{2} = E(y_{1j}^{2}) + E(y_{2j}^{2}) - 2E(y_{1j}y_{2j})$$

$$= \left( {\bar{Y}}_{1}^{2} + \frac{N_{1} - 1}{N_{1}}S_{1}^{2} \right) + \left( {\bar{Y}}_{2}^{2} + \frac{N_{2} - 1}{N_{2}}S_{2}^{2} \right) - 2{\bar{Y}}_{1}{\bar{Y}}_{2}$$

$$= ({\bar{Y}}_{1} - {\bar{Y}}_{2})^{2} + \frac{N_{1} - 1}{N_{1}}(S_{1}^{2} + S_{2}^{2})\ (3.12.1)$$

where the paired strata have the same size $N$. Hence, it is easy to see
that

$$\sum_{j = 1}^{k/2}\mspace{2mu} E(y_{1j} - y_{2j})^{2} = V({\bar{y}}_{st}) + \sum_{}^{}\ ({\bar{Y}}_{1j} - {\bar{Y}}_{2j})^{2}\ (3.12.2)$$

This shows that the quantity $\sum_{}^{}\ (y_{1j} - y_{2j})^{2}$, used
as an estimate of the variance, will overestimate $V({\bar{y}}_{st})$.
The second term will be negligible if the strata are so grouped in pairs
that their sample values differ very little from each other. In other
words, the pairing should be so arranged that the strata forming the
pair are about equal in size in total of $y$.

Hartley, Rao and Keifer (1969) have suggested a method where collapsing
of strata is not involved. They have used one or more auxiliary variates
on which the stratum means are supposed to have a linear regression.
This method may lead to smaller bias in variance estimation, in many
situations, than the method discussed above. Fuller (1970) has also
developed a method of strata construction that provides an unbiased
estimate of $V({\bar{y}}_{st})$ with one unit per stratum. The designs
are developed for equal and unequal probability sampling.

**3.13 POST-STRATIFICATION (STRATIFICATION AFTER SELECTION OF SAMPLE)**

In stratified sampling, it is presumed that the stratum sizes in the
sampling frame in each stratum are available. However, there are
instances where the latter is not always available, e.g. from the voter
list of a given locality, the age of an individual voter is available
although the lists of voters belonging to different age groups are not.
With some characteristic which is suitable for stratification, it is not
possible to know in advance to which stratum a sampling unit belongs
until the sample is selected. So the technique of post-stratification
consists in classifying the population and the selected sample into a
given number of strata after selection of the sample. The problem of
post-stratification has been discussed by Hansen, Hurwitz and Madow
(1953). A simple procedure for getting approximations to the variance of
a post-stratified estimator has been given by Williams (1962). We shall
examine here the gain in precision due to such post-stratification.

Let us assume that $N_{i}$ and $W_{i}$ ($i = 1,\ldots,k$) are known. If
the sample is considered as a stratified sample, then instead of sample
mean $\bar{y}$ we use the weighted mean
${\bar{y}}_{w} = \sum_{}^{}\ W_{i}{\bar{y}}_{i}$ which would be an
unbiased estimator of the population mean $\bar{Y}$. Since, for each $i$

$$E({\bar{y}}_{i}) = E\lbrack E({\bar{y}}_{i}/n_{i})\rbrack = E({\bar{Y}}_{i}) = {\bar{Y}}_{i}\ (3.13.1)$$

Hence

$$E({\bar{y}}_{w}) = \sum_{}^{}\ W_{i}E({\bar{y}}_{i}) = \sum_{}^{}\ W_{i}{\bar{Y}}_{i} = \bar{Y}\ (3.13.2)$$

Let us further suppose that the sample size is so large that none of the
$n_{i}$\'s ($i = 1,\ldots,k$) is zero. If $n_{i}$ ($i = 1,\ldots,k$) are
fixed, then we have

$$V({\bar{y}}_{w}|n_{1},\ldots,n_{k}) = \sum_{}^{}\ (1/n_{i} - 1/N_{i})W_{i}^{2}S_{i}^{2}\ (3.13.3)$$

Using the conditional variance formula given in relation 1.3.10 we have

$$V({\bar{y}}_{w}) = E\lbrack V({\bar{y}}_{w}|n_{1},n_{2},\ldots,n_{k})\rbrack + V\lbrack E({\bar{y}}_{w}|n_{1},n_{2},\ldots,n_{k})\rbrack$$

$$= E\lbrack V({\bar{y}}_{w}|n_{1},n_{2},\ldots,n_{k})\rbrack$$

since the second term is independent of $n_{i}$.

$$= E\sum_{}^{}\ (1/n_{i} - 1/N_{i})W_{i}^{2}S_{i}^{2} = \sum_{}^{}\ \lbrack E(1/n_{i}) - 1/N_{i}\rbrack W_{i}^{2}S_{i}^{2}\ (3.13.4)$$

An exact expression for relation (3.13.4) cannot be derived. However,
for large $n$ and $N$, Stephan (1945) has shown that

$$E(1/n_{i}) = 1/(nW_{i}) + (1 - W_{i})/(n^{2}W_{i}^{2})\ (3.13.5)$$

Substituting the value in relation (3.13.4), we get

$$V({\bar{y}}_{w}) = \sum_{}^{}\ \frac{(1 - f_{i})W_{i}S_{i}^{2}}{n} + \frac{1}{n^{2}}\sum_{}^{}\ (1 - W_{i})S_{i}^{2}\ (3.13.6)$$

The first term in relation (3.13.6) is the value of $V({\bar{y}}_{st})$
with proportional allocation. The second term represents the adjustment
in the variance due to post-stratification, which will be small in
comparison to the first term if $n$ is large. Hence post-stratification
is almost as precise as proportional stratified sampling for large
samples.

**3.14 DEEP STRATIFICATION**

Suppose there are two alternative criteria of stratification. The
question then arises as to which of the two criteria of stratification
is to be preferred. An obvious choice is to opt for two-way
stratification which yields $k$ rows and $k'$ columns on the basis of
those two stratification variables. There shall be $kk'$ strata and thus
a sample of size $n = kk'$ is required to estimate the population mean.
If it is required to estimate the variance of the estimated mean, at
least two observations should be taken from each stratum so the minimum
sample size must be $2kk'$. A problem arises when $n < kk'$ and it is
also desired to give proportional allocation to each criterion of
stratification. Bryant, Hartley and Jessen (1960) have given an
interesting and simple solution to this problem. The steps involved in
this procedure are as follows:\
(i) construct a square of $n^{2}$ cells with $n$ rows and $n$ columns,\
(ii) select $n$ of the cells with equal probability such that no two
selected cells belong to the same column or row,\
(iii) amalgamate the $n$ rows to form $k$ strata such that the $ij$th
stratum has an allocation of $n_{i}$ units, and\
(iv) amalgamate the $n$ columns to form $k'$ strata such that the $ij$th
stratum has an allocation of $n_{j}$ units.

Let $n_{ij}$ be the number of cells from the deep $ij$th stratum
selected in the sample. An unbiased estimator of the population mean is
given by

$${\bar{y}}_{dp} = \frac{1}{n}\sum_{}^{}\ \sum_{}^{}\ n_{ij}y_{ij}\ (3.14.1)$$

In stratified sampling, if unit A0 or B0 is drawn from stratum I we
would like to draw units c1, d1 or e1 from stratum II so that both types
of stratification are present with sample size 2. Similarly, c1 or d1
(stratum I) is desired with a0 or b0 (stratum II). The probability of a
desired combination is $0.5 \times 0.6 + 0.5 \times 0.4 = 0.5$.
Controlled selection makes the probability of these preferred samples as
high as possible. Here we find that the only non-preferred sample is
c1e1 and the total probability of preferred sample is 0.90.

It can be seen from the above example that we have conceptually
attempted to select 2 units from 4 deep strata formed on the basis of
two stratification systems. It should also be noted that the selection
is not made independently, but in a dependent manner. Yet the original
probabilities of selection of units are preserved. If the probabilities
are $p_{i}$ and $p_{j}$, then an unbiased estimator of the total is
given by

$$\widehat{Y} = \sum_{}^{}\ \frac{y_{i}}{p_{i}}\ (3.15.1)$$

The sampling variance of $\widehat{Y}$ is given by

$$V(\widehat{Y}) = \sum_{}^{}\ \sum_{}^{}\ \frac{p_{ij} - p_{i}p_{j}}{p_{i}p_{j}}y_{i}y_{j}\ (3.15.2)$$

which is different from that given by independent selection.

**SET OF PROBLEMS**

**3.1** A population is divided into 2 strata of sizes $N_{1}$ and
$N_{2}$ units. Let
$\phi = \lbrack n_{1}/n_{2}\rbrack/\lbrack n_{1}'/n_{2}'\rbrack$, where
$n_{1},n_{2}$ is a general allocation of the total sample size $n$, and
$n_{1}',n_{2}'$ is the optimum allocation for the estimation of mean in
stratified random sampling.\
(i) Show that the relative precision of a general allocation to the
optimum allocation is given by

$$RP = \phi(N_{1}U + N_{2})^{2}/(\phi N_{1}U + N_{2})(N_{1}U + \phi N_{2})$$

where $U = S_{1}/S_{2}$.\
(ii) Show that the relative precision is never less than
$4(1 + \phi)^{- 2}$.

**3.2** Prove that

$$V_{SR} = V_{prop} + \frac{(N - n)}{nN(N - 1)}\left\lbrack \sum_{}^{}\ N_{i}({\bar{Y}}_{i} - \bar{Y})^{2} - \sum_{}^{}\ (N - N_{i})S_{i}^{2} \right\rbrack$$

**3.3** The variate $x$, which is non-negative follows the exponential
distribution $\lambda e^{- \lambda x}dx$. The population is divided into
2 strata at a specified point $x_{0}$, and a stratified random sample of
size $n$ is taken with proportional allocation. Derive
$V({\bar{x}}_{st})$ as a function of $x_{0}$. Also find the optimum
value of $x_{0}$ which will minimize the variance.

**3.4** The variate $y$ has rectangular distribution in the interval
$(a,a + d)$. The interval is divided into $k$ equal sub-intervals which
form $k$ strata of equal size. From each stratum, a simple random sample
of size $n/k$ units is drawn. Let $V$ and $V_{1}$ be the variances for
stratified and unstratified samples of size $n$, respectively, prove
that $V/V_{1} = K^{- 2}$.

**3.5** For the normal population $(0,1)$, $f(y)$ denotes the ordinate
at $y$ and $w$ the weight between $y_{1}$ and $y_{2}$. If the
distribution is truncated at $y_{1}$ and $y_{2}$, show that the mean $M$
and variances $S^{2}$ of the truncated distribution are given by

$$M = \{ f(y_{1}) - f(y_{2})\}/w$$

and

$$S^{2} = 1 - \frac{y_{1}f(y_{1}) - y_{2}f(y_{2}) - \lbrack f(y_{1}) - f(y_{2})\rbrack^{2}}{w}$$

**3.6** A population is divided into 2 strata of sizes $N_{1}$ and
$N_{2}$ and s.d\'s $S_{1}$ and $S_{2}$. $S_{1}$ and $S_{2}$ are nearly
equal and fpc can be ignored, show that

$$V_{m}/V_{prop} = N(N_{1}c_{1} + N_{2}c_{2})/(N_{1}\sqrt{c_{1}} + N_{2}\sqrt{c_{2}})^{2}$$

The cost of the survey is fixed and given by
$C = c_{1}n_{1} + c_{2}n_{2}$. Assuming that $N_{1} = N_{2}$, compute
the relative increases in precision by using proportional allocation
when $c_{2}/c_{1} = 1$ and $2$.

**3.7** An investigator desires to take a stratified random sample with
the following assumptions:

  -------------------------------------------
  Stratum   $$N_{i}$$   $$S_{i}$$   $c_{i}$
                                    (in Rs.)
  --------- ----------- ----------- ---------
  1         400         10          4

  2         600         20          9
  -------------------------------------------

\(i\) Estimate the values of $n_{1}/n$ and $n_{2}/n$ which minimize the
total field cost $C = c_{1}n_{1} + c_{2}n_{2}$ for a given value of
$V({\bar{y}}_{st})$.\
(ii) Estimate the total sample size required, under the scheme of
optimum allocation, to make $V({\bar{y}}_{st}) = 1$, when fpc is
ignored.\
(iii) Also estimate the cost of the survey.

**3.8** After the sample in Exercise 3.7 was taken, it was found that
the field costs were actually Rs. 2 per unit in stratum 1 and Rs. 10 in
stratum 2. How much has the field cost changed from the anticipated
value?\
If the exact field cost is known in advance, how could the value
$V({\bar{y}}_{st}) = 1$ be obtained for the original estimated cost
given in Exercise 3.7.

**3.9** For estimating the average catch of fish on a certain part of
the coastal region, the number of fish-landing centres was divided into
two geographical strata of equal number of centres. From among the large
number of operating units, 3 units were selected by simple random
sampling for recording the weight of catch. The data obtained are given
below:

  --------------------------------------------------
  S. N. of      Catches of units              
  centres       selected (kg)                 
  ------------- ----------------------- ----- ------
                1                       2     3

  **Stratum I** 610                     754   688
  1                                           

  2             297                     411   515

  3             1187                    92    487

  4             1297                    533   1130

  5             860                     357   656

  **Stratum     1085                    956   980
  II** 1                                      

  2             817                     736   926

  3             920                     616   109

  4             511                     328   412

  5             906                     990   736
  --------------------------------------------------

Obtain an estimate of the average catch per unit, for the coast, with
its standard error. For a given number of centres to be selected, what
is the optimum break up between the two strata when the number of units
selected at a centre are 3 and 4. Calculate the number of centres and
the optimum break up necessary to estimate the average catch with 5 per
cent standard error.

**3.10** The following data show the wheat acreage of a stratified
random sample of 1 in 20 taken from a certain district:\
*(Table data provided in original text)*\
Size group 1: (1-5) acreage: 22 farms, no wheat\
Size group 2: (6-20) acreage: 25 farms, 7 acreage of wheat on one farm.\
Estimate the total wheat acreage of the district and the mean acreage of
wheat per farm. Estimate also the number of farms growing wheat. What
are the standard errors of the estimates?

**3.11** A sample survey for estimating the number of orchards of apple
was conducted in Mahasu district of Himachal Pradesh (India) during a
given year. Four strata A, B, C and D of villages, according to the
acreage of temperate fruit trees as obtained from the revenue records,
were formed. The sizes of strata (in acres) were 0-3, 3-6, 6-15 and 15
and above, respectively. A simple random sample of villages in each
stratum was selected and the number of apple orchards was noted in the
selected villages. The numbers of apple orchards for various strata are
given below:\
*(Table data provided in original text)*\
Estimate the number of orchards in the district. Calculate whether there
is any gain due to stratification, over simple random sampling. Using
the value of $s_{i}$, the mean square within the $i$th stratum as the
variance, give an optimum allocation of 48 villages.

**3.12** In a pilot sample survey conducted in the district of Wardha
(India), for estimation of total cattle population in the district, a
two way stratification of the district by tehsils and sizes of the
villages, as judged by the number of households, was adopted. A total
sample of 125 villages was distributed equally among all 9 strata.
Villages were sampled with equal probability and without replacement
within each stratum. All households in a village were enumerated for
total cattles. The total cattle and mean square between villages within
each stratum are given on page 78.\
Calculate the sampling variance of the estimated total cattle population
in the district, for the sample of 60 villages, if the villages were
selected by the method of\
(i) simple random sampling without stratification, and\
(ii) simple random sampling within each stratum and allocated in
proportion to the product $N_{i}S_{i}$.\
*(Table data provided in original text)*

**3.13** For a socio economic survey, all the villages in a region,
including the uninhabited ones, were grouped into four strata on the
basis of their altitude above sea level and population density. From
each stratum, 10 villages were selected with srs wr. The data on the
number of households in each of the sample villages are given below:\
*(Table data provided in original text)*\
(i) Obtain an estimate of the total number of households and its
standard error.\
(ii) Estimate the gain due to use of stratification as compared to
unstratified srs wr.\
(iii) Compare the efficiency of the present allocation with that of the
optimum allocation, keeping the total sample size fixed.

**3.14** Using the data given below and considering the size classes as
strata compare the efficiencies of the following alternative allocations
of a sample of 3000 factories for estimating the total output. The
sample is to be selected with srs wor within each stratum:\
(i) Proportional allocation\
(ii) Allocation proportional to total output\
(iii) Optimum allocation\
*(Table data provided in original text)*

**3.15** A survey is to be conducted for estimating the total number of
literates in a town inhabited by three communities, some particulars of
which are given below on the basis of the results of a pilot survey:

  -------------------------------------------------
  Community   Total number of     Percentage of
              persons             literates
  ----------- ------------------- -----------------
  1           60000               40

  2           10000               80

  3           30000               60
  -------------------------------------------------

\(i\) Treating the community as strata and assuming srs wr in each
stratum allocate a total sample size of 2000 persons to the strata in an
optimum manner for estimating the overall proportion of literates in the
town.\
(ii) Estimate the efficiency of stratification as compared to
unstratified sampling.

**REFERENCES**

Avadhani, N.M.S.B. and B.V. Sukhatme, \"Controlled sampling with equal
probabilities and without replacement\", *Int. Statist. Rev.*, 41,
175-183, (1973).\
Ayoma, H. \"A study of the stratified random sampling\". *Ann. Inst.
Statist. Math.*, 6, 1-36, (1954).\
Bowley, A.L., \"Measurement of precision attained in sampling,\" *Bull.
Inter. Statist. Inst.*, 22, 1-62, (1926).\
Bryant, E.G., \"An analysis of some two-way stratifications\" Ph.D.
Thesis, Iowa State University, Iowa (1955).\
Bryant, E.C., H.O. Hartley and R.J. Jessen, \"Design and estimation in
two-way stratification\" *J. Amer. Statist. Assoc.*, 55, 105-124,
(1960).\
Cochran, W.G. \"Comparison of methods for determining stratum
boundaries\" *Bull. Int. Statist. Inst.*, 38, 345-358, (1961).
