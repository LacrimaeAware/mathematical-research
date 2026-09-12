# A bound toward Erdős’s distinct-product problem

[Erdős problem 425](https://www.erdosproblems.com/425) asks how many integers can be chosen from $1$ to $n$ while keeping every product of a fixed number of distinct choices unique. Prime numbers provide a natural starting set. The question is how much larger a set can be.

## Result

For products of three elements, the proof gives an upper bound with the same $n^{2/3}$ power as Erdős’s proposed allowance beyond the prime count, multiplied by a logarithmic factor.

Writing $\pi(n)$ for the number of primes up to $n$, the bound is

$$|A|\le\pi(n)+O\!\left(n^{2/3}(\log n)^{1/3}(\log\log n)^{2/3}\right).$$

Erdős’s target is $\pi(n)+O(n^{2/3})$. The remaining difference is the factor $(\log n)^{1/3}(\log\log n)^{2/3}$ in the allowance beyond the primes.

## Condition on the products

Different three-element subsets of $A$ must have different products; the two subsets may overlap. The bound holds for sufficiently large $n$, with an absolute implied constant.

[Péter Pál Pach’s work on multiplicative 3-Sidon sets](https://arxiv.org/abs/1801.08733) studies the related condition in which all six elements of a product equality are distinct. The overlap condition is part of the formulation used here.

## Approach

The proof represents integers by edges joining two factors. Equal products then correspond to patterns in the graph, so restricting those patterns puts a limit on how many integers the set can contain. Keeping track of the sizes and ordering of prime factors sharpens the count.

The argument combines this graph bound with estimates on the available factorizations. Exact Python checks support the finite combinatorial steps.
