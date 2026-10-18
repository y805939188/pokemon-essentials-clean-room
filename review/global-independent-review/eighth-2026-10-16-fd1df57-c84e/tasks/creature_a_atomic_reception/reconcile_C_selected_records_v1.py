from pathlib import Path
import json,re,hashlib,datetime,collections
A=Path(__file__).parent;C=A.parent/'creature_c_existing_crea';BASE=A.parents[1];R=Path('/workspace/pokemon-essentials');utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
def rd(p):return json.loads(p.read_text())
def wr(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def ident(p):
 r=p.read_bytes();return dict(path=str(p.relative_to(BASE)),bytes=len(r),sha256=hashlib.sha256(r).hexdigest())
o=A/'same-context-C-selected-record-inventory-joins.v1.json';assert not o.exists();pr=rd(C/'progress.json');iv=rd(A/'PBS-unread-record-inventory.json');idx={(f['path'],u['section']):u for f in iv['files']for u in f['units']};joins=collections.defaultdict(list);sourceids={};packets={};skiptemplates=[]
for n in[x['path']for x in pr['meaning_packages']]:
 d=rd(C/n)
 for key in['raw_complete_records','complete_raw_records']:
  for ordinal,u in enumerate(d.get(key,[])):
   sid=d['source_identities'][u['source_identity_key']];m=re.search(r'^\[([^]]+)\]',u['text'].lstrip('\ufeff'),re.M)
   if not m:skiptemplates.append(dict(package=n,record=u.get('id'),reason='Actualwhole semicolonfacilitytemplate separatefrom15filebracketinventory, no rawreadingdenied.'));continue
   t=(sid['path'],m.group(1))
   if t not in idx:continue
   real=(R/sid['path']).read_bytes();assert len(real)==sid['bytes'] and hashlib.sha256(real).hexdigest()==sid['sha256'];lines=real.decode('utf-8-sig').splitlines();assert '\n'.join(lines[u['range'][0]-1:u['range'][1]]).rstrip()==u['text'].lstrip('\ufeff').rstrip();sourceids[sid['path']]=sid;packets[n]=ident(C/n);joins[t].append(dict(package=n,pointer=f'/{key}/{ordinal}',complete_record_id=u.get('id',m.group(1)),range=u['range'],complete_raw_text_sha256=hashlib.sha256(u['text'].encode()).hexdigest(),actual_source_reader='/root/creature_a_atomic_reception',qualification='Previous actualcomplete ownraw reading in frozenCpacket. Thisjoin mechanicalidentitycheck adds0 source-readingcredit/independentreviewers.'))
assert len(joins)==160;already=sum(idx[k]['semantic_status']=='SELECTED_COMPLETE_RECORD_ACTUALLY_READ'for k in joins);assert already==4;newby=collections.Counter(k[0]for k in joins if idx[k]['semantic_status']!='SELECTED_COMPLETE_RECORD_ACTUALLY_READ');assert dict(newby)=={'PBS/pokemon_forms.txt':82,'PBS/pokemon.txt':74}
rows=[]
for (path,h),ps in sorted(joins.items()):
 x=idx[(path,h)];prior=x['semantic_status'];rows.append(dict(path=path,header=h,inventory_id=x['id'],previous_inventory_status=prior,complete_own_frozen_record_bindings=ps,meaning_status='COMPLETE_RAWVALUES_ACTUALLY_READ; onlyexplicitjoinedfield/consumer propositions accepted, no wholePBSortransitivePASS',already_read_before_this_join=prior=='SELECTED_COMPLETE_RECORD_ACTUALLY_READ'));x.update(semantic_status='SELECTED_COMPLETE_RECORD_ACTUALLY_READ',authority=str(o.relative_to(BASE)),actual_source_reader='/root/creature_a_atomic_reception',same_context_C_complete_record_bindings=ps)
iv.update(utc=utc,selected_complete_records_actually_read=sum(u['semantic_status']=='SELECTED_COMPLETE_RECORD_ACTUALLY_READ'for f in iv['files']for u in f['units']),available_unread_units=sum(u['semantic_status']=='AVAILABLE_NOT_YET_SEMANTICALLY_READ_OR_RECEIVED'for f in iv['files']for u in f['units']));assert iv['selected_complete_records_actually_read']==457;iv['qualification_current']='457uniqueactualselected15-fileinventory units: prior301 plus156 previouslyownreadC currentrecord identities nowreconciled(160matches/4overlap). Thisisledger reconciliation,0newsource reading; no allspecies/forms/metrics or wholealternativeapproval.'
out=dict(schema='gr8-crea-same-context-C-ownraw-inventory-joins/v1',recorded_utc=utc,actual_reader='/root/creature_a_atomic_reception',source_identities=sourceids,complete_frozen_packet_identities=packets,all160_complete_record_identity_joins=rows,inventory_newly_reconciled_records=156,already_read_inventory_overlap=4,new_by_path=dict(newby),inventory_selected_unique=457,inventory_remaining=iv['available_unread_units'],separate_facilitytemplate_navigation=skiptemplates,qualification='Rawsource output actuallyfullread previously in samecontext, allheaders/completeoriginalfieldvalues retainownreader. Thispostreading reconciliation doesnot claim157newreading/compile, allbase898/wholePBS; original31mixedrecord/templatepacket remainsitsowncount. Sourceids/sliceequality onlymechanical0semanticcredit.',new_contexts=0,new_votes=0,new_source_reading_credit=0,whole_domain_acceptance=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
wr(o,out);wr(A/'PBS-unread-record-inventory.json',iv);p=rd(A/'progress.json');p['updated_utc']=utc;p['current_unique_selected_15file_inventory']=457;p['same_context_C_prior_ownraw_inventory_reconciliation']=dict(**ident(o),matched_complete_records=160,newly_reconciled=156,overlap=4,new_reading_credit=0);wr(A/'progress.json',p)
g=rd(A/'coverage-gaps.json');g['recorded_utc']=utc
for x in g['gaps']:
 if x['id']=='CAA-GAP-PBS':x['selected_record_inventory_status']=dict(unique_actualselected=457,remaining=iv['available_unread_units'],reconciliation=ident(o),currentraw_meaning='Currentselectedbase/forms160completeownrecords finite;currentwhole898/339 andunreadvariants/metricsstillOPEN.')
wr(A/'coverage-gaps.json',g)
for p in[A/'review.md',C/'review.md']:
 with p.open('a')as f:f.write(f'\n\n{utc} Samecontext C→A priorownraw reconciliation:160completecurrentbase/form identities,4alreadyininventory/156newledgerjoins(74base82form). Unique15fileinventory457/remaining{iv["available_unread_units"]}. Thisis0newrawreading/0newvotes, rawwholefieldsalreadyread remain distinctfromwholePBS/consumersemanticacceptance. Threefacilitysemicolontemplates separatetracked, no1888cupcredit.\n')
print(json.dumps(dict(receipt=ident(o),newly_reconciled=156,unique=457,remaining=iv['available_unread_units'],new_reading_credit=0,utc=utc)))
