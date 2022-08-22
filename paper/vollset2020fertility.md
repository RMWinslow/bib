---
parent: Papers
---

# Fertility, mortality, migration, and population scenarios for 195 countries and territories from 2017 to 2100: a forecasting analysis for the Global Burden of Disease Study

[Lancet html link](https://www.thelancet.com/article/S0140-6736(20)30677-2/fulltext)

[pdf link](https://www.thelancet.com/action/showPdf?pii=S0140-6736%2820%2930677-2)

## BibTeX
```
@article{vollset2020fertility,
  title={Fertility, mortality, migration, and population scenarios for 195 countries and territories from 2017 to 2100: a forecasting analysis for the Global Burden of Disease Study},
  author={Vollset, Stein Emil and Goren, Emily and Yuan, Chun-Wei and Cao, Jackie and Smith, Amanda E and Hsiao, Thomas and Bisignano, Catherine and Azhar, Gulrez S and Castro, Emma and Chalek, Julian and others},
  journal={The Lancet},
  volume={396},
  number={10258},
  pages={1285--1306},
  year={2020},
  publisher={Elsevier}
}
```

## Abstract

> Background
> Understanding potential patterns in future population levels is crucial for anticipating and planning for changing age structures, resource and health-care needs, and environmental and economic landscapes. Future fertility patterns are a key input to estimation of future population size, but they are surrounded by substantial uncertainty and diverging methodologies of estimation and forecasting, leading to important differences in global population projections. Changing population size and age structure might have profound economic, social, and geopolitical impacts in many countries. In this study, we developed novel methods for forecasting mortality, fertility, migration, and population. We also assessed potential economic and geopolitical effects of future demographic shifts.
> 
> Methods
> We modelled future population in reference and alternative scenarios as a function of fertility, migration, and mortality rates. We developed statistical models for completed cohort fertility at age 50 years (CCF50). Completed cohort fertility is much more stable over time than the period measure of the total fertility rate (TFR). We modelled CCF50 as a time-series random walk function of educational attainment and contraceptive met need. Age-specific fertility rates were modelled as a function of CCF50 and covariates. We modelled age-specific mortality to 2100 using underlying mortality, a risk factor scalar, and an autoregressive integrated moving average (ARIMA) model. Net migration was modelled as a function of the Socio-demographic Index, crude population growth rate, and deaths from war and natural disasters; and use of an ARIMA model. The model framework was used to develop a reference scenario and alternative scenarios based on the pace of change in educational attainment and contraceptive met need. We estimated the size of gross domestic product for each country and territory in the reference scenario. Forecast uncertainty intervals (UIs) incorporated uncertainty propagated from past data inputs, model estimation, and forecast data distributions.
> 
> Findings
>The global TFR in the reference scenario was forecasted to be 1·66 (95% UI 1·33–2·08) in 2100. In the reference scenario, the global population was projected to peak in 2064 at 9·73 billion (8·84–10·9) people and decline to 8·79 billion (6·83–11·8) in 2100. The reference projections for the five largest countries in 2100 were India (1·09 billion [0·72–1·71], Nigeria (791 million [594–1056]), China (732 million [456–1499]), the USA (336 million [248–456]), and Pakistan (248 million [151–427]). Findings also suggest a shifting age structure in many parts of the world, with 2·37 billion (1·91–2·87) individuals older than 65 years and 1·70 billion (1·11–2·81) individuals younger than 20 years, forecasted globally in 2100. By 2050, 151 countries were forecasted to have a TFR lower than the replacement level (TFR <2·1), and 183 were forecasted to have a TFR lower than replacement by 2100. 23 countries in the reference scenario, including Japan, Thailand, and Spain, were forecasted to have population declines greater than 50% from 2017 to 2100; China's population was forecasted to decline by 48·0% (−6·1 to 68·4). China was forecasted to become the largest economy by 2035 but in the reference scenario, the USA was forecasted to once again become the largest economy in 2098. Our alternative scenarios suggest that meeting the Sustainable Development Goals targets for education and contraceptive met need would result in a global population of 6·29 billion (4·82–8·73) in 2100 and a population of 6·88 billion (5·27–9·51) when assuming 99th percentile rates of change in these drivers.

> Interpretation
> Our findings suggest that continued trends in female educational attainment and access to contraception will hasten declines in fertility and slow population growth. A sustained TFR lower than the replacement level in many countries, including China and India, would have economic, social, environmental, and geopolitical consequences. Policy options to adapt to continued low fertility, while sustaining and enhancing female reproductive health, will be crucial in the years to come.


## My Notes


### Main goals

Projecting Global population is hard and important. They try to forcast mortality, fertility, migration, and population. Also, assess impacts of demographic shift.

---

[completed cohort fertility](https://demography.subwiki.org/wiki/Completed_cohort_fertility) at age 50 years (CCF50)
: Average number of children a woman has had by the time they turn 50.

Age-specific fertility rate
: average number of live births that females of a given age have on average in a year.

[total fertility rate](https://demography.subwiki.org/wiki/Total_fertility_rate) (TFR)
: Add up the Age-specific fertility rates, equally weighting each age cohort

general fertility rate
: Add up the Age-specific fertility rates, weighted by population size

Study says CCF50 is more stable over time.
Mythought: can you see chinese zodiac superstition reflected in TFR fluctuations (more kids born in pig year)?

---

- `We developed statistical models for completed cohort fertility at age 50 years (CCF50) and age-specific fertility as a function of educational attainment and contraceptive met need, a measure of the proportion of women in a population of reproductive age whose need for contraception has been met with modern contraceptive methods.`
- `Age-specific fertility rates were modelled as a function of CCF50 and covariates. We modelled age-specific mortality to 2100 using underlying mortality, a risk factor scalar, and an autoregressive integrated moving average (ARIMA) model.`
- `Net migration was modelled as a function of the Socio-demographic Index, crude population growth rate, and deaths from war and natural disasters; and use of an ARIMA model. `

---

Predictions:
- TFR 1.66 in 2100
- Peak population 10 billion in 2064
- decline to 9 billion in 2100
- Specific countries in 2100:
    - India 1.1b
    - Nigreia .79b
    - china .73b
    - USA .34b
    - pakistan .25b
- china becomes biggest economy in 2035, then US catches back up in 2098
- lots of old people
- Turbo charge education and contraceptives and you get more like 7 billion people in 2100



They make use of detail elements. Neat.

---

> The main provider of population forecasts for the world since the 1950s is the Population Division of the Department of Economic and Social Affairs of the UN Secretariat (UNPD), which now produces regular forecasts for each country in 5-year calendar intervals such as 2095–2100.1

> The UNPD's latest forecasts used time alone as the determinant of future trajectories for fertility and mortality; they are sophisticated curve-fitting exercises, which do not allow for alternative scenarios linked to policies or other drivers of fertility and mortality.6 

Austrian Wittgenstein Centre and collaborators
> Their scenarios are a blend of statistical models fit to past data and expert judgment on likely trends in fertility, particularly regarding rising education levels in many parts of the world.7,  12 The Wittgenstein Centre forecasts have been the most widely used forecasts in climate modelling,13 although neither the climate models nor the Wittgenstein forecasts explicitly model the interrelationship between climate change and population.

Witt.. assumes countries converge to 1.75 TFR. But  Thailand, Greece, South Korea, and Canada all have low fertility and don't seem to increase

---

### Mortality

Uses mortality model from [this paper](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(18)31694-5/fulltext), and extends it to 2100.


### Fertility

Oh cool, Lancet uses MathJax too

They  modelled CCF50 for females in birth cohort c in location l, denoted by CCFl,c using the regression model given by:

$$
CCF_{l,c} = \beta_0 + \beta_{mn} mn_{l,c} + ns(edu_{l,c}) + \eta_{l,c}
$$

mn is contraceptive met need, $ns(edu_{l,c})$ is a natrual cubic spline? on average demale educational attainment, and the $\eta$ is redisual modelled by random walk. mn and edu measured at age 25 for each cohort.

### Migration 

Model in methods appendix, section 7

---

> Countries such as China or India have a lower effective fertility rate than the TFR would suggest because the sex ratio at birth is skewed toward boys (additional results in appendix 2, section 5). 


### Economic Conswquences

- working age population (20-64) plotted in reference scenario
    - if global labour force participation by age and sex remains the same from 2017 to 2100, the ratio of the non-working adult population to the working population might reach 1·16 globally, up from 0·80 in 2017. 


>  In our model, in a population where all females have 16 years of education and 95% of females have access to contraception, the global TFR was projected to converge to 1·41 (1·35–1·47). The difference between a convergent TFR of 1·75 or 1·41 is profound in terms of long-term consequences on global population size and age structure in this century and beyond. Modelling fertility rates lower than replacement level, particularly when modelling the TFR directly, is challenging given the widely divergent realities of countries such as Singapore, Taiwan (province of China), or Japan compared with those in northern Europe. Responding to sustained low fertility is likely to become an overriding policy concern in many nations given the economic, social, environmental, and geopolitical consequences of low birth rates.



> The forecasts in the paper by Chang and colleagues of productivity per working-aged adult that we have used assume that past trends in productivity will continue.35 Having fewer individuals between the ages of 15 and 64 years might, however, have larger effects on GDP growth than what we have captured here. For example, having fewer individuals in these age groups might reduce innovation in economies, and fewer workers in general might reduce domestic markets for consumer goods, because many retirees are less likely to purchase consumer durables than middle aged and young adults.17

> In 2100, if labour force participation by age and sex does not change, the ratio of the non-working adult population to the working population might reach 1·16 globally, up from 0·80 in 2017. This ratio implies that, at the global level, each person working would have to support, through taxation and intra-family income transfers, 1·16 non-working individuals aged 15 years or older (the working age population is defined by the International Labour Organization as those aged 15 years or older).41 Moreover, the number of countries with a dependency ratio higher than 1 is expected to increase from 59 in 2017 to 145 in 2100. Taxation rates required to sustain national health insurance and social security programmes might be so large as to further reduce economic growth and investment. Insecurity from the risk that these programmes could fail might generate considerable political stress in societies with this demographic contraction. 


> As nations come to recognise the challenges of fertility rates lower than the replacement level and the potential for demographic contraction, they have four options to pursue: attempt to increase the fertility rate by creating a supportive environment for females to have children and pursue their careers, restrict access to reproductive health services, increase labour force participation especially at older ages, and promote immigration. It is worth considering how each of these options might play out in different countries.


> As nations come to recognise the challenges of fertility rates lower than the replacement level and the potential for demographic contraction, they have four options to pursue: attempt to increase the fertility rate by creating a supportive environment for females to have children and pursue their careers, restrict access to reproductive health services, increase labour force participation especially at older ages, and promote immigration. It is worth considering how each of these options might play out in different countries.


Main limitation is sparcity of historical data.





