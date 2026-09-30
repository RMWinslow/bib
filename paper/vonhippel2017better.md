---
layout: bib
title: "Better Estimates from Binned Income Data: Interpolated CDFs and Mean-Matching"
pub_authors:
  - "Paul T. von Hippel"
  - "David J. Hunter"
  - "McKalie Drown"
pub_year: 2017
date: 2026-09-29
modified: 2026-09-29
tags:
  - "Gini"
  - "gini"
  - "grouped data"
  - "income brackets"
  - "inequality"
zotero_key: "7BXU6MUC"
---

<!-- Imported from Zotero item 7BXU6MUC on 2026-09-29; citation source: Zotero BibTeX export. -->

[DOI](<https://doi.org/10.15195/v4.a26>) · [sociologicalscience.com PDF](<https://www.sociologicalscience.com/download/vol-4/november/SocSci_v4_641to655.pdf>)

## BibTeX

```bibtex
@article{vonhippel2017better,
  title = {Better {Estimates} from {Binned} {Income} {Data}: {Interpolated} {CDFs} and {Mean}-{Matching}},
  author = {von Hippel, Paul T. and Hunter, David J. and Drown, McKalie},
  year = {2017},
  journal = {Sociological Science},
  volume = {4},
  pages = {641--655},
  doi = {10.15195/v4.a26},
  issn = {2330-6696},
}
```

## Abstract

> Researchers often estimate income statistics from summaries that report the number of incomes in bins such as $0 to 10,000, $10,001 to 20,000, …, $200,000+. Some analysts assign incomes to bin midpoints, but this treats income as discrete. Other analysts fit a continuous parametric distribution, but the distribution may not fit well. We fit nonparametric continuous distributions that reproduce the bin counts perfectly by interpolating the cumulative distribution function (CDF). We also show how both midpoints and interpolated CDFs can be constrained to reproduce the mean of income when it is known. We evaluate the methods in estimating the Gini coefficients of all 3,221 U.S. counties. Fitting parametric distributions is very slow. Fitting interpolated CDFs is much faster and slightly more accurate. Both interpolated CDFs and midpoints give dramatically better estimates if constrained to match a known mean. We have implemented interpolated CDFs in the "binsmooth" package for R. We have implemented the midpoint method in the "rpme" command for Stata. Both implementations can be constrained to match a known mean.

## Notes and Excerpts

<!-- Zotero annotation 86YKNFVS; attachment 643TPWV4 -->
> We fit nonparametric continuous distributions that reproduce the bin counts perfectly by interpolating the cumulative distribution function (CDF).
>
> *p. 641*

---

<!-- Zotero annotation 4VQQXL5V; attachment 643TPWV4 -->
> Another approach is to fit the bin counts to a continuous parametric distribution.
>
> *p. 641*

---

<!-- Zotero annotation BN76ETB7; attachment 643TPWV4 -->
> Pareto, log normal, Weibull, and
>
> *p. 641*

---

<!-- Zotero annotation LUHF4I7U; attachment 643TPWV4 -->
> Dagum distributions, among others (McDonald and Ransom 2008).
>
> *p. 642*

---

<!-- Zotero annotation UYL6MXEF; attachment 643TPWV4 -->
> Unfortunately, past nonparametric approaches have been disappointing.
>
> *p. 643*

---

<!-- Zotero annotation IWJH9EPF; attachment 643TPWV4 -->
> In this article, we implement and test a nonparametric continuous method that simply connects points on the empirical cumulative distribution function (CDF). The method, which we call CDF interpolation, outperforms its predecessors in both speed and accuracy. The method can connect the points using line segments or cubic splines. When cubic splines are used, the method is similar to ”histospline” or ”histopolation” methods, which fit a spline to a histogram (Wahba 1976; Morandi and Costantini 1989). But histosplines are limited to histograms that have bins of equal width (Wang 2015). CDF interpolation is a more general approach that can handle income data for which the bins have unequal width and the top bin has no upper bound (e.g., Table 1).
>
> *p. 643*

---

<!-- Zotero annotation GVDBYZWF; attachment 643TPWV4 -->
> We also show that the differences between methods are dwarfed by the improvement we get if we constrain a method to match the grand mean of income,
>
> *p. 643*

---

<!-- Zotero annotation DZKMWWI8; attachment 643TPWV4 -->
> We initially suspected that cubic spline interpolation would improve on simple linear interpolation, but empirically this turns out to be false
>
> *p. 651*
