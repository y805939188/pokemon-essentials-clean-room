"""M06 review bookkeeping only; no reference behavior is executed or translated."""
import json
import re
import subprocess
from pathlib import Path
from datetime import datetime, timezone

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
REF = Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
B = '1f36475d22120a0d1175967d5b17d71fe8311d88'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REVIEWER = 'M06 / thread 01a12fe0-a4a3-75a0-87bd-03c04ac176c8'
FORMAL = 'deliverables/final-specification-set/'

def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

S = {
 'growth':'Data/Scripts/010_Data/001_Hardcoded data/001_GrowthRate.rb',
 'pokemon':'Data/Scripts/014_Pokemon/001_Pokemon.rb',
 'shadow':'Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb',
 'exp':'Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb',
 'itemutil':'Data/Scripts/013_Items/001_Item_Utilities.rb',
 'relearn':'Data/Scripts/016_UI/022_UI_MoveRelearner.rb',
 'evolution':'Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb',
 'evoui':'Data/Scripts/016_UI/001_Non-interactive UI/004_UI_Evolution.rb',
 'trade':'Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb',
 'daycare':'Data/Scripts/012_Overworld/007_Overworld_DayCare.rb',
 'hatch':'Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb',
 'species':'Data/Scripts/010_Data/002_PBS data/008_Species.rb',
 'forms':'Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb',
 'world':'Data/Scripts/012_Overworld/001_Overworld.rb',
 'metadata':'Data/Scripts/012_Overworld/002_Overworld_Metadata.rb',
 'start':'Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',
 'wild':'Data/Scripts/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb',
 'modifiers':'Data/Scripts/012_Overworld/002_Battle triggering/004_Overworld_EncounterModifiers.rb',
 'roam':'Data/Scripts/012_Overworld/002_Battle triggering/005_Overworld_RoamingPokemon.rb',
 'radar':'Data/Scripts/013_Items/005_Item_PokeRadar.rb',
 'catch':'Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb',
 'balls':'Data/Scripts/011_Battle/007_Other battle code/010_Battle_PokeBallEffects.rb',
 'peer':'Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb',
 'ballmenu':'Data/Scripts/013_Items/003_Item_BattleEffects.rb',
 'balluse':'Data/Scripts/011_Battle/001_Battle/006_Battle_ActionUseItem.rb',
 'damage':'Data/Scripts/011_Battle/003_Move/002_Move_Usage.rb',
 'faint':'Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb',
 'encdata':'Data/Scripts/010_Data/002_PBS data/013_Encounter.rb',
 'enctype':'Data/Scripts/010_Data/001_Hardcoded data/013_EncounterType.rb',
 'compiler':'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',
 'balance':'Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb',
 'settings':'Data/Scripts/001_Settings.rb',
 'battlecfg':'Data/Scripts/002_BattleSettings.rb',
 'pbs':'PBS/pokemon.txt', 'pbforms':'PBS/pokemon_forms.txt',
 'items':'PBS/items.txt', 'abilities':'PBS/abilities.txt', 'encounters':'PBS/encounters.txt'
}
P = {
 '30':'creature-rpg/wp30-growth-learning-and-friendship.md',
 '31':'pokemon-rules/wp31-basic-evolution.md',
 '32':'pokemon-rules/wp32-contextual-trade-and-post-battle-evolution.md',
 '32a':'pokemon-rules/wp32-context-inputs-and-scenarios.md',
 '33':'creature-rpg/wp33-daycare-and-breeding-session.md',
 '34':'pokemon-rules/wp34-inheritance-and-offspring.md',
 '35':'creature-rpg/wp35-eggs-and-hatching.md',
 '36':'creature-rpg/wp36-wild-encounters-and-modifiers.md',
 '37':'pokemon-rules/wp37-roaming-and-poke-radar.md',
 '38':'pokemon-rules/wp38-capture-and-receiving.md',
 'tgr':'test-catalog/creature-rpg-wp27-28-29-30-33.md',
 'tbr':'test-catalog/pokemon-rules-wp19-21-22-23-34.md',
 'teg':'test-catalog/creature-rpg-wp35-36-57-64-68.md',
 'tcp':'test-catalog/pokemon-rules-wp31-32-37-38.md',
 '20':'creature-rpg/wp20-hp-status-moves-helditem.md'
}

def src(key, locus, fact):
    return {'path': S.get(key, key), 'lines_or_symbol': locus, 'fact': fact, 'commit': R}

def spec(key, locus, fact='本轮仅核此合同／向量，不签全文件通过'):
    return {'path': FORMAL + P.get(key, key), 'lines_or_section': locus, 'fact': fact, 'commit': B}

caps = []
def cap(wp, description, sources, specs, branches, limits, not_checked, classification=None, finding=False, status='supported'):
    i = len(caps) + 1
    c = {
      'capability_id': f'GR4-CAP-M06-{i:03}', 'module':'M06', 'description':description,
      'source_anchors':[src(*x) for x in sources], 'spec_anchors':[spec(*x) for x in specs],
      'entry_and_preconditions':branches[0], 'configuration_data_host_limits':limits,
      'reviewer':REVIEWER, 'checked_branches_boundaries':branches,
      'evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'],
      'execution_status':'NOT_EXECUTED',
      'material_availability':{'scripts_and_named_data':'available_read_only', 'graphics_audio_maps_complete_demo':'unavailable_shared_baseline', 'host':'not_established'},
      'status':'partial' if finding else status,
      'reason':('正文主规则获静态支持，但 BR18 含不符合持物前提的五项分支。' if finding else '仅上述有界分支 supported_static；不表示运行通过或穷尽本能力。'),
      'related_findings':['GR4-M06-001'] if finding else [], 'history_links':[],
      'not_checked':not_checked, 'classification':classification or ['Creature-RPG','Pokémon Rules'],
      'primary_owner':f'WP{wp}', 'projection':'M06 主责行为；跨包只核本项列明的输入／输出接点'
    }
    caps.append(c)

cap('30','成长曲线查表／表外与反向换算',
 [('growth','41–71,77–188','先最大等级钳制，表内优先；Erratic/Fluctuating表外另有公式；经验非法分支诊断求值异常。'),('pokemon','190–237','原始经验设置清等级缓存，不做辅助入口钳制。')],
 [('30','§3、§8.1–2'),('tgr','GR-01–07')],
 ['合法登记曲线；默认最大100与作者变体101分列。','抽核六曲线L1/L50/L100和Medium边界；Erratic/Fluctuating L101；非法等级与非法经验不同失败面。'],
 '默认100；600个表值未逐值重算；未执行Ruby公式。', ['全部600表值的独立逐项算术验证','非单调表外曲线的完整运行后果'])
cap('30','战斗经验分配、逐级取整与EV先行',
 [('exp','5–224','内部/经验开关，参与/共享/全队，先EV，零基础份额早退，整数除5先于缩放，升级学习。'),('battlecfg','104–117','世代控制缩放、均分、训练家加成、捕获经验。')],
 [('30','§4'),('tgr','GR-08–24、GR-45–48')],
 ['内部正常战斗，有参与记录、玩家有效归属与未满经验个体。','抽核a78→13、零份额早退、参与共享兼任分别取整、异语言/护符/持物/亲密顺序。','当前在场才有升级友好；EV先写且零经验不回滚。'],
 '战斗资格及数学静态；Shadow提交只读此调用侧，完整覆盖继承M04/Shadow责任。', ['所有持物/能力覆写','Shadow完整净化流程','回放随机及真实多方战斗'])
cap('30','显式等级／经验辅助与经验道具提交时点',
 [('itemutil','132–204,223–327','钳制、差量先提示再写；同级增经验仍有维生素友好，减经验无；道具qty−1在辅助前。'),('pbs','237–262 (CATERPIE)','Medium、基础经验39供具名对照。')],
 [('30','§5.1–5.3，138–148'),('tgr','U03-EX01–05，244–252')],
 ['普通非蛋非Shadow、有效场景，消息/刷新正常返回、无插件。','E27→28、28→27、27→27；0请求−1；999999请求1000001。','跨等级才学招/查进化；等级辅助HP基础1特例与经验辅助不混同。'],
 '维生素h80→85另需非取得地图、非豪华球、无铃、软上限关。', ['宿主提示异常恢复','调试原始写入全流程'])
caps[-1]['history_links']=[{'id':'GR3-M06-001','relation':'regression_check','result':'supported_static; old CLOSED preserved','details':'regression.json'}]
cap('30','学习、满槽替换与重学候选／取消',
 [('itemutil','582–638','空槽学习与满槽机器教学的PP/友好分支不同，蛋调试例外、Shadow拒绝。'),('relearn','150–185','等级候选、额外first_moves前置去重，拒绝教学返回选择循环，成功才计数。'),('pokemon','625–704','静默学习保留已有对象移尾；首次记录单独管理。'),('exp','229–270','战斗版同步当前战斗者，并在招式改变后复查形态。')],
 [('30','§6.1–6.3'),('tgr','GR-25–34、GR-49、GR-52')],
 ['有效个体及招式、非空候选且UI构造正常为交互取消的前提。','机器替换保留旧PP开/关；空槽不进入满槽机器友好分支。','first_moves与等级重复身份只出现一次；配置关不补物种整张蛋招表。'],
 '提醒额外招式默认gen≥6开，保旧PP仅gen5；空UI故障未追全验证库链。', ['HM遗忘选择器完整UI','空提醒首次绘制严格验证完整调用链','TR背包/个体道具入口的记录差异'])
cap('30','友好度档位、正修正与软上限',
 [('pokemon','916–969','方法档位，地图/豪华球加1后铃×1.5取整；179软上限例外evberry。'),('shadow','108–112','Shadow心阶段≥4阻止友好变化。'),('world','69–79','128步后对可战斗队伍逐个50%行走友好。')],
 [('30','§7–8'),('tgr','GR-35–42')],
 ['普通个体h在0..255；Shadow另有覆盖守卫。','h80同地图豪华球铃行走→86；h175无加成软上限→177；h180正值被截为0；负值不受正修正。'],
 '软上限默认关闭；步进来源已读普通迈步，强制移动另分流。', ['所有道具调用者','亲密战斗效果','非合法h直接赋值后果'])
cap('31','五族进化守卫与首目标顺序',
 [('pokemon','976–1059','五检查共守卫蛋/Shadow/永石/BattleBond，按条目首目标；事件触发true不等于提交。'),('evolution','65–676','基本、时间天气、持物、交换、战后、事件各身份判定。'),('species','277–284','前身与None按消费者过滤。')],
 [('31','§3–4'),('32','§2、§7'),('tcp','BE07–10、BE29–35；CX27–29')],
 ['合法进化登记和必要上下文；按家族入口检查。','守卫阻止所有家族；EventAfterDamageTaken可设标志但返回假；事件工具取消后仍true。','HoldItem任意升级元数据本身不比较刚升级；None与Shedinja后置不作目标。'],
 '对时间/地图缺失只按具体短路；全部条件身份已读，未穷尽跨组合。', ['全部默认数据条目的可达性','未知方法注册校验全链','所有时间/天气消费者'])
cap('31','进化提交、取消与Shedinja额外个体',
 [('evoui','5–20,84–128,195–254','副本先追加；主成功动作先于换物种，随后清准备、图鉴、0/当前等级学招。'),('evolution','257–275,371–451','Shedinja队位+普通球；持物后置匹配目标且仍持物才消耗。'),('pbs','7679–7680','NINCADA的Ninjask与Shedinja条目。')],
 [('31','§5–8'),('tcp','BE11–26')],
 ['演出完成且媒体/回调正常；允许取消入口与不可取消入口分开。','队5有普通球追加副本；满队或无球跳过副本；动作发生在主物种改变之前。','取消不进入成功序列；成功后新招被拒绝不撤销物种。'],
 '仅写入和调用时序静态；未验证像素、精确动画时长。', ['图鉴提前关闭重复dispose宿主行为','复制字段的完整深浅语义','全部形态更替组合'])
cap('32','交换情境条件与收到者提交',
 [('trade','157–168,217–242','收到者检查发生于画面收尾、最终替换队伍槽之前；交换进化不可取消。'),('evolution','598–617','TradeItem消费收到者物品；TradeSpecies比较自身物种及对等方永石。'),('pbs','15330,16029','KARRABLAST/SHELMET默认参数互指。')],
 [('31','§3.3、§6'),('32','§6'),('32a','§1–2 TradeSpecies数据'),('tcp','CX30–35')],
 ['交换双方为合法现成个体、无永石/BattleBond等守卫。','默认互换两物种不命中自身比较；自定义参数=收到者自身、对等方有/无永石区分。'],
 '交换演出宿主未建立；双收尾后第二次能否抵达检查本轮不判定。', ['选择器的完整可选资格','接待事件收费奖励','二次dispose的运行后果'])
cap('32','战后升级优先、成就记录与事件待触发',
 [('start','112–122,306–327,608–651','L0/K/D初始化；外层治疗在扫描前；按升级优先、正常返回后清表。'),('evolution','622–675','K阈值直接进化，D≥49只置准备，再事件编号消费。'),('damage','294–304,393–403','玩家归属槽K/D计量无敌方目标门。'),('faint','90–94','濒死清D而此处不清K。')],
 [('32','§3–5、§7'),('32a','§4'),('tcp','CX09–29')],
 ['正常世界开始/结束通知，相关成员/索引存在，无插件重排。','检查配置开/关对2/5结果；升级先命中且取消不回头查战后；D不足不清既有准备。','友方要害计K；濒死D清零；捕获左移在接收项另核。'],
 '只核K/D写入门，未全面追每种伤害调用者。', ['所有替身/混乱/画皮伤害前置','特殊模式全部通知','真实战斗异常清理'])
cap('33','寄养移入移出与兼容性前置',
 [('daycare','273–294,437–464,520–552','寄存统计先行，原个体移位/治疗；兼容性先Shadow/Undiscovered，后性别/蛋组/同种同主。'),('pbs','3482–3496,4538–4554','DITTO无性别Ditto蛋组；PICHU Undiscovered。')],
 [('33','§3、§5.1'),('tgr','DC-01–09'),('tbr','BR26')],
 ['两个寄养槽，有效玩家队伍，默认数据；领域入口和接待事件分开。','空索引/满槽寄存统计已增；满队取回保持槽；DITTO+PICHU兼容0；合格一雌一雄同种异主=3。'],
 '接待事件不可得，领域工具不自动扣钱/拒蛋。', ['旧档寄养迁移','真实Nursery收费事件','非法负索引全部访问后果'])
cap('33','256步产蛋、共享蛋招与寄养经验',
 [('daycare','306–316,329–405,560–564','周期先蛋机会再共享后经验；共享按学员蛋招表/供方槽序，每周期仅一方向。'),('settings','157–169','默认gen8不加经验、共享开启；机器和母蛋招开关分列。'),('species','341–345','寄养共享的蛋招查询可回溯前身。')],
 [('33','§5.2、§5.4–5.5、§8'),('tgr','DC-10–11、DC-15–19')],
 ['普通迈步通知；共享两同种、学员有空槽；开关与50%门须通过。','已有蛋阻止第二次机会但不阻止共享；供方[N,M]/接受[M,N]取N；双方向只选一个。','开启经验每步+1、静默学当前新级招、不查进化/友好；报价按级差。'],
 'gen≤6经验开，gen≥8共享开；人工多级add_exp数量未作为普通步行。', ['Shadow寄养经验覆盖组合','蛋寄养升级','接待支付'])
cap('33','领取蛋的生成与容量失败顺序',
 [('daycare','354–358,488–495,253–255','生成只看两槽；生成在满队检查之前；成功入队再重置标记/计数。')],
 [('33','§5.3、§7'),('tgr','DC-12–14'),('tbr','BR26')],
 ['两槽为合法个体、生成各依赖正常；可人为直接领取而标记false/兼容0。','队有位即生成入队清计数；满队报错时随机已消耗、条件感染副作用已发生；重试重新生成。'],
 '不推定缺失事件已调用该工具；不补已有蛋/兼容守卫。', ['随机具体序列','真实接待回滚/费用'])
cap('34','后代角色、熏香物种与形态覆盖顺序',
 [('daycare','21–91','亲本只单次交换；物种亲本与招式亲本不同；基本蛋后地区/母系/永石覆盖。'),('species','305–337','前身熏香门与族内关系；offspring关系另判。'),('forms','744–758','18个地区蛋钩子按产生地编号存在形态才选。'),('pbs','4538–4565,7863–7890,12820–12835','PICHU无熏香、AZURILL海熏香、MANAPHY后代PHIONE。')],
 [('34','§3–5.2'),('tbr','BR01–09')],
 ['两合法亲本、当前数据/地图；物种生成和寄养周期资格分开。','DITTO/雄单次交换后母角色可为雄；PIKACHU系恒PICHU与MARILL无/有熏香分列。','永石形态首个符合族内/旗标亲本覆盖先前地区结果。'],
 '地区号=形态号是数据假设；未穷尽所有物种形式表。', ['全物种族图循环/坏数据','全部DefaultForm与地区形态组合','变体PBS全集'])
cap('34','遗传招式通道、Ditto性别门与保尾',
 [('daycare','92–143','共有高级招、机器、两路蛋招、电气球；去重保后、末尾4项，再静默学习。'),('pokemon','646–660','静默已有招移尾/新招追加/满槽移首。')],
 [('34','§6、§9.3'),('tbr','BR03、BR13–15')],
 ['亲本已掌握合法招、后代原始EggMoves/兼容性表，排除其它来源时可辨性别门。','雌+DITTO两槽序均不经普通蛋招/机器通道；雄/无性别非Ditto可走非雌门。','共同等级招要求包括Ditto在内双方掌握，不能自动采用非Ditto方。'],
 '机器继承默认≤5、母蛋招≥6；重学记录不在生成时自动按整蛋招表补齐。', ['完整机器目录顺序逐项','所有形式不同学招表'])
cap('34','IV继承数量与两亲本持物组合',
 [('daycare','21–45,173–212','先3项，gen≥6且亲本持DESTINYKNOT才5；每个力量属性扣一次，其余不同属性抽样。'),('pokemon','551–577','每个亲本持物读取/比较来自单一规范身份。'),('items','766–774,1423–1439','DESTINYKNOT、POWERWEIGHT、POWERBRACER是不同登记项。')],
 [('34','§7，128–134','正文的3/5数量及力量属性扣减是正确规则。'),('tbr','BR16–19，239–242','BR18错误地给双不同力量道具列5−2分支。'),('20','§6.1–6.2')],
 ['普通双亲、各一件合法持物、无插件覆盖；gen8为主对照。','双不同力量道具只能固定2+随机1=3。','同力量道具固定同一属性一次；一方Knot另一方Power可固定1+随机4=5，gen5同配置仅3。'],
 '不能同时给每个亲本两件持物；传入生成接口不含外部继承数覆写参数。', ['第三方多持物插件','实际随机分布采样'], finding=True)
cap('34','性格、特性、球与异色／病毒收尾',
 [('daycare','145–171,223–255','永石性格候选；隐藏60/普通80；族内球剔除两球；轮首异色读取，末次号未读；语言+护符重掷。'),('pokemon','389–418,477–479,496–534','异色/性格缓存以及隐藏索引判断。')],
 [('34','§5.3–5.4、§8–9'),('tbr','BR10–12、BR20–25')],
 ['合法亲本，默认gen8阈值16；无插件额外缓存读取。','异语言+Charm至多8次；N0无读取，已异色提前停，耗尽末次缓存可空。','球候选剔除MASTER/CHERISH空则保普通；特性遗传不伪称随每世代完全变化。'],
 '性质赋值会重算、换个人编号不直接清性格缓存；本轮不执行生成。', ['完整构造缓存访问图','Pokérus传播及日恢复','其它世代官方差异'])
cap('35','蛋计步、动态加速扫描与孵化提交',
 [('hatch','202–268,103–130','每蛋减1后查动态非蛋集合再最多减1，归零后提交；拥有者/首招先写再动画。'),('pokemon','214–216','蛋仅由剩余步数>0判定。'),('abilities','162,199,976','三条FasterEggHatching默认特性旗标。')],
 [('35','§3–9'),('teg','EG-01–20')],
 ['玩家队伍合法、普通迈步，媒体/输入正常为演出完成前提。','临界蛋可在首次减到0后参与扫描；多蛋顺序、濒死加速非蛋不被排除。','负计数跳过不归零；直接pbHatch不改计数且可重复；核心拥有者先改、记录首招后动画。'],
 '缺宿主/素材，静态不可达文本后备不算已运行；字段存档来源只登记。', ['季节形态演出副作用完整调用链','真实保存恢复','输入法取消与像素/音频'])
cap('36','遭遇数据查询、版本与文本编译边界',
 [('encdata','20–68','精确查失败回退0；存在性不回退；按版本枚举键型不一致导致0与v均产出。'),('enctype','16–178','26种6类别与缺省概率。'),('metadata','114–119','同值版本早退，异值有上下文才setup。'),('compiler','658–761','段头整数前缀，重复类型替换槽并继承概率；重复节拒绝前已登记前节。'),('encounters','20–49','默认005及005,1，雷达20概率表。')],
 [('36','§3'),('teg','EN-09–11、EN-26–30')],
 ['合法已登记物种，最大100，普通当前地图快照与注册数据分开。','版本1精确优先/缺则0，与each_of_version重复不同；同值不reset。','重复Land未写概率继承旧值但重置槽；非数字概率可转0。'],
 '只静态读编译，未执行；编辑器反写0→省略→默认完整链未复查。', ['PBS编辑器/反写全部入口','正整数解析器实现全链','全部地图版本分布'])
cap('36','遭遇触发概率、宽限、驱虫剂与清理',
 [('wild','91–218','雷达直通在禁用/概率/表门之后；累加器整数折算，宽限早退不累计；允许检查及双打优先。'),('world','172–218','迈步通知/传送后才触发；允许拒绝保类型，末尾复位强制单打。')],
 [('36','§4、§7–8'),('teg','EN-01–08、EN-12–16、EN-21–22')],
 ['有效类型、有可战斗成员；步进参数真；无外部钩子改状态。','基础21与累加21/189/210→21/21/22；驱虫剂只在对应门；雷达不能绕禁用。','forceSingle先于Safari/伙伴；主动请求空候选保类型/forceSingle，正常调用返回不等同战斗胜利。'],
 '原地转向如何被移动方法消费只到调用边界，未重审运动系统。', ['全部运动模式','真实随机频率','事件/插件重入'])
cap('36','候选偏好、等级与野生生成修正',
 [('wild','271–468','偏好50%且筛空回退；多掷取最大；等级含端点、HUSTLE等置最高；持物/异色/同步/创建钩子。'),('modifiers','8–59','闪光、Safari/大会IV、传说3满IV、队伍缩放的默认注册效果。'),('balance','194–236','人口标准差调整权重，取整后+2再上限。')],
 [('36','§5–7'),('teg','EN-15、EN-17–20、EN-23–25、EN-31')],
 ['首非蛋成员允许濒死；合法表与数据；作者变体明确指定。','MAGNETPULL命中但无钢仍原表；HUSTLE/GUTS区别；CuteCharm第三分支强制同性而非保默认。','同步跳过漫游；[10,50]平衡52、最后0..4给48..52。'],
 '同一随机源调用次序只静态登记；扩展能力开关gen≥8。', ['所有物种形态生成钩子','完整Safari/大会覆盖生命周期','概率统计执行'])
cap('37','漫游路线推进、替换与终结重置',
 [('roam','20–185,199–227','单条推进/25%替换、位置类型查询、终结记录，重置实际仅已捕获。'),('settings','175–213','全局10图、Kyogre4图及四默认条目。')],
 [('37','§3–5、§10'),('tcp','RM01–12、RM29、RM33')],
 ['合法漫游容器/路线；开关开、非伙伴非雷达，概率门通过才逐项选。','旧原始名vs新解析名比较；同名同区候选与换图早退是不同门。','Kyogre2普通仅21/31；额外随机可停原图；caught重置、defeated不重置。','方式读取位置类型，不用请求OldRod字段；位置nil严格查询可失败。'],
 '开关配置存在不等于Demo启用；路线异常仅审空键/无邻接。', ['调试漫游菜单','v20迁移','地图显示名解析全链'])
cap('37','漫游公开包装的临时生成与持续个体复用',
 [('start','354–408','公开包装先generate_foes再单敌覆盖；核心另建/使用阵容。'),('roam','188–227','首次持续生成与以后复用，正常写回后用原实参通知。'),('wild','383–448','漫游生成仅在同步处有isRoamer差别，其他生成通知仍执行。')],
 [('37','§5.1、§8.2'),('tcp','RM25、RM34–36')],
 ['正常候选物种/等级单敵公开包装、允许覆盖、无其它handler处理、核心正常返回。','首遇临时+持续两次，复遇临时一次；人工现成个体另分支。','原始实参为标识的裸漫游入口清理后取个体属性失败；不推断每路径都一次通知。'],
 '仅此包装/覆盖边界；战斗退出能力、PP同步完整路径未深查。', ['自然回复/再生力终局全部门','generate_foes参数解析所有形状','核心跳战完整条件'])
cap('37','雷达许可、电池、摇草与闪光数学',
 [('radar','18–156,239–267','地形表骑车先于调试电池门；使用50步；链存在不充能；四环采样与闪光阈值。')],
 [('37','§6、§9'),('tcp','RM13–18、RM37')],
 ['可摇草地、普通陆地表、未骑车；正常电量0或调试直通。','伙伴不阻止使用而后续候选取消；链5电量50普通重用被拒；离草本步先电量门后取消。','c16链1/19/20/40阈值17/222/328/328；c100链1阈值145。'],
 '四环几何只审坐标分支/数量，未逐点执行；动画资源缺失。', ['全部环坐标穷举','媒体动画ID可用性','高亮期间外部改图'])
cap('37','雷达续链、有限重抽与空候选异常',
 [('radar','161–237','续链分数整除；闪草直续；有限改选停物种而最终判等物种+级；结果先更新再重摇。')],
 [('37','§7–8'),('tcp','RM19–24、RM30–32')],
 ['有效land候选、无伙伴骑车、站摇草；链>0且所有相关表合法，异常夹具另标。','链10环2上次捕获→90；初始异种0次重抽；同种异级仍耗上限，末次异级可断。','重抽nil在读取前失败，不承诺清链；结果1/4增链，重摇无草再取消。'],
 '有序钩子的注册实现未独立遍历所有扩展；只核默认本域两个handler。', ['上车取消入口','第三方覆盖顺序','完整存档恢复'])
cap('38','捕获数学、暴击及球修正',
 [('catch','206–262','UB整数除10，HP实数乘状态后统一floor/min1，无条件/255短路，暴击/普通随机门。'),('balls','33–198','19球率、Master、2成功处理器与旧新重量/倍率条件。'),('battlecfg','63–65,77–96','新球率gen≥7、软上限默认关、暴击gen≥5。')],
 [('38','§3–4'),('tcp','CP01–14、CP23–24')],
 ['合法目标HP>0/最大HP>0，普通非必捕/非调试；显式暴击关闭或分支掷值。','A200/B1/rate45/Sleep→x112而非110；UB45普通球→4；零率x至少1。','重球新重量999/1000/1999/2000/2999/3000；暴击owned31 x15→c1，一次摇晃判定。'],
 '未重做所有y高精度计算；重量与视睡眠有效性仅消费边界，不签全部能力组合。', ['全部y数值高精度复算','战斗重量/COMATOSE完整修正栈','回放随机','Safari专用捕获公式'])
cap('38','投球许可、成功队列与战后接收失败',
 [('ballmenu','27–64,321–327','双满/禁球/非首动作/半隐身/多对手预检，UseInBattle委托投球。'),('balluse','126–131','专用球执行无一般道具效果复检与退回。'),('catch','5–106,112–201','捕获移出、经验、球效果/首招/离场、延迟队列；满队交换索引左移。'),('peer','5–24','队位优先，送盒治疗保ready；全满兜底调用处风险。')],
 [('38','§1–2、§5–6'),('32','§5'),('tcp','CP15–22；CX22–24、CX39')],
 ['正常内部战斗预检与后段人工全满触达分开；媒体/回调正常为成功前提。','挡球不算0摇失败；成功先移对手/经验再待接收；图鉴先于命名/存储。','显式队满[A,B,C]送A后L0/K/D左移，新尾空；默认容量6仅3成员不触发替换。'],
 '全满未定义消息方法结论本轮只读默认Peer，未再穷尽所有重开；伙伴持物错配全文已读、源终局未重审。', ['菜单登记/取消退球全部调用者','伙伴合并成员与终局还原全链','Shadow专用模式及捕虫大会接收','图鉴内部门全链'])

write('capabilities.json', caps)

# Complete formal-set negative search, without copying source or irrelevant long rows.
neg_pattern = r'BR18|5−2|5-2|DESTINYKNOT|羁绊之绳|红线|力量道具|Power (?:Weight|Bracer|items?)'
formal_files = sorted((ROOT / FORMAL).rglob('*.md'))
hits=[]
for p in formal_files:
    lines=[n for n,t in enumerate(p.read_text().splitlines(),1) if re.search(neg_pattern,t,re.I)]
    if lines: hits.append({'path':str(p.relative_to(ROOT)), 'line_numbers':lines})
negative={
 'search_id':'M06-NEG-IV-01','universe':{'root':FORMAL,'count':len(formal_files),'baseline':B},
 'query':neg_pattern, 'method':'全套正式Markdown合理别名搜索；命中上下文按繁育主规则、静态向量、持物共享合同与纯物品目录区分。',
 'hits':hits,
 'contexts_read':['WP34 §7, §9, §10, §11；BR16–19；WP20 §6.1–6.3','WP30/WP02配置EV项；WP42 Pickup稀有池；WP44/WP50/WP52A及相应测试的迷恋效果；WP47B/WP52C纯物品身份行','其余WP18/24/25/26及测试README命中来自文件名中的5-2，已读命中上下文，为导航而非IV规则'],
 'result':'仅BR18含双不同力量物品仍可5−2的预期；WP34明确五项必须亲本持DESTINYKNOT，WP20单持物合同并未豁免；其它命中为战斗/EV或物品目录，不改变遗传持物门。',
 'source_countercheck':{
   'query':'inherit_IVs|DESTINYKNOT|POWERWEIGHT|POWERBRACER (all Data/Scripts)',
   'result':'仅DayCare生成链定义并调用inherit_IVs；其它命中是战斗/AI/物品效果。生成入口不接收独立继承数量或多持物参数；Pokemon持物单一身份，默认PBS三物品互异。'
 },
 'evidence_level':['SOURCE_STATIC','SPEC_STATIC'],'execution_status':'NOT_EXECUTED'
}
write('negative-evidence-search.json',negative)

finding={
 'id':'GR4-M06-001','title':'BR18 在双不同力量道具前提下错误保留五项 IV 继承分支',
 'module':'M06','severity':'P3','disposition':'REQUIRED','status':'OPEN','reviewer':REVIEWER,
 'category':'事实错误','classification':['Pokémon Rules'],
 'source_baseline':{'commit':R,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','read_only':True},
 'source_anchors':caps[14]['source_anchors'],
 'specification_baseline':{'commit':B,'tree':'d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a','identity_navigation':'delivery/2026-10-12/formal-identities.json'},
 'spec_anchors':caps[14]['spec_anchors'],
 'expected_reference_behavior':'普通单持物亲本各持不同力量道具时，均不持羁绊之绳，基础继承数恒3；两种不同属性各固定1项，只再从其余4属性无放回选1项。世代≥6不会单独把3变5。',
 'current_spec_behavior':'WP34 §7正文正确，但BR18明列固定2项后剩余采样1（3−2）或3（5−2）；后者在该行前提下不可达。',
 'gap':'静态测试接受了一个需要第三件亲本持物的预期，违反同集单持物与羁绊之绳必要条件。不是正文算法缺失。',
 'preconditions':['参考默认普通亲本、每个体一项持物、无插件或自定义多持物覆写；世代8。','两亲本可用合法♂/♀PIKACHU，分别持POWERWEIGHT和POWERBRACER；合法数据/场景/玩家。','只观察IV继承通道，不要求随机具体输出、孵化或领取。'],
 'minimal_counterexample':{'input':'母POWERWEIGHT、父POWERBRACER；母HP31、父ATTACK31；其余亲本IV均0；蛋创建六IV均1（合法条件化随机输入）。','expected':'HP31、ATTACK31；其余4属性中恰1项被继承为0、3项保创建值1。总继承属性3。','incorrect_allowed_result':'若按BR18的5−2分支，再写3项为0，仅1项保创建值1，总继承属性5。','evidence_level':'DERIVED_VECTOR','execution_status':'NOT_EXECUTED'},
 'normal_case':'无Knot/无Power继承3项；双不同Power固定2+随机1；双相同Power固定同项一次+随机2。',
 'failure_or_boundary_case':'合法五项对照应为一方DESTINYKNOT、另一方POWERWEIGHT（gen≥6）：固定HP1项、再选4项；gen5下同一配对仅3项（固定1+随机2）。',
 'impact_on_independent_implementation':'照BR18构建验收会允许或要求不可能的5项组合，使正确3项实现的测试预期不唯一；正文已有正确规则，影响局限于向量质量，定P3。',
 'negative_evidence_search':negative,
 'proposed_spec_change':'仅修BR18为固定2+随机1；可补单Knot+单Power的合法5项及gen5对照。保留WP34正确数量规则和持物合同，不改参考或发明多持物能力。',
 'acceptance_criteria':[
   {'kind':'static','criterion':'双不同Power向量只允许3个不同继承属性，两个固定、一个其余属性。'},
   {'kind':'static','criterion':'若保留5项对照，前提明确gen≥6、一个Knot持有者和至多一个Power持有者；固定1+其余4。'},
   {'kind':'static','criterion':'正文与测试不暗含每亲本多件持物，且同Power重复属性只计一次。'},
   {'kind':'runtime','criterion':'本轮不要求宿主或参考运行；任何后续执行须另立隔离记录，不能把本推导升格为执行。'}
 ],
 'affected_files':[FORMAL+P['tbr']], 'shared_contracts':[FORMAL+P['34']+' §7',FORMAL+P['20']+' §6'],
 'dependencies':['WP33两槽生成入口','WP20单持物身份','世代配置'],
 'related_capabilities':['GR4-CAP-M06-015'],'related_findings':[],
 'root_cause_group':'M06_IV_VECTOR_UNSATISFIABLE_HELD_ITEM_COMBINATION',
 'history_links':{'relationship':'new','third_round_related_id':None,'second_round_related_id':None,'note':'未猜第二轮ID；与GR3-M06-001经验提示时点根因不同，不重开旧CLOSED。'},
 'evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'],'execution_status':'NOT_EXECUTED',
 'confidence':'high_static','unknowns':['第三方多持物插件可改行为，但无此材料且不在该向量前提。'],
 'excluded_claims':['不认定WP34正文继承算法错误','不认定官方游戏规则是证据','不声称运行捕获/繁育/宿主','不把随机数值恰等于亲本值视作该属性实际继承'],
 'user_decision_needed':False,'review_resolution':'待主汇总者安排一次独立反证/去重；本模块只报告，不修正式文件。'
}
write('findings.json',{'schema_version':'1.0','findings':[finding]})

reg={
 'id':'GR3-M06-001','module':'M06','reviewer':REVIEWER,'historical_status':'CLOSED (preserved)',
 'current_file_anchors':[spec('30','§5.2，138–142'),spec('tgr','U03-EX01–05，244–252')],
 'source_anchors':[src('itemutil','223–278','钳制与相等早退；差量消息早于写入；同级增经验维生素、减经验无；重算/刷新后才同级早退。')],
 'old_acceptance_references':[
  {'commit':'d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65','path':'review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/findings.json','pointer':'id=GR3-M06-001'},
  {'commit':'08fc8828229c14ab4a540db417d08194ba194a31','path':'review/remediation-third-20261012-prepare/U03/actual-integration/independent-review/attempt-01/per-id-verdicts.json','pointer':'verdicts / id=GR3-M06-001; actual_verdict PASS; actual=5004b201183574eabc92764ec4212613314bdecd'},
  {'commit':'c2eb74c7cbcf8a190d5e902d871fbce44904efd6','path':'review/remediation-third-20261012-prepare/registration/U03-formal-acceptance.json','pointer':'FORMALLY_ACCEPTED_EXACT_ACTUAL_SCOPE / accepted_ids; historical final_CLOSED=false belongs to its generation'},
  {'commit':B,'path':'delivery/2026-10-12/current-status.json','pointer':'effective_CLOSED23=23; activation=98e49a592c9e82b1e53d3f1fd403ba2ad0935983'}
 ],
 'criteria_checked':[
  {'criterion':'同级增减及同值三例的消息／时点／终值','actual_check':'读当前WP30与EX；E27→28先提示获得1再写28/h85；E28→27先提示失去1再写27/h80；相等提示未变化立即返回。','result':'supported_static'},
  {'criterion':'按钳制后T计算差量','actual_check':'0请求−1同值；999999请求1000001仅+1；1请求−4仅−1。','result':'supported_static'},
  {'criterion':'同级无升级窗/学招/进化且增减友好分支不同','actual_check':'源278及250的早退在重算/刷新之后；上涨275先有vitamin；下降没有。','result':'supported_static'}
 ],
 'consumers_checked':['ItemUtilities pbGainExpFromExpCandy 315–327：qty−1前置友好保留，不将辅助先提示推广为整个糖果无先行变更。'],
 'result':'supported_static; no regression found in original bounded criteria',
 'limits':['WP28全文、调试原始经验写入不作为此次回归签字对象','消息/资源故障、宿主会话及行为向量未执行'],
 'evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'],'execution_status':'NOT_EXECUTED'
}
write('regression.json',[reg])

# Per-document scope is deliberately partial even where all text was read.
coverage=[]
for k in ['30','31','32','32a','33','34','35','36','37','38','tgr','tbr','teg','tcp','20']:
    path=FORMAL+P[k]
    linked=[c for c in caps if any(a['path']==path for a in c['spec_anchors'])]
    anchors=[]
    for c in linked:
        for a in c['source_anchors']:
            if a not in anchors: anchors.append(a)
    coverage.append({
      'path':path,'baseline':B,
      'contracts_checked':[a['lines_or_section'] for c in linked for a in c['spec_anchors'] if a['path']==path],
      'source_anchors':anchors,'status':'partial',
      'support_evidence':{'meaning':'列明合同获supported_static；文件仅有界检查，不作全篇语义PASS。','capabilities':[c['capability_id'] for c in linked]},
      'dependencies':sorted({c['primary_owner'] for c in linked}),
      'unsupported_assertions':([{'anchor':'BR18 line241','finding':'GR4-M06-001','assertion':'双不同力量道具下5−2继承分支'}] if k=='tbr' else []),
      'not_checked':sorted({s for c in linked for s in c['not_checked']}) + (['同目录非本域测试族'] if k in ['tgr','tbr','teg'] else []),
      'read_extent':('本域GR/DC/U03-EX段已读，其他族仅导航/反证' if k=='tgr' else 'BR01–26已读，其他族只反证与导航' if k=='tbr' else 'EG/EN已读，FC/MG/TT未审' if k=='teg' else '§6持物读取/写入/单一身份，仅反证共享合同' if k=='20' else '正文／附表／对应测试文本已读；只对contracts_checked所列部分追源'),
      'evidence_level':['SOURCE_STATIC','SPEC_STATIC'],'execution_status':'NOT_EXECUTED'
    })
coverage.append({'path':FORMAL+'scope-statement.md','baseline':B,'contracts_checked':['静态证据、测试未执行、Demo/素材/插件限制；历史状态标签按交付导航解释'], 'source_anchors':[], 'status':'partial', 'support_evidence':'与共享baseline PARTIAL_READY及当前delivery/current-status的时点分层一致；不把旧候选标签当新回归。', 'dependencies':['baseline.json','delivery/2026-10-12/current-status.json'], 'unsupported_assertions':[], 'not_checked':['全局审批历史及其它域scope准确性'],'read_extent':'本域关联命中与静态/未决口径','evidence_level':['SPEC_STATIC'],'execution_status':'NOT_EXECUTED'})
write('spec-coverage.json',coverage)

write('identity.json',{
 'schema_version':'1.0','module':'M06','reviewer':REVIEWER,
 'thread_id':'01a12fe0-a4a3-75a0-87bd-03c04ac176c8','pid':81552,
 'parent_thread_id':'01a12fc2-e8c0-7e43-a721-ccfe659d75c8','role':'父会话启动的独立CLI审者；本字段非内部agent标签',
 'identity_source':'../../tasks/M06-launch.json',
 'requested':{'model':'gpt-6-astra','reasoning_effort':'ultra','service_tier':'default','fast':False},
 'actual_echo':'UNVERIFIED','formal_baseline':B,'reference_baseline':R,
 'readiness':'PARTIAL_READY (shared baseline)','baseline_source':'../../baseline.json',
 'authorization':'仅modules/M06内写入；未启动其它agent、未修正式文件/参考、未提交/push/改配置。'
})

# Inventory through all tracked reference paths; hit lines are navigation, not semantic coverage.
tracked=subprocess.check_output(['git','-C',str(REF),'ls-files','-z'],text=True).rstrip('\0').split('\0')
pat=r'growth_rate|changeHappiness|pbChangeLevel|pbChangeExp|pbLearnMove|pbRelearnMove|check_evolution|pbEvolution|DayCare|day_care|EggGenerator|steps_to_hatch|pbHatch|on_wild_pokemon_created|on_wild_species_chosen|encounter_version|PokemonEncounters|pbEncounter|roamPokemon|roamedAlready|PokeRadar|poke_radar|pbThrowPokeBall|pbCaptureCalc|CatchAndStore|PokeBallEffects|pbRecordAndStoreCaught|GAIN_EXP_FOR_CAPTURE|BREEDING_CAN_INHERIT'
relevant=[]
semantic={}
for c in caps:
 for a in c['source_anchors']:
  semantic.setdefault(a['path'],[])
  if a['lines_or_symbol'] not in semantic[a['path']]:semantic[a['path']].append(a['lines_or_symbol'])
for path in tracked:
    p=REF/path
    hit=[]
    if path.startswith('Data/Scripts/') and p.suffix=='.rb':
        hit=[n for n,l in enumerate(p.read_text(errors='replace').splitlines(),1) if re.search(pat,l)]
    if hit or path in semantic:
        relevant.append({'path':path,'status':'read_semantically' if path in semantic else 'inventoried_only','semantic_ranges':semantic.get(path,[]),'navigation_hit_lines':hit,'remainder':'未列语义范围不作已审','material_availability':'available'})
pbs_inventory=[{'path':p,'status':'read_semantically' if p in semantic else 'inventoried_only','semantic_ranges':semantic.get(p,[]),'role':'默认顶层样本' if '/' not in p[len('PBS/'):] else '目录变体/备份，未自动视作当前生效'} for p in tracked if p.startswith('PBS/')]
text_inventory=[{'path':p,'status':'inventoried_only','reason':'全部翻译资源列名；未逐字符串审本域文案或解析二进制'} for p in tracked if p.startswith('Text_english_core/')]
write('source-scope.json',{
 'schema_version':'1.0','source_baseline':R,'source_root':str(REF),'readiness_source':'../../baseline.json',
 'search_universe':'全部tracked路径盘点；对全部Data/Scripts文本按下列符号族搜索，源端主文件/注册/调用者与数据样本进一步追读。',
 'discovery_pattern':pat, 'tracked_count_shared':432,
 'related_sources':relevant,'pbs_inventory':pbs_inventory,'translation_inventory':text_inventory,
 'scope_limits':['read_semantically仅表示列明范围，非文件全部审完；inventoried_only表示材料可读但未核其语义。','PBS顶层样本未穷尽全部物种/形态/招式/遭遇表；所有gen/备份目录不作生效推断。','本域debug工具、保存迁移、编译反写、AI/招式/特殊战斗等多数caller仅盘点；详逐项not_checked。','Graphics/Audio/地图/完整Demo缺失沿用共享readiness，Fonts和两个BMP存在不等于完成演出。','Scripts.rxdata、messages_core.dat未解析或执行；未下载/安装/账户或凭据访问。'],
 'evidence_level':['SOURCE_STATIC'],'execution_status':'NOT_EXECUTED'
})
direct={FORMAL+P[k] for k in ['30','31','32','32a','33','34','35','36','37','38','tgr','tbr','teg','tcp']}
write('formal-scope.json',{
 'baseline':B,'identity_navigation':'delivery/2026-10-12/formal-identities.json','formal_count':len(formal_files),
 'direct_domain_count':len(direct),'files':[{'path':str(p.relative_to(ROOT)),'role':'domain_body_appendix_or_test' if str(p.relative_to(ROOT)) in direct else 'shared_contract_read' if str(p.relative_to(ROOT)) in [FORMAL+P['20'],FORMAL+'scope-statement.md'] else 'inventoried_search_universe_only'} for p in formal_files],
 'negative_search_ref':'negative-evidence-search.json','statement':'131为反证搜索总体，14为本域正文/附表/共享测试文件数；均非功能覆盖分母。'
})

prior_runs = json.loads((OUT/'execution.json').read_text()).get('actual_executions', []) if (OUT/'execution.json').exists() else []
write('execution.json',{
 'actual_executions':prior_runs,
 'not_executed':[
  {'kind':'EXECUTED_REFERENCE','scope':'参考Ruby、生成器、孵化、捕获、战斗与遭遇行为','reason':'本轮采用可审计静态控制流/数据检查；未运行参考。'},
  {'kind':'EXECUTED_MODEL','scope':'自制繁育/捕获/成长模型及概率仿真','reason':'DERIVED_VECTOR为手工条件推导，不冒充模型执行。'},
  {'kind':'EXECUTED_HOST_OR_DEMO','scope':'游戏宿主、素材表现、地图事件、寄养接待、存档加载','reason':'共享readiness未建立宿主；地图/Graphics/Audio/完整Demo不可得。'},
  {'kind':'TOOL_VALIDATION','scope':'编译、转换、反序列化、全600经验表重算或概率统计','reason':'未执行；后续产物JSON一致性校验另记实际条目，不能升级为行为验证。'}
 ],
 'inspection_note':'rg、nl/sed、Path文本读取、git show/ls-files用于静态取证；failed JSON导航读取已按实际list结构修正。没有加载参考程序、真实存档或执行历史审者脚本。',
 'evidence_rule':'SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR与执行状态分开；产物构建及JSON检查属于TOOL_VALIDATION。'
})

print(json.dumps({'capabilities':len(caps),'findings':1,'spec_coverage_files':len(coverage),'direct_domain_files':len(direct),'formal_search_files':len(formal_files),'reference_related_paths':len(relevant),'pbs_inventory':len(pbs_inventory),'translation_inventory':len(text_inventory)},ensure_ascii=False))
