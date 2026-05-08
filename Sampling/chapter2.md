**2. BASIC METHODS OF SIMPLE RANDOM SAMPLING**

*\"To this end was I born for this cause came I into the world, that I
should bear witness unto the truth . .. Pilate saith unto him \'What is
truth?\'\"*\
**St. John**

**2.1 SIMPLE RANDOM SAMPLING**

The simplest and common most method of sampling is simple random
sampling in which the sample is drawn unit by unit, with equal
probability of selection for each unit at each draw. Therefore, simple
random sampling is a method of selecting $n$ units out of a population
of size $N$ by giving equal probability to all units, or a sampling
procedure in which all possible combinations of $n$ units that may be
formed from the population of $N$ units have the same probability of
selection. It is also sometimes referred to as unrestricted random
sampling. If a unit is selected and noted and then returned to the
population before the next drawing is made and this procedure repeated
$n$ times, it gives rise to a simple random sample of $n$ units. This
procedure is generally known as simple random sampling with replacement
(wr). If this procedure is repeated till $n$ distinct units are selected
and all repetitions are ignored, it is called a simple random sampling
without replacement (wor).

**Theorem 2.1.1:** The probability that a specified unit of the
population being selected at any given draw is equal to the probability
of its being selected at the first draw.

**Proof:** The probability that the specified unit is selected at the
$r$th draw is clearly the product of (a) the probability that the
specified unit is not selected in any of the previous $(r - 1)$ draws,
and (b) the probability that it is selected at the $r$th draw with the
condition that it is not selected in the previous $(r - 1)$ draws.

The probability under (a), is given by

$$\frac{N - 1}{N} \cdot \frac{N - 2}{N - 1}\cdots\frac{N - r + 1}{N - r + 2} = \frac{N - r + 1}{N}$$

The probability under (b) is given by $1/(N - r + 1)$. Hence the
required probability is $1/N$ which is independent of the term $r$, i.e.
draw number.

**Theorem 2.1.2:** The probability of a specified unit being included in
the sample is equal to $n/N$.

**Proof:** Let $n$ denote the sample size. Since the specified unit may
be included in the sample at any of the $n$ draws, the probability that
a specified unit is included in the sample is the sum of the
probabilities of $n$ mutually exclusive events, viz. it is included in
the sample at the first draw, second draw, \..., $n$th draw. As shown in
Theorem 2.1.1 the probability of each case is $1/N$. Thus the required
probability is $n/N$.

**Corollary 1:** The probability of a specified sample of $n$ units,
ignoring order, is $1/\binom{N}{n}$.

**Corollary 2:** If in the population of $N$ units, $m$ units are
deleted and $m'$ are added, show that the probability of selection of
any unit at a specified draw is $(N - m + m')^{- 1}$.

**2.2 PROCEDURES OF SELECTING A RANDOM SAMPLE**

Since the theory of sampling is based on the assumption of random
sampling, the technique of random sampling is of basic significance.
Some of the procedures used for selecting a random sample are as
follows:

\(i\) Lottery Method\
(ii) Use of Random Number Tables

**2.2.1 Lottery Method**

In practice, a ticket/chit may be associated with each unit of the
population. Thus, each sampling unit has its identification mark from 1
to $N$. The procedure of selecting an individual is simple. All the
tickets/chits are placed in a container, drum or metallic spherical
device, in which a thorough mixing or reshuffling is possible, before
each draw. Draws of tickets/chits may be continued until a sample of the
required size is obtained.

This procedure of numbering units on tickets/chits and selecting one
after reshuffling becomes cumbersome when the population size is large.
It may be rather difficult to achieve a thorough shuffling in practice.
Human bias and prejudice may also creep in this method.

**2.2.2 Use of Random Number Tables**

A random number table is an arrangement of digits 0 to 9, in either a
linear or rectangular pattern, where each position is filled with one of
these digits. A table of random numbers is so constructed that all
numbers, 0, 1, 2, \..., 9, appear independent of each other. Some random
number tables in common use are:

\(i\) Tippett\'s random number tables\
(ii) Fisher and Yates tables\
(iii) Kendall and Smith tables\
(iv) A million random digits

To ascertain whether these series of random numbers are really random,
the following tests may be applied:

\(i\) Frequency test\
(ii) Serial test\
(iii) Gap test\
(iv) Poker test

A practical method of selecting a random sample is to choose units
one-by-one with the help of a table of random numbers. By considering
two-digit numbers, we can obtain numbers from 00 to 99, all having the
same frequency. Similarly, three or more digit numbers may be obtained
by combining three or more rows or columns of these tables.

The simplest way of selecting a sample of the required size is by
selecting a random number from 1 to $N$ and then taking the unit bearing
that number. This procedure involves a number of rejections since all
numbers greater than $N$ appearing in the table are not considered for
selection. The use of random numbers is, therefore, modified and some of
these modified procedures are:

\(i\) Remainder approach\
(ii) Quotient approach\
(iii) Independent choice of digits

**Remainder Approach**

Let $N$ be an $r$-digit number and let its $r$-digit highest multiple be
$N'$. A random number $k$ is chosen from 1 to $N'$ and the unit with the
serial number equal to the remainder obtained on dividing $k$ by $N$ is
selected. If the remainder is zero, the last unit is selected. As an
illustration, let $N = 123$, the highest three-digit multiple of 123 is
984. For selecting a unit, one random number from 001 to 984 has to be
selected. Let the random number selected be 287. Dividing 287 by 123,
the remainder is 41. Hence, the unit with serial number 41 is selected
in the sample.

**Quotient Approach**

Let $N$ be an $r$-digit number and let its $r$-digit highest multiple be
$N'$ such that $N'/N = q$. A random number $k$ is chosen from 0 to
$(N' - 1)$. Dividing $k$ by $q$ the quotient $r$ is obtained and the
unit bearing the serial number $(r - 1)$ is selected in the sample. As
an illustration, let $N = 16$ and hence $N' = 96$ and $q = 96/16 = 6$.
Let the two-digit random number chosen be 65 which lies between 0 and
95. Dividing 65 by 6, the quotient is 10 and hence the unit bearing
number $(10 - 1) = 9$ is selected in the sample.

**Independent Choice of Digits**

This method, suggested by Mathai (1954), consists of the selection of
two random numbers which are combined to form one random number. One
random number is chosen according to the first digit and other according
to the remaining digits of the population size. If the number chosen is
0 the last unit is chosen. But if the number made up is greater than or
equal to $N$, the number is rejected and the operation is repeated.

**Example 2.1:** Select a random sample of 11 households from a list of
112 households in a village.\
(i) By using the 3-digit random numbers given in columns 1 to 3, 4 to 6
and so on of the random number table and rejecting numbers greater than
112 (also the number 000), we have for the sample bearing serial numbers
033, 051, 052, 099, 102, 081, 092, 013, 017, 076, and 079.

\(ii\) In the above procedure, a large number of random numbers is
rejected. Hence, a commonly used device, i.e. remainder approach, is
employed to avoid the rejection of such large numbers. The greatest
three-digit multiple of 112 is 896. By using three-digit random numbers
as above, the sample will comprise of households with serial numbers
086, 033, 049, 097, 051, 052, 066, 107, 015, 106 and 020.

\(iii\) In case the quotient approach is applied, the 3-digit multiple
of 112 is 896 and $896/112 = 8$. Using the same random numbers and
dividing them by 8, we have the sample of households with list numbers
025, 004, 020, 026, 006, 006, 092, 041, 085, 027 and 086 with the
replacement method and with list numbers 025, 004, 020, 026, 006, 092,
041, 085, 027, 086 and 042 without the replacement method.

**Example 2.2:** Ten orchards, in a locality near Lucknow, were having
125, 793, 970, 830, 1502, 864, 503, 106, 970, 312 fruit trees,
respectively. Draw a random sample of 10 fruit trees by using random
numbers.

Let us assume that in the first orchard the fruit trees bear serial
numbers 1 to 125, in the second orchard from 126 to 918, and so on.
Hence, the cumulative serial numbers may be written as, 125, 918, 1888,
2718, 4220, 5084, 5587, 5693, 6663, 6975. By using 4-digit random
numbers of the above-said table with similar notions, we have 1983,
0330, 1614, 2096, 0511, 0524, 3311, 6874, 2183 and 6926.

With the first random number 1983, we select the fruit tree bearing
serial number 95 in the 4th orchard. Similarly, with the second random
number 0330, we select the tree bearing serial number 205 in the 2nd
orchard, and so on. Working out this procedure further, we find that
orchards included in the sample have serial numbers 2, 3, 4, 5 and 10.
Thus, it is not necessary to give serial numbers to fruit trees in all
the orchards, only five orchards of the above-shown numbers will suffice
the purpose of selecting a random sample of 10 fruit trees.

**2.3 ESTIMATION OF POPULATION PARAMETERS**

Let us assume that each unit $u_{i}$ in the population is associated
with a variate value $y_{i}$, for the character $y$. For parameters, let
us designate\
The population total, $Y = \sum_{i = 1}^{N}\mspace{2mu} y_{i}$\
The population mean,
$\bar{Y} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu} y_{i}$\
The population variance,
$\sigma^{2} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu}(y_{i} - \bar{Y})^{2}$

Let the $n$ units in the sample be $u_{1},u_{2},\ldots,u_{n}$, with
variate values $y_{1},y_{2},\ldots,y_{n}$ respectively. The estimators
of population total and mean are given by

$$\widehat{Y} = \frac{N}{n}\sum_{i = 1}^{n}\mspace{2mu} y_{i} = N\bar{y}$$

and

$$\bar{y} = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu} y_{i},$$

respectively.

The factor $N/n$ by which the sample total is multiplied is sometimes
called the expansion or raising or inflation factor. Its inverse $n/N$
is called the sampling fraction and is denoted by the letter $f$ in this
text.

**Theorem 2.3.1:** In simple random sampling, wor, the sample mean
$\bar{y}$ is an unbiased estimator of $\bar{Y}$ and its sampling
variance is given by

$$V(\bar{y}) = \left( 1 - \frac{n}{N} \right)\frac{S^{2}}{n} = (1 - f)\frac{S^{2}}{n}\ (2.3.1)$$

where

$$S^{2} = \frac{N}{N - 1}\sigma^{2}$$

**Proof:** We have

$$E(\bar{y}) = E\left( \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu} y_{i} \right) = \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu} E(y_{i})$$

By definition,

$$E(y_{i}) = \sum_{i = 1}^{N}\mspace{2mu} P_{i}y_{i} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu} y_{i} = \bar{Y}$$

Hence, $E(\bar{y}) = \bar{Y}$\
Thus the sample mean is an unbiased estimator of the population mean.

The variance of $\bar{y}$ is given by

$$V(\bar{y}) = E(\bar{y} - \bar{Y})^{2} = E\left\lbrack \frac{1}{n}\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y}) \right\rbrack^{2} = \frac{1}{n^{2}}E\left\lbrack \sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y})^{2} + 2\sum_{i \neq j}^{}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y})(y_{j} - \bar{Y}) \right\rbrack$$

Since

$$E(y_{i} - \bar{Y})^{2} = \frac{1}{N}\sum_{i = 1}^{N}\mspace{2mu}(y_{i} - \bar{Y})^{2} = \sigma^{2}$$

and

$$E(y_{i} - \bar{Y})(y_{j} - \bar{Y}) = \frac{1}{N(N - 1)}\sum_{i \neq j}^{}\mspace{2mu}(y_{i} - \bar{Y})(y_{j} - \bar{Y}) = \frac{1}{N(N - 1)}\left\lbrack \left( \sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y}) \right)^{2} - \sum_{i = 1}^{N}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y})^{2} \right\rbrack = \frac{- N\sigma^{2}}{N(N - 1)} = - \frac{\sigma^{2}}{N - 1}$$

Thus,

$$V(\bar{y}) = \frac{1}{n^{2}}\left\{ n\sigma^{2} - n(n - 1)\frac{\sigma^{2}}{N - 1} \right\} = \frac{N - n}{N - 1}\frac{\sigma^{2}}{n} = \left( 1 - \frac{n}{N} \right)\frac{S^{2}}{n}$$

which proves the theorem.

**Corollary 1:** In simple random sampling, wor, the standard error of
$\bar{y}$ is given by

$$S_{\bar{y}} = S\sqrt{\frac{N - n}{nN}} = S\sqrt{\frac{1 - f}{n}}\ (2.3.2)$$

**Corollary 2:** In simple random sampling, wor, the variance of
$\widehat{Y} = N\bar{y}$, as an estimator of the population total $Y$,
is obtained as

$$V(\widehat{Y}) = E(\widehat{Y} - Y)^{2} = \frac{N^{2}S^{2}(N - n)}{nN} = (1 - f)\frac{N^{2}S^{2}}{n}\ (2.3.3)$$

**Corollary 3:** In simple random sampling, wor, the standard error of
$\widehat{Y}$ is given by

$$S_{\widehat{Y}} = NS\sqrt{\frac{N - n}{nN}} = NS\sqrt{\frac{1 - f}{n}}\ (2.3.4)$$

If sampling is with replacement, a random sample of size $n$ gives
sample mean $\bar{y}$ as an unbiased estimator. From the above results,
it can be seen easily that terms $(N - n)/N$ for the variance and
$\sqrt{(N - n)/N}$ for the standard error are introduced due to
finiteness of the population and these are called finite population
corrections (fpc). In case of random sampling, wr, the variance and
standard error can be obtained by ignoring finite population correction.

**Corollary 4:** In random sampling, wr, the variance and standard error
of $\bar{y}$ can be written as

$$V(\bar{y}) = \frac{\sigma^{2}}{n},\ \sigma_{\bar{y}} = \frac{\sigma}{\sqrt{n}}\ (2.3.5a)$$

If $n$ is small as compared to $N$, the fpc will not differ much from
unity and the sampling variance of the mean will be nearly equal to that
of the mean of a sample drawn from an infinite population.

**Corollary 5:** In random sampling, wr, the variance and standard error
of $\widehat{Y} = N\bar{y}$ can be written as

$$V(\widehat{Y}) = \frac{N^{2}\sigma^{2}}{n},\ \sigma_{\widehat{Y}} = \frac{N\sigma}{\sqrt{n}}\ (2.3.5b)$$

**Theorem 2.3.2:** In simple random sampling,

$$s^{2} = \frac{\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{y})^{2}}{n - 1}\ (2.3.6)$$

is an unbiased estimator of $S^{2} = \frac{N}{N - 1}\sigma^{2}$.

**Proof:** We may write

$$s^{2} = \frac{\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}\lbrack(y_{i} - \bar{Y}) - (\bar{y} - \bar{Y})\rbrack^{2}}{n - 1} = \frac{\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu}(y_{i} - \bar{Y})^{2} - n(\bar{y} - \bar{Y})^{2}}{n - 1}$$

Therefore,

$$E(s^{2}) = \frac{\sum_{i = 1}^{n}\mspace{2mu}\mspace{2mu} E(y_{i} - \bar{Y})^{2} - nE(\bar{y} - \bar{Y})^{2}}{n - 1} = \frac{n(N - 1)S^{2}/N - n(N - n)S^{2}/(Nn)}{n - 1} = S^{2}$$

Hence $s^{2}$ is an unbiased estimator of $S^{2}$.

**Corollary 1:** An unbiased estimator of the variance of $\bar{y}$ in
random sampling, wor, is given by

$$v(\bar{y}) = \frac{(N - n)s^{2}}{Nn} = (1 - f)\frac{s^{2}}{n}\ (2.3.7)$$

For an estimate of the standard error, we take
$s_{\bar{y}} = s\sqrt{(1 - f)/n}$.

**Corollary 2:** An unbiased estimator of the variance of
$\widehat{Y} = N\bar{y}$ in random sampling, wor, is given by

$$v(\widehat{Y}) = \frac{N(N - n)s^{2}}{n} = (1 - f)N^{2}\frac{s^{2}}{n}\ (2.3.8)$$

For an estimate of the standard error, we take
$s_{\widehat{Y}} = Ns\sqrt{(1 - f)/n}$.

**Corollary 3:** An unbiased estimator of the variance of $\bar{y}$ in
random sampling, wr, is given by

$$v(\bar{y}) = \frac{s^{2}}{n}\ (2.3.9)$$

For an estimate of the standard error, we take
$s_{\bar{y}} = s/\sqrt{n}$.

**Corollary 4:** An unbiased estimator of the variance
$\widehat{Y} = N\bar{y}$ in random sampling, wr, is given by

$$v(\widehat{Y}) = \frac{N^{2}s^{2}}{n}\ (2.3.10)$$

For an estimate of the standard error, we take
$s_{\widehat{Y}} = Ns/\sqrt{n}$.

**Example 2.3:** A random sample of $n = 2$ households was drawn from a
small colony of 5 households (hypothetical population) having monthly
income (in rupees) as follows:

  ---------------------------------------------
  Household       1     2     3     4     5
  --------------- ----- ----- ----- ----- -----
  Income (in      156   149   166   164   155
  rupees)                                 

  ---------------------------------------------

\(i\) Calculate population mean $\bar{Y}$, variance $(\sigma^{2})$ and
mean square error $(S^{2})$.\
(ii) Enumerate all possible samples of size 2 by the replacement method
and show that\
(a) the sample mean gives an unbiased estimate of the population mean
and find its sampling variance;\
(b) sample variance $(s^{2})$ is an unbiased estimate of the population
variance $\sigma^{2}$; and\
(c) $v(\bar{y}) = (y_{1} - y_{2})^{2}/4$ is an unbiased estimator of
$V(\bar{y})$, i.e.
$E\lbrack v(\bar{y})\rbrack = V(\bar{y}) = \sigma^{2}/2$.\
(iii) Enumerate all possible samples of size 2 by the without
replacement method and show that\
(a) the sample mean gives an unbiased estimate of the population mean
and find its sampling variance;\
(b) the sample variance $(s^{2})$ is an unbiased estimate of the
population variance $S^{2}$; and\
(c) $v(\bar{y}) = 3(y_{1} - y_{2})^{2}/20$ is an unbiased estimator of
$V(\bar{y})$, i.e.
$E\lbrack v(\bar{y})\rbrack = V(\bar{y}) = \frac{1 - f}{n}S^{2} = \frac{3}{10}S^{2}$.

\(i\) The population mean of 5 households

$$\bar{Y} = (156 + 149 + 166 + 164 + 155)/5 = 158.00$$

The population variance

$$\sigma^{2} = \lbrack(156^{2} + 149^{2} + \cdots + 155^{2}) - 5 \times 158^{2}\rbrack/5 = 38.80$$

Hence $S^{2} = N\sigma^{2}/(N - 1) = 5 \times 38.8/4 = 48.50$

\(ii\) It can be seen that the total number of possible samples is 25
$( = 5^{2})$. Also, each of the 25 possible samples has the same
probability $(1/25)$ of being selected.

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

\(a\) The expected value of $\bar{y}$ is given by the average value of
column (6), which works out to be the population mean 158.0, thus
verifying that the estimator is unbiased. We find from columns (6) and
(7) of Table 2.3.1 that these estimates differ, in general, from
$\bar{Y}( = 158.0)$, and that the error usually varies from sample to
sample. Further, it is of interest to note from column (7) that each
sample mean $\bar{y}$ given by column (6) is an unbiased estimate of the
population mean $(\bar{Y})$ as the average of column (7) is zero, which
proves the result. The sampling variance is the mean of the squares of
error \[column (7)\] which works out to 19.40 $( = 38.80/2)$.\
(b) The sample variance $(s^{2})$ is given by $(y_{1} - y_{2})^{2}/2$
which is twice the value given in column (8). Hence, $2 \times (8)$
shows that $E(s^{2})$ is equal to 38.80 $(\sigma^{2})$, which shows that
$s^{2}$ is an unbiased estimator for the population variance in simple
random sampling, wr.\
(c) An estimator of $V(\bar{y})$ is given by
$v(\bar{y}) = (y_{1} - y_{2})^{2}/4$, the values which are given in
column (8) of Table 2.3.1 for possible samples. The expected value of
$v(\bar{y})$ is the average of the values in column (8), showing that
$E\lbrack v(\bar{y})\rbrack = V(\bar{y}) = \sigma^{2}/2$. Thus the
estimate $v(\bar{y})$ is unbiased.

**Table 2.3.2:** All samples of 2 units from 5 units in simple random
sampling without replacement

  ------------------------------------------------------------------------------------------------------------------------------------
  Sample no.    Units in     Probability   $$y_{1}$$   $$y_{2}$$   $$\bar{y}$$   Error                   $$3(y_{1} - y_{2})^{2}/20$$
                sample                                                           $(\bar{y} - \bar{Y})$   
  ------------- ------------ ------------- ----------- ----------- ------------- ----------------------- -----------------------------
  1             1,2          1/10          156         149         152.5         -5.5                    7.35

  2             1,3          1/10          156         166         161.0         3.0                     15.00

  3             1,4          1/10          156         164         160.0         2.0                     9.60

  4             1,5          1/10          156         155         155.5         -2.5                    0.15

  5             2,3          1/10          149         166         157.5         -0.5                    43.35

  6             2,4          1/10          149         164         156.5         -1.5                    33.75

  7             2,5          1/10          149         155         152.0         -6.0                    5.40

  8             3,4          1/10          166         164         165.0         7.0                     0.60

  9             3,5          1/10          166         155         160.5         2.5                     18.15

  10            4,5          1/10          164         155         159.5         -1.5                    12.15

  **Average**                                                      **158.0**                             **14.55**
  ------------------------------------------------------------------------------------------------------------------------------------

\(iii\) In case of random sampling, wor, the number of possible samples
is $10\left\lbrack = \binom{5}{2} \right\rbrack$. It can be seen that
each of the 10 possible samples has the same probability $(1/10)$ of
being selected.\
(a) The expected value of $\bar{y}$, which is given by the average of
column (6) of Table 2.3.2, works out to be the population mean 158.0,
thus verifying that $\bar{y}$ is an unbiased estimator of $\bar{Y}$.
Further, the sampling variance which is obtained by averaging the
squares of errors given in column (7) works out to be 14.55, verifying
that $V(\bar{y}) = 3\sigma^{2}/8( = 3S^{2}/10)$.\
(b) Since the sample variance $(s^{2})$ is given by
$(y_{1} - y_{2})^{2}/2$, which can be obtained easily, the average of 10
sample mean squares gives $E(s^{2})$.\
Here, $E(s^{2}) = 485/10 = 48.5$. Also, the population mean square
$= 48.5$. Thus, the sample mean square provides an unbiased estimator of
the population mean square $(S^{2})$, verifying that
$E(s^{2}) = S^{2}$.\
(c) An estimator of $V(\bar{y})$ is given by
$v(\bar{y}) = 3(y_{1} - y_{2})^{2}/20$, the values which are given in
column (8) of Table 2.3.2 and may be used here. The expected value of
$v(\bar{y})$, which is the average of the values in the column (8), is
14.55, showing that the estimator is unbiased, i.e.,
$E\lbrack v(\bar{y})\rbrack = V(\bar{y}) = \frac{3}{10}S^{2}$.

**2.4 ESTIMATION OF POPULATION PROPORTION**

Sometimes, the units in the population are classified in two groups: (i)
having a particular characteristic and (ii) not having that
characteristic. For example, a crop field may be irrigated or not
irrigated. If it is irrigated, we say that it possesses the
characteristic, \"irrigation\'. If it is not irrigated, we say that it
does not possess the particular characteristic of irrigation. If we are
interested in estimating the proportion of irrigated fields, the
population of $N$ fields can be defined with variate $y_{i}$ as having
value 1 if the field is irrigated, otherwise zero. If the total number
of irrigated fields be $N_{1}$, out of $N$

$$\sum_{i = 1}^{N}\mspace{2mu} y_{i} = N_{1}$$

Thus,

$$P = \frac{\sum_{}^{}\ y_{i}}{N} = \frac{N_{1}}{N} = \text{proportion of irrigated fields}$$

and

$$\sum_{i = 1}^{N}\mspace{2mu} y_{i}^{2} = N_{1} = NP$$

Thus, the problem of estimating a population proportion becomes that of
estimating a population mean by defining the variate as above. If
$n_{1}$ units out of a random sample of size $n$ possess that
characteristic, the sample proportion is given by $p = n_{1}/n$. Thus

$$\sum_{i = 1}^{n}\mspace{2mu} y_{i} = n_{1} = np$$

Hence, an unbiased estimator of $P$ is given by

$$\widehat{P} = (n_{1}/n) = p\ (2.4.1)$$

**Theorem 2.4.1:** In sampling, wor, the variance of $p$ is given by

$$V(p) = \frac{N - n}{n(N - 1)}PQ = (1 - f)\frac{N}{N - 1}\frac{PQ}{n}\ (2.4.2)$$

where $Q = 1 - P$. The proof is obvious.

**Corollary 1:** In sampling, wr, the variance of $p$ is given by

$$V(p) = \frac{PQ}{n}\ (2.4.3)$$

**Corollary 2:** The variance of $N_{1} = Np$, the estimated total
number of units with some desired characteristic, is given by

$$V(N_{1}) = \frac{N^{2}(N - n)PQ}{n(N - 1)}\ (2.4.4)$$

**Theorem 2.4.2:** In sampling, wor, an unbiased estimator of $V(p)$ is
given by

$$v(p) = (1 - f)\frac{pq}{n - 1}\ (2.4.5)$$

The proof is obvious.

**Corollary 1:** In sampling, wr, an unbiased estimator of $V(p)$ is
given by

$$v(p) = \frac{pq}{n - 1}\ (2.4.6)$$

**Corollary 2:** An unbiased estimate of the variance of $N_{1} = Np$ is
given by

$$v(N_{1}) = \frac{N(N - n)pq}{n - 1} = (1 - f)\frac{N^{2}pq}{n - 1}\ (2.4.7)$$

**Corollary 3:** The coefficient of variation of $p$ is given by

$$CV = \frac{\sqrt{PQ/n}}{P} = \sqrt{\frac{Q}{nP}}\ (2.4.8)$$

**Example 2.4:** A list of 3000 voters of a ward in a city was examined
for measuring the accuracy of age of individuals. A random sample of 300
names was taken, which revealed that 51 citizens were shown with wrong
ages. Estimate the total number of voters having a wrong description of
age in the list and estimate the standard error.\
Here, $N = 3000,n = 300,n_{1} = 51,p = 0.17$\
The estimate of the total number of voters having a wrong description of
age is obtained by

$${\widehat{N}}_{1} = Np = (3000)(0.17) = 510$$

\(i\) If sampling, wr, is considered, the estimate of the standard error
is given by

$$S_{{\widehat{N}}_{1}} = N\sqrt{\frac{pq}{n - 1}} = 3000\sqrt{\frac{(0.17)(0.83)}{299}} = 159.3$$

\(ii\) If sampling, wor, is considered, the estimated standard error is
given by

$$S_{{\widehat{N}}_{1}} = N\sqrt{(1 - f)\frac{pq}{n - 1}} = 3000\sqrt{(1 - 0.10)\frac{(0.17)(0.83)}{299}} = 151.1$$

**2.5 COMBINATION OF UNBIASED ESTIMATORS**

There are situations where the estimates based on several samples will
have to be pooled to get a combined estimate. If
$t_{i}(i = 1,2,\ldots,m)$ are unbiased estimators of a parameter
$\theta$, which are mutually independent, then the pooled estimator

$$T = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu} t_{i}}{m}\ (2.5.1)$$

is also an unbiased estimator of $\theta$. The variance of $T$ is given
by

$$V(T) = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu} V(t_{i})}{m^{2}}\ (2.5.2)$$

and estimate of variance

$$v(T) = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu}(t_{i} - T)^{2}}{m(m - 1)}\ (2.5.3)$$

We shall consider the problem for the following cases:\
(i) Simple random sampling for variables\
(ii) Simple random sampling for attributes

**2.5.1 Simple Random Sampling for Variables**

Let us suppose that ${\bar{y}}_{1},{\bar{y}}_{2},\ldots,{\bar{y}}_{m}$
are the sample means, each of which is drawn independently, with sizes
$n_{1},n_{2},\ldots,n_{m}$. A pooled estimator of all samples is given
by taking\
(i) the arithmetic mean of $m$ estimates

$${\bar{y}}' = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu}{\bar{y}}_{i}}{m}\ (2.5.4)$$

\(ii\) the weighted mean of $m$ estimates

$${\bar{y}}'' = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu} n_{i}{\bar{y}}_{i}}{n}\ (2.5.5)$$

where $n = \sum_{i = 1}^{m}\mspace{2mu} n_{i}$.

**When Sampling is With Replacement Method**

The sampling variances of ${\bar{y}}'$ and ${\bar{y}}''$ are given by

$$V({\bar{y}}') = \frac{1}{m^{2}}\sum_{i = 1}^{m}\mspace{2mu}\frac{\sigma^{2}}{n_{i}}\ (2.5.6)$$

and

$$V({\bar{y}}'') = \frac{\sigma^{2}}{n}\ (2.5.7)$$

Unbiased estimators of $V({\bar{y}}')$ and $V({\bar{y}}'')$ are provided
by

$$v({\bar{y}}') = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu}({\bar{y}}_{i} - {\bar{y}}')^{2}}{m(m - 1)}\ (2.5.8)$$

and

$$v({\bar{y}}'') = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu} n_{i}({\bar{y}}_{i} - {\bar{y}}'')^{2}}{n(n - 1)}\ (2.5.9)$$

It should be noted that the estimate given in relation (2.5.5) is more
efficient than that given in relation (2.5.4) and can be verified by
comparing the variances in both the cases.

**When Sampling is Without Replacement Method**

The sampling variances of ${\bar{y}}'$ and ${\bar{y}}''$ are given by

$$V({\bar{y}}') = \frac{1}{m^{2}}\sum_{i = 1}^{m}\mspace{2mu}(1 - f_{i})\frac{S_{i}^{2}}{n_{i}}\ (2.5.10)$$

and

$$V({\bar{y}}'') \approx \frac{S^{2}}{n}(1 - f)\ (2.5.11)$$

Unbiased estimators of $V({\bar{y}}')$ and $V({\bar{y}}'')$ are provided
by

$$v({\bar{y}}') = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu}(1 - f_{i})s_{i}^{2}}{m^{2}n_{i}}\ (2.5.12)$$

and

$$v({\bar{y}}'') = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu} n_{i}(1 - f_{i})s_{i}^{2}}{n^{2}}\ (2.5.13)$$

The estimators ${\bar{y}}'$ and ${\bar{y}}''$ become identical if the
sample sizes $n_{1},n_{2},\ldots,n_{m}$ are the same.

**2.5.2 Simple Random Sampling for Attributes**

The results obtained in the previous section can be applied to simple
random sampling for attributes also. If $p_{1},p_{2},\ldots,p_{m}$ are
the sample proportions based on $m$ samples of size
$n_{1},n_{2},\ldots,n_{m}$ each of which is drawn independently. A
pooled estimator of all sample is given by taking\
(i) the arithmetic mean of $m$ estimates

$$p' = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu} p_{i}}{m}\ (2.5.14)$$

\(ii\) The weighted mean of $m$ estimates

$$p'' = \frac{\sum_{i = 1}^{m}\mspace{2mu}\mspace{2mu} n_{i}p_{i}}{n}\ (2.5.15)$$

where $n = \sum_{i = 1}^{m}\mspace{2mu} n_{i}$.

**2.6 CONFIDENCE LIMITS**

In order to draw conclusions about the population parameter, confidence
limits are constructed around the sample estimate. If the sample size is
large, the sample mean is normally distributed with mean $\bar{Y}$ and
variance $V(\bar{y})$. Hence, the $100(1 - \alpha)\%$ confidence limits
for the population mean are given by

$$\bar{y} \pm t(\alpha)S_{\bar{y}}$$

where $t(\alpha)$ is the value of the normal variate corresponding to
the given level of confidence.

**Example 2.5:** A simple random sample of 50 plots was selected from a
population of 500 plots to estimate the total yield of a crop. The
sample mean yield per plot was 550 kg with a sample variance
$s^{2} = 111.25$. Estimate the total yield of the crop and set up 95%
confidence limits.\
Here, $N = 500,n = 50,\bar{y} = 550,s^{2} = 111.25$\
The estimated total yield is

$$\widehat{Y} = N\bar{y} = 500 \times 550 = 275,000\text{~kg}$$

The standard error of $\widehat{Y}$ is

$$S_{\widehat{Y}} = N\sqrt{(1 - f)\frac{s^{2}}{n}} = 500\sqrt{\left( 1 - \frac{50}{500} \right)\frac{111.25}{50}} = 500\sqrt{0.9 \times 2.225} = 500 \times 1.418 = 709$$

For 95% confidence, $t(\alpha) = 1.96$. The confidence limits are

$$275,000 \pm 1.96 \times 709 \Rightarrow (273,610,276,390)$$

**2.7 ESTIMATION OF SAMPLE SIZE**

In planning a sample survey for estimating the population parameters,
the important question is how to determine the size of the sample to be
drawn. It can be done by specifying the degree of risk (or precision) in
terms of permissible loss and the level of confidence. Before we discuss
the problem for different sampling methods, let us approach a
generalized solution to the problem of estimation of sample size.

Let $z$ be the amount of error by taking the estimate and let $l(z)$ be
the loss incurred by taking it. For a given sampling method, the theory
will provide us the density function. Thus, the expected value of the
loss for a given sample size is obtained by

$$L(n) = E\lbrack l(z)\rbrack\ (2.7.1)$$

Let us also consider the cost function for a sample of size $n$, denoted
by

$$C(n) = a + cn\ (2.7.2)$$

where $a$ is the over-head cost, and $c$ is the cost per unit in the
sampling method.

By combining relations (2.7.1) and (2.7.2), we get the total loss which
is given by

$$\Phi(n) = L(n) + \lambda C(n)\ (2.7.3)$$

where $\lambda$ is some constant quantity.

Since the purpose in taking the sample is to minimize the total loss,
$n$ should be so chosen that relation (2.7.3) is minimized. By
differentiating $\Phi(n)$ with respect to $n$ and equating
$d\Phi/dn = 0$, the optimum value of $n$ can be determined.

**Example 2.6:** If the loss function due to an error in $\bar{y}$ is
proportional to $|\bar{y} - \bar{Y}|$ and if the total cost of the
survey is $C = a + cn$, show that with simple random sampling, ignoring
fpc, the optimum value of $n$ is $(k\sigma/c\sqrt{2\pi})^{2/3}$, where
$k$ is a constant.\
Here $l(z) = |\bar{y} - \bar{Y}|$\
or $l(z) = k|\bar{y} - \bar{Y}|$\
where $k$ is some constant.\
Thus, it follows that

$$L(n) = kE|\bar{y} - \bar{Y}| = k\sqrt{\frac{2}{\pi}}\frac{\sigma}{\sqrt{n}}$$

\[It is assumed that $\bar{y}$ is distributed
$N(\bar{Y},\sigma/\sqrt{n})$\]\
Hence

$$\Phi(n) = a + cn + k\sqrt{\frac{2}{\pi}}\frac{\sigma}{\sqrt{n}}$$

By differentiation and equating $d\Phi/dn = 0$, we have

$$n = \left( \frac{k\sigma}{c\sqrt{2\pi}} \right)^{2/3}$$

A similar treatment and analysis can be applied to any sampling method
in which the loss function is inversely proportional to $n$ and the cost
function is also a function of $n$. A generalized discussion is given by
Yates (1960), and Raiffa and Schlaifer (1961). Chaudhary (1977) and
Chaudhary and Singh (1979) have discussed a line for sequential methods.
For a classified discussion, a good account of methods is given by
Nordin (1944), Blythe (1945), Deming (1950) and Tippett (1950).

Now let us elaborate the results for the simple random sampling for a
characteristic which can be measured quantitatively. Let the marginal
error permissible in the estimate be $e$, and $(1 - \alpha)$ be the
level of confidence. The sample mean is assumed to be normally
distributed with mean $\bar{Y}$ and variance

$$V(\bar{y}) = \frac{N - n}{Nn}S^{2}$$

Hence,

$$e = t(\alpha)\sqrt{\frac{(N - n)S^{2}}{Nn}}\ (2.7.4)$$

where $t(\alpha)$ is the value of the normal variate corresponding to
given $(1 - \alpha)$, which gives

$$n = \frac{t^{2}S^{2}/e^{2}}{1 + t^{2}S^{2}/(Ne^{2})}\ (2.7.5)$$

\(i\) if fpc is ignored, we have

$$n_{0} = \frac{t^{2}S^{2}}{e^{2}}\ (2.7.6)$$

\(ii\) if fpc is not ignored, we can get the value of $n$ by putting the
value of $n_{0}$ in Eqn. (2.7.5) and we have,

$$n = \frac{n_{0}}{1 + n_{0}/N}\ (2.7.7)$$

**Example 2.7:** A study of sampling methods was conducted in a
population having 500 sampling units. By total count it was obtained
that $\bar{Y} = 49$ and $S^{2} = 44.6$. In a simple random sampling, how
many sampling units should be chosen to estimate $\bar{Y}$ with a
permissible marginal error of 10 per cent and 95 per cent confidence
coefficient, when sampling is done (i) with replacement method (ii)
without replacement method?\
(i) Sampling with replacement - In this case, we can ignore fpc and we
have

$$n_{0} = \frac{t^{2}S^{2}}{e^{2}} = \frac{(1.96)^{2} \times 44.6}{(4.9)^{2}} = 7.136 \approx 8$$

\(ii\) Sampling without replacement - In this case, the fpc cannot be
ignored and we take

$$n = \frac{n_{0}}{1 + n_{0}/N} = \frac{7.136}{1 + 7.136/500} = 7.035 \approx 8$$

Similarly, we can also discuss these results when the sampling units are
classified by the presence or absence of a characteristic. With similar
notions, the sample proportion $p$ may be assumed to be normally
distributed with $P$ and variance $(N - n)P(1 - P)/n(N - 1)$. Hence, the
value of $n$ with a pre-assigned level of precision can be estimated by

$$e = t(\alpha)\sqrt{\frac{(N - n)P(1 - P)}{n(N - 1)}}\ (2.7.8)$$

where $t(\alpha)$ has the same meaning given in relation (2.7.4), which
gives

$$n = \frac{Nt^{2}P(1 - P)/e^{2}}{N - 1 + t^{2}P(1 - P)/e^{2}}\ (2.7.9)$$

\(i\) if fpc is ignored, we have

$$n_{0} = \frac{t^{2}P(1 - P)}{e^{2}}\ (2.7.10)$$

\(ii\) if fpc is not ignored, we get

$$n = \frac{n_{0}}{1 + (n_{0} - 1)/N}\ (2.7.11)$$

**Example 2.8:** In a population of 4000 people who were called for
casting their votes, 50 per cent returned to the polls. Estimate the
sample size to estimate this proportion so that the marginal error is 5
per cent with 95 per cent confidence coefficient, when the sampling is
done (i) with replacement and (ii) without replacement methods.\
(i) Sampling with replacement - In this case, we can ignore fpc and
have,

$$n_{0} = \frac{t^{2}P(1 - P)}{e^{2}} = \frac{(1.96)^{2}(0.5)(0.5)}{0.0025} \approx 385$$

\(ii\) Sampling without replacement - In this case, fpc cannot be
ignored and we have,

$$n = \frac{n_{0}}{1 + (n_{0} - 1)/N} = \frac{385}{1 + 384/4000} = 352$$

**SET OF PROBLEMS**

**2.1** Suppose, in a list of $N$ factories serially numbered, $m$
factories have gone out of existence and $n$ new factories have been
added to the list making the total number of factories $(N - m + n)$.
Give a simple procedure for selecting one factory with equal probability
from $(N - m + n)$ factories, avoiding renumbering of the original $N$
factories and show that your procedure achieves equal probability for
new factories.

**2.2** With the help of random numbers, draw random samples, each of
size 5, from the following:\
(i) Cauchy\'s population:

$$f(x) = \frac{1}{\pi}\frac{\lambda}{\lambda^{2} + (x - \mu)^{2}}$$

where $- \infty < x < \infty$ and $\lambda = 3.8$ cm and $\mu = - 2.1$
cm\
(ii) Normal population:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}exp\left\{ - \frac{(x - \mu)^{2}}{2\sigma^{2}} \right\}\  - \infty < x < \infty$$

$\mu = 8$ and $\sigma = 2$\
(iii) Bivariate normal population in which the means of two variates,
$x$ and $y$, are 68 cm and 170 kg, respectively; the s.d\'s of $x$ and
$y$ are 3 cm and 7 kg, respectively; and the correlation coefficient
$\rho$ is (i) $+ 1$ (ii) 0 and (iii) $- 1$.

**2.3** The following procedure has been used for selecting a sample of
fields for crop-cutting experiments on paddy:\
Against the name of each selected village are shown three random numbers
smaller than the highest survey number. These random numbers correspond
to three paddy fields for crop-cutting experiments. If the selected
survey number does not grow paddy, select the next paddy growing survey
number in its place.\
Examine whether the above method will provide an equal chance of
inclusion in the sample to all the paddy-growing survey numbers in the
village, given the following:\
(i) Name of the village: Payagpur\
(ii) Total number of survey numbers: 299\
(iii) Random numbers: 28, 189, 269\
(iv) Paddy-growing survey numbers: 39 to 88 and 189 to 299\
Show that the survey number 39 has a chance of $39/299$ of being
included in the sample, the survey number 189 a chance of $101/299$,
while the remaining survey numbers have a chance of only $1/299$ each.
(I.C.A.R., 1951)

**2.4** A population contains $N$ units, the variate value of one unit
being known to be $y_{0}$. A random sample, wor, is drawn from the
remaining $(N - 1)$ units. Show that the estimator
$\bar{y} + (N - 1)y_{0}$ has a smaller variance than $N\bar{y}$ based on
a random sample, wor, of size $n$ taken from the whole population.

**2.5** (i) Define simple random sampling. Is the sample mean a
consistent and unbiased estimator of the population mean? Give the
variance of the sample mean and also unbiased estimate of this variance.
What is the sample size required to estimate the population mean with a
given standard error?\
(ii) Also, if $n_{1}$ of the units in the sample are of type A, give an
unbiased estimate of the proportion of units of type A in the population
and derive its sampling variance and estimate. If the sample size is
sufficiently large, write 95% confidence limits for the unknown
proportion of units of type A in the population.

**2.6** Suppose $\nu$ distinct units occur in a sample of $n$ units
selected with equal probability with replacement from a population of
$N$ units. Show that the estimator
$\frac{N}{n}\sum_{i = 1}^{\nu}\mspace{2mu}\frac{y_{i}}{\pi_{i}}$ is
unbiased for the population mean. Obtain an unbiased estimator of the
variance of this estimator.

**2.7** From a random sample of $n$ units, a random sub-sample of $m$
units is drawn without replacement and added to the original sample.
Show that the mean based on $(n + m)$ units is an unbiased estimator of
the population mean, and that ratio of its variance to that of the mean
of the original $n$ units is approximately $(1 + 3m/n)/(1 + m/n)^{2}$,
assuming that the population size is large.

**2.8** Derive the expression for variance of a simple random sample
drawn without replacement from a finite population. $N$ balls, placed in
a lot container, are drawn at random from a supply of $Mp$ red and $Mq$
white balls. Then a sample of $n$ balls is drawn at random from the lot
container and placed in a sample container. It is found that, out of
these $n$ balls, $r$ are red. Find the $V(r)$ when the $N$ balls are put
into the lot container (i) with replacement and (ii) without
replacement.

**2.9** In simple random sampling, the variance of the sample mean is
given by
$V(\bar{y}) = N^{2}(1/n - 1/N)\frac{\sum_{}^{}\ y_{i}^{2} - N{\bar{y}}^{2}}{N - 1}$.
Denoting an unbiased estimator of $V(\bar{y})$ by $v$ and noting that
$E\left\lbrack \frac{N}{n}\sum_{}^{}\ y_{i}^{2} \right\rbrack = \sum_{}^{}\ y_{i}^{2}$,
show that

$$E(v) = \frac{1}{N - 1}E\left\lbrack \frac{N - n}{n}\left( \frac{N}{n}\sum_{}^{}\ y_{i}^{2} - N({\bar{y}}^{2} - v) \right) \right\rbrack$$

**2.10** The yields in quintals for wheat crop of 100 villages in a
certain tehsil are given below. (The figures within brackets indicate
the village numbers).\
(i) Select simple random samples of size 20 and 25 units and estimate
the average yield per plot along with their standard errors on the basis
of selected units.\
(ii) Set up 95 per cent confidence interval and comment.\
(iii) Obtain the size of the sample required for estimating the mean
yield with 5 per cent standard error.

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

**2.11** Material for the construction of 5000 wells was issued during
the year 1964 in a district as part of the Grow-More-Food Campaign in
India. The list of cultivators to whom it was issued together with the
proposed location of each well is available. It is proposed to estimate
the proportion $p$ of wells actually constructed and used for irrigation
purpose. The sample is proposed to be selected by simple random
sampling. Determine the size of the sample for values of $P$ ranging
from 0.5 to 0.9, if the permissible margin of error is 10 per cent and
the degree of assurance desired is 95 per cent.

**2.12** The data given below pertain to one complete lactation of milk
yield (in 10 kg) of 250 cows in an organised dairy farm.\
(i) Select a simple random sample of size 25.\
(ii) Estimate the mean with its standard error.\
(iii) Construct a 95 per cent confidence limit for population mean.

  -----------------------------------------------------------
  230   293   163   290   200   173   194   322   169   230
  ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
  297   151   248   271   259   214   167   207   240   286

  184   248   327   338   165   177   270   177   202   155

  155   293   190   172   150   319   151   118   213   114

  186   167   129   185   231   199   265   306   173   276

  291   231   205   220   246   239   186   299   233   208

  265   204   300   195   239   173   237   282   221   218

  197   215   213   290   146   232   305   184   149   267

  188   219   171   99    329   199   180   225   257   202

  189   207   792   327   201   300   206   199   299   153

  175   287   277   230   258   137   174   301   260   282

  211   212   284   214   283   139   223   212   207   224

  207   111   272   192   127   303   221   187   309   263

  203   176   233   239   176   218   193   243   236   275

  288   198   241   219   167   193   234   179   126   173

  279   178   275   260   191   174   235   338   242   238

  211   187   184   189   305   221   253   225   327   203

  195   158   156   185   170   271   160   188   165   218

  312   143   267   298   196   139   205   298   238   217

  145   201   313   230   185   166   147   223   271   133

  155   230   287   329   265   150   286   271   268   198

  214   231   163   335   198   270   187   174   163   201

  192   247   247   297   178   240   290   234   170   227

  230   353   170   159   236   181   230   240   212   242

  151   158   253   179   263   158   250   226   246   301
  -----------------------------------------------------------

**2.13** The frequency distribution of 232 cities in a country, by
population size (000), is given below:

  --------------------------------------------------------------------------
  Population     No. of    Population     No. of    Population     No. of
  size class     cities    size class     cities    size class     cities
  -------------- --------- -------------- --------- -------------- ---------
  50-75          81        500-550        2         1800-1850      1

  75-100         45        550-600        3         1850-1950      0

  100-150        42        600-650        1         1950-2000      1

  150-200        14        650-700        1         2000-2050      0

  200-250        9         700-750        0         2050-2100      1

  250-300        5         750-800        1         2100-3600      0

  300-350        6         800-850        2         3600-3650      1

  350-400        5         850-900        1         3650-7850      0

  400-450        5         900-950        2         7850-7900      1

  450-500        2         950-1800       0                        
  --------------------------------------------------------------------------

**REFERENCES**

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
