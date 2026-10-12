require 'json'
load '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/004_ChallengeGenerator_BattleSim.rb'

def fixture(cumulative, count)
  rating = PlayerRating.new
  history = MatchHistory.new(rating)
  opponent = PlayerRating.new
  count.times { history.addMatch(opponent, -1) }
  team = RuledTeam.allocate
  team.instance_variable_set(:@totalGames, cumulative)
  team.instance_variable_set(:@rating, rating)
  team.instance_variable_set(:@history, history)
  team
end

def state(team)
  { settled: team.instance_variable_get(:@totalGames), pending: team.games,
    visible: team.totalGames, rating: team.ratingRaw }
end

results = []
[[70, 12], [238, 12], [70, 0]].each do |cumulative, count|
  team = fixture(cumulative, count)
  before = state(team)
  team.updateRating
  after = state(team)
  raise 'count conservation failed' unless after[:settled] == cumulative + count && after[:pending] == 0 && after[:visible] == before[:visible]
  if count == 0
    raise 'empty history deviation mismatch' unless (after[:rating][1] - 383.332855).abs < 0.000001
  end
  results << { input: {cumulative: cumulative, count: count, score: -1}, before: before, after: after }
end
team = fixture(70, 12)
team.updateRating
12.times { team.addMatch(fixture(0, 0), -1) }
team.updateRating
raise 'second settlement failed' unless team.totalGames == 94 && team.games == 0
results << { input: 'second batch of 12 draws after 70+12', after: state(team) }
[-1, 1].each do |score|
  rating = PlayerRating.new
  opponent = PlayerRating.new
  history = MatchHistory.new(rating)
  history.addMatch(opponent, score)
  history.updateAndClear
  raise 'history not cleared' unless history.length == 0
  results << { input: {initial_rating: 1500, initial_deviation: 350, initial_volatility: 0.9, score: score}, output: {rating: rating.rating, deviation: rating.deviation, volatility: rating.volatility} }
end
puts JSON.pretty_generate(results)
