"""Review-owned finite byte/scope validation. Never runs reference behavior."""
import datetime,difflib,hashlib,json,subprocess,sys,re
from pathlib import Path
OWN=Path(__file__).resolve().parent
C='caa090d8e396c08b09fb2d4d5067aa00f4d6c3cb';P='469a268b92daed7b4d28d7fd0da75520cbb7228f';M='8ea169fbd0f33f378b5d732fd6bea59e854e04a6';R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PRE='review/remediation-sixth-20261014-prepare/';CAN=PRE+'candidates/R6-U12/';start=datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*a):return subprocess.check_output(['git',*a])
def ident(data):return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}
def obj(c,p):
 d=git('show',c+':'+p);mode,typ,blob=git('ls-tree',c,'--',p).decode().split()[:3];v=ident(d);assert blob==v['git_blob'];return d,dict(v,mode=mode,type=typ,commit=c,path=p)
assert git('rev-parse',C+'^{tree}').decode().strip()=='8f29be65173bb29d160aed74dbb6f7378fa81c2a'
prompt,pi=obj(P,PRE+'prompts/R6-U12-R.md');assert (pi['bytes'],pi['sha256'],pi['git_blob'])==(176641,'b16a99900db351052939f6b4a4237fed902ae31cb2945810c044692404e59726','f44d37e07997922a6a63866929e6d8a6dd9af20c')
contract,ci=obj(P,PRE+'contracts/R6-U12.json');assert contract in prompt;assert contract==git('show',C+':'+ci['path']);co=json.loads(contract)
frozen=json.loads(git('show',P+':'+PRE+'inputs/frozen-inputs.json'))
mirrors=[];maps=[];diff=[]
for path in co['candidate_formal_paths']:
 old,oi=obj(M,path);new,ni=obj(C,CAN+'mirror/'+path);assert git('show',P+':'+CAN+'mirror/'+path)==old;assert Path(path).read_bytes()==old
 oldlines=old.splitlines(keepends=True);newlines=new.splitlines(keepends=True)
 ops=difflib.SequenceMatcher(a=oldlines,b=newlines,autojunk=False).get_opcodes()
 maps.append({'formal_path':path,'baseline':oi,'candidate':ni,'semantic_read_join':'Complete candidate ranges personally read; exact equal ranges map to full baseline; all replaced old lines personally read in full diff. Not hash-only semantic credit.','ranges':[{'kind':k,'baseline_half_open_0':[a,b],'candidate_half_open_0':[x,y]} for k,a,b,x,y in ops]})
 mirrors.append({'formal_path':path,'baseline':oi,'candidate':ni})
 diff.extend(difflib.unified_diff(old.decode().splitlines(True),new.decode().splitlines(True),fromfile=M+':'+path,tofile=C+':'+CAN+'mirror/'+path,n=3))
 cat=path if '/test-catalog/' in path else locals().get('cat')
oldcat=git('show',M+':'+cat).splitlines(True);newcat=git('show',C+':'+CAN+'mirror/'+cat).splitlines(True)
assert len(oldcat)==914 and len(newcat)==931
assert all(a==b for i,(a,b) in enumerate(zip(oldcat,newcat),1) if i not in [303,327])
rows=[x for x in oldcat if x.startswith(b'| ') and not x.startswith((b'| C12 |',b'| C36 |'))];assert len(rows)==721
vectors=[x for x in newcat if x.startswith(b'| R6-U12-')];assert len(vectors)==9;assert len({x.split(b'|')[1] for x in vectors})==9
reads=[json.loads(x) for x in OWN.joinpath('read-segments.jsonl').read_text().splitlines()]
sources=[]
for path in sorted({x['path'] for x in reads if x['commit']==R}):
 data,actual=obj(R,path);expected=next(x for x in frozen['source_materials'] if x['path']==path)
 for key in ['bytes','sha256','git_blob','mode']:assert actual[key]==expected[key],(path,key)
 sources.append(dict(actual,read_ranges=[x['range'] for x in reads if x['commit']==R and x['path']==path]))
changes=git('diff','--name-status',P,C).decode().splitlines();assert len(changes)==41;assert all(x.split('\t')[-1].startswith(CAN) for x in changes)
assert sum(x.startswith('M\t') for x in changes)==4 and sum(x.startswith('A\t') for x in changes)==37
assert git('rev-parse',M+':deliverables/final-specification-set')==git('rev-parse',C+':deliverables/final-specification-set')
current=git('diff','--name-only',C).decode().splitlines()+git('ls-files','--others','--exclude-standard').decode().splitlines();assert all(x.startswith(str(OWN.relative_to(Path.cwd()))+'/') for x in current)
assert subprocess.run(['git','diff','--check'],capture_output=True).returncode==0
OWN.joinpath('candidate.diff').write_text(''.join(diff));OWN.joinpath('baseline-fulltext-join.json').write_text(json.dumps(maps,ensure_ascii=False,indent=2)+'\n')
result={'kind':'TOOL_VALIDATION_ONLY','cwd':str(Path.cwd()),'argv':sys.argv,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'prompt':pi,'contract':ci,'source_tree':git('rev-parse',R+'^{tree}').decode().strip(),'source_identities':sources,'candidate_mirrors':mirrors,'candidate_commit':C,'candidate_tree':'8f29be65173bb29d160aed74dbb6f7378fa81c2a','candidate_directory_tree':git('rev-parse',C+':'+CAN.rstrip('/')).decode().strip(),'mirror_tree':git('rev-parse',C+':'+CAN+'mirror').decode().strip(),'claims_checked':{'four_modified_mirrors':4,'candidate_payloads':41,'candidate_added_files':37,'candidate_modified_files':4,'preserved_old_table_lines':721,'new_vector_rows':9,'old_catalog_except_C12_C36_exact_ordered_bytes':True,'all9_vectors_design_only':True,'formal_tree_unchanged':True,'candidate_outside_allowlist_changes':0,'reviewer_outside_allowlist_changes':0},'reference_execution':0,'host_execution':0,'semantics':'Identity/preservation/allowlist checks do not themselves give behavioral PASS.'}
OWN.joinpath('tool-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result['claims_checked'],ensure_ascii=False))
