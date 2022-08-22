---
parent: Papers
---

# Population uncertainty and Poisson games

[Spring link](https://link.springer.com/article/10.1007/s001820050079)

[pdf link](https://link.springer.com/content/pdf/10.1007/s001820050079.pdf)

## BibTeX
```
@article{myerson1998population,
  title={Population uncertainty and Poisson games},
  author={Myerson, Roger B},
  journal={International Journal of Game Theory},
  volume={27},
  number={3},
  pages={375--392},
  year={1998},
  publisher={Springer}
}
```

## Abstract

> A general class of models is developed for analyzing games with population uncertainty. Within this general class, a special class of Poisson games is defined. It is shown that Poisson games are uniquely characterized by properties of independent actions and environmental equivalence. The general definition of equilibrium for games with population uncertainty is formulated, and it is shown that the equilibria of Poisson games are invariant under payoff-irrelevant type splitting. An example of a large voting game is discussed, to illustrate the advantages of using a Poisson game model for large games.



## My Notes


In a game with a specific number of players, we are implicitly saying that it is common knowledge that each player knows the identity of every other.
We are saying that it is common knowledge that the distribution of population is a point prob.
Sometimes easier to assume it's a Poisson Probability.


### Setup

- $T$ is set of possible types of players
- Q represnets poulation uncertainty.
- C is set of actions a player can choose.
- $U(x,b,t)$ is utility of player of type $t$ who chooses action $b$ when there are $x(c)$ players who choose each action $c$
- strategy $\sigma(c|t)$ representing the prob that a player of type $t$ chooses action $c$
  

### Poisson games specifically

Player Types are IID

Number of players  is Poisson RV with mean $n$
which means chance of exactly $k$ players is 

$$p(k|n) = \frac{e^{-n}n^k}{k!}$$

#### Useful Property of Poisson!

Aggregation Property
: Any sum of independent Poisson RV is itself a Poisson RV.

If $X_i \sim Pois(\lambda_i)$, and the $X_i$s are iid. then

$$\sum_i X_i \sim Pois\left(\sum_i \lambda_i\right)$$

$$\frac{e^{-\lambda+v}(\lambda+v)^k}{k!} = \sum_{j=0}^k \frac{}{j!} \frac{}{(k-j)!}$$

Decomposition Property
: If the sum of two independent RV is Poisson, then so too are each of those two variables

Furthermore, if we independently assign each individual some characteristc from set $S$, and then the RV representing the number of each type
is itself Poisson, mutually independent of all the other ones.


the implication of all this is that if we randomly assign types, then for each type, the distribution of number of that type is poisson

