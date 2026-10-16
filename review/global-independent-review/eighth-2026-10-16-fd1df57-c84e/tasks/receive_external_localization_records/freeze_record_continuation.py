"""Freeze four exhaustive disjoint record contracts; no reading or worker start credit."""
from pathlib import Path
import hashlib
import json
import subprocess
import datetime

T=Path(__file__).resolve().parent
REPO=T.parents[4]
PREFIX=str(T.relative_to(REPO))
INPUT='805468320bf8a44499f6d59f53820215b27899fb'
ORIGINAL='90b9e27ef03feb2c018bb2f258b5e0d5aaed012b'
CONTRACT='40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
B='fd1df570cad987dc3852a3b958f03916e317f7fe'
DEST=T/'continuation'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()

def load(path):return json.loads((T/path).read_text())
def put(path,obj):
    p=DEST/path;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def fileid(path,commit=INPUT,repo=REPO/'.git'):
    data=subprocess.check_output(['git','--git-dir='+str(repo),'show',commit+':'+path])
    entry=subprocess.check_output(['git','--git-dir='+str(repo),'ls-tree',commit,'--',path]).decode().split()
    return {'commit':commit,'path':path,'mode':entry[0],'git_blob':entry[2],'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
def localid(path):
    data=path.read_bytes()
    return {'path':str(path.relative_to(REPO)),'mode':'100644','bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob_content_id':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}

f=load('frozen-denominator.json')
old=load('evidence/recovered-target/reading-ledger.json')
forward=load('evidence/recovered-target/forward-mapping.json')
raw={Path(x['source']).stem:(T/'evidence/primary-reference'/Path(x['source']).name).read_text(encoding='utf-8-sig').splitlines() for x in load('evidence/primary-identities.json')}
oldunits={x['id']:x for x in old['units']}
oldforward={x['unit']:x for x in forward['records']}
records=[]
for x in f['primary_objects']:
    if x['kind']!='record' or x['literal_read_here']:continue
    domain=Path(x['source'][2:]).stem;n=int(x['id'].split('-')[-1])
    key,value=raw[domain][2*n+2:2*n+4]
    assert key==value # All five unequal pairs were explicitly read before this freeze.
    records.append({**x,'domain':domain,'record':n,'key':key,'value':value,'weight':len(key.encode())})
assert len(records)==10264
groups=[[] for _ in range(4)];total=sum(x['weight'] for x in records);index=0;acc=0
for x in records:
    if index<3 and acc>=total*(index+1)/4:index+=1
    groups[index].append(x);acc+=x['weight']
assert len({x['id'] for g in groups for x in g})==10264

root='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
contracts=[fileid('AGENTS.md',CONTRACT),fileid(root+'/inputs/eighth-global-review-prompt.md',CONTRACT),fileid(root+'/inputs/review-SKILL.md',CONTRACT),fileid(root+'/delegation/prompts/receive_external_localization_records.md',CONTRACT)]
shared=[fileid(PREFIX+'/'+name) for name in ['report.md','interfaces.json','reception-ledger.json','evidence/recovered-target/review.md','evidence/recovered-target/continuation-review.md','evidence/necessary-source/F-wp08-localization.md','evidence/necessary-source/R-003_Intl_Messages.rb']]
common_paths=['Data/Scripts/021_Compiler/001_Compiler.rb','Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb','Data/Scripts/010_Data/001_GameData.rb']
common_R=[fileid(path,R,'/tmp/r8-elr-reception-reference.git') for path in common_paths]
all_ids=set();entries=[]
for index,g in enumerate(groups):
    task='records_'+chr(97+index);domains=list(dict.fromkeys(x['domain'] for x in g));runs=[]
    for x in g:
        if runs and runs[-1]['domain']==x['domain'] and runs[-1]['last']+1==x['record']:runs[-1]['last']=x['record']
        else:runs.append({'domain':x['domain'],'first':x['record'],'last':x['record']})
    for run in runs:
        run['count']=run['last']-run['first']+1;run['physical_lines']=[2*run['first']+3,2*run['last']+4]
    assert sum(x['count'] for x in runs)==len(g)
    keymetadata=[];templates={}
    for domain in domains:
        selected=[x for x in g if x['domain']==domain]
        units=[oldunits[x['id']] for x in selected]
        maps=[oldforward[x['id']] for x in selected]
        pure={'id','identity','lines','record','key_sha256','translation_sha256'}
        semantic={k:units[0][k] for k in units[0] if k not in pure}
        assert all({k:v for k,v in x.items() if k not in pure}==semantic for x in units)
        mapping={k:v for k,v in maps[0].items() if k!='unit'}
        assert all({k:v for k,v in x.items() if k!='unit'}==mapping for x in maps)
        templates[domain]={'complete_original_unit_semantic_fields':semantic,'complete_original_forward_fields':mapping}
    for x in g:
        u=oldunits[x['id']]
        keymetadata.append({k:u[k] for k in ['id','identity','lines','record','key_sha256','translation_sha256']})
    factgroups=[x for x in forward['fact_groups'] if x['domain'] in domains]
    put(Path('contracts/readsets')/(task+'.original-semantic-fields.json'),{'schema':'gr8-elr-exact-per-domain-original-semantics/v1','templates':templates,'fact_groups':factgroups,'qualification':'重复语义字段由严格JSON值相等验证共享一次；原审者FULL和WAIT_ROOT都是原时点，不能转授新审者。原每记录所有业务字段均在此显示，文字值另在records.view.txt全文呈现。'})
    put(Path('contracts/readsets')/(task+'.identity-only-index.json'),{'schema':'gr8-elr-record-original-identity-fields/v1','pure_identity_fields':['id','identity','lines','record','key_sha256','translation_sha256'],'rows':keymetadata,'purpose':'完整对象集合和来源身份索引；字段仅表示位置/字节身份，绝不作为本轮值已读或业务接收。'})
    view=['# Complete literal fields, fixed R. Generation grants zero reading credit.', '# Each Rn = JSON string explicitly means raw_key == raw_translation == that full literal.', '# Stable ID: ELR-{DOMAIN}-{n:04d}; physical source lines: 2*n+3 / 2*n+4.', '# This is a reversible audit view, not compiler input; original file first record, section and whole-file context govern parsing.']
    for run in runs:
        domain=run['domain'];view.append('DOMAIN '+domain+' records '+str(run['first'])+'..'+str(run['last']))
        view.append('FULL_SOURCE_HEADER '+json.dumps(raw[domain][:4],ensure_ascii=False))
        view.extend('R'+str(x['record'])+' = '+json.dumps(x['key'],ensure_ascii=False) for x in g if x['domain']==domain and run['first']<=x['record']<=run['last'])
    viewpath=DEST/'contracts/views'/(task+'.records.view.txt');viewpath.parent.mkdir(parents=True,exist_ok=True);viewpath.write_text('\n'.join(view)+'\n')
    sourcefiles=[fileid(PREFIX+'/evidence/primary-reference/'+domain+'.txt') for domain in domains]
    getters=list(dict.fromkeys(x['receiver']['identity'][2:] for x in factgroups))
    required_R=common_R+[fileid(path,R,'/tmp/r8-elr-reception-reference.git') for path in getters]
    write_set=PREFIX+'/continuation/parts/'+task+'/'
    readset={'schema':'gr8-elr-disjoint-record-reception-contract/v1','utc':NOW,'id':'receive_elr_'+task,'status':'FROZEN_PLANNED_NOT_STARTED','input_commit':INPUT,'input_checkout_tree':'97b364e728d7919cef0194bc4fb7c247ab0c83e8','input_task_tree':'3de2c017fd12b4b92238fcbe3c526e8824345dac','original_target_commit':ORIGINAL,'parent_contract_commit':CONTRACT,'B8':B,'formal_tree':'f292698cdd4a8e725525a9be6dc34b75faaf151e','R':R,'R_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','excluded_author_contexts':['01a143ad-a413-739d-b640-d4896e2e5029','01a14465-d18e-725b-b69c-2e6f52300005'],'exclusive_write_set':write_set,'dedicated_branch':'codex/r8-elr-'+task.replace('_','-')+'-20261016','record_denominator':len(g),'record_fields_denominator':2*len(g),'literal_bytes_for_scheduling_only':sum(x['weight'] for x in g),'ordered_runs':runs,'record_ids':[x['id'] for x in g],'complete_contract_files':contracts,'shared_current_files':shared,'source_primary_files':sourcefiles,'required_R_definition_files':required_R,'definition_scope':'完整Intl823、相关GameData注册/数据构造/getter、Compiler.pbEachSection及具名producer完整函数；同文件无关巨方法不自动纳全，原locator不足必须向完整定义扩展并登记。','required_original_semantics':localid(DEST/'contracts/readsets'/(task+'.original-semantic-fields.json')),'pure_identity_index':localid(DEST/'contracts/readsets'/(task+'.identity-only-index.json')),'literal_view':localid(viewpath),'source_file_header_scope':'每个assigned域原四行头全文；跨shard共享，只作明确去重，不增加记录数。','direct_interfaces':['ELR-RECORD-PIPELINE','ELR-DOMAIN-PRODUCER-GETTER','ELR-TO-PARENT-SEVEN-INTERFACES'],'parent_retains':['ELR-I01','ELR-I02','ELR-I03','ELR-I04','ELR-I05','ELR-I06','ELR-I07'],'excluded_obligations':'不重审全系统、全PBS玩法、全部UI/战斗域、不重开R7的27；不重新把父433对计入自身记录分母；不自动批准七接口。','original_recovery_reuse':'优先读取INPUT805固定Git路径，复用已核原输入；不得要求再恢复全213或重读9MB行政台账。只有自己的必要输入需身份核对。无本地文件时普通fetch固定INPUT/R并按精确path恢复到自己写集。','execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True,'worker_start_count':0,'parent_signature':'Actual worker full record scope only; parent task-final and seven-interface cumulative signature remain parent-owned.'}
    readset['common_contract']=localid(DEST/'contracts/COMMON-CONTRACT.md')
    put(Path('contracts/readsets')/(task+'.complete.json'),readset)
    spans='\n'.join('- '+x['domain']+': '+str(x['first'])+'–'+str(x['last'])+'（'+str(x['count'])+'对）' for x in runs)
    prompt=f'''# 第八轮 localization_records 连续记录完整接收：{task}

这是用户明确授权主线程新建实际不同上下文并行的完整子合同，当前尚未启动。你不是原作者或父接收者；实际context必须核对并与readset排除名单不同。父主责七接口整合，本任务完整承担下列全部记录值、原逐记录有效语义、必要定义/域producer/getter与限定反向条款。不得只作计数、导航或摘要。

先从父派发实际固定的**本合同发布提交**读取本prompt、相邻 `../readsets/{task}.complete.json` 和 `../COMMON-CONTRACT.md`。随后先完整读readset的AGENTS、36,653B全局prompt、review-SKILL以及父原完整接收prompt，再完整读本readset全部字段。合同提交由派发消息固定；不得用同名分支的未来HEAD代替。载荷输入唯一固定 `{INPUT}`，原目标 `{ORIGINAL}`；B8 `{B}`，R `{R}`。readset记录全部mode/blob/bytes/SHA/tree及用途，不依赖父本地缓存。

## 全部独占记录分母：{len(g)}对 / {2*len(g)}字段

{spans}

稳定ID与精确物理行已冻结。跳号是父433对的已读集合或前一shard边界，不是遗漏许可。必须用readset IDs逐个收口；本任务范围内部未读必须0才可声明自身完成。四合同互斥覆盖剩余10,264对，不能借当前任务的局部原文件范围外推整文件批准。

## 必读语义、定义与消费者

逐连续range实际全文呈现records.view中的**每个完整字面值**；`Rn = literal`明确定义为该记录两个字段都等于完整literal。所有五处不同字段已留父范围，本任务仍须独立机械核这项前提，不用哈希代替文本阅读。原文件BOM/CRLF/字节身份分列；必须读原四行头。分片视图不是新的编译输入，不能把本片首条当原文件首条改变形态解释。

完整读original-semantic-fields.json中按域共用的原unit全部业务字段、原forward字段及每个完整fact_group。共享只基于严格JSON值相等，原FULL/PASS/WAIT是原审者状态。identity-only-index只含具名纯位置/哈希字段，可完整按此用途处置；当前业务文字不可塞进纯身份豁免。

全文读Intl823和WP08。独立读对应数据构造、缺省、getter和原编译消息producer的**完整函数含结束行和全部门**；Compiler.pbEachSection、GameData必要注册/读取定义同理。原fact_group定位只是导航，范围截断不算完整函数。核默认core过滤、set/add、文本真实ID/哈希域、原始字段/译文值/规范键、选中语言game→core、空串/nil及异常分层；名称/叙述不证明效果已实现、文本相等不证明PBS注册数相等。必要R文件身份及有限来源在readset，不必重审这些巨文件的无关玩法。

普通成功、缺译/空译、导出取消、先删后写、完整导入先截断、失败/部分提交和无语言配置默认均须给具体有前提的解释。原语料与运行当前语言分开。若本记录只为默认文本数据，明确其数据意义及有限链，不宣称每个字面路径或叙述都可达。对未接收的UI、PBS、媒体、历史消费者逐个具名OPEN；原必要producer未实读时不得签consumer。广义七接口交给父整合，不在这里以外域全文债务冒充你的原记录值已接收。

必须反向核本域涉及WP08条款及原forward.spec_clauses，完整必要上下文与反方解释，保持现正确scope。不得用“其它owner已读”代替收到其完整有限贡献；可以自己实际补读必要完整定义。新疑似缺口保留完整提案及最强no-required/现跨篇覆盖解释，实际独立反证交父；不得从本任务原作者自签裁决required。

## 输出、权限与完成

唯一写集 `{write_set}`，专用分支 `{readset['dedicated_branch']}`。其它parts、父公共台账、正式规格、R、历史目录及main/tag只读。不得自行spawn；需要真正拆分时先提交完整剩余合同给父，不能改角色名冒新审者。不整改、不合并、不安装、不执行恢复的旧脚本或游戏；行为均NOT_EXECUTED。用户已授权独立review专用分支报告证据普通commit/push，不强推，不新增/移动tag。

首批生成frozen-denominator.json、reading-ledger.json、reception-ledger.json、interfaces.json、proposal-counters.json、report.md。每记录给ID、完整意义/必要前提、R与B8定位、实际读片/输出凭证、消费者接合、理由、未决和原字节身份。共同语义可以完整定义一次后逐对象精确引用，但不能批量模板宣称“全部人工通过”。持续实读到本全分母0未读；所有失败/截断和后继补读保存。原始平台I/O无权威字段逐项UNVERIFIED，不倒填UTC。

全部完成本有限合同及必要定义/接口后，只能声明 `READY_FOR_PARENT_RECORD_RECEPTION`；尚缺任一必要值/定义则 `INCOMPLETE`，不能写全局PASS或父task-final。普通push后只核自身新增/改变载荷完整远端mode/blob/bytes/SHA/集合/tree；精确不变输入复用，不制造大量重复回执。最终给真实C/tree/任务tree和正文证据路径。请求gpt-6.1-sol/ultra/default普速/Fast off，实际逐项无权威回显则UNVERIFIED；所有行为执行与工具核验分列，UPDATE_NOT_STARTED。
'''
    promptpath=DEST/'contracts/prompts'/(task+'.md');promptpath.parent.mkdir(parents=True,exist_ok=True);promptpath.write_text(prompt)
    entry={'id':'receive_elr_'+task,'worker_status':'PLANNED_NOT_STARTED','record_count':len(g),'record_ids':readset['record_ids'],'runs':runs,'exclusive_write_set':write_set,'branch':readset['dedicated_branch'],'prompt':localid(promptpath),'readset':localid(DEST/'contracts/readsets'/(task+'.complete.json')),'view':localid(viewpath),'original_semantics':readset['required_original_semantics'],'identity_index':readset['pure_identity_index']}
    assert not (all_ids&set(entry['record_ids']));all_ids.update(entry['record_ids']);entries.append(entry)
put(Path('contracts/dispatch.json'),{'schema':'gr8-elr-four-disjoint-record-dispatch/v1','utc':NOW,'status':'FROZEN_PLANNED_NOT_STARTED','input_commit':INPUT,'original_target_commit':ORIGINAL,'root_contract_commit':CONTRACT,'original_records':10697,'parent_already_literal_read_records':433,'remaining_record_denominator':10264,'remaining_fields':20528,'workers':entries,'worker_count':4,'worker_start_count':0,'actual_new_contexts_created_here':0,'requested_configuration':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default normal','Fast':'off'},'parent_integrator_context':'01a14465-d18e-725b-b69c-2e6f52300005','parent_retains':['ELR-I01','ELR-I02','ELR-I03','ELR-I04','ELR-I05','ELR-I06','ELR-I07'],'pairwise_disjoint':True,'union_exactly_all_remaining':True,'non_record_debts_not_removed':'Father retains all necessary PBS35 field values, 125 reverse-linkage objects, historical original qualification and target operative payload/pure-administrative purpose accounting. Four record starts do not mark any of these accepted.','UPDATE_NOT_STARTED':True})
print(json.dumps({'workers':4,'started':0,'records':len(all_ids),'counts':[len(g) for g in groups],'literal_bytes':[sum(x['weight'] for x in g) for g in groups],'exclusive_sets':[x['exclusive_write_set'] for x in entries]},ensure_ascii=False))

if __name__=='__main__':
    pass
