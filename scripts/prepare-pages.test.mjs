import {test} from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp, mkdir, writeFile, readFile, access, symlink, rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import path from 'node:path';
import {preparePages} from './prepare-pages.mjs';

async function fixture(t) {
  const root = await mkdtemp(path.join(tmpdir(), 'pages-test-'));
  t.after(async () => {
    if (path.dirname(root) !== tmpdir() || !path.basename(root).startsWith('pages-test-')) {
      throw new Error('Unexpected fixture path');
    }
    await rm(root, {recursive: true, force: true});
  });
  await mkdir(path.join(root, 'dist'));
  await writeFile(path.join(root, 'dist', '.nojekyll'), '');
  await writeFile(path.join(root, 'dist', 'index.html'), '<h1>Current page</h1>');
  return root;
}

test('publishing removes retired downloads from generated output', async t => {
  const root = await fixture(t);
  await mkdir(path.join(root, 'docs', 'downloads'), {recursive: true});
  await writeFile(path.join(root, 'docs', '.nojekyll'), '');
  const retired = path.join(root, 'docs', 'downloads', 'retired.txt');
  await writeFile(retired, 'Old output');
  await preparePages(root);
  await assert.rejects(access(retired), {code: 'ENOENT'});
  assert.equal(await readFile(path.join(root, 'docs', 'index.html'), 'utf8'), '<h1>Current page</h1>');
});

test('publishing preserves an unmarked documentation directory', async t => {
  const root = await fixture(t);
  await mkdir(path.join(root, 'docs'));
  const note = path.join(root, 'docs', 'notes.md');
  await writeFile(note, 'Handwritten notes');
  await assert.rejects(preparePages(root), /generated-output marker/);
  assert.equal(await readFile(note, 'utf8'), 'Handwritten notes');
});

test('publishing refuses linked output directories', async t => {
  const root = await fixture(t);
  const other = path.join(root, 'other');
  await mkdir(other);
  await writeFile(path.join(other, '.nojekyll'), '');
  await writeFile(path.join(other, 'keep.txt'), 'Keep this file');
  await symlink(other, path.join(root, 'docs'), process.platform === 'win32' ? 'junction' : 'dir');
  await assert.rejects(preparePages(root), /not links/);
  assert.equal(await readFile(path.join(other, 'keep.txt'), 'utf8'), 'Keep this file');
});
