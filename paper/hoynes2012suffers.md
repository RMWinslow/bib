---
parent: Papers
---

# Who suffers during recessions?

[Author's Webpage](https://www.hilaryhoynes.com/research),
[direct pdf link](https://static1.squarespace.com/static/5ecd75a3c406d1318b20454d/t/5f45c30b500be76b442dcaff/1598407436928/Hoynes-Miller-Schaller-JEP-2012.pdf),


## BibTeX
```
@article{hoynes2012suffers,
  title={Who suffers during recessions?},
  author={Hoynes, Hilary and Miller, Douglas L and Schaller, Jessamyn},
  journal={Journal of Economic perspectives},
  volume={26},
  number={3},
  pages={27--48},
  year={2012},
  publisher={American Economic Association}
}
```

## Abstract

> In this paper we examine how business cycles affect labor market outcomes in the United States. We conduct a detailed analysis of how cycles affect outcomes differentially across persons of differing age, education, race, and gender, and we compare the cyclical sensitivity during the Great Recession to that in the early 1980s recession. We present raw tabulations and estimate a state panel data model that leverages variation across US states in the timing and severity of business cycles. We find that the impacts of the Great Recession are not uniform across demographic groups and have been felt most strongly for men, black and Hispanic workers, youth, and low education workers. These dramatic differences in the cyclicality across demographic groups are remarkably stable across three decades of time and throughout recessionary periods and expansionary periods. For the 2007 recession, these differences are largely explained by differences in exposure to cycles across industry-occupation employment.

## Notes and Excerpts

They leveraged variation in state-month unemployment to look at the effect of recessions on different groups.

Contributions of paper:

>  Our study builds on a large existing literature in labor economics and macroeco
nomics on how business cycles affect outcomes for workers and families, including 
our own prior work (Bitler and Hoynes 2010; Hoynes 2000; Hines, Hoynes, and 
Krueger 2001; Stevens, Miller, Page, and Filipski 2011). Our study makes several 
contributions to this existing literature. First, our primary focus is identifying differ
ences in the cyclicality across demographic groups. Second, we present the results 
of statistical tests for differences in the cyclicality both across groups (for a given 
time period) and over time (for a given group). Third, by using data through the 
end of 2011, we highlight the results for the Great Recession and compare them to 
the early 1980s recession. Finally, we compare the recovery periods following the 
two most severe recessions in our time frame: the recession(s) of the earlier 1980s 
(counted as one recession) and the 2007–09 recession


Regression is 

$$
y_{gst} = \beta_g UN_{st} + RaceSex_g + Age_g + Educ_g + \alpha_s + \delta_t + year_t \gamma_s + \varepsilon_{gst}
$$

Subscripts are $g,s,t$ for group, state, time.
Group specific intercepts $RaceSex_g, Age_g, Educ_g$.
State and time fixed effects $\alpha_s, \delta_t$.
State-specific time trends $\gamma_s$ (?).
Main thing they're interested in is that $beta$ there, which is group sensitivity to unemployment rate.

Also: 
> We use the Current Population Survey population weights for each cell, and *we conduct statistical inference clustering on U.S. states. ... Our approach is similar in spirit to equation 7 and Table 2 in Blanchard and Katz (1992)*

>  A final important difference between the two approaches is that the 
regression results are not only estimated over the recession periods, but instead are 
estimated using data from both contractions and expansions.


To compare recessions, they estimate different $\beta$s for the different time periods and then test whether they are different.

Overall punchlines are:
- Great recession is bigger than previous recessions, but otherwise very similar.
- Men are affected more deeply by recession but also recover more quickly as a group.

