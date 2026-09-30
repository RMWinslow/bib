---
layout: bib
title: "Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations"
pub_authors:
  - "Kunal Handa"
  - "Alex Tamkin"
  - "Miles McCain"
  - "Saffron Huang"
  - "Esin Durmus"
  - "Sarah Heck"
  - "Jared Mueller"
  - "Jerry Hong"
  - "Stuart Ritchie"
  - "Tim Belonax"
  - "Kevin K. Troy"
  - "Dario Amodei"
  - "Jared Kaplan"
  - "Jack Clark"
  - "Deep Ganguli"
pub_year: 2025
date: 2026-09-29
modified: 2026-09-29
tags:
  - "Computer Science - Artificial Intelligence"
  - "Computer Science - Computation and Language"
  - "Computer Science - Computers and Society"
  - "Computer Science - Human-Computer Interaction"
  - "Computer Science - Machine Learning"
  - "llm"
zotero_key: "Q6SJLZ86"
---

<!-- Imported from Zotero item Q6SJLZ86 on 2026-09-29; citation source: Zotero BibTeX export. -->

[DOI](<https://doi.org/10.48550/arXiv.2503.04761>) · [arxiv.org paper page](<http://arxiv.org/abs/2503.04761>) · [arxiv.org PDF](<http://arxiv.org/pdf/2503.04761v1>)

## BibTeX

```bibtex
@misc{handa2025which,
  title = {Which {Economic} {Tasks} are {Performed} with {AI}? {Evidence} from {Millions} of {Claude} {Conversations}},
  author = {Handa, Kunal and Tamkin, Alex and McCain, Miles and Huang, Saffron and Durmus, Esin and Heck, Sarah and Mueller, Jared and Hong, Jerry and Ritchie, Stuart and Belonax, Tim and Troy, Kevin K. and Amodei, Dario and Kaplan, Jared and Clark, Jack and Ganguli, Deep},
  year = {2025},
  publisher = {arXiv},
  doi = {10.48550/arXiv.2503.04761},
  url = {http://arxiv.org/abs/2503.04761},
}
```

## Abstract

> Despite widespread speculation about artificial intelligence's impact on the future of work, we lack systematic empirical evidence about how these systems are actually being used for different tasks. Here, we present a novel framework for measuring AI usage patterns across the economy. We leverage a recent privacy-preserving system to analyze over four million Claude.ai conversations through the lens of tasks and occupations in the U.S. Department of Labor's O*NET Database. Our analysis reveals that AI usage primarily concentrates in software development and writing tasks, which together account for nearly half of all total usage. However, usage of AI extends more broadly across the economy, with approximately 36% of occupations using AI for at least a quarter of their associated tasks. We also analyze how AI is being used for tasks, finding 57% of usage suggests augmentation of human capabilities (e.g., learning or iterating on an output) while 43% suggests automation (e.g., fulfilling a request with minimal human involvement). While our data and methods face important limitations and only paint a picture of AI usage on a single platform, they provide an automated, granular approach for tracking AI's evolving role in the economy and identifying leading indicators of future impact as these technologies continue to advance.

## Notes and Excerpts

<!-- Zotero annotation DQ7CF35Y; attachment E8IX33KW; color green #5fb236 -->
> For example, Frey and Osborne [2017] fit a gaussian process classifier to a dataset of 70 labeled occupations to predict which occupations are subject to computerization. Brynjolfsson et al. [2018a] hire human annotators to rate 2,069 detailed work areas in the O*NET database, focusing specifically on their potential to be performed by machine learning. Webb [2019] analyzes the overlap between patent documents and job task descriptions to predict the "exposure" of tasks to AI
>
> *p. 3*
{: .zotero-green}

---

<!-- Zotero annotation K3A4IGDQ; attachment E8IX33KW -->
> With Clio, we map Claude.ai conversations to specific occupational tasks and their associated characteristics. However, a key challenge is the size of the O*NET task database we use (∼ 20K tasks), which makes direct classification via zero or few-shot prompting impossible because the full list of tasks does not fit in the model’s context window. We instead construct this as a classification over a hierarchy of task labels (Figure 9), inspired by Morin and Bengio [2005], Mnih and Hinton [2008].
>
> *p. 17*

---

<!-- Zotero annotation JA2CLG3Z; attachment E8IX33KW -->
> Creating a task hierarchy The O*NET database contains ∼ 20K task descriptions across all occupations. We constructed a multi-level taxonomy of tasks using Clio’s hierarchy generation step (Figure 9). This process recursively organizes base-level tasks into broader categories. The following details are reproduced from Appendix Section G.7 of Tamkin et al. [2024].9
>
> *p. 17*

---

<!-- Zotero annotation BLVTENF6; attachment E8IX33KW -->
> Mapping conversations to O*NET tasks To map conversations to specific tasks, we use this generated hierarchy to perform a tree-based search through our task hierarchy. For each conversation, we first used Claude to determine if the conversation was occupationally relevant. We screen conversations using Claude 3.5 Haiku (claude-3-5-haiku-20241022). The prompt we use for screening is provided in Appendix F. If the conversation is deemed relevant, we traverse the hierarchy from top to bottom, with Claude selecting the most appropriate task at each level based on the conversation content. Through this process, Clio calculates the cumulative number of conversations assigned to each task in the O*NET database. For privacy reasons, tasks with less than 5 unique accounts or 15 conversations are excluded from our analysis. This also serves to reduce statistical noise. Complete prompts are included in Appendix F. We also experimented with multi-class classification allowing up to k=3 task assignments per conversation; results were qualitatively similar, so we report the single-class results here for simplicity.
>
> *p. 18*

---

<!-- Zotero annotation SJSDNAHN; attachment E8IX33KW -->
> Each task in O*NET is associated with one or more occupations. To conduct our occupation-level analysis, we map from individual tasks to their associated occupations. To calculate occupational use, we aggregate the number of conversations associated with tasks for a given occupation.
>
> *p. 18*

Well,... I guess there are some duplicate strings. But the IDs are unique, and I think they're using
