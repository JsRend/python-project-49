import random

from brain_games.games.brain_engine import starting_game, greeting

NUMBER_ROUND = 3
UPPER_BOUND = 50
LOWER_BOUND = 0

ANSWERS = dict({0: 'yes', 1: 'no'})


def even_game():

    user_name = greeting()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for count in range(int(NUMBER_ROUND)):

        random_number = random.randint(LOWER_BOUND, UPPER_BOUND)
        correct_answer = (ANSWERS.get(random_number % 2))

        if starting_game(random_number, correct_answer, user_name):
            continue
        else:
            return 0

    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    even_game()
