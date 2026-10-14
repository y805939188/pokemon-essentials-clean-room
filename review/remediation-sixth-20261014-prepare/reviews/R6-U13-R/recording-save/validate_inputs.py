import datetime
import difflib
import hashlib
import json
import pathlib
import platform
import re
import subprocess

ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room')
P=ROOT/'review/remediation-sixth-20261014-prepare'
OWN=P/'reviews/R6-U13-R/recording-save'
def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT)
def identity(b):
    return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),
                git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
contract=json.loads((P/'contracts/R6-U13.json').read_text())
blocks=re.findall(r'```json\n(.*?)\n```',(P/'prompts/R6-U13-R.md').read_text(),re.S)
common=json.loads(blocks[1])
remote=json.loads((P/'reviews/R6-U13-R/counter-remote-recovery.json').read_text())
frozen=json.loads((P/'inputs/frozen-inputs.json').read_text())
manifest=json.loads((P/'candidates/R6-U13/evidence/candidate-manifest.json').read_text())
checks=[]
for m in manifest:
    for role,path,binding,commit in [
        ('baseline',m['formal_path'],m['baseline'],'8ea169fbd0f33f378b5d732fd6bea59e854e04a6'),
        ('candidate',m['candidate_path'],m['candidate'],'00b45de642f07cee9953e42f04cce9c35d77346f')]:
        b=git('show',commit+':'+path)
        checks.append(dict(role=role,path=path,commit=commit,**identity(b),
                           binding_match=identity(b)==binding,
                           working_bytes_match=(ROOT/path).read_bytes()==b,
                           mode_type_blob=git('ls-tree',commit,'--',path).decode().strip()))
seen=set()
for line in (OWN/'reading-ledger.jsonl').read_text().splitlines():
    r=json.loads(line)
    if r.get('kind')!='git' or not r['locator'].startswith('8c5911'):continue
    if r['locator'] in seen:continue
    seen.add(r['locator']);path=r['locator'].split(':',1)[1]
    f=next(v for v in frozen['source_materials'] if v['path']==path)
    b=git('show',r['locator'])
    checks.append(dict(role='reference',path=path,**identity(b),
                       binding_match=all(identity(b)[k]==f[k] for k in identity(b)),
                       mode_type_blob=git('ls-tree','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','--',path).decode().strip()))
ids=next(v for v in contract['scope_contracts'] if v['id']=='GR6-F-S001')['bidirectional_evidence']['counter_evidence_ids']
for ev in ids:
    f=common[ev];b=(P/'inputs/evidence'/f['path']).read_bytes()
    checks.append(dict(role='counterevidence',path=f['path'],ev=ev,**identity(b),
                       binding_match=all(identity(b)[k]==f[k] for k in identity(b)),
                       fixed_blob_bytes_match=git('cat-file','blob',f['git_blob'])==b,
                       commit_membership='PEER_ROOT_FIXED_REF_REMOTE_VERIFIED',
                       remote_receipt_match=any(v['id']==ev and v['ref']==f['commit'] and
                                                v['path'].endswith('/'+f['path']) and
                                                all(v[k]==f[k] for k in ('bytes','sha256','git_blob')) and
                                                v['equal'] for v in remote['results'])))
hist=[]
author_hist=json.loads((P/'candidates/R6-U13/evidence/historical-regression.json').read_text())
for r in json.loads((OWN/'historical-scope-extract.json').read_text()):
    b=git('show',r['binding']['commit']+':'+r['binding']['path']);d=json.loads(b)
    for k in r['pointer'].split('/')[1:]:d=d[int(k)] if isinstance(d,list) else d[k]
    a=next(v for v in author_hist['R2_B13_controls']['assigned_scopes'] if v['id']==r['id'])['qualified_scope']
    hist.append(dict(id=r['id'],pointer=r['pointer'],original_file_identity_match=all(identity(b)[k]==r['binding'][k] for k in identity(b)),
                     common_fields_match=all(d[k]==v for k,v in a.items() if k not in ('projection_boundary','extensions')),
                     projected_extensions_match=all(e in d.get('extensions',[]) for e in a.get('extensions',[])),
                     earlier_naive_full_extension_equality=r['author_subset_matches'],
                     projection_note='003 intentionally narrows to named affected paths; full-list inequality is not a defect.'))
diffs=[]
for name in ['combat-requirements/wp56-palace-and-arena-variants.md','combat-requirements/wp58-battle-recording-and-playback.md','pokemon-rules/wp53-safari-and-bug-catching-contest.md','test-catalog/combat-requirements-wp54-55-56-58.md','test-catalog/pokemon-rules-wp53-60-61-62-69-70.md']:
    path='deliverables/final-specification-set/'+name
    a=git('show','8ea169fbd0f33f378b5d732fd6bea59e854e04a6:'+path).decode()
    b=(P/'candidates/R6-U13/mirror'/path).read_text()
    diffs.extend(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile=path,tofile='candidate/'+path,n=2))
(OWN/'reviewed-diff.patch').write_text(''.join(diffs))
count={}
text=(P/'candidates/R6-U13/mirror/deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md').read_text()
for title,prefix in [('QC','Q'),('WS','W'),('PA','P'),('RC','W')]:
    section=text.split('## '+title+'：',1)[1].split('\n## ',1)[0]
    values=re.findall(r'^\| ('+prefix+r'\d+[a-z]?) \|',section,re.M)
    count[title]=dict(count=len(values),unique=len(set(values)))
sf=(P/'candidates/R6-U13/mirror/deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md').read_text()
rows=re.findall(r'^\| (SF\d+) \|',sf,re.M);count['SF']=dict(count=len(rows),unique=len(set(rows)))
prior=git('show','8ea169fbd0f33f378b5d732fd6bea59e854e04a6:deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md').decode()
suffix_equal=prior.split('## BP：',1)[1]==sf.split('## BP：',1)[1]
nums=dict(percent_1_of205=100*1//205,percent_3_of205=100*3//205,
          factor_h24_max0=30,factor_h24_max1=30,random0_hits_30=0<30,
          equal_positive_percent_is_strict_increase=(100*3//205)>(100*3//205))
assert nums['percent_1_of205']==0 and nums['percent_3_of205']==1
result=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),cwd=str(ROOT),
            runtime=platform.python_version(),evidence_level='TOOL_VALIDATION_AND_CONSTANT_ARITHMETIC',
            prompt_contract_semantic_equal=json.loads(blocks[0])==contract,
            reference_tree_match=git('rev-parse','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b^{tree}').decode().strip()==frozen['reference_tree'],
            payload_checks=checks,historical_projection_checks=hist,test_catalog_counts=count,
            non_SF_shared_suffix_byte_equal=suffix_equal,constant_arithmetic=nums,
            reference_execution=False,behavior_model=False,real_save=False)
(OWN/'identity-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
assert result['prompt_contract_semantic_equal'] and result['reference_tree_match'] and suffix_equal
assert all(all(v for k,v in r.items() if k.endswith('_match')) for r in checks)
assert all(all(v for k,v in r.items() if k.endswith('_match')) for r in hist)
assert count=={'QC':{'count':49,'unique':49},'WS':{'count':36,'unique':36},'PA':{'count':32,'unique':32},'RC':{'count':29,'unique':29},'SF':{'count':40,'unique':40}}
print(json.dumps(dict(payload_checks=len(checks),history_checks=len(hist),catalog_counts=count,arithmetic=nums,validation='PASS'),ensure_ascii=False))
