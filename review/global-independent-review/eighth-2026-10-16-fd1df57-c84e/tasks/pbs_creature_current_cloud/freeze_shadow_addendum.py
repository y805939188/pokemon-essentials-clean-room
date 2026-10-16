from pathlib import Path
import json, datetime, hashlib, re
P=Path(__file__).resolve().parent
R=Path('/workspace/pokemon-essentials')
B=Path('/workspace/pokemon-essentials-clean-room')
U=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
T='7589c800b61ba13a13040ed0d686979b80a84fd0'
def unit(path,lo,hi):return dict(repo=str(R),commit=C,tree=T,path=path,lines=[lo,hi])
def save(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
l=json.loads((P/'reading-ledger.json').read_text())
for path in ['Data/Scripts/011_Battle/002_Battler/004_Battler_Statuses.rb','Data/Scripts/011_Battle/002_Battler/005_Battler_StatStages.rb','Data/Scripts/010_Data/001_Hardcoded data/010_Status.rb']:
 if path not in l['dependencies_full_read']:l['dependencies_full_read'].append(path)
for path,ranges,names in [
 ('Data/Scripts/011_Battle/003_Move/005_MoveEffects_Misc.rb',[[1,18]],['None wholeclass4–5; DoesNothingCongratulations also displayed complete10–18']),
 ('Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb',[[480,532]],['DoublePowerIfTargetUnderwater wholeclass502–509; neighboring complete classes only finite as displayed']),
 ('Data/Scripts/011_Battle/003_Move/013_MoveEffects_SwitchingActing.rb',[[300,349]],['TrapTargetInBattle wholeclass316–344']),
 ('Data/Scripts/011_Battle/003_Move/006_MoveEffects_BattlerStats.rb',[[972,1013],[1305,1344]],['LowerTargetDefense2 whole986–991; LowerTargetEvasion2 whole1317–1322']),
 ('Data/Scripts/011_Battle/003_Move/007_MoveEffects_BattlerOther.rb',[[134,177],[205,244],[254,296],[580,624]],['ParalyzeTarget146–164; BurnTarget217–235; FreezeTarget266–284; ConfuseTarget594–613 completeclasses']),
 ('Data/Scripts/011_Battle/003_Move/004_Move_BaseEffects.rb',[[160,199]],['TargetStatDownMove whole173–193; next class partial']),
 ('Data/Scripts/011_Battle/003_Move/003_Move_UsageCalculations.rb',[[475,535]],['pbAdditionalEffectChance489–499 and pbFlinchChance503–514 complete; actualEOF515']),
 ('Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb',[[583,762]],['pbProcessMoveHit whole583–761; classend762'])]:
 for rg in ranges:
  if not any(a['path']==path and a.get('lines')==rg for a in l['dependencies_partial_read']):l['dependencies_partial_read'].append(dict(path=path,lines=rg,complete_units=names,qualification='Actual displays ced72f/27be16/3d3f2f/7169b1/e9d3e8; neighboring partial bodies OPEN; source identity EOF computed separately.'))
l['updated_utc']=U;save('reading-ledger.json',l)
facts=json.loads((P/'bounded-pbs-facts.v6.json').read_text())
def add(title,meaning,sources):
 i=len(facts['facts'])+1
 facts['facts'].append({'id':f'PC-F{i:03d}','title':title,'fact':meaning,'actual_reader':'/root/pbs_creature_current_cloud','source_units':sources,'premises':['FixedR and no plugin/redefinition; optional Shadow content explicitly active when discussed.','Prior required class/helper calls return normally except explicitly stated rejection/failure prefix.'],'evidence':'SOURCE_STATIC','business':'NOT_EXECUTED','qualification':'Only the complete named units and expressly stated proposition; unreceived combat callbacks/callers and every native outcome remain OPEN.'})
M='Data/Scripts/011_Battle/003_Move/'
add('Shadow direct local effect classes',
    'None empty subclass adds no local effect. DoublePowerIfTargetUnderwater hitsDivingTargets? true and doubles damage multiplier only for target in TwoTurnAttackInvulnerableUnderwater. Existing ShadowOther classes: half-all fails only if no battler hasHP>1, then effect iterates every battlerHP>1 without pertarget protected/unaffected guard, removes integer currentHP/2, messages/healchecks then user recharge2/currentMove writes; UserLosesHalfHP RecoilMove uses round(current userHP/2.0), min1 after userfainted/targetunaffected guards, independent damage fraction and not prevented by RockHead/MagicGuard; StartShadowSkyWeather sets inherited WeatherMove weatherType ShadowSky. All12 existing unique selected effect classes were actually read; RemoveAllScreens has no exact class in fixed scripts.',
    [unit(M+'005_MoveEffects_Misc.rb',1,18),unit(M+'008_MoveEffects_MoveAttributes.rb',480,532),unit('Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb',330,418)])
add('Shadow status effect receivers',
    'Paralyze/Burn/Freeze/Confuse classes are MagicCoat-capable. Status form checks corresponding can-status helper; damaging form does not use that failure check and uses additional-effect method. All additional effects reject substitute and invoke helper before mutation; Confuse additionally explicit helper-return rejection. Full575 BattlerStatuses helper checks real status/substitute/weather/terrain/types/abilities/Safeguard in written order. Status write/count/Toxic reset precedes animation/message/form-check/synchronize/item/ability cures; failure later retains written prefix. Freeze wrapper passes no user; confusion writes duration2+rand4 then animation/message/cures. FullStatus76 contains NONE/SLEEP/POISON/BURN/PARALYSIS/FROZEN labels/animation/icon metadata; no host animation success proof.',
    [unit(M+'007_MoveEffects_BattlerOther.rb',134,177),unit(M+'007_MoveEffects_BattlerOther.rb',205,244),unit(M+'007_MoveEffects_BattlerOther.rb',254,296),unit(M+'007_MoveEffects_BattlerOther.rb',580,624),unit('Data/Scripts/011_Battle/002_Battler/004_Battler_Statuses.rb',1,575),unit('Data/Scripts/010_Data/001_Hardcoded data/010_Status.rb',1,76)])
add('Shadow stat lowering receivers',
    'Defense2/Evasion2 initialize statDown exact DEFENSE/EVASION and2. FullTargetStatDownMove uses eligibility for nondamaging fail check, then lowers; damaging additional effect rejects substitute/checks eligibility. Full387 StatStages implements fainted/Contrary/MirrorArmor/substitute/Mist/ability immunity/minstage gates. Basic delta honors Contrary/Simple/moldBreaker, clamps stage; write and round flags precede animation/message/OnStatLoss callback, no rollback. These are actual receiver rules, not an unconditional promise of two stages.',
    [unit(M+'006_MoveEffects_BattlerStats.rb',972,1013),unit(M+'006_MoveEffects_BattlerStats.rb',1305,1344),unit(M+'004_Move_BaseEffects.rb',173,193),unit('Data/Scripts/011_Battle/002_Battler/005_Battler_StatStages.rb',1,387)])
add('Shadow trapping receiver',
    'TrapTargetInBattle MagicCoat-capable. Status move rejects alreadyMeanLook and configured Ghost immunity, else writes MeanLook=user.index before message. Damaging additional effect separately rejects fainted/substitute/alreadytrapped/Ghost. An exception in later message doesnot restore write. Switching/flee caller policy beyond this complete class is separately OPEN.',
    [unit(M+'013_MoveEffects_SwitchingActing.rb',316,344)])
add('Additional effect chance and real hit receiver',
    'Complete pbAdditionalEffectChance: active ShieldDust without moldBreaker returns0, explicit positive argument else stored @addlEffect, >100 returns directly, qualifying SereneGrace or Rainbow doubles once, DEBUG+CTRL sets100. Complete pbProcessMoveHit checks user/accuracy and commits hit/damage/main effects before additional loop; SheerForce suppresses loop, calcDamage0 skips, chance<=0 skips, random100<chance dispatches actual additional effect. All inner ability/item callbacks and action-level outer gates retain their own OPEN scope.',
    [unit(M+'003_Move_UsageCalculations.rb',489,499),unit('Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb',583,761)])
add('Shadow exact effect-code negative control',
    'Raw SHADOWSHED FunctionCode RemoveAllScreens is not registered by an exact Battle::Move::RemoveAllScreens class in fixed Data/Scripts. The actual RemoveAllScreensAndSafeguard class is a different name. BattleMove.from_pokemon_move resolves named class else Unimplemented; that class fails status move while damaging fallback can behave as generic damage. Exact-name source-search negative evidence excludes dynamic plugins/redefinitions and doesnot itself prove execution/PP refund.',
    [unit('PBS/Shadow Pokémon backup/moves_shadow_pkmn.txt',190,201),unit(M+'001_Battle_Move.rb',1,201),unit(M+'004_Move_BaseEffects.rb',1,18),unit('Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb',383,418)])
add('All25 stored-nature heart amount tuples',
    'All25 exact tuples battle/call/walking/scent match formal table. switch selects stored @nature, never nature_for_stats override. Missing nature tuple fallback100/300/100/100; only scent multiplies, unknown method raises, adjustHeart clamps0..max only whileShadow. Complete original221 source and exact40–95 reread support this finite data/control relation.',
    [unit('Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb',40,95)])
facts['schema']='gr8-bounded-pbs-source-facts/v7';facts['utc']=U;facts['supersedes_finite_source_packet']='bounded-pbs-facts.v6.json; original immutable';facts['mandatory_companions']=['mandatory-locator-clarification.v1.json','mandatory-item-schema-clarification.v1.json'];save('bounded-pbs-facts.v7.json',facts)

# Actual formal/source values were read before this consistency-only expansion.
old=json.loads((P/'reverse-mapping.json').read_text());save('reverse-mapping.v4.frozen.json',old)
F='deliverables/final-specification-set/pokemon-rules/wp23-shadow-data-and-vectors.md'
lines=(B/F).read_text().splitlines();raw=json.loads((P/'typed-record-facts.v1.json').read_text());new=[]
def atom(id,line,assertion,sources,refs):
 new.append(dict(id=id,formal=dict(path=F,lines=[line,line]),assertion=assertion,sourcefact_ids=refs,source_units=sources,actual_reader='/root/pbs_creature_current_cloud',status='FINITE_ASSERTION_MATCHED_SOURCE_STATIC',qualification='Exact authored coordinate/complete stated premise only; backup is not defaultactive; neither fullcombat nor native behavior pass.'))
for r in raw['paths'][1]['records']:
 fields={f['key']:f for f in r['fields']};fn=fields['FunctionCode']['original_value'];fid=r['id'];fl=next(i+1 for i,s in enumerate(lines) if s.startswith('| '+fid+' |'))
 cells=[c.strip() for c in lines[fl-1].split('|')[1:-1]];assert cells==[fid,fn]
 atom('PCR-SHADOWMOVE-'+fid+'-FUNCTION',fl,f'{fid} authored FunctionCode={fn}',[unit(raw['paths'][1]['path'],fields['FunctionCode']['line'],fields['FunctionCode']['line'])],['PC-F060','PC-F061','PC-F062','PC-F063','PC-F065'])
 atom('PCR-SHADOWMOVE-'+fid+'-TYPE',205,f'{fid} authored Type=SHADOW',[unit(raw['paths'][1]['path'],fields['Type']['line'],fields['Type']['line'])],['PC-F060'])
for r in raw['paths'][0]['records']:
 fields={f['key']:f for f in r['fields']};fid=r['id'];fl=next(i+1 for i,s in enumerate(lines) if s.startswith('| '+fid+' |'));cells=[c.strip() for c in lines[fl-1].split('|')[1:-1]]
 expected={'FieldUse':'OnPokemon','BattleUse':'OnPokemon' if fid!='TIMEFLUTE' else '无','Price':str(fields['Price']['interpreted_value']),'Scent':'无（未声明 Flags）'}
 assert cells==[fid,expected['FieldUse'],expected['BattleUse'],expected['Price'],expected['Scent']]
 for key in ['FieldUse','BattleUse','Price','Scent']:
  rr=r['source_range'] if key in ['Scent','BattleUse'] and key not in fields else [fields[key]['line'],fields[key]['line']]
  atom('PCR-SHADOWITEM-'+fid+'-'+key,fl,f'{fid} {key}={expected[key]}',[unit(raw['paths'][0]['path'],*rr)],['PC-F001','PC-F002'])
 atom('PCR-SHADOWITEM-'+fid+'-CONSUMABLE',237,f'{fid} no KeyItem/important flag and omittedConsumable→true',[unit(raw['paths'][0]['path'],*r['source_range']),unit('Data/Scripts/010_Data/002_PBS data/006_Item.rb',73,270)],['PC-F001','PC-F002'])
shadow=(R/'Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb').read_text().splitlines()
for fl in range(9,34):
 cells=[c.strip() for c in lines[fl-1].split('|')[1:-1]];name=cells[0];values=list(map(int,cells[1:]));sl=next(i+1 for i,s in enumerate(shadow) if re.search(r':'+name+r'\s*=>',s));m=re.search(r'\[([^]]+)\]',shadow[sl-1]);sv=[int(v.strip()) for v in m.group(1).split(',')];assert values==sv
 for j,key in enumerate(['battle','call','walking','scent']):atom(f'PCR-SHADOW-NATURE-{name}-{key}',fl,f'Storednature{name} {key} amount={values[j]}',[unit('Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb',sl,sl),unit('Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb',76,92)],['PC-F066'])
assert len(new)==156,len(new)
old['schema']='gr8-pbs-current-reverse/v5';old['utc']=U;old['clauses'].extend(new);old['new_shadow_addendum_atoms']=156;old['atom_denominator_frozen_so_far']=len(old['clauses']);old['supersedes']='reverse-mapping.v4.frozen.json; old156zero, original preserved';save('reverse-mapping.json',old)
for name in ['bounded-pbs-facts.v7.json','reverse-mapping.json']:
 b=(P/name).read_bytes();print(name,len(b),hashlib.sha256(b).hexdigest())
print('utc',U,'newatoms',len(new),'allatoms',len(old['clauses']),'sourcefacts',len(facts['facts']))
