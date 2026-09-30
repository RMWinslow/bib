---
layout: bib
title: "Clio: privacy-preserving insights into real-world AI use"
pub_authors:
  - "Alex Tamkin"
  - "Miles McCain"
  - "Kunal Handa"
  - "Esin Durmus"
  - "Liane Lovitt"
  - "Ankur Rathi"
  - "Saffron Huang"
  - "Alfred Mountfield"
  - "Jerry Hong"
  - "Stuart Ritchie"
  - "Michael Stern"
  - "Brian Clarke"
  - "Landon Goldberg"
  - "Theodore R. Sumers"
  - "Jared Mueller"
  - "William McEachen"
  - "Wes Mitchell"
  - "Shan Carter"
  - "Jack Clark"
  - "Jared Kaplan"
  - "Deep Ganguli"
pub_year: 2024
date: 2026-09-29
modified: 2026-09-29
tags:
  - "Computer Science - Artificial Intelligence"
  - "Computer Science - Computation and Language"
  - "Computer Science - Computers and Society"
  - "Computer Science - Cryptography and Security"
  - "Computer Science - Machine Learning"
  - "llm"
zotero_key: "YNILYCIA"
---

<!-- Imported from Zotero item YNILYCIA on 2026-09-29; citation source: Zotero BibTeX export. -->

[DOI](<https://doi.org/10.48550/arXiv.2412.13678>) · [arxiv.org paper page](<http://arxiv.org/abs/2412.13678>) · [arxiv.org PDF](<http://arxiv.org/pdf/2412.13678v1>)

## BibTeX

```bibtex
@misc{tamkin2024clio,
  title = {Clio: privacy-preserving insights into real-world {AI} use},
  author = {Tamkin, Alex and McCain, Miles and Handa, Kunal and Durmus, Esin and Lovitt, Liane and Rathi, Ankur and Huang, Saffron and Mountfield, Alfred and Hong, Jerry and Ritchie, Stuart and Stern, Michael and Clarke, Brian and Goldberg, Landon and Sumers, Theodore R. and Mueller, Jared and McEachen, William and Mitchell, Wes and Carter, Shan and Clark, Jack and Kaplan, Jared and Ganguli, Deep},
  year = {2024},
  publisher = {arXiv},
  doi = {10.48550/arXiv.2412.13678},
  url = {http://arxiv.org/abs/2412.13678},
}
```

## Abstract

> How are AI assistants being used in the real world? While model providers in theory have a window into this impact via their users' data, both privacy concerns and practical challenges have made analyzing this data difficult. To address these issues, we present Clio (Claude insights and observations), a privacy-preserving platform that uses AI assistants themselves to analyze and surface aggregated usage patterns across millions of conversations, without the need for human reviewers to read raw conversations. We validate this can be done with a high degree of accuracy and privacy by conducting extensive evaluations. We demonstrate Clio's usefulness in two broad ways. First, we share insights about how models are being used in the real world from one million Claude.ai Free and Pro conversations, ranging from providing advice on hairstyles to providing guidance on Git operations and concepts. We also identify the most common high-level use cases on Claude.ai (coding, writing, and research tasks) as well as patterns that differ across languages (e.g., conversations in Japanese discuss elder care and aging populations at higher-than-typical rates). Second, we use Clio to make our systems safer by identifying coordinated attempts to abuse our systems, monitoring for unknown unknowns during critical periods like launches of new capabilities or major world events, and improving our existing monitoring systems. We also discuss the limitations of our approach, as well as risks and ethical concerns. By enabling analysis of real-world AI usage, Clio provides a scalable platform for empirically grounded AI safety and governance.

## Notes and Excerpts

<!-- Zotero annotation TFCUAVL3; attachment IFGY3VBC -->
> For non-categorical or numeric facets (e.g., our request facet), we first embed each extracted summary using all-mpnet-base-v2 [Reimers and Gurevych, 2022], a sentence transformer model that provides 768-dimensional embeddings. We then generate base-level clusters by running k-means in embedding space. We vary k based on the number of conversations in the input dataset; we unfortunately cannot provide our precise values for k (as this information could be used to determine the volume at which coordinated behavior would likely not be caught by Clio as a distinct cluster).
>
> *p. 39*

---

<!-- Zotero annotation IQQIKEST; attachment IFGY3VBC -->
> Clio’s hierarchizer transforms base clusters (described in Appendix G.5) into a hierarchy. The hierarchizer iteratively creates new levels clusters (which contain the previous level of clusters as children) until the number of top-level clusters is within the desired range. We also explored other hierarchical clustering algorithms (such as HDBSCAN [McInnes et al., 2017] and agglomerative clustering methods) but found the results inferior to the Claude-based approach.
>
> *p. 40*
