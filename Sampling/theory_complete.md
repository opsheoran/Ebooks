**1. Introduction to Sampling**

**What is Sampling?**

Sampling is not mere substitution of a partial coverage for a total
coverage. Sampling is the science and art of controlling and measuring
reliability of useful statistical information through the theory of
probability.

**Types of Data:** The data on needs and resources may be classified
into two groups.

a)  **Survey data**, comprising of data already in existence which are
    collected and recorded by observation or enquiry.

b)  **Experimental data**: Data which can only be obtained through well
    designed and controlled statistical experiments.

Survey data can further grouped into three classes:

a)  Levels and relationship of characteristics at a point of time or
    during a period of time.

b)  Knowledge of trends and relationship among characteristics over
    time.

c)  Data which are fairly stable over time.

**Sampling Unit:**

A sampling unit or elementary unit or simply a unit is an element or a
group of elements, on which observations can be made or from which the
required statistical information can be ascertained according to a well
defined procedure.

Example of units are Person, family household, farm, a period of time
such as hour, day etc. Elementary units or groups of such units, which
besides being already defined, identifiable and observable, are
convenient for purpose of sampling are called sampling units.

**Population:**

The collection of all units of a specified type in a given region at
particular point of time is termed as a population. Population may be
finite or infinite according as the no of units in it is finite or
infinite. A part or segment of a population, for each of which the
required statistical information is to be obtained separately for the
specific purpose are formed which form the domain of study.

**Sample:** A part or fraction of the population is said to constitute a
sample, or a finite sub set of the population statistical individuals is
called a sample.

**Parameter:** Any function of the values of all the population units is
known as parameter. These values are constant e.g. population mean,
population variance. Population total or Any quantity based on
population observations is called parameter.

**Statistic:** A quantity which is based on sample observations is known
as statistic. e.g. sample total, sample mean, sample variance.

**Estimator & Estimate:** An estimator is a statistic obtained by
specified procedure for estimating population parameters. It is a random
variable and differ from sample to sample. A particular value which an
estimator takes for a given sample is known as estimate.

An estimator $t$ for population parameter $\theta$ is said to be
unbiased for $\theta$ if its expected value equal to $\theta$, i.e.,
$E(t) = \theta$. Then it is said to be unbiased, otherwise if
$E(t) \neq \theta$ then it is biased.\
$$B(t) = E(t) - \theta$$

**Primary Data:** Data collected for first time by an investigator or a
person working under him. It is more reliable, time consuming and
costly.

**Secondary data:** The data collected by some person or agency in the
past for their own use. These are available in reports, news paper,
magazines, records of the department. They are cheap, less time
consuming and less reliable.

**Census vs. Sample Survey**

**Complete Enumeration:**Total counts of all units of a population for
certain characteristic is known as complete enumeration or census
survey. The money, manpower and time required for complete enumeration
will generally be large and in some limited situations the complete
enumeration is not possible.

**Sample survey:**When some of units selected in a suitable manner from
population are surveyed and an inference is drawn on the basis of survey
units about the population it is called sample survey. It is less
expensive, less time consuming.

Advantages:

1.  Less cost of survey

2.  Greater speed of getting the results

3.  Greater scope

4.  Adaptability.

**Types of Surveys:**

1.  **Ad hoc Survey:** Survey done with the intention not to repeat it
    and these are carried out to estimate the population parameters.

2.  **Repeating Survey:** The surveys which are carried out at a regular
    interval of time. These surveys are used to study the trends.
    N.S.S.O (National Sample Survey Organisation) carries out the survey
    at regular interval of time.

**Errors:**

1.  **Sampling Errors:** Sampling errors have their origin in sampling
    and they are due to the fact that only a portion of population is
    used to estimate the population parameter and for drawing the
    inference about the population. These errors are absent in complete
    enumeration. Sampling errors are decreased with an increase in
    sample size and decrease inversely proportional to square root of
    the sample size.

2.  **Non-sampling Errors:** Errors which are arising at the stage of
    ascertainment and processing of data are termed as non-sampling
    errors. Non-sampling errors are increased with the increase in
    sample size and is present in both complete enumeration as well as
    sample survey.

**Sampling Methods and Frame**

1.  **Random Sample:** Random sample is a sample drawn from the
    population in such a way that each unit in the population has a
    pre-determined probability of selection.

2.  **Simple Random Samples:** If each unit in the population has equal
    probability of selection then it is called SRS and the sampling
    procedure is called simple random sampling.

3.  **Non-Random Sample:** A sample selected not according to the law of
    chance is known as non-random sample.

4.  **Judgement or Purposive Sample:** A non-random sample drawn using
    certain amount of judgement to get a representative sample is known
    as purposive or judgement sample. In purposive sampling the units
    are selected on the basis of some auxiliary information to ensure a
    reflection of population in the sample. It is cheap, less time
    consuming, operationally convenient, sometimes more accurate when
    some confidential information is to be collected.

**Sampling Frame:** For using sampling methods for the collection of
data, it is essential to have a frame of all the sampling units of the
population to be studied with proper identification. Such a frame is
termed as a sampling frame.

**Simple Random Sampling with and Without Replacement:**

**SRSWR:** When the units in a sample are allowed to repeat in the
sample then it is termed as SRSWR. Suppose we have a population of size
$N$ and a sample of $n$ is selected with replacement then there are
$N^{n}$ possible samples and each of them will be selected with
probability $\frac{1}{N^{n}}$.

**SRSWOR:** When units are not allowed to repeat in the sample then it
is called SRSWOR. In SRSWOR, with a population size $N$, samples of $n$
can be drawn in $\binom{N}{n}$ ways each with probability of selection
is $\frac{1}{\binom{N}{n}}$.

**Estimators and Estimates:**

> **Estimator:** It is a statistic used to estimate the population
> parameter.
>
> **Estimate:** It is the specific value of the estimator based on
> sample observations for a given sample.

**Properties of Good Estimator:**

1)  It should be unbiased.

2)  It should be consistent.

3)  It should be efficient.

4)  It should be sufficient.

<!-- -->

1.  **Unbiased:** An estimator \'$t$\' for some population parameter
    $\theta$ is said to be unbiased for $\theta$ if $E(t) = \theta$ and
    if $E(t) \neq \theta$ then it is said to be biased estimator of
    $\theta$ and Bias is given by

$$B(\theta) = E(t) - \theta$$

2.  **Consistent:** An estimator $t_{n}$ based on a sample size $n$ is
    said to be consistent for $\theta$ if
    $P\lbrack|t_{n} - \theta| > \epsilon\rbrack = 0$ as $n$ is large
    i.e.

$$\lim_{n \rightarrow \infty}\mspace{2mu} P\lbrack|t_{n} - \theta| < \epsilon\rbrack = 1$$

3.  **Efficient:** An estimator is said to be more efficient than
    another estimator for parameter $\theta$ if $M(t_{1}) < M(t_{2})$
    where $M(t) = E(t - \theta)^{2}$ is known as mean square error of
    estimator.\
    *Prove that* $M(t) = V(t) + \lbrack B(t)\rbrack^{2}$

*Proof:*

$$M(t) = E\lbrack t - \theta\rbrack^{2} = E\lbrack t - E(t) + E(t) - \theta\rbrack^{2}$$

$$= E\lbrack(t - E(t))^{2} + (E(t) - \theta)^{2} + 2(t - E(t))(E(t) - \theta)\rbrack$$

$$= E\lbrack t - E(t)\rbrack^{2} + (B(\theta))^{2} + 2 \times 0$$

$$= V(t) + (B(t))^{2}$$

If unbiased, $M(t) = V(t)$.

4.  **Sufficient:** An estimator $t$ based on $n$ sample observations is
    said to be sufficient for $\theta$ if it contains all the
    information about $\theta$. Let $x_{1},x_{2},\ldots x_{n}$ be the
    sample observations then

$$L(x_{1},x_{2}\ldots x_{n}|t) = f(x_{1},x_{2}\ldots x_{n})\ldots$$

**Point and Interval Estimation:**

**Point estimation:** When an estimator is given by a single value it is
called point estimation. e.g.

$$\widehat{\mu} = \bar{x},$$

$${\widehat{\ \ \sigma}}^{2} = \frac{1}{n - 1}\sum_{}^{}\ (x_{i} - \bar{x})^{2}$$
**Interval estimation:** When the estimates are given in range with
certain degree of confidence then it is called interval estimation. e.g.
$a \leq \theta \leq b$ with 95% level of confidence. Interval estimation
are preferred over point estimation because point estimation does not
indicate the degree of confidence. Interval estimation results are more
correct than point estimators.

$$P\lbrack a \leq \theta \leq b\rbrack = 1 - \alpha$$

$$(1 - \alpha) \times 100\%\ C.I\ for\ \theta = P\{ a \leq \theta \leq b\} = 1 - \alpha$$

**Simple Random Sampling: Mathematical Derivations**

Simple Random Sampling is the most commonly used sampling scheme. In
this sampling, the units are selected from the population with equal
probability of selection. Efficiency of all sampling schemes is compared
with SRS because it is the standard sampling scheme.

**Notations:** Let us suppose that a sample of size $n$ is selected from
a population of size $N$.\
1) Let $U_{1},U_{2}\ldots U_{N}$ be the population units.\
2) $Y_{1},Y_{2}\ldots Y_{N}$ be the values / observation on these $N$
units.\
3) $u_{1},u_{2}\ldots u_{n}$ be the sample units.\
4) $y_{1},y_{2}\ldots y_{n}$ be the value of sample units.\
5) $\bar{y} = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu} y_{i} \rightarrow$
Sample Mean.\
6) $V(\bar{y}) = \frac{1}{n - 1}\sum_{}^{}\ (y_{i} - \bar{y})^{2}$.
*(Note: Unbiased sample variance is usually* $s^{2}$*,* $V(\bar{y})$
*definition follows later).*\
7) $f = \frac{n}{N} \rightarrow$ sampling fraction.\
8) $\frac{N}{n} \rightarrow$ raising fraction.\
9) $1 - f = \frac{N - n}{N} \rightarrow$ finite population correction
(f.p.c). When $N$ is large as compared to $n$,
$\frac{N - 1}{N} \approx 1$ and for large samples
$\frac{N - n}{N} \neq 1$.\
10) $\bar{Y} = \frac{1}{N}\sum_{}^{}\ Y_{i}$.\
11) $\sigma^{2} = \frac{1}{N}\sum_{}^{}\ (Y_{i} - \bar{Y})^{2}$,
$S^{2} = \frac{1}{N - 1}\sum_{}^{}\ (Y_{i} - \bar{Y})^{2}$.

**A. SRSWR (With Replacement)**

**Theorem:** Prove that in SRSWR there are $N^{n}$ possible samples each
with probability of selection $\frac{1}{N^{n}}$.\
*Proof:* In SRSWR the units are allowed to repeat in the sample. So,
every time at each draw unit is selected out of $N$ units.

1st unit is drawn in $N$ ways.\
2nd unit is drawn in $N$ ways.

Selection of sample of size $n$ is drawn in
$N \times N\cdots \times N = N^{n}$. Since each unit drawn from the
population of size $N$ and replacement of units are allowed then every
unit is selected out of $N$ units.

Probability of selecting 1st unit = $\frac{1}{N}$.\
Probability of selecting 2nd unit = $\frac{1}{N}$.\
Probability of selecting $n^{th}$ unit = $\frac{1}{N}$.\
Probability of selection of a sample =
$\frac{1}{N} \times \frac{1}{N}\ldots\frac{1}{N} = \frac{1}{N^{n}}$
ways.

**Theorem:** Prove that in SRSWR sample mean is unbiased estimator of
population mean.\
*Proof:* We know that

$$\bar{y} = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu} y_{i}$$

$$E(\bar{y}) = E\left( \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu} y_{i} \right) = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu} E(y_{i}) = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\sum_{j = 1}^{N}\mspace{2mu} P_{j}Y_{j}$$

Since $P_{j} = \frac{1}{N}$:

$$E(\bar{y}) = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\sum_{j = 1}^{N}\mspace{2mu}\frac{1}{N}Y_{j} = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\bar{Y} = \frac{n\bar{Y}}{n} = \bar{Y}$$

**Theorem:** In SRSWR $V(\bar{y}) = \frac{\sigma^{2}}{n}$.

*Proof:*

$$V(\bar{y}) = E(\bar{y} - \bar{Y})^{2} = E\left\lbrack \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu} y_{i} - \bar{Y} \right\rbrack^{2}$$

$$= E\left\lbrack \frac{\sum_{}^{}\ y_{i} - n\bar{Y}}{n} \right\rbrack^{2}$$

$$= \frac{1}{n^{2}}E\left\lbrack \sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y}) \right\rbrack^{2}$$

$$= \frac{1}{n^{2}}\left\lbrack \sum_{}^{}\ E(y_{i} - \bar{Y})^{2} + \sum_{i \neq j}^{n}\mspace{2mu}\mspace{2mu} E(y_{i} - \bar{Y})(y_{j} - \bar{Y}) \right\rbrack$$

Since draws are independent, $Cov(y_{i},y_{j}) = 0$.

$$V(\bar{y}) = \frac{1}{n^{2}}\sum_{i = 1}^{n}\mspace{2mu} E(y_{i} - \bar{Y})^{2} = \frac{1}{n^{2}}nV(y_{i}) = \frac{\sigma^{2}}{n}$$

**Theorem:** Show that in SRSWR the unbiased estimator of $V(\bar{y})$
is $\frac{s^{2}}{n}$ where

$$s^{2} = \frac{1}{n - 1}\sum_{}^{}\ (y_{i} - \bar{y})^{2}$$
*Proof:* Let us consider:

$$E\left\lbrack \frac{1}{n}\sum_{}^{}\ (y_{i} - \bar{y})^{2} \right\rbrack = E\left\lbrack \frac{1}{n}\sum_{}^{}\ (y_{i}^{2} - 2\bar{y}y_{i} + {\bar{y}}^{2}) \right\rbrack$$

$$= E\left\lbrack \frac{1}{n}\sum_{}^{}\ y_{i}^{2} - 2\bar{y}\frac{\sum_{}^{}\ y_{i}}{n} + \frac{n{\bar{y}}^{2}}{n} \right\rbrack$$

$$= E\left\lbrack \frac{1}{n}\sum_{}^{}\ y_{i}^{2} - 2{\bar{y}}^{2} + {\bar{y}}^{2} \right\rbrack = E\left\lbrack \frac{1}{n}\sum_{}^{}\ y_{i}^{2} - {\bar{y}}^{2} \right\rbrack = \frac{1}{n}\sum_{}^{}\ E(y_{i}^{2}) - E({\bar{y}}^{2})$$

We know that

$$V(\bar{y}) = E({\bar{y}}^{2}) - \lbrack E(\bar{y})\rbrack^{2}\  \Longrightarrow \ \frac{\sigma^{2}}{n} = E({\bar{y}}^{2}) - {\bar{Y}}^{2}\  \Longrightarrow \ E({\bar{y}}^{2}) = \frac{\sigma^{2}}{n} + {\bar{Y}}^{2}$$
Similarly

$$\sigma^{2} = E(y_{i}^{2}) - \lbrack E(y_{i})\rbrack^{2}\  \Longrightarrow \ \sigma^{2} = E(y_{i}^{2}) - {\bar{Y}}^{2}\  \Longrightarrow \ E(y_{i}^{2}) = \sigma^{2} + {\bar{Y}}^{2}$$
Substituting these back:

$$E\left\lbrack \frac{1}{n}\sum_{}^{}\ (y_{i} - \bar{y})^{2} \right\rbrack = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}(\sigma^{2} + {\bar{Y}}^{2}) - \left( \frac{\sigma^{2}}{n} + {\bar{Y}}^{2} \right)$$

$$= \sigma^{2} + {\bar{Y}}^{2} - \frac{\sigma^{2}}{n} - {\bar{Y}}^{2} = \sigma^{2}\left( 1 - \frac{1}{n} \right) = \frac{n - 1}{n}\sigma^{2}$$

Therefore,

$$E\left\lbrack \frac{1}{n - 1}\sum_{}^{}\ (y_{i} - \bar{y})^{2} \right\rbrack = \sigma^{2}\  \Longrightarrow \ E(s^{2}) = \sigma^{2}$$
So $s^{2}$ is an unbiased estimator of $\sigma^{2}$.\
But $V(\bar{y}) = \frac{\sigma^{2}}{n}$, so unbiased estimator of
$V(\bar{y})$ is $\frac{s^{2}}{n}$\
$$\widehat{V}(\bar{y}) = \frac{s^{2}}{n}$$

and

$$S.E(\bar{y}) = \sqrt{\frac{s^{2}}{n}} = \frac{s}{\sqrt{n}}$$

**Unbiased estimator of population total (SRSWR):**\
$$\widehat{Y} = N\bar{y}$$

$$E\left( N\bar{y} \right) = NE\left( \bar{y} \right) = N\bar{Y} = Y$$

$$V\left( \widehat{Y} \right) = V\left( N\bar{y} \right) = N^{2}V\left( \bar{y} \right) = \frac{N^{2}\sigma^{2}}{n}$$

Unbiased estimator

$$\widehat{V}\left( \widehat{Y} \right) = \frac{N^{2}s^{2}}{n}$$

$$S.E\text{~of~}\widehat{Y} = \sqrt{\frac{N^{2}s^{2}}{n}} = \frac{Ns}{\sqrt{n}}$$

95% C.I. for population total:

$$N\bar{y} \pm t_{0}\frac{Ns}{\sqrt{n}}$$

**B. SRSWOR (Without Replacement)**

**Theorem:** Prove that in SRSWOR the probability of selection of sample
of size $n$ from a population of size $N$ is $\frac{1}{\binom{N}{n}}$
and such samples are $\binom{N}{n}$.\
*Proof:* Since units are not allowed to repeat:\
1st unit is selected out of $N$ units in $N$ ways.\
Probability of selection of 1st unit is $\frac{n}{N}$.\
Probability of selection of 2nd unit is $\frac{n - 1}{N - 1}$.\
Probability of selection of 3rd unit is $\frac{n - 2}{N - 2}$.\
Probability of selection of $n^{th}$ unit is
$\frac{n - n + 1}{N - n + 1}$.\
Probability of selection of a sample of size

$$n\  = \ \frac{n}{N} \times \frac{n - 1}{N - 1} \times \cdots \times \frac{1}{N - n + 1}$$

$$= \frac{n!(N - n)!}{N!} = \frac{1}{\binom{N}{n}}$$
Out of $N$ units we want to select the samples of size $n$. There are
$\binom{N}{n}$ no. of samples of size $n$.

**Theorem:** Show that in SRSWOR $\bar{y}$ is unbiased estimator of
population mean.\
*Proof:*

$$E(\bar{y}) = \sum_{s = 1}^{\binom{N}{n}}\mspace{2mu}{\bar{y}}_{s} \times p_{s}$$

where ${\bar{y}}_{s}$ is $s^{th}$ sample mean and $p_{s}$ is the
probability of selection of $s^{th}$ sample.

$$= \sum_{s = 1}^{\binom{N}{n}}\mspace{2mu}{\bar{y}}_{s} \times \frac{1}{\binom{N}{n}} = \frac{1}{\binom{N}{n}}\sum_{s = 1}^{\binom{N}{n}}\mspace{2mu}\left( \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu} y_{i} \right)_{s}$$

Where
$\sum_{s = 1}^{\binom{N}{n}}\mspace{2mu}\sum_{i = 1}^{n}\mspace{2mu}(y_{i})_{s} \rightarrow$
Grand total of $\binom{N}{n}$ samples.\
Now each of the population unit $Y_{i}(i = 1,2\ldots N)$ appears in
$\binom{N - 1}{n - 1}$ of all possible samples.

$$\sum_{s = 1}^{\binom{N}{n}}\mspace{2mu}\left( \sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}(y_{i})_{s} \right) = \sum_{i = 1}^{N}\mspace{2mu}\binom{N - 1}{n - 1}Y_{i}$$

$$E(\bar{y}) = \frac{1}{n\binom{N}{n}}\sum_{i = 1}^{N}\mspace{2mu}\binom{N - 1}{n - 1}Y_{i}$$

Now

$$\binom{N - 1}{n - 1} = \frac{(N - 1)!}{(n - 1)!(N - n)!} = \frac{n}{N}\frac{N!}{n!(N - n)!} = \frac{n}{N}\binom{N}{n}$$

$$E(\bar{y}) = \frac{1}{n\binom{N}{n}}\frac{n}{N}\binom{N}{n}\sum_{i = 1}^{N}\mspace{2mu} Y_{i} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu} Y_{i} = \bar{Y}$$

$\bar{y}$ is unbiased estimator of $\bar{Y}$.

**Theorem:** Show that in SRSWOR

$$V(\bar{y}) = \frac{N - n}{N - 1}\frac{\sigma^{2}}{n}$$
*Proof:* We know that

$$(\bar{y}) = E(\bar{y} - E(\bar{y}))^{2} = E(\bar{y} - \bar{Y})^{2} = \sum_{s = 1}^{\binom{N}{n}}\mspace{2mu}({\bar{y}}_{s} - \bar{Y})^{2} \cdot p_{s}$$

$$= \sum_{s = 1}^{\binom{N}{n}}\mspace{2mu}({\bar{y}}_{s} - \bar{Y})^{2} \cdot \frac{1}{(\binom{N}{n})} = \frac{1}{(\binom{N}{n})}\sum_{s = 1}^{\binom{N}{n}}\mspace{2mu}\left\lbrack \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu} y_{i} - \bar{Y} \right\rbrack_{s}^{2}$$

$$= \frac{1}{\binom{N}{n}}\frac{1}{n^{2}}\sum_{s = 1}^{\binom{N}{n}}\mspace{2mu}\left\lbrack \sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}\left( y_{i} - \bar{Y} \right) \right\rbrack_{s}^{2}$$

Now

$$\left\lbrack \sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y}) \right\rbrack^{2} = \sum_{i = 1}^{n}\mspace{2mu}(y_{i} - \bar{Y})^{2} + \sum_{i \neq j}^{n}\mspace{2mu}(y_{i} - \bar{Y})(y_{j} - \bar{Y})$$
Putting in above we have:

$$V(\bar{y}) = \frac{1}{\binom{N}{n}}\frac{1}{n^{2}}\left\lbrack \sum_{s = 1}^{\binom{N}{n}}\mspace{2mu}\mspace{2mu}\left\lbrack \sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y})^{2} \right\rbrack_{s} + \sum_{s = 1}^{\binom{N}{n}}\mspace{2mu}\mspace{2mu}\left\lbrack \sum_{i \neq j}^{n}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y})(y_{j} - \bar{Y}) \right\rbrack_{s} \right\rbrack$$

Any population unit $Y_{i}$ can occur in $\binom{N - 1}{n - 1}$ samples.

$$\therefore\sum_{s = 1}^{\binom{N}{n}}\mspace{2mu}\left\lbrack \sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y})^{2} \right\rbrack_{s} = \binom{N - 1}{n - 1}\sum_{i = 1}^{N}\mspace{2mu}(Y_{i} - \bar{Y})^{2}$$

And any pair of units can occur in $\binom{N - 2}{n - 2}$ samples.

$$\therefore\sum_{s = 1}^{\binom{N}{n}}\mspace{2mu}\left\lbrack \sum_{i \neq j}^{n}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y})(y_{j} - \bar{Y}) \right\rbrack_{s} = \binom{N - 2}{n - 2}\sum_{i \neq j}^{N}\mspace{2mu}(Y_{i} - \bar{Y})(Y_{j} - \bar{Y})$$

From identity,

$$\left\lbrack \sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}(Y_{i} - \bar{Y}) \right\rbrack^{2} = \sum_{i = 1}^{N}\mspace{2mu}(Y_{i} - \bar{Y})^{2} + \sum_{i \neq j}^{N}\mspace{2mu}(Y_{i} - \bar{Y})(Y_{j} - \bar{Y}) = 0$$

$$\  \Longrightarrow \ \sum_{i \neq j}^{N}\mspace{2mu}(Y_{i} - \bar{Y})(Y_{j} - \bar{Y}) = - \sum_{i = 1}^{N}\mspace{2mu}(Y_{i} - \bar{Y})^{2}$$

Substituting these values:

$$V(\bar{y}) = \frac{1}{(\binom{N}{n})}\frac{1}{n^{2}}\left\lbrack \binom{N - 1}{n - 1}\sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}(Y_{i} - \bar{Y})^{2} - \binom{N - 2}{n - 2}\sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}(Y_{i} - \bar{Y})^{2} \right\rbrack$$

$$= \frac{1}{(\binom{N}{n})}\frac{1}{n^{2}}\left\lbrack \binom{N}{n}\frac{n}{N}\sum_{}^{}\ (Y_{i} - \bar{Y})^{2} - \frac{n(n - 1)}{N(N - 1)}\binom{N}{n}\sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}(Y_{i} - \bar{Y})^{2} \right\rbrack$$

$$= \frac{(\binom{N}{n})}{(\binom{N}{n})}\frac{1}{n^{2}}\sum_{}^{}\ (Y_{i} - \bar{Y})^{2}\left\lbrack \frac{n}{N} - \frac{n(n - 1)}{N(N - 1)} \right\rbrack$$

$$= \frac{n}{N}\frac{1}{n^{2}}\sum_{}^{}\ (Y_{i} - \bar{Y})^{2}\left\lbrack 1 - \frac{n - 1}{N - 1} \right\rbrack = \frac{1}{nN}\sum_{}^{}\ (Y_{i} - \bar{Y})^{2}\left( \frac{N - 1 - n + 1}{N - 1} \right)$$

$$= \frac{N - n}{N - 1}\frac{\sigma^{2}}{n}$$

Different forms: We know that

$$\sigma^{2} = \frac{N - 1}{N}S^{2}$$

$$V(\bar{y}) = \frac{N - n}{N - 1}\frac{N - 1}{N}\frac{S^{2}}{n} = \left( \frac{N - n}{N} \right)\frac{S^{2}}{n} = \left( 1 - \frac{n}{N} \right)\frac{S^{2}}{n} = (1 - f)\frac{S^{2}}{n}$$

$$S.E(\bar{y}) = \sqrt{V(\bar{y})} = \frac{S}{\sqrt{n}}\sqrt{1 - f} = S\sqrt{\frac{N - n}{Nn}} = S\sqrt{\frac{1}{n} - \frac{1}{N}}$$

**Unbiased Estimator of** $V(\bar{y})$ **in SRSWOR:**

$$\widehat{V}(\bar{y}) = v(\bar{y})$$
We know that

$$V(\bar{y}) = \frac{N - n}{N - 1}\frac{\sigma^{2}}{n} = \frac{N - n}{N - 1}\frac{1}{nN}\sum_{i = 1}^{N}\mspace{2mu}(Y_{i} - \bar{Y})^{2}$$

$$= \frac{N - n}{N - 1}\frac{1}{n}\left\lbrack \frac{1}{N}\sum_{}^{}\ Y_{i}^{2} - {\bar{Y}}^{2} \right\rbrack$$

$$\widehat{V}(\bar{y}) = \frac{N - n}{N - 1}\frac{1}{n}\left\lbrack Est\left( \frac{1}{N}\sum_{}^{}\ Y_{i}^{2} \right) - Est({\bar{Y}}^{2}) \right\rbrack$$

$\frac{1}{N}\sum_{}^{}\ Y_{i}$ is estimated by
$\frac{1}{n}\sum_{}^{}\ y_{i}$, i.e., $\widehat{\bar{Y}} = \bar{y}$.\
$\frac{1}{N}\sum_{}^{}\ Y_{i}^{2}$ is estimated by
$\frac{1}{n}\sum_{}^{}\ y_{i}^{2}$.\
Since

$$V(\bar{y}) = E({\bar{y}}^{2}) - {\bar{Y}}^{2}\  \Longrightarrow \ Est({\bar{Y}}^{2}) = {\bar{y}}^{2} - \widehat{V}(\bar{y})$$
Putting in equation, we get:

$$\widehat{V}(\bar{y}) = \frac{N - n}{N - 1}\frac{1}{n}\left\lbrack \frac{1}{n}\sum_{}^{}\ y_{i}^{2} - {\bar{y}}^{2} + \widehat{V}(\bar{y}) \right\rbrack$$

$$\widehat{V}(\bar{y})\left\lbrack 1 - \frac{N - n}{n(N - 1)} \right\rbrack = \frac{N - n}{n(N - 1)}\left\lbrack \frac{1}{n}\sum_{}^{}\ y_{i}^{2} - {\bar{y}}^{2} \right\rbrack$$

$$\widehat{V}(\bar{y})\left\lbrack \frac{nN - n - N + n}{n(N - 1)} \right\rbrack = \frac{N - n}{n(N - 1)}\frac{n - 1}{n}\sum_{}^{}\ (y_{i} - \bar{y})^{2}$$

$$\widehat{V}(\bar{y})\left\lbrack \frac{N(n - 1)}{n(N - 1)} \right\rbrack = \frac{N - n}{n(N - 1)}\frac{n - 1}{n}\sum_{}^{}\ (y_{i} - \bar{y})^{2}$$

$$\widehat{V}(\bar{y}) = \frac{N - n}{Nn}\frac{1}{n - 1}\sum_{}^{}\ (y_{i} - \bar{y})^{2} = \frac{N - n}{N}\frac{s^{2}}{n}$$

In SRSWR $s^{2}$ is unbiased estimator of $\sigma^{2}$. In SRSWOR
$s^{2}$ is unbiased estimator of $S^{2}$.

**Estimation of Pop Totals (SRSWOR):**\
We know that in SRSWOR $\widehat{\bar{Y}} = \bar{y}$ and population
total $= N\bar{Y}$.

$$\therefore\widehat{Y} = N\widehat{\bar{Y}} = N\bar{y}$$

$$V\left( \widehat{Y} \right) = V\left( N\bar{y} \right) = N^{2}V\left( \bar{y} \right)$$

$$= N^{2}\left( \frac{N - n}{N - 1} \right)\frac{\sigma^{2}}{n} = (1 - f)\frac{N^{2}S^{2}}{n}$$

$(1 - \alpha) \times 100\%$ C.I. for pop Mean:

$$\bar{y} \pm t_{0}\sqrt{V(\bar{y})} = \bar{y} \pm t_{0}\sqrt{\frac{N - n}{N}\frac{s^{2}}{n}}$$
$(1 - \alpha) \times 100\%$ C.I. for pop totals:

$$N\bar{y} \pm t_{0}\sqrt{N^{2}\frac{(1 - f)}{n}s^{2}}$$

**Example:**Given: $N = 5000$, $n = 16$. Mean revenue
$\bar{y} = 20\text{~per day}$. Sum of squares
$\sum_{}^{}\ (y_{i} - \bar{y})^{2} = 120$.

1.  **Sample Variance:**
    $s^{2} = \frac{1}{n - 1}\sum_{}^{}\ (y_{i} - \bar{y})^{2} = \frac{120}{15} = 8$.

2.  **95% CI for Mean:**
    $\bar{y} \pm 1.96\sqrt{\frac{s^{2}}{n}} = 20 \pm 1.96\sqrt{\frac{8}{16}} = 20 \pm 1.96(0.5) \times \sqrt{2}$.
    (Correcting the arithmetic: $\sqrt{0.5} \approx 0.707$).

3.  **Estimate of Total Revenue:**
    $\widehat{Y} = N\bar{y} = 5000 \times 20 = 100,000\text{~per day}$.

4.  **95% CI for Total:**
    $N\bar{y} \pm 1.96\sqrt{N^{2}V(\bar{y})} = 100,000 \pm 5000(1.96\sqrt{0.5})$.\
    Here is the transcription of the second document, covering simple
    random sampling for proportions, sample size estimation, and the
    relative efficiency of SRS methods.

**5. Sampling for Proportion**

This technique is used when the data is classified to two groups or
categories: individuals possessing a particular characteristic (belong
to class C) and individuals do not possessing a particular
characteristic (does not belong to class C).

In these situations, to estimate the population proportion of units
belonging to a class or to estimate the total no. of units belonging to
a category we need sampling for proportion. The selection procedure is
same as that of SRSWR or SRSWOR but estimation procedure is different.

Examples: Family (Big/Small, Joint/Nuclear, Rich/Poor), Individuals
(Smoker/Non-Smoker), Farm (Irrigated/Non-Irrigated), Plants (Damaged/Not
Damaged).

Suppose we draw a sample of size $n$ from population of size $N$. Let
$a$ be no of units out of $n$ belong to a particular category. Then the
proportion of unit belonging to a category

$$= \frac{a}{n} = p$$
Let $Y_{i}$ be the value of $i^{th}$ unit possessing a characteristic
belonging to a category then define:\
$Y_{i} = 1$ if $Y_{i} \in C$ (Belong to a class C).\
$Y_{i} = 0$ if $Y_{i} \notin C$ (does not belong to class C).\
Let $A$ be the total no. of units in population belonging to C.
$N = \text{Pop. Size}$.\
Proportion of Units belonging to $C = \frac{A}{N} = P$.

$${\bar{Y} = \frac{1}{N}\sum_{}^{}\ Y_{i} = \frac{A}{N} = P
}{\bar{y} = \frac{1}{n}\sum_{}^{}\ y_{i} = \frac{a}{n} = p}$$

**Theorem:** In SRS sample proportion $p$ is unbiased estimator of
Population proportion.\
*Proof:* We know that $\bar{Y} = \frac{1}{N}\sum_{}^{}\ Y_{i} = P$
(Population Mean).\
Now $Y_{i} = 1$ if it belongs to C, $= 0$ if it doesn\'t.\
$\sum_{}^{}\ Y_{i} =$ Total no of units belong to C.

$$\therefore\bar{Y} = \frac{1}{N}\sum_{}^{}\ Y_{i} = \frac{A}{N} = P$$
Likewise in sample, sample mean

$$\bar{y} = \frac{1}{n}\sum_{}^{}\ y_{i} = \frac{a}{n} = p$$
Now in SRS or SRSWOR $\bar{y}$ is unbiased estimator of $\bar{Y}$,
therefore $p$ is unbiased estimator of $P$.\
$\widehat{p} = p$ and $E(p) = P$.

**Theorem:** Find the variance of $p$, $V(p)$ and its unbiased
estimator.\
*Proof:* Let us consider:

$$\sigma^{2} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu}(Y_{i} - \bar{Y})^{2} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu}(Y_{i}^{2} - 2Y_{i}\bar{Y} + {\bar{Y}}^{2})$$

$$= \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu} Y_{i}^{2} - 2{\bar{Y}}^{2} + {\bar{Y}}^{2} = \frac{1}{N}\sum_{}^{}\ Y_{i}^{2} - {\bar{Y}}^{2}\ \ldots(1)$$

Now in sampling for proportion:\
If $Y_{i} \notin C$, $Y_{i}^{2} = 0$.\
If $Y_{i} \in C$, $Y_{i}^{2} = 1 = Y_{i}$.

$$\therefore\sum_{}^{}\ Y_{i}^{2} = \sum_{}^{}\ Y_{i} = A\  \Longrightarrow \ \frac{1}{N}\sum_{}^{}\ Y_{i}^{2} = \frac{A}{N} = P$$

$$\bar{Y} = \frac{1}{N}\sum_{}^{}\ Y_{i} = \frac{A}{N} = P\  \Longrightarrow \ {\bar{Y}}^{2} = P^{2}$$
Putting in (1) we have:

$$\sigma^{2} = P - P^{2} = P(1 - P) = PQ$$
Likewise considering

$${s^{2} = \frac{1}{n - 1}\sum_{i = 1}^{n}\mspace{2mu}(y_{i} - \bar{y})^{2} = \frac{1}{n - 1}(np - np^{2}) = \frac{npq}{n - 1}
}{\frac{s^{2}}{n} = \frac{pq}{n - 1}}$$

**Case 1: SRSWOR**\
We know that $V(\bar{y}) = \frac{N - n}{N - 1}\frac{\sigma^{2}}{n}$.

$$V(p) = \frac{N - n}{N - 1}\frac{PQ}{n}$$
And unbiased estimator of

$$V(\bar{y}) = \frac{N - n}{N}\frac{s^{2}}{n}\  \Longrightarrow \ \widehat{V}(p) = \frac{N - n}{N}\frac{pq}{n - 1}$$

Estimation of total no of elements is $Np$ which is unbiased estimator
of $NP$ i.e. $A$.

$$E(Np) = NE(p) = NP = A$$

$$V(\widehat{A}) = V(Np) = N^{2}V(p) = N^{2}\frac{N - n}{N - 1}\frac{PQ}{n}$$
And unbiased estimator of

$$V(\widehat{A}) = V(Np) = N^{2}\widehat{V}(p) = N^{2}\frac{N - n}{N}\frac{pq}{n - 1}$$
`<!-- -->`{=html}95% C.I. for pop proportion is

$$p \pm t_{0}\sqrt{\widehat{V}(p)}$$
`<!-- -->`{=html}95% C.I. for pop total is

$$Np \pm t_{0}\sqrt{\widehat{V}(Np)}$$

**Case 2: SRSWR**\
When the sample is drawn by SRSWR:

$$V(\bar{y}) = \frac{\sigma^{2}}{n}\  \Longrightarrow \ V(p) = \frac{PQ}{n}$$
And unbiased estimator of

$$V(\bar{y}) = \frac{s^{2}}{n}\  \Longrightarrow \ \widehat{V}(p) = \frac{pq}{n - 1}$$

**Procedures of Drawing a Simple Random Sample**

**1. Lottery Method**

1.  Assign $N$ numbers to $N$ population units.

2.  Prepare $N$ chits with nos. $1,2,\ldots,N$.

3.  Mix the chits thoroughly and draw one chit at a time. Draw the
    numbers one by one with or without replacement as the case may be.

4.  The units corresponding to which these $N$ numbers belong stand
    selected.

**2. Association of one random number to each unit**

1.  Let $N$ be a \'$d$\' digit number. Associate \'$d$\' digit numbers
    to each of the $N$ units using a random number table.

2.  Select a \'$d$\' digit number ($r$) from the random number table.

    - If $r \leq N$, select it.

    - If $r > N$, reject the draw and select the next \'$d$\' digit
      number.

3.  Continue this process until a sample of size $n$ is completed,
    either with or without replacement.

> *Probability analysis:* Out of $10^{d}$ \'$d$\' digit numbers, the
> probability of selecting a specific unit in a draw is $\frac{1}{N}$.
> Only $N$ numbers lead to selection, and $10^{d} - N$ leads to
> rejection. Probability of rejection =
> $\frac{10^{d} - N}{10^{d}} = P(r)$. Since the probability of selection
> remains the same, the system leads to SRS.\
> *Limitation:* When $10^{d} - N$ is large, a large number of draws will
> be rejected, which is a waste of time and resources.

4.  **Association of several numbers to each unit**

Let $N$ be a \'$d$\' digit number. Let $kN = N'$ be the highest \'$d$\'
digit multiple of $N$, such that $(k + 1)N$ is a $(d + 1)$ digit number.
Associate $k$ numbers to each unit as follows:

> Unit 1: $1,N + 1,2N + 1,\ldots,(k - 1)N + 1$
>
> Unit 2: $2,N + 2,2N + 2,\ldots,(k - 1)N + 2$
>
> $$\ldots$$
>
> Unit $N$: $N,2N,3N,\ldots,kN$\
> Total numbers used = $kN = N'$.

Select a \'$d$\' digit number ($R$) from $1$ to $10^{d}$. Let $R$ be the
number selected. If $R \leq N'$, find the remainder $r$ when $R$ is
divided by $N$ (or subtract the highest possible multiple of $N$ so the
remainder lies between $1$ to $N$). Select unit $U_{r}$. If $R > N'$,
reject the draw.

*Probability analysis:* Total numbers leading to selection is $kN = N'$.
Numbers associated with each unit = $k$. Probability of selection of a
unit $= \frac{k}{kN} = \frac{1}{N}$. Hence, the system leads to SRS. The
probability of rejection is $\frac{10^{d} - N'}{10^{d}}$. Since
$N' = kN$ is very large (close to $10^{d}$), the probability of
rejection is small.

**4. Simple Random Sampling from a population with an old sampling
frame**\
This technique is used when the sampling frame is not very old. It
involves minor changes (omissions and additions) rather than major ones.
Using the old frame cuts down the cost and time required to obtain a new
one.

Let\'s assume there are $N$ units in the old sampling frame, out of
which $m$ units are omitted or non-existent, and $m'$ new units are
added. Associate numbers from $1$ to $N + m'$ to these units. Select a
random number $R$.

- If $R \leq N + m'$ and points to a valid unit, select it. If it points
  to an omitted unit, reject the draw.

- If $R > N + m'$, reject the draw and take a fresh random number.\
  Continue until a sample of size $n$ is completed.

*Modifications to reduce rejection:*

- **Case 1 (when** $m > m'$**):** Allot numbers to the new units
  replacing the omitted ones. The number of remaining non-existent units
  is $m - m'$. Select a random number $r$ from $1$ to $N$. If $r$
  corresponds to a valid unit, select it. Probability of rejection is
  much smaller: $\frac{m - m'}{N}$.

- **Case 2 (when** $m < m'$**):** The $m'$ new units are assigned
  numbers. $m$ of these take the slots of the omitted units. The
  remaining $m' - m$ units are assigned new numbers
  $N + 1,N + 2,\ldots,N + m' - m$. Select a number from $1$ to
  $N + m' - m$.

**Cost Function and Sample Size Estimation**

**Cost Function:**A function which assigns the total cost of survey to
different types of costs is called cost function. In a sampling scheme
cost is a function of sample size ($n$), overhead cost ($c_{0}$), cost
of the unit ($c_{1}$), variance in the unit ($S^{2}$) and sampling
scheme.\
$C = f(n,c_{0},c_{1},S^{2})$.

**Cost function of SRS:**

Let $C$ be the total cost of the survey. $C = c_{0} + nc_{1}$.

If $C,c_{0}$ and $c_{1}$ are known to use then sample size $n$ can be
obtained as: $n = \frac{C - c_{0}}{c_{1}}$.

**Estimation of sample size in SRS:**

In SRS, as sample size increases the precision also increases but on the
other hand cost of survey will also increases. So, we have to estimate
the sample size by making a compromise between these two.

*Case I: When cost function is given.*

$$n = \frac{C - c_{0}}{c_{1}}$$
*Case II: When Permissible error and level of confidence are given.*\
Permissible Error: It is the maximum difference between estimated value
and actual value of the parameter which we are willing to tolerate.

Let us suppose that $d$ is the permissible error for estimation i.e.
$\left| \bar{y} - \bar{Y} \right| \leq d$.\
And $(1 - \alpha) \times 100$ is the level of confidence.

$$\begin{array}{r}
P\left\lbrack \left| \bar{y} - \bar{Y} \right| \leq d \right\rbrack = 1 - \alpha\ \#(1)
\end{array}$$

Also, we know that $(1 - \alpha) \times 100$ C.I for $\bar{Y}$ is
$\bar{y} \pm t_{0}\sqrt{V\left( \bar{y} \right)}$.\
$$\begin{array}{r}
P\lbrack|\bar{y} - \bar{Y}| \leq t_{0}\sqrt{V(\bar{y})}\rbrack = 1 - \alpha = 1 - \alpha\#(2)
\end{array}$$

Comparing (1) and (2) we have:\
$$d = t_{0}\sqrt{V(\bar{y})}\  \Longrightarrow \ \frac{d}{t_{0}} = \sqrt{V(\bar{y})}$$

$$\frac{d^{2}}{t_{0}^{2}} = \frac{N - n}{N}\frac{S^{2}}{n}\  \Longrightarrow \ \frac{d^{2}}{t_{0}^{2}S^{2}} = \frac{1}{n} - \frac{1}{N}$$

$$\frac{1}{N} + \frac{d^{2}}{t_{0}^{2}S^{2}} = \frac{1}{n}\  \Longrightarrow \ \frac{t_{0}^{2}S^{2} + Nd^{2}}{Nt_{0}^{2}S^{2}} = \frac{1}{n}\  \Longrightarrow \ n = \frac{Nt_{0}^{2}S^{2}}{t_{0}^{2}S^{2} + Nd^{2}}$$

$$n = \frac{t_{0}^{2}S^{2}}{\frac{t_{0}^{2}S^{2}}{N} + d^{2}}$$

Let $n_{0} = \frac{t_{0}^{2}S^{2}}{d^{2}}$.

$$n = \frac{n_{0}}{\frac{n_{0}}{N} + 1}\  \Longrightarrow \ n = \frac{n_{0}}{1 + \frac{n_{0}}{N}}$$

Where $n_{0}$ is the first approximation of sample size.

*Example:*\
$N = 500$, $n = 36$, $\bar{y} = 7.5$,
$\sum_{}^{}\ (y_{i} - \bar{y})^{2} = 350\  \Longrightarrow \ S^{2} = \frac{350}{35} = 10$.\
$P\lbrack|\bar{y} - \bar{Y}| \leq 0.5\rbrack = 0.95\  \Longrightarrow \ d = 0.5$,
$t_{0} \approx 2$ (or 1.96).\
Using
$n_{0} = \frac{t_{0}^{2}S^{2}}{d^{2}} = \frac{2^{2} \times 10}{(0.5)^{2}} = \frac{40}{0.25} = 160$.\
Final sample size needed:
$n = \frac{160}{1 + \frac{160}{500}} = \frac{160}{1 + 0.32} = \frac{160}{1.32} \approx 121$

**Estimation of Sample Size for Proportion:**\
$$P\left\lbrack |p - P| \leq d \right\rbrack = (1 - \alpha) \times 100$$

$$p \pm t_{0}\sqrt{V(p)}$$

$$d = t_{0}\sqrt{V(p)}\  \Longrightarrow \ d^{2} = t_{0}^{2}\frac{N - n}{N}\frac{pq}{n - 1}$$
Let $n_{0} = \frac{t_{0}^{2}pq}{d^{2}}$.

$$\frac{d^{2}}{t_{0}^{2}pq} = \frac{N - n}{N(n - 1)}\  \Longrightarrow \ \frac{1}{n_{0}} = \frac{N - n}{N(n - 1)}$$

$$n_{0}(N - n) = N(n - 1)\  \Longrightarrow \ n - 1 = \frac{n_{0}(N - n)}{N} = n_{0}(1 - \frac{n}{N}) = n_{0} - \frac{n_{0}n}{N}$$

$$n - \frac{n_{0}n}{N} - 1 = n_{0}\  \Longrightarrow \ n\left( 1 + \frac{n_{0}}{N} \right) = n_{0} + 1$$

$$n = \frac{n_{0} + 1}{1 + \frac{n_{0}}{N}}$$

**Relative Efficiency**

**Relative efficiency of SRSWOR as compared to SRSWR:**\
We know that in SRSWOR,
$V({\bar{y}}_{1}) = \frac{N - n}{N - 1}\frac{\sigma^{2}}{n}$.\
And in SRSWR, $V({\bar{y}}_{2}) = \frac{\sigma^{2}}{n}$.

The Relative Efficiency (R.E.) of SRSWOR with respect to SRSWR is:

$$R.E. = \frac{V({\bar{y}}_{2})}{V({\bar{y}}_{1})} = \frac{\frac{\sigma^{2}}{n}}{\frac{N - n}{N - 1}\frac{\sigma^{2}}{n}} = \frac{N - 1}{N - n}$$

Since $n > 1$, $N - 1 > N - n$, so $R.E. > 1$.\
This implies $V({\bar{y}}_{1}) < V({\bar{y}}_{2})$, meaning SRSWOR is
more precise than SRSWR. In SRSWOR, a better representative of
population units is given in the sample as compared to SRSWR.

**Stratified Sampling**

In stratified sampling, the population is divided into strata which are
homogeneous in themselves and heterogeneous from each other with respect
to a suitably chosen auxiliary variable $x$, which is highly correlated
with the variable under study. These strata are considered as
sub-populations.

The samples are drawn independently from each stratum. These strata and
samples are drawn independently from the strata, and estimates for the
population are obtained by suitably combining strata estimates.

This sampling scheme is used when the population is heterogeneous and to
give a proper representation to different categories or groups. These
groups are considered as strata. In general, stratified sampling is more
precise than SRS.

**Criteria for Selecting Auxiliary Variable** $x$**:**

1.  It should be cheap and easy to collect.

2.  It should be highly correlated with the variable under study.

3.  Population total, i.e., $\sum_{}^{}\ X_{i} = X$, should be known.

  --------------------------------------------------------------------------------------------------------------
  Strata ($h$) Strata Size      Strata Mean     Strata Variance Sample Size      Sample Mean     Sample Variance
                ($N_{h}$)    (${\bar{Y}}_{h}$)   ($S_{h}^{2}$)   ($n_{h}$)    (${\bar{y}}_{h}$)  ($s_{h}^{2}$)
  ------------ ------------ ------------------- --------------- ------------ ------------------- ---------------
       1        $$N_{1}$$    $${\bar{Y}}_{1}$$   $$S_{1}^{2}$$   $$n_{1}$$    $${\bar{y}}_{1}$$  $$s_{1}^{2}$$

       2        $$N_{2}$$    $${\bar{Y}}_{2}$$   $$S_{2}^{2}$$   $$n_{2}$$    $${\bar{y}}_{2}$$  $$s_{2}^{2}$$

       3        $$N_{3}$$    $${\bar{Y}}_{3}$$   $$S_{3}^{2}$$   $$n_{3}$$    $${\bar{y}}_{3}$$  $$s_{3}^{2}$$

       4        $$N_{4}$$    $${\bar{Y}}_{4}$$   $$S_{4}^{2}$$   $$n_{4}$$    $${\bar{y}}_{4}$$  $$s_{4}^{2}$$

   $$\ldots$$   $$\ldots$$      $$\ldots$$        $$\ldots$$     $$\ldots$$      $$\ldots$$      $$\ldots$$

     $$h$$      $$N_{h}$$    $${\bar{Y}}_{h}$$   $$S_{h}^{2}$$   $$n_{h}$$    $${\bar{y}}_{h}$$  $$s_{h}^{2}$$

   $$\ldots$$   $$\ldots$$      $$\ldots$$        $$\ldots$$     $$\ldots$$      $$\ldots$$      $$\ldots$$

     $$L$$      $$N_{L}$$    $${\bar{Y}}_{L}$$   $$S_{L}^{2}$$   $$n_{L}$$    $${\bar{y}}_{L}$$  $$s_{L}^{2}$$
  --------------------------------------------------------------------------------------------------------------

**Variables:**\
$Y_{hi} =$ value of $i^{th}$ unit in $h^{th}$ strata.\
$i = 1,2\ldots n_{h}$.\
$h = 1,2\ldots L$.

Population Mean

$$= \frac{1}{N}\sum_{h = 1}^{L}\mspace{2mu}\sum_{i = 1}^{N_{h}}\mspace{2mu} Y_{hi}$$
Population Mean of $h^{th}$ strata

$$= {\bar{Y}}_{h} = \frac{1}{N_{h}}\sum_{i = 1}^{N_{h}}\mspace{2mu} Y_{hi}\  \Longrightarrow \ \sum_{i = 1}^{N_{h}}\mspace{2mu} Y_{hi} = N_{h}{\bar{Y}}_{h}$$

$$\bar{Y} = \frac{1}{N}\sum_{h = 1}^{L}\mspace{2mu} N_{h}{\bar{Y}}_{h}$$
Strata variance

$$S_{h}^{2} = \frac{1}{N_{h} - 1}\sum_{i = 1}^{N_{h}}\mspace{2mu}(Y_{hi} - {\bar{Y}}_{h})^{2}$$
Let $n_{1},n_{2},\ldots,n_{L}$ be the sample sizes drawn from strata
$1,2,\ldots,L$.

Let $y_{hi}$ be the value of $i^{th}$ unit from the sample drawn from
the $h^{th}$ stratum, where $h = 1,2,\ldots,L$ and
$i = 1,2,\ldots,n_{h}$.

Sample mean

$${\bar{y}}_{h} = \frac{1}{n_{h}}\sum_{i = 1}^{n_{h}}\mspace{2mu} y_{hi}$$
Sample variance

$$s_{h}^{2} = \frac{1}{n_{h} - 1}\sum_{i = 1}^{n_{h}}\mspace{2mu}(y_{hi} - {\bar{y}}_{h})^{2}$$

**Theorem:** Show that in stratified sampling ${\bar{y}}_{st}$ is
unbiased estimator of population mean where
${\bar{y}}_{st} = \frac{1}{N}\sum_{}^{}\ N_{h}{\bar{y}}_{h}$ and
$V({\bar{y}}_{st}) = \frac{1}{N^{2}}\sum_{}^{}\ N_{h}^{2}(\frac{N_{h} - n_{h}}{N_{h}})\frac{S_{h}^{2}}{n_{h}}$.\
*Proof:* Let us assume that samples are drawn by SRSWOR for different
strata.

$$E({\bar{y}}_{st}) = E\left\lbrack \frac{1}{N}\sum_{h = 1}^{L}\mspace{2mu}\mspace{2mu} N_{h}{\bar{y}}_{h} \right\rbrack = \frac{1}{N}\sum_{h = 1}^{L}\mspace{2mu} N_{h}E({\bar{y}}_{h})$$

Since samples are drawn independently and each strata behave like a
population,

$$({\bar{y}}_{h}) = {\bar{Y}}_{h}$$

$$E({\bar{y}}_{st}) = \frac{1}{N}\sum_{h = 1}^{L}\mspace{2mu} N_{h}{\bar{Y}}_{h} = \bar{Y}$$

$\frac{1}{N}\sum_{h = 1}^{L}\mspace{2mu} N_{h}{\bar{y}}_{h}$ is unbiased
estimator of $\bar{Y}$.

Variance:

$$V({\bar{y}}_{st}) = V\left( \frac{1}{N}\sum_{h = 1}^{L}\mspace{2mu}\mspace{2mu} N_{h}{\bar{y}}_{h} \right) = \frac{1}{N^{2}}\sum_{h = 1}^{L}\mspace{2mu} N_{h}^{2}V({\bar{y}}_{h})$$

$$= \frac{1}{N^{2}}\sum_{h = 1}^{L}\mspace{2mu} N_{h}^{2}\left( \frac{N_{h} - n_{h}}{N_{h}} \right)\frac{S_{h}^{2}}{n_{h}}$$

$$= \frac{1}{N^{2}}\left\lbrack \sum_{h = 1}^{L}\mspace{2mu}\mspace{2mu}\frac{N_{h}^{2}S_{h}^{2}}{n_{h}} - \sum_{}^{}\ \frac{N_{h}^{2}n_{h}}{N_{h}n_{h}}S_{h}^{2} \right\rbrack$$

$$= \frac{1}{N^{2}}\left\lbrack \sum_{h = 1}^{L}\mspace{2mu}\mspace{2mu}\frac{N_{h}^{2}S_{h}^{2}}{n_{h}} - \sum_{}^{}\ N_{h}S_{h}^{2} \right\rbrack$$

$$= \sum_{}^{}\ \frac{W_{h}^{2}S_{h}^{2}}{n_{h}} - \frac{1}{N}\sum_{}^{}\ W_{h}S_{h}^{2}$$

When $N$ is very large:

$$V({\bar{y}}_{st}) = \sum_{}^{}\ \frac{W_{h}^{2}S_{h}^{2}}{n_{h}}$$

**Unbiased Estimator of** $V({\bar{y}}_{st})$**:**

In stratified sampling, each stratum behaves like a population with
samples drawn independently via SRSWR or SRSWOR. In SRSWOR, $s^{2}$ is
an unbiased estimator of $S^{2}$. Therefore, $s_{h}^{2}$ is an unbiased
estimator of $S_{h}^{2}$.

$$\widehat{V}({\bar{y}}_{st}) = \frac{1}{N^{2}}\sum_{h = 1}^{L}\mspace{2mu} N_{h}^{2}\left( \frac{N_{h} - n_{h}}{N_{h}} \right)\frac{s_{h}^{2}}{n_{h}}$$

**Estimation of Population Total:**\
$${\widehat{Y}}_{st} = N{\bar{y}}_{st}$$
Variance of estimated population total:

$$V({\widehat{Y}}_{st}) = N^{2}V({\bar{y}}_{st}) = \sum_{h = 1}^{L}\mspace{2mu} N_{h}^{2}\left( \frac{N_{h} - n_{h}}{N_{h}} \right)\frac{S_{h}^{2}}{n_{h}}$$

Estimated variance of estimated population total:

$$\widehat{V}({\widehat{Y}}_{st}) = \sum_{h = 1}^{L}\mspace{2mu} N_{h}^{2}\left( \frac{N_{h} - n_{h}}{N_{h}} \right)\frac{s_{h}^{2}}{n_{h}}$$

Confidence Intervals:

1.  C.I. for Population Mean ${\bar{Y}}_{st}$:
    ${\bar{y}}_{st} \pm t_{0}\sqrt{\widehat{V}({\bar{y}}_{st})}$

2.  C.I. for Population Total ${\widehat{Y}}_{st}$:
    $N{\bar{y}}_{st} \pm Nt_{0}\sqrt{\widehat{V}({\bar{y}}_{st})}$

**Situations Under Which Stratified Sampling is Used:**

1.  When the population sampling frame is available in the form of
    sub-frames, then sub-frames can be used as strata.

2.  When the results are required not only for the population but also
    for strata.

3.  When different information is available for different strata, then
    different sampling designs are used for different strata.

4.  When the survey organization has offices in different zones, these
    zones can be taken as strata.

5.  When the population is heterogeneous and divided into different
    groups or categories which are homogeneous in themselves.

**Points Under Consideration in Stratified Sampling:**

1.  Number of strata.

2.  Demarcation of strata.

3.  Allocation of sample size to various strata.

4.  Selection of auxiliary variable ($x$) or stratification variable.
    $x$ should be cheap, easy to collect, and highly correlated with the
    variable under study.

*Number of Strata:* Larger the number of strata, higher the precision.
Dalenius (1953) showed that in most stratified sampling from
populations, this relation holds:

$$V_{L}({\bar{y}}_{st}) = \left( \frac{L - 1}{L} \right)^{2}V_{L - 1}({\bar{y}}_{st})$$

Since $\frac{L - 1}{L} \leq 1$,

$$V_{L}({\bar{y}}_{st}) < V_{L - 1}({\bar{y}}_{st})$$
Since two units are required to be selected from each strata in order to
get the unbiased estimator of $V({\bar{y}}_{st})$, this restricts the
maximum number of strata we can have.

*Demarcation of Strata:*

In addition to the number of strata, the variance $V({\bar{y}}_{st})$
also depends upon the points of demarcation of strata. For dividing the
population, we need $y_{1},y_{2},\ldots,y_{L - 1}$ as the points of
demarcation. A set of optimum points of stratification is one which
minimizes the $V({\bar{y}}_{st})$ keeping all other factors fixed.

**Allocation of Sample Size in different strata:**

Following points should be consider for allocation: 1) Strata size
($N_{h}$) 2) Variability in stratum ($S_{h}$) 3) Cost of taking
observation for sampling units in different strata ($C_{h}$).\
1) Equal allocation 2) Proportional Allocation 3) Optimum Allocation.

**Proportional Allocation:**\
**Case I:** When only strata size is known. Select sample size
proportional to strata size i.e.

$$n_{h} \propto N_{h}\  \Longrightarrow \ n_{h} = kN_{h}$$

$$\sum_{}^{}\ n_{h} = k\sum_{}^{}\ N_{h}\  \Longrightarrow \ n = kN\  \Longrightarrow \ k = \frac{n}{N}$$

$$\therefore n_{h} = \frac{n}{N}N_{h}$$
**Case II:** When strata variance is also known.

$$n_{h} \propto N_{h}S_{h}\  \Longrightarrow \ n_{h} = kN_{h}S_{h}$$

$$n = k\sum_{}^{}\ N_{h}S_{h}\  \Longrightarrow \ k = \frac{n}{\sum_{}^{}\ N_{h}S_{h}}$$

$$\therefore n_{h} = \frac{nN_{h}S_{h}}{\sum_{}^{}\ N_{h}S_{h}}$$
**Case III:** Neyman Allocation. If cost of survey per unit from
different strata ($C_{h}$) is also given then

$$n_{h} \propto \frac{N_{h}S_{h}}{\sqrt{C_{h}}}\  \Longrightarrow \ n_{h} = k\frac{N_{h}S_{h}}{\sqrt{C_{h}}}$$

$$n = k\sum_{}^{}\ \frac{N_{h}S_{h}}{\sqrt{C_{h}}}\  \Longrightarrow \ k = \frac{n}{\sum_{}^{}\ N_{h}S_{h}/\sqrt{C_{h}}}$$

$$n_{h} = \frac{n}{\sum_{}^{}\ N_{h}S_{h}/\sqrt{C_{h}}}\frac{N_{h}S_{h}}{\sqrt{C_{h}}}$$

**Cost Function of Stratified Sampling:**

If $C_{0}$ is the overhead cost and $C_{1},C_{2},\ldots,C_{L}$ be the
cost of survey per unit from each stratum, then the cost function is
given by:

$$C = C_{0} + n_{1}C_{1} + n_{2}C_{2} + \cdots + n_{L}C_{L} = C_{0} + \sum_{h = 1}^{L}\mspace{2mu} n_{h}C_{h}$$

**Theorem:** Prove that in proportional allocation
$V_{prop}({\bar{y}}_{st}) = \frac{1 - f}{n}\sum_{}^{}\ W_{h}S_{h}^{2}$.\
*Proof:* We know that

$$V({\bar{y}}_{st}) = \frac{1}{N^{2}}\sum_{}^{}\ N_{h}\left( \frac{N_{h}}{n_{h}} - 1 \right)S_{h}^{2}$$
Under proportional allocation

$$\frac{n_{h}}{N_{h}} = \frac{n}{N}\  \Longrightarrow \ \frac{N_{h}}{n_{h}} = \frac{N}{n}$$

$$V_{prop}({\bar{y}}_{st}) = \frac{1}{N^{2}}\sum_{h = 1}^{L}\mspace{2mu} N_{h}\left( \frac{N}{n} - 1 \right)S_{h}^{2}$$

$$= \frac{N - n}{nN^{2}}\sum_{}^{}\ N_{h}S_{h}^{2} = \frac{N - n}{nN}\sum_{}^{}\ \frac{N_{h}}{N}S_{h}^{2}$$

$$= \left( \frac{N - n}{N} \right)\frac{1}{n}\sum_{}^{}\ W_{h}S_{h}^{2} = \frac{1 - f}{n}\sum_{}^{}\ W_{h}S_{h}^{2}$$

**Optimum Allocation:**\
Theorem: Show that in optimum allocation in stratified sampling
$n_{h} \propto \frac{N_{h}S_{h}}{\sqrt{C_{h}}}$.\
*Proof:* Let us define Lagrange\'s multiplier $\Phi$.

$$\Phi = V({\bar{y}}_{st}) + \lambda(C_{0} + C_{1}n_{1} + \cdots + n_{h}C_{h} + \ldots n_{L}C_{L} - C)$$

$$\Phi = \sum_{}^{}\ \frac{W_{h}^{2}S_{h}^{2}}{n_{h}} - \frac{1}{N}\sum_{}^{}\ W_{h}S_{h}^{2} + \lambda(C_{0} + \sum_{}^{}\ n_{h}C_{h} - C)$$

Differentiating w.r.t $n_{h}$:

$$\frac{\partial\Phi}{\partial n_{h}} = - \frac{W_{h}^{2}S_{h}^{2}}{n_{h}^{2}} + \lambda C_{h} = 0$$

$$\lambda C_{h} = \frac{W_{h}^{2}S_{h}^{2}}{n_{h}^{2}}\  \Longrightarrow \ n_{h}^{2} = \frac{1}{\lambda}\frac{W_{h}^{2}S_{h}^{2}}{C_{h}}\  \Longrightarrow \ n_{h} = \frac{1}{\sqrt{\lambda}}\frac{W_{h}S_{h}}{\sqrt{C_{h}}}$$

Taking the summation:

$$n = \frac{1}{\sqrt{\lambda}}\sum_{}^{}\ \frac{W_{h}S_{h}}{\sqrt{C_{h}}}$$
Dividing:

$$\frac{n_{h}}{n} = \frac{W_{h}S_{h}/\sqrt{C_{h}}}{\sum_{}^{}\ W_{h}S_{h}/\sqrt{C_{h}}}\  \Longrightarrow \ n_{h} = \frac{nW_{h}S_{h}/\sqrt{C_{h}}}{\sum_{}^{}\ W_{h}S_{h}/\sqrt{C_{h}}} = \frac{nN_{h}S_{h}/\sqrt{C_{h}}}{\sum_{}^{}\ N_{h}S_{h}/\sqrt{C_{h}}}$$

**Determination of Sample Size under Optimum Allocation:**

> **Case I:** When cost is fixed and we want to minimize the variance.

$$C - C_{0} = \sum_{h = 1}^{L}\mspace{2mu} n_{h}C_{h}$$

Substituting $n_{h}$, we get

$$n = (C - C_{0})\frac{\sum_{}^{}\ N_{h}S_{h}/\sqrt{C_{h}}}{\sum_{}^{}\ N_{h}S_{h}\sqrt{C_{h}}}$$

> **Case II:** When variance is fixed and we minimize the cost.

$$V({\bar{y}}_{st}) + \frac{1}{N}\sum_{}^{}\ W_{h}S_{h}^{2} = \sum_{}^{}\ \frac{W_{h}^{2}S_{h}^{2}}{n_{h}}$$

Substituting $n_{h}$, we get

$$n = \frac{(\sum_{}^{}\ W_{h}S_{h}\sqrt{C_{h}})(\sum_{}^{}\ W_{h}S_{h}/\sqrt{C_{h}})}{V({\bar{y}}_{st}) + \frac{1}{N}\sum_{}^{}\ W_{h}S_{h}^{2}}$$

**Theorem:** If f.p.c are ignored then show that
$V_{opt} < V_{prop} < V_{random}$.\
*Proof:*

$$V_{random} = \frac{S^{2}}{n}$$

$$V_{prop} = \frac{N - n}{nN}\sum_{}^{}\ \frac{N_{h}S_{h}^{2}}{N} \approx \frac{1}{nN}\sum_{}^{}\ N_{h}S_{h}^{2}$$

$$V_{opt} = \frac{(\sum_{}^{}\ N_{h}S_{h})^{2}}{nN^{2}} - \frac{1}{N^{2}}\sum_{}^{}\ N_{h}S_{h}^{2} \approx \frac{(\sum_{}^{}\ N_{h}S_{h})^{2}}{nN^{2}}$$

We know that:

$$S^{2} = \frac{1}{N - 1}\sum_{h = 1}^{L}\mspace{2mu}\sum_{i = 1}^{N_{h}}\mspace{2mu}(Y_{hi} - \bar{Y})^{2}\  \Longrightarrow \ (N - 1)S^{2} = \sum_{}^{}\ \sum_{}^{}\ (Y_{hi} - \bar{Y})^{2}$$

$$= \sum_{}^{}\ \sum_{}^{}\ (Y_{hi} - {\bar{Y}}_{h} + {\bar{Y}}_{h} - \bar{Y})^{2}$$

$$= \sum_{}^{}\ \sum_{}^{}\ (Y_{hi} - {\bar{Y}}_{h})^{2} + \sum_{}^{}\ \sum_{}^{}\ ({\bar{Y}}_{h} - \bar{Y})^{2} + 0\text{~cross terms}$$

$$= \sum_{}^{}\ (N_{h} - 1)S_{h}^{2} + \sum_{}^{}\ N_{h}({\bar{Y}}_{h} - \bar{Y})^{2}$$

Ignoring f.p.c.:

$$NS^{2} = \sum_{}^{}\ N_{h}S_{h}^{2} + \sum_{}^{}\ N_{h}({\bar{Y}}_{h} - \bar{Y})^{2}$$

Dividing by $nN$:

$$\frac{S^{2}}{n} = \frac{\sum_{}^{}\ N_{h}S_{h}^{2}}{nN} + \frac{\sum_{}^{}\ N_{h}({\bar{Y}}_{h} - \bar{Y})^{2}}{nN}$$

$$V_{random} = V_{prop} + (\text{Positive quantity})\  \Longrightarrow \ V_{prop} < V_{random}$$

Now:

$$V_{prop} - V_{opt} = \frac{\sum_{}^{}\ N_{h}S_{h}^{2}}{nN} - \frac{(\sum_{}^{}\ N_{h}S_{h})^{2}}{nN^{2}}$$

$$= \frac{1}{nN}\left\{ \sum_{}^{}\ N_{h}S_{h}^{2} - \left( \frac{\sum_{}^{}\ N_{h}S_{h}}{\sqrt{N}} \right)^{2} \right\}$$

$$= \frac{1}{nN}\left\lbrack \sum_{}^{}\ N_{h}(S_{h} - \bar{S})^{2} \right\rbrack\text{~where~}\bar{S} = \frac{\sum_{}^{}\ N_{h}S_{h}}{N}$$

Which is a positive quantity, so

$$V_{prop} - V_{opt} > 0\  \Longrightarrow \ V_{opt} < V_{prop}$$
Combining these two results we have:

$$V_{opt} < V_{prop} < V_{random}$$

**Multiple Stratification or Deep Stratification:**

In multi-subject surveys, when all the characters under study are
related to a common auxiliary variable $x$, then stratification is done
according to auxiliary variable $x$. But in many situations, the
characters under study are related to different auxiliary variables. In
such situations, first stratification is done according to the first
auxiliary variable, then further stratification is done on the second
auxiliary variable, and so on. Such stratification is called multiple or
deep stratification.

**Post Stratification:**

This technique of stratification is used when stratification was not
planned initially and the sample is drawn from the population by SRS or
some other sampling techniques. But later on, it was thought necessary
to have the results not only for the population but also for samples.
Then the selected sample is divided into a number of strata, and the
modified estimator based on post strata
${\bar{y}}_{st}' = \sum_{}^{}\ W_{h}'(y_{h}'/n_{h}')$ is used.

**Quota Sampling:**

In quota sampling, the population is divided into a number of groups or
strata depending upon the geographical conditions. The sample size for
each stratum is obtained by proportional allocation:
$n_{h} \propto N_{h}\  \Longrightarrow \ n_{h} = \frac{n}{N}N_{h}$. The
units from each stratum are selected not by the law of chance but as per
operational convenience. Hence, it differs from stratified sampling.

**Varying Probability Sampling (PPS)**

In many situations when the units under study have unequal sizes and
contribute unequally to the population then instead of selecting units
in equal probability the units are selected with varying probability
i.e. larger units are given more chance of selection. This method is
likely to be more precise than SRS.

In PPS, sampling size $X_{i}$ is the value of auxiliary variable which
is highly correlated with variable under study.

Prob of selection of $i^{th}$ unit

$$= p_{i} \propto X_{i}\  \Longrightarrow \ p_{i} = kX_{i}$$

$${1 = k\sum_{i = 1}^{N}\mspace{2mu} X_{i} = kX\  \Longrightarrow \ k = \frac{1}{X}
}{\  \Longrightarrow \ p_{i} = \frac{X_{i}}{X}}$$

**Theorem:** Results show that in PPS
${\widehat{Y}}_{pps} = \frac{1}{n}\sum_{}^{}\ \frac{y_{i}}{p_{i}}$ is
unbiased estimator of population total $Y$.

$$E({\widehat{Y}}_{pps}) = E\left\lbrack \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}\frac{y_{i}}{p_{i}} \right\rbrack = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu} E\left( \frac{y_{i}}{p_{i}} \right)$$

Let $i^{th}$ unit of sample be the $r^{th}$ unit of population then:

$$E({\widehat{Y}}_{pps}) = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\sum_{r = 1}^{N}\mspace{2mu} P_{r}\frac{Y_{r}}{P_{r}} = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\sum_{r = 1}^{N}\mspace{2mu} Y_{r} = \frac{n}{n}Y = Y$$

**Variance in PPS:**

$$V({\widehat{Y}}_{pps}) = V\left( \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}\frac{y_{i}}{p_{i}} \right) = \frac{1}{n^{2}}\sum_{i = 1}^{n}\mspace{2mu} V\left( \frac{y_{i}}{p_{i}} \right)$$

$$= \frac{1}{n^{2}}\left\lbrack \sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}\sum_{r = 1}^{N}\mspace{2mu}\mspace{2mu}\left( \frac{Y_{r}}{P_{r}} - Y \right)^{2}P_{r} \right\rbrack$$

$$= \frac{1}{n}\left\lbrack \sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}\frac{Y_{i}^{2}}{P_{i}} - 2Y^{2} + Y^{2} \right\rbrack = \frac{1}{n}\left\lbrack \sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}\frac{Y_{i}^{2}}{P_{i}} - Y^{2} \right\rbrack$$

Unbiased estimator:

$$\widehat{V}({\widehat{Y}}_{pps}) = \frac{1}{n(n - 1)}\sum_{i = 1}^{n}\mspace{2mu}\left( \frac{y_{i}}{p_{i}} - {\widehat{Y}}_{pps} \right)^{2}$$

**Methods of Selecting PPS Samples:**

1.  **Cumulative Total Method:** We associate numbers to the population
    units according to their cumulative size. If a random number $R$
    from $1$ to $X$ is selected, the unit to which this $R$ belongs
    stands selected.

> *Drawbacks:* This method involves cumulative totals which are very
> difficult to compute for large $N$.

2.  **Lahiri\'s Method:** This method does not involve the cumulation of
    sizes. Let $M = max(X_{1},X_{2},\ldots,X_{N})$. Select a random
    number $i$ from $1$ to $N$, and a random number $r$ from $1$ to $M$.
    If $r \leq X_{i}$, then select the $i^{th}$ unit; if $r > X_{i}$,
    reject the draw.\
    *Drawbacks:* If some units have larger sizes compared to other
    units, $M$ will be large, which results in more draws leading to
    rejection, hence it is time-consuming and costly.

3.  **Split Method:** To overcome Lahiri\'s drawback, one or two units
    with larger sizes are split into two or more units with smaller
    sizes. This automatically reduces $M$ and the probability of
    rejection.

4.  **PPS Sampling When the Frame is a Map:** If the frame consists of
    maps showing boundaries, select a random number $x_{i}$ from $1$ to
    $N$ and $y_{i}$ from $1$ to $M$ (the limits of the map axes). Plot
    point $(x_{i},y_{i})$ on the map. If it falls in a unit, that unit
    stands selected.

**Systematic Sampling:**

In systematic sampling, only one unit is selected at random and the
remaining units in the sample get automatically selected by giving equal
spacing in the population. To select a sample of size $n$ from a
population of size $N$, we find the sampling interval $k = \frac{N}{n}$
and select a random start $r$ from $1$ to $k$. The units selected are
$u_{r},u_{r + k},u_{r + 2k},\ldots,u_{r + (n - 1)k}$.

*Advantages:* Samples are well spread over the entire population and
hence systematic sampling is in general more precise than SRS.
Operationally more convenient and less costly.\
*Limitations:* Two consecutive units cannot be selected; hence we cannot
find the unbiased estimator of the variance of the estimated mean.

**Ratio Estimators**

**Upper Bound of Ratio of Bias of** $\widehat{R}$**:**\
Theorem: Prove that
$\frac{|Bias\text{~in~}\widehat{R}|}{\sigma_{\widehat{R}}} \leq C.V.(\bar{x})$.
*(Note: User\'s notes say*
$C.V.(\bar{x}) = \frac{\sigma_{\bar{x}}}{\bar{x}}$*).*\
*Proof:* We know that:

$$\rho_{\widehat{R}\bar{x}} = \frac{Cov(\widehat{R},\bar{x})}{\sigma_{\widehat{R}} \cdot \sigma_{\bar{x}}}\  \Longrightarrow \ Cov(\widehat{R},\bar{x}) = \rho_{\widehat{R}\bar{x}}\sigma_{\widehat{R}} \cdot \sigma_{\bar{x}}$$

Also

$$Cov(\widehat{R},\bar{x}) = E\lbrack\widehat{R}\bar{x}\rbrack - E(\widehat{R})E(\bar{x})$$

$$= E\left( \frac{\bar{y}}{\bar{x}}\bar{x} \right) - E(\widehat{R}) \cdot E(\bar{x})$$

$$= E(\bar{y}) - E(\widehat{R}) \cdot \bar{x} = \bar{Y} - E(\widehat{R}) \cdot \bar{x}$$

$$\therefore E(\widehat{R}) = \frac{\bar{Y} - Cov(\widehat{R},\bar{x})}{\bar{x}} = \frac{\bar{Y}}{\bar{x}} - \frac{Cov(\widehat{R},\bar{x})}{\bar{x}}$$

$$E(\widehat{R}) = R - \frac{Cov(\widehat{R},\bar{x})}{\bar{x}}$$

Bias in

$$\widehat{R} = R - E(\widehat{R}) = R - \left( R - \frac{Cov(\widehat{R},\bar{x})}{\bar{x}} \right) = \frac{Cov(\widehat{R},\bar{x})}{\bar{x}}$$

$$\text{Bias in~}\widehat{R} = \frac{\rho_{\widehat{R}\bar{x}}\sigma_{\widehat{R}} \cdot \sigma_{\bar{x}}}{\bar{x}}$$

$$\frac{|\text{Bias in~}\widehat{R}|}{\sigma_{\widehat{R}}} = \frac{|\rho_{\widehat{R}\bar{x}}\sigma_{\bar{x}}|}{\bar{x}}$$

Now since $|\rho_{\widehat{R}\bar{x}}| \leq 1$:

$$\frac{|\text{Bias in~}\widehat{R}|}{\sigma_{\widehat{R}}} \leq \frac{\sigma_{\bar{x}}}{\bar{x}}\  \Longrightarrow \ \frac{|\text{Bias in~}\widehat{R}|}{\sigma_{\widehat{R}}} \leq C.V.(\bar{x})$$

**Theorem:** If $E(y/x) = \beta x$ for all values of $x$ in a finite
population then ratio estimator is unbiased.

*Proof:* Since the relationship between $y_{i}$ and $x_{i}$ is linear
and the line of regression passes through origin then
$Y_{i} = \beta X_{i} + e_{i}$ here $\alpha = 0$.

Summing over all values of population units and divide by $N$:

$$\frac{1}{N}\sum_{}^{}\ Y_{i} = \beta\frac{\sum_{}^{}\ X_{i}}{N} + \frac{\sum_{}^{}\ e_{i}}{N}$$

$$\  \Longrightarrow \ \bar{Y} = \beta\bar{X} + 0$$

$$\beta = \frac{\bar{Y}}{\bar{X}} = R$$

Averaging over sample units: $\bar{y} = \beta\bar{x} + \bar{e}$.

$$\frac{\bar{y}}{\bar{x}} = \beta + \frac{\bar{e}}{\bar{x}}\  \Longrightarrow \ \widehat{R} = \beta + \frac{\bar{e}}{\bar{x}}$$

$$E(\widehat{R}) = E\left( \frac{\bar{y}}{\bar{x}} \right) = E\left( \beta + \frac{\bar{e}}{\bar{x}} \right) = \beta + E\left( \frac{\bar{e}}{\bar{x}} \right)$$

Since $\bar{x}$ can be hold constant for some set of value of $x_{i}$:

$$E(\widehat{R}) = \beta + \frac{1}{\bar{x}}E(\bar{e}) = \beta + 0 = \beta$$

From above we have $\beta = R$:

$$E(\widehat{R}) = \beta = R$$

Ratio estimator $\widehat{R} = \frac{\bar{y}}{\bar{x}}$ is unbiased
estimator of $R$.

**Regression Estimators**

Like ratio estimators, regression estimators are used to increase the
precision by making use of auxiliary variable and are used when the
relationship between $Y_{i}$ and $X_{i}$ is linear but does not pass
through origin.

The regression estimators are in general more precise than ratio
estimators and SRS particularly when the line of regression of $Y$ on
$X$ does not pass through origin.

Regression estimator of population mean:\
$${\bar{y}}_{lr} = \bar{y} + b_{0}(\bar{X} - \bar{x})$$
where $b_{0}$ is the estimate of regression coefficient of $y$ on $x$.

> **Case I:** when $b_{0} = 0$. then\
> ${\bar{y}}_{lr} = \bar{y}$ which is an estimator of population mean in
> SRS.\
> $\  \Longrightarrow \ $ SRS is a particular case of Regression
> estimator when $b_{0} = 0$.
>
> **Case-II:** when $b_{0} = \bar{y}/\bar{x}$\
> ${\bar{y}}_{lr} = \bar{y} - \frac{\bar{y}}{\bar{x}}(\bar{x} - \bar{X})$
> *(Note: Typo in handwritten notes corrected to standard form)*\
> $${\bar{y}}_{lr} = \bar{y} - \bar{y} + \frac{\bar{y}}{\bar{x}}\bar{X} = {\widehat{\bar{Y}}}_{R}$$
> Here ratio estimator is a particular case of regression estimator when
> $b_{0} = \bar{y}/\bar{x}$.\
> Like ratio estimator, regression estimators are biased but for large
> sample they are approximately unbiased.

**Regression Estimation:** when value of $b_{0}$ is pre-assigned then
show that regression estimator are unbiased and
$V({\bar{y}}_{lr}) = \frac{1 - f}{n}\lbrack S_{y}^{2} - 2b_{0}S_{xy} + b_{0}^{2}S_{x}^{2}\rbrack$.\
*Proof:* when $b_{0} = \text{constant}$ then\
$${{\bar{y}}_{lr} = \bar{y} - b_{0}(\bar{x} - \bar{X})\  \Longrightarrow \ E({\bar{y}}_{lr}) = E(\bar{y}) - b_{0}E(\bar{x} - \bar{X})
}{= \bar{Y} - b_{0}(E\lbrack\bar{x}\rbrack - \bar{X}) = \bar{Y} - b_{0}(\bar{X} - \bar{X})
}$$$= \bar{Y}$.\
$\  \Longrightarrow \ {\bar{y}}_{lr}$ is unbiased.

$${V({\bar{y}}_{lr}) = E({\bar{y}}_{lr} - \bar{Y})^{2} = E\lbrack\bar{y} - b_{0}(\bar{x} - \bar{X}) - \bar{Y}\rbrack^{2}
}{= E\lbrack(\bar{y} - \bar{Y}) - b_{0}(\bar{x} - \bar{X})\rbrack^{2}}$$

Let $d_{i} = (y_{i} - \bar{Y}) - b_{0}(x_{i} - \bar{X})$\
$$\bar{d} = (\bar{y} - \bar{Y}) - b_{0}(\bar{x} - \bar{X})$$
$\bar{D} = (\bar{Y} - \bar{Y}) - b_{0}(\bar{X} - \bar{X}) = 0$.\
$${V(\bar{d}) = E(\bar{d} - \bar{D})^{2} = E(\bar{d})^{2}
}{= E\lbrack(\bar{y} - \bar{Y}) - b_{0}(\bar{x} - \bar{X})\rbrack^{2}
}$$$\therefore V({\bar{y}}_{lr}) = V(\bar{d})$.\
Now in SRSWOR $V(\bar{y}) = \frac{N - n}{N} \cdot \frac{S^{2}}{n}$.\
$V(\bar{d}) = \frac{N - n}{N} \cdot \frac{S_{d}^{2}}{n}$.\
$${\therefore V({\bar{y}}_{lr}) = \frac{N - n}{Nn} \cdot \frac{1}{N - 1}\sum_{i = 1}^{N}\mspace{2mu}(d_{i} - \bar{D})^{2}
}{= \frac{N - n}{Nn} \cdot \frac{1}{N - 1}\sum_{i = 1}^{N}\mspace{2mu} d_{i}^{2}
}{= \frac{N - n}{Nn} \cdot \frac{1}{N - 1}\sum_{i = 1}^{N}\mspace{2mu}\lbrack(Y_{i} - \bar{Y}) - b_{0}(X_{i} - \bar{X})\rbrack^{2}
}{= \frac{N - n}{Nn} \cdot \frac{1}{N - 1}\lbrack\sum(Y_{i} - \bar{Y})^{2} + b_{0}^{2}\sum(X_{i} - \bar{X})^{2} - 2b_{0}\sum(X_{i} - \bar{X})(Y_{i} - \bar{Y})\rbrack
}$$$= \frac{N - n}{Nn} \cdot \lbrack S_{y}^{2} + b_{0}^{2}S_{x}^{2} - 2b_{0}S_{xy}\rbrack$.

**Theorem:** If the value of
$b_{0} = B_{0} = \frac{\sum_{i = 1}^{N}\mspace{2mu}(X_{i} - \bar{X})(Y_{i} - \bar{Y})}{\sum(X_{i} - \bar{X})^{2}} = \frac{S_{xy}}{S_{x}^{2}}$
then $V({\bar{y}}_{lr})$ is minimum. and the minimum variance will be
$\frac{1 - f}{n} \cdot S_{y}^{2}(1 - \rho^{2})$.\
*Proof:*\
Let $b_{0} = B_{0} + d$ and we want to show that $V({\bar{y}}_{lr})$ is
minimum when $d = 0$.\
We know that\
$$V({\bar{y}}_{lr}) = \frac{1 - f}{n}\lbrack S_{y}^{2} + b_{0}^{2}S_{x}^{2} - 2b_{0}S_{xy}\rbrack$$
Put $b_{0} = \frac{S_{xy}}{S_{x}^{2}} + d$\
$${V({\bar{y}}_{lr}) = \frac{1 - f}{n}\left\lbrack S_{y}^{2} - 2\left( \frac{S_{xy}}{S_{x}^{2}} + d \right)S_{xy} + \left( \frac{S_{xy}}{S_{x}^{2}} + d \right)^{2}S_{x}^{2} \right\rbrack
}{V({\bar{y}}_{lr}) = \frac{1 - f}{n}\left\lbrack S_{y}^{2} - 2\frac{S_{xy}^{2}}{S_{x}^{2}} - 2dS_{xy} + \left( \frac{S_{xy}^{2}}{S_{x}^{4}} + d^{2} + 2d\frac{S_{xy}}{S_{x}^{2}} \right)S_{x}^{2} \right\rbrack
}{= \frac{1 - f}{n}\left\lbrack S_{y}^{2} - 2\frac{S_{xy}^{2}}{S_{x}^{2}} - 2dS_{xy} + \frac{S_{xy}^{2}}{S_{x}^{2}} + d^{2}S_{x}^{2} + 2dS_{xy} \right\rbrack
}$$$= \frac{1 - f}{n}\left\lbrack S_{y}^{2} - \frac{S_{xy}^{2}}{S_{x}^{2}} + d^{2}S_{x}^{2} \right\rbrack$
\-\-- (1)\
$V({\bar{y}}_{lr})$ is minimum when
$d^{2}S_{x}^{2} = 0\  \Longrightarrow \ d = 0$.\
$V({\bar{y}}_{lr})$ has minimum variance when $d = 0$ i.e.
$b_{0} = B_{0} = \frac{S_{xy}}{S_{x}^{2}}$.\
Now putting the value of $d = 0$ in (1):\
$$V({\bar{y}}_{lr}) = \frac{1 - f}{n}\left\lbrack S_{y}^{2} - \frac{S_{xy}^{2}}{S_{x}^{2}} \right\rbrack$$
$S_{xy} = \rho S_{x}S_{y}\  \Longrightarrow \ S_{xy}^{2} = \rho^{2}S_{x}^{2}S_{y}^{2}$.\
$$= \frac{1 - f}{n}\left\lbrack S_{y}^{2} - \frac{\rho^{2}S_{x}^{2}S_{y}^{2}}{S_{x}^{2}} \right\rbrack$$
$= \frac{1 - f}{n}\lbrack S_{y}^{2}(1 - \rho^{2})\rbrack$.

**Comparisons of SRS, Ratio and Regression Estimators.**\
SRS: $V(\bar{y}) = \frac{1 - f}{n}S_{y}^{2}$ \-\-- (1)\
$V({\widehat{\bar{Y}}}_{R}) = \frac{1 - f}{n}\lbrack S_{y}^{2} + R^{2}S_{x}^{2} - 2R\rho S_{x}S_{y}\rbrack$
\-\-- (2)\
$V({\bar{y}}_{lr}) = \frac{1 - f}{n}\lbrack S_{y}^{2} + b_{0}^{2}S_{x}^{2} - 2b_{0}S_{xy}\rbrack = \frac{1 - f}{n}\lbrack S_{y}^{2}(1 - \rho^{2})\rbrack$
\-\-- (3)

From (1) and (3), since $\rho^{2} \leq 1$:\
$\therefore V({\bar{y}}_{lr}) \leq V(\bar{y})$.\
Hence regression estimator are more efficient than SRS except when
$\rho = 0$ i.e. there is no correlation between $y$ and $x$.

From (1) and (2):\
$${V({\widehat{\bar{Y}}}_{R}) \leq V(\bar{y})
}{\frac{1 - f}{n}\lbrack S_{y}^{2} + R^{2}S_{x}^{2} - 2R\rho S_{x}S_{y}\rbrack \leq \frac{1 - f}{n}S_{y}^{2}
}{R^{2}S_{x}^{2} - 2R\rho S_{x}S_{y} \leq 0\  \Longrightarrow \ R^{2}S_{x}^{2} \leq 2R\rho S_{x}S_{y}
}$$$\  \Longrightarrow \ \rho \geq \frac{1}{2}R\frac{S_{x}}{S_{y}}$ or
$\rho \geq \frac{1}{2}\frac{C.V(x)}{C.V(y)}$.\
If the $C.V(x)$ is greater than twice the $C.V(y)$ then SRS will be more
precise but if $\rho > \frac{1}{2}\frac{C.V(x)}{C.V(y)}$ which is a\...

From (2) and (3):\
Regression estimator will be more precise than Ratio estimator if\
$${V({\bar{y}}_{lr}) \leq V({\widehat{\bar{Y}}}_{R})
}{\frac{1 - f}{n}\lbrack S_{y}^{2}(1 - \rho^{2})\rbrack \leq \frac{1 - f}{n}\lbrack S_{y}^{2} + R^{2}S_{x}^{2} - 2R\rho S_{x}S_{y}\rbrack
}{1 - \rho^{2} \leq 1 + R^{2}\frac{S_{x}^{2}}{S_{y}^{2}} - 2R\rho\frac{S_{x}S_{y}}{S_{y}^{2}}
}{R^{2}\frac{S_{x}^{2}}{S_{y}^{2}} - 2R\rho\frac{S_{x}}{S_{y}} + \rho^{2} \geq 0
}{\  \Longrightarrow \ \left( R\frac{S_{x}}{S_{y}} - \rho \right)^{2} \geq 0
}$$Which is true. except when $R\frac{S_{x}}{S_{y}} = \rho$.\
$\rho = R\frac{S_{x}}{S_{y}} = \frac{C_{x}}{C_{y}}$ which hold true when
line of regression passes through the origin.\
Hence when line of regression passes through origin then ratio and
regression estimator are equally precise. Otherwise, regression
estimator is more precise.

**Role of Auxiliary information in sampling:**

Auxiliary variable: For studying a variable $Y$, we collect data for
each unit in sample for variable $X$. This variable is called auxiliary,
additional or supplementary variable.\
Criterion for selecting auxiliary variable:

1.  It should be cheap, and easy to collect readily available.

2.  It should be highly correlated with the variable under study.

3.  The population size i.e. $\sum_{i = 1}^{N}\mspace{2mu} X_{i} = X$
    should be known.

Use of auxiliary variable in different stages.

1.  Primary Stage: In stratified sampling auxiliary variable is used to
    make strata to improve estimator.

2.  Selection Stage: In PPS sampling units are selected with probability
    proportional to size i.e. $p_{i} = \frac{X_{i}}{X}$. Hence auxiliary
    variables are used at selection stage.

3.  At Estimation stage: In ratio and regression estimator method of
    estimation, auxiliary variable $x$ is used out to improve the
    estimator by using modified estimator like ratio estimator of $Y$
    i.e. ${\bar{y}}_{R} = \frac{\bar{y}}{\bar{x}}\bar{X}$ and Regression
    estimator of $Y$ i.e.
    ${\bar{y}}_{lr} = \bar{y} - b_{0}(\bar{x} - \bar{X})$. Although
    samples are selected by SRS or other sampling schemes but auxiliary
    variable are used to improve the estimator at estimation stage.

**Product Method of Estimation**

In ratio method of estimation:

$${\widehat{\bar{y}}}_{R} = \frac{\bar{y}}{\bar{x}}\bar{X}\ and\ \ {\widehat{Y}}_{R} = N \cdot {\widehat{\bar{y}}}_{R} = N\frac{\bar{y}}{\bar{x}}\bar{X} = \frac{\widehat{Y}}{\widehat{X}}X$$

These are called ratio estimator because they use the ratios of two
variables $x$ and $y$. Ratio estimators are more precise than SRS when
$\rho > \frac{1}{2}\frac{C.V(x)}{C.V(y)}$ i.e. when correlation between
$x$ and $y$ is +ve and if when correlation between $x$ and $y$ is -ve
then ratio estimator are less precise than SRS.

In the situation when there is a -ve correlation between $x$ and $y$
instead of using ratio method of estimation we use product method of
estimation.

Product estimator of population total
$= {\widehat{Y}}_{p} = \frac{\widehat{X}\widehat{Y}}{X}$.

Since we are using the product of two estimators for estimation of
population total hence it is called product method of estimation.
Product Method of estimation is more precise when
$\rho < - \frac{1}{2}\frac{C.V(x)}{C.V(y)}$.

**Limits of Bias in Product Estimators:**\
Let

$${\widehat{Y} = Y(1 + e)
}{\widehat{X} = X\left( 1 + e' \right)
}{{\widehat{Y}}_{p} = \frac{\widehat{Y}\widehat{X}}{X} = \frac{Y(1 + e)X\left( 1 + e' \right)}{X} = Y(1 + e)\left( 1 + e' \right)
}{{\widehat{Y}}_{p} = Y\left\lbrack 1 + e' + e + ee' \right\rbrack
}$$Bias $= E\left( {\widehat{Y}}_{p} \right) - Y$

$$E\left( {\widehat{Y}}_{p} \right) = E\left\lbrack Y\left( 1 + e + e' + ee' \right) \right\rbrack$$

$$= Y\left\lbrack 1 + E(e) + E\left( e' \right) + E\left( ee' \right) \right\rbrack$$

$$= Y\lbrack 1 + 0 + 0 + E(ee')\rbrack = Y\lbrack 1 + E(ee')\rbrack\  - - - \ (1)$$
Now $e = \frac{\widehat{Y} - Y}{Y}$ and
$\frac{\widehat{X} - X}{X} = e'$.

$$E\left( ee' \right) = E\left\lbrack \frac{\widehat{Y} - Y}{Y} \cdot \frac{\widehat{X} - X}{X} \right\rbrack = \frac{E\left( \widehat{Y} - Y \right)\left( \widehat{X} - X \right)}{XY} = \frac{Cov\left( \widehat{X},\widehat{Y} \right)}{XY}$$

$$E\left( {\widehat{Y}}_{p} \right) = Y\left\lbrack 1 + \frac{Cov\left( \widehat{X},\widehat{Y} \right)}{XY} \right\rbrack = Y + \frac{Cov\left( \widehat{X},\widehat{Y} \right)}{X}$$

$$\therefore E\left( {\widehat{Y}}_{p} \right) - Y = \frac{Cov\left( \widehat{X},\widehat{Y} \right)}{X}$$

$$Bias({\widehat{Y}}_{p}) = \frac{Cov(\widehat{X},\widehat{Y})}{X} = \frac{\rho_{xy}\sigma_{\widehat{X}}\sigma_{\widehat{Y}}}{X}$$

Limits of Bias:\
Since $\rho \leq 1$.

$$\frac{Bias\text{~of~}{\widehat{Y}}_{p}}{\sigma_{\widehat{Y}}} \leq \frac{\sigma_{\widehat{X}}}{X} = C.V(\widehat{X})$$
When $n$ is very large $C.V(\widehat{X})$ is small then product
estimators are unbiased i.e. bias is negligible.

**Condition under which product estimators are more precise:**\
Since Product Estimators are biased so mean square error is given by its
expected value of $({\widehat{Y}}_{p} - Y)^{2}$.\
$M({\widehat{Y}}_{p}) = E({\widehat{Y}}_{p} - Y)^{2}$.\
Now
${\widehat{Y}}_{p} = \frac{\widehat{X}\widehat{Y}}{X} = \frac{X(1 + e')(1 + e)Y}{X} = Y\lbrack 1 + e + e' + ee'\rbrack$.\
$${M({\widehat{Y}}_{p}) = E\lbrack Y(1 + e + e' + ee') - Y\rbrack^{2} = E\lbrack Y + Y(e + e' + ee') - Y\rbrack^{2}
}{= Y^{2}E\lbrack e + e' + ee'\rbrack^{2}
}{= Y^{2}E\lbrack e^{2} + e^{'2} + e^{'2}e^{2} + 2ee' + 2e^{2}e' + 2e^{'2}e\rbrack
}$$Ignoring higher order terms:\
$${= Y^{2}\lbrack E(e^{2}) + E(e^{'2}) + 2E(ee')\rbrack
}{= Y^{2}\left\lbrack E\left( \frac{\widehat{Y} - Y}{Y} \right)^{2} + E\left( \frac{\widehat{X} - X}{X} \right)^{2} + 2E\left( \frac{\widehat{X} - X}{X}\frac{\widehat{Y} - Y}{Y} \right) \right\rbrack
}{= Y^{2}\left\lbrack \frac{V(\widehat{Y})}{Y^{2}} + \frac{V(\widehat{X})}{X^{2}} + 2\frac{Cov(\widehat{X},\widehat{Y})}{XY} \right\rbrack
}$$$= \left\lbrack V(\widehat{Y}) + R^{2}V(\widehat{X}) + 2RCov(\widehat{X},\widehat{Y}) \right\rbrack$.\
$M({\widehat{Y}}_{p}) = V(\widehat{Y}) + R^{2}V(\widehat{X}) + 2RCov(\widehat{X},\widehat{Y})$.\
If Bias is negligible then
$M({\widehat{Y}}_{p}) = V({\widehat{Y}}_{p})$.

Product Estimator will be more precise than mean per unit if
$V({\widehat{Y}}_{p}) < V(\widehat{Y})$ or\
$${V(\widehat{Y}) + R^{2}V(\widehat{X}) + 2RCov(\widehat{X},\widehat{Y}) < V(\widehat{Y})
}{R^{2}V(\widehat{X}) + 2RCov(\widehat{X},\widehat{Y}) < 0
}{R^{2}V(\widehat{X}) < - 2RCov(\widehat{X},\widehat{Y})
}{\frac{Y}{X}V(\widehat{X}) < - 2Cov(\widehat{X},\widehat{Y})
}{\  \Longrightarrow \ \frac{1}{2}\frac{Y}{X}\sigma_{\widehat{X}}^{2} < - Cov(\widehat{X},\widehat{Y})
}{\frac{1}{2}\frac{Y}{X}\sigma_{\widehat{X}}^{2} < - \rho_{\widehat{X}\widehat{Y}}\sigma_{\widehat{X}}\sigma_{\widehat{Y}}
}{\  \Longrightarrow \ \frac{1}{2}\frac{Y}{X}\frac{\sigma_{\widehat{X}}}{\sigma_{\widehat{Y}}} < - \rho_{\widehat{X}\widehat{Y}}
}{- \rho_{\widehat{X}\widehat{Y}} > \frac{1}{2}\frac{C.V(\widehat{X})}{C.V(\widehat{Y})}
}$$$\rho < - \frac{1}{2}\frac{C.V(\widehat{X})}{C.V(\widehat{Y})}$.

**Systematic Sampling: Properties & Derivations**

**Theorem:** If $N = nk$ then sample mean is unbiased estimator of
population mean, i.e. ${\bar{y}}_{r}$ (mean of $r^{th}$ systematic
sample).\
${\bar{y}}_{r} = \frac{1}{n}\sum_{j = 0}^{n - 1}\mspace{2mu} y_{r + jk} =$
sample mean.\
$E({\bar{y}}_{r}) = E\left\{ \frac{1}{n}\sum_{j = 0}^{n - 1}\mspace{2mu} y_{r + jk} \right\}$.\
We know that in systematic sampling the probability of selection of each
sample from $k$ samples is $\frac{1}{k}$ and each has same probability.\
$\therefore E\lbrack{\bar{y}}_{r}\rbrack = \sum_{r = 1}^{k}\mspace{2mu}\frac{1}{k}{\bar{y}}_{r} = \sum_{r = 1}^{k}\mspace{2mu}\frac{1}{k} \cdot \frac{1}{n}\sum_{j = 0}^{n - 1}\mspace{2mu} y_{r + jk}$.\
$= \frac{1}{nk}\sum_{r = 1}^{k}\mspace{2mu}\sum_{j = 0}^{n - 1}\mspace{2mu} y_{r + jk} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu} Y_{i} = \bar{Y}$.\
$\  \Longrightarrow \ {\bar{y}}_{r}$ is unbiased estimator of $\bar{Y}$.

**Theorem:** In systematic sampling show that
$V({\bar{y}}_{r}) = \frac{\sigma^{2}}{n}\lbrack 1 + (n - 1)\rho_{w}\rbrack$
where $\rho_{w}$ is intra-class correlation coefficient between pairs of
units in systematic sample.\
*Proof:*\
$${V({\bar{y}}_{r}) = \frac{1}{k}\sum_{r = 1}^{k}\mspace{2mu}({\bar{y}}_{r} - \bar{Y})^{2} = \frac{1}{k}\sum_{r = 1}^{k}\mspace{2mu}\left\lbrack \frac{1}{n}\sum_{j = 0}^{n - 1}\mspace{2mu} y_{r + jk} - \bar{Y} \right\rbrack^{2}
}{= \frac{1}{n^{2}k}\sum_{r = 1}^{k}\mspace{2mu}\left\lbrack \sum_{i = 1}^{n}\mspace{2mu}(y_{ri} - \bar{Y}) \right\rbrack^{2}
}{= \frac{1}{n^{2}k}\sum_{r = 1}^{k}\mspace{2mu}\left\lbrack \sum(y_{ri} - \bar{Y})^{2} + \sum_{i \neq j}\mspace{2mu}(y_{ri} - \bar{Y})(y_{rj} - \bar{Y}) \right\rbrack
}{= \frac{1}{n^{2}k}\sum\sum(y_{ri} - \bar{Y})^{2} + \frac{1}{n^{2}k}\sum_{r = 1}^{k}\mspace{2mu}\sum_{i \neq j}\mspace{2mu}(y_{ri} - \bar{Y})(y_{rj} - \bar{Y})
}{= \frac{\sum(Y_{i} - \bar{Y})^{2}}{nN} + \frac{\sum\sum(y_{ri} - \bar{Y})(y_{rj} - \bar{Y})}{nN}
}{= \frac{N\sigma^{2}}{nN} + \frac{\sum\sum(y_{ri} - \bar{Y})(y_{rj} - \bar{Y})}{nN}
}$$$= \frac{\sigma^{2}}{n} + \frac{\sum\sum(y_{ri} - \bar{Y})(y_{rj} - \bar{Y})}{nN}$
\-\-- (1)\
Now we know that
$\rho_{xy} = \frac{Cov(x,y)}{\sigma_{x} \cdot \sigma_{y}}\  \Longrightarrow \ \rho_{xy}\sigma_{x} \cdot \sigma_{y} = Cov(x,y)$.\
$Cov(x,y) = \frac{\sum(X_{i} - \bar{X})(Y_{i} - \bar{Y})}{n - 1}$.\
For intra-class correlation within $k$ samples of size $n$, the sum of
cross products is $N(n - 1)\rho_{w}\sigma^{2}$.\
$\  \Longrightarrow \ N(n - 1)\rho_{w}\sigma^{2} = \sum\sum(y_{ri} - \bar{Y})(y_{rj} - \bar{Y})$.\
Substitute into (1):\
$V({\bar{y}}_{r}) = \frac{\sigma^{2}}{n} + \frac{N(n - 1)\rho_{w}\sigma^{2}}{nN} = \frac{\sigma^{2}}{n} + \frac{(n - 1)\rho_{w}\sigma^{2}}{n} = \frac{\sigma^{2}}{n}\lbrack 1 + (n - 1)\rho_{w}\rbrack$.

**Relative efficiency of Systematic sampling with SRS:**

1.  Comparison with SRSWR:\
    $$V_{1}(\bar{y}) = \frac{\sigma^{2}}{n}$$
    $V_{2}({\bar{y}}_{r}) = \frac{\sigma^{2}}{n}\lbrack 1 + (n - 1)\rho_{w}\rbrack$.\
    $R.E = \frac{\sigma^{2}/n}{\sigma^{2}/n\lbrack 1 + (n - 1)\rho_{w}\rbrack} = \frac{1}{\lbrack 1 + (n - 1)\rho_{w}\rbrack}$.\
    Systematic sampling is more efficient than SRS if its relative
    efficiency is more than 1 i.e.,\
    $V_{1}(\bar{y}) > V_{2}({\bar{y}}_{r})\  \Longrightarrow \ \frac{\sigma^{2}}{n} > \frac{\sigma^{2}}{n}\lbrack 1 + (n - 1)\rho_{w}\rbrack$.\
    $1 > 1 + (n - 1)\rho_{w}\  \Longrightarrow \ (n - 1)\rho_{w} < 0\  \Longrightarrow \ \rho_{w} < 0$.\
    This condition is generally met when units are heterogeneous within
    samples.

2.  Comparison with SRSWOR:\
    Let $V_{1}(\bar{y}) = \frac{N - n}{N - 1}\frac{\sigma^{2}}{n}$.\
    $V_{2}({\bar{y}}_{r}) = \frac{\sigma^{2}}{n}\lbrack 1 + (n - 1)\rho_{w}\rbrack$.\
    Systematic sampling would be more efficient than SRSWOR if
    $V_{1}(\bar{y}) > V_{2}({\bar{y}}_{r})$.\
    $\frac{\sigma^{2}}{n}\left\lbrack \frac{N - n}{N - 1} \right\rbrack > \frac{\sigma^{2}}{n}\lbrack 1 + (n - 1)\rho_{w}\rbrack$.\
    $\frac{N - n}{N - 1} - 1 > (n - 1)\rho_{w}\  \Longrightarrow \ \frac{N - n - N + 1}{N - 1} > (n - 1)\rho_{w}$.\
    $\frac{- (n - 1)}{N - 1} > (n - 1)\rho_{w}\  \Longrightarrow \ \rho_{w} < - \frac{1}{N - 1}$.

**Range of** $\rho_{w}$ **in systematic sampling:**\
We know that
$V({\bar{y}}_{r}) = \frac{\sigma^{2}}{n}\lbrack 1 + (n - 1)\rho_{w}\rbrack$.\
$\rho_{w}$ is intra-class correlation coefficient is less than 1. i.e.
$\rho_{w} \leq 1$.\
Since variance cannot be negative, $V({\bar{y}}_{r}) \geq 0$.\
$\frac{\sigma^{2}}{n}\lbrack 1 + (n - 1)\rho_{w}\rbrack \geq 0\  \Longrightarrow \ 1 + (n - 1)\rho_{w} \geq 0$.\
$(n - 1)\rho_{w} \geq - 1\  \Longrightarrow \ \rho_{w} \geq - \frac{1}{n - 1}$.\
Therefore: $- \frac{1}{n - 1} \leq \rho_{w} \leq 1$.

**Sampling variance of Estimated mean in systematic sampling:**\
$V({\widehat{\bar{Y}}}_{sy}) = V({\bar{y}}_{r})$. ${\bar{y}}_{r}$ is
unbiased estimator of $\bar{Y}$.\
$V({\bar{y}}_{r}) = \frac{1}{k}\sum_{r = 1}^{k}\mspace{2mu}({\bar{y}}_{r} - \bar{Y})^{2} = \sigma_{b}^{2}$
(between sample variance).\
$\sigma^{2} = \text{population variance}$.\
$\sigma^{2} = \frac{1}{N}\sum_{r = 1}^{k}\mspace{2mu}\sum_{i = 1}^{n}\mspace{2mu}(y_{ri} - \bar{Y})^{2} = \frac{1}{N}\sum\sum(y_{ri} - {\bar{y}}_{r} + {\bar{y}}_{r} - \bar{Y})^{2}$.\
$= \frac{1}{N}\sum\sum(y_{ri} - {\bar{y}}_{r})^{2} + \frac{1}{N}\sum\sum({\bar{y}}_{r} - \bar{Y})^{2} + 0\text{~(cross terms)}$.\
Now $N = nk$.\
$= \frac{1}{k}\sum_{r = 1}^{k}\mspace{2mu}\left\lbrack \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}(y_{ri} - {\bar{y}}_{r})^{2} \right\rbrack + \frac{n}{nk}\sum_{r = 1}^{k}\mspace{2mu}({\bar{y}}_{r} - \bar{Y})^{2}$.\
$= \frac{1}{k}\sum_{r = 1}^{k}\mspace{2mu}\sigma_{wr}^{2} + \frac{1}{k}\sum_{r = 1}^{k}\mspace{2mu}({\bar{y}}_{r} - \bar{Y})^{2}$.\
$= \sigma_{w}^{2} + \sigma_{b}^{2}$.\
Where $\sigma_{w}^{2}$ is within sample variance, and $\sigma_{b}^{2}$
is between sample variance.\
Variance of systematic sampling:
$V({\bar{y}}_{r}) = \sigma_{b}^{2} = \sigma^{2} - \sigma_{w}^{2}$.

Note: Systematic sampling will be more precise if the units in the
systematic samples are heterogeneous (wide spread). i.e. It is more
precise if $\sigma_{b}^{2}$ is small i.e., $V({\bar{y}}_{r})$ should be
minimum and for fixed $\sigma^{2}$, $\sigma_{w}^{2}$ is maximum. Since a
systematic sample of size $n$ is selected systematically from a
population of $k^{n}$ groups i.e. one element from each group. Therefore
for systematic sample to be heterogeneous the $n$ groups into which pop
is divided should be homogeneous.

**Estimation of** $V(\widehat{Y})$ **in systematic sampling:**\
$V(\widehat{Y}) = E({\widehat{Y}}^{2}) - \lbrack E(\widehat{Y})\rbrack^{2}$.\
$V(\widehat{Y}) = {\widehat{Y}}^{2} - Est\lbrack Y^{2}\rbrack$ \-\--
(1)\
Now
$Y^{2} = (\sum Y_{i})^{2} = \sum_{i = 1}^{N}\mspace{2mu} Y_{i}^{2} + \sum_{i \neq j}\mspace{2mu} Y_{i}Y_{j}$.\
Substituting in (1) we get:\
$V(\widehat{Y}) = {\widehat{Y}}^{2} - Est(\sum Y_{i}^{2}) - Est(\sum\sum Y_{i}Y_{j})$.\
$\sum_{i = 1}^{N}\mspace{2mu} Y_{i}^{2}$ can be estimated unbiasedly by
$\frac{N}{n}\sum y_{i}^{2}$.\
But we cannot estimate $\sum_{i \neq j}^{N}\mspace{2mu} Y_{i}Y_{j}$ as
no two consecutive units can occur in the same sample.\
Hence we cannot find unbiased estimator of the variance of the estimated
population total.

**Circular Systematic Sampling:**\
In linear systematic sampling the main drawback is the observed sample
size differ from required sample size when $N \neq nk$. Hence sample
mean is not unbiased for population mean. To overcome this drawback we
use circular systematic sampling given by D.B. Lahiri (1952).\
Steps:

1.  Select a random start $r$ from $1$ to $N$ instead of $1$ to $k$.

2.  Select every $k^{th}$ unit in the circular order so as to complete
    the sample of size $n$.\
    Sample units selected are:\
    $u_{r + jk}$ if $r + jk \leq N$\
    $u_{r + jk - N}$ if $r + jk > N$, where $j = 0,1,\ldots,n - 1$.

Example: Let $N = 18,n = 5$. $k = \frac{18}{5} \approx 4$.\
If $r = 1$: units are 1, 5, 9, 13, 17.\
If $r = 2$: units are 2, 6, 10, 14, 18.\
If $r = 3$: units are 3, 7, 11, 15, 1.\
If $r = 4$: units are 4, 8, 12, 16, 2.

**Theorem on circular systematic sampling:** Sample mean is unbiased
estimator of Population mean.\
$E({\bar{y}}_{r}) = \frac{1}{N}\sum_{r = 1}^{N}\mspace{2mu}{\bar{y}}_{r} = \frac{1}{N}\sum_{r = 1}^{N}\mspace{2mu}\left( \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu} y_{ri} \right)$.\
Since each population unit occurs exactly $n$ times in the $N$ possible
samples:\
$= \frac{1}{N}\frac{n \cdot Y}{n} = \frac{Y}{N} = \bar{Y}$.\
Hence in circular systematic sampling even if $N \neq nk$ we observed
that observed sample size $n' = n$ and sample mean is unbiased estimator
of pop mean.

**Systematic sampling from a pop with periodic variation:**\
In many situation the population has got periodic variation.

1.  If family members are arranged according to their age: Father,
    Mother, Children\...

2.  In industrial production the machine may become loose with time and
    cycles are generated or cycles are generated due to temp.\
    In systematic sampling with periodic variation its efficiency
    depends upon the sampling interval, length of variation.\
    $V({\bar{y}}_{r}) = \sigma_{b}^{2} = \sigma^{2} - \sigma_{w}^{2}$.\
    *Case I:* When the sampling intervals are equal or multiple of
    period of cyclic variation, so all the units of sample are
    homogeneous. Hence $\sigma_{w}^{2}$ is small and then
    $\sigma_{b}^{2} = \sigma^{2} - \sigma_{w}^{2}$ will be large. Low
    precision.\
    *Case II:* When sampling intervals are not equal or is odd multiples
    of half of the period of cycles. Then sample units are heterogeneous
    and hence $\sigma_{w}^{2}$ is large and $\sigma_{b}^{2}$ will be
    small and precision will be more.\
    So for higher precision in systematic sampling with periodic
    variation the sampling interval is odd multiple of half of the
    period of cycles.

**Systematic Sampling from a pop with linear trends:**\
When pop has linear trend:
$Y_{t} = a + bt\  \Longrightarrow \ \sum Y_{t} = Na + b\sum t$.\
Pop Mean
$= \bar{Y} = \frac{\sum Y_{t}}{N} = a + \frac{b}{N}\sum_{t = 1}^{N}\mspace{2mu} t = a + \frac{b}{N}\frac{N(N + 1)}{2} = a + \frac{b(N + 1)}{2}$.\
Population variance
$\sigma^{2} = \frac{1}{N}\sum_{t = 1}^{N}\mspace{2mu}(Y_{t} - \bar{Y})^{2} = \frac{1}{N}\sum\left( a + bt - a - \frac{b(N + 1)}{2} \right)^{2}$\
$${= \frac{b^{2}}{N}\sum\left( t - \frac{N + 1}{2} \right)^{2} = \frac{b^{2}}{N}\sum\left\lbrack t^{2} + \frac{(N + 1)^{2}}{4} - t(N + 1) \right\rbrack
}{= \frac{b^{2}}{N}\left\lbrack \frac{N(N + 1)(2N + 1)}{6} + N\frac{(N + 1)^{2}}{4} - \frac{N(N + 1)}{2}(N + 1) \right\rbrack
}{= b^{2}(N + 1)\left\lbrack \frac{2N + 1}{6} + \frac{N + 1}{4} - \frac{N + 1}{2} \right\rbrack
}{= b^{2}(N + 1)\left\lbrack \frac{4N + 2 + 3N + 3 - 6N - 6}{12} \right\rbrack = b^{2}(N + 1)\left\lbrack \frac{N - 1}{12} \right\rbrack
}$$$\sigma^{2} = \frac{b^{2}}{12}(N^{2} - 1)$.

*Case I:* When $n$ units are selected by SRSWR.\
$V_{1}(\bar{y}) = \frac{\sigma^{2}}{n} = \frac{b^{2}}{12n}(N^{2} - 1)$.

*Case II:* When $n$ units are selected by SRSWOR.\
$V_{2}(\bar{y}) = \frac{N - n}{N - 1}\frac{\sigma^{2}}{n} = \frac{N - n}{N - 1}\frac{b^{2}}{12n}(N + 1)(N - 1) = \frac{b^{2}}{12n}(N - n)(N + 1)$.\
$V_{2}(\bar{y}) = \frac{b^{2}}{12}(N + 1)\left\lbrack \frac{N}{n} - 1 \right\rbrack = \frac{b^{2}}{12}(N + 1)\lbrack k - 1\rbrack$.\
We can see $V_{2}(\bar{y}) < V_{1}(\bar{y})$.

*Case III:* When units are selected by systematic sampling.\
$$V({\bar{y}}_{r}) = \frac{1}{k}\sum_{r = 1}^{k}\mspace{2mu}({\bar{y}}_{r} - \bar{Y})^{2}$$
where
${\bar{y}}_{r} = \frac{1}{n}\sum_{j = 0}^{n - 1}\mspace{2mu} y_{r + jk} = \frac{1}{n}\sum_{j = 0}^{n - 1}\mspace{2mu}(a + b(r + jk))$\
$= \frac{1}{n}\left\lbrack na + nbr + bk\frac{(n - 1)n}{2} \right\rbrack = a + br + \frac{bk(n - 1)}{2}$.\
$V({\bar{y}}_{r}) = \frac{1}{k}\sum_{r = 1}^{k}\mspace{2mu}\left( a + br + \frac{bk(n - 1)}{2} - a - \frac{b(N + 1)}{2} \right)^{2}$.\
Substitute $N = nk$:\
$= \frac{b^{2}}{k}\sum_{r = 1}^{k}\mspace{2mu}\left( r + \frac{kn - k}{2} - \frac{nk + 1}{2} \right)^{2} = \frac{b^{2}}{k}\sum_{r = 1}^{k}\mspace{2mu}\left( r - \frac{k + 1}{2} \right)^{2}$.\
$= \frac{b^{2}}{k}\sum\left\lbrack r^{2} + \frac{(k + 1)^{2}}{4} - r(k + 1) \right\rbrack$.\
Similar to the derivation for $\sigma^{2}$ above, replacing $N$ with
$k$:\
$= \frac{b^{2}}{12}(k^{2} - 1)$.

Comparing the variances:\
$V_{sys} = \frac{b^{2}}{12}(k^{2} - 1) = \frac{b^{2}}{12}(k + 1)(k - 1)$.\
$V_{SRSWOR} = \frac{b^{2}}{12}(N + 1)(k - 1) = \frac{b^{2}}{12}(nk + 1)(k - 1)$.\
Therefore $V_{1}(\bar{y}) > V_{2}(\bar{y}) > V({\bar{y}}_{r})$.\
And for large $n$, they are in ratio $\approx n:n:1$.\
The variance of systematic sampling is $\frac{1}{n}$ times.\
Systematic sampling is $n$ times more efficient than SRS when there is a
linear trend in the population.

**Cluster Sampling**

In cluster sampling population is divided into a number of clusters
i.e., nearby units form a cluster. The clusters are homogeneous in
themselves and heterogeneous from each other.\
A sample of cluster is selected using SRS or any other sampling scheme
and all the units of the cluster are studied.

e.g. family may be considered as a cluster of persons. Wards may be
considered as a cluster of houses.\
Clusters may be:

1.  Naturally formed: are of unequal sizes.

2.  Artificially formed: generally of equal sizes.

This sampling is very cheap and less time consuming because we have to
approach lesser no. of locations to complete the sample size as compared
to SRS.

Since it is not well spread over whole population, hence it is less
efficient than SRS. The efficiency of cluster sampling increases with
the decrease in cluster size.

**Cluster of Equal sizes:**\
Let us suppose that we have $N$ clusters in population of size $M$.\
Let $Y_{ij}$ be the value of $j^{th}$ unit in $i^{th}$ cluster.

$$\bar{Y} = \frac{1}{NM}\sum_{i = 1}^{N}\mspace{2mu}\sum_{j = 1}^{M}\mspace{2mu} Y_{ij} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu}{\bar{Y}}_{i}$$
where ${\bar{Y}}_{i} = \frac{1}{M}\sum_{j = 1}^{M}\mspace{2mu} Y_{ij}$
is the $i^{th}$ cluster mean.\
$$V(\bar{Y}) = \frac{\sigma^{2}}{M} = \frac{1}{NM^{2}}\sum_{i = 1}^{N}\mspace{2mu}\sum_{j = 1}^{M}\mspace{2mu}(Y_{ij} - \bar{Y})^{2}$$

*(Note: this represents population variance structure)*.

**Case-I: only one cluster is selected**\
**Theorem:** show that cluster mean ${\bar{y}}_{i}$ is unbiased
estimator of population mean.\
*Proof:*

$$E\left( {\bar{y}}_{i} \right) = E\left\lbrack \frac{1}{M}\sum_{j = 1}^{M}\mspace{2mu}\mspace{2mu} y_{ij} \right\rbrack = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu}{\bar{Y}}_{i} = \frac{1}{NM}\sum_{}^{}\ \sum_{}^{}\ Y_{ij} = \bar{Y}$$

$$V({\bar{y}}_{i}) = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu}({\bar{y}}_{i} - \bar{Y})^{2} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu}\left( \frac{1}{M}\sum_{j = 1}^{M}\mspace{2mu} Y_{ij} - \bar{Y} \right)^{2}$$

$$= \frac{1}{NM^{2}}\sum_{i = 1}^{N}\left( \sum_{j = 1}^{M}\left( Y_{ij} - \overline{Y} \right) \right)^{2}$$

$$= \frac{1}{NM^{2}}\sum_{i = 1}^{N}\left\lbrack \sum_{j = 1}^{M}{\left( Y_{ij} - \overline{Y} \right)^{2} + \sum_{j \neq k}^{}{\left( Y_{ij} - \overline{Y} \right)\left( Y_{ik} - \overline{Y} \right)}} \right\rbrack$$

$$= \frac{1}{NM^{2}}\sum\sum(Y_{ij} - \bar{Y})^{2} + \frac{1}{NM^{2}}\sum_{i = 1}^{N}\mspace{2mu}\sum_{j \neq k}\mspace{2mu}(Y_{ij} - \bar{Y})(Y_{ik} - \bar{Y})$$

$$= \frac{\sigma^{2}}{M} + \frac{M(M - 1)\rho_{c}\sigma^{2}}{M^{2}}$$

$$= \frac{\sigma^{2}}{M} + \frac{(M - 1)\rho_{c}\sigma^{2}}{M} = \frac{\sigma^{2}}{M}\lbrack 1 + (M - 1)\rho_{c}\rbrack$$
Where

$$\rho_{c} = \frac{Cov(Y_{ij},Y_{ik})}{\sigma^{2}} = \frac{\sum\sum_{j \neq k}\mspace{2mu}(Y_{ij} - \bar{Y})(Y_{ik} - \bar{Y})}{NM(M - 1)\sigma^{2}}$$

**Case-II: when** $M$ **units are selected out of** $NM$ **units by
SRSWR**\
$$V_{1}(\bar{y}) = \frac{\sigma^{2}}{M}$$

**Relative efficiency of cluster sampling w.r.t. SRS**\
$$R.E. = \frac{\sigma^{2}/M}{\frac{\sigma^{2}}{M}\lbrack 1 + (M - 1)\rho_{c}\rbrack} = \frac{1}{1 + (M - 1)\rho_{c}}$$

Cluster sampling is more efficient than SRS if:\
$$V_{1}\left( \bar{y} \right) > V_{2}\left( {\bar{y}}_{i} \right)$$

$$\frac{\sigma^{2}}{M} > \frac{\sigma^{2}}{M}\lbrack 1 + (M - 1)\rho_{c}\rbrack\  \Longrightarrow \ 1 > 1 + (M - 1)\rho_{c}$$

$$\Longrightarrow \ (M - 1)\rho_{c} < 0\  \Longrightarrow \ \rho_{c} < 0$$

This condition usually not be met as nearby elements form the cluster.
Hence $\rho_{c} > 0$ in general.\
Cluster sampling in general is not more efficient than SRS.

**Range of** $\rho_{c}$: We know that $\rho_{c}$ is the correlation
coefficient hence $\rho_{c} \leq 1$. Also

$$V\left( {\bar{y}}_{i} \right) = \frac{\sigma^{2}}{M}\left\lbrack 1 + (M - 1)\rho_{c} \right\rbrack$$
As variance is +ve:\
$$\frac{\sigma^{2}}{M}\left\lbrack 1 + (M - 1)\rho_{c} \right\rbrack \geq 0\ $$

$$\Longrightarrow \ 1 + (M - 1)\rho_{c} \geq 0$$

$$\Longrightarrow \ (M - 1)\rho_{c} \geq - 1\  \Longrightarrow \ \rho_{c} \geq - \frac{1}{M - 1}$$
Range of $\rho_{c}$ is:\
$$- \frac{1}{M - 1} \leq \rho_{c} \leq 1$$

**Case-III: when** $n$ **clusters are selected out of** $N$**.**

$${\bar{y}}_{i} = \frac{1}{M}\sum_{j = 1}^{M}\mspace{2mu} y_{ij}$$
If $n$ clusters are sampled the sample mean:\
$${\bar{\bar{y}}}_{c} = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}{\bar{y}}_{i}$$

Sample mean is unbiased estimator of pop mean.\
$$E({\bar{\bar{y}}}_{c}) = E\left\lbrack \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}{\bar{y}}_{i} \right\rbrack = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu} E({\bar{y}}_{i}) = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\bar{Y} = \frac{n\bar{Y}}{n} = \bar{Y}
{\bar{\bar{y}}}_{c} = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}{\bar{y}}_{i}$$
is unbiased estimator.

Variance of the estimator:\
$$V({\bar{\bar{y}}}_{c}) = V\left( \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}{\bar{y}}_{i} \right) = \frac{1}{n^{2}}\sum_{i = 1}^{n}\mspace{2mu} V({\bar{y}}_{i}) = \frac{1}{n^{2}}\sum_{i = 1}^{n}\mspace{2mu}\sigma_{b}^{2} = \frac{n\sigma_{b}^{2}}{n^{2}} = \frac{\sigma_{b}^{2}}{n}$$

Selection of $n$ cluster means $nM$ units are selected out of $NM$
units.\
If $nM$ units are selected out of $NM$ units by SRSWR:\
$$V'(\bar{y}) = \frac{\sigma^{2}}{nM}$$

Relative efficiency of cluster sampling when $n$ clusters are selected:\
$$R.E. = \frac{\sigma^{2}/nM}{\sigma_{b}^{2}/n} = \frac{\sigma^{2}/M}{\sigma_{b}^{2}} = \frac{\sigma^{2}/M}{\frac{\sigma^{2}}{M}\lbrack 1 + (M - 1)\rho_{c}\rbrack} = \frac{1}{1 + (M - 1)\rho_{c}}$$

**Case-IV: when** $n$ **clusters are selected by SRSWOR**

$$V_{1}({\bar{\bar{y}}}_{c}) = \frac{N - n}{N - 1} \cdot \frac{\sigma_{b}^{2}}{n}$$
And if $nM$ units are selected out of $NM$ units by SRSWOR:

$$V''\left( \bar{y} \right) = \frac{NM - nM}{NM - 1} \cdot \frac{\sigma^{2}}{nM} = \frac{M(N - n)}{NM - 1} \cdot \frac{\sigma^{2}}{nM}$$

$$R.E. = \frac{M(N - n)}{NM - 1} \cdot \frac{\frac{\sigma^{2}}{nM}}{\left\lbrack \frac{N - n}{N - 1} \cdot \frac{\sigma_{b}^{2}}{n} \right\rbrack}$$

$$= \frac{N - 1}{NM - 1} \cdot \frac{\frac{\sigma^{2}}{M}}{\sigma_{b}^{2}} = \frac{N - 1}{NM - 1} \cdot \frac{\frac{\sigma^{2}}{M}}{\frac{\sigma^{2}}{M}\left\lbrack 1 + (M - 1)\rho_{c} \right\rbrack}$$

$$= \frac{N - 1}{NM - 1} \times \frac{1}{1 + (M - 1)\rho_{c}}$$

Since $\frac{N - 1}{NM - 1} < 1$, relative efficiency of cluster
sampling when $n$ clusters are sampled by SRSWOR is higher as compared
to the case when they are sampled by SRSWR.

**Cost function of cluster sampling**\
Let $c_{0}$ be the overhead cost., $c_{1}$ be the cost of survey of one
cluster of size $M$ and $c_{2}$ be the cost per unit of survey. Then the
cost function $C$ is given by

$$C = c_{0} + nc_{1} + nMc_{2}$$
If various costs are given then

$$C - c_{0} = n(c_{1} + Mc_{2})\  \Longrightarrow \ n = \frac{C - c_{0}}{c_{1} + Mc_{2}}$$
gives the no. of cluster that can be studied when various costs are
given.

**Optimum Number of clusters**\
In cluster sampling for fixed sample size, as the number of cluster
increases precision of cluster sampling increases. On the other hand if
cluster size increases the cost also increases.\
The optimum cluster size is one which:

1.  Minimize variance for a fixed cost.

2.  Minimize costs for fixed precision or variance.

In general if $n$ clusters are sampled out of $N$ then:\
$$V({\bar{\bar{y}}}_{c}) = \frac{N - n}{N - 1} \cdot \frac{\sigma_{b}^{2}}{n}$$

where

$$\sigma_{b}^{2} = \frac{\sigma^{2}}{M}\lbrack 1 + (M - 1)\rho_{c}\rbrack$$
And when $N$ is large as compared to $n$:\
Then

$$V({\bar{\bar{y}}}_{c}) \approx \frac{\sigma_{b}^{2}}{n} = \frac{\sigma^{2}}{nM}\lbrack 1 + (M - 1)\rho_{c}\rbrack$$
Substitute the value

$$n = \frac{C - c_{0}}{c_{1} + Mc_{2}}$$

$$V({\bar{\bar{y}}}_{c}) = \frac{\sigma^{2}}{M}\frac{(c_{1} + Mc_{2})}{C - c_{0}}\lbrack 1 + (M - 1)\rho_{c}\rbrack$$

$$= \frac{c_{1}\sigma^{2}}{C - c_{0}}\left\lbrack 1 + \frac{Mc_{2}}{c_{1}} \right\rbrack\left\lbrack \frac{1 + (M - 1)\rho_{c}}{M} \right\rbrack$$

Plot a graph between $M$ and the expression between square brackets. The
curve attains a minimum value that gives optimum value of $M$ at which
variance is minimum at fixed cost.

**Note:** In cluster sampling: When clusters are selected by SRSWR:

$$V({\bar{\bar{y}}}_{c}) = \frac{\sigma_{b}^{2}}{n}$$

When clusters are selected by SRSWOR:

$$V({\bar{\bar{y}}}_{c}) = \frac{N - n}{N - 1} \cdot \frac{\sigma_{b}^{2}}{n}$$

Where
$\sigma_{b}^{2} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu}({\bar{Y}}_{i} - \bar{Y})^{2}$
(between cluster variance).\
Unbiased estimators:\
$\widehat{V}({\bar{\bar{y}}}_{c}) = \frac{s_{b}^{2}}{n}$ for SRSWR.\
$\widehat{V}({\bar{\bar{y}}}_{c}) = \frac{s_{b}^{2}}{n} \cdot \frac{N - n}{N}$
if clusters are sampled by SRSWOR.\
Where

$$s_{b}^{2} = \frac{1}{n - 1}\sum_{i = 1}^{n}\mspace{2mu}({\bar{y}}_{i} - {\bar{\bar{y}}}_{c})^{2}$$

**Clusters with varying sizes:**

Naturally formed clusters are of unequal sizes e.g. number of children
per family, houses per street, number of flowers per plants and number
of village in a block etc.

Let $M_{1},M_{2},\ldots,M_{N}$ be the sizes of $N$ clusters.\
Let $M' = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu} M_{i}$ be the average
cluster size.\
Let $Y_{ij}$ be the value of $j^{th}$ unit in $i^{th}$ cluster.
$i = 1,2\ldots N$, $j = 1,2\ldots M_{i}$.\
If $n$ clusters are selected out of $N$ by SRSWR or WOR:\
$${\widehat{\bar{Y}}}_{c} = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\frac{M_{i}}{M'}{\bar{y}}_{i}$$

is unbiased estimate of population mean. Hence $M'$ must be known.

And $V({\widehat{\bar{Y}}}_{c}) = \frac{\sigma_{b}^{'2}}{n}$ when
clusters are selected by SRSWR.\
$V({\widehat{\bar{Y}}}_{c}) = \frac{N - n}{N - 1} \cdot \frac{\sigma_{b}^{'2}}{n}$
when clusters are sampled by SRSWOR.\
where

$$\sigma_{b}^{'2} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu}\left( \frac{M_{i}}{M'}{\bar{Y}}_{i} - \bar{Y} \right)^{2}$$

And unbiased estimate of variances are:\
$\widehat{V}({\widehat{\bar{Y}}}_{c}) = \frac{s_{b}^{'2}}{n}$ when
clusters are sampled by SRSWR.\
$\widehat{V}({\widehat{\bar{Y}}}_{c}) = \frac{N - n}{N} \cdot \frac{s_{b}^{'2}}{n}$
when clusters are sampled by SRSWOR.\
where
$s_{b}^{'2} = \frac{1}{n - 1}\sum_{i = 1}^{n}\mspace{2mu}\left( \frac{M_{i}}{M'}{\bar{y}}_{i} - {\widehat{\bar{Y}}}_{c} \right)^{2}$.

**Multi Stage Sampling (Sub Sampling / Nested Sampling)**

In cluster sampling, all the units of a sampled cluster are studied and
cluster sampling is cheaper and less time consuming than SRS, also less
efficient than SRS.

If instead of studying all the units of a sampled cluster we select only
few units of all the clusters then such sampling scheme is called as two
stage sampling.

Two stage sampling is a compromise between cluster and SRS. Two stage
sampling is more efficient than cluster but less efficient than SRS. Two
stage sampling is cheaper and less time consuming than SRS and costly
and more time consuming than cluster sampling.

*Example:* Suppose we want to study 50 families in a street. Suppose we
have 40 streets and in each street there are 30 houses.

No of p.s.u. (streets) $N = 40$.

No of s.s.u. (houses per street) $M = 30$.

Out of 40 streets 10 streets are selected i.e. $n = 10$.

Select 5 houses from each selected street i.e. $m = 5$.

Total no of houses selected out of $40 \times 30 = 1200$ is
$10 \times 5 = 50$.

By decreasing $m$ we can give more and more representation to the pop
and thus increase the efficiency.

Two stage sampling can further be extended to three stage or multi
stage, where samples are selected at two stages or multi stages.

**Two Stage sampling with equal size of p.s.u.**

Let us suppose that there are $N$ p.s.u. each of size $M$. Therefore
total no of units (s.s.u.) in population = $NM$.

Let $Y_{ij}$ be the value of $j^{th}$ unit in $i^{th}$ p.s.u.
$i = 1,2\ldots N$, $j = 1,2\ldots M$.\
Pop Mean $= \frac{1}{NM}\sum\sum Y_{ij} = \bar{Y}$.

Let $n$ p.s.u. out of $N$ are selected with SRSWOR and $m$ s.s.u. are
selected from each sample p.s.u.\
Total number of units sampled $= nm$.

Let $y_{ij}$ be the value of $j^{th}$ s.s.u. in $i^{th}$ p.s.u. sampled.

$${\bar{y}}_{..} = \frac{1}{nm}\sum_{i = 1}^{n}\mspace{2mu}\sum_{j = 1}^{m}\mspace{2mu} y_{ij}$$

${\bar{y}}_{i} = \frac{1}{m}\sum_{j = 1}^{m}\mspace{2mu} y_{ij}$ is the
$i^{th}$ p.s.u. sampled.

1.  In two stage sampling ${\bar{y}}_{..}$ is unbiased estimator of
    $\bar{Y}$.

2.  In two stage sampling if units are selected by SRSWOR, the variance
    of sample mean is:

> $$V\left( {\bar{y}}_{..} \right) = \left( \frac{1}{n} - \frac{1}{N} \right)S_{b}^{2} + \frac{1}{n}\left( \frac{1}{m} - \frac{1}{M} \right){\bar{S}}_{w}^{2}$$
>
> where
> $S_{b}^{2} = \frac{1}{N - 1}\sum_{i = 1}^{N}\mspace{2mu}({\bar{Y}}_{i} - \bar{Y})^{2} = \text{between p.s.u. variance}$.
>
> $${\bar{S}}_{w}^{2} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu} S_{i}^{2}
> S_{i}^{2} = \frac{1}{M - 1}\sum_{j = 1}^{M}\mspace{2mu}(Y_{ij} - {\bar{Y}}_{i})^{2} = \text{variance within~}i^{th}\text{~p.s.u.}$$.

*Special cases:*

1.  If $N$ is large as compared to $n$:\
    $$V({\bar{y}}_{..}) = \frac{S_{b}^{2}}{n} + \frac{1}{n}\left( \frac{1}{m} - \frac{1}{M} \right){\bar{S}}_{w}^{2}$$

2.  If $N$ and $M$ are both large as compared to $n$ and $m$:\
    $$V({\bar{y}}_{..}) = \frac{S_{b}^{2}}{n} + \frac{{\bar{S}}_{w}^{2}}{nm}$$

The unbiased estimator of variance of mean:

$$\widehat{V}\left( {\bar{y}}_{..} \right) = \left( \frac{1}{n} - \frac{1}{N} \right)s_{b}^{2} + \frac{1}{N}\left( \frac{1}{m} - \frac{1}{M} \right){\bar{s}}_{w}^{2}$$

where
$s_{b}^{2} = \frac{1}{n - 1}\sum_{i = 1}^{n}\mspace{2mu}({\bar{y}}_{i} - {\bar{y}}_{..})^{2}$\
and
${\bar{s}}_{w}^{2} = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu} s_{i}^{2}$
where
$s_{i}^{2} = \frac{1}{m - 1}\sum_{j = 1}^{m}\mspace{2mu}(y_{ij} - {\bar{y}}_{i})^{2}$.

**Comparison of two stage sampling with SRS and cluster:**\
*Case-I: Two stage sampling*\
In two stage sampling $n$ p.s.u. are selected out of $N$ and $m$ s.s.u.
are selected out of $M$ for each $n$ p.s.u.\
Total s.s.u. selected $= nm$ out of $NM$.

$$V_{2} = V\left( {\bar{y}}_{..} \right) = \frac{\sigma_{b}^{2}}{n} + \ldots$$

*Case-II: SRS*\
If $nm$ units are selected out of $NM$ by SRSWR:

$$V_{SRS} = V\left( \bar{y} \right) = \frac{\sigma^{2}}{nm}$$

*Case-III: Cluster sampling*\
Using cluster sampling where $n$ clusters of size $M$ are selected (if
sample size equivalent):

$$V_{cluster} = V({\bar{\bar{y}}}_{c}) = \frac{\sigma^{2}}{nM}\lbrack 1 + (M - 1)\rho_{c}\rbrack$$

Since $M > m$ and $\rho_{c}$ is +ve,

$$(M - 1)\rho_{c} > (m - 1)\rho_{c} > 0$$

$$V_{SRS}(\bar{y}) \leq V_{TwoStage}({\bar{y}}_{..}) \leq V_{Cluster}({\bar{\bar{y}}}_{c})$$
Hence two stage sampling is a compromise between cluster and SRS from
variance and precision point of view.

**Three-Stage Sampling**\
$N$ p.s.u. $\rightarrow n$ p.s.u.\
$M$ s.s.u. $\rightarrow m$ s.s.u.\
$P$ t.s.u. $\rightarrow p$ t.s.u.\
Total number of t.s.u. $= nmp$ out of $NMP$.\
$Y_{ijk}$ be the value of $k^{th}$ t.s.u. in $j^{th}$ s.s.u. of $i^{th}$
p.s.u. in the pop.\
Pop Mean $= \frac{1}{NMP}\sum\sum\sum Y_{ijk} = {\bar{Y}}_{...}$\
Sample Mean $= {\bar{y}}_{...} = \frac{1}{nmp}\sum\sum\sum y_{ijk}$.\
$y_{ijk}$ be the value of $k^{th}$ t.s.u. in $j^{th}$ s.s.u. of $i^{th}$
p.s.u. of the sample.

$$E\left( {\bar{y}}_{\ldots} \right) = {\bar{Y}}_{\ldots}$$

$${\widehat{Y}}_{\ldots} = NMP{\bar{y}}_{\ldots}$$

$$V\left( {\bar{y}}_{\ldots} \right) = \left( \frac{1}{n} - \frac{1}{N} \right)S_{b}^{2} + \frac{1}{n}\left( \frac{1}{m} - \frac{1}{M} \right){\bar{S}}_{w}^{2} + \frac{1}{nm}\left( \frac{1}{p} - \frac{1}{P} \right){\bar{\bar{S}}}_{b}^{2}$$

Where
$S_{b}^{2} = \frac{1}{N - 1}\sum_{i = 1}^{N}\mspace{2mu}({\bar{Y}}_{i} - {\bar{Y}}_{...})^{2}$
(variance between p.s.u.).\
${\bar{S}}_{w}^{2} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu} S_{i}^{2}$,
$S_{i}^{2} = \frac{1}{M - 1}\sum_{j = 1}^{M}\mspace{2mu}({\bar{Y}}_{ij} - {\bar{Y}}_{i})^{2}$
(variance of $i^{th}$ p.s.u.).

${\bar{\bar{S}}}_{b}^{2} = \frac{1}{NM}\sum\sum S_{ij}^{2}$,
$S_{ij}^{2} = \frac{1}{P - 1}\sum_{k = 1}^{P}\mspace{2mu}(Y_{ijk} - {\bar{Y}}_{ij})^{2}$\
If $N,M$ and $P$ are very large as compared to $n,m,p$ then:\
$$V({\bar{y}}_{...}) = \frac{S_{b}^{2}}{n} + \frac{{\bar{S}}_{w}^{2}}{nm} + \frac{{\bar{\bar{S}}}_{b}^{2}}{nmp}$$

Unbiased estimator of $V({\bar{y}}_{...})$:

$$\widehat{V}\left( {\bar{y}}_{\ldots} \right) = \left( \frac{1}{n} - \frac{1}{N} \right)\frac{s_{b}^{2}}{n} + \frac{1}{N}\left( \frac{1}{m} - \frac{1}{M} \right)\frac{{\bar{s}}_{w}^{2}}{n} + \frac{1}{NM}\left( \frac{1}{p} - \frac{1}{P} \right)\frac{{\bar{\bar{s}}}_{b}^{2}}{nm}$$

Where
$s_{b}^{2} = \frac{1}{n - 1}{\sum_{}^{}}_{i = 1}^{n}\mspace{2mu}({\bar{y}}_{i} - {\bar{y}}_{\ldots})^{2}$

${\bar{s}}_{w}^{2} = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu} s_{i}^{2}$,
where
$s_{i}^{2} = \frac{1}{m - 1}\sum_{j = 1}^{m}\mspace{2mu}({\bar{y}}_{ij} - {\bar{y}}_{i})^{2}$.\
${\bar{\bar{s}}}_{b}^{2} = \frac{1}{nm}\sum\sum s_{ij}^{2}$, where
$s_{ij}^{2} = \frac{1}{p - 1}\sum_{k = 1}^{p}\mspace{2mu}(y_{ijk} - {\bar{y}}_{ij})^{2}$.

**Cost function:**\
Let $c_{0}$ be the overhead cost.\
$c_{1}$ be the cost of survey per p.s.u.\
$c_{2}$ be the cost of survey per s.s.u.\
$C = c_{0} + nc_{1} + nmc_{2}$ is the cost function of two stage
sampling.

**Estimation of Ratio**

Sometimes instead of estimating population mean, we are interested in
estimating the ratio of two population or ratio of two pop totals.\
e.g.\
Sex Ratio =
$\frac{\text{Total number of female}}{\text{Total no of males}}$.\
Per capita Income = $\frac{\text{Total income}}{\text{Total pop}}$.\
Per capita consumption of milk =
$\frac{\text{Total milk yield}}{\text{Total pop}}$.

Let $Y_{1},Y_{2}\ldots Y_{N}$ be the value of pop units for variable
$y$.\
Let $X_{1},X_{2}\ldots X_{N}$ be the value of pop units for variable
$x$.\
Ratio of pop total
$R = \frac{\text{Totals for variable~}y}{\text{Totals for variable~}x} = \frac{\sum Y_{i}}{\sum X_{i}} = \frac{Y}{X}$.\
Ratio of pop mean
$= \frac{\frac{1}{N}\sum Y_{i}}{\frac{1}{N}\sum X_{i}} = \frac{\bar{Y}}{\bar{X}}$.\
Let $y_{1},y_{2}\ldots y_{n}$ be the value of sample units for variable
$y$.\
Let $x_{1},x_{2}\ldots x_{n}$ be the value of sample units for variable
$x$.\
Ratio of sample mean $= \widehat{R} = \frac{\bar{y}}{\bar{x}}$.

$\widehat{R} = \frac{\bar{y}}{\bar{x}}$ is biased estimator of pop ratio
$R$.\
$E(\widehat{R} - R) = E\left( \frac{\bar{y}}{\bar{x}} - R \right) = E\left( \frac{\bar{y} - R\bar{x}}{\bar{x}} \right)$.\
When $n$ is large then $\bar{x}$ in denominator can be replaced by
$\bar{X}$:\
$E(\widehat{R} - R) \approx \frac{\bar{Y} - R\bar{X}}{\bar{X}} = \frac{\bar{Y}}{\bar{X}} - R = R - R = 0$.\
For large $n$, $\widehat{R}$ is unbiased estimator of pop ratio.

$V(\widehat{R}) \approx \frac{1 - f}{n{\bar{X}}^{2}} \cdot \frac{1}{N - 1}\sum_{i = 1}^{N}\mspace{2mu}(Y_{i} - RX_{i})^{2}$.\
*Proof:* We know that $\widehat{R} = \frac{\bar{y}}{\bar{x}}$.\
Let $d_{i} = y_{i} - Rx_{i}$, $i = 1,2\ldots n$.
$\bar{d} = \bar{y} - R\bar{x}$.\
$\bar{D} = \frac{1}{N}\sum D_{i} = \bar{Y} - R\bar{X} = 0$.\
In SRSWOR:
$V(\bar{d}) = \frac{N - n}{N} \cdot \frac{S_{d}^{2}}{n} = \frac{N - n}{N} \cdot \frac{1}{n} \cdot \frac{1}{N - 1}\sum_{i = 1}^{N}\mspace{2mu}(D_{i} - \bar{D})^{2}$.\
$V(\bar{d}) = \frac{1 - f}{n} \cdot \frac{1}{N - 1}\sum_{i = 1}^{N}\mspace{2mu}(Y_{i} - RX_{i})^{2}$.\
Now
$V(\widehat{R}) = E(\widehat{R} - R)^{2} = E\left( \frac{\bar{y}}{\bar{x}} - R \right)^{2} = E\left\lbrack \frac{\bar{y} - R\bar{x}}{\bar{x}} \right\rbrack^{2}$.\
$\approx \frac{1}{{\bar{X}}^{2}}E\lbrack\bar{y} - R\bar{x}\rbrack^{2} = \frac{1}{{\bar{X}}^{2}}E(\bar{d})^{2} = \frac{1}{{\bar{X}}^{2}}V(\bar{d})$.\
$V(\widehat{R}) = \frac{1}{{\bar{X}}^{2}}\frac{1 - f}{n}\frac{1}{N - 1}\sum_{i = 1}^{N}\mspace{2mu}(Y_{i} - RX_{i})^{2}$.

Unbiased estimator of $V(\widehat{R})$ is
$\widehat{V}(\widehat{R}) = \frac{1 - f}{n{\bar{x}}^{2}}s_{d}^{2}$ where
$s_{d}^{2} = \frac{1}{n - 1}\sum_{i = 1}^{n}\mspace{2mu}(y_{i} - \widehat{R}x_{i})^{2}$.

**Ratio Estimator:**\
In ratio estimation we make use of auxiliary variable $x$ along with the
variable $y$ and make use of the correlation between $X_{i}$ and
$Y_{i}$.\
We can improve the traditional estimate of $\bar{Y}$ i.e. instead of
using $\bar{y}$ as an estimator for $\bar{Y}$ we use
${\widehat{\bar{Y}}}_{R} = \frac{\bar{y}}{\bar{x}}\bar{X}$ as the
estimator of pop mean. Where $\bar{X}$ is the pop mean for variable $x$
and must be known.\
Ratio estimators are in general biased but more precise.\
$V({\widehat{\bar{Y}}}_{R}) = V\left( \frac{\bar{y}}{\bar{x}}\bar{X} \right) = V(\widehat{R}\bar{X}) = {\bar{X}}^{2}V(\widehat{R})$.\
$= {\bar{X}}^{2}\left\lbrack \frac{1 - f}{n{\bar{X}}^{2}}\frac{1}{N - 1}\sum(Y_{i} - RX_{i})^{2} \right\rbrack$.\
$= \frac{1 - f}{n}\frac{1}{N - 1}\sum_{i = 1}^{N}\mspace{2mu}(Y_{i} - RX_{i})^{2}$
(1st form).

$${V({\widehat{\bar{Y}}}_{R}) = \frac{1 - f}{n}\frac{1}{N - 1}\sum_{i = 1}^{N}\mspace{2mu}\lbrack(Y_{i} - \bar{Y}) - R(X_{i} - \bar{X})\rbrack^{2}
}{= \frac{1 - f}{n}\frac{1}{N - 1}\left\lbrack \sum(Y_{i} - \bar{Y})^{2} + R^{2}\sum(X_{i} - \bar{X})^{2} - 2R\sum(X_{i} - \bar{X})(Y_{i} - \bar{Y}) \right\rbrack
 = \frac{1 - f}{n}\lbrack S_{Y}^{2} + R^{2}S_{X}^{2} - 2RS_{XY}\rbrack}$$
(2nd form).

Where
$\rho = \frac{\sum(X_{i} - \bar{X})(Y_{i} - \bar{Y})}{\sqrt{\sum(X_{i} - \bar{X})^{2}\sum(Y_{i} - \bar{Y})^{2}}} = \frac{S_{XY}}{S_{X}S_{Y}}$.\
So $S_{XY} = \rho S_{X}S_{Y}$.\
$V({\widehat{\bar{Y}}}_{R}) = \frac{1 - f}{n}\lbrack S_{Y}^{2} + R^{2}S_{X}^{2} - 2\rho RS_{X}S_{Y}\rbrack$.

3rd form:\
$$V({\widehat{\bar{Y}}}_{R}) = \frac{1 - f}{n}{\bar{Y}}^{2}\left\lbrack \frac{S_{Y}^{2}}{{\bar{Y}}^{2}} + \frac{{\bar{Y}}^{2}}{{\bar{X}}^{2}}\frac{1}{{\bar{Y}}^{2}}S_{X}^{2} - 2\rho\frac{\bar{Y}}{\bar{X}}\frac{1}{{\bar{Y}}^{2}}S_{X}S_{Y} \right\rbrack
 = \frac{1 - f}{n}{\bar{Y}}^{2}\lbrack C_{Y}^{2} + C_{X}^{2} - 2\rho C_{X}C_{Y}\rbrack$$.

Unbiased estimator of $V({\widehat{\bar{Y}}}_{R})$ is
$\widehat{V}({\widehat{\bar{Y}}}_{R}) = \frac{1 - f}{n}\lbrack s_{y}^{2} + {\widehat{R}}^{2}s_{x}^{2} - 2\widehat{R}s_{xy}\rbrack$.

**Condition under which Ratio estimator is more precise than mean per
unit of SRS:**\
In Ratio method of estimation we know that:\
$V({\widehat{\bar{Y}}}_{R}) = \frac{1 - f}{n}\lbrack S_{Y}^{2} + R^{2}S_{X}^{2} - 2\rho RS_{X}S_{Y}\rbrack$.\
And in SRSWOR $V(\bar{y}) = \frac{1 - f}{n}S_{Y}^{2}$.\
Ratio estimator will more precise than SRSWOR if
$V({\widehat{\bar{Y}}}_{R}) \leq V(\bar{y})$.\
$\frac{1 - f}{n}\lbrack S_{Y}^{2} + R^{2}S_{X}^{2} - 2R\rho S_{X}S_{Y}\rbrack \leq \frac{1 - f}{n}S_{Y}^{2}$.\
$\  \Longrightarrow \ R^{2}S_{X}^{2} - 2R\rho S_{X}S_{Y} \leq 0\  \Longrightarrow \ R^{2}S_{X}^{2} \leq 2R\rho S_{X}S_{Y}$.\
$RS_{X} \leq 2\rho S_{Y}\  \Longrightarrow \ \rho \geq \frac{RS_{X}}{2S_{Y}}\  \Longrightarrow \ \rho \geq \frac{1}{2}\frac{\bar{Y}}{\bar{X}}\frac{S_{X}}{S_{Y}}\  \Longrightarrow \ \rho \geq \frac{1}{2}\frac{S_{X}/\bar{X}}{S_{Y}/\bar{Y}}\  \Longrightarrow \ \rho \geq \frac{1}{2}\frac{C_{X}}{C_{Y}}$.\
Hence Ratio estimator are more precise than SRS if
$\rho \geq \frac{1}{2}\frac{C_{X}}{C_{Y}}$.

In particular when $C_{X} = 2C_{Y}$ then $\rho \geq 1$ which is a
contradiction. Hence when coefficient of variation of a variable $x$
exceeds twice the coefficient of variation of variable $y$, then in the
situation Ratio estimator is less precise and should not be used.\
In general, $X_{i}$ are some past frame of $Y_{i}$, so $C_{X} = C_{Y}$
hold approximately. So the ratio estimator is more precise than SRS if
$\rho \geq 1/2$.

**Remarks:**

1.  If $\rho > \frac{1}{2}\frac{C_{X}}{C_{Y}}$, then ratio estimators
    are more precise than SRS.

2.  If $C_{X} > 2C_{Y}$ then $\rho > 1$ which is a contradiction. Hence
    in this situation ratio estimator are less precise than SRS and
    should not be used.

3.  When $X_{i}$ has some past values of $Y_{i}$ then $C_{X} = C_{Y}$.
    In this situation ratio estimator will be more precise if
    $\rho \geq 1/2$.

4.  When there is a linear trend in $Y_{i}$ and $X_{i}$ and line of
    regression passes through origin, then ratio estimator are unbiased.

5.  Ratio estimator are BLUE if:

    a.  Line of regression passes through origin and

    b.  The variance $Y_{i}$ about this line is proportional to $X_{i}$.
