"""Read-only structural validation of the explicit audit inputs and own outputs.
This script neither executes reference source nor assigns semantic PASS.
"""
import collections
import json
import pathlib
import re
import subprocess

ROOT=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=ROOT/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-CA/subtasks/effects-c'
forward=[json.loads(x) for x in (OUT/'forward-matrix.jsonl').read_text().splitlines()]
ledger=[json.loads(x) for x in (OUT/'reading-ledger.jsonl').read_text().splitlines()]
summary=[]
required={
 'reference/pokemon-essentials/Data/Scripts/011_Battle/006_AI MoveEffects/007_AI_MoveEffects_Items.rb':376,
 'reference/pokemon-essentials/Data/Scripts/011_Battle/006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb':628,
 'reference/pokemon-essentials/Data/Scripts/011_Battle/006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb':877,
 'deliverables/final-specification-set/combat-requirements/wp52-c-items-calling-and-control-evaluation.md':208,
 'deliverables/final-specification-set/combat-requirements/wp52-c-item-control-coverage-and-data.md':191,
 'deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md':294,
 'deliverables/final-specification-set/combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md':240,
 'deliverables/final-specification-set/combat-requirements/wp52-b-effect-coverage.md':111,
}
for path,total in required.items():
    covered=set()
    for r in ledger:
        if r.get('kind')=='actual_contiguous_read' and r['path']==path:
            covered.update(range(r['start'],r['end']+1))
    missing=sorted(set(range(1,total+1))-covered)
    assert not missing,(path,missing)
    summary.append({'path':path,'expected_lines':total,'actual_read_missing_lines':missing,
        'classification':'READ_COVERAGE_ONLY_SEMANTIC_STATUS_SEPARATE'})

# Detect other literal registrations of assigned identities anywhere in the
# complete AI-effect directory; retain text locations for audit and manually
# interpret absent/cross-registry sources rather than treating all as callable.
identities={r['registration']['destination_identity'] for r in forward}
hits=[]
directory=ROOT/'reference/pokemon-essentials/Data/Scripts/011_Battle/006_AI MoveEffects'
for p in sorted(directory.glob('*.rb')):
    text=p.read_text()
    for match in re.finditer(r'Handlers::(\w+)\.(add|copy)\(\s*"([^"]+)"',text):
        names=[match.group(3)]
        if match.group(2)=='copy':
            closing=text.index(')',match.end())
            names+=re.findall(r'"([^"]+)"',text[match.end():closing])
        if not identities.intersection(names):continue
        # This is only a locator. Handler bodies are never parsed as semantics.
        line=text.count('\n',0,match.start())+1
        hits.append({'path':str(p.relative_to(ROOT)),'start':line,'receiver':match.group(1),
            'operation':match.group(2),'literal_ids':names,'classification':'INVENTORY_ONLY'})
(OUT/'cross-registration-inventory.json').write_text(json.dumps(hits,ensure_ascii=False,indent=2)+'\n')
report={'actual_read_coverage':summary,'hand_written_semantic_rows':len(forward),
 'by_source':dict(collections.Counter(r['source']['path'] for r in forward)),
 'total_missing_read_lines':0,'structural_only':True,'reference_execution':False,
 'independent_model_execution':False,'full_host_demo':False}
(OUT/'tool-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
