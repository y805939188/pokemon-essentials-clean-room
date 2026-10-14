require "json"
module SaveData
  def self.register_conversion(id, &block)
    return unless id == :v20_rename_bag_variables
    collector = Object.new
    def collector.essentials_version(value); end
    def collector.display_title(value); end
    def collector.to_value(key, &block); SaveData.instance_variable_set(:@captured, block); end
    collector.instance_eval(&block)
  end
  def self.captured; @captured; end
end
load "reference/pokemon-essentials/Data/Scripts/002_Save data/005_Game_SaveConversions.rb"
bag = Object.new
bag.instance_variable_set(:@lastpocket, 2)
bag.instance_variable_set(:@lastPocket, 8)
bag.instance_variable_set(:@last_viewed_pocket, 3)
SaveData.captured.call(bag)
first = [bag.instance_variable_get(:@lastpocket), bag.instance_variable_get(:@lastPocket), bag.instance_variable_get(:@last_viewed_pocket)]
bag.instance_variable_set(:@last_viewed_pocket, 5)
SaveData.captured.call(bag)
second = [bag.instance_variable_get(:@lastpocket), bag.instance_variable_get(:@lastPocket), bag.instance_variable_get(:@last_viewed_pocket)]
puts JSON.generate({evidence: "TOOL_VALIDATION", host: "isolated local Ruby; no game/RGSS; registration collector plus bare object", first: first, second: second, file_operations: "reference file read only; no save IO"})
