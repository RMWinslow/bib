---
parent: Papers
---

# Measuring commuting in the american time use survey

[pdf link](https://mpra.ub.uni-muenchen.de/93239/2/MPRA_paper_93239.pdf)

[github repo with stata code](https://github.com/graykimbrough/atus-commuting)

## BibTeX
```
@article{kimbrough2019measuring,
  title={Measuring commuting in the american time use survey},
  author={Kimbrough, Gray},
  journal={Journal of Economic and Social Measurement},
  volume={44},
  number={1},
  pages={1--17},
  year={2019},
  publisher={IOS Press}
}
```

## Abstract

> Research into the relationships between commuting and other activities has been
hampered by the lack of suitably comprehensive datasets. This paper identifies a possible source of detailed information for such studies, the American Time Use Survey
(ATUS). This paper surveys approaches used by researchers to analyze commuting in
the ATUS and outlines a method of measuring commuting in a clear and consistent
way. This analysis details the advantages of this method over other approaches. Commuting measured in the ATUS using this methodology is shown to be consistent with
commuting measures in other large, nationally representative studies. The proposed
methodology makes possible a range of analyses exploiting the unique information in
the ATUS


## Notes and Excerpts

> For this analysis, commutes are defined generally as trips from home to work or from
work to home. Classifying direct trips—with no stops along the way to perform any other
tasks—as commuting is straightforward. Problems arise when an individual stops along
the way between home and work, because it is not evident which of this travel is commuting and which is primarily intended to reach other destinations. The methodology detailed in this paper provides a consistent means of accounting for stops when measuring
and analyzing commuting behavior in the ATUS.

BLS provides “travel related to work,”
but 

> More significantly, it excludes many commuting spells when stops are made
along the way between home and work. Notably, this effect is asymmetrical, impacting
the trip to work differently from the trip home. If a worker reports stopping to perform
another activity along the way to work, the last travel spell is generally coded as work-related travel. However, stopping on the way from work to home means that no travel
from this commute leg is classified as travel related to work.

[allard2018impact](https://www.bls.gov/opub/mlr/2018/article/what-is-the-impact-of-recoding-travel-activities-in-the-american-time-use-survey.htm)
makes a similar point.

> The Brown and Borisova methodology considers all travel between home and work to be commuting, regardless of the number or length of stops. For
individuals starting and ending at home, this can be thought to provide an upper bound
of commuting time, but including all travel between the two likely substantially overestimates commuting time.

## Calculating Commuting Using trip chains


> The trip tour methodology outlined by McGuckin and Nakamoto McGuckin and Nakamoto
(2004) ... All trips in a trip chain that contains stops of no more than 30 minutes each are combined to form tours anchored by home, work, or another location. Using this framework,
commuting trip tours are those that either begin at home and end at work, or begin at
work and end at home ... The Department of Transportation applies this methodology to the NHTS data to
produce datasets containing information on trip tours


National Household Travel Survey.

> all sleep spells occurring at the beginning and end of the ATUS diary day
(that is, beginning before 4 A.M. or ending after 4 A.M.) are treated as occurring at the
respondent’s home

> In summary, when the commuting trip tour measure is applied to the ATUS, observed
commuting behavior matches up closely with observed behavior in the NHTS, both in the
aggregate (as shown by comparisons of means) and throughout the day (as shown in tempograms)