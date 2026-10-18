#!/usr/bin/env python3
"""Serialize this context's manually reviewed finite metadata conclusions."""
import datetime
import hashlib
import json
import pathlib
import re
import stat
import subprocess

BASE = pathlib.Path(__file__).resolve().parent
REPO = BASE.parents[4]
RR = BASE.parents[1]
R = pathlib.Path('/workspace/pokemon-essentials')
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
RC = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REVIEWER = '/root/reference_metadata_completion'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def write(name, value):
    (BASE/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

def git(*args, cwd=REPO):
    return subprocess.check_output(['git', *args], cwd=cwd, text=True).strip()

def identity(path, repo=None, commit=None):
    path = pathlib.Path(path)
    data = path.read_bytes()
    row = {'path':str(path), 'bytes':len(data),
           'sha256':hashlib.sha256(data).hexdigest(),
           'actual_mode':oct(stat.S_IMODE(path.stat().st_mode)),
           'logical_lines':len(data.splitlines()), 'newline_count':data.count(b'\n')}
    if repo is not None:
        relative = str(path.relative_to(repo))
        row.update(repo=str(repo), path=relative, commit=commit,
                   git_blob=git('hash-object','--',relative,cwd=repo),
                   workspace_tree=git('rev-parse',commit+'^{tree}',cwd=repo))
        mode, kind, blob = git('ls-tree',commit,'--',relative,cwd=repo).split('\t')[0].split()
        row.update(git_mode=mode, git_type=kind, fixed_git_blob=blob,
                   fixed_bytes_match=data==subprocess.check_output(['git','show',commit+':'+relative],cwd=repo))
    return row

readset_path = RR/'delegation/readsets/reference_metadata.json'
readset = json.loads(readset_path.read_text())
primary = [identity(R/x['path'],R,RC) for x in readset['reference']]
assert sum(x['bytes'] for x in primary)==31678
assert sum(x['logical_lines'] for x in primary)==742
assert all(x['fixed_bytes_match'] for x in primary)
assert git('rev-parse',B8+'^{tree}')=='751dfde81048c81390f89a65ca1d1a565ba8e1ca'
assert git('rev-parse',B8+':deliverables/final-specification-set')=='f292698cdd4a8e725525a9be6dc34b75faaf151e'

purpose = {
 '.gitignore':'Version-control inclusion/exclusion metadata; not a runtime inventory or a filesystem deletion rule.',
 '.rubocop.yml':'Author static-lint configuration and rationale; no RuboCop/runtime execution or future-framework style adoption.',
 'Essentials Engine wiki.url':'Five-line Windows InternetShortcut shell metadata; external target content is not an input.',
 'LICENSE':'Complete CC BY-NC-SA 4.0 text classified as reference licensing metadata; no legal advice or applicability/compatibility judgment.',
 'README.md':'Current reference provenance and author-workflow statements; executable effects require the named source/loader premises.'}
for x in primary:
    x['purpose']=purpose[x['path']]
    x['actual_reader']=REVIEWER
    x['semantic_status']='FULL_READ_AND_TYPE_PURPOSE_DISPOSED'

contracts = [REPO/'AGENTS.md', RR/'inputs/eighth-global-review-prompt.md',
 RR/'inputs/review-SKILL.md', RR/'delegation/prompts/reference_metadata.md',readset_path,
 RR/'delegation/reference-metadata-real-primary-recovery-actual-start.v1.json']
dependencies = [RR/'adjudication/root-primary-task-final-registry.v1.json',
 RR/'adjudication/root-developer-task-final-acceptance.v1.json',
 RR/'tasks/developer_full_cloud/interfaces.json',
 RR/'tasks/developer_full_cloud/forward-mapping.json',
 REPO/'deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md']
depids=[]
for p in dependencies:
    d=identity(p,REPO,B8) if 'deliverables' in p.parts else identity(p)
    d['read_scope'] = ('L1–105 and L309–360 actually read; formal dependency only, primary whole-file credit remains developer owner.'
       if 'deliverables' in p.parts else 'Full operative receipt/interface, or exact selected fact objects; see dependency-reception.json for exact granularity.')
    depids.append(d)
write('identities.json', {'schema':'gr8-reference-metadata-identities/v1','recorded_utc':NOW,
 'fixed_B8':B8,'fixed_R':RC,'reference_tree':git('rev-parse',RC+'^{tree}',cwd=R),
 'report_branch':git('branch','--show-current'),'report_HEAD_at_identity_capture':git('rev-parse','HEAD'),
 'local_main_ref':'ABSENT: initial git rev-parse main failed; no main ref created or moved',
 'primary':primary,'contracts':[identity(p) for p in contracts],'dependencies':depids,
 'fixed_checks_are_identity_only':True,'working_tree_limit':'Other task changes exist; no overlapping writer observed in exclusive tasks/reference_metadata_completion/.'})

units=[]
def add(path, key, start, end, fact, disposition, consumer=None, premise=None, children=None):
    row={'id':'RM-'+str(len(units)+1).zfill(3),'path':path,'unit':key,'lines':[start,end],
         'actual_reader':REVIEWER,'fact':fact,'disposition':disposition,
         'consumer':consumer or 'Reference metadata/type-and-purpose audit; no game behavior contract required',
         'premise':premise or 'Limited to the fixed reference bytes and this object type.',
         'evidence_level':'SOURCE_STATIC','business_execution':'NOT_EXECUTED'}
    if children: row['subassertions']=children
    units.append(row)

ignores=[
 ('media-and-plugin-folders',1,6,'Four directory patterns cover Audio, Graphics, Plugins and Screenshots. Each has the directory suffix.', ['Audio/','Graphics/','Plugins/','Screenshots/']),
 ('data-exclusion-and-three-reinclusions',7,12,'Data immediate children are excluded, with explicit reinclusion of the archive loader, script directory and core messages file.', ['Data/*','!Data/Scripts.rxdata','!Data/Scripts/','!Data/messages_core.dat']),
 ('project-root-patterns',13,18,'Patterns identify errorlog, two project descriptors and matching RGSS libraries.', ['errorlog.txt','Game.ini','Game.rxproj','RGSS*.dll']),
 ('editor-patterns',19,24,'Four author editor/workspace metadata patterns.', ['.vscode/','*.code-workspace','.idea/','*.mkproj']),
 ('operating-system-patterns',25,31,'Five OS-generated names/patterns, including an optional-suffix DS_Store pattern and two Desktop case variants.', ['.DS_Store','.DS_Store?','ehthumbs.db','Thumbs.db','[Dd]esktop.ini']),
 ('temporary-pattern',32,34,'Names with a leading tilde are classified as temporary.', ['~*'])]
for key,a,b,f,children in ignores:
    add('.gitignore',key,a,b,f,'ADMIN_VERSION_CONTROL',
        'Git author workflow; README L34–42',
        'Pattern text only: tracked files remain tracked; ignore matches alone do not establish actual absence or an unavailable asset.',children)

config_notes={
 'AllCops':'Target syntax/lint compatibility string is 3.0; new cops are enabled. This is not a measured Ruby host version.',
 'Layout/EmptyLineAfterGuardClause':'Guard-clause empty-line cop disabled.',
 'Layout/ExtraSpacing':'Alignment and spacing before trailing comments allowed.',
 'Layout/FirstHashElementIndentation':'Consistent first-element indentation.',
 'Layout/HashAlignment':'Both rocket and colon hash alignment use table style.',
 'Layout/MultilineMethodCallBraceLayout':'Multiline call brace layout cop disabled.',
 'Layout/SpaceInsideHashLiteralBraces':'No-space hash brace style.',
 'Lint/UnusedBlockArgument':'Unused block argument cop disabled.',
 'Lint/UnusedMethodArgument':'Unused method argument cop disabled.',
 'Metrics':'Entire Metrics department disabled; comment is maintenance rationale, not a complexity measurement.',
 'Naming/ClassAndModuleCamelCase':'Camel-case class/module naming cop disabled.',
 'Naming/FileName':'Filename naming cop disabled; numbering/display rationale read.',
 'Naming/MethodName':'Method naming cop disabled; comment estimate is author rationale, not a newly verified count.',
 'Naming/MethodParameterName':'Parameter naming cop disabled; comment estimate is author rationale, not a newly verified count.',
 'Naming/VariableName':'Variable naming cop disabled; comment estimate is author rationale, not a newly verified count.',
 'Security/Eval':'Eval cop disabled; comment describes script conditions/switches, not safe-execution approval.',
 'Security/MarshalLoad':'Marshal-load cop disabled; not an authorization to deserialize arbitrary input.',
 'Style/AccessorGrouping':'Accessor grouping cop disabled.',
 'Style/ConditionalAssignment':'Cop disabled; assign_inside_condition remains a configured style field without making the disabled cop active.',
 'Style/Documentation':'Documentation cop disabled; comment points to yard as author practice.',
 'Style/EndlessMethod':'Endless method style disallowed.',
 'Style/FormatString':'sprintf style selected.',
 'Style/FormatStringToken':'Unannotated format tokens selected.',
 'Style/FrozenStringLiteralComment':'Frozen-string comment cop disabled; not a runtime claim that every string is mutable.',
 'Style/GlobalVars':'Global variable style cop disabled.',
 'Style/HashSyntax':'Mixed hash-key syntax disallowed by selected style.',
 'Style/IfInsideElse':'Cop disabled, with AllowIfModifier retained as a field.',
 'Style/Lambda':'lambda style selected.',
 'Style/NegatedIf':'Negated-if cop disabled; rationale read without imposing future product style.',
 'Style/NumericPredicate':'Comparison style selected; this is lint preference, not a numeric behavior guarantee.',
 'Style/OptionalBooleanParameter':'Optional boolean parameter cop disabled.',
 'Style/PreferredHashMethods':'Preferred hash method cop disabled.',
 'Style/RedundantReturn':'Redundant return cop disabled.',
 'Style/SingleLineBlockParams':'Single-line block parameter cop disabled.',
 'Style/SingleLineMethods':'Single-line methods cop disabled.',
 'Style/SlicingWithRange':'Slicing-with-range cop disabled.',
 'Style/StringLiterals':'Double-quoted string style selected; comment allows needed literal semantics.',
 'Style/SymbolArray':'Bracket symbol array style selected.',
 'Style/WordArray':'Bracket word array style selected.',
 'Style/SymbolProc':'Methods with arguments allowed for this cop.',
 'Style/TernaryParentheses':'Ternary condition parentheses required by style.',
 'Style/WhileUntilModifier':'While/until modifier cop disabled.'}
config_lines=(R/'.rubocop.yml').read_text().splitlines()
config_keys=[(i,s[:-1]) for i,s in enumerate(config_lines,1) if re.match(r'^[A-Za-z][^:]*:$',s)]
assert set(k for _,k in config_keys)==set(config_notes)
for n,(a,key) in enumerate(config_keys):
    z=(config_keys[n+1][0]-1) if n+1<len(config_keys) else len(config_lines)
    fields=[]
    for line in config_lines[a:z]:
        if re.match(r'^  [A-Za-z]',line):
            k,v=line.strip().split(':',1);fields.append({'key':k,'value_text':v.strip()})
    add('.rubocop.yml',key,a,z,config_notes[key],'AUTHOR_LINT_CONFIG',
        'RuboCop configuration reader if an author invokes it; not invoked in this task.',
        'Exact field values and full surrounding rationale read; installed RuboCop version, enabled defaults and lint outcomes unverified.',fields)

add('Essentials Engine wiki.url','shell-property-set',1,2,'GUID-shaped shell property section and Prop3 numeric tuple retained as shortcut metadata.','ADMIN_SHORTCUT',children=['section identifier','Prop3=19,11'])
add('Essentials Engine wiki.url','internet-shortcut',3,5,'InternetShortcut section contains an HTTPS wiki target and an empty IDList field.','ADMIN_SHORTCUT',
    'Windows shell or user opening this shortcut, neither executed nor browsed here.',
    'Target string is not the target page contents; external site availability, accuracy and behavior remain outside this readset.',
    ['InternetShortcut section','URL target string','empty IDList'])

lic=[
 ('title-and-corporation-disclaimer',1,15,'License identity is Attribution-NonCommercial-ShareAlike 4.0 International; corporation disclaimer covers non-law-firm role, no lawyer-client relation, as-is information and disclaimer scope.'),
 ('using-public-licenses-introduction',16,23,'Considerations are informational, non-exhaustive and outside the license terms.'),
 ('licensor-considerations',24,37,'Licensor guidance discusses authority, irrevocability, understanding terms, securing rights and marking excluded material.'),
 ('public-considerations',38,55,'Public guidance distinguishes permissions actually needed, copyright authority, other restrictions and nonmandatory requests.'),
 ('public-license-acceptance',56,71,'Public License heading and acceptance/consideration framing identify the terms that follow.'),
 ('1a-adapted-material',72,83,'Defines Adapted Material by permission-requiring derivation and the stated music synchronization case.'),
 ('1b-adapter-license',84,87,'Defines the license applied to the adapter contribution.'),
 ('1c-compatible-license',88,91,'Defines the named compatibility category by the designated list; list not fetched.'),
 ('1d-copyright-and-similar-rights',92,99,'Defines covered copyright and related rights and explicitly excludes the stated other-rights categories.'),
 ('1e-effective-technological-measures',100,105,'Defines technological measures by the stated treaty/law reference; no application to this project decided.'),
 ('1f-exceptions-limitations',106,109,'Defines exceptions and limitations that apply to a use.'),
 ('1g-license-elements',110,113,'Defines the three named elements.'),
 ('1h-licensed-material',114,117,'Defines material to which the licensor applied the license.'),
 ('1i-licensed-rights',118,122,'Defines granted rights by applicable copyright/similar rights and licensor authority.'),
 ('1j-licensor',123,125,'Defines the granting person or entity.'),
 ('1k-noncommercial',126,133,'Defines NonCommercial and the no-monetary-compensation file-sharing condition.'),
 ('1l-share',134,141,'Defines public provision by permission-requiring methods, including individually chosen access.'),
 ('1m-database-rights',142,147,'Defines database rights by directive and equivalent-rights reference.'),
 ('1n-you',148,151,'Defines the exercising individual/entity and corresponding possessive.'),
 ('2a1-grant-and-two-branches',152,166,'Grant terms are worldwide, royalty-free, non-sublicensable, non-exclusive and irrevocable; reproduction/sharing and adapted-material production/reproduction/sharing each carry the stated NonCommercial condition.'),
 ('2a2-exceptions',167,171,'States license terms do not apply where exceptions/limitations apply.'),
 ('2a3-term-reference',172,174,'Term points to section 6(a).'),
 ('2a4-media-and-technical-modifications',175,186,'Covers media/formats and necessary technical changes, related waiver/nonassertion and the stated non-adaptation treatment.'),
 ('2a5a-downstream-material',187,194,'Downstream recipients receive the licensor offer for Licensed Material.'),
 ('2a5b-downstream-adapted-material',195,200,'Downstream adapted-material offer is under the adapter license conditions.'),
 ('2a5c-downstream-restrictions',201,207,'Describes restrictions on additional terms and technological measures that restrict granted exercise.'),
 ('2a6-no-endorsement',208,214,'Grant does not imply connection, sponsorship, endorsement or official status.'),
 ('2b1-moral-personality-rights',215,224,'Other-rights clause distinguishes unlicensed moral/privacy/publicity rights and limited waiver/nonassertion.'),
 ('2b2-patents-trademarks',225,227,'States patent and trademark rights are not licensed.'),
 ('2b3-royalties',228,237,'Separates possible waiver of collection for licensed exercise from reserved royalties in other cases.'),
 ('3-condition-preamble',238,244,'Exercise of Licensed Rights is subject to following conditions; attribution heading.'),
 ('3a1ai-creator-identity',245,256,'Sharing condition retains supplied creator/designated attribution identification in a reasonable requested manner.'),
 ('3a1aii-copyright-notice',257,258,'Sharing condition retains a supplied copyright notice.'),
 ('3a1aiii-license-notice',259,260,'Sharing condition retains a supplied notice referring to the license.'),
 ('3a1aiv-disclaimer-notice',261,263,'Sharing condition retains a supplied warranty disclaimer notice.'),
 ('3a1av-material-link',264,266,'Sharing condition retains supplied material URI/link to the reasonably practicable extent.'),
 ('3a1b-modification-indication',267,269,'Sharing condition indicates modifications and retains prior modification indication.'),
 ('3a1c-license-identification',270,273,'Sharing condition identifies license and supplies text or URI/link.'),
 ('3a2-reasonable-manner',274,279,'Conditions may be satisfied reasonably according to medium, means and context, with link example.'),
 ('3a3-removal-request',280,283,'Licensor-requested removal of specified information applies to the reasonably practicable extent.'),
 ('3b1-adapter-license',284,292,'For shared produced Adapted Material, adapter license uses same elements at this/later version or listed compatible license.'),
 ('3b2-adapter-license-link',293,297,'Adapter-license text or URI/link may be provided reasonably for the sharing context.'),
 ('3b3-no-extra-restrictions',298,303,'Adapter terms/measures must not restrict exercise of adapter-license rights in the stated way.'),
 ('4a-database-use',304,313,'If covered database rights apply, substantial contents extraction/reuse/reproduction/sharing grant carries the NonCommercial condition.'),
 ('4b-adapted-database',314,319,'Describes inclusion of substantial contents in a protected database and distinguishes database from individual contents.'),
 ('4c-database-attribution',320,322,'Substantial-contents sharing invokes section 3(a) conditions.'),
 ('4-supplement',323,327,'Database section supplements rather than replaces other applicable copyright/similar-rights obligations.'),
 ('5a-no-warranties',328,340,'States as-is/as-available and broad warranty disclaimer subject to separate undertaking and allowed jurisdictional extent.'),
 ('5b-liability-limits',341,350,'States broad liability limitation with the stated jurisdictional qualification.'),
 ('5c-disclaimer-interpretation',351,356,'Directs the disclaimer interpretation toward the stated maximum possible waiver.'),
 ('6a-term-and-termination',357,363,'Term follows licensed rights and noncompliance triggers automatic termination as stated.'),
 ('6b-reinstatement-and-remedies',364,376,'Reinstatement alternatives are cure within 30 days of discovery or express reinstatement; licensor remedies remain unaffected.'),
 ('6c-separate-offers-and-distribution',377,381,'Separate terms or stopping distribution do not themselves terminate the public license.'),
 ('6d-survival',382,385,'States which numbered sections survive termination.'),
 ('7a-extra-terms',386,390,'Additional or different communicated terms bind licensor only if expressly agreed.'),
 ('7b-separate-arrangements',391,395,'Other arrangements remain separate and independent.'),
 ('8a-permission-unneeded-use',396,402,'Interpretation does not constrain uses lawfully made without license permission.'),
 ('8b-unenforceable-provision',403,409,'Describes minimum reformation or severance while preserving remaining terms.'),
 ('8c-express-waiver',410,413,'Waiver/consent requires express agreement.'),
 ('8d-privileges-immunities',414,420,'States preservation of relevant privileges and immunities.'),
 ('cc-postscript-and-contact',421,436,'Postscript distinguishes CC nonparty status, optional licensor role for its own publications, trademark permission policy, paragraph exclusion from license and contact address.')]
assert lic[0][1]==1 and lic[-1][2]==436
assert all(lic[i][2]+1==lic[i+1][1] for i in range(len(lic)-1))
for key,a,b,f in lic:
    add('LICENSE',key,a,b,f,'LICENSE_TYPE_AND_PURPOSE',
        'Reference provenance/license audit (L13); no gameplay or future implementation clause is derived.',
        'This records the complete text type and conditional structure only. Rights ownership, applicability, compatibility, legal compliance and future framework licensing are not adjudicated.')

readme=[
 ('identity-and-version',1,4,'Identifies Pokémon Essentials and states basis on v21.1.','PROVENANCE',None),
 ('fork-and-update-workflow',5,14,'Suggests fork, separately acquire v21.1, overlay clone and pull future changes; no successful download, merge or game-start observation.','AUTHOR_GUIDANCE',None),
 ('split-script-location',15,18,'States scripts are individual files in Data/Scripts and subfolders, with collaboration/versioning rationale.','CURRENT_WORKFLOW','WP75 §1, §2, §12.1–12.2'),
 ('script-discovery-order',19,20,'States per-folder scripts first, then ordered recursive subfolders. Exact .rb/hidden-directory and failure premises come from DEV-LOADER, not README.','BEHAVIOR_JOIN','WP75 §12.4'),
 ('two-root-tools',21,24,'Names two root author tools and distinguishes extraction and reintegration purposes.','CURRENT_WORKFLOW','WP75 §3.2'),
 ('extract-and-clear',25,25,'Extraction statement includes deleting existing individual scripts; precise source contract clears the whole tree after the archive-size guard.','BEHAVIOR_JOIN','WP75 §3.3, §12.1'),
 ('backup-and-loader',26,26,'Normal extraction backs up the old archive before installing a loader archive; failed earlier stages need not reach backup.','BEHAVIOR_JOIN','WP75 §12.1, §12.4'),
 ('combine-and-retained-files',27,28,'Combining produces an archive and leaves script files in place; their lack of direct effect is conditional on consuming that archive, not a promise that files cannot be read elsewhere.','BEHAVIOR_JOIN','WP75 §12.2'),
 ('ruby-prerequisite-and-intention',29,31,'Author tools require Ruby; future friendlier tooling is an intention rather than a current product requirement. No Ruby version is promised here.','AUTHOR_GUIDANCE','WP75 §3.2'),
 ('gitignore-entry-and-four-folders',32,36,'README explains omission policy and lists four folder families; actual inventory is not inferred from this prose.','ADMIN_VERSION_CONTROL','.gitignore L1–6'),
 ('data-exceptions',37,40,'README lists script tree, loader archive and core-message exceptions; translation utility does not certify selected language, translation quality or runtime load.','ADMIN_VERSION_CONTROL','.gitignore L7–12; existing kernel/media owners retain message behavior scope'),
 ('root-and-temp-omissions',41,42,'README summarizes project-root and temporary omissions; editor/OS patterns are explicitly present in the fully read .gitignore.','ADMIN_VERSION_CONTROL','.gitignore L13–34')]
for key,a,b,f,d,c in readme:
    add('README.md',key,a,b,f,d,c,
        'README is current author-facing text; source/program facts and allowed normal/failed prefixes are separately received where behavior is asserted.')

file_rows=[]
for x in primary:
    p=x['path']; intervals=[[1,x['logical_lines']]]
    io= ['002-license-1','005-license-2','006-license-3'] if p=='LICENSE' else ['003-config-read']
    file_rows.append({'path':p,'identity_sha256':x['sha256'],'logical_lines':x['logical_lines'],
      'newline_count':x['newline_count'],'read_intervals':intervals,
      'read_io_labels':io,'actual_reader':REVIEWER,'status':'FULL_READ',
      'structural_unit_ids':[u['id'] for u in units if u['path']==p],
      'unread_intervals':[],'unreceived_units':0,'purpose':purpose[p]})
write('reading-ledger.json',{'schema':'gr8-reference-metadata-reading-ledger/v1',
 'actual_reader':REVIEWER,'recorded_utc':NOW,'files':file_rows,'structures':units,
 'counts':{'files':5,'logical_lines':742,'newlines':741,'bytes':31678,
           'structural_units':len(units),'rubocop_top_level_blocks':len(config_keys),
           'license_contiguous_clause_units':len(lic),'gitignore_patterns':22,
           'available_primary_unread':0,'available_primary_unreviewed_units':0,'necessary_incoming_unreceived':0},
 'line_count_explanation':'LICENSE final line has no LF: 436 logical lines versus 435 newlines; combined wc -l is 741, full splitlines count is 742.',
 'continuous_io':'License reads 1–160,161–320,321–436; other four objects each emitted to EOF in 003. Comments, separators, blank context and all final bytes actually read.',
 'secondary_actual_reading':{'formal_path':'deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md','intervals':[[1,105],[309,360]],'primary_whole_file_credit':False},
 'attempted_extra_output':'010 emitted WP75 1–180 together with other outputs and renderer truncation occurred. Only later fully visible 013 ranges (1–105) and 014 (309–360) are credited. Rest is unused, not needed and not counted as FULL.'})

finite=json.loads((BASE/'read-io/018-script-finite-facts-corrected.stdout').read_text())
assert len(finite['entries'])==18
fwd=json.loads((RR/'tasks/developer_full_cloud/forward-mapping.json').read_text())
loader=next(x for x in fwd['entries'] if x['id']=='DEV-LOADER')
loader_selected={k:loader[k] for k in ['id','source','actual_receiver','original_reader','fact','evidence_level','disposition','runtime']}
assert loader_selected['source']['sha256']=='da24a2220936c6d44ddc60f180aed37beede022012d7addc99b5562ed07c52e1'
write('dependency-reception.json',{'schema':'gr8-reference-metadata-finite-dependency-reception/v1',
 'receiver':REVIEWER,'recorded_utc':NOW,'status':'FINITE_NECESSARY_INCOMING_JOIN_RECEIVED',
 'root_receipt':'adjudication/root-developer-task-final-acceptance.v1.json',
 'receipt_role':'Original full-source reader qualification and exact scope, not a PASS substitute.',
 'script_facts':finite['entries'],'loader_fact':loader_selected,
 'actually_received_semantics':[
  'Extraction/archive≥10 guard precedes destructive cleanup and exports; backup then loader on normal reaching those stages. Earlier failures keep precise already-written prefixes.',
  'Combine/archive≤10 guard then discard old list, rebuild from sorted files before sorted subdirectories, retain loose files and overwrite archive without backup.',
  'Current fixed loader requires compatible unencrypted project and reachable file system. Files are loaded first per directory; hidden directories skipped; matching file suffix case-insensitive.',
  'Open/read is outside local eval rescue. ScriptError and ordinary-error diagnostics differ; actual message≥900 drives attempted log overwrite. Prior loaded effects are not rolled back.',
  'No Ruby loader, extraction, combine, game host, lint, production service or asset execution occurred.'
 ],
 'facts_not_imported':'Other developer facts, all formal-clause IDs mechanically attached by producer, whole unrelated callers and final global acceptances are not inherited.',
 'necessary_unreceived':0,'root_reception_of_this_new_contribution':'PENDING_ROOT_ACTUAL_RECEPTION',
 'business_execution':'NOT_EXECUTED'})

mapping=[]
for u in units:
    target=u['consumer']
    if u['path']=='README.md' and u['disposition']=='BEHAVIOR_JOIN': target=u['consumer']
    mapping.append({'unit_id':u['id'],'source':{'repo':str(R),'commit':RC,'path':u['path'],
      'lines':u['lines'],'identity_sha256':next(x['sha256'] for x in primary if x['path']==u['path'])},
      'fact':u['fact'],'premise':u['premise'],'consumer':target,
      'disposition':u['disposition'],'formal_requirement_created':False,
      'support':'Own full metadata read; exact dependency-reception facts where source behavior is needed.'})
write('forward-mapping.json',{'schema':'gr8-reference-metadata-forward/v1','reviewer':REVIEWER,
 'entries':mapping,'count':len(mapping),'unmapped_available_primary_units':0,
 'scope':'All five metadata files are disposed by type/use or joined to existing behavioral contracts. No license, lint or shortcut term is promoted to gameplay or future architecture.'})

wp75='deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md'
reverse=[
 ('RM-REV-01',[48,48],'External author scripts require Ruby; two default directions.','README.md',[23,30],['DEV-SRC-015','DEV-SRC-024'],'Runtime installation/version and tool execution are not observed.'),
 ('RM-REV-02',[54,54],'Two directions use opposite guards; normal/first-file-failure prefixes are distinct.','README.md',[25,28],['DEV-SRC-008','DEV-SRC-010','DEV-SRC-014','DEV-SRC-017','DEV-SRC-019','DEV-SRC-023'],'Exact numeric boundaries come from actual source-owner facts, not from README prose.'),
 ('RM-REV-03',[313,314],'Extract requires at least ten archive records before clearing the loose tree.','README.md',[25,25],['DEV-SRC-008','DEV-SRC-017'],'Legal archive and accessible target, with previous steps normal; no user confirmation/rollback promise.'),
 ('RM-REV-04',[317,317],'On normal reaching closeout, original archive backup precedes replacing archive with loader.','README.md',[26,26],['DEV-SRC-008','DEV-SRC-017','DEV-LOADER'],'Backup cannot be assumed if earlier export failed; fixed loader bytes only.'),
 ('RM-REV-05',[318,318],'Each failure stage preserves its already-written prefix; no transaction.','README.md',[25,26],['DEV-SRC-014','DEV-SRC-023'],'Current formal retains earlier-deletion/late-backup distinctions instead of making README a success guarantee.'),
 ('RM-REV-06',[322,322],'Combine accepts at most ten old records then rebuilds fresh archive content.','README.md',[27,28],['DEV-SRC-010','DEV-SRC-019'],'Old archive is gate input, not retained loader; accepted size alone does not guarantee file reads/writes succeed.'),
 ('RM-REV-07',[323,323],'Combine aggregates sorted local files before sorted recursive directories.','README.md',[19,19],['DEV-SRC-011','DEV-SRC-020'],'Separate file and directory order; no mixed sorting or global two-level recursion limit.'),
 ('RM-REV-08',[324,324],'Combine overwrites without backup and leaves loose files.','README.md',[27,28],['DEV-SRC-010','DEV-SRC-019'],'Loose files stop being direct inputs only under combined-archive consumption; no arbitrary-caller nonuse guarantee.'),
 ('RM-REV-09',[346,346],'Loader first selects matching rb files and then descends ordered nonhidden subdirectories.','README.md',[17,19],['DEV-LOADER'],'Fixed readable loader, compatible unencrypted project, accessible filesystem, prior scripts normal; no actual startup.'),
 ('RM-REV-10',[348,359],'Loader read/eval/error/log layers and pre-error side effects remain distinct.','README.md',[19,26],['DEV-LOADER'],'README short description does not imply all errors caught or successful rollback/logging.')]
write('reverse-mapping.json',{'schema':'gr8-reference-metadata-reverse/v1',
 'primary_formal_files':0,'primary_formal_clauses':0,'dependency_claims':[
 {'id':i,'formal_path':wp75,'formal_commit':B8,'formal_lines':fr,'claim':claim,
  'metadata_path':p,'metadata_lines':sr,'behavior_source_fact_ids':facts,'premise':pr,
  'disposition':'SUPPORTED_FINITE_DEPENDENCY_JOIN','source_evidence_scope':'dependency-reception.json: actual original owner facts; primary metadata read by this context'}
 for i,fr,claim,p,sr,facts,pr in reverse],
 'unsupported_finite_claims':0,'unreviewed_required_dependency_claims':0,
 'type_dispositions':['LICENSE conditional rights text is not a game rule.','.rubocop.yml is lint configuration, not Ruby host certification.','.gitignore defines patterns, not actual asset absence.','Shortcut target is not external-page evidence.','README acquisition/pull instructions and future intention are author guidance, not present functional guarantees.'],
 'no_whole_formal_acceptance':True})

interfaces=[
 {'id':'RM-IF-EXTRACT-COMBINE','producer':'README L23–30 and actual developer facts DEV-SRC-007–024',
  'consumer':'WP75 §3.2–3.3 and §12.1–12.3','received':'18 exact fact objects, their source identity/line range and normal/failed-step premises in 018 output; original full source credit remains developer reader.',
  'countercase':'An 11-record input permits extraction and rejects combine. If clear succeeds but first output open fails, no new backup or loader is implied. Ten records permit both directions.',
  'status':'FINITE_STATIC_JOIN_RECEIVED','unreceived':0},
 {'id':'RM-IF-LOADER','producer':'README L17–19/L26 plus fixed current loader DEV-LOADER',
  'consumer':'WP75 §12.4','received':'Exact fixed-loader ordering and open/read-before-eval rescue, script versus ordinary errors, ≥900 log attempt and preserved loaded prefix, with source identity and actual original reader.',
  'countercase':'Root z.rb is selected before a child directory a/ is descended. A read failure is outside local eval rescue. Earlier effects survive later failure.',
  'status':'FINITE_STATIC_JOIN_RECEIVED','unreceived':0},
 {'id':'RM-IF-TYPE-PURPOSE','producer':'All LICENSE/.rubocop.yml/.gitignore/shortcut fields and README administrative claims',
  'consumer':'R8 metadata/provenance/type inventory only','received':'Own complete text and each structural block/conditional clause; no runtime producer demanded from a nonruntime object.',
  'countercase':'An ignore entry cannot remove an already tracked asset; a lint target string cannot establish an installed runtime; a URL string cannot establish page contents.',
  'status':'OWN_COMPLETE_TYPE_DISPOSITION','unreceived':0}]
write('interfaces.json',{'schema':'gr8-reference-metadata-interfaces/v1','reviewer':REVIEWER,
 'entries':interfaces,'necessary_incoming_count':2,'necessary_incoming_received':2,
 'necessary_incoming_unreceived':0,'new_cross_domain_blockers':[],
 'root_acceptance_of_own_result':'Not self-granted; parent must actually receive this contribution.',
 'business_execution':'NOT_EXECUTED'})
write('proposals.json',{'schema':'gr8-reference-metadata-proposals/v1','reviewer':REVIEWER,
 'new_proposals':[],'required':[],'optional':[],'no_required_revision_records':[],
 'independent_policy':[],'new_limits':[],'aliases':[],'withdrawn':[],
 'counts':{'proposals':0,'required':0,'optional':0,'no_required_revision':0,'policy':0,'new_limits':0},
 'reason':'Every primary unit is either exact nonruntime metadata disposed by type/purpose or a README author-workflow claim supported, with precise premises, by already current WP75/source-owner facts. No distinct current source/spec discrepancy found in this exact scope.',
 'independent_counterproposal_status':'No finding proposed, hence no proposer self-counterreview or additional independent vote asserted.',
 'retained_qualifications':['L13: license type/purpose review does not give legal conclusions.','L03/L10/L14: loader/tool source qualification and static decode do not become Ruby/game execution.','Asset completeness must come from actual inventory and current material owners; .gitignore is insufficient.'],
 'formal_B8_PASS_granted':False,'global_review_complete':False,'UPDATE_NOT_STARTED':True})

ios=[]
for p in sorted((BASE/'read-io').glob('*.json')):
    d=json.loads(p.read_text());d['metadata_path']=str(p.relative_to(BASE));ios.append(d)
write('execution-record.json',{'schema':'gr8-reference-metadata-execution/v1','recorded_utc':NOW,
 'actual_reviewer':REVIEWER,'read_only_captured_commands':ios,
 'uncaptured_platform_transcript':[
  {'chunk_id':'aaf53e','purpose':'Initial locating search; output truncated; no semantic credit from enumeration.'},
  {'chunk_id':'fdda59','purpose':'Root AGENTS actual complete read.'},
  {'chunk_id':'55c5bd','purpose':'Actual full supplied review-SKILL read.'},
  {'chunk_id':'a0e3f4','purpose':'Full prompt lines1–80 actual read.'},
  {'chunk_id':'0e6d9e','purpose':'Full prompt lines81–160 actual read.'},
  {'chunk_id':'439927','purpose':'Full prompt lines161–241 actual read.'},
  {'chunk_id':'68343c','exit_code':1,'purpose':'Original task prompt read; mistyped readset path missing delegation component failed. Corrected by captured001; failure retained, no hidden success.'},
  {'chunk_id':'16d247','exit_code':0,'purpose':'Initial combined branch/status command output truncated; nested git rev-parse main failed because local main ref absent. Later fixed-object identity004 succeeded. Shell final code0 is not proof that every child command succeeded.'},
  {'chunk_id':'0f8dda','exit_code':0,'purpose':'Actual full four metadata files and fixed R identity; later repeated with saved raw I/O003.'},
  {'chunk_id':'a1c5a1','exit_code':0,'purpose':'Necessary formal clause and decoded-loader path locations only.'},
  {'chunk_id':'ca048b','exit_code':0,'purpose':'Inspected developer fact object structure to correct projection; final whole18 exact facts read in018.'}],
 'failed_original_launcher':'023 preserves actual old FAILED exit1, read-only app-server initialization failure; zero original semantic reading/context credit.',
 'projection_attempt':'016 returned zero records because the identity path is nested. It is an unsuccessful selection, not source absence; 018 corrected selection and all18 output objects actually read.',
 'truncation':'009/010 combined response exceeded output and part of review/WP75 was hidden. Full interface JSON was visible; no full developer review.md credit claimed. Required WP75 ranges reread fully via013/014.',
 'evidence_levels':{'source_static':'Own5 complete metadata texts and finite explicit qualified source facts.','tool_validation':'Identity/hash/enumeration/projection and output capture only.','derived_vector_executions':0,'reference_observations':0,'independent_behavior_models':0,'full_host_demo':0,'native_media':0,'real_save_replay':0},
 'business_execution':'NOT_EXECUTED','lint_execution':'NOT_EXECUTED','external_wiki_browsing':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})

first=min(d['started_utc'] for d in ios)
config={'model':'gpt-6.1-sol','effort':'ultra','tier':'default normal','speed':'normal','Fast':'off'}
actual={k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast','platform_UUID']}
write('progress.json',{'schema':'gr8-reference-metadata-completion-progress/v1',
 'logical_task':'reference_metadata_completion','original_primary':'reference_metadata',
 'actual_reviewer':REVIEWER,'platform_canonical_task_name':REVIEWER,
 'platform_UUID':'UNVERIFIED','started_utc':'2026-10-16T14:47:34.229565+00:00',
 'start_time_source':'Parent actual spawn receipt; initial true creation, not the failed old launcher.',
 'first_saved_read_io_utc':first,'updated_utc':NOW,'ended_utc':NOW,
 'status':'COMPLETED_FINITE_METADATA_REVIEW_PENDING_ROOT_RECEPTION',
 'scope':'Original reference_metadata five-R primary omission completed; no new global layer.',
 'fixed_B8':B8,'fixed_R':RC,'requested':config,'actual':actual,
 'counts':{'primary_files':5,'primary_files_full_read':5,'primary_logical_lines':742,
  'primary_bytes':31678,'primary_formal_files':0,'primary_units':len(units),
  'primary_units_reviewed':len(units),'available_primary_unread':0,'unmapped_primary_units':0,
  'necessary_incoming_interfaces':2,'necessary_incoming_interfaces_received':2,
  'necessary_incoming_interfaces_unreceived':0,'finite_reverse_claims':10,
  'finite_reverse_claims_unreviewed':0,'new_findings':0},
 'root_actual_reception':'PENDING_ROOT_ACTUAL_RECEPTION_OF_THIS_NEW_CONTRIBUTION',
 'root_decision_self_granted':False,'global_review_complete':False,
 'original_failed_launcher_preserved':True,'write_set':'tasks/reference_metadata_completion/',
 'logs':'read-io/<label>.json + .stdout + .stderr; actual platform transcript references in execution-record.json',
 'tail_example':'tail -n 20 tasks/reference_metadata_completion/progress.json (from report root)',
 'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})

report=f'''本补完已完成既有 reference_metadata 的确切 5 个参考对象审查：31,678 bytes、742 逻辑行，全部逐文件读至 EOF，全部 {len(units)} 个配置/许可/README/快捷方式结构单元已作用途处置，真实可审未读 0、未映射 0。原 primary 正式文件分母为 0；本次额外实际读取 WP75 L1–105 与 L309–360，并完成 10 条必要反向声明接合。必要 incoming 接口 2/2 已接收、未接收 0。新增 finding/proposal/required/optional/policy/limit 均为 0。结论仅限该确切范围，待 root 实际接收本新贡献；不自授全局或 B8 PASS。

实际审者 {REVIEWER} 是这次真实新上下文。原 tasks/reference_metadata 的 launcher 为 FAILED、exit 1，初始化 app-server 时只读文件系统失败，没有完整贡献或阅读信用；原文件原样保留。root 在该原目录的 root-completion 阅读是另一份实际阅读，未替代本上下文的完整审读，也未用角色改名创造审者。

固定输入 B8 {B8}、workspace tree 751dfde81048c81390f89a65ca1d1a565ba8e1ca、formal tree f292698cdd4a8e725525a9be6dc34b75faaf151e；R {RC}、tree 7589c800b61ba13a13040ed0d686979b80a84fd0。5R 字节均与固定 Git 对象相等，身份见 identities.json。报告分支是 codex/review-eighth-20261016-fd1df57-c84e；本地无 main ref，未新建或移动。报告 HEAD 是后继审计提交，未替代 B8。其他任务既有变更保持，本任务唯一写目录为 tasks/reference_metadata_completion/。

LICENSE 的 436 逻辑行分 1–160、161–320、321–436 连续实读，最后一行无 LF，所以 wc 合计 741 换行并不表示漏读；其全部定义、条件分支和末尾 CC 段落有 {len(lic)} 个连续条款单元。该文本完整按许可类型/用途处置，不判断本项目法律适用性、权利归属、兼容性或将来框架许可。许可条件不转成游戏行为、迁移要求或永久架构约束。

.rubocop.yml 全部 {len(config_keys)} 个顶层配置块、每个叶字段和说明均已读。TargetRubyVersion 3.0 是 lint 目标字段，不证明安装/运行版本；disabled cop 下的残留 style 字段不被当成启用；禁用 Eval/MarshalLoad cop 不是运行安全许可。历史实例数量是作者理由，不是本轮实测。未运行 RuboCop。

.gitignore 全 22 条模式及解释已读，README 的对应省略说明与之接合。模式与 reinclusion 只说明 Git 作者规则，既不删已 tracked 文件，也不证明某资产不存在。快捷方式全 5 行全部字段按 shell 导航处置；未访问 URL，网页内容和可用性不进入本轮证据。

README 全部当前声明已拆分：v21.1 来源、fork/另取工程/覆盖 clone/pull 指导、散文件所在位置、文件先于子目录的递归顺序、两工具方向、清树/备份/loader、合并后文件保留、Ruby 前提、未来意图与忽略概述。未来友好工具意图不是现有功能。更新指导不保证 merge 或启动成功。提取/合并/loader 的源事实精确接收自 developer 实际原 reader，见 dependency-reception.json：18 个 DEV-SRC-007–024 对象及 DEV-LOADER 的原身份、范围、前提；接收既核实际语义也保留原 reader 资格，不用 PASS 标签代替内容，不重复主张本人读了 183×2 源码全文。

普通与反例接合保留：11 节允许提取而拒绝合并，10 节两方向均可进入；清树后首输出打开失败不产生新备份/loader；正常收尾先备份后 loader；合并不备份、保留散文件；loader 每层文件排序先行，再排序递归非隐藏目录，读文件在局部求值保护外，早先副作用不整体回滚。WP75 当前 §3.2–3.3、§12.1–12.4 已保留这些前提和失败边界，因此本元资料范围未发现需要新修订的偏差。规则来源与短 README 说明分别记录，未把文档简述放大成运行保证。

请求 gpt-6.1-sol / ultra / default 普速 / Fast off。实际 model、effort、tier、speed、Fast、平台 UUID 均未回显，为 UNVERIFIED；可见 canonical task name 单列，不能认证配置。保存的真实命令、UTC、stdout/stderr 和底层 exit 在 read-io/；早期路径错误、空投影和嵌套 git 失败/截断在 execution-record.json 实名保留。静态/身份工具不计行为运行。本次提取、合并、loader、游戏/Demo、lint、原生媒体、真实存档与外部服务执行全部 NOT_EXECUTED，新业务运行 0。

交付 reading-ledger.json、identities.json、forward-mapping.json、reverse-mapping.json、interfaces.json、dependency-reception.json、proposals.json、execution-record.json、progress.json、validation.json 与 completion-manifest.json。manifest 在最后由独立终端步骤绑定完整本目录载荷，不包含自己的未来 hash，不制造递归回执。root 的实际接收与报告分支发布由 root 负责。本任务不 commit/push、不改 formal/main/R/tag、不安装、不整改、不进入第九轮或 TypeScript。UPDATE_NOT_STARTED。
'''
(BASE/'review.md').write_text(report)
print(json.dumps({'status':'ARTIFACTS_WRITTEN','primary_files':5,'logical_lines':742,
 'bytes':31678,'units':len(units),'license_units':len(lic),'rubocop_blocks':len(config_keys),
 'necessary_unreceived':0,'new_findings':0,'UPDATE_NOT_STARTED':True},ensure_ascii=False))
