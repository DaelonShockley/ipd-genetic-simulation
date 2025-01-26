import random

class Player():
    def __init__(self, table_init_magnitude, mod_init_magnitude, rounds_per_game, score_both_coop, score_both_def, score_player_def, score_opp_def):
        #initializes decision matrix with a probability of +/- table_init_weight
        self.decision_matrix = self.initialize_decision_matrix(self.decision_matrix, table_init_magnitude)
        #initializes all modifier weights to +/- mod_init_magnitude
        self.total_opp_defection_weight = self.initialize_weight(mod_init_magnitude)
        self.opp_defection_rate_weight = self.initialize_weight(mod_init_magnitude)
        self.total_player_defections_weight = self.initialize_weight(mod_init_magnitude)
        self.player_defection_rate_weight = self.initialize_weight(mod_init_magnitude)
        self.rounds_played_weight = self.initialize_weight(mod_init_magnitude)
        self.rounds_left_weight = self.initialize_weight(mod_init_magnitude)
        self.score_diff_weight = self.initialize_weight(mod_init_magnitude)

        self.rounds_per_game = rounds_per_game
        self.total_score = 0
        self.wins = 0

        self.score_both_coop = score_both_coop
        self.score_both_def = score_both_def
        self.score_player_def = score_both_def
        self.score_opp_def = score_opp_def

    def initialize_decision_matrix(array, magnitude):
        """
        fills an empty array with 32 random decimals between 0 and 1

        Parameters: 
        array (list): an empty array to be filled with decimal values
        magnitude (float): the maximum value which a decimal in the array can be

        returns:
        none - the array is modified in place
        """
        for _ in range(32):
            array.append(random.uniform(0, magnitude))

    def initialize_weight(magnitude):
        """
        fills an empty array with 32 random decimals between 0 and 1

        Parameters: 
        magnitude (float): the maximum magnitude of the value which will be returned

        returns:
        float - a value between -magnitude and +magnitude
        """
        return random.uniform(-magnitude, magnitude)
    
    def get_decision(self, history, total_opp_defection, total_player_defection, rounds_played, score_diff):
        """
        gets the decision of the player based off the decision matrix and modifier weights given game history and ongoing values

        Parameters: 
        history (sting) - a string representing the opponents decisions for each round, where 1 represents defection and 0 represents cooperation (ex: "00010). 
        Only the last 5 rounds will be directly considered in this simulation, but you could change that by modifying this class. 
        total_opp_defection (integer) - the number of times the opponent has defected in the entire game
        total_player_defection (integer) - the number of times the player has defected in the entire game
        rounds_played (integer) - the number of rounds played until this point
        score_diff (integer) - the difference between the player score and the opponenets score 

        returns:
        defect (boolean) - true represents that the player will defect, while false represents that the player will cooperate
        """

        opp_defection_rate = total_opp_defection / rounds_played
        player_defection_rate = total_player_defection / rounds_played
        rounds_left = self.rounds_per_game - rounds_played

        #the history is given as a binary string, so we can convert that string to decimal in order to get the index of the corresponding 
        #probability from the decision matrix
        ind = self.binary_to_decimal(history)
        table_p = self.decision_matrix[ind]

        # Normalize the modifiers' contributions to ensure all modifiers have the same impact
        max_opp_defection = self.rounds_per_game  
        max_player_defection = self.rounds_per_game
        max_rounds_played = self.rounds_per_game
        max_rounds_left = self.rounds_per_game
        max_score_diff = self.rounds_per_game * self.score_player_def  #Assuming the most points are awarded for defecting when the opponent cooperates

        #find the probability that the player will cooperate
        # Apply normalized contributions for each modifier term
        decision_p = table_p
        decision_p += (total_opp_defection / max_opp_defection) * self.total_opp_defection_weight
        decision_p += (opp_defection_rate) * self.opp_defection_rate_weight
        decision_p += (total_player_defection / max_player_defection) * self.total_player_defections_weight
        decision_p += (player_defection_rate) * self.player_defection_rate_weight
        decision_p += (rounds_played / max_rounds_played) * self.rounds_played_weight
        decision_p += (rounds_left / max_rounds_left) * self.rounds_left_weight
        decision_p += (score_diff / max_score_diff) * self.score_diff_weight

        # Normalize the probability to stay within [0, 1]
        decision_p = max(0, min(1, decision_p))

        #true indicates defection, false indicates cooperation
        if random.random() < decision_p:
            return False  # Cooperate
        else:
            return True  # Defect

    def binary_to_decimal(binary_str):
        """
        Convert a binary string to a decimal integer.

        Parameters:
        binary_str (str): The binary string to be converted.

        Returns:
        int: The decimal integer equivalent of the binary string.
        """
        binary_str = binary_str[-5:]
        return int(binary_str, 2)