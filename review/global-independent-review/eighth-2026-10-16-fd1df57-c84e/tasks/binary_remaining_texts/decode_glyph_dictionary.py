"""Inert complete trie traversal following the received FreeType lookup structure."""
import pathlib,json,struct,hashlib
P=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes();s=11961024;z=12017021;raw=b[s:z];covered=set();entries=[];nodes=[]
def mark(a,e):
 assert 0<=a<e<=len(raw);covered.update(range(a,e))
def u16(i):return struct.unpack_from('>H',raw,i)[0]
def walk(pos,prefix,stack):
 assert pos not in stack and len(stack)<128;stack=stack+(pos,);start=pos;name=prefix
 while True:
  c=raw[pos];name+=chr(c&127);pos+=1
  if not c&128:break
 flags=raw[pos];pos+=1;value=None
 if flags&128:value=u16(pos);pos+=2;entries.append({'name':name,'unicode':value,'node_start':s+start})
 n=flags&127;children=[u16(pos+2*i) for i in range(n)];mark(start,pos+2*n);nodes.append({'start':s+start,'end':s+pos+2*n,'prefix_name':name,'unicode':value,'children_absolute_offsets':[s+i for i in children]})
 for q in children:walk(q,name,stack)
assert raw[0]==0;count=raw[1];mark(0,2+2*count)
for i in range(count):walk(u16(2+2*i),'',())
assert len({r['name'] for r in entries})==len(entries);gaps=sorted(set(range(len(raw)))-covered)
out={'source_path':'Game.exe','start':s,'end':z,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'root_children':count,'nodes':nodes,'entries':entries,'covered_bytes':len(covered),'unparsed_offsets':[s+i for i in gaps],'qualification':'Metadata dictionary name->Unicode mapping, not executable target code. Complete byte/trie structure only; no font rasterization or API reachability is inferred.'};(P/'glyph-dictionary-structure.json').write_text(json.dumps(out,indent=2)+'\n');(P/'glyph-dictionary-name-view.txt').write_text('\n'.join('%s=%04X'%(r['name'],r['unicode']) for r in sorted(entries,key=lambda r:r['name']))+'\n');print(json.dumps({'bytes':len(raw),'entries':len(entries),'nodes':len(nodes),'covered_bytes':len(covered),'unparsed_bytes':len(gaps)}))
