"""Record completed manual joins/current scope, without new semantic reading."""
import datetime
import json
from pathlib import Path
B=Path(__file__).resolve().parent
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def load(n): return json.loads((B/n).read_text())
def write(n,d): (B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
a=load('manual-atomic-clauses.json');rows=a['records'];index={r['id']:r for r in rows}
groups=[
 (['KAR-EVENT-ARITY','KAR-EVENT-TRIGGER2','KAR-EVENT-NAMED-REPLACE','KAR-EVENT-FAIL-PREFIX','KAR-HANDLER-EXACT-FIRST','KAR-HANDLER-REMOVE','KAR-HANDLER-CLEAR','KAR-HANDLER-COPY'],'COMPLETE_PRIMITIVE_AND_FINITE_ACTUAL_CALLER_SCOPE','SFR12/GamePlayer/micro/partner/trainer/interpreter'),
 (['KAR-PBS-TOP-DISCOVERY','KAR-PBS-OPTIONAL-SKIP'],'COMPLETE_DISCOVERY_OPTIONAL_INPUT_SCOPE','SFR06/Shadow3completefixture'),
 (['KAR-INTL-CURRENT-LAYERS','KAR-INTL-EMPTY-HIT'],'COMPLETE_LOOKUP_FINITE_DISPLAY_SCOPE','SFR25/media-complete-body/UI/Slot'),
 (['KAR-DEPRECATION-PERUSE'],'COMPLETE_ALIAS_DEFINITION_NO_DEFAULT_CALLER_INVENTED','SFR21'),
 (['KAR-HTTP-CONSTRUCT-FIRST','KAR-HTTP-WRITE-PREFIX'],'COMPLETE_HTTP_SOURCE_REAL_MG_CALLER_SCOPE','SFR19/mg-http-finite-reception+mandatoryLoadbinding'),
 (['KAR-STATS-DERIVED-TYPES'],'COMPLETE_LAZY_GETTER_AND_FINITE_QUERY_SCOPE','SFR16/GameStats/Interpreter/StatsUI'),
 (['KAR-WP04-MAP-SAVE-SWALLOW'],'TRIAGE_ONLY_NOT_REQUIRED_COMPLETE_WP75_OWNER_FINITE_JOIN','developer-wp75-map-filename-finite-reception/SFR11/31'),
 (['KAR-WP06-WPT-095','KAR-WP06-WPT-096'],'COMPLETE_FINITE_LOTTERY_NATIVE_RNG_UNEXECUTED','root-lottery-finite-reception; noargreseednotrestore'),
 (['KAR-WP09-SLOT10'],'COMPLETE_DISTINCT_VARIABLE_CALLER_CONTRACTS','SFR14/16 Lottery/Timer/Interpreter'),
 (['KAR-WP09-MAP10','KAR-WP09-MAP11'],'CURRENT_STATIC_MAP_PROJECTION_HISTORY_NOT_INHERITED','OwnMapFactory/Overworld/StartGame; GR3-M03-004qualificationUNVERIFIEDnotreused'),
 (['KAR-WP10-PHONE04'],'COMPLETE_CONVERSION_PHONE_PREFIX_SCOPE','SFR29/Phone706/Conversion420; requestaswritten,noPhone.getsuccessinferred')
]
deltas=[]
for ids,status,evidence in groups:
    for aid in ids:
        r=index[aid];deltas.append({'id':aid,'old':r.get('reception_status'),'current':status,'operative_join':evidence})
        r.setdefault('previous_reception_status_before_final_scope',r.get('reception_status'))
        r.update(reception_status=status,current_scope_join=evidence)
raw_ids=[r['id'] for r in rows if r.get('reception_status','').startswith(('OPEN_RAW_HISTORICAL','OPEN_EXACT_HISTORICAL'))]
assert raw_ids==['KAR-WP06-WPT-062','KAR-WP07-IO-084','KAR-WP07-IO-085','KAR-WP07-IO-086']
for aid in raw_ids:
    index[aid]['current_evidence_qualification']='ORIGINAL_RAW_EXECUTION_UNVERIFIED; currentSOURCE_STATIC/DERIVED_VECTOR qualificationaccepted; no oldrun inherited. Doesnotblockboundedcurrentstaticcontract perrootlatestinstruction.'
a['current_primary_signature']={'status':'QUALIFIED_CURRENT_PRIMARY_SOURCE_STATIC_COMPLETE','utc':NOW,'scope':'Exactly13frozenprimaryformal/allcurrentnecessarysource/premise/finiteconsumermeaning; notwholeglobaldomain','independent_claim_occurrences':4776,'working_records_with16aliases':4792,'historical_raw_unverified_atoms':raw_ids,'current_declared_unknowns':'Native/Demo/combination/eventcaller/dynamicglobalcoverage limits areaccepteddeclaredqualifications, not fakeunreadmaterials or proofnoneexist.','legacy_open_label_policy':'OriginaldownstreamOPENlabels retainedwhereoutsidecurrentclaimscope. Namedcurrentmissingedges haveexplicitnewjoins. No allfuturecallback/allrawPBSobligationinvented.','business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'}
write('manual-atomic-clauses.json',a)
write('atomic-final-bounded-static-join-differences.v1.json',{'schema':'KAR-final-bounded-static-join-differences.v1','utc':NOW,'new_explicit_finite_scope_joins':deltas,'historical_raw_qualifications':raw_ids,'signature':a['current_primary_signature']})
old=load('old-locator-disposition.json');count=0
for r in old['records']:
    if r['disposition'].startswith(('LAYOUT_','TABLE_')): continue
    assert r.get('explicit_manual_child_ids') or r.get('manual_child_assertions')
    r.setdefault('previous_checkpoint_disposition',r['disposition'])
    r.update(disposition='COMPLETE_MANUAL_CURRENT_FORMAL_CHILD_MEANINGS_WITH_BOUNDED_PER_CHILD_DISPOSITION',current_scope_signature='manual-atomic-clauses.json#/current_primary_signature',pending='Onlyexactperchilddeclaredhistorical/native/outside-domainqualification, not unfinishednamedcurrentmeaning.')
    count+=1
assert count==1723 and len(old['records'])==2219
old.update(updated_utc=NOW,current_primary_scope='1723semanticlocators bindalreadyhandreconstructedcompletecurrentclaims;496exactlayout/tablepurposes retained. Thisrecordscompletedmanualwork/necessaryjoins, notmerecount/locatorpresence.')
write('old-locator-disposition.json',old)
g=load('coverage-gaps.json');matrix=[]
for path in g['PBS_remaining_paths']:
    if path=='PBS/pokemon.txt': purpose='CompleteBULBASAURselectedproducer+common schema/default foronlyspecificnonuniformstatsliteral; other897notadopted.'
    elif 'battle_tower_' in path or '/cup_' in path: purpose='Current5facilitylists10explicitfileexistence vs2unreferencedFancy; noallrecordvaluesclaimedinprimary.'
    elif path.endswith(('items.txt','moves.txt')): purpose='CompletequalifiedPBSbattleproducerfieldcontracts/defaults+candidateexistence; noallliteralvaluesclaim.'
    elif path.endswith(('pokemon_forms.txt','pokemon_metrics.txt')): purpose='Complete source schema/inheritance/query/cloning/export conditionalvectors; noall339/674literalclaim. Backupcandidateexistence/manualselectiononly.'
    else: purpose='Backup9filenames/existence/top-levelnonrecursive/manualselection/U03boundary only; noallrecordcompletenessclaim.'
    matrix.append({'path':path,'own_raw_FULL':False,'current_primary_necessary_scope':purpose,'scope_disposition':'NECESSARY_CURRENT_PRIMARY_VALUE_OR_EXISTENCE_SCOPE_RECEIVED; wholeliteralnotclaimed','material_available':True})
assert len(matrix)==37
write('pbs-necessary-primary-scope.v1.json',{'schema':'KAR-necessary-primary-PBS-scope.v1','utc':NOW,'root_scope_instruction':'Latestrootacceptsactualformalnecessarycompleteproducerobjects/commonpremises, noblindallliteralreread.','own_PBS_FULL':36,'physical_paths_not_own_FULL':matrix,'necessary_selected_value_receipt':'received/pcr-bulbasaur-finite-reception.v1.json','qualified_field_receipt':'received/pbs-battle-qualified-producer-fields.v1.json+mandatorycountclarifier','default_facility_lists':'Alreadyown25L5completerecords/10uniqueexplicitpaths,2topFancyunreferenced; completecompiler/discovery actualread.','no_inheritance':'No otherRAW/FULL becomesownFULL,noallcombinedPBS/runtimePASS.','business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'})
print(json.dumps({'utc':NOW,'extra_specific_joins':len(deltas),'semantic_locators':count,'layout_purposes':496,'raw_history_UNVERIFIED':raw_ids,'PBS_necessary_scope_matrix':37}))
