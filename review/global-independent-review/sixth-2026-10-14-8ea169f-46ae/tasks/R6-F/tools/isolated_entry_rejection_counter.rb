# Independent negative check of the alleged stale Entry command across loop iterations.
# Exact already-read entry method and rule files, memory-only scene; no real Summary/host.
require 'json'
require 'digest'
R = '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/'
INPUTS = {
 'Data/Scripts/016_UI/005_UI_Party.rb' => '6717a61c57d70ea534e7f6d1e76af05dd0ba725494ff75973691d126aba3ef6d',
 'Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/002_Challenge_Rulesets.rb' => 'c31011ebfc610f013ade62ba733c90198b8be95570e18a004dc82d0db63790c3',
 'Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/003_Challenge_EntryRestrictions.rb' => '10c3f9d92c6cebb126f84517a5f607808bf3d8d904eb1f349a744fd3e7651698'
}.freeze
INPUTS.each { |p,h| raise 'input mismatch' unless Digest::SHA256.file(R+p).hexdigest==h }
module Settings; MAX_PARTY_SIZE = 6; end
def _INTL(s,*a); a.each_with_index { |v,i| s=s.gsub("{#{i+1}}",v.to_s) }; s; end
load R+INPUTS.keys[1]
load R+INPUTS.keys[2]
def pbEachCombination(list,n,&block); list.combination(n,&block); end
class AuditScene
 attr_reader :annotations,:summary_calls,:menus
 def initialize(actions); @actions=actions;@annotations=[];@summary_calls=[];@menus=[];end
 def pbStartScene(*args);end
 def pbAnnotate(v);@annotations << v.dup;end
 def pbSelect(*args);end
 def pbSetHelpText(*args);end
 def pbChoosePokemon;raise 'exhausted actions' if @actions.empty?;@actions.shift;end
 def pbShowCommands(prompt,commands);@menus << commands.dup;commands.index('Entry') || commands.index('Cancel');end
 def pbSummary(index);@summary_calls << index;yield if block_given?;end
 def pbEndScene;end
end
class AuditScreen
 attr_reader :messages
 def initialize(party,scene);@party=party;@scene=scene;@messages=[];end
 def pbRefreshSingle(*args);end
 def pbDisplay(v);@messages << v;end
end
AuditScreen.class_eval(File.readlines(R+INPUTS.keys[0])[1050...1139].join,R+INPUTS.keys[0],1051)
P = Struct.new(:name,:species)
party=[P.new('A1',:BULBASAUR),P.new('A2',:BULBASAUR),P.new('B',:EEVEE)]
results = [[0,1,6,-1],[0,2,6],[6,-1]].map do |actions|
 rules=PokemonRuleSet.new.setNumber(2).addTeamRule(SpeciesClause.new)
 scene=AuditScene.new(actions.dup)
 screen=AuditScreen.new(party,scene)
 ret=screen.pbPokemonMultipleEntryScreenEx(rules)
 {actions:actions,preflight:rules.hasValidTeam?(party),annotations:scene.annotations,
  menu_commands:scene.menus,summary_calls:scene.summary_calls,messages:screen.messages,
  returned:ret && ret.map(&:name)}
end
i=0; loop_locals=[]
loop do
 i+=1
 command=0 if i==1
 loop_locals << {iteration:i,command:command}
 break if i==2
end
puts JSON.pretty_generate({validation:'ISOLATED_EXACT_ENTRY_METHOD_WITH_MEMORY_SCENE',
 ruby:RUBY_DESCRIPTION,input_sha256:INPUTS,host_demo:'NOT_RUN',
 observation_limit:'Only whether Summary is invoked; does not execute real Summary resources.',
 pure_ruby_loop_local_control:loop_locals,results:results})
