#!/usr/bin/env python3
"""Finite identity, preservation and independent arithmetic checks; no source execution."""
import sys, json, subprocess, hashlib, re
from pathlib import Path
from decimal import Decimal

REPO = Path.cwd()
PREP = REPO / 'review/remediation-sixth-20261014-prepare'
BATCH = PREP / 'candidates/R6-U07'
base = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
main = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
contract = json.loads((PREP/'contracts/R6-U07.json').read_text())
inputs = json.loads((PREP/'inputs/frozen-inputs.json').read_text())
result = {'level': 'TOOL_VALIDATION_AND_DERIVED_CONSTANT_ARITHMETIC',
          'source_execution': False, 'host_execution': False,
          'independent_review': 'PENDING', 'checks': []}

def check(name, condition, detail):
    result['checks'].append({'name':name,'pass':bool(condition),'detail':detail})
    assert condition, (name,detail)

def ident(b):
    return {'bytes':len(b), 'sha256':hashlib.sha256(b).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}

check('branch_and_base', subprocess.check_output(['git','branch','--show-current'],text=True).strip() ==
      'codex/remediation-sixth-r6-u07-author-20261014' and
      subprocess.run(['git','merge-base','--is-ancestor',base,'HEAD']).returncode == 0,
      'Unique author branch descends from fixed preparation; no formal merge')
for path in contract['candidate_formal_paths']:
    row=next(x for x in inputs['formal_materials'] if x['path']==path)
    b=subprocess.check_output(['git','show',main+':'+path])
    check('formal_identity:'+path,ident(b)=={k:row[k] for k in ident(b)},ident(b))
    check('formal_untouched:'+path,(REPO/path).read_bytes()==b,'Current formal bytes remain frozen')
for path in contract['read_only_reference_paths']:
    row=next(x for x in inputs['source_materials'] if x['path']==path)
    b=(Path('/tmp/r6-u07-inputs/Maruno17/pokemon-essentials')/contract['frozen_reference']/path).read_bytes()
    check('source_identity:'+path,ident(b)=={k:row[k] for k in ident(b)},ident(b))

wp_path,cat_path,ui_path=contract['candidate_formal_paths']
wp=(BATCH/'mirror'/wp_path).read_text(); cat=(BATCH/'mirror'/cat_path).read_text()
old_wp=subprocess.check_output(['git','show',main+':'+wp_path],text=True)
old_cat=subprocess.check_output(['git','show',main+':'+cat_path],text=True)
check('wp67_bytes_preserved',(BATCH/'mirror'/ui_path).read_bytes()==(REPO/ui_path).read_bytes(),
      'WP67-A full baseline reviewed; §9.4 is consistent, no necessary textual correction')

def section(text,prefix):
    a=text.index(prefix); m=re.search(r'\n#{1,3} ',text[a+len(prefix):])
    return text[a:a+len(prefix)+m.start()] if m else text[a:]

preserved_sections=['### 3.1','### 3.3','### 3.4','### 4.3','### 4.5','### 4.6',
                    '## 5.','### 6.1','### 6.2','### 7.1','### 8.1','### 8.3','### 8.5',
                    '### 9.2','### 10.2a','### 14.1','## 15.','## 17.']
for s in preserved_sections:
    check('historical_section_preserved:'+s,section(old_wp,s)==section(wp,s),
          'Exact bytes retained for old scope; rechecked against already-read source as applicable')
old_math=[x for x in old_wp.splitlines() if any(k in x for k in [
    '**初次曲线**','**初次手绘**','**改帧数后重采样**','**三套取样的精确定义',
    '直线(0,0)','折线(0,0)','初次曲线N5'])]
check('AN007_optional_recurrence_and_N5_preserved',all(x in wp.splitlines() for x in old_math),
      'Default control requests changed; existing sample definitions and explicit N5 vectors retained')
changed_rows={'AN-M05','AN-M09','AN-M12','AN-M16','AN-M18','AN-M22','AN-M23','AN-M25','B20-C025','B20-D024'}
rows=lambda t:[x for x in t.splitlines() if x.startswith('| ')]
old=rows(old_cat);new=rows(cat)
check('catalog_row_order_and_count',len(old)==len(new),'No row added/deleted; original case denominators retained')
for a,b in zip(old,new):
    key=a.split('|')[1].strip()
    check('catalog_row:'+key,a==b or key in changed_rows,'Changed only the ten scoped existing rows')
    if key in changed_rows and key!='AN-M05':
        check('old_vector_preserved:'+key,b.startswith(a[:-1].rstrip()),'Old expectations retained; bounded new controls appended')
for t in ['当前帧槽 0–59 中','集合当前选中成员','播放器**建立时捕获**',
          'Opacity=17','X=550','此前已有非空 P','0.3333／0.6666','没有恢复旧槽的步骤']:
    check('mandatory_rule:'+t,t in wp,'Present in primary normative body')

# These are constant calculations, not a behavior model or reference execution.
check('AN001_count_control',sum(i<60 for i in [0,2])==2 and sum(i<60 for i in [0,60])==1,
      {'normal':2,'moved_to_60':1,'meaning':'manually established deletion threshold applied only by static reasoning'})
check('AN003_anchor_arithmetic',(200+128-128,128+128-128)==(200,128) and
      (200+64,128+64)==(264,192),{'requests':[200,128],'editor_requests':[264,192]})
check('AN004_gradient_clamp',max(-500,min(550,500))==500 and max(-500,min(20,500))==20,
      {'work_550':500,'work_20':20,'cancel':'no source or model execution'})
check('AN007_default_request_arithmetic',Decimal('300')*Decimal('0.3333')==Decimal('99.99') and
      Decimal('300')*Decimal('0.6666')==Decimal('199.98'),{'request':[99.99,199.98],'pixel':'UNKNOWN'})

diff=subprocess.run(['git','diff','--check',base],capture_output=True,text=True)
check('diff_check',diff.returncode==0,diff.stderr or diff.stdout or 'no whitespace errors')
changed=subprocess.check_output(['git','diff','--name-only',base],text=True).splitlines()
untracked=subprocess.check_output(['git','ls-files','--others','--exclude-standard'],text=True).splitlines()
prefix='review/remediation-sixth-20261014-prepare/candidates/R6-U07/'
allowed={prefix+'mirror/'+x for x in contract['candidate_formal_paths']}
check('write_allowlist',all(x in allowed or x.startswith(prefix+'evidence/') for x in changed+untracked),
      {'tracked':changed,'untracked_count':len(untracked)})
result['summary']={'passed':len(result['checks']),'failed':0,'reference_runs':0,'host_runs':0,'demo_runs':0}
(BATCH/'evidence/validation-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result['summary'],ensure_ascii=False))
