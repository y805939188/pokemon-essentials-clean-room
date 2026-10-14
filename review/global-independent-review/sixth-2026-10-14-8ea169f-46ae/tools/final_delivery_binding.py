"""External finite binding of the handoff; this receipt does not claim its own future commit."""
import argparse,datetime,json,pathlib,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1];REPO=ROOT.parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--handoff',required=True);ap.add_argument('--readback',required=True);a=ap.parse_args()
receipt=json.loads((ROOT/'publication'/a.readback/'readback.json').read_text())
assert receipt['commit']==a.handoff and receipt['all_full_bytes_match']
names=['cloud-sixth-update-handoff-prompt.md','cloud-sixth-update-handoff-manifest.json',
       'final-report.md','summary.md','handoff/batch-assignment.json','handoff/dependency-graph.json','handoff/file-conflict-graph.json']
entries={x['path']:x for x in receipt['entries']};rel=str(ROOT.relative_to(REPO))
selected=[entries[rel+'/'+p] for p in names]
manual=[x for x in receipt['entries'] if x['path'].startswith(rel+'/handoff/entries/')];assert len(manual)==28
manifest_bytes=subprocess.check_output(['git','show',a.handoff+':'+rel+'/cloud-sixth-update-handoff-manifest.json'],cwd=REPO)
manifest=json.loads(manifest_bytes)
out={'schema':'r6.final-delivery-binding.v1','recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'fixed_main':manifest['fixed_project_inputs']['main'],'fixed_workspace_tree':manifest['fixed_project_inputs']['workspace_tree'],
 'fixed_formal_tree':manifest['fixed_project_inputs']['formal_tree'],'fixed_R_commit':manifest['fixed_project_inputs']['reference_commit'],
 'fixed_R_tree':manifest['fixed_project_inputs']['reference_tree'],'delivery_tag':manifest['fixed_project_inputs']['delivery_tag'],
 'r6_core':manifest['r6_core'],'r6_report_publication':manifest['r6_report_publication'],
 'handoff_commit':a.handoff,'handoff_workspace_tree':receipt['workspace_tree'],'handoff_report_directory_tree':receipt['report_directory_tree'],
 'selected_payload_identities':selected,'manual_author_reviewer_prompt_identities':manual,
 'full_handoff_package_remote_readback':{'files':receipt['files'],'bytes':receipt['bytes'],'all_full_bytes_match':True,
   'source':'publication/'+a.readback+'/readback.json','entries':receipt['entries']},
 'counts':{'required':56,'P2':39,'P3':17,'optional':8,'no_required_revision':1,'optional_float_facet':1,'policy':7,'limits':14,
   'source_available_unreviewed':0,'formal_unread':0,'formal_unmapped':0,'reference':432,'formal':131,'formal_finite_blocks':20379,
   'first_wave_independent_candidate_batches':14,'prospective_formal_paths':54,'file_conflict_pairs':24},
 'finite_identity_rule':'This external receipt binds existing handoff objects. Its own final publication commit/tree and final readback are bound by the final chat; no recursive self hash or further mandatory administrative commits.',
 'strict_write_boundary_incident':'INC-R6-001 retained; current protection clean does not erase historical outside-dir creation',
 'update_started':False,'status':'UPDATE_NOT_STARTED'}
(ROOT/'publication/final-delivery-binding.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k in ['handoff_commit','handoff_workspace_tree','handoff_report_directory_tree','counts','status']},ensure_ascii=False))
