# A common-divisor restriction on recurring prime gaps

Some distances between consecutive primes occur infinitely often. These recurring distances are called **Polignac numbers**. Polignac’s conjecture predicts that every positive even distance recurs; the twin-prime conjecture is the distance-two case.

The question here concerns what the recurring distances must have in common. The argument uses the four-group sieve in [Merikoski’s *Limit points of normalized prime gaps*, Proposition 18 in the corrected version](https://arxiv.org/html/1811.03008v3#S4).

## Result

The four-point selection law gives a restriction on the entire set of recurring gaps:

$$\gcd(\mathrm{POL})\in\{2,4,6\}.$$

All recurring prime gaps are even. This result narrows their **greatest common divisor** to three possibilities, ruling out any shared prime divisor greater than three. It constrains the collection without needing to identify a particular gap that recurs.

## The four-point law

Choose four distinct residue classes $R$ modulo $M$. Assume they leave a class unoccupied modulo every prime dividing $M$. Then a nonzero difference between two of these classes is represented by an infinitely recurring consecutive-prime gap:

$$ (\mathrm{POL}\bmod M)\cap\bigl((R-R)\setminus\{0\}\bigr)\ne\varnothing.$$

The gcd restriction is a consequence of this more general selection law. The written argument and its fixed-tuple application of the external sieve have internal proof review.

## A related modular consequence

Combining the selector with the [finite-group structure theorem](finite-symmetry.md) gives a density bound on residue classes. For $M$ coprime to $42$, at least $\lceil4M/9\rceil$ classes are occupied by zero or a positive or negative recurring gap. This describes how broadly those signed gaps spread around a modular number circle.

## Approach

The construction arranges a fixed set of candidate positions into four groups and uses divisibility conditions to make intervening positions composite. The external sieve places primes in distinct groups. Repeating the argument at larger scales forces a fixed consecutive-prime gap to recur.

This studies actual consecutive-prime gaps. The separate [long-gap construction](prime-patterns.md) studies patterns that survive small-prime divisibility tests.
