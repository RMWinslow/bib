---
tags: []
parent: Papers
collections: []
$version: 46
$libraryID: 1
$itemKey: L5BHDBCG

---
# Accurate intelligible models with pairwise interactions

[pdf link](https://dl.acm.org/doi/pdf/10.1145/2487575.2487579?casa_token=Vxg_1m8v63gAAAAA:GRRs0289rhOSxCPGU1Qm-MUGSxyW2CEA3Cniv-pY73h-GRTsSFoFQfuWmUz60JeruN1EBCb-MEc-oQ)

## BibTeX

```
@inproceedings{lou2013accurate,
  title={Accurate intelligible models with pairwise interactions},
  author={Lou, Yin and Caruana, Rich and Gehrke, Johannes and Hooker, Giles},
  booktitle={Proceedings of the 19th ACM SIGKDD international conference on Knowledge discovery and data mining},
  pages={623--631},
  year={2013}
}
```

## Abstract

> Standard generalized additive models (GAMs) usually model the dependent variable as a sum of univariate models. Although previous studies have shown that standard GAMs can be interpreted by users, their accuracy is significantly less than more complex models that permit interactions. In this paper, we suggest adding selected terms of interacting pairs of features to standard GAMs. The resulting models, which we call GA2M-models, for Generalized Additive Models plus Interactions, consist of univariate terms and a small number of pairwise interaction terms. Since these models only include one- and two-dimensional components, the components of GA2M-models can be visualized and interpreted by users. To explore the huge (quadratic) number of pairs of features, we develop a novel, computationally efficient method called FAST for ranking all possible pairs of features as candidates for inclusion into the model. In a large-scale empirical study, we show the effectiveness of FAST in ranking candidate pairs of features. In addition, we show the surprising result that GA2M-models have almost the same performance as the best full-complexity models on a number of real datasets. Thus this paper postulates that for many problems, GA2M-models can yield models that are both intelligible and accurate.

## Notes and Excerpts

This is a test.

$$
g(E[y]) = \sum f_i(x_i) + \sum f_{ij}(x_i,x_j)
$$

General additive models are easy to interpret but not as good as more complex models. But pairwise interactions can still be visualized as heatmaps, and in some of the data they test, pairwise interactions can capture most of the signal of more complex models.

Other ways of detecting interactions include ANOVA, partial dependence functions, GUIDE (which splits data into quadrants based on medians). I think their FAST is similar in some ways but does a serach for the best cuts instead of using the medians, and greedily selects pairs one at a time by looking at the residuals.

Then followed by implementation details for efficient space usage and compute.

One weakness is that if two variables are highly correlated, then we might falsely pick up an interaction involving a proxy and then fail to pick up any interaction with the true variable after that.

implemented as python package in [nori2019interpretml](nori2019interpretml)
