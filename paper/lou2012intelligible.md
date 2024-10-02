---
parent: Papers
---

# Intelligible models for classification and regression

[pdf link](https://dl.acm.org/doi/pdf/10.1145/2339530.2339556?casa_token=-4ZimIeLvQAAAAAA:UPxn4ffbR3gq1YJ3Im0KK4LmCtU3cwZljPnLlVfGVHY4mUnLN81t27CIZTQ0aSkVYpRrygPmw6hLEg)

## BibTeX
```
@inproceedings{lou2012intelligible,
  title={Intelligible models for classification and regression},
  author={Lou, Yin and Caruana, Rich and Gehrke, Johannes},
  booktitle={Proceedings of the 18th ACM SIGKDD international conference on Knowledge discovery and data mining},
  pages={150--158},
  year={2012}
}
```

## Abstract

> Complex models for regression and classification have high accuracy, but are unfortunately no longer interpretable by users. We
study the performance of generalized additive models (GAMs),
which combine single-feature models called shape functionsthrough
a linear function. Since the shape functions can be arbitrarily complex, GAMs are more accurate than simple linear models. But since
they do not contain any interactions between features, they can be
easily interpreted by users.
We present the first large-scale empirical comparison of existing
methods for learning GAMs. Our study includes existing spline and
tree-based methods for shape functions and penalized least squares,
gradient boosting, and backfitting for learning GAMs. We also
present a new method based on tree ensembles with an adaptive
number of leaves that consistently outperforms previous work. We
complement our experimental results with a bias-variance analysis that explains how different shape models influence the additive model. Our experiments show that shallow bagged trees with
gradient boosting distinguish itself as the best method on low- to
medium-dimensional dataset


## Notes and Excerpts


Generalized additive models are models of the form

$$g(y) = \sum f_i(x_i)$$

This includes basic linear and logistic models.
This paper plays around with more complex ways of choosing the $f_i$ functions

see also [lou2013accurate](lou2013accurate), which incorporates pairwise interactions
and which is in turn
implemented as python package in [nori2019interpretml](nori2019interpretml)


