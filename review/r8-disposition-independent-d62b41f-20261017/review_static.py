#!/usr/bin/env python3
"""Independent document/Git checks; never writes candidate inputs."""
from pathlib import Path
import collections, copy, datetime, hashlib, importlib.util, json, re, shutil, subprocess, sys, unicodedata
sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SRC = ROOT / 'planning/implementation-routing/r8-20261017'
CANDIDATE = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
DELIVERY = '4575e80d041ab0c74a42e2e36399d05791dbaa5b'
BASE = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
FORMAL = 'deliverables/final-specification-set'
R8 = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
E = OUT / 'evidence'
E.mkdir(exist_ok=True)
def save(name, value):
    (E/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
def run(argv):
    p=subprocess.run(argv,cwd=ROOT,capture_output=True)
    rec={'argv':argv,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':p.returncode,'stdout':p.stdout.decode(errors='replace'),'stderr':p.stderr.decode(errors='replace')}
    with (E/'commands.jsonl').open('a') as fp:fp.write(json.dumps(rec,ensure_ascii=False)+'\n')
    return rec
def git(*args):
    r=run(['git',*args])
    if r['exit_code']:raise RuntimeError(r)
    return r['stdout']
def h(b):return hashlib.sha256(b).hexdigest()
def identity(commit,path):
    b=subprocess.check_output(['git','show',f'{commit}:{path}'],cwd=ROOT)
    return {'commit':commit,'path':path,'bytes':len(b),'sha256':h(b),'git_blob':git('rev-parse',f'{commit}:{path}').strip()}
def load(path):return json.loads(path.read_text())
m=load(SRC/'routing-manifest.json');cov=load(SRC/'section-coverage.json')
identities=[];identity_errors=[]
for entry in load(SRC/'candidate-file-manifest.json')['files']:
    path=entry['path'];actual=identity(CANDIDATE,path)
    actual['git_mode']=git('ls-tree',CANDIDATE,'--',path).split()[0]
    actual['worktree_equal']=h((ROOT/path).read_bytes())==actual['sha256']
    actual['matches_author_manifest']=all(actual[k]==entry[k] for k in ['bytes','sha256','git_blob','git_mode'])
    identities.append(actual)
    if not actual['matches_author_manifest'] or not actual['worktree_equal']:identity_errors.append(path)
save('candidate-identities.json',{'candidate':CANDIDATE,'entries':identities,'self_manifest':identity(CANDIDATE,'planning/implementation-routing/r8-20261017/candidate-file-manifest.json'),'errors':identity_errors})
paths=git('ls-tree','-r','--name-only',DELIVERY,'--',FORMAL).splitlines()
mdpaths=[p for p in paths if p.endswith('.md')]
index=load(ROOT/R8/'tasks/inventory_denominator/formal-inventory.json')
wp=load(ROOT/R8/'coverage/wp-final-coverage.json')
batch=load(ROOT/R8/'handoff/batch-assignment.json')
source_proof={s:git('rev-parse',f'{s}:{FORMAL}').strip() for s in [BASE,DELIVERY,CANDIDATE]}
save('isolation-and-scope.json',{'candidate':CANDIDATE,'formal_trees':source_proof,'delivery_to_candidate_diff':git('diff','--name-status',DELIVERY,CANDIDATE),'base_to_delivery_formal_diff':git('diff','--name-status',BASE,DELIVERY,'--',FORMAL),'all_formal_tree_paths':paths,'markdown_count':len(mdpaths),'non_markdown':sorted(set(paths)-set(mdpaths)),'source_index_equal':set(mdpaths)=={x['path'] for x in index},'manifest_equal':set(mdpaths)=={x['source']['path'] for x in m['documents']},'wp_plan_rows':len(wp['rows']),'raw_specs_markdown_count':len([x for x in git('ls-tree','-r','--name-only',BASE,'--','specs').splitlines() if x.endswith('.md')]),'remote_refs_before':run(['git','ls-remote','origin','refs/heads/main','refs/heads/codex/r8-disposition-tagging-20261017'])})
# A separately written lexer for the ATX/Setext/fence constructs actually present.
# Global slug collision handling, unlike the candidate's per-base counter.
def parse(text):
    lines=text.splitlines();out=[];fence=None;used=set()
    for i,line in enumerate(lines):
        f=re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$',line)
        if fence:
            if re.match(r'^ {0,3}'+re.escape(fence[0])+r'{'+str(fence[1])+r',}\s*$',line):fence=None
            continue
        if f:
            fence=(f[1][0],len(f[1]));continue
        atx=re.match(r'^ {0,3}(#{1,6})(?:[ \t]+(.*?)|[ \t]*)$',line)
        if atx:
            level=len(atx[1]);title=re.sub(r'[ \t]+#+[ \t]*$','',atx[2] or '').strip();start=i+1
        elif i and re.fullmatch(r' {0,3}(?:=+|-+)[ \t]*',line) and lines[i-1].strip() and not lines[i-1].lstrip().startswith(('#','|','>','-','*','`')):
            level=1 if '=' in line else 2;title=lines[i-1].strip();start=i
        else:continue
        title_clean=re.sub(r'<[^>]*>','',title)
        title_clean=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',title_clean).lower()
        slug=''.join(c for c in title_clean if c in ' -_' or unicodedata.category(c)[0] in 'LN').replace(' ','-')
        unique=slug;k=1
        while unique in used:unique=f'{slug}-{k}';k+=1
        used.add(unique)
        out.append({'line_start':start,'level':level,'title':title,'anchor':unique})
    for j,x in enumerate(out):x['line_end']=next((y['line_start']-1 for y in out[j+1:] if y['level']<=x['level']),len(lines))
    return out
all_sections=[];doc_proof=[];diff=[];ranges=[]
by_cov=collections.defaultdict(list)
for c in cov['sections']:by_cov[c['path']].append(c)
for path in mdpaths:
    b=(ROOT/path).read_bytes();hs=parse(b.decode());all_sections.extend({'path':path,**x} for x in hs)
    actual=[tuple(x[k] for k in ['line_start','level','title','anchor','line_end']) for x in hs]
    declared=[tuple(x[k] for k in ['line_start','level','title','anchor','line_end']) for x in by_cov[path]]
    if actual!=declared:diff.append({'path':path,'independent_only':[x for x in actual if x not in declared],'candidate_only':[x for x in declared if x not in actual]})
    doc_proof.append({'path':path,'bytes':len(b),'sha256':h(b),'lines':len(b.decode().splitlines()),'headings':len(hs),'role':next(d['document_role'] for d in m['documents'] if d['source']['path']==path)})
save('independent-heading-coverage.json',{'parser_scope':'ATX with indentation, Setext, matching fence length, global duplicate slug handling; local static parser, not remote GitHub rendering','documents':doc_proof,'headings':all_sections,'heading_count':len(all_sections),'levels':dict(collections.Counter(x['level'] for x in all_sections)),'differences':diff})
bindings=[]
for d in m['documents']:
    path=d['source']['path'];bs=[b for b in batch['batches'] if path in b['actual_target_write_set']]
    expect=sorted(b['id'] for b in bs);req=sorted({x for b in bs for x in b['required_ids']})
    fs=[f for f in m['features'] if f['document_id']==d['document_id']]
    bindings.append({'document_id':d['document_id'],'path':path,'expected_batches':expect,'expected_batch_wide_required_ids':req,'document_binding_equal':sorted(d['upstream']['batches'])==expect and sorted(d['upstream']['required_ids'])==req,'feature_ids':[f['feature_id'] for f in fs],'all_feature_bindings_equal':all(sorted(f['upstream']['batches'])==expect and sorted(f['upstream']['required_ids'])==req for f in fs),'all_gates_retained':all(f['current_applicability']['status']=='待整改后核对' and f['upstream']['status']=='待整改后核对' and not f['upstream']['accepted_events'] for f in fs) if bs else None})
save('batch-binding-check.json',{'bindings':bindings,'pending_rows':sum(bool(f['upstream']['batches']) for f in m['features']),'u07_write_set':next(b['actual_target_write_set'] for b in batch['batches'] if b['id']=='R8-U07'),'qualification':'document-wide conservative binding; does not assert every finding affects every row'})
for command in ['validate','check-generated']:
    run(['python',str(SRC.relative_to(ROOT)/'routing.py'),command])
run(['python',str(SRC.relative_to(ROOT)/'routing.py'),'assess-current','--commit',CANDIDATE])
# Load candidate without bytecode, redirect only mutating tool outputs into review evidence.
spec=importlib.util.spec_from_file_location('candidate_routing',SRC/'routing.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
sandbox=E/'tool-output';sandbox.mkdir(exist_ok=True)
shutil.copyfile(SRC/'routing-manifest.schema.json',sandbox/'routing-manifest.schema.json')
mod.HERE=sandbox
own=mod.self_test(m,cov);save('author-self-test-isolated.json',{'call':'routing.self_test(unmodified fixed candidate inputs), HERE redirected to review evidence/tool-output; ROOT unchanged','result':own})
mutations=[]
def check(name,fn):
    mm=copy.deepcopy(m);cc=copy.deepcopy(cov);fn(mm,cc)
    try:errors=mod.errors(mm,cc);mutations.append({'case':name,'rejected':bool(errors),'errors':errors[:8]})
    except Exception as exc:mutations.append({'case':name,'rejected':True,'exception':str(exc)})
check('missing name',lambda m,c:m['features'][0].pop('name'))
check('invalid source anchor',lambda m,c:m['features'][0]['source'].update(anchor='missing-anchor'))
check('unknown route',lambda m,c:m['features'][0]['future_plan'].update(destination='unknown'))
check('empty coverage mapping replaced by ALL_FORMAL_FEATURES',lambda m,c:c['sections'][60].update(feature_refs=[],coverage_scope='ALL_FORMAL_FEATURES'))
check('arbitrary existing but unrelated feature coverage',lambda m,c:c['sections'][60].update(feature_refs=[m['features'][-1]['feature_id']]))
check('stale coverage title level line_end',lambda m,c:c['sections'][60].update(title='wrong',level=6,line_end=999999))
check('false current feature snapshot and path',lambda m,c:m['features'][0]['current_applicability'].update(snapshot_commit='0'*40,document='missing.md'))
check('false declared source formal tree',lambda m,c:m['source_baseline'].update(formal_tree='0'*40))
check('false source git blob',lambda m,c:m['features'][0]['source'].update(file_git_blob='0'*40))
check('empty planned collaborators',lambda m,c:m['features'][0]['future_plan'].update(partners=[]))
check('drop known R8-U06 batch binding',lambda m,c:m['features'][0]['upstream'].update(batches=[],required_ids=[]))
check('invalid dependency WP',lambda m,c:m['features'][0]['dependencies'].update(wp_refs=['WP999']))
check('unbound accepted event bypasses gate',lambda m,c:(m['features'][0]['upstream'].update(accepted_events=['invented'],status='已校准'),m['features'][0]['current_applicability'].update(status='已校准')))
def arbitrary_verified(m,c):
    m['features'][0]['destination_verification'].update(status='已验证',evidence=[{'kind':'TARGET_BEHAVIOR_PROTOTYPE','ref':'not-an-evidence','target_commit':'0'*40,'scope':'all','result':'PASS'}])
check('invented target evidence structure',arbitrary_verified)
save('extended-validator-negatives.json',{'scope':'TOOL_VALIDATION; acceptance of semantic evidence is reported as a human gate, not proof that tool can authenticate it','cases':mutations})
save('root-read-ledger.json',{'full_semantic_read':['AGENTS.md',str((SRC/'README.md').relative_to(ROOT)),str((SRC/'review-prompt.md').relative_to(ROOT)),str((SRC/'routing.py').relative_to(ROOT)),str((SRC/'routing-manifest.schema.json').relative_to(ROOT)),str((SRC/'unresolved-boundaries.json').relative_to(ROOT)),str((SRC/'backfill-contract.json').relative_to(ROOT)),str((SRC/'accepted-source-updates.json').relative_to(ROOT)),str((SRC/'handoff.json').relative_to(ROOT)),str((SRC/'evidence/startup.json').relative_to(ROOT)),R8+'/DELIVERY.md',R8+'/inputs/review-SKILL.md',R8+'/handoff/cloud-eighth-update-handoff-prompt.md','deliverables/final-specification-set/test-catalog/README.md'],'machine_full_read':['candidate-file-manifest.json','routing-manifest.json','section-coverage.json','routing-policy.json','coverage-summary.json','validation-result.json','validator-negative-checks.json',R8+'/handoff/batch-assignment.json',R8+'/handoff/cloud-eighth-update-handoff-manifest.json'],'note':'Structured indexes were parsed in full; relevant batch IDs, contracts pointers and write sets semantically read. This ledger does not claim reading referenced Ruby/readset source units or remote historical evidence.'})
print(json.dumps({'identity_errors':identity_errors,'formal_documents':len(mdpaths),'independent_headings':len(all_sections),'heading_differences':diff,'pending_rows':sum(bool(f['upstream']['batches']) for f in m['features']),'extended_negative_rejected':sum(x['rejected'] for x in mutations),'extended_negative_total':len(mutations)},ensure_ascii=False,indent=2))
