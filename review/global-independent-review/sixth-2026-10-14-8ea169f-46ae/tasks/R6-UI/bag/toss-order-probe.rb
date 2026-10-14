# Audit-only fixed-reference orchestration with explicit local surrogates.
require 'json'
require 'open3'
require 'digest'
REFERENCE = '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials'
REVISION = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PATH_NAME = 'Data/Scripts/016_UI/007_UI_Bag.rb'
source, stderr, status = Open3.capture3('git', '-C', REFERENCE, 'show', "#{REVISION}:#{PATH_NAME}")
raise stderr unless status.success?
class Window_DrawableCommand; end
class Color
  def initialize(*); end
end
class ItemFixture
  def is_mail?; false; end
  def is_machine?; false; end
  def can_hold?; true; end
  def is_important?; false; end
  def name; 'Fixture'; end
  def portion_name; 'fixture'; end
  def portion_name_plural; 'fixtures'; end
end
module GameData
  module Item
    def self.get(_); ItemFixture.new; end
  end
end
module ItemHandlers
  def self.hasOutHandler(_); false; end
end
def pbCanRegisterItem?(_); false; end
def _INTL(message, *values)
  values.each_with_index { |value, index| message = message.gsub("{#{index + 1}}", value.to_s) }
  message
end
class ContainerFixture
  attr_reader :amount, :events
  def initialize(amount, events); @amount = amount; @events = events; end
  def quantity(_); @amount; end
  def registered?(_); false; end
  def remove(_, quantity = 1)
    @amount -= quantity
    @events << { phase: 'remove', quantity: quantity, remaining: @amount }
    true
  end
end
class PlayerFixture
  def party; []; end
  def pokemon_party; []; end
end
class SceneFixture
  def initialize(container, events, raise_at_message = false)
    @container, @events, @raise_at_message = container, events, raise_at_message
    @choices = [:POTION, nil]
  end
  def pbStartScene(_); @events << { phase: 'start' }; end
  def pbChooseItem; @choices.shift; end
  def pbShowCommands(_, commands)
    @events << { phase: 'commands', commands: commands }
    commands.index('Toss')
  end
  def pbChooseNumber(*); 3; end
  def pbConfirm(_); true; end
  def pbDisplay(message, *)
    @events << { phase: 'message', quantity_at_message: @container.amount, message: message }
    raise 'bounded scene-message failure' if @raise_at_message
  end
  def pbRefresh; @events << { phase: 'refresh', amount: @container.amount }; end
  def pbEndScene; @events << { phase: 'end' }; end
end
class TempFixture
  def fly_destination; nil; end
end
class GlobalFixture
  attr_accessor :pcItemStorage
end
$DEBUG = false
$player = PlayerFixture.new
$game_temp = TempFixture.new
$PokemonGlobal = GlobalFixture.new
eval(source, TOPLEVEL_BINDING, "fixed-reference:#{PATH_NAME}")
results = []
[['bag_normal', false, false], ['bag_message_failure', true, false], ['pc_normal', false, true]].each do |name, failure, pc|
  events = []
  container = ContainerFixture.new(5, events)
  scene = SceneFixture.new(container, events, failure)
  screen = PokemonBagScreen.new(scene, container)
  $PokemonGlobal.pcItemStorage = container
  error = nil
  begin
    pc ? screen.pbTossItemScreen : screen.pbStartScreen
  rescue => caught
    error = caught.message
  end
  results << { name: name, final_quantity: container.amount, error: error, events: events }
end
puts JSON.generate({ reference_commit: REVISION, source_path: PATH_NAME, source_sha256: Digest::SHA256.hexdigest(source), original_reference_entry_methods_executed: ['PokemonBagScreen.pbStartScreen', 'PokemonBagScreen.pbTossItemScreen'], surrogate_boundaries: ['screen input/result scene', 'item/handler metadata', 'container removal semantics', 'player/global/temp', 'translation', 'declaration-time graphics constants'], native_game_execution_count: 0, native_UI_execution_count: 0, real_save_execution_count: 0, independent_model_execution_count: 0, vectors: results })
