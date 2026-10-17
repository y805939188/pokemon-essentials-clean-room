#!/usr/bin/env python3
"""Document/transport checks only. Does not execute Ruby or model game behavior."""
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import unicodedata

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / '.git').exists())
BASE = HERE.parent.parent
RR = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
INPUT = '4575e80d041ab0c74a42e2e36399d05791dbaa5b'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
checks = []


def git(*args, repo=ROOT):
    return subprocess.check_output(['git', '-C', str(repo), *args])


def load(name):
    return json.loads((HERE / name).read_text())


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check(name, condition, detail):
    checks.append(dict(name=name, result='PASS' if condition else 'FAIL', detail=detail))


def slug(text):
    text = re.sub(r'[^\w\-\s]', '', text.lower())
    return re.sub(r'\s', '-', text)


ident = load('identities.json')
check('fixed_input_tree', git('rev-parse', INPUT + '^{tree}').decode().strip() == ident['input_tree'], ident['input_tree'])
check('fixed_reference_tree', git('rev-parse', REF + '^{tree}', repo='/workspace/pokemon-essentials').decode().strip() == ident['reference_tree'], ident['reference_tree'])
check('formal_tree_matches_B8', ident['formal_tree'] == 'f292698cdd4a8e725525a9be6dc34b75faaf151e', ident['formal_tree'])
check('isolated_branch', git('branch', '--show-current').decode().strip() == ident['branch'], ident['branch'])
received = load('received-contracts.json')
assignment = next(x for x in json.loads((ROOT / RR / 'handoff/batch-assignment.json').read_text())['batches'] if x['id'] == 'R8-U09')
check('assignment_unchanged_snapshot', received['batch_assignment'] == assignment, 'Original selection and provenance remain historical; current selections separate.')
contracts = json.loads((ROOT / RR / 'handoff/contracts.zh.json').read_text())['records']
check('seven_full_contract_snapshots', received['records'] == [contracts[n] for n in [32, 37, 21, 29, 31, 33, 35]], 'Exact full records, not summaries.')
optional = load('optional-dispositions.json')
selected = {x['id'] for x in optional['selected']}
check('only_owned_optional_selected', selected == set(assignment['optional_ids_if_later_selected']), sorted(selected))
allowed = set(assignment['actual_target_write_set'])
for issue in selected:
    allowed.update(assignment['conditional_target_write_set_by_id'][issue])
actual = {str(p.relative_to(BASE / 'mirror')) for p in (BASE / 'mirror').rglob('*') if p.is_file()}
check('exact_nine_contract_mirrors', actual == allowed and len(actual) == 9, sorted(actual))
check('no_candidate_symlinks', all(not p.is_symlink() for p in BASE.rglob('*')), 'All candidate files are ordinary files.')
grouped = defaultdict(list)
for edit in load('exact-edits.json')['changes']:
    grouped[edit['target']].append(edit)
check('thirteen_bounded_fragments', len(load('exact-edits.json')['changes']) == 13 and set(grouped) == allowed, '9 target files, 13 exact replacements.')
for target in sorted(allowed):
    original = git('show', INPUT + ':' + target).decode()
    expected = original
    unique = True
    for edit in grouped[target]:
        unique &= expected.count(edit['old']) == 1
        expected = expected.replace(edit['old'], edit['new'], 1)
    output = (BASE / 'mirror' / target).read_text()
    check('exact_edit_reconstruction:' + target, unique and expected == output, 'Every byte outside the declared replacements is preserved.')
manifest = load('mirror-manifest.json')['mirrors']
for entry in manifest:
    data = (ROOT / entry['mirror']).read_bytes()
    check('manifest:' + entry['target'], digest(data) == entry['candidate']['sha256'] and len(data) == entry['candidate']['bytes'] and git('hash-object', str(ROOT / entry['mirror'])).decode().strip() == entry['candidate']['blob'], 'SHA256/bytes/Git blob agree.')
wp03 = next((BASE / 'mirror' / p).read_text() for p in allowed if '/wp03-' in p)
expected_rows = [(1,'Undiscovered','Undiscovered'),(2,'Monster','Monster'),(3,'Water1','Water 1'),(4,'Bug','Bug'),(5,'Flying','Flying'),(6,'Field','Field'),(7,'Fairy','Fairy'),(8,'Grass','Grass'),(9,'Humanlike','Humanlike'),(10,'Water3','Water 3'),(11,'Mineral','Mineral'),(12,'Amorphous','Amorphous'),(13,'Water2','Water 2'),(14,'Ditto','Ditto'),(15,'Dragon','Dragon')]
section = wp03.split('### 6.2 蛋群的固定作者身份目录\n',1)[1].split('\n## 7.',1)[0]
rows = [(int(n),i.strip(),v.strip()) for n,i,v in re.findall(r'^\| (\d+) \| ([^|]+) \| ([^|]+) \|$',section,re.M)]
check('exact_15_ID_label_order', rows == expected_rows, rows)
eggsource = git('show',REF+':Data/Scripts/010_Data/001_Hardcoded data/003_EggGroup.rb',repo='/workspace/pokemon-essentials').decode()
sourceids = re.findall(r':id\s*=>\s*:(\w+)',eggsource)
check('15_IDs_match_fixed_source', sourceids == [x[1] for x in expected_rows], sourceids)
catalog = next(p for p in allowed if '/test-catalog/' in p)
old = git('show', INPUT + ':' + catalog).decode().splitlines()
new = (BASE / 'mirror' / catalog).read_text().splitlines()
old_rows = [x for x in old if re.match(r'^\| (?:EG|EN|FC|TT|MG)-\d+ \|', x)]
new_rows = [x for x in new if re.match(r'^\| (?:EG|EN|FC|TT|MG)-\d+ \|', x)]
check('shared_catalog_only_MG32_changes', [x for x in old if not x.startswith('| MG-32 |')] == [x for x in new if not x.startswith('| MG-32 |')], 'All other lines, including MG25/29/30/31 and EG/EN/FC/TT, remain byte-identical.')
check('all_catalog_IDs_and_counts_preserved', [x.split('|')[1].strip() for x in old_rows] == [x.split('|')[1].strip() for x in new_rows] and len([x for x in new_rows if x.startswith('| MG-')]) == 32, dict(total_rows=len(new_rows),MG=32))
for target, edits in grouped.items():
    # Validate only newly introduced relative Markdown links against the formal overlay.
    for edit in edits:
        old_links = re.findall(r'\]\(([^)]+)\)', edit['old'])
        for link in re.findall(r'\]\(([^)]+)\)', edit['new']):
            if link in old_links or '://' in link:
                continue
            path, _, fragment = link.partition('#')
            resolved = (ROOT / target).parent / path if path else ROOT / target
            resolved = resolved.resolve()
            rel = str(resolved.relative_to(ROOT))
            overlay = BASE / 'mirror' / rel
            source = overlay if overlay.exists() else resolved
            exists = source.is_file()
            anchors = {slug(line.lstrip('#').strip()) for line in source.read_text().splitlines() if re.match(r'^#{1,6} ',line)} if exists else set()
            check('new_link:' + target + ':' + link, exists and (not fragment or fragment in anchors), dict(target=rel,anchor=fragment))
controls = load('static-controls.json')['controls']
check('22_controls_not_claimed_executed', len(controls) == 22 and all(x['execution'] == 'NOT_EXECUTED' for x in controls), dict(actual_controls=len(controls),six_MG_name_cases=[x['id'] for x in controls if re.match(r'MG-0[1-6]$',x['id'])]))
check('all_seven_resolved_with_evidence', {x['id'] for x in load('issue-resolutions.json')['records']} == {x['id'] for x in received['records']} and all(x['targets'] and x['discriminating_controls'] and x['unresolved_dependencies'] for x in load('issue-resolutions.json')['records']), 'Required 2, optional 5; all still pending independent review.')
check('four_gates_pending', all(v == 'PENDING_INDEPENDENT_RECEIPT' for v in ident['gates'].values()), ident['gates'])
tracked = git('diff','--name-only',INPUT,'--').decode().splitlines()
untracked = git('ls-files','--others','--exclude-standard').decode().splitlines()
prefix = str(BASE.relative_to(ROOT)) + '/'
check('all_writes_within_exclusive_candidate', all(p.startswith(prefix) for p in tracked+untracked), dict(tracked=len(tracked),untracked=len(untracked)))
check('formal_public_and_original_reports_untouched', not git('diff','--name-only',INPUT,'--','deliverables','audit','planning',RR).strip(), 'Formal targets/public indexes/original report contain no changes from fixed input.')
for entry in load('reading-ledger.json')['events']:
    data=git('show',entry['commit']+':'+entry['path'],repo=entry['repo'])
    start,end=entry['range']
    selected_data=b''.join(data.splitlines(keepends=True)[start-1:end])
    assert digest(data)==entry['file_sha256'] and digest(selected_data)==entry['selected_sha256'],entry['path']
check('reading_event_bytes_reverified', True, 'Exact ranges match fixed Git objects; hash validation does not award semantic reading credit.')
result=dict(schema='r8-u09-document-validation/v1',utc=datetime.now(timezone.utc).isoformat(),status='PASS' if all(c['result']=='PASS' for c in checks) else 'FAIL',qualification='Author TOOL_VALIDATION only; no candidate review acceptance or business execution.',checks=checks)
(HERE/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=result['status'],checks=len(checks),failures=[x for x in checks if x['result']=='FAIL']),ensure_ascii=False))
raise SystemExit(0 if result['status']=='PASS' else 1)
