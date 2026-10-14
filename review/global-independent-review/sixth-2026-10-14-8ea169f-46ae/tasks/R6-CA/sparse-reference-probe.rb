# Isolated reference-handler probe, NOT a battle simulator or hostDemo.
# Only the manifest-bound, fully read reference files are loaded.
# Host objects below are explicit controlled fixtures. No save, UI, or network.
require 'json'
require 'digest'
require 'ostruct'
$DEBUG = false
$INTERNAL = false
$probe_errors = []
def pbPrintException(error)
  $probe_errors << { 'class' => error.class.name, 'message' => error.message,
                     'location' => error.backtrace.first }
end
ROOT = '/Users/dingshinn/Desktop/pokemon-framework-reference'
manifest = JSON.parse(File.read(File.join(__dir__, 'probe-inputs.json')))
manifest['files'].each do |entry|
  path = File.join(ROOT, entry['path'])
  raise 'input hash mismatch' unless Digest::SHA256.file(path).hexdigest == entry['sha256']
end
module Settings
  MORE_TYPE_EFFECTS = true
end
module PBEffects
  [:Yawn, :JawLock, :MeanLook, :Octolock, :TrappingUser, :Confusion,
   :PerishSong, :ToxicSpikes, :Trapping, :Curse, :Nightmare, :LeechSeed,
   :Wish, :WishAmount, :Substitute].each { |key| const_set(key, key) }
end
class Battle; end
manifest['files'].each { |entry| load File.join(ROOT, entry['path']) }

class ProbeBattler
  attr_reader :index, :effects, :stages, :status, :statusCount, :side
  attr_accessor :dead
  def initialize(index, sleeping=false)
    @index=index; @side=index%2; @dead=false
    @effects=Hash.new(-1)
    @effects[PBEffects::Yawn]=sleeping ? 0 : 2
    @stages={ATTACK:0,DEFENSE:0,SPECIAL_ATTACK:0,SPECIAL_DEFENSE:0,SPEED:0,ACCURACY:0,EVASION:0}
    @status=sleeping ? :SLEEP : :NONE; @statusCount=sleeping ? 3 : 0
  end
  def battler; self; end
  def pokemon; self; end
  def name; 'controlled fixture'; end
  def fainted?; @dead; end
  def pbCanSleepYawn?; true; end
  def wants_status_problem?(_); false; end
  def ability_active?; false; end
  def item_active?; false; end
  def has_active_item?(_); false; end
  def has_active_ability?(_); false; end
  def has_type?(_); false; end
  def trappedInBattle?; false; end
  def check_for_move; false; end
end

def probe(name, indices, skill, handler, random, dead=nil, early=nil)
  sleeping=(handler==:asleep)
  members=[]
  indices.each { |i| members[i]=ProbeBattler.new(i, sleeping) }
  user=members[1]
  members[dead].dead=true if dead
  members[early].effects[PBEffects::MeanLook]=user.index if early
  ai=Battle::AI.new(nil)
  ai.instance_variable_set(:@battlers,members)
  ai.instance_variable_set(:@trainer,OpenStruct.new(:high_skill? => skill>=48))
  ai.define_singleton_method(:pbAIRandom) { |_limit| @draw_count=(@draw_count||0)+1; random }
  before=$probe_errors.length
  result='NOT_ASSIGNED'
  PBDebug.logonerr do
    result=Battle::AI::Handlers::ShouldSwitch[handler].call(user,[ProbeBattler.new(8)],ai,nil)
  end
  {'case'=>name,'handler'=>handler,'indices'=>indices,'skill'=>skill,'fixed_random'=>random,
   'dead'=>dead,'early_pointing_index'=>early,'result'=>result,
   'draws'=>ai.instance_variable_get(:@draw_count)||0,
   'diagnostic_returned'=>true,'errors'=>$probe_errors[before..-1]}
end

rows=[]
{ '1v1'=>[0,1], '1v2'=>[0,1,3], '2v1'=>[0,1,2], '2v2'=>[0,1,2,3],
  '1v3'=>[0,1,3,5], '3v1'=>[0,1,2,4], '2v3'=>[0,1,2,3,5],
  '3v2'=>[0,1,2,3,4], '3v3'=>[0,1,2,3,4,5] }.each do |layout, indices|
  [:yawning,:asleep].each { |handler| rows << probe(layout,indices,48,handler,60) }
end
rows << probe('medium_sparse_yawn',[0,1,3],32,:yawning,60)
rows << probe('medium_sparse_sleep_r59',[0,1,3],32,:asleep,59)
rows << probe('medium_sparse_sleep_r60',[0,1,3],32,:asleep,60)
rows << probe('dense_dead_slot',[0,1,2,3],48,:yawning,60,2)
rows << probe('sparse_short_circuit_before_hole',[0,1,3],48,:yawning,60,nil,0)
rows << probe('sparse_hit_after_hole',[0,1,3],48,:yawning,60,nil,3)
puts JSON.pretty_generate({'evidence_level'=>'ISOLATED_ACTUAL_REFERENCE_HANDLERS_WITH_STUBS',
 'not_proven'=>['complete_battle','UI_reporter','reference_initialization_at_runtime','action_registration','frequency_distribution','hostDemo'],
 'rows'=>rows})
