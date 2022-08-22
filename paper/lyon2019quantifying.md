---
parent: Papers
---

# Quantifying the losses from international trade

[pdf link](http://pseweb.eu/ydepot/seance/513030_lw_quant_losses.pdf)

## BibTeX
```
@article{lyon2019quantifying,
  title={Quantifying the losses from international trade},
  author={Lyon, Spencer and Waugh, Michael E},
  journal={Unpublished manuscript},
  year={2019}
}
```

## Abstract

> Did trade with China harm the US economy in the 2000s? A popular narrative suggests
so—that the rapid rise in Chinese import penetration lead to an expanding trade deficit and
negative impacts on wages and employment within narrowly defined labor markets. We provide an alternative interpretation of this evidence by developing a dynamic, standard incomplete market model with Ricardian trade and frictional labor markets and calibrated to match
local-labor-market evidence. Despite being consistent with the evidence of Autor, Dorn, and
Hanson (2013), a rising trade exposure induces a boom: a increase in GDP and employment,
a modest increase in consumption, and an improving trade deficit. Much heterogeneity in the
gains from trade underlays the aggregate effects; however, very few actually lose from trade.


## My Notes

The 2020 Trade Prelim at UMN asked us to read this paper and answer questions about it.

My responses are below.

### Question Part 1

What in your view is the major innovation in this paper relative to the related literature?

#### My Response

**Background:** In the early 2000s, China joined the WTO and the cost of importing goods from China into the US
decreased.
Subsequently, two things happened over the 2000s: The US trade deficit increased, and imports as a percentage
of GDP also massively increased.
A common narrative is to connect these facts and argue that increased imports from China were not associated
with increased export opportunities, thus increasing the trade deficit and hurting those industries which now had
to compete with Chinese imports.


Another paper, *Autor Dorn and Hanson (2013)*, which this paper is heavily influenced by, found the empirical
result that local labor markets which were more highly exposed to Chinese imports had lower wages and lower
participation.
Ah! But this is a result about differentials, not absolute levels of wages and participation. It doesn’t necessarily
mean that wages and participation went down in the aggregate.
The paper’s contribution is to set up a model of trade which:
- can be calibrated to match the empirical results from Autor Dorn and Hanson (2013) with import-exposed sections of the economy seeing relatively lower wages and participation
- allows households to partially, but not completely mitigate the income-risk caused by trade shocks.

The latter point is the innovation which yields very counterintuitive results. If the trade-induced income shocks
could be entirely insured against, then the gains from trade would be shared amongst everyone and the empirical
results about lower wages from ADF wouldn’t matter for welfare. And if the households couldn’t take any action
to insure against income-risk, then the trade shocks would pass right through to household consumption.

But because the authors set things up so that households can choose the extent to which they mitigate trade
risk, something strange happens: Even though at a local level, increased import-exposure reduces wages and labor
participation as in ADF; the aggregate participation goes up, as does output, consumption and net exports, thus
yielding a conclusion which goes against the common narrative (and predicts counterfactual aggregates) while still
matching the local level empirical facts.



### Question Part 2

Would the model used in this paper be suitable for examining the distributional impact of the China shock across
skilled and unskilled workers? If not, suggest some modifications / an alternative model that would be suitable for
examining such an impact. Feel free to make use of other papers we discussed in class in your answer.

#### My Response

Not really.

The model has a distribution of productivities. However, these productivity levels are attached to the “islands”
corresponding to the intermediate goods rather than the households.

Each household has the same aptitude $w_h$ for home production and has the same endowment of potential labor
hours. Households are instead differentiated by the assets they own and the island they live on.

And if a household decides to move to another island, then they island they move to is drawn at random, and
is in no way determined by any facts about the household itself.

In other words, the differences in productivity across workers in this model are caused by where people live
rather their intrinsic skill levels. It’s not about who you are but rather *where* you are.

To incorporate a difference between skilled and unskilled workers:

- You could have it so that effective units of potential labor hours differ between individuals. The “extra time” which high-skilled households have would be interpreted as being able to get more units of effective labor out of each day. The “wage” would be the same across individual households in the same location, but collecting one unit of a wage would take a smaller portion of the high-skill household’s time.
- or You could make the moving process “sticky” in z. Which is to say, when a household moves, instead of moving them to a independently chosen random island, move them using a process which is dependent on the productivity level of their current island.
    – For example, you could have the new island have z within some distance of the z or their old island
    – Or you could split the islands into two sectors, setting up the distributions of z such that the productivities in one sector of islands are typically lower than is the other. And households can move, but only withintheir sector.

*Post-exam Note: I was overthinking things. Could have also simply made production function use skilled and unskilled labor.*



### Question Part 3

Would the model used in this paper be suitable for examining the distributional impact of the China shock across
skilled and unskilled workers? If not, suggest some modifications / an alternative model that would be suitable for
examining such an impact. Feel free to make use of other papers we discussed in class in your answer.

#### My Response

There are a few interesting implications the come from the cost of moving.

Firstly, for very unproductive low z islands, participating in the labor market doesn’t yield very good returns.
So households will tend to either try to move to a better island, or drop out and engage in home production. The
presence of a monetary cost of moving means that if a household’s assets are just a little bit too low to pay the
moving costs, then they’ll participate even in the poor labor market so that they can save up enough assets to move
out.

And secondly and more generally, this cost of moving means that households with very low wealth simply cannot
choose to move. They are trapped on their poor islands by poverty.

Finally, because the households on low z islands are likely to have experienced a run of bad luck with regards to
shocks to income, such households are also more likely to have low assets. So the people who want to move islands
are also those likely to be unable to move islands.
Without this monetary cost, even the poorest of households will be able to move if they so desire, and the low $z$ islands would tend to become more rapidly depopulated.

The empirical results for *Autor,Dorn,Hanson(2013)* suggest that trade exposure has very little effect on the
migration from a commuting area.
But in this paper’s model, we get that higher trade exposure incentivizes households to take action to insure
against risk, and moving to a better island is one such way to do this.
So by imposing a monetary cost on moving, the authors are given a parameter which which they can calibrate
to make migration patterns match what is observed.






### Question Part 4

In the model used in this paper, there is both a utility cost and a monetary cost of moving across islands. What
do you think would change if there were only a utility cost? Why do you think the authors decided to include the
monetary cost?

#### My Response

The reason that this model concludes that a China shock is associated with higher output, consumption and labor
supply is that reducing the costs of imports exposes the country more to trade and so increases income risk. Income
may be much higher or much lower due to trade, but the most important thing is that it is more variable.
So households take extra action to mitigate this income risk and smooth out consumption over time, working
extra during the good times so they can save up assets to live off of while engaging in home production during the
bad times.

And so with the self-insurance mechanism removed, income risk increases, reducing the ability of households to
smooth out consumption over time, thus reducing welfare.
My intuition is that this would increase the inequality of the welfare distribution as people with very good or
bad luck with regards to income shocks are less able to use inter-temporally trade to mitigate their bad luck, or
spread their good luck out over time.
With self-insurance, a very high income this period can be used to give yourself a nest-egg which can smooth out
consumption over future periods. Without self-insurance, then that surge of income can only be used as consumption
or to move to a better island.

Removing the self-insurance wouldn’t completely eliminate the households ability to insure against income risk.
They could still do so via the choice of when to move and whether to enter the labor market vs engage in home
production. But even this would be complicated by, for example, the fact that because a household cannot save
means to move, they need to earn more than m in a single period, which will exacerbate the poverty trap from part
(3) .






### Question Part 5

Does the authors’ assumption that the interest rate is constant and exogenous affect their conclusions about the
impact of the China Shock on the U.S. trade balance? How? The following paper may help you think about this:

[The Role of Trade Costs in the Surge of Trade Imbalances](http://rreyes-heroles.com/uploads/3/6/2/8/36287730/jmp_reyesheroles.pdf)


#### My Response

Yes.

As discussed in part (4), the mechanism by which the model results in increased output etc. is by increasing
income risk and so encouraging households to insure against this by engaging in increased labor.
Namely, whereas the standard story is that US trade deficits increased as a result of the China Shock, this model
predicts that such a shock leads to decreased trade deficits. And the reason for this is that in export-exposed islands,
where income tends to be higher, households work more to save up for when they might become import-exposed.
And this savings behavior results in exports increasing more than imports do.

But Lyon and Waugh note in the paper that a decline in real interest rates will make it easier to trade across
time, reducing the need for such precautionary labor. So a significant enough reduction in R would overwhelm the
trade-induced precaution and so lead to increased trade deficits.
The authors argue that the appropriate conclusion from the model is therefore that the China Shock isn’t
responsible for increasing US trade deficits. But rather, agreeing with Bernanke (2005), it was the large fall in real
interest rates which coincidentally took place at the same time that triggered increased trade deficits.

In light of this conclusion, the linked paper throws an extra pickle into the mix by describing a mechanism by
which decreasing trade costs and patterns of trade can themselves change the real interest rate.
