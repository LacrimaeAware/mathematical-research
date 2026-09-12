# Recovering two boundaries and their noise rates

Suppose a device reports whether two hidden linear tests agree, but sometimes flips its answer. The two output classes may have different, unknown error rates. Can the measurements identify both the hidden tests and the errors?

Recovery with unknown asymmetric label noise has an established theory, including [Scott, Blanchard and Handy’s work](https://proceedings.mlr.press/v30/Scott13.html). This study asks which low-order measurements contain enough information for a specific two-boundary model.

## Result

**Measurements through degree three can be identical for different boundaries and different noise rates. Degree four supplies enough information to recover both.** An explicit pair of models establishes the ambiguity; an inversion formula establishes recovery.

A label-weighted moment averages the observed label multiplied by a polynomial of the input coordinates. The degree tells us which polynomial measurements are available. The result identifies a precise change in the information collected that resolves the ambiguity.

| Available measurements | What they determine |
|---|---|
| Label-weighted moments through degree three | Can leave two different geometries and noise channels indistinguishable |
| Selected fourth-degree moments, together with lower-degree measurements | Recover both boundaries and both flip rates under the model |

## The model

Inputs are standard Gaussian. The clean response is $\operatorname{sign}((a\cdot X)(b\cdot X))$, for two distinct boundaries through the origin. Each clean class has a constant flip rate, with $\eta_++\eta_-<1$. Recovery respects the symmetries of the unordered boundary pair. These are guarantees from population moments; the proof also gives perturbation bounds for estimated moments.

## Approach

Second-degree measurements identify the relevant plane but mix together the boundary angle and noise strength. Fourth-degree measurements separate those quantities. A bounded angular implementation uses the same geometric information and is unchanged by positive rescaling of individual inputs.

The work includes an explicit indistinguishable pair, written inversion and perturbation arguments, and synthetic experiments. Narrow angles make recovery less stable. The result provides a concrete noise-calibration case within the broader [geometry-recovery study](geometry-recovery.md).
