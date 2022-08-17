---
parent: Papers
---

# Judicial mechanism design

[pdf link](https://faculty.wcas.northwestern.edu/bhs675/JMD.pdf)

## BibTeX
```
@article{siegel2018judicial,
  title={Judicial mechanism design},
  author={Siegel, Ron and Strulovici, Bruno},
  journal={Unpublished manuscript. Pennsylvania State University, Department of Economics, University Park},
  year={2018}
}
```

## Abstract

> This paper proposes a mechanism design approach to study criminal justice systems. We derive
properties of optimal mechanisms for two notions of welfare distinguished by their treatment of
deterrence. These properties (i) provide insights into the effects of defendants’ private information
about their guilt, (ii) highlight forces that may underlie certain features of existing systems, such
as plea bargaining and binary verdicts and the separation of fact finding and sentencing, and (iii)
indicate directions for possible improvements of criminal trials, such as varying the standard for
conviction across crimes


## My Notes


Authors
: Ron Siegel and Bruno Strulovici

Summary
: Builds a model which suggests the optimality of 'plea-bargain' mechanisms. 


In this paper's model, defendants are either guilty or innocent, and can choose to plea guilty or innocent. The level of punishment depends on the defendant's actual guilt, on their self-reported plea, and on some costly-to-generate signal representing the amount of evidence for their guilt. (The signal is drawn from one of two distributions with monotone likelihood ratio property (MLRP) depending on whether the person is guilty. But the person's signal realization is unknown to them when they make their report.)

In the tradition of mechanism design, only truth-inducing mechanisms are considered. In any optimal policy in this model, a guilty plea must be at least weakly optimal for a guilty person, and likewise an innocent plea for an innocent person.

When the probability that a defendant is guilty is exogenous (and utility and social welfare are strictly concave), optimal policy consists of:

- A fixed punishment for anyone who pleads guilty (a 'plea-bargain').
    - *(Without the concave utility assumption, the optimal plea-bargain punishment might instead be a lottery over two different punishment severities.)*
- A 'trial' for anyone who pleads innocent, where the signal is generated and then:
    - no punishment is dealt out if the signal is below some evidence threshold, but
    - *maximum* punishment is dealt out if the signal is above that evidence threshold.

The evidence threshold, and the severity of the plea-bargain punishment are chosen such that a guilty person is indifferent between plea-ing innocent or guilty, and they are assumed to always choose to plea guilty. (An extension argues that if some of the guilty people plea innocent, then the above mechanism still can *approximate* optimality.)
Oddly, in equilibrium, everyone who receives the maximal punishment is innocent. Committing to this unjust punishment is simply the least-costly way to compel the guilty to confess.

A model with deterrence is also considered. The number of defendants is connected to the actual number of crimes committed.
There is some exogenous probability that the correct person is prosecuted for a crime, and second exogenous probability that the *incorrect* person is prosecuted. The latter probability is assumed to be so low that it doesn't affect a person's decision about whether to commit a crime.
In this modified version of the model, optimal policy ends up looking much the same.
The only difference is that under some circumstances, the optimal plea-bargain punishment may be a lottery over two different punishment severities, even when utilities are strictly concave.

In this model, something like the Becker rule arises in optimal policy. When a case goes to trial and the defendant is found guilty, punishment is as high as possible. And the probability of punishment is as low as possible while still achieving some desired effect.
This is despite the lack of a risk-neutrality assumption, and is ultimately the consequence of the MLRP assumption.
Quoth the paper:

>  In Becker’s framework, extreme sentences are used to save on enforcement costs. In our framework, extreme sentences play a different role: they serve to maximize the screening power of plea bargaining.

It is worth noting that the MLRP is a stronger assumption than First-Order Stochastic Dominance.