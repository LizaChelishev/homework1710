import game

min_number_of_guesses = 0
for round in range(0, 3):
    number_of_guesses = game.game()
    if min_number_of_guesses == 0 or number_of_guesses < min_number_of_guesses:
        min_number_of_guesses = number_of_guesses
        best_round = round + 1
print('The minimum number of guesses is: ' + str(min_number_of_guesses) + ' in round: ' + str(best_round))

