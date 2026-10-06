"""Own static source range/hash bookkeeping; reviewed source is never executed."""
import sys, pathlib, subprocess, json, hashlib
OUT=pathlib.Path(__file__).parent
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
mode,repo,path=sys.argv[1:4]
b=subprocess.check_output(['git','-C',repo,'show',REF+':'+path])
lines=b.decode().splitlines(keepends=True)
identity={'repository':'reference/pokemon-essentials','commit':REF,'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'lines':len(lines)}
if mode=='read':
 a,z=map(int,sys.argv[4:6]);assert 1<=a<=z<=len(lines)
 print(json.dumps(identity));print('RANGE',a,z)
 for n in range(a,z+1):print(str(n)+': '+lines[n-1],end='')
 (OUT/'completion-source-last-display.json').write_text(json.dumps({'identity':identity,'range':[a,z],'not_yet_acknowledged':True})+'\n')
elif mode=='ack':
 a,z=map(int,sys.argv[4:6]);last=json.loads((OUT/'completion-source-last-display.json').read_text());assert last['identity']==identity and last['range']==[a,z]
 p=OUT/'completion-source-reading.json';o=json.loads(p.read_text()) if p.exists() else {'static_only':True,'runtime_observations':0,'behavior_vectors_executed':0,'reads':[]}
 o['reads'].append({'identity':identity,'range':[a,z],'range_sha256':hashlib.sha256(''.join(lines[a-1:z]).encode()).hexdigest(),'consumed_after_complete_display':True});p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n');print('ACK',path,a,z)
elif mode=='search':
 import re
 pat=re.compile(sys.argv[4]);print(json.dumps(identity))
 for n,s in enumerate(lines,1):
  if pat.search(s):print(str(n)+': '+s,end='')
