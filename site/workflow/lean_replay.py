"""Replay saved Lean proof candidates against one fixed theorem statement.

Requires Lean 4 on PATH. This runner compiles local code; use trusted candidates.
The proof body varies, while the statement and a second type check stay fixed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
from tempfile import TemporaryDirectory

from validate_graph import require


def source_for(problem, proof):
    imports = '\n'.join('import ' + module for module in problem['imports'])
    return (f'{imports}\nset_option maxHeartbeats 100000\n'
            f"theorem PortfolioCandidate : {problem['statement']} :=\n{proof}\n"
            f"example : {problem['statement']} := PortfolioCandidate\n"
            '#check PortfolioCandidate\n#print axioms PortfolioCandidate\n')


def replay(problem, lean='lean', timeout=30):
    executable = shutil.which(lean)
    require(executable is not None, 'Lean executable not found')
    require(isinstance(problem['statement'], str) and problem['statement'].strip(), 'Missing statement')
    require(isinstance(problem['imports'], list) and
            all(re.fullmatch(r'[A-Za-z_][A-Za-z0-9_.]*', m) for m in problem['imports']), 'Invalid import name')
    require(problem['candidates'] and len({c['id'] for c in problem['candidates']}) == len(problem['candidates']),
            'Candidates need unique IDs')
    version = subprocess.run([executable, '--version'], capture_output=True, text=True,
                             encoding='utf-8', timeout=timeout, check=True).stdout.strip()
    allowed = {'propext', 'Classical.choice', 'Quot.sound'}
    results = []
    with TemporaryDirectory(prefix='lean-replay-') as temp:
        path = Path(temp) / 'Candidate.lean'
        for candidate in problem['candidates']:
            source = source_for(problem, candidate['proof'])
            path.write_text(source, encoding='utf-8', newline='\n')
            record = {'id': candidate['id'], 'source_sha256': hashlib.sha256(source.encode()).hexdigest()}
            try:
                run = subprocess.run([executable, '-DwarningAsError=true', 'Candidate.lean'],
                                     cwd=temp, capture_output=True, text=True, encoding='utf-8', timeout=timeout)
                output = run.stdout + run.stderr
                matches = re.findall(r"'PortfolioCandidate' depends on axioms:\s*\[([^\]]*)\]", output)
                no_axioms = "'PortfolioCandidate' does not depend on any axioms" in output
                axioms = sorted({a.strip() for match in matches for a in match.split(',') if a.strip()})
                accepted = run.returncode == 0 and bool(matches or no_axioms) and set(axioms) <= allowed
                record.update(accepted=accepted, exit_code=run.returncode,
                              axioms=axioms, diagnostics=output.strip(), timed_out=False)
            except subprocess.TimeoutExpired:
                record.update(accepted=False, exit_code=None, axioms=[], diagnostics='Compiler timeout', timed_out=True)
            results.append(record)
    return {'problem': problem['id'], 'statement': problem['statement'], 'lean_version': version,
            'allowed_axioms': sorted(allowed), 'timeout_seconds': timeout, 'results': results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('problem', nargs='?', type=Path, default=Path(__file__).with_name('lean-example.json'))
    parser.add_argument('--lean', default='lean')
    parser.add_argument('--timeout', type=int, default=30)
    args = parser.parse_args()
    try:
        require(args.timeout > 0, 'Timeout must be positive')
        result = replay(json.loads(args.problem.read_text(encoding='utf-8')), args.lean, args.timeout)
    except (ValueError, KeyError, TypeError, OSError, subprocess.SubprocessError) as error:
        parser.exit(1, f'ERROR: {error}\n')
    print(json.dumps(result, indent=2))
    if not any(r['accepted'] for r in result['results']):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
