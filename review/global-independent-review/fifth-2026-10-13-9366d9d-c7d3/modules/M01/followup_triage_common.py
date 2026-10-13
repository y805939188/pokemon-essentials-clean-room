"""Followup audit metadata helpers. Never load/execute reference code."""
import copy
import hashlib
import json
from pathlib import Path

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]
REF=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
B='9366d9d17aaeac3b4414236468affa650fb3dd27'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
FORMAL='deliverables/final-specification-set/'
def read(name):return json.loads((OUT/name).read_text())
def write(name,value):(OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
BASE=read('followup-partial-baseline.json')
INPUT=read('followup-partial-triage-input.json')['records']
OLD=read('source-to-spec.json')['capabilities']
OLD_INDEX={x['capability_id']:i for i,x in enumerate(OLD)}
COV=read('reading-coverage.json')
CANON_PATH='review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/counterevidence/root-M01/canonical-findings.json'
CANON=json.loads((ROOT/CANON_PATH).read_text())['findings']
SPECS={
 '02':'generic-kernel/wp02-rule-configuration-and-data-variants.md',
 '03':'generic-kernel/wp03-content-identity-and-schema.md',
 '04':'generic-kernel/wp04-pbs-lifecycle.md',
 '08':'generic-kernel/wp08-localization.md',
 '11':'engine-overworld/wp11-map-topology-transfer.md',
 '14':'engine-overworld/wp14-random-dungeons.md',
 '18':'creature-rpg/wp18-creature-identity-species-ownership.md',
 '19':'pokemon-rules/wp19-attributes-ability-and-stats.md',
 '21':'pokemon-rules/wp21-dynamic-forms-and-display.md',
 '24':'creature-rpg/wp24-player-trainers-partners.md',
 '25':'creature-rpg/wp25-party-and-storage.md',
 '27':'creature-rpg/wp27-bag-and-item-storage.md',
 '28':'creature-rpg/wp28-item-use-and-training.md',
 '29':'creature-rpg/wp29-shops-and-exchanges.md',
 '31':'pokemon-rules/wp31-basic-evolution.md',
 '34':'pokemon-rules/wp34-inheritance-and-offspring.md',
 '36':'creature-rpg/wp36-wild-encounters-and-modifiers.md',
 '43':'pokemon-rules/wp43-types-accuracy-and-damage.md',
 '51':'combat-requirements/wp51-ai-action-selection-and-skill.md',
 '62':'pokemon-rules/wp62-pokedex-records-regions-and-content.md',
 '63':'user-interface/wp63-pokegear-map-music-and-phone.md',
 '65':'user-interface/wp65-title-load-options-pause-and-pc.md',
 '66B':'user-interface/wp66-b-storage-and-pokedex-ui.md',
 '66C':'user-interface/wp66-c-bag-item-storage-and-shop-ui.md',
 '73A':'demo-dx/wp73-a-content-editors.md',
 '73B':'demo-dx/wp73-b-world-editors.md',
 '74':'demo-dx/wp74-battle-animation-authoring-and-exchange.md',
 '75':'demo-dx/wp75-project-conversion-and-authoring-tools.md',
 '76':'demo-dx/wp76-facility-content-generation-and-simulation.md',
 '77':'demo-dx/wp77-demo-evidence-and-capability-coverage.md',
}
SRC={
 'intl':'Data/Scripts/001_Technical/003_Intl_Messages.rb',
 'parse':'Data/Scripts/021_Compiler/001_Compiler.rb',
 'compile':'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',
 'write':'Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb',
 'data':'Data/Scripts/010_Data/001_GameData.rb',
 'town':'Data/Scripts/010_Data/002_PBS data/002_TownMap.rb',
 'ability':'Data/Scripts/010_Data/002_PBS data/004_Ability.rb',
 'move':'Data/Scripts/010_Data/002_PBS data/005_Move.rb',
 'item':'Data/Scripts/010_Data/002_PBS data/006_Item.rb',
 'species':'Data/Scripts/010_Data/002_PBS data/008_Species.rb',
 'ribbon':'Data/Scripts/010_Data/002_PBS data/012_Ribbon.rb',
 'trtype':'Data/Scripts/010_Data/002_PBS data/014_TrainerType.rb',
 'trainer':'Data/Scripts/010_Data/002_PBS data/015_Trainer.rb',
 'meta':'Data/Scripts/010_Data/002_PBS data/016_Metadata.rb',
 'mapmeta':'Data/Scripts/010_Data/002_PBS data/018_MapMetadata.rb',
 'dtiles':'Data/Scripts/010_Data/002_PBS data/019_DungeonTileset.rb',
 'dparams':'Data/Scripts/010_Data/002_PBS data/020_DungeonParameters.rb',
 'phone':'Data/Scripts/010_Data/002_PBS data/021_PhoneMessage.rb',
 'bag':'Data/Scripts/016_UI/007_UI_Bag.rb',
 'itempc':'Data/Scripts/016_UI/018_UI_ItemStorage.rb',
 'phonecall':'Data/Scripts/013_Items/004_Item_Phone.rb',
 'messages':'Data/Scripts/007_Objects and windows/011_Messages.rb',
 'editor':'Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb',
 'props':'Data/Scripts/020_Debug/002_Editor_DataTypes.rb',
 'shape':'Data/Scripts/010_Data/001_Hardcoded data/004_BodyShape.rb',
 'color':'Data/Scripts/010_Data/001_Hardcoded data/005_BodyColor.rb',
 'habitat':'Data/Scripts/010_Data/001_Hardcoded data/006_Habitat.rb',
}

def source(key,a,b,fact,entry='M01有限后继具名来源',caller='实际作者输入/输出或所列消费路径'):
    path=SRC.get(key,key);p=REF/path
    data=p.read_bytes();blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    return dict(path=path,version=dict(commit=R,git_blob=blob),lines=[a,b],symbol_or_data_keys=entry,
                caller_config=caller,supporting_fact=fact)

def spec(key,a,b,statement,clause=None):
    path=FORMAL+SPECS[key] if key in SPECS else key
    return dict(path=path,version=B,lines=[a,b],section_or_vector=clause or '具名当前合同范围',current_statement=statement)

def oldref(index):
    identity=INPUT[index]['capability_id']
    return dict(path='source-to-spec.json',sha256=BASE['original_files']['source-to-spec.json'],
                json_pointer='/capabilities/'+str(OLD_INDEX[identity]),capability_id=identity)

def canon(number,scope):
    identity=f'GR5-M01-{number:03d}'
    i=next(i for i,x in enumerate(CANON) if x['id']==identity);x=CANON[i]
    return dict(id=identity,path=CANON_PATH,sha256=BASE['canonical_sha256'],json_pointer='/findings/'+str(i),
                disposition=x['disposition'],status=x['status'],severity=x['severity'],subscope=scope,
                reuse='母汇总者+C01最终有界判断；本次不重新反证、执行或裁决旧ID。')

def negative(anchors,extra=None):
    out=[]
    for a in anchors:
        old=next((e for e in COV['specifications'] if e['path']==a['path']),None)
        out.append(dict(path=a['path'],version=B,focused_range=a['lines'],
                        prior_read_ranges=old.get('read_ranges',[]) if old else [],
                        prior_evidence_anchor=dict(path='reading-coverage.json',sha256=BASE['original_files']['reading-coverage.json']),
                        method='复用本轮已完成的正文/原稿/向量审读；本后继仅就具名条款和合理同义入口定点核对。',
                        result=a['current_statement']))
    if extra:out.extend(extra)
    return out

def finding(number,title,severity,root,inputs,src,sp,rules,gap,case,normal,boundary,impact,change,
            preconditions=None,excluded=None,negative_extra=None,related=None,owner='M01'):
    x=copy.deepcopy(read('findings.json')['findings'][0])
    identity=f'GR5-M01-{number:03d}'
    x.update(id=identity,title=title,module='M01',reviewer='M01 independent reviewer / finite followup proposer',
             severity=severity,disposition='unresolved',status='candidate_pending_independent_counterevidence',
             category='bounded_author_or_consumer_contract_gap',priority=severity+' provisional',
             batch_owner=owner,root_cause_group=root,source_anchors=src,spec_anchors=sp,
             expected_reference_behavior=dict(rules=rules,scope='仅所列入口与前提；不规定未来API、类、存储容器或源语言实现。'),
             current_spec_behavior='；'.join(a['current_statement'] for a in sp),gap=gap,
             preconditions=preconditions or ['固定R和B5；无插件/回调覆写具名路径','所列依赖、其余数据与先行步骤正常；观察点只到具名提交/拒绝或读写结果'],
             minimal_counterexample=dict(input=case[0],static_expected=case[1],execution='NOT_EXECUTED'),
             normal_case=dict(input=normal[0],static_expected=normal[1],execution='NOT_EXECUTED'),
             failure_or_boundary_case=dict(input=boundary[0],static_expected=boundary[1],execution='NOT_EXECUTED'),
             impact_on_independent_implementation=impact,negative_evidence_search=negative(sp,negative_extra),
             proposed_spec_change=change,affected_files=list(dict.fromkeys(a['path'] for a in sp if a['path'].startswith(FORMAL))),
             shared_contracts=[root],related_capabilities=[INPUT[i]['capability_id'] for i in inputs],
             related_findings=related or [],dependencies=['母任务指派非原提出者作独立反证后再裁决；本次不自签最终required'],
             history_links=[],evidence_level=['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'],
             execution_status=dict(followup='NOT_EXECUTED',reference=False,behavior_model=False,author_tool_or_generator=False,
                                   note='只作静态阅读及审查产物的JSON/锚点记账；没有场景或I/O往返行为执行。'),
             acceptance_criteria=dict(static=['逐条核对具名源事实、现行正文/原稿/向量与独立反证','补充分支、前提、正常/边界对照；不扩大为所有异常输入或所有消费者','政策与固定参考事实分别表达，保持既有正确合同'],
                                      must_execute=[],if_later_authorized='若母任务另行批准隔离执行，须先给具体版本/输入/命令/副作用；本提案不以新增执行为前提。'),
             confidence=dict(source_behavior='high_static_for_named_path',spec_gap='bounded_candidate_pending_independent_counterevidence'),
             unknowns=['真实宿主/完整作者工作流未执行','独立非原提出者反证尚未派发完成'],
             excluded_claims=(excluded or [])+['不把源方法或类的存在本身变为新公开接口要求','不重开GR5-M01-001..007的C01最终有界裁决','不修改正式规格、参考源或历史证据'],
             user_decision_needed=dict(required_now=False,compatibility_policy='固定参考事实与未来是否保留该兼容行为分开；本次无需向用户追问政策。'),
             review_resolution=dict(proposal_analysis_complete=True,independent_counterevidence='pending',final_required_signed=False,
                                    next_owner='mother task assigns a different reviewer'),
             followup_input_records=[oldref(i) for i in inputs],
             followup_input_anchor=dict(path='followup-partial-triage-input.json',sha256=BASE['input_sha256']))
    return x
