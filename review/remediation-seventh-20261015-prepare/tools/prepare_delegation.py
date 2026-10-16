"""Make bounded R7 dispatch inputs from the once-indexed local handoff cache.

This is preparation/transport tooling, never a source semantics or review PASS.
"""
from pathlib import Path
import collections
import gzip
import hashlib
import itertools
import json

PROJECT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parents[1]
REVIEW = 'review/global-independent-review/seventh-2026-10-14-e646432-7a91'
ROOT = PROJECT / REVIEW
CACHE = Path('/workspace/r7-input-cache')
EVIDENCE = Path('/workspace/r7-evidence')
C2 = '4580645dfbfec4a3c7ccbad56ae293cc619b0d25'
B = 'e646432c644dec04d306842cc5a559a29c718fbc'


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write('\n')


def ident(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}


def clean(value):
    """Drop only mechanical provenance duplicates from the short reading surface."""
    if isinstance(value, dict):
        return {k: clean(v) for k, v in value.items() if not any(word in k for word in ['原裁决字段定位', '原始证据', '全部原验收向量证据', 'original_scope_ref'])}
    if isinstance(value, list):
        return [clean(v) for v in value]
    return value


def main():
    index_bytes = (ROOT / 'publication-transport/core/payload-index.json').read_bytes()
    expected_index = json.loads((CACHE / 'core_transport_index.json').read_bytes())
    assert all(ident(index_bytes)[k] == expected_index[k] for k in ident(index_bytes))
    index = json.loads(index_bytes)
    logical = {r['logical_path']: r for r in index['logical_files']}
    compressed = {r['sha256']: r for r in index['compressed_objects']}
    selected = [r for p, r in logical.items() if p.startswith('tasks/R7-C13/')]
    selected += [logical['tasks/R7-C17/limits-and-alias-reception.json']]
    EVIDENCE.mkdir(exist_ok=False)
    restored = []
    for row in selected:
        source = ROOT / 'publication-transport/core' / row['transport_path']
        encoded = ident(source.read_bytes())
        assert all(encoded[k] == compressed[row['sha256']]['transport_' + k] for k in encoded)
        target = EVIDENCE / row['logical_path']
        target.parent.mkdir(parents=True, exist_ok=True)
        sha = hashlib.sha256()
        blob = hashlib.sha1(f"blob {row['bytes']}\0".encode())
        count = 0
        with gzip.open(source, 'rb') as inp, target.open('xb') as out:
            for data in iter(lambda: inp.read(1024 * 1024), b''):
                out.write(data)
                sha.update(data)
                blob.update(data)
                count += len(data)
        actual = {'bytes': count, 'sha256': sha.hexdigest(), 'git_blob_content_id': blob.hexdigest()}
        assert all(actual[k] == row[k] for k in actual), row['logical_path']
        restored.append({'logical_path': row['logical_path'], 'transport_path': row['transport_path'], **actual})
    dump(OUT / 'startup/evidence-recovery.json', {
        'qualification': 'FULL_BYTE_TRANSPORT_CHECK_ONLY; no new semantic or execution credit',
        'core_commit': '28e0d9df6ca4f75de9773a502ebdaa177cc0752c', 'publication_C2': C2,
        'destination': str(EVIDENCE), 'restored_count': len(restored),
        'restored_bytes': sum(r['bytes'] for r in restored), 'files': restored,
    })
    assignment = json.loads((CACHE / 'batch_assignment.json').read_bytes())
    deps = json.loads((CACHE / 'dependency_graph.json').read_bytes())
    conflict = json.loads((CACHE / 'file_conflict_graph.json').read_bytes())
    assert len(assignment['batches']) == 13 and len(assignment['primary_batch_by_required']) == 27
    assert deps['blocking_author_edges'] == [] and conflict['author_candidate_write_write_conflicts'] == []
    all_targets = collections.defaultdict(set)
    required_targets = collections.defaultdict(set)
    for batch in assignment['batches']:
        for path in batch['candidate_paths']:
            all_targets[path['actual_path']].add(batch['id'])
            if any(c['kind'] == 'required' for c in path['contributions']):
                required_targets[path['actual_path']].add(batch['id'])
    all_pairs = {p for ids in all_targets.values() for p in itertools.combinations(sorted(ids), 2)}
    required_pairs = {p for ids in required_targets.values() for p in itertools.combinations(sorted(ids), 2)}
    groups = []
    for path, ids in sorted(all_targets.items()):
        if len(ids) > 1:
            groups.append({'id': f'CG{len(groups)+1:02}', 'path': path, 'batches_including_conditional': sorted(ids), 'required_batches': sorted(required_targets[path]), 'writer': 'R7-I', 'gate': 'serial clause-level integration, preserve earlier accepted contribution, fresh integrated non-author R7-IR review'})
    dump(OUT / 'delegation/conflict-groups.json', {'original_C2_graph': REVIEW + '/handoff/file-conflict-graph.json', 'original_conflict_entries_including_reads': len(conflict['conflicts']), 'all_target_pairs': len(all_pairs), 'mandatory_target_pairs': len(required_pairs), 'groups': groups, 'optional_adoption': 'NOT_ADOPTED; conditional same-record synchronization requires concrete justification; no optional finding/policy/facet promoted'})
    rows = []
    instructions = '''本轮只修独立行为规格，不实现框架、不复制参考代码。先读项目 AGENTS.md。所有工作在本云端；旧 Mac 路径仅为来源身份。固定 B={B}，C2={C2}，R=8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。项目 /workspace/pokemon-essentials-clean-room，参考 /workspace/r7-reference（只读）。
本批是 {id}，必修 {ids}。作者请求 gpt-6.1-sol / xhigh / service_tier=default 普通速度；独立 reviewer 请求 gpt-6.1-sol / ultra / default 普通速度；禁 Fast。请求与真实配置回参分开，不能自行认证，缺有效回参保留 UNVERIFIED。
所有作者阻塞入边为0，仅表示可独立准备；公共目标存在冲突。唯一整合者 R7-I；不改共享正式路径、公共台账、main、tag、旧证据和 reference，不提交、不推送、不再派生任务。作者只写 candidates/{id}/ 下完整目标路径镜像与 evidence/author/。reviewer 只写 candidates/{id}/evidence/reviewer/，不修作者文件。可保存补丁，但最终交 R7-I 按 clause 整合，不能以整文件覆盖其它批次结果。
本批精简合同 delegation/contracts/{id}.json（相对于 review/remediation-seventh-20261015-prepare）包含原七组及完整原引用；原合同 C2:{review}/handoff/prompts/{id}-author.md / reviewer.md。C13 逻辑证据已按原 bytes/SHA/blob 恢复到 /workspace/r7-evidence/tasks/R7-C13/；源证据链、原反证和完整向量仍须按本批 pointer/范围阅读。不要每批重扫80MB Manifest。需要额外逻辑成员时读固定 core payload-index 的精确 logical_path 并核 gzip 解码身份，或交 R7-I 定向恢复。哈希与退出0均不是语义 PASS。
L01-L14 保留，完整当前用途记录 /workspace/r7-evidence/tasks/R7-C17/limits-and-alias-reception.json。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立完整模型、宿主/Demo/native媒体/真实存档回放分别计。本轮准备新增运行观察0。未执行向量保持 NOT_EXECUTED。7 optional、2导航facet、1 no-required、2 policy 不采用，不改变旧56/92关闭。条件同步路径仅为同一必修消除具体矛盾时才可提出，并说明依据；不得顺手扩成可选改进。
'''
    for batch in assignment['batches']:
        bid = batch['id']
        paths = []
        for path in batch['candidate_paths']:
            paths.append({'path': path['actual_path'], 'candidate_path': path['candidate_path'], 'classification': 'required' if any(c['kind'] == 'required' for c in path['contributions']) else 'conditional_same_record_not_automatic', 'scopes': path['contributions']})
        batch_groups = [g['id'] for g in groups if bid in g['batches_including_conditional']]
        contract = {'schema': 'r7.cloud-bounded-batch-contract.v1', 'publication_C2': C2, 'original_batch_pointer': '/batch_assignment/batches/' + str(len(rows)), 'batch_id': bid, 'required_ids': batch['required_ids'], 'blocking_author_dependencies': batch['blocking_author_dependencies'], 'reception_conditions': batch['nonblocking_reception_conditions'], 'paths': paths, 'conflict_groups': batch_groups, 'original_full_contracts': batch['contracts']}
        dump(OUT / f'delegation/contracts/{bid}.json', contract)
        common = instructions.format(B=B, C2=C2, id=bid, ids=', '.join(batch['required_ids']), review=REVIEW)
        summary = '\n精确写入路径（全部加 candidates/' + bid + '/ 前缀；required 与 conditional 分开）：\n' + '\n'.join(f"- {p['classification']}: {p['path']}" for p in paths)
        summary += '\n冲突组：' + ', '.join(batch_groups) + '。无作者前置批次；接收门：' + ' | '.join(batch['nonblocking_reception_conditions']) + '\n'
        for original in batch['contracts']:
            g = original['complete_seven_groups']
            summary += '\n' + original['record_id'] + '\n'
            for group in ['二_证据_前提_反例_四路径', '三_最小修订_正确保留', '四_验收与回归']:
                summary += json.dumps(clean(g[group]), ensure_ascii=False, indent=2) + '\n'
        for role in ['author', 'reviewer']:
            if role == 'author':
                task = '\n角色：作者。完整读取本批七组和被接收的独立反证；用固定 B 字节建立镜像，按最小规则修正文/必要目录/向量，保留正确scope。提交 evidence/author/report.md、per-id.json、artifact-manifest.json（逐镜像固定B身份、新bytes/SHA/blob、读写集、精确变更、每向量阶段、失败/取消/部分提交、未满足依赖和配置UNVERIFIED）。不得宣称独立PASS、ACCEPTED或CLOSED。完成后停止写入，回报全部产物路径供 R7-I 固定快照。\n'
            else:
                task = '\n角色：独立非作者 reviewer。此 prompt 现在只发布，不立即启动。须先由 R7-I 提供冻结的 candidate-input.json，含作者真实context、候选提交/树或逐文件bytes/SHA/blob、作者证据与完整差异；缺少则报告明确依赖，不自行猜HEAD。必须是与作者不同的实际context。逐必修核完整合同、原非作者反证、固定R的源/消费者、候选正文/目录/向量、正确保留和共享贡献；对正常/取消/异常/部分提交及必要历史回归出逐ID PASS/FAIL/WAIT。写 evidence/reviewer/report.md 与 per-id.json，绑定实际输入和真实context/配置回参。候选PASS只进入待整合，不等于整合PASS、ACCEPTED或CLOSED。不以作者报告或自审代替独立内容审查。\n'
            target = OUT / f'delegation/prompts/{bid}-{role}.md'
            target.write_text(common + summary + task)
        rows.append({'id': bid, 'title': batch['title'], 'required_ids': batch['required_ids'], 'author_entry': bid+'-A', 'reviewer_entry': bid+'-R', 'blocking_author_dependencies': [], 'reception_conditions': batch['nonblocking_reception_conditions'], 'paths': [{'path': p['path'], 'candidate_path': p['candidate_path'], 'classification': p['classification']} for p in paths], 'conflict_groups': batch_groups, 'author_prompt': f'delegation/prompts/{bid}-author.md', 'reviewer_prompt': f'delegation/prompts/{bid}-reviewer.md', 'contract': f'delegation/contracts/{bid}.json', 'candidate_pass': False, 'integrated_pass': False, 'accepted': False, 'closed': False, 'actual_author_task': None, 'actual_reviewer_task': None})
    dump(OUT / 'delegation/batches.json', {'schema': 'r7.cloud-compact-dispatch.v1', 'fixed_B': B, 'C2': C2, 'required_denominator': 27, 'batch_denominator': 13, 'first_wave_author_eligible': [r['id'] for r in rows], 'slots_claimed': False, 'reviewers_eligible': [], 'sole_integrator': 'R7-I', 'fresh_integrated_reviewer': 'R7-IR', 'batches': rows})
    dump(OUT / 'delegation/artifact-identities.json', [{'path': str(p.relative_to(OUT)), **ident(p.read_bytes())} for p in sorted((OUT/'delegation').rglob('*')) if p.is_file()])
    print(json.dumps({'batches': len(rows), 'required': 27, 'recovered_files': len(restored), 'all_target_pairs': len(all_pairs), 'mandatory_target_pairs': len(required_pairs), 'conflict_groups': len(groups), 'compact_prompt_bytes': sum(p.stat().st_size for p in (OUT/'delegation/prompts').glob('*.md'))}))


if __name__ == '__main__':
    main()
