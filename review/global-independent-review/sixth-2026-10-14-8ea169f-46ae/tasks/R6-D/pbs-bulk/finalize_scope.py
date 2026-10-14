"""Finalize clarified PBS scope with parent-adjudication proposals, never PASS."""
import audit as a, relations as r, build_mappings as b, field_semantics as fs
from collections import defaultdict,Counter
from pathlib import Path
import json,re,gzip

def load(name):return b.read(name)
def location(rec,field=None):return r.loc(rec,field)
def run():
    a.bind();summary=load('field-semantics-summary.json')
    assert summary['actual_fields_with_rule']==104 and summary['missing_required_reading_ranges']==0
    rules=load('field-semantic-rules.json');lookup={(x['family'],x['field']):x for x in rules};records=r.readrecords();files=load('file-inventory.json')
    profile=defaultdict(lambda:defaultdict(dict))
    for rec in records:profile[rec['profile']][rec['family']][r.normid(rec)]=rec
    headers=[]
    for fam in r.SCHEMAS:
        pair=fam in {'pokemon_forms','pokemon_metrics','shadow_pokemon'}
        body='Symbolic section identity, exact case; duplicate generic identity rejects before registering the current record after per-record validation.'
        refs=[];s=[b.L(b.CP,4,67)];form=[]
        if fam=='pokemon_forms':
            body='Registered Species identity followed by positive form number; construct compound identity, refuse an existing compound key, preserve base table while adding forms. Actual corpus uses base-species heads; compiler enum membership is not a separate base-only predicate.';s=[b.L(b.CP,388,445),b.L(b.CP,448,457)];refs=['Species registered at form-read time']
        elif fam in {'pokemon_metrics','shadow_pokemon'}:
            body='Registered Species identity and optional positive form number; omitted form becomes0, zero-form key is species identity, positive form becomes a compound key. A separate existence test for a species-form record is absent from these validators.';s+=[b.L(b.CP,549,563) if fam=='pokemon_metrics' else b.L(b.CP,574,588)];refs=['Species enum before optional positive form; no separate form-record existence check']
        if fam=='berry_plants':body+=' Item association is runtime only, not an enum constraint.'
        if fam=='shadow_pokemon':body+=' Optional absent inputs return before clearing the table; absent .dat load also preserves an existing table.';s+=[b.L(r.SCHEMA_DIR+'011_ShadowPokemon.rb',11,29)];form+=[b.L(b.WP03,79,87)]
        source=r.SCHEMA_DIR+r.SOURCE_FILE[fam];definition=[]
        for n,l in enumerate((a.ROOT/source).read_text().splitlines(),1):
            if '"SectionName"' in l and ('[:id' in l):definition.append(b.L(source,n))
        headers.append({'header_rule_id':'HEADER.'+fam,'family':fam,'behavior':body,'source':definition+s,'reference_premises':refs,'formal':[b.L(b.WP03,153,176),b.L(fs.WP18,49,54) if pair else b.L(b.WP03,122,136)]+form,'status':'REVIEWED_AUTHOR_IDENTITY_WIRING_NOT_PASS'})
    a.save('header-contracts.json',headers)
    # Every authored occurrence and omitted allowable field maps to a human rule.
    forward=[];applications=Counter();staged=[];embedded=[];stagefails=[]
    source_by_rule=defaultdict(list)
    for rec in records:
        fields=r.effective(rec);fam=rec['family'];base_id=rec['identity'].split(',')[0].strip();base=profile[rec['profile']]['pokemon'].get(base_id) if fam=='pokemon_forms' else None
        base_fields=r.effective(base) if base else {};rows=[]
        wild_absent=not any(k in fields for k in ['WildItemCommon','WildItemUncommon','WildItemRare'])
        for key in r.SCHEMAS[fam]:
            rule=lookup[(fam,key)];auth=fields.get(key);occ=auth if isinstance(auth,list) else ([auth] if auth else [])
            if occ:mode='authored';origin=[location(rec,x) for x in occ]
            elif fam=='pokemon_forms' and key in fs.SPECIES_INHERIT and (not key.startswith('WildItem') or wild_absent):
                mode='inherit_effective_base';bf=base_fields.get(key);bl=bf if isinstance(bf,list) else ([bf] if bf else []);origin=[location(base,x) for x in bl] if bl else [{'kind':'base_constructor_default','rule':'AUTHOR.pokemon.'+key,'base':location(base)}]
            else:mode='record_default';origin=[{'kind':'constructor_default','rule':rule['rule_id'],'default':rule['omission']['base_or_record_default']}]
            if fam=='pokemon_forms' and key.startswith('WildItem') and not occ and not wild_absent:mode='empty_pool_because_other_wild_item_group_authored';origin=[{'kind':'record_constructor_empty_pool'}]
            rows.append({'field':key,'rule_id':rule['rule_id'],'author_input':mode,'value_origin':origin,'formal_assessment':rule['formal_assessment'],'status':'CONDITIONAL_RULE_APPLICATION_NOT_GAMEPLAY_PASS'})
            source_by_rule[rule['rule_id']].append({'path':rec['path'],'identity':rec['identity'],'start_line':rec['start_line'],'field_lines':[x['line'] for x in occ],'mode':mode})
            applications[mode]+=1
        implicit=[]
        if fam=='pokemon_forms':
            for key in ['Name','GenderRatio','GrowthRate','Incense']:
                implicit.append({'field':key,'mode':'fixed_inheritance_not_a_form_author_property','base_record':location(base),'base_rule_id':'AUTHOR.pokemon.'+key,'source':b.L(b.CP,460,469)})
        forward.append({**location(rec),'header_rule_id':'HEADER.'+fam,'profile_premise':'current top-level; or coherent conditional generation replacement; or Shadow overlay on current registries. Backups are not automatically discovered.','field_applications':rows,'implicit_inherited_fields':implicit,'structural_evidence':'record-inventory.jsonl; shape-checks.json; reference-relations.json','semantic_evidence':'field-semantic-rules.json; header-contracts.json; precise cross-domain links','status':'ALL_PBS_AUTHOR_FIELDS_MAPPED_TO_REVIEWED_RULES; NOT_PASS'})
        # Target/offspring at base finalization precede all form registration.
        if fam=='pokemon':
            for key in ['Offspring','Evolution','Evolutions']:
                auth=fields.get(key);occ=auth if isinstance(auth,list) else ([auth] if auth else [])
                for prop in occ:
                    vals=r.atoms(prop['value']);targets=vals if key=='Offspring' else (vals[::3] if key=='Evolutions' else vals[:1])
                    for target in targets:
                        ok=target in profile[rec['profile']]['pokemon'];z={**location(rec,prop),'target':target,'phase':'base-species whole-table finalization before forms','base_identity_available':ok,'source':b.L(b.CP,332,352),'status':'phase-specific literal prerequisite checked, not compiler execution'};staged.append(z)
                        if not ok:stagefails.append(z)
        for prop in rec['fields']:
            if prop['key']!='Flags':continue
            for index,flag in enumerate(r.atoms(prop['value'])):
                match=re.fullmatch(r'NaturalGift_(\w+)_(\d+)',flag,re.I)
                if match:
                    typ,power=match.groups();reg=profile[rec['profile']]['types'];target=reg.get(typ)
                    embedded.append({**location(rec,prop),'position':index,'flag':flag,'embedded_runtime_type_identity':typ,'type_location':location(target) if target else None,'authored_power':int(power),'consumer_fallback':'type NORMAL if full matching target identity absent; power first full pattern at least10','source':[b.L(fs.S+'011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb',1350,1370)],'formal':[b.L(fs.F+'combat-requirements/wp47-a-move-attributes-targeting-and-calling.md',66)],'classification':'runtime encoded flag data; NOT compiler enum constraint'})
                elif re.fullmatch(r'Fling_(\d+)',flag,re.I):
                    embedded.append({**location(rec,prop),'position':index,'flag':flag,'authored_power':int(flag.rsplit('_',1)[1]),'consumer_fallback':'first full numeric pattern, at least10; prefix eligibility is separate','source':[b.L(fs.S+'011_Battle/003_Move/011_MoveEffects_Items.rb',403,436)],'classification':'runtime encoded flag data; NOT enum reference'})
                elif re.fullmatch(r'DefaultForm_(\d+)',flag,re.I):
                    form=int(flag.rsplit('_',1)[1]);key=base_id+','+str(form);exists=form==0 or key in profile[rec['profile']]['pokemon_forms']
                    embedded.append({**location(rec,prop),'position':index,'flag':flag,'form_number':form,'corresponding_form_data_exists':exists,'consumer':'first matching default-form marker; missing later form lookup may use base fallback','source':[b.L(fs.SP,243,252)],'classification':'runtime form selector; NOT extra compile-validation rule'})
    a.save('source-to-spec-matrix.json',forward)
    reverse=[]
    for rule in rules:
        for clause in rule['formal_clauses']+rule['shared_formal_parser']+rule['export_formal']:
            reverse.append({'formal_clause':clause,'author_rule_id':rule['rule_id'],'source_declarations':rule['schema_source'],'constructor':rule['constructor_source'],'normalization_source':rule['normalization_source'],'necessary_consumers':rule['necessary_consumers'],'premises':rule['premises'],'record_occurrences':source_by_rule[rule['rule_id']],'assessment':rule['formal_assessment'],'gap_proposals':rule['gap_proposals'],'status':'REVIEWED_PBS_AUTHOR_SCOPE_MAPPING_NOT_PASS'})
    a.save('spec-to-source-matrix.json',reverse)
    a.save('stage-specific-reference-checks.json',{'checks':staged,'exceptions':stagefails,'phase_boundary':'Only base evolution target/offspring membership tightened here. General compiler scheduling/failure/full dependency graph remains K/parent.'})
    a.save('embedded-flag-contracts.json',embedded)
    a.save('record-author-scope-coverage.json',{'records':len(records),'each_record_has_header':len(forward),'records_missing_field_mapping':[],'field_application_modes':dict(applications),'author_fields_reviewed':104,'rules_including_omission_only':len(rules),'required_rule_reading_gaps':0,'semantic_review_extent':'Generic author-field rule semantics independently read; all records mechanically joined under those explicit premises. This is not manual transcription of206649 lines, execution, or approval of downstream algorithms.','status':'REVIEW_COMPLETE_FOR_PARENT_ADJUDICATION_NOT_PASS'})
    for row in files:
        row['semantic_status']='Structural inventory only; current author semantics are independently joined in source-to-spec-matrix.json; NOT_PASS'
    a.save('file-inventory.json',files)
    with (a.OUT/'record-inventory.jsonl').open('w') as output:
        for row in records:
            row['semantic_status']='Structural evidence only; see the independent reviewed author-rule join; NOT_PASS'
            output.write(json.dumps(row,ensure_ascii=False)+'\n')
    classes={'pokemon':['Creature-RPG','Pokémon Rules'],'pokemon_forms':['Creature-RPG','Pokémon Rules'],'pokemon_metrics':['Engine / Overworld Integration','User Interface'],'moves':['Combat Requirements','Pokémon Rules'],'abilities':['Pokémon Rules','Combat Requirements'],'items':['Creature-RPG','Pokémon Rules','User Interface'],'berry_plants':['Pokémon Rules','Engine / Overworld Integration'],'types':['Pokémon Rules','Combat Requirements','User Interface'],'shadow_pokemon':['Pokémon Rules','Combat Requirements']}
    a.save('feature-matrix-projection.json',{'destination_owner':'Parent/global Feature Matrix; no protected global matrix edited from this task directory.','shared_classification':['Generic Kernel (author content contracts)','Demo / Developer Experience (PBS author lifecycle)'],'families':[{'family':family,'classification':classes[family],'records':sum(x['family']==family for x in records),'actual_fields':sum(x['family']==family and x['appears_in_assigned_data'] for x in rules),'rule_ids':[x['rule_id'] for x in rules if x['family']==family],'status':'reviewed author scope; proposals await non-proposer; NOT_PASS'} for family in sorted(classes)]})
    # Keep initial discovery artifacts readable without leaving stale unresolved
    # obligations for work completed in this continuation.
    old_bindings=load('field-contract-matrix.json')
    for row in old_bindings:
        row['author_semantic_rule_id']='AUTHOR.'+row['family']+'.'+row['field']
        row['status']='SCHEMA_AND_AUTHOR_SEMANTIC_RULE_REVIEWED; see field-semantic-rules.json; parent adjudication pending; NOT_PASS'
    a.save('field-contract-matrix.json',old_bindings)
    facts=load('behavior-facts.json')
    for row in facts:
        if row['fact_id']=='D18':row.update(formal_clauses=[b.L(fs.WP20,125,132)],status='REVIEWED_LIMITED_STATIC_CONTRACT')
        if row['fact_id']=='D19':row.update(formal_clauses=[b.L(fs.WP20,145,150)],status='REVIEWED_LIMITED_STATIC_CONTRACT')
    a.save('behavior-facts.json',facts)
    # Supersede first checkpoint's overbroad gameplay obligation, retaining
    # downstream boundaries explicitly instead of inventing a whole-game PASS.
    a.save('semantic-pending-records.json',{'supersedes':'Initial checkpoint treated downstream gameplay algorithms as repeated per-record obligations; parent clarified PBS author scope.','remaining_in_scope_unread_records':0,'remaining_in_scope_unread_field_rules':0,'remaining_in_scope_unread_required_contexts':0,'downstream_algorithm_handoffs':'Per rule and move-effects-bidirectional-locations.json; explicit out-of-scope domains below.','parent_adjudication_pending':True,'not_a_PASS':True})
    # Keep all four original suspicions for a non-proposer's rebuttal.
    findings=[x for x in load('findings.json') if x['id'] in {'R6-D-PBS-C01','R6-D-PBS-C02','R6-D-PBS-C03','R6-D-PBS-C04'}]
    for f in findings:
        if 'initial_proposer_recommendation' not in f:f['initial_proposer_recommendation']=f.get('proposal_status')
        f['proposal_status']='PENDING_PARENT_REBUTTAL_OR_ADJUDICATION'
        f['non_proposer_review_required']=True
        f['scope_after_parent_clarification']='Full downstream algorithms are explicit cross-domain handoffs, not unread repeated PBS record obligations.'
        if f['id']=='R6-D-PBS-C02':
            f['formal']=[b.L(fs.WP20,145,150)]
            f['minimal_revision']='No proposer revision requested; existing WP20 membership contract now directly located for parent rebuttal.'
            f['dependencies']=['Interactive tutoring and consumption algorithms handed to WP28/30; author-field wiring review completed.']
    new=[
      {'id':'R6-D-PBS-C05','title':'Type/Move/Item 部分作者省略值缺少明确正式合同','impact_level':'MEDIUM_PROPOSED_COMPLETENESS_GAP','source':[b.L(r.SCHEMA_DIR+'003_Type.rb',33,46),b.L(r.SCHEMA_DIR+'005_Move.rb',41,56),b.L(r.SCHEMA_DIR+'006_Item.rb',119,137)],'formal':[b.L(b.WP03,89,110),b.L(b.WP03,282,292),b.L(b.WP27,45,67)],'preconditions':'合法新身份，依赖正常；Move 显式Type=NORMAL且Category/Power省略得到合法Status0；无语言命中或只观察原始字段。','ordinary_control':'Item显式Name=Review及NamePlural=Reviews分别保留；Move显式名/描述/优先级/效果率保留；Type显式图标3/特殊真/伪真保留。','minimal_counterexample':'合法Item只给Name=Review而省NamePlural，原始复数为Unnamed，不是Review或自动复数；合法Move省Name/Description/Priority/EffectChance/Flags为Unnamed/???/0/0/空；合法Type仅身份得到Unnamed/图标0/特殊假/伪假。','cancellation_exception_partial_commit':'只观察成功条目登记及原始查询；没有UI取消。当前条目转换后登记，后续错误不回滚已登记条目；不据此证明整表保存或最终翻译/绘图。','negative_search':'本轮对全部131正式文件检索Unnamed、IsSpecialType、IsPseudoType、IconPosition及作者默认组合；WP03有限省略表覆盖Ability与部分Move，WP27覆盖数值/用途/消费，未找到上述完整Type/Move/Item默认组合；职责目录仅指派领域，不展开语义。','necessary_consumers':[b.L(r.SCHEMA_DIR+'003_Type.rb',49,59),b.L(r.SCHEMA_DIR+'005_Move.rb',65,96),b.L(r.SCHEMA_DIR+'006_Item.rb',140,164)],'minimal_revision':'由主审判定后，在相应数据合同补有限省略默认，特别明确Item复数名独立默认；不扩成全部字段必填。','preserved_scope':'其余既有价格/用途/消费、类型NONE、命中100、PP5、Status0/None效果合同保持；名称与本地化输出分开。','synchronize_files':['generic-kernel/wp03-content-identity-and-schema.md','creature-rpg/wp27-bag-and-item-storage.md','pokemon-rules/wp43-types-accuracy-and-damage.md','test-catalog/generic-kernel-wp02-03-04.md'],'acceptance':'省略与显式普通对照可由规格唯一得出所列原始值，新增向量继续NOT_EXECUTED。','dependencies':['K的通用解析/登记合同','本地化主责的空译/缺译合同']},
      {'id':'R6-D-PBS-C06','title':'显式部分形态指标记录的缺字段默认，不能由缺整条查询克隆替代','impact_level':'MEDIUM_PROPOSED_AUTHOR_CONTRACT_GAP','source':[b.L(r.SCHEMA_DIR+'010_SpeciesMetrics.rb',17,23),b.L(r.SCHEMA_DIR+'010_SpeciesMetrics.rb',32,68),b.L(b.CP,543,563)],'formal':[b.L(b.WP03,56),b.L(fs.WP73B,160,164),b.L(b.WP04,199,206)],'preconditions':'VENUSAUR及其形态1均有效，指标编译依赖正常，基础背面坐标人工设5,6；合法正形态节只给ShadowSize2，其余字段省略，读写成功且无额外查询/覆盖。','ordinary_control':'完全没有形态1指标记录时再查询，惰性克隆基础背面5,6；显式形态BackSprite7,8则读7,8。','minimal_counterexample':'形态1指标节存在却省BackSprite时，构造默认0,0；随后查询命中已有记录，不复制基础5,6。FrontSprite、Altitude、ShadowX、ShadowSize分别缺省0,0/0/0/2同理。','cancellation_exception_partial_commit':'比较编译登记/查询结果，不伪称编辑保存。查询缺整条可先登记基础/形态，显式条目编译已登记状态也不因之后错误整体撤回；档案/PBS仍分别提交。','negative_search':'正式SpeciesMetrics条款明确缺整条查询克隆，WP73-B明确五组及查询副作用/导出，但本轮未找到显式部分形态指标逐字段默认合同；基础Species形态继承表不能套到Metrics。','necessary_consumers':[b.L(r.SCHEMA_DIR+'010_SpeciesMetrics.rb',32,56),b.L(r.SCHEMA_DIR+'010_SpeciesMetrics.rb',59,80)],'minimal_revision':'补Metrics作者记录缺字段默认表，明确与缺整条惰性克隆分层，加入部分形态/整条缺席/显式坐标三组向量。','preserved_scope':'保留既有查询副作用、后缀空、新形态复制及非零形态选路径/等值省略、已有战斗不广播重定位。','synchronize_files':['generic-kernel/wp03-content-identity-and-schema.md','demo-dx/wp73-b-world-editors.md','test-catalog/generic-kernel-wp02-03-04.md'],'acceptance':'同一合法基础5,6下，三组分别0,0 /5,6 /7,8，且不改参考或声称已运行。','dependencies':['K编译登记','资源/指标消费者WP15/67-A/73-B']},
      {'id':'R6-D-PBS-C07','title':'合法作者Happiness256可被个体创建直接保留，超出WP30无条件0–255措辞','impact_level':'MEDIUM_PROPOSED_CONTRADICTION','source':[b.L(r.SCHEMA_DIR+'008_Species.rb',76,77),b.L(r.SCHEMA_DIR+'008_Species.rb',194,195),b.L(b.CP,292,329),b.L(fs.CO,35,40),b.L(fs.CO,1159,1226)],'formal':[b.L(fs.WP30,184,187),b.L(fs.WP18,94)],'preconditions':'独立作者夹具仅将合法BULBASAUR记录的Happiness改256，其余依赖、物种字段与宿主成功；从该已登记物种正常创建L5个体，显式关闭招式初始化和创建形态复检以隔离此入口；无插件或后续友好度改变。不是默认随附数据的超界声称。','ordinary_control':'Happiness255保持255；省略保持70；显式0保持0。','minimal_counterexample':'Happiness是非负整数格式，256通过该格式及已读物种专用验证；物种记录保留256，个体创建直接复制，创建末尾没有友好钳制，得到256。','cancellation_exception_partial_commit':'裸创建没有确认/取消流程；成功创建观察点限定在返回后、其它友好变更之前。RNG/能力计算不据此宣称已执行；前门异常不会产生该成功观察结果。','negative_search':'物种验证292–329无255上限；构造175–220与个体创建1159–1226无友好钳制；全部正式文件对Happiness/友好255范围的负搜索未找到合法作者超界初值例外。编辑器0–255并不约束PBS非负整数入口。','necessary_consumers':[b.L(fs.CO,1187,1188),b.L(fs.CO,1214,1226)],'minimal_revision':'限定WP30的0–255为正常受控变化/作者常规域，明确合法作者超界初值直接保留，或明确区分参考事实与未来校验政策；补256/255/省略/0四组向量。','preserved_scope':'保持正常友好变化后的钳制和所有默认数据/公式，不能改述为所有友好变更都无钳制；不修参考，不宣称默认数据异常。','synchronize_files':['creature-rpg/wp30-growth-learning-and-friendship.md','creature-rpg/wp18-creature-identity-species-ownership.md','test-catalog/creature-rpg-wp18-20-24-25-26.md','test-catalog/creature-rpg-wp27-28-29-30-33.md'],'acceptance':'正式范围措辞与合法作者256→物种256→个体256不矛盾，普通对照保持；全部仍静态未执行。','dependencies':['K非负格式接受域','WP18创建静态合同','WP30变化入口负责后续修正']},
      {'id':'R6-D-PBS-C08','title':'ShadowSize0的None标签与资源查询0须限定观察层','impact_level':'LOW_PROPOSED_SCOPE_QUALIFICATION','source':[b.L(r.SCHEMA_DIR+'010_SpeciesMetrics.rb',59,87),b.L(fs.S+'010_Data/002_PBS data/009_Species_files.rb',156,178),b.L(fs.S+'011_Battle/004_Scene/006_Battle_Scene_Objects.rb',684,698)],'formal':[b.L(fs.WP73B,23),b.L(fs.WP73B,134,137),b.L(fs.F+'engine-overworld/wp15-resource-matching-and-audio.md',59,63)],'preconditions':'合法物种，无物种/形态自有影子图；指标ShadowSize0；人工资源解析夹具仅允许有效通用Shadow/0成功，前述资源缺席，图像装载成功；不推定参考目录实际含此资源，本快照无Graphics目录可验证。','ordinary_control':'0资源也缺席则无匹配位图；尺寸2且Shadow/2有效则请求2；自有影子存在时先用自有图。','minimal_counterexample':'阴影资源选择仍按数值0请求通用Shadow/0，已有有效0资源可形成位图；没有size0提前返回或指标shows_shadow按0抑制的分支。这里只断言请求/位图选择，不认证实际可见像素。','cancellation_exception_partial_commit':'资源选择不是用户取消事务；不替代指标编辑BACK恢复与保存门；媒体异常只沿实际前缀，不声称视觉成功。','negative_search':'已读shadow_filename/shadow_bitmap及指标shows_shadow没有数值0禁用门；WP73-B的0=None是选择器标签与基线约定，资源规格仍写Shadow/N通用分支。','necessary_consumers':[b.L(fs.S+'010_Data/002_PBS data/009_Species_files.rb',156,178)],'minimal_revision':'主审若认定原措辞会被读成无条件禁用，限定0=None为编辑标签/无0通用资源时的效果；保留参考实际资源请求。','preserved_scope':'不要求创建0资源，不推测实际渲染，不更改默认阴影图或编辑列表枚举。','synchronize_files':['demo-dx/wp73-b-world-editors.md','engine-overworld/wp15-resource-matching-and-audio.md'],'acceptance':'区分0标签、通用0路径请求及实际媒体可用性；若现有规格范围已足够，由非提出者明确反证取消提案。','dependencies':['资源主责对人工夹具及选择器标签范围裁决']},
    ]
    for x in new:x.update(proposal_status='PENDING_PARENT_REBUTTAL_OR_ADJUDICATION',non_proposer_review_required=True)
    a.save('findings.json',findings+new)
    # Static author-contract vectors are review proposals, never executed tests.
    vectors=[]
    for rule in rules:
        vectors.append({'id':'R6-D-V-'+rule['family']+'-'+rule['field'],'rule_id':rule['rule_id'],'premises':rule['premises'],'inputs':['Omit this field in an otherwise valid new record; forms use stated base-value premises.','Provide an explicit legal non-default ordinary value; preserve all other prerequisites.'],'observations':['Registered raw field / effective inherited field, before downstream overrides and localization.','Use only the named field consumer boundary; separate actual full action success.'],'expected_omission':rule['omission'],'expected_explicit':'Apply stated field normalization/override, then the named consumer; see rule for coupled wild-item/evolution/metrics behavior.','existing_vectors':rule['related_existing_vectors'],'status':'PROPOSED_DERIVED_VECTOR_NOT_EXECUTED'})
    a.save('proposed-author-vectors.json',vectors)
    # Exact scope boundary agreed by parent, rather than a hidden all-game duty.
    boundary={'in_scope':['All44 assigned PBS files, record identity/range and104 actually authored family×field combinations.','Schema, omission defaults, inheritance/replacement, validation and normalization, duplicate/repeat/order semantics, author writeback boundary.','Necessary direct consumers and named cross-domain effect/fallback/ability/evolution/flag entries; finite formal/test-vector comparison.','All per-record field presence/default/inheritance maps, conditional and phase-specific identities, embedded NaturalGift/Fling/DefaultForm input semantics.'],
    'outside_scope_handoffs':['Combat effect/ability/item/AI algorithm bodies beyond author entry binding (combat review C/K or relevant module owner).','Hardcoded growth/evolution method algorithm proofs beyond registered identity/parameter-kind (WP19/30/31/32 owners).','Other PBS families, encounters/trainer/facility/dungeon/demo cross-profile compatibility and runtime activation (parent).','Full compiler orchestration, all failure/recovery/serialization and real export execution (K).','Actual host, media, font/render pixels, game play, save data and full optional feature activation (resource/localization/serialized and parent owners).'],
    'not_inferred':['0 conditional unresolved identities does not establish complete compile or all-version support.','Byte identity does not import a historical semantic PASS.','Per-record applications are deterministic evidence joined to independently read human rules, not individual gameplay execution.','Formal gaps are proposals for a non-proposer; no final adjudication or PASS generated.']}
    a.save('scope-boundary-and-handoffs.json',boundary)
    protected={'bindings':a.bind(),'reference_status':a.git('status','--porcelain',cwd=a.REF),'protected_main_diff':a.git('diff','--name-only',a.MAIN,'--','reference','deliverables/final-specification-set','specs','planning','audit')}
    assert not protected['reference_status'] and not protected['protected_main_diff']
    a.save('protected-input-check.json',protected)
    status={'task':'R6-D/pbs-bulk','status':'REVIEW_COMPLETE_WITH_PROPOSALS_FOR_PARENT','scope':'Clarified PBS author fields and consumer wiring; downstream algorithm bodies are named handoffs.','PASS':False,'non_proposer_adjudication_pending':True,'files':44,'unique_blobs':29,'lines':206649,'records':16732,'actual_family_field_rules':104,'rules_including_omission_only_fields':116,'header_rules':9,'record_field_maps':len(forward),'record_field_applications':sum(applications.values()),'required_field_rule_reading_gaps':0,'missing_in_scope_semantic_rule_definitions':0,'remaining_in_scope_unread_records':0,'structural_reference_atoms':load('relations-summary.json')['reference_atoms'],'conditional_unresolved_reference_atoms':0,'phase_specific_reference_exceptions':len(stagefails),'embedded_flag_atoms':len(embedded),'embedded_natural_gift_types':sum('embedded_runtime_type_identity' in x for x in embedded),'unresolved_embedded_natural_gift_types':sum('embedded_runtime_type_identity' in x and x['type_location'] is None for x in embedded),'default_form_flags_without_corresponding_form_record':sum(x.get('corresponding_form_data_exists') is False for x in embedded),'default_form_missing_record_disposition':'12 path occurrences across6 active/Gen8 species; runtime selector and base fallback, not a compiler enum violation.','proposal_count':len(findings+new),'proposal_ids':[x['id'] for x in findings+new],'runtime':'NOT_EXECUTED','actual_model':'UNVERIFIED','actual_effort':'UNVERIFIED','tier':'UNVERIFIED','speed':'UNVERIFIED','runtime_uuid':'UNVERIFIED','prior_checkpoint':'Initial BLOCKED was incomplete work and overbroad downstream scope; continued at parent request until required PBS field semantics closed. No external blocker asserted.','next_owner':'Parent performs independent rebuttal/adjudication and integrates cross-domain handoffs; no formal files edited.'}
    a.save('task-status.json',status)
    # Verify all persisted JSON and compressed receipts after final rewrites.
    checked=[]
    for p in sorted(a.OUT.glob('*.json')):
        obj=json.loads(p.read_text())
        if isinstance(obj,dict) and obj.get('artifact_encoding')=='gzip_json':
            blob=(a.OUT/obj['artifact']).read_bytes();raw=gzip.decompress(blob)
            assert a.sha(blob)==obj['compressed_sha256'] and a.sha(raw)==obj['uncompressed_sha256'] and len(raw)==obj['uncompressed_bytes'];json.loads(raw)
        checked.append(p.name)
    a.save('artifact-validation.json',{'json_files_validated':checked,'gzip_receipts':'all byte-count and SHA256 checks succeeded','field_rule_required_reading_gaps':0,'record_maps':len(forward),'scope':'artifact and mapping integrity only; not behavior execution or PASS','protected_inputs_unchanged':True})
    print(json.dumps(status,ensure_ascii=False,indent=2))

if __name__=='__main__':
    a.append('command-log.jsonl',{'time':a.now(),'script':'finalize_scope.py','script_sha256':a.sha(Path(__file__).read_bytes()),'purpose':'finalize clarified PBS author scope, per-record rule applications, parent-adjudication proposals and explicit handoffs'})
    run()
