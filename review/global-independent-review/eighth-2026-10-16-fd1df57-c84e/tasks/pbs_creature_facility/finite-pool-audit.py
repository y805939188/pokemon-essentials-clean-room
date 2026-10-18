"""Finite data projection and graph certificates, never execute reference behavior.

The graph criterion is mathematical: a team satisfying distinct species and
nonempty-item identities is a matching from species to item. An absent held item
has a private right vertex for that species. Duplicate source occurrences retain
their sampling weight but do not change existence of a matching.
"""
from pathlib import Path
import collections
import hashlib
import json

HERE = Path(__file__).parent
REF = Path('/workspace/pokemon-essentials')

def write(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def templates(path):
    result = []
    for line_no, line in enumerate((REF / path).read_text(encoding='utf-8-sig').splitlines(), 1):
        if not line or line.startswith('#'):
            continue
        species, item, nature, evs, moves = line.strip().split(';')
        result.append(dict(index=len(result), line=line_no, species=species, item=item or None,
                           nature=nature, evs=evs.split(','), moves=moves.split(','),
                           raw_item=item or None, raw_moves=moves.split(',')))
    return result

def certificate(rows, item_clause=True):
    edges = collections.defaultdict(dict)
    for row in rows:
        right = row['item'] if row['item'] and item_clause else '@free:' + row['species']
        edges[row['species']].setdefault(right, row['index'])
    held = {}
    def augment(species, visited):
        for item, row_index in edges[species].items():
            if item in visited:
                continue
            visited.add(item)
            if item not in held or augment(held[item][0], visited):
                held[item] = (species, row_index)
                return True
        return False
    for species in edges:
        augment(species, set())
    return dict(maximum_matching=len(held), witness_rows=[v[1] for v in held.values()])

def main():
    raw = json.loads((HERE / 'trainer-structure.json').read_text())
    traits_doc = json.loads((HERE / 'subreviews/trait_eligibility/finite-traits.json').read_text())
    traits = collections.defaultdict(list)
    for row in traits_doc['records']:
        if row['dataset'] == 'default' and row['template_created_this_form']:
            traits[row['species']].append(row)
    pairs = {
        'PBS/battle_tower_trainers.txt': 'PBS/battle_tower_pokemon.txt',
        'PBS/cup_fancy_trainers.txt': 'PBS/cup_fancy_pkmn.txt',
        'PBS/cup_fancy_trainers_single.txt': 'PBS/cup_fancy_pkmn_single.txt',
        'PBS/cup_little_trainers.txt': 'PBS/cup_little_pkmn.txt',
        'PBS/cup_pika_trainers.txt': 'PBS/cup_pika_pkmn.txt',
        'PBS/cup_poke_trainers.txt': 'PBS/cup_poke_pkmn.txt',
    }
    data = {f: templates(f) for f in pairs.values()}
    predicates = {
        'all_normal': None, 'standard': 'standard_non_egg', 'fancy': 'fancy_species_cold',
        'little_factory': 'little_factory_species_cold', 'little_direct': 'little_direct_species_cold',
        'light_direct': 'light_direct_species_cold', 'strict_little': 'strict_species_cold',
        'factory': 'factory_species',
    }
    def eligibility(row, name):
        options = traits[row['species']]
        assert options, ('missing creation-form predicate', row['species'])
        values = [True if predicates[name] is None else x[predicates[name]] for x in options]
        if name == 'strict_little' and (row['item'] in ['BERRYJUICE', 'DEEPSEATOOTH'] or
                                       any(m in ['SONICBOOM', 'DRAGONRAGE'] for m in row['moves'])):
            values = [False] * len(values)
        return all(values), any(values)
    # IDs here are projections, not calls to the reference registries.
    ids = {}
    for kind, file in [('species', 'PBS/pokemon.txt'), ('items', 'PBS/items.txt'), ('moves', 'PBS/moves.txt'), ('trainer_types', 'PBS/trainer_types.txt')]:
        ids[kind] = {s[1:-1] for s in (REF / file).read_text(encoding='utf-8-sig').splitlines() if s.startswith('[')}
    all_rows = [r for rows in data.values() for r in rows]
    literals = {
        'species': sorted({r['species'] for r in all_rows}),
        'items': sorted({r['raw_item'] for r in all_rows if r['raw_item']}),
        'moves': sorted({m for r in all_rows for m in r['raw_moves'] if m}),
        'trainer_types': sorted({r['fields']['Type']['value'] for r in raw['source_records']}),
    }
    write('literal-validation.json', dict(evidence='TOOL_VALIDATION', behavior='NOT_EXECUTED',
          unique_counts={k: len(v) for k, v in literals.items()}, literals=literals,
          absent={k: sorted(set(v) - ids[k]) for k, v in literals.items()},
          premise='Current default PBS headers, no alternate profile or plugin registration; existence is not eligibility or execution.'))
    normalization = []
    for file, table in data.items():
        for row in table:
            if row['item'] and row['item'] not in ids['items']:
                row['item'] = None
            row['moves'] = [m for m in row['moves'][:4] if m in ids['moves']]
            # All current source rows retain at least one valid move, so the
            # source's first-registry-move fallback is not reached here.
            assert row['moves'], ('empty valid moves', file, row['index'])
            if row['raw_item'] != row['item'] or row['raw_moves'] != row['moves']:
                normalization.append(dict(file=file, index=row['index'], line=row['line'],
                                          raw_item=row['raw_item'], item=row['item'],
                                          raw_moves=row['raw_moves'], moves=row['moves']))
    write('template-default-normalization.json', dict(evidence='SOURCE_STATIC_WITH_TOOL_VALIDATION',
          behavior='NOT_EXECUTED', premise='Default registered headers and no plugin aliases; fromInspected drops unknown item/moves. Empty trailing move slots are omitted.',
          raw_literal_inventory='literal-validation.json', normalized_held_ids=sorted({r['item'] for r in all_rows if r['item']}),
          differences=normalization))
    rows_out = []
    summary = {}
    for record in raw['source_records']:
        file = record['file']; candidates = [int(x) for x in record['fields']['PokemonNos']['value'].split(',')]
        table = data[pairs[file]]
        assert all(0 <= i < len(table) for i in candidates)
        item = dict(file=file, trainer_index=len([x for x in rows_out if x['file'] == file]),
                    original_section=record['section'], source_range=[record['start'], max(v['line'] for v in record['fields'].values())],
                    candidates=candidates, candidate_occurrences=len(candidates), predicates={})
        for name in predicates:
            kinds = {}
            for quantifier, take in [('every_creation_form', 0), ('some_creation_form', 1)]:
                eligible = [table[i] for i in candidates if eligibility(table[i], name)[take]]
                cert = certificate(eligible, name != 'strict_little')
                cert['eligible_occurrences'] = len(eligible)
                cert['eligible_template_indices'] = list(dict.fromkeys(r['index'] for r in eligible))
                kinds[quantifier] = cert
            item['predicates'][name] = kinds
        rows_out.append(item)
    for file, pokemon_file in pairs.items():
        sub = [r for r in rows_out if r['file'] == file]
        summary[file] = {'trainers': len(sub), 'templates': len(data[pokemon_file]), 'profiles': {}}
        for name in predicates:
            selected = [r['predicates'][name]['every_creation_form'] for r in sub]
            summary[file]['profiles'][name] = {
                'minimum_matching': min(x['maximum_matching'] for x in selected),
                'no_team3_trainer_indices': [r['trainer_index'] for r in sub if r['predicates'][name]['some_creation_form']['maximum_matching'] < 3],
                'no_robust_team4_trainer_indices': [r['trainer_index'] for r in sub if r['predicates'][name]['every_creation_form']['maximum_matching'] < 4],
                'form_condition_changes_graph': [r['trainer_index'] for r in sub if r['predicates'][name]['some_creation_form'] != r['predicates'][name]['every_creation_form']],
            }
    write('finite-pool-certificates.json', dict(schema='gr8.pbs-facility.finite-pools/v1',
          qualification='TOOL_VALIDATION over SOURCE_STATIC peer traits; cold/consistent species caches and current default headers required; independent graph argument in review.md. No reference/model/host behavior executed.',
          traits_input_sha256=hashlib.sha256((HERE / 'subreviews/trait_eligibility/finite-traits.json').read_bytes()).hexdigest(),
          records=rows_out, summary=summary))
    write('finite-pool-summary.json', summary)
    # Complete 15 disjoint nonnegative win bands plus the negative branch.
    thresholds = [(0,0,100),(6,80,40),(7,80,40),(13,120,20),(14,100,40),(20,140,20),(21,120,40),(27,160,20),(28,140,40),(34,180,20),(35,160,40),(41,200,20),(42,180,40),(48,220,40),(49,200,100)]
    bands = {}
    for n in (200, 300):
        all_indices = set(); values=[]
        for j,(wins,start,length) in enumerate(thresholds):
            a=start*n//300; count=length*n//300; all_indices.update(range(a,a+count))
            values.append(dict(win_lower=wins, win_upper=thresholds[j+1][0]-1 if j+1<len(thresholds) else None,
                               first_index=a, last_index=a+count-1, count=count))
        bands[n]=dict(bands=values, absent_trainer_indices=sorted(set(range(n))-all_indices), negative_wins_return=0)
    write('trainer-selection-domain.json', dict(evidence='DERIVED_VECTOR', behavior='NOT_EXECUTED', domains=bands))
    factory=[]
    low=[(0,173),(174,272),(273,371),(372,491),(492,610),(611,729),(730,849),(372,881)]
    high=[(372,491),(492,610),(611,729),(730,849)]+[(372,881)]*4
    for file, table in data.items():
        for level_mode, domains in [('ordinary',low),('maximum_level',high)]:
            for group,(a,z) in enumerate(domains):
                lo=a*len(table)//881;hi=z*len(table)//881
                valid=[r for r in table[max(lo,0):min(hi+1,len(table))] if eligibility(r,'factory')[0]]
                cert=certificate(valid)
                factory.append(dict(file=file, N=len(table), level_mode=level_mode, group=group,
                                    domain=[lo,hi], missing_indices=[i for i in range(lo,hi+1) if i>=len(table)],
                                    valid_domain_matching=cert,
                                    arbitrary_valid_exclusions_sufficient_3_plus6=cert['maximum_matching']>=15,
                                    arbitrary_valid_exclusions_sufficient_4_plus6=cert['maximum_matching']>=16))
    write('factory-domain-certificates.json', dict(evidence='DERIVED_VECTOR_AND_TOOL_VALIDATION', behavior='NOT_EXECUTED',
          premise='Current factory predicates, suggested level50/100, nonnegative wins/swaps and already-valid excluded team. Matching bound M >= n+2e is sufficient, not necessary; excluded species/item vertices remove at most2e matched edges. Bad index can still fail before validation.',
          domains=factory))
    print(json.dumps({'trainer_records':len(rows_out), 'template_records':len(all_rows), 'factory_domains':len(factory),
                      'literals':{k:len(v) for k,v in literals.items()},
                      'fixed_factory_nontermination':{'Pika':'3*20=60>50','Poke':'3*55=165>155','Fancy':'3*30=90>80'},
                      'trainer_200_unreachable':bands[200]['absent_trainer_indices']},ensure_ascii=False))

if __name__ == '__main__':
    main()
