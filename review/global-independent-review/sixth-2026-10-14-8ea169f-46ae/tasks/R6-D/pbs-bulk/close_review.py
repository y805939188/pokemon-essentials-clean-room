"""Explicit partial closeout. BLOCKED means real unread semantic scope remains."""
import audit as a, build_mappings as b, relations as r
from pathlib import Path
from collections import Counter, defaultdict
import json,re,gzip

def run():
    bindings=a.bind();records=r.readrecords();files=b.read('file-inventory.json');facts=b.read('behavior-facts.json')
    links=b.read('move-effect-consumer-links.json');formal=list((a.ROOT/'deliverables/final-specification-set').rglob('*.md'))
    codes={x['effect_identity'] for x in links};mentions=defaultdict(list)
    pat=re.compile(r'(?<![A-Za-z0-9_])('+('|'.join(sorted(map(re.escape,codes),key=len,reverse=True)))+r')(?![A-Za-z0-9_])')
    for p in sorted(formal):
        for n,line in enumerate(p.read_text().splitlines(),1):
            for code in set(pat.findall(line)):mentions[code].append({'path':str(p.relative_to(a.ROOT)),'line':n,'status':'literal_formal_mention_only_NOT_CLAUSE_SEMANTIC_APPROVAL'})
    for x in links:
        x['formal_effect_identity_mentions']=mentions.get(x['effect_identity'],[])
        x['status']='PRECISE_SOURCE_AND_FORMAL_LOCATION_DISCOVERY_ONLY; handler/formal semantics pending'
    a.save('move-effects-bidirectional-locations.json',links)
    # Every source/class location remains eligible for continuation, including
    # copies in optional backup paths; names alone are not implementation proof.
    ledger=[json.loads(x) for x in (a.OUT/'reading-ledger.jsonl').read_text().splitlines()]
    model=defaultdict(set)
    for x in ledger:
        if x['mode']=='model_visible_contiguous_read':model[x['path']].update(range(x['start_line'],x['end_line']+1))
    extent=[]
    for f in files:
        readlines=model[f['path']]
        missing=[];start=None
        for n in range(1,f['lines']+2):
            unread=n<=f['lines'] and n not in readlines
            if unread and start is None:start=n
            if not unread and start is not None:missing.append([start,n-1]);start=None
        extent.append({'path':f['path'],'total_lines':f['lines'],'model_visible_read_lines':len(readlines),'unread_direct_ranges':missing,'exact_byte_duplicate_of':f['same_blob_as'],'full_byte_inventory':True,'full_record_semantic_approval':False,'dedup_scope':'A byte duplicate can reuse inspected data values only after matching them; it does not reuse an old semantic PASS.'})
    a.save('direct-reading-coverage.json',extent)
    # Review candidates are proposals for parent adjudication. None is promoted
    # to a new defect when an existing formal clause already preserves it.
    findings=[
      {'id':'R6-D-PBS-C01','proposal_status':'DO_NOT_FILE_NEW_DEFECT_ALREADY_COVERED','title':'SHADOWSHED 无匹配 RemoveAllScreens 实现','impact_level':'NONE_AS_NEW_FINDING; would be material if spec claimed screen clearing','source':[b.L('reference/pokemon-essentials/PBS/Shadow Pokémon backup/moves_shadow_pkmn.txt',193,213),b.L(b.MV,57,68),b.L(b.SRC+'011_Battle/003_Move/004_Move_BaseEffects.rb',10,17)],'formal':[b.L(b.WP23,225,228),b.L(b.WP43,29,35),b.L(b.SPEC+'test-catalog/pokemon-rules-wp43-44-46-48-50.md',243)],'preconditions':'Optional move/type data validly loaded; no additional matching effect; ordinary gates reach the move-specific gate.','ordinary_control':'Known None/Physical move follows ordinary damage; separately valid RemoveAllScreensAndSafeguard has its own behavior.','minimal_counterexample':'Status/RemoveAllScreens sample reaches the generic unsupported-effect gate and fails rather than clearing screens.','cancellation_exception_partial_commit':'This review read the factory/fallback only; PP/history action prefix is specified in WP43 but the full caller chain is not re-reviewed here. No automatic refund claim.','negative_search':'All reference .rb top-level Battle::Move effect declarations scanned; sole unlocated bound name is RemoveAllScreens. Formal exact-name search finds explicit existing treatment.','necessary_consumers':['factory57–68','Unimplemented10–17'],'minimal_revision':'None proposed: preserve existing explicit fallback scope.','preserved_scope':'No automatic enabling of Shadow backups; no reference fix proposed; no enum-parse error inference.','synchronize_files':[],'acceptance':'Retain WP23/43 and existing FB05 vector; do not count this as a new unresolved defect.','dependencies':['Full action caller-chain semantic re-review remains open.']},
      {'id':'R6-D-PBS-C02','proposal_status':'DO_NOT_FILE_NEW_DEFECT_DUPLICATE_IS_MEMBERSHIP_INPUT','title':'两个形态 TutorMoves 重复标识','impact_level':'NONE_FOR_REVIEWED_COMPATIBILITY_QUERY','source':[b.L('reference/pokemon-essentials/PBS/pokemon_forms.txt',427,438),b.L('reference/pokemon-essentials/PBS/pokemon_forms.txt',1219,1228),b.L(b.CORE,708,714)],'formal':[b.L(b.SPEC+'creature-rpg/wp30-growth-learning-and-friendship.md',1)],'preconditions':'Valid EXEGGUTOR form1 / GIRATINA form1 and registered queried TRICKROOM / DOUBLETEAM; exact active and Gen8 bytes identical.','ordinary_control':'One occurrence returns affirmative compatibility.','minimal_counterexample':'A second identical atom still gives the same membership result; no duplicate-error or extra tutoring action follows from this reader.','cancellation_exception_partial_commit':'Compatibility query only; tutoring menu selection/consumption and cancellation are not re-reviewed.','negative_search':'All assigned list-valued fields checked; four path-specific duplicate fields are two active/Gen8 pairs.','necessary_consumers':['Pokemon compatible_with_move?708–714'],'minimal_revision':'No defect proposal from duplicate shape; full WP30 destination still pending.','preserved_scope':'Do not assert all duplicate lists are harmless or that the compiler globally deduplicates tutor moves.','synchronize_files':[],'acceptance':'Keep duplicates as authored data; do not invent rejection tests.','dependencies':['Full formal WP30 review and other consumers remain open.']},
      {'id':'R6-D-PBS-C03','proposal_status':'DO_NOT_FILE_NEW_DEFECT_EXISTING_101_RULE','title':'EffectChance=101 并非非法百分比','impact_level':'NONE_AS_NEW_FINDING','source':[b.L(r.SCHEMA_DIR+'005_Move.rb',34),b.L(b.SRC+'011_Battle/003_Move/003_Move_UsageCalculations.rb',489,498)],'formal':[b.L(b.WP43,157)],'preconditions':'Chance consumer reached; target Shield Dust gate and mold-breaker state evaluated first.','ordinary_control':'100 continues to ordinary modifier/debug branches; 101 returns before those branches.','minimal_counterexample':'Data chance101 must not be rejected solely for exceeding100; schema only requires a nonnegative integer.','cancellation_exception_partial_commit':'No action mutation or draw was executed; full additional-effect caller prerequisites remain separate.','negative_search':'Assigned literal values contain15 occurrences across profiles, no numeric shape failure; formal explicitly retains >100.','necessary_consumers':['pbAdditionalEffectChance489–498'],'minimal_revision':'None; preserve the existing >100 clause and avoid a new artificial [0,100] data restriction.','preserved_scope':'This is a chance calculation boundary, not a guarantee that the effect is applied.','synchronize_files':[],'acceptance':'No schema rejection from101; later shielding, force and callback conditions remain visible.','dependencies':['All15 per-record effects and complete application chains remain unreviewed.']},
      {'id':'R6-D-PBS-C04','proposal_status':'DO_NOT_FILE_NEW_DEFECT_RUNTIME_ASSOCIATION_ALREADY_SEPARATED','title':'BerryPlant→Item 不应误报为编译枚举依赖','impact_level':'NONE_AS_NEW_FINDING','source':[b.L(r.SCHEMA_DIR+'007_BerryPlant.rb',13,18),b.L(b.CP,268,278),b.L(b.BERRY,83,105)],'formal':[b.L(b.WP04,118),b.L(b.WP60,45,49)],'preconditions':'Compiler berry identity is symbolic; runtime may later query both item and berry data.','ordinary_control':'A current berry ID has both registries and can reach normal lookup.','minimal_counterexample':'Hypothetical valid symbolic berry section absent from Item is not rejected by these empty berry validators, although later item-dependent interaction can fail.','cancellation_exception_partial_commit':'No hypothetical input compiled or runtime mutation executed. Generic compiler may have already registered earlier sections before a later error; no transaction assumption.','negative_search':'All332 current/backup berry rows resolve to conditional Item registries; zero missing references does not prove a schema enum requirement.','necessary_consumers':['BerryPlant schema13–18','empty validators274–278','runtime strict lookup83–105'],'minimal_revision':'None; keep existing compile-vs-runtime distinction.','preserved_scope':'Do not certify arbitrary berry IDs usable, or entire backup compatibility.','synchronize_files':[],'acceptance':'Reference atom ledger labels this association runtime-only, not an enum check.','dependencies':['Full planting UI, item flag eligibility and exception paths remain open.']},
    ]
    a.save('findings.json',findings)
    protected={'bindings':bindings,'main_protected_diff':a.git('diff','--name-only',a.MAIN,'--','reference','deliverables/final-specification-set','specs','planning','audit'),'reference_worktree_status':a.git('status','--porcelain',cwd=a.REF),'new_output_root':str(a.OUT),'read_only_reference':True}
    assert not protected['main_protected_diff'] and not protected['reference_worktree_status'],protected
    a.save('protected-input-check.json',protected)
    summary=b.read('relations-summary.json')
    status={'task':'R6-D/pbs-bulk','status':'BLOCKED','completion_claim':False,'blocking_reason':'真实语义缺读：尚未逐记录完成全部实际消费者、配置前提、正式条款及相关向量的双向闭合。不得用parse/identity联接、旧结果或字节去重冒充本轮语义PASS。','inputs':bindings,'files':44,'unique_blobs':29,'total_lines':206649,'records':16732,'full_semantic_closed_records':0,'full_semantic_pending_records':16732,'field_structures_bound':104,'reference_atoms_checked':summary['reference_atoms'],'conditional_unresolved_atoms':summary['conditional_unresolved_atoms'],'literal_shape_exceptions':summary['shape_exceptions'],'limited_static_behavior_facts':22,'literal_shadow_table_rows_matched':153,'new_confirmed_findings':0,'candidate_proposals_not_new_defects':4,'formal_reverse_mapping':'PARTIAL, not complete clause universe','runtime_evidence':'NOT_EXECUTED','runtime_metadata':{'actual_model':'UNVERIFIED','actual_effort':'UNVERIFIED','service_tier':'UNVERIFIED','speed':'UNVERIFIED','runtime_uuid':'UNVERIFIED'},'necessary_next_work':['Read every pending semantic data unit and all required consumer/configuration contexts; begin with unique non-shadow species/forms/moves/items and domain-specific formal contracts.','Resolve receiver types for runtime-consumer-candidates rather than treating lexical matches as proven data consumers.','Finish full field semantics and exact formal/test-vector mapping; all records remain explicitly pending until then.','Revisit variant premises with other PBS domains (encounters/trainers/facilities/demo) owned by the parent; this audit intentionally excludes those files.','Only after semantic unread=0 may this scope be assessed for completion.']}
    a.save('task-status.json',status)
    # Check all gzip receipts and JSON syntax. This validates artifacts, not rules.
    verified=[]
    for p in sorted(a.OUT.glob('*.json')):
        obj=json.loads(p.read_text())
        if isinstance(obj,dict) and obj.get('artifact_encoding')=='gzip_json':
            blob=(a.OUT/obj['artifact']).read_bytes();raw=gzip.decompress(blob)
            assert len(raw)==obj['uncompressed_bytes'] and a.sha(raw)==obj['uncompressed_sha256'] and a.sha(blob)==obj['compressed_sha256']
            json.loads(raw)
        verified.append(p.name)
    a.save('artifact-validation.json',{'json_files_validated':verified,'gzip_receipts':'all checked hashes/byte counts and parsed','scope':'artifact integrity only; not behavioral tests or semantic approval','protected_inputs_unchanged':True})
    print(json.dumps({'status':'BLOCKED','semantic_pending':16732,'json_files_validated':len(verified),'new_confirmed_findings':0,'limited_facts':22,'proposals_not_new_defects':4},ensure_ascii=False,indent=2))

if __name__=='__main__':
    a.append('command-log.jsonl',{'time':a.now(),'script':'close_review.py','script_sha256':a.sha(Path(__file__).read_bytes()),'purpose':'truthful partial closeout, uncertainty/negative controls, artifact-integrity checks'})
    run()
