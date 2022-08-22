---
parent: Papers
---

# The spread of epidemic disease on networks

[arxiv link](https://arxiv.org/abs/cond-mat/0205009) 

[arxiv pdf](https://arxiv.org/pdf/cond-mat/0205009.pdf)

## BibTeX
```
@article{newman2002spread,
  title={Spread of epidemic disease on networks},
  author={Newman, Mark EJ},
  journal={Physical review E},
  volume={66},
  number={1},
  pages={016128},
  year={2002},
  publisher={APS}
}
```

## Abstract

> The study of social networks, and in particular the spread of disease on networks, has attracted considerable recent attention in the physics community. In this paper, we show that a large class of standard epidemiological models, the so-called susceptible/infective/removed (SIR) models can be solved exactly on a wide variety of networks. In addition to the standard but unrealistic case of fixed infectiveness time and fixed and uncorrelated probability of transmission between all pairs of individuals, we solve cases in which times and probabilities are non-uniform and correlated. We also consider one simple case of an epidemic in a structured population, that of a sexually transmitted disease in a population divided into men and women. We confirm the correctness of our exact solutions with numerical simulations of SIR epidemics on networks. 


## My Notes


>  Epidemic behavior usually shows a phase transition
with the parameters of the model—a sudden transition from
a regime without epidemics to one with. This transition hap-
pens as the ‘‘reproductive ratio’’ R 0 of the disease, which is
the fractional increase per unit time in the number of infec-
tive individuals, passes though one.

> Within the class of fully mixed models much elaboration
is possible, particularly concerning the effects of age struc-
ture in the population, and population turnover. The crucial
element however that all such models lack is network topol-
ogy.

### Standard SIR

$s(t)$, $i(t)$, $r(t)$ are fractions of population susceptible, infective, recovered at time $t$.

$$\frac{ds}{dt} = -\beta i s$$

$$\frac{di}{dt} = \beta i s - \gamma i$$

$$\frac{dr}{dt} = \gamma i$$

Disease that spreads quickly and confers immunity. This model not appropriate for diseases that propogate on larger time scales.

> The model described above assumes that the population is
fully mixed, meaning that the individuals with whom a sus-
ceptible individual has contact are chosen at random from
the whole population. It also assumes that all individuals
have approximately the same number of contacts in the same
time, and that all contacts transmit the disease with the same
probability.

This paper tweaks so disease transmission can only happen along edges of social graph

### Network based model

#### chance of transmission along connection

- Person $i$ is infective
- Person $j$ is susceptible
- average rate of disease causing contacts $r_{ij} between them$
- Person $i$ remains infective for time $\tau_i$
- Probability disease will not transmit form $i$ to $j$: $$1-T_{ij} = \lim_{\delta t\to 0}(1-r_{ij} \delta t)^{\tau_i /\delta t} = e^{-r_{ij}\tau_i}$$
- Probability of transmission: $$T_{ij} = 1-e^{-r_{ij}\tau_i}$$
    - In discrete time, $$T_{ij} = 1-(1-r_{ij})^{\tau_i}$$
- If $r_{ij}$ and $\tau_i$ are iid, so is $T_ij$, and hence the a priori prob of transmission is just $T$, the mean of $T_{ij}$
    - This makes things solvable.
- this encompasses SEIR models with incubation as well
    - abstracts away from temporal behavior of infectivity and the like
- equivalent to edge percolation where edges are occupied with iid probability $T$

#### probability generating functions

$$G_0(x) \equiv \sum_k p_k x^k$$

$$G_0(1) = \sum_k p_k 1^k = \sum_k p_k = 1$$

$$p_k = \frac{1}{k!}\frac{d^k G_0}{dx^k} |_{x=0}$$

#### Power property:

If $G$ is the pgf for some distribution over non-negative integers, then the sum of $m$ iid draws has pgf 
$$[G_0(x)]^m$$

#### Moments Property:

Mean is given by first derivative evaluated at 1.

$$E[k] = \sum_k k p_k = G^\prime_0 (1)$$

higher moments more complicated:

$$E[k^n] = \sum_k k^n p_k = \left[ \left( x^n \frac{d}{dx} \right)^n G_0(x) \right]_{x=1}$$

#### Excess degree of neighbor

If we follow random edge to its end, we are biased towards vertices with high degree.

Chance that end of randomly selected edge has degree $k$ is the portion of edges in the network connected to nodes with degree $k$:
$$k p_k / \sum_k kp_k$$

Thus the pgf for degree of neighbor is 

$$\frac{\sum_k k p_k x^k}{\sum_k k p_k} = x\frac{G^\prime_0 (x)}{G^\prime_0 (1)}$$

But if we want to exclude the edge we arrived on, we call this *excess degree*. Chance that a random neighbor has excess degree k is chance that that neighbor has degree $k+1$: 
$$(k+1) p_{k+1} / \sum_k kp_k$$

The pgf for the distribution of excess degrees of our neighbors is 

$$G_1 (x) \equiv \sum_k \frac{(k+1) p_{k+1} x^k}{\sum_k kp_k} = \frac{1}{x}\frac{\sum_k k p_k x^k}{\sum_k k p_k} = \frac{G^\prime_0 (x)}{G^\prime_0 (1)} = \frac{G^\prime_0 (x)}{\mu_k}$$

#### distribution of occupied edges

Probability of vertex having exactly $m$ of $k$ edges filled is 
$$\binom{k}{m}T^m (1-T)^{k-m}$$

pgf is thus

$$G_0 (x;T) \equiv \sum_k p_k \sum_{m=0}^k \binom{k}{m}T^m (1-T)^{k-m} x^m$$

$$G_0 (x;T) = \sum_k p_k (1-T+xT)^k$$

$$G_0 (x;T) = G_0(1-(1-x)T)$$

Similarly, 

$$G_1(x;T)=G_1(1-(1-x)T)$$


#### cluster size (outbreak size)

$H_1$ is pgf for size of cluster of connected vertices reached by going to end of random edge.

$$H_1(x;T) = xG_1(\ H_1(x;T)\ ;T) \tag{17}$$

$H_0$ is size of cluster starting from random vertex

$$H_0(x;T) = xG_0(\ H_1(x;T)\ ;T)$$

Can get distribution of cluster sizes $P_s(T)$ by differentiation. 
Typically done numerical. Approximation can cause problems.
Paper recommends numerical contour integration using Cauchy formula over the unit circle.

$$P_s(T) = \frac{1}{s!}\frac{d^s H_0}{dx^s} |_{x=0} = 
\frac{1}{2\pi i} \oint \frac{H_0 (\zeta;T)}{\zeta^{s+1}}d\zeta
$$


#### mean outbreak size

But can find outbreak size in closed form:

$$\mu_s = H^\prime_0 (1;T) = 1+G_0^\prime (1;T) H_1^\prime (1;T)$$

Differentiate

$$H_1(x;T) = xG_1(\ H_1(x;T)\ ;T)$$

$$H_1^\prime(1;T) = 1+G_1^\prime(1;T) H_1^\prime(1;T)$$

$$H_1^\prime(1;T) = \frac{1}{1 - G_1^\prime(1;T)}$$

So 

$$\mu_s = 1+G_0^\prime (1;T) \frac{1}{1 - G_1^\prime(1;T)}
= 1+ \frac{TG_0^\prime(1)}{1-TG_1^\prime (1)}$$

Or in other words, if $\mu_k$ is the mean degree of nodes
and $\mu_{ke}$ is the mean excess degree of neighbors,
then  mean outbreak size is

$$\mu_s = 1 + \frac{T\mu_k}{1-T\mu_{ke}}$$

#### Epidemic threshold

Divergence in $\mu_s$
at $T\mu_{ke}=1$

This occurs at critical transmissibility $T_c$

$$T_c = \frac{1}{\mu_{ke}} = \frac{1}{G_1^\prime} = \frac{\mu_k}{G_0^{\prime\prime}\ } = \frac{\sum_k k p_k}{\sum_k k (k-1) p_k}$$

Above threshold, we have giant component and (17) no longer valid because might have loops.
To fix, redefine $H_0$ as pgf for non-epidemic outbreaks - clusters unconnected to giant cluster.
Above, threshold, these don't fill entire graph:

$$H_0 (1;T) = \sum_s P_s = 1-S(T)$$

where $S(T)$ is fraction of population affected by epidemic, and also chance that an outbreak will cause an epidemic.
Really just measuring chance a node is in the giant cluster.

$$S(T) = 1-H_0(1;T) =  1 - G_0 (H_1(1;T);T) =  1 - G_0 (u;T)$$

where $u$ is the solution to $u=G_1(u;T)$.


#### degree of infected people

Solution to $u$ above can be interpreted as probability that the end of a random edge remains uninfected/ belongs to finite cluster.

- Probability a specific neighbor doesn't get you sick is chance no transmission $1-T$ + chance they would transmit but never get sick $Tu$.
    - $v=1-T+Tu=1-(1-u)T$
- Probability you don't get sick during epidemic if you have $k$ neighbors
    - $v^k = (1-(1-u)T)^k$
- Probability that vertex has degree $k$ given that it is uninfected 
    - $$\frac{p_k v^k}{\sum_k p_k v^k}=\frac{p_k v^k}{G_0(v)}$$
    - pgf is $$\frac{G_0(vx)}{G_0(v)}$$

Average degree of vertices outside giant component (unifected) is 
$$z_{out} 
= v\frac{G_0^\prime(v)}{G_0(v)} =  v\frac{G_1(v)}{G_0(v)}z
=\frac{u[1-(1-u)T]}{1-S}z$$

Pgf for infected vertices: 
$$\frac{G_0(x)-G_0(vx)}{1-G_0(v)}$$

Mean degree of infected vertices

$$z_{in} = \frac{1-vG_1(v)}{1-G_0(v)}z = \frac{1-u[1-(1-u)T]}{S}z$$

where $z\equiv \mu_k$


- $1-S = G_0(u;T) \leq u$
    - $G_0$ has only positive derivatives
    - It is convex everywhere within domain of convergence


### Example 1 

Power-law of exponent $a$ with exponential cutoff around degree $\kappa$

$$p_k = 0$$
for $k=0$ and
$$p_k = C k^{-a} e^{-k/\kappa}$$
for $k\geq 1$.

<details markdown="block" open>

C is fixed by normalization.

$$\sum_k p_k = \sum_k C k^{-a} e^{-k/\kappa} =1$$

$$C = \frac{1}{\sum_k k^{-a} e^{-k/\kappa} }$$

$$G_0(x) = \sum_k p_k x^k
= \sum_k \frac{k^{-a} (xe^{-1/\kappa})^k}{\sum_k k^{-a} (e^{-1/\kappa})^k}$$

$$G_0^\prime(x) = \sum_k \frac{k^{-a} (e^{-1/\kappa})^k x^{k-1} k}{\sum_k k^{-a} (e^{-1/\kappa})^k}
= \sum_k \frac{k^{-a+1} (xe^{-1/\kappa})^k}{x\sum_k k^{-a} (e^{-1/\kappa})^k}$$


$$\mu_k = \frac{\sum_{k}k^{-a+1}(e^{-1/\kappa})^{k}}{\sum_{k}k^{-a}(e^{-1/\kappa})^{k}}$$

???

$$G_1(x) = \frac{G_0^\prime(x)}{\mu_k}
= \frac{\sum_k k^{-a+1} (xe^{-1/\kappa})^k}{x\sum_k k^{-a+1} (e^{-1/\kappa})^k}$$

$$T_c = \frac{\sum_k k p_k}{\sum_k k(k-1) p_k}
= \frac{\sum_k k C k^{-a} e^{-k/\kappa}}{\sum_k k (k-1) C k^{-a} e^{-k/\kappa}}
$$

$$T_C = \frac{\sum_k C k^{-a+1} e^{-k/\kappa}}{\sum_k C k^{-a+2} e^{-k/\kappa} - C k^{-a+1} e^{-k/\kappa}}$$

</details>

Something something polylogarithm.

Simulation on 100000 vertices shows

>  the statistical properties of the disease outbreaks really
do depend only on the transmissibility T, and not on the
individual rates and times of infection. 

and

> Second, the data
clearly agree well with our analytic results for average out-
break size and epidemic size, confirming the correctness of
our exact solution. The small disagreement between simula-
tions and exact solution ... appears to be a finite size
effect, due to the relatively small system sizes used in the
simulations.

For example, with $a=2,\kappa=10$:
- simulations on random graphs suggest critical transmission threshold is $T_c\approx0.322$
- Exact solution gives $T_c \approx 0.329$
- Fully mixed SIR model would predict $T_c = 0.558$.



### Correlated transmission 

Let transmission rate $r$ vary. Person $i$ has transmission rate to others drawn from distribution $P_i(r)$.

A priori transmission probability

$$T_i = 1- \int_0^\infty  P_i(r)P(\tau)e^-rt \; drd\tau$$

Number of occupied edges leading from particular vertex is generated by

$$G_0(x;\{T_i\} = \frac{1}{N} \sum_{i=0}^N \sum_{m=0}^{k_i} \binom{k_i}{m} T_i^m (1-T_i)^{k_i-m}x^m$$

$$G_0(x;\{T_i\}) = \frac{1}{N} \sum_{i=0}^N [1-(1-x)T_i]^{k_i}$$

??? 
Excess degree generated by 

$$G_1(x;\{T_i\}) = \frac{\sum_i k_i [1-(1-x)T_i]^{k_i-1}\ }{\sum_i k_i}$$

PGF for small outbreaks:

$$H_0(x;\{T_i\}) = xG_0 (H_1(x;\{T_i\});\ \{T_i\})$$

$$H_1(x;\{T_i\}) = xG_1(H_1(x;\{T_i\});\ \{T_i\})$$

Critical trandsition happens when 
$$G_1^\prime(1;\{T_i\})=1$$

or equivalently when
$$\sum_i k_i [(k_i-1)T_i-1]=0$$

#### Example: T depends on on degree of infective person

$T_i$ is a function
only of $k_i$.

Then let $T_k$ denote mean transmissibility for vertices of degree $k$ and:

$$G_0(x;\{T_i\}) = \frac{1}{N} \sum_{i=0}^N [1-(1-x)T_i]^{k_i}
= \sum_k p_k [1-(1-x)T_k]^{k}$$

$$G_1(x;\{T_i\}) = \frac{\sum_i k_i [1-(1-x)T_i]^{k_i-1}\ }{\sum_i k_i}
= \frac{\sum_k k p_k [1-(1-x)T_k]^{k-1}\ }{\sum_k k p_k}$$


#### Example: T depends on on degree of person being infected

If the probability of transmission to a person with degree $k$ is $U_k$, then define

$$G_0(x;\{U_k\}) \equiv \sum_k p_k x^k$$

Independent of $\{U_k\}$ because the chance an infective person has the disease is 1.???

$$G_1(x;\{U_k\}) \equiv \frac{\sum_k k p_k [1-(1-x^{k-1})U_k]}{\sum_k k p_k}$$

???

#### Example: T depends on degree of both the giver and the reciever

Transmision occurs from person with degree $j$ to neighbor with degree $k$ 
with prob $$T_j U_k$$

$$G_0(x;\{T_k\},\{U_k\}) = \sum_k p_k [1-(1-x)T_k]^{k}$$

$$G_1(x;\{T_k\},\{U_k\}) = \frac{\sum_k k p_k [1-(1-[1-(1-x)T_k]^{k-1})U_k]}{\sum_k k p_k}$$


#### Example: T depends inversly on degree of infective

Specifically, have some baseline $T$ and then
$$T_k = T / k$$

Critical threshold at 

$$\sum_i k_i [(k_i-1)T_i-1] > 0$$

$$\sum_i k_i [(k_i-1)T/k_i-1] > 0$$

$$\sum_i [(k_i-1)T-k_i] > 0$$

$$T>\frac{\sum_{i}k_{i}}{\sum_{i}(k_{i}-1)} = \frac{\mu_k}{\mu_k - 1}$$

But $T \leq 1$, so epidemics cannot occur.
Transmissibility must fall off slower than inversely with degree in at least part of their range to have epidemics.

### Bipartite graph (STD example)

- $M$ men, $N$ women
- Men have $j$ connections with women, from distribution $p_j$
    - $p_j \sim j^a$
- Men have $k$ connections with women, from distribution $q_k \sim k^b$
- exponents fall in range 3.1-3.3

Generating functions:

$$f_0 (x) = \sum_j p_j x^j$$

$$f_1 (x) = \frac{f_0^\prime(x)}{\mu_j}$$

$$g_0 (x) = \sum_k q_k x^k$$

$$g_1 (x) = \frac{g_0^\prime(x)}{\mu_k}$$

It must be that 
$$\frac{\mu_j}{M} = \frac{\mu_k}{N}$$

(Why not $$\mu_j M = \mu_kN$$)?

Then define


$$f_0 (x;T) = f_0(1-(1-x)T)$$

$$f_1 (x;T) = f_1(1-(1-x)T)$$

$$g_0 (x;T) = g_0(1-(1-x)T)$$

$$g_1 (x;T) = g_1(1-(1-x)T)$$

Outbreak starts at male, goes to some number of females, then back to some number of males. Distribution of second gen number of males infected is

$$F_0(x;T_{mf},T_{fm})=f_0(g_1(x;T_{fm}) \ ;\ T_{mf})$$

If disease arrives along random vertex to male

$$F_1(x;T_{mf},T_{fm})=f_1(g_1(x;T_{fm}) \ ;\ T_{mf})$$

Likewise could define

$$G_0(x;T_{mf},T_{fm})=g_0(f_1(x;T_{mf}) \ ;\ T_{fm})$$

$$G_1(x;T_{mf},T_{fm})=g_1(f_1(x;T_{mf}) \ ;\ T_{fm})$$


Define Hs for male clusters

$$H_1(x;T_{mf},T_{fm}) = x F_1(\ H_1(x;T_{mf},T_{fm})\ ;T_{mf},T_{fm}) \tag{17}$$

$$H_0(x;T_{mf},T_{fm}) = x F_0(\ H_1(x;T_{mf},T_{fm})\ ;T_{mf},T_{fm})$$

Average small outbreak size:

$$\mu_s = \frac{T\mu}{1-T\mu_e}$$

$$\mu_s = \frac{F_0^\prime (1;T_{mf},T_{fm})}{1-F'_1(x;T_{mf},T_{fm})}$$

$$\mu_s = \frac{T_{mf}T_{fm}\ \mu_j \mu_{ke}\ }{1-T_{mf}T_{fm}\ \mu_{je} \mu_{ke}\ }$$

Essentially, in the bipartite graph, look at only 1 partition, and treat the two as if they are connected if they share a partner in the other partition.

Epidemic transition happens when 
$$T_{mf}T_{fm}\ \mu_{je} \mu_{ke} 
=T_{mf}T_{fm} \frac{\mu_j}{\sum_j p_j j (j-1)} \frac{\mu_k}{\sum_k p_k k (k-1)}
=1$$

Critical threshold same when looking at either partition. But average outbreak size is not.

#### threshold with power law

Algebra algebra. 
Set $a=b$ for power law degree distribution in the biparitie example.

Then if $a < 3$, then $T_c^2 = 0$
So unless if is impossible to transmit disease from one sex to the other, epidemic is always possible.

With high enough $a$, epidemic only possible with garunteed transmission.

Strangely, measured distribution for Britain seems to fall right in the transition zone where epidemics are possible but not garunteed.
Don't take too seriously, though.





