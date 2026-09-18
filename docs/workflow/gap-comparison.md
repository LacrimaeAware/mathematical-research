# Fixed-pattern gap comparison: public example source

This is an excerpt for the workflow demonstration, reviewed September 17, 2026.
The full public note supplies definitions, citations and proof scope:
https://lacrimaeaware.github.io/mathematical-research/notes/prime-patterns.html

For a fixed admissible integer constellation H of size k >= 2, the original
matching construction gives G_H(x) >>_H x(log x)^k / log log x.
The Lean endpoint main_gap_v6_cleanup uses quantitative Selberg and labelled
Bennett-Frieze results as explicit inputs.

The written Rankin adaptation developed in this project gives
G_H(x) >>_H x(log x)^(2k-1) (log log log x)^k / (log log x)^(2k).
It combines a fixed-dimensional Selberg sieve, a smooth-number exception
estimate, and a covering construction using the fixed integer shifts.
Dividing this scale by the original gives
(log x)^(k-1) (log log log x)^k / (log log x)^(2k-1), which tends to infinity
for each fixed k >= 2. Both therefore imply the original gap scale.

The larger formula is a derivation made in this project, not a theorem quoted
verbatim from the cited literature. The priority of that application remains
an open comparison. The original Lean endpoint covers the matching route.
