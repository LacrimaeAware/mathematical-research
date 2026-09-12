# Building the portfolio

The website uses static HTML and CSS. Markdown summaries are rendered with Marked and KaTeX; styles and fonts are bundled locally.

## Preview

With Node.js 20 or later, npm and Python installed:

```bash
npm ci
npm run build
npm run preview
```

Open the loopback address printed by the preview command.

Edit the homepage in `site/index.html`, its styles in `site/style.css`, and the topic summaries in `site/summaries`. The build clears its `dist` output directory and includes only the homepage, summaries, stylesheet, filter and proof-help scripts, and KaTeX assets. Relative links support hosting below a repository subpath.

## Research filters

Public copy describes the result directly: “the theorem establishes”, “the construction gives”, or “the calculation shows”. Use **Result** for summary headings. Reserve first-person voice for motivation and research context; avoid “I proved”, “we proved” and equivalent personal achievement claims. This is a choice of voice and does not change the result’s proof status.

`site/research.json` is the generated public snapshot of the maintained research register. In the local research workspace, the build first calls `MathExperimentation/tools/research_portfolio.py` to export it from `research/status.json`. Changes to registered evidence block export until the affected assessment is reconciled. A standalone checkout builds the committed public snapshot without access to private research files.

The public page has one subject filter. Each card carries its own proof labels and an explanation available by hover, focus or tap. **Lean-verified** means substantial formalization of the selected result with its theorem interfaces explained. **Written proof** refers to a written argument for the particular result summarized, with self-review or internal review. Related open questions belong inside the summaries.

Cards retain the order exported by the maintained register. Each metadata entry must match exactly one `data-research` card and summary page. The build generates proof badges and `RESEARCH.md` from the same snapshot. Topic scope paragraphs marked `proof-scope` are synchronized too. `README.md` is the hand-edited visual front page; `media/portfolio-preview.jpg` is a screenshot of the site.

Private candidate rankings, paper plans and evidence paths are never exported. The private overview is generated separately in the research workspace.

The `subject` URL parameter preserves the selection on reload and supports links to an area of mathematics. Without JavaScript, all cards remain readable.

## Publish the presentation

The public repository serves GitHub Pages from `main:/docs`, matching the linked live portfolio. In the public checkout, rebuild the presentation and refresh its generated Pages directory:

```bash
npm ci
npm run pages
```

Review and commit the changed source and `docs/` together. The Pages preparation command refuses to write over a non-generated documentation directory. When removing a page, also remove its retired generated counterpart from `docs/` before committing. `dist/` and `node_modules/` stay untracked.

The repository contains the public summaries and presentation source. The research implementations and full proof notes are maintained separately. KaTeX's license is distributed with its bundled assets.
