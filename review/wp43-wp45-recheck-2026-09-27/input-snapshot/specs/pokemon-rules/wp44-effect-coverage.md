# WP44 附表：有界效果归属与数据对应（v2，首审有限修订）

状态：**ReviewPending（WP44有界覆盖索引，R01/R02修订后待复审）**；被审v1 `ea5237d3257e1326876d3aae8d36c9bac003eb9682ad7402b05bc02797b45e39`（24,809字节）留史，v2不冒充已审；静态审计材料，无运行确认。主行为见 [WP44](wp44-statuses-stat-stages-and-immunities.md)。源码名称仅为不透明审计身份，不是未来类、API或架构建议。

## 1. 范围和核对方法

固定源为 `Data/Scripts/011_Battle/003_Move/006_MoveEffects_BattlerStats.rb`：全文结构清点114个效果标识，67个纯参数段读取常量数据，47个其它行为段逐段阅读。下表114行各有归属；“前向”不是该效果已完成，也不把它当未发现。行为族共享边界向量不是为每个名称重新运行一个程序。

其中106项含本包阶级或附带标记合同（含除雾的阶级部分，其清理范围归WP45）；3项建立侧／全场效果归WP45；4项原能力值变更归WP47-A；1项HP平均归WP46。主归属计数106＋3＋4＋1＝114，共享责任不再计为新增效果。

| 源效果标识（审计） | 起始行 | 行为提要 | 主归属／交界 | 静态验收关联 |
| --- | ---: | --- | --- | --- |
| `RaiseUserAttack1` | :4 | 使用者：攻击＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserAttack2` | :14 | 使用者：攻击＋2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserAttack2IfTargetFaints` | :25 | 击倒记录成立后升攻击 | WP44 §7（具名复合／直接重写族） | 击倒／未击倒，G01上限 |
| `RaiseUserAttack3` | :43 | 使用者：攻击＋3 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserAttack3IfTargetFaints` | :54 | 击倒记录成立后升攻击 | WP44 §7（具名复合／直接重写族） | 击倒／未击倒，G01上限 |
| `MaxUserAttackLoseHalfOfTotalHP` | :73 | HP代价后直接设攻击极值 | WP44 §7（具名复合／直接重写族） | G10 |
| `RaiseUserDefense1` | :117 | 使用者：防御＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserDefense1CurlUpUser` | :127 | 蜷缩并升防：防御＋1；通用效果先设蜷缩标记，再执行该阶段的自身上升。 | WP44 [§7.1 K01](wp44-statuses-stat-stages-and-immunities.md#wp44-k01)，对象／条件／入口分支在该条完整给出 | G01/G06 |
| `RaiseUserDefense2` | :142 | 使用者：防御＋2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserDefense3` | :152 | 使用者：防御＋3 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserSpAtk1` | :162 | 使用者：特攻＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserSpAtk2` | :172 | 使用者：特攻＋2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserSpAtk3` | :182 | 使用者：特攻＋3 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserSpDef1` | :192 | 使用者：特防＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserSpDef1PowerUpElectricMove` | :203 | 充电并升特防：先把充电计数设2，再请求特防＋1；电招威力消费引用WP43，尾递减见§4。 | WP44 [§7.1 K02](wp44-statuses-stat-stages-and-immunities.md#wp44-k02)，对象／条件／入口分支在该条完整给出 | G01/G14 |
| `RaiseUserSpDef2` | :219 | 使用者：特防＋2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserSpDef3` | :229 | 使用者：特防＋3 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserSpeed1` | :239 | 使用者：速度＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserSpeed2` | :249 | 使用者：速度＋2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserSpeed2LowerUserWeight` | :260 | 身体轻量化：速度＋2；先比较“当前重量查询结果＋已存重量变化”是否大于1，是则已存重量变化再减1000参考重量单位并反馈，然后进入自身升速。 | WP44 [§7.1 K03](wp44-statuses-stat-stages-and-immunities.md#wp44-k03)，对象／条件／入口分支在该条完整给出 | G01/G06 |
| `RaiseUserSpeed3` | :278 | 使用者：速度＋3 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserAccuracy1` | :288 | 使用者：命中＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserAccuracy2` | :298 | 使用者：命中＋2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserAccuracy3` | :308 | 使用者：命中＋3 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserEvasion1` | :318 | 使用者：闪避＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserEvasion2` | :328 | 使用者：闪避＋2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserEvasion2MinimizeUser` | :338 | 变小并升闪避：先设置变小标记，再请求闪避＋2；踩踏计算引用WP43。 | WP44 [§7.1 K04](wp44-statuses-stat-stages-and-immunities.md#wp44-k04)，对象／条件／入口分支在该条完整给出 | G01/G03 |
| `RaiseUserEvasion3` | :353 | 使用者：闪避＋3 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserCriticalHitRate2` | :363 | 聚气：聚气记录直接设2，属于会心输入，不是七阶级中某项＋2。 | WP44 [§7.1 K05](wp44-statuses-stat-stages-and-immunities.md#wp44-k05)，对象／条件／入口分支在该条完整给出 | G14 |
| `RaiseUserAtkDef1` | :383 | 使用者：攻击＋1，防御＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserAtkDefAcc1` | :393 | 使用者：攻击＋1，防御＋1，命中＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserAtkSpAtk1` | :403 | 使用者：攻击＋1，特攻＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserAtkSpAtk1Or2InSun` | :414 | 成长：攻击→特攻依序请求各＋1；使用开始阶段若用户有效天气为晴／大日照，本次两项请求都改＋2。 | WP44 [§7.1 K06](wp44-statuses-stat-stages-and-immunities.md#wp44-k06)，对象／条件／入口分支在该条完整给出 | G06 |
| `LowerUserDefSpDef1RaiseUserAtkSpAtkSpd2` | :432 | 破壳：精确提交顺序：防御−1→特防−1→攻击＋2→特攻＋2→速度＋2。 | WP44 [§7.1 K17](wp44-statuses-stat-stages-and-immunities.md#wp44-k17)，对象／条件／入口分支在该条完整给出 | J04/G06 |
| `RaiseUserAtkSpd1` | :485 | 使用者：攻击＋1，速度＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserAtk1Spd2` | :495 | 使用者：速度＋2，攻击＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserAtkAcc1` | :505 | 使用者：攻击＋1，命中＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserDefSpDef1` | :516 | 使用者：防御＋1，特防＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserSpAtkSpDef1` | :526 | 使用者：特攻＋1，特防＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserSpAtkSpDefSpd1` | :537 | 使用者：特攻＋1，特防＋1，速度＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserMainStats1` | :548 | 使用者：攻击＋1，防御＋1，特攻＋1，特防＋1，速度＋1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseUserMainStats1LoseThirdOfTotalHP` | :560 | 五项上升并付1/3总HP代价 | WP44 §7（具名复合／直接重写族） | G06/G10 |
| `RaiseUserMainStats1TrapUserInBattle` | :596 | 背水一战：攻击→防御→特攻→特防→速度，各请求＋1；随后仅当当时拘束聚合查询为假才设置背水一战标记。 | WP44 [§7.1 K07](wp44-statuses-stat-stages-and-immunities.md#wp44-k07)，对象／条件／入口分支在该条完整给出 | G06 |
| `StartRaiseUserAtk1WhenDamaged` | :619 | 愤怒记录：建立时只置愤怒真，不立即升阶；后续命中反馈中，愤怒者存活且可升攻击时请求攻击＋1。 | WP44 [§7.1 K08](wp44-statuses-stat-stages-and-immunities.md#wp44-k08)，对象／条件／入口分支在该条完整给出 | G01 |
| `LowerUserAttack1` | :628 | 使用者：攻击−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerUserAttack2` | :638 | 使用者：攻击−2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerUserDefense1` | :648 | 使用者：防御−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerUserDefense2` | :658 | 使用者：防御−2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerUserSpAtk1` | :668 | 使用者：特攻−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerUserSpAtk2` | :678 | 使用者：特攻−2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerUserSpDef1` | :688 | 使用者：特防−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerUserSpDef2` | :698 | 使用者：特防−2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerUserSpeed1` | :708 | 使用者：速度−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerUserSpeed2` | :718 | 使用者：速度−2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerUserAtkDef1` | :728 | 使用者：攻击−1，防御−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerUserDefSpDef1` | :739 | 使用者：防御−1，特防−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerUserDefSpDefSpd1` | :750 | 使用者：速度−1，防御−1，特防−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `RaiseTargetAttack1` | :760 | 目标升攻击：目标攻击＋1。 | WP44 [§7.1 K09](wp44-statuses-stat-stages-and-immunities.md#wp44-k09)，对象／条件／入口分支在该条完整给出 | G01/G06 |
| `RaiseTargetAttack2ConfuseTarget` | :797 | 目标增强与混乱分别查询并部分成功 | WP44 §7（具名复合／直接重写族） | G11/V06 |
| `RaiseTargetSpAtk1ConfuseTarget` | :826 | 目标增强与混乱分别查询并部分成功 | WP44 §7（具名复合／直接重写族） | G11/V06 |
| `RaiseTargetSpDef1` | :855 | 目标升特防：特防＋1；招式明确忽略替身。 | WP44 [§7.1 K10](wp44-statuses-stat-stages-and-immunities.md#wp44-k10)，对象／条件／入口分支在该条完整给出 | G01 |
| `RaiseTargetRandomStat2` | :871 | 从资格通过的七阶级集合随机升2 | WP44 §7（具名复合／直接重写族） | G12 |
| `RaiseTargetAtkSpAtk2` | :893 | 装饰式双攻增强：每个目标先攻击＋2，再特攻＋2。 | WP44 [§7.1 K11](wp44-statuses-stat-stages-and-immunities.md#wp44-k11)，对象／条件／入口分支在该条完整给出 | G06 |
| `LowerTargetAttack1` | :923 | 目标：攻击−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetAttack1BypassSubstitute` | :933 | 忽略替身降攻击：攻击−1；相比普通攻击−1族，明确允许招式忽略替身。 | WP44 [§7.1 K12](wp44-statuses-stat-stages-and-immunities.md#wp44-k12)，对象／条件／入口分支在该条完整给出 | J03 |
| `LowerTargetAttack2` | :945 | 目标：攻击−2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetAttack3` | :955 | 目标：攻击−3 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetDefense1` | :965 | 目标：防御−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetDefense1PowersUpInGravity` | :976 | 重力增强降防：防御−1；重力计数>0时，在招式基底威力输入阶段把整数威力乘3/2并取整数下界，81→121；重力不生效则保留原值。 | WP44 [§7.1 K13](wp44-statuses-stat-stages-and-immunities.md#wp44-k13)，对象／条件／入口分支在该条完整给出 | J01 |
| `LowerTargetDefense2` | :986 | 目标：防御−2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetDefense3` | :996 | 目标：防御−3 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetSpAtk1` | :1006 | 目标：特攻−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetSpAtk2` | :1016 | 目标：特攻−2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetSpAtk2IfCanAttract` | :1027 | 诱惑式降特攻：特攻−2。 | WP44 [§7.1 K14](wp44-statuses-stat-stages-and-immunities.md#wp44-k14)，对象／条件／入口分支在该条完整给出 | G05 |
| `LowerTargetSpAtk3` | :1065 | 目标：特攻−3 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetSpDef1` | :1075 | 目标：特防−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetSpDef2` | :1085 | 目标：特防−2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetSpDef3` | :1095 | 目标：特防−3 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetSpeed1` | :1105 | 目标：速度−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetSpeed1WeakerInGrassyTerrain` | :1116 | 青草削弱降速：速度−1；当前存储场地为青草时，在本招基底威力阶段减半并四舍五入（正值恰半向上），61→31；否则保留原值。 | WP44 [§7.1 K15](wp44-statuses-stat-stages-and-immunities.md#wp44-k15)，对象／条件／入口分支在该条完整给出 | J02 |
| `LowerTargetSpeed1MakeTargetWeakerToFire` | :1133 | 沥青射击：先进入速度−1的普通单项提交；之后目标尚无沥青标记时置真，使后续火相性按WP43§3.3乘2，不叠加标记。 | WP44 [§7.1 K16](wp44-statuses-stat-stages-and-immunities.md#wp44-k16)，对象／条件／入口分支在该条完整给出 | G05/G01 |
| `LowerTargetSpeed2` | :1156 | 目标：速度−2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetSpeed3` | :1166 | 目标：速度−3 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetAccuracy1` | :1176 | 目标：命中−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetAccuracy2` | :1186 | 目标：命中−2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetAccuracy3` | :1196 | 目标：命中−3 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetEvasion1` | :1206 | 目标：闪避−1 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetEvasion1RemoveSideEffects` | :1217 | 降闪避与清理独立，清理可使招式在不能降时仍可行 | WP44 阶级部分；WP45 清理范围与期限 | G05/G06与WP45除雾对照 |
| `LowerTargetEvasion2` | :1317 | 目标：闪避−2 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetEvasion3` | :1327 | 目标：闪避−3 | WP44 §5、§7（基本／多项族） | G01/G02/G03/G06 |
| `LowerTargetAtkDef1` | :1337 | 目标：攻击−1，防御−1 | WP44 [§5.3 多项镜甲预检](wp44-statuses-stat-stages-and-immunities.md#wp44-mirror-precheck)；模式破坏者不关闭本层，中央反射另判 | M01–M03；原参数及有界目标资格保留 |
| `LowerTargetAtkSpAtk1` | :1347 | 目标：攻击−1，特攻−1 | WP44 [§5.3 多项镜甲预检](wp44-statuses-stat-stages-and-immunities.md#wp44-mirror-precheck)；模式破坏者不关闭本层，中央反射另判 | M01–M03；原参数及有界目标资格保留 |
| `LowerPoisonedTargetAtkSpAtkSpd1` | :1358 | 毒目标集合与多项下降；镜甲来源资格另核 | WP44 [§5.3 多项镜甲预检](wp44-statuses-stat-stages-and-immunities.md#wp44-mirror-precheck)；模式破坏者不关闭本层，中央反射另判 | M01–M03；原参数及有界目标资格保留 |
| `RaiseAlliesAtkDef1` | :1431 | 同侧盟友攻防增强：每个有效目标攻击＋1→防御＋1。 | WP44 [§7.1 K18](wp44-statuses-stat-stages-and-immunities.md#wp44-k18)，对象／条件／入口分支在该条完整给出 | J05/G06 |
| `RaisePlusMinusUserAndAlliesAtkSpAtk1` | :1478 | 正负电双攻增强：每个有效目标攻击＋1→特攻＋1。 | WP44 [§7.1 K19](wp44-statuses-stat-stages-and-immunities.md#wp44-k19)，对象／条件／入口分支在该条完整给出 | J05/J06/G06 |
| `RaisePlusMinusUserAndAlliesDefSpDef1` | :1531 | 正负电双防增强：每个有效目标防御＋1→特防＋1。 | WP44 [§7.1 K20](wp44-statuses-stat-stages-and-immunities.md#wp44-k20)，对象／条件／入口分支在该条完整给出 | J05/J06/G06 |
| `RaiseGroundedGrassBattlersAtkSpAtk1` | :1577 | 耕地式草成员增强：每个有效目标攻击＋1→特攻＋1。 | WP44 [§7.1 K21](wp44-statuses-stat-stages-and-immunities.md#wp44-k21)，对象／条件／入口分支在该条完整给出 | J07/G06 |
| `RaiseGrassBattlersDef1` | :1617 | 鲜花防守式草成员增强：防御＋1。 | WP44 [§7.1 K22](wp44-statuses-stat-stages-and-immunities.md#wp44-k22)，对象／条件／入口分支在该条完整给出 | J07/G01 |
| `UserTargetSwapAtkSpAtkStages` | :1647 | 直接交换／复制／反转／归零阶级；方向标记各自更新 | WP44 §7（具名复合／直接重写族） | G07/G08 |
| `UserTargetSwapDefSpDefStages` | :1670 | 直接交换／复制／反转／归零阶级；方向标记各自更新 | WP44 §7（具名复合／直接重写族） | G07/G08 |
| `UserTargetSwapStatStages` | :1693 | 直接交换／复制／反转／归零阶级；方向标记各自更新 | WP44 §7（具名复合／直接重写族） | G07/G08 |
| `UserCopyTargetStatStages` | :1716 | 直接交换／复制／反转／归零阶级；方向标记各自更新 | WP44 §7（具名复合／直接重写族） | G07/G08 |
| `UserStealTargetPositiveStatStages` | :1742 | 计算伤害前夺正阶级；目标归零不以用户接收成功为条件 | WP44 §7（具名复合／直接重写族） | G08 |
| `InvertTargetStatStages` | :1767 | 直接交换／复制／反转／归零阶级；方向标记各自更新 | WP44 §7（具名复合／直接重写族） | G07/G08 |
| `ResetTargetStatStages` | :1795 | 直接交换／复制／反转／归零阶级；方向标记各自更新 | WP44 §7（具名复合／直接重写族） | G07/G08 |
| `ResetAllBattlersStatStages` | :1808 | 直接交换／复制／反转／归零阶级；方向标记各自更新 | WP44 §7（具名复合／直接重写族） | G07/G08 |
| `StartUserSideImmunityToStatStageLowering` | :1826 | 侧保护／顺风／全场防守读取交换 | WP45 主规则；WP44 查询或数值交界 | WP45 建立／重复／到期对照 |
| `UserSwapBaseAtkDef` | :1846 | 战斗原能力值交换／平均，非阶级 | WP47-A 待提取完整招式；WP43读取输入 | 本轮仅定位，不声称验收整招 |
| `UserTargetSwapBaseSpeed` | :1859 | 战斗原能力值交换／平均，非阶级 | WP47-A 待提取完整招式；WP43读取输入 | 本轮仅定位，不声称验收整招 |
| `UserTargetAverageBaseAtkSpAtk` | :1872 | 战斗原能力值交换／平均，非阶级 | WP47-A 待提取完整招式；WP43读取输入 | 本轮仅定位，不声称验收整招 |
| `UserTargetAverageBaseDefSpDef` | :1886 | 战斗原能力值交换／平均，非阶级 | WP47-A 待提取完整招式；WP43读取输入 | 本轮仅定位，不声称验收整招 |
| `UserTargetAverageHP` | :1899 | 双方HP平均与增减，非阶级 | WP46 待提取完整恢复／伤害族 | 本轮仅定位 |
| `StartUserSideDoubleSpeed` | :1921 | 侧保护／顺风／全场防守读取交换 | WP45 主规则；WP44 查询或数值交界 | WP45 建立／重复／到期对照 |
| `StartSwapAllBattlersBaseDefensiveStats` | :1942 | 侧保护／顺风／全场防守读取交换 | WP45 主规则；WP44 查询或数值交界 | WP45 建立／重复／到期对照 |

## 2. 状态文件的有界目录

`007_MoveEffects_BattlerOther.rb` 的 :1–658 状态段含 31 项，逐段读取；计算替代（天气命中、特殊相性）引用WP43，完整变身／动作引用其负责包。

| 源标识 | 起始行 | 主归属 |
| --- | ---: | --- |
| `SleepTarget` | :4 | WP44 §3–6（状态／附带入口） |
| `SleepTargetIfUserDarkrai` | :26 | WP44 §3–6（状态／附带入口） |
| `SleepTargetChangeUserMeloettaForm` | :40 | WP44 §3–6（状态／附带入口） |
| `SleepTargetNextTurn` | :54 | WP44 §3–6（状态／附带入口） |
| `PoisonTarget` | :75 | WP44 §3–6（状态／附带入口） |
| `PoisonTargetLowerTargetSpeed1` | :102 | WP44 §3–6（状态／附带入口） |
| `BadPoisonTarget` | :132 | WP44 §3–6（状态／附带入口） |
| `ParalyzeTarget` | :146 | WP44 §3–6（状态／附带入口） |
| `ParalyzeTargetIfNotTypeImmune` | :169 | WP44 §3–6（状态／附带入口） |
| `ParalyzeTargetAlwaysHitsInRainHitsTargetInSky` | :183 | WP44 §3–6（状态／附带入口） |
| `ParalyzeFlinchTarget` | :200 | WP44 §3–6（状态／附带入口） |
| `BurnTarget` | :217 | WP44 §3–6（状态／附带入口） |
| `BurnTargetIfTargetStatsRaisedThisTurn` | :240 | WP44 §3–6（状态／附带入口） |
| `BurnFlinchTarget` | :249 | WP44 §3–6（状态／附带入口） |
| `FreezeTarget` | :266 | WP44 §3–6（状态／附带入口） |
| `FreezeTargetSuperEffectiveAgainstWater` | :288 | WP44 §3–6（状态／附带入口） |
| `FreezeTargetAlwaysHitsInHail` | :298 | WP44 §3–6（状态／附带入口） |
| `FreezeFlinchTarget` | :308 | WP44 §3–6（状态／附带入口） |
| `ParalyzeBurnOrFreezeTarget` | :325 | WP44 §3–6（状态／附带入口） |
| `GiveUserStatusToTarget` | :339 | WP44 §3–6（状态／附带入口） |
| `CureUserBurnPoisonParalysis` | :385 | WP44 §3–6（状态／附带入口） |
| `CureUserPartyStatus` | :420 | WP44 §3–6（状态／附带入口） |
| `CureTargetBurn` | :500 | WP44 §3–6（状态／附带入口） |
| `StartUserSideImmunityToInflictedStatus` | :512 | WP45侧保护建立／期限；WP44免疫查询 |
| `FlinchTarget` | :532 | WP44 §3–6（状态／附带入口） |
| `FlinchTargetFailsIfUserNotAsleep` | :549 | WP44 §3–6（状态／附带入口） |
| `FlinchTargetFailsIfNotUserFirstTurn` | :565 | WP44 §3–6（状态／附带入口） |
| `FlinchTargetDoublePowerIfTargetInSky` | :579 | WP44 §3–6（状态／附带入口） |
| `ConfuseTarget` | :594 | WP44 §3–6（状态／附带入口） |
| `ConfuseTargetAlwaysHitsInRainHitsTargetInSky` | :618 | WP44 §3–6（状态／附带入口） |
| `AttractTarget` | :635 | WP44 §3–6（状态／附带入口） |

余下标识已定位，**不因与状态同文件而算作本包完成**：

| 源标识 | 起始行 | 负责范围 |
| --- | ---: | --- |
| `SetUserTypesBasedOnEnvironment` | :659 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `SetUserTypesToResistLastAttack` | :721 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `SetUserTypesToTargetTypes` | :762 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `SetUserTypesToUserMoveType` | :799 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `SetTargetTypesToPsychic` | :833 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `SetTargetTypesToWater` | :855 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `AddGhostTypeToTarget` | :877 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `AddGrassTypeToTarget` | :898 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `UserLosesFireType` | :919 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `SetTargetAbilityToSimple` | :939 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `SetTargetAbilityToInsomnia` | :973 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `SetUserAbilityToTargetAbility` | :1007 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `SetTargetAbilityToUserAbility` | :1047 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `UserTargetSwapAbilities` | :1086 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `NegateTargetAbility` | :1155 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `NegateTargetAbilityIfTargetActed` | :1178 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `IgnoreTargetAbility` | :1196 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `StartUserAirborne` | :1206 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `StartTargetAirborneAndAlwaysHitByMoves` | :1229 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `HitsTargetInSky` | :1260 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `HitsTargetInSkyGroundsTarget` | :1268 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |
| `StartGravity` | :1299 | WP45重力；WP43/44有效查询消费 |
| `TransformUserIntoTarget` | :1338 | WP47-A/B 类型／特性／浮空／变身完整族；WP43/44只引用实际输入／守卫 |

## 3. 当前PBS样本（文本数据确认）

每条只记录用于与效果身份核对的字段，未执行编译器或生成器；显示描述不是行为证据。

| 数据ID | 类型／类别 | 效果标识 |
| --- | --- | --- |
| SWORDSDANCE | NORMAL／Status | `RaiseUserAttack2` |
| GROWL | NORMAL／Status | `LowerTargetAttack1` |
| BELLYDRUM | NORMAL／Status | `MaxUserAttackLoseHalfOfTotalHP` |
| SHELLSMASH | NORMAL／Status | `LowerUserDefSpDef1RaiseUserAtkSpAtkSpd2` |
| SWAGGER | NORMAL／Status | `RaiseTargetAttack2ConfuseTarget` |
| TOPSYTURVY | DARK／Status | `InvertTargetStatStages` |
| HAZE | ICE／Status | `ResetAllBattlersStatStages` |
| PSYCHUP | NORMAL／Status | `UserCopyTargetStatStages` |
| TOXIC | POISON／Status | `BadPoisonTarget` |
| YAWN | NORMAL／Status | `SleepTargetNextTurn` |
| REST | PSYCHIC／Status | `HealUserFullyAndFallAsleep` |
| ATTRACT | NORMAL／Status | `AttractTarget` |

状态与阶级全局名录来自已读Status／Stat数据定义；阶段型特性／道具的完整效果目录由WP48/49/50继续提取。此表只给本包实际范围与负责包，不能据此宣称所有域外功能已经实现或验证。
