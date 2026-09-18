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

Edit the homepage in `site/index.html`, its styles in `site/style.css`, and the topic summaries in `site/summaries`. The build clears its `dist` output directory and includes only the homepage, summaries and workflow case study, explicitly selected workflow examples, tools and tests, stylesheet, filter and proof-help scripts, and KaTeX assets. Relative links support hosting below a repository subpath.

## Research filters

`site/research.json` supplies the topic order, subject filters and proof descriptions. A standalone checkout builds this committed snapshot. Maintainers can set `RESEARCH_REGISTRY_TOOL` to a local exporter script; the build then refreshes the snapshot before rendering and stops if export fails.

The public page has one subject filter. Each card carries its own proof labels and an explanation available by hover, focus or tap. **Lean-verified** means substantial formalization of the selected result with its theorem interfaces explained. **Written proof** refers to a written argument for the particular result summarized, with self-review or internal review. Related open questions belong inside the summaries.

Each metadata entry must match exactly one `data-research` card and summary page. The build generates proof badges and `RESEARCH.md` from the same snapshot. Topic scope paragraphs marked `proof-scope` are synchronized too. `README.md` is the repository front page; `media/portfolio-preview.jpg` is a screenshot of the site.

The `subject` URL parameter preserves the selection on reload and supports links to an area of mathematics. Without JavaScript, all cards remain readable.

## Publish the presentation

The public repository serves GitHub Pages from `main:/docs`, matching the linked live portfolio. In the public checkout, rebuild the presentation and refresh its generated Pages directory:

```bash
npm ci
npm run pages
```

Commit the changed source and `docs/` together. The Pages preparation command replaces the generated directory, so retired pages and downloads are removed. It refuses to replace a directory without the generated-output marker or to follow a linked output directory. `dist/` and `node_modules/` stay untracked. Run `npm run test:pages` to check these protections.

The repository contains the public summaries and presentation source. The research implementations and full proof notes are maintained separately. KaTeX's license is distributed with its bundled assets.

## Workflow example

Run `python site/workflow/research_state.py check` and `python -m unittest discover -s site/workflow -p "test_*.py"` to check the public example and the validator. This small public example is separate from the private research maps. It checks graph structure, not proof validity.
