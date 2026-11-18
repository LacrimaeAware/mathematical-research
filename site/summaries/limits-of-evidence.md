# Measuring how a rare event can disappear

If two events each occur 10% of the time, independence gives a 1% chance of both occurring. Keeping both individual rates fixed, it takes a change of exactly **2% in total variation distance** to bring the joint probability to zero.

## Unequal event rates

Let the individual probabilities be $\alpha$ and $\beta$, with $\alpha+\beta\le1$. These rates and the requirement that the events never coincide determine the joint distribution of their two indicators. Its total variation distance from independence is $2\alpha\beta$. Total variation is the largest difference in probability that two distributions assign to the same event.

The mutual information of the two indicators under this distribution is asymptotic to $\alpha\beta$ as both rates tend to zero, using natural logarithms.

## Why joint estimates matter

A dependence estimate that allows an error of $2\alpha\beta$ in total variation can be consistent with a joint probability of zero. The distinction between individual and simultaneous conditions also arises in sieve problems involving prime pairs. [Terence Tao’s sieve-theory notes](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/)
