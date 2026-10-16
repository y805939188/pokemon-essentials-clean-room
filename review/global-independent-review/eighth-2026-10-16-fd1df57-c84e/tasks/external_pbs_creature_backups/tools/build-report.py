"""Build mechanical coordinates around explicit, separately recorded reading attestations.

This program grants no semantic reading, clause support, or acceptance credit.
It writes only this task's directory. Run from any working directory.
"""
import collections
import datetime
import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = pathlib.Path('/workspace/pokemon-essentials-clean-room')
REF = pathlib.Path('/workspace/pokemon-essentials')
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PIN = '30cfed0996003b6ebf4b5c51cc04f31ca9255440'
TASK = ROOT.relative_to(SPEC).as_posix()
UTC = datetime.datetime.now(datetime.timezone.utc).isoformat()

def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])

def write(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def identity(repo, commit, path):
    b = git(repo, 'show', f'{commit}:{path}')
    local = (repo / path).read_bytes()
    mode, kind, blob = git(repo, 'ls-tree', commit, '--', path).decode().split('\t')[0].split()
    return dict(repo=str(repo), commit=commit,
                tree=git(repo, 'rev-parse', commit+'^{tree}').decode().strip(),
                path=path, cloud_path=str(repo/path), mode=mode, kind=kind, blob=blob,
                bytes=len(b), sha256=hashlib.sha256(b).hexdigest(),
                lines=len(b.splitlines()), workspace_bytes_match_commit=(b == local))

def covered(a, b, ranges):
    return all(any(lo <= n <= hi for lo, hi in ranges) for n in range(a, b+1))

def missing(total, ranges):
    out = []
    start = None
    for n in range(1, total+2):
        yes = n <= total and not any(a <= n <= b for a,b in ranges)
        if yes and start is None:
            start = n
        if not yes and start is not None:
            out.append([start,n-1]); start = None
    return out

notes = json.loads((ROOT/'semantic-notes.json').read_text())
inv = json.loads((ROOT/'inventory.json').read_text())
identities = {}
ledgers = []
forward = []
counts = collections.Counter()
metrics_assurance = []
for i, entry in enumerate(inv['primary'], 1):
    path = entry['path']
    key = f'P{i:02}'
    ident = identity(REF, R, path)
    identities[key] = ident
    assert ident['workspace_bytes_match_commit']
    assert ident['blob'] == entry['git_blob'] and ident['sha256'] == entry['sha256']
    b = (REF/path).read_bytes()
    raw = b.splitlines(keepends=True)
    lines = [x.decode('utf-8-sig').rstrip('\r\n') for x in raw]
    offsets = [0]
    for line in raw:
        offsets.append(offsets[-1]+len(line))
    attest = notes['primary'].get(path, {})
    ranges = attest.get('ranges', [])
    status = 'FULL_READ' if covered(1,len(lines),ranges) else 'PARTIAL_READ' if ranges else 'AVAILABLE_UNREAD'
    mode = attest.get('representation', 'RAW_CONTINUOUS_READ' if ranges else 'NONE')
    starts = [(n, re.match(r'^\s*\[([^]]+)\]', line).group(1))
              for n,line in enumerate(lines,1) if re.match(r'^\s*\[([^]]+)\]',line)]
    sections = []
    for j,(start, section) in enumerate(starts):
        end = starts[j+1][0]-1 if j+1 < len(starts) else len(lines)
        # The separator preceding the next header is administrative, not a field.
        fields = []
        for n in range(start+1,end+1):
            text = lines[n-1].strip()
            if not text or text.startswith('#'):
                continue
            field = re.match(r'^(\w+)\s*=', text)
            kind = field.group(1) if field else 'SLOT' if re.match(r'^\d+\s*,',text) else 'ENCOUNTER_TYPE'
            fields.append([n, kind])
        semantic_end = fields[-1][0] if fields else start
        sstatus = 'READ_NOT_ACCEPTED' if covered(start,semantic_end,ranges) else 'PARTIAL_READ_NOT_ACCEPTED' if any(a<=start<=z for a,z in ranges) else 'AVAILABLE_UNREAD'
        sid = f'{key}:S{j+1:04}'
        sections.append(dict(id=sid, section=section, lines=[start,end], byte_offsets_half_open=[offsets[start-1],offsets[end]],
                             fields_line_key=fields, status=sstatus, acceptance='PENDING_MAIN_REVIEWER'))
        counts['sections'] += 1
        counts[sstatus] += 1
        counts['physical_fields_or_type_slot_lines'] += len(fields)
        counts['read_physical_fields_or_type_slot_lines'] += sum(any(a<=n<=z for a,z in ranges) for n,_ in fields)
        group = 'FG-BASE' if path.endswith('/pokemon.txt') else 'FG-FORMS' if path.endswith('pokemon_forms.txt') else 'FG-METRICS' if path.endswith('pokemon_metrics.txt') else 'FG-ENCOUNTERS'
        forward.append([sid, group if sstatus == 'READ_NOT_ACCEPTED' else None, sstatus, 'PENDING_FULL_PER_FIELD_BIDIRECTIONAL_MAPPING'])
    entry['semantic_status'] = status
    entry['read_range'] = ranges
    entry['evidence_level'] = 'SOURCE_STATIC' if ranges else 'INVENTORY_ONLY'
    entry['identity_id'] = key
    entry['representation'] = mode
    counts[status+'_files'] += 1
    counts['bytes'] += len(b)
    counts['lines'] += len(lines)
    counts['read_line_positions'] += sum(z-a+1 for a,z in ranges)
    counts['read_bytes_in_attested_ranges'] += sum(offsets[z]-offsets[a-1] for a,z in ranges)
    if status == 'FULL_READ':
        counts['complete_read_file_bytes'] += len(b)
    if path.endswith('pokemon_metrics.txt'):
        expected = ['BackSprite','FrontSprite','ShadowX','ShadowSize']
        metrics_assurance.append(dict(identity_id=key, section_count=len(sections),
            each_section_exactly_four_unique_expected_fields=all([v for _,v in s['fields_line_key']]==expected for s in sections),
            purpose='Mechanical check that previously displayed literal structure tables did not discard duplicate/extra fields; no new semantic credit.'))
    ledgers.append(dict(identity_id=key,path=path,total_lines=len(lines),total_bytes=len(b),
                        file_status=status,representation=mode,read_ranges=ranges,unread_ranges=missing(len(lines),ranges),
                        attestation_pointer='semantic-notes.json#/primary/'+path.replace('~','~0').replace('/','~1'),
                        all_sections=sections,acceptance='PENDING_MAIN_REVIEWER'))

deps = []
formal = []
for i,(path,note) in enumerate(notes['dependencies'].items(),1):
    key=f'D{i:02}'
    repo, commit = (REF,R) if note['repo']=='R' else (SPEC,B8)
    ident=identity(repo,commit,path)
    identities[key]=ident
    status='FULL_READ' if covered(1,ident['lines'],note['ranges']) else 'PARTIAL_READ'
    deps.append(dict(identity_id=key,path=path,read_ranges=note['ranges'],unread_ranges=missing(ident['lines'],note['ranges']),
                     read_status=status,acceptance='PENDING_MAIN_REVIEWER',
                     clause_decomposition='NOT_ESTABLISHED' if repo==SPEC else 'CONTROL_FLOW_READ; CROSS_CHAIN_ACCEPTANCE_PENDING'))
    if repo==SPEC:
        ls=(SPEC/path).read_text().splitlines()
        formal.append(dict(identity_id=key,path=path,full_text_read=True,
                           physical_nonblank_nonseparator_line_positions=[n for n,l in enumerate(ls,1) if l.strip() and not re.fullmatch(r'[| :\-]+',l.strip())],
                           semantic_clause_subassertion_denominator='NOT_ESTABLISHED',
                           unmapped_semantic_subassertions='NONZERO_NOT_ENUMERATED; includes unrelated clauses and undecomposed compound clauses',
                           accepted_semantic_clauses=0))

unread_r = [
'Data/Scripts/001_Settings.rb','Data/Scripts/002_BattleSettings.rb',
'Data/Scripts/014_Pokemon/001_Pokemon.rb',
'Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb',
'Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb',
'Data/Scripts/014_Pokemon/002_Pokemon_MegaEvolution.rb',
'Data/Scripts/010_Data/001_Hardcoded data/001_GrowthRate.rb',
'Data/Scripts/010_Data/001_Hardcoded data/002_GenderRatio.rb',
'Data/Scripts/010_Data/001_Hardcoded data/003_EggGroup.rb',
'Data/Scripts/010_Data/001_Hardcoded data/004_BodyShape.rb',
'Data/Scripts/010_Data/001_Hardcoded data/005_BodyColor.rb',
'Data/Scripts/010_Data/001_Hardcoded data/006_Habitat.rb',
'Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb',
'Data/Scripts/010_Data/001_Hardcoded data/008_Stat.rb',
'Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb',
'Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb',
'Data/Scripts/011_Battle/004_Scene/006_Battle_Scene_Objects.rb',
'Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb',
'Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb',
'Data/Scripts/002_Save data/001_SaveData.rb',
'Data/Scripts/002_Save data/002_SaveData_Value.rb',
'Data/Scripts/002_Save data/003_SaveData_Conversion.rb']
unread_s = [
'generic-kernel/wp03-content-identity-and-schema.md',
'engine-overworld/wp15-resource-matching-and-audio.md',
'pokemon-rules/wp22-transformation-data.md','pokemon-rules/wp22-mega-and-primal-reversion.md',
'pokemon-rules/wp31-basic-evolution.md','pokemon-rules/wp34-inheritance-and-offspring.md',
'creature-rpg/wp30-growth-learning-and-friendship.md',
'demo-dx/wp73-a-content-editors.md','demo-dx/wp73-b-world-editors.md',
'test-catalog/generic-kernel-wp02-03-04.md','test-catalog/creature-rpg-wp18-20-24-25-26.md',
'test-catalog/pokemon-rules-wp19-21-22-23-34.md','test-catalog/creature-rpg-wp35-36-57-64-68.md',
'test-catalog/pokemon-rules-wp53-60-61-62-69-70.md']
unread_r += [p for p in git(REF,'ls-tree','-r','--name-only',R,'Data/Scripts/010_Data/002_PBS data').decode().splitlines()
             if pathlib.Path(p).name.startswith(('001_','002_','003_','004_'))]
gaps=[]
for repo,commit,paths in [(REF,R,unread_r),(SPEC,B8,['deliverables/final-specification-set/'+p for p in unread_s])]:
    for path in paths:
        key=f'U{len(gaps)+1:02}'
        identities[key]=identity(repo,commit,path)
        gaps.append(dict(identity_id=key,path=path,status='AVAILABLE_UNREAD',
                         unreceived=True,blocking='Corresponding data/consumer or formal reverse clause chain cannot close.'))

pinpaths={
'inputs/delegation-prompt.md':'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/delegation/prompts/pbs_creature_backups.md',
'inputs/primary-readset.json':'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/delegation/readsets/pbs_creature_backups.json',
'inputs/eighth-global-review-prompt.md':'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/eighth-global-review-prompt.md',
'inputs/review-SKILL.md':'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/review-SKILL.md',
'inputs/AGENTS.md':'AGENTS.md'}
for i,(copy,src) in enumerate(pinpaths.items(),1):
    ident=identity(SPEC,PIN,src) if (SPEC/src).exists() else None
    # Pinned delegation files are intentionally not checked out in this branch.
    b=git(SPEC,'show',f'{PIN}:{src}')
    tree=git(SPEC,'rev-parse',PIN+'^{tree}').decode().strip()
    mode,kind,blob=git(SPEC,'ls-tree',PIN,'--',src).decode().split('\t')[0].split()
    identities[f'I{i:02}']=dict(repo=str(SPEC),commit=PIN,tree=tree,path=src,copy=copy,mode=mode,kind=kind,
                              blob=blob,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),
                              copy_exact=(b==(ROOT/copy).read_bytes()),read_status='FULL_READ')
    assert identities[f'I{i:02}']['copy_exact']

counts['accepted_primary_sections']=0
counts['unreceived_primary_sections']=counts['sections']
counts['unread_or_partial_sections']=counts['AVAILABLE_UNREAD']+counts['PARTIAL_READ_NOT_ACCEPTED']
counts['formal_full_text_read_files']=len(formal)
counts['reference_dependency_full_read_files']=sum(d['read_status']=='FULL_READ' and identities[d['identity_id']]['repo']==str(REF) for d in deps)
counts['discovered_unread_dependency_files']=len(gaps)
counts['behavior_executions']=0
inv['utc']=UTC
inv['mechanical_only']=False
inv['identity_enumeration_mechanical_only']=True
inv['semantic_status_source']='Explicit reviewer ranges in semantic-notes.json; no parser-generated reading credit.'
write('inventory.json',inv)
write('identities.json',dict(schema='r8-task-identities/v1',utc=UTC,B8=dict(commit=B8,tree='751dfde81048c81390f89a65ca1d1a565ba8e1ca',formal_tree='f292698cdd4a8e725525a9be6dc34b75faaf151e'),
 R=dict(commit=R,tree='7589c800b61ba13a13040ed0d686979b80a84fd0',declared_upstream='Maruno17/pokemon-essentials',actual_clone_origin='https://github.com/y805939188/pokemon-essentials.git',upstream_master_commit_verified=R),
 source_thread_id='01a13f49-a154-7054-9b04-ce31f924d01c',actual_session_id='UNVERIFIED',reviewer='/root',
 actual_cloud_roots=[str(SPEC),str(REF)],historical_Mac_paths='Historical only; not mounted, not substituted for cloud paths.',payloads=identities))
write('reading-ledger.json',dict(schema='r8-task-reading-ledger/v1',utc=UTC,reviewer='/root',
 counting_rule='Sections and physical property/type/slot lines are mechanical coordinates, not a semantic subassertion denominator. FULL_READ is reading only. No final acceptance credit.',
 counts=counts,primary=ledgers,read_dependencies=deps,formal_read_decomposition_status=formal,
 semantic_subassertion_denominator='NOT_ESTABLISHED',metrics_table_representation_assurance=metrics_assurance,
 input_read_order=['I01','I02','I03','I04','I05'],input_full_reads=5))
write('gaps.json',dict(schema='r8-task-gaps/v1',utc=UTC,status='REVIEW_INCOMPLETE',
 primary_unread=[dict(identity_id=x['identity_id'],path=x['path'],ranges=x['unread_ranges']) for x in ledgers if x['unread_ranges']],
 discovered_unread_dependencies=gaps,dependency_denominator_closed=False,
 further_available_unread=['Default/alternative move, item, type and ability records and their material consumers; no creature_b contribution received.',
 'R6/R7 historical qualification/supplementary records beyond the fully read global prompt; historical current relation not independently restored.',
 'Remaining formal, test-catalog, coverage, caller, persistence/reload and resource chains as expansion requires.'],
 unreceived=['All 6712 primary sections','All selected reverse assertions','All consumer/interface handoffs','Main independent disproof and final reception'],
 material_limit_claim=False,reason='These are available-but-unread or unaccepted work, not opaque/host/material limits. No infrastructure failure prevents continued reading.'))
write('coverage.json',dict(schema='r8-task-coverage/v1',utc=UTC,counts=counts,formal_total_at_B8=131,
 semantic_forward_complete=False,semantic_reverse_complete=False,all_formal_clause_denominator='NOT_ESTABLISHED',
 known_closure_dependency_denominator=len(deps)+len(gaps),closure_dependency_denominator_exhaustive=False,
 classification_decisions=dict(required=0,optional=0,no_required_revision=0,policy=0,limit=0),
 local_questions=1,independently_decided_questions=0,NO_REQUIRED_UPDATE=False,update_started=False))

progress=json.loads((ROOT/'progress.json').read_text())
progress.update(status='FAILED',semantic_status='REVIEW_INCOMPLETE',failure_reason='Exhaustive assigned review not completed; exact available-unread and reception gaps remain.',
 start_utc='UNVERIFIED_EXACT_FIRST_ACTION',earliest_instrumented_utc='2026-10-16T07:56:45.625890+00:00',
 updated_utc=UTC,checkpoint_utc=UTC,end_utc='UNVERIFIED_UNTIL_TURN_END',
 process_state='Current reviewer context active when checkpoint written; no child launched.',
 read_complete_files=counts['FULL_READ_files'],partial_read_files=counts['PARTIAL_READ_files'],unread_files=counts['AVAILABLE_UNREAD_files'],
 read_complete_primary_sections=counts['READ_NOT_ACCEPTED'],unread_or_partial_primary_sections=counts['unread_or_partial_sections'],
 unreceived_primary_sections=counts['sections'],semantic_acceptance='PENDING_MAIN_REVIEWER',
 publication='Pending core commit and ordinary push; final publication record binds actual IDs.',update_started=False)
write('progress.json',progress)
print(json.dumps(dict(counts=counts,dependencies_read=len(deps),discovered_unread=len(gaps)),ensure_ascii=False))
