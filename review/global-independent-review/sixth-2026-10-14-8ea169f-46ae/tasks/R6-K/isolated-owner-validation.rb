require "json"
load "reference/pokemon-essentials/Data/Scripts/001_Technical/001_Debugging/004_Validation.rb"
load "reference/pokemon-essentials/Data/Scripts/014_Pokemon/005_Pokemon_Owner.rb"
results=[]
[[0,0,0,2],[1,0,0,2],[1,0,1,2],[0,"Valid",0,2]].each do |args|
  begin
    owner=Pokemon::Owner.new(*args)
    results << {args: args,result: "constructed",name: owner.name,name_class: owner.name.class.name}
  rescue => e
    results << {args: args,result: "rejected",error_class: e.class.name}
  end
end
owner=Pokemon::Owner.new(0,"Valid",0,2)
begin
 owner.name=0
 results << {action:"set name 0",result:"accepted"}
rescue=>e
 results << {action:"set name 0",result:"rejected",error_class:e.class.name,name:owner.name}
end
puts JSON.generate({evidence:"TOOL_VALIDATION",host:"isolated local Ruby; loaded validation and owner definitions; no game/RGSS or save IO",results:results})
