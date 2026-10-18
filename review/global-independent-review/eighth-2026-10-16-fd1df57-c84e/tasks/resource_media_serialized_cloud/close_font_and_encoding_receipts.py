"""Freeze actual content receptions; validate byte bindings, never execute target data."""
from pathlib import Path
import json
import hashlib
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parent
FONT = BASE.parent / "media_font_programs"
NOW = datetime.now(timezone.utc).isoformat()


def read_json(path):
    return json.loads(path.read_text())


def identity(path):
    raw = path.read_bytes()
    return {"path": str(path), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def save(name, value):
    path = BASE / name
    assert not path.exists(), path
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    return identity(path)


contribution = read_json(FONT / "contribution.json")
binding = read_json(FONT / "delivery-binding.json")
assert identity(FONT / "contribution.json")["sha256"] == "18eed98701921e2fe898810de569cc022dc48bab435f14425627d8119277aae1"
assert identity(FONT / "delivery-binding.json")["sha256"] == "8d6146a043fb018903a652c2fa14971f1e933efbad87a6aa50f229af1cd1461b"
assert len(contribution["full_owned_unit_identities"]) == 13
assert len({x["id"] for x in contribution["function_stack_interfaces"]}) == 71
assert len(contribution["function_stack_interfaces"]) == 72  # F49 has two actual branches.
assert len(contribution["complete_function_call_edges"]) == 10
assert len(contribution["complete_local_reverse_facets"]["local_facets"]) == 7
assert (FONT / "facts.md").read_text() == contribution["complete_factbody"]
assert sum(x["bytes"] for x in binding["files"]) == binding["payload_bytes"] == 29432326
assert len(binding["files"]) == binding["file_count"] == 261
for record in binding["files"]:
    actual = identity(Path(record["path"]))
    assert actual == record, actual["path"]
    assert Path(record["path"]).parent == FONT

game = Path("/workspace/pokemon-essentials/Game.exe").read_bytes()
assert len(game) == 14732288
assert hashlib.sha256(game).hexdigest() == "5c75e92fcbb6ec50b9f8fc61913d751a8945d6a1fc69c3017c7b8686b532bf04"
start, end = contribution["source_font_span"]
assert hashlib.sha256(game[start:end]).hexdigest() == contribution["source_font_sha256"]
for table in contribution["full_owned_unit_identities"]:
    raw = game[table["start"]:table["end"]]
    assert len(raw) == table["bytes"]
    assert hashlib.sha256(raw).hexdigest() == table["sha256"]

program = read_json(FONT / "program-ledger.json")
structure = read_json(FONT / "structure-ledger.json")
assert program["program_count"] == len(program["all_programs"]) == 2349
assert program["program_bytes"] == 121793 and program["opcode_count"] == 52297
assert structure["glyph_count"] == len(structure["glyphs"]) == 2587
assert len(structure["tables"]) == 13 and len(structure["raw_layout_structures"]) == 168

font_receipt = {
    "schema": "gr8-actual-font-contribution-reception/v1",
    "utc": NOW,
    "receiver": "/root/resource_media_serialized_cloud",
    "actual_original_reader": "/root/media_font_programs",
    "status": "ACTUAL_COMPLETE_CONTRIBUTION_CONTENT_RECEIVED_WITH_ALL_PREMISES_AND_EXCLUSIONS",
    "immutable_inputs": [identity(FONT / x) for x in ["contribution.json", "delivery-binding.json", "facts.md", "identities.json", "reading-ledger.json", "review.md"]],
    "actual_content_read": [
        "Entire 69073B contribution, with its complete 21784B fact body, all 13 table identities, all 72 branch-specific interfaces for 71 definitions, all 10 call-edge objects, all glyph call totals, all 13 forward objects, all 7 reverse facets, all 4 interfaces, all 5 parent receipts, full negative rationale, payload identities and metadata gaps.",
        "Entire 76153B delivery-binding object: complete administrative fields and all 261 path/bytes/SHA objects, read in bounded nontruncated groups. Whole identities.json, reading-ledger.json and review.md also actually read.",
        "Initial single 69073B cat output was platform-truncated; subsequent complete key groups and separate whole factbody output supply every omitted object. Truncated initial output alone is not used to grant reception.",
    ],
    "source_credit": "Original 13-table/program/rule FULL belongs to actual child reader. Parent receives complete contributed facts and common premises, not a second self-FULL read of all 29MB raw artifacts, and not a second independent vote.",
    "complete_received_contribution": contribution,
    "complete_received_original_identity_objects": read_json(FONT / "identities.json"),
    "complete_received_reader_attestation": read_json(FONT / "reading-ledger.json"),
    "binding_verification": {"all_files": 261, "all_bytes": 29432326, "stable": True, "source_font_and_13_table_bytes_equal": True, "machine_check_semantic_credit": 0},
    "independent_receiver_counterreview": [
        {"topic": "computed CALL", "countercheck": "F17's clamped fixed-point arithmetic yields only44..47; no blanket unbounded-dynamic-call exemption. Host rounding/projection input remains unknown."},
        {"topic": "stack branch", "countercheck": "Retain F49's8→0/5→0 branches; 72 interface rows are71 definitions, not72 functions. No materialized glyph/prep/function caller ofF49, and no contrary fixed formal claim, so no formal defect manufactured."},
        {"topic": "numeric vs control", "countercheck": "All65761 push entries have exact roles and consumer PCs. Geometry/point/CVT values have whole-range type/use; functionIDs/ppem/DELTA/loop/storage/zone/rounding controls require actual values and are explicitly included in original reader's whole evidence."},
        {"topic": "layout", "countercheck": "All GSUB6/GPOS26 lookups and GDEF/kern rules are received. Raw168 coverage/class structures are part of actual reader's source scope. Preserve null anchors, class/feature/flag selection, Hebrew input order and separate duplicate-valued kern/GPOS tables; no host shaping/dual application inferred."},
        {"topic": "19-table envelope", "countercheck": "Child13 plus parent's6 distinct tables equals19; parent's whole header/directory/name/post/cmap/gaps package closes physical envelope. This is coverage, not another vote or semantic proof by checksum."},
        {"topic": "native", "countercheck": "Three whole native contributions retain parent original3208-instruction credit. Concrete face loading and71 source FDEFs are different layers; activeclass/SFNT service/installedcallbacks/VM CFG remain named OPEN."},
        {"topic": "formal", "countercheck": "WP17 requests/candidate fallback/font stacks and explicitly bounded fixture do not promise pixel parity, selected embeddedfont or full OpenType feature execution. No contradiction established by newly read font programs; finite required/optional/policy0 does not adjudicate whole-domain NO_REQUIRED_UPDATE."},
    ],
    "readable_owned_font_structures_remaining": 0,
    "native_OPEN": contribution["proposal_dispositions"]["limits"][0],
    "host_NOT_EXECUTED": contribution["proposal_dispositions"]["limits"][1],
    "full_native_graph_received": False,
    "whole_global_PASS": False,
    "new_formal_defects": [],
    "business": "NOT_EXECUTED",
    "update": "UPDATE_NOT_STARTED",
}
font_result = save("font-programs-layout-reception.json", font_receipt)

encoding = read_json(BASE / "serialized-encoding-closure-structure.json")
encoding_receipt = {
    "schema": "gr8-complete-serialized-encoding-contribution/v1",
    "utc": NOW,
    "source_full_reader": "/root/resource_media_serialized_cloud",
    "B8": contribution["B8"],
    "R": contribution["R"],
    "scope": "Entire encoding wrappers, symbol and symbol-link metadata for both current safely parsed serialized artifacts; every source byte already belongs to original13R denominator.",
    "actual_full_structure": encoding,
    "complete_source_facts": [
        {"id": "ENC01", "fact": "messages_core.dat all21216 I wrappers enclose one raw String with exactly one ivar E=>true. One literal symbol:E defines index0; all21215 subsequent ; references resolve to that same E. No extra ivar keys, values, wrapped types or symbol definitions exist in the complete85150-node parse."},
        {"id": "ENC02", "fact": "Every one of21216 current raw message strings is valid UTF-8. This is whole current byte-domain validation, separate from the previously completed full10697 pair/body read and all178 original object-link relationships."},
        {"id": "ENC03", "fact": "Scripts.rxdata entire11-node parse has two I-wrapped raw Strings, title and compressed source; each has the same single E=>true annotation. The title is valid UTF-8. The compressed561B payload is not valid UTF-8, despite the annotation. Preserve original compressed bytes; zlib decoding and complete49-line Main read were previously completed safely."},
        {"id": "ENC04", "fact": "Encoding annotations are metadata, not byte validation or execution. Do not transcode/repair compressed data, infer successful host Marshal loading, or run Main. No other class/user-defined/hook/deserialization tag is present in either entire parsed current artifact."},
    ],
    "consumer_join": "Kernel's actual complete Intl message lookup normalizes lookup keys separately from stored bodies, and Main consumers request existing decoded strings/bytes. This source structure does not change current/default language separation, whitespace preservation, or actual host Ruby object freezing/encoding acceptance; those remain bounded by previously received consumer packets and NOT_EXECUTED.",
    "failure_and_partial": "Inert parser rejects unsupported tags and checks complete byte consumption; it constructs JSON metadata and raw byte views, never Ruby objects or hooks. All-current valid UTF8 assertion applies only to message strings and title, not compressed stream. A malformed/other serialized input is outside these exact byte identities; no generic rollback/recovery is inferred.",
    "formal_disposition": "No new formal defect. Complete encoding metadata supplements whole serialized structure; it cannot alone prove successful host execution, entire Intl/PBS/compiled data behavior or NO_REQUIRED_UPDATE.",
    "evidence": [identity(BASE / n) for n in ["serialized_encoding_closure.py", "serialized-encoding-closure-structure.json", "serialized-encoding-closure.execution.json"]],
    "complete_execution_metadata": read_json(BASE / "serialized-encoding-closure.execution.json"),
    "generation_semantic_credit": 0,
    "target_execution": "NOT_EXECUTED",
    "update": "UPDATE_NOT_STARTED",
}
encoding_result = save("serialized-encoding-closure-contribution.json", encoding_receipt)
print(json.dumps({"utc": NOW, "font_reception": font_result, "encoding_contribution": encoding_result, "machine_check_semantic_credit": 0, "business": "NOT_EXECUTED", "update": "UPDATE_NOT_STARTED"}, ensure_ascii=False, indent=2))
