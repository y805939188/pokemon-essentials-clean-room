"""Reviewer-owned byte/text/literal-set checks only; no reference execution."""
from pathlib import Path
import json,hashlib,re,subprocess
from decimal import Decimal,localcontext
ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=ROOT/'review/wp58-wp62-wp38-review-2026-09-30'
PREV=ROOT/'review/wp55-wp57-closure-review-2026-09-29'
DEL=ROOT/'review/wp58-wp62-wp38-delivery-2026-09-29'
REF=ROOT/'reference/pokemon-essentials';S=REF/'Data/Scripts'
COMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def meta(p):
    b=p.read_bytes();return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def match(p,d):return p.is_file() and meta(p)=={k:d[k] for k in ['sha256','bytes']}
def save(name,d):(OUT/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
f=json.loads((OUT/'input-manifest.json').read_text())
checks={'fixed_inputs':len(f['inputs']),'changed_inputs':[x['path'] for x in f['inputs'] if not match(ROOT/x['path'],x)],
 'changed_snapshots':[x['path'] for x in f['inputs'] if not match(OUT/'input-snapshot'/x['path'],x)],'prior':[]}
for name in ['wp55-wp57-closure-review-2026-09-29','wp55-wp57-recheck-2026-09-29','wp55-wp57-review-2026-09-28',
 'wp52b-wp52c-wp54-recheck-2026-09-28','wp52b-wp52c-wp54-review-2026-09-28','wp50-wp51-wp52a-recheck-2026-09-28',
 'wp50-wp51-wp52a-review-2026-09-28','wp46-wp47-review-2026-09-27','wp42-wp48-wp49-recheck-2026-09-27']:
    d=ROOT/'review'/name;inp=json.loads((d/'input-manifest.json').read_text())['inputs'];arts=json.loads((d/'final-checks.json').read_text())['artifacts']
    checks['prior'].append({'review':name,'snapshots':len(inp),'changed_snapshots':[x['path'] for x in inp if not match(d/'input-snapshot'/x['path'],x)],
      'artifacts':len(arts),'changed_artifacts':[x['path'] for x in arts if not match(ROOT/x['path'],x)]})
diffs=[]
for p in sorted((DEL/'backfill-diffs').glob('*.diff')):
    ls=p.read_text().splitlines(keepends=True);base=ls[0][4:].strip();target=ls[1][4:].strip();src=(ROOT/base).read_text().splitlines(keepends=True);res=[];pos=0;i=2
    while i<len(ls):
        m=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',ls[i]);assert m,(p,i)
        start=int(m[1])-1 if int(m[1]) else 0;res+=src[pos:start];pos=start;i+=1
        while i<len(ls) and not ls[i].startswith('@@ '):
            l=ls[i];i+=1
            if l.startswith('\\'):continue
            if l[0] in ' -':assert src[pos]==l[1:],(p,pos);pos+=1
            if l[0] in ' +':res.append(l[1:])
    res+=src[pos:];diffs.append({'file':str(p.relative_to(ROOT)),**meta(p),'base':base,'target':target,'exact':''.join(res).encode()==(ROOT/target).read_bytes()})
save('diff-checks.json',diffs)
old_specs=[]
for p in [x['path'] for x in f['changes_from_previous'] if x['path'].startswith('specs/')]:
    rows=lambda q:[l for l in q.read_text().splitlines() if l.startswith('|')]
    old_specs.append({'path':p,'all_tables_unchanged':rows(ROOT/p)==rows(PREV/'input-snapshot'/p)})
save('backfill-checks.json',{'old_spec_tables':old_specs,'note':'Manual diff confirms status/identity updates; current numeric tables and all 78 scenario rows unchanged. Backfill-response current identity table has two stale records; see report maintenance.'})

specs=['specs/combat/wp58-battle-recording-and-playback.md','specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md','specs/pokemon-rules/wp38-capture-and-receiving.md']
inline=[];scenarios={}
for p in specs:
    txt=(ROOT/p).read_text();scenarios[p]=len(re.findall(r'^\| W\d+ \|',txt,re.M))
    for m in re.finditer(r'\]\(([^)]+\.md)\)（[^`]*`([0-9a-f]{64})`，([\d,]+)字节',txt):
        path,h,n=m.groups();rec={'sha256':h,'bytes':int(n.replace(',',''))};inline.append({'file':p,'target':path,**rec,'matches':match((ROOT/p).parent/path,rec)})
bd=json.loads((DEL/'boundary-checks.json').read_text());bindings=[{**x,'matches':match(ROOT/x['sender'],x)} for x in bd['bindings']]
selfd=json.loads((DEL/'self-checks.json').read_text());embedded=[]
for p,d in selfd['artifacts'].items():embedded.append({'path':p,'kind':'artifacts','matches':match(ROOT/p,d)})
for d in selfd['packages']:embedded.append({'path':d['file'],'kind':'packages','matches':match(ROOT/d['file'],d)})
jsons=[x['path'] for x in f['manifest_rows'] if x['path'].endswith('.json')];badjson=[]
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
save('integrity-checks.json',{'scenario_counts':scenarios,'inline_bindings':inline,'boundary_bindings':bindings,'current_self_identities':embedded,'registered_JSON':len(jsons),'bad_JSON':badjson,'spec_matrix_links':len(links),'bad_links':badlinks})

# Literal inventories only. These counts do not evaluate reference handlers.
reg=(S/'011_Battle/008_Other battle types/005_RecordedBattle.rb').read_text()
props=re.findall(r'@properties\["(\w+)"\]\s*=',reg.split('module RecordedBattlePlaybackModule')[0])
balls=(S/'011_Battle/007_Other battle code/010_Battle_PokeBallEffects.rb').read_text()
regs=re.findall(r'Battle::PokeBallEffects::(\w+)\.add\(:(\w+)',balls)
ball_data=[]
for m in re.finditer(r'^\[([^]]+)\]\s*$([\s\S]*?)(?=^\[|\Z)',(REF/'PBS/items.txt').read_text(),re.M):
    flag=re.search(r'^Flags\s*=\s*(.+)$',m[2],re.M)
    if flag and any(x.strip() in ['PokeBall','SnagBall'] for x in flag[1].split(',')):ball_data.append(m[1])
calls=[]
for p in (S/'011_Battle').rglob('*.rb'):
    for n,l in enumerate(p.read_text().splitlines(),1):
        if l.lstrip().startswith('#') or re.search(r'\bdef\s+(?:self\.)?pbRandom',l):continue
        if re.search(r'\bpbRandom\(',l):calls.append({'path':str(p.relative_to(REF)),'line':n,'Safari':'001_SafariBattle.rb' in p.name})
regional=(REF/'PBS/regional_dexes.txt').read_text()
coverage={'properties':props,'properties_count':len(props),'poke_ball_registrations':regs,'registered_ball_count':len({v for _,v in regs}),
 'ball_data_count':len(ball_data),'ball_data':ball_data,'unregistered_balls':sorted(set(ball_data)-{v for _,v in regs}),
 'random_call_lines':len(calls),'random_nonSafari_lines':sum(not x['Safari'] for x in calls),'random_calls':calls,
 'regional_sections':re.findall(r'^\[(\d+)\]',regional,re.M),'regional_lines':len(regional.splitlines()),
 'note':'Raw inventories only; no proof of reachability, capacity, runtime execution or behavioral completeness.'}
save('coverage-checks.json',coverage)

# Independent fixed arithmetic, not a capture evaluator or reference expression runner.
const=[]
with localcontext() as ctx:
    ctx.prec=70
    for n,expected in [(1,23187),(15,38527),(22,41395),(90,53910),(112,56167)]:
        y=Decimal(65536)/(Decimal(255)/Decimal(n))**(Decimal(3)/Decimal(16))
        const.append({'x':n,'y_decimal':str(y),'floor':int(y),'expected':expected,'matches':int(y)==expected})
save('constant-checks.json',{'method':'Independent fixed constants only; no conditional evaluator/reference code execution.',
 'shake_thresholds':const,'status_rounding_counterexample':{'raw_before_status':'(600-2)*45/600 = 44.85','multiply_then_floor':int(Decimal('44.85')*Decimal('2.5')),'wrong_early_floor':int(Decimal(44)*Decimal('2.5'))},
 'critical_sample':{'x':15,'modifier':10,'c':15*10//12},'warning':'W07 gives only modified catch rate; y is not determined without HP/status or explicit x.'})

sources={d['path'] for d in selfd['source_identities']}
extras=['Data/Scripts/011_Battle/007_Other battle code/010_Battle_PokeBallEffects.rb','Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb',
 'Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb','Data/Scripts/010_Data/002_PBS data/008_Species.rb','Data/Scripts/010_Data/002_PBS data/013_Encounter.rb',
 'Data/Scripts/004_Game classes/012_Game_Stats.rb','Data/Scripts/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb',
 'Data/Scripts/011_Battle/003_Move/011_MoveEffects_Items.rb','Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb',
 'Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb','Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/005_Challenge_BattleRules.rb','PBS/pokemon_forms.txt']
extras+=['Data/Scripts/011_Battle/002_Battler/004_Battler_Statuses.rb','Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb']
sources.update(extras);src=[]
for rel in sorted(sources):
    p=REF/rel;blob=subprocess.run(['git','--no-optional-locks','-C',str(REF),'show',COMMIT+':'+rel],capture_output=True,check=True).stdout
    src.append({'path':str(p.relative_to(ROOT)),**meta(p),'commit_blob_equal':blob==p.read_bytes(),'in_delivery_source_ledger':rel not in set(extras) or rel in {x['path'] for x in selfd['source_identities']}})
save('source-checks.json',{'commit':COMMIT,'paths':src,'note':'Commit blob verification is separate from actual read scope. Fresh ranges and inherited boundaries are recorded in review-notes.json. No reference code executed.'})
checks['reference_head']=subprocess.run(['git','--no-optional-locks','-C',str(REF),'rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip()
checks['reference_status']=subprocess.run(['git','--no-optional-locks','-C',str(REF),'status','--porcelain'],capture_output=True,text=True,check=True).stdout
save('identity-checks.json',checks)
print(json.dumps({'fixed':checks['fixed_inputs'],'changed':checks['changed_inputs'],'prior':checks['prior'],'diffs':len(diffs),'bad_diffs':[d['file'] for d in diffs if not d['exact']],
 'old_tables':old_specs,'scenarios':scenarios,'inline':len(inline),'bad_inline':[x for x in inline if not x['matches']],'bindings':len(bindings),'bad_bindings':[x for x in bindings if not x['matches']],
 'bad_self':[x for x in embedded if not x['matches']],'json':len(jsons),'bad_json':badjson,'links':len(links),'bad_links':badlinks,
 'coverage_counts':{'properties':len(props),'balls':len(ball_data),'ball_registrations':len(regs),'random_calls':len(calls),'nonSafari':sum(not x['Safari'] for x in calls),'regional_lines':len(regional.splitlines())},
 'sources':len(src),'bad_source':[x['path'] for x in src if not x['commit_blob_equal']]},ensure_ascii=False,indent=2))
