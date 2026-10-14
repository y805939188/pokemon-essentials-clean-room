# Audit-only isolated control-flow probe. No native game host, media, saves,
# maps, service, network, or production implementation is invoked.
require "json"
module Settings
  FISHING_BEGIN_COMMON_EVENT = -1
  FISHING_END_COMMON_EVENT = -1
  EXCLAMATION_ANIMATION_ID = 3
  FISHING_AUTO_HOOK = false
end
class ProbePlayer
  attr_accessor :lock_pattern, :pattern
  attr_reader :movement
  def set_movement_type(value); @movement = value; end
  def straighten; end
  def x; 0; end
  def y; 0; end
end
class ProbeScene
  def spriteset; self; end
  def addUserAnimation(*args); end
end
def pbCommonEvent(_id); false; end
def pbWait(_seconds); end
def pbCreateMessageWindow; {}; end
def pbDisposeMessageWindow(_window); end
def pbMessageDisplay(*args); end
def _INTL(value); value; end
def rand(domain)
  $probe_draws << domain.to_s
  value = $probe_values.shift
  raise "unexpected random draw" if value.nil?
  value
end
source = File.expand_path("../../../../../reference/pokemon-essentials/Data/Scripts/012_Overworld/005_Overworld_Fishing.rb", __dir__)
load source
# The wait/input host is replaced with explicit return values; this validates
# only the source coordinator's draw guards, not timing, input or animation.
def pbWaitMessage(_window, _time); $probe_cancel; end
def pbWaitForInput(*args); $probe_hook_input; end
cases = [
  ["no_encounter", false, false, true, false, false, [5]],
  ["wait_cancel", true, true, true, false, false, [5]],
  ["bite_miss", true, false, true, false, false, [5, 99]],
  ["hook_timeout", true, false, false, false, false, [5, 0, 5]],
  ["normal_success", true, false, true, false, false, [5, 0, 5, 0]],
  ["auto_success", true, false, true, true, false, [5, 0, 5]],
  ["accelerated_no_encounter", false, false, true, false, true, [8, 5]]
]
results = cases.map do |name, encounter, cancel, hook_input, auto, speedup, values|
  Settings.send(:remove_const, :FISHING_AUTO_HOOK)
  Settings.const_set(:FISHING_AUTO_HOOK, auto)
  $stats = Struct.new(:fishing_count).new(0)
  $PokemonGlobal = Struct.new(:fishing, :surfing).new(false, false)
  $game_player = ProbePlayer.new
  $player = Struct.new(:first_pokemon).new(speedup ? Struct.new(:ability_id).new(:STICKYHOLD) : nil)
  $scene = ProbeScene.new
  $probe_draws = []
  $probe_values = values.dup
  $probe_cancel = cancel
  $probe_hook_input = hook_input
  result = pbFishing(encounter, 1)
  raise "unconsumed expected draws" unless $probe_values.empty?
  {case: name, result: result, random_domains: $probe_draws, fishing_count: $stats.fishing_count,
   fishing: $PokemonGlobal.fishing, pattern_locked: $game_player.lock_pattern, movement: $game_player.movement,
   evidence: "TOOL_VALIDATION_ISOLATED_SOURCE_CONTROL_FLOW", host_execution: false}
end
puts JSON.pretty_generate(results)
