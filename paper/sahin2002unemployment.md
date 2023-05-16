---
parent: Papers
---

# Unemployment insurance and the role of self-insurance

[pdf link](https://academiccommons.columbia.edu/doi/10.7916/D83X8JS7/download)

## BibTeX
```
@article{sahin2002unemployment,
  title={Unemployment insurance and the role of self-insurance},
  author={Abdulkadiro{\u{g}}lu, Atila and Kuru{\c{s}}{\c{c}}u, Burhanettin and {\c{S}}ahin, Ay{\c{s}}eg{\"u}l},
  journal={Review of Economic dynamics},
  volume={5},
  number={3},
  pages={681--703},
  year={2002},
  publisher={Elsevier}
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

> The model we study is different from the ones analyzed in the cited papers in several
aspects. First of all, we do not look at fully optimal dynamic contracts since they are
difficult to characterize when agents have hidden savings...
Secondly, we focus on the moral
hazard problem based on unobservability of job refusals as opposed to the job-search effort...
Thirdly, we insist on budget balance of the unemployment insurance system. 



Model is possibly a good teaching example.


<!--Hopefully, I can copypaste the following snippet into a remark slides template without modification-->



### Consumer's choices

The consumer's optimand is straightforward:

$$E \sum_j \beta^j U(c_j,l_j) = E \sum_j \beta^j \frac{(c^{1-\sigma}l^\sigma)^{1-\rho}-1}{1-\rho}$$

Two decisions the consumer faces:

1. How to split income between consumption and (non-interest-bearing) savings
    - budget is $m'+c = m+y_d$, where $m$ is assets, and $y_d$ is disposable income.
    - assets are subject to the constrain $m'\geq 0$

2. Whether to work (when the worker has a job offer)
    - The worker can either choose not not to work, in which case $l=1$
    - or they can choose to work a fixed amount $\hat h (=0.45)$, in which case $l=1-\hat h$
    - Beyond this possible binary decision each period, they can't choose *how much* to work.
 


---

### Model of Job Search

Three more state variables are introduced: $s,\eta,\mu$.

- Employment opportunity $s\in\set{e,u}$ represents whether the person has a job opportunity ($s=e$) or not ($s=u$).
    - $s$ evolves according to a 2x2 transition matrix $\chi$, calibrated like so:

$$\chi = 
\begin{bmatrix}
   \chi(e,e) & \chi(e,u) \\
   \chi(u,e) & \chi(u,u)
\end{bmatrix} =
\begin{bmatrix}
   0.9681 & 0.0319 \\
   0.5 & 0.5
\end{bmatrix}
$$


- employment status $\eta\in\Set{0,1}$ represents whether the person actually works. 
- $\mu\in\set{0,1}$ indicates whether the person collects unemployment benefits.
    - If $(s,\eta)=(e,0)$, there is a probability $\pi(t)$ that the person collects benefits and probability $1-\pi(t)$ they do not.
    - Otherwise, $\mu$ works as you'd expect. 
        - $(s,\eta)=(e,1) \implies \mu=0$, 
        - and $s=u \implies \eta=0, \mu=1$

<!--
- Note that $s=u \implies \eta=0$. But if the person chooses not to accept an employment opportunity, $(s,\eta)=(e,0)$.
-->

---

### Structure of Unemployment Insurance

$$\theta(t) = 
\begin{cases}
    \theta_t & \text{if } t\in\{0,...,T-1\} \\
    \theta_T & \text{if } t\geq T
\end{cases}$$

- Each $\theta$ is a replacement ratio, meaning that a person collecting unemployment insurance receives a fraction of their typical income.
- $t$ is the duration of the person's current unemployment spell. (optimal benefits will taper off)
    - $t$ increments whenever the person does not work ($\eta=0$). And $t=0$ if the person worked last period.
- For tractability the replacement ratio is constant from period $T$ of unemployment onwards.



---

### Disposable Income

$\tau$ is the proportional tax rate.

- If the person is working ($\eta=1$), then disposable income is $y_d=(1-\tau)y$
- If the person isn't working:
    - If they collect benefits, then $y_d=(1-\tau)\theta(t)y$
    - If they don't, then $y_d=0$


<!--(And yes, real-world unemployment benefits are taxed, at least in Minnesota)-->



<!--

---

### Value Function

...

$$\gdef\CONTINUEUNEMP#1{\beta\sum_{s'}\chi(#1,s')V(m',s',t+1)}$$

$$\gdef\VCOLLECTUI{\max_{m'}\Set{
    U(m+(1-\tau)\theta(t)y-m',1) + \CONTINUEUNEMP{u}}}$$

$$V(m,u,t)=\VCOLLECTUI$$



$$\gdef\VCOLLECTUIalt{\max_{m'}\Set{
    U(y_d(x)+m-m',1) + \CONTINUEUNEMP{u}}}$$

$$V(m,u,t)=\VCOLLECTUIalt$$
-->

---

### Market Clearing and Equilibrium

State of a person is $x=(m,s,t,\mu)$

Stationary equilibrium consists of 
- decision rules $\eta(m,s,t)$, $c(x)$, $m'(x)$
- time-invariant measure $\lambda(x)$ of people in state $x$
- tax rate $\tau$

Such that

- Given $\tau$, the decision rule is optimal for the consumers.
- Goods market clears: $\sum_x \lambda(x) c(x) = \sum_x \lambda(x) \eta(x)y$
- $\lambda(x')=\lambda(x)$
- Government budget  balanced:

$$\sum_{m,t}\lambda(m,e,t,\textcolor{red}{0})\eta(m,e,t)\tau y =
\sum_{m,s,t}\lambda(m,s,t,\textcolor{red}{1})(1-\tau)\theta(t)y$$



---



### Social Planner's Problem

$$\max\sum_{t=0}^\infty \beta^t \lbrack N_t U(c_{1t}, 1-\hat h) + (1-N_t)U(c_{2t},1) \rbrack$$

subject to 

$$N_t c_{1t} +  (1-N_t) c_{2t} \leq N_t y, \;\; N_t \leq \bar N$$


Where 
- $N_t$ is employment rate, 
- $c_{1t}$ is consumption for employed people
- $c_{2t}$ is consumption for unemployed people
- $\bar N$ is set to 0.94



In the following slide, welfare cost of an equilibrium
is given as $1-\phi$,
where $phi$ is the value such that $(\phi c_{1t}, \phi c_{2t})$
gives the same average utility as the equilibrium allocations.



---


### Summary of Optimal Plans

$\pi(1)=1$ for all of the following:

| Case | $\theta$ | emp rate | $1-\phi$ | 
|:-:|:-:|:-:|:-:|
| T=1, No savings, $\pi(0)=0$ | .25 | .94 | 2.50% |
| T=4, No savings, $\pi(0)=0$ | .65, .65, .65, .3 | .90 | 0.485% |
| T=1, No savings, $\pi(0)=1$ | .25 | .94 | 2.50% |
| T=4, No savings, $\pi(0)=1$ | .3, .25, .25., .2 | .94 | 2.50% |
| Savings, no UI | 0 | .94 | 0.683% |
| T=1, Savings, , $\pi(0)=0$ | .05 | .94 | 0.683% |
| T=4, Savings, $\pi(0)=0$ | .95, 0, 0, .1 | .94 | 0.483% |
| T=1, Savings, $\pi(0)=1$ | 0 | .94 | 0.683% |
| T=4, Savings, $\pi(0)=1$ | 0, 0, .05, .05 |  | 0.634% |








