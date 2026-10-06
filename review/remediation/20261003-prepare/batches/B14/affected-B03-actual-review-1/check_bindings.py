"""Independent document/hash/diff checks; no historical programs executed."""
import csv, io, json, re, subprocess, hashlib
from read_bookkeeping import *
C3='c06db6cd964188b3c693a9b7820e3a8aaffe0b04'
C2='af39efbf32549be964cb083bd49bed6d1d5c0d2a'
BASE='review/remediation/20261003-prepare/batches/B14/integration-stage-1/'
def obj(n):return json.loads(blob(ACT,BASE+n))
def actual_id(c,p):
    b=blob(c,p);return identity(c,p,b)
def compare(c,p,row):
    a=actual_id(c,p)
    return {k:[row[k],a['blob' if k=='git_blob' else k]] for k in ['git_blob','sha256','bytes'] if k in row and row[k]!=a['blob' if k=='git_blob' else k]}
res={'reviewed_ACT':ACT,'behavior_proof':False,'failures':[]}
res['ACT_object']=subprocess.check_output(['git','show','--no-patch','--format=%H%n%T%n%P',ACT]).decode().splitlines()
copies=obj('copy-identities.json')['files'];copied=[]
for r in copies:
    p=r['path'];c=r['commit'];err=compare(c,p,r);err2=compare(ACT,p,r)
    copied.append({'path':p,'source_commit':c,'role':r['binding'],'source_mismatch':err,'ACT_mismatch':err2})
res['exact_copies']=copied
man=obj('integration-manifest.json');bound=obj('boundary-and-bindings.json')
expected=set(x['path'] if isinstance(x,dict) else x for x in man['copied_paths']+man['public_successor_paths']+man['bounded_new_record_paths'])
changed=set(subprocess.check_output(['git','diff','--no-ext-diff','--no-textconv','--no-renames','--name-only',PRE,ACT,'--']).decode().splitlines())
res['scope']={'expected':len(expected),'changed':len(changed),'unexpected':sorted(changed-expected),'missing':sorted(expected-changed),'complete_changed_paths':sorted(changed)}
res['hash_table']=[]
for r in csv.DictReader(io.StringIO(blob(ACT,BASE+'current-hashes.tsv').decode()),delimiter='\t'):
    r['bytes']=int(r['bytes']);c=ORIG if r['binding']=='IMMUTABLE_ORIGINAL_REPORT_HISTORICAL_INPUT_NOT_CURRENT_TREE' else ACT
    try:err=compare(c,r['path'],r)
    except subprocess.CalledProcessError:err={'unavailable':True}
    res['hash_table'].append({'path':r['path'],'binding':r['binding'],'commit':c,'mismatch':err})
readers=obj('current-readers.json');res['planned_reads']=[]
for r in readers['planned']:
    a=r['current'];c=a.get('commit') or (ORIG if 'ORIGINAL' in a.get('binding','') and 'INTENDED' not in a.get('binding','') else ACT)
    res['planned_reads'].append({'index':r['planned_index'],'path':r['path'],'current_commit':c,'current_mismatch':compare(c,r['path'],a),'before_mismatch':compare(r['before'].get('commit',PRE),r['path'],r['before']),'changed_assertion':r['changed']})
res['public_tables']=[]
for p in ['review/remediation/20261003-prepare/approval-ledger.tsv','review/remediation/20261003-prepare/traceability-successor.tsv']:
    old=blob(PRE,p).splitlines(keepends=True);new=blob(ACT,p).splitlines(keepends=True);rows=list(csv.DictReader(io.StringIO(blob(ACT,p).decode()),delimiter='\t'))
    res['public_tables'].append({'path':p,'same_schema':old[0]==new[0],'old170_exact_prefix':old==new[:len(old)],'old_records':len(old)-1,'new_records':len(new)-1,'appended_records':len(new)-len(old),'appended_IDs':[r['finding_id'] for r in rows[len(old)-1:]],'appended_rows':rows[len(old)-1:]})
res['catalogs']=[]
def rows(c,p):return [l for l in blob(c,p).splitlines(keepends=True) if re.match(rb'\|\s*(?:[A-Z]{2}\d+|B04-R\d+)\s*\|',l)]
for p in ['deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md','deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md']:
    prior=rows(C2,p);now=rows(ACT,p);old=rows(PRE,p)
    protected=[x for x in old if re.match(rb'\| (MP|MV|EV|IM|MR|DG|FW)\d+ \|',x)]
    res['catalogs'].append({'path':p,'C2_rows':len(prior),'ACT_rows':len(now),'old_rows_preserved_in_exact_order':all(x in now for x in prior) and [x for x in now if x in prior]==prior,'prior_rows_sha256':hashlib.sha256(b''.join(prior)).hexdigest(),'appended_rows':[x.decode().rstrip('\r\n') for x in now if x not in prior],'protected_B03_rows':len(protected),'protected_B03_same_bytes_order_multiplicity':[x for x in now if re.match(rb'\| (MP|MV|EV|IM|MR|DG|FW)\d+ \|',x)]==protected,'whole_C2_identical':blob(C2,p)==blob(ACT,p)})
res['original_control_reuse']=[]
orig=json.loads(blob(ORIG,'review/global-independent-review/2026-10-03-fd82a639/findings.json'));orig={x['id']:x for x in orig};acc=json.loads(blob(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json'))
for r in obj('finding-registration.json')['dispositions']:
    i=r['id'];bad=[k for k,v in r['complete_current_control_fields'].items() if orig[i].get(k,acc[i].get(k))!=v];res['original_control_reuse'].append({'record_key':r['record_key'],'id':i,'primary':r['primary'],'pending':r['status']=='INTEGRATED_PENDING_ACTUAL' and not r['accepted_B14_contribution'],'original_selector_matches':orig[i]==json.loads(blob(ORIG,r['original']['path']))[int(r['original']['selector'][1:])],'current_fields_equal':not bad,'mismatch_keys':bad,'current_control_keys':list(r['complete_current_control_fields'])})
save('mechanical-verification.json',res)
print('ACT',res['ACT_object']);print('copy mismatches',[(x['path'],x['source_mismatch'],x['ACT_mismatch']) for x in copied if x['source_mismatch'] or x['ACT_mismatch']]);print('scope',res['scope']['expected'],res['scope']['changed'],res['scope']['unexpected'],res['scope']['missing']);print('hash mismatches',[x for x in res['hash_table'] if x['mismatch']]);print('planned mismatches',[x for x in res['planned_reads'] if x['current_mismatch'] or x['before_mismatch']]);print('tables',[{k:v for k,v in r.items() if k not in ['appended_rows']} for r in res['public_tables']]);print('catalogs',res['catalogs']);print('control failures',[x for x in res['original_control_reuse'] if not x['pending'] or not x['original_selector_matches'] or not x['current_fields_equal']])
