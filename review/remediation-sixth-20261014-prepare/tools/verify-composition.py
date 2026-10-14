#!/usr/bin/env python3
"""Finite byte/hunk preservation checks. This tool does not sign semantic acceptance."""
import argparse, collections, difflib, hashlib, json, re, subprocess
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('input')
p.add_argument('--commit')
p.add_argument('--formal-root', help='Optional read-only staged formal mirror, before formal receipt')
args=p.parse_args()
repo=Path(__file__).resolve().parents[3]
def git(*a):return subprocess.check_output(['git',*a],cwd=repo)
def blob(commit,path):return git('cat-file','blob',commit+':'+path)
def identity(data):return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}
def read(path):
 if args.commit:return blob(args.commit,path)
 if args.formal_root and path.startswith('deliverables/final-specification-set/'):
  return (Path(args.formal_root)/path).read_bytes()
 return (repo/path).read_bytes()
def rows(data):
 # Existing catalogs reuse short IDs in named families (e.g. AI:S10 and AE:S10).
 # Check raw rows before indexing and retain that namespace; never collapse to a dict first.
 result=collections.Counter();family='document'
 for line in data.decode().splitlines():
  if line.startswith('## '):family=re.split(r'[（(]',line[3:],maxsplit=1)[0].strip()
  m=re.match(r'^\|\s*([^|]+?)\s*\|',line)
  if m and re.fullmatch(r'[A-Za-z][A-Za-z0-9_.:-]*[0-9][A-Za-z0-9_.:-]*',m.group(1).strip()):result[family+'::'+m.group(1).strip()]+=1
 return result
d=json.loads(read(args.input))
assert len(d['required_ids'])==d['required_count'] and len(set(d['required_ids']))==d['required_count']
assert len(d['batches']) in (12,13,14) and len({b['batch'] for b in d['batches']})==len(d['batches'])
assert {i for b in d['batches'] for i in b['required_ids']}==set(d['required_ids'])
assert sum(len(b['required_ids']) for b in d['batches'])==d['required_count']
assert len({f['path'] for f in d['files']})==len(d['files'])
checks=[];contributions=0;new_lines=0;navigation_mappings=0
for f in d['files']:
 actual=read(f['path']);assert identity(actual)==f['actual'],f['path']
 base=blob(d['fixed_main'],f['path']);assert identity(base)==f['baseline']
 assert actual!=base and not re.search(rb'^(<<<<<<<|\|\|\|\|\|\|\||=======|>>>>>>>)',actual,re.M)
 actual_lines=actual.decode().splitlines();line_set=set(actual_lines)
 for c in f['contributions']:
  candidate=blob(c['candidate_commit'],c['candidate_path'])
  assert identity(candidate)==c['identity']
  candidate_base=blob(d['preparation_commit'],c['candidate_path']);assert candidate_base==base
  assert candidate!=base
  a=base.decode().splitlines();b=candidate.decode().splitlines()
  # Preserve each exact added/replacement block in order. Merge context can differ.
  for kind,i,j,u,v in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
   if kind in ('replace','insert'):
    block=b[u:v]
    for resolution in d['resolutions']:
     if resolution['path']==f['path'] and 'candidate_lines' in resolution:
      assert f['path']=='deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md'
      old=resolution['candidate_lines'].get(c['batch'])
      if old and old in block:
       base_line=resolution['baseline_line'];ours=resolution['candidate_lines']['R6-U09'];theirs=resolution['candidate_lines']['R6-U14']
       assert base_line in a and ours.startswith(base_line) and ours!=base_line
       assert theirs==base_line.replace('的 KL01–KL36（','的 KL01–KL36 及 R6-U14-FLAGS 静态对照（',1)
       assert resolution['actual_line']==theirs+ours[len(base_line):]
       block=[resolution['actual_line'] if x==old else x for x in block];navigation_mappings+=1
    if any(x.strip() for x in block):
     hay=actual_lines;needle=block
     if f['path']=='deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md':
      assert any(x['path']==f['path'] and x.get('semantic_change') is False for x in d['root_edits'])
      hay=[x for x in hay if x.strip()];needle=[x for x in needle if x.strip()]
     assert any(hay[k:k+len(needle)]==needle for k in range(len(hay)-len(needle)+1)),(f['path'],c['batch'],'lost candidate block',u,v)
    new_lines+=sum(bool(x.strip()) for x in block)
  contributions+=1
 before=rows(base);after=rows(actual)
 increased_duplicates={k:v for k,v in after.items() if v>1 and v>before[k]}
 assert not increased_duplicates,(f['path'],increased_duplicates)
 checks.append({'path':f['path'],'contributions':len(f['contributions']),'baseline_case_rows':sum(before.values()),'actual_case_rows':sum(after.values()),'removed_case_ids':sorted(before.keys()-after.keys()),'increased_duplicate_case_ids':increased_duplicates})
payload=blob(d['receiver_delta']['payload_commit'],d['receiver_delta']['payload_path'])
receiver=json.loads(payload);actual=read(receiver['receiver_path']).decode()
assert actual.count(receiver['proposed_full_line'])==1 and receiver['old_full_line'] not in actual
assert d['receiver_delta']['applied'] and not d['receiver_delta']['INTEGRATED_PASS']
for b in d['batches']:
 contract=read(b['contract_path']);assert identity(contract)==b['contract_identity']
 assert json.loads(contract)['required_ids']==b['required_ids']
 report=blob(b['independent_review']['review_commit'],b['independent_review']['report_path'])
 # U04 report identity is stored in the actual input for this composite, as for all other reports.
 assert identity(report)==b['independent_review']['report_identity']
 assert b['candidate_published_commit'] in report.decode()
 assert b['required_ids'] and b['author_cloud_thread_id']!=b['independent_review']['reviewer_cloud_thread_id']
 prefix='review/remediation-sixth-20261014-prepare/candidates/'+b['batch']+'/mirror/'
 expected=set(git('diff-tree','--no-commit-id','--name-only','-r',d['preparation_commit'],b['candidate_published_commit'],'--',prefix).decode().splitlines())
 received={c['candidate_path'] for f in d['files'] for c in f['contributions'] if c['batch']==b['batch']}
 assert received==expected,(b['batch'],'missing/extra candidate paths',sorted(expected-received),sorted(received-expected))
assert d['state']=='ACTUAL_COMPOSITION_PENDING_INDEPENDENT_REVIEW'
assert not d['INTEGRATED_PASS'] and not d['formal_acceptance'] and not d['CLOSED']
print(json.dumps({'evidence_level':'TOOL_VALIDATION','files_full_byte_bound':len(checks),'contributions_added_blocks_retained':contributions,'explicit_shared_navigation_line_mappings':navigation_mappings,'nonblank_candidate_added_lines_checked':new_lines,'receiver_clause_exact':True,'case_row_checks':checks,'reference_model_host_Demo_execution':0,'semantic_PASS':False,'INTEGRATED_PASS':False,'accepted':0,'CLOSED':0},ensure_ascii=False))
