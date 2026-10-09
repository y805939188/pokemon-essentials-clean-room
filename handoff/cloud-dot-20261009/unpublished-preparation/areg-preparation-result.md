> Archived REGISTRATION_PREPARATION_TEMPLATE_NOT_APPROVAL. This is input, not approval or authority. Local reader/duplicate-proof rules are nonbinding for cloud takeover.

Private AREG-G preparation handoff — `RUN_ID20261003-prepare`. Preparation only; no repository, index or ref writes, children, other sessions/messages, reference execution or behavioral verification performed. Configuration: `gpt-6.1-sol / xhigh / default Standard`; effective backend **UNVERIFIED**, approved Plan A.

Prefixes below are repository-relative: `F = deliverables/final-specification-set/`, `P = review/remediation/20261003-prepare/`, `B = P/batches/B14/`.

**1. Incoming frozen material and provenance**

Use accepted B09 `1e6b11a47370f1c7c4659a32443fc1afda597bac` and PLAN `41fffb540c6483f5296ea0d33b789b75180d27ed`.

The supplied C2 token beginning `2af39…` has 41 characters. Both frozen C3 records identify C2 as **`af39efbf32549be964cb083bd49bed6d1d5c0d2a`**, tree `932ffac11a2701ddb432516e7bd07aa990fd326f`. Preserve this discrepancy explicitly.

C2’s 12 formal paths, found through frozen Git trees/diff inventory, are:

```text
specs/overworld/wp16-world-rendering-and-visual-transitions.md
specs/overworld/wp59-world-time-weather-field-moves.md
specs/overworld/wp60-fishing.md
specs/pokemon-rules/wp60-berry-plants.md
specs/pokemon-rules/wp61-field-passive-effects-and-blackout.md
F/engine-overworld/wp16-world-rendering-and-visual-transitions.md
F/engine-overworld/wp59-world-time-weather-field-moves.md
F/engine-overworld/wp60-fishing.md
F/pokemon-rules/wp60-berry-plants.md
F/pokemon-rules/wp61-field-passive-effects-and-blackout.md
F/test-catalog/engine-overworld-wp11-15-59-60.md
F/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md
```

C3 authorizes changes within three existing paths, adding no formal path. Proposal `c0dc3037f6aafd736915af1d0bd920455012b30a`; authorization `9503a85a122bf760f747d2b26718d3fee295bef2`.

| Document | C2 blob → authorized intended blob | Intended SHA256; bytes |
|---|---|---|
| Original WP59; §3.5 suffix | `35fec86286c104c7a4c7f4e7af5558afdd9fc65b` → `d604af4c40f6925370f4488067f6bbd30ecd2b3e` | `4a414ffb5f75422753da7f936cf3b404af25476cbb513cf9a2ac3551d4bc8f76`; 55347 |
| Final WP59; §3.5 suffix and §9 navigation | `32ff5e6573df3565fb8159a198b5cce582f844d0` → `a2bda5c3e0d5b967d8ef050bc36b4cac8ed8c420` | `7fb2c3b2cd87128267fabfcd212adab3dd3f250643458e7b8527a3205d636e7c`; 44766 |
| Engine catalog; §I heading and WT41–44 append | `54041886ccec35d2ff7316dd8a86b8c78c8e1990` → `168d674f8477c53cb5ba14740319b346735cc3ed` | `4d9770a871b6118cdc89414e6f1df3689f52aa60ddd42ec98e0f21315dab4e5c`; 80758 |

These are **intended identities**, not an applied C3 candidate. Authorization records `formal_applied=false`, `new_candidate_commit=null`.

The known minimal incoming evidence inventory is the 34 C2 additions:

| Directory beneath `B` | Exact contents |
|---|---|
| `author-stage-1/` | `B09-reread-assessment.md`, `input-refreeze.json`, `original-application.json` |
| `scope-proposal-1/` | `README.md`, `scope-manifest.json`, `scope-validation.json`, `source-evidence.json`; four `original-patches/specs__…md.patch` files corresponding to original WP59, fishing, berry and WP61 |
| `candidate-1/` | `AREG-proposals.json`, `README.md`, `changed-paths.json`, `contributions.json`, `downstream-handshake.json`, `reverse-impact-packages.json`, `source-limits.json`, `source-reading-log.json`, `validation.json` |
| `candidate-2/` | `amendment-application.json`, `bounded-amendment-1.json`, `fix-response.json`, `fix-response.md`, `original-FLY-amendment.patch`, `revised-identities.json`, `source-reading-log.json`, `staged-validation.json`, `validation.json`; `amendments/01-B14-B04-R1-01.patch`, `02-B14-B04-R1-01.patch`, `03-R-B14-1-001.patch`, `04-R-B14-1-001.patch`, `05-R-B14-1-001.patch` |

Also preserve C3’s eight `candidate-3/scope-proposal-1/` files—three named patches, `scope-manifest.json`, `scope-request.md`, `source-reading-log.json`, `static-designs.json`, `validation.json`—and `candidate-3/scope-authorization-1.json`. Add the later frozen application/freeze package and complete required report packages from their supplied manifests; their paths/SHAs are not available yet.

Keep scope checkpoint `b37533ef1cfc7808ed41d64215647a78d165ada4`, C1 `47f7514765f8569ae9172bb06a2cd615e2b83b8a`, failed affected-B09 report `93b81d1e05b16b7f5c999e472620b8cc4d9c5d02`, full C2 report `18716a3e3e9200a98bedc1375d9e71cdae59adfa`, and fresh B08 report `016ec3ff80f001fc2bc64e968bdcff021d3ab331` as distinct historical objects. **No C2 PASS transfers to C3 or actual integration.**

Reference provenance remains logical `reference/pokemon-essentials/`, commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`, tree `7589c800b61ba13a13040ed0d686979b80a84fd0`. Carry exact existing source-log bindings and reading limits; do not import reference source, serialized data, media or copied source expressions.

**2. Public registration boundary**

The established G public-write set is exactly:

```text
audit/source-traceability.md
F/README.md
F/scope-statement.md
F/test-catalog/README.md
planning/coverage.md
planning/feature-matrix.md
P/historical-errata.md
P/final-integration-review.md
P/approval-ledger.tsv
P/traceability-successor.tsv
```

Use necessary B14 successor text and append records. Preserve all 170 existing approval and traceability rows, historical sections, dated manifests, old hashes, reports and snapshots. Shared finding IDs require separate B14 records; identify the batch inside the obligations data. Do not overwrite an earlier batch’s row by `finding_id`.

Approval columns, unchanged and in order:

```text
finding_id, canonical_state, candidate_commit, candidate_reviewer,
candidate_review_commit, candidate_verdict, accepted_contribution_kind,
public_registration_verdict, integration_verdict, downstream_gate,
reviewed_integration_commit, integration_review_commit,
integration_reviewer, integration_disposition, remaining_obligations
```

Traceability columns:

```text
finding_id, canonical_state, original_report_commit, effective_priority,
candidate_commit, candidate_review_commit, accepted_candidate_contribution,
current_clause_inputs, static_test_ids_not_executed,
public_successor_application, remaining_batches, remaining_obligations,
integration_gate
```

Refresh only necessary current navigation. The catalog README’s affected `条目` cells may reflect confirmed current WT/FS/BP/FP ranges; preserve unrelated columns and owner rows. Preserve historical Feature Matrix rows and their approvals; add scoped B14 registration context without expanding confidence or coverage.

A new batch-local `B/integration-stage-1/current-hashes.tsv` uses:

```text
path, git_blob, sha256, bytes, binding
```

It describes that G freeze’s bytes, not acceptance or semantic coverage. The existing B09-G table is immutable: its approval and central-handoff hashes precede B09-C’s two public updates. At accepted B09, the current blobs are respectively `0f04bf3f3015bb18d51129709a57faf30f0ca361` and `07a2354cd15353de42766a0350d9f4409b3f9738`.

Do not edit approved PLAN controls, canonical `finding-ledger.tsv`, historical approval snapshots or other root registries.

**3. Register 24 contributions as pending actual**

Register 19 primary IDs: `GIR-FD82-C086–C089`, `C091–C095`, `C097–C106`. Register five local shared contributions: `GIR-FD82-002`, `003`, `C003`, `C007`, `WP80-INTAKE-R01`.

Each new record must bind the exact passed C3 candidate and reports, accepted predecessor, current formal/row identities, source provenance, scope/application evidence, original/acceptance object locators and hashes, complete current controls, minimum gates, contributor obligations and actual-review status.

Apply C2’s six traceability overlays and C3’s bounded successor. Recalculate clause/row coordinates: C1 fishing locators become stale after later WT additions. C3’s observation remains contextual to C007/003, adding no root or approved extension.

G status is **`INTEGRATED_PENDING_ACTUAL`**:

- B14 accepted contributions: **0**; parent C not performed.
- Public records after a clean append: **194 = 170 accepted + 24 pending**.
- Accepted statistics remain **9/21 batches, 170 records, 142 touched IDs, 109 unique primary IDs**.
- Specific minimum: **109 satisfied / 0 missing / 0 insufficient**.
- Strict all-contribution classification within those 109 accepted primaries: **100 satisfied / 9 pending**.
- Canonical findings: **229 OPEN / 0 CLOSED**.

Do not add 19 candidate primaries, static row counts, observations or coauthor contributions to accepted denominators. The five B14 primaries already touched by accepted coauthors—C093/C094/C095/C103/C106—remain distinct from accepted B14 primary work.

**4. Refreeze readers and prepare eight actual requests**

Refresh the complete 72-read contract, current public inputs, 12 formal identities and additional affected readers. Preserve explicit historical bindings for the two global-report paths; do not substitute current-tree copies. Refreeze both whole catalogs and owner interfaces.

Once actually applied and frozen, the authorized C3 catalog shape would be engine 361 plus Pokémon 148 = 509 rows. Its requirement is preservation of all **505 C2 row bytes/order/multiplicity**, plus WT41–44; confirm against the supplied C3 freeze rather than treating the proposal as proof.

Prepare full R-B14 plus seven separate affected actual packages:

| Reviewer | Bounded required interface |
|---|---|
| Full R-B14 | All 24 contributions/19 primaries, 12 formal paths, current controls, public registration and complete integration differences |
| B02 | Both shared catalogs; C003 cache/test premises and untouched owner rows |
| B03 | Connected-weather postwrite 20, movement/waterfall completion, FLY repair, preserved map/event/dungeon rows |
| B04 | WP16 splash amendment, weather/resource/fade/location interfaces, cave presentation and preserved supplements |
| B06 | WP61 soot erasure, collection cap/statistics, notification multiplicity and engine-catalog reader |
| B07 | Shared catalogs, poison/daily infected-member conditions and protected owner rows |
| B08 | WP33–37 producer/caller interfaces, encounter ordering, berry settlement/rounding, ordinary/forced step distinctions |
| B09 | WP38–42 interfaces; fresh full WP39/WP40 consumption, C3 tint/battle-time correction, fishing/return/end-state boundaries and both accepted report corrections |

Every package needs the same exact actual commit/tree/parents, exact passed C3 receipt bindings, current reader identities, relevant complete controls, positive/reverse static designs and full unfiltered accepted-predecessor→actual and C3-candidate→actual differences. Equal blobs or prior PASS labels do not discharge these gates. A supported `NOT_AFFECTED` disposition must come from the separate exact comparison; the writer cannot certify it.

Future reviewer requests remain `gpt-6.1-sol / Ultra / default Standard`, effective **UNVERIFIED** under Plan A. One G writer; total active author/reviewer tasks at most three. This preparation dispatches none.

B10 formal work remains blocked until B14-C, followed by refreezing **all 53 reads/eight writes** and its dependency contract. Later WP46 changes retain conditional separate affected B14 candidate and actual review.

**5. Successor errata**

Append bounded explanations; never rewrite historical reports:

- **Fishing 15→16:** `review/wp80-delivery-2026-10-03/batch-03/clause-disposition.md`, historical lines 131–133, incorrectly claimed 15/15 equivalence. The original had 16 scenarios; the final body retained valid-start behavior but the catalog omitted its separate scenario. FS16 restores it. FS17–18 are additional B14 contrasts; current fishing has 18 rows, not 16.
- **B09-G-O01/B013:** under the complete participating-partner/full-party/normal-receive fixture, one terminal restoration traversal gives **boxed A=Y, live B=empty**. No later shifted-player traversal restores B. Link accepted `report-corrections-successor.json`.
- **R-B08-ACT-OBS01/005:** ordinary NearAlly entry requires **live user0**, fainted near2/no reserve and live far4. Selection/USE registers4; unchanged-state normal target resolution rejects far4. No final effect, PP or message conclusion; self0/B033 remains separate.

Retain original IDs and provenance for C2 FLY, berry timestamp and WP16 splash observations, plus C3 `B14-AFFECTED-B09-001`. Preserve the distinction between B14-introduced incomplete FLY premises and retained prior berry/splash/cross-reference residue. These are not additional canonical repairs.

**6. Exact actual freeze and child policy**

After all required C3 candidate gates pass, the future authorized writer should integrate exact formal/evidence bytes, record merges/conflicts, append bounded public registration, and freeze the resulting public-integrated actual.

Record complete changed-path identities and unfiltered diffs using fixed endpoints, with `--no-ext-diff --no-textconv --no-renames --binary`; no path filter for the complete comparisons.

B09’s historical freeze specifically used a single-parent evidence-only child adding exactly:

```text
upstream-to-payload-identities.json
candidate-to-payload-identities.json
diff-and-freeze.json
```

The inspected B14 contract does **not itself mandate that layout**. Use it only if the future G authorization explicitly requires it. If required, record the exact payload parent and enumerated additions, preserve every payload formal/public/reader byte, and include payload→actual comparison. Otherwise do not invent a mandatory child.

Supply final actual SHA/tree externally through the authorized publication/readback process. Never embed a commit’s own SHA or a recursive self/validation hash. Any changed reviewed formal byte requires a successor candidate and applicable gates. G provides no actual PASS or C acceptance.

**7. Semantic-read audit**

All document reads used frozen Git objects. Broad truncated displays were followed by bounded field rereads; parsing/hashing was not counted as semantic reading.

| Frozen material | Semantic selectors/ranges consumed |
|---|---|
| Accepted B09 `AGENTS.md` | Lines 1–297 |
| PLAN stage-b/cross-chain/B14 | Complete lines 1–49 / 1–24 / 1–33 |
| B09-C `acceptance-manifest.json` | Metadata lines 2–178, 1079–1163, 1229–1427; normative/output identity arrays inspected separately |
| B09-C B14 contract | Metadata/gates/limits/interfaces; all 24 current control projections at lines 1533–6879, including roots, extensions and minimum fields |
| B09-C statistics | All `/rows/0..108`, `/touched_ID_rows/0..141`, `/accepted_contribution_receipts/0..169`, basis variants, transitions, pending lists and denominator definitions; relational projections plus complete identity map |
| B09-G records | Manifest public/schema/freeze policies; registration schema and sample disposition; current-reader binding/affected-gate fields; complete 18-row current-hashes table |
| C2 B14 package | AREG proposals 1–381; contributions 1–2728 through complete field projections/provenance maps; reverse-impact nonduplicated fields; changed paths; full revised identities 1–305 and fix-response 1–360; amendment/application records |
| C3 authorization/proposal | Authorization 1–125; scope request and all three complete document patches, including WT41–44 premises/results; proposal identity/preservation fields |
| Reports | Full failed B09 report; full C2 gate metadata; fresh B08 manifest and report lines 1–18; relevant scoped/limit passages of accepted B02/B03/B04/B06/B07 reports referenced by the contract |
| Public Markdown/TSVs | Current B09 prefixes, central C prefix, affected catalog-index and F14 feature rows; exact TSV headers and representative current/historical G rows |

Important exact anchors:

- B14 contract SHA256: `a60a1c7f57937d5f299d57c7c16b13558c03b032e54f6545892f106f1667e9bd`.
- Current statistics SHA256: `8a710f89ea329edbb2c67edbd8b50efcd02701a621f4ee793ed3796adb1f1518`.
- C3 authorization SHA256: `b138c342340b48920797103e5eaed4464082bdf2db7f4fd94acc415ca97a75bc`.

Deduplication used exact selectors: each minimum field matched its corresponding current-control field; all 20 effective-case projections matched root-adjudication fields by `raw_id`. Canonical JSON hashes used UTF-8, sorted keys, `ensure_ascii=false`, compact separators. Example C007 effective projection hash: `8276bf0f137e4016a9c806da2318379b37da135dfb4f372f088731383ef0a158`.

**Unexpanded/unread:** underlying historical bodies behind identity catalogues and prior-statistics hashes; unrelated global finding history; B09-G’s complete 20 disposition bodies and unrelated reader-body semantics; all 1,870 validation assertions; complete source-log bodies and source implementation; full formal bodies outside inspected patch/context material. These are not claimed reviewed by this preparation.

**8. Bounded uncertainties and preserved limits**

The applied C3 candidate SHA, application record, successor report SHAs and exact C3 gate results are pending external delivery. The intended three identities cannot substitute for them. Future incoming inventories and actual diff totals must be derived from those freezes.

Historical chronology/cross-container leases and backend effectiveness remain unverified; add no certification gate. Preserve U01–U10, G01–G12, AX01–AX20 and every named limitation: binary/serialized data, actual maps/events, media/fonts/audio, host/executables/DLLs/mkxp/capacity, plugins/dynamic/deprecated/EventScene/shadow reachability, backups/gen, eight cup-list references, Pokémon metrics samples, unlisted ranges and real Demo chains.

Runtime observations **0**; proven Demo chains **0**; behavior vectors **unexecuted**. C007’s complete 67-berry table remains conditional on an explicit full-content compatibility commitment. This handoff makes no future PASS, acceptance, closure or formal change.