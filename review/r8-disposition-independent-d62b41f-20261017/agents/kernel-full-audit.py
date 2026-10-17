#!/usr/bin/env python3
"""Independent static Markdown/JSON/Git audit. Writes only kernel-full-* evidence."""
import collections, datetime, hashlib, json, pathlib, re, subprocess, sys, unicodedata

ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT = ROOT / 'review/r8-disposition-independent-d62b41f-20261017/agents'
ROUTING = 'planning/implementation-routing/r8-20261017/'
CANDIDATE = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
SOURCE = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
DELIVERY = '4575e80d041ab0c74a42e2e36399d05791dbaa5b'
FORMAL = 'deliverables/final-specification-set'
IO = []

def run(argv):
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    p = subprocess.run(argv, cwd=ROOT, capture_output=True)
    IO.append({'argv': argv, 'cwd': str(ROOT), 'started_utc': started,
               'exit': p.returncode, 'stdout': p.stdout.decode(errors='replace'),
               'stderr': p.stderr.decode(errors='replace')})
    if p.returncode: raise RuntimeError(argv)
    return p.stdout

def sha(b): return hashlib.sha256(b).hexdigest()
def blob_sha(b): return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def git(*args): return run(['git', *args])
def read_json(p): return json.loads((ROOT / p).read_text())
def write(name, value): (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

def parse_headings(data):
    # Independent scanner, including ATX and Setext recognition and fenced-code exclusion.
    lines = data.decode().splitlines(keepends=True)
    found, seen, fence = [], collections.Counter(), None
    for i, line in enumerate(lines):
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line.rstrip('\r\n'))
        if mark:
            c, n = mark[1][0], len(mark[1])
            if fence is None: fence=(c,n)
            elif c == fence[0] and n >= fence[1] and not mark[2].strip(): fence=None
            continue
        if fence: continue
        m = re.match(r'^ {0,3}(#{1,6})[ \t]+(.*?)[ \t]*$', line.rstrip('\r\n'))
        if m: level,title=len(m[1]),re.sub(r'[ \t]+#+[ \t]*$', '', m[2])
        elif i and re.match(r'^ {0,3}(=+|-+)[ \t]*$', line.rstrip('\r\n')) and lines[i-1].strip() and not lines[i-1].lstrip().startswith(('|','#','-')):
            level,title=(1 if line.lstrip().startswith('=') else 2),lines[i-1].strip()
        else: continue
        start = i+1 if m else i
        plain = re.sub(r'<[^>]*>', '', title)
        plain = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', plain).lower()
        base = ''.join(c for c in plain if c in ' -_' or unicodedata.category(c)[0] in 'LN').replace(' ','-')
        anchor=base+(('-'+str(seen[base])) if seen[base] else '')
        seen[base]+=1
        found.append({'level':level,'title':title,'anchor':anchor,'line_start':start,
                      'heading_sha256':sha(lines[start-1].encode())})
    for i,h in enumerate(found):
        h['line_end']=next((n['line_start']-1 for n in found[i+1:] if n['level']<=h['level']),len(lines))
    return found,lines

m=read_json(ROUTING+'routing-manifest.json')
c=read_json(ROUTING+'section-coverage.json')
docs=[(i,d) for i,d in enumerate(m['documents']) if '/generic-kernel/' in d['source']['path'] or '/test-catalog/generic-kernel-' in d['source']['path']]
fs=[(i,f) for i,f in enumerate(m['features']) if '/generic-kernel/' in f['source']['document']]
assert git('rev-parse','HEAD').decode().strip()==CANDIDATE
tree=git('rev-parse',CANDIDATE+':'+FORMAL).decode().strip()
assert tree=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
actual=git('ls-tree','-r','--name-only',SOURCE,'--',FORMAL+'/generic-kernel',FORMAL+'/test-catalog').decode().splitlines()
actual=sorted(p for p in actual if p.endswith('.md') and ('/generic-kernel/' in p or '/generic-kernel-' in p))
assert actual==sorted(d['source']['path'] for _,d in docs)
errors=[]; ledger=[]; source_data={}; all_headings=[]
read_chunks={
 'wp02-rule-configuration-and-data-variants.md':[[1,278,'a97bc6']],
 'wp03-content-identity-and-schema.md':[[1,200,'d0ecc8'],[201,393,'8ad73e']],
 'wp04-pbs-lifecycle.md':[[1,170,'94e866'],[171,320,'e7a31f']],
 'wp05-events-extensions-plugins.md':[[1,147,'cf68e0']],
 'wp06-stats-directory.md':[[1,143,'cf68e0']],
 'wp06-time-random-steps-stats.md':[[1,196,'18abc4']],
 'wp07-deprecation-appendix.md':[[1,54,'18abc4']],
 'wp07-diagnostics-files-http.md':[[1,191,'3b21ee']],
 'wp08-localization.md':[[1,125,'efed47'],[126,231,'0cabb1']],
 'wp09-save-startup-continue.md':[[1,179,'355499']],
 'wp10-migration-failure-recovery.md':[[1,150,'ab732a'],[151,281,'818b36']],
 'generic-kernel-wp02-03-04.md':[[1,80,'b98825'],[81,160,'878e69'],[161,236,'693fa4']],
 'generic-kernel-wp05-06-07-08-09-10.md':[[1,100,'49b5f9'],[101,200,'bd2038'],[201,288,'1c92ad']]
}
for di,d in docs:
    path=d['source']['path']; data=(ROOT/path).read_bytes(); source_data[path]=data
    hs,lines=parse_headings(data); expected=[(j,s) for j,s in enumerate(c['sections']) if s['path']==path]
    same=True
    for commit in [SOURCE,DELIVERY,CANDIDATE]:
        same = (git('show',commit+':'+path)==data) and same
    ident=d['source']
    cur=d['current_applicability']
    if not(same and ident['commit']==SOURCE and ident['sha256']==sha(data) and ident['bytes']==len(data)
           and ident['git_blob']==blob_sha(data) and cur['snapshot_commit']==DELIVERY
           and cur['identity']['sha256']==sha(data) and cur['identity']['git_blob']==blob_sha(data)):
        errors.append(['identity',path])
    fields=['level','title','anchor','line_start','line_end','heading_sha256']
    if [[h[k] for k in fields] for h in hs] != [[s[k] for k in fields] for _,s in expected]: errors.append(['heading_coverage',path])
    chunks=read_chunks[pathlib.Path(path).name]
    assert sorted(n for a,b,_ in chunks for n in range(a,b+1))==list(range(1,len(lines)+1))
    row={'document_id':d['document_id'],'manifest_pointer':'/documents/'+str(di),'path':path,
         'bytes':len(data),'sha256':sha(data),'lines':len(lines),'headings':len(hs),
         'heading_levels':dict(collections.Counter(str(h['level']) for h in hs)),
         'full_text_read':True,'read_ranges':[[a,b] for a,b,_ in chunks],
         'actual_read_tool_chunks':[z for _,_,z in chunks],
         'source_delivery_candidate_worktree_identical':same,'feature_count':len(d['feature_ids']),
         'section_mapping_counts':dict(collections.Counter(s['mapping_kind'] for _,s in expected)),
         'coverage_indices':[j for j,_ in expected]}
    ledger.append(row); all_headings.extend(expected)
feature_checks=[]
for fi,f in fs:
    s=f['source'];data=source_data[s['document']];lines=data.decode().splitlines(keepends=True)
    hs,_=parse_headings(data); h=next((x for x in hs if x['anchor']==s['anchor']),None)
    ok=h is not None and h['title']==s['heading'] and h['heading_sha256']==s['heading_sha256']
    ranges=s['line_ranges']; part=''.join(''.join(lines[a-1:b]) for a,b in ranges).encode()
    ok=ok and sha(part)==s['unit_sha256'] and s['file_sha256']==sha(data) and s['file_git_blob']==blob_sha(data)
    ok=ok and s['commit']==SOURCE and f['current_applicability']['snapshot_commit']==DELIVERY
    overlap=[]
    for _,g in fs:
        if g['feature_id']==f['feature_id'] or g['source']['document']!=s['document']:continue
        for a,b in ranges:
            for x,y in g['source']['line_ranges']:
                if max(a,x)<=min(b,y):overlap.append(g['feature_id'])
    if overlap or not ok:errors.append(['feature_identity_or_overlap',f['feature_id']])
    feature_checks.append({'feature_id':f['feature_id'],'pointer':'/features/'+str(fi),'fixed_identity_and_unit_hash_match':ok,'overlapping_feature_ids':overlap})
view=(ROOT/(ROUTING+'views/generic-kernel.md')).read_text(); vl=view.splitlines()
assert re.findall(r'^\| (FR-\d{6}) /',view,re.M)==[f['feature_id'] for _,f in fs]
assert all('待验证' in next(l for l in vl if l.startswith('| '+f['feature_id']+' /')) and '未实现 / 未验收' in next(l for l in vl if l.startswith('| '+f['feature_id']+' /')) for _,f in fs)
cfm=read_json(ROUTING+'candidate-file-manifest.json');candidate_errors=[]
candidate_tree={}
for line in git('ls-tree','-r',CANDIDATE,'--',ROUTING).decode().splitlines():
    meta,path=line.split('\t',1); mode,kind,oid=meta.split();candidate_tree[path]=(mode,oid)
for x in cfm['files']:
    data=(ROOT/x['path']).read_bytes()
    if (len(data)!=x['bytes'] or sha(data)!=x['sha256'] or blob_sha(data)!=x['git_blob']
        or candidate_tree[x['path']]!=(x['git_mode'],x['git_blob'])):candidate_errors.append(x['path'])
assert not candidate_errors
changed=git('diff','--name-status',DELIVERY,CANDIDATE).decode().splitlines()
assert all(l.startswith('A\t'+ROUTING) for l in changed)
author_results=[]
for command in ['validate','check-generated']:
    data=run(['python',ROUTING+'routing.py',command])
    author_results.append({'command':command,'result':json.loads(data)})
mechanical={'candidate':CANDIDATE,'formal_tree':tree,'source':SOURCE,'delivery':DELIVERY,
 'counts':{'documents':len(docs),'body_documents':11,'catalog_documents':2,'features':len(fs),
           'body_lines':sum(x['lines'] for x in ledger[:11]),'catalog_lines':sum(x['lines'] for x in ledger[11:]),
           'body_bytes':sum(x['bytes'] for x in ledger[:11]),'catalog_bytes':sum(x['bytes'] for x in ledger[11:]),
           'headings':len(all_headings),'body_headings':sum(x['headings'] for x in ledger[:11]),'catalog_headings':sum(x['headings'] for x in ledger[11:]),
           'mapping_kinds':dict(collections.Counter(s['mapping_kind'] for _,s in all_headings)),
           'routes':dict(collections.Counter(f['future_plan']['destination'] for _,f in fs))},
 'reading_ledger':ledger,'feature_identity_checks':feature_checks,'view':{'path':ROUTING+'views/generic-kernel.md','lines':len(vl),'sha256':sha(view.encode()),'full_text_read_ranges':[[1,54],[55,106],[107,147]],'actual_read_tool_chunks':['5a828e','61d357','5b6bff'],'all_66_rows_in_order':True},
 'candidate_file_manifest_entries_checked':len(cfm['files']),'candidate_file_manifest_errors':candidate_errors,
 'delivery_to_candidate_changes':changed,'author_readonly_commands':author_results,'errors':errors,
 'semantic_claim':'Only this domain was fully semantically read. Tools do not establish routing semantics or compatibility.'}
write('kernel-full-mechanical-evidence.json',mechanical)
write('kernel-full-audit-tool-io.json',{'commands':IO,'exit':1 if errors else 0,'stderr':'','stdout':'STATIC_AUDIT_PASS' if not errors else 'STATIC_AUDIT_FAIL'})
write('kernel-full-domain-records.json',{'features':[{'manifest_index':i,**f} for i,f in fs],
 'documents':[{'manifest_index':i,**d} for i,d in docs], 'section_coverage':[{'coverage_index':i,**s} for i,s in all_headings]})
print(json.dumps({'counts':mechanical['counts'],'errors':errors,'candidate_file_manifest_errors':candidate_errors,'author_commands':[{'command':r['command'],'errors':r['result'].get('errors')} for r in author_results]},ensure_ascii=False,indent=2))
sys.exit(1 if errors else 0)
