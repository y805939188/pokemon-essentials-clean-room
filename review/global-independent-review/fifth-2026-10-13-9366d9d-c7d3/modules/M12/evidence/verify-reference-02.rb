require 'json'
module RPG
  class CommonEvent
    attr_accessor :list
    def initialize(list); @list = list; end
  end
  class EventCommand
    attr_accessor :code, :indent, :parameters
    def initialize(code, indent, parameters); @code = code; @indent = indent; @parameters = parameters; end
  end
end
load '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb'
fixtures = JSON.parse(File.read('/tmp/pokemon-gr5-c7d3/reference-execution-01/six-family-fixtures.json'))
rows = fixtures.map do |f|
  e = RPG::CommonEvent.new([
    RPG::EventCommand.new(111, 0, [12, f['input_compatibility_text'].dup]),
    RPG::EventCommand.new(0, 1, []),
    RPG::EventCommand.new(412, 0, []),
    RPG::EventCommand.new(0, 0, [])
  ])
  passes = []
  2.times do |n|
    begin
      changed = !!Compiler.fix_event_use(e, 0, nil)
      passes << {pass: n+1, business_status: 'returned', changed: changed,
                 exits: e.list.count { |c| c.code == 115 },
                 command_codes: e.list.map(&:code),
                 condition: e.list.find { |c| c.code == 111 }.parameters[1]}
    rescue Exception => err
      passes << {pass: n+1, business_status: 'exception', error_class: err.class.name, message: err.message}
      break
    end
  end
  {family: f['family'], mode: f['mode'], historical_expected_empty_branch_revisit: f['empty_branch_revisit'], passes: passes}
end
puts JSON.pretty_generate({ruby: RUBY_DESCRIPTION, results: rows})
