#!/usr/bin/env python3
"""Reproduce exact inherited coverage relation/schema incompatibility without apply."""
import importlib.util
import json
from pathlib import Path
import sys
import jsonschema
sys.dont_write_bytecode=True
ROOT=Path('/workspace/r8-disposition-r2-review')
INV=ROOT/'planning/implementation-routing/r8-20261017'
OUT=ROOT/'review/r8-disposition-r2-independent-a32873d-20261017/agents'
old=json.loads((INV/'section-coverage.json').read_text())
schema=json.loads((INV/'current-section-coverage.schema.json').read_text())
manifest=json.loads((INV/'routing-manifest.json').read_text())
docs={d['document_id']:d for d in manifest['documents']}
sections=[]
for prior in old['sections']:
    # These get/default expressions intentionally match backfill lines 183-186.
    relation={'feature_refs':prior['feature_refs'],'metadata_refs':prior.get('metadata_refs',[]),
              'coverage_scope':prior.get('coverage_scope','EXPLICIT_SOURCE_FUNCTIONS_OR_METADATA'),
              'metadata_reason':prior.get('metadata_reason','Retained explicit source functional mapping')}
    h={k:prior[k] for k in ['document_id','path','level','title','anchor','line_start','line_end','heading_sha256']}
    h.update(relation,mapping_basis='RETAIN_EXPLICIT_SOURCE_MAPPING_BY_UNCHANGED_ANCHOR; not a new source quotation',
             accepted_events=docs[prior['document_id']]['upstream']['accepted_events'])
    sections.append(h)
data={'schema_version':'routing-current-section-coverage.v1','snapshot':manifest['current_snapshot'],
      'source_baseline_commit':'fd1df570cad987dc3852a3b958f03916e317f7fe','sections':sections,
      'qualification':'INDEPENDENT SYNTHETIC STATIC RELATION/SCHEMA PROBE'}
errors=list(jsonschema.Draft202012Validator(schema).iter_errors(data))
result={'scope':'EXACT_BACKFILL_RELATION_CONSTRUCTION_STATIC_SCHEMA_PROBE_ONLY',
        'argv':['python',str(Path(__file__).relative_to(ROOT))],
        'source_expression':'prior.get(metadata_reason, default) preserves an explicit JSON null',
        'historical_sections':len(old['sections']),'null_metadata_reason_count':sum(s['metadata_reason'] is None for s in sections),
        'schema_error_count':len(errors),'schema_error_examples':[{'pointer':'/'+('/'.join(map(str,e.path))),
            'error':e.message,'section':sections[e.path[1]]['title']} for e in errors[:5]],
        'all_errors_null_metadata_reason':all(e.path[-1]=='metadata_reason' and e.instance is None for e in errors),
        'current_2704_full_check_run':False,'author_apply_executed':False}
(OUT/'source-coverage-null-reason-summary.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
