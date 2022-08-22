---
parent: Papers
---

# The paradox of information and voter turnout

[Springer html link](https://link.springer.com/article/10.1007/s11127-015-0288-1)

## BibTeX
```
@article{mcmurray2015paradox,
  title={The paradox of information and voter turnout},
  author={McMurray, Joseph},
  journal={Public Choice},
  volume={165},
  number={1},
  pages={13--23},
  year={2015},
  publisher={Springer}
}
```

## Abstract

> The most prominent explanation for the paradox of voter turnout is that citizens are willing to bear the cost of voting because they perceive a benefit (e.g., fulfilling a civic duty or expressing themselves) that is independent of the election outcome. However, a separate literature highlights the empirical importance of information for voter participation, and existing explanations for this are that uninformed citizens either expect smaller benefits from voting, or defer strategically to peers who know more. This paper simply points out that, while either of these theories offers a plausible explanation for the importance of information, neither is robust if the motivation for voting is unrelated to the election outcome. This is because citizens with positive net voting costs should abstain, no matter how well informed, while those with negative net voting costs should vote, no matter how poorly informed. Thus, the purported resolution to the turnout paradox raises a new paradox of information and voter turnout. Intuitively, the quality of a vote should matter only if the vote is somehow instrumental, suggesting that future work should continue to explore instrumental rationales for voting.

## My Notes



### Lit review

> citizens who are better-informed about
political issues and exhibit greater confidence in their opinions tend to vote more fre-
quently than those who lack information. (Geys 2006)

Education is most important determinant of turnout. 
Maybe because ignorant want to not dilute the effect of better informed peers with shared values.

Other theory is that some people just like voting. But in large elections, anyone who likes voting should vote, and we shouldn't see the info effect.

### Model

Following *Large Poisson Games* (Myerson 98),

- N citizens
    - People don't know how many
    - But common knowledge that $N$ drawn from Poisson with mean $n$.
- Collectively vote on policy in set $\chi=\{-1,1\}$
- Flip a coin to determine the popular policy $z\in\chi$.
- Person $i$ benefits most from policy $z_i\in\chi$
    - They get utility $u_H$ if this policy is passed, and $u_L$ otherwise.
    - The probability that the individual benefits from the popular policy is  $P(z_i=1 | z=1)=\frac{1+\rho}{2}=P(z_i=-1 | z=-1)$, independently drawn.
    -  The probability they don't is $P(z_i=1 | z=-1)=\frac{1-\rho}{2}=P(z_i=-1 | z=1)$
    -  $\rho\in[0,1]$ is the coorelation between $z,z_i$
       -  If $\rho=1$, everyone has same good policy (common value, Condorect 1785)
       -  If $\rho=0$, everyone has coinflip best. (private value)
    -  The coorelation between $z_i,z_j$ is $\rho^2$, and the popular policy benefits the majority with expected size $\frac{1+\rho}{2}$.
- People don't actually know which policy is best for them.
    - Each person has expertise $q_i\in[0,1]=Q$ drawn iid from distribution $F$.
    - They get signal $s_i\in\chi$ corelated with $z_i$. Better corelation with more expertise.
        $$Pr(s_i=z_i)=\frac{1+q_i}{2}$$
- Each person can vote for either option, or they can abstain.
    - If they vote, they incur cost $\tilde c_i$ but recieves pyschological benefit $d_i$
    - Net cost $c_i\equiv \tilde c_i - d_i$ can thus be positive or negative.
    - Each person's net cost is drawn iid from continuous dist $G$ with support $[\underline c, \overline c]=C$.
- The distributions of $c_i,q_i,s_i$ are common knowledge, but each draw is private info.

If you vote at all, dominant strategy is to vote for candidate that you think is best, $s_i$. 
So the only really choice is to vote or abstain.

- A strategy $\sigma$ is a mapping that specifies an action for every expertise level and net voting cost. And $\Sigma$ is the set of such strategies.
    
    $$\sigma:[0,1]\times[\underline c, \overline c] \to \{0,1\} $$

    $$\sigma:expertiseQ\times netCostC \to \{abstain,vote\} $$
    

Votes are cast simultaneously, winner $w\in\chi$ is chosen by simple majority, ties broken by coin toss.

Expected utility for person $i$ is then 

$$Eu_i = u_H \Pr [w=z_i] + u_L \Pr [w\neq z_i] - c_i \sigma(q_i,c_i)$$

### Bayesian Nash Equilibrium

Following Myerson 98, equilibrium will be symmetric. 

If all opponents play according to some strategy $\sigma\in\Sigma$, then $\sigma$ is a Bayesian Nash Equilibrium if it is the best response to everyone else playing that strategy.

The probability that any two people $i,j$ benefit from the same strategy is 

$$\phi = \frac{1+\rho}{2}\frac{1+\rho}{2} + \frac{1-\rho}{2}\frac{1-\rho}{2} =\frac{1+\rho^2}{2}$$

Then given strategy $\sigma$, the expected portion of person i's peers who will vote for $z_i$ is 

$$v_+ = \int_0^1 \int_{\underline c}^{\overline c} \left[ \phi\frac{1+q}{2} + (1-\phi)\frac{1-q}{2} \right] \sigma(q,c) \ \ dG(c)dF(q)$$


Or in other words, the integrand reprsents that a person with cost $c$ and expertise $q$ will vote in a way that benefits you, if:
- They actually bother to vote at all ($\sigma$)
- and either:
    - they also benefit and vote correctly
    - they don't benefit from the policy, but mistakenly vote for it anyways.

Likewise, the expected share that votes against $z_i$ is 

$$v_- = \int_Q \int_C \left[ \phi\frac{1-q}{2} + (1-\phi)\frac{1+q}{2} \right] \sigma(q,c) \ \ dG(c)dF(q)$$

Note that $\rho\geq 0$ so $\phi \geq \frac{1}{2}$ and so $v_+ \geq v_-$, with equiality iff $\rho=0$

By **decomposition property** of Poisson games (TODO), number of votes for and against $z_i$ are Poisson random variables, with means $nv_+$ and $nv_-$.

The probability of a particular set of votes ($n_+$ votes for $z_i$ and $n_-$ against) being cast is 

$$\psi (n_+,n_-) = \frac{ {(nv_+)}^{n_+} e^{-nv_+}}{n_+!} \cdot \frac{(nv_-)^{n_-} e^{-nv_-}}{n_-!} = \frac{ {n}^{n_-+n_+} e^{-n(v_-+v_+)}}{n_-!n_+!} v_+^{n_+} v_-^{n_-}$$

Because a poisson pmf is $\frac{\lambda^k e^{-\lambda}}{k!}$ 

The probability that $z_i$ wins and loses by a margin of $m\geq 0$ votes is 

$$\pi_m = \Sigma_{k=0}^\infty \phi(k+m,k)$$

$$\pi_-m = \Sigma_{k=0}^\infty \phi(k,k+m)$$


And the proababilty that $z_i wins the election is

$$Pr(w=z_i)=\frac{1}{2}\pi_0 + \sum_{m=1}^\infty \pi_m$$

**Environmental equivalence** property of Poisson games means each individual can reinterpret $N_+$ and $N_-$ as number of votes cast by their peers. 
Your individual vote can add one to either total. So if you vote for $z_i$, it will win with probability 

$$\frac{1}{2}\pi_{-1} + \sum_{m=0}^\infty \pi_m$$

So if you vote for $z_i$, you'll increase it's chance of winning by 

$$P_+ = \frac{1}{2}\pi_{-1} + \sum_{m=0}^\infty \pi_m - \frac{1}{2}\pi_0 - \sum_{m=1}^\infty \pi_m = \frac{\pi_0+\pi_{-1}}{2}$$

And if you vote for against it, you'll reduce its chance of wining by 

$$P_- = \frac{1}{2}\pi_0 + \sum_{m=1}^\infty \pi_m - \frac{1}{2}\pi_{1} - \sum_{m=2}^\infty \pi_m +  = \frac{\pi_1+\pi_{0}}{2}$$

The expected benefit of voting is thus a combination of several things:
- The chance that the vote is pivotal (P_+ or P_-)
- The chance you vote for the correct policy ($\frac{1+q_i}{2}$)
- The difference in benefits you get between outcomes ($u_H-u_L$)
- The net cost of voting $c_i$

Expected benefit of of voting is given by

$$\Delta Eu_i = \left[ \frac{1+q_i}{2} P_+ - \frac{1-q_i}{2} P_-  \right] [u_H - u_L] - c_i$$

This function is increasing in $q$ but decreasing in $c$ so you are more likely to vote if:
- You are better informed
- It's easy for you to vote
- You get some strong psychological benefit from voting.


Cost Threshold Strategy
: $\sigma$ is a cost threshold strategy if there is some positive, increasing threshold function $\tau$ such that a citizen votes iff $c\leq \tau(q)$

For example, to vote iff your expected benefit is positive is a CTS with threshold 

$$\tau(q) = \left[ \frac{1+q}{2} P_+ - \frac{1-q}{2} P_-  \right] [u_H - u_L]$$

Can't apply fixed point theorems to best response to get equilibrium,  sadly. They use a technique from [Oliveros 13](https://www.sciencedirect.com/science/article/abs/pii/S0022053113000288) by applying fixed point to pivot probabilities $P_+,P_-$.



Proposition 1
: $\sigma_{br}$ is a best response to $\sigma$ only if $\sigma_{br}$ is a cost-threshold strategy, with threshold as given by 
    
    $$\tau(q) = \left[ \frac{1+q}{2} P_+ - \frac{1-q}{2} P_-  \right] [u_H - u_L]$$
    
    Moreover, there exists a cost threshold strategy $\sigma^*$ which is a Bayesian Nash Eq

$\tau(q)$ above maps pivot probabilities to new pivot probabilites. And a fixed point exists by Brouwer's theorem.


Note that if $\rho=0$, (private values) $\phi=1-\phi$, so expected votes same for both policies. Then Our special $\tau$ is positive as long as $q_i>0$ because $P_+ = P_-$.

But with $\rho>0$, we expect that our policy will be correlated with others' and so $P_+ < P_-$. So $\tau(q)<0$ for low enough $q$.

### Large elections

What is behavior as $n\to\infty$? 

$\tau^*_n$ converges uniformlu to zero as $n\to\infty$

