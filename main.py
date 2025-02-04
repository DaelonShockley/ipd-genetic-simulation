from player import Player
from game import Game
from genetic import Genetic
import time
import math
import csv

start_time = time.time()

table_init_magnitude = 1
rounds_per_game = 20
games_per_match = 100

score_both_coop = 3
score_both_def = 1
score_player_def = 5
score_opp_def = 0

population_size = 100
number_of_rounds = 20

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
    for i in range(3):
        print("Opponent History Weight:")
        print(players[i].opp_history_weight)
        print("Self History Weight")
        print(players[i].self_history_weight)

        print(f"Total score after facing {population_size - 1} opponents {games_per_match} times")
        print(sorted_players[i].total_score)
        print("Player defection rate:")
        print(sorted_players[i].num_defections/(sorted_players[i].num_defections + sorted_players[i].num_cooperations))
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

def log_generation():
    total_defection_rate = 0
    highest_defection = 0
    lowest_defection = 1

    total_wins = 0
    total_losses = 0
    total_draws = 0

    total_score = 0
    highest_score = 0
    lowest_score = 5000000

    for player in players: 
        stats = player.log()

        total_score += stats[0]
        total_wins += stats[1]
        total_losses += stats[2]
        total_draws += stats[3]
        total_defection_rate += stats[4]

        if stats[4] > highest_defection:
            highest_defection = stats[4]
        elif stats[4] < lowest_defection:
            lowest_defection = stats[4]

        if stats[0] > highest_score:
            highest_score = stats[0]
        elif stats[0] < lowest_score:
            lowest_score = stats[0]

    with open("final_results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        #[generation, highest_score, average_score, lowest_score, total_wins, total_losses, total_draws, highest_defection_rate, average_defection_rate, lowest_defection_rate]
        writer.writerow([rounds_run, highest_score, total_score/100, lowest_score, total_wins, total_losses, total_draws, highest_defection, total_defection_rate/100, lowest_defection])


players = []
for _ in range(population_size):
    player = Player(table_init_magnitude, rounds_per_game)
    players.append(player)

rounds_run = 0

while(rounds_run < number_of_rounds):
    #run the round of matches between players
    gen_time = time.time()
    Game.run_round(players, rounds_per_game, games_per_match, score_both_coop, score_both_def, score_player_def, score_opp_def)

    log_generation()

    players = Genetic.crossover(players, record)

    rounds_run += 1
    gen_end = time.time()
    gen_time_elapsed = gen_end - gen_time
    print(f"generation {rounds_run}/{number_of_rounds} completed in {gen_time_elapsed:.6f} seconds")

#one more round since we ended on a crossover phase
Game.run_round(players, rounds_per_game, games_per_match, score_both_coop, score_both_def, score_player_def, score_opp_def)
log_generation()

print_fittest()

run_game_top_two_players(5)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.6f} seconds")


