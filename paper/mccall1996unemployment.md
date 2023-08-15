---
parent: Papers
---

# Unemployment insurance rules, joblessness, and part-time work

[https://www.jstor.org/stable/2171865](JSTOR link)

## BibTeX
```
@article{mccall1996unemployment,
  title={Unemployment insurance rules, joblessness, and part-time work},
  author={McCall, Brian P},
  journal={Econometrica: Journal of the Econometric Society},
  pages={647--682},
  year={1996},
  publisher={JSTOR}
}
```

## Abstract

> In most states, unemployment insurance recipients accepting part-time work can earn up to a specific amount (the "disregard") with no reduction in benefits. Benefits are then reduced on a dollar for dollar basis for earnings in excess of the disregard. The disregard varies both across states and within a state over time. This paper analyzes the effects of changes in the disregard on job search behavior. A continuous-time job search model is developed and under general conditions an increase in the disregard is shown to increase both the part-time and overall re-employment hazards. Data from the Current Population Survey's Displaced Worker Supplements are used to test these predictions. Estimates from a competing risks model with correlated risks and time-varying coefficients shows that increasing the disregard significantly increases the conditional probability of part-time re-employment during the first three months of joblessness.


## Notes and Excerpts

> Since its inception in the
 1930's, state laws have had provisions that allowed individuals to continue
 receiving at least partial benefits while working part-time. Most compensated
 weeks of unemployment involve payment of full benefits. The fraction of
 compensated weeks involving partial benefit payments, however, has risen by
 nearly one-third over the last decade.
 
> Originally, the most common provision for
 partial benefits was to reduce weekly benefits to the point were benefits plus
 earnings equaled 120 percent of the weekly benefit amount (see Haber and
 Murray (1966)). Now, most states allow individuals to earn up to a certain
 amount (termed the "disregard") with no reduction in benefits. Benefits are
 then reduced on a dollar for dollar basis for earnings exceeding the disre

Uses CPS Displaced Workers Supplement

Competing Risks approach.



### Model

- continuous time job search
- no wage uncertainty
- split time between leisure, full-time job search, and part-time job search
- All full-time pay $w_f$ for $h_f$ units of time. All part-time jobs pay $w_p$ for $h_p$.
- prob of job offer dependent on time spent searching
- IN a part-time job, can still spend time searching for full-time job
- remain in full-time job indefinitely
- no savings?
- consumption:
    - 0 if they don't get benefits
    - b if they do (get benefits up to some time period)
- assume individuals prefer to work full time if possible

Results of this setup:

> To summarize, the theory predicts that, under fairly general circumstances, an
 increase in the disregard will increase both the part-time and overall re-employ-
 ment hazards of UI recipients whose part-time earnings fall between y and
 b +y and will decrease their full-time re-employment hazard. Moreover, the
 theory predicts that the magnitude of these effects should be greatest at the
 beginning of the unemployment spell.


### Data

> The data used to test the model's predictions are derived from the January
 1986, 1988, 1990, and 1992 Current Population Survey's Displaced Workers Supplements

Note: this supplement is available in the first or second month of even-numbered years.
Last two are from 2022 Jan and 2020 Jan.
(So no direct overlap with FPUC period, but the questionare does ask about the previous three years.)
[See here for an example variable on IPUMS](https://cps.ipums.org/cps-action/variables/DWREAS)

What they want is info about full-time/part-time status of first post-displacement job.
They only see info about current job, but there are ways to see whether that's the first.

Methods for estimating part-time status of first job:
1. If they are still working there and reported less than 35 hours last week.
2. As above, and also they say the job is not usually full-time.

To limit missing data, only individuals displaced in prior year are included.
Plus some econometric techniques to adjust for right censoring and missing data.

Only looks at states where the benefits formula has a disregard then
reduces by one dollar for each dollar earned.
37 states included.
Final sample size of 3343.
