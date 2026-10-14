"""Structural QA only: range continuity, JSON and exact local denominator coverage.

Does not execute reference or score semantic correctness. Writes only here.
"""
import collections
import hashlib
import json
from pathlib import Path

ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=Path(__file__).resolve().parent
ledger=[json.loads(line) for line in (OUT/'reading-ledger.jsonl').read_text().splitlines() if line]
required={
 'AGENTS.md':297,
 'reference/pokemon-essentials/Data/Scripts/011_Battle/006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb':1559,
 'reference/pokemon-essentials/Data/Scripts/011_Battle/006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb':531,
 'reference/pokemon-essentials/Data/Scripts/011_Battle/006_AI MoveEffects/006_AI_MoveEffects_Healing.rb':683,
 'deliverables/final-specification-set/combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md':240,
 'deliverables/final-specification-set/combat-requirements/wp52-b-effect-coverage.md':111,
 'deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md':294,
}
coverage=[]
for path,total in required.items():
    raw=(ROOT/path).read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    assert len(raw.decode('utf-8-sig').splitlines())==total
    entries=[e for e in ledger if e['path']==path and e['stage']=='range_emitted_not_semantic_pass']
    seen=set()
    for e in entries:
        assert e['sha256']==digest,(path,'input drift')
        assert (OUT/e['log']).is_file()
        seen.update(range(e['start'],e['end']+1))
    gaps=sorted(set(range(1,total+1))-seen)
    assert not gaps,(path,gaps)
    coverage.append(dict(path=path,total_lines=total,unread_lines=len(gaps),sha256=digest,
                         validation='RANGE_LOG_CONTINUITY_ONLY_NOT_SEMANTIC_APPROVAL'))
inventory=json.loads((OUT/'structural-inventory.json').read_text())
forward=json.loads((OUT/'forward-matrix.json').read_text())
reverse=json.loads((OUT/'reverse-matrix.json').read_text())
vectors=json.loads((OUT/'vector-matrix.json').read_text())
findings=json.loads((OUT/'findings.json').read_text())
assert len(inventory)==len(forward)==203
assert len({r['id'] for r in forward})==203
assert {r['id'] for r in forward}=={r['id'] for r in inventory}
assert all(r.get('fact') and r.get('consumer') and r.get('upstream_precondition') and r.get('formal_clause') and r.get('boundary') for r in forward)
assert len(vectors)==56 and len({r['id'] for r in vectors})==56
assert len(findings)==2 and all('ROOT' in f['status'] for f in findings)
result=dict(validation='STRUCTURAL_COMPLETE_WITH_UNADJUDICATED_PROPOSALS',
            not_semantic_approval=True,input_drift_detected=False,range_coverage=coverage,
            registration_denominator=203,semantic_rows=203,unmapped_units=0,
            reverse_rows=len(reverse),local_vectors=len(vectors),proposals=len(findings),
            statuses=dict(collections.Counter(r['status'] for r in forward)),
            executed_reference=False,executed_independent_model=False,complete_host_demo=False)
(OUT/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['range_coverage','statuses']},ensure_ascii=False))
