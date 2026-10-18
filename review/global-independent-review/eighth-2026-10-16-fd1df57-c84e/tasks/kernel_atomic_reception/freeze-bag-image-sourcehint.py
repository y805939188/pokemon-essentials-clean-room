"""Finite source contribution, not a new finding or independent vote."""
from pathlib import Path
import datetime,hashlib,json
B=Path('/workspace/pokemon-essentials-clean-room');R=Path('/workspace/pokemon-essentials')
BASE=Path(__file__).resolve().parent;RR=BASE.parent.parent
lib=json.loads((RR/'tasks/coverage_acceptance_incremental/dispatch/kernel_atomic_reception.readset.json').read_text())['all_fixed_R432_F131_identity_library']
units=[]
def unit(path,lo,hi,label,credit):
 raw=(R/path).read_bytes();fixed=next(x for x in lib if x['repo']=='R' and x['path']==path)
 assert len(raw)==fixed['bytes'] and hashlib.sha256(raw).hexdigest()==fixed['sha256']
 lines=raw.decode('utf-8-sig').splitlines(keepends=True)
 units.append({'id':'BAGIMAGE-U%02d'%(len(units)+1),'source_identity':fixed,'range':[lo,min(hi,len(lines))],'unit':label,'actual_reader':'/root/kernel_atomic_reception','actual_credit':credit,'text':''.join(lines[lo-1:hi])})
unit('Data/Scripts/016_UI/007_UI_Bag.rb',64,106,'complete Window_PokemonBag.drawItem','Own complete Window/Scene and normalScreen1–580 partial; not whole714L file')
unit('Data/Scripts/007_Objects and windows/010_DrawText.rb',1138,1154,'complete pbDrawImagePositions to actualEOF','Own exact complete method only; not wholeDrawText source')
unit('Data/Scripts/001_Technical/002_Files/001_FileTests.rb',1,484,'complete fixed FileTests source, includes actual resolve/RTP/pbGetFileChar/pbTryString/canonicalize dependencies','Own prior complete484L actually read; extra unrelated definitions confer no new business acceptance')
unit('Data/Scripts/007_Objects and windows/008_AnimatedBitmap.rb',1,228,'complete AnimatedBitmap/PngAnimatedBitmap/GifBitmap','Own actual whole228L in Slot finitecounter; no new context/vote')
unit('Data/Scripts/007_Objects and windows/001_RPG_Cache.rb',1,144,'complete BitmapWrapper/RPG Cache definitions','Own actual whole144L in Slot finitecounter; native Bitmap boundary remains unrun')
unit('Data/Scripts/001_Technical/002_RubyUtilities.rb',24,31,'complete String.first/last definitions and class owner','Own prior complete406L; this packet only these complete named methods')
for lo,hi,label in [(478,491,'Translation class and complete stringToKey'),(511,529,'complete load_message_files'),(600,611,'complete getFromHash'),(638,642,'complete delayed_load_message_files'),(703,703,'SCRIPT_TEXTS constant24'),(752,754,'complete MessageTypes.getFromHash delegate'),(774,785,'complete _INTL wrapper')]:unit('Data/Scripts/001_Technical/003_Intl_Messages.rb',lo,hi,label,'Own prior complete823L; exact named lookup/load definitions only')
unit('Data/Scripts/010_Data/002_PBS data/006_Item.rb',167,202,'complete has_flag?/importance/machine/key/quantity predicates','Own prior fullItem; unrelated following unlosable method not included')
unit('Data/Scripts/013_Items/008_PokemonBag.rb',139,143,'complete registered?','Own prior full301L PokemonBag; no native persistence proof')
unit('Data/Scripts/013_Items/001_Item_Utilities.rb',1,28,'ItemHandlers owner/constants and complete hasUseInFieldHandler','Own PARTIAL exact definitions; remaining handler registrations and ItemUtilities not whole read')
unit('Data/Scripts/013_Items/001_Item_Utilities.rb',121,123,'complete pbCanRegisterItem?','Own PARTIAL exact wholemethod; source first28 and108–141 actually read')
unit('Text_english_core/SCRIPT_TEXTS.txt',3439,3440,'complete actual Bag icon_register key/value pair','Own only this pair plus previously sevenSlot pairs; BOM/UTF8 envelope previously checked, not all3305pairs')
inv=RR/'evidence/external-recovered/localization_records/90b9e27ef03feb2c018bb2f258b5e0d5aaed012b/evidence/continuation/image-unit-inventory.json'
raw=inv.read_bytes();obj=json.loads(raw)[17];assert obj['id']=='ELR-IMG-18' and obj['path']=='Data/Scripts/016_UI/007_UI_Bag.rb'
report={
 'schema':'gr8-kernel-finite-bag-localized-image-sourcehint/v1',
 'captured_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reader':'/root/kernel_atomic_reception','fixed_R':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','fixed_B8':'fd1df570cad987dc3852a3b958f03916e317f7fe',
 'classification':'SOURCE_CONTRIBUTION_ONLY_NO_NEW_FINDING_NO_ROOT_EXPANSION','new_required':0,'new_optional':0,'new_context':0,'new_vote':0,'business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED',
 'premises':['Fixed source definitions/no overrides/concurrent mutations; legitimate Item/Bag/window/bitmap and normal priorcalls.','Legal successfully loaded currentlanguage game/core Hash domain24, String translations; defaulttextpair doesnot activate a language.','Finite A/B control uses ordinary nonprefix valid equally appropriate layout images and observes requested identity rather than pixels; repository asset existence not asserted.'],
 'source_units':units,
 'facts':[
  {'id':'BAGIMG-F01','fact':'Only important items enter register-icon gate. Already registered uses sprite row0; otherwise pbCanRegisterItem? (UseInField handler presence) permits row24. Both callsites use the same _INTL identity Graphics/UI/Bag/icon_register. Nonimportant, or important neither registered nor canRegister, skips this icon.','source':'U01/U14–U17; existing HandlerHash exact/conditional machinery separately personally full-read; no allactual item-handler catalog asserted.'},
  {'id':'BAGIMG-F02','fact':'No image translation => originalA; currentgame24[A]=nonemptyB overrides core and handsB to draw helper evenwhenA exists. Onlycore samekey works ifgame miss. EmptyString stilltruthyhit; no language/options/save writes fromlookup.'},
  {'id':'BAGIMG-F03','fact':'This actual chain differs from directSlotreel: pbDrawImagePositions first calls pbBitmapName(B), then AnimatedBitmap(resolvedB or originalB). Resolver strips recognized lowercase suffix, tries .png then .gif per actualRTP eachPath (current ./), pbTryString tests firstbyte. It never chooses originalA after B failure.'},
  {'id':'BAGIMG-F04','fact':'B empty is passed through pbBitmapName first. If an actual resolver candidate .png/.gif is found, the resulting path proceeds; ifno candidate, originalempty reachesAnimatedBitmap and filename=nil regex fails beforeGifrescue under completeString.last. It is not IconSprite emptyclear and not universally immediateSlot-stylefailure before resolver.'},
  {'id':'BAGIMG-F05','fact':'NonemptyordinaryB cache-load StandardError is caught onlybyGifBitmap and attempts32x32blank; blankcreation/play or lateroperations canfail outsidecatch. Frameprefix takesPng withuncaughtload/frame-validation path. No blanket normalreturn/retryA.'},
  {'id':'BAGIMG-F06','fact':'Draw helper uses requested x/y, sourcex0/sourcey0 or24, width -1 selectsloadedbitmap width, height24 fixed; blits then disposes source. No guarantee arbitraryB layout or nativepixel equivalence.'},
  {'id':'BAGIMG-F07','fact':'After successful icon draw showing_register_icon=true, suppressing quantity evenifshow_quantity? true. The row text positions accumulate earlier but actualtextdraw follows icon/quantity logic. A thrown image-path exception canstopbeforecurrentrowtext and beforethatflagassignment; no localrescue/ensure forwholeDrawItem/helper.'},
  {'id':'BAGIMG-F08','fact':'Scene refresh clears contents before per-row draw; earlier rows/pixels and allocated/wrapped bitmap prefix are not rolledbackonlaterfailure. Normal resourcehelperdisposes onlyafterblt; a raised earliercall doesnot guarantee this cleanup. Native/windowexceptionhigherhandlingunverified.'},
  {'id':'BAGIMG-F09','fact':'External continuation already has exact same complete caller ELR-IMG-18 at inventoryindex17. Actual full selected object and all its premise/reader/evidence fields received below; not a new missed root inferred from no title/search match, not whole36inventory acceptance.'}
 ],
 'control':'Given important registered Item/normalrow, bothlanguagesmiss=>A. Addonlycurrentgame24[A]=B=>B atpbBitmapName input; Aremainsavailable, iconrow0/layoutsame. BothstaticNOT_EXECUTED. Alternate canRegister branch row24 shareskey butisnotneededtothe minimalregisteredcontrol.',
 'inventory_finite_reception':{'path':str(inv),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'complete_object_pointer':'/17','original_actual_reader':obj['actual_reader'],'object':obj,'credit':'Only exact complete object17 actually read; remaining35 structurally parsed for selection, not credited as full semantic inventory.'},
 'formal_boundary':'WholeWP08/WP15 current contract already actually read inSlotcounter; this packet supplies source/consumer only. Slot7 accepted scope not silently enlarged. Root must compare complete external continuation and any necessary independent counter before scope/classification change.',
 'remaining':['No wholeUI_Bag714/fullDrawText1152/sourceItemUtilitiesall credit.','Actual registered Item/UseInField catalog and native media/pixels/actual language loading not run.','Original allR1–R7 canonical roots not fully received, no new-root history negative.','Return to KERNEL whole primary atomic/consumer work.'],
 'io':['io/catalog-bag-complete-item-window-and-class-headers.json','io/catalog-bag-complete-start-and-navigation-definitions.json','io/catalog-bag-complete-normal-screen-caller.json','io/bag-image-complete-draw-helper-and-wrapper-resolve.json','io/bag-image-complete-predicate-and-default-pair-units.json'],
 'actual_direct_output_notes':'Inventory complete selected object a88975; ItemHandlers1–50 e6ff93 and FileTestsRTP complete earlier own484 actualFULL. No backfilled direct-command times.'
}
p=BASE/'bag-localized-register-image-sourcehint.v1.json';p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':report['captured_utc'],'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'complete_units':len(units),'facts':9}))
