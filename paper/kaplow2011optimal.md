---
parent: Papers
---

# TITLE

[UChicago html link](https://www.journals.uchicago.edu/doi/full/10.1086/664614?casa_token=-KKF_sR_MPsAAAAA%3A8waPlzqG0905mD5ci88Lv5CKR_BiVOJ7eY7jz0EyCnXD6FuRntIX8NL6VcYwREhMSRCIfoNi-U8)


## BibTeX
```
@article{kaplow2011optimal,
  title={On the optimal burden of proof},
  author={Kaplow, Louis},
  journal={Journal of Political Economy},
  volume={119},
  number={6},
  pages={1104--1140},
  year={2011},
  publisher={University of Chicago Press Chicago, IL}
}
```

## Abstract

> The burden of proof, a central feature of adjudication and other decision-making contexts, constitutes an important but largely unappreciated policy instrument. The optimal strength of the burden of proof, as well as optimal enforcement effort and sanctions, involves trading off deterrence and the chilling of desirable behavior, the latter being absent in previous work. The character of the optimum differs markedly from prior results and from conventional understandings of proof burdens. There are important divergences across models in which enforcement involves monitoring, investigation, and auditing. A number of extensions are analyzed, in one instance nullifying key results in prior work.




## My Notes

Author
: Louis Kaplow

Summary 
: Builds a model in which a policy maker tries to dis-incentivize harmful acts via sanction with the risk that those sanctions will unjustly be applied to people who committed some benign act instead.

In this paper's model, punishment itself causes no harm to social welfare. Instead, unjust punishment harms social welfare via a 'chilling effect', by disincentivizing benign action which can be mistaken for harmful action.

There are two separate populations of people: one considering whether to commit some harmful act with a negative externality, and a separate population considering whether to commit some benign action. Both types of actions carry a risk of being punished; if a person does neither action, they won't be punished.

There are three policy levers:

- The **severity** of punishment;
- the level of costly **enforcement**, which increases the probability that a person will be punished for committing *any* act;
- and the **evidence threshold** required for punishment, which implicitly defines a sort of ROC curve representing the tradeoff between the rate at which harmful actors are punished, and the rate at which benign actors are punished. 

Individuals are risk neutral, so as per the 'Becker Rule', optimal policy involves maximal punishment. The remaining analysis then is about the optimal tradeoff between higher levels of enforcement and  lower evidence thresholds.

<!--- A larger negative externality favors both an increase in enforcement and/or a decrease in the evidence threshold. Deterrence is more important.
- A smaller relative population of people considering whether to commit the *benign* action (ie criminals are a larger portion of the population) likewise favors both an increase in enforcement and/or a decrease in the evidence threshold.-->

<!--The paper also says optimal policy will have 'under-deterrence', meaning that the harm of externality exceeds the benefit to the marginal person doing the crime-->

<!--Also, in this model, trying to choose an evidence threshold such that the ex-post probabilities of punished innocents vs free guiltos satisfies some particular ratio can have wacky counterintuitive multiple-equilibrium style consequences. EG higher evidence threshold increases the number of benign actors and can result in a larger number of benign actors being prosecuted.-->

The model can be interpreted as a story in which people choose whether to commit an act; then have some chance of being prosecuted if they chose to act; and then, if prosecuted, are punished based on the evidence about whether their action was harmful or benign. 
An increase in the evidence threshold can in theory <!--because no MLRP?--> *increase* the probability of innocence conditional on being prosecuted. 
*(Note to self: This paper assumes FSD. Would stronger assumption MLRP prevent this counterintuitive result?)*

Several extensions are considered. Here are two I find interesting:

*No Benign actors:* Enforcement targets everyone; the evidence threshold determines the tradeoff between TPR (the probability that a guilty person will be punished) and FPR (the probability that an innocent person will be punished). <!--This seems like the more basic version which I'm guessing the author tried first.-->
Because people are risk neutral and punishment itself has no social cost, optimal policy consists simply of:

- maximum-intensity punishment,
- an evidence threshold that maximizes informedness (the difference between TPR and FPR),
- and whatever level of enforcement is optimal given the above.

*Costly Punishment:* If the punishment itself harms social welfare, then the effects are ambiguous. In particular, the optimal evidence threshold could go up or down when the cost of punishment is introduced into the social welfare function. This is because *an increase in the probability that a benign actor is punished* decreases the number of benign actors, and so potentially *decreases the quantity of benign actors who are punished*. <!--Zero tolerance policy (in the sense of unjustly punishing things which are similar to the transgression) can be good?-->
The chilling effect might now be a net positive for social welfare.
