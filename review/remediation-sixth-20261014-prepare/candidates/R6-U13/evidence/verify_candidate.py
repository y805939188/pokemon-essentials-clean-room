"""Finite identity, reading coverage, changed-span and catalogue audit.

This executes documentation checks and independent integer arithmetic only.
It does not execute reference behavior, a substitute engine, a writer or host UI.
"""
from pathlib import Path
from collections import Counter
import datetime, difflib, hashlib, json, re, subprocess

REPO = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
PREP = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BASE = 'review/remediation-sixth-20261014-prepare'
PREFIX = BASE+'/candidates/R6-U13/'
CONTRACT = json.loads(subprocess.check_output(['git','show',PREP+':'+BASE+'/contracts/R6-U13.json'],cwd=REPO))

def git(*args):
    return subprocess.check_output(['git',*args],cwd=REPO)

def digest(b):
    return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}

def dump(name, x):
    (OUT/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')

def covered(intervals,n):
    covered=set()
    for a,b in intervals: covered.update(range(a,b+1))
    return len(set(range(1,n+1))-covered)

ledger=[json.loads(l) for l in (OUT/'reading-ledger.jsonl').read_text().splitlines()]
readings={}
for r in ledger:
    key=(r['commit'],r['path']);readings.setdefault(key,[]).append((r['start_line'],r['end_line']))
counter_paths=[BASE+'/inputs/evidence/tasks/R6-F/'+p for p in [
 'countercheck-input-provenance.json','countercheck-ui-entry-stale-command.json',
 'counterchecks-safari-generator.json','counterchecks-variants.json',
 'generator/counterchecks-root-findings.json','isolated-entry-rejection-counter.json',
 'root-findings-countercheck-input.json']]
counter_checks=[]
for p in counter_paths:
    b=git('show',PREP+':'+p);n=len(b.splitlines());gap=covered(readings.get((PREP,p),[]),n)
    assert gap==0,(p,gap)
    counter_checks.append({'commit':PREP,'path':p,**digest(b),'lines':n,
                           'presented_intervals':readings[(PREP,p)],'readable_unread':gap,
                           'earlier_execution_not_adopted_as_new_author_execution':True})
dump('counter-packet-identities.json',counter_checks)
sources=CONTRACT['read_only_reference_paths']
assert isinstance(sources,list)
formal=CONTRACT['candidate_formal_paths']
identities=[]
for kind,commit,paths in [('source',REF,sources),('formal',MAIN,formal)]:
    for p in paths:
        b=git('show',commit+':'+p);n=len(b.splitlines())
        gap=covered(readings.get((commit,p),[]),n)
        assert gap==0,(kind,p,gap)
        identities.append({'kind':kind,'commit':commit,'path':p,**digest(b),'lines':n,
                           'presented_intervals':readings[(commit,p)],'readable_unread':gap})

promptpath=BASE+'/prompts/R6-U13-A.md'
prompt=git('show',PREP+':'+promptpath)
assert digest(prompt)=={'bytes':485217,'sha256':'8d8203cf36be44e060690ebaf668d9be58f36666cd69d8b8ffb4a9618dc8ed8c','git_blob':'5f5eec18555b03a9d855907fa3409c1884f5f26d'}
contract=git('show',PREP+':'+BASE+'/contracts/R6-U13.json')
embedded=prompt.decode().split('```json\n',1)[1].split('\n```',1)[0].encode()
assert embedded==contract.rstrip(b'\n')
ag=git('show',PREP+':AGENTS.md')
assert ag==(REPO/'AGENTS.md').read_bytes()
dump('input-identities.json',{'prepare':PREP,'formal':MAIN,'reference':REF,
 'prompt':{'path':promptpath,**digest(prompt),'lines':8383,
 'manual_contiguous_read_segments':[[1,170],[171,770],[771,1370],[1371,1970],[1971,2570],[2571,3170],[3171,3770],[3771,4370],[4371,4970],[4971,5570],[5571,6170],[6171,6770],[6771,7370],[7371,7670],[7671,7970],[7971,8383]],
 'semantic_attestation':'Author fully read all these segments before edits; initial reads preceded JSONL helper; UTC/command receipts for these initial ranges are not reconstructed. One truncated larger presentation was reread in two complete halves.'},
 'contract':{'path':BASE+'/contracts/R6-U13.json',**digest(contract),'full_read':'Identical first JSON block fully read through prompt line7106; initial truncated cat not counted.'},
 'AGENTS':{'path':'AGENTS.md',**digest(ag),'full_read':True},'required_source_and_formal':identities})

# Check all bidirectional fixed payloads used by each contract, not a search hit.
payload_checks=[]
for scope in CONTRACT['scope_contracts']:
    for kind in ['source','formal']:
        for z in scope['bidirectional_evidence'][kind]:
            ident=z['payload_identity'];b=git('show',ident['commit']+':'+ident['path'])
            observed=digest(b)
            assert all(observed[k]==ident[k] for k in observed),(scope['id'],ident['path'])
            payload_checks.append({'id':scope['id'],'kind':kind,'locator':z['locator'],
                                   'commit':ident['commit'],'path':ident['path'],**observed,'identity_matches':True})
dump('contract-payload-checks.json',payload_checks)

changed=git('diff','--name-only',PREP).decode().splitlines()
untracked=git('ls-files','--others','--exclude-standard').decode().splitlines()
allowed={PREFIX+'mirror/'+p for p in formal}
assert len(allowed)==8
assert all(p in allowed or p.startswith(PREFIX+'evidence/') for p in changed+untracked)
assert set(changed)&allowed==allowed
assert git('branch','--show-current').decode().strip()=='codex/remediation-sixth-r6-u13-author-20261014'
subprocess.run(['git','diff','--check'],cwd=REPO,check=True)

manifest=[];spans=[]
for p in formal:
    old=git('show',MAIN+':'+p);baseline=git('show',PREP+':'+PREFIX+'mirror/'+p)
    new=(REPO/PREFIX/'mirror'/p).read_bytes()
    assert baseline==old and new!=old,p
    manifest.append({'formal_path':p,'candidate_path':PREFIX+'mirror/'+p,
                     'baseline':digest(old),'candidate':digest(new),'baseline_mirror_equals_fixed_main':True})
    sm=difflib.SequenceMatcher(None,old.decode().splitlines(),new.decode().splitlines(),autojunk=False)
    for tag,a,b,c,d in sm.get_opcodes():
        if tag!='equal':spans.append({'path':p,'operation':tag,'old_lines':[a+1,b],
                                      'new_lines':[c+1,d],'old_text':old.decode().splitlines()[a:b],
                                      'new_text':new.decode().splitlines()[c:d]})
dump('candidate-manifest.json',manifest)
dump('changed-spans.json',spans)

ct='deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md'
pt='deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'
before=git('show',MAIN+':'+ct).decode();after=(REPO/PREFIX/'mirror'/ct).read_text()
def groups(s):
    parts=re.split(r'^## ',s,flags=re.M)
    names=[p.split('：',1)[0] for p in parts[1:]]
    assert len(names)==len(set(names)),('duplicate series headers',names)
    return {p.split('：',1)[0]:p for p in parts[1:]}

def catalogue_rows(s, pattern, label):
    raw=[l for l in s.splitlines() if re.match(pattern,l)]
    ids=[l.split('|')[1].strip() for l in raw]
    duplicates={k:v for k,v in Counter(ids).items() if v>1}
    assert not duplicates,(label,duplicates)
    audit={'series':label,'raw_row_count':len(raw),'unique_id_count':len(set(ids)),
           'duplicate_counts':duplicates,'raw_ids':ids,'checked_before_indexing':True}
    return dict(zip(ids,raw)),audit

def sf30_subcase_presence(line):
    columns=line.split('|')
    assert len(columns)==5 and columns[1].strip()=='SF30'
    inp,out=columns[2],columns[3]
    return {
      'normal_save_load_input':all(t in inp for t in ['d两会话正常结束后','保存/普通载入依赖有效','正常保存→载入']),
      'normal_nonactive_and_statistics':all(t in out for t in ['d会话仍为未开始/已结束态','模式统计字段持久']),
      'normal_clock_and_execution_limits':all(t in out for t in ['计时起点等运行时刻值的重载语义仍未知','仅静态设计、未执行真实保存/载入']),
      'default_conversion_search_input':all(t in inp for t in ['e检索固定参考当前默认保存转换集合与注册者','排除插件/动态追加']),
      'dedicated_conversion_absence':all(t in out for t in ['e当前默认集合无Safari/捕虫专用格式转换','普通载入无针对两会话的专用格式迁移']),
      'conversion_no_generalization': '不外推任意版本/插件或整个存档都无迁移' in out}

counts={};preservation=[];raw_row_audits=[]
for g,n,modified in [('QC',49,set()),('WS',36,{'W13'}),('PA',32,{'P14','P15','P16'}),('RC',29,{'W18'})]:
    a=groups(before)[g];b=groups(after)[g]
    oldrows,old_audit=catalogue_rows(a,r'^\| [QWP]\d',g+' baseline')
    newrows,new_audit=catalogue_rows(b,r'^\| [QWP]\d',g+' candidate')
    assert new_audit['raw_row_count']==n
    raw_row_audits.extend([old_audit,new_audit])
    assert all(k in newrows for k in oldrows)
    for k,v in oldrows.items():
        if k not in modified:assert newrows[k]==v,(g,k)
    counts[g]=n
    preservation.append({'series':g,'original_count':len(oldrows),'current_count':n,
                          'changed_original_rows':sorted(modified),'all_other_original_rows_byte_equal':True,
                          'changed_row_semantics_proved_by_this_tool':False})
pb=git('show',MAIN+':'+pt).decode();pa=(REPO/PREFIX/'mirror'/pt).read_text()
assert pb.split('## BP：',1)[1]==pa.split('## BP：',1)[1]
oldsf,old_audit=catalogue_rows(pb,r'^\| SF\d','SF baseline')
newsf,new_audit=catalogue_rows(pa,r'^\| SF\d','SF candidate')
raw_row_audits.extend([old_audit,new_audit])
assert new_audit['raw_row_count']==40
assert all(k in newsf for k in oldsf)
assert all(newsf[k]==v for k,v in oldsf.items() if k not in {'SF01','SF30'})
sf30_presence=sf30_subcase_presence(newsf['SF30'])
assert all(sf30_presence.values()),sf30_presence
prior=git('show','00b45de642f07cee9953e42f04cce9c35d77346f:'+PREFIX+'mirror/'+pt).decode()
prior_sf,_=catalogue_rows(prior,r'^\| SF\d','SF prior FAIL candidate')
oldcols=prior_sf['SF30'].split('|');newcols=newsf['SF30'].split('|')
assert newcols[2].strip().startswith(oldcols[2].strip())
assert newcols[3].strip().startswith(oldcols[3].strip())
counts['SF']=40
preservation.append({'series':'SF','original_count':35,'current_count':40,'changed_original_rows':['SF01','SF30'],'all_other_original_rows_byte_equal':True,'BP_FP_PD_VF_LT_suffix_byte_equal':True,
 'SF30_new_menu_input_and_expected_prefix_byte_equal':True,'SF30_restored_subcase_presence':sf30_presence,
 'subcase_check_limit':'Text-presence and exact menu-prefix checks; author static comparison in repair-01/report.md establishes the bounded meaning. This tool does not prove arbitrary changed-row semantics or runtime save/load.'})

wp40='deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md'
wold=git('show',MAIN+':'+wp40).decode();wnew=(REPO/PREFIX/'mirror'/wp40).read_text()
addon='Arena 裁判调用同一完整取消：只清列明持续招，回复期为正时保留当前招身份；裁判后的存活未替代者仍受下一轮回复门约束（WP56 §3.2），败者倒下/补位清效另算。'
assert wnew.replace(addon,'')==wold
dump('tool-validation.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cwd':str(REPO),
 'argv':['python',str(Path(__file__).relative_to(REPO))],'exit':0,'stderr':'',
 'checks':{'allowlist':True,'eight_actual_mirror_changes':True,'baseline_fixed_main':True,'fixed_identity_checks':True,'whole_required_read_coverage':True,'diff_check':True,'unique_catalogue_ids':True,'catalogue_counts':counts},
 'preservation':preservation,'raw_catalogue_rows':raw_row_audits,'wp40_old_text_equal_after_removing_only_arena_addition':True,
 'arithmetic':{'1x100_div205':1*100//205,'3x100_div205':3*100//205,'r0_less_expected30':0<30},
 'expected_constants_not_computed':{'h24_m0_factor':30,'h24_m1_factor':30},
 'probability_factor_semantics_proved_by_this_tool':False,
 'level':'TOOL_DOCUMENT_AUDIT_AND_INDEPENDENT_ARITHMETIC','reference_execution':False,'behavior_model_execution':False,'writer_execution':False,'host_execution':False})
print(json.dumps({'status':'AUTHOR_TOOL_CHECKS_PASS_NOT_INDEPENDENT_REVIEW','counts':counts,'mirror_files':len(manifest),'required_source_files':len(sources),'formal_files':len(formal),'write_scope':PREFIX},ensure_ascii=False))
