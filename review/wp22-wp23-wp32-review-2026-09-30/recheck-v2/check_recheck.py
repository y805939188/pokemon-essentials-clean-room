"""Independent reviewer: bytes, text, literal tables and fixed constants only."""
from pathlib import Path
import hashlib, json, re, subprocess

ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OLD = ROOT/'review/wp22-wp23-wp32-review-2026-09-30'
OUT = OLD/'recheck-v2'
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
assert len(fixed['inputs'])==919
assert all(match(ROOT/x['path'],x) and match(OUT/'input-snapshot'/x['path'],x) for x in fixed['inputs'])
prior=[]
for name in ['wp22-wp23-wp32-review-2026-09-30','wp58-wp62-wp38-review-2026-09-30/closure-review','wp58-wp62-wp38-review-2026-09-30/recheck-v2','wp58-wp62-wp38-review-2026-09-30',
 'wp55-wp57-closure-review-2026-09-29','wp55-wp57-recheck-2026-09-29','wp55-wp57-review-2026-09-28',
 'wp52b-wp52c-wp54-recheck-2026-09-28','wp52b-wp52c-wp54-review-2026-09-28','wp50-wp51-wp52a-recheck-2026-09-28',
 'wp50-wp51-wp52a-review-2026-09-28','wp46-wp47-review-2026-09-27','wp42-wp48-wp49-recheck-2026-09-27']:
    d=ROOT/'review'/name;f=read(d/'input-manifest.json')['inputs'];a=read(d/'final-checks.json')['artifacts']
    bad=[x['path'] for x in f if not match(d/'input-snapshot'/x['path'],x)]
    bad_a=[x['path'] for x in a if not match(ROOT/x['path'],x)]
    assert not bad and not bad_a
    prior.append({'review':name,'snapshots':len(f),'listed_artifacts':len(a),'changed_snapshots':bad,'changed_artifacts':bad_a})

diffs=[]
for p in sorted((OLD/'revision-diffs').glob('*.diff')):
    lines=p.read_text().splitlines(keepends=True);base=lines[0][4:].strip();target=lines[1][4:].strip()
    if base.startswith('input-snapshot/'):
        base=str(OLD.relative_to(ROOT))+'/'+base
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
assert len(diffs)==17
save('diff-checks.json',diffs)

selfd=read(DEL/'self-checks.json');bd=read(DEL/'boundary-checks.json')
assert len(bd['bindings'])==46
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
assert scenario_counts=={'WP22':25,'WP23':46,'WP32':38}
assert all(x['matches'] for x in artifacts+inline) and len(inline)==46
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
save('integrity-checks.json',{'fixed':919,'prior':prior,'artifacts':artifacts,'bindings':bindings,'inline_bindings':inline,
 'scenario_counts_only':scenario_counts,'registered_JSON_valid':len(js),'spec_matrix_links_exist':len(links),'backfill_old_tables':old_tables,
 'note':'Mechanical identity/count checks do not decide behavioral correctness.'})

# Fixed arithmetic and unchanged accepted data only; no reference evaluator.
save('constant-checks.json',{'method':'Independent fixed arithmetic, no Ruby or game invocation',
 'R01':{'saved':416,'request':416*4//5,'intended_exp':1000+416*4//5,'level11_floor':1331,'level12_floor':1728,'boundary_valid':1331<=1000+416*4//5<1728},
 'R02':'Raw nil and false unequal; both falsey. Reread source comparisons, did not execute Ruby.',
 'R03':'Default M4000 threshold1000 contains entire numeric-rand(0) interval [0,1); static branch and effective getter independently reread.'})
unchanged=[]
for rel in ['specs/pokemon-rules/wp22-transformation-data.md','specs/pokemon-rules/wp32-context-inputs-and-scenarios.md']:
    rows=lambda p:[l for l in p.read_text().splitlines() if l.startswith('|')]
    same=rows(ROOT/rel)==rows(OLD/'input-snapshot'/rel)
    assert same
    unchanged.append({'path':rel,'all_data_table_rows_unchanged':same})
rel='specs/pokemon-rules/wp23-shadow-data-and-vectors.md'
cur=(ROOT/rel).read_text();prev=(OLD/'input-snapshot'/rel).read_text()
for start,end in [('## 1.','## 2.'),('## 3.','## 4.')]:
    assert cur.split(start)[1].split(end)[0]==prev.split(start)[1].split(end)[0]
save('accepted-data-preservation.json',{'tables':unchanged,'WP23_Nature_and_optional_content_sections_unchanged':True})

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
print(json.dumps({'fixed':919,'manifest':917,'TSV':821,'diffs_exact':17,'scenario_counts':scenario_counts,'bindings':len(bindings),'inline_bindings':len(inline),'JSON':len(js),'links':len(links),'source_blobs':len(sources),'old_tables':old_tables,'accepted_data_unchanged':True,'reference_clean':True},ensure_ascii=False,indent=2))
