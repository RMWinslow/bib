---
parent: Papers
---

# Children, time allocation, and consumption insurance

[html link](https://www.journals.uchicago.edu/doi/10.1086/698752)

## BibTeX
```
@article{blundell2018children,
  title={Children, time allocation, and consumption insurance},
  author={Blundell, Richard and Pistaferri, Luigi and Saporta-Eksten, Itay},
  journal={Journal of Political Economy},
  volume={126},
  number={S1},
  pages={S73--S115},
  year={2018},
  publisher={University of Chicago Press Chicago, IL}
}
```

## Abstract

> We study choices of households deciding on consumption and allocation of spouses’ time to work, leisure, and child care. With uncertainty, the allocation of goods and time over the life cycle also serves the purpose of smoothing marginal utility in response to shocks. Combining data on consumption, wages, hours of work, and time spent with children, we compute the sensitivity of consumption and time allocation to transitory and permanent wage shocks. We find that family labor supply responses depend on three counteracting forces: complementarity of leisure time, substitutability of time in the production of child services, and added worker effects.


## Notes and Excerpts

> To address these issues we derive structural marginal rate of substitution relations between leisure time of the two partners, the time they allocate to child care, consumption, and prices (hourly wages). We estimate a subset of the structural parameters of the model using data from three data sets: the Panel Study of Income Dynamics (PSID), the American Time Use Survey (ATUS), and the Consumer Expenditure Survey (CEX). We use the latter to impute consumption to all household units in the ATUS (where no consumption information is available). We then use numerical simulation of the model to recover the remaining preference parameters.

- PSID has data on consumption, labor time and wagerates. But PSID lacks consistent data on childcare time. It has some supplementary data in the "the Child Development Survey (CDS)", but that has limitations.
- ATUS has detailed information on time use for primary respondent and has wage data, but lacks info on spouse/partner time use. Also lacks info on consumption.
- "We then impute this information using cohort-education-year average values of parental time and hourly wages (from the ATUS male respondents) and household consumption (from the CEX)."


> the responses of the two subutility margins are of opposite signs, highlighting the tension between substitutability and complementarity in driving the hours response. In particular, the hours of work of young mothers appear to respond little to a temporary increase in the male’s wage (which induces an increase in his hours) because the force that pushes her to reduce her leisure time (or work longer) due to the lower leisure time of her companion is counteracted by the force that pushes her to increase child care time because the husband is now allocating fewer hours to child raising and her time is a substitute for his time in the household production of child care services


### PSID Data

> Since 1999, in addition to income data and demographics, the PSID collects data about detailed asset holdings and consumption expenditures. Since we need both consumption and assets data (the latter to construct instruments), we focus on interview data from the 1999–2015 sample period. 

That has all the info needed except time spent on child care.

For the estimation of eq 7 and 8, 
Sample restricted to married couples where wife is 25-65, with no young children (age 10 or less) present.

> In this sample parental time is zero by assumption, and hence leisure time can be obtained as the difference between total time available and hours of work.

Further data restrictions:
- no missing data on consumption or education of both earners
- drop observations where one of the earners is working 60+ hours a week for the entire year

Similar to blundell2016consumption, consumption categories are food, health expenditures, utilities, gasoline, car maintenance, transportation, education, child care, home insurance, and rent or rent equivalent 

> In the 2015 wave, because of an error in the PSID data collection procedure, the data on car maintenance are missing whenever a car insurance value is reported. We impute these values using a within-household projection of the car maintenance budget share on all other transportation-related budget shares as well as the food budget share.

Also data clipped at top and bottom one percent


### ATUS Data

<!--
> One respondent per household (either the husband or wife in couple households) reports detailed information on how he or she spent his or her time on the previous day. The matching with the CPS can be used to recover demographic information for the respondent and the spouse (including his or her hourly wage), although some information is updated at the time of the ATUS interview.
-->

> Our definition of child care time includes caring for and helping household children (activity codes 030101–030199), activities related to household children’s education (activity codes 030201–030299), activities related to household children’s health (activity codes 030301–030399), and travel related to caring for children (180381). 

> **Separately for each year, we impute child care time of the husbands of wife respondents by computing the average child care time of all husband respondents (averaged over their wives’ birth cohort and education, which are always observed).**


Looks at HH with young child.
Drops weekend and holiday observations.

> Unfortunately, the ATUS does not contain any information about consumption. We hence impute consumption using data from the CEX, described next. Separately for each year, we impute to each ATUS household the average level of consumption observed in the CEX for households with the same wife’s birth cohort and level of education.

> among working married couples with a child aged 10 or less, about 31 percent of husbands and 8 percent of wives report zero hours spent with their kids

This is due to the diary nature of the data. And it doesn't mean a third of fathers *never* spend time with their kids.
For example, maybe on the diary day, the father left home early and didn't come back until after kid went to sleep.
Or maybe he was out of town on a business trip, etc.

For this reason, the authors focus on wife's child care time.
Unfortunately, in ATUS you only get to see the time use of one HH member.
That's why husband child care time is imputed as described above.


### CEX Data

There is an interview survey, where participants are asked to recall their spending each quarter for a year.
And a diary survey, where participants are sampled once and fill in a 2-week diary.

They focus on interview data and define nondurable consumption as:

> nondurable consumption defined as the sum of spending on food at home, food away from home, alcohol and tobacco, utilities, maintenance and repairs, education, housing services, financial services, clothing, health, entertainment, cash contributions, transportation, and other nondurables. We then deflate using the CPI.

And they exclude rural households (possibly because CPI looks at urban HHs?) those with incomplete income responses and those with zero consumption.



---

Estimates for wage process parameters come from blundell2016consumption

### Effects of a simulated shock to wages

- If husbands wage goes up temporarily: 
    - If no kids, wife's timeuse doesn't respond much. There's a wealth effect, but Wife's also leisure becomes less valuable because husband/wife leisure are complements.
    - If kids, wife works less in response because they have to compensate for reduced childcare time from husband.
- Own permanent wage elasticities are positive, meaning substitution effect dominates. Women respond more, which is typical result in labor supply literature.
- If husband's permanent wage increases, he has less leisure and child care time. Wife works less and spends more time on childcare. If wife's permanent income increases, there is a similar story, except husband increases leisure more than childcare, and total childcare time declines.

> a 10 percent permanent decline in the male’s hourly wage results in a 3.9 percent decline in consumption. Savings and taxes attenuate the response of consumption relative to after-tax and transfers household earnings (a 5 percent decline)

<!--
TODO: Try to understand the big ol' utility function they're using.
-->

<!--
Effect of shocks in model:

> The hours cross-responses are also interesting. When the husband’s wage increases temporarily, so that he works longer hours, wives in households without kids respond very little. This reflects pure leisure nonseparability: spouses enjoy spending nonworking time together, along with small wealth effects of the transitory shock, giving rise together to virtually no response of leisure or hours. However, hours are reduced (−0.08) in households with kids because wives now have to confront the decline in child care time of the husband, for which her child care hours are substitutes. While these effects are small, they are consistent with the idea that the presence of young children can affect cross–labor supply responses.

> The fact that the own permanent wage elasticities are positive implies that the substitution effect dominates. Hence, permanent declines in wages induce declines in labor supply for both partners (albeit larger for women, a traditional result in the labor supply literature).

> For women in couples without young kids, a permanent decline in the husband’s wage means he works less and earns less. She works more because of an added worker effect. In couples with children, husbands who work less allocate some of their leisure time to children, implying that the wife can work more because of substitutability effects in home production of child services.

- Permanent decline in husband's wage:
    - without kids, Wife works more
    - with kids, husband works 
-->



---

### Notes for teachings

Household's problem is complex but might be a good teaching example.

Here's a big quote related to their choice of borrowing constraint:

> While our assumption of an exogenous borrowing constraint is a frequent characterization of borrowing limits in life cycle models of consumption and labor supply, it is not uncontroversial. Several papers consider instead “natural borrowing constraints” à la Aiyagari (1994), in which (because of an Inada condition on preferences) households never choose to have a level of assets that could induce, with positive probability, a future state of the world in which consumption is exactly zero. In this sense, the borrowing limit is the maximum amount that an individual can repay with certainty. As shown by Hai and Heckman (2017), this notion of natural borrowing constraints needs rethinking in a context with endogenous labor supply or human capital investments, since lenders cannot force individuals to work or to invest in human capital to repay their debt. As a consequence, the borrowing limits imposed by lenders must take into account the incentive compatibility constraints of the borrowers. While these are important theoretically based versions of borrowing limits, endogenizing the nature of liquidity constraints is beyond the scope of our paper.

In 3102, we use the "natural borrowing constraints" described. They feel that putting those into the model would induce too many complications. Instead they go with the very very simple restriction that assets must be non-negative.
HHs are allowed to borrow in a period, in the sense of consuming more than they earn, but only if they had saved enough in some previous period.



