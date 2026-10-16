"""Conditional profile data certificates, not a behavior model or reference run."""
from pathlib import Path
import collections, hashlib, importlib.util, json
HERE=Path(__file__).parent
REF=Path('/workspace/pokemon-essentials')
spec=importlib.util.spec_from_file_location('finite_pool_math',HERE/'finite-pool-audit.py')
math=importlib.util.module_from_spec(spec);spec.loader.exec_module(math)
raw=json.loads((HERE/'trainer-structure.json').read_text())
traits_doc=json.loads((HERE/'subreviews/trait_eligibility/finite-traits.json').read_text())
pairs={'PBS/battle_tower_trainers.txt':'PBS/battle_tower_pokemon.txt','PBS/cup_fancy_trainers.txt':'PBS/cup_fancy_pkmn.txt','PBS/cup_fancy_trainers_single.txt':'PBS/cup_fancy_pkmn_single.txt','PBS/cup_little_trainers.txt':'PBS/cup_little_pkmn.txt','PBS/cup_pika_trainers.txt':'PBS/cup_pika_pkmn.txt','PBS/cup_poke_trainers.txt':'PBS/cup_poke_pkmn.txt'}
predicates={'all_normal':None,'standard':'standard_non_egg','fancy':'fancy_species_cold','little_factory':'little_factory_species_cold','little_direct':'little_direct_species_cold','light_direct':'light_direct_species_cold','strict_little':'strict_species_cold','factory':'factory_species'}
out={};identities=[]
for dataset in ['default','Gen 5 backup','Gen 6 backup','Gen 7 backup','Gen 8 backup']:
    traits=collections.defaultdict(list)
    for row in traits_doc['records']:
        if row['dataset']==dataset and row['template_created_this_form']:
            traits[row['species']].append(row)
    base=REF/'PBS' if dataset=='default' else REF/'PBS'/dataset
    ids={}
    for kind,file in [('items','items.txt'),('moves','moves.txt')]:
        path=base/file;b=path.read_bytes()
        ids[kind]={s[1:-1] for s in b.decode('utf-8-sig').splitlines() if s.startswith('[')}
        identities.append(dict(dataset=dataset,path=str(path.relative_to(REF)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),credit='HEADER_ID_PROJECTION_ONLY; full item profile reading received CRE-B; no move-body reading credit'))
    tables={p:math.templates(p) for p in pairs.values()}
    discarded=[]
    for file,table in tables.items():
        for row in table:
            if row['item'] and row['item'] not in ids['items']:row['item']=None
            row['moves']=[m for m in row['moves'][:4] if m in ids['moves']]
            assert row['moves'], (dataset,file,row['index'],'fallback needed')
            if row['raw_item']!=row['item'] or any(m and m not in row['moves'] for m in row['raw_moves']):
                discarded.append(dict(file=file,index=row['index'],line=row['line'],raw_item=row['raw_item'],item=row['item'],raw_moves=row['raw_moves'],moves=row['moves']))
    def eligible(row,name):
        values=[True if predicates[name] is None else t[predicates[name]] for t in traits[row['species']]]
        assert values
        if name=='strict_little' and (row['item'] in ['BERRYJUICE','DEEPSEATOOTH'] or any(m in ['SONICBOOM','DRAGONRAGE'] for m in row['moves'])): values=[False]*len(values)
        assert all(values)==any(values), ('created forms differ',dataset,row['species'],name)
        return all(values)
    records=[];index=collections.Counter();summary={}
    for record in raw['source_records']:
        file=record['file'];table=tables[pairs[file]];indices=[int(x) for x in record['fields']['PokemonNos']['value'].split(',')]
        rec=dict(file=file,trainer_index=index[file],predicates={});index[file]+=1
        for name in predicates:
            cert=math.certificate([table[i] for i in indices if eligible(table[i],name)],name!='strict_little')
            rec['predicates'][name]=cert
        records.append(rec)
    for file in pairs:
        selected=[r for r in records if r['file']==file];summary[file]={}
        for name in predicates:
            summary[file][name]=dict(minimum_matching=min(r['predicates'][name]['maximum_matching'] for r in selected),
                no_team3=[r['trainer_index'] for r in selected if r['predicates'][name]['maximum_matching']<3],
                no_team4=[r['trainer_index'] for r in selected if r['predicates'][name]['maximum_matching']<4])
    out[dataset]=dict(discarded_unknown_literals=discarded,records=records,summary=summary,creation_form_all_some_equal=True)
math.write('conditional-profile-certificates.json',dict(evidence='TOOL_VALIDATION of finite data and universally proved matching rule',behavior='NOT_EXECUTED',premise='Each complete Gen5/6/7/8 dataset is separately substituted/compiled, not simultaneously active. Cold/consistent caches, fixed source definitions and normal successful creation; no claim current runtime loaded backup. Header projections only establish IDs, not battle effects.',traits_sha256=hashlib.sha256((HERE/'subreviews/trait_eligibility/finite-traits.json').read_bytes()).hexdigest(),header_identity_inputs=identities,datasets=out))
math.write('conditional-profile-summary.json',{k:dict(normalization=d['discarded_unknown_literals'],summary=d['summary'],creation_form_all_some_equal=d['creation_form_all_some_equal']) for k,d in out.items()})
print(json.dumps(dict(datasets=len(out),trainer_profile_records=sum(len(d['records']) for d in out.values()),matching_graphs=sum(len(d['records'])*8 for d in out.values()),unknown_literal_rows={k:len(v['discarded_unknown_literals']) for k,v in out.items()},behavior='NOT_EXECUTED')))
