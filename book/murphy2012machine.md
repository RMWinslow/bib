---
parent: Books
---

# Machine learning: a probabilistic perspective


## BibTeX
```
@book{murphy2012machine,
  title={Machine learning: a probabilistic perspective},
  author={Murphy, Kevin P},
  year={2012},
  publisher={MIT press}
}
```

## Publisher Blurb

> A comprehensive introduction to machine learning that uses probabilistic models and inference as a unifying approach.
Today's Web-enabled deluge of electronic data calls for automated methods of data analysis. Machine learning provides these, developing methods that can automatically detect patterns in data and then use the uncovered patterns to predict future data. This textbook offers a comprehensive and self-contained introduction to the field of machine learning, based on a unified, probabilistic approach.
>
> The coverage combines breadth and depth, offering necessary background material on such topics as probability, optimization, and linear algebra as well as discussion of recent developments in the field, including conditional random fields, L1 regularization, and deep learning. The book is written in an informal, accessible style, complete with pseudo-code for the most important algorithms. All topics are copiously illustrated with color images and worked examples drawn from such application domains as biology, text processing, computer vision, and robotics. Rather than providing a cookbook of different heuristic methods, the book stresses a principled model-based approach, often using the language of graphical models to specify models in a concise and intuitive way. Almost all the models described have been implemented in a MATLAB software package—PMTK (probabilistic modeling toolkit)—that is freely available online. The book is suitable for upper-level undergraduates with an introductory-level college math background and beginning graduate students.


## My Notes


### 11.4.2.5-7 - EM for GMMs - K means

Book calls K-means a "popular variant of  EM algorithm for GMMs"  
"Hard EM"

1. Initialize $m_k$
2. repeat until converged:
   1. Assign each point to closest cluster center. $z_i=\argmin_k || x_i -\mu_k ||_2^2$
   2. Update each cluster center as mean of points in cluster. 
    
   $$\mu_k = \frac{1}{N_k}\sum_{i:z_i=k}x_i$$

"can be
interpreted as a greedy algorithm for approximately minimizing a loss function related to data
compression"

#### Initialization

- Random
- **farthest point clustering** or **k-means++** : pick first at random, rest weighted towards those far away
- speech recognition likes to incrementally grow gmms. split up clusters and dissapear them if they don't behave


# 25 - Clustering

Flat clustering is $O(ND)$. Hierarchical is $O(N^2 \log N)$;

Hamming distance for categorical variables

#### validation

> The validation of clustering structures is the most difficult and frustrating part of cluster
analysis. Without a strong effort in this direction, cluster analysis will remain a black art
accessible only to those true believers who have experience and great courage. — *Jain
and Dubes (Jain and Dubes 1988)*

If $k$ denotes cluster and $c$ denotes class, then **purity of a cluster** is biggest single-class portion of the cluster:

$$p_k \equiv \max_c \frac{N_{kc}}{N_k}$$

**Rand Index** is fraction of clustering decisions which are correct, compared to some reference. Adjusted Rand Index doesn't give credit for what random clustering could do.