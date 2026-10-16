"""Apply explicit new finite joins and selected three-facet Stats refinement.

No inference of behavior from locators, hashes or whole-file reading counts.
"""
import collections
import datetime
import hashlib
import json
from pathlib import Path

B=Path(__file__).resolve().parent
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(n): return json.loads((B/n).read_text())
def write(n,x): (B/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def ident(n):
    raw=(B/n).read_bytes()
    return {'path':n,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

payload=read('manual-atomic-clauses.json')
atoms=payload['records'];byid={r['id']:r for r in atoms}
# Each of these new mappings was explicitly read and adjudicated in this turn.
joins=[
 ('KAR-SAVE-BOOT-EMPTY','KNOWN_REQUIRED_ROOT_KER002_BOUNDED','Existing root KER002 accepts empty-data boot gate; no longer pending rootclassification.','sourcefact-current-scope-reconciliation.v1.json','SFR28'),
 ('KAR-MIG-BAG-OLDKEEP','CURRENT_CONVERSION_AND_BAG_UI_JOIN_CLOSED','Retained old browser field survives singleobjectrerun; actualUIreads/writes currentposition, no oldfieldcleanup.','bag-localization-residual-new-joins.v1.json','KAR-BLR-F01–03'),
 ('KAR-LZ-DEBUG-AUTHOR-CHOICE','AUTHOR_MENU_COMPLETE_SOURCE_JOIN_CLOSED','Authorlanguage/coregame/mapmode gates received; independentplayerlanguage.','bag-localization-residual-new-joins.v1.json','KAR-BLR-F04'),
 ('KAR-LZ-DEBUG-EXPORT-CANCEL','AUTHOR_MENU_COMPLETE_SOURCE_JOIN_CLOSED','Every explicitcancel returnsbeforeextract request.','bag-localization-residual-new-joins.v1.json','KAR-BLR-F04'),
 ('KAR-LZ-DEBUG-EXPORT-NO-SWITCH','AUTHOR_MENU_COMPLETE_SOURCE_JOIN_CLOSED','Exportregistration makesno playerlanguage/currentstore assignment.','bag-localization-residual-new-joins.v1.json','KAR-BLR-F04'),
 ('KAR-LZ-IMPORT-MENU-FRAGMENT','AUTHOR_MENU_COMPLETE_SOURCE_JOIN_CLOSED','SelectedTextfragment mutatesinplace andexact Translatorcaller/defaultnamespace retained.','bag-localization-residual-new-joins.v1.json','KAR-BLR-F05'),
 ('KAR-EP-PLUGIN-NO-SAMPLE','FIXED_TRACKED_SAMPLE_ABSENCE_QUALIFICATION_RECEIVED','FixedR432trackedpaths containno Plugins sample/PluginScripts artifact; not universalhost/plugin absence.','sourcefact-current-scope-reconciliation.v1.json','SFR13; io/fixed-plugin-sample-census.json'),
 ('KAR-EP-PLUGIN-DEBUG-EXPORT','PBS_EXPORT_CROSSREFERENCE_PURPOSE_RECEIVED','Actualdebug PBScompile/exportcaller differsstartup; no pluginexportAPI invented fromnavigation.','bag-localization-residual-new-joins.v1.json','KAR-BLR-F06'),
 ('KAR-WP03-DESCR-AREA-NOHABITAT','ACTUAL_COMPLETE_AREA_METHOD_JOIN_CLOSED','Own302–402pointsanddrawmethods establishEncounter/Map/visiblepoint/shape, notHabitat; E03remainsInfo.','pokedex-area-residual-new-joins.v1.json','KAR-AREA-F01–02'),
 ('KAR-WP04-EVOLUTION-FIRST-PREDICATE','ACTUAL_FIRST_TRUTHY_RUNTIME_JOIN_CLOSED','Valid B,C sequence firstLevel>=16 returnsB undercompleteeligibility/filter/earlierdependencyconditions.','evolution-first-runtime-new-join.v1.json','KAR-EVO-FIRST-F01–02'),
 ('KAR-WP06-WPT-080','ACTUAL_FINITE_STATS_WRITERS_AND_QUALIFIED_COUNTS_RECEIVED','Allreceived finitewriterentries plusfourSafariContest/twotimesetters; categorycounts65do not certifyDemo/iffsuccess.','sourcefact-current-scope-reconciliation.v1.json','SFR16'),
 ('KAR-WP06-WPT-082','EXPLICIT_UNKNOWN_WRITER_BOUNDARY_RECEIVED','Unknownbattle_points_won source preserved asdeclaredqualification, not inventedNPC orunreadrequiredwriter.','sourcefact-current-scope-reconciliation.v1.json','SFR16'),
 ('KAR-WP06-WPT-103','EXPLICIT_NO_ESTABLISHED_DEFAULT_CALLER_BOUNDARY_RECEIVED','No demonstrateddefaultcaller is an evidenceboundary, not a theoremzero/allrandomunification; no extraexhaustivecallerclaim.','sourcefact-current-scope-reconciliation.v1.json','SFR15'),
 ('KAR-WP06-WPT-109','EXPLICIT_RECORDING_APPLICABILITY_LIMIT_RECEIVED','Capturedrecordreplaymethods do not proveallrandom/layout/versioninterceptions; this limitation isaccepted.','sourcefact-current-scope-reconciliation.v1.json','SFR15/SFR30'),
 ('KAR-WP06-WPT-124','ACTUAL_ENCOUNTER_SETUP_AND_VERSION_JOIN_CLOSED','OwnWildEncounters469/fivecompletefixtures/Areaeach_of_version connectglobalversion conditionalsetup; exactgates retained.','five-encounter-fixtures-consumers-contribution.v1.json','all12manualfacts +KAR-AREA-F01'),
 ('KAR-WP09-CATALOG01','COMPLETE_SV_CATALOG_NAVIGATION_RECEIVED','SV01–17 completeindependentcasepremises/orderedexpectedresults alreadyhandreconstructed; navdoesnotclaimexecution.','catalog050607080910-manual-atoms.json','SVcasescomplete'),
 ('KAR-WP10-CATALOG01','COMPLETE_MG_CATALOG_NAVIGATION_RECEIVED','MG01–19 completeindependentcasepremises andprefixes alreadyhandreconstructed; no executioncredit.','catalog050607080910-manual-atoms.json','MGcasescomplete'),
 ('KAR-WP10-BAGV02','ACTUAL_CURRENT_POSITION_UI_JOIN_CLOSED','Ordinarybrowse/currentpositionnavigation andnormalchoosingwrapperrestore actuallyreceived; retainedoldfieldnotcleared.','bag-localization-residual-new-joins.v1.json','KAR-BLR-F01–03')
]
delta=[]
for aid,status,meaning,file,fact in joins:
    r=byid[aid]
    before=r.get('reception_status')
    r.setdefault('previous_reception_status_before_current_joins',before)
    r.update(reception_status=status,current_finite_join={'complete_contribution':ident(file),'fact':fact,'meaning':meaning},pending='Only exact stated native/override/earlier-dependency/history qualification remains; stale named source/interface pending resolved by complete new join.')
    delta.append({'id':aid,'previous':before,'current':status,'meaning':meaning,'evidence':ident(file),'fact':fact})

# Refresh exact already-received configuration routes; this index grants no new reading.
cons=read('consumer-candidate-dispositions.json')
config_delta=[]
for r in atoms:
    if not r['id'].startswith('KAR-WP02-CONFIG-'): continue
    symbol=r.get('finite_consumer_index',{}).get('symbol')
    if not symbol: continue
    selected=[x for x in cons['records'] if x['kind']=='settings' and x['symbol']==symbol]
    assert all(x['status']!='OPEN_NOT_YET_SEMANTICALLY_RECEIVED' for x in selected)
    r['finite_consumer_index']={'symbol':symbol,'kind':'POINTERS_TO_ACTUALLY_RECEIVED_FINITE_MEANINGS_NOT_NEW_READ_CREDIT','original_census_candidates':[{'id':x['id'],'status':x['status'],'manual_fact':x.get('manual_fact'),'contribution':x.get('contribution'),'meaning_and_premise':'Exact complete record in consumer-candidate-dispositions.json; mandatoryprovidercompanions retained'} for x in selected],'remaining_specific_locations':[],'extra_method_and_discovered_locations':'consumer-candidate-dispositions.json exactnamed collections; notautomaticzero-referenceexemption','dynamic_transitive_denominator':'NOT_GLOBALLY_EXHAUSTED; no currentformalclaim requiresallgamecallback theorem'}
    r['reception_status']='DECLARATION_DEFAULT_DEPENDENCY_AND_FINITE_ACTUAL_CONSUMPTION_RECONCILED'
    r['consumer_status']='All original714/extra8/discovered2 have exactmeanings/purposes; default/dependency itself hasalreadycompleteownsource. No native/allgame approval.'
    config_delta.append(r['id'])

# Explicitly split independent directory columns; do not conflate labels and writers.
stats=read('wp06-stats-directory-manual-field-atoms.json')
old_stats=stats['records'];new_stats=[];refinements=[]
retired=set()
for r in old_stats:
    if not r['id'].endswith('-UPDATE-SEMANTICS'):
        new_stats.append(r);continue
    parent=r['id'];retired.add(parent)
    cells=[s.strip() for s in r['formal']['exact_text'].strip('|').split('|')]
    assert len(cells)==7
    name,shape,initial,update,persist,evidence,owner=cells
    located=[x for x in cons['records'] if x['kind']!='settings' and x['symbol']==name]
    assert all(x['status']!='OPEN_NOT_YET_SEMANTICALLY_RECEIVED' for x in located)
    basis=[{'id':x['id'],'manual_fact':x.get('manual_fact'),'contribution':x.get('contribution'),'status':x['status']} for x in located]
    children=[]
    for facet,claim,status in [
        ('UNIT_OR_SHAPE',f'{name} directory unit/shape label is {shape}.','DECLARED_DIRECTORY_UNIT_NOT_ARBITRARY_VALUE_TYPE_INVARIANT'),
        ('UPDATE_CATEGORY',f'{name} update category: {update}.','QUALIFIED_UPDATE_CATEGORY_WITH_ACTUAL_PREFIX_OR_EXPLICIT_UNKNOWN'),
        ('RESPONSIBILITY_NAVIGATION',f'{name} responsibility navigation is {owner}.','DOCUMENT_OWNER_NAVIGATION_NOT_RUNTIME_CAUSAL_CLAIM'),
    ]:
        aid=parent.removesuffix('UPDATE-SEMANTICS')+facet
        child={'id':aid,'refines_retired_composite':parent,'formal':r['formal'],'assertion':claim,'reception_status':status,'source_status':'Current135scope SFR16 +actual74fielddefinitions/defaultsavewiring andfiniteconsumer facts','complete_finite_consumer_refs':basis,'evidence_qualifier':evidence,'premise':'FixedR/B8 legalordinaryobjects andeach exactsourcefactpremise. Unitlabel isnotruntimeclamp; category isnotiffwholeactionsuccess; ownerisnavigation. ExistingU01/methodknown-callerunknown/writerunlocated qualifications retained.','normal_failure_cancel_partial':'Each candidate manualfact retains actual earlyreturn/exception/prefix/cancel. For8U01 fields onlycomment/eventdependency isclaimed; halltime/badgetime mechanismknown butcallerunproved; BPwonunlocated. No fakeeventreachability.','target_behavior':'NOT_EXECUTED'}
        new_stats.append(child);children.append(aid)
    refinements.append({'retired_composite':parent,'children':children,'reason':'Unit/shape, update rule category andresponsibility areindependentlycheckablefacets; originalguardedupdateformula/prefix qualification remainsone relation.'})
assert len(retired)==74 and len(refinements)==74
stats.update(records=new_stats,explicit_facets=len(new_stats),updated_utc=NOW,global_or_chapter_semantic_denominator_frozen=False,remaining='Allfinitewriter/purposeedges received. Historicalexecutionrawprobes/native/Demo retaindeclaredqualifications; no generic namedsourcepending.')
write('wp06-stats-directory-manual-field-atoms.json',stats)
atoms=[r for r in atoms if not r['id'].startswith('KAR-WP06-STATS-')]+new_stats
assert len(atoms)==4792 and len({r['id'] for r in atoms})==4792
aliases=[r['id'] for r in atoms if r.get('reception_status')=='ALIAS_OF_EXPLICIT_MANUAL_CHILD']
assert len(aliases)==16
payload.update(records=atoms,updated_utc=NOW,manual_atomic_denominator={'working_records_including_aliases':4792,'retired_composites_not_counted':74,'independent_claim_occurrences':4776,'explicit_noncounting_aliases':aliases,'count_definition':'Unique independentlycheckable formalclaimoccurrences afterexplicit74columnrefinements and16identifiedaliases; semanticpropositions retaincompleteinput/prefix/qualifiers. Notold2219locators,notallgamebranch/callbackdenominator. Contractscope/definition/ownership/evidencequalifications distinguishedfromruntimeclaims byeachrecordstatus.','source_static_scope':'Current13Fboundedclaims only; native/declaredhistoricalrawqualification separate. No globaldomainPASS.'})
write('manual-atomic-clauses.json',payload)
old=read('old-locator-disposition.json');replacements={q['retired_composite']:q['children'] for q in refinements}
for r in old['records']:
    for key in ['explicit_manual_child_ids','manual_child_assertions']:
        if isinstance(r.get(key),list) and all(isinstance(v,str) for v in r[key]):
            r[key]=[z for v in r[key] for z in replacements.get(v,[v])]
old['updated_utc']=NOW;old['current_stats_refinement']='atomic-current-joins-and-denominator-refinement.v1.json';write('old-locator-disposition.json',old)
result={'schema':'KAR-current-finite-joins-and-selected-atomic-refinement.v1','utc':NOW,'reader':'/root/kernel_atomic_reception','new_explicit_resolved_joins':delta,'configuration_pointer_refresh_ids':config_delta,'stats74_selected_column_refinements':refinements,'unique_denominator':payload['manual_atomic_denominator'],'not_repeated':'Previouslyvalidated atomassertions/sourcebodies not reread or recopied; onlynecessarynewmeaning/joins andselectedfacetdiffs here. No readingcreditfrommechanicalnormalization.','business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'}
write('atomic-current-joins-and-denominator-refinement.v1.json',result)
print(json.dumps({'utc':NOW,'explicit_new_joins':len(delta),'config_refs_refreshed':len(config_delta),'stats_old':len(old_stats),'stats_new':len(new_stats),'working_records':4792,'independent_claim_occurrences':4776,'aliases':16}))
