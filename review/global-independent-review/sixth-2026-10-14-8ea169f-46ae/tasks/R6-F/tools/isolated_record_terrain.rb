# In-memory record/restore audit; no host, files of data, saved game, media or BGM.
require 'json'
require 'digest'
R = '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/'
INPUTS = {
  'Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb' => '4f03221157435e9951dd64c5854a6a823a3ff615eaa8c421e3bc1d7912e61d36',
  'Data/Scripts/011_Battle/007_Other battle code/002_Battle_ActiveField.rb' => '797cb7876bc8ca08d7ac9604c2887e65aaac27d92a4d9fa01b7ab1598bff2817',
  'Data/Scripts/011_Battle/001_Battle/001_Battle.rb' => 'cceb07e5b430018d6a4b0227316af5cb3e7f60aa9ec7ee729086b5e494beb56d'
}.freeze
INPUTS.each { |p,h| raise 'frozen input mismatch' if Digest::SHA256.file(R+p).hexdigest != h }
module PBEffects
  def self.const_missing(name)
    const_set(name, constants.size)
  end
end
class Battle; end
load R + INPUTS.keys[1]
class Battle
  attr_reader :field
  def initialize(scene=nil, party1=[], party2=[], player=nil, opponent=nil)
    @field = Battle::ActiveField.new
    @party1,@party2,@player,@opponent = party1,party2,player,opponent
    @party1starts,@party2starts,@items,@rules = [0],[0],[],{}
    @internalBattle,@canRun,@switchStyle,@showAnims = false,true,true,true
    @backdrop,@backdropBase,@time,@environment = 'indoor1',nil,0,:None
  end
  def pbStartBattle; 0; end
end
# Only these already-read complete setters are loaded from the main class.
src = File.readlines(R + INPUTS.keys[2])
Battle.class_eval(src[693...698].join,R+INPUTS.keys[2],694)
Battle.class_eval(src[779...784].join,R+INPUTS.keys[2],780)
class BattlePalaceBattle < Battle; end
class BattleArenaBattle < Battle; end
class Player; end
load R + INPUTS.keys[0]
results = [:None,:Electric].map do |terrain|
  recorded = RecordedBattle.new
  recorded.defaultTerrain = terrain
  recorded.defaultWeather = :Rain
  recorded.pbStartBattle
  packet = Marshal.restore(recorded.pbDumpRecord)
  replay = RecordedBattle::PlaybackBattle.new(nil,packet)
  replay.pbStartBattle
  {input_terrain:terrain, recorded_terrain:recorded.field.terrain,
   recorded_terrain_duration:recorded.field.terrainDuration,
   replay_terrain:replay.field.terrain,replay_terrain_duration:replay.field.terrainDuration,
   packet_keys:packet[1].keys.sort,
   recorded_weather:recorded.field.weather, replay_weather:replay.field.weather,
   recorded_default_weather:recorded.field.defaultWeather,
   replay_default_weather:replay.field.defaultWeather}
end
puts JSON.pretty_generate({validation:'ISOLATED_ACTUAL_REFERENCE_CAPTURE_AND_RESTORE_WITH_STUB_BASE_BATTLE',
                          input_sha256:INPUTS,host_demo:'NOT_RUN',results:results})
