#!/usr/bin/env python3
"""R-B08 post-first-judgment Git/JSON/text comparison; no historical programs."""
import json,pathlib,hashlib,subprocess,re,posixpath,collections
ROOT=pathlib.Path('/workspace/r-b08-actual-review');TMP=pathlib.Path('/tmp/r-b08-actual-inputs')
ACT='49c21538e72b7a5873972cd00fcae1ee390cce64';BASE='759eee80ce7856570fde2de12d5dcf98ce7e6017';CAND='0f35a393d9de467cd5f7e695b6072687bb582186';R08='239a29c466d6efc1a5a240f57ad53b55c91f9e42';BP='review/remediation/20261003-prepare/batches/B08/';IP=BP+'integration-stage-1/'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def raw(c,p):return git('show',c+':'+p)
def obj(c,p):return json.loads(raw(c,p))
def sha(b):return hashlib.sha256(b).hexdigest()
checks=[]
def check(v,label):checks.append({'check':label,'pass':bool(v)})
a=obj(ACT,IP+'input-inspection.json');b=obj(ACT,IP+'validation-results.json');m=obj(ACT,IP+'integration-manifest.json');df=obj(ACT,IP+'diff-and-freeze.json');sc=obj(ACT,IP+'scope-counts.json');obs=obj(ACT,IP+'scope-and-observation-registration.json')
for name,v,key,count in [('preintegration',a,'checks','check_count'),('payload',b,'current_checks','current_check_count')]:
 check(len(v[key])==v[count],name+' declared check count');check(all(r['pass_'] is True for r in v[key]),name+' all claimed pass (self-report consistency only)')
check(a['check_count']==1837 and b['preintegration_checks']==1837 and b['current_check_count']==1665,'exact self-report denominators')
check(a['source_identities']==m['source_identities'],'complete108 source copies exact')
for d in a['source_identities']:
 z=raw(d['commit'],d['path']);check(sha(z)==d['sha256'] and len(z)==d['bytes'] and git('rev-parse',d['commit']+':'+d['path']).decode().strip()==d['git_blob'],'self-inspection addressed source:'+d['path'])
check(a['formal_read_receipt']['formal12']==[d['candidate']['path'] for d in m['formal_candidate_identities']],'read-receipt full12 exact membership')
for d in a['formal_read_receipt']['original_diff_reads']:
 z=git('diff','--no-ext-diff','--no-textconv','--no-color','--binary','--full-index','--unified=0',BASE,CAND,'--',d['path']);check(len(z)==d['bytes'] and sha(z)==d['sha256'],'original receipt exact full-index zero-context Git diff:'+d['path'])
 changed=[l for l in z.decode().splitlines() if l.startswith(('+','-')) and not l.startswith(('+++','---'))];check(len(changed)==d['changed_line_occurrences'] and set(d['unique_changed_lines_read']).issubset(changed),'original receipt changed-line membership:'+d['path'])
 check(len(d['unique_changed_lines_read'])+d['exact_reuse']==len(changed),'original receipt occurrence/reuse arithmetic:'+d['path'])
check(a['original_sync_request_preserved']==obs['original_sync_request_preserved'] and a['parent_scope_record_preserved']==obs['parent_authorization_record_preserved'] and a['original_application_preserved']==obs['original_application_preserved'],'all three original-scope complete evidence copies')
check(a['catalog_counts']==df['catalogs'] and a['allocated_static_designs']==sc['new_static_ids'],'catalog full count and15 designs copies')
check(a['changed_old_rows']==['DC-08','EG-13','EN-01','EN-15','EN-16'] and a['protected_sections']==14,'five old semantic rows and14 protected sections')
for d in a['old_row_EOF_boundary']:
 old=next(l for l in raw(BASE,d['path']).splitlines(keepends=True) if l.startswith(b'| '+d['id'].encode()+b' |'));new=next(l for l in raw(ACT,d['path']).splitlines(keepends=True) if l.startswith(b'| '+d['id'].encode()+b' |'));check(sha(old)==d['old_sha256'] and sha(new)==d['new_sha256'] and old.rstrip(b'\n')==new.rstrip(b'\n'),'BR25 EOF only exact bytes')
z=git('diff','--no-ext-diff','--no-textconv','--no-color','--binary','--full-index','--unified=3',BASE,CAND);check(len(z)==a['complete_candidate_diff']['bytes'] and sha(z)==a['complete_candidate_diff']['sha256'],'complete candidate diff independent full-index three-context digest')
check(len(git('diff','--no-renames','--name-only',BASE,CAND).decode().splitlines())==a['complete_candidate_diff']['path_count']==57 and a['complete_candidate_diff']['unfiltered'] is True,'candidate exact57 unfiltered paths')
check(sum(r['check'].startswith('recorded Git identity ') for r in a['checks'])==a['reported_identity_checks_recomputed']==678,'678 reported identity labels (count only; independent source identities separately verified)')
for key in ['reference_execution','author_reviewer_program_execution','behavior_vectors_executed','runtime_observations','proven_Demo_chains']:check(b[key]==0,'bounded payload observation:'+key)
check(a['reference_execution']==0 and a['author_reviewer_program_execution']==0 and a['semantic_adjudication_by_A_REG'] is False and b['semantic_adjudication_by_A_REG'] is False,'no integrator behavioral adjudication claims')
check(b['original_prepare_authorize_apply_proof']=='AUTHOR_SELF_REPORT_ONLY' and 'AUTHOR_SELF_REPORT_ONLY' in a['original_order_limit'],'historical chronology explicitly self-report')
check(b['result']=='BOUNDED_GIT_TEXT_IDENTITY_PUBLIC_REGISTRATION_PASS_THREE_ACTUAL_ULTRA_PENDING','self-result is bounded and actual gates pending')
# Independently resolve all newly introduced Markdown links in ten public paths and integration README.
allpaths=set(git('ls-tree','-r','--name-only',ACT).decode().splitlines())
public=[d['path'] for d in m['current_public_paths']];linkcount=0
for p in public+[IP+'README.md']:
 if not p.endswith('.md'):continue
 txt=raw(ACT,p).decode();old=raw(BASE,p).decode() if p in public else ''
 def links(s):return collections.Counter(re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)',s))
 for target,count in (links(txt)-links(old)).items():
  if ':' in target or target.startswith('#'):continue
  q=posixpath.normpath(posixpath.join(posixpath.dirname(p),target.split('#')[0]));check(q in allpaths,'new relative link resolves:'+p+' -> '+target);linkcount+=count
out={'reviewed_actual':ACT,'first_judgment_recorded_before_comparison':True,'checks':len(checks),'failed':[r for r in checks if not r['pass']],'check_records':checks,'new_relative_link_occurrences':linkcount,'integrator_reported_checks':{'preintegration':1837,'payload':1665},'interpretation':'New independent text/identity comparisons; all-pass labels and chronology/environment claims remain self-reports, not rerun historical evidence. Validation results describe the payload phase; exact final actual difference is independently reconstructed separately.'}
(TMP/'integrator-comparison-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='check_records'},ensure_ascii=False,indent=2))
