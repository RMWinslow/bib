---
parent: Papers
---

# Reassessing the ins and outs of unemployment

[NBER link](https://www.nber.org/papers/w13421)

[ScienceDirect link](https://www.sciencedirect.com/science/article/pii/S1094202512000063)


## BibTeX
```
@article{shimer2012reassessing,
  title={Reassessing the ins and outs of unemployment},
  author={Shimer, Robert},
  journal={Review of Economic Dynamics},
  volume={15},
  number={2},
  pages={127--148},
  year={2012},
  publisher={Elsevier}
}
```

## Abstract

> This paper uses readily accessible aggregate time series to measure the probability that an employed worker becomes unemployed and the probability that an unemployed worker finds a job, the ins and outs of unemployment. Since 1948, the job finding probability has accounted for three-quarters of the fluctuations in the unemployment rate in the United States and the employment exit probability for one-quarter. Fluctuations in the employment exit probability are quantitatively irrelevant during the last two decades. Using the underlying microeconomic data, the paper shows that these results are not due to compositional changes in the pool of searching workers, nor are they due to movements of workers in and out of the labor force. These results contradict the conventional wisdom that has guided the development of macroeconomic models of the labor market since 1990.




## Notes and Excerpts

Assumptions:
- all workers ex ante identical
  - in any particular period, everyone has same job finding and exit probability
- Only transition between employment and unemployment

> Given these assumptions, I show that the
probability that an unemployed worker finds a job during a period is a simple function of the number of unemployed
workers at the start of the period, the number of unemployed workers at the end of the period, and the number of unemployed workers at the end of the period who were employed at some point during the period.


> assume that all unemployed workers find a job—become employed—with probability Ft and all employed workers lose a job—become unemployed—with probability Xt during period t


Let $u_t$ and $u_{t+1}$ be unemployed workers, 
and $u_{t+1}^s$ be short term unemployed workers, 
"those who are unemployed at date t + 1 but held a job at some point during period t." 
Then job finding rate is 

$$
F_t = 1 - \frac{u_{t+1}-u^s_{t+1}}{u_t}
$$

To get $u$ from CPS is standard.

To get $u^s$


>  The survey also asks unemployed workers how long
they have been unemployed and the BLS tabulates the number of unemployed workers with
zero to four weeks duration. I use this as my measure of short term unemployment from
January 1948 to December 1993. Unfortunately, the redesign of the CPS instrument in 1994
introduced a significant discontinuity in the short term unemployment series (Abraham and
Shimer, 2001); Appendix A describes how I measure the short-term unemployment rate after 1994.


> Until 1994, unemployed workers in all eight rotation groups were asked how long they
had been unemployed. But since then, the CPS has not asked a worker who is unemployed
in consecutive months the duration of her unemployment spell in the second month. Instead,
the BLS calculates unemployment duration in the second month as the sum of unemployment
duration in the first month plus the intervening number of weeks. Thus prior to 1994, the CPS
measure of short term unemployment should capture the total number of unemployed workers
who were employed at any point during the preceding month, while after the redesign, short
term unemployment only captures workers who transition from employment at one survey
date to unemployment at the next survey date.
> ...
> note that one would
expect that the redesign of the CPS instrument would not affect measured unemployment
duration in rotation groups 1 and 5, the ‘incoming rotation groups’, since these workers
are always asked their unemployment duration, but would reduce the measured short term
unemployment rate in the remaining six rotation groups.
> ...
> In this paper I use short term unemployment from the full sample from 1948 to 1993
and then use only the incoming rotation groups in the later period.
> [Details follow.]


