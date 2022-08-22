---
parent: Papers
---

# Real-time forward-looking skewness over the business cycle

[pdf link](http://www.dew-becker.org/documents/skewness.pdf)

## BibTeX
```
@techreport{dew2021real,
  title={Real-time forward-looking skewness over the business cycle},
  author={Dew-Becker, Ian},
  year={2021},
  institution={Northwestern University Working Paper. 2021. Available online: http://www~…}
}
```

## Abstract

> This paper measures option-implied skewness for individual firms and the overall
stock market between 1980 and 2020 giving a real-time measure of conditional micro
skewness. There are three key results for firm-level skewness: 1. It is significantly
procyclical, while market skewness is acyclical; 2. It leads the business cycle, and it
is strongly linked to credit spreads, suggesting one potential causal channel; 3. It is
significantly, and not mechanically, correlated with aggregate volatility, implying that
there is a common shock driving them both, which is also linked to the business cycle.



## My Notes


### Big idea:
- Measure *expectations*
    - measure skwness of expected stock returns through option prices
    - MEasure skewness from firms and S&P
- Relate skewness to business cycle indicators
    - They find procyclical at firm level, no relation at aggregate S&P level
    - Firm skewness is correlated with employment, industrial growth, capactiy, utilization, and measures of credit tightness like VIX
    - Boom: heavy right tail, bust heavy left tail.

### Data sources:
- Berkely option database 1980-1995
- Optionmetrics 1996-2019
- Agg skewnewss from CME S&P 500 1983-1994 and Optionmetrics

Options are one month in advance.
restric to just 200 largest firms by market cap.

### Skewness from Option Prices

scaled third moment:

$$skew_t(x_{t+1})\equiv   \frac{E_t [(x_{t+1}-E_t x_{t+1})^3]}{E_t [(x_{t+1}-E_t x_{t+1})^2]^{3/2}}$$

Option implied skewness, following [Kozhan, Neuberger, Schneider 2013]

$$SKEW_t = 3 \frac{\int_{0}^{\infty}\left[\frac{K-F_{t}}{K^{2}F_{t}}O_{t}(K)\right]\ dK}{\int_{0}^{\infty}\left[\frac{1}{K^{2}}O_{t}(K)\right]\ dK} $$

where $O_t(K)$ is the price of an out of the money option at strike $K$ on data $t$.

Note that estimating skewness of expectations has to deal with risk premium baked in.


#### Fatih's sidenote about stock options. 

Call options insures the downside. 
Any LLC faces a similar payoff function.
This kind of payoff structure encourages risk taking.

Elon Musk had billions in personal gains from his stock options
which let him buy millions of shares at something like 70 dollars.

Put option is the mirror image of call option.

The upfront payment is set in equilibrium so that doing both loses you money in expectation.

Options create stange nonlinearities in payoff structure.