# Dependency and proof experiments

Three small Python components explore dependency maps and Lean proof candidates.

| Component | What it does |
|---|---|
| `validate_graph.py` | Sorts an AND/OR dependency map and traces a result’s dependencies. |
| `research_state.py` | Associates claims with source files and produces a Markdown dependency summary. |
| `lean_replay.py` | Runs candidate proofs of one fixed statement through Lean and collects compiler diagnostics. |

Python 3.10+; Lean replay also needs Lean 4 on PATH.

From the repository root, run the component tests with:

```sh
python -m unittest discover -s site/workflow -p "test_*.py"
```
