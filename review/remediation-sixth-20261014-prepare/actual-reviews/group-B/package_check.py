"""Bind the finite review package and check only reviewer payload/authorized scope."""
import datetime, hashlib, json, pathlib, subprocess
ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room');OWN=pathlib.Path(__file__).resolve().parent
PRE='review/remediation-sixth-20261014-prepare/actual-reviews/group-B/'
ACTUAL='86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def identity(d):return dict(bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest())
assert git('branch','--show-current').decode().strip()=='codex/remediation-sixth-actual-b-20261014'
assert git('rev-parse','HEAD').decode().strip()==ACTUAL
assert not git('diff','--name-only')
assert not git('diff','--cached','--name-only')
paths=git('ls-files','--others','--exclude-standard','--',PRE).decode().splitlines()
checks=[]
for p in paths:
 if p==PRE+'package-manifest.json':continue
 data=(ROOT/p).read_bytes();assert not any(l.rstrip(b'\r\n').endswith((b' ',b'\t')) for l in data.splitlines(keepends=True)),p
 checks.append(dict(path=p,mode='100644',type='blob',identity=identity(data)))
patch=json.loads((OWN/'candidate-differences.patch.json').read_text());raw=(OWN/'candidate-differences.patch').read_bytes()
assert patch['patch'].encode()==raw
assert patch['raw_sha256']==hashlib.sha256(raw).hexdigest() and patch['raw_lines']==425
assert json.loads((OWN/'criteria-results.json').read_text())['passed']==9
assert json.loads((OWN/'static-verification.json').read_text())['failed']==0
manifest=dict(schema='R6.actual.group-B.package.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),actual_commit=ACTUAL,
 result='PASS_REVIEWER_SCOPE_AND_PAYLOAD_PACKAGE',payloads=checks,payload_count=len(checks),
 excluded=['package-manifest.json itself (no self-hash)','ignored .scratch/__pycache__/raw candidate-differences.patch; raw diff losslessly preserved in tracked JSON','later commit/push/readback process logs and finite publication receipt'],
 limits='File whitespace/JSON/Git payload validation only; no game behavior execution.',
 preserved_packaging_failure=dict(command=['git','diff','--check','--no-index','/dev/null',PRE+'candidate-differences.patch'],exit=3,UTC='NOT_CAPTURED_SEPARATELY_PLATFORM_OUTPUT_ONLY',reason='Unified diff blank context lines contain their required space; encoded losslessly rather than changing reference/formal content or deleting the working evidence'))
(OWN/'package-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(result=manifest['result'],manifest_payloads=len(checks),lossless_patch_lines=425,reference_model_host_execution=0)))
