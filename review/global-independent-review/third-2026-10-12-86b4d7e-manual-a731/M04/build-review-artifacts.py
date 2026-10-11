"""Assembles actual independent root review records; not a behavior implementation."""
from pathlib import Path
import json,csv,re,hashlib
OUT=Path(__file__).resolve().parent
ROOT=OUT.parent
REPO=OUT.parents[3]
source={x['path']:x for x in csv.DictReader((ROOT/'reference-file-inventory.tsv').open(),delimiter='\t')}
formal={x['path']:x for x in json.loads((ROOT/'formal-spec-identities.json').read_text())}
P='Data/Scripts/014_Pokemon/001_Pokemon.rb'
F='Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb'
SH='Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb'
SHO='Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb'
PC='Data/Scripts/016_UI/023_UI_PurifyChamber.rb'
MO='Data/Scripts/014_Pokemon/004_Pokemon_Move.rb'
OW='Data/Scripts/014_Pokemon/005_Pokemon_Owner.rb'
ME='Data/Scripts/014_Pokemon/002_Pokemon_MegaEvolution.rb'
SP='Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb'
TR='Data/Scripts/015_Trainers and player/003_Trainer_Sprites.rb'
paths=lambda *n:['deliverables/final-specification-set/'+x for x in n]
families=[
('身份/物种形态/默认字段',[P,OW,'Data/Scripts/010_Data/002_PBS data/008_Species.rb'],paths('creature-rpg/wp18-creature-identity-species-ownership.md'),'§2–4;CI01,25','基身份与形态内容分层；默认值数值/空表/空值/字符串不同；同物种设置不换形','SUPPORTED_STATIC','Species schema默认已由M01新独立读取和原限定证据支持；不推广缺资料PBS编译成功'),
('生成/随机/缓存返回态',[P,F],paths('creature-rpg/wp18-creature-identity-species-ownership.md','pokemon-rules/wp19-attributes-ability-and-stats.md'),'§4;CI02–06,26–28;ST38–44','六IV先各随机0..31，32位ID来自两个16位抽样；能力重算先缓存Nature；创建复检可额外抽形态且withMoves只控招式','SUPPORTED_STATIC','PRNG跨语言/实际播种与动态插件未知；FINAL1 A022旧邻接withMoves=false跳回调不复用，见reuse-qualification-corrections.json'),
('个体复制及引用独立/共享',[P,SH,OW],paths('creature-rpg/wp18-creature-identity-species-ownership.md','pokemon-rules/wp23-shadow-hyper-and-purification.md'),'§5;S03;CI10–13;SH41','IV/EV/moves/owner/ribbons独立，markings/fused/mail共享；Shadow暂存EV表仍共享；同身份与新建不同','SUPPORTED_STATIC','不扩为所有未知插件字段深复制，不强制源对象组织'),
('来源/拥有者/外来/命名',[P,OW],paths('creature-rpg/wp18-creature-identity-species-ownership.md'),'§6–7;CI14–24','四字段类型校验；训练家复制现值/外来语言默认2；id或名字不同外来；空/同物种名清昵称；时间整数秒','SUPPORTED_STATIC','获取/赠送/孵化/捕获完整入口各M05/M06/M11负责'),
('类型/性别与单性别',[P,'Data/Scripts/010_Data/001_Hardcoded data/002_GenderRatio.rb'],paths('pokemon-rules/wp19-attributes-ability-and-stats.md'),'§3.1–3.2;ST21–25,45','类型副本不限2；低8位严格小于女性阈值；单性别守卫先行/其它性别值忽略','SUPPORTED_STATIC','动态新增规则目录与任意坏数据非全组合证明'),
('普通/超级异色独立缓存',[P],paths('pokemon-rules/wp19-attributes-ability-and-stats.md'),'§3.3;ST28–33,41–44','32位两半异或阈值8/16与等0；独立首算/分别失效；写super真强shiny真、false不清','SUPPORTED_STATIC','源普通缓存与super可不满足数学蕴含，数据/宿主未运行'),
('特性索引/显式覆盖/回退',[P],paths('pokemon-rules/wp19-attributes-ability-and-stats.md'),'§3.4;ST26','自然0/1、隐藏>=2空位回低位但索引不改；负索引/无特性；未知覆盖忽略；简化形态不清缓存','SUPPORTED_STATIC','效果/触发另M08；当前数据未保证任何动态组合'),
('Nature完整顺序与25修正',[P,'Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb'],paths('pokemon-rules/wp19-attributes-ability-and-stats.md'),'§3.5;表N;ST27,39–40,49–50,60–63','固定25顺序/5中性/20修正，显示与计算覆盖分离；有覆盖时清显示不重算、不填回','SUPPORTED_STATIC','WP03固定身份前提内；任意插件修改目录数量未保证'),
('等级经验接口与错误边界',[P,'Data/Scripts/010_Data/001_Hardcoded data/001_GrowthRate.rb'],paths('pokemon-rules/wp19-attributes-ability-and-stats.md'),'§4;ST51','写等级域1..max/写经验清cache无通用夹限；满级展示0；非法等级返回错误对象与非法经验诊断名字失败不同','PARTIAL','GrowthRate完整曲线/收益由M06，M04按入口与精确历史语义复用'),
('IV/EV/上限标记与写入者层',[P,SH,'Data/Scripts/010_Data/001_Hardcoded data/008_Stat.rb'],paths('pokemon-rules/wp19-attributes-ability-and-stats.md'),'§5.1–5.3;ST46–48,52–59,64–67','原始IVvs31覆盖；培养252/510与设施255/255例外；存储不钳制、计算EV先整除4；统计/展示读原值','SUPPORTED_STATIC','设施创建及增量完整门由M05/M09，原始输入不存在项仍算术失败'),
('能力数学与HP差值写回',[P,'Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb'],paths('pokemon-rules/wp19-attributes-ability-and-stats.md'),'§5.4–5.6;ST01–20,54–55','EV/4→乘等级整除100→Nature再次整除；基础HP1例外；上限增量可复活濒死、存活最低1、最后HP钳','SUPPORTED_STATIC','合法整数数据静态公式，不以源表达式实现新框架；固定向量未执行'),
('HP/状态/计数与蛋守卫',[P,SH],paths('creature-rpg/wp20-hp-status-moves-helditem.md'),'§3–4;HP01–12','HP0先状态治疗但蛋保留状态/计数，准备flag恒清；Shadow超频叠清；状态不可用守卫先校验，设置不改计数','SUPPORTED_STATIC','战斗施加/尾转普通毒由M07；实际道具入口M05'),
('治疗逐入口/PP恢复',[P,MO,SH],paths('creature-rpg/wp20-hp-status-moves-helditem.md'),'§3.2;HP07–09','单HP不清状态；完整HP→状态→PP→清ready；蛋都早退；不清Shadow/Hyper/量表；PP越界失败','SUPPORTED_STATIC','储存治疗保ready与寄养/设施消费者另模块'),
('招式容量/顺序/静默学习',[P,MO],paths('creature-rpg/wp20-hp-status-moves-helditem.md'),'§5.1;HP13–15,35–39','零/五项整表允许；新招只移首一次；已知同对象移末；reset最新重复保留后取末4；负索引域','SUPPORTED_STATIC','正常UI非同一全局四槽保证；零招详情失败M10'),
('首招记录/兼容/重学',[P,'Data/Scripts/010_Data/002_PBS data/008_Species.rb'],paths('creature-rpg/wp20-hp-status-moves-helditem.md'),'§5.2–5.3;HP16–20,40–45','整记录保重复/次序，逐加入只阻本次重复；等级/记录可重学 vs 教授/等级/前身蛋招兼容不同','PARTIAL','TR双入口/重学UI门M05/M10，已读合同与历史证据；不代签全部消费者'),
('招式标识/PP/提升计数',[MO,P],paths('creature-rpg/wp20-hp-status-moves-helditem.md'),'§5.4–5.5;HP21–23,32–34','总PP=基础+整数20%每提升；换标识/计数后钳PP；极负计数写后区间逆失败PP旧值保留；战斗同步专门门','SUPPORTED_STATIC','非关联/变身只临时；未用弃用getter异常未扩为未来API要求'),
('持物/邮件/还原记录',[P],paths('creature-rpg/wp20-hp-status-moves-helditem.md'),'§6;HP24–31','持久未知设置忽略，战斗未知清空；邮件读取按当前物品失效；I可更新非原始快照；伙伴参与错位另链','PARTIAL','完整B013/捕获/效果链由M05/M06/M07/M08共同支持，M04局部不能签全链'),
('形态注册/复制/查询',[F],paths('pokemon-rules/wp21-dynamic-forms-and-display.md'),'§3.1;FM32','映射整份替换；复制时绑定共享处理器；源重注册不重绑目标；字符串不符号归一；条件当前0用例','SUPPORTED_STATIC','机制可用不证明真实插件组合'),
('全部读取型形态/锁定/时限',[P,F],paths('pokemon-rules/wp21-dynamic-forms-and-display.md'),'§3.2 A;§3.4;FM01–10,21','持物/能力/招式/性别/季节/地图/3与5天；锁定优先，battle/storage读取短路；不同值才动态提交','SUPPORTED_STATIC','系统时钟回拨/真实地图/插件未知'),
('创建/区域蛋随机与映射',[P,F],paths('pokemon-rules/wp21-dynamic-forms-and-display.md'),'§3.2 B/E;FM05–06,22;CI26–28','UNOWN28/南瓜100面/矿7..13/茶10%/63装饰/2流派等；地图地域需实际形态记录；0仍提交','SUPPORTED_STATIC','寄养遗传与启用由M06；不以注册数证明全部运行'),
('形态三提交入口及中断',[P,F],paths('pokemon-rules/wp21-dynamic-forms-and-display.md'),'§4.1;CI09;FM17,20','写形态→清特性→可让出→提交处理器→重算→图鉴；simple不清/不handler/dex；同值显式仍作用','SUPPORTED_STATIC','图鉴读取填性别/shiny；失败已有写入保留'),
('六物种改招完整映射/失败',[F,MO,'Data/Scripts/013_Items/001_Item_Utilities.rb'],paths('pokemon-rules/wp21-dynamic-forms-and-display.md'),'§4.2表F;FM13–20,36–43','ROTOM同值可删零/保底先后，KYUREM边删压缩跳项，NECROZMA旧超形态门，CALYREX后压缩，双犬终战还原','SUPPORTED_STATIC','学习先解析再蛋/Shadow拒；取消不回滚形态，运行演出未证'),
('战斗开始/入离/参战标志',[F,'Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb'],paths('pokemon-rules/wp21-dynamic-forms-and-display.md'),'§3.2 D;§4.3;FM11–12,42','起场/入场/离场19物种按wild/used/end/faint各门；形态取值与持久改招接点分开','PARTIAL','root实读注册，caller顺序主要由M07；默认标志和实际注册必须对应'),
('SPINDA图像修饰/精灵入口',[F,'Data/Scripts/010_Data/002_PBS data/009_Species_files.rb',SP],paths('pokemon-rules/wp21-dynamic-forms-and-display.md','engine-overworld/wp15-resource-matching-and-audio.md'),'§3.2 E','编号八4位组/四形状、双倍2×2采样、RGB夹限/重叠、非蛋正背逐帧；静态核心缺合同','PARTIAL','GR3-M04-001；真实Graphics/像素/越界宿主未知'),
('标记/缎带/华丽大赛记录',[P,'Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb'],paths('pokemon-rules/wp21-dynamic-forms-and-display.md'),'§5;FM23–35','标记缺值ACTION比较失败、仓库无清零；ribbon给去重/升级可重复/合法未拥有删除失败；美丽进化>=170','PARTIAL','记录/变更可得；UI资源变体与玩法比赛写入未证；M06/M10验证消费者'),
('Mega目标/身份/裸接口',[ME,F],paths('pokemon-rules/wp22-mega-and-primal-reversion.md','pokemon-rules/wp22-transformation-data.md'),'M01–04;ME01–10,26','按物种/来源form/石或已知招首匹配；无PP/有效物门；当前Mega读形态字段；解除读unmega','SUPPORTED_STATIC','48目标每条件/六数值已逐项对照，输入字段等价不证明编译或UI可达'),
('Mega训练家许可/次数/取消/提交',[ME,'Data/Scripts/011_Battle/001_Battle/008_Battle_ActionOther.rb'],paths('pokemon-rules/wp22-mega-and-primal-reversion.md'),'§4;ME07–18','真实业主资源/Transform/禁止→可达→野生→debug→后门；登记≠执行；持久再battle重复提交；HP差值非百分比','PARTIAL','精确既有限定复用+M07新源；M10 UI实审，Meta95HP保留'),
('Primal/解除与世界设施边界',[ME,F],paths('pokemon-rules/wp22-mega-and-primal-reversion.md'),'§5–6;ME19–25','两宝珠，无环/次数；入场前伤害可早退；无宝珠人工1不被query视Primal故裸解除不回0；裸/世界/设施收尾不同','SUPPORTED_STATIC','正常门与坏状态区别；世界/设施联合审，无新统一互斥架构'),
('Shadow建立/阶段/复制',[SH],paths('pokemon-rules/wp23-shadow-hyper-and-purification.md'),'§2–3;SH01–04,41','重建非幂等S/V重0/G=M；query未赋/false保留；阶段ceil5G/M；负G改变Shadow资格；V共享','SUPPORTED_STATIC','131可选数据字段全文匹配但未启用'),
('Shadow招式候选/保留/恢复',[SH,SHO],paths('pokemon-rules/wp23-shadow-hyper-and-purification.md'),'§4;SH08–10,50','先有效shadow池至4；缺SHADOWRUSH不新增；原招跳前k/阶段后缀；保既有对象/PP顺序后补；净化才恢复全','SUPPORTED_STATIC','battle招式不由香自动同步；类型/内容不默认启用'),
('Hyper资格/概率/有效vs存储',[SH,SHO,'Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb'],paths('pokemon-rules/wp23-shadow-hyper-and-purification.md'),'§5;SH11–16,42','正G含端点1001/4000；G0普通rand0浮点写真但有效假；20%服从全局随机/回合后伤24，旧初始化下标门','PARTIAL','M07战斗整链与随机/回放不同输入，当前默认有界结论不扩跨宿主'),
('Shadow成长/EV暂存/恢复',[SH,SHO,'Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb'],paths('pokemon-rules/wp23-shadow-hyper-and-purification.md'),'§6;SH17–24,43–45','阶段<=3且V存在暂存；H4/5普通EV；收益余量不计S；净化4/5整数折算、逐项EV余量，S缺跳重算','PARTIAL','收益全公式M06/M07；已读root净化提交/窗口失败callback不存在，保持部分提交边界'),
('香/时间之笛/遗迹石入口门',[SHO,SH],paths('pokemon-rules/wp23-shadow-hyper-and-purification.md'),'§7;SH25–28,47–52','h255+G0拒、254可成功；Nature存储非mint；香缺Scent前门；TIMEFLUTE成功消费却净化早退；LUGIA外门/选择门不同','SUPPORTED_STATIC','源异常已有准确合同，不重复新finding；普通道具外层由M05'),
('净化室编成/移动/接收/取消',[PC,SHO,'Data/Scripts/013_Items/001_Item_Utilities.rb'],paths('pokemon-rules/wp23-shadow-hyper-and-purification.md'),'§8.1/8.3;SH33–46','9组4外圈共享成员，rawshadow替换；盒满队空取出仍清源；净化跨级先缺update失败，S0到存放双满仍清源','SUPPORTED_STATIC','root读PC1–630领域/controller及helper；真实Storage选人/演出由M10；normal与直接位置分层'),
('净化室亲和/三角数/流量/步进',[PC,SHO],paths('pokemon-rules/wp23-shadow-hyper-and-purification.md','pokemon-rules/wp23-shadow-data-and-vectors.md'),'§8.2;SH29–32','ANY类型对有利，Normal自对特例，T=n(n+1)/2+E最大14，F=E+C+floor(n/2)，Lugia九组恰14；正G才扣，不换招','SUPPORTED_STATIC','独立数学静态；源注释额外bestcircle不当规则，事件Demo0'),
('九个体/训练家图像helper',[SP,TR],paths('engine-overworld/wp15-resource-matching-and-audio.md','user-interface/wp66-a-party-and-summary-ui.md'),'资源/图标呈现交界','精灵换图/原点九方向；图标0.25/0.5/1秒按HP档、濒死首帧；selected偏移；训练家4frame0.5/box0.4','PARTIAL','来源辅助参数已读，M10 UI及M03资源主体；缺Graphics/字体实际渲染与帧节奏未知'),
]
rows=[]
for i,(name,sources,specs,clauses,behavior,status,limits) in enumerate(families,1):
    rows.append(dict(capability_id=f'M04-C{i:03}',module='M04',category='Creature-RPG / Pokémon Rules / Combat Requirements / Engine/UI integration',capability=name,source_paths=';'.join(sources),source_loci='固定完整主源或指定caller范围，实际阅读按file-coverage',spec_paths=';'.join(specs),spec_clauses=clauses,test_design=clauses+';全部NOT_EXECUTED',normal_failure_boundary=behavior,status=status,limitations=limits))
def tsv(path,rows):
    with path.open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
tsv(OUT/'capability-coverage.tsv',rows)
assigned=json.loads((OUT/'assigned-files.json').read_text());assigned_set={x['path'] for x in assigned}
file_rows=[]
allpaths=sorted(assigned_set|{p for x in rows for p in x['source_paths'].split(';')}|{'PBS/pokemon_forms.txt','PBS/pokemon.txt','PBS/items.txt'}|{f'PBS/Shadow Pokémon backup/{x}' for x in ['shadow_pokemon.txt','moves_shadow_pkmn.txt','items_shadow_pkmn.txt','types_shadow_pkmn.txt']})
for p in allpaths:
    rel=[x for x in rows if p in x['source_paths'].split(';')]
    scope='FULL_TEXT_READ' if p in assigned_set or 'Shadow Pokémon backup/' in p or p.endswith('/009_Nature.rb') or p.endswith('/002_GenderRatio.rb') or p.endswith('/008_Stat.rb') else 'TARGETED_CALLER_OR_DATA_FIELD_READ; exact qualified historical/new M01/M07 independent evidence reused where stated'
    if p==PC:scope='lines1–630 domain/controller/helper full; later scene only targeted; M10 owns full UI'
    if p.startswith('PBS/pokemon'):scope='Mega48 and matched base identities/fields only; not full species/forms semantics'
    if p=='PBS/items.txt':scope='Mega ring/stone/orb valid identities and item samples, not full content semantics'
    file_rows.append(dict(source_path=p,git_blob=source[p]['git_blob'],category='Pokémon/Creature/Combat/Engine/UI',read_scope=scope,status='SUPPORTED_STATIC' if p in assigned_set and p not in [SP,TR] else 'PARTIAL',capability_ids=';'.join(x['capability_id'] for x in rel),limitations='Actual source range not runtime; cross-domain whole consumers/host/resource not promoted.'))
tsv(OUT/'file-coverage.tsv',file_rows)
specrows=[]
for ident in json.loads((OUT/'assigned-specs.json').read_text()):
    p=ident['path'];name=Path(p).name;txt=(REPO/p).read_text();rel=[x for x in rows if p in x['spec_paths'].split(';')]
    if '/test-catalog/' in p:rel=rows
    for lineno,line in enumerate(txt.splitlines(),1):
        table=line.startswith('| ') and not line.startswith('| ---')
        if not (line.startswith('#') or table):continue
        clause=f'line{lineno} '+(line.split('|')[1].strip() if table else line.lstrip('#').strip())
        status='SUPPORTED_STATIC';limit='已读当前条款/表行与对应静态入口；未执行案例/宿主/资源。'
        if '未决' in clause or '未验证' in clause:status='UNRESOLVED';limit='具名原未知/动态/宿主/事件资源，不由本轮静态读取解除。'
        if '/test-catalog/' in p and table:
            token=line.split('|')[1].strip()
            owned=token.startswith(('CI','HP','ST','FM','ME','SH'))
            if 'pokemon-rules-wp19' in p and token.startswith('BR'):owned=False
            if not owned:status='PARTIAL';limit='其它领域正文/案例由M05/M06/M10等责任模块；M04不单签。'
        if 'wp21-' in name and ('其它' in clause or '图像修饰' in clause):status='PARTIAL';limit='GR3-M04-001 斑点数学与形状未提供；真实媒体仍未知。'
        if '/wp22-transformation-data' in p or '/wp23-shadow-data' in p:limit='逐行静态字段对照见data-field-equivalence.json；固定参考可读不证明实际编译/启用。'
        specrows.append(dict(spec_path=p,clause=clause,source_paths=';'.join(sorted({s for x in rel for s in x['source_paths'].split(';')})),source_loci='相关完整固定主源/注册表及精确caller范围；行为细分见capability-coverage.tsv',status=status,test_design='原具名系列/向量;NOT_EXECUTED',limitations=limit))
tsv(OUT/'spec-coverage.tsv',specrows)
f1path='review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/all229-dispositions.json'
f1=json.loads((REPO/f1path).read_text());index={x['id']:(i,x) for i,x in enumerate(f1['records'])}
controls=json.loads((OUT/'regression-controls.json').read_text())
records=[]
cross={'GIR-FD82-A036','GIR-FD82-A037','GIR-FD82-A044','GIR-FD82-A053','GIR-FD82-B013','GIR-FD82-B032','GIR-FD82-C124','GIR-FD82-C126'}
for x in controls:
    id=x['id'];i,h=index[id];basis=h.get('normal_reverse_partial_failure_review',h.get('normal_reverse_partial_failure',{'normal':h.get('normal_static_judgment'),'reverse':h.get('reverse_and_neighbor_static_judgment'),'partial':h.get('partial_failure_and_specific_limits')}))
    records.append(dict(id=id,reviewer='/root',status='PARTIAL' if id in cross else 'SUPPORTED_STATIC',actual_read_scope='完整approved有效资格/反例/minimum/recheck/root+extension字段，完整相应FINAL语义字段与身份；当前M04正式条款/数据/案例+主源，各跨域消费者单独责任不代签',historical_reuse={'commit':'c2bc1a341ba6acdf7c8c111dc88d39a162a093d6','path':f1path,'pointer':f'/records/{i}','record_sha256':hashlib.sha256(json.dumps(h,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'basis':'131正式字节/必要历史全身份一致；有效前提不变，当前source/formal另核；不转授旧签名'},historical_semantic_scope=basis,explicit_reuse_exclusions=['FINAL1 A022 neighboring_reverse的withMoves=false跳创建回调表述不复用；source与当前CI03明确只控制招式'] if id=='GIR-FD82-A022' else [],current_spec_paths=[x['path'] for x in json.loads((OUT/'assigned-specs.json').read_text())],new_finding_relations=[],execution='NOT_EXECUTED',limitations='跨owner/host/resource/动态组合保留；原229状态未修改'))
(OUT/'regression-review.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
correction={'kind':'QUALIFIED_EVIDENCE_REUSE_EXCLUSION_NOT_HISTORICAL_REWRITE_OR_REOPEN','id':'OBS-REG-A022-WITHMOVES','reviewer':'/root','historical_commit':'c2bc1a341ba6acdf7c8c111dc88d39a162a093d6','historical_path':f1path,'historical_pointer':f'/records/{index["GIR-FD82-A022"][0]}/normal_reverse_partial_failure_review/neighboring_reverse','historical_claim':'withMoves=false或已有非零形态跳该创建回调','actual_source_and_current_contract':'withMoves=false仅跳招式初始化/重置；创建回调只受形态0及recheck_form门。当前WP18 §4.1和CI03已准确明确形态仍提交。','source_commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','source_path':P,'source_loci':'creation tail actual callback and reset_moves guards','policy':'保留旧完整对象和原CLOSED，不复用该错误邻接句；原A022有效要求由正确source/正式条款/其余完整独立证据支持。不是正式规格新缺口，不新增canonical必修。'}
(OUT/'reuse-qualification-corrections.json').write_text(json.dumps(correction,ensure_ascii=False,indent=2)+'\n')
(OUT/'junction-review.md').write_text('''# M04个体规则交界审查

独立root；固定身份见baseline/各finding/矩阵。源与静态场景执行0。

| 链 | 正常 | 失败/边界 | 判定 |
|---|---|---|---|
| 内容→创建→形态→统计/图鉴 | 直接记录默认与PBS验证分开；性格能力重算先缓存；形态0复检可再抽，0仍提交 | withMoves=false不挡form回调，只挡moves；recheck关闭或非零初形态不调用；图鉴读取可先填gender/shiny | SUPPORTED_STATIC；A022旧FINAL邻接误句不复用 |
| IV/EV/Nature→能力→HP | 先EV整除4再等级再Nature；HP1特例；HP差值保持伤量 | 减上限存活最低1，濒死增上限会复活；存储255设施例外不被计算/禁用正规化 | SUPPORTED_STATIC；设施全创建由M09 |
| 形态提交→学习/UI→字段 | 先form/cache，再handler，再stats/dex；直改保槽/up并钳PP | ROTOM同值删空、KYUREM边压缩跳项、学习取消不回滚form；解析缺招先失败 | SUPPORTED_STATIC；M10真实UI另核 |
| 持物/捕获→伙伴/队伍→终局 | I为可更新记录，部分消耗写穿，无伙伴同步可保持正确 | 实际伙伴参与集合与满队移位player列表分离时旧送盒成员被写后继物；M04不能用普通消耗单签全捕获 | PARTIAL待M05/M06/M07/M08 root整合，原B013范围保留 |
| Shadow→步/战斗→Hyper/招式 | Nature储存表、256步和chamber每步不同；有效状态与存储flag分开 | G0可写Hyper提示但query假；香缺Flags常规拒，笛成功消费却净化早退；已有准确合同无重复新ID | SUPPORTED_STATIC局部；M06/M07/M11完整消费者 |
| 净化→EV/EXP→等级窗口→接收 | S0同等级可越窗口，普通Math F/T与九组14门可计算 | 跨级chamber屏无update首窗口失败，先S/V/Shadow/level已提交；遗迹石有空callback；到达存放后双满仍清源 | SUPPORTED_STATIC源链；完整储存选择UI及媒体M10 |
| 编号→精灵→帧 | 非蛋有效资源copy后逐帧施四斑点；正背皆可，纯species入口不同 | 静态位置/形状/2×2采样/两组RGB缺最终合同；越界和真实位图未知 | PARTIAL，GR3-M04-001；M03/M10交界 |

缎带缺持有删除、TIMEFLUTE、零招模型、Primal还原术语等定点候选已与完整允许集核对；已有准确条款时不再新增finding。未用getter/任意插件/语义外输入不被虚构成当前默认能力通过。
''')
(OUT/'report.md').write_text(f'''# M04 个体与基础规则独立评审

COMPLETED_STATIC_WITH_LIMITS。新独立root /root，主会话codex://threads/01a12bbf-9300-7833-82d7-d392ae9fa731；未参与被冻结作者或登记。请求gpt-6.1-sol/ultra/Standard，回显UNVERIFIED。主9源完整实读；另补Nature全25、GenderRatio/Stat、PurifyChamber1–630、物种图像消费者、学习/等级辅助关键段与数据目录；10份分配正式行为正文/附表及两测试目录所辖CI/HP/ST/FM/ME/SH全部案例实读，其余BR/PT/PS/AQ为其它模块，不单签。源/运行/静态案例执行0。

独立分母{len(rows)}个行为族；文件{len(file_rows)}记录、反向条款/表行/案例{len(specrows)}记录。计数只作导航，正常失败边界见capability-coverage和junction。身份/状态缓存、数学、三形态入口、Mega/Primal、Shadow建立/成长/净化及部分提交主体可独立实现；新增P2 GR3-M04-001：SPINDA斑点静态数学/形状和帧/入口合同缺失。真实Graphics/宿主像素仍未知，不以缺素材抹掉可得规则。

48Mega每条条件/6值与正式表逐项匹配；131可选Shadow每量表/有序招匹配，18效果身份/4物品/1类型文本已完整读，见data-field-equivalence。仅静态字段，不安装/编译/启用备份、不声称全pokemon/forms/metrics语义。完整21历史控制有效资格、反例、最低修订及复核和相应FINAL语义按固定身份消费；8项跨owner只在M04层支持。发现历史FINAL A022邻接误句withMoves=false跳回调，当前源/正式CI03正确，因此明确排除该句复用并保留旧完整对象/原CLOSED，不新添正式必修、不改历史签名，见reuse-qualification-corrections。

已有TIMEFLUTE前后门错配、缎带合法未拥有删除失败、ROTOM零招、Hyper G0、Shadow复制V共享、净化跨级缺callback等合同准确，不因源历史异常重复提新ID。历史bug是否未来兼容由用户决定；不能改参考来凑理想行为。

源类/字段容器仅取证，规则以独立数学、状态和场景审查；没有框架实现/源翻译/新API设计。模型、源/规格身份与保全见baseline。余下跨module交界由root在全12模块收口；本模块完成不等于游戏/全内容/资源/动态/运行PASS。
''')
print(json.dumps({'module':'M04','families':len(rows),'file_records':len(file_rows),'spec_records':len(specrows),'legacy_controls':len(records),'new_findings':1,'runtime_and_cases':0}))
