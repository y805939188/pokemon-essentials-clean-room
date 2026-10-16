"""Assemble exact reception ledgers from already-read immutable inputs.

This assembler is not the semantic reader. Human continuous reading ranges and
their limits are explicitly recorded below. No target program is executed.
"""
from pathlib import Path
import json,gzip,hashlib,collections,datetime,subprocess
ROOT=Path(__file__).resolve().parent
IN=ROOT.parent/'binary_remaining_texts'/'ruby-zlib-subtask'
R=Path('/workspace/pokemon-essentials')
B=Path('/workspace/pokemon-essentials-clean-room')
FORMAL='deliverables/final-specification-set/'
RCOMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BCOMMIT='fd1df570cad987dc3852a3b958f03916e317f7fe'
UTC=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def write(n,x):
 (ROOT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def rows(p):
 with gzip.open(p,'rt') as f:return [json.loads(l) for l in f]
def identity(root,path,commit):
 data=(root/path).read_bytes()
 git=subprocess.run(['git','-C',str(root),'show',commit+':'+path],capture_output=True,check=True)
 assert git.stdout==data,(root,path,'working bytes differ from frozen commit')
 blob=subprocess.run(['git','-C',str(root),'rev-parse',commit+':'+path],capture_output=True,text=True,check=True).stdout.strip()
 return dict(path=path,bytes=len(data),sha256=sha(data),git_blob=blob,commit=commit,line_count=len(data.splitlines()),frozen_bytes_equal=True)
C=rows(ROOT/'candidate-contexts.jsonl.gz')
U=rows(IN/'readset.jsonl.gz')
O=rows(IN/'unread.jsonl.gz')
T={u['read_id']:u for u in U}
assert len(C)==len(O)==20907 and len(U)==13574
assert {c['candidate_id'] for c in C}=={c['candidate_id'] for c in O}
assert sum(len(u['refs']) for u in U)==20907
setsha=sha(('\n'.join(sorted(c['candidate_id'] for c in C))+'\n').encode())
assert setsha=='8cdc30800211e75e7f04abc71eb242b88712bbe00222aac6fb7e9a682c5873e6'
P=json.loads((ROOT/'new-program-inventory.json').read_text())['units']
Y=json.loads((ROOT/'yarb-decoded.json').read_text())
CS=json.loads((ROOT/'complete-cstrings.json').read_text())
program_of={cid:u['name'] for u in P for cid in u['candidate_ids']}
cstr_of=collections.defaultdict(list)
for i,s in enumerate(CS,1):
 for cid in s['candidate_ids']:cstr_of[cid].append(i)

# These source ranges were actually read, including complete relevant methods.
source_ranges={
 'scripts_extract.rb':[[1,183]],
 'scripts_combine.rb':[[1,183]],
 'mkxp.json':[[1,159]],
 'Data/Scripts/001_Technical/001_MKXP_Compatibility.rb':[[1,None]],
 'Data/Scripts/001_Technical/002_Files/001_FileTests.rb':[[270,330]],
 'Data/Scripts/001_Technical/005_PluginManager.rb':[[510,660]],
 'Data/Scripts/001_Technical/003_Intl_Messages.rb':[[1,189],[502,566]],
 'Data/Scripts/020_Debug/002_Animation editor/004_AnimEditor_ExportImport.rb':[[1,130]],
 'Data/Scripts/020_Debug/002_Animation editor/001_AnimEditor_SceneElements.rb':[[1,115]],
 'Data/Scripts/016_UI/024_UI_MysteryGift.rb':[[300,370]],
 'Data/Scripts/002_Save data/001_SaveData.rb':[[1,None]],
 'Data/Scripts/002_Save data/003_SaveData_Conversion.rb':[[162,215]],
 'Data/Scripts/003_Game processing/004_Interpreter_Commands.rb':[[180,255]],
 'Data/Scripts/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb':[[1,55]],
 'Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb':[[1,215]],
 'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb':[[85,153]],
 'Data/Scripts/016_UI/013_UI_Load.rb':[[278,358]],
 'Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb':[[473,763]],
}
formal_ranges={
 'generic-kernel/wp07-diagnostics-files-http.md':[[1,128]],
 'generic-kernel/wp05-events-extensions-plugins.md':[[72,128]],
 'generic-kernel/wp08-localization.md':[[98,124]],
 'generic-kernel/wp09-save-startup-continue.md':[[1,190]],
 'demo-dx/wp74-battle-animation-authoring-and-exchange.md':[[1,105],[356,374]],
 'demo-dx/wp75-project-conversion-and-authoring-tools.md':[[290,360]],
 'creature-rpg/wp64-mail-and-mystery-gift.md':[[81,100]],
}
source_evidence=[]
formal_evidence=[]
for p,rg in source_ranges.items():
 ident=identity(R,p,RCOMMIT)
 ident['actually_read_line_ranges']=[[a,min(z if z is not None else ident['line_count'],ident['line_count'])] for a,z in rg]
 ident['entire_file_read']=ident['actually_read_line_ranges']==[[1,ident['line_count']]]
 ident['credit']='Actual complete displayed ranges; boundary methods outside these ranges are not claimed complete.'
 source_evidence.append(ident)
for p,rg in formal_ranges.items():
 ident=identity(B,FORMAL+p,BCOMMIT)
 ident['actually_read_line_ranges']=[[a,min(z,ident['line_count'])] for a,z in rg]
 ident['entire_file_read']=ident['actually_read_line_ranges']==[[1,ident['line_count']]]
 ident['credit']='Only the stated B8 clauses/ranges; no credit for other formal documents.'
 formal_evidence.append(ident)
write('consumer-source-identities.json',dict(source=source_evidence,formal=formal_evidence))

consumers=[
 dict(id='HOST',sources=['mkxp.json','Data/Scripts/001_Technical/001_MKXP_Compatibility.rb'],facts=['UTF-8 default internal/external encoding and $VERBOSE=nil are explicitly configured in R.','Host configuration is data; no native/OS/GUI behavior has been executed.'],formal=['generic-kernel/wp07-diagnostics-files-http.md:1-128'],limits=['No promise that every compiled runtime capability is called by the default game.']),
 dict(id='TOOLS',sources=['scripts_extract.rb','scripts_combine.rb'],facts=['Archive entries are Marshal-loaded and per-script compressed bytes inflated; text CR removal precedes output.','Combine wraps source in per-entry deflate then Marshal output, with explicit folder/archive entry points.','The literal compressed loader payload is not decoded here; its separate parent preflight ownership is not borrowed as reading credit.'],formal=['demo-dx/wp75-project-conversion-and-authoring-tools.md:290-360'],limits=['No tool run; no write/rollback result observed.']),
 dict(id='PLUGINS',sources=['Data/Scripts/001_Technical/005_PluginManager.rb:510-660'],facts=['Compile collects script files, deflates each, Marshal-dumps the list, then invokes GC.start.','Runtime registers plugin metadata before each script inflate/UTF-8/tab conversion; inflate/conversion precede the local eval exception protection.','The eval protection catches Exception and reports/exits; completed metadata and earlier script effects have no local rollback.'],formal=['generic-kernel/wp05-events-extensions-plugins.md:72-128'],limits=['No independent normative defect proposed from broad exception wording; additional global review may qualify that contract.']),
 dict(id='INTL',sources=['Data/Scripts/001_Technical/003_Intl_Messages.rb:1-189','Data/Scripts/001_Technical/003_Intl_Messages.rb:502-566','Data/Scripts/001_Technical/002_Files/001_FileTests.rb:270-330'],facts=['Gather reads/inflates archive scripts and plugin scripts, using UTF-8 on plugin payloads, and processes map/common text; Hangup handling does not make ordinary decode failures empty text.','Default core/game message files use Marshal.load in pbRgssOpen and type validation; local rescue resets both arrays.','pbRgssOpen temporarily requests Marshal.neverload around archive load_data; this does not redefine the recovered native Marshal.load wrapper.'],formal=['generic-kernel/wp08-localization.md:98-124','generic-kernel/wp07-diagnostics-files-http.md:1-128']),
 dict(id='ANIMATION',sources=['Data/Scripts/020_Debug/002_Animation editor/004_AnimEditor_ExportImport.rb:1-130','Data/Scripts/020_Debug/002_Animation editor/001_AnimEditor_SceneElements.rb:1-115'],facts=['Single animation exchange is Marshal.dump -> Zlib deflate -> pack(m) -> CRLF; import reverses it through Marshal.restore.','Object/type/conversion/slot substitution are locally protected; post-substitution canvas work is later. Cancel does not submit a new selection.','Clipboard holds serialized bytes: data reloads a fresh object and setData dumps before replacing typekey.'],formal=['demo-dx/wp74-battle-animation-authoring-and-exchange.md:356-374']),
 dict(id='GIFTS',sources=['Data/Scripts/016_UI/024_UI_MysteryGift.rb:331-349'],facts=['Gift encoding is Marshal.dump -> deflate -> pack(m). Empty decode input returns []; nonempty uses unpack(m), inflate and Marshal.restore.','Item entries are normalized by GameData::Item.get; Pokemon entries retain the same loaded object. The decode helper has no local rescue.'],formal=['creature-rpg/wp64-mail-and-mystery-gift.md:81-100']),
 dict(id='SAVE',sources=['Data/Scripts/002_Save data/001_SaveData.rb','Data/Scripts/002_Save data/003_SaveData_Conversion.rb:162-215','Data/Scripts/016_UI/013_UI_Load.rb:278-358'],facts=['The reader accepts one Hash or the legacy sequence until EOF; conversion writeback and ordinary save open wb before Marshal.dump.','Conversion creates the .bak serialization before conversions run; language selection writes the updated option to the already loaded save data directly.','Marshal.load is the recovered builtin wrapper; it delegates actual deserialization to native marshal_load.'],formal=['generic-kernel/wp09-save-startup-continue.md:125-163'],limits=['Native object reconstruction format, malformed stream outcomes, actual file effects and full migration policy are outside the recovered wrapper.']),
 dict(id='COPY_AND_REPLAY',sources=['Data/Scripts/003_Game processing/004_Interpreter_Commands.rb:223-250','Data/Scripts/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb:13-22','Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb:1-188','Data/Scripts/018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb:101-153','Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb:473-763'],facts=['Marshal round trips supply independent event/page/encounter copies.','Recorded battle properties serialize nested party/items/rules and replay restores them; top-level record restoration precedes selecting the playback kind.'],formal=[],limits=['These are concrete R consumers, not a claim to reread all battle/compiler domain specifications.']),
 dict(id='VM_BUILTINS',sources=['x64-msvcrt-ruby310.dll:builtin_binary','new-program-inventory.json','rb_load_with_builtin_functions.objdump.stdout','ibf_load_setup_bytes.lto_priv.0.objdump.stdout','ibf_load_small_value.isra.0.objdump.stdout'],facts=['All 16 real containers match actual COFF starts, header lengths, registry pointers and sizes.','16 ruby_opt_init.part.0 calls pass the registry feature and its builtin table; gem_prelude has a null builtin table.','All 120 R operands match index/name in 115 actual native records; exact function/compiler pointers and symbols are retained.','Loader sets the VM builtin table, loads ISEQ zero, clears that table and tail-calls rb_iseq_eval.'],formal=['generic-kernel/wp07-diagnostics-files-http.md:1-128'],limits=['Full native execution/leaf CFG and host effects are not implied by static wrapper reception.']),
 dict(id='ZLIB_DLL',sources=['zlib1.dll','ruby-imports.json'],facts=['All 90 independent zlib DLL literal candidates are raw-byte verified and fully read.','Ruby has an Init_zlib builtin-extension initialization call, but its parsed import descriptors contain no zlib1.dll import.'],formal=['demo-dx/wp75-project-conversion-and-authoring-tools.md:290-360','demo-dx/wp74-battle-animation-authoring-and-exchange.md:356-374','creature-rpg/wp64-mail-and-mystery-gift.md:81-100'],limits=['Do not equate Ruby Zlib API use with direct consumption of the separate zlib1.dll. Game/native caller reception remains the parent binary task responsibility.']),
]
write('consumers.json',dict(schema='gr8.ruby-zlib.consumers/v1',consumers=consumers,identities='consumer-source-identities.json',discovery_search='consumer-search.stdout',execution='NOT_EXECUTED'))
parent_import_path=ROOT.parent/'binary_remaining_texts'/'game-imports.json'
parent_import_bytes=parent_import_path.read_bytes()
parent_imports=json.loads(parent_import_bytes)
zlib_parent=next(d for d in parent_imports['descriptors'] if d['name']['text']=='zlib1.dll')
assert [d['name']['text'] for d in zlib_parent['imports']]==['deflate','deflateEnd','deflateInit2_','deflateReset']
write('parent-zlib-contribution.json',dict(owner='/root/binary_remaining_texts',artifact=str(parent_import_path),artifact_sha256=sha(parent_import_bytes),actually_read_here='Only the complete exact zlib1.dll descriptor and its four imported names, not the complete parent Game review.',descriptor=zlib_parent,credit='Parent independently parsed/full-read Game imports; static dependency only, no selected runtime path or Ruby-to-zlib1 relation.'))

facts={
 'gem_prelude_bin':('RZP01','Gem/ErrorHighlight/DidYouMean defined-constant gates conditionally require their libraries. LoadError handlers warn, with the rubygems path mismatch case reraised.',['VM_BUILTINS','HOST']),
 'prelude_bin':('RZP02','Binding#irb and Kernel#pp lazily require irb/pp; the pp wrapper forwards splat arguments and its visibility/alias instructions are retained.',['VM_BUILTINS']),
 'marshal_bin':('RZP03','Marshal.load(source, proc=nil, freeze:false) forwards three arguments to native marshal_load; restore is an alias. This exposes wrapper defaults and delegation, not the native object format.',['VM_BUILTINS','TOOLS','INTL','ANIMATION','GIFTS','SAVE','COPY_AND_REPLAY']),
 'nilclass_bin':('RZP04','NilClass#to_i returns 0 and #to_f returns 0.0.',['VM_BUILTINS']),
 'timev_bin':('RZP05','Time.now forwards in:nil to new; at has omitted-subsecond/default microsecond and in:nil gates. initialize uses the omitted-year sentinel, rejects a duplicate positional zone plus in keyword, then delegates current-time/argument branches.',['VM_BUILTINS']),
 'kernel_bin':('RZP06','class/frozen?, clone(freeze:nil), Float(exception:true) delegate native builtins. tap yields self then returns self; then/yield_self yield self when a block exists, otherwise take the native enumerator branch.',['VM_BUILTINS']),
 'array_bin':('RZP07','shuffle/shuffle! use keyword random default Random. sample distinguishes omitted count and count supplied and forwards the random provider; its mandatory-only variant delegates the no-argument builtin.',['VM_BUILTINS']),
 'warning_bin':('RZP08','Warning.warn forwards its collected message arguments and uplevel/category defaults nil to its native builtin.',['VM_BUILTINS']),
 'pack_bin':('RZP09','Array#pack has buffer:nil; String#unpack/unpack1 have offset:0; wrappers delegate the format and option to native pack/unpack builtins.',['VM_BUILTINS','ANIMATION','GIFTS']),
 'trace_point_bin':('RZP10','TracePoint constructor/event forwarding, attribute wrappers and enable(target:nil,target_line:nil,target_thread:nil) are preserved; native tracing outcomes are separate.',['VM_BUILTINS']),
 'ast_bin':('RZP11','AST parse/parse_file/of default keep_script_lines:false; Node accessors delegate. Node#source returns nil without retained lines, otherwise slices the recorded line span, adjusts boundary columns and joins.',['VM_BUILTINS']),
 'dir_bin':('RZP12','Dir.open returns the directory without a block; with a block it yields then ensures close, including exception paths. [] has base:nil/sort:true; glob keeps optional positional flags and keyword flags with an undef distinction.',['VM_BUILTINS','TOOLS']),
 'io_bin':('RZP13','IO#read_nonblock defaults buffer:nil and exception:true; write_nonblock defaults exception:true; both delegate exactly those arguments to native builtins.',['VM_BUILTINS','HOST']),
 'numeric_bin':('RZP14','Generic Numeric real?/integer?/finite?/infinite? have true/false/true/nil defaults. Integer integer? is true, ord/to_i/to_int return self; Float#to_f returns self; other arithmetic/class helpers are native builtin wrappers.',['VM_BUILTINS']),
 'ractor_bin':('RZP15','Ractor.new requires a block, conditionally warns, captures caller location and creates. select requires a ractor or supplied yield value. send/yield default move:false; receive, port, local storage and inspection wrappers/branches are preserved; make_shareable(copy:false) selects its native branch.',['VM_BUILTINS']),
 'gc_bin':('RZP16','GC.start/garbage_collect default full_mark/immediate_mark/immediate_sweep true and pass fourth argument false; status/stat/compaction wrappers preserve defaults. using_rvargc? compares SIZE_POOL_COUNT to 1; ObjectSpace garbage_collect is installed as a module function.',['VM_BUILTINS','PLUGINS']),
}
factlist=[]
for u in P:
 fid,description,consumer_ids=facts[u['name']]
 factlist.append(dict(id=fid,unit=u['name'],description=description,candidate_ids=u['candidate_ids'],source=dict(path='x64-msvcrt-ruby310.dll',start=u['start'],end_exclusive=u['end_exclusive'],sha256=u['sha256'],coff_symbol=u['coff_symbol']),consumers=consumer_ids,formal_targets=sorted({f for c in consumers if c['id'] in consumer_ids for f in c['formal']}),evidence=['yarb-decoded.json','new-program-inventory.json'],status='FULL_STATIC_WRAPPER_RECEPTION',native_leaf_status='NOT_FULLY_REVIEWED',execution='NOT_EXECUTED'))

forward=[]
dispositions=[]
counter=collections.Counter()
for c in C:
 cid=c['candidate_id'];pid=program_of.get(cid);cs=cstr_of.get(cid,[])
 kind='RECOVERED_YARB_PROGRAM' if pid else 'COMPLETE_MULTILINE_CSTRING' if cs else 'ZLIB_LITERAL' if c['path']=='zlib1.dll' else 'PE_HEADER_OR_OVERLAY_LITERAL' if c['section']=='headers_or_overlay_or_cross_section' else 'RUBY_DATA_LITERAL' if c['section']=='.data' else 'RUBY_RUNTIME_LITERAL'
 refs=['reading-ledger.json:text-view-all','identities.json:all_raw_candidates_verified']
 if pid:refs+=['yarb-decoded.json:'+pid,'new-program-inventory.json:'+pid]
 if cs:refs+=['complete-cstrings.json:'+str(n) for n in cs]
 consumer_ids=facts[pid][2] if pid else ['ZLIB_DLL'] if c['path']=='zlib1.dll' else ['HOST','VM_BUILTINS']
 fact_ids=[facts[pid][0]] if pid else ['LITERAL_EXISTENCE']
 d=dict(c)
 d.update(input_semantic_status=c['semantic_status'],input_type_disposition=c['type_disposition'],input_reason=c['reason'],input_semantic_reader=c['semantic_reader'],semantic_reader='/root/binary_ruby_zlib_remaining',semantic_status='FULL_STATIC_PROGRAM_AND_LITERAL_READ' if pid else 'FULL_LITERAL_READ',type_disposition=kind,reason='Full literal actually read in the complete continuous text-view; raw source identity verified. Additional program or whole-cstring context is linked when present. This grants no blanket native CFG or behavior approval.',text_sha256=sha(T[c['read_id']]['text'].encode()),reading_evidence=refs,program_unit=pid,complete_multiline_cstring_units=cs,semantic_fact_ids=fact_ids,consumer_ids=consumer_ids,native_behavior_status='NOT_EXECUTED',native_cfg_credit='NONE_EXCEPT_THREE_EXPLICIT_LOADER_FUNCTION_BODIES',global_approval='NOT_GRANTED')
 dispositions.append(d);counter[kind]+=1
 forward.append(dict(candidate_id=cid,read_id=c['read_id'],literal_view_line=c['view_line'],disposition=kind,program_unit=pid,cstring_units=cs,fact_ids=fact_ids,consumer_ids=consumer_ids))
with gzip.open(ROOT/'full-disposition-ledger.jsonl.gz','wt',encoding='utf-8') as f:
 for d in dispositions:f.write(json.dumps(d,ensure_ascii=False,separators=(',',':'))+'\n')
literal_units=[]
for line,u in enumerate(U,1):
 literal_units.append(dict(read_id=u['read_id'],view_line=line,text=u['text'],text_sha256=sha(u['text'].encode()),candidate_ids=[r['candidate_id'] for r in u['refs']],fact='LITERAL_EXISTENCE',read_status='FULL_LITERAL_READ',role_credit='The text itself is received: runtime names, diagnostics, format/configuration vocabulary, numeric-looking data and compiler syntax fragments. Symbol-neighborhood annotations are navigation only; no regex/nearest-symbol assignment grants native semantics.'))
reverse_formal=[]
for e in formal_evidence:
 short=e['path'][len(FORMAL):]
 reverse_formal.append(dict(formal_identity=e,consumer_ids=[c['id'] for c in consumers if any(f.startswith(short+':') for f in c['formal'])],program_fact_ids=[f['id'] for f in factlist if any(t.startswith(short+':') for t in f['formal_targets'])],mapping_scope='Only the read clauses and stated boundary, not whole-formal completeness.'))
write('bidirectional-mapping.json',dict(schema='gr8.ruby-zlib.bidirectional/v1',candidate_forward=forward,literal_reverse=literal_units,program_facts=factlist,formal_reverse=reverse_formal,literal_fact=dict(id='LITERAL_EXISTENCE',meaning='Exact candidate bytes decode to the fully read literal; existence does not prove a default call, diagnostic trigger, numeric table schema, or full native behavior.'),semantics_limits=['Compiler-looking single/multiline fragments were fully read as syntax/templates; they are not substituted for their native emitters or promoted to standalone complete functions.','No candidate is removed using approximate symbol names, regexes, pointer-like appearance or old 659C/six-MJIT reception.','The separate Game occurrences of equal texts are outside this child scope.']))

ranges=[[1,1000],[1001,1800],[1801,2600],[2601,3400],[3401,4200],[4201,5000],[5001,5800],[5801,6600],[6601,7600],[7601,8400],[8401,9200],[9201,10400],[10401,11600],[11601,12600],[12601,13574]]
write('reading-ledger.json',dict(schema='gr8.ruby-zlib.reading-ledger/v1',reader='/root/binary_ruby_zlib_remaining',utc_written=UTC,credit_model=dict(atomic='A fully read distinct text is propagated only to its exact verified original refs, without borrowing Game refs.',literal='All 13574 distinct texts were actually displayed/read continuously; not sampled or keyword-selected.',program='All decoded objects, fields, control-flow instructions, catches, keyword/optional tables and caller/builtin wiring were actually read for every one of 16 YARB containers.',native='The full objdump file was generated/indexed, not fully read. Only three explicitly saved loader function bodies and the 16 saved caller contexts were fully read.'),contracts=dict(directory=str(IN),full_read=['prompt.md','global-prompt.md','AGENTS.md','review-SKILL.md','parent-prompt.md','manifest.json'],global_prompt_read='Complete 36653-byte file; initial truncation was repaired with overlapping continuous character ranges through end. Manifest and input containers verified before source slices.'),text_view=dict(id='text-view-all',path=str(IN/'text-view.txt.gz'),decoded_sha256='62ba3ebbd919ec6a7c5c58fccbe62237c6089631d3f4b5373953e7a15d07ba5c',actual_contiguous_line_ranges=ranges,truncation_repair=[[12969,12980]],distinct_texts=13574,candidate_occurrences=20907,status='FULL_LITERAL_READ',search_or_script_classification_not_substitute=True),whole_multiline_cstrings=dict(path='complete-cstrings.json',count=536,bytes=sum(s['bytes'] for s in CS),candidate_occurrences=sum(len(s['candidate_ids']) for s in CS),actual_read_index_ranges=[[1,100],[101,536]],status='FULL_WHOLE_CSTRING_READ',credit='Diagnostics, AST displays, preprocessor/source-line hints and C/MJIT fragments all read to their real NUL boundary; not 536 standalone programs.'),new_programs=dict(path='yarb-decoded.json',units=[dict(name=u['name'],start=u['start'],end_exclusive=u['end_exclusive'],sha256=u['sha256'],iseq_indexes=[0,len(y['iseqs'])-1],object_indexes=[0,len(y['objects'])-1],instruction_count=sum(len(q['code']) for q in y['iseqs']),status='FULL_STATIC_READ') for u,y in zip(P,Y)],truncation_repair='timev_bin was fully reread after the first combined view truncated part of its objects/ISEQs.',builtin_entries=115,builtin_references=120,all_builtin_wiring_rows_read=True,raw_field_note='fields.location_first_lineno is the serialized VALUE (FIXNUM), not an already decoded source line; raw node ids/flags are preserved, not interpreted as behavior. Code location and instruction_info expose actual line values.'),source_evidence=source_evidence,formal_evidence=formal_evidence,decoder_reference=dict(directory='decoder-reference',compile_c_read_ranges=[[10610,10695],[10920,11038],[11105,11594],[11730,11920],[12100,12162],[12186,12266],[12380,12412],[12445,12587],[12730,12865]],typemap_rb='FULL_READ',builtin_h='FULL_READ',vm_core_h='Keyword structure definition excerpt read; not the entire header.',insns_def='Downloaded inventory only; not used as opcode authority and not claimed fully read.',target_opcode_authority='202 raw PE name/type/length table entries; decoder checks each length against operand count.'),execution=dict(target='NOT_EXECUTED',tools='Independent inert parsers, git read-only identity commands and objdump static output only. Receipts include original stdout/stderr, UTC and exits; failures are preserved.'),not_claimed=['Full native Ruby/zlib leaf CFG reception','Execution of Ruby/C/native programs','Game text occurrence reception','Global formal completeness or no-required approval']))

native_leaves=[]
for u in P:
 for e in u['builtin_wiring']['entries']:
  native_leaves.append(dict(unit=u['name'],builtin=e['name'],index=e['index'],func_pointer=e['func_pointer'],func_raw=e['func_raw'],func_symbols=e['func_symbols'],compiler_pointer=e['compiler_pointer'],compiler_raw=e['compiler_raw'],compiler_symbols=e['compiler_symbols'],status='NOT_FULLY_REVIEWED_NATIVE_CFG',reason='Exact native targets retained; serialized wrappers, literal compiler fragments and loader contexts do not constitute full native callee CFG semantics.'))
remaining=dict(schema='gr8.ruby-zlib.remaining/v1',scope_candidate_count=20907,scope_set_sha256=setsha,scope_distinct_texts=13574,unread_candidate_count=0,unread_candidate_ids=[],unread_distinct_text_count=0,unread_read_ids=[],readable_new_yarb_unread_units=[],readable_whole_cstring_unread_units=[],disposition_counts=dict(counter),scope_received='LOCAL_RECEPTION_COMPLETE_PENDING_PARENT_AND_INDEPENDENT_RECEPTION',not_a_global_closure=True,full_parent_denominator=57948,parent_owned_game_scope='Not changed or discharged by this child.',unresolved=[dict(id='NATIVE_LEAF_CFG',kind='BOUND_NATIVE_MATERIAL_UNKNOWN',exact_targets=native_leaves,not_candidate_unread=True),dict(id='NATIVE_ZLIB',kind='BOUND_NATIVE_MATERIAL_UNKNOWN',path='zlib1.dll',sha256='4b08bebfac59f1c453668d1742df29fdbe1be195d3d73ab7a8851b9a52d2acfe',range='Native .text and callers beyond the literal candidates; no dynamic linker/ABI/codec execution.',not_candidate_unread=True),dict(id='PARENT_ZLIB_CONSUMER',kind='DEPENDENCY',owner='/root/binary_remaining_texts',detail='Game/native import wiring of independent zlib1.dll must be received in the parent. Ruby Zlib APIs do not prove a direct dependency because the parsed Ruby imports have no zlib1.dll.'),dict(id='INDEPENDENT_PROGRAM_RECEPTION',kind='INDEPENDENT_REVIEW_PENDING',owner='/root',detail='New 16-container program discovery submitted for separate-context reception/counterevidence. This proposer does not independently approve its own discovery.'),dict(id='HOST_EXECUTION',kind='NOT_EXECUTED',detail='All runtime/OS/GUI/disk/codec outcomes remain unexecuted; no dynamic success is inferred.')],update_status='UPDATE_NOT_STARTED',business_execution='NOT_EXECUTED')
write('remaining.json',remaining)
remaining['unresolved']=[x for x in remaining['unresolved'] if x['id']!='PARENT_ZLIB_CONSUMER']
remaining['parent_contributions']=[dict(id='PARENT_ZLIB_CONSUMER',status='RECEIVED_PARENT_STATIC_IMPORT_EVIDENCE',evidence='parent-zlib-contribution.json',scope='Only Game PE imports four zlib1 names; parent retains Game occurrence/disposition responsibility.')]
write('remaining.json',remaining)

proposal=dict(id='GR8-RZ-YARB-001',kind='NEW_RECOVERABLE_PROGRAM_DISCOVERY',status='SUBMITTED_FOR_SEPARATE_CONTEXT_RECEPTION',normative_required_claim='NOT_PROPOSED',sections={
 '1_scope_and_identity':dict(source='x64-msvcrt-ruby310.dll',commit=RCOMMIT,containers='new-program-inventory.json',exact_candidate_memberships=542,raw_container_bytes=34524,b8_commit=BCOMMIT,formal_tree='f292698cdd4a8e725525a9be6dc34b75faaf151e'),
 '2_observation_and_claim':'Sixteen actual Ruby 3.1 builtin YARB containers are recoverable inert program material. Their full decoded bodies and caller/native wiring are new evidence, distinct from prior C-string program approvals. This is a reception correction, not an allegation that all runtime methods require new normative clauses.',
 '3_complete_source_and_consumer_chain':dict(decoded='yarb-decoded.json',objects=654,iseqs=171,instructions=1002,registry='new-program-inventory.json',builtin_entries=115,bytecode_refs=120,consumers='consumers.json'),
 '4_ordinary_case_and_minimal_counterexample':dict(ordinary='Marshal.load wrapper supplies proc=nil and freeze:false, calls builtin marshal_load with three arguments; restore is an alias. pack/unpack and GC.start wrappers similarly retain explicit options.',minimal_counterexample_to_blanket_opaque='nilclass_bin has executable ISEQs returning integer 0 and floating 0.0. Treating every YARB byte as opaque would hide this finite readable behavior.',counterexample_to_overclaim='The wrapper reaching marshal_load does not prove actual deserialization succeeds, and an installed Ractor method is not evidence the default game calls it.'),
 '5_failure_cancel_partial_commit':dict(examples=['Dir.open with a block has an ensure-close path, including exceptions.','Time.initialize rejects duplicate zone arguments before native initialization.','gem_prelude catches LoadError with the recorded warning/reraise paths.','R plugin metadata and earlier scripts can remain before a later failure; no overall rollback is inferred.'],runtime='All examples are static readings, NOT_EXECUTED.'),
 '6_formal_mapping_and_correctly_preserved':dict(mapping='bidirectional-mapping.json',preserved=['WP75 script conversion compression/serialization and nontransactional boundaries.','WP74 animation single-item exchange decode/type/local protection.','WP64 serialise/compress/base64 and nonempty decode propagation.','WP09 direct save/conversion/language write paths.'],formal_gap_claim='No required new normative defect alleged in this child; native/host boundaries and default callers must constrain any later proposal.'),
 '7_minimal_change_and_regression':dict(formal_changes='UPDATE_NOT_STARTED',requested_action='Root assigns another actual context to verify the complete new program and decoder evidence, then decides reception and any concrete gap.',static_regression='Exact raw SHA, 16 registry pointers/sizes, all 202 opcode table entries, 171 ISEQ decode closure, 115 builtin records and 120 matching builtin references.',execution='NOT_EXECUTED'),
 '8_history_relationship':'No reception credit borrowed from old 659 C strings, six new MJIT programs or the four root-rebutted GR8-BIN claims. Our remaining20907 set has no candidate identity overlap with those earlier complete program ranges; Game equal-text occurrences remain parent-owned.'})
write('proposals.json',dict(schema='gr8.ruby-zlib.proposals/v1',required_findings=[],new_program_discoveries=[proposal],independent_reception_owner='/root',global_verdict='NOT_ISSUED'))

runtime=dict(requested=dict(model='gpt-6.1-sol',reasoning_effort='ultra',service_tier='default/normal',fast_mode='off'),actual=dict(model='UNVERIFIED',reasoning_effort='UNVERIFIED',service_tier='UNVERIFIED',fast_mode='UNVERIFIED'),basis='No authoritative actual runtime echo was available in this child context; requested values are not treated as actual settings.')
write('runtime-settings.json',runtime)
write('progress.json',dict(schema='gr8.ruby-zlib.progress/v1',utc=UTC,state='DELIVERED_LOCAL_RECEPTION_PENDING_PARENT_ACCEPTANCE',scope_candidates=20907,scope_distinct_texts=13574,raw_candidates_verified=20907,actually_read_distinct_texts=13574,actually_read_candidate_occurrences=20907,unread_candidates=0,unread_distinct_texts=0,whole_multiline_cstrings=536,new_yarb_containers=16,new_yarb_objects=654,new_yarb_iseqs=171,new_yarb_instructions=1002,builtin_records=115,builtin_refs=120,independent_discovery_reception='PENDING_ROOT',parent_denominator_discharged=False,target_execution='NOT_EXECUTED',update_status='UPDATE_NOT_STARTED',runtime=runtime))

reference_files=[]
for p in sorted((ROOT/'decoder-reference').iterdir()):
 if p.is_file() and p.name not in ('reference-identities.json',):reference_files.append(dict(path=p.name,bytes=p.stat().st_size,sha256=sha(p.read_bytes())))
write('decoder-reference/reference-identities.json',dict(fixed_reference_commit='c2ac5ccbc2571c4e5c2981588d5991530540e545',files=reference_files,usage='Official fixed Ruby source is a decoder format reference only; the target binary supplies every recovered byte and opcode table. Downloaded files are not installed or executed.'))
print(json.dumps(dict(candidate_count=len(dispositions),distinct_texts=len(literal_units),candidate_set_sha256=setsha,dispositions=dict(counter),program_units=len(factlist),source_identities=len(source_evidence),formal_identities=len(formal_evidence),unread_candidates=0,target_execution=0)))
