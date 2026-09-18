"""Regression tests for graph errors and stale-evidence handoff rejection."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from research_state import compile_handoff, digest, load_state
from validate_graph import validate

HERE = Path(__file__).parent


class ResearchStateTests(unittest.TestCase):
    def setUp(self):
        self.graph = json.loads((HERE / 'dependency-example.json').read_text(encoding='utf-8'))

    def test_example_and_deterministic_handoff(self):
        state, graph, report = load_state(HERE / 'example-state.json')
        self.assertEqual((report['nodes'], report['edges']), (8, 3))
        handoff = compile_handoff(state, graph, report)
        self.assertEqual(handoff, (HERE / 'example-handoff.md').read_text(encoding='utf-8'))
        self.assertIn(' AND ', handoff)
        self.assertIn(' OR ', handoff)
        self.assertIn('External inputs', handoff)

    def test_structural_failures(self):
        cases = []
        duplicate = deepcopy(self.graph)
        duplicate['nodes'].append(deepcopy(duplicate['nodes'][0]))
        cases.append((duplicate, 'Duplicate node'))
        missing = deepcopy(self.graph)
        missing['edges'][0]['from'].append('missing_lemma')
        cases.append((missing, 'Missing node'))
        cycle = deepcopy(self.graph)
        cycle['edges'].append({'from': ['original_bound'], 'to': 'selberg', 'logic': 'AND'})
        cases.append((cycle, 'cycle'))
        logic = deepcopy(self.graph)
        logic['edges'][0]['logic'] = 'MAYBE'
        cases.append((logic, 'logic'))
        empty = deepcopy(self.graph)
        empty['edges'][0]['from'] = []
        cases.append((empty, 'premise'))
        repeated = deepcopy(self.graph)
        repeated['edges'].append(deepcopy(repeated['edges'][0]))
        cases.append((repeated, 'Duplicate edge'))
        status = deepcopy(self.graph)
        status['nodes'][0]['status'] = 'probably_true'
        cases.append((status, 'status'))
        for graph, message in cases:
            with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                validate(graph)

    def test_stale_source_rejected_by_cli(self):
        with TemporaryDirectory() as temp:
            folder = Path(temp)
            for name in ('example-state.json', 'dependency-example.json', 'gap-comparison.md'):
                shutil.copyfile(HERE / name, folder / name)
            with (folder / 'gap-comparison.md').open('a', encoding='utf-8') as source:
                source.write('\nUnreviewed change\n')
            result = subprocess.run([sys.executable, str(HERE / 'research_state.py'), 'handoff',
                                     str(folder / 'example-state.json')], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout, '')
            self.assertIn('Changed evidence', result.stderr)

    def test_state_reference_errors(self):
        for change, expected in [('source', 'source mapping'), ('target', 'unknown claim'),
                                 ('escape', 'escapes'), ('graph', 'Changed evidence')]:
            with self.subTest(change=change), TemporaryDirectory() as temp:
                folder = Path(temp)
                for name in ('example-state.json', 'dependency-example.json', 'gap-comparison.md'):
                    shutil.copyfile(HERE / name, folder / name)
                state = json.loads((folder / 'example-state.json').read_text(encoding='utf-8'))
                if change == 'source':
                    state['node_sources']['selberg'] = ['absent']
                elif change == 'target':
                    state['attempts'][0]['target'] = 'absent'
                elif change == 'escape':
                    state['sources'][0]['path'] = '../outside.md'
                else:
                    with (folder / 'dependency-example.json').open('a', encoding='utf-8') as graph:
                        graph.write(' ')
                (folder / 'example-state.json').write_text(json.dumps(state), encoding='utf-8')
                with self.assertRaisesRegex(ValueError, expected):
                    load_state(folder / 'example-state.json')

    def test_line_endings_do_not_change_fingerprint(self):
        with TemporaryDirectory() as temp:
            path = Path(temp) / 'source.md'
            path.write_bytes(b'alpha\nbeta\n')
            expected = digest(path)
            path.write_bytes(b'alpha\r\nbeta\r\n')
            self.assertEqual(digest(path), expected)

    def test_existing_output_preserved(self):
        with TemporaryDirectory() as temp:
            output = Path(temp) / 'handoff.md'
            output.write_text('keep this', encoding='utf-8')
            result = subprocess.run([sys.executable, str(HERE / 'research_state.py'), 'handoff',
                                     '--output', str(output)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(output.read_text(encoding='utf-8'), 'keep this')


if __name__ == '__main__':
    unittest.main()
