import json,pathlib,hashlib,subprocess,datetime
r=pathlib.Path(__file__).resolve().parent
report=r.parents[2]
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
def rawgit(path):return subprocess.check_output(['git','show',R+':'+path],cwd='/workspace/pokemon-essentials')
def sha(b):return hashlib.sha256(b).hexdigest()
def save(n,d): (r/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def identity(p):
 b=p.read_bytes();return {'path':p.name,'bytes':len(b),'sha256':sha(b)}
d=json.loads((r/'trainer-types72-selected-exact.v2.json').read_text())
provider=report/d['source_packet']['path']
pb=provider.read_bytes();assert len(pb)==303465 and sha(pb)=='848bc06ab5f79aa87f3a89f7d90da81e905ac26f5ca524318865988a5ae832a7'
unitchecks=[]
for u in d['complete_source_units']:
 s=u['source_identity'];b=rawgit(s['path']);a,z=u['complete_unit_range'];body=''.join(b.decode().splitlines(keepends=True)[a-1:z])
 assert len(b)==s['bytes'] and sha(b)==s['sha256'] and body==u['complete_body']
 blob=subprocess.check_output(['git','rev-parse',R+':'+s['path']],cwd='/workspace/pokemon-essentials',text=True).strip();assert blob==s['git_blob']
 unitchecks.append({'identity':s,'complete_unit_range':[a,z],'exact_body_equal_fixedR':True,'actual_full_unit_read':('6c3b70' if s['path'].endswith(('001_Trainer.rb','003_Utilities_BattleAudio.rb','001_GameData.rb')) else 'b57cba')})
g=d['complete_primary_record_group'];b=rawgit(g['path']);s=g['identity'];assert len(b)==s['bytes'] and sha(b)==s['sha256'];lines=b.decode('utf-8-sig').splitlines()
for rec in g['records']:
 assert lines[rec['source_range'][0]-1].strip()=='['+rec['id']+']'
 for f in rec['fields']:
  key,value=lines[f['line']-1].split('=',1);assert key.strip()==f['key'] and value.strip()==f['original_value']
assert len(g['records'])==72
# Literal identity/range checking only; this is not an importer, typed parser, or business model.
p='Data/Scripts/010_Data/001_GameData.rb';b=rawgit(p);body=''.join(b.decode().splitlines(keepends=True)[234:242])
generic={'source_identity':{'repo':'/workspace/pokemon-essentials','commit':R,'path':p,'bytes':len(b),'sha256':sha(b),'blob':'ccfd971a29b3bab107e2da6865ac0050ed3256b0'},'complete_unit_range':[235,242],'complete_body':body,'actual_read':['79bad9','ae4420'],'meaning':'Generic get_property_for_PBS startsnil; onlyschema-key+respond_to calls mapped getter; false or emptyArray is omitted asnil; allotherreturns preserved. TrainerType override mapsID toSectionName and suppressesSkillLevel onlywhen the returned value equals effectivebaseMoney. Dynamic getter failure propagates; no whole exporter/compiler/runtime credit.'}
receipt={'schema':'facility-trainer-type72-full-field-and-finite-producer-reception/v2','utc':utc,'actual_reader':'/root/facility_atomic_completion_cloud','original_actual_reader':'/root/pbs_creature_current_cloud','fixedR':R,'scope':'All72 complete group0TrainerType records, allraw/typed/default/omitted fields and originalbinding metadata; exactlyfourcompletefacts, sixcompleteunits, sixcompleteconsumermeanings andtwofullmandatorycompanions. Doesnotadopt group1twentyTrainerrecords orotherfacts/meanings/units.','source_packet':d['source_packet'],'exact_selection':identity(r/'trainer-types72-selected-exact.v2.json'),'lossless_view':dict(identity(r/'trainer-types72-complete-fields.view.txt'),lines=79,actual_full_read='0be56b all79lines',inverse_each_complete_record_equal=True,metadata_check='4b1f4d'),'actual_object_read':{'envelope':'46f213 envelopecompletebeforeunrelatedunitoutputtruncation','fourfacts':'b1f988 andae4420','sixmeanings':'b57cba','companions':'b1f988 bothcomplete','sixsourceunits':unitchecks},'complete_primary_group_identity':s,'records':72,'all_raw_field_line_values_equal_fixedR':True,'additional_complete_generic_export_unit':generic,'accepted_finite_meanings':[
 {'id':'FAC-TTYPE-01','meaning':'Name/Gender/BaseMoney/Skill/Flags/allthreeBGM completevalues andallomissions receivedfor72. Constructor fallbackNameUnnamed,Gender2,BaseMoney30,Skill||effectiveBaseMoney,flags[]; valid0remains0. No binaryregistryorder inferencefromPBS firstrecord.'},
 {'id':'FAC-TTYPE-02','meaning':'LiveTrainerType.facadegetters andcase-insensitivehas_flag? remain distinctfrom authoredPBS recordstrings. All72Flags[]/IntroBGMnil inthisfixedgroup do notassert allotherregistries/plugins, nor override Player trainer_type getter.'},
 {'id':'FAC-TTYPE-03','meaning':'Generatedtrainer weights/namegender depend on actualBaseMoney/Gender andspecies base-data keys. YOUNGSTER currentrecordBaseMoney16/Skill16/Male0, but ordinaryallocationloop remains unbounded andhasnobreak. All200YOUNGSTER shortcut is separatelyconditional.'},
 {'id':'FAC-TTYPE-04','meaning':'Ordinary battle/victory arrays retainlasttruthytypefield; emptystring overwritesearliermusic thenfallsback, whileFromType directlyreturnstruthyrawfield includingemptystring. Preloadclonefirst. Intro memorization/request prefixesreceived; nativeaudiosuccessNOT_EXECUTED.'},
 {'id':'FAC-TTYPE-05','meaning':'AITrainer existingtrainer uses live.skill_level and copiesflags, applies>0/32/100automaticflags thenAntiXremoval; threshold48alsoindependent. Wild3flag branch isinitialnoTrainer-onlyconditional. Sourceownfull100L actuallyread; 898/339primaryrecords are providerpremises andnottransferredtoFAC bythisfact.'},
 {'id':'FAC-TTYPE-06','meaning':'Owner.new_from_trainer obtains currentid/name/gender/language andvalidates thenconstructs; referencealias/name andliteralUnknown2 preserved. CompleteOwnerunit received; no alllifecycle callbacks/publicfutureAPImandate.'}
 ],'truncated_output_handling':[{'receipt':'f9bbe7','status':'TRUNCATED_NOT_FULL_READ;laterexactselection/viewandnamedunitreadsestablishonlyscopeabove'},{'receipt':'46f213','status':'unitmetadata/bodysectiontruncated; repairedsixnamedunitreads b1f988/b57cba/6c3b70; envelopefullyvisible'}],'OPEN':['All20normalTrainergroup1records andother8facts/9meanings/6units notadoptedfrom303465Bpacket.','Compiler enumeration/localization resources, complete Player/AI/catch/Bag/media/world semantics notgrantedbyselectedsourceFULL.','453species/649constructedclasses/2732provenances andfiniteeligibilitycertificateproof input joins remainOPEN. All1600trainer/all1888cupliteralfields reception isnotqualificationproof.','964formal seed childexhaustiveness and202external joins remainOPEN; true overall atomicdenominator null.'],'actual_new_contexts':0,'new_votes':0,'new_required':0,'new_optional':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True,'wholeFAC_complete':False}
save('trainer-types72-reception.v2.json',receipt)
led=json.loads((r/'reading-ledger.json').read_text());led['updated_utc']=utc;led['v2_exact_receptions'].append({'utc':utc,'packet':'trainer-types72-reception.v2.json','source':d['source_packet'],'complete_group':72,'facts':4,'units':6,'meanings':6,'companions':2,'receipts':['0be56b','b1f988','b57cba','6c3b70','ae4420'],'qualification':'Onlyexactselectedscope; full72fieldslosslessview andsixunitsactualread; no20Trainergroup1/all303kFULL orprimarytrait/graphproof inherit.'});save('reading-ledger.json',led)
pr=json.loads((r/'progress.json').read_text());pr['updated_utc']=utc;pr['trainer_type72_complete_finite_reception']='trainer-types72-reception.v2.json';save('progress.json',pr)
inter=json.loads((r/'interfaces.json').read_text());inter['updated_utc']=utc
for x in inter['interfaces']:
 if x['id']=='FAC-I08':x['trainer_type_primary_finite_reception']='trainer-types72-reception.v2.json complete72records/allfields and4facts6units6meanings2companions; no649classes/453species/2732provenances or proofclosure.'
save('interfaces.json',inter)
print(json.dumps(identity(r/'trainer-types72-reception.v2.json')))
