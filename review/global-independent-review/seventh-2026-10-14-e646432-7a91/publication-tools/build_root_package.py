"""Root-owned final handoff renderer. It never launches update work or mutates Git.

P03's actual cloud-path prerequisite cannot be certified before the human starts
the future cloud task. This renderer preserves that unknown explicitly, rather
than supplying a fictitious path or changing the completed domain evidence.
"""
import argparse
import collections
import gzip
import hashlib
import json
import re
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT.parents[2]
B='e646432c644dec04d306842cc5a559a29c718fbc'
FT='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
def ident(raw):
    return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
            'git_blob_content_id':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}
def pretty(v):return json.dumps(v,ensure_ascii=False,indent=2)+'\n'
def read(p):return json.loads(p.read_bytes())
def git(*argv):return subprocess.check_output(['git','-C',str(PROJECT),*argv])
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--core',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
    out=Path(a.output).resolve()
    if ROOT not in out.parents or out.exists():raise ValueError('new output within report required')
    if not re.fullmatch('[0-9a-f]{40}',a.core):raise ValueError('immutable full core commit SHA required')
    rr=str(ROOT.relative_to(PROJECT));core=a.core
    if git('rev-parse',core+':deliverables/final-specification-set').decode().strip()!=FT:raise ValueError('core formal tree changed')
    git('merge-base','--is-ancestor',B,core)
    core_id={'commit':core,'workspace_tree':git('rev-parse',core+'^{tree}').decode().strip(),
             'report_path':rr,'report_tree':git('rev-parse',core+':'+rr).decode().strip()}
    prefix=rr+'/publication-transport/core';index_raw=git('show',core+':'+prefix+'/payload-index.json');index=json.loads(index_raw)
    logical={v['logical_path']:v for v in index['logical_files']}
    objects={v['sha256']:v for v in index['compressed_objects']}
    def core_read(rel):
        row=logical[rel];obj=objects[row['sha256']]
        encoded=git('show',core+':'+prefix+'/'+row['transport_path'])
        actual=ident(encoded)
        if any(actual[k]!=obj['transport_'+k] for k in ('bytes','sha256','git_blob_content_id')):
            raise ValueError('encoded core member mismatch '+rel)
        raw=gzip.decompress(encoded)
        if any(ident(raw)[k]!=row[k] for k in ('bytes','sha256','git_blob_content_id')):
            raise ValueError('decoded core member mismatch '+rel)
        return raw
    def core_json(rel):return json.loads(core_read(rel))
    def core_text(rel):return core_read(rel).decode('utf8')
    approval=core_json('evidence/final-root-reception.json')
    if approval['status']!='FINAL_REVIEW_INPUT_ACCEPTED' or approval['effective_unread'] or approval['pending']:
        raise ValueError('actual final root reception missing')
    for rel,h in approval['accepted_payload_sha256'].items():
        if logical[rel]['sha256']!=h:raise ValueError('core accepted payload mismatch '+rel)
    root_records=core_json('findings.json');zh=core_json('tasks/R7-C13/chinese-contracts.json')
    canonical=core_json('canonical-records.json');plan=core_json('batch-plan.final.json')
    for d in (root_records,zh,canonical):
        if len(d['records'])!=37:raise ValueError('37 record denominator')
    if len(plan['batches'])!=13 or len(plan['primary_batch_by_required'])!=27:raise ValueError('13/27 batch denominator')
    if collections.Counter(v['classification'] for v in root_records['records'])!={'required':27,'optional':7,'no_required_revision':1,'policy':2}:raise ValueError('classification drift')
    sections={name:core_json(rel) for name,rel in approval['json_sections'].items()}
    fixed=core_json('startup/fixed-inputs.json')
    def binding(rel):
        row=logical[rel]
        return {'logical_path':rel,'core_commit':core,'core_report_tree':core_id['report_tree'],
                **row,'actual_encoded_tree_member':prefix+'/'+row['transport_path']}
    # Every logical file has its full original identity and purpose, and every
    # actual encoded member has a separate content/tree identity in this index.
    manifest={'schema':'r7.root-final-handoff-manifest.v1','status':'MANUAL_UPDATE_HANDOFF_READY',
              'update_started':False,'update_status':'UPDATE_NOT_STARTED','fixed_inputs':fixed,
              'core':core_id,'external_publication_binding':{'path':rr+'/publication/final-delivery-binding.json',
                 'mechanism':'C0_CORE_C1_HANDOFF_C2_EXTERNAL_PUBLICATION_BINDING','self_commit_tree':None,
                 'qualification':'C1 package identity is bound by the later C2 file; C2 own immutable commit is given in final delivery. No recursive self hash.'},
              'future_environment':{'local_project':str(PROJECT),'local_reference':fixed['reference']['path'],
                 'actual_cloud_paths':'UNVERIFIED_FUTURE_TASK_NOT_STARTED',
                 'startup_rule':'手动启动后解析实际仓库绝对路径，核B/R/tag/tree及只读材料；保存原路径到实际路径映射，不假称本机绝对路径就是云端路径。'},
              'root_records':root_records,'canonical_records':canonical,'complete_chinese_contracts':zh,
              'coverage_and_qualification_sections':sections,'batch_assignment':plan,
              'dependency_graph':core_json('dependency-graph.json'),'file_conflict_graph':core_json('file-conflict-graph.json'),
              'all_core_logical_payloads':index,'core_transport_index':{'path':prefix+'/payload-index.json',**ident(index_raw)},
              'accepted_payload_bindings':{rel:binding(rel) for rel in approval['accepted_payload_sha256']},
              'optional_navigation_facets':core_json('evidence/root-h22-counter/counter-review-and-facets.json'),
              'classification_counts':{'required':27,'required_severity':{'P2':10,'P3':17},'optional_entries':7,
                 'optional_new_roots':5,'optional_inherited_root_aliases':2,'additional_optional_navigation_facets':2,
                 'no_required_revision':1,'policy_entries':2,'policy_new_roots':1,'inherited_policy_qualification_facets':1,
                 'R6_inherited_separate':{'optional':8,'FLOAT':1,'policy':7,'limits':14,'no_required_revision':1}},
              'payload_recovery':'完整core传输索引逐载荷保存原bytes/SHA/content-blob/用途与实际gzip树成员；restore后按各原ledger精确pointer/范围阅读。恢复/传输本身不增加语义信用。原私有平台流留本地，公开tool I/O投影另有完整身份，不能声称原私有流已远端读回。'}
    intro='''# 第七轮完整中文云端有限整改交接 Prompt

本合同供用户另行手动启动。交接文件生成和发布时 UPDATE_NOT_STARTED；不得因读取本合同就自动另开update任务。用户把此正文作为后续update会话的启动指令后，在其授权范围持续推进，不另等一次形式启动确认。

目标是修正从零实现所依赖的独立行为规格；不实现引擎、TypeScript包或适配器，不移植Ruby结构，不复制源表达式到正式规格。先完整读项目根和适用AGENTS.md。reference、B、旧报告/接受/关闭回执、交付及归档tag、main、其它worktree和未发布成果只读。不得reset、force push、移动main/tag、补忽略规则掩盖差异、删除工作树或改变系统安全配置。

先解析实际项目/参考绝对路径并保存本机原路径到执行路径映射，逐一核固定commit/workspace/formal/tree/tag、九有效补充和历史恢复身份、dirty/untracked及可能冲突写者。未来云端实际路径当前UNVERIFIED；路径不同不能伪称相同，缺依赖只冻结受影响范围。原5049未跟踪的98+4951既有分类不等于新产物；按身份保护，不清理。源432/formal131/补充9是当前分母，53改78未改、76贡献、3只读mirror、54 prospective paths均不是替代分母。

完整原证据、独立反证、普通对照/最小反例、四路径、最小修正规则、正确保留scope、必要同步/消费者、验收回归和精确读写集见下列全部37条七组合同。27必修恰属13主批；7 optional entries、2额外optional导航facet、1 no-required、2 policy entries，以及原R6的8 optional/1 FLOAT/7 policy/14 limits/1 no-required分母独立。别名和资格facet不新算根因，不把待选择兼容政策强塞mandatory。GR7只登记新审查结论，不重开或改写旧56/92关闭台账。旧proposed/WAIT/OPEN保持生成时点，当前接受/关闭另列。

按每条已接非作者反证缩窄的最低合同修订，不采回作者已被反证的宽范围。强断言逐前提核；定义与接线、请求与实际画面/听感、内存/PBS/导出/存档/重载、正常/取消/异常/部分提交分开。源缺陷的事实与未来是否兼容分开，不能偷偷改成理想行为或永久兼容。静态可判定项可无宿主验收；未执行向量仍是推导。任何新发现保留稳定ID/原提案、完整证据与异议，交不同实际审者反证，再由整合主会话裁决。

13批作者只写独立 candidates/<batch>/<完整目标路径> 的候选镜像及各自证据；不直接改共享正式正文或公共索引。R7-I是唯一实际整合/台账写者。每批由不同实际context的非作者reviewer核完整候选；整合后再交新的非作者R7-IR核实际整合字节。候选PASS、实际整合PASS、正式ACCEPTED、最终CLOSED分开。共享接收、直接/传递依赖、回归未满足保持开放；policy待决只阻塞依赖它的范围。

未来author请求gpt-6.1-sol / xhigh / default普速；reviewer请求gpt-6.1-sol / ultra / default普速，均禁Fast。不得把请求argv当实际模型证明；无明确回显逐项UNVERIFIED，不查额度/认证。保存逻辑入口ID、真实PID/thread/context、prompt SHA、UTC、完整stdout/stderr、退出码、读写集、依赖和状态。现成CLI参数已由本机help核过；26份完整入口与argv/status方法随包提供，实际执行路径启动时绑定，不猜云端目录或服务slots。第一波13个隔离author均无已证作者阻塞入边；这不是13个服务slot或已运行声明。

允许必要本地读取、解析、静态工具、隔离临时检查及已授权的有限观察；执行前读懂程序和依赖、绑定固定输入/受控输出并保存真实日志。不得盲跑下载脚本、安装软件、用生产账户/真实存档/未授权服务或执行未知native。新增安全宿主/素材观察需具名条件满足；材料不足保持相应limit并继续静态可判定项。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立模型、完整宿主/Demo/native媒体/真实保存回放分别计。R7只有本机Ruby数字谓词1过程10输入观察，不证明随附宿主；完整模型/游戏宿主/Demo/native媒体/真实保存回放均0。R6历史18Ruby尝试=12已知0/4非零/2未知，17进入定义/1未加载，含无效/重复替身，不称18成功测试。

R1–R6范围、旧FAIL/修订PASS、实际整合/最终登记/ACCEPTED/CLOSED、R3 optional/U08未启动和NO_REQUIRED、R4 16/75到17/76、R5 SC-U07纠正、R6 U13旧FAIL和新PASS必须按准确输入保留。L01–L14有限已审与未知边界完整保留；已有可读IL/shader/Main49/messages/SF2/字体/BMP及消费者不能因宿主缺失而免读。有限可读单元未读不得改标limit；不要求无界逆向全部机器码。

完成后核每个required最低规则、必要正文/附表/向量/反向消费者、共享实际写文件和历史精确回归，保留正确scope；核prompt/manifest/ID/计数/图/状态一致。update仅在另立授权分支普通提交和推送，禁止改main/tag或force；正式发布与是否合并服从该后续会话的明确授权。核心证据先冻结，再后继发布绑定，逐本次新文件完整远端读回，不能用exit0或hash替代语义验收。
'''
    body=intro+'\n固定输入、本轮真实core与外部发布绑定机制：\n\n```json\n'+pretty({'fixed':fixed,'core':core_id,'publication_binding':manifest['external_publication_binding'],'future_paths':manifest['future_environment']})+'```\n\n'
    body+=core_text('tasks/R7-C13/chinese-handoff.md')
    body+='\n\n## 额外两个可选导航facet（不扩必修）\n\n'+core_text('evidence/root-h22-counter/optional-navigation-facets.zh.md')
    body+='\n\n## 十三批、依赖、共享接收和状态\n\n```json\n'+pretty(plan)+'```\n\n```json\n'+pretty(manifest['dependency_graph'])+'```\n'
    for name in ('historical_qualifications','inherited_nonmandatory','limits','execution'):
        if name in sections:body+='\n\n## '+name+' 完整当前用途记录\n\n```json\n'+pretty(sections[name])+'```\n'
    out.mkdir(parents=True)
    # Full objects remain present; whitespace-only compaction keeps the large
    # manifest inside ordinary Git's single-file limit without dropping fields.
    files={'cloud-seventh-update-handoff-prompt.md':body,'cloud-seventh-update-handoff-manifest.json':json.dumps(manifest,ensure_ascii=False,separators=(',',':'))+'\n',
           'batch-assignment.json':pretty(plan),'dependency-graph.json':pretty(manifest['dependency_graph']),
           'file-conflict-graph.json':pretty(manifest['file_conflict_graph'])}
    prompt_prefix='tasks/R7-P03/plan-candidate/prompts/'
    prompt_paths=sorted(p for p in logical if p.startswith(prompt_prefix) and p.endswith('.md'))
    if len(prompt_paths)!=26:raise ValueError('26 exact frozen manual entries required')
    for p in prompt_paths:
        files['prompts/'+Path(p).name]='# 用户手动委派入口；UPDATE_NOT_STARTED\n\n'+intro+'\n实际R7 core：\n```json\n'+pretty(core_id)+'```\n\n'+core_text(p)
    inv=core_json('tasks/R7-P03/plan-candidate/cli-invocations.candidate.json')
    for row in inv:
        row['status']='NOT_STARTED';row['path_binding']='Actual local argv only; future cloud startup must resolve and record actual absolute project/package paths before launch.'
        row['stdin_prompt_path']=str(out/'prompts'/(row['entry_id'][:-2]+'-'+row['role']+'.md'))
    files['cli-invocations.json']=pretty(inv)
    for name,text in files.items():
        data=text.encode()
        if len(data)>=95_000_000:raise ValueError('ordinary GitHub member too large: '+name)
        p=out/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
    output_index={'schema':'r7.handoff-package-members.v1','core':core_id,'update_started':False,
                  'members':[{'path':name,**ident(text.encode())} for name,text in files.items()],
                  'qualification':'Self index identity is bound by external C2; it cannot contain its own publication commit/hash.'}
    (out/'package-members.json').write_text(pretty(output_index))
    print(pretty({'status':'MANUAL_HANDOFF_RENDERED_NOT_STARTED','files':len(files)+1,
                  'required':27,'batches':13,'core':core_id,'largest_member':max((len(v.encode()),k) for k,v in files.items())}))
if __name__=='__main__':main()
