"""Identity/serialization checks only. Never import or execute recovered/reference code."""
import collections
import hashlib
import json
import pathlib
import re
import subprocess

OUT = pathlib.Path(__file__).resolve().parent
TASK = OUT.parent.parent
REPO = next(p for p in OUT.parents if (p / '.git').exists())
RREPO = pathlib.Path('/workspace/pokemon-essentials')
CONTRACT = '35d85e4484b892ebc32542346861440638d2183c'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
TARGET = '18d21310bdc360c87d7ffd886df7d06aef8604a7'
READSET = TASK / 'continuation/02_ball_base_fields/readset.complete.json'
D = json.loads(READSET.read_text())
C = json.loads((TASK / 'continuation-contracts.json').read_text())
REC = TASK / 'recovered' / TARGET


def git(*args, repo=REPO):
    return subprocess.check_output(['git', '-C', str(repo), *args])


def ident(path):
    b = path.read_bytes()
    return dict(bytes=len(b), sha256=hashlib.sha256(b).hexdigest(),
                git_blob=hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest(),
                mode='100755' if path.stat().st_mode & 0o111 else '100644')


def pointer(doc, ptr):
    for key in ptr.strip('/').split('/'):
        key = key.replace('~1', '/').replace('~0', '~')
        doc = doc[int(key)] if isinstance(doc, list) else doc[key]
    return doc


def put(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')


def main():
    errors = []
    evidence = {'schema': 'r8-cp02-input-validation/v1', 'credit': 'TOOL_VALIDATION_ONLY',
                'contract': CONTRACT, 'target': TARGET, 'B8': B8, 'R': R}
    evidence['git'] = {k: git('rev-parse', v).decode().strip() for k, v in {
        'contract_tree': CONTRACT + '^{tree}', 'B8_tree': B8 + '^{tree}',
        'B8_formal_tree': B8 + ':deliverables/final-specification-set'}.items()}
    evidence['git']['R_commit'] = git('rev-parse', 'HEAD', repo=RREPO).decode().strip()
    evidence['git']['R_tree'] = git('rev-parse', 'HEAD^{tree}', repo=RREPO).decode().strip()
    evidence['git']['R_status'] = git('status', '--porcelain', repo=RREPO).decode()
    assert evidence['git']['R_commit'] == R
    assert evidence['git']['R_tree'] == '7589c800b61ba13a13040ed0d686979b80a84fd0'
    assert evidence['git']['R_status'] == ''
    evidence['contract_files'] = []
    job = next(j for j in C['jobs'] if j['id'] == '02_ball_base_fields')
    for key in ['prompt', 'readset']:
        path = TASK / job[key]
        got = ident(path)
        expected = job[key + '_identity']
        assert all(got[k] == expected[k] for k in got)
        evidence['contract_files'].append(dict(path=str(path.relative_to(REPO)), **got))
    assert len(D['primary_objects']) == 618
    assert set(job['ids']) == {o['id'] for o in D['primary_objects']}
    ids = [i for j in C['jobs'] for i in j.get('ids', [])]
    assert len(ids) == len(set(ids)) == 1045
    evidence['contract_partition'] = {j['id']: len(j.get('ids', [])) for j in C['jobs']}
    evidence['population'] = dict(collections.Counter(o['population'] for o in D['primary_objects']))
    evidence['cached_payloads'] = []
    assert len(D['original_complete_readset']['files']) == 31
    for f in D['original_complete_readset']['files']:
        path = REC / f['relative_to_target_task']
        got = ident(path)
        assert all(got[k] == f[k] for k in got), path
        evidence['cached_payloads'].append(dict(path=str(path.relative_to(REPO)), **got,
                                               remote_path=f['remote_path_at_target_commit']))
    assert sum(f['bytes'] for f in evidence['cached_payloads']) == 1628507
    source_path = D['source_groups'][0]['reference']['path']
    base = RREPO / source_path
    evidence['reference_and_candidate_identities'] = []
    seen = set()
    for f in [g['reference'] for g in D['source_groups']] + D['all_dependency_identity_candidates']:
        key = (f['commit'], f['path'])
        if key in seen:
            continue
        seen.add(key)
        path = (RREPO if f['commit'] == R else REPO) / f['path']
        got = ident(path)
        assert all(got[k] == f[k] for k in ['bytes', 'sha256', 'git_blob']), path
        evidence['reference_and_candidate_identities'].append(dict(commit=f['commit'], path=f['path'], **got))
    raw = {f: json.loads((REC / f).read_text()) for f in {o['origin_file'] for o in D['primary_objects']}}
    for o in D['primary_objects']:
        assert pointer(raw[o['origin_file']], o['origin_pointer']) == o['meaning'], o['id']
    evidence['exact_object_origin_matches'] = 618
    # Parse literal table values, not Ruby expressions. Numeric tones and quoted resource names only.
    lines = base.read_text().splitlines()
    token = re.compile(r'Tone\.new\(([^)]*)\)|"([^"\n]*)"')
    tables = {}
    for pop, start, end, n in [('release_field', 265, 344, 14), ('capture_field', 469, 564, 17)]:
        rows = {}
        ball = None
        for ln in range(start, end + 1):
            line = lines[ln - 1].split('#', 1)[0]
            m = re.search(r':([A-Z]+)\s*=>', line)
            if m:
                ball = m.group(1)
                rows[ball] = []
            for t in token.finditer(line):
                value = [int(v.strip()) for v in t.group(1).split(',')] if t.group(1) is not None else t.group(2)
                rows[ball].append((ln, value))
        assert len(rows) == 16 and all(len(v) == n for v in rows.values())
        for o in [x for x in D['primary_objects'] if x['population'] == pop]:
            ln, value = rows[o['ball']][o['meaning']['index']]
            assert value == o['meaning']['value'] and ln == o['meaning']['source_line'], o['id']
        tables[pop] = rows
    for o in [x for x in D['primary_objects'] if x['population'] == 'RGB_field']:
        line = lines[o['meaning']['source_line'] - 1]
        rgb = re.search(r'Color\.new\(([^)]*)\)', line).group(1)
        assert [int(v.strip()) for v in rgb.split(',')] == o['meaning']['rgb']
    evidence['literal_source_checks'] = {'release_fields': 224, 'capture_fields': 272, 'RGB_fields': 16}
    # Original exact object bytes stay at the fixed readset/origin pointers; do not duplicate 618 wrappers.
    evidence['errors'] = errors
    evidence['result'] = 'IDENTITIES_AND_SERIALIZATION_MATCH'
    put('input-validation.json', evidence)
    print(json.dumps({'result': evidence['result'], 'cached_payloads': 31,
                      'exact_origins': 618, 'literal_checks': evidence['literal_source_checks'],
                      'partition': evidence['contract_partition']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
