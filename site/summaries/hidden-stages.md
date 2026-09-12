# What a repeated observation reveals about hidden stages

Suppose a task finishes after two hidden waiting stages. You observe the total time, but different members of the population have different stage speeds. Can those totals tell you what would happen if both stages were sped up?

This belongs to a broader statistical question: what can repeated observations reveal about a heterogeneous population? [Wei and Nguyen](https://arxiv.org/abs/2004.05542) study identification and estimation in models built from repeated observations of latent types.

## Result

An explicit construction gives populations with **exactly the same baseline completion-time distribution but different responses to a speed-up**. Even knowing the baseline distribution perfectly leaves information missing.

The accompanying proof establishes a sharp lower bound for the completion probability after an additive increase in stage rates. A compatible population attains the bound, so it describes the best guarantee available from those pooled totals.

For two stages, **one matched repeat supplies enough information to estimate the actual response**. The two runs share the same hidden stage rates. An explicit unbiased statistic uses their totals directly, and an extension controls the estimated completion curve across all deadlines at a fixed rate boost.

## The model and guarantee

The stages have independent exponential waiting times conditional on their hidden rates. The intervention adds a known rate $\theta$ to each stage. Repeats preserve the hidden rate pair.

With a positive rate floor $\ell$, the number of matched panels needed for error $\varepsilon$ at fixed confidence has order

$$O\!\left((1+\theta/\ell)\varepsilon^{-2}\right).$$

A matching lower bound holds in the specified difficult regime. These are mathematical guarantees for this stage model.

## Related results: what a checkpoint changes

A related discrete-time model uses independent geometric stages and multiplies each stage’s success probability by a known factor. Here the exact total-time distribution identifies the accelerated law. A simulation theorem shows that no algorithm with a fixed cap on baseline records can reproduce that speed-up exactly across the allowed parameter range.

Separate upper and lower bounds compare observation designs. In explicit difficult examples, one intermediate checkpoint removes the growth in episode count caused by a long known block of stages. These written results distinguish identifying a speed-up from estimating it efficiently, and show why the location of an observation can matter.

## Approach

The argument compares populations that are indistinguishable from pooled totals, derives the sharp envelope, and uses the joint law of matched repeats to recover the missing response. Separate internal checks cover the estimator, its observation cost and its lower bound.
