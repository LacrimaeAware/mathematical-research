# An infinite family of factorization obstructions

Suppose each factor in a product must stay below a fixed limit. An integer can fail to fit into two factors even when its square fits into four and its cube into six. In algebra, this tests a closure property called **seminormality**: whether knowing that a square and cube belong to a structure forces the original element to belong too. [Bruns, Li and Römer](https://arxiv.org/abs/math/0506221) study this property and its consequences for monoid rings.

## Result

The construction gives an **infinite family of multiplication structures that fail this square-and-cube closure test**. The obstruction persists at every sufficiently large factor limit, however far the limit is increased.

The argument also describes how the missing elements extend into independent families and gives explicit lower bounds for their number. This gives information about both the existence and the extent of the failure in the associated algebra.

## Statement

For every integer $n\ge19624$, there is an integer $N$ that cannot be expressed as the product of two positive integers at most $n$, while $N^2$ is a product of four and $N^3$ a product of six positive integers at most $n$.

Equivalently, the corresponding graded multiplication monoid fails seminormality for every such $n$.

## Approach

The approach treats prime factors as items to distribute among a fixed number of bounded factors. Exact integer searches produced examples where the square and cube fit more efficiently. A scaling argument preserves the obstruction across whole ranges of factor limits.

Finite calculations check that the ranges join up initially; an explicit prime-interval estimate from [Dusart, Proposition 6.8](https://arxiv.org/abs/1002.0442) shows that coverage continues indefinitely. The algebraic part identifies independent directions in which the missing elements can extend, allowing entire families to be counted.

## An open extension: one extra layer

Writing a number as its prime-exponent vector connects bounded factorization to configuration packing, a perspective developed in [Limbach, Scheidweiler and Triesch’s multiplication-table work](https://arxiv.org/abs/2503.23578). The work here gives a precise correspondence and arithmetic examples where a fractional packing plan needs an extra whole layer. Whether one extra layer always suffices is the general round-up conjecture and remains open. It is a further question arising from the factorization study.
