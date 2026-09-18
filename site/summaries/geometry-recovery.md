# Recovering hidden boundaries from accurate predictions

A classifier can predict the right labels without making its underlying rule easy to inspect. This project asks when accurate predictions also determine the geometry: a collection of straight boundaries, with the label changing whenever a point crosses one of them.

For Gaussian observations and a fixed number of separated boundaries, the main theorem turns small prediction error into **linearly small coefficient error**, independently of the surrounding dimension. The current manuscript develops this into convex reconstruction from label measurements and recovery guarantees for corrupted samples.

## The coefficient guarantee

Let $P$ be a normalized product of $r$ distinct affine linear factors, with threshold magnitudes at most $T$ and separation at least $\eta$. For a normalized polynomial $Q$ of degree at most $r$, sufficiently small Gaussian sign error $\varepsilon$ implies

$$\|Q-P\|_2\le C(r,T,\eta)\,\varepsilon.$$

The norm is Gaussian $L^2$, equivalently the Euclidean distance between coefficients in an orthonormal Hermite basis. A predictor may use extra coordinates and need not already have the correct factorized form. The constant is uniform in the ambient dimension when $r$, $T$ and $\eta$ are fixed.

## From measurements to boundaries

Low-degree label moments summarize how the labels correlate with polynomial features. Given the complete vector of these moments through degree $r$, a convex reconstruction procedure recovers the coefficients and then the individual boundaries. Moment error $\delta$ and optimization tolerance $\tau$ give recovery error $O_{r,T,\eta}(\delta+\tau)$.

The normalization matters. In a quadratic example with true boundaries at $-1$ and $1$, directly treating the label moments as polynomial coefficients puts the boundaries near $\pm1.32477$ and misclassifies about 13.2% of observations. The convex reconstruction recovers the target from the same exact moments.

Combining the reconstruction with robust moment estimation gives a polynomial-time procedure, for fixed model parameters, with error

$$O_{r,T,\eta}\!\left(\xi\log(1/\xi)^{r/2}+\tau\right)$$

under a small adversarial replacement fraction $\xi$. The robust estimation input comes from [Diakonikolas, Kane and Stewart, *Learning Geometric Concepts with Nasty Noise*](https://arxiv.org/abs/1707.01242); the coefficient and boundary recovery argument is the part developed here.

## What the recent sample analysis adds

The manuscript also compares recovering from moments with fitting the observations directly. If $m$ of $N$ observations are replaced, an empirical sign-error minimizer satisfies a coefficient bound of order

$$O_{r,T,\eta}\!\left(\frac{m}{N}+\frac{M\log N+\log(1/\beta)}{N}\right),\qquad M=\binom{n+r}{r},$$

with probability at least $1-\beta$, in the small-error regime. Here $n$ is the input dimension. This is a statistical guarantee for an empirical minimizer; the polynomial-time construction above uses moments.

A two-boundary example gives a raw-sample lower bound of order $(m+1)/N$. A separate conditioning calculation quantifies how moment inversion becomes less stable as two boundaries approach one another. Together these results distinguish the cost of limited measurements from the cost of noisy observations.

## Proof and related work

Near a true boundary, the label switches sides. The proof turns the probability of missed sign changes into coefficient estimates, then separates the relevant coordinates from the surrounding ones. Convex reconstruction uses the curvature of a Gaussian absolute-value objective.

<!-- proof-scope:geometry-recovery -->
Written coefficient stability, convex moment reconstruction and sample-recovery bounds for fixed complexity and separated, bounded boundaries. The core theorem has a separate internal proof review; the later sampling and conditioning results have recorded self-checks.
<!-- /proof-scope -->

[Matching stability](matching-stability.md) handles boundaries that collide or cancel. [Recovery with unknown label noise](noisy-boundary-recovery.md) gives a measurement threshold for recovering two boundaries together with their error rates.
