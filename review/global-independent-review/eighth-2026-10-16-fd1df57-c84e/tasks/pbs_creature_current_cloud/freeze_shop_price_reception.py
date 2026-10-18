from pathlib import Path
import json, datetime, hashlib, subprocess

P=Path(__file__).resolve().parent
R=Path('/workspace/pokemon-essentials')
C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
UTC=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
Q=P.parent/'creature_b'
def meta(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
f=json.loads((Q/'dependency-semantic-facts.json').read_text())
l=json.loads((Q/'reading-ledger.json').read_text())
i=json.loads((Q/'identities.json').read_text())
facts=f['facts'][:10]
assert [x['id'] for x in facts]==['SHOP-DATA','SHOP-SCENE','SHOP-BUY','SHOP-BONUS','SHOP-SELL','SHOP-ENTRY','BP-DATA','BP-SCENE','BP-BUY','BP-ENTRY']
entries=l['initial'][30:32]
ids=i['payloads'][30:32]
for entry, identity in zip(entries,ids):
    assert entry['identity']==identity
    b=(R/identity['path']).read_bytes()
    assert len(b)==identity['bytes'] and hashlib.sha256(b).hexdigest()==identity['sha256']
    assert b==subprocess.check_output(['git','show',C+':'+identity['path']],cwd=R)
    assert entry['own_full_read'] and entry['reviewer']=='/root/creature_b'
typed=json.loads((P/'typed-record-facts.v1.json').read_text())
shadow=typed['paths'][0]
assert shadow['path']=='PBS/Shadow Pokémon backup/items_shadow_pkmn.txt'
rows=[]
for rec,price,sell in zip(shadow['records'],[600,800,1200,0],[300,400,600,0]):
    fs={x['key']:x['interpreted_value'] for x in rec['fields']}
    assert fs['Price']==price and rec['omitted_fields']['SellPrice']==sell and rec['omitted_fields']['BPPrice']==1
    rows.append({'id':rec['id'],'raw_price':price,'default_sell_price':sell,'default_BP_price':1,'important':False,'consumed_after_use':True,'normal_buy_price_without_positive_override':price,'normal_sell_price_without_nonnegative_override':sell,'BP_actual_unit_cost_without_positive_override':1,'BP_quantity_window_subtotal_per_unit':0,'normal_sell_eligible_without_override':sell>0})
receipt={
 'schema':'gr8-pbs-current-shop-price-reception/v1','utc':UTC,
 'actual_receiver':'/root/pbs_creature_current_cloud','actual_original_reader':'/root/creature_b',
 'inputs':[meta(Q/x) for x in ['dependency-semantic-facts.json','reading-ledger.json','identities.json']],
 'received_complete_common':{k:v for k,v in f.items() if k!='facts'},
 'received_complete_facts':facts,
 'received_complete_source_reading_entries':entries,
 'received_complete_source_identities':ids,
 'actual_reception_io':{'facts':['f8d819','85ced8','1449b8','92dfc6'],'reading_entries':['74df60','92dfc6'],'identities':['57b9d5','92dfc6'],'qualification':'Complete named objects and all shared premises actually displayed and read. Git/byte checks performed afterwards bind identities only; they do not substitute for reading and do not transfer sourceFULL to this receiver.'},
 'own_complete_raw_records':shadow,
 'manual_derived_price_rows':rows,
 'own_necessary_sources':{'Item':'Own full270-line definition/schema/defaults/getters; exact consumed_after_use? name and important predicate are clarified by mandatory-consumable-predicate-clarification.v1.json.','Player':'Own full123-line class; setters clamp reached money/BP assignment. Constructor values and overridden setters retain their separately stated premises.','Bag':'Own full301-line Bag/PC/StorageHelper; ordinary add/remove can partially mutate on false. Shop add-one rollback is a different explicit loop with its own failure prefix.'},
 'manual_receiver_meaning':[
  {'id':'PC-SHADOW-PRICE-INSTALL','meaning':'These four records are optional Shadow backup bodies, absent from default discovered PBS inputs. All below require explicit inclusion/installation and successful registry/archive loading. No default shop stock or purchase event is inferred from the record.'},
  {'id':'PC-SHADOW-PRICE-OVERRIDE','meaning':'For the no-applicable-override case, buy/sell/BP values are the four complete rows above. Normal and BP buy use only positive temporary buy-slot override; normal sell accepts nonnegative sell-slot override. The overlay writer and arbitrary externally supplied stock are outside this receipt.'},
  {'id':'PC-SHADOW-PRICE-UI','meaning':'Names/description flow through Item getters into received shop list and description interfaces; machine extras, icon resolution, localization and rendered pixels are independent. For BPPrice=1 without positive override, quantity subtotal shows floor(1/2)*quantity=0 while confirmation and real cost use full quantity*1.'},
  {'id':'PC-SHADOW-PRICE-PURCHASE','meaning':'All four are nonimportant. Without positive override, TIMEFLUTE normal money price0 reaches free-item ordinary maximum999 subject to bag/cancel/confirmation and later checks; other values yield min(999,floor(resource/price)). Completed item additions precede spend statistics and resource setter; add failure rolls back the just-added prefix and may raise if removal fails. No all-or-nothing guarantee across arbitrary exceptions.'},
  {'id':'PC-SHADOW-PRICE-SALE','meaning':'Without a nonnegative sell override, the three scents are sell-price positive and TIMEFLUTE price0 is rejected before quantity choice. Reached sale updates clamped wallet and actual-increase statistic before unchecked one-at-a-time removal, so no generic transaction rollback guarantee is inferred.'},
  {'id':'PC-SHADOW-PRICE-EXIT','meaning':'Entry normalizes and filters the supplied stock array in place; ordinary exit clears the full temporary price overlay. Abnormal exit has no guaranteed cleanup. No stock reconstruction or shop-presence claim follows from PBS alone.'}
 ],
 'own_formal_full_read':{'path':'deliverables/final-specification-set/creature-rpg/wp29-shops-and-exchanges.md','actual_io':'74df60','scope':'Whole document actually read; finite shop/BP clauses assessed with the 10 received complete facts. This receipt does not claim all WP29 UI/media/test predicates or every external caller.'},
 'remaining':'No own FULL two shop source files, no PRICE-WRITER fact reception, no arbitrary stock/caller/override writer or all693 defaultItem record-body acceptance; no host UI/audio/native/save execution. Existing frozen typed record OPEN wording remains historical; only these named price/description consumer propositions resolve here.',
 'business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED','new_findings':[],'new_contexts':0,'new_votes':0
}
out=P/'shadow-item-shop-price-reception.v1.json'
assert not out.exists()
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
own=json.loads((P/'reading-ledger.json').read_text())
formal=receipt['own_formal_full_read']['path']
if formal not in own['formal_full_read']:own['formal_full_read'].append(formal)
own['updated_utc']=UTC
(P/'reading-ledger.json').write_text(json.dumps(own,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':UTC,**meta(out),'complete_facts':len(facts),'complete_original_reading_entries':2,'own_shadow_records':4,'own_formal_full':len(own['formal_full_read'])},ensure_ascii=False))
