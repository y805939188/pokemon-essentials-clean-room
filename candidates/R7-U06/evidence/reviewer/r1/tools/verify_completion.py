"""Validate artifact declarations, supplemental identities and fixed arithmetic.

This does not execute source, author programs, behavior vectors or a model.
"""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

OUT=Path(__file__).resolve().parents[1]
CTX=Path('/workspace/r7-context/R7-U06-reviewer')
CR=Path('/workspace/r7-review-input/R7-U06-r1-fd0c1e6f50587331846921d446d893f1c1e84f3d/candidate')
B='e646432c644dec04d306842cc5a559a29c718fbc'
REPO=Path('/workspace/r7-u06-reviewer-checkout')

def ident(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob_content_id':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}

def check(data, expected):
    actual=ident(data)
    for k,v in actual.items():
        if k in expected:assert v==expected[k],(k,v,expected[k])
    return actual

def write(name,data):
    with (OUT/name).open('x') as f:json.dump(data,f,ensure_ascii=False,indent=2);f.write('\n')

def main():
    author=json.loads((CR/'candidates/R7-U06/evidence/author/artifact-manifest.json').read_bytes())
    declared=[]
    for row in author['complete_mirrors']:
        check((CR/row['candidate_path']).read_bytes(),row['candidate'])
        base=subprocess.check_output(['git','show',B+':'+row['original_path']],cwd=REPO)
        check(base,row['original_B']);declared.append(row['candidate_path'])
    for row in author['supporting_files']:
        check((CR/row['path']).read_bytes(),row);declared.append(row['path'])
    assert len(declared)==len(set(declared))==42
    supplements=[]
    for directory in ['supplemental-plan','source-supplement','consumer-supplement']:
        plan=json.loads((OUT/'receipts'/directory/'R7-U06.json').read_bytes())
        for group in ['artifacts','evidence','fixed_read_inputs']:
            for row in plan[group]:supplements.append({'path':row['local_path'],**check((CTX/row['local_path']).read_bytes(),row)})
    for p in CTX.glob('recovery-receipt-*.json'):
        target=OUT/'receipts'/p.name
        if target.exists():assert target.read_bytes()==p.read_bytes()
        else:shutil.copyfile(p,target)
    mirrors=CR/'candidates/R7-U06/deliverables/final-specification-set'
    vcounts={}
    for name,heading in [('pokemon-rules-wp43-44-46-48-50.md','### R7-U06：形态吸收与基底求值'),('combat-requirements-wp49-51-52.md','### R7-U06：蒸汽机直接每击反应')]:
        text=(mirrors/'test-catalog'/name).read_text()
        section=text.split(heading)[1].split('\n## ')[0]
        ids=[line.split('|')[1].strip() for line in section.splitlines() if line.startswith('| ')][2:]
        assert len(ids)==len(set(ids))==15
        assert 'execution＝NOT_EXECUTED' in section
        vcounts[name]=ids
    wp49=(mirrors/'combat-requirements/wp49-ability-phase-triggers.md').read_text()
    wp46=(mirrors/'pokemon-rules/wp46-damage-multihit-and-healing.md').read_text()
    assert '#611-蒸汽机的直接每击速度请求' in wp46
    assert '### 6.1.1 蒸汽机的直接每击速度请求' in wp49
    assert not (mirrors/'pokemon-rules/wp43-types-accuracy-and-damage.md').exists()
    values={'SNEASEL_base':5+95//10,'MAGIKARP_base':5+10//10,
            'three_base_evaluations':[10,20,30],
            'water_basic':((2*20//5+2)*40*33//55)//50+2,
            'speed_stage2':35*4//2,'speed_stage6':35*8//2,
            'stage_minus4_request6':min(-4+6,6),'stage_plus5_request6':min(5+6,6)}
    assert values['SNEASEL_base']==14 and values['MAGIKARP_base']==6
    assert values['water_basic']==6 and values['water_basic']*3==18 and 100-18==82
    assert values['speed_stage2']==70 and values['speed_stage6']==140
    assert values['stage_minus4_request6']==2 and values['stage_plus5_request6']==6
    scopes={
      'Data/Scripts/011_Battle/003_Move/009_MoveEffects_MultiHit.rb':[[69,86],[155,180]],
      'Data/Scripts/011_Battle/003_Move/003_Move_UsageCalculations.rb':[[239,300]],
      'Data/Scripts/011_Battle/003_Move/002_Move_Usage.rb':[[150,204],[320,350]],
      'Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb':[[1,60],[290,428],[580,762]],
      'Data/Scripts/011_Battle/007_Other battle code/003_Battle_DamageState.rb':[[1,61]],
      'Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb':[[156,169]],
      'Data/Scripts/011_Battle/001_Battle/001_Battle.rb':[[370,410]],
      'Data/Scripts/011_Battle/002_Battler/010_Battler_UseMoveTriggerEffects.rb':[[1,80]],
      'Data/Scripts/011_Battle/002_Battler/005_Battler_StatStages.rb':[[1,155]],
      'Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb':[[48,53],[248,300],[344,365]],
      'Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb':[[1,65],[210,240]],
      'Data/Scripts/003_Game processing/005_Event_Handlers.rb':[[148,205]],
      'Data/Scripts/011_Battle/005_AI/008_AI_Utilities.rb':[[99,159]],
      'Data/Scripts/011_Battle/006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb':[[135,186]],
      'Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb':[[130,225]],
      'Data/Scripts/001_Settings.rb':[[11,20]],
      'Data/Scripts/002_BattleSettings.rb':[[1,50],[95,140]],
      'PBS/moves.txt':[[632,642],[2243,2253],[2782,2793],[8591,8601]],
      'PBS/pokemon.txt':[[159,180],[3402,3415],[5665,5679],[6244,6263],[14471,14502],[20092,20106],[21557,21581],[22519,22541]],
      'PBS/pokemon_forms.txt':[[2241,2248]],'PBS/types.txt':[[1,129]],'PBS/abilities.txt':[[965,982]]}
    readset=[{'repository':'Maruno17/pokemon-essentials','commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','path':p,'read_lines':ranges,**ident((CTX/'inputs/reference'/p).read_bytes()),'qualification':'NAMED_SOURCE_STATIC_READ; OTHER_RANGES_UNCLAIMED'} for p,ranges in scopes.items()]
    write('receipts/source-read-set.json',readset)
    write('receipts/completion-validation.json',{'stage':'TOOL_VALIDATION','declared_author_files_verified':len(declared),'supplemental_files_verified':supplements,'new_vector_ids':vcounts,'constant_arithmetic':values,'behavior_vectors':'NOT_EXECUTED','reference_or_behavior_model_processes':0,'full_reference_tree_verification':False,'semantic_PASS_from_tool':False})
    print(json.dumps({'author_manifest_nonself_files':len(declared),'supplements':len(supplements),'new_vectors':sum(map(len,vcounts.values())),'constant_arithmetic':values,'stage':'TOOL_VALIDATION_ONLY'},ensure_ascii=False))

if __name__=='__main__':main()
