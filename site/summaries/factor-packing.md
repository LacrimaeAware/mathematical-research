# Factorization obstructions and their algebraic consequences

An integer can fail to fit into two bounded factors even when its square fits into four and its cube into six. This tests an algebraic closure property called **seminormality**: whether including an element's square and cube forces the element itself to be included.

The project develops explicit obstructions in multiplication-table structures, counts families of missing elements, and connects arithmetic repairs to the depth of the associated rings.

## A persistent square-and-cube obstruction

For every integer $n\ge19624$, there is an integer $N$ that cannot be expressed as the product of two positive integers at most $n$, while $N^2$ is a product of four and $N^3$ a product of six positive integers at most $n$.

The construction treats prime factors as items to distribute among bounded factors. Exact searches provide initial examples; scaling and [Dusart's explicit prime-interval estimate, Proposition 6.8](https://arxiv.org/abs/1002.0442), extend the coverage indefinitely.

## Larger families of missing elements

A later calculation corrects and extends a three-prime example from [Limbach, Scheidweiler and Triesch's multiplication-table paper](https://arxiv.org/abs/2503.23578). It gives a family of holes whose size satisfies

$$H_n\sim\frac{15}{4}\frac{n^{31/30}}{(\log n)^3}.$$

The corrected construction applies for $n\ge2^{120}$. Using the established algebra of seminormal monoid rings, these missing elements produce independent families in associated Picard-group calculations over every field.

## A separate depth result

The arithmetic repair argument also controls depth, an invariant measuring regularity in a commutative ring. For the graded multiplication-table rings, the asymptotic deficit between dimension and depth is at least about **6.43% of dimension**:

$$\liminf_{n\to\infty}\frac{\operatorname{dim}R_n-\operatorname{depth}R_n}{\operatorname{dim}R_n}\ge0.0643474512866896.$$

This conclusion uses the pattern of ways a missing factorization can be repaired. The translation from that arithmetic pattern to ring depth builds on classical monoid-ring theory, including [Bruns, Li and Römer](https://arxiv.org/abs/math/0506221).

## Further question and proof scope

Prime-exponent vectors also connect the problem to configuration packing. The work gives a correspondence and examples where a fractional plan needs an extra whole layer. Whether one extra layer always suffices is the general round-up question.

<!-- proof-scope:factor-packing -->
Written arithmetic repair and depth arguments with recorded internal reviews. A separate, self-checked correction of an earlier multiplication-table example gives larger families of missing elements and associated Picard-group consequences.
<!-- /proof-scope -->
