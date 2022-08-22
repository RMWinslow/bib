---
parent: Papers
---

# Individual variation in susceptibility or exposure to SARS-CoV-2 lowers the herd immunity threshold

[html link](https://www.sciencedirect.com/science/article/pii/S0022519322000613)

## BibTeX
```
@article{gomes2022individual,
  title={Individual variation in susceptibility or exposure to SARS-CoV-2 lowers the herd immunity threshold},
  author={Gomes, M Gabriela M and Ferreira, Marcelo U and Corder, Rodrigo M and King, Jessica G and Souto-Maior, Caetano and Penha-Gon{\c{c}}alves, Carlos and Gon{\c{c}}alves, Guilherme and Chikina, Maria and Pegden, Wesley and Aguas, Ricardo},
  journal={Journal of theoretical biology},
  volume={540},
  pages={111063},
  year={2022},
  publisher={Elsevier}
}
```

## Abstract

> Individual variation in susceptibility and exposure is subject to selection by natural infection, accelerating the acquisition of immunity, and reducing herd immunity thresholds and epidemic final sizes. This is a manifestation of a wider population phenomenon known as “frailty variation”. Despite theoretical understanding, public health policies continue to be guided by mathematical models that leave out considerable variation and as a result inflate projected disease burdens and overestimate the impact of interventions. Here we focus on trajectories of the coronavirus disease (COVID-19) pandemic in England and Scotland until November 2021. We fit models to series of daily deaths and infer relevant epidemiological parameters, including coefficients of variation and effects of non-pharmaceutical interventions which we find in agreement with independent empirical estimates based on contact surveys. Our estimates are robust to whether the analysed data series encompass one or two pandemic waves and enable projections compatible with subsequent dynamics. We conclude that vaccination programmes may have contributed modestly to the acquisition of herd immunity in populations with high levels of pre-existing naturally acquired immunity, while being crucial to protect vulnerable individuals from severe outcomes as the virus becomes endemic.

## My Notes


> **One Sentence Summary:** Models that curtail individual variation in susceptibility or exposure
to infection overestimate epidemic sizes and herd immunity thresholds. 
---



> Although estimates vary, simple calculations suggest that herd immunity to SARS-
CoV-2 requires 60-70% of the population to be immune. By fitting epidemiological models that 
allow for heterogeneity to SARS-CoV-2 outbreaks across the globe, we show that variation in
susceptibility or exposure to infection reduces these estimates


Basic idea is that the people most likely to get sick are then most likely to become immune from that sickness.
Thus the natural spread of disease, unlike random vaccination, has a built in selection mechanism to target the individuals who need it most (in the societal sense of "need")

> We integrate
continuous distributions of susceptibility or connectivity in otherwise basic epidemic models for
COVID-19 and show that as the coefficient of variation (CV) increases from 0 to 4, the herd
immunity threshold declines from over 60% (4, 5) to less than 10%. 

coefficient of variation is the ratio of standard deviation $\sigma$ to absolute mean $| \mu |$

### continuous transmission in heterogenous populations

susceptibility parameter $x$

$\dot{S}(x)=-\lambda x S(x)$

$\dot{E}(x)=\lambda x S(x)-\delta E(x)$

$\dot{I}(x)=\delta E(x)-\gamma I(x)$

$\lambda$ represents the "average force of infection" and $\lambda = \frac{\beta}{N} \int \rho E(x) + I(x) \, dx$

$$R_0 = \langle x \rangle \frac{\beta}{N} (\frac{\rho}{\delta} + \frac{1}{\gamma})$$

$\rho$ is "a factor measuring the infectivity of individuals in compartment E in relation to those
in I" and $\langle x \rangle$ is mean susceptibility at time 0.

Before epidemic, susceptibility has pdf $q(x)$ with mean $1$ and coefficient of variation $CV=\langle (x-1)^2 \rangle$

$R_{eff}=R_t=$ susceptibility at time $t$ multplied by $R_0$

> Countries where suppression of the initial outbreak was more successful, such as Austria, have
acquired less immunity and therefore the potential for future transmission in the respective
populations remains naturally larger. However, also in these situations, expectations for the 5
potential of subsequent waves is much reduced by variation in susceptibility to infection.

> Susceptibility factors were implemented as gamma
distributions... 
Consensus parameter values
$\delta=1/4$ per day...
$\gamma=1/4$ per day...
$\rho=0.5$

> In a directly transmitted infectious disease, such as COVID-19, variation in exposure to infection
is primarily governed by patterns of connectivity among individuals. We incorporate this in the
system (Equation 1) by adding variation in infectivity and assuming a positive correlation
between susceptibility and infectivity.
Formally this corresponds to modifying the force of
infection ... and basic reproductive number as  
> 
> $$\lambda = \frac{\beta}{N} \frac{\int x [\rho E(x) + I(x)] \, dx}{\int x q(x) \, dx}$$
> 
> $$R_0 = \frac{\langle x^2 \rangle}{\langle x \rangle} \frac{\beta}{N} (\frac{\rho}{\delta} + \frac{1}{\gamma})$$
> 
> where $\langle x^2 \rangle$ and $\langle x \rangle$ are second and first moments of distribution $q(x)$ prior to the epidemic
