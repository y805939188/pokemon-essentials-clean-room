require 'json'
def nil_or_empty?(value)
  value.nil? || value.empty?
end
def hasConst?(owner, name)
  owner.const_defined?(name)
end
def getConst(owner, name)
  owner.const_get(name)
end
reference_root = '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials'
load File.join(reference_root, 'Data/Scripts/021_Compiler/001_Compiler.rb')
load File.join(reference_root, 'Data/Scripts/001_Technical/003_Intl_Messages.rb')
fixtures = {
  'distinct_keys' => "[24]\nK\nFirst\nL\nOther\n",
  'duplicate_key' => "[24]\nK\nFirst\nK\nLast\n",
  'normalized_collision' => "[24]\nA  B\nFirst\nA B\nLast\n",
  'repeated_hash_section' => "[24]\nK\nFirst\nL\nOther\n[24]\nK\nLast\nM\nNew\n",
  'repeated_array_section' => "[24]\n0\nOriginal0\nFirst\n2\nOriginal2\nKeep\n[24]\n0\nOriginal0\nLast\n",
  'array_then_hash' => "[24]\n0\nOriginal\nFirst\n[24]\nK\nLast\n",
  'hash_then_array' => "[24]\nK\nFirst\n[24]\n0\nOriginal\nLast\n"
}
results = []
fixtures.each do |id, input|
  path = File.join(__dir__, id + '.txt')
  File.write(path, input)
  all_text = []
  begin
    Translator.compile_text_from_file(path, all_text)
    results << {id: id, result: all_text[24], exception: nil}
  rescue StandardError => error
    results << {id: id, result: all_text[24], exception: error.class.name, message: error.message}
  end
end
backslash_ampersand = [92,38].pack('U*')
backslash_one = [92,49].pack('U*')
results << {id: 'plain_parameter', result: _INTL('X{1}Y', 'Q')}
results << {id: 'ampersand_parameter', result: _INTL('X{1}Y', backslash_ampersand)}
results << {id: 'one_parameter', result: _INTL('X{1}Y', backslash_one)}
results << {id: 'map_ampersand_parameter', result: _MAPINTL(5, 'X{1}Y', backslash_ampersand)}
results << {id: 'formatted_ampersand_parameter', result: _ISPRINTF('X{1:s}Y', backslash_ampersand)}
puts JSON.pretty_generate(results)
