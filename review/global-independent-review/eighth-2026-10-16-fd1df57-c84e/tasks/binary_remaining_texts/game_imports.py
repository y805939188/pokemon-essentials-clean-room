"""Independent static Game PE import descriptor/thunk recovery."""
import pathlib,struct,json,hashlib
P=pathlib.Path(__file__).resolve().parent;b=pathlib.Path('/workspace/pokemon-essentials/Game.exe').read_bytes();pe=json.loads((P/'pe-sections.json').read_text())['Game.exe'];h=struct.unpack_from('<I',b,60)[0];opt=h+24;assert struct.unpack_from('<H',b,opt)[0]==0x20b
def off(r):
 for s in pe['sections']:
  if s['rva']<=r<s['rva']+s['bytes']:return s['offset']+r-s['rva']
 raise ValueError(hex(r))
def zstr(r):
 s=off(r);e=b.index(0,s);return {'start':s,'end':e,'text':b[s:e].decode('ascii'),'sha256':hashlib.sha256(b[s:e]).hexdigest()}
rva,size=struct.unpack_from('<II',b,opt+112+8);s=off(rva);rows=[];q=s
while True:
 original,timestamp,forward,name,first=struct.unpack_from('<IIIII',b,q)
 if not any((original,timestamp,forward,name,first)):break
 names=[];t=off(original or first);i=0
 while True:
  v=struct.unpack_from('<Q',b,t+8*i)[0]
  if not v:break
  x={'lookup_slot':t+8*i,'iat_rva':first+8*i,'iat_slot':off(first+8*i),'raw_thunk':v}
  if v>>63:x['ordinal']=v&65535
  else:x.update({'hint':struct.unpack_from('<H',b,off(v))[0],'name':zstr(v+2)})
  names.append(x);i+=1
 rows.append({'descriptor_start':q,'name':zstr(name),'lookup_rva':original,'first_thunk_rva':first,'imports':names});q+=20
out={'import_directory_rva':rva,'directory_size':size,'descriptor_start':s,'terminator_start':q,'descriptors':rows,'qualification':'PE static named dependency edges only. DLL chosen by runtime loader/search path and dynamic loads remain unproved; no DLL/EXE executed.'};(P/'game-imports.json').write_text(json.dumps(out,indent=2)+'\n');view=[]
for r in rows:view.append(r['name']['text']+': '+', '.join(x['name']['text'] if 'name' in x else '#'+str(x['ordinal']) for x in r['imports']))
(P/'game-import-view.txt').write_text('\n'.join(view)+'\n');print('\n'.join(view))
