# Mathematical research & research workflow design

Independent undergraduate work in number theory, algebra, geometry and statistical inference, developed with AI assistance.

**[Explore the portfolio →](https://lacrimaeaware.github.io/mathematical-research/)** · [Research index](RESEARCH.md) · [Workflow case study](site/summaries/research-workflow.md)

[![The research portfolio: geometry recovery, multiplication tables and workflow design](media/portfolio-preview.jpg)](https://lacrimaeaware.github.io/mathematical-research/)

I’m interested in what a mathematical model really tells us, and which questions become easier to answer when its assumptions are made precise. I choose the research questions, design the workflow, and direct testing and revision. AI assists with derivations, code and editing; Python experiments and Lean proofs provide targeted checks.

## Three starting points

| Project | What to explore |
|---|---|
| [Geometry recovery](site/summaries/geometry-recovery.md) | A dimension-independent coefficient guarantee, convex reconstruction from label moments, and recovery bounds for corrupted samples. |
| [Multiplication-table stabilization](site/summaries/multiplication-tables.md) | A sharp worst-alphabet onset scale, with an improved upper bound for the complete multiplication table. |
| [Research workflow design](site/summaries/research-workflow.md) | Python tools for dependency validation, SHA-256 evidence checks, generated handoffs and Lean candidate replay. Includes runnable examples and an integration roadmap. |

## A workflow built through research

I designed the task structure, review requirements and handoffs for investigations that span models and sessions. The working prototype checks AND/OR dependency maps and source fingerprints, compiles research handoffs, and replays saved Lean proof candidates against a fixed statement.

```sh
python site/workflow/research_state.py check
python site/workflow/research_state.py handoff --output handoff.md
```

Python 3.10+. The [tool README](site/workflow/README.md) includes a Lean replay example and tests. The [engineering roadmap](site/workflow/engineering-roadmap.md) covers prover integration, proof-generation evaluation and later training experiments.

**[Browse all twelve research topics →](https://lacrimaeaware.github.io/mathematical-research/#research)** Each page explains the question, result, source connection and proof scope. Further topics include symmetric networks, hidden stages, factorization obstructions and arithmetic tensors. The prime-pattern page compares the original formalized construction with the larger bound from a Rankin-style adaptation.

## Run the presentation

```sh
npm ci
npm run build
npm run preview
```

The build checks card/metadata agreement and renders the mathematics with KaTeX. [Build details](DEVELOPMENT.md) · [Python, Lean and proof labels](site/summaries/methods.md)

---

**LacrimaeAware** · AI-assisted mathematical research and human-directed workflow design.
