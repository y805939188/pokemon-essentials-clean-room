#!/usr/bin/env python3
"""Independent bounded delta/conservation audit; reads fixed Git blobs only."""
import ast
import collections
import copy
import difflib
import functools
import gzip
import hashlib
import json
from pathlib import Path
import re
import subprocess
import unicodedata

ROOT = Path('/workspace/r8-r3-seven-line-review')
OUT = ROOT / 'review/r8-r3-seven-line-independent-7ed3e05-20261017/agents'
P = 'planning/implementation-routing/r8-20261017/'
C = '7ed3e0554ac24339a7e61cab152f628037111644'
B = 'c0f62d973180679134f2eb1a488c1dc359c8658f'
PRIOR = '34202eb7accfee48bb8761db88b340bd77f54a42'
R2 = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'
INITIAL = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
CURRENT = '5f87743293290de2e219ecdd6c19e88280f60c9a'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
IDS = ['FR-000029','FR-000032','FR-000173','FR-000204','FR-000227','FR-000456','FR-000596']
reads = {}
checks = []
def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT)
def sha(raw):
    return hashlib.sha256(raw).hexdigest()
def ident(raw):
    try: lines = len(raw.decode().splitlines())
    except UnicodeDecodeError: lines = None
    return dict(bytes=len(raw),sha256=sha(raw),git_blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),lines=lines)
@functools.lru_cache(None)
def blob(c,p):
    raw=git('show',c+':'+p)
    reads[c+':'+p]=ident(raw)
    return raw
def load(p,c=C): return json.loads(blob(c,P+p))
def save(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def require(name,condition,detail=None):
    checks.append(dict(check=name,passed=bool(condition),detail=detail))
def escape(x): return str(x).replace('~','~0').replace('/','~1')
def diff(a,b,p=''):
    if type(a) is not type(b): return [dict(pointer=p,kind='TYPE_OR_VALUE',before=a,after=b)]
    if isinstance(a,dict):
        out=[]
        for k in sorted(a.keys()|b.keys()):
            q=p+'/'+escape(k)
            if k not in a: out.append(dict(pointer=q,kind='ADD',after=b[k]))
            elif k not in b: out.append(dict(pointer=q,kind='REMOVE',before=a[k]))
            else: out.extend(diff(a[k],b[k],q))
        return out
    if isinstance(a,list):
        if len(a)!=len(b): return [dict(pointer=p,kind='ARRAY_LENGTH',before=a,after=b)]
        return [v for i,(x,y) in enumerate(zip(a,b)) for v in diff(x,y,p+'/'+str(i))]
    return [] if a==b else [dict(pointer=p,kind='VALUE',before=a,after=b)]
def get(obj,p):
    for part in p.strip('/').split('/') if p else []:
        part=part.replace('~1','/').replace('~0','~')
        obj=obj[int(part)] if isinstance(obj,list) else obj[part]
    return obj
def byid(rows): return {r['feature_id']:r for r in rows}

# Full fixed-parent tree delta, not the author's changes-from-c0 list.
paths=git('diff','--name-only',B,C).decode().splitlines()
oldpaths=set(git('ls-tree','-r','--name-only',B,'--',P).decode().splitlines())
files=[]
for path in paths:
    old=blob(B,path) if path in oldpaths else None
    new=blob(C,path)
    row=dict(path=path,previous=ident(old) if old is not None else None,current=ident(new))
    if path.endswith('.json'):
        row['comparison']='COMPLETE_JSON_OBJECT_POINTER_DIFF'
        row['delta']=diff(json.loads(old),json.loads(new)) if old is not None else [dict(pointer='',kind='ADD_FILE',after=json.loads(new))]
    else:
        raw=gzip.decompress(new) if path.endswith('.gz') else new
        row['comparison']='DECOMPRESSED_COMPLETE_TEXT' if path.endswith('.gz') else 'COMPLETE_TEXT_DIFF'
        row['decompressed_identity']=ident(raw) if path.endswith('.gz') else None
        row['delta_text']=''.join(difflib.unified_diff((old or b'').decode(errors='replace').splitlines(True),raw.decode().splitlines(True),fromfile=B+':'+path,tofile=C+':'+path))
    files.append(row)
save('propagation-full-pointer-delta.json',dict(candidate=C,parent=B,paths=len(paths),files=files))
require('exactly41_changed_paths_all_within_routing',len(paths)==41 and all(p.startswith(P) for p in paths))
require('candidate_exact_single_parent',git('rev-list','--parents','-n','1',C).decode().split()==[C,B])

m=load('routing-manifest.json'); old=load('routing-manifest.json',B)
features=byid(m['features']); oldfeatures=byid(old['features'])
mdelta=diff(old,m)
expected=['/features/'+str(i)+'/differences/1' for i,f in enumerate(m['features']) if f['feature_id'] in IDS]
require('manifest_exact_seven_differences1_leaves',sorted(x['pointer'] for x in mdelta)==sorted(expected),mdelta)
require('all_other_manifest_values_identical_parent',len(mdelta)==7)
unchanged=[]
for i,f in enumerate(m['features']):
    prior=oldfeatures[f['feature_id']]
    protected={k:v for k,v in f.items() if k!='differences'}
    unchanged.append(dict(feature_id=f['feature_id'],protected_object_sha256=sha(json.dumps(protected,ensure_ascii=False,sort_keys=True).encode()),
        all_fields_except_differences_equal=protected=={k:v for k,v in prior.items() if k!='differences'},
        differences_equal=f['differences']==prior['differences'],
        out_feature_refs=f['dependencies']['feature_refs'],
        inbound_feature_refs=[x['feature_id'] for x in m['features'] if f['feature_id'] in x['dependencies']['feature_refs']],
        reason='Only current descriptive difference leaf repaired; immutable/current locator, source scope, responsibilities, dependency edges and target/stage states identical.' if f['feature_id'] in IDS else 'Complete row identical; no edge or source contract changed by this descriptive repair. Existing prior independent four-facet/source calibration credit remains applicable.'))
require('all736_protected_objects_equal',len(unchanged)==736 and all(x['all_fields_except_differences_equal'] for x in unchanged))
require('729_complete_rows_equal',sum(x['differences_equal'] for x in unchanged)==729)
require('all_documents_metadata_retired_full_objects_equal_parent',all(m[k]==old[k] for k in ['documents','metadata_records','retired_features']))
initial=load('routing-manifest.json',INITIAL); initialrows=byid(initial['features']+initial.get('retired_features',[]))
require('33_retired_bodies_equal_initial_d62',len(m['retired_features'])==33 and all({k:v for k,v in f.items() if k!='retirement'}==initialrows[f['feature_id']] for f in m['retired_features']))
require('33_metadata_equal_R2',m['metadata_records']==load('routing-manifest.json',R2)['metadata_records'] and len(m['metadata_records'])==33)
require('all736_pending_target_and_stage',all(f['destination_verification']['status']=='待验证' and f['future_plan']['stage']=='待定' and f['future_plan']['stage_approval']=='未批准' and f['implementation']['status']=='未实现' and f['implementation']['acceptance_status']=='未验收' for f in m['features']))
save('propagation-row-conservation.json',dict(candidate=C,parent=B,records=unchanged))

# Reconstruction starts from the genuine archived 35175 bytes; validates all before values.
archive_name='revisions/r3/tools/post-source-pre-semantic-35175c7094b0.json.gz'
archive=gzip.decompress(blob(C,P+archive_name)); patch=load('revisions/r3/source-refinement-patch.json'); oldpatch=load('revisions/r3/source-refinement-patch.json',B)
reconstructed=json.loads(archive); target=byid(reconstructed['features']); replay=[]
for record in patch['records']:
    for change in record['field_changes']:
        obj=target[record['feature_id']]; parts=change['pointer'].strip('/').split('/')
        for p in parts[:-1]: obj=obj[p]
        replay.append(dict(feature_id=record['feature_id'],pointer=change['pointer'],before_equal=obj[parts[-1]]==change['before']))
        obj[parts[-1]]=copy.deepcopy(change['after'])
serialized=(json.dumps(reconstructed,ensure_ascii=False,indent=2)+'\n').encode()
require('35175_archive_hash_and_original_bytes',sha(archive)==patch['input_manifest_sha256']=='35175c7094b008e77af35cf6a7811c5fcd6f1a0dd20020b64d32b40d5670256e' and blob(C,P+archive_name)==blob(B,P+archive_name))
require('replay78_rows162_fields_all_before_values_equal',len(patch['records'])==78 and len(replay)==162 and all(x['before_equal'] for x in replay))
require('full_reconstructed_object_and_serialized_bytes_equal',reconstructed==m and serialized==blob(C,P+'routing-manifest.json'))
pdelta=diff(oldpatch,patch)
require('patch_exactly_seven_after_difference_second_values',len(pdelta)==7 and all(re.fullmatch(r'/records/\d+/field_changes/\d+/after/1',x['pointer']) for x in pdelta))
require('all_patch_before_values_unchanged',[(r['feature_id'],[(c['pointer'],c['before']) for c in r['field_changes']]) for r in patch['records']]==[(r['feature_id'],[(c['pointer'],c['before']) for c in r['field_changes']]) for r in oldpatch['records']])
preserved=['revisions/r3/author-refinement-application.json','revisions/r3/source-narrative-correction.json','revisions/r3/tools/accepted-backfill-result.json']
require('original_apply_receipts_preserved',all(blob(C,P+p)==blob(B,P+p) for p in preserved))
history=[p for p in git('ls-tree','-r','--name-only',R2,'--',P).decode().splitlines() if '/revisions/r1/' in p or '/revisions/r2/' in p]
history_records=[dict(path=p,identity=ident(blob(C,p)),equal_R2=blob(C,p)==blob(R2,p),equal_parent=blob(C,p)==blob(B,p)) for p in history]
require('all58_R1_R2_historical_artifacts_preserved',len(history)==58 and all(x['equal_R2'] and x['equal_parent'] for x in history_records))
save('propagation-reconstruction.json',dict(candidate=C,archive_identity=ident(archive),replayed_rows=len(patch['records']),replayed_fields=len(replay),replay=replay,manifest_identity=ident(serialized),object_equal=reconstructed==m,serialized_equal=serialized==blob(C,P+'routing-manifest.json'),historical_files=history_records))

# Propagation, without importing any author module or facts dictionary.
delta=load('revisions/r3/feature-source-deltas.json'); prevdelta=load('revisions/r3/feature-source-deltas.json',B)
fdiff=diff(prevdelta,delta)
require('seven_unit_records_only_fact_and_future_boundary_changed',len(fdiff)==14 and {delta['records'][int(x['pointer'].split('/')[2])]['feature_id'] for x in fdiff}==set(IDS) and all(x['pointer'].endswith(('/source_fact_delta','/future_boundary_reassessment')) for x in fdiff))
fdocs=load('revisions/r3/source-file-reassessment.json'); fdocprev=load('revisions/r3/source-file-reassessment.json',B)
ddiff=diff(fdocprev,fdocs)
require('six_file_records_only_fact_and_future_boundary_changed',len(ddiff)==12 and len({x['pointer'].split('/')[2] for x in ddiff})==6 and all(x['pointer'].endswith(('/source_fact_reassessment','/future_plan_reassessment')) for x in ddiff))
unitrows=byid(delta['records']); filerows={r['document']:r for r in fdocs['records']}; sourceproof=[]
for fid in IDS:
    f=features[fid]; u=unitrows[fid]; document=f['source']['document']; loc=f['current_applicability']['locator']; raw=blob(CURRENT,document); lines=raw.decode().splitlines(True)
    effective=''.join(''.join(lines[a-1:b]) for a,b in loc['line_ranges']).encode()
    sourceproof.append(dict(feature_id=fid,document=document,current_commit=CURRENT,ranges=loc['line_ranges'],file_sha256=sha(raw),unit_sha256=sha(effective),file_identity_matches=sha(raw)==loc['file_sha256'] and ident(raw)['git_blob']==loc['file_git_blob'],unit_matches=sha(effective)==loc['unit_sha256'],unit_sidecar_matches_manifest=f['differences'][1].startswith(u['source_fact_delta']),future_boundary_matches_file=u['future_boundary_reassessment']==filerows[document]['future_plan_reassessment']))
require('all_seven_source_units_fixed_git_and_sidecars_aligned',all(all(r[k] for k in ['file_identity_matches','unit_matches','unit_sidecar_matches_manifest','future_boundary_matches_file']) for r in sourceproof))
require('six_file_facts_exact_unit_aggregation',all(r['source_fact_reassessment']==''.join(unitrows[fid]['source_fact_delta'] for fid in IDS if features[fid]['source']['document']==r['document']) for r in fdocs['records'] if r['document'] in {features[fid]['source']['document'] for fid in IDS}))
text=blob(C,P+'revisions/r3/build-author-evidence.py').decode(); prior=blob(B,P+'revisions/r3/build-author-evidence.py').decode()
def assigns(t): return {n.targets[0].id:ast.literal_eval(n.value) for n in ast.parse(t).body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ['manual','unit_narratives']}
curas=assigns(text); oldas=assigns(prior)
require('generator_manual_exact_six_facts_and_boundaries_only',set(curas['manual'])==set(oldas['manual']) and [k for k in oldas['manual'] if curas['manual'][k]!=oldas['manual'][k]]==[Path(r['document']).name for r in fdocs['records'] if any(x['pointer']=='/records/'+str(fdocs['records'].index(r))+'/source_fact_reassessment' for x in ddiff)])
affected_documents={features[fid]['source']['document'] for fid in IDS}
require('generator_six_affected_fact_boundary_values_match_sidecars',all(curas['manual'][Path(r['document']).name]==(r['source_fact_reassessment'],r['future_plan_reassessment']) for r in fdocs['records'] if r['document'] in affected_documents))
require('generator_WP42_unit_overrides_exact',curas['unit_narratives']=={fid:unitrows[fid]['source_fact_delta'] for fid in ['FR-000029','FR-000032']})
require('generator_historical_guard_byte_preserved',text.splitlines(True)[:7]==prior.splitlines(True)[:7] and '35175c7094b008e77af35cf6a7811c5fcd6f1a0dd20020b64d32b40d5670256e' in ''.join(text.splitlines(True)[:7]))
class NormalizeGenerator(ast.NodeTransformer):
    def visit_Assign(self,node):
        if isinstance(node.targets[0],ast.Name) and node.targets[0].id=='unit_narratives': return None
        if isinstance(node.targets[0],ast.Name) and node.targets[0].id=='manual': node.value=ast.Constant(value='BOUND_FACTS_VERIFIED_SEPARATELY')
        return self.generic_visit(node)
    def visit_Call(self,node):
        if isinstance(node.func,ast.Attribute) and isinstance(node.func.value,ast.Name) and node.func.value.id=='unit_narratives' and node.func.attr=='get': return ast.parse("d['source_fact_reassessment']",mode='eval').body
        return self.generic_visit(node)
require('generator_all_other_AST_identical',ast.dump(NormalizeGenerator().visit(ast.parse(text)))==ast.dump(NormalizeGenerator().visit(ast.parse(prior))))
preexisting_generator_differences=[dict(document=r['document'],generator_fact=curas['manual'][Path(r['document']).name][0],final_sidecar_fact=r['source_fact_reassessment'],both_unchanged_from_parent=curas['manual'][Path(r['document']).name]==oldas['manual'][Path(r['document']).name] and r==fdocprev['records'][fdocs['records'].index(r)]) for r in fdocs['records'] if r['document'] not in affected_documents and curas['manual'][Path(r['document']).name]!=(r['source_fact_reassessment'],r['future_plan_reassessment'])]
require('three_legacy_generator_final_sidecar_differences_unchanged',len(preexisting_generator_differences)==3 and all(r['both_unchanged_from_parent'] for r in preexisting_generator_differences))
facet_diffs={}
for name,key in [('facet-inheritance.json','records'),('feature-resolution.json','active_feature_results')]:
    cur=load('revisions/r3/'+name); prev=load('revisions/r3/'+name,B); changes=diff(prev,cur); facet_diffs[name]=changes
    require(name+'_only_seven_author_pending_records',len(changes)==7 and {cur[key][int(d['pointer'].split('/')[2])]['feature_id'] for d in changes}==set(IDS) and all(d['kind']=='ADD' and d['pointer'].endswith('/current_calibration_repair') and d['after']['author_status']=='CORRECTED_AWAITING_INDEPENDENT_REVIEW' and d['after']['received_facet_verdict']=='FAIL' for d in changes))
# Every unaffected view byte is conserved, and affected view text changes are exactly replacements.
views=[p for p in paths if '/views/' in p]
for path in views:
    previous=blob(B,path).decode(); expected_view=previous
    for fid in IDS: expected_view=expected_view.replace(oldfeatures[fid]['differences'][1],features[fid]['differences'][1])
    require('view_exact_narrative_replacements:'+Path(path).name,expected_view.encode()==blob(C,path))
require('exactly_three_affected_views',len(views)==3)
actual_source_diff=git('diff','--abbrev=7',B8,CURRENT,'--',*sorted(affected_documents))
require('six_file_diff_archive_equal_actual_fixed_Git',gzip.decompress(blob(C,P+'revisions/r3-calibration-repair/source-six-files.diff.gz'))==actual_source_diff)
source_readset=''
for fid in IDS:
    f=features[fid];p=f['source']['document'];lines=blob(CURRENT,p).decode().splitlines()
    source_readset+=fid+' '+CURRENT+':'+p+'\n'
    for a,b in f['current_applicability']['locator']['line_ranges']:
        source_readset+=''.join(str(n)+': '+lines[n-1]+'\n' for n in range(a,b+1))
    source_readset+='\n'
require('seven_unit_readset_archive_exact_fixed_Git',source_readset.encode()==gzip.decompress(blob(C,P+'revisions/r3-calibration-repair/source-effective-readset.txt.gz')))
save('propagation-sidecar-proof.json',dict(candidate=C,unit_deltas=fdiff,file_deltas=ddiff,patch_deltas=pdelta,facet_deltas=facet_diffs,source_units=sourceproof,views=views,preexisting_nonrunnable_historical_generator_differences=preexisting_generator_differences))

# Independent Markdown heading/range walk (no routing imports).
def headings(raw):
    lines=raw.decode().splitlines(True); result=[]; seen=collections.Counter(); fence=None
    for n,line in enumerate(lines,1):
        fm=re.match(r'^\s{0,3}(`{3,}|~{3,})',line)
        if fm:
            mark=fm[1][0]; fence=mark if fence is None else None if fence==mark else fence
            continue
        if fence: continue
        match=re.match(r'^(#{1,6})[ \t]+(.+?)[ \t]*\n?$',line)
        if not match: continue
        title=re.sub(r'[ \t]+#+[ \t]*$','',match[2]); cleaned=re.sub(r'<[^>]*>','',title)
        cleaned=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',cleaned).lower()
        base=''.join(c for c in cleaned if c in ' -_' or unicodedata.category(c)[0] in 'LN').replace(' ','-')
        anchor=base+('-'+str(seen[base]) if seen[base] else '');seen[base]+=1
        result.append(dict(level=len(match[1]),title=title,anchor=anchor,line_start=n,heading_sha256=sha(line.encode())))
    for i,row in enumerate(result): row['line_end']=next((x['line_start']-1 for x in result[i+1:] if x['level']<=row['level']),len(lines))
    return result,lines
historic=load('section-coverage.json'); coverage=load('current-section-coverage.json')
require('historical_coverage_bytes_unchanged_parent_and_R2',blob(C,P+'section-coverage.json')==blob(B,P+'section-coverage.json')==blob(R2,P+'section-coverage.json'))
require('current_coverage_and_mapping_bytes_unchanged_parent',all(blob(C,P+p)==blob(B,P+p) for p in ['current-section-coverage.json','revisions/r3/new-heading-mappings.json']))
heading_errors=[]; actual_historical=[]; actual_current=[]; docproof=[]
for d in m['documents']:
    p=d['source']['path']; now=blob(CURRENT,p); was=blob(B8,p)
    identity=dict(commit=CURRENT,path=p,**{k:ident(now)[k] for k in ['bytes','sha256','git_blob']})
    docproof.append(dict(document_id=d['document_id'],path=p,identity_matches=d['current_applicability']['identity']==identity))
    for commit,raw,out in [(B8,was,actual_historical),(CURRENT,now,actual_current)]:
        hs,_=headings(raw);out.extend(dict(document_id=d['document_id'],path=p,**h) for h in hs)
fields=['document_id','path','level','title','anchor','line_start','line_end','heading_sha256']
project=lambda rows:[{k:r[k] for k in fields} for r in rows]
require('all131_current_document_identities_fixed_Git',len(docproof)==131 and all(r['identity_matches'] for r in docproof))
require('all2683_historical_headings_recomputed',len(actual_historical)==2683 and project(actual_historical)==project(historic['sections']))
require('all2704_current_headings_recomputed',len(actual_current)==2704 and project(actual_current)==project(coverage['sections']))
oldkeys={(s['path'],s['anchor']) for s in historic['sections']}; added=[s for s in actual_current if (s['path'],s['anchor']) not in oldkeys]
mappings=load('revisions/r3/new-heading-mappings.json'); mapproof=[]
for row in mappings['accepted_mappings']:
    p=row['document']; raw=blob(CURRENT,p); hs,lines=headings(raw);h=next(h for h in hs if h['anchor']==row['anchor']); si=row['source_identity']
    expected_si=dict(commit=CURRENT,document=p,anchor=h['anchor'],heading=h['title'],heading_level=h['level'],heading_sha256=sha(h['title'].encode()),raw_markdown_heading_sha256=h['heading_sha256'],line_ranges=[[h['line_start'],h['line_end']]],unit_sha256=sha(''.join(lines[h['line_start']-1:h['line_end']]).encode()),file_sha256=sha(raw),file_git_blob=ident(raw)['git_blob'],file_bytes=len(raw))
    consumer_ok=all(c['source']=={k:features[c['feature_id']]['source'][k] for k in ['commit','document','anchor','line_ranges']} for c in row['consumer_fixed_sources'])
    cov=next(c for c in coverage['sections'] if c['path']==p and c['anchor']==row['anchor'])
    mapproof.append(dict(document=p,anchor=row['anchor'],identity_equal=si==expected_si,consumers_equal=consumer_ok,refs_equal=row['feature_refs']==cov['feature_refs'] and row['metadata_refs']==cov['metadata_refs']))
require('21_added_heading_mappings_fixed_identity_and_consumers',len(added)==len(mapproof)==21 and all(all(r[k] for k in ['identity_equal','consumers_equal','refs_equal']) for r in mapproof))
save('propagation-heading-conservation.json',dict(candidate=C,current_source=CURRENT,documents=docproof,historical_count=len(actual_historical),current_count=len(actual_current),new_heading_count=len(added),new_heading_mapping_proof=mapproof))

# Receipt events are immutable; directly dereference each external acceptance record.
registry=load('accepted-source-updates.json'); events=registry['events']; receiptproof=[]; required=set(); optional=set(); contributions=[]
for e in events:
    evidence=e['evidence'][0]; raw=blob(evidence['commit'],evidence['path']); rec=get(json.loads(raw),e['receipt_record_pointer'])
    required.update(rec.get('required_ids',[]));optional.update(rec.get('selected_optional_ids',[]))
    targets=rec.get('actual_target_identities',[rec['actual_target_identity']] if 'actual_target_identity' in rec else [])
    target_ok=[]
    for t in targets:
        actual=ident(blob(t['commit'],t['path']))
        target_ok.append(all(t[k]==actual[k] for k in ['bytes','sha256']) and t['blob']==actual['git_blob'])
        contributions.append(dict(batch=rec['batch'],path=t['path'],actual_target_identity_matches=target_ok[-1]))
    receiptproof.append(dict(event=e['event_id'],receipt_commit=evidence['commit'],receipt_path=evidence['path'],receipt_identity=ident(raw),record_pointer=e['receipt_record_pointer'],accepted=rec['ACCEPTED'],closed=rec['CLOSED'],actual_artifact_matches_event=rec['actual_artifact_commit']==e['commit'],batch_matches=e['batches']==[rec['batch']],all_target_identities_equal=all(target_ok),target_count=len(targets)))
require('nine_events_and_registry_unchanged_parent',len(events)==9 and blob(C,P+'accepted-source-updates.json')==blob(B,P+'accepted-source-updates.json'))
require('nine_actual_receipts_accepted_not_closed_and_fixed_targets',len(receiptproof)==9 and all(r['accepted'] is True and r['closed'] is False and r['actual_artifact_matches_event'] and r['batch_matches'] and r['all_target_identities_equal'] for r in receiptproof))
require('39_issue_acceptance_29required10optional',len(required)==29 and len(optional)==10 and not required&optional)
bound=[f for f in m['features'] if f['upstream']['batches']]
require('230_bound_rows_accepted_events_complete',len(bound)==230 and all(set(f['upstream']['accepted_events']) and f['upstream']['status']=='已回填ACCEPTED源规格；去向待独立复审' for f in bound))
require('all230_binding_objects_exact_parent',all(f['upstream']==oldfeatures[f['feature_id']]['upstream'] for f in bound))
require('40_receipt_target_contributions',len(contributions)==40)
save('propagation-acceptance-conservation.json',dict(candidate=C,events=receiptproof,contributions=contributions,required_ids=sorted(required),optional_ids=sorted(optional),binding_rows=[dict(feature_id=f['feature_id'],upstream=f['upstream']) for f in bound]))

# Fresh author I/O differs for a legitimate input manifest and regenerated timestamps.
io_names=['revisions/r3/tools/accepted-binding-results.json','revisions/r3/tools/actual-command-io.json','revisions/r3/tools/actual-results.json','revisions/r3/tools/final-calibration-proof.json','revisions/r3/tools/navigation-results.json','revisions/r3/tools/preservation-results.json','revisions/r3/tools/source-guard-results.json']
io_proof=[]
for p in io_names:
    before=load(p,B); after=load(p);ds=diff(before,after)
    io_proof.append(dict(path=p,differing_pointers=[x['pointer'] for x in ds],complete_delta_in='propagation-full-pointer-delta.json'))
oldio=load('revisions/r3/tools/actual-command-io.json',B); newio=load('revisions/r3/tools/actual-command-io.json')
def argv_semantics(argv):
    return ['PYTHON' if i==0 else a[a.index(P):] if P in a else a for i,a in enumerate(argv)]
require('ten_author_suite_command_semantics_unchanged',len(newio['commands'])==10 and all(argv_semantics(a['argv'])==argv_semantics(b['argv']) for a,b in zip(oldio['commands'],newio['commands'])))
require('ten_author_suite_exit_stderr_unchanged',all(a['exit_code']==b['exit_code']==0 and a['stderr']==b['stderr']=='' for a,b in zip(oldio['commands'],newio['commands'])))
require('ten_author_suite_all17_input_hashes_stable',len(newio['initial_input_sha256'])==17 and all(x['input_sha256_before']==x['input_sha256_after']==newio['initial_input_sha256'] for x in newio['commands']))
require('ten_author_suite_only_manifest_patch_inputs_rebound',{k for k in oldio['initial_input_sha256'] if oldio['initial_input_sha256'][k]!=newio['initial_input_sha256'][k]}=={'routing-manifest.json','revisions/r3/source-refinement-patch.json'})
require('final_calibration15_check_results_unchanged',load('revisions/r3/tools/final-calibration-proof.json')['checks']==load('revisions/r3/tools/final-calibration-proof.json',B)['checks'] and len(load('revisions/r3/tools/final-calibration-proof.json')['checks'])==15)
require('final_calibration_counts_unchanged',load('revisions/r3/tools/final-calibration-proof.json')['counts']==load('revisions/r3/tools/final-calibration-proof.json',B)['counts'])
require('formal_tree_and_reference_unchanged',git('rev-parse',C+':deliverables/final-specification-set').decode().strip()=='f292698cdd4a8e725525a9be6dc34b75faaf151e' and not git('diff','--name-only',B,C,'--','deliverables/final-specification-set','reference'))
save('propagation-independent-proof.json',dict(candidate=C,parent=B,prior_review=PRIOR,current_source=CURRENT,checks=checks,all_passed=all(x['passed'] for x in checks),source_units=sourceproof,author_io_delta_summary=io_proof,counts=dict(changed_paths=len(paths),active=len(m['features']),metadata=len(m['metadata_records']),retired=len(m['retired_features']),historical_headings=len(actual_historical),current_headings=len(actual_current),new_headings=len(added),bindings=len(bound),events=len(events),contributions=len(contributions)),destination_counts=dict(collections.Counter(f['future_plan']['destination'] for f in m['features']))))
save('propagation-input-identities.json',dict(candidate=C,parent=B,prior_review=PRIOR,current_source=CURRENT,reading_credit='Complete fixed Git blobs mechanically parsed for identity, JSON object/field deltas, heading and archive replay. Semantic prose reading is separately stated in report; this ledger does not claim fresh full-document semantic review.',inputs=[dict(pointer=k,**v) for k,v in sorted(reads.items())]))
print(json.dumps(dict(checks=len(checks),passed=sum(x['passed'] for x in checks),failed=[x for x in checks if not x['passed']],manifest_sha256=sha(serialized),inputs=len(reads)),ensure_ascii=False,indent=2))
