import random
import numpy as np

class Playeralt():
    def __init__(self, table_init_magnitude, rounds_per_game):
        self.opp_history_weight = np.random.uniform(-table_init_magnitude, table_init_magnitude, (rounds_per_game, 2))
        self.self_history_weight = np.random.uniform(-table_init_magnitude, table_init_magnitude, (rounds_per_game, 2))

    def get_decision(self, player_history, opp_history){

    }

    