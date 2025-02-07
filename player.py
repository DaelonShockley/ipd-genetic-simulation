import random
import numpy as np
import scipy.special

class Player():
    def __init__(self, table_init_magnitude, rounds_per_game):
        self.opp_history_weight = np.random.uniform(-table_init_magnitude/2, table_init_magnitude, (rounds_per_game, 2))
        self.self_history_weight = np.random.uniform(-table_init_magnitude/2, table_init_magnitude, (rounds_per_game, 2))

        self.total_score = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0

        self.num_defections = 0
        self.num_cooperations = 0

    def get_decision(self, self_history, opp_history):
        '''
        get player decision, result of true means player will defect
        '''
        probabilities = []

        if self_history == "":
            probabilities.append(self.opp_history_weight[0][0])
            probabilities.append(self.self_history_weight[0][0])
            odds = np.mean(probabilities)
            if random.random() <= odds:
                self.num_cooperations += 1
                return False #cooperate
            else:
                self.num_defections += 1
                return True #defect 

        for i in range(len(opp_history) + 1):
            probabilities.append(self.opp_history_weight[i-1][int(opp_history[-i])])

        for i in range(len(self_history) + 1):
            probabilities.append(self.self_history_weight[i-1][int(self_history[-i])])

        #odds = np.mean(probabilities)
        odds = scipy.special.expit(np.mean(probabilities))

        if random.random() <= odds:
            self.num_cooperations += 1
            return False #cooperate
        else:
            self.num_defections += 1
            return True #defect 
        
    def log(self):
        return [self.total_score, self.wins, self.losses, self.draws, self.num_defections/(self.num_defections + self.num_cooperations)]

    
        
    

    
