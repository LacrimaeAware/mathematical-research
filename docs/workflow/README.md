# Research workflow prototype

Small, runnable components from an AI-assisted mathematics workflow: dependency
validation, evidence fingerprints, generated handoffs and Lean candidate replay.
Python 3.10+; the Lean example also needs Lean 4 on PATH (tested with 4.34.0).

From the repository root:

```sh
python site/workflow/research_state.py check
python site/workflow/research_state.py handoff --output handoff.md
python site/workflow/lean_replay.py
python -m unittest discover -s site/workflow -p "test_*.py"
```

The handoff command creates a new file and preserves an existing output.

## What to inspect

| Component | Behavior | Example |
|---|---|---|
| `validate_graph.py` | Checks unique identifiers, AND/OR edges and references; topologically sorts the map and traces the root's dependencies. | [8-node map](dependency-example.json) |
| `research_state.py` | Validates attempt records and claim-to-source links; checks SHA-256 text fingerprints before emitting Markdown. | [State](example-state.json) → [generated handoff](example-handoff.md) |
| `lean_replay.py` | Generates a file for each saved proof candidate with the same statement, runs Lean with a timeout, and records diagnostics, axioms and source hashes. | [Candidates](lean-example.json) → [recorded compiler output](lean-example-result.json) |

Try editing `gap-comparison.md`, then run `research_state.py check`: it exits
with an error naming the changed source. Review and explicitly update the
fingerprint before generating another handoff. Text fingerprints normalize
CRLF/LF line endings for reproducible Windows/Linux checkouts.

The Lean smoke test rejects an incorrect proof and a placeholder, and accepts
the corrected proof. The runner treats warnings as errors, requires an axiom
report and permits only the standard `propext`, `Classical.choice` and
`Quot.sound` axioms. Run trusted local candidate code: Lean metaprograms can
execute code. This runner is a compiler adapter, not a sandbox.

The example graph abbreviates written research arguments. Its structural
validation does not certify those arguments. The Lean smoke test checks the
adapter's behavior, rather than measuring research proof-solving performance.

[Research brief](research-brief.md) · [Engineering roadmap](engineering-roadmap.md)
