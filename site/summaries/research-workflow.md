# Current mathematical questions

## How many observations reveal shared factors when some rows are corrupted?

Several measurements can vary together because of a few hidden factors. Suppose the number of factors and the center are known, background noise can differ by coordinate, and a small fraction of whole observations can be replaced. Even among the clean observations, magnitudes can vary so widely that a covariance matrix need not exist. The target is the shape of the distribution, which describes the relative spread in different directions.

For independent elliptical observations, a recovery theorem separates the factor component from the diagonal noise when the factor directions are sufficiently spread out, the noise is bounded above and below, and a positive lower bound on factor strengths is known. If every row is eligible for replacement, the initial estimate still carries a sample cost quadratic in the number of coordinates at fixed accuracy. With an additional clean sample whose size grows linearly with dimension, a separate theorem avoids that quadratic cost. Can the same saving be obtained without a trusted sample when the factor strengths are unequal?

## How much can a distribution change when two draws are combined?

On a group, a probability distribution can stay exactly the same when two independent draws are multiplied. A stability theorem bounds the distance to such a distribution when the change under multiplication is very small. On locally compact groups the leading constant is sharp. How far can the range of errors be enlarged? [Convolution stability](convolution-stability.md)

## How many labels are needed to recover Gaussian decision boundaries?

Suppose a label flips whenever a point crosses one of a fixed number of hidden hyperplanes. An adversary can replace a small fraction of the observations, including both the points and their labels. For separated boundaries with bounded offsets, a recovery theorem controls the errors in the coefficients, the boundary locations and the predictions.

When there are $r\ge2$ boundaries in $d$ dimensions, the exponent of $d$ in the labeled sample bound is $\lceil r/2\rceil$, up to logarithmic factors with other parameters fixed. The procedure also uses simulated, unlabeled Gaussian points and more computation than the labeled count suggests. Can the computational cost be reduced while retaining the same guarantee on corrupted training data? [Geometry of Gaussian decision boundaries](geometry-recovery.md)
