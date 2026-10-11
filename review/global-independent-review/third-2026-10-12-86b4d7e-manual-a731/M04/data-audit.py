"""Static text-table audit of inspected snapshot fields; no source compiler/execution."""
from pathlib import Path
import json,re
OUT=Path(__file__).resolve().parent
REPO=OUT.parents[3]
REF=REPO/'reference/pokemon-essentials'
def fields(path):
    result={};cur=None
    for n,line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(),1):
        line=line.strip()
        if not line or line.startswith('#'):continue
        if line.startswith('[') and line.endswith(']'):
            cur=line[1:-1];result[cur]={'_header_line':n};continue
        if cur is not None and '=' in line:
            key,value=line.split('=',1);result[cur][key.strip()]=value.strip()
    return result
forms=fields(REF/'PBS/pokemon_forms.txt')
species=fields(REF/'PBS/pokemon.txt')
items=fields(REF/'PBS/items.txt')
actual=[]
for key,d in forms.items():
    if 'MegaStone' in d or 'MegaMove' in d:
        sp,f=key.split(',');actual.append({'species':sp,'form':int(f),'condition':d.get('MegaStone',d.get('MegaMove')),'kind':'stone' if 'MegaStone' in d else 'move','stats':d['BaseStats'].replace(' ',''),'unmega_form':int(d.get('UnmegaForm','0')),'mega_message':int(d.get('MegaMessage','0')),'source_header_line':d['_header_line']})
formal=[]
p=REPO/'deliverables/final-specification-set/pokemon-rules/wp22-transformation-data.md'
for n,line in enumerate(p.read_text().splitlines(),1):
    if not line.startswith('| '):continue
    cells=[x.strip() for x in line.split('|')[1:-1]]
    if len(cells)==4 and re.fullmatch('[A-Z0-9]+',cells[0]) and cells[1].isdigit():
        formal.append({'species':cells[0],'form':int(cells[1]),'condition':cells[2].split()[-1],'stats':cells[3].replace('／',','),'formal_line':n})
a={(x['species'],x['form']):x for x in actual};bad=[]
for f in formal:
    aa=a[(f['species'],f['form'])]
    if f['condition']!=aa['condition'] or f['stats']!=aa['stats']:bad.append({'source':aa,'formal':f})
assert len(actual)==len(formal)==48 and not bad
shadow=fields(REF/'PBS/Shadow Pokémon backup/shadow_pokemon.txt')
shadow_formal=[]
for n,line in enumerate((REPO/'deliverables/final-specification-set/pokemon-rules/wp23-shadow-data-and-vectors.md').read_text().splitlines(),1):
    if not line.startswith('| '):continue
    cells=[x.strip() for x in line.split('|')[1:-1]]
    if len(cells)==3 and cells[0] in shadow and cells[1].isdigit():
        shadow_formal.append({'species':cells[0],'gauge':int(cells[1]),'moves':cells[2].replace('／',','),'formal_line':n})
shadow_bad=[]
for f in shadow_formal:
    d=shadow[f['species']]
    if f['gauge']!=int(d.get('GaugeSize','4000')) or f['moves']!=d['Moves']:shadow_bad.append({'formal':f,'source_fields':d})
assert len(shadow)==len(shadow_formal)==131 and not shadow_bad
smoves=fields(REF/'PBS/Shadow Pokémon backup/moves_shadow_pkmn.txt');sitems=fields(REF/'PBS/Shadow Pokémon backup/items_shadow_pkmn.txt');stypes=fields(REF/'PBS/Shadow Pokémon backup/types_shadow_pkmn.txt')
move_bad=[]
text=(REPO/'deliverables/final-specification-set/pokemon-rules/wp23-shadow-data-and-vectors.md').read_text()
for key,d in smoves.items():
    if not any(line.startswith('| '+key+' | '+d['FunctionCode']+' |') for line in text.splitlines()):move_bad.append(key)
assert not move_bad and len(smoves)==18 and len(sitems)==4 and len(stypes)==1
result={'kind':'ROOT_STATIC_DATA_FIELD_EQUIVALENCE_NO_COMPILATION','reviewer':'/root','reference_commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','spec_commit':'167296dbe9e2384627b0ed696e87aeb01f211252','actual_checked_fields':'48 Mega species/form/condition/6 BaseStats values against each formal row; 131 Shadow gauge and ordered moves;18 shadow function identities;4 item usage/flags and1 type text independently read','Mega48':actual,'Mega_formal48':formal,'mega_mismatches':bad,'Shadow131':shadow_formal,'shadow_mismatches':shadow_bad,'shadow_move_effect_mismatches':move_bad,'optional_shadow_not_activated':True,'root_shadow_4files_full_text_read':True,'limitations':['This small report parser is only field extraction of the inspected legal snapshot, not an implementation/reference compiler/PBS parser compatibility proof.','Gen5–8 backup/full pokemon/metrics content semantics are not promoted.','No source execution, compilation, runtime or behavioral/static case execution.']}
(OUT/'data-field-equivalence.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'Mega48_fields_match':not bad,'Shadow131_fields_match':not shadow_bad,'Shadow18_effects_match':not move_bad,'source_or_case_execution':0}))
