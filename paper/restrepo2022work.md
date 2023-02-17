---
parent: Papers
---

# Work from home and daily time allocations: evidence from the coronavirus pandemic

[html link](https://link.springer.com/article/10.1007/s11150-020-09497-9)

## BibTeX
```
@article{restrepo2022work,
  title={Work from home and daily time allocations: evidence from the coronavirus pandemic},
  author={Restrepo, Brandon J and Zeballos, Eliana},
  journal={Review of Economics of the Household},
  volume={20},
  number={3},
  pages={735--758},
  year={2022},
  publisher={Springer}
}
```

## Abstract

> Telecommuting has been on the rise in the U.S. and working from home may affect how workers allocate their time over the course of a day. In this paper, using a seemingly unrelated regression (SUR) framework, we examine differences in time spent in major activities between individuals who worked from home and away from home. We use data on prime working-age adults (age 25–54 years old) who participated in the 2017–18 Leave and Job Flexibilities Module of the American Time Use Survey. Results show that prime working-age American adults who worked from home during their diary day spent less time working and on personal care, but more time on leisure, sleeping, and on food production and consumption than those who worked away from home. For instance, among individuals with a spouse or partner present, those who worked from home spent 25 more minutes engaged in food production and 48 more minutes eating and drinking at home than did individuals who worked away from home, which are large relative to the sample averages of 33 and 31 min, respectively. These results show that there is important variation in the daily time allocation of workers in their prime working years and suggest in particular that working from home may allow for substantially more time to produce food and consume food at home, which may provide teleworkers with health benefits since home-produced meals tend to be lower in calories and higher in nutrients than meals prepared away from home.


## Notes and Excerpts

> Our main analysis sample consists of two subgroups of prime working-age adults (age 25–54):Footnote9 (1) respondents who are telework-eligible and worked only from home the day before their ATUS interview (worked from home [“WFH”]) and (2) respondents who worked only in their office or somewhere else the day before their ATUS interview (worked away from home [“WAFH”]). 


> To estimate the conditional association between working from home and the time spent in major activities (net of other observable differences between types of workers), we follow similar work on estimating the demand for sleep (Biddle and Hamermesh 1990; Ásgeirsdóttir and Ólafsson 2015). However, since we are interested in comparing the effects of working from home the day before their ATUS interview on multiple uses of time, we specified regression equations of the following form in a seemingly unrelated regression (SUR) framework,Footnote15
> 
>  $$T_i=α_1+α_2 \text{WFH}_i + βX'_i + γ \text{UR}_i + δ \text{STATE}_i+ϕ\text{INTERVIEW}'_i + ε_i$$
>
> where T is the (inverse hyperbolic sine transformed) time spent by individual i in a given activity {main work, personal care, leisure, sleeping, food production, or eating and drinking at home};Footnote16

- WFH is WFH dummy
- X is a vector of individual-level characteristics—age, age squared, gender, presence of household children dummy, education level, race/ethnicity, hourly worker dummy, full-time worker dummy, the logarithm of hourly wage, occupation dummies, telework eligibility dummy, and dummy for metropolitan area residence
- UR time and state specific unemployment rate
- STATE is state of residence dummy
- INTERVIEW is a vector of interview-related factors for individual i (dummies for year of interview, month of interview, and day of the week) that may affect time use;

Footnote 16:

> We transform the right-skewed activity variables in order to better approximate normal distributions. Specifically, we use the Stata command asinh (i.e. inverse hyperbolic since transformation) since we have observations with zero time use (i.e., respondents who did not engage in a given activity). Thus, the average percentage difference in time allocated to a given activity for a person who worked from home (relative to a person who worked away from home) is given by the formula $\exp(α_2)−1$.



> All analyses in this paper are consistent with BLS standards. BLS analyses using ATUS are generally conducted at the 90-percent level of confidence (BLS 2017b), so we also follow this convention in our analyses. Also, BLS determined that 77 observations was the minimum number of respondents who could support an ATUS cell estimate. Thus, all statistics presented in this paper are based on at least 77 respondents and 10 or more people who reported doing the activity. We only present participation rates in cases with fewer than 10 people who reported doing the activity, and we verified that the estimated standard error is less than 5 percent. For all other statistics with 10 or more people reported doing the activity, we verified that either the estimated standard error is less than 5 min or that the estimated coefficient of variation is less than 0.3.




TODO: Refresh understanding of generalized least squares.

https://www.statsmodels.org/dev/examples/notebooks/generated/gls.html

https://medium.com/keita-starts-data-science/heteroskedasticity-in-linear-regressions-and-python-16eb57eaa09


TODO: Compare SUR to [Multi-task LASSO](https://scikit-learn.org/stable/modules/linear_model.html#multi-task-lasso) or Multi-Task Elastic Net. Specifically re properties on time seires?



