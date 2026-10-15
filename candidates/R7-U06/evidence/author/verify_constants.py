"""Independent constant arithmetic only, without state transitions or reference code."""
from fractions import Fraction
import json

values = {
    'SNEASEL_base': 5 + 95//10,
    'MAGIKARP_base': 5 + 10//10,
    'TripleKick_three_evaluations': [10, 2*10, 3*10],
    'water_example_base_damage': ((2*20//5+2)*40*33//55)//50+2,
    'water_example_final_damage': 6*3,
    'water_example_remaining_HP': 100-18,
    'stage_negative4_plus6': min(-4+6,6),
    'stage_0_plus6': min(0+6,6),
    'stage_positive5_plus6': min(5+6,6),
    'speed_at_stage2': 35*Fraction(4,2),
    'speed_at_stage6': 35*Fraction(8,2),
}
assert list(values.values()) == [14,6,[10,20,30],6,18,82,2,6,6,70,140]
print(json.dumps({'stage':'TOOL_VALIDATION_CONSTANT_ARITHMETIC',
    'values':values,'behavior_vector_execution':'NOT_EXECUTED',
    'reference_or_behavior_model_processes':0},default=int))
