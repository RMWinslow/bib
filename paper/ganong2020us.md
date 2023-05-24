---
parent: Papers
---

# US unemployment insurance replacement rates during the pandemic

[NBER Summary Article](https://www.nber.org/digest/jul20/unemployment-benefit-replacement-rates-during-pandemic)

[ScienceDirect HTML](https://www.sciencedirect.com/science/article/pii/S0047272720301377)


## BibTeX
```
@article{ganong2020us,
  title={US unemployment insurance replacement rates during the pandemic},
  author={Ganong, Peter and Noel, Pascal and Vavra, Joseph},
  journal={Journal of public economics},
  volume={191},
  pages={104273},
  year={2020},
  publisher={Elsevier}
}
```

## Abstract

> We use micro data on earnings together with the details of each state's unemployment insurance (UI) system to compute the distribution of UI benefits after the uniform $600 Federal Pandemic Unemployment Compensation (FPUC) supplement implemented by the CARES Act. We find that between April and July 2020, 76% of workers eligible for regular Unemployment Compensation have statutory replacement rates above 100%, meaning that they are eligible for benefits which exceed lost wages. The median statutory replacement rate is 145%. We also compute comprehensive replacement rates, which account for employer provided non-wage compensation and differential tax treatment of labor income and UI. 69% of UI-eligible unemployed have comprehensive replacement rates above 100% and the median comprehensive replacement rate is 134%. The presence of the FPUC has important implications for the incidence of the recession and reverses income patterns which would have otherwise arisen across income levels, occupations, and industries.



## Notes and Excerpts

> construct quarterly earnings histories for workers using earnings data from the Current Population Survey Annual Social and Economic Supplement. They then apply the UI benefit formula for each state to calculate UI benefits, and they add payments under the CARES Act

> Because median lost wages are much lower than mean lost wages, and the CARES benefit boost was designed to generate a 100 percent earnings replacement for someone with mean earnings, total unemployment benefits now exceed lost wages for the median unemployed worker in every state. In Maryland, the median eligible unemployed worker receives benefits equal to 129 percent of lost earnings. In New Mexico, this value is 177 percent.

---

> Our baseline statutory replacement rate compares an unemployed worker's UI benefit to their lost wage earnings. However, we also compute a comprehensive replacement rate, which instead compares unemployment benefits to a broader measure of lost earnings which includes non-wage compensation like employer-provided health insurance and accounts for the differential tax treatment of labor income and UI.

> unlike in normal recessions, groups with dramatic declines in labor income during the pandemic do not necessarily have commensurate declines in overall cash flow once UI benefits are included

>  our paper is a purely descriptive analysis of the effects of UI supplements on household income, and we take no stand on optimal policy

> Models of the labor market which include relevant search frictions predict that workers should compare the flow value of unemployment to the expected present discounted value of a potential employment match. Just because a worker can temporarily earn more on unemployment than by working does not necessarily mean that they will turn down an offer of employment. Petrosky-Nadeau (2020) and Boar and Mongey (2020) estimate that even with the $600 supplement, most unemployed would accept an offer at their previous wages.

> Barrero et al. (2020) show that even in the peak period of job losses, there were many businesses with both gross and net hiring.


---

- a simulator for unemployment benefits by state
- micro data with earnings and labor force status from the Current Population Survey (CPS).


Ah, I was looking for this!
[a document from the government with a table of benefits formaulas](https://oui.doleta.gov/unemploy/content/sigpros/2020-2029/January2020.pdf).
The linked document is from 2020 January, but I'd bet I'll be able to find similar, more recent documents.

> Where states have multiple ways to qualify for unemployment benefits, we allow only the primary listed way in the document. We calculate benefit amounts for a single unemployed person with no dependents. We do not consider eligibility through alternative base periods. To find benefit amounts under the CARES Act we add $600 to benefit amounts from January 2020.


> We estimate the earnings history of the unemployed by combining data from the 2019 Annual Social and Economic Supplement (ASEC) of the CPS with information on the distribution of unemployment in the basic monthly CPS from April–July 2020

> Specifically, we study the probability of unemployment among CPS labor force participants in April, May, June, and July 2020 who also responded to a survey question about weekly earnings as part of the Merged Outgoing Rotation Group (MORG) in 2019.

They look at people who were laid off or have been unemployed less than 26 weeks, because this group seems most likely to be eligible for UI.
And although they can't see the highest earning quarter (for calcing WBA), they use ASEC to make an educated guess.

Use CPS sample (during pandemic) to fit the following model:

$$logit(P(unemployed)) = WageDecile + State + Occupation + Industry + noise$$

Then apply this fitted model to 2019 ASEC data.
The weight placed on each person is then the product of their statistical weight.
and of the model's predicted unemployment probability for that person.

---

> To assess the validity of our methodology, we compare our estimates to data on average benefits and pre-job loss earnings of actual UI claimants as reported by the Department of Labor.

---

They try to model "comprehensive replacement rate"
which incorporates payroll taxes and non-wage benefits.
They multiply employer-provided health benefits by 2.23 to estimate total non-wage benefits.

excluding tipped workers reduces estimates slightly, but the estimates remain quite high.

---


> the PUA program expanded UI eligibility to cover many workers with self-employment income. However, PUA is only available for workers who do not qualify for UC. This means that workers with enough wage income to qualify for UC must collect UC benefits even if they have self-employment income which exceeds wage income

They do something to deal with this. Not sure I follow.

> there are very few workers who qualify for UC based on wage income but also have sizable self-employment income







