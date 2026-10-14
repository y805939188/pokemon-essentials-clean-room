"""Serialize manually assigned clause/case responsibility; no reference execution.

Parsing below locates existing formal lines and test IDs only. Hand-written maps
explicitly separate semantic review in this subdomain from content-only reads.
"""
import datetime
import json
import pathlib
import re

ROOT=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=ROOT/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-CA/subtasks/effects-c'
F='deliverables/final-specification-set/combat-requirements/wp52-c-items-calling-and-control-evaluation.md'
C='deliverables/final-specification-set/combat-requirements/wp52-c-item-control-coverage-and-data.md'
B='deliverables/final-specification-set/combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md'
BC='deliverables/final-specification-set/combat-requirements/wp52-b-effect-coverage.md'
CAT='deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md'
forward=[json.loads(x) for x in (OUT/'forward-matrix.jsonl').read_text().splitlines()]
def uid(file,start):return f'EC-{file}-{start:03d}'
ce={
 8:('ai010:470-476,559-560','75/76 boundary6/−6 and preserving/clamp order checked'),
 9:('ai010:477-498,559-560','Gen8 high-HP negative healing6, Ripen−9, disliked-confusable−3→−12 checked'),
 10:('ai010:499-508,559-560','ASPEARBERRY branch cannot find ASPEAR key;−6 or clamped0'),
 11:('ai010:554-557','Leppa constant6/Ripen9 without PP condition checked'),
 12:('ai010:515-526','Taunt1 does not count;Taunt2 does;preserving−6/+6'),
 13:('EC-007-004,EC-007-036,EC-007-065; battler:421-427','Independent item-activation and four-times signs checked; no held-item prerequisite in activation'),
 14:('EC-007-157','Corrosion V9→0 difference−9 times4→−36; inactive side0'),
 15:('EC-007-176','Missing/inactive/nonpositive60 vs active9 gain18 checked'),
 16:('EC-007-191','W7 cap20/W0 useless;duration1 nil wrapper preserves input'),
 17:('EC-007-088,EC-007-093','Saved record current empty gain20;inactive60;occupied failure'),
 18:('EC-007-232,EC-007-238','Ordinary canConsumeBerry false not Stuff Cheeks failure;medium bonus5 checked'),
 19:('EC-007-273','Enemy utility clamps negative before sign;positive6→−6 checked;ally preserves'),
 20:('EC-007-343','Toxic Orb ordinary poison delegate and Flame Orb burn delegate, no separate toxic expectation'),
 21:('EC-008-599,EC-008-610','Slow stale-data check bypass/−10 vs fast target failure checked'),
 22:('EC-008-625,EC-008-627','Sketch target failure exists;overall copy absent;Mimic fast−5 not imported'),
 23:('EC-008-514','Whole same-side party scan does not exclude fainted/PP0;>=6 egg excluded'),
 24:('EC-008-535','Any nonblacklisted real sleepTalk-choice legal slot passes;all rejected fails'),
 25:('EC-008-144; realchange:229-266','Cave7 flinch delegate vs water5 unmatched symbol/default preserves checked'),
 26:('EC-008-004','Strict U above integer two-thirds and ally inclusive integer one-third checked;given interior vector valid'),
 27:('EC-008-240,EC-008-245','Only existing HelpingHand target-failure;usable damage+5 ignores acted flag'),
 28:('EC-008-080,EC-008-106,EC-008-115','Non-Ghost raise helper60 stops drop;Ghost HP half gate independent'),
 29:('EC-009-027,EC-009-062','Reserve-last status early60 vs damage−20 then remaining terms checked'),
 30:('EC-009-093,EC-009-104,EC-009-109','No reserve still drops scored;copy failure cannot overwrite'),
 31:('EC-009-120','Perish−20 and+4 stage25 additive5;reserve flag−20 further'),
 32:('EC-009-200','Wild early preserves/current substitute trainer preserves;does not predict substitute break'),
 33:('EC-009-296,EC-009-345','No-reserve status60/damage retains;Octolock drop component independent'),
 34:('EC-009-238','5+10+8+10+15=48;existing bind early preserves checked'),
 36:('EC-009-456;ai010:292-312;ai008:23-27','Round same-side includes U;finite PP0 excluded'),
 37:('EC-009-475','Position distance2 gives10;distance1 gives60;not actual priority'),
 38:('EC-009-505','Eligible Quash target before slowest ally local−10;alreadylast60'),
 39:('EC-009-545','First matching duplicate slot determines local PP eligibility;real-lookup suffix belongs WP47B parent'),
 40:('EC-009-545','T faster60;otherwise legal prior slot+10 without action replay'),
 41:('EC-009-643','Fast PP6 gives10,7/11 both−10;trailing penalty checked'),
 42:('EC-009-665','Mental Herb60;without5+10+8=23 checked'),
 43:('EC-009-771','Empty choice-lock branch yields60;populated lock continues;direction not normalized'),
 44:('EC-009-722;ai010:231-257,567-595','Fast raw type immunity20/super−8;slow10 checked'),
 45:('EC-009-840','ThroatChop1 allowed/2 blocked;additional-effect sentinel checked'),
 46:('EC-009-862;pbs_moves:7450-7457;targetdata:26-33,59-62;ai005:45-56','Ordinary User target0 does not consume;direct target hook first foe only8'),
 52:('EC-009-574;ai010:199-216','High rough speed may already include Tailwind;second multiplier and room-duration>1 inversion checked'),
 53:('EC-007-268,EC-007-329','Teatime lacks active-item gate/Fling has it;distinct entry rules'),
 54:('EC-007-111,EC-007-157','Removal+36/corrosion−36 same V9 target checked'),
 55:('handlerhash:154-160','Direct registry lookup precedes ordered first-matching condition;future case not runtime tested'),
 56:('EC-008-240,EC-008-245;ai001:105-113','Helping Hand target+5;no whole registration from global literal registration inventory'),
 57:('EC-009-857,EC-009-862;pbs_moves:7450-7457;targetdata:26-33,59-62','Normal targetless overall100 if other changes absent;direct target108 not116'),
}
be={
 'B10':('EC-008-255,EC-008-260','Counter qualifying foe terms5+8+5=18;no foes60;local base60 distinct from default targetless normal scoring'),
 'B11':('EC-008-319,EC-008-324','Metal Burst slower-than-foe gate checked;no damage record simulation'),
 'B29':('EC-008-392,EC-008-401','Swallow at h50 early−10 skips low-count5;h49 adds10 then−5'),
 'B55':('EC-008-187;realchange:340-354','Grounded Psychic81*3/2 integer121;ungrounded81;target expansion separately real query'),
 'B56':('EC-008-057,EC-008-062','Friend49% integer gain10 vs50%−10;enemy keeps;general inversion separate'),
 'B57':('EC-008-418,EC-008-431,EC-008-444','Per ally one10 if other Pledge;only same function0'),
}
catalog=[]
section=''
for no,line in enumerate((ROOT/CAT).read_text().splitlines(),1):
    if line.startswith('## '):section=line[3:].split('：')[0]
    m=re.match(r'\| ([A-Z]\d+(?:[a-z])?) \|',line)
    if not m:continue
    case=m.group(1)
    e={'path':CAT,'line':no,'series':section,'case':case,'content_read':True,
      'status':'READ_OUTSIDE_ASSIGNED_SEMANTIC_SCOPE','aggregate_pass':False}
    if section=='CE' and case.startswith('C'):
        n=int(case[1:])
        if n in ce:e.update({'status':'SOURCE_STATIC_DERIVED_VECTOR_CHECKED_WITH_NAMED_PRECONDITIONS','source_units':ce[n][0],'semantic_check':ce[n][1]})
        elif n==59:e.update({'status':'PARTIAL_DOMAIN_SUPPORT_PARENT_OWNS_B_OVERRIDES','source_units':'EC-009-104,EC-009-109;handlerhash:97-140','semantic_check':'Parting Shot cross-family absence checked;Fury Cutter/RemoveProtections source units outside child'})
    elif section=='BE' and case in be:e.update({'status':'SOURCE_STATIC_DERIVED_VECTOR_CHECKED_WITH_NAMED_PRECONDITIONS','source_units':be[case][0],'semantic_check':be[case][1]})
    catalog.append(e)
(OUT/'catalog-matrix.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in catalog))

# Every nonblank C formal line gets a read/scope row. A source-backed local
# clause is distinguished from an index entry and from a parent-owned clause.
scope=[]
for path in [F,C]:
    for no,line in enumerate((ROOT/path).read_text().splitlines(),1):
        if not line.strip():continue
        own=[r['unit_id'] for r in forward if (r['formal']['path']==path and r['formal']['line']==no) or (r['formal_coverage']['path']==path and r['formal_coverage']['line']==no)]
        e={'formal':{'path':path,'line':no},'content_read':True,'aggregate_pass':False}
        if own:e.update({'scope':'ASSIGNED_SOURCE_CLAUSE','semantic_units':own,'status':'SEE_DISTINCT_HAND_REASONED_UNITS'})
        elif line.startswith('#') or line.strip()=='---' or re.match(r'\| [-: ]+\|',line):e.update({'scope':'DOCUMENT_STRUCTURE','status':'READ_STRUCTURE_ONLY'})
        else:e.update({'scope':'SHARED_OR_OTHER_SOURCE_RESPONSIBILITY','status':'READ_NOT_WHOLE_DOMAIN_SEMANTIC_SIGNOFF','parent_owner':'R6-CA'})
        if path==F and 62<=no<=77:
            e.update({'scope':'SHARED_CONSUMPTION_HELPER_READ','status':'SOURCE_STATIC_HELPER_CHECKED','source':'005_AI/010_AIBattler.rb:470-560','limits':'Stat-worthwhile central helper is parent-owned;item utility branch/constants and clamping independently read here.'})
        if path==F and no==108:e.update({'scope':'SHARED_PREPARATION_CONSUMER','status':'SOURCE_STATIC_CHECKED','source':'005_AI/005_AI_ChooseMove.rb:142-171;011_AIMove.rb:11-16','limits':'Real nested invocation and blacklist complete datasets remain WP47 parent-owned.'})
        if path==F and no==156:e.update({'scope':'PARTIAL_LOCAL_CLAUSE','status':'SHELL_TRAP_CHECKED_FOCUS_PUNCH_SUCKER_PUNCH_PARENT_OWNED','semantic_units':['EC-009-426','EC-009-437']})
        if path==F and no==158:e.update({'scope':'PARTIAL_LOCAL_CLAUSE','status':'ROUND_CHECKED_BEAK_BLAST_PARENT_OWNED','semantic_units':['EC-009-456']})
        scope.append(e)
(OUT/'formal-scope-matrix.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in scope))

considered=[
 {'candidate':'EC-CONSIDERED-01','question':'Sketch/Parting Shot cross-family copies accidentally scored as effective?','status':'NOT_PROPOSED_FORMAL_ALREADY_EXPLICIT',
  'source':['008_AI_MoveEffects_ChangeMoveEffect.rb:625-628','009_AI_MoveEffects_SwitchingActing.rb:93-110','005_Event_Handlers.rb:102-118'],
  'formal':[F+':117-118',F+':142',C+':17-18',C+':72-74',C+':84'],'reason':'Both exact absent-source cases and retention/default distinction already expressed;ordinary counterexample matches existing prose.'},
 {'candidate':'EC-CONSIDERED-02','question':'Secret Power water/stat-drop path should gain attack-drop score?','status':'NOT_PROPOSED_FORMAL_PRESERVES_OBSERVED_QUIRK',
  'source':['008_AI_MoveEffects_ChangeMoveEffect.rb:144-182','012_MoveEffects_ChangeMoveEffect.rb:229-266'],
  'formal':[F+':130',CAT+':260'],'reason':'Unassigned stat variable and unmatched symbol lookup preserve input;spec explicitly does not repair it to real effect semantics.'},
 {'candidate':'EC-CONSIDERED-03','question':'Default Imprison target score +8 actually consumed?','status':'NOT_PROPOSED_FORMAL_ALREADY_HAS_ORDINARY_PATH_BOUNDARY',
  'source':['009_AI_MoveEffects_SwitchingActing.rb:857-877','PBS/moves.txt:7450-7457','017_Target.rb:26-33,59-62','005_AI_ChooseMove.rb:45-56,232-285'],
  'formal':[F+':178',CAT+':281',CAT+':292'],'reason':'Normal User has zero targets;formal explicitly excludes target-hook consumption and distinguishes direct108 from normal100.'},
 {'candidate':'EC-CONSIDERED-04','question':'Three counter base60 registrations imply ordinary damage-score consumption?','status':'NOT_PROPOSED_LOCAL_HOOK_CONTRACT_QUALIFIED_BY_SHARED_ENTRY_GATE',
  'source':['008_AI_MoveEffects_ChangeMoveEffect.rb:255-344','PBS/moves.txt:2255-2265,7278-7288,8205-8214','017_Target.rb:26-33,53-57','005_AI_ChooseMove.rb:45-56,232-285'],
  'formal':[B+':13',B+':71',CAT+':144',CAT+':159-160'],'reason':'Ordinary None-target action scores overall preference but not per-target damage. B values expressly local handler/base quantities and conditional entry, so no false ordinary-candidate arithmetic asserted;recorded explicit consumer caveat in each P matrix row.'},
 {'candidate':'EC-CONSIDERED-06','question':'After You/Instruct ally+10 and Pollen Puff healing branch reachable as ordinary default AI single-target candidates?','status':'NOT_PROPOSED_SHARED_WP51_FOE_FILTER_ALREADY_EXPLICIT',
  'source':['005_AI_ChooseMove.rb:57-69','017_Target.rb:136-141','PBS/moves.txt:53-62,5687-5694,7460-7468','009_AI_MoveEffects_SwitchingActing.rb:475-500,545-569','008_AI_MoveEffects_ChangeMoveEffect.rb:57-75'],
  'formal':['deliverables/final-specification-set/combat-requirements/wp51-ai-action-selection-and-skill.md:132',F+':162',F+':164',B+':128',CAT+':232'],
  'reason':'Default NearOther single-target enumeration excludes ally candidates. Positive ally branches are local/direct calculations, not normal selected ally actions. Existing WP51 clause states this exact general filter;each relevant forward row now records ordinary nonconsumption explicitly.'},
 {'candidate':'EC-CONSIDERED-05','question':'Fling base default10 also holds when no item and prediction flag off?','status':'NOT_PROPOSED_NORMAL_ELIGIBILITY_AND_EXCEPTION_SCOPE_PRESERVED',
  'source':['007_AI_MoveEffects_Items.rb:329-376','011_MoveEffects_Items.rb:431-436','005_AI_ChooseMove.rb:66-68'],
  'formal':[F+':99',F+':208'],'reason':'Normal prediction rejects no item;direct base query underlying0 and medium target-score nil-item failure are separately recorded. Prose does not promise a successful itemless normal10 candidate;independent score/prediction exception reservation already explicit.'},
 {'candidate':'GR6-C-001','status':'PARTIAL_CROSSCHECK_NO_FINAL_REBUTTAL_BY_THIS_CHILD',
  'source':['005_AI/001_Battle_AI.rb:28-31,44','005_AI/008_AI_Utilities.rb:9-35'],
  'reason':'Sparse original array and nil-safe named iterators independently confirmed. Direct high-skill switch scans, legal layout construction, exact early-short-circuit normal sets and exception reporting are parent-owned and not replaced by this partial check.'},
]
(OUT/'considered-issues.json').write_text(json.dumps(considered,ensure_ascii=False,indent=2)+'\n')
status=json.loads((OUT/'task-status.json').read_text())
status.update({'status':'COMPLETE_ASSIGNED_STATIC_SUBDOMAIN','completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'catalog_rows_read':len(catalog),'catalog_rows_semantically_checked_here':sum(x['status'].startswith('SOURCE_STATIC') for x in catalog),
 'formal_c_nonblank_scope_rows':len(scope),'reverse_matrix_rows':len((OUT/'reverse-matrix.jsonl').read_text().splitlines()),
 'blockers':[],'scope_limit':'This child does not classify GR6-C-001 or sign off parent-owned ItemRanking/Misc/BattlerOther/WP51 sources.'})
(OUT/'task-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
with (OUT/'reading-ledger.jsonl').open('a') as f:
    for path in [F,C,B,BC,CAT]:
        f.write(json.dumps({'kind':'semantic_scope_recorded','path':path,'time_utc':status['completed_at_utc'],
          'record':'formal-scope-matrix.jsonl/catalog-matrix.jsonl/forward-matrix.jsonl/reverse-matrix.jsonl',
          'note':'Whole content newly read; only explicitly assigned source clauses/cases marked semantically checked;shared/outside responsibility not signed off.'},ensure_ascii=False)+'\n')
print(json.dumps({'catalog_rows':len(catalog),'case_checks_here':status['catalog_rows_semantically_checked_here'],
 'formal_scope_rows':len(scope),'status':status['status']},ensure_ascii=False))
