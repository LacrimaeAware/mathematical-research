"""Validate an AND/OR research dependency map with the Python standard library."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict, deque
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(data):
    nodes, edges = data['nodes'], data['edges']
    ids = [node['id'] for node in nodes]
    require(all(isinstance(n, str) and n for n in ids), 'Node IDs must be nonempty strings')
    require(len(set(ids)) == len(ids), 'Duplicate node IDs')
    known = set(ids)
    require(data['root'] in known, 'Missing root node')
    statuses = set(data['status_vocabulary'])
    for node in nodes:
        require(node['status'] in statuses, f"Unknown status: {node['id']}")
        require(isinstance(node['label'], str) and node['label'].strip(), 'Missing node label')
    outgoing, incoming = defaultdict(set), defaultdict(set)
    indegree = dict.fromkeys(ids, 0)
    edge_keys = set()
    for edge in edges:
        premises, target, logic = edge['from'], edge['to'], edge['logic']
        require(logic in {'AND', 'OR'}, 'Edge logic must be AND or OR')
        require(isinstance(premises, list) and premises, 'Edge needs at least one premise')
        require(len(set(premises)) == len(premises), 'Duplicate premise within edge')
        require(target in known and all(p in known for p in premises), 'Missing node reference')
        key = (tuple(sorted(premises)), target, logic)
        require(key not in edge_keys, 'Duplicate edge')
        edge_keys.add(key)
        for premise in premises:
            incoming[target].add(premise)
            if target not in outgoing[premise]:
                outgoing[premise].add(target)
                indegree[target] += 1
    ready = deque(sorted(n for n in ids if indegree[n] == 0))
    order = []
    while ready:
        node = ready.popleft()
        order.append(node)
        for target in sorted(outgoing[node]):
            indegree[target] -= 1
            if indegree[target] == 0:
                ready.append(target)
    require(len(order) == len(ids), 'Directed cycle detected')
    ancestors = {data['root']}
    pending = [data['root']]
    while pending:
        for parent in incoming[pending.pop()]:
            if parent not in ancestors:
                ancestors.add(parent)
                pending.append(parent)
    return {
        'nodes': len(nodes), 'edges': len(edges),
        'root': data['root'], 'dependency_order': [n for n in order if n in ancestors],
        'detached': sorted(known - ancestors),
        'statuses': dict(sorted(Counter(n['status'] for n in nodes).items())),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?', type=Path,
                        default=Path(__file__).with_name('dependency-example.json'))
    args = parser.parse_args()
    try:
        report = validate(json.loads(args.path.read_text(encoding='utf-8')))
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, f'INVALID: {error}\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
