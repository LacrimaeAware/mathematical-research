# Prime-built arrays with near-maximal rank

Can relationships among primes produce arrays that behave like random data? Pairwise residue conditions determine which triples are compatible; each compatible triple carries an additional sign. Collecting these signs produces a three-index array, or **tensor**.

[Koymans and Smith](https://arxiv.org/abs/2405.09311) use a trilinear large-sieve estimate for Rédei symbols in their work on sums of rational cubes and Selmer groups. The question here is what those estimates imply for these arrays.

## Result

The argument gives distribution bounds for these signs and connects them to rank guarantees. In the associated finite random model, the tensor’s analytic rank is within a constant of the ambient dimension with high probability. Partition and slice rank also have near-maximal lower bounds.

The arithmetic argument transfers the relevant statistical conclusions to compatible prime data in a range where the number of chosen primes grows with their size.

High rank measures resistance to being expressed through a small collection of simpler components. It gives a quantitative way to describe the complexity of the resulting arithmetic patterns.

## The range

For the bias and contraction conclusions, the number of selected primes can grow on the scale of $\sqrt{\log X}$, with a specified constant and a fixed margin below the threshold. All primes lie in $(X,2X]$, and the residue and compatibility conditions are part of the statement.

## Approach

The proof combines finite-field calculations with the external large-sieve estimates. Fixing most prime coordinates leaves a two- or three-variable sum to control; careful counting then preserves the estimate as the array grows.

## Further arithmetic application

A later written deduction studies quadratic twists $E_n:y^2=x^3-n^2x$. Take $n$ to be a product of $k$ distinct primes in $(X,2X]$, each congruent to $1$ modulo $8$ and a quadratic residue modulo every other selected prime. Uniformly for $2\le k\le\sqrt{\log X}/32$, the deduction gives a proportion at least $1/3-o(1)$ of these products with rank zero and

$$\operatorname{Sha}(E_n/\mathbb Q)[2^\infty]\cong(\mathbb Z/2\mathbb Z)^{2k}.$$

Here the group records an arithmetic obstruction to passing from local solutions to rational ones. The consequence connects the sign calculations to a concrete invariant of elliptic curves. Its proof combines a structured matrix calculation with named external Cassels-pairing and analytic inputs.

The accompanying comparison distinguishes these growing-rank families from the fixed-rank limiting distributions in [Smith's quadratic-twist work](https://arxiv.org/abs/2207.05143).
