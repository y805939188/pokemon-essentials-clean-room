"""Materialize this reviewer's already-read semantic notes and finite static checks.
The script confers no reading credit and never executes reference behavior.
"""
from pathlib import Path
import datetime, hashlib, json, re, subprocess
from capture import capture
OUT=Path(__file__).resolve().parent
S=Path('/workspace/pokemon-essentials-clean-room')
R=Path('/workspace/pokemon-essentials')
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BT='751dfde81048c81390f89a65ca1d1a565ba8e1ca'
RT='7589c800b61ba13a13040ed0d686979b80a84fd0'
REVIEWER='/root/com_move/attributes_calling'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z')
MP='deliverables/final-specification-set/combat-requirements/wp47-a-move-attributes-targeting-and-calling.md'
DP='deliverables/final-specification-set/combat-requirements/wp47-a-attributes-targeting-calling-data.md'
CP='deliverables/final-specification-set/test-catalog/combat-requirements-wp47-ab.md'
M='Data/Scripts/011_Battle/003_Move/'
BB='Data/Scripts/011_Battle/002_Battler/'
OTHER='Data/Scripts/011_Battle/007_Other battle code/'
source_names=['008_MoveEffects_MoveAttributes.rb','012_MoveEffects_ChangeMoveEffect.rb']
def dump(name,o): (OUT/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def git(repo,*args): return subprocess.check_output(['git','-C',str(repo),*args]).decode().strip()
payloads={}
def identity(repo,p,commit):
    k=('R:' if repo==R else 'B8:')+p
    if k in payloads:return k
    b=(repo/p).read_bytes()
    fixed=subprocess.check_output(['git','-C',str(repo),'show',f'{commit}:{p}'])
    payloads[k]={'id':k,'repo':str(repo),'path':p,'commit':commit,'tree':RT if repo==R else BT,
        'formal_tree':'f292698cdd4a8e725525a9be6dc34b75faaf151e' if p.startswith('deliverables/') else None,
        'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':git(repo,'rev-parse',f'{commit}:{p}'),
        'mode':git(repo,'ls-tree',commit,'--',p).split()[0],
        'actual_matches_fixed_bytes':b==fixed,'actual_blob':git(repo,'hash-object',str(repo/p))}
    if b!=fixed:raise RuntimeError(f'Identity conflict {k}')
    return k
def ref(p,a,b):return {'payload':identity(R,p,RC),'lines':[a,min(b,len((R/p).read_text().splitlines()))]}
groups={
'FACTORY':([ref(M+'001_Battle_Move.rb',1,247),ref('Data/Scripts/014_Pokemon/004_Pokemon_Move.rb',1,77),ref('Data/Scripts/010_Data/002_PBS data/005_Move.rb',1,408)],'合法效果名按登记效果构造；不存在实现进入Unimplemented，非法常量名仍可能异常。个体招式新建PPUp0/满PP，战斗临时PP可另设−1。GameData层display只返回数据类型/威力/分类/准确率，注释中的动态分支不运行；战斗Move层仅AuraWheel在MORPEKO原物种或变身物种记录成立时活动返回pbBaseType，其余type与damage/category/accuracy委托个体招式的数据层。'),
'TYPE':([ref(M+'007_MoveEffects_BattlerOther.rb',659,934),ref(BB+'003_Battler_ChangeSelf.rb',129,151),ref(BB+'001_Battle_Battler.rb',303,337),ref(BB+'001_Battle_Battler.rb',491,516)],'普通改类型读未压制前的原能力身份；当前基础/额外类型和燃尽/羽栖是场上态。单类型写入与复制对象的规范化不同，新增额外类型仅单字段覆盖。每个招式有自己的存在性/重复/候选资格。'),
'RAW':([ref(M+'006_MoveEffects_BattlerStats.rb',1846,1894),ref(BB+'001_Battle_Battler.rb',81,110),ref(BB+'002_Battler_Initialize.rb',70,127),ref(BB+'002_Battler_Initialize.rb',285,302),ref(BB+'009_Battler_UseMoveSuccessChecks.rb',303,525)],'四原能力操作直接提交场上原值，阶级/HP/持久个体字段不随写；WonderRoom只交换防御getter，setter名称不变。接力对新成员原记录重施PowerTrick，普通刷新重新取持久能力，变身刷新有守卫。替身属公共变化招资格，速度互换专属绕过。'),
'PARAM':([ref(M+'008_MoveEffects_MoveAttributes.rb',1222,1620),ref(M+'003_Move_UsageCalculations.rb',1,520),ref(BB+'007_Battler_UseMove.rb',193,253),ref(M+'013_MoveEffects_SwitchingActing.rb',669,680)],'本次类型先计算，局部基底类型覆盖与之后电覆盖分开；伤害基底逐击可重查当前持物/环境。觉醒力量排序/旧代位值、17/17/4持物表、天气/场地接地门均保持实际快照。'),
'NG':([ref(M+'008_MoveEffects_MoveAttributes.rb',1338,1380),ref(BB+'007_Battler_UseMove.rb',367,429),ref(BB+'007_Battler_UseMove.rb',583,760),ref(M+'003_Move_UsageCalculations.rb',228,280),ref(BB+'010_Battler_UseMoveTriggerEffects.rb',1,218),ref(BB+'006_Battler_AbilityAndItem.rb',212,323),ref(OTHER+'009_Battle_ItemEffects.rb',364,388),ref(OTHER+'009_Battle_ItemEffects.rb',1311,1333),ref(BB+'001_Battle_Battler.rb',663,690),ref(BB+'001_Battle_Battler.rb',421,449)],'NaturalGift整招门只查有效树果和前缀；首击后JABO反伤可触发U普通ORAN食用，C写穿清持物，等同I才清，R/P写实际物且Belch真。下一击普通critical后先访问空item.id失败；已有首击/HP/物品/PP前缀不回滚。高HP保果、单击与现有坏标志分别是不同正常对照。'),
'ENV':([ref(M+'012_MoveEffects_ChangeMoveEffect.rb',224,333),ref(M+'012_MoveEffects_ChangeMoveEffect.rb',861,918),ref(M+'003_Move_UsageCalculations.rb',487,520)],'Camouflage、NaturePower和SecretPower拥有不同目的与回退。NaturePower场地分支缺招保TRIATTACK不查环境；SecretPower起用记录附效后所有击后抽一次，畏缩声明与实际分支集合不同，精神动画拼写保留。'),
'PROTECT':([ref(M+'008_MoveEffects_MoveAttributes.rb',634,1032),ref(M+'008_MoveEffects_MoveAttributes.rb',1222,1272),ref(M+'004_Move_BaseEffects.rb',436,491),ref(M+'002_Move_Usage.rb',106,126),ref(BB+'009_Battler_UseMoveSuccessChecks.rb',303,581),ref(M+'012_MoveEffects_ChangeMoveEffect.rb',360,447),ref('Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb',711,750)],'保护先查对应标志、适用倍率抽签再最后行动；失败倍率1，成功当前×3旧×2。公共目标门按可保护/分类及UNSEENFIST原接触决定挡招，实际接触/护具/中央资格决定反应。锁定在逐击层较早放行，不越过目标保护。'),
'MISC':([ref(M+'005_MoveEffects_Misc.rb',1,44)],'庆祝仅区分野生名字/业主名字反馈；牵手无存活盟友则失败；跃起重力不能选用，主效仅无事发生反馈。'),
'TARGET':([ref(BB+'008_Battler_UseMoveTargeting.rb',1,203),ref(BB+'007_Battler_UseMove.rb',249,429),ref(M+'012_MoveEffects_ChangeMoveEffect.rb',1,39),ref(M+'012_MoveEffects_ChangeMoveEffect.rb',140,219),ref(M+'012_MoveEffects_ChangeMoveEffect.rb',340,354),ref('Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb',1,222)],'执行目标构造和重定向各查本次动态类别；User通常空逐目标列表；资格使用类别num_targets/targets_foe而非实际人数。重定向先位置/开关守卫再龙箭扩展，再抗重定向能力，随后Spotlight/FollowMe/属性吸引。PROTEAN后期诅咒重建不再调用重定向。'),
'CALL':([ref(M+'012_MoveEffects_ChangeMoveEffect.rb',694,1226),ref(BB+'007_Battler_UseMove.rb',1,762),ref(BB+'008_Battler_UseMoveTargeting.rb',1,203),ref(BB+'009_Battler_UseMoveSuccessChecks.rb',1,595),ref('Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb',1,301),ref(OTHER+'006_Battle_Clauses.rb',1,306)],'临时调用slot−1/PP−1/special真与accuracy-skip分离；未越过选择/目标/半无敌等前门。候选为各自精确名单/标志和目标约定。内层会改历史/行动标志且异常无通用恢复。反射复用招式且只直接一击；抢夺接管者改变但原PP已扣。后装规则另可影响目标资格。'),
'COPY':([ref(M+'012_MoveEffects_ChangeMoveEffect.rb',1232,1330),ref(BB+'003_Battler_ChangeSelf.rb',104,124),ref(BB+'003_Battler_ChangeSelf.rb',179,188),ref('Data/Scripts/014_Pokemon/004_Pokemon_Move.rb',1,77)],'模仿/写生均先检查变身/本槽/目标最近普通招/重复/名单/Shadow，再第一槽写。模仿仅临时槽，写生先持久槽后临时，PP和PPUp来自新建；显示/形态检查在写后，复制不即用。'),
'DATA':([], '附表精确身份数据经过本轮逐行阅读，与源明列数组和当前PBS标志、注册类型对照；成员资格只覆盖明列集合，不授予整个调用成功或运行结果。')}
for path in sorted((R/'PBS').rglob('*.txt')):
    if path.name in ['moves.txt','items.txt','types.txt','moves_shadow_pkmn.txt','items_shadow_pkmn.txt','types_shadow_pkmn.txt']:
        groups['DATA'][0].append(ref(str(path.relative_to(R)),1,len(path.read_text(encoding='utf-8-sig').splitlines())))
# Preserve exact raw bytes of already semantically read primary/formal/caller files.
full_deps=[M+'001_Battle_Move.rb',BB+'007_Battler_UseMove.rb',BB+'008_Battler_UseMoveTargeting.rb',BB+'009_Battler_UseMoveSuccessChecks.rb',BB+'010_Battler_UseMoveTriggerEffects.rb',M+'003_Move_UsageCalculations.rb','Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb','Data/Scripts/010_Data/002_PBS data/003_Type.rb','Data/Scripts/010_Data/002_PBS data/005_Move.rb','Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb','Data/Scripts/014_Pokemon/004_Pokemon_Move.rb',OTHER+'006_Battle_Clauses.rb']
for i,p in enumerate([M+x for x in source_names]+full_deps): capture(f'bound-source-{i:02d}',['cat',str(R/p)])
for i,p in enumerate([MP,DP,CP]):
    identity(S,p,B8)
    capture(f'bound-formal-{i:02d}',['cat',str(S/p)])
for p in ['AGENTS.md','review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/eighth-global-review-prompt.md','review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/review-SKILL.md']:
    b=(S/p).read_bytes()
    payloads['INPUT:'+p]={'repo':str(S),'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'kind':'instruction','read':'FULL_READ'}
unit_notes={}
for l in (OUT/'unit-facts.tsv').read_text().splitlines():
    n,c,f=l.split('\t');unit_notes[n]=(c,f)
units=[]
for f in source_names:
    p=M+f;ls=(R/p).read_text().splitlines()
    starts=[]
    for i,l in enumerate(ls,1):
        m=re.match(r'^class Battle::Move::(\w+)|^def (pbHiddenPower)',l)
        if m: starts.append((i,m[1] or m[2]))
    for ix,(a,n) in enumerate(starts):
        b=starts[ix+1][0]-1 if ix+1<len(starts) else len(ls)
        contract,fact=unit_notes[n]
        mainlocal='WP47-A' in contract
        group='CALL' if (f.startswith('012') and a>=694 and a<1232) else 'COPY' if a>=1232 and f.startswith('012') else 'PARAM' if f.startswith('008') and a>=1277 else 'PROTECT' if mainlocal else 'TARGET' if a<40 and f.startswith('012') else 'ENV' if n=='EffectDependsOnEnvironment' else 'CALL'
        consumers=[{'path':BB+'007_Battler_UseMove.rb','lines':[154,578],'meaning':'构造/前门/初始历史/目标/起用/击次与后段'}, {'path':BB+'007_Battler_UseMove.rb','lines':[583,760],'meaning':'实际每击求值、HP提交、触发、主要效果/附效顺序'}]
        if 'WP46' in contract or 'WP43' in contract: consumers.append({'path':M+'003_Move_UsageCalculations.rb','lines':[228,520],'meaning':'分类、威力/攻防参数、普通伤害/附效消费者'})
        units.append({'id':'RUNIT:'+n,'reviewer':REVIEWER,'source':ref(p,a,b),'definition':n,'main_contract':contract,'fact':fact,
          'premise':'对象与所需数据合法并到达具名钩子；共同资格/后装覆盖不可由原定义绕过。','consumer_chain':consumers,
          'source_status':'FULL_READ','evidence_level':'SOURCE_STATIC','execution':'NOT_EXECUTED',
          'reception_owner':REVIEWER if mainlocal else '/root/com_move','reception_status':'LOCAL_SOURCE_AND_FORMAL_CHECKED' if mainlocal else 'SUBMITTED_TO_PARENT_NOT_YET_RECEIPTED',
          'negative_boundary':'未执行宿主、未证无界插件组合；原始定义与后装Clauses按事实分列。'})
# All primary formal paragraphs/table rows were manually decomposed below.
main_lines=(S/MP).read_text().splitlines()
breaks={}
for l in (OUT/'main-breakdown.tsv').read_text().splitlines():
    n,gs,atoms=l.split('\t');breaks[int(n)]=(gs.split(','),atoms.split(';'))
reverse=[]
def assertion(doc,line,text,gs,seq=1,reason=None):
    evidence=[]
    for g in gs:
        refs,body=groups[g]
        evidence.append({'group':g,'facts':body,'source_locations':refs})
    o={'id':f'{doc}:L{line:03d}:A{seq:02d}','formal':{'payload':identity(S,doc,B8),'line':line},'formal_full_context':(S/doc).read_text().splitlines()[line-1],'assertion':text,
       'reviewer':REVIEWER,'support':'SUPPORTED_SOURCE_STATIC','evidence_level':'SOURCE_STATIC','execution':'NOT_EXECUTED',
       'source_facts':evidence,'justification':reason or '在所述有限前提下，定义的资格、读值、写点及已实读中央消费者一致；该子断言不扩为宿主执行或其它输入保证。'}
    reverse.append(o);return o
for line,(gs,atoms) in breaks.items():
    for i,t in enumerate(atoms,1): assertion(MP,line,t,gs,i)
administrative=[]
for i,l in enumerate(main_lines,1):
    if not l.strip() or i in breaks:continue
    structural=l.startswith('#') or l.strip()=='---' or l.startswith('| ---') or l.startswith('| 身份') or l.startswith('| 效果') or l.startswith('| 目标') or l.startswith('| 静态')
    administrative.append({'formal':MP,'line':i,'text':l,'disposition':'SECTION_OR_TABLE_STRUCTURE' if structural else 'NAVIGATION_AND_EVIDENCE_BOUNDARY_READ',
      'reason':'章节/表头无额外行为断言。' if structural else '分类、净化来源/审计导航/证据等级声明已读；历史接受和全仓导航由root核，本分片不授历史PASS。'})
data_lines=(S/DP).read_text().splitlines()
call_names=['UseLastMoveUsed','UseMoveTargetIsAboutToUse','UseRandomMove','UseRandomMoveFromUserParty','UseRandomUserMoveIfAsleep','ReplaceMoveThisBattleWithTargetLastMoveUsed','ReplaceMoveWithTargetLastMoveUsed']
source12=(R/M/source_names[1]).read_text()
def blacklist(n):
    m=re.search(r'^class Battle::Move::'+n+r'\b.*?(?=^class Battle::Move::|\Z)',source12,re.M|re.S)
    text=m[0]
    m2=re.search(r'@moveBlacklist = \[(.*?)\n    \]',text,re.S)
    base=set(re.findall(r'^\s*"(\w+)"',m2[1],re.M))
    add=set()
    ma=re.search(r'@moveBlacklist \+= \[(.*?)\n      \]',text,re.S)
    if ma:add=set(re.findall(r'^\s*"(\w+)"',ma[1],re.M))
    return base,add
bl={n:blacklist(n) for n in call_names}
matrix=[];berry_rows=[];held_rows=[]
for i,l in enumerate(data_lines,1):
    if re.match(r'\| [A-Za-z0-9]+ \|',l):
        cells=[c.strip() for c in l.strip('|').split('|')]
        if 13<=i<=75:
            effect=cells[0]
            for j,(n,cell) in enumerate(zip(call_names,cells[1:])):
                base,add=bl[n]
                actual='常' if effect in base else '≥6' if effect in add else '—'
                matrix.append({'line':i,'effect':effect,'entry':n,'asserted':cell,'actual':actual,'equal':cell==actual})
                assertion(DP,i,f'{effect} 在 {n} 的明列排除资格为 {cell}（其它资格保持）。',['CALL','DATA'],j+1,
                    '已逐列实读具名初始化名单，当前单元将精确字符串及世代追加分别比对；破折号仅表示该名单未排除。')
        elif 87<=i<=124:
            held_rows.append(cells)
            assertion(DP,i,f'{cells[0]}: 有效持物 {cells[1]} 对应存在时类型 {cells[2]}。',['PARAM','DATA'],1,'源明列映射与数据行一一相等；有效持物和目的类型存在性是行为层条件。')
        elif 132<=i<=198:
            berry_rows.append(cells)
            assertion(DP,i,f'当前默认 {cells[0]} 的完整NaturalGift类型/威力为 {cells[1]}/{cells[2]}。',['NG','DATA'],1,'已读当前及备选标志：此行仅当前默认内容；不是整招锁定快照、不是备选自动启用或食果效果定义。')
for n,atoms in {
5:['附表为当前净化正文','全部静态无运行确认'],9:['常表示所有代明列排除','≥6表示仅新代追加','—不等于无条件允许','按效果字符串不是显示名/父族'],
77:['逐列常/增量数量41+2/9+0/45+0/41+16/30+0/5+0/2+0','额外候选过滤仍独立'],
79:['Reduce与Set怨念字符串不同','MeteorBeam未明列不补排','未知效果不保证通用递归终止'],83:['有效持物且目的类型存在才映射','其它退NORMAL'],
128:['全部当前完整NaturalGift标志按数据原顺序读取','资格仍要求有效树果','缺完整匹配现有物品可P1','空物品身份访问先失败','ORAN首击反应可自耗','表不锁定整招快照','67身份不因向量增减'],
200:['67条默认标志','至少10夹限仍适用','数据不是源程序逐行翻译'],204:['本包效果59项包含四原能力操作'],
208:['PowerTrick/SpeedSwap/PowerSplit/GuardSplit默认身份','四原值操作主合同2.1','阶级/持久/空间/刷新/接力边界保留'],
212:['12侧状态/保护/等离子浴身份WP45唯一主责','本包不重复定义新门'],
214:['WP46伤害/恢复身份不重复计入本包','WP44状态/阶级有其它primary','类型9项在本包','能力/浮空/变身招式归WP47-B','持久形态/Shadow归WP22/23','SwitchingActing青草优先级归本包','被动物品WP50','WP79未据此判完成']}.items():
    for j,a in enumerate(atoms,1): assertion(DP,n,a,['DATA','CALL','PARAM'] if n not in [128,200] else ['NG','DATA'],j)
line206=data_lines[205]
for j,n in enumerate(re.findall(r'\b[A-Z][A-Za-z0-9]+\b',line206),1):
    if n in unit_notes or n in ['DoesNothingCongratulations','DoesNothingFailsIfNoAlly','DoesNothingUnusableInGravity','SetUserTypesBasedOnEnvironment','SetUserTypesToResistLastAttack','SetUserTypesToTargetTypes','SetUserTypesToUserMoveType','SetTargetTypesToPsychic','SetTargetTypesToWater','AddGhostTypeToTarget','AddGrassTypeToTarget','UserLosesFireType','HigherPriorityInGrassyTerrain']:
        assertion(DP,206,f'效果身份 {n} 由本包相应主合同接收。',['TYPE','RAW','PARAM','CALL','PROTECT','TARGET'],j)
for i,l in enumerate(data_lines,1):
    if not l.strip():continue
    if not any(x['formal']['payload']=='B8:'+DP and x['formal']['line']==i for x in reverse):
        administrative.append({'formal':DP,'line':i,'text':l,'disposition':'SECTION_TABLE_OR_NAVIGATION_READ','reason':'表头、章节、空白分隔或不新增行为的本包导航；有效正文已在独立子断言表。'})
# Catalog: all 108 vector rows read; 52 are this primary, 56 have other primary.
vector_explanations={
'MA-A01':('TYPE','首槽门在循环内先break；≥6不会因首槽无候选继续找后槽，旧代会。'),
'MA-A02':('TYPE','ExtraType只有一个写点，草直接覆盖幽灵，非新增列表。'),
'MA-A03':('TYPE','canChangeType直接检查原ability_id，胃液仅影响active门。'),
'MA-A04':('TYPE','AfterAllHits没有unaffected守卫，保护后仍被逐目标调用，BurnUp条件只看自身标志。'),
'MA-A05':('PARAM','s=0/63端点经N=17索引0/16；QMARKS伪类排，FAIRY存在且末位。'),
'MA-A06':('PARAM','旧位从60开始，第二位仅HP/攻击能补1/2，整数算出68/68/69/70。'),
'MA-A07':('PARAM','类型场地分支无接地门；基底明确affectedByTerrain才倍增。'),
'MA-A08':('PARAM','强风不是None故基底倍增，类型case无强风分支故NORMAL；天气被压为None则不倍增。'),
'MA-A09':('NG','保护只让目标unaffected；外壳继续AfterMove，未换出的U结束钩子有物即消费且belch=false。'),
'MA-A10':('ENV','附效定义位于AfterAllHits而非AdditionalEffect；洞穴记录7实际畏缩，但flinchingMove声明集合无7。'),
'MA-T01':('TARGET','预选倒下使中央addTarget失败，然后随机近盟友；仅一候选概率1，无候选保空。'),
'MA-T02':('TARGET','User目标数据num_targets0，默认无逐目标；允许空集进入全局效果，所以恢复可执行。'),
'MA-T03':('TARGET','strength初100且仅严格变小者替换，2优先4，等值保速度序先见，SkyDrop先跳。'),
'MA-T04':('TARGET','能力吸引扫描U盟友且不查MoldBreaker；后继ImmunityByAbility另因MoldBreaker早返。'),
'MA-T05':('TARGET','pbModifyTargets在STALWART返回前；早先扩出的第二目标不会被删除。'),
'MA-T06':('CALL','先Snatch1且遍历包含自己，自己值等于当前强度触发+1成为2；消费不要求1。'),
'MA-P01':('PROTECT','固定0抽签通过后仍检查其它存活未行动UseMove/Shift，空则失败复位1。'),
'MA-P02':('PROTECT','KingShield挡伤害分支已进入；实际接触/资格允许时当前代降1，≤7降2。'),
'MA-P03':('PROTECT','共同目标保护检查在逐击LockOn返回之前，标unaffected不会到锁定成功层。'),
'MA-C01':('CALL','Copycat计数阶段缓存battle.lastMoveUsed，随后才把全局改自己，调用缓存X。'),
'MA-C02':('CALL','Assist逐个招式条目push无去重，三条目均匀，X两个槽占2/3。'),
'MA-C03':('CALL','≥6仅排空/自己索引/蛋，没排倒下非蛋；其招式仍过其它名单过滤。'),
'MA-C04':('CALL','Battle选择sleepTalk真绕PP0，调用无槽新temporaryPP−1，原候选PP无写入；外壳普通扣PP已完成。'),
'MA-C05':('CALL','1000次有界逐抽只从当前抽中身份决定，无合格回退；全部拒本次失败。'),
'MA-C06':('CALL','MeFirst候选只查伤害类及名单，内层pbCanChooseMove因healingMove和HealBlock拒；pbUseMove返回后清MeFirst，无PP退款。'),
'MA-C07':('COPY','外壳先用realMove写穿扣PP；Mimic新temporary不替换个体槽，Sketch先替换个体槽；新建PPUp0满PP；无立即调用。'),
'MA-C08':('CALL','七族名单按精确函数码，Reduce条目不会匹配Set；标志和其它名单独立。'),
'MA-C09':('ENV','Electric已进入case，不会执行else环境；缺THUNDERBOLT保初始TRIATTACK，默认缺失留查找异常风险。'),
'MA-C10':('CALL','两明列名单无MeteorBeam升特攻效果，不能由父族或注释排除；实际其它选择门仍保留。'),
'MA-T07':('TARGET','初始Ghost动态单敌方，先固定3再FollowMe改1；Curse目标写咒后扣floor101/2=50。'),
'MA-T08':('TARGET','清唯一FollowMe且其它吸引无后，初抽3不重抽，仍3；其余扣血顺序不变。'),
'MA-T09':('TARGET','AllNearFoes类别num_targets2使can_target_one_foe=false，即使列表1也在重定向守卫返回。'),
'MA-T10':('TARGET','非Ghost初始User空列表不重定向；global分支先速度−1后攻击+1、防御+1，无咒或扣血。'),
'MA-T11':('TARGET','普通PP/历史先写，初始User空；PROTEAN后清选择重建随机3但不重定向；目标门后3写咒扣50。'),
'MA-T12':('TARGET','起始Ghost最初已经动态单敌方并正常重定向1；没有后期类型变更分支，PP4/HP51。'),
'MA-T13':('TARGET','移除PROTEAN不变Ghost；User空集仍进入general，三阶级顺序且HP101。'),
'MA-T14':('TARGET','非Ghost三请求都不可变使whole-move门早失败，在PROTEAN前；PP/历史已提交但类型/HP不写。'),
'MA-T15':('TARGET','初门非Ghost通过后改Ghost重建3；3已有咒在目标门拒；无重新FollowMe和无HP代价，PP/类型保留。'),
'MA-T16':('TARGET','target.Curse写点先于ReduceHP，夹在两者的异常保留前咒/PP/类型，未到HP写点保持101；晚异常则HP51保留。')}
for n in range(1,5): vector_explanations[f'U04-NG{n:02d}']=('NG',groups['NG'][1]+' 四个独立变化：主例失败/高HP保果/无亲子爱单击/现有坏标志分别按主稿3.1.1区分，不把静态推导写成运行。')
raw_reasons={1:'正常无空间两次直接交换100/60↔60/100，旗标逐次反转。',2:'速度专属绕替身交换50/100，阶级无写点。',3:'攻floor201/2=100、特攻floor303/2=151，两端相同。',4:'无空间防floor201/2=100、特防floor303/2=151。',5:'普通变化招替身共同门在effect前拒；共同有效穿透是单独绕过。',6:'WonderRoom getter防=原特防80，而setter写原防，第二次不会恢复100/60/80。',7:'先读203/101和100/100，写原防151/原特防100，getter再交换。',8:'Baton在新初始化原attack120/defense70上直接交换，非旧值copy且不借空间getter。',9:'pbUpdate非Transform从持久个体覆盖5原值，Transform跳过；普通换入另初始化。'}
for n,r in raw_reasons.items(): vector_explanations[f'R5-U04-RAW{n:02d}']=('RAW',r)
vectors=[];section=''
for line,l in enumerate((S/CP).read_text().splitlines(),1):
    if l.startswith('## '):section=l
    if not l.startswith('| '):continue
    cells=[c.strip() for c in l.strip('|').split('|')]
    if len(cells)!=3 or cells[0] in ['ID','---']:continue
    short=cells[0]
    if short[0:1] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':continue
    key=('MA-'+short if section.startswith('## MA') else 'SB-'+short if section.startswith('## SB') else short)
    if short.startswith('MA-') or short.startswith('SB-'):key=short
    primary=key in vector_explanations
    g,why=vector_explanations.get(key,('CALL','共享目录本行完整阅读；属WP47-B或WP46的另一个primary，已向父审者提交接口，未以本分片阅读授予其正式语义接收。'))
    row={'id':key,'catalog_line':line,'input':cells[1],'expected':cells[2],'primary':primary,
         'reviewer':REVIEWER,'owner':REVIEWER if primary else '/root/com_move/switching_control or /root/com_move (WP46)',
         'check':why,'source_facts':{'group':g,'facts':groups[g][1],'locations':groups[g][0]},
         'support':'SUPPORTED_DERIVED_VECTOR' if primary else 'READ_OTHER_PRIMARY_RECEPTION_OPEN','evidence_level':'DERIVED_VECTOR','execution':'NOT_EXECUTED'}
    vectors.append(row)
    if primary:
        # Semicolon/sentence boundaries here preserve the already-read original
        # natural-language subassertions and are reviewed with the explicit reason.
        atoms=[x.strip() for x in re.split('[；。]',cells[2]) if x.strip()]
        for j,a in enumerate(atoms,1):assertion(CP,line,a,[g],j,why)
for u in units:
    matching=[r['id'] for r in reverse if u['definition'] in r['assertion']]
    u['reverse_consumers']=matching
    u['formal_locator']=MP+' '+u['main_contract'] if 'WP47-A' in u['main_contract'] else '父审者负责 '+u['main_contract']+' 对应完整正文/向量接收'
assert all(x['equal'] for x in matrix),[x for x in matrix if not x['equal']]
assert len(units)==125
assert len([x for x in vectors if x['primary']])==52
assert len(held_rows)==38 and len(berry_rows)==67
dump('identities.json',{'reviewer':REVIEWER,'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','fast':False},'actual':dict.fromkeys(['model','effort','tier','fast','platform_agent_id'],'UNVERIFIED'),
    'fixed':{'B8':B8,'B8_tree':BT,'formal_tree':'f292698cdd4a8e725525a9be6dc34b75faaf151e','R':RC,'R_tree':RT},
    'observed_HEAD':git(S,'rev-parse','HEAD'),'observed_formal_tree':git(S,'rev-parse','HEAD:deliverables/final-specification-set'),
    'observed_R_HEAD':git(R,'rev-parse','HEAD'),'path_mapping':{'cloud_spec':str(S),'cloud_reference':str(R),'Mac_historical_paths':'合同内历史位置，未当云端实际路径'},'payloads':list(payloads.values()),'observed_utc':NOW})
ledger=[{'payload':identity(R,M+f,RC),'status':'FULL_READ','continuous_intervals':[[1,len((R/M/f).read_text().splitlines())]],'reviewer':REVIEWER,'unit_ids':[u['id'] for u in units if u['source']['payload']=='R:'+M+f],'unread_intervals':[]} for f in source_names]
for p in [MP,DP,CP]:ledger.append({'payload':identity(S,p,B8),'status':'FULL_READ','continuous_intervals':[[1,len((S/p).read_text().splitlines())]],'reviewer':REVIEWER,'unread_intervals':[],'primary':p!=CP,'shared_catalog_primary_vectors':52 if p==CP else None,'shared_catalog_other_primary_read':56 if p==CP else None})
for p in full_deps:ledger.append({'payload':identity(R,p,RC),'status':'FULL_READ_DEPENDENCY','continuous_intervals':[[1,len((R/p).read_text().splitlines())]],'reviewer':REVIEWER,'semantic_scope':'本分片涉及的完整定义/控制流，未接受整个依赖域正式合同。'})
full_set={x['payload'] for x in ledger}
for g,(refs,body) in groups.items():
    for rr in refs:
        if rr['payload'] in full_set:continue
        ledger.append({'payload':rr['payload'],'status':'RELEVANT_UNITS_FULL_READ' if not payloads[rr['payload']]['path'].startswith('PBS/') else 'RELEVANT_FIELDS_READ',
          'continuous_intervals':[rr['lines']],'reviewer':REVIEWER,'semantic_scope':g,'facts':body,
          'boundary':'未声明未列单元全文审查；PBS相关记录身份/功能码/类型/分类/威力/命中/目标/优先级/标志已读，其余名称/价格/描述/总PP未依此投影授予语义信用，由全域PBS主责。' if payloads[rr['payload']]['path'].startswith('PBS/') else '有限定义链，文件其它单元由原primary负责。'})
dump('reading-ledger.json',{'reviewer':REVIEWER,'read_credit_basis':'本轮工具输出逐连续区间/完整单元实读；脚本只保存/核身份/算计数，不授阅读信用。','primary_source_files':2,'primary_source_units':125,'primary_formal_files':2,'shared_formal_files_full_read':1,'shared_vectors_total':len(vectors),'primary_vectors':52,'other_primary_vectors_read':len(vectors)-52,'primary_unread_source_units':0,'primary_unread_formal_units':0,'primary_unread_vectors':0,'pending_reception_interfaces':3,'payloads':ledger,'formal_structure_dispositions':administrative,
    'pbs_evidence':{'raw':'evidence/pbs-records.stdout','semantic_projection':'evidence/pbs-semantics.txt','semantic_projection_read_intervals':[[1,420],[421,850],[851,1280],[1281,1700],[1701,1900]],'not_full_pbs_domain_credit':True},
    'original_io':{'earlier_tool_outputs':'平台functions.exec chunk原输出，未倒填时间/底层exit；后续同固定字节重捕保存在evidence/bound-source-*及bound-formal-*。','early_chunks':['b2278b','0f2b92','1b50c3','3e5c33','2e21b6','ebc9fe','73db03','d3d73f','483f24','d23ab0','4184dd','fc4fc1','cdfc8f','f77ffa','206964','fc8ec8','d9fc6e','b07c05','575e59','6685ab','c59fd4','15ac45','398692'],'new_commands':'evidence/commands.jsonl'}})
dump('forward-mapping.json',{'reviewer':REVIEWER,'evidence_level':'SOURCE_STATIC','units':units,'source_groups':{k:{'facts':v[1],'locations':v[0]} for k,v in groups.items()},'callback_boundaries':'实际handler为已读有限ORAN/JABO/属性吸引与后装规则；其它完整能力/物品域依赖最终接收仍OPEN。'})
dump('reverse-mapping.json',{'reviewer':REVIEWER,'assertion_count':len(reverse),'assertions':reverse,'vectors':vectors,'data_checks':{'blacklist_cells':matrix,'held_mapping_rows':held_rows,'natural_gift_rows':berry_rows},'administrative_dispositions':administrative,'formal_missing_breakdown_lines':[i for i,l in enumerate(main_lines,1) if l.strip() and i not in breaks and not any(a['formal']==MP and a['line']==i for a in administrative)]})
interfaces=[
 {'id':'ATTR-CORE','producer':REVIEWER,'receiver':'/root/combat_review','state':'OPEN_FINAL_RECEPTION','read_own_source':True,'facts':'普通/特殊使用两个标志、历史/PP写点、目标/全局空集、反射单击/抢夺接管、击后/结束时点已逐完整方法核。后期PROTEAN诅咒只重建不重定向；参考不能从外壳成功显示推inner成功。','source_groups':['CALL','TARGET','PROTECT'],'remaining':'具名中央主责对本有限结果最终接收，未缺读本分片必要caller。'},
 {'id':'ATTR-BATTLER','producer':REVIEWER,'receiver':'COM-BATTLER final primary UNVERIFIED; integration /root/com_move','state':'OPEN_FINAL_RECEPTION','read_own_source':True,'facts':'raw能力getter/setter/WonderRoom、类型current/extra/燃尽/羽栖、刷新/接力、持物写穿与各记录已有限追读。类型变更不修改持久物种；原值操作不修改阶级/持久能力。','source_groups':['TYPE','RAW','NG'],'remaining':'全Battler域最终接收不由本分片局部阅读替代。'},
 {'id':'ATTR-ABILITY-ITEM','producer':REVIEWER,'receiver':'COM-ABILITY-ITEM final primary UNVERIFIED; integration /root/com_move','state':'OPEN_FINAL_RECEPTION','read_own_source':True,'facts':'NaturalGift经JABO→U即时HP检查→ORAN消费→下一击空物身份失败，正常高HP/单击/坏标志对照；LightningRod/StormDrain重定向与moldbreaker免疫分层。','source_groups':['NG','TARGET'],'remaining':'其它handler组合/整个WP48/49/50正式域最终接收OPEN。'},
 {'id':'ATTR-DAMAGE-RECEPTION','producer':REVIEWER,'receiver':'/root/com_move','state':'SUBMITTED','facts':'008/012中所有WP43/45/46定义逐类facts完整。原OHKOIce冰拒被后装Clauses继承alias覆盖，准确率修正仍保留；两个fixed20/40均用sonicboomclause。','unit_ids':[u['id'] for u in units if 'WP47-A' not in u['main_contract']]},
 {'id':'ATTR-AI','producer':REVIEWER,'receiver':'/root/com_ai','state':'SENT_AWAIT_RECEIPT','facts':'已发125逐项facts位置及NG每次空身份首次失败、实际OHKOIce后装与AI独立冰门差异。纯读AI预测不可冒充实际反应链。','source_groups':['NG','PARAM']},
 {'id':'ATTR-SHARED-CATALOG','producer':REVIEWER,'receiver':'/root/com_move/switching_control and /root/com_move(WP46)','state':'READ_OTHER_PRIMARY','facts':'共享catalog全165行108向量均已读，52为本主责；其余56不重复给本分片primary接收。'}]
dump('interfaces.json',{'reviewer':REVIEWER,'interfaces':interfaces,'blocking_pending_final_reception':3,'nonblocking_submitted':[x['id'] for x in interfaces[3:]]})
dump('proposals.json',{'reviewer':REVIEWER,'proposals':[],'required':0,'optional':0,'no_required_classification_records':0,'policy_records':[],'decision_status':'NO_NEW_PROPOSAL_IN_FINITE_PRIMARY; global裁决由root','independent_refutation':'无提案待独立反证；不得以此声明全部系统NO_REQUIRED_UPDATE。','negative_checks':[
  {'claim':'精确调用排除表','result':'441格/世代资格经真实名单对照，无差异；表有本来拼写不匹配的正确保留。','evidence':'reverse-mapping.json:data_checks.blacklist_cells'},
  {'claim':'类型/威力共同快照','result':'正文已明确不同求值时点；NG自耗续击失败被覆盖；未构成新gap。','evidence':'forward NG / vectors U04-NG01..04'},
  {'claim':'诅咒动态/后期目标','result':'正文及MA-T07..T16已正确区分初始重定向与PROTEAN后期只重建；PP/历史/类型/咒/HP写序一致。','evidence':'TARGET source full caller'},
  {'claim':'原值两用恢复','result':'正文及RAW06已明确WonderRoom反例；接力用原记录重施与刷新丢失边界保留。','evidence':'RAW'},
  {'claim':'无条件强断言','result':'保护、半无敌、额外能力/物品门、内层PP/历史副作用均有限明确；未用观察缺失臆造运行结果。','evidence':'CALL/PROTECT'}],
  'execution':'NOT_EXECUTED','update_status':'UPDATE_NOT_STARTED'})
progress=json.loads((OUT/'progress.json').read_text());progress.update({'state':'COMPLETED','semantic_reception':'OPEN_FOR_THREE_CROSS_DOMAIN_INTERFACES','updated_utc':NOW,'end_utc':NOW,'start_utc':None,'first_observed_utc':'2026-10-16T03:22:56Z','start_utc_qualification':'精确平台启动UTC未回显，不倒填；首条clock见first_observed_utc。','counts':{'source_files':2,'source_units':125,'source_unread':0,'primary_formal_files':2,'shared_catalog_files':1,'primary_vectors':52,'shared_other_primary_read':56,'primary_unread_vectors':0,'formal_assertions':len(reverse),'proposals':0,'required':0,'open_final_reception_interfaces':3}});dump('progress.json',progress)
report=f'''# COM-MOVE 属性、目标与调用有限分片审查

审者 `{REVIEWER}`。本轮完整合同36653字节、AGENTS与指定review-SKILL均全文读取；本交付是审计记录，不修正式规格。固定B8 `{B8}`，R `{RC}`；当前工作HEAD为报告后继，正式目录树仍固定 `f292698cdd4a8e725525a9be6dc34b75faaf151e`，所有登记payload实际字节逐个与固定Git对象相同。云端路径与合同Mac历史路径分列。

两主参考文件连续完整读取共2950行：008的92类及独立HiddenPower函数共93结构、012的32类，共125结构，每个有具体自然语言事实、资格/数值/写点/消费者（unit-facts.tsv、forward-mapping.json）。两份WP47-A正文/数据全文共435行；共享catalog全文165行，108个向量均读，本分片独占52个（原MA29、MA-T07–T16十个、NG四个、RAW九个），另外56个保留WP47-B/WP46主责。主范围未读源结构0、未读正式单位0、未读主责向量0。反向拆出{len(reverse)}条具前提/根事实/消费者的子断言，黑名单{len(matrix)}格逐项核对，持物类型38行、NaturalGift67行。分句/脚本核数不代替上述本轮语义阅读。

007_Battler_UseMove、008_Targeting、009_SuccessChecks、010_TriggerEffects、003_UsageCalculations、ActionAttacksPriority、Move/Type/Target数据定义、Pokemon::Move和后装Clauses均全文实读；其它类型、原能力值、物品记录、刷新/接力、ORAN/JABO处理器按完整相关定义追读。完整source身份、精确区间和有效边界见reading-ledger与identities。PBS恢复包含默认和Gen5/6/7/8、Shadow备选；相关记录的运行选择字段完整投影1900行分五连续块实读，原完整记录4781行保存。名称/价格/描述/总PP等未依此投影授全PBS全文信用；全域PBS接收仍属其primary，不把备选自动启用。

当前有限主责未形成新提案。重要正反校验：NaturalGift主例首击/JABO/ORAN提交后下一击空身份访问异常，与高HP/单击/现有坏标志对照均和正文一致；初始Ghost诅咒重定向、PROTEAN后期只重建及失败前缀均已明确；原能力值的WonderRoom读写和Baton重施已保留；精确排除串、千次挥指抽取、抢夺自增与模仿/写生PP均一致。后装Clauses导致OHKOIce原冰拒被继承alias覆盖，本分片已实际读该覆盖并同步父审者/AI；它是父审者告知已有WP43/46合同的接合事实，本分片未新立重复根因。GameData层活动display返原数据；Battle::Move层保留AuraWheel合格MORPEKO的动态类型专例，其余注释内动态算法不授执行信用，已同步WP43父审者。

COM-CORE、COM-BATTLER、COM-ABILITY-ITEM三项最终跨域接收仍OPEN（本分片必要源链已读），另向父审者提交WP43/45/46事实、向COM-AI发送有限预测/实际行为接合；这些状态不改标limit，也不冒称全系统完成。所有本轮行为执行0，证据只有SOURCE_STATIC/DERIVED_VECTOR；工具身份/计数检查另列TOOL_VALIDATION，向量全部NOT_EXECUTED。没有宿主画面/音频/存档/异常恢复/无限插件组合认证。

请求gpt-6.1-sol / ultra / default普速 / Fast off；实际model、effort、tier、Fast、平台agent ID均未回显，逐字段UNVERIFIED。平台逻辑入口已知；精确平台启动UTC未回显，首个实测UTC为03:22:56Z，最终更新时间{NOW}。前期原I/O保存在平台chunk，后续完整重捕及stdout/stderr/底层exit/UTC在evidence/commands.jsonl，失败路径检索及cat保留非0退出，无倒填。

交付progress、identities、reading-ledger、forward-mapping、reverse-mapping、interfaces、proposals、review；辅助逐类事实和逐条款人工拆分保留供父审者复核。唯一写集为当前分片目录。没有formal/reference/planning/audit修改，没有commit/push，没有安装或行为运行。UPDATE_NOT_STARTED。
'''
(OUT/'review.md').write_text(report)
print(json.dumps({'units':len(units),'formal_assertions':len(reverse),'primary_vectors':52,'catalog_vectors':len(vectors),'blacklist_cells':len(matrix),'pending_final_reception':3,'report':str(OUT/'review.md')},ensure_ascii=False))
