"""Human-authored meaningful clauses, not token/line/semicolon splitting. Static audit only."""
from pathlib import Path
import json,datetime
O=Path(__file__).resolve().parent; P='deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md'
A={
13:['持久HP与上限规则','持久异常与计数规则','持久moves/first_moves规则','持久每Move的PP/提升计数规则','持久item与战斗临时分界','还原记录终局读取语义'],
36:['HP与totalhp存个体','status与statusCount存个体','moves及first_moves存个体','PP与ppup存每Move','持物存个体','跨战斗对象保持不同于native存档实测'],
37:['战内能力阶级为局部','战内效果标志为局部','替换用Move副本为局部','局部不自动成为保存值'],
38:['BattlerHP写穿个体','Battler异常写穿个体','Battler计数写穿个体','Battler持物写穿个体','PP只有专门同步入口具写回语义'],
39:['开战逐成员item初始化还原表','永久消耗可清记录','永久移出可清记录','终局读届时记录写成员','不保证原始item永远返还'],
40:['非蛋HP<=0才fainted','非蛋HP>0才able','蛋fainted为false','蛋able为false'],
41:['heal_HP蛋早退','heal_status蛋早退','heal_PP蛋早退','heal蛋早退','can_relearn蛋拒绝','进化具体入口须分别审定'],
42:['sleep计数表示剩余回合','poison0普通','poison1表示剧毒','其它状态无本层独立计数语义'],
50:['本节HP字段入口范围区别heal_HP直接写与calc_stats条件性调用HP setter'],
52:['写HP最低0','写HP最高最近totalhp','HP上限不在此即时重算'],
53:['HP结果0请求heal_status','非蛋该请求写NONE','非蛋该请求count0','蛋该请求早退留旧异常','蛋该请求留旧count','ready_to_evolve恒false不受蛋守卫'],
54:['Shadow包装先走原HP setter','结果HP<=0清hyper_mode','蛋也经过该附加清理'],
55:['calc_stats可能改totalhp','重算HP按旧缺血量保留','旧HP0上限正增加可得到正增量'],
57:['totalhp与五项实能力由calc_stats写','able/fainted均排除蛋'],
63:['heal_HP无输入','蛋早退','非蛋直接HP=totalhp','不走HP setter0分支','保status','保count','保PP','保ready_to_evolve','保happiness'],
64:['heal_status蛋早退','非蛋不要求able','非蛋可HP0','写NONE','写count0','保HP','保PP','保ready_to_evolve'],
65:['heal_PP蛋早退','nil索引则遍历全部Move','非nil只处理对应槽','每槽当前PP=total_pp','保HP','保异常','保ready_to_evolve'],
66:['heal蛋早退','非蛋先heal_HP','再heal_status','再heal_PP','最后ready_to_evolve=false','保happiness','保来源','保Owner','前段异常截断后续无回滚'],
67:['Trainer.heal_party按当前party顺序','逐成员调用heal','蛋仍由成员守卫','中途异常可只治疗前缀'],
69:['部分HP新值=current+量','超上限取上限','经HP setter写','pbHPItem拒绝不可用','拒绝已满并提示','REVIVE仅fainted','普通复活floor(totalhp/2)','所得<=0再写1','随后heal_status','MAXREVIVE回满','MAXREVIVE清异常','MAXHONEY复制同handler','REVIVALHERB回满清异常后扣happiness','后段演出异常不回滚已写HP'],
71:['野外败/平局治疗具名caller待完整审','比赛失败/黑屏重开治疗具名caller待完整审','设施胜利治疗具名caller待完整审','storage存入治疗保存ready标志后恢复','DayCare存入治疗与取回差别待完整审','解释器param0配置分支待完整审','治疗球捕获调用heal','状态道具调用heal_status','这是非穷尽目录'],
75:['四治疗蛋均无效果','不报错','蛋仍可calc_stats改HP','蛋仍可calc_stats改totalhp'],
76:['heal_HP单项保异常','heal完整非蛋清异常','单项治疗不得推广完整治疗结果'],
77:['heal保happiness','保来源','保昵称','保招式标识与顺序','保ppup','PP回到含ppup的total_pp'],
78:['正常非蛋hp=0后状态NONE','正常非蛋hp=0后count0','hp0非蛋heal_status可调用','蛋heal_status不改旧状态'],
79:['过上限写成上限','负HP写0','负HP走清状态与ready及hyper各守卫'],
87:['注册NONE第1','SLEEP第2','POISON第3','BURN第4','PARALYSIS第5','FROZEN第6','SLEEP动画Sleep图标0','POISON动画Poison图标1','BURN动画Burn图标2','PARALYSIS动画Paralysis图标3','FROZEN动画Frozen图标4','NONE图标默认0无animation','濒死/病毒额外icon资源在底部','创建经heal_status初始化NONE/count0'],
91:['status=先able门','蛋静默拒绝','fainted静默拒绝','守卫先于解析'],
92:['可用者输入Symbol/String/Status记录解析','未知解析nil后raise','错误含输入类型','非法类型校验raise','失败不写新status'],
93:['成功写规范status.id','保statusCount','调用者负责另写count'],
97:['SLEEP的count表示回合','实际递减序列归WP44'],98:['POISON/count0普通','POISON/count1剧毒','战内Toxic计时另字段'],99:['其它状态count没有本层独立语义','不据任意count推新异常'],
100:['正常正count的POISON收尾清0；实际helper对所有POISON写count0不检查正值','其它状态不由该门清count','创建count0','完整heal非蛋count0'],
106:['Battlerstatus setter写局部后个体再UI','Battlercount setter写局部后个体再UI','睡眠递减实际caller仍需具体读'],107:['野外收尾仅以status==POISON为门写count0；正常正count充分而非必要条件'],108:['heal_status非蛋NONE','heal_status非蛋count0'],109:['状态治疗道具经heal_status','正常包外先有蛋/使用资格'],110:['捕获满队移出成员先毒计数归普通','送盒保存的是清后count'],111:['debug存在直接异常读写面','完整debug入口未读不授普通路径信用'],
115:['不可用status=非法身份仍静默','不可用status=非法类型仍静默','able门早于validate'],116:['statusCount accessor不校验范围','负值原样存','过大值原样存','正常producer资格独立'],117:['HP setter0非蛋清异常','蛋0保异常/count','不扩展成任意rawinstancevar写都清'],
125:['正常初始化至多4','学习UI使用4槽','moves字段整表无统一长度守卫','允许空数组','列表有序','每对象id','每对象pp','每对象ppup','每ppup总PP按20%算'],126:['numMoves=list.length','hasMove先try_get','未知false','合法id任一槽相等true'],127:['learn_move是静默模型入口','Trainer装载实调','战斗升级实调待CORE具体同步'],128:['learn_move未知无变化'],129:['已会元素从旧位删除','同对象追加末尾','PP保留','ppup保留','不新建'],130:['未会新建Move','新Movepp满','ppup0','追加后length>4只shift一次','输入<=4输出<=4','输入5输出5','不循环缩短'],
131:['标识删除未知无效','标识删除不存在无效','按标识删所有同id','index允许-n到n-1','-1末项','-n首项','越界整数无变','空表无有效index','forget_all_moves清至0','caller取消必须先判负','debug具体非负门未读不据方法猜'],
132:['reset_moves从当前Species movelist','先level<=current','出现重复删旧再追加保最新','保表顺序','末尾取至多4','各新Move对象','PP满','多caller可用不等于逐caller已接'],133:['moves=直接可存5合法对象','不截断','numMoves5','record_first_moves全5','clone全5各Move独立','顺序保持','四槽初始化不推出整表限制'],
134:['withMoves=false创建可空','forget_all_moves可空','ROTOM显式同值回调可空','非蛋Summary空moves绘4占位','USE读nil.display_damage失败','失败前未到BACK循环','直接forget页面先读空首招失败','事件选招封装同早读','普通非蛋非Shadow空槽学习成功','不进入满槽遗忘'],
138:['record_first_moves先清空','遍历当前所有moves','每槽复制id','保重复','保顺序','id=可构造合法同id两槽','记录不改变PP'],139:['add_first_move未知无效','已有id不追加','已有重复不修复','remove_first_move未知无效','合法id删所有相等记录','clear_first_moves清空'],
140:['赠送存入前record','silent赠送record','送partyrecord','hatchrecord','tradingrecord','catchrecord','MysteryGiftrecord','purify补记','debug记录待读','记录是取得时刻快照'],
141:['Bag机器handler传is_TR给pbMoveTutorChoose','成功TR教学后追加first_move','重复已有不新加','成功后外层消费','PartyUse机器成功消费','PartyUse未调用add_first_move','pbLearnMove本体不补first_move','拒绝不补','取消不补','未学会不补','TM57实际TR属性待具体记录确认','TM57教学CHARGEBEAM待具体记录确认','不能以名字推TM分类'],
142:['relearner候选消费first_moves受Settings','can_relearn另消费且不受同开关'],143:['学习不自动更新first_moves','遗忘不自动更新first_moves','first_moves空仍可有level候选'],
147:['can_relearn蛋false','Shadowfalse','有level<=current且未会true','否则有first_move未会true','均无false','不直接检查全部egg_moves'],148:['候选先取合格levelmoves','level候选去重','配置开才取first_moves','仅未会且非level候选','记录放level候选前','最终并集去重','不直接追加egg_moves全表','孵化蛋招通过record进入','BagTR通过add进入','开关关不追加record','模型can_relearn仍看record'],149:['未知move兼容false','tutormoves命中true','levelmoves命中true不受当前level','eggmoves命中true','本种eggmoves为空才查baby species eggmoves','三类皆无false'],150:['本节判定定义不代替WP30全部选择流程'],
154:['total_pp=base_pp+floor(base_pp*ppup/5)','每点20%','本层无0..3域限制'],155:['pp=最低0','最高当时total_pp'],156:['id=严格get规范id','先写id','ppup保留','再旧PP钳至新total_pp','后段钳制异常保留已写id'],157:['ppup=先写任意传值','不做范围夹制','再以当前PP走pp=','正常整数结果按新total_pp夹制'],158:['base20/ppup-6派生total-4','clamp0..-4失败','失败已写ppup-6','旧PP未赋新值','后续pp=也失败','正常PPUP/PPMAX不产生负计数'],
159:['heal_PP逐Move回满','pbRestorePP缺槽return0','缺idreturn0','total_pp<=0return0','超量截上限','持久PP先写','pbBattleRestorePP持久增量0就return','非Transform且战斗槽存在且id相同才同步副本'],
160:['pbSetPP先写包装PP','存在realMove','id相等','非Transform三门才回持久','直接包装pp=不回','多回合不重复扣PP具体门待完整读','negativePP特殊调用不扣具体门待读','total_pp<=0无限具体门待读'],
164:['逐持久Move包装','包装pp独立数值','包装realMove引用原对象','直接pp accessor无写穿'],165:['直接包装pp=只局部','专门setter包装先写','三门通过写realMove.pp','Transform不回','无realMove不回','id不同不回','模仿复制具体构造待各family','战后持久不采纳这些副本'],166:['升级学习先更新持久list','随后同步战斗对应槽','完整升级具体流程尚待CORE具名包'],167:['终局无需整体PP抄回','此前专门setter已同步','捕获record_first_moves'],168:['孵化配置蛋招有独立流程','模型learn_move无蛋守卫','模型forget无蛋守卫','交互pbLearnMove有蛋/debug守卫','具体caller资格不能合并'],
176:['item读取try_get未知nil','item_id读取原始id'],177:['hasItem无参检查非nil','带参用GameData比较','符号可比','字符串可比','记录可比','无itemfalse','未知参数解析语义以registry为准'],178:['wild_items三列表','common池','uncommon池','rare池','pbGenerateWildPokemon按累计概率选','相同三池特殊common分支'],182:['item=nil清除','非nil未知静默return','已登记写规范id','无提示'],183:['Pokemon未知item保旧值','Battler未知try_getnil','Battler局部nil后写穿清Pokemon','两入口不同失败后果'],184:['字段合同不授全部GiveTake流程'],188:['mail读缺失返回nil','mail.item与item_id失配清@mail','mail=仅Mail或nil','其它类型赋前raise','pbStoreMail已有mail则raise','成功Mail构造item严格get','更换持物后延迟mail读取可清'],189:['item与poke_ball独立','捕获写poke_ball不隐含持物'],190:['进化持物清除各caller独立','战内偷打消费各效果独立','不能统一未知校验','还原记录与当前item不同字段'],
194:['Battleritem=先try_get','写局部规范id/nil','写Pokemonitem同id/nil','未知清空'],195:['开战initialItems取当时item','正常消费同当前记录才清记录','永久取失可更新记录','打落临时仅清当前不清记录','各效果族尚非全部审读'],196:['正常终局遍历pbParty0','每索引initialItems0写回','无实际partner且数组同步是逐成员对照前提','partner合并数组可与player.party不同','满队移旧成员会记录错位'],197:['正常消费清当前','同id记录也清','无再获得终局仍nil'],198:['暂时打落清当前','记录原id保留','终局写回原id'],199:['合法永久更新后终局用新记录','不返还不变原快照'],200:['捕获入party追加当前item至initialItems','战后按该记录','直接box不入party还原循环','box保持当时item'],201:['满队移旧者先当前item送box','再删player.party','再左移player initialItems','无partner集合相同时旧者退出还原','实际partner时mergedparty仍持共享旧身份','终局按移后记录可误写box中旧者','也可能误写留队成员','仅登记partner未参战不满足反例','需暂时打落保记录条件','普通永久消费不替代该前提'],202:['本合同仅记录可更新与终局读取','WP50每效果独立定义仍待接'],
208:['HP正常范围0..totalhp','0非蛋NONE','0非蛋count0','蛋保旧异常/count','0readyfalse不分蛋','Shadow0hyperfalse'],209:['治疗蛋无效','异常设置蛋无效','relearn蛋否','进化蛋守卫具体定义待审','蛋重算HP仍写'],210:['status=只able','未知可用raise','非法类型可用raise','成功保count'],211:['sleepcount语义','poisoncount语义','收尾poison正count清0'],212:['初始化至多4','常规UI4','整表可0或>4','静默超限只shift1','reset最近4','已会静默移动末尾','顺序持久'],213:['总PP派生','成功pp=落合法区间','极负ppup先写后失败旧pp可区间外','ppup无域校验'],214:['当前moves与first_moves独立','整表记录保重复','整表记录保顺序','逐项只阻新追加','不修原重复'],215:['HP写穿','异常写穿','count写穿','item写穿','PP专门入口才写穿','副本不自动回写','终局item用当时记录'],216:['个体已知或nil可设','未知忽略','战斗未知清空','mail失配读取清'],
220:['heal_PP索引>=length读nil失败','正常caller全体或有效索引','pbRestorePP缺槽守卫0','pbRestorePP缺id守卫0','heal_PP字段本体不守该空槽'],221:['极负ppup写入后clamp失败','PP仍旧值'],222:['不可用先早退','可用未知raise','可用非法类型raise'],223:['count直接整数原样存'],224:['个体未知item不变','战斗未知item清空'],225:['换item后mail读取失配清空'],226:['过高HP夹上限','负HP归0','非蛋清异常','蛋保异常/count'],227:['送box还原边界按201','各效果族更新点非穷尽'],
233:['HEAL_STORED true才治疗','送box含捕获满队','先存ready','完整heal','再恢复ready','若heal中途raise恢复不保证'],234:['默认代>=6开启relearner更多','决定记录候选追加','不直接加egg全表','不改can_relearn'],235:['捕获经验开关改奖励调用','不直接更改本节字段setter规则','完整经验后继仍按CORE门'],237:['Shadow治疗组合未执行','病毒捕获治疗组合未执行','已静态读包装不升级运行确认'],
250:['满队记录左移事实已接','伙伴映射限定已接','完整WP38反向向量单独接受'],251:['PP同步外其它family未全部接','Transform/模仿不代表每复制族'],252:['睡眠递减具体序列未全接','剧毒独立计时未全接','免疫门未全接'],253:['Mail本体/GiveTake/Write已全文读','邮局及寄存完整UI仍待具名接合'],254:['storage保存ready恢复已读','Shadow经heal_HP直接赋不清hyper可从完整源码推出','其它字段保留须逐字段不推全对象'],255:['蛋招孵化source能力可审','具体工程事件可达性未知','不归材料上限'],256:['全部静态','业务NOT_EXECUTED','场景NOT_EXECUTED']}
ADMIN={3:'分类/实现独立资格。',5:'净化/字段名身份/静态证据与无运行资格。',17:'HP范围导航。',18:'状态范围导航。',19:'招式范围导航。',20:'持物范围导航。',21:'战斗持久交界导航。',25:'WP42/44/40排除边界。',26:'WP50/28/64/38排除边界。',27:'WP30流程外置边界。',28:'进化寄养孵化外置边界。',34:'术语表标题。',61:'治疗入口表标题。',104:'状态写入者表标题。',231:'配置表标题。',241:'45HP例导航与主题清单，不代替逐例接受或运行。',245:'上游依赖导航，不授全域。',246:'下游依赖导航，不授全域。'}
GROUPS={
'HP':dict(source=['Pokemon.hp=/heal_HP/heal_status/heal_PP/heal/calc_stats完整定义','ShadowPokemon完整HP包装','Trainer.heal_party完整定义','Item_Utilities完整917L','Item_Effects412–630完整具名HP/status/revive handlers','Storage/CatchStore/Peers完整定义'],received=['CORE CAR-CRE-F01..11 fullfacts','UI complete P/S/B and finite X units','KERNEL SAVE01..07/EVT01..05'],premise='正常固定R合法个体与有效上限；蛋入口独立；HP字段赋值、直接heal_HP与calc_stats写点分开。',chain='创建或字段/道具/战斗HP写→个体异常/count/ready/hyper→Party/Storage/Catch→Summary/Party图标→player/storage保存注册及load；native图别名尚未执行。',prefix='蛋/无效果守卫先于道具写；SE可能在写前失败；HP/状态先提交后刷新与文字，后段失败保留已达前缀；heal各步骤不构成回滚事务。'),
'MOVES':dict(source=['Pokemon move queries/learn/forget/reset/record/compatible/can_relearn完整定义','Pokemon::Move完整77L','Species/GrowthRate/FormHandlers完整定义','Item_Utilities pbLearnMove/pbUseItem/pbUseItemOnPokemon完整caller','MoveRelearner完整source','Item_Effects move_machines74–91和PP632–713完整handler'],received=['UI S06/S09等具体完整unit保原reader','CORE CAR-CRE PP完整有限facts','KERNEL Species/compiler15facts+41defaults'],premise='列表含合法Move时讨论任意长度；空表与异常对象失败分别限定；正常非蛋非Shadow学习成功；机器元数据属性不可由名字推断。',chain='创建/reset或整表/learn/Move setter→持久moves/first_moves→Summary/Forget/Learn/Relearner→clone/party/storage→player/storage保存对象；原记录与当前招式互不自动同步。',prefix='解析/蛋Shadow/已会/确认/索引取消门各在真实写前；学习新Move写后文字失败不回滚；ppup/id先写后clamp失败保留已写字段和旧PP；外层消费仅成功返回后。'),
'ITEM':dict(source=['Pokemon item/item_id/item=/hasItem?/mail/mail=完整定义','Item_Mail完整125L','Item_Utilities Give/Take/Write调用者完整','CatchStore271L/Peers77L完整源','WildEncounters469L完整生成定义'],received=['CORE CAR-CRE-F01/F11 and CAR-CAA-J04完整有限包','UI P/B/X完整有界units','KERNEL SAVE完整有限join'],premise='默认ordinary battle入口与直接自建Battle分开；参与集合与player.party数组身份是否相同显式区分；raw字段与解析setter分开。',chain='野生生成/赠送/GiveTake/战斗写→Pokemon item/mail→还原记录更新→CatchStore入队/box移位→终局pbParty0按索引写→UI→player/storage保存load。',prefix='未知个体item无写；Battler未知先本地nil再个体清；Mail读取本身可写清；GiveTake取消不保证更早取信/Bag写回；捕获先送盒再删除并移记录，不回滚已写前缀。')}
def group(ln):
 if 125<=ln<=168 or ln in [212,213,214,220,221,234,251,255]:return 'MOVES'
 if 176<=ln<=202 or ln in [215,216,224,225,227,250,253]:return 'ITEM'
 return 'HP'
def main():
 a=json.loads((O/'manual-atomic-clauses.json').read_text());d=json.loads((O/'old-locator-disposition.json').read_text());new=[]
 for r in d['rows']:
  if r['path']!=P:continue
  ln=r['range'][0]; assert not r.get('manual_children'),ln
  if ln in ADMIN:r.update(decomposition='COMPLETE_BOUNDED_TYPE_DISPOSITION',type_disposition=ADMIN[ln],accepted=True);continue
  assert ln in A,ln
  ct=dict(GROUPS[group(ln)]);ct['group']=group(ln);ct['cancel']='Only caller-specific explicit cancel gates apply; setters/heal definitions have no UI cancellation.';ct['business']='NOT_EXECUTED';pending=[]
  if ln in [41,71,106,107,111,131,140,160,166,168,195,198,202,209,235,251,252,253,255]:pending.append('Only explicitly read source/received units accepted; named caller/family terms in this row marked 待读/未全接 remain exact available OPEN, not material limit')
  if ln==141:pending.append('Actual TM57 PBS full record and pbMoveTutorChoose complete producer still to read; Party nonappend and machine dispatcher read')
  ct['open_exact']=pending;ids=[]
  for i,t in enumerate(A[ln],1):
   aid=f'CAA-W20-L{ln:03d}-A{i:02d}';ids.append(aid);new.append(dict(id=aid,old_locator=r['id'],formal_path=P,formal_line=ln,assertion=t,complete_contract=ct,parent_decomposition='MANUALLY_EXHAUSTED_BOUNDED_FORMAL_ROW',source_support='PARTIAL_EXACT_SOURCE_PENDING' if pending else 'SUPPORTED_BOUNDED_STATIC',business='NOT_EXECUTED'))
  r.update(decomposition='MANUAL_EXHAUSTED_BOUNDED_FORMAL_ROW',manual_children=ids,source_support='PARTIAL_EXACT_SOURCE_PENDING' if pending else 'SUPPORTED_BOUNDED_STATIC',consumer=ct,premise=ct['premise'],accepted=False)
 a['atoms']+=new;a['formal_wp20_atoms']=len(new);a['recorded_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();d['manually_exhausted_locators']=sum(bool(r.get('manual_children')) for r in d['rows']);d['fully_accepted_locators']=sum(r.get('accepted',False) for r in d['rows']);d['not_manually_exhausted_locators']=sum(not r.get('manual_children') and r.get('decomposition')!='COMPLETE_BOUNDED_TYPE_DISPOSITION' for r in d['rows'])
 for f,v in [('manual-atomic-clauses.json',a),('old-locator-disposition.json',d)]: (O/f).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
 print('new',len(new),'all',len(a['atoms']),'behavior',d['manually_exhausted_locators'],'typed',d['fully_accepted_locators'],'pending',d['not_manually_exhausted_locators'])
if __name__=='__main__':main()
