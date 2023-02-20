---
parent: Papers
---

# Deconstructing life cycle expenditure

[pdf link](https://scholar.princeton.edu/sites/default/files/670740_0.pdf)

## BibTeX
```
@article{aguiar2013deconstructing,
  title={Deconstructing life cycle expenditure},
  author={Aguiar, Mark and Hurst, Erik},
  journal={Journal of Political Economy},
  volume={121},
  number={3},
  pages={437--492},
  year={2013},
  publisher={University of Chicago Press Chicago, IL}
}
```

## Abstract

> We revisit two well-known facts regarding life cycle expenditures: the
“hump”-shaped profile of nondurable expenditures and the increase
in cross-household consumption inequality. We document that the
behavior of total nondurables masks surprising heterogeneity in the life
cycle profile of individual consumption subcomponents. We provide
evidence that the categories driving life cycle consumption either are
inputs into market work or are amenable to home production. Using a
quantitative model, we document that the disaggregated life cycle consumption profiles imply a level of uninsurable permanent income risk
that is substantially lower than that implied by a model using a composite
consumption good.



## Notes and Excerpts


- Nondurable consumption is hump-shaped over lifecycle. 25% higher in middle age than at 25 or 65
- The decline is driven by food, nondurable transportation, clothing, and personal care.
- housing services, utilities, entertainment, domestic services, charitable giving, etc. don't exhibit this old-age decline.
- cross-sectional variance in non-durable consumption increases with age and is driven by the same categories.



> Models based solely on fluctuations in financial resources to explain the profiles predict that categories with larger
income elasticities should display greater increases in cross-sectional dispersion and more pronounced hump shapes. However, the disaggregated
data show no such pattern. 

> The data do, however, support a prominent role for expenses that are
closely linked to a household’s opportunity cost of time. 

Basically, they argue that the decrease in consumption after middle age is caused by 
decreasing attachment to the labor force,
which comes with a decreased need to spend on things like food and transportation.

Supporting evidence for this:
- There is an age-related decline in fast food and cafeteria visits, but not in visits to restaurants with table service. 
- Time spent commuting declines after age 50 but time spent on non-work travel slightly increases in the second half of life.

------

Time-separable, strictly concave utility over N
consumption commodities is $u(c_1, c_2, ... , c_N)$
where each consumption good is a combination of time $h_n$ and market expenditures $x_n$,
given by some crs technology $c_n = f_n(x_n,h_n)$.


Static one period problem with fixed non-market time $H$ and total expenditures $X$
(so choosing what to buy after choosing *how much* to work and spend):

$$
\max_{\{x,h,c\}} u(c_1, c_2, ... , c_N) \\
s.t. \\ 
c_i = f_i(x_i,h_i) \\
\sum_n p_nx_n \leq X \\
\sum_n h_n \leq H \\
$$

With $\lambda$ as the multiplier for budget and $\lambda w$ the multiplier for time, the FOCs will be 

$$
\frac{\partial u}{\partial c_i} \frac{c_i}{x_i} = \lambda p_i
$$

$$
\frac{\partial u}{\partial c_i} \frac{c_i}{h_i} = \lambda w
$$

Using $f_{xi}$ and $f_{hi}$ as shorthand for $\frac{c_i}{x_i}$ and $\frac{c_i}{h_i}$, 
these FOCs imply

$$\frac{ f_{hi} }{ f_{xi} } = \frac{w}{p_i}$$



------


> We use the extracts compiled by Ed Harris and John Sabelhaus and provided
by the NBER (http://www.nber.org/data/ces_cbo.html). Harris and Sabelhaus
aggregate expenditures into 47 categories, which are listed in the supplementary
documentation. The Harris and Sabelhaus data set includes households whose
first interview was conducted between the first quarter of 1980 and the second
quarter of 2003. Owing to changes in the survey methodology, data from the last
two quarters of 1985 and 1995 are omitted.32 The data set contains a total of
167,133 households.
>
> We restrict the Harris and Sabelhaus sample in the following ways. First, we
keep households whose heads are between ages 25 and 75. To obtain reliable estimates of cohort effects, we also restrict attention to cohorts with at least 10 years
of data. In particular, we restrict the sample to households born between 1915
and 1968, that is, to households whose head is at most 65 in 1980 and at least
35 in 2003. This leaves 122,962 households. Second, the household must have
completed all four expenditure surveys, providing a complete picture of annual
expenditures. There are 75,883 such households in the sample, or roughly 62 percent. Harris and Sabelhaus provide adjusted weights to use with the restricted sample. However, their restricted sample also excludes households with incomplete income reports and students. Usage of their adjusted weights necessitates excluding
these households as well, leaving 58,305 households.
>
> Our final sample restriction is that households must have strictly positive expenditure on six major expenditure categories: food, housing services, utilities,
clothing and personal care, nondurable transportation, and nondurable entertainment. Roughly 92 percent of the sample satisfied this last criterion, resulting
in a sample of 53,412 households. This is our main sample for analysis


[link for NBER CEX extracts](https://www.nber.org/research/data/consumer-expenditure-survey-extracts)
Only goes to 2003 sadly.

- Use NBER CEX extract (1980-2003)
- restrict to households that report expenditures in all four quarters and sum to get annual expenditures
- restrict sample to households that report non-zero annual expenditure on all of: food, entertainment, transportation, clothing and personal care, utilities, housing and rent.
- focus on households in which head is age 25-75, inclusive.
- these restrictions give 53412 households

Additional caveats

- When looking at consumption subcategories, they bottom-code to one dollar and take logs. (Whew. I've done that before. Glad to know it's not silly to do.)
- for lifecycle means and cross-section dispersion, they look at nondurables excluding health and education, meaning: *food, alcohol, tobacco, clothing and personal care, utilities, domestic services, nondurable transportation, airfare, nondurable entertainment, net gambling receipts, business services, and charitable giving*
  - aalternate measure includes housing services, meaning rent or rent equivalent.


To estimate lifecycle profile for consumption category, they regress:

$$
\begin{align*}
\ln C &= \beta_0 + \beta_{age} age  + \beta_{coh} cohortDummies + \\
& \beta_{age} normalizedYearDummies + \beta_{fam} familyStructureDummies + \varepsilon\\
\end{align*}
$$

Year effects are assumed to capture cyclicality.
Meaning year effects must average zero over the sample period,
and be orthogonal to a time trend.
(See Deaton 1997 for details why this is done?)


To get cross sectional variance, they do the above regression, 
they find the variance of the residuals and then regress the variance on age and cohort dummies.
Not sure I quite understand the details.
TODO: See Deaton and Paxson (1994) for details of approach.



---



> There is little
consensus within the literature about the appropriate way to adjust for
changes in family size. Moreover, the size of the hump in life cycle expenditures is sensitive to the family size controls.11 One common alternative
approach is to adjust for changes in family size over the life cycle by deflating expenditure in year t by a measure of adult equivalence scales
in year t, where the equivalence scales are based on the household’s family composition in that year.12 The equivalence scale usually assigns a
value of 1 to the first adult household member, a value of either 0.5 or
0.7 to each additional adult member, and a value of 0.3 or 0.5 to each
child. Alternatively, the equivalence scale is some mathematical rule such
as the square root of family size. 

> 11 See Fernandez-Villaverde and Krueger (2006) for a discussion of the various ways in
which the literature has controlled for family size when estimating life cycle profiles of
expenditures. Fernandez-Villaverde and Krueger also show how the hump in lifetime expenditures is quantitatively sensitive to the choice of family size controls.   
12 A common set of equivalence scales are provided by the Organization for Economic
Cooperation and Development (OECD)

But they don't like this approach because 
- no consensus on which multipliers to use
- heterogeneity within categories (why do teenagers counts the same as babies?)
- adn they think the multipliers should vary by consumption category

They note they're still implicitly assuming that family composition is exogenous
rather than endogenously determined by income.


They note that CEX has some measurement problems with clothing, energy and childcare.
Ratio of CEX expenditures to Nation accounts for those categories have fallen.
See  Bee, Meyer, and Sullivan (2012)





---




In a previous paper,
they used Continuing Survey of Food Intake of Individuals (CSFII) 
to show that food intake increases after middle age despite decline in expenditures


Can't seperate types of travel spending in CEX, but ATUS suggests one third of travel is commuting:

> The average individual between the ages of 25 and 75 spends 9.0 hours per
week traveling, with 2.3 hours per week associated with commuting to and
from work. For those who work, work-related travel represents roughly
one-third of all time spent traveling.


See Figure 6 for cute graph of travel time by age.
Though I'm not sure the implications of using family composition dummies in there.
Might have to make that comparison myself.



----

use demand system analysis to look at relationship between spending and work.

Total expenditures included as control variable

regress share of expenditures in each consumption category $k$ on: 
age cohort and family dummies;
log price level of goods overall and from category $k$; 
and a controls for labor status (oof husband and wife).

Also instrument total expenditures with log family income (bottom coded with an extra dummy), family income squared, family income cubed, 
and education dummies.


The run the numbers and this analysis confirms that clothing, nondurable transportation, and food
are the only expenditures categories positively associated with labor supply.


----

For the model analysis:

- power utility with two goods
- one good only market, the other cobb douglass in market and time
- agents live for fixed T+1 periods, discount at rate $\beta$
- risk free asset with constant rate $r$ over lifespan

Two sources of risk:
- labor productivity shock which follows $b_1 t + b_2 t^2 + fixedEffect_i + AR(1)process + \varepsilon$
    - fixed effect varies by person. Time effects shared.
- risk of retirement or disability. You'll transfer from the state in which you can work to one in which you can't. 

State $s$ consists of (assets $a$, time (eg age), retirement status, the persistent parts of productivity shocks, and also a variable $\epsilon$ I can't find (did they mean $\varepsilon$? I am a confusion).

Problem is to choose expenditures, new assets $a'$ and time use. In recursive form problem is:

$$V(s) = \max u(c_1,c_2) + \beta \mathbb{E}[V(s') | s]$$


subject to

$$
a' = \begin{cases}
(1+r)a +wn \exp z - c_1 - x_h&\text{if } R=0 \\
(1+r)a + S - c_1 - x_h&\text{if } R=1 \\
\end{cases}
$$

(S is social security)

$$
c_2 = f(x_h,h)\\
1 = n+h\\
a' \geq \underline a\\
n \geq \underline n \text{ if }R=0\\
h \geq 0
$$

(Good teaching example?)

They use PSID to pin down age-contingent 'risk' of retirement. (TODO: I want to see/make such a graph.)





---



> In Section VI, we compare the model’s implied wage process with that observed
in our PSID sample. The latter parameters were estimated as follows. Using the
PSID sample, we regressed log real wage on a full set of age dummies, normalized
year dummies, and a full set of cohort dummies. This is essentially (without family
size controls) the specification used for consumption (4).






















