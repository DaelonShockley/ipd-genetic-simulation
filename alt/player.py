import random
import numpy as np

class Playeralt():
    def __init__(self, table_init_magnitude, rounds_per_game):
        self.opp_history_weight = np.random.uniform(-table_init_magnitude, table_init_magnitude, (rounds_per_game, 2))
        self.self_history_weight = np.random.uniform(-table_init_magnitude, table_init_magnitude, (rounds_per_game, 2))

    def get_decision(self, self_history, opp_history):
        '''
        get player decision, result of true means player will cooperate
        '''
        probabilities = []

        for i in (0, len(opp_history)):
            probabilities.append(self.opp_history_weight[i][int(opp_history[i])])

        for i in (0, len(self_history)):
            probabilities.append(self.self_history_weight[i][int(self_history[i])])

        odds = np.mean(probabilities)

        if random.random() <= odds:
            return True
        else:
            return False

    
        
    

    