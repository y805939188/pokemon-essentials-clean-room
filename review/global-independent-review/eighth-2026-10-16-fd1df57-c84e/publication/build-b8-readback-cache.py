from pathlib import Path
import subprocess,json,hashlib,datetime
repo=Path('/workspace/pokemon-essentials-clean-room'); rr=repo/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'; dest=Path('/workspace/scratch/r8-readback-b8-only-cache.git'); b8='fd1df570cad987dc3852a3b958f03916e317f7fe';target='8362441bff0d6da1b11a8894c784dc08f61e67f0';events=[]
assert not dest.exists(),'fresh B8-only cache required'
def run(args,stdin=None):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.run(args,input=stdin,stdout=subprocess.PIPE,stderr=subprocess.PIPE);end=datetime.datetime.now(datetime.timezone.utc).isoformat();events.append({'command':args,'start_utc':start,'end_utc':end,'exit_code':p.returncode,'stdout':p.stdout.decode('utf-8','replace'),'stderr':p.stderr.decode('utf-8','replace')});assert p.returncode==0,events[-1];return p.stdout
run(['git','init','--bare',str(dest)])
pack_hash=run(['git','-C',str(repo),'pack-objects','--revs',str(dest/'objects/pack/b8-input')],(b8+'\n').encode()).decode().strip()
expected=set(subprocess.check_output(['git','-C',str(repo),'rev-list','--objects','--no-object-names',b8]).decode().splitlines())
idx=dest/'objects/pack'/('b8-input-'+pack_hash+'.idx');packed=subprocess.check_output(['git','show-index'],input=idx.read_bytes()).decode();actual={x.split()[1] for x in packed.splitlines()};assert actual==expected,(len(actual),len(expected))
check=subprocess.run(['git','-C',str(dest),'cat-file','-e',target],stdout=subprocess.PIPE,stderr=subprocess.PIPE);assert check.returncode!=0,'report target must remain absent'
assert subprocess.check_output(['git','-C',str(dest),'rev-parse',b8+'^{tree}']).decode().strip()=='751dfde81048c81390f89a65ca1d1a565ba8e1ca'
files=[{'name':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted((dest/'objects/pack').iterdir())]
proof={'schema':'gr8-fixed-b8-only-readback-cache/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cache':str(dest),'allowed_commit_closure':b8,'allowed_tree':'751dfde81048c81390f89a65ca1d1a565ba8e1ca','source_checkout':str(repo),'closure_object_count':len(expected),'expected_sorted_object_ids_sha256':hashlib.sha256(('\n'.join(sorted(expected))+'\n').encode()).hexdigest(),'actual_pack_object_ids_equal_exact_B8_closure':True,'pack_files':files,'report_target_absence_check':{'commit':target,'exit_code':check.returncode,'stdout':check.stdout.decode('utf-8','replace'),'stderr':check.stderr.decode('utf-8','replace')},'events':events,'semantic_credit':'NONE; safe transport cache only','update_started':False}
raw=(json.dumps(proof,ensure_ascii=False,indent=2)+'\n').encode();(dest/'cache-input-scope.json').write_bytes(raw);(rr/'publication/b8-only-readback-cache.json').write_bytes(raw);print(json.dumps({'cache':str(dest),'objects':len(expected),'pack_files':files,'target_absent':True},ensure_ascii=False))
