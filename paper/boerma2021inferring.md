---
parent: Papers
---

# Inferring inequality with home production

[Wiley Online html link](https://onlinelibrary.wiley.com/doi/full/10.3982/ECTA15966)

[Author's webpage](https://sites.google.com/site/loukaskarabarbounis/research) with slides, appendix, and replication material

## BibTeX
```
@article{boerma2021inferring,
  title={Inferring inequality with home production},
  author={Boerma, Job and Karabarbounis, Loukas},
  journal={Econometrica},
  volume={89},
  number={5},
  pages={2517--2556},
  year={2021},
  publisher={Wiley Online Library}
}
```

## Abstract

> We revisit the causes, welfare consequences, and policy implications of the dispersion in households' labor market outcomes using a model with uninsurable risk, incomplete asset markets, and home production. Allowing households to be heterogeneous in both their disutility of home work and their home production efficiency, we find that home production amplifies welfare-based differences, meaning that inequality in standards of living is larger than we thought. We infer significant home production efficiency differences across households because hours working at home do not covary with consumption and wages in the cross section of households. Heterogeneity in home production efficiency is essential for inequality, as home production would not amplify inequality if differences at home only reflected heterogeneity in disutility of work.



## My Notes

### classroom discussion

A potential tangential teaching example.
This paper's model might not be good for presenting in class.
But the concepts are very relevant to the discussion of leisure in chapter 4.

> It is well known, however, that households spend roughly half as much time in home production activities such as child care, shopping, and cooking as in the market.

"Blah blah blah, here's what leisure means,
incidentally, one of the professors here studies leisure in more detail...
yes indeed, economics is a broader field than what many think of it as,
anyways, we aren't worrying about that here."


### Idle thought about my household

I was talking with someone, mentioned that I have enough savings to survive a couple years.
He says "wow, how horrible your standard of living must be to save that much money on such a low salary".
I pointed to supplemental income. 
But another factor for quality of life is my household's very high home production productivity.

### Marriage

> Our model features a single decision maker within each household. We model hours worked across spouses as perfect substitutes and in our quantitative results, ... The perfect substitutability of hours (across sectors and spouses) is essential for the no-trade result. We can extend the model for separate disutility of work by spouse.

### P and N sectors

To make the model identifiable, they assume there are two distinct types of chores:

- N type, where people vary by efficiency but dislike it the same amount as they dislike working 
- P type, where people vary by how much they dislike doing it, but have the same skill levels

To split tasks into the two types, they index them by how manually intensive they are. Above-median chores are type P, below median are type N.

- Type N: skills vary: childcare, shopping, nursing, "other"
- Type P: preferences vary, but same skill level: cooking, cleaning, gardening, laundry, "other"

Does the analysis change if the categories are split differently? 
The categories don't feel right to me.

People wildly vary in cooking skill.
I like cooking just as much as my wife does. 
But she does most of the cooking because she is *much, much* better at it.

Conversely, I am just as good at shopping as my wife is,
but dislike shopping more than she does.
(If anything bet I'm a more efficient shopper because I just want to get out of there.)

My intuition is that a better indicator is the variance in wages within the comparable occupation.
That might introduce a correlation in dispersions though. I don't think that would have major effects on the analysis. But who knows?

Sensitivity analyses in table VIII.
Eyeballing it, I don't see anything about different splits,
nor in the appendix.
That might be a project to do this weekend.

Thoughts:
Main results are from lack of negative coorelation between market hours and home production hours.
But cooking, cleaning, shopping, laundry *feel* to me like the kinds of things where there should be a negative correlation:
TODO: check whether there actually is a negative correlation.


<!-- Relevant?
> Tables A.IV and A.V demonstrate that the correlation of home hours
with both consumption and wages is broadly similar in magnitude between the CEX/ATUS sample and the
PSID samples in which home production time is not imputed
-->

Indeed , the counterfactual illustrated in figure 5 says that if there were either:

- a strongly negative correlation between log wages and hours spent on type N chores (child care) or
- a strongly negative correlation between log consumption and hours spent on type N chores

then the model with home production would indeed have less inequality (by the equivalent variation metric)
than the model without home production.

> We calculate that hN has a correlation of 0.07 with log zM and 0 with log cM . ...

> if the data featured a significantly more negative correlation between
hN and either log zM or log cM , then we would have concluded that inequality in the model
with home production is actually lower.

Based on the counterfactuals in table VII, where they put all the chore time into one sector or another,
They find that if there are only type P chores, then the inequality is comparable to the model without home production.

> We conclude that heterogeneity in home production efficiency
rather than disutility of work is important in amplifying inequality across households

This might be a reasonable response to the childcare issue.
They repeat the analysis for various demographic subgroups (see Table VIII)

> Additionally, verifying our results at the subgroup level is
reassuring because it allows us to control for dimensions of heterogeneity which we did
not model, such as spousal employment at the extensive margin, the presence of young
children, or the number of children

In particular, restricting the analysis to the group without children still results in the home production model having higher inequality.
(the difference is smaller than the baseline but it's still there.)


A note about why PSID is not the best source of data

>  Second, the PSID has lower quality of time use data compared to the time diaries from the ATUS. In
particular, it is not clear if respondents include activities such as child care and shopping
in their reported home hours.3

> The survey question is, “About how much time do you spend on housework in an average week? I mean
time spent cooking, cleaning, and doing other work around the house."

Yeah, I wouldn't include child care time in that metric either.


But on the other hand:

> Our results using the PSID are particularly reassuring because we do not take a stance
about the classification of time uses between hN and hP . Therefore, the result that inequality is higher with home production does not hinge on which activities are subject to
efficiency heterogeneity and which activities are subject to disutility heterogeneity. What
is important for this result is that some portion of home production time is subject to
heterogeneity in production efficiency.

So that means in PSID, home production in total isn't negatively correlated with wage or consumption, yes?
TODO: Check whether I am interpreting this correctly.

Table X comes closest to doing the kind of sensitivity analysis I'd like to see (because there is no category split)
but I don't see them explicitly looking at different chore partitions. 
Are there partitions in which hN *is* negatively correlated with wage or consumption?



### Hump Shaped Home Efficiency

> The model with home production generates a hump-shaped profile of home efficiency
θN ... Until
roughly 40, θN tracks market productivity zM since φ > 1. Despite zM still rising, θN starts
to decline after 40 and returns to its initial value by 65. This pattern is generated by the
strong decline in hours hN after 40. As shown in Table IV, child care is the subcategory of
hN responsible for this decline.

Now wait a dang second. 
Sector N chores are in large part (slightly more than half) child care. 
So what they're observing is simply that the time spent on child care is hump shaped.
(Edit: actually, the initial rise is because earnings are rising, not just because childcare is.)
Then their model is interpreting that as a hump shaped pattern in the efficiency of home production.

A few potential responses to this:
- Yes, that makes sense. Your fertility declines with age, while your readiness for parenting increases with age. So as long as we count fertility as a factor of home productivity, then sure enough θN is hump shaped.
- Yes, that makes sense, and is a reflection of the nuclear family norms. If children were more often raised by their grandparents, then the hump shaped would be less prominent. These kinds of child care arrangements are in fact a social technology, and so a hump-shaped pattern of "home efficiency" is a sensible representation of the economies studied.
- No, this doesn't make sense. The analysis needs to be redone. (Without child care included in either category?)

Perhaps I ought to take a look at cardia2018market.

### Marriage?

This is more nebulous, but marriage?

If a person with high market wages marries a person with high home productivity, and then they specialize, 
will there still be a connection between market wages and home efficiency?

The paper has this to say:

> We define household market hours hM as the sum of hours worked by
spouses and define market productivity zM as the average of wages of individual members
weighted by their market hours.

Someone is married to a spouse with lower wages. 
They get divorced. 
The high-earning spouse's household suddenly has much higher labor productivity, and lower hours. 
The model says that this is because their home efficiency shot up?

This particular concern seems alleviated by:

> Further, sensitivity analyses presented in Section 5 confirm our inequality results in a sample of singles and in a
subsample of married households with a working spouse for which valuation at market wages is less concerning. 


And an even more nebulous question: what happens if spousal matching is endogenous?
I'm not even sure where to begin thinking about folding that into this kind of analysis.









<!--
NAME REDACTED said he really dislikes this paper.
I went to write down *why* but had a brain fart and can't remember.
I remember he was talking about his cooking decisions.
He really likes cooking. Buys a bunch of hello fresh.
But he's terrible at cooking. 
Oh right!. He also said there's a limit to how much work you can do.
Someone working full time 40 hours a week, 
at the margin, can't substitute home time for *additional work time*
The intensive margin isn't flexible like that. 
(Maybe some sort of lifetime efficiency comparison would make more sense?)
-->



