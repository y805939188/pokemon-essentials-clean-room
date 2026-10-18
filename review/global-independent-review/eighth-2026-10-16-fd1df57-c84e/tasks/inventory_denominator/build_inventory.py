#!/usr/bin/env python3
"""Read-only inventory. Metadata enumeration grants no semantic-read credit."""
import collections
import datetime
import hashlib
import json
import mimetypes
import os
from pathlib import Path
import stat
import subprocess

OUT = Path(__file__).resolve().parent
B = Path('/workspace/pokemon-essentials-clean-room')
R = Path('/workspace/pokemon-essentials')
BC = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
RC = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'

def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])

def tree(repo, commit):
    result = {}
    for record in git(repo, 'ls-tree', '-rz', '-l', commit).split(b'\0'):
        if not record:
            continue
        meta, path = record.split(b'\t', 1)
        mode, kind, blob, size = meta.decode().split()
        result[path.decode()] = {'git_mode': mode, 'git_type': kind,
                                 'git_blob': blob, 'git_bytes': int(size) if size != '-' else None}
    return result

def digest(data):
    return hashlib.sha256(data).hexdigest()

def inventory(repo, commit, paths, scope, tracked):
    repo_tree = git(repo, 'rev-parse', commit + '^{tree}').decode().strip()
    result = []
    for path in sorted(paths):
        absolute = repo / path
        entry = {'repo': str(repo), 'commit': commit, 'workspace_tree': repo_tree,
                 'path': path, 'scope': scope, 'responsible_task': 'inventory_denominator',
                 'evidence_level': 'INVENTORY_ONLY', 'semantic_status': 'UNREAD',
                 'read_range': None, 'purpose': scope, 'tracked': path in tracked,
                 'type': mimetypes.guess_type(path)[0] or 'application/octet-stream'}
        entry.update(tracked.get(path, {'git_mode': None, 'git_type': None,
                                        'git_blob': None, 'git_bytes': None}))
        if absolute.exists() or absolute.is_symlink():
            info = absolute.lstat()
            data = os.readlink(absolute).encode() if stat.S_ISLNK(info.st_mode) else absolute.read_bytes()
            entry.update(actual_mode=oct(stat.S_IMODE(info.st_mode)), actual_kind='symlink' if stat.S_ISLNK(info.st_mode) else 'regular_file',
                         bytes=len(data), sha256=digest(data), actual_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(), exists=True)
            entry['matches_git_blob'] = entry['actual_blob'] == entry['git_blob'] if entry['tracked'] else None
        else:
            entry.update(actual_mode=None, actual_kind='MISSING', bytes=None, sha256=None,
                         actual_blob=None, exists=False, matches_git_blob=False)
        result.append(entry)
    return result

def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

rt, bt = tree(R, RC), tree(B, BC)
rpaths = set(rt)
for base, dirs, files in os.walk(R):
    dirs[:] = [d for d in dirs if d != '.git']
    for filename in files:
        rpaths.add(str((Path(base)/filename).relative_to(R)))
rinventory = inventory(R, RC, rpaths, 'reference_all_existing_plus_tracked', rt)
write('reference-inventory.json', rinventory)

prefixes = {'formal': 'deliverables/final-specification-set/', 'planning': 'planning/',
            'audit': 'audit/', 'delivery_navigation': 'delivery/2026-10-16-seventh/',
            'r7_supplement_candidate': 'review/remediation-seventh-20261015-prepare/',
            'r6_supplement_candidate': 'review/remediation-sixth-20261014-prepare/'}
binventory = []
for scope, prefix in prefixes.items():
    paths = {p for p in bt if p.startswith(prefix)}
    for base, dirs, files in os.walk(B / prefix):
        for filename in files:
            paths.add(str((Path(base)/filename).relative_to(B)))
    part = inventory(B, BC, paths, scope, bt)
    binventory.extend(part)
    write(scope+'-inventory.json', part)
binventory.extend(inventory(B, BC, ['README.md','CURRENT-DELIVERY.md','AGENTS.md'], 'root_current_navigation', bt))
write('b8-scoped-inventory.json', binventory)

# Parse links as candidates only; semantic currentness is owned by history_current.
navpaths = ['delivery/2026-10-16-seventh/eighth-review-inputs.json',
            'delivery/2026-10-16-seventh/history-navigation.json',
            'review/remediation-seventh-20261015-prepare/completion/final-delivery-binding.json']
links = []
def walk(value, pointer, source):
    if isinstance(value, dict):
        for k, v in value.items():
            walk(v, pointer+'/'+k.replace('~','~0').replace('/','~1'), source)
    elif isinstance(value, list):
        for i, v in enumerate(value):
            walk(v, pointer+'/'+str(i), source)
    elif isinstance(value, str) and '/' in value and not value.startswith(('http:', 'https:', 'refs/')):
        links.append({'source': source, 'pointer': pointer, 'value': value,
                      'path_at_B8': value if value in bt else None,
                      'classification': 'MECHANICAL_LINK_CANDIDATE_NOT_SEMANTIC_ACCEPTANCE'})
for p in navpaths:
    walk(json.loads((B/p).read_text()), '', p)
write('supplement-navigation-link-candidates.json', links)
resolved = sorted({x['path_at_B8'] for x in links if x['path_at_B8']})
write('navigation-reachable-b8-inventory.json', inventory(B, BC, resolved, 'navigation_reachable_at_B8_candidate', bt))
summary = {'schema': 'gr8-inventory-summary/v1', 'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'mechanical_only': True, 'update_started': False,
           'reference': {'tracked': len(rt), 'existing': sum(x['exists'] for x in rinventory),
                         'extra_existing': [x['path'] for x in rinventory if not x['tracked']],
                         'missing_tracked': [x['path'] for x in rinventory if not x['exists']],
                         'mismatched_tracked': [x['path'] for x in rinventory if x['tracked'] and not x['matches_git_blob']]},
           'b8_tracked_all': len(bt),
           'b8_scoped_counts': dict(collections.Counter(x['scope'] for x in binventory)),
           'navigation_candidates': len(links), 'navigation_distinct_resolved_B8_paths': len(resolved),
           'supplement_currentness': 'UNVERIFIED_PENDING_HISTORY_CURRENT_ACCEPTANCE',
           'inventory_mismatches': [x['path'] for x in binventory if x['tracked'] and not x['matches_git_blob']]}
write('inventory-summary.json', summary)
for name, entries in [('reference-paths.txt', rinventory), ('b8-scoped-paths.txt', binventory)]:
    (OUT/name).write_text(''.join(x['path']+'\n' for x in entries))
print(json.dumps(summary, ensure_ascii=False))
