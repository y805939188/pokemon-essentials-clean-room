# Syntax parsing only. No reference code execution; no semantic PASS emission.
require 'open3'
require 'json'
require 'digest'
repo = '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials'
rev = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
out = '/Users/dingshinn/Desktop/pokemon-framework-reference/review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-UI/structural-inventory.json'
listing, err, status = Open3.capture3('git', '-C', repo, 'ls-tree', '-r', '--name-only', rev, '--', 'Data/Scripts/016_UI')
raise err unless status.success?
rows = []
listing.lines.map(&:strip).each do |path|
  bytes, err, status = Open3.capture3('git', '-C', repo, 'show', "#{rev}:#{path}")
  raise err unless status.success?
  ast = RubyVM::AbstractSyntaxTree.parse(bytes)
  visit = lambda do |node|
    if node.is_a?(RubyVM::AbstractSyntaxTree::Node)
      if [:DEFN, :DEFS, :CLASS, :MODULE].include?(node.type)
        name = node.type == :DEFN ? node.children[0].to_s : node.type == :DEFS ? node.children[1].to_s : bytes.lines[node.first_lineno-1].strip
        rows << {path: path, commit: rev, sha256: Digest::SHA256.hexdigest(bytes), kind: node.type.to_s, name: name, start_line: node.first_lineno, end_line: node.last_lineno, stage: 'structure_parsed_only', semantic_status: 'NOT_ASSIGNED_BY_PARSER'}
      end
      node.children.each { |child| visit.call(child) }
    elsif node.is_a?(Array)
      node.each { |child| visit.call(child) }
    end
  end
  visit.call(ast)
end
File.write(out, JSON.pretty_generate(rows) + "\n")
puts JSON.generate({output: out, files: listing.lines.length, units: rows.length, stage: 'structure_parsed_only'})
