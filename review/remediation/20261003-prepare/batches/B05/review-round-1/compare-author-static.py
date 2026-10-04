import json,re,hashlib,pathlib,subprocess,datetime
P=pathlib.Path('/workspace/pokemon-essentials-clean-room');R=pathlib.Path('/workspace/b05-reference');D=P/'review/remediation/20261003-prepare/batches/B05/review-round-1';A=D.parent
B='0a12de641542f9a59909d2a950c1de8df17ca09d';C='1914cd379bcb7c8b6feb13dc3e872b7ded27d9a4';V='7dc7dd5dfc986788fd6d9ce7b2bdaa6208837b4e';O='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
def g(*args):return subprocess.check_output(['git','-C',str(P),*args])
def t(commit,path):return g('show',commit+':'+path).decode()
def sha(b):return hashlib.sha256(b).hexdigest()
def mask_section(s,n):
 pattern=r'(?ms)^'+ ('## ' if '.' not in n else '### ')+re.escape(n)+(r'\. ' if '.' not in n else r' ')+r'.*?(?=^#{1,3} |\Z)'
 out,count=re.subn(pattern,'<approved-section-'+n+'>\n',s);assert count==1,(n,count);return out
rules={'specs/creature-rpg/wp18-creature-identity-species-ownership.md':['3.2','4.2','9'],'specs/creature-rpg/wp20-hp-status-moves-helditem.md':['5.1','5.2','5.3','9'],'specs/pokemon-rules/wp19-attributes-ability-and-stats.md':['3.5'],'specs/pokemon-rules/wp21-dynamic-forms-and-display.md':['4.1','4.2'],'specs/pokemon-rules/wp23-shadow-hyper-and-purification.md':[]}
def mask(s,p):
 for n in rules[p]:s=mask_section(s,n)
 if 'wp20-' in p:
  a=s.index('## 7. ');b=s.index('## 8. ',a);part,n=re.subn(r'(?m)^5\. .*$', '<approved-invariant-7.5>',s[a:b]);assert n==1;s=s[:a]+part+s[b:]
 if 'wp21-' in p:s,n=re.subn(r'(?ms)^\*\*C\. .*?(?=^\*\*E\. )','<approved-c-and-d>\n',s);assert n==1
 if 'wp23-' in p:s,n=re.subn(r'(?m)^\| W06 \|.*$','<approved-W06>',s);assert n==1
 return s
v=json.loads((D/'independent-static-validation.json').read_text());old=json.loads((A/'author/candidate-manifest.json').read_text());new=json.loads((A/'author-v2/candidate-manifest.json').read_text());disp=json.loads((A/'author-v2/finding-dispositions.json').read_text());prop=json.loads((A/'author-v2/registrar-proposals.json').read_text()); orig={x['id']:x for x in json.loads(t(O,'review/global-independent-review/2026-10-03-fd82a639/findings.json'))}
res={'comparison_started_after_first_phase_freeze':True,'first_phase_freeze_sha256':sha((D/'first-phase-freeze.json').read_bytes()),'candidate_commit':C,'author_script_executed':False,'author_claimed_static_check_counts':{'v1':94,'v2':121},'author_claimed_evidence_check_counts':{'v1':217,'v2':195},'these_counts_are_not_independent_behavior_validation':True}
res['original_outside_approved_clauses_equal']={p:mask(t(B,p),p)==mask(t(C,p),p) for p in rules}
res['candidate_manifest_formal_set_matches']=set(new['formal_paths'])==set(v['formal_paths'])
res['candidate_manifest_formal_hashes_match']=all(new['formal_file_sha256'][x['path']]==x['sha256'] for x in v['candidate_formal_manifest'])
res['full_formal_diff_matches_author_v2']=g('diff',B,C,'--',*v['formal_paths'])==(A/'author-v2/formal-diff.patch').read_bytes()
res['v1_author_directory_unchanged']=not g('diff','--name-only',V,C,'--',str((A/'author').relative_to(P))).strip()
res['v1_ten_formal_deliverables_unchanged']=not g('diff','--name-only',V,C,'--','deliverables').strip()
res['shared_test_tails_byte_equal']={p:t(B,p)[t(B,p).index(marker):]==t(C,p)[t(C,p).index(marker):] for p,marker in [(v['formal_paths'][8],'## PT：'),(v['formal_paths'][9],'## BR：')]}
res['row_count_added']=sum(len(x['added']) for x in v['neighbor_test_rows'].values())
res['per_id']=[{'id':x['id'],'author_priority_matches_original':x['priority']==orig[x['id']]['priority'],'author_state_remains_OPEN':x['canonical_status'].startswith('OPEN'),'author_original_scope_gate_pending':x['original_scope_gate_pending'],'author_case_constraints_match_original':x['effective_case_constraints']==orig[x['id']].get('effective_case_constraints'),'author_tests':x['static_test_ids'],'author_remaining_responsibility':x['remaining_responsibility'],'review_comparison':'AGREES_WITH_INDEPENDENT_SCOPED_JUDGMENT','registrar_state_keeps_OPEN':next(y for y in prop['all_16_ids'] if y['id']==x['id'])['recommended_state'].startswith('OPEN;')} for x in disp]
res['all_16_ids_same']=set(x['id'] for x in disp)==set(x['id'] for x in v['original_objects'])==set(x['id'] for x in prop['all_16_ids'])
res['all_static_comparison_checks_pass']=all(res[k] for k in ['candidate_manifest_formal_set_matches','candidate_manifest_formal_hashes_match','full_formal_diff_matches_author_v2','v1_author_directory_unchanged','v1_ten_formal_deliverables_unchanged','all_16_ids_same']) and all(res['original_outside_approved_clauses_equal'].values()) and all(res['shared_test_tails_byte_equal'].values()) and res['row_count_added']==38 and all(x['author_priority_matches_original'] and x['author_state_remains_OPEN'] and x['author_case_constraints_match_original'] and not x['author_original_scope_gate_pending'] and x['registrar_state_keeps_OPEN'] for x in res['per_id'])
(D/'author-comparison.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='per_id'},ensure_ascii=False,indent=2))
