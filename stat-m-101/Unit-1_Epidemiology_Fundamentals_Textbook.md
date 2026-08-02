# STAT-MDC-101: Bio-Statistics

## Unit-I: Epidemiology Fundamentals

---

### Learning Objectives

After completing this unit, you should be able to:

- define epidemiology and distinguish it from clinical medicine;
- list and explain the sequential steps used to investigate a disease outbreak;
- calculate and interpret ratios, proportions, rates, prevalence, incidence, mortality rates, and measures of association;
- describe the design, analysis, and interpretation of case-control and cohort studies;
- compute sensitivity, specificity, positive predictive value, and negative predictive value for a screening test;
- identify common biases and confounding in epidemiologic research and suggest ways to control them; and
- apply these concepts to Indian public health situations such as dengue outbreaks, campus mess food poisoning, rural screening camps, and vaccination drives.

---

# 1.1 Introduction to Epidemiology

> Imagine that a single student in your college hostel develops a stomach upset. The doctor examines the student, gives oral rehydration and an antispasmodic, and the student recovers by evening. That is clinical medicine: one patient, one diagnosis, one treatment. But suppose that by the next afternoon, forty students living in Block-A of the same hostel develop vomiting and diarrhoea, while students in Block-B remain perfectly well. Treating each of the forty students is necessary, yet it is not sufficient. Someone must ask why Block-A alone was affected, what was served at breakfast, whether the milk was left uncovered, and how the contaminated food reached only one section of the dining hall. This shift from caring for an individual to understanding the health experience of an entire group is the central purpose of epidemiology. In India, this perspective matters every day — during dengue outbreaks after monsoon showers, when pulse polio teams move through villages, or when a screening van checks rural women for anaemia. Epidemiology gives us the tools to count, compare, and act before more people fall ill.

## Formal Definition of Epidemiology

Epidemiology is the study of the **distribution** and **determinants** of health-related states or events in specified human populations, and the application of this study to the prevention and control of health problems.

The definition has four practical parts:

1. **Study** — systematic collection, analysis, and interpretation of health data.
2. **Distribution** — the pattern of disease with respect to person, place, and time.
3. **Determinants** — the causes, risk factors, or exposures that influence health outcomes.
4. **Application to prevention and control** — using findings to protect community health.

*Example:* Counting tuberculosis cases across districts in Tamil Nadu and noticing that most occur in urban slums is a study of distribution. Investigating overcrowding and poor ventilation as causes is a study of determinants. Providing directly observed treatment is application.

## Epidemiology and Clinical Medicine

Clinical medicine focuses on the diagnosis and treatment of an individual patient. Epidemiology, by contrast, focuses on groups of people and asks why disease occurs in some members of a population but not in others. Both are essential: clinical care heals the sick person, while epidemiology prevents illness in the community.

| Aspect | Clinical Medicine | Epidemiology |
| --- | --- | --- |
| Unit of concern | Individual patient | Population or community |
| Main question | What is wrong with this patient? | Why are people in this group getting sick? |
| Typical action | Diagnose and treat | Investigate, measure, and prevent |
| Example | Treating one child with dengue | Mapping a dengue cluster to remove breeding sites |

## The Triad of Descriptive Epidemiology: Person, Place, and Time

When an outbreak is first reported, three simple questions guide the investigation:

- **Person (Who?)** — age, sex, occupation, immunisation status, diet, and habits. For example, severe dengue is more common in young children and in people with a previous dengue infection.
- **Place (Where?)** — village, urban ward, hostel block, water source, or health facility. A cluster of typhoid cases around a single street vendor points to a common source.
- **Time (When?)** — dates of onset, seasonal patterns, and epidemic curves. Malaria rises after the monsoon, while influenza may peak in winter months.

*Example:* During a cholera outbreak in Odisha, investigators found that cases were clustered around a particular tube well (**place**), affected mostly adults aged 20–40 (**person**), and began three days after a wedding feast (**time**). This pattern directed the control effort to the well and the feast leftovers.

## Applications of Epidemiology

Epidemiology is used to:

- identify the cause of new or recurring diseases;
- measure the burden of disease in a community;
- describe the natural history of illness;
- evaluate the effectiveness of vaccines, drugs, and public health programmes;
- plan health services and allocate resources; and
- monitor trends over time and across regions.

*Example:* The Indian government uses epidemiologic data from the National Family Health Survey to decide where to expand iron and folic acid supplementation programmes for anaemia.

---

# 1.2 Principles of Epidemiologic Investigation

> When several people in a village fall ill with similar symptoms after a community feast, panic spreads quickly. Neighbours blame the weather, the water, or a particular dish. A health worker cannot afford to guess. She must follow a clear, step-by-step method to confirm that an outbreak is truly occurring, find every affected person, describe the pattern of illness, form a sensible explanation, test it with data, stop further cases, and tell the community what happened. This systematic procedure is called an epidemiologic investigation. In India, such investigations have traced cholera to contaminated hand-pumps, food poisoning to sweets distributed at a wedding, and dengue to uncovered water storage tanks. The logic is the same whether the setting is a metropolitan hospital, a college campus, or a remote tribal area: move from suspicion to evidence, and from evidence to action. Mastery of this protocol prepares a biostatistician to serve as a valuable member of any outbreak response team.

## Definition

An **epidemiologic investigation** is a systematic, step-by-step procedure used to identify the source, cause, and mode of transmission of a disease within a population, and to recommend control measures.

## Step-by-Step Protocol for Outbreak Investigation

Public health teams generally follow the protocol described below. The steps overlap in practice, but each has a distinct purpose.

**Step 1. Verify the outbreak and diagnosis.** Confirm that the observed number of cases is higher than the usual baseline for that place and season, and verify the laboratory diagnosis.

*Example:* If a village normally reports two typhoid cases per month and suddenly reports fifteen in one week, an outbreak is likely.

**Step 2. Define a case and count cases.** A **case definition** is a clear set of clinical, laboratory, and time-place criteria used to decide whether a person should be counted as a case. Cases may be classified as suspected, probable, or confirmed. Once the definition is fixed, cases are actively sought in hospitals, clinics, schools, and the community.

*Example:* For a dengue outbreak, a case definition might read: "Any person living in Ward 4 of City X between 1 July and 31 August with fever and either thrombocytopenia or a positive dengue NS1 test."

**Step 3. Search for additional cases.** Active case finding ensures that mild or unreported cases are not missed. This step is important because incomplete counting can distort the epidemic curve and the attack rate.

*Example:* Health workers visiting every household in an affected village may discover children with mild diarrhoea who had not attended the health centre.

**Step 4. Perform descriptive analysis by person, place, and time.** Data are arranged to show who is affected, where cases live or work, and when symptoms began. A graph of cases by date of onset is called an **epidemic curve**. The curve reveals whether the outbreak is due to a single common exposure, person-to-person spread, or ongoing transmission.

*Example:* An epidemic curve that rises sharply and falls within one incubation period suggests a point-source outbreak, such as a single contaminated meal.

**Step 5. Formulate a working hypothesis.** Based on the descriptive pattern, the investigator proposes one or more plausible explanations. For example, if all cases ate paneer from the same hostel mess on a particular morning, contaminated paneer becomes the working hypothesis.

**Step 6. Test and refine the hypothesis.** Analytical study designs such as case-control or cohort studies are used to estimate risk. Statistical measures such as the odds ratio, relative risk, or attack rate ratio help decide whether the hypothesis is supported.

**Step 7. Implement control and prevention measures.** Action should not wait until every analysis is complete. Immediate steps may include removing suspected food, chlorinating water, isolating infectious patients, vaccinating contacts, or issuing health advisories.

*Example:* During a measles outbreak, control measures include vaccinating all children in the affected area and isolating cases for four days after the rash appears.

**Step 8. Evaluate control measures and communicate findings.** The team continues to monitor new cases. If the curve falls, the intervention is working. A final report is prepared for health authorities and the affected community so that similar outbreaks can be prevented.

![Diagram 1: Sequential Steps in an Outbreak Investigation](images/diagram1_outbreak_investigation.svg)

*Figure 1.1: Sequential steps in an epidemiologic outbreak investigation.*

## The Epidemic Curve

An epidemic curve is a histogram showing the number of new cases on the vertical axis and the date of symptom onset on the horizontal axis. Its shape tells the investigator:

- a sharp upward and downward slope suggests a **point-source outbreak**;
- a series of progressively later peaks suggests **person-to-person spread**; and
- a flat, extended plateau suggests a **continuous common source**.

*Example:* In a food-poisoning outbreak at a marriage hall, the epidemic curve may show almost all cases falling within a single 24-hour window, consistent with a common contaminated dish.

## Case Definition

A good case definition includes:

- **Clinical criteria** — symptoms, signs, or severity;
- **Laboratory criteria** — confirmation by test, culture, or imaging; and
- **Time, place, and person restrictions** — the period and population under study.

The definition should be applied uniformly to cases and non-cases. It should be made **before** data collection begins to avoid bias.

---

# 1.3 Basic Epidemiologic and Health Measures

> A newspaper reports that fifty people in City A and fifty people in City B have diabetes. Does this mean both cities face the same health problem? Not at all. If City A has only five hundred residents, then one person in ten has diabetes. If City B has one hundred thousand residents, then only one person in two thousand is affected. Raw numbers hide the size of the population at risk. To make fair comparisons, epidemiologists convert counts into proportions, ratios, and rates. These measures allow a district health officer to compare malaria deaths in Bihar with those in Kerala, or a college doctor to judge whether a hostel outbreak is unusually large. In this section we learn the basic arithmetic of epidemiology. The ideas are simple, but they must be applied with care, because the wrong denominator can change the entire conclusion. Understanding these measures is the first step toward reading health reports and planning public health action with confidence.

## Ratios, Proportions, and Rates

Three fundamental tools are used to express the size and speed of health events.

### Ratio

A **ratio** is a comparison of two separate quantities where the numerator is not included in the denominator.

$$
\text{Ratio} = \frac{\text{Quantity A}}{\text{Quantity B}}
$$

*Example:* If a hospital has 150 doctors and 300 nurses, the doctor-to-nurse ratio is $150/300 = 1:2$.

### Proportion

A **proportion** is a fraction in which the numerator is included in the denominator. It has no units and ranges from 0 to 1, or from 0% to 100% when multiplied by 100.

$$
\text{Proportion} = \frac{\text{Number of events in a group}}{\text{Total number in that group}}
$$

*Example:* If 40 of 200 students in a class are anaemic, the proportion anaemic is $40/200 = 0.20$, or 20%.

### Rate

A **rate** measures how frequently a health event occurs in a defined population over a specified time period. A rate always includes a time element and is usually multiplied by a constant such as 1,000 or 100,000 for easier interpretation.

$$
\text{Rate} = \frac{\text{Number of events in a time period}}{\text{Population at risk during that time period}} \times k
$$

where $k$ is a constant multiplier, usually $1,000$, $100,000$, or $1,000,000$.

*Example:* If a town of 50,000 reports 100 new malaria cases in a year, the annual malaria incidence rate is $(100/50{,}000) \times 1{,}000 = 2$ cases per 1,000 population per year.

## Measures of Disease Frequency: Prevalence and Incidence

### Prevalence

**Prevalence** is the proportion of a population that has a particular disease or condition at a given point or period in time. It includes both old and newly diagnosed cases.

#### Point Prevalence

**Point prevalence** measures existing cases at one specific instant.

$$
\text{Point Prevalence} = \frac{\text{Number of existing cases at a point in time}}{\text{Total population at risk at that same point}} \times k
$$

*Example:* On 1 July 2025, a village of 1,000 residents had 50 people living with diagnosed hypertension. The point prevalence of hypertension was $(50/1{,}000) \times 100 = 5\%$.

#### Period Prevalence

**Period prevalence** measures cases existing at any time during a specified interval.

$$
\text{Period Prevalence} = \frac{\text{Number of cases existing anytime during the period}}{\text{Average or mid-period population at risk}} \times k
$$

*Example:* During the calendar year 2024, a primary health centre recorded 120 people who had tuberculosis at any point. With a mid-year population of 10,000, the period prevalence was $(120/10{,}000) \times 1{,}000 = 12$ per 1,000 population.

### Incidence

**Incidence** measures the number of new cases that develop in a population at risk during a given time period. It tells us how fast the disease is spreading.

#### Cumulative Incidence (Risk)

**Cumulative incidence** is the proportion of healthy individuals at risk who develop the disease over a fixed period. It assumes everyone is followed for the full period.

$$
\text{Cumulative Incidence} = \frac{\text{Number of new cases during the period}}{\text{Number of healthy individuals at risk at the start}} \times k
$$

*Example:* At the start of a year, 800 healthy workers in a textile factory were monitored for asthma. Forty developed asthma during the year. The cumulative incidence was $(40/800) \times 1{,}000 = 50$ cases per 1,000 workers per year.

#### Incidence Density Rate (Person-Time Rate)

**Incidence density** is a true rate. It divides new cases by the total person-time of observation contributed by the population. Person-time is the sum of the time each individual remains at risk and under observation.

$$
\text{Incidence Density} = \frac{\text{Number of new cases during follow-up}}{\text{Total person-time at risk}}
$$

*Example:* A cohort of 100 HIV-negative injection drug users is followed for one year. Two drop out after six months, and the rest complete follow-up. The total person-time is $(98 \times 1) + (2 \times 0.5) = 99$ person-years. If 10 new HIV infections occur, the incidence density is $10/99 = 0.101$ per person-year, or 10.1 per 100 person-years.

## Relationship Between Prevalence, Incidence, and Duration

In a stable population, the three quantities are related by:

$$
P = I \times D
$$

where $P$ is prevalence, $I$ is incidence, and $D$ is the average duration of disease.

Think of prevalence as water in a bathtub. New cases flow in through the tap; recovery and death drain water out. If a disease lasts many years, such as diabetes or hypertension, the tub stays full even when the inflow is modest. If a disease is brief, such as food poisoning or the common cold, water drains quickly and prevalence remains low even when many new cases occur.

![Diagram 2: Disease Reservoir Model](images/diagram2_disease_reservoir.svg)

*Figure 1.2: Disease reservoir model showing how incidence adds cases and how recovery or death removes them, with $P = I \times D$.*

*Example:* Type 2 diabetes cannot be cured easily, but modern medicine allows patients to live with it for decades. Because duration is long, prevalence is high even if the annual incidence is modest. In contrast, a rotavirus infection lasts only a few days, so its prevalence at any moment is low even when many children are falling ill.

## Attack Rate

An **attack rate** is a cumulative incidence used during outbreaks. It is usually expressed as a percentage.

$$
\text{Attack Rate} = \frac{\text{Number of people who become ill}}{\text{Total number of people at risk}} \times 100
$$

*Example:* After a college farewell dinner, 60 students ate the biryani and 30 became ill. The attack rate among biryani eaters was $(30/60) \times 100 = 50\%$.

## Measures of Mortality

### Crude Death Rate (CDR)

The **crude death rate** is the total number of deaths from all causes in a calendar year per 1,000 mid-year population.

$$
\text{CDR} = \frac{\text{Total deaths from all causes in a year}}{\text{Mid-year population}} \times 1{,}000
$$

*Example:* A district with a mid-year population of 500,000 recorded 4,000 deaths in one year. Its CDR was $(4{,}000/500{,}000) \times 1{,}000 = 8$ deaths per 1,000 population.

### Cause-Specific Mortality Rate

The **cause-specific mortality rate** is the number of deaths from a particular cause per unit of population in a given year.

$$
\text{Cause-Specific Mortality Rate} = \frac{\text{Deaths from a specific cause in a year}}{\text{Mid-year population}} \times 100{,}000
$$

*Example:* If the same district recorded 250 deaths from coronary heart disease in a year, the cause-specific mortality rate from heart disease was $(250/500{,}000) \times 100{,}000 = 50$ per 100,000 population per year.

### Case Fatality Rate (CFR)

The **case fatality rate** is the proportion of people diagnosed with a specific disease who die from it.

$$
\text{CFR} = \frac{\text{Number of deaths due to the disease}}{\text{Total diagnosed cases of the disease}} \times 100
$$

*Example:* During a dengue outbreak, 500 people tested positive and 15 died. The CFR was $(15/500) \times 100 = 3\%$.

## Summary Table of Basic Measures

| Measure | Numerator | Denominator | Use |
| --- | --- | --- | --- |
| Point prevalence | Existing cases at one point | Population at risk | Snapshot of disease burden |
| Period prevalence | Cases existing anytime in a period | Average/mid-period population | Burden over an interval |
| Cumulative incidence | New cases in a period | Healthy at risk at start | Risk of developing disease |
| Incidence density | New cases | Person-time at risk | True rate when follow-up varies |
| Attack rate | New cases in an outbreak | People exposed | Outbreak investigation |
| Crude death rate | All deaths | Mid-year population | Overall mortality |
| Cause-specific mortality rate | Deaths from one cause | Mid-year population | Specific disease mortality |
| Case fatality rate | Deaths from a disease | Diagnosed cases | Lethality of a disease |

---

# 1.4 Observational Study Designs: Case-Control Studies

> Suppose doctors in a city notice twenty young adults with a rare liver condition. Following ten thousand healthy teenagers for twenty years to see who develops the illness would take too long and cost too much. Instead, researchers begin with the disease and look backward. They gather the twenty sick young adults as cases and select a comparable group of twenty healthy young adults as controls. Then they ask both groups about past exposures, such as dietary supplements, medication history, or alcohol use. If the sick group was exposed far more often than the healthy group, the exposure becomes a suspect cause. This backward-looking design is called a case-control study. It is especially useful for rare diseases and for conditions with a long latency, such as cancer. In India, case-control studies have helped investigate oral cancer risk from tobacco chewing and childhood pneumonia risk from indoor air pollution, offering timely answers when forward follow-up is impractical.

## Classification of Epidemiologic Study Designs

Epidemiologic studies are broadly divided into **observational** and **experimental** studies. In observational studies the researcher records events as they occur naturally. In experimental studies, such as clinical trials, the researcher assigns an intervention.

Within observational studies, **descriptive studies** describe patterns of disease by person, place, and time, while **analytical studies** test specific hypotheses about exposure-disease relationships. The two main analytical designs are the case-control study and the cohort study. A **cross-sectional study** measures exposure and disease at the same point in time and can be either descriptive or analytical depending on its purpose.

```text
Epidemiologic Study Designs
│
├── Observational studies
│   ├── Descriptive studies
│   │   └── (case reports, case series, cross-sectional surveys)
│   └── Analytical studies
│       ├── Case-control study  (retrospective)
│       └── Cohort study        (prospective or retrospective)
│
└── Experimental studies
    └── Clinical trials
```

## Definition

A **case-control study** is an analytical observational study in which individuals with a disease or outcome of interest (**cases**) are compared with individuals without the disease (**controls**) to assess differences in past exposure to suspected risk factors.

![Diagram 3: Retrospective Case-Control Study Design](images/diagram3_case_control_design.svg)

*Figure 1.3: Architecture of a case-control study. The inquiry moves from present disease status back to past exposure history.*

## The 2×2 Contingency Table

Data from a case-control study are arranged as follows:

| Past Exposure | Cases (Diseased) | Controls (Healthy) | Total |
| --- | --- | --- | --- |
| Exposed | $a$ | $b$ | $a+b$ |
| Unexposed | $c$ | $d$ | $c+d$ |
| Total | $a+c$ | $b+d$ | $a+b+c+d$ |

*Example:* In a study of oral cancer and tobacco chewing, 80 cases and 80 controls are asked about chewing habits. If 60 cases and 20 controls chewed tobacco, the table has $a=60$, $b=20$, $c=20$, and $d=60$.

## Odds Ratio (OR)

Because case-control studies begin with diseased and non-diseased individuals, the true incidence in the population cannot be measured directly. The usual measure of association is the **odds ratio**.

The odds of exposure among cases is $a/c$. The odds of exposure among controls is $b/d$. The odds ratio is:

$$
OR = \frac{a/c}{b/d} = \frac{a \times d}{b \times c}
$$

### Interpretation of the Odds Ratio

| Value | Interpretation |
| --- | --- |
| $OR = 1$ | No association between exposure and disease. |
| $OR > 1$ | Exposure is associated with higher odds of disease; possible risk factor. |
| $OR < 1$ | Exposure is associated with lower odds of disease; possible protective factor. |

An odds ratio of 2.5 means that the odds of past exposure were 2.5 times higher among cases than among controls.

*Example:* Using the oral cancer table above:

$$
OR = \frac{60 \times 60}{20 \times 20} = \frac{3600}{400} = 9.0
$$

Tobacco chewers had nine times the odds of oral cancer compared with non-chewers.

## Advantages and Limitations

**Advantages:**

- Efficient for rare diseases.
- Fast and relatively inexpensive.
- Requires a smaller sample size than a cohort study.
- Can examine many exposures for one disease.

**Limitations:**

- Cannot calculate direct incidence or relative risk directly.
- Susceptible to recall bias and selection bias.
- Choosing appropriate controls can be difficult.
- Temporal sequence between exposure and disease may be unclear.

*Example:* A case-control study of childhood asthma and indoor biomass cooking in rural households can be completed in months, but mothers' recall of cooking fuel use during pregnancy may be imperfect.

---

# 1.5 Observational Study Designs: Cohort Studies

> Imagine you want to know whether working night shifts increases the risk of heart disease among information-technology professionals. You cannot simply ask sick patients about their work history and expect a clear answer, because other factors such as smoking, diet, and stress may confuse the picture. Instead, you recruit one thousand healthy IT workers today. You divide them into those who regularly work night shifts and those who work only during the day. You then follow both groups forward for ten years and record every new case of heart disease. Because both groups started healthy, any difference in disease occurrence can reasonably be linked to the exposure. This forward-looking design is called a cohort study. It is the design of choice when the exposure is rare but the outcome is not, and when the researcher needs to measure incidence directly. Long-running cohort studies in India have followed tobacco users, industrial workers, and rural women to understand the future burden of chronic disease.

## Definition

A **cohort study** is an analytical observational study in which healthy participants are selected on the basis of their exposure status and followed forward in time to compare the incidence of disease between exposed and unexposed groups.

![Diagram 4: Prospective Cohort Study Design](images/diagram4_cohort_design.svg)

*Figure 1.4: Architecture of a cohort study. The inquiry moves from present exposure status forward to future disease occurrence.*

## The 2×2 Contingency Table

In a cohort study, the table is built from incidence data:

| Exposure | Developed Disease | Remained Healthy | Total |
| --- | --- | --- | --- |
| Exposed | $a$ | $b$ | $a+b$ |
| Unexposed | $c$ | $d$ | $c+d$ |
| Total | $a+c$ | $b+d$ | $a+b+c+d$ |

*Example:* In a study of smoking and chronic cough, 200 smokers and 300 non-smokers are followed for five years. Twenty smokers and six non-smokers develop chronic cough. Thus $a=20$, $b=180$, $c=6$, and $d=294$.

## Measures of Association in Cohort Studies

### Incidence in Exposed and Unexposed Groups

$$
I_e = \frac{a}{a+b}
$$

$$
I_u = \frac{c}{c+d}
$$

### Relative Risk (RR)

**Relative risk** is the ratio of incidence in the exposed group to incidence in the unexposed group.

$$
RR = \frac{I_e}{I_u} = \frac{a/(a+b)}{c/(c+d)}
$$

*Interpretation:*

| Value | Meaning |
| --- | --- |
| $RR = 1$ | No association between exposure and disease. |
| $RR > 1$ | Exposure increases disease risk. |
| $RR < 1$ | Exposure reduces disease risk; possible protective factor. |

A relative risk of 5 means that exposed individuals are five times as likely to develop the disease as unexposed individuals.

*Example:* Using the smoking data:

$$
I_e = \frac{20}{200} = 0.10, \quad I_u = \frac{6}{300} = 0.02
$$

$$
RR = \frac{0.10}{0.02} = 5.0
$$

Smokers were five times as likely as non-smokers to develop chronic cough.

### Attributable Risk (AR)

**Attributable risk** is the difference in incidence between the exposed and unexposed groups. It measures the excess disease incidence that can be attributed to the exposure.

$$
AR = I_e - I_u
$$

*Example:*

$$
AR = 0.10 - 0.02 = 0.08
$$

This means 80 extra cases of chronic cough per 1,000 smokers over five years are attributable to smoking.

### Attributable Risk Percent (AR%)

The attributable risk percent tells us what percentage of disease in the exposed group is due to the exposure.

$$
AR\% = \frac{I_e - I_u}{I_e} \times 100
$$

*Example:*

$$
AR\% = \frac{0.10 - 0.02}{0.10} \times 100 = 80\%
$$

Eighty percent of chronic cough among smokers in this study was attributable to smoking.

## Comparison of Case-Control and Cohort Studies

| Feature | Case-Control Study | Cohort Study |
| --- | --- | --- |
| Direction | Retrospective: outcome → exposure | Prospective or retrospective: exposure → outcome |
| Starting point | Diseased cases and healthy controls | Healthy exposed and unexposed groups |
| Best for | Rare diseases | Rare exposures |
| Time and cost | Fast, inexpensive | Long, expensive |
| Sample size | Smaller | Larger |
| Direct incidence | Cannot be calculated directly | Can be calculated |
| Main measure | Odds ratio | Relative risk and attributable risk |
| Main bias risk | Recall bias, selection bias | Attrition bias (loss to follow-up) |

---

# 1.6 Quantitative Methods in Health Screening

> A mobile health camp visits a rural village and tests one thousand adults for diabetes using a quick finger-prick blood-glucose strip. The result appears within two minutes. This rapid test is not a final diagnosis. Its purpose is to sort apparently healthy people into two groups: those who probably have diabetes and need a full laboratory test, and those who are probably healthy. This preventive sorting process is called screening. Screening is widely used in India: anaemia checks for adolescent girls, vision tests in schools, blood-pressure camps for adults, and tuberculosis symptom screening in high-risk areas. A good screening test must not miss true cases and must not falsely label healthy people as sick. In this section we learn how to measure the accuracy of a screening test using a simple 2×2 table and four standard indicators. These ideas help health workers decide which test to use and how to interpret unexpected positive or negative results in the field.

## Definition

A **screening test** is a rapid test or examination applied to an asymptomatic population to classify individuals as likely having a specific disease or as likely not having it. Screening is not diagnostic; individuals who screen positive require confirmatory testing by a **gold standard**.

*Example:* A school vision test that flags children with poor eyesight is a screening test. Those who fail are sent to an ophthalmologist for a full eye examination, which is the gold standard.

## The 2×2 Screening Evaluation Matrix

The screening test result is compared with the true disease status as determined by the gold standard.

![Diagram 5: 2×2 Health Screening Evaluation Matrix](images/diagram5_screening_matrix.svg)

*Figure 1.5: Two-by-two matrix comparing screening test results with the gold standard.*

| Screening Test | Disease Present (Gold Standard +) | Disease Absent (Gold Standard −) |
| --- | --- | --- |
| Test Positive | True Positive ($a$) | False Positive ($b$) |
| Test Negative | False Negative ($c$) | True Negative ($d$) |

*Example:* A rapid test for HIV is evaluated against a laboratory ELISA test. If 95 truly infected people test positive, 5 test negative, 2 uninfected people test positive, and 198 test negative, then $a=95$, $b=2$, $c=5$, and $d=198$.

## Core Evaluation Metrics

### Sensitivity

**Sensitivity** is the ability of a test to correctly identify those who truly have the disease.

$$
\text{Sensitivity} = \frac{a}{a+c} \times 100
$$

A highly sensitive test produces few false negatives. It is preferred when missing a true case has serious consequences, such as in HIV or tuberculosis screening.

*Example:* Using the HIV data:

$$
\text{Sensitivity} = \frac{95}{95+5} \times 100 = 95\%
$$

The test correctly identified 95% of infected individuals.

### Specificity

**Specificity** is the ability of a test to correctly identify those who truly do not have the disease.

$$
\text{Specificity} = \frac{d}{b+d} \times 100
$$

A highly specific test produces few false positives. It is preferred when a false-positive result would lead to harmful or expensive follow-up.

*Example:*

$$
\text{Specificity} = \frac{198}{2+198} \times 100 = 99\%
$$

The test correctly cleared 99% of uninfected individuals.

### Positive Predictive Value (PPV)

**PPV** is the probability that a person who tests positive actually has the disease.

$$
\text{PPV} = \frac{a}{a+b} \times 100
$$

*Example:*

$$
\text{PPV} = \frac{95}{95+2} \times 100 = \frac{95}{97} \times 100 \approx 97.94\%
$$

About 98% of those who tested positive were truly infected.

### Negative Predictive Value (NPV)

**NPV** is the probability that a person who tests negative is truly free of the disease.

$$
\text{NPV} = \frac{d}{c+d} \times 100
$$

*Example:*

$$
\text{NPV} = \frac{198}{5+198} \times 100 = \frac{198}{203} \times 100 \approx 97.54\%
$$

About 97.5% of those who tested negative were truly uninfected.

## Predictive Values and Disease Prevalence

PPV and NPV depend not only on sensitivity and specificity but also on the prevalence of disease in the screened population. When prevalence is low, even a specific test will generate many false positives, so PPV falls. When prevalence is high, PPV rises and NPV falls. This is why a screening test that performs well in a high-prevalence hospital setting may perform less well in a low-prevalence community screening camp.

*Example:* Suppose a breast-cancer screening test has 90% sensitivity and 90% specificity. In a population where breast-cancer prevalence is 1%, screening 10,000 women yields 90 true positives and 990 false positives. The PPV is only $90/(90+990) = 7.7\%$. In a high-risk group with 10% prevalence, the same test yields 900 true positives and 900 false positives, giving a PPV of 50%.

---

# 1.7 Biases and Error Control in Epidemiologic Research

> Suppose you ask heart-disease patients to recall how many fried snacks they ate each week ten years ago. A patient who survived a major heart attack may think hard about every samosa and pakora. A healthy control person may casually forget half of what they ate. If the researcher does not account for this difference in memory, the study may wrongly conclude that fried snacks caused the disease. This is an example of bias — a systematic error that distorts the truth. Bias can enter at every stage: choosing participants, collecting information, analysing data, or interpreting results. In India, where health records may be incomplete and follow-up over long distances is difficult, bias is a constant concern. Recognising and controlling it is as important as calculating the odds ratio or relative risk. In this section we discuss the main types of bias and the problem of confounding, along with practical ways to reduce their influence.

## Bias

**Bias** is any systematic error in the design, conduct, analysis, or interpretation of a study that leads to an incorrect estimate of the effect of an exposure on a disease.

### Selection Bias

**Selection bias** arises when the way participants are chosen or recruited makes the study groups different from the target population in a way that affects the exposure-disease relationship.

*Example:* If a case-control study of oral cancer recruits cases from a cancer hospital but controls from a nearby dental clinic, the controls may differ from the source population in tobacco-use habits.

### Recall Bias

**Recall bias** occurs when cases and controls remember past exposures differently. Sick individuals often search their memories more thoroughly than healthy controls.

*Example:* Mothers of children with birth defects may recall medication use during pregnancy more completely than mothers of healthy children.

### Attrition Bias

**Attrition bias** occurs when participants are lost to follow-up during a cohort study, and those lost differ systematically from those who remain.

*Example:* In a ten-year study of smoking and chronic disease, heavy smokers may be more likely to drop out, leading to an underestimate of risk.

## Confounding

**Confounding** occurs when a third variable is associated with both the exposure and the disease, and distorts the apparent relationship between them. A confounding variable must:

1. be a risk factor for the disease;
2. be associated with the exposure; and
3. not lie on the causal pathway between exposure and disease.

*Example:* Early studies suggested that coffee drinking caused heart disease. Later research showed that heavy coffee drinkers were also more likely to smoke. Smoking was the true confounder; once smoking was controlled through stratification or regression, coffee was no longer linked to heart disease.

## Controlling Bias and Confounding

Some common strategies include:

- random selection of controls;
- blinding interviewers and participants;
- using medical records instead of memory where possible;
- minimising loss to follow-up;
- matching cases and controls on age, sex, or other factors;
- stratification and multivariate analysis to adjust for confounders.

*Example:* In a study of biomass cooking and childhood pneumonia, researchers might match households on income and locality so that these factors do not confound the association.

---

# 1.8 Solved Real-World Case Studies

## Case Study 1: Hostel Mess Food Poisoning Investigation

**Scenario:** One hundred students ate dinner at a college hostel. Sixty students ate paneer butter masala, and 36 of them fell ill with gastroenteritis. Forty students did not eat paneer, and 4 of them fell ill.

**Solution:**

| Exposure | Ill | Not Ill | Total | Attack Rate |
| --- | --- | --- | --- | --- |
| Ate paneer | 36 | 24 | 60 | $36/60 \times 100 = 60.0\%$ |
| Did not eat paneer | 4 | 36 | 40 | $4/40 \times 100 = 10.0\%$ |

$$
RR = \frac{0.60}{0.10} = 6.0
$$

**Conclusion:** Students who ate paneer were six times as likely to become ill. Paneer butter masala was the likely source of the outbreak.

## Case Study 2: Smoking and Chronic Cough

**Scenario:** A five-year cohort study followed 200 smokers and 300 non-smokers. At the end of follow-up, 20 smokers and 6 non-smokers had developed chronic cough.

**Solution:**

| Exposure | Chronic Cough | Healthy | Total | Incidence |
| --- | --- | --- | --- | --- |
| Smokers | 20 | 180 | 200 | $20/200 = 0.10$ |
| Non-smokers | 6 | 294 | 300 | $6/300 = 0.02$ |

$$
RR = \frac{0.10}{0.02} = 5.0
$$

$$
AR = 0.10 - 0.02 = 0.08
$$

$$
AR\% = \frac{0.08}{0.10} \times 100 = 80\%
$$

**Conclusion:** Smokers had five times the risk of chronic cough. Eighty percent of the cough incidence among smokers was attributable to smoking.

## Case Study 3: High Salt Intake and Heart Attack

**Scenario:** A researcher selected 50 heart-attack patients and 50 healthy individuals matched by age. Past records showed that 35 cases and 15 controls had a history of high salt intake.

**Solution:**

| Past Salt Intake | Cases | Controls |
| --- | --- | --- |
| High | 35 | 15 |
| Normal | 15 | 35 |

Here $a = 35$, $b = 15$, $c = 15$, and $d = 35$.

$$
OR = \frac{a \times d}{b \times c} = \frac{35 \times 35}{15 \times 15} = \frac{1225}{225} \approx 5.44
$$

**Conclusion:** The odds of high salt intake were about 5.4 times higher among heart-attack patients than among healthy controls.

## Case Study 4: Rural Anaemia Screening Camp

**Scenario:** Three hundred adults were screened with a rapid haemoglobin strip test. The gold standard blood test confirmed that 100 had anaemia and 200 did not. The rapid test correctly identified 85 anaemic individuals and incorrectly labelled 20 healthy individuals as positive.

**Solution:**

| Screening Test | Anaemia Present | Anaemia Absent |
| --- | --- | --- |
| Positive | 85 | 20 |
| Negative | 15 | 180 |

$$
\text{Sensitivity} = \frac{85}{85+15} \times 100 = 85\%
$$

$$
\text{Specificity} = \frac{180}{20+180} \times 100 = 90\%
$$

$$
\text{PPV} = \frac{85}{85+20} \times 100 = \frac{85}{105} \times 100 \approx 80.95\%
$$

$$
\text{NPV} = \frac{180}{15+180} \times 100 = \frac{180}{195} \times 100 \approx 92.31\%
$$

**Conclusion:** The test was reasonably good at detecting anaemia and excellent at ruling it out. Because the test is not perfect, all positive cases should receive the gold standard test for confirmation.

## Case Study 5: Dengue Outbreak Case Fatality Rate

**Scenario:** During a dengue outbreak in a district, 500 people tested positive for the virus and 15 died from complications.

**Solution:**

$$
CFR = \frac{15}{500} \times 100 = 3\%
$$

**Conclusion:** Three percent of diagnosed dengue patients died during this outbreak. The figure helps health authorities judge severity and plan intensive-care resources.


---

# 1.9 Chapter End Exercises and Self-Assessment Bank

## Part A: Multiple Choice Questions (20 MCQs)

**1. Epidemiology is defined as the study of:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Individual patient treatments in hospital wards  
&nbsp;&nbsp;&nbsp;&nbsp;b) Distribution and determinants of health states in human populations  
&nbsp;&nbsp;&nbsp;&nbsp;c) Microscopic chemical interactions in blood  
&nbsp;&nbsp;&nbsp;&nbsp;d) Surgical techniques for chronic diseases

*Correct Answer:* **b** — Epidemiology examines population-level health patterns and causes rather than bedside clinical care.

**2. Point prevalence is defined as the proportion of a population with a disease at:**

&nbsp;&nbsp;&nbsp;&nbsp;a) A single specific point in time  
&nbsp;&nbsp;&nbsp;&nbsp;b) A 10-year follow-up interval  
&nbsp;&nbsp;&nbsp;&nbsp;c) The time of birth only  
&nbsp;&nbsp;&nbsp;&nbsp;d) The end of an epidemic period

*Correct Answer:* **a** — Point prevalence measures existing cases at one designated instant.

**3. Incidence rate is defined as the rate at which:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Old cases recover from an illness  
&nbsp;&nbsp;&nbsp;&nbsp;b) New cases develop in a population at risk  
&nbsp;&nbsp;&nbsp;&nbsp;c) Hospital beds are occupied  
&nbsp;&nbsp;&nbsp;&nbsp;d) Deaths occur among treated patients

*Correct Answer:* **b** — Incidence counts only newly occurring cases.

**4. If a chronic disease cannot be cured but treatment extends patient survival, disease prevalence will:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Decrease to zero  
&nbsp;&nbsp;&nbsp;&nbsp;b) Remain completely unchanged  
&nbsp;&nbsp;&nbsp;&nbsp;c) Increase over time  
&nbsp;&nbsp;&nbsp;&nbsp;d) Equal the incidence rate exactly

*Correct Answer:* **c** — Extending survival increases duration $D$; since $P = I \times D$, prevalence rises.

**5. A case-control study is defined as an observational design that moves:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Forward from exposure to outcome  
&nbsp;&nbsp;&nbsp;&nbsp;b) Retrospectively from outcome to past exposure  
&nbsp;&nbsp;&nbsp;&nbsp;c) Forward from healthy status to recovery  
&nbsp;&nbsp;&nbsp;&nbsp;d) Experimentally by giving drug doses

*Correct Answer:* **b** — Case-control studies start with disease status and look backward.

**6. The primary measure of association calculated in a case-control study is the:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Relative risk  
&nbsp;&nbsp;&nbsp;&nbsp;b) Odds ratio  
&nbsp;&nbsp;&nbsp;&nbsp;c) Attributable risk  
&nbsp;&nbsp;&nbsp;&nbsp;d) Population risk difference

*Correct Answer:* **b** — Because direct incidence cannot be measured, the odds ratio is the primary metric.

**7. A cohort study is defined as a design that selects participants based on their:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Disease status  
&nbsp;&nbsp;&nbsp;&nbsp;b) Exposure status  
&nbsp;&nbsp;&nbsp;&nbsp;c) Hospital admission date  
&nbsp;&nbsp;&nbsp;&nbsp;d) Recovery rate

*Correct Answer:* **b** — Cohort studies begin with healthy groups classified by exposure.

**8. Relative risk is defined as the ratio of:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Odds of exposure in cases to odds in controls  
&nbsp;&nbsp;&nbsp;&nbsp;b) Incidence rate in exposed group to incidence rate in unexposed group  
&nbsp;&nbsp;&nbsp;&nbsp;c) Total deaths to total healthy individuals  
&nbsp;&nbsp;&nbsp;&nbsp;d) Prevalence in urban areas to prevalence in rural areas

*Correct Answer:* **b** — $RR = I_e / I_u$.

**9. An odds ratio equal to 1.0 means:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Exposure increases disease risk significantly  
&nbsp;&nbsp;&nbsp;&nbsp;b) Exposure decreases disease risk significantly  
&nbsp;&nbsp;&nbsp;&nbsp;c) There is no association between exposure and disease  
&nbsp;&nbsp;&nbsp;&nbsp;d) Study calculations are mathematically invalid

*Correct Answer:* **c** — $OR = 1$ indicates equal exposure odds in cases and controls.

**10. Case fatality rate is defined as the proportion of:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Deaths in a city divided by mid-year population  
&nbsp;&nbsp;&nbsp;&nbsp;b) Diagnosed patients with a specific disease who die from it  
&nbsp;&nbsp;&nbsp;&nbsp;c) Deaths caused by accidents in factory workers  
&nbsp;&nbsp;&nbsp;&nbsp;d) Recovered cases relative to total admissions

*Correct Answer:* **b** — CFR = (deaths from disease / diagnosed cases) × 100.

**11. Sensitivity of a screening test is defined as the test's ability to correctly identify:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Healthy individuals as negative  
&nbsp;&nbsp;&nbsp;&nbsp;b) Diseased individuals as positive  
&nbsp;&nbsp;&nbsp;&nbsp;c) False positive cases in a lab  
&nbsp;&nbsp;&nbsp;&nbsp;d) Carrier states in animals

*Correct Answer:* **b** — Sensitivity = $a/(a+c)$.

**12. Specificity of a screening test is defined as the test's ability to correctly identify:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Diseased individuals as positive  
&nbsp;&nbsp;&nbsp;&nbsp;b) Non-diseased individuals as negative  
&nbsp;&nbsp;&nbsp;&nbsp;c) New incidence rates  
&nbsp;&nbsp;&nbsp;&nbsp;d) Case fatality differences

*Correct Answer:* **b** — Specificity = $d/(b+d)$.

**13. A false positive result in a screening program occurs when a person:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Has the disease and tests positive  
&nbsp;&nbsp;&nbsp;&nbsp;b) Does not have the disease but tests positive  
&nbsp;&nbsp;&nbsp;&nbsp;c) Has the disease but tests negative  
&nbsp;&nbsp;&nbsp;&nbsp;d) Does not have the disease and tests negative

*Correct Answer:* **b** — A false positive is a healthy individual misclassified as positive.

**14. Positive predictive value is defined as the proportion of:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Test-positive individuals who truly have the disease  
&nbsp;&nbsp;&nbsp;&nbsp;b) Test-negative individuals who are healthy  
&nbsp;&nbsp;&nbsp;&nbsp;c) Diseased people who test negative  
&nbsp;&nbsp;&nbsp;&nbsp;d) Healthy people who test positive

*Correct Answer:* **a** — PPV = $a/(a+b)$.

**15. Loss of study participants over time during a prospective study leads to:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Recall bias  
&nbsp;&nbsp;&nbsp;&nbsp;b) Attrition bias  
&nbsp;&nbsp;&nbsp;&nbsp;c) Selection bias at baseline  
&nbsp;&nbsp;&nbsp;&nbsp;d) Interviewer bias

*Correct Answer:* **b** — Loss to follow-up creates attrition bias.

**16. Which study design is most efficient for studying extremely rare diseases?**

&nbsp;&nbsp;&nbsp;&nbsp;a) Cohort study  
&nbsp;&nbsp;&nbsp;&nbsp;b) Case-control study  
&nbsp;&nbsp;&nbsp;&nbsp;c) Randomised controlled trial  
&nbsp;&nbsp;&nbsp;&nbsp;d) Field population survey

*Correct Answer:* **b** — Case-control studies start with pre-identified cases, making them ideal for rare diseases.

**17. Crude death rate is traditionally expressed per:**

&nbsp;&nbsp;&nbsp;&nbsp;a) 100 population  
&nbsp;&nbsp;&nbsp;&nbsp;b) 1,000 population  
&nbsp;&nbsp;&nbsp;&nbsp;c) 10,000 population  
&nbsp;&nbsp;&nbsp;&nbsp;d) 100,000 population

*Correct Answer:* **b** — CDR is standardised per 1,000 mid-year population.

**18. In a stable population, prevalence ($P$), incidence ($I$), and duration ($D$) are related as:**

&nbsp;&nbsp;&nbsp;&nbsp;a) $P = I + D$  
&nbsp;&nbsp;&nbsp;&nbsp;b) $P = I \times D$  
&nbsp;&nbsp;&nbsp;&nbsp;c) $P = I / D$  
&nbsp;&nbsp;&nbsp;&nbsp;d) $P = D / I$

*Correct Answer:* **b** — Prevalence equals incidence multiplied by average duration.

**19. Which variable describes person-level characteristics in descriptive epidemiology?**

&nbsp;&nbsp;&nbsp;&nbsp;a) Altitude  
&nbsp;&nbsp;&nbsp;&nbsp;b) Rainfall  
&nbsp;&nbsp;&nbsp;&nbsp;c) Age  
&nbsp;&nbsp;&nbsp;&nbsp;d) Season

*Correct Answer:* **c** — Age is a fundamental person-level characteristic.

**20. A screening test with very high sensitivity is preferred when:**

&nbsp;&nbsp;&nbsp;&nbsp;a) Missing a true disease case has serious health consequences  
&nbsp;&nbsp;&nbsp;&nbsp;b) Diagnostic treatment is very harmful  
&nbsp;&nbsp;&nbsp;&nbsp;c) The test is extremely expensive  
&nbsp;&nbsp;&nbsp;&nbsp;d) Disease is mild and self-healing

*Correct Answer:* **a** — High sensitivity minimises false negatives.

## Part B: Fill in the Blanks (20 Questions)

**1.** Epidemiology is defined as the study of the distribution and ________ of disease in human populations.

*Answer:* **determinants**

**2.** The number of newly occurring cases of a disease in a population over a given time is called ________.

*Answer:* **incidence**

**3.** Total existing cases (old plus new) divided by population at risk gives the ________ rate.

*Answer:* **prevalence**

**4.** The proportion of diagnosed patients of a specific disease who die from it is defined as the ________ rate.

*Answer:* **case fatality**

**5.** In case-control studies, participants are selected on the basis of their ________ status.

*Answer:* **disease / outcome**

**6.** In cohort studies, participants are selected on the basis of their ________ status.

*Answer:* **exposure**

**7.** The formula $(a \times d)/(b \times c)$ in a 2×2 table computes the ________ ratio.

*Answer:* **odds**

**8.** The ratio of incidence rate in exposed group to incidence rate in unexposed group is defined as ________ risk.

*Answer:* **relative**

**9.** The difference in incidence rates between exposed and unexposed groups is defined as ________ risk.

*Answer:* **attributable**

**10.** The proportion of truly sick people correctly identified by a screening test is defined as ________.

*Answer:* **sensitivity**

**11.** The proportion of truly healthy people correctly identified as negative by a test is defined as ________.

*Answer:* **specificity**

**12.** A sick person misclassified as healthy by a screening test is called a ________ negative.

*Answer:* **false**

**13.** A healthy person misclassified as sick by a screening test is called a ________ positive.

*Answer:* **false**

**14.** An odds ratio greater than 1.0 indicates that an exposure is a potential ________ factor.

*Answer:* **risk**

**15.** Systematic loss of participants during long-term follow-up leads to ________ bias in cohort studies.

*Answer:* **attrition**

**16.** Patients struggling to remember past dietary habits leads to ________ bias in case-control studies.

*Answer:* **recall**

**17.** The ultimate accurate diagnostic test against which screening tests are evaluated is called the ________ standard.

*Answer:* **gold**

**18.** Mid-year population is used in the denominator to calculate the ________ death rate.

*Answer:* **crude**

**19.** Long disease duration causes the disease ________ to increase over time.

*Answer:* **prevalence**

**20.** Screening is conducted on individuals who are ________ (showing no outward symptoms).

*Answer:* **asymptomatic**

## Part C: True / False Statements (20 Questions)

**1.** Epidemiology focuses strictly on individual patient care in clinical settings.

*Statement is:* **False** — Epidemiology focuses on whole population groups and public health.

**2.** Incidence rate includes both old and newly diagnosed cases in its numerator.

*Statement is:* **False** — Incidence includes only newly diagnosed cases.

**3.** A case-control study tracks participants forward into the future to see who gets sick.

*Statement is:* **False** — Case-control studies are retrospective.

**4.** Relative risk can be calculated directly from a standard case-control study.

*Statement is:* **False** — Case-control studies yield odds ratios; direct incidence and relative risk cannot be calculated.

**5.** Fatal diseases with very short survival times tend to have low prevalence.

*Statement is:* **True** — Short duration reduces prevalence because $P = I \times D$.

**6.** Specificity measures the test's ability to correctly clear non-diseased individuals.

*Statement is:* **True** — Specificity = $d/(b+d)$.

**7.** False positive results cause unnecessary psychological anxiety for patients.

*Statement is:* **True** — Misclassifying healthy people as sick creates anxiety and unnecessary follow-up.

**8.** An odds ratio of less than 1.0 suggests an exposure may protect against disease.

*Statement is:* **True** — $OR < 1$ indicates lower odds of disease in exposed individuals.

**9.** Cohort studies require smaller sample sizes than case-control studies.

*Statement is:* **False** — Cohort studies generally require larger sample sizes.

**10.** Attributable risk measures the excess rate of disease caused directly by an exposure.

*Statement is:* **True** — $AR = I_e - I_u$.

**11.** Case fatality rate is usually expressed per 100,000 mid-year population.

*Statement is:* **False** — CFR is expressed as a percentage of diagnosed cases.

**12.** Point prevalence measures disease status at one designated moment in time.

*Statement is:* **True** — Point prevalence evaluates burden at a specific instant.

**13.** Cohort study participants must already have the disease when follow-up starts.

*Statement is:* **False** — Participants must be disease-free at baseline.

**14.** Positive predictive value changes depending on disease prevalence in the population.

*Statement is:* **True** — PPV rises with prevalence and falls when prevalence is low.

**15.** Observational study designs involve giving new medicines to participants.

*Statement is:* **False** — Observational studies only observe natural exposures.

**16.** Crude death rate accounts for age differences between different populations.

*Statement is:* **False** — CDR does not adjust for age; age-specific rates are needed.

**17.** High sensitivity minimises the number of false negative test results.

*Statement is:* **True** — High sensitivity ensures sick individuals are detected.

**18.** Loss of participants during cohort follow-up creates attrition bias.

*Statement is:* **True** — Differential dropout over time leads to attrition bias.

**19.** Retrospective studies examine historical records or past memories.

*Statement is:* **True** — Retrospective designs look back at past data.

**20.** A screening test provides a final medical diagnosis by itself.

*Statement is:* **False** — Screening only flags potential cases; a gold standard test is required for diagnosis.

## Part D: Matching Type Questions (5 Sets of 4 Items)

### Set 1: Basic Epidemiological Measures

| Column A | Column B |
| --- | --- |
| 1. Prevalence | A. Proportion of diagnosed patients who die |
| 2. Incidence | B. Total existing cases divided by population at risk |
| 3. Crude death rate | C. New cases occurring over a given time period |
| 4. Case fatality rate | D. Total deaths per 1,000 mid-year population |

*Answer Key:* **1-B, 2-C, 3-D, 4-A**

*Explanation:* Prevalence tracks total existing cases; incidence tracks new cases; crude death rate measures total deaths per 1,000 mid-year population; case fatality rate measures the proportion of diagnosed patients who die.

### Set 2: Study Designs and Metrics

| Column A | Column B |
| --- | --- |
| 5. Case-control study | A. Direct ratio of exposed to unexposed incidence |
| 6. Cohort study | B. Retrospective study starting with sick and healthy groups |
| 7. Odds ratio | C. Calculated as $(a \times d)/(b \times c)$ |
| 8. Relative risk | D. Prospective study following exposed groups forward |

*Answer Key:* **5-B, 6-D, 7-C, 8-A**

### Set 3: Screening Definitions

| Column A | Column B |
| --- | --- |
| 9. Sensitivity | A. Ability to correctly clear healthy individuals [$d/(b+d)$] |
| 10. Specificity | B. Ability to correctly identify sick individuals [$a/(a+c)$] |
| 11. Positive predictive value | C. Probability that a negative test person is truly healthy |
| 12. Negative predictive value | D. Probability that a positive test person truly has disease |

*Answer Key:* **9-B, 10-A, 11-D, 12-C**

### Set 4: Screening Categories

| Column A | Column B |
| --- | --- |
| 13. True positive | A. Test is positive, but person is healthy |
| 14. False positive | B. Test is negative, but person is sick |
| 15. False negative | C. Test is negative, and person is healthy |
| 16. True negative | D. Test is positive, and person is sick |

*Answer Key:* **13-D, 14-A, 15-B, 16-C**

### Set 5: Interpretation of Risk Values

| Column A | Column B |
| --- | --- |
| 17. Relative risk = 1.0 | A. Exposure acts as a protective factor |
| 18. Relative risk > 1.0 | B. Exposure acts as a risk factor |
| 19. Relative risk < 1.0 | C. No association between exposure and disease |
| 20. Attributable risk | D. Excess rate of disease caused directly by exposure |

*Answer Key:* **17-C, 18-B, 19-A, 20-D**

## Part E: Subjective and Analytical Questions (10 Questions with Detailed Solutions)

### Q1. How is epidemiology defined? Explain its primary objectives and applications in simple terms.

**Solution:**

Epidemiology is the study of the distribution and determinants of health-related states or events in specified human populations, and the application of this study to the prevention and control of health problems.

Its primary objectives are:

1. to identify the causes of disease, such as contaminated water or smoking;
2. to measure the burden of illness in a community so that resources can be planned;
3. to track how a disease changes over time;
4. to evaluate whether vaccines, drugs, or public health programmes work; and
5. to guide government policy for disease prevention.

*Example:* The pulse polio programme used epidemiologic surveillance to identify areas with ongoing poliovirus transmission and target vaccination campaigns there.

### Q2. How are prevalence and incidence defined? Explain their mathematical differences and describe how disease duration links them.

**Solution:**

**Prevalence** is the proportion of a population that has a disease at a given point or period in time. It includes both old and new cases.

**Incidence** is the number of new cases that develop in a population at risk during a given time period.

The mathematical link in a stable population is:

$$
P = I \times D
$$

where $D$ is the average duration of disease. A disease with long duration, such as diabetes, accumulates cases and produces high prevalence even when annual incidence is moderate. A disease with short duration, such as food poisoning, has low prevalence even when many people become ill.

### Q3. What are the eight key steps in an outbreak investigation?

**Solution:**

1. Verify the outbreak and diagnosis by comparing case counts with the baseline.
2. Define a case and actively search for cases in the community.
3. Perform descriptive analysis by person, place, and time, and draw an epidemic curve.
4. Formulate a working hypothesis about the source and mode of transmission.
5. Test and refine the hypothesis using analytical studies and risk estimates.
6. Implement control and prevention measures without waiting for final results.
7. Evaluate the effectiveness of control measures by monitoring new cases.
8. Communicate findings to health authorities and the public.

### Q4. Define crude death rate and case fatality rate. How do they differ?

**Solution:**

**Crude death rate** is the total number of deaths from all causes in a year per 1,000 mid-year population. It measures general mortality in a population.

**Case fatality rate** is the proportion of people diagnosed with a specific disease who die from it. It measures how deadly that particular disease is.

The key difference lies in the denominator. CDR uses the entire mid-year population, while CFR uses only diagnosed cases of the disease.

*Example:* A CDR of 8 per 1,000 tells us about overall health conditions in a district. A CFR of 3% for dengue tells us the risk of death once dengue has been diagnosed.

### Q5. Define a case-control study. Explain its setup, advantages, and limitations.

**Solution:**

A **case-control study** is an observational retrospective study that compares individuals with a disease (cases) to individuals without the disease (controls) to assess differences in past exposure.

**Setup:** Cases and controls are selected, and their histories of exposure to suspected risk factors are compared. Data are arranged in a 2×2 table, and the odds ratio is calculated as $OR = (a \times d)/(b \times c)$.

**Advantages:** efficient for rare diseases, fast, inexpensive, and requires a smaller sample size than a cohort study.

**Limitations:** cannot measure direct incidence or relative risk directly, and is vulnerable to recall bias and selection bias.

### Q6. Define a cohort study. Explain how relative risk and attributable risk are calculated and interpreted.

**Solution:**

A **cohort study** is an observational study in which healthy participants are selected on the basis of exposure status and followed forward in time to measure disease development.

The incidence in the exposed group is $I_e = a/(a+b)$ and in the unexposed group is $I_u = c/(c+d)$.

**Relative risk** is $RR = I_e / I_u$. It compares disease risk in exposed and unexposed individuals. $RR = 1$ means no association; $RR > 1$ means the exposure is a risk factor; $RR < 1$ means it is protective.

**Attributable risk** is $AR = I_e - I_u$. It measures the excess incidence of disease attributable to the exposure.

### Q7. Compare case-control and cohort study designs across key parameters.

**Solution:**

| Parameter | Case-Control Study | Cohort Study |
| --- | --- | --- |
| Direction | Retrospective (outcome → exposure) | Prospective or retrospective (exposure → outcome) |
| Starting point | Diseased cases and healthy controls | Healthy exposed and unexposed groups |
| Best suited for | Rare diseases | Rare exposures |
| Time and cost | Fast and inexpensive | Long and expensive |
| Sample size | Smaller | Larger |
| Direct incidence | Cannot be calculated | Can be calculated |
| Main measure | Odds ratio | Relative risk and attributable risk |
| Main bias | Recall bias, selection bias | Attrition bias |

### Q8. Define sensitivity, specificity, positive predictive value, and negative predictive value.

**Solution:**

- **Sensitivity** = $a/(a+c)$. It is the ability of a test to correctly identify diseased individuals as positive.
- **Specificity** = $d/(b+d)$. It is the ability of a test to correctly identify non-diseased individuals as negative.
- **Positive predictive value** = $a/(a+b)$. It is the probability that a person who tests positive truly has the disease.
- **Negative predictive value** = $d/(c+d)$. It is the probability that a person who tests negative is truly disease-free.

### Q9. A screening test was evaluated on 300 adults. The gold standard showed that 100 had diabetes and 200 did not. The test correctly gave positive results for 85 diabetic adults and incorrectly gave positive results for 20 healthy adults. Calculate sensitivity, specificity, and positive predictive value.

**Solution:**

The 2×2 table is:

| Screening Test | Diabetes Present | Diabetes Absent |
| --- | --- | --- |
| Positive | 85 | 20 |
| Negative | 15 | 180 |

$$
\text{Sensitivity} = \frac{85}{85+15} \times 100 = 85\%
$$

$$
\text{Specificity} = \frac{180}{20+180} \times 100 = 90\%
$$

$$
\text{PPV} = \frac{85}{85+20} \times 100 = \frac{85}{105} \times 100 \approx 80.95\%
$$

### Q10. Define bias and confounding. Explain recall bias and attrition bias with simple examples.

**Solution:**

**Bias** is any systematic error in study design, data collection, analysis, or interpretation that distorts the true effect of an exposure on a disease.

**Confounding** occurs when a third variable is associated with both the exposure and the disease and distorts their apparent relationship.

**Recall bias** happens when cases and controls remember past exposures differently. *Example:* Mothers of children with birth defects may recall drug use during pregnancy more completely than mothers of healthy children.

**Attrition bias** happens when participants are lost to follow-up in a cohort study and those lost differ from those who remain. *Example:* Heavy smokers may drop out of a long-term smoking study, causing an underestimate of lung disease risk.

---

# 1.10 Summary

Epidemiology is the study of the distribution and determinants of health events in populations, applied to prevention and control. It differs from clinical medicine by focusing on groups rather than individuals.

Descriptive epidemiology uses the triad of person, place, and time. Outbreak investigations follow a clear eight-step protocol from verification to communication.

Basic measures include ratios, proportions, and rates. Prevalence measures existing disease burden, while incidence measures the speed of new cases. In a stable population, $P = I \times D$. Mortality is measured by crude death rate, cause-specific mortality rate, and case fatality rate.

Case-control studies move backward from disease to exposure and use the odds ratio. Cohort studies move forward from exposure to disease and use relative risk and attributable risk.

Screening tests are evaluated against a gold standard using sensitivity, specificity, predictive value, and negative predictive value. Predictive values depend on disease prevalence.

Bias and confounding can distort results. Selection bias, recall bias, and attrition bias are common, and confounders must be controlled through design or analysis.

---

# References and Further Reading

- Cox, D.R. and Oakes, D. (1984). *Analysis of Survival Data*. Chapman and Hall.
- Johnson, R.A. and Wichern, D.W. (2007). *Applied Multivariate Statistical Analysis*. Pearson.
- Rencher, A.C. and Christensen, W.F. (2012). *Methods of Multivariate Analysis*. Wiley.
- Sharma, S. (1996). *Applied Multivariate Techniques*. Wiley.
- Indira Gandhi National Open University. *MST-019: Epidemiology and Clinical Trials* study material. Available through [eGyankosh](https://egyankosh.co.in/books/mst-019).
