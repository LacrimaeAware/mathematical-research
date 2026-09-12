# Prime-built arrays with near-maximal rank

Prime numbers obey exact arithmetic rules, yet some patterns among them behave statistically like random choices. Understanding that behaviour helps describe large families of arithmetic objects. [Koymans and Smith](https://arxiv.org/abs/2405.09311) use a trilinear large-sieve estimate for Rédei symbols in their work on sums of rational cubes and Selmer groups.

The question here is what those estimates imply for arrays built from relationships among primes. Pairwise residue conditions determine which triples are compatible; each compatible triple carries an additional sign. Collecting these signs produces a three-index array, or **tensor**.

## Result

The argument gives distribution bounds for these signs and connects them to rank guarantees. In the associated finite random model, the tensor’s analytic rank is within a constant of the ambient dimension with high probability. Partition and slice rank also have near-maximal lower bounds.

The arithmetic argument transfers the relevant statistical conclusions to compatible prime data in a range where the number of chosen primes grows with their size.

High rank measures resistance to being expressed through a small collection of simpler components. It gives a quantitative way to describe the complexity of the resulting arithmetic patterns.

## The range

For the bias and contraction conclusions, the number of selected primes can grow on the scale of $\sqrt{\log X}$, with a specified constant and a fixed margin below the threshold. All primes lie in $(X,2X]$, and the residue and compatibility conditions are part of the statement.

## Approach

The proof combines finite-field calculations with the external large-sieve estimates. Fixing most prime coordinates leaves a two- or three-variable sum to control; careful counting then preserves the estimate as the array grows.

The written work includes a corrected uniform transfer and a separate internal check of its inequalities and normalization. The large-sieve theorems provide the external arithmetic input.
