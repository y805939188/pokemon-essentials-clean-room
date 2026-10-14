"""Joins human-authored review facts to the structural inventory. No reference execution."""
from pathlib import Path
import csv,json,re
R=Path(__file__).resolve().parent
D=Path('deliverables/final-specification-set/combat-requirements')
names={'A':'wp52-a-generic-numerical-and-status-evaluation.md','AD':'wp52-a-evaluation-coverage-and-data.md','B':'wp52-b-field-damage-healing-and-target-evaluation.md','BD':'wp52-b-effect-coverage.md','C':'wp52-c-items-calling-and-control-evaluation.md','CD':'wp52-c-item-control-coverage-and-data.md'}
facts={}
def put(keys,where,note,contrast):
 for key in keys.split():
  assert key not in facts,key
  facts[key]={'formal':where,'fact':note,'ordinary_boundary_or_countercheck':contrast}
put('DoesNothingCongratulations DoesNothingFailsIfNoAlly DoesNothingUnusableInGravity DoubleMoneyGainedFromBattle','A:243;AD:21-24','局部整体偏好固定60，三份复制沿同族已存在行为；不撤销真实动作或奖金。','ScoreMoves关闭不消费；60以后仍可被通用整体修正。')
put('FailsIfNotUserFirstTurn','A:243;AD:25','命令时点在场轮大于0预测失败，否则整体偏好加25。','轮0与1，预测关不能补20；评分关不能补25。')
put('FailsIfUserHasUnusedMove','A:243;AD:26','排同身份槽后必须存在其它招且所有其它身份已用；不以PP判断用过。','只有同身份槽亦失败；其它招全用与仍有未用对照。')
put('FailsIfUserNotConsumedBerry','A:243;AD:27','仅按已打嗝资格记录作失败预测。','持果而未有记录不等于已消费。')
put('FailsIfTargetHasNoItem','C:100;CD:34','无物或当前物无效预测目标失败，未登记专用价值分。','预测关闭不触发这道失败；真实可选及效果仍独立。')
put('FailsUnlessTargetSharesTypeWithUser','A:243;AD:28','双方包含额外类型的当前集合无交集时预测目标失败。','额外类型构成交集足够；原基础类型不共同不必失败。')
put('FailsIfUserDamagedThisTurn','C:156;CD:36','先按U与全部存活敌的粗速计数，U不快于任何敌给60、全快加15；高档按T不能动/混乱或迷恋指向U/麻痹互斥加15/10/5；HP意识按T半血及四分之一各减10。','只需U至少快过一个敌可继续；高档状态三分支不叠加，HP两项可叠加。')
put('FailsIfTargetActed','C:156;CD:36','T比U快或T无可用伤害招给60；否则HP意识依T半血/四分之一各减10。','不读取已选招或本轮已行动；同速按粗速空间反转。')
put('CrashDamageIfFailsUnusableInGravity','B:216;BD:19','可间伤时减去向0截断的0.6乘100与粗命中之差；不可间伤保持。','粗命中110导致局部加6；不补坚硬脑袋免罚。')
for k,w in [('StartSunWeather','晴'),('StartRainWeather','雨'),('StartSandstormWeather','沙'),('StartHailWeather','雹'),('StartShadowSkyWeather','暗影天')]:
 put(k,'B:148-170;BD:21,23',f'{w}整招失败沿共同已有极端/同天气条件；有效全局天气阻断给60；HP意识低于整数半血减'+('15' if k=='StartShadowSkyWeather' else '10')+'，高档先减旧收益再加新收益。','失败门读存储天气；旧期限1不会免失败；新收益含starting，能力全局门先行。')
for k,t in [('StartElectricTerrain','电'),('StartGrassyTerrain','草'),('StartMistyTerrain','雾'),('StartPsychicTerrain','超能')]:
 put(k,'B:150,172-174;BD:21,23',f'已有{t}地形预测失败；HP意识低于半血减10，高档先减旧地形收益，再加拟建{t}地形收益。','不以当前到期轮数跳同地形门；种子收益和接地者收益由不同遍历消费。')
put('RemoveTerrain','B:150;BD:21,23','无当前地形预计失败；效果分减当前地形收益，不先判正负。','去掉对己方有利地形可减分；非None的负收益反而加分。')
for k,cap,rate,filters in [('AddSpikesToFoeSide',3,'10/7/5','浮空与魔法防守'),('AddToxicSpikesToFoeSide',2,'8/5','浮空与不可中毒近似'),('AddStealthRocksToFoeSide',1,'10','魔法防守'),('AddStickyWebToFoeSide',1,'8','浮空')]:
 put(k,'B:178;BD:21,23',f'已有上限{cap}层/标记则失败；敌方整侧队伍排非可战斗和当前存活场上索引，中等排靴并排{filters}；无合格后备60，否则每人按{rate}，最多30。','低档不使用中等过滤；当前倒下在场成员的队伍索引不由存活集合排除；BD21误定位到5.1需订正5.2。')
put('SwapSideEffects','C:193,197;CD:38,40,183-184','失败扫描实际数值/布尔名单，两侧皆空才失败；中等坏组己非空加10、敌排0/1才减10，高档好组敌排0/1加10、己非空减10。','布尔真不等整数1；火海湿地确在好组；层1敌坏组与己坏组不对称。')
put('UserMakeSubstitute','B:180;BD:21,23','已有正替身或HP不超过整数四分之一且至少1预计失败；HP意识按当前HP比四舍五入加0..10，每敌无可用绕替身招加5，上次损HP至少整数四分之一加7。','HP门含等号；最近损失门无HP意识要求；不估未来挡伤量。')
put('RemoveUserBindingAndEntryHazards','C:194;CD:40','当代先消费自身升速1整体评分；束缚正加10、种子非负加15，己有后备才按菱毒菱网各15、岩20加分。','升速得到60也继续清除偏好；无后备不计危害而可计种子。')
put('AttackTwoTurnsLater','B:180;BD:23,25','目标位置已有未来攻击正计数失败；整体己无可战斗后备减20。','两个阶段分别登记；不将目标在落下时身份变更预测成失败。')
put('UserSwapsPositionsWithAlly','C:195;CD:38,40','传侧号作盟友索引，后筛同业主与邻近，数量不等1预计失败；整体固定减30。','自身高席位可过初筛但邻近拒自身；席0/席2对照不等同正常盟友枚举。')
put('BurnAttackerBeforeUserActs','C:158;CD:40','逐敌需接触效果许可且中央可烧，加10；高档另需可用实际接触招。','高档查招与中央烧资格独立；不建立真实反烧。')
put('AllBattlersLoseHalfHPUserSkipsNextTurn','B:140;BD:23','逐存活者排HP1，敌/己分别累计当前HP整数半；加整数20敌/己、减整数20己/敌，然后接休息评分。','任一累计0除零；外层候选异常可保持100，非本处理器60。')
put('UserLosesHalfHP','B:130;BD:23','转交扣总HP一半族的整体偏好，未因此改变本招真实扣当前HP一半。','HP意识25/75边界及高档后备加分仍沿被调用合同。')
put('RemoveAllScreensAndSafeguard','B:184;BD:21,23','两侧三墙和神秘守护均无正则失败；敌四计数均至多1给60，否则己视角清墙收益减首敌反视角收益，再敌守护加10己守护减10。','计数1可免失败但不必有收益；当前成员存活集合过滤，非双方全员重复扣。')
# Ordinary parameterized stat families were read at each copy declaration; identities retain actual parameters.
for stem,stat in [('Attack','攻击'),('Defense','防御'),('SpAtk','特攻'),('SpDef','特防'),('Speed','速度'),('Accuracy','命中'),('Evasion','闪避')]:
 for n in [1,2,3]:
  put(f'RaiseUser{stem}{n}','A:116-140;AD:34-61',f'自身{stat}+{n}：变化招中央不能升才整失败；效果按实际请求量送升阶资格/方向/残余/天然/单纯/封顶和各项增量。','失败与效果评分族分开；伤害附效不因不能升整败；复制不冻结原始攻击参数。')
for k,stat in [('RaiseUserAtkDef1','攻击/防御各1'),('RaiseUserAtkDefAcc1','攻击/防御/命中各1'),('RaiseUserAtkSpAtk1','攻击/特攻各1'),('RaiseUserAtkSpd1','攻击/速度各1'),('RaiseUserAtk1Spd2','速度2/攻击1'),('RaiseUserAtkAcc1','攻击/命中各1'),('RaiseUserDefSpDef1','防御/特防各1'),('RaiseUserSpAtkSpDef1','特攻/特防各1'),('RaiseUserSpAtkSpDefSpd1','特攻/特防/速度各1'),('RaiseUserMainStats1','五主项各1')]:
 put(k,'A:116-140,163;AD:63-74',f'自身多项{stat}：变化招任一中央可升则不全败；效果使用真实多项请求并逐项筛收益，非真实镜甲整招前检。','伤害招不全败；仅一项封顶与全部封顶对照；复制读取实际请求顺序和量。')
for k,n in [('RaiseUserAttack2IfTargetFaints',2),('RaiseUserAttack3IfTargetFaints',3)]: put(k,'A:148;AD:36,38',f'粗伤达到目标当前HP的0.9倍时才评自身攻击+{n}，否则保持输入。','阈值含等号，并非仅粗伤足以真实击倒；未登记失败。')
put('MaxUserAttackLoseHalfOfTotalHP','A:149;AD:39','当前HP不超过max整数半总HP与1或攻不可升则失败；升攻请求12夹上限后再HP意识浮点扣缺HP比例60。','H101/h50失败而51可评；不先实际扣HP，不将中途浮点先截断。')
put('RaiseUserDefense1CurlUpUser','A:150;AD:41','普通防+1后，尚未变圆且有可用滚动再加10。','普通升分60不在本处理器止链，变圆标记不因预测写入。')
put('RaiseUserSpDef1PowerUpElectricMove','A:150;AD:48','特防+1后，有可用电伤害招再加10。','充电实际可消费性未在本处重建。')
put('RaiseUserSpeed2LowerUserWeight','A:151;AD:53','速度+2后，中等且重量大于1，己/各敌重量比威力招减5、敌目标重量威力招加5，六代起2000至小于3000且敌有天空摔投减10。','1与2重量、1999/2000/2999/3000四界；无中等不使用重量偏好。')
put('RaiseUserEvasion2MinimizeUser','A:152;AD:60','闪避+2后，中等且尚未变小，每敌有可用踩踏招减15当代或10旧代。','已变小只保留普通升阶评分；每敌最多一份。')
put('RaiseUserCriticalHitRate2','A:152;AD:62','聚气至少2预计失败；无可用伤害60，否则加15；中等有效对应会心道具加10且有效狙击手另加10。','物种绑定幸运拳/大葱/棍分别核；无中等不加两个10。')
put('RaiseUserAtkSpAtk1Or2InSun','A:153;AD:66','实际有效晴/大日照把攻特攻请求各改2，其它各1；失败仍沿多升资格。','天气伞等作用已包含effectiveWeather；不直接改真实阶级。')
put('LowerUserDefSpDef1RaiseUserAtkSpAtkSpd2','A:153;AD:67','预测升降全部中央不可才全败；先三项各升2，恰60停，否则防特防各降1非whole。','仅下降可施不保证评分不返回60；不把降阶量变负。')
put('RaiseUserMainStats1LoseThirdOfTotalHP','A:154;AD:75','HP不超过整数三分之一且至少1或无可升项失败；五项各1评分非60后，HP意识且HP至多75%才扣整数45乘缺口除总HP。','H100/h75扣11，h76不扣；HP成本不先写入。')
put('RaiseUserMainStats1TrapUserInBattle','A:155;AD:76','已背水标记或多项全不能则失败；五项升评分后，只在能新拘束且可选后备时检查残余致死无收益，或灭亡/迷恋/正残余任一减15。','升评分60不会自动止链；不能新困时不减拘束成本。')
put('StartRaiseUserAtk1WhenDamaged','A:156;AD:77','HP意识且不超过整数三分之一直接保持；攻值得升加10，另有辅助力量加7。','本处不实际请求立即升攻。')
for k,param in [('LowerUserAttack1','攻1'),('LowerUserAttack2','攻2'),('LowerUserDefense1','防1'),('LowerUserDefense2','防2'),('LowerUserSpAtk1','特攻1'),('LowerUserSpAtk2','特攻2'),('LowerUserSpDef1','特防1'),('LowerUserSpDef2','特防2'),('LowerUserSpeed1','速1'),('LowerUserSpeed2','速2'),('LowerUserAtkDef1','攻防各1'),('LowerUserDefSpDef1','防特防各1'),('LowerUserDefSpDefSpd1','速防特防各1')]:
 put(k,'A:116-140;AD:78-90',f'自身下降{param}只登记整体效果，使用实际正下降请求量及降阶共同方向/资格。','伤害招whole强制假，不能因附效无效取消伤害；各copy沿当前同族行为。')
put('RaiseTargetAttack1 RaiseTargetSpDef1','A:116-140,159;AD:91,94','分别目标攻击1/特防1；目标失败中央资格；效果使用相应升阶请求。','前者失败另限定变化招，后者没有该限定；具体处理器不可被同一泛化失败公式盖过。')
put('RaiseTargetAttack2ConfuseTarget RaiseTargetSpAtk1ConfuseTarget','A:157;AD:92-93','分别攻2/特攻1与混乱两者均不能才失败；非有效唱反调或模式破坏且不能混乱给60，否则升阶非whole后接混乱。','唱反调无模式破坏可以只评下降；不能混乱不是普遍整失败。')
put('RaiseTargetRandomStat2','A:158;AD:95','七项无任何中央可升才失败；唱反调无模式破坏或残余致死60，非自身减7、有效单纯加10；HP70%界加10否则向0截断50乘比率减0.6；辅助力量加10、每敌惩罚减8。','不逐随机项目求期望；单纯评分额外10不改变实际随机量。')
put('RaiseTargetAtkSpAtk2','A:159;AD:96','两攻击均不可升目标失败；敌方效果60，己方攻特攻各2共同评分。','效果敌方60后若可敌招盟友反转另消费；不提前挪到真实资格。')
for stem,stat in [('Attack','攻击'),('Defense','防御'),('SpAtk','特攻'),('SpDef','特防'),('Speed','速度'),('Accuracy','命中'),('Evasion','闪避')]:
 for n in [1,2,3]:
  put(f'LowerTarget{stem}{n}','A:116-140,163;AD:97-124',f'目标{stat}降{n}：变化招中央不能降预测失败；目标效果使用实际请求量、正量夹限及共同下降偏好。','伤害附效不能施加不造成整招失败；每条copy保持阶段且读取新招参数。')
put('LowerTargetAttack1BypassSubstitute','A:116-140;AD:98','攻降1同族失败/效果复制；替身绕过沿真实本招性质和通用预测。','不能因copy源普通攻击降阶就丢绕替身性质。')
put('LowerTargetDefense1PowersUpInGravity','A:161;AD:102','防降1失败和分复制；中等基数预测消费实际重力基底：重力正时1.5倍整数商。','输入81得到121，未重力81；基数门中等不等ScoreMoves。')
put('LowerTargetSpeed1WeakerInGrassyTerrain','A:161;AD:113','速降1失败和分复制；中等基数沿实际青草基底：青草半值最近整数。','输入61青草31，否则61；不加接地条件。')
put('LowerTargetSpAtk2IfCanAttract','A:160;AD:107','普通特攻降2资格再排无性别/同性/有效迟钝非模式破坏；分复制普通降2。','模式破坏只取消迟钝门，不取消性别门。')
put('LowerTargetSpeed1MakeTargetWeakerToFire','A:162;AD:114','尚无沥青时失败直接假；已沥青才按变化招降速资格；先降速分，未沥青且己有火伤害及T火非免疫再加10乘相性。','速已最低而沥青未建立仍可加火弱点；不是完整原新类型差值。')
put('LowerTargetAtkDef1 LowerTargetAtkSpAtk1','A:116-140,163;AD:123-124','变化招多降逐请求中央任一可降不全败；目标分沿共同多降。','伤害招不由此拒；真实镜甲整体资格未完整预测。')
put('LowerPoisonedTargetAtkSpAtkSpd1','A:163;AD:125','先需真毒，再多降资格；分复制多降读取攻特攻速各1。','只视为毒的其它状态不够；失败关时分数体仍按自身中央门。')
put('RaiseAlliesAtkDef1','A:164;AD:126','目标攻防任一中央可升即可不全败，目标分攻防各1共同评分。','数据选择盟友集合由消费者，非这个处理器自行枚举后备。')
for k,stats in [('RaisePlusMinusUserAndAlliesAtkSpAtk1','攻击/特攻'),('RaisePlusMinusUserAndAlliesDefSpDef1','防御/特防')]:
 put(k,'A:164;AD:127-128',f'整体失败扫描己存活有效PLUS/MINUS且{stats}任一可升；目标失败再筛能力；UserSide整体分遍历全部己场上{stats}各1非whole，不再筛能力；目标分按两项升。','默认UserAndAllies走目标筛；作者UserSide数据时整体分支可达，目标对象与身份符号比较支持。')
put('RaiseGroundedGrassBattlersAtkSpAtk1','A:165;AD:129','目标需草、非浮空且非半无敌，攻特攻任一可升；目标分各1。','不把非浮空门套给花盾。')
put('RaiseGrassBattlersDef1','A:165;AD:130','目标需草且非半无敌、中央可升防；目标分防1。','浮空草仍能通过本专用资格。')
for k,stats in [('UserTargetSwapAtkSpAtkStages','攻特攻'),('UserTargetSwapDefSpDefStages','防特防'),('UserTargetSwapStatStages','全部七项')]:
 put(k,'A:166;AD:131-133',f'{stats}取T减U正差列表和保持负号的负差列表；没有正差60，否则对U升T降正列表、U降T升负列表，全固定。','负请求被共同正量门丢弃；只负差并非有收益，不能取绝对值修正预测。')
put('UserCopyTargetStatStages','A:167;AD:134','仅U采用同样正/负差；无正差60早退；新会心机制且过早退才按聚气/磨砺新增或丢失分别加减5。','只有聚气不同而无正阶差仍60；不因正列表存在保证项目值得。')
put('UserStealTargetPositiveStatStages','A:168;AD:135','收T七项正阶；U升非固定、T降固定，非whole；无正保持原分。','粗伤在偷阶之前，未预先更新进攻/防御。')
put('InvertTargetStatStages','A:168;AD:136','无变化阶预测失败；正阶两倍入下降、负阶两倍仍负入上升；无正下降列表60，否则固定评分。','全负阶有真实效果却预测无用；负上升量不参与。')
put('ResetTargetStatStages ResetAllBattlersStatStages','A:168;AD:137-138','正阶入下降、负阶直接保持负入上升；固定且非whole；黑雾额外无任何对象改变阶才整失败并逐存活对象累计。','负请求被共同正量门丢弃；不重新调用中央写阶。')
put('StartUserSideImmunityToStatStageLowering','A:169;AD:139','已有白雾正失败；每敌有可用目标单/多降族或毒液陷阱/毒降速/吸取力量任一加15，无匹配敌60。','每敌一份而非每招一份；不可仅查效果名末尾降阶。')
put('UserSwapBaseAtkDef','A:170;AD:140','已力量戏法或基础攻防相等60；防高先需升攻值得，按40倍比提升向0截断，可忽略降防时另5；攻高需升防值得且降攻无用。','不是新旧整招伤害比较，固定变化仍走值得门。')
put('UserTargetSwapBaseSpeed','A:171;AD:141','基础速度同值60；空间剩大于1偏换得低速，否则偏换高；按40倍比提升向0截断。','空间剩1不反转，基础速度不同于粗总速度。')
put('UserTargetAverageBaseAtkSpAtk UserTargetAverageBaseDefSpDef','A:172;AD:142-143','U两项均不低于T60；逐项原值对比，只要相应升或降值得，就按40倍原比改善加或损失减并向0截断；无有用变化60。','不先求均值，不给T的完整战术效益独立二次加权。')
put('LowerTargetEvasion1RemoveSideEffects','B:182;BD:29-30','任何目标侧墙/危害、六代目标对侧危害、八代地形足以不因降闪避失败；评分非敌60，先降阶后继续清理：墙任一大于1加10，两侧危害按各自宽松换人门加减15，八代减地形收益。','墙1免失败但不加清墙10；降阶60也继续清理。')
put('UserTargetAverageHP','B:126;BD:30','U当前HP至少T给60，否则用未夹限浮点平均与U当前HP之比，至少1.2才加向0截断10乘该比。','U50/T69无收益，T70加12；真实均分HP上限和治疗封锁另合同。')
put('StartUserSideDoubleSpeed','B:186;BD:31-32','已顺风失败；中等空间大于1给60；当前己最慢高于敌最快60；严格跨侧速度在一至二倍之间每对加10，另8；0对60。','100对200不计、对199计；不是名义布局。空敌无本地兜底。')
put('StartSwapAllBattlersBaseDefensiveStats','B:188;BD:32','逐存活对象基础防特防不等才作固定改变值得，按20倍比值提升/损失向0截断，敌方反号；无人有意义或累计不大于100给60。','空间已开不自动取反；不同原值但净100仍60。')
put('SleepTarget','A:180,184,190;AD:149','变化招中央不可睡目标失败；睡评分先排瞌睡/治疗果/更快雨中湿润之躯，再中央可睡才附效修正和15；己方协同、早起/鳞片/睡中招与治疗能力分别调整。','附效抑制返回变化60或伤害原分；不把后备加入己侧协同。')
put('SleepTargetIfUserDarkrai','A:194;AD:150','整门需原/变身物种Darkrai，另独立目标睡门，目标分复制睡。','评分身份未使其它物种能正常通过整门。')
put('SleepTargetChangeUserMeloettaForm','A:194;AD:151','仅目标睡分复制，无同名独立失败登记。','不能因SleepTarget有目标失败就推断本键复制了它。')
put('SleepTargetNextTurn','A:194;AD:152','已有瞌睡正或当前中央不能睡失败，目标分复制睡。','预测使用当前可睡查询，非完整未来天气/守护时序。')
put('PoisonTarget BadPoisonTarget','A:180,185,190;AD:153,155','中央毒变化资格；评分先毒疗/治疗果/快雨治门，再15和HP整数15比率；己侧毒协同/无情，对侧收益能力/同步/治招/转移/间伤和治疗能力各按列表修正。','剧毒复制普通毒偏好，不另模拟毒计数；毒疗后段减25通常被前门遮住。')
put('PoisonTargetLowerTargetSpeed1','A:195;AD:154','毒和降速均不可才目标失败；从0算毒，非60加回，再速降1非whole。','毒组件无收益不删除降速；不按联合成功概率加权。')
put('ParalyzeTarget','A:180,186,190;AD:156','中央麻变化资格；评分果与快雨治门，基本10；粗速更快且严格小于2/4倍加15，混乱和迷恋各7；协同与收益/同步/治招/转移/治疗能力修正。','恰2倍当代不加15；两个7可以叠加；同步资格读真实反射资格。')
put('ParalyzeTargetIfNotTypeImmune','A:198;AD:157','独立以本次类型近似免疫拒绝，再变化中央麻门；目标分复制麻。','类型免疫与中央状态免疫分别检查。')
put('ParalyzeTargetAlwaysHitsInRainHitsTargetInSky','A:198;AD:158','只目标麻分复制；命中和空中效果由其它入口消费。','不能把本分复制当同名失败复制。')
for k,state in [('ParalyzeFlinchTarget','麻'),('BurnFlinchTarget','烧'),('FreezeFlinchTarget','冻')]:
 put(k,'A:196;AD:159,161,165',f'{state}与畏缩各从0算；两者均60才返回60，非60各加到原分。','普通伤害组件无用多返回0而非60；未按两概率联合期望处理。')
put('BurnTarget','A:180,187,190;AD:160','中央烧变化资格；果/快雨治门；基本15，有物理且非毅力加8、再无特殊加8；己侧协同及收益能力/耐热/同步/治招/转移/不间伤/治疗能力分别修正。','物攻两份8可叠加；有效毅力既阻物理奖励又参与减8，真实伤害另算。')
put('FreezeTarget','A:180,188,190;AD:162','中央冻变化资格；果/快雨治门；基本15、己侧协同、鳞片减8、自融招减15、治疗能力修正。','无概率抽样，冻不能施加伤害附效仍可伤害。')
put('FreezeTargetSuperEffectiveAgainstWater FreezeTargetAlwaysHitsInHail','A:198;AD:163-164','目标冻分复制；额外水相性/冰雹命中归通用类型命中消费者。','复制仅G，未补F/T。')
put('ParalyzeBurnOrFreezeTarget','A:197;AD:166','LUM或更快雨治保持，否则三种状态各从0算、非60各整数除3再加。','不按可成功组件重新归一；负整数商下界可与最终向0不同。')
put('GiveUserStatusToTarget','A:199;AD:167','U无真实异常整失败、T不能受当前异常目标失败；U不愿保留先加15，再按身份接对应状态评分，只有非60接受。','转移真实可治疗量不在评分写入；子评分60保留加15后分。')
put('CureUserBurnPoisonParalysis','A:200;AD:168','U非烧毒麻失败；愿保留给60，否则加20。','无异常却预测关闭时wants NONE真仍60，非所有治状态统一愿望方向。')
put('CureUserPartyStatus','A:200;AD:169','队伍无可战斗异常者整失败；效果重设100，再全部非空异常者各加12，睡计数1除外。','已倒下异常者可计分但单独不足使失败预测通过；已算目标分被重设。')
put('CureTargetBurn','A:201;AD:170','附效抑制保持；T真实烧时先减附效加值，再愿保留烧加15、不愿减10。','不真烧不改；这里刻意减附效，不当统一概率奖励。')
put('StartUserSideImmunityToInflictedStatus','A:202;AD:171','已有守护失败；薄雾持续且己全受地形60；敌无后备减20并返回，否则每己存活场上加15。','薄雾期限1不屏蔽；无后备分支不再每人加15。')
put('FlinchTarget FlinchTargetFailsIfUserNotAsleep','A:203;AD:172-173','T更快/正替身或有效精神力非模式破坏保持；附效未抑制加15，麻/混乱大于1/迷恋任一再8。','附效抑制不把伤害招变60；睡中限定通用整门另管。')
put('FlinchTargetFailsIfNotUserFirstTurn','A:203;AD:174','在场轮大于0整体失败，目标分复制普通畏缩。','命令时点0对1，不移真实执行时点门。')
put('FlinchTargetDoublePowerIfTargetInSky','A:203;AD:175;B:50;BD:36','目标分复制畏缩；中等基数另调本招真实基底，空中族/被天空摔投时翻倍。','P与G分责，翻倍不保证畏缩可施。')
put('ConfuseTarget ConfuseTargetAlwaysHitsInRainHitsTargetInSky','A:204;AD:176-177','中央混乱变化资格（变体仅分copy）；有效PERSIM前门保持，未排LUM；可混乱才附效和10、HP整数20比率、麻或迷恋8、蹒跚减15。','无PERSIM而LUM仍可计分；不把五大状态果门泛化。')
put('AttractTarget','A:205;AD:178','中央迷恋变化资格；可施才附效和15、麻或混乱8；红线可反施减15、变化招且U迷人之躯另减15。','两个负15独立可叠；不通过实际反施资格不减红线项。')
put('SetUserTypesBasedOnEnvironment','A:213;AD:184','环境类型按真实表及存在性回退，U不可改或无其它当前类型失败；有新类型伤害加14，每丢失旧类型有伤害减14。','只评攻击同属性，不比较防守。')
put('SetUserTypesToResistLastAttack','A:213;AD:185','U可改且T最近类型有效，存在非现有非伪且抵抗该类型的候选才不失败；当前已免疫60、弱/中/抗分别15/10/5。','不按可选候选类型逐个最佳化；最近记录不要求真实造成伤害。')
put('SetUserTypesToTargetTypes','A:213;AD:186','U不可改、T含额外当前类型空或双方基础和额外均相等目标失败；没有专设目标效果评分。','不可因目录有T就补G；类型数组比较保留顺序语义。')
put('SetUserTypesToUserMoveType','A:215;AD:187','整失败查当前代首槽/旧全槽可选不同非伪类型；所登记目标分仅找新类型伤害加14一次。','默认CONVERSION是User目标数0，不消费目标分；局部扩展仅在真的调用前提。')
for k,t in [('SetTargetTypesToPsychic','超能'),('SetTargetTypesToWater','水'),('AddGhostTypeToTarget','幽灵'),('AddGrassTypeToTarget','草')]:
 put(k,'A:217;AD:188-191',f'失败沿实际本招目标前门；遍历T所有存活对侧者所有伤害槽，不按PP过滤，原招本次类型对新{t}单类型弱点加10、免疫减10'+('、抗性减5。' if k.startswith('Add') else '。'),'不是新旧完整当前类型差值；同一成员多槽可多份。')
put('UserLosesFireType','A:215;AD:192','仅U当前无火预测整失败，没有专属失火类型评分。','含额外火也满足当前有火；不补防守收益。')
put('SetTargetAbilityToSimple SetTargetAbilityToInsomnia','A:233;AD:193-194','先身份存在再实际目标前门；T能力不活跃60；旧减新评级按每点5且最少差3调整，盟友反号。','差0不加最少15；有效性门与评级本身假设能力可有独立。')
put('SetUserAbilityToTargetAbility','A:235;AD:195','预测另排U不可失再实际目标前门；U能力不活跃60，旧评级高于新加5倍至少3差，反向减。','反直觉评级方向保留，8换2加30，2换8减30。')
put('SetTargetAbilityToUserAbility','A:233;AD:196','U需有能力、不同T、非不可得和继承者/接收者/复制，另真实目标门；T能力活跃才旧减新评级按阵营评分。','当代真实传递可能不拒同能力，AI额外失败保留。')
put('UserTargetSwapAbilities','A:235;AD:197','预测另排U无/不可失/不可得/神奇守护；两者皆无效60；各自新减旧，无效者差0，只有U差大于T差才按阵营加5倍至少3差。','后减分条件重复前比较，因此负向不可达，2与5不扣、5与2加15。')
put('NegateTargetAbility','A:237;AD:198','实际目标前门预测；T能力不活跃60；评级正加每点5且至少15、负减且至少15，盟友反号。','评级0保持；不可失名单属于实际门。')
put('NegateTargetAbilityIfTargetActed','A:237;AD:199','T正替身/不可失/能力无效或U更快保持，否则同抑制评级分。','不重建真实目标已行动；同速空间双方粗快可提前保持。')
put('StartUserAirborne','C:188;CD:44,46','铁球有效/扎根/击落/已有磁浮预计失败；已有飞行/有效漂浮/气球/意念移物60；每敌地伤且非抗加10，中等有地形减8。','地形减分不要求U当前接地；真实重力前门不在此重建。')
put('StartTargetAirborneAndAlwaysHitByMoves','C:189;CD:48,50','有效铁球或真实目标门失败；T已飞行/漂浮/气球60；T对侧每成员所有槽非0命中低于90加5、至多50另5，中等真实基数；地伤非抗每成员减7，中等地形加8。','直接枚举含PP0/OHKO；命中0两项皆排。')
put('HitsTargetInSkyGroundsTarget','C:190;CD:50','T替身保持；不浮空且T更快或不在飞翔弹跳保持；其它加10，每T敌有地伤加8，中等地形减8。','不把两回合天空摔投加入本专门条件；不是全部实际已行动判定。')
put('StartGravity','C:191;CD:44,46','已有重力整失败；逐存活者浮空收益按敌/己反号，地形中等修正；其对侧地伤逐人加减8；天空摔投己加8敌减8；数据命中低于85招己加8敌减8；U粗快且三天空两回合再敌加10己减10。','数据命中0包括在低命中偏好；所有组可累计且没有OHKO排除。')
put('TransformUserIntoTarget','C:192;CD:48,50','U变身或T变身/幻觉预测失败；目标分固定减5。','真实正替身未在这个专用预测门拒，通用替身门另看当前本招是否变化及可绕。')
# Capability-rating units: each declaration and each copy key was separately read.
for k,t in [('BLAZE','火'),('OVERGROW','草'),('SWARM','虫'),('TORRENT','水'),('STEELWORKER','钢')]: put(k,'A:223;AD:211',f'中等能力评级：有可用{t}伤害招保留基础值，否则0。','有限PP0不算；总PP0仍可参与；该查询不先核假设能力有效。')
put('CUTECHARM RIVALRY','A:224;AD:211,213','中等评级无性别变0，否则基础值。','RIVALRY同族copy沿CUTECHARM行为但保留自身不同基础评级。')
put('FRIENDGUARD HEALER SYMBOISIS TELEPATHY','A:225;AD:211,213','中等评级错传侧号作盟友索引，无枚举结果0，否则基础值。','高席自身可被算盟友；SYMBOISIS字面不等SYMBIOSIS，基础FRIENDGUARD本来0不会因此变正。')
put('GALEWINGS','A:226;AD:211','中等有原飞行类型可用招保留，否则0。','变化飞行招也满足，不要求伤害。')
put('HUGEPOWER PUREPOWER','A:226;AD:211,213','中等以固定变化问攻击升值得，真保留基础，假0。','防代攻/借目标攻击不使攻击值得；接力棒/辅助力量提前值得仍可保留。')
for k,what in [('IRONFIST','拳'),('LIQUIDVOICE','声音'),('MEGALAUNCHER','波动'),('PRANKSTER','变化'),('RECKLESS','反伤'),('ROCKHEAD','反伤但排坠落'),('SKILLLINK','2至5击族'),('TRIAGE','治疗')]: put(k,'A:227-228;AD:211',f'中等有可用{what}招保留基础，否则0。','仅能力评级适用资格，不证明真实每招必获能力收益。')
put('PUNKROCK','A:229;AD:211','中等无可用伤害声音招变1，有则保留基础。','有声音变化招仍为1。')
put('SANDFORCE','A:229;AD:211','中等无可用地岩钢伤害招变2，有则保留基础。','不要求当前沙暴。')
put('RUNAWAY','A:229;AD:211','中等野生变0，其余保留基础。','默认基础RUNAWAY也是0；不假定登记使其非零。')

inventory=list(csv.DictReader((R/'inventory-registrations.csv').open()))
missing=sorted(set(r['key'] for r in inventory)-facts.keys())
assert not missing,missing
consumers={
 'MoveFailureCheck':('005_AI/005_AI_ChooseMove.rb:38-43,177-191','PredictMoveFailure；整招失败20；可被先行合法性屏蔽'),
 'MoveFailureAgainstTargetCheck':('005_AI/005_AI_ChooseMove.rb:196-225,294-299','PredictMoveFailure；实际枚举目标；失败-1排除'),
 'MoveEffectScore':('005_AI/005_AI_ChooseMove.rb:232-285','ScoreMoves；目标合成之后整体效应和通用整体修正'),
 'MoveEffectAgainstTargetScore':('005_AI/005_AI_ChooseMove.rb:294-323','ScoreMoves且实际目标入口；后通用目标修正与盟友反转'),
 'MoveBasePower':('005_AI/011_AIMove.rb:81-92；001_Battle_AI.rb:115-118','中等才使用基数登记；固定伤害与普通粗伤不同消费者'),
 'AbilityRanking':('005_AI/010_AIBattler.rb:407-420；001_Battle_AI.rb:154-156','中等才修正评级；操作处理器另做能力有效性门')}
out=[]
for n,r in enumerate(inventory,1):
 f=facts[r['key']];c,g=consumers[r['family']]
 special='DEFAULT_USER_TARGET_NOT_CONSUMED' if r['key']=='SetUserTypesToUserMoveType' and r['family']=='MoveEffectAgainstTargetScore' else ('COPY_BINDING_AND_ACTUAL_PARAMETERS_REVIEWED' if r['operation']=='copy' else 'BRANCH_CONDITIONS_REVIEWED')
 loc=[]
 for prefix,line in [x.split(':') for x in f['formal'].split(';')]:loc.append(str(D/names[prefix])+':'+line)
 # This lookup is only a second locator, never the semantic conclusion.
 for pkg in ['AD','BD','CD']:
  for line,s in enumerate((D/names[pkg]).read_text().splitlines(),1):
   if re.search(r'(?<![A-Za-z0-9_])'+re.escape(r['key'])+r'(?![A-Za-z0-9_])',s):loc.append(str(D/names[pkg])+':'+str(line))
 out.append({**r,'fact_id':'EA-'+str(n).zfill(3),'behavioral_fact':f['fact'],'consumer':c,'gates':g,'formal_clause':' | '.join(dict.fromkeys(loc)),'boundary_or_countercheck':f['ordinary_boundary_or_countercheck'],'semantic_disposition':special,'evidence':'SOURCE_STATIC+MANUAL_DERIVATION;NO_REFERENCE_EXECUTION'})
with (R/'forward-matrix.csv').open('w') as h:
 w=csv.DictWriter(h,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
(R/'semantic-facts.json').write_text(json.dumps(facts,ensure_ascii=False,indent=2))
print(json.dumps({'forward_rows':len(out),'facts_by_identity':len(facts),'missing_semantic_identity':missing},ensure_ascii=False))
