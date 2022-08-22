---
parent: Papers
---

# Network theory and SARS: predicting outbreak diversity

[ScienceDirect html link](https://www.sciencedirect.com/science/article/pii/S0022519304003510)

## BibTeX
```
@article{meyers2005network,
  title={Network theory and SARS: predicting outbreak diversity},
  author={Meyers, Lauren Ancel and Pourbohloul, Babak and Newman, Mark EJ and Skowronski, Danuta M and Brunham, Robert C},
  journal={Journal of theoretical biology},
  volume={232},
  number={1},
  pages={71--81},
  year={2005},
  publisher={Elsevier}
}
```

## Abstract

> Many infectious diseases spread through populations via the networks formed by physical contacts among individuals. The patterns of these contacts tend to be highly heterogeneous. Traditional “compartmental” modeling in epidemiology, however, assumes that population groups are fully mixed, that is, every individual has an equal chance of spreading the disease to every other. Applications of compartmental models to Severe Acute Respiratory Syndrome (SARS) resulted in estimates of the fundamental quantity called the basic reproductive number R0—the number of new cases of SARS resulting from a single initial case—above one, implying that, without public health intervention, most outbreaks should spark large-scale epidemics. Here we compare these predictions to the early epidemiology of SARS. We apply the methods of contact network epidemiology to illustrate that for a single value of , any two outbreaks, even in the same setting, may have very different epidemiological outcomes. We offer quantitative insight into the heterogeneity of SARS outbreaks worldwide, and illustrate the utility of this approach for assessing public health strategies.


## My Notes


- non-evolving social network
    - Each person is a node
    - connections along which disease can spread are edges
- transmissibility $T$
    - average chance that that an edge is open
    - average chance that an infected person will transmit to a given susceptible person whom they have contact with
    - cooresponds to rate of contact, likelihood of transmission per contact event, duration of infectious period, susceptibility level, all rolled into one.
    - epidemic threshold $T_c$ is the minimum transmissibility to turn outbreaks into epidemics
            
        $$T_c = \frac{\langle k \rangle}{\langle k^2 \rangle - \langle k \rangle}$$

    - $\langle k \rangle$ is mean degree of network. 
- $$R_0 = T(\langle k^2 \rangle / \langle k \rangle - 1)$$
    - $T_c$ cooresponds to $$R_0 = 1$$
- probability generating functions
    - $p_k$ is probability that a node has $k$ neighbors
    - pgf for number of neighbors: $$G_0(x) = \sum_k p_k x^k$$
    - pgf for number of edges - 1 (nunmber of edges other than the one we arrived on, "excess degree"): $$G_1(x) = \sum_k k p_k x^{k-1} / \sum_k k p_k$$
    - mean degree = $$\langle k \rangle = \sum_k k p_k$$
    - mean excess degree = $$\langle k_e \rangle = \frac{\sum_k k (k-1) p_k}{\sum_k k p_k} = \frac{\langle k^2 \rangle}{\langle k \rangle - 1}$$
- average size of outbreak $\langle s \rangle$
    - derive by nesting pgfs for new infections per vertex
    - find that $$\langle s \rangle = 1+ \frac{T \langle k \rangle}{1-T\langle k_e \rangle}$$
    - At epidemic threshold, mean outbreak size diverges.
- $u$ is edge weighted non-prevalence, the chance person at the end of a random edge does not have the disease
    - found implicitly by solving $$u = \frac{\sum_k k p_k (1-(1-u)T)^{k-1}}{\sum_k k p_k}$$
    - Newman finds $u$ using numerical root finding method.
- chance of epidemic $$S = 1 - \sum_k p_k (1-(1-u)T)^k$$
    - $S$ is also expected proportion of population that will be infected should an epidemic occur.
- probability $\varepsilon_k$ that patient zero with $k$ neighbors will start epidemic
    - $1-T$ is chance no transmission to specific neighbor
    - $Tu$ is chance that even with transmission, no epidemic. ???
    - $$\varepsilon_k = 1-(1-T+Tu)^k = 1 - (1-(1-u)T)^k$$
- probability outbreak of size $N$ will ignite epidemic is $$1-\prod_i (1-\varepsilon_{k_i})$$
    - $i$ is index of individuals in the initial outbreak
    - just 1 minus chance no individuals start epidemic
- probability individual with $k$ neighbors becomes infected during the epidemic is $v_k$
    - $$v_k = 1 - (1-(1-u)T)^k$$


---


### simulations

Then the paper does some simulations and compares them to the theory.

all three networks have the same $R_0$, and same critical threshold, but have different vulnerabilities to epidemics.

- Poisson network
    - implicit basis of standard SIR model
    - clasically predicts epidemic happens with chance $1-1/R_0$
    - homogenous vertices, so any two outbreaks are essentially the same
    - small outbreaks include a moderate number of individuals
    - distribution $$p_k = (\mu^k / k!) e^{-\mu}$$ with $\mu=19.6$
- Power law network
    - mostly low-contact individuals
    - a few superspreaders
    - epidemic happens when there is a large chance that the disease reaches a superspreader.
    - many outbreaks fail to do so.
    - small outbreaks usually die out after 1 or 2 cases
    - distribution where for $k > 0$, $$p_k = Ck^{-\alpha}e^{-k/\kappa}$$ with $\kappa=94.2$ and $\alpha=2$
- urban network
    - based on Vancouver households
    - assigns people to households, classrooms, hosptal wards
    - connections are formed in each place
    - nearly exponential tail for degree distribution for degrees greater than 10

$T=0.155$ matches up with $R_0=2.7$, good fit for pre-intervention SARS

Simulated SIR results match up very well with timeless analytical predictions, even for complicated urban network


### intervention

- contact intervention
- transmission intervention

- Either intervention has the same porportional effects for an individual???
    - reduce contacts to fraction $a$
        - initial risk $1-(1-(1-u)T)^k$ 
        - new risk $1-(1-(1-u)T)^{ak}$ 
    - reduce transmission rate to fraction $a$
        - initial risk $1-(1-(1-u)T)^k$ 
        - new risk $1-(1-(1-u)aT)^{k}$ 
    - This isn't true! I went and done checked!
    - Oh, it's only the same "to leading order"

In vancouver network, 
a typical non-working adult cuts risk by 33% when cutting contacts in half.
But health care worker cuts risk only by 17%

---

Contacts are fixed throughout epidemic.
Tells a story where intervention is implemented early and consistently.


TODO: Want to read but can't easily find Pourbohloul, B., Meyers, L. A., et al., In review. Halting the spread of respiratory infections: A quantitative comparison of prevention and control strategies.

<!--Does this only work on discrete numbers of connections. If I allow connections to be continuous, does that just completely break things down? I think it might.-->