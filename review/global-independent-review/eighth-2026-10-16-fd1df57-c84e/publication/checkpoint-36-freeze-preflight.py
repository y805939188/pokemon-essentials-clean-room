"""C35 read-only preparation; never freeze, stage, commit, push or fetch a target."""
from pathlib import Path
import concurrent.futures, datetime, hashlib, json, subprocess

W = Path('/workspace/pokemon-essentials-clean-room')
R = Path('/workspace/pokemon-essentials')
PREFIX = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
RR = W / PREFIX
PUB = RR / 'publication'
IO = PUB / 'checkpoint-36-io'
IO.mkdir(exist_ok=True)
HEAD = '2460370f1e410bd49cc29e377b89662838aed2b3'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
BRANCH = 'codex/review-eighth-20261016-fd1df57-c84e'
FORMAL = 'f292698cdd4a8e725525a9be6dc34b75faaf151e'
commands = [
    [str(W), 'branch', '--show-current'],
    [str(W), 'rev-parse', B8+'^{tree}'],
    [str(W), 'rev-parse', B8+':deliverables/final-specification-set'],
    [str(W), 'diff', '--name-only', '-z', B8],
    [str(W), 'status', '--porcelain', '-z', '--untracked-files=all'],
    [str(R), 'rev-parse', 'HEAD'],
    [str(R), 'rev-parse', 'HEAD^{tree}'],
    [str(R), 'status', '--porcelain', '-z', '--untracked-files=all'],
    [str(W), 'ls-remote', 'origin', 'refs/heads/main',
     'refs/tags/delivery/seventh-round-closed-final-20261016', 'refs/heads/'+BRANCH],
    [str(W), 'rev-parse', 'HEAD'],
    [str(W), 'diff', '--cached', '--name-only', '-z'],
    [str(W), 'rev-parse', 'HEAD:deliverables/final-specification-set'],
]

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def run(item):
    i, args = item
    argv = ['git', '-C', *args]
    start = now()
    p = subprocess.run(argv, capture_output=True)
    out = {'args': argv, 'start_utc': start, 'end_utc': now(), 'exit': p.returncode}
    for key, value in [('stdout', p.stdout), ('stderr', p.stderr)]:
        path = IO / ('freeze-preflight-%02d.%s' % (i+1, key))
        assert not path.exists(), str(path)
        path.write_bytes(value)
        out.update({key: str(path.relative_to(RR)), key+'_bytes': len(value),
                    key+'_sha256': hashlib.sha256(value).hexdigest()})
    return out, p.stdout

with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
    results = list(pool.map(run, enumerate(commands)))
events = [x[0] for x in results]
raw = [x[1] for x in results]
assert all(e['exit'] == 0 for e in events)

def paths_z(value):
    return [x.decode() for x in value.split(b'\0') if x]

def porcelain_paths(value):
    rows = value.split(b'\0')
    result = []
    i = 0
    while i < len(rows):
        entry = rows[i]
        i += 1
        if not entry:
            continue
        assert len(entry) >= 4 and entry[2:3] == b' ', entry
        result.append(entry[3:].decode())
        if b'R' in entry[:2] or b'C' in entry[:2]:
            assert i < len(rows) and rows[i]
            result.append(rows[i].decode())
            i += 1
    return result

diff_paths, dirty_paths = paths_z(raw[3]), porcelain_paths(raw[4])
refs = {line.split()[1]: line.split()[0] for line in raw[8].decode().splitlines()}
checks = dict(
    branch=raw[0].decode().strip() == BRANCH,
    B8_tree=raw[1].decode().strip() == '751dfde81048c81390f89a65ca1d1a565ba8e1ca',
    B8_formal=raw[2].decode().strip() == FORMAL,
    report_only_diff=all(p.startswith(PREFIX+'/') for p in diff_paths),
    report_only_status=all(p.startswith(PREFIX+'/') for p in dirty_paths),
    R_HEAD=raw[5].decode().strip() == '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
    R_tree=raw[6].decode().strip() == '7589c800b61ba13a13040ed0d686979b80a84fd0',
    R_clean=raw[7] == b'',
    protected_remote=refs.get('refs/heads/main') == B8 and refs.get('refs/tags/delivery/seventh-round-closed-final-20261016') == B8,
    HEAD=raw[9].decode().strip() == HEAD,
    empty_index=raw[10] == b'',
    HEAD_formal=raw[11].decode().strip() == FORMAL,
    remote_report_HEAD=refs.get('refs/heads/'+BRANCH) == HEAD,
)
out = dict(schema='gr8-checkpoint36-freeze-preflight/v1', utc=now(),
           status='PASS' if all(checks.values()) else 'FAILED', checks=checks,
           HEAD=HEAD, report_branch=BRANCH, events=events,
           diff_path_count=len(diff_paths), dirty_path_count=len(dirty_paths),
           path_differences_outside_RR=sorted(p for p in set(diff_paths+dirty_paths) if not p.startswith(PREFIX+'/')),
           candidate_freeze='NOT_STARTED', staging='NOT_STARTED', commit='NOT_STARTED',
           push='NOT_STARTED', target_remote_readback='NOT_STARTED',
           new_contexts=0, new_votes=0, semantic_credit='NONE',
           business_execution='NOT_EXECUTED', UPDATE_NOT_STARTED=True,
           actual_model='UNVERIFIED', actual_effort='UNVERIFIED', actual_service_tier='UNVERIFIED',
           actual_speed='UNVERIFIED', actual_Fast='UNVERIFIED', actual_UUID='UNVERIFIED')
destination = PUB / 'checkpoint-36-freeze-preflight.json'
assert not destination.exists()
destination.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({k: out[k] for k in ['status', 'HEAD', 'checks', 'diff_path_count', 'dirty_path_count']}, ensure_ascii=False))
assert out['status'] == 'PASS'
