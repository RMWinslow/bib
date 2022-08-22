---
parent: Papers
---

# Cool to be smart or smart to be cool? Understanding peer pressure in education

[non-open published link](https://academic.oup.com/restud/article-abstract/86/4/1487/5003980)

[NBER link](https://www.nber.org/papers/w23020)

## BibTeX
```
@article{bursztyn2019cool,
  title={Cool to be smart or smart to be cool? Understanding peer pressure in education},
  author={Bursztyn, Leonardo and Egorov, Georgy and Jensen, Robert},
  journal={The Review of Economic Studies},
  volume={86},
  number={4},
  pages={1487--1526},
  year={2019},
  publisher={Oxford University Press}
}
```

## Abstract

> Concerns about social image may negatively affect schooling behavior. We identify two potentially important peer cultures: one that stigmatizes effort (thus, where it is “smart to be cool”) and one that rewards ability (where it is “cool to be smart”). We build a model showing that either may lower the takeup of educational activities when takeup and performance are potentially observable to peers. We design a field experiment allowing us to test whether students are influenced by these concerns at all, and then which they are more influenced by. We examine high schools in two settings: a low-income, high minority share area and a higher-income, lower minority share area. In both settings, peer pressure reduces takeup of an SAT prep package. We show that this is consistent with a greater concern for hiding effort in the lower-income school, and a greater concern with hiding low ability in the higher-income schools.


## My Notes


> “Better to remain silent and be thought a fool than to speak out and remove all doubt”  
>  - Abe Lincoln

This paper asks "Okay, but what if that attitude is hurting student engagement?

---

> More
recently, Bursztyn and Jensen (2015) find that schooling investments, including both takeup of a
free SAT prep course and effort exerted in practicing for a high-stakes high school exit exam, are
greatly, and negatively, affected when those behaviors are observable to peers.

> As in the classic signaling
model of Spence (1973), the psychic cost of studying is assumed to be lower for high economic types.


---

Students have social skill (cool) and economic skill (smarts). 
Being seen as cool or smart is desirable. 
But some cool students may deliberately underperform on tests to signal their coolness.
Then mediocre students may also do so to disguise their middling economic skill as a signal of coolness.

### Experiment:

Lottery with chance $p$ to win SAT prep package, but your choice to signup and results are public.
- If students avoid test prep because they want to signal coolness by not studying, higher $p$ should increase signup rate because the cost is signing up, not getting a bad result.
- If students avoid it because they want to hide their low test ablity, higher $p$ should decrease signups because it would reveal the fake smarties?

Feels unintutive to me, but I have to admit it's a clever setup. And they do discuss a bunch of other possible factors.

Signup rates are found to be lower in all schools when the decision is public. 
High achieving schools (as categorized in pre-registration) had fewer signups as $p$ increased, with low-grade students being most affected.
Low achieving schools had more signups.
In both cases, signups decreased most among students who said they care about popularity.
Matches their hypothesis.

Additional surveys suggested that popularity hit from effort does indeed come from perception of people who study as being unfun to be around.


---

### Model

#### Playing it cool

- continuum of students
- can particpate in educational activity (my shorthand: studying) that costs time, gives benefit $b$
    - $s_i = 1$ indicates participation, $=0$ indicates non-participation
- Opportunity cost of student's time is private info $c_i$
    - Assume this reflects student's social type.
    - Cool kids have opportunity cost $c_i = h > b$
    - Dweebs have opportunity cost $c_i = l < b$ 
- Students value popularity. Get benefit $\lambda_s$ from being seen as cool.
    - Students care about expected value of being seen as cool.


Thus utility is given by

$$(b-c_i) s_i + \lambda_s \Pr (c_i = h | Info)$$

If there is no public info, then students will study iff $b > c_i$.

If there is public info, no cool kid will study.
And if portion $q$ are dweebs, and portion $r$ of dweebs study, then 
- benefit of signing up is $b-l$
- cost of signing up is $\lambda_s \frac{1-q}{1-qr}$
- all dweebs study if $\lambda_s \leq b-l$
- no dweebs study if $\lambda_s \geq \frac{b}{1-q}$
- some dweebs, $1-\frac{\lambda_s}{b}$ study otherwise.

#### Signalling smarts

- uniform distribution of economic type $a_i$ on interval $[0,1]$
    - higher econ type is smarter student.
    - independent of social type.
- Now no penalty for being a dweeb, $\lambda_s = 0$
- But social reward for being smart $\lambda_e$
- studying reveals your ability
    - also public info just that you sign up.


Thus utility is given by

$$(b-c_i) s_i + \lambda_e E ( E (a | Info) | a_i )$$


**Important:** They assume $h > b + \lambda_e$, which prevents cool kids from studying to prove how smart they are. This would lead to positive peer effects instead of negative ones.

In this setting, dweebs study if they're smart enough.
- If $\lambda_e \leq 2b$, then even the thickest dweeb with $a_i = 0$ will study.
    - This is because not studying pools the dweeb with the cool kids who have expected smarts of $1\over 2$
- Otherwise, there is a cutoff in smarts $t$ where dweebs study iff $a_i > t$.
    - The cutoff is given by the indiffernce condition:

$$b-l +\lambda_e t = \lambda_e (\frac{1-q}{1-q+qt} \frac{1}{2} + \frac{qt}{1-q+qt} \frac{t}{2} )$$

$$benefitOfStudy = benefitOfSlack$$

$$b-l + lambda_e t = \lambda_e (\frac{cools}{cools+thickDweebs} \frac{1}{2} + \frac{thickDweebs}{cools+thickDweebs} \frac{t}{2} )$$

*I think there might be some typos in their equations. If not, I am confused.*


#### Model with both concerns and a lottery

- students who sign up have iid chance $p$ of actually getting to participate in the educational activity.
    - If wins lottery, gets $b$, pays $c_i$, reveals results
    - If loses, no benefit, no cost, reveals signup but not result

Utility:


$$(b-c_i) s_i  p + \lambda_s \Pr (c_i = h | Info) + \lambda_e E ( E (a | Info) | a_i )$$

Expected utility for a dweeb who signs up is 

$$p(b-l) + \lambda_e (p a_i + (1-p) \frac{1+t}{2})$$


Expected utility for anyone who doesn't is

$$\lambda_s \frac{1-q}{1-q+qt} + \lambda_e (\frac{1-q}{1-q+qt} \frac{1}{2} + \frac{qt}{1-q+qt} \frac{t}{2})$$


There is a threshold $t$ such that dweebs sign up if they are above the threshold and don't if they are below it.


---

Figure 1 is really interesting.

Clearly shows how a higher value placed on being seen as smart can increase or decrease the partipication of students in study activities. 
If being cool is highly valued, then more social value on signalling smartness increases participation.
But if being cool is low value, then reduced participation from emphasis on signalling smartness.

On the other hand, higher value of coolness always 

