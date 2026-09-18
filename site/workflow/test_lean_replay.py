import json
from pathlib import Path
import shutil
import unittest
from unittest.mock import patch
import subprocess

from lean_replay import replay, source_for

HERE = Path(__file__).parent


class LeanReplayTests(unittest.TestCase):
    def setUp(self):
        self.problem = json.loads((HERE / 'lean-example.json').read_text(encoding='utf-8'))

    def test_statement_is_checked_twice(self):
        source = source_for(self.problem, 'by\n  intro n\n  rfl')
        self.assertEqual(source.count(self.problem['statement']), 2)
        self.assertIn('#print axioms PortfolioCandidate', source)

    @unittest.skipUnless(shutil.which('lean'), 'Lean 4 is required for the compiler integration test')
    def test_real_compiler_rejects_wrong_proof_and_placeholder(self):
        result = replay(self.problem)
        self.assertEqual([r['accepted'] for r in result['results']], [False, False, True])
        self.assertEqual(result['results'][2]['axioms'], [])

    def test_timeout_returns_rejected_candidate(self):
        version = subprocess.CompletedProcess(['lean', '--version'], 0, 'Lean test', '')
        with patch('lean_replay.shutil.which', return_value='lean'), patch(
            'lean_replay.subprocess.run', side_effect=[version] +
            [subprocess.TimeoutExpired('lean', 1)] * 3
        ):
            result = replay(self.problem, timeout=1)
        self.assertTrue(all(r['timed_out'] and not r['accepted'] for r in result['results']))


if __name__ == '__main__':
    unittest.main()
