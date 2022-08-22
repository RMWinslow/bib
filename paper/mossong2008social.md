---
parent: Papers
---

# Social contacts and mixing patterns relevant to the spread of infectious diseases

[html link](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0050074)

## BibTeX
```
@article{mossong2008social,
  title={Social contacts and mixing patterns relevant to the spread of infectious diseases},
  author={Mossong, Jo{\"e}l and Hens, Niel and Jit, Mark and Beutels, Philippe and Auranen, Kari and Mikolajczyk, Rafael and Massari, Marco and Salmaso, Stefania and Tomba, Gianpaolo Scalia and Wallinga, Jacco and others},
  journal={PLoS medicine},
  volume={5},
  number={3},
  pages={e74},
  year={2008},
  publisher={Public Library of Science}
}
```

## Abstract

> **Background**
> Mathematical modelling of infectious diseases transmitted by the respiratory or close-contact route (e.g., pandemic influenza) is increasingly being used to determine the impact of possible interventions. Although mixing patterns are known to be crucial determinants for model outcome, researchers often rely on a priori contact assumptions with little or no empirical basis. We conducted a population-based prospective survey of mixing patterns in eight European countries using a common paper-diary methodology.
> 
> **Methods and Findings**
7,290 participants recorded characteristics of 97,904 contacts with different individuals during one day, including age, sex, location, duration, frequency, and occurrence of physical contact. We found that mixing patterns and contact characteristics were remarkably similar across different European countries. Contact patterns were highly assortative with age: schoolchildren and young adults in particular tended to mix with people of the same age. Contacts lasting at least one hour or occurring on a daily basis mostly involved physical contact, while short duration and infrequent contacts tended to be nonphysical. Contacts at home, school, or leisure were more likely to be physical than contacts at the workplace or while travelling. Preliminary modelling indicates that 5- to 19-year-olds are expected to suffer the highest incidence during the initial epidemic phase of an emerging infection transmitted through social contacts measured here when the population is completely susceptible.
> 
> **Conclusions**
To our knowledge, our study provides the first large-scale quantitative approach to contact patterns relevant for infections transmitted by the respiratory or close-contact route, and the results should lead to improved parameterisation of mathematical models used to design control strategies.



## My Notes


Diary study that tries to empirically map out physical contacts. Finds age-contact matrix, and finds number of contacts based day of week, country, activity, etc.

> Although mixing patterns are known to be crucial determinants for model
outcome, researchers often rely on a priori contact assumptions with little or no empirical basis.
We conducted a population-based prospective survey of mixing patterns in eight European
countries using a common paper-diary methodology.

>  Contact patterns were highly assortative with age:
schoolchildren and young adults in particular tended to mix with people of the same age.
Contacts lasting at least one hour or occurring on a daily basis mostly involved physical
contact, while short duration and infrequent contacts tended to be nonphysical. Contacts at
home, school, or leisure were more likely to be physical than contacts at the workplace or while
travelling. Preliminary modelling indicates that 5- to 19-year-olds are expected to suffer the
highest incidence during the initial epidemic phase of an emerging infection transmitted
through social contacts measured here when the population is completely susceptible.

> [unlike with HIV needle sharing networks], the contact structure for these infections has been
assumed to follow a predetermined pattern governed by a
small number of parameters that are then estimated using
seroepidemiological data

Uses negative binomial model

### Simulation:

Divide population in 15 age bands. Denote the number of at-risk
contacts of an individual in age class j with individuals in age
class i by $k_{ij}$. This matrix $K$ is called the *next generation matrix* in epidemiology.

> For large [generation number] $i$ , the
vector $x_i$ will be proportional to the leading eigenvector of $K$.We find that, in practice, the distribution of new cases is
stable after five generations; that is, the distribution no longer
depends on the precise age of the initial case.

>  the observed contact
patterns reveal that schoolchildren drive the epidemic in all
age groups during the initial phase of spread for infections
transmitted by droplets and through close contacts.

### contact data

Contains table of contacts based on age, sex, household size, day of week, and country.

> On average, German participants reported the fewest daily
number of contacts (mean ¼ 7.95, standard deviation [SD] ¼
6.26) and Italians the highest number (mean ¼ 19.77, SD ¼
12.27). The contact distributions in all countries are slightly
skewed, the skewness statistics ranging from 0.62 in IT to 2.96
in DE (Figure S1).

(What definition of skewness? $\frac{\mu - v}{\sigma}$?)

> Apart from the remarkable
similarity of the general contact pattern structure in the
different countries, three main features are apparent from
the data. First, the dominant feature is the strong diagonal
element: individuals in all age groups tend to mix assortatively
... Second, two parallel secondary diagonals starting at
roughly 30–35 years for both contacts and participants are
offset from the central diagonal. This pattern represents
children mixing with adults in the 30–39 age range
... The third feature is more apparent in the data for all
reported contacts (Figure 3A) than for physical contacts only:
a wider contact ‘‘plateau’’ of adults with other adults
primarily due to low-intensity contacts, with many of these
contacts occurring at work

> One of the most important findings of our study is that the
age and intensity patterns of contact are remarkably similar
across different European countries even though the average
number of contacts recorded differed. This similarity implies
that the results may well be applicable to other European
countries, and that the initial phase of spread of newly
emerging infections in susceptible populations, such as SARS
was in 2003, is likely to be very similar across Europe and in
countries with similar social structures

> Another major insight gained from our study comes from
the observation that the contacts made by children and
adolescents are more assortative than contacts made by other
age groups. That is, most of the individuals contacted by
children and teenagers are of very similar age, and these
contacts tend to be of long duration. This pattern is likely to
be the main reason why children and teenagers are and have
been an important conduit for the initial spread of close-
contact infections in general and for influenza in particular

> Our results suggest that
if efforts concentrate on locating contacts in the home,
school, workplace, and leisure settings, on average more than
80% of all contacts would be found.

> However, we note that our survey did not address
the clustering of contacts; such clustering of contacts might
result in less-pronounced differences in age-specific inci-
dence than suggested by our calculations.

> One of the major assumptions behind our approach is that
talking with or touching another person constitutes the main
at-risk events for transmitting infectious diseases. There may
be other at-risk events that our methodology does not
capture, such as being in a confined space or in close physical
proximity with other individuals and not talking to them