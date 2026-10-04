"""Independent Git/document identity checks; no reference code is executed.

Run from the main repository root with --reference /path/to/detached/reference.
Outputs JSON to stdout. Reference reads are byte/hash checks, not read coverage.
"""
import argparse
import collections
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess

BASE = '6452c0e03025605222f3de9a272221e2b82eeda4'
PAYLOAD = '99d9c24c43b503763bdbf259db19e5c651e27175'
HANDOFF = 'da6daba7d6c6365d4578d7173a6d8316acae8bb8'
FINAL = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PREFIX = 'review/remediation/20261003-prepare/batches/B04/'
ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode().strip())
parser = argparse.ArgumentParser()
parser.add_argument('--reference', type=Path, required=True)
args = parser.parse_args()
checks = []

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def data(commit, path):
    return git('show', commit + ':' + path)

def obj(commit, path):
    return json.loads(data(commit, path))

def sha(value):
    return hashlib.sha256(value).hexdigest()

def blob(value):
    return hashlib.sha1(b'blob ' + str(len(value)).encode() + b'\0' + value).hexdigest()

def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()

def check(name, condition, detail=None):
    if not condition:
        raise AssertionError((name, detail))
    checks.append({'check': name, 'detail': detail})

def identity(commit, row):
    value = data(commit, row['path'])
    check('identity ' + commit + ':' + row['path'],
          sha(value) == row['sha256'] and len(value) == row['bytes']
          and blob(value) == row.get('git_blob', row.get('blob')))

freeze = obj(HANDOFF, PREFIX + 'freeze-stage-1/freeze.json')
check('payload parent is accepted baseline', git('rev-parse', PAYLOAD + '^').decode().strip() == BASE)
check('payload tree frozen', git('rev-parse', PAYLOAD + '^{tree}').decode().strip() == freeze['candidate_payload_tree'])
check('handoff parent is payload', git('rev-parse', HANDOFF + '^').decode().strip() == PAYLOAD)
paths = git('diff', '--name-only', BASE, PAYLOAD).decode().splitlines()
check('complete exact frozen path set', set(paths) == {r['path'] for r in freeze['candidate_files']} and len(paths) == 38)
for row in freeze['candidate_files']:
    identity(PAYLOAD, row)
    identity(HANDOFF, row)
check('handoff adds only freeze reports', set(git('diff', '--name-only', PAYLOAD, HANDOFF).decode().splitlines()) == {
    PREFIX + 'freeze-stage-1/README.md', PREFIX + 'freeze-stage-1/freeze.json', PREFIX + 'freeze-stage-1/complete-candidate.diff'})
complete = git('diff', '--full-index', '--unified=0', BASE, PAYLOAD)
check('complete frozen diff exact bytes', complete == data(HANDOFF, PREFIX + 'freeze-stage-1/complete-candidate.diff'))
identity(HANDOFF, freeze['complete_baseline_to_payload_diff'])
handshake = obj(BASE, 'review/remediation/20261003-prepare/batches/B06/acceptance-stage-1/downstream-handshake.json')
contract = handshake['B04']
for row in contract['planned_reads']:
    identity(row.get('commit', BASE), row)
check('74 planned inputs bound', len(contract['planned_reads']) == 74)
formal = contract['allowed_formal_write_paths'] + contract['allowed_original_sync_paths']
check('13 formal paths authorized', len(formal) == 13 and set(p for p in paths if not p.startswith(PREFIX)) == set(formal))
gate = obj(PAYLOAD, PREFIX + 'author-round-1/read-freeze-gate.json')
for row in gate['identities_checked']:
    identity(row['commit'], row)
check('103 author gate identities independently checked', len(gate['identities_checked']) == 103)
control = obj(PAYLOAD, PREFIX + 'author-round-1/finding-controls.json')
findings = {r['id']: r for r in obj(FINAL, 'review/global-independent-review/2026-10-03-fd82a639/findings.json')}
acceptance = obj(PLAN, 'review/remediation-20261003-prepare/finding-acceptance.json')
if isinstance(acceptance, list):
    acceptance = {r['id']: r for r in acceptance}
for row in contract['contribution_controls']:
    ident = row['id']
    check('effective original object ' + ident, control[ident]['original'] == findings[ident]
          and sha(canonical(findings[ident])) == row['original_object_sha256'])
    check('fixed acceptance object ' + ident, control[ident]['acceptance'] == acceptance[ident]
          and sha(canonical(acceptance[ident])) == row['acceptance_object_sha256'])
check('35 exact contribution IDs; 23 primary', set(control) == set(contract['contribution_finding_ids'])
      and len(control) == 35 and len(contract['primary_finding_ids']) == 23)
catalog_checks = []
new_ids = []
for path in sorted(p for p in formal if '/test-catalog/' in p):
    def rows(commit):
        pairs = []
        for line in data(commit, path).decode().splitlines():
            match = re.match(r'^\| ([A-Z][A-Z0-9-]*) \|', line)
            if match and match[1] != 'ID':
                pairs.append((match[1], line))
        return pairs
    before, after = rows(BASE), rows(PAYLOAD)
    old, new = dict(before), dict(after)
    check('old catalog ID multiplicity retained ' + path,
          all(collections.Counter(k for k, _ in after)[k] == n
              for k, n in collections.Counter(k for k, _ in before).items()))
    check('all old catalog rows retained ' + path, set(old) <= set(new))
    changed = sorted(k for k in old if old[k] != new[k])
    permitted = {'engine-overworld-wp11-15-59-60.md': ['RS09', 'RS10', 'RS17'],
                 'engine-overworld-wp16.md': ['WR06', 'WR12'],
                 'user-interface-wp17-63-65-66-67-68-69-70-71.md': ['MG23', 'DT03', 'DT07']}[Path(path).name]
    check('only assigned old row changes ' + path, changed == sorted(permitted))
    protected = [pair for pair in before if pair[0] not in permitted]
    check('other old row bytes and order retained ' + path,
          protected == [pair for pair in after if pair[0] in old and pair[0] not in permitted])
    added = [k for k, line in after if k not in old]
    check('new catalog IDs unique ' + path, len(added) == len(set(added)))
    new_ids.extend(added)
    catalog_checks.append({'path': path, 'old_rows': len(before), 'new_static_rows': len(added), 'changed_old_rows': changed})
inventory = obj(PAYLOAD, PREFIX + 'author-round-1/static-design-inventory.json')
check('111 new static designs exact inventory', len(new_ids) == len(set(new_ids)) == 111 and set(new_ids) == set(inventory['new_ids']))
check('34 source coverage scenes', sum(k.startswith('XC-') for k in new_ids) == 34)
check('author formal diff exact', data(PAYLOAD, PREFIX + 'author-round-1/formal-full.diff') == git('diff', '--full-index', '--unified=0', BASE, PAYLOAD, '--', *formal))
for row in obj(PAYLOAD, PREFIX + 'author-round-1/original-sync-ledger.json')['entries']:
    check('original exact diff ' + row['original_path'], data(PAYLOAD, row['diff']['path']) == git('diff', '--full-index', '--unified=0', BASE, PAYLOAD, '--', row['original_path']))
handover = obj(PAYLOAD, PREFIX + 'author-round-1/interface-handoff.json')
for key in ['B04_to_B07', 'B04_to_B06']:
    check('five successor readers ' + key, len(handover[key]['changed_readers']) == 5)
    for row in handover[key]['changed_readers']:
        identity(PAYLOAD, row)
for path in handover['B04_to_B07']['reverse_changes_require_affected_B04_recheck'] + ['deliverables/final-specification-set/creature-rpg/wp24-player-trainers-partners.md', 'deliverables/final-specification-set/engine-overworld/wp13-interpreter-command-matrix.md']:
    check('read-only dependency unchanged ' + path, data(BASE, path) == data(PAYLOAD, path))
ref = args.reference.resolve()
def refgit(*args):
    return subprocess.check_output(['git', '-C', str(ref), *args])
check('real fixed reference commit', refgit('rev-parse', 'HEAD').decode().strip() == REF and refgit('cat-file', '-t', REF).decode().strip() == 'commit')
check('reference clean', not refgit('status', '--porcelain'))
source = list(csv.DictReader(data(PAYLOAD, PREFIX + 'author-round-1/source-reading-log.tsv').decode().splitlines(), delimiter='\t'))
for row in source:
    content = (ref / row['path']).read_bytes()
    lines = content.splitlines(keepends=True)
    a, b = int(row['first']), int(row['last'])
    check('author source identity/range ' + row['path'] + ':' + str(a) + '-' + str(b),
          content == refgit('show', REF + ':' + row['path']) and row['commit'] == REF
          and 1 <= a <= b <= len(lines) == int(row['actual_lines'])
          and sha(content) == row['full_sha256'] and blob(content) == row['full_blob']
          and sha(b''.join(lines[a - 1:b])) == row['range_sha256'])
check('candidate whitespace', subprocess.run(['git', '-C', str(ROOT), 'diff', '--check', BASE, PAYLOAD], capture_output=True).returncode == 0)
# Compare declarative compatibility data as text; this does not evaluate Ruby,
# implement reference behavior, construct host objects, or execute test vectors.
world = data(PAYLOAD, 'deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md').decode()
messages = data(PAYLOAD, 'deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md').decode()
pattern_source = (ref / 'Data/Scripts/006_Map renderer/004_TileDrawingHelper.rb').read_text().split('AUTOTILE_PATTERNS = [', 1)[1].split('# converts neighbors', 1)[0]
source_patterns = [tuple(map(int, x.split(','))) for x in re.findall(r'\[(\d+,\s*\d+,\s*\d+,\s*\d+)\]', pattern_source)]
candidate_patterns = {int(k): tuple(map(int, v.split(','))) for k, v in re.findall(r'(?<!\d)(\d+):((?:\d+,){3}\d+)', world)}
check('48 exact declarative pattern identities', len(source_patterns) == len(candidate_patterns) == 48
      and all(candidate_patterns[i] == v for i, v in enumerate(source_patterns)))
entry_source = (ref / 'Data/Scripts/016_UI/025_UI_TextEntry.rb').read_text().split('class PokemonEntryScene2', 1)[1].split('@@Characters = [', 1)[1].split('ROWS', 1)[0]
source_groups = [re.findall(r'"([^"\n]*)"', line)[:5] for line in entry_source.splitlines() if '.scan(/./)' in line]
candidate_character_rows = [re.findall(r'`([^`]+)`', line) for line in messages.splitlines() if re.match(r'^\| [0-4] \| `', line)]
check('20 exact compatibility character rows including spaces and Unicode', len(source_groups) == 4
      and len(candidate_character_rows) == 5
      and all(source_groups[g][r].replace('\\#', '#') == candidate_character_rows[r][g].replace('·', ' ')
              for g in range(4) for r in range(5)))
time_source = (ref / 'Data/Scripts/012_Overworld/003_Overworld_Time.rb').read_text().split('HOURLY_TONES = [', 1)[1].split('CACHED_TONE_LIFETIME', 1)[0]
source_hours = [tuple(map(int, x.split(','))) for x in re.findall(r'Tone.new\(([-\d,\s]+)\)', time_source)]
candidate_hours = {}
hour_table = world.split('默认24整点四通道', 1)[1].split('四通道均按分钟', 1)[0]
for line in hour_table.splitlines():
    if not re.match(r'^\| \d', line):
        continue
    cells = [x.strip() for x in line.split('|')[1:-1]]
    value = tuple(map(int, cells[1].replace('−', '-').split(',')))
    for part in cells[0].split('、'):
        ends = list(map(int, part.split('–')))
        for hour in range(ends[0], ends[-1] + 1):
            check('hour identity no overlap ' + str(hour), hour not in candidate_hours)
            candidate_hours[hour] = value
check('24 exact declarative hourly tones', len(source_hours) == len(candidate_hours) == 24
      and all(candidate_hours[i] == v for i, v in enumerate(source_hours)))
print(json.dumps({'kind': 'INDEPENDENT_DOCUMENT_AND_IDENTITY_CHECKS_ONLY', 'all_checks_passed': True,
                  'checks': checks, 'check_count': len(checks), 'catalogs': catalog_checks,
                  'complete_diff_sha256': sha(complete), 'formal_paths': formal, 'static_new_ids': new_ids,
                  'author_source_range_hashes_verified': len(source), 'author_source_files_hash_verified': len({r['path'] for r in source}),
                  'hash_verification_is_not_semantic_read_coverage': True, 'reference_execution': 0,
                  'static_vector_execution': 0, 'runtime_observations': 0, 'proven_demo_chains': 0}, ensure_ascii=False, indent=2))
