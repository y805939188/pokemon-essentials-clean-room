"""Complete per-candidate disposition; semantic UNREAD is never inferred away."""
from pathlib import Path
import array, bisect, collections, datetime, gzip, hashlib, json, re
O=Path(__file__).resolve().parent
P=O.parent/'preflight_resources'
R=Path('/workspace/pokemon-essentials')
utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
sha=lambda b:hashlib.sha256(b).hexdigest()
def save(name,v):(O/name).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pool=json.loads((O/'semantic-text-readset.json').read_text())
engine={r['read_id'] for r in pool if any(q['path']=='Game.exe' and 10648064<=q['start']<10704000 for q in r['refs'])}
small={r['read_id'] for r in pool if any(q['path'] in ['zlib1.dll','animmaker.exe','extendtext.exe'] for q in r['refs']) and not any(q['section']=='.text' for q in r['refs'])}
programlike={l.split(' ',1)[0] for l in (O/'program-like-text-view.txt').read_text().splitlines()}
raw_attribution={r['read_id'] for r in pool if any(q['section']=='.text' for q in r['refs']) and re.search(r'CRYPTOGAMS|Camellia for x86_64|Mike Hamburg|expand 32-byte k',r['text'])}
readids=engine|small|programlike|raw_attribution
read_by_candidate={q['id']:r['read_id'] for r in pool if r['read_id'] in readids for q in r['refs']}
meta={f['path']:f for f in json.loads((O/'pe-metadata.json').read_text())['files']}
png=json.loads((O/'png-ranges.json').read_text())
bro=json.loads((O/'brotli-dictionary-proof.json').read_text())
counts=collections.Counter();byfile={};unread_unique=set();seen=set();known=collections.Counter();fullcounts=collections.Counter();unreadcount=0
with gzip.open(O/'full-disposition-ledger.jsonl.gz','wt') as output, gzip.open(O/'remaining-unread.jsonl.gz','wt') as unread:
 for name,m in meta.items():
  b=(R/name).read_bytes();instr_start=array.array('I');instr_end=array.array('I');instr_line=array.array('I')
  if name!='animmaker.exe':
   with gzip.open(O/(name+'.instructions.jsonl.gz'),'rt') as h:
    for line in h:
     ins=json.loads(line);instr_start.append(ins['start']);instr_end.append(ins['end_exclusive']);instr_line.append(ins['stdout_line'])
  xrefs=json.loads(gzip.decompress((O/(name+'.rip-targets.v2.json.gz')).read_bytes()))
  fc=collections.Counter()
  for line in (O/(name+'.section-candidates.jsonl')).open():
   r=json.loads(line);a,z=r['start'],r['end_exclusive'];s=r['text'];sec=r['section'];rid=r['candidate_id']
   row={k:r[k] for k in ['candidate_id','path','inventory_line','encoding','start','end_exclusive','bytes','sha256','section','previous_read_refs']}
   row['semantic_reader']='/root/binary_controller_strings_review'
   status='UNREAD';typ='UNDETERMINED_READABLE_OR_BINARY_CONTEXT';reason='Available finite candidate requires content/context reception; not an L04 exemption.'
   if name=='Game.exe' and bro['Game_start']<=a and z<=bro['Game_end_exclusive']:
    status='INVENTORY_ONLY';typ='COMPRESSION_DICTIONARY_TOKEN_BYTES';reason='Exact whole kBrotliDictionaryData symbol equality, 122784 bytes; see brotli-dictionary-proof.json. HTML/JS fragments are dictionary words, not an assembled executable program.'
   elif name=='Game.exe' and 13227296<=a and z<=13241056:
    status='INVENTORY_ONLY';typ='PACKED_UINT16_LOOKUP_TABLE_SUBRUN';reason='Exact base referenced at instruction8094406 and indexed 16-bit read8094415 followed by byte rotation/store. Run is 13758 bytes of paired values; next table base13241056 has separate references. No language program or GUI text inferred.'
   elif name=='Game.exe' and 9774912<=a and z<=10217559:
    status='FULL_READ_CONTROLLER_TABLE_TEXT';typ='CONTROLLER_RECORD_OR_COMMENT';reason='All1678lines/1666records/790patterns/122orders/806names received through lossless pattern and name views; original per-line identities retained in controller ledger. GUID identities inventory-only, not semantic behavior.'
   elif r['previous_read_refs']:
    status='STRUCTURE_PARSED_PRIOR_SEMANTIC_CONTRIBUTION';typ='BOUND_PREVIOUSLY_READ_UNIT';reason='Current source/raw extraction identity independently verified for787units; original semantic contributor is preflight_resources, not this reader; see previous-unit-identity-reception.json.'
    known.update(r['previous_read_refs'])
   elif rid in read_by_candidate:
    status='FULL_READ_TEXT_LITERAL_ONLY';typ='DIAGNOSTIC_INTERFACE_CONFIG_LABEL_OR_SHORT_PROGRAM';reason='Literal content fully read in named view; consumer and operational assertions require separate native/source evidence. Text equality permits content reuse, not receiver/reachability reuse.';row['read_id']=read_by_candidate[rid]
   elif sec.startswith('.debug') or sec=='COFF_symbol_or_string_table':
    status='INVENTORY_ONLY';typ='STRUCTURED_DEBUG_COFF_IDENTITY_OR_ENCODING';reason='Bounded PE/COFF parser identifies debug section or COFF symbol/string-table raw range. Symbol/source path/line encoding is administrative lookup data; no behavior or interface implementation claim.'
   elif sec in ['.edata','.idata']:
    status='INVENTORY_ONLY';typ='STRUCTURED_NATIVE_IMPORT_EXPORT_IDENTITY_OR_TABLE_ENCODING';reason='Bounded PE directories parsed fully as import/export symbols and address/hint/ordinal records. The name inventory does not supply native API behavior or active binding; relevant engine strings read separately.'
   elif sec in ['.pdata','.xdata','.reloc','.CRT','.tls']:
    status='INVENTORY_ONLY';typ='NATIVE_NUMERIC_TABLE_ENCODING';reason='Candidate lies in exact PE exception/unwind/relocation/initialization/TLS table raw range; printable byte subrun is retained as identity only.'
   elif name=='Game.exe' and any(p['start']<=a and z<=p['end_exclusive'] for p in png):
    status='INVENTORY_ONLY';typ='EMBEDDED_PNG_CHUNK_OR_COMPRESSED_PIXEL_ENCODING';reason='Exact PNG signature, bounded IHDR/IDAT/IEND chunks with all CRCs verified; see png-ranges.json. No PNG decoder/rendering outcome claimed.'
   elif sec=='.rsrc':
    for res in m['resources']:
     if res['offset']<=a and z<=res['offset']+res['size']:
      if res['path'][0] in [3,14]:
       status='INVENTORY_ONLY';typ='ICON_DIB_PIXEL_OR_ICON_DIRECTORY_ENCODING';reason='Exact resource leaf type3/type14, DIB dimensions32bpp/group fields parsed; no textual command or display result inferred.'
      elif res['path'][0] in [16,24]:
       status='FULL_READ_RESOURCE_METADATA';typ='VERSION_OR_XML_MANIFEST_FIELD';reason='All version-resource keys/values and full612byte Game manifest read; metadata includes version/product/language/DPI declarations, not a host success guarantee.'
      break
   elif name=='animmaker.exe' and sec=='.text':
    status='STRUCTURE_PARSED_PRIOR_SEMANTIC_CONTRIBUTION';typ='MANAGED_CIL_METADATA_OR_HEAP_ENCODING';reason='CLI metadata tables/heaps and15method bodies are completely parsed; original CIL semantic contribution is preflight_resources, no native x86 disassembly credit. String/heap occurrences are not separately claimed executed.'
   elif sec=='.text':
    i=bisect.bisect_right(instr_start,a)-1;j=bisect.bisect_left(instr_start,z)-1
    if i>=0 and j>=i and instr_start[i]<=a and instr_end[j]>=z and all(instr_end[k]==instr_start[k+1] for k in range(i,j)):
     status='INVENTORY_ONLY';typ='EXECUTABLE_INSTRUCTION_OR_IMMEDIATE_BYTE_SUBRUN';reason='Exact run covered by contiguous decoded .text instruction bytes; may include immediate fragments of assembled diagnostics. Regex candidate is not a standalone source string/program; no native CFG, message reconstruction or execution equivalence claimed.'
     row['instruction_evidence']={'first_offset':instr_start[i],'last_offset':instr_start[j],'stdout_first_line':instr_line[i],'stdout_last_line':instr_line[j],'stdout':name+'.objdump.stdout.gz'}
   row.update(semantic_status=status,type_disposition=typ,reason=reason)
   if str(a) in xrefs:row['address_references']=xrefs[str(a)]
   row['bounded_context_hex']={'before':b[max(0,a-8):a].hex(),'after':b[z:min(len(b),z+8)].hex()}
   assert rid not in seen;seen.add(rid);counts[status]+=1;fc[status]+=1
   output.write(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n')
   if status=='UNREAD':
    unread.write(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n');unreadcount+=1;unread_unique.add(s)
   if status.startswith('FULL_READ'):fullcounts[typ]+=1
  byfile[name]=dict(fc)
assert len(seen)==260161
save('disposition-summary.json',dict(schema='r8.binary-controller-string-disposition.v1',recorded_utc=utc(),finite_candidates=len(seen),status_counts=dict(counts),by_file=byfile,full_read_literal_counts=dict(fullcounts),unread_candidates=unreadcount,unread_distinct_texts=len(unread_unique),accepted_literal_content_ids=sorted(readids),previous_unit_ids_referenced=len(known),qualification='Complete candidate accounting, not complete semantic reading. All actual UNREAD remains in remaining-unread.jsonl.gz; no required/no-required conclusion for the full domain. Native machine CFG and arbitrary encodings remain separate limits.',behavior_vectors='NOT_EXECUTED',update_status='UPDATE_NOT_STARTED'))
print(json.dumps(dict(total=len(seen),counts=dict(counts),unread_unique=len(unread_unique),read_unique=len(readids),by_file=byfile)))
