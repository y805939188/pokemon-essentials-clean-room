# 独立并行批次B · 送审交付摘要

已按 WP68→WP69→WP70 串行完成提取、逐包静态自检与字节固定，交付6份主规格、3份数据附表和108个静态场景。全部新稿状态为 **ReviewPending（具名静态范围，独立并行批次B，尚未外审／待统一合入登记）**；本交付可供独立外审，不代表已发起另一会话或获得通过。

工作区：`/Users/dingshinn/Desktop/pokemon-spec-parallel-minigames/`。主库和交接目录只读；未修改全局矩阵、manifest、主TSV、reference或任何reviewer原件。固定reference commit为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

## 范围与场景

| 包 | 活动与具名范围 | 场景 | 附表 |
| --- | --- | ---: | --- |
| WP68 | Duel D-A～E；Triple Triad T-A～G | 12＋24 | 卡面／价格向量在正文 |
| WP69 | Slot Machine S-A～F；Voltorb Flip V-A～E | 16＋18 | 有序22×3转轮；75棋盘候选 |
| WP70 | Lottery L-A～E；Mining M-A～F | 16＋22 | 61挖掘候选／48身份／13铁形状 |

## 新规格的完整身份

下列路径相对独立工作区；建议主库规格路径同名，实际导入以 integration-proposal.json 的精确白名单为准。

| 新产物 | SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/ui/wp68-duel.md` | `6699589968fd4b8822f563f75c5b083cc89fda6fe23adefa04041ee895db2ede` | 9133 |
| `specs/creature-rpg/wp68-triple-triad.md` | `1cb1ebf9da6989c3a0ab1edf26a7cf0157fc8c702c679ca17d245274fbb03adf` | 17196 |
| `specs/ui/wp69-slot-machine.md` | `ac2c0ad509b897f72287a9ee55c12930a8c7e6c0aa395b90f968a9c6a00d0fe6` | 11143 |
| `specs/pokemon-rules/wp69-voltorb-flip.md` | `1708fbb07da943c13b6726ea2232f6eaa13b9906d77ccd39fa57b094c00eb60d` | 10295 |
| `specs/ui/wp69-slot-reels.md` | `6065db8382d3cc0eba4f506c75e58194c04ece6747e1706bf539b09f106dc3b1` | 1945 |
| `specs/pokemon-rules/wp69-voltorb-layouts.md` | `50d97a9f6a61c97087341a1b0c1f5551957a60ad62b46afe91ad1d4a1973ec97` | 4053 |
| `specs/pokemon-rules/wp70-lottery.md` | `f37d37df4c2992b81e8a6a38bd02570d0de4db927c3d0efd051fb6181a40f7ed` | 10078 |
| `specs/ui/wp70-mining.md` | `7c692fbbf9990dfb3b50a13e9e2773b00dc29b1bde4a60142714c15fe21e238a` | 12474 |
| `specs/ui/wp70-mining-data.md` | `ddd6f46d30f61912fd052d22df3c90716799a820c8c6e6c1ad2135ac92fce9f9` | 5594 |

## 冻结输入与验证

14份核心上下文／依赖、4份闭合权威材料的完整身份均独立复测；再固定2份交接材料，共20份只读上下文副本。根AGENTS与快照版字节一致。依赖绑定WP06／17／19／24／25／27；冻结矩阵中的旧状态是输入历史，闭合报告才证明该基线WP62已限定通过。没有追随或接管主线A的WP22／23／32。

实际执行的检查包括：9份新稿逐包固定版本回验、108个场景ID核对、43条新稿相对链接存在性、28份具名源文件完整哈希／字节及commit blob比较、33条阅读范围记录、字面数据顺序／重复／尺寸、固定算术、JSON和导入集合核对。源读取深度按source-manifest逐文件记录，不把整文件身份复测说成全文语义审读。所选实时依赖在批末取证时未漂移，不要求主库整份历史快照一致。

6个输入／返回流程、资源提交／上限、彩票集合、数值／随机／统计及产物绑定的交界结论见 [boundary-checks.json](boundary-checks.json)。自行检查只支持送审，不自动提升为Reviewed。数字核对没有运行玩法、输入、参考Ruby或表达式、生成器、编译器、转换器、事件解释器、插件、真实存档／地图或网络；没有Agent／新任务／跨会话消息／提交／推送。

## 具名边界与未决

- Duel无中局退出；同归零按负；正常恢复速度不等于坐标／朝向状态事务恢复。
- Triple Triad最大等级未消费、direct败局错扣残留身份、AI评分与连锁不同；均单列参考反例。
- Slot支付tick未推进、耗尽读取旧全局余额、重玩前可额外投币；Voltorb高等级踩雷倒置夹限失败，1000次校验失败仍返末盘。
- Lottery含蛋、队伍重复扫描、首个最优保留；检索不发奖。Mining内部位置重试可不终止，坍塌／放弃仍发已揭物，逐件接收可整批部分成功。
- 未确认需要修改旧已审规格的反例； [new-observations.md](new-observations.md) 仅登记本批新范围异常，没有重开旧编号。
- 最终概率／重试可达频率在对应具名项保持未决；Demo事件、宿主、媒体、插件、U01–U10、WP77证据边界及WP78→WP79→WP80出口全部保留。

## 自有配套文件完整身份

此表在摘要写入前测量；摘要自身由局部TSV与integration-proposal记录，避免自哈希。最终运输清单／检查报告见current-hashes.tsv与final-checks.json，不属于历史主TSV或审查批准。

| 配套文件 | SHA-256 | 字节 |
| --- | --- | ---: |
| delivery/boundary-checks.json | `b88a153539d54510576de328e2afc92d9dd1c7989fb56e44cd4293831990bd19` | 8665 |
| delivery/checks/verify_delivery.py | `33abbd81ade3a7b0d64ebf1feafd4443837f9384ece31174ba02586acd5ff75a` | 6384 |
| delivery/checks/verify_package.py | `e97521d6c589f3eb63863d9b048facfac95cad62004c3542658e053d6b66aa63` | 2634 |
| delivery/checks/wp68-constant-checks.json | `01b129e16e7bd20d9d0a0fd44c382becbb8428df4e56df329be692379584bff2` | 483 |
| delivery/checks/wp68-fixed.json | `b26df4b94bf49fec4eb0a0cdd64316c9e3cc381bafb97e59d36476578679edfb` | 3031 |
| delivery/checks/wp69-constant-checks.json | `1cfedc929aec00b3f46828213b0c1b56fc0027ce3f0f7b99fc9fc9f73f8949e7` | 878 |
| delivery/checks/wp69-fixed.json | `55f2bf42ecae7699cfbe9013b5c29c2b18dbff78b6d68eed4ce122e79391abbc` | 3863 |
| delivery/checks/wp70-constant-checks.json | `94b0c2a3ec2c3808cf337a1ea3eae1df20b7377295d388918d68a6a3abc4201c` | 4289 |
| delivery/checks/wp70-fixed.json | `bb81d26dab9ac6c5da855f3870875126d0a456825e4d9a8d71d0d58add274442` | 3243 |
| delivery/evidence/batch-integrity.json | `0dd5fcd559c373b8ea5445f7e5b93252700fee3a8c812b6da4317b25fd942686` | 17009 |
| delivery/evidence/source-manifest.json | `0895375ef13c3e3b041926ea24d8ee83eb1e6a53513fe8439bd626bf1dd18b13` | 14339 |
| delivery/input-manifest.json | `699fc23b7a5cbd0c986ba7aa76ab8d7432185a9b6dc0c3bb83e9070ac7836cdc` | 11849 |
| delivery/new-observations.md | `62371334e87bb116b66d03e75f5d638272f7deafcb2d362a082e87839c7aebec` | 1979 |
| delivery/proposed-feature-matrix-rows.md | `b3a6dea6655a214b13a4afb89768d4bb1de10af97734aa95515eff727dd08eb7` | 4035 |
| delivery/self-checks.json | `4f6f22448691798ff2bc5cea032c81a1e13a0bfa26c84ecac78c8e56a95df729` | 17282 |

## 单一整合协议与停止点

整合者逐文件核对 integration-proposal.json：确认来源身份／待审状态、主库目标未冲突、冻结依赖与整合时版本适用，然后只导入明确白名单的新文件，并串行登记六条矩阵提案、manifest和主TSV。若整合时改字节，应重测并保留被审版本差异。不得以整个独立工作区覆盖主库；20份上下文副本全部排除。新规格的审计源路径映射主库reference，不是本地文件存在性声明；合入后还需再次检查链接。

本批在完成WP70及本送审包后停止，不启动WP71或第四包，不执行主库整合，不占用全局轮次。
