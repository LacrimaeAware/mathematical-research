# Computation and formal proof

## Python

The work includes integer-factorization searches, divisibility experiments, geometric recovery experiments and finite probability models. For factor packing, the checks compare two independent algorithms on 720 small problems and verify the constructions used in the threshold result. Other checks cover finite graph counts and exact probability distributions.

## Lean

<!-- proof-scope:prime-patterns -->
The original matching-based gap bound is substantially formalized in Lean, conditional on quantitative Selberg and labelled Bennett–Frieze inputs. A separate written Rankin-style adaptation gives the larger bound displayed in the comparison.
<!-- /proof-scope -->

The recorded kernel audit for `main_gap_v6_cleanup` reports only Lean’s standard logical axioms, with no placeholder-proof axiom. This checks the formal deductions from the two named inputs.

The finite-symmetry development also formalizes specific density, quotient-class and fibre deductions. Its full structure theorem has a written proof.

## Proof labels

**Lean-verified** means substantial formalization of the result being presented. Each badge explains the scope and any external theorem interfaces.

**Written proof** means a written argument for the specific result described, with self-review or internal proof review. Related open questions are identified in the summaries. This label does not describe every claim in the broader project.

[Prime-pattern result](prime-patterns.md) · [Finite-symmetry result](finite-symmetry.md) · [Factorization result](factor-packing.md)

<p id="ai-assistance">AI assists with derivations, literature comparison, code and editing.</p>
