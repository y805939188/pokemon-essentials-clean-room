"""Independent rational-number check of fixed WP43 vectors; no reference execution."""
from fractions import Fraction as Q
import json
from pathlib import Path

OUT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference/review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-CM')

def nearest_positive(value):
    value = Q(value)
    return (2 * value.numerator + value.denominator) // (2 * value.denominator)

def stat_scale(stage):
    return Q(2 + stage, 2) if stage >= 0 else Q(2, 2 - stage)

def accuracy_scale(stage):
    return Q(3 + stage, 3) if stage >= 0 else Q(3, 3 - stage)

def threshold(q, a, e, multiplier=Q(1)):
    acc = nearest_positive(100 * accuracy_scale(a) * multiplier)
    eva = max(1, nearest_positive(100 * accuracy_scale(e)))
    return acc, eva, q * acc // eva

def damage(level, power, attack, defense, attack_stage=0, defense_stage=0,
           power_multiplier=Q(1), final_multiplier=Q(1), critical=False):
    if critical:
        attack_stage = max(attack_stage, 0)
        defense_stage = min(defense_stage, 0)
    a = int(attack * stat_scale(attack_stage))
    d = int(defense * stat_scale(defense_stage))
    p = max(1, nearest_positive(power * power_multiplier))
    a, d = max(1, a), max(1, d)
    level_factor = int(Q(2 * level, 5) + 2)
    ratio_floor = int(Q(level_factor * p * a, d))
    base = ratio_floor // 50 + 2
    return [p, a, d, ratio_floor, base, max(1, nearest_positive(base * final_multiplier))]

checks = []
def check(identity, value, expected):
    assert value == expected, (identity, value, expected)
    checks.append({'id': identity, 'result': value, 'expected': expected,
                   'evidence': 'INDEPENDENT_RATIONAL_MODEL', 'reference_execution': False})

check('TD05', threshold(90, 0, 1), (100, 133, 67))
check('TD06', threshold(90, 6, -6), (300, 33, 818))
check('TD07', threshold(90, 0, 0, Q(5, 3) * Q(6, 5)), (200, 100, 180))
check('TD08', [r < 80 for r in [79, 80, 90]], [True, False, False])
check('TD12-low', damage(50, 40, 100, 100, final_multiplier=Q(3, 2)*Q(85, 100)), [40,100,100,880,19,24])
check('TD12-high', damage(50, 40, 100, 100, final_multiplier=Q(3, 2)), [40,100,100,880,19,29])
check('TD13-new', damage(50, 40, 100, 100, final_multiplier=Q(9, 4)), [40,100,100,880,19,43])
check('TD13-old', damage(50, 40, 100, 100, final_multiplier=Q(3)), [40,100,100,880,19,57])
check('TD14', damage(50, 75, 101, 103, -1, 1, Q(13, 10), Q(85, 100)), [98,67,154,938,20,17])
check('TD15', damage(50, 75, 101, 103, -1, 1, Q(13, 10), Q(3, 2), True), [98,101,103,2114,44,66])
check('TD16', damage(1, 0, 0, 0), [1,1,1,2,2,2])
check('TD17', damage(50, 40, 100, 100, final_multiplier=Q(3, 2)*Q(3, 4)*Q(1, 2)), [40,100,100,880,19,11])
check('TD18', min(50, 30), 30)
check('TD19-endure', min(50, 30)-1, 29)
check('TD19-substitute', min(50, 12), 12)
check('TD20-generation8', 80 // 8, 10)
check('TD21', [r < 70 for r in [69,70]], [True,False])
check('TD25-nonice', 30+50-50-10, 20)
check('TD25-ice', 30+50-50, 30)

result = {'bound_formal': 'deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md:13-35',
          'workspace_commit': '8ea169fbd0f33f378b5d732fd6bea59e854e04a6',
          'formal_tree': '1046fbb657882e84b3dfc6d017943a9edf7782e5',
          'mode': 'DERIVATION_AND_TOOL_VERIFICATION', 'checks': checks,
          'limitation': 'Not an actual battle, floating-point equivalence, random simulation, or hostDemo result.'}
(OUT / 'wp43-numeric-results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'checks': len(checks), 'passed': len(checks), 'mode': result['mode'], 'reference_executed': False}))
