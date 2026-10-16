"""Guarded C35 transport verifier. --check-config performs no target fetch."""
from pathlib import Path
import datetime, hashlib, json, re, subprocess, sys

W = Path('/workspace/pokemon-essentials-clean-room')
PREFIX = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
RR = W / PREFIX
PUB = RR / 'publication'
IO = PUB / 'checkpoint-35-io'
BASELINE = 'publication/r8-four-receivers-and-metadata-readback-34.json'
BASE_SHA = '9c8576ad239dd37794f87530806d71b25cb2df3f1f570a87d444bc008f0a862c'
BASE_COMMIT = '81cc98eec7cc81706e51c8b274e9ff7042c0868b'
BASE_TREE = '6dff475826daa5e4b90c5cd6f5f30e2634962229'
TRUSTED_SHA = 'c7993a3be2b3d0a4dfefd464e086a274c8bccc27f13dffa96a1647627c4d46ba'
SEED = Path('/workspace/scratch/r8-four-receivers-and-metadata-readback-34/remote.git')
FLAT = Path('/workspace/scratch/checkpoint-34-flat-verified-c33/remote.git')
events = []

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def run(argv):
    start = now()
    p = subprocess.run(argv, capture_output=True)
    events.append(dict(args=argv, start_utc=start, end_utc=now(), exit=p.returncode,
                       stdout=p.stdout.decode(errors='replace'), stderr=p.stderr.decode(errors='replace')))
    return p

def ident(path):
    raw = path.read_bytes()
    return dict(path=str(path.relative_to(RR)), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())

def check_config():
    raw = (RR / BASELINE).read_bytes()
    assert len(raw) == 27194524 and hashlib.sha256(raw).hexdigest() == BASE_SHA
    base = json.loads(raw)
    assert (base['status'], base['commit'], base['report_tree'], base['isolated_git_dir']) == ('VERIFIED', BASE_COMMIT, BASE_TREE, str(SEED))
    assert base['compressed_original_count'] == 116
    trusted = PUB / 'incremental-remote-readback.py'
    assert hashlib.sha256(trusted.read_bytes()).hexdigest() == TRUSTED_SHA
    assert SEED.is_dir() and FLAT.is_dir()
    assert (SEED / 'objects/info/alternates').read_text() == str(FLAT / 'objects')+'\n'
    assert not (FLAT / 'objects/info/alternates').exists()
    assert SEED.resolve().is_relative_to('/workspace/scratch')
    assert FLAT.resolve().is_relative_to('/workspace/scratch')
    assert not SEED.resolve().is_relative_to(W / '.git')
    p = run(['git', '-C', str(SEED), 'rev-parse', BASE_COMMIT+':'+PREFIX])
    assert p.returncode == 0 and p.stdout.decode().strip() == BASE_TREE
    # Adapter differs only by complete init/tree logging and explicit provenance.
    source = trusted.read_text()
    old_init = "p=subprocess.run(['git','init','--bare',str(bare)],capture_output=True);assert p.returncode==0"
    new_init = "init_start=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.run(['git','init','--bare',str(bare)],capture_output=True);events.append(dict(args=['init','--bare',str(bare)],git_dir=str(bare.parent),start_utc=init_start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit=p.returncode,stdout=p.stdout.decode(errors='replace'),stderr=p.stderr.decode(errors='replace')));assert p.returncode==0"
    old_tree = "raw=subprocess.check_output(['git','-C',str(where),'ls-tree','-r','-z',c,'--',prefix])"
    new_tree = "raw=run(where,'ls-tree','-r','-z',c,'--',prefix).stdout"
    assert source.count(old_init) == source.count(old_tree) == 1
    source = source.replace(old_init, new_init).replace(old_tree, new_tree)
    marker = "destination=r/'publication'/f'{name}.json';destination.write_text"
    assert source.count(marker) == 1
    provenance = "out.update(original_trusted_verifier_source_sha256='"+TRUSTED_SHA+"',baseline_flattening_receipt='publication/checkpoint-34-flat-seed-provenance.json',baseline_flattening_receipt_sha256='51449150b024fac59fd168ae28b7443d868b0c16598d070eaace808c6e5d41d5',c35_seed_policy='C34 verified remote cache backed only by C33 flat remote cache; no legacy deep alternate chain and no current worktree object source.',verifier_adaptation='Only init/tree command logging and provenance; original exact commit/tree/delta/changed-blob/116gzip assertions retained.');"
    source = source.replace(marker, provenance+marker)
    adapter = PUB / 'checkpoint-35-adapted-incremental-readback.py'
    assert adapter.read_text() == source, 'Adapter exact derivation mismatch'
    return dict(baseline=ident(RR / BASELINE), trusted=ident(trusted), adapter=ident(adapter),
                wrapper=ident(Path(__file__)), successful_seed=str(SEED), flat_backing=str(FLAT),
                alternate_layers_after_new_fresh_bare=2, flat_has_no_alternates=True,
                original_target_tree_blob_gzip_assertions_retained=True)

def main():
    deps = check_config()
    if sys.argv[1:] == ['--check-config']:
        head = run(['git', '-C', str(W), 'rev-parse', 'HEAD'])
        assert head.returncode == 0 and head.stdout.decode().strip() == BASE_COMMIT
        result = dict(schema='gr8-checkpoint35-readback-readiness/v1', utc=now(),
                      status='CONFIG_VERIFIED_NO_TARGET_FETCH', dependencies=deps, events=events,
                      candidate_freeze='NOT_STARTED', staging='NOT_STARTED', commit='NOT_STARTED',
                      push='NOT_STARTED', target_remote_readback='NOT_STARTED',
                      semantic_credit='NONE', business_execution='NOT_EXECUTED', UPDATE_NOT_STARTED=True)
        dest = PUB / 'checkpoint-35-readback-readiness.json'
        assert not dest.exists()
        dest.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
        print(json.dumps(dict(status=result['status'], dependencies=deps), ensure_ascii=False))
        return
    assert len(sys.argv) == 3, 'Usage: wrapper --check-config OR wrapper EXACT_COMMIT UNUSED_READBACK_NAME'
    commit, name = sys.argv[1:]
    assert re.fullmatch('[0-9a-f]{40}', commit) and commit != BASE_COMMIT
    assert re.fullmatch('r8-[a-z0-9-]+-readback-35', name)
    assert not (Path('/workspace/scratch') / name).exists()
    assert not (PUB / (name+'.json')).exists()
    head = run(['git', '-C', str(W), 'rev-parse', 'HEAD'])
    assert head.returncode == 0 and head.stdout.decode().strip() == commit
    remote = run(['git', '-C', str(W), 'ls-remote', 'origin', 'refs/heads/codex/review-eighth-20261016-fd1df57-c84e'])
    assert remote.returncode == 0 and remote.stdout.decode().split() == [commit, 'refs/heads/codex/review-eighth-20261016-fd1df57-c84e']
    absent = run(['git', '-C', str(SEED), 'cat-file', '-e', commit+'^{commit}'])
    assert absent.returncode != 0, 'New target must be absent in successful C34 seed before fresh fetch'
    IO.mkdir(exist_ok=True)
    log = IO / 'target-readback-wrapper.json'
    assert not log.exists()
    # Persist guard evidence even if the trusted verifier later fails.
    record = dict(utc=now(), status='GUARDS_PASSED_VERIFYING', commit=commit, name=name, dependencies=deps, events=events)
    log.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    p = run([sys.executable, '-B', str(PUB / 'checkpoint-35-adapted-incremental-readback.py'), commit, name, BASELINE])
    for key in ['stdout', 'stderr']:
        (IO / ('target-readback.'+key)).write_text(events[-1][key])
    record.update(utc=now(), status='VERIFIER_SUCCEEDED' if p.returncode == 0 else 'VERIFIER_FAILED', events=events)
    log.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    print(p.stdout.decode(errors='replace'), end='')
    if p.stderr:
        print(p.stderr.decode(errors='replace'), end='', file=sys.stderr)
    assert p.returncode == 0

if __name__ == '__main__':
    main()
