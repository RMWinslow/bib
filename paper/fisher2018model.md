---
parent: Papers
---

# Model class reliance: Variable importance measures for any machine learning model class, from the “Rashomon” perspective

[arxiv pdf link](https://arxiv.org/pdf/1801.01489v1)

## BibTeX
```
@article{fisher2018model,
  title={Model class reliance: Variable importance measures for any machine learning model class, from the “Rashomon” perspective},
  author={Fisher, Aaron and Rudin, Cynthia and Dominici, Francesca},
  journal={arXiv preprint arXiv:1801.01489},
  volume={68},
  pages={331--346},
  year={2018}
}
```

## Abstract

> There are serious drawbacks to many current variable importance (VI) methods, in that they tend to not
be comparable across model types, can obscure implicit assumptions about the data generating distribution,
or can give seemingly incoherent results when multiple prediction models fit the data well. In this paper
we propose a framework of VI measures for describing how much any model class (e.g. all linear models of
dimension p), any model-fitting algorithm (e.g. Ridge regression with fixed regularization parameter), or any
individual prediction model (e.g. a single linear model with fixed coefficient vector), relies on covariate(s) of
interest. The building block of our approach, Model Reliance (MR), compares a prediction model’s expected
loss with that model’s expected loss on a pair observations in which the value of the covariate of interest has
been switched. Expanding on MR, we propose Model Class Reliance (MCR) as the upper and lower bounds on
the degree to which any well-performing prediction model within a class may rely on a variable of interest, or
set of variables of interest. Thus, MCR describes reliance on a variable while accounting for the fact that many
prediction models, possibly of different parametric forms, may fit the data well. We give probabilistic bounds
for MR and MCR, leveraging existing results for U-statistics. We also illustrate connections between MR,
conditional causal effects, and linear regression coefficients. We outline implementations of our approaches
for regularized linear regression, and to regression in a reproducing kernel Hilbert space. We then apply MR
& MCR to study the behavior of recidivism prediction models, using a public dataset of Broward County
criminal records





