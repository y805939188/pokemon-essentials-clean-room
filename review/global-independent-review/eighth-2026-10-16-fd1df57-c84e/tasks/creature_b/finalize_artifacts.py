"""Update reviewer-authored dispositions and validate evidence packaging, not game behavior."""
import datetime,hashlib,json,pathlib
p=pathlib.Path(__file__).resolve().parent;now=datetime.datetime.now(datetime.timezone.utc).isoformat()
rev=json.loads((p/'reverse-mapping.json').read_text())
for g in rev['groups']:
    c=g['clause']
    if g['file'].endswith('wp28-item-use-and-training.md'):
        if c.startswith('§3.3野外'):
            g['source_facts']+=['PAUSE','FISH','OVERWORLD','FIELD-MOVES'];g['status']='ITEM_FIELD_HELPERS_AND_DIRECT_CONSUMERS_FULL_READ; IF-WORLD-TRANSITIVE_REMAINS'
        elif c.startswith('§3.5'):
            g['source_facts']+=['COMMAND','ATTACK','ENDING'];g['status']='REGISTRATION_ATTACK_NORMALEND_SOURCE_CHAIN_RECEIVED; FULL_EOR_VECTOR_IF-EOR-COMPOSITION_REMAINS'
        elif c.startswith('§3.6'):
            g['source_facts']+=['ITEM-DATA','REGISTRY','DATA-IDENTITY'];g['status']='ALL_INITIAL_PBS_RECORDS_FULL_READ_OR_PROVEN_BYTE_ASSOCIATED; PBS_RECEIPT_SEPARATE'
        elif c.startswith('§5.1') or c.startswith('§5.2') or c.startswith('§5.5'):
            g['status']='ITEM_OWN_SOURCE_PLUS_FINITE_COM_MOVE_BATTLER_ITEM_CAPTURE_FACTS_RECEIVED; INTERFACE_LIMITS_RETAINED'
        elif c.startswith('§5.3'):
            g['source_facts']+=['NATURE','SPECIES-DEFINITION','EVOLUTION-DEFINITION','EVOLUTION-UI'];g['status']='ITEM_SOURCE_AND_EXPLICIT_COMPLETE_RECORD_VECTORS_RECEIVED; OTHER_SHARED_DOMAIN_PRIMARY_NOT_GRANTED'
        elif c.startswith('§5.4'):
            g['source_facts']+=['EVOLUTION-DEFINITION','EVOLUTION-UI','MOVE-DEFINITION'];g['status']='OWN_FULL_TEACH_EVOLUTION_DEFINITIONS_AND_CANDY_STONE_CONSUMER_RECEIVED; SUMMARY_FULLSLOT_HOST_SEPARATE'
        elif c.startswith('§5.6'):
            g['source_facts']+=['FORMS','STORAGE-UI','PARTY-UI','SPECIES-DEFINITION'];g['status']='OWN_FULL_FORM_AND_STORAGE_UI_SOURCE_CHAIN_RECEIVED; EXACT_RECORD_AND_HOST_QUALIFICATIONS_IN_INTERFACES'
    if g['file'].endswith('creature-rpg-wp27-28-29-30-33.md') and c in ['BG01–31','IU01–59/PP01–07','SH01–28']:
        g['individual_vector_mapping']='vector-mapping.json';g['status']='ALL125_RELEVANT_ROWS_INDIVIDUALLY_AUTHORED_AFTER_SOURCE_AND_FORMAL_FULL_READ; FINITE_INTERFACES_RETAINED'
rev.update(primary_full_text_audit_complete=True,all_transitive_interfaces_received=False,complete_semantic_acceptance=False,reason='All10 initial primary payloads fully read and reviewer-authored meanings mapped; five named external actual receptions remain in interfaces.json. This is not a whole-system pass.')
(p/'reverse-mapping.json').write_text(json.dumps(rev,ensure_ascii=False,indent=2)+'\n')
recordfacts={'schema':'gr8-creb-selected-record-facts/v1','reviewer':'/root/creature_b','utc':now,'scope':'12 complete logical PBS records actually displayed/read within3 larger files; no whole-file read credit for those3 PBS paths. Exact payload identities, display stdout/ranges/UTC/exit in reading-ledger.extra_partial_reads.','facts':[
 {'id':'VDATA-NATURE','records':'pokemon.txt BULBASAUR3–29; full Nature173; Pokemon calc_stats full1227','fact':'Base45/49/49/45/65/65 inPBSstatorder; L50 IV31 EV0 Hardy yields HP120 ATK69 DEF69 SPA85 SPD85 SPEED65. Lonely attack+10percent floor75/defense-10percent floor62; Brave attack75/speed58. Mint override leaves originalHARDY. MatchesIU56 arrays; derived arithmetic, not gameexecution.'},
 {'id':'VDATA-CATERPIE','records':'pokemon.txt CATERPIE237–262; moves.txt TACKLE5326–5337/STRINGSHOT327–337','fact':'CaterpiecurrentdefaultShieldDust/RunAwayhidden; evolvesLevel7Metapod, Tackle+StringShot records exist PP35/40. Legaltemplate/input remains explicitly constructed, no generator call. Full Evolution/Pokemon/UI verify maxCandy check/cancel prefix forIU54, no runtimeanimation claim.'},
 {'id':'VDATA-TR','records':'pokemon.txt MAGNEMITE2125–2151; moves.txt CHARGEBEAM1398–1410 and TACKLE5326–5337; ownfullitemsTM57','fact':'MagnemiteTutorMovesincludesChargeBeam; explicitknownTackle fixturevalid. DefaultTM57 FieldUseTR/MoveChargeBeam, movePP10. Bag wrapperaddsfirstmoves/stat; Partydirectdoesnot; actualfutureSummaryselection/relearn consumer outside finite itemfacts.'},
 {'id':'VDATA-FUSION','records':'pokemon.txt SOLGALEO20421–20444/NECROZMA20637–20660; forms NECROZMA1 1986–1997; moves Sunsteel8016–8027/Moongeist3186–3197/Confusion7253–7265','fact':'LegalSolgaleoandNecrozma records present; Necrozmaform1 dataexists andinherits omittedfields through compiler. Fullformcallback attemptsSunsteelStrikePP5; given[Tackle] freeslot fixturegains newmovePP5/pp_up0. Split forget/formfallback code fullyread; otherformrecords not claimed fullread.'}], 'execution':'DERIVED_VECTOR / NOT_EXECUTED'}
(p/'selected-record-facts.json').write_text(json.dumps(recordfacts,ensure_ascii=False,indent=2)+'\n')
interfaces=json.loads((p/'interfaces.json').read_text());assert interfaces['open_actual_receipt']==5
ledger=json.loads((p/'reading-ledger.json').read_text())
assert ledger['initial_own_full_read']==46 and ledger['primary_full_read']==10 and ledger['same_byte_associated_paths']==1
progress=json.loads((p/'progress.json').read_text());progress.update(updated_utc=now,ended_utc=now,status='PRIMARY_SCOPE_DELIVERED_WITH_NAMED_EXTERNAL_RECEPTIONS',phase='ALL6R_AND4FORMAL_PRIMARY_FULL_READ_MAPPED',initial_dependency_full_read=36,initial_dependency_byte_associated=1,unreceived_interfaces=5,interface_denominator=20,finite_accepted_interfaces=15,new_required=0,semantic_acceptance='FINITE_SOURCE_STATIC_PRIMARY_AUDIT; FIVE_EXTERNAL_RECEPTIONS_OPEN; NO_GLOBAL_PASS',selected_record_full_structures=12,selected_record_partial_payload_paths=3)
(p/'progress.json').write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n')
ledger.update(updated_utc=now,status='PRIMARY_SCOPE_DELIVERED_WITH_NAMED_EXTERNAL_RECEPTIONS',semantic_acceptance='PRIMARY_FULL_TEXT_AND_ATOMIC_MAPPING_COMPLETE; FIFTEEN_FINITE_INTERFACES_RECEIVED_AND_FIVE_EXTERNAL_FACETS_OPEN',extra_partial_payload_count=len(ledger['extra_partial_reads']),selected_complete_record_structures=12,structured_receipts=[{'artifact':'tasks/pbs_creature_facility/literal-validation.json','selector':'/literals/items','complete_structure_rows':84,'full_artifact_read':False,'execution_time_utc':'UNVERIFIED_NO_TOOL_TIMESTAMP_ECHO','receipt':'facility-item-interface.json plus IF-FACILITY-ITEM; peer-receipts.json scoped snapshot'},{'artifact':'tasks/pbs_creature_facility/template-default-normalization.json','selector':'/normalized_held_ids','complete_structure_rows':83,'full_artifact_read':False,'execution_time_utc':'UNVERIFIED_NO_TOOL_TIMESTAMP_ECHO','receipt':'IF-FACILITY-ITEM; peer-receipts.json scoped snapshot'},{'artifact':'tasks/combat_review/source-to-spec.json','selectors':['CORE-F001..014','CORE-F019','CORE-F023..026','CORE-F040..044','CORE-F048','CORE-F054','CORE-F057'],'full_artifact_read':False,'scope':'Only displayed complete logical fact objects, not all4625lines/entireCORE receipt','execution_time_utc':'UNVERIFIED_NO_TOOL_TIMESTAMP_ECHO'}])
(p/'reading-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
report=f'''CRE-B 的6个参考主责与4个正式主责均已连续全文读完并映射；没有新增 required。B8固定commit fd1df570cad987dc3852a3b958f03916e317f7fe、tree751dfde81048c81390f89a65ca1d1a565ba8e1ca、正式tree f292698cdd4a8e725525a9be6dc34b75faaf151e；R固定commit8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b、tree7589c800b61ba13a13040ed0d686979b80a84fd0。逐载荷blob、bytes、SHA及真实阅读输出见identities.json与reading-ledger.json。

初始47载荷中，46个由本上下文实际连续全文读取；Gen8/items与default/items已独立证同blob/SHA/字节，仅关联其独立条件路径，不计第二次本人显示。初始未读0；其中10primary、27代码dependency、4whole-file共享catalog全部本人全文读。六个PBS路径共3154个路径记录，五个独立raw载荷全文加Gen8关联；描述、全部字段、无默认caller的定义及配置均审。额外完整载荷{len(ledger['extra_full_reads'])}个；另3个PBS路径只读12个完整逻辑记录，精确区间与未授全文资格单列。没有以行数、脚本清单或旧PASS代替事实判断。

forward-mapping.json含50个人工主责源单元；dependency-semantic-facts.json含{len(json.loads((p/'dependency-semantic-facts.json').read_text())['facts'])}个人工依赖单元；reverse-mapping.json含47个正式条款组和原子子断言；vector-mapping.json逐ID接合BG31、IU59、SH28及PP7共125条。PBS机械索引与人工语义接收分别在pbs-record-inventory.json、pbs-record-reception.json，前者不授语义信用。

实际补读了Party、Bag、Ready、PC/Mail、Shop/BP、Interpreter、GameData、物种/招式定义、FormHandlers、StorageUI、Evolution及画面、Phone及画面、Pause、Overworld、FieldMoves、Fishing、SaveData以及战斗命令/攻击/正常终局。跨审只按实际审者和完整接收载荷有限采用com_move的Battler/Ability/Item/Fling/NaturalGift事实、root电话反证和pbs_creature_facility的PBF-ITEM合同。15/20个有限接口已接收；五个外域实际接收面仍开放，逐个消费者与范围见interfaces.json：野外传递、EOR完整复合向量、共享目录其他主责、其他道具消费者、历史/二进制/宿主。它们不是伪造材料不可得或初始primary漏读，也没有被改标为已接收。

电话四项观察已有WP63明文；迁移后序缺get需显式合法runtimeglobal前提，默认冷启动更早失败映射WP10。CRE001仅接收root已采纳P3及本片独立验证的有限道具外层事实：合法255状态明确交给普通EV工具可在clamp失败前保留库存；默认设施internalBattle=false不能据此宣称战斗道具默认可达。WP28受限起始状态限定保留，不另立无谓mandatory，不扩大到Shadow。Mail取消前缀、瓶子/融合重入及Shadow门已有当前合同，未新计根。设施default STICK缺记录→nil与LEEK不同的有限接口已接收，设施整体裁决由实际primary/root处理。所有triage在proposals.json。

证据等级为SOURCE_STATIC / DERIVED_VECTOR；业务执行0，所有向量NOT_EXECUTED；UPDATE_NOT_STARTED。只写tasks/creature_b，未改正式规格、R、历史、其它任务或公共状态；未安装、commit、push或自动整改。请求配置gpt-6.1-sol/ultra/default普速/Fast off；实际model、effort、tier、speed/Fast及平台opaque ID均无回显，逐项UNVERIFIED。实际显示UTC/exit在read-io/index.jsonl；早期无UTC回显的导航失败不追造时间，见tool-limitations.json。

开始UTC2026-10-16T03:27:40.832940+00:00；本次打包UTC{now}。本交付只结清本片完整primary审读与有限接口，不声明全系统审查通过。
'''
(p/'review.md').write_text(report)
print(json.dumps({'utc':now,'initial_full':46,'byte_associated':1,'primary_full':10,'extra_full':len(ledger['extra_full_reads']),'extra_partial_paths':len(ledger['extra_partial_reads']),'finite_interfaces':15,'open_interfaces':5,'new_required':0}))
