import subprocess,json,hashlib,re,datetime,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent;C='86bbc99b28d93db4ed9d6897daf5f3725ccd1808';U='9971fe84896786645cdcda3ab45e5caf7785cabc';D='e93d0e56750a6a16cc50cc68b2c97f11ea255153';R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';FORM='deliverables/final-specification-set/';PREFIX='review/remediation-sixth-20261014-prepare/candidates/'
def read(c,p):return subprocess.check_output(['git','show',c+':'+p])
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
x=json.loads(read(C,'review/remediation-sixth-20261014-prepare/integration/U01-U14-final-composite-20261014/actual-review-input.json'));bindings=[]
for row in json.loads((BASE/'actualfiles-projection.json').read_text())['files']:
 b=read(C,row['path']);assert ident(b)==row['actual'];entry=subprocess.check_output(['git','ls-tree',C,'--',row['path']]).decode().strip();assert entry==f"100644 blob {row['actual']['git_blob']}\t{row['path']}";bindings.append({'path':row['path'],'actual':ident(b),'mode_type_identity_equal':True})
paths=['combat-requirements/wp56-palace-and-arena-variants.md','combat-requirements/wp58-battle-recording-and-playback.md','pokemon-rules/wp53-safari-and-bug-catching-contest.md','test-catalog/combat-requirements-wp54-55-56-58.md'];assert all(read(C,FORM+p)==read(U,PREFIX+'R6-U13/mirror/'+FORM+p) for p in paths)
test='test-catalog/pokemon-rules-wp53-60-61-62-69-70.md';a=read(C,FORM+test);u=read(U,PREFIX+'R6-U13/mirror/'+FORM+test);d=read(D,PREFIX+'R6-U11/mirror/'+FORM+test);mark='## BP：'.encode();ap,asuf=a.split(mark,1);up,us=u.split(mark,1);dp,ds=d.split(mark,1);assert ap==up and asuf==ds
rawcounts={};ct=read(C,FORM+paths[3]).decode();pt=a.decode()
for name,body,pattern,expected in [('QC',ct.split('## QC：',1)[1].split('## WS：',1)[0],r'^\| (Q\d+) \|',49),('WS',ct.split('## WS：',1)[1].split('## PA：',1)[0],r'^\| (W\d+) \|',36),('PA',ct.split('## PA：',1)[1].split('## RC：',1)[0],r'^\| (P\d+) \|',32),('RC',ct.split('## RC：',1)[1],r'^\| (W\d+b?) \|',29),('SF',pt.split('## SF：',1)[1].split('## BP：',1)[0],r'^\| (SF\d+) \|',40)]:
 ids=re.findall(pattern,body,re.M);assert len(ids)==expected and len(set(ids))==expected;rawcounts[name]={'raw':len(ids),'unique':len(set(ids)),'ids':ids}
assert 'W22b' in rawcounts['RC']['ids']
led=[json.loads(l) for l in (BASE/'reading-ledger.jsonl').read_text().splitlines()];coverage=[]
for p in paths+[test]:
 loc=C+':'+FORM+p;lines=read(C,FORM+p).decode().splitlines();rr=[r['range'] for r in led if r.get('locator')==loc and 'range' in r];covered=set(n for lo,hi in rr for n in range(lo,hi+1));assert covered==set(range(1,len(lines)+1));coverage.append({'path':FORM+p,'lines':len(lines),'new_presented_ranges':rr,'complete_new_fulltext':True,**ident(read(C,FORM+p))})
old_review='3ef4854ef43eac92fd1dc57350e4cf6aa160082b';oldledger='review/remediation-sixth-20261014-prepare/reviews/R6-U13-R/recording-save/reading-ledger.jsonl';old=[json.loads(l) for l in read(old_review,oldledger).decode().splitlines()];by={}
for rec in old:
 loc=rec.get('locator','')
 if loc.startswith(R+':Data/Scripts/'):
  k=loc.split(':',1)[1];by.setdefault(k,[]).append(rec)
sources=[]
for k,recs in by.items():
 b=read(R,k);actual=ident(b);assert all(all(rec[z]==actual[z] for z in actual) for rec in recs);sources.append({'fixed_ref':R,'path':k,**actual,'old_review':old_review,'old_presented_ranges':[rec.get('presented_range',rec.get('range')) for rec in recs],'new_full_semantic_read':False,'qualification':'Exact immutable old actual-reading ranges reused, not old verdict transferred'})
assert subprocess.check_output(['git','rev-parse',C+'^{tree}']).decode().strip()=='67e8c55d520fa8cad2928cb4b95e24c3ed602d5a';assert subprocess.check_output(['git','rev-parse',C+':deliverables/final-specification-set']).decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c';assert subprocess.check_output(['git','rev-parse',R+'^{tree}']).decode().strip()==x['fixed_reference_tree']
res={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'argv':sys.argv,'cwd':str(Path.cwd()),'actual_commit':C,'workspace_tree':'67e8c55d520fa8cad2928cb4b95e24c3ed602d5a','formal_tree':'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c','formal_identities':bindings,'fulltext_coverage':coverage,'four_actual_files_equal_U13_candidate':paths,'pokemon_composition':{'SF_full_prefix_exact_U13_repair':True,'nonSF_full_suffix_exact_U11':True,'whole_actual_bytes':ident(a)},'raw_before_index_counts':rawcounts,'same_source_qualification_bindings':sources,'contract':'contract-qualification-binding.json','semantic_verdict_from_tool':False,'reference_author_serializer_model_realIO_execution':False}
(BASE/'identity-and-coverage-checks.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'status':'FINITE_DOCUMENT_CHECK_PASS','complete_actual_files':len(coverage),'related_formal_identities':len(bindings),'old_source_identity_bindings':len(sources),'raw_unique':{k:[v['raw'],v['unique']] for k,v in rawcounts.items()},'candidate_write':False,'reference_execution':False}))
