"""Capture complete explicitly selected JSON objects, preserving original identity."""
import pathlib,json,sys,datetime,uuid,hashlib
P=pathlib.Path(__file__).resolve().parent;start=datetime.datetime.now(datetime.timezone.utc).isoformat();f=pathlib.Path(sys.argv[1]);b=f.read_bytes();d=json.loads(b);section=sys.argv[2]
if section=='facts':selected=d['facts'][int(sys.argv[3]):int(sys.argv[4])]
elif section=='rows':selected=d['rows'][int(sys.argv[3]):int(sys.argv[4])]
elif section=='common':selected=d['common']
elif section=='families':selected={k:d[k]for k in ['item_family_meanings','form_family_meanings']}
elif section=='row-new':
 selected=[]
 for x in d['rows'][int(sys.argv[3]):int(sys.argv[4])]:
  ref=x['original_full_object'];fn,ptr=ref.split('#');orig=json.loads((f.parent/fn).read_text())['rows'][int(ptr.rsplit('/',1)[1])]
  assert x['original_actual_reader_preserved']==orig['source_units']
  selected.append({**{k:v for k,v in x.items()if k!='original_actual_reader_preserved'},'original_full_object_sha256':hashlib.sha256(json.dumps(orig,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'preserved_source_units':'Exactly equal original_full_object.source_units; original complete object personally received in prior main authored review, reused without a new reader/sourceFULL transfer.'})
elif section=='envelope':selected={k:v for k,v in d.items()if k not in ['facts','item_family_meanings','form_family_meanings']}
else:raise ValueError(section)
stdout=json.dumps(selected,ensure_ascii=False,indent=2)+'\n';stem='selected-'+uuid.uuid4().hex;(P/'io'/(stem+'.stdout')).write_text(stdout);(P/'io'/(stem+'.stderr')).write_text('');(P/'io'/(stem+'.json')).write_text(json.dumps(dict(argv=sys.argv,input_path=str(f),input_bytes=len(b),input_sha256=hashlib.sha256(b).hexdigest(),actual_reader='/root/core_atomic_reception',utc_start=start,utc_end=datetime.datetime.now(datetime.timezone.utc).isoformat(),helper_exit=0,business='NOT_EXECUTED',stdout=stem+'.stdout',stderr=stem+'.stderr'),ensure_ascii=False,indent=2)+'\n');print(stdout);print('IO',stem)
