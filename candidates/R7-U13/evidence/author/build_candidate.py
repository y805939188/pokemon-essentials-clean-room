"""Build only the four authorized complete mirrors from fixed B bytes."""
import datetime
import difflib
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / 'candidates/R7-U13'
EVIDENCE = OUT / 'evidence/author'
CONTEXT = Path('/workspace/r7-context/R7-U13-author')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'

def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}

def save_json(name, value):
    (EVIDENCE/name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

contract = json.loads((CONTEXT/'dispatch/delegation/contracts/R7-U13.json').read_text())
assert subprocess.check_output(['git','rev-parse','HEAD'], cwd=ROOT, text=True).strip() == B
assert subprocess.check_output(['git','branch','--show-current'], cwd=ROOT, text=True).strip() == 'codex/r7-u13-author-20261015-wave1'
rows = []
diffs = []
for item in contract['paths']:
    path = item['path']
    old = subprocess.check_output(['git','show',B+':'+path], cwd=ROOT)
    assert old == (CONTEXT/'inputs/project'/path).read_bytes()
    text = old.decode('utf-8')
    if path.endswith('/wp15-resource-matching-and-audio.md'):
        anchor = '- **未验证组合**：'
        assert text.count(anchor) == 1
        note = '- **MIDI 的独立声明输入（仅静态）**：固定参考配置为 MIDI 播放声明独立音色库输入，随附资源身份为 `soundfont.sf2`。轨道查找与该声明分开；声明不认证原生实际选择、读取、载入或格式接受，也不认证合成与发声。缺库/坏库、字段缺省/无效、guard 与后端失败结果仍未知（L04/L09）；原 SF2 全结构、独立复算与配置审查证据保留，本项不重审其算法。此静态事实不选择未来 SF2、FluidSynth、宿主 API 或旧兼容配置，也不扩成所有未提取宿主设置的必修缺口。\n'
        text = text.replace(anchor,note+anchor)
        anchor = '- 内容身份（符号 ID 与形态查询回退）；'
        dependency = '- MIDI 播放的独立音色库声明输入见 §7；轨道存在、逻辑登记与请求交付均不证明该输入已被原生消费、接受或发声（L04/L09）。\n'
        assert text.count(anchor) == 1
        text = text.replace(anchor,dependency+anchor)
        scope = ['§7：增加一个静态声明/资格条目','§10：增加依赖交叉引用；§11未改']
    elif path.endswith('/engine-overworld-wp11-15-59-60.md'):
        anchor = '\n本目录所有行为与静态向量的执行状态统一为 **NOT_EXECUTED**；新增逐行状态不提升历史案例的证据等级。'
        addition = '\nGR7-D07-001 独立静态声明向量（不改 B04-R17 的查找语义；普通请求、取消、失败与部分提交仍沿原合同）：\n\n| ID | 输入／前提 | 静态预期与观察边界 | 执行状态 |\n| --- | --- | --- | --- |\n| GR7-D07-001-S01 | 固定参考随附配置；普通对照为可查到的 theme.mid、记录音量80/音调100、选项100、正常系统且无默认覆盖；另在纸面夹具中只把声明库身份改为 absent-bank.sf2 | 记录 MIDI 播放的独立音色库输入，随附身份 `soundfont.sf2`。纸面改变只区分声明输入关系，同轨道/参数的查找与游戏层80/100请求不变；原生实际选择、读取、载入、接受、guard、合成及声音仍未知（L04/L09），不推缺库必败/静音或加载成功。nil/空名不推库初始化/释放/取消；BGM有限重试不成为SF2错误处理。普通WAV请求不能抵消此声明；不选择未来格式/后端/API或旧兼容配置。 | DERIVED_VECTOR / NOT_EXECUTED |\n'
        assert text.count(anchor) == 1
        text = text.replace(anchor,'\n'+addition+anchor)
        scope = ['B04-R01–28后追加一个独立静态声明向量；历史标题、行、顺序、状态均未改']
    elif path == 'planning/feature-matrix.md':
        lines = text.splitlines(keepends=True)
        ix = next(i for i,line in enumerate(lines) if line.startswith('| F05-02 |'))
        fields = lines[ix].rstrip('\n').split('|')
        assert len(fields) == 11
        fields[7] = fields[7].rstrip() + '＋Pending（GR7-D07-001：MIDI 独立音色库静态声明候选，待非作者核验及 R7-I 接收） '
        fields[9] = fields[9].rstrip() + '；声明的随附身份为 `soundfont.sf2`，不认证 L04/L09 原生选择、接受、合成或声音 '
        lines[ix] = '|'.join(fields) + '\n'
        text = ''.join(lines)
        scope = ['仅F05-02状态/备注加待审声明；F05-01和历史批准原字节保留']
    elif path == 'audit/source-traceability.md':
        start = text.index('### T-WP15-01 ')
        end = text.index('\n### T-WP59-01 ', start)
        section = text[start:end]
        anchor = '| 证据层级 |'
        assert section.count(anchor) == 1
        note = '| 第七轮定点来源（GR7-D07-001，仅静态） | 固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`：`reference/pokemon-essentials/mkxp.json:64–66` 声明 MIDI 独立音色库输入及随附身份 `soundfont.sf2`；本候选定点重读消费者：`Data/Scripts/001_Technical/002_Files/001_FileTests.rb:109–115, 181–236, 262–273`、`Data/Scripts/008_Audio/002_Audio_Play.rb:1–68, 102–118, 152–168, 202–233`、`Data/Scripts/004_Game classes/002_Game_System.rb:44–149, 153–249`、`Data/Scripts/008_Audio/001_Audio.rb:1–154`。它们分别限定字面/后缀查找、路由/提前返回、请求/登记/有限重试和时长，不证明音色库消费。 |\n'
        note += '| 第七轮原生及保留边界 | 固定 R 的 `Game.exe` 仅重新核完整文件身份；另读取 C2 `4580645dfbfec4a3c7ccbad56ae293cc619b0d25` 的 `tasks/R7-C11/challenges/native/forward-map.json` 既有有限接口/注册与具名未读依赖证据，未新读整份原生程序。L04 配置供应/分派、L09 接受/guard/合成/声音保持未知；原 SF2 全结构、独立复算、配置审查事实保留，本项不重审 SF2 算法，不指定未来格式/后端/API或旧兼容配置。 |\n'
        note += '| 第七轮候选与向量 | 正文 §7/§10、目录独立向量 `GR7-D07-001-S01` 与 F05-02 同步；C11-V01–V08、D07-SF-CFG-01–06 的逐项前提/结果/阶段保留于本批 `evidence/author/per-id.json`，行为全部 NOT_EXECUTED。候选待非作者核验和 R7-I 接收，不提升原批准及宿主状态。 |\n'
        section = section.replace(anchor,note+anchor)
        text = text[:start]+section+text[end:]
        scope = ['仅T-WP15-01追加三个来源/资格/向量行；其余审查/未知原字节保留']
    else:
        raise AssertionError(path)
    new = text.encode('utf-8')
    destination = ROOT/item['candidate_path']
    destination.parent.mkdir(parents=True,exist_ok=True)
    if destination.exists():
        assert destination.read_bytes() == new, 'conflicting candidate bytes: ' + str(destination)
    else:
        destination.write_bytes(new)
    rows.append({'original_path':path,'candidate_path':item['candidate_path'],
                 'base_commit':B,'base':identity(old),'candidate':identity(new),
                 'scope':scope,'contract_scopes':item['scopes']})
    diffs.append(''.join(difflib.unified_diff(old.decode().splitlines(True),text.splitlines(True),fromfile='B/'+path,tofile=item['candidate_path'],n=0)))
save_json('artifact-manifest.json',{'schema':'r7-u13-author-artifact-manifest.v1','batch_id':'R7-U13','record_ids':['GR7-D07-001'],'status':'CANDIDATE_READY_NOT_REVIEWED','base_commit':B,'base_repository_tree':'84f79ec6e772aacbf3a464fde68cdc5a280e2950','base_formal_tree':'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c','reference_commit':R,'reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','artifacts':rows,'evidence_identity_qualification':'Each complete mirror binds original B/new bytes, SHA256 and Git blob above. All evidence files are additionally bound by the final candidate commit/tree and full remote per-file readback; this manifest does not claim a self-hash.'})
(EVIDENCE/'changes.patch').write_text('\n'.join(diffs))
save_json('execution-context.json',{'schema':'r7-u13-actual-author-context.v1','observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'role':'R7-U13-author','actual_thread_id':os.environ.get('CODEX_THREAD_ID','UNVERIFIED'),'source_thread_id':'01a13f49-a154-7054-9b04-ce31f924d01c','actual_platform_task_id':os.environ.get('CODEX_TASK_ID','UNVERIFIED'),'actual_separate_context_id':os.environ.get('CODEX_CONTEXT_ID','UNVERIFIED'),'environment_id':os.environ.get('CODEX_ENVIRONMENT_ID','UNVERIFIED'),'evidence_process_pid':os.getpid(),'evidence_process_parent_pid':os.getppid(),'pid_qualification':'PID belongs to this public author tooling invocation; no separate model CLI was started. Platform model-process PID is not exposed.','requested_configuration':{'model':'gpt-6.1-sol','reasoning_effort':'xhigh','service_tier':'default','speed':'ordinary','fast':'forbidden'},'effective_configuration':{'model':'UNVERIFIED','reasoning_effort':'UNVERIFIED','service_tier':'UNVERIFIED','speed':'UNVERIFIED'},'effective_configuration_qualification':'No runtime configuration echo available; task argv, self-report, tool exit0 and environment identity do not attest effective model settings. No quota/authentication inspection.','subtasks_or_reviewers_created':0,'candidate_review':'NOT_STARTED_BY_AUTHOR'})
print(json.dumps({'status':'FOUR_COMPLETE_MIRRORS_WRITTEN','mirrors':rows,'diff_path':str(EVIDENCE/'changes.patch')},ensure_ascii=False,indent=2))
