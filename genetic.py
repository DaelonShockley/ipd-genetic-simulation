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
        
        #copy the previous rounds most fit into the new population, resetting stats
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

        for i in range(0, len(player1.opp_history_weight)):
            new_player.opp_history_weight[i] = random.choices([player1.opp_history_weight[i], player2.opp_history_weight[i]], weights=weights, k=1)[0]
            new_player.self_history_weight[i] = random.choices([player1.self_history_weight[i], player2.self_history_weight[i]], weights=weights, k=1)[0]

        new_player.total_score = 0
        new_player.wins = 0
        new_player.losses = 0
        new_player.draws = 0

        return new_player
    
    @staticmethod
    def introduce_mutation(new_player: Player, mutation_rate, max_mutation_magnitude):
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
        new_player.opp_history_weight = [
            mutate_value(val) for val in new_player.opp_history_weight
        ]

        new_player.self_history_weight = [
            mutate_value(val) for val in new_player.self_history_weight
        ]

        return new_player