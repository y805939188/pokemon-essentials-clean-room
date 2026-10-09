"""Create this review's Git/text evidence manifests; no behavior evaluation."""
import datetime
import hashlib
import json
import pathlib
import subprocess

BASE = "1d06c45cc0a744fca181ac80ee573cc9ebb9b862"
C = "8ddba850af71f24e7bd77a80b7605c456c31dc7a"
P = "9ad5539f38544fef6037356018015fe418021514"
R = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
ROOT = "review/remediation/20261003-prepare/batches/B12/"
OUT = pathlib.Path(ROOT + "candidate-review-1")
F = "deliverables/final-specification-set/"

def git(*args):
    return subprocess.check_output(["git", *args])

def read(c, p):
    return git("show", c + ":" + p)

def identity(c, p):
    b = read(c, p)
    return dict(commit=c, path=p, git_blob=git("rev-parse", c + ":" + p).decode().strip(), sha256=hashlib.sha256(b).hexdigest(), bytes=len(b))

def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")

metadata = json.loads((OUT / "metadata-verification.json").read_text())
matrix = json.loads(read(C, ROOT + "candidate-1/contribution-matrix.json"))
controls = json.loads(read(C, ROOT + "author-draft-1/qualified-control-bindings.json"))
registered = json.loads((OUT / "registration-comparison.json").read_text())

# A before/after identity comparison proves preservation, not semantic rereading.
preserved_paths = [
    "creature-rpg/wp28-item-use-and-training.md",
    "creature-rpg/wp36-wild-encounters-and-modifiers.md",
    "pokemon-rules/wp37-roaming-and-poke-radar.md",
    "combat-requirements/wp39-battle-context-and-participants.md",
    "combat-requirements/wp40-commands-obedience-and-action-order.md",
    "combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md",
    "pokemon-rules/wp46-damage-multihit-and-healing.md",
    "pokemon-rules/wp50-held-item-triggers-and-consumption.md",
    "engine-overworld/wp59-world-time-weather-field-moves.md",
    "engine-overworld/wp60-fishing.md",
    "pokemon-rules/wp60-berry-plants.md",
    "pokemon-rules/wp61-field-passive-effects-and-blackout.md",
    "pokemon-rules/wp62-pokedex-records-regions-and-content.md",
    "user-interface/wp63-pokegear-map-music-and-phone.md",
    "creature-rpg/wp64-mail-and-mystery-gift.md",
    "test-catalog/pokemon-rules-wp43-44-46-48-50.md",
    "test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md",
    "scope-statement.md",
]
preservation = []
for p in preserved_paths:
    p = F + p
    preservation.append(dict(before=identity(BASE, p), after=identity(C, p), identical=read(BASE, p) == read(C, p), proof_kind="whole-file-byte-preservation; not whole-owner semantic re-review"))
for p in ["specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md", "specs/ui/wp63-pokegear-map-music-and-phone.md", "specs/creature-rpg/wp64-mail-and-mystery-gift.md", "specs/combat/wp52-a-evaluation-coverage-and-data.md", "specs/combat/wp52-b-effect-coverage.md"]:
    preservation.append(dict(before=identity(BASE, p), after=identity(C, p), identical=read(BASE, p) == read(C, p), proof_kind="whole-file-byte-preservation"))
assert all(x["identical"] for x in preservation)
write("accepted-interface-preservation.json", dict(FIX_BASE=BASE, reviewed_commit=C, files=preservation, changed_catalog_old_rows=metadata["catalogs"], notes=["MH39–MH44 and original 139+1 identity boundary remain byte-identical.", "B15 C122 maps to WP62 §6.1 / PD31–34 and original W31–34; C109 maps to WP63 §3.1 / §8 and P33/P34. These are finding IDs, not catalog row IDs.", "Only SF35 added in the WP53–70 catalog. All old row bytes/order/multiplicity are independently retained; no acceptance inferred merely from shared file or shared 003."]))

# Explicitly record newly read source ranges; inherited author logs are separate.
sources = {
    "Data/Scripts/011_Battle/005_AI/003_AI_UseItem.rb": "1-70;81-103;101-183",
    "Data/Scripts/011_Battle/005_AI/001_Battle_AI.rb": "48-69;103-119;150-163",
    "Data/Scripts/013_Items/003_Item_BattleEffects.rb": "12-79;154-165;288-298",
    "Data/Scripts/013_Items/001_Item_Utilities.rb": "96-99",
    "Data/Scripts/011_Battle/001_Battle/006_Battle_ActionUseItem.rb": "5-23;34-59",
    "Data/Scripts/011_Battle/005_AI/010_AIBattler.rb": "56-183;260-316;425-471",
    "Data/Scripts/011_Battle/005_AI/002_AI_Switch.rb": "192-225",
    "Data/Scripts/011_Battle/005_AI/006_AI_ChooseMove_GenericEffects.rb": "30-49;329-346",
    "Data/Scripts/011_Battle/006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb": "63-109;215-248;382-405;1170-1205",
    "Data/Scripts/011_Battle/006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb": "240-249",
    "Data/Scripts/011_Battle/006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb": "91-112;857-877",
    "Data/Scripts/011_Battle/006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb": "203-250;322-334",
    "Data/Scripts/011_Battle/006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb": "324-336;1588-1602",
    "Data/Scripts/011_Battle/005_AI/005_AI_ChooseMove.rb": "23-87;232-285",
    "Data/Scripts/011_Battle/005_AI/008_AI_Utilities.rb": "125-230;867-898",
    "Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb": "26-65",
    "Data/Scripts/011_Battle/003_Move/001_Battle_Move.rb": "65-85;127-168",
    "Data/Scripts/011_Battle/003_Move/004_Move_BaseEffects.rb": "300-322; whole-file pbTarget declaration search only",
    "Data/Scripts/011_Battle/003_Move/009_MoveEffects_MultiHit.rb": "279-318; whole-file pbTarget declaration search only",
    "PBS/moves.txt": "1768-1776",
    "Data/Scripts/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb": "211-218;247-278",
    "Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb": "170-205;299-327;356-409",
    "Data/Scripts/018_Alternate battle modes/002_BugContest.rb": "171-196;350-404",
    "Data/Scripts/012_Overworld/001_Overworld.rb": "197-218;637-650",
    "Data/Scripts/003_Game processing/005_Event_Handlers.rb": "97-140;148-191",
}
source_reads = [dict(input=identity(R, p), ranges=ranges, kind="bounded static text/caller inspection; no Ruby execution") for p, ranges in sources.items()]
project_reads = [dict(input=identity(C, "AGENTS.md"), scope="whole repository instruction file"), dict(input=identity(C, "handoff/cloud-dot-20261009/original-contract.md"), scope="whole public original contract")]
for p in ["B12-downstream-contract.json", "README.md", "affected-interface-map.json", "author-dispatch.json", "author-dispatch.md", "catalog-locks.json", "independent-review-requirements.json", "input-identities.json", "original-and-acceptance-controls.json", "source-limits.json"]:
    project_reads.append(dict(input=identity(P, ROOT + "refreeze-after-B15-C-1/" + p), scope="contract, identity, navigation; complete nine logical controls where applicable"))
for p in ["README.md", "catalog-preservation.json", "cross-input-report.json", "metadata-checks.json", "original-scope-proposal.json", "qualified-control-bindings.json", "reading-log.json", "registration-collection-comparison.json", "sanitization-audit-map.json", "scope-amendment-1.json", "source-reading-log.json"]:
    project_reads.append(dict(input=identity(C, ROOT + "author-draft-1/" + p), scope="author evidence scrutinized; large repeated arrays independently compared as metadata, not adopted as verdict"))
for p in ["README.md", "affected-interface-proposals.json", "configuration.json", "contribution-matrix.json", "formal-output-identities.json", "independent-review-dispatch.md", "independent-review-request.json", "metadata-checks.json", "original-output-identities.json", "public-registration-proposals.json", "source-limits.json"]:
    project_reads.append(dict(input=identity(C, ROOT + "candidate-1/" + p), scope="candidate dispatch/claims/limits; independent conclusion recorded in this report"))
for x in metadata["outputs"]:
    project_reads.append(dict(input=x["output"], scope="changed clause semantic review, original/final/appendix/catalog synchronization; full identity verified"))
reused = [dict(id=x["id"], original=x["whole_original_object_binding"], acceptance=x["whole_approved_acceptance_binding"], scope="exact whole logical object and complete current qualified fields; no recursive reopening of raw historical report tree") for x in controls["contributions"]]
write("reading-log.json", dict(role="R-B12-FULL-CANDIDATE-1", reviewed_commit=C, reviewed_tree=metadata["reviewed_tree"], FIX_BASE=BASE, reference_commit=R, reference_tree=git("rev-parse", R + "^{tree}").decode().strip(), project_reads=project_reads, reference_static_reads=source_reads, exact_control_reuse=reused, inherited_author_read_log_identity_checks=metadata["reading_log_identities"], inherited_author_source_identity_checks=metadata["source_identities"], reading_distinctions=["57 author reading-log entries were independently identity checked; this does not claim 57 new whole-file semantic reviews.", "19 author source entries were identity checked. Newly inspected reviewer ranges are independently listed above.", "Full unfiltered 43-file binary diff is stored. Formal/original changes and evidence claims were semantically reviewed; large duplicated control/registration arrays were exhaustively compared by new metadata programs.", "One broad local locator search for C109/C122 produced historical-report search hits; those hits were not used as quality verdicts or recursively opened. Accepted text and direct source limits at exact FIX_BASE are the preservation basis.", "Source body text was viewed through git show only. Reference object fetch is not source execution or reference modification.", "No applicable B12 local skill found in .agents/skills; AGENTS.md and exact dispatch govern this review."], reference_programs_executed=0, historical_author_reviewer_programs_executed=0, extra_tasks_spawned=0))

limits_candidate = json.loads(read(C, ROOT + "candidate-1/source-limits.json"))
limits_paths = ["review/remediation/20261003-prepare/batches/B09/candidate-2/source-limits.json", "review/remediation/20261003-prepare/batches/B15/acceptance-stage-1/source-limits.json"]
write("source-limits.json", dict(role="R-B12-FULL-CANDIDATE-1", reviewed_commit=C, inherited_candidate_limits_identity=identity(C, ROOT + "candidate-1/source-limits.json"), inherited_candidate_limits=limits_candidate, direct_exact_accepted_limits=[dict(input=identity(BASE, p), preserved_contents=json.loads(read(BASE, p))) for p in limits_paths], own_scope="Bounded static reference source/caller and specification review plus self-written Git/JSON/hash/text bookkeeping. This is new semantic review, not runtime confirmation.", retained_limits=["U01–U10", "G01–G12", "AX01–AX20"], named_unread=limits_candidate["named_unread_preserved"], conditional_67_berry_rows_retained=True, nonlocal_shared_findings_and_other_batches_remain_open=True, unlisted_source_paths_and_ranges_not_semantically_reviewed=True, reference_execution=0, Ruby_execution=0, game_execution=0, compiler_execution=0, converter_execution=0, generator_execution=0, deserializer_execution=0, historical_author_reviewer_program_execution=0, behavior_vectors_executed=0, runtime_observations=0, proven_Demo_chains=0, own_metadata_program_execution_only=["verify_metadata.py", "compare_registrations.py", "write_review_evidence.py"]))
write("configuration.json", dict(role="R-B12-FULL-CANDIDATE-1", source_thread_id="01a10d94-84b9-759e-aa1d-edb0d9b6d0e2", requested=dict(model="gpt-6.1-sol", reasoning_effort="ultra", service_tier="default", speed="Standard"), admission=dict(source="Selected cloud delegation explicitly requests gpt-6.1-sol/ultra/Standard and this assigned task is running.", status="UNVERIFIED_NO_AUDIT", trusted_effective_parameter_echo="NOT_AVAILABLE", no_backend_parameter_certification=True), effective=dict(model="UNVERIFIED", reasoning_effort="UNVERIFIED", service_tier="UNVERIFIED", speed="UNVERIFIED"), approved_Plan_A="Successful requested task admission may proceed; absent trusted echo is disclosed UNVERIFIED and is not itself a blocker. Explicit unsupported/downgrade evidence would need handling.", explicit_unsupported_or_downgrade_evidence=None, deliberate_model_or_effort_substitution=False, CLI_or_native_runtime_substitution=False, extra_tasks_spawned=0, quota_probes=0, credential_or_permission_probes=0))

judgments = {
    "003": ("A§6/B§1+B附表§1/2.4/C§5.1 remove designated source line/history anchors; preserve family identities, final counter split and missing-source defaults.", "CE/C59 permits different representations with identical observations; adding duplicate scores or cross-family dynamic aliases fails equivalence.", "HandlerHash text and exact original tables support consecutive-use overwrite, RemoveProtections +7 preservation and Parting Shot stat-drop preservation. Other 003/B16/B21 duties remain open."),
    "A046": ("WP51 AI estimate1 is separate from WP28 active floor(H/4) and WP50 held gates.", "AI/I08: H101/105,h1 active25/26=>HP26/27; AI estimate remains1; misspelled SITURUSBERRY does not match.", "WP28/WP50 byte-identical; no rewrite of accepted recovery or canonical A046."),
    "B017": ("AI Pain Split ratio is not clamped; accepted WP46 integer average/ordered HP writes/item checks receive the execution obligation.", "BE/B63: U51/60,T150/200=>60/100; AI ratio100.5/51. HealBlock permits effect; substitute is separate earlier rejection.", "B28 unchanged; WP46 MH39–44 and 139+1 identities byte-identical; B10 primary remains accepted without cross-batch closure."),
    "B020": ("Scan complete Items list; generic+CanUse checks precede classification with nil selected index, firstAction false, AI context, messages false. Exception leaves entire selection; ordinary reporter permits later phases.", "AI/I06/I07: POTION,ETHER produces no UseItem/no consumption; removing ETHER registers POTION and consumes once. MAXETHER/activeLEPPA same exception; generic refusal avoids dependent queries.", "POKEFLUTE/dolls/balls battle-context dependencies retained; WP28 manual selection/WP50 heldLEPPA distinct; reporter/plugin/facility exceptions not generalized."),
    "B021": ("Independent integer/minimum1 per component before signed aggregation; weather and ability qualification, BigRoot/Heatproof order, Wish saved value, Perish direct999999 all retained.", "AI/S08: H11,h9 rainDish+Curse gives1, gates4/2 false at skill32; clearCurse -1. AE/G13 H11,h2 d1<h; removeRainDish d2>=h. S09 covers root/burn/Wish0/Perish alternatives.", "No HP writes or final action inference; high-skill extra switch gates and WP42 real round order retained."),
    "B022": ("All A334/B270/C167 occurrence tuples checked against original family+identity+copy source; B literal269 plus one explicit overwrite provenance, not two effective scores. A AbilityRanking20add+5copy=25.", "BE/B61 Assurance target +8, distinct Revenge overall; B02b independent OHKOIce ice refusal/nonice ordinary gate. CE/C56 HelpingHand overall100,target+5; C57 Imprison User candidate100/direct target108, not116.", "Removed false Morpeko/grassy-heal direct entries while retaining copies. Original correct A/B/C identity rows and algorithms preserved; 786/783/782 and 57/839 scopes kept distinct from conditional67berries."),
    "B023": ("Default GEOMANCY PBS User =>num_targets0 =>whole failure/whole score; target two-turn/stat preference not invoked. Local target handlers remain in their families.", "BE/B62 XERNEAS55 H203 legal fixture HP203/50 x noItem/PowerHerb gives four candidate100; all3+6=>20; partial cap100.", "No execution/HP/stat/herb writes or final selection claim. Exact original patch2 quality agrees with source callers and target/class data."),
    "B024": ("Gems base6; comparator is MECHANICS_GENERATION<=5, not base score. 18 gem type mappings and direct-key precedence retained, both raw controls covered.", "CE/C58 medium FIREGEM+usableEMBER yields8 at5 and6 at8; without usable matching fire damage yields0 at both. Fling/Acrobatics/external direct key excluded explicitly.", "Actual WP50 boost/consumption/pledge exception unchanged. Original patches3/4 agree; proposal4 label correction §3=>§4 changes no patch content."),
    "B026": ("Contest starts by shortening player party, not clearing partner; step double-candidate choice precedes public one-enemy+can_override gate and normal partner preparation.", "SF35 valid active20/K, NaturalPark BugContest, partner, forceSingle false=>ordinary2v2/no contest budget transfer or retained overwrite/no single-wild-end; victory partner healing. No partner or forceSingle true=>single takeover if override/unhandled; override false=>no takeover.", "B08 forceSingle/Safari/partner/member precedence, SF01–34, timer pre-expiry and budget/store/notification boundaries preserved. Demo/event composition remains U01."),
}
rows = []
for x in matrix["contributions"]:
    key = x["id"].removeprefix("GIR-FD82-")
    minimum, contrast, boundary = judgments[key]
    bound = next(y for y in controls["contributions"] if y["id"] == x["id"])
    rows.append(dict(id=x["id"], primary=x["primary"], primary_owner=x["primary_owner"], verdict="PASS_SCOPED", exact_control_metadata=next(y for y in metadata["controls"] if y["id"] == x["id"]), whole_original_object_sha256=bound["whole_original_object_sha256"], whole_acceptance_object_sha256=bound["whole_acceptance_object_sha256"], clauses=x["clauses"], static_designs=x["designs"], minimum_review=minimum, legal_counterexample_and_reverse_review=contrast, consumer_and_retained_boundary_review=boundary, original_scope_quality_review="exact parent-approved patch independently checked" if x["primary"] and key != "B022" else "correct original extraction preserved", original_final_appendix_catalog_trace_agreement=True, current_qualified_scope_and_acceptance_minimum_met=True, behavior_vectors_executed=0, canonical_state="OPEN", blocking_findings=[]))
write("review.json", dict(role="R-B12-FULL-CANDIDATE-1", verdict="PASS_SCOPED", reviewed_commit=C, reviewed_tree=metadata["reviewed_tree"], FIX_BASE=BASE, contribution_count=len(rows), primary_count=sum(x["primary"] for x in rows), contributions=rows, blocking_findings=[], minimal_author_fix_scope=[], approval_scope="Exact B12 candidate FULL nine local contributions/six primaries only.", required_affected_candidate_roles=["B07", "B08", "B10", "B11"], other_role_receipts_signed=False, actual_review=False, A_REG_G=False, A_REG_C=False, main_merge=False, canonical_closed=False, generated_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))

proposal = json.loads(read(C, ROOT + "candidate-1/affected-interface-proposals.json"))
potential_key = next(k for k,v in proposal.items() if isinstance(v,list) and v and isinstance(v[0],dict) and "owner" in v[0])
routing = {
    "B02": (False, "Only shared WP53–70 reader overlap: sole new row SF35 belongs to B12; all 157 previous row bytes/order/multiplicity retained. No changed B02 clause/caller/data/condition identified."),
    "B03": (False, "Same complete old-row preservation; C109 receiving WP63/P33/P34 byte-identical. SF35 adds no B03 resource/parser contract."),
    "B04": (False, "003 designated locators removed while behavioral final binding/defaults preserved; source layout is not a receiving behavior obligation. No B04 caller/sanitization semantic interface changed; all old shared catalog rows retained."),
    "B07": (True, "WP28 active SITRUS floor(H/4) and manually selected PP index vs WP51 AI estimate and nil-index list exception/no-consumption. Review changed originals plus formal boundary at exact candidate."),
    "B08": (True, "WP36 forceSingle/Safari/partner/member precedence and step two-candidate caller vs WP53 public cardinality/can_override and WP37 handled/wild-end. Check normal partner vs contest budget/store/notification chain."),
    "B09": (False, "WP39/40/42 receiving texts byte-identical. Updated residual value is explicitly AI approximation; no actual end-of-round writes/order, command/resource contracts or final source binding/default behavior changed."),
    "B10": (True, "Accepted WP46 PainSplit integer average/ordered writes/item checks vs WP52 AI ratio, and loaded actual OHKOIce clause vs independent AI ice failure. Protect 139+1 and MH39–44 exact old rows."),
    "B11": (True, "WP50 held LEPPA/SITRUS and gem execution vs WP51 active nil-index/estimate and WP52 gem preference; protect every accepted AB row in shared combat catalog, same bytes/order/multiplicity."),
    "B14": (False, "WP59/60/61 receiving files byte-identical; SF35 explicitly normal return before contest expiry, preserving timer and blackout gates. Complete old SF/BP/FP rows retained; no changed time/step lifecycle identified."),
    "B15": (False, "WP62/63/64 originals and finals byte-identical. C122 nil vs empty labels/PD31–34/W31–34, and C109 final-selected query/P33/P34 retained exactly. Changed catalog adds SF35 only, no new Pokédex/mail/map-query behavior."),
}
routes = []
for x in proposal[potential_key]:
    required, reason = routing[x["owner"]]
    inputs = []
    for b in x["potential_navigation_inputs"]:
        got = identity(b["commit"], b["path"])
        assert all(got[k] == b[k] for k in ["git_blob", "sha256", "bytes"])
        inputs.append(dict(frozen_navigation_input=got, candidate_input=identity(C,b["path"])))
    routes.append(dict(owner=x["owner"], FULL_routing="REQUIRED_BOUNDED_AFFECTED_REVIEW" if required else "NO_REAL_INTERFACE_CHANGE_IDENTIFIED_BY_FULL", rationale=reason, exact_navigation_inputs=inputs, owner_candidate_receipt=None, owner_actual_receipt=None, no_owner_receipt_signed=True))
assert set(x["owner"] for x in routes) == set(routing)
write("affected-routing.json", dict(role="R-B12-FULL-CANDIDATE-1", reviewed_commit=C, FIX_BASE=BASE, purpose="FULL independent interface determination/routing only; not a substitute for any affected owner receipt.", potential_count=len(routes), required_affected_candidate_count=4, routes=routes, exact_actual_version_requires_new_determination=True, B16="After B12 candidate/required affected/G/actual/C, parent must refreeze five changed formal readers and actual changed original/caller inputs; no B16 review or acceptance signed.", B13_B21_and_canonical_shared_controls_remain_open=True))
print("Wrote review manifests: 9 contributions / 6 primaries, 10 affected routes, 25 bounded source identities; all 23 preserved files byte-identical.")
