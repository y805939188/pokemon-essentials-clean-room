"""Extract finite plaintext spans from fixed Game.exe without loading it."""
import hashlib, json, pathlib, re
root=pathlib.Path(__file__).resolve().parents[1]
src=root.parents[2]/'reference/pokemon-essentials/Game.exe'
b=src.read_bytes();out=root/'evidence/bin-readable';out.mkdir(exist_ok=True)
rows=[]
for m in re.finditer(rb'[\x09\x0a\x0d\x20-\x7e]{16,}',b):
    t=m.group().decode('ascii')
    if '\n' not in t and not re.search(r'\b(?:module|class|def|require|eval|alias|uniform|varying|void\s+main)\b',t): continue
    code=bool(re.search(r'\b(?:void\s+main|uniform\s+(?:float|vec|mat|sampler)|varying\s+(?:vec|float)|module\s+[A-Z]|def\s+(?:self\.)?\w+|class\s+[A-Z])',t))
    controller=t.startswith('# Game Controller DB')
    if code:kind='shader' if re.search(r'\b(?:void\s+main|uniform|varying)\b',t) else 'compatibility_script_candidate'
    elif controller:kind='controller_data'
    else:kind='other_printable_multiline_or_keyword_data'
    row={'id':f'BIN-{len(rows):04d}','file_offset':m.start(),'bytes':len(m.group()),'sha256':hashlib.sha256(m.group()).hexdigest(),'lines':len(t.splitlines()),'kind':kind,'status':'EXTRACTED_NOT_YET_SEMANTICALLY_READ'}
    if code or controller:
        p=out/(row['id']+'.txt');p.write_bytes(m.group());row['extracted_path']=str(p.relative_to(root))
    rows.append(row)
(out/'inventory.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'finite_candidate_spans':len(rows),'code_candidates':sum('extracted_path' in x and x['kind']!='controller_data' for x in rows),'controller_spans':sum(x['kind']=='controller_data' for x in rows),'code_ranges':[x for x in rows if 'extracted_path' in x and x['kind']!='controller_data']},ensure_ascii=False,indent=2))
