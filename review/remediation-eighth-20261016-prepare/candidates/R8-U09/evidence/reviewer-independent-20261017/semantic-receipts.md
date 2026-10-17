# 本次非作者实读回执

固定候选 `6fddcf1af27169cdd31eabf42cc947b3424f18f8`，基线 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`，参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

本表是本次实际子上下文的最终回执接收；不把旧reader或作者FULL转移给主审。完整路径、父对象身份与45适用完整单位保存在[input-ledger.json](input-ledger.json)，来源合同保留原commit/path与C35恢复位置。

## /root/egg_domain

```json
{
  "context": "/root/egg_domain",
  "result": "PASS_SCOPED",
  "contracts": [
    "GR8-PBS-EGGGROUP-DOMAIN-001"
  ],
  "formal_whole": [
    "WP03 baseline1–393/candidate1–419",
    "WP18 baseline1–386/candidate1–388",
    "WP33 1–213",
    "WP34 baseline/candidate1–233",
    "README1–169",
    "scope1–155"
  ],
  "reference_ranges": [
    [
      "Data/Scripts/010_Data/001_Hardcoded data/003_EggGroup.rb",
      [
        [
          1,
          101
        ]
      ],
      "4972a9047e6a3f395ac5139aa9dcfdb8c13b6907"
    ],
    [
      "Data/Scripts/010_Data/001_GameData.rb",
      [
        [
          76,
          153
        ]
      ],
      "ccfd971a29b3bab107e2da6865ac0050ed3256b0"
    ],
    [
      "Data/Scripts/010_Data/002_PBS data/008_Species.rb",
      [
        [
          52,
          111
        ],
        [
          175,
          223
        ]
      ],
      "1ce450615687be8ecba5dde48474dd745acda29d"
    ],
    [
      "Data/Scripts/021_Compiler/001_Compiler.rb",
      [
        [
          255,
          293
        ],
        [
          384,
          486
        ],
        [
          690,
          737
        ]
      ],
      "1dd5f374734935f15502f973e07d2a603a1477dd"
    ],
    [
      "Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb",
      [
        [
          4,
          68
        ],
        [
          283,
          383
        ],
        [
          388,
          538
        ]
      ],
      "48e8b782e7175b2631b05d801d6bdcc391b5ddbe"
    ],
    [
      "Data/Scripts/012_Overworld/007_Overworld_DayCare.rb",
      [
        [
          1,
          564
        ]
      ],
      "302921c96ecfc4767d9ab9515d8d1e7820aa858c"
    ],
    [
      "Data/Scripts/020_Debug/002_Editor_DataTypes.rb",
      [
        [
          1040,
          1176
        ]
      ],
      "ee08fe75502b1fdb88ef948017452e9fdf7e65c8"
    ],
    [
      "Data/Scripts/020_Debug/001_Editor_Utilities.rb",
      [
        [
          116,
          129
        ]
      ],
      "3c1d94899443121d3c5a00bbb0cbd501efb84598"
    ],
    [
      "PBS/pokemon.txt",
      [
        [
          3218,
          3244
        ],
        [
          3482,
          3507
        ],
        [
          4538,
          4564
        ]
      ],
      "39aa345a49b40ba835abeb3c3d1a29ab67850986"
    ]
  ],
  "reports": [
    "adjudication/root-egggroup-domain-exact-inputs.v1.json",
    "tasks/pbs_creature_current_cloud/egggroup-exact-domain-review-request.v1.json",
    "tasks/counter_egggroup_existing_kernel/counterreview.json",
    "tasks/counter_egggroup_existing_kernel/necessary-source-units.json",
    "tasks/counter_egggroup_existing_kernel/mandatory-compile-generic-complete-range.v1.json",
    "adjudication/root-egggroup-domain-reception.v1.json",
    "adjudication/root-final-history-and-canonical-reception.v1.json (record32 + public qualifications)"
  ],
  "additional_formal_ranges": [
    "WP04 49–119/271–285",
    "audit/source-traceability160–176/233–245/554–566/822–834/941–953"
  ]
}
```

## /root/mg_name

```json
{
  "context": "/root/mg_name",
  "result": "PASS",
  "contracts": [
    "GR8-CRE-MG-NAME-CANCEL-001"
  ],
  "formal_whole": [
    "WP64 baseline/candidate1–174",
    "Creature catalog baseline/candidate1–183",
    "WP17 1–319"
  ],
  "delta_units": 10,
  "reference_ranges": [
    [
      "Data/Scripts/016_UI/024_UI_MysteryGift.rb",
      [
        [
          1,
          428
        ]
      ],
      "ef9558d924bc66f12ef93111a7745d7fa3eba28a"
    ],
    [
      "Data/Scripts/007_Objects and windows/011_Messages.rb",
      [
        [
          405,
          709
        ],
        [
          821,
          859
        ]
      ],
      "91c985bd0fda9a2368c894dee0ebbc9a476e9886"
    ],
    [
      "Data/Scripts/007_Objects and windows/012_TextEntry.rb",
      [
        [
          1,
          259
        ]
      ],
      "4258af660932798839ff3d8df01b11230c1e8ee1"
    ],
    [
      "Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb",
      [
        [
          1474,
          1488
        ]
      ],
      "6dd0c35a31040174efadefa2ba24a1c85a2499f9"
    ],
    [
      "Data/Scripts/020_Debug/003_Debug menus/007_Debug_PokemonCommands.rb",
      [
        [
          1088,
          1100
        ]
      ],
      "946ca260faca8a01faeced60c9d48bc2b479fc16"
    ],
    [
      "Data/Scripts/016_UI/007_UI_Bag.rb",
      [
        [
          552,
          580
        ]
      ],
      "e215b15f6555a6c136ee8ab2ca5d25b3195f376b"
    ]
  ],
  "extra_CREB_units": "All12 exact source units in handoff/accepted-facts-and-mandatory-companions.json; 6198B root +21730B full corrections +5113B Mail source companion actually read. Extra006_Item_Mail1–125,019_UI_PC1–237,Item_Utilities781–854.",
  "reports": [
    "tasks/creature_e_mail_mystery_completion_cloud/mg-name-escape-candidate.v1.json",
    "tasks/mg_name_escape_counterreview_cloud/independent-counterreview.md",
    "tasks/mg_name_escape_counterreview_cloud/input-read-ledger.json",
    "adjudication/root-mg-name-escape-required-adjudication.v1.json",
    "adjudication/root-r7-current38-bounded-crosswalk-reception.v1.json",
    "adjudication/root-primary-creature_e/mail-mystery-primary-complete-root-reception.v1.json",
    "adjudication/root-primary-creature_e/ui-mysterygift-pc-reception.v1.json",
    "adjudication/root-primary-creature_e/forward-mapping.json",
    "tasks/creature_b/final-evidence-corrections.current.json"
  ],
  "controls": "6/6 naming controls; MG25/29–32 preserved; complete receive/download/codec chain preserved",
  "extra_context": "/root/mg_name/counter_semantics: six controls read-only counter PASS, no duplicate historical vote"
}
```

## /root/ui_shadow

```json
{
  "context": "/root/ui_shadow",
  "result": "PASS",
  "contracts": [
    "GR8-UI-003",
    "GR8-PBS-SHADOW-TYPE-LEGACY-001"
  ],
  "formal_whole": [
    "WP66A baseline/candidate1–267",
    "WP23 appendix baseline/candidate1–241"
  ],
  "delta_units": 22,
  "delta_extension": "Compiler967–1018 includes final method end",
  "extra_reference_ranges": [
    "Summary1–1400",
    "DrawText1–1151",
    "GrowthRate1–188",
    "ShadowPokemon data1–70",
    "SaveValues1–127",
    "Pokemon180–250",
    "Pokemon Shadow extension1–221",
    "PBS pokemon1–42 complete BULBASAUR (not wholePBS FULL)",
    "default types1–129",
    "original optionalSHADOW1–7",
    "originalSHADOWRUSH102–113",
    "Compiler384–485/690–737",
    "Item1–48"
  ],
  "reports": [
    "UI complete proposal/counter",
    "SHADOW complete query/eight-section counter/all13 facts",
    "token21574 complete mandatory companion",
    "generic complete-range companion",
    "findings complete corresponding2 records",
    "originalroot adjudications and finalcanonical corresponding2 records"
  ],
  "controls": "ordinary/Shadow 64 and0 width, max level, saved_exp; perMove true/false fixed sample with valid effective type"
}
```

## /root/three_optional

```json
{
  "context": "/root/three_optional",
  "result": "PASS",
  "contracts": [
    "GR8-EXT-CD-004",
    "GR8-EXT-CD-003",
    "GR8-CRE-WP31-UNKNOWN-001"
  ],
  "formal_whole": [
    "WP34 baseline/candidate1–233",
    "WP26 baseline/candidate1–208",
    "WP31 baseline/candidate1–268",
    "WP58 1–181"
  ],
  "delta_units": 13,
  "extra_reference_ranges": [
    "DayCare1–564",
    "Pokemon28/77/390–399/497–503/805–812/976–1045/1099–1127/1159–1226",
    "Pokemon_Owner1–73",
    "Settings17/135",
    "RecordedBattle1–287",
    "Challenge_Battles1–144",
    "CatchAndStoreMixin1–271",
    "Battle_Peers1–77",
    "Battle1–215",
    "Trainer1–194",
    "Player1–123",
    "Battle_CommandPhase1–265",
    "Battle_StartAndEnd247–317/405–512",
    "Species52–111/277–285",
    "GameData78–146",
    "Compiler384–436/438–484/690–737",
    "CompilePBS4–68/283–538",
    "Evolution1–75; rest file lexical registration count64 only"
  ],
  "extra_formal_ranges": [
    "WP03 200–227",
    "WP04 66–112/163–183",
    "BR full220–261 plus context",
    "BE full1–46"
  ],
  "reports": [
    "delegation/counter_cd004_existing_crea-input.v1.json",
    "evidence/adjudication-inputs/722949b59a945e31580d19edc56be56346632d45934694dae6e2fa5a8b7d89a5.json",
    "adjudication/root-cd004-navigation-reception.v1.json",
    "delegation/counter_cd003_existing_fac-input.v1.json",
    "evidence/adjudication-inputs/769291164338918537338e64881f91e57bf964c2f911185bb5523145c4ebb6d2.json",
    "adjudication/root-cd003-recording-attribution-reception.v1.json",
    "tasks/creature_c_existing_crea/wp31-unknown-method-note-review-request.v1.json",
    "adjudication/root-wp31-unknown-exact-inputs.v1.json",
    "tasks/creature_b/history-final-joins/comparison.json",
    "adjudication/root-final-history-and-canonical-reception.v1.json corresponding3 records"
  ]
}
```

## /root/evidence_audit

```json
{
  "context": "/root/evidence_audit",
  "result": "PASS_EVIDENCE_SCOPE_ONLY",
  "full_public_qualifications": [
    "AGENTS6328B",
    "review-SKILL3598B",
    "eighth-global-review-prompt36653B",
    "history-qualifications15058B",
    "accepted-facts22397B",
    "policy25539B",
    "CREB input-provenance-corrections3290B",
    "final-execution-classification22069B/304lines",
    "originalhandoff preparation prompt/parent-dispatch/mandatory-supplement"
  ],
  "bounded_public_history": "root-final-history103072B public qualifications/counts/history rules +7canonical records; other32 structure/navigation only",
  "readset_classification": "45 applicable delta units; inherited64 root inputs/8 companions preserve original handoff receipt chain; do not force foreign32 root business rereview",
  "author_qualification": "80events+14formal retrospective whole-doc declarations; authorAGENTS explicit event and MG236–428 FULL not demonstrated; reviewer補讀不倒填"
}
```

## 有限结果与协调

五个直接子审全部完成，无所属具名必要未读单位。EggGroup、MG及五optional均PASS_SCOPED；证据审PASS限授权、身份、资格和读集分型。MG反方子context只读核六命名分支，同结论，未新增历史根/重复票。

MG完整1–428由本次审者实际读取，连同CREB12单位和邮件Give/Take补读；作者窄范围声明不被改写。WP31检查guard仅按§4，after-evolution内部动作直接扫描自身没有这些guard，不扩任意坏数据接口。超1MB源/报告的空content响应已由语义审者用既知blob恢复真实内容，可得未读不记limit。

所有语义控制均SOURCE_STATIC/DERIVED_VECTOR、NOT_EXECUTED。actual配置缺权威echo逐字段UNVERIFIED。候选PASS不代替实际整合、ACCEPTED或CLOSED。
