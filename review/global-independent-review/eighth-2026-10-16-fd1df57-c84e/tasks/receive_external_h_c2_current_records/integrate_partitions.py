"""Serialize explicitly accepted fixed A/C contributions, preserving readers.

This is a receiver-owned report serializer, never a primary-reading generator.
Acceptance was decided after reading every contribution judgment, interface and
counter plus common qualifications; structural checks and remote bytes alone
grant no semantic credit. Original partition code is never imported/executed.
"""
import datetime, hashlib, json
from pathlib import Path
T=Path(__file__).resolve().parent
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
RECEIVER='01a14465-f204-7783-a526-9b43e91ea005'
PARTITIONS={
 'A':{'commit':'75722b4d08a2cbafc93156a4099cf6750ad966ea','reader':'01a1448b-68af-70ff-b817-bacab22f0014','count':12,'groups':84,'files':123,'bytes':5840394},
 'C':{'commit':'86f054be0aad15de7a45d2a956d77612bc84bcb4','reader':'01a1448b-8afc-70f4-a964-6d2d89141000','count':11,'groups':77,'files':138,'bytes':4413600}}
NOTES={
 'GR7-M03-001':'接受非致死逐席继续及外层延迟消费；不接受作者扩张的致死终局推断。与显式专用中止的退款旁路分开。',
 'GR7-M03-002':'接受查询只读、true濒死首候选及直接球入口补救；不扩大到普通菜单保证或默认捕获故障。',
 'GR7-M04-001':'实际复制与成功后提示分开；无玩家/失败场景恢复及已提交前缀保留，optional未选。',
 'GR7-M04-102':'Hash登记与直接call失败、菜单配置effect消费者分开；不改登记政策，optional未选。',
 'GR7-M04-301':'接受主路径、命名前失败、一次回退和返回后SE请求，未把逻辑请求当截图/声音实测。',
 'GR7-M05-001':'接受零位移创建/正常完成/逐消费者顺序；强制路线及失败前缀不被普遍计步结论覆盖。',
 'GR7-M06-001':'接受小图/钳边/在途手动卷动反例与正常320到448；只保WR01的历史同步残留。',
 'GR7-M06-002':'接受逐入口尾部差异和静态帮助例外；不与净化室缺scene方法混作统一UI保证，保留O-002不同根。',
 'GR7-M07-001':'接受完整PID与高16位单位对照、统一守卫及查询阶段限定，optional未选。',
 'GR7-M07-002':'接受合法作者旗标使母动态提交先于子代显式提交；失败/领取容量后置不回滚，非默认全体产蛋。',
 'GR7-M08-001':'接受本步先捕获活动态后递减、耗尽取消和概率早退；与M05共享步链只计一次对象，optional未选。',
 'GR7-M09-001':'接受计划/成功击/实际基底求值三计量；吸收、替身和停止对照及不同AI消费者历史资格保留。',
 'GR7-H08-001':'接受新导航投影修正及Bag部分添加/请求数量反馈；冻结R6和两个optional facet不重开。',
 'GR7-M13-003':'接受abortable显式专用Exception绕过领域终局退款，正常undo及actioned门分开；optional未选。',
 'GR7-M15-002':'接受selected恰尾条件、Load已释放前缀/Delete尾添、BACK内存与外层Save差别；仅目录前提已修。',
 'GR7-D06-001':'接受完整21规范名字及有限字段/外层循环；_stricmp不等精确大小写，前序选择/装载/注册与设备桥仍未验证。',
 'GR7-M04-101':'接受准备/解压与eval保护阶段分界、前缀非事务；正向范围支持no-required，不造全局负检索。',
 'GR7-D07-001':'接受现有MIDI bank声明及脚本查找/缩放/有限重试；不选择未来SF2政策，不关闭原生消费与实际声音限制。',
 'GR7-J01-001':'接受三复合producer外部身份关系/显式0拒绝/别名重复/query及编译前缀；与M01整数比较不同根，旧C03映射债不倒改。',
 'GR7-H14-001':'接受UTIL03单末LF继承facet与历史Ruby局部回执；不重跑、不增加policy根、不推广PBS。',
 'GR7-POL-001':'接受字体偏置/数值测高/同Rect变异及失败前缀六向量；独立policy未选，实际像素未知。',
 'GR7-J16-001':'接受非空BGM返回先于登记再成员视觉；与满经验闪光及音频真实发声资格分开，正确L22保留。',
 'GR7-J16-003':'接受跨级先落1331再缺update失败及S0/双满正常返回清中心；未泛称所有EXP失败或存放成功才清。'}
def read(p):return json.loads(p.read_text())
def write(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def main():
    accepted=[];contributions={}
    for name,identity in PARTITIONS.items():
        P=T/'.work'/('partition-'+name);out=T/'partition-receptions'/name
        remote=read(out/'remote-readback.json');assert remote['commit']==identity['commit'] and remote['file_count']==identity['files'] and remote['bytes']==identity['bytes'] and remote['exact_path_mode_blob_collection_equal']
        checks=read(out/'structural-checks.json');assert checks['frozen_partition_exact_ids']
        judgments=read(P/('judgments.json' if name=='A' else 'adjudication.json'))
        interfaces=read(P/'interfaces.json')['records'];counters=read(P/'proposal-counters.json')['records']
        assert len(judgments)==identity['count']
        records=[]
        for j,i,c in zip(judgments,interfaces,counters):
            assert j['id']==i['id']==c['id'];rid=j['id'];assert rid in NOTES
            record=dict(id=rid,primary_reader=identity['reader'],fixed_delivery_commit=identity['commit'],
              contribution_judgment=j,contribution_interface=i,contribution_counter=c,
              parent_interface_receiver=RECEIVER,parent_interface_reception=NOTES[rid],
              accepted_scope='Complete assigned canonical/current seven groups/proposal/counter/necessary source and B8 facts through the named independent reader; parent accepts contribution and interfaces.',
              parent_primary_source_reread=False,parent_duplicate_primary_credit=0,
              no_new_behavior='NOT_EXECUTED',new_root_ACCEPTED_or_CLOSED=False)
            records.append(record);accepted.append(record)
        contribution=dict(schema='gr8.partition.fixed-contribution-reception/v1',utc=NOW,partition=name,**identity,
          receiver=RECEIVER,status='RECEIVED_COMPLETE_CONTRIBUTION_AND_INTERFACE',records=records,
          original_qualifications='Original PENDING/WAIT/null/failed states retained at their own time; B8 scoped closure distinct; optional/policy unselected; runtime/native/host limits unchanged.',
          original_model_effort_tier_speed_Fast='UNVERIFIED',new_required_proposals=0,root_task_final='NOT_GRANTED',
          actual_remote_readback='remote-readback.json',structural_checks='structural-checks.json',
          file_count_qualification='A fixed directory has123 files, independently read back. Parent message125 is not adopted as exact count.' if name=='A' else 'Exact fixed directory138 files independently read back.')
        write(out/'accepted-contribution.json',contribution);contributions[name]=contribution
    assert len(accepted)==23 and len({r['id'] for r in accepted})==23
    by_id={r['id']:r for r in accepted};ids=set(by_id)
    rec=read(T/'reception-ledger.json')
    direct=[r for r in rec['fully_received_records'] if r['id'] not in ids];assert len(direct)==4
    additions=[]
    for r in accepted:
        j=r['contribution_judgment'];name='A' if r['id'] in {v['id'] for v in contributions['A']['records']} else 'C'
        additions.append(dict(id=r['id'],status='RECEIVED_COMPLETE_PARTITION_CONTRIBUTION_AND_INTERFACE',
          meaning=j['meaning'],record_evidence=['partition-receptions/'+name+'/accepted-contribution.json',r['fixed_delivery_commit']+':continuation-results/'+name+'/reception-ledger.json'],
          source_spec_join=j.get('source_join',dict(source_labels=j.get('source_units'),B8_labels=j.get('B8_units'))),
          normal_control=j.get('examples','Complete original values received by named partition reader; parent interfaces accepted, not re-read as own primary work.'),
          failure_cancel_partial=j.get('cancel_failure',j['meaning']),reason=r['parent_interface_reception'],remaining=[],
          primary_reader=r['primary_reader'],parent_interface_receiver=RECEIVER,parent_primary_source_reread=False,
          historical_and_current_qualification=j.get('history',j.get('history_and_alias'))))
    rec['fully_received_records']=direct+additions
    rec['necessary_unreceived_records']=[r for r in rec['necessary_unreceived_records'] if r['id'] not in ids]
    rec['partition_integration_utc']=NOW;rec['direct_primary_records']=4;rec['accepted_partition_records']=23
    rec['root_task_final']='NOT_READY; B10 and D29 plus remaining common purposes/interfaces still OPEN'
    assert len(rec['fully_received_records'])==27 and len(rec['necessary_unreceived_records'])==10;write(T/'reception-ledger.json',rec)
    f=read(T/'frozen-denominator.json');received={r['id'] for r in rec['fully_received_records']}
    f['canonical_received_ids']=[r['id'] for r in f['canonical_records'] if r['id'] in received]
    f['canonical_unreceived_ids']=[r['id'] for r in f['canonical_records'] if r['id'] not in received]
    for r in f['canonical_records']:
        if r['id'] in ids:r.update(status='RECEIVED_VIA_FIXED_PARTITION_CONTRIBUTION',primary_reader=by_id[r['id']]['primary_reader'],delivery_commit=by_id[r['id']]['fixed_delivery_commit'])
    f['partition_integration_utc']=NOW;f['credit_provenance']='4 primary records read by this context;23 by independently named A/C readers and contribution/interface accepted here. No automatic hash or duplicate primary credit.';write(T/'frozen-denominator.json',f)
    remaining=read(T/'remaining-objects.exact.json')
    for r in remaining['objects']:
        r['fully_received']=r['id'] in received
        if r['id'] in ids:r['reception_provenance']=dict(primary_reader=by_id[r['id']]['primary_reader'],delivery_commit=by_id[r['id']]['fixed_delivery_commit'],parent_interface_receiver=RECEIVER)
    write(T/'remaining-objects.exact.json',remaining)
    reading=read(T/'reading-ledger.json');reading.update(canonical_groups_remaining=70,canonical_records_complete=27,canonical_records_unreceived=10,original_proposal_and_counter_complete=27,
      canonical_groups_received=189,canonical_groups_primary_read_by_this_context=28,canonical_records_primary_read_by_this_context=4,original_proposal_and_counter_primary_read_by_this_context=4,
      canonical_records_received_via_named_partitions=23,partition_integration_utc=NOW,
      partition_credit_rule='canonical_groups_read remains this context direct28. Complete received189 = direct28 + A84 + C77; records27 = direct4 + A12 + C11. No repeat primary reading/vote. Shared purposes still D-owned.')
    reading['accepted_partition_receipts']={n:dict(commit=v['commit'],reader=v['reader'],records=v['count'],groups=v['groups'],receipt='partition-receptions/'+n+'/accepted-contribution.json') for n,v in PARTITIONS.items()};write(T/'reading-ledger.json',reading)
    interface=read(T/'interfaces.json');interface['records']=[r for r in interface['records'] if r.get('id') not in ids]
    for r in accepted:interface['records'].append(dict(id=r['id'],producer='Fixed partition '+r['fixed_delivery_commit'],consumer='This receiver aggregate ledger',status='CONTRIBUTION_AND_INTERFACE_RECEIVED',facts=r['contribution_interface'],reason=r['parent_interface_reception'],primary_reader=r['primary_reader'],parent_primary_reread=False))
    interface['other_interfaces']='B10 canonical source/consumer bodies and D29/common operative purposes remain OPEN; no global signature.';write(T/'interfaces.json',interface)
    counters=read(T/'proposal-counters.json');counters['received_partition_counters']={n:dict(commit=v['commit'],reader=v['reader'],new_required=0,full_counters='partition-receptions/'+n+'/accepted-contribution.json',root_final='PENDING_MAIN_REVIEWER') for n,v in PARTITIONS.items()};write(T/'proposal-counters.json',counters)
    progress=read(T/'progress.json');progress.update(canonical_received=27,canonical_remaining=10,canonical_groups_received=189,canonical_groups_remaining=70,direct_primary_canonical=4,accepted_partition_canonical=23,
      partition_integration_utc=NOW,status_detail='A12/C11 complete fixed contributions and interfaces received; direct4 retained. B10 awaiting full delivery; D29/common purposes continuing after incomplete b3580. Still INCOMPLETE; root task-final not granted.')
    progress['parent_reported_started']={'A':'01a1448b-68af-70ff-b817-bacab22f0014','B':'01a1448b-49c1-72b6-b6ed-c8a724535018','C':'01a1448b-8afc-70f4-a964-6d2d89141000','D':'01a1448b-ab99-7002-850f-b61ed5c1100c'}
    progress['partition_state']={'A':PARTITIONS['A']['commit']+' RECEIVED_CONTRIBUTION_AND_INTERFACE','C':PARTITIONS['C']['commit']+' RECEIVED_CONTRIBUTION_AND_INTERFACE','B':'PARENT_REPORTED_RUNNING; no delivery received','D':'b3580edf37ca9e824297fc3118913794308abe1b PARENT_REPORTED_INCOMPLETE_CONTINUING; no completed semantic receipt'};write(T/'progress.json',progress)
    validation=read(T/'validation.json');validation.update(partition_integration_utc=NOW,canonical_equation='4+12+11+10=37',groups_equation='28+84+77+70=259',legacy_equation='2+29=31',A_C_exact_assignment_and_disjointness='PASS',A_C_current_value_and_source_identity_checks='PASS; identity only',A_remote='PASS;123files/5840394bytes',C_remote='PASS;138files/4413600bytes',whole_task_final='NOT_READY');write(T/'validation.json',validation)
    print(json.dumps(dict(received=27,remaining=10,groups_received=189,groups_remaining=70,legacy_received=2,legacy_remaining=29,status='INCOMPLETE'),ensure_ascii=False))
if __name__=='__main__':main()
