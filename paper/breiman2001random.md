---
parent: Papers
---

# Random forests

[springer](https://link.springer.com/article/10.1023/A:1010933404324)

## BibTeX
```
@article{breiman2001random,
  title={Random forests},
  author={Breiman, Leo},
  journal={Machine learning},
  volume={45},
  pages={5--32},
  year={2001},
  publisher={Springer}
}
```

## Abstract

> Random forests are a combination of tree predictors such that each tree depends on the values of a random vector sampled independently and with the same distribution for all trees in the forest. The generalization error for forests converges a.s. to a limit as the number of trees in the forest becomes large. The generalization error of a forest of tree classifiers depends on the strength of the individual trees in the forest and the correlation between them. Using a random selection of features to split each node yields error rates that compare favorably to Adaboost (Y. Freund & R. Schapire, Machine Learning: Proceedings of the Thirteenth International conference, ***, 148–156), but are more robust with respect to noise. Internal estimates monitor error, strength, and correlation and these are used to show the response to increasing the number of features used in the splitting. Internal estimates are also used to measure variable importance. These ideas are also applicable to regression.


## Notes

This paper is usually cited as the originator of the idea of permutation importance.
See for example:
[this article by Christoph Molnar](https://christophm.github.io/interpretable-ml-book/feature-importance.html#fn43)
or [the sklearn documentation for permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html)

And the core of the idea *is* there, but not in the general form typically used.
Here, it's applicable specifically to a Random Forest model rather than being something model agnostic. 
For each tree in the ensemble, the variable m is permuted on the out of bag data, 
and then you look at the percent increase in misclassification rate.

Compare to the generic form in the links above, where you permute that variable in a held out validation or testing set.


