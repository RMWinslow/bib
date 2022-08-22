---
parent: Papers
---

# The effect of changing sexual activity on HIV prevalence

Url
: [HTML Science Direct](https://www.sciencedirect.com/science/article/pii/S002555649810010X?casa_token=kCq1PXxw2KIAAAAA:FEuM2jnl7x3s_297hMHqeO35YmpxjoCHgq1INAb9_9dY9vXe-eOqzuviyFPzMK2Qd75icMpBSw)


## BibTeX
```
@article{kremer1998effect,
  title={The effect of changing sexual activity on HIV prevalence},
  author={Kremer, Michael and Morcom, Charles},
  journal={Mathematical biosciences},
  volume={151},
  number={1},
  pages={99--122},
  year={1998},
  publisher={Elsevier}
}
```

## Abstract

> In a one-sex preferred mixing model, reductions in the rate of partner change by those with low sexual activity increase the average probability of HIV infection in the remaining pool of available partners. This increases prevalence among people with high activity, and since high activity people disproportionately influence the spread of HIV, may increase long-run prevalence in the population as a whole. Calculations using the model and survey data on sexual activity indicate that in low prevalence populations, many people have low enough activity that reductions in their activity might increase the endemic steady-state prevalence. If these results prove robust in more realistic models, they would support the case for targeting public health messages urging reduced sexual activity to high activity people.



## My Notes


From [^anderson], in a simple random mixing model, 

$$R_0 = \frac{\beta}{\delta} \left(  \mu + \frac{\sigma^2}{\mu}  \right)$$

$$R_0 = \frac{birthRate}{deathRate} \left(  meanPartnerChange + \frac{variancePartnerChange}{meanPartnerChange}  \right)$$

[^anderson]: Anderson, R. M., & May, R. M. (1992). **Infectious diseases of humans: dynamics and control.** *Oxford university press*.

With $N$ discrete groups of people, each representing $\alpha_k$ portion of the population and with $i_k$ partners per year:

$$R_0 = \frac{\beta}{\delta} \frac{\sum \alpha_k i_k^2}{\sum \alpha_k i_k}$$

deriv wrt $i_j$

$$R_{0}^{\prime}=\frac{\beta}{\delta}\cdot\frac{2\alpha_{j}i_{j}\sum\alpha_{k}i_{k}-\alpha_{j}\sum\alpha_{k}i_{k}^{2}}{\left(\sum\alpha_{k}i_{k}\right)^{2}}$$

If enough variance, and low enough $i_j$, this can actually be negative, meaning increased partners decreases $R_0$.

Compare the two formulas for $R_0$ and you get that
$$i < \frac{1}{2}  (\mu + \frac{\sigma^2}{\mu})$$


But authors say result isn't robust, so don't try applying this to actual policy.

---

Rentin[12]: two group example with random mixing, increase by low-activity group reduces steady state prevalence.

Kremer [11] analyzes externalieits using asymettric information. :( Unpublished notes.

---

## Model

- N groups of people, indexed by k. 
    - Have $i_k$ sex partners per year.
    - Make up portion $\alpha_k$ of population
    - $y_k$ portion of group $k$ has HIV
- mean sexual activity is thus 

$$\mu = \sum_k \alpha_k i_k$$

- variance is 

$$\sigma^2 = \sum_k \alpha_k (i_k - \mu)^2$$

- pool-risk (activity weighed prevalence)

$$\lambda = \sum_k \frac{\alpha_k i_k y_k}{\mu}$$

- People select partners randomly, but with preference for their own type
    - $1-\gamma$ chance of completely random seleciton
    - $\gamma$ chance of random selection from their group
- New births happen to keep relative sizes of groups consant
- probablity of transmission when infected sexes uninfected is $\beta$
- Thus an uninfected individual becomes infected at rate:
    - $$\gamma \beta i_k y_k \cdot (1-y_k)$$ from their own group
    - $$(1-\gamma) \beta i_k \gamma \cdot (1-y_k)$$ from the general population
- dynamics of illenss in group k:

$$\dot y_k = -\delta y_k + \gamma \beta i_k y_k \cdot (1-y_k) + (1-\gamma) \beta i_k \gamma \cdot (1-y_k)$$

$$\theta = \frac{\beta}{\delta}$$

From Jacquez [13], either the disease becomes endemic and stable or dies out. Threshold function (where $G < 1$ means dies out) is 

$$G(\gamma,\frac{\beta}{\delta}, \{i_k\}, \{\alpha_k\},) = \frac{\beta}{\delta} (1-\gamma) (\mu+\frac{\sigma^2}{\mu}) + \frac{\beta}{\delta} \gamma \max_k \{i_k\}$$

Thus if $G > 1$, steady state given by solving

$$Y_k = \frac{\beta}{\delta} i_k (1-Y_k)(\gamma Y_k +(1-\gamma) \Lambda)$$

where 

$$\Lambda = \sum_k \frac{\alpha_k i_k Y_k}{\mu}$$

is the steady state pool risk.


If no preference for sex with their own group, ($\gamma = 0$) simplifies to 

$$Y_k = \frac{\frac{\beta}{\delta} i_k \Lambda}{1 + \frac{\beta}{\delta} i_k \Lambda}$$

---

## effect of change in $ i_k$

If someone with partners fewer than $\Lambda$ increases activity
- In short run, lowers $\lambda$, because hookups are less risky
- In long run, may or may not lower $\Lambda$


Define $j_t$ to be cut off for activity level below which increase in activity leads to reduction in long-term prevalence.

Define $j_e$ to be cut off so that increase in activity decreases steady-state pool-risk. (POsitive externailty creators). Always positive.

Some technical lemmas.

If group has activity less than $j_e$ partners per year, increase in activity will reduce $\Lambda$ at the margins where

$$j_e = \frac{\delta}{\beta(\gamma+(1-\gamma)\Lambda)^2}\left( \gamma-(1-\gamma)\Lambda + \sqrt{\frac{1-\gamma}{1-\Lambda}} (\Lambda - (1-\Lambda)\gamma) \right)$$

and 

$$0 < j_e < \frac{\delta}{\beta(1-\Lambda)}$$


More technical proofs

### special case: random mizing

$$j_e = \frac{\delta}{\beta(\Lambda)^2}\left( -\Lambda + \sqrt{\frac{1}{1-\Lambda}} (\Lambda) \right)$$

$$j_e = \frac{\delta}{\beta\Lambda}\left(\sqrt{\frac{1}{1-\Lambda}} - 1 \right)$$

$$Y_e = 1-\sqrt{1-\Lambda}$$

Then some simulations and implications


## conclusions

perferes mixing single sex model

Best matches situtation where sex seekers always have a partner. If dating low activity people takes time then reduction by low activity would reduce activity from high activity groups and thus change implications.

---

Further reading

Kremer [2]: Integrating behavioral choice into epidemiological models of AIDS

Whitaker Rentin[12]: A theoretical model of interpreting the recenetly reported increas in homosexual gonorrhea
 
Kremer [11]: AIDS and Imperfect Signals of Risk :( Unpublished notes.

Jacquez Simon Koopman Sattenspiel  Perry[13]: modelling analysing HIV transmission: the effect of contact patterns.

