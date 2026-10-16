"""Evidence-only assembly. Does not execute reference or behavior models."""
from pathlib import Path
import collections
import datetime
import gzip
import hashlib
import json
import subprocess

REPO = Path('/workspace/pokemon-essentials-clean-room')
ROOT = REPO / 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
OUT = ROOT / 'tasks/item_catalog_schema_final_reception'
PRODUCER = ROOT / 'evidence/external-recovered/external_item_atomic_completion/70dee4e34d08cf32cfaee41d1fa21cd4e4b8d446'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
CAT1 = 'deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md'
CAT2 = 'deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md'
MAIN = 'deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def dump(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def identity(path, repo=None, commit=None):
    raw = path.read_bytes()
    val = dict(path=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(),
               git_blob_from_bytes=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),
               mode=oct(path.stat().st_mode & 0o777))
    if repo and commit:
        rel = str(path.relative_to(repo))
        original = subprocess.check_output(['git', '-C', str(repo), 'show', f'{commit}:{rel}'])
        val.update(repo=str(repo), commit=commit, repository_path=rel,
                   fixed_object_equals_worktree=(original == raw))
        assert original == raw, rel
    return val

# Exact producer applicability is a qualification, not a semantic selection by a
# fresh keyword scan: finish_review.py 123-130 and its frozen reception rows.
catalog = json.loads((PRODUCER / 'evidence/catalog-reception.json').read_text())
applicable = [v for v in catalog['rows'] if v['disposition'] == 'FINITE_ITEM_FIXTURE_AND_COMMON_PREMISES_RECEIVED']
atoms = json.load(gzip.open(PRODUCER / 'evidence/semantic-atoms.json.gz', 'rt'))
groups = {v['id']: v for v in atoms['groups']}
assertions = {v['id']: v for v in atoms['assertions']}
handlers = {v['id']: v for v in atoms['handler_units']}

common = [
    dict(id='IC-P01', locations=[dict(path=CAT1, lines=[1,3]),dict(path=CAT2,lines=[1,3])],
         meaning='全部向量为固定B8/R上的SOURCE_STATIC或DERIVED_VECTOR，execution=NOT_EXECUTED；素材、实际宿主和任意插件/组合不由静态接收批准。'),
    dict(id='IC-P02', locations=[dict(path=CAT1,lines=[161,161]),dict(path=CAT1,lines=[189,191]),dict(path=MAIN,lines=[173,173])],
         meaning='普通伤害仅改变所列项：L50、P60、攻防100、单目标、中性、非会心、无本系/天气/灼伤/其它道具修正、最大随机，基础整数28。能力为有效输入，除明列压制/模式破坏变化。先按相应P/A/D/F槽及百分数取整，不能把倍率任意移至最终伤害。'),
    dict(id='IC-P03', locations=[dict(path=MAIN,lines=[9,31])],
         meaning='身份登记、已装载记录、当前持有C和普通有效性分开；先实际caller后局部门。C写穿持久个体，I为还原记录，R回收，P拾取物及序号，Belch为本战吃果。通用触发、直接消费、主动背包消费分列，未被真正调用不补写。'),
    dict(id='IC-P04', locations=[dict(path=CAT1,lines=[230,241])],
         meaning='精神香草六对照：普通单打存活非蛋非变身T，默认真实TACKLE槽PP正并有正常使用历史；U DISABLE成功通过近期普通招/槽/PP/香气幕/命中/保护/反射等前门。无查封/魔法空间/腐蚀/KLUTZ/压制/共生/中改写，反馈正常。继续同一T，无倒下/换人/变身/初始化/新Disable；菜单较慢情形与已登记执行较快情形独立。'),
    dict(id='IC-P05', locations=[dict(path=CAT1,lines=[243,253])],
         meaning='追加HI34–36各对照独立；原行与其它WP不被计数接收覆盖。HI34明确主动/持物/AI三入口及排除连锁，HI35重量单位0.1kg及能力/物品各自有效门，HI36只比较同口径(族,物品)完整展开身份，身份相同不证明行为或运行。'),
    dict(id='IC-P06', locations=[dict(path=CAT1,lines=[255,268]),dict(path='deliverables/final-specification-set/test-catalog/combat-requirements-wp47-ab.md',lines=[98,109])],
         meaning='N夹具：默认合法NATURALGIFT真实槽/PP正/可行动、物理单目标、当前代双方零阶；U有效PARENTALBOND、ORANBERRY，H160/h81，C=I=ORAN，R/P空，Belch假；T有效JABOCABERRY可食且首损δ1>0后仍活，U可间伤可治可食。无明列失手/免疫/保护/替身/画皮/冰脸/抢夺/反射/压制/睡冻/换人/治疗封锁/紧张感/共生/RIPEN/CHEEKPOUCH/其它回调或异常，提示正常。合法当前能力是前提，不宣称运行获取链；本次毒类型/首基底80不等于续击最终伤害。普通停止门及正常终局还原另查，外层宿主恢复未知。'),
    dict(id='IC-P07', locations=[dict(path=CAT2,lines=[98,100]),dict(path=MAIN,lines=[94,94])],
         meaning='I08分开主动使用的实际HP请求、AI表估量和持有触发；合法SITRUSBERRY、H101/105和h1是给定输入；AI拼写表项不改变WP28真实量，也不绕WP50可治/可食/有效/半血与消费记录门。'),
    dict(id='IC-P08', locations=[dict(path=MAIN,lines=[29,31]),dict(path=CAT1,lines=[232,241]),dict(path=CAT1,lines=[257,268])],
         meaning='取消/失败/异常逐路径限定：上游取消或未进入本体不创造新的写入；中央/数据/提示正常返回才有后继。到达写点后故障仅保留真实前缀，不能补完成或统一回滚。负替补选择在退出包/按钮消费之后；下游普通招式拒绝不退款已用香草；N夹具第二击空身份失败不退款首击HP/PP/双方物品记录。无游戏/故障注入实际执行。'),
    dict(id='IC-P09', locations=[dict(path=MAIN,lines=[74,84])],
         meaning='低HP先过食果：h≤floor(H/4)通过；floor(H/4)<h≤floor(H/2)时false完全绕GLUTTONY谓词，活跃与否均可，true才需有效GLUTTONY；两种都不放宽半血以上。普通有效性、canHeal/可升与forced具体例外仍逐条有效。按root必收限定不把requires no Gluttony误作必须无贪吃者。')
]

# Each entry was manually received against the full current row, its premises,
# and the already received producer facts. These are operations, not row counts.
# Tuple: accepted operation; exact WP50 lines; producer groups; handler IDs;
# cancellation/failure/retained-prefix qualification.
M = {
'HI01': ('物理讲究头带在P槽60×1.5=90，随后公式得41；不能对基准28末乘得42。',[19,61],['G-ACTIVE','D-DamageCalcFromUser'],['H-DamageCalcFromUser-CHOICEBAND'],'计算入口未到无该修正；不由数值修正保证命中或后续消费。'),
'HI02': ('广角镜1.1与光粉0.9合成0.99，命中百分数99、闪避100；q80整数阈79，r78过、r79拒。',[18,43,45,53],['G-ACTIVE','D-AccuracyCalcFromUser','D-AccuracyCalcFromTarget'],['H-AccuracyCalcFromUser-WIDELENS','H-AccuracyCalcFromTarget-BRIGHTPOWDER'],'失败命中只拒该命中；倍率不等于实际伤害或消费。'),
'HI03': ('浮石按物品层对101整除2得50、输入1下限1；模式破坏者不跳物品层。',[17,42],['G-ACTIVE','D-WeightCalc'],['H-WeightCalc-FLOATSTONE'],'重量查询无本地菜单取消/消费；后续捕获仍查自己的门。'),
'HI04': ('先制之爪r19提升档1、r20档0；局部重排复用初始档不重新抽，不能越过更高招式优先级。',[50],['G-PRIORITY','D-PriorityBracketChange','D-PriorityBracketUse'],['H-PriorityBracketChange-QUICKCLAW','H-PriorityBracketUse-QUICKCLAW'],'只有真实到达首次排序抽样才计；局部重算不补第二抽样。'),
'HI05': ('ORAN H100/h26在可治可食有效时false半血门不要求GLUTTONY，活跃与否都+10至36；h25对照至35。',[74,79],['G-PINCH','G-HP','G-CONSUME'],['H-HPHeal-ORANBERRY'],'食果/可治前门仍可拒；false不表示需无GLUTTONY。真返回后才通用消费。'),
'HI06': ('SITRUS请求先floor(101/4)=25再RIPEN×2=50，h25至75；不是对101/2四舍五入得51。',[79],['G-HP','G-CONSUME'],['H-HPHeal-SITRUSBERRY'],'回复提交与反馈/随后消费分列；不得倒推全部路径原子。'),
'HI07': ('世代8 FIGY H100/h25请求33，性格降攻时可自混乱才混乱；forced满HP可0回复仍混乱并真返回。',[80],['G-CONFUSION','G-PINCH','G-CONSUME','G-HP'],['H-HPHeal-FIGYBERRY'],'forced仅绕所列门；0实际回复不证明假返回或不消费，后续依真返回。'),
'HI08': ('MICLE低HP门通过后，原标记假仍不触发/消费；原真保持真并消费，后续命中才清并×1.2。',[84],['G-PINCH','G-CONSUME'],['H-HPHeal-MICLEBERRY'],'命中消费标记是独立后继，不能由本体提示补作。'),
'HI09': ('STARF先收可升项再抽；仅速度可升时仍先抽速度，然后低HP门可拒且不消费。',[82],['G-STATBERRY','G-STAGE','G-PINCH'],['H-HPHeal-STARFBERRY'],'拒门前随机抽样已发生，不能声称失败无抽样。'),
'HI10': ('MENTALHERB仅定身计数5时清为0并用后消费，DisableMove=X保持；不能概括全部字段清除。',[88,90],['G-CONSUME'],['H-StatusCure-MENTALHERB'],'本地清计数与后继普通许可分列，后继拒绝不撤销香草。'),
'HI11': ('WHITEHERB七阶级负值直接归零：攻-2至0、速+3不变并标升阶；不走中央+2的单纯等转换。',[88],['G-CONSUME'],['H-OnEndOfUsingMoveStatRestore-WHITEHERB'],'无负阶拒且不消费；有负阶写入后反馈错误不自动还原。'),
'HI12': ('LEPPA按持久空PP槽X从0至10，再直接把同下标变身槽Y PP5赋10，不查身份同一。',[92],['G-CONSUME'],['H-OnEndOfUsingMove-LEPPABERRY'],'持久PP写入在战斗PP之前，两写点非原子；只有真返回后消费。'),
'HI13': ('有效OCCA在本次克制火、RIPEN有效时最终量÷4并标果；helper不查紧张感食果门。',[70],['G-RESIST'],['H-DamageCalcFromTarget-OCCABERRY'],'计算标记/反馈在前，每击后消费另到达；动画不证明目标正失血。'),
'HI14': ('匹配宝石在计算先标GemConsumed并P×1.3，首击反馈、整招后才消费；誓约同物不触发。',[66],['G-GEM'],['H-DamageCalcFromUser-FIREGEM'],'多击消费前可参与再计算；中断不补整招消费。所指FIREGEM为18类型共同组的示例绑定。'),
'HI15': ('头盔在实际接触许可及可间伤下使H101使用者损16；目标外层允许倒下不由T=0自动拒。',[22,100,109],['G-MOVE-HIT','G-HP'],['H-OnBeingHit-ROCKYHELMET'],'仅到达受击入口后判门；头盔不消费，能力/间伤门独立。'),
'HI16': ('弱点保单克制且攻+6/特攻0，只特攻+2后消费；两项都封顶则不消费。',[111],['G-MOVE-HIT','G-STAGE','G-CONSUME'],['H-OnBeingHit-WEAKNESSPOLICY'],'两项中央资格逐次；不能将部分成功回滚或给封顶项额外提升。'),
'HI17': ('红牌有候选先普通消费再查U扎根，故无实际拖出仍已耗；允许的共生发生在后拒门前。',[129],['G-MOVE-HIT','G-CONSUME'],['H-AfterMoveUseFromTarget-REDCARD'],'无候选不消费；有候选后扎根拒不退款，保留已写C/I/R/P等前缀。'),
'HI18': ('退出包前门过后先消费，负替补选择返回假而原成员仍在；回合末只离场等补位。',[127],['G-CONSUME','G-ENTRY'],['H-OnStatLoss-EJECTPACK'],'本例负选择是消费后取消/失败，不恢复物品；未到消费的前门拒另列。'),
'HI19': ('退出按钮不查普通局部换出拘束，已有后备且前门过则消费并选换，与退出包分列。',[128],['G-MOVE-HIT','G-CONSUME'],['H-AfterMoveUseFromTarget-EJECTBUTTON'],'负选择亦在已消费之后，不能以未换人证明未扣物；未进入本体不造消费。'),
'HI20': ('贝壳之铃累计损失80请求10，U45/100至55，跨半记录可清，后续危急回避可能不退出。',[131],['G-MOVE-HIT','G-HP'],['H-AfterMoveUseFromUser-SHELLBELL'],'恢复与后继退出各有实际门，不由跨半旧标记保证退出；本物不消费。'),
'HI21': ('生命宝珠可曾增伤，但所有目标最终本击替身使hitBattler门假，后段不扣H/10。',[63,130],['G-MOVE-HIT','G-HP'],['H-DamageCalcFromUser-LIFEORB','H-AfterMoveUseFromUser-LIFEORB'],'计算增伤与后段扣HP不是同一成功条件，SHEERFORCE等入口门独立。'),
'HI22': ('地形种子当前场地匹配且可升即防/特防+1并消费；拥有者浮空不构成拒门。',[140],['G-FIELD','G-STAGE','G-CONSUME'],['H-TerrainStatBoost-ELECTRICSEED'],'可升门失败不消费；通知和每次当下有效性需实际重读。'),
'HI23': ('剩饭H15/h14名义floor(15/16)=0，但中央最低恢复1至15；满HP前门拒。',[145],['G-EOR','G-HP'],['H-EndOfRoundHealing-LEFTOVERS'],'不消费，回合末实际到达与可治是前提；名义0不等于实际0。'),
'HI24': ('幸运蛋当前收益101×3整除2=151；POWER速收益(1+8)×2=18，再服从EV总/单项上限。',[150,151],['G-REWARD'],['H-ExpGainModifier-LUCKYEGG','H-EVGainModifier-POWERANKLET'],'奖励入口用持久物而非战场有效性；前置基础收益及后继上限不由此替代。'),
'HI25': ('魔法空间中的成长成员仍直接以持久当前幸运蛋参与真实收益入口，不套场上有效性删去奖励。',[27,150],['G-REWARD'],['H-ExpGainModifier-LUCKYEGG'],'入口确实已到是前提；本例不签全部奖励分配或终局流程。'),
'HI26': ('普通退出包C=I消费把新R/P记当前包并清C/I、禁共生；气球不可回收消费不新写R/P但可共生。',[31],['G-CONSUME'],['H-OnStatLoss-EJECTPACK','H-OnBeingHit-AIRBALLOON'],'不新写R/P不等于清旧R/P；写点后的故障仅保留已到前缀。'),
'HI27': ('黑色污泥毒类型满HP既不回复也不反伤；非毒可间伤H101时损floor(101/8)=12并走效果伤害反应。',[144],['G-EOR','G-HP'],['H-EndOfRoundHealing-BLACKSLUDGE'],'两分支互斥，不以毒满HP恢复失败落入反伤；后续反应实际到达另查。'),
'HI28': ('爽喉喷雾声音变化招、实计1且双方队伍未灭可升时特攻+1并直接消费，无伤害类别门。',[23,132],['G-MOVE-HIT','G-STAGE','G-CONSUME'],['H-AfterMoveUseFromUser-THROATSPRAY'],'SHEERFORCE整招后段总门仍须先到达；不因局部守卫满足补执行。'),
'HI29': ('ORAN H100/h50活跃或无GLUTTONY均恢复至60；h51两者都过不了低HP门且不消费。',[74,79],['G-PINCH','G-HP','G-CONSUME'],['H-HPHeal-ORANBERRY'],'只变h50/51的边界，GLUTTONY不扩半血以上；可治可食有效前提保留。'),
'HI30': ('SITRUS H100/h50无GLUTTONY亦通过false门，请求25至75，正常真返回才通用消费。',[74,79],['G-PINCH','G-HP','G-CONSUME'],['H-HPHeal-SITRUSBERRY'],'有效性、食果和可治不被false绕过；回复后消费按真正到达计。'),
'HI31': ('世代6五混乱恢复果H100/h50无GLUTTONY用false门，请求floor(100/8)=12至62；性格混乱另查。',[80],['G-CONFUSION','G-PINCH','G-HP','G-CONSUME'],['H-HPHeal-FIGYBERRY','H-HPHeal-WIKIBERRY','H-HPHeal-MAGOBERRY','H-HPHeal-AGUAVBERRY','H-HPHeal-IAPAPABERRY'],'性格/混乱中央资格不能被HP结果代替；仅真返回接消费。'),
'HI32': ('世代8五混乱果H100/h50用true门，无有效GLUTTONY拒；有效GLUTTONY请求33至83，性格另查。',[74,80],['G-CONFUSION','G-PINCH','G-HP','G-CONSUME'],['H-HPHeal-FIGYBERRY','H-HPHeal-WIKIBERRY','H-HPHeal-MAGOBERRY','H-HPHeal-AGUAVBERRY','H-HPHeal-IAPAPABERRY'],'未通过true门不消费；GLUTTONY有效性不与身份存在混同。'),
'HI33': ('ORAN H100/h26虽可治且物有效，先有对侧有效UNNERVE则不触发/消费；无该阻碍至36。',[74,79],['G-PINCH','G-HP','G-CONSUME'],['H-HPHeal-ORANBERRY'],'食果早门拒不抽象为半血阈值失败；不补回复或消费。'),
'HI10a': ('T先正常TACKLE，慢U成功DISABLE后香草清计数保身份并消费；下次普通菜单按身份拒登记TACKLE。',[88,90],['G-CONSUME'],['H-StatusCure-MENTALHERB'],'后续菜单拒不退香草或治疗；其它招/命令另按资格，未造下一已登记招式。'),
'HI10b': ('近期TACKLE且空禁用身份时已合法登记PP5，较快U DISABLE+香草后到T执行身份门拒；PP仍5、失败真，清近期/类型与普通历史/目标、取消连用并正常结束。',[90],['G-CONSUME'],['H-StatusCure-MENTALHERB'],'本例为已登记执行拒，与HI10a菜单拒分开；香草先前已耗不退。'),
'HI10c': ('同成员持续在场且到正常期限段，计数0跳递减及自然归零回调，TACKLE身份仍在且普通许可仍拒。',[90],['G-CONSUME'],['H-StatusCure-MENTALHERB'],'只限无新身份改写且实际到段，不签完整宿主/永久状态。'),
'HI10d': ('独立无香草成功DISABLE保持正计数5，每轮实际到期限5→4→3→2→1→0，真正1→0回调清身份。',[90],['G-CONSUME'],['H-StatusCure-MENTALHERB'],'此后仅该身份门可过，其余招式资格仍独立。'),
'HI10e': ('残留0计数/TACKLE身份独立经正常换入初始化或实际变身清理，计数0/身份空，此门可过。',[90],['G-CONSUME'],['H-StatusCure-MENTALHERB'],'不是保证其它门或最终招式成功，不能把HI10c扩成永久禁用。'),
'HI10f': ('保留身份的特殊使用同招只跳定身具名门；独立改匹配治疗招并加治疗封锁仍可由另一门拒。',[90],['G-CONSUME'],['H-StatusCure-MENTALHERB'],'特殊调用不保证成功，治疗封锁等实际前门仍保留。'),
'HI34': ('主动SITRUS H101/105、h1请求25/26至26/27并各扣库存1；主动h80/101请求25实加21至满仍扣库存。持有h80不触发/不写C/I/R/P；持有h1请求同量后清C/I、记R/P和Belch，不扣背包；AI估量1不作请求。',[79,94],['G-HP','G-PINCH','G-CONSUME'],['H-HPHeal-SITRUSBERRY'],'各为独立合法且未取消输入；主动取消不凭夹具补扣，主动和被动消费记录不互换。'),
'HI35': ('0.1kg单位2360依LIGHTMETAL至1180再FLOATSTONE至590：新沉重球率25/x8；只查封浮石至1180率45/x15，只模式破坏跳能力仍物品至1180率45/x15；两者变为2360率65/x21。',[11,17,42],['G-ACTIVE','D-WeightCalc'],['H-WeightCalc-FLOATSTONE'],'能力门和物品门独立；捕获准入/满HP/状态/调试/会心前提给定，x不保证随机捕获。'),
'HI36': ('按每行箭头源和新增身份展开，跨族同名不去重；指定Speed10/HPHeal16/StatusCure8/TargetAccuracy2/UserDamage71/TargetDamage23、32族196唯一配对，165直接+31目的复制、21复制语句；两空族0。',[3,169,175],['G-REGISTRY'],[],'身份集合比较只核同口径，不由计数关闭伤害/消费语义或证明196种物品/运行成功。'),
'U04-HI01': ('N首击目标损失在前，T先消费JABO；U反伤20至61后ORAN10至71并普通消费，C/I空、R/P记ORAN更新序号、Belch真并写穿，T记JABO；背包不变。I原不同则保留旧I。',[117,119],['G-U04','G-CONSUME','G-MOVE-HIT','G-HP'],['H-OnBeingHit-JABOCABERRY','H-HPHeal-ORANBERRY'],'第二击空身份失败不撤首击损失和双方记录；不以该局部异常保证宿主退出/恢复或正常终局还原。'),
'U04-HI02': ('N只改h101，JABO20后U81高于80，ORAN不触发，U C/I/R/P保留，T已耗；续击正常后使用结束直接耗ORAN并记R/P，Belch仍假、U81。',[121],['G-U04','G-CONSUME','G-MOVE-HIT','G-HP'],['H-OnBeingHit-JABOCABERRY','H-HPHeal-ORANBERRY'],'每击自食与直接消费有不同Belch后置；80基底不作第二击最终伤害。'),
'U04-HI03': ('N仅去有效PARENTALBOND，单击JABO20→ORAN10及普通消费至U71；末尾空物守卫跳消费，不重写原R/P/序号。',[121,123],['G-U04','G-CONSUME','G-MOVE-HIT','G-HP'],['H-OnBeingHit-JABOCABERRY','H-HPHeal-ORANBERRY'],'无第二次基底访问，故无该局部异常；正常终局还原仍为独立后继，异常不保证还原。'),
'I08': ('合法SITRUS H101/105、h1主动请求25/26至26/27；AI估量表仍1（SITURUSBERRY拼写不命中），持有触发沿自身WP50有效/可治/可食/阈值门。',[79,94],['G-HP','G-PINCH','G-CONSUME'],['H-HPHeal-SITRUSBERRY'],'主动/AI/被动分别观察，不从估量推出真实回复，也不从合法身份推出一定持物消费。')
}

assert len(M) == len(applicable) == 46
assert {v['id'] for v in applicable} == set(M)
rows = []
for old in applicable:
    key = old['id']; meaning, formal_lines, group_ids, handler_ids, prefixes = M[key]
    line = (REPO / old['path']).read_text().splitlines()[old['line']-1]
    cols = [v.strip() for v in line.strip().strip('|').split('|')]
    assert cols[0] == key and len(cols) == 3, key
    linked = []
    for gid in group_ids:
        linked += groups[gid]['assertions']
    for hid in handler_ids:
        assert hid in handlers, hid
        linked += handlers[hid]['atom_ids']
    fact_ids = list(dict.fromkeys(linked))
    premises = ['IC-P01','IC-P03','IC-P08']
    if key in ['HI01','HI02','HI03','HI04']: premises += ['IC-P02']
    if key.startswith('HI10'): premises += ['IC-P04'] if key != 'HI10' else []
    if key in ['HI34','HI35','HI36']: premises += ['IC-P05']
    if key.startswith('U04-'): premises += ['IC-P06']
    if key in ['I08','HI34']: premises += ['IC-P07']
    if key in ['HI05','HI06','HI07','HI09','HI29','HI30','HI31','HI32','HI33']: premises += ['IC-P09']
    rows.append(dict(id=key, catalog_path=old['path'], line=old['line'],
        complete_current_clause=line, input_or_premises=cols[1], expected=cols[2],
        accepted_operation=meaning, common_premises=list(dict.fromkeys(premises)),
        cancellation_failure_and_reached_prefix=prefixes,
        current_formal=dict(path=MAIN, lines=formal_lines),
        already_root_received_producer_groups=group_ids,
        already_root_received_handler_bindings=handler_ids,
        fact_binding_resolution='group IDs resolve to groups[id].assertions; handler IDs resolve to handler_units[id].atom_ids in the preserved producer semantic-atoms. Root has already received their complete meaning. This mapping receives the complete current vector operation, not another698-assertion review.',
        actual_catalog_reader='/root/item_catalog_schema_final_reception',
        source_reader_qualification='Original external_item_atomic_completion actual reader; root has received all698 meanings/all247 controls and necessary named peer interfaces. Source-location extraction here grants no new source full-read credit.',
        judgment='FINITE_CURRENT_CATALOG_OPERATION_AND_ALL_APPLICABLE_PREMISES_RECEIVED',
        execution='NOT_EXECUTED'))

dump('catalog-operative-complete-mapping.v1.json', dict(schema='gr8-item-catalog-finite-operative-reception/v1',
    utc=NOW, B8=B8, formal_tree='f292698cdd4a8e725525a9be6dc34b75faaf151e',R=R,
    producer_commit='70dee4e34d08cf32cfaee41d1fa21cd4e4b8d446',
    producer_applicability='Exactly the46 FINITE_ITEM_FIXTURE_AND_COMMON_PREMISES_RECEIVED rows of frozen catalog-reception;45 CAT1 plus1 CAT2 I08. Other484 table/header rows keep foreign primary ownership; original complete669-line read is producer qualification, not this reviewer669-line credit.',
    applicable_vectors=46, received_vectors=46, finite_unread=0,finite_unreceived=0,
    common_premises=common, vectors=rows, historical_qualifications=[dict(path=MAIN,line=179,disposition='ROOT_GLOBAL_HISTORY_JOIN_REQUIRED; old limited PASS wording is not R8 approval'),dict(path=MAIN,line=181,disposition='ROOT_GLOBAL_HISTORY_JOIN_REQUIRED; WP50-R01 CLOSED retained in its old fixed-input/static scope only')],
    new_formal_findings=0, business_executions=0,UPDATE_NOT_STARTED=True))

originals=[identity(p) for p in sorted(PRODUCER.rglob('*')) if p.is_file()]
inputs=[
    dict(identity=identity(ROOT/'inputs/eighth-global-review-prompt.md'), actual_read=[[1,125],[126,241]],disposition='FULL_READ'),
    dict(identity=identity(REPO/'AGENTS.md'),actual_read=[[1,297]],disposition='FULL_READ'),
    dict(identity=identity(ROOT/'inputs/review-SKILL.md'),actual_read=[[1,51]],disposition='FULL_READ; audit-output qualification only; no standalone revision performed'),
    dict(identity=identity(ROOT/'adjudication/root-item-operative-reception-progress.v1.json'),actual_read='whole',disposition='FULL_READ; existing root receptions reused, not relabeled source FULL'),
    dict(identity=identity(ROOT/'adjudication/mandatory-item-pinch-false-gluttony-meaning-qualification.v1.json'),actual_read='whole',disposition='FULL_READ; effective does-not-require Gluttony meaning applied'),
    dict(identity=identity(REPO/CAT1,REPO,B8),actual_read=[[1,8],[160,307]],operative_ranges=[[161,161],[189,268]],disposition='FINITE_READ; all45 applicable vectors plus complete shared premises; foreign actual read ranges do not transfer primary ownership'),
    dict(identity=identity(REPO/CAT2,REPO,B8),actual_read=[[1,103]],operative_ranges=[[1,3],[98,100]],disposition='FINITE_READ; I08 plus local context; no whole349-line approval'),
    dict(identity=identity(REPO/'deliverables/final-specification-set/test-catalog/combat-requirements-wp47-ab.md',REPO,B8),actual_read=[[98,114]],operative_ranges=[[98,109]],disposition='FINITE_N_CLIP_FULL; U04-NG01–04 controls and alias/caller/failure premises; other vectors remain foreign'),
    dict(identity=identity(REPO/MAIN,REPO,B8),actual_read=[[1,70],[74,181]],disposition='FINITE_READ; catalog contract and operative context only; no new wholeWP50 primary credit;73 and earlier truncated areas not filled by assumption'),
    dict(identity=identity(PRODUCER/'review.md'),actual_read='whole',disposition='FULL_READ; original current qualification'),
    dict(identity=identity(PRODUCER/'progress.json'),actual_read='whole',disposition='FULL_READ; original current qualification'),
    dict(identity=identity(PRODUCER/'reading-ledger.json'),actual_read=[[1,117]],disposition='FINITE_READ; original source/formal/catalog ranges; remaining administrative/foreign units unadopted'),
    dict(identity=identity(PRODUCER/'evidence/catalog-reception.json'),actual_read='Whole530-row object parsed mechanically; top-level schema/files/complete_lines/scope, disposition counts, and complete46 applicable path/line/id/disposition projection actually displayed',disposition='STRUCTURE_PARSED whole; finite46 metadata and full B8 clauses actually received; other484 retain foreign owner, no whole-row semantic read claimed'),
    dict(identity=identity(PRODUCER/'evidence/semantic-atoms.json.gz'),actual_read='premises3 whole;247 group IDs/196 handler IDs and necessary matching source/operative locators by index',disposition='FINITE_INDEX_AND_PREMISES_ONLY;698 source meanings not repeated or newly signed'),
    dict(identity=identity(PRODUCER/'evidence/finish_review.py'),actual_read=[[123,130]],disposition='STATIC_QUALIFICATION_RECIPE_ONLY; not executed; other search hits navigation only')
]
dump('identity-read-ledger.v1.json',dict(schema='gr8-item-catalog-schema-tail-identity-read-ledger/v1',utc=NOW,
    task='/root/item_catalog_schema_final_reception',state='CATALOG_FINITE_RECEIVED_SCHEMA_SUBREVIEW_PENDING',
    fixed=dict(B8=B8,workspace_tree='751dfde81048c81390f89a65ca1d1a565ba8e1ca',formal_tree='f292698cdd4a8e725525a9be6dc34b75faaf151e',R=R,R_tree='7589c800b61ba13a13040ed0d686979b80a84fd0'),
    local_head_observed='0aecad3442ffda46bdb025c76280da20df18ca56',
    local_head_qualification='Later review-only checkout; fixed B8 operands used for byte equality. No reset/index/commit/push performed.',
    configuration_requested=dict(model='gpt-6.1-sol',effort='ultra',tier='default',speed='normal',Fast=False),
    configuration_actual=dict(model='UNVERIFIED',effort='UNVERIFIED',tier='UNVERIFIED',speed='UNVERIFIED',Fast='UNVERIFIED',platform_task_id='UNVERIFIED'),
    inputs=inputs,producer_originals_preservation=originals,
    original_files=len(originals),original_bytes=sum(v['bytes'] for v in originals),
    tools_and_read_failures=[
        dict(kind='TRUNCATED_AGGREGATE_OUTPUT',qualification='Initial global-prompt aggregate and large catalog JSON output truncated; no whole-read credit. Prompt recovered by complete1–125/126–241 windows; catalog by complete applicability projection and actual full current46 rows/premises.'),
        dict(kind='TRUNCATED_WP50_AGGREGATE_OUTPUT',qualification='Combined producer qualification/WP50 output exceeded aggregate budget; only visible finite74–181 operative context retained,1–70 independently shown later;71–73 not claimed.'),
        dict(kind='WRONG_WORKDIR_PATH',qualification='Relative evidence searches from repo root returned not found, including one gzip open traceback; no semantics or identity granted. Correct report-root/absolute paths then used. A shell final successful command does not erase preceding Python failure.'),
        dict(kind='CODE_NAVIGATION_ONLY',qualification='rg hits in producer scripts locate original applicability logic only; producer scripts were never executed.')],
    business_execution=dict(reference=0,independent_model=0,native=0,game=0,save=0,fault_injection=0),
    not_claimed=['Full Item primary signoff','Root global signoff','R8 approval from WP50:179/181 old PASS/CLOSED','Whole foreign PBS868raw or six862-record selection rereview','Whole catalogs669 lines by this reviewer','Full semantic-atoms698 rereview','New business tests'],
    UPDATE_NOT_STARTED=True))
print(json.dumps(dict(vectors=len(rows),catalog_mapping_bytes=(OUT/'catalog-operative-complete-mapping.v1.json').stat().st_size,
                     original_files=len(originals),original_bytes=sum(v['bytes'] for v in originals)),ensure_ascii=False))
