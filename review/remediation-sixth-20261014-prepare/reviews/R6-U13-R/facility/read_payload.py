import sys,subprocess,pathlib,json,hashlib,datetime,platform
base=pathlib.Path('/workspace/pokemon-essentials-clean-room')
owned=base/'review/remediation-sixth-20261014-prepare/reviews/R6-U13-R/facility'
p=pathlib.Path(sys.argv[1]); lo=int(sys.argv[2]) if len(sys.argv)>2 else 1; hi=int(sys.argv[3]) if len(sys.argv)>3 else None
repo=sys.argv[4] if len(sys.argv)>4 else str(base); commit=sys.argv[5] if len(sys.argv)>5 else None
if commit:
 raw=subprocess.check_output(['git','-C',repo,'show',commit+':'+str(p)])
 entry=subprocess.check_output(['git','-C',repo,'ls-tree',commit,'--',str(p)],text=True).strip()
 actual_commit=subprocess.check_output(['git','-C',repo,'rev-parse',commit],text=True).strip(); tree=subprocess.check_output(['git','-C',repo,'rev-parse',commit+'^{tree}'],text=True).strip()
else:
 raw=p.read_bytes(); rp=p.resolve().relative_to(base); entry=subprocess.check_output(['git','-C',repo,'ls-tree','HEAD','--',str(rp)],text=True).strip(); actual_commit=subprocess.check_output(['git','-C',repo,'rev-parse','HEAD'],text=True).strip(); tree=subprocess.check_output(['git','-C',repo,'rev-parse','HEAD^{tree}'],text=True).strip()
lines=raw.decode('utf-8').splitlines(); hi=len(lines) if hi is None else min(hi,len(lines)); blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
rec={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cwd':str(pathlib.Path.cwd()),'argv':sys.argv,'platform':platform.platform(),'repo':repo,'commit':actual_commit,'tree':tree,'path':str(p),'tree_entry':entry,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'git_blob':blob,'line_count':len(lines),'range':[lo,hi],'full_payload':lo==1 and hi==len(lines),'exit':0,'reading_kind':'semantic_range'}
with (owned/'reading-ledger.jsonl').open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(json.dumps(rec,ensure_ascii=False))
for i in range(lo-1,hi):print(str(i+1)+':'+lines[i])
