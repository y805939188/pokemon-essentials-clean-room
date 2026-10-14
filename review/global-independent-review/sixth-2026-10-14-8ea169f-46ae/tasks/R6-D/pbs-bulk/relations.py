"""Fixed-input literal data review. No source execution or semantic PASS claim.

Fields whose consumer semantics are not model-reviewed stay open even when
all literal atoms resolve. Unknown code names are candidates, not compile errors.
"""
import audit as a
from collections import Counter, defaultdict
from pathlib import Path
import json, re, csv

SCHEMA_DIR='reference/pokemon-essentials/Data/Scripts/010_Data/002_PBS data/'
COMPILER='reference/pokemon-essentials/Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb'
FORMS='deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md'
LIFECYCLE='deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md'
VARIANTS='deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md'
SOURCE_FILE={'types':'003_Type.rb','abilities':'004_Ability.rb','moves':'005_Move.rb','items':'006_Item.rb','berry_plants':'007_BerryPlant.rb','pokemon':'008_Species.rb','pokemon_forms':'008_Species.rb','pokemon_metrics':'010_SpeciesMetrics.rb','shadow_pokemon':'011_ShadowPokemon.rb'}
# Hand-bound from model-visible schema reads recorded in reading-ledger.jsonl.
# A symbolic atom's resolution is checked separately from its scalar shape.
SCHEMAS={
 'types':{'Name':'text','IconPosition':'u','IsSpecialType':'b','IsPseudoType':'b','Weaknesses':'*Type','Resistances':'*Type','Immunities':'*Type','Flags':'list_text'},
 'abilities':{'Name':'text','Description':'text','Flags':'list_text'},
 'moves':{'Name':'text','Type':'Type','Category':'MoveCategory','Power':'u','Accuracy':'u','TotalPP':'u','Target':'Target','Priority':'i','FunctionCode':'effect_identity','Flags':'list_text','EffectChance':'u','Description':'text'},
 'items':{'Name':'text','NamePlural':'text','PortionName':'text','PortionNamePlural':'text','Pocket':'v','Price':'u','SellPrice':'u','BPPrice':'u','FieldUse':'FieldUse','BattleUse':'BattleUse','Flags':'list_text','Consumable':'b','ShowQuantity':'b','Move':'Move','Description':'text'},
 'berry_plants':{'HoursPerStage':'v','DryingPerHour':'u','Yield':'u,v'},
 'pokemon_metrics':{'BackSprite':'i,i','FrontSprite':'i,i','FrontSpriteAltitude':'i','ShadowX':'i','ShadowSize':'u'},
 'shadow_pokemon':{'GaugeSize':'v','Moves':'*Move','Flags':'list_text'},
}
SPECIES={'Name':'text','FormName':'text','Types':'*Type','BaseStats':'v,v,v,v,v,v','GenderRatio':'GenderRatio','GrowthRate':'GrowthRate','BaseExp':'v','EVs':'pairs_Stat_v','CatchRate':'u','Happiness':'u','Abilities':'*Ability','HiddenAbilities':'*Ability','Moves':'pairs_u_Move','TutorMoves':'*Move','EggMoves':'*Move','EggGroups':'*EggGroup','HatchSteps':'v','Incense':'Item','Offspring':'*Species','Height':'f','Weight':'f','Color':'BodyColor','Shape':'BodyShape','Habitat':'Habitat','Category':'text','Pokedex':'text','Generation':'i','Flags':'list_text','WildItemCommon':'*Item','WildItemUncommon':'*Item','WildItemRare':'*Item','Evolution':'evolution','Evolutions':'evolutions'}
SCHEMAS['pokemon']=SPECIES
SCHEMAS['pokemon_forms']={k:v for k,v in SPECIES.items() if k not in {'Name','GenderRatio','GrowthRate','Incense'}}
SCHEMAS['pokemon_forms'].update({'PokedexForm':'u','MegaStone':'Item','MegaMove':'Move','UnmegaForm':'u','MegaMessage':'u'})
INLINE={'MoveCategory':{'Physical','Special','Status'},'FieldUse':{'OnPokemon','Direct','TM','HM','TR'},'BattleUse':{'OnPokemon','OnMove','OnBattler','OnFoe','Direct'}}
HARD={'GrowthRate':'001_GrowthRate.rb','GenderRatio':'002_GenderRatio.rb','EggGroup':'003_EggGroup.rb','BodyShape':'004_BodyShape.rb','BodyColor':'005_BodyColor.rb','Habitat':'006_Habitat.rb','Evolution':'007_Evolution.rb','Stat':'008_Stat.rb','Target':'017_Target.rb'}

def atoms(v):return [x.strip() for x in next(csv.reader([v],skipinitialspace=True))]
def loc(r,f=None):
    z={'path':r['path'],'identity':r['identity'],'start_line':r['start_line'],'end_line':r['end_line']}
    if f:z.update(field=f['key'],line=f['line'])
    return z
def effective(r):
    d={}
    for f in r['fields']:
        if f['key']=='Evolution':d.setdefault('Evolution',[]).append(f)
        else:d[f['key']]=f
    return d
def normid(r):
    return re.sub(r'\s*,\s*',',',r['identity'])
def readrecords():return [json.loads(x) for x in (a.OUT/'record-inventory.jsonl').read_text().splitlines()]
def run():
    a.bind();rs=readrecords();registries=defaultdict(lambda:defaultdict(dict));hard={};methods={}
    for dom,f in HARD.items():
        p=a.ROOT/'reference/pokemon-essentials/Data/Scripts/010_Data/001_Hardcoded data'/f
        ids={};cur=None
        for n,line in enumerate(p.read_text().splitlines(),1):
            m=re.search(r':id\s*=>\s*:(\w+)',line)
            if m:
                cur=m[1];ids[cur]={'path':str(p.relative_to(a.ROOT)),'line':n}
                if dom=='Evolution':methods[cur]={'kind':'none','source':ids[cur]}
            m=re.search(r':parameter\s*=>\s*(:?\w+)',line)
            if m and dom=='Evolution' and cur:methods[cur]['kind']=m[1].lstrip(':')
        hard[dom]=ids
        a.append('reading-ledger.jsonl',{'time':a.now(),'path':str(p.relative_to(a.ROOT)),'start_line':1,'end_line':len(p.read_text().splitlines()),'mode':'deterministic_id_parameter_location_scan','semantic_status':'NOT_A_SEMANTIC_READ'})
    doms={'pokemon':'Species','pokemon_forms':'Species','moves':'Move','items':'Item','abilities':'Ability','types':'Type','berry_plants':'BerryPlant','pokemon_metrics':'SpeciesMetrics','shadow_pokemon':'ShadowPokemon'}
    for r in rs:
        ident=normid(r)
        if r['family']=='pokemon_forms':ident=ident.replace(',','_')
        registries[r['profile']][doms[r['family']]][ident]=loc(r)
    # Shadow is a conditional overlay of current data, never a standalone game profile.
    shadow='Shadow Pokémon backup'
    overlay={k:{**v,**registries[shadow].get(k,{})} for k,v in registries['.'].items()}
    for k,v in registries[shadow].items():overlay.setdefault(k,{}).update(v)
    registries[shadow]=overlay
    relations=[];shapes=[];duplicates=[];orders=[];cross=[];unknownkeys=[]
    def check_ref(r,f,domain,value,position,stage='field_enum'):
        reg=hard.get(domain,registries[r['profile']].get(domain,{}))
        target=reg.get(value)
        relations.append({**loc(r,f),'position':position,'domain':domain,'target_identity':value,'target_location':target,'literal_resolution':'present' if target else 'absent_in_conditional_registry','validation_stage':stage,'precondition':'All same-profile families replace active data; Shadow overlays current registries. No actual compilation executed.','semantic_status':'identity_relation_only_not_semantic_approval'})
    def scalar(kind,v):
        if kind=='u':return bool(re.fullmatch(r'\d+',v))
        if kind=='v':return bool(re.fullmatch(r'\d+',v)) and int(v)>0
        if kind=='i':return bool(re.fullmatch(r'-?\d+',v))
        if kind=='f':
            try:float(v);return True
            except ValueError:return False
        if kind=='b':return v.lower() in {'0','1','true','false','yes','no','y','n'}
        return True
    for r in rs:
        ident=atoms(r['identity'])
        if r['family'] in {'pokemon_forms','pokemon_metrics','shadow_pokemon'}:
            fake={'key':'SectionName','line':r['start_line']}
            check_ref(r,fake,'Species',ident[0],0,'section_species_enum')
            if len(ident)>1:shapes.append({**loc(r,fake),'shape':'positive_form_integer','ok':scalar('v',ident[1]),'scope':'authored_scalar_shape'})
        if r['family']=='berry_plants':
            # Runtime association; not a compiler enum validation.
            check_ref(r,{'key':'SectionName','line':r['start_line']},'Item',r['identity'],0,'runtime_association_ONLY_not_compile_check')
        for f in r['fields']:
            k=f['key'];kind=SCHEMAS[r['family']].get(k)
            if not kind:unknownkeys.append(loc(r,f));continue
            if kind=='text':continue
            v=f['value'];vs=atoms(v);ok=True
            if kind in {'u','v','i','f','b'}:ok=len(vs)==1 and scalar(kind,vs[0])
            elif kind in INLINE:ok=len(vs)==1 and vs[0] in INLINE[kind]
            elif ',' in kind:ks=kind.split(',');ok=len(vs)==len(ks) and all(scalar(t,x) for t,x in zip(ks,vs))
            elif kind.startswith('pairs_'):
                _,first,second=kind.split('_');ok=len(vs)%2==0
                for j,x in enumerate(vs):
                    typ=first if j%2==0 else second
                    if typ in {'u','v'}:ok=ok and scalar(typ,x)
                    else:check_ref(r,f,typ,x,j)
                if k=='Moves':
                    levels=[int(x) for x in vs[::2] if scalar('u',x)]
                    if any(x>y for x,y in zip(levels,levels[1:])):orders.append({**loc(r,f),'kind':'nonmonotonic_authored_learning_levels','conclusion':'legal_shape; authored order retained for later consumer analysis'})
            elif kind in {'evolution','evolutions'}:
                ok=len(vs) in {2,3} if kind=='evolution' else len(vs)%3==0
                groups=[vs] if kind=='evolution' else [vs[i:i+3] for i in range(0,len(vs),3)]
                for group in groups:
                    if len(group)<2:continue
                    check_ref(r,f,'Species',group[0],0,'deferred_base_species_or_immediate_form_enum')
                    check_ref(r,f,'Evolution',group[1],1)
                    method=methods.get(group[1]);param=group[2] if len(group)>2 else None
                    if method and method['kind']!='none':
                        if param is None:ok=False
                        elif method['kind']=='Integer':ok=ok and scalar('u',param)
                        elif method['kind']!='String':check_ref(r,f,method['kind'],param,2,'evolution_parameter_deferred_enum')
            elif kind not in {'list_text','effect_identity'}:
                domain=kind.lstrip('*')
                for j,x in enumerate(vs):check_ref(r,f,domain,x,j,'deferred_offspring_enum' if k=='Offspring' and r['family']=='pokemon' else 'field_enum')
            shapes.append({**loc(r,f),'shape':kind,'ok':ok,'scope':'literal_atom_shape_only; not compiler execution or semantic validity'})
            if kind.startswith('*') or kind in {'list_text'}:
                dup={x:c for x,c in Counter(vs).items() if c>1}
                if dup:duplicates.append({**loc(r,f),'duplicates':dup,'conclusion':'consumer-specific duplicate behavior required; not invalidity'})
        fs=effective(r)
        if r['family']=='moves':
            category=fs['Category']['value'] if 'Category' in fs else 'Status';power=int(fs['Power']['value']) if 'Power' in fs else 0
            cross.append({**loc(r),'check':'move_category_power','category':category,'power':power,'predicted_validation':'reject' if category=='Status' and power!=0 else ('warn_coerce_Status' if category!='Status' and power==0 else 'no_category_power_intervention'),'precondition':'new unique identity, legal prior lexical conversion and registered references; warning returns normally','source':{'path':COMPILER,'start_line':211,'end_line':218}})
    a.save('reference-relations.json',relations);a.save('shape-checks.json',shapes);a.save('duplicate-atoms.json',duplicates);a.save('nonmonotonic-learning-lists.json',orders);a.save('move-category-power-controls.json',cross)
    a.save('unknown-authored-fields.json',unknownkeys)
    # Every field delta is represented, including text hashes; no prose copied.
    byprofile=defaultdict(dict)
    for r in rs:byprofile[r['profile']][(r['family'],normid(r))]=r
    current=byprofile['.'];deltas=[];stats=[]
    for profile,rows in byprofile.items():
        if profile in {'.',shadow}:continue
        ctr=Counter()
        for key in sorted(set(rows)|set(current)):
            old=rows.get(key);new=current.get(key)
            if old is None:kind='added_to_current';fields=[]
            elif new is None:kind='absent_from_current';fields=[]
            else:
                of=effective(old);nf=effective(new);fields=[]
                for field in sorted(set(of)|set(nf)):
                    l=of.get(field);r=nf.get(field)
                    def payload(v):
                        if v is None:return None
                        if isinstance(v,list):return [payload(x) for x in v]
                        return {k:x for k,x in v.items() if k!='line'}
                    if payload(l)!=payload(r):fields.append({'field':field,'backup':l,'current':r})
                kind='changed_fields' if fields else 'same_authored_fields'
            ctr[(key[0],kind)]+=1
            deltas.append({'profile':profile,'family':key[0],'identity':key[1],'comparison':kind,'backup_location':loc(old) if old else None,'current_location':loc(new) if new else None,'field_deltas':fields,'meaning':'literal authored delta only; availability and runtime semantics remain conditional'})
        stats.append({'profile':profile,'counts':[{'family':k[0],'comparison':k[1],'records':v} for k,v in sorted(ctr.items())]})
    a.save('profile-record-deltas.json',deltas);a.save('profile-comparison-summary.json',stats)
    # Named implementations are located only; a missing implementation has its own
    # runtime fallback, unlike a missing Type/Move enum. No automatic invalidity.
    handlers=defaultdict(list)
    for p in sorted((a.REF/'Data/Scripts').rglob('*.rb')):
        for n,line in enumerate(p.read_text().splitlines(),1):
            m=re.match(r'\s*class Battle::Move::(\w+)',line)
            if m:handlers[m[1]].append({'path':str(p.relative_to(a.ROOT)),'line':n})
    links=[]
    for r in rs:
        if r['family']!='moves':continue
        f=effective(r).get('FunctionCode');code=f['value'] if f else 'None'
        links.append({**loc(r,f),'effect_identity':code,'implementation_locations':handlers.get(code,[]),'missing_disposition':'runtime Unimplemented fallback; NOT enum parse rejection' if not handlers.get(code) else None,'factory':{'path':'reference/pokemon-essentials/Data/Scripts/011_Battle/003_Move/001_Battle_Move.rb','start_line':57,'end_line':68},'semantic_status':'handler_bodies_not_reviewed'})
    a.save('move-effect-consumer-links.json',links)
    unresolved=[x for x in relations if not x['target_location']]
    a.save('conditional-unresolved-references.json',unresolved)
    summary={'reference_atoms':len(relations),'conditional_unresolved_atoms':len(unresolved),'literal_shapes_checked':len(shapes),'shape_exceptions':sum(not x['ok'] for x in shapes),'unknown_authored_fields':len(unknownkeys),'duplicate_list_fields':len(duplicates),'nonmonotonic_learning_lists':len(orders),'move_category_power_counts':dict(Counter(x['predicted_validation'] for x in cross)),'moves_with_unlocated_named_handlers':len([x for x in links if not x['implementation_locations']]),'unlocated_effect_identities':sorted({x['effect_identity'] for x in links if not x['implementation_locations']}),'semantic_complete':False}
    a.save('relations-summary.json',summary);print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':
    a.append('command-log.jsonl',{'time':a.now(),'script':'relations.py','script_sha256':a.sha(Path(__file__).read_bytes()),'purpose':'conditional literal relation, shape, profile and named consumer-location audits'})
    run()
