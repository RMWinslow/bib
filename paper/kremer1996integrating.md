---
parent: Papers
---

# Integrating behavioral choice into epidemiological models of AIDS

[QJE link](https://academic.oup.com/qje/article-abstract/111/2/549/1938412#no-access-message)

[NBER working paper link](https://www.nber.org/papers/w5428)

## BibTeX
```
@article{kremer1996integrating,
  title={Integrating behavioral choice into epidemiological models of AIDS},
  author={Kremer, Michael},
  journal={The Quarterly Journal of Economics},
  volume={111},
  number={2},
  pages={549--573},
  year={1996},
  publisher={MIT Press}
}
```

## Abstract

> Increased HIV risk creates incentives for people with low sexual activity to reduce their activity, but may make high-activity people fatalistic, leading them to reduce their activity only slightly, or actually increase it. If high-activity people reduce their activity by a smaller proportion than low-activity people, the composition of the pool of available partners will worsen, creating positive feedbacks, and possibly multiple steady states. Early public health efforts may allow societies to reach more favorable steady states.



## My Notes


- Behavior of small grop of active people is critical to spread of disease
    - Hethcote Yorke 1984, Over Piot 1993
- Most models treat behavior independent of prevalence.
- Some changes in response to prevalence
    - McKusick 1985, Ahituv Hotz Philison 1993
- Anecdotal evidence of fatalism among high-prevalence populations
    - Barneet Blaikie 1992
- If increase in prevalence has bigger effect on low-risk individuals, can lead to situation wher high-risk actually increase their activity
- can lead to multiple equilibria
- anti-AIDS policies can be counteracted by behavioral response
    - Philipson POsner 1993, Hadeler Castillo-Chavez 1994
- If behavior is function of **lagged** prevalence, will generate cycles in prevalence
    - Avery Heymann Zeckhauser 1994, Brauer Castillo-Chavez, Velasco-Hernandex 1994
- This paper has behavior change in reponse to pool of availible partners, which can lead to multiple steady-states and positive feebacks.

---

### Homogenous population

This is for an SI model. No R.

- die at Poisson hazard rate $\delta$
- transmission rate $\beta$
- rate of partner change $i$, function of $Y$
- prevalence $Y$

$$\dot Y = i(Y)\beta Y\cdot(1-Y)-\delta Y$$

$$R_0 = i(0) {\beta \over \delta} $$

$$Y_{ss} = \frac{1-\delta}{i(Y_{ss})\beta}$$

- Individuals choose $i$ to maximize $u(i)-p(i)$
    - $u(i)$ has diminishing marginal utility from additional partners. $u'' < 0$
    - $p(i)$ is probability of becoming infected.
- some maximium rate of partner change $i_{max}$

#### For low activity people:

Unique fixed point for $Y_{ss}$

Elasticity of $i$ in response to $\beta$ determines whether reductions in transmission rate increase (when elasticity greater than one) or decrease (less than) steady state prevalence 

In the high elasticity case, partially effective vaccine could reduce welfare.
Individual who gets vaccinated is better off, but has more partners, increasing risk pool.
$\beta Y$ won't increase, because that's the prob of infection from an additional partner. 

Is it?

Oh. Because probability of infection can be approximated as linear in the rate of partner change.

#### High activity people:

More generally, probability that someone will be infected before dying of other causes:

$$p(i) = \frac{i\beta Y}{\delta + i \beta Y}$$

$$\frac{\partial p}{\partial i} = \frac{\delta \beta Y}{(\delta + i \beta Y)^2}$$

Effect of increase in prevalence on marginal risk of infection from an additional partner:

$$\frac{\partial^2 p}{\partial i \partial Y} = \frac{\delta \beta [\delta - i \beta Y]}{\delta+i\beta Y}$$

If $i > \frac{\delta}{\beta Y}$,
which happens when $i \beta Y > \delta$,
then increases in prevalence will reduce marginal risk of infection from an additional partner.
This happens when there is at least a 50% chance of being infected $p(i)$.
If you change it so lifetime is fixed length, then cutoff if $1-\frac{1}{e}\approx 0.63$.

Why? Increase in prevalence shifts prob mass of getting sick towards early partners. Increases marginal risk of first few, and decreases marginal risk of later partners.

Mutiple equilibriums possible.
Kremer notes unlikely because no national population with ss prevalence high enough.
But what about in an acute outbreak, eh?



### Low prevalence, heterogenous population

What if people have different i(Y) functions?

- portion $a_H$ of population is high activity
    - has $i_H$ partners
    - prevalence $Y_H$
- portion $a_L$ of population is low activity
    - has $i_L$ partners
    - prevalence $Y_L$
- with random mizing, chance that random partner is infected (activity-weighted prevalence) is

$$W = \frac{a_H i_H Y_H +a_L i_L Y_L}{a_H i_H + a_L i_L}$$

- utility function that makes each group reduce partners by equal absolute amounts

$$u_k (i) = \theta_k i_k - \psi i_k ^2$$

- For simplicity, assume low prevalence so that probability of infection can be approximated as linear in number of partners
    - This means if cost of infection is $c$, then optimand is 

$$u_k(i) - i \beta c W$$

- At the optimum

$$i_k = \max \left\{ \frac{\theta_k}{2\psi} - \frac{\beta c W}{2\psi}, 0 \right\}$$

- If all groups have $i > 0$, then an increase in prevalence of $\Delta$ will cause all groups to reduce partners by $\frac{\beta c \Delta}{2\psi}$
    - This will increase $W$ because equal absolute reductions are larger proportional reductions for less active group.
    - Easy to see for this util func, but similar positive feedback happens with isoelastic util , where reduction is equiproportional to increase in marg prob of infection 
        - marginal prob less sensitive for high active people, so smaller proportional reductions than low active
        - More general, under random mathching, positive feedback happens whenever highly active people reduce activity proportionally less than less active people.
  

### Equilibrium

$$(i_H, i_L)$$ 
is an equilibrium given prevalences if
the resulting $$W$$ causes groups to choose those $i$s.

$$(i_H, i_L, Y^*_H, Y^*_L)$$
is a steady state equilibrium if the $i$s
are a steady state given the $Y$s, and the $Y$s are the prevalences from the $i$s 

Multiple equilibria for moderate prevalences.

For high enough prevalence, unique equilibrium with $i_L = 0$

For low enough prevalence, unique equilibrium with $i_L > 0$

#### Proposition 1
1. If $$Y_H < \theta_L$$, there will be unique equilibrium with $i_L > 0$
2.  If $$Y_H > \theta_L$$, and $$Y_H > [\theta_L (1+a_H)-a_H \theta_H - a_L Y_L]/a_H$$, there will be unique equilibrium with $i_L > 0$
3.  If big tangle of algebra, then one equi with $i_L = 0$ and two with $\ > 0$


#### steady states?

In randomly mixing population, 

$$\frac{dY_j}{dt} = \textcolor{brown}{\beta} \textcolor{green}{i_j (1-Y_j)} \textcolor{blue}{\sum_k \frac{i_k Y_K a_k}{\sum_k i_k a_k}} - \textcolor{red}{\delta Y_j}$$

The change in prevalence for a group is
<span style="color:brown">the chance of infection from contact</span>
times <span style="color:green">the number of contacts uninfected members have</span>
times <span style="color:blue">the chance that a random contact is infected</span> minus <span style="color:red">the members of that group that die.</span>

Divide by $Y_j$,
take the limit as prevalence goes to zero,
and use the approximation that $Y_k \over Y_j$ approaches $i_k \over i_j$ at low prevalence.
(anderson, May, 1991)

Then in low prevalence populations, 

$$R_0 \approx \frac{\beta}{\delta} c$$

where c is a weighted average number of partners

$$c \equiv \sum_k \frac{i_k^2 a_k}{\sum_k i_k a_k}$$

Let $\mu$ and $\sigma^2$ denote the mean and variance of of number of partners per period???

- Express $c$ as $c=\mu+\sigma^2 / \mu$.
- $dc/d\mu = 1-\sigma^2/\mu^2$
- differentiate c wrt to i, to get that increases in activity by group with fewer than $c/2$ partners ill reduce $R_0$.
- equal increase in activity by all individuals will reduce $R_0$ if $\mu < \sigma$
    - Kremer 1995
- Not an unreasonable condition. 
    - NSSAL found in Britain, mean partners over last five years 1.98 and variance 4.36
    - Johnson et al 1994
- can have multiple equilibria where low-activity equilibrium has disease, and high activity equilibrium does not.
- possible story: waiting until disease is established makes eradication impossible.




### High prevalence populations

Situation where increased prevalence increases number of partners for high-activity people.

- utility function: $$u_k(i) = -\tau_k / i$$
- two groups, high activity  and low, denoted by $H$ and $L$
- each group $k$ comprises $a_k$ portion of the population
- elasticity of partners wrt prob infection is $1/2^{22}$???
- at the optimum
    
    $$i_k = \min \left\{
    \frac{\delta}{\sqrt{\delta \beta W \over \tau_k}-\beta W}
    ,i_{max}\right\}$$ (bc)
    
    for $\delta\in(0,\tau_k \beta W)$ and 
    $i_{max}$ otherwise.

- optimal partners delcines in $W$ until $p(i)=1/2$, then increases to $i_{max}$???
- assume $i_{max}$ is so high that prevalence among such people can be approximated as 1.
- To get constant prevalence, each group must satisfy

$$\beta i_k (1-Y_k) W = \delta Y_k$$ (ec)

- so any steady state equilibrium must satisfy both the behavioral condition (bc) and the epidemiological condition (ec)
- set of ss equilibria depend on $t_k$ values
    - if $$\tau_L,\tau_H > \delta/\beta$$, then $$i_L=i_H-i{max}$$
    - For very low $\tau$s, we get submaximal partner rates.
    - For some parameter values, can construct multiple ss equil
        - If $$a_h i_{max} > > a_L i_L(1)$$, then high-activity people can dominate the pool
        - In this case, If there is a submaximal sse, will also be a sse  in which $i_H$ is maximal, so $W\approx 1$ and 

        $$i_L\approx i_L(1) = \frac{\delta}{\sqrt{\delta \beta \over \tau_k}-\beta}$$
        - Social welfare could be better in the low variance steady state (because lower pool risk and thus better tradeoff between sex and disease risk) despite higher unweighted prevalence
        - Example: small population of turbo-horndogs all have the disease. Larger population of prudes can't have sex at all due to disease risk from random mixing
        - Example 2: three types: horndogs, prostitutes, and prudes. If prudes stop having sex because of increased risk, more horndogs go to prostitutes, which further increases prevalence (I recall reading some empirical examples of this, but not in this paper)


### Preferred matching

- High activity people are more likely to match with each other.
    - Kaplan Cramton Palteil 1990
- Preferred matching model
    - people match within group with probability $\gamma$
    - match randomly with probability $1-\gamma$
    - Jacquez et al 1988
- Probability your partner is infected: $$\gamma Y_j + (1-\gamma)W$$
- Larger set of circumstance in which positive feedback loops can happen.

Multiple equilibria can't occur if elasticity of partners to marginal infection probability is less than one

- denote number of partners of other low activity people $\bar i_L$
- denote preferred num partner for low-active person $$i^*(\bar i_L, i_H) = i^*(\bar i_L, i_H(\bar i_L))$$
    - For isoelastic utility and $Y_L > 0$, this fucntion is continuous, bounded, and has positive intercept
    - Thus $$di^*_L / d \bar i_L$$ must be greater than one at some point to have multiple equilibria.
    - An x percent increase in $\bar i_L$ will necessarily reduce pool risk by less than x percent???
    - I don't follow the last step of the proof. confused




### Conclusions

Focus public health messages on high-activity individuals.

Behavioral response can either increase or decrease effectiveness of health intervention.

High-activity people can become fatalistic, increasing activity in response to increased prevalence.



This is for endemic disease. What about for transient disease epidemic?