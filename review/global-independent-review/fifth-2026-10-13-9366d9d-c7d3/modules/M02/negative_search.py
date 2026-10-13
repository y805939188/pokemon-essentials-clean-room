from pathlib import Path
import re,json
P=Path(__file__).parent
queries={
 'persistent_stores':r'Game_(?:Variables|Switches|SelfSwitches)|pbGet\b|pbSet\b|变量.{0,12}(?:nil|false|空值)|自开关.{0,16}(?:严格|布尔)|ID ≤ 5000',
 'conditional_lifecycle':r'HandlerHashSymbol|addIf|条件.{0,12}(?:撤销|移除|删除|清空)|(?:移除|清空).{0,12}(?:处理器|条件)',
 'archive_stream':r'StringInput|FileInputMixin|FileOutputMixin|fgetdw|pbRgssOpen|字符串流|内存流|SEEK_END|EOF|流.{0,6}(?:游标|定位|关闭|末尾)',
 'legacy_berry_mapping':r'v20_fix_planted_berry|berry_conversion|mulch_conversion|旧.{0,8}树果.{0,8}(?:映射|迁移)|数字.{0,8}(?:树果|敷料)|6/7/8|389.{0,20}CHERI',
 'critical_completion':r'关键段|pbCriticalCode|mainFunction|普通异常.{0,16}(?:结束|返回|终止)|包装.{0,12}返回.{0,4}[01]',
 'misc_utilities':r'深合并|递归合并|温度|华氏|摄氏|上下文.{0,8}回调|回调.{0,8}上下文|每会话|会话平均|双参数随机|Kernel.rand'
}
root=Path('deliverables/final-specification-set')
res={'schema_version':'gr5.review.v1','specification_baseline':'9366d9d17aaeac3b4414236468affa650fb3dd27','method':'read-only text search; match inventory is not semantic review; semantic read ranges listed in finding negative_evidence_search and spec-to-source','queries':[]}
for key,pat in queries.items():
 hits=[]
 for f in sorted(root.rglob('*.md')):
  for i,t in enumerate(f.read_text().splitlines(),1):
   if re.search(pat,t,re.I):hits.append({'path':str(f),'line':i,'matched_text':t})
 res['queries'].append({'id':key,'pattern':pat,'scope':str(root)+'/**/*.md','matches':hits})
 print(key,[(x['path'].split('/')[-1],x['line']) for x in hits])
(P/'negative-search.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
