---
parent: Other
---

# This overlooked variable is the key to the pandemic

[Link to article](https://www.theatlantic.com/health/archive/2020/09/k-overlooked-variable-driving-pandemic/616548/)

## BibTeX
```
@article{tufekci2020overlooked,
  title={This overlooked variable is the key to the pandemic},
  author={Tufekci, Zeynep},
  journal={The Atlantic},
  volume={30},
  year={2020}
}
```


## My Notes




### Brief summaries of linked articles:

🤔 means I might want to come back and read in more detail.

[Overdispersion and Backwards contact tracing](https://www.medrxiv.org/content/10.1101/2020.08.01.20166595v1.full.pdf) 🤔

#### Regulatory issues

[Low-sensitivity testing being denied approval](https://www.theatlantic.com/health/archive/2020/08/how-to-test-every-american-for-covid-19-every-day/615217/) 

Inexpensive, low sensitivity test, saliva based, 15 minute turnaround

> The tests Mina describes already exist: They are sitting in the office of e25 Bio, a small start-up in Cambridge, Massachusetts; half a dozen other companies are working on similar products. But implementing his vision will require changing how we think about tests. These new tests are much less sensitive than the ones we run today, which means that regulations must be relaxed before they can be sold or used. Their closest analogue is rapid dengue-virus tests, used in India, which are manufactured in a quantity of 100 million a year. Mina envisions nearly as many rapid COVID-19 tests being manufactured a day. Only the federal government, acting as customer and controller, can accomplish such a feat.

> In CDC guidelines written by a council of state epidemiologists, a positive PCR result is the only way to confirm a case of COVID-19. And the Food and Drug Administration, which regulates all COVID-19 tests used in the U.S., judges every other type of test against PCR. 

Also some talk about pooled testing.

[Perfect as the enemy of the good: Using low-sensitivity tests to mitigate SARSCoV-2 outbreaks](https://dash.harvard.edu/bitstream/handle/1/37363184/Transmission%20Tracing%20-%20Kennedy-Shaffer%20Baym%20Hanage.pdf?sequence=1&isAllowed=y) 🤔

"Tracing transmission events rather than infected individuals can
efficiently and effectively prevent infection waves."

#### Links about Sweden's Strategy

- [A description of Sweden's policy](https://www.cnbc.com/2020/03/30/sweden-coronavirus-approach-is-very-different-from-the-rest-of-europe.html)
- [concerns about second wave](https://www.businessinsider.com/sweden-decline-coronavirus-deaths-cases-2020-9)


#### Superspreading events

- [Testing of 35k people after SK superspreading event](https://asia.nikkei.com/Spotlight/Coronavirus/South-Korea-tests-35-000-people-linked-to-club-coronavirus-cluster)
- [Choir outbreak in Washington - detailed analysis](https://www.cdc.gov/mmwr/volumes/69/wr/mm6919e6.htm)
  - 60 people exposed to index case. 2 hours of singing.
  - 32 new confirmed cases, 20 probable; 53-87% transmission ("attack rate")
  - Median incubation for COVID19 is 5.1 days, but median was 3 days in this outbreak.
- [Early covid19 transmission in Jakarta-Depok and Batam](https://www.medrxiv.org/content/medrxiv/early/2020/07/24/2020.06.28.20142133.full.pdf)
  - $R_0$ estimated at 6.79 and 2.47
  - $k$ estimated at 0.06 and 0.2
- [SARS 2 in Georgia](https://www.pnas.org/content/117/36/22430) 
  - "Superspreading is ubiquitous over space and time, and has particular importance in rural areas and later stages of an outbreak. " ?! A funeral in particular.
  - "First, our results show that the reproductive number reduced to below one in about 2 wk after the shelter-in-place order. "
  - "We estimate that the infected nonelderly cases (<60 y) may be 2.78 [2.10, 4.22] times more infectious than the elderly"
- [Superspreading in Tianjin](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7277812/) 🤔
  - $R$ 0.67, $k$ 0.25
  - When we examined the chronological development of the infection in Tianjin, we found that the confirmed cases were mainly composed of the imported cases and the household infections in the early and the later stage of outbreak, respectively. The transition happened around 3 February
  - Interesting simulations and pictures. Want to come back to this one.
- [Hong Kong SSEs with SARS2](https://www.nature.com/articles/s41591-020-1092-0)
  - 19% (95% confidence interval, 15–24%) of cases seeded 80% of all local transmission
  - Transmission in social settings was associated with more secondary cases than households when controlling for age 
- [Infographics about Korea's Patient 31](https://graphics.reuters.com/CHINA-HEALTH-SOUTHKOREA-CLUSTERS/0100B5G33SB/index.html)
- [Identifying and Interrupting Superspreading Events](https://wwwnc.cdc.gov/eid/article/26/6/20-0495_article). Many examples.

#### Other case studies

- [Household spread in Guangzhou - Lancet](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30471-0/fulltext) 🤔
  - Includes contact tracing maps
  - Breakdown of transmission through different kinds of contacts
  - "Social distancing or other potential personal behavioural changes might have also shifted the contact pattern between household members, as shown by the two-fold reduction in the probability of household transmission observed between January and February"
  - Also, The Lancet has a good display format for citations.
- [Estimating dispersion outside of china](https://wellcomeopenresearch.org/articles/5-67/v3) [2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7338915/) 🤔
  - Based on [WHO report](https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200227-sitrep-38-covid-19.pdf) on local vs imported cases in each country, takes accepted $R_0$ estimates and uses them to calculate $k$ estimate of 0.1
  - Might want to come back and look at the source code for this one.
- [Shenzen China contact tracing](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7185944/)
  - household secondary attack rate was 11·2%
- [Stochasticity and heterogeneity in the transmission dynamics of SARS-CoV-2](https://arxiv.org/pdf/2005.13689.pdf) 🤔
- [ Aotearoa New Zealand](https://www.medrxiv.org/content/10.1101/2020.08.05.20168930v3)
  - "Re, of New Zealand's largest cluster decreased from 7 to 0.2 within the first week of lockdown."
- [Status of environmental surveillance for SARS-CoV-2 virus](https://www.who.int/news-room/commentaries/detail/status-of-environmental-surveillance-for-sars-cov-2-virus) - Potential to use water smapling to detect virus in animal population, etc.
- [Combining fine-scale social contact data with epidemic modelling](https://www.medrxiv.org/content/10.1101/2020.05.26.20113720v2)
  - Simulates outbreak on social network derived from GPS data
  - "tracing contacts-of-contacts reduced the size of simulated outbreaks more than tracing of only contacts, but resulted in almost half of the local population being quarantined at a single point in time"

This guy looks like he might have some [entertaining books](http://kucharski.io/books/) about contagion and gambling.

Jensen's inquality and growth in populations?



### Highlighted Quotes:


>  After nine months of collecting epidemiological data, we know that this is an overdispersed pathogen

> in Western societies, where the pandemic playbook was geared toward the flu—and not without reason, because pandemic flu is a genuine threat. However, influenza does not have the same level of clustering behavior.

> Scarpino told me, “Diseases like the flu are pretty nearly deterministic and R0 (while flawed) paints about the right picture (nearly impossible to stop until there’s a vaccine).” That’s not necessarily the case with super-spreading diseases.


> Much is still unknown about the super-spreading of SARS-CoV-2. It might be that some people are super-emitters of the virus, in that they spread it a lot more than other people. 

> In study after study, we see that super-spreading clusters of COVID-19 almost overwhelmingly occur in poorly ventilated, indoor environments where many people congregate over time—weddings, churches, choirs, gyms, funerals, restaurants, and such—especially when there is loud talking or singing without masks. 

> Overdispersion should also inform our contact-tracing efforts. ... Right now, many states and nations engage in what is called forward or prospective contact tracing. Once an infected person is identified, we try to find out with whom they interacted afterward so that we can warn, test, isolate, and quarantine these potential exposures. ... Instead, in many cases, we should try to work backwards to see who first infected the subject.  
> Because of overdispersion, most people will have been infected by someone who also infected other people, because only a small percentage of people infect many at a time, whereas most infect zero or maybe one person

> if we can use retrospective contact tracing to find the person who infected our patient, and then trace the forward contacts of the infecting person, we are generally going to find a lot more cases compared with forward-tracing contacts of the infected patient, which will merely identify potential exposures, many of which will not happen anyway, because most transmission chains die out on their own.

(analogy to friendship paradox)

> Similarly, the infectious person who is transmitting the disease is like the pandemic social butterfly

Talk about how  cheap, low-sensitivity testing can be more useful in this kind of clustered spreading events.

> In an overdispersed regime, identifying transmission events (someone infected someone else) is more important than identifying infected individuals. 

> Wastewater testing [(in dorms andd nursing homes)] also has low sensitivity; it may miss positives if too few people are infected, but that’s fine for population-screening purposes. 

> Unfortunately, until recently, many such cheap tests had been held up by regulatory agencies in the United States, partly because they were concerned with their relative lack of accuracy in identifying positive cases compared with PCR tests—a worry that missed their population-level usefulness for this particular overdispersed pathogen.

> [Overdispersion] means that events that result in spreading and non-spreading of the virus are asymmetric in their ability to inform us. 

> although Sweden joins many other countries in failing to protect elderly populations in congregate-living facilities, its measures that target super-spreading have been stricter than many other European countries. ... Sweden imposed a 50-person limit on indoor gatherings in March, and did not remove the cap ... Plus, the country has a small household size and fewer multigenerational households...  Both transmission and illness risks go up with age, and Sweden went all online for higher-risk high-school and university students—the opposite of what we did in the United States.

> The most informative case studies may well be those who had terrible luck initially, like South Korea, and yet managed to bring about significant suppression. 

> Compared with a steadier regime, success in a stochastic scenario can be more fragile than it looks.  Once a country has too many outbreaks, it’s almost as if the pandemic switches into “flu mode,” as Scarpino put it, meaning high, sustained levels of community spread even though a majority of infected people may not be transmitting onward.

> Oshitani told me that in Japan, they had noticed the overdispersion characteristics of COVID-19 as early as February, and thus created a strategy focusing mostly on cluster-busting, ... “the chain of transmission cannot be sustained without a chain of clusters or a megacluster.” Japan thus carried out a cluster-busting approach, including undertaking aggressive backward tracing to uncover clusters. 

Three Cs: **Crowds** in **Closed** spaces in **Close** Contact

(One thing that I disagree with the article on is that it spends a lot of time talking about the importance of understanding clustering for persuing an approach in which gov shuts down theatres and stadiums. But this is also a sound strategy even if your target is just to clamp down on the average. I don't think that undestanding $k$ is super important for this strategy.)

> The U.K.’s recent decision to limit outdoor gatherings to six people while allowing pubs and bars to remain open

!!!
