"""Audit-only literal provenance/placeholder inventory. Does not run Ruby,
reference functions, host loaders, expressions, formatters or behavior vectors.
No source fragments retained: hashes, source positions and placeholder kinds.
"""
import re,hashlib
from collections import defaultdict,Counter
import review_state as s

def h(x):return hashlib.sha256(x.encode()).hexdigest()
def norm(x):
 x=re.sub(r'^[ \t\r\n\f\v]+','',x,flags=re.M)
 x=re.sub(r'[ \t\r\n\f\v]+$','',x,flags=re.M)
 return re.sub(r'[ \t\r\n\f\v]{2,}',' ',x)
def decode_format_text(x):
 for a,b in [('<<1>>','\x01'),('<<r>>','\r'),('<<n>>','\n'),('<<[>>','['),('<<]>>',']'),('<<t>>','\t')]:x=x.replace(a,b)
 return x

def consume_quoted(text,start):
 # Independent inert double-quoted literal lexer; every backslash pair is
 # preserved until decoding. Interpolation is never evaluated.
 i=start+1;raw=[]
 while i<len(text):
  if text[i]=='"':return ''.join(raw),i+1
  if text[i]=='\\' and i+1<len(text):raw.append(text[i:i+2]);i+=2
  else:raw.append(text[i]);i+=1
 return None,start+1

def scan_decode(raw):
 # Data collection recognizes five substitutions in that order; no eval.
 for a,b in [('\\r','\r'),('\\n','\n'),('\\1','\x01'),('\\"','"'),('\\\\','\\')]:raw=raw.replace(a,b)
 return raw
idx=defaultdict(list);unclosed=[];all_literals=[];escape_pairs=Counter()
for p in sorted((s.REF/'Data/Scripts').rglob('*.rb')):
 text=p.read_text(encoding='utf-8-sig');lines=text.splitlines();disabled=set();inblock=False
 for n,l in enumerate(lines,1):
  if l.startswith('=begin'):inblock=True
  if inblock:disabled.add(n)
  if l.startswith('=end'):inblock=False
 for m in re.finditer(r'\b(_INTL|_ISPRINTF)\s*\(\s*(")',text):
  raw,end=consume_quoted(text,m.end()-1);n=text.count('\n',0,m.start())+1
  if raw is None:unclosed.append({'path':str(p.relative_to(s.REF)),'line':n});continue
  decoded=scan_decode(raw);key=norm(decoded);escape_pairs.update(re.findall(r'\\.',raw));prefix=lines[n-1].split(m[1],1)[0]
  row={'path':str(p.relative_to(s.REF)),'version':s.R,'line':n,'end_line':text.count('\n',0,end)+1,'entry':m[1],'lexical_context':'disabled_block' if n in disabled else 'comment_only' if prefix.lstrip().startswith('#') else 'code_candidate','raw_literal_sha256':h(raw),'collected_key_sha256':h(key),'contains_interpolation_syntax':'#{' in raw,'placeholder_indices':[int(v) for v in re.findall(r'\{(\d+)\}',decoded)],'format_placeholders':[{'index':int(a),'format':b} for a,b in re.findall(r'\{(\d+):([^}]+)\}',decoded)]}
  idx[h(key)].append(row);all_literals.append(row)
text=s.read('text-records-SCRIPT_TEXTS.json');lines=(s.REF/'Text_english_core/SCRIPT_TEXTS.txt').read_text(encoding='utf-8-sig').splitlines();unlinked=[];placeholder_patterns=Counter();format_patterns=Counter();no_active=[]
for r in text['records']:
 key=decode_format_text(lines[r['lines'][0]-1]);val=decode_format_text(lines[r['lines'][1]-1]);sources=idx.get(h(norm(key)),[])
 r['literal_source_candidates']=sources
 r['placeholder_indices']=[int(v) for v in re.findall(r'\{(\d+)\}',val)]
 r['formatted_placeholders']=[{'index':int(a),'format':b} for a,b in re.findall(r'\{(\d+):([^}]+)\}',val)]
 r['control_token_names']=sorted(set(re.findall(r'\\([A-Za-z]+)',val)))
 r['decoded_control_characters']={str(ord(c)):val.count(c) for c in ['\r','\n','\t','\x01'] if c in val}
 r['bracket_or_escape_collision_markers']={'literal_decoded_marker':'<<' in key or '<<' in val,'unmatched_braces':val.count('{')!=val.count('}')}
 r['semantic_status']='literal_provenance_and_placeholder_shape_checked_consumer_contract_pending'
 if not sources:unlinked.append({'record':r['record'],'lines':r['lines'],'key_sha256':r['key_sha256'],'placeholder_indices':r['placeholder_indices'],'formatted_placeholders':r['formatted_placeholders'],'key_preview':key[:160]})
 elif not any(x['lexical_context']=='code_candidate' for x in sources):no_active.append({'record':r['record'],'sources':sources})
 placeholder_patterns.update(str(i) for i in r['placeholder_indices']);format_patterns.update(x['format'] for x in r['formatted_placeholders'])
s.write('text-records-SCRIPT_TEXTS.json',text)
s.write('script-text-audit.json',{'schema_version':'gr5.review.v1','source_baseline':s.R,'boundary':'All3305corpus records inspected for literal source provenance, interpolation token shape and controls; no call reachability/argument-value or runtime proof. Lexical compiler collection may include comments/disabled bodies. Unlinked keys remain callable translation data.','literal_occurrences':len(all_literals),'literal_unique_normalized_keys':len(idx),'unclosed_candidates':unclosed,'unmatched_corpus':unlinked,'only_noncode_matches':no_active,'simple_placeholder_occurrences':dict(placeholder_patterns),'format_placeholder_occurrences':dict(format_patterns),'source_escape_pairs':dict(escape_pairs)})
print('literal occurrences',len(all_literals),'unique',len(idx),'corpus',len(text['records']),'unlinked',len(unlinked),'noncode',len(no_active),'unclosed',len(unclosed))
print('placeholders',dict(placeholder_patterns),'formats',dict(format_patterns),'escapes',dict(escape_pairs))
for r in unlinked:print(r)
