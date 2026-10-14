"""Persist reproducible negative/location searches without copying source text."""
import audit as a, build_mappings as b
from pathlib import Path
from collections import Counter,defaultdict
import subprocess,json,re

def run():
    a.bind();root=a.ROOT
    jobs=[
      ('formal_unnamed_defaults','Unnamed',['deliverables/final-specification-set']),
      ('formal_type_field_names','IsSpecialType|IsPseudoType|special_type|icon_position',['deliverables/final-specification-set']),
      ('formal_item_names','NamePlural|PortionName|复数.{0,20}(默认|省略|缺省)|省略.{0,20}复数',['deliverables/final-specification-set']),
      ('formal_metric_author_fields','BackSprite|FrontSprite|ShadowSize|ShadowX|SpeciesMetrics',['deliverables/final-specification-set']),
      ('formal_happiness_bounds','Happiness.{0,30}(255|限制|上限|非负)|happiness.{0,30}(255|上限)|物种.{0,20}友好.{0,20}(255|钳)|友好.{0,20}0.{0,5}255',['deliverables/final-specification-set']),
      ('source_descriptive_generation_habitat','\\.habitat\\b|\\.generation\\b|:habitat\\b|:generation\\b|"Habitat"|"Generation"',['reference/pokemon-essentials/Data/Scripts']),
      ('source_backup_literals','Gen [5-8] backup|Shadow Pokémon backup',['reference/pokemon-essentials/Data/Scripts']),
      ('source_remove_all_screens','RemoveAllScreens',['reference/pokemon-essentials/Data/Scripts']),
      ('formal_remove_all_screens','RemoveAllScreens',['deliverables/final-specification-set']),
    ]
    receipts=[]
    for name,pattern,paths in jobs:
        cmd=['rg','--json','-n',pattern,*paths];p=subprocess.run(cmd,cwd=root,capture_output=True,text=True)
        assert p.returncode in {0,1},p.stderr
        hits=[]
        for line in p.stdout.splitlines():
            row=json.loads(line)
            if row['type']!='match':continue
            d=row['data'];hits.append({'path':d['path']['text'],'line':d['line_number'],'matched_line_sha256':a.sha(d['lines']['text'].encode()),'match_count':len(d['submatches'])})
        a.append('command-log.jsonl',{'time':a.now(),'command':cmd,'cwd':str(root),'exit_code':p.returncode,'stdout_sha256':a.sha(p.stdout.encode()),'purpose':name,'extent':'location/negative search only; source text not copied; not semantic read'})
        receipts.append({'search_id':name,'pattern':pattern,'paths':paths,'exit_code':p.returncode,'matching_lines':len(hits),'hits':hits,'meaning':'Exact searched forms only; a negative result does not prove every synonymous expression absent.'})
    a.save('negative-and-location-search-receipts.json',receipts)
    # Improve the class-name location join by excluding block-commented text.
    classes=defaultdict(list)
    for p in sorted((a.REF/'Data/Scripts').rglob('*.rb')):
        comment=False
        for n,line in enumerate(p.read_text().splitlines(),1):
            if re.match(r'^=begin(?:\s|$)',line):comment=True;continue
            if re.match(r'^=end(?:\s|$)',line):comment=False;continue
            if comment:continue
            m=re.match(r'\s*class Battle::Move::(\w+)\b',line)
            if m:classes[m[1]].append({'path':str(p.relative_to(root)),'line':n})
    links=b.read('move-effects-bidirectional-locations.json')
    for row in links:
        row['active_text_definition_locations']=classes.get(row['effect_identity'],[])
        row['factory_binding_scope']='Static non-block-commented declaration plus factory/fallback; no reference execution or internal-effect approval.'
    a.save('move-effects-bidirectional-locations.json',links)
    a.save('effect-active-declaration-check.json',{'records':len(links),'unlocated_records':[{'path':x['path'],'identity':x['identity'],'effect':x['effect_identity']} for x in links if not x['active_text_definition_locations']],'comment_exclusion':'Ruby column-zero block comments excluded; this is location evidence only.','status':'binding check, NOT runtime PASS'})
    print(json.dumps({'searches':[{x['search_id']:x['matching_lines']} for x in receipts],'moves':len(links),'unlocated_effect_ids':sorted({x['effect_identity'] for x in links if not x['active_text_definition_locations']})},ensure_ascii=False,indent=2))

if __name__=='__main__':
    a.append('command-log.jsonl',{'time':a.now(),'script':'search_receipts.py','script_sha256':a.sha(Path(__file__).read_bytes()),'purpose':'repeat relevant exact-form negative/location searches into persistent receipts; exclude commented effect declarations'})
    run()
