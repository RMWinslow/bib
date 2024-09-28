---
parent: Papers
---

# Variance decomposition analysis: What is it and how to perform it

[ScienceDirect Link](https://www.sciencedirect.com/science/article/pii/S0019850122002590)

## BibTeX
```
@article{zaefarian2022variance,
  title={Variance decomposition analysis: What is it and how to perform it--A complete guide for B2B researchers},
  author={Zaefarian, Ghasem and Iurkov, Viacheslav and Koval, Mariia},
  journal={Industrial marketing management},
  volume={107},
  pages={315--322},
  year={2022},
  publisher={Elsevier}
}
```

## Abstract

> Variance decomposition analysis allows partitioning the total variance in an outcome variable, e.g., firm performance, into several components. Such partitioning allows identifying groups of factors (e.g., firm-, industry-, and country-specific) that explain a significant portion of the variation in firm performance, thus helping researchers, managers, and policymakers better understand the sources of competitive advantage. The present study aims to inform scholars, particularly those in business-to-business (B2B) marketing, about the benefits of utilizing variance decomposition analysis and draw scholarly attention to the relevant statistical techniques needed to produce accurate estimates. We specifically point to multilevel modeling techniques due to their significant advantages over other approaches to decompose the variance in a given outcome variable. We provide a detailed step-by-step guide as well as the related Stata codes on conducting variance decomposition analysis with multilevel modeling techniques. Using a 10-year (2009–2018) dataset comprising 7281 distinct European B2B firms operating in 348 industries and 29 countries, we empirically examine the relative importance of firm, industry, country, year, and residual effects in driving firm performance for B2B firms. Our analysis shows that firm-specific factors have the highest relative importance for B2B firms' performance, followed by home country and industry effects.


## Notes and Excerpts


>  In parallel, there has been an advancement in methodological approaches from more basic ones, such as analysis of variance (ANOVA) (
McGahan and Porter, 1997
, 
McGahan and Porter, 2002
), to multilevel modeling with maximum likelihood estimation (
Hough, 2006
; 
Karniouchina, Carson, Short, & Ketchen, 2013
; 
Misangyi et al., 2006
) or more complex estimation methods involving Bayesian Markov chain Monte Carlo (MCMC) algorithms (
Castellaneta & Gottschalg, 2016
; 
Guo, 2017
).


> Earlier studies utilizing variance decomposition analysis to estimate components of firm performance relied on two approaches: variance components analysis (VCA) or analysis of variance (ANOVA) (e.g., 
McGahan and Porter, 1997
, 
McGahan and Porter, 2002
; 
Rumelt, 1991
). Although these studies provided a step forward in enhancing our understanding of the “general importance of industry, corporate, and business effects on firm performance” (
McGahan & Porter, 2002
: 835), VCA and ANOVA have been found to have several critical limitations (
Bowman & Helfat, 2001
; 
Brush & Bromiley, 1997
).

> Compared to VCA, ANOVA is more robust to deviations from these assumptions, producing more consistent and reliable empirical findings (
Garson, 2012
). At the same time, the main limitations of ANOVA are that it provides no explicit variance decomposition (i.e., the result differs depending on how the effects enter the model) and does not allow to capture interaction effects adequately (
Hoffman, 2015
). 

> Multilevel modeling (MLM), also known as hierarchical linear modeling, allows addressing the discussed limitations of both VCA and ANOVA (
Hoffman, 2015
). First, MLM directly decomposes variance in the outcome variance into each level (
Hoffman, 2015
), relaxing the assumption of independence of lower-level units nested in higher-level units. Second, MLM ensures efficient estimation of unbalanced data, preventing the loss of information


-----


1. Define categories of explanatory variables.
2. get data
3. identify possible subsamples
4. data cleaning
5. model specification and estimation


Here's the important bit:

<!--
> variance decomposition studies normally require a sizeable amount of lower-level observations (e.g., firms nested in industries or countries). Also, to separate residual effects from firm effects, the data should have a panel structure
-->

> We utilize two existing approaches to performance variance decomposition: multilevel modeling with maximum likelihood estimation (e.g., 
Hough, 2006
; 
Misangyi et al., 2006
) and multilevel modeling with MCMC estimation in a Bayesian framework (e.g., 
Castellaneta & Gottschalg, 2016
; 
Guo, 2017
). The former approach has been more standard in the variance decomposition research, and it can be easily implemented using standard statistical software, such as using the “mixed” command in Stata. The latter approach has been introduced to the management literature relatively recently; one of its benefits is that it allows obtaining reference statistics, such as standard error, for both the absolute effects (variances) and relative effects (percentages) of different variance components (
Browne, 2017
).

### Multi-level modelling with MLE

In their example, let $t,i,j$ denote time, firm, industry.

In Model 1:

$$ROA_{tij} = \alpha_{0ij} + e_{tij}$$

$$\alpha_{0ij} = \beta_{00j} + u_{ij}$$

$$\beta_{00j} =   \gamma_{000} + v_j$$

The $e,u,v$ represent residuals at the observation, between-firm, and between-industry level.
The $\gamma_{000}$ term is the "grand-mean" ROA for all observations.

The calculation for variance attributable to each level is as you'd expect.
For example, in this model, the proportion of variance between firms is

$$\sigma^2_u \over (\sigma^2_e + \sigma^2_u + \sigma^2_v)$$

Now suppose you want to include a variable like YEAR which can't be nested in the above.
Then set up Model 2 like so:

$$ROA_{tij} = \alpha_{0ij} + \alpha_{1ij}YEAR_{tij} + e_{tij}$$

$$\alpha_{0ij} = \beta_{00j} + u_{ij}$$

$$\beta_{00j} =   \gamma_{000} + v_j$$

Portion of variance explained by year effects is then:

$$\sigma^2_{e,model1} - \sigma^2_{e,model2} \over (\sigma^2_e + \sigma^2_u + \sigma^2_v)_{model1}$$

Now add (home) country effects at firm level:

Model 3:


$$ROA_{tij} = \alpha_{0ij} + \alpha_{1ij}YEAR_{tij} + e_{tij}$$

$$\alpha_{0ij} = \beta_{00j} + \beta_{01j}COUNTRY_{ij} + u_{ij}$$

$$\beta_{00j} =   \gamma_{000} + v_j$$

And to get country effects, observe decrease in variance at firm and industry levels:

$${\sigma^2_{u,model2} - \sigma^2_{u,model3} \over (\sigma^2_e + \sigma^2_u + \sigma^2_v)_{model2}} + {\sigma^2_{v,model2} - \sigma^2_{v,model3} \over (\sigma^2_e + \sigma^2_u + \sigma^2_v)_{model2}}$$

This isn't quite intuitive to me. Why for YEAR do we look only at that level, but for COUNTRY we look at that level and the one above it?

---


They also look at "Multilevel modeling with MCMC estimation in a Bayesian framework", but don't have mathematical details in this paper, just instructions on a STATA package to use for that kind of analysis.


