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


### Structure of Unemployment Insurance

$$\theta(t) = 
\begin{cases}
    \theta_t & \text{if } t\in\{0,...,T-1\} \\
    \theta_T & \text{if } t\geq T
\end{cases}$$

- Each $\theta$ is a replacement ratio, meaning that a person collecting unemployment insurance receives a fraction of their typical income.
- $t$ is the duration of the person's current unemployment spell. (optimal benefits will taper off)
- For tractability the replacement ratio is constant from period $T$ of unemployment onwards.


---

### Consumer's choices

The consumer's optimand is straightforward:

$$E \sum_j \beta^j U(c_j,l_j) $$

Two decisions the consumer faces:

1. How to split income between consumption and (non-interest-bearing) savings
    - budget is $m'+c = m+y_d$, where $m$ is assets, and $y_d$ is disposable income.

2. Whether to work (when the worker has a job offer)
    - The worker can either choose not not to work, in which case $l=1$
    - or they can choose to work a fixed amount $\hat h (=0.45)$, in which case $l=1-\hat h$
    - Beyond this possible binary decision each period, they can't choose *how much* to work.
 


---

### Model of Job Search

Three more state variables are introduced: $s,\eta,\mu$.

- Employment opportunity $s\in\{e,u\}$ represents whether the person has a job opportunity ($s=e$) or not ($s=u$).
    - $s$ evolves according to a 2x2 transition matrix $\chi$, calibrated like so:

$$\chi = 
\begin{bmatrix}
   \Pr(s'=e|s=e) & \Pr(s'=u|s=e) \\
   \Pr(s'=e|s=u) & \Pr(s'=u|s=u)
\end{bmatrix} =
\begin{bmatrix}
   0.9681 & 0.0319 \\
   0.5 & 0.5
\end{bmatrix}
$$


- employment status $\eta\in{0,1}$ represents whether the person is actually working. 
    - Note that $s=u \implies \eta=0$. But if the person chooses not to accept an employment opportunity, $(s,\eta)=(e,0)$.
- $\mu\in\{0,1\}$ indicates whether the person collects unemployment benefits.
    - If $(s,\eta)=(e,0)$, there is a probability $\pi(t)$ that the person collects benefits and probability $1-\pi(t)$ they do not.
    - Otherwise, $\mu$ works as you'd expect. 
        - $(s,\eta)=(e,1) \implies \mu=0$, 
        - and $(s,\eta)=(u,0) \implies \mu=0$



--- 

### Value Function and State?

---


### Summary of Results




