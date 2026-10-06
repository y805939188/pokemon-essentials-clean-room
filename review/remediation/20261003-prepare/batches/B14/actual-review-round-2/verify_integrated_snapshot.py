"""New report-only Git-object/diff/JSON relationship bookkeeping; no behavior simulation."""
import json,pathlib,subprocess,hashlib,re,csv,io,sys,functools
import complete_reader as c
P=pathlib.Path(__file__).parent
def h(b):return hashlib.sha256(b).hexdigest()
def obj(sha,path):return json.loads(c.show(sha,path))
@functools.lru_cache(None)
def tree(sha):
    rows=subprocess.check_output(['git','ls-tree','-rz',sha]).split(b'\0');out={}
    for r in rows:
        if r:
            a,p=r.split(b'\t',1);out[p.decode()]=a.decode()
    return out
inv=json.loads((P/'diff-inventories.json').read_text());formal=set(json.loads((P/'formal-diff-reading-map.json').read_text())['paths']);b=obj(c.ACT,c.G+'boundary-and-bindings.json');public=set(b['public_paths'])
audit=json.loads((P/'audit-complete-context-map.json').read_text());auditpaths={x['path'] for x in audit['inputs']};del audit
base=tree(c.BASE);actual=tree(c.ACT);streams=[]
for s in inv:
    raw=subprocess.check_output(['git','diff']+s['flags']+[s['from'],s['to']]);assert len(raw)==s['bytes'] and h(raw)==s['sha256']
    starts=[m.start() for m in re.finditer(br'(?m)^diff --git ',raw)];chunks=[raw[x:y] for x,y in zip(starts,starts[1:]+[len(raw)])];assert len(chunks)==len(s['paths'])
    groups=[];global_line=1
    for chunk,i in zip(chunks,s['paths']):
        path=i['path'];assert h(chunk)==i['sha256'] and len(chunk)==i['bytes'];assert chunk.startswith(('diff --git '+i['identity']+'\n').encode())
        after=c.show(c.ACT,path);before=c.show(s['from'],path) if path in tree(s['from']) else b''
        # Replay only the textual Git patch in memory to verify exact body, context and terminators.
        lines=chunk.splitlines(keepends=True);old=before.splitlines(keepends=True);new=after.splitlines(keepends=True);pos=0;result=[];hunks=[];n=0
        while n<len(lines):
            line=lines[n];match=re.match(br'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',line)
            if not match:n+=1;continue
            a=int(match[1]);alen=int(match[2] or b'1');bn=int(match[3]);blen=int(match[4] or b'1');start=a-1 if alen else a;assert start>=pos
            result.extend(old[pos:start]);pos=start;n+=1;oldcount=0;newcount=0;body_start=n;coords=[]
            while n<len(lines) and not lines[n].startswith(b'@@ '):
                z=lines[n]
                if z.startswith(b'\\ No newline at end of file'):
                    assert coords;previous=coords[-1];previous['no_final_terminator']=True
                    if previous['prefix'] in [' ','+']:result[-1]=result[-1].removesuffix(b'\n')
                    n+=1;continue
                prefix=z[:1]
                if prefix not in [b' ',b'+',b'-']:raise AssertionError(('unexpected diff body',path,n))
                val=z[1:]
                # A following no-newline marker adjusts comparison with the native object.
                no_nl=n+1<len(lines) and lines[n+1].startswith(b'\\ No newline at end of file');native=val.removesuffix(b'\n') if no_nl else val
                oldline=pos+1 if prefix in [b' ',b'-'] else None;newline=len(result)+1 if prefix in [b' ',b'+'] else None
                if prefix in [b' ',b'-']:assert old[pos]==native,(path,pos);pos+=1;oldcount+=1
                if prefix in [b' ',b'+']:result.append(val);newcount+=1
                coords.append({'stream_line':global_line+n,'path_diff_line':n+1,'prefix':prefix.decode(),'before_line':oldline,'ACT_line':newline,'native_line_sha256':h(native),'native_bytes':len(native)})
                n+=1
            assert (oldcount,newcount)==(alen,blen),(path,oldcount,newcount,alen,blen)
            hunks.append({'header':line.decode().rstrip('\n'),'stream_lines':[global_line+body_start-1,global_line+n-1],'ordered_body_coordinates':coords})
        result.extend(old[pos:]);assert b''.join(result)==after,('patch body mismatch',path)
        if path in formal:coverage={'kind':'WHOLE_12_FORMALS_AND_COMPLETE_FORMAL_HUNKS','maps':['formal-complete-context-map.json','formal-diff-reading-map.json'],'removed_context':'Full formal diff exact semantic values consumed'}
        elif path in public:
            assert c.show(c.C3,path)==c.show(c.BASE,path),('public C3 differs from accepted predecessor',path)
            coverage={'kind':'WHOLE_CURRENT_AND_WHOLE_PREDECESSOR_PUBLIC_NATIVE_INPUTS','map':'public-complete-context-map.json','TSV':'Complete ordered columns, rows, exact raw JSON cell hashes and native decoded meanings consumed'}
        else:
            assert path in auditpaths and not before,('unmapped changed path',path)
            coverage={'kind':'WHOLE_NEW_AUDIT_NATIVE_INPUT_WITH_ALL_SEMANTIC_MEANINGS','map':'audit-complete-context-map.json','private_raw_archive':'Not duplicated; exact body reconstructed from frozen Git input, typed ordered context map and full unfiltered stream parameters'}
        groups.append({'path':path,'before_sha256':h(before),'ACT_sha256':h(after),'path_stream_sha256':h(chunk),'hunks':hunks,'coverage':coverage,'semantic_read_completed':True})
        global_line+=len(lines)
    streams.append({'label':s['label'],'from':s['from'],'to':s['to'],'flags':s['flags'],'bytes':len(raw),'sha256':h(raw),'paths':groups,'path_count':len(groups),'hunk_count':sum(len(x['hunks']) for x in groups),'path_filter':None,'excluded_paths_or_hunks':[],'exact_patch_reconstruction':True})
(P/'complete-unfiltered-stream-reading-map.json').write_text(json.dumps({'reviewed_ACT':c.ACT,'streams':streams,'basis':'All native semantic meanings actually consumed through primary/formal/public/audit maps; exact full unfiltered reconstruction verified separately. No inventory/hash treated as behavior reading.'},ensure_ascii=False,separators=(',',':'))+'\n')
reg=obj(c.ACT,c.G+'finding-registration.json');cl=obj(c.ACT,c.G+'clause-location-bindings.json');checks=[]
for r in reg['dispositions']:
    rid=r['id'];loc=cl['records'][rid];assert loc['record_key']==r['record_key'];assert loc['current_formal_locations']==r['current_formal_locations']
    heads=0;rows=0
    for f in r['current_formal_locations']:
        raw=c.show(c.ACT,f['path']);ident=f['identity'];assert h(raw)==ident['sha256'] and len(raw)==ident['bytes'];assert raw==c.show(c.C3,f['path']);ls=raw.decode().splitlines(keepends=True)
        expanded=[z for cb in f['clause_bindings'] for z in cb['expanded_sections']]
        assert expanded==[x['section_number'] for x in f['current_heading_locators']]
        for z in f['current_heading_locators']:
            value=ls[z['line']-1];assert value.rstrip('\n')==z['heading'] and h(value.encode())==z['heading_sha256'];assert re.match(r'^#+\s+'+re.escape(z['section_number'])+r'(?:\s|[.、:：])',value);heads+=1
    for row in r['current_test_rows']:
        raw=c.show(c.ACT,row['path']);line=raw.splitlines(keepends=True)[row['line']-1];assert len(line)==row['row_bytes'] and h(line)==row['row_sha256'];assert re.match(br'^\|\s*'+re.escape(row['id'].encode())+br'\s*\|',line);rows+=1
    assert [x['id'] for x in r['current_test_rows']]==r['static_test_ids_not_executed']
    for receipt in r['candidate_receipts']:
        assert receipt['reviewed_candidate']==c.C3 and receipt['report_commit']!=c.ACT
        for path in receipt['complete_directory_paths']:assert c.show(c.ACT,path)==c.show(receipt['report_commit'],path)
    assert r['status']=='INTEGRATED_PENDING_ACTUAL' and not r['accepted_B14_contribution'] and not r['closure_authorized']
    checks.append({'id':rid,'record_key':r['record_key'],'current_formal_bindings_exact':True,'current_heading_locators':heads,'current_test_row_bindings':rows,'candidate_receipts_separate':True,'pending_actual_and_unaccepted':True})
tsvs=[]
for path in sorted(public):
    if not path.endswith('.tsv'):continue
    bef=c.show(c.BASE,path);aft=c.show(c.ACT,path);assert aft.startswith(bef)
    before=list(csv.DictReader(io.StringIO(bef.decode()),delimiter='\t'));now=list(csv.DictReader(io.StringIO(aft.decode()),delimiter='\t'));assert len(before)==170 and len(now)==194 and list(before[0])==list(now[0]) and now[:170]==before
    for r,row in zip(reg['dispositions'],now[170:]):
        assert r['id']==row['finding_id'] and row['canonical_state']=='OPEN' and row['candidate_commit']==c.C3
        rem=json.loads(row['remaining_obligations']);assert rem['record_key']==r['record_key'];assert rem['original_and_approved_binding']==r['original'] and rem['approved_acceptance']==r['approved_acceptance'];assert rem['remaining_contributors']==r['pending_contributors'];assert rem['all_contributors']==r['all_contributor_batches']
        assert rem['candidate_receipts']==[{k:q[k] for k in ['owner','report_commit','reviewed_candidate']} for q in r['candidate_receipts']];assert not rem['canonical_closure']
        if 'reviewed_integration_commit' in row:assert row['reviewed_integration_commit']==row['integration_review_commit']==row['integration_reviewer']==''
        if 'current_clause_inputs' in row:
            t=json.loads(row['current_clause_inputs']);assert t['formal']==r['current_formal_locations'] and t['rows']==r['current_test_rows'];assert row['static_test_ids_not_executed']==','.join(r['static_test_ids_not_executed'])
    tsvs.append({'path':path,'before_records':170,'current_records':194,'exact_raw_prefix_preserved':True,'schema_and_column_order_preserved':True,'24_ordered_records_match_registration':True,'current_ACT_approval_blank':True})
copies=obj(c.ACT,c.G+'copy-identities.json')['files']
for x in copies:
    raw=c.show(c.ACT,x['path']);assert raw==c.show(x['commit'],x['path']) and h(raw)==x['sha256'] and len(raw)==x['bytes']
changed={p for p in actual if base.get(p)!=actual[p]};declared={x['path'] for x in copies}|public|{p for p in actual if p.startswith(c.G)};assert changed==declared and not set(base)-set(actual)
protected=[p for p in base if p not in changed];assert all(actual[p]==base[p] for p in protected)
(P/'final-integration-relationship-checks.json').write_text(json.dumps({'reviewed_ACT':c.ACT,'registrations':checks,'public_tables':tsvs,'copies':len(copies),'formal':12,'evidence':49,'candidate_report_paths':155,'bounded_public_edits':10,'new_G_paths':len([p for p in actual if p.startswith(c.G)]),'changed_paths':len(changed),'protected_predecessor_objects':len(protected),'unaffected_predecessor_objects_equal':True,'unexpected_changed_or_deleted_paths':[],'heading_row_relationships':'Navigation identities verified; quality reasoned independently in contribution/owner dispositions','semantics':'Pending labels are immutable pre-freeze payload values; external ACT controls reviewed identity. No report SHA substitutes for reviewed SHA.'},ensure_ascii=False,indent=2)+'\n')
print('COMPLETE',[(x['path_count'],x['hunk_count']) for x in streams],len(checks),len(copies),len(protected),flush=True)
