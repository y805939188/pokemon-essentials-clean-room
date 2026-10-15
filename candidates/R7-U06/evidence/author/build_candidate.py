"""Create four complete frozen-B mirrors with bounded prose edits; no game code."""
from pathlib import Path
import subprocess

B = 'e646432c644dec04d306842cc5a559a29c718fbc'
ROOT = Path(__file__).resolve().parents[4]
PREFIX = ROOT / 'candidates/R7-U06'

def read(path):
    return subprocess.check_output(['git', 'show', B + ':' + path], cwd=ROOT).decode('utf-8')

def put(path, text):
    target = PREFIX / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(text.encode('utf-8'))

def once(text, old, new):
    assert text.count(old) == 1, old
    return text.replace(old, new, 1)

path = 'deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md'
text = read(path)
text = once(text, '减伤果消耗 → 蒸汽机等 → 再濒死。',
    '减伤果消耗 → [蒸汽机的直接每击速度请求](../combat-requirements/wp49-ability-phase-triggers.md#611-蒸汽机的直接每击速度请求)等 → 再濒死。')
text = once(text, '每次基底求值加一份数据 P，普通单目标第 1/2/3 击为 P/2P/3P；',
    '每次基底求值加一份数据 P，普通单目标且三击均到达基底求值时，第 1/2/3 次求值为 P/2P/3P；画皮/结冻头吸收的成功击不求基底、不推进累计威力，仍占计划/成功击数；')
text = once(text, '快照名单长度为计划次数，逐击按队伍顺序取一名，其物种基础攻击值 b 决定基底 5＋⌊b/10⌋；',
    '快照名单长度为计划次数；仅每次实际普通基底求值才按队伍顺序取并消费一名，其物种基础攻击值 b 决定基底 5＋⌊b/10⌋。画皮/结冻头吸收的成功击仍占计划/成功击数，但不消费参与者；后续首次普通求值仍取尚未消费的首名。无形态吸收时保持原参与者序列，替身仍进行普通求值并推进；')
put(path, text)

path = 'deliverables/final-specification-set/combat-requirements/wp49-ability-phase-triggers.md'
text = read(path)
text = once(text, '### 6.2 招式结束的使用者能力', '''### 6.1.1 蒸汽机的直接每击速度请求

STEAMENGINE 是直接每击后段规则，位置在招式附效、额外畏缩及减伤果消费之后、随后目标与 U 的濒死检查之前。它与更早的 OnBeingHit 受击能力调用分开，不增加登记族或（族，能力）配对计数。

本次已确定的计算类型为火或水时，依本击实际目标列表顺序逐个检查：排除 unaffected、本击 calcDamage 为 0 或本击替身的目标；其余要求当下普通有效的 STEAMENGINE，并经 WP44 的中央可升速度资格，才以拥有者自身为来源请求速度＋6。普通有效性仍拒倒下、胃液或有效气体压制；不另增“真实肉身 HP 正损失”的门。没有独立的模式破坏者或强行屏蔽门，不能把强行对附效、整招后段二/三的抑制套到此直接尾部。

这是增量请求，沿中央资格、夹限与反馈：原阶级−4→＋2、0→＋6、＋5→＋6，已＋6不再升；原速度数值不因升阶重写。多击每次到此位置均重查当前能力、伤害状态和阶级，不锁定首击资格；在当前单一能力前提下，不构造同时具有蒸汽机、唱反调或单纯的例子。未到达此反应的更早取消/失败不补升阶；后续故障也不自动撤销已到的 PP、HP 或阶级写入，不保证宿主恢复。

### 6.2 招式结束的使用者能力''')
put(path, text)

path = 'deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md'
text = read(path)
text = once(text, '## AB：特性参与计算、免疫与有效性', '''### R7-U06：形态吸收与基底求值

全部 SOURCE_STATIC／DERIVED_VECTOR，execution＝NOT_EXECUTED。共同前提：机制世代8、合法真实槽且当前PP正，普通单目标，使用/服从/目标/命中等前门通过；无替身、模式破坏者、其它能力/物品反应、睡冻/换人、重入/插件/演出故障，双方非变身且足够存活到全部指定击。BU夹具为SNEASEL合法BEATUP，业主合格队伍恰按顺序[SNEASEL基础攻95、MAGIKARP基础攻10]、均无真实异常，目标MIMIKYU0/DISGUISE；TK夹具为合法TRIPLEKICK(P10)使用者对EISCUE0/ICEFACE，三次命中均过。形态改变后的攻防仍读当下值；14/6/10/20/30均为基底，不是计算伤害或实际HP损失。各行独立改变所列条件，未列门保持共同前提。

| ID | 输入／独立变化 | 静态预期 |
| --- | --- | --- |
| C01-M09-BU-ABS | BU夹具，首击画皮吸收 | 计划2；首击C1、直接hpLost0，不消费参与者，破皮与当代额外总HP整除8照旧；存活续击首次求值取SNEASEL基底14，总成功击2。MAGIKARP基底6本次未求值 |
| C01-M09-BU-CONTROL | BU仅改目标起始已破皮形态1 | 两次普通基底14、6，计划与成功击数仍2 |
| C01-M09-TK-ABS | TK夹具，首击结冻头吸收 | 首击C1/直接hpLost0，切形1但累计威力仍0；后两击基底10、20，总成功击3，不补一击重试 |
| C01-M09-TK-CONTROL | TK仅改目标起始形态1、无形态吸收 | 三次基底10、20、30；命中规则仍独立，SKILLLINK的既有门不改 |
| C01-M09-SUB-BU | 从BU-CONTROL独立加未绕过的替身吸收首击，双方仍可续击且无其它改写 | 首击仍求普通基底14并消费首名；第二击普通基底6，不套形态早返；目标个体HP与替身损失分别记录 |
| C01-M09-SUB-TK | 从TK-CONTROL独立加未绕过的替身吸收首击且能续击 | 普通基底仍依次10、20、30，替身不会冻结累计威力 |
| C01-M09-MISS-STOP-FIRST-BU | BU仅改U命中阶级−1、T闪避0，无必中，首击命中抽值99而失败 | 无基底求值、成功击0，止于该门；只保留已到的PP/历史前缀，不消费首名 |
| C01-M09-MISS-STOP-FIRST-TK | TK首击命中抽值99而失败，无有效SKILLLINK | 无基底求值、成功击0，不补后击 |
| C01-M09-MISS-STOP-LATER | TK首击吸收，第二击命中失败，无有效SKILLLINK | 仅吸收/切形及成功击1的前缀；没有10/20基底，失败不重试，不撤销已到前缀 |
| C01-M09-MISS-STOP-FAINT-U | BU或TK首击吸收后，仅令独立反应使U倒下 | 后续击停止，不承诺14或10/20；已到吸收/形态/HP/PP保持 |
| C01-M09-MISS-STOP-SLEEP | 同上仅令U进入真实睡眠且未被治愈 | 成功击返回后的停止门阻续击，不补后续基底；不是重新普通服从/PP检查 |
| C01-M09-MISS-STOP-FREEZE | 同上仅令U进入真实冰冻且未被治愈 | 独立冰冻停止门阻续击，只保留已到前缀 |
| C01-M09-MISS-STOP-FAINT-T | 同上仅令唯一目标在吸收后的独立后段倒下 | 全目标倒下停止门阻续击，不因计划尚余而补击 |
| R7-U06-M09-CANCEL | 在上游命令取消，尚未建立本次BU/TK使用 | 不建立本次计划/基底消费，不补造扣PP；进入本族执行后没有另一个UI取消步骤 |
| R7-U06-M09-PREFIX | 独立令故障发生在已吸收/切形/HP前缀之后、下次求值之前；另令故障发生在后续一次基底/HP提交之后 | 前者不补后续求值或HP，后者只保留已到写点；二者均不回滚已扣PP，不保证宿主恢复或完成计划 |

原MH02/MH06普通向量保留；C01-M09-SUB与C01-M09-MISS-STOP的分项覆盖如上，固定伤害覆盖与AI估量不扩入本组。

## AB：特性参与计算、免疫与有效性''')
put(path, text)

path = 'deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md'
text = read(path)
text = once(text, '## AI：动作选择与技能', '''### R7-U06：蒸汽机直接每击反应

全部 SOURCE_STATIC／DERIVED_VECTOR，execution＝NOT_EXECUTED，主合同 WP49 §6.1.1，时序接 WP46 §2.1。共同夹具S：机制世代8、普通单打，水类型U合法WATERGUN槽、当前PP5（总PP仍25）、L20/特攻33；T为存活非变身ROLYCOLY，L50、岩、H/h100/100、当前特防55/原速度35/速度阶级0、当前普通有效STEAMENGINE。所有行动/服从/范围/保护/免疫/命中门通过，非会心、最大波动，单目标/相性2；无本例外天气/场地/物品/徽章或其它倍率、替身/压制、反射/抢夺、换人/能力或阶级中间改写、重入/插件或反馈故障。各变体独立，类型/伤害改变时不沿用水夹具的HP82。

| ID | 输入／独立变化 | 静态预期 |
| --- | --- | --- |
| R7-U06-SE01 | S正常水命中 | 普通基础量6，水本系与相性合成×3，T先损18至82、U PP5→4；随后直接尾部速度0→＋6，升阶标记真；原速度35不改，下次普通速度查询140 |
| R7-U06-SE02 | 独立合法火招命中，同样非零calcDamage、无替身/无效且T仍活 | 在附效/额外畏缩/减伤果消费之后请求速度＋6，然后后续濒死检查；不将18点水伤害复制成火伤害 |
| R7-U06-SE03 | S仅改T能力为默认HEATPROOF，仍用水 | 无此速度反应，阶级0/普通速度35；耐热火倍率不作用水，原水伤害/PP前缀保持 |
| R7-U06-SE04 | 独立合法非火/水招造成非零计算伤害，T仍活；另以原火/水招经合法输电令本次计算类型为电且所有门通过 | 两者均无蒸汽机反应；按本次计算类型判门，不按原数据火/水判定；伤害各自另算 |
| R7-U06-SE05 | S仅加未绕过的替身，本击伤害由替身承受 | 即使calcDamage非零，替身门独立拒升；实际替身损失与个体HP分开，先前PP不退款 |
| R7-U06-SE06 | S独立改保护或普通失手，使该目标unaffected | 不向该目标请求升速；保留实际已到的PP/历史前缀，不补伤害或退款 |
| R7-U06-SE07 | 条件化已经到达直接尾部、本击calcDamage0，其余候选门满足 | 非零计算伤害门独立拒绝；这是该入口守卫对照，不声称普通正伤害夹具能自然生成0 |
| R7-U06-SE08 | S仅改为胃液压制；另仅改为场上存在普通有效气体 | 当下普通有效性各自拒，不升速；不把蒸汽机当不可压制能力 |
| R7-U06-SE09 | 独立合法火/水命中使T在此尾部已倒下 | 普通能力有效性拒，无速度请求；更早允许濒死的OnBeingHit不能替代本处门 |
| R7-U06-SE10 | S仅将速度初阶分别改−4、＋5、＋6 | 分别−4→＋2（原速35的后继普通查询70）、＋5→＋6（实增1）、＋6不再升；是请求＋6而非赋绝对＋6 |
| R7-U06-SE11 | 合法普通两击火或水，各击T仍活，无替身/压制或其它阶级变化 | 首击0→＋6；续击独立重查，封顶不再增。若两击间合法能力改变/压制，第二击按其当下能力拒，不锁定首击资格 |
| R7-U06-SE12 | S仅令U有效模式破坏者，本次类型仍水，其余门通过 | 本直接尾部不被独立模式破坏者门屏蔽，仍可请求＋6，中央资格保持 |
| R7-U06-SE13 | 独立默认DARMANITAN有效SHEERFORCE、合法EMBER且附效数据正，T仍为有效蒸汽机并存活，无其它改写 | 强行按既有门抑制附效及具名整招后段二/三；本每击直接尾部仍可请求速度＋6，不将T设为同时有单纯/唱反调 |
| R7-U06-SE14 | 上游取消尚未建立使用；另在更早失败/故障处停止于反应之前 | 不补蒸汽机请求；只保留各路径已到的PP/HP/记录，不凭取消补扣或退款 |
| R7-U06-SE15 | 独立在中央速度写入后、后段反馈正常返回前发生故障 | 保留已写阶级和已到PP/HP前缀；反馈/后续濒死或宿主恢复不能补完成，不宣称行为故障注入已执行 |

GR7-M10-001-C1–C7分别由SE01/02、SE04、SE05–09、SE10、SE11、SE12/13、SE14/15覆盖。原AB全部31条及后续AI/AE/BE/CE各行保持，登记48族267配对与WP48的27族148配对不因直接规则而增加。

## AI：动作选择与技能''')
put(path, text)
print('Created four complete frozen-B mirrors; WP43 conditional edit not used.')
