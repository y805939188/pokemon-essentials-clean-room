# B05 原稿最小同步范围申请

本申请仅请求下列五个原稿路径的条款同步；正式写路径仍以批准 B05 十项白名单为准。具体可审补丁见 [original-synchronization-proposed.patch](original-synchronization-proposed.patch)，共五路径、233 行 diff；原稿尚未改动。授权依据待父任务答复，本申请不构成批准。

| 路径／条款 | 现状与拟同步结果 | Finding／固定参考证据 |
| --- | --- | --- |
| `specs/creature-rpg/wp18-creature-identity-species-ownership.md` §3.2 默认字段、§4.2 初始化随机、§9 同值边界 | 补清 `Unnamed`、`???`、继承形态的图鉴号、0 的解除形态／Mega 消息、空字符串后缀与空值／空列表的区别；把“两类随机”限定为基础初始化，明确创建复检可再抽样形态 | A021/A022；`010_Data/002_PBS data/008_Species.rb:175–220`、`014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:146–150`、`014_Pokemon/001_Pokemon.rb:1136–1227` |
| `specs/creature-rpg/wp20-hp-status-moves-helditem.md` §5 已知招式／记录／重学／索引删除 | 按入口限定四槽；整表可存五项和空列表；静默新增只删除首项一次；明确有效负索引及越界无变化；重学配置仅追加首招记录，不直接追加物种蛋招；补背包 TR 成功后的首招追加与队伍入口差异及零招式调用边界 | A023/A024/A025/A044/C126 的 B05 贡献；`014_Pokemon/001_Pokemon.rb:605–731`、`016_UI/022_UI_MoveRelearner.rb`、`019_Utilities/001_Utilities.rb:452–486`、`016_UI/005_UI_Party.rb:726–743`、`016_UI/006_UI_Summary.rb:740–843` |
| `specs/pokemon-rules/wp19-attributes-ability-and-stats.md` §3.5 性格修正 | 加入完整 25 个序号→身份→升降属性映射（20 个修正、5 个中性），保留原有计算覆盖、缓存和取整规则，补具名数值对照 | A020 的 B05 部分；`010_Data/001_Hardcoded data/009_Nature.rb:12–173`；B01 只交付 WP03 依赖，未交付本表 |
| `specs/pokemon-rules/wp21-dynamic-forms-and-display.md` §3 C/D、§4.2 招式改写 | 补 ROTOM/KYUREM/NECROZMA/CALYREX/ZACIAN/ZAMAZENTA 具体招式及数据门；修明 ROTOM 同值裸提交可删唯一招，不补原实现没有的保底；保留 PP 钳制、删除时序、学习拒绝及部分失败 | A026/A027 的 B05 部分；`014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:221–265,325–385,562–587,650–729`、`014_Pokemon/004_Pokemon_Move.rb:24–27` |
| `specs/pokemon-rules/wp23-shadow-hyper-and-purification.md` 静态场景 W06 | 原 W06 的 H4/h80/JOY×1 不足以决定下降量和是否跨阶段；固定 HARDY/M4000/G2500 得 G2410/H4/h80，增加 LONELY 对照得 G2370/H3/h80；性格与起始量明确，友好阶段门仍先于降量 | A031；`014_Pokemon/003_Pokemon_ShadowPokemon.rb:51–53,71–79,99–104,116–119`、`014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:226–244` |

范围排除：历史批准／review／冻结记录、公共索引、Feature Matrix、coverage、trace、哈希、登记状态；WP28/WP30/WP66A/WP76 的跨批正文。原 Mega 表 `BANETTITE`、原 Shadow 的 `h=255 且 G=0` 门及原 GROWLITHE/SNORUNT 招式表正确，保留原稿，只修净化稿。U/G/AX、可选内容与运行观察 0、demo 链 0、静态向量未执行的限定全部保留。以上证据均为固定参考的静态阅读，不是运行验证。
