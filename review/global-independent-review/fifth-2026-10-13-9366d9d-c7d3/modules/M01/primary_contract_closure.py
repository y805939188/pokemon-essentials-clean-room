"""Manual source-to-current-contract decisions. No reference/model execution."""
import review_state as s
import review_ops as o
F='deliverables/final-specification-set/'
P={
 '02':F+'generic-kernel/wp02-rule-configuration-and-data-variants.md',
 '03':F+'generic-kernel/wp03-content-identity-and-schema.md',
 '04':F+'generic-kernel/wp04-pbs-lifecycle.md',
 '08':F+'generic-kernel/wp08-localization.md',
}
def locate(prefix):
    if prefix in P:return P[prefix]
    candidates=list((s.ROOT/F).glob('*/wp'+prefix+'-*.md'))
    assert len(candidates)==1,(prefix,candidates)
    P[prefix]=str(candidates[0].relative_to(s.ROOT));return P[prefix]

# A partial capability is a completed comparison exposing bounded contract detail
# that remains absent/ambiguous. It is NOT an unread source or a claimed full pass.
decisions={
 'M01-LZ-COLLECT':('partial',[('08','§6.1'),('04','§7')], 'Collection sources, map/shared buckets and partial timeout mutation are explicit. Exact textual literal recognizer, event continuation normalization at final flush, and archive/file traversal gates remain finer than the contract. All actual18 corpora and their producer links were separately reviewed; dynamic event/plugin reachability is unavailable.'),
 'M01-LZ-ESCAPE':('partial',[('08','§6.2–6.3.1')], 'Listed control substitutions and whitespace/hash loss are supported. The conditional bracket-escaping gate and literal marker collision are not fully specified by the general exchange table; all actual records were checked without executing a round trip.'),
 'M01-LZ-EXPORT':('partial',[('08','§6.2–6.2.1')], 'Overwrite/deletion, array-vs-hash format and sparse-event precheck match. Default-only entry enumeration, skipping empty originals and ignoring language-only keys remain part of candidate002, rather than being inferred from runtime fallback.'),
 'M01-LZ-IMPORT':('supported',[('08','§6.3–6.4')], 'Preprocessing, numeric-prefix/constant/Map identity, first-content shape discrimination, arity, same-domain merge and truncate-before-parse match the active reader and writer. Mixed-shape outcomes are only certified for the explicitly described static branches, not general serializer compatibility.'),
 'M01-LZ-KEY':('partial',[('08','§3.2; §6.3.2')], 'GR5-M01-003: current text does not distinguish line-edge normalization order from whole-string trimming. Actual Controls key/value and all corpus keys were inspected; no runtime execution.'),
 'M01-LZ-LOAD':('partial',[('08','§4; §5.2; §7')], 'Immediate/delayed language loading, pair reset and outer-array validation match. Lazy default-pair caching and failure/retry timing remain more specific than the prose. Core/game defaults are not runtime lookup fallback.'),
 'M01-LZ-DEFAULT-BUILD':('partial',[('08','§2; §6.1–6.2')], 'GR5-M01-002: current default-message purpose does not define set-vs-add or core suppression by equal index value versus existing hash key. Corpus inspection supplies actual data context, not substitute algorithm evidence.'),
 'M01-LZ-LOOKUP':('supported',[('08','§5.1–5.2')], 'Array/hash/map lookup precedence, valid empty-string hit, original-text fallback and malformed-inner-data propagation match. All public wrappers were inspected.'),
 'M01-LZ-PRIVATE':('partial',[('08','§4; §6.1–6.2')], 'Alias-only navigation entry for loading/default building; no independent capability counted. Detailed decisions belong to M01-LZ-LOAD and M01-LZ-DEFAULT-BUILD.'),
 'M01-LZ-DOMAINS':('supported',[('08','§3.1–3.2')], 'All31 identities0–30 and real hash/array/map consumers match. Eighteen supplied nonempty core domains are a content snapshot, not the complete domain directory.'),
 'M01-LZ-INTERPOLATE':('supported',[('08','§5.2–5.3; §8')], 'Replacement argument semantics, ordered substitution, missing arguments and formatting outside rescue match. All actual formatted templates/argument sites were checked; historical execution was not reused.'),
 'M01-DIAGNOSTIC':('supported',[('04','§6')], 'Current filename/section/key/line position context and error attachment match; actual host presentation and exception-report failure are outside this static projection.'),
 'M01-CSV-QUOTE':('supported',[('04','§4.2; §5.5')], 'Comma/quote-triggered wrapping, explicit forced wrapping, empty value and lack of hash protection match the current writer/reparse boundary. Not a lossless general CSV claim.'),
 'M01-PBS-SECTIONS':('partial',[('04','§4.2')], 'BOM/blank/comment processing, ordinary overwrite and repeated-property accumulation match. Empty-section suppression and numeric-section wrapper restrictions are not all explicit; these are completed source comparisons, not unexamined parser branches.'),
 'M01-TRANSLATION-SECTIONS':('supported',[('08','§6.3')], 'Column-zero comment test before stripping, interior hash retention, empty-section skipping and header recognition are explicit and agree.'),
 'M01-LINE-READERS':('supported',[('04','§4.2'),('76','§8.4')], 'Active preprocessed sections and the facility raw-line input are distinguished; adjacent unused reader behavior is audit-only. Facility semicolon parsing and tolerant references are covered by the specialized contract.'),
 'M01-CSV-SPLIT':('supported',[('04','§4.2')], 'Odd-quote joining and position-sensitive backslash-quote stripping, including exhausted joining and last-field retention, match. All actual quoted facility values preserve their outer ordinary quotes; no malformed-data runtime test claimed.'),
 'M01-CSV-LEGACY-SCALARS':('supported',[('04','§2; §4.2')], 'Unused scalar helpers were read and explicitly excluded from the active format contract; no extra active capability inferred.'),
 'M01-CSV-CAST':('partial',[('03','§5.1'),('04','§4.2')], 'Signed/nonnegative/positive/name/symbol distinctions match. GR5-M01-001 records the float recognizer boundary. Boolean aliases and hex textual spelling also have more detail than generic type names; no assumption that a host default parser is equivalent.'),
 'M01-CSV-ENUM':('partial',[('03','§5.1–5.2'),('04','§4.2')], 'Registered references and undefined-value rejection match. Ordered-list first-index, hash-valued enumerations and legacy constant-module branches have source-specific compatibility details not fully stated in the summary; inline trainer-gender aliases are recorded per field.'),
 'M01-CSV-LEGACY-RECORD':('supported',[('04','§4.2')], 'Unused old record evaluators are not counted as current accepted grammar.'),
 'M01-CSV-RECORD':('partial',[('03','§5.1'),('04','§4.2')], 'Optional uppercase, repeated groups, raw q termination and scalar-vs-array results match. Fixed-schema surplus-tail ignoring and the mandatory first evaluation of a repeated group are not specified by saying fixed-length tuple/list.'),
 'M01-CSV-WRITE':('partial',[('04','§5.5')], 'Generic formatting and non-lossless round trip are correct. Internal nil slots versus omitted trailing optional slots, enum output forms and repeated grouping are not completely defined; per-field export omissions remain separately recorded.'),
 'M01-PARSE-CONTENT':('partial',[('03','§3; §5.2'),('76','§8.4')], 'Facility tolerant references and current-profile STICK/VICEGRIP fallback are covered. Legacy normalization/Nidoran aliases and unused parser branches remain audit-specific details, not implied aliases for current content identities.'),
 'M01-PBS-MIGRATE':('supported',[('04','§5.2')], 'Both fixed-path textual renames, write-only-on-change and discovery-vs-fixed-file failure boundary match.'),
 'M01-PBS-DISCOVER-SCHEDULE':('supported',[('02','§6.1–6.2'),('04','§4.1; §4.3')], 'Root-only longest-base discovery, backups excluded,22 scheduled families and specialized fixed facility list agree. Full73 paths and ten referenced facility children are independently mapped.'),
 'M01-PBS-COMPILE-ALL':('supported',[('04','§3; §5; §6; §7')], 'Ordered compilation and terminal text/event/animation integrations are reviewed as orchestration boundaries; all necessary direct calls read. No complete map-conversion algorithm certification implied.'),
 'M01-PBS-TRIGGER-FAIL':('supported',[('04','§3; §6')], 'Debug-only gate, integer-second max freshness, import999 exclusion, pre-delete attempts, Reset/SystemExit bypass, Hangup conversion and early-unbuilt-list exception boundary match.'),
 'M01-PBS-GENERIC':('supported',[('03','§4.2; §5.2'),('04','§4.2')], 'Optional missing-all return precedes clear; identity/unknown field/repeated property/validation/register/save/message order agrees, including phone default-key exception.'),
 'M01-PBS-TOWN':('supported',[('63','§3'),('08','§3.1'),('04','§4.2')], 'Repeated points and independent region/location/description text collections match the current map contract and generic data lifecycle. Every actual point and optional switch field was reviewed.'),
 'M01-PBS-CONNECTION':('partial',[('11','§3'),('04','§5.5')], 'Valid directional/opposed and numeric connection forms match all19 actual rows. Mixed first-numeric/second-directional inputs and asymmetric missing-endpoint diagnostics are finer than current valid-input contract; map assets are unavailable.'),
 'M01-PBS-TYPE':('supported',[('43','§3–4'),('03','§5.1–5.2')], 'Separate dedup and final forward reference checks agree with the type-list contract. All generation memberships and optional Shadow type were reviewed; weakness-before-resistance-before-immunity precedence remains in the registry rule.'),
 'M01-PBS-ABILITY':('supported',[('03','§5; §7'),('08','§3.1–3.2'),('35','§4')], 'Generic registration and two hash text domains match; every actual ability record links to this data contract. FasterEggHatching has its separately inspected consumer; other ability effects are outside M01 data certification.'),
 'M01-PBS-MOVE':('partial',[('43','§2–3'),('03','§4.3; §5'),('04','§4.2')], 'Category/power fields and text linkage are supported. Status-with-power rejection versus damaging-with-zero warning/downgrade is not fully specified by the field catalog; effect factory fallback is a separate shared observation.'),
 'M01-PBS-ITEM-BERRY':('supported',[('27','§2–3'),('60-berry','§2–3'),('03','§5.1'),('04','§4.3')], 'Item references and independent BerryPlant symbol identity match; reversed berry yield normalization and data defaults compared against the full plant contract. No inferred compiler Item foreign key.'),
 'M01-PBS-SPECIES':('partial',[('18','§3.2; §4'),('31','§3'),('04','§4.2; §5.5')], 'All actual records, typed references and evolution edges reviewed. Explicit generic six-column order and restricted float input remain candidates004/001. Deferred references, generated predecessors and per-field constraints are separately described in the audit field ledger.'),
 'M01-PBS-FORMS':('partial',[('18','§3.1–3.2'),('22-transformation','§1'),('04','§5.5')], 'Base/form identities and meaningful inheritance are covered, including all48 mega rows. Empty move/evolution list inheritance and the all-three-held-item fallback condition have greater specificity than the general inheritance wording; same scalar candidates as base species apply.'),
 'M01-PBS-METRICS-SHADOW':('supported',[('03','§3.2; §4.2–4.4'),('04','§5.5'),('23-shadow-data','all131 data rows')], 'Compound zero/base identity, optional Shadow absence, metric query-created records and export path decisions agree with current contracts and full actual data.'),
 'M01-PBS-DEX':('partial',[('03','§5.2'),('62','§3'),('04','§5.5')], 'Unique section/member rules and all151/256 actual membership/order match. Sparse positive dex IDs can fail the final unguarded iteration; current runtime missing-table fallback does not specify compiler sparse-section behavior.'),
 'M01-PBS-RIBBON':('supported',[('03','§5; §7'),('08','§3.1–3.2')], 'Generic field constraints and name/description localization match; all actual ribbon records are data projection, not full contest/award workflow certification.'),
 'M01-PBS-ENCOUNTER':('supported',[('03','§3.2; §5.2'),('04','§4.4'),('36','§3')], 'Dedicated permissive header/chance conversion, strict slot positive values, duplicate section rejection, duplicate slot merge and repeated-method replacement match the detailed current exception table and all actual profile records.'),
 'M01-PBS-TRAINER':('partial',[('03','§3.2; §5.2'),('18','§4.3'),('24','§5'),('73-a','§3.5')], 'Identity overwrite and member validation/duplicate-move removal are covered. Six-column input remains004; absent-member final overlays remain006. Dedicated unknown-line skipping and complete numeric/ball validation retain bounded audit detail.'),
 'M01-PBS-FACILITY':('supported',[('02','§6.1'),('76','§8.4'),('55','§2.5'),('57','§2')], 'Fixed list, all13 actual files, optional missing child files, tolerant identity handling and translated speeches are explicitly handed off. Repeated pool indices remain weighted positions, not deduplicated species; source failures and nonatomic writes retain the named specialized boundaries.'),
 'M01-PBS-METADATA':('partial',[('03','§3.2'),('24','§3'),('61','blackout return destination'),('04','§4.2')], 'Global/player schema selection, duplicate checks, required global0/player1/Home and localized storage author were analyzed. Runtime identity/Home use is supported; the generic validation prose does not enumerate all specialized compile-time required-record checks. Initial currency copying is distinct from setter clamping.'),
 'M01-PBS-MAP-DUNGEON':('partial',[('11','§3'),('14','§3; §5; §8'),('04','§4.2')], 'Actual69 maps and both dungeon configurations match the field and consumer ledger. Missing MapInfos name fallback, absent tile arrays and empty tileset registry failures are not all covered by the general fallback wording; not inferred from valid samples.'),
 'M01-PBS-PHONE':('supported',[('03','§3.2; §5.2'),('04','§4.2'),('63','§4–5')], 'Default normalized string identity versus contact triple, repeated message categories, whole-record default overwrite and final ten-category collection match; default duplicate counterevidence is explicit in current primary contracts.'),
 'M01-PBS-ANIMATION':('partial',[('04','§5.4'),('74','§15')], 'Move/OppMove validation and load-failure empty collection match. The change flag means at least one recognized mapping added to a newly built table, not comparison with the old saved mapping; wording remains ambiguous.'),
 'M01-WRITE-GENERIC':('supported',[('03','§3.1'),('04','§5.5')], 'Suffix-driven path selection, BOM/section/property output and no cleanup/lossless promise agree; specialized field omissions are recorded separately.'),
 'M01-WRITE-CONNECTION':('partial',[('11','§3'),('04','§5.5')], 'Skipping deleted maps and equivalent connection output match. Direction normalization precedence and pair swap/negation are finer than the summarized output contract; all19 actual data relationships reviewed, absent map geometry unverified.'),
 'M01-WRITE-SPECIES':('partial',[('04','§5.5'),('18','§3.1–3.2'),('73-a','§2; §6')], 'Base/form suffix grouping and singular evolution write mutation versus plural editor read are explicit. Full individual getter suppression/inheritance conditions remain partial; source fields were all read.'),
 'M01-WRITE-METRICS':('supported',[('04','§5.5'),('73-b','metric editor save boundary')], 'Nonzero-form suffix path selection, matching-form omission and query-before-save path effects match the current dedicated table.'),
 'M01-WRITE-DEX-RIBBON':('partial',[('62','§3'),('04','§5.5')], 'Actual membership and output uniqueness/order match. Family-based textual regrouping and nil skipping are more detailed than the generic no-byte-roundtrip promise; ribbon generic output separately covered.'),
 'M01-WRITE-ENCOUNTER':('partial',[('04','§5.5'),('36','§3'),('73-b','encounter save lifecycle')], 'Nonpositive probability omission and default restoration are explicit. Nonpositive version omission can additionally collapse negative-version identity; no such actual supplied negative record, but permissive input accepts it.'),
 'M01-WRITE-TRAINER-FACILITY':('partial',[('04','§5.5'),('76','§8.4'),('73-a','§6')], 'Trainer compound identity and specialized facility output/failure paths match; complete false/nil field omission and SuperShiny ordinary-Shiny suppression remain finer than general export prose.'),
 'M01-WRITE-METADATA':('partial',[('04','§5.5'),('24','§3'),('73-a','§6')], 'Suffix grouping, global-before-player order and effective inherited charset output reviewed; current general output contract does not enumerate all these normalization details.'),
 'M01-WRITE-DUNGEON-ALL':('partial',[('04','§5.5'),('14','§5'),('73-b','dungeon/world data boundary')], 'All22 writer calls and nontransactional lifecycle checked. Tileset-resource loading even without output paths and original-tile-only serialization remain bounded finer details.'),
}

# Resolve prefixes with multiple main/data siblings explicitly.
for key,name in {
 '60-berry':'pokemon-rules/wp60-berry-plants.md',
 '22-transformation':'pokemon-rules/wp22-transformation-data.md',
 '23-shadow-data':'pokemon-rules/wp23-shadow-data-and-vectors.md',
 '74':'demo-dx/wp74-battle-animation-authoring-and-exchange.md',
 '76':'demo-dx/wp76-facility-content-generation-and-simulation.md',
}.items():P[key]=F+name
d=s.read('source-to-spec.json')
for c in d['capabilities']:
    if c['capability_id'] not in decisions:continue
    status,refs,comparison=decisions[c['capability_id']]
    c.update(status=status,spec_anchors=[dict(path=locate(key),version=s.B,clause=clause) for key,clause in refs],
             current_contract_comparison=comparison,semantic_comparison_complete=True,
             evidence_level='supported_static' if status=='supported' else 'static_semantic_comparison',
             supported_boundary='Only the named M01 data/config/lifecycle projection; no reference/model/runtime execution or full consumer-domain certification.',
             pending=[],open_consumer_or_data_review=None)
    if c['capability_id']=='M01-LZ-PRIVATE':c['alias_of']=['M01-LZ-LOAD','M01-LZ-DEFAULT-BUILD']
s.write('source-to-spec.json',d)
o.progress('已逐条收束56项主责翻译/解析/编译/反写能力的现行合同比较。partial现用于具体覆盖不足，不再用已完成的数据阅读任务占位；supported均限定静态交界。','固定注册表、数据记录方法和配置条款的最终精确映射')
print('Manual primary capability decisions:',len(decisions))
