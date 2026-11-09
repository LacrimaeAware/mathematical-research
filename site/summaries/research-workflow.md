# Research workflow and current directions

The workflow starts with a mathematical question, compares published results and uses a bounded proof attempt or experiment to decide what to try next.

AI assists with derivations, literature searches, implementation and editing.

## Current work

Recent work studies robust factor recovery: estimating shared directions and unequal background noise from observations with outliers and highly variable magnitudes. The next planned step is to compare the written recovery guarantee with existing methods and define a reproducible validation task.

Separate investigations study convolution stability, asking how close a distribution is to an exactly stable one when convolving it with itself changes it only slightly, and robust learning from corrupted labels.

## Research cycle

1. Read the closest published results and check their assumptions.
2. Write competing explanations and a test that could distinguish them.
3. Compare what the proof or experiment establishes, including failed approaches.
4. Update the source notes, reusable arguments and next decision.

The wider project maintains a cumulative bibliography with reading notes, a reusable-method archive and comparison workbooks generated from its research records.

## Public workflow tools

| Component | Function | Inspect |
|---|---|---|
| Dependency checks | Detect cycles, missing claims and duplicate dependencies. | [Python validator](../workflow/validate_graph.py) · [example map](../workflow/dependency-example.json) |
| Source versions and handoffs | Check saved source hashes before generating a research handoff. | [State checker and compiler](../workflow/research_state.py) · [generated handoff](../workflow/example-handoff.md) |
| Lean replay | Compile saved candidates against a fixed statement and record diagnostics, timeouts and axioms. | [Runner](../workflow/lean_replay.py) · [recorded output](../workflow/lean-example-result.json) |
| Portfolio generation | Generate topic metadata and proof labels from the research register. | [Build and data flow](https://github.com/LacrimaeAware/mathematical-research/blob/main/DEVELOPMENT.md) |

## Try the prototype

From a checkout of the [repository](https://github.com/LacrimaeAware/mathematical-research), with Python 3.10+:

```sh
python site/workflow/research_state.py check
python site/workflow/research_state.py handoff --output handoff.md
```

The included example follows the two [prime-pattern gap constructions](prime-patterns.md). Edit its source excerpt and rerun the check: the changed fingerprint blocks a new handoff until the evidence is reviewed.

With Lean 4 installed, `python site/workflow/lean_replay.py` runs a small adapter test: an incorrect proof and a placeholder are rejected; a valid proof of the same statement is accepted. The [tool README](https://github.com/LacrimaeAware/mathematical-research/blob/main/site/workflow/README.md) includes the regression tests and input formats.

## Proposed prover integrations

Further Lean integrations and proof-generation benchmarks remain [proposals](../workflow/engineering-roadmap.md). The public prototype currently uses batch compilation.

[Research-brief template](../workflow/research-brief.md) · [Proof labels and verification](methods.md)
