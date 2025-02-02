from player import Player
from itertools import combinations

class Game():
    @staticmethod
    def run_round(players: list[Player], rounds_per_game, games_per_match, score_both_coop, score_both_def, score_player_def, score_opp_def):
        for player1, player2 in combinations(players, 2):  # Iterate through all unique pairs of players
            for _ in range(games_per_match):
                Game.run_single_game(player1, player2, rounds_per_game, score_both_coop, score_both_def, score_player_def, score_opp_def)

    @staticmethod
    def run_single_game(player1, player2, rounds_per_game, score_both_coop, score_both_def, score_player_def, score_opp_def):
        history_play_1 = "" #decisions of player 1
        history_play_2 = "" #decisions of player 2
        player1_score = 0
        player2_score = 0

        rounds_played = 0
        while(rounds_played < rounds_per_game):
            player1_decision = player1.get_decision(history_play_1, history_play_2)
            player2_decision = player2.get_decision(history_play_2, history_play_1)

            #remember that a decision of True means the player is defecting, similarly a "1" in the history represents a defection
            if(not player1_decision and not player2_decision): #both players cooperate
                player1_score += score_both_coop
                player2_score += score_both_coop
                history_play_1 += "0"
                history_play_2 += "0"
            elif(player1_decision and not player2_decision): #player1 defects, player2 cooperates
                player1_score += score_player_def
                player2_score += score_opp_def
                history_play_1 += "1"
                history_play_2 += "0"
            elif(not player1_decision and player2_decision): #player1 cooperates, player2 defects
                player1_score += score_opp_def
                player2_score += score_player_def
                history_play_1 += "0"
                history_play_2 += "1"
            else: #both players defect
                player1_score += score_both_def
                player2_score += score_both_def
                history_play_1 += "1"
                history_play_2 += "1"

            rounds_played += 1

        player1.total_score += player1_score
        player2.total_score += player2_score

        if(player1_score > player2_score):
            player1.wins += 1
            player2.losses += 1
        elif(player1_score == player2_score):
            player1.draws += 1
            player2.draws += 1
        else:
            player2.wins += 1
            player1.losses += 1

    @staticmethod
    def run_single_game_interactive(player1, player2, rounds_per_game, score_both_coop, score_both_def, score_player_def, score_opp_def):
        history_play_1 = "" #decisions of player 1
        history_play_2 = "" #decisions of player 2
        player1_score = 0
        player2_score = 0

        rounds_played = 0
        while(rounds_played < rounds_per_game):
            player1_decision = player1.get_decision(history_play_1, history_play_2)
            player2_decision = player2.get_decision(history_play_2, history_play_1)

            #remember that a decision of True means the player is defecting, similarly a "1" in the history represents a defection
            if(not player1_decision and not player2_decision): #both players cooperate
                player1_score += score_both_coop
                player2_score += score_both_coop
                history_play_1 += "0"
                history_play_2 += "0"
                print("Both players cooperate")
                print(f"Player 1: {history_play_1} - total score: {player1_score}")
                print(f"Player 1: {history_play_2} - total score: {player2_score}")
            elif(player1_decision and not player2_decision): #player1 defects, player2 cooperates
                player1_score += score_player_def
                player2_score += score_opp_def
                history_play_1 += "1"
                history_play_2 += "0"
                print("Player 1 defects, Player 2 cooperates!")
                print(f"Player 1: {history_play_1} - total score: {player1_score}")
                print(f"Player 1: {history_play_2} - total score: {player2_score}")
            elif(not player1_decision and player2_decision): #player1 cooperates, player2 defects
                player1_score += score_opp_def
                player2_score += score_player_def
                history_play_1 += "0"
                history_play_2 += "1"
                print("Player 1 cooperates, Player 2 defects!")
                print(f"Player 1: {history_play_1} - total score: {player1_score}")
                print(f"Player 1: {history_play_2} - total score: {player2_score}")
            else: #both players defect
                player1_score += score_both_def
                player2_score += score_both_def
                history_play_1 += "1"
                history_play_2 += "1"
                print("Both players defect!")
                print(f"Player 1: {history_play_1} - total score: {player1_score}")
                print(f"Player 1: {history_play_2} - total score: {player2_score}")

            rounds_played += 1

        player1.total_score += player1_score
        player2.total_score += player2_score

        if(player1_score > player2_score):
            print("\nPlayer 1 wins!\n")
            player1.wins += 1
            player2.losses += 1
        elif(player1_score == player2_score):
            print("\nIt's a draw\n")
            player1.draws += 1
            player2.draws += 1
        else:
            print("\nPlayer 2 wins!\n")
            player2.wins += 1
            player1.losses += 1

