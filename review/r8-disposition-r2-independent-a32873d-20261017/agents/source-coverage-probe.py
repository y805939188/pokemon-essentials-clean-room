#!/usr/bin/env python3
"""Synthetic static function probe; never applies or creates author current data."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
sys.dont_write_bytecode=True
ROOT=Path('/workspace/r8-disposition-r2-review')
INV=ROOT/'planning/implementation-routing/r8-20261017'
OUT=ROOT/'review/r8-disposition-r2-independent-a32873d-20261017/agents'
spec=importlib.util.spec_from_file_location('independent_coverage',INV/'revisions/r2/tools/current-coverage-check.py')
cc=importlib.util.module_from_spec(spec);spec.loader.exec_module(cc)
m=json.loads((INV/'routing-manifest.json').read_text())
schema=json.loads((INV/'current-section-coverage.schema.json').read_text())
old=json.loads((INV/'section-coverage.json').read_text())
docs={d['document_id']:d for d in m['documents']}
fields=['document_id','path','level','title','anchor','line_start','line_end','heading_sha256','feature_refs']
data={'schema_version':'routing-current-section-coverage.v1','snapshot':copy.deepcopy(m['current_snapshot']),
      'source_baseline_commit':cc.r.B8,'qualification':'INDEPENDENT SYNTHETIC STATIC FIXTURE ONLY','sections':[]}
for s in old['sections']:
    row={k:s[k] for k in fields}
    row.update(metadata_refs=s.get('metadata_refs',[]),coverage_scope=s.get('coverage_scope','EXPLICIT_SOURCE_FUNCTIONS_OR_METADATA'),
        metadata_reason=s.get('metadata_reason') or 'Independent fixture normalization: explicit existing functional mapping',
        mapping_basis='RETAIN_EXPLICIT_SOURCE_MAPPING_BY_UNCHANGED_ANCHOR; not a new source quotation',
        accepted_events=docs[s['document_id']]['upstream']['accepted_events'])
    data['sections'].append(row)
baseline=cc.check(data,m,schema)
idx=next(i for i,s in enumerate(data['sections']) if s['path'].endswith('/combat-requirements/wp39-battle-context-and-participants.md') and s['title']=='4. 战斗初始化与布局')
before=copy.deepcopy(data['sections'][idx])
data['sections'][idx].update(feature_refs=[],metadata_refs=[],coverage_scope='ALL_FORMAL_FEATURES')
found=cc.check(data,m,schema)
result={'scope':'ISOLATED_SYNTHETIC_FUNCTION_PROBE_NOT_ACTUAL_CURRENT_FULL_RUN',
        'argv':['python',str(Path(__file__).relative_to(ROOT))],
        'fixture_snapshot':m['current_snapshot']['commit'],'baseline_errors':baseline,
        'mutation_before':before,'mutation_after':data['sections'][idx],'mutated_errors':found,
        'blank_behavior_heading_accepted':not found,'current_2704_full_check_run':False,
        'author_apply_executed':False,'first_attempt':'Read-only stdin fixture builder failed on missing optional coverage_scope. Exact backfill-default construction then exposed 1776 null metadata_reason schema errors (separate artifact); this scope-only fixture explicitly normalizes those null reasons to isolate ALL_FORMAL_FEATURES behavior.',
        'checker_sha256':cc.r.digest((INV/'revisions/r2/tools/current-coverage-check.py').read_bytes()),
        'schema_sha256':cc.r.digest((INV/'current-section-coverage.schema.json').read_bytes())}
(OUT/'source-coverage-scope-probe.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['mutation_before','mutation_after']},ensure_ascii=False,indent=2))
