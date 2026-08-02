# STAT-MDC-101: Bio-Statistics

## Unit-IV: Introduction to Survival Analysis

---

### Learning Objectives

After completing this unit, you should be able to:

- explain what survival analysis is and when it is used;
- understand the meaning of censoring and its types;
- define survival function, hazard function, and cumulative hazard function;
- estimate the survival function using the actuarial and Kaplan-Meier methods;
- explain the idea of total time on test and its use;
- describe basic tests for comparing survival curves;
- define ageing classes IFR, IFRA, NBU, NBUE and their dual classes; and
- state the relationships among these classes.

---

# 4.1 Introduction to Survival Analysis

> Suppose a doctor treats ten cancer patients with a new drug. After six months, some patients die, some are still alive, and one patient shifts to another city and cannot be traced. If we only count the patients who died, we ignore those who are still alive. We also cannot say that the missing patient died. We only know that he survived until he left. This kind of data, where we do not know the exact time of the event for everyone, needs special methods. Survival analysis is the branch of statistics that deals with such data. It is used not only for death but for any event that happens over time, such as recovery, relapse, machine failure, or getting a job.

## What is Survival Analysis?

**Survival analysis** is a set of statistical methods used to study the time until an event of interest occurs. The event may be death, recovery, failure, marriage, or any other change that can be placed in time.

*Example:* A study records how many months cancer patients live after treatment. Another study records how many days a machine works before it breaks down.

## Why is Survival Analysis Different?

Ordinary statistical methods like mean and standard deviation are not suitable for survival data because:

- some individuals have not experienced the event by the end of the study;
- some are lost to follow-up;
- survival times are often not normally distributed; and
- the data are usually skewed, with many short times and a few long times.

## Key Terms

- **Survival time:** The time from the start of the study until the event occurs.
- **Event:** The outcome of interest, such as death, recovery, or failure.
- **Censored observation:** An observation in which the exact survival time is not known.
- **Start point:** The time when follow-up begins, such as the date of diagnosis.
- **Endpoint:** The time when the event occurs or follow-up ends.

## Censoring

**Censoring** happens when we do not know the exact survival time. There are three main types.

### Right Censoring

**Right censoring** is the most common type. It occurs when the event has not happened by the end of the study, or when the individual is lost to follow-up. We know that the person survived at least until the last follow-up date.

*Example:* A patient is still alive when the study ends after two years. We know he survived more than two years, but we do not know the exact time of death.

### Left Censoring

**Left censoring** occurs when we know the event happened before a certain time, but we do not know exactly when.

*Example:* A person tests positive for a disease, but we do not know when the infection actually began.

### Interval Censoring

**Interval censoring** occurs when we know the event happened between two time points, but not the exact time.

*Example:* A patient is checked every six months. The disease is absent at 12 months but present at 18 months. So the disease appeared sometime between 12 and 18 months.

![Diagram 1: Types of Censoring](images/unit4_diagram1_censoring_types.svg)

*Figure 4.1: The three main types of censoring.*

---

# 4.2 Basic Survival Functions

> To study survival data, we use several related functions. The survival function tells us the probability that a person survives beyond a given time. The hazard function tells us the risk of the event happening at a particular time. The cumulative hazard function adds up these risks. These functions are connected, and if we know one, we can find the others.

## Survival Function

The **survival function**, denoted by $S(t)$, is the probability that an individual survives longer than time $t$.

$$
S(t) = P(T > t)
$$

At the start, $S(0) = 1$, because everyone is alive. As time increases, $S(t)$ decreases. In the long run, $S(\infty) = 0$.

*Example:* If $S(5) = 0.70$, it means there is a 70% chance that a person survives more than 5 years.

## Cumulative Distribution Function

The **cumulative distribution function**, $F(t)$, is the probability that the event has occurred by time $t$.

$$
F(t) = P(T \leq t) = 1 - S(t)
$$

*Example:* If $S(5) = 0.70$, then $F(5) = 0.30$. There is a 30% chance that the event occurs within 5 years.

## Probability Density Function

The **probability density function**, $f(t)$, describes how survival times are spread out. It is the derivative of $F(t)$.

$$
f(t) = \frac{d}{dt}F(t) = -\frac{d}{dt}S(t)
$$

## Hazard Function

The **hazard function**, $h(t)$, is the risk of the event happening at time $t$, given that the individual has survived up to time $t$.

$$
h(t) = \frac{f(t)}{S(t)}
$$

*Example:* If $h(t)$ increases with time, it means older items are more likely to fail. This is called positive ageing.

## Cumulative Hazard Function

The **cumulative hazard function**, $H(t)$, is the total risk accumulated up to time $t$.

$$
H(t) = \int_0^t h(u)\, du
$$

It is related to the survival function by:

$$
S(t) = \exp[-H(t)]
$$

*Example:* If $H(5) = 0.30$, then $S(5) = e^{-0.30} \approx 0.74$.

## Relationships Between the Functions

| Given | $S(t)$ | $F(t)$ | $f(t)$ | $h(t)$ |
| --- | --- | --- | --- | --- |
| $S(t)$ | — | $1 - S(t)$ | $-\frac{dS}{dt}$ | $-\frac{d}{dt}\ln S(t)$ |
| $F(t)$ | $1 - F(t)$ | — | $\frac{dF}{dt}$ | $\frac{f(t)}{1 - F(t)}$ |
| $f(t)$ | $\int_t^\infty f(u)\,du$ | $\int_0^t f(u)\,du$ | — | $\frac{f(t)}{\int_t^\infty f(u)\,du}$ |
| $h(t)$ | $\exp[-H(t)]$ | $1 - \exp[-H(t)]$ | $h(t)\exp[-H(t)]$ | — |

---

# 4.3 Life Table or Actuarial Estimator

> Before computers were common, actuaries used life tables to estimate survival probabilities. The method divides time into fixed intervals, such as 0–1 year, 1–2 years, and so on. For each interval, we find the proportion of people who survived through that interval. Then we multiply these proportions to get the overall survival probability. This method is called the actuarial method or life table method.

## Idea of the Actuarial Method

The actuarial method divides the follow-up time into intervals. For each interval, it estimates the conditional probability of surviving that interval given that the person was alive at the start. The overall survival probability is found by multiplying these conditional probabilities.

## Steps

1. Divide the time range into intervals, such as 0–1, 1–2, 2–3 years.
2. For each interval, count:
   - $n_i$ = number at risk at the start of the interval;
   - $d_i$ = number who died in the interval;
   - $c_i$ = number censored in the interval.
3. Adjust for censoring. A common adjustment is to treat each censored person as contributing half the interval. So the effective number at risk is:

$$
n_i' = n_i - \frac{c_i}{2}
$$

4. Estimate the conditional probability of surviving the interval:

$$
\hat{p}_i = 1 - \frac{d_i}{n_i'}
$$

5. Estimate the cumulative survival probability up to the end of the interval:

$$
\hat{S}(t_i) = \hat{p}_1 \times \hat{p}_2 \times \cdots \times \hat{p}_i
$$

## Example

Consider the following data for 100 patients:

| Year | At risk at start | Died | Censored |
| --- | --- | --- | --- |
| 0–1 | 100 | 10 | 5 |
| 1–2 | 85 | 8 | 4 |
| 2–3 | 73 | 6 | 3 |

For year 0–1:

$$
n_1' = 100 - 5/2 = 97.5
$$

$$
\hat{p}_1 = 1 - 10/97.5 = 0.8974
$$

For year 1–2:

$$
n_2' = 85 - 4/2 = 83
$$

$$
\hat{p}_2 = 1 - 8/83 = 0.9036
$$

For year 2–3:

$$
n_3' = 73 - 3/2 = 71.5
$$

$$
\hat{p}_3 = 1 - 6/71.5 = 0.9161
$$

The estimated survival probabilities are:

$$
\hat{S}(1) = 0.8974
$$

$$
\hat{S}(2) = 0.8974 \times 0.9036 = 0.8113
$$

$$
\hat{S}(3) = 0.8113 \times 0.9161 = 0.7433
$$

So about 74% of patients are estimated to survive beyond 3 years.

---

# 4.4 Kaplan-Meier Estimator

> The Kaplan-Meier estimator is a popular method for estimating the survival function. Unlike the actuarial method, it does not use fixed intervals. It uses the exact times at which events occur. It is also called the product-limit estimator because the survival probability is found by multiplying a series of conditional probabilities.

## Idea of the Kaplan-Meier Method

At each time when an event occurs, the Kaplan-Meier estimator updates the survival probability. It multiplies the previous survival probability by the conditional probability of surviving that event time.

## Formula

Suppose events occur at distinct times $t_1, t_2, \ldots, t_k$. Let:

- $d_i$ = number of events at time $t_i$;
- $n_i$ = number of individuals at risk just before time $t_i$.

The Kaplan-Meier estimator is:

$$
\hat{S}(t) = \prod_{t_i \leq t} \left(1 - \frac{d_i}{n_i}\right)
$$

If there are no events up to time $t$, then $\hat{S}(t) = 1$.

## Example

Six patients are followed after surgery. Their survival times in months are: 4, 6, 6, 8, 10+, 12. The "+" sign means the patient was censored at 10 months.

| Time | At risk | Died | Censored | Conditional survival | Cumulative survival |
| --- | --- | --- | --- | --- | --- |
| 0 | 6 | 0 | 0 | — | 1.0000 |
| 4 | 6 | 1 | 0 | 1 - 1/6 = 0.8333 | 0.8333 |
| 6 | 5 | 2 | 0 | 1 - 2/5 = 0.6000 | 0.8333 × 0.6000 = 0.5000 |
| 8 | 3 | 1 | 0 | 1 - 1/3 = 0.6667 | 0.5000 × 0.6667 = 0.3333 |
| 10 | 2 | 0 | 1 | — | 0.3333 |
| 12 | 1 | 1 | 0 | 1 - 1/1 = 0.0000 | 0.0000 |

The estimated survival function is:

$$
\hat{S}(t) = \begin{cases}
1 & \text{if } t < 4 \\
0.8333 & \text{if } 4 \leq t < 6 \\
0.5000 & \text{if } 6 \leq t < 8 \\
0.3333 & \text{if } 8 \leq t < 12 \\
0 & \text{if } t \geq 12
\end{cases}
$$

![Diagram 2: Kaplan-Meier Survival Curve](images/unit4_diagram2_kaplan_meier.svg)

*Figure 4.2: A Kaplan-Meier curve drops at event times and stays flat between them.*

## Actuarial vs Kaplan-Meier

| Feature | Actuarial / Life Table | Kaplan-Meier |
| --- | --- | --- |
| Time intervals | Fixed intervals | Exact event times |
| Censoring adjustment | Uses midpoint assumption | Uses exact risk set |
| Shape | Smooth curve | Step function |
| Best for | Grouped data | Individual event times |

---

# 4.5 Total Time on Test

> The total time on test is a simple idea with many uses. It is the total time that all individuals in the study have been observed. This total can be used to check whether the data follow an exponential distribution. It can also be used to draw a graph called the TTT plot, which helps us understand the ageing behaviour of items.

## Definition

The **total time on test** is the sum of all observed survival times, including both complete and censored observations. It is denoted by TTT.

For a sample of $n$ individuals with observed times $t_1, t_2, \ldots, t_n$, the total time on test is:

$$
TTT = \sum_{i=1}^{n} t_i
$$

If some observations are censored, we still add their observed follow-up times.

*Example:* Four machines are tested. Their failure times are 20, 35, and 50 hours. The fourth machine is still working at 60 hours when the test ends. The total time on test is:

$$
TTT = 20 + 35 + 50 + 60 = 165 \text{ hours}
$$

## TTT Transform

The **TTT transform** is a scaled version of the total time on test. It plots the cumulative observed time against the cumulative number of failures. It helps us see how failures are spread over time.

## Use in Testing Exponentiality

The exponential distribution has a constant hazard rate. This means the risk of failure does not change with time. The TTT plot can be used to test this idea.

- If the TTT plot is a straight line through the origin, the data may follow an exponential distribution.
- If the TTT plot is concave, the hazard is increasing. The items are wearing out.
- If the TTT plot is convex, the hazard is decreasing. The items are improving with age.

*Example:* If light bulbs fail at a constant rate, their TTT plot will be a straight line. If old bulbs start failing more often, the plot will be concave.

---

# 4.6 Tests for Hazard Function and Comparing Survival Curves

> Often we want to compare two treatments. We may ask whether a new drug leads to longer survival than the old drug. Looking at the two Kaplan-Meier curves gives a visual idea, but we also need a statistical test. Two common tests are the log-rank test and the Wilcoxon test.

## Log-Rank Test

The **log-rank test** compares the survival experience of two or more groups. It looks at the number of events observed in each group and compares them with the number expected if the groups had the same survival pattern.

The test statistic is based on the differences between observed and expected events at each event time.

*Interpretation:* A small p-value means the survival curves are significantly different.

*Example:* If the log-rank test gives p < 0.05, we conclude that the new treatment gives different survival times than the old treatment.

## Wilcoxon Test

The **Wilcoxon test** for survival data is similar to the log-rank test, but it gives more weight to early differences between the curves. It is useful when we believe the treatments differ most at the beginning.

*Example:* If two drugs differ mainly in the first few months, the Wilcoxon test may detect this difference better than the log-rank test.

## Choosing a Test

- Use the **log-rank test** when you believe the hazard ratio is roughly constant over time.
- Use the **Wilcoxon test** when you expect early differences to be more important.

---

# 4.7 Ageing Classes of Life Distributions

> Some items become weaker as they grow older. Others become stronger. Ageing classes help us describe this behaviour mathematically. These classes are important in reliability and survival analysis. They tell us whether a new item is better than a used item, or whether the risk of failure increases with age.

![Diagram 3: Hazard Function Shapes](images/unit4_diagram3_hazard_shapes.svg)

*Figure 4.3: Hazard functions can be constant, increasing, or decreasing with time.*

## IFR: Increasing Failure Rate

A distribution is said to be **IFR** if its hazard function $h(t)$ increases with time.

*Meaning:* As an item grows older, its risk of failure increases.

*Example:* Old machines with worn-out parts are more likely to fail.

## IFRA: Increasing Failure Rate Average

A distribution is **IFRA** if the average hazard up to time $t$ is increasing.

*Meaning:* The average risk over time is going up. IFR implies IFRA, but IFRA is a broader class.

## NBU: New Better than Used

A distribution is **NBU** if a new item is more likely to survive than an item that has already been used for some time.

Mathematically:

$$
S(x + t) \leq S(x)S(t)
$$

*Meaning:* The chance that a new item survives $x+t$ time is at least as high as the chance that a used item survives an additional $t$ time.

*Example:* A new car tyre is more reliable than a tyre that has already run 20,000 km.

## NBUE: New Better than Used in Expectation

A distribution is **NBUE** if the expected remaining life of a new item is at least as large as the expected remaining life of a used item.

*Meaning:* On average, a new item will last longer than a used item.

## Dual Classes

For each positive ageing class, there is a dual negative ageing class.

| Positive Ageing | Meaning | Dual Class | Meaning |
| --- | --- | --- | --- |
| IFR | Increasing failure rate | DFR | Decreasing failure rate |
| IFRA | Increasing failure rate average | DFRA | Decreasing failure rate average |
| NBU | New better than used | NWU | New worse than used |
| NBUE | New better than used in expectation | NWUE | New worse than used in expectation |

- **DFR:** The hazard decreases with time. Items improve with age.
- **NWU:** A used item is better than a new item.
- **NWUE:** The expected remaining life of a used item is at least as large as that of a new item.

## Hierarchy of Classes

The positive ageing classes are related as follows:

$$
IFR \Rightarrow IFRA \Rightarrow NBU \Rightarrow NBUE
$$

This means every IFR distribution is also IFRA, every IFRA distribution is also NBU, and every NBU distribution is also NBUE.

Similarly, for negative ageing:

$$
DFR \Rightarrow DFRA \Rightarrow NWU \Rightarrow NWUE
$$

![Diagram 4: Hierarchy of Ageing Classes](images/unit4_diagram4_ageing_classes.svg)

*Figure 4.4: The hierarchy of positive and dual ageing classes.*

## Properties

- The exponential distribution is the boundary case. It is both IFR and DFR because its hazard is constant.
- The classes are useful in reliability theory to decide maintenance policies.
- IFR and NBU distributions are used to model ageing and wear-out.
- DFR and NWU distributions are used to models where items improve with use.

---

# 4.8 Solved Examples

## Example 1: Censoring Type

A patient joins a cancer study on 1 January 2023. On 1 July 2023, the patient is still alive but moves to another city. What type of censoring is this?

**Solution:**

This is **right censoring**. We know the patient survived at least six months, but we do not know the exact survival time.

## Example 2: Survival and Hazard Relationship

If $S(t) = e^{-0.2t}$, find the hazard function.

**Solution:**

For the exponential distribution:

$$
S(t) = e^{-\lambda t}
$$

where $\lambda = 0.2$. The hazard function is:

$$
h(t) = \frac{f(t)}{S(t)} = \lambda = 0.2
$$

So the hazard is constant at 0.2.

## Example 3: Kaplan-Meier Estimate

Five patients are followed after a heart attack. Their survival times in months are: 2, 4, 4, 6+, 8. Calculate the Kaplan-Meier survival probabilities.

**Solution:**

| Time | At risk | Died | Censored | Conditional survival | Cumulative survival |
| --- | --- | --- | --- | --- | --- |
| 2 | 5 | 1 | 0 | 1 - 1/5 = 0.8000 | 0.8000 |
| 4 | 4 | 2 | 0 | 1 - 2/4 = 0.5000 | 0.8000 × 0.5000 = 0.4000 |
| 6 | 1 | 0 | 1 | — | 0.4000 |
| 8 | 1 | 1 | 0 | 1 - 1/1 = 0.0000 | 0.0000 |

So $\hat{S}(t) = 0.80$ for $2 \leq t < 4$, $0.40$ for $4 \leq t < 8$, and $0$ for $t \geq 8$.

## Example 4: Total Time on Test

Three bulbs fail at 100, 150, and 200 hours. Two bulbs are still working at 250 hours when the test stops. Find the total time on test.

**Solution:**

The observed times are 100, 150, 200, 250, and 250 hours.

$$
TTT = 100 + 150 + 200 + 250 + 250 = 950 \text{ hours}
$$

## Example 5: Ageing Class

The hazard function of a machine increases with time. Which ageing class does it belong to?

**Solution:**

Since the hazard increases with time, the distribution is **IFR** (Increasing Failure Rate).


---

# 4.9 Chapter End Exercises and Self-Assessment Bank

## Part A: Multiple Choice Questions (20 MCQs)

**1. Survival analysis is used when the outcome variable is:**

&nbsp;&nbsp;&nbsp;&nbsp;a) A category like male or female  
&nbsp;&nbsp;&nbsp;&nbsp;b) The time until an event occurs  
nbsp;&nbsp;&nbsp;&nbsp;c) A single measurement at one point  
&nbsp;&nbsp;&nbsp;&nbsp;d) A percentage only

*Correct Answer:* **b** — Survival analysis studies time-to-event data.

**2. Right censoring occurs when:**

&nbsp;&nbsp;&nbsp;&nbsp;a) The event happened before the study began  
&nbsp;&nbsp;&nbsp;&nbsp;b) The event has not happened by the end of follow-up  
&nbsp;&nbsp;&nbsp;&nbsp;c) The exact event time is known  
&nbsp;&nbsp;&nbsp;&nbsp;d) The study is too short

*Correct Answer:* **b** — Right censoring means the event is not yet observed.

**3. The survival function S(t) gives:**

&nbsp;&nbsp;&nbsp;&nbsp;a) The probability that the event occurs before time t  
&nbsp;&nbsp;&nbsp;&nbsp;b) The probability that survival time is exactly t  
&nbsp;&nbsp;&nbsp;&nbsp;c) The probability of surviving beyond time t  
&nbsp;&nbsp;&nbsp;&nbsp;d) The number of deaths up to time t

*Correct Answer:* **c** — $S(t) = P(T > t)$.

**4. The hazard function is the:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Total risk up to time t  
&nbsp;&nbsp;&nbsp;&nbsp;b) Instantaneous risk of the event at time t  
&nbsp;&nbsp;&nbsp;&nbsp;c) Probability of surviving exactly t years  
&nbsp;&nbsp;&nbsp;&nbsp;d) Number of censored observations

*Correct Answer:* **b** — The hazard is the instantaneous failure risk.

**5. The cumulative hazard function H(t) is related to S(t) by:**

&nbsp;&nbsp;&nbsp;&nbsp;a) $S(t) = H(t)$  
&nbsp;&nbsp;&nbsp;&nbsp;b) $S(t) = 1 - H(t)$  
&nbsp;&nbsp;&nbsp;&nbsp;c) $S(t) = \exp[-H(t)]$  
&nbsp;&nbsp;&nbsp;&nbsp;d) $S(t) = \log[H(t)]$

*Correct Answer:* **c** — $S(t) = e^{-H(t)}$.

**6. The actuarial method divides time into:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Exact event times  
&nbsp;&nbsp;&nbsp;&nbsp;b) Fixed intervals  
nbsp;&nbsp;&nbsp;&nbsp;c) Random intervals  
&nbsp;&nbsp;&nbsp;&nbsp;d) Single point

*Correct Answer:* **b** — The actuarial method uses fixed intervals.

**7. The Kaplan-Meier estimator is also called the:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Maximum likelihood estimator  
&nbsp;&nbsp;&nbsp;&nbsp;b) Product-limit estimator  
nbsp;&nbsp;&nbsp;&nbsp;c) Moment estimator  
&nbsp;&nbsp;&nbsp;&nbsp;d) Interval estimator

*Correct Answer:* **b** — Kaplan-Meier is the product-limit estimator.

**8. In the Kaplan-Meier method, the survival curve is:**

&nbsp;&nbsp;&nbsp;&nbsp;a) A smooth straight line  
&nbsp;&nbsp;&nbsp;&nbsp;b) A step function  
nbsp;&nbsp;&nbsp;&nbsp;c) A circle  
nbsp;&nbsp;&nbsp;&nbsp;d) A parabola

*Correct Answer:* **b** — It drops at event times and stays flat between them.

**9. The total time on test is:**

&nbsp;&nbsp;&nbsp;&nbsp;a) The time until the first failure  
&nbsp;&nbsp;&nbsp;&nbsp;b) The sum of all observed survival times  
nbsp;&nbsp;&nbsp;&nbsp;c) The maximum survival time  
nbsp;&nbsp;&nbsp;&nbsp;d) The average survival time

*Correct Answer:* **b** — TTT is the sum of all observed times.

**10. A straight-line TTT plot suggests:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Increasing hazard  
nbsp;&nbsp;&nbsp;&nbsp;b) Constant hazard  
nbsp;&nbsp;&nbsp;&nbsp;c) Decreasing hazard  
nbsp;&nbsp;&nbsp;&nbsp;d) No data

*Correct Answer:* **b** — A straight TTT plot suggests exponential data.

**11. The log-rank test is used to:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Estimate the hazard function  
nbsp;&nbsp;&nbsp;&nbsp;b) Compare survival curves of two or more groups  
nbsp;&nbsp;&nbsp;&nbsp;c) Find the mean survival time  
nbsp;&nbsp;&nbsp;&nbsp;d) Draw a histogram

*Correct Answer:* **b** — The log-rank test compares survival curves.

**12. IFR stands for:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Increasing Failure Rate  
nbsp;&nbsp;&nbsp;&nbsp;b) Increasing Final Rate  
nbsp;&nbsp;&nbsp;&nbsp;c) Integrated Failure Rate  
nbsp;&nbsp;&nbsp;&nbsp;d) Instantaneous Failure Ratio

*Correct Answer:* **a** — IFR means Increasing Failure Rate.

**13. If the hazard function decreases with time, the distribution is:**

&nbsp;&nbsp;&nbsp;&nbsp;a) IFR  
nbsp;&nbsp;&nbsp;&nbsp;b) DFR  
nbsp;&nbsp;&nbsp;&nbsp;c) NBU  
nbsp;&nbsp;&nbsp;&nbsp;d) NBUE

*Correct Answer:* **b** — Decreasing failure rate means DFR.

**14. NBU means:**

&nbsp;&nbsp;&nbsp;&nbsp;a) New Better than Used  
nbsp;&nbsp;&nbsp;&nbsp;b) New Before Use  
nbsp;&nbsp;&nbsp;&nbsp;c) Normal Better than Used  
nbsp;&nbsp;&nbsp;&nbsp;d) Not Better than Used

*Correct Answer:* **a** — NBU means New Better than Used.

**15. The dual class of IFR is:**

&nbsp;&nbsp;&nbsp;&nbsp;a) NBU  
nbsp;&nbsp;&nbsp;&nbsp;b) DFR  
nbsp;&nbsp;&nbsp;&nbsp;c) NBUE  
nbsp;&nbsp;&nbsp;&nbsp;d) IFRA

*Correct Answer:* **b** — The dual of IFR is DFR.

**16. Which class is the broadest among the positive ageing classes?**

&nbsp;&nbsp;&nbsp;&nbsp;a) IFR  
nbsp;&nbsp;&nbsp;&nbsp;b) IFRA  
nbsp;&nbsp;&nbsp;&nbsp;c) NBU  
nbsp;&nbsp;&nbsp;&nbsp;d) NBUE

*Correct Answer:* **d** — NBUE is the broadest class.

**17. The exponential distribution has:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Increasing hazard  
nbsp;&nbsp;&nbsp;&nbsp;b) Decreasing hazard  
nbsp;&nbsp;&nbsp;&nbsp;c) Constant hazard  
nbsp;&nbsp;&nbsp;&nbsp;d) Zero hazard

*Correct Answer:* **c** — Exponential distribution has constant hazard.

**18. Left censoring means:**

&nbsp;&nbsp;&nbsp;&nbsp;a) The event happened before a known time  
nbsp;&nbsp;&nbsp;&nbsp;b) The event has not yet happened  
nbsp;&nbsp;&nbsp;&nbsp;c) The event is known exactly  
nbsp;&nbsp;&nbsp;&nbsp;d) The person joined late

*Correct Answer:* **a** — Left censoring means the event occurred before observation.

**19. The actuarial method uses which assumption for censored individuals in an interval?**

&nbsp;&nbsp;&nbsp;&nbsp;a) They all die at the start  
nbsp;&nbsp;&nbsp;&nbsp;b) They all survive the interval  
nbsp;&nbsp;&nbsp;&nbsp;c) They are at risk for half the interval  
nbsp;&nbsp;&nbsp;&nbsp;d) They are ignored

*Correct Answer:* **c** — Censored individuals are assumed to contribute half the interval.

**20. The Wilcoxon test for survival data gives more weight to:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Late differences  
nbsp;&nbsp;&nbsp;&nbsp;b) Early differences  
nbsp;&nbsp;&nbsp;&nbsp;c) Censored observations only  
nbsp;&nbsp;&nbsp;&nbsp;d) The largest survival time

*Correct Answer:* **b** — Wilcoxon test is more sensitive to early differences.

## Part B: Fill in the Blanks (20 Questions)

**1.** Survival analysis studies the ________ until an event occurs.

*Answer:* **time**

**2.** When the exact survival time is unknown, the observation is called ________.

*Answer:* **censored**

**3.** The most common type of censoring is ________ censoring.

*Answer:* **right**

**4.** The survival function is denoted by ________.

*Answer:* **S(t)**

**5.** The cumulative distribution function is equal to 1 minus the ________ function.

*Answer:* **survival**

**6.** The hazard function is the ratio of the density function to the ________ function.

*Answer:* **survival**

**7.** The actuarial method is also called the ________ table method.

*Answer:* **life**

**8.** The Kaplan-Meier estimator uses exact ________ times.

*Answer:* **event / failure**

**9.** The Kaplan-Meier survival curve is a ________ function.

*Answer:* **step**

**10.** The total time on test is the ________ of all observed survival times.

*Answer:* **sum**

**11.** A straight-line TTT plot suggests a ________ hazard.

*Answer:* **constant**

**12.** The ________ test is used to compare two survival curves.

*Answer:* **log-rank**

**13.** IFR means ________ Failure Rate.

*Answer:* **Increasing**

**14.** The dual class of NBU is ________.

*Answer:* **NWU**

**15.** NBUE means New Better than Used in ________.

*Answer:* **Expectation**

**16.** The exponential distribution is both IFR and ________.

*Answer:* **DFR**

**17.** The class IFR is ________ than the class NBUE.

*Answer:* **smaller / narrower**

**18.** In the actuarial method, censored individuals are usually assumed to be at risk for ________ the interval.

*Answer:* **half**

**19.** The cumulative hazard function H(t) is the integral of the ________ function.

*Answer:* **hazard**

**20.** If old items are more likely to fail, the distribution shows ________ ageing.

*Answer:* **positive**

## Part C: True / False Statements (20 Questions)

**1.** Survival analysis can only be used for death as the event.

*Statement is:* **False** — It can be used for any time-to-event outcome.

**2.** Right censoring occurs when the event happens after the study ends.

*Statement is:* **True** — We only know the person survived at least until the end.

**3.** The survival function always starts at 0.

*Statement is:* **False** — It starts at 1 because everyone is alive at time 0.

**4.** The hazard function can be greater than 1.

*Statement is:* **True** — Hazard is a rate, not a probability.

**5.** The actuarial method uses exact failure times.

*Statement is:* **False** — It uses fixed time intervals.

**6.** The Kaplan-Meier estimator can handle censored data.

*Statement is:* **True** — It is designed for censored survival data.

**7.** Total time on test ignores censored observations.

*Statement is:* **False** — Censored times are included up to the censoring point.

**8.** The log-rank test compares mean survival times directly.

*Statement is:* **False** — It compares the whole survival experience.

**9.** IFR implies IFRA.

*Statement is:* **True** — Every IFR distribution is also IFRA.

**10.** DFR means the hazard decreases with time.

*Statement is:* **True** — DFR stands for Decreasing Failure Rate.

**11.** NBU means a used item is better than a new item.

*Statement is:* **False** — NBU means new is better than used.

**12.** The exponential distribution belongs to both IFR and DFR classes.

*Statement is:* **True** — Its hazard is constant, so it satisfies both definitions.

**13.** NBUE is a broader class than NBU.

*Statement is:* **True** — NBU implies NBUE.

**14.** Interval censoring means the event time is known exactly.

*Statement is:* **False** — It means the event is known to lie in an interval.

**15.** The Kaplan-Meier curve rises when a death occurs.

*Statement is:* **False** — It drops at death times.

**16.** A concave TTT plot suggests increasing hazard.

*Statement is:* **True** — Concave TTT plot indicates wear-out.

**17.** The Wilcoxon test gives equal weight to all time points.

*Statement is:* **False** — It gives more weight to early differences.

**18.** The survival function and the cumulative distribution function add up to 1.

*Statement is:* **True** — $S(t) + F(t) = 1$.

**19.** The hazard function is also called the force of mortality.

*Statement is:* **True** — It is another name for the hazard function.

**20.** Left censoring is more common than right censoring in medical studies.

*Statement is:* **False** — Right censoring is more common.

## Part D: Matching Type Questions (5 Sets of 4 Items)

### Set 1: Survival Functions

| Column A | Column B |
| --- | --- |
| 1. S(t) | A. Total accumulated risk |
| 2. F(t) | B. Probability of surviving beyond time t |
| 3. h(t) | C. Probability that event occurs by time t |
| 4. H(t) | D. Instantaneous risk of event |

*Answer Key:* **1-B, 2-C, 3-D, 4-A**

### Set 2: Estimation Methods

| Column A | Column B |
| --- | --- |
| 5. Actuarial method | A. Uses fixed time intervals |
| 6. Kaplan-Meier method | B. Uses exact event times |
| 7. Total time on test | C. Sum of observed survival times |
| 8. Log-rank test | D. Compares survival curves |

*Answer Key:* **5-A, 6-B, 7-C, 8-D**

### Set 3: Censoring Types

| Column A | Column B |
| --- | --- |
| 9. Right censoring | A. Event known to be in an interval |
| 10. Left censoring | B. Event not yet observed |
| 11. Interval censoring | C. Event happened before observation |
| 12. Complete data | D. Exact event time known |

*Answer Key:* **9-B, 10-C, 11-A, 12-D**

### Set 4: Ageing Classes

| Column A | Column B |
| --- | --- |
| 13. IFR | A. New better than used |
| 14. DFR | B. Decreasing failure rate |
| 15. NBU | C. Increasing failure rate |
| 16. NBUE | D. New better than used in expectation |

*Answer Key:* **13-C, 14-B, 15-A, 16-D**

### Set 5: Dual Classes

| Column A | Column B |
| --- | --- |
| 17. IFRA | A. New worse than used |
| 18. DFRA | B. New worse than used in expectation |
| 19. NWU | C. Decreasing failure rate average |
| 20. NWUE | D. Increasing failure rate average |

*Answer Key:* **17-D, 18-C, 19-A, 20-B**

## Part E: Subjective and Analytical Questions (10 Questions with Detailed Solutions)

### Q1. What is survival analysis? Give two examples where it can be used.

**Solution:**

Survival analysis is a set of statistical methods used to study the time until an event of interest occurs. It is used when some observations are censored.

Examples:
1. Studying how long cancer patients survive after treatment.
2. Studying how long a machine works before it breaks down.

### Q2. Explain the three types of censoring with examples.

**Solution:**

**Right censoring:** The event has not happened by the end of follow-up. Example: A patient is still alive when the study ends.

**Left censoring:** The event happened before a known time. Example: A person tests positive for a disease, but the exact infection time is unknown.

**Interval censoring:** The event happened between two check-up times. Example: A disease is absent at 6 months but present at 12 months.

### Q3. Define survival function, hazard function, and cumulative hazard function. How are they related?

**Solution:**

- **Survival function:** $S(t) = P(T > t)$, the probability of surviving beyond time $t$.
- **Hazard function:** $h(t) = f(t)/S(t)$, the instantaneous risk of the event at time $t$.
- **Cumulative hazard function:** $H(t) = \int_0^t h(u)\,du$, the total risk up to time $t$.

They are related by $S(t) = \exp[-H(t)]$ and $F(t) = 1 - S(t)$.

### Q4. Describe the actuarial method of estimating survival probability.

**Solution:**

The actuarial method divides time into fixed intervals. For each interval, it calculates the conditional probability of surviving that interval. The effective number at risk is adjusted for censoring by assuming censored individuals are at risk for half the interval. The cumulative survival is found by multiplying the conditional survival probabilities across intervals.

### Q5. Describe the Kaplan-Meier estimator.

**Solution:**

The Kaplan-Meier estimator uses exact event times. At each event time, it multiplies the previous survival estimate by $(1 - d_i/n_i)$, where $d_i$ is the number of events and $n_i$ is the number at risk just before that time. The result is a step function that drops at each event time.

### Q6. What is total time on test? How is it used?

**Solution:**

The total time on test is the sum of all observed survival times, including censored times. It is used to draw the TTT plot. A straight-line TTT plot suggests constant hazard and possible exponential distribution. A concave plot suggests increasing hazard, and a convex plot suggests decreasing hazard.

### Q7. What is the log-rank test? When is it used?

**Solution:**

The log-rank test compares the survival curves of two or more groups. It compares the observed number of events with the expected number of events under the assumption that the groups have the same survival pattern. It is used when we want to test whether treatments or groups differ in survival experience.

### Q8. Define IFR, IFRA, NBU, and NBUE.

**Solution:**

- **IFR:** Increasing Failure Rate; hazard increases with time.
- **IFRA:** Increasing Failure Rate Average; average hazard increases with time.
- **NBU:** New Better than Used; a new item is more likely to survive than a used item.
- **NBUE:** New Better than Used in Expectation; a new item has greater expected remaining life than a used item.

### Q9. State the hierarchy among IFR, IFRA, NBU, and NBUE. What are the dual classes?

**Solution:**

Hierarchy: $IFR \Rightarrow IFRA \Rightarrow NBU \Rightarrow NBUE$.

Dual classes are:
- DFR is dual to IFR.
- DFRA is dual to IFRA.
- NWU is dual to NBU.
- NWUE is dual to NBUE.

### Q10. The survival times of five patients are: 3, 5, 5, 7+, 9. Calculate the Kaplan-Meier survival estimates.

**Solution:**

| Time | At risk | Died | Censored | Conditional survival | Cumulative survival |
| --- | --- | --- | --- | --- | --- |
| 3 | 5 | 1 | 0 | 1 - 1/5 = 0.8000 | 0.8000 |
| 5 | 4 | 2 | 0 | 1 - 2/4 = 0.5000 | 0.8000 × 0.5000 = 0.4000 |
| 7 | 1 | 0 | 1 | — | 0.4000 |
| 9 | 1 | 1 | 0 | 1 - 1/1 = 0.0000 | 0.0000 |

So $\hat{S}(t) = 0.80$ for $3 \leq t < 5$, $0.40$ for $5 \leq t < 9$, and $0$ for $t \geq 9$.

---

# 4.10 Summary

Survival analysis deals with time-to-event data where some observations may be censored. The main functions are the survival function $S(t)$, the cumulative distribution function $F(t)$, the probability density function $f(t)$, the hazard function $h(t)$, and the cumulative hazard function $H(t)$. These functions are mathematically related.

Censoring can be right, left, or interval. Right censoring is the most common.

The survival function can be estimated using the actuarial or life-table method, which uses fixed intervals, or the Kaplan-Meier product-limit method, which uses exact event times.

The total time on test is the sum of observed survival times. It is used in TTT plots to check for exponentiality and ageing behaviour.

The log-rank test and Wilcoxon test are used to compare survival curves between groups.

Ageing classes describe how failure risk changes with time. IFR, IFRA, NBU, and NBUE describe positive ageing. Their dual classes DFR, DFRA, NWU, and NWUE describe negative ageing. The hierarchy is $IFR \Rightarrow IFRA \Rightarrow NBU \Rightarrow NBUE$.

---

# References and Further Reading

- Cox, D.R. and Oakes, D. (1984). *Analysis of Survival Data*. Chapman and Hall.
- Elandt-Johnson, R.C. and Johnson, N.L. *Survival Models and Data Analysis*. Wiley.
- Miller, R.G. (1981). *Survival Analysis*. Wiley.
- Indira Gandhi National Open University. *MST-019: Epidemiology and Clinical Trials* study material. Available through [eGyankosh](https://egyankosh.co.in/books/mst-019).
