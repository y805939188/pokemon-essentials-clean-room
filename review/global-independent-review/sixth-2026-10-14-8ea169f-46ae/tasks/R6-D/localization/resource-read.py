"""Read only the concrete localized image-path consumers selected by an audited search."""
import audit,json,re,sys
hits=[]
for line in (audit.OUT/'localized-resource-consumers.stdout').read_text().splitlines():
 m=re.match(r'^(.*\.rb):(\d+):(.*)$',line)
 if not m:raise ValueError('unrecognized search row')
 path,no,body=m.groups();no=int(no);p=audit.ROOT/path;ls=p.read_text(encoding='utf-8-sig').splitlines();k=re.search(r'_INTL\("([^"]*)"',body).group(1)
 hits.append({'key':k,'path':path,'line':no,'range':[max(1,no-3),min(len(ls),no+3)]})
audit.write('resource-consumers.json',hits)
a=int(sys.argv[1]);b=min(int(sys.argv[2]),len(hits)-1)
for i in range(a,b+1):
 h=hits[i];print('CONSUMER',i,h['key']);audit.read(h['path'],*h['range'])
audit.event('localized_resource_consumer_batch',hit_range=[a,b],total_hits=len(hits))
