# Building the portfolio

The website uses static HTML and CSS. Markdown summaries are rendered with Marked and KaTeX; styles and fonts are bundled locally.

## Preview

With Node.js 22.12 or later, npm and Python installed:

```bash
npm ci
npm run build
npm run preview
```

Open the loopback address printed by the preview command.

Edit the homepage in `site/index.html`, its styles in `site/style.css`, and the topic summaries in `site/summaries`. The build replaces `dist/` with the homepage, summaries, workflow examples and local assets. Relative links support hosting below a repository subpath.

## Research filters

`site/research.json` supplies the topic order, subject filters and proof descriptions. A standalone checkout builds this committed snapshot. Maintainers can set `RESEARCH_REGISTRY_TOOL` to a local exporter script; the build then refreshes the snapshot before rendering and stops if export fails.

The public page has one subject filter. Each card carries proof labels explained on hover, focus or tap.

Each metadata entry must match exactly one `data-research` card and summary page. The build generates proof badges and `RESEARCH.md` from the same snapshot. Topic scope paragraphs marked `proof-scope` are synchronized too. `README.md` is the repository front page; `media/portfolio-preview.jpg` is a screenshot of the site.

The `subject` URL parameter preserves the selection on reload and supports links to an area of mathematics. Without JavaScript, all cards remain readable.

## Publish the presentation

The public repository serves GitHub Pages from `main:/docs`, matching the linked live portfolio. In the public checkout, rebuild the presentation and refresh its generated Pages directory:

```bash
npm ci
npm run pages
```

Commit the changed source and `docs/` together. `dist/` and `node_modules/` stay untracked. Run `npm run test:pages` to test Pages preparation.

KaTeX's license is distributed with its bundled assets.

## Python component tests

Run `python -m unittest discover -s site/workflow -p "test_*.py"`.
