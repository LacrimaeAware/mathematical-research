# Matching decision boundaries even when they cancel

Two models can give almost identical answers while using different internal parameters. Understanding when their parameters must also agree is an inverse-stability problem, studied for neural networks by [Berner, Elbrächter and Grohs](https://arxiv.org/abs/1905.09803).

Here a model changes its binary answer each time an input crosses a straight boundary. Crossing two identical boundaries changes the answer twice, so the effects cancel. This makes it possible for a model to contain extra boundaries that its predictions barely reveal.

## Result

The theorem gives a **linear bound on the cost of pairing boundaries that nearly cancel**, under Gaussian inputs. It allows boundaries to coincide or approach one another. Its constant depends on the number of boundaries and their distance from the origin, independently of the surrounding dimension.

Exact cancellation already explains why identical boundaries disappear. The quantitative result measures how close the boundaries must be when cancellation is only approximate. With separated true boundaries, a consequence matches every true boundary to a distinct estimated one, with error proportional to prediction error.

## The guarantee

Take an even number $k$ of boundary tests $h_i(x)=\operatorname{sign}(u_i\cdot x-b_i)$, where $\|u_i\|=1$ and $|b_i|\le T$. Define the departure of their combined output from a constant by

$$\Delta=1-\left|\mathbb E\prod_{i=1}^k h_i(G)\right|,\qquad G\sim N(0,I).$$

If $D$ is the least total angle-and-threshold error over all pairings, the written proof establishes

$$\sqrt{\pi/2}\,\Delta\le D\le C(k,T)\,\Delta.$$

The global constant is explicit and can be large. A sharper estimate applies when the true boundaries are separated.

## Approach

A boundary far from every other boundary creates a region where its sign change is visible. Gaussian probability estimates turn that visible region into a lower bound on prediction disagreement. Repeatedly pairing nearby boundaries gives the global estimate, accounting for how each removal changes the error.

This supports the broader [geometry-recovery study](geometry-recovery.md), especially its treatment of collisions. Both the matching argument and its separated-boundary consequence have written proofs and independent internal review.
