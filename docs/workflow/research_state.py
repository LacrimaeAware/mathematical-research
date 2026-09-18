"""Check research evidence and compile a dependency-aware Markdown handoff.

Python 3.10+, standard library only. Files referenced by a state must be within
its directory. Neither command changes the state or accepts new fingerprints.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from validate_graph import require, validate


def digest(path):
    # Normalize line endings so Git checkouts agree across Windows and Linux.
    content = path.read_text(encoding='utf-8').replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def local_file(base, name):
    require(isinstance(name, str) and bool(name), 'Missing artifact path')
    relative = Path(name)
    require(not relative.is_absolute(), 'Artifact paths must be relative')
    candidate = (base / relative).resolve()
    require(candidate.is_relative_to(base.resolve()), 'Artifact path escapes the state directory')
    require(candidate.is_file(), f'Missing artifact: {name}')
    return candidate


def load_state(path):
    state = json.loads(path.read_text(encoding='utf-8'))
    require(state['schema_version'] == 1, 'Unsupported schema version')
    graph_path = local_file(path.parent, state['graph']['path'])
    graph = json.loads(graph_path.read_text(encoding='utf-8'))
    report = validate(graph)
    stale = []
    if digest(graph_path) != state['graph']['sha256']:
        stale.append(state['graph']['path'])
    sources = {}
    for source in state['sources']:
        require(source['id'] not in sources, 'Duplicate source ID')
        source_path = local_file(path.parent, source['path'])
        sources[source['id']] = source
        if digest(source_path) != source['sha256']:
            stale.append(source['path'])
    require(sources, 'At least one reviewed source is required')
    node_ids = {n['id'] for n in graph['nodes']}
    require(set(state['node_sources']) == node_ids, 'Source mapping must cover exactly the graph nodes')
    for refs in state['node_sources'].values():
        require(isinstance(refs, list) and refs and all(r in sources for r in refs), 'Unknown or empty source mapping')
    attempt_ids = set()
    for attempt in state['attempts']:
        require(attempt['id'] not in attempt_ids, 'Duplicate attempt ID')
        attempt_ids.add(attempt['id'])
        require(attempt['target'] in node_ids, 'Attempt targets an unknown claim')
        require(attempt['status'] in {'proposed', 'in_progress', 'completed', 'route_failed'}, 'Unknown attempt status')
        for field in ('question', 'method', 'check', 'outcome'):
            require(isinstance(attempt[field], str) and attempt[field].strip(), f'Missing attempt {field}')
    require(not stale, 'Changed evidence; review before compiling: ' + ', '.join(stale))
    return state, graph, report


def compile_handoff(state, graph, report):
    nodes = {n['id']: n for n in graph['nodes']}
    selected = set(report['dependency_order'])
    lines = ['# Research handoff', '', '## Claim', '', nodes[graph['root']]['label'], '',
             '## Dependencies and recorded support', '']
    for node_id in report['dependency_order']:
        node = nodes[node_id]
        refs = ', '.join(state['node_sources'][node_id])
        lines.append(f"- **{node_id}** — {node['label']} ({node['status']}; source: {refs}).")
    lines += ['', '## Dependency rules', '']
    for edge in graph['edges']:
        if edge['to'] in selected:
            joiner = ' AND ' if edge['logic'] == 'AND' else ' OR '
            lines.append(f"- ({joiner.join(edge['from'])}) → {edge['to']}")
    lines += ['', '## External inputs', '']
    external = [n for n in report['dependency_order'] if nodes[n]['status'] == 'external_input']
    lines += [f"- {nodes[n]['label']}" for n in external] or ['None recorded.']
    lines += ['', '## Attempts and questions', '']
    for attempt in state['attempts']:
        if attempt['target'] not in selected:
            continue
        lines += [f"### {attempt['id']} · {attempt['status']}", '', attempt['question'], '',
                  f"Method: {attempt['method']}", '', f"Check: {attempt['check']}", '',
                  f"Recorded outcome: {attempt['outcome']}", '']
    lines += ['## Source manifest', '', 'SHA-256 of UTF-8 text with LF line endings.', '',
              f"- Graph: `{state['graph']['path']}` — `{state['graph']['sha256']}`"]
    used = {ref for n in selected for ref in state['node_sources'][n]}
    for source in state['sources']:
        if source['id'] in used:
            lines.append(f"- {source['id']}: `{source['path']}` — `{source['sha256']}`")
    return '\n'.join(lines).rstrip() + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['check', 'handoff'])
    parser.add_argument('state', nargs='?', type=Path, default=Path(__file__).with_name('example-state.json'))
    parser.add_argument('--output', type=Path, help='Write a new handoff file; existing files are preserved')
    args = parser.parse_args()
    try:
        state, graph, report = load_state(args.state)
        if args.command == 'check':
            require(args.output is None, '--output is only supported for handoff')
            print(json.dumps({'pass': True, 'reviewed_sources': len(state['sources']), **report}, indent=2))
        else:
            result = compile_handoff(state, graph, report)
            if args.output:
                with args.output.open('x', encoding='utf-8', newline='\n') as output:
                    output.write(result)
            else:
                print(result, end='')
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, f'INVALID: {error}\n')


if __name__ == '__main__':
    main()
