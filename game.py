import random


def game():
    number_of_guesses = 1
    lucky_number = random.randint(1, 100)
    print('lucky number is: ' + str(lucky_number))
    while True:
        guessed_number = int(input('Guess a number between 1 and 100: '))
        if guessed_number == lucky_number:
            print('bingo')
            break
        elif guessed_number > lucky_number:
            print('too high')
        elif guessed_number < lucky_number:
            print('too low')
        number_of_guesses += 1
    print('Number of guesses is: ', number_of_guesses)
    return number_of_guesses


