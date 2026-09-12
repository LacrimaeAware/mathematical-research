# Recovering hidden boundaries from accurate predictions

A classifier can predict the right labels without making its reasoning easy to inspect. A more mathematical question is whether accurate predictions can force it to recover the underlying geometry. Work such as [Diakonikolas, Kane and Stewart’s *Learning Geometric Concepts with Nasty Noise*](https://arxiv.org/abs/1707.01242) studies how geometric rules can be learned from imperfect observations.

The model considered here uses rules formed from several straight boundaries: the label changes whenever a point crosses one of them. The observations follow a Gaussian distribution.

## Result

The theorem establishes that, under explicit separation and degree conditions, **small prediction error forces small coefficient error**. The constant in this guarantee is independent of the number of surrounding coordinates. A predictor may use extra coordinates and need not already have the correct factorized form.

This connects getting the answers right to recovering the mathematical rule that produced them. Related results give a convex reconstruction procedure from low-degree label measurements, followed by recovery of the individual boundaries.

## The guarantee

Let $P$ be a normalized product of $r$ distinct affine linear factors, with bounded thresholds and separation at least $\eta$. For a normalized polynomial $Q$ of degree at most $r$, sufficiently small Gaussian sign error $\varepsilon$ implies

$$\|Q-P\|_2\le C(r,T,\eta)\,\varepsilon.$$

Here $T$ bounds the thresholds. In an orthonormal Gaussian polynomial basis, this norm measures the distance between the complete coefficient vectors. The guarantee holds with $r$, $T$ and $\eta$ fixed as the ambient dimension changes.

## Related results

[Matching stability](matching-stability.md) handles boundaries that collide or cancel, giving a linear bound on how closely their parameters must pair. [Recovery with unknown label noise](noisy-boundary-recovery.md) identifies a precise information threshold: third-degree measurements can leave two models indistinguishable, while fourth-degree measurements recover both boundaries and their error rates.

## Approach

Near a true boundary, the target label switches sides. A predictor that misses the boundary must make mistakes on a region of positive probability. The proof turns that observation into coefficient estimates, then separates the relevant coordinates from the surrounding ones.

The work includes written proofs, an internal review of the coefficient theorem, and numerical recovery experiments. The dependence on the number and separation of boundaries remains an important question for practical computation.
