# A bound toward Erdős’s distinct-product problem

[Erdős problem 425](https://www.erdosproblems.com/425) asks how many integers can be chosen from $1$ to $n$ while keeping every product of a fixed number of distinct choices unique. Prime numbers provide a natural starting set. The question is how much larger a set can be.

## Result

Let $A$ be a subset of the integers from $1$ to $n$ whose three-element subsets all have distinct products. Writing $\pi(n)$ for the number of primes up to $n$, the bound is

$$|A|\le\pi(n)+O\!\left(n^{2/3}(\log n)^{1/3}\right).$$

Erdős’s proposed upper bound is $\pi(n)+O(n^{2/3})$. The bound above still has a factor of $(\log n)^{1/3}$ in the error term.

## Condition on the products

The condition includes pairs of subsets that share an element. The bound holds for sufficiently large $n$, with an absolute implied constant.

[Péter Pál Pach’s work on multiplicative 3-Sidon sets](https://arxiv.org/abs/1801.08733) studies the related condition in which all six elements of a product equality are distinct.

## Approach

The proof represents integers by edges joining two factors. Equal products then correspond to patterns in the graph, so restricting those patterns puts a limit on how many integers the set can contain. Keeping track of the sizes and ordering of prime factors sharpens the count.
