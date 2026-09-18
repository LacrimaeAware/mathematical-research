# Engineering an AI-assisted research workflow

Long investigations leave behind partial proofs, competing drafts and assumptions that need checking. I designed the task structure and review process for this work, and I’m developing Python tools to make those investigations easier to inspect and continue across models and sessions.

The prototype connects **research-state validation, source fingerprints, generated handoffs and Lean compiler feedback**. AI assists with derivations, literature searches, implementation and editing; I set the direction and requirements and iterate on the process through the research itself.

## Working components

| Component | Engineering detail | Inspect |
|---|---|---|
| Dependency validation | AND/OR directed acyclic graphs record shared lemmas and alternative routes. A topological sort detects cycles; reference checks catch missing claims and duplicate edges. | [Python validator](../workflow/validate_graph.py) · [example map](../workflow/dependency-example.json) |
| Evidence and handoffs | A structured JSON state links claims to source files and research attempts. SHA-256 text fingerprints detect changed evidence before the tool compiles a dependency-aware Markdown handoff. | [State checker and compiler](../workflow/research_state.py) · [generated handoff](../workflow/example-handoff.md) |
| Lean candidate replay | The runner generates Lean files from saved proof candidates while keeping the statement fixed. It records compiler diagnostics, timeouts, source hashes and the theorem’s axiom report. | [Runner](../workflow/lean_replay.py) · [recorded output](../workflow/lean-example-result.json) |
| Portfolio generation | A maintained research register generates the public metadata and proof-scope descriptions. Fingerprint checks require changed research evidence to be reconciled before export. | [Build and data flow](https://github.com/LacrimaeAware/mathematical-research/blob/main/DEVELOPMENT.md) |

These tools grow out of a workflow used across the investigations. One retained dependency map has **195 nodes and 45 edges**. Research briefs specify the hypotheses, proposed approach, decisive check and return format; handoffs preserve useful deductions when a route fails.

## Try the prototype

From a checkout of the [repository](https://github.com/LacrimaeAware/mathematical-research), with Python 3.10+:

```sh
python site/workflow/research_state.py check
python site/workflow/research_state.py handoff --output handoff.md
```

The included example follows the two [prime-pattern gap constructions](prime-patterns.md). Edit its source excerpt and rerun the check: the changed fingerprint blocks a new handoff until the evidence is reviewed.

With Lean 4 installed, `python site/workflow/lean_replay.py` runs a small adapter test: an incorrect proof and a placeholder are rejected; a valid proof of the same statement is accepted. The [tool README](https://github.com/LacrimaeAware/mathematical-research/blob/main/site/workflow/README.md) includes the regression tests and input formats. Structural checks, compiler acceptance and mathematical interpretation each have a separate job.

## Next engineering steps

The next integration is live goal and diagnostic access through [Lean LSP MCP](https://github.com/oOo0oOo/lean-lsp-mcp), alongside a trial of [Lean Blueprint](https://github.com/PatrickMassot/leanblueprint) for linking written lemmas to formal declarations.

After that, I want to compare one-shot generation, compiler-guided repair and retrieval-assisted repair on fixed, held-out theorem groups. [Lean Copilot](https://github.com/lean-dojo/LeanCopilot), [Pantograph](https://github.com/stanford-centaur/PyPantograph) and [LeanDojo-v2](https://github.com/lean-dojo/LeanDojo-v2) provide concrete references for proof search, prover interaction and eventual training experiments. The [engineering roadmap](../workflow/engineering-roadmap.md) specifies the interfaces and checks for each stage.

[Research-brief template](../workflow/research-brief.md) · [Proof labels and verification](methods.md)
