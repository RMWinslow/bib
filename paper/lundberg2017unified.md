---
parent: Papers
---

# A unified approach to interpreting model predictions

[arxiv link](https://arxiv.org/abs/1705.07874)

[NeurIPS link](https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html)
(Cool website, btw. With integrated links to paper, reviewer comments, etc.)

[github repo](https://github.com/shap/shap)


## BibTeX
```
@article{lundberg2017unified,
  title={A unified approach to interpreting model predictions},
  author={Lundberg, Scott M and Lee, Su-In},
  journal={Advances in neural information processing systems},
  volume={30},
  year={2017}
}
```

## Abstract

> Understanding why a model makes a certain prediction can be as crucial as the prediction's accuracy in many applications. However, the highest accuracy for large modern datasets is often achieved by complex models that even experts struggle to interpret, such as ensemble or deep learning models, creating a tension between accuracy and interpretability. In response, various methods have recently been proposed to help users interpret the predictions of complex models, but it is often unclear how these methods are related and when one method is preferable over another. To address this problem, we present a unified framework for interpreting predictions, SHAP (SHapley Additive exPlanations). SHAP assigns each feature an importance value for a particular prediction. Its novel components include: (1) the identification of a new class of additive feature importance measures, and (2) theoretical results showing there is a unique solution in this class with a set of desirable properties. The new class unifies six existing methods, notable because several recent methods in the class lack the proposed desirable properties. Based on insights from this unification, we present new methods that show improved computational performance and/or better consistency with human intuition than previous approaches.


## Notes and Excerpts

> The best explanation of a simple model is the model itself; it perfectly represents itself and is easy to
understand. 

For more complex models, we have to simplify the model to get an explanation, 
but *that explanation is itself a simple model.*

They look at "additive feature attribution methods", 
where the explanation method is a linear function of binary variables.

Shapley Regression Values:
Retrain linear model on all feature subsets,
Do a weighted average of how much adding a feature affects things.
If $F$ is the set of all features, and $i$ is the set containing just a particular feature,
then shapley for that feature is 

$$
\sum_{S\subseteq F\backslash i}\frac{\left|S\right|!\,\left(\left|F\right|-\left|S\right|-1\right)!}{\left|F\right|!}\left[f_{S\cup i}(x_{S\cup i})-f_{S}(x_{S})\right]
$$

This, along with approximations of it, and along with methods like LIME, DeepLIFT, and LWRP are all examples of additive feature attribution models.

---

If you want an afam with a few nice properties (local accuracy is a bit twisty but missingness and consistency make sense), then the model you want for the coefficients of your simple explanation model are:

$$
\phi_{i}(f,x)=\sum_{z'\subseteq x'}\frac{\left|z'\right|!\,\left(\left|M\right|-\left|z'\right|-1\right)!}{\left|M\right|!}\left[f_{x}(z')-f_{x}(z'\backslash i)\right]
$$

$M$ is the number of simplified input features (the length of $z'$ I think?), $abs(z')$ is the number that are non-zero, $z'\subseteq x'$ is all the $z'$ vectors where the non-zero entries are a subset of the non-zero entires in $x'$. Bit confused about what $M$ here means.

----

Implementation details are described. 
computation is simplified if we assume feature independence and model linearity.

In a linear model with feature independence, 
get the feature importance $\phi_i$
by multiplying model coefficient by difference from mean.
Cf [friedman2008predictive](friedman2008predictive)








---


[lundberg2018consistent](lundberg2018consistent) has some neat tricks you can do with shap importances.
