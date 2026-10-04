"""B05 text/identity checks only; no reference loading or behavioral execution."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess

BASE = '0a12de641542f9a59909d2a950c1de8df17ca09d'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
INTEGRATION = '93d0714ddfdb4900e946c0acd1cc80cf6431f0a0'
REFERENCE = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REFERENCE_TREE = '7589c800b61ba13a13040ed0d686979b80a84fd0'
ROOT = Path(__file__).resolve().parents[6]
AUTHOR = Path(__file__).resolve().parent
FINAL = ROOT / 'deliverables/final-specification-set'
parser = argparse.ArgumentParser()
parser.add_argument('--reference', type=Path, default=Path('/workspace/reference-B05-pokemon-essentials'))
args = parser.parse_args()
REF = args.reference.resolve()
checks = []

def git(*cmd, repo=ROOT):
    return subprocess.check_output(['git', '--no-optional-locks', '-C', str(repo), *cmd])

def check(name, condition, details=None):
    checks.append({'check': name, 'ok': bool(condition), 'details': details})
    assert condition, (name, details)

def read(path):
    return path.read_text(encoding='utf-8-sig')

def rows(text):
    return [[x.strip() for x in line.strip('|').split('|')] for line in text.splitlines() if line.startswith('|')]

def literal_sections(text):
    # Read plaintext section headings and literal field lines, never a data loader.
    result = []
    for heading, body in re.findall(r'^\[([^\]\n]+)\]\s*\n(.*?)(?=^\[|\Z)', text, re.M | re.S):
        fields = {}
        for line in body.splitlines():
            if '=' in line and not line.lstrip().startswith('#'):
                key, value = line.split('=', 1)
                fields[key.strip()] = value.strip()
        result.append((heading, fields))
    return result

check('reference SHA', git('rev-parse', 'HEAD', repo=REF).decode().strip() == REFERENCE)
check('reference tree', git('rev-parse', 'HEAD^{tree}', repo=REF).decode().strip() == REFERENCE_TREE)
check('reference clean', not git('status', '--porcelain', '--untracked-files=all', repo=REF).strip())
check('reference outside author Git', not REF.is_relative_to(ROOT))
check('approved planning bytes inherited unchanged', not git('diff', PLAN, BASE, '--', 'review/remediation-20261003-prepare').strip())
check('B01 successor contains no formal byte changes', not git('diff', INTEGRATION, BASE, '--', 'deliverables', 'specs', 'planning', 'audit').strip())

plan_root = ROOT / 'review/remediation-20261003-prepare'
batches = json.loads(read(plan_root/'batches.json'))
batch = next(x for x in batches if x['id'] == 'B05')
b02 = next(x for x in batches if x['id'] == 'B02')
check('B02 and B05 physical write sets disjoint', not set(batch['write_paths']) & set(b02['write_paths']))
check('B02 writes do not invalidate B05 frozen readers', not set(b02['write_paths']) & set(batch['read_paths']))
check('B05 writes do not invalidate B02 frozen readers', not set(batch['write_paths']) & set(b02['read_paths']))
check('ten formal paths and sixteen contributions', len(batch['write_paths']) == 10 and len(batch['contribution_finding_ids']) == 16 and len(batch['primary_finding_ids']) == 10)
allowed = set(batch['write_paths'])
receipt = AUTHOR/'original-scope-decision.json'
if receipt.exists():
    decision = json.loads(read(receipt))
    if decision.get('approved'):
        allowed.update(decision['approved_paths'])
changed = git('diff', BASE, '--name-only').decode().splitlines()
check('tracked changes stay in authorized paths', all(p in allowed or p.startswith('review/remediation/20261003-prepare/batches/B05/author/') for p in changed), changed)
check('no public registry or historical modifications', all(not p.startswith(('planning/', 'audit/', 'review/remediation-20261003-prepare/')) and (not p.startswith('review/') or p.startswith('review/remediation/20261003-prepare/batches/B05/author/')) for p in changed))

creature = 'deliverables/final-specification-set/test-catalog/creature-rpg-wp18-20-24-25-26.md'
pokemon = 'deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md'
for path, marker in [(creature, '## PT：'), (pokemon, '## BR：')]:
    old = git('show', BASE+':'+path).decode()
    new = read(ROOT/path)
    check('protected shared tail '+marker, old.split(marker, 1)[1] == new.split(marker, 1)[1], path)
for path, counts in [(creature, {'CI-':28,'HP-':45,'PT-':28,'PS-':28,'AQ-':35}), (pokemon, {'ST':67,'FM':43,'ME':26,'SH':52,'BR':25})]:
    text = read(ROOT/path)
    for prefix, count in counts.items():
        ids = re.findall(r'^\| '+re.escape(prefix)+r'(\d+) \|', text, re.M)
        check('unique contiguous catalog '+prefix, len(ids) == count and sorted(map(int, ids)) == list(range(1, count+1)), count)
    check('static-only catalog qualifier '+path, '不是已执行测试' in text)

nature_text = read(REF/'Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb')
labels = {'ATTACK':'攻击','DEFENSE':'防御','SPEED':'速度','SPECIAL_ATTACK':'特攻','SPECIAL_DEFENSE':'特防'}
source_natures = []
for body in re.findall(r'GameData::Nature\.register\(\{(.*?)\}\)', nature_text, re.S):
    name = re.search(r':id\s*=>\s*:(\w+)', body).group(1)
    pairs = re.findall(r'\[:(\w+),\s*(-?\d+)\]', body)
    up = next((labels[s] for s, amount in pairs if int(amount) == 10), '无')
    down = next((labels[s] for s, amount in pairs if int(amount) == -10), '无')
    source_natures.append([str(len(source_natures)), name, up, down])
spec_natures = [r for r in rows(read(FINAL/'pokemon-rules/wp19-attributes-ability-and-stats.md')) if len(r) == 4 and r[0].isdigit()]
check('all 25 Nature identities and modifier pairs', spec_natures == source_natures and len(source_natures) == 25)
check('five exact neutral positions', [int(r[0]) for r in spec_natures if r[2:] == ['无','无']] == [0,6,12,18,24])

forms = literal_sections(read(REF/'PBS/pokemon_forms.txt'))
source_megas = []
for heading, fields in forms:
    if 'MegaStone' not in fields and 'MegaMove' not in fields:
        continue
    species, form = heading.split(',')
    kind = '石 '+fields['MegaStone'] if 'MegaStone' in fields else '招 '+fields['MegaMove']
    source_megas.append([species, form, kind, '／'.join(fields['BaseStats'].split(','))])
    check('Mega source unmega/message '+heading, fields.get('UnmegaForm','0') == '0' and fields.get('MegaMessage','0') == ('1' if species == 'RAYQUAZA' else '0'))
mega_rows = [r for r in rows(read(FINAL/'pokemon-rules/wp22-transformation-data.md')) if len(r) == 4 and r[1].isdigit() and r[2].startswith(('石 ','已知招式 '))]
for row in mega_rows:
    row[2] = row[2].replace('已知招式 ', '招 ', 1)
check('all 48 Mega identity/condition/base-stat rows ordered', mega_rows == source_megas and len(mega_rows) == 48)
check('Mega target species and stone/move counts', len({r[0] for r in mega_rows}) == 46 and sum(r[2].startswith('石 ') for r in mega_rows) == 47)
item_ids = {h for h,_ in literal_sections(read(REF/'PBS/items.txt'))}
check('all Mega stones valid item identities', all(r[2][2:] in item_ids for r in mega_rows if r[2].startswith('石 ')))
move_ids = {h for h,_ in literal_sections(read(REF/'PBS/moves.txt'))}
named_moves = {'TACKLE','GROWL','POUND','SCRATCH','TAILWHIP','LEER','AMNESIA','CHARGEBEAM','OVERHEAT','HYDROPUMP','BLIZZARD','AIRSLASH','LEAFSTORM','THUNDERSHOCK','ICEBURN','FREEZESHOCK','GLACIATE','FUSIONFLARE','FUSIONBOLT','SCARYFACE','SUNSTEELSTRIKE','MOONGEISTBEAM','CONFUSION','GLACIALLANCE','ASTRALBARRAGE','IRONHEAD','BEHEMOTHBLADE','BEHEMOTHBASH','DRAGONASCENT'}
check('named default move identities valid as literal records', named_moves <= move_ids and {'TM57','BANETTITE','RUSTEDSWORD','RUSTEDSHIELD','FOCUSBAND'} <= item_ids)
check('BANETTITE correct; invalid sanitized spelling absent', any(r[:3] == ['BANETTE','1','石 BANETTITE'] for r in mega_rows) and 'BANETTEITE' not in read(FINAL/'pokemon-rules/wp22-transformation-data.md'))

shadow_source = [[h,f.get('GaugeSize','4000'),'／'.join(f['Moves'].split(','))] for h,f in literal_sections(read(REF/'PBS/Shadow Pokémon backup/shadow_pokemon.txt'))]
shadow_spec = read(FINAL/'pokemon-rules/wp23-shadow-data-and-vectors.md')
shadow_rows = [r for r in rows(shadow_spec) if len(r) == 3 and r[1].isdigit() and r[2].startswith('SHADOW')]
check('all 131 optional Shadow identities/gauges/move order', shadow_rows == shadow_source and len(shadow_rows) == 131)
heart_source_text = read(REF/'Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb')
heart_source = [[name, *[x.strip() for x in amounts.split(',')]] for name,amounts in re.findall(r':(\w+)\s*=>\s*\[(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*\d+\s*)\]', heart_source_text)]
heart_rows = [r for r in rows(shadow_spec) if len(r) == 5 and r[0] in {x[0] for x in heart_source}]
check('all 25 heart reduction rows', heart_rows == heart_source and len(heart_rows) == 25)
move_source = literal_sections(read(REF/'PBS/Shadow Pokémon backup/moves_shadow_pkmn.txt'))
move_rows = [r for r in rows(shadow_spec) if len(r) == 2 and r[0].startswith('SHADOW')]
check('18 optional Shadow move effect bindings', move_rows == [[h,f['FunctionCode']] for h,f in move_source] and len(move_rows) == 18)
optional_items = literal_sections(read(REF/'PBS/Shadow Pokémon backup/items_shadow_pkmn.txt'))
item_rows = [r for r in rows(shadow_spec) if len(r) == 5 and r[0] in {x[0] for x in optional_items}]
check('all four optional item use/price/absent Scent flag rows', item_rows == [[h,f['FieldUse'],f.get('BattleUse','无'),f['Price'],'无（未声明 Flags）'] for h,f in optional_items] and all('Flags' not in f for _,f in optional_items))
shadow_type = literal_sections(read(REF/'PBS/Shadow Pokémon backup/types_shadow_pkmn.txt'))
check('optional SHADOW type literal special/resistance fields', len(shadow_type) == 1 and shadow_type[0][0] == 'SHADOW' and shadow_type[0][1]['IsSpecialType'] == 'true' and shadow_type[0][1]['Resistances'] == 'SHADOW')
check('optional data stays conditional', '非默认启用' in shadow_spec and '不启用备份集' in read(FINAL/'pokemon-rules/wp22-transformation-data.md'))

char_text = read(FINAL/'pokemon-rules/wp19-attributes-ability-and-stats.md')
char_rows = [r for r in rows(char_text) if len(r) == 6 and r[0] in {'HP','攻击','防御','速度','特攻','特防'}]
check('all 30 characteristic meanings present', len(char_rows) == 6 and all(len(r[1:]) == 5 and all(r[1:]) for r in char_rows))
check('characteristic tie order explicit', 'HP → 攻击 → 防御 → 速度 → 特攻 → 特防' in char_text and '相等的后续项不替换' in char_text)
shadow_main = read(FINAL/'pokemon-rules/wp23-shadow-hyper-and-purification.md')
check('both scent gates use h255 and G0', shadow_main.count('**h=255 且 G=0**') == 1 and '**友好度 h=255 且 G=0**' in shadow_main and '不是 H5/G0' not in shadow_main)

# Independent fixed arithmetic only; no cases, actors, reference routines or UI run.
check('fixed arithmetic: Bulbasaur HP and neutral bases', 121*50//100+60 == 120 and 129*50//100+5 == 69 and 161*50//100+5 == 85 and 121*50//100+5 == 65)
check('fixed arithmetic: positive/negative Nature floors', 69*110//100 == 75 and 69*90//100 == 62 and 85*90//100 == 76 and 65*90//100 == 58 and 105*110//100 == 115 and 105*90//100 == 94)
check('fixed arithmetic: heart thresholds and EV terms', 2500-90 == 2410 and 2500-130 == 2370 and 3*800 < 2410 <= 4*800 and 2*800 < 2370 <= 3*800 and 510//2 == 255 and 255//4 == 63)

check('scope proposal is applicable without writing originals', subprocess.run(['git','apply','--check',str(AUTHOR/'original-synchronization-proposed.patch')],cwd=ROOT,capture_output=True).returncode == 0 if not (receipt.exists() and json.loads(read(receipt)).get('approved')) else True)
file_hashes = {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in batch['write_paths']}
result = {'status':'PASS_STATIC_TEXT_AND_FIXED_ARITHMETIC_ONLY','candidate_parent':BASE,'reference_sha':REFERENCE,'checks':checks,'formal_file_sha256':file_hashes,'behavioral_vectors_executed':0,'runtime_observations':0,'demo_chains_executed':0,'reference_scripts_executed':0,'independent_review':'PENDING','integration_review':'NOT_STARTED','canonical_closures':0}
(AUTHOR/'static-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'status':result['status'],'behavioral_vectors_executed':0,'runtime_observations':0,'demo_chains_executed':0},ensure_ascii=False))
