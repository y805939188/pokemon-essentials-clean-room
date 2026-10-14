# Local audit harness. Only these fixed, already-read class ranges are evaluated.
# No files, media, saves, network, or host game are loaded by the evaluated ranges.
require 'open3'
require 'digest'
require 'json'
repo = '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials'
rev = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
path = 'Data/Scripts/016_UI/023_UI_PurifyChamber.rb'
source, error, status = Open3.capture3('git', '-C', repo, 'show', "#{rev}:#{path}")
raise error unless status.success?
raise 'input hash mismatch' unless Digest::SHA256.hexdigest(source) == '84b1ef76c669575d606c1200f678d58c35912f02873764233595419c2110509d'

class Sprite
  attr_accessor :bitmap, :visible, :x, :y, :z, :pokemon, :viewport, :angle
  def initialize(viewport = nil)
    @viewport = viewport
    @x = @y = @z = @angle = 0
  end
end
class FakeBitmap
  attr_reader :width, :height
  def initialize(w, h); @width = w; @height = h; end
  def fill_rect(*); end
end
class BitmapSprite < Sprite
  def initialize(w, h, viewport = nil)
    super(viewport)
    @bitmap = FakeBitmap.new(w, h)
  end
end
class PokemonIconSprite < Sprite
  def initialize(*); super(nil); end
  def setOffset(*); end
end
module Graphics
  def self.width; 512; end
  def self.height; 384; end
end
class Color
  def self.white; new; end
  def self.new(*); Object.new; end
end
class PurifyChamber
  SETSIZE = 4
end
def pbSetSmallFont(*); end
def pbDrawTextPositions(*); end

lines = source.lines
eval(lines[38...47].join, TOPLEVEL_BINDING, path, 39)
eval(lines[675...743].join, TOPLEVEL_BINDING, path, 676)
eval(lines[833...1067].join, TOPLEVEL_BINDING, path, 834)

empty_chamber = Object.new
def empty_chamber.getShadow(*); nil; end
def empty_chamber.setCount(*); 0; end
def empty_chamber.setList(*); []; end

ordinary = DirectFlowDiagram.new
ordinary.setAngle(90)
puts JSON.generate({case: 'ordinary_explicit_angle', result: ordinary.instance_variable_get(:@angle), evidence_mode: 'isolated_actual_reference', hostDemo: false})
begin
  view = PurifyChamberSetView.new(empty_chamber, 0)
  raise 'host angle reader did not resolve' unless view.instance_variable_get(:@directflow).instance_variable_get(:@angle) == 0
  puts JSON.generate({case: 'empty_set_view_initial_refresh_with_sprite_angle_contract', result: 'refresh completed', refutation: 'Before the later local assignment, angle resolves the inherited Sprite angle reader. Earlier NameError came from incomplete host stub.', source_ranges: [[39,47],[676,743],[834,1067]], evidence_mode: 'isolated_actual_reference', stubbed_host_angle: 0, no_stateful_game_loaded: true, hostDemo: false})
end
