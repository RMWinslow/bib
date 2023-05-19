---
parent: Papers
---

# Optimal unemployment insurance

[link](https://www.journals.uchicago.edu/doi/abs/10.1086/262078?casa_token=P5MAbZEzOMUAAAAA:m57thXoRwoiUbOXc6FkIoAAIrDntRRAA-uxHFn73EuInIzXfRRTGmlSmvhbP5W5vaUi9TLiSqpo)

## BibTeX
```
@article{hopenhayn1997optimal,
  title={Optimal unemployment insurance},
  author={Hopenhayn, Hugo A and Nicolini, Juan Pablo},
  journal={Journal of political economy},
  volume={105},
  number={2},
  pages={412--438},
  year={1997},
  publisher={The University of Chicago Press}
}
```

## Abstract

> This paper employs a dynamic general equilibrium model to design and evaluate 
long-term unemployment insurance plans (plans that depend on workers’ unemployment 
history) in economies with and without hidden savings. We show that optimal benefit 
schemes and welfare implications differ considerably in these two economies. Switching 
to long-term plans can improve welfare significantly in the absence of hidden savings. 
However, welfare gains are much lower when we consider hidden savings. Therefore, we 
argue that switching to long-term plans should not be a primary concern from a policy 
point of view.



## Notes and excerpts

### Model

- Goal is to maximize 

    $$E \sum_t β^t [u(c_t) - a_t]$$

    where $a_t$ is search effort at time $t$

- Probability of finding a job is $p_t = p(a_t)$ (str incr, str concave down, twice diff, satisfies Inada)
  - Hah, search effort is allowed to be negative. Range just has to include 0. Deliberate effort *not* to find a job?
- Principal (the gov) can perfectly control agent's (worker's) consumption stream. (No private savings, essentially)
- all jobs are identical and permanent, offering wage $w$
- contracts map employment history to $\Set{a_t,z_t}$, where $a_t$ is recommended effort and $z_t$ is net transfer

#### Full information

Principle is risk neutral, agent is risk-averse.
So with observable effort, the problem just has principle bear all the risk.

Optimal plan would be to offer constant $c$
and prescribe constant effort level $a^\star$ which solves:

$$a^\star = \argmax_a p(a) \sum_t δ^t [1-p(a)]^t \left[ \frac{δ u'(c)w}{1-δ}-a \right]$$




#### Unobservable Search Effort

Job search has a cost.

Suppose contract offers expect discounted utilities $V$.
Let $V_e$ be edutility at the beginning of next period if you find a job at the end of this period,
and $V_u$ edutility if you don't.

It follows that 

$$V = u(c) - a + β\left[p(a)V_e + (1-p(a))V_u\right]$$

By incentive compatibility, the contractually recommend effort $a$ must maximize the above expression.

Because concave $p()$, nascondtion for $a$ is 

$β p'(a) (V_e-V_u) = 1$


Since employment is permanent, 
contract after finding job is just to give constant $c_e$ 
defined implicitly by 

$$V_e = \frac{u(c_e)}{1-β}$$

Then given continuation cost of providing contract to employed, contract must minimize costs of program subject to guaranteeing some value $V$ for unemployed person at time 0.
Problem may not be convex, so solved with numerical approximation.



---

### Analysis of optimal contracts in model

- unemployment benefit decreasing over time
- If cost of program $C(V)$ is convex, then $V_u < V$
- Wage tax dependent on unemployment history (because contract must punish longer unemployment with lower claims on future consumption)
- Under (some conditions), tax levied on worker will increase with length of previous unemployment spell
- Suppose $\frac{-p''(a)}{p'(a)^2}$ increasing in $a$ and $C(V)$, then $V_u$ will be increasing function of $V$


---

### Calibrating to US unemployment insurance

TODO: More notes here.

>  Note
also that for the first 5 weeks the tax is negative, which means that
unemployed workers receive a permanent subsidy if they find a job
quickly.



----

Thought about this pper and others:
What are the effects of wealth restrictions on program eligibility?
Changes nature of optimal program. What does it do for utility?

> As in other models of repeated moral hazard, we have assumed
that the principal controls directly the consumption of the agent. A
feature that is common to all these models is that along the optimal
contract the agent is savings-constrained: if the agent could save part
of the transfer received without knowledge of the principal, he
would choose to do so.

I'm thinking of how some food stamps in the US only have an income limit, 
while others also have an asset limit.
(My HH only eligible for the former.)





