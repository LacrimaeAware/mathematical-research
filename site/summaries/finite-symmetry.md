# A seven-part pattern forced by symmetry

How few connections can a network have if every four points must contain a connected pair? This is a version of a question from Turán’s extremal graph theory. [Li and Yang](https://arxiv.org/abs/2606.29284) study it for networks where a group supplies the same connection rule at every point, including what changes beyond groups of prime size.

## Result

The theorem establishes that, under a **4/9 density threshold** and the group assumptions below, the network must contain a pattern of **seven repeating classes**. Each class is connected internally and to its two neighbors around a cycle.

## Group assumptions and conclusion

Let $G$ be a finite abelian group whose size is divisible by neither 2 nor 3. Let $D=-D$ contain zero, and connect distinct $x,y\in G$ when $x-y\in D$. Suppose every four vertices contain a connected pair and $|D|<4|G|/9$.

There is an index-seven subgroup $H$ and a nonzero $c\in G/H$ such that, for the quotient map $\pi$,

$$\pi^{-1}\{0,c,-c\}\subseteq D.$$

The density counts the allowed differences in $D$, including zero.

## An exact extremal consequence

If $7$ divides $N=|G|$ and $N$ is coprime to $6$, the largest possible degree of a $K_4$-free Cayley graph on $G$ is $4N/7$. The largest possible edge count is $2N^2/7$. Every maximizer is obtained by pulling back the complement of a seven-cycle from a quotient of order seven.

## Connection to earlier work

The complementary graph has degree $N-|D|$, so the threshold above corresponds to degree greater than $5N/9$. At the same threshold, Illingworth gives a graph homomorphism to the complement of a seven-cycle when every vertex neighborhood is bipartite. The Cayley result starts from a $K_4$-free graph on the specified abelian group and identifies the seven classes as cosets of a subgroup. [Illingworth, Theorem 3.1(b)](https://doi.org/10.1017/S0963548322000050)

## Proof scope

<!-- proof-scope:finite-symmetry -->
Written proof of the 4/9 structure theorem and its exact extremal consequences in the specified finite abelian groups. Specific finite density, quotient and fibre deductions are also checked in Lean.
<!-- /proof-scope -->
