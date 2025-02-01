from player import Player

table_init_magnitude = 1
rounds_per_game = 20

player = Player(table_init_magnitude, rounds_per_game)

print(player.opp_history_weight)
print(player.self_history_weight)

print(player.get_decision("0101", "1010"))