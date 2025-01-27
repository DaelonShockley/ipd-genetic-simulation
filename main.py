from player import Player
from game import Game
 
table_init_magnitude = 1
mod_init_magnitude = 0.01
rounds_per_game = 20
matches_per_round = 1

score_both_coop = 3
score_both_def = 1
score_player_def = 5
score_opp_def = 0

population_size = 100
fittest_gene_prob = .5 #the probability that a gene is taken from the more fit parent

'''
player1 = Player(1, 0.01, 20, 2, 1, 3, 0)

print(player1.decision_matrix)
print(player1.total_opp_defection_weight)
print(player1.opp_defection_rate_weight)
print(player1.total_player_defections_weight)
print(player1.total_player_defections_weight)
print(player1.rounds_played_weight)
print(player1.rounds_left_weight)
print(player1.score_diff_weight)
print("\n")
player1.total_score += 1
player1.wins += 1
print(player1.rounds_per_game)
print(player1.total_score)
print(player1.wins)
print("\n")
print(player1.score_both_coop)
print(player1.score_both_def)
print(player1.score_player_def)
print(player1.score_opp_def)

print(player1.get_decision("01", 2, 3, 5, 2))
'''

players = []
for _ in range(population_size):
    player = Player(table_init_magnitude, mod_init_magnitude, rounds_per_game, 
                    score_both_coop, score_both_def, score_player_def, score_opp_def)
    players.append(player)

Game.run_round(players, matches_per_round, rounds_per_game, score_both_coop, score_both_def, score_player_def, score_opp_def)

for player in players:
    print(player.total_score)
    print(player.wins)
