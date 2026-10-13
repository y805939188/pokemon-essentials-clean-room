"""Static evidence addresses. Selection/matching never establishes semantic review."""
from reg_io import *
from functools import lru_cache
import hashlib,re,difflib

def digest(x):return hashlib.sha256(x if isinstance(x,bytes) else json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def pointer_get(o,p):
 for k in p.strip('/').split('/') if p.strip('/') else []:o=o[int(k)] if isinstance(o,list) else o[k.replace('~1','/').replace('~0','~')]
 return o
@lru_cache(None)
def history_obj(c,p):return jfixed(p,c)
@lru_cache(None)
def lines(p,c=B):return fixed(p,c).splitlines()
def pairs(x):
 if isinstance(x,int):return [[x,x]]
 if isinstance(x,(tuple,list)):
  if len(x)==2 and all(isinstance(v,int) for v in x):return [list(x)]
  if all(isinstance(v,int) for v in x):return [[v,v] for v in x]
  return [a for v in x for a in pairs(v)]
 if isinstance(x,str):return [[int(m[0]),int(m[1] or m[0])] for m in re.findall(r'(?<!\d)(\d+)(?:[–—-](\d+))?(?!\d)',x)]
 return []
def section_ranges(p):
 ls=lines(p);heads=[]
 for n,s in enumerate(ls,1):
  if re.match(r'^#{1,6} ',s):
   title=s.lstrip('#').strip();m=re.match(r'(\d+(?:\.\d+)*[a-z]?)(?:[.、\s]|$)',title)
   heads.append({'number':m.group(1) if m else None,'line':n,'heading':title,'depth':len(s)-len(s.lstrip('#'))})
 for i,h in enumerate(heads):
  end=next((x['line']-1 for x in heads[i+1:] if x['depth']<=h['depth']),len(ls));h['lines']=[h['line'],end]
 return heads

def walk(o,p='',path=None):
 if isinstance(o,dict):
  path=o.get('path',path)
  yield p,o,path
  for k,v in o.items():yield from walk(v,p+'/'+str(k).replace('~','~0').replace('/','~1'),path)
 elif isinstance(o,list):
  for i,v in enumerate(o):yield from walk(v,p+'/'+str(i),path)

def matching_sections(p,text):
 nums=set(re.findall(r'§\s*(\d+(?:\.\d+)*[a-z]?)',text))
 for m in re.finditer(r'§?\s*(\d+)\.(\d+)\s*[–—-]\s*(\d+)\.(\d+)',text):
  a,b,c,d=map(int,m.groups())
  if a==c and b<=d and d-b<20:nums.update(f'{a}.{i}' for i in range(b,d+1))
 return [h for h in section_ranges(p) if h['number'] in nums]

def remap(p,c,ranges):
 old=lines(p,c);now=lines(p);mp={}
 for a,b,n in difflib.SequenceMatcher(None,old,now,autojunk=False).get_matching_blocks():
  mp.update({a+j+1:b+j+1 for j in range(n)})
 idx=[(i,mp.get(i)) for a,b in ranges for i in range(a,min(b,len(old))+1)]
 out=[]
 for i,n in idx:
  if n is None:continue
  if out and out[-1][1]+1==n:out[-1][1]=n
  else:out.append([n,n])
 return out,[i for i,n in idx if n is None]

def fresh_units(module):
 base=HERE.parent/module;fn=base/'spec-to-source.json'
 if not fn.exists():return [],None
 raw=fn.read_bytes();file_hash=digest(raw);data=json.loads(raw);out=[]
 def add(p,o,path):
  if not path or not str(path).startswith(('deliverables/','specs/','audit/')):return
  rng=pairs(o.get('lines',o.get('line',[])))
  if not rng:return
  status=o.get('status',o.get('capability_status',o.get('result',o.get('state'))))
  semantic=any(k in o for k in ['comparison','comparison_result','reason','current_unit','capability_ids','source_anchors','source','source_mappings','source_anchor_group_ref','capabilities','capability_status','capability_refs','source_refs','source_anchor_ids','semantic_disposition'])
  if semantic:out.append({'file':str(fn.relative_to(ROOT)),'file_sha256':file_hash,'pointer':p,'record_sha256':digest(o),'path':path,'ranges':rng,'status':status,'snapshot':o})
 for p,o,path in walk(data):
  if any(z in p for z in ['/source_anchor','/spec_anchor','/source_mapping','/data_anchor']):continue
  add(p,o,path)
 return out,{'path':str(fn.relative_to(ROOT)),'sha256':digest(raw),'count':len(out)}

def fresh_caps(module):
 fn=HERE.parent/module/'source-to-spec.json'
 if not fn.exists():return []
 raw=fn.read_bytes();file_hash=digest(raw);data=json.loads(raw)
 return [{'file':str(fn.relative_to(ROOT)),'file_sha256':file_hash,'pointer':'/capabilities/'+str(i),'record_sha256':digest(o),'id':o.get('id',o.get('capability_id')),'status':o.get('status',o.get('capability_status',o.get('state'))),'snapshot':o} for i,o in enumerate(data.get('capabilities',[]))]
