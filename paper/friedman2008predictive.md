---
parent: Papers
---

# Predictive learning via rule ensembles

[Project Euclid link](https://projecteuclid.org/journals/annals-of-applied-statistics/volume-2/issue-3/Predictive-learning-via-rule-ensembles/10.1214/07-AOAS148.full)

## BibTeX
```
@article{friedman2008predictive,
  title={Predictive learning via rule ensembles},
  author={Friedman, Jerome H and Popescu, Bogdan E},
  year={2008}
}
```

## Abstract

> General regression and classification models are constructed as linear combinations of simple rules derived from the data. Each rule consists of a conjunction of a small number of simple statements concerning the values of individual input variables. These rule ensembles are shown to produce predictive accuracy comparable to the best methods. However, their principal advantage lies in interpretation. Because of its simple form, each rule is easy to understand, as is its influence on individual predictions, selected subsets of predictions, or globally over the entire space of joint input variable values. Similarly, the degree of relevance of the respective input variables can be assessed globally, locally in different regions of the input space, or at individual prediction points. Techniques are presented for automatically identifying those variables that are involved in interactions with other variables, the strength and degree of those interactions, as well as the identities of the other variables with which they interact. Graphical representations are used to visualize both main and interaction effects.


## Notes and Excerpts

Overview of ensemble methods.



In general, ensembles are linear combinations of base learners.

The "importance sampled learning ensemble"
(ISLE) methodology from Friedman and Popescu (2003) is as follows. 
Given a set of base learners $\{f_m(x)\}$, the weights $\{a_m\}$ are 
determined by a linear regression:

$$
\arg\min_{\left\{ a_{m}\right\} }\,\sum_{i}L\left(y_{i},\,a_{0}+\sum_{m}a_{m}f_{m}(X_{i})\right)+\lambda\sum_{m}\left|a_{m}\right|
$$

where $L$ is sum loss function. So this is basically just Lasso on the base learners. 

The base learners are generated in Friedman and Popescu (2003) using a "perturbation sampling technique", which is exactly what you'd expect.
There's also another shrinkage hyperparam $\nu$ which determines how much the construction of the ase learner depends on the previous ones.

> Although, in principle, most of these procedures can be used with other base
learners, they have almost exclusively been applied with decision trees



---


Rule Based Ensembles have 
simple simple binary rules
as the base learners.
Could in theory do a combinatoric approach.
But that's slow.
In practice, you interpret decision trees as
collections of rules.

A "rulefit" learner generates a tree ensemble the same way ISLE does, but then extracts the rules from the tree and uses those in a rule based ensemble.  On the simulated data in this paper, rulefit does better than the other tree ensembles tried. 


Though caution: Here's a note from [Christoph Molnar](https://christophm.github.io/interpretable-ml-book/rulefit.html):

> An anecdotal drawback: The papers claim a good performance of RuleFit – often close to the predictive performance of random forests! – but in the few cases where I tried it personally, the performance was disappointing. Just try it out for your problem and see how it performs.

Also from that link: [R](https://cran.r-project.org/web/packages/pre/index.html) and [Python](https://github.com/christophM/rulefit) implementations.



----

Also discussed is mixing rules in with linear numeric inputs. 
After all, there's nothing saying the base learners need to be the same structure.


I think they're basically describing doing a regularized linear model with a bunch of constructed rules-based features.
That's basically what I did for the MEBDI competition, but on an ad-hoc basis. 
Theirs is more formalized. 


They Winsorize each linear term.
They also normalize each to give it 
the "same a priori influence as a typical rule":

$$
l_j(x_j) \leftarrow 0.4\frac{l_j(x_j)}{std(l_j(x_j) )}
$$

Compare 0.4 factor to [gelman2008scaling](gelman2008scaling). Here they say 0.4 is the average standard deviation of rules with a uniform support distribution $sk ∼ U (0, 1)$.[^scalingnote]

[^scalingnote]: A binary variable with prevalence $p$ has variance $p\cdot(1-p)$, and if you integrate standard deviation over a uniform distribution of prevalences, you get 
$$\int_0^1\sqrt{p(1-p)}\ dp = \frac{\pi}{8} \approx 0.39270 \approx 0.4$$
I've read lots of discussion online about how to handle a mix of numeric and binary variables, but I've never seen the tip to scale by a factor of 0.4, which seems pretty intuitive. I've only seen one reference to the Gelman advice to scale by 0.5, and more common practice is to scale *up* the binary variables.






----


Importance measures based on de-standarized coeeficient values in the ensemble can then be used as a measure of global feature importance:

For rules: 

$$I_k = \left|a_k\right|\cdot \sqrt{s_k(1-s_k)}$$

For linear predictors:

$$I_j = \left|a_j\right|\cdot std(l_j(x_j)$$

Local measures of influence for each observation can be found by multiplying abs of $a$ by abs of difference from mean for each input.


Important input features are those which appear in important rules. Add importance of linear predictors + importance of each rule which includes that feature, divided by number of features in that rule.


---

There is some additional information about interaction effects I'd like to come back to read later.




