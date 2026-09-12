# Computation and formal proof

Python code supports example searches, algorithm comparisons and exact calculations. Lean provides a language for formal proofs that a small logical kernel can check, from the definitions through the stated conclusion.

## Python

The work includes integer-factorization searches, divisibility experiments, geometric recovery experiments and finite probability models. For factor packing, the checks compare two independent algorithms on 720 small problems and verify the constructions used in the threshold result. Other checks cover finite graph counts and exact probability distributions.

## Lean

<!-- proof-scope:prime-patterns -->
The long-gap construction is substantially formalized in Lean, including its final endpoint. Two external theorem interfaces remain: quantitative Selberg and the labelled Bennett–Frieze matching result. The written manuscript supplies the extension argument.
<!-- /proof-scope -->

The final gap theorem’s kernel audit reports only Lean’s standard logical axioms, with no placeholder-proof axiom. This checks the formal deductions from the two named inputs.

The finite-symmetry development also formalizes specific density, quotient-class and fibre deductions. Its full structure theorem has a written proof.

## Proof labels

**Lean-verified** means substantial formalization of the result being presented. Each badge explains the scope and any external theorem interfaces.

**Written proof** means a written argument for the specific result described, with self-review or internal proof review. Related open questions are identified in the summaries. This label does not describe every claim in the broader project.

[Prime-pattern result](prime-patterns.md) · [Finite-symmetry result](finite-symmetry.md) · [Factorization result](factor-packing.md)
