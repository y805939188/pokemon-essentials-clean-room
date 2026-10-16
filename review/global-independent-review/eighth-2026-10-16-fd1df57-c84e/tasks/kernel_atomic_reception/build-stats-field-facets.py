"""Review metadata only: exact manually selected declaration/default/save/use facets."""
from pathlib import Path
import datetime
import json
import re

BASE = Path(__file__).resolve().parent
ROOT = Path('/workspace/pokemon-essentials-clean-room')
FORMAL = 'deliverables/final-specification-set/generic-kernel/wp06-stats-directory.md'
lines = (ROOT / FORMAL).read_text().splitlines()
stats = Path('/workspace/pokemon-essentials/Data/Scripts/004_Game classes/012_Game_Stats.rb').read_text()
consumers = json.loads((BASE / 'consumer-candidate-dispositions.json').read_text())['records']
rows = []
for number, line in enumerate(lines, 1):
    if not line.startswith('| '):
        continue
    cells = [value.strip() for value in line.strip('|').split('|')]
    if len(cells) == 7 and re.fullmatch('[a-z_]+', cells[0]):
        rows.append((number, cells))
assert len(rows) == 74
declared = set()
for line in stats.split('class Game_Temp', 1)[0].splitlines():
    if 'attr_accessor ' in line or 'attr_writer ' in line:
        declared.update(re.findall(r':([a-z_]+)', line.split('#')[0]))
assert {cells[0] for _, cells in rows} == declared
atoms = []
for number, cells in rows:
    name, shape, initial, update, persistence, evidence, owner = cells
    default = ('fresh50-element zero array' if name == 'gym_leader_attempts'
               else 'fresh empty array' if name == 'times_to_get_badges' else 'numeric0')
    facets = [
        ('DECLARATION', f'{name} is one of74 declared stored GameStats fields.', 'accessor/writer declarations'),
        ('INITIAL', f'GameStats constructor initializes {name} to {default}.', 'GameStats.initialize'),
        ('PERSIST', f'{name} is on the whole GameStats object saved/loaded by :stats registration, not separately serialized by this declaration.', 'SaveData :stats and Value save/load'),
    ]
    for facet, claim, unit in facets:
        sources = [{'path': 'Data/Scripts/004_Game classes/012_Game_Stats.rb',
                    'complete_unit': unit, 'reader': '/root/kernel_atomic_reception', 'whole_file_read': True}]
        if facet == 'PERSIST':
            sources += [
                {'path': 'Data/Scripts/002_Save data/004_Game_SaveValues.rb', 'complete_unit': 'stats registration120–127', 'reader': '/root/kernel_atomic_reception', 'whole_file_read': True},
                {'path': 'Data/Scripts/002_Save data/002_SaveData_Value.rb', 'complete_unit': 'Value save/load and ordered compile/load helpers', 'reader': '/root/kernel_atomic_reception', 'whole_file_read': True},
            ]
        atoms.append({'id': f'KAR-WP06-STATS-{name}-{facet}',
                      'formal': {'path': FORMAL, 'lines': [number], 'exact_text': lines[number - 1]},
                      'assertion': claim, 'source_complete_units': sources,
                      'source_status': 'EXACT_FIELD_DECLARATION_DEFAULT_OR_SAVE_WIRING_RECONCILED',
                      'reception_status': 'OWN_FULL_NAMED_UNITS',
                      'premise': 'FixedR/B8 default registrations, legal standard GameStats/SaveData objects. Native Marshal/file effects NOT_EXECUTED; recursive field validity/alias equality not inferred.',
                      'target_behavior': 'NOT_EXECUTED'})
    candidates = [item for item in consumers if item['kind'] != 'settings' and item['symbol'] == name]
    accepted = [item for item in candidates if item['status'].startswith('RECEIVED_')]
    pending = [item['id'] for item in candidates if item['status'] == 'OPEN_NOT_YET_SEMANTICALLY_RECEIVED']
    state = ('EXPLICIT_U01_MISSING_EVENT_CALLER' if 'U01' in evidence
             else 'READABLE_ASSIGNMENT_CALLER_UNPROVED' if name in ['time_to_enter_hall_of_fame', 'times_to_get_badges']
             else 'WRITER_SOURCE_UNLOCATED_NO_EVENT_INFERENCE' if name == 'battle_points_won'
             else 'FINITE_NAMED_CONSUMERS_RECEIVED_REMAINDER_OPEN')
    atoms.append({'id': f'KAR-WP06-STATS-{name}-UPDATE-SEMANTICS',
                  'formal': {'path': FORMAL, 'lines': [number], 'exact_text': lines[number - 1]},
                  'assertion': f'{name} unit/shape category {shape}; update category {update}; responsibility {owner}.',
                  'source_status': state, 'reception_status': state,
                  'full_original_finite_consumer_records': accepted,
                  'exact_unreceived_candidate_ids': pending,
                  'pending': 'Meanings not entailed by complete named consumer facts remain OPEN; completion-category wording not upgraded to iff-success/rollback. U01 comments are not verified event reachability. Composite refinement still required before final atomic denominator.',
                  'evidence_qualifier': evidence,
                  'premise': 'FixedR/B8 and each original complete consumer premise; actual writer timing separate from declaration/default. Native/Demo/event reachability not certified.',
                  'target_behavior': 'NOT_EXECUTED'})
payload = {'schema': 'gr8-kernel-stats-directory-explicit-field-atoms/v1',
           'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'records': atoms,
           'manual_records_selected_after_complete_formal_and_source_read': True,
           'field_set_equality_checked_only_as_membership_verification': True,
           'fields': 74, 'explicit_facets': len(atoms), 'global_or_chapter_semantic_denominator_frozen': False,
           'remaining': 'Update-category composites, missing actual consumers, negative-source premise and primarydomain reverse joins remain continued work.'}
(BASE / 'wp06-stats-directory-manual-field-atoms.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print('74 selected field declaration/default/persist/use facets:', len(atoms))
