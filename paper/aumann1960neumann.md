---
parent: Papers
---

# Von Neumann-Morgenstern solutions to cooperative games without side payments

PUT A LINK TO THE PAPER HERE

## BibTeX
```
@article{aumann1960neumann,
  title={Von Neumann-Morgenstern solutions to cooperative games without side payments},
  author={Aumann, Robert J and Peleg, Bezalel},
  journal={Bulletin of the American Mathematical Society},
  volume={66},
  number={3},
  pages={173--179},
  year={1960},
  publisher={American Mathematical Society}
}
```

## Excerpt from Intro

> The use of side payments in the classical1 theory of n-person games involves three restrictive assumptions. First, there must be a common medium of exchange (such as money) in which the side payments may be effected; next, the side payments must be physically and legally feasible; and finally, it is assumed that utility is "unrestrictedly transferable," i.e. that each player's utility for money is a linear function of the amount of money.3 These assumptions severely limit the applicability of the classical theory; in particular, the last assumption has been characterized by Luce and Raiffa as being "exceedingly restrictive—for many purposes it renders n-person theory next to useless." It is the purpose of this paper to present the outline of a theory that parallels the classical theory, but makes no use of side payments.



## My Notes

This paper was recommended to me as an example of "good writing". Here are some notes I jotted down.

### First Page

In VNM's treatment of n-person games with side payments, VNM requires that:

- there be a common medium of exchange
- the side payments must be physically and legally feasible
- utility is "unrestrictedly transferable," 
i.e. that each player's utility for money
is a linear function of the amount of money

The paper tries to take a different approach to avoid the avoid the use of these restrictive side payments.

In fact, here's the entire first page quoted:

> The use of side payments in the classical 1 theory of ^-person games
involves three restrictive assumptions. First, there must be a com-
mon medium of exchange (such as money) in which the side payments
may be effected; next, the side payments must be physically and
legally feasible; and finally, it is assumed that utility is "unre-
strictedly transferable," i.e. that each player's utility for money 2 is a
linear function of the amount of money. 3 These assumptions severely
limit the applicability of the classical theory; in particular, the last
assumption has been characterized by Luce and Raiffa [2, p. 233]
as being "exceedingly restrictive—for many purposes it renders n-
person theory next to useless." It is the purpose of this paper to pre-
sent the outline of a theory that parallels the classical theory, but
makes no use of side payments.* Our definitions are related to those
given in [2, p. 234] and in [3], but whereas the previous work went
no further than proposing definitions, the theory outlined here con-
tains results which generalize a considerable portion of the classical
theory. It thus demonstrates that the restrictive side payment as-
sumption is not necessary for the development of a theory based on
the ideas of von Neumann and Morgenstern. Only a general descrip-
tion of the theory and statements of the more important theorems will
be included here; details and proofs will be published elsewhere.

Here's what it accomplishes:

- It states a fact about existing literature in a clear and concise way.
- It quotes somebody else saying that this is a problem. (Shows that there's agreement about the need for a fix)
- States the paper it's building on top of.
- Says what's new in this paper.
- Describes what the paper contains.

All on just one page.



### The meat of the paper

#### Definitions of effectiveness

&alpha;-effective
: A coalition B is said to be a-effective for the payoff vector x if there
is a strategy* for B, such that for each strategy used by N—B, each mem-
ber i of B receives at least $x_i$.
(aka maximin)

&beta;-effective
: A coalition B is said to be &beta;-effective for the payoff vector x, if
for each strategy used by N—B, there is a strategy for B such that each
member i of B receives at least $X_i$.
(aka minimax)



#### axiomatic treatment
An n-person "characteristic function" is a set N with n members together with a function v that carreis each subset B of N insto a subset v(B) of $E^N$ so that 

$$
\begin{gather}
    v(B) \text{ is convex} \\
    v(B) \text{ is closed} \\
    v(\varnothing) = E^N \\
    x \in v(B), y \in E^N, y_i \leq x_i \forall i \in B \implies y\in v(B) \\
    B_1, B_2 disjoint \implies v( B_1 \cup B_2 ) \supset v(B_1) \cap v(B_2) \\
\end{gather}
$$

An n-person "game" is an n-person characteristic function (N, v)
together with a convex compact polyhedral subset H of v(N).

This is an axiomatic way of defining games in terms of the effective payoffs of various possible coalitions. 

> In order to justify these definitions, it is necessary to show that an
arbitrary finite game, when combined with the concept either of
$\alpha$-effectiveness or of $\beta$-effectiveness, satisfies our definition of a
game. For the most part this is straightforward; the only deep part
occurs in verifying condition (5) in the case of $\beta$-effectiveness, where
use is made of Kakutani's fixed point theorem.

> Condition (5) is not needed for any of the results stated in this paper. It was
included in order to underscore the parallelism with the classical theory, and with
the hope that stronger axioms will eventually yield a richer theory.


#### Additional Definitions and Solutions

Domination
: A payoff vector x is said to *dominate* a payoff vector *y via B* if $x\in v{B)$
and $x_i > y_i$ for all $i\in B$; x is said to *dominate* y if there is a B such
that x dominates y via B.

dom K
: If K is an arbitrary set of payoff vectors,
we define dom K to be the set of all payoff vectors dominated by at
least one member of K. 

P-stable 
: If P is an arbitrary set of payoff vectors,
then a subset K of P is said to be *P-stable* if $K\cap dom K$ is empty and
$K \cup dom K \supset P$ .

P-core
: The set P — dom P is called the P-core.

With these definitions, standard proofs go through essentially unchanged.

Individually rational
: A payoff vector x is called individually rational 
if $ x \geq \sup ( v(\{ i \} )_i $
for each $i \in N$.

Group Rationality
: x is called group
rational if there is no $y\in H$ such that $y_i > X_i$ for each $i \in V$.

(The original paper has definitions clumped together in paragraphs. I'd prefer them to be seperated like the above.)

It can be proved that if $\bar{A}$ is that set of individually rational members of H, 
and if  A is the set of members of $\bar{A}$ that are also group rational,
then a subset of H is A-stable iff it is $\bar{A}$ stable.

Then a *solution* of the game is defined to be an A-stable set.

#### Solutions

> all 2-person
games have a unique solution, 12 namely all of A. 

> Therorem 1: Every 3-person zero-sum game is solvable.

> Incidentally, Theorem 1 is the only one of our results for which
the assumption that the v(B) be convex (condition (1)) is required.

#### etc

Unlike in the "classical VNM, 
the composition of two games has solutions which are precisely the composition of the solutions of each of the two games

Notes are also made about supergames and extended games



### Final thoughts

This paper was a brief summary of a new theoretical framework.
Solves some problems from the old framework. 
Paper is concise in describing the defintions and consequences. And in describing how things change.

