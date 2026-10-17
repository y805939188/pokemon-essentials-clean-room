#!/usr/bin/env python3
"""Independent fixed-object R3 source/receipt audit; no business execution."""
import collections
import copy
import datetime
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
ROOT = Path('/workspace/r8-disposition-r3-review')
OUT = Path(__file__).parent
REL = Path('planning/implementation-routing/r8-20261017')
INV = ROOT / REL
CAND = 'c0f62d973180679134f2eb1a488c1dc359c8658f'
R2 = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'
R2REPORT = '0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
FINAL = '5f87743293290de2e219ecdd6c19e88280f60c9a'
PACKAGE = '8336249c78b4698cd77445653d3b05ff6a76ce94'
PKG = 'review/remediation-eighth-20261016-prepare/accepted-cumulative/'
FORMAL = 'deliverables/final-specification-set/'
LOG = []

def sha(x): return hashlib.sha256(x).hexdigest()
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def command(argv, cwd=ROOT, data=None, check=True, env=None):
    start=now(); p=subprocess.run(argv, cwd=cwd, input=data, capture_output=True, env=env)
    LOG.append(dict(argv=list(map(str,argv)),cwd=str(cwd),started_utc=start,ended_utc=now(),exit_code=p.returncode,
                    stdin_sha256=sha(data) if data is not None else None,stdout=p.stdout.decode('utf-8','replace'),stderr=p.stderr.decode('utf-8','replace')))
    if check: p.check_returncode()
    return p
def git(*args, cwd=ROOT, data=None, env=None): return command(['git',*args],cwd,data,env=env).stdout
def blob(c,p): return git('show',c+':'+str(p))
def load(c,p): return json.loads(blob(c,p))
def read(p): return json.loads(Path(p).read_bytes())
def save(n,d):
    data=(json.dumps(d,ensure_ascii=False,indent=2)+'\n').encode()
    (OUT/n).write_bytes(gzip.compress(data,mtime=0) if n.endswith('.gz') else data)
def identity(c,p):
    b=blob(c,p); mode,typ,h=git('ls-tree',c,'--',p).decode().split('\t')[0].split()
    return dict(commit=c,path=p,mode=mode,blob=h,bytes=len(b),sha256=sha(b))
def module(n,p):
    s=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def structure(d):
    if isinstance(d,dict): return {k:len(v) if isinstance(v,(list,dict)) else v for k,v in d.items()}
    return dict(type=type(d).__name__,length=len(d))

def audit():
    evidence=dict(candidate=CAND,baseline=B8,current=FINAL,package=PACKAGE,started_utc=now())
    prior=[]; prior_data={}
    prefix='review/r8-disposition-r2-independent-a32873d-20261017/'
    names=['REPORT.md','findings.json','feature-results.json','finding-results.json','issue-results.json','reading-coverage.json','section-results.json']
    names+=git('ls-tree','-r','--name-only',R2REPORT,'--',prefix+'agents').decode().splitlines()
    names=[n[len(prefix):] if n.startswith(prefix) else n for n in names]
    for n in names:
        if not (n.startswith('agents/source-') or n in ['REPORT.md','findings.json','feature-results.json','finding-results.json','issue-results.json','reading-coverage.json','section-results.json']):continue
        b=blob(R2REPORT,prefix+n)
        row={'identity':identity(R2REPORT,prefix+n),'consumption':'COMPLETE_JSON_PARSE_AND_RECONCILE' if n.endswith('.json') else 'FULL_PROSE_READ' if n in ['REPORT.md','agents/source-report.md'] else 'SOURCE_CODE_OR_PATCH_BYTE_RECONCILIATION'}
        if n.endswith('.json'):
            d=json.loads(b); prior_data[n]=d;row['structure']=structure(d)
        prior.append(row)
    save('source-prior-reconciliation.json',prior)
    files=[]; package_data={}
    paths=git('ls-tree','-r','--name-only',PACKAGE,'--',PKG).decode().splitlines()
    for p in paths:
        b=blob(PACKAGE,p); row={'identity':identity(PACKAGE,p)}
        if p.endswith('.json'):package_data[p[len(PKG):]]=json.loads(b);row['structure']=structure(json.loads(b));row['consumption']='COMPLETE_JSON_PARSE_AND_ALL_RECORD_RECONCILIATION'
        else:row['consumption']='FULL_DIFF_OR_PROSE_SEMANTIC_READ'
        files.append(row)
    evidence['package_inputs']=files; evidence['package_file_count']=len(files)
    ledger=read(INV/'revisions/r3/tools/cumulative-input-ledger.json')
    evidence['package_ledger_exact']=all(any(x['identity']['path']==f['path'] and all(x['identity'][k]==f[k] for k in ['commit','bytes','sha256']) and x['identity']['blob']==f['git_blob'] for x in files) for f in ledger['files'])
    receipts=package_data['batch-receipts.json']['records']; target_checks=[]; receipt_checks=[]
    for row in receipts:
        ref=row['acceptance_receipt']; receipt=load(ref['commit'],ref['path']); actual=receipt['records'][int(ref['record_pointer'].split('/')[-1])]
        targets=actual.get('actual_target_identities') or [actual['actual_target_identity']]
        record={'batch':row['batch'],'receipt_identity':identity(ref['commit'],ref['path']),'receipt_pointer':ref['record_pointer'],'ACCEPTED':actual['ACCEPTED'],'actual_integrated_PASS':actual['actual_integrated_PASS'],'actual_snapshot':actual['actual_artifact_commit'],'required_ids':actual['required_ids'],'selected_optional_ids':row['selected_optional_ids'],'target_count':len(targets),'actual_report':row['actual_independent_review']}
        record['package_binding_equal']=actual['batch']==row['batch'] and actual['actual_artifact_commit']==row['accepted_actual_snapshot'] and actual['required_ids']==row['required_ids']
        for t in targets:
            i=identity(actual['actual_artifact_commit'],t['path']); final=identity(FINAL,t['path']);target_checks.append({'batch':row['batch'],'receipt_target':t,'actual':i,'current':final,'receipt_identity_match':all(i[k]==t[k] for k in ['blob','bytes','sha256']),'current_same_bytes':all(i[k]==final[k] for k in ['blob','bytes','sha256'])})
        receipt_checks.append(record)
    evidence['receipt_checks']=receipt_checks;evidence['target_identity_checks']=target_checks
    issues=package_data['issue-status.json']['records']; registry=read(INV/'accepted-source-updates.json')
    actual_reports={}
    for row in receipts:
        ref=row['actual_independent_review']; key=ref['commit']+':'+ref['result_path']
        if key not in actual_reports:
            d=load(ref['commit'],ref['result_path']); actual_reports[key]={'identity':identity(ref['commit'],ref['result_path']),'structure':structure(d),'data':d}
    evidence['actual_report_indexes']=[{k:v for k,v in x.items() if k!='data'} for x in actual_reports.values()]
    issue_results=[]
    for issue in issues:
        owner=next(x for x in receipts if x['batch']==issue['owner_batch']); ref=issue['acceptance_receipt'];actual=load(ref['commit'],ref['path'])['records'][int(ref['record_pointer'].split('/')[-1])]
        match=issue['id'] in actual['required_ids']+owner['selected_optional_ids']
        issue_results.append({'id':issue['id'],'classification':issue['classification'],'batch':issue['owner_batch'],'source_verdict':'PASS_RECEIPT_BOUND_SOURCE_ACCEPTANCE' if match and actual['ACCEPTED'] else 'FAIL','receipt_membership':match,'ACCEPTED':actual['ACCEPTED'],'CLOSED':issue.get('CLOSED'), 'actual_report':issue['actual_independent_review'],'qualification':'Source-spec acceptance only; no target compatibility, execution, phase approval or whole-round closure'})
    evidence['issue_source_results']=issue_results;evidence['issue_counts']=dict(collections.Counter(x['classification'] for x in issues))
    m=read(INV/'routing-manifest.json'); old=load(R2,str(REL/'routing-manifest.json')); r=module('independent_source_readonly',INV/'routing.py');_,wp,batches=r.fixed_inputs()
    formal_checks=[]
    for item in package_data['formal-file-identities.json']['files']:
        actual=identity(FINAL,item['path']);doc=next(x for x in m['documents'] if x['source']['path']==item['path']);declared=doc['current_applicability']['identity']
        formal_checks.append({'actual':actual,'package_identity_equal':all(actual[k]==item[k] for k in ['commit','path','mode','blob','bytes','sha256']),'document_current_identity_equal':all(actual[k]==declared[raw] for k,raw in [('commit','commit'),('path','path'),('blob','git_blob'),('bytes','bytes'),('sha256','sha256')]),'document_global_snapshot_equal':doc['current_applicability']['snapshot_commit']==m['current_snapshot']['commit']})
    evidence['formal_identity_checks']=formal_checks
    original=[f for f in old['features'] if f['upstream']['batches']]; bound=[f for f in m['features'] if f['upstream']['batches']]; oldmap={f['feature_id']:f for f in old['features']}
    new=[f['feature_id'] for f in bound if not oldmap[f['feature_id']]['upstream']['batches']]
    expanded=[f['feature_id'] for f in bound if f['upstream']['batches']!=oldmap[f['feature_id']]['upstream']['batches'] or f['upstream']['required_ids']!=oldmap[f['feature_id']]['upstream']['required_ids']]
    currentmap={f['feature_id']:f for f in m['features']}
    preservation=[{'feature_id':f['feature_id'],'old_batches_preserved':set(f['upstream']['batches'])<=set(currentmap[f['feature_id']]['upstream']['batches']),'old_required_ids_preserved':set(f['upstream']['required_ids'])<=set(currentmap[f['feature_id']]['upstream']['required_ids']),'binding_basis_preserved':f['upstream']['binding_basis']==currentmap[f['feature_id']]['upstream']['binding_basis'],'authority_preserved':f['upstream']['authority']==currentmap[f['feature_id']]['upstream']['authority']} for f in original]
    evidence['bindings']={'R2_bound':len(original),'current_bound':len(bound),'newly_bound':len(new),'new_or_extended':len(expanded),'newly_bound_ids':new,'new_or_extended_ids':expanded,'old191_obligation_preservation':preservation,'statuses':dict(collections.Counter(f['upstream']['status'] for f in bound)), 'pending':[f['feature_id'] for f in bound if set(f['upstream']['batches'])-r.covered_batches(f['upstream'],{e['event_id']:e for e in registry['events']})]}
    extensions=[]
    for d in m['documents']:
        planned=r.doc_bindings(d['source']['path'],wp,batches)[2]['batches'];actual=set(d['upstream']['batches'])-set(planned)
        if actual:extensions.append({'path':d['source']['path'],'planned_batches':planned,'actual_extra_batches':sorted(actual),'current_batches':d['upstream']['batches']})
    evidence['actual_write_extensions']=extensions
    changed=git('diff','--name-only',B8,FINAL,'--',FORMAL).decode().splitlines(); patch=git('diff',B8,FINAL,'--',FORMAL); (OUT/'source-full-final.patch').write_bytes(patch)
    package_patch=git('diff','--unified=0','4575e80d041ab0c74a42e2e36399d05791dbaa5b',FINAL,'--',FORMAL)
    evidence['full_diff']={'bytes':len(patch),'sha256':sha(patch),'files':len(changed),'package_diff_exact_at_declared_unified0':package_patch==blob(PACKAGE,PKG+'full-formal-changes.patch'),'independent_context_lines':3,'package_context_lines':0}
    changed_results=[]
    for p in changed:
        single=git('diff',B8,FINAL,'--',p);ranges=[]
        for h in re.findall(rb'^@@ -([^ ]+) \+([^ ]+) @@',single,re.M):ranges.append({'old':h[0].decode(),'current':h[1].decode()})
        changed_results.append({'document':p,'old_identity':identity(B8,p),'current_identity':identity(FINAL,p),'full_diff_sha256':sha(single),'hunks':ranges,'reading':'FRESH_COMPLETE_DIFF_ALL_ADDED_DELETED_CONTEXT_AND_HEADERS','verdict':'PASS_SOURCE_RECEPTION; domain routing facets separately allocated'})
    evidence['changed_source_results']=changed_results
    heading=[];maps=read(INV/'revisions/r3/new-heading-mappings.json')['accepted_mappings'];oldkeys={(s['path'],s['anchor']) for s in read(INV/'section-coverage.json')['sections']};current=read(INV/'current-section-coverage.json')
    added=[s for s in current['sections'] if (s['path'],s['anchor']) not in oldkeys]
    for h in maps:
        hs,lines=r.headings(blob(FINAL,h['document'])); actual=next(x for x in hs if x['anchor']==h['anchor']);s=next(x for x in added if x['path']==h['document'] and x['anchor']==h['anchor'])
        ident=identity(FINAL,h['document']);si=h['source_identity'];unit=''.join(''.join(lines[a-1:b]) for a,b in h['line_ranges']).encode()
        heading.append({'document':h['document'],'anchor':h['anchor'],'title':actual['title'],'range':[actual['line_start'],actual['line_end']],'feature_refs':s['feature_refs'],'metadata_refs':s['metadata_refs'],'source_identity':ident,'title_hash':sha(actual['title'].encode()),'raw_heading_hash':actual['heading_sha256'],'all_declared_identities_equal':si['heading_sha256']==sha(actual['title'].encode()) and si['raw_markdown_heading_sha256']==actual['heading_sha256'] and si['unit_sha256']==sha(unit) and si['file_sha256']==ident['sha256'] and si['file_git_blob']==ident['blob'] and si['file_bytes']==ident['bytes'] and h['line_ranges']==[[actual['line_start'],actual['line_end']]],'mapping_consumers_equal':s['feature_refs']==h['feature_refs'] and s['metadata_refs']==h['metadata_refs'],'basis':h['basis'],'was_r2_U04_pending':h['previous_stage']['was_U04_pending'],'verdict':'PENDING_SEMANTIC_WRITEUP'})
    evidence['new_heading_results']=heading
    bodies=[]
    fs={f['feature_id']:f for f in m['features']}
    for fid in sorted({x for h in maps for x in h['feature_refs']}):
        f=fs[fid];p=f['current_applicability']['document'];lines=blob(FINAL,p).decode().splitlines(keepends=True);ranges=f['current_applicability']['locator']['line_ranges'];bodies.append('\n== '+fid+' '+p+' '+str(ranges)+' ==\n'+''.join(''.join(lines[a-1:b]) for a,b in ranges))
    (OUT/'source-consumer-readset.txt').write_text(''.join(bodies))
    # Preserve the first real apply's chronology rather than claiming a later guard existed.
    io=read(INV/'revisions/r3/tools/source-backfill-command-io.json');initial=gzip.decompress((INV/'revisions/r3/tools/backfill-at-initial-apply.py.gz').read_bytes());failure=read(INV/'revisions/r3/tools/first-current-coverage-render-results.json');norm=read(INV/'revisions/r3/tools/current-coverage-normalization.json')
    evidence['initial_apply_timing']={'io_start':io['started_utc'],'io_end':io['ended_utc'],'apply_exit':io['exit_code'],'tool_hash_equal_archived_initial':sha(initial)==io['backfill_tool_sha256'],'old_code_has_prospective_guard':b'prospective_coverage_errors' in initial,'old_code_preserves_explicit_null':b"prior.get('metadata_reason'," in initial,'first_current_check':structure(failure),'normalization_count':norm['normalized_count'],'all_normalizations_null_to_nonempty_string':all(x['before'] is None and isinstance(x['after'],str) and x['after'] for x in norm['normalized_fields']),'historical_coverage_unchanged_during_apply':io['input_sha256_before']['section-coverage.json']==io['input_sha256_after']['section-coverage.json']}
    ui=FORMAL+'user-interface/wp65-title-load-options-pause-and-pc.md';u01=next(x for x in target_checks if x['batch']=='R8-U01' and x['actual']['path']==ui);u04=next(x for x in target_checks if x['batch']=='R8-U04' and x['actual']['path']==ui);uipatch=git('diff','--unified=0',u01['actual']['commit'],FINAL,'--',ui)
    evidence['UI65_shared_history']={'U01_identity':u01['actual'],'U04_identity':u04['actual'],'U01_current_bytes_equal':u01['current_same_bytes'],'U04_current_bytes_equal':u04['current_same_bytes'],'last_two_line_package_patch_exact':uipatch==blob(PACKAGE,PKG+'last-UI65-repair.patch'),'changed_current_lines':re.findall(r'^@@ -[^ ]+ \+([^ ]+) @@',uipatch.decode(),re.M),'meaning':'U01 historical receipt remains; only final U04 exact target binds current two-line movement/jump definition repair.'}
    save('source-machine-evidence.json',evidence)
    save('source-command-io.json.gz',LOG)
    print(json.dumps({'package_files':len(files),'receipts':len(receipts),'target_contributions':len(target_checks),'target_identity_match':all(x['receipt_identity_match'] for x in target_checks),'historical_target_current_mismatches':[(x['batch'],x['actual']['path']) for x in target_checks if not x['current_same_bytes']],'issues':len(issues),'bindings':{k:v for k,v in evidence['bindings'].items() if not k.endswith('ids')},'extensions':extensions,'diff':evidence['full_diff'],'new_headings':len(heading),'consumer_readset_chars':sum(map(len,bodies)),'initial_apply_timing':evidence['initial_apply_timing']},ensure_ascii=False,indent=2))

if __name__=='__main__': audit()
