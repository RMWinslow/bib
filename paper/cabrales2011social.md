---
parent: Papers
---

# Social interactions and spillovers

[pdf from author's website](https://www.ucl.ac.uk/~uctpcab/research/synergies.pdf)

## BibTeX
```
@article{cabrales2011social,
  title={Social interactions and spillovers},
  author={Cabrales, Antonio and Calv{\'o}-Armengol, Antoni and Zenou, Yves},
  journal={Games and Economic Behavior},
  volume={72},
  number={2},
  pages={339--360},
  year={2011},
  publisher={Elsevier}
}
```

## Abstract

> The aim of this paper is to provide a tractable model where both socialization (or network
formation) and productive efforts can be analyzed simultaneously. This permits a full
fledged equilibrium/welfare analysis of network formation with endogenous productive
efforts and heterogeneous agents. We show that there exist two stable interior equilibria,
which we can Pareto rank. The socially efficient outcome lies between these two equilibria.
When the intrinsic returns to production and socialization increase, all equilibrium actions
decrease at the Pareto-superior equilibrium, while they increase at the Pareto-inferior
equilibrium. In both cases, the percentage change in socialization effort is higher (in
absolute value) than that of the productive effort.
 


## Notes and Excerpts

> Social interactions are sometimes called non-market interactions to emphasize the fact
that these interactions are not regulated by the price mechanism (see, in particular, Scheinkman, 2008). 

Example:

> Each parent exerts two types of costly effort: productive effort
with the child (i.e. doing homework with the child, doing sport activities together, driving him to different activities, and
so on) and socialization effort related to education (going to parental evenings, birthday parties, or any activity that involves
other parents). In this example, each parent does not directly decide with whom he interacts, but rather participates in
parental activities (parental evenings, birthday parties) which can eventually lead to social interactions with other parents.


### Model details

Connection formatation is reminiscent of what I do, in that parents choose overall level of socialization activity, 
and then intensity of connection to each other type is proportional to the level of activity each of those types chooses.
(Or was it quadratic in the model I used...)
Connection strength between i and j is

$$g_{ij} = \frac{s_i s_j}{\sum_j s_j}$$

Parents also choose a productive investment level $k_i$
and then their private returns are

$$b_i k_i - c \frac{k_i^2}{2}$$
$$benefit_i \cdot k_i - cost \cdot \frac{k_i^2}{2}$$

(Idiosyncratic benefits but shared costs.) 
There are a few simplifying assumptions here similar to what I do in my contagion paper.
I should play around with this utility function though.

The "synergistic" returns depend on your effort, the effort of each other type, and the connection strengths.
The following formula is chosen in part so that the cross-derivative wrt $k_i$
and $k_j$ is positive, representing complentarities.

$$a \cdot k_i \cdot \sum_{j\neq i} g_{ij} k_j  - \frac {s_i^2}{2}$$

Would it make sense to model the benefits of other kinds of social interaction in this way?
Is interacting with a popular person more "fun"? Maybe...
If we make the investment the same for each type, then the payoff from socializing becomes:

$$a \cdot \sum_{j\neq i} \frac{s_i s_j}{\sum_j s_j}  - \frac {s_i^2}{2} \\
= a \cdot s_i \cdot \frac{\sum_{j\neq i} s_j}{\sum_j s_j}  - \frac {s_i^2}{2} \\
= a \cdot s_i \cdot \frac{\sum_j s_j - s_i}{\sum_j s_j}  - \frac {s_i^2}{2} \\
= a \cdot s_i  -  (\frac{a}{\sum_j s_j}  + \frac{1}{2} ) s_i^2
$$

... not sure what I was trying to figure out there...

### Three equilibria

Anyways, there are three equilibria if we set up the game with a finite set of types and infinitely many of each type.
- the unstable equilibrium where nobody socializes
- two stable interior equilbria where everybody puts in effort of both types which is proportional to their private benefit parameter $benefit_i$
  - one with high levels of private and social effort
  - one with low levels of private and social effort for everyone

In particular, if there are an infinite equal population of each type $\tau$
(this is the limit when there are $m$ of each type as $m$ geos to infinity)
then each person wants to choose private and social effort levels $b_i k$
and $b_i s$ where k and s are positive solutions to 

$$s = a \frac{\sum_\tau b_\tau^2}{\sum_\tau b_\tau} k^2$$
$$\frac{1}{k} = c - a \frac{\sum_\tau b_\tau^2}{\sum_\tau b_\tau} s$$

That second one can be rearranged as follows,

$$s = \frac{c-1/k}{a\frac{\sum_\tau b_\tau^2}{\sum_\tau b_\tau}}$$

and [then here's a desmos graph for the case where there's only one type](https://www.desmos.com/calculator/bdv6cnxnrf). The intersections of the curve on the desmos graph correspond to the numbers given in Table 1 of the paper. 
The calculator also illustrates the statement from theorem one that if $ab$ is too high, then the interior equilibria won't exist.


### Odd equilibrium effects

If total effort $s_i +$
$k_i$ is bounded, then upper equilibirum might dissapear and an upper-corner equlibrium might appear.

They also claim because of positive externalities, 
the socially efficient outcome(s) lay between the two externalities.
But I'm having a bit of trouble wrapping my head around the interpretation there,
and [when I plug in the table 1 params into equation 16, there isn't a solution?](https://www.desmos.com/calculator/xswxvebetx)


Oddly, when types have very different values of $b_\tau$,
then an increase in one types private benefits from effort
can actually hurt the other type.
EG say $b_1 <$
$(\sqrt{2}-1)b_2$, 
then an increase in $b_1$ would actually **decrease** the low-equilibrium welfare of type 2.
Basically, when $b_1$ is really low, everyone mostly just interacts with type 2.
But then type 1 wants to put in more effort, so more neighbors are of type 1, 
which makes type 2 want to socialize less.








### Empirical Implications

> (i) Better educated parents exert more productive effort educating their kids than low-educated parents, i.e. ki and
bi are positively related (Proposition 3). This fact is well documented. For example, for England, using the National Child
Development Study, Patacchini and Zenou (2010) find that more educated parents put more effort in educating their children
than less educated parents. 

>  (ii) Better educated parents are more prone to socialize with other parents than low-educated parents, i.e. si and bi
are positively related (Proposition 3). There is also empirical evidence on this issue. Putnam (1995) documents that less
educated people are less engaged in the life of their communities, in particular, group membership.


There are obviously other explanations for these relationships, 
but they way they tie it to their model is cute.

They also claim the multiple equilibria phenomenon might be a hidden factor explaining divergent outcomes between neighborhoods with the same observables.

Finally: they make a prediction: parental education should affect socialization effort proportionally more than direct effort. 

--- 

I wonder if I could take ATUS and classify childcare tasks into these two kinds of effort.
Would I even be able to see most of the socialization effort tasks?

