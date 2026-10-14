#!/usr/bin/env python3
"""Bounded text/identity checks only. Does not load or execute reference code."""
from pathlib import Path
import json,hashlib,subprocess,difflib,re
repo=Path(__file__).resolve().parents[5]
p=repo/'review/remediation-sixth-20261014-prepare'
e=p/'candidates/R6-U02/evidence'
c=json.loads((p/'contracts/R6-U02.json').read_text())
inputs=json.loads((p/'inputs/frozen-inputs.json').read_text())
prepare='469a268b92daed7b4d28d7fd0da75520cbb7228f'
branch='codex/remediation-sixth-r6-u02-author-20261014'
def git(*a):return subprocess.check_output(['git',*a],cwd=repo)
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
assert git('branch','--show-current').decode().strip()==branch
subprocess.run(['git','merge-base','--is-ancestor',prepare,'HEAD'],cwd=repo,check=True)
changed=git('diff','--name-only',prepare).decode().splitlines()
allowed={str((p/'candidates/R6-U02/mirror'/x).relative_to(repo)) for x in c['candidate_formal_paths']}
assert all(x in allowed or x.startswith(str(e.relative_to(repo))+'/') for x in changed)
subprocess.run(['git','diff','--check',prepare],cwd=repo,check=True)
assert git('diff',prepare,'--','deliverables','audit','planning','AGENTS.md','review/remediation-sixth-20261014-prepare/contracts','review/remediation-sixth-20261014-prepare/prompts','review/remediation-sixth-20261014-prepare/inputs')==b''
formal=[]
for x in c['candidate_formal_paths']:
 b=git('cat-file','blob',c['frozen_main']+':'+x);row=next(t for t in inputs['formal_materials'] if t['path']==x)
 assert all(ident(b)[k]==row[k] for k in ident(b))
 assert (repo/x).read_bytes()==b
 new=(p/'candidates/R6-U02/mirror'/x).read_bytes();assert new!=b and new.endswith(b'\n')
 assert b'```ruby' not in new and b'Data/Scripts/' not in new and b'reference/pokemon-essentials/' not in new
 formal.append({'formal_path':x,'baseline':ident(b),'candidate':ident(new),'mode':'100644','git_type':'blob'})
 # Existing link destinations are resolved against their formal-equivalent location.
 for link in re.findall(r'\]\(([^)]+)\)',new.decode()):
  if not re.match(r'^[a-zA-Z]+:|^#',link):assert (repo/x).parent.joinpath(link.split('#')[0]).exists(),(x,link)
source=[]
for x in c['read_only_reference_paths']+[r['path'] for r in json.loads((e/'supplemental-inputs.json').read_text())]:
 row=next(t for t in inputs['source_materials'] if t['path']==x)
 b=(Path('/tmp/r6-u02-inputs/Maruno17/pokemon-essentials')/c['frozen_reference']/x).read_bytes()
 assert all(ident(b)[k]==row[k] for k in ident(b));source.append({'path':x,'commit':c['frozen_reference'],'tree':inputs['reference_tree'],**row})
(e/'source-identities.json').write_text(json.dumps(source,ensure_ascii=False,indent=2)+'\n')
# Count AI IDs only within its own family, keeping all original table rows.
ai_path=c['candidate_formal_paths'][4];hi_path=c['candidate_formal_paths'][5]
a=(p/'candidates/R6-U02/mirror'/ai_path).read_text();family=a.split('## AI：',1)[1].split('## AE：',1)[0]
ids=re.findall(r'^\| ([A-Z]\d\d) \|',family,re.M);assert len(ids)==37 and len(set(ids))==37
h=(p/'candidates/R6-U02/mirror'/hi_path).read_text();hi_ids=re.findall(r'^\| (HI10[a-f]) \|',h,re.M);assert len(hi_ids)==6 and len(set(hi_ids))==6
for path,exception in [(ai_path,set()),(hi_path,{'HI10'})]:
 b=git('cat-file','blob',c['frozen_main']+':'+path).decode();new=(p/'candidates/R6-U02/mirror'/path).read_text()
 for line in b.splitlines():
  if re.match(r'^\| [A-Za-z][A-Za-z0-9-]* \|',line) and line.split('|')[1].strip() not in exception:assert line in new,(path,line)
# Compare every R5 exact span in these paths, remapping by unchanged line blocks.
hist=json.loads((e/'historical-r5-qualified-projection.json').read_text());spans=[]
for r in hist:
 for s in r['formal_consumers']:
  b=git('cat-file','blob',c['frozen_main']+':'+s['path']).decode().splitlines(keepends=True)
  n=(p/'candidates/R6-U02/mirror'/s['path']).read_text().splitlines(keepends=True)
  lo,hi=s['lines'];raw=''.join(b[lo-1:hi]).encode();assert hashlib.sha256(raw).hexdigest()==s['span_sha256'],(r['id'],s)
  mapping={i:k+(i-j) for j,k,size in difflib.SequenceMatcher(a=b,b=n,autojunk=False).get_matching_blocks() for i in range(j,j+size)}
  assert all(i in mapping for i in range(lo-1,hi)),(r['id'],s)
  ns=[mapping[i] for i in range(lo-1,hi)];assert ns==list(range(ns[0],ns[-1]+1))
  newraw=''.join(n[ns[0]:ns[-1]+1]).encode();assert newraw==raw
  spans.append({'id':r['id'],'candidate_clause':r['candidate_clause'],'activation_lines':r['activation_lines'],**s,'candidate_lines':[ns[0]+1,ns[-1]+1],'result':'EXACT_UNCHANGED_BYTES','scope':'qualification/span preservation only, not new runtime or whole-ID PASS'})
(e/'historical-span-validation.json').write_text(json.dumps(spans,ensure_ascii=False,indent=2)+'\n')
(e/'candidate-mirror-manifest.json').write_text(json.dumps(formal,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':'PASS_STATIC_TEXT_IDENTITY_AND_PRESERVATION','formal_mirrors':len(formal),'source_payload_identities':len(source),'R5_precise_spans':len(spans),'AI_rows':len(ids),'new_AI_rows':7,'new_HI_rows':6,'old_catalog_rows_preserved_except_HI10_minimal_clarification':True,'formal_public_inputs_unchanged':True,'source_behavior_execution':0,'independent_model_execution':0,'host_demo_execution':0,'not_independent_candidate_pass':True},ensure_ascii=False,indent=2))
