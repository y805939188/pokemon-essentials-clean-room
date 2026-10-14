# Reviewed audit harness: in-memory stubs, no real save, scene, map or external service.
# Loads only fully read fixed files and one fully read UI method; no production code.
require 'json'
require 'digest'
ROOT = '/Users/dingshinn/Desktop/pokemon-framework-reference'
REF = ROOT + '/reference/pokemon-essentials/'
BOUND = {
  'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/001_Challenge_BattleChallenge.rb' => 'f0417a0440747730bceeb9f0778534ddaf68f1dfc1a2119e641ab3ed973fb5b8',
  'Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/002_Challenge_Rulesets.rb' => 'c31011ebfc610f013ade62ba733c90198b8be95570e18a004dc82d0db63790c3',
  'Data/Scripts/016_UI/005_UI_Party.rb' => '6717a61c57d70ea534e7f6d1e76af05dd0ba725494ff75973691d126aba3ef6d'
}.freeze
BOUND.each { |p, digest| raise 'input mismatch' unless Digest::SHA256.file(REF+p).hexdigest == digest }
module Settings
  MAX_PARTY_SIZE = 6
end
def _INTL(text, *args)
  args.each_with_index { |v, i| text = text.gsub("{#{i+1}}", v.to_s) }
  text
end
module Game
  def self.save(safe: false)
    $save_requests << {safe: safe, party: $player.party.dup}
    true
  end
end
def pbWriteCup(*args); end
def pbGetBTTrainers(id); [0]; end
def pbBattleChallengeTrainer(wins, list); 0; end
def pbBattleChallenge; $challenge; end
load REF + BOUND.keys[0]
load REF + BOUND.keys[1]

def facility_case(cancel: false, repeat_start: false)
  $save_requests = []
  $player = Struct.new(:party).new([:original])
  $game_map = Struct.new(:map_id, :need_refresh).new(1, false)
  $game_player = Struct.new(:x, :y).new(2,3)
  $challenge = BattleChallenge.new
  $challenge.set('tower', 1, Object.new)
  type = $challenge.send(:ensureType, 'tower')
  type.currentWins, type.currentSwaps = 5, 2
  $challenge.setParty([:entrant])
  $challenge.start
  $challenge.start if repeat_start
  if cancel
    $challenge.pbCancel
    after_cancel = {identity: $challenge.currentChallenge, current_wins: type.currentWins,
                    current_swaps: type.currentSwaps, in_progress: $challenge.pbInProgress?,
                    party: $player.party}
    $challenge.pbEnd
    return {case: 'cancel_then_end', after_cancel: after_cancel,
            after_end: {identity: $challenge.currentChallenge, current_wins: type.currentWins,
                        current_swaps: type.currentSwaps, party: $player.party}, saves: $save_requests.size}
  end
  $challenge.setDecision(1)
  $challenge.pbEnd
  {case: repeat_start ? 'repeat_start' : 'normal_end', party: $player.party,
   current_wins: type.currentWins, current_swaps: type.currentSwaps, saves: $save_requests.size}
end

class AuditScene
  attr_reader :annotations, :selections
  def initialize(actions)
    @actions, @annotations, @selections = actions, [], []
  end
  def pbStartScene(*args); end
  def pbAnnotate(value); @annotations << value.dup; end
  def pbSelect(value); @selections << value; end
  def pbSetHelpText(*args); end
  def pbChoosePokemon; raise 'exhausted actions' if @actions.empty?; @actions.shift; end
  def pbShowCommands(prompt, commands); commands.index('Entry') || commands.index('Cancel'); end
  def pbSummary(index); @selections << {unexpected_summary_index: index}; yield if block_given?; end
  def pbEndScene; end
end
class AuditPartyScreen
  attr_reader :messages
  def initialize(party, scene)
    @party, @scene, @messages = party, scene, []
  end
  def pbRefreshSingle(*args); end
  def pbDisplay(message); @messages << message; end
end
ui = File.readlines(REF + BOUND.keys[2])[1050...1139].join
AuditPartyScreen.class_eval(ui, REF + BOUND.keys[2], 1051)
def selection_case(number)
  rules = PokemonRuleSet.new
  rules.setNumber(number) if number > 0
  party = [Struct.new(:name).new('A'), Struct.new(:name).new('B')]
  scene = AuditScene.new([0,1,6,-1])
  screen = AuditPartyScreen.new(party, scene)
  result = screen.pbPokemonMultipleEntryScreenEx(rules)
  {case: number == 0 ? 'raw_default_zero_capacity' : 'positive_capacity_control',
   public_number: rules.number, annotations: scene.annotations,
   focus_changes: scene.selections, messages: screen.messages, result: result}
end
results = [facility_case, facility_case(cancel: true), facility_case(repeat_start: true),
           selection_case(0), selection_case(1)]
puts JSON.pretty_generate({validation: 'ISOLATED_ACTUAL_REFERENCE_WITH_MEMORY_ONLY_STUBS',
                          host_demo: 'NOT_RUN', input_sha256: BOUND, results: results})
