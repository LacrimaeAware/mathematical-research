import {cp, mkdir, readdir, realpath, lstat, rm} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';

async function generatedDirectory(directory, allowEmpty = false) {
  const info = await lstat(directory);
  if (!info.isDirectory() || info.isSymbolicLink() || await realpath(directory) !== directory) {
    throw new Error('Pages directories must be real directories, not links.');
  }
  if (allowEmpty && !(await readdir(directory)).length) return;
  const marker = await lstat(path.join(directory, '.nojekyll')).catch(() => null);
  if (!marker?.isFile() || marker.isSymbolicLink()) {
    throw new Error('Refusing to replace a directory without its generated-output marker.');
  }
}

export async function preparePages(projectRoot) {
  const root = await realpath(projectRoot);
  const source = path.join(root, 'dist');
  const target = path.join(root, 'docs');
  if (path.dirname(target) !== root || source === target) throw new Error('Unexpected Pages directory');
  await generatedDirectory(source);
  const targetInfo = await lstat(target).catch(error => {
    if (error.code !== 'ENOENT') throw error;
    return null;
  });
  if (targetInfo) {
    await generatedDirectory(target, true);
    await rm(target, {recursive: true});
  }
  await mkdir(target, {recursive: true});
  await cp(source, target, {recursive: true});
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  await preparePages(fileURLToPath(new URL('../', import.meta.url)));
  console.log('Prepared docs/ for GitHub Pages. Commit the presentation source and generated docs together.');
}
