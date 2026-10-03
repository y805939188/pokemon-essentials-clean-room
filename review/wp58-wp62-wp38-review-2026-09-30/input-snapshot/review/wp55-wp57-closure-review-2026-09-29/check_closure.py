"""Independent text/byte/diff checks; does not execute reference or extractor code."""
from pathlib import Path
import json,hashlib,re,subprocess
ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=ROOT/'review/wp55-wp57-closure-review-2026-09-29'
PREV=ROOT/'review/wp55-wp57-recheck-2026-09-29'
REF=ROOT/'reference/pokemon-essentials'
COMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def meta(p):
    b=p.read_bytes();return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def match(p,d):return p.is_file() and meta(p)=={k:d[k] for k in ['sha256','bytes']}
def save(name,d):(OUT/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
f=json.loads((OUT/'input-manifest.json').read_text());old=json.loads((PREV/'input-manifest.json').read_text())
checks={'fixed_inputs':len(f['inputs']),'changed_inputs':[x['path'] for x in f['inputs'] if not match(ROOT/x['path'],x)],
 'changed_snapshots':[x['path'] for x in f['inputs'] if not match(OUT/'input-snapshot'/x['path'],x)],'prior':[]}
for name in ['wp55-wp57-recheck-2026-09-29','wp55-wp57-review-2026-09-28','wp52b-wp52c-wp54-recheck-2026-09-28','wp52b-wp52c-wp54-review-2026-09-28',
 'wp50-wp51-wp52a-recheck-2026-09-28','wp50-wp51-wp52a-review-2026-09-28','wp46-wp47-review-2026-09-27','wp42-wp48-wp49-recheck-2026-09-27']:
    d=ROOT/'review'/name;inp=json.loads((d/'input-manifest.json').read_text())['inputs'];arts=json.loads((d/'final-checks.json').read_text())['artifacts']
    checks['prior'].append({'review':name,'snapshots':len(inp),'changed_snapshots':[x['path'] for x in inp if not match(d/'input-snapshot'/x['path'],x)],
      'artifacts':len(arts),'changed_artifacts':[x['path'] for x in arts if not match(ROOT/x['path'],x)]})
mp=[x['path'] for x in f['manifest_rows']];op=[x['path'] for x in old['manifest_rows']]
tp=[x['path'] for x in f['delivery_rows']];ot=[x['path'] for x in old['delivery_rows']]
checks['registry']={'manifest':len(mp),'TSV':len(tp),'old_manifest_order_preserved':[p for p in mp if p in set(op)]==op,
 'old_TSV_order_preserved':[p for p in tp if p in set(ot)]==ot,'added':len(set(mp)-set(op)),'added_sets_equal':set(mp)-set(op)==set(tp)-set(ot)}
diffs=[]
for p in sorted((PREV/'revision-diffs').glob('*.diff')):
    ls=p.read_text().splitlines(keepends=True);base=ls[0][4:].strip();target=ls[1][4:].strip()
    src=(ROOT/base).read_text().splitlines(keepends=True);res=[];pos=0;i=2
    while i<len(ls):
        m=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',ls[i]);assert m,(p,i)
        start=int(m[1])-1 if int(m[1]) else 0;res+=src[pos:start];pos=start;i+=1
        while i<len(ls) and not ls[i].startswith('@@ '):
            line=ls[i];i+=1
            if line.startswith('\\'):continue
            if line[0] in ' -':assert src[pos]==line[1:],(p,pos);pos+=1
            if line[0] in ' +':res.append(line[1:])
    res+=src[pos:];diffs.append({'file':str(p.relative_to(ROOT)),**meta(p),'base':base,'target':target,'exact':''.join(res).encode()==(ROOT/target).read_bytes()})
save('diff-checks.json',diffs)
delivery=ROOT/'review/wp55-wp57-delivery-2026-09-28'
bd=json.loads((delivery/'boundary-checks.json').read_text());bindings=[{**d,'matches':match(ROOT/d['sender'],d)} for d in bd['bindings']]
specs=['specs/combat/wp55-facility-session-and-restoration.md','specs/combat/wp56-palace-and-arena-variants.md','specs/creature-rpg/wp57-factory-rentals-and-swaps.md']
scenarios=[];inline=[]
for p in specs:
    a=(PREV/'input-snapshot'/p).read_text();b=(ROOT/p).read_text()
    def rows(s):return {re.match(r'^\| ([WPF]\d+) \|',l)[1]:l for l in s.splitlines() if re.match(r'^\| [WPF]\d+ \|',l)}
    ar,br=rows(a),rows(b)
    scenarios.append({'file':p,'before':len(ar),'after':len(br),'added':sorted(set(br)-set(ar)),'removed':sorted(set(ar)-set(br)),
       'changed':[k for k in ar if k in br and ar[k]!=br[k]],'unchanged':sum(ar[k]==br.get(k) for k in ar)})
    for m in re.finditer(r'\]\(([^)]+\.md)\)（[^`]*`([0-9a-f]{64})`，([\d,]+)字节',b):
        path,h,n=m.groups();d={'sha256':h,'bytes':int(n.replace(',',''))}
        inline.append({'file':p,'target':path,**d,'matches':match((ROOT/p).parent/path,d)})
oldself=json.loads((ROOT/'review/wp52b-wp52c-wp54-delivery-2026-09-28/self-checks.json').read_text());embedded=[];vectors=[]
for p,d in oldself['artifacts'].items():embedded.append({'file':p,'record':'artifacts','matches':match(ROOT/p,d)})
for pkg in oldself['packages']:
    embedded.append({'file':pkg['file'],'record':'packages','matches':match(ROOT/pkg['file'],pkg)})
    actual={}
    for l in (ROOT/pkg['file']).read_text().splitlines():
        if re.match(r'^\| [BCQ]\d+[a-z]? \|',l):
            cs=[x.strip() for x in l.strip('|').split('|')];actual[cs[0]]={'input':cs[1],'expected':cs[2]}
    for v in pkg['vectors']:
        if actual[v['id']]!={k:v[k] for k in ['input','expected']}:vectors.append({'package':pkg['package'],'id':v['id']})
jsons=[p for p in mp if p.endswith('.json')];badjson=[]
for p in jsons:
    try:json.loads((ROOT/p).read_text())
    except Exception as e:badjson.append({'file':p,'error':str(e)})
links=[];badlinks=[]
for p in list((ROOT/'specs').rglob('*.md'))+[ROOT/'planning/feature-matrix.md']:
    for dest in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        d=dest.strip('<>')
        if re.match(r'\w+://',d) or d.startswith('#'):continue
        d=re.sub(r':\d+$','',d.split('#')[0])
        if not d:continue
        rec={'file':str(p.relative_to(ROOT)),'target':d,'exists':(p.parent/d).exists()};links.append(rec)
        if not rec['exists']:badlinks.append(rec)
save('propagation-checks.json',{'scenario_rows':scenarios,'boundary_bindings':bindings,'inline_bindings':inline,'C02_current_identity_checks':embedded,'C02_vector_mismatches':vectors,
 'registered_json':len(jsons),'bad_json':badjson,'spec_matrix_links':len(links),'bad_links':badlinks})
sources=[]
for d in json.loads((PREV/'source-checks.json').read_text())['paths']:
    p=ROOT/d['path'];rel=str(p.relative_to(REF));blob=subprocess.run(['git','--no-optional-locks','-C',str(REF),'show',COMMIT+':'+rel],capture_output=True,check=True).stdout
    sources.append({'path':d['path'],**meta(p),'commit_blob_equal':blob==p.read_bytes(),'unchanged_since_first_review':match(p,d)})
save('source-checks.json',{'commit':COMMIT,'paths':sources,'fresh_scope':'8 paths; final two findings, C03 and direct propagation only; see static-checks.json; earlier accepted scope inherited','source_execution':False})
checks['reference_head']=subprocess.run(['git','--no-optional-locks','-C',str(REF),'rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip()
checks['reference_status']=subprocess.run(['git','--no-optional-locks','-C',str(REF),'status','--porcelain'],capture_output=True,text=True,check=True).stdout
save('identity-checks.json',checks)
print(json.dumps({'fixed':checks['fixed_inputs'],'changed_inputs':checks['changed_inputs'],'prior':checks['prior'],'registry':checks['registry'],'diffs':len(diffs),'bad_diffs':[d['file'] for d in diffs if not d['exact']],
 'scenarios':scenarios,'boundary_bindings':len(bindings),'bad_bindings':[d for d in bindings if not d['matches']], 'inline_bindings':len(inline),'bad_inline':[d for d in inline if not d['matches']],
 'C02_stale':[d for d in embedded if not d['matches']],'C02_vector_mismatches':vectors,'JSON':len(jsons),'bad_json':badjson,'links':len(links),'bad_links':badlinks,'sources':len(sources),'bad_source':[d['path'] for d in sources if not d['commit_blob_equal'] or not d['unchanged_since_first_review']]},ensure_ascii=False,indent=2))
