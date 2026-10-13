"""Literal-data comparison only; no source loading, game/model or UI execution."""
import ast
import collections
import csv
import json
import pathlib
import re

W = pathlib.Path('/Users/dingshinn/.codex/worktrees/review-fifth-9366d9d/pokemon-framework-reference')
R = pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
O = pathlib.Path(__file__).resolve().parents[1]
F = W / 'deliverables/final-specification-set'

def constant_data(path, name):
    text = (R/path).read_text()
    start = re.search(r'^  '+name+r'\s*=\s*\[',text,re.M).end()-1
    depth = 0
    for end in range(start,len(text)):
        c=text[end]
        if c=='[':depth+=1
        if c==']':depth-=1
        if depth==0:break
    data=re.sub(r'#.*','',text[start:end+1])
    data=re.sub(r':([A-Z][A-Z0-9_]*)',r'"\1"',data)
    return ast.literal_eval(data)

def rows(path):
    for number,line in enumerate(path.read_text().splitlines(),1):
        if line.startswith('| '):yield number,[x.strip().strip('`') for x in line.split('|')[1:-1]]

def pbs(path):
    result=[]
    for ln,line in enumerate((R/path).read_text(encoding='utf-8-sig').splitlines(),1):
        line=line.split('#',1)[0].strip()
        if not line:continue
        if line.startswith('['):result.append({'key':line[1:-1],'line':ln,'fields':[]})
        elif '=' in line:
            k,v=line.split('=',1);result[-1]['fields'].append({'key':k.strip(),'value':v.strip(),'line':ln})
        else:result[-1]['fields'].append({'key':None,'value':line,'line':ln})
    return result

mining='Data/Scripts/017_Minigames/006_Minigame_Mining.rb'
items=constant_data(mining,'ITEMS');irons=constant_data(mining,'IRON')
item_rows=[(ln,x) for ln,x in rows(F/'user-interface/wp70-mining-data.md') if len(x)==6 and x[0].isdigit()]
iron_rows=[(ln,x) for ln,x in rows(F/'user-interface/wp70-mining-data.md') if len(x)==4 and x[0].isdigit()]
assert len(items)==len(item_rows)==61 and len(irons)==len(iron_rows)==13
comparisons=[]
for i,(raw,(ln,row)) in enumerate(zip(items,item_rows),1):
    ident,weight,gx,gy,width,height,mask=raw
    shape='/'.join(''.join('#' if q else '.' for q in mask[y*width:(y+1)*width]) for y in range(height))
    expected=[str(i),ident,str(weight),f'{width}×{height}',str(sum(mask)),shape]
    comparisons.append({'kind':'mining_item','ordinal':i,'identity':ident,'source_line':150+i,'formal_line':ln,'all_rule_fields_equal':row==expected,'resource_origin':[gx,gy],'resource_origin_disposition':'explicitly outside future-layout prescription in current appendix; source resource contract available, no media execution'})
for i,(raw,(ln,row)) in enumerate(zip(irons,iron_rows),1):
    gx,gy,width,height,mask=raw
    shape='/'.join(''.join('#' if q else '.' for q in mask[y*width:(y+1)*width]) for y in range(height))
    comparisons.append({'kind':'mining_iron','ordinal':i,'source_line':213+i,'formal_line':ln,'all_rule_fields_equal':row==[str(i),f'{width}×{height}',str(sum(mask)),shape],'resource_origin':[gx,gy]})

slot=constant_data('Data/Scripts/017_Minigames/003_Minigame_SlotMachine.rb','ICONS_SETS')
names=['樱桃','小磁怪','大舌贝','皮卡丘','可达鸭','红 7','蓝 7','重玩']
slot_rows=[(ln,x) for ln,x in rows(F/'user-interface/wp69-slot-reels.md') if len(x)==4 and x[0].isdigit()]
for i,(ln,row) in enumerate(slot_rows):
    comparisons.append({'kind':'slot_position','ordinal':i,'formal_line':ln,'all_rule_fields_equal':row==[str(i)]+[names[reel[i]] for reel in slot]})
frequency_rows=[(ln,x) for ln,x in rows(F/'user-interface/wp69-slot-reels.md') if len(x)==4 and x[0] in names]
for ln,row in frequency_rows:
    value=names.index(row[0]);counts=[reel.count(value) for reel in slot]
    comparisons.append({'kind':'slot_frequency','identity':row[0],'formal_line':ln,'all_rule_fields_equal':list(map(int,row[1:]))==counts})

layouts=constant_data('Data/Scripts/017_Minigames/004_Minigame_VoltorbFlip.rb','TILE_DISTRIBUTIONS')
layout_rows=[(ln,x) for ln,x in rows(F/'pokemon-rules/wp69-voltorb-layouts.md') if len(x)==9 and x[0].isdigit()]
index=0
for level,group in enumerate(layouts,1):
    for ordinal,data in enumerate(group,1):
        bombs,twos,threes,f,g=data;ln,row=layout_rows[index];index+=1
        expected=[level,ordinal,bombs,twos,threes,25-bombs-twos-threes,f,g,2**twos*3**threes]
        comparisons.append({'kind':'voltorb_candidate','level':level,'ordinal':ordinal,'formal_line':ln,'all_rule_fields_equal':list(map(int,row))==expected})
assert index==75==len(layout_rows)

regions=pbs('PBS/regional_dexes.txt')
for region in regions:
    flat=[]
    for line in region['fields']:
        flat += [{'identity':s,'source_line':line['line'],'regional_number':len(flat)+i+1} for i,s in enumerate(line['value'].split(','))]
    region['ordered_members']=flat
    region['duplicate_identities']=[x for x,c in collections.Counter(q['identity'] for q in flat).items() if c>1]
    region['consumer_contract']='Exact ordered member identities, compiler duplicate rejection, 1-based regional number, no offset by default; names/map projection use configured list index, not region name.'

town=pbs('PBS/town_map.txt')
for region in town:
    region['point_records']=[{'source_line':q['line'],'values':next(csv.reader([q['value']]))} for q in region['fields'] if q['key']=='Point']
    region['consumer_contract']='Point order feeds first-match name/details/healing queries; same coordinate habitat visibility is a union; switch-field wallmap hiding is separate; only valid visited or debug-enabled healing triple can be chosen.'

phone=pbs('PBS/phone.txt')
for record in phone:
    record['field_counts']=dict(collections.Counter(q['key'] for q in record['fields']))
    record['consumer_contract']='Repeated field text forms ordered random candidate lists; missing current-version record falls to start-version record then default record. Fields are consumed from that selected record; a missing field does not separately fall through records. Segments split at message separator, per-call TP/TE draw reused; no demo registration or playback proof.'

maps=pbs('PBS/map_metadata.txt')
map_projection=[]
for record in maps:
    fields=[q for q in record['fields'] if q['key'] in ['Name','MapPosition','MapSize','Flags','HealingSpot']]
    map_projection.append({'map':record['key'],'source_line':record['line'],'fields':fields,'consumer_contract':'Map-position region gate; name fallback, NoPhoneSignal/HideEncountersInPokedex flags; cursor uses only shape length while habitat reads each character.'})

item_fields={r['key']:r for r in pbs('PBS/items.txt')}
mining_pockets=[]
for identity in dict.fromkeys(row[0] for row in items):
    record=item_fields[identity];pocket=next(q for q in record['fields'] if q['key']=='Pocket')
    mining_pockets.append({'identity':identity,'record_line':record['line'],'pocket_line':pocket['line'],'pocket':int(pocket['value']),'expected_pocket':2 if identity in ['REVIVE','MAXREVIVE'] else 1})

report={'schema_version':'gr5.M11-data-comparison.v1','evidence_level':'TOOL_VALIDATION','not_behavior_execution':True,'parser_limits':'Known literal integer/symbol array grammar only; no Ruby eval. PBS decoder for fields relevant to these fixed files only, not a general compiler substitute. Manual source and contract review is separate.','comparisons':comparisons,'literal_mismatches':[q for q in comparisons if not q['all_rule_fields_equal']],'mining_pockets':mining_pockets,'regional_dexes':regions,'town_maps':town,'phone_messages':phone,'map_metadata_projection':map_projection}
(O/'data-comparison.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'literal_rows':len(comparisons),'literal_mismatches':len(report['literal_mismatches']),'regional_members':{r['key']:len(r['ordered_members']) for r in regions},'town_points':{r['key']:len(r['point_records']) for r in town},'phone_fields':{r['key']:r['field_counts'] for r in phone},'mining_pockets':mining_pockets,'maps':map_projection},ensure_ascii=False))
