---
parent: Papers
---

# Really uncertain business cycles

[pdf link](https://drive.google.com/file/d/118x7m_7cMB55OdO1TLfUWv_io7yfISyy/view)

[Nick Bloom's Research Page](https://nbloom.people.stanford.edu/research)

[NBER page](https://www.nber.org/papers/w18245)

## BibTeX
```
@article{bloom2018really,
  title={Really uncertain business cycles},
  author={Bloom, Nicholas and Floetotto, Max and Jaimovich, Nir and Saporta-Eksten, Itay and Terry, Stephen J},
  journal={Econometrica},
  volume={86},
  number={3},
  pages={1031--1065},
  year={2018},
  publisher={Wiley Online Library}
}
```

## Abstract

> We investigate the role of uncertainty in business cycles. First, we demonstrate that microeconomic uncertainty rises sharply during recessions, including during the Great Recession of 2007–2009. Second, we show that uncertainty shocks can generate drops in gross domestic product of around 2.5% in a dynamic stochastic general equilibrium model with heterogeneous firms. However, we also find that uncertainty shocks need to be supplemented by first-moment shocks to fit consumption over the cycle. So our data and simulations suggest recessions are best modelled as being driven by shocks with a negative first moment and a positive second moment. Finally, we show that increased uncertainty can make first-moment policies, like wage subsidies, temporarily less effective because firms become more cautious in responding to price changes.


## My Notes



> recessions appear to be characterized by a negative first-moment and a positive
second-moment shock to the establishment-level driving processes.

<!--## Empirics
TODO: Come back to this part-->


### Model

DEviates from RBC model in three ways
- uncertainty varies across time
- heterogenous firms
- nonconvex adjustment costs in capital and labor

These make firms more cautious when uncertainty is high.



> First, we add to the extensive
literature building on the DSGE framework that studies the role of TFP shocks in caus-
ing business cycles. In this literature, recessions are generally caused by large negative
technology shocks (e.g., King and Rebelo (1999)). The reliance on negative technology
shocks has proven to be controversial


### Measuring uncertainty

Assume firm $j$ produces output in time period $t$ according to 

$$y_{jt} = A_t z_{jt} f(k_{jt}, n_{jt})$$

Productivity is product of aggregate $A$ and idiosyncratic $z$.
Both follow [AR processes](https://en.wikipedia.org/wiki/Autoregressive_model)

$$\log A_t = \rho^A \log A_{t-1} + \sigma^A_{t-1} \epsilon_t$$

$$\log z_{jt} = \rho^Z \log z_{j,t-1} + \sigma^Z_{t-1} \epsilon_{jt}$$

Variances of innovations $\sigma^*_t$ both move according to two-state markov chains.

### Firm Technology

Diminishing returns to scale

$$y_{jt} = A_t z_{jt} k^\alpha_{jt}, n^\nu_{jt}$$

Law of motion of capital

$$k_{j,t+1} = (1-\delta_k) k_{jt} + i_{jt}$$

Capital adjustment costs $AC_k$
sum of fixed disruption cost $F^k$
and resale loss for disinvestment.

$$
AC_k =\begin{cases}
        0, & \text{if $i=0$}\\
        y(z,A,k,n)F^k, & \text{if $i > 0$}\\
        y(z,A,k,n)F^k - Si, & \text{if $i < 0$}\\
    \end{cases}
$$

Law of motion for hours worked.

$$n_{jt} = (1-\delta_n) n_{j,t-1} + s_{j,t}$$

$\delta_n$ from retirement, quitting, etc.

Labor adjustment costs

$$
AC_n =\begin{cases}
        0, & \text{if $s=0$}\\
        y(z,A,k,n)F^L + |s|Hw, & \text{otherwise}\\
    \end{cases}
$$

Let $\mu$ denote joint distribution of firm level variables (idio prod, capital, labor) in the last period.


### Firm value function

Let $X$ denote a firm's state variables:

$$X = (k,n_{-1},z;A,\sigma^A,\sigma^Z,\mu)$$

Let $@$ denote the aggregate state variables

Firm's problem is choose investment and labor to maximize 

$$V(X) = \max_{i,n} \left[
        y - wn - i - AC^k (X) - AC^n (X) 
        + E[mV(X')]
    \right]$$


given 
- law of motion for joint distribution $\mu' = \Gamma(A,\sigma^A,\sigma^Z,\mu)$
- wage determined by $w(A,\sigma^A,\sigma^Z,\mu)$
- stochastic discount factor $m(A,\sigma^A,\sigma^Z,\mu,A',\sigma'^A,\sigma'^Z,\mu')$

$K(X)$ and $N^d(X)$ denote policy rules.


### Households

Let $\psi$ denote one period purchased shares in firms.

HH problem is 

$$W(@) = \max_{C,N,\psi'} \{
        U(C,N)+\beta E[W(@')]
    \}$$

subject to law of motion for $\mu$ and a sequential budget constraint

$$C + \int q\ d\psi' \leq wN + \int \rho\ d\mu$$

where
- sum of dividends and resell values of stocks $\rho(k,n_{-1},@)$ integrated across distribution of firms.
- new shares bought at prices $q(X')$, integrated over share purchasing.
- wage $w(@)$

Policy functions $C(\psi,@),N^s(\psi,@),\Psi'(\psi,@)$



### Market clearing

Assets market:

$$\mu'(k',n,z') = \int \psi'(k',n,z) f(z'|z)\; dz$$

Goods Market:

$$C(\psi,@) = \int [Azk^\alpha N^d (X)^\nu - K(X) + (1-\delta_k)k - AC^k(k,K(X)) - AC^n (n_{-1}, N(X))] \; d\mu$$

Labor market:

$$N^s (\psi,@) = \int N^d() \; d\mu$$

And the law of motion for distribution $\Gamma$ is generated by the policy functions and exogenous evolution of state variables.

TODO: Come back and standardize the state notations. The paper just full writes them out.

$$\newcommand\agst{\checkmark}$$

$$\agSt = A, \sigma^A...$$


### Solving model

> heavily relies on the approach in Khan
and Thomas (2008) and Bachmann, Caballero, and Engel (2013)

From HH, get

$$w = - \frac{U_N}{U_C}$$

$$m = \beta\frac{U_C'}{U_C}$$

Assume utility seperable across consumption and work

$$U(C,N)={C^{1-\eta} \over 1-\eta} - \theta \frac{N^\chi}{\chi}$$

These imply equilibrium wage is 
$w = \theta N^{\chi-1}C^\eta$

Define intertemporal price $p(@)=U_C$
then redfine value fucntion $\tilde V=pV$

$$\tilde V(X) = \max_{i,n} p(@)(y-wn-i-AC) + \beta E[\tilde V(X')]$$

Then apply nonlinear techniques from Krusell and Smith 89. 

### Calibrating

Can't calibrate for uncertainty process vars, so have to use 
[SMM](https://en.wikipedia.org/wiki/Method_of_simulated_moments)

Quarterly periods so:

|var|value|justification|
|---|---|---|
||||
|$\beta$|$0.95^{1/4}$||
|$\eta$|1|unit elastic intertemporal subs|
|$\theta$|2|spend third of time working|
|$\chi$|1|infinite frisch elasticity|
|$\alpha$|0.25|TODO|
|$\nu$|0.5|CRS labor share 2/3 |
|$\rho^A$|0.95|persistance of prod shock|
|$\rho^Z$|0.95|Kahn Thomas 08|
||||
|$\delta_k$|0.026|Annual depr of 10%|
|$\delta_n$|0.088|Annual 35% (Shimer 2005)|
|$F^K$|0||
|$S$|0.339|Resale loss Bloom 2009|
|$F^L$|0.021|pc of annual sales|
|$H$|0.018|pc of annual wage bill|


Treat two uncertainty markovs as just one.
Estimate from US data.
TRansition low to high 2.6% of quarters.
TRans back 6% of quarters.

||low|high|
|---|---|---|
|Agg Vol|0.67%|1.07%|
|Idio Vol|5.1%|20.91%|


<!--### Consquences
TODO: read more about predictions of model.-->