"""Reviewer-owned hashes, literal tables, sets and in-memory diff reconstruction.
No reference code, extractor check script, game, generator or interpreter is executed.
"""
from pathlib import Path
import json,hashlib,re,subprocess
ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=ROOT/'review/wp55-wp57-review-2026-09-28'
PREV=ROOT/'review/wp52b-wp52c-wp54-recheck-2026-09-28'
DEL=ROOT/'review/wp55-wp57-delivery-2026-09-28'
REF=ROOT/'reference/pokemon-essentials'
COMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def meta(p):
    b=p.read_bytes();return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def match(p,x):
    return p.exists() and meta(p)=={k:x[k] for k in ['sha256','bytes']}
def save(n,d):
    (OUT/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
fixed=json.loads((OUT/'input-manifest.json').read_text())
identity={'fixed_inputs':len(fixed['inputs']),
 'changed_inputs':[x['path'] for x in fixed['inputs'] if not match(ROOT/x['path'],x)],
 'changed_snapshots':[x['path'] for x in fixed['inputs'] if not match(OUT/'input-snapshot'/x['path'],x)],'prior':[]}
for name in ['wp52b-wp52c-wp54-recheck-2026-09-28','wp52b-wp52c-wp54-review-2026-09-28',
 'wp50-wp51-wp52a-recheck-2026-09-28','wp50-wp51-wp52a-review-2026-09-28','wp46-wp47-review-2026-09-27','wp42-wp48-wp49-recheck-2026-09-27']:
    d=ROOT/'review'/name;inputs=json.loads((d/'input-manifest.json').read_text())['inputs'];arts=json.loads((d/'final-checks.json').read_text())['artifacts']
    identity['prior'].append({'review':name,'snapshots':len(inputs),
      'changed_snapshots':[x['path'] for x in inputs if not match(d/'input-snapshot'/x['path'],x)],
      'artifacts':len(arts),'changed_artifacts':[x['path'] for x in arts if not match(ROOT/x['path'],x)]})
diffs=[]
for p in sorted((DEL/'backfill-diffs').glob('*.diff')):
    lines=p.read_text().splitlines(keepends=True);base=lines[0][4:].strip();target=lines[1][4:].strip()
    src=(ROOT/base).read_text().splitlines(keepends=True);out=[];pos=0;h=2
    while h<len(lines):
        m=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',lines[h]);assert m,(p,h)
        start=int(m[1])-1 if int(m[1]) else 0;out+=src[pos:start];pos=start;h+=1
        while h<len(lines) and not lines[h].startswith('@@ '):
            line=lines[h];h+=1
            if line.startswith('\\'):continue
            if line[0] in ' -':assert src[pos]==line[1:],(p,pos);pos+=1
            if line[0] in ' +':out.append(line[1:])
    out+=src[pos:]
    diffs.append({'path':str(p.relative_to(ROOT)),**meta(p),'baseline':base,'target':target,'reconstructs_current':''.join(out).encode()==(ROOT/target).read_bytes()})
save('diff-checks.json',diffs)
old_del=ROOT/'review/wp52b-wp52c-wp54-delivery-2026-09-28'
old_self=json.loads((old_del/'self-checks.json').read_text());embedded=[];vector_diffs=[]
for path,x in old_self['artifacts'].items():embedded.append({'path':path,'matches':match(ROOT/path,x)})
for package in old_self['packages']:
    embedded.append({'path':package['file'],'package':package['package'],'matches':match(ROOT/package['file'],package)})
    text=(ROOT/package['file']).read_text();rows={}
    for line in text.splitlines():
        if re.match(r'^\| [BCQ]\d+[a-z]? \|',line):
            cols=[v.strip() for v in line.strip('|').split('|')];rows[cols[0]]={'input':cols[1],'expected':cols[2]}
    for v in package['vectors']:
        if rows.get(v['id'])!={k:v[k] for k in ['input','expected']}:vector_diffs.append({'package':package['package'],'id':v['id']})
table_protection=[]
for path in [x['path'] for x in fixed['changes_from_previous'] if x['path'].startswith('specs/')]:
    a=(PREV/'input-snapshot'/path).read_text();b=(ROOT/path).read_text()
    rows=lambda text:[l for l in text.splitlines() if l.startswith('|')]
    table_protection.append({'path':path,'tables_unchanged':rows(a)==rows(b)})
save('backfill-checks.json',{'C02_current_artifacts_packages':embedded,'C02_vector_differences':vector_diffs,'old_spec_tables':table_protection})

links=[];badlinks=[]
for p in list((ROOT/'specs').rglob('*.md'))+[ROOT/'planning/feature-matrix.md']:
    for d in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        d=d.strip('<>')
        if re.match(r'\w+://',d) or d.startswith('#'):continue
        d=re.sub(r':\d+$','',d.split('#')[0])
        if not d:continue
        item={'file':str(p.relative_to(ROOT)),'target':d,'exists':(p.parent/d).exists()};links.append(item)
        if not item['exists']:badlinks.append(item)
jsons=[x['path'] for x in fixed['manifest_rows'] if x['path'].endswith('.json')];badjson=[]
for p in jsons:
    try:json.loads((ROOT/p).read_text())
    except Exception as e:badjson.append({'path':p,'error':str(e)})
boundary=json.loads((DEL/'boundary-checks.json').read_text());bindings=[]
for x in boundary['bindings']:
    bindings.append({**x,'matches':match(ROOT/x['sender'],x)})
save('integrity-checks.json',{'manifest_rows':fixed['manifest_rows_count'],'tsv_rows':fixed['delivery_rows_count'],
 'registered_json':len(jsons),'bad_json':badjson,'spec_matrix_links':len(links),'bad_links':badlinks,'delivery_bindings':bindings})

S=REF/'Data/Scripts';coverage={}
pal=(S/'011_Battle/008_Other battle types/003_BattlePalaceBattle.rb').read_text()
src_tables=[]
for name in ['BattlePalaceUsualTable','BattlePalacePinchTable']:
    chunk=re.search(r'@@'+name+r' = \{(.*?)\n  \}',pal,re.S)[1]
    src_tables.append({k:[int(v) for v in nums.split(',')] for k,nums in re.findall(r':(\w+)\s*=>\s*\[([\d, ]+)\]',chunk)})
doc=(ROOT/'specs/combat/wp56-palace-and-arena-variants.md').read_text()
tab=[{},{}]
for key,first,second in re.findall(r'^\| ([A-Z]+) \| ([\d, ]+) \| ([\d, ]+) \|$',doc,re.M):
    tab[0][key]=[int(v) for v in first.split(',')];tab[1][key]=[int(v) for v in second.split(',')]
coverage['Palace_raw_tables']={'rows':[len(t) for t in src_tables],'exact':tab==src_tables,'row_sums_100':all(sum(v)==100 for t in src_tables for v in t.values()),'note':'Raw values match; actual selection thresholds do NOT equal a simple A,D,S partition. See WP56-R01.'}
ch=(S/'018_Alternate battle modes/001_Battle Frontier/003_Challenge_ChooseFoes.rb').read_text()
tr=[list(map(int,m)) for m in re.findall(r'^\s*\[\s*(\d+),\s*(\d+),\s*(\d+)\]',ch[:ch.index('def pbGenerateBattleTrainer')],re.M)]
d55=(ROOT/'specs/combat/wp55-facility-session-and-restoration.md').read_text()
dtr=[list(map(int,m)) for m in re.findall(r'^\| (\d+) \| (\d+) \| (\d+) \|$',d55,re.M)]
coverage['trainer_table']={'rows':len(tr),'exact':tr==dtr}
factory=ch[ch.index('def pbBattleFactoryPokemon'):]
pairs=[list(map(int,m)) for m in re.findall(r'^\s*\[\s*(\d+),\s*(\d+)\]',factory,re.M)]
d57=(ROOT/'specs/creature-rpg/wp57-factory-rentals-and-swaps.md').read_text()
docpairs=[list(map(int,m)) for m in re.findall(r'^\| \d[^|]*\| (\d+)–(\d+) \| (\d+)–(\d+) \|$',d57,re.M)]
coverage['factory_domains']={'rows':len(docpairs),'exact':all(x[:2]==pairs[8+n] and x[2:]==pairs[n] for n,x in enumerate(docpairs)),'note':'Inclusive upper template 881 is the out-of-range endpoint at actual length N; matching numbers alone is not behavioral acceptance.'}
coverage['scenario_rows']={}
for path in ['specs/combat/wp55-facility-session-and-restoration.md','specs/combat/wp56-palace-and-arena-variants.md','specs/creature-rpg/wp57-factory-rentals-and-swaps.md']:
    coverage['scenario_rows'][path]=len(re.findall(r'^\| [WPF]\d+ \|',(ROOT/path).read_text(),re.M))
save('coverage-checks.json',coverage)

data=json.loads((DEL/'self-checks.json').read_text());sources={x['path'] for x in data['source_identities']}
extras=['001_Technical/002_RubyUtilities.rb','003_Game processing/001_StartGame.rb','014_Pokemon/001_Pokemon.rb',
 '015_Trainers and player/001_Trainer.rb','011_Battle/002_Battler/002_Battler_Initialize.rb','011_Battle/002_Battler/001_Battle_Battler.rb',
 '010_Data/001_Hardcoded data/010_Status.rb','012_Overworld/002_Overworld_Metadata.rb','002_Save data/004_Game_SaveValues.rb']
extras+=['011_Battle/001_Battle/005_Battle_ActionSwitching.rb','014_Pokemon/005_Pokemon_Owner.rb']
sources|={str((S/p).relative_to(ROOT)) for p in extras};sourcechecks=[]
for p in sorted(sources):
    q=ROOT/p;rel=str(q.relative_to(REF));blob=subprocess.run(['git','--no-optional-locks','-C',str(REF),'show',COMMIT+':'+rel],capture_output=True,check=True).stdout
    sourcechecks.append({'path':p,**meta(q),'commit_blob_equal':blob==q.read_bytes()})
save('source-checks.json',{'commit':COMMIT,'paths':sourcechecks,'fresh_scope_note':'See review-notes.json; 7 main behavior files read in full; remaining paths are bounded consumers, literal data and integrity checks. No execution.'})
identity['reference_head']=subprocess.run(['git','--no-optional-locks','-C',str(REF),'rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip()
identity['reference_status']=subprocess.run(['git','--no-optional-locks','-C',str(REF),'status','--porcelain'],capture_output=True,text=True,check=True).stdout
save('identity-checks.json',identity)
print(json.dumps({'fixed':identity['fixed_inputs'],'changed_inputs':identity['changed_inputs'],'prior':identity['prior'],'diffs':len(diffs),'diff_mismatch':[x for x in diffs if not x['reconstructs_current']],
 'C02_mismatch':[x for x in embedded if not x['matches']],'C02_vector_mismatch':vector_diffs,'old_tables':table_protection,
 'bindings':len(bindings),'bad_bindings':[x for x in bindings if not x['matches']],'JSON':len(jsons),'bad_json':badjson,'links':len(links),'bad_links':badlinks,
 'coverage':coverage,'sources':len(sourcechecks),'source_mismatches':[x['path'] for x in sourcechecks if not x['commit_blob_equal']]},ensure_ascii=False,indent=2))
