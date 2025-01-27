import random
from player import Player
import math
from itertools import combinations
import copy

class Genetic():
    @staticmethod
    def crossover(players: list[Player], record = False, fitter_gene_prob = .5, mutation_rate = 0.01, max_mutation_magnitude = .2):
        '''
        This function will find the most fit members of the population, crossing them with each other twice in order to produce a new population the same size of the original
        
        Parameters: 
        players - a list of the players creating the simulation population. The length of this list must be a perfect square
        record - a boolean, if true the fittest will be selected based on their number of wins rather than total score
        fitter_gene_prob - the probability that a given "gene" will come from the fitter of the two parent players

        Returns: 
        new_players - a list of player objects the same size as the players input
        '''

        fittest_size = int(math.sqrt(len(players)))

        if record:
        # Sort by wins first, then by draws, then by total_score
            sorted_players = sorted(players, key=lambda p: (p.wins, p.draws, p.total_score), reverse=True)
        else:
        # Sort by total_score first, then by wins, then by draws
            sorted_players = sorted(players, key=lambda p: (p.total_score, p.wins, p.draws), reverse=True)

        

        sorted_players = sorted_players[:fittest_size]
        
        new_players = []
        for player in sorted_players:
            new_player = copy.deepcopy(player)
            new_player.total_score = 0
            new_player.wins = 0
            new_player.losses = 0
            new_player.draws = 0
            new_players.append(new_player)

        for player1, player2 in combinations(sorted_players, 2):  # Iterate through all unique pairs of players
            for _ in range(2): #two offspring per combination
                new_player = Genetic.single_crossover(player1, player2, fitter_gene_prob)
                new_players.append(Genetic.introduce_mutation(new_player, mutation_rate, max_mutation_magnitude))

        #to do: introduce mutations to new_players

        return new_players

    @staticmethod
    def single_crossover(player1: Player, player2: Player, fitter_gene_prob):
        '''
        This function creates a new player object which is a cross of the two given

        inputs: 
        player1 - a player object which will be one parent of the new player object
        player2 - a player object which will be one parent of the new player object
        fitter_gene_prob - the probability that a given gene will come from the fitter parent (player1 in this case)

        output:
        new_player - a player object which is a cross between player1 and player 2
        '''

        weights = [fitter_gene_prob, 1-fitter_gene_prob]

        new_player = copy.deepcopy(player1)

        for i in range(0, len(player1.decision_matrix)):
            new_player.decision_matrix[i] = random.choices([player1.decision_matrix[i], player2.decision_matrix[i]], weights=weights, k=1)[0]

        new_player.total_opp_defection_weight = random.choices([player1.total_opp_defection_weight, player2.total_opp_defection_weight], weights=weights, k=1)[0]
        new_player.opp_defection_rate_weight = random.choices([player1.opp_defection_rate_weight, player2.opp_defection_rate_weight], weights=weights, k=1)[0]
        new_player.total_player_defections_weight =random.choices([player1.total_player_defections_weight, player2.total_player_defections_weight], weights=weights, k=1)[0]
        new_player.player_defection_rate_weight =random.choices([player1.player_defection_rate_weight, player2.player_defection_rate_weight], weights=weights, k=1)[0]
        new_player.rounds_played_weight =random.choices([player1.rounds_played_weight, player2.rounds_played_weight], weights=weights, k=1)[0]
        new_player.rounds_left_weight =random.choices([player1.rounds_left_weight, player2.rounds_left_weight], weights=weights, k=1)[0]
        new_player.score_diff_weight =random.choices([player1.score_diff_weight, player2.score_diff_weight], weights=weights, k=1)[0]

        new_player.total_score = 0
        new_player.wins = 0
        new_player.losses = 0
        new_player.draws = 0

        return new_player
    
    @staticmethod
    def introduce_mutation(new_player, mutation_rate, max_mutation_magnitude):
        '''
        Introduces mutations to the decision matrix and weight attributes of a player.
        
        Parameters:
        new_player - the player object to mutate
        max_mutation_magnitude - the maximum percentage change for a mutation
        mutation_rate - the probability of each gene or weight mutating
        
        Returns:
        new_player - the mutated player object
        '''
        def mutate_value(value):
            if random.random() < mutation_rate:
                # Randomly increase or decrease by up to max_mutation_magnitude%
                mutation_factor = 1 + random.uniform(-max_mutation_magnitude, max_mutation_magnitude)
                return value * mutation_factor
            return value

        # Mutate the decision matrix
        new_player.decision_matrix = [
            mutate_value(val) for val in new_player.decision_matrix
        ]

        # Mutate all weight attributes
        new_player.total_opp_defection_weight = mutate_value(new_player.total_opp_defection_weight)
        new_player.opp_defection_rate_weight = mutate_value(new_player.opp_defection_rate_weight)
        new_player.total_player_defections_weight = mutate_value(new_player.total_player_defections_weight)
        new_player.player_defection_rate_weight = mutate_value(new_player.player_defection_rate_weight)
        new_player.rounds_played_weight = mutate_value(new_player.rounds_played_weight)
        new_player.rounds_left_weight = mutate_value(new_player.rounds_left_weight)
        new_player.score_diff_weight = mutate_value(new_player.score_diff_weight)

        return new_player
