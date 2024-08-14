---
parent: Papers
---

# The alpha beta gamma of the labor market

[Author's webpage](https://www.victoria-gregory.com/research)

## BibTeX
```
@techreport{gregory2021alpha,
  title={The alpha beta gamma of the labor market},
  author={Gregory, Victoria and Menzio, Guido and Wiczer, David G},
  year={2021},
  institution={National Bureau of Economic Research}
}
```

## Abstract

> Using a large panel dataset of US workers, we calibrate a search-theoretic model of the
labor market, where workers are heterogeneous with respect to the parameters governing
their employment transitions. We first approximate heterogeneity with a discrete number
of latent types, and then calibrate type-specific parameters by matching type-specific
moments. Heterogeneity is well approximated by 3 types: αs, βs and γs. Workers of type
α find employment quickly because they have large gains from trade, and stick to their
jobs because their productivity is similar across jobs. Workers of type γ find employment
slowly because they have small gains from trade, and are unlikely to stick to their job
because they keep searching for jobs in the right tail of the productivity distribution.
During the Great Recession, the magnitude and persistence of aggregate unemployment
is caused by γs, who are vulnerable to shocks and, once displaced, they cycle through
multiple unemployment spells before finding stable employment.


## Notes and Excerpts


> There are a couple of technical hurdles involved in carrying out the steps of our analysis.
First, we need to find a parsimonious way to measure workers’ heterogeneity, since estimating
individual-specific parameters for about half a million workers via maximum likelihood would
be too cumbersome. Second, we need to find a way to solve for the aggregate dynamics of an
equilibrium model in which workers are heterogeneous. We tackle these hurdles by using the
2-stage Grouped Fixed Effects (GFE) method of Bonhomme Lamadon and Manresa (2021) to
estimate a version of the directed search model of Menzio and Shi (2011).


> We access the **Longitudinal Employer-Household Dynamics (LEHD) dataset** between 1997 and 2014 and observe the history of employment transitions for over 500,000 individual workers. 

They record:
- time spent in unemployment,
- distribution of unemployment spell duration
- distribution of employment spell duration

And then perform k-means clustering with k=3.
Type α are most of population. They find new jobs fast and are slow to lose them.
Type γ are slow to find job and quick to lose them.
Third type is in between. 

> Interestingly, we
find that a worker’s type cannot be forecast by demographic characteristics and industry—a
finding that suggests that grouping workers by demographics and industry is not the best way
to approximate this form of heterogeneity.

Model allows workers to transition EE, EU, UE

> We calibrate the type-specific parameters of the model by matching type-specific moments,
such as the distribution of unemployment spell durations, the distribution of job durations, the
unemployment rate, the average earnings, etc...

Basically, in their model, the γ type choose to have less stable employment because the distribution of potential matches is highly variable. Whereas the α choose to stay put because they have good jobs, but not with much variance. (The latter is copacetic with my observations that it's doctors and so forth that tend to have stable employment. Not sure how the γ squares with temp agents and construction workers... I guess it might make sense.)

Some other things in their model:
- earnings losses from losing long-term job are larger and more persistent for gamma types.
- composition of unemployment pool tracks with what we see in the data (UE rate declines sharply with unemployment duration)
- In a simulation of aggregate shock, gamma types are impacted more. Their UE and EU rates are affected more because they are more likely to be in "marginal" positions where working is just barely worth it. And they are affected for a longer time because they have to sample several jobs again.
    - As a result, productivity dip is smaller and more transitory than employment dip.
    - This seems to match up pretty okayish with what was seen during the recession.

> The size and persistence of the increase in type-specific
unemployment during the Great Recession are qualitatively similar to the predictions of the
model in response to an aggregate productivity shock, but the magnitude of the decline in labor
productivity is smaller and more transitory than as predicted by the model.


*(Does the model just have workers choosing to leave? No firing? That's interesting that you can generate the patterns with just worker choice, because the intuitive story might be that type gamma workers are somehow "bad" at keeping jobs.)*

---

>  The main contribution of the paper is to provide a
coherent, calibrated, and tractable framework that explicitly takes into account the fact that
workers are very different with respect to the speed at which they move from unemployment
to employment, the frequency at which they become unemployed, the amount of time they
spend on different jobs, and that this heterogeneity runs deeper than the differences in average
transition rates between workers with different observable characteristics.

TODO: Come back and take a look at their lit review. This general research question is something very interesting to me.

---

> **Much work remains to be done. First, we need to understand what determines the type of worker, since basic demographics, industry and location cannot forecast types. In order to shed more light on this question, we would need to access a dataset containing more information about individuals (such, as say, the NLSY). Second, we need to understand whether a worker’s type is permanent or transitory. Given the limitations of our data, we maintained that a worker’s type is fixed—even though preliminary analysis shows that a worker’s types before and after the Great Recession are very highly correlated. Relatedly, it would be interesting to access a longer panel dataset to understand whether the composition of the population by type has changed over time and, in turn, whether such change may be responsible for the changing nature of labor market fluctuations. Lastly, it would be interesting to connect the insights of  these papers to optimal policy. Once we acknowledge that workers are heterogeneous in their search process, how should unemployment insurance be redesigned?**



### LEHD Data

See here: https://www.census.gov/programs-surveys/ces/data/restricted-use-data/lehd-data.html

It looks like there are some summary stats available to public, 
and microdata available to certain workers.

> In order to access LEHD microdata, researchers must have an approved project with authorization to use specific data sets. Researchers must also demonstrate that they cannot conduct their research using public-use data sources, and they must identify the ways in which their project will benefit both the objectives of the U.S. Census Bureau and the broader research community. All researcher access to restricted–use data occurs at one of the secure Federal Statistical Research Data Centers (FSRDCs).

(No FSRDC in South Dakota, of course. There is one in Lincoln.)





