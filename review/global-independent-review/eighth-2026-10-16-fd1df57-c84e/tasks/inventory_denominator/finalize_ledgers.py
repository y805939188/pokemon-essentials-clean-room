#!/usr/bin/env python3
"""Record only reads actually performed in this context; no historic PASS reuse."""
import datetime
import hashlib
import json
from pathlib import Path
import re

OUT=Path(__file__).resolve().parent
B=Path('/workspace/pokemon-essentials-clean-room')
BC='fd1df570cad987dc3852a3b958f03916e317f7fe'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
identity={x['path']:x for x in json.loads((OUT/'b8-scoped-inventory.json').read_text())}
read_notes={
 'AGENTS.md':'Complete clean-room mission, source separation, architecture neutrality, documentation standard, workflow and completeness rules; no framework work and no source copying.',
 'planning/module-map.md':'All18 domains, seven classifications, primary-contract discipline, capture ownership split, configuration variants, Mega/Shadow/learning/call/obedience junctions, and knowledge-dependency route read.',
 'planning/extraction-plan.md':'All87 executable rows including five split families; Dependencies are completion knowledge, not runtime architecture or start barriers.84 content rows includeWP01;78/79/80 are review stages. All nine crosscuts and three local checkpoints read. Historical authorization statements do not override current user review contract.',
 'planning/coverage.md':'Complete287 lines read, including chronological B21/B20/B09/B08/B07/B04/B06/B03/B05/B02/B01/B14 andR5 layers. All historic432/312/33/84/113/1731 counts,34E-navigation,17NA,4supplements,9unread PBS sample dispositions and runtime/demo zero qualifications recovered as history only. None establishesR8 coverage.',
 'planning/feature-matrix.md':'Complete596 lines read; original113 feature rows,18domains and10 multi-WP feature mappings read; all historical R2/R3/R5/R6/R7 amended scope/status/normal/boundary/control clauses read. Final R7 current27/13 finite-static CLOSED supersedes old production-time candidates without erasure; noR8 PASS inherited.'}
ledger=[]
for path,note in read_notes.items():
    raw=(B/path).read_bytes();lines=raw.splitlines(keepends=True)
    ledger.append({'path':path,'repo':str(B),'commit':BC,'workspace_tree':identity[path]['workspace_tree'],
                   'git_blob':identity[path]['git_blob'],'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
                   'reader':'/root/inventory_denominator','read_status':'FULL_READ','ranges':[[1,len(lines)]],
                   'remaining_ranges':[],'semantic_scope':note,'source_fact_or_formal_clause_acceptance':False,
                   'evidence_location':'Actual platform tools exec_command outputs in this context; raw per-call UTC/stdout/stderr not separately captured locally before this ledger; no retroactive execution provenance invented'})

path='planning/review-manifest-2026-09-19.md'
raw=(B/path).read_bytes();manifest_raw=raw;lines=raw.splitlines(keepends=True)
ranges=[[1,65],[1835,1932],[2795,2848],[4115,4127]]
unread=[[66,1834],[1933,2794],[2849,4114]]
ledger.append({'path':path,'repo':str(B),'commit':BC,'workspace_tree':identity[path]['workspace_tree'],
               'git_blob':identity[path]['git_blob'],'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
               'reader':'/root/inventory_denominator','read_status':'MIXED_FULL_READ_AND_INVENTORY_ONLY_HISTORY','ranges':ranges,
               'remaining_current_semantic_ranges':[], 'not_semantically_read_history_ranges':unread,
               'read_lines':sum(b-a+1 for a,b in ranges),
               'inventory_only_history_lines':sum(b-a+1 for a,b in unread),
               'current_qualification_full_read_ranges':[[1,4],[1913,1918],[2801,2827],[4115,4127]],
               'semantic_scope':'First historical version entries; entire1835–1932 historical correspondence and initial2.2 provenance limits; full3.1 identity correction; fullfinalB21 errata. Other historic identity/navigation/snapshot fields receive complete type/identity disposition, not semantic reading credit. See manifest-purpose-disposition.json. Initial1835–1912 oversized output truncated; credited only after smaller continuous re-reads.',
               'source_fact_or_formal_clause_acceptance':False})

for entry in json.loads((OUT/'r6-retained-and-small-identities.json').read_text()):
    if '/inputs/' in entry['path']:
        raw=(B/entry['path']).read_bytes()
        ledger.append(dict(entry,reader='/root/inventory_denominator',read_status='FULL_READ',
                 ranges=[[1,len(raw.splitlines())]],remaining_ranges=[],
                 semantic_scope='All fields; exactB8/9aa bytes equal, linked read not two independent reviewers. See r6-small-payload-reading.json.',
                 source_fact_or_formal_clause_acceptance=False))
ledger.append({'path':'Library:eighth-global-review-prompt.md','library_file_id':'libfile_f8ff592304d081918512f51317a8ecee',
               'read_status':'FULL_READ','ranges':[[1,180],[181,241]],'remaining_ranges':[],
               'reported_size_bytes':36653,'expected_sha256':'63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b',
               'local_original_byte_sha256':'UNVERIFIED_NO_MATERIALIZED_ORIGINAL_BYTES',
               'reader':'/root/inventory_denominator','evidence':['contract-library-read-001-180.json','contract-library-read-181-241.json'],
               'qualification':'Both structured reads show no warnings, second has_more false. No Library download retried.'})

result={'schema':'gr8-reading-ledger/v1','task':'inventory_denominator','updated_utc':now,'entries':ledger,
        'configuration':{'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'Fast off'},
                         'actual':{k:'UNVERIFIED' for k in ['model','effort','tier','speed']}},
        'logical_platform_name':'/root/inventory_denominator','opaque_platform_agent_session_id':'UNVERIFIED',
        'platform_status_last_observed':'running via collaboration.list_agents; no opaque ID/config echo',
        'reference_source_read_credit_this_task':0,'formal_semantic_read_credit_this_task':0,
        'qualification':'Other named reviewer read ledgers are separate evidence. Their live state is not overwritten by this coordinator ledger.',
        'update_started':False}
(OUT/'reading-ledger.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')

# A complete structural index is explicitly a mechanical disposition of every line.
blocks=[];start=1;kind=None
for n,line in enumerate(lines,1):
    text=line.decode(errors='replace')
    k='heading' if re.match(r'^#{1,6} ',text) else 'table_row' if text.startswith('|') else 'prose_or_list' if text.strip() else 'blank'
    if k!=kind and kind is not None:
        blocks.append({'start_line':start,'end_line':n-1,'kind':kind,'semantic_status':'SEE_READING_LEDGER_ONLY'})
        start=n
    kind=k
blocks.append({'start_line':start,'end_line':len(lines),'kind':kind,'semantic_status':'SEE_READING_LEDGER_ONLY'})
(OUT/'manifest-structural-index.json').write_text(json.dumps({'path':path,'whole_file_bytes':len(manifest_raw),
    'qualification':'Mechanical line-kind segmentation only, no semantic reading credit','blocks':blocks,
    'semantic_read_ranges':ranges,'not_semantically_read_history_ranges':unread},ensure_ascii=False,indent=2)+'\n')
sections=[{'start_line':1,'end_line':5,'type':'registry_purpose_and_self_hash_boundary','current_use':'provenance qualification, fully read'},
 {'start_line':6,'end_line':1834,'type':'dated_original_WP80_171_version_identity_index','current_use':'historical restoration index; not B8 formal identities or current behavior primary'},
 {'start_line':1835,'end_line':1912,'type':'original_WP_review_hash_correspondence','current_use':'dated historical qualification only; read but no B8 approval transfer'},
 {'start_line':1913,'end_line':2079,'type':'historical_version_relation_and_evidence_limits','current_use':'1913–1918 provenance limitations fully read; dated old rounds are restoration navigation'},
 {'start_line':2080,'end_line':2800,'type':'explicitly_superseded_historical_identity_rows','current_use':'historical identity keys only; no original artifact identity silently upgraded to B8'},
 {'start_line':2801,'end_line':2827,'type':'CLOSURE_R01_18_identity_errata','current_use':'fully read; old rows retained, exact eighteen superseded metadata fields and frozen-context qualification retained'},
 {'start_line':2828,'end_line':4114,'type':'dated_rounds_1_to_171_historical_delivery_snapshots','current_use':'historical production-time summaries; old behavior excerpts/cases not current primary, authoritative B8 formal and exact successor records are separately reviewed'},
 {'start_line':4115,'end_line':4127,'type':'B21_successor_erratum_and_qualification','current_use':'fully read; explicitly says earlier hash/status rows retain their time and do not identify newer bytes'}]
line_rows=[]
for n,line in enumerate(lines,1):
    text=line.decode('utf-8')
    sr=next(s for s in sections if s['start_line']<=n<=s['end_line'])
    was_read=any(a<=n<=b for a,b in ranges)
    line_rows.append({'line':n,'byte_start':sum(len(v) for v in lines[:n-1]),'bytes':len(line),
        'sha256':hashlib.sha256(line).hexdigest(),'section_type':sr['type'],
        'literal_path_keys':re.findall(r'`([^`\n]*[/\\][^`\n]*)`',text),
        'full_sha256_keys':re.findall(r'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])',text),
        'disposition':'FULL_READ_DOCUMENT_ONLY' if was_read else 'INVENTORY_ONLY_HISTORICAL_NAVIGATION',
        'reason':sr['current_use'],'semantic_credit':was_read,'B8_behavior_approval_credit':False})
(OUT/'manifest-purpose-disposition.json').write_text(json.dumps({'schema':'gr8-manifest-purpose/v1',
    'path':path,'commit':BC,'bytes':len(manifest_raw),'sha256':hashlib.sha256(manifest_raw).hexdigest(),
    'git_blob':identity[path]['git_blob'],'sections':sections,'lines':line_rows,
    'full_read_lines':230,'inventory_only_history_lines':3897,'all_lines_disposed':len(line_rows)==4127,
    'current_qualification_unread_lines':0,
    'scope_authority':'Root confirmed original prompt permits complete type/identity disposition for noncurrent historical index; actual current semantic fields must be read.',
    'qualification':'Complete structure/type/identity treatment, not FULL_READ of whole file. Dated case excerpts do not create independent B8 primary behavior or new approval; B8 clauses and exact R7/R6 successors remain in named reviewer readsets.',
    'negative_navigation_search':'No literal B8 commit/formal tree, R6/R7 labels or GR7 entries found by bounded rg search; search is routing evidence only, not semantic completeness proof.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'full_document_reads':5,'historical_small_version_entries':8,'manifest_read_lines':230,'manifest_inventory_only_history_lines':3897,'manifest_current_qualification_unread':0},ensure_ascii=False))
