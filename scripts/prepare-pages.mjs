import {cp, mkdir, readdir, access, realpath} from 'node:fs/promises';
import {existsSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import path from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const source = path.join(root, 'dist');
const target = path.join(root, 'docs');
await access(path.join(source, '.nojekyll'));
if (existsSync(target)) {
  if (await realpath(target) !== path.resolve(target)) throw new Error('Pages output must not be a link.');
  if ((await readdir(target)).length && !existsSync(path.join(target, '.nojekyll'))) {
    throw new Error('Refusing to replace a docs directory that is not generated Pages output.');
  }
}
await mkdir(target, {recursive:true});
await cp(source, target, {recursive:true});
console.log('Prepared docs/ for GitHub Pages. Commit the presentation source and generated docs together.');
