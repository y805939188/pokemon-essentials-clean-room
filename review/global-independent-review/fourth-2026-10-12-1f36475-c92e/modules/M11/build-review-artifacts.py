"""Assemble bounded M11 audit records; writes only beside this file."""
from pathlib import Path
from datetime import datetime, timezone
import json
import re
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
FORMAL = ROOT / 'deliverables/final-specification-set'
R = Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
B = '1f36475d22120a0d1175967d5b17d71fe8311d88'
RC = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
reviewer = {
    'module': 'M11', 'thread_id': '01a13017-c27c-7020-a9f8-9bb66eb74f64',
    'pid': 67804, 'role': '父会话启动的独立 CLI 审者',
    'identity_source': 'tasks/M11-launch.json',
    'requested_model': 'gpt-6-astra', 'requested_reasoning_effort': 'ultra',
    'requested_service_tier': 'default', 'requested_fast': False,
    'actual_echo': 'UNVERIFIED',
}
source_baseline = {'path': str(R), 'commit': RC, 'tree': '7589c800b61ba13a13040ed0d686979b80a84fd0', 'readiness': 'PARTIAL_READY', 'identity_basis': '共享 baseline.json；未重核全仓'}
spec_baseline = {'commit': B, 'tree': 'd696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a', 'root': 'deliverables/final-specification-set', 'files': 131, 'identity_basis': '共享 baseline.json'}
P = {
 'dex': 'pokemon-rules/wp62-pokedex-records-regions-and-content.md',
 'gear': 'user-interface/wp63-pokegear-map-music-and-phone.md',
 'dexui': 'user-interface/wp66-b-storage-and-pokedex-ui.md',
 'triad': 'creature-rpg/wp68-triple-triad.md', 'duel': 'user-interface/wp68-duel.md',
 'slots': 'user-interface/wp69-slot-machine.md', 'reels': 'user-interface/wp69-slot-reels.md',
 'vf': 'pokemon-rules/wp69-voltorb-flip.md', 'vfdata': 'pokemon-rules/wp69-voltorb-layouts.md',
 'mining': 'user-interface/wp70-mining.md', 'mindata': 'user-interface/wp70-mining-data.md',
 'lottery': 'pokemon-rules/wp70-lottery.md', 'tile': 'user-interface/wp71-tile-puzzles.md',
 'uitest': 'test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md',
 'pktest': 'test-catalog/pokemon-rules-wp53-60-61-62-69-70.md',
 'tttest': 'test-catalog/creature-rpg-wp35-36-57-64-68.md',
 'bag': 'creature-rpg/wp27-bag-and-item-storage.md',
 'cfg': 'generic-kernel/wp02-rule-configuration-and-data-variants.md',
 'resources': 'engine-overworld/wp15-resource-matching-and-audio.md',
 'input': 'user-interface/wp17-messages-windows-input.md',
}
S = {
 'dex': 'Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb',
 'dexmenu': 'Data/Scripts/016_UI/002_UI_Pokedex_Menu.rb',
 'dexmain': 'Data/Scripts/016_UI/003_UI_Pokedex_Main.rb',
 'dexentry': 'Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb',
 'pause': 'Data/Scripts/016_UI/001_UI_PauseMenu.rb',
 'gear': 'Data/Scripts/016_UI/008_UI_Pokegear.rb',
 'map': 'Data/Scripts/016_UI/009_UI_RegionMap.rb',
 'phoneui': 'Data/Scripts/016_UI/010_UI_Phone.rb',
 'music': 'Data/Scripts/016_UI/011_UI_Jukebox.rb',
 'phone': 'Data/Scripts/013_Items/004_Item_Phone.rb',
 'slots': 'Data/Scripts/017_Minigames/003_Minigame_SlotMachine.rb',
 'vf': 'Data/Scripts/017_Minigames/004_Minigame_VoltorbFlip.rb',
 'triad': 'Data/Scripts/017_Minigames/002_Minigame_TripleTriad.rb',
 'duel': 'Data/Scripts/017_Minigames/001_Minigame_Duel.rb',
 'lottery': 'Data/Scripts/017_Minigames/005_Minigame_Lottery.rb',
 'mining': 'Data/Scripts/017_Minigames/006_Minigame_Mining.rb',
 'tile': 'Data/Scripts/017_Minigames/007_Minigame_TilePuzzles.rb',
 'bag': 'Data/Scripts/013_Items/008_PokemonBag.rb',
 'util': 'Data/Scripts/019_Utilities/001_Utilities.rb',
 'acquire': 'Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb',
 'enc': 'Data/Scripts/010_Data/002_PBS data/013_Encounter.rb',
 'cfg': 'Data/Scripts/001_Settings.rb',
 'sprites': 'Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb',
 'spritefiles': 'Data/Scripts/010_Data/002_PBS data/009_Species_files.rb',
 'system': 'Data/Scripts/004_Game classes/002_Game_System.rb',
 'storage': 'Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb',
 'compiler': 'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',
}

def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def src(key, loc, fact):
    return {'path': S.get(key, key), 'commit': RC, 'lines_or_symbol': loc, 'fact': fact}

def spec(key, loc, fact='本次读取的对应行为条款'):
    return {'path': 'deliverables/final-specification-set/' + P.get(key, key), 'commit': B, 'section_or_vector': loc, 'fact': fact}

common_limits = ['无 Graphics/Audio/真实地图与完整 Demo；不声称输入、画面或音频已运行', '不穷尽插件、任意坏输入及外部并发改写']
caps = []

def cap(description, sources, specs, branches, reason, not_checked, classification, status='supported', entry='正常已构建领域状态、有效默认数据及所列入口前提', config='默认固定快照；变体仅限本项列出的条件', history=None, related=None):
    cid = f'GR4-CAP-M11-{len(caps)+1:03d}'
    caps.append({
        'capability_id': cid, 'module': 'M11', 'description': description,
        'source_anchors': sources, 'spec_anchors': specs,
        'entry_and_preconditions': entry, 'configuration_data_host_limits': [config] + common_limits,
        'reviewer': reviewer, 'checked_branches_boundaries': branches,
        'evidence_level': ['SOURCE_STATIC', 'SPEC_STATIC', 'DERIVED_VECTOR'],
        'execution_status': 'NOT_EXECUTED',
        'material_availability': {'source': 'available', 'formal': 'available', 'host_media_demo': 'unavailable_or_unestablished'},
        'status': status, 'reason': ('supported_static：' if status == 'supported' else '') + reason,
        'related_findings': related or [], 'history_links': history or [],
        'not_checked': not_checked, 'classification': classification,
        'primary_owner': 'M11', 'projection': [],
    })
    return cid

cap('图鉴记录的归一、首写/覆盖、刷新及清理',
 [src('dex','14–359；register / register_last_seen / refresh_accessible_dexes','基种键、异色维、性别归一、两入口形态名判断差异及可关闭刷新')],
 [spec('dex','§2–4；PD01–05、PD20–24、PD26–27')],
 ['未知标识的守卫族与登记族分开','seen/owned 独立','无性别2写形态时并0；最近见到保留原性别','形态2可查询却不计入形态数','clear 保留解锁；关闭刷新可保留旧可访问缓存'],
 '字段写入与异常边界有承接；记录含异色不自动推出图像采用异色，见另项展示缺口。',
 ['所有战斗、孵化、进化、回放调用者完整复查','任意负性别/非法维度输入'], ['Pokémon Rules'])
cap('地区解锁、成员查询与可访问列表',
 [src('dex','279–341、351–358','解锁锁定越界归全国；当前地区分支只查已见，不查解锁'),src('util','380–418','成员空表为无值；编号缺失0；长度与全国分支独立'),src('compiler','593–628','顺序平铺；重复节/重复物种拒绝；检查后保存')],
 [spec('dex','§5.1–5.2；PD06–12'),spec('dexui','§5.1–5.3')],
 ['当前地区模式 true/false','全国已解锁未知物种查询短路','区域空表查询失败与UI全国回退分离','重复节/同表物种重复拒绝'],
 '未把区域号、地区图鉴号、解锁位及可访问缓存合并。', ['稀疏节号编译诊断细节','regional_dexes 全部物种顺序逐项核对'], ['Pokémon Rules','Generic Kernel'])
cap('赠送图鉴展示的世代条件及两静默入口差别',
 [src('cfg','17、306–319','默认世代8；更常显示新条目由世代≥7派生'),src('acquire','48–128','普通赠送提示条件；两个静默入口 see_form=false 的见过写入不同')],
 [spec('dex','§3.2、§3.4；PD24'),spec('cfg','图鉴、地图与电话配置表'),spec('creature-rpg/wp26-acquisition-gifts-and-script-trade.md','§3 获得入口')],
 ['规则世代6/7：普通赠送自动条目门不同，领域登记不因此停止','see_form=false 且有效既有个体：静默加入写seen；仅入队静默只owned','正常容量拒绝先于包装内图鉴登记'],
 '默认与变体来源明确，未把展示开关当成全部图鉴写入开关。', ['全部蛋构造/形态处理器组合','备份世代 PBS 全量迁移'], ['Pokémon Rules','Creature-RPG'])
cap('可列形态资格与查看即写、BACK 不回滚',
 [src('dexentry','154–199、440–483','结构门先于已见门；性别折叠/标签；进入形态选择首轮写末次形态，默认异色false')],
 [spec('dex','§6.1；PD31–34'),spec('dexui','§7.2；B38')],
 ['非0无名或展示重定向排除','仅雌已见且基础前图同解析时雄档展示','已存在空串与nil标签不同','可列>1首轮写入；不移动BACK仍不回滚'],
 '形式、资格与记录副作用已承接；本项不等于异色图像选择已完整。', ['真实前图性别差异文件','每一默认形态逐项内容审计'], ['Pokémon Rules','User Interface'])
cap('栖息地掩码、版本枚举和重复可见点并集',
 [src('dexentry','302–351','资格过滤、形状已有字符、平移与可见点并集'),src('enc','30–35、53–59','单取版本回退与枚举v0误并入不同'),src('map','183–228','地图查询为同格首条，不是并集')],
 [spec('dex','§5.3–5.3.1，行114–139'),spec('dexui','§7.1，行200'),spec('pktest','PD16；U05-HAB01–04'),spec('gear','§3.1–3.2')],
 ['宽3的10000仅1格、11111五格、缺尾格不亮','缺省/宽0回退1格','首条隐藏第二条可见：Area亮、地图三查询空','v1无X而v0有X可误亮；get正常回退不合并'],
 '旧GR3四条验收在当前字节得到独立静态支持。', ['非01字符、越界映射','实际地图及栖息地动画'], ['Pokémon Rules','User Interface'], history=['GR3-M11-001'])
cap('图鉴记录异色与实际物种图像请求的分离',
 [src('dex','195–227','首次登记和最近见到均可保留异色true'),src('dexmain','264–295、417–448、766–768','选中物种预览读取性别/形态，固定普通外观'),src('dexentry','5–67、71–116、139–151、582–617','完整、摘要单种及简略入口均复用固定普通外观刷新；Info、Forms前/后/图标请求false'),src('sprites','64–68、253–258','外观参数透传至资源选择'),src('spritefiles','3–34、47–52、86–89、118–120','普通请求不尝试异色目录')],
 [spec('dex','§2，行19–21；§4，行89–90；§6'),spec('dexui','§6.1、§7.1–7.3，行146–211'),spec('resources','§4.1'),spec('uitest','BX B20–B39'),spec('pktest','PD03–05、PD19、PD31–34')],
 ['保存末次[0,0,true]，不进入形态选择器：预览/Info仍请求普通且记录true保持','仅异色已见仍可列该形态；没有异色选择项','简略获得条目与完整条目采用同样展示参数','普通记录false是邻近正常对照'],
 '规格保留记录和浏览重写规则，却缺少预览及条目图像主动忽略异色的消费合同；资源通用回退不能补足调用方参数。',
 ['真实像素结果；普通与异色媒体均缺失','插件添加异色切换'], ['User Interface','Pokémon Rules','Engine / Overworld Integration'], status='partial', related=['GR4-M11-001'])
caps[-1]['projection'] = ['M10：WP66-B 图鉴UI消费者；由父汇总者去重']
cap('图鉴列表筛选与失败搜索的持久模式',
 [src('dexmain','317–414、771–848、1092–1117、1224–1238、1255–1283','空地区回退；资格/裁尾；Start先写模式，空结果不替换列表/参数')],
 [spec('dex','§6'),spec('dexui','§6.1–6.3'),spec('pktest','PD13、PD28–29'),spec('uitest','BX B25–26、B35')],
 ['数值序保留中间未见而裁末尾','首字母查seen；类型体型查owned','失败Start→Cancel保存新持久模式但保留原显示列表','已有结果态BACK复位0，普通态BACK不复位'],
 '四种状态量及取消后状态已明确。', ['身高体重子页全部导航/locale转换','搜索同名/同体型排序稳定性'], ['User Interface'])
cap('Pokégear及地图工具入口、返回和飞行分流',
 [src('pause','133–155、206–235','暂停入口资格及返回后飞行消费'),src('gear','89–113、134–205','三默认命令及Map返回结束齿轮、Phone/Jukebox返回继续')],
 [spec('gear','§2.1–2.3；P01–05'),spec('dexui','§5.1')],
 ['持机与TOWNMAP暂停项互斥','空电话本仍有Phone按钮','BACK关齿轮、Map选择写目的地并结束'],
 '本域入口与地图选择返回已支持；FLY后续执行仅为边界依赖。', ['插件新增菜单项','飞行消耗、转移和Box Link返回链完整复核'], ['User Interface','Engine / Overworld Integration'])
cap('地图定位、可见点首条、飞行选择与编辑器取消',
 [src('map','70–152、173–244、270–355','请求区域回退、子格长度折算、首条可见性、保存/退出门、治疗点返回'),src('Data/Scripts/010_Data/002_PBS data/002_TownMap.rb','SCHEMA Point','点数据及可选字段'),src('PBS/town_map.txt','3–36','两区域、治疗点与开关51/52样本')],
 [spec('gear','§3；P06–11、P33–38')],
 ['无定位显式地区仍回0','正常20×20的10000只用长度到(15,13)','同格隐藏首条不回退第二','wallmap隐藏开关点','未访问治疗点无选择；CTRL不越首条/可见门','编辑器未改BACK直接退出'],
 '三类地图消费者差异成立；不把栖息地掩码套到玩家定位。', ['编辑器写文件实现/实际PBS反写','八向移动的全部时序'], ['User Interface','Engine / Overworld Integration'])
cap('电话注册、隐藏再注册、UI移动取消及删除',
 [src('phone','18–113、172–188、227–265','可选持机预检；两注册形态误用版本参数查重；隐藏不复用；普通反馈可在写后失败'),src('phoneui','160–185、210–269','移动BACK还原、NPC删除不提供、可见优先排序')],
 [spec('gear','§4.1–4.3、§4.6；P14–19、P39、PL01–04')],
 ['无机直调合法注册仍成功','隐藏同键注册另建','版本数3起始0重复新增','文本类型普通反馈先写后失败；静默成功','UI取消移动还原；NPC旧删除包装不同于UI门'],
 '准入预检与写入守卫、先提交后反馈异常均有承接。', ['所有相等排序键的宿主排序稳定性','异步脚本改联系人期间UI状态'], ['Creature-RPG','User Interface'])
cap('电话再战、来电倒计时、问候与物种占位抽样',
 [src('phone','118–143、295–310、352–383、414–559','就绪按不同系统秒递减1；来电按帧delta；消息版本回退；TP/TE每通各抽一次'),src('PBS/phone.txt','3–48','默认与Jeff/Susie消息组；默认无End、具名组有End')],
 [spec('gear','§4.4、§5.2–5.3；P20–28、P41–42；PL12、PL14–17')],
 ['20–39整数分钟并当次递减；就绪1后跳过','菜单等暂停两计时','消息旗标1→2先于播放完成','标准body1/body2且body存在75%；无body恒拼接','TE取Land/Cave/Water首非空前四槽均匀；不是遭遇权重'],
 '时点、条件概率与再战状态已有可区分合同。', ['系统时间向后/跨秒卡顿全部组合','真实来电公共事件内容'], ['Creature-RPG','Generic Kernel','User Interface'])
cap('电话呼出失败与18项弃用输入',
 [src('phone','328–348、389–407、583–705','记录呼出依信号/同图/区域门；按身份呼出缺公开查询；旧reset未定义参数；版本包装失配'),src('Data/Scripts/010_Data/002_PBS data/021_PhoneMessage.rb','try_get；initialize','NPC零公共事件落训练家消息类型校验失败')],
 [spec('gear','§4.5–4.6、§5.1、§8；P31–32、P40、P45–46；PL01–18')],
 ['记录呼出无信号先拒绝','按标识呼出在信号门前失败','NPC公共事件0与正但不存在不同','旧包装18行逐一对照转发/输入顺序，未执行'],
 '旧身份合同没有将转发等同可用；本次未见新增规格缺口。', ['弃用告警设施内部','事件编译器生成再战页的完整执行'], ['Creature-RPG','Demo / Developer Experience'])
cap('点唱机覆盖、遭遇旗标及Custom失败',
 [src('music','65–148','固定六命令；Custom枚举/选曲，目录缺失在清状态前失败'),src('system','65–81、140–148','默认BGM覆盖优先；设置覆盖与清除'),src('Data/Scripts/012_Overworld/002_Overworld_Metadata.rb','135–149','新地图效果两遭遇率旗标默认清除')],
 [spec('gear','§6、§8；P29–30、P43–44'),spec('resources','§6 音频覆盖')],
 ['Custom A→March仍由覆盖A消费，旗标higher真','Stop清覆盖与旗标','Custom目录缺失保留旧状态；空可进入目录USE与BACK不同','换图清旗标和跨图覆盖独立'],
 '资源存在性、音乐请求和持久覆盖的不同层次已保留。', ['实际目录枚举/音频播放','音频其他通道与淡出完整机制'], ['User Interface','Engine / Overworld Integration'])
cap('Triad卡值、价格、库存与随机手牌/对手候选',
 [src('triad','13–84、638–645、700–805、968–1041','属性离散阈值、严格向上量化、准备副本归并、按槽抽取、200候选后索引域'),src('bag','237–299','添加按槽序填充、删除按身份从首匹配槽扣减')],
 [spec('triad','§2–4；TT01–10、TT25'),spec('bag','§3.2，行70–73')],
 ['方向量44/45与188/189','全10买25000而非24000；P500/501步长分支','空仓直接1500部分成功与赠送预检拒绝','准备[A1,A1,B3]→[A2,B3]首抽1/2；满A槽不归并','maxLevel不参与抽样；minLevel0索引0..19'],
 '随机域、量化与容器共享合同可共同确定行为；不把完整最终牌组称为均匀。', ['最终五抽联合概率与对手排序并列分布','所有物种/代际备份的四值'], ['Creature-RPG','Pokémon Rules','Generic Kernel'])
cap('Triad落牌、翻转、取消、胜负奖励及买卖',
 [src('triad','258–346、371–449、647–695、806–963、1048–1243','手选撤回；openhand按玩家手数导航；samewins递归；真实与评分翻转不同；direct败局错误扣身份；买卖提交先后')],
 [spec('triad','§5–7；TT11–24、TT26'),spec('tttest','TT15–22、TT25–26')],
 ['普通相等不翻/samewins相等递归','elements仅初落牌进攻+1，连锁无加成','选格BACK回选牌、手选零张BACK蜂鸣不退出','countunplayed5:5可平','合法preset的direct败局不扣原牌却加所得','真值prize覆盖noprize胜奖；未知奖不回退','卖牌先加钱后删，满钱仍删牌'],
 '参考异常被保留为事实，未依据模式名称改写成理想奖惩。', ['每种完整棋盘连锁枚举','实际卡面素材及地图滚动','无候选异常宿主呈现'], ['Creature-RPG','User Interface'])
cap('Duel动作矩阵、特殊资格、概率与同时倒下',
 [src('duel','57–327','10/10生命、特殊一次、对手先抽再给台词、16格伤害及玩家归零优先')],
 [spec('duel','§2–6；D01–12')],
 ['16组动作损失逐支对应','敌特殊未用权重3:4:4:2，用后3:4:4','3/4生命双特殊后双方0按玩家失败','BACK不能取消动作菜单','收尾恢复旧速度但固定朝向关，不保证坐标归位'],
 '正常、边界、失败与世界副作用的主要合同匹配。', ['包装NPC身份的随机调用计数','强制移动路线实际执行/地形碰撞','12台词真实事件实参'], ['User Interface','Engine / Overworld Integration'])
cap('老虎机转轮、滑移、有效线及会话结算',
 [src('slots','8–99、147–272、313–455','66有序位置、简单min/困难max滑移、1/3/5线、重玩、信用局部修改与离场净额')],
 [spec('slots','§1–6；S01–16'),spec('reels','完整有序与频次表')],
 ['滑移0/1/2/3的单样本及两样本分布手工核算','重复停止重抽同最左轮','重玩帧DOWN先扣币','全局正余额而信用0不自动GameOver，可BACK','中奖累计与重玩可并存；净差100→105仅won+5','上限清剩余；异常前未提交账无保证'],
 '正文及所有22×3位置/频次通过文本数据核验；未把频次转成最终中奖率。', ['宿主图片高度与转动时序','停止策略的最终概率','任意并发余额改写'], ['User Interface','Creature-RPG','Generic Kernel'])
cap('Voltorb候选、严格拒绝、奖额领取及等级失败',
 [src('vf','12–113、126–219、356–523、667–704','75候选、1000次失败末盘回退、揭完倍率过关、领取先写币；等级>1倒置夹限')],
 [spec('vf','§1–6；VF01–18'),spec('vfdata','75行全部参数/补足数/乘积')],
 ['免费格行或列无雷；总数=G/行数=F均拒绝','1000次全拒绝仍返回最后一盘','已揭格可标记；标记不保护普通翻牌','余额0有币盒可玩；确认退出领取；拒绝保留','等级1正常重新开；2..8踩雷在下一盘前失败','最高候选固定积3456，上限只记实际到账'],
 '默认内容与边界描述匹配；所有候选附表字面/常数验证通过。', ['标准运行库夹限异常的真实宿主呈现','生成接受率与1000重试失败频率','完整牌局运行'], ['Pokémon Rules','User Interface','Generic Kernel'])
cap('挖矿占位、层厚、工具、临界终局与奖励',
 [src('mining','42–64、148–227、233–438、440–645','61项/13铁形状；位置内层无界；层厚分布；中心铁守卫；闪光后登记与坍塌优先领取'),src('bag','263–299','逐件直接添加而无批量事务')],
 [spec('mining','§1–6；M01–22'),spec('mindata','61物品及13铁形状全表')],
 ['61行权重2370，48身份/口袋一致；掩码全表一致','HEARTSCALE重复与化石/石板整组互斥','物品外层500次不终止位置内层','中心铁厚2只挖中心，厚3正常范围','损耗48末镐挖完仍坍塌但发新揭物','确认放弃仅发已揭；有限容量逐件部分成功','闪光中断未登记；重复领取非幂等'],
 '掩码、概率输入、提交顺序均有足够事实；数据附表工具核验通过。', ['默认不可放布局的实际可达率','矿点事件/墙体重生规则','宿主动画和资源效果'], ['User Interface','Creature-RPG','Generic Kernel'])
cap('彩票生成、连续尾数匹配及非原子输出',
 [src('lottery','5–46','日期seed、重播种、最低五位匹配、队伍先扫描、结果变量顺序'),src('storage','388–395','第二遍包含队伍伪盒-1、跳空位、包含蛋'),src('util','516–519','生成写入包装与刷新')],
 [spec('lottery','§2–5；LT01–16')],
 ['2026-09-30的数学seed1037630；不声称具体随机号码','7与00007匹配5；112345与12345匹配5','队伍蛋并列优先、位置1','第一遍队伍空洞抛错而结果未写','输出同变量最后覆盖为匹配数；检索不发奖'],
 '号码、匹配、集合及兑奖未知被正确分层。', ['真实开奖日期/时区/奖品表/领奖次数','地区代理完整运行','跨语言随机序列一致性'], ['Pokémon Rules','Creature-RPG','Generic Kernel'])
cap('七种拼图的动作、完成优先、取消与尺寸反例',
 [src('tile','89–238、250–366、369–508、511–607','七模式初始化与动作；完成先于输入；BACKfalse/确认true；非方形端点及空白末格漏扫')],
 [spec('tile','§2–9、§10；T01–26及三空态反向')],
 ['模式1/2互换与暂持旋转优先','模式3默认4×4筛选；2×3末格空白错误接受/拒绝','模式6 3×2向上列移越界反例','模式4初始恒等进入完成；完成BACKtrue/未完成BACKfalse','默认4×4模式6五次奇排列；模式7W奇性证明与S偶性约束','箭头显示门与可移动方向分离'],
 '本次按源算式与固定向量静态核对，未运行生成器/求解器；既有尺寸异常保留。', ['非默认尺寸的完全可达性','最短解及最终分布','位图整除/像素布局与按键帧时序'], ['User Interface','Demo / Developer Experience','Generic Kernel'])

for idx in (16,17,18):
    caps[idx]['evidence_level'].append('TOOL_VALIDATION')
    caps[idx]['tool_validation'] = 'data-validation.json；仅字面数据核验已执行，能力行为未执行'

# Full formal corpus counter-search. Retain file/line anchors, not copied prose.
queries = [r'(图鉴|Pokédex|Pokedex).{0,80}(普通|异色|闪光|shiny)',
           r'(异色|闪光|shiny).{0,80}(图鉴|Pokédex|Pokedex)',
           r'(忽略|丢弃|固定|强制|不显示|不展示).{0,40}(异色|闪光|shiny)',
           r'(普通外观|普通配色|非闪光|non.?shiny)',
           r'(last_form_seen|pbUpdateDummyPokemon|setIconBitmap)']
negative = {'scope': 'all 131 formal Markdown files including appendices, tests and scope', 'files_searched': len(list(FORMAL.rglob('*.md'))), 'queries': []}
for q in queries:
    hits = []
    for p in sorted(FORMAL.rglob('*.md')):
        for n, line in enumerate(p.read_text().splitlines(), 1):
            if re.search(q, line, re.I):
                hits.append({'path': str(p.relative_to(ROOT)), 'line': n})
    negative['queries'].append({'regex': q, 'matched_lines': len(hits), 'hits': hits})
negative['read_contexts'] = [spec('dex','§2–4、§6'), spec('dexui','§5–7'), spec('resources','§4.1'), spec('input','物种图标合同，行206'), spec('user-interface/wp66-a-party-and-summary-ui.md','邮件图鉴图标、摘要异色红编号，行125、143'), spec('demo-dx/wp72-debug-contexts-and-controls.md','填充盒子与异色登记，行115、129、164、207'), spec('uitest','BX B20–39；未见固定普通外观向量'), spec('pktest','PD01–34；末次异色字段/形式浏览均未给图像消费规则')]
negative['result'] = '未找到图鉴选中预览/条目图像固定普通外观的承接。命中记录写入、调试登记、摘要红编号、邮件个体快照及通用资源回退，均不补足本调用方的固定参数。'
negative['source_counter_search'] = {'scope': 'R/Data/Scripts 全部脚本', 'terms': ['class PokemonPokedexInfo_Scene','def pbUpdateDummyPokemon','def setIconBitmap','shiny','DEX_SHOWS_ALL_FORMS'], 'result': '本固定脚本集只定位这两处图鉴消费者定义；直接读取入口调用和取图透传，未见后续覆写或配置改为采用保存的异色字段。插件未取得、不推断不存在。'}
write('negative-evidence.json', negative)

finding = {
 'id': 'GR4-M11-001', 'title': '图鉴预览和条目固定请求普通外观的消费规则未进入正式合同',
 'module': 'M11', 'severity': 'P2', 'disposition': 'REQUIRED', 'status': 'CONFIRMED',
 'reviewer': reviewer, 'category': '实现信息不足', 'classification': ['User Interface','Pokémon Rules','Engine / Overworld Integration'],
 'source_baseline': source_baseline, 'source_anchors': caps[5]['source_anchors'],
 'specification_baseline': spec_baseline, 'spec_anchors': caps[5]['spec_anchors'],
 'expected_reference_behavior': '图鉴保留seen-form及末次形态中的异色记录，但主列表选中物种预览与条目刷新只消费保存的性别/形态，图像选择固定为普通外观。完整Info/Forms前图、背图、Forms物种图标及获得后的简略Info同样处理；没有异色浏览切换。普通刷新本身不把末次记录的true改false，进入形态选择器的首轮写入是另一条已经记载的副作用。',
 'current_spec_behavior': 'WP62描述异色维度与末次三元组、展示消费者；WP66-B说明图像/形态展示及选择器三参写入导致异色默认false，但没有规定选择器以外的图像请求固定false。WP15只给按已提供属性的资源选择与回退。',
 'gap': '仅依正式集合不能确定末次异色true时应请求普通还是异色图像；现有通用资源合同允许两种调用方输入，无法唯一复现参考。',
 'preconditions': ['固定R，无插件或临时外部改写；合法已见/已拥有BULBASAUR雄性形态0，末次形态为[0,0,true]。可由合法异色个体登记/最近见到形成，不要求执行真实事件。', '普通图鉴入口资格、地区/物种/metrics/消息/输入/宿主成立；用于区分视觉的假设资源同时提供相互不同的普通和异色前图/背图/图标。本轮这些媒体实际不可得。', '先检查普通预览和Info，未进入Forms选择器；以直接符合条件的简略条目入口作另一个独立夹具。'],
 'minimal_counterexample': {'input': '上述末次异色true，打开主列表选中BULBASAUR，随后打开完整Info；不调用形态选择器。', 'reference': '两处请求普通前图；保存末次异色仍true。独立简略Info同样请求普通前图。', 'alternative_allowed_by_current_spec': '实现方把末次三元组完整传给通用资源服务，从而显示异色；数据/资格/形式切换描述都可满足，视觉仍偏离R。', 'evidence_level': 'DERIVED_VECTOR', 'execution_status': 'NOT_EXECUTED'},
 'normal_case': '相同输入只有末次异色false：仍请求普通外观；读取性别、形态和已见/拥有资格不变。',
 'failure_or_boundary_case': '仅异色见过可满足形态资格，图像仍普通；若没有普通/通用图而只有异色图，普通请求不据保存true改查异色，最终依WP15普通请求回退/无图合同，不臆测宿主崩溃。进入多项形态选择器后首轮会另将末次异色写false，此已有合同不可冒充进入前的消费规则。',
 'impact_on_independent_implementation': '玩家仅见到/获得异色后首次打开图鉴，就可能看到与参考不同的外观；错误会贯穿列表预览、完整条目和简略条目，并可能把正确的异色记录误清除来达到普通显示。',
 'negative_evidence_search': {'artifact': 'negative-evidence.json', 'scope': negative['scope'], 'queries': queries, 'result': negative['result'], 'source_counter_search': negative['source_counter_search']},
 'proposed_spec_change': '在WP62记录→展示交界及WP66-B列明哪些图像请求固定普通外观，保留性别/形态选择和异色记录；明确普通刷新不清记录、Forms选择器才有既有写入。补true/false成对静态向量，并为完整/简略入口交叉引用。只补参考事实，不要求未来沿用同名方法/对象，不自行决定是否改进异色浏览政策。',
 'acceptance_criteria': [
   {'kind': 'STATIC', 'criterion': '仅读正式集合即可判定末次异色true时主列表选中预览、完整Info/Forms前后图及图标、简略Info均请求普通外观。'},
   {'kind': 'STATIC', 'criterion': '普通预览/Info刷新不改变保存的异色true；与进入Forms选择器首轮写false的已有合同明确分开。'},
   {'kind': 'STATIC', 'criterion': '有同性别/形态的末次true/false成对向量，及仅异色已见的形态资格对照；不将资源回退误作固定普通选择的原因。'},
   {'kind': 'STATIC', 'criterion': '不改WP15通用按属性取图合同，不把规则推广到队伍/摘要/战斗个体外观；新向量标记未执行。'},
   {'kind': 'RUNTIME_OPTIONAL', 'criterion': '不以当前无媒体/宿主阻止事实修订；如后来运行，应另提供正常/异色相异资源、命令输入及实际输出记录，不能把本轮静态推导标成执行。'},
 ],
 'affected_files': [str('deliverables/final-specification-set/' + P[k]) for k in ('dex','dexui','pktest','uitest')],
 'shared_contracts': ['WP62记录消费','WP66-B图鉴UI','WP15通用物种图像参数与回退；不要求修改通用规则'],
 'dependencies': ['图鉴普通登记/最近见到','物种图像与图标资源选择','完整/简略条目入口'],
 'related_capabilities': ['GR4-CAP-M11-006'], 'related_findings': [], 'root_cause_group': 'M11-pokedex-record-versus-image-variant',
 'history_links': {'relation': 'new', 'third_round': None, 'second_round': None, 'note': 'GR3-M11-001仅栖息地掩码，独立回归仍支持CLOSED；本项不是重开。未知第二轮关联不猜ID。'},
 'evidence_level': ['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'], 'execution_status': 'NOT_EXECUTED',
 'confidence': 'HIGH_STATIC', 'unknowns': ['实际图像像素、媒体/宿主效果','未来产品是否主动提供异色浏览的政策取舍','外部插件行为'],
 'excluded_claims': ['不声称图鉴不记录异色','不声称普通刷新清除末次异色','不把主列表预览误称每行拥有标记图标','不声称真实地图/事件已可达或运行成功','不判定参考固定普通外观是应修复的游戏bug'],
 'user_decision_needed': False,
 'review_resolution': '独立静态确认一项规格缺口，待父汇总者安排针对性反证/去重；未修改正式规格。',
 'primary_owner': 'M11', 'projection': ['M10 / WP66-B'],
}
write('findings.json', {'schema_version':'1.0','findings':[finding]})
write('capabilities.json', caps)

regression = [{
 'id':'GR3-M11-001', 'module':'M11', 'reviewer':reviewer,
 'historical_status':'CLOSED', 'historical_status_changed':False,
 'current_specification_baseline':spec_baseline,
 'current_file_anchors':caps[4]['spec_anchors'], 'source_anchors':caps[4]['source_anchors'],
 'old_acceptance_fixed_references':[
   {'commit':'d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65','path':'review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/findings.json','item':'GR3-M11-001 / acceptance_criteria'},
   {'commit':'1cb48da29e9363a2947eb16c75461bc3e76ae726','path':'review/remediation-third-20261012-prepare/U05/actual-integration/independent-review/attempt-01/per-id-verdicts.json','item':'verdicts5 / GR3-M11-001；实际6eb83dc0f4c9b2cbaf4bc5a6a972387a49ae4ea1'},
   {'commit':'c2eb74c7cbcf8a190d5e902d871fbce44904efd6','path':'review/remediation-third-20261012-prepare/registration/U05-formal-acceptance.json','item':'accepted_ids含GR3-M11-001；FORMALLY_ACCEPTED_EXACT_ACTUAL_SCOPE'},
 ],
 'criteria_checked':[
  {'criterion':'HAB01/02可计算1格/5格、缺尾格','actual_check':'当前WP62行123–135与source313–351逐项回读；宽3文本10000/11111的已有字符索引给出对应格，不补第6格。','consumer':'WP66-B Area页','result':'supported'},
  {'criterion':'HAB03缺省/宽0与各资格门分离','actual_check':'source337–340只有宽>0启用形状；地图资格与可见Point在各自门判断；当前WP62行136和HAB03一致。','consumer':'Area要点生成','result':'supported'},
  {'criterion':'HAB04并集/首条、版本缺陷并存','actual_check':'Point全集收集与RegionMap首条查询独立；当前WP62行137–139、WP63行47、Encounter枚举53–59一致。','consumer':'Area/地图名称/详情/治疗点','result':'supported'},
  {'criterion':'静态场景不升级执行','actual_check':'当前正文139与U05向量标NOT_EXECUTED；本轮未调用该生成器或宿主。','consumer':'规格与测试目录证据口径','result':'supported'},
 ],
 'result':'supported', 'meaning':'supported_static；旧CLOSED保持，非重新发证或运行PASS',
 'evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'], 'execution_status':'NOT_EXECUTED',
 'limits':['非01文本与越界另保留','真实地图/UI/媒体未执行','新GR4-M11-001系独立显示参数缺口，不属于该旧验收'],
}]
write('regression.json', regression)

# File-level reverse coverage is limited to the contracts actually checked above.
coverage = []
formal_relevant = sorted(set(a['path'].removeprefix('deliverables/final-specification-set/') for c in caps for a in c['spec_anchors']))
for rel in formal_relevant:
    path = 'deliverables/final-specification-set/' + rel
    linked = [c for c in caps if any(a['path'] == path for a in c['spec_anchors'])]
    checked = [a['section_or_vector'] for c in linked for a in c['spec_anchors'] if a['path'] == path]
    partial = rel in (P['dex'], P['dexui'], P['uitest'], P['pktest'])
    coverage.append({
       'path':path, 'specification_baseline':B,
       'contracts_checked':list(dict.fromkeys(checked)),
       'source_anchors':list({(a['path'],a['lines_or_symbol']):a for c in linked for a in c['source_anchors']}.values()),
       'status':'partial' if partial else 'supported',
       'support_evidence':[{'capability_id':c['capability_id'],'scope':c['description'],'status':c['status']} for c in linked],
       'evidence_level':['SOURCE_STATIC','SPEC_STATIC'],
       'dependencies':list(dict.fromkeys(a['path'] for c in linked for a in c['spec_anchors'] if a['path'] != path)),
       'unsupported_assertions':(['遗漏固定普通外观图像请求，GR4-M11-001；不是宣称整份文件事实错误'] if partial else []),
       'not_checked':['仅检查上述章节/向量；本文件其它共享模块不在本轮通过范围','宿主、媒体与插件完整行为'] + list(dict.fromkeys(n for c in linked for n in c['not_checked'])),
       'status_meaning':'supported仅为所列合同的supported_static，不是全文件/模块通过',
    })
for rel, scope in [('scope-statement.md','§2材料/具名未读、§3证据层级、§4净化、§5不声明完整运行；历史审批层未重裁'),('README.md','集合导航和范围限制；当前身份从共享baseline取用，不以历史审批文字转授'),('test-catalog/README.md','目录导航与使用约定：条目为静态推导预期；历史数量/审批不作运行证据')]:
    coverage.append({'path':'deliverables/final-specification-set/'+rel,'specification_baseline':B,'contracts_checked':[scope],'source_anchors':[],'status':'partial','support_evidence':['读取范围与证据口径，并与共享baseline材料限制对照'],'evidence_level':['SPEC_STATIC'],'dependencies':['共享baseline.json'],'unsupported_assertions':[],'not_checked':['全局历史审批身份/统计逐项复核归汇总者','其余历史层正文未全文审查'],'status_meaning':'导航/范围局部读取，不是行为审查通过'})
write('spec-coverage.json', coverage)

# Search inventory includes hits and explicit directly relevant files. A hit is not a semantic read.
pattern = r'pokedex|pok[eé]gear|triad|duel|slotmachine|voltorb|mining|lottery|tilepuzzle|regional_dex|Phone::|town_map'
proc = subprocess.run(['rg','-l','-i',pattern,str(R/'Data/Scripts'),str(R/'PBS'),str(R/'Text_english_core')],capture_output=True,text=True,check=False)
paths = {str(Path(p).relative_to(R)) for p in proc.stdout.splitlines()}
paths.update(a['path'] for c in caps for a in c['source_anchors'])
paths.update(['PBS/phone.txt','PBS/town_map.txt','PBS/items.txt','PBS/types.txt','PBS/trainers.txt','PBS/trainer_types.txt','PBS/map_metadata.txt','PBS/encounters.txt','PBS/regional_dexes.txt','townmapgen.html'])
paths.update(str(p.relative_to(R)) for p in (R/'Text_english_core').glob('*') if p.is_file())
semantic = {}
for c in caps:
    for a in c['source_anchors']:
        semantic.setdefault(a['path'], []).append({'locus':a['lines_or_symbol'],'fact':a['fact'],'capability_id':c['capability_id']})
inventory = []
for p in sorted(paths):
    kind = 'read_semantically' if p in semantic else 'inventoried_only'
    if p == 'PBS/items.txt':
        kind = 'read_semantically'
        semantic[p] = [{'locus':'48个挖矿身份及Pocket字段，见data-validation.json','fact':'仅静态字面解析并与附表比较；非全物品域审查','capability_id':'GR4-CAP-M11-019'}]
    inventory.append({'path':p,'material_availability':'available' if (R/p).is_file() else 'not_present_at_exact_path','review_depth':kind,'read_anchors':semantic.get(p,[]),'not_checked':['未列语义锚点部分未审；匹配词/存在性不等于解析或行为支持']})
write('source-scope.json', {'schema_version':'1.0','source_baseline':source_baseline,'discovery':{'tool':'rg --files / rg -l -i','pattern':pattern,'scope':['Data/Scripts','PBS','Text_english_core'],'search_exit_code':proc.returncode,'interpretation':'显式主文件/依赖补入；宽搜索含无关导航命中，保守登记为仅盘点；不以命中数为覆盖分母'},'files':inventory,'unavailable_or_not_reviewed':[{'scope':'Graphics/Audio/真实地图/完整Demo','availability':'unavailable','review_depth':'not_reviewed'},{'scope':'Data/Scripts.rxdata、Data/messages_core.dat及其他序列化数据','availability':'available_per_shared_baseline','review_depth':'not_reviewed'},{'scope':'Gen 5/6/7/8 backup、pokemon_metrics全量、翻译全文、工具townmapgen运行','availability':'available','review_depth':'not_reviewed'},{'scope':'插件与动态注入、宿主音画及系统兼容','availability':'not_established','review_depth':'not_reviewed'}]})

validation = json.loads((OUT/'data-validation.json').read_text())
write('execution.json', {
 'actual_executions':[{'execution_id':'GR4-M11-DATA-001','evidence_level':'TOOL_VALIDATION','purpose':'比较三附表与源字面数据；非行为测试','pre_execution_plan':'validation-plan.md','tool':'exec_command / python3','command':validation['command'],'version':validation['python_version'],'started_at':validation['started_at'],'finished_at':validation['finished_at'],'inputs':['R 三个小游戏脚本文本','B 三个数据附表','PBS/items.txt'],'output':'data-validation.json','result':validation['counts'],'mismatches':validation['errors'],'exit_code':validation['exit_code'],'side_effects':validation['side_effects'],'execution_status':'COMPLETED'}],
 'not_executed':[{'scope':'参考Ruby/游戏宿主/Demo事件/媒体与音频','execution_status':'NOT_EXECUTED'},{'scope':'图鉴普通外观反例与全部正文/目录行为向量','execution_status':'NOT_EXECUTED','evidence_level':'DERIVED_VECTOR'},{'scope':'Triad/老虎机/Voltorb/挖矿/彩票/拼图随机生成、完整对局、概率模拟','execution_status':'NOT_EXECUTED'},{'scope':'编译、反序列化、备份世代切换、真实存档、网络与外部账户','execution_status':'NOT_EXECUTED'}],
 'administrative_note':'常规读取、文本检索、JSON产物生成/校验不是行为执行；本轮仅上列字面数据核验构成专项工具验证。',
})
write('review-identity.json', {'module':'M11','reviewer':reviewer,'parent_thread_id':'01a12fc2-e8c0-7e43-a721-ccfe659d75c8','source_baseline':source_baseline,'specification_baseline':spec_baseline,'completed_at':datetime.now(timezone.utc).isoformat(),'independence':'本轮独立读参考与当前正式集合后判断，旧PASS只作导航；未启动其他agent','write_scope':str(OUT)})
print(json.dumps({'capabilities':len(caps),'spec_coverage_records':len(coverage),'source_inventory':len(inventory),'findings':['GR4-M11-001']},ensure_ascii=False))
