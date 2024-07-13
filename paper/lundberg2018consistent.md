---
parent: Papers
---

# Consistent individualized feature attribution for tree ensembles

[arxiv link](https://arxiv.org/abs/1802.03888)

## BibTeX
```
@article{lundberg2018consistent,
  title={Consistent individualized feature attribution for tree ensembles},
  author={Lundberg, Scott M and Erion, Gabriel G and Lee, Su-In},
  journal={arXiv preprint arXiv:1802.03888},
  year={2018}
}
```

## Abstract

> Interpreting predictions from tree ensemble methods such as gradient boosting machines and random forests is important, yet feature attribution for trees is often heuristic and not individualized for each prediction. Here we show that popular feature attribution methods are inconsistent, meaning they can lower a feature's assigned importance when the true impact of that feature actually increases. This is a fundamental problem that casts doubt on any comparison between features. To address it we turn to recent applications of game theory and develop fast exact tree solutions for SHAP (SHapley Additive exPlanation) values, which are the unique consistent and locally accurate attribution values. We then extend SHAP values to interaction effects and define SHAP interaction values. We propose a rich visualization of individualized feature attributions that improves over classic attribution summaries and partial dependence plots, and a unique "supervised" clustering (clustering based on feature attributions). We demonstrate better agreement with human intuition through a user study, exponential improvements in run time, improved clustering performance, and better identification of influential features. An implementation of our algorithm has also been merged into XGBoost and LightGBM, see this [http URL](http://github.com/slundberg/shap) for details.






## Notes and Excerpts


The discuss how Shapley is ideal feature importance metric when true model is linear combination of binary characteristics. It's the only one that's local and consistent (goes up when importance goes up).
Permutation importance also looks good in their examples, but that isn't a local thing.
Haven't heard of any of the other metrics they say are inconsistent.

There are nice ways to use them to interpret interactions and do supervised clustering.
For clustering, you do individualized feature importances 
and then do clustering on the importances instead of on the original data. 
Example using census dat to predict whether people will make >50k a year?


> Jupyter notebooks to compute all results are available at [http://github.com/slundberg/shap/notebooks/tree_shap_paper](http://github.com/slundberg/shap/notebooks/tree_shap_paper)

Neat stuff.
Not much explanation of the actual metric though, and 
no mention of whether it handles correlated inputs gracefully.
See [lundberg2017unified](lundberg2017unified) for that.
