from player import Player
from game import Game
from genetic import Genetic
import math
 
table_init_magnitude = 1
mod_init_magnitude = 0.01
rounds_per_game = 20
matches_per_round = 2

score_both_coop = 3
score_both_def = 1
score_player_def = 5
score_opp_def = 0

population_size = 100
fittest_gene_prob = .5 #the probability that a gene is taken from the more fit parent

mutation_rate = 0.01 
max_mutation_magnitude = .2

number_of_rounds = 250

player_memory = 5

record = False #should fittest be decided by record rather than total score? 

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

def print_fittest():
    fittest_size = int(math.sqrt(len(players)))

    if record:
        # Sort by wins first, then by draws, then by total_score
        sorted_players = sorted(players, key=lambda p: (p.wins, p.draws, p.total_score), reverse=True)
    else:
        # Sort by total_score first, then by wins, then by draws
        sorted_players = sorted(players, key=lambda p: (p.total_score, p.wins, p.draws), reverse=True)

    sorted_players = sorted_players[:fittest_size]

    print(f"TOP {fittest_size} ALGORITHMS AFTER {number_of_rounds} ROUNDS OF SIMULATION")
    for i in range(0, len(sorted_players)):
        print(f"rank {i+1} player")
        print("Decision matrix: ")
        print(sorted_players[i].decision_matrix)
        print("Total Opponent Defection Weight:")
        print(sorted_players[i].total_opp_defection_weight)
        print("Total Opponent Defection Rate Weight:")
        print(sorted_players[i].opp_defection_rate_weight)
        print("Total Player Defection Weight:")
        print(sorted_players[i].total_player_defections_weight)
        print("Total Player Defection Rate Weight:")
        print(sorted_players[i].total_player_defections_weight)
        print("Rounds Played Weight:")
        print(sorted_players[i].rounds_played_weight)
        print("Rounds Left Weight:")
        print(sorted_players[i].rounds_left_weight)
        print("Score Differential Weight:")
        print(sorted_players[i].score_diff_weight)
        print("Opponent Defected Last Round Weight:")
        print(sorted_players[i].opp_def_prev_round_weight)
        print("Player Defected Last Round Weight:")
        print(sorted_players[i].player_def_prev_round_weight)
        print("\n")
        print(f"Total score after facing {population_size - 1} opponents {matches_per_round} times")
        print(sorted_players[i].total_score)
        print("Player record:")
        print(f"{sorted_players[i].wins} - {sorted_players[i].losses} - {sorted_players[i].draws}")
        print("\n")

def run_game_top_two_players(games):
    fittest_size = int(math.sqrt(len(players)))

    if record:
        # Sort by wins first, then by draws, then by total_score
        sorted_players = sorted(players, key=lambda p: (p.wins, p.draws, p.total_score), reverse=True)
    else:
        # Sort by total_score first, then by wins, then by draws
        sorted_players = sorted(players, key=lambda p: (p.total_score, p.wins, p.draws), reverse=True)

    sorted_players = sorted_players[:fittest_size]

    for i in range(games):
        Game.run_single_game_adv_interactive(sorted_players[0], sorted_players[1], rounds_per_game, score_both_coop, score_both_def, score_player_def, score_opp_def)

players = []
for _ in range(population_size):
    player = Player(player_memory, table_init_magnitude, mod_init_magnitude, rounds_per_game, 
                    score_both_coop, score_both_def, score_player_def, score_opp_def)
    players.append(player)

rounds_run = 0

while(rounds_run < number_of_rounds):
    #run the round of matches between players
    Game.run_round(players, matches_per_round, rounds_per_game, score_both_coop, score_both_def, score_player_def, score_opp_def)

    players = Genetic.crossover(players, record, fittest_gene_prob, mutation_rate, max_mutation_magnitude)

    rounds_run += 1

#one more round since we ended on a crossover phase
Game.run_round(players, matches_per_round, rounds_per_game, score_both_coop, score_both_def, score_player_def, score_opp_def)

print_fittest()

run_game_top_two_players(3)







