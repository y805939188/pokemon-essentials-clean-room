"""Fresh R-B04 actual metadata audit; no reference behavior is executed or modeled."""
import collections
import csv
import datetime
import difflib
import gzip
import hashlib
import json
from pathlib import Path
import re
import subprocess

R=Path('/workspace/pokemon-essentials-clean-room')
T=Path(__file__).resolve().parent
OUT=T if str(T).startswith('/tmp/') else Path('/tmp/b09-b04-actual-audit-output')
OUT.mkdir(parents=True,exist_ok=True)
REF=Path('/tmp/b09-b04-actual-reference')
A='dc64807c2d726171827017ec636c6a73efd8e4b5'
C='18873059e56314fcd48f6081d5a65a79301a52f6'
B='407536adb682a04161d3e9c82f153a62b1becd97'
PAY='3ec4af10f9822999b329ac794e4694bc5aa89aac'
G='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
P='41fffb540c6483f5296ea0d33b789b75180d27ed'
S='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
OLD='d9bdc21825ac484bdc8f93a3a3dea1642912257d'
B05='2790043cc7f605fd58489806ce2dc8c54ffbeb2c'
Q='review/remediation/20261003-prepare/batches/B09/'
ST=Q+'integration-stage-1/'
FLAGS=['--no-ext-diff','--no-textconv','--no-color','--no-renames','--binary','--full-index','--unified=3']
checks=[];bindings=[];cache={}

def git(*args,cwd=R):return subprocess.check_output(['git',*args],cwd=cwd)
def content(c,p):
    k=(c,p)
    if k not in cache:cache[k]=git('show',c+':'+p,cwd=REF if c==S else R)
    return cache[k]
def sha(b):return hashlib.sha256(b).hexdigest()
def obj(c,p):return json.loads(content(c,p))
def canonical(v):return sha(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def identity(c,p):
    b=content(c,p)
    return dict(commit=c,path=p,git_blob=git('rev-parse',c+':'+p,cwd=REF if c==S else R).decode().strip(),sha256=sha(b),bytes=len(b))
def check(ok,kind,label):checks.append(dict(kind=kind,label=label,passed=bool(ok)))
def verify(v,default,label,path=None):
    p=v.get('path') or path
    if not p or not all(k in v for k in ['git_blob','sha256','bytes']):return
    c=v.get('commit') or default
    actual=identity(c,p)
    ok=all(v[k]==actual[k]for k in ['git_blob','sha256','bytes'])
    check(ok,'identity',label+' '+c+':'+p)
    bindings.append(dict(label=label,declared=v,actual=actual,matched=ok))
def walk(v,label,default=A,path=None):
    if isinstance(v,dict):
        verify(v,default,label,path)
        for k,x in v.items():walk(x,label+'/'+k,B if k=='baseline'else C if k=='reviewed_candidate'else default,v.get('path')or path)
    elif isinstance(v,list):
        for i,x in enumerate(v):walk(x,label+'/'+str(i),default,path)
def paths(a,z):return [x.split('\t')for x in git('diff','--name-status','--no-renames',a,z).decode().splitlines()]
def diff(a,z,ps=()):return git('diff',*FLAGS,a,z,*(['--',*ps]if ps else []))
def write(n,v):(OUT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def evidence(n):
    p=T/n
    return p.read_bytes() if p.exists() else gzip.decompress((T/(n+'.gz')).read_bytes())

ba=paths(B,A);ca=paths(C,A);bc=paths(B,C)
check(len(ba)==199 and collections.Counter(s for s,p in ba)=={'M':24,'A':175},'scope','B-to-A all199=24M+175A')
check(len(ca)==112 and collections.Counter(s for s,p in ca)=={'M':10,'A':102},'scope','C-to-A all112=10M+102A')
check(all(s in ['M','A']for s,p in ba+ca),'scope','no deletion/rename/type changes')
formal=[p for s,p in bc if s=='M'];public=[p for s,p in ca if s=='M']
check(len(formal)==14 and len(set(formal))==14 and len(public)==10,'scope','14 formal and10 public exact partition')
check(set(p for s,p in ba if s=='M')==set(formal+public),'scope','no extra modified path')
check(all(p.startswith(Q)for s,p in ba if s=='A'),'scope','all175 additions scoped under B09')
check(all(p.startswith(Q)for s,p in ca if s=='A'),'scope','all102 postcandidate additions under B09')
check(git('cat-file','-t',A).strip()==b'commit' and git('rev-parse',A+'^{tree}').decode().strip()=='6f836ef1e40c1720413b8b1202845320880e0954','identity','real fixed actual commit/tree')
check(git('rev-list','--parents','-n','1',A).decode().split()==[A,PAY],'graph','actual single parent payload')
check(subprocess.run(['git','merge-base','--is-ancestor',B,A],cwd=R).returncode==0 and subprocess.run(['git','merge-base','--is-ancestor',C,A],cwd=R).returncode==0,'graph','B/C ancestry')
dm=obj(A,ST+'diff-and-freeze.json');m=obj(A,ST+'integration-manifest.json')
check(paths(PAY,A)==[['A',p]for p in sorted(dm['expected_actual_changed_paths'])],'envelope','exact3 final evidence additions')
check(dm['expected_actual_parent']==PAY and dm['payload_tree']==git('rev-parse',PAY+'^{tree}').decode().strip(),'envelope','payload frozen identity')
for label,b in [('baseline',B),('candidate',C)]:
    check(diff(b,A)==evidence(label+'-to-actual.diff'),'diff','independent full unfiltered '+label+'-to-actual')
check(diff(B,A,formal)==(T/'formal.diff').read_bytes() and diff(C,A,public)==(T/'public.diff').read_bytes(),'diff','complete scoped formal/public diffs')
formal_pairs=[]
for p in formal:
    check(content(C,p)==content(A,p),'formal','exact candidate-to-actual body '+p)
    formal_pairs.append(dict(path=p,before=identity(B,p),reviewed_candidate=identity(C,p),actual=identity(A,p),candidate_actual_bytes_equal=True))
check(len(m['source_identities'])==175 and len(m['reviewed_normative_identities'])==14 and set(m['public_write_paths'])==set(public),'scope','stage source/formal/public counts')
for v in m['source_identities']:
    verify(v,C,'incoming exact source')
    check(content(v['commit'],v['path'])==content(A,v['path']),'history','actual preserves incoming source '+v['path'])
for v in m['reviewed_normative_identities']:verify(v,C,'declared reviewed14')
for report in m['candidate_reports']:
    rows=paths(C,report['commit'])
    check(len(rows)==report['path_count'] and all(s=='A'and p.startswith(report['report_directory'])for s,p in rows),'history','isolated historical report '+report['role'])
    check(git('rev-list','--parents','-n','1',report['commit']).decode().split()==[report['commit'],C],'history','candidate report parent '+report['role'])
    for s,p in rows:check(content(report['commit'],p)==content(A,p),'history','historical report bytes '+p)
for merge in m['normal_native_merges']:
    c=merge['result']
    check(git('rev-list','--parents','-n','1',c).decode().split()[1:]==merge['parents'] and git('rev-parse',c+'^{tree}').decode().strip()==merge['tree'],'graph','native integration result '+c)
for n in ['candidate-to-payload-identities.json','upstream-to-payload-identities.json']:
    v=obj(A,ST+n);rows=paths(v['before_commit'],PAY)
    check([(x['change'],x['path'])for x in v['changed_paths']]==[tuple(x)for x in rows],'diff','payload full identity manifest '+n)
    check(v['command'][:6]==['git','diff','--no-ext-diff','--no-textconv','--no-renames','--binary'] and v['command'][6:]==[v['before_commit'],PAY],'diff','explicit unfiltered recorded command '+n)
    raw=git(*v['command'][1:])
    check(len(raw)==v['diff_bytes']and sha(raw)==v['diff_sha256'],'diff','payload full diff hash '+n)
    walk(v,n)
for n in ['integration-manifest.json','diff-and-freeze.json','current-readers.json','scope-and-observation-registration.json','downstream-dependency-assessment.json','merge-and-dependency-impact.json','scope-counts.json']:
    walk(obj(A,ST+n),n)
hashrows=list(csv.DictReader(content(A,ST+'current-hashes.tsv').decode().splitlines(),delimiter='\t'))
check(len(hashrows)==18,'identity','18 current public/stage hash rows')
for x in hashrows:
    verify(dict(x,bytes=int(x['bytes'])),A,'current hash table')
ctpath='review/remediation/20261003-prepare/batches/B08/acceptance-stage-1/B09-downstream-contract.json'
ct=obj(B,ctpath)
check(content(B,ctpath)==content(C,ctpath)==content(A,ctpath),'history','accepted B08 B09 contract preserved')
walk(ct,'accepted B09 contract',B)
read=obj(A,ST+'current-readers.json');rc=obj(C,Q+'candidate-2/read-coverage.json')
check(len(read['readers'])==70 and [x['path']for x in read['readers']]==[x['path']for x in rc['readers']],'dependency','current70 exact candidate order')
check([x['path']for x in read['readers'][:62]]==[x['path']for x in ct['planned_reads']],'dependency','original62 plan order retained')
for x in read['readers']:
    p=x['path'];cv=x['reviewed_candidate'].get('commit',C);av=x['actual_current'].get('commit',A)
    check(x['candidate_to_actual_changed']==(content(cv,p)!=content(av,p)),'dependency','current changed marker '+p)
    verify(x['actual_current'],A,'current actual70',p)
check(set(x['path']for x in read['current_public_versions'])==set(public),'dependency','ten current public versions separately frozen')
for x in read['affected_current_scopes']:
    for v in x['actual_current_inputs']:verify(v,A,'affected scope '+x['accepted_batch'])
    check(x['same_normative_blob_does_not_transfer_PASS'],'dependency','no PASS transfer '+x['accepted_batch'])
prior=m['prior_accepted_statistics'];verify(prior,B,'fixed prior completion statistics')
check(content(B,prior['path'])==content(A,prior['path']),'public','prior accepted statistics bytes unchanged')
ba04=obj(B,'review/remediation/20261003-prepare/batches/B04/acceptance-stage-1/acceptance-manifest.json')
check(len(ba04['accepted_formal_identities'])==13,'scope','accepted B04 thirteen paths')
b04=[]
for v in ba04['accepted_formal_identities']:
    p=v['path'];check(content(B,p)==content(C,p)==content(A,p),'history','current accepted B04 path unchanged '+p)
    b04.append(dict(path=p,accepted_manifest_identity=v,baseline=identity(B,p),candidate=identity(C,p),actual=identity(A,p),baseline_actual_equal=True))
for batch in ['B04','B06','B07','B08']:
    p='review/remediation/20261003-prepare/batches/'+batch+'/acceptance-stage-1/acceptance-manifest.json'
    check(content(B,p)==content(A,p),'history','accepted upstream receipt unchanged '+batch)
reg=obj(A,ST+'finding-registration.json')
root={x['id']:x for x in obj(G,'review/global-independent-review/2026-10-03-fd82a639/findings.json')}
acc=obj(P,'review/remediation-20261003-prepare/finding-acceptance.json')
check([d['id']for d in reg['dispositions']]==ct['contribution_finding_ids'],'qualification','all20 order')
check(sum(d['B09_primary']for d in reg['dispositions'])==13,'qualification','13 primary')
controls=[]
for d in reg['dispositions']:
    i=d['id'];o=root[i];a=acc[i];fields=d['complete_current_control_fields'];mins=d['complete_minimum_acceptance_fields']
    check(canonical(o)==d['original_complete_object_sha256'] and canonical(a)==d['acceptance_complete_object_sha256'],'qualification','complete fixed object hashes '+i)
    for k,v in fields.items():check(v==(o[k]if k in o else a.get(k)),'qualification',i+' complete field '+k)
    for k in ['current_qualifications','effective_case_constraints','root_adjudications','extensions','extension_decisions']:
        expected=o.get(k,a.get(k))
        check(expected is None or fields.get(k)==expected,'qualification',i+' no omitted effective field '+k)
    for k,v in mins.items():check(v==a[k],'qualification',i+' minimum/determinate field '+k)
    check(d['canonical_state']=='OPEN'and not d['canonical_edited']and not d['canonical_closure']and d['accepted_B09_contributions']==0,'qualification','no closure/acceptance '+i)
    controls.append(dict(id=i,source_file_identity=identity(G,'review/global-independent-review/2026-10-03-fd82a639/findings.json'),acceptance_file_identity=identity(P,'review/remediation-20261003-prepare/finding-acceptance.json'),original_complete_object_sha256=canonical(o),acceptance_complete_object_sha256=canonical(a),current_control_fields_sha256=canonical(fields),minimum_fields_sha256=canonical(mins),all_complete_fields_match=True,complete_extensions_preserved=True,primary_owner=d['primary_owner'],other_contributors_pending=d['other_contributors_pending'],current_qualifications=o['current_qualifications'],semantic_review_scope='B04 affected interfaces where applicable; not full B09 primary'))
for i in ['GIR-FD82-C071','GIR-FD82-C072','GIR-FD82-C073']:
    o=root[i];a=acc[i]
    controls.append(dict(id=i,original_complete_object_sha256=canonical(o),acceptance_complete_object_sha256=canonical(a),current_qualifications=o['current_qualifications'],complete_effective_control_reference=G+':review/global-independent-review/2026-10-03-fd82a639/findings.json#'+i,complete_acceptance_reference=P+':review/remediation-20261003-prepare/finding-acceptance.json#'+i,owner_body_and_catalog_preserved=True,semantic_review_scope='Current caller positive naming bound and unchanged generic numeric/navigation contract'))
public_audit=[]
for p in public:
    before=content(C,p);after=content(A,p)
    if p.endswith('.tsv'):
        check(after.startswith(before),'public','whole old150 rows byte-prefix '+p)
        rows=list(csv.DictReader(after.decode().splitlines(),delimiter='\t'));old=list(csv.DictReader(before.decode().splitlines(),delimiter='\t'));new=rows[len(old):]
        check(len(old)==150 and len(rows)==170 and [x['finding_id']for x in new]==ct['contribution_finding_ids'],'public','170=150+exact20 rows '+p)
        for row,d in zip(new,reg['dispositions']):
            i=row['finding_id'];remain=json.loads(row['remaining_obligations'])
            check(row['canonical_state']=='OPEN'and row['candidate_commit']==C and row['candidate_review_commit']==m['candidate_reports'][0]['commit'],'public','candidate/open identity '+p+' '+i)
            check(remain['other_batch_obligations']==d['other_contributors_pending']and not remain['canonical_closure']and remain['parent_C']=='NOT_PERFORMED'and remain['actual_full_R09']=='PENDING_ULTRA_STANDARD','public','same complete remaining owner gates '+p+' '+i)
            if p.endswith('approval-ledger.tsv'):
                kind='B09_'+('PRIMARY'if d['B09_primary']else'PARTIAL')+'_CANDIDATE_SCOPED_PENDING_FIVE_ACTUAL_REVIEWS'
                check(row['candidate_verdict']=='PASS_SCOPED'and row['accepted_contribution_kind']==kind and row['downstream_gate']=='BLOCKED'and row['integration_verdict']=='NOT_REVIEWED_PENDING_FIVE_ULTRA_STANDARD','public','no candidate-as-actual approval '+i)
            else:
                cl=json.loads(row['current_clause_inputs']);check(row['accepted_candidate_contribution']=='PASS_SCOPED_B09_CANDIDATE_ONLY'and row['remaining_batches']==';'.join(d['other_contributors_pending'])and cl['reviewed_candidate']==C,'public','trace candidate/scope/remaining '+i)
        public_audit.append(dict(path=p,before=identity(C,p),after=identity(A,p),old150_byte_preserved=True,appended20_rows=new,disposition='CANDIDATE_ONLY_PENDING_FIVE_ACTUAL'))
    elif p.endswith('/test-catalog/README.md'):
        plain=diff(C,A,[p]).decode();minus=[x[1:]for x in plain.splitlines()if x.startswith('-')and not x.startswith('---')]
        check(len(minus)==2 and all('wp31-32-37-38.md' in x or 'wp39-40-41-42-45.md' in x for x in minus),'public','only two catalog range rows replaced')
        check('CP01–CP24' in after.decode()and 'BC01–BC25、CM01–CM33、SW01–SW29' in after.decode()and '未执行' in after.decode(),'public','catalog range/static no runtime claim')
        public_audit.append(dict(path=p,before=identity(C,p),after=identity(A,p),disposition='ONLY_CATALOG_RANGES_AND_PENDING_STATIC_SCOPE'))
    else:
        oldlines=before.decode().splitlines(keepends=True);newlines=after.decode().splitlines(keepends=True)
        ops=difflib.SequenceMatcher(None,oldlines,newlines,autojunk=False).get_opcodes()
        check(all(tag in ['equal','insert']for tag,*_ in ops),'public','whole historical markdown bytes/order preserved '+p)
        added=''.join(''.join(newlines[j1:j2])for tag,i1,i2,j1,j2 in ops if tag=='insert')
        check('B09接受贡献0'in added and '229 OPEN／0 CLOSED'in added and 'B09-G-O01'in added and ('实际配置UNVERIFIED'in added or p.endswith('historical-errata.md')) and 'Ultra/Standard实际报告均绑定同一最终actual SHA'in added,'public','pending/limits/O01 retained '+p)
        public_audit.append(dict(path=p,before=identity(C,p),after=identity(A,p),added_text=added,disposition='PENDING_STATUS_AND_SCOPE_ONLY_NO_NEW_BEHAVIOR'))
sc=obj(A,ST+'scope-counts.json')
def rows(c,p):
    return [(m.group(1),line)for line in content(c,p).decode().splitlines()if(m:=re.match(r'^\|\s*([A-Za-z][A-Za-z0-9-]*\d[A-Za-z0-9-]*)\s*\|',line))]
for p,v in sc['catalog_counts'].items():
    old,new=rows(B,p),rows(A,p);oi=[x[0]for x in old];ni=[x[0]for x in new]
    check(len(old)==v['before']and len(new)==v['after'],'catalog','exact static rows '+p)
    check([x for x in ni if x in oi]==oi and [x for x in ni if x not in oi]==v['added_ids'],'catalog','old order/multiplicity and exact new IDs '+p)
    om=dict(old);nm=dict(new);check([i for i in oi if om[i]!=nm[i]]==v['changed_old_ids'],'catalog','exact old row changes '+p)
for v in sc['protected_whole_sections']:
    p=v['path'];h=v['heading'];b=content(B,p);z=content(A,p)
    def section(data):
        start=data.index(h.encode());end=data.find(b'\n## ',start+1)
        return data[start:end if end>=0 else len(data)]
    check(section(b)==section(z),'catalog','independent whole protected owner section '+p+' '+h)
for v in sc['new_static_designs_not_executed']:
    line=content(A,v['path']).splitlines(keepends=True)[v['line']-1]
    check(v['id'].encode()in line and any(len(x)==v['bytes']and sha(x)==v['sha256']for x in [line,line.rstrip(b'\r\n')])and v['status']=='STATIC_DESIGN_NOT_EXECUTED','catalog','new ID exact static row '+v['id'])
dep=obj(A,ST+'downstream-dependency-assessment.json');b14=dep['B14']
check(len(b14['all72_current_assessment_inputs'])==72 and len(b14['allowed6_write_input_versions'])==6 and not b14['formal_writer_authorized']and not b14['assessment_is_author_baseline'],'dependency','B14 72/6 current assessment not authorization')
check(dep['B09_B14_serialization']['serialization_order']==['B09','B14']and not dep['B09_B14_serialization']['semantic_independence'],'dependency','B09 then B14 serial unchanged')
request=obj(C,Q+'candidate-2/affected-B04-review-request.json')
for x in request['changed_readers']:
    for cl in x['full_before_after_clauses']:check(cl['before_text']in content(B,x['path']).decode()and cl['after_text']in content(A,x['path']).decode(),'clauses','actual full changed-reader text '+x['path']+' '+cl['clause'])
for x in request['untouched_owner_clauses']:
    p=x['path'];lo,hi=x['lines'];excerpt=''.join(content(A,p).decode().splitlines(keepends=True)[lo-1:hi])
    check(excerpt==x['before_text']==x['after_text']and content(B,p)==content(A,p),'clauses','untouched owner exact '+p+' '+str(x['lines']))
for p in [Q+'candidate-1/original-scope-approval.json',Q+'scope-amendment-2/approval.json',Q+'scope-amendment-2/application.json']:
    check(content(C,p)==content(A,p),'scope','exact permission/application preserved '+p)
obs=obj(A,ST+'scope-and-observation-registration.json')['report_wording_observations'][0]
check(obs['id']=='B09-G-O01'and not obs['canonical_finding_added']and not obs['formal_edit']and not obs['report_edit'],'observation','historical report error not new adjudication')
for k in ['source_report','source_machine_disposition']:
    v=obs[k];check(content(v['commit'],v['path'])==content(A,v['path']),'observation','wrong historical report preserved '+k)
errp=Q+'affected-B05-integration-review-1/B09-G-O01-successor-erratum.md'
err=content(B05,errp).decode();check(A in err and '盒A=Y、留队B=空'in err and '一次正常终局还原后'in err,'observation','exact same-actual B05 successor erratum context')
check(git('rev-list','--parents','-n','1',B05).decode().split()==[B05,A],'observation','B05 actual report distinct single child of same actual')
for eventname in ['reference-reading-events.jsonl','project-reading-events.jsonl']:
    for line in (T/eventname).read_text().splitlines():
        e=json.loads(line);data=content(e['commit'],e['path'])
        check(sha(data)==e['sha256']and len(data)==e['bytes']and 1<=e['start']<=e['end']<=len(data.decode().splitlines()),'own-read','fresh exact range '+e['path']+':'+str(e['start']))
write('formal14-identities.json',formal_pairs);write('B04-current-preserved13.json',b04);write('public10-audit.json',public_audit);write('complete-control-bindings.json',controls)
write('actual-identity-audit.json',dict(at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),actual=A,candidate=C,baseline=B,method=__doc__,checks=len(checks),passed=sum(x['passed']for x in checks),failed=sum(not x['passed']for x in checks),results=checks,identity_bindings=bindings))
print(json.dumps(dict(checks=len(checks),passed=sum(x['passed']for x in checks),failed=[x for x in checks if not x['passed']],cached_files=len(cache)),ensure_ascii=False))
if any(not x['passed']for x in checks):raise SystemExit(1)
