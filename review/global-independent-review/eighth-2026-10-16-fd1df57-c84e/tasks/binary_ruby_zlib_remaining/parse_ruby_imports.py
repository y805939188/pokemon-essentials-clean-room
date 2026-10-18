"""Inert PE import table reader for the exact verified Ruby DLL."""
from pathlib import Path
import json,struct
P=Path(__file__).resolve().parent
B=Path('/workspace/pokemon-essentials/x64-msvcrt-ruby310.dll').read_bytes()
I=json.loads((P/'identities.json').read_text())['sources'][0]
def raw(rva):
 s=next(s for s in I['sections'] if s['rva']<=rva<s['rva']+s['size'])
 return s['raw']+rva-s['rva']
def cs(p):return B[p:B.index(0,p)].decode('ascii')
pe=struct.unpack_from('<I',B,0x3c)[0]
assert B[pe:pe+4]==b'PE\0\0'
optional=pe+24
assert struct.unpack_from('<H',B,optional)[0]==0x20b
directory,size=struct.unpack_from('<II',B,optional+112+8)
start=raw(directory);out=[]
for n in range(size//20):
 words=struct.unpack_from('<5I',B,start+n*20)
 if not any(words):break
 oft,stamp,forward,name,ft=words
 dll=cs(raw(name));fn=[]
 for j in range(10000):
  v=struct.unpack_from('<Q',B,raw(oft or ft)+j*8)[0]
  if not v:break
  fn.append(dict(index=j,iat_rva=ft+j*8,name=cs(raw(v)+2) if v>>63==0 else None,ordinal=(v&65535) if v>>63 else None))
 else:raise AssertionError('unterminated thunk table')
 out.append(dict(descriptor_raw=start+n*20,dll=dll,functions=fn))
else:raise AssertionError('unterminated import descriptors')
(P/'ruby-imports.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(import_directory_rva=directory,import_descriptor_count=len(out),import_count=sum(len(d['functions']) for d in out),dlls=[x['dll'] for x in out],zlib1_imports=[x for x in out if 'zlib1' in x['dll'].lower()]),indent=2))
