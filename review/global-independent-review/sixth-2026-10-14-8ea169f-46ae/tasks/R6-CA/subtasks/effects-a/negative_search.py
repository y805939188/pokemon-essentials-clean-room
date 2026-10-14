"""Bound read-only searches; captures commands, exit codes and actual stdout."""
from pathlib import Path
import subprocess,json
R=Path(__file__).resolve().parent
scripts='reference/pokemon-essentials/Data/Scripts'
formal='deliverables/final-specification-set'
jobs=[['rg','-n',r'ai\.battlers\.any\?',scripts],
 ['rg','-n',r'@battlers\[[^]]+\]\s*=\s*nil|@battlers\.compact|@battlers\.delete',scripts+'/011_Battle'],
 ['rg','-n','空席|空槽|稀疏|非对称|不对称',formal+'/combat-requirements/wp51-ai-action-selection-and-skill.md',formal+'/combat-requirements/wp52-a-generic-numerical-and-status-evaluation.md',formal+'/combat-requirements/wp52-a-evaluation-coverage-and-data.md',formal+'/test-catalog/combat-requirements-wp49-51-52.md'],
 ['rg','-n','AddSpikesToFoeSide|AddToxicSpikesToFoeSide|AddStealthRocksToFoeSide|AddStickyWebToFoeSide|5.2 危害',formal+'/combat-requirements/wp52-b-effect-coverage.md',formal+'/combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md']]
out=[]
for cmd in jobs:
 x=subprocess.run(cmd,text=True,capture_output=True)
 out.append({'argv':cmd,'exit_code':x.returncode,'stdout':x.stdout,'stderr':x.stderr,'evidence':'NEGATIVE_SEARCH_NOT_FULL_READ'})
(R/'logs/negative-searches.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
