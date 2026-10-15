"""R7-U10 byte/line audit. Never executes reference or restored programs."""
from pathlib import Path
from collections import Counter
import datetime,hashlib,json,os,subprocess,urllib.request,concurrent.futures
ROOT=Path('/workspace/r7-ir-R7-U10-wave3')
REPO=ROOT/'result-checkout'
OUT=REPO/'review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U10/r1/evidence'
MI='e54f54a2cb32e546eabd46aaf53ed45b30a8af89';B='e646432c644dec04d306842cc5a559a29c718fbc'
def identity(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest())
def git(*args):return subprocess.check_output(['git','-C',str(REPO),*args],stderr=subprocess.PIPE)
def readgit(commit,path):
 try:return git('show',commit+':'+path)
 except subprocess.CalledProcessError:
  if commit==B and path=='review/remediation-seventh-20261015-prepare/current-navigation-errata.json':return b''
  raise
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
res={'start_utc':start,'pid':os.getpid(),'tool_type':'TOOL_VALIDATION_ONLY','reference_programs_executed':0,'restored_identity_files':[],'errors':[]}
for name in ['original','actual-input']:
 plan=json.loads((ROOT/('original-plans' if name=='original' else 'actual-plans')/'R7-U10.json').read_text())
 for kind in ['artifacts','evidence','fixed_read_inputs']:
  for row in plan[kind]:
   data=(ROOT/name/row['local_path']).read_bytes();actual=identity(data)
   matches=all(actual[k]==row.get('git_blob_content_id' if k=='git_blob' else k,actual[k]) for k in actual)
   if not matches:res['errors'].append(['restore',name,row['local_path']])
   res['restored_identity_files'].append({'snapshot':name,'path':row['local_path'],**actual,'matches_plan':matches,'commit':row['commit'],'source_path':row['path']})
fi=json.loads((ROOT/'bootstrap/integrated-input.json').read_text())
res['git_objects']={sha:git('rev-parse',sha+'^{tree}').decode().strip() for sha in [MI,B,'b98fa82f8a08b5630ac568cbe8c34f607f623cfb','72c93538d6e6cc15cb0be15ccfc3b8268d4b0af7']}
res['formal_trees']={sha:git('rev-parse',sha+':deliverables/final-specification-set').decode().strip() for sha in [MI,B]}
formal=[]
for row in fi['all_formal_file_identities']:
 a=readgit(MI,row['path']);base=readgit(B,row['path']);ai=identity(a);bi=identity(base)
 ok=all(ai[k]==row[k] for k in ai) and all(bi[k]==row['base_B_identity'][k] for k in bi)
 ok=ok and (a!=base)==row['changed_against_B']
 formal.append({'path':row['path'],'actual':ai,'base':bi,'changed':a!=base,'matches_FI':ok})
 if not ok:res['errors'].append(['formal',row['path']])
res['formal_files']=formal;res['formal_counts']={'all':len(formal),'changed':sum(x['changed'] for x in formal),'unchanged':sum(not x['changed'] for x in formal)}
j=json.loads((ROOT/'actual-input/integration/applied-clauses.json').read_text())
plan=json.loads((ROOT/'actual-plans/R7-U10.json').read_text())
lookup={(x['commit'],x['path']):(ROOT/'actual-input'/x['local_path']) for x in plan['artifacts']}
cache={}
def candidate(key):
 if key in lookup:return lookup[key].read_bytes()
 p=ROOT/'supplement/candidate-mirrors'/key[0]/key[1];p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():return p.read_bytes()
 url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+key[0]+'/'+key[1]
 data=urllib.request.urlopen(url,timeout=40).read();p.write_bytes(data);return data
keys=set((h['candidate_commit'],h['candidate_path']) for f in j['cumulative_files'] for h in f['hunks'])
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for key,data in zip(sorted(keys),pool.map(candidate,sorted(keys))):cache[key]=data
res['candidate_mirrors']=[{'commit':k[0],'path':k[1],**identity(v)} for k,v in sorted(cache.items())]
res['journal_files']=[];res['journal_hunks']=[]
for f in j['cumulative_files']:
 path=f['path'];base=readgit(B,path);bl=base.decode().splitlines(keepends=True)
 actual=readgit(MI,path);al=actual.decode().splitlines(keepends=True)
 hs=sorted(f['hunks'],key=lambda h:(h['base_line_indices_half_open'][0],h.get('integration_wave_rank',0),h['batch_order']))
 built=[];pos=0
 for idx,h in enumerate(hs):
  lo,hi=h['base_line_indices_half_open'];clo,chi=h['candidate_line_indices_half_open'];alo,ahi=h['actual_final_line_indices_half_open']
  removed=''.join(bl[lo:hi]);cand=cache[(h['candidate_commit'],h['candidate_path'])];added=''.join(cand.decode().splitlines(keepends=True)[clo:chi])
  checks={'removed_text':removed==h['removed_text'],'added_text':added==h['added_text'],'removed_identity':identity(removed.encode())==h['removed_identity'],'added_identity':identity(added.encode())==h['added_identity'],'actual_clause_at_declared_lines':''.join(al[alo:ahi])==h['added_text'],'nonoverlap':lo>=pos}
  res['journal_hunks'].append({'path':path,'batch_id':h['batch_id'],'required_ids':h['required_ids'],'base_lines_half_open':h['base_line_indices_half_open'],'actual_lines_half_open':h['actual_final_line_indices_half_open'],'candidate_commit':h['candidate_commit'],'candidate_path':h['candidate_path'],'added_identity':identity(added.encode()),'checks':checks})
  if not all(checks.values()):res['errors'].append(['hunk',path,h['batch_id'],checks])
  built+=bl[pos:lo];built.append(h['added_text']);pos=hi
 built+=bl[pos:];assembled=''.join(built).encode()
 admin=[a for a in j['root_administrative_adjustments'] if a['path']==path]
 if admin:assembled+=admin[0]['added_text'].encode()
 ok=assembled==actual
 res['journal_files'].append({'path':path,'hunks':len(hs),'contributors':f['contributors'],'assembled':identity(assembled),'actual':identity(actual),'full_replay_matches':ok})
 if not ok:res['errors'].append(['assembled',path])
res['journal_hunk_counts']=dict(Counter(x['batch_id'] for x in res['journal_hunks']))
res['prior_accepted_files']=[]
for path in j['prior_accepted_paths_preserved_exact']:
 a=readgit(MI,path);p=(ROOT/'actual-input/prior-accepted/previous-actual'/path).read_bytes();ok=a==p
 res['prior_accepted_files'].append({'path':path,**identity(a),'unchanged_from_prior_MI':ok})
 if not ok:res['errors'].append(['prior',path])
res['shared_order']=j['same_boundary_insertions']
res['qualification']='Byte and line replay only; not semantic review, execution, independence, acceptance or closure.'
res['end_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(OUT/'byte-audit.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:res[k] for k in ['pid','formal_counts','journal_hunk_counts','errors']},ensure_ascii=False))
