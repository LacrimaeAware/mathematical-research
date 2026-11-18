# Which columns of Pascal’s triangle reach every remainder?

Fix a column $k$ in Pascal’s triangle and read its entries $\binom{n}{k}$ as $n$ increases. Which remainders occur when those entries are divided by a power of a prime?

Column $k=7$ shows why the power matters. Its entries take all three possible remainders modulo $3$. Modulo $9$, the only remainders are $0,1,3,6,8$.

## How common are columns that reach every remainder?

Fix any prime $p$. Among the first $X$ columns, the proportion that attain every remainder modulo every power of $p$ tends to one as $X$ grows. The same column works at every precision, though different entries can supply different remainders.

Sun and Zhang established this property for explicit families of columns and asked which columns have it for a given prime. The density theorem shows how common the property is. A full classification of the exceptional columns remains open in general. [Sun and Zhang, *Binomial coefficients and the ring of p-adic integers*](https://arxiv.org/abs/0812.3089)

## Several primes at once

Choose a fixed $b$ with $0<b<1/25$. For a proportion tending to one of the columns $k\le X$, the conclusion holds simultaneously for every prime $p\le(\log X)^b$. Those columns attain every remainder modulo every integer whose prime factors lie in that range, with arbitrary exponents. Sun and Zhang’s conjecture about columns satisfying the condition at *every* prime up to $k$ remains open.
