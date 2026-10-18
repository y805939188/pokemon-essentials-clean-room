# R8-U01 完整有效派发入口

状态 READY_PENDING_ROOT_CORE_FREEZE，UPDATE_NOT_STARTED，update_started:false。本提示词供用户在root实际冻结/后继发布绑定后手动派发；目前已启动整改0。B8=fd1df570cad987dc3852a3b958f03916e317f7fe，R=8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。项目 /workspace/pokemon-essentials-clean-room；R /workspace/pokemon-essentials 只读。

当前唯一分类依据是 adjudication/root-decisions.partial.json 的38条有限记录：29 required（2P2/27P3）与9 optional；另1独立视觉政策UNSELECTED，12有限NO_REQUIRED与4 binary负例分列，UI002原候选撤销。不是全轮最终总数。原33合同分类/严重度全保持；新5条见本包 contracts.delta.zh.json。全部9个optional保持未选择。旧合同中已解决的pending提案、33计数和WIP身份仅留历史，执行以本有效索引及root最终绑定为准。

完整读取 AGENTS.md、inputs/eighth-global-review-prompt.md、inputs/review-SKILL.md，以及本批固定引用的原prompt全文/原readset全部必要条款、对应contracts七组和新增根完整合同；精确重复内容可核等后关联去重，所有独有语义都须实读。索引、哈希、旧PASS和脚本不能代替实读。原包固定交付 5caff3bd1a1b062b48b7eda46777a614921946f3，恢复目录 evidence/external-recovered/handoff_preparation_cloud/5caff3bd1a1b062b48b7eda46777a614921946f3；原任务远端路径为该报告根/tasks/handoff_preparation_cloud/。原33全文不缩成摘要。

执行前，由root的真实后继发布入口提供最终语义core commit/tree、实际包含本补充和最终报告的enclosing commit以及逐文件身份。现有HEAD、旧40f45...、原准备5caff...都不是未来最终core；本包core/enclosing字段保持空。核对实际提供的commit、tree、path/mode/blob/bytes/SHA后才使用。共同门满足后9批隔离mirror可独立准备，9是逻辑批数，不代表slots；当前可启动0。

作者请求gpt-6.1-sol/xhigh，真实非作者reviewer请求gpt-6.1-sol/ultra；均default普速、normal、Fast off。actual model/effort/tier/speed/Fast无权威echo逐字段UNVERIFIED，实际作者/审者ID尚NOT_STARTED。CLI/Desktop启动方法未实际测试，UNVERIFIED；用户手动建立实际context并粘贴本批入口，不编造flags或任务ID。

候选作者只写本批mirror及独立证据，不直接写正式target。所有正式文件、公共planning/audit索引、共享目录及台账由R8-INTEGRATOR唯一写者逐贡献整合；仅同步实际受影响行，不扩大整表重写。候选PASS、actual整合PASS、ACCEPTED、CLOSED四门分列；最终actual审者须实际不同于作者、全文接收受影响结果与累计保留。文件冲突是写权/接收门，不自动变成根因语义先后依赖。

采用最终态文档修订：错误原位替换、必要缺项补齐、正确scope保留；原提案/反证/撤销按原字节留审计。不改R、不开发框架、不复制源码或Ruby架构、不选择未选optional/policy、不合并main。SOURCE_STATIC/DERIVED_VECTOR与TOOL_VALIDATION/真实执行分列，本准备新增业务/游戏/宿主/编译/行为模型/向量运行0，NOT_EXECUTED，不用运行未知豁免可得条款。

本批必修：GR8-KER-001、GR8-KER-002。

固定保留全文：review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/evidence/external-recovered/handoff_preparation_cloud/5caff3bd1a1b062b48b7eda46777a614921946f3/handoff/batches/R8-U01/prompt.md（49291 bytes，SHA256 7c34e0762ffc6a3316bb696314b428293e48b553faae959cfa226181e95fc9a4）。原完整读集：review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/evidence/external-recovered/handoff_preparation_cloud/5caff3bd1a1b062b48b7eda46777a614921946f3/handoff/batches/R8-U01/readset.json（SHA256 e3afa535266c25f1ff6182703d9b6b34a1bbe68ce2c0f087bd4a61d445e54594）。先读上述全文，再组合本入口及新增完整合同；任何引用材料缺失保持具体范围OPEN，不能将此入口单独当已完成阅读。

本批没有新增必修行为根。原完整逐项合同、普通/失败/取消/部分提交控制、preserve与验收原文继续有效；只更新共同分类、冻结/执行门和全局接收边界。

本批完整有效读写/角色/候选/actual分工：

```json
{
  "id": "R8-U01",
  "title": "存档有序失败与读取结果门",
  "required_ids": [
    "GR8-KER-001",
    "GR8-KER-002"
  ],
  "input_contract_commit": null,
  "R8_core": "READY_PENDING_ROOT_CORE_FREEZE",
  "candidate_mirror_prefix": "review/remediation-eighth-20261016-prepare/candidates/R8-U01/mirror/",
  "candidate_write_set": [
    "review/remediation-eighth-20261016-prepare/candidates/R8-U01/mirror/deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md",
    "review/remediation-eighth-20261016-prepare/candidates/R8-U01/mirror/deliverables/final-specification-set/generic-kernel/wp10-migration-failure-recovery.md",
    "review/remediation-eighth-20261016-prepare/candidates/R8-U01/mirror/deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md",
    "review/remediation-eighth-20261016-prepare/candidates/R8-U01/mirror/deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md"
  ],
  "actual_target_write_set": [
    "deliverables/final-specification-set/generic-kernel/wp09-save-startup-continue.md",
    "deliverables/final-specification-set/generic-kernel/wp10-migration-failure-recovery.md",
    "deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md",
    "deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md"
  ],
  "evidence_ids": [
    "E0006",
    "E0007",
    "E0008",
    "E0010",
    "E0026",
    "E0072",
    "E0077",
    "E0082",
    "E0117",
    "E0121",
    "E0122",
    "E0123",
    "E0137",
    "E0138",
    "E0141",
    "E0142"
  ],
  "semantic_predecessor_batches": [],
  "independence": "候选镜像与其它批隔离；本批实际target整合由R8-INTEGRATOR唯一写。",
  "author": {
    "logical_entry": "R8-A-R8-U01",
    "requested_model": "gpt-6.1-sol",
    "effort": "xhigh",
    "tier": "default",
    "speed": "normal",
    "Fast": "off",
    "actual_task_id": "NOT_STARTED",
    "actual_configuration": {
      "model": "UNVERIFIED",
      "effort": "UNVERIFIED",
      "tier": "UNVERIFIED",
      "speed": "UNVERIFIED",
      "Fast": "UNVERIFIED"
    }
  },
  "reviewer": {
    "logical_entry": "R8-R-R8-U01",
    "requested_model": "gpt-6.1-sol",
    "effort": "ultra",
    "tier": "default",
    "speed": "normal",
    "Fast": "off",
    "actual_task_id": "NOT_STARTED",
    "independence": "必须实际不同于该批作者，不能改角色名自验。",
    "actual_configuration": {
      "model": "UNVERIFIED",
      "effort": "UNVERIFIED",
      "tier": "UNVERIFIED",
      "speed": "UNVERIFIED",
      "Fast": "UNVERIFIED"
    }
  },
  "shared_receivers": [
    "UI65加载",
    "WP08本地化",
    "WP09恢复",
    "WP65标题/加载"
  ],
  "state": "PLANNED_NOT_STARTED",
  "current_launch_blocker": "READY_PENDING_ROOT_CORE_FREEZE; UPDATE_NOT_STARTED",
  "optional_ids_if_later_selected": [
    "GR8-UI-001"
  ],
  "selected_optional_ids": [],
  "conditional_target_write_set_by_id": {
    "GR8-UI-001": [
      "deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md"
    ]
  },
  "inherited_complete_prompt": {
    "repo": "/workspace/pokemon-essentials-clean-room",
    "commit": null,
    "tree": null,
    "commit_binding": "PENDING_ACTUAL_ENCLOSING_ROOT_PUBLICATION; exact content identity below, not a future Git identity",
    "path": "review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/evidence/external-recovered/handoff_preparation_cloud/5caff3bd1a1b062b48b7eda46777a614921946f3/handoff/batches/R8-U01/prompt.md",
    "mode": "100644",
    "bytes": 49291,
    "sha256": "7c34e0762ffc6a3316bb696314b428293e48b553faae959cfa226181e95fc9a4",
    "blob": "2f093c9489947ac6ceb0833e4e888e7f9f54ed33",
    "purpose": "原批次全文固定保留；受本有效共同门与增量条款限定"
  },
  "inherited_complete_readset": {
    "repo": "/workspace/pokemon-essentials-clean-room",
    "commit": null,
    "tree": null,
    "commit_binding": "PENDING_ACTUAL_ENCLOSING_ROOT_PUBLICATION; exact content identity below, not a future Git identity",
    "path": "review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/evidence/external-recovered/handoff_preparation_cloud/5caff3bd1a1b062b48b7eda46777a614921946f3/handoff/batches/R8-U01/readset.json",
    "mode": "100644",
    "bytes": 115770,
    "sha256": "e3afa535266c25f1ff6182703d9b6b34a1bbe68ce2c0f087bd4a61d445e54594",
    "blob": "fd6db2ede15697a467884eb5812e14d492993b0b",
    "purpose": "原完整必要读集，不以本索引替代实读"
  },
  "inherited_semantic_scope": "全部原required合同七组、反例、preserve、验收、回归及共同前提原文保留；旧33计数/core/pending状态由本补充和root最终事实取代。",
  "input_commit_rule": "原40f45...仅为历史准备输入；执行前绑定实际包含本补充与根最终报告的enclosing commit，不伪造未来hash。",
  "additional_contract_ids": [],
  "optional_additional_contract_ids": [],
  "additional_read_requirement": "继承原批全文和原readset；本批无新增必修行为范围。",
  "file_ownership_note": "原候选独占mirror及R8-INTEGRATOR唯一正式writer分工保留。",
  "additional_contract_pointer": "handoff/contracts.delta.zh.json#/records"
}
```

输出候选变更、逐ID验收/回归与保留范围、精确输入与目标身份、实读台账、失败/未知边界、共享贡献接收状态；作者不得自签actual最终验收。UPDATE_NOT_STARTED。
