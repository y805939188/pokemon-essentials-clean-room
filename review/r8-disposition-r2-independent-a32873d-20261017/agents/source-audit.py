#!/usr/bin/env python3
"""Independent static source/receipt audit. Writes only source-* review artifacts."""
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
REPO = Path('/workspace/r8-disposition-r2-review')
OUT = REPO / 'review/r8-disposition-r2-independent-a32873d-20261017/agents'
INV = REPO / 'planning/implementation-routing/r8-20261017'
CANDIDATE = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'
CURRENT = '908273093e1f6b27fc58249417675dd62d146224'
NEXT = '0eee6d141f33758eda34bd8ebad94a3e2b617f5a'

def git(*args, **kw):
    return subprocess.check_output(['git', *args], cwd=REPO, **kw)

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

def save(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

r = load_module('independent_source_routing', INV / 'routing.py')
b = load_module('independent_source_backfill', INV / 'revisions/r2/tools/backfill-accepted-sources.py')
m = json.loads((INV / 'routing-manifest.json').read_bytes())
old_cov = json.loads((INV / 'section-coverage.json').read_bytes())
reg = json.loads((INV / 'accepted-source-updates.json').read_bytes())
intake = json.loads((INV / 'revisions/r2/tools/accepted-receipt-intake.json').read_bytes())
reading = json.loads((INV / 'revisions/r2/accepted-source-reading.json').read_bytes())
pending = json.loads((INV / 'revisions/r2/accepted-u04-proposed-mappings.json').read_bytes())
identities = []
receipts = []
for commit, path in sorted({(e['receipt_commit'],e['receipt_path']) for e in intake['events']}):
    data = r.blob(commit,path)
    receipt = json.loads(data)
    receipts.append({'identity':r.identity(commit,path), 'receipt':receipt})
    for record in receipt['records']:
        for raw in record.get('actual_target_identities') or [record['actual_target_identity']]:
            actual = r.identity(record['actual_artifact_commit'], raw['path'])
            identities.append({'batch':record['batch'],'claimed':raw,'actual':actual,
                'match':all(actual[k] == raw[v] for k,v in [('git_blob','blob'),('sha256','sha256'),('bytes','bytes')]),
                'current_descendant_same_bytes':r.blob(NEXT,raw['path']) == r.blob(record['actual_artifact_commit'],raw['path'])})
all_keys = {}
for commit in [r.B8,CURRENT,NEXT]:
    all_keys[commit]=[(d['source']['path'],h['anchor']) for d in m['documents'] for h in r.headings(r.blob(commit,d['source']['path']))[0]]
added = set(all_keys[NEXT])-set(all_keys[r.B8])
removed = set(all_keys[r.B8])-set(all_keys[NEXT])
accepted = reading['new_heading_coverage']['accepted_mappings']
proposals = pending['mappings']
heading_results = []
for kind, rows in [('ACCEPTED_PROPOSAL_ONLY',accepted),('PENDING_U04_PROPOSAL_ONLY',proposals)]:
    for h in rows:
        data=r.blob(NEXT,h['document']);hs,lines=r.headings(data)
        real=next(x for x in hs if x['anchor']==h['anchor'])
        unit=''.join(lines[real['line_start']-1:real['line_end']]).encode()
        identity=h['actual_source_identity']
        match=(all(h[k]==real[k] for k in ['title','anchor','line_start','line_end','level']) and
            identity['file_sha256']==r.digest(data) and identity['file_git_blob']==r.identity(NEXT,h['document'])['git_blob'] and
            identity['heading_sha256']==r.digest(real['title'].encode()) and identity['section_sha256']==r.digest(unit))
        heading_results.append({'kind':kind,'document':h['document'],'anchor':h['anchor'],'identity_match':match,
            'title':h['title'],'ranges':[[real['line_start'],real['line_end']]],'feature_refs':h['feature_refs'],
            'metadata_refs':h['metadata_refs'],'basis':h.get('basis',h.get('consumer_basis')),
            'evidence_heading_hash_convention':'SHA256_TITLE_ONLY',
            'routing_locator_heading_hash_convention':'SHA256_RAW_MARKDOWN_LINE_WITH_NEWLINE',
            'raw_markdown_heading_sha256':real['heading_sha256']})
accepted_paths={x['actual']['path'] for x in identities}
changes=git('diff','--name-only',r.B8,NEXT,'--',r.FORMAL).decode().splitlines()
_,wp,batches=r.fixed_inputs()
extensions=[]
for row in identities:
    path=row['actual']['path']
    planned=r.doc_bindings(path,wp,batches)[2]['batches']
    if row['batch'] not in planned:
        extensions.append({'batch':row['batch'],'path':path,'planned_batches':planned})
diffs=[]
for start,end,name in [(CURRENT,'49a558f7d5498680ba88d532f3815e07d7844459','908-to-49'),('49a558f7d5498680ba88d532f3815e07d7844459',NEXT,'49-to-U06')]:
    raw=git('diff','--no-ext-diff','--unified=3',start,end,'--',r.FORMAL)
    declared=(INV / ('revisions/r2/accepted-source-evidence/'+name+'.patch')).read_bytes()
    diffs.append({'old':start,'new':end,'bytes':len(raw),'sha256':r.digest(raw),'lines':len(raw.splitlines()),'matches_author_evidence':raw==declared})
    (OUT / ('source-diff-'+name+'.patch')).write_bytes(raw)

# Minimal independently owned Git fixture: descendants add one unreceipted
# sentence to an already accepted file; all accepted receipt objects stay fixed.
fixture=Path('/tmp/r8-r2-source-fixture-a32873d.git')
fixture_commands=[]
if not fixture.exists():
    subprocess.run(['git','init','--bare',str(fixture)],check=True,capture_output=True)
    objects=git('rev-parse','--path-format=absolute','--git-common-dir').decode().strip()+'/objects'
    (fixture/'objects/info/alternates').write_text(objects+'\n')
def fg(*args, input=None, env=None):
    argv=['git','--git-dir='+str(fixture),*args]
    result=subprocess.run(argv,input=input,env=env,capture_output=True,check=True)
    fixture_commands.append({'argv':argv,'stdin_sha256':None if input is None else r.digest(input),
        'exit_code':result.returncode,'stdout_sha256':r.digest(result.stdout),'stderr':result.stderr.decode(),
        'stdout':result.stdout.decode() if len(result.stdout)<2000 else 'Large read-only blob; hash recorded'})
    return result.stdout
target='deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md'
before=r.blob(CURRENT,target)
lines=before.decode().splitlines(keepends=True)
assert '提示' not in lines[195]  # actual accepted U02 location
lines[195]=lines[195].rstrip('\n')+' [INDEPENDENT UNRECEIPTED STATIC FIXTURE CHANGE]\n'
after=''.join(lines).encode()
sha=fg('hash-object','-w','--stdin',input=after).decode().strip()
env=dict(os.environ,GIT_INDEX_FILE='/tmp/r8-r2-source-fixture-a32873d.index',GIT_AUTHOR_NAME='Independent static fixture',GIT_AUTHOR_EMAIL='review@example.invalid',GIT_COMMITTER_NAME='Independent static fixture',GIT_COMMITTER_EMAIL='review@example.invalid',GIT_AUTHOR_DATE='2026-10-17T16:00:00+00:00',GIT_COMMITTER_DATE='2026-10-17T16:00:00+00:00')
fg('read-tree',CURRENT,env=env)
fg('update-index','--add','--cacheinfo','100644',sha,target,env=env)
tree=fg('write-tree',env=env).decode().strip()
descendant=fg('commit-tree',tree,'-p',CURRENT,input=b'Independent unreceipted source fixture\n',env=env).decode().strip()
for mod in [r,b.r]:
    mod.git=lambda *args: fg(*args)
    mod.blob.cache_clear();mod.identity.cache_clear()
mm=copy.deepcopy(m)
mm['current_snapshot']['commit']=descendant
mm['current_snapshot']['formal_tree']=r.git('rev-parse',descendant+':'+r.FORMAL.rstrip('/')).decode().strip()
for d in mm['documents']:
    d['current_applicability']['snapshot_commit']=descendant
    d['current_applicability']['identity']=r.identity(descendant,d['source']['path'])
    if d['source']['path']==target:
        fs=[f for f in mm['features'] if f['document_id']==d['document_id']]
        _,locators,_=b.map_document(d,fs,descendant)
        for f in fs:f['current_applicability']['locator']=locators[f['feature_id']]
for f in mm['features']:f['current_applicability']['snapshot_commit']=descendant
probe_errors=r.errors(mm,old_cov,reg)
probe={'scope':'ISOLATED_STATIC_DOCUMENT_FIXTURE_ONLY','fixture_git':str(fixture),'parent':CURRENT,
    'snapshot':descendant,'changed_path':target,'accepted_event_commit':reg['events'][0]['commit'],
    'accepted_blob':r.identity(CURRENT,target)['git_blob'],'unaccepted_current_blob':sha,
    'new_receipt_supplied':False,'validator_errors':probe_errors,'validator_accepted_unreceipted_change':not probe_errors,
    'author_core_mutation':False,'author_apply_executed':False,
    'mutation':{'line':196,'old_line':before.decode().splitlines()[195],'new_line':lines[195].rstrip('\n'),
                'old_file_sha256':r.digest(before),'new_file_sha256':r.digest(after)},
    'function_invocation':'routing.errors(updated_actual_manifest, unchanged_historical_section_coverage, unchanged_U02_U03_registry)',
    'manifest_fixture_sha256':r.digest(json.dumps(mm,ensure_ascii=False,sort_keys=True).encode()),
    'routing_py_sha256':r.digest((INV/'routing.py').read_bytes()),
    'backfill_py_sha256':r.digest((INV/'revisions/r2/tools/backfill-accepted-sources.py').read_bytes())}
save('source-fixture-command-io.json',fixture_commands)
save('source-stale-receipt-probe.json',probe)
summary={'candidate':CANDIDATE,'current_snapshot':m['current_snapshot'],'current_events':reg['events'],
    'receipts':receipts,'target_identity_results':identities,'target_count':len(identities),
    'all_target_identities_match':all(x['match'] for x in identities),
    'all_accepted_target_bytes_preserved_in_0eee':all(x['current_descendant_same_bytes'] for x in identities),
    'receipt_batches':sorted(x['batch'] for x in identities),
    'heading_counts':{k:len(v) for k,v in all_keys.items()},'added_headings':sorted(added),'removed_headings':sorted(removed),
    'heading_results':heading_results,'heading_proposal_set_exact':added=={(h['document'],h['anchor']) for h in heading_results},
    'all_heading_identities_match':all(h['identity_match'] for h in heading_results),
    'changed_formal_paths':changes,'unaccepted_changed_paths':sorted(set(changes)-accepted_paths),'actual_write_set_extensions':extensions,
    'diff_checks':diffs,'probe':probe}
save('source-machine-evidence.json',summary)
print(json.dumps({k:v for k,v in summary.items() if k in ['target_count','all_target_identities_match','all_accepted_target_bytes_preserved_in_0eee','heading_counts','heading_proposal_set_exact','all_heading_identities_match','unaccepted_changed_paths','actual_write_set_extensions','diff_checks','probe']},ensure_ascii=False,indent=2))
