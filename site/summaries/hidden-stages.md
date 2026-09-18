# How many repeats reveal hidden stages?

Suppose a task finishes after several hidden waiting stages. Only the total time is visible, and different members of the population have different stage counts and speeds. Can repeated observations reveal the hidden population—and predict what happens when every stage speeds up?

## An exact observation threshold

For populations with **at most $m$ independent exponential stages**, $m$ matched completion times identify the population's joint distribution of stage count and unordered stage rates. Each matched group shares the same hidden type, with independent waiting times across runs.

The threshold is sharp: with $m-1$ matched totals, two populations can give exactly the same observations but different responses to an additive rate increase. The construction works for any positive deadline and positive boost.

For two stages, this means **two runs—one matched repeat—suffice**. Pooled totals alone can leave the intervention response undetermined even when their distribution is known exactly.

## Estimating the response directly

The intervention adds a known rate $\theta$ to each stage. An explicit unbiased statistic uses matched totals to estimate the resulting completion probability, with a uniform guarantee when the hidden rates have a positive lower bound.

In the two-stage case, with rate floor $\ell$, the number of matched panels needed for error $\varepsilon$ at fixed confidence has order

$$O\!\left((1+\theta/\ell)\varepsilon^{-2}\right).$$

A matching lower bound holds in the specified difficult regime. The two-stage study also gives sharp bounds on intervention response from pooled totals and an extension to simultaneous estimation across deadlines.

## Connection to existing work

[Vandermeulen and Scott](https://arxiv.org/abs/1607.00071) study mixture identification from grouped observations, with thresholds controlled by the number of mixture components. [Wei and Nguyen](https://arxiv.org/abs/2004.05542) study identification and estimation from repeated observations of latent types.

Here the controlling quantity is the **number of exponential stages within each type**. The population may mix arbitrarily many types, the number of stages can be unknown, and repeated rates are allowed. The proof uses the special transform structure of exponential sums to obtain the stage-count threshold.

## Related result: what a checkpoint changes

A separate discrete-time model uses independent geometric stages and multiplies their success probabilities by a known factor. Its exact total-time distribution identifies the accelerated law. An intermediate checkpoint can also reduce the observation cost: in explicit examples, one checkpoint removes the growth in episode count caused by a long known block of stages.

## Proof scope

<!-- proof-scope:hidden-stages -->
Written, self-reviewed threshold for populations with at most m exponential stages: m matched totals identify the hidden stage count and unordered rates, while m−1 can fail. Uniform estimator guarantees assume a positive rate floor. Exact identity checks supplement the proof.
<!-- /proof-scope -->
