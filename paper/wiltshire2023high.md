---
parent: Papers
---

# High Minimum Wages and the Monopsony Puzzle

[working paper](https://irle.berkeley.edu/wp-content/uploads/2023/05/High-Minimum-Wages-and-the-Monopsony-Puzzle.pdf)


## BibTeX
```
@article{wiltshire2023high,
  title={High Minimum Wages and the Monopsony Puzzle},
  author={Wiltshire, Justin C and McPherson Carl and Reich Michael},
  year={2023},
}
```



## Abstract

> We present the first causal analysis of recent large minimum wage increases, focusing on 47
larger U.S. counties that reached $15 or more by 2022q1. Using stacked county-level synthetic control estimators, we find substantial pay growth, no disemployment effects and reduced wage inequality. Our novel procedure ameliorates pandemic-related bias. We pose and
address a monopsony puzzle: Researchers often invoke monopsony to explain absent negative
employment effects, yet the model generally predicts positive employment effects. When we
reduce selection and attenuation biases—by excluding areas with local minimum wages and
high-wage counties—we find large, significant positive employment effects.


## Notes and excerpts

### Data Sources

> We use the Quarterly Census of Employment and Wages (QCEW) administrative data for our
county-level and state-level analyses. The QCEW data covers about 95 percent of all U.S. payroll
jobs. For our fast food analysis, we restrict the QCEW data to private sector workers in NAICS
722513.20 For our restaurant-focused analysis, we restrict the QCEW data to private sector workers
in the California restaurant industry (NAICS 722)... 
We cannot distinguish whether changes in weekly earnings result from
changes in hourly pay rates or changes in the number of quarterly hours. However, previous research (Nadler et al. 2018) has demonstrated the small variation in quarterly hours in the QCEW

> Our data on hourly wage distributions come from the CPS Outgoing Rotation Group (ORG) samples, beginning in 2009q4 and continuing through 2022q2. We make standard restrictions to the
samples, such as excluding self-employed individuals and individuals who did not respond to the
wage questions. We restrict the data to workers in the contiguous U.S. who reside in California,
New York and the 20 states that did not experience any minimum wage changes since July 2009

> As the unemployment rate is an important predictor of our outcomes of interest, we include it as a
covariate in our analyses. We obtain annual county-level unemployment rates from the Bureau of
Labor Statistics’ Local Area Unemployment Statistics (LAUS) program. Using the LAUS, we also
calculate annual state-level unemployment rates for our state-level analyses.

> We use Google’s Community Mobility Data as aggregated by Chetty et al. (2020) to construct an
index of the effects of these local pandemic responses on economic activity in fast food restaurants.

---

### Methods

"Stacked sythentic control method"

> For a given outcome of interest, our synthetic control estimator selects weights to best match an
individual treated unit to a subset of untreated “donor pool” units along specified dimensions in the
pre-treatment period. The resulting weighted average of donor pool unit outcomes is the synthetic
control estimate of the counterfactual dynamic outcome path. Under fairly general assumptions and
with a good pre-treatment “fit” between the treated unit and its synthetic control, the difference in
the two dynamic outcome paths yields the estimated treatment effects. 


I wonder if I can find a python implementation of synthetic controls. Concept seems pretty straight forward.

The weights on "donor pool units" are like probability weights (in the sense they are non-negative, summing to 1), and are chosen to minimize some measure of distance between a treated individual and their synthetic control.

Fit is chosen for first half on control period,
then evaluated for rest of control period.
Then post treatment period used to estimate effect of intervention.

Some complicated stuff to try to adjust for effect of pandemic.
Plus some attempts for selection and attenuation; places that enact minimum wage rises tend to have higher wages to begin with, for example.



### Results

> Panel A of Table 2 also shows that the minimum wage policies increased employment 9.1 percent
in the treated counties. The placebo-variance-based 95 percent confidence intervals rule out an
employment elasticity with respect to the minimum wage below 0.05. The own-wage elasticity of
0.55 (s.e. = 0.15) is somewhat more positive than the 0.41 OWE for all workers in Cengiz et al.
(2019), while our [0.05, 0.14] 95 percent confidence interval on employment is much narrower
than their [-0.5, +1.13] confidence interval.37 The RMSPE-based p-value of 0.13 suggests our
positive estimated employment effect is only borderline significant, suggesting caution in drawing
a confident causal inference of a positive employment effect

My thoughts: standard "monopsony" model is firm doesn't want to hire more people because they'd need to raise the wage to do that. Higher minimum wage forces them to raise wage. And since the wage is higher anywaysthey I figure they might as well hire more people. Now after the pandemic businesses were very hesitant to raise wages had difficulty hiring people as a resultandthat seems like exactly the kind of situation where minimum wage rate raise would increase employment even though I wouldn't call quite call that a monopsony situation.Is there some other model besides just a pure monopsony in which firms are able to choose to have lower employment and wages some model of search frictions perhaps. (Changes enacted in CA starting back in 2014, reached 15 in 2022)

Little effect on median wage, so wage inequality mechanically decreased as well.

> In conjunction with the raw earnings patterns evident in Figure 3, these results suggest that labor
supply to the fast food sector was better-sustained and recovered more quickly in treated counties,
where the financial reward for working a fast food job was higher. At the same time, fast food
employers in untreated counties rapidly increased wages in response to the labor shortage they
faced.



---

> These funds included lump-sum stimulus checks of $1,200 per adult and $600 per child in April 2020 and subsequent payments of $600 and $1,400 (https://www.usa.gov/covid-stimulus-checks); uniform enhancements of $600
weekly to unemployment benefits, implying median wage replacement rates of 145 percent nationally, and higher still in
food service industries and in donor states (Ganong and Vavra, 2000); and relief funds of $150 billion issued to cities and
counties on a per capita basis (https://www.nlc.org/covid-19-pandemic-response/american-rescue-plan-act/arpa-localrelief-frequently-asked-questions/ARPA-info). In normal times, UI replacement rates rarely exceed 50 percent and are
generally lower in our donor states.


---

What about hours? Did min wage hikes affect intensive margin for employers?
I see a positive result on hours for teen employees, but not for the general data.
Maybe they couldn't estimate that number, or maybe I just missed it when reading.




