---
parent: Papers
---

# Wage inequality and segregation by skill

[NBER link](https://www.nber.org/papers/w5718)

[NBER pdf link](https://www.nber.org/system/files/working_papers/w5718/w5718.pdf)


## BibTeX
```
@misc{kremer1996wage,
  title={Wage inequality and segregation by skill},
  author={Kremer, Michael and Maskin, Eric},
  year={1996},
  publisher={National bureau of economic research Cambridge, Mass., USA}
}
```

## Abstract

> Evidence from the US, Britain, and France suggests that recent growth in wage inequality has been accompanied by greater segregation of high- and low-skill workers into separate firms. A model in which workers of different skill-levels are imperfect substitutes can simultaneously account for these increases in segregation and inequality either through technological change, or, more parsimoniously, through observed changes in the skill-distribution



## My Notes



- growing wage gap based on education
- less common for low and high skill workers to work in same firm
- model low and high as imperfect substitutes
- When mean and variance of skill increase, firms have to specialize in one over the other.

### Simple model of worker pairs

Consider firm which needs two tasks done, and hires workers with skills $q$ (assistant) and $q'$ (manager) to do each.

$$f(q,q')=q^c+q'^d \equiv qq'^2$$

*(f:This is the most important piece of the model. Simple idea that does a lot of work.
Problem with CES literature is that changes are made at top level without looking at micro foundations.)*

Better to assign high skill employee to manager position.

- one-good economy
- exogenous distribution of workers of different skills
- indefinite supply of firms, same production funciton
- dispersion of skill distribution decreases dispersion of skill between manager and assisstant.
    - Example: two people with skill L, two with H
    - Should the be matched by skill or should low-skill be paired with high
    - cross-matching makes sense if $$L^3 + H^3 < 2LH^2$$, which happens if $$H < (1+\sqrt{5})L/2$$
- Two competing effects:
    - Assymetry between tasks promotes cross-matching (high skilled all managers), 
    - but complementarity promotes assortive matching 

### Example with wages
- three skill levels: $L < M < H$
- population $x$ with skill $L$, $x$ with skill $H$, more than $2x$ with skill $M$.
- $H < (1+\sqrt{5})L/2$, so no self-match for $H$ or $L$ types
- Both H and L types should be matched with M types because $LH^2 + M^3 < LM^2 + MH^2$
- There will be some M types left over.
- Assume workers absorb all revenue. Then:
    - M-types in M,M firms earn $w(M) = M^3 / 2$
    - Other M types earn the same
    - L types in L,M firms earn $w(L)=LM^2-w(M)=LM^2-M^3/2$
    - H types in H,M firms earn $w(L)=MH^2-w(M)=MH^2-M^3/2$
- what happens when M skill increases?  
    $$\frac{d}{dM}w(L) = 2LM - \frac{3}{2}M^2$$  
    $$\frac{d}{dM}w(H) = H^2 - \frac{3}{2}M^2$$

- If low dispersion $L\approx H$, then a marginal increase in M causes $w(L)$ to rise and $w(H)$ to fall. Wages converge.
- If high dispersion where $$L < \frac{3}{4}M < \frac{\sqrt 6}{4}H$$, opposite effect. wages diverge.
- Intutition:
    - If L close to M, 
        - Increase in M's share decreases more slowly than total product.
        - "trickle-down" effect, where improving productivity of high-paid workers accrues benefits to low-paid
        - *I think this is the only time I've actually seen that term used by an economist.*
    - If L and M far apart
        - product of LM firms rises more slowly than MM firms, so wages of M increase, and wages of L fall.
        - At the same time, boosts wage of H for similar reasons.


### segregation index

- $J$ firms indexed by $j$
- $z_j$ workers in firm $j$
    - $Z_j$ denotes the set of these
- Denote mean skill level $\bar q$
- Define index of correlation or segregation $\rho$:

$$\rho \equiv 
\frac{\sum_j\sum_{k\in Z_j} (q_k-\bar q) \sum_{k\in Z_j} (q_k-\bar q)/z_j }
{\sum_j\sum_{k\in Z_j} (q_k-\bar q)^2}$$

- $\rho=0$ indicates all firms have same skill mix. 
- $\rho=1$ indicates complete segregation, in which workers within each firm have no variation.
- Equivalent to 
    - one minus the variance within firms divided by overall variance
    - regressing $q$ on firm dummies and looking at $R^2$
- With finite firms, $\rho > 0$ expected due to random chance. 
    - Even with random employee assignment, some firms will just get lucky.
    - If all firms had $K$ workers, randomly chosen from pool, expectation is that $\rho = 1/K$
- index adjusted for firm size

$$\rho_c = 1 - (1-\rho)\frac{N-1}{N-J}$$


### measuring segregation

- Want to measure at plant level
    - obfuscated by outsourcing
    - French data more similar to firm level
- France Wage Structure Surveys (ESS)
    - correlation of low wages and experience rose within business units
    - segregation by worker category rose.
- Similar evidence from US and BRitish worker surveys 
- segregation indices by US state
    - Kremer Trosker 1995
    - Worker-Establishment Characteristics Database (WECD)
    - states with more education variance have more segregation by education
    - Prediction doesn't work for varaince/segregation by age
    - when using log wage or predicted wage as skill indicator, prediction correct but not statistically significant.






### Generalized model

- two distributions - pre and post shift - on worker skill level $n\in\mathbb Z$
    - support bounded by $\underline n, \bar n$
- parameter $\theta=0$ representing pre-shift in distributions, $\theta=1$ post-shift
- $\mu(\theta)$ for means
    - assume equal to $n^*(\theta)$ modes
- Recall $A=2/(1+\sqrt 5)$ to be cutoff ratio that makes assortive better than cross-matching
- $$
- Some additional assumptions to ensure some modal workers will self-match
    - makes computation of equilibrium wages easier.
- Some additional assumptions to ensure there is a range of workers who will match with modal workers.
- shift in distributions reflects stylized facts
    - mean skill rises
        - n^*(1)=n^*(0)+1
    - dispersion increases
        - tails get symetrically fatter but retain relative shapes
        - $p(n;1)/p(n;0)=\alpha$ for all n outside some central range.



### Propositions

#### Prop1 (trickle down)
With tight bounds on the distribution of skill, a shift of the kind described decreases wage dispersion.
If $\underline n > \sqrt{2/3} \bar n$, then 
- $w(n;0) < w(n;1)$ for all $n < n^*(0)$
- $w(n;0) > w(n;1)$ for all $n > n^*(1)$


#### Prop2

Given large enough bounds in the story above, the wage in the low tail decreases, and wage in high tail increases

#### segregation
Increase in skill dispersion increases segragation index, provided shift in mean is small relative to shift in dispersion


---



*Tangential related thoughts*

To what extent does a private school paying teachers lower the quality of public schools.


High skill dispersion makes it difficult to sustain unions. (TODO)

TODO: read Shirwen Rosen's papers. 
Simple models are good at capturing ideas.

- KS stereotypes
- interesting that political polarization is maybe just an instance of general societal polarization
- Kremer likes his two-type dispersion models
- In Kremer model, seems between-firm segregation happens because you hire really high quality janitors.
- prefential mixing in Newman model