import {readFile, writeFile, mkdir, cp, rm} from 'node:fs/promises';
import {existsSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {marked} from 'marked';
import katex from 'katex';

const root = fileURLToPath(new URL('../', import.meta.url));
const out = path.join(root, 'dist');
if(path.dirname(out) !== path.resolve(root) || path.basename(out) !== 'dist') throw new Error('Unexpected output directory');
const math = (text, displayMode) => katex.renderToString(text.trim(), {displayMode, throwOnError:true, strict:'error'});
const registryTool = path.resolve(root, '../../MathExperimentation/tools/research_portfolio.py');
if (existsSync(registryTool)) {
  execFileSync('python', [registryTool, '--export-public', path.join(root, 'site/research.json')], {stdio:'inherit'});
} else {
  console.log('Building the recorded public snapshot; the private source register is not in this checkout.');
}
const research = JSON.parse(await readFile(path.join(root, 'site/research.json'), 'utf8'));
const escapeHtml = value => String(value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
for (const [slug, entry] of Object.entries(research.entries)) {
  for (const [field, labels] of [['subjects', research.subjects], ['proof', research.proofStatuses]]) {
    if (!Array.isArray(entry[field]) || !entry[field].length || entry[field].some(key => !Object.hasOwn(labels, key))) {
      throw new Error(`Invalid ${field} classification for ${slug}`);
    }
  }
}
const renderTags = (entry, slug) => `<ul class="research-tags" aria-label="Subjects and proof status">${entry.subjects.map(key => `<li>${escapeHtml(research.subjects[key])}</li>`).join('')}${entry.proof.map(key => `<li class="proof-tag"><button type="button" data-proof-help aria-expanded="false" aria-describedby="scope-${slug}-${key}">${escapeHtml(research.proofStatuses[key])} <span aria-hidden="true">ⓘ</span></button><span class="scope-tooltip" id="scope-${slug}-${key}" role="tooltip" hidden>${escapeHtml(entry.scope)}</span></li>`).join('')}</ul>`;
const filterRow = (key, title, labels, field) => {
  const available = new Set(Object.values(research.entries).flatMap(entry => entry[field]));
  const choices = [['all', 'All'], ...Object.entries(labels).filter(([value]) => available.has(value))];
  const descriptions = key === 'proof' ? research.proofDescriptions : {};
  return `<div class="filter-row" role="group" aria-labelledby="${key}-filter-label" data-filter-group="${key}"><span id="${key}-filter-label" class="filter-label">${title}</span><div class="filter-options">${choices.map(([value, label]) => `<button type="button" data-value="${value}" aria-pressed="${value === 'all'}" aria-controls="research-list"${descriptions[value] ? ` title="${escapeHtml(descriptions[value])}"` : ''}>${escapeHtml(label)}</button>`).join('')}</div></div>`;
};
const filters = `<div class="research-filters" data-research-filters hidden>${filterRow('subject', 'Subject', research.subjects, 'subjects')}</div>`;
marked.use({extensions:[
  {name:'displayMath',level:'block',start:src=>src.indexOf('$$'),tokenizer(src){const m=/^\$\$\s*\n?([\s\S]+?)\n?\$\$(?:\n|$)/.exec(src);if(m)return{type:'displayMath',raw:m[0],text:m[1]};},renderer:token=>math(token.text,true)},
  {name:'inlineMath',level:'inline',start:src=>src.indexOf('$'),tokenizer(src){const m=/^\$([^$\n]+)\$/.exec(src);if(m)return{type:'inlineMath',raw:m[0],text:m[1]};},renderer:token=>math(token.text,false)}
]});
// The preview contains summaries only. Clear previous generated files so that
// retired proof notes and supporting downloads cannot survive a rebuild.
await rm(out,{recursive:true,force:true});
await mkdir(path.join(out,'notes'),{recursive:true});
let index=await readFile(path.join(root,'site/index.html'),'utf8');
const found = new Set();
index=index.replace(/<article\b[^>]*data-research="([^"]+)"[^>]*>[\s\S]*?<\/h3>/g, (card, slug) => {
  const entry = research.entries[slug];
  if (!entry || found.has(slug)) throw new Error(`Missing or duplicate research entry: ${slug}`);
  found.add(slug);
  return card.replace('>', ` data-subject="${entry.subjects.join(' ')}">`) + renderTags(entry, slug);
});
if(found.size !== Object.keys(research.entries).length) throw new Error('Research metadata and cards do not match');
// The register orders main results, supporting results and open questions,
// then uses editorial significance, proof level and editorial topic order.
const cards = new Map([...index.matchAll(/<article\b[^>]*data-research="([^"]+)"[^>]*>[\s\S]*?<\/article>/g)].map(match => [match[1], match[0]]));
const orderedCards = Object.keys(research.entries).map((slug, i) => cards.get(slug).replace(/(<div class="card-label"><span>)\d+ \/ /, `$1${String(i + 1).padStart(2,'0')} / `)).join('\n');
index=index.replace(/(<section class="research-grid"[^>]*>)[\s\S]*?(<\/section>)/, `$1\n${orderedCards}\n$2`);
index=index.replace('<!-- research-filters -->',filters)
  .replace('<!-- research-count -->',`${found.size} research topics`)
  .replace(/data-math="([^"]*)"><\/(strong|span)>/g,(_,tex,tag)=>`>${math(tex,false)}</${tag}>`);
await writeFile(path.join(out,'index.html'),index);
await cp(path.join(root,'site/style.css'),path.join(out,'style.css'));
await cp(path.join(root,'site/filters.js'),path.join(out,'filters.js'));
await cp(path.join(root,'site/proof-tags.js'),path.join(out,'proof-tags.js'));
await mkdir(path.join(out,'vendor'),{recursive:true});
await cp(path.join(root,'node_modules/katex/dist/katex.min.css'),path.join(out,'vendor/katex.min.css'));
await cp(path.join(root,'node_modules/katex/dist/fonts'),path.join(out,'vendor/fonts'),{recursive:true});
await cp(path.join(root,'node_modules/katex/LICENSE'),path.join(out,'vendor/KATEX-LICENSE.txt'));
for(const slug of [...Object.keys(research.entries),'methods']){
  let source=await readFile(path.join(root,'site/summaries',`${slug}.md`),'utf8');
  source=source.replace(/<!-- proof-scope:([\w-]+) -->[\s\S]*?<!-- \/proof-scope -->/g, (_, key) => `<!-- proof-scope:${key} -->\n${research.entries[key].scope}\n<!-- /proof-scope -->`);
  await writeFile(path.join(root,'site/summaries',`${slug}.md`),source);
  const title=source.split('\n')[0].replace(/^# /,'');
  let body=marked.parse(source).replace(/<table>/g,'<div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable data table"><table>').replace(/<\/table>/g,'</table></div>');
  if(research.entries[slug]) body=body.replace('</h1>','</h1>'+renderTags(research.entries[slug], slug));
  body=body.replace(/href="([\w-]+)\.md(?=["#])/g, (match, target) => Object.hasOwn(research.entries,target) || target==='methods' ? `href="${target}.html` : match);
  await writeFile(path.join(out,'notes',`${slug}.html`),`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escapeHtml(title)} · LacrimaeAware</title><link rel="stylesheet" href="../style.css"><link rel="stylesheet" href="../vendor/katex.min.css"><script src="../proof-tags.js" defer></script></head><body><main class="note"><a class="back" href="../index.html">← Independent Mathematical Research</a>${body}<p class="note-footer">Unrefereed work. External priority is unestablished.</p></main></body></html>`);
}
const rows=await Promise.all(Object.entries(research.entries).map(async ([slug,entry])=>{
    const title=(await readFile(path.join(root,'site/summaries',`${slug}.md`),'utf8')).split('\n')[0].replace(/^# /,'').trim();
    return `| [${title}](site/summaries/${slug}.md) | ${entry.brief} | ${entry.proof.map(key=>research.proofStatuses[key]).join(' · ')} |`;
}));
await writeFile(path.join(root,'RESEARCH.md'), `# Research index\n\n[Browse the visual portfolio](https://lacrimaeaware.github.io/mathematical-investigations/) · [Repository overview](README.md)\n\nEach proof label applies to the result described in its summary.\n\n| Research | Result or question | Proof status |\n|---|---|---|\n${rows.join('\n')}\n`);
await writeFile(path.join(out,'.nojekyll'),'');
console.log(`Built the filtered overview and ${Object.keys(research.entries).length + 1} short summaries. Output includes only public pages and their local assets.`);

