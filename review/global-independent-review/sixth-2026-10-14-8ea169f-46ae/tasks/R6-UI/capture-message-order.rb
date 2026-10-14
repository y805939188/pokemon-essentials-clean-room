# Isolated actual-reference probe; no graphical host, saves, I/O effects or network.
require 'open3'
require 'digest'
require 'json'
REF_REPO = '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials'
REF_REV = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def frozen_source(path, expected)
  bytes, err, status = Open3.capture3('git', '-C', REF_REPO, 'show', "#{REF_REV}:#{path}")
  raise err unless status.success?
  raise 'binding mismatch' unless Digest::SHA256.hexdigest(bytes) == expected
  bytes.lines
end
class Battle; end
module Settings
  HEAL_STORED_POKEMON = false
end
module MultipleForms
  def self.call(*); nil; end
end
def _INTL(template, *args)
  template.gsub(/\{(\d+)\}/) { args[$1.to_i - 1].to_s }
end
catch_path = 'Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb'
catch_lines = frozen_source(catch_path, '3242b22c2719ced91097e69060488024b7ee1368152f3266cda1c37fcf33b4a3')
# Source module's complete first method, then close the module for this local load.
eval(catch_lines[0...85].join + "\nend\n", TOPLEVEL_BINDING, catch_path, 1)
peer_path = 'Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb'
peer_lines = frozen_source(peer_path, '9cf59982aaea924cc109721f440d235fd310bfaed3caf2c612d1ec4bc5fbc6ce')
eval(peer_lines[3...60].join, TOPLEVEL_BINDING, peer_path, 4)

class FixturePokemon
  attr_accessor :name, :status, :statusCount, :hp, :form
  def initialize(name); @name = name; @status = :NONE; @hp = 10; @form = 0; end
  def shadowPokemon?; true; end
  def makeUnmega; end
  def makeUnprimal; end
  def totalhp; 10; end
  def item_id; @name + '_item'; end
end
class FixturePlayer
  attr_reader :party
  def initialize; @party = ('A'..'F').map { |name| FixturePokemon.new(name) }; end
  def party_full?; @party.length >= 6; end
end
class FixtureStorage
  attr_reader :stored
  def initialize; @stored = []; end
  def currentBox; 0; end
  def pbStoreCaught(pkmn); @stored.push(pkmn); 0; end
  def [](index); Struct.new(:name).new('Box1'); end
end
class FixtureScene
  def pbPartyScreen(*); yield 0, nil; end
end
class ControlledInterruption < StandardError; end
class FixtureBattle < Battle
  include Battle::CatchAndStoreMixin
  attr_reader :snapshots
  def initialize(interrupt = false)
    @fixture_player = FixturePlayer.new
    @peer = Battle::Peer.new
    @scene = FixtureScene.new
    @sendToBoxes = 0
    @usedInBattle = [Array.new(6, false)]
    @initialItems = [@fixture_player.party.map(&:item_id)]
    @snapshots = []
    @interrupt = interrupt
    $PokemonStorage = FixtureStorage.new
    $game_temp = Struct.new(:party_levels_before_battle, :party_critical_hits_dealt, :party_direct_damage_taken).new([1,2,3,4,5,6],[10,20,30,40,50,60],[100,200,300,400,500,600])
  end
  def pbPlayer; @fixture_player; end
  def pbShowCommands(*); 0; end
  def pbDisplay(*); end
  def snapshot(stage)
    {stage: stage, party: pbPlayer.party.map(&:name), box: $PokemonStorage.stored.map(&:name), initial_items: @initialItems[0].clone, levels: $game_temp.party_levels_before_battle.clone}
  end
  def pbDisplayPaused(message)
    @snapshots.push(snapshot(message))
    raise ControlledInterruption, 'message boundary' if @interrupt
  end
end
normal = FixtureBattle.new
normal.pbStorePokemon(FixturePokemon.new('N'))
puts JSON.generate({case: 'normal', message_observations: normal.snapshots, after: normal.snapshot('returned'), mode: 'isolated_actual_reference', source_ranges: {catch_path=>[1,85],peer_path=>[4,60]}, hostDemo: false})
raise 'order check failed' unless normal.snapshots[0][:party] == ['B','C','D','E','F'] && normal.snapshots[0][:box] == ['A'] && normal.snapshots[0][:initial_items][0] == 'A_item'
raise 'normal tail check failed' unless normal.snapshot('returned')[:party] == ['B','C','D','E','F','N']
interrupted = FixtureBattle.new(true)
begin
  interrupted.pbStorePokemon(FixturePokemon.new('N'))
rescue ControlledInterruption
  puts JSON.generate({case: 'controlled_message_interruption', after: interrupted.snapshot('interrupted'), mode: 'isolated_actual_reference', no_cleanup_guarantee: true, hostDemo: false})
end
