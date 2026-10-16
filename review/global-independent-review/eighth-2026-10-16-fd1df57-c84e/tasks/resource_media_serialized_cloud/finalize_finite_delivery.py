"""Freeze this finite review, validating identities without executing reviewed assets."""
from pathlib import Path
from datetime import datetime, timezone
import json
import hashlib
import subprocess

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
RROOT = Path("/workspace/pokemon-essentials")
NOW = datetime.now(timezone.utc).isoformat()


def load(path):
    return json.loads(path.read_text())


def put(name, value):
    (BASE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def ident(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(BASE)), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def git_bytes(root, *args):
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True)
    assert result.returncode == 0, result.stderr.decode()
    return result.stdout


proposal = load(BASE / "proposals.json")
proposal["zero_is_not_no_required_update"] = "Complete finite media content reviewed; named L04native source CFG/selection OPEN and L08host NOT_EXECUTED; global final reception belongs root."
proposal["optional_formal_count"] = 0
proposal["policy_formal_count"] = 0
proposal["finite_material_content_complete"] = True
proposal["root_global_final_granted"] = False
put("proposals.json", proposal)

failures = load(BASE / "ordinary-tool-failure-notes.json")
failures["failures"].append({"operation": "review.md rewrite patch used delete/add for same path and was rejected by patch validation", "exit": "TOOL_VALIDATION_FAILURE", "exact_utc": "UNVERIFIED", "effect": "no mutation; later single complete file write succeeded", "approval_rejection": False})
failures["recorded_utc"] = NOW
put("ordinary-tool-failure-notes.json", failures)

identities = load(BASE / "identities.json")
reading = load(BASE / "reading-ledger.json")
structures = load(BASE / "full-structure-and-program-ledger.json")
counter = load(BASE / "counterreview.json")
assert len(identities["primary"]) == len(reading["primary"]) == len(structures["primary"]) == 13
assert len(structures["new16_units"]) == 16
assert len(counter["records"]) == 5
assert all(len(x["eight_section_counterreview"]) == 8 for x in counter["records"])
assert not counter["new_formal_required_defects"]
assert reading["primary_file_denominator"] == 13 and reading["logical_extra_units"] == 16
assert reading["embedded_font_19table_current"]["readable_owned_tables_unread"] == 0
assert reading["native_current_total"]["units_or_windows"] == 45
assert reading["native_current_total"]["instruction_rows"] == 4860
assert git_bytes(RROOT, "rev-parse", identities["R"] + "^{tree}").decode().strip() == "7589c800b61ba13a13040ed0d686979b80a84fd0"
project = Path("/workspace/pokemon-essentials-clean-room")
assert git_bytes(project, "rev-parse", identities["B8"] + ":deliverables/final-specification-set").decode().strip() == "f292698cdd4a8e725525a9be6dc34b75faaf151e"
source_results = []
for row in identities["primary"]:
    path = RROOT / row["path"]
    relative_source = path.relative_to(RROOT).as_posix()
    data = path.read_bytes()
    frozen = git_bytes(RROOT, "cat-file", "blob", identities["R"] + ":" + relative_source)
    assert data == frozen
    assert len(data) == row["bytes"]
    assert hashlib.sha256(data).hexdigest() == row["sha256"]
    assert hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() == row["blob"]
    source_results.append({"path": row["path"], "bytes": len(data), "fixed_R_byte_equal": True, "sha256_equal": True, "blob_equal": True})

checkpoint = load(BASE / "current-delivery-checkpoint.json")
for row in checkpoint["packages"]:
    assert ident(BASE / row["path"]) == row
for path in BASE.rglob("*.json"):
    load(path)  # JSON only; no target deserialization or executable import.

required = ["progress.json", "identities.json", "reading-ledger.json", "forward-mapping.json", "reverse-mapping.json", "interfaces.json", "proposals.json", "review.md"]
validation = {"schema": "gr8-media-final-finite-validation/v1", "utc": NOW, "base8": [ident(BASE / n) for n in required], "all13_current_equals_fixed_R": source_results, "formal_tree_equal": True, "primary_file_denominator": 13, "additional_logical_units": 16, "five_proposals_all8sections_present": True, "frozen_current_packages_verified": len(checkpoint["packages"]), "native_units_or_windows": 45, "native_instruction_rows": 4860, "HRTF_partial_window_included": 33, "font_readable_tables_remaining": 0, "font_original_readers": {"child": 13, "parent": 6}, "checks_semantic_credit": 0, "business": "NOT_EXECUTED", "update": "UPDATE_NOT_STARTED", "global_final_granted": False}
put("finite-validation.json", validation)

excluded = {"finite-payload-binding.json", "finite-final-manifest.json", "finite-finalization.execution.json", "finite-finalization.stdout", "finite-finalization.stderr"}
files = [ident(p) for p in sorted(BASE.rglob("*")) if p.is_file() and str(p.relative_to(BASE)) not in excluded]
binding = {"schema": "gr8-media-finite-payload-binding/v1", "utc": NOW, "owner": "/root/resource_media_serialized_cloud", "files": files, "file_count": len(files), "payload_bytes": sum(x["bytes"] for x in files), "excluded_from_self_binding": sorted(excluded), "exclusion_reason": "Binding cannot hash itself; final manifest binds this complete binding and is externally identified in handoff; wrapper streams/exit/UTC are written only after finalizer returns.", "business": "NOT_EXECUTED", "update": "UPDATE_NOT_STARTED"}
put("finite-payload-binding.json", binding)

material_units = []
for row in structures["new16_units"]:
    material_units.append({k: row[k] for k in ["id", "source", "kind", "start", "end_exclusive", "bytes", "sha256", "records", "ordered_patterns", "unique_names", "pointer_table_start", "pointer_table_end", "pointer_table_sha256"] if k in row})
manifest = {
    "schema": "gr8-media-final-finite-manifest/v1",
    "utc": NOW,
    "owner": "/root/resource_media_serialized_cloud",
    "status": "FINITE_CONTENT_REVIEW_COMPLETE_AWAITING_ACTUAL_ROOT_CONTENT_RECEPTION",
    "B8": identities["B8"], "formal_tree": "f292698cdd4a8e725525a9be6dc34b75faaf151e", "R": identities["R"], "R_tree": "7589c800b61ba13a13040ed0d686979b80a84fd0",
    "base8": [ident(BASE / n) for n in required],
    "complete_payload_binding": ident(BASE / "finite-payload-binding.json"),
    "bound_file_count": len(files), "bound_payload_bytes": binding["payload_bytes"],
    "validation": ident(BASE / "finite-validation.json"),
    "primary_complete_source_units": identities["primary"],
    "new16_complete_material_units": material_units,
    "whole_primary_semantic_dispositions": [
        "8TTF/104tables/2326glyph complete static structure/names/cmap and fullrange geometry/metric type-use; no fpgm/prep/cvt and allglyphinstructionlength0.",
        "2BMP all128pixels plus whole TownMap consumer andmkxpconfig.",
        "Scripts complete inert11nodes andunique49line Main read; allencodingmetadata, compressedbytes preserved despiteEtrue/invalidUTF8.",
        "messages complete85150nodes/31buckets/85hashes/10697wholepairs/21216strings/all178links; allEtrue UTF8metadata andall5bodywhitespace differences retained.",
        "SF2 completeRIFF/INFO/hydra25786records/236presets/240instruments/1463zones/505samples/allPCM2000710s16 type-use; nativebackendandhearing separate.",
    ],
    "whole_new_material_semantic_dispositions": [
        "12DXBC entire194SHDR+218Aon9instructions/metadata,2wholecreationfunctions.",
        "4401glyphdict mappings/wholetrie structuretype-use/wholelookup; originalcase/aliases/control/PUA mapping retained.",
        "257controller rawrecords/119orderedpatterns/209names/21targets,4initialwholefunctions+wholefileloader/platformwrappers; gameactionbridge unknown.",
        "HRTF completeMinPHR03header/828IR/26496s24coefficients/828delay type-use. Exactnative33instructionwindow only, wholecontaining15143Bfunction notread.",
        "Embeddedfont all19tablebodies andwhole350200B envelope; actualchild13 tables/2587glyphs/2349programs/52297instructions/71defs/alllayout received throughcomplete69073Bcontribution; parent6metadatatables originalFULL. Source readers and second-vote prohibition preserved.",
    ],
    "counterreview": {"path": "counterreview.json", "proposals": 5, "complete_sections_each": 8, "source_post_count_assertion_rejected": "2298 notaccepted; independentcompletepost evidence2333; originalproposalbytesunchanged; noformalrequireddefect", "new_required": 0, "new_optional": 0, "new_policy": 0},
    "native_known_scope": reading["native_current_total"],
    "named_source_OPEN_L04": [
        "activefontclassregistration/selection;SFNTservice+08/+10;installedcallbacks69ace0/69ad40/6997a0/69b0c0/69e1e0;glyphloader/VMlowerCFG",
        "SF2backend/default/clamp/synthesis;HRTFsurroundingfunction/downstreamparse;shaderchecksum/Aon9header/outerselector",
        "controllerlowerI/O/stringprimitives/GUIDdevice→gamebridge;glyphdictionarycallers",
    ],
    "host_UNKNOWN_L08": "Alltarget Font.exist/text_size/hinting/features/charmap/raster/UI/GPU/device/audio/hearing NOT_EXECUTED. These do not exempt readablemedia/programs, all of which are now disposed in finite scope.",
    "complete_shared_consumers": ["Kernel12+15producers+4common+Traineridentity", "UI25initial+36text+7dex24facts", "World11limitedunits", "Core4facts+completePrioritymethod+2actualaudioCallerCorrectionmethods/wholeoldpayloadmanifest"],
    "own_additional_consumers": "8wholeGameData1784lines/9facts;3wholeaudio/path/System1049lines/5facts;TownMap419lines;mkxp159lines",
    "source_credit": "OriginalsourceFULLstaysactualnamedreader; complete contributedfactbody/premises received without secondselfFULL/vote. No oldhistoryPASS or wholeunadoptedsourcecredit inherited.",
    "contribution_packages": checkpoint["packages"],
    "ordinary_IO_qualification": "Controlledrunsretainrawstdout/stderr/exit/actualUTC. Ordinaryunwrappedreadingsonlyplatformstreams; missingper-commandUTC/truncation/EOFmetadata UNVERIFIED. Noallprivatepublicreadbackclaim; failures notbackdated.",
    "immutable_history": "Originaltwo0STARTcontractsunchanged; separateactualfontACTUAL1routeandreceipt. messagescontractactual0, parentfullbodyread. Earlierfrozencontributions retainhistoricOPEN; currentlive8+manifest narrowthem.",
    "requested": identities["requested"], "actual": identities["actual"],
    "approval_rejections": [],
    "global_final_granted": False,
    "business": "NOT_EXECUTED", "update": "UPDATE_NOT_STARTED",
    "public_git": "rootownscommit/push/readback; this context neitherperformed norclaimedpublication",
}
put("finite-final-manifest.json", manifest)
print(json.dumps({"utc": NOW, "manifest": ident(BASE / "finite-final-manifest.json"), "binding": ident(BASE / "finite-payload-binding.json"), "validation": ident(BASE / "finite-validation.json"), "bound_files": len(files), "bound_bytes": binding["payload_bytes"], "business": "NOT_EXECUTED", "update": "UPDATE_NOT_STARTED", "global_final_granted": False}, indent=2))
