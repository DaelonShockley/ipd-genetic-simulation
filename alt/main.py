from player import Player
from game import Game
from genetic import Genetic
import time
import math

start_time = time.time()

table_init_magnitude = 1
rounds_per_game = 20
games_per_match = 2

score_both_coop = 3
score_both_def = 1
score_player_def = 5
score_opp_def = 0

population_size = 100
number_of_rounds = 500

record = False

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
    for i in range(0, 2):
        print("Opponent History Weight:")
        print(players[i].opp_history_weight)
        print("Self History Weight")
        print(players[i].self_history_weight)

        print(f"Total score after facing {population_size - 1} opponents {games_per_match} times")
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
        Game.run_single_game_interactive(sorted_players[0], sorted_players[1], rounds_per_game, score_both_coop, score_both_def, score_player_def, score_opp_def)

players = []
for _ in range(population_size):
    player = Player(table_init_magnitude, rounds_per_game)
    players.append(player)

rounds_run = 0

while(rounds_run < number_of_rounds):
    #run the round of matches between players
    gen_time = time.time()
    Game.run_round(players, rounds_per_game, games_per_match, score_both_coop, score_both_def, score_player_def, score_opp_def)

    players = Genetic.crossover(players, record)

    rounds_run += 1
    gen_end = time.time()
    gen_time_elapsed = gen_end - gen_time
    print(f"generation {rounds_run}/{number_of_rounds} completed in {gen_time_elapsed:.6f} seconds")

#one more round since we ended on a crossover phase
Game.run_round(players, rounds_per_game, games_per_match, score_both_coop, score_both_def, score_player_def, score_opp_def)

print_fittest()

run_game_top_two_players(3)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.6f} seconds")


