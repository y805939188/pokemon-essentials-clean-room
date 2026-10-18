"""Freeze dispatchable follow-up readsets; never create a task or imply a read."""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import subprocess

REPO=Path('/workspace/pokemon-essentials-clean-room')
TASK=Path(__file__).resolve().parent
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
C2='4580645dfbfec4a3c7ccbad56ae293cc619b0d25'
R6='9aa72bc99a4cf52c8fb9cad8a637a963341388b0'
C2ROOT='review/global-independent-review/seventh-2026-10-14-e646432-7a91/'
R7ROOT='review/remediation-seventh-20261015-prepare/'
R6ROOT='review/remediation-sixth-20261014-prepare/'
INDEX=REPO/(C2ROOT+'publication-transport/core/payload-index.json')

def git(*args):
    cache=TASK/'object-cache.git'
    argv=['git','--git-dir',str(cache),*args] if cache.exists() else ['git',*args]
    return subprocess.check_output(argv,cwd=REPO)

def ident(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}

def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def main():
    snapshot_root=TASK/('readset-materialized-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
    snapshot_root.mkdir()
    index=json.loads(INDEX.read_text())
    logical={x['logical_path']:x for x in index['logical_files']}
    encoded={x['transport_path']:x for x in index['compressed_objects']}
    treecache={}
    fixed_manifest=json.loads((TASK/'recovery-manifest.json').read_text())['files']
    recovered={(x['commit'],x['path']):x for x in fixed_manifest}
    cached_manifest=TASK/'cached-r6-recovery-manifest.json'
    if cached_manifest.exists():
        for x in json.loads(cached_manifest.read_text())['files']:
            recovered[(x['declared']['commit'],x['declared']['path'])]=x
    prior=json.loads((TASK/'reading-ledger.json').read_text())['entries']
    full_read={x.get('input',{}).get('path') for x in prior if x['status']=='FULL_READ'}
    full_read.update(R7ROOT+'review-receptions/'+p+'/report.md' for p in [
        'IR-R7-U01/r1','IR-R7-U03/r1-final','IR-R7-U06/r1-final',
        'IR-R7-U10/r1-complete','IR-R7-U12/r1-complete'])

    def row(commit,path,purpose,reading='UNREAD_BY_HISTORY_CURRENT'):
        if commit not in treecache:
            treecache[commit]=git('rev-parse',commit+'^{tree}').decode().strip()
        entry=git('ls-tree',commit,'--',path).decode().split()
        if not entry:
            return {'commit':commit,'path':path,'status':'MISSING_AT_COMMIT','purpose':purpose,'reading':reading}
        data=git('show',commit+':'+path)
        local=REPO/path
        current=local.is_file() and local.read_bytes()==data
        frozen=recovered.get((commit,path),{})
        local_path=str(local) if current else frozen.get('local_path')
        if not local_path:
            snapshot=snapshot_root/commit/path
            snapshot.parent.mkdir(parents=True,exist_ok=True)
            if snapshot.exists():
                assert snapshot.read_bytes()==data
            else:
                with snapshot.open('xb') as f:f.write(data)
            local_path=str(snapshot)
        out={'repository':str(REPO),'commit':commit,'tree':treecache[commit],
             'path':path,'mode':entry[0],**ident(data),'purpose':purpose,
             'reading':'FULL_READ_BY_HISTORY_CURRENT' if path in full_read else reading,
             'local_path':local_path,
             'materialization':'EXACT_EXISTING_BYTES' if current or frozen else 'GIT_SHOW_RESTORED_NEW_ISOLATED_SNAPSHOT',
             'semantic_credit_from_materialization':False}
        if '/review-receptions/' in path:
            reception=local.parent/'reception.json'
            if reception.exists():
                j=json.loads(reception.read_text());p=j.get('parent_receipt',{})
                if p:out['original_result_binding']={k:p.get(k) for k in ['result_commit','result_tree','prefix','reviewer_task_id','parent_reported']}
        return out

    def transport(path,purpose,reading='UNREAD_BY_HISTORY_CURRENT'):
        item=logical[path];e=encoded[item['transport_path']]
        direct=REPO/(C2ROOT+path)
        matches=[]
        for manifest in TASK.glob('*recovery-manifest.json'):
            try:
                for r in json.loads(manifest.read_text()).get('files',[]):
                    if r.get('logical',{}).get('logical_path')==path:matches.append(r['local_path'])
            except Exception:pass
        return {'repository':str(REPO),'commit':C2,'tree':treecache.get(C2),'logical_path':path,
                'path':C2ROOT+path,'mode':('100644' if item['mode']==420 else '100755' if item['mode']==493 else 'UNSUPPORTED_MODE'),
                'logical_posix_mode':oct(item['mode']),
                'bytes':item['bytes'],'sha256':item['sha256'],'git_blob':item['git_blob_content_id'],
                'tree_membership':'Decoded logical blob; immutable Git tree contains compressed transport path',
                'transport_path':C2ROOT+'publication-transport/core/'+item['transport_path'],
                'encoded_identity':e,'purpose':purpose,'reading':reading,
                'local_path':str(direct) if direct.exists() else (matches[0] if matches else None),
                'materialization':'LOCAL_BOUNDED_GZIP_WITH_DUAL_IDENTITIES',
                'semantic_credit_from_materialization':False}

    c2_primary=['canonical-records.json','findings.json','final-report.md','reading-ledger.final.json',
        'coverage/summary.final.json','history/qualifications.final.json',
        'history/inherited-nonmandatory.final.json','evidence/final-root-reception.json',
        'execution/phase-summary.final.json','handoff/cloud-seventh-update-handoff-prompt.md',
        'handoff/cloud-seventh-update-handoff-manifest.json','publication/final-delivery-binding.json',
        'handoff/batch-assignment.json','handoff/dependency-graph.json','handoff/file-conflict-graph.json']
    c2set=[row(C2,C2ROOT+p,'Current historical normative records, accepted scope, evidence/limits and purpose classification; authoritative fields require actual reading') for p in c2_primary]
    for p in ['tasks/R7-C13/chinese-contracts.json','evidence/aliases-and-tombstones.final.json',
              'coverage/current-interface-reception.json','tasks/R7-C19/final-adjudication-integrity.json',
              'tasks/R7-C17/canonical-supplement-purpose-index.json',
              'tasks/R7-C17/canonical-source-fact-registry.json','tasks/R7-C17/canonical-clause-registry.json',
              'tasks/R7-C17/canonical-program-index.json','tasks/R7-C17/limits-and-alias-reception.json',
              'evidence/root-h22-counter/counter-review-and-facets.json']:
        c2set.append(transport(p,'Classify every actual current semantic field; full referenced evidence only where it supports current facts/qualification. Pure former source/formal coverage indices remain historical purpose, not R8 approval.'))

    r7paths={R7ROOT+x for x in ['ledger.json','completion/final-report.md','completion/final-delivery-binding.json',
        'completion/final-publication-receipt.json','completion/formal-files.json','completion/current-public-reception.json',
        'completion/public-sync-manifest.json','completion/public-sync-validation.json','closure/final/decision.json',
        'closure/final/dependency-and-history-reception.json','closure/preflight/final-static-projection.json',
        'delegation/task-registry/current.json','current-navigation-errata.json',
        'process-adjudications/R7-U06-IR-PROC-001/v1/decision.json']}
    r7paths.update(str(p.relative_to(REPO)) for p in (REPO/R7ROOT/'review-receptions').glob('**/*') if p.is_file())
    r7paths.update(str(p.relative_to(REPO)) for p in (REPO/R7ROOT/'candidate-freezes').glob('**/candidate-input.json'))
    r7paths.update(str(p.relative_to(REPO)) for p in (REPO/R7ROOT/'acceptance').glob('**/decision.json'))
    r7paths.update(str(p.relative_to(REPO)) for p in (REPO/R7ROOT/'delegation/contracts').glob('*.json'))
    r7paths.update(str(p.relative_to(REPO)) for p in (REPO/R7ROOT/'integration').glob('**/integrated-input.json'))
    r7set=[row(B8,p,'All32 report versions, complete per-ID semantic scope,13 latest candidate freezes plus old U01 version,27 closure,7 shared receivers and finite dependency/history obligations; receipt identities inventory only where truly administrative') for p in sorted(r7paths)]

    nine=[R6ROOT+p for p in ['completion/final-delivery.json','ledger.json','task-register.json','reception-queue.json',
        'integration/public-sync-20261014/sync-input.json','integration/public-sync-20261014/dependency-status.json',
        'integration/public-sync-20261014/sync-report.md']]+['planning/feature-matrix.md','audit/source-traceability.md']
    r6set=[row(c,p,'Nine effective supplements: current56 rules, cases, consumers, staged acceptance and110 finite edges; original versus B8 successor identities separate') for c in [R6,B8] for p in nine]
    r6set.extend(row(R6,R6ROOT+'inputs/'+p,'Current nonmandatory source records; consume existing exact-field reading ledger, read any remaining effective semantics and preserve original proposal phase') for p in ['optional-records.json','optional-facets.json','policy-records.json','limit-records.json','no-required-revision-records.json'])
    r6set.extend(row(R6,str(p.relative_to(REPO)),'Original56 complete scope contracts referenced by current supplement; read complete relevant rule/case/consumer obligations') for p in sorted((REPO/R6ROOT/'contracts').glob('R6-U*.json')))
    r6set.append(transport('tasks/R7-C17/current56-contract-reception.json','Full56 scoped contracts and351 case reception, source/current clause premises; prior acceptance does not grant R8 source approval'))
    r6set.append(transport('tasks/R7-H01/recovered-manifest.json','Exact original R6 report manifest bytes (sha13ac2990...), equal to76038 original now verified in isolated cache; classify identity tables versus current retained contracts/evidence; restore is not reading'))
    for p in ['final-report.md','limits-and-missing-materials.md','execution-evidence.json','summary.md',
              'cloud-sixth-update-handoff-prompt.md','cloud-sixth-update-handoff-manifest.json','publication/final-delivery-binding.json']:
        r6set.append(row('76038a81fbb376ab318159e24268bd369cdec2ba',
            'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/'+p,
            'Exact original R6 report now available in isolated cache; classify/read current retained scope and supporting original evidence. Manifest/prompt repeated contracts may be associated only after exact structural/byte proof.'))
    for p in ['tasks/R7-H10/actual-independent-qualification-full.json','tasks/R7-H10/report.md']:
        r6set.append(transport(p,'Exact-field fallback and original A-E/5c scope binding; raw originals have now been fetched into isolated cache, fallback never replaces their missing semantic reading'))
    r6navigation=json.loads((TASK/'recovered-transport/history/recovery-identity-verification.json').read_text())
    for x in r6navigation:
        d=x['declared']
        if 'actual-reviews/' in d['path'] or 'acceptance-reviews/' in d['path']:
            matches=[p for p,v in logical.items() if v['sha256']==d['sha256']]
            if matches:
                rr=transport(matches[0],'Original actual content/final registry qualification; read original scope/phase without inheriting oldPASS')
                rr['original_identity']=d;r6set.append(rr)
            else:
                try:r6set.append(row(d['commit'],d['path'],'Original actual/final audit qualification'))
                except subprocess.CalledProcessError:r6set.append({**d,'materialization':'MISSING_GIT_AND_NO_EXACT_TRANSPORT_MATCH','reading':'UNREAD'})

    earlyset=[]
    for p in ['tasks/R7-H12/report.md','tasks/R7-H12/preserved-special-history.json','tasks/R7-H12/r5-activation-selections.json',
        'tasks/R7-H12/subreaders/r1/qualification.json','tasks/R7-H12/subreaders/r2/qualification.json',
        'tasks/R7-H12/subreaders/r3-r4/qualification.json','tasks/R7-H12/subreaders/r1/original-authorities.inventory.json',
        'tasks/R7-H12/earlier-round-qualification-full.json','tasks/R7-H05/execution-qualification.json',
        'tasks/R7-H05/report.md']:
        earlyset.append(transport(p,'R1-R5 exact original qualification and current succession only; full current rules/cases/premises, pure administrative/body-routing by exact identity, no unlimited old workflow recursion'))
    definitions=[
        ('H-C2-CURRENT-RECORDS','C2完整规范记录与有效事实/接收/分类/限制用途',c2set,
         '完整读取37规范记录与findings原提案/反证/别名，核中文合同/交接一致及accepted scope。对80MB manifest按真实结构分层；all_core_logical_payloads身份索引不授全文语义信用，其余当前规则/案例/依赖/事实/状态不得一概标行政。核当前有效facet/policy/limit以及支撑事实的精确证据。与原27关闭和B8当前条款分开。'),
        ('H-R7-FINAL-RECEPTIONS','R7候选/实际12contexts/最终依赖共享接收',r7set,
         '完整处理32报告版本、13批最新候选与旧U01r1、42任务ID、12实际contexts、27ID唯一主责、各MI/FI及正式接受关闭。U04/U05共享一次实际context；旧FAIL/WAIT和U06程序裁决分别接收，续审不增审者。完整读27依赖/关闭记录与七组共享/累计保留。当前已读6份实际报告可具名接收，剩余逐篇读；不以旧PASS代本轮内容。'),
        ('H-R6-EFFECTIVE-CONTRACTS','R6九项有效补充/56合同/351cases与原实际资格',r6set,
         '完整处置九项B8与9aa双版本；七份完全同字节、matrix/audit后继有改变。逐56合同、351case、110边及3联合接口读当前有效规则/前提/消费者/接受范围，行政/历史身份分列。nonmandatory已有当前字段实读可具名关联，但原proposal未读仍不可冒全读。原五实际内容/5c最终登记/b7接受/4df关闭不同阶段；U13旧FAIL/后继PASS准确恢复。'),
        ('H-EARLY-QUALIFICATIONS','R1-R5准确原资格/更正/有限后继',earlyset,
         'R1原WP/primary不臆造全局finding总数；R2 229/21/341分母；R3 23/76及OPTIONAL/NO_REQUIRED/U08原未启动；R4原17/76与B5 16/75、c492Summary有限后继区分；R5唯一92CLOSED 51P2/41P3与7optional/7no-required/6policy/13limits、410native/568schema/158extra保持。恢复SC-U07-001错LF前提/纠正排除与U03/U08旧FAIL后继范围；不无界递归旧行政副本。')]
    shards=[]
    for sid,title,rows,scope in definitions:
        unique={(r.get('commit'),r.get('path'),r.get('logical_path')):r for r in rows}
        rows=list(unique.values())
        readset=TASK/'dispatch-ready'/f'{sid}.readset.json'
        save(readset,{'schema':'r8.history.followup-readset.v1','shard_id':sid,'frozen_B8':B8,'frozen_R':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','scope':scope,'files':rows,
            'reading_credit_rule':'Identities/restoration/structure parsing do not create semantic reading. Consume exact already-read field receipts only with named reader/context and pointer range; every remaining effective semantic field must be actually read.',
            'recovery_tool':str(TASK/'recover_transport.py'),'recovery_tool_write_note':'Existing helper writes only its own TASK. For a new task, read it then create a reviewed copy inside the new authorized write root with TASK changed to that task directory. Use a previously absent recovered-NAME directory; do not execute restored programs.'})
        prompt=TASK/'dispatch-ready'/f'{sid}.md'
        prompt.write_text(f'''# 第八轮独立全局审查后续任务 {sid}\n\n你是新的实际独立审读context，任务为：{title}。\n\n先完整读取本报告根inputs/review-SKILL.md（clean-document-revision；3598bytes，SHA256ac3c8560f38192269b65b061673896a77f5eb794b90e90644e3c445b2c3be1f8）和合同 `{TASK/'contract.md'}`（36653 bytes，SHA25663944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b）及项目根AGENTS.md。B8唯一当前基线为{B8}，workspace tree751dfde81048c81390f89a65ca1d1a565ba8e1ca，formal treef292698cdd4a8e725525a9be6dc34b75faaf151e；R只读8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/tree7589c800b61ba13a13040ed0d686979b80a84fd0。R7C2为{C2}；R6原有效补充{R6}。实际路径项目{REPO}，R为/workspace/pokemon-essentials。\n\n请求gpt-6.1-sol/ultra/default普速，Fast关闭；实际model/effort/tier/speed与平台ID没有回显逐项UNVERIFIED，不查认证/额度。根会话需在正式派发时明确本任务唯一write_root和真实平台ID；未赋write_root前只读。不得自行spawn，父会话统一调度实际slots。不得改B8正文、planning/audit、R、历史报告/回执/main/tag，不commit/push；只写父会话授予的任务独立目录。\n\n范围：{scope}\n\n准确逐载荷readset：`{readset}`（{len(rows)}行载荷，{sum(r.get('bytes',0) for r in rows)} decoded bytes，重复版本身份保留）。逐行保留commit/path/mode/blob/bytes/SHA256及purpose、读状态、现存/恢复路径；这些计数不是语义阅读完成。现context已有读取证据为`{TASK/'reading-ledger.json'}`及current-nonmandatory-semantic-records.json、R7-stage-identity-audit.json；只能按精确字段/实际读者接收，不外推FULL_READ。\n\n先核材料可用性和恢复工具；需要恢复时先完整读懂helper，在自己的write_root内复制已读helper并只将TASK改为自己的目录，然后用新名字恢复到原先不存在且无symlink的隔离目录。保留原gz和编码/解码完整身份；恢复不执行证据程序，不授semantic credit。readset中original_result_binding/original_identity给原不可变来源，B8 reception副本需核同字节；若原对象缺失而精确gz可恢复，应分别登记Git可用性与实际载荷可用性。\n\n连续分块实读大JSON；纯行政/身份索引与当前有效语义分列，不把可读缺读改标limit，不借旧PASS代本轮。每条当前规则/前提/案例/依赖/状态/接收范围实际读到，完整ledger记录JSON pointer或连续行区间、identity、用途、实际读者及UTC。疑似问题用稳定GR8-HIST-或父分配ID，给双向定位/完整前提/普通对照/最小反例/最小修订/正确保留/独立反证待决，不自封required。\n\n输出progress.json、reading-ledger.json、purpose-dispositions.json、history/current acceptance语义记录、findings.json及unread.json。真实未读/未接收明确计数，向父会话反馈已读与准确缺口。行为初始NOT_EXECUTED/新增0；未实际执行的向量保持NOT_EXECUTED。最终状态UPDATE_NOT_STARTED。\n''')
        shards.append({'id':sid,'title':title,'status':'PLANNED_NOT_DISPATCHED','requested_configuration':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','Fast':False},
            'actual_platform_identity':'NOT_STARTED_UNVERIFIED','write_root':'PARENT_MUST_ASSIGN_AT_DISPATCH','scope':scope,
            'readset_path':str(readset),'readset_identity':ident(readset.read_bytes()),'prompt_path':str(prompt),'prompt_identity':ident(prompt.read_bytes()),
            'input_rows':len(rows),'input_decoded_bytes_with_versions':sum(r.get('bytes',0) for r in rows),
            'inputs_already_full_read_by_history_current':sum(r['reading']=='FULL_READ_BY_HISTORY_CURRENT' for r in rows),
            'dependencies':['Contract read and frozen-input identity check','Parent-assigned independent write root'],
            'blocking_semantic_dependencies':[],'independently_dispatchable_after_capacity_and_write_root_assignment':True})
    save(TASK/'subshards.json',{'schema':'r8.history.followup-shards.v1','recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'status':'PLANNED_NOT_STARTED','author':'/root/history_current','update_started':False,'root_manages_actual_slots':True,
        'not_a_model_or_runtime_certificate':True,'isolated_object_cache':str(TASK/'object-cache.git'),
        'cache_publication':'LOCAL_ONLY; do not commit nested bare repository; publish exact object/recovery receipts and selected restored evidence',
        'shards':shards})
    print(json.dumps([{k:s[k] for k in ['id','input_rows','input_decoded_bytes_with_versions','inputs_already_full_read_by_history_current']} for s in shards]))

if __name__=='__main__':
    main()
