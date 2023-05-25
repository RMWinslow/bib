---
parent: Papers
---

# Machine learning methods that economists should know about

[html link](https://www.annualreviews.org/doi/full/10.1146/annurev-economics-080217-053433)

## BibTeX
```
@article{athey2019machine,
  title={Machine learning methods that economists should know about},
  author={Athey, Susan and Imbens, Guido W},
  journal={Annual Review of Economics},
  volume={11},
  pages={685--725},
  year={2019},
  publisher={Annual Reviews}
}
```

## Abstract

> We discuss the relevance of the recent machine learning (ML) literature for economics and econometrics. First we discuss the differences in goals, methods, and settings between the ML literature and the traditional econometrics and statistics literatures. Then we discuss some specific methods from the ML literature that we view as important for empirical researchers in economics. These include supervised learning methods for regression and classification, unsupervised learning methods, and matrix completion methods. Finally, we highlight newly developed methods at the intersection of ML and econometrics that typically perform better than either off-the-shelf ML or more traditional econometric methods when applied to particular classes of problems, including causal inference for average treatment effects, optimal policy estimation, and estimation of the counterfactual effect of price changes in consumer choice models.

## Notes and Excerpts


### Terminology Differences

| ML | Stats | 
|:--|:--|
| training sample | sample used to estimate parameters |
| training | estimation |
| features | regressors, covariates, or predictors |
| weights | regression parameters |
| bias | parameter for a constant term |
|  |  |

---

little focus on validating a model in econometric setting



---

### Supervised Learning for Regression

- ensembles
- Regularized Linear Regressions - LASSO, Ridge, etc.
    - LASSO vs best subset selection 
- Regression trees and random forests
    - Each leaf provides a sample average. To get unbiased estimate, split data before training and apply tree-partition to the non-training set.
    - comparison to kernel regressions
    - Fit forest and then apply GMM to each test point, with higher weights placed on points which share leaves with the test point. 
- Neural Networks
    - Convolutional Network: Instead of having all the nodes from a previous layer feed into a node, choose a subset (eg nearby pixels).
- Boosting: Apply very simple models, with each successive model being trained on the residual.


---

### Supervised Learning for Classification

- Classification Trees and Forests: Like the regression version, except objective for splits is based on an "impurity function"
- Support Vector Machine
    - If possible, find a separating hyperplane with lots of wiggle room.
    - If no such separating hyperplane will do, you can allow for some wiggle room.
    - Comparison to logistic regression. You end up with a linear estimator which is less affected by points far from hyperplane.
    - A Kernel can be added which allows the "hyperplane" to implicitly contain transformations of the original features.


---

### Unsupervised Learning

- K Means Clustering
- Generative Adversarial Networks

---

### Inference with ML

- Average Treatment Effects τ:
    - estimate conditional outcome expections μ and/or "propensity score" $e$ (which involves account for covariates that predict treatment?)
    - Lasso/subset-selection isn't great for this. Features optimal for estimating μ not necessarily optimal for estimating τ
        - Omitting covariates highly correlated with treatment can bias estimate even if connection to outcome is weak.
        - "Belloni et al. (2014) propose using a covariate selection method that selects both covariates that are predictive of the outcome and covariates that are predictive of the treatment"
    - covariate balancing: choose weights that lead to same mean covariates in treatment and control groups.
    - "typically, economists prioritize precise estimates of causal effects above predictive power" (See eg IV. Goodness of fit drops, but it's worth it.) 
- "Influence function", "orthogonalization" "nuisance parameters"
    - sample splitting, cross-fitting, out-of-bag prediction, and leave-one-out estimation
- Conditional Average Treatment Effects
    - Athey & Imbens (2016) build "causal trees", optimizing splits to find treatment effect heterogeneity. Wager & Athey (2017) describe a "causal forest".
- "Optimal policy estimation"


---

### Multi-Armed Bandits

- Assigning fixed number of people to each treatment arm can be wasteful.
- Thompson sampling: assign each unit to treatment with probability equal to prob that that treatment is the optimal one.
- upper confidence bounds (UCBs): construct confidence interval for each treatment arm. Assign next unit to treatment with highest upper bound of confidence interval
- assignment treatment to units based on characteristics (if treatement effect heterogenous)


---

### "Matrix Completion and Recommender Systems"

Above techniques most sensible for cross-sectional data.
What about panel data?

- Netflix problem: winning solutions had model averaging, matrix factorization, nearest neighbors
- Matrix Completion. Low-rank factorizations
- econometrics approaches similar problems with
    - fixed effect methods
    - synthetic controls (missing values for only a single row of the matrix) = "vertical regression"
- "horizontal regression" in program evaluation literature: outcomes in last period are regressed on outcomes in earlier periods
- matrix completion tries to exploit stable patterns across time *and* between units
- augmenting demand estimation with matrix completion












