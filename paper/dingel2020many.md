---
parent: Papers
---

# How many jobs can be done at home?

[ScienceDirect link](https://www.sciencedirect.com/science/article/pii/S0047272720300992)

[Github repo for this paper](https://github.com/jdingel/DingelNeiman-workathome)

## BibTeX
```
@article{dingel2020many,
  title={How many jobs can be done at home?},
  author={Dingel, Jonathan I and Neiman, Brent},
  journal={Journal of Public Economics},
  volume={189},
  pages={104235},
  year={2020},
  publisher={Elsevier}
}
```

## Abstract

> Evaluating the economic impact of “social distancing” measures taken to arrest the spread of COVID-19 raises a fundamental question about the modern economy: how many jobs can be performed at home? We classify the feasibility of working at home for all occupations and merge this classification with occupational employment counts. We find that 37% of jobs in the United States can be performed entirely at home, with significant variation across cities and industries. These jobs typically pay more than jobs that cannot be done at home and account for 46% of all US wages. Applying our occupational classification to 85 other countries reveals that lower-income economies have a lower share of jobs that can be done at home.



## Notes and Excerpts

Uses two surveys from release 24.2 of the database administered by O*NET,

> The first survey is called the Work Context Questionnaire

> The second survey is called the Generalized Work Activities Questionnaire

> The median occupation had 26 respondents for each Work Context question and 25 respondents for each Generalized Work Activities question.

They use responses from these surveys to disqualify certain activites from WFH

From Work Context survey:

- Average respondent says they use email less than once per month (Q4)
- Average respondent says they deal with violent people at least once a week (Q14)
- Majority of respondents say they work outdoors every day (Q17 & Q18)
- Average respondent says they are exposed to diseases or infection at least once a week (Q29)
- Average respondent says they are exposed to minor burns, cuts, bites, or stings at least once a week (Q33)
- Average respondent says they spent majority of time walking or running (Q37)
- Average respondent says they spent majority of time wearing common or specialized protective or safety equipment (Q43 & Q44)

And from GWA Questionnaire:

- Performing General Physical Activities is very important (Q16A)
- Handling and Moving Objects is very important (Q17A)
- Controlling Machines and Processes [not computers nor vehicles] is very important (Q18A)
- Operating Vehicles, Mechanized Devices, or Equipment is very important (Q20A)
- Performing for or Working Directly with the Public is very important (Q32A)
- Repairing and Maintaining Mechanical Equipment is very important (Q22A)
- Repairing and Maintaining Electronic Equipment is very important (Q23A)
- Inspecting Equipment, Structures, or Materials is very important (Q4A)


They also manually assigned occupations based on Gut Instinct.
These results were correlated with their category above.


> Mas and Pallais (2020) offer a detailed and helpful overview
of the prevalence, features, and demand for alternative working arrangements, including the ability to work from home. Citing the
Quality of Worklife Survey and the Understanding American Study,
they report that less than 13% of full- and part-time jobs have a formal “work-from-home” arrangement, even though twice that
amount work often from home.

<!--Only 8 pages. Well documented Git repo. My god, this is a clean paper.-->


I wonder if it might not be easy to test this paper using the 2021 ATUS data?