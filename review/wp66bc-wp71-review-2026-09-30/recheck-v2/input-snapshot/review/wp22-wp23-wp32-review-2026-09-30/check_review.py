"""Independent reviewer: bytes, text, literal tables and fixed constants only."""
from pathlib import Path
import hashlib, json, re, subprocess

ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT = ROOT/'review/wp22-wp23-wp32-review-2026-09-30'
DEL = ROOT/'review/wp22-wp23-wp32-delivery-2026-09-30'
PREV = ROOT/'review/wp58-wp62-wp38-review-2026-09-30/closure-review'
REF = ROOT/'reference/pokemon-essentials'
COMMIT = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'

def meta(p):
    b=p.read_bytes();return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def read(p):return json.loads(p.read_text())
def save(n,d):(OUT/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def match(p,d):return p.is_file() and meta(p)=={k:d[k] for k in ('sha256','bytes')}

fixed=read(OUT/'input-manifest.json')
assert len(fixed['inputs'])==876
assert all(match(ROOT/x['path'],x) and match(OUT/'input-snapshot'/x['path'],x) for x in fixed['inputs'])
prior=[]
for name in ['wp58-wp62-wp38-review-2026-09-30/closure-review','wp58-wp62-wp38-review-2026-09-30/recheck-v2','wp58-wp62-wp38-review-2026-09-30',
 'wp55-wp57-closure-review-2026-09-29','wp55-wp57-recheck-2026-09-29','wp55-wp57-review-2026-09-28',
 'wp52b-wp52c-wp54-recheck-2026-09-28','wp52b-wp52c-wp54-review-2026-09-28','wp50-wp51-wp52a-recheck-2026-09-28',
 'wp50-wp51-wp52a-review-2026-09-28','wp46-wp47-review-2026-09-27','wp42-wp48-wp49-recheck-2026-09-27']:
    d=ROOT/'review'/name;f=read(d/'input-manifest.json')['inputs'];a=read(d/'final-checks.json')['artifacts']
    bad=[x['path'] for x in f if not match(d/'input-snapshot'/x['path'],x)]
    bad_a=[x['path'] for x in a if not match(ROOT/x['path'],x)]
    assert not bad and not bad_a
    prior.append({'review':name,'snapshots':len(f),'listed_artifacts':len(a),'changed_snapshots':bad,'changed_artifacts':bad_a})

diffs=[]
for p in sorted((DEL/'backfill-diffs').glob('*.diff')):
    lines=p.read_text().splitlines(keepends=True);base=lines[0][4:].strip();target=lines[1][4:].strip()
    if base.startswith('closure-review/input-snapshot/'):
        base=str(PREV.relative_to(ROOT))+'/input-snapshot/'+base.removeprefix('closure-review/input-snapshot/')
    src=(ROOT/base).read_text().splitlines(keepends=True);result=[];pos=0;i=2
    while i<len(lines):
        m=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',lines[i]);assert m,(p,i)
        start=int(m[1])-1 if int(m[1]) else 0;result+=src[pos:start];pos=start;i+=1
        while i<len(lines) and not lines[i].startswith('@@ '):
            l=lines[i];i+=1
            if l.startswith('\\'):continue
            if l[0] in ' -':assert src[pos]==l[1:],(p,pos);pos+=1
            if l[0] in ' +':result.append(l[1:])
    result+=src[pos:];exact=''.join(result).encode()==(ROOT/target).read_bytes();assert exact
    diffs.append({'path':str(p.relative_to(ROOT)),**meta(p),'base':base,'target':target,'exact':exact})
assert len(diffs)==6
save('diff-checks.json',diffs)

selfd=read(DEL/'self-checks.json');bd=read(DEL/'boundary-checks.json')
assert len(bd['bindings'])==45
bindings=[{**x,'matches':match(ROOT/x['sender'],x)} for x in bd['bindings']]
assert all(x['matches'] for x in bindings)
artifacts=[];scenario_counts={};inline=[]
for pkg in selfd['packages']:
    for x in pkg['artifacts']:
        artifacts.append({**x,'matches':match(ROOT/x['path'],x)})
    p=ROOT/pkg['artifacts'][0]['path'];txt=p.read_text();count=len(re.findall(r'^\| W\d+ \|',txt,re.M))
    scenario_counts[pkg['package']]=count
    for line in txt.splitlines():
        m=re.match(r'^\| WP\d+(?:-[ABC])? \| `([^`]+)` \| `([0-9a-f]{64})` \| ([0-9,]+) \|$',line)
        if m:
            target,h,n=m.groups();e={'sha256':h,'bytes':int(n.replace(',',''))};inline.append({'file':str(p.relative_to(ROOT)),'target':target,**e,'matches':match(ROOT/target,e)})
assert scenario_counts=={'WP22':25,'WP23':42,'WP32':38}
assert all(x['matches'] for x in artifacts+inline) and len(inline)==45
js=[x['path'] for x in fixed['manifest_rows'] if x['path'].endswith('.json')]
for rel in js:read(ROOT/rel)
links=[]
for p in list((ROOT/'specs').rglob('*.md'))+[ROOT/'planning/feature-matrix.md']:
    for dest in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        if re.match(r'\w+://',dest) or dest.startswith('#'):continue
        dest=re.sub(r':\d+$','',dest.strip('<>').split('#')[0])
        if not dest:continue
        assert (p.parent/dest).exists(),(p,dest)
        links.append({'file':str(p.relative_to(ROOT)),'target':dest})
old_tables=[]
for rel in ['specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md','specs/pokemon-rules/wp38-capture-and-receiving.md']:
    table=lambda p:[l for l in p.read_text().splitlines() if l.startswith('|')]
    old_tables.append({'path':rel,'table_rows_unchanged':table(ROOT/rel)==table(PREV/'input-snapshot'/rel)})
assert all(x['table_rows_unchanged'] for x in old_tables)
save('integrity-checks.json',{'fixed':876,'prior':prior,'artifacts':artifacts,'bindings':bindings,'inline_bindings':inline,
 'scenario_counts_only':scenario_counts,'registered_JSON_valid':len(js),'spec_matrix_links_exist':len(links),'backfill_old_tables':old_tables,
 'note':'Mechanical identity/count checks do not decide behavioral correctness.'})

# Plain PBS records, preserving repeated fields and order; not a game data loader.
def pbs(rel):
    entries=[];cur=None
    for n,line in enumerate((REF/rel).read_text().splitlines(),1):
        line=line.lstrip('\ufeff').strip()
        if not line or line.startswith('#'):continue
        m=re.match(r'^\[([^]]+)\]',line)
        if m:cur={'id':m[1],'line':n,'fields':[]};entries.append(cur);continue
        if cur and '=' in line:
            k,v=line.split('=',1);cur['fields'].append((k.strip(),v.strip(),n))
    return entries
def fields(x):return {k:v for k,v,_ in x['fields']}
def mdrows(text):
    return [[v.strip() for v in l.strip('|').split('|')] for l in text.splitlines() if l.startswith('|') and not l.startswith('| ---')]
checks=[]
forms=pbs('PBS/pokemon_forms.txt');mega=[]
for x in forms:
    d=fields(x)
    if 'MegaStone' not in d and 'MegaMove' not in d:continue
    sp,form=x['id'].split(',');req=('石 '+d['MegaStone']) if 'MegaStone' in d else ('已知招式 '+d['MegaMove'])
    mega.append([sp.strip(),str(int(form)),req,'／'.join(d['BaseStats'].split(',')),str(x['line'])])
text=(ROOT/'specs/pokemon-rules/wp22-transformation-data.md').read_text()
doc=[x for x in mdrows(text.split('## 2.')[0]) if re.fullmatch(r'[A-Z0-9_]+',x[0])]
checks.append({'name':'WP22 all48 Mega table values/order/source lines','source_count':len(mega),'document_count':len(doc),'matches':mega==doc})
items=pbs('PBS/items.txt');stones=[x['id'] for x in items if 'MegaStone' in fields(x).get('Flags','').split(',')];rings=[x['id'] for x in items if 'MegaRing' in fields(x).get('Flags','').split(',')]
checks.append({'name':'WP22 default47 stones and1 ring','stones':len(stones),'rings':rings,'matches':len(stones)==47 and rings==['MEGARING']})

text=(ROOT/'specs/pokemon-rules/wp23-shadow-data-and-vectors.md').read_text()
natures=[]
src=(REF/'Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb').read_text()
for m in re.finditer(r':([A-Z]+)\s*=>\s*\[\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+)\]',src):natures.append(list(m.groups()))
doc=[x for x in mdrows(text.split('## 2.')[0]) if re.fullmatch('[A-Z]+',x[0])]
checks.append({'name':'WP23 all25 Nature rows','source_count':len(natures),'matches':natures==doc})
shadow=pbs('PBS/Shadow Pokémon backup/shadow_pokemon.txt');data=[]
for x in shadow:
    f=fields(x);data.append([x['id'],f.get('GaugeSize','4000'),'／'.join(f.get('Moves','').split(',')),str(x['line'])])
doc=[x for x in mdrows(text.split('### 3.1')[1].split('### 3.2')[0]) if re.fullmatch(r'[A-Z0-9_]+',x[0])]
checks.append({'name':'WP23 all131 optional Shadow records','source_count':len(data),'matches':data==doc})
moves=pbs('PBS/Shadow Pokémon backup/moves_shadow_pkmn.txt');data=[[x['id'],fields(x)['FunctionCode']] for x in moves]
doc=[x for x in mdrows(text.split('### 3.2')[1]) if x[0].startswith('SHADOW')]
checks.append({'name':'WP23 all18 optional move function IDs','source_count':len(data),'matches':data==doc})
optional_items=pbs('PBS/Shadow Pokémon backup/items_shadow_pkmn.txt')
checks.append({'name':'WP23 optional item flags absent','count':len(optional_items),'matches':len(optional_items)==4 and all('Flags' not in fields(x) for x in optional_items)})

text=(ROOT/'specs/pokemon-rules/wp32-context-inputs-and-scenarios.md').read_text()
methodrows=[x for x in mdrows(text.split('## 1.')[1].split('## 2.')[0]) if re.fullmatch(r'[A-Za-z0-9]+',x[0])]
methods={x[0] for x in methodrows};evos=[]
for file in ['pokemon.txt','pokemon_forms.txt']:
    for x in pbs('PBS/'+file):
        for k,v,line in x['fields']:
            if k!='Evolution':continue
            vals=[z.strip() for z in v.split(',')]
            for i in range(0,len(vals),3):
                target,method=vals[i:i+2];param=vals[i+2] if i+2<len(vals) else ''
                if method in methods:evos.append([x['id'],target,method,param or '无',f'{file}:{line}'])
doc=[x for x in mdrows(text.split('## 2.')[1].split('## 3.')[0]) if re.fullmatch(r'[A-Z0-9_,]+',x[0])]
counts={m:sum(x[2]==m for x in evos) for m in sorted(methods)}
registry=set(re.findall(r':id\s*=>\s*:(\w+)',(REF/'Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb').read_text()))
checks.append({'name':'WP32 35 contextual IDs registered','count':len(methods),'matches':len(methods)==35 and methods<=registry})
checks.append({'name':'WP32 all57 evolution entries/order/lines','source_count':len(evos),'document_count':len(doc),'matches':evos==doc})
checks.append({'name':'WP32 per-method counts','counts':counts,'matches':all(counts[x[0]]==int(x[1]) for x in methodrows)})
save('literal-data-checks.json',checks)

# Fixed independent arithmetic vectors only. No branching reference simulation.
save('constant-checks.json',{'method':'Fixed constants and finite set boundaries only; reference not executed',
 'Mega_HP':{'level':50,'IV':0,'EV':0,'base80':(2*80)*50//100+50+10,'base95':(2*95)*50//100+50+10,'current70_after':70+15,'current5_after_reversion':max(5-15,1)},
 'purification_exp':[[n,n*4//5] for n in [121,1,4,5,0,416]],
 'chamber_T_E0':[n*(n+1)//2 for n in range(5)],'chamber_T_all_edges':[n*(n+1)//2+n for n in range(1,5)],
 'chamber_F_all_edges_plus_center':[n+1+n//2 for n in range(1,5)],'hyper_default_positive_G':{'success_values':1001,'values':4000,'percentage':25.025},
 'hyper_G0_default':'Ordinary Battle → numeric rand(0) → [0,1) float; every such value <=1000. Stored flag and message occur; effective getter remains false. Source/language contract, no RNG execution.'})

srcd=read(DEL/'source-identities.json');sources=[]
extra=['Data/Scripts/001_Technical/002_RubyUtilities.rb','Data/Scripts/010_Data/001_Hardcoded data/008_Stat.rb','Data/Scripts/010_Data/001_Hardcoded data/001_GrowthRate.rb']
paths={x['path'] for x in srcd['sources']}|{'reference/pokemon-essentials/'+x for x in extra}
for path in sorted(paths):
    p=ROOT/path;rel=str(p.relative_to(REF));blob=subprocess.run(['git','--no-optional-locks','-C',str(REF),'show',COMMIT+':'+rel],capture_output=True,check=True).stdout
    assert blob==p.read_bytes(),path
    sources.append({'path':path,**meta(p),'commit_blob_equal':True})
assert all(match(ROOT/x['path'],x) for x in srcd['sources'])
save('source-checks.json',{'commit':COMMIT,'delivery_source_count':len(srcd['sources']),'sources':sources,'note':'Blob identity verification separate from actual semantic reading ranges in review-notes.json.'})
head=subprocess.run(['git','--no-optional-locks','-C',str(REF),'rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip()
status=subprocess.run(['git','--no-optional-locks','-C',str(REF),'status','--porcelain'],capture_output=True,text=True,check=True).stdout
assert head==COMMIT and not status
save('reference-checks.json',{'head':head,'ordinary_status':status})
print(json.dumps({'fixed':876,'manifest':874,'TSV':778,'diffs_exact':6,'scenario_counts':scenario_counts,'bindings':len(bindings),'inline_bindings':len(inline),'JSON':len(js),'links':len(links),'source_blobs':len(sources),'literal_checks':checks,'old_tables':old_tables,'reference_clean':True},ensure_ascii=False,indent=2))
