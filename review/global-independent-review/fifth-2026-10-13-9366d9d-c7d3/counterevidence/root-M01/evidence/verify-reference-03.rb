# Audit harness only: load fixed definitions, call named functions on synthetic data.
require 'json'
require 'stringio'
R = '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials'
def nil_or_empty?(value)
  return true if value.nil?
  value.respond_to?(:empty?) && value.empty?
end
load File.join(R, 'Data/Scripts/001_Technical/003_Intl_Messages.rb')
load File.join(R, 'Data/Scripts/021_Compiler/001_Compiler.rb')
load File.join(R, 'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb')
observations=[]
checks=[]
['.','1','1.','.5','0.5','-1.0','+1.0','1e2'].each do |input|
  begin
    value=Compiler.get_csv_record(input,[:height,'f'])
    record={height:value}
    Compiler.validate_compiled_pokemon(record)
    observations << {kind:'float_active_schema_and_size_validation', input:input, parsed:value, stored_height:record[:height], outcome:'returned'}
  rescue StandardError => error
    observations << {kind:'float_active_schema_and_size_validation', input:input, outcome:'exception', error_class:error.class.name, message:error.message}
  end
end
expected={'.'=>[0.0,1],'1'=>[1.0,10],'1.'=>[1.0,10],'.5'=>[0.5,5],'0.5'=>[0.5,5]}
observations.each do |row|
  ex=expected[row[:input]]
  checks << (ex ? [row[:parsed],row[:stored_height]]==ex : row[:outcome]=='exception')
end
lookup=Translation.new
lookup.instance_variable_set(:@core_messages,[])
lookup.instance_variable_set(:@game_messages,[])
lookup.game_messages[24]={"A\nB"=>'T', 'A B'=>'U'}
[["A\n\nB", "A\nB",'T'],["A\nB","A\nB",'T'],['A  B','A B','U'],[" A\n B ","A\nB",'T']].each do |input,key,output|
  actual_key=Translation.stringToKey(input)
  actual_output=lookup.getFromHash(24,input)
  observations << {kind:'key_normalization_and_lookup',input:input,key:actual_key,value:actual_output}
  checks << (actual_key==key && actual_output==output)
end
def seeded(core,game)
  t=Translation.new
  t.instance_variable_set(:@default_core_messages,core)
  t.instance_variable_set(:@default_game_messages,game)
  t
end
[:setMessagesAsHash,:addMessagesAsHash].each do |entry|
  core=[];core[24]={'A'=>'core A'}
  game=[];game[24]={'Z'=>'old Z','A'=>'old A'}
  t=seeded(core,game)
  t.public_send(entry,24,['A','B'])
  actual=t.default_game_messages[24]
  ex= entry==:setMessagesAsHash ? {'B'=>'B'} : {'Z'=>'old Z','A'=>'old A','B'=>'B'}
  observations << {kind:'default_hash_collection',entry:entry,result:actual}
  checks << (actual==ex)
end
[:setMessages,:addMessages].each do |entry|
  core=[];core[21]=['A',nil]
  game=[];game[21]=['old A','old index1','old index2']
  t=seeded(core,game);t.public_send(entry,21,['A','B'])
  actual=t.default_game_messages[21]
  ex= entry==:setMessages ? [nil,'B'] : ['old A','B','old index2']
  observations << {kind:'default_array_collection',entry:entry,result:actual}
  checks << (actual==ex)
end
[0,4].each do |map_id|
  core=[];core[0]=[];core[0][0]={'A'=>'common A'}
  game=[]
  t=seeded(core,game);t.setMapMessagesAsHash(map_id,['A'])
  actual=t.default_game_messages[0][map_id]
  observations << {kind:'map_default_filter',map_id:map_id,result:actual}
  checks << (actual==(map_id==0 ? {} : {'A'=>'A'}))
end
io=StringIO.new
Translator.write_section_texts_to_file(io,'SCRIPT_TEXTS',{'B'=>'translated B','X'=>'language only'},{'B'=>'B','Empty'=>''})
actual=io.string
observations << {kind:'export_default_keys_only',bytes:actual.bytesize,result:actual}
checks << (actual=="[SCRIPT_TEXTS]\r\nB\r\ntranslated B\r\n")
io2=StringIO.new
Translator.write_section_texts_to_file(io2,'SCRIPT_TEXTS',{'B'=>''},{'B'=>'B'})
observations << {kind:'export_valid_empty_translation',result:io2.string}
checks << (io2.string=="[SCRIPT_TEXTS]\r\nB\r\n\r\n")
puts JSON.pretty_generate({runtime:RUBY_DESCRIPTION,case_count:observations.length,observations:observations,all_observed_fields_match:checks.all?,failed_check_indices:checks.each_index.select{|i| !checks[i]}})
exit(checks.all? ? 0 : 1)
