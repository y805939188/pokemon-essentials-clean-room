require 'json'
load '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb'
Command = Struct.new(:parameters, :indent)
inputs = {
  'normal_single_line' => 'pbWildBattle(:RATTATA, 5)',
  'preceding_line' => "false\npbWildBattle(:RATTATA, 5)",
  'following_line' => "pbWildBattle(:RATTATA, 5)\nfalse",
  'inline_prefix' => 'false; pbWildBattle(:RATTATA, 5)',
  'inline_suffix' => 'pbWildBattle(:RATTATA, 5); false',
  'empty_parentheses' => 'pbWildBattle()'
}
results = inputs.map do |id, input|
  list = [Command.new([12, input.dup], 0)]
  begin
    changed = Compiler.replace_old_battle_scripts(nil, list, 0)
    {id: id, input: input, changed: changed, result: list[0].parameters[1], list_count: list.length, business_status: 'returned'}
  rescue Exception => e
    {id: id, input: input, business_status: 'exception', class: e.class.name, message: e.message}
  end
end
puts JSON.pretty_generate({ruby: RUBY_DESCRIPTION, results: results})
