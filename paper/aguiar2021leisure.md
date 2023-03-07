---
parent: Papers
---

# Leisure luxuries and the labor supply of young men

[NBER link](https://www.nber.org/papers/w23552)

## BibTeX
```
@article{aguiar2021leisure,
  title={Leisure luxuries and the labor supply of young men},
  author={Aguiar, Mark and Bils, Mark and Charles, Kerwin Kofi and Hurst, Erik},
  journal={Journal of Political Economy},
  volume={129},
  number={2},
  pages={337--382},
  year={2021},
  publisher={The University of Chicago Press Chicago, IL}
}
```

## Abstract

> Younger men, ages 21 to 30, exhibited a larger decline in work hours over the last fifteen years than older men or women. Since 2004, time-use data show that younger men distinctly shifted their leisure to video gaming and other recreational computer activities. We propose a framework to answer whether improved leisure technology played a role in reducing younger men's labor supply. The starting point is a leisure demand system that parallels that often estimated for consumption expenditures. We show that total leisure demand is especially sensitive to innovations in leisure luxuries, that is, activities that display a disproportionate response to changes in total leisure time. We estimate that gaming/recreational computer use is distinctly a leisure luxury for younger men. Moreover, we calculate that innovations to gaming/recreational computing since 2004 explain on the order of half the increase in leisure for younger men, and predict a decline in market hours of 1.5 to 3.0 percent, which is 38 and 79 percent of the differential decline relative to older men.



## Notes and Excerpts

> This is clear from the ATUS time diaries, as younger men’s time spent on recreational computing increased more than
their increase in total leisure time (including computers). That is, the
time devoted to all other leisure activities actually declined, even though
total leisure time increased. This would be consistent with stable leisure
Engel curves only if the sum of all other leisure activities is inferior (with
respect to total leisure time). Not only is that counterintuitive, it is also
inconsistent with the estimates presented below that all broad subcategories of leisure are normal activities, for which time spent on that activity
increases with total leisure.

> ind that, for a fixed market wage and marginal utility of consumption, improved computer leisure technology increased younger men’s
marginal value of time by 2.5%. By contrast, we find that better computer
technology caused no reduction in labor supply for older men and a
much smaller negative effect for women, results compatible with our
finding that the activity is not a strong leisure luxury for either group. 

They emphasize that video games aren't the only factor leading to less young male unemployment.
During the great recessions for example, leisure technology can at most explain a teeny tiny bit of the dip.

> The ATUS shows a corresponding drop in market hours for younger men of nearly 4 hours per
week, or about 10%, while computer leisure increased by a full hour.

> Our working paper, Aguiar et al. (2017), also finds that budgets for younger men have
become increasing detached from their labor earnings, especially via a much higher tendency to live with older relatives.

> Our focus on time allocation owes a natural debt to the seminal papers of Mincer (1962) and Becker (1965). They emphasize that labor supply is influenced by how time is allocated outside of market work—for
instance, female labor force participation being affected by improved
household technology. 

> We divide activities into six broad categories: market work, job search,
home production, child care, education, and leisure.12 Our classification
of time-use activities follows closely the classification used in Aguiar and
Hurst (2007b), Aguiar, Hurst, and Karabarbounis (2013), and Boppart
and Ngai (2017). Job search includes sending out resumes, job interviewing, and researching jobs. Home production includes doing household
chores or maintenance, preparing meals, shopping, and caring for other
adults. We separate child care from home production. Education refers
to time spent on one’s own education, such as attending courses or doing
homework. Leisure consists of watching television and movies, recreational computing and video games, reading, playing sports, hobbies,
and so on. 
We
treat a portion of eating, sleeping, and personal care (ESP) as leisure, as
these categories have both a biological and a leisure component. To isolate
the leisure component of ESP, we exclude 7 hours per day from total ESP
time to account for the fact that a certain amount of ESP is needed for survival.13 Given this, each individual’s time use across the six categories sums
to a maximum of 17 hours per day, or 119 hours per week.

Though their six categories add up to around 117.something. With a bit of wiggle across demographics.

Also worth noting:
They compare 2004-2007 to 2014-2017.
In other word they exclude the Great Recession in their headline statistics.

> ESP also increased for young men during this time period, by 1.7 hours
per week. The marked increase in sleeping time is a feature of the ATUS
data across all demographic groups during this time period (e.g., younger
women, older men, and older women). This may be a real phenomenon
or is possibly an artifact of how sleep time is measured within the ATUS. 18  
> 18: The sleep time-use category includes sleeplessness and trying to fall to sleep. So watching TV while trying to fall to sleep may be classified as either sleeping or TV watching.

They also note the ATUS increase in sleep time is not found in other data sets (like National Health and Nutrition Examination Survey).

TODO: ATUS separately tracks sleeping and sleeplessness. Does the increase persist if the latter is excluded? 
(ATUS code 010102)

---

> We estimate that technology growth for recreational computing increased the reservation wages of younger men by 2.5%, holding their marginal utility of consumption fixed. By contrast, we estimate that these innovations increased younger women’s reservation wages by 1.0% and had
little effect for older men and women. 







### Model bits

utility is of consumption and some combination of leisure

$$U(c,v(\mathbf h;\bm\theta, \bm{ξ}))$$

$$v(\mathbf h_k;\bm\theta, \bm{ξ}_k) = 
\sum_i \frac{(\theta_i \xi_{ik} h_{ik})^{1-(1/\eta_i)}}{1-(1/\eta_i)}$$

where $i$ indexes activities, $k$ indexes individuals, $h,\theta,\xi$, are respectively
time spent on activities, leisure technology shifters, and idiosyncratic preferences.
($\theta$ are common and change over time; $\xi$ are individual and are drawn from steady distribution)
$eta$ governs diminishing returns associated with time spent on a specific activity.

Note loose additive separability and time separability.

Normalize time to 1 and let $\lambda$ denote marginal value of wealth.

Then problem is 

$$\max_{c,\bm h, N} \left\{   U(c,v(\bm{h;\theta,\xi})) + \lambda (wN-c)    \right\}$$

subject to 

$$N + \sum_i h_i \leq 1, \\
N\in[0,1]$$

FOCs are $\frac{\partial U}{\partial c} = \lambda$
and $\frac{\partial U}{\partial v}\frac{\partial v}{\partial hi} = w$ for all $i$.

Define $\hat w \equiv \frac{w}{\partial U / \partial v}$
as the normalized price of time.

Consider subproblem of allocating time across leisure activities:

$$v(H; \bm{\theta, \xi}) \equiv \max_{\bm h} v(\bm{h; \theta, \xi}), \text{ s.t.: } \sum_i h_i \leq H$$

Combine FOC, form of $v$, and definition of $\hat w$ to get

$$\hat w = (\theta_i \xi_i h_i)^{-1/\eta_i} \cdot \theta_i \xi_i\\
h_i = (\theta_i \xi_i)^{\eta_i-1} \hat w^{-\eta_i}$$

($v_H\equiv \frac{\partial v}{\partial H} =\hat w$)

Sum to get $H=\sum_i (\theta_i \xi_i)^{\eta_i-1} \hat w^{-\eta_i}$
(strictly monotonic mapping between $H$ and $\hat w$).
Derivative wrt $H$ to get 
$1=\sum_i \left[(\theta_i \xi_i)^{\eta_i-1} \hat w^{-\eta_i} \cdot -\eta_i \frac{1}{\hat w} \frac{\partial\hat w}{\partial H}  \right]$.
Therefore

$$\frac{\partial\hat w}{\partial H} =
\frac{-\hat w}{\sum_i \left[(\theta_i \xi_i)^{\eta_i-1} \hat w^{-\eta_i} \cdot \eta_i  \right]} = 
\frac{-\hat w}{\sum_i h_i \cdot \eta_i}
$$

<!--
Or take derivative \hat w wrt to H and apply the inverse function theorem.
-->

And so the elasticity of $\hat w$ wrt to $H$ is the time-share-weighted average of individual elasticities?

$$\frac{\partial\ln\hat w}{\partial\ln H} = 
\frac{\partial\hat w}{\partial H}\frac{H}{\hat w} = 
\frac{-1}{\sum_i \frac{h_i}{H} \eta_i}$$


<!--
NOTE: I'm actually having trouble deriving equation (8) from the paper. Might be a typo on their part.

Similarly, holding $H$ fixed, 
Take derivative wrt \theta_{j}:

$$0=\left(\eta_{j}-1\right)\xi_j(\theta_{j}\xi_{j})^{\eta_{j}-2}\hat{w}^{-\eta_{j}}+\sum_{i}\left[(\theta_{i}\xi_{i})^{\eta_{i}-1}\hat{w}^{-\eta_{i}}\cdot(-\eta_{i}\frac{1}{\hat{w}}\frac{\partial\hat{w}}{\partial\theta_{j}})\right]$$

$$\left(\eta_{j}-1\right)\xi_j(\theta_{j}\xi_{j})^{\eta_{j}-2}\hat{w}^{-\eta_{j}}=\sum_{i}\left[h_{i}\eta_{i}\cdot(\frac{1}{\hat{w}})\right]\cdot\frac{\partial\hat{w}}{\partial\theta_{j}}$$

$$\frac{\partial\hat{w}}{\partial\theta_{j}}=\frac{H}{H}\frac{\left(\eta_{j}-1\right)\xi_j(\theta_{j}\xi_{j})^{\eta_{j}-2}\hat{w}^{-\eta_{j}}\hat{w}}{\sum_{i}\left[h_{i}\eta_{i}\right]}$$

$$\frac{\partial\hat{w}}{\partial\theta_{j}}=\frac{\left(\eta_{j}-1\right)\xi_j(\theta_{j}\xi_{j})^{-1}\frac{h_{j}}{H}\hat{w}}{\sum_{i}\left[\frac{h_{i}}{H}\eta_{i}\right]}
=\frac{\left(\eta_{j}-1\right)\frac{h_{j}}{H}}{\sum_{i}\left[\frac{h_{i}}{H}\eta_{i}\right]}\frac{\hat w}{\theta_i}$$

And then the elasticity is straightforwardly 

$$\frac{\partial\ln\hat w}{\partial\ln\theta_j}= 
\frac{\left(\eta_{j}-1\right)\frac{h_{j}}{H}}{\sum_{i}\left[\frac{h_{i}}{H}\eta_{i}\right]}$$
-->

Combine FOC with the above to get a "leisure Engel curve"

$$\frac{\partial h_i}{\partial H} = \frac{\partial h_i}{\partial \hat w}\frac{\partial \hat w}{\partial H}=
\frac{\eta_i h_i}{\sum_i \eta_i h_i}$$

$$\frac{\partial\ln h_i}{\partial\ln H} = \frac{\partial h_i}{\partial H}\frac{H}{h_i}=
\frac{\eta_i}{\sum_i \frac{h_i}{H} \eta_i}$$

The last equation is elasticity of a leisure activity wrt total leisure time.
Activities with higher $\eta_i$ are "leisure luxuries".

> The crucial assumption is that the shadow
price of time is the same when choosing between alternative leisure activities

Another important equation for their empirical work:
Let $j$ be a "reference activity" whose technology does not change,
and let $\xi_j=\xi_i$. Then

$$\frac{\ln h_i}{\eta_i} - \frac{\ln h_j}{\eta_j} = \frac{\eta_i - 1}{\eta_i}\ln \theta_i - \frac{\eta_j - 1}{\eta_j}\ln \theta_j$$

$$\frac{\Delta\ln h_i}{\eta_i} - \frac{\Delta\ln h_j}{\eta_j} = \frac{\eta_i - 1}{\eta_i}\ln \Delta\theta_i - \frac{\eta_j - 1}{\eta_j}\ln \Delta\theta_j = \frac{\eta_i - 1}{\eta_i}\ln \Delta\theta_i$$

via the assumption that $\theta_j$ is unchanging.
Rearrange to get

$$\Delta\ln\theta_i = \frac{\Delta\ln h_i - \frac{\eta_i}{\eta_j}\Delta\ln h_j}{\eta_i-1}$$

----

empirical specification sarting on page 362

> Deaton and Muellbauer’s (1980) Almost Ideal Demand System
(AIDS).

TODO: Read more about Almost Ideal Demand System...



