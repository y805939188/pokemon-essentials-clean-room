#!/usr/bin/env python3
"""Metadata-only evidence-pointer candidate index; no source/runtime execution."""
from pathlib import Path
import collections, datetime, hashlib, json, re, sys

RR = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
W = RR.parents[2]
R = Path('/workspace/pokemon-essentials')
START = datetime.datetime.now(datetime.timezone.utc).isoformat()
INPUTS, PARSE_ERRORS, LINKS = {}, [], []
def sha(b): return hashlib.sha256(b).hexdigest()
def relative(p):
    try: return str(p.relative_to(RR))
    except ValueError: return str(p)
def jp(p,k): return p+'/'+str(k).replace('~','~0').replace('/','~1')
def read(p, role):
    p = p.resolve()
    raw = p.read_bytes()
    key = relative(p)
    rec = INPUTS.setdefault(key, {'path':key,'bytes':len(raw),'sha256':sha(raw),'roles':[]})
    if role not in rec['roles']: rec['roles'].append(role)
    try: return json.loads(raw)
    except Exception as e:
        PARSE_ERRORS.append({'path':key,'error':str(e),'disposition':'UNKNOWN_SCHEMA_NOT_SEMANTIC_LIMIT'})
        return None
def dump(name,d):
    with (OUT/name).open('w') as f:json.dump(d,f,ensure_ascii=False,separators=(',',':'));f.write('\n')
def walk(v,p=''):
    yield p,v
    if isinstance(v,dict):
        for k,x in v.items(): yield from walk(x,jp(p,k))
    elif isinstance(v,list):
        for i,x in enumerate(v): yield from walk(x,jp(p,i))

inv = {}
for kind, n in [('reference','reference-inventory.json'),('formal','formal-inventory.json')]:
    rows = read(RR/'tasks/inventory_denominator'/n,'FIXED_PATH_IDENTITY_INVENTORY')
    for i,row in enumerate(rows):
        inv[(kind,row['path'])] = {'identity':row,'inventory_pointer':f'/'+str(i)}
REGPATH = RR/'adjudication/root-primary-task-final-registry.v1.json'
reg = read(REGPATH,'CURRENT_ROOT_TASK_FINAL_REGISTRY_SNAPSHOT')
REGHASH = INPUTS[relative(REGPATH)]['sha256']
receipts, receipt_data, roots = {}, {}, collections.defaultdict(set)
bindings = collections.defaultdict(list)
explicit_artifacts = collections.defaultdict(list)

def artifact_path(s, base=None):
    if not isinstance(s,str) or '\n' in s or len(s)>800: return None
    s=s.split('#',1)[0]
    if not s: return None
    if not (s.startswith(('tasks/','evidence/','adjudication/','review/','/workspace/')) or re.fullmatch(r'[\w./ -]+\.(?:json|md|txt)',s)):return None
    p=Path(s)
    attempts=[]
    if p.is_absolute(): attempts=[p]
    else:
        if s.startswith('review/'): attempts.append(W/p)
        attempts.append(RR/p)
        if base: attempts.append(base.parent/p)
    for q in attempts:
        try:
            q=q.resolve()
            q.relative_to(RR)
            if OUT==q or OUT in q.parents: continue
            if q.is_file(): return q
        except (ValueError,OSError): pass
    return None
def owning_root(p):
    parts=p.relative_to(RR).parts
    if len(parts)>1 and parts[0]=='tasks': return RR/parts[0]/parts[1]
    if len(parts)>3 and parts[:2]==('evidence','external-recovered'):
        return RR.joinpath(*parts[:4])
    return None
def bind_paths(d,task,source,depth):
    for pointer,v in walk(d):
        if not isinstance(v,str): continue
        p=artifact_path(v,source)
        if p is None: continue
        link={'task':task,'from':relative(source),'pointer':pointer,'to':relative(p),'kind':'LITERAL_EXISTING_ARTIFACT_PATH','depth':depth}
        LINKS.append(link)
        explicit_artifacts[p].append(link)
        root=owning_root(p)
        if root:
            roots[root].add(task)
            if link not in bindings[root]:bindings[root].append(link)

for i,x in enumerate(reg.get('accepted',[])):
    task=x['task']; expected=x['receipt']; p=RR/expected['path']
    raw=p.read_bytes() if p.exists() else None
    exact=raw is not None and len(raw)==expected['bytes'] and sha(raw)==expected['sha256']
    receipts[task]={'registry_pointer':f'/accepted/{i}','expected':expected,'exact_current_match':exact,'status_original':x.get('status')}
    if not exact: continue
    d=read(p,'EXACT_CURRENT_ROOT_TASK_FINAL_RECEIPT');receipt_data[task]=d
    bind_paths(d,task,p,0)
    # Exact commit may be named separately from the recovered directory, without a path literal.
    commit_values=[]
    for ptr,v in walk(d):
        if isinstance(v,str) and re.fullmatch('[0-9a-f]{40}',v) and 'commit' in ptr.lower():commit_values.append((ptr,v))
    for ptr,c in commit_values:
        for q in (RR/'evidence/external-recovered').glob('*/'+c):
            if q.is_dir():
                roots[q].add(task)
                bindings[q].append({'task':task,'from':relative(p),'pointer':ptr,'to':relative(q),'kind':'EXACT_COMMIT_DIRECTORY_CANDIDATE_ONLY','depth':0})

# Follow explicitly linked adjudication segments, manifests, and operative JSON metadata.
queue=[(p,l['task'],1) for p,ls in list(explicit_artifacts.items()) for l in ls if p.suffix=='.json' and ('adjudication' in p.parts or re.search('manifest|binding',p.name))]
seen_links=set()
while queue:
    p,task,depth=queue.pop(0)
    if (p,task) in seen_links or depth>2:continue
    seen_links.add((p,task))
    d=read(p,'ROOT_LINKED_JSON_METADATA')
    if d is None:continue
    before=set(explicit_artifacts)
    bind_paths(d,task,p,depth)
    for q in set(explicit_artifacts)-before:
        if q.suffix=='.json' and ('adjudication' in q.parts or re.search(r'manifest|binding',q.name)):queue.append((q,task,depth+1))

# Resource support is explicitly enumerated by the root receipt; name-to-directory resolution is navigation only.
resource=receipt_data.get('resource_media_serialized',{})
for ptr,v in walk(resource.get('real_qualified_readers',[]),'/real_qualified_readers'):
    if isinstance(v,str) and v.startswith('/root/'):
        q=RR/'tasks'/v.split('/')[-1]
        if q.is_dir():
            roots[q].add('resource_media_serialized')
            bindings[q].append({'task':'resource_media_serialized','from':receipts['resource_media_serialized']['expected']['path'],'pointer':ptr,'to':relative(q),'kind':'EXPLICIT_ROOT_READER_NAME_DIRECTORY_NAVIGATION_ONLY'})

# Original routed owners and later named split primaries with no exact current receipt stay unaccepted candidates.
scope=read(RR/'delegation/scope-freeze.v1.json','ORIGINAL_ROUTING_ONLY_NO_READING_CREDIT')
unaccepted_roots=set()
for name in list(scope.get('primary_assignments',{}))+['com_battler','com_ability_item','creature_b','creature_a','creature_c','combat_review','kernel_review','formal_shared','reference_metadata','localization_records']:
    p=RR/'tasks'/name
    if p.is_dir() and p not in roots:unaccepted_roots.add(p)
unaccepted_roots.add(RR/'tasks/coverage_acceptance_incremental/delta-inputs/root-primaries/formal_shared')

selector=re.compile(r'identit|reading[-_].*ledger|read[-_].*ledger|^reading-ledger|forward|reverse|source-to-spec|clause-to-source|accepted-contribution|manifest|readset|peer[-_](?:receipt|reception)|source[-_]reading|^contribution')
metadata=collections.defaultdict(set)
for root,tasks in list(roots.items()):
    for p in root.rglob('*.json'):
        rel=p.relative_to(root)
        if any(x in ['io','read-io','read_io','raw','input-snapshot','.git','node_modules','integration-membership'] for x in rel.parts):continue
        if selector.search(p.name):metadata[p].update(tasks)
for root in unaccepted_roots:
    for p in root.rglob('*.json'):
        rel=p.relative_to(root)
        if any(x in ['io','read-io','read_io','raw','input-snapshot','.git','node_modules','integration-membership'] for x in rel.parts):continue
        if selector.search(p.name):metadata[p].add('NO_CURRENT_TASK_FINAL_RECEIPT:'+root.name)
for p,links in explicit_artifacts.items():
    if p.suffix=='.json' and selector.search(p.name):
        metadata[p].update(x['task'] for x in links)

CANONICAL_PATHS={path:kind for kind,path in inv}
BASES=[str(R)+'/',str(W)+'/',str(W/'reference/pokemon-essentials')+'/']
def canonical(s):
    if not isinstance(s,str):return None
    if s in CANONICAL_PATHS:return CANONICAL_PATHS[s],s,'EXACT_PATH'
    if len(s)>500 or not s.startswith(('Data/','Fonts/','PBS/','deliverables/','/workspace/','./')):return None
    s=s.strip().replace('\\','/')
    for base in BASES:
        if s.startswith(base):s=s[len(base):];break
    if s.startswith('./'):s=s[2:]
    s=s.split('#',1)[0]
    # Only exact known path, or exact known path followed by a line locator. Never basename expansion.
    for kind in ['reference','formal']:
        if (kind,s) in inv:return kind,s,'EXACT_PATH'
    line=re.match(r'^(.*?)(?::(?:L)?\d+(?:[-–]\d+)?|#L\d+)$',s)
    if line:
        for kind in ['reference','formal']:
            if (kind,line[1]) in inv:return kind,line[1],'EXACT_PATH_WITH_LINE_LOCATOR'
    return None

reader_keys=re.compile(r'^(?:reader|reviewer|actual_reader|actual_reviewer|owner|actor|source_reader|actual_source_reader|source_actual_reader|actual_original_reader|original_reader|actual_primary_reader|actual_primary_semantic_reader|actual_semantic_reader|team_full_reader|actual_primary_receiver|source_read_by|read_by|received_by|receiver|actual_receiver|original_author|primary_reception_thread)$')
state_keys=re.compile(r'(?:^status$|semantic_status|reading_status|read_status|evidence_level|source_status|credit$|own_full_read|full_read$|personal_status|read_credit|byte_association|disposition$)')
range_keys=re.compile(r'(?:range|interval|read_lines|physical_line_count|total_lines|line_count|unread_raw_lines|source_read_method|reading_method|consumer_status|qualification|boundary|scope$|scope_limit|credit_warning|source_credit_policy)')
id_keys={'bytes','sha256','git_blob','actual_blob','blob','commit','frozen_commit','ref','repo','git_bytes','observed_bytes','observed_sha256'}
def small(v):
    if isinstance(v,(str,int,float,bool)) or v is None:return v
    if isinstance(v,list) and len(v)<=80 and all(not isinstance(x,dict) for x in v):return v
    if isinstance(v,dict) and len(v)<=20 and all(isinstance(x,(str,int,float,bool,list,type(None))) for x in v.values()):return v
    return None
def fields(d,p,rx):
    out=[]
    if isinstance(d,dict):
        for k,v in d.items():
            if rx.search(k) and small(v) is not None:
                raw=json.dumps(small(v),ensure_ascii=False,separators=(',',':'))
                if len(raw)>2000:out.append({'pointer':jp(p,k),'value':'NOT_INLINED_SEE_EXACT_ORIGINAL_POINTER','original_value_type':type(v).__name__,'original_value_json_bytes':len(raw.encode()),'not_a_reading_limit':True})
                else:out.append({'pointer':jp(p,k),'value':small(v)})
    return out
def categorize(v):
    ss=' '.join(str(x['value']) for x in v).upper()
    labels=[]
    # Search labels are navigation only and never a semantic or completeness verdict.
    if 'ASSOCIAT' in ss or 'BYTE_IDENT' in ss:labels.append('RAW_ASSOCIATION_LABEL_PRESENT')
    if 'PARTIAL' in ss or 'FINITE' in ss or 'RELEVANT_COMPLETE' in ss:labels.append('RAW_PARTIAL_OR_FINITE_LABEL_PRESENT')
    if 'FULL' in ss or 'WHOLE' in ss:labels.append('RAW_FULL_OR_WHOLE_LABEL_PRESENT')
    if 'UNREAD' in ss or 'OPEN' in ss:labels.append('RAW_UNREAD_OR_OPEN_LABEL_PRESENT')
    return labels or ['ORIGINAL_STATUS_UNSPECIFIED']

dump('discovery.json',{'metadata_files':len(metadata),'metadata_bytes':sum(p.stat().st_size for p in metadata),'roots':[{ 'path':relative(p),'task_candidates':sorted(t)} for p,t in roots.items()],'registry_snapshot_sha256':REGHASH})
groups=collections.defaultdict(dict)
artifact_statistics=[]
for p,tasks in sorted(metadata.items(),key=lambda x:str(x[0])):
    d=read(p,'ORIGINAL_OWNER_STRUCTURED_METADATA_INDEXED_ONLY')
    if d is None:continue
    globalread=fields(d,'',reader_keys)
    hits=0
    def rec(v,ptr='',ancestors=()):
        nonlocal_placeholder=None
        if isinstance(v,dict):
            for k,x in v.items():rec(x,jp(ptr,k),ancestors+((ptr,v),))
        elif isinstance(v,list):
            for i,x in enumerate(v):rec(x,jp(ptr,i),ancestors)
        elif isinstance(v,str):
            result=canonical(v)
            if result is None:return
            key, path, mode=result
            if not ancestors:return
            rptr,node=ancestors[-1]
            # identity subobjects may inherit row fields from their immediate containing record, not arbitrary aggregates.
            if ptr.rsplit('/',1)[-1] in ['path','payload','identity_path','source','formal','reference','source_path','formal_path'] and rptr.endswith('/identity') and len(ancestors)>1:rptr,node=ancestors[-2]
            rr=fields(node,rptr,reader_keys)
            if not rr:rr=globalread
            states=fields(node,rptr,state_keys)
            ranges=fields(node,rptr,range_keys)
            ids=[{'pointer':jp(rptr,k),'value':x} for k,x in node.items() if k in id_keys and small(x) is not None]
            for k in ['identity','identity_binding','file_identity','source_identity']:
                if isinstance(node.get(k),dict):
                    ids += [{'pointer':jp(jp(rptr,k),a),'value':b} for a,b in node[k].items() if a in id_keys and small(b) is not None]
            artifact=relative(p)
            bucket=(artifact,tuple(sorted(tasks)),json.dumps(rr,sort_keys=True),json.dumps(states,sort_keys=True),json.dumps(ranges,sort_keys=True),json.dumps(ids,sort_keys=True))
            g=groups[(key,path)].setdefault(bucket,{'artifact':artifact,'owner_task_candidates':sorted(tasks),'membership_mode':mode,'path_pointers':[],'reader_fields_original':rr,'status_fields_original':states,'range_and_qualification_fields_original':ranges,'identity_fields_original':ids,'navigation_labels_only':categorize(states)})
            g['path_pointers'].append(ptr)
    rec(d)
    artifact_statistics.append({'path':relative(p),'task_candidates':sorted(tasks),'schema_original':d.get('schema') if isinstance(d,dict) else 'LIST','root_binding':'CANDIDATE_DIRECTORY_OR_EXPLICIT_LINK_ONLY_NO_BLANKET_ACCEPTANCE'})

# Per-artifact groups carry raw fields and pointers; receipt binding is reported separately.
rows=[]
unmatched=[]
binary_kinds={'native_PE','serialized_data','font_tables_and_glyphs','bitmap_pixels','soundfont_RIFF_hydra'}
for (kind,path),fixed in inv.items():
    candidates=list(groups.get((kind,path),{}).values())
    for c in candidates:
        c['path_pointers']=sorted(set(c['path_pointers']))
        c['exact_current_root_receipts']=[{'task':t,'registry_pointer':receipts[t]['registry_pointer'],'receipt_path':receipts[t]['expected']['path'],'inputs_pointer':'/root_receipts/'+t,'exact_current_match':True} for t in c['owner_task_candidates'] if t in receipts and receipts[t]['exact_current_match']]
        c['receipt_binding_qualification']='Root accepted task exists; this artifact/path membership is a pointer candidate, not individual blanket semantic approval.'
    has_reader=any(c['reader_fields_original'] for c in candidates)
    has_receipt=any(c['exact_current_root_receipts'] for c in candidates)
    has_both=any(c['reader_fields_original'] and c['exact_current_root_receipts'] for c in candidates)
    identity=fixed['identity']
    row={'kind':kind,'path':path,'fixed_identity':{k:identity.get(k) for k in ['repo','commit','workspace_tree','git_blob','bytes','sha256','payload_kind']},'inventory_pointer':{'artifact':f'tasks/inventory_denominator/{kind}-inventory.json','pointer':fixed['inventory_pointer']},'candidate_groups':candidates,'mechanical_only':True,'semantic_PASS':None,'individual_FULL_granted':False}
    if kind=='reference' and identity.get('payload_kind') in binary_kinds:
        row['resource_root_guard']={'receipt':receipts.get('resource_media_serialized'),'readers_list_pointer':'/real_qualified_readers','populations_pointer':'/required_readable_populations','opaque_boundary_pointer':'/named_remaining_machinecode_boundary','qualification':'Required readable resources/programs and actual finite native windows only. Never entire machinecode/binary FULL. Original per-reader ranges/status retained.'}
    reasons=[]
    if not candidates:reasons.append('NO_EXACT_FIXED_PATH_OCCURRENCE_IN_SELECTED_ORIGINAL_METADATA')
    if not has_reader:reasons.append('NO_EXPLICIT_READER_FIELD_BOUND_TO_EXACT_PATH_CANDIDATE')
    if not has_receipt:reasons.append('NO_EXACT_CURRENT_REGISTRY_RECEIPT_FOR_PATH_CANDIDATE_OWNER')
    if has_reader and has_receipt and not has_both:reasons.append('READER_AND_CURRENT_RECEIPT_NOT_IN_SAME_CANDIDATE_BINDING')
    row['mapping_status']='CANDIDATE_WITH_EXPLICIT_READER_AND_CURRENT_RECEIPT' if has_both else 'INCOMPLETE_CANDIDATE_MAPPING'
    rows.append(row)
    if reasons:unmatched.append({'kind':kind,'path':path,'reasons':reasons,'candidate_artifacts':sorted({c['artifact'] for c in candidates}),'disposition':'UNKNOWN_MAPPING_NOT_MATERIAL_LIMIT_NOT_SEMANTIC_FAIL'})

END=datetime.datetime.now(datetime.timezone.utc).isoformat()
registry_unchanged=sha(REGPATH.read_bytes())==REGHASH
validation={'schema':'gr8-mechanical-membership-validation/v1','start_utc':START,'end_utc':END,'exit':0,'fixed_reference_paths':sum(x['kind']=='reference' for x in rows),'fixed_formal_paths':sum(x['kind']=='formal' for x in rows),'unique_keys':len({(x['kind'],x['path']) for x in rows}),'registry_entries':len(receipts),'exact_current_receipts':sum(x['exact_current_match'] for x in receipts.values()),'registry_unchanged_during_run':registry_unchanged,'candidate_groups':sum(len(x['candidate_groups']) for x in rows),'paths_with_candidate_reader_and_receipt':sum(x['mapping_status']=='CANDIDATE_WITH_EXPLICIT_READER_AND_CURRENT_RECEIPT' for x in rows),'unmatched_paths':len(unmatched),'binary_guard_rows':sum('resource_root_guard'in x for x in rows),'input_artifacts':len(INPUTS),'parse_errors':PARSE_ERRORS,'new_contexts':0,'new_votes':0,'new_semantic_reading_credit':0,'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True,'global_denominator_frozen_here':False,'global_PASS_granted':False,'actual_configuration_UUID':'UNVERIFIED'}
assert validation['fixed_reference_paths']==432 and validation['fixed_formal_paths']==131
assert validation['binary_guard_rows']==18
assert validation['unique_keys']==563
# A concurrent registry successor is retained as a separate later input by qualify_index.py.
dump('index.json',{'schema':'gr8-fixed-path-evidence-pointer-candidates/v1','scope':'MECHANICAL_INDEX_ONLY_NO_NEW_READING_CREDIT','rows':rows})
dump('unmatched.json',{'schema':'gr8-mechanical-mapping-unmatched/v1','qualification':'Missing mappings are unknown, never inferred limits or semantic failures. Candidate presence is not sufficient semantic coverage.','rows':unmatched})
dump('inputs.json',{'schema':'gr8-membership-index-input-identities/v1','registry_snapshot_sha256':REGHASH,'inputs':list(INPUTS.values()),'root_receipts':receipts,'candidate_root_bindings':[{'directory':relative(p),'tasks':sorted(t),'links':bindings[p]} for p,t in roots.items()],'artifact_statistics':artifact_statistics})
dump('links.json',{'schema':'gr8-literal-artifact-pointer-links/v1','qualification':'Directory and literal path navigation only. Exact bytes do not grant semantic credit.','links':LINKS})
dump('validation.json',validation)
report=f'''# 固定路径证据指针候选索引\n\n本次仅索引现有结构化字段；新增 context、独立票、语义阅读信用均为 0。固定路径为 R432/F131，共 563 个唯一成员。未冻结全局语义分母、未授语义 PASS、未把原 PARTIAL/finite/byte-association 升为 FULL。\n\n当前 registry 快照含 {len(receipts)} 项，精确收据匹配 {validation['exact_current_receipts']} 项。{validation['paths_with_candidate_reader_and_receipt']} 个路径具有“同一候选中的原 reader 字段及当前 task-final 收据”；这只是可核对指针，仍须 root 检查原字段、范围及接收链，不能直接当逐路径语义通过。{len(unmatched)} 个路径列在 unmatched.json。\n\n- `index.json`：每个固定 path、原始身份、JSON 指针、原 reader/status/range/qualification 字段，以及候选当前收据。\n- `inputs.json`：实际解析输入的字节数/SHA、收据及目录绑定来源；`links.json` 保留字面导航链。目录成员关系不等于逐文件实际接收。\n- `unmatched.json`：无精确原路径、无具名 reader 或无当前收据等机械缺口；均保 UNKNOWN，不改成材料 limit。\n- `validation.json`：563 唯一成员、21 份快照收据、18 个 binary 限定和本次机械执行状态。\n\n18 个原 binary 均附 root 可读 resource 收据和原实际读者列表/可读总体/opaque native 范围指针；仅保留实际结构、程序、字段和有限机器码窗口资格，不声称整个 binary 或全 machinecode FULL。\n\n原身份库存的 UNREAD/INVENTORY_ONLY 只代表库存时点；forward/reverse 的行数未用作原子分母。未展开 basename 推断；不重复审读源/record 语义。被引用的旧状态与较新状态原样共存，索引不自行选新状态覆盖旧账。\n\n业务行为 NOT_EXECUTED；UPDATE_NOT_STARTED。实际 model/effort/tier/speed/Fast/UUID 均 UNVERIFIED。本次输入读取与 Python 解析仅是机械索引，不能冒充原 owner/source 的新 FULL 信用。\n'''
(OUT/'report.md').write_text(report)
print(json.dumps(validation,ensure_ascii=False))

