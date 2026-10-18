from pathlib import Path
import json,re,datetime,hashlib,subprocess
P=Path(__file__).resolve().parent;R=Path('/workspace/pokemon-essentials');C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';UTC=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
G='Data/Scripts/010_Data/001_Hardcoded data/001_GrowthRate.rb';PK='Data/Scripts/014_Pokemon/001_Pokemon.rb';F='deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md'
def ident(path):
 b=(R/path).read_bytes();assert b==subprocess.check_output(['git','show',C+':'+path],cwd=R)
 return {'repo':str(R),'commit':C,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':subprocess.check_output(['git','rev-parse',C+':'+path],cwd=R,text=True).strip(),'lines':len(b.splitlines())}
gi=ident(G);pi=ident(PK);text=(R/G).read_text();lines=text.splitlines()
# Own arithmetic for a formally stated mathematical function. No Ruby/reference call.
def curve(k,n):
 if n==1:return 0
 if k=='Medium':return n**3
 if k=='Fast':return 4*n**3//5
 if k=='Slow':return 5*n**3//4
 if k=='Parabolic':return 6*n**3//5-15*n*n+100*n-140
 if k=='Erratic':
  if n<=50:return n**3*(100-n)//50
  if n<=68:return n**3*(150-n)//100
  if n<=98:return n**3*((1911-10*n)//3)//500
  return n**3*(160-n)//100
 if k=='Fluctuating':
  if n<=15:return n**3*(24+(n+1)//3)//50
  if n<=35:return n**3*(14+n)//50
  return n**3*(32+n//2)//50
 raise AssertionError(k)
formal_lines={'Medium':64,'Fast':65,'Slow':66,'Parabolic':67,'Erratic':68,'Fluctuating':69}
formula_meanings={
 'Medium':'n^3; valid table L1 is the explicit0 exception.',
 'Fast':'floor(4*n^3/5); valid table L1=0.',
 'Slow':'floor(5*n^3/4); valid table L1 is the explicit0 exception.',
 'Parabolic':'floor(6*n^3/5)-15*n^2+100*n-140; table L1 explicitly0 rather than extending this expression there.',
 'Erratic':'Table valid levels use four specified integer branches: <=50,51..68,69..98 (inner floor first),99..100. Registered out-of-table formula is floor((n^4+2000*n^3)/3500), a distinct function.',
 'Fluctuating':'Table valid levels use <=15,16..35,>=36 with specified inner integer divisions. Registered out-of-table formula is floor((n^3+floor(n/2)+32)*4/(100+n)), a distinct function.'}
records=[];value_atoms=[]
for m in re.finditer(r'GameData::GrowthRate\.register\(\{(.*?)\}\)',text,re.S):
 body=m.group(0);k=re.search(r':id\s*=>\s*:(\w+)',body).group(1);a=text[:m.start()].count('\n')+1;z=text[:m.end()].count('\n')+1
 tab=re.search(r':exp_values\s*=>\s*\[(.*?)\]',body,re.S);values=[int(v) for v in re.findall(r'-?\d+',tab.group(1))];assert len(values)==101 and values[0]==-1
 rows=[]
 for n,v in enumerate(values[1:],1):
  expected=curve(k,n);assert v==expected,(k,n,v,expected)
  rows.append([n,v,expected])
  value_atoms.append({'id':f'PCR-GROWTH-TABLE-{k}-{n:03}','formal':{'path':F,'lines':[formal_lines[k],71]},'assertion':f'For {k} valid table level{n}, minimum experience is{v}; table lookup is authoritative after the maximum-level clamp.','sourcefact_ids':[],'source_units':[{'identity':gi,'lines':[a,z]},{'identity':gi,'lines':[41,47]}],'actual_reader':'/root/pbs_creature_current_cloud','status':'FINITE_ASSERTION_MATCHED_SOURCE_STATIC_AND_OWN_ARITHMETIC','premises':['Fixed six registries; valid integer requested level after max-level clamp lies in1..100.','L1 explicit table0 exception retained; this cell is not an extrapolated out-of-table formula or executed lookup.'],'qualification':'Every raw table value actually read before extraction. This row serializes its own integer value and the independently specified arithmetic comparison; parsing/assert equality is only a post-reading consistency check.'})
 records.append({'ordinal':len(records)+1,'id':k,'source_identity':gi,'source_range':[a,z],'complete_source_body':body,'name':k,'zero_index_sentinel':-1,'valid_level_count':100,'vector_columns':['level','raw_table_minimum_exp','own_integer_math_result'],'complete_valid_level_vectors':rows,'manual_formula_meaning':formula_meanings[k],'formal_curve_row':[formal_lines[k],formal_lines[k]],'actual_reader':'/root/pbs_creature_current_cloud'})
assert [r['id'] for r in records]==['Medium','Erratic','Fluctuating','Parabolic','Fast','Slow'] and len(value_atoms)==600
happy=[('walking',[2,2,1],195),('levelup',[5,4,3],196),('groom',[10,10,4],197),('evberry',[10,5,2],198),('vitamin',[5,3,2],199),('wing',[3,2,1],200),('machine',[1,1,0],201),('battleitem',[1,1,0],201),('faint',[-1,-1,-1],202),('faintbad',[-5,-5,-10],203),('powder',[-5,-5,-10],204),('energyroot',[-10,-10,-15],205),('revivalherb',[-15,-15,-20],206)]
happy_atoms=[]
for method,gains,fl in happy:
 for tier,gain in enumerate(gains):
  happy_atoms.append({'id':f'PCR-HAPPY-TABLE-{method}-{tier}','formal':{'path':F,'lines':[fl,fl]},'assertion':f'Method {method}, happiness band{tier} (within0..255), base gain{gain} before positive-only modifiers and final clamp.','sourcefact_ids':[],'source_units':[{'identity':pi,'lines':[929,969]}],'actual_reader':'/root/pbs_creature_current_cloud','status':'FINITE_ASSERTION_MATCHED_SOURCE_STATIC','premises':['Fixed method and ordinary happiness0..255; map/item/callback dependencies return normally where read.','Caller existence is not inferred from method registration; groom ordinary caller remains unlocated.'],'qualification':'Complete own method and formal table actually read, including every band; no execution.'})
misc=[
 ('MAX',52,'Maximum level delegates to Settings, default100; compilation may invoke it before gameplay globals exist.'),
 ('CLAMP-TABLE',53,'minimum_exp_for_level first clamps above max, then uses table when index<table length; registered formula is only the later fallback.'),
 ('MAXIMUM',54,'maximum_exp calls minimum_exp_for_level at current max level.'),
 ('ADD-CLAMP',55,'add_exp clamps the sum to[0,maximum_exp], separately from the raw Pokemon exp= writer.'),
 ('REVERSE',56,'Valid reverse lookup first returns max when exp>=maximum_exp, otherwise finds the first level threshold greater than exp and returns previous level.'),
 ('ERRATIC-101',74,'With explicit max101, registered Erratic out-of-table expression gives618474; default max100 instead clamps request101 to table600000.'),
 ('FLUCT-101',74,'With explicit max101, registered Fluctuating out-of-table expression gives20505; default max100 clamps request101 to table1640000. No monotonic continuation is inferred.'),
 ('HAPPY-INITIAL',186,'Species authored Happiness256 can survive the nonnegative schema and direct constructor copy; creator does not impose controlled-change255 clamp.'),
 ('HAPPY-UNKNOWN',208,'Unknown happiness method raises before final happiness assignment.'),
 ('HAPPY-MAP',209,'Only positive base gain receives matching-obtain-map +1.'),
 ('HAPPY-BALL',209,'Only positive base gain receives LUXURYBALL +1, after the map bonus.'),
 ('HAPPY-BELL',209,'SOOTHEBELL multiplies the already map/ball-adjusted positive gain by1.5 then floors.'),
 ('HAPPY-SOFT',209,'Enabled soft cap applies only to positive gain and methods other than evberry; at happiness>=179 gain0, below it capped by179-happiness.'),
 ('HAPPY-NEGATIVE',210,'Negative base gains bypass map/ball/bell/soft-cap positive-only branch.'),
 ('HAPPY-FINAL',187,'After a method and its modifiers finish normally, happiness+gain is clamped0..255; this later method does not retroactively clamp constructor observation.'),
]
misc_atoms=[]
assert (101**4+2000*101**3)//3500==618474 and ((101**3+101//2+32)*4)//201==20505
for id,fl,meaning in misc:
 source=({'identity':gi,'lines':[23,71]} if not id.startswith('HAPPY') else {'identity':pi,'lines':[916,969]})
 misc_atoms.append({'id':'PCR-GROWTH-'+id,'formal':{'path':F,'lines':[fl,fl]},'assertion':meaning,'sourcefact_ids':[],'source_units':[source],'actual_reader':'/root/pbs_creature_current_cloud','status':'FINITE_ASSERTION_MATCHED_SOURCE_STATIC_AND_OWN_ARITHMETIC','premises':['Fixed source and stated valid input/current configuration; normal invoked dependencies; no external override.','Only this assertion, not all parent paragraph or arbitrary out-of-range behavior.'],'qualification':'Manual semantic comparison and own exact integer arithmetic where numeric; no reference/game execution.'})
for index,(a,z,value) in enumerate([(0,99,0),(100,149,1),(150,199,2),(200,229,3),(230,254,4),(255,255,5)]):
 misc_atoms.append({'id':f'PCR-GROWTH-AFFECTION-{index}','formal':{'path':F,'lines':[214,216]},'assertion':f'For ordinary happiness{a}..{z}, affection_level returns{value}; raw out-of-domain inputs are not inferred from this band.','sourcefact_ids':[],'source_units':[{'identity':pi,'lines':[916,925]}],'actual_reader':'/root/pbs_creature_current_cloud','status':'FINITE_ASSERTION_MATCHED_SOURCE_STATIC','premises':['Valid integer happiness in the named ordinary band; no plugin override.'],'qualification':'Complete own getter read. The fallback5 also covers other unmatched raw values in source, without broadening the formal ordinary-domain table.'})
atoms=value_atoms+happy_atoms+misc_atoms
out=P/'growth-happiness-all-values.complete.v1.json';assert not out.exists()
d={'schema':'gr8-pbs-current-growth-happiness-complete-finite/v1','utc':UTC,'actual_reader':'/root/pbs_creature_current_cloud','fixed_R':C,'actual_read_io':{'whole_GrowthRate188':['9d6dea','fea4be'],'whole_WP30_286':['b9857e','6cc809'],'happiness_complete_getters':['ababf1'],'original_own_full_read':'Already recorded in reading-ledger before this reread; no new reviewer/context.'},'complete_growth_records':records,'growth_interface_source':{'identity':gi,'range':[1,73],'complete_body':'\n'.join(lines[:73])+'\n'},'complete_happiness_source':{'identity':pi,'range':[916,969],'complete_body':'\n'.join((R/PK).read_text().splitlines()[915:969])+'\n'},'complete_happiness_rows':[{'method':m,'base_gains_0_99_100_199_200_255':v,'formal_line':fl} for m,v,fl in happy],'complete_manual_reverse_atoms':atoms,'primary_consumer_joins':['Species.growth_rate copied or form-inherited then Pokemon.growth_rate resolves the selected current effective Species record.','Pokemon.level/level=/exp_fraction and constructor use this exact curve; trainers create ordinary owned members through that constructor.','Own full DayCare and BattleExp use bounded growth add/level interfaces; their arbitrary battle item effects or host UI callbacks are separate.','Species Happiness initializes Pokemon.happiness directly; whole changeHappiness reads the current integer band only when invoked.'],'qualification':'All600 raw table values and all6 complete registry bodies actually read before post-reading extraction/arithmetic. Independent Python mathematics validates our written formal expressions only, never executes Ruby/game/reference parser. Shared source methods/type checking and finite consumers are read separately. No complete growth/battle/learning UI domain acceptance.','remaining':'All unreceived held-item callbacks, arbitrary UI/native/event callers and external alternative definitions remain OPEN.15 EggGroup directory adjudication remains a separate OPEN query.','business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED','new_findings':[],'new_contexts':0,'new_votes':0}
out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
rev=json.loads((P/'reverse-mapping.json').read_text());assert len(rev['clauses'])==1738;prior=P/'reverse-mapping.v10.frozen.json';assert not prior.exists();prior.write_bytes((P/'reverse-mapping.json').read_bytes());known={a['id'] for a in rev['clauses']};assert all(a['id'] not in known for a in atoms);rev['clauses']+=atoms;rev['schema']='gr8-pbs-current-reverse/v11';rev['utc']=UTC;rev['supersedes']='reverse-mapping.v10.frozen.json retained';rev['atom_denominator_frozen_so_far']=len(rev['clauses']);rev['growth_happiness_addendum']={'path':out.name,'new_atoms':len(atoms),'growth_valid_table_cells':600,'happiness_band_cells':39,'misc':len(misc_atoms),'prior':1738,'current':len(rev['clauses']),'meaning':'Typed table cells plus independently stated formula/caller predicates; count does not establish parent-domain completeness.'};(P/'reverse-mapping.json').write_text(json.dumps(rev,ensure_ascii=False,indent=2)+'\n')
ledger=json.loads((P/'reading-ledger.json').read_text());ledger['dependencies_partial_read'] += [{'path':'Data/Scripts/016_UI/020_UI_PokeMart.rb','lines':[1,175],'actual_read_chunk':'2b7e38','complete_units':['whole PokemonMartAdapter4–96','whole BuyAdapter101–133','whole SellAdapter138–174']},{'path':'Data/Scripts/016_UI/021_UI_BattlePointShop.rb','lines':[1,90],'actual_read_chunk':'2b7e38','complete_units':['whole BattlePointShopAdapter4–89']}];ledger['updated_utc']=UTC;(P/'reading-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':UTC,'path':str(out),'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'growth_records':6,'valid_table_cells':600,'happy_band_cells':39,'new_atoms':len(atoms),'reverse_atoms':len(rev['clauses'])},ensure_ascii=False))
