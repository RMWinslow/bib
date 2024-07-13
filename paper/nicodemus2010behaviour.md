---
parent: Papers
---

# The behaviour of random forest permutation-based variable importance measures under predictor correlation

[Springer Link](https://link.springer.com/article/10.1186/1471-2105-11-110)


## BibTeX
```
@article{nicodemus2010behaviour,
  title={The behaviour of random forest permutation-based variable importance measures under predictor correlation},
  author={Nicodemus, Kristin K and Malley, James D and Strobl, Carolin and Ziegler, Andreas},
  journal={BMC bioinformatics},
  volume={11},
  pages={1--13},
  year={2010},
  publisher={Springer}
}
```

## Abstract

> **Background**
Random forests (RF) have been increasingly used in applications such as genome-wide association and microarray studies where predictor correlation is frequently observed. Recent works on permutation-based variable importance measures (VIMs) used in RF have come to apparently contradictory conclusions. We present an extended simulation study to synthesize results.
> 
> **Results**
In the case when both predictor correlation was present and predictors were associated with the outcome (HA), the unconditional RF VIM attributed a higher share of importance to correlated predictors, while under the null hypothesis that no predictors are associated with the outcome (H0) the unconditional RF VIM was unbiased. Conditional VIMs showed a decrease in VIM values for correlated predictors versus the unconditional VIMs under HA and was unbiased under H0. Scaled VIMs were clearly biased under HA and H0.
> 
> **Conclusions**
Unconditional unscaled VIMs are a computationally tractable choice for large datasets and are unbiased under the null hypothesis. Whether the observed increased VIMs for correlated predictors may be considered a "bias" - because they do not directly reflect the coefficients in the generating model - or if it is a beneficial attribute of these VIMs is dependent on the application. For example, in genetic association studies, where correlation between markers may help to localize the functionally relevant variant, the increased importance of correlated predictors may be an advantage. On the other hand, we show examples where this increased importance may result in spurious signals.




## Notes and Excerpts


<!--
In short, some papers (like the Strobl et al talked about in [hooker2021unrestricted](hooker2021unrestricted)
say that Permutation importance causes problems with correlated predictors.
But NIcodemus and Malley say the permutation-based variable importance measures are unbiased, while the GINI measures are biased.

Also

> Meng et al. [5] suggest a revised tree-building algorithm and VIM that suppress the inclusion of
correlated predictors in the same tree.
-->

Somewhat reminiscent of  [hooker2021unrestricted](hooker2021unrestricted),
they set up a simulation where there is an unimportant variable correlated with important variables.
And the random forests articficially boost the importance of that variable.

> Tree-building uses predictors sequentially in each
tree and single predictors that are strongly correlated
with the outcome are more likely to be selected at the
first split. Statistically speaking, in the first split of each
tree the split criterion is a measure of the bivariate effect
of each predictor on the response, or of the marginal
correlation between that predictor and the response. In
the case of predictors that are strongly correlated with
influential predictors, this univariate or marginal effect
is almost as strong as that of the originally influential
predictor.

