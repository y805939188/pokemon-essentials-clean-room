"""Reviewer-owned text, literal-set, byte and diff audit. Never loads reference code.
Only writes its own review directory; no extractor scripts are imported or run.
"""
from pathlib import Path
import collections, hashlib, json, re, subprocess

ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT = ROOT / 'review/wp52b-wp52c-wp54-review-2026-09-28'
REF = ROOT / 'reference/pokemon-essentials'
COMMIT = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
DELIVERY = ROOT / 'review/wp52b-wp52c-wp54-delivery-2026-09-28'
frozen = json.loads((OUT/'input-manifest.json').read_text())

def meta(p):
    b = p.read_bytes()
    return {'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b)}

def save(name, obj):
    (OUT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')

def check_meta(p, d):
    return p.is_file() and all(meta(p)[k] == d[k] for k in ('sha256','bytes'))

fixed = frozen['inputs']
identity = {'method':'own read-only byte/text audit; no reference execution',
 'current_fixed_count':len(fixed),
 'current_changed':[d['path'] for d in fixed if not check_meta(ROOT/d['path'],d)],
 'current_snapshot_changed':[d['path'] for d in fixed if not check_meta(OUT/'input-snapshot'/d['path'],d)],
 'prior':[]}
for name in ['wp50-wp51-wp52a-recheck-2026-09-28','wp50-wp51-wp52a-review-2026-09-28',
             'wp46-wp47-review-2026-09-27','wp42-wp48-wp49-recheck-2026-09-27']:
    old = ROOT/'review'/name
    inp = json.loads((old/'input-manifest.json').read_text())['inputs']
    final = json.loads((old/'final-checks.json').read_text())
    artifacts = final['artifacts']
    identity['prior'].append({'review':name,'inputs':len(inp),
      'snapshot_changed':[d['path'] for d in inp if not check_meta(old/'input-snapshot'/d['path'],d)],
      'artifacts':len(artifacts),'artifact_changed':[d['path'] for d in artifacts if not check_meta(ROOT/d['path'],d)]})

# In-memory reconstruction only; never applies the supplied patches.
diff_results=[]
for p in sorted((DELIVERY/'backfill-diffs').glob('*.diff')):
    lines=p.read_text().splitlines(keepends=True)
    base=lines[0][4:].strip(); target=lines[1][4:].strip()
    src=(ROOT/base).read_text().splitlines(keepends=True)
    result=[]; pos=0; h=2
    while h<len(lines):
        m=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',lines[h])
        assert m, (p,h,lines[h])
        start=int(m[1])-1 if int(m[1]) else 0
        result+=src[pos:start];pos=start;h+=1
        while h<len(lines) and not lines[h].startswith('@@ '):
            line=lines[h];h+=1
            if line.startswith('\\'): continue
            if line[0] in ' -':
                assert src[pos]==line[1:],(p,pos)
                pos+=1
            if line[0] in ' +': result.append(line[1:])
    result+=src[pos:]
    diff_results.append({'path':str(p.relative_to(ROOT)), **meta(p), 'baseline':base,'target':target,
                         'reconstructs_current':''.join(result).encode()==(ROOT/target).read_bytes()})
save('diff-checks.json',diff_results)

# Compare the new coverage tables with registration names/locations and copy bindings.
battle=REF/'Data/Scripts/011_Battle'
entries=[]; bindings={}; missing=[]; statements=0; addifs=0
for p in sorted(list((battle/'005_AI').glob('*.rb'))+list((battle/'006_AI MoveEffects').glob('*.rb'))):
    s=p.read_text(); rel=str(p.relative_to(battle))
    addifs+=len(re.findall(r'Battle::AI::Handlers::\w+\.addIf\(',s))
    pattern=r'Battle::AI::Handlers::(\w+)\.(add|copy)\(\s*((?:"[^"]+"|:\w+)(?:\s*,\s*(?:"[^"]+"|:\w+))*)'
    for m in re.finditer(pattern,s):
        family,op,args=m.groups();statements+=1
        names=[a or b for a,b in re.findall(r'"([^"]+)"|:(\w+)',args)]
        line=s[:m.start()].count('\n')+1
        source=names[0] if op=='copy' else None
        origin=f'{rel}:{line}'
        destinations=names[1:] if op=='copy' else names
        for key in destinations:
            entries.append({'file':rel,'line':line,'family':family,'id':key,'operation':op,'copy_source':source})
            if op=='add': bindings[family,key]=origin
            elif (family,source) in bindings: bindings[family,key]=bindings[family,source]
            else: missing.append({'family':family,'source':source,'destination':key,'location':origin})
source_index={(x['file'],x['line'],x['family'],x['id']):x for x in entries}
coverage={'add_copy_statements':statements,'addIf_statements':addifs,'occurrences':len(entries),
 'distinct_occurrence_keys':len({(x['family'],x['id']) for x in entries}),
 'effective_direct_keys':len(bindings),'missing_copy_sources':missing,'appendices':[]}
for name in ['wp52-b-effect-coverage.md','wp52-c-item-control-coverage-and-data.md']:
    table=[]; errors=[]
    for n,line in enumerate((ROOT/'specs/combat'/name).read_text().splitlines(),1):
        m=re.match(r'\| (.+\.rb):(\d+) \| (\w+) / `([^`]+)` \| ([^|]+) \| ([^|]+) \| ([^|]*) \|',line)
        if not m: continue
        file,ln,family,key,op,contract,final=m.groups();ln=int(ln)
        row=source_index.get((file,ln,family,key));table.append((family,key))
        expected_op='add' if row and row['operation']=='add' else 'copy←'+(row['copy_source'] if row else '?')
        expected_final=bindings.get((family,key))
        if not row or not op.strip().startswith(expected_op): errors.append({'line':n,'reason':'location/operation'})
        if expected_final and not final.strip().startswith(expected_final): errors.append({'line':n,'reason':'final binding','expected':expected_final,'actual':final})
        if not expected_final and not any(x in final for x in ['空','无','未']): errors.append({'line':n,'reason':'absent binding','actual':final})
    coverage['appendices'].append({'file':name,'occurrences':len(table),'distinct':len(set(table)),
       'effective':len({k for k in table if k in bindings}),'errors':errors})

u=(battle/'005_AI/008_AI_Utilities.rb').read_text()
base=u[u.index('BASE_ITEM_RATINGS = {'):u.index('\n  }',u.index('BASE_ITEM_RATINGS = {'))]
base=re.sub(r'#.*','',base)
source_ratings={int(v):re.findall(r':(\w+)',items) for v,items in re.findall(r'(-?\d+)\s*=>\s*\[([^]]+)\]',base,re.S)}
c=(ROOT/'specs/combat/wp52-c-item-control-coverage-and-data.md').read_text()
table_ratings={int(v):items.split(', ') for v,items in re.findall(r'^\| (-?\d+) \| ([A-Z0-9_, ]+) \|$',c,re.M)}
coverage['base_item_rating']={'groups':len(source_ratings),'identities':sum(map(len,source_ratings.values())),
 'exact_ordered_match':source_ratings==table_ratings}
condition_tables={}
for group in ['type_boosting_items','gems']:
    region=u[u.index('ItemRanking.addIf(:'+group):]
    if group=='type_boosting_items':
        chunk=re.search(r'boosters = \{(.*?)\n    \}',region,re.S).group(1)
        data=[(item,typ) for typ,items in re.findall(r':(\w+)\s*=>\s*\[([^]]+)\]',chunk) for item in re.findall(r':(\w+)',items)]
    else:
        chunk=re.search(r'boosted_type = \{(.*?)\n    \}',region,re.S).group(1)
        data=re.findall(r':(\w+)\s*=>\s*:(\w+)',chunk)
    actual=re.findall(r'^\| '+group+r' \| (\w+) \| (\w+) \|$',c,re.M)
    condition_tables[group]={'identities':len(data),'exact_ordered_match':data==actual}
coverage['condition_tables']=condition_tables
supplied=json.loads((DELIVERY/'self-checks.json').read_text())
oldledger=supplied['ai_registration_ledger']['entries']
source_tuples={(e['file'],e['line'],e['family'],e['id'],e['operation'],e['copy_source']) for e in entries}
supplied_tuples={(e['file'],e['line'],e['family'],e['id'],e['operation'],e['copy_source']) for e in oldledger}
coverage['delivery_ledger_exact_match']=source_tuples==supplied_tuples
coverage['delivery_ledger_ownership_counts']=dict(collections.Counter(e['owner'] for e in oldledger))

# Definitions and named clause keys are literal sets, not invocation.
rules=REF/'Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules'
rule_ids=[]
for p in sorted(rules.glob('*.rb')):
    for n,line in enumerate(p.read_text().splitlines(),1):
        m=re.match(r'^(?:class|module) (\w+)',line)
        if m:rule_ids.append((p.name,n,m[1]))
q=(ROOT/'specs/combat/wp54-entry-rules-and-cup-data.md').read_text()
qrows=[(f,int(n),name) for f,n,name in re.findall(r'^\| (\S+\.rb):(\d+) \| `(\w+)` \|',q,re.M)]
factories=(rules/'001_Challenge_ChallengeRules.rb').read_text().split('=begin')[0]
factory_ids=re.findall(r'^def (pb\w+CupRules|pbBattle\w+Rules)\b',factories,re.M)
factory_table=re.findall(r'^\| (pb\w+Rules) \|',q,re.M)
clause_text=(battle/'007_Other battle code/006_Battle_Clauses.rb').read_text()
clause_keys=set(re.findall(r'rules\["(\w+)"\]',clause_text))
clause_keys |= set(re.findall(r'rules\["(\w+)"\]',(rules/'005_Challenge_BattleRules.rb').read_text()))
clause_rows=set(re.findall(r'^\| (\w+clause|suddendeath) \|',q,re.M))
coverage['WP54']={'definition_identities':len(rule_ids),'definition_table_exact':rule_ids==qrows,
 'active_factories':len(factory_ids),'factory_identity_order_exact':factory_ids==factory_table,
 'clause_keys':sorted(clause_keys),'clause_keys_exact':clause_keys==clause_rows,
 'profile_behavior':'Reviewer manually read active factory bodies and direct samples; identities alone do not establish behavior.'}
save('coverage-checks.json',coverage)

main_paths=['specs/combat/wp52-b-field-damage-healing-and-target-evaluation.md',
 'specs/combat/wp52-c-items-calling-and-control-evaluation.md',
 'specs/combat/wp54-entry-eligibility-level-adjustment-and-clauses.md']
scenarios=[]
for p in main_paths:
    rows=[l for l in (ROOT/p).read_text().splitlines() if re.match(r'^\| [BCQ]\d{2} \|',l)]
    scenarios.append({'file':p,'count':len(rows),'ids':[r.split('|')[1].strip() for r in rows]})
old_scenarios=[]
for p in ['specs/pokemon-rules/wp50-held-item-triggers-and-consumption.md',
 'specs/combat/wp51-ai-action-selection-and-skill.md',
 'specs/combat/wp52-a-generic-numerical-and-status-evaluation.md']:
    prior=ROOT/'review/wp50-wp51-wp52a-recheck-2026-09-28/input-snapshot'/p
    getrows=lambda text:[l for l in text.splitlines() if re.match(r'^\| [A-Z]\d{2} \|',l)]
    before=getrows(prior.read_text());after=getrows((ROOT/p).read_text())
    old_scenarios.append({'file':p,'count':len(after),'identical':before==after})
save('scenario-index.json',{'new':scenarios,'new_total':sum(d['count'] for d in scenarios),
 'prior':old_scenarios,'method':'text identities/counts only; semantic finding B04 is separately recorded'})

source_paths={d['path'] for d in supplied['source_identities']}
source_paths |= {str(p.relative_to(ROOT)) for p in (battle/'005_AI').glob('*.rb')}
source_paths |= {str(p.relative_to(ROOT)) for p in (battle/'006_AI MoveEffects').glob('*.rb')}
source_paths |= {'reference/pokemon-essentials/Data/Scripts/011_Battle/003_Move/001_Battle_Move.rb',
 'reference/pokemon-essentials/Data/Scripts/014_Pokemon/004_Pokemon_Move.rb',
 'reference/pokemon-essentials/Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb'}
sources=[]
for p in sorted(source_paths):
    rel=str((ROOT/p).relative_to(REF))
    b=subprocess.run(['git','--no-optional-locks','-C',str(REF),'show',COMMIT+':'+rel],capture_output=True,check=True).stdout
    sources.append({'path':p,**meta(ROOT/p),'commit_blob_equal':b==(ROOT/p).read_bytes()})
save('source-checks.json',{'commit':COMMIT,'paths':sources,'count':len(sources),
 'note':'Byte equality is separate from fresh read scope. Fresh ranges and inherited scope are recorded in review-notes.json. No source code execution.'})

# JSON and local links are syntax/existence checks, not behavior validation.
json_paths=[d['path'] for d in frozen['manifest_rows'] if d['path'].endswith('.json')]
bad_json=[]
for p in json_paths:
    try: json.loads((ROOT/p).read_text())
    except Exception as e: bad_json.append({'path':p,'error':str(e)})
link_files=[ROOT/'planning/feature-matrix.md']
link_files+=sorted((ROOT/'specs').rglob('*.md'))
links=[];bad_links=[]
for p in link_files:
    for match in re.finditer(r'\]\(([^)]+)\)',p.read_text()):
        dest=match[1].strip('<>')
        if re.match(r'\w+://',dest) or dest.startswith('#'): continue
        dest=dest.split('#')[0]
        if not dest:continue
        dest=re.sub(r':\d+$','',dest)
        q=p.parent/dest
        item={'file':str(p.relative_to(ROOT)),'target':dest,'exists':q.exists()}
        links.append(item)
        if not item['exists']:bad_links.append(item)
identity.update({'registered_json_count':len(json_paths),'bad_json':bad_json,
 'relative_links_scope':'all current specs and feature-matrix','relative_links_count':len(links),'bad_links':bad_links,
 'reference_head':subprocess.run(['git','--no-optional-locks','-C',str(REF),'rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip(),
 'reference_status':subprocess.run(['git','--no-optional-locks','-C',str(REF),'status','--porcelain'],capture_output=True,text=True,check=True).stdout})
save('identity-checks.json',identity)
print(json.dumps({'identity':{k:v for k,v in identity.items() if k!='prior'},'prior':identity['prior'],
 'diffs':len(diff_results),'bad_diffs':[x for x in diff_results if not x['reconstructs_current']], 'coverage':coverage},ensure_ascii=False,indent=2))
