---
parent: Papers
---

# Modeling the consumption response to the CARES Act

[NBER link](https://www.nber.org/papers/w27876)

## BibTeX
```
@techreport{carroll2020modeling,
  title={Modeling the consumption response to the CARES Act},
  author={Carroll, Christopher D and Crawley, Edmund and Slacalek, Jiri and White, Matthew N},
  year={2020},
  institution={National Bureau of Economic Research}
}
```

## Abstract

> To predict the effects of the 2020 U.S. CARES Act on consumption, we extend a model that matches responses to past consumption stimulus packages. The extension allows us to account for two novel features of the coronavirus crisis. First, during lockdowns, many types of spending are undesirable or impossible. Second, some of the jobs that disappear during the lockdown will not reappear. We estimate that, if the lockdown is short-lived (the median point of view as we are writing in April 2020), the combination of expanded unemployment insurance benefits and stimulus payments should be sufficient to allow a swift recovery in consumer spending to pre-crisis levels. If the lockdown lasts longer (or there is a ‘second wave’), an extension of enhanced unemployment benefits will likely be necessary for consumption spending to recover quickly.

## Notes and Excerpts

They build a more sophisticated model of the pandemic, where:
- certain kinds of goods are unavailable to purchase.
- certain industries are hit harder, such that 
  - some people expect to get their jobs back quickly
  - and some people expect to be unemployed for a long time.


> Perhaps surprisingly, we find the effectiveness of the combined stimulus checks
and unemployment benefits package for aggregate consumption is not substantially
different from a package that distributed the same quantity of money equally among
households. 


Wowzers, that's a dense lit review section!
I mean, just look at this thing:

> Many papers have recently appeared on the economic effects of the pandemic
and policies to manage it. Several papers combine the classic susceptible–infected–
recovered (SIR) epidemiology model with dynamic economic models to study the
interactions between health and economic policies (Eichenbaum, Rebelo, and Trabandt (2020) and Alvarez, Argente, and Lippi (2020), among others). Guerrieri,
Lorenzoni, Straub, and Werning (2020) shows how an initial supply shock (such as a
pandemic) can be amplified by the reaction of aggregate demand. The ongoing work
of Kaplan, Moll, and Violante (2020) allows for realistic household heterogeneity
in how household income and consumption are affected by the pandemic. Glover,
Heathcote, Krueger, and Ríos-Rull (2020) studies distributional effects of optimal
health and economic policies. Closest to our paper is some work analyzing the effects
of the fiscal response to the pandemic, including Faria-e-Castro (2020b) in a two-agent
DSGE model, and Bayer, Born, Luetticke, and Müller (2020) in a HANK model.
All of this work accounts for general equilibrium effects on consumption and employment, which we omit, but none of it is based on a modeling framework explicitly
constructed to match micro and macroeconomic effects of past stimulus policies, as
ours is.
A separate strand of work focuses on empirical studies of how the economy reacts
to pandemics; see, e.g., Baker, Farrokhnia, Meyer, Pagel, and Yannelis (2020), Jorda,
Singh, and Taylor (2020), Correia, Luck, and Verner (2020), Chetty, Friedman, Hendren, Stepner, and Team (2020), Garner, Safir, and Schild (2020), Casado, Glennon,
Lane, McQuown, Rich, and Weinberg (2020) and Coibion, Gorodnichenko, and Weber
(2020).

Lots more lit review in this paper, even after lit review section.
4/21 pages of main paper are bibliography. 
Impressive, in a way.



---

Adapts standard lifecycle model with a few twists.

- Transition between types of unemployed: Each quarter, deeply unemployed has 1/3 chance to transition to normal unemployed (2/3 to remain deeply unemployed), before then being able to find employment as normal (2/3 chance each period).
- Temporary shock to MPC as some forms of consumption are impossible.
- unexpected shock, sending households into deep or normal unemployment, similar to what I do.




> Our model assumes that the unemployment shock from the pandemic is a singular
event, with no change in the longer run job separation rate for employed households
(calibrated to generate a steady state unemployment rate of 5%). Consequently,
agents in our model who remain employed in Q2 2020 have no additional precautionary saving motive against a heightened risk of unemployment, and any change in
their consumption behavior arises from the marginal utility shock

> To calibrate the drop in marginal utility, we estimate that 10.9 percent of the
goods that make up the consumer price index become highly undesirable, or simply
unavailable, during the pandemic

---
