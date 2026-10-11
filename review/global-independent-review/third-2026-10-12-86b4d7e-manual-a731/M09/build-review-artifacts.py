"""Serialize this independent review's manual judgments; no reference execution."""
import csv,json,hashlib,subprocess,re
from pathlib import Path
ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=ROOT/'review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/M09'
REF=ROOT/'reference/pokemon-essentials'
RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';SC='167296dbe9e2384627b0ed696e87aeb01f211252';DC='86b4d7e1d8645e75af91a215240f8786a5bb4ca8'
AI='Data/Scripts/011_Battle/005_AI/'
EF='Data/Scripts/011_Battle/006_AI MoveEffects/'
BT='Data/Scripts/011_Battle/008_Other battle types/'
CF='Data/Scripts/018_Alternate battle modes/001_Battle Frontier/'
CR='Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/'
FILES=json.loads((OUT/'assigned-files.json').read_text());SPECS=json.loads((OUT/'assigned-specs.json').read_text())
SRC={str(i+1):x['path'] for i,x in enumerate(FILES)}
SPEC={}
for x in SPECS:
 n=Path(x['path']).name
 for code in ['51','52-a','52-b','52-c','54','55','56','58','57']:
  if n.startswith('wp'+code+'-'):
   k=code+('-data' if any(t in n for t in ['defaults','coverage','cup-data']) else '')
   SPEC[k]=x['path']
SPEC['t-fac']='deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md'
SPEC['t-ai']='deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md'
SPEC['t-fc']='deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md'

def sha(v):return hashlib.sha256(v).hexdigest()
def gitblob(p,ref=True):
 try:return subprocess.check_output(['git','-C',str(REF if ref else ROOT),'rev-parse',f'{RC if ref else SC}:{p}'],text=True,stderr=subprocess.DEVNULL).strip()
 except subprocess.CalledProcessError:return ''
def srcs(codes):return '|'.join(SRC[c] for c in codes.split(','))
def write_tsv(name,fields,rows):
 with (OUT/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
CAP=[]
def cap(key,name,codes,loci,doc,clauses,test,boundary,status='SUPPORTED_STATIC',limits='运行=0；未声称最优AI、宿主或全组合动态通过。',category='Combat Requirements / Pokémon Rules'):
 CAP.append(dict(capability_id='M09-'+key,module='M09',category=category,capability=name,source_paths=srcs(codes),source_loci=loci,spec_paths='|'.join(SPEC[d] for d in doc.split(',')),spec_clauses=clauses,test_design=test,normal_failure_boundary=boundary,status=status,limitations=limits))
# Source-derived behavior families; these descriptions are the reviewer's judgment.
cap('01','按席位属主取AI档与资源；玩家/伙伴/野生和中途补位入口','1,9','001:14–45,75–78;009:29–96','51','§1–2','AI-A01/A03；受控玩家与伙伴对照','已选择或强制动作跳过；中途只请求替补，不能借敌方资源。')
cap('02','技能缺省、数值阈值及初始传奇野生档','9','29–96','51','§2','AI-A01/A02；31/32/47/48/99/100边界','无本地255硬上限；传奇档由初始野生成员设定，不按每次换入重设。')
cap('03','作者标记追加、反标删除与阈值独立','9','55–82','51','§2','AI-A02','Anti移除对应标记，不抹除高/最佳技能判定；重复不去重。')
cap('04','基础决策阶段与异常后的继续、Mega登记','1,4','001:48–69;004:7–14','51','§2/4/5','AI-I03/I06/I07/M07','换出→道具→模式自动→Mega→候选；正常报告后可继续，已写状态无统一回滚。')
cap('05','普通换出资格、顺序意愿及中档否决','2','8–58,177–705','51,51-data','§3.1；附表§4','AI-S01/S05/S06','野生、不能换出、高档对手全不能动先拒；强迫差招跳意愿/否决而不跳外层门。')
cap('06','灭亡/残余/治状态/祈愿/瞌睡/睡眠意愿','2','177–418','51','§3.1表前六族','AI-S01/S07/S08/S09','逐族概率、危害与束缚门保持；祈愿比较使用缺HP减危害方向。')
cap('07','无用/全部吸收/吸收来袭/骤死/高伤害意愿','2','424–596','51','§3.1表后五族','AI-S05/S06；吸收一对成功与全吸收反向','替身字段0仍真；后备可伤是存在一组；30%/25%/50%门按族，不保证最终换人。')
cap('08','四种普通换人否决','2','608–705','51','§3.1否决表','AI-S01/S04；致命危害/正阶和/神奇守护对照','骤死特例分层，正阶总和不由负阶抵消；已有克制招只核局部PP。')
cap('09','替补过滤、保留王牌、顺序选择与评分平手','2','60–153','51','§3.2','AI-S02/S03/S04','普通排同侧重复后备、王牌；强迫保留仅候选；高普通最高<100拒，平手无另随机。')
cap('10','危害、浮空、中毒和吸收的持久后备近似','2,8','002:107–171;008:43–95','51','§3.2','AI-S06；靴/铁球/重力/薄雾对照','基础相性与有效性近似不等真实入场；TELEPATHY此假设不吸收。')
cap('11','每项最低量、符号和资格的残余近似','10','57–183','51,52-a','§3.3；A§4.1','AI-S07/S08/S09；AE-G13','各项先整数/至少1后合成；Wish保存量、Perish999999例外；不夹真实HP、不模拟连锁。')
cap('12','完整业主主动道具资格扫描与分类','3','100–132,178–254','51,51-data','§4；附表§1–3','AI-I01/I02/I06/I07/I08','分类前完整扫描；nil招索引/AI上下文可使整阶段退出，已收候选不登记/消费。')
cap('13','治疗状态意愿方向、HP75%量门、X/全阶/复活排序','3','111–174,186–254','51','§4','AI-I01–I08','SITRUS估1；全阶取错组；X偏更高阶；复活同档取后索引；执行量属于真实道具合同。')
cap('14','招式候选资格、替代评估招及共享字段','5','23–87,142–171','51','§5','AI-M04/M05/M09；CE-C21/C25','最终仍原槽；整失败保留20；准备写类型/忽略能力，完成清标记而不宣称全副作用回滚。')
cap('15','零/单/多目标候选与重定向近似','5','45–127','51','§5','AI-M08；逐单目标条目数对照','单可敌目标过滤友方；预计吸到盟友可无候选；多目标合成一条，不能当真实重定向。')
cap('16','野生稳定槽重复与分数权重抽取','5','129–137,330–392','51','§5','AI-M01–M07','阈值为技能平方根，最高分乘阈值取底；空候选自动、零权重没有明确新选择兜底。')
cap('17','整招/目标失败、平均和友军反转评分阶段','5','177–324','52-a','§2.1','AE-A01–A05','目标负排除，60友方排除；185反转、有效目标平均+多目标奖；整体修正后截断>=0。')
cap('18','22通用评分修正按组登记顺序合成','7','4–517','52-a,52-a-data','§2.2；附表§3.1','AE-A05–A10','单项60不封全链；命中罚/伤害/KO/触发加分/同命/忍耐各门独立。')
cap('19','粗类型、优先、速度及相性近似','10,11','010:187–258,567–594;011:11–73','52-a','§3.1/3.2','AE-N01/N07；同速空间反向','高才真实速度；同速空间可双方更快；地飞铁球早返和额外类型/沥青保留。')
cap('20','粗会心表、负下标与强制/禁止预测','11','104–121,500–541','52-a','§3.1','AE-N02/N02b/N02c/N02d；BE-B12b','禁会心级-1粗伤仍取末项；旧五档末2/新四档末1；目标会心物品误传使用者物。')
cap('21','粗伤倍率、槽次取整、固定量与不致死','11','81–375','52-a','§3.2','AE-N03/N04/N05/N09–N11','不加随机；目标树果跳过；存活同侧墙人数25/19；亲子爱无条件近似乘P，不逐击模拟。')
cap('22','粗命中与附效评分的0/负值/抑制','11','379–562','52-a','§3.3','AE-N06/N07/N08','命中不封100；两VictoryStar得96；附效-999是消费者哨兵，非最终分。')
cap('23','阶级资格、方向、唱反调、单纯及残余/天然门','6','11–153,310–441','52-a','§4.1','AE-G01–G04/G13','固定变化绕中央但仍核有用和限幅；正请求才保留；伤害附效whole假。')
cap('24','階级增量相对倍率、HP负整除和错位命中','6','158–299,446–569','52-a','§4.2','AE-G05/G06/G07','早期5n、HP整除向负无穷；攻击8/12、防10、速度局部反向/命中错位不修成真实规则。')
cap('25','普通自身升/降及目标单降参数族','13','4–48,73–290,324–456,527–618,737–968,1026–1063','52-a,52-a-data','§4.1–4.3；附表§2.2','AE-G01/G05；各能力项1/2/3、复合顺序对照','读取当时实际招式请求；对普通标量/复合逐项夹±6，不能由效果名重造参数。')
cap('26','腹鼓/充电/变圆/变小/成长/破壳/背水特殊升阶','13','53–68,81–92,145–155,192–214,267–319,358–395,457–522','52-a','§4.3','AE-G11；唱反调和HP边界','各前门/附加门分层；破壳升无用60后不降；低HP罚并非真实扣血。')
cap('27','混乱复合、点穴、指导、正负电和草群升','13','623–732,1081–1198','52-a','§4.3','AE-G10；虚张/点穴/草接地对照','UserSide正负电整体遍历不再次过滤能力；点穴不逐随机项目期望。')
cap('28','诱惑、沥青、毒多降和动态基底','13','784–792,829–917,1068–1076','52-a','§4.3','AE-G12；重力81→121/草场61→31','毒需真毒；沥青未标不因降速无用全败；中央资格不等镜甲真实复合前门。')
cap('29','交换/复制/偷取/颠倒/清除阶级与白雾','13','1203–1439','52-a','§4.3','AE-G08/G09；正负差对照','负请求仍负被丢，不改绝对值；复制无正差先60；白雾按指定可用降阶族。')
cap('30','基础能力值互换/均分的比值偏好','13','1444–1583','52-a','§4.3','AE-G08；有用/无用对照','偏好算比值改善，不先实际均分；相等60，空间剩1与>1区分。')
cap('31','睡/毒/麻/烧/冻协同与治疗排除','14','4–456','52-a','§5','AE-S01–S06','状态可施资格与偏好前门分开；无效附效保持；主状态果/雨湿润/协同以存活场上为集合。')
cap('32','瞌睡/暗黑洞/精神转移/自治/全队治疗','14','58–87,461–571','52-a','§5','AE-S02/S09/S11','瞌睡起用预测做普通睡眠资格，非到期查询；全队评分重置100并可计倒下异常者。')
cap('33','畏缩、混乱、迷恋及状态保留意愿','14,10','003:576–685;010:368–396','52-a','§5','AE-S07/S08/S10','PERSIM前门未排LUM；迷恋红线/可施门；NONE愿保留，主动道具布尔方向另述。')
cap('34','改类型与不消费的User纹理评分','14','690–935','52-a','§6','AE-T01/T02','只看进攻/新单型相性；普通User0不消费纹理目标分，不补防守最优预测。')
cap('35','能力基础完整评级与25绑定的局部门','8,10','008:101–159,235–381;010:407–421','52-a,52-a-data','§6；附表§3.2/4','AE-T06/T07','拼写字面保持；中档才修正；侧号当盟友索引可能含自身。')
cap('36','能力给予/复制/传递/交换/抑制的方向','14','941–1105','52-a','§6','AE-T03/T04/T05','扮演反向、交换负向分支不可达；资格沿真实前门，评级不保证能力当前有效。')
cap('37','无收益/首回合/珍藏/打嗝/共同类型前门','12','9–97','52-a','§7','AE-F01/F02','没有注册失败不补；局部60不取消真实金钱/动作。')
# B numerical/field/healing families.
for key,name,loci,clauses,test,boundary in [
('38','固定量、等级随机代表、HP差与不致死','004:4–58,531–535','§2.1','BE-B01/B02','固定基底直接绕普通倍率；代表等级值不是随机范围。'),
('39','OHKO等级/坚硬/冰目标预测与命中','004:63–110;011:392–395','§2.1/2.2','BE-B02/B02b','AI冰目标拒与加载后的真实目标资格分开，基底当前HP。'),
('40','自身/目标HP、友好、正阶和及速度威力','004:131–183','§2.1','BE-B03；比例端点','明确分段整数和真实速度查询；不是按包装粗速。'),
('41','预期剩余PP、重量比和计数威力','004:188–246','§2.1/2.2','BE-B04/B04b/B04c/B05/B06','PP0缺总PP别名查询先败；连续切割基底自身计数、最终整体分读回声。'),
('42','震级、视为状态、无物及半无敌条件威力','004:251–377','§2.1','BE-B07/B08/B09','71代表值，地下/草场折入P；杂技有效飞行宝石近似并非真实消费链。'),
('43','相性折P、IV、树果、天气/地形基底','004:1292–1301,1414–1477','§2.1','BE-B55；自然之恩有果/空果/前缀对照','完整数据值和资格前缀不同；NaturalGift预测不模拟首击后自耗/续击。'),
('44','本轮失HP/目标已动、溅射、会心控制偏好','004:115–126,382–526','§2.2','BE-B10/B12/B12b/B58/B61','仅登记的阶段生效；保护会心禁负级而不套粗伤负下标。')]:
 cap(key,name,'15,11',loci,'52-b',''+clauses,test,boundary)
cap('45','多击合并基底和破替身近似','16','4–185','52-b','§3','BE-B13–B16','总基底一次骨架，2–5用3.1基底/3次数；并非真实逐击/耐受连锁。')
cap('46','休息、两回合、香草、日光和半无敌偏好','16','190–479','52-b','§3','BE-B17–B20','香草跳普通罚；目标保护集罚一次；不同技能/附效和目标族独立。')
cap('47','Geomancy User0不消费目标升阶/两回合分','16,5','005:45–56,273–282;MultiHit:322–334','52-b','§3','BE-B62','四HP/香草组合100；全三项封顶整体20，部分封顶100，不移动评分族。')
cap('48','滚动连续攻击、忍耐代表和HP罚','16','494–531','52-b','§3','BE-B21','代表P与真实记录分开；睡>2/真冻过滤、四分之一60与叠加HP罚。')
cap('49','自疗/睡觉/天气恢复/羽栖/净化','17','4–122','52-b','§4','BE-B22/B23','真实可治先门；HP比例罚/补与异常保留方向分开，羽栖不另评防守。')
cap('50','吸取力量/半伤/食梦/四分之三吸取','17','127–226','52-b','§4','BE-B24/B25','污泥仅粗伤<当前HP时罚；估治不先夹目标HP，根和缺HP夹限顺序保持。')
cap('51','群治/附治状态/治友/祈愿/环根/种子噩梦','17','231–429','52-b','§4','BE-B26/B27/B51–B54','附治状态误调评分族而无HP奖；友治敌60，祈愿为位置。')
cap('52','痛楚平分实际平均与AI浮比交界','13','1588–1595','52-b','§4','BE-B28/B63','实际U51/60,T150/200得60/100；AI100.5/51，HealBlock非拒、替身前门拒。')
cap('53','扣半、自灭/牺牲、薄雾/搏命、同命怨念','12,17','Misc:614–645;Healing:434–683','52-b','§4','BE-B30/B31/B32/B33','后备与HP门逐族；全场扣半零和可除零；实际失败/提交不由偏好保证。')
cap('54','随机伤治、反击、蓄力喷出吞下及誓约','19','42–75,187–190,214–452','52-b','§2.1/2.2/4/6.2','BE-B10/B11/B29/B55/B56/B57','反击代表60不读真实记录；吞下半血早返跳蓄力罚；协同未证明实际选择。')
cap('55','建天气/地形、减旧收益和组内任一匹配','12,6','Misc:169–353,650–666;Generic:573–796','52-b,52-b-data','§5.1；附表§3','BE-B34–B38','全局天气抑制、伞门与阵营方向保留；种子首轮外不限接地。')
cap('56','四危害、替身、未来攻击及全除墙','12','358–461,511–532,560–571,671–708','52-b','§5.2','BE-B39；HP/已有记录门','对侧整队后备而非仅属主；未来招存位置，替身HP成本并非已提交。')
cap('57','除雾/除墙/顺风/奇妙空间','13,15','Stats:970–1021,1600–1672;Attributes:728–746','52-b','§5.2','BE-B40/B41/B42','危害清理资格与分数分开；严格跨侧速度对、空间不按已开反转。')
cap('58','玩水玩泥和三墙建立偏好','15','569–723','52-b','§6','BE-B59；旧/新代、HP和黏土对照','无对应伤害敵为60；墙建立与粗伤减伤人数是两层。')
cap('59','保护五族、掀榻、戏法/快速/广域及挺住','15','540–564,751–1170','52-b','§6.1','BE-B43–B46','各资格与残余/连续罚保持；旧广域误用本招伤害属性；挺住无>=4先门。')
cap('60','反伤、坠落、解除保护和Hoopa','12,15','Misc:157–164;Attributes:1175–1287','52-b','§6.2','BE-B47/B48/B49','缺源复制不覆盖+7；坠落不封命中100；反伤致死60保留同后备关系。')
cap('61','锁定、识破/奇迹、输电/等离子浴','15','1332–1399,1482–1559','52-b','§6.2','BE-B50/B60','原槽直接枚举不排PP；电化比较主体和优先方向不改成实际行动模拟。')
# C item/calling/control families.
cap('62','完整物品基础评级、条件优先和价值后置','8,10','008:163–228,387–898;010:432–465','52-c,52-c-data','§2.1；附表§2–4','CE-C01–C07/C55/C58','215身份15档；中等才评级修正，投掷/杂技后置不限中等；直接键遮条件组。')
cap('63','强制消费效用与负值保留/熟成','10','470–560','52-c','§2.2','CE-C08–C12','ASPEAR拼写不匹配ASPEARBERRY；Leppa不核PP；估量不改真实低HP触发。')
cap('64','偷取、递送、交换、回收及拍落/焚烧/腐蚀','18','4–186','52-c','§3','CE-C13/C14/C15/C17/C54','±4差值、实际物品有效门逐人；野生/不可移/替身/黏着分门，腐蚀方向与拍落相反。')
cap('65','魔法空间、强制吃果、虫咬与投掷','18','191–376','52-c','§3','CE-C16/C18–C20/C53','剩1空返回保留；对敌消费先夹负；Fling参数查首完整标记/至少10，真实失败另属M08。')
cap('66','仿效/鹦鹉/抢先/借助/梦话及模仿写生','19,5','Effect:460–628;Choose:142–171','52-c','§4','CE-C21–C24','准备可替代评估对象；借助未排倒下PP；写生整体copy失源不造目标算法。')
cap('67','外衣/抢夺/重定向/帮助/火药','19','4–32,196–209,240–250,551–589','52-c','§4','CE-C26/C27/C56','仅已知招和当前可动集合；帮助目标+5无整体登记，不重建真实已行动门。')
cap('68','诅咒分型与秘密之力附效映射','19','80–182','52-c','§4','CE-C25/C28','幽灵HP罚有HPAware门；降阶代码错存效果符号未调用降阶helper，不补理想收益。')
cap('69','自换/撤退射击/接力/变化和伤害拖出','20','4–233','52-c','§5.1','CE-C29–C32','变化王牌60与伤害-20不同；撤退跨族copy失源；破替身预测不替代执行时点。')
cap('70','持续束缚、困住、Octolock/互锁/妖精锁','20','238–416','52-c','§5.2','CE-C33/C34','可新拘束近似与真实可换分开；全无后备/残余可倒下分whole；Octolock清除门不限中等。')
cap('71','真气拳/突袭/甲壳陷阱/鸟嘴/轮唱','12,20','Misc:102–164,597–609;Switching:426–470','52-c','§5.2','CE-C35/C36','快慢/可动/接触烧资格逐族；轮唱己侧包括自己，不推出有同伴。')
cap('72','您先请/延后/号令与戏法空间','20','475–608','52-c','§5.3','CE-C37–C40/C52','粗速排序非真实优先序；号令首槽与真实末槽不同；高粗速仍再乘顺风。')
cap('73','最近招PP损失、定身/折磨/安可/挑衅','20','618–810','52-c','§5.3','CE-C41–C44','减PP4较慢/7..10仍-10；锁字段空的挑衅无用方向不倒置；预测关可能空访问。')
cap('74','治疗/声音/封印限制','20','815–877','52-c','§5.3','CE-C45/C46/C57','声音>1保持；封印默认User0不消费目标+8；查共享只首敌。')
cap('75','磁浮/意念移物/击落/重力/变身','14','1115–1282','52-c','§6','CE-C47/C48/C51','重力含命中0可用招；变身预测只变身幻觉标记，不补实际替身拒绝。')
cap('76','侧效果交换和盟友位置互换','12','466–506,576–592','52-c,52-c-data','§6；附表§5','CE-C49/C50','bool true非数1；好组含火海湿地；错传侧号但邻近排自身，不可自交换。')
cap('77','最终有效绑定、无源copy及共同缺省','1,15,19,20','Handlers:97–161;Attributes:215–246,1175–1191;Change:625–628;Switch:104–110','52-a-data,52-b-data,52-c-data','各附表注册语义和重复定点','CE-C22/C30/C55/C59；BE-B05/B47','同族末写、copy取当时存在源；缺源不创建/不覆盖；不同内部表示等价但跨族别名/重复相加不等价。')
# Facilities and record families.
cap('78','数量范围、规则合取、子集误入整队及复制','30,31','Challenge:9–117;Rulesets:5–125','54,54-data','§2.1/5；附表§1–2','QC-Q01/Q02/Q07/Q08/Q19','初始化最少1、设人数恰n；原子集公开入口实入整队；复制最少重置，不要求未来容器组织。',category='Creature-RPG / Combat Requirements')
cap('79','五种资格入口、组合枚举与首错误','31','127–223','54','§2.2','QC-Q03–Q06/Q16/Q31','可注册枚举输入最大长度；可选有效组枚举原列表最少数；文案缺失与假分别记。',category='Creature-RPG / User Interface')
cap('80','报名UI及nil/空列表/非空提交','25,31','Data:38–49;Rulesets:127–223','54,55','§2.3；会话§2.3','QC-Q31；WS-W28/W29/W35','界面先有效组，再顺序选/最终校验；nil不写且返nil，[]提交且返false；普通UI空确认未证。',category='User Interface / Creature-RPG')
cap('81','成员/队伍资格与缓存、昵称异常','32','4–392','54,54-data','§3；附表§3/4.2','QC-Q10–Q18','标准普通能力表提前允许、不自动拒倒下；Baby物种缓存；昵称缺方法；负扩展缺真全拒。',category='Creature-RPG / Pokémon Rules')
cap('82','十活动杯工厂、五直接样本和会话模式','24,30,31','Session:46–77;Challenge:123–256;Rulesets:229–323','54,54-data,55','§5；附表§1–2；会话§2.1','QC-Q19/Q20/Q24/Q42','同名样本不等工厂；Factory无标准限制；双战与3人不矛盾；注释赛事非默认。')
cap('83','等级策略、完整经验、同级跳写和HP差','30,33','Challenge:61–81;Level:4–229','54','§4.1','QC-Q21–Q29','固定/上限/开放/总额/组合各门；先保存两侧EXP，非法值部分写无事务；无统一HP/PP快照。')
cap('84','单场治疗/经验物品快照和位置还原','27,33','Battles:40–97;Level:28–79','54,55','§4.2；会话§3/4','QC-Q30/Q45/Q46；WS-W21/W22/W26','EXP先、调整返后物品；正常经验→治疗→解除变身→物品；当前索引错配、缺EXP跳/缺物写空；异常不保证善后。')
cap('85','条款键、11设置与3仅消费者','21,34','Clauses:11–306;Rules:10–103','54,54-data','§6；附表§5','QC-Q32–Q40/Q47','精确clause后缀；设置不筛报名招；sleep/freeze/skillswap/OHKO各消费阶段保留。')
cap('86','冰OHKO加载后真实门与AI独立拒冰','21,15','Clauses:192–238;AIAttributes:63–110','54,52-b','§6.1；B§2.1','QC-Q41；BE-B02b','同级非冰U/冰T无坚硬，条款假目标过、阈20；r19/r20分；AI仍拒；通过不等必倒。')
cap('87','平局/自灭/灭亡歌/骤死的裁判来源','21','11–52,248–306','54','§6','QC-Q36–Q39/Q43/Q44','selfKO用最后使用者；draw用检查点使用者/保存歌源；返假不取消动作；正结果门分层。')
cap('88','挑战注册、惰性类型及规则读数边界','24','4–176,324–363','55','§2.1/2.2','WS-W25/W32','已有规则不重算；配置读取字段未写，活动字符串与0比較不能到副本；最大/上次/当前计数分开。',category='Creature-RPG / Generic Kernel')
cap('89','开始、计数、名单去重和结束条件','24','181–257,284–304','55','§2.2','WS-W09/W18/W19/W20/W26/W27','<=0部分进行中写；单场不写决定不加胜；distinct不足循环无上限。',category='Creature-RPG')
cap('90','原队伍引用、活动提交、取消和结束','24,25','Session:200–229,270–282;Data:38–49','55','§2.3','WS-W10–W16/W28–W30/W35','原队伍只开始按引用存；取消有快照恢复；结束无条件恢复后判活动，未开始可置空。',category='Creature-RPG / Generic Kernel')
cap('91','暂停继续、保存返回与地图转移','24','231–241,258–282,306–318','55','§2.4/4','WS-W17/W23/W33/W34','决定0开始暂停继续仍保存；临时开始点存后恢复；未捕获异常跳恢复；结束非0保存。',category='Engine / Overworld Integration / Generic Kernel')
cap('92','训练家指数区间/IV阶梯与队伍生成','26','6–83','55','§2.5','WS-W01–W08/W19/W20/W31','区间按长度缩放；rand0非整值；短列表直接不补校验，长有放回合法重试无上限。')
cap('93','名单加载机制、编译字段和个体创建','25','21–33,101–219','55','§2.5/6','显式名单优先/默认/缺编译物反向；文本样本','训练家及模板分别首匹配；EV均分/RETURN转FRUSTRATION/亲密0/随机ID；实际编译产物缺失。','PARTIAL','脚本机制SUPPORTED_STATIC；全PBS内容语义和实际启用未证。',category='Demo / Developer Experience / Creature-RPG')
cap('94','设施图形、台词与事件接点','25','55–95','55','§2.7','WS-W23/W24','图形异常回NPC01；非活动开场省略；真实接待/费用/BP奖励事件缺材料。','PARTIAL','UI机制静态支持；Graphics/地图事件/宿主不可得。',category='User Interface / Engine / Overworld Integration')
cap('95','Factory分组域/IV阈值、临时人数及失败','26','88–164','57','§2.1–2.3/5','FC-01–FC-08/FC-13/FC-14/FC-16/FC-17','上下端含；上端可N取空；整体新+旧校验；中途失败人数不恢复，无重试上限。')
cap('96','Factory候选默认拥有者和引用交换','24,25','Session:373–423;Data:201–217','57,55','§2.4/2.5/4/5；会话§2.5','FC-10/FC-12/FC-15','空训练家构造有效默认记录0/空名/2/2，分给NPC/交换不改；不写永久获得。',category='Creature-RPG / Pokémon Rules')
cap('97','初租三选确认与交换两屏取消提交','28,24','UI:168–246;Session:388–423','57','§3–4','FC-09–FC-11','初租不能退出，第三拒撤；交换成功计数、取消不计但仍提交；活动P不同于R可见替换。',category='User Interface / Creature-RPG')
cap('98','Palace类别优先与两张完整性格表','22','6–76,105–140','56','§2.1/2.2','PA-P01–P06','50行概率数据，生效第二门2A+D；辅助可被吞；防御先于变化判定。')
cap('99','Palace部分资格、-2无力和玩家/AI入口','22','78–140','56,58','§2.4；记录§4/5.3','PA-P07/P27；RC-W07','玩家安可/无常规可用先自动；AI先模式选；PP>0，锁只CHOICEBAND、折磨；-2执行提前失败。')
cap('100','Palace压半生命周期、提示与换人概率','22','142–164,175–244','56','§2.3/2.5','PA-P08–P12/P23–P25','真睡/倒下排；同在场回血不清、换入清；概率最高候选早返跳刚换标记，强迫参数未读。')
cap('101','Arena心分/成功槽覆盖/体分','23','4–36,96–125,127–176','56','§3.1','PA-P13–P19/P26','技为最后赋值槽、攻击阶段全清，整体失败未结算不补；体用首发HP不封100。')
cap('102','Arena连续裁判、直接倒下和顺序补位','23','42–94,127–200,213–216','56,58','§3.2/3.3；回放§5.3','PA-P16/P20/P21/P28；RC-W25','首发复位；正常补位不清累积/计数/基线/提示；>=3每轮判，HP写穿；无询问记录。')
cap('103','Arena裁判分项显示与总结呈现','23','222–365','56','§3.2','PA-P17/P18；分项顺序审读','心→技→体逐显与2/0或1/1评分，窗口释放为宿主呈现边界。','PARTIAL','文字/顺序静态支持；实际图形/逐帧UI未运行。',category='User Interface')
cap('104','记录模式和临时→全局生命周期','27,24','Battles:13–34,84–143;Session:95–103','58','§1/2/6.1','RC-W03/W04/W13/W14/W15','决定1/2/5导出、其它清；事件提升且清临时；空无操作、未知型后启动败。',category='Generic Kernel / Combat Requirements')
cap('105','记录18初始属性、复制边界和缺布局','24','28–71,147–179','58','§3/6.2','RC-W01/W02/W18/W20','队伍字节副本而非全状态；布局/Mega/ally物未存，默认1v1使非空高席某分支败。')
cap('106','每轮命令覆盖、失败保留和取消残留','24','80–125,198–222','58','§4/6.3','RC-W05–W10/W19','成功登记覆盖；自动-1整体丢目标；取消不清记录；换位/呼叫无钩子会留旧槽。')
cap('107','记录随机域与AI/命令评估随机分离','24,8','Recorded:129–132,188–192;Utilities:5','58','§5.1','RC-W11/W12/W17','执行战斗随机序列取值；AI/Palace/global不录；没有种子/跨实现等价保证。')
cap('108','询问式/随机式替补及首命令前入场消费者','24','74–78,182–186','58','§5.2','RC-W16/W24/W25/W26','攻击后/回合末/入场询问共享流、负值亦记；Roar/RedCard只随机；EjectPack先耗负选不替换。')
cap('109','回放固定四席、序列不足、实时背包','24','147–223','58','§5.4/6.2/6.3','RC-W12/W20/W21/W23','缺轮次先下标/长度败，随机/替补越界取空再递增；玩家消耗物直扣实时背包。')
cap('110','回放正常终局、BURMY标记和中止','24,27','Recorded:194–196,250–256;Battles:111–128','58','§6.4/6.5','RC-W22/W22b/W23','副本形态仍写图鉴；位0首发真/位1换入按队伍索引假；中止0不正常终局；无设施善后。')
cap('111','录像未保存场域/默认天气与准备顺序','24,27','Recorded:47–67,164–179;Battles:50–67','58,54','§3/6；WP54§4.2','旧非必修B030三组仅静态复核','联合默认场域/准备/字段完整合同可推出Misty0对2和晴到期Rain对None；不自动重开或要求新字段。')
cap('112','模拟工具真实战斗分支的AI/规则/恢复消费者','1,30,27','AI:48–78;Challenge:111–117;Battles:40–97','51,54,55,58','跨WP76交界','普通设施/模拟1%分支成对静态读','模拟开controlPlayer、非内部、仅正常治/物品恢复，不直接继承设施完整经验/解除/录像持久链。','PARTIAL','模拟主体完整裁决属M12；这里只核AI/规则/记录消费者接口。',category='Demo / Developer Experience / Combat Requirements')
# Evidence-level material controls, deliberately outside semantic source family completion.
cap('113','全设施PBS名单可得文件、样本与消费关系','25','21–33,113–138','55,57','数据输入与名单选择','每对训练家首/末节、模板首2/末1样本；Fancy未引用反向','机制/静态样本支持不等全内容语义或编译启用；非singleFancy两个文件仅存在。','PARTIAL','5引用名单对+1未引用Fancy对；普通训练家2文件样本；全内容/合法性未全面验证。',category='Demo / Developer Experience')
cap('114','设施编译物、真实录像、地图事件、媒体与宿主','27,25','Battles:111–143;Data:21–33,77–88','55,56,57,58','未决与U01/U05','存在性只读检查；不执行/反序列化','trainer_lists.dat、Battles/*.dat、地图事件/Audio/Graphics不可得；场景及加载动态不能判PASS。','MISSING_MATERIAL','具名验收：提供匹配基线编译物/录像/事件/媒体与宿主后另做授权运行验证。',category='Engine / Overworld Integration / Generic Kernel')
source_corrections={'80':'26,31','82':'25,30,31','84':'28,33','88':'25','89':'25','90':'25,26','91':'25','92':'27','93':'26','94':'26','95':'27','96':'25,26','97':'29,25','104':'28,25','110':'24,28','111':'24,28','112':'1,30,28','113':'26','114':'28,26'}
for c in CAP:
 k=c['capability_id'].split('-')[-1]
 if k in source_corrections:c['source_paths']=srcs(source_corrections[k])
write_tsv('capability-coverage.tsv',list(CAP[0]),CAP)
if not (OUT/'findings.json').exists():(OUT/'findings.json').write_text('[]\n')
# File classification and exact material identity. Added files are scoped reads,
# not claims of whole other-module review.
extra=[
('Data/Scripts/010_Data/002_PBS data/014_TrainerType.rb','SOURCE_TEXT_SCHEMA','1–134 full schema/default/editor/resource text','SUPPORTED_STATIC','01,02,03','该训练家类型schema已审；Editor/资源真实可达仍未运行。'),
('Data/Scripts/010_Data/002_PBS data/015_Trainer.rb','SOURCE_TEXT_SCHEMA','1–213 full schema/conversion text','SUPPORTED_STATIC','01,12','普通训练家转换数据机制审读；全作者数据语义另列。'),
('Data/Scripts/015_Trainers and player/001_Trainer.rb','SHARED_SOURCE_TEXT','1–62 targeted','PARTIAL','01,02,03','只核类型技能/Flags、属主资源接口。'),
('Data/Scripts/010_Data/001_GameData.rb','SHARED_SOURCE_TEXT','216–232 identity comparison','PARTIAL','35,62','数据身份和对象比较门；全注册/编译不在本文件读范围。'),
('Data/Scripts/003_Game processing/005_Event_Handlers.rb','SHARED_SOURCE_TEXT','97–197 full generic/symbol handler operations','PARTIAL','77','只核末写/无源copy/直接优先与条件首匹配，不执行处理器。'),
('Data/Scripts/001_Technical/001_Debugging/001_PBDebug.rb','SHARED_SOURCE_TEXT','1–32 wrapper/log boundaries','PARTIAL','04,14','普通异常报告包装，报告自身失败不保证继续。'),
('Data/Scripts/001_Settings.rb','CONFIGURATION_TEXT','17/131/233/238 targeted values and related search','PARTIAL','02,12,13,62,83','机制8、最高100、主动治疗/糖果门；不作全Settings语义覆盖。'),
('Data/Scripts/002_BattleSettings.rb','CONFIGURATION_TEXT','critical/mechanics/X/SMARTER_WILD setting search','PARTIAL','02,20,22,62','只核M09实际消费配置；不扩到全部战斗配置。'),
('Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb','SHARED_SOURCE_TEXT_COMPILER','900–1063, focus 951–1063','PARTIAL','93,113','设施专用显式入口与六字段/缺文件回空机制；没有编译。'),
('Data/Scripts/019_Utilities/001_Utilities.rb','SHARED_SOURCE_TEXT','1–61 combination/language','PARTIAL','79,96','组合行为已审；其余工具未审。'),
('Data/Scripts/011_Battle/001_Battle/001_Battle.rb','SHARED_SOURCE_TEXT','120–174 defaults','PARTIAL','105,109','回放构造字段缺省；全普通战斗主体另属M07。'),
('Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb','SHARED_SOURCE_TEXT','1–330,365–395 targeted switch/record/entry paths','PARTIAL','05,09,80,102,108,110','M09过滤、询问/随机辅助、参战口径、入场终扫；中间危害完整行为另属M07。'),
('Data/Scripts/011_Battle/001_Battle/006_Battle_ActionUseItem.rb','SHARED_SOURCE_TEXT','1–80 registration/consumption/refund','PARTIAL','12,13,109','资格/登记/扣资源时点；实际完整物品效果另属M05/M08。'),
('Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb','SHARED_SOURCE_TEXT','42–68,185–220','PARTIAL','01,04,99,106','普通/Palace选招入口与AI命令跳过。'),
('Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb','SHARED_SOURCE_TEXT','262–280,330–348,487–515','PARTIAL','87,104,110','中止捕获、正常终局、回放副本形态/初始物品恢复；不是全结果域审查。'),
('Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb','SHARED_SOURCE_TEXT','360–393 perish/yawn source checkpoint','PARTIAL','32,87','保存歌源→倒下→检查点正决定出口；全回合末另属M07。'),
('Data/Scripts/011_Battle/004_Scene/001_Battle_Scene.rb','SHARED_SOURCE_TEXT_UI','96–112,204–220','PARTIAL','110','取消中止及消息自动推进静态；宿主逐帧未验证。'),
('Data/Scripts/011_Battle/002_Battler/004_Battler_Statuses.rb','SHARED_SOURCE_TEXT','10–175,270–310','PARTIAL','31,32,33','普通睡眠输入和瞌睡到期无来源查询区分。'),
('Data/Scripts/011_Battle/003_Move/006_MoveEffects_BattlerStats.rb','SHARED_SOURCE_TEXT_PARAMETERS','all named statUp/statDown assignments, including order; ordinary/compound ranges','PARTIAL','25,26,27,28,29,30,52','核AI消费参数，不重复认证M08所有真实效果及状态提交。'),
('Data/Scripts/011_Battle/003_Move/007_MoveEffects_BattlerOther.rb','SHARED_SOURCE_TEXT','20–110','PARTIAL','32','瞌睡起用真实普通睡眠资格与计数2，非到期门。'),
('Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb','SHARED_SOURCE_TEXT_PARAMETERS','1–740,1280–1587','PARTIAL','38,39,40,41,42,43','基底参数/HP/速度/重量/状态/计数/IV/NaturalGift实际查询已核，保护其它真实域不在本增读范围。'),
('Data/Scripts/011_Battle/003_Move/009_MoveEffects_MultiHit.rb','SHARED_SOURCE_TEXT_PARAMETERS','195–229,282–308,315–355','PARTIAL','46,47','日光基底/三项Geomancy/蓄防与特攻真实参数；不执行两回合。'),
('Data/Scripts/011_Battle/003_Move/012_MoveEffects_ChangeMoveEffect.rb','SHARED_SOURCE_TEXT_DATA','695–763,815–835,924–990,1020–1106,1137–1179,1233–1256,1286–1307','PARTIAL','66','完整调用排除列表及代际项文本；本地预测消费者已全读；真实嵌套执行由M08。'),
('Data/Scripts/011_Battle/003_Move/013_MoveEffects_SwitchingActing.rb','SHARED_SOURCE_TEXT','1–146,164–248,562–619,787–815','PARTIAL','69,72,73,108','攻击后选择替补链及号令/安可黑名单；其它真实控制不扩审。'),
('Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb','SHARED_SOURCE_TEXT','378–410','PARTIAL','108','紧急退出训练家/EOR/负选择分支；完整能力由M08。'),
('Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb','SHARED_SOURCE_TEXT','447–473,1520–1555','PARTIAL','108','EJECTPACK/EJECTBUTTON/REDCARD的选择流，随机不同询问；其它物品由M08。'),
('Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb','SHARED_SOURCE_TEXT','48–60','PARTIAL','110','副本离场形态提交调用。'),
('Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb','SHARED_SOURCE_TEXT','209–285','PARTIAL','84,111','设施准备先于快照，尺寸/默认场域/背景输入；全触发域由M07/M06。'),
('Data/Scripts/014_Pokemon/001_Pokemon.rb','SHARED_SOURCE_TEXT','150–180,1198–1209','PARTIAL','96,110','形态写全局图鉴与空训练家默认拥有者；其它个体域由M04。'),
('Data/Scripts/014_Pokemon/005_Pokemon_Owner.rb','SHARED_SOURCE_TEXT','1–38','PARTIAL','96','默认记录四字段的含义；无测试执行。'),
('Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb','SHARED_SOURCE_TEXT','178–215','PARTIAL','110','BURMY离场必须endBattle+传入used标志；全形态域非M09。'),
('Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/004_ChallengeGenerator_BattleSim.rb','SHARED_SOURCE_TEXT_DX','1–180,330–430','PARTIAL','112','只核累积及真实1%/近似99%消费者；完整模拟主体属M12，其GR3-M12-002不吞并。')]
file_rows=[];identities=[]
for x in FILES:
 p=REF/x['path'];blob=gitblob(x['path']); b=p.read_bytes()
 identities.append({'repo':'reference','path':x['path'],'commit':RC,'blob':blob,'matches_assignment':blob==x['git_blob'] and sha(b)==x['sha256']})
 caps=[c['capability_id'] for c in CAP if x['path'] in c['source_paths'].split('|')]
 file_rows.append(dict(source_path=x['path'],git_blob=blob,category='SOURCE_TEXT_PRIMARY',read_scope='Full behavior text; all conditions/parameters/phase/return branches read; comments/logging separately bounded where material',status='SUPPORTED_STATIC',capability_ids='|'.join(caps),limitations='静态文本审读；未执行Ruby/参考/案例/宿主/序列化。'))
for p,cat,scope,status,keys,lim in extra:
 file_rows.append(dict(source_path=p,git_blob=gitblob(p),category=cat,read_scope=scope,status=status,capability_ids='|'.join('M09-'+x.zfill(2) for x in keys.split(',')),limitations=lim))
# Every available facility pair, plus ordinary trainer inputs, receives its own sample record.
for p in sorted((REF/'PBS').glob('*.txt')):
 if not (p.name.startswith(('cup_','battle_tower_')) or p.name in ['trainers.txt','trainer_types.txt','battle_facility_lists.txt']):continue
 relative=str(p.relative_to(REF));ls=p.read_text(encoding='utf-8-sig').splitlines()
 data=[i+1 for i,l in enumerate(ls) if l.strip() and not l.lstrip().startswith('#')]
 full=p.name=='battle_facility_lists.txt'
 scope='all sections/Trainers/Pokemon/Challenges fields' if full else 'first trainer section + last section fields' if 'trainers' in p.name or p.name=='trainer_types.txt' else 'first two template rows and last template row'
 consumed='存在且被显式设施名单引用' if p.name.startswith('battle_tower_') or p.name.startswith(('cup_poke_','cup_little_','cup_pika_')) or '_single' in p.name else '仅存在；当前设施名单未引用' if p.name.startswith('cup_fancy_') else '普通训练家schema输入'
 file_rows.append(dict(source_path=relative,git_blob=gitblob(relative),category='PBS_TEXT_DATA',read_scope=scope+f'; data boundary lines {data[0]}..{data[-1]}',status='SUPPORTED_STATIC' if full else 'PARTIAL',capability_ids='M09-113|M09-93' if full or p.name not in ['trainers.txt','trainer_types.txt'] else 'M09-01|M09-12|M09-113',limitations=consumed+'；样本不是全内容语义/编译/实际启用证明。'))
file_rows.extend([
 dict(source_path='Data/trainer_lists.dat',git_blob='',category='COMPILED_BINARY_MISSING',read_scope='existence checked only',status='MISSING_MATERIAL',capability_ids='M09-93|M09-114',limitations='目录缺编译物，禁止反序列化；仅可描述文本编译/加载机制。'),
 dict(source_path='Battles/*.dat',git_blob='',category='RECORD_BINARY_MISSING',read_scope='inventory/availability checked',status='MISSING_MATERIAL',capability_ids='M09-104|M09-114',limitations='无实际录像字节或产出者证据；未反序列化。'),
 dict(source_path='Data/Map*.rxdata|Data/MapInfos.rxdata',git_blob='',category='DEMO_EVENT_BINARY_MISSING',read_scope='baseline inventory checked',status='MISSING_MATERIAL',capability_ids='M09-94|M09-114',limitations='接待、收费、奖励、会话显式推进和录像提升的地图事件链无法检查。'),
 dict(source_path='Audio/|Graphics/|Plugins/|Game.ini|Game.rxproj',git_blob='',category='HOST_RESOURCE_MISSING',read_scope='baseline inventory checked',status='MISSING_MATERIAL',capability_ids='M09-94|M09-103|M09-114',limitations='实际媒体/UI/插件/宿主运行分开未证，不据脚本名字声称可运行。')])
write_tsv('file-coverage.tsv',['source_path','git_blob','category','read_scope','status','capability_ids','limitations'],file_rows)
for x in SPECS:
 b=(ROOT/x['path']).read_bytes();blob=gitblob(x['path'],False)
 identities.append({'repo':'formal','path':x['path'],'commit':SC,'blob':blob,'matches_assignment':blob==x['git_blob'] and sha(b)==x['sha256']})
(OUT/'input-identities.json').write_text(json.dumps({'reviewer_task':'/root/m09_ai_facilities_v3','checked_inputs':identities,'mismatches':[i for i in identities if not i['matches_assignment']],'interpretation':'Identity only; semantic judgments in coverage/report; no behavior cases executed'},ensure_ascii=False,indent=2)+'\n')
# Clause serialization: each substantive paragraph, bullet and table data row is
# a separate row. Family-specific source mapping was manually selected above.
RANGES={
 '51':[(9,18,'01,04,14'),(19,30,'02,03,04'),(33,61,'05,06,07,08'),(62,73,'09,10'),(74,100,'11'),(102,125,'12,13'),(128,144,'14,15,16')],
 '51-data':[(7,28,'12,13'),(30,80,'12,13'),(82,88,'05,06,07,08')],
 '52-a':[(9,19,'17,19,23'),(25,35,'17'),(37,66,'18'),(72,80,'19,20'),(82,98,'21'),(100,108,'22'),(114,122,'23'),(124,140,'24'),(142,174,'25,26,27,28,29,30'),(178,207,'31,32,33'),(211,237,'34,35,36'),(241,243,'37')],
 '52-a-data':[(7,15,'77'),(17,28,'37'),(30,143,'25,26,27,28,29,30'),(145,178,'31,32,33'),(180,199,'34,36'),(201,213,'18,35'),(215,235,'35'),(237,260,'77')],
 '52-b':[(9,19,'17,77'),(25,61,'38,39,40,41,42,43'),(63,73,'44,54'),(77,103,'45,46,47,48'),(107,140,'49,50,51,52,53,54'),(146,174,'55'),(176,188,'56,57'),(192,196,'58'),(198,210,'59'),(212,228,'60,61,54')],
 '52-b-data':[(7,15,'77'),(17,25,'55,56,53,60'),(27,32,'52,57'),(34,36,'42'),(38,50,'38,39,40,41,42,43,44,58,59,60,61'),(52,62,'45,46,47,48'),(64,74,'49,50,51,53'),(76,86,'54'),(88,107,'55')],
 '52-c':[(9,17,'62,77'),(23,60,'62'),(62,77,'63'),(81,102,'64,65'),(106,130,'66,67,68'),(136,146,'69'),(148,158,'70,71'),(160,180,'72,73,74'),(184,197,'75,76')],
 '52-c-data':[(7,24,'77'),(26,30,'62'),(32,40,'67,71,76'),(42,50,'75'),(52,62,'64,65'),(64,74,'66,67,68'),(76,88,'69,70,71,72,73,74'),(90,176,'62'),(178,187,'62,73,76')],
 '54':[(7,13,'78,79,80'),(17,27,'78'),(29,41,'79'),(43,49,'80'),(51,70,'81'),(74,93,'83'),(95,103,'84'),(105,113,'82'),(115,136,'85,87'),(138,144,'86')],
 '54-data':[(7,24,'82'),(26,47,'78,82'),(49,64,'81'),(66,86,'78,81,83,85'),(88,109,'85,86')],
 '55':[(7,15,'88,89,90'),(19,24,'88,82'),(26,48,'89,90'),(50,57,'90'),(59,65,'91'),(67,99,'92,93'),(101,103,'95,96,97'),(105,112,'80,94'),(114,119,'84,104'),(121,132,'84,89,90,91,92')],
 '56':[(7,13,'98,102'),(17,55,'98'),(57,59,'100'),(61,70,'99'),(72,81,'100'),(85,95,'101'),(97,110,'102,103'),(112,126,'99,100,101,102')],
 '58':[(7,35,'104'),(37,65,'105'),(67,83,'106'),(87,103,'107'),(105,122,'108'),(124,130,'99,102,106'),(132,134,'109'),(138,140,'104'),(142,150,'105,109,110'),(152,154,'109'),(156,162,'110')],
 '57':[(9,22,'95,96,97'),(28,49,'95'),(51,57,'96'),(61,69,'97'),(73,83,'97,96'),(87,100,'95,96,97')]
}
cap_by={c['capability_id'].split('-')[-1]:c for c in CAP}
def clause_caps(doc,line):
 if doc in RANGES:
  for a,b,keys in RANGES[doc]:
   if a<=line<=b:return [cap_by[k.zfill(2)] for k in keys.split(',')]
 return [c for c in CAP if SPEC.get(doc) in c['spec_paths'].split('|')]
# All semantic source tokens: used only to improve loci of already reviewed table rows.
source_texts={x['path']:(REF/x['path']).read_text().splitlines() for x in FILES}
def refine(text,selected):
 ids=set(re.findall(r'[A-Z][A-Za-z0-9_]{9,}',text))
 hits=[]
 for p in set(s for c in selected for s in c['source_paths'].split('|')):
  rows=source_texts.get(p,[]);found=[str(i+1) for i,l in enumerate(rows) if any(t in l for t in ids)]
  if found:hits.append(p+':'+','.join(found))
 return '|'.join(hits)
rows=[];test_counts={}
for doc,path in SPEC.items():
 if doc.startswith('t-'):continue
 sec=''; meaningful=0
 for i,l in enumerate((ROOT/path).read_text().splitlines(),1):
  if l.startswith('#'):sec=l.lstrip('# ').strip();continue
  if not l.strip() or l.strip()=='---' or re.match(r'^\|\s*:?-',l):continue
  if i<7:continue
  if l.startswith('|') and any(l.startswith('| '+x) for x in ['效果身份','物品 |','ID |','族 |','评级 |','输入']):continue
  selected=clause_caps(doc,i)
  if not selected:continue
  meaningful+=1
  limits='对应能力 '+','.join(c['capability_id'] for c in selected)+'；静态条款支持，运行=0。'
  status='SUPPORTED_STATIC'
  if any(t in l for t in ['未运行','无运行','运行未决','未验证','U01','U05','前向保留','保留责任']):status='PARTIAL';limits+='实际材料/运行或非本地依赖保留；不将审计状态文字作行为证明。'
  if '未决' in sec and i>30:status='PARTIAL'
  if doc=='51' and i==155:
   status='PARTIAL';limits+=' GR3-M09-001 P3/OPTIONAL：录像下游编号WP57误指，实际WP58；其余行为受支持。'
  loci=refine(l,selected) or '|'.join(c['source_loci'] for c in selected)
  label=(l.split('|')[1].strip() if l.startswith('|') else l[:75])
  rows.append(dict(spec_path=path,clause=f'{sec} / L{i} / {label}',source_paths='|'.join(sorted(set(p for c in selected for p in c['source_paths'].split('|')))),source_loci=loci,status=status,test_design='；'.join(dict.fromkeys(c['test_design'] for c in selected)),limitations=limits))
# Test rows are individually series-qualified, never merged by short W/A IDs.
for doc in ['t-ai','t-fac','t-fc']:
 path=SPEC[doc];series='';count=0
 for i,l in enumerate((ROOT/path).read_text().splitlines(),1):
  if l.startswith('## '):series=l[3:].split('：')[0].strip();continue
  if not re.match(r'^\| (?:[A-Z]\d+|FC-\d+)',l):continue
  if doc=='t-ai' and series=='AB':continue
  if doc=='t-fc' and not l.startswith('| FC-'):continue
  tid=l.split('|')[1].strip();q=series+':'+tid
  count+=1
  if doc=='t-ai':
   chosen=[c for c in CAP if c['capability_id'].split('-')[-1].isdigit() and int(c['capability_id'].split('-')[-1])<=77 and (q in c['test_design'] or tid in c['test_design'])]
   if not chosen:chosen=[c for c in CAP if {'AI':'51','AE':'52-a','BE':'52-b','CE':'52-c'}.get(series) in [k for k,v in SPEC.items() if v in c['spec_paths'].split('|')]]
  elif doc=='t-fac':
   keys={'QC':range(78,88),'WS':range(88,95),'PA':range(98,104),'RC':range(104,112)}[series]
   chosen=[cap_by[str(k).zfill(2)] for k in keys]
  else:chosen=[cap_by[str(k)] for k in [95,96,97]]
  # The body/cases were read above; this line packages their source support.
  rows.append(dict(spec_path=path,clause=f'{q} / L{i}',source_paths='|'.join(sorted(set(p for c in chosen for p in c['source_paths'].split('|')))),source_loci=refine(l,chosen) or '|'.join(c['source_loci'] for c in chosen),status='SUPPORTED_STATIC',test_design=f'{q}：逐行检查法律前提、指定阶段预期、数值和邻近反向；NOT_EXECUTED',limitations='测试设计审读；未执行案例/向量、未构造参考实例或仿制模拟器；该测试不证明所有组合覆盖。'))
 test_counts[doc]=count
rows.append(dict(spec_path='deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md',clause='§10 / L253 / Battle Arena cross-module consumer',source_paths=SRC['23'],source_loci='58–94,111–200',status='PARTIAL',test_design='PA-P28与首轮P16成对：3/4/5连续裁判和补位无新对阵提示；静态审读，运行0',limitations='GR3-M10-004 P2归M10；本轮补读该正式行证实更替提示/每3回合残留，与WP56/58冲突。M09本地正确不覆盖该消费者；历史B028关闭不改。'))
write_tsv('spec-coverage.tsv',['spec_path','clause','source_paths','source_loci','status','test_design','limitations'],rows)
# Precise historical reuse: immutable per-ID records, qualified semantics and
# current clauses. No state transition on any historical ledger is performed.
controls=json.loads((OUT/'regression-controls.json').read_text())
nav={r['original_id']:r for r in csv.DictReader((OUT.parent/'regression-229.tsv').open(),delimiter='\t')}
final_path='review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/all229-dispositions.json'
final_records=json.loads((ROOT/final_path).read_text())['records']
final_blob=subprocess.check_output(['git','-C',str(ROOT),'rev-parse',f'c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:{final_path}'],text=True).strip()
reg_notes={
'GIR-FD82-A046':('51 §4 L121/51-data L24,L28；AI-I02/I08','AI估量1、实际主动H101/105请求25/26、持物门三分；SITURUSBERRY不命中，未把估量改真实恢复。','M09只核AI接收端；WP28真实族和全局最低修订由M05/M08共同裁决。'),
'GIR-FD82-B003':('54 §6 L121–136；54-data §5 L94–109；QC-Q47','精确14键、11设置/3仅消费者；sleep与sleepclause无别名；skillswapclause共享目标门，默认杯各自启用。','M09负责设施设置与消费者，WP39/47其它作者入口交M07/M08。'),
'GIR-FD82-003':('52-a-data §6/52-b-data §1/52-c-data §1；CE-C59；54 §6；56 §1/4；58 §3/5','源行/继承历史未成为未来结构要求；族+身份、外部录像字段、copy缺源和共享副作用保留；两种内部表示可等价，叠重复/跨族动态alias不可。','仅消费B12/B13本地贡献；全部root/extensions限定保留，不代签其它11贡献。'),
'GIR-FD82-B010':('54 §6.1；52-b §2.1；QC-Q41/BE-B02b','默认加载后非冰U/冰T同L50，条款假目标资格过、阈20、r19/r20分；条款真资格拒，AI仍拒冰。','重读原OHKO/条款与AI独立门；没有执行继承加载或命中。'),
'GIR-FD82-B017':('52-b §4 L126；BE-B28/B63；WP46 §6.4接收','实际整数平均并分别限总HP与AI浮比不同；U51/60,T150/200实际60/100；HealBlock非拒、替身早拒。','M09消费AI接缝；真实HP提交和MH39–44完整裁决归M07/M08，未借计数关闭。'),
'GIR-FD82-B018':('58 §7 L166；test-fac QC47/WS35/PA28/RC27','RC现W01–26加W22b=27，四族137；旧W01–23加W22b24及原总127身份意义保持，新W24–26独立列。','只核M09计数传播；WP46/48/50各族完整计数属M07/M08；计数非语义覆盖。'),
'GIR-FD82-B020':('51 §4 L104–110；51-data §1；AI-I06/I07','完整Items先通用/CanUse后分类；POTION+ETHER先候选后nil索引失败、整阶段无UseItem/无消费；移除ETHER可POTION一次消费。','实际物品资格源由当前调用参数核；正常异常报告才继续，未保证报告/插件失败也继续。'),
'GIR-FD82-B021':('51 §3.3；52-a §4.1；AI-S08/S09/AE-G13','H11/h9雨盘-1与诅咒2得d1，两意愿阈4/2不过；h2局部d>=h假；无诅咒d-1；非最终动作证明。','每分量取整/最低1与Wish/Perish例外完整实读；下游仅合格局部consumer。'),
'GIR-FD82-B022':('52-b-data §2.4；52-c-data §2.5/2.6；BE-B02b/B61/CE-C56/C57','Assurance目标+8与Revenge整体分开；OHKOIce独立冰门；HelpingHand整体100/目标+5；ImprisonUser100/直接108非116。','全族身份/位置/复制/参数与正文相核；839键口径只作完整性，不替代114行为族。'),
'GIR-FD82-B023':('52-b §3 L101；BE-B62','默认GEOMANCY User0不消费目标两回合/升阶；HP203/50×无物/香草四组合100，全三项封顶整体20，部分封顶100。','PBS User、候选0target、整体无分/失败绑定及真实三项参数实读；未运行AI。'),
'GIR-FD82-B024':('52-c §2.1 L58；52-c-data §4 L116/165；CE-C05/C58','FIREGEM基础6；机制5/8有EMBER得8/6，无可用火伤害两代0；比较参数是机制世代。','18配对及39增幅物完整表核；估量不等真实伤害增幅。'),
'GIR-FD82-B025':('54 §6 L129–136；QC-Q43/Q44','draw读取检查点使用者，灭亡歌先保存歌源；双Lapras两个最后出招方对照均决定2；selfKO最后使用者方向独立。','重读Perish局部正决定门；全终局/成长出口由M07共同裁决，未运行四轮。'),
'GIR-FD82-B027':('54 §2.3 L47；55 §2.3；WS-W28/W29/W35','活动P收到[]提交并活动空，包装false；nil不提交不覆盖P且返回nil；普通UI空确认未证。','直接工具边界保持，不能把条件假混为同返回身份。'),
'GIR-FD82-B028':('56 §3；58 §5.3；PA-P16/P19/P20/P28/RC-W25','开场复位；正常补位保留count/mind/skill/首发HP/prompt，3/4/5轮继续裁判；最后HP写穿与终局保持。','孤立复位全Scripts仅定义；真实补位链核，未执行Growl实例。'),
'GIR-FD82-B029':('58 §5.2/6.3；RC-W16/W24/W25/W26','BatonPass攻击后询问记录1/回放同点消费；Roar随机不询问；Arena拒候选；首命令前EjectPack亦记，负选已耗不替换，EOR延后。','重读全部辅助入口调用者与item先ability首真停止；无回放/序列化执行。')}
reg=[]
for x in controls:
 ident=nav[x['id']];idx=int(ident['FINAL1_pointer'].split('/')[-1]);f=final_records[idx]
 assert f['id']==x['id']
 note,judgment,limit=reg_notes[x['id']]
 contrib=[]
 for c in f.get('all_contributor_joins',[]):
  key=c['record_key']
  if key.startswith(('B12/','B13/')):
   contrib.append({'record_key':key,'precise_actual_identity':c.get('actual_independent_report',c.get('independent_disposition')),'qualified_semantic_fields_read':['qualified_attributed_actual_semantic_evidence','fixed_qualified_independent_semantic_basis'],'limits':'Only named M09 local scope; historical signature not transferred'})
 reg.append({'id':x['id'],'status':'SUPPORTED_STATIC','read_scope':'Approved complete effective premises, minimum_counterexample, minimum_revision, determinate_recheck, current_qualifications, extension_decisions; original root_adjudications and applicable extension root_review; exact FINAL1 per-ID semantic normal/reverse/partial/minimum judgment and B12/B13 local reasons; current M09 clauses and source families reread. Raw_reports retained only as immutable history, not current verdict.','current_clauses':note,'current_semantic_judgment':judgment,'related_new_findings':[],'historical_state_unchanged':ident['old_state'],'identity_reuse':{'original_object_sha256':ident['original_object_sha256'],'approved_object_sha256':ident['approved_object_sha256'],'FINAL1_object_sha256':ident['FINAL1_object_sha256'],'FINAL1':{'commit':'c2bc1a341ba6acdf7c8c111dc88d39a162a093d6','path':final_path,'pointer':ident['FINAL1_pointer'],'git_blob':final_blob},'original_pointer':ident['original_pointer'],'approved_pointer':ident['approved_pointer'],'accepted_contribution_keys':ident['accepted_contribution_keys'],'exact_identity_integrity':'Root verified whole458 original/approved and whole229 FINAL1 object hashes plus all341 unique keyed joins; integrity only.'},'semantic_reuse_reason':'Same fixed reference and exact fixed formal carrier; full effective qualification and relevant final semantic judgment read, then current behavior independently compared. Counts/receipt alone never used as PASS.','effective_input_fields':{'premises':x['approved'].get('premises'),'minimum_counterexample':x['approved'].get('minimum_counterexample'),'minimum_revision':x['approved'].get('minimum_revision'),'determinate_recheck':x['approved'].get('determinate_recheck'),'current_qualifications':x['approved'].get('current_qualifications'),'extension_decisions':x['approved'].get('extension_decisions')},'final_semantic_field_names_read':[k for k in ['normal_reverse_partial_failure_review','current_semantic_judgment','minimum_and_determinate_recheck_judgment','normal_reverse_partial_failure','minimum_revision_and_determinate_recheck'] if k in f],'applicable_contribution_reuse':contrib,'limits':limit,'execution':{'reference':0,'cases':0,'runtime':0,'deserialization':0}})
old_original=json.loads((ROOT/'review/global-independent-review/2026-10-03-fd82a639/findings.json').read_text())
b030=next(x for x in old_original if x['id']=='GIR-FD82-B030')
nonrequired=[]
for x in json.loads((OUT.parent/'regression-identity-checks.json').read_text())['original_nonrequired4']:
 nonrequired.append({'id':x['id'],'object_sha256':x['object_sha256'],'old_required_revision':False,'current_action':'PRESERVED_NOT_REOPENED','read_scope':'Complete effective B030 qualification/root adjudication/premises/counterexamples/minimum/recheck read' if x['id']=='GIR-FD82-B030' else 'Identity/title/old nonrequired boundary; outside M09 behavior scope','current_semantic_review':'WP54 preparation + WP58 exhaustive18fields + WP45 defaults jointly imply three differences; optional clarification does not establish new required defect. No new M09 evidence contradicts effective old decision.' if x['id']=='GIR-FD82-B030' else 'N/A to M09; not reassigned or silently reopened','new_finding':None})
for r in reg:
 if r['id']=='GIR-FD82-B028':
  r['related_new_findings']=['GR3-M10-004']
  r['cross_module_disagreement']={'owner':'M10','finding':'GR3-M10-004','status':'CONFIRMED_CURRENT_CONSUMER_MISMATCH','formal_path':'deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md','loci':'§10 L253','read_scope':'This exact current row independently reread after M10 notice, compared with source Arena58–94,111–200 and current WP56/58/PA-P28','judgment':'M09 local clauses supported; WP67-A still promises replacement matchup prompt/every3 rounds. Nonlocal consumer is a new M10 finding, not a historical reopening or whole-ID PASS.'}
  r['limits']+=' 当前M10消费者残留异议见GR3-M10-004；旧FINAL1复用不覆盖这一当前新证据。'
(OUT/'regression-review.json').write_text(json.dumps({'reviewer_task':'/root/m09_ai_facilities_v3','kind':'QUALIFIED_STATIC_CONTROL_CONSUMPTION_NO_REOPENING_OR_SIGNATURE_TRANSFER','formal_commit':SC,'reference_commit':RC,'controls':reg,'nonrequired4':nonrequired,'execution':{'runtime':0,'reference':0,'static_cases':0,'serialization':0}},ensure_ascii=False,indent=2)+'\n')
counts={
 'capability_families':len(CAP),'capability_status_counts':{s:sum(c['status']==s for c in CAP) for s in sorted({c['status'] for c in CAP})},
 'assigned_source_files':len(FILES),'file_rows':len(file_rows),'assigned_specs':len(SPECS),'spec_rows':len(rows),
 'test_rows':test_counts,'new_findings':len(json.loads((OUT/'findings.json').read_text())),'execution':0}
(OUT/'coverage-counts.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(counts,ensure_ascii=False))
