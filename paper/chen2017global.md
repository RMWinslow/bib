---
parent: Papers
---

# The global rise of corporate saving

[Sciencedirect html link](https://www.sciencedirect.com/science/article/pii/S0304393217300284)

[Author's webpage](https://sites.google.com/site/loukaskarabarbounis/research), (includes pdf, slides, appendix, and dataset)


## BibTeX
```
@article{chen2017global,
  title={The global rise of corporate saving},
  author={Chen, Peter and Karabarbounis, Loukas and Neiman, Brent},
  journal={Journal of monetary economics},
  volume={89},
  pages={1--19},
  year={2017},
  publisher={Elsevier}
}
```

## Abstract

> The sectoral composition of global saving changed dramatically during the last three decades. Whereas in the early 1980s most of global investment was funded by household saving, nowadays nearly two-thirds of global investment is funded by corporate saving. This shift in the sectoral composition of saving was not accompanied by changes in the sectoral composition of investment, implying an improvement in the corporate net lending position. We characterize the behavior of corporate saving using both national income accounts and firm-level data and clarify its relationship with the global decline in labor share, the accumulation of corporate cash stocks, and the greater propensity for equity buybacks. We develop a general equilibrium model with product and capital market imperfections to explore quantitatively the determination of the flow of funds across sectors. Changes including declines in the real interest rate, the price of investment, and corporate income taxes generate increases in corporate profits and shifts in the supply of sectoral saving that are of similar magnitude to those observed in the data.




## My Notes and Excerpts

> Consistent with previous studies such as Poterba (1987), we measure corporate saving as undistributed corporate profits. We note that corporate saving is a flow measure, distinct from the stock of savings accumulated through cash or other financial assets, and equals physical investment plus net lending in the corporate sector. Corporate saving together with government and household saving equal national saving.

Undistributed corporate profits. That's roughly three percent of GDI, but 15% of global GDP by their measurement? 
Is this because of depreciation? Consumption of fixed capital is counted separately in GDI (see CCAdj)
but represents investments and thus accounting profits the firm has gained.
Consumption of Fixed Capital is roughly 16 percent of US GDI.

(Yes, corporate savings here is Accounting profits minus dividends.)

> The corporate sector, therefore, transitioned from being a net borrower to being a net lender of funds to the rest of the global economy.

> When aggregated to the economy level, GVA equals GDP less net taxes on products.5 GVA is detailed in the generation of income account and equals the sum of income paid to capital, labor, and taxes:



> We generate these lines by pooling all countries with saving data for all three sectors and regressing the ratios of sector saving to GDP on time fixed effects. We weight the regressions by GDP, translated at market exchange rates, and we control for changes in the country composition of our unbalanced panel by absorbing country fixed effects. To benchmark the level of the lines, we pool all available countries in our data in 2013 and calculate the appropriate global value. We then use the estimated time fixed effects to extrapolate that level backwards. All subsequent plots at the global level from the national accounts data are constructed equivalently.

I'm not one hundred percent sure why they don't just use the direct aggregates. 
I think it has to do with the fact that the set of countries in their panel is changing over time?

> We conclude that forces causing the decline in the labor’s share of income did not produce commensurate increases in tax, dividend, and interest payments, resulting in an increase in corporate saving.

> First, as with most analyses of firm-level financing decisions that focus on non-financial corporations such as Fama and French (2001) and DeAngelo et al. (2004), we exclude financial firms (SIC codes 6000–6999). We also exclude other unclassified firms (SIC codes greater than or equal to 9000) as well as firms for which we cannot calculate a gross saving rate for at least 10 years.



Firm data is calculated from Compustat. Unfortunately, gross value added isn't present in the data.
It must be estimated as Gross Output minus Intermediate Consumption.
What they want to do at the firm level is calculate intermediates using:

- Operating Expenses = Cost of Goods Sold + Selling, General, and Administrative Expenses
- Intermediate Consumption = Operating Expenses - Depreciation - R&D - Staff Compensation - Production Taxes

But there is a further Problem: 
Staff Compensation and Production Taxes aren't in Compustat either.

So instead they use industry level multipliers pulled from the national accounts.

$$\pi_{cit} = \frac{Intermediates_{cit}}{Intermediates_{cit}+Compensation_{cit}+Taxes_{cit}} \\
= \frac{Intermediates_{cit}}{Operating Expenses_{cit} - Depreciation_{cit} - R\&D_{cit}}$$

Then assuming this fraction is the same for all firms in an industry, each firm's intermediate inputs are estimated as:

$$Intermediates_{fcit} = \pi_{cit} \times Operating Expenses_{fcit} - Depreciation_{fcit} - R\&D_{fcit}$$


Firm level savings is:

- Gross Savings = Sales + Depreciation + R&D - Operating Expenses - Interest - Corporate Taxes - Dividends

And the savings rate for a firm is Gross Savings divided by Gross Value Added.



> We use a standard within-between decomposition to quantify the extent to which the changes in the corporate saving rate reflect changes within or between industries. Denoting groups of firms by $i$ we decompose changes in the aggregate saving rate into these components as follows:

$$
\Delta 率_t = 
\underbrace{
    \sum_i \Big[ \big (率_{i,t} - 率_{i,t-1}\big) \cdot \frac{\omega_{i,t}+\omega_{i,t-1}}{2}\Big]
    }_{\text{Within-Group Component}} + 
\underbrace{
    \sum_i \Big[ \big (\omega_{i,t} - \omega_{i,t-1}\big) \cdot \frac{率_{i,t}+率_{i,t-1}}{2}\Big]
    }_{\text{Between-Group Component}}
$$

Where $率$ is the savings rate and $\omega_{i,t}$ 
is the share of group $i$ in total gross value added at time $t$.

(my simplification of formula)


Mostly the within components.

> Taken together, the results in Sections 3.2–3.4 suggest that the growth in corporate saving is not primarily driven by basic characteristics such as firm size or age and is not specific to a small number of industries. Much like our conclusion from analysis of the national accounts, these firm-level data paint a picture of a global and pervasive phenomenon. It is unlikely to reflect structural changes such as the decline in manufacturing, idiosyncratic changes in the market power of particular firms or industries, or changes in the corporate financial practices of particular firms or countries.


If I'm reading table 4 right, in recent years, 
increases in net lending were primarily spent to repay debt.




Fit a model to the start of the data. 
Tweak the parameters, see that it resembles the patterns near the end of the data. (kind of)
Untweak some of the parameters to see how important each change was.

> Rows 5–8 in the third panel of Table 5 conduct a series of counterfactual exercises to quantify separately the role of individual parameter changes. Here, we focus on the parameter changes that are quantitatively the most important and present in the Appendix additional counterfactual exercises. In each exercise, we revert one of the parameters back to its initial value and keep the others at their final values. Comparing the results in these rows with those in row 4 gives the independent impact of the excluded change.


Potentially an example to show in class. Not to work through.
But to say. Look, here's a more complicated model with the same conceptual components.

