from player import Player
from itertools import combinations

class Game():
    @staticmethod
    def run_round(players: list[Player], num_games, rounds_per_game, score_both_coop, score_both_def, score_player_def, score_opp_def):
        """
        Run a round of games where each unique pair of players plays against each other multiple times.

        Parameters:
        players - list[Player]: List of Player objects participating in the round.
        num_games - int: Number of games each pair of players should play.
        rounds_per_game - int: Number of rounds per game.
        score_both_coop - int: Score when both players cooperate.
        score_both_def - int: Score when both players defect.
        score_player_def - int: Score for a player who defects when the opponent cooperates.
        score_opp_def - int: Score for a player who cooperates when the opponent defects.

        Returns:
        None. Updates player attributes in place.
        """
        #print("round beginning")

        for player1, player2 in combinations(players, 2):  # Iterate through all unique pairs of players
            for _ in range(num_games):  # Run num_games between the pair
                Game.run_single_game(
                    player1, 
                    player2, 
                    rounds_per_game, 
                    score_both_coop, 
                    score_both_def, 
                    score_player_def, 
                    score_opp_def
                )


    @staticmethod
    def run_single_game(player1: Player, player2: Player, rounds_per_game, score_both_coop, score_both_def, score_player_def, score_opp_def):
        '''
        Method to run a single prisoners dilemma game between two players

        Parameters:
        player1 - a player object participating in the game
        player2 - a player object participating in the game
        rounds_per_game - the number of rounds to be completed in the game
        score_both_coop - the score given to a player when both players choose to cooperate
        score_both_def - the score given to a player when both players choose to defect
        score_player_def - the score given to a player when the player chooses to defect and the opponent chooses to cooperate
        score_opp_def - the score given to a player when the player chooses to cooperate and the opponent chooses to defect

        Returns: 
        no returns; however, the total_score, wins, and draws, attributes of the player objects will be altered
        '''

        history_play_1 = "" #decisions of player 1
        history_play_2 = "" #decisions of player 2
        player1_defections = 0
        player2_defections = 0
        player1_score = 0
        player2_score = 0

        rounds_played = 0
        while(rounds_played < rounds_per_game):
            player1_decision = player1.get_decision(history_play_2, player2_defections, player1_defections, rounds_played, player1_score - player2_score)
            player2_decision = player2.get_decision(history_play_1, player1_defections, player2_defections, rounds_played, player2_score - player1_score)

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
        elif(player1_score == player2_score):
            player1.draws += 1
            player2.draws += 1
        else:
            player2.wins += 1

        #print("one game simulatied")




