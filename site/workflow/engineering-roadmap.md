# Engineering roadmap

Reviewed September 17, 2026. This plan extends the working Python tools in this
directory. The linked systems are integration candidates and design references.

## 1. Connect generated Lean attempts to live prover feedback

Start with [Lean LSP MCP](https://github.com/oOo0oOo/lean-lsp-mcp): it exposes
diagnostics and goal states through the Lean language server. Pin a version in
an isolated Lean project, retrieve a goal, submit one candidate and save the
diagnostic response alongside its source hash. Acceptance: reproduce one failed
attempt and one accepted repair without changing the theorem statement.

The current `lean_replay.py` already provides the batch compiler side of this
experiment. Next, feed its diagnostics to a model with a fixed attempt budget,
then replay the returned proof. Keep the statement and imports under review;
preserve failed attempts rather than only the final successful proof.

## 2. Make the written argument and Lean declarations navigable together

[Lean Blueprint](https://github.com/PatrickMassot/leanblueprint) is the relevant
model for linking mathematical exposition, dependencies and formal declarations.
Trial it on one small, already formalized argument. Acceptance: every selected
lemma links to its statement, named Lean declaration and declared dependencies;
unformalized analytic inputs remain identifiable at the right nodes.

## 3. Compare proof generation strategies on a fixed evaluation set

[Lean Copilot](https://github.com/lean-dojo/LeanCopilot) combines model-generated
tactics with Aesop search. [Pantograph](https://github.com/stanford-centaur/PyPantograph)
offers programmatic tactic execution and proof-state inspection. Use these as
baselines or adapters before writing a new search engine.

Prepare separate development and held-out theorem groups; split related lemmas
together so near-duplicates do not cross the split. Freeze theorem statements,
imports, toolchain, context access, time and attempt budgets. Compare one-shot
generation, compiler-guided repair and retrieval-assisted repair. Report solved
tasks at each budget, timeouts, failures, token use and axiom checks. Review the
formal statement against the intended mathematics separately.

Acceptance: a script reruns the same tasks and produces per-attempt JSON plus a
summary. Start with a small engineering evaluation; expand before drawing model
performance conclusions. The included addition example is only a smoke test.

## 4. Build training data after the evaluation is stable

[LeanDojo-v2](https://github.com/lean-dojo/LeanDojo-v2) documents tracing, retrieval,
supervised fine-tuning and GRPO training components. Its predecessor's README
directs new projects to v2. First export checked `(goal, context, candidate,
diagnostics, outcome)` records with source versions and dataset licenses. Then
test retrieval and, if there is enough suitable data and compute, a small
supervised fine-tuning experiment. Compare it against the frozen baseline.

Record the data split, configuration, compute cost and held-out measurements
for each experiment. The near-term work is prover integration and evaluation;
training experiments follow once the evaluation and data collection are stable.
