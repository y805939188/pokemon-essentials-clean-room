require 'json'
module Settings
  PHONE_REMATCHES_POSSIBLE_FROM_BEGINNING = false
end
module EventHandlers
  def self.add(*args); end
end
module GameData
  module TrainerType
    def self.exists?(value)
      [:CAMPER, 'CAMPER'].include?(value)
    end
    def self.get(value)
      raise 'invalid fixture type' unless exists?(value)
      Struct.new(:id, :name).new(:CAMPER, 'Camper')
    end
  end
end
module MessageTypes
  TRAINER_NAMES = 14
end
class Game_Event
  attr_reader :map_id, :id
  def initialize
    @map_id = 2
    @id = 7
  end
end
class ProbeGlobal
  attr_accessor :phone
  def initialize
    @phone = Phone.new
  end
end
class ProbeMeta
  def has_flag?(flag)
    flag == 'NoPhoneSignal'
  end
end
def _INTL(text, *args)
  text
end
def pbGetMessageFromHash(type, name)
  name
end
def pbMessage(text)
  $probe_messages << text
end
$probe_messages = []
load ARGV[0]
$PokemonGlobal = ProbeGlobal.new
$game_map = Struct.new(:metadata, :map_id).new(ProbeMeta.new, 1)
results = []
results << {id: 'P01', class_get: Phone.respond_to?(:get), class_get_trainer: Phone.respond_to?(:get_trainer), instance_get: $PokemonGlobal.phone.respond_to?(:get)}
[:trainer, :npc].each do |kind|
  args = kind == :trainer ? [:CAMPER, 'Jeff', 0] : ['NPC']
  begin
    Phone::Call.make_outgoing(*args)
    results << {id: kind == :trainer ? 'P02' : 'P03', error: nil}
  rescue StandardError => err
    results << {id: kind == :trainer ? 'P02' : 'P03', error: err.class.name, method_name: err.respond_to?(:name) ? err.name : nil, messages: $probe_messages.length}
  end
end
contact = Phone::Contact.new(true, 2, 7, :CAMPER, 'Jeff', 3, 0, 0)
$PokemonGlobal.phone.contacts << contact
before_messages = $probe_messages.length
ret = Phone::Call.make_outgoing(contact)
results << {id: 'P04', return_value: ret, message_delta: $probe_messages.length - before_messages}
contact.version = 1
$PokemonGlobal.phone.rematch_variant = 2
v = Phone.variant(:CAMPER, 'Jeff', 0)
Phone.increment_version(:CAMPER, 'Jeff', 0)
results << {id: 'P05', public_variant: v, record_variant: contact.variant, record_version_after_public_increment: contact.version, record_next_version: contact.next_version}
[:event, :ids].each do |kind|
  $PokemonGlobal = ProbeGlobal.new
  args = kind == :event ? [Game_Event.new, :CAMPER, 'Jeff', 3, 0] : [2, 7, :CAMPER, 'Jeff', 3, 0]
  2.times { Phone.add_silent(*args) }
  results << {id: kind == :event ? 'P06' : 'P07', contacts: $PokemonGlobal.phone.contacts.map { |c| [c.versions_count, c.start_version, c.visible?] }}
end
module SaveData
  class ProbeConversion
    attr_reader :callback
    def essentials_version(*args); end
    def display_title(*args); end
    def to_value(key, &block); @callback = block; end
  end
  def self.register_conversion(id, &block)
    value = ProbeConversion.new
    value.instance_eval(&block)
    @probe_callback = value.callback
  end
  def self.probe_callback; @probe_callback; end
end
source_lines = File.readlines(ARGV[1])
eval(source_lines[354..380].join, TOPLEVEL_BINDING, ARGV[1], 355)
legacy = [true, :CAMPER, 'Jeff', 0, 2, 3, 2, 7]
global = ProbeGlobal.new
global.phone = nil
global.instance_variable_set(:@phoneNumbers, [legacy])
$PokemonGlobal = global
begin
  SaveData.probe_callback.call(global)
rescue StandardError => err
  results << {id: 'P08', error: err.class.name, method_name: err.respond_to?(:name) ? err.name : nil, phone_created: !global.phone.nil?, new_count: global.phone.contacts.length, legacy_retained: global.instance_variable_get(:@phoneNumbers) == [legacy], new_flag: global.phone.contacts[0].rematch_flag}
end
SaveData.probe_callback.call(global)
results << {id: 'P09', second_call_count: global.phone.contacts.length, legacy_still_retained: global.instance_variable_get(:@phoneNumbers) == [legacy]}
cold = ProbeGlobal.new
cold.phone = nil
cold.instance_variable_set(:@phoneNumbers, [legacy])
$PokemonGlobal = nil
begin
  SaveData.probe_callback.call(cold)
rescue StandardError => err
  results << {id: 'P10', error: err.class.name, method_name: err.respond_to?(:name) ? err.name : nil, phone_created: !cold.phone.nil?, new_count: cold.phone.contacts.length, legacy_retained: cold.instance_variable_get(:@phoneNumbers) == [legacy]}
end
puts JSON.generate({ruby: RUBY_VERSION, vector_count: results.length, results: results})
