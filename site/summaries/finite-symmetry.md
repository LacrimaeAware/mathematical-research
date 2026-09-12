# A seven-part pattern forced by symmetry

How few connections can a network have if every four points must contain a connected pair? This is a version of a question from Turán’s extremal graph theory. [Li and Yang](https://arxiv.org/abs/2606.29284) study it for networks where a group supplies the same connection rule at every point, including what changes beyond groups of prime size.

## Result

The theorem establishes that, under a **4/9 density threshold** and the group assumptions below, the network must contain a pattern of **seven repeating classes**. Each class is connected internally and to its two neighbors around a cycle.

This identifies an organization forced by the connection rule and sparsity. It helps explain why the available subgroup structure matters when moving from prime-sized systems to more general finite groups.

## Group assumptions and conclusion

Let $G$ be a finite abelian group whose size is divisible by neither 2 nor 3. Let $D=-D$ contain zero, and connect distinct $x,y\in G$ when $x-y\in D$. Suppose every four vertices contain a connected pair and $|D|<4|G|/9$.

There is an index-seven subgroup $H$ and a nonzero $c\in G/H$ such that, for the quotient map $\pi$,

$$\pi^{-1}\{0,c,-c\}\subseteq D.$$

The density counts the allowed differences in $D$, including zero.

## Approach

The proof translates the network condition into restrictions on differences between group elements. Structure theorems from additive combinatorics narrow the possible arrangements to repeating classes. The remaining case analysis identifies which arrangements are compatible with the density bound, leading to the seven-class pattern.

The Lean development includes a density constraint and the exclusion of a possible five-class case. Python calculations provide small examples against which to check the structural picture.
