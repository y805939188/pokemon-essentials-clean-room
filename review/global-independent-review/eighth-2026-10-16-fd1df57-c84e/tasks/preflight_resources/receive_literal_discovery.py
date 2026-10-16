"""Persist explicit classifications made after reading all 67 new scan candidates."""
from pathlib import Path
import datetime, json
O=Path(__file__).resolve().parent
j=json.loads((O/'current-literal-discovery.json').read_text())
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
cnotes={
137:'Generated value assignment casts one substituted unsigned-hex value to VALUE; substitution producer and destination type context unproved.',
139:'Generated str assignment casts one substituted unsigned-hex value to VALUE; source object and GC effects unproved.',
152:'Generated ary assignment casts one substituted unsigned-hex value to VALUE; array identity and native control flow unproved.',
155:'Generated hash assignment casts one substituted unsigned-hex value to VALUE; object identity and lifetime unproved.',
160:'Generated flag assignment casts one substituted unsigned-hex value to VALUE; surrounding branch and meaning unproved.',
170:'Generated obj assignment casts one substituted unsigned-hex value to VALUE; surrounding type guard and native selection unproved.',
171:'Generated pushval assignment casts one substituted unsigned-hex value to VALUE; actual stack effect and source lifetime unproved.',
181:'Conditional-compilation opening directive for OPT_CALL_THREADED_CODE; its associated branches and assembly order are outside this literal.',
195:'Generated key assignment casts one substituted unsigned-hex value to VALUE; actual hash lookup semantics not established by this fragment.',
214:'ALWAYS_INLINE static VALUE function declaration template has two substituted integer name parts and ec,frame,self,iseq parameters; no body here.',
215:'Static-inline VALUE function opening template has two substituted integer name parts and ec,frame,self,iseq parameters; body and concatenation unknown.',
218:'VALUE function opening template takes a substituted name and ec/frame parameters; body and producer unknown.',
263:'VALUE v assignment begins a ractor_select request using ec,rs and array length, with trailing argument list incomplete; no Ractor behavior inferred.'
}
out=[]; facts=json.loads((O/'forward-map.json').read_text())
# The existing file is a wrapper; its facts field is the canonical list.
if isinstance(facts,list): factrows=facts
else:
 facts['updated_utc']=now
 factrows=facts['facts']
for r in j['rows']:
 if r['contained_in_known']: continue
 n=int(r['id'].rsplit('-',1)[1]); s={k:r[k]for k in ['id','path','start','end_exclusive','bytes','sha256','rules']}
 if n in cnotes:
  s.update(reading_status='FULL_READ_CONDITIONAL_FRAGMENT',classification='ADDITIONAL_C_GENERATOR_FRAGMENT',semantic_note=cnotes[n])
  factrows.append(dict(id='RES-SUP-'+r['id'],reader='/root/preflight_resources',summary=cnotes[n],source={k:r[k]for k in ['path','start','end_exclusive','sha256']},consumer='Native generator construction/activation/substitution remains L04',spec='No new required clause inferred; conditional literal fact',premise='Full literal read; no complete generated function, producer, caller or native execution recovered',evidence_level='SOURCE_STATIC',execution_status='NOT_EXECUTED',disposition='CONDITIONAL_LITERAL_FACT_NATIVE_SELECTION_LIMIT_L04'))
 elif n==17:
  s.update(reading_status='FULL_READ_SCANNER_BOUNDARY',classification='KNOWN_SHADER_PLUS_ADJACENT_BYTE',semantic_note='Known PC-0017 complete sample-copy shader is followed by one printable I byte in scanner run; it is not a new shader statement or a new program.')
 else:
  s.update(reading_status='FULL_READ_NONPROGRAM_LITERAL',classification='NONPROGRAM_DIAGNOSTIC_OR_METADATA',semantic_note='Full short candidate read: diagnostic, name, version banner or status text. Marker alone does not make this a coherent Ruby/C/JavaScript program.')
 out.append(s)
assert len(out)==67 and sum(x['classification']=='ADDITIONAL_C_GENERATOR_FRAGMENT'for x in out)==13
save=lambda p,v:(O/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
save('literal-discovery-reception.json',dict(created_utc=now,reader='/root/preflight_resources',source='current-literal-discovery.json',rows=out,counts={'new_candidates_full_read':67,'additional_C_fragments':13,'nonprogram_diagnostic_or_metadata':53,'known_shader_boundary':1},qualification='All candidates selected by the exact five ASCII rules have known-read-unit or new full-read dispositions. This closes only that finite rule set, not all readable binary material, Unicode/UTF16/compressed inputs, alternative grammar, native CFG or host behavior.',independent_acceptance='PENDING'))
save('forward-map.json',facts)
ledger=json.loads((O/'reading-ledger.json').read_text());ledger['updated_utc']=now
ledger['rows'].append(dict(owner='/root/preflight_resources',repo='R',path='Game.exe;x64-msvcrt-ruby310.dll;zlib1.dll;animmaker.exe;extendtext.exe',evidence_level='SOURCE_STATIC',ranges='all5exact ASCII-run marker rules,315 candidates:248 contained in previously full-read units;67 newly fully read',structural_units='13 additional Cfragments,53 nonprogram text,1 known shader boundary among67 new candidates',reading_status='FULL_READ_FINITE_SCANNER_CANDIDATE_SET',accepted=False,remarks='Current fixed bytes independently scanned; exact rules and exclusions in current-literal-discovery.json. Does not prove full binary discovery or native selection.'))
save('reading-ledger.json',ledger)
finding=json.loads((O/'findings.json').read_text());finding['created_utc']=now
finding['examined_nonfindings'].append(dict(id='RES-OBS-SUP',source='Independent exact-rule current ASCII scan:315candidate sets received;67new short candidates fully read,13 additionalCfragments',formal='L04/L05 and conditional literal boundaries',result='No additional complete active program or formal mismatch established; 13 templates added as finite conditional facts.',premise='Only five exact ASCII rules; Unicode/UTF16/compression/other grammar and native producer remain open',independent_counterreview='PENDING'))
save('findings.json',finding)
progress=json.loads((O/'progress.json').read_text());progress['updated_utc']=now
progress['outputs'].extend(['resource-report.md','current-literal-discovery.json','literal-discovery-reception.json'])
progress['remaining']=[x.replace('native other-body/literal-discovery residual disposition','native other-body and non-ASCII/alternative-grammar discovery residual disposition')for x in progress['remaining']]
save('progress.json',progress)
print(json.dumps({'candidates_received':315,'new_read':67,'new_C_fragments':13,'all_C_fragments_read_at_least':659,'forward_facts':len(factrows),'behavior_executions':0}))
