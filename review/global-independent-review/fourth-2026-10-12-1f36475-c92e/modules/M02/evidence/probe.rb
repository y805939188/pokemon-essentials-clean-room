require 'json'
REF = '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts'
module HTTPLite
  @calls = []
  class << self
    attr_reader :calls
    def post_body(*args)
      @calls << args
      { status: 200, body: 'OK' }
    end
  end
end
load File.join(REF, '001_Technical/002_Files/003_HTTP_Utilities.rb')
load File.join(REF, '019_Utilities/001_Utilities.rb')
load File.join(REF, '004_Game classes/001_Switches and Variables/003_Game_Variables.rb')
def pbGetTimeNow
  Time.at($probe_time)
end
class ProbeMap
  attr_reader :refreshes
  def initialize; @refreshes = 0; end
  def refresh; @refreshes += 1; end
end
results = []
def measure(results, id)
  before = HTTPLite.calls.length
  begin
    result = yield
    results << { id: id, result: result, http_calls: HTTPLite.calls.length - before }
  rescue => e
    results << { id: id, error: e.class.name, message: e.message, http_calls: HTTPLite.calls.length - before }
  end
end
measure(results, 'POST-string-key-safe') { pbPostData('http://example.invalid/', { 'k' => 'a_b.-9' }) }
measure(results, 'POST-symbol-safe') { pbPostData('http://example.invalid/', { :k => 'a_b.-9' }) }
measure(results, 'POST-symbol-space') { pbPostData('http://example.invalid/', { :k => 'a b' }) }
measure(results, 'POST-symbol-space-convenience') { pbPostToString('http://example.invalid/', { :k => 'a b' }) }
measure(results, 'POST-space-value') { pbPostData('http://example.invalid/', { 'k' => 'a b' }) }
measure(results, 'POST-space-key') { pbPostData('http://example.invalid/', { 'a b' => 'x' }) }
measure(results, 'POST-space-convenience') { pbPostToString('http://example.invalid/', { 'k' => 'a b' }) }
measure(results, 'POST-https') { pbPostData('https://example.invalid/', { 'k' => 'a b' }) }
[99, 100, 101].each do |elapsed|
  $game_variables = Game_Variables.new
  $game_map = ProbeMap.new
  $probe_time = 1000
  pbTimeEvent(1, 100)
  stored = $game_variables[1].dup
  $probe_time += elapsed
  valid = pbTimeEventValid(1)
  results << { id: "TIME-elapsed-#{elapsed}", initial: stored, valid: valid, final: $game_variables[1], refreshes: $game_map.refreshes }
end
$game_variables = Game_Variables.new
$game_map = ProbeMap.new
$probe_time = 1000
pbTimeEvent(1, 100)
$probe_time = 1050
first = pbTimeEventValid(1)
$probe_time = 1101
second = pbTimeEventValid(1)
results << { id: 'TIME-early-query-then-late', first: first, second: second, final: $game_variables[1] }
[0, -5].each do |duration|
  $probe_time = 1000
  pbTimeEvent(1, duration)
  $probe_time = 2000
  results << { id: "TIME-duration-#{duration}", valid: pbTimeEventValid(1), final: $game_variables[1] }
end
$probe_time = 1728000100
pbTimeEventDays(1, 1)
stored = $game_variables[1].dup
results << { id: 'TIME-days-1', initial: stored, valid: pbTimeEventValid(1), final: $game_variables[1] }
puts JSON.pretty_generate({ ruby: RUBY_DESCRIPTION, results: results, http_arguments: HTTPLite.calls })
