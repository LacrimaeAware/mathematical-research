# Longer gaps between prime-pair candidates

The twin-prime conjecture asks whether pairs of primes two apart continue forever. One related question is how far apart their **candidates** can be: pairs that pass divisibility tests by all primes up to a chosen cutoff. [Ziller and Morack’s work on the paired Jacobsthal function](https://arxiv.org/abs/1706.00317) connects bounds on these gaps to conjectures about prime pairs.

## Result

The construction establishes a lower bound for the longest gaps between candidates, improving the elementary construction by a factor growing like $\log x/\log\log x$, where $x$ is the prime cutoff. The result also applies to larger fixed patterns of numbers.

For pairs $n,n+2$, the guaranteed gap grows from the elementary scale $x\log x$ to

$$\frac{x(\log x)^2}{\log\log x}.$$

These gaps measure how long divisibility obstructions can persist. This helps describe the limits of what a prime-search sieve can leave behind.

## The general bound

Let $H$ be a fixed set of $k\ge2$ integer offsets that leaves at least one possible starting residue modulo every prime. Let $G_H(x)$ be the longest interval with no starting integer $n$ for which all $n+h$, $h\in H$, avoid prime divisors at most $x$. Then

$$G_H(x)\gg_H\frac{x(\log x)^k}{\log\log x}.$$

The notation means a lower bound up to a positive constant depending on $H$, for all sufficiently large $x$.

## Approach

The proof treats the gap problem as covering a stretch of consecutive starting positions with divisibility restrictions. The difficulty is coordinating restrictions from different primes so that they cover a long stretch efficiently. Sieve estimates control the positions still available, and a combinatorial matching result helps organize the remaining coverage.

<!-- proof-scope:prime-patterns -->
The long-gap construction is substantially formalized in Lean, including its final endpoint. Two external theorem interfaces remain: quantitative Selberg and the labelled Bennett–Frieze matching result. The written manuscript supplies the extension argument.
<!-- /proof-scope -->
