"""Retrieve exact immutable text for inspection; save only hashes and read ranges."""
import hashlib
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

SHA = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
ROOT = Path('review/remediation/20261003-prepare/batches/B12')
OUT = ROOT / 'affected-candidate-review-1/B02/source-reading.json'
GROUPS = {
    'item': {'003_AI_UseItem.rb': [(150,183)], '001_Battle_AI.rb': [(40,70)]},
    'item-registration': {'003_AI_UseItem.rb': [(75,100),(115,134)]},
    'encounter': {'003_Overworld_WildEncounters.rb': [(200,220),(235,265)],
                  '002_BugContest.rb': [(160,200),(350,405)]},
    'battle': {'001_Overworld_BattleStarting.rb': [(170,210),(270,330),(345,455)]},
    'ratio': {'004_AI_MoveEffects_MoveAttributes.rb': [(63,110),(382,405)]},
    'residual': {'010_AIBattler.rb': [(56,183)], '002_AI_Switch.rb': [(192,225)]},
    'consumer': {'006_AI_ChooseMove_GenericEffects.rb': [(30,49),(329,346)]},
    'pain': {'002_AI_MoveEffects_BattlerStats.rb': [(1588,1602)]},
    'step': {'001_Overworld.rb': [(177,218)]},
}
declared = json.loads((ROOT / 'author-draft-1/source-reading-log.json').read_text())['static_reads']
log = json.loads(OUT.read_text()) if OUT.exists() else {
    'reference_commit': SHA, 'repository': 'Maruno17/pokemon-essentials',
    'execution': 0, 'source_saved_or_reproduced_in_report': False, 'reads': []}
for name, ranges in GROUPS[sys.argv[1]].items():
    identity = next((x for x in declared if x['path'].split('/')[-1] == name), None)
    if identity is None:
        assert name == '001_Overworld.rb'
        identity = {'path':'Data/Scripts/012_Overworld/001_Overworld.rb'}
    url = 'https://raw.githubusercontent.com/Maruno17/pokemon-essentials/' + SHA + '/' + urllib.parse.quote(identity['path'])
    raw = urllib.request.urlopen(url, timeout=30).read()
    actual = {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
              'git_blob':hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()}
    assert all(identity[k] == actual[k] for k in actual if k in identity)
    identity.update(actual)
    record = {'path':identity['path'], 'url':url, 'git_blob':identity['git_blob'],
              'sha256':identity['sha256'], 'bytes':len(raw), 'ranges':ranges,
              'mode':'STATIC_TEXT_READ_NO_SOURCE_EXECUTION'}
    log['reads'].append(record)
    print('EXACT STATIC', identity['path'])
    lines = raw.decode().splitlines()
    assert all(end <= len(lines) for start, end in ranges)
    for start, end in ranges:
        for n in range(start, end + 1):
            print(str(n) + ': ' + lines[n-1])
OUT.write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n')
