import json,hashlib,subprocess,datetime
from pathlib import Path
T=Path('review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/ui_full');R=Path('/workspace/pokemon-essentials')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
specs=[('Data/Scripts/010_Data/002_PBS data/018_MapMetadata.rb',None),('PBS/map_metadata.txt',None),('Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',[[1,110],[1160,1255]]),('Data/Scripts/021_Compiler/001_Compiler.rb',[[1,166],[255,437],[660,745]]),('Data/Scripts/010_Data/001_GameData.rb',None),('Data/Scripts/010_Data/002_PBS data/002_TownMap.rb',None),('PBS/town_map.txt',None)]
sources=[]
for path,ranges in specs:
 raw=(R/path).read_bytes();n=len(raw.splitlines());full=ranges is None;ranges=ranges or [[1,n]]
 sources.append(dict(repo=str(R),commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',tree='7589c800b61ba13a13040ed0d686979b80a84fd0',path=path,blob=subprocess.check_output(['git','rev-parse','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+path],cwd=R,text=True).strip(),mode='100644',bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),lines=n,reader='/root/ui_full',whole_file_read=full,status='FULL_READ' if full else 'PARTIAL_READ_COMPLETE_NAMED_UNITS',ranges=ranges))
rows='''001|Intro|no map position
002|Lappet Town|0,13,12; Outdoor/ShowArea; BattleBack field
003|\\PN\'s house|0,13,12; HealingSpot2,8,8
004|Pokémon Lab|0,13,12
005|Route 1|0,13,11; Outdoor/ShowArea; field
006|Route 1|0,13,11
007|Cedolan City|0,13,10; Outdoor/ShowArea; MapSize2,11
008|Lappet Town|0,13,12
009|Cedolan City|0,14,10; HealingSpot8,17,11
010|Cedolan City|0,13,10; indoor3; EnvironmentRock; DisableBoxLink
011|Cedolan City|0,14,10
012|Cedolan City|0,14,10
013|Cedolan City|0,14,10
014|Cedolan City|0,13,10
015|Cedolan City|0,13,10
016|Cedolan City|0,13,10
017|Cedolan City|0,13,10
018|Cedolan City|0,13,10
019|Cedolan City|0,13,10
020|Cedolan City|0,13,10
021|Route 2|0,14,8; Outdoor/ShowArea; Rain100; field; MapSize1,11
023|Lerucean Town|0,15,8; Outdoor/ShowArea
024|Lerucean Town|0,15,8; HealingSpot23,11,15
025|Lerucean Town|0,15,8
026|Lerucean Town|0,15,8
027|Lerucean Town|0,15,8
028|Natural Park|0,16,8; Outdoor/ShowArea; field; MossRock/BugContest
029|Natural Park|0,16,8; Bicycle; BugContestReception
030|Natural Park|0,16,8; BugContestReception
031|Route 3|0,14,6; Outdoor/ShowArea; field; MapSize2,1101
034|Route 3|0,15,6; Bicycle; cave1; EnvironmentCave; IceRock
035|Ingido Plateau|0,13,6; Outdoor/ShowArea
036|Ingido Plateau|0,13,6; HealingSpot35,17,7
037|Ingido Plateau|0,13,6; elite1; DisableBoxLink
038|Ingido Plateau|0,13,6; DisableBoxLink
039|Route 4|0,11,6; Outdoor/ShowArea; field; MapSize2,11
040|Route 4|0,11,6; Outdoor/ShowArea/BicycleAlways
041|Route 5|0,11,7; Outdoor/ShowArea/BicycleAlways; MapSize1,111
044|Route 6|0,11,10; Outdoor/ShowArea; field; MapSize2,11
045|Route 6|0,11,10; Outdoor/ShowArea/BicycleAlways
046|Route 4|0,12,6; Bicycle
047|Route 7|0,15,10; Outdoor/ShowArea; Rain0; rocky; MapSize2,11; EnvironmentRock
049|Route 7|0,16,10; Bicycle; cave1; EnvironmentCave; Magnetic/DistortionWorld
050|Route 7|0,16,10; Bicycle/DarkMap; cave3; EnvironmentCave; Magnetic/DistortionWorld
051|Route 7|0,16,10; Bicycle/Dungeon; cave2; EnvironmentCave; Magnetic/DistortionWorld/ScaleWildEncounterLevels
052|Battle Frontier|0,17,10; Outdoor/ShowArea
053|Battle Frontier|0,17,10; HealingSpot52,17,14
054|Battle Frontier|0,17,10
055|Battle Frontier|0,17,10; HealingSpot52,30,10
056|Battle Frontier|0,17,10; indoor1; DisableBoxLink
057|Battle Frontier|0,17,10
058|Battle Frontier|0,17,10
059|Battle Frontier|0,17,10; indoor1; DisableBoxLink
060|Battle Frontier|0,17,10
061|Battle Frontier|0,17,10; indoor1; DisableBoxLink
062|Battle Frontier|0,17,10
063|Battle Frontier|0,17,10; DisableBoxLink
064|Battle Frontier|0,17,10; indoor1; DisableBoxLink
065|Battle Frontier|0,17,10; DisableBoxLink
066|Safari Zone|0,12,12; Outdoor/ShowArea; field
067|Safari Zone|0,12,12
068|Safari Zone|0,12,12; Outdoor/ShowArea/SafariMap; forest; EnvironmentForest
069|Route 8|0,13,13; Outdoor/ShowArea; DiveMap70; field
070|Route 8|0,13,13; underwater; EnvironmentUnderwater
071|Route 8|0,13,13
072|Berth Island|0,18,17; Outdoor/ShowArea; Storm50; field; DistortionWorld
073|Faraday Island|0,22,16; Outdoor/ShowArea; field; DistortionWorld
074|Route 6|0,12,10; Bicycle
075|Tiall Region|1,13,16; Outdoor; city'''
defaults=[]
for line in rows.splitlines():
 a,b,c=line.split('|');defaults.append(dict(id=a,real_name=b,all_supplied_other_fields=c))
texts=[
'MapMetadata DATA_FILENAMEmap_metadata.dat; PBS_BASE_FILENAMEmap_metadata; SCHEMA MapPosition=uuu, MapSize=us, Flags=*s, Name=s; SectionName=u. Other declaredfields actualfullschema/editor_properties/constructorread, not abbreviatedsourceFULL.',
'Constructor directly assigns town_map_position and town_map_size references fromhash; absentstaynil; flags defaults[] and suffix emptystring, no added shape/length/bit validation. Positive/zerowidth only from parser, directconstructor no validation.',
'Constructor preserves supplied name/string; name uses MAP_NAMEShash lookup then basicMapName fallback whennil/empty; replaces\\PN inplace ifplayer. Sharedtranslatedstrings maymutate before displayconfirmation; existing UI001optional unchanged.',
'has_flag? caseinsensitive any equality; HideEncountersInPokedex exactconsumerstring depends flags and currentfilter, not a distinct schema boolean.',
'GameData::ClassMethodsIDNumbers.register writesnew constructedobject underhashid; exists nilfalse then validatesclass/integer; get strictunknownraises; try_get unknownnil.',
'Numericclass each sortskeys; load uses const_set(DATA,load_data(Data/DATA_FILENAME)); it doesnot rerun constructor/schema validation. save uses currentDATA via save_data. No loadfromPBS implied by thisloader.',
'compile_map_metadata delegates generic with validationfalse perrecord/finaltrue. Perrecord onlyfills missing/emptyreal_name fromMapInfos; final createsmap_namesindexedbyid and setsMAP_NAMEShashmessages.',
'Generic optionalfileearlyreturn only OPTIONALconstanttruthy and noexistingpath; MapMetadata hasnoOPTIONAL. Otherwise clearDATA before readingpaths andschema.',
'For eachpath generic startsprogress, computesPBSfilesuffix, opensbinary, sections parsed; initializesidsection.to_sym then SectionName=u replacesidwithinteger. Onlypresent schema properties compiled, unknownproperties not stored bythisloop.',
'Generic ^repeatproperties parseeachvalueintoarray andcompact; plainproperty singleCSVrecord; emptyresultarray convertednil. Registration afterperrecordvalidation and duplicateid check; duplicate raisesafterearlierrecordsremain.',
'After allpaths finalvalidationcalled, then game_data.save. Reader/parse/validation/duplicate/message/save failure has no globalrollback; priorDATAclear/registeredrecords/messagebucketprefix remain atactualstage.',
'pbEachFileSectionEx stripsfirstUTF8BOM ifpresent, forcesUTF8; skipsinitial# and blank; prepline removes #tail and outerspace. [section] beginsnewrecord andyieldsprior; exactkeyvalueassign repeatednormalkeyreplaces, ^schemaaccumulates; malformed/preamble raises.',
'pbEachFileSection accepts anynonemptysectionname; numberedwrapperexists but genericusesordinarywrapper thenSectionNameparser. Graphicsupdatesatcountgates are requests and mayraise before laterparse/registration.',
'split_csv_line splitcomma then quotedconcatenations andouterspace trimming, compactnils; get_csv_record appliesdeclaredschema order; optionaluppercase emptynil; * repeats, ^ singleliststripmarker; q preservesraw; no fixed rowlength semanticcheck forMapSize string.',
'cast_csv_value u requiresdigitsincluding0, v additionallynonzero, s returnsvalueunchanged; therefore MapSizewidth0 allowed and 10000/11111/stringsx allowed bys. Creatorlegitimate01content is formalnormalpremise, notparserenforcedbitlength.',
'TownMap43 andPBS36 alreadyownFULL. TownMapschema Point=* or^structured coordinates/text/fly/switch use exactoriginaldefinition; constructorkeepspointarray, no semantic equality toMapMetadata position enforced.',
'compile_town_map samegeneric; perrecordvalidationempty; finalcollectsregionnamesindexedbyid and allpointnames/interestnames, uniqueseach, sets3hashmessagebuckets before save. No consistencyvalidation againstMapMetadata footprint.',
'All69defaultmap_metadata records individuallyread; every suppliedfield preserved inhandwritten69rowrecord list and originalrawtext below. No HideEncountersInPokedex defaultflag occurs; nondefaultsuppliedflag conditional remainssupported.',
'DefaultMapSize suppliedonly0072,11;0211,11;0312,1101;0392,11;0411,111;0442,11;0472,11. Other68? recordcount69 means62 others have absentnilMapSize; no authorimplicitrectanglepadding.',
'DefaultMapPosition only001absent,075region1allothersregion0. Manyinteriorids sharelocationandnames; Area union can overlap. This doesnot make everymetadata map encounteravailable.',
'Area consumer E01 completeusesactualGameDataEncounter speciespresence, mapmetadata flag/region andpointvisibility, then existingnonzeroASCIIshape characters union. RegionMapfirstmatchingpoint andrectanglecursor are separate ownUI63 units.',
'Finite shapes width3/10000 or11111 are conditional suppliedmetadata values, not claimed defaultPBSrecords. Sourceconstructor/parserleave the string length; Area consumer preservesexistingcells only, no sixthpadding.',
'No Data/map_metadata.dat in currentR filesystem or fixedgit tree was reported by actualresource_media_serialized_cloud with readonlycheckUTC2026-10-16T06:03:25.106375+00:00, existsfalse/treeemptyexit0. This packet treatsserializedactualrecordsABSENT, not availableunread or automaticallyequalPBS.',
'Complete compilerentrypath governing automaticcompile/defaultdebugrelease startup not allreadhere. Staticconditional compileunit doesnotprove compileinvoked, successfuldiskoutput/load or anyrender/flight.'
]
texts[18]=texts[18].replace('Other68? recordcount69 means62 others','Other62 records')
facts=[dict(id=f'UI-AREA-P-{i:03}',meaning=s) for i,s in enumerate(texts,1)]
wp=json.loads((T.parent/'ui_wp66/forward-mapping.json').read_text())['units'];own=json.loads((T/'forward-mapping.json').read_text())['semantic_units']
d=dict(schema='gr8-ui-area-producer-interface/v1',id='UI-AREA-PRODUCER-01',reader='/root/ui_full',utc=now,sources=sources,facts=facts,manual_fact_count=len(facts),default_records=defaults,default_record_count=len(defaults),literal_default_PBS=(R/'PBS/map_metadata.txt').read_text(),received_complete_consumer_units=[x for x in wp if x['id'] in ['E01','E03','E04','E05','E06','X15','X20']],own_complete_region_units=[x for x in own if x['id'].startswith('UI63-') and int(x['id'][-3:]) in [3,4,5,6,7,24]],bound_scope='Closes actualconstructor+conditionalcompiler+currentliteraldefault records for Area finitecurrentformal claims; compiledactualrecords ABSENT, invocation/createdbinary/runtime not proved. WholeWP63 cumulative ordering alreadyownfullmapping334atoms; no allencounterdata/world/domainapprove.',business='NOT_EXECUTED',business_execution_count=0,update='UPDATE_NOT_STARTED',global_approval=False)
p=T/'area-producer-interface.json';p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
deps=json.loads((T/'dependency-identities.json').read_text())
for rec in sources:
 old=next((x for x in deps['records'] if x['path']==rec['path']),None)
 if old:
  if not old.get('whole_file_read'):
   old.update(rec)
 else:deps['records'].append(rec)
deps['utc']=now;(T/'dependency-identities.json').write_text(json.dumps(deps,ensure_ascii=False,indent=2)+'\n')
b=p.read_bytes();print(json.dumps(dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),facts=len(facts),records=len(defaults))))
