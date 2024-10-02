---
parent: Papers
---

# InterpretML: A Unified Framework for Machine Learning Interpretability

[arxiv pdf](https://arxiv.org/pdf/1909.09223),
[github repo](https://github.com/interpretml/interpret)

## BibTeX
```
@article{nori2019interpretml,
  title={InterpretML: A Unified Framework for Machine Learning Interpretability},
  author={Nori, Harsha and Jenkins, Samuel and Koch, Paul and Caruana, Rich},
  journal={arXiv preprint arXiv:1909.09223},
  year={2019}
}
```

## Abstract

> InterpretML is an open-source Python package which exposes machine learning interpretability algorithms to practitioners and researchers. InterpretML exposes two types of
interpretability – glassbox, which are machine learning models designed for interpretability (ex: linear models, rule lists, generalized additive models), and blackbox explainability
techniques for explaining existing systems (ex: Partial Dependence, LIME). The package
enables practitioners to easily compare interpretability algorithms by exposing multiple
methods under a unified API, and by having a built-in, extensible visualization platform.
InterpretML also includes the first implementation of the Explainable Boosting Machine, a
powerful, interpretable, glassbox model that can be as accurate as many blackbox models.
The MIT licensed source code can be downloaded from github.com/microsoft/interpret.


## Notes and Excerpts


The package is an API for multiple ML interpretability dinguses.

Then it also introduces a new algorithm: Explainable Boosting Machine.
It's a generalized additive model, which means that in a certain sense, we're adding up a bunch of functions based on one variable each. 
(But it's also set up so it can do pairwise interactions by training functions on pairs of features as well.)
Meant to handle a lot of the modern ML stuff behind the scenes for you when it's learning the function for each input.

> EBM is a fast implementation of the GA2M algorithm (Lou et al., 2013) [...] The algorithmic details for the training procedure, selection
of pairwise interaction terms, and case studies can be found in (Lou et al., 2012, 2013;
Caruana et al., 2015)

See [lou2013accurate](lou2013accurate) and [lou2012intelligible](lou2012intelligible)

