"""Read-only pinned resource recovery; outputs only in this previously new task dir."""
from pathlib import Path
import collections, datetime, hashlib, json, re, shutil, subprocess, sys
O=Path(__file__).resolve().parent
P=O.parent/'preflight_resources'
R=Path('/workspace/pokemon-essentials')
B=Path('/workspace/pokemon-essentials-clean-room')
C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BC='fd1df570cad987dc3852a3b958f03916e317f7fe'
sha=lambda b:hashlib.sha256(b).hexdigest()
utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def git(root,*a):return subprocess.run(['git','-C',str(root),*a],check=True,capture_output=True).stdout
def ident(root,c,p):
 b=(root/p).read_bytes();g=git(root,'show',c+':'+p);assert b==g,p
 return dict(repo=str(root),commit=c,path=p,bytes=len(b),sha256=sha(b),blob=git(root,'rev-parse',c+':'+p).decode().strip(),mode=git(root,'ls-tree',c,'--',p).decode().split()[0])
idx=json.loads((P/'handoff/readset-index.json').read_text())
ids=[]
for x in idx['strings']:
 p=P/x['inventory'];b=p.read_bytes();assert len(b)==x['inventory_bytes'] and sha(b)==x['inventory_sha256'];ids.append(dict(path=str(p),bytes=len(b),sha256=sha(b),purpose='finite candidate inventory; no semantic inheritance'))
 ids.append(ident(R,C,x['path']))
for x in idx['historical_navigation']+[idx['current_decoder_identity'],idx['controller_readset_identity']]:
 p=P/x['path'];b=p.read_bytes();assert len(b)==x['bytes'] and sha(b)==x['sha256'];ids.append(dict(path=str(p),bytes=len(b),sha256=sha(b),purpose=x.get('qualification','readset/decoder, independently checked')))
for root,c,p in [(R,C,'mkxp.json'),(R,C,'Data/Scripts/001_Technical/004_Input.rb'),(R,C,'Data/Scripts/016_UI/001_Non-interactive UI/002_UI_Controls.rb'),(B,BC,'deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md'),(B,BC,'deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md')]:ids.append(ident(root,c,p))
write(O/'identities.json',dict(created_utc=utc(),identities=ids,B8=BC,B8_tree=git(B,'rev-parse',BC+'^{tree}').decode().strip(),formal_tree=git(B,'rev-parse',BC+':deliverables/final-specification-set').decode().strip(),R=C,R_tree=git(R,'rev-parse',C+'^{tree}').decode().strip(),report_HEAD=git(B,'rev-parse','HEAD').decode().strip()))
# Preserve reviewed source tool exactly; a minimal adapter supplies only Reader/helpers.
T=O/'tools';T.mkdir(exist_ok=False)
src=P/'recovered-resource-evidence/temporary/binary-tools/audit_binaries.py'
shutil.copyfile(src,T/'audit_binaries.py')
(T/'audit_resources.py').write_text('''from pathlib import Path
import hashlib,json,struct
ROOT=Path('/workspace/pokemon-essentials')
OUT=Path(__file__).resolve().parent
PIN={'R_commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'}
def sha(b):return hashlib.sha256(b).hexdigest()
def save(n,v):
 assert Path(n).name==n
 (OUT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\\n')
def require(x,m):
 if not x:raise ValueError(m)
class Reader:
 def __init__(self,b):self.b=b
 def span(self,s,n):
  require(0<=s<=len(self.b) and 0<=n<=len(self.b)-s,'out of bounds')
  return self.b[s:s+n]
 def unpack(self,f,p):return struct.unpack(f,self.span(p,struct.calcsize(f)))
''')
sys.path.insert(0,str(T))
from audit_binaries import PE,CLI
pe_rows=[];stats={}
for x in idx['strings']:
 name=x['path'];data=(R/name).read_bytes();pe=PE(data)
 row=dict(path=name,bytes=len(data),sha256=sha(data),meta=pe.meta,imports=pe.imports(),exports=pe.exports(),resources=pe.resources(),debug=pe.debug(),coff_symbols=pe.coff_symbols(),coff_symbol_offset=pe.symoff,coff_symbol_count=pe.nsym,coff_string_base=pe.strbase,coff_string_size=pe.strsize)
 if pe.dirs[14][0]:row['CLI']=CLI(pe).ledger()
 pe_rows.append(row)
 cs=collections.Counter()
 out=O/(name+'.section-candidates.jsonl')
 with out.open('x') as f:
  for i,line in enumerate((P/x['inventory']).open(),1):
   r=json.loads(line);a,z=r['start'],r['end_exclusive'];assert sha(data[a:z])==r['sha256'];enc='ascii' if r['encoding']=='ascii' else 'utf-16-le';assert data[a:z].decode(enc)==r['text']
   ss=[s['name'] for s in pe.sections if s['size'] and s['offset']<=a and z<=s['offset']+s['size']]
   sec=ss[0] if len(ss)==1 else 'headers_or_overlay_or_cross_section'
   if pe.symoff and pe.symoff<=a and z<=pe.strbase+pe.strsize:sec='COFF_symbol_or_string_table'
   r.update(candidate_id=name+':'+str(i),inventory_line=i,section=sec,semantic_status='UNREAD',type_disposition='PENDING')
   f.write(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n');cs[sec]+=1
 stats[name]=dict(cs)
write(O/'pe-metadata.json',dict(utc=utc(),files=pe_rows,qualification='STRUCTURE_PARSED; no execution or inherited semantic review'))
write(O/'section-summary.json',stats)
ctrl=json.loads((P/'handoff/controller-readset.json').read_text())
raw=(R/'Game.exe').read_bytes()[ctrl['offset']:ctrl['end_exclusive']]
assert sha(raw)==ctrl['region_sha256'] and raw==(P/'current-controller/raw.txt').read_bytes()
(O/'controller-raw.txt').write_bytes(raw)
write(O/'progress.json',dict(status='RUNNING',owner='/root/binary_controller_strings_review',updated_utc=utc(),requested_configuration=idx['requested_configuration'],actual_configuration=idx['actual_configuration'],platform_task_id='/root/binary_controller_strings_review (logical canonical task name; platform UUID UNVERIFIED)',baseline=dict(B8=BC,R=C),scope='1666 controller records; complete finite 260161 string candidate type disposition and readable current semantic units/consumers; independent acceptance not inherited',execution=dict(reference=0,independent_model=0,host=0,behavior_vectors='NOT_EXECUTED'),update_started=False,outputs=['identities.json','pe-metadata.json','section-summary.json'],unread='All semantic units initially UNREAD; structure parsing is distinct'))
print(json.dumps(dict(identities=len(ids),sections=stats,controller_lines=len(ctrl['rows']),controller_records=ctrl['record_count'],patterns=ctrl['pattern_count']),ensure_ascii=False))
