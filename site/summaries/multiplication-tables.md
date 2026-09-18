# When repeated multiplication follows a polynomial

Choose a finite set of positive integers $S$. Form all products of exactly $k$ members of $S$, allowing repetition, and count the distinct answers. Although products collide in complicated ways, the count eventually agrees exactly with a polynomial in $k$.

The question is **how long it takes to reach that polynomial regime**. This is the arithmetic stabilization question raised in Section 6 of [Limbach, Scheidweiler and Triesch, *Effective Khovanskii, Ehrhart Polytopes, and the Erdős Multiplication Table Problem*](https://arxiv.org/html/2503.23578v1).

## Result

Write $K(S)$ for the least nonnegative onset after which the polynomial formula holds. For integer alphabets drawn from $\{1,\ldots,n\}$, the worst possible onset has the sharp scale

$$\max_{\varnothing\ne S\subseteq\{1,\ldots,n\}}K(S)
=\exp\!\left(\Theta\!\left(\frac{n^{1/3}}{\log n}\right)\right).$$

This includes the improved upper bound

$$K(\{1,\ldots,n\})\le\exp\!\left(O\!\left(\frac{n^{1/3}}{\log n}\right)\right)$$

for the **complete multiplication table**. The matching lower constructions use selected subsets $S$; they establish sharpness across all alphabets, rather than a lower bound of the same order for the complete table.

For positive rational alphabets whose reduced numerators and denominators are at most $n$, the corresponding worst-case scale is

$$\exp\!\left(\Theta\!\left(\frac{\sqrt n}{\log n}\right)\right).$$

## Why arithmetic changes the bound

Writing each number as its vector of prime exponents turns multiplication into addition. Equal products become integer relations between these vectors. The proof localizes the arithmetic structure of minimal relations and bounds their size; carefully chosen chains supply the lower constructions.

The conversion from relation bounds to eventual polynomial behavior uses established tools, including [Granville, Smith and Walker's sumset stabilization theorem](https://arxiv.org/abs/2406.03275) and Hilbert-series arguments. The additional step here is the sharp control of the relations arising from bounded integers and rationals.

## Literature connection and proof

The upper bound addresses the arithmetic-specific onset question in the multiplication-table literature. [Sabuncu and Táfula's work on large-dimensional multiplication tables](https://arxiv.org/abs/2608.16163) provides a recent comparison: this result improves the stabilization bound, while their main asymptotic counting result is a different conclusion.

<!-- proof-scope:multiplication-tables -->
Complete written stabilization argument, a separate internal review and exact finite checks. The sharp lower bound concerns selected alphabets; the upper bound also applies to the complete multiplication table. The proof uses established circuit-to-stabilization and Hilbert-series results.
<!-- /proof-scope -->

[Factorization obstructions](factor-packing.md) studies another feature of the same multiplication structures: products missing from a bounded factorization even when their powers fit.
