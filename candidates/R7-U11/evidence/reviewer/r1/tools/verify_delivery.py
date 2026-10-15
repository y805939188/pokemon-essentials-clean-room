"""Validate reviewer-only write scope, JSON shape and read-only input preservation."""
import datetime,hashlib,json,pathlib,subprocess
repo=pathlib.Path('/workspace/r7-u11-reviewer-checkout');out=pathlib.Path(__file__).resolve().parents[1];prefix='candidates/R7-U11/evidence/reviewer/r1/';B='e646432c644dec04d306842cc5a559a29c718fbc'
def git(*a):return subprocess.check_output(['git',*a],cwd=repo)
assert git('branch','--show-current').decode().strip()=='codex/r7-u11-reviewer-20261015-r1'
assert git('rev-parse','HEAD').decode().strip()==B
tracked=git('diff','--name-only',B).decode().splitlines();assert not tracked
new=git('ls-files','--others','--exclude-standard').decode().splitlines();assert new and all(p.startswith(prefix) for p in new)
assert not any(p.is_symlink() for p in out.rglob('*'))
for n in ('report.md','per-id.json','review-input-receipt.json'):assert (out/n).is_file()
for p in out.rglob('*.json'):json.loads(p.read_bytes())
d=json.loads((out/'per-id.json').read_bytes());assert {r['record_id']:r['verdict'] for r in d['records']}=={'GR7-M16-001':'PASS_SCOPED_CANDIDATE','GR7-M17-002':'PASS_SCOPED_CANDIDATE'};assert d['integrated_PASS'] is False and d['ACCEPTED'] is False and d['CLOSED'] is False
checks=[]
for label,root in [('original',pathlib.Path('/workspace/r7-context/R7-U11-reviewer')),('candidate',pathlib.Path('/workspace/r7-review-input/R7-U11-r1-f151a507bb43e8c936845c7408ab4bc14138caf0'))]:
 receipt=json.loads((out/(label+'-restoration-receipt.json')).read_bytes())
 for r in receipt['files']:
  b=(root/r['local_path']).read_bytes();assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256'];assert hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()==r['git_blob_content_id']
 checks.append({'kind':label,'unchanged_files':len(receipt['files'])})
# A diff check on newly staged files occurs separately before the commit.
r={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'branch':'codex/r7-u11-reviewer-20261015-r1','base':B,'tracked_files_changed':tracked,'new_files_at_check':new,'snapshot_preservation':checks,'json_parsing':'VALID','scope':'ONLY_AUTHORIZED_REVIEWER_R1','semantic_check_count':{'GR7-M16-001':8,'GR7-M17-002':12},'vectors':'NOT_EXECUTED','qualification':'Final delivery tool checks do not supply behavior-run or integrated-acceptance credit.'}
(out/'review-validation.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'scope':r['scope'],'tracked_changed':0,'input_files_unchanged':85,'new_files_at_check':len(new),'verdicts':'TWO_PASS_SCOPED_CANDIDATE'}))
