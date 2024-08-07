---
parent: Papers
---

# Statistical modeling: The two cultures

[link at Project Euclid](https://projecteuclid.org/journals/statistical-science/volume-16/issue-3/Statistical-Modeling--The-Two-Cultures-with-comments-and-a/10.1214/ss/1009213726.full)

[slides](https://ledaliang.github.io/journalclub/_static/breiman2001/Presentation.pdf)

## BibTeX
```
@article{breiman2001statistical,
  title={Statistical modeling: The two cultures (with comments and a rejoinder by the author)},
  author={Breiman, Leo},
  journal={Statistical science},
  volume={16},
  number={3},
  pages={199--231},
  year={2001},
  publisher={Institute of Mathematical Statistics}
}
```

## Abstract

> There are two cultures in the use of statistical modeling to reach conclusions from data. One assumes that the data are generated by a given stochastic data model. The other uses algorithmic models and treats the data mechanism as unknown. The statistical community has been committed to the almost exclusive use of data models. This commitment has led to irrelevant theory, questionable conclusions, and has kept statisticians from working on a large range of interesting current problems. Algorithmic modeling, both in theory and practice, has developed rapidly in fields outside statistics. It can be used both on large complex data sets and as a more accurate and informative alternative to data modeling on smaller data sets. If our goal as a field is to use data to solve problems, then we need to move away from exclusive dependence on data models and adopt a more diverse set of tools.

## Notes and Excerpts

> *Rashomon*: the multiplicity of good models;  
> *Occam*: the conflict between simplicity and accuracy;  
> *Bellman*: dimensionality—curse or blessing?  

Interestingly, the author is skeptical of linear models in general.
Or perhaps he just wishes people published cross-validation metrics...



> One goal of statistics is to extract information
from the data about the underlying mechanism producing the data. The greatest plus of data modeling
is that it produces a simple and understandable picture of the relationship between the input variables
and responses. For instance, logistic regression in
classification is frequently used because it produces
a linear combination of the variables with weights
that give an indication of the variable importance.
The end result is a simple picture of how the prediction variables affect the response variable plus
confidence intervals for the weights.
...
McCullah and Nelder (1989) write “Data will
often point with almost equal emphasis on several possible models, and it is important that the
statistician recognize and accept this.” 


> Just as
the 5% level of significance became a de facto standard for publication, the Cox model for the analysis
of survival times and logistic regression for survive–
nonsurvive data have become the de facto standard
for publication in medical journals. That different
survival models, equally well fitting, could give different conclusions is not an issue.


> [Rashomon] is closely onnected to what I call
instability(Breiman, 1996a) that occurs when there
are many different models crowded together that
have about the same training or test set error. Then
a slight perturbation of the data or in the model
construction will cause a skip from one model to
another. The two models are close to each other in
terms of error, but can be distant in terms of the
form of the model.
...
To improve accuracy by weeding out less
important covariates you run into the multiplicity
problem. The picture of which covariates are important can vary significantly between two models
having about the same deviance.



> For decades, the first step in prediction methodology was to avoid the curse. If there were too many
prediction variables, the recipe was to find a few
features (functions of the predictor variables) that
“contain most of the information” and then use
these features to replace the original variables.
...
But recent work has shown that
dimensionality can be a blessing.


Several interesting examples of the value of random forest models
with permutation importance to identify important features.
In fact, I wonder if a standard random forest is more amenable to this kind of interpretation,
since each tree can't affect the other.
Where with gradient boosting, 


Oh, and "bagging" comes from "**b**oostrap **agg**regat**ing**", apparently.


---


This was written in 2001, so dtrees and nnets were the old stuff and suppport vector machines were the new hotness at the time.
See:

> Support vector machines can also be used to
provide accurate predictions in other areas (e.g.,
regression). It is an exciting idea that gives excellent performance and is beginning to supplant the
use of neural nets. A readable introduction is in
Cristianini and Shawe-Taylor (2000)

Interesting that new ideas of how to wire together nnets brought them back as the new hotness.

Also, some insight into the idea behind SVM:
Turns the curse of dimensionality in your favor 
because raising dimensions increases chance of separating hyperplane.
(But difficult to balance with need for low generalization error.)





















