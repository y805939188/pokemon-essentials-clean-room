"""Check immutable patch, fourteen original vectors, old controls and new links."""
from pathlib import Path,PurePosixPath
import json,subprocess,difflib,hashlib,datetime,posixpath,re
from run_logged import identity
W=Path('/workspace/r7-ir-R7-U13');T=Path(__file__).parent;B='e646432c644dec04d306842cc5a559a29c718fbc';MI='45c80832a41c1b56dcd7e9d93497758cbb7721de'
def git(*a):return subprocess.check_output(['git','-C',str(W/'checkout'),*a])
def js(p):return json.loads(p.read_bytes())
J=js(W/'actual-input/integration/applied-clauses.json');out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':[],'links':[],'qualification':'TOOL_VALIDATION only; documentary judgment is in report/per-ID'}
patch=''
for f in J['files']:
    p=f['path'];a=git('show',B+':'+p).decode() if f['baseline_identity']['bytes'] else '';b=git('show',MI+':'+p).decode()
    patch+=''.join(difflib.unified_diff(a.splitlines(keepends=True),b.splitlines(keepends=True),fromfile='a/'+p,tofile='b/'+p))
assert patch.encode()==(W/'actual-input/integration/actual-changes.patch').read_bytes()
out['patch']={'independent_full_patch_exact':True,'paths':24,'identity':identity(patch.encode())}
author=js(W/'actual-input/candidate/candidates/R7-U13/evidence/author/per-id.json')['records'][0]
review=js(W/'actual-input/candidate-review/candidates/R7-U13/evidence/reviewer/r1/per-id.json')['records'][0]
counter=js(W/'original/evidence/tasks/R7-C13/inputs/evidence/received-final-proposals/GR7-D07-001/counter-review.json')['findings'][0]
proposal=js(W/'supplemental/tasks/R7-D07/findings.json')['findings'][0]
for v in counter['regression_vectors']+proposal['regression_vectors']:
    for who,vs in [('author',author['vectors']),('candidate-reviewer',review['vectors'])]:
        row=next(x for x in vs if x['id']==v['id'])
        for k in ['id','input','expected','execution']:assert row[k]==v[k],(who,k,v['id'])
    out['checks'].append({'id':v['id'],'original_input_expected_execution_exact':True})
wp='deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md'
old=git('show',B+':'+wp).decode();new=git('show',MI+':'+wp).decode()
section=lambda s,n:s[s.index('## '+n+'.'):s.index('## '+str(int(n)+1)+'.')] if n!='11' else s[s.index('## 11.'):]
out['old_controls']={}
for n in ['6','11']:
    assert section(old,n)==section(new,n);out['old_controls']['WP15_section'+n+'_exact']=identity(section(new,n).encode())
eng='deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md'
a=git('show',B+':'+eng).decode().splitlines(keepends=True);b=git('show',MI+':'+eng).decode().splitlines(keepends=True)
rows=[l for l in a if re.match(r'\| B04-R\d+ \|',l)];assert len(rows)==28
assert rows==[l for l in b if re.match(r'\| B04-R\d+ \|',l)]
out['old_controls']['B04_R01_R28_exact_ordered_rows']=28
assert sum(l.startswith('| GR7-D07-001-S01 |') for l in b)==1
out['old_controls']['new_S01_unique']=True
mat='planning/feature-matrix.md';a=git('show',B+':'+mat).decode().splitlines();b=git('show',MI+':'+mat).decode().splitlines()
assert next(l for l in a if l.startswith('| F05-01 |'))==next(l for l in b if l.startswith('| F05-01 |'))
out['old_controls']['F05_01_exact']=True
# All newly introduced local Markdown links in own/shared target contributions.
for f in J['files']:
    if f['path'] not in ['audit/source-traceability.md',mat,eng,wp]:continue
    texts=[h['added_text'] for h in f['hunks']]+[r.get('added_text','') for r in J['root_administrative_reception_adjustments'] if r['path']==f['path']]
    for text in texts:
        for dest in re.findall(r'\]\(([^)]+)\)',text):
            if '://' in dest or dest.startswith('#'):continue
            path,_,fragment=dest.partition('#');target=posixpath.normpath(posixpath.join(posixpath.dirname(f['path']),path))
            content=git('show',MI+':'+target)
            if fragment:
                headings=[re.sub(r'[^\w\- ]','',h.lstrip('#').strip()).replace(' ','-').lower() for h in content.decode().splitlines() if h.startswith('#')]
                assert fragment in headings,(target,fragment)
            out['links'].append({'from':f['path'],'href':dest,'actual_MI_target':target,'target_identity':identity(content),'resolved_static':True,'browser_execution':False})
out['candidate_author_evidence_rule']={'batch':'R7-U13','commit':'5635c73ea14adc278961da0e3917c2d00d580a25','path':'candidates/R7-U13/evidence/author/per-id.json','exact_Git_blob_verified':True,'current_MI_path_assumption':False}
(T/'preservation-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'patch_exact':True,'original_vectors':14,'B04_original_rows':28,'new_S01_unique':True,'new_local_links_checked':len(out['links'])}))
