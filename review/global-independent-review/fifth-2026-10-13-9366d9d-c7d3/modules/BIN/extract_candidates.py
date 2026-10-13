"""Reproduce fixed-R plaintext inventories. Raw text is written only under /tmp."""
import pathlib,json,hashlib,re,struct,collections
O=pathlib.Path(__file__).parent;T=pathlib.Path('/tmp/gr5-bin-readable');T.mkdir(exist_ok=True)
r=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Game.exe').read_bytes()
res=json.loads((O.parent/'RES/binary-interface-audit.json').read_text())['records'][0]
pe=struct.unpack_from('<I',r,60)[0];n=struct.unpack_from('<H',r,pe+6)[0];sz=struct.unpack_from('<H',r,pe+20)[0];sections=[]
for i in range(n):
 p=pe+24+sz+i*40;name=r[p:p+8].split(b'\0')[0].decode();vs,va,rs,off=struct.unpack_from('<4I',r,p+8);sections.append({'name':name,'start':off,'end':off+rs})
blocks=[]
for i,z in enumerate(res['embedded_readable']['blocks']):
 d=r[z['offset']:z['offset']+z['size']];assert hashlib.sha256(d).hexdigest()==z['sha256']
 b={k:v for k,v in z.items() if k in ['offset','size','sha256','lines','kind']};b['id']=f'B{i:02}';blocks.append(b)
 if i:(T/f'B{i:02}.txt').write_bytes(d)
(O/'block-inventory.json').write_text(json.dumps({'schema_version':'gr5.review.v1','source':'R/Game.exe','blocks':blocks,'sections':sections},ensure_ascii=False,indent=2)+'\n')
rows=[]
for enc,pattern in [('ascii',rb'[\x20-\x7e]{4,}'),('utf-16-le',rb'(?:[\x20-\x7e]\x00){4,}')]:
 for m in re.finditer(pattern,r):
  block=next((b['id'] for b in blocks if b['offset']<=m.start()<b['offset']+b['size']),None);section=next((s['name'] for s in sections if s['start']<=m.start()<s['end']),'outside_sections')
  rows.append({'id':len(rows),'offset':m.start(),'size':len(m.group()),'encoding':enc,'sha256':hashlib.sha256(m.group()).hexdigest(),'section':section,'block':block,'text':m.group().decode(enc)})
assert len(rows)==res['string_scan']['candidate_count']==161104
(T/'strings.jsonl').write_text(''.join(json.dumps(v)+'\n' for v in rows))
spans=[{'offset':m.start(),'size':len(m.group()),'text':m.group().decode()} for m in re.finditer(rb'[\x09\x0a\x0d\x20-\x7e]{16,}',r)]
short=[s for s in spans if not any(b['offset']==s['offset'] for b in blocks) and re.search(r'\b(?:void\s+main|uniform\s+(?:float|vec|mat|sampler)|varying\s+(?:vec|float)|module\s+[A-Z]|def\s+(?:self\.)?\w+|class\s+[A-Z])',s['text'])]
assert len(short)==28
(T/'short-code.json').write_text(json.dumps(short))
ml=[s for s in spans if '\n' in s['text'] and not any(b['offset']==s['offset'] for b in blocks)]
assert len(ml)==665
(T/'multiline-short.json').write_text(json.dumps(ml))
cs=[v for v in rows if not v['block'] and v['section'] in ['.data','.rdata'] and re.search(r'\b(?:if|unless|rescue|class|module|def|return|while|begin|proc|lambda|end|require)\b|=>|->|\$[A-Za-z_]',v['text'])]
assert len(cs)==622
(T/'code-suspects.json').write_text(json.dumps(cs))
intervals=[(s['offset'],s['offset']+s['size']) for s in short[:-1]]+[(b['offset'],b['offset']+b['size']) for b in blocks if b['kind']=='embedded_shader_text' and b['id']!='B52']+[(10704000,10787965),(12051776,12174560),(10582784,10582939),(10678624,10678648),(10678656,10678671),(11657192,11657281),(11657282,11657307)]
pat=r'\b(?:def|module|class|alias|alias_method|require|load|eval|proc|lambda|BEGIN|END|function|precision|uniform|varying|attribute|void|float|vec[234]|mat[234])\b|\.new\(|\.call\(|(?:^|\s)(?:if|unless|for|while|return)\b|^#(?:define|version|extension|if)|\$[A-Za-z_]\w*\s*='
broad=[s for s in spans if not any(a<=s['offset']<b for a,b in intervals) and re.search(pat,s['text'])]
assert len(broad)==360
(T/'broad-code-suspects.json').write_text(json.dumps(broad))
print('Fixed input extracted:',len(blocks),'long blocks,',len(rows),'string candidates;',len(short),'additional code-shaped spans including one help-text false positive.')
