"""Three actually read complete files; explicit manually checked record-field inventory."""
from pathlib import Path
import datetime,hashlib,json
P=Path(__file__).resolve().parent;RR=P.parent.parent;R=Path('/workspace/pokemon-essentials');NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
groups=[
 ('CHERIBERRY CHESTOBERRY PECHABERRY RAWSTBERRY ASPEARBERRY',3,15,2,5),
 ('LEPPABERRY ORANBERRY PERSIMBERRY',4,15,2,5),
 ('LUMBERRY',12,8,2,5),('SITRUSBERRY',8,7,2,5),
 ('FIGYBERRY WIKIBERRY MAGOBERRY AGUAVBERRY IAPAPABERRY',5,10,1,5),
 ('RAZZBERRY BLUKBERRY NANABBERRY WEPEARBERRY PINAPBERRY',2,35,2,10),
 ('POMEGBERRY KELPSYBERRY QUALOTBERRY HONDEWBERRY GREPABERRY TAMATOBERRY',8,8,1,5),
 ('CORNNBERRY MAGOSTBERRY RABUTABERRY NOMELBERRY',6,10,2,10),
 ('SPELONBERRY WATMELBERRY BELUEBERRY',15,8,2,15),
 ('PAMTREBERRY DURINBERRY',15,8,3,15),
 ('OCCABERRY PASSHOBERRY WACANBERRY RINDOBERRY YACHEBERRY CHOPLEBERRY KEBIABERRY SHUCABERRY COBABERRY PAYAPABERRY TANGABERRY CHARTIBERRY KASIBBERRY HABANBERRY COLBURBERRY BABIRIBERRY CHILANBERRY ROSELIBERRY',18,6,1,5),
 ('LIECHIBERRY GANLONBERRY SALACBERRY PETAYABERRY APICOTBERRY LANSATBERRY STARFBERRY',24,4,1,5),
 ('ENIGMABERRY MICLEBERRY CUSTAPBERRY JABOCABERRY ROWAPBERRY KEEBERRY MARANGABERRY',24,7,1,5),
]
expected={name:{'HoursPerStage':h,'DryingPerHour':d,'Yield':[a,b]} for names,h,d,a,b in groups for name in names.split()}
assert len(expected)==67
lib=json.loads((RR/'tasks/coverage_acceptance_incremental/dispatch/kernel_atomic_reception.readset.json').read_text())['all_fixed_R432_F131_identity_library'];ledger=json.loads((P/'reading-ledger.json').read_text())
files=[]
for gen in [6,7,8]:
 path=f'PBS/Gen {gen} backup/berry_plants.txt';raw=(R/path).read_bytes();fixed=next(x for x in lib if x['repo']=='R' and x['path']==path);assert len(raw)==fixed['bytes'] and hashlib.sha256(raw).hexdigest()==fixed['sha256']
 records=[];current=None
 for no,line in enumerate(raw.decode('utf-8-sig').splitlines(),1):
  if line.startswith('['):current={'id':line[1:-1],'header_line':no,'fields':{}};records.append(current)
  elif '=' in line:
   key,value=[s.strip() for s in line.split('=',1)];current['fields'][key]=[int(v) for v in value.split(',')] if key=='Yield' else int(value)
 assert len(records)==67 and {x['id']:x['fields'] for x in records}==expected
 files.append({'fixed_identity':fixed,'actual_reader':'/root/kernel_atomic_reception','actual_full_read_output':'330a93 complete1–336 each of three named files','IO':'io/gen6-gen7-gen8-berry-complete-records.json','all_records_with_all_fields':records,'manual_match':'All67 explicit IDs and Hours/Drying/Yield values visually read for EACH file, then compared to independently entered expected groups. Not reading by sameblob or fullrange metadata.'})
 ledger['records'].append({'repo':'R','path':path,'status':'FULL_READ','reader':'/root/kernel_atomic_reception','whole_file_read':True,'range':[1,336],'fixed_identity':fixed,'actual_read_evidence':['330a93','io/gen6-gen7-gen8-berry-complete-records.json'],'scope':'All67 complete records/allfields. Backup explicit selection only, not automatic MECHANICS_GENERATION load.'})
ledger['updated_utc']=NOW;(P/'reading-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
packet={'schema':'kernel-three-berry-backups-complete201-records/v1','utc':NOW,'reader':'/root/kernel_atomic_reception','files':files,'manually_entered_all67_field_values':expected,'finite_facts':['Gen6/7/8 each67 records with exactly HoursPerStage,DryingPerHour,Yield; all201 actual full records read separately.','Allthree exact ID/value sets agree, including Roseli18/6/1,5 and Kee/Maranga24/7/1,5; grouped table does not change source insertion order retained per file.','Gen6/7/8 backup data does not self-select by MECHANICS_GENERATION. Caller must explicitly supply selected file or replace ordinary default input; default compiler input remains PBS/berry_plants.txt.','Current schema/constructor/clear-register-save and directwb failure prefix retain previously own complete GameData::BerryPlant/Compiler/default131-record packet. This addendum supplies only previously unread three concrete backup recordsets.'],'source_definition_forward':'berryplant-definition-and-131-records-contribution.v1.json','common_premise':'Fixed R source, no override, selected path readable, schema/parser available; records values are source input, not proof compiler run, Item availability, world planting, elapsed thresholds, Bag/store/save or all berries successful.','failure_cancel_partial':'Before any compile no mutation from these files merely existing. Explicit compile clears registry then registers reached entries, and save can fail after registration or wb truncation. There is no local cancel in data.','new_finding_context_vote_required':0,'execution':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'}
out=P/'three-berry-backups-201-records-contribution.v1.json';out.write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n');raw=out.read_bytes();print(json.dumps({'utc':NOW,'files':3,'records':201,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'PBS_FULL':13,'PBS_remaining':60}))
