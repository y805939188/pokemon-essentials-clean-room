"""Read-only raw PE registry/builtin binding; writes only this isolated directory."""
from pathlib import Path
import json, struct, hashlib, gzip, re
ROOT=Path(__file__).resolve().parent
B=Path('/workspace/pokemon-essentials/x64-msvcrt-ruby310.dll').read_bytes()
I=json.loads((ROOT/'identities.json').read_text())['sources'][0]
S=json.loads((ROOT/'x64-msvcrt-ruby310.dll.coff-symbols.json').read_text())
Y=json.loads((ROOT/'yarb-decoded.json').read_text())
C=[json.loads(l) for l in gzip.open(ROOT/'candidate-contexts.jsonl.gz','rt')]
def raw(va):
 rva=va-I['image_base']
 for s in I['sections']:
  if s['rva']<=rva<s['rva']+s['size']:return s['raw']+rva-s['rva']
 raise AssertionError(hex(va))
def cs(va):
 p=raw(va);return B[p:B.index(0,p)].decode('ascii')
def symbols(va):
 return [s['name'] for s in S if s.get('rva')==va-I['image_base']]
registry=[]
p=4873280
for n in range(17):
 a,b,c=struct.unpack_from('<QQQ',B,p+n*24)
 if a==0:
  assert b==0 and c==0 and n==16
  break
 y=next(y for y in Y if y['start']==raw(b))
 assert c==y['bytes']
 registry.append(dict(index=n,raw=p+n*24,feature=cs(a),name_pointer=hex(a),container_pointer=hex(b),container_raw=raw(b),bytes=c,unit=y['name']))
calls=json.loads((ROOT/'builtin-load-callsites.json').read_text())
for j,call in enumerate(calls):
 feature=registry[j]['feature']
 rows=call['lines']
 assert '<rb_load_with_builtin_functions>' in rows[6],rows
 if feature=='gem_prelude':
  assert any('xor    edx,edx' in x for x in rows[:6]);tva=0
 else:
  lea=next(x for x in reversed(rows[:6]) if re.search(r'lea\s+rdx,',x))
  tva=int(re.search(r'# ([0-9a-f]+)',lea)[1],16)
 nlea=next(x for x in reversed(rows[:6]) if re.search(r'lea\s+rcx,',x))
 nva=int(re.search(r'# ([0-9a-f]+)',nlea)[1],16);assert cs(nva)==feature
 entries=[]
 if tva:
  tp=raw(tva)
  for n in range(1000):
   fp,argc,index,np,cp=struct.unpack_from('<QiiQQ',B,tp+n*32)
   if index==-1:
    assert fp==0 and argc==0 and cp==0
    assert cs(np)=='NULL',cs(np)
    break
   assert index==n
   entries.append(dict(index=index,name=cs(np),argc=argc,raw=tp+n*32,func_pointer=hex(fp),func_raw=raw(fp),func_symbols=symbols(fp),compiler_pointer=hex(cp),compiler_raw=raw(cp) if cp else None,compiler_symbols=symbols(cp) if cp else []))
  else:raise AssertionError('unterminated builtin table')
 unit=next(y for y in Y if y['name']==registry[j]['unit'])
 refs=[]
 for q in unit['iseqs']:
  for ins in q['code']:
   for op in ins['operands']:
    if op['type']=='R':
     ent=entries[op['index']];assert op['name']==ent['name'],(feature,op,ent)
     refs.append(dict(iseq=q['index'],pc=ins['pc'],opcode=ins['name'],builtin_index=op['index'],builtin_name=op['name'],native_func=ent['func_pointer']))
 unit['builtin_wiring']=dict(registry=registry[j],callsite=call,table_pointer=hex(tva),table_raw=raw(tva) if tva else None,entries=entries,bytecode_native_refs=refs)
 unit['candidate_ids']=[c['candidate_id'] for c in C if c['path']==I['path'] and c['start']>=unit['start'] and c['end_exclusive']<=unit['end_exclusive']]
 unit['text_read_ids']=sorted({c['read_id'] for c in C if c['candidate_id'] in unit['candidate_ids']})
inv=[{k:v for k,v in u.items() if k not in ('objects','iseqs')}|dict(iseq_count=len(u['iseqs']),object_count=len(u['objects']),instruction_count=sum(len(q['code']) for q in u['iseqs']),semantic_reception='FULL_STATIC_READ',native_leaf_cfg='NOT_FULLY_REVIEWED',target_execution='NOT_EXECUTED') for u in Y]
(ROOT/'new-program-inventory.json').write_text(json.dumps(dict(schema='gr8.ruby-zlib.program-inventory/v1',registry_start=p,registry_end_exclusive=p+17*24,registry_sha256=hashlib.sha256(B[p:p+17*24]).hexdigest(),units=inv),ensure_ascii=False,indent=2)+'\n')
for u in inv:
 print(u['name'],u['start'],u['end_exclusive'],u['sha256'],'candidates',len(u['candidate_ids']))
 for e in u['builtin_wiring']['entries']:
  print(' ',e['index'],e['name'],e['argc'],e['func_pointer'],e['func_symbols'],'compiler',e['compiler_pointer'],e['compiler_symbols'])
print(json.dumps(dict(units=len(inv),candidate_memberships=sum(len(u['candidate_ids']) for u in inv),builtin_entries=sum(len(u['builtin_wiring']['entries']) for u in inv),bytecode_refs=sum(len(u['builtin_wiring']['bytecode_native_refs']) for u in inv))))
