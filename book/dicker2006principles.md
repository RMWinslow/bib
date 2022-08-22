---
parent: Books
---

# Principles of epidemiology in public health practice

[pdf copy from cdc](https://www.cdc.gov/csels/dsepd/ss1978/SS1978.pdf)

[html version of the text from the cdc](https://www.cdc.gov/csels/dsepd/ss1978/index.html)

## BibTeX
```
@article{dicker2006principles,
  title={Principles of epidemiology in public health practice; an introduction to applied epidemiology and biostatistics},
  author={Dicker, Richard C and Coronado, Fatima and Koo, Denise and Parrish, R Gibson},
  year={2006}
}
```

## My Notes on Measures of Risk


[This page in particular defines and explains many terms from the epidemiological literature](https://www.cdc.gov/csels/dsepd/ss1978/lesson3/section2.html).

See also the [cdc's glossary](https://www.cdc.gov/csels/dsepd/ss1978/glossary.html)


### Morbidity Frequency Measures

Morbidity means you're sick.

"**Incidence**" is used to refer to the speed at which *new* cases are appearing, while **prevalence** counts all active cases.

**Incidence proportion** / **Attack Rate** / **Risk**:

$$\frac{\text{new cases this period}}{\text{population at start of period}}$$

**Incidence rate** / **person-time rate**:

$$\frac{\text{new cases this period}}{\text{person-years of observation}}$$

**Secondary Attack Rate**:

$$\frac{\text{new cases among contacts}}{\text{total contacts}}$$

**Point prevalence**:

$$\frac{\text{Current cases (new and preexisting)  }}{\text{Population}}$$

**Period prevalence**:

$$\frac{\text{Number of cases throughout time period}}{\text{Average population during time-period}}$$



### Mortality  Frequency Measures

Mortality means you're dead. 

**Crude death rate**:

$$\frac{\text{deaths this period}}{\text{population this period}}$$

**Cause-specific death rate**:

$$\frac{\text{deaths from this disease, this period}}{\text{population this period}}$$

**Proportionate mortality**:

$$\frac{\text{deaths from this disease, this period}}{\text{all deaths this period}}$$

**Death-to-case ratio**:

$$\frac{\text{deaths from this disease, this period}}{\text{new cases of this disease this period}}$$


### Childbirth-specific terms

**Neonatal mortality rate**:

$$\frac{\text{deaths of children < 28 days old}}{\text{live births}}$$

**Postneonatal mortality rate**:

$$\frac{\text{deaths of children 28-364 days old}}{\text{live births}}$$

**Infant mortality rate**:

$$\frac{\text{deaths of children < 1 year old}}{\text{live births}}$$

**Maternal mortality rate**:

$$\frac{\text{deaths related to pregnancy this period}}{\text{live births}}$$

**Crude birth rate**:

$$\frac{\text{live births}}{\text{population}}$$

**Crude fertility rate**:

$$\frac{\text{live births}}{\text{women 15 to 44 years old}}$$

**Crude rate of natural increase**:

$$\frac{\text{live births - deaths}}{\text{population}}$$

### Measures of Association

**Risk Ratio**:

$$\frac{\text{Risk for group}}{\text{Risk for comparison group}}$$

$$= \frac{\text{new cases in group}}{\text{population of group}} \cdot  \frac{\text{population of comparison }}{\text{new cases in comparison }}   $$

**Rate Ratio**:

$$\frac{\text{Rate for group}}{\text{Rate for comparison group}}$$

$$= \frac{\text{new cases in group}}{\text{new cases in comparison}} \cdot  \frac{\text{person-years of observation of comparison}}{\text{person-years of observation of group}} $$

**Odds ratio**:
$$\frac{\text{exposed and diseased}\cdot \text{unexposed and no disease}}{\text{exposed and no disease}\cdot \text{unexposed and diseased}}$$
<!--
$$=\frac{Pr(diseased|exposed)}{Pr(diseased|unexposed)}$$-->

### Measures of Public Health Impact

**Attributable proportion** / **attributable risk percent**:

$$\frac{\text{Risk for exposed - Risk for unexposed}}{\text{Risk for Exposed}}$$

**Vaccine efficacy** / **vaccine effectiveness**:

$$\frac{\text{Risk for unvaccinated - Risk for vaccinated}}{\text{Risk for unvaccinated}}$$

equal to (1 - risk ratio) with unvaccinated as comparison group.



## Notes on Public Health Surveillance

**Notifiable conditions**

> A notification is the reporting of certain diseases or other health-related conditions by a specific group, as specified by law, regulation, or agreement. Notifications are typically made to the state or local health agency. ... When reporting is required by law, the diseases or conditions to be reported are known as **notifiable** diseases or conditions.

<!-- Individual notifiable disease case reports are considered confidential and are not available for public inspection. In most states, a case report from a physician or hospital is sent to the local health department, ... The local health department then forwards a copy of the case report to the state health department.... In some states all laboratory reports are sent to the state health department, which informs the local health department responsible for following up with the physician.

> This form of data collection ... is called **passive surveillance** (provider-initiated). Less commonly, health department staff may contact healthcare providers to solicit reports. This **active surveillance** (health department-initiated) is usually limited to specific diseases over a limited period of time-->

**Passive surveillance**
: Health provider sends reports on notifiable conditions to health department, as required by law.

**Active surveillance**
: Health department solicits reports, (such as during outbreak)

**Sentinel Reporting**
: A pre-arranged sample of providers agree to report all cases of certain conditions.

**Registries**
: Permanent legal records of a person's health events. Examples: Birth, death, cancer treatment.

### Major health data systems

- National Notifiable Disease Surveillance System (NNDSS)
  - The list of notifiable diseases varies from state to state
  - All states typically report quarantine-worthy diseases, like cholera, plague, and yellow fever
- Chronic disease data is less timely:
  - Hospital discharge records
  - public surveys
  - National Vital Statistics System
- Risk factor data (smoking, blood pressure, etc.) relies on surveys. Examples:
  - National Health and Nutrition Examination Survey (NHANES)
    - most comprehensive, source of famous data about lead exposure and second-hand smoke
  - Behavioral Risk Factor Surveillance System (BRFSS)
  - Youth Risk Behavior Surveillance System (YRBSS)
  - National Health Interview Survey (NHIS)
  -  National Household Survey on Drug Abuse 
-  Injuries: U.S. Consumer Product Safety Commission’s (CPSC) National Electronic Injury Surveillance System (NEISS) collects data 

[Here's a list](https://www.cdc.gov/csels/dsepd/ss1978/lesson5/appendixd.html) of more major health data systems

### Surveillance for Influenza

Flu is widespread each winter, but rarely confirmed by lab test.

Health authorities recieve reports of:

- Lab ID'd flu from nose swaps (rare)
- outbreaks of influenza-like illness
- reports from schools or businesses of excess absenteeism
- death certificates for pneumonia and flu (from some locations)
- number of flu-like patients (seen by selected physicians)
- pharmacy reports or antiviral drugs

One health department uses number of chest radiographs a mobile radiology group performs of nursing home patients as a metric.

7 Key data systems for assessing flu activity:
- 125 labs which send reports
- **U.S. Influenza Sentinel Providers Surveillance Network** receives reports from ~1000 providers
- **122 City Mortality Reporting System** tracks pneumonia/flu deaths from 122 locales
- Each state self-asses as “No Activity,” “Sporadic,” “Local,” “Regional,” or “Widespread.”
- **NNDSS** labels flu-related pediatric mortality as a notifiable condition
- **Emerging Infections Program** keeps track of lab-confirmed flu-related pediatric hospitalizations in 11 metro areas.



### Sucess of NDSS mandatory reporting

- For rare and serious diseases (rabies,plague), reporting rate near 100%.
- STD and tuberculosis reporting rate also very high
- But for some diseases, reporting rate very low
  - Shigellosis and other infectious diarrheas have maybe only 1 in 20 cases reported
  - Nonbloody diarrheas maybe 1 in 40

> Undoubtedly, the greatest stimulus to reporting was the prompt visit of the surveillance team for outbreak investigations and control whenever cases were reported. This simple, obvious, and direct indication that the routine weekly reports were actually seen and were a cause for public health action did more, I am sure, than the multitude of government directives which were issued.
> *--Henderson DA. Surveillance of smallpox*

#### On biases in reporting:

> First, health-care providers are more likely to report a case that results in severe illness and hospitalization than a mild case, even though a person with mild illness might be more likely to transmit infection to others because the person might not be confined at home or in the hospital. This bias results in an inflated estimate of disease severity in such measures as the death-to-case ratio. 
> 
> Second, health-care providers are more likely to report cases when the disease is receiving media attention. This bias results in an underestimate of the baseline incidence of disease after media attention wanes.
> 
> Both biases were operating in 1981 during the national epidemic of tampon-associated toxic shock syndrome. Early reports indicated a death-to-case ratio much higher than the ratio determined by subsequent studies, and reported cases declined more than incident cases after the publicity waned.  
> [--*source*](https://pubmed.ncbi.nlm.nih.gov/10603216/)