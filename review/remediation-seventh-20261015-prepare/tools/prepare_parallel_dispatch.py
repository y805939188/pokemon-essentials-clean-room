"""Freeze bounded parent-launched R7 author/reviewer dispatch; starts no tasks."""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'delegation/parallel-dispatch'
PREFIX = 'review/remediation-seventh-20261015-prepare'
REPOSITORY = 'y805939188/pokemon-essentials-clean-room'
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
PREPARATION = '4bd152023b4bcb3dd5a3654deffe75aeebc40f10'
CONTRACT = 'f622356f3beb9e84ea8cff9db07c7fb382565d3f'
RECOVERY = '658488c81f1f3181a488298ab27850c8af951d73'


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x') as stream:
        stream.write(text)


def dump(path, value):
    write(path, json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def common(bid, role):
    effort = 'xhigh' if role == 'author' else 'ultra'
    return f'''# {bid} 独立云端{role}派发

只执行本次具名角色，不创建子任务或其它作者/reviewer。父会话唯一负责 cloud_threads.create；无用户设置的并发数量上限，但不要把可并行当成已创建或服务slots证明。父会话已报告U01=01a13f52-add1-7706-b7ec-54e07e0d7013、U04=01a13f52-cc74-7568-9e75-85ac773c6015、U05=01a13f52-ecf8-73f9-8c9b-f5c164f0c017为inProgress，不重复创建它们。其它批次以父会话真实task登记去重；本静态派发文本不是创建回执。

本角色请求 gpt-6.1-sol / {effort} / service_tier=default 普通速度，禁Fast。模型/档位/速度的实际有效回参缺失时逐项UNVERIFIED，不以请求argv、自报或成功退出认证配置，不查额度/认证。实际task/context/PID、请求、UTC、完整可发布工具I/O和退出分开留存；私有模型流不作为公共证据推送。

仓库 https://github.com/{REPOSITORY}.git 。输入远端分支 `codex/remediation-seventh-20261015-cloud`；固定准备提交 `{PREPARATION}`。行为基线B `{B}`，正式tree ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c。参考固定R为 Maruno17/pokemon-essentials 的8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/tree7589c800b61ba13a13040ed0d686979b80a84fd0。只在云端工作，不操作用户Mac，不用浮动HEAD替代固定输入。先读实际项目AGENTS.md。

原完整七组合同：提交 `{CONTRACT}` 的 `{PREFIX}/delegation/contracts/{bid}.json`。
原角色入口：同提交 `{PREFIX}/delegation/prompts/{bid}-{role}.md`。
固定恢复工具：提交 `{RECOVERY}` 的 `{PREFIX}/tools/restore_container_context.py`。
逐批证据恢复清单：同提交 `{PREFIX}/recovery/batches/{bid}.json`。
跨容器说明：同提交 `{PREFIX}/recovery/independent-containers.md`。
上述固定文件可由 `https://raw.githubusercontent.com/{REPOSITORY}/<完整固定commit>/<精确路径>` 读取，不必下载80MB Manifest或扫描完整core包。先完整阅读工具和本批清单再执行；不盲跑下载程序、不执行恢复出的参考/native程序。

独立容器不共享整合者本地目录。将工具和本批清单分别保存为 `/workspace/r7-bootstrap/{bid}-{role}/tools/restore_container_context.py` 与 `/workspace/r7-bootstrap/{bid}-{role}/recovery/batches/{bid}.json`，运行：

```bash
python3 /workspace/r7-bootstrap/{bid}-{role}/tools/restore_container_context.py --plan-directory /workspace/r7-bootstrap/{bid}-{role}/recovery/batches --batch {bid} --destination /workspace/r7-context/{bid}-{role}
```

工具定向恢复本批原载荷、身份/原绑定及L01-L14、固定源/正式读输入和冻结合同/Prompt。原 `/workspace/r7-evidence` 映射到 `/workspace/r7-context/{bid}-{role}/evidence`；原 `/workspace/r7-reference` 映射到 `.../inputs/reference`；固定正文在 `.../inputs/project/`，原入口在 `.../dispatch/delegation/`。这些只是有界文件快照，不是完整Git checkout或运行认证。已有匹配恢复可复用；连接中断保留目录、同环境同目录加--resume，不覆盖冲突字节、不另起替代任务。有新的具体可读依赖应具名定向补取，不能伪标limit。

规格只描述可供从零重写的独立功能、逻辑、行为，不实现引擎/TypeScript包/适配器，不移植Ruby结构或复制源表达式。完整前提、普通对照、取消/异常/部分提交、最小规则、正确保留scope、消费者和历史回归按原七组及已接非作者反证审读，不复活已被反证排除的宽提案。7 optional、2额外导航facet、1 no-required、2 policy均未采用；同一必修的条件同步须给具体矛盾和依据，不自动扩大。

L01-L14和旧56/92关闭边界保持。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立完整模型、游戏宿主/Demo/native媒体/真实存档回放分开。未执行向量保持NOT_EXECUTED，身份/退出0不替代语义验收。有效配置UNVERIFIED，宿主等0不得提升。进度分母固定27项/13批；只有R7-I写正式正文、公共台账和整合分支，不改main/tag/旧证据、不force、不提前关闭依赖问题。

'''


def author(row):
    bid = row['id']
    branch = f"codex/r7-u{bid[-2:]}-author-20261015-wave1"
    text = common(bid, 'author')
    text += '本批必修：' + '、'.join(row['required_ids']) + '。作者前置批次：无；所有作者仅写各自镜像，可同时准备，不能因此同时覆盖共享正式文件。\n\n'
    contract = json.loads((ROOT/row['contract']).read_bytes())
    for item in contract['original_full_contracts']:
        groups = item['complete_seven_groups']
        text += '## ' + item['record_id'] + '\n\n'
        for key in ['三_最小修订_正确保留', '四_验收与回归']:
            value = {k: v for k, v in groups[key].items() if k not in ['原裁决字段定位', '全部原验收向量证据']}
            text += json.dumps(value, ensure_ascii=False, indent=2) + '\n\n'
    text += '精确允许写集仅为下列完整候选镜像及本批 `evidence/author/`：\n\n'
    for path in row['paths']:
        text += f"- {path['classification']}: `{path['candidate_path']}`\n"
    text += f'''
冲突组：{', '.join(row['conflict_groups']) or '无共享正式目标组'}。父会话/R7-I使用固定 `{CONTRACT}` 的 `{PREFIX}/delegation/conflict-groups.json` 中各实际路径和当前完整合同判定共享接收，候选隔离不等于正式合入无冲突。

在自己的独立容器/checkout从固定B `{B}` 创建唯一成果分支 `{branch}`。如存在同名分支、未发布成果或父会话已登记本批实际task，先核HEAD/status/远端并保护原成果，不覆盖、不reset、不force、不自换替代分支；若共享整合者工作树，不切换其分支，回报父会话取得隔离工作树。

本派发按本轮普通提交/推送授权和父会话要求，**仅覆盖旧精简入口“不提交/不推送”的成果传输限制**：可普通提交本批candidates镜像及证据，只普通push至 `{branch}`。与B的差异必须全部位于 `candidates/{bid}/`；不夹带bootstrap、恢复输入、其它批次、正式文件或公共台账。不得推送整合分支或main，不合并main、不移动tag。原行为合同和验收范围未改变。

以固定B原字节建立完整镜像，定点修订最低规则。交 `candidates/{bid}/evidence/author/report.md`、`per-id.json`、`artifact-manifest.json`：逐文件原B/新bytes/SHA/blob、精确scope/读写集、全部必要向量的阶段/结果、失败/取消/部分提交、未满足依赖、真实task/context、请求与实际配置资格、命令I/O和退出。新文件必须进入候选提交，不只回报容器绝对路径。

返回真实候选commit/tree、唯一分支、普通push和逐新文件完整远端读回证据；完成后冻结停止写入。只报告 CANDIDATE_READY_NOT_REVIEWED，不自称独立PASS、ACCEPTED或CLOSED。R7-I核完整差异/身份后生成candidate-input.json，再由不同实际context的ultra reviewer审候选；之后R7-I逐条整合，再由新的R7-IR审实际整合字节。候选PASS、整合PASS、ACCEPTED、CLOSED分开，共享接收和直接/传递依赖/历史回归未满足保持OPEN。
'''
    return branch, text


def reviewer(row):
    bid = row['id']
    branch = f"codex/r7-u{bid[-2:]}-reviewer-20261015-r1"
    freeze_path = f'{PREFIX}/candidate-freezes/{bid}/candidate-input.json'
    text = common(bid, 'reviewer')
    text += f'''本批必修：{'、'.join(row['required_ids'])}。这是完整的候选冻结后reviewer入口，**现在不是可启动回执**。父会话仅在R7-I已经完成真实候选接收/冻结后才创建本独立任务。

启动必须由R7-I另外提供：实际冻结commit/tree，以及该commit下精确路径 `{freeze_path}`。不得用当前HEAD、浮动作者分支或作者口头PASS猜输入。缺冻结绑定、完整候选/作者证据、作者真实task身份或可确认不同的实际reviewer context，则WAIT_INPUT_OR_INDEPENDENCE，不开始语义PASS，不启动另一个reviewer。

candidate-input.json须绑定本批及必修ID、固定B、原合同commit/path、作者实际task/context资格、唯一作者分支、候选实际commit/tree、候选对B完整差异、每个候选文件和作者证据的bytes/SHA256/blob、条件同步依据、接收完整性、真实命令及未满足依赖；冻结字节不得后来被浮动branch替换。完整门见 `{PREFIX}/delegation/parallel-dispatch/candidate-freeze-requirements.json`（以父会话提供的本派发固定commit为准）。

你必须与本批作者为不同实际context，不派生子任务、不担任自己的作者或自己的R7-IR。task ID/PID和有效模型回参分开；无配置回显保留UNVERIFIED。收到真实冻结后先按精确文件身份读回作者候选和完整证据，保存为新的只读 `/workspace/r7-review-input/{bid}/`；不要checkout作者分支、改作者文件或执行作者/参考未知程序。固定证据恢复工具不包含候选，也不能替代候选接收。

逐必修完整审查原七组、已接非作者反证、固定R的源/消费者、B与候选正文/目录/向量、全部正确保留scope、必要历史回归和反向消费者。检查正常/取消/异常/部分提交、源缺陷事实与未来政策分层；分别核所有强断言的前提。核作者对B的完整差异仅在本批candidates/，并只修改原批准实际目标的镜像/证据。条件同步不得借机采纳optional/policy。

特别核共享冲突组 {', '.join(row['conflict_groups']) or '无'} 的本批贡献能否与其它贡献按条款接收；这里只给候选结论，不声称其它批次依赖或实际合入已经完成。逐ID给 PASS_SCOPED_CANDIDATE / FAIL_SCOPED_CANDIDATE / WAIT_INPUT_OR_INDEPENDENCE，并引用实际候选字节和完整反例/回归范围；传输哈希、作者自审、退出0、旧全局PASS均不能代替本次独立内容审查。未执行向量不写成运行成功。

只写 `candidates/{bid}/evidence/reviewer/r1/` 下 report.md、per-id.json、review-input-receipt.json、artifact-manifest.json 及本次真实工具证据，不修候选，不写正式/公共文件。独立成果运输按本轮普通提交/推送授权限于唯一分支 `{branch}`：在自己的干净隔离checkout从固定B `{B}` 建分支，普通提交/推送上述reviewer证据；不携带或改写作者镜像，不推作者/整合/main分支，不force。若同名分支非本task所有，保护原成果并回报，不另换分支。若父会话用平台导出传回同样须包含全部新文件和完整身份，不能仅给本地绝对路径。

返回真实审者task/context、审查输入冻结commit和候选commit/tree、逐ID结论、未满足依赖、结果commit/tree/分支及普通push/远端完整读回证据。候选PASS仅供R7-I整合；你无权登记实际整合PASS、ACCEPTED或CLOSED。实际合入后必须新建独立R7-IR审真实整合字节，依赖和回归满足后才关闭。
'''
    return branch, freeze_path, text


def main():
    batches = json.loads((ROOT/'delegation/batches.json').read_bytes())['batches']
    launches = json.loads((OUT/'parent-launch-receipt.json').read_bytes())
    active = {row['batch_id']: row for row in launches['entries']}
    all_author = []
    all_reviewer = []
    for row in batches:
        bid = row['id']
        if bid in active:
            all_author.append({'batch_id': bid, 'status': 'IN_PROGRESS_PARENT_REPORTED_DO_NOT_REDISPATCH', 'task_id': active[bid]['author_task_id'], 'prompt_commit': PREPARATION, 'prompt_path': f'{PREFIX}/delegation/pilot-dispatch/{bid}-author.md', 'output_branch': f"codex/r7-u{bid[-2:]}-author-20261015-pilot1", 'required_ids': row['required_ids'], 'conflict_groups': row['conflict_groups']})
        else:
            branch, text = author(row)
            path = OUT/'authors'/f'{bid}-author.md'
            write(path, text)
            all_author.append({'batch_id': bid, 'status': 'READY_PARENT_CREATE_ONLY_NOT_LAUNCHED', 'task_id': None, 'prompt_path': str(path.relative_to(ROOT.parents[1])), 'output_branch': branch, 'base_commit': B, 'required_ids': row['required_ids'], 'blocking_author_dependencies': [], 'conflict_groups': row['conflict_groups']})
        branch, freeze_path, text = reviewer(row)
        path = OUT/'reviewers'/f'{bid}-reviewer.md'
        write(path, text)
        all_reviewer.append({'batch_id': bid, 'status': 'BLOCKED_ON_ACTUAL_CANDIDATE_FREEZE_NOT_LAUNCHED', 'task_id': None, 'prompt_path': str(path.relative_to(ROOT.parents[1])), 'required_candidate_freeze_path': freeze_path, 'required_freeze_commit': None, 'output_branch': branch, 'requested_effort': 'ultra', 'author_task_id': active[bid]['author_task_id'] if bid in active else None})
    graph = json.loads((ROOT/'delegation/conflict-groups.json').read_bytes())
    groups = graph['groups']
    rows = []
    for row in batches:
        related = sorted({peer for group in groups if row['id'] in group['batches_including_conditional'] for peer in group['batches_including_conditional'] if peer != row['id']})
        rows.append({'batch_id': row['id'], 'author_mirror_write_conflict': False, 'author_blocking_dependencies': [], 'formal_target_conflict_peers_including_conditional': related, 'conflict_groups': row['conflict_groups']})
    dump(OUT/'conflict-relations.json', {'schema': 'r7.parallel-author-versus-integration-conflicts.v1', 'author_parallelism': 'All13 isolated mirrors have0 author-blocking edges and0 candidate write/write conflicts;3 already active,10ready. No user cap; actual service capacity not asserted.', 'integrator': 'R7-I only', 'unique_formal_batch_pairs': 19, 'file_specific_pair_occurrences': 39, 'conflict_groups': groups, 'batches': rows, 'conditional_and_optional_qualification': 'Includes conditional same-record paths; no optional finding/policy/facet adopted. Whole-file replacement and simultaneous conflicting formal integration forbidden.'})
    dump(OUT/'candidate-freeze-requirements.json', {
        'schema': 'r7.candidate-freeze-gates.v1', 'status': 'NO_CANDIDATE_FROZEN_YET', 'required_denominators': {'issues': 27, 'batches': 13},
        'sole_freezer': 'R7-I', 'immutable_receipt_path_template': PREFIX+'/candidate-freezes/<R7-Uxx>/candidate-input.json',
        'required_fields': ['batch_id', 'required_ids', 'fixed_B', 'original_contract_commit_path_identity', 'author_task_id', 'author_context_and_qualification', 'author_output_branch', 'candidate_commit', 'candidate_tree', 'complete_diff_against_B', 'candidate_and_author_evidence_file_identities', 'conditional_sync_justifications', 'input_reception_complete', 'unmet_dependencies', 'freeze_utc', 'requested_and_effective_configuration_qualification'],
        'file_identity_fields': ['path', 'bytes', 'sha256', 'git_blob', 'base_B_identity_or_explicit_new_file'],
        'freezer_checks': ['Obtain real task completion/result commit from parent; creation/inProgress is not completion.', 'Fetch/read exact author result without whole-branch merge; verify commit/tree, complete changed/untracked/new-file set and all bytes.', 'Diff from fixed B stays within the assigned candidates/<batch>/ and exact approved target mirrors/evidence.', 'Preserve original rules, conditional boundaries, all authored evidence and task/configuration/phase qualifications.', 'Publish immutable candidate-input receipt and provide its actual commit/tree plus complete candidate contents to a different-context reviewer.'],
        'reviewer_launch_gates': ['R7-I freeze complete and exact commit supplied', 'Author has stopped writing; later repairs receive new versioned freeze', 'Different actual reviewer context; gpt-6.1-sol ultra/default normal speed requested', 'Full candidate and original evidence received; no floating HEAD or author self-review substitution'],
        'after_candidate_PASS': ['R7-I integrates clauses serially and preserves all already received contributions', 'Publish actual integrated commit/tree and shared-file/dependency/regression reception ledger', 'New independent R7-IR reviews actual cumulative integrated bytes', 'R7-I formally ACCEPTS scoped passing contracts', 'CLOSE only when exact shared reception and direct/transitive dependencies and regressions meet original contract; unresolved policy blocks only affected scope'],
        'current_candidate_reviewers_eligible': [], 'current_actual_integrated_reviewers_eligible': [], 'no_auto_close': True,
    })
    dump(OUT/'dispatch-index.json', {'schema': 'r7.full-parallel-parent-dispatch.v1', 'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'creator': 'PARENT cloud_threads.create only', 'created_by_integrator': 0, 'user_task_concurrency_cap': None, 'capacity_or_model_echo_verified': False, 'fixed_preparation_commit': PREPARATION, 'original_contract_commit': CONTRACT, 'recovery_commit': RECOVERY, 'registered_author_count': 3, 'ready_new_author_count': 10, 'prepared_reviewer_count': 13, 'reviewers_currently_eligible': [], 'author_entries': all_author, 'reviewer_entries': all_reviewer, 'progress_denominators': {'required': 27, 'batches': 13}, 'candidate_pass': 0, 'integrated_pass': 0, 'accepted': 0, 'closed': 0})
    files = [p for p in sorted(OUT.rglob('*')) if p.is_file() and p.name != 'artifact-identities.json']
    dump(OUT/'artifact-identities.json', [{'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'git_blob': hashlib.sha1(f'blob {p.stat().st_size}\0'.encode()+p.read_bytes()).hexdigest()} for p in files])
    print(json.dumps({'new_author_inputs': 10, 'registered_in_progress': 3, 'prepared_reviewer_inputs': 13, 'reviewers_eligible': 0, 'tasks_created_here': 0}))


if __name__ == '__main__':
    main()
