# 备份作者数据的字段合同

以下为基于 Essentials v21.1、标签后 23 个提交的参考快照中，四代备份输入的静态解释。作者数据的语法记号沿用[内容身份与数据模式](../spec/core/content-identity-and-schema.md)。这些备份须显式选用，物种、形态、显示和遭遇还分别依赖有效的登记项与宿主输入。各字段的含义是静态结论，整份备份的编译与实际效果未验证。

## 记录身份

- 基础物种使用新的作者标识。仅有备份记录不会激活它。
- 形态要求已登记基础物种与正形态号。按同一世代的基础资料解释该形态。
- 显示指标的身份为登记物种与可选的正形态号。省略按 0，显式给出非空的 0 被拒。
- 遭遇节将地图和版本文本按该入口的整数转换读取，省略版本取 0。相同地图与版本的重复记录另受重复键规则约束。

## 字段、默认值与继承

| 字段 | 适用输入 | 作者语法 | 缺省值 | 形态或专用记录的处理 | 用途 |
| --- | --- | --- | --- | --- | --- |
| Name | BASE_ONLY | s | Unnamed | 取基础值 | 物种名可经翻译后显示，与内容身份分别处理。 |
| FormName | BASE_AND_FORM | q | nil | 形态自有默认 | 形态名称独立，不继承基础标签；图鉴显示别名与原形态检查有不同消费者。 |
| PokedexForm | FORM_ONLY | u | record form | 形态自有默认 | 只改图鉴呈现别名，保存形态、实际数据、战斗形态与资源请求仍按各自身份。 |
| MegaStone | FORM_ONLY | e:Item | nil | 形态自有默认 | Mega 候选所需的登记物品。道具分类旗标与战中许可另有门槛。 |
| MegaMove | FORM_ONLY | e:Move | nil | 形态自有默认 | 已知所需招式可独立满足候选条件，当前 PP 不参与此判断。 |
| UnmegaForm | FORM_ONLY | u | 0 | 形态自有默认 | 候选的还原形态须匹配当前简化形态，当前 Mega 记录定义还原目标。 |
| MegaMessage | FORM_ONLY | u | 0 | 形态自有默认 | 选择该候选的提示，不单独授予战斗许可。 |
| Types | BASE_AND_FORM | *e:Type | [NORMAL] | 复制基础列表/映射 | 登记属性依序去重、除去空项，无固定两属性上限；个体查询得到独立列表。 |
| BaseStats | BASE_AND_FORM | vvvvvv | six main stats 1 | 复制基础列表/映射 | 依次为 HP、攻击、防御、速度、特攻、特防。按属性身份计算。 |
| GenderRatio | BASE_ONLY | e:GenderRatio | Female50Percent | 取基础值 | 单一性别以缺少雌性几率表示，否则用个人识别值低字节判阈值。 |
| GrowthRate | BASE_ONLY | e:GrowthRate | Medium | 取基础值 | 六条成长曲线之一，查等级与经验先用表、后用公式。 |
| BaseExp | BASE_AND_FORM | v | 100 | 取基础值 | 正的基础经验是战斗经验计算输入。 |
| EVs | BASE_AND_FORM | *ev:Stat | six main yields 0 | 复制基础列表/映射 | 正的指定属性产出，重复属性后写覆盖；查询给出六项。 |
| CatchRate | BASE_AND_FORM | u | 255 | 取基础值 | 捕获难度的输入，最终成功还取决于捕获规则。 |
| Happiness | BASE_AND_FORM | u | 70 | 取基础值 | 初始亲密度按原值赋给新个体，作者输入无 255 上限，之后常规变更成功后限在 0–255。 |
| Abilities | BASE_AND_FORM | *e:Ability | [] | 复制基础列表/映射 | 通常特性有顺序，个人识别值奇偶选择的索引缺席时取首个。 |
| HiddenAbilities | BASE_AND_FORM | *e:Ability | [] | 复制基础列表/映射 | 隐藏特性从索引 2 起；所选隐藏项缺席时回到通常特性的奇偶选择。 |
| Moves | BASE_AND_FORM | *ue:Move | [] | 空时从基础嵌套列表复制 | 等级/招式对按顺序保留含等级 0 与重复；重置取最新重复项、最多四个。进化按独立入口学等级 0 和当前等级的招式。 |
| TutorMoves | BASE_AND_FORM | *e:Move | [] | 复制基础列表/映射 | 机器或教学资格按登记身份有序给出，满足资格本身不会学会或扣物。 |
| EggMoves | BASE_AND_FORM | *e:Move | [] | 复制基础列表/映射 | 蛋招式原表与祖先回退查询分开；不能据此将整表加入重学候选。 |
| EggGroups | BASE_AND_FORM | *e:EggGroup | [Undiscovered] | 复制基础列表/映射 | 登记蛋组决定配对与角色，拥有蛋组不保证给定的一对相容。 |
| HatchSteps | BASE_AND_FORM | v | 1 | 取基础值 | 正孵化步数；创建蛋的步数赋值与后续孵化回调分开。 |
| Incense | BASE_ONLY | e:Item | nil | 取基础值 | 幼体阶段的登记香决定是否向前身递归；PICHU 没有通用香要求。 |
| Offspring | BASE_AND_FORM | base:*s then final Species enumeration; form:*e:Species | [] | 复制基础列表/映射 | 替代后代有序保留，同一身份重复的次数影响抽样权重。 |
| Height | BASE_AND_FORM | f | 1 tenth metre | 取基础值 | 十进制米乘 10 后舍入，最低 1，查询与图鉴以十分之一米为单位。 |
| Weight | BASE_AND_FORM | f | 1 tenth kilogram | 取基础值 | 十进制千克乘 10 后舍入，最低 1，查询与图鉴以十分之一千克为单位。 |
| Color | BASE_AND_FORM | e:BodyColor | Red | 取基础值 | 十项描述标识之一，可翻译；与遭遇区域独立。 |
| Shape | BASE_AND_FORM | e:BodyShape | Head | 取基础值 | 十四项体型标识有顺序并关联图标，实际图像是否存在另验。 |
| Habitat | BASE_AND_FORM | e:Habitat | None | 取基础值 | 十项描述标识；区域页可见性由遭遇和地图元数据决定。 |
| Category | BASE_AND_FORM | s | ??? | 取基础值 | 分类文本独立翻译，然后由图鉴拥有门控制呈现。 |
| Pokedex | BASE_AND_FORM | q | ??? | 取基础值 | 图鉴文字在行预处理后读取，井号注释可能先移除，翻译后显示可异于原始文字。 |
| Generation | BASE_AND_FORM | i | 0 | 取基础值 | 带符号的首次世代描述，不激活备份也不选择机制常量。 |
| Flags | BASE_AND_FORM | *s | [] | 复制基础列表/映射 | 标志不区分大小写并按完整标识比较；首个 DefaultForm_N 控制基础形态。母系、永恒之石与传说标志各由不同规则消费。 |
| WildItemCommon | BASE_AND_FORM | *e:Item | [] | 三组全省略才一起继承 | 普通、少见、稀有三组中任一显式给出就抑制全部三组的基础继承；三个非空池相同可保证对应持物。 |
| WildItemUncommon | BASE_AND_FORM | *e:Item | [] | 三组全省略才一起继承 | 三组以单次累积抽选分支取值，普通权重 50/5/1、相应领队效果 60/20/5。 |
| WildItemRare | BASE_AND_FORM | *e:Item | [] | 三组全省略才一起继承 | 空池的抽选可能为空；成功写入按登记道具身份校验，与能否持有的另一标志分开。 |
| Evolutions | BASE_AND_FORM | base:*ses; form:*ees | [] | 空时从基础嵌套列表复制 | 复数进化列表按模式顺序先于单数列表，普通复数属性重复书写以后一次为准。 |
| Evolution | BASE_AND_FORM | base:^seS; form:^eeS | [] | 空时从基础嵌套列表复制 | 单数进化三元组可重复并按出现顺序追加在复数列表后，参数按方法类型转换，None 与反向前身不参加实际触发检查。 |
| BackSprite | METRICS | ii | [0,0] | 显示记录自有缺省 | 偶数战位背面绘制的 x、y 均乘 2；图鉴背面另取垂直值乘 2。 |
| FrontSprite | METRICS | ii | [0,0] | 显示记录自有缺省 | 奇数战位正面绘制 x、y 均乘 2；孵化与交换直接请求战位 1。 |
| FrontSpriteAltitude | METRICS | i | 0 | 显示记录自有缺省 | 对手正面 y 减高度的两倍。四代所查 2,696 个形态绘制输入都省略该字段。 |
| ShadowX | METRICS | i | 0 | 显示记录自有缺省 | 阴影分支只移动对手阴影横坐标，增量为值的两倍，不作通常身体偏移。 |
| ShadowSize | METRICS | u | 2 | 显示记录自有缺省 | 物种/形态专用影子优先，随后才按通用尺寸选影子；专用影子不使用编辑后的通用尺寸。 |
| ENCOUNTER_TYPE | ENCOUNTER | registered EncounterType + optional to_i chance | type trigger chance | 遭遇专用规则 | 某遭遇类型首次省略概率取类型默认，重复类型替换已有槽位，重复时省略概率则保留前次概率。 |
| SLOT | ENCOUNTER | positive weight, Species, min, optional max | max=min | 遭遇专用规则 | 物种/形态须登记，等级 1 至最大等级，最小不大于最大。相同物种及范围先合并，按权重降序、物种名升序排序，再在该表内按权重抽选，等级在该槽位的最小值至最大值间选择，含两端。 |

## 版本样例

- 第五、六世代地图 75 的特定槽位使用基础物种。第七、八世代对应槽位出现 GEODUDE_1、RATTATA_1、DIGLETT_1、MEOWTH_1、SANDSHREW_1、VULPIX_1。四代中地图 5 的版本 0 与 1 各有不同的陆地/夜间表，地图 39 和 44 有 SHELLOS_1。最高等级省略时为定级，同种身份的不同等级范围仍是不同槽位。
- 四套显示资料各有 674 行。背面 y 与阴影横移均为 0，通用影子尺寸有 1、2、3，部分正面 y 为负；高度省略为 0。较新物种缺指标时仍需依对应的惰性创建规则处理。
- Mega 胡地的特防在第六世代样本为 95，在第七世代为 105。第五世代洛托姆形态 1–5 省略能力覆盖，第六世代显式提供；相邻版本的覆盖不可用于补空。第七世代小卡拉卡拉形态 1 省略名称与属性，含世代与进化；MINIOR 形态 1–6 在该备份无记录。
- 第八世代坚盾剑怪刀剑形态的攻击和特攻为 140。Mega 波士可多拉省略 BaseExp，取本世代基础。Calyrex 的合体形态与资料依赖分别读取；不能从 Alcremie 形态 7–62 的图鉴别名推断这份备份还含 1–6。
- 第五世代无 Mega 条目。第六至八世代分别用当代属性元组；第八世代喵喵的形态差异见[个体状态与兼容边界](../spec/creatures/item-identity-and-related-compatibility.md)。
