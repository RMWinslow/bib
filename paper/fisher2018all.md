---
parent: Papers
---

# All models are wrong but many are useful: Variable importance for black-box, proprietary, or misspecified prediction models, using model class reliance

[arxiv link](https://arxiv.org/abs/1801.01489)

## BibTeX
```
@article{fisher2018all,
  title={All models are wrong but many are useful: Variable importance for black-box, proprietary, or misspecified prediction models, using model class reliance},
  author={Fisher, Aaron and Rudin, Cynthia and Dominici, Francesca},
  journal={arXiv preprint arXiv:1801.01489},
  volume={480},
  year={2018}
}
```

## Abstract

> Variable importance (VI) tools describe how much covariates contribute to a prediction model's accuracy. However, important variables for one well-performing model (for example, a linear model f(x)=xTβ with a fixed coefficient vector β) may be unimportant for another model. In this paper, we propose model class reliance (MCR) as the range of VI values across all well-performing model in a prespecified class. Thus, MCR gives a more comprehensive description of importance by accounting for the fact that many prediction models, possibly of different parametric forms, may fit the data well. In the process of deriving MCR, we show several informative results for permutation-based VI estimates, based on the VI measures used in Random Forests. Specifically, we derive connections between permutation importance estimates for a single prediction model, U-statistics, conditional variable importance, conditional causal effects, and linear model coefficients. We then give probabilistic bounds for MCR, using a novel, generalizable technique. We apply MCR to a public data set of Broward County criminal records to study the reliance of recidivism prediction models on sex and race. In this application, MCR can be used to help inform VI for unknown, proprietary models.




## Notes and Excerpts

Christoph Molnar cites this paper in [his article on Permutation importance.](https://christophm.github.io/interpretable-ml-book/feature-importance.html)

[fisher2018model](fisher2018model) covers similar ground.

This paper builds builds on the permutation importance originally described in [breiman2001random](breiman2001random).

Here, they describe a sort of abstract generalization of permutation importance that can establish bounds on
how important a feature *can* be in a well-formed model (rather than how important it is in a particular model.) 
And they also give an example of estimating bounds for how important certain features are in a black box model.
Lots of interesting stuff, much of which is going over my head. 
I'll need to revisit this paper again some time.


---

> in Random Forests, VI is measured by
the decrease in prediction accuracy when a covariate is permuted (Breiman, 2001; Breiman
et al., 2001; see also Strobl et al., 2008; Altmann et al., 2010; Zhu et al., 2015; Gregorutti
et al., 2015; Datta et al., 2016; Gregorutti et al., 2017). A similar “Perturb” VI measure has
been used for neural networks, where noise is added to covariates (Recknagel et al., 1997;
Yao et al., 1998; Scardi and Harding, 1999; Gevrey et al., 2003). Such tools can be useful
for identifying covariates that must be measured with high precision, for improving the
transparency of a “black box” prediction model (see also Rudin, 2019), or for determining
what scenarios may cause the model to fail


> Several common approaches for variable selection, or for describing relationships between
variables, do not necessarily capture a variable’s importance. Null hypothesis testing methods may identify a relationship, but do not describe the relationship’s strength. Similarly,
checking whether a variable is included by a sparse model-fitting algorithm, such as the
Lasso (Hastie et al., 2009), does not describe the extent to which the variable is relied on.
Partial dependence plots (Breiman et al., 2001; Hastie et al., 2009) can be difficult to interpret if multiple variables are of interest, or if the prediction model contains interaction
effects



