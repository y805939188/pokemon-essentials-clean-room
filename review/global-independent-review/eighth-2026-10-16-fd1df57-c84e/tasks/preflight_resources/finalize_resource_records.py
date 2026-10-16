"""Record finite static reading and exact input identities; never execute R programs."""
from pathlib import Path
import datetime, hashlib, json, subprocess

O = Path(__file__).resolve().parent
R = Path('/workspace/pokemon-essentials')
B = Path('/workspace/pokemon-essentials-clean-room')
RC = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BC = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
def get(repo, obj):
    return subprocess.run(['git', '-C', str(repo), 'show', obj], check=True, capture_output=True).stdout
def save(name, value):
    (O/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

ids = json.loads((O/'source-identities.json').read_text())
new = [
 ('Data/Scripts/001_Technical/002_Files/001_FileTests.rb', 'all file/path/StringInput branches; no native encrypted load or real storage observation'),
 ('Data/Scripts/008_Audio/001_Audio.rb', 'all page/duration/path branches; no media parser or playback execution')
]
ledger = json.loads((O/'reading-ledger.json').read_text())
for path, remark in new:
    data = get(R, RC+':'+path)
    assert data == (R/path).read_bytes(), path
    blob = subprocess.run(['git','-C',str(R),'rev-parse',RC+':'+path],check=True,capture_output=True,text=True).stdout.strip()
    mode = subprocess.run(['git','-C',str(R),'ls-tree',RC,'--',path],check=True,capture_output=True,text=True).stdout.split()[0]
    ids[path] = dict(repo='R',commit=RC,tree='7589c800b61ba13a13040ed0d686979b80a84fd0',path=path,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=blob,mode=mode)
    if not any(x.get('path')==path for x in ledger['rows']):
        ledger['rows'].append(dict(owner='/root/preflight_resources',repo='R',path=path,identity_ref='source-identities.json#'+path,evidence_level='SOURCE_STATIC',ranges={'lines':[1,len(data.splitlines())]},structural_units='all definitions, branches and literals',reading_status='FULL_READ',accepted=False,remarks=remark))
save('source-identities.json',ids)
ledger['updated_utc']=now
ledger['rows'].append(dict(owner='/root/preflight_resources',repo='B8',path='deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md',ranges='§12.1–§12.4 complete',reading_status='FULL_READ_NAMED_SECTIONS',evidence_level='CURRENT_SPEC',accepted=False,remarks='Both root script tools and Main loader fully read; local static match only, independent reception pending'))
ledger['rows'].append(dict(owner='/root/preflight_resources',repo='B8',path='deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md',ranges={'lines':[392,433]},reading_status='FULL_READ_NAMED_SECTIONS',evidence_level='CURRENT_SPEC',accepted=False,remarks='R7-U11 EXT and TOOL-AN complete premises and all vectors re-read; not executed'))
save('reading-ledger.json',ledger)

decoder=json.JSONDecoder()
def json_stream(name):
    s=(O/name).read_text(); result=[]
    while s.strip():
        s=s.lstrip(); value,end=decoder.raw_decode(s);result.append(value);s=s[end:]
    return result
pes=json_stream('evidence/current-small-pe.stdout')+json_stream('evidence/current-other-pe.stdout')
inventory=json.loads((O/'current-programs-v2/inventory.json').read_text())
den=[]
for item in pes:
    p=item['pe']; path=Path(p['path']).name; data=get(R,RC+':'+path)
    assert len(data)==p['bytes'] and data==(R/path).read_bytes()
    cursor=0
    for reg in p['continuous_partition']:
        assert reg['start']==cursor and hashlib.sha256(data[reg['start']:reg['end_exclusive']]).hexdigest()==reg['sha256']
        cursor=reg['end_exclusive']
    assert cursor==len(data)
    overlays=[x for x in inventory if Path(x['path']).name==path]
    den.append(dict(path=path,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),source_commit=RC,headers_fields=p['fields'],sections=p['sections'],continuous_partition=p['continuous_partition'],named_import_libraries=[{'dll':x['dll'],'entries':len(x['entries'])}for x in p['imports']],import_count=sum(len(x['entries'])for x in p['imports']),clr_metadata_present=item['clr'] is not None,known_extracted_units=[{'id':x['id'],'kind':x['kind'],'start':x['start'],'end_exclusive':x['end_exclusive'],'sha256':x.get('sha256')}for x in overlays],qualification='Complete byte partition and extracted-unit inventory are STRUCTURE_PARSED. Only explicit reading-ledger units earn finite semantic FULL_READ. Neither native CFG nor library behavior is inferred.'))
save('native-region-denominator.json',dict(schema='r8.resources.native-denominator.v1',created_utc=now,source_commit=RC,files=den,scope_note='This is a byte/section denominator, not semantic coverage percentage or proof that every recoverable literal has been found. Candidate navigation used recovered locators checked against current bytes; negative discovery closure remains open.'))

findings=dict(schema='r8.resource.findings.v1',created_utc=now,proposer='/root/preflight_resources',status='PARTIAL_REVIEW_PENDING_INDEPENDENT_RECEPTION',required_update_proposals=[],required_update_acceptance='UNDETERMINED_FOR_FULL_RESOURCE_DOMAIN',update_started=False,behavior_executions=0,examined_nonfindings=[
 dict(id='RES-OBS-AN',source='animmaker all15methods/743instructions/1670bytes/11EH',formal='WP74 §18.1–§18.3; TOOL-AN01–17',result='No mismatch identified in fully read finite static request bodies and named clauses.',premise='Reader/image/XML/filesystem effects remain conditional; no .NET execution',independent_counterreview='PENDING'),
 dict(id='RES-OBS-EXT',source='extendtext complete1740byte .text including correctly aligned callback,17imports and dialog literals',formal='WP75 §14; R7-U11-EXT01–12',result='No mismatch identified in finite marker/mutex/query/geometry/wait/exit requests.',premise='No Win32 execution, observed geometry, ownership or precise period',independent_counterreview='PENDING'),
 dict(id='RES-OBS-LOAD',source='Scripts.rxdata inert archive and Main49lines; scripts_extract/combine both183lines',formal='WP75 §12.1–§12.4',result='No mismatch identified in named discovery/order/guards/normalization and failure-prefix clauses.',premise='No Marshal user classes, Ruby evaluation, target storage or native boot executed',independent_counterreview='PENDING'),
 dict(id='RES-OBS-COMP',source='Game XP/VX/Ace all3448lines and named current Sprite/Cache/Weather/Audio consumers',formal='GR6-POL-001; WP15/WP16 named consumer clauses',result='Legacy profiles remain distinct unselected policy; active current source reopenings cannot be replaced with old profile defaults.',premise='Native profile selector, dynamic object fields and arbitrary plugin replacement unknown; downstream closure incomplete',independent_counterreview='PENDING'),
 dict(id='RES-OBS-SH',source='66Game shader candidates:55main/5prelude/6false;650Ruby C candidates:646fragments/4false',formal='WP16 high-level rendering; L04/L05',result='Literal formulas and premises recorded; no proved active binding supports promoting these conditional details into new mandatory host requirements.',premise='Native construction, substitutions, uniforms, textures, GPU compilation and pixels unknown',independent_counterreview='PENDING'),
 dict(id='RES-OBS-TOWN',source='townmapgen414lines plus all128BMPpixels',formal='WP75 §13; CV-M30',result='Known/selected marker byte values and DOM placement preserve source request boundary.',premise='No browser, region PNG or visual output observed',independent_counterreview='PENDING'),
 dict(id='RES-OBS-DURATION',source='Audio001 full154lines and FileTests full484lines',formal='WP15 §6.4.1',result='Named literal-first WAV/MP3/Ogg path/failure boundaries remain appropriately limited.',premise='No real file parsing or audible output; corrupt-input exceptions are not unified',independent_counterreview='PENDING')
],unread_readable=[
 'Game controller table1666 records/790 complete-field patterns: parsed, record semantics unread',
 'all8font field/glyph semantics; allSF2 hydra/PCM semantic interpretation; messages10697key/body pairs: parsed, not semantic full read by this task; resource_media_serialized reception pending',
 'Game/Ruby/zlib other native machine control flow, resource/type/export metadata not fully semantic read',
 'all-formal-clause reverse check and all downstream consumers outside named source read set'
],opaque_or_host_limits=['L01/L02 absent full project/media','L03 compatible host','L04 native selector/full CFG and external behavior','L05 GPU selection/supplied state/pixels','L06 external .NET XML/image/filesystem effects','L07 Win32 returns/geometry/cycle','L08 target font availability/rendering/hinting','L09 SF2 loader/guards/synthesis','L10 native loader/language quality','L11 unbounded plugins','L12 services/save/replay','L13 legal conclusions/history PASS','L14 missing historical execution metadata'],qualification='No required proposal found in this finite subset is not a whole-domain NO_REQUIRED_UPDATE conclusion. All finite nonfindings await independent non-proposer acceptance.')
save('findings.json',findings)

progress=json.loads((O/'progress.json').read_text());progress['updated_utc']=now
progress['outputs']=['preflight-report.md','reading-ledger.json','source-identities.json','resource-recovery-receipt.json','native-region-denominator.json','forward-map.json','reverse-map.json','findings.json']
progress['remaining']=['controller1666 semantic records','native other-body/literal-discovery residual disposition','cross-domain downstream source and formal reception','independent non-proposer reception','resource_media_serialized font/SF2/messages semantic reception']
save('progress.json',progress)
print(json.dumps({'source_identities':len(ids),'ledger_rows':len(ledger['rows']),'native_files':len(den),'native_bytes':sum(x['bytes']for x in den),'nonfindings':len(findings['examined_nonfindings']),'behavior_executions':0,'required_update_proposals':0,'status':findings['status']},ensure_ascii=False))
