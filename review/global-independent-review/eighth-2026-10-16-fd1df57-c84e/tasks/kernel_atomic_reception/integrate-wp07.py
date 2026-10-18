"""Attach hand-authored semantic claims to exact old locators; no target execution."""
from pathlib import Path
import csv
import datetime
import hashlib
import json

BASE=Path(__file__).resolve().parent
ROOT=Path('/workspace/pokemon-essentials-clean-room')
R=Path('/workspace/pokemon-essentials')
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
FORMALS={'IO':'deliverables/final-specification-set/generic-kernel/wp07-diagnostics-files-http.md','DP':'deliverables/final-specification-set/generic-kernel/wp07-deprecation-appendix.md'}
FILES={
 'file':'Data/Scripts/001_Technical/002_Files/001_FileTests.rb',
 'mixin':'Data/Scripts/001_Technical/002_Files/002_FileMixins.rb',
 'http':'Data/Scripts/001_Technical/002_Files/003_HTTP_Utilities.rb',
 'error':'Data/Scripts/001_Technical/001_Debugging/003_Errors.rb',
 'debug':'Data/Scripts/001_Technical/001_Debugging/001_PBDebug.rb',
 'console':'Data/Scripts/001_Technical/001_Debugging/002_DebugConsole.rb',
 'deprecation':'Data/Scripts/001_Technical/001_Debugging/005_Deprecation.rb',
 'main':'Data/Scripts/999_Main/999_Main.rb',
}
def source_for(unit):
 if unit.startswith('history-'):return []
 if unit.startswith('FileInputMixin') or unit.startswith('FileOutputMixin') or unit=='StringInput.each_byte':return ['mixin']
 if unit.startswith('Dir.') or unit.startswith('StringInput.') or unit.startswith('RTP.') or unit in ['safeGlob','pbRgssExists?','pbRgssOpen','pbGetFileChar','pbGetFileString','pbTryString','pbResolveBitmap','pbBitmapName','pbResolveAudioSE','read-failure-boundary']:return ['file']
 if unit=='deprecated-file-wrappers':return ['file','deprecation','console']
 if unit.startswith('pbDownload') or unit.startswith('pbPost') or unit.startswith('http-'):return ['http']
 if unit.startswith('pbGetException') or unit.startswith('pbPrintException') or unit=='error-classes' or unit=='pbCriticalCode':return ['error']
 if unit.startswith('main'):return ['main','error']
 if unit.startswith('PBDebug'):return ['debug','error']
 if unit.startswith('Kernel.echo') or unit.startswith('Console.'):return ['console']
 if unit.startswith('Deprecation.') or unit.startswith('Module.deprecated'):return ['deprecation','console','error']
 if unit=='diagnostic-layer-boundary':return ['debug','console','error']
 return []
ledger_path=BASE/'reading-ledger.json';ledger=json.loads(ledger_path.read_text());full={x['path'] for x in ledger['records'] if x.get('status')=='FULL_READ' and x.get('repo')=='R'}
identity=[]
for path in FILES.values():
 raw=(R/path).read_bytes();assert path in full,path
 identity.append({'path':path,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'file_lines':len(raw.decode('utf-8-sig').splitlines()),'actual_source_reader':'/root/kernel_atomic_reception','actual_full_read_evidence':'Existing77-source real read, plus complete IO rereads wp07-*.json; equality does not generate reading credit.'})
records=[];text={k:(ROOT/v).read_text().splitlines() for k,v in FORMALS.items()}
with (BASE/'wp07-manual-atoms.tsv').open() as stream:
 for row in csv.DictReader(stream,delimiter='\t'):
  line=int(row['formal_line']);code=row['formal'];unit=row['source_unit'];src=[{'path':FILES[k],'complete_named_unit':unit,'actual_reader':'/root/kernel_atomic_reception','whole_file_actually_read':True,'identity_ref':FILES[k],'navigation':'Named definition in actual complete source, not a mechanically assigned full-file semantic range.'} for k in source_for(unit)]
  if unit=='history-http-original':src=[{'actual_full_records_received':['received/history-http-r7-qualified-record26.json','received/history-http-original-record3.json'],'original_raw_probe_files_read':False,'scope':'Complete original contract/counterreview/criteria read only, no inherited execution/current-PASS.'}]
  records.append({'id':'KAR-WP07-'+row['id'],'formal':{'path':FORMALS[code],'lines':[line],'exact_text':text[code][line-1]},'assertion':row['assertion'],'source_complete_units':src,'source_status':row['status'],'reception_status':row['status'],'normal_failure_cancel_partial':row['premise_and_failure_boundary'],'premise':'FixedB8/R. Only actual named complete definition and specific provider/input premises; target/native execution NOT_EXECUTED. Callable helper does not imply a default business consumer.','original_fact_refs':[row['original_fact']] if row['original_fact'] else [],'receiver':'/root/kernel_atomic_reception','target_behavior':'NOT_EXECUTED','update_started':False})
assert len(records)==132 and len({r['id'] for r in records})==132
(BASE/'wp07-manual-atoms.json').write_text(json.dumps({'schema':'kernel-wp07-hand-authored-semantic-children-v1','utc':NOW,'working_children':132,'global_and_chapter_atomic_denominator_frozen':False,'source_identities':identity,'records':records,'remaining':'Exact original history raw probes, all applicable business consumers and remaining formal scope/semantic refinement continue; no global or locator-wide acceptance.'},ensure_ascii=False,indent=2)+'\n')
mainp=BASE/'manual-atomic-clauses.json';main=json.loads(mainp.read_text());newids={r['id'] for r in records};main['records']=[r for r in main['records'] if r['id'] not in newids]+records;mainp.write_text(json.dumps(main,ensure_ascii=False,indent=2)+'\n')
oldp=BASE/'old-locator-disposition.json';old=json.loads(oldp.read_text())
for r in old['records']:
 children=[x['id'] for x in records if x['formal']['path']==r['path'] and r['range'][0]<=x['formal']['lines'][0]<=r['range'][1]]
 if children:r['manual_child_assertions']=children;r['disposition']='PARTIAL_EXPLICIT_MANUAL_CHILD_ASSERTIONS_RECONCILED';r['semantic_acceptance']='ONLY_NAMED_CHILD_STATUS_AND_FULL_PREMISE; NO_LOCATOR_WIDE_PASS';r['pending']='Remaining nonchild meanings/consumer/history/negative premises continue; row is not an atomic denominator.'
oldp.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
sfp=BASE/'sourcefact-consumer-receptions.json';sf=json.loads(sfp.read_text())
for item in sf['records']:
 links=[r['id'] for r in records if item['fact_id'] in r['original_fact_refs']]
 if links:item['manual_atom_links']=sorted(set(item.get('manual_atom_links',[])+links));item['named_child_reception']='Only exact child statuses/premises accepted; retain original unsupported portions and precise remaining consumers.'
assert next(x for x in sf['records'] if x['fact_id']=='KER-F101')['status']=='PARTIALLY_UNSUPPORTED_OLD_RECORD_NOT_ADOPTED_AS_WRITTEN'
for name,path,provider,count in [('ROOT-LOTTERY-3-GROUPS','received/root-lottery-finite-reception.v1.json','/root',11),('CREA-LIFECYCLE-18','received/crea-lifecycle-ef79b21e-reception.json','/root/creature_a_atomic_reception',18),('MEDIA-ENCODING-4','received/media-serialized-encoding-87f3db06-reception.json','/root/resource_media_serialized_cloud',4)]:
 item={'id':name,'reception_path':path,'provider':provider,'complete_finite_fact_count':count,'source_credit':'Original real reader only; receiver sourceFULL added0','whole_domain_received':False};sf.setdefault('named_contributions',[]);sf['named_contributions']=[v for v in sf['named_contributions'] if v['id']!=name]+[item]
sf['updated_utc']=NOW;sfp.write_text(json.dumps(sf,ensure_ascii=False,indent=2)+'\n')
pp=BASE/'progress.json';progress=json.loads(pp.read_text());progress.update(updated_utc=NOW,explicit_manual_atom_subset=len(main['records']),wp07_explicit_manual_subset=132,old_locators_with_explicit_partial_child_binding=sum(bool(r.get('explicit_manual_child_ids') or r.get('manual_child_assertions')) for r in old['records']));cc=json.loads((BASE/'consumer-candidate-dispositions.json').read_text());progress['consumer_candidate_dispositions']=cc['summary'];pp.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':NOW,'new_children':132,'working_total':len(main['records']),'partial_locator_bindings':progress['old_locators_with_explicit_partial_child_binding'],'original_F101_rejection_preserved':True}))
