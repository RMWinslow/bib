---
parent: Papers
---

# Scaling regression inputs by dividing by two standard deviations

[pdf link](https://onlinelibrary.wiley.com/doi/pdf/10.1002/sim.3107)

[unpublished pdf from author's website](http://www.stat.columbia.edu/~gelman/research/unpublished/standardizing.pdf)

## BibTeX
```
@article{gelman2008scaling,
  title={Scaling regression inputs by dividing by two standard deviations},
  author={Gelman, Andrew},
  journal={Statistics in medicine},
  volume={27},
  number={15},
  pages={2865--2873},
  year={2008},
  publisher={Wiley Online Library}
}
```

## Abstract

> Interpretation of regression coefficients is sensitive to the scale of the inputs. One method often used to place input variables on a common scale is to divide each numeric variable by its standard deviation. Here we propose dividing each numeric variable by two times its standard deviation, so that the generic comparison is with inputs equal to the mean ±1 standard deviation. The resulting coefficients are then directly comparable for untransformed binary predictors. We have implemented the procedure as a function in R. We illustrate the method with two simple analyses that are typical of applied modeling: a linear regression of data from the National Election Study and a multilevel logistic regression of data on the prevalence of rodents in New York City apartments. We recommend our rescaling as a default option—an improvement upon the usual approach of including variables in whatever way they are coded in the data file—so that the magnitudes of coefficients can be directly compared as a matter of routine statistical practice. 

