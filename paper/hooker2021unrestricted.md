---
parent: Papers
---

# Unrestricted permutation forces extrapolation: variable importance requires at least one more model, or there is no free variable importance

[Springer Link](https://link.springer.com/article/10.1007/s11222-021-10057-z)

## BibTeX
```
@article{hooker2021unrestricted,
  title={Unrestricted permutation forces extrapolation: variable importance requires at least one more model, or there is no free variable importance},
  author={Hooker, Giles and Mentch, Lucas and Zhou, Siyu},
  journal={Statistics and Computing},
  volume={31},
  pages={1--16},
  year={2021},
  publisher={Springer}
}
```

## Abstract

> This paper reviews and advocates against the use of permute-and-predict (PaP) methods for interpreting black box functions. Methods such as the variable importance measures proposed for random forests, partial dependence plots, and individual conditional expectation plots remain popular because they are both model-agnostic and depend only on the pre-trained model output, making them computationally efficient and widely available in software. However, numerous studies have found that these tools can produce diagnostics that are highly misleading, particularly when there is strong dependence among features. The purpose of our work here is to (i) review this growing body of literature, (ii) provide further demonstrations of these drawbacks along with a detailed explanation as to why they occur, and (iii) advocate for alternative measures that involve additional modeling. In particular, we describe how breaking dependencies between features in hold-out data places undue emphasis on sparse regions of the feature space by forcing the original model to extrapolate to regions where there is little to no data. We explore these effects across various model setups and find support for previous claims in the literature that PaP metrics can vastly over-emphasize correlated features in both variable importance measures and partial dependence plots. As an alternative, we discuss and recommend more direct approaches that involve measuring the change in model performance after muting the effects of the features under investigation.


## Notes and Excerpts


> many researchers have
suggested methods to “X-ray the black box” in order to provide insight into which input features are important and how
they effect predictions; a task so precarious that others have
advocated against the practice altogether (Rudin 2019).


>  Our message can be
simply summarized by
> > When features in the training set exhibit statistical dependence, permute-and-predict methods can be
highly misleading when applied to the original model.



Describes permutation based techniques:

- Variable Importance, as described in [breiman2001random](breiman2001random) and [fisher2018model](fisher2018model)
- PDP plots, as in [friedman2001greedy](friedman2001greedy) and refined as ICE plots.




> Strobl
et al. (2007) investigate classification and note that the importance measures based on permuted OOB error in CART
built trees are biased toward features that are correlated
with other features and/or have many categories and further
suggest that bootstrapping exaggerates these effects. Archer
and Kimes (2008) explore a similar setup and also note
improved performance when (true) signal features—those
actually related to the response—are uncorrelated with noise
features. Nicodemus et al. (2010) investigates these claims of
feature preference in a large-scale simulation study and again
find that the OOB measures overestimate the importance of
correlated predictors.

(Yeah, I can kind of feel this kind of thing.)

Two problems: 
Permutation Importance treats two correlated variables as being manipulable separately from each other.
That's inescapable. <!--See Strobl et al. (2007)-->
The second is related to extrapolation bias, since we'll see combinations of parameters that we don't see in data.

> As a concrete
example: an evaluation of the importance of pregnancy status
in a model that also includes gender would result in the evaluation of the response of pregnant men as often as pregnant
women.

They point out that in a linear model like the following:

$$
f(x) = \beta_0 + \sum_j \beta_j x_j
$$

If each $x_j$ has variance 1, its permutation importance is given by $\beta_j^2$, regardless of correlation among the features.
Hrm, this actually makes me feel *better* about permutation importance, oddly enough.

But they say in their experiments, if we treat estimation of the $\beta$s as our goal, 
this estimation is biased upwards for covariates correlated with each other.
This could lead to problems if you use PI for covariate selection.


----

How to deal with this?
One way is to create perturbed features conditionally on the other features. (Strobl does this).
The other method discussed and advocated for suggests re-learning models after dropping out features,
but... that just doesn't feel right to me. Will need to think about this more.

> Very recent work has demonstrated that even though it seems
quite unintuitive to think that a permuted feature could substantially improve predictive performance, such an outcome
is possible in low signal settings (Mentch and Zhou 2020).

Okay, they actually advocate for a *condition*-and-relearn approach.

Lots of cites for things like shapley values, even if they do cite them to critique them.

> For a linear model such as (2) with covariates that have
the same scale, variable importance can be obtained from
the magnitude of covariates; see Gregorutti et al. (2015)

In their simulations, they have true data generated by a linear function.
Then they say/show that for linear models PI relates to true coefficients,
but for random forests and nnets, they see considerable bias.

Okay, I think I *kind of* get what they're saying.
If you have two highly correlated variables:
permuting only 1 will, by construction, push us into an area of feature space not present in the sample.
Linear models break gracefully,
But in forest and nnets, the complicated interactions can result in garbage inputs.
(EG pregnant men)
That garbage results in unusually bad performance, 
which is misinterpreted by PI as each of those features being important.

---


Further discussion of alternatives at the end.
<!--Should take another look at the model class reliance thing in [fisher2018model](fisher2018model).-->


> Methods that avoid
re-learning the response can be based on conditional permutation or simulation, but in general that still requires a
model for xi j|xi,− j ; see Liu and Zheng (2018) for recent
developments. Alternative measures of importance include
generalizations of Sobol indices (Hooker 2007) and Shapley values (Owen 2014; Lundberg and Lee 2017),
although the calculation of these, if not undertaken carefully, can be
subject to the same extrapolation bias that we identify here.







