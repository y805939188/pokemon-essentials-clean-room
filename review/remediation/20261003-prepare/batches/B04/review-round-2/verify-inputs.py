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
PAYLOAD = '50f9ca2506bf0de21c33c644569c9987f84b80a3'
PREVIOUS_PAYLOAD = '99d9c24c43b503763bdbf259db19e5c651e27175'
PREVIOUS_HANDOFF = 'da6daba7d6c6365d4578d7173a6d8316acae8bb8'
ROUND1_REPORT = 'f0d89a0989cf16d7ea2592fdf75a968b553caefa'
HANDOFF = '5da06e2baf0879978a871c6952fab1105909b511'
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

freeze = obj(HANDOFF, PREFIX + 'freeze-stage-2/freeze.json')
check('payload parent is previous full handoff', git('rev-parse', PAYLOAD + '^').decode().strip() == PREVIOUS_HANDOFF)
check('payload tree frozen', git('rev-parse', PAYLOAD + '^{tree}').decode().strip() == freeze['candidate_payload_tree'])
check('handoff parent is payload', git('rev-parse', HANDOFF + '^').decode().strip() == PAYLOAD)
paths = git('diff', '--name-only', BASE, PAYLOAD).decode().splitlines()
check('complete exact frozen path set', set(paths) == {r['path'] for r in freeze['candidate_files']} and len(paths) == 62)
for row in freeze['candidate_files']:
    identity(PAYLOAD, row)
    identity(HANDOFF, row)
check('handoff adds only freeze reports', set(git('diff', '--name-only', PAYLOAD, HANDOFF).decode().splitlines()) == {
    PREFIX + 'freeze-stage-2/README.md', PREFIX + 'freeze-stage-2/freeze.json', PREFIX + 'freeze-stage-2/complete-candidate.diff', PREFIX + 'freeze-stage-2/round2-delta.diff'})
complete = git('diff', '--full-index', '--unified=0', BASE, PAYLOAD)
check('complete frozen diff exact bytes', complete == data(HANDOFF, PREFIX + 'freeze-stage-2/complete-candidate.diff'))
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
inventory = obj(PREVIOUS_PAYLOAD, PREFIX + 'author-round-1/static-design-inventory.json')
old_ids = set(inventory['new_ids'])
check('original 111 design IDs retained plus exactly three new', len(old_ids) == 111 and len(new_ids) == len(set(new_ids)) == 114 and set(new_ids) == old_ids | {'B04-W24','B04-R27','B04-R28'})
retained_rows = []
modified_rows = []
for path in sorted(p for p in formal if '/test-catalog/' in p):
    old_rows = dict((m[1],line) for line in data(PREVIOUS_PAYLOAD,path).decode().splitlines() if (m := re.match(r'^\| ([A-Z][A-Z0-9-]*) \|',line)) and m[1] in old_ids)
    current_rows = dict((m[1],line) for line in data(PAYLOAD,path).decode().splitlines() if (m := re.match(r'^\| ([A-Z][A-Z0-9-]*) \|',line)) and m[1] in old_ids)
    for ident, line in old_rows.items():
        check('retained old B04 design ' + ident, ident in current_rows)
        (retained_rows if line == current_rows[ident] else modified_rows).append(ident)
check('108 original design rows byte equal, exactly three corrected',len(retained_rows) == 108 and set(modified_rows) == {'B04-W01','B04-R13','B04-R14'})
check('34 source coverage scenes', sum(k.startswith('XC-') for k in new_ids) == 34)
delta_paths = git('diff','--name-only',PREVIOUS_HANDOFF,PAYLOAD).decode().splitlines()
check('exact 27 incremental paths',len(delta_paths)==27 and set(delta_paths)==set(freeze['round2_delta_files']))
check('exact six formal incremental paths',len([p for p in delta_paths if not p.startswith(PREFIX)])==6)
for p in paths:
    if '/author-round-1/' in p or '/freeze-stage-1/' in p:
        check('first-round candidate history immutable ' + p,data(PREVIOUS_HANDOFF,p)==data(PAYLOAD,p))
check('complete delta exact frozen bytes',git('diff','--full-index','--unified=0',PREVIOUS_HANDOFF,PAYLOAD)==data(HANDOFF,PREFIX+'freeze-stage-2/round2-delta.diff'))
identity(HANDOFF,freeze['previous_handoff_to_payload_diff'])
for p in ['deliverables/final-specification-set/creature-rpg/wp24-player-trainers-partners.md','deliverables/final-specification-set/engine-overworld/wp13-interpreter-command-matrix.md','deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md','deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md']:
    check('read-only dependency unchanged ' + p,data(BASE,p)==data(PAYLOAD,p))
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
# This block inspects author evidence only after independent-first-judgment.json
# was saved. All operations are fixed Git/document byte checks.
auth = obj(PAYLOAD, PREFIX + 'author-round-2/authorization-and-limits.json')
check('round2 authorization matches independently derived formal increment', set(auth['allowed_changed_formal_paths']) == set(p for p in delta_paths if not p.startswith(PREFIX)))
check('cumulative exact formal authorization',set(auth['formal_cumulative_paths'])==set(formal))
for row in obj(PAYLOAD, PREFIX+'author-round-2/formal-artifact-identities.json')['files']:
    identity(PREVIOUS_HANDOFF,row['previous']);identity(PAYLOAD,row['candidate'])
    check('reported delta flag exact '+row['path'],row['changed'] == (data(PREVIOUS_HANDOFF,row['path'])!=data(PAYLOAD,row['path'])))
check('author incremental formal diff exact',data(PAYLOAD,PREFIX+'author-round-2/formal-delta.diff')==git('diff','--full-index','--unified=0',PREVIOUS_HANDOFF,PAYLOAD,'--',*formal))
for row in obj(PAYLOAD,PREFIX+'author-round-2/original-sync-ledger.json')['entries']:
    identity(PREVIOUS_HANDOFF,row['previous']);identity(PAYLOAD,row['candidate'])
    if row['changed']:
        check('original exact incremental sync '+row['original'],data(PAYLOAD,row['diff']['path'])==git('diff','--full-index','--unified=0',PREVIOUS_HANDOFF,PAYLOAD,'--',row['original']))
        identity(PAYLOAD,row['diff'])
    else:
        check('unchanged necessary original '+row['original'],data(PREVIOUS_HANDOFF,row['original'])==data(PAYLOAD,row['original']))
manifest = obj(PAYLOAD,PREFIX+'author-round-2/author-artifact-manifest.json')['files']
check('exact twenty author manifest entries excluding self',len(manifest)==20 and {r['path'] for r in manifest} == {p for p in paths if '/author-round-2/' in p and not p.endswith('/author-artifact-manifest.json')})
for row in manifest:identity(PAYLOAD,row)
report_binding=obj(PAYLOAD,PREFIX+'author-round-2/review-input-bindings.json')
for row in report_binding['artifact_identities']:identity(ROUND1_REPORT,row)
check('exact fourteen immutable first review artifacts bound',len(report_binding['artifact_identities'])==14 and {r['path'] for r in report_binding['artifact_identities']}==set(git('ls-tree','-r','--name-only',ROUND1_REPORT,'--',PREFIX+'review-round-1').decode().splitlines()))
old_findings=obj(ROUND1_REPORT,PREFIX+'review-round-1/new-findings.json')['findings']
check('two original observations preserved verbatim',report_binding['two_complete_observations']==old_findings and [r['original_report_observation'] for r in obj(PAYLOAD,PREFIX+'author-round-2/review-observation-responses.json')['observations']]==old_findings)
response_rows=obj(PAYLOAD,PREFIX+'author-round-2/finding-responses.json')['responses']
check('exact thirty-five current responses',len(response_rows)==35 and {r['id'] for r in response_rows}==set(control))
for row in response_rows:
    ident=row['id']
    check('full current control hashes '+ident,row['inherited_control_hashes']=={'original':sha(canonical(findings[ident])),'acceptance':sha(canonical(acceptance[ident]))})
    check('no canonical approval in author response '+ident,row['new_approval'] is False and row['canonical_state']=='OPEN')
    for clause in row['clauses']:
        lines=data(PAYLOAD,clause['path']).decode().splitlines()
        check('precise clause locator '+ident+':'+clause['section'],1<=clause['line']<=len(lines) and lines[clause['line']-1].lstrip('# ')==clause['heading'])
    for design in row['static_designs']:
        lines=data(PAYLOAD,design['path']).decode().splitlines()
        check('precise static design locator '+ident+':'+design['id'],1<=design['line']<=len(lines) and lines[design['line']-1]==design['fixture_and_expected'])
    prior=next(r for r in obj(PREVIOUS_PAYLOAD,PREFIX+'author-round-1/finding-responses.json')['responses'] if r['id']==ident)
    if ident not in {'GIR-FD82-C061','GIR-FD82-C062'}:
        check('other thirty-three scope and design ownership retained '+ident,row['scope']==prior['scope'] and {r['id'] for r in row['static_designs']}=={r['id'] for r in prior['static_designs']} and row['other_contributors_pending']==prior['other_contributors_pending'])
inventory2=obj(PAYLOAD,PREFIX+'author-round-2/static-design-inventory.json')
check('current inventory agrees with independently derived count',set(inventory2['new_ids'])=={'B04-W24','B04-R27','B04-R28'} and set(inventory2['modified_existing_ids'])==set(modified_rows) and inventory2['cumulative_new_rows_from_accepted_baseline']==114 and inventory2['executions']==0)
handover=obj(PAYLOAD,PREFIX+'author-round-2/interface-handoff.json')
for key,delta_count,fifth in [('B04_to_B07',2,'specs/ui/wp17-messages-windows-input.md'),('B04_to_B06',3,'specs/overworld/wp15-resource-matching-and-audio.md')]:
    readers=handover[key]['changed_readers']
    check('five frozen successor readers '+key,len(readers)==5 and fifth in {r['path'] for r in readers} and sum(r['changed_since_round1'] for r in readers)==delta_count)
    for row in readers:
        identity(PAYLOAD,row);identity(PREVIOUS_HANDOFF,row['previous'])
        check('successor delta flag exact '+row['path'],row['changed_since_round1']==(data(PREVIOUS_HANDOFF,row['path'])!=data(PAYLOAD,row['path'])))
check('two explicit reverse B07 triggers',handover['B04_to_B07']['reverse_changes_require_affected_B04_recheck']==['deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md','deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md'])
source2=list(csv.DictReader(data(PAYLOAD,PREFIX+'author-round-2/source-reading-log.tsv').decode().splitlines(),delimiter='\t'))
author_read_union=collections.defaultdict(set)
for row in source2:
    value=(ref/row['path']).read_bytes();lines=value.splitlines(keepends=True);a,b=int(row['first']),int(row['last'])
    check('new author source bounds/hash '+row['path']+':'+str(a)+'-'+str(b),row['commit']==REF and 1<=a<=b<=len(lines)==int(row['actual_lines']) and sha(value)==row['full_sha256'] and blob(value)==row['full_blob'] and sha(b''.join(lines[a-1:b]))==row['range_sha256'] and value==refgit('show',REF+':'+row['path']))
    author_read_union[row['path']].update(range(a,b+1))
check('five files twelve new author bounded reads',len(author_read_union)==5 and len(source2)==12)
for row in csv.DictReader(data(PAYLOAD,PREFIX+'author-round-2/source-unread-ranges.tsv').decode().splitlines(),delimiter='\t'):
    all_lines=set(range(1,int(row['actual_lines'])+1));unread=set()
    for part in row['unread_this_round'].split(','):
        ends=list(map(int,part.split('-')));unread.update(range(ends[0],ends[-1]+1))
    check('precise author unread complement '+row['path'],unread==all_lines-author_read_union[row['path']])
check('unchanged public source qualifications',data(BASE,'review/wp79-coverage-review-2026-10-03/revision-v6/source-judgments.json')==data(PAYLOAD,'review/wp79-coverage-review-2026-10-03/revision-v6/source-judgments.json'))
check('reference remote independently fixed',refgit('remote','get-url','origin').decode().strip()=='https://github.com/Maruno17/pokemon-essentials.git')
check('all zero execution/no-close limitations',all(auth[k]==0 for k in ['runtime_observations','proven_demo_chains','vector_executions','reference_execution','canonical_closed','new_canonical_ids','public_register_plan_history_writes']) and auth['effective_configuration']=='UNVERIFIED' and auth['trusted_effective_echo'] is None)

print(json.dumps({'kind': 'INDEPENDENT_DOCUMENT_AND_IDENTITY_CHECKS_ONLY', 'all_checks_passed': True,
                  'checks': checks, 'check_count': len(checks), 'catalogs': catalog_checks,
                  'complete_diff_sha256': sha(complete), 'formal_paths': formal, 'static_new_ids': new_ids,'original_111_retained': True,'original_rows_byte_equal':len(retained_rows),'modified_original_rows':sorted(modified_rows),'new_round2_rows':['B04-W24','B04-R27','B04-R28'],
                  'round2_author_source_range_hashes_verified':len(source2),'round2_author_source_files_hash_verified':len(author_read_union),'author_source_range_hashes_verified': len(source), 'author_source_files_hash_verified': len({r['path'] for r in source}),
                  'hash_verification_is_not_semantic_read_coverage': True, 'reference_execution': 0,
                  'static_vector_execution': 0, 'runtime_observations': 0, 'proven_demo_chains': 0}, ensure_ascii=False, indent=2))
