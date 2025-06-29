---
parent: Papers
---

# The future of employment: How susceptible are jobs to computerisation?

[pdf link](https://oms-www.files.svdcdn.com/production/downloads/academic/The_Future_of_Employment.pdf)

[sciencedirect link](https://www.sciencedirect.com/science/article/abs/pii/S0040162516302244)

## BibTeX
```
@article{frey2017future,
  title={The future of employment: How susceptible are jobs to computerisation?},
  author={Frey, Carl Benedikt and Osborne, Michael A},
  journal={Technological forecasting and social change},
  volume={114},
  pages={254--280},
  year={2017},
  publisher={Elsevier}
}
```

## Abstract

>  We examine how susceptible jobs are to computerisation. To as
sess this, we begin by implementing a novel methodology to estimate
the probability of computerisation for 702 detailed occupations, using a
Gaussian process classifier. Based on these estimates, we examine ex
pected impacts of future computerisation on US labour market outcomes,
with the primary objective of analysing the number of jobs at risk and
the relationship between an occupation’s probability of computerisation,
wages and educational attainment. According to our estimates, about 47
percent of total US employment is at risk. We further provide evidence
that wages and educational attainment exhibit a strong negative relation
ship with an occupation’s probability of computerisation


## Notes and Excerpts


They do acknowledge that computers can do quite complex cognitive tasks.
That's the point of the study.

>  First, our analysis builds on the
 labour economics literature on the task content of employment (Autor, et al.,
 2003; Goos and Manning, 2007; Autor and Dorn, 2013). Based on defined
 premises about what computers do, this literature examines the historical im
pact of computerisation on the occupational composition of the labour mar
ket. However, the scope of what computers do has recently expanded, and will
 inevitably continue to do so (Brynjolfsson and McAfee, 2011; MGI, 2013).
 Drawing upon recent progress in ML, we expand the premises about the tasks
 computers are and will be suited to accomplish. Doing so, we build on the task
 content literature in a forward-looking manner. 


They use O∗NET for occupational work activities. But Also:
>  Our analysis builds on the task categorisation of Autor, et al. (2003), which
 distinguishes between workplace tasks using a two-by-two matrix, with routine
 versus non-routine tasks on one axis, and manual versus cognitive tasks on the
 other. ...  Following recent
 technological advances, however, computerisation is now spreading to domains
 commonly defined as non-routine. 


Production is Cobb douglass with inputs of (non-susceptible labor and susceptible labor + computers)


$$
Q = (L_s + C)^{1-\beta} L_{NS}^\beta
$$

>  Drawing upon the ML and
 MR literature, and a workshop held at the Oxford University Engineering Sci
ences Department, we identify several engineering bottlenecks, corresponding
 to three task categories. According to these findings, non-susceptible labor in
puts can be described as,

> $$L_{NS} = \sum_i (L_{PM,i} + L_{C,i} + L_{SI,i})$$

> where LPM, LC and LSI are labour inputs into perception and manipulation
tasks, creative intelligence tasks, and and social intelligence tasks.



Despite the paper being "about" the increasing capacity of machines, it still looks like they were blindsided by what the bottlenecks actually are. EG:

> For a computer to make a
 subtle joke, for example, would require a database with a richness of knowledge
 comparable to that of humans, and methods of benchmarking the algorithm’s
 subtlety

They identify nine )net characteristics related to these supposed 'bottlenecks' and then fit a model to to a small set of hand-labelled binary 0,1 automatibility labels. Then they apply that model to all 700 occupations.

I think there is some merit to replicating their paper with different labels assigned to some occupations.


---

Section II is about history of technology and employment. Potentially good teaching example.





---

Predicted least vulnerable:

1. 0.0028 29-1125 Recreational Therapists
2. 0.003 49-1011 First-Line Supervisors of Mechanics, Installers, and Repairers
3. 0.003 11-9161 Emergency Management Directors
4. 0.0031 21-1023 Mental Health and Substance Abuse Social Workers
5. 0.0033 29-1181 Audiologists
 6. 0.0035 29-1122 Occupational Therapists
 7. 0.0035 29-2091 Orthotistsand Prosthetists
 8. 0.0035 21-1022 Healthcare Social Workers
 9. 0.0036 29-1022 Oraland Maxillofacial Surgeons
 10. 0.0036 33-1021 First-Line Supervisors of Fire Fighting and Prevention Workers

Predicted most vulnerable:

693. 0.99 43-4141 New Accounts Clerks
694. 0.99 51-9151 Photographic Process Workers and Processing Machine Operators
695. 0.99 13-2082 Tax Preparers
696. 0.99 43-5011 Cargo and Freight Agents
697. 0.99 49-9064 Watch Repairers
698. 0.99 1 13-2053 Insurance Underwriters
699. 0.99 15-2091 Mathematical Technicians
700. 0.99 51-6051 Sewers, Hand
701. 0.99 23-2093 TitleExaminers, Abstractors, and Searchers
702. 0.99 41-9041 Telemarketers


Seems like the model mostly picked up on the social aspects as being the barrier to computerization.

Top and bottom seem plausible to me.

Some iffy ones: 
- 265. 0.38 27-3091 Interpreters and Translators
- Economists are hand-labelled as 0, lol.
-  592. 0.94 0 35-3031 Waiters and Waitresses
-  130. 0.042 15-1132 Software Developers, Application
