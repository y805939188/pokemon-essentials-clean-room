import json,re,subprocess,pathlib,hashlib
P=pathlib.Path('/workspace/pokemon-essentials-clean-room'); R=pathlib.Path('/workspace/b05-reference')
C='1914cd379bcb7c8b6feb13dc3e872b7ded27d9a4'; B='0a12de641542f9a59909d2a950c1de8df17ca09d'; O='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
def g(*args):return subprocess.check_output(['git','-C',str(P),*args],text=True)
def data(p):return p.read_text(encoding='utf-8-sig')
def sections(p):
 out={}; cur=None
 for line in data(p).splitlines():
  s=line.strip()
  if s.startswith('[') and s.endswith(']'):cur=s[1:-1];out[cur]={}
  elif cur and '=' in s and not s.startswith('#'):
   k,v=s.split('=',1);out[cur][k.strip()]=v.strip()
 return out
def rows(p, start=None, end=None):
 text=data(p)
 if start is not None:text=text.split(start,1)[1].split(end,1)[0]
 return [[c.strip() for c in s.split('|')[1:-1]] for s in text.splitlines() if s.startswith('|')]
def equal_tables(actual,expected):
 return {'rows':len(actual),'expected_rows':len(expected),'missing':sorted(set(expected)-set(actual)),'extra':sorted(set(actual)-set(expected)),'differences':[{'key':str(k),'actual':actual[k],'expected':v} for k,v in expected.items() if k in actual and actual[k]!=v]}
res={'candidate':C,'fix_base':B,'review_base':'e1e01bb18d824931e54f182dd61af5a9f908ba85','original_report':O,'reference':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','method':'Read-only text fields and Markdown rows compared; independent fixed arithmetic. No Ruby execution, source conversion, data loading, compilation or behavioral simulation.'}
forms=sections(R/'PBS/pokemon_forms.txt'); items=sections(R/'PBS/items.txt')
mega={k:[v.get('MegaStone',v.get('MegaMove')),list(map(int,v['BaseStats'].split(',')))] for k,v in forms.items() if 'MegaStone' in v or 'MegaMove' in v}
for name,pre in [('final','deliverables/final-specification-set/pokemon-rules/'),('original','specs/pokemon-rules/')]:
 actual={','.join(x[:2]):[re.findall(r'[A-Z][A-Z0-9_]+',x[2])[-1],list(map(int,x[3].split('／')))] for x in rows(P/(pre+'wp22-transformation-data.md')) if len(x)>=4 and re.fullmatch(r'[A-Z]+',x[0]) and re.fullmatch(r'\d+',x[1])}
 res['mega_'+name]=equal_tables(actual,mega)
res['mega_stones_all_registered']=all(v[0] in items for k,v in mega.items() if 'MegaStone' in forms[k])
res['mega_flag_identity_set_matches']=set(k for k,v in items.items() if 'MegaStone' in v.get('Flags','').split(','))==set(v['MegaStone'] for v in forms.values() if 'MegaStone' in v)
shadow=sections(R/'PBS/Shadow Pokémon backup/shadow_pokemon.txt'); shadow_expect={k:[int(v.get('GaugeSize','4000')),v['Moves'].split(',')] for k,v in shadow.items()}
for name,pre in [('final','deliverables/final-specification-set/pokemon-rules/'),('original','specs/pokemon-rules/')]:
 actual={x[0]:[int(x[1]),x[2].split('／')] for x in rows(P/(pre+'wp23-shadow-data-and-vectors.md'),'### 3.1','### 3.2') if len(x)>=3 and re.fullmatch(r'[A-Z]+',x[0]) and re.fullmatch(r'\d+',x[1])}
 res['shadow_'+name]=equal_tables(actual,shadow_expect)
optional_moves=sections(R/'PBS/Shadow Pokémon backup/moves_shadow_pkmn.txt')
optional_items=sections(R/'PBS/Shadow Pokémon backup/items_shadow_pkmn.txt')
for name,pre in [('final','deliverables/final-specification-set/pokemon-rules/'),('original','specs/pokemon-rules/')]:
 path=P/(pre+'wp23-shadow-data-and-vectors.md')
 actual={x[0]:x[1] for x in rows(path,'### 3.2','## 4.') if len(x)==2 and x[0].startswith('SHADOW')}
 res['optional_move_effects_'+name]=equal_tables(actual,{k:v['FunctionCode'] for k,v in optional_moves.items()})
 actual={x[0]:[x[1],x[2],int(x[3]),x[4].replace(' ','')] for x in rows(path,'### 3.2','## 4.') if len(x)==5 and x[0] in optional_items}
 expected={k:[v['FieldUse'],v.get('BattleUse','无'),int(v['Price']),'无（未声明Flags）'] for k,v in optional_items.items()}
 res['optional_items_'+name]=equal_tables(actual,expected)
res['optional_move_types']=sorted(set(v['Type'] for v in optional_moves.values()))
res['optional_items_flags_absent']=all('Flags' not in v for v in optional_items.values())
heart_text=data(R/'Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb')
heart={k:list(map(int,nums.split(','))) for k,nums in re.findall(r':([A-Z]+)\s*=>\s*\[([\d, ]+)\]',heart_text)}
for name,pre in [('final','deliverables/final-specification-set/pokemon-rules/'),('original','specs/pokemon-rules/')]:
 actual={x[0]:list(map(int,x[1:])) for x in rows(P/(pre+'wp23-shadow-data-and-vectors.md')) if len(x)==5 and re.fullmatch(r'\d+',x[1])}
 res['heart_'+name]=equal_tables(actual,heart)
stat_names={'ATTACK':'攻击','DEFENSE':'防御','SPEED':'速度','SPECIAL_ATTACK':'特攻','SPECIAL_DEFENSE':'特防'}
natures=[]
for block in data(R/'Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb').split('GameData::Nature.register(')[1:]:
 name=re.search(r':id\s*=>\s*:([A-Z]+)',block).group(1); ch=re.findall(r'\[:([A-Z_]+),\s*(-?\d+)\]',block)
 natures.append([name,next((stat_names[s] for s,n in ch if int(n)==10),'无'),next((stat_names[s] for s,n in ch if int(n)==-10),'无')])
for name,pre in [('final','deliverables/final-specification-set/pokemon-rules/'),('original','specs/pokemon-rules/')]:
 actual={x[0]:x[1:] for x in rows(P/(pre+'wp19-attributes-ability-and-stats.md')) if len(x)==4 and re.fullmatch(r'\d+',x[0])}
 res['nature_'+name]=equal_tables(actual,{str(i):v for i,v in enumerate(natures)})
res['nature_neutral_count']=sum(x[1]=='无' for x in natures)
# These are only our own fixed integer arithmetic, not a reference implementation.
res['fixed_arithmetic']={'hp':(45*2+31)*50//100+50+10,'unmodified_atk_def':(49*2+31)*50//100+5,'unmodified_spa_spd':(65*2+31)*50//100+5,'unmodified_speed':(45*2+31)*50//100+5,'atk_plus':69*110//100,'def_minus':69*90//100,'speed_minus':65*90//100,'spa_minus':85*90//100,'synthetic_plus_minus':[105*110//100,105*90//100],'heart_hardy':[2500-90,(2500-90+799)//800],'heart_lonely':[2500-130,(2500-130+799)//800],'facility_255':[510//2,255//4]}
ids=json.loads((P/'review/remediation-20261003-prepare/batches.json').read_text())[4]['contribution_finding_ids']
orig=json.loads(g('show',O+':review/global-independent-review/2026-10-03-fd82a639/findings.json')); om={x['id']:x for x in orig}; acceptance=json.loads((P/'review/remediation-20261003-prepare/finding-acceptance.json').read_text())
res['original_objects']=[{'id':i,'priority':om[i]['priority'],'sha256_of_canonical_object':hashlib.sha256(json.dumps(om[i],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'raw_reports':len(om[i]['raw_reports']),'adjudications':len(om[i]['root_adjudications']),'extensions':len(om[i].get('extensions',[])),'acceptance_inherited_equal':all(acceptance[i][k]==om[i][k] for k in ['current_qualifications','root_adjudications','premises','minimum_counterexample','minimum_revision','determinate_recheck','evidence','extension_decisions']),'effective_case_constraints_equal':acceptance[i].get('effective_case_constraints',[])==om[i].get('effective_case_constraints',[])} for i in ids]
changes=g('diff','--name-only',B,C).splitlines();res['formal_paths']=[x for x in changes if x.startswith(('deliverables/','specs/'))]
res['formal_count']=len(res['formal_paths']);res['other_candidate_paths_only_B05_review']=all(x.startswith('review/remediation/20261003-prepare/batches/B05/') for x in changes if x not in res['formal_paths'])
res['candidate_formal_manifest']=[{'path':x,'blob':g('rev-parse',C+':'+x).strip(),'sha256':hashlib.sha256(g('show',C+':'+x).encode()).hexdigest(),'lines':len(g('show',C+':'+x).splitlines())} for x in res['formal_paths']]
res['neighbor_test_rows']={}
for x in res['formal_paths']:
 if '/test-catalog/' not in x:continue
 old={r.split('|')[1].strip():r for r in g('show',B+':'+x).splitlines() if re.match(r'\| [A-Z]+-?\d+ \|',r)}
 new={r.split('|')[1].strip():r for r in g('show',C+':'+x).splitlines() if re.match(r'\| [A-Z]+-?\d+ \|',r)}
 res['neighbor_test_rows'][x]={'modified_existing':[k for k in old if old[k]!=new.get(k)],'added':[k for k in new if k not in old],'deleted':[k for k in old if k not in new],'unaffected_pt_ps_aq_br_equal':all(old[k]==new.get(k) for k in old if k.startswith(('PT','PS','AQ','BR')))}
res['correct_original_tables_unchanged_from_fix_base']=all(g('show',B+':'+x)==g('show',C+':'+x) for x in ['specs/pokemon-rules/wp22-transformation-data.md','specs/pokemon-rules/wp23-shadow-data-and-vectors.md'])
res['review_baseline_formal_changes']=g('diff','--name-only','e1e01bb18d824931e54f182dd61af5a9f908ba85',B,'--','specs','deliverables').splitlines()
res['reference_head']=subprocess.check_output(['git','-C',str(R),'rev-parse','HEAD'],text=True).strip();res['reference_tree']=subprocess.check_output(['git','-C',str(R),'rev-parse','HEAD^{tree}'],text=True).strip();res['reference_clean']=not subprocess.check_output(['git','-C',str(R),'status','--porcelain'],text=True)
res['all_static_checks_pass']=all(not v['missing'] and not v['extra'] and not v['differences'] for v in res.values() if isinstance(v,dict) and 'expected_rows' in v) and res['formal_count']==15 and res['reference_clean'] and all(x['acceptance_inherited_equal'] and x['effective_case_constraints_equal'] for x in res['original_objects']) and all(x['unaffected_pt_ps_aq_br_equal'] and not x['deleted'] for x in res['neighbor_test_rows'].values())
pathlib.Path('/tmp/b05-independent-static.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k not in ['candidate_formal_manifest','original_objects','review_baseline_formal_changes']},ensure_ascii=False,indent=2))
