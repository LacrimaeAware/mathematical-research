# Measuring how a rare event can disappear

Prime-pattern research often asks whether several rare conditions hold at once. Separate frequency estimates are only part of that question. [Terence Tao’s sieve-theory notes](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/) develop this issue through the problem of counting twin primes.

## Result

The calculation determines how close a probability model can remain to independence after removing a joint event, while preserving both individual event rates.

For two events that each occur 10% of the time, independence gives a 1% chance of both occurring. Redistributing just **2% of the probability mass** removes that joint event completely while leaving both 10% rates intact.

The calculation gives a concrete precision requirement: an error tolerance larger than the cost of removing the target can conceal its total absence. It helped me decide which statistical estimates would be useful to pursue in the prime-pattern work.

## Unequal event rates

For event probabilities $\alpha,\beta$ with $\alpha+\beta\le1$, the law of the two event indicators with zero joint probability has total variation distance $2\alpha\beta$ from independence. Total variation measures the largest change in probability assigned to an event.

The minimum mutual information compatible with absence is asymptotic to $\alpha\beta$ as both rates tend to zero. Mutual information measures the dependence between the two indicators.

## Approach

The argument holds the individual event rates fixed and compares the possible joint distributions with independence. Exact rational calculations make the amount of redistributed probability explicit. Extending the calculation to unequal rates and mutual information connects the examples to a general question: how accurately must an argument control dependence to detect its target event?
