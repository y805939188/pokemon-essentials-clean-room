require 'json'
class BitmapSprite
  attr_accessor :bitmap
end
class AuditBitmap
  def clear; end
  def blt(*args); end
end
module System
  class << self
    attr_accessor :audit_time
    def uptime; @audit_time; end
  end
end
AuditImage = Struct.new(:height, :bitmap)
Rect = Struct.new(:x, :y, :width, :height)
load '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/017_Minigames/003_Minigame_SlotMachine.rb'

def reel
  object = SlotMachineReel.allocate
  object.bitmap = AuditBitmap.new
  {
    :@reel => SlotMachineReel::ICONS_SETS[0].clone,
    :@index => 0, :@difficulty => 1, :@toppos => 0,
    :@current_y_pos => -1, :@spin_speed => 640,
    :@spinning => false, :@stopping => false, :@slipping => 0,
    :@images => AuditImage.new(48, nil),
    :@shading => AuditImage.new(144, nil)
  }.each { |name, value| object.instance_variable_set(name, value) }
  object
end

def snapshot(object)
  { :index => object.instance_variable_get(:@index),
    :spinning => object.spinning?,
    :slipping => object.instance_variable_get(:@slipping),
    :stopping => object.instance_variable_get(:@stopping),
    :showing => object.showing }
end

results = []
System.audit_time = 0.0
object = reel
object.startSpinning
System.audit_time = 0.01
object.update
results << { :case => 'first_update', :at => 0.01, :observed => snapshot(object), :expected_index => 1 }
object.stopSpinning(true)
System.audit_time = 0.02
object.update
results << { :case => 'no_boundary', :at => 0.02, :observed => snapshot(object), :expected_index => 1, :expected_spinning => true }
System.audit_time = 0.20
object.update
results << { :case => 'zero_slip_cross_two', :at => 0.20, :observed => snapshot(object), :expected_index => 1, :expected_spinning => false }

System.audit_time = 0.0
object = reel
object.startSpinning
System.audit_time = 0.01
object.update
object.stopSpinning(true)
object.instance_variable_set(:@slipping, 2)
System.audit_time = 0.20
object.update
results << { :case => 'positive_slip_reaches_zero', :at => 0.20, :observed => snapshot(object), :expected_index => 3, :expected_spinning => true }
System.audit_time = 0.25
object.update
results << { :case => 'later_boundary_stops', :at => 0.25, :observed => snapshot(object), :expected_index => 3, :expected_spinning => false }

results.each do |entry|
  entry[:observed_fields_match] = entry[:observed][:index] == entry[:expected_index]
  if entry.key?(:expected_spinning)
    entry[:observed_fields_match] &&= entry[:observed][:spinning] == entry[:expected_spinning]
  end
end
puts JSON.pretty_generate({ :runtime => RUBY_DESCRIPTION, :records => results,
  :scope => 'Only original reel state methods with supplied legal initial state and inert drawing/time dependencies; no constructor/game/UI/input/media proof.' })
exit(results.all? { |r| r[:observed_fields_match] } ? 0 : 1)
