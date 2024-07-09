---
parent: Papers
---

# Permutation importance: a corrected feature importance measure

[html link](https://academic.oup.com/bioinformatics/article/26/10/1340/193348)

## BibTeX
```
@article{altmann2010permutation,
  title={Permutation importance: a corrected feature importance measure},
  author={Altmann, Andr{\'e} and Tolo{\c{s}}i, Laura and Sander, Oliver and Lengauer, Thomas},
  journal={Bioinformatics},
  volume={26},
  number={10},
  pages={1340--1347},
  year={2010},
  publisher={Oxford University Press}
}
```

## Abstract

> Motivation: In life sciences, interpretability of machine learning models is as important as their prediction accuracy. Linear models are probably the most frequently used methods for assessing feature relevance, despite their relative inflexibility. However, in the past years effective estimators of feature relevance have been derived for highly complex or non-parametric models such as support vector machines and RandomForest (RF) models. Recently, it has been observed that RF models are biased in such a way that categorical variables with a large number of categories are preferred.

> Results: In this work, we introduce a heuristic for normalizing feature importance measures that can correct the feature importance bias. The method is based on repeated permutations of the outcome vector for estimating the distribution of measured importance for each variable in a non-informative setting. The P-value of the observed importance provides a corrected measure of feature importance. We apply our method to simulated data and demonstrate that (i) non-informative predictors do not receive significant P-values, (ii) informative variables can successfully be recovered among non-informative variables and (iii) P-values computed with permutation importance (PIMP) are very helpful for deciding the significance of variables, and therefore improve model interpretability. Furthermore, PIMP was used to correct RF-based importance measures for two real-world case studies. We propose an improved RF model that uses the significant variables with respect to the PIMP measure and show that its prediction accuracy is superior to that of other existing models.


