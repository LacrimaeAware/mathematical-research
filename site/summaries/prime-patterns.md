# Two constructions for gaps in prime-pattern candidates

How long can an interval contain no starting position for a fixed pattern of numbers that passes all small-prime divisibility tests? This project studies that question through two covering constructions and a Lean formalization of the original argument.

For a pair such as $n,n+2$, these are gaps between **sieve candidates**. [Ziller and Morack's paired Jacobsthal function](https://arxiv.org/abs/1706.00317) gives one connection to prime-pair questions. The gap statements describe the divisibility tests, rather than asserting infinitely many prime pairs.

## The object being measured

Fix an admissible set $H$ of $k\ge2$ integer offsets: modulo each prime, at least one starting residue avoids all forbidden offsets. Let $G_H(x)$ be the longest interval containing no $n$ for which every $n+h$, $h\in H$, has no prime divisor at most $x$.

The following are lower bounds for this same quantity, with positive constants depending on $H$, for sufficiently large $x$.

| Construction | Guaranteed gap scale |
|---|---|
| Elementary covering | $x(\log x)^{k-1}$ |
| Original matching-based argument | $x(\log x)^k/\log\log x$ |
| Rankin-style adaptation derived in this project | $x(\log x)^{2k-1}(\log\log\log x)^k/(\log\log x)^{2k}$ |

The original argument improves the elementary construction by a growing logarithmic factor. The Rankin-style adaptation developed during this project gives a still larger lower bound for every fixed $k\ge2$, using the structure of the fixed shifts.

For $H=\{0,2\}$, the Rankin-style bound is

$$G_H(x)\gg_H x(\log x)^3\frac{(\log\log\log x)^2}{(\log\log x)^4}.$$

## How the constructions fit the literature

The original proof combines sieve estimates with a hypergraph matching argument to cover a long interval of starting positions. Its formal development records the deductions and the interfaces to its two external theorem inputs.

The second construction adapts the classical Rankin strategy, using a Selberg sieve and estimates for smooth-number exceptions. It is a derivation for this fixed-pattern problem recorded in this project, building on methods such as those in [Ford, Green, Konyagin and Tao, *Large gaps between consecutive prime numbers*](https://arxiv.org/abs/1408.4505). It is not a bound quoted verbatim from that paper.

[Ford, Konyagin, Maynard, Pomerance and Tao, *Long gaps in sieved sets*](https://arxiv.org/abs/1802.07604), discusses limitations of its method for higher-dimensional sieves. That broader setting does not have all the fixed-shift structure used in this comparison. The two questions therefore need their hypotheses compared explicitly.

## Formal proof scope

<!-- proof-scope:prime-patterns -->
The original matching-based gap bound is substantially formalized in Lean, conditional on quantitative Selberg and labelled Bennett–Frieze inputs. A separate written Rankin-style adaptation gives the larger bound displayed in the comparison.
<!-- /proof-scope -->

The Lean endpoint is `main_gap_v6_cleanup`. Its recorded kernel audit lists the standard logical axioms and no placeholder-proof axiom. The quantitative Selberg and labelled Bennett–Frieze results enter as explicit hypotheses. This formal audit applies to the original bound.

[Computation and formal proof](methods.md) explains the verification labels used throughout the portfolio.
