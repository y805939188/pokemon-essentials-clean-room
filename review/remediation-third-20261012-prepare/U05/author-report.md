# U05 作者候选交接

已从固定派发858ac243763ec10a342aec50047bfbbbaec662ad建立独立作者分支/工作树，按接受base1cbb5fd292b9552d46cc193511fa451ed3ba31ee完整复制并修订七个候选镜像。正式正文、公共台账、U01/U02/U03/U04/U06固定包、旧报告/229关闭/341 scoped贡献、main和参考均未改。作者自检不构成独立PASS、actual、接受或CLOSED。

| 必修ID | 候选条款 | 新静态设计及修订结果 |
| --- | --- | --- |
| GR3-M10-001 | wp66-a-party-and-summary-ui.md §4.4/4.4.1；wp66-b-storage-and-pokedex-ui.md §4.2 | U05-MV01/U05-MV02/U05-MV03 |
| GR3-M10-002 | wp66-c-bag-item-storage-and-shop-ui.md §5/5.1/7 | U05-QN01/U05-QN02/U05-QN03/U05-QN04 |
| GR3-M10-003 | wp67-a-battle-interaction-and-presentation.md §9.1 | U05-TX01/U05-TX02/U05-TX03/U05-TX04 |
| GR3-M10-004 | wp67-a-battle-interaction-and-presentation.md §10 | BT-K40/U05-AR01/U05-AR02 |
| GR3-M11-001 | wp62-pokedex-records-regions-and-content.md §5.3/5.3.1；wp66-b-storage-and-pokedex-ui.md §7.1 | U05-HAB01/U05-HAB02/U05-HAB03/U05-HAB04 |

M10-001分别记录取回后确认袋1/A空/B持物（总2）、BACK袋1/A/B空、未嵌套袋0/A空/B持物；来源/索引未变，不套C125、不加守恒或重验证。M10-002给三入口完整首匹配顺序、0/1与立即1/11等待以及单键/极限门。M10-003给busy非暂停仅恢复、显式暂停只解除、全显才返回，并保普通/暂停1秒/3秒。M10-004只修UI首提示/正常补位不复位和3/4/5连续判；完整B028/PA-P28合法三员/Growl/HP前提与旧关闭保持。M11-001给正宽/ceil/行优先已有占位/平移/可见Point并集、1格/5格/缺尾/缺省零宽/关闭首条第二可见，区分WP63长度与首条并保版本枚举缺陷。

已接受U04仅作必要WP67-A消费者一致性：执行退款残留与同轮正常终局/下一命令/正式失能的2/1/1、每次容量与提示正常返回、异常前缀不回滚；自然之恩首击/HP条/反应/持物已提交前缀不推出外层恢复/退出/错误窗口。U05-RF01–03/NG01不是第六finding。WP28 f6bb后继及WP17/63/56/PA-P28只读，shared-consumer-proposal.json明确无需foreign正文变化，不产生竞争镜像。

原目录完整输入/ID/资格与顺序保留；仅UI目录K40的更替对阵残留按独立复审指出有界纠正，其余570/571旧表行及图鉴170旧表行逐字保留。初始decc9db候选的K40错误不借新增AR设计覆盖，修订后候选另行独立复核。七文件base/new完整blob、SHA256、bytes见candidate-identities.json；candidate.patch仅七正式映射，在临时基线副本git apply --check、apply后全部七文件与候选逐字一致。完整固定输入身份核对、十五限定控制精确tuple/资格对象、九必要交界/N14–17变化局部和逐验收/正常/反向/unknown见author-self-check.json。identity/JSON/patch检查只证明字节与结构，不代表行为执行。

真实读取范围：完整派发文件解析，五canonical及验收、十五控制的有效前提/反例/限定/最低修订/确定复核、九交界有限合同与N14–17去重语义阅读；不重复整套raw/ACT/229/341历史证明。必要参考定点全列于source_read_spans，固定R commit8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/tree7589c800b61ba13a13040ed0d686979b80a84fd0；只通过git读取文本，未运行Ruby/游戏/编译器/转换器/反序列化器/行为案例或Demo。

公共来源和Feature Matrix为精确prior身份＋append文本提案，仅唯一整合员承接；registration-proposal.json保18/23、5/6主题、CLOSED0/U07未完成，未写正式接受。模型请求沿派发，缺有效回显记UNVERIFIED，不做额度审计。素材/宿主/输入可达/Demo/逐帧输出仍未知，所有案例NOT_EXECUTED；历史异常未来兼容由用户决定。

独立复审入口为本目录independent-review-task.md。父任务须用外部真实作者commit/tree绑定七完整镜像、candidate-identities、patch与八作者证据；另一个角色在独立工作树/分支只写independent-review/attempt-01/的六文件。此作者不签其结果，也不提前构造actual或登记接受。作者commit/tree与完整远端fetch字节回读结果由最终外部回执返回，避免递归self-SHA。
