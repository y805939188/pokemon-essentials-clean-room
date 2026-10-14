import datetime
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT = ROOT / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-CA/subtasks/effects-c'
FILES = {
    'agents': 'AGENTS.md',
    's007': 'reference/pokemon-essentials/Data/Scripts/011_Battle/006_AI MoveEffects/007_AI_MoveEffects_Items.rb',
    's008': 'reference/pokemon-essentials/Data/Scripts/011_Battle/006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb',
    's009': 'reference/pokemon-essentials/Data/Scripts/011_Battle/006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb',
    'formal': 'deliverables/final-specification-set/combat-requirements/wp52-c-items-calling-and-control-evaluation.md',
    'coverage': 'deliverables/final-specification-set/combat-requirements/wp52-c-item-control-coverage-and-data.md',
    'catalog': 'deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md',
    'ai001': 'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/001_Battle_AI.rb',
    'ai005': 'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/005_AI_ChooseMove.rb',
    'ai008': 'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/008_AI_Utilities.rb',
    'ai009': 'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/009_AITrainer.rb',
    'ai010': 'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/010_AIBattler.rb',
    'ai011': 'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/011_AIMove.rb',
    'handlers': 'reference/pokemon-essentials/Data/Scripts/003_Game processing/006_Event_HandlerCollections.rb',
    'formal_b': 'deliverables/final-specification-set/combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md',
    'handlerhash': 'reference/pokemon-essentials/Data/Scripts/003_Game processing/005_Event_Handlers.rb',
    'realitems': 'reference/pokemon-essentials/Data/Scripts/011_Battle/003_Move/011_MoveEffects_Items.rb',
    'realchange': 'reference/pokemon-essentials/Data/Scripts/011_Battle/003_Move/012_MoveEffects_ChangeMoveEffect.rb',
    'realswitch': 'reference/pokemon-essentials/Data/Scripts/011_Battle/003_Move/013_MoveEffects_SwitchingActing.rb',
    'battler': 'reference/pokemon-essentials/Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb',
    'coverage_b': 'deliverables/final-specification-set/combat-requirements/wp52-b-effect-coverage.md',
    'pbs_moves': 'reference/pokemon-essentials/PBS/moves.txt',
    'ai007': 'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/007_AI_ChooseMove_OtherScores.rb',
    'targetdata': 'reference/pokemon-essentials/Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb',
    'movebase': 'reference/pokemon-essentials/Data/Scripts/011_Battle/003_Move/001_Battle_Move.rb',
    'formal51': 'deliverables/final-specification-set/combat-requirements/wp51-ai-action-selection-and-skill.md',
    'ai006': 'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/006_AI_ChooseMove_GenericEffects.rb',
    'parentfacts': 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-CA/core-facts.tsv',
    'parentforward': 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-CA/forward-core.jsonl',
    'parentreverse': 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-CA/reverse-core.jsonl',
    'parentnotes': 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-CA/core-review-notes.md',
    'parentvectors': 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-CA/vectors-core.tsv',
    'parentrebuttal': 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-CA/gr6-c-001-independent-rebuttal.md',
    'ai002': 'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/002_AI_Switch.rb',
    'ai003': 'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/003_AI_UseItem.rb',
    'battle001': 'reference/pokemon-essentials/Data/Scripts/011_Battle/001_Battle/001_Battle.rb',
    'battlestart': 'reference/pokemon-essentials/Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb',
    'battlerinit': 'reference/pokemon-essentials/Data/Scripts/011_Battle/002_Battler/002_Battler_Initialize.rb',
    'battlerchange': 'reference/pokemon-essentials/Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb',
    'debug': 'reference/pokemon-essentials/Data/Scripts/001_Technical/001_Debugging/001_PBDebug.rb',
    'itembattle': 'reference/pokemon-essentials/Data/Scripts/013_Items/003_Item_BattleEffects.rb',
    'actionitem': 'reference/pokemon-essentials/Data/Scripts/011_Battle/001_Battle/006_Battle_ActionUseItem.rb',
}
key, first, last = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
path = ROOT / FILES[key]
data = path.read_bytes()
lines = data.decode().splitlines()
last = min(last, len(lines))
assert 1 <= first <= last
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
name = f'{key}-{first}-{last}.txt'
output = '\n'.join(f'{i}: {lines[i-1]}' for i in range(first, last + 1)) + '\n'
(OUT / 'logs' / name).write_text(output)
entry = {'kind': 'actual_contiguous_read', 'path': FILES[key], 'start': first, 'end': last,
         'total': len(lines), 'sha256': hashlib.sha256(data).hexdigest(), 'time_utc': now,
         'log': 'logs/' + name, 'semantic_pass': False,
         'note': 'Actual returned text; semantic conclusions recorded separately in matrices/report.'}
with (OUT / 'reading-ledger.jsonl').open('a') as f:
    f.write(json.dumps(entry, ensure_ascii=False) + '\n')
print(output, end='')
