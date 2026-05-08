**1. BASIC CONCEPT OF SAMPLE SURVEYS**

**1.1 INTRODUCTION**

As Deming (1950) so succinctly puts it:

*\"Sampling is not mere substitution of a partial coverage for a total
coverage. Sampling is the science and art of controlling and measuring
reliability of useful statistical information through the theory of
probability.\"*

The enumeration of population by sampling methods, proposed by Laplace
in 1783, came into widespread use only by the mid-thirties of this
century. From the outset, some basic questions arose:

\(i\) How should the observations be made?\
(ii) How many observations should be made?\
(iii) How should the total sample be made?\
(iv) How should the data thus obtained be analysed?

The answers to these questions were sought and, in the process, a number
of different techniques and methods were developed. These methods were
tested to determine whether the above mentioned questions were
adequately answered or not. In course of time, the concept of
generalization through the introduction of inductive logic, i.e.
proceeding from the part to the whole, caught the attention of
statisticians engaged in developing suitable techniques of sampling. In
this context a related question cropped up, viz. how should this
generalization be made? The answer to this question was sought with the
help of the technique of probability. Thus the concept of probability
sampling originated. The use of probability in sampling theory came to
be recognised as a reliable tool in drawing inferences about the
populations, whether finite or not.

In traditional applications the experimenter assumes some kind of
probability structure with the observations, while in sample surveys he
introduces the probability element by adopting the technique of
randomization. The idea of probability structure in planned experiments
was originally given by Fisher (1935) who showed that deliberately
introduced randomization in the selection of a part from the whole
provides a valid method of obtaining an estimate of the amount of error
committed. He demonstrated practically that the randomization not only
gives a procedure for valid selection of the part from the whole, but
also gives an expression to the amount of risk committed in doing so.
Thus, the problem was reduced to determining the methods for selection
and estimation, which would minimize the risk involved. Mahalanobis
(1944) introduced another important concept- that of cost function. The
problem was considered to be one of finding the combinations of
selection and estimation procedures which would minimize the cost
function.

**1.2 FIELDS OF APPLICATION OF SAMPLING TECHNIQUES AND LIMITATIONS**

The main objective of this work is to present the theory and techniques
of sample surveys with their application in different types of problems
in the field. Sample surveys are to be widely used as a means of
collecting information to meet a definite need in government, industry
and trade, physical and life sciences and technology, social,
educational and economical problems, etc. The sample survey technique is
now commonly used for obtaining information on various social and
economic activities of society. All walks of life are covered by sample
surveys. It is not possible to include the full range of applications in
this work. However, some specific situations in which sampling
techniques can successfully be employed have been given:

\(i\) When results with maximum accuracy or reliability with a fixed
budget, or with the minimum number of units with a specified degree of
reliability are required.\
(ii) When the units under investigation show considerable variation for
the characteristic under study.\
(iii) When a total count of the population is not possible or is very
costly or destructive.\
(iv) When the scope of the investigation is very wide and the population
is not completely known.\
(v) When time, money and other resources are limited.

Sampling theory has its own limitations which may be briefly outlined as
follows:

\(i\) In spite of the fact that a proper choice of design is employed, a
sample does not fully cover the parent population and consequently
results are not exact.\
(ii) Sampling theory and its application in the field need the services
of trained and qualified personnel without whom results of sample
surveys are not dependable.\
(iii) The planning and execution of sample surveys should be done very
carefully, or the data may provide misleading results.

**1.3 DEFINITIONS AND PRELIMINARIES**

The following definitions and basic concepts are developed here before
we discuss the details of sampling methods:

We are usually faced with a collection (called population):

$$V = (u_{1},\ldots,u_{N})$$

of the objects, $u_{1},\ldots,u_{N}$ (called units or elements), of
which some property (called characteristic) $y$ is defined for every
unit $u_{i}$.

Sampling theory is mainly concerned with ways of obtaining samples, i.e.
sequences or sets of units taken from $V$, in order to estimate
parameters such as $Y,\bar{Y},\sigma^{2},R$, etc. A useful theory can be
developed on the basis of the theory of probability (it is assumed that
the reader has some knowledge of it). We shall consider a random
experiment, the outcome of which depends on chance. The results of
random experiment will be called sample points and the totality of all
sample points consistent with the method of sampling adopted will be
called the sample space. Every outcome of the experiment is described by
one, and only one, sample point. The method of sampling must also define
the probability $P(s)$ that a particular sample $s$ is drawn such that
$P(s) \geq 0$, and $\sum_{}^{}\ P(s) = 1$.

We shall take as proved a number of standard results in the probability
theory, which will be used in the discussion of sampling theory. Let
there be a random variate $X$ taking the values $x_{i}$ with probability
$p_{i}$ ($i = 1,\ldots,N$). The expected value of $X$ is defined as

$$E(X) = \sum_{i = 1}^{N}\mspace{2mu} p_{i}x_{i} = \bar{X}$$

(We shall be using the notation $\sum_{i}^{}\mspace{2mu} y_{i}$ for
$\sum_{i = 1}^{N}\mspace{2mu} y_{i}$ throughout the text, unless
mentioned otherwise.)

In general, if $\phi(X)$ be a function of $X$, then

$$E\{\phi(X)\} = \sum_{i}^{}\mspace{2mu} p_{i}\phi(x_{i})$$

We shall be using the results contained in the following theorems:

**Theorem 1.1:** If $X$ and $Y$ are two random variates.

$$E(X + Y) = E(X) + E(Y)\ (1.3.1)$$

In a generalized form of $k$ random variates,

$$E\left( \sum_{i}^{}\mspace{2mu}\mspace{2mu} X_{i} \right) = \sum_{i}^{}\mspace{2mu} E(X_{i})\ (1.3.2)$$

A more generalized form can be written as

$$E\left( \sum_{}^{}\ a_{i}X_{i} \right) = \sum_{}^{}\ a_{i}E(X_{i})\ (1.3.3)$$

where $a_{i}(i = 1,\ldots,k)$ are the constants.

**Theorem 1.2:** If $X$ and $Y$ are independent,

$$E(X \cdot Y) = E(X)E(Y)\ (1.3.4)$$

**Theorem 1.3:** The variance of a random variate

$$Z = aX + b$$

where $a$ and $b$ are constants, is given by

$$V(Z) = a^{2}V(X)\ (1.3.5)$$

**Theorem 1.4:** The covariance of $X$ and $Y$ is given by

$$\text{Cov}(X,Y) = E\lbrack XY - E(X)E(Y)\rbrack\ (1.3.6)$$

$$= \rho\lbrack V(X)V(Y)\rbrack^{1/2}$$

where $\rho$ stands for the correlation coefficient of $X$ and $Y$.

**Theorem 1.5:** If $X_{i}$ and $a_{i}$ ($i = 1,\ldots,k$) are $k$
random variates and constants respectively, then

$$V\left( \sum_{i = 1}^{k}\mspace{2mu}\mspace{2mu} a_{i}X_{i} \right) = \sum_{i = 1}^{k}\mspace{2mu} a_{i}^{2}V(X_{i}) + \sum_{i \neq j}^{}\mspace{2mu} a_{i}a_{j}\text{Cov}(X_{i},X_{j})\ (1.3.7)$$

**Theorem 1.6:** If $X$ and $Y$ are independent random variates, then

$$V(XY) = V(X)V(Y) + \lbrack E(X)\rbrack^{2}V(Y) + \lbrack E(Y)\rbrack^{2}V(X)\ (1.3.8)$$

**Theorem 1.7:** The expected value of a random variate $X$ is given by

$$E(X) = E_{Y}\lbrack E(X|Y)\rbrack\ (1.3.9)$$

where $E_{Y}$ stands for the conditional expectation of $X$ for a given
$Y$, and $E_{Y}$ stands for the expectation over the space of $Y$.

**Theorem 1.8:** The variance of a random variate $X$ is the sum of the
expected value of the conditional variance and the variance of the
conditional expected value. Symbolically,

$$V(X) = E_{Y}\lbrack V(X|Y)\rbrack + V_{Y}\lbrack E(X|Y)\rbrack\ (1.3.10)$$

We assume that it is either not feasible or is too time consuming or
expensive to measure $X$ on each unit $u_{i}$, or if performed on all
elements, measurements would be too inexact. We, therefore, select some
of the elements (a sample). Thus, a sampling unit may be taken as a
well-defined and identifiable element or group of elements on which
observations can be made. A collection of such units is usually called
population. A population is said to be finite if the number of units
contained in it is finite. Usually a list has to be prepared or a serial
order has to be given to all units in the population. This creates the
sampling frame. A part or fraction of the population is said to
constitute a sample. The number of units, not necessarily distinct,
included in the sample is known as the sample size. The number of
distinct units in the sample is termed as the effective sample size.

Any function of sample values is called statistic. If it is used to
estimate any parameter it will be called estimator. An estimator is a
random variate and may take different values from sample to sample. The
value the estimator takes on in any particular sample is then its
estimate. The difference between the estimator ($t$) and the parameter
($\theta$) is called error. An estimator ($t$) is said to be unbiased
estimator for the parameter ($\theta$) if

$$E(t) = \theta,$$

otherwise biased. Thus bias is given by

$$E(t - \theta) = B(t)$$

A relative measure of bias is $B(t)/\theta$. The mean of squares of
error taken from $\theta$ is called mean-square error (MSE).
Symbolically,

$$\text{MSE}(t) = E(t - \theta)^{2}$$

The sampling variance of $t$ is defined by

$$V(t) = E\lbrack t - E(t)\rbrack^{2}$$

Obviously,

$$\text{MSE}(t) = E(t - \theta)^{2}$$

$$= E\lbrack\{ t - E(t)\} + \{ E(t) - \theta\}\rbrack^{2}$$

$$= E\lbrack t - E(t)\rbrack^{2} + \lbrack E(t) - \theta\rbrack^{2}$$

$$= V(t) + B^{2}(t)$$

The positive square root of the variance is termed as the standard error
of the estimator. The ratio of the standard error of the estimator to
the expected value of the estimator is known as the relative standard
error.

Given two estimators $t_{1}$ and $t_{2}$ of a parameter, the estimator
$t_{1}$ is said to be more efficient than $t_{2}$, if the mean square
error of $t_{1}$ is less than the mean square error of $t_{2}$. The
relative efficiency of $t_{1}$ as compared to $t_{2}$, which differs in
respect of sample size or sampling method or both, may be defined as the
reciprocal of the ratio of the sampling variances of the estimator given
by both techniques when the same number of units is taken. The relative
efficiency may also be obtained as the ratio of the reciprocals of
sample sizes for both sampling methods when the same type of sampling
units are taken.

In fact, the question here is how to measure accuracy, i.e., to measure
the expected difference between the estimate and the true value. It is
usually measured by efficiency which is inversely proportional to the
mean-square error. Since the true value of the parameter is generally
unknown, the efficiency may be measured in terms of precision, i.e. the
expected difference of the estimate from its expected value. Thus,
precision of an estimator is inversely proportional to its sampling
variance.

**1.4 CENSUS AND SAMPLE SURVEYS, ADVANTAGES AND DISADVANTAGES**

The total count of all units of the population for a certain
characteristic is known as complete enumeration, also termed census
survey. The money, manpower and time required for carrying out complete
enumeration will generally be large and there are many situations with
limited means where complete enumeration will not be possible. There are
also instances where it is not practicable to enumerate all units due to
their perishable nature where recourse to selection of a few units will
be helpful. When only a part, called a sample, is selected from the
population and examined, it is called sample enumeration sample survey.

A sample survey will usually be less expensive than a census survey and
the desired information will be obtained in less time. This does not
imply that economy is the only consideration in conducting a sample
survey. It is most important that a degree of accuracy of results is
also maintained. Occasionally, the technique of sample survey is applied
to verify the results obtained from a census survey. It has been
established that in many situations a well-conducted sample survey can
provide much more precise results than a census survey. The relative
merits and demerits of sample surveys vis-a-vis census surveys have been
discussed by Mahalanobis (1950), Yates (1953), Zarkovich (1961) and
Lahiri (1963). Cochran (1977) has very lucidly shown the advantages of
sample surveys over census surveys. In brief, these are:

\(i\) reduced cost of survey,\
(ii) greater speed of getting results,\
(iii) greater accuracy of results,\
(iv) greater scope, and\
(v) adaptability.

Fisher (1950) sums up the merits of sample surveys over census surveys
as follows:

*\"I have made four claims for the sampling procedure. About the first
three, adaptability, speed and economy, I need say nothing further. Too
many examples are already available to show how much the method has to
give in these ways. But, why do I say that it is more scientific than
the only procedure with which it may sometimes be in competition,
complete enumeration? The answer, in my view, lies in the primary
process of designing and enquiry by sampling. Rooted as it is in the
mathematical theory of the errors of random sampling, the idea of
precision is from the first in the forefront. The director of the survey
plans from the first for a predetermined and known level of precision;
it is a consideration of which he never loses sight, and precision
actually attained, subject to well-understood precautions, is manifest
from the results of the enquiry.\"*

Despite the above advantages, sample surveys are not always preferred to
census surveys. Sampling theory has its own limitations and the
advantages of sampling over complete enumeration can be derived only if

\(i\) the units are drawn in a scientific manner\
(ii) an appropriate sampling technique is used, and\
(iii) the size of units selected in the sample is adequate. If
information is required for each unit, census is the only answer.

**1.5 PRINCIPLES OF SAMPLING THEORY**

The main aim of sampling theory is to make sampling more effective so
that the answer to a particular question is given in a valid, efficient
and economical way. The theory of sampling is based on three important
basic principles:

\(i\) Principle of Validity,\
(ii) Principle of Statistical Regularity, and\
(iii) Principle of Optimization.

**Principle of Validity**

This principle states that the sampling design provides valid estimates
about population parameters. By valid we mean that the sample should be
so selected that the estimates could be interpreted objectively and in
terms of probability. Thus, the principle ensures that there is some
definite and pre-assigned probability for each individual in the
sampling design.

**Principle of Statistical Regularity**

The principle of statistical regularity, which has its origin in the
theory of probability, can be explained in these words:

*\"A moderately large number of items chosen at random from a large
group are almost sure on the average to possess the characteristics of
the large group.\"*

This principle stresses upon the desirability and importance of
selecting sample designs where inclusion of sampling units in the sample
is based on probability theory.

**Principle of Optimization**

This principle takes into account the desirability of obtaining a
sampling design which gives optimum results. In other words,
optimization is meant to develop methods of sample selection and of
estimation those provide: (i) a given level of efficiency with the
minimum possible resources or (ii) a given value of cost with the
maximum possible efficiency.

Thus, the principle of optimization minimises the risk or loss of
sampling design, i.e. the principle stresses upon obtaining optimum
results with minimization of the total loss in terms of cost and mean
square error.

**1.6 PRINCIPAL STEPS IN A SAMPLE SURVEY**

Sample survey techniques have now come to be used widely as an organized
and established fact-finding instrument and it is, therefore, essential
to describe briefly the main steps which are involved in a sample
survey. Some of the main steps to be included are given as follows:

\(i\) Statement of objectives\
(ii) Definition of population to be studied\
(iii) Determination of sampling frame and sampling units\
(iv) Selection of proper sampling design\
(v) Organization of field work\
(vi) Summary and analysis of data

**Statement of Objectives**

In a sample survey, the first step is to lay down a clear statement of
objectives of the survey. The user should ensure that these objectives
are commensurate with available resources in terms of money, man-power
and the time limit of the survey.

**Definition of Population**

The population from which the sample is to be drawn should be defined in
clear and unambiguous terms. For example, to estimate the average yield
per plot for a crop, it is necessary to define the size of the plot in
clear terms. The sampled population (population to be sampled) should
coincide with the target population (population about which information
is required). The demographic, geographical, administrative and other
boundaries of the population must be specified so that there remains no
ambiguity regarding the coverage of the survey.

**Determination of Sampling Frame and Sampling Units**

The main requirement of sample surveys is to fix up the sampling frame,
i.e., the list of all sampling units with reference to which relevant
data are to be collected. It is the sampling frame which determines the
sampling structure of a survey. A sampling frame is the key note around
which the selection and estimation procedures revolve. The population
should be capable of division into units which are distinct, unambiguous
and non-overlapping and cover the entire population.

**Selection of Proper Sampling Design**

If an appropriate sampling design is selected, the final estimates will
be quite reliable. The size of the sample, procedure of selection and
estimation of parameters along with the amount of risk involved are some
of the important statistical aspects which should receive careful
attention. If a number of sampling designs for taking a sample is
available, then the total risk, i.e. the cost and precision, should be
considered before making a final selection of the sampling design.

**Organization of Field Work**

The achievement of the aims of a sample survey depends to a large extent
on reliable field work. If field work is done honestly, sincerely and
according to the instructions laid down and if there is careful
supervision of field staff, there remains no doubt about achieving the
aims of the survey. It is, therefore, necessary to make provisions for
adequate supervisory staff for inspection of field work.

**Summary and Analysis of Data**

In a sample survey, the final step of the analysis and drawing
inferences from a sample to a population is a very vital and fascinating
issue. Since the results of the survey are the basis for policy making,
it is the most essential part of the sample survey and should be handled
carefully.\
The analysis of the data collected in a survey may be broadly classified
as follows:

\(i\) Scrutiny and editing of the data\
(ii) Tabulation of data\
(iii) Statistical analysis\
(iv) Reporting and conclusions\
Finally, a report of the findings of the survey, suggesting possible
action to be taken, should be written.

**1.7 PROBABILITY AND NON-PROBABILITY SAMPLING**

The technique of selecting a sample is of fundamental importance in
sampling theory and usually depends upon the nature of the
investigation. The sampling procedures which are commonly used may be
broadly classified under the following heads:

(i) Probability sampling

(ii) \(ii\) Non-probability sampling

**Probability Sampling**

This is the method of selecting samples according to certain laws of
probability in which each unit of the population has some definite
probability of being selected in the sample. It is to be noted here that
there are number of samples of specified types
$S_{1},S_{2},\ldots,S_{k}$ that can be formed by grouping units of a
given population, and each possible sample $S_{i}$ has, assigned to it,
a known probability of selection $p_{i}$. A clear specification of all
possible samples of a given type alongwith their corresponding
probabilities of selection is said to constitute a sampling design. In
subsequent chapters of this book we shall consider only the procedures
of probability sampling.

**Non-Probability Sampling**

This is the method of selecting samples, in which the choice of
selection of sampling units depends entirely on the discretion or
judgement of the sampler. This method is also sometimes called purposive
or judgement sampling. In this procedure, the sampler inspects the
entire population and selects a sample of typical units which he
considers close to the average of the population.

This sampling method is mainly used for opinion surveys, but cannot be
recommended for general use as it is subject to the drawbacks of
prejudice and bias of the sampler. However, if the sampler is
experienced and an expert, it is possible that judgement sampling may
yield useful results. It, however, suffers from a serious defect that it
is not possible to compute the degree of precision of the estimate from
the sample values.

**1.8 SAMPLING UNIT**

A sampling unit has already been defined in the previous section, but it
needs further description as it forms the basis of sampling procedure.
These units may be natural units of the population such as individuals
in a locality, or natural aggregates of such units such as family, or
they may be artificial units such as a farm, etc. Before selecting the
sample, the population must be divided into units which are distinct,
unambiguous and non-overlapping, such that every element (smallest
component part in which a population can be divided) of the population
belongs to one and only one sampling unit. Since the collection of all
sampling units of a specified type constitutes a population, the
sampling units should be so specified that each and every element in the
population occurs just in one sampling unit. Otherwise, some of the
elements will not be included in any sample. For example, if the
sampling unit is a family, it should be so defined that an individual
does not belong to two different families nor should it leave out any
individuals belonging to it.

**1.9 SAMPLING FRAME**

As defined earlier, a complete list of sampling units which represents
the population to be covered is called the sampling frame popularly
known as frame. The construction of a sampling frame is sometimes one of
the major practical problems. Generally, it is assumed that a frame is
perfect if it is exhaustive, complete, and up-to-date in respect of
sampling units and character structures. So the frame should always be
made up-to-date and free from errors of omission and duplication of
sampling units. Different aspects of sampling frames have been discussed
by Mahalanobis (1944), Yates (1960), Seal (1962), Hansen, Hurwitz, and
Jabine (1963), Singh (1978) and others. A sampling frame is subject to
several types of defect which may be broadly classified as follows:

\(i\) A frame may be incomplete - When some sampling units of the
population are either completely omitted or included more than once.\
(ii) A frame may be inaccurate - When some of the sampling units of the
population are listed inaccurately or some units which do not actually
exist are included in the list.\
(iii) A frame may be inadequate - When it does not include all classes
of the population which are to be taken in the survey.\
(iv) A frame may be out-of-date - When it has not been updated according
to the exigencies of the occasion, although it was accurate, complete
and adequate at the time of construction.

Lists which have been routinely collected for some purpose are generally
found to be incomplete and inaccurate and often contain unknown amounts
of duplication. Such lists should be carefully examined and scrutinised
to ensure that they are free from all such defects. If they are not
up-to-date they should be made so. A good frame is difficult to
construct, but experience always helps in its construction.

**1.10 DESIDERATA IN PLANNING OF SAMPLE SURVEYS**

The main stages of a survey are planning, data collection and data
processing. Some of the important aspects involved in the planning and
execution of a sample survey may be classified under the following
heads:

**Specification of Data Requirements**

When specifying the data requirements, the sampler should always include
the following points:\
(i) Statistical statement of the desired information\
(ii) Clear specification of the domain of study\
(iii) Form of data which are to be collected and limitations of budget\
(iv) Degree of precision aimed at

**Survey Reference and Reporting Periods**

From the operational point of view, it is desirable to decide about
these periods well in advance. The survey period is the time period
during which the required data are collected. It is advisable to divide
the survey period into shorter sub-periods to ensure an even
representation of the sample. The reference period is the time period to
which the data information should refer. It depends on the objective of
the survey. For different items there may be different reference
periods. The reporting period is the time period for which the
information is collected for a unit and is determined by the nature and
condition of the survey. For technical considerations there may be
different reporting periods for different items, but from the
operational point of view it is desirable to use the same reference
period for all items as far as possible.

**Preparation of Sampling Frame**

Since the sampling frame decides the structure of the survey and its
design, it is necessary to pay adequate attention to the preparation of
an up-to-date and accurate sampling frame. Even if some resources are to
be spent on such work, it will be worthwhile.

**Choice of Sampling Design**

A decision about an optimum sampling design, after taking the various
technical, operational and risk factors into consideration, plays a very
significant part. The principle of optimization should always be kept in
mind, i.e. to achieve\
(i) either a given degree of precision with a minimum cost, or\
(ii) the maximum possible precision with a fixed cost.

**Method of Data Collection**

The planning and execution of a survey is influenced to a large extent
by the method of data collection. After a very careful examination of
the frame, design, budget and objectives of the survey, a decision
should be taken regarding the choice of method of data collection, i.e.
to collect primary data or to use secondary data. In case the primary
data is to be collected, a clear-cut mode of collection should be given
as to whether data are to be collected by personal interview, mail
enquiry, physical measurement, etc. To maintain uniformity, it is
necessary to give detailed field instructions.

**Field Work and Training of Personnel**

It is essential that the personnel should be thoroughly trained in
locating sample units and the methods of collection of required data,
before starting field work. The staff should be trained well, not only
in the statistical aspects but also in the art of eliciting correct
information from different sources.

**Processing of Survey Data**

Processing of the collected data in a survey may be broadly classified
under the following heads:\
(i) Scrutiny and editing of data\
(ii) Tabulation of data\
(iii) Statistical analysis\
It is, therefore, necessary to plan the survey work in such a way that
the flow of work-material through various stages of data processing
ensures the desired degree of precision in survey results.

**Preparation of Reports**

The guidelines, as formulated by the United Nations (1949), for
preparation of sample-survey reports should be adequate for the purpose.
The report may have sections such as objectives; scope; subject
coverage; method of data collection; survey reference and reporting
periods; sampling design and estimation procedure, tabulation procedure;
presentation of results; accuracy; cost structure; responsibility; and
references. It may be useful to give a summary of the main results which
can be used by the financing agency for policy decisions.

**1.11 SAMPLING AND NON-SAMPLING ERRORS**

The errors involved in collection, processing and analysis of the data
in a survey may be classified as:\
(i) Sampling error, and\
(ii) Non-sampling error

**Sampling Error**

The error which arises due to only a sample being used to estimate the
population parameters is termed sampling error or sampling fluctuation.
Whatever may be the degree of cautiousness in selecting a sample, there
will always be a difference between the population value (parameter) and
its corresponding estimate.

This error is inherent and unavoidable in any and every sampling scheme.
A sample with the smallest sampling error will always be considered a
good representative of the population. This error can be reduced by
increasing the size of the sample. In fact, the decrease in sampling
error is inversely proportional to the square root of the sample size
and the relationship can be examined graphically as shown in Fig. 1.1.
When the sample survey becomes a census survey, the sampling error
becomes zero.

*\[Fig. 1.1: Relationship of sampling error with sample size.\]*

**Non-Sampling Error**\
Besides sampling error, the sample estimate may be subject to other
errors which, grouped together, are termed non-sampling errors. The main
sources of non-sampling errors are:\
(i) Failure to measure some of the units in the selected sample.\
(ii) Observational errors due to defective measurement technique.\
(iii) Errors introduced in editing, coding and tabulating the results.

In practice, the census survey results may suffer from non-sampling
error although these may be free from sampling error. The non-sampling
error is likely to increase with increase in sample size, while sampling
error decreases with increase in sample size.

**SET OF PROBLEMS**

1.1 Describe the advantages of a sample survey in comparison with a
census survey. Write the circumstances under which census surveys are
preferred to sample surveys.

1.2 Explain what you understand by probability sampling and
non-probability sampling. What are their relative advantages and
disadvantages?

1.3 Draw a schedule for enquiry into the state of employment,
under-employment in the rural sector of India. Justify your definitions
and concepts and elaborate a set of instructions to field workers.

1.4 What are the points which need special attention at the planning
stages of sample surveys? With reference to any suitable example
(preferably surveys actually conducted in India), explain whether these
have been covered or not.

1.5 Define population, sampling unit and sampling frame for conducting
surveys on each of the following subjects. Mention other possible
sampling units, if any, in each case and discuss their relative merits.\
(i) Popularity of family planning among families having more than two
children.\
(ii) Monthly fish-catch along a given stretch of sea coast.\
(iii) Election for a political office with adult franchise.\
(iv) Measurement of the volume of timber available in a forest.\
(v) Annual yield of apple fruit in a hilly district.\
(vi) Labour manpower in the urban area of a state.\
(vii) Study of incidence of lung cancer and heart attacks among the
rural inhabitants of a country.\
(viii) Housing conditions in a rural area.\
(ix) Pre-harvest acreage under a specified crop in a region.\
(x) Study of birth-rate in a district.\
(xi) Study of nutrient contents of food consumed by the residents in a
city.

1.6 You are required to plan a sample survey to study the problem of
indebted-ness among the rural agricultural population in India. Suggest
a suitable survey plan on the following points:\
(i) Sampling unit\
(ii) Sampling frame\
(iii) Method of sampling\
(iv) Method of data collection\
Draft a suitable questionnaire that may be used in this regard.

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
