"""Inventory new report payloads; current file identity is bound externally after commit."""
import argparse,datetime,hashlib,json,pathlib,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1];REPO=ROOT.parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
files=[p for p in ROOT.rglob('*') if p.is_file() and 'temporary' not in p.relative_to(ROOT).parts]
encoded=b'\0'.join(str(p.relative_to(REPO)).encode() for p in files)+b'\0'
ignored=subprocess.run(['git','check-ignore','-z','--stdin'],cwd=REPO,input=encoded,capture_output=True)
assert ignored.returncode in (0,1)
exclusions={x.decode() for x in ignored.stdout.split(b'\0') if x}
out=[]
for p in sorted(files):
 path=str(p.relative_to(REPO));rel=str(p.relative_to(ROOT))
 if path in exclusions or rel==a.output:continue
 data=p.read_bytes();kind='binary'
 try:data.decode('utf-8');kind='utf8_text'
 except UnicodeDecodeError:pass
 purpose='generated audit evidence/identity/index' if p.suffix in ('.json','.jsonl','.tsv','.gz') else 'review report/contract' if p.suffix=='.md' else 'read-only audit tooling' if p.suffix in ('.py','.rb') else 'raw acquisition/execution output'
 out.append({'path':path,'relative_path':rel,'commit_assignment':'semantic core external publication binding',
 'tree_attribution':'report directory tree in external receipt','bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
 'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),
 'type':kind,'purpose':purpose,'reading_scope':'actual source/data reading, full finite parse, independent assessment or raw command log as writer ledgers and final domain reports specify; not root full-text credit for every administrative/log line',
 'evidence_level':'SOURCE_STATIC/DERIVED_VECTOR/TOOL_VALIDATION/REFERENCE_OBSERVATION differentiated in owning record, not inferred from this inventory'})
result={'schema':'r6.report-payloads.v1','created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'entries':out,'files':len(out),'bytes':sum(x['bytes'] for x in out),'excluded_self':a.output,
 'ignored_inputs':'temporary object cache and six fixed-source binary copies remain isolated; recover from exact fixed R through tools/recover_isolated_inputs.py',
 'ignored_pycache':True,'post_creation_command_receipts_bound_by_later_actual_git_tree':True,'update_started':False}
(ROOT/a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='entries'},ensure_ascii=False))
