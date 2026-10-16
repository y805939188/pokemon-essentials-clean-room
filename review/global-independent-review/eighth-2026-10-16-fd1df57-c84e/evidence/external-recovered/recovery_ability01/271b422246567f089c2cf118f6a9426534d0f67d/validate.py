import pathlib,json,hashlib,re,subprocess,collections,datetime
P=pathlib.Path.cwd(); R=P.parent/'pokemon-essentials';ROOT='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e';T=P/ROOT/'tasks/recovery_ability01';OLD=P/ROOT/'tasks/external_ability_atomic_completion';checks=[]
def read(n):return json.loads((T/n).read_text())
def ck(name,condition,details=None):
 checks.append({'check':name,'pass':bool(condition),'detail':details});assert condition,(name,details)
def git(*a,cwd=P):return subprocess.check_output(['git',*a],cwd=cwd).decode().strip()
i=read('identities.json');f=read('forward-mapping.json');v=read('reverse-mapping.json');pr=read('progress.json');it=read('interfaces.json')
for key,x in i['inputs'].items():
 repo=P if x['repo']==P.name else R;raw=subprocess.check_output(['git','show',x['commit']+':'+x['path']],cwd=repo);head=f'blob {len(raw)}\0'.encode()+raw
 ck('input '+key,len(raw)==x['bytes'] and hashlib.sha256(raw).hexdigest()==x['sha256'] and hashlib.sha1(head).hexdigest()==x['git_blob'] and git('ls-tree',x['commit'],'--',x['path'],cwd=repo).split()[0]==x['mode'])
raw=(R/i['inputs']['PRIMARY']['path']).read_text();lines=raw.splitlines();regs=[]
for n,line in enumerate(lines,1):
 m=re.match(r'Battle::AbilityEffects::(\w+)\.(add|copy)\((.*)',line)
 if not m:continue
 fam,kind,tail=m.groups();syms=re.findall(r':([A-Z][A-Z0-9_]*)',tail);end=n
 if kind=='add':
  while lines[end-1]!=')':end+=1
 regs.append({'id':f'{fam}.{syms[0]}.{kind}','family':fam,'kind':kind,'identities':syms,'source_lines':[n,end]})
ck('independent literal registry count',len(regs)==263)
old=json.loads((OLD/'registry-units.json').read_text())['units'];ck('all263 exact source identities/ranges',regs==[{k:u[k] for k in regs[0]} for u in old])
ck('all263 current successor groups exact',[(r['id'],r['source_lines'],r['identities']) for r in regs]==[(r['id'],r['source_lines'],r['identities']) for r in f['groups']])
pairs={(u['family'],ab) for u in regs for ab in (u['identities'] if u['kind']=='add' else u['identities'][1:])};ck('expanded267 pairing',len(pairs)==267)
a=json.loads((OLD/'forward-mapping.json').read_text());m=json.loads((OLD/'manual-meanings.json').read_text());ma={x['id']:x for x in a['assertions']}
ck('all743 assertion records',len(ma)==743)
ck('manual239 exact dedup',all(m[g['id']]['assertions']==[ma[k]['meaning'] for k in g['assertion_ids']] for g in a['meaning_groups'] if g['kind']=='add'))
ck('all743 legacy IDs retained once',collections.Counter(k for g in f['groups'] for k in g['legacy_assertion_ids'])==collections.Counter(ma.keys()))
for g in a['meaning_groups']:
 for anchor in g.get('operative_anchors',[]):
  actual=(P/anchor['path']).read_text().splitlines()[anchor['line']-1]
  ck('old operative text '+g['id']+':'+str(anchor['line']),anchor['text']==actual)
for arow in a['assertions']:
 ck('old assertion anchor fields exact '+arow['id'],arow['source_lines']==next(g['source_lines'] for g in a['meaning_groups'] if g['id']==arow['source_unit']) and arow['operative_anchors']==next(g['operative_anchors'] for g in a['meaning_groups'] if g['id']==arow['source_unit']))
locs={r['id'] for r in v['rows']};expected=set()
for wp in ['WP48','WP49']:
 ls=(P/i['inputs'][wp]['path']).read_text().splitlines()
 expected|={f'{wp}.L{n:03}' for n,t in enumerate(ls,1) if t.strip()}
 for r in [x for x in v['rows'] if x['path_key']==wp]:ck('formal text identity '+r['id'],hashlib.sha256(ls[r['line']-1].encode()).hexdigest()==r['text_sha256'])
ck('actual all363 nonblank formal lines',locs==expected,(len(locs),len(expected),list(expected-locs)))
legacy=json.loads((OLD/'reverse-mapping.json').read_text())['rows'];fail=[]
for r in legacy:
 text='\n'.join((P/r['path']).read_text().splitlines()[r['lines'][0]-1:r['lines'][1]])
 if text!=r['text']:fail.append(r['id'])
ck('all334 old complete row texts exact',not fail,fail)
contract=json.loads(subprocess.check_output(['git','show','b924c4cec2ce2eab65964d7bb4879feb456b4f87:'+ROOT+'/tasks/external_ability_atomic_completion/next-dispatch.json'],cwd=P))
opened=contract['contracts'][0]['open_reverse_locator_ids'];ck('all contracted open reverse IDs handled',set(opened)<=locs,len(opened))
ck('all groups use existing operative nonidentity anchors',all(k in locs and not any(w['id']==k and w['disposition'] in ['IDENTITY_ONLY','STRUCTURE_ONLY'] for w in v['rows']) for g in f['groups'] for k in g['operative_locators']))
ck('all48 wrappers',len(f['dispatch'])==48 and len({x['family'] for x in f['dispatch']})==48)
for d in f['dispatch']:
 n=d['source_lines'][0];ck('actual wrapper '+d['family'],lines[n-1].startswith('  def self.trigger'+d['family']+'('))
ck('correct nil wrapper69-72',f['shared_wrapper_actual_lines']==[69,72] and 'new_ret.nil?' in lines[70])
sourceids=[c['id'] for g in f['groups']+f['dispatch'] for c in g['children']]+[c['id'] for c in f['shared_meanings']];revIds=[c['id'] for r in v['rows'] for c in r['children']]
ck('all source child IDs unique',len(sourceids)==len(set(sourceids)))
ck('all formal child IDs unique',len(revIds)==len(set(revIds)))
ck('1515 source/1283 formal frozen child count',len(sourceids)==1515 and len(revIds)==1283)
ck('count fields exact',pr['counts']['source_children_including_factored_common']==len(sourceids) and pr['counts']['formal_children']==len(revIds))
G={g['id'] for g in f['groups']};S={s['id']:s for s in json.loads(subprocess.check_output(['git','show','5c1e9a4679f66f4f1a6a8fb85c21335dd46eb0b1:'+ROOT+'/tasks/ability_cont_02/trigger-sites.json'],cwd=P))['sites']};ck('accepted91 census join exact',len(S)==91 and all(set(s['current_registry_unit_ids'])=={g['id'] for g in f['groups'] if g['family']==s['family']} for s in S.values()))
ck('all source concrete consumer lists exact',all(set(g['consumers_received_from_CONT02'])=={s['id'] for s in S.values() if s['family']==g['family']} for g in f['groups']))
allowed=set(G)|set(it['accepted_CONT02_reuse'])|set(it['finite_definitions'])|set(it['nonprimary_dispositions'])|{'PRIMARY_REGISTRY'}
bad=[]
for row in v['rows']:
 for ch in row['children']:
  for ref in row['support']:
   if ref.startswith('PRIMARY:'):
    if ref[8:] not in G:bad.append(ref)
   elif ref.startswith(('CAT1:','CAT2:','CONT03:')):continue
   elif ref not in allowed:bad.append(ref)
ck('all reverse supports resolve',not bad,sorted(set(bad)))
ck('no empty support except explicit scope/structure',all(r['support'] or r['disposition']=='SCOPE_PRESERVED' for r in v['rows'] for c in r['children']))
for route in it['nonprimary_dispositions'].values():ck('nonprimary operative route exists '+route['operative'],(P/route['operative']).exists())
ck('fixed formal and reference local identities',git('rev-parse','HEAD',cwd=R)==i['frozen']['R'] and git('rev-parse',i['frozen']['B8']+':deliverables/final-specification-set')==i['frozen']['formal_tree'] and git('rev-parse','HEAD:deliverables/final-specification-set')==i['frozen']['formal_tree'])
ck('reference working tree clean',git('status','--porcelain',cwd=R)=='')
ck('no tracked writes outside recovery',all(p.startswith(ROOT+'/tasks/recovery_ability01/') for p in git('diff','--name-only','HEAD').splitlines()))
ck('all execution remains not executed',pr['business_execution']=='NOT_EXECUTED' and not pr['update_started'] and pr['spawned_agents']==0)
summary={'schema':'gr8-recovery-ability01-validation/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Static identity/set/reference validation only; zero Ruby/model/game/native behavior execution. These checks do not independently certify semantics.','command':'python review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/recovery_ability01/validate.py (from repository root, with fixed Git objects available)' ,'checks_total':len(checks),'all_pass':True,'check_groups':['Every immutable input mode/blob/bytes/SHA','Independent literal263 registration IDs/ranges/267 pairs','239 manual meaning lists exactly factor all743 original records','All original forward anchors exactly bind to fully read text','All334 original reverse rows bind to complete text;363 actual nonblank lines have dispositions','All contracted open reverse locators included','48 wrappers/fallback identity and corrected69–72','1515 source/1283 formal child ID uniqueness and complete links','Accepted91 consumer census mechanically joined without new semantic credit','Protection and execution boundaries'],'failed_checks':[],'mechanical_pass_does_not_grant_semantic_PASS':True,'semantic_result':'Own primary/full formal reading and manually authored children complete within CONT01 finite scope. Two named nonprimary routes retain their existing owners; no global closure or new required judgment.','counts':pr['counts']}
(T/'validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n');print(json.dumps(summary,ensure_ascii=False))
