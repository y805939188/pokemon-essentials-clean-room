"""Freeze only the additional finite caller units actually read by this receiver.

No gameplay or recovered helper is executed. The R working copy is checked
against its pinned Git objects before any selected text is recorded.
"""
import hashlib
import json
from pathlib import Path
import subprocess

T = Path(__file__).resolve().parents[1]
R = Path('/workspace/pokemon-essentials')
REV = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
S = 'Data/Scripts/'
specs = [
 ('HEAL', '014_Pokemon/001_Pokemon.rb', [(274,306)]),
 ('DRAIN', '011_Battle/003_Move/010_MoveEffects_Healing.rb', [(170,215),(385,402),(454,585),(671,695)]),
 ('TRANSFER', '011_Battle/003_Move/011_MoveEffects_Items.rb', [(379,470)]),
 ('GIFT', '011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb', [(1338,1380)]),
 ('CONTROL', '011_Battle/003_Move/013_MoveEffects_SwitchingActing.rb', [(261,419),(442,647)]),
 ('BEAK', '011_Battle/003_Move/005_MoveEffects_Misc.rb', [(687,693)]),
 ('NO_RETREAT', '011_Battle/003_Move/006_MoveEffects_BattlerStats.rb', [(596,613)]),
 ('OTHER', '011_Battle/001_Battle/008_Battle_ActionOther.rb', [(31,175)]),
 ('SWITCH', '011_Battle/001_Battle/005_Battle_ActionSwitching.rb', [(1,226),(274,297)]),
 ('RUN', '011_Battle/001_Battle/007_Battle_ActionRunning.rb', [(1,160)]),
 ('ITEM_ACTION', '011_Battle/001_Battle/006_Battle_ActionUseItem.rb', [(1,149)]),
 ('COMMAND', '011_Battle/001_Battle/009_Battle_CommandPhase.rb', [(1,157)]),
 ('ACTION', '011_Battle/001_Battle/010_Battle_AttackPhase.rb', [(1,100),(176,202)]),
 ('EXP', '011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb', [(1,271)]),
 ('END', '011_Battle/001_Battle/002_Battle_StartAndEnd.rb', [(405,512)]),
 ('EOR', '011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb', [(1,781)]),
 ('CATCH', '011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb', [(1,107),(164,201)]),
 ('WORLD_END', '012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb', [(306,329)]),
 ('FACILITY_END', '018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb', [(39,99)]),
 ('CONTEST_END', '018_Alternate battle modes/002_BugContest.rb', [(301,308)]),
 ('ACCURACY', '011_Battle/003_Move/003_Move_UsageCalculations.rb', [(84,170)]),
 ('ABILITY_CALLBACKS', '011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb', [(305,309),(341,345),(1093,1191),(2553,2569),(3204,3208)]),
 ('ITEM_CALLBACKS', '011_Battle/007_Other battle code/009_Battle_ItemEffects.rb', [(551,584),(693,719),(1628,1663),(1669,1691),(1894,1898),(1944,1948)]),
 ('DATABOX', '011_Battle/004_Scene/006_Battle_Scene_Objects.rb', [(1,413),(418,506)]),
 ('SCENE', '011_Battle/004_Scene/004_Scene_PlayAnimations.rb', [(93,179),(184,214),(221,232),(283,327)]),
 ('ANIMATION_BASE', '011_Battle/004_Scene/007_Battle_Scene_BaseAnimation.rb', [(1,66)]),
 ('SPLASH_ANIMATION', '011_Battle/004_Scene/008_Battle_Scene_Animations.rb', [(220,253)]),
]

def git(*args):
    return subprocess.check_output(['git', '-C', str(R), *args])

assert git('rev-parse', 'HEAD').decode().strip() == REV
records = []
for ident, rel, ranges in specs:
    path = S + rel
    raw = git('show', REV + ':' + path)
    assert raw == (R / path).read_bytes(), path
    lines = raw.decode().splitlines(keepends=True)
    assert all(1 <= a <= b <= len(lines) for a,b in ranges), path
    records.append(dict(id=ident, commit=REV, path=path,
      blob=git('rev-parse', REV+':'+path).decode().strip(),
      parent_bytes=len(raw), parent_sha256=hashlib.sha256(raw).hexdigest(),
      units=[dict(first=a,last=b,text=''.join(lines[a-1:b])) for a,b in ranges],
      purpose='ACTUALLY_PRESENTED_NECESSARY_CALLER_TEXT; not another primary domain vote'))
(T/'evidence/final-finite-sources.json').write_text(json.dumps(dict(
 schema='r8-battler-additional-finite-caller-units/v1', records=records,
 reading='Literal command outputs in the active receive_external_com_battler conversation; boundary repairs separately presented. No invented exported transcript.',
 execution='NOT_EXECUTED', semantic_credit_from_hashes=0,
 UPDATE_NOT_STARTED=True), ensure_ascii=False, indent=2)+'\n')
print('FROZEN', len(records), 'finite caller source parents; identity only, no gameplay')
