"""Actual six complete type input bodies, not semantic credit from identical blobs."""
from pathlib import Path
import datetime,hashlib,json
P=Path(__file__).resolve().parent;RR=P.parent.parent;R=Path('/workspace/pokemon-essentials');NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
paths=['PBS/types.txt']+[f'PBS/Gen {g} backup/types.txt' for g in [5,6,7,8]]+['PBS/Shadow Pokémon backup/types_shadow_pkmn.txt']
lib=json.loads((RR/'tasks/coverage_acceptance_incremental/dispatch/kernel_atomic_reception.readset.json').read_text())['all_fixed_R432_F131_identity_library'];ledger=json.loads((P/'reading-ledger.json').read_text());files=[]
for path in paths:
 raw=(R/path).read_bytes();fixed=next(x for x in lib if x['repo']=='R' and x['path']==path);assert len(raw)==fixed['bytes'] and hashlib.sha256(raw).hexdigest()==fixed['sha256']
 records=[];current=None
 for no,line in enumerate(raw.decode('utf-8-sig').splitlines(),1):
  if line.startswith('['):current={'id':line[1:-1],'header_line':no,'all_explicit_fields':{}};records.append(current)
  elif '=' in line:
   k,v=[s.strip() for s in line.split('=',1)];current['all_explicit_fields'][k]=v
 want=1 if 'Shadow' in path else 18 if 'Gen 5' in path else 19;assert len(records)==want
 files.append({'fixed_identity':fixed,'actual_reader':'/root/kernel_atomic_reception','complete_body_actually_read':'1cd455 no truncation, every six listed path independently printed in complete form','full_text':raw.decode('utf-8-sig'),'all_complete_records':records,'record_count':want})
 ledger['records'].append({'repo':'R','path':path,'status':'FULL_READ','reader':'/root/kernel_atomic_reception','whole_file_read':True,'range':[1,len(raw.decode('utf-8-sig').splitlines())],'fixed_identity':fixed,'actual_read_evidence':['1cd455','io/types-default-and-all-four-generation-backups-full.json'],'scope':'All records/all explicit fields in actual file; not default active use of backup or whole battle/type behavior.'})
ledger['updated_utc']=NOW;(P/'reading-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
facts=[
 'Default and Gen6/7/8 each19 records NORMAL,FIGHTING,FLYING,POISON,GROUND,ROCK,BUG,GHOST,STEEL,QMARKS,FIRE,WATER,GRASS,ELECTRIC,PSYCHIC,ICE,DRAGON,DARK,FAIRY in that source order, IconPosition0–18.',
 'Gen5 has18 same first18 IDs/positions, no FAIRY. Shadow optional file supplies only SHADOW nameShadow/IconPosition19/IsSpecialType true/Resistances SHADOW.',
 'Every record Name/IconPosition and every ordered Weaknesses/Resistances/Immunities list is retained in per-record transcription; no omitted field projected away.',
 'QMARKS actual name??? and IsPseudoType true; it is a real record, not a missing-entry sentinel. It omits IsSpecialType and all three effectiveness lists.',
 'FIRE,WATER,GRASS,ELECTRIC,PSYCHIC,ICE,DRAGON,DARK,FAIRY explicitly IsSpecialType true in default/newer tables; earlier physical group omits flag. Gen5 has first8 of those, Shadow its separate true flag.',
 'Gen5 STEEL resists DARK and GHOST and omits FAIRY; newer STEEL drops DARK/GHOST and includes FAIRY. Gen5 has no FAIRY entries in weakness/resistance lists.',
 'Newer FAIRY weaknesses POISON/STEEL, resists FIGHTING/BUG/DARK, immune DRAGON; newer POISON/FIRE/STEEL resist FAIRY, FIGHTING/DRAGON/DARK weak FAIRY. Other exact lists and list order stay as complete per-record input.',
 'NORMAL immune GHOST; FLYING immune GROUND; GROUND immune ELECTRIC; GHOST immune NORMAL/FIGHTING; STEEL immune POISON; DARK immune PSYCHIC. Order differences in Gen5 arrays retained rather than sorted away.',
 'Source GameData::Type schema/constructor owns omitted false/empty-list defaults and effectiveness queries; complete definition already actually own read. Record values here do not themselves execute compilation or battle matching.',
 'Generation backups and Shadow optional source are not activated merely by MECHANICS_GENERATION. Actual selected compiler file list/defaultinput and explicit optional inclusion matter; fixed currentdata need not match every alternative.',
 'Whole compile clear/register/save order and directwb failure prefixes remain separate complete Compiler facts. Inputtable has no own cancel or transaction. No target/native test run.',
]
obj={'schema':'kernel-types-six-complete-inputs/v1','utc':NOW,'reader':'/root/kernel_atomic_reception','all6files':files,'complete_record_total':sum(x['record_count'] for x in files),'manual_semantic_facts':facts,'actual_read_IO':'io/types-default-and-all-four-generation-backups-full.json','credit':'All6 actual complete texts/fields personally read in1cd455. Parsing is faithful transcription/navigation and not an auto-generated semantic PASS. FullType/Compiler definitions independently personally read previously; not all battle/UI/domain consumers accepted.','target_execution':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED','new_finding_context_vote_required':0}
out=P/'types-six-complete-records-contribution.v1.json';out.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n');raw=out.read_bytes();print(json.dumps({'utc':NOW,'files':6,'records':obj['complete_record_total'],'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'ownPBSfull':19,'remainingPBS':54}))
