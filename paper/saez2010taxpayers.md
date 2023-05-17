---
parent: Papers
---

# Do taxpayers bunch at kink points?

[AEA link](https://www.aeaweb.org/articles?id=10.1257/pol.2.3.180).
[NBER pdf link](https://www.nber.org/system/files/working_papers/w7366/w7366.pdf)


## BibTeX
```
@article{saez2010taxpayers,
  title={Do taxpayers bunch at kink points?},
  author={Saez, Emmanuel},
  journal={American economic Journal: economic policy},
  volume={2},
  number={3},
  pages={180--212},
  year={2010},
  publisher={American Economic Association}
}
```

## Abstract

> This paper uses tax return data to analyze bunching at the kink points of the US income tax schedule. We estimate the compensated elasticity of reported income with respect to (one minus) the marginal tax rate using bunching evidence. We find clear evidence of bunching around the first kink point of the Earned Income Tax Credit but concentrated solely among the self-employed. A simple tax evasion model can account for those results. We find evidence of bunching at the threshold of the first income tax bracket where tax liability starts but no evidence of bunching at any other kink point.



## Notes and excerpts


Final version seems quite different. Just reading the abstracts, the working paper doesn't talk about EITC, for example.


> Our empirical analysis uses the 
large annual tax return data publicly released by the Internal Revenue Service (IRS)
since 1960.

> A large body of work has shown strong evidence of behavioral responses to the EITC along the extensive 
margin, i.e., the decision to participate in the labor force. Evidence of behavioral responses along the intensive 
margin (i.e., hours of work conditional on working) is weak or absent (see Nada Eissa and Hilary Hoynes 2006 and 
V. Joseph Hotz and John Karl Scholz 2003 for recent surveys)


For EITC, they find very strong evidence of bunching for the self-employed
but not for wage earners. They suggest it's a matter of reporting rather than 
actually affecting the labor supply.
(My thought though: Could it not instead be a matter of labor flexibility?)

amount of bunching grows over time

> many taxpayers do not know their marginal tax rate or report it with 
substantial error (e.g., Edwin T. Fujii and Clifford B. Hawley 1988 for US evidence)


Raj Chetty et al. (2009) similarly finds bunching at big kink near top of tax bracket,
but not much evidence for bunching at smaller kink points.
Other papers for example find bunching from Social Security earnings limits, 
UK family credit (which has 16 hour working requirement),
age bunching due to pension programs,

---

### EITC Thresholds (approx)

For years 1995-2008, in 2008 dollars:
(Maybe also for later years.)

|  | 1 Kid (brackets) | 1 Kid (emtr) | 2+ Kids | 2+ Kids (emtr) |
|:-:|:-:|:-:|:-:|:-:|
| Phase in | 0-8580 | -34 | 0-12060 | -40 |
| Plateau | -15740 | 0 | -15740 | 0 |
| Phase Out | -33995 | 16 | -38646 | 21 |



---

### measuring elasticity and bunching


$$\gdef\KINKPOINT{z^\star}$$

$$\gdef\KINKWIDTH{dz^\star}$$

At pre-tax income level $\KINKPOINT$, tax rate goes from $t$ to $t+dt$.
Define width of kink point $\KINKWIDTH$ 
such that person who would earn up to $\KINKPOINT+\KINKWIDTH$
at tax rate $t$ instead only earns $\KINKPOINT$ at tax rate $t+dt$.

Total number of people earning at the kink point 
is $h(\KINKPOINT)\times\KINKWIDTH$, 
where $h()$ is
smooth density distribution of incomes when there isn't a kink point.

Let $e$ be "compensated elasticity of earnings wrt to 1 minus the tax rate"
By definition, $e$ satisfies

$$\frac{\KINKWIDTH}{\KINKPOINT} = e\frac{dt}{1-t}$$

- larger elasticity should mean more bunching
- amount of bunching should be determined by ratio $\frac{dt}{1-t}$ (0 to 10 should produce same amount as 90 to 91)
- they say with heterogeneity in elasticity, the amount of bunching should still be proportional to the average compensated elasticity

quasilinear utility for simplicity (so they don't have to worry about the difference between compensated and uncompensated elasticities)

---

mentioned explanations for why wage earners don't bunch:
- low intensive elasticity
- may not understand the structure of the EITC (surveys suggest this is plausible)
- lack flexibility to adjust hours (because employers impose hours constraints)
- stochastic earnings or work opportunities make control of exact earnings difficult
- inability to misreport earnings (because third party reports income), (whereas they mention evidence that some 80 percent of "small informal business suppliers" underreport income)

Bunching only started being obvious in 1991, when EITC subsidy rate went over 16 percent.
Explanation they propose:
- Social Security and Medicare tax the income at 15.3 percent
- If EITC subsidy above 15.3 percent, then there is an incentive to report income near the low end(effective marginal tax rate is negative)
- Then the first kink point in EITC, where the income subsidy stops, is the point that maximizes transfers from the government.
- There might also be over-reporting

They focus on the misreporting explanation. See below.

There is similarly bunching only around the first kink in Federal Income Tax (where liability starts)
They have more difficulty explaining this. Maybe higher elasticity or hours flexibility at the low end.
(My intuition is that the flexibility is the main factor. Higher-end incomes are most salaried, right? That's something I could check, perhaps...)


---

### Simple model of tax avoidance

- Assume people have formal earnings $w$ and informal earnings $y$
    - $\hat y$ are the informal earnings reported
- Both are smoothly distributed and don't respond to taxes.
- net disposable income is such that :

$$c = w+y - T(w+\hat y)$$

To get bunching only at the first kink point:
- assume linear preferences 
- with fixed costs $q_A$ of reporting $\hat y > 0$.
- As suggested by data, impose constraint that $\hat y \geq 0$, because negative $\hat y$ is likely to trigger an audit (data has negative self-employment income, but these aren't responsible for the bunching)
- also a "moral fixed cost" $q_M$ of misreporting income 

Assuming utility is quasilinear in disposable income, goal is to choose $\hat y$
to maximize

$$\gdef\INDICATOR#1{\mathbb{1}_{(#1)}}$$

<!--alas, I think \mathbb lacks support for numbers-->

$$w+y - T(w+\hat y) - q_A \INDICATOR{\hat y > 0} - q_A \INDICATOR{\hat y \neq y}$$

Furthermore, assume transfer payments are singly peaked at $-T(z^\star)$, 
where $z^\star$ is the income that results in this amount of transfers.
(EITC plus payroll taxes does result in a singly peaked transfer at a positive income level).
If EITC subsidy smaller than payroll tax


Under these assumptions they proove the optimal self reported $\hat y$ is one of:
- The truthful value $\hat y = y$
- Complete evasion $\hat y = 0$,
- or the report that maximizes transfer $\hat y = w - z^\star$


































