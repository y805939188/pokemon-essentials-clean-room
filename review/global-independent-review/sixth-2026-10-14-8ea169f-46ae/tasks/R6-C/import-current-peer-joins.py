import json,hashlib,datetime
from pathlib import Path
b=Path(__file__).parent;D='deliverables/final-specification-set/';pe=b.parent/'R6-O/cross-interface-C.json';o=json.loads(pe.read_text());facts={r['id']:r for r in o['facts']};joins=[]
def external(path,a,z,ids,assessment,source=None,owner='R6-O'):
 refs=[{'artifact':str(pe),'artifact_sha256':hashlib.sha256(pe.read_bytes()).hexdigest(),'fact_id':i,'source_owner':'R6-O','fact':facts[i]['fact'],'source_receipts':facts[i]['source']}for i in ids]
 units=[]
 for i in ids:
  for s in facts[i]['source']:
   units.append({'path':s['path'],'start':s['lines'][0],'end':s['lines'][1],'read_owner':'R6-O','ledger_receipt':{'path':s['ledger'],'lines':s['ledger_lines']}})
 units+=source or []
 joins.append({'path':D+path,'start':a,'end':z,'disposition':'CURRENT_OWNER_SOURCE_FACT_RECEIVED_C_REVERSE_CLAUSE_CHECKED','source_units':units,'external_fact_receipts':refs,'responsible_domain':owner,'semantic_assessment':assessment,'preconditions':'完整主formal C本轮已读；O原始完整源读与K音频原始完整源读按owner保留。只按该入口/配置/正常尾达到/有效数据条件；未知host限，不补统一回滚。','evidence':'R6-O_SOURCE_STATIC + R6-C_FORMAL_STATIC','aggregate_pass':False})
w39='combat-requirements/wp39-battle-context-and-participants.md';w42='combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md';w45='combat-requirements/wp45-weather-terrain-side-and-position-effects.md'
external(w39,49,74,['O-C-WILD-WRAPS'],'公众先生成、仅single+canOverride覆写；核心skip/startnotification/现成对象复用；双敌不走单敌覆盖；尾通知与bool结果不等核心数值。')
external(w39,76,103,['O-C-TRAINER-WRAPS','O-C-WILD-WRAPS'],'配对加载/输入形态/版本与缺资料重试、pair等待存与消费时点按具名源；合法作者输入和错误前缀分别，不以界面空队当准入skip。')
external(w39,105,114,['O-C-SKIP'],'zeroable/debugCtrl在创建前skip，wild1/trainerzero0、清规则和临时音频/encounter字段；不发正常start/end通知。')
external(w39,116,123,['O-C-RULES-PREPARE'],'伙伴noPartner/absent门先，之后enemy>1或显式nonsingle；合并引用列表与当前玩家列表共享程度独立，defaultdouble仅指定分支。')
external(w39,229,258,['O-C-RULES-PREPARE','O-C-ANIMATION-AUDIO-RESULT','O-C-AFTERMATH'],'一次规则与battle内rawrules别名/覆盖、环境/weather/terrain/背景/time、正常善后结果变量依次接合；异常保前缀无全局finally承诺。')
external(w39,295,296,['O-C-TRAINER-WRAPS','O-C-WILD-WRAPS'],'资料/未知species/越界level/悬挂配对按解析入口首错；匹配当前源strictguard及重试，未运行demo。')
external(w39,300,301,['O-C-TRAINER-WRAPS','O-C-WILD-WRAPS'],'waiting在未到tail时保留，普通return野生只2/5假、训练家只1真；override直接ret不再次布尔归一。')
external(w39,308,316,['O-C-RULES-PREPARE'],'设置来源与具名消费者比对：Storm/Fog标识terrain和weather类别映射不同，选项之后显式rules优先，伙伴全局字段不是敌数凭空生成。')
external(w42,205,259,['O-C-AFTERMATH','O-C-ANIMATION-AUDIO-RESULT'],'正常core返后unform/真实partner治疗/可败wait→endnotify/evo→Pickup/Honey或blackout→straighten；L0/K/D清在evo正常返回后；错误不保证尾清。')
external(w45,34,38,['O-C-RULES-PREPARE'],'explicit天气/terrain优先，terrain onlyStorm/Fog IDs，weather用类别；default setter -1无普通通知。C原core694–815消费者已全读。')
# K actual full BattleAudio149 receipt joins O actual normal callers; no claim C read the entire helper.
kpath=b.parent/'R6-K/forward-source-matrix.jsonl';ks=[json.loads(x)for x in kpath.read_text().splitlines()];k=next(q for q in ks if q.get('path','').endswith('003_Utilities_BattleAudio.rb'))
source=[{'path':k['path'],'start':1,'end':149,'read_owner':'R6-K','ledger_receipt':{'acquisition_log':k['acquisition_log'],'timestamp':k['timestamp']}}]
external(w39,260,277,['O-C-ANIMATION-AUDIO-RESULT'],'K新全BattleAudio helper149字节/层次和C各成功scene audio调用相接：野生/胜利/捕获预置独立，trainer数组最后非nil/empty区别，选择请求不证明实际播放，直接helper无已定位固定consumer保持原scope。',source,'R6-C/R6-O/R6-K')
(b/'peer-clause-joins.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in joins));print('O/K shared clausegroups',len(joins),'exactfact receipts',len(facts))
